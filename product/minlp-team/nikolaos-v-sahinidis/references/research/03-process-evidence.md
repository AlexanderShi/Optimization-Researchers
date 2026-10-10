# 03 · Process evidence: what Sahinidis actually does

> **Researcher**: Nikolaos V. ("Nick") Sahinidis · Google Scholar `PTXe50QAAAAJ` · DBLP pid 123/7012 · ORCID 0000-0003-2087-9131 · homepage https://sahinidis.coe.gatech.edu/
> **Dimension**: research agent 03 of 06, process evidence (nuwa research-craft Phase 1), MINLP Team
> **Research date**: 2026-10-10
> **Sources consulted**: 66, listed under "Sources" (53 primary, 13 secondary or observed). For 17 of them I used only the abstract, the metadata, the titles or an index listing, or could not open them at all: the full text is closed, the server refused access, or only the dates were needed. Each such item is marked in the list. WebSearch calls used: 2 of 3.
> **Identifiers**: I resolved every DOI in this file in this run, through the Crossref REST API (DataCite DOIs through doi.org or the hosting repository), and every arXiv id through the arXiv API. A script then compared the finished file with the lists of checked identifiers (see the end of "Sources").
> **Method**: I looked for behaviour, not statements, and read:
> 1. the public records of his software: the BARON, ALAMO and BAM release notes, manuals and FAQs of his company, The Optimization Firm (TOF); the 2000 BARON manual and the 1998–2005 BARON web pages through the Wayback Machine; the benchmark slide deck, example models, test libraries, raw benchmark results and README files on his group site and on minlp.com;
> 2. the experimental sections of 12 papers and one PhD thesis from his group (full text, open access or arXiv);
> 3. the early and final versions of 4 arXiv preprints that have several versions;
> 4. four newsletters of the CMU Center for Advanced Process Decision-making (CAPD), January 2008 to August 2009 (Wayback copies), which print his group's progress report each semester;
> 5. outside checks on his work: an independent solver comparison (Neumaier et al. 2005), a prize citation (Optima 73), a Dagstuhl working-group report, Hans Mittelmann's 2026 benchmark pages, the QPLIB paper, OpenReview, Crossref (errata and retractions) and GitHub;
> 6. two talk transcripts (§B1, §B3, §C3, §E2).
> **Local corpus**: when this run started, `references/sources/papers`, `talks`, `essays`, `software` and `publications` held only `.gitkeep` files. There is no user-supplied material, so nothing below is marked "from user-supplied material". I did not open `references/sources/private/`.
> **Talk transcripts**: during this workflow a parallel research agent saved two YouTube auto-caption transcripts of his talks under `sources/talks/`: the UConn lecture of 10 April 2017 and the Texas A&M lecture of 5 March 2025. I read both and cite them as [stated, P, ASR]. They are machine captions that no human has checked, so I quote only short clean fragments with their timestamps and paraphrase the rest. I saved no transcript myself.
> **Earlier scratch**: an interrupted earlier run of this agent had left downloads in the shared scratch folder. I used that folder only as a list of leads. I fetched every source cited below again in this run and read the new copy.
> **Relation to 01 and 06**: `01-publications.md` dissects the signature works. `06-trajectory.md` gives the timeline and lists several bugs from the release notes. I do not repeat their content. Where I build on them I write "see 01 §…" or "see 06 §…". I re-read every quotation in this file myself in this run.
> **Tags**:
> - [stated]: he, his group or his firm said or wrote it.
> - [practice]: the record shows it was done (code, release notes, data files, papers, dates).
> - [observed]: others wrote it.
> - [inferred]: my reading, which no source states.
> - **P** = primary, **S** = secondary.
> - "Group" means his students, postdocs and co-authors on a paper.
> - "TOF" means The Optimization Firm, LLC, of which he is CEO. Its unsigned web pages and release notes record the projects he leads; they are not his personal statements. I tag them [practice], or [stated, TOF].
> **Quoting**: quotations are verbatim. I rejoined words hyphenated at PDF line ends. I removed spaces that the HTML-to-text conversion had put around inline code ("1e-6 ," became "1e-6,"), and collapsed runs of spaces inside quoted lines of model files. Where a source uses curly apostrophes, I kept them. Page numbers are printed page numbers. For arXiv preprints the page numbers are PDF pages, and for the thesis I give section numbers.

---

## Process patterns at a glance

Each pattern is documented in the section named in brackets. The patterns are my reading of the evidence there [inferred]; the evidence itself is [practice].

1. **The solver works as his lab notebook.** Results go into BARON (or ALAMO or BAM) first, and the papers later describe what the code already does. The release notes are dated and specific, and they name serious bugs. [§A1, §A3]
2. **Every paper leaves a test library behind, and the library then joins the development set.** Of the 23 libraries that TOF says it routinely uses to develop BARON, 13 come from his group's papers. [§A2]
3. **One standard protocol for a decade.** GAMS, one thread, 500 s, optimality gaps of 10^-6, and the same Xeon X5650 machine class from 2014 to 2026. Old BARON versions are rerun on the same hardware to measure progress. Ablation means switching a feature off inside the production solver. [§B1–B2]
4. **Baselines are chosen so that the comparison measures one thing.** Only codes that allow the ablation are included. Commercial MIP solvers are forced into global mode. The strongest ML baseline runs on its best hardware. A closed-source solver is wrapped rather than skipped. [§B2–B3]
5. **A deterministic global solver supplies the ground truth.** Success rules are explicit and raw results are published. [§B4, §A2]
6. **Special classes and cheap prototypes come first** (specialized modules in 1998, GAMS prototypes, a Python prototype on a laptop). General code comes later. [§C1–C2]
7. **He enters a new area with a benchmark; his own algorithms follow about a decade later.** [§C3]
8. **Debugging runs through users' models.** The manual asks users to "send us the .bar file". Release notes credit fixes to customer models and to outside test frameworks. Features are disabled when they misbehave and later "reactivated after multiple fixes". [§D1, §A3]
9. **Numerical safety and determinism are engineered into the code.** Answers from subsolvers are checked before use, and the code uses safe LPs, ULP-aware comparisons, work units and pinned seeds. [§D2–D3]
10. **Papers report losses and null effects; product pages report wins.** [§E3–E5]
11. **Criticism is met by cooperation and fixes, not by published rebuttals.** He adopted the protocol of the study that had found errors in BARON. [§E6]
12. **Projects are reported to sponsors every semester. Projects that produce no artifact disappear without announcement.** [§G1, §H]

---

## A. The working unit: a solver, a test library, a release (layers 4 and 7)

### A1. Code first, paper second

- **Fourier–Motzkin presolve.** The BARON release notes record the technique before the paper was submitted:
  - 2023.11.4: "Improvements in CBC-based MIP relaxations and Fourier-Motzkin elimination."
  - 2024.3.1: "Improvements in Fourier-Motzkin elimination implementation."
  - 2024.5.8: "Extended Fourier-Motzkin elimination to certain integer-variable cases."
  - 2026.9.10: "Fourier-Motzkin elimination extended to linear columns that appear in nonlinear rows."

  The paper (Zhang, Ploskas & Sahinidis, *Math. Program. Comput.* 18:345–378, 2026, DOI 10.1007/s12532-026-00316-3) carries the dates "Received: 20 March 2024 / Accepted: 17 March 2026". It states: "Code availability The code developed during this research is embedded in the BARON solver." (p. 376). The technique was therefore in BARON before the paper was submitted. [practice, P] Era: Georgia Tech and TOF, 2023–2026. The first author is TOF's research scientist (§G2).
- **Student theses become solver modules.** Nohra's CMU thesis (2020, DOI 10.1184/R1/12584804.v1) says: "The new relaxation and branching techniques are implemented in BARON, and tested by conducting numerical experiments on a large collection of problems." (§1.2, in the outline of chapter 3). The CAPD report of January 2009 states the general rule: "Their results are, from time to time, incorporated into BARON." (p. 36). [stated, P] 01 §4 lists the theses that became modules.
- **Who maintains the code.**
  - January 2008: "Nick Sahinidis and Mohit Tawarmalani are currently maintaining the BARON software." (CAPD newsletter, p. 33).
  - January 2009: "Nick continues the development of BARON, primarily in collaboration with his former student Mohit Tawarmalani" (p. 35).
  - 2026, TOF's Our Team page: "Besides the many developers working to advance the BARON and ALAMO projects worldwide, meet our essential commercialization team."
  - The 2026 manual names a single author: "Nick Sahinidis, The Optimization Firm, LLC". [stated, P]
  - The benchmark slide deck on his group page (comparisons.pptx) lists "Nick Sahinidis" as creator and last editor in its file metadata: created 1998-08-15, modified 2014-12-13, revision count 2390. [practice, P] That he edits the benchmark slides himself is [inferred]; metadata can be inherited from a template.
- **Size and form of the code over time** (BARON manual v4.0, revision of 28 June 2000, §1.1, pp. 1–2):
  - Version 1, 1991–93: "The first version of BARON was merely 1800 lines of code written in the GAMS modeling language [2] in 1991-93 when duality-based range reduction techniques were developed [16]."
  - Version 2, 1994–95: about 10,000 lines of FORTRAN 77.
  - Version 3.0, 1996–97: "approximately 23,000 lines of FORTRAN 90 code and 10,000 lines of code written in C".
  - Version 4.0: "approximately 26,000 lines of FORTRAN 90 code and 17,000 lines of code written in C."

  The manual describes each version together with the application classes it was "applied to". [stated, P]
- Era and resources: this pattern needs a code base under his control since 1991 and, since 2001, a company that sells it. An early-career researcher cannot copy it wholesale; 06 §8 gives an adjusted version (own a small code base). [inferred]

### A2. Every paper leaves a test library behind

- **The BARON development set.** TOF's "Optimization Test Problems" page: "The following test libraries are routinely used in the context of developing BARON. Some of these problems originate from applications, while others have been designed to test, develop, or challenge solvers:". It lists 23 libraries. Most come in BARON, GAMS, MATLAB and Pyomo format; `euclidlib` has no MATLAB version, `minlprlp` comes in BARON, GAMS, LP and MPS, and `inf` also comes in MPS. [practice, P] I matched each library to the source the page names.
  - **13 come from the group's own papers**:
    - `qcqp`: Bao, Sahinidis & Tawarmalani, *Optim. Methods Softw.* 24:485–504, 2009, DOI 10.1080/10556780902883184.
    - `qcqp2`: Bao, Sahinidis & Tawarmalani, *Math. Program.* 129:129–157, 2011, DOI 10.1007/s10107-011-0462-2.
    - `mult3`, `mult4`, `qcqp3`: Bao, Khajavirad, Sahinidis & Tawarmalani, *Math. Program. Comput.* 7:1–37, 2015, DOI 10.1007/s12532-014-0073-z.
    - `inf`: Puranik & Sahinidis, *INFORMS J. Comput.* 29:754–766, 2017, DOI 10.1287/ijoc.2017.0761.
    - `bcp`: Puranik & Sahinidis, *J. Glob. Optim.* 67:59–77, 2017, DOI 10.1007/s10898-016-0491-8.
    - `sr`: Cozad & Sahinidis, *Math. Program.* 170:97–119, 2018, DOI 10.1007/s10107-018-1289-x.
    - `boxqpx2`, `eiqp2`, `qsap1`: Nohra, Raghunathan & Sahinidis, *SIAM J. Optim.* 31:142–171, 2021, DOI 10.1137/19m1271762.
    - `minlprlp`: Zhang, Ploskas & Sahinidis 2026 (above).
    - `euclidlib`: the page attributes it to a 2026 *SIAM Review* article by Kuznetsov and Sahinidis. I could not verify that article (no Crossref or arXiv record), and 06 reports the same absence.
  - **10 are external**:
    - `global`, `minlp`, `prince`: MINLPLib.
    - `ibm`: the CMU-IBM project.
    - `mpec`: MPECLib.
    - `morg`: minlp.org.
    - `binqp`: OR-Library.
    - `boxqp`: Vandenbussche and Nemhauser.
    - `poly`: two papers by Sherali et al.
    - `lgmiqp`: Lima and Grossmann.
  - So each new problem class the group studies ends up as a public library. The library then joins the set on which every later BARON version is developed. [inferred]
- **The Fourier–Motzkin paper builds its own library on purpose**: "we collect the root-node LP relaxations from SCIP 8.0 [7] for the problems in the MINLP benchmark library MINLPlib [11], forming the LP library we call MINLPrLPLib". The library is released on minlp.com (Zhang, Ploskas & Sahinidis 2026, §5). [practice, P]
- **The BAM development set is the group's two published DFO benchmarks.** TOF's "Black-box Optimization Test Problems" page: "On this page, we maintain a collection of black-box optimization problems that we routinely use to develop BAM." It offers two sets:
  - `rs13`: the 502 problems of Rios & Sahinidis 2013.
  - `ps22`: the 267 problems of Ploskas & Sahinidis 2022.

  Both come as Python files, C and Fortran API sources, simulation executables for five platforms, Fortran sources and BAM input files; rs13 also comes with optimal solutions. [practice, P] This matters for §E2.
