# 03 · Process evidence (what Grossmann and his group actually DID)

> **Researcher**: Ignacio E. Grossmann, R. R. Dean University Professor, Department of Chemical Engineering, Carnegie Mellon University (Center for Advanced Process Decision-making, CAPD). DBLP 31/5106; Google Scholar `fiZryxEAAAAJ`; ORCID 0000-0002-7210-084X.
> **Dimension**: research agent 03 of 06, process evidence (nuwa research-craft Phase 1, framework §二 agent 3): behaviour traces, not statements. Layers 4 (execution) and 5 (judging results) dominate; layers 2, 3, 6 and 7 appear only where an artefact shows behaviour.
> **Research date**: 2026-10-10
> **Sources consulted**: 42 (30 primary, 12 secondary), listed under "Sources". Items that could not be read (blocked, paywalled, sponsor-only or not found) are listed under "Gaps". WebSearch: 1 call of the 4 allowed.
> **Local corpus**: `references/sources/papers`, `essays` and `software` hold only `.gitkeep`. `talks/` holds three auto-caption transcripts that agents 02 and 04 saved during this workflow run; they are not user-supplied. I used the 2024 interview transcript for discovery accounts. No finding below is "from user-supplied material". `references/sources/private/` was not opened.
> **Reuse of earlier downloads**: an earlier, interrupted pass of this workflow had left raw files in the shared scratch folder: author copies from egon.cheme.cmu.edu, CMU KiltHub reports, two arXiv version pairs, a sparse clone of the Pyomo repository, and saved MINLPLib and GAMS pages. I reused them as raw data and re-read every passage I cite. New in this run: the GDPlib clone; MINLPLib instance data plus 335 instance pages; six CAPD newsletters; arXiv submission histories; Crossref, OpenReview and GitHub records; the 2019 correction notice; and the group's web-interfaces page.
> **Verification**: every quotation in this file (about 130 quoted strings) was matched by script against its source text. Titles and one HTML-rendered string were checked by hand. Sources were PDF text from `pdftotext`, code files, GitHub JSON or the caption file. Each paper named carries a DOI, an arXiv id or a KiltHub DOI resolved in this run (Crossref, arXiv, figshare). A few papers appear only as titles printed in a reference list that I read; they are marked so.
> **Tags**:
> - [stated]: Grossmann said or wrote it, in a sole-author text, an interview or the CAPD newsletter he edited and signed. In the newsletter, the author of each group section is not printed.
> - [practice]: a documented action in a paper, report, code file, test, release or record. The actor is always named: **IEG** for his own act, **group** for co-authored or supervised work (students, postdocs, visitors), **lineage** for work in former students' labs after they left (e.g. D. E. Bernal Neira's SECQUOIA lab at Purdue).
> - [observed]: written by third parties.
> - [inferred]: my reading.
> - **P / S**: primary / secondary.
> **Caveat on authorship**: from 2015 on, almost every artefact here is multi-author. Grossmann is usually last or middle author, and his personal share cannot be separated. Such items show *group* practice under his direction, not necessarily his own hand.
> **Page and time references**: "p." is the PDF page of the copy read; "journal p." means the published pagination was read. Caption quotes give the start of the ~30 s caption block [h:mm:ss]. They are verbatim automatic speech recognition (ASR), errors included, with glosses in parentheses.

---

## 0. What this file adds to 01, 02 and 04

01 dissected the signature works (outer approximation (OA) 1986, DICOPT, LP/NLP-based branch and bound (LP/NLP-BB), generalized disjunctive programming (GDP), enterprise-wide optimization (EWO)) from reports and retrospectives. 02 recorded the stated method, and 04 the supervision. This file follows **artefacts over time**: which test instances recur, how test sets and baselines were chosen, what the code does by default, what changed between preprint and journal version, how corrections and criticism were handled, and what the group reported to its industrial sponsors while work was still in progress. Where 01 already gives a fact I write "see 01 §…" instead of repeating it.

## A. Era and resource context of the practices below

| Period | Compute and tools | Team (as the artefacts show it) | Artefacts examined here |
|---|---|---|---|
| 1983–1986 | CMU Design Research Center (DRC); IBM MILP code MPSX, NLP code MINOS; one small test problem per claim | IEG + one PhD student (M. A. Duran) | 1983 DRC report (via 01); 1986 OA paper (abstract and reference list only); 1987 erratum |
| 1986–1991 | Cornell Theory Center IBM-3090 during IEG's 1986–87 visiting professorship; GAMS built with the World Bank GAMS team; Fortran logic; ports to IBM/CMS, VAX/VMS and IBM-PC/DOS | IEG + visiting student (G. R. Kocis), then J. Viswanathan and I. Quesada | EDRC-06-43-88 (1988); Quesada & Grossmann EDRC report (1991) |
| 2000–2009 | CPLEX/OSL, CONOPT, BARON; COIN-OR (Ipopt, Cbc); IBM–CMU MINLP project (from 2004); NSF OCI-0750826 (minlp.org) | 15–20 PhD students plus visitors and a postdoc (P. Bonami), per the newsletters | CAPD newsletters 2000–2009; Bonmin report (2005); LOGMIP |
| 2013–2026 | GAMS with Gurobi/BARON/SCIP; MATLAB prototypes; Pyomo (with Sandia National Laboratories); Julia/JuMP; GitHub CI; arXiv | students, postdocs (J. Kronqvist), Sandia staff (J. D. Siirola), former students' labs | IJOC manuscript (2013–15); 2017–2025 manuscripts and arXiv versions; Pyomo GDPopt/MindtPy; GDPlib; Pyomo issue #3939 |

---

## B. Findings by layer (framework §一)

### Layer 4. Execution: test problems, baselines, implementation, debugging

#### B4.1 One small test instance, carried for 43 years [practice, IEG → group → lineage; P]

The clearest behavioural trace in the record is the reuse of the same small instances from the first MINLP report to the 2026 regression tests.

| Instance | First appearance | Later appearances (all checked) |
|---|---|---|
| **"Eight-process" superstructure** (8 binaries) | 1983 DRC report: "This has been confirmed in a test problem involving 8 binary variables, 9 continuous variables and 23 inequality constraints." (KiltHub 10.1184/R1/6467171.v1; quoted by 01) | **1986**: Test Problem 3 of the OA paper. MINLPLib `synthes3` cites Duran & Grossmann 1986 and has exactly 8 binaries, 17 variables (so 9 continuous) and 23 constraints; optimum 68.0097, added 2001.<br>**1988**: "EX3" in the DICOPT test table (8 binaries, 25 continuous, 30 constraints; EDRC-06-43-88 Table I, p. 23).<br>**1991**: "ex3" in the LP/NLP-BB tables (1991 report Table 6, p. 31).<br>**1996**: the GDP version in Türkay & Grossmann (the Pyomo docstring points to "page 969 of Turkay & Grossmann, 1996").<br>**2002**: the 2002 review (01 SW4).<br>**2018–2026**: Pyomo MindtPy test `eight_process_problem.py`: "Re-implementation of Duran example 3 superstructure synthesis problem in Pyomo" (expected optimum 68.0). It is used in both the convex and the nonconvex model lists. The GDPopt test suite loads it 26 times out of 48 example loads (22 algebraic, 4 logical form); the other loads are strip packing 12, constrained layout 5, two small literature examples 5. |
| **Test Problem 4: product positioning** (25 binaries) | 1986 OA paper. The problem comes from the marketing/OR literature. The paper's reference list (Springer page) includes S. Albers and K. Brockhoff, "A procedure for new product positioning in an attribute space", *European Journal of Operational Research* 1 (1977) 230–238; B. Gavish, D. Horsky and K. Srikanth, "An approach to the optimal positioning of a new product", *Management Science* 29 (1983) 1277–1297; F. S. Zufryden, "ZIPMAP—A zero-one integer programming model for market segmentation and product positioning", *J. Oper. Res. Soc.* 30 (1979) 63–70 (titles as printed there) | **1987**: the erratum corrects its optimum (see B5.1).<br>**1988**: "EX4" (25 binaries, 5 continuous, 30 constraints, 25 nonlinear inequalities; Table I, p. 23).<br>**1991**: "ex4", where the partial-surrogate variant was also tested (Tables 6–7, p. 31).<br>**2001**: MINLPLib `ex4` ("Product positioning in a multiattribute space"; source "MINOPT Model Library model duran86-4.dat, Aldo Vecchietti's Model Collection").<br>**2020s**: GDPlib `positioning`, "adapted from its equivalent in LOGMIP", with "Optimal objective value: -8.06". |
| **Batch design** (Kocis & Grossmann 1988, *Ind. Eng. Chem. Res.* 27(8):1407–1421, DOI 10.1021/ie00080a013) | 1988 | MINLPLib `batchdes`, `batch` (2001; optimum 167427.657); GDPlib `small_batch`; the 2025 LD-SDA paper: "Consider an instance of the optimal design for chemical batch processing from Kocis and Grossmann [66]" (arXiv:2405.05358v2, small-batch case study) |
| **Course and thesis material** | 2018 onward | MindtPy test `minlp_simple.py`: "Implementation of MINLP problem in Assignment 6 of the Advanced PSE lecture at CMU." `from_proposal.py`: "MINLP test model adapted from material in David Bernal's PhD thesis proposal". Pyomo commit by Emma Johnson, 2018-03-03: "Adding grossmann lecture test cases, test for validity of cuts applying cutting planes to the one-disjunction one". Each test model hard-codes its known optimum (e.g. `m.optimal_value = 3`). |

