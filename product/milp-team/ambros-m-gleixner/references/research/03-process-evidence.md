# Ambros M. Gleixner · 03 Process evidence (what he actually does)

- **Researcher**: Ambros M. Gleixner (living). Diplom TU Berlin 2008; researcher at Zuse Institute Berlin (ZIB) 2008–2015; PhD TU Berlin 2015; head of the ZIB research group "Mathematical Optimization Methods" 2015–2023; professor at HTW Berlin since 2020 and affiliated researcher of the ZIB division Mathematical Algorithmic Intelligence (homepage, S29). SoPlex and SCIP developer, VIPR initiator, first author of MIPLIB 2017. DBLP 07/3479, ORCID 0000-0003-0391-5903.
- **Dimension**: nuwa research-craft Phase 1, research agent 03 of 06: process evidence. This file covers behaviour that is visible in code, commit histories, test scripts, experiment sections, version changes, issue and pull-request threads, mailing-list answers, corrections and dropped work.
- **Research date**: 2026-11-08.
- **Sources consulted**: 35 opened and read in full or in part (S1–S34 and S39). A further 15 works (S35–S38, S40–S50) are named only with identifiers checked through Crossref, DBLP or arXiv metadata in this run; they are marked "not read". WebSearch calls used: 0 (everything came from curl, the GitHub API via `gh`, the arXiv and Crossref APIs, and WebFetch).
- **Local corpus**: `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep`, so there was no user-supplied material. `private/` was not opened.
- **Access limits (not bypassed)**: the ZIB report server (opus4.kobv.de) and OpenReview (forums and API) answered with bot challenges. Neither was circumvented, so ZIB-Reports that exist only there and the NeurIPS 2021 reviews are listed under Gaps.
- **Tags**: [stated] = what Gleixner wrote or said about how he works ("(co-authored)" when the text has co-authors). [practice] = what papers, code, commits or records show was actually done; "(group)" when the work was done mainly by students or postdocs in his group. [observed] = what others recorded (bug reporters, other maintainers). [inferred] = my inference, not established. Each item also says primary or secondary.
- **Attribution caveat (read first)**: from about 2016 almost every paper is first-authored by a student or postdoc (Eifler, Hoen, Mexi, Chmiela, Bestuzheva, Ghannam, ...). Gleixner's own hands are visible in: the single-authored PhD thesis (S10); the two-author papers with D. E. Steffy (S11; S44, S45 not read); the MIPLIB 2017 lead authorship (S8); 1,071 SoPlex commits, 1,648 SCIP commits and 59 commits to the VIPR checker (S2, S4, S5); his code-review and pull-request comments; and 262 SCIP mailing-list posts (S25). Items built on student-led papers are tagged "(group)".
- **Quotation policy**: the papers and the thesis are copyrighted. Verbatim fragments are kept short (under 15 words) and appear only where the wording itself is the evidence; everything else is paraphrased with section and page references. Commit subjects are cited as identifiers.

---

## 0. Era and resource context (timeline used for every item below)