- **Raw benchmark results are published with the paper.** The page that accompanies Rios & Sahinidis 2013 (https://sahinidis.coe.gatech.edu/dfo) says: "Here, we provide all test problems and detailed results that can be used to (a) reproduce the results of the paper and (b) facilitate comparisons with other derivative-free optimization algorithms." [practice, P]
  - The page offers GAMS models grouped by class and by size, C and Fortran sources, the problem data, a results file for each of the 22 solvers, and separate "refinement ability" results.
  - The README says: "Ten instances were solved from randomly generated starting points." and "Columns 7-56 contain the best objective function value found by the solver every 50 function calls."
  - The starting points can be regenerated from a published matrix of random numbers: "File 'starting_points.xls' contains the information to generate the starting points."
  - The page for the mixed-integer study (https://sahinidis.coe.gatech.edu/midfo) repeats this structure for 13 solvers and 267 problems.
- **Student application problems become black-box benchmarks.** The group site's page "Test problems for SO and DFO algorithms" offers two of them, each with a problem description and Windows and Linux executables [practice, P]:
  - a cooling-crystallization solvent design problem (description dated 28 July 2014; authors Nick Austin and Nick Sahinidis);
  - a polymer design problem (April 2021; Yijia Sun and Nick Sahinidis).
- **The 2014 BARON comparison set is still the one on the group page.** The page says: "A systematic comparison on 1740 test problems shows that BARON has an edge over other global codes for NLP/MINLP." and "This test set includes all problems from these libraries that are accepted by all solvers." The four zip files have HTTP Last-Modified dates of December 2013 and June 2014. [practice, P] The protocol is in §B1; contradiction C4 discusses its age.
- **The data URLs printed in the papers break, but the data survive.** [practice, P]
  - The 2013 paper prints "All test problems are available at http://archimedes.cheme.cmu.edu/?q=dfocomp." (p. 1266). On 2026-10-10 that address redirected to an HTTPS address that failed the TLS handshake.
  - The 2022 paper prints "All data generated or analyzed during this study are available from https://sahinidis.coe.gatech.edu/bbo?q=midfo" (p. 459). That address returned HTTP 404.
  - Both data sets are now at /dfo and /midfo.
- Era: the DFO libraries were built at CMU in 2008–2012 with NIH, NETL and NSF money (01 §SW3). Today the firm hosts the libraries.

### A3. Releases as a public record of errors

- **Cadence.** [practice, P]
  - BARON: 65 dated releases from 2022.1.19 to 2026.9.10 (13 in 2022, 14 in 2023, 14 in 2024, 18 in 2025, 6 up to September 2026).
  - ALAMO: 108 dated releases from "2013.10" to 2026.9.10.
  - BAM: 19 releases in 2025–2026.
- **Severity is named.** The BARON notes call 11 fixes "serious" or "major". Examples: "Serious fix in initialization that led to BARON ignoring variable bounds, although rarely affecting problems." (2026.5.28) and "Major fix in violation calculations that had previously zeroed out violations for variables at bounds." (2022.12.18). The ALAMO notes do the same: "Fixed a major bug in the adaptive-sampling routine that had effectively disabled adaptive sampling." (2020.4.25). 06 §6 quotes further cases, including a bug that stayed hidden from 2013 to 2018. [practice, P]
- **The notes name where bug reports came from**:
  - "identified through customer test cases" (BARON 7.0–7.9, 2004–2007);
  - "Following extensive testing of BARON 5.0 by external groups, BARON 6.0 incorporated those fixes" (6.0, 2002–2003);
  - "Fix in the flowers module identified through a customer-reported problem." (2024.1.5);
  - "Fix in the SOCP recognition routine for a customer-reported model." and "Fix in range reduction for a customer-reported QCQP model." (2024.2.29);
  - "Fix in the reformulator to address a customer report." (2024.3.10);
  - "Range reduction made more conservative in response to a customer infeasibility report." (2025.3.19);
  - "Fix in convexity recognition identified during a run with GNU compilers." (2025.7.16);
  - "Fix in the range-reduction routine that addressed failures reported by the SECQUOIA testing framework." (2025.11.17).

  According to its GitHub organization page, SECQUOIA is a research group at Purdue's Davidson School of Chemical Engineering. I could not identify the testing framework itself (Gaps). [practice, P; SECQUOIA identity observed, S]
- **Disable, fix, reactivate.** A component is switched off when it misbehaves and comes back only after repair. Examples [practice, P]:
  - "Reactivation of flow-cover and GUB-cover cut generators after multiple fixes." (2023.11.4);
  - "Edge-concave relaxations reactivated after multiple fixes." (2024.9.12);
  - "Reactivated identification of implied knapsack constraints in cut generation." and "Reactivated clique merging in presolve." (2025.2.1);
  - "Reactivated Gomory cuts, now using linked lists and hash tables for the row-similarity structure." (2025.9.29).
- **Negative engineering results are recorded too**: "Reset CLP's primal-column-steepest pricing to its original version after testing showed no benefit from modifications." (2025.7.29). [practice, P]
- **The firm's products test each other.** "Fixed overflows in monomial reduction that had led to incorrect infeasibility claims for ALAMO-generated models with poor numerical scaling." (BARON 2025.7.10). Since 2022.6.4 ALAMO uses an embedded BARON for all its internal optimization, and BAM embeds both. [practice, P]
- **Benchmark results are tracked from version to version**: "In comparison to the September 2022 version, the average speedup on the entire MINLPlib is approximately 1.7x in geometric mean." (2023.1.5). Another note warns that library numbers miss what customers see: "The new version leads to orders-of-magnitude speedups for difficult problems supplied by customers. Problems in standard test libraries such as MINLPlib and GlobalLib are not affected as much." (2022.1.19). [stated, TOF, P] There are therefore two test populations: public libraries and customer models, and only the first is public. [inferred]

---

## B. How baselines and test problems are chosen (layer 4)

### B1. One standard protocol for global-solver experiments (2014–2026)

| Year | Source | Machine | Limit and tolerances | Other conditions |
|---|---|---|---|---|
| 2014 | Comparison slides (comparisons.pptx, slide 1) | 64-bit Intel Xeon X5650, 2.66 GHz | 500 CPU seconds; optca and optcr of 1e-6 | "Each BARON run restricted to single processor"; "All experiments under GAMS"; performance profiles made with the GAMS performance tools; BARON 14.4.0 against Antigone 1.1, Couenne 0.4, LindoGlobal 9.0 and SCIP 3.1 |
| 2017 | Puranik & Sahinidis, arXiv:1706.08601 v1, p. 16 | "All computational tests were run on a 64-bit Intel Xeon X5650 2.66 Ghz processor running CentOS release 7." | 500 s; absolute and relative optimality tolerances of 10^-6 | BARON, Couenne and SCIP under GAMS |
| 2018 | Khajavirad & Sahinidis, abstract (DOI 10.1007/s12532-018-0138-5) | "a standard workstation" | 500 s | 369 GlobalLib, 250 MINLPLib, 980 PrincetonLib and 142 IBMLib problems |
| 2020 | Nohra thesis §2.4 and §3.6 | "All experiments are performed under GAMS 24.6.1 on a 64-bit Intel Xeon X5650 2.66Ghz processor running CentOS release 7." Later: "all experiments are conducted under GAMS 30.1.0 on a 64-bit Intel Xeon X5650 2.66GHz processor with a single-thread." | 500 s; relative and absolute tolerances of 10^-6 | — |
| 2025 | Zhang & Sahinidis, *Optim. Lett.* (DOI 10.1007/s11590-025-02208-2), p. 10 | — | 500 s; absolute and relative gaps of 10^-6 | — |
| 2026 | Zhang, Ploskas & Sahinidis, *Math. Program. Comput.* 18, §5 | "The computations were performed on a 64-bit Intel Xeon X5650 2.55 GHz processor." | CPLEX with a 3,600 s limit (an LP study) | — |

- The comparisons of his global solver ran under one protocol for about a decade, and the CPU model stayed the same from 2014 to 2026. [practice, P]
- **The version history itself is benchmarked on fixed hardware.** In his March 2025 Texas A&M lecture (auto-captions, [0:18:41]–[0:20:16]) he shows BARON results "over a 20 some year uh time period". The test set is one he calls "a collection of problems that I don't necessarily like"; he says someone else had been using it until very recently to benchmark MINLP solvers. His summary: from solving about one problem in three at the start to almost the whole collection, at about 40 times the speed. He explains the method: "I'm running now different versions of the algorithm on the same Hardware that's how I'm doing this comparison". He adds that "we're not able to solve all the problems". [stated, P, ASR] This is the same logic as the fixed benchmark machine above: hold the hardware and the test set constant, vary only the code. [inferred]
- [inferred] Fixed hardware and fixed limits make results comparable across a decade of papers and BARON versions. The cost is that absolute times are measured on an ageing machine. See C7 for the change in clock speed.

### B2. Ablation inside production solvers, and only against solvers that can be ablated

- **Choice of competitors.** In Puranik & Sahinidis (*Constraints* 22:338–376, 2017, DOI 10.1007/s10601-016-9267-5; arXiv:1706.08601 v1) the competitors are chosen by the ablation they allow: "The global MINLP solvers Antigone [135] and LindoGlobal [117] are also available under GAMS but were not used in these experiments since they do not offer facilities that turn off their presolve routines." (p. 15). [practice, P]
- **Scope is limited, and stated.** "Comparing the relative impact of the individual reduction techniques on the performance of global solvers is beyond the scope of this work." (p. 16).
- **How to read the figures.** "It should be pointed out that no comparisons are possible between BARON and Couenne by looking at their respective performance profiles since these profiles depend solely on the solvers included in each figure." (p. 16).
- **Results by library.** "In the sequel we present results for each library separately so as to demonstrate that the observed trends are not dominated by any particular library, convexity, or integrality properties." (p. 16). [practice, P]
- **Named builds as the unit of ablation.** In Nohra's thesis each variant has a name: BARONctf against BARONdef in §2.4, and BARONqp1, BARONqp2, BARONnoqp and BARONqcr in §3.6. [practice, P]
- **An oracle bound before learning.** In the graph-network probing paper (Zhang & Sahinidis 2025), every instance was solved with and without probing first, which gives a per-instance "Best" setting. "Overall, we observe that perfectly selecting the probing settings can reduce solution times by approximately 40% for the MINLP collection and 25% for the NLP collection." (p. 10). The learned model is then judged against this ceiling. [practice, P]
- **Turning the DFO benchmark on his own solver.** Liu, Ploskas & Sahinidis (*J. Glob. Optim.* 74:611–637, 2019, DOI 10.1007/s10898-018-0640-3; abstract only) use 27 DFO solvers to tune BARON's options on "A set of 126 problems from the GLOBALLib and MINLPLib collections". [practice, P]
- Era: CMU 2013–2020 (Puranik, Nohra, Liu) and Georgia Tech/TOF 2024–2025 (Zhang). The pattern requires owning the production solver (§A1).

### B3. Baselines get their best settings, or are wrapped when the code is closed

- **Forcing MIP solvers into global mode** (Nohra thesis §3.6): "When dealing with nonconvex problems, we: (i) run all solvers with relative/absolute tolerances of 10-6 and a time limit of 500 seconds, and (ii) set the CPLEX option optimalitytarget to 3 and the GUROBI option nonconvex to 2 in order to ensure that these two solvers search for a globally optimal solution." [practice, P]
- **Wrapping a closed-source baseline** (Fourier–Motzkin paper, p. 365): "Since we do not have access to CPLEX's internal source code and cannot directly integrate FME into its presolve phase, we instead apply the FMEpre algorithm to models already presolved by CPLEX, then feed them back into CPLEX for solving."
- **Choosing a mode that isolates the effect** (p. 367): "The default CPLEX was not chosen for comparison because it may combine the use of the barrier algorithm methods and variants of simplex methods, which cannot provide clean and interpretable results."
- **Removing uninformative instances** (same section): "Trivial problems (solved within one second by CPLEX with and without FME) and timeout problems (instances which CPLEX cannot solve within an hour no matter whether FME is used or not) are eliminated from our collection." [practice, P]
- **The strongest ML baseline on its best hardware** (Bayramoğlu, Nemhauser & Sahinidis, arXiv:2604.00094 v1) [practice, P]:
  - "In GNN-G, the GNN inference is executed on a high-end GPU." (p. 11)
  - "We use the validation sets to tune hyperparameters for our models and all baselines, and we use the test sets to measure how accurately each method approximates SB decisions." (p. 6)
  - "Problem sizes and generators match those in Gasse et al. (2019) to enable direct comparison." (p. 6)
  - "All MIP solves run in a single-threaded mode and in isolation to avoid interference from other jobs." (p. 11)
  - "Finally, for each problem domain, we create five independent training datasets by varying the random seed used to select SB data tuples."
  - "Finally, to ensure data quality, we discard any node where SB triggers numerical issues and SCIP reports errors." (p. 8)

  The study runs on SCIP 8.0.0 rather than on BARON, so the comparison stays on the GNN authors' own ground. [practice, P; the motive is inferred]
- **Competitors get the ground-truth ingredients.** In the 2017 UConn lecture ([0:38:08]) he describes ALAMO's comparison with other modeling approaches on "a collection of 45 simple problems". The problems were posed to the modeling techniques as black boxes, and "all these modeling techniques have access to the true basis functions", so the comparison tests model selection, not the basis library. In the 2025 Texas A&M lecture ([0:28:30]) the same comparison appears on "a collection of 45 problems that we synthesized", eight years later. [stated, P, ASR]
- **His own tool as one baseline among others.** In the probing paper the classical baselines include ALAMO, and the paper reports where it wins and where it loses: "ALAMO achieves the best recall and F1-score, effectively classifying correctly more positive instances but with lower accuracy" (p. 11). [practice, P]
- **Application papers report the better general solver** (Li, Dey & Sahinidis, arXiv:2307.07648 v3, p. 18): "As a result, we focused on SCIP and BARON and we report the results on solving the MINLP formulation with BARON, which performed better in our tests." [practice, P]
- **RL is benchmarked against exact models** (OR-Gym, arXiv:2008.06319): the RL agents are compared with MILP models solved by Gurobi 8 and with a robust-optimization model solved by BARON 19. [practice, P]

### B4. The DFO benchmarking protocol (2013, 2022, 2025)

**2013, continuous** (Rios & Sahinidis, *J. Glob. Optim.* 56:1247–1293, DOI 10.1007/s10898-012-9951-y). All items [practice, P]; 01 §SW3 covers the headline results.

- **Test set.**
  - Problems are limited to at most 300 variables with bound constraints only, "As most of the optimization packages tested in this study were designed for low-dimensional unconstrained problems" (§7.1).
  - The 502 problems come from six sources. The published problem list has six source labels: PrincetonLib, GlobalLib, Richtarik, Nesterov, Conn et al. and Luksan–Vlcek.
- **Budget, justified by cost.** "To put this limit in perspective, 2,500 function evaluations for the bioremedation model of [98], which represents a typical application of derivative-free optimization methods to expensive engineering problems, would run for about 200 CPU days." (p. 1266)
- **Identical conditions for all solvers.**
  - Missing bounds were set to [-10,000, 10,000].
  - Solvers that do not accept bounds received a constant large objective value outside the box.
  - All solvers got the same random starting points, ten per problem (§7.2).
- **Success rule.** "A solver was considered to have successfully solved a problem during a run if it returned a solution with an objective function value within 1 % or 0.01 of the global optimum, whichever was larger." (p. 1267)
- **Ground truth.** BARON supplied the global optima, and LINDOGLOBAL was used where BARON cannot read the functions (p. 1267; quoted in 01 §SW3).
- **Defaults, with developers allowed to set them.**
  - "Even for less expensive functions, most typical users of optimization packages are not experts on the theory and implementation of the underlying algorithm and rarely explore software options." (p. 1268)
  - Therefore, "following the approach of [102] in a recent comparison of optimization codes, comparisons were carried out using the default parameter values for each package, along with identical stopping criteria and starting points across solvers" (pp. 1268–1269).
  - Reference [102] is Neumaier, Shcherbina, Huyer & Vinkó 2005, the independent study that had reported wrong answers from BARON 7.2 (§E6).
- **Developer rounds and a hold-out set.**
  - "In an effort to encourage developers to revise and improve their software, we shared our computational results with them over several rounds." (p. 1249)
  - "The developers of DAKOTA, IMFIL, SID-PSM, and the TOMLAB solvers improved their codes [...] using feedback from our results." (pp. 1283, 1287)
  - The hold-out set (§7.12): "These additional test problems were obtained from the original ones via a transformation of variables that preserves smoothness and convexity characteristics but otherwise changes the problems considerably, including the shape of the objective functions and location of all local solutions." The transformation used condition number c = 2.
  - The outcome: "The results with and without the transformation were almost identical." (p. 1287)
- **What the data show.** No solver from his own group took part. The paper compares 22 codes by others. [practice, P]

**2022, mixed-integer** (Ploskas & Sahinidis, *J. Glob. Optim.* 82:433–462, DOI 10.1007/s10898-021-01085-0).

- **Test set constructed from MINLPLib 2.**
  - "Most of the original problems from the MINLPLib 2 library have constraints. In this paper, we are interested in solving bound-constrained mixed-integer problems, so we omitted the constraints." (p. 445)
  - "Moreover, we also used 79 continuous problems from the MINLPLib 2 library and imposed integrality constraints on the variables in order to have a representative sample of non-binary discrete problems." (p. 445)
- **Same ground-truth source and success rule as 2013.** "We used the general-purpose global optimization solver BARON [70] to obtain the global solution of each problem."
- **Changes from 2013**: five starting points instead of ten, an Intel Xeon W-2123 at 3.6 GHz, and no developer rounds: "Finally, we used the default algorithmic parameters for each solver, i.e., we did not tune solvers in any way to the problems at hand." (p. 445)
- **Outcome.** The winners were others' open-source codes: "The open-source solvers MISO and NOMAD were the best performers among all solvers tested." (p. 433). [practice, P]

**2023–2026, own algorithms enter the benchmark.**

- **Model-and-Search** (Ma, Rios, Zheng, Sahinidis & Rajagopalan, *Comput. Optim. Appl.* 92:889–921, 2025, DOI 10.1007/s10589-025-00686-9). It is tested on the same library: "We test MAS with a set of 501 black-box problems used as a test library in previous studies [30] and available from [31]." The budget is "An overall evaluation budget of 300 is imposed on each run." (p. 912). The baselines are local solvers only (DFO, BOBYQA, IMFIL, DAKOTA/PATTERN, NOMAD), which matches MAS's local design.
- **Branch-and-Model** (*Comput. Optim. Appl.* 85:337–367, 2023, DOI 10.1007/s10589-023-00466-3; abstract only) reports "Extensive computational experiments over 500 publicly open-source test problems and one industrially-relevant application".
- **A 2026 conference presentation** (Oh & Sahinidis, OSTI, DOI 10.2172/3031241; abstract only) extends the 2013 study to "42 data-driven optimization algorithms on a broad collection of 502 test problems". [practice, P]

### B5. Instance selection in joint libraries (QPLIB)

The QPLIB paper (Furini et al., *Math. Program. Comput.* 11:237–265, 2019, DOI 10.1007/s12532-018-0147-4; 13 authors, Sahinidis among them; submitted version read):

- It gathered instances from "the BARON library http://www.minlp.com/nlp-and-minlp-test-problems" among others (p. 14).
- It filtered them by difficulty: "Thanks to these extensive preliminary tests, we discarded all instances that are solved by at least 30% of the complete solvers within a time limit of 30 seconds." (p. 15)
- It refused to rank solvers: "A consequence of our focus is that this paper is not concerned with the performance of the very diverse available set of QP solvers; we will not report any data comparing them." (p. 2)

[practice, P, joint] His personal role in these choices is not stated (Gaps).

### B6. The quality-assurance view he co-signed with GAMS (2003)

Slides "Global Optimization with GAMS: Applications and Performance" by Bussieck, Lasdon, Pintér and Sahinidis (PDF dated 11 September 2003). [stated-joint, P]

- On benchmark design (slide 24): "Model selection decides about the "winner"".
- On reproducibility (slide 28): "Non-reproducible tests damage the reputation of a solver" and "Requirement: low cost replication of such results by an independent auditor (user/tester)".
- On tools (slide 30): PAVER is spelled out as "Performance Analysis and Visualization for Effortless Reproducibility".
- On risk (slide 27): "Risks of GO: raise expectation & fail to deliver".
- His practice matches: the 2014 slides use the GAMS performance tools, and Puranik & Sahinidis 2017 generate their performance profiles "through PAVER". [practice, P]

Who wrote which slide is unknown; the slides belong to a GAMS-led deck.

---

## C. What gets done first (layers 2 and 3)

### C1. Special classes first, visible in the software itself

01 §SW1 quotes the 2002 preface on this. The software record shows it directly.

- **1998.** The BARON page (Wayback, 1998-12-06) describes:
  - "A "core" module for global optimization of arbitrary problems as long as problem-specific lower and upper bounding routines are provided by the user."
  - 12 "specialized modules": separable concave quadratic, separable concave, Cobb–Douglas economies of scale, fixed charge, fractional, univariate polynomial, linear multiplicative, general linear multiplicative, mixed-integer convex quadratic, MILP, indefinite QP and factorable NLP.
  - "With the exception of the factorable nonlinear programming module, all other modules solve linearly constrained problems."
- **2000.** The manual devotes a chapter to "Using the Specialized Modules", among them "Module barmisdp: Mixed Integer Semidefinite Programming" (table of contents, p. 86). Its core component asks the user for Fortran routines, such as a feasibility checker for which "The user must decide on the tolerance to be used for constraint satisfaction." (§7.2.3, p. 53).
- **2026.** The manual mentions no modules.
- **The example files show the migration.** The univariate-polynomial example p2.bar contained, in August 2000, "// use BARON's specialized module for univariate polynomials" and "MODULE: POLY;". The current file on the group site has "MODULE: NLP;". Over the same period nlp1.bar lost its subsolver lines ("nlpsol: 2; //use MINOS as the NLP solver" and "lpsol: 4; //use SNOPT as the LP solver"). The Duran–Grossmann MINLP example minlp1.bar is byte-identical in 2000 and 2026.

All items [practice, P]. Era: UIUC, 1991–2000, Industrial Engineering, small grants (01 §1.1).

### C2. Cheap prototypes before production code

Prototypes are written in a modeling language or a scripting language, run on a few small problems, and moved into compiled code later. [practice, P; the summary is inferred]

- **BARON 1.0**: 1,800 lines of GAMS, 1991–93 (§A1).
- **Successive LP, 2008–09.**
  - "During this summer, Yiqi has implemented a simple successive linear programming algorithm under the GAMS environment. He has successfully solved a small collection of twenty small test problems" (CAPD, August 2008, p. 36).
  - Six months later it ran on "a collection of over 100 small and medium test problems" against CONOPT (January 2009, p. 38).
- **Neural-network training, 2008.** "A general-purpose code will be written in GAMS" (January 2008, p. 34).
- **Quadratic relaxations, 2024–25.** "Moreover, we implemented the algorithm in Python and acknowledge that efficiency gains could be achieved by utilizing a compiled language." The study ran on "a Lenovo ThinkPad T490 laptop" (Strahl, Raghunathan, Sahinidis & Gounaris, *J. Glob. Optim.* 93:923–952, 2025, DOI 10.1007/s10898-025-01565-7, p. 936). The same sentence continues: "Hence, we do not speculate on the impact on computational efficiency" of quadratic versus linear relaxations. This paper is co-supervised with Gounaris at CMU.
- **Fourier–Motzkin presolve.** The paper's study uses a standalone module: "Our implementation uses the general-purpose MINLP solver BARON 25.3 [47] to parse LPs and builds a standalone LP presolve module" (§5).
- **GPU computing, 2008.** "For less than $3000, we purchased a standard computer to which we added to Graphics Processing Units (GPUs)." (August 2008, p. 36)

### C3. Enter a new area with a benchmark; algorithms a decade later

- **The DFO line, step by step** (CAPD reports):
  - January 2008, p. 34: "Luis Miguel Rios has collected 225 test problems from the globallib and princetonlib collections and solved them under different conditions using 18 different black-box solvers." The plan: "Current plans in this line of research include the addition of non-smooth problems in the test set collection and the inclusion of additional solvers. Test problems of black-box models from industry are currently sought. In the long run, we plan to develop novel algorithms for this difficult class of optimization problems."
  - January 2009, p. 38: 20 solvers.
  - August 2009, p. 41: 23 solvers.
  - 2013 paper: 502 problems and 22 solvers.
  - The group's own DFO algorithms were published in 2023 (Branch-and-Model) and 2025 (Model-and-Search). The BAM product shipped in 2025–26 (06 §6–7 give the dates, including the 2010 first talk on MAS).

  [practice, P]
- **The benchmark then picks parts for his own tools.** In the 2017 UConn lecture ([0:24:15]–[0:24:46]) he says the group compared "about 25 or 30 different derivative free optimization" solvers on "a collection of about 500 test problems". SNOBFIT, which he says was developed at the University of Vienna, found global optima for most of them. From this the group drew a design choice: "we're going to be using snowfit to do this adaptive sampling" (the caption's spelling of SNOBFIT). SNOBFIT is still ALAMO's error-maximization sampler. The ALAMO manual says "the SAMPLER option selects it", and the 2019 release notes add a native Fortran SNOBFIT. It became the default sampler only in release 2024.10.19 (C8). [stated, P, ASR; practice, P]
- **The same order elsewhere.**
  - A 2011 review and comparison of SDP relaxations came before the 2021–22 convex quadratic relaxations with SDP-quality bounds (01 §SW2).
  - A 2008–09 study of LP presolve sequences, run with an outside package (GALAHAD), came before the 2026 presolve paper (§E5).

  [practice, P]
- Era: CMU 2007–2012. The study ran on MATLAB and Linux rigs (01 §SW3) and was funded by NIH, NETL and NSF. The product came through TOF in 2025–26, about 17 years after the January 2008 report. [practice; the product dates are from 06]

### C4. A training problem first for a new student, then the application, then the general method

- **Training problem.** On Keith Zorn's least-squares project (CAPD, January 2008, p. 33): "This problem will serve to train Keith in the area of global optimization, before he embarks on the study of more complex problems."
- **Research questions framed as two testable questions** (pp. 33–34): "(1) does global optimization provide better solutions to standard curve fitting problems and (2) can global optimality be reached within reasonable computing times, i.e., a small multiple of the time taken by local optimization algorithms?"
- **The application.** It moved to Hartree–Fock problems. In August 2009 (p. 41) the report says "a rather unusual relaxation (high order RLT) considerably tightens the relaxation gap and results in an approach that is over a magnitude faster than other approaches to this problem."

  [stated, P]
- **The general method.** The published outcome is general solver methods, not a chemistry paper:
  - "Global optimization of general non-convex problems with intermediate bilinear substructures" (*Optim. Methods Softw.* 29:442–462, 2014, DOI 10.1080/10556788.2013.783032);
  - "Global optimization of general nonconvex problems with intermediate polynomial substructures" (*J. Glob. Optim.* 59:673–693, 2014, DOI 10.1007/s10898-014-0190-2).

  [practice, P] That the application trick was generalized into solver technique is [inferred] from titles and dates.

### C5. Customer models choose part of the agenda

- The manual (§13.3) turns a user's difficulty into a lead: "If everything else fails, send us the .bar file with your model. We may be able to identify special structure and improve BARON’s performance for your model." [stated, TOF, P]
- The 2022.1.19 note reports "orders-of-magnitude speedups for difficult problems supplied by customers" (§A3). [stated, TOF, P]
- That customer models steer which structures get special treatment is [inferred]; the customer models themselves are not public (Gaps).

---

## D. Debugging, numerical safety and reproducibility (layer 4)

### D1. Debugging runs through the user's model file

- **The manual's procedure.** The 2026 manual ends its troubleshooting chapter (§13, organized "by symptom") with a request for the model file four times:
  - "If everything else fails, send us the .bar file with your model." (§13.3)
  - "If you still believe BARON is making an incorrect optimality claim, send us the .bar file with your model." (§13.4)
  - The same request for incorrect infeasibility claims (§13.5) and for inconsistent results (§13.6).
- **The same request in 2000**: "Please report any comments and suggestions to Nick Sahinidis" (manual v4.0, §1.2, p. 2).
- **The fixes that follow** are those credited to customer models in §A3. [practice, P]
- **Tools to capture a user's run.**
  - "New BARON model files via BARWRITEMODEL and trace via BARTRACE." (19.3.21–19.3.24)
  - "Host name is now printed in the listing file." (2024.2.21)
  - ALAMO: "Listing file now includes all problem data, so a run can be reproduced entirely from the listing file via the ALAMO GUI." (2017.9.8)

  [practice, P]

### D2. Check the subsolver's answer before using it

- **Strong branching taken in-house.** "Strong branching implemented natively in BARON (no longer relying on solver routines); enables solution-correctness checks and provides duals." (16.3.4–16.12.7)
- **Missing bounds handled safely.** "Systematic treatment of missing bounds through safe relaxations." (11.0.0–11.9.1)
- **Safe LPs.** "Revamped LP interfaces and safe-LP procedures." (14.x); "More conservative reduction based on marginals." (2023.11.4); "Serious bug fix in the use of marginals-based tests during probing of the objective: these are now applied only to safe LPs." (2025.12.10)
- **Safe bound tightening.** "New family of safe bound tightening routines for squares, powers, monomials, and bilinears, replacing the previous relaxed forward reduction scheme." (2026.9.10)
- **Floating-point comparisons.** "ULP-aware comparisons introduced in reduction and branching routines, eliminating all previously observed cases of branching too close to a variable bound." (2026.9.10)

  All [practice, P].
- **A student's module follows the same rule** (Nohra thesis §3.5): "The relaxation solution returned by the QP subsolver is used at the current node only if it satisfies the KKT conditions." [practice, P]
- **The firm's statement** (FAQ): "BARON includes safeguards to ensure that its solvers do not make false infeasibility claims, maintaining the rigor of its global infeasibility results." [stated, TOF, P]

### D3. Determinism as a feature

- **BARON.**
  - "Used -fp-model consistent to improve consistency between runs on the same or different platforms." (18.5.8–18.12.26)
  - "Restricted CONOPT calls to a single thread for determinism." (2025.3.19)
  - The random seed became a user option (2024.5.8).
  - "Random seeds are now pinned in BARON's subsolvers for deterministic behavior across runs." (2026.9.10)
- **ALAMO.**
  - Strict floating-point compiler flags "to minimize the effect of floating-point round-off errors" (2021.4.29).
  - "New deterministic termination limits based on work units used" (2026.5.27).
- **BAM.** "BARON is now invoked with options that ensure deterministic behavior across runs; consecutive BAM calls within one process are now bit-identical." (2026.5.27)

  All [practice, P].
- **The manual explains why.**
  - §5.6: "Wall-clock and CPU seconds do not provide the same reproducibility." It adds: "A run stopped by MaxWork stops at exactly the same point on every machine."
  - §13.6: "BARON is compiled conservatively to facilitate reproducibility."

  [stated, P]
- **His benchmark runs follow the same rule**: BARON is restricted to one processor in the 2014 slides, and the 2026 branching study runs single-threaded and "in isolation". [practice, P]

### D4. The manual names the solver's silent failure modes

All items [stated, P].

- **Declarations BARON trusts without checking** (§13.4): "These three declarations are believed by BARON without verification, and an incorrect one produces a wrong answer silently."
- **Missing bounds.** §13.1 walks through a run that ends in "*** Normal completion ***" with 100% progress, followed by "*** Globality is therefore not guaranteed ***". The comment: "A user who reads only the normal-completion message and the 100% progress indicator may draw a conclusion that the output does not support."
- **Bounds that silence the warning but ruin the run** (§13.1): "Do not invent an enormous bound merely to silence the message: a bound of 10 10 may make the relaxation valid but useless, and the run will be slow rather than wrong." The "10 10" is how the text extraction renders 10 to the power 10.
- **When not to use BARON** (§4):
  - "If a model is known to be convex, a local NLP solver can return the global optimum directly and may do so faster."
  - "If only a good solution is needed quickly, without a guarantee, a multistart local search may be more appropriate."
- **Parallelism** (§13.3): "Raise threads but don’t expect miracles from parallelization for NP-hard problems".

### D5. Negative findings in the semester reports

- **GPU iterative methods** (CAPD, August 2008, p. 36): "We are finding that while parallelism of KACZ allows considerable CPU time reductions per iteration, it nonetheless increases the number of iterations for this algorithm. In addition, we are finding that developing sparse matrix implementations is more challenging than implementing successful dense matrix implementations."
- **Successive LP against CONOPT** (January 2009, p. 38): "CONOPT is up to 4 times faster for QPs and 10 to 20 times faster for general NLPs. This is encouraging, given the preliminary nature of Yiqi's implementation, especially the fact that there is no preprocessing in his code and no clever restarts of LPs."

  [stated, P] A loss against a commercial baseline is reported, then framed as encouraging for a prototype.

---

## E. How results are judged (layer 5)

### E1. Ground truth, explicit thresholds, two kinds of runs

The DFO studies (§B4) define success against certified global optima, with a stated tolerance. They report both median (average-case) and best-of-runs behaviour. They also run a separate "refinement ability" test from near-optimal starting points (README; 2013 §7.11). [practice, P]

### E2. Guarding against overtraining, and where that guard is missing

- **2013.** The hold-out was a set of transformed copies of the same 502 problems (§B4). [practice, P] A linear change of variables with condition number 2 "preserves smoothness and convexity characteristics". It is therefore a weak hold-out: it tests memorized optima and step sizes, not new problem structure. [inferred]
- **BAM.** Its public performance claims rest on the two libraries that TOF says it "routinely use[s] to develop BAM" (§A2):
  - the BAM manual §4;
  - the product page;
  - the OSTI abstract;
  - the release notes ("Solves approximately 80% of standard benchmark problems to global optimality", 2026.5.27).

  In what I read, no hold-out or unseen test set is mentioned for these claims. [practice, P for the sources; the gap is inferred] Contradiction C1 sets this against the 2013 practice.
- **His own description of the BAM evaluation** (Texas A&M lecture, March 2025, auto-captions [0:52:50]–[0:53:22], paraphrased because the captions are garbled here):
  - BAM was run in the same setting, on the same test problems, against the best algorithms of the earlier study, and it solves more problems than any other available algorithm.
  - For low-dimensional problems all algorithms work well; BAM's advantage grows with dimension.
  - "clearly there's more that need to be done in this context".

  [stated, P, ASR] This confirms that the headline evaluation reuses the published test set and has no unseen set. [inferred]

### E3. Separate solved from unsolved, filter trivial instances, report the instances that got worse

- **Nohra thesis §2.4** (cutting planes for convex-transformable functions in BARON 17.2):
  - Of 262 problems, 157 where no cut was generated and 19 trivial ones were removed, leaving 86.
  - Solved and unsolved instances are analysed separately.
  - The thesis reports: "In our experiments we observed that there are a few instances for which the new cuts lead to a increase in the number of nodes in the tree."
  - On the 52 instances neither variant solved: "As seen in the figure, for most of the problems considered in this comparison, the CTF cutting planes have little effect on the best lower bounds."
  - The headline effect is modest: "average reductions of 19% in the CPU time" on 34 instances, and "increases by 6% the number of problems that can be solved to global optimality within 500 seconds".

  [practice, P]
- **Nohra thesis §3.6.** "A problem is regarded as trivial if it can be solved by both solvers in less than one second." For the unsolved instances: "we say that two solvers obtain similar gaps if their remaining gaps are within 10% of each other." [practice, P]
- **Fourier–Motzkin paper.**
  - Results are reported over all problems and over "the 1,114 problems impacted by FME".
  - Tables 12–14 list "FME-impacted problems with the largest improvements and deteriorations".
  - The conclusion states a small effect: FME "yields up to 6%, 8% and 11% reductions in CPU time on challenging FME-impacted problems with CPLEX for the primal simplex, dual simplex, and barrier methods, respectively." (p. 373)

  [practice, P]
- **Probing paper.** Ambiguous labels are removed before learning: "To improve the accuracy of the classification models, we excluded instances whose solution times differed by less than 10% between runs with and without probing." The paper also notes the result depends on the implementation: "The statistics in the first few columns of Table 1 may vary when switching to a different implementation of probing algorithms, thus requiring retraining the GCN model under the same settings." (p. 10) [practice, P]
- **Branching preprint.** The paper concedes the accuracy comparison: "Overall, the GNN achieves the highest accuracy, consistent with the greater expressive power of deep networks." (p. 10) It then moves the comparison to solve time: "Even so, while these results indicate that GNNs better predict SB decisions on small instances, prediction accuracy alone does not determine solver performance, especially as problem size grows." (p. 10) [practice, P]
- **Gas-network paper** (v3, p. 15): "In a preliminary study, we concluded that the design problem based on the largest GasLib-4197 network remains challenging to solve with our framework." It also reports where its method beats BARON: "For both nominations, we see that with smaller stress levels, the problems can be directly solved by the initial budget search procedure which outperforms BARON." (p. 19) [practice, P]

### E4. Portfolio conclusions in research outputs, winner framing in product pages

- **Research outputs** [stated, P]:
  - The DFO interim report: "(d) all solvers are `useful' in the sense that there are at least a few problems for which each solver is best in terms of solution quality." (CAPD, January 2008, p. 34)
  - The LP scaling study: "There is no current scaling technique that dominates all others." (p. 35)
  - The 2013 conclusion: a four-solver portfolio (01 §SW3).
  - The 2026 OSTI abstract: "The study also shows that no single solver consistently outperforms the others across all problem types, indicating that our future laboratory applications may benefit from using a small set of strong solvers rather than relying on a single method."
- **Product pages** [stated, TOF, P]:
  - BAM product page: "At a fixed evaluation budget, BAM finds the best solution for over 80% of 750+ test problems. It far outperforms both the strongest alternative DFO codes, which solve 50–60%, and traditional Bayesian Optimizers, which solve 10%."
  - Group BARON page: "BARON has an edge over other global codes for NLP/MINLP" (2014 data).
- **Progress tracked on one fixed set.** The BAM release notes report a single number on one fixed set as the product matures: "approximately 50% of standard benchmarks" (2025.7.10), "70%" (2025.11.17), "77%" (2025.11.28), "approximately 80%" (2026.5.27). [practice, P]

### E5. Promising interim claims that were never published

These are research lines from the 2008–09 CAPD reports for which I found no later publication (Crossref scan of 323 works with author "Sahinidis", no matching title). [practice, P; "never published" is inferred from absence]

- **Globally optimal neural-network training.**
  - The project started from "an algorithm developed earlier by Voudouris and Sahinidis (unpublished)" (January 2008, p. 34).
  - Interim claim: "The main conclusion thus far has been that our approach results in lower training errors and much simpler neural networks than all other approaches." (January 2009, p. 37)
  - In August 2009 the section heading "Global Optimization for Machine Learning Problems" is still printed (table of contents, p. 41), but the section has no text. 01 §3 item 6 lists the earlier MS theses on the topic.
- **A unified interface to the DFO solvers.**
  - August 2008, p. 35: "This software platform is currently being tested and will be soon made available."
  - January 2009 (p. 38) and August 2009 (p. 41): the platform "will be made available in the near future".
  - I found no released interface; the 2013 data page offers models and results, not the interface.
- **Successive linear programming** (2008–09). The goal was "a trust region technique that is provably convergent". The project is absent from the August 2009 report.
- **LP algorithms on FPGAs.** "The long-term goal of this project is to develop novel algorithms for LPs and make them available via distributed implementations on modern GPUs and FPGAs." (August 2009, p. 42) GPU papers followed: Elble, Sahinidis & Vouzis, *Parallel Comput.* 36:215–231, 2010, DOI 10.1016/j.parco.2009.12.003. I found no FPGA paper.
- **The "optimal" presolve sequence.** "Our main finding was that the sequence in which different presolve techniques are applied to any given LP problem can affect the final outcome of preprocessing" and "Current work focuses on identifying an "optimal" presolve sequence." (August 2009, p. 42) The question comes back 17 years later: the 2026 Fourier–Motzkin paper has a table "Shifted geometric means of the reduction in model size with different orders of expensive presolve methods". The link between the two is [inferred].

### E6. How criticism is answered: cooperation, fixes, adoption of the critic's protocol

- **Cooperation with the critics.** Neumaier, Shcherbina, Huyer & Vinkó tested BARON 7.2/GAMS for the COCONUT project (*Math. Program.* 103:335–356, 2005, DOI 10.1007/s10107-005-0585-4; author preprint). Their acknowledgments say: "Nick Sahinidis (BARON) provided valuable support in obtaining and running their software." (preprint p. 3). [observed, P]
- **Fixes.** Their report notes: "In the mean time, BARON/GAMS had some bugs fixed, which eliminates all wrong claims to infeasibility and reduces the rate of wrong claims of global optimality to 12/675 = 1.8%. This raises the hope that the next official release has a much improved reliability." (p. 19). 01 §3 item 2 gives the 4% initial rate. [observed, P]
- **Adoption of the critics' protocol.** His own 2013 DFO benchmark copies their protocol: "following the approach of [102]" (§B4). Their paper also shows how reviewers shaped the protocol: "Upon request by a reviewer, we also add some performance profiles" (p. 20). [practice, P]
- **Outside testing named in release notes**: the 6.0 notes and the SECQUOIA fix (§A3). [practice, P]
- **As editor, he reports results against his own solver without rebuttal.** His 2019 editorial for an *Optimization and Engineering* special issue (DOI 10.1007/s11081-019-09438-1) lists papers whose methods "outperform BARON". It sums up: "Many of the papers develop tailored algorithms that outperform general-purpose MINLP solvers." (p. 304) On convex MINLPs, Kronqvist et al.'s SHOT "has an edge, followed very closely by the global solver BARON" (p. 303). [stated, P]
- **Engaging a debate in statistics.** See §F3: the group re-ran the other authors' released code and listed "points of agreement and divergence".
- **No published rebuttal found.** I found no reply, comment or rebuttal by him to a criticism. OpenReview holds only records imported from DBLP for his name: no reviews and no rebuttals. [practice, S; absence]
- **Independent benchmarks in 2026.** BARON stays in Hans Mittelmann's public benchmarks. On the MINLP page two other commercial solvers are marked "publication suppressed"; BARON is not. [observed, P]

  | Mittelmann page (date on page) | Instances | BARON version | BARON: solved (scaled time) | Others |
  |---|---|---|---|---|
  | MINLP, MINLPLib (26 Feb 2026) | 200, limit 2 h | not stated | 158 (1.0, fastest) | SCIP 154 (1.4), LINDO 116 (4.8), SHOT 96 (5.6); Gurobi and Xpress "publication suppressed" |
  | Continuous non-convex QPLIB (17 May 2026) | 102 | 25.12.10 | 31 (1, fastest) | ANTIGONE 35 (1.65), COPT 28 (1.39), MINOTAUR 22, SCIP 15 |
  | Binary non-convex QPLIB (9 May 2026) | 128 | 25.11.17 | 74 (4.03) | SHOT 91 (1), COPT 83 (2.42), RAPOSa 69, SCIP 36 |
  | Discrete non-binary QPLIB (12 May 2026) | — | 25.3.19 | 66 (7.92) | SHOT 99 (1), COPT 88 (2.01), SCIP 40 |
  | QUBO-QPLIB (21 Sep 2026) | 23 | 25.11.17 | 13 (20.8) | QUBOWL 22 (1), QUPLANE 22 (4.60) |

  TOF's news item of 2 December 2025 reads: "BARON maintains its top win rate on the Mittelmann benchmarks, especially for continuous nonconvex QP and MINLP test sets." [stated, TOF] On the 2026 pages BARON is fastest on those two sets. It is not the leader on the three discrete QP sets, where specialized and MIP-based codes win. See C5.

### E7. How the community read his practice

- **The Beale–Orchard-Hays prize defines what it rewards** (Optima 73, January 2007, p. 3): "the prize is awarded to a paper appearing within the past three years that describes development of software, the computational evaluation and testing of new algorithms, and the development of new methods for empirical testing of algorithms".
- **The 2006 citation** for the 2005 polyhedral branch-and-cut paper (DOI 10.1007/s10107-005-0581-8): "The nominated paper develops techniques that enhance previous versions of BARON." It adds: "BARON also incorporates techniques from automatic differentiation, interval arithmetic, and other areas to yield an automatic, modular, and relatively efficient solver for the very difficult area of global optimization." (p. 4)

[observed, P] The praise is measured ("relatively efficient"). The citation treats the paper as an enhancement of a software system, which matches §A1. [inferred]

---

## F. How results are written up and released (layer 6)

### F1. Versions are named, and citing the version is requested

- **The group page asks for versions**: "The best way to cite BARON is by citing one of the BARON publications and mentioning the version of the software utilized." [stated, P]
- **The papers I read name the versions of all solvers.** Examples [practice, P]:
  - BARON 14.4.0 and four competitors in the 2014 slides;
  - ANTIGONE 1.1, BARON 19.12, COUENNE 0.5, CPLEX 12.10, GUROBI 9.0, LINDOGLOBAL 12.0 and SCIP 6.0 in Nohra §3.6;
  - a version table in the 2022 DFO paper;
  - SCIP 8.0.0 with SoPlex 6.0.0 in the branching preprint;
  - BARON 25.3 and CPLEX 22.1.1 in the Fourier–Motzkin paper.
- **TOF keeps old builds**: "TOF code distributions are now archived as zip archives starting with BARON 13." (14.x notes). [practice, P]

### F2. Open data, mostly closed code

- **Test problems and raw results are open** (§A2).
- **Code from the solver line is closed or on request.**
  - The Fourier–Motzkin code is "embedded in the BARON solver" (p. 376).
  - Model-and-Search: "Code availability Interested readers should contact N. V. Sahinidis." (p. 919)
  - The Branch-and-Model full text was not read (closed). [practice, P]
- **Open code comes from student-led or co-supervised projects.**
  - OR-Gym is MIT-licensed on GitHub (hubbs5/or-gym). On 2026-10-10 the repository had 456 stars and 99 forks; its last commit is dated 2023-02-13, and the contributors are students (no commits by him).
  - The JMLR transfer-learning paper added a code link between arXiv v1 and v2. v2 reads "The source code for reproducing the experimental results is available at", followed by a GitHub address that is broken across a line in the PDF. The JMLR page links https://github.com/Shaohan-Chen/Transfer-learning-in-Mallows-Cp, the first author's repository.

  [practice, P]
- **Who can reproduce his solver results.**
  - BARON (FAQ): "Free academic licenses are currently available only to individuals affiliated with Carnegie Mellon University, the University of Illinois at Urbana-Champaign, or the University System of Georgia." Other academics buy discounted licenses, and the free version is limited to 10 variables, 10 constraints and 50 nonlinear operations (manual §1.2).
  - BAM (manual §4): "BAM's free academic license provides full access to the software and permits benchmarking with other solvers. We encourage users to compare any desired test problems and report their results in the open literature."

  [stated, TOF, P] Independent reproduction of BARON-based results is therefore easier through NEOS, GAMS or AMPL than from source. [inferred]

### F3. A discussion piece: re-run the others' code, correct your own terms, do not advertise

Sarwar, Sauk & Sahinidis, "A Discussion on Practical Considerations with Sparse Regression Methodologies" (*Statist. Sci.* 35:593–601, 2020, DOI 10.1214/20-STS806; arXiv:2011.09362 v1 and v2). It discusses Hastie, Tibshirani & Tibshirani (DOI 10.1214/19-STS733) and Bertsimas, Pauphilet & Van Parys (DOI 10.1214/19-STS701). All items [practice, P] unless marked.

- **Credits the others' openness, then uses it.**
  - "Before discussing the papers, we commend both groups for making the code for their research available open-source. Hastie et al. go notably further by distributing the code for not only their regression methods, but also for the scripts used to run their actual simulations." (v2, p. 2)
  - "These experiments were actualized because the authors have provided open-source implementations." (p. 5)
- **Corrects a term between versions.**
  - v1 defines "FPR %" as "the false positive rate (i.e., the percentage of regressors chosen that are erroneously included)".
  - v2 replaces every occurrence with "FDR %" and "the false discovery rate", which is what that definition describes.
- **No self-promotion.** ALAMO, his group's best-subset modeling tool, is not mentioned anywhere in the discussion, although the debate is about best subset selection against the lasso. [practice, P; the significance is inferred]
- **States its limits**: "It is impossible to give broad advice for all conceivable situations and the experiments in this paper and the two discussed can only capture a portion of the range of problem configurations." (p. 9) [stated, P]
- **Opens on dialogue**: "The authors have started a highly constructive dialogue, our goal is to continue it." (abstract) [stated, P]

### F4. When preprints are posted

Posting dates come from the arXiv API; journal dates come from Crossref (online date where Crossref has one).

| arXiv id | Posted (v1) | Journal version | Position |
|---|---|---|---|
| 1701.03978 | 2017-01-15 | *Chem. Eng. Res. Des.* 116:2–26, issue December 2016, DOI 10.1016/j.cherd.2016.10.014 | after the issue |
| 1705.10437 | 2017-05-30 | *Chem. Eng. Res. Des.* 131:16–28, issue March 2018, DOI 10.1016/j.cherd.2017.05.015 | before the issue (no online date in Crossref) |
| 1705.10918 | 2017-05-31 | *Comput. Chem. Eng.* 106:785–795, issue November 2017, DOI 10.1016/j.compchemeng.2017.02.010 | before the issue (no online date in Crossref) |
| 1706.08591 | 2017-06-26 | *Ann. Oper. Res.* 240:351–380, online 2015-09-23, DOI 10.1007/s10479-015-2019-x | 21 months after online publication |
| 1706.08601 | 2017-06-26 | *Constraints* 22:338–376, online 2017-01-14 | 5 months after online publication |
| 2008.06319 | 2020-08-14 | none found | preprint only |
| 2010.04822 | 2020-10-09 | *SIAM J. Optim.* 31:142–171, online 2021-01-12 | 3 months before |
| 2011.09362 | 2020-11-18 | *Statist. Sci.* 35(4), November 2020 | same month |
| 2106.13721 | 2021-06-25 | *Math. Program.* 196:203–233, online 2021-07-06, DOI 10.1007/s10107-021-01680-9 | 11 days before |
| 2107.02847 | 2021-07-06 | *J. Mach. Learn. Res.* 23(134):1–105, 2022 (JMLR paper number 19-816) | during review; v2 "Accepted to the Journal of Machine Learning Research" |
| 2307.07648 | 2023-07-14 | *J. Glob. Optim.* 90:931–963, DOI 10.1007/s10898-024-01424-x (Springer page: received 3 April 2023, accepted 26 July 2024, published 3 September 2024) | 3 months after submission; v3 (30 January 2024) posted during review |
| 2408.13053, 2408.13058 | 2024-08-23 | *J. Glob. Optim.* 93:923–952 and 953–987 (part I received 24 August 2024; both online December 2025; part II DOI 10.1007/s10898-025-01567-5) | at submission |
| 2604.00094 | 2026-03-31 | under review (06 §7: the CV lists it as submitted to *INFORMS J. Comput.*) | at submission |

[practice, P] [inferred] The pattern changes over time:

- In 2017 arXiv served as an archive for papers already published or accepted.
- In 2020–21 most papers were posted around acceptance or publication; the JMLR paper was posted during review.
- From 2023 on, papers were posted during review or at submission. The gas-network paper went up three months after submission, and revised versions followed while it was under review. The quadratic-relaxation papers and the branching preprint went up at submission. All of these have co-authors from Georgia Tech ISyE, MERL or CMU.
- Where I could check dates, no entry appeared on arXiv well ahead of journal submission. The earliest relative posting is the 2024 pair, one day before the journal's "received" date. For the 2020–21 entries, OR-Gym and the 2026 preprint, I do not know the submission date.
- The JMLR paper number suggests submission in 2019, two years before the arXiv posting. That reading rests on JMLR's numbering convention and is [inferred].

### F5. How results are shown

[practice, P]

- Performance profiles: the GAMS performance tools in 2014, PAVER in 2017, Dolan–Moré profiles in 2022.
- Fraction of problems solved against the number of function evaluations, for DFO.
- Shifted geometric means: the Fourier–Motzkin paper, the probing paper and the branching preprint.
- Library-by-library breakdowns: 2017, the Fourier–Motzkin paper, the comparisons slides.
- A worked two-dimensional example (camel6) that plots every solver's search before the statistics: 2013 §6; the 2022 paper repeats it with st_e36; the BAM manual's quickstart uses camel6 again.

---

## G. Research organization (layer 7)

### G1. Every semester, a written project-by-project report

The CAPD newsletters of 2008–2009 print a section "Nick Sahinidis' Group". Its structure:

- **Two thrusts**: "THRUST 1--OPTIMIZATION ALGORITHMS, THEORY, AND SOFTWARE" and "THRUST 2--APPLICATIONS OF OPTIMIZATION IN BIOLOGY, CHEMISTRY, ENGINEERING, AND MEDICINE".
- **One entry per project**, giving the student, the status and the plans.
- **A box "Enabling Software From Nick Sahinidis' Group"**, which lists BARON and the bioinformatics servers CMOS, R3 and SBH (January 2009, p. 35).

[practice, P]

What the reports show:
- **The group spanned two universities after his August 2007 move to CMU.** Bao, Rios and Elble are listed as "Ph.D. student ... at the University of Illinois" (January 2008, pp. 33–35).
- **Projects map to artifacts**: a BARON module, a benchmark, a GPU code, a scaling study.
- **Projects without an artifact drop out of the reports** (§E5).

Era: CMU and CAPD with industrial sponsors, 2007–2009. Later reports sit behind a sponsor login, and I did not access them (Gaps).

### G2. A firm and a group, with a division of labour

- **The firm co-writes the solver papers.** TOF's research scientist Yi Zhang is first author of the 2025 BARON paper (DOI 10.1007/s10589-024-00633-0, abstract only), of the probing paper and of the Fourier–Motzkin paper. The probing and Fourier–Motzkin papers both list "The Optimization Firm, LLC" as affiliation 1, for Zhang and for Sahinidis, next to Georgia Tech. The Fourier–Motzkin paper states: "Funding No funding was received to perform this research." (p. 376) [practice, P] [inferred] Work on the solver core is now done largely on the firm's time, while grant-funded work goes to the application lines (01 §1.1 and 06 §2 list the grants).
- **The commercialization team is three people** (Our Team page). [stated, TOF, P]

### G3. Compute: cheap and long-lived

- **His own cluster**: "With a focus on the impact of these techniques on the performance of the simplex method, over half a billion LP solves were executed in Nick's Linux cluster at Illinois." (January 2008, p. 35)
- **A $3000 GPU box** in 2008 (§C2).
- **One benchmark CPU model from 2014 to 2026** (§B1).
- **The Georgia Tech cluster** in 2026: "Experiments are run on Linux servers equipped with Intel Xeon Gold 6226 CPUs at 2.70 GHz (PACE 2017). GNN-G additionally utilizes an NVIDIA Tesla V100 (16 GB) GPU for inference." (arXiv:2604.00094 v1, p. 11)
- **A laptop** for a prototype (§C2).

[practice, P]

### G4. Outside testing networks

- **GAMS, from 2001** (slides, slide 2): "2001: Start of collaboration GAMS Dev. Corp. and developers of BARON, LGO, and OQNLP". [stated-joint, P]
- **The COCONUT comparison**, 2004–05 (§E6).
- **QPLIB**, 2019 (§B5).
- **The Dagstuhl seminar 18081**, 2018. The report's working group on "Sound experimentation with MINLP software" notes: "The participation of core developers from the MIP and MINLP solvers ANTIGONE, BARON, Couenne, Gurobi, Minotaur, SCIP and FICO Xpress resulted in a discussion on a technical level that is generally difficult to reach in a broader audience." (DOI 10.4230/DagRep.8.2.64, p. 85). Its conclusions include "the need to incorporate experimentation on permuted models as has become standard in the MIP community" and "the affirmation that conducting fair benchmarks between different solvers remains inherently difficult and users of solver software should not rely on simplistic comparisons." [observed, S]
- At the same seminar he presented ALAMO (abstract, p. 81): "We present the methodology behind ALAMO and comparisons with a variety of learning techniques, including the lasso." [stated, P] Whether he attended the benchmarking working group in person is not recorded.

---

## H. Dropped, abandoned or failed (consolidated)

01 §3 and 06 §6 list the publication-level failures (a 1992 erratum, an accepted paper that never appeared, dormant research lines). What follows adds process-level drops visible in code and reports. All are [practice, P]; the reasons are not documented unless quoted.

1. **Specialized modules**: twelve in 1998, a chapter in 2000, none in 2026. The examples migrated from `MODULE: POLY` to `MODULE: NLP` (§C1).
2. **The mixed-integer SDP module.** BARON 5.0 (1999–2000): "Support for semidefinite programming relaxations was included. The mixed-integer semidefinite-programming module was developed in collaboration with Matthew Wilkins." The 2000 manual documents `barmisdp`; the 2026 manual does not mention it. This settles the question 01 §SW2 left open: the module is gone. Why it was dropped is still undocumented.
3. **Subsolvers and platforms dropped or replaced**:
   - "Dropped support of MINOS/SNOPT for solution of LP subproblems (still used as NLP solvers)." (10.x)
   - "Dropped all 32-bit versions." (18.x)
   - "Replaced MUMPS by HSL57 for IPOPT." (18.x)
   - "Replaced MC19 with the better MC29." (19.x)
   - "CONOPT4 is now used exclusively, replacing CONOPT3." (2023.11.10)
   - "BARON's embedded FilterSD algorithm is now off by default." (2022.1.19)
   - "CBC and CLP presolve disabled." (2022.7.22)
4. **Algorithmic features switched off where they hurt**:
   - "Aggregation cuts disabled for mixed-integer rows." (2025.2.1)
   - "The MIQP subsolver call is now disabled for problems with no more than 20 constraints." (2025.11.17)
   - "BARON no longer performs risky presolve disaggregations when CBC is used as the MIP subsolver." (2025.11.28)
   - "Presolve no longer disaggregates square terms involved in absolute functions or powers, since this destroys convexity recognition." (2024.9.12)
   - "Ill-conditioned cuts for monomials are no longer generated." (2026.9.10)
5. **Free distribution replaced by commercial licensing.**
   - In 2000 the code "may be used and distributed freely as long as it is not sold for profit or incorporated in commercial products" (manual §1.2, p. 2).
   - The free 1996 build was limited to "up to 20 variables only" (availability page, 2000).
   - TOF was founded in 2001 (01 §1.9).
   - Today the free version is limited to 10 variables, 10 constraints and 50 nonlinear operations.
6. **ALAMO dependencies and options dropped**:
   - "MATLAB-SNOBFIT is no longer supported." (2019.7.3)
   - "GAMS dependency eliminated from the software and the documentation." (2022.6.4)
   - "Replaced the REGULARIZER option with SCREENER" (2019.8.3)
   - "Removed the MINTERMS option from the manual; this option was never implemented." (2021.12.5). The manual had documented an option the code never had.
7. **Research lines that stopped in 2008–09**: neural-network training, successive LP, the unified DFO interface, LP algorithms on FPGAs (§E5).
8. **OR-Gym** has been unmaintained since February 2023, after its student authors left (§F2; 06 §6 notes that no journal version exists).
9. **A self-check on ALAMO's flagship step.**
   - ALAMO's adaptive sampling used SNOBFIT through MATLAB until 2019 (2014.3.1: "MATLAB/SNOBFIT link for error-maximization sampling"; 2019.7.3: the native Fortran SNOBFIT).
   - A bug "had effectively disabled adaptive sampling" until 2020.4.25.
   - The default sampler was random until 2024.10.19: "The default sampler is now SAMPLER=2 (ALAMO's adaptive sampling) instead of random sampling."
   - See C8.
10. **Errata and retractions.** I re-ran the Crossref scan: 323 works with author "Sahinidis". It finds only the 1992 erratum (DOI 10.1021/ie00004a041) and a 2021 correction to a prize announcement (DOI 10.1007/s11081-021-09651-x). No retraction was found; this matches 01 §3.

---

## I. Early versus final versions

| Work | Early version | Final version | What changed | Tag |
|---|---|---|---|---|
| Li, Dey & Sahinidis, gas network design | arXiv:2307.07648 v1 (14 Jul 2023): "A decomposition framework for gas network design"; abstract: "We conduct experiments on a benchmark network"; "The proposed framework was tested on the Gaslib-582 network" (p. 18) | v3 (30 Jan 2024): "A reformulation-enumeration MINLP algorithm for gas network design"; *J. Glob. Optim.* 90:931–963, 2024 | New title. An enumeration outer loop was added ("a nested loop that includes a two-stage procedure ... in the inner loop and an efficient enumeration scheme in the outer loop"). Tests grew from one network to five ("As a result, we consider GasLib-11, GasLib-24, GasLib-40, GasLib-134, and GasLib-582 networks.", p. 15). A failure on GasLib-4197 is now reported (§E3). The journal received the paper on 3 April 2023, before v1 was posted, and accepted it on 26 July 2024, so v3 was posted while the paper was under review. The changes may answer referees, but no referee report is public [inferred]. The journal version was not read. | [practice, P] |
| Sarwar, Sauk & Sahinidis, sparse-regression discussion | arXiv:2011.09362 v1 (18 Nov 2020) | v2 (8 Feb 2021) = *Statist. Sci.* 35:593–601 | FPR replaced by FDR throughout (§F3). No other substantive change found in a word-level diff. | [practice, P] |
| Hubbs et al., OR-Gym | arXiv:2008.06319 v1 (14 Aug 2020) | v2 (17 Oct 2020); no journal version found | Appendix "Model Sizes" added ("Table 5: Average model sizes and solution times for MILP models."). The knapsack sentence now says solved "to optimality using Gurobi 8". | [practice, P] |
| Chen, Sahinidis & Gao, transfer learning with Mallows' Cp | arXiv:2107.02847 v1 (6 Jul 2021) | v2 (29 May 2022), "Accepted to the Journal of Machine Learning Research"; JMLR 23(134) | Section headings show a new §5.3, "Feature Selection Using Approximate Cp and TLCp Methods". A link to the reproduction code was added (§F2). Both versions contain the real-data experiments. | [practice, P] |
| Strahl et al., quadratic relaxations I | arXiv:2408.13053 v1 (23 Aug 2024) | *J. Glob. Optim.* 93:923–952 (received 24 Aug 2024, accepted 14 Nov 2025) | Only one arXiv version exists. I did not diff it against the published PDF. | — |

---

## J. Taste as revealed by practice (layer 1, short)

02 covers stated taste. Here are three preferences that show in behaviour; all are [inferred] from the practice cited.

- **Certificates over speed.** He builds the ground truth with a deterministic solver (§B4). His DFO product is deterministic by design, and its manual sets it against stochastic Bayesian optimization (BAM manual §4.1). The solver warns when "Globality is therefore not guaranteed" (§D4).
- **Small models.** ALAMO selects few basis functions (01 §SW4). The branching preprint uses "fewer than 4% of the parameters of a state-of-the-art graph neural network (GNN)" (abstract) and makes interpretability and CPU-only deployment its selling points.
- **Breadth over showcases.** His comparisons use whole public libraries, filtered only for solver acceptance or triviality (§B1–B4), not hand-picked instances.

---

## Contradictions (kept, not reconciled)

- **C1. Hold-out discipline: 2013 study versus BAM claims.**
  - In 2013 he guarded others' solvers against overtraining on his benchmark with an unseen, transformed test set (§B4, §E2).
  - The 2025–26 BAM claims rest on rs13 and ps22, which TOF says it "routinely use[s] to develop BAM". In the BAM manual, product page, OSTI abstract and release notes, no hold-out is mentioned. [practice for both; the tension is inferred]
- **C2. Three framings and three numbers for the same BAM benchmark.**
  - OSTI abstract (March 2026): "42 data-driven optimization algorithms on a broad collection of 502 test problems", "BAM showing the highest overall performance and solving more than 80% of the benchmark problems", together with "no single solver consistently outperforms the others".
  - BAM manual §4: "over 40 software implementations".
  - Product page: "finds the best solution for over 80% of 750+ test problems", with competitors at "50–60%" and Bayesian optimizers at "10%".
  - Release notes: "Solves approximately 80% of standard benchmark problems to global optimality."
  - The test set (502 or 750+) and the metric (solved, best found, global optimality) differ between these sources.
- **C3. Praise for open code versus closed code.**
  - The 2020 discussion "commend[s] both groups for making the code for their research available open-source" (§F3).
  - His own solver-line code is commercial, embedded in BARON, or available on request (§F2).
  - His test problems and raw results are open. The contrast is between open data and closed code.
- **C4. A 2014 benchmark shown as current in 2026.** The group's BARON page still says "BARON has an edge over other global codes" on the strength of the 2014 comparison: BARON 14.4.0 against SCIP 3.1, Couenne 0.4, Antigone 1.1 and LindoGlobal 9.0. Independent 2026 results are mixed (C5).
- **C5. "Top win rate" versus the independent tables.**
  - TOF (December 2025): "top win rate on the Mittelmann benchmarks, especially for continuous nonconvex QP and MINLP test sets".
  - Mittelmann 2026, continuous non-convex QPLIB: BARON has the best scaled time (1), but ANTIGONE solves more instances (35 against 31).
  - On the binary, non-binary discrete and QUBO pages, SHOT, COPT or specialized QUBO codes lead (§E6).
  - The claim holds for the metric and the sets it names. It does not hold for every Mittelmann page.
- **C6. IBMLib size.** The group's BARON page and the 2014 slides say "141 MINLPs from IBMLib", with a total of 1740. The Khajavirad & Sahinidis 2018 abstract says "142 problems from IBMLib"; with the same other libraries the total would be 1741.
- **C7. Benchmark CPU clock.** The 2014 slides, the 2017 preprint and the 2020 thesis give the Xeon X5650 a clock of 2.66 GHz. The 2026 Fourier–Motzkin paper gives the same CPU model at 2.55 GHz. I could not establish whether this is a different machine or a typo.
- **C8. ALAMO's published method versus its shipped defaults.**
  - The 2014 abstract: "The model is then improved systematically through the use of derivative‐free optimization solvers to adaptively sample new simulation or experimental points."
  - In the software, error-maximization sampling needed MATLAB until 2019.7.3.
  - A bug "had effectively disabled adaptive sampling" until 2020.4.25; when it was introduced is not stated.
  - The default sampler was random until 2024.10.19.
  - The default `MAXITER` of 1 turns adaptive sampling off unless the user supplies a simulator or a data bank (ALAMO manual). [practice, P; the tension is inferred]
- **C9. The FAQ is out of date about BAM.** It still says "The Optimization Firm is planning to offer a separate tool for black-box (derivative-free) optimization in the future". BAM was launched on 2 June 2026, and the 2026 BARON manual already refers users to it.
- **C10. Tuning policy in his two DFO benchmarks.**
  - 2013: developers supplied options and improved their codes over several rounds.
  - 2022: "we did not tune solvers in any way to the problems at hand".
  - Both are documented. The reason for the change is not stated.
- **C11. Where the GPU paper went.** The CAPD report says "A related paper has been submitted to Parallel Programming." (January 2009, p. 39). The published version appeared in *Parallel Computing* 36:215–231, 2010.

---

## Gaps

- **BARON's internal test harness.** The regression scripts and pass/fail criteria of BARON (and ALAMO, BAM) are not public. The release notes and the statement that 23 libraries are "routinely used" are the only window. The customer models are not public either.
- **I found no OpenReview reviews or rebuttals for his name.** The public notes search returned only records imported from DBLP, and the per-author query requires a login challenge. Referee reports and rejected papers: none found (as in 01 and 06).
- **Closed full texts, read as abstracts only**:
  - Zhang & Sahinidis 2025 (*Comput. Optim. Appl.*);
  - Liu, Ploskas & Sahinidis 2019;
  - Branch-and-Model 2023;
  - Khajavirad & Sahinidis 2018;
  - Tawarmalani & Sahinidis 2005;
  - Cozad, Sahinidis & Miller 2014.

  Not read at all:
  - Kılınç & Sahinidis 2018 (the Taylor & Francis page returned 403);
  - the journal version of the gas-network paper.
- **AIChE abstracts.** "Third generation branch-and-reduce algorithms and software" (2012, paper 398a) and "Recent advances in the BARON project" (2016, paper 314a) were found by WebSearch. Both curl and WebFetch got HTTP 403, and there was no Wayback copy. The search engine's summary says the first BARON generation used nonlinear relaxations that a second generation replaced with polyhedral ones. I could not read the text, so this is unverified. The 2000 manual confirms only that version 4.0 (1997–98) "allows an entirely linear programming based solution approach".
- **CAPD newsletters after August 2009** sit behind a sponsor login (capd-archive.cheme.cmu.edu returned HTTP 401). I did not try to get past it, so the 2010–2020 semester reports are missing.
- **SECQUOIA testing framework.** I identified the Purdue group, not the framework or its report on BARON.
- **IDAES `alamopy` authorship.** The GitHub API rate limit stopped the commit-history query, so who wrote the open wrapper of ALAMO is unknown.
- **Rejoinders in *Statistical Science*** (DOIs 10.1214/20-sts733rej and 10.1214/20-sts701rej) were not read. Whether Hastie et al. or Bertsimas et al. answered the discussion is unknown.
- **The PI's personal coding.** Statements from 2008–09 say he and Tawarmalani maintain BARON. For 2020–26, the share of code he writes himself compared with TOF staff is not documented.
- **Performance variability.** I found no experiment with permuted models in the group papers I read, although the 2018 Dagstuhl working group recommended it. Absence in a sample of papers is not proof.
- **Model-and-Search uses 501 problems, not 502.** The reason is not stated in the parts I read.
- **Euclidean-norm library.** The source article of `euclidlib` (a 2026 SIAM Review paper listed on minlp.com) is unverified (§A2).
- **Talks.** The two transcripts available are uncorrected machine captions. Talks in which he discusses development or testing in more detail (for example the yearly "BARON project" status talks listed in 06) have no recording or transcript that I found.

---

## Notes for the other research files

- **01 §1.9** treats the expansion of BAM as Branch-and-Model as [inferred]. The BAM product page is headed "Branch-And-Model (BAM) Optimization Tool", so this is now [stated, TOF, P].
- **01 §SW2** leaves the fate of the mixed-integer SDP module undetermined. The module is documented in the 2000 manual (`barmisdp`), recorded in the BARON 5.0 notes, and absent from the 2026 manual (§H item 2). That it was dropped is now [practice]; the reason is still unknown.
- **06 §6** could not identify SECQUOIA. It is a research group at Purdue's Davidson School of Chemical Engineering (GitHub organization page).

---

## Sources

One line each: title, author, date, URL or identifier, P or S. Items I could not read in full are marked "abstract only", "metadata only", "dates only", "titles only", "index", "not accessible" or "not accessed".

**Software, firm and group records (primary)**

1. "BARON Release Notes" (BARON 1.0 to 2026.9.10), The Optimization Firm, read 2026-10-10, https://minlp.com/baron-release-notes — P
2. "BARON user manual and installation guide", v. 2026.9.10, N. Sahinidis (TOF), 10 Sep 2026, https://minlp.com/baron-user-manual — P
3. "BARON Frequently Asked Questions", TOF, undated, https://minlp.com/baron-frequently-asked-questions — P
4. "Optimization Test Problems", TOF, undated, https://minlp.com/optimization-test-problems — P
5. "ALAMO Release Notes" (2013.10 to 2026.9.10), TOF, https://minlp.com/alamo-release-notes — P
6. ALAMO user manual (2026.9.10), TOF, https://minlp.com/alamo-user-manual — P
7. "BAM Release Notes" (2025.7.10 to 2026.9.10), TOF, https://minlp.com/bam-release-notes — P
8. BAM user manual (2026), TOF, https://minlp.com/bam-user-manual — P
9. "BAM Data Driven Optimizer" product page, TOF, https://minlp.com/bam-data-driven-optimizer — P (vendor claims)
10. "Black-box Optimization Test Problems", TOF, https://minlp.com/black-box-optimization-test-problems — P
11. "News", TOF (items January 2024 to September 2026), https://minlp.com/news — P (vendor claims)
12. "Our Team", TOF, https://minlp.com/our-team — P
13. "BARON Software" and "Examples" pages with 11 example .bar files, Sahinidis group, Georgia Tech, https://sahinidis.coe.gatech.edu/software/baron-software — P
14. "COMPARISONS" slide deck (comparisons.pptx, 6 slides, file modified 2014-12-13), N. Sahinidis, https://sahinidis.coe.gatech.edu/public/content/baron/comparisons.pptx — P
15. DFO comparison data page, README and problem list, L. M. Rios and N. V. Sahinidis, https://sahinidis.coe.gatech.edu/dfo (also /public/README and /comp) — P
16. Mixed-integer DFO data page and problem list, N. Ploskas and N. V. Sahinidis, https://sahinidis.coe.gatech.edu/midfo (also /midfo_comp) — P
17. "Test problems for SO and DFO algorithms", with N. Austin and N. Sahinidis, "Cooling Crystallization Solvent Design" (28 Jul 2014) and Y. Sun and N. Sahinidis, "Design of polymer configuration and flow" (Apr 2021), https://sahinidis.coe.gatech.edu/research/test-problems-so-and-dfo-algorithms — P
18. BARON web pages at UIUC, Wayback captures of 1998-12-06 (baron.html), 2000-08-17 (baron/baron.html), 2000-08-30 (baron/availability.html and examples/*.bar), http://web.archive.org/web/19981206111813/http://archimedes.scs.uiuc.edu:80/baron.html — P
19. "BARON: Branch And Reduce Optimization Navigator. User's Manual, Version 4.0", N. V. Sahinidis, revision of 28 June 2000, Wayback capture 2000-08-30 of http://archimedes.scs.uiuc.edu/baron/manuse.pdf — P
20. CAPD Newsletters, Carnegie Mellon University, January 2008, August 2008, January 2009, August 2009, section "Nick Sahinidis' Group", Wayback captures of http://capd.cheme.cmu.edu/NewsletterArchive/ — P
21. "Global Optimization with GAMS: Applications and Performance", M. R. Bussieck, L. S. Lasdon, J. D. Pintér, N. V. Sahinidis, slides, PDF dated 11 Sep 2003, https://www.gams.com/archives/presentations/present_BLOglobal.pdf — P (joint)
22. arXiv API listing for au:Sahinidis (14 entries), read 2026-10-10, http://export.arxiv.org/api/query?search_query=au:Sahinidis — P
23. Crossref REST API scan of 323 works with author "Sahinidis" for corrections, errata and retractions, 2026-10-10 — P

**Papers, theses and abstracts (primary)**

24. "Derivative-free optimization: a review of algorithms and comparison of software implementations", L. M. Rios, N. V. Sahinidis, *J. Glob. Optim.* 56:1247–1293, 2013, DOI 10.1007/s10898-012-9951-y — P
25. "Review and comparison of algorithms and software for mixed-integer derivative-free optimization", N. Ploskas, N. V. Sahinidis, *J. Glob. Optim.* 82:433–462, 2022, DOI 10.1007/s10898-021-01085-0 — P
26. "Domain reduction techniques for global NLP and MINLP optimization", Y. Puranik, N. V. Sahinidis, *Constraints* 22:338–376, 2017, DOI 10.1007/s10601-016-9267-5; arXiv:1706.08601 v1 (read) — P
27. "Learning to deactivate probing with graph convolutional network for mixed-integer nonlinear programming", Y. Zhang, N. V. Sahinidis, *Optim. Lett.*, online 3 Jun 2025, DOI 10.1007/s11590-025-02208-2 — P
28. "A novel linear optimization presolve technique based on Fourier-Motzkin elimination", Y. Zhang, N. Ploskas, N. V. Sahinidis, *Math. Program. Comput.* 18:345–378, 2026, DOI 10.1007/s12532-026-00316-3 — P
29. "Constructing Tight Quadratic Relaxations for Global Optimization: I. Outer-Approximating Twice-Differentiable Convex Functions", W. R. Strahl, A. U. Raghunathan, N. V. Sahinidis, C. E. Gounaris, *J. Glob. Optim.* 93:923–952, 2025, DOI 10.1007/s10898-025-01565-7; arXiv:2408.13053 v1; part II DOI 10.1007/s10898-025-01567-5, arXiv:2408.13058 (metadata only) — P
30. "Model-and-search: a derivative-free local optimization algorithm", K. Ma, L. M. Rios, H. Zheng, N. V. Sahinidis, S. Rajagopalan, *Comput. Optim. Appl.* 92:889–921, 2025, DOI 10.1007/s10589-025-00686-9 — P
31. "A decomposition framework for gas network design" (arXiv:2307.07648 v1, 14 Jul 2023) and "A reformulation-enumeration MINLP algorithm for gas network design" (v3, 30 Jan 2024), Y. Li, S. S. Dey, N. V. Sahinidis; *J. Glob. Optim.* 90:931–963, 2024, DOI 10.1007/s10898-024-01424-x (Springer landing page read for the received, accepted and published dates; journal text not read) — P
32. "A Discussion on Practical Considerations with Sparse Regression Methodologies", O. Sarwar, B. Sauk, N. V. Sahinidis, *Statist. Sci.* 35:593–601, 2020, DOI 10.1214/20-STS806; arXiv:2011.09362 v1 and v2 — P
33. "OR-Gym: A Reinforcement Learning Library for Operations Research Problems", C. D. Hubbs, H. D. Perez, O. Sarwar, N. V. Sahinidis, I. E. Grossmann, J. M. Wassick, arXiv:2008.06319 v1 and v2, 2020; GitHub repository hubbs5/or-gym (API metadata read 2026-10-10) — P
34. "Transfer Learning in Information Criteria-based Feature Selection", S. Chen, N. V. Sahinidis, C. Gao, arXiv:2107.02847 v1 and v2; *J. Mach. Learn. Res.* 23(134):1–105, 2022 (JMLR volume 23 listing, https://jmlr.org/papers/v23/) — P
35. "Speeding Up Mixed-Integer Programming Solvers with Sparse Learning for Branching", Bayramoğlu, G. L. Nemhauser, N. V. Sahinidis, arXiv:2604.00094 v1, 31 Mar 2026 — P
36. "Novel Relaxation Techniques for Global Optimization of NLPs and MINLPs", C. J. Nohra Khouri, PhD thesis, Carnegie Mellon University, 2020, DOI 10.1184/R1/12584804.v1 — P (student thesis)
37. "Mixed-integer nonlinear programming 2018", N. V. Sahinidis, *Optim. Eng.* 20:301–306, 2019, DOI 10.1007/s11081-019-09438-1 — P
38. "QPLIB: a library of quadratic programming instances", F. Furini et al. (13 authors including N. Sahinidis), *Math. Program. Comput.* 11:237–265, 2019, DOI 10.1007/s12532-018-0147-4 (submitted version read) — P (joint)
39. "Algorithm-guided experimentation for autonomous AI systems in self-driving laboratories", D. Oh, N. Sahinidis, ACS Spring 2026 presentation, 23 Mar 2026, DOI 10.2172/3031241 (abstract only) — P
40. "ALAMO: Machine learning from data and first principles", N. V. Sahinidis, abstract in Dagstuhl Reports 8(2), Seminar 18081, p. 81, 2018, DOI 10.4230/DagRep.8.2.64 — P
41. "A polyhedral branch-and-cut approach to global optimization", M. Tawarmalani, N. V. Sahinidis, *Math. Program.* 103:225–249, 2005, DOI 10.1007/s10107-005-0581-8 (abstract only) — P
42. "A hybrid LP/NLP paradigm for global optimization relaxations", A. Khajavirad, N. V. Sahinidis, *Math. Program. Comput.* 10:383–421, 2018, DOI 10.1007/s12532-018-0138-5 (abstract only) — P
43. "Solving continuous and discrete nonlinear programs with BARON", Y. Zhang, N. V. Sahinidis, *Comput. Optim. Appl.* 92:1123–1161, 2025, DOI 10.1007/s10589-024-00633-0 (abstract only) — P
44. "Tuning BARON using derivative-free optimization algorithms", J. Liu, N. Ploskas, N. V. Sahinidis, *J. Glob. Optim.* 74:611–637, 2019, DOI 10.1007/s10898-018-0640-3 (abstract only) — P
45. "Branch-and-Model: a derivative-free global optimization algorithm", K. Ma, L. M. Rios, A. Bhosekar, N. V. Sahinidis, S. Rajagopalan, *Comput. Optim. Appl.* 85:337–367, 2023, DOI 10.1007/s10589-023-00466-3 (abstract only) — P
46. "Learning surrogate models for simulation-based optimization", A. Cozad, N. V. Sahinidis, D. C. Miller, *AIChE J.* 60:2211–2227, 2014, DOI 10.1002/aic.14418 (abstract only) — P
47. "Spectral Relaxations and Branching Strategies for Global Optimization of Mixed-Integer Quadratic Programs", C. J. Nohra, A. U. Raghunathan, N. V. Sahinidis, *SIAM J. Optim.* 31:142–171, 2021, DOI 10.1137/19m1271762 (arXiv:2010.04822), and "SDP-quality bounds via convex quadratic relaxations for global optimization of mixed-integer quadratic programs", same authors, *Math. Program.* 196:203–233, 2022, DOI 10.1007/s10107-021-01680-9 (arXiv:2106.13721) — P (dates only; content read through item 36)
48. "GPU computing with Kaczmarz's and other iterative algorithms for linear systems", J. M. Elble, N. V. Sahinidis, P. Vouzis, *Parallel Comput.* 36:215–231, 2010, DOI 10.1016/j.parco.2009.12.003; "Scaling linear optimization problems prior to application of the simplex method", J. M. Elble, N. V. Sahinidis, *Comput. Optim. Appl.* 52:345–371, 2012, DOI 10.1007/s10589-011-9420-4 — P (metadata only)
49. "Global optimization of general non-convex problems with intermediate bilinear substructures", K. Zorn, N. V. Sahinidis, *Optim. Methods Softw.* 29:442–462, 2014, DOI 10.1080/10556788.2013.783032; "Global optimization of general nonconvex problems with intermediate polynomial substructures", same authors, *J. Glob. Optim.* 59:673–693, 2014, DOI 10.1007/s10898-014-0190-2 — P (metadata only)
50. Papers that seeded the BARON test libraries (§A2): DOIs 10.1080/10556780902883184, 10.1007/s10107-011-0462-2, 10.1007/s12532-014-0073-z, 10.1287/ijoc.2017.0761, 10.1007/s10898-016-0491-8, 10.1007/s10107-018-1289-x — P (metadata only)
51. Earlier arXiv postings (dates only, §F4): Austin, Sahinidis & Trahan, DOI 10.1016/j.cherd.2016.10.014 (arXiv:1701.03978); Ploskas, Laughman, Raghunathan & Sahinidis, DOI 10.1016/j.cherd.2017.05.015 (arXiv:1705.10437); Wilson & Sahinidis, DOI 10.1016/j.compchemeng.2017.02.010 (arXiv:1705.10918); Amaran, Sahinidis, Sharda & Bury, DOI 10.1007/s10479-015-2019-x (arXiv:1706.08591); the corrections DOI 10.1021/ie00004a041 (1992) and DOI 10.1007/s11081-021-09651-x (2021) — P (metadata only)
52. "The ALAMO Approach to Machine Learning: Best Subset Selection, Adaptive Sampling, and Constrained Regression", N. Sahinidis, UConn Institute for Advanced Systems Engineering distinguished lecture, 10 Apr 2017, https://www.youtube.com/watch?v=BZ76x6VWllA; YouTube auto-caption transcript saved in `sources/talks/` by a parallel agent of this workflow — P (ASR, not checked by a human)
53. "Optimization and Machine Learning Nexus: Model-Based and Data-Driven Approaches", N. Sahinidis, Texas A&M Energy Institute Distinguished Lecture, 5 Mar 2025, https://www.youtube.com/watch?v=E320mxWiR24; YouTube auto-caption transcript saved in `sources/talks/` by a parallel agent of this workflow — P (ASR, not checked by a human)

**Outside sources (secondary or observed)**

54. "A comparison of complete global optimization solvers", A. Neumaier, O. Shcherbina, W. Huyer, T. Vinkó, *Math. Program.* 103:335–356, 2005, DOI 10.1007/s10107-005-0585-4 (author preprint, https://arnold-neumaier.at/ms/comparison.pdf) — S (observed)
55. *Optima* 73, Mathematical Programming Society newsletter, January 2007, pp. 3–4, Beale–Orchard-Hays Prize 2006 citation, https://mathopt.zib.de/Optima-Issues/optima73.pdf — S (observed; found by WebSearch)
56. Dagstuhl Seminar 18081 report, §4.2 "Sound experimentation with MINLP software", P. Bonami, A. M. Gleixner, J. Linderoth, R. Misener (eds.), pp. 84–85, 2018, DOI 10.4230/DagRep.8.2.64 — S (observed)
57. H. Mittelmann, "Mixed Integer Nonlinear Programming Benchmark (MINLPLIB)", 26 Feb 2026, https://plato.asu.edu/ftp/minlp.html — S (observed)
58. H. Mittelmann, "Continuous Non-Convex QPLIB Benchmark", 17 May 2026, https://plato.asu.edu/ftp/cnconv.html; "Binary Non-Convex QPLIB Benchmark", 9 May 2026, https://plato.asu.edu/ftp/qplib.html — S (observed)
59. H. Mittelmann, "Discrete Non-Convex QPLIB Benchmark (non-binary)", 12 May 2026, https://plato.asu.edu/ftp/nonbinary.html; "Nonconvex QUBO-QPLIB Benchmark", 21 Sep 2026, https://plato.asu.edu/ftp/qubo.html — S (observed)
60. SECQUOIA organization page, GitHub, read 2026-10-10, https://github.com/SECQUOIA — S
61. OpenReview API notes search for "Sahinidis", 2026-10-10 (only DBLP-imported records returned) — S
62. "Best Subset, Forward Stepwise or Lasso? ...", T. Hastie, R. Tibshirani, R. Tibshirani, *Statist. Sci.* 35:579–592, 2020, DOI 10.1214/19-STS733; "Sparse Regression: Scalable Algorithms and Empirical Performance", D. Bertsimas, J. Pauphilet, B. Van Parys, *Statist. Sci.* 35:555–578, 2020, DOI 10.1214/19-STS701; rejoinders DOI 10.1214/20-sts733rej and DOI 10.1214/20-sts701rej — S (metadata only)
63. jump-dev/BARON.jl issue list, GitHub, read 2026-10-10, https://github.com/jump-dev/BARON.jl/issues (titles only; issue 77 asks for trigonometric functions) — S
64. Wayback Machine CDX listings for archimedes.scs.uiuc.edu/baron/* and capd.cheme.cmu.edu, 2026-10-10 — S (index)
65. AIChE Annual Meeting abstracts "Third generation branch-and-reduce algorithms and software" (2012, 398a) and "Recent advances in the BARON project" (2016, 314a), https://proceedings.aiche.org/ — S (not accessible: HTTP 403; found by WebSearch)
66. CAPD sponsor archive, https://capd-archive.cheme.cmu.edu/sponsor-resources — S (login-restricted, HTTP 401; not accessed)

Identifier check, run on the finished file: a script extracted every DOI and arXiv id from this file and compared them with the identifiers resolved in this run through the Crossref API, doi.org or the repository, and the arXiv API.