- [inferred] The 1983 instance and MINLPLib `synthes3` are the same problem: the sizes are identical (8/9/23) and MINLPLib attributes `synthes3` to Duran & Grossmann 1986. The Pyomo "eight-process" model is a larger formulation of the same superstructure (8 binaries; optimum 68.0 against 68.0097). I did not read the 1986 paper itself, so the match rests on sizes, optima and attributions.
- [inferred] Method: new theory is checked on instances whose optimum is known and stable for decades; once the code exists, regression tests freeze those optima. Generality is claimed from application papers and libraries, not from these canonical instances.

#### B4.2 From the group's own portfolio to community test libraries [practice, group/lineage; P + S]

1. **1988: the group's own models only.** The DICOPT report tests fifteen problems, all from the group's application work (batch design, flowsheets, planning, flexibility, reliability; EDRC-06-43-88, Table I p. 23).
2. **2005: the IBM–CMU library, and a selection rule tied to their own algorithm.** Bonami et al. report (31 Oct 2005, KiltHub 10.1184/R1/6466718.v1):
   - "These 41 problems were selected from a library of more than 150 convex problems that we collected [27]." (p. 12)
   - "We selected problems that were solved in less than 3 hours by an earlier implementation of the hybrid algorithm described in the previous section." (p. 12)
   - On the constrained-layout family: "Note that these problem are intentionally poorly modeled in order to have a large integrality gap and no feasible solution near the optimal solution of the continuous relaxation." (p. 10)
   - The Water problems existed only in AMPL format, so SBB and DICOPT (GAMS solvers) could not be run on them. Still: "We kept these problems in the test set, since they have a large number of continuous variables, a feature absent from other problems." (p. 12)
   - [inferred] Two habits show here: deliberately badly formulated instances are added to stress the algorithms, and the test set is conditioned on what an earlier version of their own algorithm could solve. The second is a selection effect the paper states openly but does not discuss.
3. **Who built the library, and the paper that never appeared.** The January 2006 CAPD newsletter credits the students: "Pierre has tested his code with close to two hundred test problems." Sawaya helped build most of the convex problems (batch design, retrofit planning, layout, trim loss); Laird contributed some water-contamination problems (p. 14). It announces: "An additional paper that will concentrate on the large set of test problems with an explanation of them is being prepared by Nick, Carl and Pierre." (p. 14) The 2005 report cites it as N. W. Sawaya, C. D. Laird, P. Bonami, "A novel library of non-linear mixed-integer and generalized disjunctive programming problems. In preparation." A Crossref title search found no such publication. The library lived on as a web page (egon.cheme.cmu.edu/ibm/page.htm) and as MINLPLib's source "Bonmin test library". [practice, group; abandoned paper, see §C]
4. **2008–2009: minlp.org, a library of problems described before they are coded.** August 2009 newsletter, p. 19: "instead of simply providing input files in GAMS, AMPL, AIMMS or similar, we have a library of problems where we introduce them first in their qualitative form". The August 2008 issue (p. 16) states the same plan in the future tense. The library listing (read 2026-10-10) shows entries contributed by students and visitors, not by IEG himself: Vecchietti 2011, Trespalacios 2013 and 2016, Bernal 2022, Kakkad and Pedrozo 2024. [practice, group; P-institutional]
5. **MINLPLib today** (instance data CSV and 335 instance pages, read 2026-10-10) [practice, S; my count]:
   - **Share.** 180 of 1,633 instances (11%) list at least one reference co-authored by Grossmann. I resolved 26 reference keys from instance pages. I excluded one key where he is only the volume editor, and left out up to 11 more instances whose multi-reference entries could not be resolved unambiguously.
   - **Added in waves:** 2001: 21; 2002: 2; 2007: 3; **2013: 76**; 2014: 1; 2017: 3; **2019: 54**; **2026: 20**.
   - **Convexity:** 87 convex, 91 nonconvex, 2 unclassified.
   - **Route into MINLPLib:** minlp.org 56; Bonmin test library 24; MacMINLP 9; GAMS Model Library 9; Floudas et al. handbook 6; MINOPT 5; BARON book 2; Vecchietti collection 2; other 74.
   - **Largest reference keys:**
     - Furman–Sawaya–Grossmann (54 hull reformulations with the FSG perspective function, suffix `hfsg`, 2019);
     - Duran & Grossmann 1986 (53);
     - Türkay & Grossmann 1996 (48);
     - minlp.org problem 117, Mouret & Grossmann "Crude-oil Operations Scheduling" (24);
     - Ovalle, Bhatia, Laird & Grossmann 2026 (*Ind. Eng. Chem. Res.* 65(7):3981–3998, DOI 10.1021/acs.iecr.5c02853; 20 multiperiod-blending instances, March 2026).
   - **Pairing of formulations.** Many of these GDP-derived families appear twice, as big-M (`…m`) and hull (`…hfsg`) versions of the same model. [inferred: the habit of publishing both reformulations of each GDP as benchmark instances]
6. **GDPlib** (lineage; SECQUOIA/gdplib, created 2020-05-24, clone of 2026-08-16): 20 of its 23 model folders cite a source co-authored by Grossmann. Its README states the purpose: "We envision GDPlib as an open library of GDP models to provide examples for prospective modelers, and to provide a benchmarking set for algorithm developers." [practice, lineage; P for the lineage, S for IEG]
7. **The legacy codes survive as web interfaces.** 01 lists MAGNETS, SYNHEAT, CYCLE, BATCHSPC and others as codes "listed only by name on his research page" and marks them "Not examined." The page `https://newton.cheme.cmu.edu/interfaces/` (read 2026-10-10) lists 39 entries. One model appears twice, and two entries are links (LOGMIP, minlp.org), which leaves 36 distinct model interfaces:
   - legacy: SYNHEAT, CYCLE, BatchSPC/BatchMPC, MULTISTAGE, PRODEV, GREENPLAN;
   - recent: Order-To-Cash, RTN-Logistics CCS, MULTIPERIOD BLEND, and "Alternate LP Solutions", which is the model of Kakkad et al., *Optim. Eng.* 25(4):2401–2424, 2024, DOI 10.1007/s11081-024-09887-3.
   - The group's software page describes it as "web-based software for Mixed Integer Programming Application in Process Systems Engineering" that "contains implementations through interfaces with GAMS of many process synthesis, supply chain, planning and scheduling MILP, MINLP and GDP models."
   - [practice, group; P; interfaces not executed]

#### B4.3 How test sets are built in the benchmark era [practice, group; P]