| Period | Role / setting | Compute, tools, team | Evidence |
|---|---|---|---|
| 2004–2008 | Studies in Bayreuth (Vordiplom 2004) and TU Berlin (Diplom 2008, open-pit mining by IP). UNSW honours project with G. Froyland | — | S29, S30 |
| Sep 2008–2015 | Research assistant at ZIB. His first SoPlex commit, a maintenance fix, is dated 2008-09-04, in his first year there. Iterative refinement (IR) in SoPlex from June 2012; the rational solver in SoPlex 2.0 (Feb 2014) | Thesis runs on a cluster of Xeon `X5672` (3.2 GHz, 48 GB), one job per node; QSopt_ex 2.5.10 as the exact-LP competitor; SCIP and SoPlex in C/C++, Python evaluation scripts | S4, S10 §1.3.1 |
| 2015–2023 | Head of the research group "Mathematical Optimization Methods". In his July 2017 CV the group had 2 senior researchers, 10 research assistants and 4 student assistants. MIPLIB 2017 (2016–2019), VIPR (2016), SCIP 5/6 era | MIPLIB 2017 data: 8 solvers, 4 h limit, about 40 CPU years on two ZIB clusters. Exact-MIP runs on Xeon E5-2660 v3 / Gold 5122 clusters | S30, S8 §4.6, S3, S13 §4.1 |
| 2020–present | Professor at HTW Berlin; affiliated researcher at the ZIB division Mathematical Algorithmic Intelligence | 2025: integrates exact SCIP into mainline SCIP 10.0 himself (411 SCIP commits that year). VIPR checker maintained jointly with A. Hoen | S29, S5, S2 |
| Oct 2026 | Third parties audit his VIPR checker, one of them with a Lean 4-verified checker (LeanVIPR). One PR text carries an AI coding-assistant attribution line | Formal-methods and AI-assisted code review now available to outsiders | S2 (PRs #24, #25, #28) |

---

## 1. Research taste: what counts as worth doing (behavioural evidence)

**PE-01. Correctness of solver output is the axis of his own programme, followed for about 15 years.** [practice] [stated] primary
- The practice is a continuous chain of his own and his group's projects:
  - SoPlex IR (commit "implemented iterative refinement", 2012-06-08; S4);
  - the rational SoPlex 2.0 solver (2013–2014 commits, CHANGELOG "27 Feb 2014 - Release 2.0.0"; S4);
  - the VIPR certificate format and checker (Nov 2016; S1, S3);
  - exact SCIP with presolving, repair heuristic and certificates (2021; S12);
  - safe Gomory mixed-integer (GMI) cuts (2023; S13);
  - precision boosting inside IR (2023/2025; S14);
  - delta debugging for MIP solvers (2024; S15);
  - an a posteriori exact check of floating-point branch-and-bound decisions (2024/2025; S16);
  - the exact solving mode with VIPR certificates in SCIP 10.0 (Nov 2025; S19 §3.1);
  - a numerically safe branch-price-and-cut for an application (2026; S20).
- Stated: his homepage calls exact LP and IP over the rationals a growing interest. It says he is currently "most actively working on a algorithms and software for verifying the correctness" (sic) of IP results with VIPR, together with making SCIP an exact MIP solver (S29, read 2026-11-08).
- Context: ZIB's SCIP/SoPlex project, BMBF Research Campus MODAL funding (acknowledged in S12, S13, S16, S18).

**PE-02. Experiments are meant to explain behaviour, not to win a race.** [stated, single-authored] [practice] primary
- Stated: thesis §1.3 (p. 10) says his interest is not purely competitive testing but analysing the reasons for algorithmic behaviour by "controlled scientific testing". It cites Hooker 1995 (S37).
- Practice: later computational sections open with a numbered list of questions to answer:
  - the LP-oracle paper lists three questions: how many instances each algorithm solves; how much time goes into rational factorization and reconstruction; how many refinements are needed (S11 §6, p. 20);
  - the exact-MIP status update has "three main questions": component attribution, impact of presolving and heuristics, certificate overhead (S12 §4, pp. 6–7);
  - the safe-GMI paper again has "three main questions" (S13 §4, p. 20).

**PE-03. He treats test-set curation as research in its own right, with its limits stated.** [practice] [stated (co-authored)] primary
- Practice: MIPLIB 2017 was compiled as a sequence of optimization problems: diversity-preselection MIPs, a collection MIP and a benchmark MIP over more than a hundred instance features and several clusterings (S8 §5, pp. 466ff.).
- Stated (co-authored, S8 pp. 445–446): average performance on the benchmark set is not a criterion for choosing a solver for a specific application. The process needed many manual and heuristic decisions with high impact, which is why the paper describes them in technical detail. The conclusion calls the result "only one of many possible and justified outcomes" (S8 §7, p. 485).

---

## 2. Problem choice and timing

**PE-04. New projects start from limitations he wrote down in earlier work.** [practice] primary
- IR to precision boosting: thesis §2.6 (pp. 55–56) says classical IR breaks down when the LP is too ill-conditioned for the floating-point oracle. It names QSopt_ex-style raising of the working precision as the remedy (S10). Eight years later his group combines precision boosting with IR (arXiv 2311.08037, 2023; IJOC 2025; S14).
- Certificates to debugging: the 2016 VIPR paper's conclusion proposes approximate certificates from inexact data for debugging solvers and measuring numerical violations (S3, arXiv 1611.08832v1 §6). In 2024–2025 his group checks every critical floating-point B&B decision of SCIP in exact arithmetic (S16).
- Missing cuts to safe cuts: the 2021 status update ends by saying the performance gap to floating-point solvers is still large. It names numerically safe cutting planes as the missing technique (S12 §4, p. 12). The safe-GMI paper follows in 2023 (S13).
- Proof assistant: the same 2016 conclusion proposes converting certificates for formal verification by a proof assistant such as HOL Light (S3). In 2026 a third party built LeanVIPR, a VIPR checker whose soundness is proved in Lean 4 (S2, comment on PR #25). No such work by his own group was found.

**PE-05. A research line is pursued until it ships in the default distribution, over a decade.** [practice] primary
- Exact MIP timeline:
  - 2013: the Cook–Koch–Steffy–Wolter framework (S35);
  - Nov 2016: the certificate-printing version for VIPR is "available from the authors by request" (S1 experiments/README.md);
  - 2020–2022: per-paper tarballs of a development version published by L. Eifler (S24);
  - later mirrored as the branch `exact-rational` of scipopt/scip (S24);
  - Nov 2025: shipped as the exact mode of SCIP 10.0 (S19 §3.1);
  - Nov 2025: Gleixner himself updates the Homebrew formulas so that SoPlex and SCIP build with MPFR and the exact mode. Each formula gets a test of exact solving (Homebrew PRs #256157 and #256158; S27).
- Context: one long-lived research campus (MODAL) and a solver team. Most code was written by doctoral students; he did the final integration (PE-38).

**PE-06. He chooses applications where wrong answers are costly or where a solver's tolerance hides errors.** [practice] primary
- Wireless network design models with tiny signal-to-interference coefficients. Exact LP/MIP methods are used to check whether designs that floating-point solvers report as feasible really are feasible (S21, abstract and §1).
- Machine-assisted proofs: exact SCIP and VIPR for finite cases of Chvátal's conjecture, plus Coq to check that the certificate encodes the intended model (S18, abstract and §2).
- [inferred] Both serve as showcases for the exactness programme. His 2017 CV lists an earlier Siemens internship on efficient planning of wireless networks (S30), a possible origin of the first topic (not verified). The SAP supply-chain project led to a separate, non-exact paper (S40).

---

## 3. Idea generation (as visible in what gets built first)

**PE-07. The cheapest possible experiment comes first.** [stated, single-authored] [practice] primary
- Thesis §3.2.1 "A First Experiment" (pp. 64–65, S10). Before designing new exact-LP algorithms he warm-starts the existing exact solver QSopt_ex from the basis that IR produced. In his words this "only requires linking two out-of-the-box libraries" (quotation marks inside the original omitted).
- In the same experiment he notes that comparing against plain QSopt_ex would be biased, because the floating-point engines differ, for example in presolving. The reference point is therefore QSopt_ex warm-started from the basis of SoPlex at double precision (S10 p. 64).

**PE-08. He combines the competitor's method with his own instead of replacing it.** [practice] primary (group for the 2023+ items)
- QSopt_ex's incremental precision boosting is put inside the SoPlex IR loop (S14, abstract).
- Proof logging is taken from SAT and pseudo-Boolean solving: VeriPB-style certification of MIP presolve, with J. Nordström (S22). Pseudo-Boolean conflict analysis comes into MIP (CP 2023; DBLP S31).
- Delta debugging is explicitly imported from the SAT and SMT solver community (S15 v5 §1, p. 2).

**PE-09. A known feasible solution is the debugging oracle.** [practice] primary
- Mailing list, July 2018, thread "Infeasible with C-API but feasible with Interactive Shell": he suggests writing the shell's solution to a file and reading it in the API code. If it is rejected, the violated constraint points to the problem. "Expert mode" is SCIP's debug-solution check (`-DDEBUGSOL=on`, `misc/debugsol`), which reports where the solution gets cut off (S25, 2018-July/003465).
- The same oracle runs through his code:
  - "check debug solution in prop_genvbounds" (SCIP commit, 2013-12-24, S5);
  - MIP-DD's design: every reduction must keep a fixed reference solution feasible (S15 §2; README of the IJOC repository);
  - the 2025 exact check of every B&B decision (S16).

---

## 4. Experiments and execution

### 4.1 Measurement discipline

**PE-10. Timing jobs run alone on a machine.** [stated] [practice] primary
- Thesis §1.3.1 (p. 10): one job per cluster node, to avoid mutual slowdown of parallel processes distorting running times (S10).
- VIPR 2016: jobs "run exclusively to ensure accurate time measurement" (S1 experiments/README.md; S3 v2 §5).
- Chvátal paper: one job per node, 12 h limit (S18 §4).
- SCIP 10.0 report (co-authored): a single run on each machine, single-threaded (S19 §2.1).
- Exception: see C4. The MIPLIB 2017 data collection ran two jobs per node.

**PE-11. Averages come with an explicit shift, and significance is tested separately from magnitude.** [stated, single-authored] [practice] primary
- Thesis §1.3.2–1.3.3 (pp. 10–12):
  - shifted geometric means, citing Achterberg's thesis, Achterberg and Wunderling 2013 (S38) and Hendel;
  - a one-sided Wilcoxon signed-rank test on log-ratios, SciPy implementation with `zero_method="pratt"`, at the 5% level;
  - the explicit warning that significance ignores magnitude: a negligibly small but consistent speed-up would pass as highly significant although it is practically irrelevant (S10 p. 12).
- Practice in the thesis's branching chapter (§7.4.4–7.5, pp. 168–172):
  - subgroups "all solved" and ≥1/10/100/1000 s, defined by excluding instances easy for all settings;
  - he notes that this comparison favours SCIP's default;
  - lower-bound speedups computed with the instances solved by only one setting;
  - the COVER rule's gain reported as not statistically significant (PE-27).
- The shifts vary between papers (see C8): 10 s and 1 MB (S1, S3), 0.001 s and 100 nodes (S12 §4), 1 s and 100 nodes (S13 §4.1; S19 §2.1).

**PE-12. Performance variability is handled with seeds and permutations, and only where it can matter.** [practice] primary
- Three random seeds, each instance–seed pair counted as one observation; the original framework, which has no seed option, runs with one seed (S12 §4).
- 132 MIPLIB 2017 benchmark instances × 3 seeds = 396 runs (S13 §4.1).
- Original plus a permuted copy of every instance (S16 §3.1).
- Test-set maintenance after 5-seed runs: SCIP commits "move 25 instances from mipdev-hard to solvable after partial 5 seed run" (2017-11-13) and "move 22 instances ... after 5 seed run" (2017-11-16) (S5).
- He also says where seeds are not needed: the certificate overhead is "not subject to performance variability", so it is measured with one seed (S13 §4.4, p. 24).
- SCIP 10.0 (co-authored): 3 seeds for MILP, 5 for MINLP (S19 §2.1).

**PE-13. Overheads are measured only on instances that both variants solve.** [practice] primary
- Certificate overhead uses only instances solved by both versions, because timeouts "would bias the results in favor of the certificate" (S12 §4, p. 11).
- In the GMI paper the time limit with verification is raised to 6 h so that the same instances are solved (S13 §4.4, p. 25).
- The LP-oracle paper calls an algorithm "fastest" if it is within 5% of the best time, to absorb measurement noise (S11 §6.2, footnote 2).

### 4.2 Baselines and test problems

**PE-14. The baseline is constructed to be fair, and the remaining mismatch is stated.** [practice] primary
- Exact versus floating-point GMI cuts: he first builds a reduced floating-point SCIP with every plugin that exact SCIP lacks switched off. Cuts are then compared within that baseline (`fpnocuts` / `fpgmi` against `nocuts` / `safegmi` / `densmall`; S13 §4, pp. 20–21).
- Old versus new exact framework: the same QSopt_ex version as the original. He states that the floating-point LP solver had to differ (CPLEX 12.3.0 against 12.8.0) and argues why this matters little (S12 §4, p. 7).
- SCIP 10.0 is compared with both the previous major release (9.0) and the latest bugfix release (9.2.4), so that robustness fixes and new features are separated (S19 §2, co-authored).

**PE-15. The same curated exact-MIP test sets are reused for 14 years.** [practice] primary (group)
- "fpeasy" (57 instances) and "numdiff" (50 instances) were curated by Cook, Koch, Steffy and Wolter for IPCO 2011 (S36). They are reused:
  - for VIPR in 2016 (S3);
  - for the 2021 status update (S12 §4);
  - for the 2025 B&B-decision analysis (S16 §3.1, reference [6]).
- Later papers add the MIPLIB 2017 benchmark set as a "more ambitious" complement (S12; S13).
- [inferred] This keeps a long series comparable across tool generations. The price is that the hard set stays fixed at 2011 numerics.

**PE-16. Large LP test beds are assembled from public sources, with every exclusion named.** [practice] primary
- Thesis §1.4.1 (p. 13):
  - sources: Netlib including kennington, Mittelmann, Mészáros, and the LP relaxations of COR@L and all MIPLIBs;
  - obvious duplicates removed; 1,242 primal and dual feasible LPs;
  - blanks in names replaced so that QSopt_ex can parse them;
  - 7 instances excluded for the 48 GB memory limit, named in footnote 26;
  - 33 instances that floating-point SoPlex cannot solve in 2 h removed, named in footnote 27;
  - result: 1,202 LPs.
- The same 1,202 LPs are reused in the 2019 oracle paper (S11 §6.1).
- The construction is visible in the SoPlex repository (S4, `check/`, 2014):
  - "add irpaper.test";
  - "add coral instances to irpaper.test and remove duplicates";
  - "add script support for running perPlex and QSopt_ex after SoPlex";
  - separate cluster scripts for the two competitors (`check_cluster_perplex.sh`, `check_cluster_qsoptex.sh`).

**PE-17. Benchmark admission rules exclude ambiguity, not difficulty.** [practice] primary
- MIPLIB 2017 benchmark suitability, criteria B.1–B.9 (S8 §5.1, pp. 467–468):
  - solved by at least one solver in 4 h, to avoid the MIPLIB 2003 situation of benchmark instances unsolved for 15 years;
  - at least 10 s with half of the solvers;
  - limits on dynamism and coefficient size;
  - consistent results across all solvers;
  - no indicator constraints;
  - finite optimum or infeasible;
  - at most 10^6 nonzeros.
- Table 7 counts exclusions per criterion; 334 instances were excluded for inconsistent results.
- He applies the same filters in his own papers:
  - instances where floating-point and exact solutions disagree are excluded from gap-closed statistics (S13 §4.2, p. 21);
  - SCIP 10.0 (co-authored) drops "numerically inconsistent" instances from the "all" subset (S19 §2.1).

### 4.3 Verification layered on top of every experiment

**PE-18. Results are cross-checked independently of the solver that produced them.** [practice] primary
- MIPLIB 2017 (S8 §4.7, pp. 464–465):
  - every reported solution is checked against the original MPS file in GMP arithmetic with the MIPLIB solution checker;
  - its violation measure was changed from purely absolute to a mixed absolute and relative rule, with tolerance 10^-5;
  - cross-solver inconsistencies (a verified solution better than another solver's dual bound) are detected with the log parser IPET;
  - example given: on bc1 one solver of eight claimed a suboptimal value as optimal.
- MIPcc23 (committee rules in his repository; S6 RULES.md):
  - dual bounds verified against exact precomputed values with tolerance 10^-5·max(|z|,1);
  - primal solutions checked at 10^-5 absolute violation and 10^-4 integrality;
  - an invalid bound or infeasible solution costs twice the worst rank.
- Chvátal paper: four components: model, exact SCIP, VIPR check, and Coq to verify the input data of the certificate (S18 §2, Fig. 1).

**PE-19. Certificates are used to find wrong reasoning even when the answer is right.** [practice] primary
- In the 2021 status update, the certificate showed that the original exact framework claimed infeasibility of instance x_4 (numdiff) at the root for an incorrect reason, although the instance is infeasible (S12 §4, p. 11).
- The 2025 B&B analysis classifies every leaf decision. Errors on FPEasy: 2 of 57 instances, with dual-side errors only. On NumDiff, 25 (original) and 27 (permuted) of 50 instances had a fully correct solving process (S16 Table 1). The conclusion singles out sub-problems that are infeasible in exact arithmetic: there the floating-point solver sometimes finds slightly violated solutions and prunes nodes on that basis. Tighter feasibility tolerances fix this only partly (S16 §4).

### 4.4 Debugging

**PE-20. When answering users he isolates the cause by swapping components.** [practice] primary
- Mailing list, March 2018 (S25, 2018-March/003328), on numerical trouble in a column-generation set-covering model:
  - he asks how large the big-M is;
  - he notes that a missing dual solution explains why reduced-cost pricing is not called;
  - he asks what the dual-bound column says;
  - he advises updating SCIP/SoPlex and trying another LP solver to tell "a systemative formulation or an LP solver issue" (sic) apart.
- August 2014 (S25, 2014-August/002119): asked why an optimal solution has a variable with negative reduced cost, he explains it by the dual feasibility tolerance (numerics/dualfeastol, −1e-7 by default in SCIP 3.1) and does not treat it as a bug.
- February 2011 (S25, 2011-February/000628): he diagnoses a SoPlex limitation (no primal ray for unbounded LPs), implements the ray in the developer version and sends the user a patched SoPlex.
- 262 posts on the SCIP list, 2009–2024; third after G. Gamrath (383) and S. Vigerske (323) among 5,106 posts from Dec 2006 to Sep 2026. Peaks: 42 posts in 2014 and 40 in 2020 (counted from the monthly author indexes, S25).

**PE-21. Reports to other teams' solvers come with reproducible commands and an argument for keeping debug and optimized builds identical.** [practice] [observed] primary
- Jan–Mar 2023 he opened six pull requests on HiGHS (S26). In the same period he was developing SCIP's HiGHS LP interface himself: SCIP commits "fixes to lpi_cpx.c and nonlinear unit tests from lpi_highs development" (2023-01-13) and "add lpi_highs.cpp on master" (2023-12-08) (S5). The pull requests:
  - #1102 "fix applyScalingToLpRow", found by SCIP's unit tests;
  - #1121 (assert relaxations);
  - #1175 (relative feasibility tolerance in primal bound shifting);
  - #1182 (dual tolerance in `computeExactDualObjectiveValue()`): triggered on MIPLIB 2017's milo-v12-6-r2-40-1 when SCIP runs with a dual tolerance of 1e-10;
  - #1184 (small matrix values introduced by presolve, with the exact command line to reproduce) and its follow-up #1195.
- In #1184 he argued that debug and optimized builds should not behave differently, because that makes debugging harder.
- Two of the six were merged (#1102, #1175). The maintainer superseded or declined the others: #1121 by his own #1122; #1184 with his own analysis of the small values; #1182 closed as stale in Feb 2025.
- On #1195 the maintainer wrote "Please leave me to write things like this"; Gleixner answered "Okay, just wanted to help." [observed, both quotes verbatim]

**PE-22. His group turns every hard bug into a minimal instance and a regression test.** [practice] primary (group)
- MIP-DD shrinks a bug-triggering MIP while the bug still reproduces, using nine modifiers. Reduced instances are added to SCIP's regularly tested set `check/instances/Issue` (S15 v5 §3, p. 8).
- The IJOC code and data repository ships the reduced instances and logs for each case study, plus SCIP's 8.x bugfix list (S15, github.com/INFORMSJoC/2024.0844).
- Context: the MIP-DD case studies ran on a MacBook Air M2 (S15 §3). They measure reduction time, not solver performance.
- Gleixner has no commits in the MIP-DD repository (S15, git log). His role was supervision and authorship.

**PE-23. He fixes his own measurement tools as readily as solver code.** [practice] primary
- `check/evaluation.py` (SoPlex, 2014-03-21): the consistency check against reference values compared a numeric value with the string 'optimal'. It could never fire, so wrong objective values were never flagged. Fixed, and an "inconsistents" count was added to the summary (S4).
- `check/compare.py` (SoPlex, 2014-10-23, commit 45402499): the incremental shifted geometric mean used the wrong exponent and did not subtract the shift. Fixed (S4).
- SCIP `check.awk` (2013-11-12): "fixed parsing of dual bound in check.awk (was wrong for maximization)" (S5).
- [inferred] Both SoPlex fixes predate the final IR-paper runs, since `irpaper.test` was assembled in Sep–Oct 2014. Not verified: the thesis log files were not opened.

**PE-24. Try, measure, revert, and say so in the log.** [practice] primary
- SoPlex 2008-12-19: he undid his own earlier change to `maxInfeas()`, noting it "was WRONG since r1.33". 2010-08-11: "last check-in contained wrong modification in maxInfeas() -- remove again" (S4).
- SoPlex, July 2014, months after the 2.0 release: he reverts three of his own recent rational-solver commits, "make parameter EQTRANS true again", "remove code for restricting inequalities from solverational.cpp" (both 2014-07-14) and "only apply rational factorization if parameter RATFAC == true" (2014-07-16). Parameters `bool:eqtrans` and `bool:ratfac` then appear in the SoPlex 2.2 release notes (June 2015; S4).
- SCIP, December 2013: "relax cutoff bound in obbt propagator for numerical stability" (12-20), reverted on 12-25 (S5).
- SCIP default switches for his own propagators: OBBT activated at the root and generalized variable bounds at every node (2012-05-14), then "deactivated prop_genvbounds by default" (2012-10-26) (S5). In today's master `prop_genvbounds.c` has frequency 1 (active) and `prop_obbt.c` frequency 0 (root) (S5). When genvbounds was reactivated was not traced.

### 4.5 Reproducibility artefacts

**PE-25. He archives code versions, logs and per-instance results with the paper.** [stated] [practice] primary
- Thesis §1.3.1: the exact versions used and the log files were archived (S10 p. 10). Appendix A holds instance-wise tables (pp. 201ff.).
- VIPR, Nov 2016: gzipped certificates for every instance on his ZIB web space. The supplementary page lists time, nodes, sizes and the verified bound range for each instance (S1 experiments/README.md). He committed the tables himself on the day the repository was created (2016-11-20/23).
- Exact SCIP: one tarball per paper (0.1 for IPCO 2021, 0.2 for the 2022 Math. Program. paper, 0.3 for safe GMI cuts) (S24 README, written by Eifler).
- IJOC code and data repositories for MIP-DD, PaPILO and cut-based conflict analysis (S15; S39; DOI 10.1287/ijoc.2024.0999.cd for S41). The B&B analyzer is public at github.com/alexhoen/bnbanalyzer (S16 §3.1).
- MIPcc23: public instance series, a solution checker and an evaluation script in his repository. The hidden series were added after the competition (commit "Add hidden datasets and associated metadata", 2023-04-16; S6).

---

## 5. Judging results: negative results, corrections, criticism, abandoned work

**PE-26. Negative and unflattering numbers stay in the paper.** [practice] primary
- VIPR 2016: certificate-printing SCIP is much slower. Easy-all time 63.3 s against 190.9 s in v2. Many runs hit the 10 GB certificate limit (the "memout" rows). Timeouts are reported as their own row, not hidden (S3 v2 Table 1).
- 2021: the certificate overhead is +101% on fpeasy and +51% on numdiff, called "not negligible". Presolving cannot yet be certified because PaPILO does not support it (S12 §4, Table 7).
- 2023: presolving is still uncertified, so only the presolved problem is verified. One instance (mas74) took almost 8 h with verification (S13 §4.4).

**PE-27. What is significant is kept, what is not is quietly dropped.** [practice] primary, partly [inferred]
- Thesis Ch. 7 tested three MINLP branching rules (S10 §7.4–7.5, pp. 165–172):
  - NLSCORE: −17.1% time on instances solved by at least one setting, highly significant;
  - VARTYPE: solves more instances but is slower on the others; with the extra instances −3.6%, significant;
  - COVER: dominated by NLSCORE and not significant.
- Today's SCIP keeps NLSCORE as `nlscoreweight` with default 0.1 in `branch_relpscost.c` (S5).
- A GitHub code search for "splitting cover" in scipopt/scip finds nothing (S5, 2026-11-08). [inferred] COVER branching was not kept.
- Whether VARTYPE survives could not be established: `branch_pscost.c` compares variable types, but no link to the thesis rule was found.

**PE-28. Claims are recalibrated between preprint and final version.** [practice] primary
- MIP-DD (S15):
  - v1 (May 2024) said a preliminary version had tracked down "the majority of the bugs fixed since version 8.0.3". Its abstract claimed about 71.4% more bugfixes than in the same period before;
  - v5 (Apr 2025) and the IJOC version replace both with a count: MIP-DD helped to reduce the reproducing instances of "24 among all the 51 MIP-related and finally fixed bugs" in SCIP 8.0.1 to 8.1.1. That is under half (v5 §3, p. 8; abstract);
  - the title changed from "A Delta Debugger" to "Delta Debugging".
- VIPR (S3):
  - arXiv v1 (Nov 2016, ZIB-Report 16-58): Table 1 covers 106 instances. nw04 is excluded because the tightening tool viprttn ran out of memory;
  - v2 (revised March 2017, the IPCO version): 107 instances. viprttn now reorders derivations by a depth-first topological sort to reduce peak memory (v2 §5), and all timings changed (e.g. easy-all viprttn time 25.8 s → 8.9 s);
  - [practice] he fixed the tool rather than keep the exclusion. For what the public repository and the supplementary page show, see C3.

**PE-29. Released benchmarks are corrected in public, with the method reused for the correction.** [practice] primary
- Two MIPLIB 2017 benchmark instances (neos-5075914-elvire, neos-3754224-navua) turned out to be numerically unstable after release. A variant of the benchmark-selection MIP computed a minimal exchange that keeps the balance requirements, and benchmark v2 was published in June 2019 (S8 §7, pp. 485–486; S9 news 2019-06-24, five instances exchanged).
- Further corrections in the MIPLIB news log (S9):
  - 2020-05-24: the download Benchmark.zip now "correctly" contains benchmark-v2 instead of v1. [inferred] The packaged set may have lagged the June 2019 update by up to eleven months; the news entry gives no start date;
  - 2019-01-28: 29 collection files differed from the MIPLIB 2010/2003 files of the same name and were corrected;
  - 2023-07-28: supportcase22, tagged infeasible, was found feasible, and a wrong file of bley_xl1 was replaced;
  - 2024-07-18: one instance "corrected from hard to open".
- The site lists Gleixner and Mark Turner as current maintainers. Solution-file release 37 came on 2026-09-24 (S9 index).

**PE-30. Latent soundness bugs in his trusted checker survived for years.** [practice] primary (verified by me in the code)
- The VIPR checker `viprchk` is the component that is supposed to be trusted. The code published with the 2016 paper (archived repo ambros-gleixner/VIPR, commit c39fd63c, `code/viprchk.cpp`) contains:
  1. **Solution check**: `processSOL()` loops over j but tests `constraint[i]`, i being the solution index. A claimed solution is therefore checked against one constraint only. Fixed in `viprchk.cpp` by A. Hoen in scipopt/vipr PR #5 (merged 2024-12-04). The CHANGELOG entry for VIPR 1.1 reads "consider all constraints for checking the feasibility of solutions". The bug is still present in the archived repository's master and in `viprchk_parallel.cpp` on scipopt/vipr master 99eec19 (line 870) (S1, S2).
  2. **Unsplitting**: the assumption list of the second branch was intersected with that of the first instead of joined to it, so assumptions used only in the second branch were dropped. Gleixner fixed this himself on 2023-04-04 (commit 56211850 "fix assumption handling in unsplitting"; S1). The fix was not carried over to `viprchk_parallel.cpp` (S2, PR #28 §1).
  3. **Rounding over continuous variables**: `Constraint::round()` checks only that coefficients of integer variables are integral and ignores nonzero coefficients on continuous variables. This is present in the 2016 code and still on master (S1, S2 `viprchk.cpp` lines 1634–1662). Reported in Oct 2026 (PR #24).
  4. **Unsplit with fractional right-hand side**: `canUnsplit` checks that the two right-hand sides differ by 1 but not that they are integral. Present in 2016 (S1); reported in Oct 2026 (PR #24).
  5. **Tautology check for infeasibility proofs**: found and fixed by Gleixner himself in June 2025. For infeasible relation-to-prove certificates the check always passed because two variables were uninitialized (PR #15; S2).
- [observed] The October 2026 reporters showed that the master checker accepts certificates that purport to prove feasible problems infeasible (PR #24). A third party building LeanVIPR, a checker proved sound in Lean 4, confirmed the rounding hole independently and added a wrong-optimum example (comment on PR #25). PR #28 lists further holes, including `{ sol }` cut-offs and malformed counts read with `atoi()`.
- [inferred] The 2016 claim that `viprchk` found no case of an infeasible solution being accepted (C1) was made with bug 1 in the checker. Whether any published certificate was affected was not examined (Gaps).

**PE-31. How he answers criticism of his own verification software.** [practice] [observed] primary
- External PR #24 was opened on 2026-10-27 12:12 UTC. Gleixner replied about 17 hours later: "Thank you for the fixes! I will prepare a small revision" and said he would ping the reporter for review before the final merge (S2).
- The next day he opened PR #25 with his revisions and asked the reporter to double-check. The reporter confirmed that the revision was correct and that it fixed a further null-pointer case (trashed second assumption), then added four commits and a stacked PR #28.
- As of 2026-11-08 none of #24/#25/#28 is merged (S2, state "open").
- Earlier he fixed what his own use exposed:
  - early termination (PR #14, 2025-05-28): a valid certificate failed because redundant derivations followed the proof, so the checker now tests every assumption-free derivation against the bound to prove;
  - the tautology fix (PR #15, 2025-06-18), with the matching change in SCIP's internal GitLab cited as MR 3894;
  - lazy canonicalization when domination checks fail (Mar–Apr 2025);
  - all recorded in the VIPR 1.2 release notes (S2 CHANGELOG).
- Context: of the 147 commits in scipopt/vipr (2016–2026, including the history imported from the archived repository), 59 are his. A. Hoen has 52 under two names, L. Eifler 20 and D. E. Steffy 14 (S2).

**PE-32. Work that never reached print, or took years to.** [practice] primary (identifiers checked; texts mostly not read)
- ZIB-Report 12-36, "Factorization and update of a reduced basis matrix for the revised simplex method" (Oct 2012, single-authored; listed in his 2017 CV, S30). A Crossref title-and-author search on 2026-11-08 finds no journal version. Not read (ZIB OPUS blocked). [inferred] An abandoned simplex-engine idea.
- Preprints without a Crossref record as of 2026-11-08 [inferred: unpublished, or published under another title]:
  - arXiv 2403.13567 "Certified Constraint Propagation and Dual Proof Analysis in a Numerically Exact MIP Solver" (2024). It is nevertheless cited as reference [18] for a feature shipped in SCIP 10.0 (S23; S19 refs);
  - arXiv 2311.03877 "A proof system for certifying symmetry and optimality reasoning in integer programming" (2023);
  - the full SONC paper arXiv 2304.12145 (2023); its 4-page HUGO 2022 version is arXiv 2211.05518;
  - arXiv 2512.17551 "Clique Probing for Mixed-Integer Programs" (Dec 2025, recent);
  - all checked via the arXiv metadata harvested in this run (S32) and Crossref (S33).
- Slow paths: the supply-chain report ZIB-Report 16-45 (Nov 2016, "Submitted" in the 2017 CV) appeared in J. Comput. Math. 37(6) (S40). The ISSAC 2012 IR paper (S45) became the IJOC 2016 article (S44) four years later. MIPLIB 2017 took 14 months from submission to acceptance (received 25 July 2019, accepted 10 Sep 2020; Crossref, S8).
- Pieces cut during integration: the 2025 exact-SCIP revision removes the plugin `branchexact.*` and "unfinished additions in README.md and doc/xternal.c" (S5 commits, March 2025). In the 2022 VIPR port, a file that Cheung had written years earlier was dropped from the README. Eifler's comment says it "was never meant to be published I guess?" (PR #1 review, S1).

---

## 6. Expression

**PE-33. Papers report denominators, subsets and the test set in the headline claim.** [practice] primary
- Abstract numbers always come with a test set and a limit:
  - a 6.6× speed-up over the original framework and 2.8 times as many MIPLIB 2017 benchmark instances solved within two hours (S12);
  - 21.5% more instances and 26.8% less time on the MIPLIB 2017 benchmark (S13);
  - 24 of 51 bugfixes (S15 v5).
- Tables are split into all, solved, memout and timeout rows (S3), or into brackets and "both-solved" (S19).
- Instance lists for exclusions go into footnotes (S10 pp. 13, 64–65).

**PE-34. Supplementary material lives in the code repository, next to the checker.** [practice] primary
- VIPR's GitHub repository holds the format specification (v1.0 and, for the GMI paper, v1.1), the four tools, and the experiments page linking every certificate (S1 README).
- He reviews student documentation for completeness. In VIPR PR #1 (Aug 2022) he asked for a description of an undocumented term ("cutwidth"), an example call, documentation of the v1.1 extensions, and removal of the old makefile, and offered to test the build himself (S1, review comments).

---

## 7. Research organisation

**PE-35. He wrote SCIP's code-review checklist and kept revising it.** [practice] primary
- Commit 8201ee1d (2018-01-26, "add first merqe request template", sic) creates `.gitlab/merge_request_templates/Feature.md`. Checklist items:
  - documentation, CHANGELOG and coding style;
  - naming and placement of new methods;
  - user documentation;
  - coverage settings and unit tests;
  - makedist and both build systems;
  - ctest;
  - "Has performance impact been checked on mi(nl)pdev-solvable (if activated by default)?";
  - backwards compatibility and SCIP_APIVERSION for API changes.
- He revised it:
  - June 2018: "Is the code change correct?" became the first item; ctest named per LP solver (`jenkins ctest {soplex master,soplex bugfix,cplex,gurobi,mosek,xpress}`);
  - August and October 2020: questions rephrased as checkable statements; explicit `jenkins performance` commands; API-change items clarified. His edit of 2020-08-27 (e4e67068) also removed a clause requiring that a developer responsible for SAP be mentioned whenever a default parameter changes. Who had added that clause was not traced;
  - September 2021 (S5).
- The current default template, edited later by S. Vigerske, keeps this structure (S5, `.gitlab/merge_request_templates/Default.md`).

**PE-36. He maintains the internal benchmark sets behind the template's performance-check item.** [practice] primary
- SCIP commits (S5):
  - instances moved between `mipdev-hard` and `mipdev-solvable` after multi-seed runs (Nov 2017), and further moves in May–June 2018;
  - "update all.solu from MIPLIB2010 solu file and some Gurobi runs" (2017-11-16): reference values from a commercial solver;
  - coverage settings for new features such as sparsify presolve and symmetry before the SCIP 5.0 release (Nov 2017).
- Context: SCIP 5.0 (Dec 2017) and 6.0 (July 2018) releases, while he headed the research group.

**PE-37. Competitions and libraries are designed against gaming.** [practice] primary (committee)
- MIPcc23: the repository is in his account. He wrote the description (2022-10-30), clarified the rules on sequential solving of instance series and on what changes count (Nov–Dec 2022), and adjusted the score computation (2022-11-19) (S6 commits). The rules:
  - only open-source software;
  - one thread, 16 GB;
  - no look-ahead within a series;
  - organizers and their family members cannot enter, and students are explicitly encouraged;
  - hidden series chosen by the jury (S6 RULES.md).
- The competition paper says the time-limit and early-stop rules were meant "to close loopholes for the competition" (S7 §3, p. 7).

**PE-38. As group head and professor he still does the integration commits.** [practice] primary
- SCIP: 1,648 commits under his name, 10th of all authors. By year: 2017: 144, 2018: 134, 2020: 156, 2021: 165, 2025: 411 (S5).
- In 2025, 312 non-merge commits (411 with merges), 145 of them in March 2025, mostly on branch `exactip-revision`:
  - renames for consistency (e.g. "rename exact/enabled -> exact/enable for consistency", 2025-03-28);
  - removal of unfinished or unsafe parts ("mark reader_cip as not exact", "remove branchexact.*");
  - unit-test fixes and build-system work (S5).
- SoPlex: 1,071 commits, 2nd after M. Miltenberger. Peak in 2013–2014 (179 and 369), the rational-solver build-up; 20 commits again in 2025 (S4).
- Homebrew formula updates for the SCIP 10.0 / SoPlex 8.0 release (Nov 2025; S27).
- PaPILO: 7 commits; MIP-DD: none (S15, S39). He leads these papers but did not write their code.

**PE-39. Public GitHub repositories are mirrors; work happens on ZIB's internal GitLab.** [practice] primary
- VIPR 2016–2022 history: one commit "port current status from gitlab" (2022-07-22) by Eifler (S1). scipopt/vipr was created in Feb 2024 with "Commit current codebase from gitlab" (S2).
- ZIMPL PR #4 (2025-10-20): he reverts a merged external pull request so that it can be merged "in internal git" and the encoding errors fixed there (S27).
- VIPR PR #15 cites a SCIP merge request on git.zib.de (S2).
- [inferred] Public artefacts can lag the papers by years (C3).

**PE-40. A long-running two-person methods partnership next to the student pipeline.** [practice] primary (DBLP S31)
- The exact-LP theory and IR papers are with D. E. Steffy: ISSAC 2012 (with K. Wolter), IJOC 2016, IPCO 2017 (with K. Cheung), and the two-author IPCO 2019 / Math. Program. 2020 paper (S11, S31). Steffy also reviewed the IR documentation in SoPlex ("Dan's comments on iterative refinement documentation", 2012-07-27; S4).
- From 2018 the exactness line passes to doctoral students: Eifler (exact SCIP, GMI, precision boosting), Hoen (PaPILO, MIP-DD, B&B analysis), Borst. From 2023 cross-community co-authors join (J. Nordström, PB proof logging).

---

## Contradictions (kept, not reconciled)

**C1. A verification claim versus the verifier it rested on.** The 2016 supplementary page (still online, S1) says each certificate was verified and that `viprchk` found no case of exact SCIP pruning an optimal solution "or incorrectly accepted an infeasible solution". The checker published with it checked a claimed solution against one constraint only (PE-30 item 1). It also accepted continuous-variable rounding and fractional unsplits (items 3–4). [practice vs stated (co-authored)]

**C2. The design goal of trivially checkable certificates versus ten years of latent checker bugs.** The 2016 paper argues that certificates should be "as simple to verify as possible" to convince skeptics (S3 §1). The Chvátal paper presents the independent checker as a safeguard against solver bugs (S18, abstract). Yet the trusted checker's holes were found by the group's own later use (2023–2025) and by a formally verified outside checker in 2026 (PE-30). In 2016 he already listed formal verification as future work (S3 §6). [stated vs practice]

**C3. Final paper versus public supplement and code.** The IPCO version (S3 v2) reports 107 instances with an improved, topologically sorting viprttn. The GitHub supplementary page still shows the November 2016 table: 106 instances, nw04 excluded, older timings (S1 experiments/README.md, last edited 2023-09-27 for an instance-name fix). The public `viprttn.cpp` gained the topological sort only with the 2022 GitLab port (commit 03d6b615; the 2016 file has none; S1). From 2017 to 2022 the public repository therefore could not reproduce the paper's final table. [practice vs practice]

**C4. Exclusive-node timing rule versus the MIPLIB 2017 data campaign.** The thesis rule is one job per node to avoid distorted times (S10 §1.3.1). Benchmark papers keep it (PE-10). The MIPLIB 2017 performance data, used to define benchmark suitability ("at least 10 s with 50% of the solvers"), ran two jobs per node with 4 threads each (S8 §4.6, p. 462). [stated vs practice] The purpose differs (classification, not benchmarking); the rule was still relaxed.

**C5. MIP-DD impact claim, v1 versus v5 (PE-28).** The v1 wording ("the majority of the bugs fixed since version 8.0.3"; about 71.4% more bugfixes) and the v5/IJOC wording (24 of 51 MIP-related bugs in SCIP 8.0.1–8.1.1) cannot both be the same measurement of the same thing. [practice vs practice]

**C6. Parameter name in the release report versus the code.** The SCIP 10.0 report (co-authored) tells users to set `exact/enabled` (S19 §3.1, p. 7). Gleixner had renamed it to `exact/enable` in March 2025 (S5 commit), and the released code and FAQ use `exact/enable`. A code search finds no `exact/enabled` in scipopt/scip (S5, 2026-11-08). [practice vs stated (co-authored)]

**C7. Author order of PaPILO.** arXiv v3 (Mar 2024) lists Gleixner, Hoen, Gottwald. The IJOC article and Crossref list Gleixner, Gottwald, Hoen (S17, S33). [record vs record]

**C8. No single averaging convention.** The shift for shifted geometric means is 10 s (VIPR, thesis Ch. 7), 0.001 s (2021 status update) or 1 s (2023 GMI, SCIP 10), with 100 nodes or 1 MB alongside (PE-11). The thesis defends shifted means as a method but fixes no value. [practice vs practice]

**C9. Two counts of inconsistent instances inside the MIPLIB 2017 paper.** §4.7 says 328 instances (5%) were removed for inconsistent solver results (S8 p. 465). Table 7 lists 334 under criterion B.5 (S8 p. 468), on the 5,666-instance ground set. The paper does not explain the difference of 6. [record vs record]

---

## Gaps (could not be found or read)

- **Peer review**: OpenReview lists two NeurIPS 2021 blind submissions titled "Learning to Schedule Heuristics in Branch and Bound" (forums mvEhkIqn45_ and fEImgFxKU63; Chmiela, Khalil, Gleixner, Lodi, Pokutta; S34). The forums, reviews and rebuttals could not be read because OpenReview showed a bot challenge, which was not bypassed. Why two submissions exist is unknown. No other public referee reports or rebuttals were found.
- **Rejections**: no evidence of rejected papers was found; journal histories beyond the Crossref received and accepted dates were not available.
- **ZIB OPUS**: the ZIB-Report server answered with a bot challenge. Not read: ZIB-Reports 12-19 and 12-36, the SCIP 5.0 and 6.0 release reports (his first-authorship of these was not verified), the ZIB-Report versions of the IR paper, and MIPLIB 2010 (S46). arXiv mirrors were used where they exist.
- **Internal history**: SCIP and SoPlex development is reviewed on ZIB's internal GitLab. His merge-request reviews, the VIPR GitLab history (2018–2022) and internal issue discussions are not public.
- **Impact of the checker bugs**: whether any certificate behind a published claim (IPCO 2017 supplement; the Chvátal paper S18; S12; S13) exploited a VIPR soundness hole was not examined. That would mean re-checking the published certificates with a fixed checker such as LeanVIPR.
- **MIP-DD markers**: the SCIP bugfix list in the MIP-DD IJOC repository marks entries with `x`, `*`, `o` and `-` (27, 30, 13 and 42 lines). The legend was not found in the files read, so I could not reconcile the marks with "24 of 51".
- **Not read in full**: the IR article (S44, paywalled; its content was read via thesis Ch. 2), the OBBT article (S48; only the thesis Ch. 6 outline), SCIP 8.0 (S47), the presolve-certification paper (S22, skimmed) and Appendix A of the thesis.
- **Talks**: no talk recordings or transcripts were found within this run's budget. None were saved to `sources/talks/`.
- **Mailing list**: only 9 of his 262 posts were opened; a systematic classification of all posts is still open.
- **Student-side view**: how he splits work with students is visible only through commit counts and review comments. Agent 04 covers mentorship.

---

## Sources

Primary unless marked. "Read" = opened in this run; "not read" = identifier checked only. S35–S38 are works by others, cited for context (secondary).

- S1. VIPR archived repository, github.com/ambros-gleixner/VIPR (created 2016-11-20; archived 2025-01-07): README.md, experiments/README.md, code/viprchk.cpp at c39fd63c and 56211850, viprttn.cpp at 948d76ba and 03d6b615, commit log (55 commits), PR #1 and its review comments. Read. Primary.
- S2. VIPR repository, github.com/scipopt/vipr (master 99eec19): CHANGELOG (VIPR 1.0–1.2), commit log (147 commits), viprchk.cpp and viprchk_parallel.cpp, PRs #1–#25 and #28, including #5, #14, #15, #24, #25 and #28 with comments (2024–2026). Read. Primary; the reporters' statements are [observed].
- S3. K. K. H. Cheung, A. Gleixner, D. E. Steffy, "Verifying Integer Programming Results", IPCO 2017, LNCS pp. 148–160, DOI 10.1007/978-3-319-59250-3_13; arXiv 1611.08832 v1 (2016-11-27) and v2 (2019-01-01; ZIB-Report 16-58, revised March 2017). Read. Primary.
- S4. SoPlex repository, github.com/scipopt/soplex: full git log (treeless clone, 2001–2026; 1,071 commits by Gleixner, 2008–2025), CHANGELOG (Releases 1.7.1–9.0.0), check/ commit history and diffs 45402499 (2014-10-23) and the evaluation.py fix of 2014-03-21. Read. Primary.
- S5. SCIP repository, github.com/scipopt/scip: full git log (treeless clone; 1,648 commits by Gleixner, 2008–2026), MR-template commits 8201ee1d (2018-01-26) and later revisions, .gitlab/merge_request_templates/Default.md, src/scip/branch_relpscost.c, prop_genvbounds.c, prop_obbt.c, heur_undercover.c, set.c, doc/inc/faq/faqtext.txt; GitHub code search 2026-11-08. Read. Primary.
- S6. MIPcc23 repository, github.com/ambros-gleixner/MIPcc23: RULES.md, README.md, commit log (2022-10-28 to 2024-02-02). Read. Primary (committee document committed by Gleixner).
- S7. S. Bolusani, M. Besançon, A. Gleixner, T. Berthold, C. D'Ambrosio, G. Muñoz, J. Paat, D. Thomopulos, "The MIP Workshop 2023 Computational Competition on reoptimization", Mathematical Programming Computation 16 (2024) 255–266, DOI 10.1007/s12532-024-00256-w; arXiv 2311.14834v2. Read. Primary.
- S8. A. Gleixner, G. Hendel, G. Gamrath, T. Achterberg et al., "MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library", Mathematical Programming Computation 13 (2021) 443–490, DOI 10.1007/s12532-020-00194-3 (open-access full text). Read. Primary.
- S9. MIPLIB 2017 website, miplib.zib.de: index.html, news.html, CHANGELOG.html (accessed 2026-11-08). Read. Primary.
- S10. A. M. Gleixner, "Exact and Fast Algorithms for Mixed-Integer Nonlinear Programming", PhD thesis, TU Berlin, 2015, DOI 10.14279/depositonce-4938 (353 pp.). Read: §§1.3–1.4, 2.6, 3.2.1, 7.4–7.5, 8 and the TOC. Primary (single-authored).
- S11. A. Gleixner, D. E. Steffy, "Linear programming using limited-precision oracles", Mathematical Programming 183 (2020) 525–554, DOI 10.1007/s10107-019-01444-6; arXiv 1912.12820v1 (ZIB-Report 19-57). Read (§6–7). Primary.
- S12. L. Eifler, A. Gleixner, "A computational status update for exact rational mixed integer programming", Mathematical Programming 197 (2023) 793–812, DOI 10.1007/s10107-021-01749-5 (IPCO 2021 version DOI 10.1007/978-3-030-73879-2_12); arXiv 2101.09141v1 (ZIB-Report 21-04). Read. Primary.
- S13. L. Eifler, A. Gleixner, "Safe and Verified Gomory Mixed-Integer Cuts in a Rational Mixed-Integer Program Framework", SIAM Journal on Optimization 34 (2024) 742–763, DOI 10.1137/23M156046X; arXiv 2303.12365 v1 (2023-03-22) and v3 (2023-11-07). Read (abstract, §4). Primary.
- S14. L. Eifler, J. Nicolas-Thouvenin, A. Gleixner, "Combining Precision Boosting with LP Iterative Refinement for Exact Linear Optimization", INFORMS Journal on Computing 37 (2025) 933–944, DOI 10.1287/ijoc.2023.0409; arXiv 2311.08037v1. Read (abstract, setup). Primary.
- S15. A. Hoen, D. Kamp, A. Gleixner, "MIP-DD: Delta Debugging for Mixed-Integer Programming Solvers", INFORMS Journal on Computing 38 (2026) 414–423, DOI 10.1287/ijoc.2024.0844; arXiv 2405.19770 v1 (2024-05-30) and v5 (2025-04-16); code and data github.com/INFORMSJoC/2024.0844 (DOI 10.1287/ijoc.2024.0844.cd); github.com/scipopt/MIP-DD README and log. Read. Primary (group).
- S16. A. Hoen, A. Gleixner, "Analyzing the Numerical Correctness of Branch-and-Bound Decisions for Mixed-Integer Programming", CPAIOR 2025, LNCS pp. 35–50, DOI 10.1007/978-3-031-95976-9_3; arXiv 2412.14710 v1 and v3. Read. Primary.
- S17. A. Gleixner, L. Gottwald, A. Hoen, "PaPILO: A Parallel Presolving Library for Integer and Linear Optimization with Multiprecision Support", INFORMS Journal on Computing 35 (2023) 1329–1341, DOI 10.1287/ijoc.2022.0171; arXiv 2206.10709 v1 and v3. Read (front matter). Primary.
- S18. L. Eifler, A. Gleixner, J. Pulaj, "A Safe Computational Framework for Integer Programming Applied to Chvátal's Conjecture", ACM Transactions on Mathematical Software 48 (2022) 14:1–14:12, DOI 10.1145/3485630; arXiv 1809.01572v2. Read (abstract, §2, setup). Primary.
- S19. C. Hojny, M. Besançon, K. Bestuzheva, ..., A. Gleixner et al., "The SCIP Optimization Suite 10.0", arXiv 2511.18580v1 (2025-11-23). Read (§2.1, §3.1, references). Primary (co-authored).
- S20. M. Ghannam, A. Gleixner, G. Mexi, E. Lam, "A Numerically-safe Branch-Price-and-Cut Algorithm for the Length-Constrained Cycle Partition Problem", arXiv 2607.15837v1 (2026-07-17). Read (abstract, §5). Primary.
- S21. F. D'Andreagiovanni, A. M. Gleixner, "Towards an accurate solution of wireless network design problems", ISCO 2016, LNCS 9849 pp. 135–147, DOI 10.1007/978-3-319-45587-7_12; arXiv 1604.00513v2. Read (abstract, §1–2). Primary.
- S22. A. Hoen, A. Oertel, A. Gleixner, J. Nordström, "Certifying MIP-Based Presolve Reductions for 0–1 Integer Linear Programs", CPAIOR 2024, LNCS pp. 310–328, DOI 10.1007/978-3-031-60597-0_20; arXiv 2401.09277v2. Skimmed. Primary (group).
- S23. S. Borst, L. Eifler, A. Gleixner, "Certified Constraint Propagation and Dual Proof Analysis in a Numerically Exact MIP Solver", arXiv 2403.13567v1 (2024). Skimmed. Primary (group).
- S24. exact-SCIP development repository, github.com/leoneifler/exact-SCIP: README and log (2020–2023). Read. Primary (group; written by Eifler).
- S25. SCIP mailing-list archive, listserv.zib.de/pipermail/scip/: author indexes Dec 2006–Sep 2026 (5,106 posts; 262 by Gleixner). Messages read: 2011-February/000628, 2014-August/002119, 2017-February/003003, 2018-March/003328, 2018-July/003465, 2020-April/003918, 2020-May/003984, 2022-July/004510, 2023-July/004685. Read. Primary.
- S26. HiGHS pull requests by ambros-gleixner: github.com/ERGO-Code/HiGHS #1102, #1121, #1175, #1182, #1184, #1195 (2023), with the maintainer's replies. Read. Primary; replies [observed].
- S27. Other pull requests by ambros-gleixner: Homebrew/homebrew-core #256157 (soplex 8.0.0) and #256158 (scip 10.0.0) (Nov 2025); scipopt/zimpl #4 (Oct 2025); scipopt/soplex #20 (2023); listing of all 17 PRs via the GitHub search API. Read. Primary.
- S28. GitHub user record and repository list of ambros-gleixner (api.github.com, 2026-11-08). Read. Primary (metadata).
- S29. Gleixner homepage, www.zib.de/userpage/gleixner/ (copy fetched 2026-11-08 by a sibling agent into the workflow scratch area). Read. Primary [stated].
- S30. Gleixner, Curriculum Vitae "updated July 31, 2017" (PDF linked from the homepage; text copy in the workflow scratch area). Read. Primary.
- S31. DBLP record pid 07/3479 (SPARQL export, 74 records, fetched 2026-11-08 by a sibling agent). Read. Secondary (bibliographic).
- S32. arXiv API author listing (48 preprints, with versions, comments and journal references; fetched 2026-11-08 by a sibling agent). Read. Secondary (bibliographic).
- S33. Crossref REST API lookups of the DOIs and title searches above (2026-11-08). Read. Secondary (bibliographic).
- S34. OpenReview notes search API result for "Learning to Schedule Heuristics in Branch and Bound" (two NeurIPS 2021 Blind_Submission notes); forum content not read (bot challenge). Secondary (metadata).
- S35. W. Cook, T. Koch, D. E. Steffy, K. Wolter, "A hybrid branch-and-bound approach for exact rational mixed-integer programming", Mathematical Programming Computation 5 (2013) 305–344, DOI 10.1007/s12532-013-0055-6. Not read (baseline context).
- S36. W. Cook, T. Koch, D. E. Steffy, K. Wolter, "An Exact Rational Mixed-Integer Programming Solver", IPCO 2011, LNCS pp. 104–116, DOI 10.1007/978-3-642-20807-2_9 (origin of the fpeasy and numdiff sets). Not read.
- S37. J. N. Hooker, "Testing heuristics: We have it all wrong", Journal of Heuristics 1 (1995) 33–42, DOI 10.1007/BF02430364 (cited in S10 §1.3). Not read.
- S38. T. Achterberg, R. Wunderling, "Mixed Integer Programming: Analyzing 12 Years of Progress", in Facets of Combinatorial Optimization (2013) 449–481, DOI 10.1007/978-3-642-38189-8_18 (cited for the benchmarking methodology). Not read.
- S39. PaPILO code and data repository, github.com/INFORMSJoC/2022.0171 (file listing only); github.com/scipopt/papilo git log (7 commits by Gleixner). Read (listing and log). Primary.
- S40. G. Gamrath, A. Gleixner, T. Koch, M. Miltenberger, D. Kniasew, D. Schlögel, A. Martin, D. Weninger, "Tackling Industrial-Scale Supply Chain Problems by Mixed-Integer Programming", Journal of Computational Mathematics 37(6) 866–888 (Crossref issued date 2021-07-01; volume year not checked), DOI 10.4208/jcm.1905-m2019-0055 (ZIB-Report 16-45, Nov 2016). Not read (status only).
- S41. G. Mexi, F. Serrano, T. Berthold, A. Gleixner, J. Nordström, "Cut-Based Conflict Analysis in Mixed Integer Programming", INFORMS Journal on Computing (online 2025), DOI 10.1287/ijoc.2024.0999; arXiv 2410.15110. Not read (status only).
- S42. G. Mexi, M. Besançon, S. Bolusani, A. Chmiela, A. Hoen, A. Gleixner, "Scylla: A Matrix-Free Fix-Propagate-and-Project Heuristic for Mixed-Integer Optimization", Lecture Notes in Operations Research (2025) 65–72, DOI 10.1007/978-3-031-58405-3_9; arXiv 2307.03466. Not read (status only).
- S43. A. Chmiela, E. B. Khalil, A. Gleixner, A. Lodi, S. Pokutta, "Learning to Schedule Heuristics in Branch-and-Bound", NeurIPS 2021, arXiv 2103.10294. Not read.
- S44. A. M. Gleixner, D. E. Steffy, K. Wolter, "Iterative Refinement for Linear Programming", INFORMS Journal on Computing 28(3) (2016) 449–464, DOI 10.1287/ijoc.2016.0692. Not read (paywalled; content via S10 Ch. 2).
- S45. A. M. Gleixner, D. E. Steffy, K. Wolter, "Improving the accuracy of linear programming solvers with iterative refinement", ISSAC 2012, pp. 187–194, DOI 10.1145/2442829.2442858. Not read.
- S46. T. Koch, T. Achterberg, E. Andersen, ..., A. M. Gleixner et al., "MIPLIB 2010", Mathematical Programming Computation 3 (2011) 103–163, DOI 10.1007/s12532-011-0025-9. Not read.
- S47. K. Bestuzheva, M. Besançon, ..., A. Gleixner et al., "Enabling Research through the SCIP Optimization Suite 8.0", ACM Transactions on Mathematical Software 49 (2023), DOI 10.1145/3585516. Not read.
- S48. A. M. Gleixner, T. Berthold, B. Müller, S. Weltge, "Three enhancements for optimization-based bound tightening", Journal of Global Optimization 67 (2017) 731–757, DOI 10.1007/s10898-016-0450-4. Not read (thesis Ch. 6 outline only).
- S49. K. Bestuzheva, H. Völker, A. Gleixner, "Strengthening SONC Relaxations with Constraints Derived from Variable Bounds", arXiv 2304.12145v1 (2023); short version arXiv 2211.05518v1 (HUGO 2022). Not read (status only).
- S50. J. van Doornmalen, L. Eifler, A. Gleixner, C. Hojny, "A proof system for certifying symmetry and optimality reasoning in integer programming", arXiv 2311.03877v2 (2023); J. von Holly-Ponientzietz, A. Hoen, M. Turner, A. Gleixner, "Clique Probing for Mixed-Integer Programs", arXiv 2512.17551v2 (2025). Not read (status only).
