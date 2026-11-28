# Ambros M. Gleixner · 01 · Publication landscape and signature works

| | |
|---|---|
| Researcher | Ambros M. Gleixner (DBLP pid 07/3479; ORCID 0000-0003-0391-5903; Google Scholar user DUFnBNcAAAAJ, linked from his homepage). Living. Homepage (S1, undated, footer © 2008–2022): professor for discrete mathematics and operations research at HTW Berlin and affiliated researcher in the ZIB division Mathematical Algorithmic Intelligence |
| Dimension | Research agent 01 of 06: publication landscape and dissection of signature works (framework §二 Agent 1, §五) |
| Research date | 2026-11-08 |
| Sources consulted | 35, listed as S1–S35 under "Sources" (30 primary, 5 secondary). WebSearch: 1 of the 5 allowed calls used; everything else via curl, WebFetch, the Crossref REST API and `scripts/dblp_works.py` |
| Local corpus | `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep`: no user-supplied material. `private/` was not opened |
| OpenAlex | not queried (`OPENALEX_API_KEY` is not set) |
| Quotation policy | To respect copyright, findings are paraphrased with a pinpoint page; exactly one short verbatim phrase is quoted (§2, SW1, marked with quotation marks). Check exact wording at the cited page before quoting downstream. Titles of works are given in italics as identifiers |