| Work (artefact read) | Test-set rule | Controls and reporting |
|---|---|---|
| Trespalacios & Grossmann, IJOC manuscript (journal: *INFORMS J. Comput.* 27(1):59–74, 2015, DOI 10.1287/ijoc.2014.0610) | Five problem families at fixed sizes; "The instances were generated by defining problem size and randomly generating the parameters of the problems" (p. 25) | Big-M: "the Big M parameter was estimated using the most basic solution for the given data" (p. 25). Controlled comparison: "Cuts and presolve were deactivated in Gurobi for all linear instances." (p. 26) This isolates formulation strength from solver cuts |
| Bernal, Vigerske, Trespalacios, Grossmann, manuscript of 22 Apr 2017 (journal: *Optim. Methods Softw.* 35(1):171–190, 2020, DOI 10.1080/10556788.2019.1641498) | MINLPLib2 rev. 342: convex, at least one integer variable, no semicontinuous variables or SOS, which gives "a set of 326 instances" (p. 10). Then: "Second, we run DICOPT with convex option enabled and feasibility pump disabled and removed all instances for which DICOPT terminated in less than one second." Same-model families: "Therefore, we reduced these subsets to the four largest instances." This leaves 68 (p. 10) | 1800 s; GAMS gap tolerance 0; PAVER 2 for comparisons and GAMS/Examiner2 to check primal feasibility (p. 10) |
| Kronqvist, Bernal, Grossmann, manuscript of 14 Dec 2017 (journal: *Math. Program.* 180:285–310, 2020, DOI 10.1007/s10107-018-1356-3) | Matched to the method's intended regime: "As mentioned earlier both L-OA and Q-OA are intended for problems with high to medium degrees of non-linearity, and therefore, we used the following criteria for choosing the test problems". Share of nonlinear variables above 0.5, which gives "There are in total 109 convex MINLP problems in MINLPlib2 (rev. 373, as of 2017-11-07) that satisfy the given criteria." (p. 19) | All variants run in one MATLAB implementation with the same subsolvers (Gurobi 7.5.1, IPOPT 3.12.7); 900 s. Parameter sensitivity reported: varying the level parameter "resulted in significant changes for individual instances but insignificant when considering the whole test set" |
| Kronqvist, Bernal, Lundell, Grossmann, preprint of 3 Jun 2018 and published version (*Optim. Eng.* 20(2):397–455, 2019, DOI 10.1007/s11081-018-9411-8) | All MINLPLib instances classified as convex, with at least one discrete variable and some nonlinearity: 366 in the preprint ("these constitute our master benchmark test set", p. 14), 335 in the journal (B5.3). Solvers "chosen based on criteria like availability, active development, and support for a file format available in MINLPLib [100]" (preprint p. 2) | Defaults plus each solver's convex settings: "Note that we have not tried to fine-tune any of the solvers; however, if there is a convex strategy, or recommended convex parameters we have used those." (journal p. 448). Solution profiles with virtual best and worst solver; PAVER flags returned solutions that contradict known bounds; subsets by continuous-relaxation gap and discrete density. Resource note: "a wall clock time limit of 900 s was also used with all solvers. Even with the 15-min time limit per problem, the total running time for the experiments was more than two weeks." (journal p. 418) |
| Chen et al., Pyomo.GDP manuscript "v6" (June 2020; journal: *Optim. Eng.* 23(1):607–642, 2022, DOI 10.1007/s11081-021-09601-7) | 39 instances, released where permitted as GDPlib (p. 22) | 1 h limit (p. 26); three solution-quality classes: global optimum within 1% gap, "best known" within 1%, "acceptable" within 10%; virtual best |
| Bernal Neira & Grossmann, arXiv:2109.09657 (COAP 88(1):251–312, 2024, DOI 10.1007/s10589-024-00557-9) | 217 instances | single thread; 3600 s or relative gap 10^-5 (v3 p. 9); absolute performance profiles (added in v3, see B5.3) |
| Ovalle et al., arXiv:2405.05358 (*Comput. Chem. Eng.* 195:108993, 2025, DOI 10.1016/j.compchemeng.2024.108993) | Four case-study families (reactor series, binary distillation column, rate-based catalytic distillation, batch design) | "Although the Neighborhood Search can be trivially parallelized, this study limited experiments to a single thread." (v2 p. 18) |

- [inferred] Since about 2013 the group defines its test sets by explicit, reproducible filters on a public library. It removes trivial instances by a time threshold, de-duplicates families of the same model, and verifies returned solutions with independent tools (PAVER, Examiner). This replaced the 1980s habit of a portfolio of the group's own models (B4.2).

#### B4.4 Baselines: their own earlier method is the standing foil, and they print where it loses [practice, group; P]

| Year | Comparison | Verbatim result |
|---|---|---|
| 1983 / 1986 | OA against branch and bound and generalized Benders decomposition (GBD) | one-fifth and one-half of their CPU time on one instance (see 01 SW1) |
| 2000 | S. Lee's GDP global algorithm against DICOPT | "The algorithm found the rigorous global optimum ($726,205) in about 2 minutes. In contrast, applying DICOPT to the MINLP formulation to that problem yields a suboptimal solution of $787,983." (CAPD newsletter June 2000, p. 13) |
| 2003 | a partitioning strategy against DICOPT and GBD | "DICOPT solved this problem in 351 secs, but obtained a suboptimal profit of 191.77. In contrast the partitioning procedure took 1880 secs and found a profit of 200.37." (Dec 2003, p. 25) |
| 2003 and 2006 | L. Bergamini's piecewise-MILP global method against BARON | "The algorithm required 5 minutes, while BARON could not solve the problem within 15 minutes." The same sentence appears in Dec 2003 (p. 15) and Jan 2006 (p. 16). The test problem "originated in an internship of Sangbum Lee at Eastman Chemical" (Jan 2006) |
| 2006 | the new open-source hybrid (later Bonmin) against SBB and DICOPT | "DICOPT solved 20 of the 38 problems the fastest" and "The hybrid method (i.e. branch and cut) proved to dominate for the remaining 18 problems in terms of speed and successful completion." (Jan 2006, p. 14) |
| 2017 | DICOPT with feasibility pump against old DICOPT, AlphaECP, BONMIN and SCIP | "None of the solvers is fastest on a majority of instances, but SCIP is most efficient, followed by the two variants of DICOPT." (manuscript p. 15) |
| 2020 | Pyomo.GDP strategies against each other | "For all three classes of solution quality, we observe that no individual solver is able to address all problems as effectively as the "Virtual best" composite solver." This is used as evidence for a design principle: "This validates the core principle that flexible solution strategies should be available for effective optimization frameworks." (manuscript p. 28) |
| 2025 | LD-SDA against the group's own GDPopt algorithms (LOA, LBB, GLOA) and big-M/hull reformulations solved by BARON, SCIP, DICOPT, KNITRO and SBB | the outcome claims are discussed in B5.3 |

- [inferred] The default foil is DICOPT or the group's previous algorithm, both products of the same group. When an outside solver wins (SCIP in 2017; the single-tree solvers SHOT and AOA in the 2019 review, see 01), the text says so.
- [inferred] Global solvers (BARON) are typically given short limits (15 min in 2003–2006) in comparisons that favour the new method. A caution for anyone reusing these comparisons.

#### B4.5 Implementation path: algorithms go into a modelling system, are written by students, and often ship before the paper [practice; P + S]

**1. DICOPT, the 1986–88 prototype.**
- "This work was performed at Cornell University in 1986-1987 while Ignacio Grossmann was the Mary Upson Visiting Professor" (EDRC-06-43-88, p. 3).
- "The command files, which are very small, are written in REXX for IBM/CMS, DCL for VAX/VMS, and BAT for IBM-PC/DOS." (p. 10)
- Subsolvers were compared: "Computational experience has indicated that MPSX outperforms ZOOM/XMP in solving the master problems both in efficiency and reliability." (p. 12)
- IEG's own account: "I was on sabatico I could now learned about Ming system so we were able to implement our minlp method you know in gamps" [1:00:28] (ASR: sabbatical; modelling system; GAMS). [practice, IEG + student; stated]

**2. Shipping before publishing.**

| Improvement | In software | Preprint or report | Journal |
|---|---|---|---|
| Linearizations of infeasible NLP subproblems in DICOPT (option `infeasder`), by A. Vecchietti | described as available in Jan 2006 (newsletter p. 16) | none identified | none identified (not searched separately) |
| Feasibility pump in DICOPT | the manuscript says the extension "has been available in GAMS" (footnote marker omitted) "since version 24.5" (p. 2); GAMS 24.5.1 was released 23 Sep 2015 (GAMS release notes) | 22 Apr 2017 | online Aug 2019, *Optim. Methods Softw.* 35(1), 2020 |
| Furman–Sawaya–Grossmann (FSG) perspective approximation for the hull | idea written down in Jan 2006 (B5.2); Pyomo default since commit `ea82583` of 2015-02-20 by J. Siirola: "Update to the GDP convex hull reformulation to include the improved relaxation by Sawaya, Furman, and Grossmann." | Optimization Online 2016, as cited in the Pyomo docstring | *Comput. Optim. Appl.* 76(2):589–614, 2020, DOI 10.1007/s10589-020-00176-0 |
| LD-SDA (logic-based discrete-steepest descent) | Pyomo code from 2024-02-04 (Z. Peng); released in Pyomo 6.9.0 (21 Feb 2025) | arXiv v1 May 2024, v2 Jan 2025 | *Comput. Chem. Eng.* 195, April 2025 |
| GDPopt and MindtPy | first commits 2018-02-01 (Q. Chen) and 2018-03-14 (D. Bernal) | PSE 2018 conference papers, e.g. Bernal, Chen, Gong, Grossmann, *Comput. Aided Chem. Eng.* 44:895–900, 2018, DOI 10.1016/B978-0-444-64241-7.50144-0 | Pyomo.GDP, *Optim. Eng.* 2021/2022 |

