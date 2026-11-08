# 01 · Publications: landscape and signature-work anatomy

> **Researcher**: Ruth Misener (Imperial College London, Department of Computing; DBLP pid 04/8800; Google Scholar `AQxtWHoAAAAJ`; ORCID 0000-0001-5612-5417 as recorded by DBLP. The ORCID record itself was not opened.)
> **Dimension**: research agent 01 of 06, signature works and the publication landscape (nuwa research-craft Phase 1)
> **Research date**: 2026-10-10
> **Sources consulted**: 29, listed under "Sources" (18 primary, 11 secondary or observed). Four further sources could not be used:
> - OpenAlex: not run, because `OPENALEX_API_KEY` is not set.
> - Mittelmann's benchmark pages (plato.asu.edu): connection failed.
> - The APOGEE website (helios.princeton.edu): connection failed.
> - The Wayback Machine: HTTP 429.
>
> WebSearch calls used: 1 of 2.
> **Method**: the following sources and tools, in this run:
> - Lists and metadata: DBLP SPARQL (`scripts/dblp_works.py`); the Google Scholar profile (WebFetch, all 155 rows); her CV PDF (updated 3 December 2025, read in full); her homepage; the Crossref, Semantic Scholar and Unpaywall APIs; Springer article pages for abstracts and received/accepted dates; arXiv abstract pages and the arXiv author search.
> - Full texts, read in part (sections named in §2): author manuscripts of GloMIQO, the 2012 *Math. Program.* paper, ANTIGONE, APOGEE and JOTA 2010 from Imperial's Spiral repository; arXiv texts of the gradient-boosted-tree, ENTMOOT and OMLT papers; the GALINI preprint (Optimization Online); the Dagstuhl 18081 report.
> - Her own words: her 2016 essay on Floudas in *SIAG/OPT Views and News*; the auto-generated captions of her 2023 inaugural lecture, saved as `../sources/talks/2023-03-13-just-relax-inaugural-lecture-asr.md`.
> - Others: GAMS solver manuals and release notes; the cog-imperial GitHub organisation; one independent solver comparison (Kronqvist et al. 2019).
>
> No user-supplied material existed in `references/sources/`, only `.gitkeep` files and `RESOURCES.md`. `references/sources/private/` was not opened.
> **Tags**:
> - [stated]: what Misener said or wrote about her own work.
> - [practice]: what the record shows she did (papers, code, CV entries, author lists, version histories).
> - [observed]: what others wrote or said.
> - [inferred]: my reading, with no primary source for it.
>
> Items also say primary or secondary where it matters. In the paper lists of §1.2, every item is [practice, primary] unless tagged otherwise.
> **Quoting**: quotations are verbatim, with three exceptions:
> - PDF text extraction dropped some glyphs (the α in αBB, Mišić's diacritics, curly apostrophes, £) and split words at line-break hyphens. I restored only those.
> - Quotes marked **[ASR captions]** come from YouTube's machine captions of the 2023 lecture. They match the caption track word for word, but the captions may not match the speech exactly. Misrecognised words inside such quotes are flagged [sic, ASR], and the transcript header resolves them.
> - "[sic]" alone marks a typo in the original paper.

---

## 0. Identity and data hygiene (read this before reusing any count)

- **DBLP has no namesake contamination.** DBLP 04/8800 holds 93 records from 2010 to 2026: 40 articles, 18 proceedings papers and 35 CoRR/informal records. I merged CoRR duplicates into their published versions and dropped one reprint. That leaves 72 distinct works, all of which fit her topics and co-author network. [practice, secondary]
- **DBLP is incomplete for her early chemical-engineering output.** It misses:
  - the 2009 *Ind. Eng. Chem. Res.* papers;
  - both *Applied and Computational Mathematics* papers (2009, 2012);
  - the *AIChE J.* papers;
  - most chemical-engineering conference proceedings.

  **Her CV is the most complete list** [stated, primary]:

  | CV block | Count |
  |---|---|
  | Peer-reviewed journal papers (J01–J65) | 65 |
  | Computer-science conference papers (C01–C16) | 16 |
  | Engineering conference papers (E01–E27) | 27 |
  | Workshop papers (W01–W04) | 4 |
  | Software "primarily written by me" (S01–S03) | 3 |
  | Mathematical models (M01–M02) | 2 |
- **The CV is not complete either.** [practice, primary]
  - It omits Kronqvist, Misener and Tsay, "P-split formulations…", *Math. Program.* 218(1–2):57–94 (online 9 June 2025, DOI 10.1007/s10107-025-02232-1).
  - It predates the ICLR 2026 paper.
  - Two works with many citations appear in the CV only as **talk titles**, never as papers: the neural-network-scored SDP cuts (seminars S23 and S26) and the general GALINI solver (talk I31). See §1.9.
- **Google Scholar** (fetched 2026-10-10) shows 155 rows, 6,188 citations, h-index 36 and i10-index 76 (since 2021: 3,783 / 30 / 63). [practice, secondary] The row count overcounts papers. The rows include:
  - conference abstracts (*Blood*, *J. Tissue Eng. Regen. Med.*);
  - technical reports for the GloMIQO 2.2 and ANTIGONE 1.0 test suites;
  - a newsletter issue;
  - duplicate preprints;
  - one student's Master's thesis (Suraj G, 2019).
- **arXiv** lists 46 preprints. The earliest is 1511.05385 (November 2015). None of the GloMIQO/ANTIGONE-era papers are on arXiv; their author versions sit in Imperial's Spiral repository. From 2017 on, almost every paper has an arXiv version. [practice, secondary]
- **OpenAlex was not used**, because `OPENALEX_API_KEY` is not set, as the task specified. Semantic Scholar was used only for per-paper citation counts; its author search returned no usable record.

---

## 1. Publication landscape

### 1.1 Career and resource context (the frame for every practice below)

| Period | Position | Resources and context | Evidence |
|---|---|---|---|
| 2003–2007 | BS Chemical Engineering, MIT | Robert C. Byrd Honors Scholarship | CV [stated, primary] |
| 2007–2012 | PhD Chemical Engineering, Princeton, advised by Christodoulos A. Floudas. Thesis: "Novel Global Optimization Methods: Theoretical & Computational Studies on Pooling Problems with Environmental Constraints" (2012; **not read**) | Funding: NSF Graduate Research Fellowship (DGE-0646086) and Floudas's NSF grant CBET-0827907 (paper acknowledgments). Tools: C++, CPLEX 11.1–12.4, SNOPT 5.3, LAPACK, and GAMS via the GAMS Modeling Object API, with linking code adapted from COIN-OR GAMSLinks. Hardware: one Linux workstation with "one Intel Core 2 Quad processor with four 2.83 GHz cores and 4 GB of RAM associated with each processor" (GloMIQO manuscript §4). GAMS, Sahinidis (BARON) and Schrage (LindoGLOBAL) gave the competitor licences free | CV; GloMIQO and MP-B manuscripts [stated/practice, primary] |
| 2012–2014 | Royal Academy of Engineering Research Fellow, Centre for Process Systems Engineering (Chemical Engineering), Imperial | RAEng Research Fellowship 2012–2017, £539k; she declined an Imperial Junior Research Fellowship. ANTIGONE was benchmarked "running 64 bit Linux on an Intel Xeon X5650 2.67 GHz processor with 24 GB RAM". GloMIQO and ANTIGONE were "Commercial through Princeton & GAMS Development Corp." (CV S02–S03). Biomedical collaborations with Mantalaris and Pistikopoulos | CV; ANTIGONE manuscript [stated, primary] |
| 2014–2017 | Lecturer, Department of Computing, Imperial. Job talk 03/2014: "Mixed-Integer Nonlinear Optimization: Foundations and Applications" (CV S03) | First students: Mistry (MEng 2014–15, then PhD 2015–20), Kouyialis (PhD 2014–18), Baltean-Lugojan (PhD 2015–19), Ceccon (MSc 2015, then PhD 2016–21) | CV [stated, primary] |
| 2017–2020 | Senior Lecturer | EPSRC Early Career Fellowship "GALINI: Global ALgorithms for mixed-Integer Nonlinear optimisation of Industrial systems" (2017–2022, £984k, "Includes 6 years postdoc funding"; grant EP/P016871/1). BASF research project (2017, £40k), then a BASF PhD studentship "Global optimisation with ensemble machine learning models" (2019–2022, £270k). IBM PhD Fellowship to Baltean-Lugojan (2017–18). Co-investigator on EPSRC U2 and ROAD2H and on the EU H2020 networks ModLife and SyMBioSys | CV; GALINI README [stated/practice, primary] |
| 2020– | Professor | BASF/Royal Academy of Engineering Research Chair in Data-Driven Optimisation (2022–2027, £216k). Research fellows Kronqvist (Royal Society Newton Fellow, 2019–21) and Tsay (EPSRC/Imperial fellowships, 2020–22). Co-director of the EPSRC AI hub AIchemy (2024–29). Prosperity Partnerships with BASF (IConIC) and Eli Lilly. Amazon Scholar from 2025 | CV; homepage [stated, primary] |
| Awards tied to the works below | — | *J. Global Optim.* Best Paper 2013 (GloMIQO). W. David Smith, Jr. Graduate Student Paper Award 2014 (the 2012 *Math. Program.* paper and GloMIQO). CPAIOR 2021 Distinguished Paper (1 of 30). Rosenbrock Prize 2021 (*Optim. Eng.*, with Kronqvist). COIN-OR Cup 2022 (OMLT). *Comput. Chem. Eng.* Best Paper 2023 (Folch et al.). BCS Roger Needham Award 2023 | CV [stated, primary]. The CV's two-column layout misplaces award years; I aligned them from the raw text |

**How she came to Imperial** [observed, primary; ASR captions]. Pistikopoulos told this in his vote of thanks at her 2023 inaugural lecture:
- He met her at Princeton around 2009, when Floudas introduced her as "his next big thing".
- Late in 2011 Floudas phoned him because "the couple has been deciding to move to to the UK".
- On her later move from Chemical Engineering to Computing: "we're not very happy that you know Ruth was hijacked by the department of computing we wanted to her to stay within the chemical engineering department".

### 1.2 Topics by period

Each line lists works whose identifier I checked with a tool in this run:
- the DOI via Crossref or DBLP;
- or the arXiv id via arxiv.org;
- or, where no DOI exists, venue + year + title, matched across Scholar and the CV.

**2008–2012: PhD with Floudas. Pooling problems, piecewise-linear relaxations, an MIQCQP solver**

- **Pooling and piecewise-linear relaxations.**
  - C. E. Gounaris, R. Misener, C. A. Floudas, "Computational Comparison of Piecewise-Linear Relaxations for Pooling Problems", *Ind. Eng. Chem. Res.* 48(12):5742–5766, 2009. DOI 10.1021/ie8016048
  - R. Misener, C. E. Gounaris, C. A. Floudas, "Global Optimization of Gas Lifting Operations: A Comparative Study of Piecewise Linear Formulations", *Ind. Eng. Chem. Res.* 48(13):6098–6104, 2009. DOI 10.1021/ie8012117
  - R. Misener, C. A. Floudas, "Advances for the pooling problem: Modeling, global optimization, and computational studies", *Applied and Computational Mathematics* 8(1):3–22, 2009. No DOI; the title, venue and pages agree across Scholar, the CV and reference 97 of the GloMIQO manuscript.
  - R. Misener, C. A. Floudas, "Piecewise-Linear Approximations of Multidimensional Functions", *J. Optim. Theory Appl.* 145(1):120–147, 2010. DOI 10.1007/s10957-009-9626-0
  - R. Misener, C. A. Floudas, "Global Optimization of Large-Scale Generalized Pooling Problems: Quadratically Constrained MINLP Models", *Ind. Eng. Chem. Res.* 49(11):5424–5438, 2010. DOI 10.1021/ie100025e
  - R. Misener, C. E. Gounaris, C. A. Floudas, "Mathematical modeling and global optimization of large-scale extended pooling problems with the (EPA) complex emissions constraints", *Comput. Chem. Eng.* 34(9):1432–1456, 2010. DOI 10.1016/j.compchemeng.2010.02.014
  - R. Misener, J. P. Thompson, C. A. Floudas, "APOGEE: Global optimization of standard, generalized, and extended pooling problems via linear and logarithmic partitioning schemes", *Comput. Chem. Eng.* 35(5):876–892, 2011. DOI 10.1016/j.compchemeng.2011.01.026. **Signature work 1**
- **Floudas-group applications where she is a middle author.**
  - J. Li, R. Misener, C. A. Floudas, crude-oil scheduling, *AIChE J.* 58(1):205–226, 2012, DOI 10.1002/aic.12623, and its robust version, *AIChE J.* 58(8):2373–2396, 2012, DOI 10.1002/aic.12772.
  - R. C. Baliban, J. A. Elia, R. Misener, C. A. Floudas, "Global optimization of a MINLP process synthesis model for thermochemical based conversion of hybrid coal, biomass, and natural gas to liquid fuels", *Comput. Chem. Eng.* 42:64–86, 2012, DOI 10.1016/j.compchemeng.2012.03.008.
  - A. Skjäl, T. Westerlund, R. Misener, C. A. Floudas, "A Generalization of the Classical αBB Convex Underestimation via Diagonal and Nondiagonal Quadratic Terms", *J. Optim. Theory Appl.* 154(2):462–490, 2012, DOI 10.1007/s10957-012-0033-6.
- **The MIQCQP relaxations and GloMIQO.** **Signature work 2**
  - R. Misener, C. A. Floudas, "Global optimization of mixed-integer quadratically-constrained quadratic programs (MIQCQP) through piecewise-linear and edge-concave relaxations", *Math. Program.* 136(1):155–182, 2012 (Series B). DOI 10.1007/s10107-012-0555-6
  - R. Misener, C. A. Floudas, "GloMIQO: Global mixed-integer quadratic optimizer", *J. Global Optim.* 57(1):3–50, 2013 (online 7 March 2012). DOI 10.1007/s10898-012-9874-7
- **A review.** R. Misener, C. A. Floudas, "Global optimization of mixed-integer models with quadratic and signomial functions: a review", *Applied and Computational Mathematics* 11(3):317–336, 2012 (CV J13; Scholar).

**2013–2016: RAEng fellow, then lecturer in Computing. The solver consolidated, biomedical systems, her first own students**

- **Solvers.**
  - R. Misener, C. A. Floudas, "A Framework for Globally Optimizing Mixed-Integer Signomial Programs", *J. Optim. Theory Appl.* 161(3):905–932, 2014. DOI 10.1007/s10957-013-0396-3
  - R. Misener, C. A. Floudas, "ANTIGONE: Algorithms for coNTinuous / Integer Global Optimization of Nonlinear Equations", *J. Global Optim.* 59(2–3):503–526, 2014. DOI 10.1007/s10898-014-0166-2. **Signature work 3**
  - R. Misener, J. B. Smadbeck, C. A. Floudas, "Dynamically generated cutting planes for mixed-integer quadratically constrained quadratic programs and their incorporation into GloMIQO 2", *Optim. Methods Softw.* 30(1):215–249, 2015. DOI 10.1080/10556788.2014.916287 (**not read**)
- **Biomedical and bioprocess line**, with Mantalaris, Panoskaltsis and Pistikopoulos.
  - R. Misener et al., "Global superstructure optimisation of red blood cell production in a parallelised hollow fibre bioreactor", *Comput. Chem. Eng.* 71:532–553, 2014. DOI 10.1016/j.compchemeng.2014.10.004
  - M. Fuentes-Garí et al., "A systematic framework for the design, simulation and optimization of personalized healthcare: Making and healing blood", *Comput. Chem. Eng.* 81:80–93, 2015. DOI 10.1016/j.compchemeng.2015.03.008
  - S. Savvopoulos et al., "A Personalized Framework for Dynamic Modeling of Disease Trajectories in Chronic Lymphocytic Leukemia", *IEEE Trans. Biomed. Eng.* 63(11):2396–2404, 2016. DOI 10.1109/TBME.2016.2533658
  - R. Misener et al., "Stem cell biomanufacturing under uncertainty: A case study in optimizing red blood cell production", *AIChE J.* 64(8):3011–3022, 2018. DOI 10.1002/aic.16042
- **A review.** F. Boukouvala, R. Misener, C. A. Floudas, "Global optimization advances in Mixed-Integer Nonlinear Programming, MINLP, and Constrained Derivative-Free Optimization, CDFO", *Eur. J. Oper. Res.* 252(3):701–727, 2016. DOI 10.1016/j.ejor.2015.12.018
- **The first papers led by her own students** (CV).
  - M. Mistry, R. Misener, "Optimising heat exchanger network synthesis using convexity properties of the logarithmic mean temperature difference", *Comput. Chem. Eng.* 94:1–17, 2016. DOI 10.1016/j.compchemeng.2016.07.001. From Mistry's MEng thesis.
  - F. Ceccon, G. Kouyialis, R. Misener, "Using functional programming to recognize named structure in an optimization problem: Application to pooling", *AIChE J.* 62(9):3085–3095, 2016. DOI 10.1002/aic.15308. From Ceccon's MSc thesis.
  - D. Ulmasov, C. Baroukh, B. Chachuat, M. P. Deisenroth, R. Misener, "Bayesian Optimization with Dimension Scheduling: Application to Biological Systems", arXiv:1511.05385 (ESCAPE 26, 2016). Her earliest Bayesian-optimization item: an MSc thesis co-supervised with Deisenroth.
- **Her essay on Floudas.** R. Misener, "Christodoulos Achilleus Floudas", *SIAG/OPT Views and News* 24(1):12–16, October 2016. Read in full; see §2. [stated]

**2017–2021: Senior lecturer on the EPSRC "GALINI" fellowship. Broadening into complexity, approximation, uncertainty, machine learning for solvers, and solver software in Python**

- **Pooling complexity.** R. Baltean-Lugojan, R. Misener, "Piecewise parametric structure in the pooling problem: from sparse strongly-polynomial solutions to NP-hardness", *J. Global Optim.* 71(4):655–690, 2018. DOI 10.1007/s10898-017-0577-y. Preprint: Optimization Online 2016/05/5457, posted 22 May 2016.
- **Approximation algorithms and scheduling.**
  - D. Letsios, G. Kouyialis, R. Misener, "Heuristics with performance guarantees for the minimum number of matches problem in heat recovery network design", *Comput. Chem. Eng.* 113:57–85, 2018. DOI 10.1016/j.compchemeng.2018.03.002
  - D. Letsios et al., "Approximation algorithms for process systems engineering", *Comput. Chem. Eng.* 132:106599, 2020. DOI 10.1016/j.compchemeng.2019.106599
  - D. Letsios, M. Mistry, R. Misener, "Exact lexicographic scheduling and approximate rescheduling", *Eur. J. Oper. Res.* 290(2):469–478, 2021. DOI 10.1016/j.ejor.2020.08.032
- **Logic and explainability.**
  - M. Mistry, A. Callia D'Iddio, M. Huth, R. Misener, "Satisfiability modulo theories for process systems engineering", *Comput. Chem. Eng.* 113:98–114, 2018. DOI 10.1016/j.compchemeng.2018.03.004
  - K. Cyras, D. Letsios, R. Misener, F. Toni, "Argumentation for Explainable Scheduling", AAAI 2019. DOI 10.1609/aaai.v33i01.33012752
- **Design of experiments.** S. Olofsson, M. P. Deisenroth, R. Misener, "Design of Experiments for Model Discrimination Hybridising Analytical and Data-Driven Approaches", ICML 2018, PMLR 80:3905–3914 (arXiv:1802.04170). Her first computer-science conference paper (CV C01).
- **Optimization under uncertainty.** J. Wiebe, I. Cecílio, R. Misener, "Data-Driven Optimization of Processes with Degrading Equipment", *Ind. Eng. Chem. Res.* 57(50):17177–17191, 2018. DOI 10.1021/acs.iecr.8b03292. Funded by Schlumberger.
- **Symmetry.** G. Kouyialis, X. Wang, R. Misener, "Symmetry Detection for Quadratic Optimization Using Binary Layered Graphs", *Processes* 7(11):838, 2019. DOI 10.3390/pr7110838
- **Machine learning inside the solver.** R. Baltean-Lugojan, P. Bonami, R. Misener, A. Tramontani, "Scoring positive semidefinite cutting planes for quadratic optimization via trained neural networks", Optimization Online 2018/11/6943 (posted 26 November 2018; listed as revised November 2019). **Never published in a journal** (§1.9).
- **Community resources.**
  - F. Furini et al. (13 authors incl. Misener), "QPLIB: a library of quadratic programming instances", *Math. Program. Comput.* 11(2):237–265, 2019. DOI 10.1007/s12532-018-0147-4
  - P. Bonami, A. M. Gleixner, J. Linderoth, R. Misener (eds.), report of Dagstuhl Seminar 18081, *Dagstuhl Reports* 8(2):64–87, 2018. DOI 10.4230/DagRep.8.2.64
- **Polynomial optimization.** J. S. Campos, R. Misener, P. Parpas, "A multilevel analysis of the Lasserre hierarchy", *Eur. J. Oper. Res.* 277(1):32–41, 2019. DOI 10.1016/j.ejor.2019.02.016
- **Neural-network verification.** E. Botoeva, P. Kouvaros, J. Kronqvist, A. Lomuscio, R. Misener, "Efficient Verification of ReLU-Based Neural Networks via Dependency Analysis", AAAI 2020, 34(04):3291–3299. DOI 10.1609/aaai.v34i04.5729
- **Structure detection in Pyomo.** F. Ceccon, J. D. Siirola, R. Misener, "SUSPECT: MINLP special structure detector for Pyomo", *Optim. Lett.* 14(4):801–814, 2020. DOI 10.1007/s11590-019-01396-y
- **Trained gradient-boosted trees.** M. Mistry, D. Letsios, G. Krennrich, R. M. Lee, R. Misener, "Mixed-Integer Convex Nonlinear Optimization with Gradient-Boosted Trees Embedded", *INFORMS J. Comput.* 33(3):1103–1119, 2021. DOI 10.1287/ijoc.2020.0993 (arXiv:1803.00952, v1 March 2018). **Signature work 4 (start)**
- **Convex MINLP cuts.** J. Kronqvist, R. Misener, "A disjunctive cut strengthening technique for convex MINLP", *Optim. Eng.* 22(3):1315–1345, 2021 (online 2020). DOI 10.1007/s11081-020-09551-6. Rosenbrock Prize (CV).
- **Intermediate formulations.** J. Kronqvist, R. Misener, C. Tsay, "Between Steps: Intermediate Relaxations Between Big-M and Convex Hull Formulations", CPAIOR 2021, LNCS pp. 299–314. DOI 10.1007/978-3-030-78230-6_19 (arXiv:2101.12708). **Signature work 5 (start)**
- **Perspective.** E. N. Pistikopoulos et al. (9 authors incl. Misener), "Process systems engineering – The generation next?", *Comput. Chem. Eng.* 147:107252, 2021. DOI 10.1016/j.compchemeng.2021.107252

**2021–2026: Professor and BASF/RAEng chair. Optimization over trained models, intermediate formulations, Bayesian optimization, graphs and molecules**

- **Optimization over trained models.** **Signature work 4**
  - A. Thebelt et al., "ENTMOOT: A framework for optimization over ensemble tree models", *Comput. Chem. Eng.* 151:107343, 2021. DOI 10.1016/j.compchemeng.2021.107343 (arXiv:2003.04774)
  - F. Ceccon et al., "OMLT: Optimization & Machine Learning Toolkit", *J. Mach. Learn. Res.* 23(349):1–8, 2022 (arXiv:2202.02414)
- **Intermediate formulations.** **Signature work 5**
  - C. Tsay, J. Kronqvist, A. Thebelt, R. Misener, "Partition-based formulations for mixed-integer optimization of trained ReLU neural networks", NeurIPS 34 (2021), pp. 3068–3080 (arXiv:2102.04373)
  - J. Kronqvist, R. Misener, C. Tsay, "P-split formulations: a class of intermediate formulations between big-M and convex hull for disjunctive constraints", *Math. Program.* 218(1–2):57–94, 2026 (online 9 June 2025). DOI 10.1007/s10107-025-02232-1 (arXiv:2202.05198)
- **Pooling at scale.** F. Ceccon, R. Misener, "Solving the pooling problem at scale with extensible solver GALINI", *Comput. Chem. Eng.* 159:107660, 2022. DOI 10.1016/j.compchemeng.2022.107660 (arXiv:2105.01687)
- **Robust optimization.**
  - J. Wiebe, I. Cecílio, J. Dunlop, R. Misener, "A robust approach to warped Gaussian process-constrained optimization", *Math. Program.* 196(1–2):805–839, 2022. DOI 10.1007/s10107-021-01762-8
  - J. Wiebe, R. Misener, "ROmodel: modeling robust optimization problems in Pyomo", *Optim. Eng.* 23(4):1873–1894, 2022. DOI 10.1007/s11081-021-09703-2
- **Bayesian optimization.**
  - A. Thebelt et al., "Tree ensemble kernels for Bayesian optimization with known constraints over mixed-feature spaces", NeurIPS 2022 (arXiv:2207.00879)
  - J. P. Folch et al., "SnAKe: Bayesian Optimization with Pathwise Exploration", NeurIPS 2022 (arXiv:2202.00060)
  - J. P. Folch et al., "Combining multi-fidelity modelling and asynchronous batch Bayesian Optimization", *Comput. Chem. Eng.* 172:108194, 2023. DOI 10.1016/j.compchemeng.2023.108194. The journal's Best Paper (CV).
  - J. P. Folch et al., "Transition Constrained Bayesian Optimization via Markov Decision Processes", NeurIPS 2024 (arXiv:2402.08406). With A. Krause and M. Mutný.
  - S. Zhang, R. M. Lee, B. Shafei, D. Walz, R. Misener, "Dependence in constrained Bayesian optimization", *Optim. Lett.* 18(6):1457–1473, 2024. DOI 10.1007/s11590-023-02047-z
  - T. Boyne, J. P. Folch, R. M. Lee, B. Shafei, R. Misener, "BARK: A Fully Bayesian Tree Kernel for Black-box Optimization", ICML 2025 (arXiv:2503.05574)
  - J. P. Dürholt et al. (BASF-led, 18 authors), "BoFire: Bayesian Optimization Framework Intended for Real Experiments", *J. Mach. Learn. Res.* 26(204):1–7, 2025 (arXiv:2408.05040)
- **Graphs and molecules.**
  - S. Zhang et al., "Optimizing over trained GNNs via symmetry breaking", NeurIPS 2023 (arXiv:2305.09420)
  - C. Hojny, S. Zhang, J. S. Campos, R. Misener, "Verifying message-passing neural networks via topology-based bounds tightening", ICML 2024, pp. 18489–18514 (arXiv:2402.13937)
  - S. Zhang et al., "Augmenting optimization-based molecular design with graph neural networks", *Comput. Chem. Eng.* 186:108684, 2024. DOI 10.1016/j.compchemeng.2024.108684
  - S. Zhang et al., "Limeade: Let integer molecular encoding aid", *Comput. Chem. Eng.* 199:109115, 2025. DOI 10.1016/j.compchemeng.2025.109115
  - Y. Xie, S. Zhang, J. Qing, R. Misener, C. Tsay, "BoGrape: Bayesian optimization over graphs with shortest-path encoded", ICLR 2026 (arXiv:2503.05642)
- **Data, statistics and chemistry.**
  - A. Thebelt et al., "Maximizing information from chemical engineering data sets: Applications to machine learning", *Chem. Eng. Sci.* 252:117469, 2022. DOI 10.1016/j.ces.2022.117469
  - R. Sedgwick et al., "Transfer learning Bayesian optimization for competitor DNA molecule design for use in diagnostic assays", *Biotechnol. Bioeng.* 122(1):189–210, 2025. DOI 10.1002/bit.28854
  - T. Boyne et al., "The Catechol Benchmark: Time-series Solvent Selection Data for Few-shot Machine Learning", NeurIPS 2025 Datasets & Benchmarks (arXiv:2506.07619)
- **Perspective.** R. Misener, L. T. Biegler, "Formulating data-driven surrogate models for process optimization", *Comput. Chem. Eng.* 179:108411, 2023. DOI 10.1016/j.compchemeng.2023.108411. Her FOCAPO/CPC 2023 joint keynote; **not read**.

**Reading the periods** [inferred, from the lists and her own framing]

- **One spine runs through all four periods**: building relaxations and formulations that let a solver exploit structure. In order:
  - piecewise-linear relaxations (2009–11);
  - edge-concave facets and automatic process-network reformulations (2012–13);
  - an extensible term-based relaxation framework (2014);
  - convexity, symmetry and special-structure detection (2016–20);
  - NN-scored SDP cuts (2018);
  - MIP formulations of trained trees, ReLU networks and GNNs (2018–24);
  - parameterized intermediate formulations (2021–26);
  - since 2020, global optimization of Bayesian-optimization acquisition functions written as MINLPs (ENTMOOT, tree kernels, BARK, graph BO).

  She frames it the same way herself [stated, primary; ASR captions, 05:37]: "So all I've been doing here at Imperial uh is basically figuring out how to relax better."
- **The application domains change with collaborators and funding.** They run from refineries and the EPA (Floudas), to blood bioreactors and leukaemia (Mantalaris and Pistikopoulos), heat recovery (EPSRC First Grant), Royal Mail scheduling, Schlumberger drilling, and BASF and Eli Lilly chemistry. Her own account of how directions get chosen [stated, primary; ASR captions, 46:04–46:34]: "basically I'm a person who chooses my my my my vision in some part by my pub buddies" and "So in some ways very opportunistic."
- **A 2010 sentence foreshadows the ML turn.** The JOTA 2010 paper (author version, abstract): "If mixed-integer linear optimization problems (MILPs) involving multidimensional piecewise-linear functions can be easily and efficiently solved to global optimality, then non-analytic functions can be used as an objective or constraint function for large optimization problems." Trained tree ensembles (piecewise-constant) and ReLU networks (piecewise-linear) are exactly such non-analytic functions. Calling this a continuity is my reading. [inferred, with a primary quote]

### 1.3 Author order: first author until 2015, last author from 2016

In her fields (chemical engineering, OR and machine learning), author order is not alphabetical. The student or postdoc who did the work comes first and the supervising PI comes last. Sometimes a co-supervisor takes the final position instead.

Counts over the CV lists [practice, primary]:

| CV block | Misener first | Misener last | Middle |
|---|---|---|---|
| Journal J01–J19 (2009–2015) | 13 | 0 | 6 |
| Journal J20–J65 (2015–2025) | 2 | 28 | 16 |
| CS conferences C01–C16 (2018–2025) | 0 | 8 | 8 |

- **J01–J19.** All 13 first-authored papers are either with Floudas (pooling, piecewise-linear, GloMIQO, ANTIGONE, signomial, GloMIQO 2) or her RAEng-era bioreactor paper (J17).
- **J20–J65.** Both first-authored papers are invited pieces: the 2018 *AIChE J.* "Futures" paper (J33) and the 2023 FOCAPO/CPC keynote paper with Biegler (J60). The middle positions are collaborator-led work:
  - biomedical papers led by Mantalaris's group;
  - the EJOR review;
  - QPLIB;
  - the PSE perspective;
  - co-supervised work where the ML co-supervisor is last.
- **The pivot year is 2016.** Mistry & Misener (from the MEng thesis) and Ceccon, Kouyialis & Misener (from the MSc thesis) are her first last-authored papers. [practice, primary]
- **Team size grows.** Mean authors per distinct DBLP work: 3.2 (2009–12), 3.9 (2013–16), 4.7 (2017–20), 6.2 (2021–26). [practice, secondary]
- **Two author orders differ between the CV and other records.** Neither changes the first/last picture.
  - "Partial Lasserre relaxation for sparse Max-Cut": Campos, Parpas, Misener in the CV; Campos, Misener, Parpas in Crossref.
  - The AAAI 2020 paper: Botoeva, Kronqvist, Kouvaros, Lomuscio, Misener in the CV; Botoeva, Kouvaros, Kronqvist, Lomuscio, Misener in Crossref and Scholar.

### 1.4 Collaboration network and students

**Most frequent co-authors** among the 72 distinct DBLP works [practice, secondary]:

| Co-author | Papers | Years |
|---|---|---|
| Calvin Tsay | 17 | 2021–26 |
| Robert M. Lee (BASF) | 14 | 2018–26 |
| Christodoulos A. Floudas | 11 | 2010–17 |
| Dimitrios Letsios | 10 | 2018–21 |
| Behrang Shafei (BASF) | 10 | 2022–26 |
| Shiqiang Zhang | 10 | 2022–26 |
| Miten Mistry | 8 | 2016–21 |
| Mark van der Wilk | 8 | 2020–26 |
| David Walz (BASF) | 8 | 2021–25 |
| Jose Pablo Folch | 7 | 2022–25 |
| Juan S. Campos | 6 | 2019–25 |
| Jan Kronqvist | 6 | 2020–26 |
| Alexander Thebelt | 6 | 2021–22 |
| Marc P. Deisenroth | 5 | 2015–21 |
| Jixiang Qing | 5 | 2025–26 |

**Clusters** [practice from the author lists; the grouping is inferred]:
- **(a) Floudas's Princeton group**: Gounaris, Thompson, Jie Li, Baliban, Elia, Smadbeck; plus Skjäl and Westerlund (Åbo Akademi).
- **(b) Imperial chemical engineering**: Pistikopoulos, Mantalaris, Panoskaltsis, Fuentes-Garí, Velliou, Allenby, Savvopoulos; and Chachuat.
- **(c) Imperial computing and mathematics colleagues**: Deisenroth, Parpas, Toni, Huth, Lomuscio, Ham, van der Wilk, Filippi; plus Stevens (Materials) and Jelfs (Chemistry).
- **(d) Industry**: BASF (Lee, Krennrich, Sudermann-Merx, Walz, Shafei); IBM/CPLEX (Bonami, Tramontani); Royal Mail (Bradley); Schlumberger (Cecílio); Eli Lilly (García-Muñoz).
- **(e) The Pyomo/Sandia ecosystem**: Siirola, Bynum, Jalving, Haddad; plus Laird (CMU).
- **(f) The MINLP community**: the QPLIB consortium, and her Dagstuhl 18081 co-organizers Bonami, Gleixner and Linderoth.
- **(g) ETH Zürich**, for MDP-constrained Bayesian optimization: Krause and Mutný.

**PhD students**, from the CV section "Research Mentoring for PhD Candidates" [stated, primary]:

| Student | Years | Thesis topic or funding (CV) | Verified papers with her |
|---|---|---|---|
| Georgia Kouyialis | 2014–18 | "Exploiting Symmetry in Mixed-Integer Nonlinear Optimisation"; EPSRC DTA | symmetry detection (*Processes* 2019); functional-programming pooling (*AIChE J.* 2016) |
| Radu Baltean-Lugojan | 2015–19 | "Exploiting Structure in Nonconvex Quadratic Optimisation"; EPSRC DTA; IBM PhD Fellowship | pooling complexity (JOGO 2018); NN-scored SDP cuts (preprint 2018) |
| Miten Mistry | 2015–20 (MEng 2014–15) | "Branching strategies for mixed-integer programs containing logical constraints and decomposable structure"; HiPEDS CDT | LMTD convexity (C&CE 2016); SMT (C&CE 2018); gradient-boosted trees (IJOC 2021) |
| Simon Olofsson | 2016–20 | Gaussian processes for design of experiments; EU H2020 ModLife | ICML 2018; GPdoemd (C&CE 2019); IEEE TBME 2019 |
| Francesco Ceccon | 2016–21 (MSc 2015) | EPSRC | SUSPECT (Optim. Lett. 2020); GALINI (C&CE 2022); OMLT (JMLR 2022) |
| Johannes Wiebe | 2017–21 | Schlumberger and HiPEDS CDT | degrading equipment (I&ECR 2018); robust pooling (I&ECR 2019); warped GP (MP 2022); ROmodel (OE 2022) |
| Alexander Thebelt | 2019–23 | BASF | ENTMOOT (C&CE 2021); tree kernels (NeurIPS 2022); CES 2022; Applied Energy 2022; OMLT |
| Ruby Sedgwick | 2019–23 | EPSRC CDT AI4Health; co-supervised with M. Stevens | *Biotechnol. Bioeng.* 2025 |
| Jose Pablo Folch | 2020–24 | BASF and EPSRC CDT StatML; co-supervised with M. van der Wilk | SnAKe (NeurIPS 2022); multi-fidelity BO (C&CE 2023, Best Paper); MDP BO (NeurIPS 2024) |
| James Odgers | 2020–25 | Eli Lilly/EPSRC; co-supervised with S. Filippi | PLS bootstrap (*AIChE J.* 2023; Scholar); GPLVMs (AISTATS 2025) |
| Shiqiang Zhang | 2021– | Hans Rausing Scholarship | GNN symmetry breaking (NeurIPS 2023); ICML 2024; Limeade (C&CE 2025); graph encoding (arXiv 2025) |
| Toby Boyne | 2023– | BASF and StatML CDT | BARK (ICML 2025); Catechol (NeurIPS 2025) |

**Research fellows and postdocs she mentored** (CV) [stated, primary]:
- Jan Kronqvist (2019–21).
- Calvin Tsay (2020–22; now Associate Professor at Imperial).
- Dimitrios Letsios (2016–19).
- Kristijonas Cyras (2017–20; F. Toni was his primary supervisor).
- Juan Campos Salazar.
- Chrysoula Kappatou (2020–23).
- Ruby Sedgwick and Jixiang Qing (2023–25).

**Masters and undergraduate projects that became papers** (CV) [stated, primary]: Mistry (J25), Ceccon (J26), Ulmasov (E17), Wesselhoeft (E22), Page (C03 and J45), Suraj G (J45).

**One network detail** [practice, primary; any causal link is inferred]:
- Misener was the external examiner of Kronqvist's PhD (Åbo Akademi, 09/2018; CV thesis committees).
- His 2019 review with Bernal, Lundell and Grossmann benchmarked ANTIGONE critically (§2, SW3).
- He then joined her group as a Newton Fellow (2019–21) and co-authored SW5.

### 1.5 Usual venues

**Journals in the CV (65 papers, counted by hand)** [practice, primary]:

| Field | Papers | Venues |
|---|---|---|
| Chemical engineering | 31 | *Comput. Chem. Eng.* 18; *Ind. Eng. Chem. Res.* 7; *AIChE J.* 5; *Chem. Eng. Sci.* 1 |
| Optimization and OR | 22 | *J. Global Optim.* 3; *J. Optim. Theory Appl.* 3; *Eur. J. Oper. Res.* 3; *Optim. Eng.* 3; *Math. Program.* 2 (3 counting P-split 2026); *Optim. Lett.* 2; *Appl. Comput. Math.* 2; one each in *Math. Program. Comput.*, *Optim. Methods Softw.*, *INFORMS J. Comput.* and *J. Scheduling* |
| Biomedical | 8 | — |
| Machine learning | 1 | *JMLR* |
| Other | 3 | *Processes*, *Chem. Soc. Rev.*, *Applied Energy* |

**Computer-science conferences in the CV (C01–C16)** [practice, primary]:
- NeurIPS 6 (2021–25), ICML 3 (2018, 2024, 2025), AAAI 2 (2019, 2020).
- One each at AAMAS, CPAIOR, COCOA, AISTATS and GECCO.
- ICLR 2026 is in DBLP but postdates the CV.
- Each CS entry in the CV carries its CORE rank and acceptance rate.

**The pattern** [inferred]:
- Solver and algorithm papers go to *J. Global Optim.* and *Math. Program.*
- Application and modelling papers go to *Comput. Chem. Eng.* and *I&ECR*.
- From 2018, ML-facing work goes to NeurIPS, ICML and AAAI. The same ideas then reappear in *Comput. Chem. Eng.* for the process-systems audience.

### 1.6 Most-cited works

Columns: GS = Google Scholar, fetched 2026-10-10; S2 = Semantic Scholar, with influential citations in brackets; CR = Crossref "is-referenced-by" count. [practice, secondary]

| # | Work | GS | S2 | CR |
|---|---|---|---|---|
| 1 | Misener & Floudas, ANTIGONE, JOGO 2014 | 742 | 568 (24) | 457 |
| 2 | Pistikopoulos et al., PSE – the generation next?, C&CE 2021 (perspective, 9 authors) | 332 | — | 254 |
| 3 | Boukouvala, Misener & Floudas, MINLP and CDFO review, EJOR 2016 | 326 | — | 217 |
| 4 | Misener & Floudas, GloMIQO, JOGO 2013 | 280 | 224 (16) | 160 |
| 5 | Botoeva et al., ReLU network verification, AAAI 2020 | 248 | — | 92 |
| 6 | Ceccon et al., OMLT, JMLR 2022 | 232 | — | — |
| 7 | Misener & Floudas, pooling review, Appl. Comput. Math. 2009 | 215 | — | — |
| 8 | Gounaris, Misener & Floudas, piecewise-linear relaxations for pooling, I&ECR 2009 | 196 | — | 122 |
| 9 | Misener, Thompson & Floudas, APOGEE, C&CE 2011 | 185 | — | 112 |
| 10 | Furini et al., QPLIB, MPC 2019 | 172 | — | 79 |
| 11 | Misener & Floudas, MIQCQP piecewise-linear and edge-concave relaxations, MP 2012 | 165 | 133 (7) | 95 |
| 12 | Misener & Floudas, piecewise-linear approximations, JOTA 2010 | 150 | — | 93 |
| 13 | Tsay et al., partition-based ReLU formulations, NeurIPS 2021 | 146 | — | — |
| 14 | Thebelt et al., chemical engineering data sets and ML, CES 2022 | 143 | — | 109 |
| 15 | Misener & Biegler, data-driven surrogate models, C&CE 2023 | 122 | — | 103 |

Further Scholar counts:
- The gradient-boosted-tree paper in *INFORMS J. Comput.* has 99 and ENTMOOT 80.
- The Bayesian-optimization papers are cited less so far: multi-fidelity BO 60, SnAKe 31, the NeurIPS 2022 tree kernels 26, BARK 7.
- The unpublished NN-scored SDP-cut preprint has 97.

### 1.7 Recent works (about the last 12 months, October 2025 to October 2026)

- **P-split.** J. Kronqvist, R. Misener, C. Tsay, *Math. Program.* 218(1–2):57–94. Issue dated July 2026; online 9 June 2025. DOI 10.1007/s10107-025-02232-1 [practice]
- **BoGrape.** Y. Xie, S. Zhang, J. Qing, R. Misener, C. Tsay, "BoGrape: Bayesian optimization over graphs with shortest-path encoded", ICLR 2026 (DBLP). arXiv:2503.05642, latest version 21 April 2026. [practice]
- **The Catechol Benchmark.** T. Boyne et al., NeurIPS 2025 Datasets & Benchmarks (arXiv:2506.07619, v2 27 November 2025). A benchmark dataset, a new kind of output for her group. [practice]
- **Graph encoding.** S. Zhang, R. Misener, "Beyond adjacency: Graph encoding with reachability and shortest paths", arXiv:2509.20247 (24 September 2025). Its abstract introduces "explicit optimization formulations for graph search space" and proves that its symmetry-breaking constraints "will not reduce the original graph space". [practice]
- **Meta-learning.** B. Langdon et al. (with Misener, van der Wilk and Tsay, and the BASF co-authors Lee and Shafei), "Meta-learning for sample-efficient Bayesian optimisation of fed-batch processes", arXiv:2605.05382 (6 May 2026). [practice]
- **GPLVMs.** M. Tretiakov, S. Filippi, V. Fortuin, R. Misener, R. Sedgwick, J. Odgers, "Amortized Structured Stochastic Variational Inference for Gaussian Process Latent Variable Models", arXiv:2610.03647 (v1 2 October 2026). [practice]
- **Talks** [stated, primary]:
  - CV item K28 lists an upcoming plenary at the SIAM Conference on Optimization 2026 (Edinburgh, 06/2026), "Optimizing over graphs: Challenges, Formulations, and Applications". Whether it took place was not checked.
  - Her 2025 plenary and semi-plenary talks at EUROPT, ICCOPT and OR 2025 had one title: "Bayesian optimization for mixed feature spaces using tree kernels and graph kernels" (CV K25–K27).

**Reading** [inferred]:
- Her newest main topic is optimization over graph-structured spaces: GNNs, molecules and neural architectures. It uses the same MINLP-formulation toolkit as the solver years: explicit encodings, symmetry breaking and bounds tightening.
- Of the items above, only the 2026 GPLVM preprint has no optimization-formulation component.

### 1.8 Software as publication

| Software | Facts | Tags |
|---|---|---|
| APOGEE (2010) | A C++ core with SNOPT 5.3 and CPLEX 12.1 (or SCIP 2.0.0 with CLP 1.13), plus a cross-platform "APOGEE Desktop Client". Stated to be "freely available to the scientific community at helios.princeton.edu/APOGEE/". On 2026-10-10 that host did not answer (connection failed) | [stated/practice, primary; status observed] |
| GloMIQO | "first available in GAMS 23.8" (ANTIGONE manuscript). GAMS 40.1.0 release notes (1 August 2022): "As announced, dropped GLOMIQO. The use of ANTIGONE is equivalent." The GloMIQO manual page exists in the GAMS 30–39 documentation and returns 404 from GAMS 40 on | [stated, primary; observed, secondary] |
| ANTIGONE | "first available in GAMS 24.1". Still documented in the current GAMS documentation (version 54). The manual page is dated "16 April 2013", and its sample log reads "Version 1.0". It requires an ANTIGONE licence, a CPLEX licence and a CONOPT or SNOPT licence | [observed, secondary] |
| CV entries S01–S03 | "The following implementations are primarily written by me. Implementations of my group's optimisation algorithms, i.e. code primarily written by my team, are on our GitHub account." | [stated, primary] |
| GitHub `cog-imperial` (33 public repositories; API, 2026-10-10) | OMLT: 349 stars, 77 forks, created 2021-06-03, last push 2026-07-09. romodel: 89 stars. entmoot: 64. galini: 45 (created 2018-04-02). GPdoemd: 37. Limeade: 31. suspect: 26. SnAKe: 17. Several repositories exist only to reproduce one paper: PartitionedFormulations_NN, GNN_MIP_CAMD, OMLT_CAMD, DCBO, min_matches_heuristics, two_stage_scheduling | [practice, primary] |
| Code with every paper | From J25 (2016) on, most CV entries carry a "GitHub link" note, and many also a "Video link" | [practice, primary] |
| Her own usage figure [ASR captions, 29:04] | "we won uh, Coinor Cup [sic, ASR] as the best operations research uh, software um, that's open source" and "we're doing 20,000 downloads a month and have been for the last year". This is about OMLT, in March 2023; not checked independently | [stated, primary] |

### 1.9 Failures, abandoned directions and unpublished work

Each item gives the evidence. Reasons are given only where a source states them.

1. **Logarithmic partitioning lost to linear partitioning inside her own solver (APOGEE, 2011).** [practice, primary; reason stated: solver stability]
   - The novel logarithmic piecewise relaxation won at high partition counts, but small partition counts converged fastest, and three large instances had numerical trouble with it.
   - Conclusion (APOGEE author version): "Therefore, we will continue using the linear relaxation scheme to solve pooling problems."
2. **Her PhD's piecewise-linear relaxations ship switched off in GloMIQO.** "Therefore, the default in GloMIQO is not to use the piecewise-linear relaxations." [practice, primary]
3. **The generic solver lost to the special-purpose one.** The 2012 *Math. Program.* author version: "Observe in Table 6 that our pooling problem-specific solver APOGEE [65] regurally [sic] outperforms the more generic work presented here." [practice, primary]
4. **GloMIQO was retired as a standalone product.** GAMS dropped it in GAMS 40.1.0 (August 2022) because ANTIGONE covers it. [observed, secondary]
5. **ANTIGONE stops at version 1.x in the public record.** [practice, primary]
   - No later ANTIGONE paper or major version was found.
   - Her solver building moved to open-source Python on Pyomo: SUSPECT (2019/2020) and GALINI (repository from 2018; EPSRC fellowship 2017–22).
   - Why she left the commercial C++/GAMS line is **not stated** in anything I read.
   - Her 2013 talk "Architecting ANTIGONE: Design Choices and Tradeoffs" (ZIB MODAL workshop, CV I03) was **not found**.
6. **The general GALINI solver paper never appeared in a journal, as of the December 2025 CV.** [practice, primary]
   - The Optimization Online preprint (Baltean-Lugojan, Bynum, Ceccon, Li, Misener; 14 January 2021) describes a general, extensible MIQCQP solver.
   - The journal paper (*Comput. Chem. Eng.* 2022) has two authors and narrows to pooling problems with plug-ins.
   - The preprint is candid about speed: "This is the result we expected since GALINI is built to be easy to extend and does not focus on performance."
   - Whether the general paper was submitted and rejected: **not known**.
7. **The NN-scored SDP-cut work with IBM's Bonami and Tramontani remains a preprint.** [practice, primary]
   - It is Optimization Online 2018/11/6943 (revised November 2019), with 97 Scholar citations.
   - In the CV it appears only as seminar titles S23 and S26 (2019); it also appears as a 2018 Dagstuhl abstract.
   - It is also the core of Baltean-Lugojan's 2019 thesis (Spiral record found; thesis **not read**).
   - What happened to it after 2019: **not known**.
8. **The gradient-boosted-tree paper was reframed.** [practice, primary]
   - arXiv v1 (2 March 2018) was titled "Optimization with Gradient-Boosted Trees and Risk Control". That is the CoRR title DBLP records for 1803.00952, and also the title of her January 2018 SIAM UKIE plenary (CV K03).
   - By v3 (25 September 2019) it was "Mixed-Integer Convex Nonlinear Optimization with Gradient-Boosted Trees Embedded".
   - It appeared in *INFORMS J. Comput.* in 2021, about 3.3 years after v1.
   - Reason for the retitling: **not stated**.
9. **P-split took four years from conference paper to journal.** [practice, primary]
   - Timeline: CPAIOR preprint (January 2021; Distinguished Paper) → arXiv:2202.05198 v1 (10 February 2022) → *Math. Program.* received 21 April 2024 → accepted 17 April 2025.
   - What happened between February 2022 and April 2024 is **not known**.
10. **Directions that stopped, with the years of their papers** [practice; reasons not documented]:
    - bioprocess and leukaemia modelling with Mantalaris and Pistikopoulos (2013–2018);
    - SMT for process systems (2017–18);
    - explainable scheduling via argumentation, with Toni (2018–20);
    - rescheduling with Royal Mail (2018–21);
    - symmetry detection (2017–19);
    - the Lasserre-hierarchy work with Campos and Parpas (2019–23).

    The end dates line up with grant end dates in the CV (U2 2015–19; ModLife and SyMBioSys 2015–19; ROAD2H 2017–20) and with postdoc departures (Letsios moved to King's College London). That match is my reading [inferred]. Her own account is the "very opportunistic" quote in §1.2.
11. **Retractions, corrections and rejections.** None of the 52 Crossref records retrieved shows an update or retraction relation. A dedicated Retraction Watch search was not done. No rejected papers are documented in the public sources I found.

### 1.10 What she herself puts first [stated, primary]

- **Her 2023 inaugural lecture** [ASR captions]:
  - On the GloMIQO/ANTIGONE structure-detection work [11:12–12:44]: "So this is the work that got me hired uh by this department." On what it did: "Adding these equations which were redundant in the original problem formulation tightened the relaxation. This was already known. But what we did was that we actually um found ways of getting these equations." And: "So uh this one uh best paper in the journal of global optimization and got me this job."
  - She then walks through: Mistry's convexity observation for heat recovery networks; Letsios's rescheduling; Kronqvist's partitioned bounds for neural networks; Sedgwick's transfer-learning Bayesian optimization; and the tree-model line from Mistry to ENTMOOT to OMLT.
  - Asked which improvement surprised her most, she picked an academic result over an industrial one [45:03–45:33]: "where we were able to jump forward on a more academic problem was in uh where Mitten [sic, ASR] figured out uh the convexity uh of this one structure and basically then it was that these problems that had been super difficult were now quite easy."
- **Her 2016 essay on Floudas** highlights GloMIQO and ANTIGONE. It also highlights the answer, found with Baltean-Lugojan, to Floudas's question about why piecewise approximations work (§2, SW1).
- **Her CV** lists APOGEE, GloMIQO and ANTIGONE as the software "primarily written by me" (S01–S03).
- **Her repeated plenary titles**:
  - "Between formulations or: How I Learned to Stop Worrying and Love Parameters": HUGO 2022, plus talks at MIT, Princeton, Cornell and the IMA.
  - "OMLT: Optimization and Machine Learning Toolkit": a PSE 2021+ keynote and five industry seminars.
  - "Bayesian optimization for mixed feature spaces using tree kernels and graph kernels": four plenaries or semi-plenaries in 2025.

---

## 2. Signature works, dissected (framework §五)

**How the five were chosen**:
- SW3 is the most cited.
- SW2 is what she names herself: "the work that got me hired"; a *J. Global Optim.* Best Paper; software "primarily written by me".
- SW1, SW4 and SW5 are turning points:
  - SW1 is the origin: a PhD question that took eight years to answer.
  - SW4 is the 2018 turn to optimizing over trained ML models; it is now her most visible software.
  - SW5 is formulation theory driven by that ML turn.
- Tree-ensemble Bayesian optimization sits inside SW4 because it reuses the same formulations.

### SW1. Piecewise-linear relaxations for pooling problems and APOGEE (2009–2011), closed by the 2018 complexity paper

**Works**:
- Gounaris, Misener, Floudas, *Ind. Eng. Chem. Res.* 48(12):5742–5766, 2009. DOI 10.1021/ie8016048
- Misener & Floudas, *Ind. Eng. Chem. Res.* 49(11):5424–5438, 2010. DOI 10.1021/ie100025e
- Misener, Gounaris & Floudas, *Comput. Chem. Eng.* 34(9):1432–1456, 2010. DOI 10.1016/j.compchemeng.2010.02.014
- **Misener, Thompson & Floudas, APOGEE, *Comput. Chem. Eng.* 35(5):876–892, 2011. DOI 10.1016/j.compchemeng.2011.01.026**
- Follow-up: Baltean-Lugojan & Misener, *J. Global Optim.* 71(4):655–690, 2018. DOI 10.1007/s10898-017-0577-y

**What I read**:
- The APOGEE author version (Spiral, dated 21 December 2010): abstract, §1, the §5 discussion, §6 and §7.
- The JOTA 2010 author version: abstract and introduction.
- The 2016 essay, in full.
- The 2018 JOGO paper: abstract only.
- The 2009–2010 *I&ECR* papers: **not read**.

| Dimension | Content |
|---|---|
| **Origin** | Her 2016 essay on Floudas [stated, primary]: "one of his more recent intuitions was that piecewise linear underestimators seemed to be effective in solving the pooling problem [117-119]". Reference 117 is Meyer & Floudas 2006 (generalized pooling); 118–119 are her own 2009 and 2011 papers. So the PhD started from **the advisor's empirical intuition and his group's earlier piecewise work**. Her first conference talk was "Computational Comparison of Piecewise Linearization Schemes in Gas Lifting and Pooling Operations" (AIChE, 11/2008; CV P01). [practice, primary] |
| **Why then** | The APOGEE abstract names one trigger [stated, primary]: the logarithmic scheme was "inspired by recent work proposing models with a logarithmic number of binary variables for piecewise linear continuous functions, piecewise linear functions, and lower semicontinuous functions [Vielma and Nemhauser, 2010, Vielma et al., 2010a]". The extended pooling problem used a then-current regulation, the EPA "Title 40 Code of Federal Regulations Part 80.45: Complex Emissions Model". [inferred] CPLEX 12.x had made large MILP relaxations routine on a single workstation. |
| **Key insight** | Relax the bilinear terms of a pooling problem piecewise, through a MILP that switches under- and over-estimators on each segment. Then judge any relaxation **inside the whole global-optimization algorithm**, not at an isolated root node. APOGEE author version [stated, primary]: "our goal is to design the best overall algorithm that can address any pooling problem, so we are interested in the performance of the two relaxations when they are incorporated into the APOGEE algorithm rather than in an isolated root node relaxation." She contrasts this with "previous work that isolates the performance of a single MILP". |
| **Minimum evidence** | [practice, primary] 25 benchmark pooling problems (standard, generalized and EPA-extended). Each was solved with the linear and the logarithmic scheme at NP = 3, 4, 5, 6, 8, 12 and 16 partitions, with a 7200 CPU s limit. Findings: the logarithmic scheme "is particularly advantageous for higher partitioning levels", from NP = 8 up by their Table 8 counts. But "the global optimization algorithm seems to converge fastest with smaller partitioning levels (e.g., NP = 3, 4, 5) where there is an advantage in using the linear partitioning scheme". And "guessing the right partition is not a crucial element of our process". |
| **Abandoned paths** | [practice, primary] The paper's own novelty was not adopted: "three of the very large-scale problems (i.e., Meyer 10, Meyer 15, and EPA Large R1) have numerical difficulty with the logarithmic scheme and our goal is that the solver APOGEE should be as stable as possible … Therefore, we will continue using the linear relaxation scheme to solve pooling problems." Later, GloMIQO switched the piecewise scheme itself off by default (SW2). |
| **Reception** | [observed, secondary] Scholar: 215 (the 2009 review), 196 (I&ECR 2009), 185 (APOGEE). Her essay says the link between the NLP pooling problem and its MIP approximations was "further unpacked" by Dey & Gupte, "Analysis of MILP Techniques for the Pooling Problem", *Oper. Res.* 63(2):412–427, 2015, DOI 10.1287/opre.2015.1357 (not read). Others took up the linear-versus-logarithmic question again: Castro, Liao & Liang, "Comparison of mixed-integer relaxations with linear and logarithmic partitioning schemes for quadratically constrained problems", *Optim. Eng.* 23(2):717–747, 2022, DOI 10.1007/s11081-021-09603-5 (title checked via Crossref; **not read**). |
| **Closing the loop, eight years later** | Her essay again [stated, primary]: "still Chris would push me: Why did these piecewise approximations work so well? How could we eliminate the computational dependence on parameters? Actually, thanks to work with Radu Baltean-Lugojan [127], I finally have a first answer to these questions Chris asked me eight years ago". Reference 127 is the Optimization Online preprint of 22 May 2016. The essay cites it as "A parametric approach to the pooling problem"; the record is now titled "Piecewise Parametric Structure in the Pooling Problem – from Sparse Strongly-Polynomial Solutions to NP-Hardness". It appeared in *J. Global Optim.* (received 5 February 2017, accepted 8 October 2017). Its abstract (Springer) [practice, primary]: "The structure uncovered in this approach validates Professor Christodoulos A. Floudas’ intuition that pooling problems are rooted in piecewise-defined functions." |
| **Method it shows** | [inferred; each step is documented in the sources above] **Take an empirical intuition seriously, test it holistically, ship the stable variant, and keep asking "why" until there is a structural explanation.** (1) Start from a heuristic intuition that works, here piecewise relaxations for pooling. (2) Compare variants inside the full algorithm, on instances of application size. (3) Adopt the robust variant even when your own novelty loses. (4) Years later, explain the empirical success structurally, through parametric analysis and the complexity boundary. |

### SW2. Edge-concave and piecewise-linear relaxations for MIQCQP (2012) and the GloMIQO solver (2012/2013)

**Works**:
- R. Misener, C. A. Floudas, *Math. Program.* 136(1):155–182, 2012. DOI 10.1007/s10107-012-0555-6 (received 8 March 2011; accepted 4 October 2011; online 24 May 2012)
- **R. Misener, C. A. Floudas, "GloMIQO: Global mixed-integer quadratic optimizer", *J. Global Optim.* 57(1):3–50, 2013. DOI 10.1007/s10898-012-9874-7** (received 18 November 2011; accepted 10 February 2012; online 7 March 2012)
- Follow-up: R. Misener, J. B. Smadbeck, C. A. Floudas, GloMIQO 2, *Optim. Methods Softw.* 30(1):215–249, 2015. DOI 10.1080/10556788.2014.916287 (**not read**)

**What I read**: the Spiral author manuscripts.
- *Math. Program.* 2012: abstract, §1, §4.1, §4.3, §5 and acknowledgments.
- GloMIQO: §1, §2, §3.3.4, §3.6, §4 (set-up and aggregate results), §5 and acknowledgments. Its header says "Received: February 8, 2012", probably the date of the revision.
- The published versions and the online supplement were **not read**; they may differ.

| Dimension | Content |
|---|---|
| **Origin** | Three primary sources [stated]. (1) The 2016 essay: "In 2008, when Chris told me that my early-stage Ph.D. assessment needed a promise to write and publicly release a global MINLP solver, I told him he was being unreasonable. He said to do it anyway; and I must have made a face, because I remember him telling me sharply: "you will not roll your eyes at your advisor!" He was right in the end, and we released first GloMIQO [131] and then ANTIGONE [132] as global optimization solvers in the modeling language GAMS." (2) The edge-concave line extended Meyer & Floudas: "One of my projects extended the Meyer and Floudas [130] methodology to develop multiterm underestimators for bilinear functions [125]". She recalls emailing Floudas "good news (regarding facets of bilinear functions)" and quotes his reply of 12 March 2011. (3) The reformulation idea. The GloMIQO acknowledgments thank "Benoit Chachuat for a long conversation that sparked our reformulation strategies." |
| **Why then** | [stated context; the reading is inferred] The theory of edge-concave envelopes already existed in her own group (Meyer & Floudas, *Math. Program.* 2005; reference 130 of the essay). Her pooling work supplied large process-network test cases. The competitor landscape was moving (GloMIQO §2): "SCIP was originally developed as an mixed-integer programming (MIP) solver, but was recently extended to MIQCQP … SCIP offers the most interesting comparison to GloMIQO because it helps clarify the trade-offs associated with our constituent algorithmic components". GAMS supplied free licences and the GMO API, and vendors donated competitor licences. Everything ran on one quad-core workstation. |
| **Key insight** | **Find structure the user did not declare, exploit it, and hand back the answer in the user's own terms.** GloMIQO reformulates the user's input and detects "special structure including convexity and edge-concavity". It adds facets of low-dimensional (n ≤ 3) edge-concave aggregations that dominate the termwise McCormick relaxation, and then branches and bounds. In her own later words [ASR captions, 12:44]: "Adding these equations which were redundant in the original problem formulation tightened the relaxation. This was already known. But what we did was that we actually um found ways of getting these equations." The paper's claim [stated, primary]: "GloMIQO is on the leading edge of integrating reformulation techniques that can be implemented generically and applied universally." |
| **Minimum evidence** | [practice, primary] *Math. Program.* 2012: 43 experiments (point packing, process networks, GLOBALLib) on one workstation, "a 7200 CPU s time limit", with CPLEX 11.1, SNOPT 5.3 and GAMS 23.6. Verdict: "while we find strong evidence for the value of low-dimensional edge-concave aggregations in any MIQCQP, the piecewise-linear underestimation scheme is best applied to specific classes of MIQCQP (e.g., process networks problems with many nonlinearly-participating variables)". GloMIQO: 399 test problems against BARON 10.1.2, Couenne 0.4, LindoGLOBAL 6.1.1.588 and SCIP 2.1.0. "GloMIQO is the fastest solver for 68% of the test cases and can address 81% of the test cases within the time limit." |
| **How the evidence was policed** | [practice, primary] Three safeguards. (1) An independent feasibility check: "After solving each of the 399 test cases using GAMS, a Perl script asserted the feasibility of the solution returned by each solver". Infeasible answers were relabelled as failures; "Couenne 0.4 returns an infeasible point in over half of the 399 test cases". (2) One parameter setting for all problems: "parameter values and algorithmic options are not changed between problems". (3) Interleaved runs, "so as minimize [sic] the effect of fluctuating machine load", following Dolan and Moré. The *Math. Program.* paper also compares relaxations inside the full algorithm: "This holistic view makes the comparisons fairly subtle but also allows us to draw better-informed conclusions." |
| **What the evidence said against her** | [stated, primary] GloMIQO and SCIP "represent an interesting algorithmic trade-off": SCIP was faster on the smaller instances. "We do not know if it would be possible for GloMIQO to dynamically abandon its more elaborate approach under circumstances where a SCIP-like algorithm is more effective or if a slower solution time on the smaller problems is a price we pay for addressing the exceptionally large problems." On pooling, the special-purpose APOGEE "regurally [sic] outperforms the more generic work presented here" (*Math. Program.* 2012). |
| **Abandoned paths** | [practice, primary; observed] The piecewise-linear relaxations of SW1 became opt-in: "However, for problems that can converge without the piecewise-linear underestimators, the convergence is generally faster when they are excluded [99]. Therefore, the default in GloMIQO is not to use the piecewise-linear relaxations … Users are strongly encouraged to experiment with activating the piecewise-linear options for models that do not solve within a reasonable amount of time". The standalone GloMIQO product ended in GAMS 40 (2022), because ANTIGONE subsumes it. |
| **Reception** | *J. Global Optim.* Best Paper of 2013; W. David Smith, Jr. Graduate Student Paper Award 2014 for both papers (CV) [stated]. Scholar: GloMIQO 280, *Math. Program.* 2012 165. The ANTIGONE paper lists published applications of GloMIQO [stated]: crystal orientation, multiperiod blend scheduling, network flow, water network design and cutting ellipses. In the 2023 lecture she credits this work with getting her the Imperial Computing job [stated, ASR]. |
| **Method it shows** | [inferred] **Automate the expert's reformulation tricks inside the solver, then benchmark like an auditor.** Encode tightening tricks that experts already know but apply by hand as automatic structure detection. Check every competitor's answer independently. Use one parameter setting for everything. Report where the approach loses, and why. |

### SW3. ANTIGONE (2013/2014)

**Works**:
- **R. Misener, C. A. Floudas, "ANTIGONE: Algorithms for coNTinuous / Integer Global Optimization of Nonlinear Equations", *J. Global Optim.* 59(2–3):503–526, 2014. DOI 10.1007/s10898-014-0166-2** (received 10 April 2013; accepted 21 February 2014; online 20 March 2014)
- Stepping stone: R. Misener, C. A. Floudas, the signomial framework, *J. Optim. Theory Appl.* 161(3):905–932, 2014. DOI 10.1007/s10957-013-0396-3 (**not read**)

**What I read**: the Spiral author manuscript: §1, §2, the opening of §3 and §3.1, §5 (set-up and selected results), and §6. The 177-page supplement and the published version were **not read**.

| Dimension | Content |
|---|---|
| **Origin** | [stated, primary] The 2008 solver promise (SW2, essay). The manuscript: "ANTIGONE integrates our previous MIQCQP [102, 104, 107] and MISO [105] work into a cohesive whole; ANTIGONE further generalizes the computational framework to include exponential and logarithmic functions." The essay lists what it took from the Floudas group: "αBB [80], generalised geometric programming [133, 134], edge-concave underestimators [130, 135], and automatic transformations for process networks problems [125, 131]". Written at Princeton and finished after her move: the manuscript gives her "Present address" as Chemical Engineering at Imperial, and its funding includes "the Royal Academy of Engineering Research Fellowship to R.M." |
| **Why then** | [stated context; the reading is inferred] GloMIQO had just been released commercially through GAMS 23.8, which gave a distribution channel; ANTIGONE was "first available in GAMS 24.1". Large public test libraries now existed, including GLOBALLib, MINLPLib, minlp.org and PrincetonLib. The paper itself names the trend it was built for: "an accelerating trend towards developing good underestimators for very specific terms". |
| **Key insight** | [stated, primary] The contribution is the **architecture**, not any single relaxation: "Section 3 may be read as a type of critical literature review; the intellectual contribution is the way ANTIGONE ties together its many constitutive algorithms." Term types are C++ classes in an inheritance hierarchy, so "we anticipate further advances in the area of term-specific underestimators and have architected ANTIGONE accordingly." |
| **Minimum evidence** | [practice, primary] 2,571 test problems × 5 solvers = 12,855 runs, each with a 7200 s limit. The competitors were BARON 12.7.3, Couenne 0.4, LINDO 8.0 and SCIP 3.0, "the latest versions as of February 2014", on a Xeon X5650 with 24 GB RAM. "No other parameters were altered from default." The same Perl feasibility check as in GloMIQO was used, and performance profiles came from the GAMS PAVER tools. Reported strengths: ANTIGONE is "particularly good at coming to a finite optimality gap for difficult problems; this is useful for contexts where globally optimizing a problem is beyond the reach of current technology but there is still a need to understand bounds on the global solution". It was "unusually strong" on the 115 minlp.org problems. |
| **What the evidence said against her** | Her own diagnosis [stated, primary]: "it is evident that the strongest component of ANTIGONE is in addressing problems with quadratic nonlinearities … ANTIGONE derives the core of its strength from quadratic instances." An independent benchmark [observed, primary document]: Kronqvist, Bernal, Lundell & Grossmann, "A review and comparison of solvers for convex MINLP", *Optim. Eng.* 20:397–455, 2019, DOI 10.1007/s11081-018-9411-8, tested ANTIGONE 1.1 under GAMS 25.1.2. ANTIGONE found solutions within 0.1% for 275 problems but verified optimality for only 236. The authors wrote: "Since ANTIGONE is a global solver without a user-selected convex strategy, it might fail to recognize some of the problems as convex, and therefore, generate weaker relaxations." |
| **Abandoned paths** | [practice, primary; the reasons are inferred, not sourced] The record has no ANTIGONE 2 and no later algorithm paper. The GAMS manual is still dated 16 April 2013 [observed]. Her later solver work is open-source Python on Pyomo: SUSPECT for convexity and structure detection (2020), and GALINI (EPSRC fellowship 2017–22). Why she left the commercial C++ line is **not stated**. The nearest evidence is her stated move toward "data-driven constraints" (§1.10) and GALINI's published design choice of extensibility over performance (§1.9). |
| **Reception** | [stated/observed] Her most cited work: Scholar 742, Semantic Scholar 568 (24 influential), Crossref 457. GAMS has distributed it from 2013 to the present. She notes one use she had no part in, Boukouvala, Hasan & Floudas's grey-box methodology: "One application of ANTIGONE (although I had nothing to do with it)". Her own GALINI preprint benchmarks against "ANTIGONE, Baron, Couenne and SCIP included in GAMS 31.1". |
| **Method it shows** | [inferred] **Architect for the next paper, not this one.** Treat the solver as an extensible framework whose units (term classes) can absorb other people's future relaxations. When global optimality is out of reach, measure and report the finite gap. Say plainly which problem class carries the results. |

### SW4. Optimizing over trained tree ensembles and neural networks: gradient-boosted trees (2018/2021) → ENTMOOT (2020/2021) → OMLT (2022) → tree-kernel Bayesian optimization (2022, 2025)

**Works**:
- M. Mistry, D. Letsios, G. Krennrich, R. M. Lee, R. Misener, *INFORMS J. Comput.* 33(3):1103–1119, 2021. DOI 10.1287/ijoc.2020.0993; arXiv:1803.00952
- A. Thebelt, J. Kronqvist, M. Mistry, R. M. Lee, N. Sudermann-Merx, R. Misener, ENTMOOT, *Comput. Chem. Eng.* 151:107343, 2021. DOI 10.1016/j.compchemeng.2021.107343; arXiv:2003.04774
- **F. Ceccon, J. Jalving, J. Haddad, A. Thebelt, C. Tsay, C. D. Laird, R. Misener, OMLT, *J. Mach. Learn. Res.* 23(349):1–8, 2022; arXiv:2202.02414**
- A. Thebelt et al., NeurIPS 2022; arXiv:2207.00879
- T. Boyne et al., BARK, ICML 2025; arXiv:2503.05574

**What I read**:
- OMLT in full (8 pages; arXiv v2, which is the JMLR version).
- The *INFORMS J. Comput.* paper (arXiv v3): abstract, the related-work paragraph, acknowledgments.
- ENTMOOT (arXiv v3): abstract, the opening of §1, the Gurobi comparison paragraph, acknowledgments.
- The tree-kernel BO paper and BARK: abstracts only.

| Dimension | Content |
|---|---|
| **Origin** | The trigger was industrial [practice, primary]. The *INFORMS J. Comput.* acknowledgments thank "BASF SE" and her EPSRC fellowship (EP/P016871/1). The CV lists a 2017 BASF research project (£40k), then a 2019–22 BASF PhD studentship, "Global optimisation with ensemble machine learning models". The paper's abstract motivates the problem "e.g., for picking the best chemical process catalyst" and gives the users' reason: "Decision makers may wish to optimize discrete models to repurpose legacy predictive models". Her own account [stated, primary; ASR captions, 28:03–29:04]: Mistry developed the formulation (the caption says "over neural networks", but the context is regression trees). Then "a lot of people got excited about Mitten's [sic, ASR] work". Thebelt and the BASF collaborators "developed this blackbox optimization toolmoot [sic, ASR: tool ENTMOOT] which uh is now in use at the chemicals company uh BSF [sic, ASR: BASF] for design of experiments. Then we decided that wasn't enough." |
| **Why then** | Partly [stated]: she attributes the turn to her move into Computing [ASR captions, 46:34]: "investigations into datadriven constraints that basically came from being in a computer science department and being introduced to some of this stuff". The rest is [inferred]: tree ensembles were already BASF's working models. MIP formulations of trained ReLU networks and tree ensembles were appearing at the same time; OMLT cites Fischetti & Jo 2018, Anderson et al. 2020 and Mišić 2020. The EPSRC fellowship paid for software engineering, and the Pyomo developers at Sandia became co-authors. The 2018 Dagstuhl summary she co-wrote already says: "Many machine learning challenges can be formulated as MINLP. Also, machine learning can significantly improve MINLP solver software." |
| **Key insight** | **A trained model is just another structured set of constraints.** Write it into the optimization problem, exploit its structure (piecewise-constant trees, piecewise-linear ReLU networks) rather than treating it as a black box, and then make the formulations interchangeable. OMLT [stated, primary]: "OMLT automates the otherwise tedious and error-prone task of translating already-trained NN and GBT models into optimization formulations suitable for solver software." And: "The literature often presents these different optimization formulations as competitors, e.g., our partition-based formulation competes with the big-M formulation for ReLU NNs … In OMLT, competing optimization formulations become alternatives: users can switch between the Section 3 formulations and find the best for a specific application." In Bayesian optimization the same move is applied to the acquisition function. The tree-kernel paper (abstract) develops "a compatible optimization formulation for the acquisition function"; BARK (abstract): "Our tree-based approach enables global optimization over the surrogate, even for mixed-feature spaces." |
| **Minimum evidence** | [practice, primary] *INFORMS J. Comput.*: "several heuristic methods to find feasible solutions, and an exact, branch-and-bound algorithm leveraging structural properties of the gradient-boosted trees and penalty functions", tested on a "concrete mixture design instance and a chemical catalysis industrial instance". ENTMOOT proves the acquisition step globally optimal and benchmarks against BO frameworks, including RoBO, SMAC3, Scikit-Optimize and CMA-ES. OMLT shows one ReLU network switched between complementarity, big-M and partition formulations "with 248, 308, and 428 constraints, respectively". The paper describes the switch as a one-line change; the comparison symbol before "1 line of code" was lost in text extraction. |
| **What the evidence said against her** | ENTMOOT [stated, primary]: "While Gurobi 9 is still the best choice for small and moderate instances, i.e. instances that commonly occur in design of experiments, we want to highlight that algorithmic elements exploiting the underlying structure of tree-based models can help when scaling the optimization efforts." OMLT concedes that its MNIST verification examples "could also be addressed effectively with dedicated NN verification tools, e.g., Beta-CROWN". The *INFORMS J. Comput.* paper positions itself narrowly: "The main difference with our work is that we are more focused on the optimization side." |
| **Abandoned paths** | [practice, primary] (1) The "risk control" framing of arXiv v1 (2018) left the title by v3 (2019); see §1.9. (2) ENTMOOT's own tree formulation moved into OMLT: "The OMLT 1.0 GBTBigMFormulation uses the Mišić (2020) and Mistry et al. (2021) formulation and thereby simplifies our GBT-based black-box optimization tool ENTMOOT". ENTMOOT was later rebuilt: an "entmoot-v2" branch, with Thebelt, Sudermann-Merx and Boyne as the current authors. |
| **Reception** | [stated/observed] COIN-OR Cup 2022 for OMLT (CV). Scholar: OMLT 232, *INFORMS J. Comput.* 99, ENTMOOT 80, the NeurIPS 2022 tree kernels 26, BARK 7. OMLT has 349 GitHub stars and 77 forks; her 2023 figure was 20,000 downloads a month (§1.8). BASF co-authored the BO framework BoFire (*JMLR* 2025) with her group. BCS Roger Needham Award 2023 (announced 11 December 2023), "in recognition of her work identifying and solving fundamental computer science research challenges at the intersection of computational optimisation and machine learning". That wording is as extracted from the BCS page by WebFetch. |
| **Method it shows** | [inferred] **Turn the partner's model into the solver's problem, then harden it into a tool.** (1) Take the trained model an industrial partner already trusts. (2) Write it as constraints and exploit its structure for exact global optimization. (3) Generalize from one model class (trees) to several (neural networks, GNNs) behind a common interface. (4) Invest in software engineering (CI, documentation, COIN-OR) so formulations become alternatives the user can select. In her words [ASR captions, 29:04]: "one we tried to make this uh real at BSF [sic, ASR] and two we tried to make this real with respect to doing reasonable software engineering." |

### SW5. Between big-M and convex hull: P-split and partition-based formulations (2021–2026)

**Works**:
- J. Kronqvist, R. Misener, C. Tsay, CPAIOR 2021. DOI 10.1007/978-3-030-78230-6_19; arXiv:2101.12708
- C. Tsay, J. Kronqvist, A. Thebelt, R. Misener, NeurIPS 2021; arXiv:2102.04373
- **J. Kronqvist, R. Misener, C. Tsay, *Math. Program.* 218(1–2):57–94, 2026. DOI 10.1007/s10107-025-02232-1; arXiv:2202.05198**
- Antecedent: E. Botoeva et al., AAAI 2020. DOI 10.1609/aaai.v34i04.5729

**What I read**: abstracts (arXiv and Springer), version histories and Springer dates. Full texts were **not read**.

| Dimension | Content |
|---|---|
| **Origin** | [stated, primary; ASR captions, 21:25–23:27] The problem came from a neighbouring field. Lomuscio's verification group introduced it to her: "maybe I don't want to solve the forward problem all the time where I set the x's and I figure out the y's. Maybe I want to set the y's and figure out the x's." She credits the partition idea to her research fellow Kronqvist: "What if instead um I break things up and I partition the x's? … he was able to get these tighter variable bounds uh which was brilliant. Um so he won best paper in a uh a conference that we have." She presents it as his idea, not hers. |
| **Why then** | [inferred] MIP formulations of trained ReLU networks were an active topic. The big-M formulation is weak, while convex-hull (extended) formulations are large; OMLT cites Anderson et al. 2020. Kronqvist arrived as a Newton Fellow in 2019 with expertise in convex MINLP and disjunctive cuts; their *Optim. Eng.* 2021 paper won the Rosenbrock Prize. Tsay arrived in 2020. The AAAI 2020 verification work had just made bound tightening for ReLU networks concrete. |
| **Key insight** | [practice, primary; CPAIOR abstract] Interpolate between the two textbook extremes with a single parameter: "The proposed "P-split" formulations split convex additively separable constraints into P partitions and form the convex hull of the partitioned disjuncts. Parameter P represents the trade-off of model size vs. relaxation strength." The NeurIPS 2021 abstract: "At one extreme, one partition per input recovers the convex hull of a node, i.e., the tightest possible formulation for each node. For fewer partitions, we develop smaller relaxations that approximate the convex hull, and show that they outperform existing formulations." Her talk title for this theme is "Between formulations or: How I Learned to Stop Worrying and Love Parameters" (HUGO 2022 plenary; MIT, Princeton and Cornell seminars; CV K20, S33, S41, S42). The MIT version lists joint work with Campos and Parpas (partial Lasserre relaxations) and with the OMLT team. That she treats these as one theme is my reading [inferred]. |
| **Minimum evidence** | [practice, primary] Theory (CPAIOR abstract): "under certain assumptions, the relaxations form a hierarchy starting from a big-M equivalent and converging to the convex hull". Computation: K-means clustering, P_ball problems and ReLU networks (CPAIOR). The journal version uses 344 instances and adds semi-supervised clustering: "For many of the test problems, P-split formulations are solved with a similar number of explored nodes as the convex hull formulation, while reducing the solution time by an order of magnitude and outperforming big-M both in time and number of explored nodes." |
| **Abandoned paths** | [practice, primary] None documented. The journal version took from February 2022 (arXiv v1) to April 2024 (received) to June 2025 (online); the reason for the gap is **not known**. The journal version adds a generalization to nonconvex disjuncts, which the CPAIOR abstract lacks: "we generalize the results for the case with nonconvex constraints within the disjuncts". |
| **Reception** | [stated/practice] CPAIOR 2021 Distinguished Paper Award, 1 of 30 accepted papers (CV). Scholar: CPAIOR 30, NeurIPS 2021 146, *Math. Program.* 2025 27. Shipped as `ReluPartitionFormulation` in OMLT 1.0 (dense layers only). |
| **Method it shows** | [inferred] **When two classical formulations each win somewhere, build the parameterized family between them, prove its hierarchy, and let the parameter (and the user) choose.** This is the theory behind OMLT's "competitors become alternatives". |

### Cross-index: candidate methods for Phase 2

All candidates are [inferred] from the anatomies above.

| Candidate method | Evidence across works | Stated support |
|---|---|---|
| M1 Detect and exploit structure the user did not declare | SW2, SW3; convexity detection (Mistry 2016, SUSPECT 2020); symmetry detection (2017–19); GNN symmetry breaking (2023) | "figuring out how to relax better" (lecture, 05:37); structure detection as "insider information" (lecture, 09:10–09:41) |
| M2 Judge components inside the whole algorithm and ship the stable variant | SW1 (linear over logarithmic); SW2 (piecewise off by default; holistic comparison) | The APOGEE and *Math. Program.* 2012 quotes above |
| M3 Benchmark like an auditor: independent feasibility checks, one parameter setting, losses admitted | SW2, SW3 (the Perl checker; "We do not know if…"; strength only on quadratic problems) | — |
| M4 Software as the unit of publication: release, extend, harden | APOGEE, GloMIQO, ANTIGONE, SUSPECT, GALINI, OMLT, ENTMOOT; a code link per paper | CV S01–S03; COIN-OR Cup; "reasonable software engineering" (lecture) |
| M5 Turn a partner's data-driven model into a MINLP | SW4; warped-GP constraints (*Math. Program.* 2022); GNNs (2023–25) | Lecture 28:03–29:34; the Dagstuhl summary |
| M6 Parameterized families between extremes | SW5; partial Lasserre (2023); neural-network partitions (2021) | Talk title "How I Learned to Stop Worrying and Love Parameters" |
| M7 Choose directions through collaborators ("opportunistic") | The topic waves in §1.2; §1.9 item 10 | Lecture 46:04–46:34 |

---

## 3. Contradictions (kept, not reconciled)

1. **She says proofs bore her, yet she publishes a steady stream of theory.**
   - Stated [ASR captions, 30:35]: "if anybody needs uh uh sort of uh just a convergence proof or something to just work because you're going to use one of those components that I that I presented probably you got to find somebody else because it's boring and I'm not interested."
   - Practice:
     - the hierarchy proofs for P-split (SW5);
     - the strongly-polynomial/NP-hardness boundary of the pooling problem (JOGO 2018);
     - approximation algorithms with performance guarantees (Letsios et al. 2018–21);
     - proofs of cut validity and dominance (Kronqvist & Misener 2021);
     - proofs of correctness and completeness for graph encodings (arXiv 2025).
   - The statement may target routine convergence proofs for components rather than structural theory. That reading is [inferred].
2. **She argued for piecewise-linear relaxations, then shipped them switched off.**
   - Her PhD papers and APOGEE argue for piecewise relaxations.
   - Her essay records that Floudas "absolutely insisted that his piecewise linear underestimation technique for bilinear terms [117-119] was not relevant unless it was effectively applied to real-world instances".
   - Yet GloMIQO excludes them by default ("the default in GloMIQO is not to use the piecewise-linear relaxations").
   - And the *Math. Program.* 2012 paper shows her own special-purpose APOGEE beating the generic solver on pooling.
3. **APOGEE's novelty is not its recommendation.** The paper's novelty is the logarithmic formulation; the paper recommends the linear one.
4. **The pooling preprint changed title.**
   - The 2016 essay cites "A parametric approach to the pooling problem" (Optimization Online 2016/05/5457), as do her 2016 talk titles (CV I08, I11).
   - The same Optimization Online record now reads "Piecewise Parametric Structure in the Pooling Problem – from Sparse Strongly-Polynomial Solutions to NP-Hardness".
   - This is a retitling, not a conflict of fact.
5. **The lecture caption and the paper disagree on Mistry's formulation.** At 28:03 the caption says "a set of optimization constraints over neural networks". The paper (*INFORMS J. Comput.* 2021) and the surrounding sentences concern regression trees. Whether this is a slip of the tongue or an ASR error is unresolved.
6. **ANTIGONE's name has two expansions.**
   - The title: "…Global Optimization of Nonlinear **Equations**".
   - The manuscript introduction: "ANTIGONE (Algorithms for coNTinuous / Integer Global Optimization of Nonlinear **Expressions**; first available in GAMS 24.1)".
7. **GloMIQO's dates differ across records.**
   - The author manuscript says "Received: February 8, 2012"; Springer says received 18 November 2011 and accepted 10 February 2012.
   - The CV and Scholar date GloMIQO 2013 (the print issue); Springer published it online on 7 March 2012.
   - The CV lists the award as "Journal of Global Optimization Best Paper of 2013".
8. **The CV is incomplete.** The CV of 3 December 2025 omits the P-split paper, published online in June 2025, and two well-cited preprints appear in it only as talk titles (§0).
9. **Author orders differ** between the CV and Crossref for J55 (Partial Lasserre) and C04 (AAAI 2020) (§1.3).
10. **"Eight years in Computing" against a 2014 start.** In 2023 the lecture thanks people she worked with over "the last eight years in department of computing", but the CV dates her Computing lectureship from 2014, which makes nine. Pistikopoulos, at the same event, said "eight nine years now". Minor.

---

## 4. Gaps (what I could not find or did not read)

- **Full texts not read**:
  - the published versions of all signature works (I read the Spiral author versions, which may differ);
  - the GloMIQO 2 paper (*Optim. Methods Softw.* 2015) and the signomial paper (*J. Optim. Theory Appl.* 2014);
  - the 2009–2010 *I&ECR* papers;
  - the full P-split and NeurIPS 2021 papers;
  - the Bayesian-optimization papers beyond their abstracts;
  - the 2023 Misener & Biegler perspective;
  - her PhD thesis (Princeton 2012);
  - the theses of Baltean-Lugojan (2019) and Kouyialis (2019), both found in Spiral;
  - the ANTIGONE and GloMIQO online supplements.
- **The talk "Architecting ANTIGONE: Design Choices and Tradeoffs"** (ZIB MODAL workshop, 11/2013): no slides or video found. It would be the best primary source on the design alternatives ANTIGONE dropped.
- **"Deterministic Global Optimisation at CPSE: Models, Algorithms, and Software"** (CPSE Newsletter 10, 2014; CV G1): not located.
- **Reasons, for which no public source was found**:
  - why she left the commercial ANTIGONE line for open-source Python solvers;
  - why the general GALINI paper and the NN-scored SDP-cut paper never appeared in journals;
  - why the P-split journal version was only submitted in 2024.

  No rejected submissions are documented.
- **Independent benchmarks after 2019**: Mittelmann's pages were unreachable. I read only one independent comparison, Kronqvist et al. 2019, which covers convex MINLP only.
- **OpenAlex** (no API key) and **Semantic Scholar author-level metrics** (empty author search): not used. The citation landscape rests on Scholar.
- **APOGEE**: the distribution site is dead. Whether an archived copy exists was not checked, because the Wayback Machine returned HTTP 429.
- **Recent statements**: the June 2026 SIAM OP26 plenary on "Optimizing over graphs" was not checked for slides or video.
- **Retractions and errata**: no search beyond the Crossref metadata.

---

## 5. Sources

**Primary** (by Misener, her group, or her own records)

1. R. Misener, Curriculum vitae, updated 3 December 2025, 32 pp., http://www.doc.ic.ac.uk/~rmisener/Misener_CV.pdf (read in full) — primary
2. R. Misener, homepage "Optimization Models, Algorithms, and Software", http://wp.doc.ic.ac.uk/rmisener/ (accessed 2026-10-10) — primary
3. R. Misener, "Just relax, Or: How I'm bad at my own algorithmic advice.", Imperial inaugural lecture, video published 13 March 2023, https://www.youtube.com/watch?v=dN860HNsAs0. Auto-captions saved as `../sources/talks/2023-03-13-just-relax-inaugural-lecture-asr.md`. Also contains Pistikopoulos's vote of thanks [observed] — primary
4. R. Misener, "Christodoulos Achilleus Floudas", *SIAG/OPT Views and News* 24(1):12–16, October 2016, https://siagoptimization.github.io/assets/views/ViewsAndNews-24-1.pdf (read in full) — primary
5. R. Misener, C. A. Floudas, GloMIQO, author manuscript, Spiral hdl:10044/1/19682. Published as *J. Global Optim.* 57(1):3–50, 2013, DOI 10.1007/s10898-012-9874-7 — primary
6. R. Misener, C. A. Floudas, MIQCQP piecewise-linear and edge-concave relaxations, author manuscript, Spiral hdl:10044/1/10938. Published as *Math. Program.* 136(1):155–182, 2012, DOI 10.1007/s10107-012-0555-6 — primary
7. R. Misener, C. A. Floudas, ANTIGONE, author manuscript, Spiral hdl:10044/1/15506. Published as *J. Global Optim.* 59(2–3):503–526, 2014, DOI 10.1007/s10898-014-0166-2 — primary
8. R. Misener, J. P. Thompson, C. A. Floudas, APOGEE, author version dated 21 December 2010, Spiral hdl:10044/1/29737. Published as *Comput. Chem. Eng.* 35(5):876–892, 2011, DOI 10.1016/j.compchemeng.2011.01.026 — primary
9. R. Misener, C. A. Floudas, "Piecewise-Linear Approximations of Multidimensional Functions", author version, Spiral hdl:10044/1/31814. Published as *J. Optim. Theory Appl.* 145(1):120–147, 2010, DOI 10.1007/s10957-009-9626-0 — primary
10. M. Mistry, D. Letsios, G. Krennrich, R. M. Lee, R. Misener, arXiv:1803.00952v3. Published as *INFORMS J. Comput.* 33(3):1103–1119, 2021, DOI 10.1287/ijoc.2020.0993 — primary
11. A. Thebelt et al., ENTMOOT, arXiv:2003.04774v3. Published as *Comput. Chem. Eng.* 151:107343, 2021, DOI 10.1016/j.compchemeng.2021.107343 — primary
12. F. Ceccon et al., "OMLT: Optimization & Machine Learning Toolkit", *J. Mach. Learn. Res.* 23(349):1–8, 2022, arXiv:2202.02414v2 (read in full) — primary
13. R. Baltean-Lugojan, M. L. Bynum, F. Ceccon, C. Li, R. Misener, "GALINI: An extensible mixed-integer quadratically-constrained optimization solver", Optimization Online, 14 January 2021, https://optimization-online.org/2021/01/8207/ (read in part) — primary
14. R. Baltean-Lugojan, P. Bonami, R. Misener, A. Tramontani, "Scoring positive semidefinite cutting planes for quadratic optimization via trained neural networks", Optimization Online, 26 November 2018, https://optimization-online.org/2018/11/6943/ (abstract); and R. Baltean-Lugojan, R. Misener, Optimization Online, 22 May 2016, https://optimization-online.org/2016/05/5457/ (record page) — primary
15. P. Bonami, A. M. Gleixner, J. Linderoth, R. Misener (eds.), "Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization (Dagstuhl Seminar 18081)", *Dagstuhl Reports* 8(2):64–87, 2018, DOI 10.4230/DagRep.8.2.64 (executive summary, her talk abstract, the ML working group) — primary
16. arXiv abstract pages with version histories for 2101.12708, 2102.04373, 2202.05198, 2207.00879, 2503.05574, 2202.00060, 2211.06149, 2509.20247, 2610.03647, 2605.05382, 2506.07619 and 2505.23640, https://arxiv.org/abs/ (accessed 2026-10-10) — primary
17. Springer article pages (abstracts; received, accepted and online dates) for DOIs 10.1007/s10898-012-9874-7, 10.1007/s10107-012-0555-6, 10.1007/s10898-014-0166-2, 10.1007/s10898-017-0577-y, 10.1007/s10107-025-02232-1 and 10.1007/s11081-020-09551-6 — primary (publisher record)
18. GitHub organisation cog-imperial: the API listing of 33 public repositories, and the READMEs of OMLT, entmoot, galini and suspect, https://github.com/cog-imperial (accessed 2026-10-10) — primary (practice)

**Secondary and observed**

19. Google Scholar profile AQxtWHoAAAAJ, all 155 rows in citation order, https://scholar.google.com/citations?user=AQxtWHoAAAAJ (WebFetch, 2026-10-10) — secondary
20. DBLP person 04/8800 via SPARQL (`scripts/dblp_works.py`), 93 records, https://dblp.org/pid/04/8800.html — secondary
21. Crossref REST API: metadata for 37 DOIs and 15 bibliographic searches, https://api.crossref.org (2026-10-10) — secondary
22. Semantic Scholar Graph API: citation and influential-citation counts for ANTIGONE, GloMIQO and the 2012 *Math. Program.* paper, and the abstract of the 2022 GALINI pooling paper, https://api.semanticscholar.org — secondary
23. Unpaywall API: open-access locations for 13 DOIs (email parameter nuwa-skill@users.noreply.github.com), https://api.unpaywall.org — secondary
24. Spiral (Imperial) DSpace API: item and file metadata, including the theses of Baltean-Lugojan (hdl:10044/1/79281) and Kouyialis (hdl:10044/1/67897), both **not read**, https://spiral.imperial.ac.uk — secondary
25. arXiv author search for "Misener, Ruth" (46 preprints), https://arxiv.org/search/ — secondary
26. GAMS documentation: the ANTIGONE manual (current, version 54), https://www.gams.com/latest/docs/S_ANTIGONE.html; the GloMIQO manual (GAMS 30), https://www.gams.com/30/docs/S_GLOMIQO.html; the GAMS 40 release notes, https://www.gams.com/40/docs/RN_40.html — observed, secondary
27. J. Kronqvist, D. E. Bernal, A. Lundell, I. E. Grossmann, "A review and comparison of solvers for convex MINLP", *Optim. Eng.* 20:397–455, 2019, DOI 10.1007/s11081-018-9411-8 (the ANTIGONE passages read) — observed (independent peers)
28. BCS, "Professor Ruth Misener awarded the 2023 BCS Roger Needham Award", 11 December 2023, https://www.bcs.org/articles-opinion-and-research/professor-ruth-misener-awarded-the-2023-bcs-roger-needham-award/ (via WebFetch) — observed
29. Imperial College News (A. Idle), "Professor Ruth Misener Honoured with 2023 BCS Roger Needham Award", 20 December 2023, https://www.imperial.ac.uk/news/250395/professor-ruth-misener-honoured-with-2023/ (via WebFetch) — observed

**Identifier checked, text not read**:
- Dey & Gupte, *Oper. Res.* 63(2):412–427, 2015. DOI 10.1287/opre.2015.1357
- Castro, Liao & Liang, *Optim. Eng.* 23(2):717–747, 2022. DOI 10.1007/s11081-021-09603-5

**Could not be accessed**:
- OpenAlex: not run, because `OPENALEX_API_KEY` is not set.
- The plato.asu.edu benchmarks: connection failed.
- helios.princeton.edu/APOGEE: connection failed.
- The Wayback Machine availability API: HTTP 429.