**Tags.**
- **[stated]**: said or written by Gleixner in a sole-author text (thesis, homepage, CV, his signed announcements). **[stated, joint]**: a co-signed paper whose "we" voice cannot be split among authors.
- **[practice]**: what the record shows was done (experiments, tables, test sets, version histories, the publication record itself).
- **[observed]**: what others recorded (bibliographic databases, citation counts, other people's theses and papers).
- **[inferred]**: my inference; the basis is named.
- **P / S**: primary / secondary source.

**Page conventions.** Thesis (S4): printed page numbers (roman for front matter). MIPLIB 2017 (S5): journal pagination 443–490. ZIB-Report/arXiv versions (S6–S10): the report's own page numbers (title pages unnumbered).

**Reading depth.**
- Read in full or in large part: S4 (front matter, introduction, §1.3–1.4, §2.6, §3.1 opening, §3.2.1, §3.5, ch. 4 opening, §6.5, ch. 7 opening, §7.5, ch. 8), S5 (§1–2, §4.7, §7, acknowledgements), S6 (complete), S8 (complete except tables), S2 (complete), S1 (complete).
- Opening pages only (abstract and introduction): S7, S9, S10.
- Abstract and version history only: S11–S26 (arXiv abstract pages).
- Metadata only: S27–S31 (indexes), S32–S35.
- Not read: the IJOC 2016 iterative-refinement paper, the JOGO 2017 OBBT paper and the ISSAC 2012 paper as published (their content is taken from the thesis, which says it contains them, S4 p. 5); MIPLIB 2010; the SCIP Optimization Suite release reports; the full texts of everything from 2022 on, apart from the opening pages of S9 and S10.

---

## 0. Authorship and role labels (must survive into the skill)

The team.json hint asks to keep what Gleixner wrote apart from what he supervised. The ZIB/HTW group mostly orders authors alphabetically or puts students first, so position alone is weak evidence (§1.4).

| Label | Evidence | Tag |
|---|---|---|
| Sole-authored works: the Diplom thesis (2008, W1), ZIB-Report 12-36 on factorizing a reduced basis matrix (2012, W10) and the PhD thesis (2015, W16). No sole-authored journal article was found | S2 pp. 2–3; S28 | [practice] P |
| He says he himself implemented a number of rational extensions to SoPlex, built around the ideas of the LP-oracles paper (W33) and his thesis | S1 (Projects paragraph) | [stated] P |
| The software of the thesis (iterative refinement, exact LP, OBBT, branching rules) went into SoPlex and SCIP | S4 p. 6 | [stated] P |
| The iterative-refinement line was started on Daniel Steffy's initiative to study iterative refinement with SoPlex; Kati Wolter tested and profiled the exact SoPlex extensions | S4 p. iii | [stated] P |
| The first warm-start experiment for exact LP (§3.2.1) was designed jointly with Steffy and Wolter | S4 p. 64 | [stated] P |
| The OBBT components of SCIP were implemented and improved by Benjamin Müller and Stefan Weltge | S4 p. iii | [stated] P |
| The branching work of thesis ch. 7 is partly joint with Timo Berthold | S4 p. 149 | [stated] P |
| VIPR (W23): three authors in alphabetical order, roles not divided; they wrote a C++ reference checker and added certificate output to the exact version of SCIP built by Wolter | S6 pp. 2, 8 (acknowledgements) | [stated, joint] P |
| MIPLIB 2017 (W47): corresponding author; first three authors (Gleixner, Hendel, Gamrath) then the other 13 in alphabetical order, so the first three are contribution-ordered | S5 p. 443; author list | [practice] P; ordering rule [inferred] |
| He signed the MIPLIB 2017 call for contributions alone, on behalf of an initiative of ten organizations, and co-signed the release with Hendel and Gamrath | S33, S34 | [practice] P |
| SCIP Optimization Suite 5.0 (Dec 2017) and 6.0 (Jul 2018): first author, the rest alphabetical. In 3.2, 4.0 and 7.0–10.0 he sits in the alphabetical block | S32 | [practice] P; [inferred] he coordinated the 5.0 and 6.0 reports |
| PaPILO (W58): he is listed first, but the order Gleixner, Gottwald, Hoen is alphabetical, and his own co-signed paper credits Leona Gottwald with creating PaPILO | S8 p. 12 (acknowledgements); S28 | [stated, joint] P |
| Exact rational MIP since 2021 (W48, W63, W68, W72): first author Leon Eifler or another junior; Eifler's TU Berlin PhD (2025) has Thorsten Koch as advisor and Gleixner as one of four referees | S35 | [practice] P |
| Student-led papers from 2019 on: Gleixner last or inside an alphabetical senior block (W37–W83) | DBLP order (S28) | [practice] P; supervision role [inferred]; formal advisorship verified only for Eifler |

---

## 1. Publication landscape

### 1.1 Record coverage

- [observed, S] **DBLP** (S28, SPARQL via `scripts/dblp_works.py`, 2026-11-08): 74 records, 2009–2026 (33 articles, 24 conference papers, 15 CoRR preprints, 2 data sets); 72 carry a DOI, 14 an arXiv id. Affiliation HTW Berlin and ZIB. DBLP misses the theses, ZIB-Reports, SCIP release reports, the NACO 2012 papers, the J. Comput. Math. paper, the IJOC 2025 cut-based conflict analysis paper and most post-2023 preprints.
- [observed, S] **arXiv** (S29): 48 preprints, 1604.00513 (April 2016) to 2607.15837 (July 2026). The team.json estimate of about 48 is confirmed. Nothing before 2016: earlier preprints went out as ZIB-Reports (S2).
- [observed, S] **Google Scholar** (S30, WebFetch rendering of pages 1–2): 107 items; 5,496 citations (3,697 since 2021), h-index 31, i10-index 51. Yearly citations rise from 14 (2010) to 759 (2025) and 799 (2026, partial year), with one dip (125 in 2014, 112 in 2015). Profile keywords he chose himself: mixed-integer nonlinear programming, arithmetically exact optimization, operations research [stated, P]. The rendering omitted author and venue lines; a few items are duplicates or junk entries (for example a CP 2023 proceedings volume and an item titled *Based on Joint Work With...*).
- [practice, P] **Homepage** (S1) and **long CV** (S2, dated July 31, 2017, 7 pp.): the CV lists 28 publications to 2017, 57 talks (2009–2016), funded projects, software, teaching and refereeing. The homepage BibTeX file (S3) stops in 2014.
- [observed, S] **Crossref** (S31): metadata for 25 DOIs (dates, received/accepted, counts).
- Not reached: Semantic Scholar (HTTP 429 twice), ZIB OPUS (Anubis bot wall; not bypassed). See Gaps.

### 1.2 Verified works

Every identifier was resolved with a tool on 2026-11-08: DBLP (S28) unless another source is named. "Read" says what was read in this run. Author order: "alpha" = alphabetical by surname. Items with only a ZIB-Report number or URN come from his own CV (S2) or scipopt.org (S32); those URNs were not resolved because ZIB OPUS was unreachable.

| # | Year | Work (full title) | Venue | Identifier | Authors (order) | Read | Tags |
|---|---|---|---|---|---|---|---|
| W1 | 2008 | *Solving Large-scale Open Pit Mining Production Scheduling Problems by Integer Programming* | Diplom thesis, TU Berlin (supervisor R. H. Möhring) | URN urn:nbn:de:0297-zib-11389 (S2, S3) | Gleixner | not read | [practice] P |
| W2 | 2009 | *LP-based disaggregation approaches to solving the open pit mining production scheduling problem with block processing selectivity* | Comput. Oper. Res. 36(4):1064–1089 | DOI 10.1016/j.cor.2007.12.006 | Boland, Dumitrescu, Froyland, Gleixner (alpha) | not read | [practice] P |
| W3 | 2010 | *Undercover – a primal heuristic for MINLP based on sub-MIPs generated by set covering* | Proc. EWMINLP 2010, CIRM Marseille, pp. 103–112 | venue + year + title (S2, S3) | Berthold, Gleixner (alpha) | not read | [practice] P |
| W4 | 2011 | *MIPLIB 2010* | Math. Program. Comput. 3(2):103–163 | DOI 10.1007/s12532-011-0025-9 | Koch, then 15 alpha; Gleixner 9th | not read | [practice] P |
| W5 | 2011 | *On the computational impact of MIQCP solver components* | ZIB-Report 11-01 | URN urn:nbn:de:0297-zib-11998 (S2) | Berthold, Gleixner, Heinz, Vigerske (alpha) | not read | [practice] P |
| W6 | 2012 | *Comparing MIQCP Solvers to a Specialised Algorithm for Mine Production Scheduling* | HPSC 2009 proceedings (Springer 2012), pp. 25–39 | DOI 10.1007/978-3-642-25707-0_3 | Bley, Gleixner, Koch, Vigerske (alpha) | not read | [practice] P |
| W7 | 2012 | *Improving the accuracy of linear programming solvers with iterative refinement* | ISSAC 2012, pp. 187–194 | DOI 10.1145/2442829.2442858 | Gleixner, Steffy, Wolter (alpha) | via thesis | [practice] P |
| W8 | 2012 | *Towards globally optimal operation of water supply networks* | NACO 2(4):695–711 | DOI 10.3934/naco.2012.2.695 (Crossref) | Gleixner, Held, Huang, Vigerske (alpha) | not read | [practice] P |
| W9 | 2012 | *Analyzing the computational impact of MIQCP solver components* | NACO 2(4):739–748 | DOI 10.3934/naco.2012.2.739 (Crossref) | Berthold, Gleixner, Heinz, Vigerske (alpha) | not read | [practice] P |
| W10 | 2012 | *Factorization and update of a reduced basis matrix for the revised simplex method* | ZIB-Report 12-36 | URN urn:nbn:de:0297-zib-16349 (S2) | Gleixner | not read | [practice] P |
| W11 | 2012 | *Solving mixed integer linear and nonlinear problems using the SCIP Optimization Suite* | ZIB-Report 12-27 | URN urn:nbn:de:0297-zib-15654 (S2) | Berthold, Gamrath, Gleixner, Heinz, Koch, Shinano (alpha) | not read | [practice] P |
| W12 | 2013 | *Learning and Propagating Lagrangian Variable Bounds for Mixed-Integer Nonlinear Programming* | CPAIOR 2013, pp. 355–361 | DOI 10.1007/978-3-642-38171-3_26 | Gleixner, Weltge (alpha) | via thesis | [practice] P |
| W13 | 2013 | *Undercover Branching* | SEA 2013, pp. 212–223 | DOI 10.1007/978-3-642-38527-8_20 | Berthold, Gleixner (alpha) | via thesis | [practice] P |
| W14 | 2014 | *Undercover: a primal MINLP heuristic exploring a largest sub-MIP* | Math. Program. 144(1–2):315–346 | DOI 10.1007/s10107-013-0635-2 | Berthold, Gleixner (alpha) | via thesis | [practice] P |
| W15 | 2015 | *Branching on Multi-aggregated Variables* | CPAIOR 2015, pp. 141–156 | DOI 10.1007/978-3-319-18008-3_10 | Gamrath, Melchiori, Berthold, Gleixner, Salvagnin | not read | [practice] P |
| W16 | 2015 | *Exact and fast algorithms for mixed-integer nonlinear programming* | PhD thesis, TU Berlin (defended 24 June 2015; reviewers Grötschel, Koch, Lodi) | DOI 10.14279/depositonce-4938 | Gleixner | large parts (S4) | [stated] [practice] P |
| W17 | 2016 | *Iterative Refinement for Linear Programming* | INFORMS J. Comput. 28(3):449–464 | DOI 10.1287/ijoc.2016.0692 | Gleixner, Steffy, Wolter (alpha) | via thesis | [practice] P |
| W18 | 2016 | *Towards an Accurate Solution of Wireless Network Design Problems* | ISCO 2016, pp. 135–147 | DOI 10.1007/978-3-319-45587-7_12; arXiv 1604.00513 | D'Andreagiovanni, Gleixner (alpha) | not read | [practice] P |
| W19 | 2016 | *The SCIP Optimization Suite 3.2* | ZIB-Report 15-60 (Feb 2016) | report number (S2, S32) | Gamrath, then alpha; Gleixner 4th | not read | [practice] P |
| W20 | 2016 | *Methoden zur Reduktion der Rechenzeit linearer Optimierungsmodelle in der Energiewirtschaft – Eine Performance-Analyse* | EnInnov 2016, Graz | venue + year + title (S2) | Cao, Gleixner, Miltenberger (alpha) | not read | [practice] P |
| W21 | 2017 | *The SCIP Optimization Suite 4.0* | ZIB-Report 17-12 (Mar 2017) | report number (S2, S32) | Maher, then alpha; Gleixner 5th | not read | [practice] P |
| W22 | 2017 | *Three enhancements for optimization-based bound tightening* | J. Glob. Optim. 67(4):731–757 | DOI 10.1007/s10898-016-0450-4 | Gleixner, Berthold, Müller, Weltge (first, not alpha) | via thesis | [practice] P |
| W23 | 2017 | *Verifying Integer Programming Results* | IPCO 2017, pp. 148–160 | DOI 10.1007/978-3-319-59250-3_13; arXiv 1611.08832; ZIB-Report 16-58 | Cheung, Gleixner, Steffy (alpha) | full (arXiv v2) (S6) | [stated, joint] [practice] P |
| W24 | 2017 | *The SCIP Optimization Suite 5.0* | ZIB-Report 17-61 (Dec 2017) | report number (S32) | Gleixner, then 21 alpha | not read | [practice] P |
| W25 | 2018 | *The SCIP Optimization Suite 6.0* | ZIB-Report 18-26 (Jul 2018) | report number (S32) | Gleixner, then 24 alpha | not read | [practice] P |
| W26 | 2018 | *SCIP: global optimization of mixed-integer nonlinear programs in a branch-and-cut framework* | Optim. Methods Softw. 33(3):563–593 | DOI 10.1080/10556788.2017.1335312 | Vigerske, Gleixner | not read | [practice] P |
| W27 | 2018 | *Mixed-Integer Programming for Cycle Detection in Nonreversible Markov Processes* | Multiscale Model. Simul. 16(1):248–265 | DOI 10.1137/16M1091162; arXiv 1609.02063 | Witzig, Beckenbach, Eifler, Fackeldey, Gleixner, Grever, Weber | not read | [practice] P |
| W28 | 2018 | *Optimizing Large-Scale Linear Energy System Problems with Block Diagonal Structure by Using Parallel Interior-Point Methods* | OR 2017 proceedings, pp. 641–647 | DOI 10.1007/978-3-319-89920-6_85 | Breuer, …, Gleixner (7th of 11, alpha) | not read | [practice] P |
| W29 | 2018 | *Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization (Dagstuhl Seminar 18081)* | Dagstuhl Reports 8(2):64–87 | DOI 10.4230/DagRep.8.2.64 | Bonami, Gleixner, Linderoth, Misener (alpha) | not read | [practice] P |
| W30 | 2018 | *Preface* (Mathematical Optimization at ICMS 2016) | Optim. Methods Softw. 33(3):419 | DOI 10.1080/10556788.2018.1459255 | Gleixner, Kirches, Mitchell, Ralphs (alpha) | not read | [practice] P |
| W31 | 2019 | *QPLIB: a library of quadratic programming instances* | Math. Program. Comput. 11(2):237–265 | DOI 10.1007/s12532-018-0147-4 | Furini, Traversi, then 11 alpha; Gleixner 5th | not read | [practice] P |
| W32 | 2019 | *Solving quadratic programs to high precision using scaled iterative refinement* | Math. Program. Comput. 11(3):421–455 | DOI 10.1007/s12532-019-00154-6; arXiv 1803.07178 | Weber, Sager, Gleixner | not read | [practice] P |
| W33 | 2019 / 2020 | *Linear Programming Using Limited-Precision Oracles* | IPCO 2019, pp. 399–412; Math. Program. 183(1):525–554 (2020) | DOI 10.1007/978-3-030-17953-3_30; DOI 10.1007/s10107-019-01444-6; arXiv 1912.12820; ZIB-Report 19-57 | Gleixner, Steffy (alpha) | opening pages (S7) | [practice] P |
| W34 | 2019 | *Tackling Industrial-Scale Supply Chain Problems by Mixed-Integer Programming* | J. Comput. Math. 37(6):866–888 (ZIB-Report 16-45) | DOI 10.4208/jcm.1905-m2019-0055 (Crossref) | Gamrath, Gleixner, Koch, Miltenberger, Kniasew, Schlögel, Martin, Weninger | not read | [practice] P |
| W35 | 2020 | *The SCIP Optimization Suite 7.0* | ZIB-Report 20-10 (Mar 2020) | report number (S32) | Gamrath, then alpha; Gleixner 8th | not read | [practice] P |
| W36 | 2017 / 2018 | *Exact Methods for Recursive Circle Packing* (arXiv v1) → *Price-and-verify: a new algorithm for recursive circle packing using Dantzig–Wolfe decomposition* | Ann. Oper. Res. 284(2):527–555 (online 14 Dec 2018, issue 2020) | DOI 10.1007/s10479-018-3115-5; arXiv 1702.07799; ZIB-Report 17-07 | Gleixner, Maher, Müller, Pedroso (alpha) | abstracts v1 and v2 (S12) | [practice] P |
| W37 | 2020 | *Using Two-Dimensional Projections for Stronger Separation and Propagation of Bilinear Terms* | SIAM J. Optim. 30(2):1339–1365 | DOI 10.1137/19M1249825; arXiv 1903.05521 | Müller, Serrano, Gleixner | not read | [practice] P |
| W38 | 2020 | *On the relation between the extended supporting hyperplane algorithm and Kelley's cutting plane algorithm* | J. Glob. Optim. 78(1):161–179 | DOI 10.1007/s10898-020-00906-y; arXiv 1905.08157 | Serrano, Schwarz, Gleixner | abstract (S11) | [practice] P |
| W39 | 2020 / 2022 | *On Generalized Surrogate Duality in Mixed-Integer Nonlinear Programming* | IPCO 2020, pp. 322–337; Math. Program. 192(1):89–118 (2022) | DOI 10.1007/978-3-030-45771-6_25; DOI 10.1007/s10107-021-01691-6; arXiv 1912.00356 | Müller, Muñoz, Gasse, Gleixner, Lodi, Serrano | not read | [practice] P |
| W40 | 2020 | *Two-row and two-column mixed-integer presolve using hashing-based pairing methods* | EURO J. Comput. Optim. 8(3):205–240 | DOI 10.1007/s13675-020-00129-6 | Gemander, Chen, Weninger, Gottwald, Gleixner, Martin | not read | [practice] P |
| W41 | 2020 | *First Experiments with Structure-Aware Presolving for a Parallel Interior-Point Method* | OR 2019 proceedings, pp. 105–111 | DOI 10.1007/978-3-030-48439-2_13; arXiv 1908.00796 | Gleixner, Kempke, Koch, Rehfeldt, Uslu (alpha) | not read | [practice] P |
| W42 | 2020 / 2022 | *Accelerating Domain Propagation: an Efficient GPU-Parallel Algorithm over Sparse Matrices* | IA3@SC 2020, pp. 1–11; Parallel Comput. 109:102874 (2022) | DOI 10.1109/IA351965.2020.00007; DOI 10.1016/j.parco.2021.102874; arXiv 2009.07785 | Sofranac, Gleixner, Pokutta | not read | [practice] P |
| W43 | 2021 / 2022 | *An Algorithm-Independent Measure of Progress for Linear Constraint Propagation* | CP 2021, 52:1–52:17; Constraints 27(4):432–455 (2022) | DOI 10.4230/LIPIcs.CP.2021.52; DOI 10.1007/s10601-022-09338-9; arXiv 2106.07573 | Sofranac, Gleixner, Pokutta | not read | [practice] P |
| W44 | 2021 | *Conflict-Driven Heuristics for Mixed Integer Programming* | INFORMS J. Comput. 33(2):706–720 | DOI 10.1287/ijoc.2020.0973; arXiv 1902.02615 | Witzig, Gleixner | not read | [practice] P |
| W45 | 2021 | *Learn to relax: Integrating 0-1 integer linear programming with pseudo-Boolean conflict-driven search* | Constraints 26(1):26–55 | DOI 10.1007/s10601-020-09318-x | Devriendt, Gleixner, Nordström (alpha) | not read | [practice] P |
| W46 | 2021 | *Learning to Schedule Heuristics in Branch and Bound* | NeurIPS 2021, pp. 24235–24246 | arXiv 2103.10294 | Chmiela, Khalil, Gleixner, Lodi, Pokutta | not read | [practice] P |
| W47 | 2021 | *MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library* | Math. Program. Comput. 13(3):443–490 | DOI 10.1007/s12532-020-00194-3 | Gleixner, Hendel, Gamrath, then 13 alpha | large parts (S5) | [stated, joint] [practice] P |
| W48 | 2021 / 2023 | *A Computational Status Update for Exact Rational Mixed Integer Programming* | IPCO 2021, pp. 163–177; Math. Program. 197(2):793–812 (online Jan 2022) | DOI 10.1007/978-3-030-73879-2_12; DOI 10.1007/s10107-021-01749-5; arXiv 2101.09141; ZIB-Report 21-04 | Eifler, Gleixner (alpha) | full (arXiv v1) (S8) | [stated, joint] [practice] P |
| W49 | 2021 | *The SCIP Optimization Suite 8.0* | ZIB-Report 21-41 | arXiv 2112.08872 | Bestuzheva, then alpha; Gleixner 10th | not read | [practice] P |
| W50 | 2018 / 2022 | *Chvátal's Conjecture Holds for Ground Sets of Seven Elements* (arXiv v1) → *A Safe Computational Framework for Integer Programming Applied to Chvátal's Conjecture* | ACM Trans. Math. Softw. 48(2):14:1–14:12 | DOI 10.1145/3485630; arXiv 1809.01572 | Eifler, Gleixner, Pulaj (alpha) | abstracts v1 and v2 (S13) | [practice] P |
| W51 | 2022 | *A massively parallel interior-point solver for LPs with generalized arrowhead structure, and applications to energy system models* | Eur. J. Oper. Res. 296(1):60–71 | DOI 10.1016/j.ejor.2021.06.063 | Rehfeldt, Hobbie, Schönheit, Koch, Möst, Gleixner | not read | [practice] P |
| W52 | 2022 | *The Machine Learning for Combinatorial Optimization Competition (ML4CO): Results and Insights* | NeurIPS 2021 Competitions and Demonstrations Track, pp. 220–231 | arXiv 2203.02433 | Gasse et al.; Gleixner 9th of 42 | not read | [practice] P |
| W53 | 2023 | *Enabling Research through the SCIP Optimization Suite 8.0* | ACM Trans. Math. Softw. 49(2):22:1–22:21 | DOI 10.1145/3585516; arXiv 2303.07101 | Bestuzheva, then alpha; Gleixner 10th of 35 | not read | [practice] P |
| W54 | 2023 | *A computational study of perspective cuts* | Math. Program. Comput. 15(4):703–731 | DOI 10.1007/s12532-023-00246-4; arXiv 2103.09573 | Bestuzheva, Gleixner, Vigerske (alpha) | not read | [practice] P |
| W55 | 2023 / 2025 | *Efficient Separation of RLT Cuts for Implicit and Explicit Bilinear Products* (IPCO) / *…Bilinear Terms* (MP) | IPCO 2023, pp. 14–28; Math. Program. 210(1):47–74 (2025) | DOI 10.1007/978-3-031-32726-1_2; DOI 10.1007/s10107-024-02104-0; arXiv 2211.13545 | Bestuzheva, Gleixner, Achterberg | not read | [practice] P |
| W56 | 2023 | *Improving Conflict Analysis in MIP Solvers by Pseudo-Boolean Reasoning* | CP 2023, 27:1–27:19 | DOI 10.4230/LIPIcs.CP.2023.27; arXiv 2307.14166 | Mexi, Berthold, Gleixner, Nordström | not read | [practice] P |
| W57 | 2023 | *Online Learning for Scheduling MIP Heuristics* | CPAIOR 2023, pp. 114–123 | DOI 10.1007/978-3-031-33271-5_8; arXiv 2304.03755 | Chmiela, Gleixner, Lichocki, Pokutta | not read | [practice] P |
| W58 | 2023 | *PaPILO: A Parallel Presolving Library for Integer and Linear Optimization with Multiprecision Support* | INFORMS J. Comput. 35(6):1329–1341 | DOI 10.1287/ijoc.2022.0171; arXiv 2206.10709 | Gleixner, Gottwald, Hoen (alpha) | opening pages (S9) | [practice] P |
| W59 | 2023 | *Hybrid Genetic Search for Dynamic Vehicle Routing with Time Windows* | preprint | arXiv 2307.11800 | Ghannam, Gleixner | abstract (S16) | [practice] P |
| W60 | 2023 | *Scylla: a matrix-free fix-propagate-and-project heuristic for mixed-integer optimization* | preprint | arXiv 2307.03466 | Mexi, Besançon, Bolusani, Chmiela, Hoen, Gleixner | abstract (S15) | [practice] P |
| W61 | 2022 / 2023 | *Strengthening SONC Relaxations with Constraints Derived from Variable Bounds* | HUGO 2022 (4 pp.) and an extended preprint | arXiv 2211.05518; arXiv 2304.12145 | Bestuzheva, Gleixner, Völker / Bestuzheva, Völker, Gleixner | listing only | [practice] P |
| W62 | 2023 | *A proof system for certifying symmetry and optimality reasoning in integer programming* | preprint | arXiv 2311.03877 | van Doornmalen, Eifler, Gleixner, Hojny (alpha) | abstract (S17) | [practice] P |
| W63 | 2024 | *Safe and Verified Gomory Mixed-Integer Cuts in a Rational Mixed-Integer Program Framework* | SIAM J. Optim. 34(1):742–763 | DOI 10.1137/23M156046X; arXiv 2303.12365 | Eifler, Gleixner (alpha) | abstract (S14) | [practice] P |
| W64 | 2024 | *The MIP Workshop 2023 Computational Competition on reoptimization* | Math. Program. Comput. 16(2):255–266 | DOI 10.1007/s12532-024-00256-w; arXiv 2311.14834 | Bolusani, Besançon, Gleixner, Berthold, D'Ambrosio, Muñoz, Paat, Thomopulos | not read | [practice] P |
| W65 | 2024 | *Certifying MIP-Based Presolve Reductions for 0-1 Integer Linear Programs* | CPAIOR 2024, pp. 310–328 | DOI 10.1007/978-3-031-60597-0_20; arXiv 2401.09277 | Hoen, Oertel, Gleixner, Nordström | not read | [practice] P |
| W66 | 2024 | *Branch and Cut for Partitioning a Graph into a Cycle of Clusters* | ISCO 2024, pp. 97–108 | DOI 10.1007/978-3-031-60924-4_8; arXiv 2401.08412 | Eifler, Witzig, Gleixner | not read | [practice] P |
| W67 | 2024 | *Branch and Price for the Length-Constrained Cycle Partition Problem* | preprint | arXiv 2401.17937 | Ghannam, Mexi, Lam, Gleixner | abstract (S21) | [practice] P |
| W68 | 2024 | *Certified Constraint Propagation and Dual Proof Analysis in a Numerically Exact MIP Solver* | preprint | arXiv 2403.13567 | Borst, Eifler, Gleixner (alpha) | abstract (S22) | [practice] P |
| W69 | 2024 | *The SCIP Optimization Suite 9.0* | ZIB-Report 24-02-29 | arXiv 2402.17702 | Bolusani, then alpha; Gleixner 10th | not read | [practice] P |
| W70 | 2025 | *A diving heuristic for mixed-integer problems with unbounded semi-continuous variables* | EURO J. Comput. Optim. 13:100107 | DOI 10.1016/j.ejco.2025.100107; arXiv 2403.19411 | Halbig, Hoen, Gleixner, Witzig, Weninger | not read | [practice] P |
| W71 | 2025 | *Analyzing the Numerical Correctness of Branch-and-Bound Decisions for Mixed-Integer Programming* | CPAIOR 2025, pp. 35–50 | DOI 10.1007/978-3-031-95976-9_3; arXiv 2412.14710 | Hoen, Gleixner | opening pages (S10) | [stated, joint] [practice] P |
| W72 | 2025 | *Combining Precision Boosting with LP Iterative Refinement for Exact Linear Optimization* | INFORMS J. Comput. 37(4):933–944 | DOI 10.1287/ijoc.2023.0409; arXiv 2311.08037 | Eifler, Nicolas-Thouvenin, Gleixner | abstract (S18) | [practice] P |
| W73 | 2025 | *Investigating Round-Up Properties for the Length-Constrained Cycle Partition Problem* | OR 2024 proceedings, pp. 193–198 | DOI 10.1007/978-3-031-92575-7_27 | Runnwerth, Ghannam, Gleixner | not read | [practice] P |
| W74 | 2025 | *Sorting Criteria for Line-Based Periodic Timetabling Heuristics* | OR 2024 proceedings, pp. 348–354 | DOI 10.1007/978-3-031-92575-7_50 | Ebert, Masing, Lindner, Gleixner | not read | [practice] P |
| W75 | 2025 | *Cut-Based Conflict Analysis in Mixed Integer Programming* | INFORMS J. Comput. (online 12 Nov 2025) | DOI 10.1287/ijoc.2024.0999 (Crossref); arXiv 2410.15110 | Mexi, Serrano, Berthold, Gleixner, Nordström | abstract (S20) | [practice] P |
| W76 | 2025 | *The SCIP Optimization Suite 10.0* | preprint (Optimization Online, Nov 2025) | arXiv 2511.18580 | Hojny, then alpha; Gleixner 9th of 34 | abstract (S23) | [practice] P |
| W77 | 2025 | *Branch and price for nonlinear production-maintenance scheduling in complex machinery* | preprint | arXiv 2511.07143 | Dionísio, Gleixner, Pedroso, Bestuzheva | listing only | [practice] P |
| W78 | 2025 | *Clique Probing for Mixed-Integer Programs* | preprint | arXiv 2512.17551 | von Holly-Ponientzietz, Hoen, Turner, Gleixner | listing only | [practice] P |
| W79 | 2026 | *MIP-DD: Delta Debugging for Mixed-Integer Programming Solvers* | INFORMS J. Comput. 38(2):414–423 | DOI 10.1287/ijoc.2024.0844; arXiv 2405.19770 | Hoen, Kamp, Gleixner | abstract (S19) | [practice] P |
| W80 | 2026 | *Distributed Parallel Structure-Aware Presolving for Arrowhead Linear Programs* | preprint | arXiv 2603.03498 | Kempke, Maher, Rehfeldt, Gleixner, Koch, Uslu | listing only | [practice] P |
| W81 | 2026 | *CHAP: A Hybrid GPU-CPU Heuristic for MIP* | preprint | arXiv 2605.05086 | Tjusila, Hoen, Kempke, Mexi, Berthold, Gleixner, Koch, Pokutta | abstract (S24) | [practice] P |
| W82 | 2026 | *Boolean Algebra -- Driven Sepsis Diagnosis* | preprint | arXiv 2605.29686 | Weber, Kappert, Reidelbach, Gleixner, Fackeldey, Bauer | abstract (S25) | [practice] P |
| W83 | 2026 | *A Numerically-safe Branch-Price-and-Cut Algorithm for the Length-Constrained Cycle Partition Problem* | preprint | arXiv 2607.15837 | Ghannam, Gleixner, Mexi, Lam | abstract (S26) | [practice] P |

Not listed as works because no identifier could be checked: several Google Scholar items (*Feature-based algorithm selection for mixed integer programming*, 2018; *Speeding up energy system models – a best practice guide*, 2020; *Introduction to constraint integer programming*, 2014; *Extending SCIP for solving MIQCPs*, 2010; two BEAM-ME reports, 2020 and 2021; *SCIP8: rethinking nonlinear constraint representation and recent progress*, 2022). The Japanese RAMP 2012 paper on the SCIP Optimization Suite appears in S2/S3 (pp. 165–192) and is left out as marginal.

### 1.3 Topics by five-year period

| Period | Topics (works) | Position and context |
|---|---|---|
| 2004–2008 | Open-pit mine production scheduling by integer programming: UNSW honours project with Gary Froyland, then the Diplom thesis with Möhring (W1). [inferred] The UNSW collaboration surfaces as W2 (2009) | Student; DAAD study-abroad scholarship 2006, German National Merit Foundation 2005–2008 (S2 pp. 1, 6) |
| 2009–2013 | MINLP inside SCIP: MIQCP solver components (W5, W9), water supply networks (W8), mining MIQCPs (W6), the Undercover heuristic and covers (W3, W13), Lagrangian variable bounds (W12). LP accuracy: iterative refinement at ISSAC (W7) and a reduced-basis factorization (W10). Co-author of MIPLIB 2010 (W4); SCIP Optimization Suite reports (W11) | Research assistant at ZIB (2008–2015); co-chair of CPAIOR 2011 in Berlin (S1) |
| 2014–2018 | PhD thesis (W16) and its journal versions: iterative refinement for LP (W17), OBBT (W22). Verification: VIPR (W23). SCIP releases 3.2–6.0 (W19, W21, W24, W25), global MINLP in SCIP (W26). Applications: wireless network design accuracy (W18), cycle detection in Markov processes (W27), SAP supply chains (W34), energy-system LPs (W20, W28), recursive circle packing by Dantzig–Wolfe (W36). Libraries: MIPLIB 2017 call (Nov 2016) and release (Nov 2018), QPLIB (W31). Chvátal's conjecture by exact IP (W50 v1, 2018). Dagstuhl 18081 (W29) | Head of the ZIB group Mathematical Optimization Methods from 2015 (S1, S2) |
| 2019–2023 | Exact LP theory (W33) and exact rational MIP (W48, W63, W72 preprint, W62). Students' MINLP relaxations (W37, W38, W39, W54, W55, W61). ML for MIP heuristics (W46, W57, W52). GPU domain propagation (W42, W43). Conflict analysis, including pseudo-Boolean reasoning with Jakob Nordström (W44, W45, W56). Presolve (W40, W58). Parallel interior point for energy LPs (W41, W51). SCIP 7.0/8.0 (W35, W49, W53). MIPLIB 2017 paper (W47). MIP Workshop 2023 competition (W64) | Professor at HTW Berlin from 2020 (S1); ZIB group head until 2023 (S1) |
| 2024–2026 | Certified and numerically safe solving: certified presolve (W65), certified propagation and dual proofs (W68), numerical correctness of B&B decisions (W71), delta debugging (W79), precision boosting (W72), exact mode in SCIP 10.0 (W76). Conflict analysis with cuts (W75). Branch-and-price and branch-and-cut applications (W66, W67, W73, W77, W83), timetabling (W74). Primal heuristics, including GPU (W70, W81). Clique probing (W78), distributed presolving (W80), sepsis diagnosis by Boolean algebra (W82) | Last author on nearly all papers |

[inferred] Two threads run through every period: (a) numerical trust (accuracy, then exactness, then certificates and correctness analysis: W7 → W17 → W23 → W33 → W48 → W63/W65/W68/W71/W72 → W76) and (b) solver components measured inside SCIP. Applications enter through ZIB partnerships (SAP, energy, biology, mining) and mostly appear once.

### 1.4 Author position: alphabetical early, students first later

Counts over DBLP articles and conference papers with 2–9 authors (S28; my classification by surname order):

| Period | Papers | Alphabetical order | Not alphabetical: Gleixner first / middle / last |
|---|---|---|---|
| 2009–2013 | 5 | 5 | 0 / 0 / 0 |
| 2014–2018 | 9 | 5 | 1 / 2 / 1 |
| 2019–2023 | 26 | 11 | 0 / 10 / 5 |
| 2024–2026 | 11 | 1 | 0 / 4 / 6 |

- [practice, P] Until 2017 his papers follow the alphabetical convention. His first-listed papers W7, W12, W17, W33, W36, W41 and W58 are all in alphabetical order, so the first slot there says nothing about contribution. Contribution-ordered first authorships are W22 (OBBT, 2017), the first-three block of MIPLIB 2017 (W47) and the SCIP 5.0/6.0 reports (W24, W25).
- [practice, P] From 2019 the student-first convention dominates. Gleixner is then last (W37, W38, W44, W71, W72, W79, W83) or inside an alphabetical senior block after the students (W42, W56, W65). [inferred] The real shift is from alphabetical peer papers (2009–2017) to student-led papers (2019 on), not a plain first-to-last move.
- [practice, P] His last first-listed paper is PaPILO (arXiv June 2022, IJOC Nov 2023), and that listing is alphabetical. DBLP and arXiv show no first-listed paper from 2024 on.

### 1.5 Collaboration network and students

DBLP co-author counts (papers with fewer than 10 authors, conference and journal versions of one title counted once; S28):

- **Exact-arithmetic partner:** Daniel E. Steffy (Oakland University), 4 papers, 2012–2019 (W7, W17, W23, W33); thanked again for discussions in 2021 (S8 p. 12). Kati Wolter (2 papers; exact SCIP). Kevin K. H. Cheung (Carleton; W23).
- **ZIB peers, 2008–2015:** Timo Berthold (6 papers, 2013–2024), Stefan Vigerske (3), Thorsten Koch (3; reviewer of Gleixner's thesis, S4 title page, and formal TU Berlin advisor of Eifler, S35), Stefan Heinz, Stefan Weltge (2), Gerald Gamrath and Gregor Hendel (MIPLIB 2017; Hendel's Ipet tool is thanked in S4 p. iii and S6 p. 8).
- **Juniors who lead papers with him** (first-listed junior with Gleixner last or senior; supervision [inferred] except Eifler): Leon Eifler (7, 2016–2025), Alexander Hoen (6, 2023–2026), Jakob Witzig (5, 2016–2025), Benjamin Müller (5, 2017–2020), Antonia Chmiela (4, 2021–2023), Mohammed Ghannam (4, 2023–2026), Gioni Mexi (4, 2023–2026), Ksenia Bestuzheva (3, 2023–2025), Felipe Serrano (3, 2020), Boro Sofranac (2021–2022). Single papers: Dominik Kamp, Jules Nicolas-Thouvenin, Kilian Runnwerth, Patricia Ebert, Sander Borst, Jacob von Holly-Ponientzietz, João Dionísio, Nils-Christian Kempke, Gennesaret Tjusila, Tobias Weber.
- **Verified formal role:** Leon Eifler, *Algorithms and certificates for exact Mixed Integer Programming*, PhD TU Berlin 2025 (accepted 2024-11-08): advisor Thorsten Koch; referees Koch, Gleixner, Stefano Coniglio, Timo Berthold (S35). [inferred] Students in his ZIB group took their doctorates at TU Berlin under Koch, with Gleixner as day-to-day lead. Agent 04 checks the other theses.
- **Senior collaborators after 2019:** Sebastian Pokutta (5, 2020–2023, plus W81 in 2026; ML and GPU), Andrea Lodi (3, 2020–2021; also on his PhD committee, S4 title page), Jakob Nordström (3, 2021–2024, plus W75; pseudo-Boolean proof logging and conflict-driven search), Elias B. Khalil (W46, W52), Tobias Achterberg (W55; MIPLIB 2010/2017), Edward Lam (W67, W83), Dieter Weninger (W40, W70).
- **Application partners:** Marcus Weber and Konstantin Fackeldey at ZIB (Markov processes 2016–2018, then sepsis 2026), Fabio D'Andreagiovanni (wireless), João Pedro Pedroso (circle packing 2017–2020; scheduling 2025), Gary Froyland and Natashia Boland (mining), the BEAM-ME energy consortium, and SAP staff (W34).

### 1.6 Usual venues

- [practice, P] DBLP articles and conference papers: Math. Program. Comput. 6, Math. Program. 5, INFORMS J. Comput. 5 (6 with W75, not yet in DBLP), IPCO 5, Operations Research Proceedings 4, CPAIOR 3; two each in ISCO, J. Glob. Optim., Optim. Methods Softw., EURO J. Comput. Optim., SIAM J. Optim., CP, Constraints and ACM TOMS (S28).
- [practice, P] He has been a Technical Editor of Mathematical Programming Computation since 2015 (S2 p. 7). MPC is his most frequent venue.
- [inferred] He publishes in the home venue of the community whose tool he borrows: ISSAC (symbolic and algebraic computation) for iterative refinement (W7), CP and Constraints for pseudo-Boolean conflict reasoning (W43, W45, W56), an SC workshop and Parallel Computing for GPU propagation (W42), NeurIPS for learned heuristic scheduling (W46).

### 1.7 Most cited

Google Scholar counts from the WebFetch rendering of 2026-11-08 (S30); Crossref "is-referenced-by" counts from the same day (S31) where a DOI exists.

| Rank | Work | GS | Crossref | His position |
|---|---|---|---|---|
| 1 | MIPLIB 2010 (W4) | 589 | 299 | 9th of 16 |
| 2 | MIPLIB 2017 (W47) | 531 | 182 | first (contribution) |
| 3 | SCIP Optimization Suite 5.0 (W24) | 429 | — | first (coordinator, inferred) |
| 4 | SCIP Optimization Suite 8.0 (W49) | 417 | — | alphabetical block |
| 5 | SCIP Optimization Suite 7.0 (W35) | 337 | — | alphabetical block |
| 6 | SCIP global MINLP, OMS 2018 (W26) | 323 | 161 | second of 2 |
| 7 | SCIP Optimization Suite 9.0 (W69) | 278 | — | alphabetical block |
| 8 | Open-pit mining, C&OR 2009 (W2) | 259 | 127 | alphabetical |
| 9 | QPLIB (W31) | 176 | 80 | alphabetical block |
| 10 | SCIP Optimization Suite 3.2 (W19) | 152 | — | alphabetical block |
| 11 | OBBT, JOGO 2017 (W22) | 146 | 81 | first (contribution) |
| 12 | Learning to schedule heuristics (W46) | 129 | — | middle |
| 13 | Iterative refinement for LP, IJOC 2016 (W17) | 125 | 42 | alphabetical |
| 14 | SCIP Optimization Suite 4.0 (W21) | 124 | — | alphabetical block |
| — | ISSAC 2012 (W7) / VIPR (W23) / exact MIP status update (W48) / LP oracles (W33) | 70 / 69 / 60 / 35 | 24 / 25 / 17+2 / 14+0 | — |

[inferred] Nine of his ten most cited items are community infrastructure (instance libraries, SCIP release reports, SCIP's MINLP paper). His own technical lines (OBBT, iterative refinement, VIPR, exact MIP) sit at 35–146 GS citations.

### 1.8 Recent works and latest traces (last 12 months: Nov 2025 – Nov 2026)

- SCIP Optimization Suite 10.0 (W76, Nov 2025): the abstract lists a new solving mode for exact rational MILP and MIP-DD, the first open-source delta debugger for MIP solvers [stated, joint, P, S23]. [inferred] This closes the agenda his homepage announces, to extend SCIP into a numerically exact MIP solver (S1).
- Published: cut-based conflict analysis (W75, IJOC, Nov 2025); MIP-DD (W79, IJOC 38(2), 2026).
- Preprints: production-maintenance branch-and-price (W77), clique probing (W78), distributed structure-aware presolving (W80, latest version Oct 2026), CHAP GPU–CPU heuristic portfolio tested on the 50-instance 2026 Land-Doig MIP Competition benchmark under its five-minute limit (W81; per its abstract it finds solutions to 47 instances, Gurobi default 44, cuOpt heuristics-only 43; S24), sepsis diagnosis by Boolean polynomial rings (W82), numerically safe branch-price-and-cut for LCCP (W83, July 2026).
- Newest arXiv record: 2607.15837 (17 July 2026). Homepage footer © 2008–2022 (S1).

---

## 2. Signature works (framework §五)

Chosen as: his most cited work as contribution-ordered first author (SW4), the thesis core and his own priority on the homepage (SW1), his most cited first-authored algorithmic paper (SW2), the turning point from accuracy to verifiability (SW3), and the current agenda run with students (SW5). Candidate methods CM1–CM8 are defined in §4.

### SW1 · LP iterative refinement (W7 ISSAC 2012 → W16 thesis ch. 2–3 → W17 IJOC 2016; theory W33 MP 2020)

- **Origin.** [stated, P] Thesis p. iii credits Dan Steffy with the initiative to study iterative refinement using SoPlex. Thesis pp. 1–2: two motivations. First, in MINLP solvers numerical trouble often appears in the LP relaxations, so LP accuracy is a necessary step. Second, multiscale ME models of bacterial growth defeat double-precision LP solvers, which can fail even to decide feasibility; Ali Ebrahim supplied the instances (p. iii).
- **Why then.** [inferred, basis: thesis §3.1, pp. 57–64] QSopt_ex had made exact LP practical by incremental precision boosting; ZIB owned SoPlex, a simplex code that returns bases and hot-starts; the exact rational SCIP (Cook, Koch, Steffy, Wolter, 2013, cited in S8) needed fast exact LP; the COBRA systems-biology community wanted accurate LPs (thesis p. 6).
- **Key insight.** [stated, P] Thesis p. 3: carry Wilkinson's iterative refinement for linear systems over to LP, correcting primal and dual violations at once. The expensive part (a sequence of related LPs) runs in fast floating point; the cheap part (residuals and corrections) runs in exact rational arithmetic. Thesis p. 55: geometrically, each round zooms further into the region around the refined solution.
- **Minimum evidence.** [practice, P] Thesis pp. 64–65, §3.2.1 (A First Experiment): warm-start QSopt_ex from the refined basis, which needs only two existing libraries linked together. To avoid a biased comparison, the reference is QSopt_ex warm-started from SoPlex's unrefined basis, not plain QSopt_ex (p. 64). On the 23 instances where refinement changed the final basis, total time fell to 18% on average (factor 5.5; p. 65). Thesis p. 3: precision 10^-50 costs only 3% (easy) and 7% (hard) average slowdown against a standard 10^-9 floating-point solve.
- **Abandoned paths and limits.** [stated, P] Iterative refinement breaks down when the LP is too ill-conditioned for the floating-point solver (p. 55); 7 of 1,202 LPs failed this way, and QSopt_ex solved 6 of them (p. 89). Two proposed fixes (pp. 88–89): (a) run the rational factorization in a background thread while reconstruction continues (no later record found in this run); (b) integrate precision boosting into the refinement loop. [practice, P] (b) was carried out eight years later by Eifler, Nicolas-Thouvenin and Gleixner (W72, arXiv Nov 2023, IJOC 2025; S18 abstract). [practice] The ISSAC version covered only primal and dual feasible LPs solved by simplex (thesis p. 5).
- **Reception.** [observed, S] GS 125 (W17) and 70 (W7); Crossref 42 and 24. [stated, P] SoPlex became a standard plug-in of the COBRApy package, and NEOS offered SoPlex with 80-bit precision and exact extensions (thesis p. 6). [practice, P] The theory came afterwards: W33's abstract says it gives a foundation for understanding the methods that work best in practice for exact LP (S7 p. 1). Extension to QP: W32.
- **Era and resources.** 2011–2015; ZIB cluster of Xeon `X5672` at 3.2 GHz with 48 GB, one job per node; GMP rationals; QSopt_ex 2.5.10 as baseline; 1,202 public LPs from Netlib, Mittelmann, Mészáros, COR@L and MIPLIB relaxations, 40 excluded for memory or time with a bias argument (thesis pp. 10, 13–14).
- **Stated research stance.** [stated, P] Thesis p. 10: his experiments aim less at competitive testing than to "analyze the reasons for their behavior by controlled scientific testing" (citing Hooker 1995).
- **Methods it shows.** CM1, CM2, CM3, CM5.

### SW2 · Three enhancements for optimization-based bound tightening (W22 JOGO 2017; W12 CPAIOR 2013; thesis ch. 6)

- **Origin.** [stated, P] Thesis pp. 3, 5: OBBT is effective but expensive; the goal is to approximate it cheaply. [practice, P] Talks titled *Rapid optimality-based bound tightening* at FRICO and ISMP 2012, and *Lagrangian Variable Bounds or: how to profit from redundancy in MINLP* in 2013 (S2 p. 5). Implementation in SCIP by Müller and Weltge (thesis p. iii).
- **Why then.** [inferred, basis: thesis pp. iii, 174] Vigerske had turned SCIP into an MINLP solver, and MINLPLib2 offered a large heterogeneous benchmark.
- **Key insight.** [stated, P] Thesis pp. 3, 5, 173–174: the optimality proofs of the OBBT auxiliary LPs yield one-row relaxations, which he names Lagrangian variable bounds, that propagate repeatedly at almost no cost, a cheap stand-in for iterated OBBT. Plus filtering of bounds and ordering of LP solves.
- **Minimum evidence.** [practice, P] Thesis pp. 147–148: on instances solved with and without OBBT, average time drops 6.5% (continuous) and 2.3% (integer); on instances taking at least 100 s, 17.1% and 18.8%; 16 more instances solved, 3 lost.
- **Abandoned paths and negative results.** [stated, P] Thesis p. 148: OBBT alone gives no significant average speedup, because the nodes saved are paid for by root-node LP time. Only the LVB propagation makes it significant.
- **Reception.** [observed, S] GS 146; Crossref 81.
- **Era.** MINLPLib2; Wilcoxon signed-rank tests on paired shifted runtimes (thesis pp. 11–12).
- **Methods it shows.** CM2, CM3, CM6.

### SW3 · Verifying Integer Programming Results — VIPR (W23 IPCO 2017; ZIB-Report 16-58)

- **Origin.** [stated, joint, P] S6 pp. 1–2: MIP solvers occasionally return wrong answers, and even exact solvers can contain implementation errors. Two applications drove the work: Achterberg's MIP models for circuit design verification and Pulaj's MIP work on Frankl's conjecture; the software was used on both. The authors frame the motive as raising confidence, not as distrust of solvers (p. 1).
- **Why then.** [inferred, basis: S6 pp. 1–2] An exact rational SCIP existed and could be instrumented; the SAT community already checked unsatisfiability proofs, which the paper names as its analogue (p. 2); his exact SoPlex supplied the LP side.
- **Key insight.** [stated, joint, P] S6 p. 2: a certificate is a list of statements, each checkable by a few inference rules, in the style of natural deduction, and independent of how it was produced. It is simple enough that others can write their own checker without knowing MIP algorithms.
- **Minimum evidence.** [practice, P] S6 pp. 7–8, Table 1: 107 instances from the exact-SCIP test sets on Xeon E5-2660 v3 nodes run exclusively. Checking takes far less time than solving; the tightening tool shrinks certificates, most extremely on markshare1_1 from 10 GB to 8 kB.
- **Abandoned paths and limits.** [practice, P] S6 p. 8: 5 easy and 12 hard instances hit the 10 GB certificate limit; the certificate-producing solver is slower because only two of its dual-bounding methods can print certificates; file output costs about 7% of solving time. Future work named on p. 8: certificates in floating point via directed rounding; approximate certificates for debugging solvers or measuring numerical violations; formal checking with HOL Light. [inferred] The debugging and measuring idea returns in W71 (2025) and W79 (2026); no HOL Light follow-up was found in this run.
- **Reception.** [observed, S] GS 69; Crossref 25. [practice, P] Follow-ups: W50 (Chvátal, with Coq-checked input), W48 (certificates for all dual-bounding methods), W62 (proof system for symmetry handling, cuts and presolve), W65 (certified presolve). [stated, P] His homepage names VIPR, together with making SCIP an exact MIP solver, as his most active work (S1, undated).
- **Era.** 2016–2017, his second and third years as group head; MODAL funding; partners at Carleton and Oakland.
- **Methods it shows.** CM4, CM7.

### SW4 · MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library (W47, MPC 2021)

- **Origin.** [stated, P] His call of 11 Nov 2016 (S33): six years after MIPLIB 2010, solver and hardware progress had made many instances too easy and new challenges were needed; for the first time model files and data would be collected; submissions closed 28 Feb 2017; the initiative named ASU, COIN-OR, CPLEX, FICO, Gurobi, MIPCL, MOSEK, NuOPT, SAS and ZIB. [stated, joint, P] S5 p. 444: a committee of 21 researchers with representatives of nine MIP solvers steered the process.
- **Why then.** [stated, joint, P] S5 p. 444: on the MIPLIB 2010 benchmark, virtual best and worst of three commercial solvers sped up 2.70× and 3.62× from 2011 to December 2018, about 16% a year from algorithms alone. [inferred] A pool of 5,721 instances was too large to select by hand, as earlier editions had been (S5 p. 445).
- **Key insight.** [stated, joint, P] S5 pp. 445, 484–485: write the selection itself as MIP models that pick a balanced, diverse set across several clusterings of a feature space with more than 100 dimensions, plus performance requirements. The paper presents the process as its main new feature and as a gain in transparency.
- **Minimum evidence.** [stated, joint, P] S5 p. 485: comparing the clusters with manually assigned model groups from submitters' metadata shows the feature space describes the instances well.
- **Abandoned paths and failures.** [practice, P] S5 pp. 464–465: the old checker tolerance proved too strict for large coefficients, so a new mixed absolute and relative violation rule was introduced; 328 instances (5%) with inconsistent results across solvers were excluded from benchmark selection. S5 p. 485: two benchmark instances with numerical problems slipped through and a variant of the selection MIP computed a minimal replacement (benchmark update, June 2019). [stated, joint, P] S5 pp. 445–446, 485: many manual and heuristic choices remain; the result is one of many justifiable outcomes, and the method is not offered as a general blueprint. S5 p. 445: average performance on the benchmark should not decide which solver to use for a given application.
- **Reception.** [observed, S] GS 531; Crossref 182. [practice, P] Received 25 Jul 2019, accepted 10 Sep 2020, online 7 Jan 2021 (S31); 68 originally open instances solved by the time of writing (S5 p. 486). Release signed by Gleixner, Hendel and Gamrath on 8 Nov 2018 (S34). [practice, P] His own later work benchmarks on it (W48, W68, W71, W75); W71 notes that the collection tags 193 instances as numerically problematic (S10 p. 2).
- **Era and resources.** Committee of 21; performance data from eight solvers; the work of the first, second, third, ninth and last authors (Gleixner, Hendel, Gamrath, Koch, Shinano) funded by MODAL (S5 p. 486).
- **Methods it shows.** CM8, CM3, CM4.

### SW5 · A computational status update for exact rational MIP (W48 IPCO 2021 / MP 2023) → SCIP 10.0 exact mode (W76)

- **Origin.** [stated, joint, P] S8 pp. 1–2: floating-point roundoff undermines the optimality promise of MIP solvers. This matters when MIP is used to prove mathematics (his own W50 did that), and in hardware verification and compiler optimization. The last milestone, the 2013 Cook–Koch–Steffy–Wolter hybrid-precision branch and bound, lacked presolve, primal heuristics and other components of fast floating-point solvers.
- **Why then.** [inferred, basis: S8 pp. 2, 12] The parts had just become available in-house: PaPILO's multiprecision presolve, SoPlex's refinement-based exact LP, VIPR certificates.
- **Key insight.** [stated, joint, P] S8 pp. 2–3: carry the hybrid-precision scheme into every component. Heuristics run on the floating-point copy and their solutions are repaired by an exact LP; presolve is symbolic; certificates cover all dual-bounding methods. The stated goal is SAT-level rigor with most of the floating-point speed kept, shown first on a small selection of methods.
- **Minimum evidence.** [practice, P] S8 abstract and p. 12: on the MIPLIB 2017 benchmark, 6.6× faster than the 2013 framework and 2.8 times as many instances solved in two hours; 30 more instances solved, mean time down 84.8% on instances solved by at least one version, primal solutions on 167 instead of 74 instances.
- **Abandoned paths and limits.** [stated, joint, P] S8 p. 12: the gap to floating-point solvers is still large, partly because safe cutting planes are missing. [practice, P] Bound-shift is switched off when its success rate falls below 20% (S8 p. 8). [practice, P] The next projects close the named gaps one by one: safe Gomory mixed-integer cuts (W63), certified propagation and dual proof analysis with a reported 23% speedup on MIPLIB 2017 (W68), precision boosting inside refinement (W72), and finally the exact solving mode in SCIP 10.0 (W76).
- **Reception.** [observed, S] GS 60; Crossref 17 (MP) and 2 (IPCO); MP received 31 May 2021, accepted 24 Nov 2021 (S31). [practice, P] Eifler's PhD (2025) is built on this line (S35).
- **Era.** First years at HTW Berlin; ZIB group with MODAL funding (BMBF 05M14ZAM, 05M20ZBM; S8 p. 1).
- **Methods it shows.** CM1, CM4, CM5.

---

## 3. Failures, abandoned directions, unwritten papers

| # | Item | Evidence | Tag |
|---|---|---|---|
| F1 | OBBT alone not significant; only the propagated Lagrangian variable bounds made it pay | S4 p. 148 | [stated] P |
| F2 | COVER branching (built on the minimum-cover concept from Undercover) improved time but failed significance and lost to the simpler NLSCORE rule; VARTYPE branching slowed instances that default SCIP also solved. He concludes the most effective rules were simple hybrid refinements of existing scores | S4 pp. 171–172, 174 | [stated] P |
| F3 | Iterative refinement fails on extremely ill-conditioned LPs (7 of 1,202), where precision boosting wins | S4 pp. 55, 89 | [stated] P; fixed in W72 [practice] |
| F4 | VIPR certificate files exceeded 10 GB on 17 of 107 instances; certificate mode slower | S6 p. 8 | [practice] P |
| F5 | MIPLIB 2017: two numerically problematic benchmark instances slipped through, so the benchmark was updated in June 2019; 328 inconsistent instances excluded; checker tolerance redesigned | S5 pp. 464–465, 485 | [practice] P |
| F6 | Exact MIP in 2021 still far behind floating-point solvers | S8 p. 12 | [stated, joint] P |
| F7 | Circle packing: arXiv v1 (Feb 2017) calls the method the first exact method for RCPP and its dual bounds exact; v2 (Jan 2019) and the journal title (*Price-and-verify*) say first dedicated method with strong dual bounds | S12 v1 vs v2 | [practice] P; reason not documented |
| F8 | Chvátal: arXiv v1 (Sep 2018) is titled as a theorem; v2 (Sep 2020) is reframed as a safe computational framework and adds a Coq check of the input. TOMS received Sep 2020, accepted Sep 2021. Whether an earlier submission was rejected is not documented | S13 v1 vs v2; S31 | [practice] P |
| F9 | LCCP branch and price (W67, Feb 2024) has no venue in DBLP; reworked into a numerically safe branch-price-and-cut preprint (W83, Jul 2026; arXiv notes text overlap). Closed instances: 13 → 14, the latter now with numerically safe bounds | S21, S26 | [practice] P; rework reason [inferred] |
| F10 | Preprints with no venue in DBLP as of 2026-11-08: W59, W60, W61 (long version), W62, W67, W68, W77, W78, W80–W83. Not evidence of rejection | S28, S29 | [practice] P |
| F11 | Lines that stop in the record: mining (last 2012), water networks (2012), wireless design (2016), Markov cycle detection (2018, but ZIB biology partners return in 2026), ML-scheduled heuristics (2021–2023; nothing in DBLP after), GPU propagation (2020–2022; GPU returns in 2026 via W81) | S28, S29 | [practice] P; "exit" [inferred] |
| F12 | Thesis proposal of a parallel hybrid of rational factorization and reconstruction: no later record found | S4 p. 88 | [stated] P; not found |
| F13 | Rejected papers, errata, retractions | none found | — |

---

## 4. Candidate methods surfaced by this dimension (for Phase 2 cross-checking)

Not yet validated; agents 02–03 and Phase 2 decide.

- **CM1 Mixed precision: heavy work in floating point, residuals, repairs and safe bounds in exact arithmetic.** W7/W17 (refinement), W48 (exact repair of heuristic solutions), W63 (safe cuts by directed rounding), W68 (safe propagation), W72 (precision boosting only when needed), W71 (exact checks of floating-point decisions). [practice] ×6, 2012–2025.
- **CM2 Build inside the production open-source solver and measure on broad public test sets.** The thesis sets this as the evaluation standard (S4 p. 2): implement in state-of-the-art solvers and test on heterogeneous, practice-relevant benchmarks. Archived versions and logs, one job per node (S4 p. 10); fair baselines (S4 p. 64). Every SW above ships in SoPlex, SCIP or PaPILO.
- **CM3 Explain, do not just rank.** Shifted geometric means on difficulty-filtered subsets plus one-sided Wilcoxon signed-rank tests; significance is kept apart from magnitude (S4 pp. 10–12); negative results are reported (F1, F2). MIPLIB 2017 warns against using benchmark averages to choose a solver (S5 p. 445).
- **CM4 Make results checkable by someone else.** Simple-rule certificates (W23), the cross-solver consistency check and exact solution checker of MIPLIB 2017 (S5 pp. 464–465), Coq-checked input (W50), a proof system (W62), certified presolve (W65), delta debugging, which per its abstract helped in 24 of 51 documented MIP bug fixes in SCIP 8.0.1–8.1.1 (W79, S19), a posteriori correctness analysis (W71).
- **CM5 Carry a paper's stated limitation into the next project, usually a student's.** Thesis §3.5 → W72; VIPR's future work → W71/W79; W48's missing safe cuts → W63; W67 → W83.
- **CM6 Reuse by-products the solver already computed.** Dual information of OBBT LPs as Lagrangian variable bounds (W12, W22); conflict analysis that learns from infeasibility (W44, W56, W75).
- **CM7 Import a mature neighbouring field's tool and publish where it lives.** Wilkinson refinement (numerical linear algebra) at ISSAC; SAT and pseudo-Boolean proof logging and conflict-driven search with Nordström at CP/Constraints (W45, W56, W65, W75); GPU kernels at an SC workshop (W42); learning at NeurIPS (W46).
- **CM8 Turn a community curation decision into a transparent optimization model and document the arbitrary choices.** MIPLIB 2017 selection MIPs and the June 2019 minimal update (S5 pp. 445–446, 485).

---

## 5. Era and resource context

| Period | Position | Resources and setting | Source |
|---|---|---|---|
| Mid-2000s | Student at Bayreuth (Vordiplom 2004), UNSW honours year (year garbled in the CV layout; [inferred] around 2005–2006, with the 2006 DAAD scholarship), TU Berlin Diplom 2008; Siemens internships (one on wireless network planning) | Scholarships; mining problem from UNSW | S1, S2 pp. 1, 6; S4 p. iv |
| 2008–2015 | Research assistant, ZIB Department of Optimization | Matheon (DFG) 2008–2014, Berlin Mathematical School 2007–2015, MODAL from 2014, COST TD1207; ZIB cluster, one job per node; SoPlex and SCIP maintained in-house; student assistants | S1, S2, S4 pp. iii–iv, 10 |
| 2015–2023 | Head of ZIB group Mathematical Optimization Methods; in 2017, 2 senior researchers, 10 research assistants and 4 student assistants | MODAL grants 05M14ZAM and 05M20ZBM; BMWi BEAM-ME (PI of ZIB sub-project); SAP and Siemens projects (PI); MPC technical editor from 2015 | S1, S2 p. 1, p. 6; S5 p. 486; S8 p. 1 |
| 2016–2021 | MIPLIB 2017 lead | Committee of 21 with nine solver teams; eight solvers for performance data | S5 pp. 444–445 |
| 2020– | Professor at HTW Berlin; affiliated researcher at ZIB (Mathematical Algorithmic Intelligence) | Students take PhDs at TU Berlin (Eifler: advisor Koch, Gleixner referee); GPU work (cuPDLPx, GPU tabu search) in 2026 | S1, S35, S24 |

---

## Contradictions

Kept as found; not reconciled.

- **C1 PaPILO author order and credit.** arXiv metadata, DBLP and IJOC list Gleixner, Gottwald, Hoen (alphabetical); the header of arXiv v3 (Mar 2024) reads Gleixner, Hoen, Gottwald (S9 p. 1). The IJOC title reads Integer and Linear Optimization, the arXiv title Integer and Linear Programming. His own 2021 co-signed paper credits Gottwald with creating PaPILO (S8 p. 12), while he is first author.
- **C2 Agenda versus measurement.** The exactness agenda says roundoff compromises the optimality promise of floating-point MIP (S8 p. 1). His 2025 study with Hoen finds that in the overwhelming majority of cases every branch-and-bound decision is exactly correct, and that errors touch only a few leaves (S10 abstract).
- **C3 Speed versus robustness.** The thesis claims exact SoPlex is 1.85–3 times faster than QSopt_ex (S4 pp. 3, 88). The same thesis says precision boosting handles extremely ill-conditioned LPs where refinement fails (S4 pp. 88–89).
- **C4 Circle packing claims** v1 vs final (F7): v1 calls the method exact, with exact dual bounds; the final version calls it dedicated, with strong dual bounds.
- **C5 Chvátal framing** v1 vs v2 (F8): a theorem paper vs a framework paper.
- **C6 Citation counts differ by source.** MIPLIB 2017: GS 531 vs Crossref 182; IJOC 2016: 125 vs 42 (S30, S31). Coverage differences; no third source (Semantic Scholar failed).
- **C7 SCIP 10.0 author list.** The citation block on scipopt.org (28 names; S32) includes Chmiela, who is absent from arXiv 2511.18580; arXiv (34 names; S23) adds Ehls, Lübbecke, Meinhold, Mohr, Patel, Reinartz Groba and von Holly-Ponientzietz.
- **C8 Dates.** J. Comput. Math. 37(6) is a 2019 issue (GS gives 2019) while Crossref's published date for W34 is 2021-07-01 (S31). W36 is online in Dec 2018, in an issue dated 2020.
- **C9 Homepage dating.** The CV block gives the ZIB group headship as 2015–2023, while the footer reads © 2008–2022 (S1). The homepage statement that VIPR is his most active work is therefore undated.

---

## Gaps

- Semantic Scholar API: HTTP 429 on both attempts; no S2 counts or influential-citation data.
- OpenAlex: not used (no `OPENALEX_API_KEY`).
- ZIB OPUS (opus4.kobv.de): behind an Anubis proof-of-work bot wall; not bypassed. ZIB-Report URNs from the CV were not resolved, and report-only items listed by Google Scholar could not be verified (§1.2, last paragraph).
- Google Scholar rendering via WebFetch gave titles, years and counts only; author and venue lines were not captured; the SCIP Optimization Suite 6.0 report (first author per S32) did not appear in the rendering. Possibly a rendering omission; not checked.
- Not read: W7, W17 and W22 as published (the thesis was used instead); MIPLIB 2010; the SCIP release reports; full texts of W63, W72, W75, W76, W79 and W50; the ML papers.
- No interview or talk explaining why he took the MIPLIB 2017 lead or the exact-MIP agenda. The CV lists 57 talks to 2016, but no slides were read and nothing was saved to `talks/`.
- No public record of rejected submissions; the reasons for the v1 → v2 changes in W36 and W50 are not documented.
- Awards and prizes: the one WebSearch call found none linked to him or to MIPLIB 2017 (S27). One search is not conclusive.
- Google Scholar counts were read off a WebFetch summary of the profile page; transcription errors by the summarizer are possible and only the DOI'd works were cross-checked (Crossref, S31).
- Formal supervision verified only for Eifler (S35). Other students are inferred from co-authorship (agent 04).
- Code (scipopt/soplex, scipopt/scip exact-rational branch, scipopt/VIPR) was not inspected (agent 03).

---

## Sources

Primary:
- S1 Ambros Gleixner, homepage (projects, short CV, publications), www.zib.de/userpage/gleixner/ (footer © 2008–2022; fetched 2026-11-08) — primary
- S2 Ambros Gleixner, *Curriculum Vitae of Ambros Gleixner*, updated 31 July 2017, www.zib.de/userpage/gleixner/gleixner.pdf — primary
- S3 Ambros Gleixner, BibTeX file of publications 2008–2014, www.zib.de/userpage/gleixner/gleixner.bib — primary
- S4 A. M. Gleixner, *Exact and fast algorithms for mixed-integer nonlinear programming*, PhD thesis, TU Berlin, 2015, DOI 10.14279/depositonce-4938 (PDF via depositonce.tu-berlin.de) — primary
- S5 A. Gleixner, G. Hendel, G. Gamrath et al., *MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library*, Math. Program. Comput. 13 (2021) 443–490, DOI 10.1007/s12532-020-00194-3 (open-access PDF, CC BY 4.0) — primary
- S6 K. K. H. Cheung, A. Gleixner, D. E. Steffy, *Verifying Integer Programming Results*, ZIB-Report 16-58 (revised March 2017), arXiv 1611.08832v2 — primary
- S7 A. Gleixner, D. E. Steffy, *Linear Programming using Limited-Precision Oracles*, ZIB-Report 19-57 (Nov 2019), arXiv 1912.12820v1 — primary
- S8 L. Eifler, A. Gleixner, *A Computational Status Update for Exact Rational Mixed Integer Programming*, ZIB-Report 21-04 (Jan 2021), arXiv 2101.09141v1 — primary
- S9 A. Gleixner, A. Hoen, L. Gottwald (header order of v3), *PaPILO: A Parallel Presolving Library for Integer and Linear Programming with Multiprecision Support*, arXiv 2206.10709v3, 20 Mar 2024 — primary
- S10 A. Hoen, A. Gleixner, *Analyzing the numerical correctness of branch-and-bound decisions for mixed-integer programming*, arXiv 2412.14710v3, 3 Apr 2025 — primary
- S11 S. Serrano, R. Schwarz, A. Gleixner, *On the Relation between the Extended Supporting Hyperplane Algorithm and Kelley's Cutting Plane Algorithm*, arXiv 1905.08157 abstract page, May 2019 — primary
- S12 A. Gleixner, S. Maher, B. Müller, J. P. Pedroso, *Exact Methods for Recursive Circle Packing*, arXiv 1702.07799 abstract pages v1 (Feb 2017) and v2 (Jan 2019) — primary
- S13 L. Eifler, A. Gleixner, J. Pulaj, arXiv 1809.01572 abstract pages v1 (*Chvátal's Conjecture Holds for Ground Sets of Seven Elements*, Sep 2018) and v2 (Sep 2020) — primary
- S14 L. Eifler, A. Gleixner, *Safe and Verified Gomory Mixed Integer Cuts in a Rational MIP Framework*, arXiv 2303.12365 abstract page, v1–v3 2023 — primary
- S15 G. Mexi et al., *Scylla: a matrix-free fix-propagate-and-project heuristic for mixed-integer optimization*, arXiv 2307.03466 abstract page, July 2023 — primary
- S16 M. Ghannam, A. Gleixner, *Hybrid Genetic Search for Dynamic Vehicle Routing with Time Windows*, arXiv 2307.11800 abstract page, July 2023 — primary
- S17 J. van Doornmalen, L. Eifler, A. Gleixner, C. Hojny, *A proof system for certifying symmetry and optimality reasoning in integer programming*, arXiv 2311.03877 abstract page, Nov 2023 — primary
- S18 L. Eifler, J. Nicolas-Thouvenin, A. Gleixner, *Combining Precision Boosting with LP Iterative Refinement for Exact Linear Optimization*, arXiv 2311.08037 abstract page, Nov 2023 — primary
- S19 A. Hoen, D. Kamp, A. Gleixner, *MIP-DD: A Delta Debugger for Mixed Integer Programming Solvers*, arXiv 2405.19770 abstract page, v1–v5 2024–2025 — primary
- S20 G. Mexi, F. Serrano, T. Berthold, A. Gleixner, J. Nordström, *Cut-based Conflict Analysis in Mixed Integer Programming*, arXiv 2410.15110 abstract pages v1 (Oct 2024) and v2 (Oct 2025) — primary
- S21 M. Ghannam, G. Mexi, E. Lam, A. Gleixner, *Branch and Price for the Length-Constrained Cycle Partition Problem*, arXiv 2401.17937 abstract page, Feb 2024 — primary
- S22 S. Borst, L. Eifler, A. Gleixner, *Certified Constraint Propagation and Dual Proof Analysis in a Numerically Exact MIP Solver*, arXiv 2403.13567 abstract page, Mar 2024 — primary
- S23 C. Hojny et al., *The SCIP Optimization Suite 10.0*, arXiv 2511.18580 abstract page and author metadata, Nov 2025 — primary
- S24 G. K. Tjusila et al., *CHAP: A Hybrid GPU-CPU Heuristic for MIP*, arXiv 2605.05086 abstract page, May 2026 — primary
- S25 M. Weber et al., *Boolean Algebra -- Driven Sepsis Diagnosis*, arXiv 2605.29686 abstract page, May 2026 — primary
- S26 M. Ghannam, A. Gleixner, G. Mexi, E. Lam, *A Numerically-safe Branch-Price-and-Cut Algorithm for the Length-Constrained Cycle Partition Problem*, arXiv 2607.15837 abstract page, July 2026 — primary
- S32 SCIP project, citation block with all SCIP Optimization Suite release reports 3.2–10.0, www.scipopt.org/index.php (fetched 2026-11-08) — primary
- S33 A. Gleixner, *MIPLIB 2017: Call for Contributions to the 6th Mixed Integer Programming LIBrary*, Opt-Net mailing list, 11 Nov 2016, listserv.zib.de/pipermail/opt-net/2016-November/001275.html — primary
- S34 A. Gleixner, G. Hendel, G. Gamrath, *MIPLIB 2017: Official release of the new Mixed-Integer Programming LIBrary, version 6*, Opt-Net, 8 Nov 2018, listserv.zib.de/pipermail/opt-net/2018-November/001665.html — primary
- S35 DepositOnce record of L. Eifler, *Algorithms and certificates for exact Mixed Integer Programming*, PhD thesis, TU Berlin, 2025 (advisor and referee metadata), DOI 10.14279/depositonce-23941 — primary

Secondary:
- S27 WebSearch result list (1 query on prizes and MIPLIB 2017, 2026-11-08): no award found; it supplied the links to S33 and S34 — secondary
- S28 DBLP SPARQL endpoint (sparql.dblp.org), person pid 07/3479, 74 records, via `scripts/dblp_works.py`, 2026-11-08 — secondary
- S29 arXiv author search "Gleixner, Ambros", 48 results, arxiv.org/search (fetched 2026-11-08) — secondary
- S30 Google Scholar profile DUFnBNcAAAAJ (pages 1–2), scholar.google.com/citations?user=DUFnBNcAAAAJ, via WebFetch 2026-11-08 — secondary
- S31 Crossref REST API (api.crossref.org/works) metadata for 25 DOIs, 2026-11-08 — secondary

---

## Update 2026-11-28 (full-text pass, T3.6): coverage from the Google Scholar list

The publication list is complete at the level of the Google Scholar profile, and every work outside the skip rows now has a paper card. Sources: `../sources/publications/scholar.md` (the profile https://scholar.google.com/citations?user=DUFnBNcAAAAJ, harvested and audited 2026-11-26, cross-checked with DBLP 07/3479, Crossref, arXiv, ZIB OPUS and the homepage; machine-readable in `works.json`), the full-text index `../sources/papers/INDEX.md`, the paper cards indexed in `07-paper-cards.md` and the synthesis `08-deep-reading-synthesis.md`. Citations like [S022 p. 17] point to a card and the page of the file it read, often a report or arXiv version even without a version word (the card key of `09-evidence-ledger.md` names the file); a version word (TR, arXiv, report, draft) marks cards always cited with their version. The sections above stay as the web-research record of 2026-11-08; where the full texts change them, this section says so. The sealed passages named in `holdout.md` are not restated here.

### Coverage

| Item | Count | Note |
|---|---|---|
| Google Scholar rows | 107 | one-to-one with the S rows of `works.json` (`scholar.md`, audit 2026-11-26) |
| `works.json` entries | 116 | 107 Scholar (S), 7 DBLP, OPUS or arXiv only (D), 2 homepage only (H); 13 marked `dup_of` |
| Distinct works indexed | 103 | INDEX.md roles: core 60, supplement 40, skip 3 |
| Open full texts | 92 | `txt` in INDEX.md (Source column: 44 arXiv, 40 `manual`, supplied by hand, 5 author or repository URLs, 3 Unpaywall); 11 `no-oa` |
| **Read in full / in part** | **90 / 2** | INDEX Read column: carded 90, skimmed 2 (S063, S064) |
| Abstract only | 6 | D001, S051, S056, S057, S077, S081 |
| Metadata only | 2 | S099, S101 |
| Skipped | 3 | S059 and S107 (talks), S088 (a junk Scholar row) |
| Card entries / works with a card | 103 / 101 | D005 and S022 carry an earlier abstract- or metadata-level card and a later full card (08 §1) |
| Card quotes verified | 197 | 197 exact (`verify_card_quotes.py`, 2026-11-28) |

The 100 works outside the skip rows, by kind and read depth (full / part / abstract / metadata): journal 36 (33 / 1 / 2 / 0); conference 34 (29 / 0 / 4 / 1); report 16 (15 / 1 / 0 / 0); preprint 10 (10 / 0 / 0 / 0); thesis 2 (2 / 0 / 0 / 0); other 2 (1 / 0 / 0 / 1).

Works with a card by period (08 §8): 2008–2012: 13 · 2013–2017: 13 · 2018–2022: 41 · 2023–2026: 33. He is first-listed (alphabetical bylines included) or sole author in 4, 5, 7 and 1 of them. Many cards read a ZIB-Report or arXiv version (among them S001, S013, S017, S020, S011, S029, S058, S067, S078, S082, S085, S015, S026, S060, S007, D002, D003, D005); only the exact-MIP status update was compared across versions [D002; S022] (08 §11).

### Leads of §0–§4 settled by the full texts

| Lead (section) | Resolution | Cards |
|---|---|---|
| Reading depth: ISSAC 2012, IJOC 2016 and JOGO 2017 not read as published | Read in their report versions [S020 TR; S013 TR] and in full [S011]; the 3% / 7% slowdowns and the 7 of 1,202 failures are in the journal report [S013 TR pp. 19–20] and the thesis, while ISSAC 2012 has its own smaller study [S020 TR pp. 9–10] (08 §3.2) | S020, S013, S011, S032 |
| Reading depth and Gaps: MIPLIB 2010 and the SCIP release reports not read | Read: MIPLIB 2010 [S001 TR], the Suite reports 3.2 to 10.0 [S010; S014; S003; D004; S005; S004; S007; S021] and the 8.0 journal paper [S015]; release reports credit him with named features [S010 p. 28; S003 p. 37; D004 p. 39; S004 p. 83; S007 p. 27; S021 p. 39] | Suite series |
| SW3 (VIPR) | Read in full in the revised ZIB-Report version: 107 instances, 17 runs at the 10 GB cap, 10 GB trimmed to 8 kB [S019 p. 10]; the version read cannot show whether an earlier one excluded an instance (S019 card) | S019 |
| SW4 (MIPLIB 2017) | Read in full [S002]. Three statements of SKILL.md corrected: instances are licensed CC BY-SA 4.0 by default [S002 p. 6] (CC BY 4.0 is the article's own [S002 p. 44]); the solution checker computes in GMP arithmetic but accepts by tolerances [S002 p. 22], objective values recomputed exactly [S002 p. 42]; the count of five exchanged instances is the changelog's, not the paper's [S002 pp. 43–44] | S002 |
| SW5 (exact MIP status update) | Both versions read [D002; S022]: the journal's quoted sentence is on printed p. 809 [S022 p. 17]; it opens with four questions, the IPCO version with three [S022 p. 8; D002 p. 8]; certificate overheads differ by version [D002 pp. 13–14; S022 p. 16] | D002, S022 |
| §1.4 Author position: alphabetical until 2017 | Alphabetical bylines appear before and after 2017 [S020 TR p. 3; S039 p. 3; S019 p. 3; S041 p. 3; S068 p. 3; S060 p. 1; S085 p. 1]; a non-alphabetical first-author byline in 2016/2017 [S011 pp. 1, 3]; release reports put the lead first and the rest alphabetically [S003 pp. 3, 41; S021 p. 1]: byline order is not a reliable signal of his role (08 §3.2) | as listed |
| Gaps: the ML papers and works from 2022 on not read | Read in full: the ML papers [S012; S016; S040; S069] and the exact, presolve, conflict-analysis, GPU and HTW-era papers of 2022–2026 (07 and 08 §8) | see 07 |
| §3 Unwritten papers: the background rational factorization and the MIPLIB hindsight study | Still not found: the factorization is proposed again in 2020 [S029 p. 25] and taken up in no later card; the hindsight study is not reported [S002 p. 43] (08 §11) | S029, S002 |

### Signature-work anatomies

SKILL.md now rests its four anatomies of §2 on the full texts where they exist and adds two works read in full: Gleixner and Steffy, *Linear programming using limited-precision oracles*, Math. Program. 183 (2020), DOI 10.1007/s10107-019-01444-6 [S029], and Hoen and Gleixner, *Analyzing the numerical correctness of branch-and-bound decisions for mixed-integer programming*, CPAIOR 2025, DOI 10.1007/978-3-031-95976-9_3 [S072]. Their rows and the earlier web-research versions are in `09-evidence-ledger.md` (`#anatomy-…` sections). In the T3.6 review fixes (2026-11-28) the oracle paper joined the iterative-refinement anatomy as its theory sequel, so SKILL.md has five anatomies. §2 above is kept as the web-research record.