**3. Who writes the code.**
- Pyomo history (31,465 commits; sparse clone of `main` at `b473cba`, 2026-10-06) has **no commit authored by Grossmann** under any spelling.
- GDPopt non-merge commits: E. S. Johnson 233, Q. Chen 183, Z. Peng 65, J. D. Siirola 35, M. Mundt 20, others. MindtPy: Z. Peng about 774 under four spellings, Siirola 45, Q. Chen 31, D. E. Bernal (Neira) 26, others.
- The GDPopt docstring credits undergraduates and master's students: "Several key GDPopt components were prototyped by BS and MS students:", namely logic-based branch and bound (S. Kale), the MC++ interface (J. Bates), set-covering initialization (E. Fernandez) and the logic-to-linear transformation (R. Valentin).
- [practice, group; P] [inferred] IEG directs and writes about the software; students, postdocs and Sandia staff write it. A missing commit is not proof that he wrote no code.

**4. Software outlives students only when it is handed on.**

| Tool | What happened |
|---|---|
| DICOPT | went to GAMS: "originally developed by Jagadisan Viswanathan, Ignacio E. Grossmann, and Aldo Vecchietti", now "maintained by GAMS" (GAMS manual; see 01 Contradiction 2 on Kocis) |
| LOGMIP | went to INGAR, Argentina (Vecchietti). By 2020: "LOA is no longer supported in LOGMIP. Therefore, GDPopt-LOA is the only working modern implementation of LOA, built as a meta-solver in Pyomo.GDP, with a free and open-source code base" (Pyomo.GDP manuscript p. 10) |
| PROSYN (Kravanja & Grossmann, *Comput. Chem. Eng.* 14(12):1363–1378, 1990, DOI 10.1016/0098-1354(90)80018-7) | continued by Kravanja as MipSyn (e.g. Kravanja, *Comput. Chem. Eng.* 34(11):1831–1848, 2010, DOI 10.1016/j.compchemeng.2010.04.017) |
| DisjunctiveProgramming.jl (H. Perez; JuliaCon Proc. 2023, DOI 10.21105/jcon.00117) | moved from the student's account to the `infiniteopt` organisation; last commit 2026-10-09 |
| OR-Gym (C. Hubbs et al., arXiv:2008.06319) | last commit 2023-02-13 (456 stars, 11 open issues), i.e. dormant after the student left |

[practice; P/S]

**5. Defaults stay conservative; improvements are opt-in.**
- The newsletter on the new DICOPT option: "In the current version an integer cut is simply added if the NLP is found to be infeasible. This is often very ineffective as the integer cut is quite weak, especially as the dimensionality of the 0-1 variables increases." Then: "For nonconvex problems there is the risk of cutting off optimal solutions." And: "By default infeasder is 0. In this case DICOPT runs like the previous version" (Jan 2006, p. 16).
- Eleven years later the group's own paper names the cost of that default: "The main reason for this is that by default, and to address nonconvex problems, DICOPT does not include linearizations of nonlinearities from infeasible NLPs into the MIP." (FP manuscript p. 2)
- The GAMS manual today still has `infeasder` default 0. A separate `convex` option (default 0) switches the stopping rule, the infeasible-NLP linearizations, the penalty weights and the feasibility pump together.
- Pyomo's hull is the opposite case: there the newer FSG formula became the default, with the note "The default, "FurmanSawayaGrossmann", is strongly recommended." (`pyomo/gdp/plugins/hull.py`). [practice; P + S]

#### B4.6 What gets done first [practice; P + S]

- **Relaxed problem first.** DICOPT starts from the NLP relaxation. Today's manual (GAMS-maintained): "In general it is not a good idea to try to solve an MINLP model if the relaxed model cannot be solved reliably." In 1988 the user had to supply the first binary vector and a starting point. The master problem then supplied starting points: "In fact, in all these problems, once the first NLP problem converged there was no difficulty in subsequent iterations." (EDRC-06-43-88, p. 12)
- **Keep subproblems feasible.** The 1988 report writes NLP subproblems with slacks and a large penalty. The manual still recommends this: "Since this may slow the convergence, it is recommended to reformulate the MINLP with "elastic" constraints".
- **Cover every nonlinear disjunct before iterating.** GDPopt's default `init_algorithm` is `set_covering`: "The purpose of this initialization is to generate linearizations corresponding to each of the disjuncts." (`discrete_problem_initialize.py`). Only disjuncts with nonlinear constraints need covering. GDPopt's LOA cites Türkay & Grossmann 1996 (*Comput. Chem. Eng.* 20(8):959–978, DOI 10.1016/0098-1354(95)00219-7). I did not check whether set covering is described in that paper.
- **Convex first, nonconvex later.** "In the first phase of the project we have restricted ourselves to solving MINLP problems that have a convex relaxation." (Jan 2006, p. 13, IBM–CMU project)

#### B4.7 Debugging and validation habits [practice; P]

1. **Swap the subsolver.**
   - MPSX against ZOOM/XMP for the master problems (1988, above).
   - In the 2019 review: "We have also modified limits and other parameters when it is apparent that implementation issues are the cause of, e.g., premature termination of a solver on some problem instances or numerical instability. For example, without adding the CONOPT option specified below, DICOPT and SBB fails to solve all the smallinv-instances in MINLPLib." (journal p. 448)
2. **Multistart on nonconvex models.** The 1988 report's Table III, "Computational Results with Nonconvex MINLP Problems", lists per problem how many initial points were tested and from how many the global optimum was found (p. 25). In the text: "the global optimum was found in 24 out of 28 cases" (p. 14).
3. **Check returned solutions independently.** PAVER 2 and GAMS/Examiner2 (2017); PAVER in the 2019 review.
4. **Turn a heuristic into a bounded method, or bound it.**
   - June 2000: "Jayanth discovered that unfortunately the procedure described above only provides an upper bound to the expected completion time. For this reason he has developed a rigorous branch and bound" (p. 16).
   - Dec 2001: "The disadvantage is that it is a heuristic. However, Iiro was fortunately able to find an expression for computing a lower bound to the makespan" (p. 20). The bound showed deviations of 1–3% from the optimum on the examples.
5. **Lineage, 2026: cross-check one algorithm against other routes on the shared library.**
   - D. E. Bernal Neira's Pyomo issue #3939 (opened 2026-05-11) reports a bug in GDPopt's global LOA: "The current code can generate a convex cut that excludes feasible points and causes GLOA to terminate with an incorrect incumbent."
   - It was found by comparing GLOA with big-M, hull and LBB on GDPlib models: "Default `gdpopt.gloa`, however, quickly reported a worse false certificate under all tested solver profiles:" (comment of 2026-05-14).
   - The issue is open as of 2026-10-10. In the clone of 2026-10-06, `gloa.py` still builds both cuts from the concave slope.
   - GLOA follows Lee & Grossmann, *Comput. Chem. Eng.* 25(11–12):1675–1697, 2001, DOI 10.1016/S0098-1354(01)00732-3. The defect is in the 2018 Pyomo implementation, not in the paper. [practice, lineage; P]

### Layer 5. Judging results: corrections, criticism, revision

#### B5.1 Corrections: few, small, made by re-solving; no retraction found [practice; P/S]

Seven correction notices on works with I. E. Grossmann as author were found, against roughly 900 works (01 §0). Six came from Crossref keyword queries (erratum, corrigendum, correction, comments, reply, retraction). The seventh is the 1987 OA erratum, whose Crossref title repeats the paper's title:

| Notice | Corrects | Content |
|---|---|---|
| *Math. Program.* 39(3):337, 1987, DOI 10.1007/BF02592081 | Duran & Grossmann 1986, DOI 10.1007/BF02592064 | **Read.** "The solution that was reported in Table 4A with z* =7.7891 is suboptimal." The corrected optimum 8.0641 "was found by resolving Test Problem No. 4 on an IBM 3090/400 with 5 FPS Array Processors at the Cornell Theory Center, Ithaca, NY." |
| *Ind. Eng. Chem. Res.* 31(4):1236, 1992, DOI 10.1021/ie00004a041 | Sahinidis & Grossmann 1991, DOI 10.1021/ie00054a015 | not read |
| *Ind. Eng. Chem. Res.* 31(7):1834, 1992, DOI 10.1021/ie00007a035 | Birewar & Grossmann 1990, DOI 10.1021/ie00107a008 | not read |
| *Comput. Chem. Eng.* 25(7–8):1153, 2001, DOI 10.1016/S0098-1354(01)00706-2 | Lee & Grossmann 2000, DOI 10.1016/S0098-1354(00)00581-0 | not read (ScienceDirect 403) |
| *Optim. Eng.* 20(4):1191–1192, 2019, DOI 10.1007/s11081-019-09446-1 | Galan et al. 2019, DOI 10.1007/s11081-019-09444-3 | **Read.** Typographic: "In the original publication of the article, in Table 4 and Table 5 lower case `k' which is the correct convention of the units was published as upper case `K'." |
| *Comput. Chem. Eng.* 133:106639, 2020, DOI 10.1016/j.compchemeng.2019.106639 | Ye, Grossmann & Pinto 2018, DOI 10.1016/j.compchemeng.2017.08.013 | not read. Crossref lists three authors for the paper and four for the corrigendum (adds S. Ramaswamy); what it corrects is unknown [inferred: possibly the author list] |
| *Ind. Eng. Chem. Res.* 59(44):19838, 2020, DOI 10.1021/acs.iecr.0c05114 | Franzoi et al. 2020, DOI 10.1021/acs.iecr.0c02868 | not read |

- **The 1987 correction has held for 40 years.** MINLPLib's `ex4` has primal bound −8.06413617 (minimization form), and the dual bounds of BARON, SCIP, Couenne, CPLEX, Gurobi, LINDO and SHOT all equal it. GDPlib carries the corrected value (−8.06). [practice + S]
- [inferred] Behaviour: errors were found by re-solving with better tools (the Cornell toolchain that became DICOPT) and published as a short notice within about a year. The test instance was kept, and the libraries carry the corrected value.

#### B5.2 Answering critics and known defects in print [practice; P]

1. **A published exchange (1992).** R. L. Salcedo, "Comments on "An MINLP process synthesizer for a sequential modular simulator"", *Ind. Eng. Chem. Res.* 31(12):2804–2805, DOI 10.1021/ie00012a027. U. M. Diwekar, I. E. Grossmann, E. S. Rubin, "Response to comments …", same issue, p. 2805, DOI 10.1021/ie00012a028. The original paper is *Ind. Eng. Chem. Res.* 31(1):313–322, 1992, DOI 10.1021/ie00001a042. The comment and the response are one page or less each. Their content was **not read** (ACS 403; one WebSearch found nothing). This is the only published comment–response pair found for his work.
2. **Fletcher and Leyffer's stronger cuts.** Fletcher & Leyffer replaced OA's integer cuts for infeasible NLPs with feasibility cuts (*Math. Program.* 66:327–349, 1994, DOI 10.1007/BF01581153). The group's code took this up only as an **opt-in** DICOPT option about 11 years later (2006, B4.5), with the nonconvex-safe default kept. The co-authored history (Kronqvist, Bernal Neira & Grossmann, "50 years of mixed-integer nonlinear and disjunctive programming", *Eur. J. Oper. Res.* 331(3):687–705, 2026, DOI 10.1016/j.ejor.2025.07.016; copy saved by agent 01) acknowledges: "The resulting gradient cuts are generally stronger, as the no-good cuts only exclude a single integer assignment." (see 01 SW1)
3. **The hull's numerical defect, fixed over 20 years.**
   - Lee & Grossmann 2000 (DOI 10.1016/S0098-1354(00)00581-0) introduced the ε-perturbed perspective. Grossmann & Lee 2003 (*Comput. Optim. Appl.* 26(1):83–100, DOI 10.1023/A:1025154322278) is the paper the Pyomo docstring cites for the (y+ε) form.
   - The January 2006 newsletter names the failure modes. If ε is too small, accuracy suffers. If it is larger and a disjunct does not apply, the approximation can become infeasible. N. Sawaya derived rigorous alternatives (Jan 2006, p. 15).
   - Then: "Based on input by Kevin Furman from ExxonMobil, Nick has been considering the alternative convex expression", "which not only circumvents the infeasibility that arises in the original Grossmann & Lee expression" (p. 15).
   - That expression became Pyomo's default in February 2015 and was published in *Comput. Optim. Appl.* in 2020 (DOI 10.1007/s10589-020-00176-0).
   - Pyomo's documentation now warns that both older forms "have numerical and feasibility issues" (`hull.py`; Sandia-maintained text). [practice, group; P]
   - [inferred] Defects in the group's own methods get fixed by later students, sometimes on an industrial collaborator's idea. The fix reaches code years before the journal.

#### B5.3 What changes between preprint and journal (no referee reports are public) [practice, group; P]

No referee report or rebuttal for any Grossmann journal paper was found. One NeurIPS 2025 paper (spotlight) has an OpenReview forum: D. Ovalle, L. T. Biegler, I. E. Grossmann, C. D. Laird, M. Dulce Rubio, "Conformal Mixed-Integer Constraint Learning with Feasibility Guarantees", arXiv:2506.03531, forum `ZvUZvT8tgg`. Its reviews were behind a challenge page and were **not read**. The closest available evidence of how the group responds to review is therefore the difference between versions:

| Paper and versions | What changed | What stayed |
|---|---|---|
| **Convex-MINLP review.** Preprint 3 Jun 2018 (egon) to journal (received 5 Jun 2018, revised 16 Nov 2018, online 3 Dec 2018). Sentence-level diff: 212 journal sentences have no close match (similarity ≥ 0.6) in the preprint; many are reworded solver descriptions or text-extraction artefacts, so the changes listed here were checked by hand | Test set 366 to 335: "The smallinvSNPr* instances were also excluded, since they recently lost their convex classification in MINLPLib due to rounding errors in the problem format that actually made them slightly nonconvex." (journal p. 418). `meanvarxsc` dropped (semicontinuous variables). Pajarito replaced by Pavito: "Because of this, Pajarito is left out of the numerical comparison and only Pavito is included." (p. 414). Knitro split into Knitro-QG and Knitro-BB. Developers' advice followed: "Couenne warns against using another LP solver than CLP, which we respected since it actually improved performance significantly." (p. 418); filterSQP for Minotaur | Protocol (900 s, defaults plus convex settings, profiles, subsets); the "fine tune" sentence (preprint p. 44, journal p. 448) |
| **Conic GDP.** arXiv:2109.09657 v1 (20 Sep 2021), v2 (3 Mar 2023), v3 (19 Feb 2024); journal online 20 Feb 2024 | Claim recast as a hypothesis. v3 adds "We present a set of examples and perform a computational study that supports our central hypothesis: considering the original conic structure of conic GDP problems can lead to more efficient solutions to such problems." (p. 4). A generalisation softened: v1 "This is since the description of problems using algebraic constraints is more natural for practitioners." (p. 3) became v3 "This is because the description of problems using algebraic constraints might be more natural for certain practitioners, e.g., in fields such as chemical engineering, where material and energy balances are naturally representable via scalar algebraic constraints." (p. 2). Absolute performance profiles added. Some results moved out: "Therefore, the implementation results are left out of this manuscript, although they are included in the repository for reference." (v3 p. 11). The constrained-layout and k-means examples were posted on minlp.org (2022 entries) | Same 217 instances and the same solvers (KNITRO, BARON, MOSEK, CPLEX, Gurobi, SCIP counts nearly unchanged). 29 months from v1 to publication |
| **LD-SDA.** arXiv:2405.05358 v1 (8 May 2024) to v2 (27 Jan 2025, the journal version) | Abstract strengthened. v1: "The results show convergence efficiency and solution quality improvements compared to conventional GDP and MINLP solvers." v2: "In the case studies presented in this work, including batch processing, reactor superstructures, and distillation columns, LD-SDA consistently outperforms conventional GDP and MINLP solvers, especially as problem size grows." Limitations added; absent in v1, they appear in v2: "Nonetheless, the scalability of the LD-SDA still needs to be evaluated for larger superstructure problems, e.g., those resulting in more than 7 external variables." (p. 26). Also: no global guarantee, exponential growth of the neighbourhood, single thread. Theory added (integral convexity; a positions-based external-variable reformulation that avoids premature stops on unevenly spaced sets; a no-cycling property). v1's "outperformed state-of-the-art MINLP solvers and GDP solution techniques" was scoped in v2 to "for the problems studied" | Same case studies and the same baseline set (LOA, LBB, GLOA; BARON, SCIP, DICOPT, KNITRO, SBB) |

- [inferred] Under review the group keeps the experiment and changes the scaffolding around it. It prunes instances that no longer qualify, follows solver developers' recommendations, states limitations, and scopes or reframes claims. Experiments are seldom redesigned.

#### B5.4 Negative results in their own progress reports and code [practice, group; P]

- "The cutting plane technique was not very helpful in both cases, although in the retrofit problem it did improve substantially the performance of the big-M reformulation." (Jan 2006, p. 15; the two cases are a process-retrofit and a job-shop problem; the method had worked on strip packing)
- "Generating rigorous tight cuts for the MILP in this problem, however, has turned out to be surprisingly difficult." (Dec 2001, p. 20)
- "We see that enabling the feasibility pump leads to a small performance loss with respect to solution time, but improvements in finding optimal solutions and proving optimality." (FP manuscript, p. 14). With the pump's cuts reused, "the computing time is considerably decreased by reusing the cuts from the feasibility pump" (p. 14).
- Bonmin 2006: their own DICOPT was fastest on 20 of 38 problems (B4.4).
- In code: "For nonconvex problems, LOA may not report rigorous lower/upper bounds." (GDPopt docstring, added 2020-01-15)
- In the DICOPT manual: "Although the algorithm has provisions to handle non-convexities, it does not necessarily obtain the global optimum."

### Layers 2 and 3. Where problems and ideas came from (process accounts and traces)

- **OA from discussions with a student** [stated]: "with him having the discussions on what what later on became as the a approximation method" [0:55:47] (ASR: outer-approximation; "him" is Marco Duran).
- **GDP from an interdisciplinary centre** [stated]: "we had a very nice a sort of research effort in engineering design that was multi-disciplinary and as part of that professor John hooker was part of that and he was you know very much interested in logic" [0:56:52]. The student was R. Raman; the paper is Raman & Grossmann, *Comput. Chem. Eng.* 18(7):563–578, 1994, DOI 10.1016/0098-1354(93)E0010-7.
- **The engineering defect behind logic-based decomposition** [stated]: "when the flows go to zero okay the equations can become singular" [0:58:57]. And: "they were driven by the need to solve these engineering problems" [0:58:26]. The same defect is written into the 1988 report, where linearization terms "vanish when variables take zero values" (01 SW2). [practice/stated, consistent over 36 years]
- **Problems and ideas from industry** [practice, group; P]:
  - The FSG formula came from K. Furman of ExxonMobil (B5.2).
  - Bergamini's test problem came from an Eastman internship (B4.4).
  - Stated: "we would probably never have run into that problem if we were just reading some papers" [1:17:09], and "it's not only that they come give us a problem we then you know do some solutions but what we're looking for is a two-way street" [1:14:04].
- **Said vs did: industrial co-authorship.** He says of Dow's John Wassick: "with him we we've written at least you know 15 maybe even 20 20 joint papers" [1:14:34]. The record exceeds the claim. A Crossref query for Grossmann plus Wassick returns 28 records, 2008–2026: 21 journal articles, 3 book chapters, 1 proceedings paper and 3 preprints. The first is Erdirik-Dogan, Grossmann & Wassick, *Ind. Eng. Chem. Res.*, 2008, DOI 10.1021/ie701682m; the latest Sun et al., *Comput. Chem. Eng.*, 2026, DOI 10.1016/j.compchemeng.2026.109654. [stated vs practice; P/S]

### Layer 6. How results are reported (format behaviour over time) [practice; P]

| Era | Unit of evidence |
|---|---|
| 1983 | CPU-time ratios on one instance |
| 1986 | "Numerical results are reported for several example problems to illustrate the potential of the proposed algorithm", plus "a theoretical comparison with generalized Benders decomposition" on lower bounds (Springer abstract) |
| 1988 | CPU s, iterations and subsolver split per problem (Table I); success counts from multistart (Table III) |
| 1991 | node counts and number of NLPs against OA |
| 2002 | nodes and root bound on the canonical example (01 SW4) |
| 2006 | count of problems on which each code is fastest |
| 2017–2019 | performance and solution profiles, virtual best/worst, PAVER-verified status, subsets by gap and density |
| 2020 | three solution-quality classes |
| 2024 | absolute performance profiles |

- **Dissemination.**
  - Technical report first, then journal (DRC/EDRC reports 1983–1994, now on KiltHub). Author copies on egon.cheme.cmu.edu.
  - arXiv only since 2020: 16 preprints, 12 of them single-version.
  - **All 16 were submitted by a co-author** (Ovalle 4, Zhang 2, Perez 2, and one each by Hubbs, Bernal Neira, Achkar, A. Lee, Tristán, Peng, Pulsipher, Vyas), none by Grossmann (arXiv submission histories).
- **Reports to sponsors.** The 2000–2009 CAPD newsletters give each project a block: "New developments:", "Students:" with start dates, then a narrative with instance sizes, times, failures and next steps. Text is carried forward between issues (the BARON sentence of Dec 2003 recurs in Jan 2006). [practice, group; P]

### Layer 7. Organisation visible in the artefacts [practice; P]

- **Division of labour.**
  - Students and postdocs write code, test libraries and preprints (B4.5, B4.2, Layer 6).
  - Visitors contribute whole components: Vecchietti (LOGMIP, DICOPT option), Bergamini (global GDP algorithm), Bonami (postdoc, Bonmin).
  - Industrial researchers contribute formulas and problems (Furman; Wassick).
- **Continuity mechanisms.** Models outlive their students through GAMS web interfaces, MINLPLib, minlp.org and GDPlib. Code survives when handed to a maintainer (GAMS, INGAR, Pyomo/Sandia, `infiniteopt`) and goes quiet when it is not (OR-Gym).
- **Plans written down, then changed.**
  - Jan 2006: "Our next major step in this project will concentrate on handling nonconvexities in an "ad-hoc" manner, that is without performing rigorous global optimization." (p. 14)
  - Aug 2008 and Aug 2009: the project had moved to Couenne, a rigorous spatial branch-and-bound code (with P. Belotti), and to the NSF cyberinfrastructure (pp. 8, 15–16, 19–20). The library paper of 2006 became the minlp.org site (B4.2).

---

## C. Failures, abandoned directions, corrections (consolidated)

| Item | Evidence | Tag |
|---|---|---|
| OA "Part II" (relation with GBD), DRC-06-68-84, Dec 1984 | Cited as a separate report in the 1986 paper's reference list (Springer page), but the 1986 abstract already contains "a theoretical comparison with generalized Benders decomposition … on the lower bounds" | [practice; P] nuance to 01 §3 (see Contradictions) |
| Library paper "in preparation" (Sawaya, Laird, Bonami, 2005–06) | Announced twice; nothing in Crossref; replaced by egon/ibm page and minlp.org | [practice; P] |
| "Ad-hoc" nonconvex plan (2006) | Superseded by the rigorous Couenne project (2008–09) | [practice; P] |
| Partial surrogate constraints (1991) | Tested "on two test problems" (1991 report p. 23). The GDPopt docstring has listed "- Partial surrogate cuts [pending]" since its first commit (2018-02-01), still pending in 2026 | [practice; P] [inferred link: same term, the docstring cites no source] |
| GBD in GDPopt | "- Generalized Bender decomposition [pending]" since 2018-02-01 | [practice; P] |
| Two-phase convexity tests in DICOPT (1987–88) | Replaced by the augmented-penalty heuristic (see 01 SW2) | [practice; P] |
| Cutting planes for linear GDP | "not very helpful" on retrofit and job-shop (2006) | [practice; P] |
| LOA inside LOGMIP | "no longer supported" by 2020; re-implemented in Pyomo | [practice; P] |
| OR-Gym | no commits since Feb 2023 | [practice; S] |
| GLOA implementation (Pyomo) | false certificates, issue open since May 2026 | [practice, lineage; P] |
| Errata and corrections | 7 notices, 2 read (B5.1); no retraction found | [practice; P/S] |
| Rejections | Only the stories told in the interview (see 02 §D, 04 §D); no rejected manuscript identified in the record | — |

## D. Process patterns (candidates for Phase 2; all [inferred] from the evidence above)

1. **Canonical-instance continuity.** A handful of small instances with known optima (eight-process, product positioning, small batch) carry every new method from 1983 to 2026: report, paper, solver test table, library, regression test.
2. **Own portfolio, then public library.** Test sets begin as the group's application models. From 2005 on they are curated into public libraries (Bonmin library, minlp.org, MINLPLib, GDPlib), with both big-M and hull versions and with problem descriptions before code.
3. **Ship in a modelling system, publish later.** DICOPT (GAMS, 1986–88), the feasibility pump (GAMS 2015, paper 2017/2019), FSG (Pyomo 2015, paper 2020), LD-SDA (Pyomo 2024–25). Students and visitors implement.
4. **Conservative defaults, opt-in improvements** in tools that users depend on (DICOPT's nonconvex-safe defaults since the 1980s).
5. **Own previous method as the foil, with losses printed.** DICOPT or the previous algorithm is the baseline; outside winners are acknowledged (SCIP 2017, SHOT/AOA 2019).
6. **Declare heuristics; bound them when possible.** Stated in papers, manuals and docstrings; heuristics paired with lower bounds or multistart statistics.
7. **Long gestation for numerical fixes.** The hull ε problem was named by 2006, the formula was in code in 2015, the paper came out in 2020. Ideas can come from industry.
8. **Revision keeps experiments and adjusts claims.** Prune invalid instances, adopt solver-developer advice, add limitations, scope or reframe claims.
9. **Progress reporting as a research instrument.** Twice-yearly sponsor newsletters record numbers, failures and next steps per student. That is where negative results appear first.

## Contradictions (kept, not reconciled)

1. **OA "Part II".** 01 reads the 1984 GBD-relation report as never journal-published and possibly abandoned. The 1986 paper's own abstract (Springer) says it ends with "a theoretical comparison with generalized Benders decomposition", and its reference list cites the Part II report separately. Both can hold: no separate Part II paper, but part of its content in the 1986 paper. I did not read the 1986 full text.
2. **LD-SDA v2, abstract against conclusion.** The abstract says "consistently outperforms … especially as problem size grows". The conclusion says "the scalability of the LD-SDA still needs to be evaluated for larger superstructure problems, e.g., those resulting in more than 7 external variables."
3. **LD-SDA "future work" against the code.** v2 (27 Jan 2025): "Moreover, future work also involves the integration of the LD-SDA into the GDPOpt solver in Pyomo.GDP, making this algorithm available to a wider audience." The Pyomo LD-SDA code exists from 2024-02-04, and Pyomo 6.9.0 shipped it on 2025-02-21, 25 days after v2.
4. **Feasibility-pump paper, abstract against results.** The abstract: the comparisons "demonstrate the effectiveness of the proposed algorithm in terms of solution quality and solving time." The results: "a small performance loss with respect to solution time" when the pump is enabled in DICOPT (against DICOPT without it), a considerable time decrease once the pump's cuts are reused to initialize the OA master, and "SCIP is most efficient" in the comparison with other solvers.
5. **"No fine-tuning" against "modified limits".** The 2019 review says "we have not tried to fine-tune any of the solvers". The same appendix: "We have also modified limits and other parameters when it is apparent that implementation issues are the cause of … premature termination … or numerical instability". In addition, SHOT (two of the four authors among its developers) and DICOPT (the last author's group) are among the 15 solvers benchmarked. The developers are named in the solver descriptions; there is no explicit conflict-of-interest statement.
6. **IJOC manuscript, internal count.** "The algorithm was tested with 30 instances of five problems" (p. 19) against "Thirty six instances were solved." (p. 25). The results section also discusses "Dice" and "DiceH" problems that are not among the five families. The published 2015 version was not read, so whether this was fixed is unknown.
7. **DICOPT defaults against the group's later diagnosis.** The 2006 report calls the integer-cut default "often very ineffective". The 2017 paper names it as the reason DICOPT has "difficulty in finding a feasible solution". The default remains unchanged in the 2026 manual and is overridden only through the `convex` option.
8. **Wassick co-authorship.** Stated "at least you know 15 maybe even 20". The record shows 21 journal articles plus 4 other peer-reviewed items. An understatement, not a refutation.
9. **Bonmin test selection.** The 2005 report presents "a new publicly available library of test instances" as a contribution. Its 41-problem test set was selected by solvability with the authors' own earlier hybrid code. These are kept side by side.

## Gaps

- **Referee reports and rebuttals**: none public for his journal papers. The OpenReview forum of the NeurIPS 2025 paper exists, but the API and page returned a challenge, so its reviews were not read.
- **The 1992 comment and response** (Salcedo; Diwekar–Grossmann–Rubin): content not read (ACS 403; 1 WebSearch, no result).
- **Correction contents** not read: Lee & Grossmann 2001 erratum (ScienceDirect 403); Ye et al. 2020 corrigendum; the two 1992 I&ECR errata; the 2020 cutpoint correction.
- **Published versions not compared with the manuscripts read**:
  - Quesada & Grossmann 1992: whether the nonconvex section was dropped (no abstract via OpenAlex or Semantic Scholar);
  - the feasibility-pump paper 2019/2020; regularized OA 2020; Pyomo.GDP 2021/22 (OSTI holds only the submitted version); Bonmin 2008; IJOC 2015.
  - The 1986 OA paper itself was not read (only abstract and reference list), so the test-problem details there are inferred from MINLPLib, the 1988 report and the erratum.
- **CAPD newsletters 2010–2022** are marked "only available to CAPD sponsors" and were not accessed, by rule. Of the roughly 25 public 2000–2009 issues, 6 were read (plus one e-newsletter).
- **Grossmann's own code**: no repository authored by him was found. The original DICOPT Fortran and the legacy codes behind the web interfaces are not public. The interfaces were not executed.
- **The Optimization Online date (2016) of the FSG paper** is taken from the Pyomo docstring; the Optimization Online page was not opened.
- **Personal share**: for 2013–2026 artefacts, Grossmann's individual role in test-set design or revision decisions cannot be separated from his co-authors'.
- **Search budget**: 1 WebSearch used; everything else came from curl, WebFetch and APIs.

## Sources

Primary (Grossmann's papers, reports and their versions; his group's code, records and reports):
1. M. A. Duran, I. E. Grossmann, "An outer-approximation algorithm for a class of mixed-integer nonlinear programs", *Math. Program.* 36(3):307–339, 1986. DOI 10.1007/BF02592064. Springer page: abstract and 47-item reference list read; full text not read. (primary)
2. M. A. Duran, I. E. Grossmann, Erratum, *Math. Program.* 39(3):337, 1987. DOI 10.1007/BF02592081. Read in full. (primary)
3. M. A. Duran, I. E. Grossmann et al., "Mixed-integer programming: is it a useful tool in process synthesis?", DRC report, 1983. KiltHub DOI 10.1184/R1/6467171.v1. One sentence re-verified. (primary)
4. G. R. Kocis, I. E. Grossmann, "Computational experience with DICOPT solving MINLP problems in process systems engineering", EDRC-06-43-88, Jan 1988. KiltHub DOI 10.1184/R1/6466841.v1. Journal version *Comput. Chem. Eng.* 13(3):307–315, 1989, DOI 10.1016/0098-1354(89)85008-2. Report read in part (pp. 3, 8, 10–15, 23, 25). (primary)
5. I. Quesada, I. E. Grossmann, "An LP/NLP based branch and bound algorithm for MINLP optimization", EDRC 06-123-92 (dated December 1991). KiltHub DOI 10.1184/R1/6466757.v1. Journal version *Comput. Chem. Eng.* 16(10–11):937–947, 1992, DOI 10.1016/0098-1354(92)80028-8. Report read in part (pp. 16, 18, 23–24, 31). (primary)
6. P. Bonami, L. T. Biegler, A. R. Conn, G. Cornuéjols, I. E. Grossmann, C. D. Laird, J. Lee, A. Lodi, F. Margot, N. Sawaya, A. Wächter, "An algorithmic framework for convex mixed integer nonlinear programs", report of 31 Oct 2005. KiltHub DOI 10.1184/R1/6466718.v1. Journal version *Discrete Optim.* 5(2):186–204, 2008, DOI 10.1016/j.disopt.2006.10.011. Report read in part (pp. 10, 12, references). (primary)
7. F. Trespalacios, I. E. Grossmann, IJOC manuscript, https://egon.cheme.cmu.edu/Papers/Trespalacios_JOC-2013-07-OA-119.pdf. Journal version *INFORMS J. Comput.* 27(1):59–74, 2015, DOI 10.1287/ijoc.2014.0610. Read in part (pp. 19, 25–31). (primary)
8. D. E. Bernal, S. Vigerske, F. Trespalacios, I. E. Grossmann, manuscript of 22 Apr 2017, https://egon.cheme.cmu.edu/Papers/Bernal_Feaspump.pdf. Journal version *Optim. Methods Softw.* 35(1):171–190, 2020, DOI 10.1080/10556788.2019.1641498. Read in part (pp. 1–2, 10, 14–15). (primary)
9. J. Kronqvist, D. E. Bernal, I. E. Grossmann, manuscript of 14 Dec 2017, https://egon.cheme.cmu.edu/Papers/Kronqvist_Bernal_QOA.pdf. Journal version *Math. Program.* 180:285–310, 2020, DOI 10.1007/s10107-018-1356-3. Read in part (p. 19, conclusions). (primary)
10. J. Kronqvist, D. E. Bernal, A. Lundell, I. E. Grossmann, preprint of 3 Jun 2018, https://egon.cheme.cmu.edu/Papers/ConvexMINLPReview2018_OO.pdf. Compared sentence by sentence with source 11. (primary)
11. Same authors, "A review and comparison of solvers for convex MINLP", *Optim. Eng.* 20(2):397–455, 2019 (open access). DOI 10.1007/s11081-018-9411-8. Benchmark sections and appendix read. (primary)
12. Q. Chen, E. S. Johnson, D. E. Bernal, R. Valentin, S. Kale, J. Bates, J. D. Siirola, I. E. Grossmann, Pyomo.GDP manuscript "v6" (PDF of 9 Jun 2020), https://egon.cheme.cmu.edu/Papers/Chen_pyomo_gdp_v6.pdf. Journal version *Optim. Eng.* 23(1):607–642, 2022, DOI 10.1007/s11081-021-09601-7. Read in part (pp. 10, 22, 26, 28). (primary)
13. D. E. Bernal Neira, I. E. Grossmann, arXiv:2109.09657 v1 (2021-09-20) and v3 (2024-02-19). Journal version *Comput. Optim. Appl.* 88(1):251–312, 2024, DOI 10.1007/s10589-024-00557-9. v1 and v3 compared. (primary)
14. D. Ovalle, D. A. Liñán, A. Lee, J. M. Gómez, L. Ricardez-Sandoval, I. E. Grossmann, D. E. Bernal Neira, arXiv:2405.05358 v1 (2024-05-08) and v2 (2025-01-27). Journal version *Comput. Chem. Eng.* 195:108993, 2025, DOI 10.1016/j.compchemeng.2024.108993. Compared. (primary)
15. A. Galan, C. de Prada, G. Gutierrez, D. Sarabia, I. E. Grossmann, R. Gonzalez, "Correction to: Implementation of RTO in a large hydrogen network considering uncertainty", *Optim. Eng.* 20(4):1191–1192, 2019. DOI 10.1007/s11081-019-09446-1. Read in full. (primary)
16. CAPD Newsletter, June 2000, https://capd-archive.cheme.cmu.edu/NewsletterArchive/june2000.pdf. Grossmann-group section scanned. (primary)
17. CAPD Newsletter, December 2001, https://capd-archive.cheme.cmu.edu/NewsletterArchive/Dec2001.PDF. Scanned. (primary)
18. CAPD Newsletter, December 2003, https://capd-archive.cheme.cmu.edu/NewsletterArchive/December2003.pdf. Scanned. (primary)
19. CAPD Newsletter, January 2006, https://capd-archive.cheme.cmu.edu/NewsletterArchive/CAPD%20NewsletterJan06.pdf. MINLP/GDP sections read (pp. 6, 13–16). (primary)
20. CAPD Newsletter, August 2008, https://capd-archive.cheme.cmu.edu/NewsletterArchive/CAPDNewsletterAug08.pdf. Scanned. (primary)
21. CAPD Newsletter, August 2009, https://capd-archive.cheme.cmu.edu/NewsletterArchive/Newsletter%20August%2009.pdf. Scanned. The October 2006 e-newsletter, signed by Grossmann, was also opened. (primary)
22. Pyomo repository, https://github.com/Pyomo/pyomo, `main` at `b473cba` (2026-10-06). Read: `pyomo/contrib/gdpopt`, `pyomo/contrib/mindtpy` (code and tests), `pyomo/gdp/plugins/hull.py`, `CHANGELOG.md`, and the git history (31,465 commits). (primary record of the group's and Sandia's code)
23. Pyomo issue #3939, "GDPopt GLOA convex affine cuts use concave MC++ slopes", opened 2026-05-11 by `bernalde`, open at 2026-10-10, https://github.com/Pyomo/pyomo/issues/3939. Body and 2 comments read. (primary, lineage)
24. GDPlib, https://github.com/SECQUOIA/gdplib, `main` at `b4f7498` (2026-08-16). README and 23 model READMEs read. (primary for the lineage; secondary for Grossmann)
25. Grossmann Research Group, Software page, http://egon.cheme.cmu.edu (copy saved earlier in this run, re-read). (primary)
26. "Web-based software for Mixed Integer Programming Applications in Process Systems Engineering", https://newton.cheme.cmu.edu/interfaces/, read 2026-10-10. (primary, group)
27. CMU-IBM Cyber-Infrastructure for MINLP, library pages https://www.minlp.org/library/ (lib.php?lib=MINLP and lib=GDP), read 2026-10-10. (primary-institutional)
28. *Subject to: Ignacio Grossmann*, interview, uploaded 2024-02-08, https://www.youtube.com/watch?v=jNjqnsnUzhE. Caption transcript saved by agent 04 at `../sources/talks/2024-02-08_subject-to-interview_jNjqnsnUzhE.txt`; sections 0:41–1:18 read. (primary, caption-derived; re-check against audio before publishing a quote)
29. arXiv abstract pages (submission histories) of the 16 preprints, e.g. https://arxiv.org/abs/2109.09657, read 2026-10-10. (primary records)
30. Crossref records, metadata only, content not read:
    - the 1992 exchange: comment, DOI 10.1021/ie00012a027; response, DOI 10.1021/ie00012a028; original paper, DOI 10.1021/ie00001a042;
    - correction notices: DOI 10.1021/ie00004a041, 10.1021/ie00007a035, 10.1016/S0098-1354(01)00706-2, 10.1016/j.compchemeng.2019.106639, 10.1021/acs.iecr.0c05114. (primary items)

Secondary:
31. GAMS, DICOPT solver manual, https://www.gams.com/latest/docs/S_DICOPT.html (copy saved earlier in this run, re-read). (secondary; maintained by GAMS)
32. GAMS release notes: 24.5.1 major release of 23 Sep 2015, https://www.gams.com/latest/docs/RN_MAIN.html and RN_245.html. (secondary)
33. MINLPLib, https://www.minlplib.org/: `instancedata.csv` (1,633 instances); 335 instance pages, one per reference key; pages `synthes1`, `synthes3`, `ex4`, `batchdes`. Read 2026-10-10. (secondary)
34. LOGMIP website, http://www.logmip.ceride.gov.ar/ (reachable; minimal content). (secondary)
35. GitHub API metadata for `infiniteopt/DisjunctiveProgramming.jl` and `hubbs5/or-gym`, read 2026-10-10. (secondary)
36. Crossref co-author query "Grossmann Wassick" (28 matching records, 2008–2026), 2026-10-10. (secondary)
37. Crossref verification of 43 DOIs and 10 title queries, 2026-10-10. (secondary)
38. OpenReview API search: NeurIPS 2025 record `ZvUZvT8tgg` (metadata only). (secondary)
39. Semantic Scholar API records for the correction notices (metadata; abstracts elided). (secondary)
40. OpenAlex record for Quesada & Grossmann 1992 (no abstract). (secondary)
41. CAPD newsletter listing, https://capd-archive.cheme.cmu.edu/newsletters.html (shows which issues are sponsor-only). (secondary)
42. WebSearch, 1 query on the 1992 Salcedo comment; no relevant result. (secondary)

Other works named (identifier checked against Crossref in this run, content not read unless stated): Kocis & Grossmann 1988, DOI 10.1021/ie00080a013; Viswanathan & Grossmann 1990, DOI 10.1016/0098-1354(90)87085-4; Kravanja & Grossmann 1990, DOI 10.1016/0098-1354(90)80018-7; Kravanja 2010, DOI 10.1016/j.compchemeng.2010.04.017; Sahinidis & Grossmann 1991, DOI 10.1021/ie00054a015; Birewar & Grossmann 1990, DOI 10.1021/ie00107a008; Raman & Grossmann 1994, DOI 10.1016/0098-1354(93)E0010-7; Fletcher & Leyffer 1994, DOI 10.1007/BF01581153; Türkay & Grossmann 1996, DOI 10.1016/0098-1354(95)00219-7; Lee & Grossmann 2000, DOI 10.1016/S0098-1354(00)00581-0; Lee & Grossmann 2001, DOI 10.1016/S0098-1354(01)00732-3; Grossmann & Lee 2003, DOI 10.1023/A:1025154322278; Furman, Sawaya & Grossmann 2020, DOI 10.1007/s10589-020-00176-0; Bernal, Chen, Gong & Grossmann 2018, DOI 10.1016/B978-0-444-64241-7.50144-0; Ye, Grossmann & Pinto 2018, DOI 10.1016/j.compchemeng.2017.08.013; Galan et al. 2019, DOI 10.1007/s11081-019-09444-3; Franzoi et al. 2020, DOI 10.1021/acs.iecr.0c02868; Kakkad et al. 2024, DOI 10.1007/s11081-024-09887-3; Kronqvist, Bernal Neira & Grossmann 2026 (EJOR), DOI 10.1016/j.ejor.2025.07.016 (one sentence read in the copy saved by agent 01); Ovalle, Bhatia, Laird & Grossmann 2026, DOI 10.1021/acs.iecr.5c02853; Erdirik-Dogan, Grossmann & Wassick 2008, DOI 10.1021/ie701682m; Sun et al. 2026, DOI 10.1016/j.compchemeng.2026.109654; DisjunctiveProgramming.jl, JuliaCon Proc. 2023, DOI 10.21105/jcon.00117; OR-Gym, arXiv:2008.06319; NeurIPS 2025 paper, arXiv:2506.03531. The three product-positioning papers (Albers & Brockhoff 1977; Gavish, Horsky & Srikanth 1983; Zufryden 1979) are named with venue, year and title exactly as printed in the 1986 paper's reference list; they were not checked separately.
