# Daniel P. Robinson: signature works and publication landscape (research agent 01)

- **Researcher**: Daniel P. Robinson. Lehigh University, Industrial and Systems Engineering (ISE), since 2019. Earlier: Johns Hopkins University (JHU), Applied Mathematics and Statistics (AMS), 2011–2019. Postdoctoral work at Oxford (with N. I. M. Gould) and Northwestern (with J. Nocedal). PhD in Mathematics, UC San Diego, 2007; committee chair Philip E. Gill.
- **Dimension**: signature works and the publication landscape (framework §二, agent 1; dissections follow framework §五).
- **Research date**: 2026-10-16
- **Sources consulted**: 39 (listed at the end). 30 are primary: his homepage and its archived publication and talk lists, his 2007 thesis, three Oxford/RAL report versions of his first paper, eight papers or preprints read in full text, two errata, arXiv version histories, his GitHub repositories, GALAHAD source headers, and his ORCID record. 9 are secondary: DBLP, OpenAlex, Semantic Scholar, Crossref metadata, the arXiv author search, and one WebSearch summary. **WebSearch calls used: 1.**
- **Local corpus**: `references/sources/papers/`, `talks/`, `essays/`, `software/` and `publications/` contain only `.gitkeep`. **None of the findings come from user-supplied material.** `private/` was not opened.
- **Sibling notes**: `02-methodology.md` and `06-trajectory.md` (same folder) were used only as leads, for example for the Curtis errata URLs and the Wayback snapshot URLs. Every identifier below was re-checked with a tool in this run, using DBLP SPARQL, Crossref, OpenAlex, Semantic Scholar, arXiv abstract pages, or the document itself.

### How the evidence was gathered (and what failed)

- **DBLP**: `scripts/dblp_works.py --name` found pid 20/8222 as the only matching person (85 records, 2010–2026, top co-authors René Vidal, Frank E. Curtis and Chong You). `--pid 20/8222` returned 43 articles, 21 conference papers and 21 informal (CoRR) records, 72 of them with DOIs. The records are saved in the scratch folder, not the repo.
- **Google Scholar**: the author search redirected to a Google login page (HTTP 302 to accounts.google.com), and none of his pages (homepage, Lehigh faculty page, OptML people page) links to a Scholar profile. A WebSearch did not surface one either. **No Scholar data is used.**
- **OpenAlex**: `OPENALEX_API_KEY` is **not set**, so `fetch_publications.py` was not run. One keyless works query by ORCID (127 works, sorted by citations) succeeded, and two single-work lookups also worked.
- **Semantic Scholar**: the author search splits him across at least four profiles linked to his DBLP name. The main one (id 1780452) has 93 papers, 3,016 citations and h = 30, and contains at least one paper by a different Robinson. Two follow-up requests returned HTTP 429.
- **arXiv**: the abstract and PDF pages worked. The author search is noisy: of its 148 hits, many are other Robinsons.
- **Full texts read** (all openly hosted): his thesis (eScholarship); Oxford NA reports 08/09 and 08/18 and RAL-TR-2009-001; the TRACE and adaptive-AL papers as PDFs hosted on Curtis's Lehigh site; arXiv 1507.01238 (v1 and v3 abstracts, v3 text), 1605.02633, 1602.07018, 2007.10525 and 2007.14951.
- **Could not reach**: Oxford eprints (connection failed); eScholarship landing page (HTTP 403, though the PDF itself downloaded); AD Scientific Index (403). The SIAM journal versions of the 2010 SQP papers are paywalled, so I read their report versions instead.

### Tag legend

- **[stated]**: said or written by Robinson, or in a text he co-signs (papers, abstracts, his homepage, his bio). Co-authored texts are marked "collective".
- **[practice]**: what the record shows he did (papers, dates, code, experiments, acknowledgments).
- **[observed]**: what others report about him or his work.
- **[inferred]**: my synthesis. Treat it as a hypothesis.
- **P / S**: primary / secondary source.

---

## 1. Publication landscape

### 1.1 Size and coverage of the record

| Source | Count | Notes | Tag |
|---|---|---|---|
| DBLP pid 20/8222 | 85 records, 2010–2026: 64 refereed (43 journal articles, 21 conference papers) and 21 CoRR | Misses at least 10 verified items (next row) | [practice] S |
| Items verified via Crossref but absent from DBLP | *IMA JNA* 32(2) 2012, DOI 10.1093/imanum/drq043; *IMA JNA* 37(1) 2017, DOI 10.1093/imanum/drw004; *IMA JNA* 39(3) 2019, DOI 10.1093/imanum/dry022; *IMA JNA* 40(2) 2020, DOI 10.1093/imanum/drz008; *TOP* 23(1) 2015, DOI 10.1007/s11750-015-0371-2; *Phys. Rev. E* 103(5) 2021, DOI 10.1103/PhysRevE.103.053304; *J. Stat. Mech.* 2020 124008, DOI 10.1088/1742-5468/abcaee; SIAM book 2025, DOI 10.1137/1.9781611978599; *IJOO* 8(3) 2026, DOI 10.1287/ijoo.2025.0091; FLICS 2026, DOI 10.1109/FLICS70075.2026.11621940 | So the refereed total is at least **about 74** | [practice] P (Crossref) |
| OpenAlex, works by ORCID 0000-0003-0251-4227 | 127 | Includes preprint duplicates and the 2007 thesis | [practice] S |
| ORCID record | 84 work groups, 2007–2024 | Not updated after 2024 | [practice] P |
| Homepage publication list (Wayback snapshot 2025-08-09) | 7 sections, ending around 2021 | The live page shows a broken shortcode | [stated] P |

The homepage list's own categories show how he sorts his output [stated, P]:

1. Published Journal Articles (Refereed)
2. Published Conference and Proceedings Articles (Refereed)
3. Invited Publications (Not Refereed)
4. Published Books and Book Chapter
5. Articles Under Review
6. Working Papers
7. Technical Reports

### 1.2 Topics by five-year period

The counts below cover DBLP refereed records only. I assigned topics by title keywords, so the classification is **[inferred]** and the boundaries between topics are rough.

| Period | Refereed records (DBLP) | Topic mix | Representative works (verified) |
|---|---|---|---|
| 2007–2011 (PhD, Oxford, Northwestern) | 3, plus the thesis and 3 Oxford/RAL reports | 100% deterministic constrained NLP | Thesis "Primal-Dual Methods for Nonlinear Optimization" (UCSD 2007, eScholarship item 8hz1b6q0); Gould & Robinson, *SIOPT* 20(4) 2010, DOI 10.1137/080744542 and DOI 10.1137/080744554; Gould, Robinson, Thorne, *MPC* 2(1) 2010, DOI 10.1007/s12532-010-0011-7 |
| 2012–2016 (JHU, junior) | 17 | 12 deterministic NLP/QP (SQP, augmented Lagrangian, filter, active-set QP, LCP); 5 ML/vision | Gill & Robinson, *COAP* 51 2012, DOI 10.1007/s10589-010-9339-1; Gill & Robinson, *SIOPT* 23(4) 2013, DOI 10.1137/120882913; Curtis, Jiang, Robinson, *Math. Prog.* 152 2015, DOI 10.1007/s10107-014-0784-y; Robinson (sole author), *JOTA* 166(1) 2015, DOI 10.1007/s10957-015-0708-x; You, Robinson, Vidal, CVPR 2016, DOI 10.1109/CVPR.2016.425 |
| 2017–2021 (JHU, then Lehigh) | 29, the peak | 13 ML/vision (subspace clustering, DPCP, sparse recovery, dynamical systems); 5 complexity; 5 sparse/regularized; 4 deterministic NLP; 2 stochastic | TRACE, *Math. Prog.* 162 2017, DOI 10.1007/s10107-016-1026-2; FaRSA, *SIOPT* 27(3) 2017, DOI 10.1137/16M1062259; regional complexity, *Math. Prog.* 187 2021, DOI 10.1007/s10107-020-01492-3; stochastic SQP, *SIOPT* 31(2) 2021, DOI 10.1137/20M1354556 |
| 2022–2026 (Lehigh) | 15, plus the book and *IJOO* 2026 | 8 stochastic or constrained learning (stochastic SQP family, stochastic IPM, fairness); 4 sparse/proximal; 3 ML/vision; no deterministic second-order SQP | *MOR* 49(4) 2024, DOI 10.1287/moor.2021.0154; *SIOPT* 34(4) 2024, DOI 10.1137/23M1556149; *Math. Prog.* 205 2024, DOI 10.1007/s10107-023-01981-1; Dai, Qu, Robinson, *SIOPT* 35(4) 2025, DOI 10.1137/24M1653586; Curtis & Robinson, *Practical Nonconvex Nonsmooth Optimization* (SIAM 2025) |

**Reading the table** [inferred]:

- The **constant** across all four periods is the machinery: SQP-type decompositions, merit-function and penalty-parameter control, and active-set or reduced-space phases.
- What **changes** is the problem class it is applied to:
  - 2007–2016: deterministic NLP and QP.
  - 2015–2021: ℓ1 and subspace-clustering problems from vision.
  - From 2020: stochastic objectives with deterministic constraints, and constrained learning.
- **ML/vision share**: 0 of 3 records in 2010–11, 5 of 17 in 2012–16, 13 of 29 in 2017–21, 3 of 15 in 2022–26. The vision wave peaks and then fades.

### 1.3 Author order: the "first to last author" shift

- **Optimization papers use alphabetical author order** [practice, P/S]. Of 22 DBLP refereed records co-authored with Curtis, 21 are alphabetical. The only exception is AISTATS 2023: Dai, Wang, Curtis, Robinson, where the student comes first. The Gould papers are alphabetical (Gould, Robinson; Gould, Loh, Robinson; Gould, Orban, Robinson), and so are the Gill papers (Gill, Kungurtsev, Robinson). **In this community, author position says little about who led the work.**
- **Non-alphabetical orders do carry signal** [practice S; reading inferred]. DBLP has 26 non-alphabetical entries (refereed records plus the 2025–26 preprints, with one CoRR duplicate). They fall into three groups:
  - **2013, first author**: Robinson, Feng, Nocedal, Pang, *SIOPT* 23(3), DOI 10.1137/110845094. This is his Northwestern postdoc paper, and he leads it.
  - **2015–2020, middle author**: Vidal-group papers put the student first and Vidal (the PI) last, with Robinson in between, e.g. "You, Robinson, Vidal" and "Zhu, Wang, Robinson, Naiman, Vidal, Tsakiris".
  - **2021 onward, last author**: "Ding, Zhu, Tsakiris, Vidal, Robinson" (AISTATS 2021); "Ding, Zhu, Vidal, Robinson" (ICML 2021); "Dai, Chen, Wang, Robinson" (TMLR 2023); "Dai, Wang, Curtis, Robinson" (AISTATS 2023). [inferred] This marks Tianyu Ding and Yutong Dai as students he supervised himself, and it is the visible first-to-last shift. In 2021 he moves from the optimization specialist inside Vidal's group to the senior author of his own students' ML-venue papers.
- **Two-author papers with a student**: Mohy-ud-Din & Robinson (*SIOPT* 2015); Dai & Robinson (*OMS* 39(4) 2024, DOI 10.1080/10556788.2024.2346643). **Solo papers**: *JOTA* 2015; *TOP* 2015 (a discussion piece). No solo research paper appears after 2015.
- **A possible advisor signal**: the order "Khatti, Robinson, Curtis" (arXiv 2505.15788) breaks the alphabetical rule. [inferred] It suggests Robinson is Zahra Khatti's primary advisor. Not verified.

### 1.4 Collaboration network and likely students

**Co-authors on DBLP refereed records**, all periods [practice, S]:

| Co-author | Records |
|---|---|
| Frank E. Curtis | 22 |
| René Vidal | 22 |
| N. I. M. Gould | 9 |
| Chong You | 9 |
| Zhihui Zhu | 6 |
| M. C. Tsakiris | 5 |
| Tianyu Ding | 5 |
| Yutong Dai | 5 |
| P. E. Gill | 4 |
| Tianyi Chen | 4 |
| Hao Jiang | 3 |
| V. Kungurtsev | 3 |
| G. França | 3 |
| E. Mallada | 3 |
| Tianjiao Ding | 3 |
| Baoyu Zhou | 3 |

The non-DBLP *IMA JNA* papers add 1 more with Gill/Kungurtsev and 2 more with Curtis, and the 2025 book is co-authored with Curtis.

**The main partner shifts with each period**:

| Period | Main partners |
|---|---|
| 2010–11 | Gould only |
| 2012–16 | Gould and Curtis (4 each), Vidal (4) |
| 2017–21 | Vidal (15), Curtis (10) |
| 2022–26 | Curtis (8), Dai (5) |

**Likely students and postdocs.** None of these advisor roles is verified from a degree record in this run.

| Person | Where and when | Evidence |
|---|---|---|
| Hao Jiang | JHU | The adaptive-AL paper reads "H. Jiang, D.P. Robinson--Research supported by National Science Foundation Grant DMS-1217153", which is Robinson's own grant [practice, P] |
| Tianyi Chen | JHU (tchen59@jhu.edu on FaRSA) | Co-author of the FaRSA papers |
| Hassan Mohy-ud-Din | JHU | Two-author *SIOPT* 2015 paper |
| Yueling Loh | JHU? | Filter SQP papers with Gould, 2014–15 |
| Tianyu Ding | JHU | Robinson is last author in 2021 |
| Yutong Dai | Lehigh (yud319@lehigh.edu on the group-sparsity paper) | Robinson last author 2023; two-author *OMS* 2024 |
| Xiaoyi Qu | Lehigh | Proximal-gradient papers |
| Zahra Khatti | Lehigh | Fairness work; order "Khatti, Robinson, Curtis" |
| Chia-Yuan Wu | Lehigh | Fairness and collaborative-learning work |
| Lingjun Guo | Lehigh | Progressive sampling |
| Lara Zebiane | Lehigh | Noisy active-set identification |
| Qi Wang | Lehigh | Stochastic IPM |
| Baoyu Zhou | Lehigh (baz216@lehigh.edu on stochastic SQP) | Likely co-supervised with Curtis [inferred] |

### 1.5 Usual venues

| Period | Optimization venues (DBLP) | ML / vision venues (DBLP) |
|---|---|---|
| 2010–11 | *SIOPT* 2, *MPC* 1 | — |
| 2012–16 | *SIOPT* 6, *COAP* 2, *MPC* 1, *Math. Prog.* 1, *JOTA* 1 | CVPR 2, ICML 1, ACSSC 1, IJCAI 1 |
| 2017–21 | *SIOPT* 5, *Math. Prog.* 5, *COAP* 2, *J. Sci. Comput.* 1 | ICML 4, NeurIPS 3, CVPR 2, ECCV 1 |
| 2022–26 | *SIOPT* 4, *OMS*, *IJOO*, *MOR* | TPAMI, TAC, AISTATS, TMLR, CVPR 2025 |

- **Overall** [practice, S]: *SIAM J. Optim.* is his home journal, with 17 DBLP records.
- **No conference-only habit in optimization** [inferred]. Every optimization result goes to a journal, usually after a technical report:
  - Oxford NA / RAL reports for 2008–09;
  - CCoM report 16-01;
  - Lehigh ISE / COR@L TR numbers on arXiv after 2018, e.g. 18T-003, 20T-012, 20T-015.

### 1.6 Most-cited works

Counts were retrieved on 2026-10-16. They are secondary, and the three indexes **disagree**; the disagreements are kept in Contradictions.

| Work | Semantic Scholar | OpenAlex | Crossref | Identifier |
|---|---|---|---|---|
| You, Robinson, Vidal, "Scalable Sparse Subspace Clustering by Orthogonal Matching Pursuit", CVPR 2016 | 385 | 394 | 274 | DOI 10.1109/CVPR.2016.425; arXiv 1507.01238 |
| You, Li, Robinson, Vidal, "Oracle Based Active Set Algorithm for Scalable Elastic Net Subspace Clustering", CVPR 2016 | 275 | 275 | 199 | DOI 10.1109/CVPR.2016.426; arXiv 1605.02633 |
| Curtis, Robinson, Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε^{-3/2}) for nonconvex optimization", *Math. Prog.* 162 (2017) | 135 | 157 | 97 | DOI 10.1007/s10107-016-1026-2 |
| You, Robinson, Vidal, "Provable Self-Representation Based Outlier Detection in a Union of Subspaces", CVPR 2017 | 124 | 110 | not checked | DOI 10.1109/CVPR.2017.460 |
| Gill & Robinson, "A primal-dual augmented Lagrangian", *COAP* 51 (2012) | 113 | 92 | 73 | DOI 10.1007/s10589-010-9339-1 |
| Yang, Robinson, Vidal, "Sparse Subspace Clustering with Missing Entries", ICML 2015 | 99 | 63 | — | ICML 2015, pp. 2463–2472 (homepage list); DBLP |
| Berahas, Curtis, Robinson, Zhou, "Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization", *SIOPT* 31(2) (2021) | 95 | 38 | 39 | DOI 10.1137/20M1354556; arXiv 2007.10525 |
| Gould, Robinson, Thorne, "On solving trust-region and other regularised subproblems in optimization", *MPC* 2(1) (2010) | 92 | 76 | 57 | DOI 10.1007/s12532-010-0011-7 |
| França, Robinson, Vidal, "ADMM and Accelerated ADMM as Continuous Dynamical Systems", ICML 2018 | 89 | 49 | — | arXiv 1805.06579 |
| Gill & Robinson, "A Globally Convergent Stabilized SQP Method", *SIOPT* 23(4) (2013) | 74 | 50 | 46 | DOI 10.1137/120882913 |
| Gould & Robinson, "A Second Derivative SQP Method: Global Convergence", *SIOPT* 20(4) (2010) | 67 | 57 | 40 | DOI 10.1137/080744542 |
| Curtis, Jiang, Robinson, "An adaptive augmented Lagrangian method for large-scale constrained optimization", *Math. Prog.* 152 (2015) | 61 | 49 | 43 | DOI 10.1007/s10107-014-0784-y |

- [inferred] **His two most-cited works are vision papers on which he is the middle author.** His most-cited optimization work is TRACE.
- **Among optimization-venue papers**, the next tier by citations is:
  - the primal-dual augmented Lagrangian (thesis line);
  - the trust-region subproblem solver paper (postdoc);
  - stochastic SQP (Lehigh flagship).
- **The one paper he names himself.** His own bio picks out a single paper, which is not in the top tier [stated, P; ICCOPT 2025 bio]: "awarded a Best Paper Prize from Optimization Letters for his co-authored 2018 paper titled "Concise Complexity Analyses for Trust-Region Methods"". That paper is Curtis, Lubberts, Robinson, *Optim. Lett.* 12(8):1713–1724, DOI 10.1007/s11590-018-1286-2, with 23 Crossref citations.

### 1.7 What he features as important (his own selection)

His homepage *Current Research* page (live, fetched 2026-10-16) illustrates four threads, and each is tied to one paper [stated, P]:

1. **"Deterministically Constrained Stochastic Optimization"**. Paper: Berahas et al., arXiv 2007.10525.
   - Why now: "Such problems are just now emerging in data science since large-scale decision-making applications demand the ability to solve problems with more realistic, nonlinear systems of equations/inequalities that impose constraints on the decision variables."
   - Funding: "This research is funded by the Office of Naval Research since 2021."
2. **"Subspace Clustering"**. Paper: Ding et al., "Noisy Dual Principal Component Pursuit", ICML 2019.
   - Claim: "We are currently focused on a Dual Principal Component Pursuit (DPCP) approach, which has routinely been shown to outperform other state-of-the-art algorithms."
3. **"Group-Sparse Regularization"**. Paper: Curtis, Dai, Robinson, arXiv 2007.14951.
   - Claim: "One can see that our method FaRSA-Group significantly outperforms gglasso."
4. **"Predicting Septic Shock"**. Paper: Saria & Robinson, IJCAI 2016.

His self-description (homepage) [stated, P]: "I work in Computational Optimization because I design, analyze, and implement algorithms for solving optimization problems." His bio (ICCOPT 2025) [stated, P]: "specific interest in the design, analysis, and implementation of efficient algorithms for large-scale convex and nonconvex problems, with particular interest in applications related to computer vision and medicine/healthcare."

[inferred] None of his deterministic SQP, augmented-Lagrangian, filter or funnel work is featured, although it fills most of his 2010–2017 record. The page shows his post-2019 identity, centered on applications and data.

### 1.8 Recent works (2025-08 to 2026-10)

| Date | Item | Identifier | Tag |
|---|---|---|---|
| 2025-08-31 | Curtis, Robinson, Zebiane, "Active-Set Identification in Noisy and Stochastic Optimization" | arXiv 2509.00888 | [practice] P |
| 2025-09-22 | Curtis & Robinson, *Practical Nonconvex Nonsmooth Optimization*, SIAM (MOS-SIAM Series) | DOI 10.1137/1.9781611978599 (Crossref; not read) | [practice] P |
| 2025 | Curtis, Kungurtsev, Robinson, Wang, "A Stochastic-Gradient-Based Interior-Point Algorithm for Solving Smooth Bound-Constrained Optimization Problems", *SIOPT* 35 | DOI 10.1137/23M1569460; arXiv 2304.14907 | [practice] S (DBLP) |
| 2025-10 (arXiv id; latest version 2026-05-13) | Curtis, Guo, Robinson, "Progressively Sampled Equality-Constrained Optimization" | arXiv 2510.00417 | [practice] P |
| 2025-05 (arXiv id; latest version 2025-10-21) | Khatti, Robinson, Curtis, "Fair Supervised Learning Through Constraints on Smooth Nonconvex Unfairness-Measure Surrogates" | arXiv 2505.15788 | [practice] P |
| 2025-12-05 | Dai, Qu, Robinson, "A Proximal-Gradient Method for Equality Constrained Optimization", *SIOPT* 35(4):2654–2683 | DOI 10.1137/24M1653586. [inferred] It continues arXiv 2404.07460, "A Proximal-Gradient Method for Constrained Optimization", which Robinson submitted himself in April 2024 | [practice] P |
| 2025-12 (arXiv id; latest version 2026-01-15) | Curtis, Qu, Robinson, "A Proximal-Gradient Method for Solving Regularized Optimization Problems with General Constraints" | arXiv 2512.23166 | [practice] P |
| 2026-07 | Wu, Curtis, Robinson, "A Bilevel Optimization Approach for Computing Synthetic Data to Mitigate Unfairness in Collaborative Machine Learning", *IJOO* 8(3):248–265 | DOI 10.1287/ijoo.2025.0091 | [practice] P |
| 2026-05 / 2026-06 | Wu, Curtis, Robinson, "Robust Server Defense Against Unreliable Clients in One-Shot Fair Collaborative Machine Learning", FLICS 2026, pp. 239–247 | arXiv 2605.08616; DOI 10.1109/FLICS70075.2026.11621940 | [practice] P |
| 2026-08-12 | Curtis, Guo, Robinson, "A Local-Linearly Convergent Algorithm for Nonconvex Equality-Constrained Optimization" | arXiv 2608.12665 | [practice] P |

[inferred] All of the recent output is either the stochastic-constrained line or the proximal and sparsity line meeting constraints, plus applied fairness work led by students. The arXiv author search shows **no new deterministic second-order SQP work since 2020.**

### 1.9 Failures, unfinished items, corrections (as seen from the publication record)

| # | Item | Evidence | Tag |
|---|---|---|---|
| U1 | **Five "Working Papers" and one "Under Review" item on the homepage list (around 2020) never appear** in DBLP or OpenAlex. The list: (a) Ahn, Pang, Robinson, MINLP for cost-sensitive prediction; (b) Basu, Ding, Robinson, "A reduced-space accelerated optimization algorithm for low-rank optimization", "In preparation for submission to siam journal on optimization"; (c) Robinson, "A primal-dual matrix-free algorithm for strictly convex quadratic problems", "In preparation for submission to mathematical programming computation"; (d) Robinson, "A truncated-Newton algorithm for unconstrained optimization with strong global and local convergence properties", "In preparation for submission to the ima journal on numerical analysis"; (e) Robinson, Vidal, You, "Basis pursuit and orthogonal matching pursuit for subspace-preserving recovery: theoretical analysis", JMLR, "Articles Under Review" (arXiv 1912.13091 exists; no journal record found). The Ahn–Pang MINLP item is not in OpenAlex and was not further checked. Two of the five are **sole-author** projects | Wayback list; DBLP; OpenAlex | [practice] P |
| U2 | **A venue change**: França, Robinson, Vidal, "A nonsmooth dynamical systems perspective on accelerated extensions of ADMM" is listed as "Siam j. control optim., 2020" under Working Papers. It appeared in *IEEE Trans. Autom. Control* 68 (2023), DOI 10.1109/TAC.2023.3238857 (arXiv 1808.04048 v1 2018 → 2023). Whether SICON rejected it is **unknown** | Wayback list; DBLP; arXiv listing | [practice] P; reason not found |
| U3 | **A stub preprint**: Gill, Kungurtsev, Robinson, "Negative Curvature and Second-order optimality for regularized SQP", arXiv 1205.2304 (v1 2012-05-10). Its abstract is only the title, and no publication has that title. [inferred] It is probably an early placeholder of the stabilized-SQP papers of 2016–17 | arXiv abs page | [practice] P |
| U4 | **Two GALAHAD packages announced but never shipped**: "our evolving GALAHAD package TRIMSQP" (Oxford NA 08/09, June 2008, §5), renamed "our evolving GALAHAD package S2QP" (NA 08/18, November 2008, and RAL-TR-2009-001, February 2009, §5). The current GALAHAD `src/` tree (140 entries, fetched 2026-10-16) has no `s2qp` or `trimsqp`. Packages that do exist trace to his co-authored work: TRS and RQS ("originally released GALAHAD Version 2.3. January 7th, 2009") and DQP ("originally released in GALAHAD Version 2.5. August 1st 2012"), whose headers name Gould as "Principal author" | report PDFs; GitHub ralna/GALAHAD | [practice] P |
| U5 | **Published corrections** to two signature papers. TRACE corrigendum: "This means that the inequality in the published paper is correct, but not as tight as it could have been." Stochastic SQP corrigendum: "A corrected statement of Corollary 3.14(a) from the published paper is below." | errata PDFs on Curtis's Lehigh site | [practice] P |
| U6 | **Software left unfinished**: the GitHub account `daniel-p-robinson`, which has 3 public repositories, holds "FaRSA" (C++, created 2020-07-30, last push 2021-07-20). Its README says: "This software is under development.  Please check back later." and "FaRSA is written in C++ and is released under the ??? License." The older "FaRSA-L1-C" (C, 2017-05 to 2018-05, "Fast Reduced Space Algorithm v2.0", authors Chen, Curtis, Robinson) is complete enough to build with `make` | GitHub API, README files | [practice] P |
| U7 | **No rejections, referee reports or retractions** were found for any work. | — | gap |

---

## 2. Signature works (5 dissections and 1 short supporting one)

**Selection rule** (framework §五):

- **Most cited**: S3 (vision) and S4 (optimization).
- **Ones he features himself**: S5 (homepage thread 1) and S6 (homepage thread 3, via FaRSA-Group). His bio names the concise trust-region paper, which is folded into S4.
- **Turning points**:
  - S1: start of the career; postdoc problem chosen from the thesis.
  - S3: entry into vision.
  - S5: the Lehigh stochastic turn.
  - S6: his longest-running self-owned line.

S2 (adaptive augmented Lagrangian) is a short supporting dissection. It is the first JHU paper with his own student and grant, and it shows his "steering" transfer.

Each dissection follows the framework's rows: origin, why then, key insight, minimum evidence, abandoned paths, reception, method shown, plus era and resources.

### S1. Second-derivative SQP without global QP solutions (Gould & Robinson, 2008–2012)

- **Identifiers**:
  - Gould & Robinson, "A Second Derivative SQP Method: Global Convergence", *SIOPT* 20(4):2023–2048 (2010), DOI 10.1137/080744542.
  - Companion: "… Local Convergence and Practical Issues", *SIOPT* 20(4):2049–2079, DOI 10.1137/080744554.
  - Follow-up: "A second-derivative SQP method with a 'trust-region-free' predictor step", *IMA JNA* 32(2):580–601 (2012), DOI 10.1093/imanum/drq043.
  - Report chain:
    - Oxford NA 08/09, "A Second Derivative SQP Method with Imposed Descent" (June 2008);
    - Oxford NA 08/18, "A Second Derivative SQP Method: Theoretical Issues" (November 2008);
    - RAL-TR-2009-001, "A second derivative SQP method: global convergence" (February 9, 2009).
- **Origin**. The [stated] P part, from his thesis (UCSD 2007, §6.2, pp. 163–164), explains why he used SNOPT (a quasi-Newton SQP code) as the inner solver: "It is likely that a second-derivative solver would improve the efficiency of the methods significantly. However, the efficiency of second-derivative solvers is critically dependent on the method used to treat the occurrence of negative curvature in the Hessian of the subproblem. The choice of an appropriate second-derivative solver is an ongoing research issue that is beyond the scope of this thesis." [inferred] The link is mine: the open problem his thesis set aside became his first postdoc project with Gould within a year (SIAM OP08 talk "A Second Derivative SQP Method with Imposed Descent", May 2008, archived talks list). **No primary source states this link.**
- **Why then** [stated, collective, P; RAL-TR-2009-001 §1, p. 4]: "To our knowledge, all previous second-order SIQP methods assume that global minimizers of nonconvex subproblems are computed, which is not a realistic assumption in most cases." The conclusion opens: "Research on second-derivative SQP methods is very active." [inferred] The ingredients were in place:
  - Fletcher's Sl1QP gave a template;
  - Yuan's analysis gave weaker-assumption results to extend;
  - Gould's group was building GALAHAD QP solvers, which made inner solvers available.
- **Key insight** (abstract, all three versions): build the step from "quadratic subproblems that are either convex, and thus may be solved efficiently, or need not be solved globally", and impose "an explicit descent-constraint" on certain QP subproblems "which 'guides' the iterates through areas in which nonconvexity is a concern."
- **What they rated highest** [stated, collective, P; RAL-TR-2009-001 §5, p. 34]: "we proved that our method is globally convergent without having to compute the global minimizer of a nonconvex quadratic program; this is arguably the greatest contribution of this paper."
- **Minimum evidence**: a convergence proof first, with no numbers. The global-convergence paper has no experiments. The companion reports only "preliminary numerical results on the Hock and Schittkowski test set" (Crossref abstract of DOI 10.1137/080744554) [practice, P].
- **Abandoned or changed paths** [practice, P; from comparing the three report versions in this run]:
  1. Between June and November 2008, the SEQP-type subproblem grew from a passing mention (3 mentions of "SEQP" in NA 08/09) to a full option (18 in NA 08/18; 20 in RAL-TR-2009-001). The method was then presented as "an SIQP/SEQP hybrid".
  2. The weaker-Hessian-assumption results, deferred in June 2008 ("will be covered in a separate paper"), were folded into the November 2008 version.
  3. The promised software was renamed TRIMSQP → S2QP and never released (U4).
  4. The 2008 title "… with Imposed Descent" became "… Global Convergence" (2009–10).
- **Reception** [practice, S]: 67/57/40 citations (S2/OpenAlex/Crossref) for the global paper and 42/38/31 for the local one, which is modest. [inferred] The descent-constraint device did not become standard practice, but the stance "do not assume global QP solutions" carries on: Robinson's single-author *TOP* 2015 comment says he believes "the assumption placed on the subproblem solutions is unsatisfactory and should be avoided if possible" (quoted from agent 06's reading; **not re-read in this run**, though DOI 10.1007/s11750-015-0371-2 was re-checked).
- **Method shown** [inferred]: **M1. Refuse the unrealistic subproblem assumption.** Design steps whose theory needs only convex or local subproblem solutions, then prove convergence before writing any code.
- **Era and resources** [practice, P]:
  - Thesis: SNOPT called from Matlab through a MEX interface, on 40 CUTEr problems with at most 50 variables and 50 constraints. The thesis acknowledgments thank Gill "for the graduate research assistantship working for Northrop Grumman".
  - Postdoc: EPSRC grants EP/E053351/1 and EP/F005369/1 (report footnote). He was a junior researcher with one senior partner, and the paper went first into the Oxford NA and RAL report series.

### S2 (short, supporting). Adaptive "steering" augmented Lagrangian (Curtis, Jiang, Robinson 2015)

- **Identifiers**:
  - *Math. Prog.* 152:201–245, DOI 10.1007/s10107-014-0784-y ("Received: 10 December 2012 / Accepted: 15 April 2014").
  - Follow-up with Gould: *OMS* 31(1):157–186 (2016), DOI 10.1080/10556788.2015.1071813, arXiv 1408.4500.
  - Talks: "Steering Augmented Lagrangian Methods" at ISMP Berlin (August 2012), INFORMS (October 2012) and Argonne (July 2013) (archived talks list).
- **Key insight** [stated, collective, P; abstract]: "an adaptive update for the penalty parameter motivated by recently proposed techniques for exact penalty methods." [inferred] In other words, a steering rule from exact-penalty SQP (Curtis's line) moved into augmented-Lagrangian methods.
- **Scope stated honestly** [stated, collective, P; p. 202]: "(If the constraints are well-scaled, then these issues become less of a practical concern and basic AL methods are quite efficient. Thus, our enhancements are most beneficial for difficult and/or poorly scaled problems.)"
- **Admitted weakness** [stated, collective, P; p. 243]: "One potential deficiency of our proposed technique is the lack of a guarantee that the penalty parameter will remain bounded away from zero".
- **Evidence design** [practice, P]:
  - a Matlab implementation compared with LANCELOT, "a very mature Fortran-90 implementation", on equality-constrained CUTEr problems;
  - a stated fairness rule for the comparison: "this strategy allows for a fair comparison with Lancelot on equality constrained problems since Lancelot employs a similar iterative scheme for the subproblem".
- **Resources** [practice, P]: "H. Jiang, D.P. Robinson--Research supported by National Science Foundation Grant DMS-1217153". This was his first single-PI grant, and Jiang was his student; 2012–14 was the start of his own group.
- **Method shown** [inferred]: **M2. Transplant a globalization mechanism** from one method family to another (here exact-penalty steering → augmented Lagrangian).

### S3. Scalable sparse subspace clustering (You, Robinson, Vidal, CVPR 2016; with the elastic-net active-set companion)

- **Identifiers**:
  - You, Robinson, Vidal, "Scalable Sparse Subspace Clustering by Orthogonal Matching Pursuit", CVPR 2016, pp. 3918–3927, DOI 10.1109/CVPR.2016.425, arXiv 1507.01238 (v1 2015-07-05, v2 2015-08-31, v3 2016-05-05; v3 comments: "Accepted to CVPR 2016 as an oral presentation").
  - Companion: You, Li, Robinson, Vidal, "Oracle Based Active Set Algorithm for Scalable Elastic Net Subspace Clustering", CVPR 2016, pp. 3928–3937, DOI 10.1109/CVPR.2016.426, arXiv 1605.02633 ("accepted to CVPR 2016 for oral presentation").
- **Origin** [practice, P]:
  - First talk "Large-scale Subspace Clustering" at MOPTA, August 2014 (archived talks list).
  - Then co-PI on Vidal's NSF BIGDATA award from September 2014 (reported by agent 06; not re-checked here).
  - Both papers are submitted by Chong You, Vidal's student.
  - [inferred] The topic and data came from the Vidal group; Robinson brought scalable-optimization expertise. **What he personally contributed is not stated anywhere I found.**
- **Why then** [stated, collective, P; v3 §1]: "Thus, there is a need for methods that both guarantee a subspace-preserving affinity under broad conditions and are computationally efficient." The companion's contribution is "an efficient and provably correct active-set based algorithm for solving the elastic net problem" (ORGEN). [inferred] That is an active-set reduced-subproblem method, which is Robinson's home technique.
- **Key insight**: replace the ℓ1 basis-pursuit solve with greedy OMP and prove conditions under which the resulting affinity is still subspace-preserving. The companion uses an "oracle region" to grow and shrink an active set.
- **Minimum evidence** [stated, collective, P; v3 contributions]: "SSC-OMP is orders of magnitude faster than the original SSC-BP, and can handle up to 100,000 data points."
- **Claims narrowed between v1 and v3** [practice, P; abstracts compared in this run]:
  - v1 (July 2015): "This paper proposes a new subspace clustering method based on orthogonal matching pursuit that is computationally efficient and guaranteed to provide the correct clustering for arbitrary subspaces. … Moreover, our approach is the only one that can handle 100,000 points."
  - v3 (May 2016): "In this paper we study a subspace clustering method based on orthogonal matching pursuit. We show that the method is both computationally efficient and guaranteed to give a subspace-preserving affinity under broad conditions."
  - v3 also adds: "It is worth noting that the idea of using OMP for SSC had already been considered in [12]."
  - So between versions, the novelty claim ("new method", "correct clustering", "only one") was **scaled down** to "study", "subspace-preserving affinity", and an acknowledged prior source. [inferred] Most likely this followed review or reader feedback. Whether v1 was rejected at an earlier venue is **not known**.
- **Reception** [practice, S]: his two most-cited papers by every index (SSC-OMP: 385/394/274; EnSC: 275/275/199), both CVPR orals. The line ran to TPAMI 2022 (DOI 10.1109/TPAMI.2020.3035599) and NeurIPS 2024.
- **Method shown** [inferred]: **M3. Carry active-set and reduced-space machinery into a neighboring field's bottleneck subproblem** (here the elastic net), together with **M5. Scale as the headline evidence** ("orders of magnitude faster", 100,000 points).
- **Era and resources**: JHU Center for Imaging Science; a large vision group with students as first authors. [inferred] Compute was CPU-scale; the papers report datasets of up to 100,000 points.

### S4. TRACE: optimal complexity inside a trust-region method (Curtis, Robinson, Samadi 2017), and its sequels

- **Identifiers**:
  - "A trust region algorithm with a worst-case iteration complexity of O(ε^{-3/2}) for nonconvex optimization", *Math. Prog.* 162(1–2):1–32, DOI 10.1007/s10107-016-1026-2 ("Received: 21 October 2014 / Accepted: 5 May 2016").
  - Sequels:
    - "Complexity Analysis of a Trust Funnel Algorithm for Equality Constrained Optimization", *SIOPT* 28(2):1533–1563 (2018), DOI 10.1137/16M1108650, arXiv 1707.00337;
    - "An inexact regularized Newton framework …", *IMA JNA* 39(3):1296–1327, DOI 10.1093/imanum/dry022, arXiv 1708.00475;
    - "Concise complexity analyses for trust region methods", *Optim. Lett.* 12(8):1713–1724 (2018), DOI 10.1007/s11590-018-1286-2, arXiv 1802.07843 (Best Paper Prize);
    - "Regional complexity analysis of algorithms for nonconvex smooth optimization", *Math. Prog.* 187:579–615, DOI 10.1007/s10107-020-01492-3, arXiv 1802.01062 (v1 2018-02-04, Lehigh ISE/COR@L TR 18T-003);
    - Curtis, Robinson, Royer, Wright, "Trust-Region Newton-CG with Strong Second-Order Complexity Guarantees for Nonconvex Optimization", *SIOPT* 31(1):518–544 (2021), DOI 10.1137/19M130563X, arXiv 1912.04365.
- **Origin** [stated, collective, P; Acknowledgments]: "The authors are extremely grateful to Coralia Cartis, Nicholas I. M. Gould, and Philippe L. Toint for enlightening discussions about the arc algorithm and its theoretical properties that were inspirational for the algorithm proposed in this paper." The funding line includes his grant: "DMS-1217153".
- **Why then** [stated, collective, P; §1]: "Worst-case complexity bounds, on the other hand, have typically been overlooked when analyzing nonconvex optimization algorithms." "The focus on complexity bounds in the field of nonconvex optimization started to change with recent studies on cubic regularization methods." ARC had set the O(ε^{-3/2}) target, and classical trust region was stuck at O(ε^{-2}).
- **Key insight** [stated, collective, P; abstract]: keep the trust-region framework but use "modified step acceptance criteria and a novel trust region update mechanism". The text adds that "there are situations in which our algorithm may reject a step and expand the trust region".
- **Minimum evidence**: a proof only; **the paper has no numerical experiments.** An appendix argues that each iteration "need not be more computationally expensive" than a traditional trust-region iteration [practice, P].
- **Open points and corrections** [stated, collective, P; §4]:
  - Sharpness: "We expect that this is also the case for our algorithm, but this has not yet been confirmed."
  - Assumptions: "we have assumed that the algorithm uses exact first- and second-order derivative information, and that each iteration involves computing a globally optimal solution of a trust region subproblem. These requirements must often be relaxed when solving large-scale problems."
  - The corrigendum later tightened Lemma 3.19 (U5).
- **Abandoned paths**: none recorded in the paper. [inferred] The inexact-Newton framework (2018–19) is the promised relaxation of the exact-subproblem assumption: "A complete investigation of these ideas is the subject of current research."
- **Reception** [practice, S]: his most-cited optimization paper (135/157/97). The concise follow-up won the *Optimization Letters* Best Paper Prize (he cites this himself in his bio).
- **The later turn against the yardstick** [stated, collective, P; regional-complexity abstract, arXiv 1802.01062]: "This arguably leads to conservative characterizations based on anomalous objectives rather than on ones that are typically encountered in practice."
- **Method shown** [inferred]: **M2 again** (move ARC's complexity guarantee into trust regions), then **M6. Question the yardstick after meeting it.**
- **Era and resources** [practice, P]: Robinson was at JHU, and the first and third authors were at Lehigh (Samadi has a lehigh.edu address; that he was a student is [inferred]). It was a theory paper, with a review time of about 19 months.

### S5. Stochastic SQP for deterministic equality constraints (Berahas, Curtis, Robinson, Zhou 2021), and its family

- **Identifiers**:
  - arXiv 2007.10525 (v1 2020-07-20; "Lehigh ISE Technical Report 20T-012"; submitted by Curtis); *SIOPT* 31(2):1352–1379 (2021), DOI 10.1137/20M1354556.
  - Family:
    - *MOR* 49(4) 2024, DOI 10.1287/moor.2021.0154, arXiv 2106.13015 (rank-deficient Jacobians);
    - *IJOO* 6 2024, DOI 10.1287/ijoo.2022.0008, arXiv 2107.03512 (inexact);
    - *Math. Prog.* 205:431–483, DOI 10.1007/s10107-023-01981-1, arXiv 2112.14799 (worst-case complexity);
    - *SIOPT* 34(4):3592–3622, DOI 10.1137/23M1556149, arXiv 2302.14790 (inequality constraints);
    - arXiv 2510.00417 and 2608.12665 (progressive sampling).
- **Origin** [stated, P; homepage]: the problems are "just now emerging in data science" (quoted in 1.7). [practice, S] The stepping stone is Curtis & Robinson, "Exploiting negative curvature in deterministic and stochastic optimization", *Math. Prog.* 176 (2019), DOI 10.1007/s10107-018-1335-8, arXiv 1703.00412: his first paper mixing deterministic and stochastic settings.
- **Why then** [stated, collective, P; §1]: "Significantly fewer algorithms have been proposed for solving stochastic equality constrained optimization problems. … A few algorithms have been proposed that may be employed in this setting … although these are based on penalty methodologies, so do not benefit from advantages of SQP techniques." [observed, P] A competing group posted a stochastic SQP about seven months later, with a different merit function: Na, Anitescu, Kolar, arXiv 2102.05320 (v1 2021-02-10). This places the Lehigh paper early. I did not do a full priority search.
- **Key insight / construction strategy** [stated, collective, P; abstract]: "As a starting point for this stochastic setting, an algorithm is proposed for the deterministic setting that is modeled after a state-of-the-art line-search SQP algorithm, but uses a stepsize selection scheme based on Lipschitz constants … This sets the stage for the proposed algorithm for the stochastic setting, for which it is assumed that line searches would be intractable."
- **Minimum evidence** [stated, collective, P; §4]: first show that the deterministic version is *as reliable as* line-search SQP, while openly not claiming efficiency: "We do not claim that "SQP Adaptive" is as efficient as "SQP Backtracking" since, as has been verified by others in the literature, the line search scheme is very effective across a broad range of problems."
- **Experimental design** [practice, P; §4]:
  - Matlab implementations.
  - 49 CUTE equality-constrained problems, selected by f not constant, "n+m ≤ 1000", and LICQ holding.
  - Gaussian gradient noise at four levels, 10 runs each, giving 490 instances per level.
  - **The baseline gets every advantage.** Its stepsize was tuned per instance over 11 values: "Overall, this means that for each problem, "Stochastic Subgradient" was given 110 times the number of iterations that were allowed for "Stochastic SQP.""
  - **The proposed method is handicapped** to match the baseline: "For "Stochastic SQP," we set Hk = I for all k for fairness of comparison with the (first-order) subgradient method."
- **Assumptions admitted** [stated, collective, P]:
  - "The LICQ is a relatively strong assumption in the modern literature … but it is a reasonable one in our context due to the significant challenges that arise in the stochastic setting" (§2).
  - On bounded iterates: "This is not ideal in the context of a stochastic algorithm" (§5).
- **Corrections**: the corrigendum to Corollary 3.14(a) (U5).
- **Abandoned paths** [inferred]: none stated. The sequels remove the stated weak points one at a time: rank-deficient Jacobians in place of LICQ (*MOR* 2024), inexact subproblem solves (*IJOO* 2024), complexity (*Math. Prog.* 2024), and inequality constraints (*SIOPT* 2024).
- **Reception** [practice, S]: 95/38/39 citations, the widest spread between indexes for any of his papers. It is his Lehigh flagship, the first item on his homepage, and funded by ONR "since 2021" [stated, P].
- **Method shown** [inferred]: **M4. Build the deterministic analogue first, then remove the step that becomes intractable** (here the line search). Also **M5. Design the benchmark so the baseline gets its best shot.** **M7. A programme of sequels**, each lifting one admitted assumption.
- **Era and resources**: Lehigh, with a joint postdoc (Berahas, then at Michigan) and a student (Zhou). Matlab on CUTE problems of moderate size (n+m ≤ 1000).

### S6. FaRSA and subspace acceleration for ℓ1 and group sparsity (2016–2022), his longest self-owned line

- **Identifiers**:
  - Chen, Curtis, Robinson, "A Reduced-Space Algorithm for Minimizing ℓ1-Regularized Convex Functions", *SIOPT* 27(3):1583–1610 (2017), DOI 10.1137/16M1062259, arXiv 1602.07018 (v1 2016-02-23, **submitted by Robinson**).
  - "FaRSA for ℓ1-regularized convex optimization: local convergence and numerical experience", *OMS* 33(2):396–415 (2018), DOI 10.1080/10556788.2017.1415336.
  - Curtis, Dai, Robinson, "A Subspace Acceleration Method for Minimization Involving a Group Sparsity-Inducing Regularizer", *SIOPT* 32(2):545–572 (2022), DOI 10.1137/21M1411111, arXiv 2007.14951 (v1 2020-07-29, Lehigh ISE TR 20T-015, **submitted by Robinson**).
- **Origin**. The paper states its own starting point [stated, collective, P; arXiv 1602.07018 §1.1]: posing the ℓ1 problem as a bound-constrained QP and solving it "using the techniques developed in [5, 6, 7] (see also [12])". Refs [5–7] are Dostál's proportioning BCQP papers; [12] is Mohy-ud-Din & Robinson, *SIOPT* 2015, his student's BCQP solver. The paper then says: "Indeed, our initial developments of this work was based on these ideas. However, the algorithm proposed in this paper involves some deviations and enhancements from this starting point." [inferred] The line thus grows from his JHU BCQP/active-set work (NSF DMS-1217153, "New Active-Set Methods for Optimization and Complementarity Problems", from agent 06; not re-checked).
- **Why then** [stated, collective, P]:
  - FaRSA frames LIBLINEAR and OBA as complementary: "We have the perspective that both LIBLINEAR and OBA are valuable state-of-the-art algorithms that complement each other."
  - FaRSA-Group adds a modelling reason: "Despite the successes of ℓ1-norm regularization, its inadequacy in the context of many modern machine learning applications has been noticed by researchers, and is one motivation for the use of group regularization" (2007.14951 §1).
- **Key insight**: an evolving predicted support, reduced-space subproblems solved inexactly (Newton-CG or coordinate descent), and "a computationally practical condition that determines when the predicted support should be updated" (FaRSA abstract).
- **Abandoned path (stated)**: the direct BCQP-reformulation route above was the "initial development". The final algorithm departs from it [stated, collective, P].
- **Minimum evidence and benchmark choices** [practice, P]:
  - **FaRSA (2016)**:
    - a "preliminary Matlab implementation … that we are happy to provide upon request";
    - 31 LIBSVM-type datasets plus three others (gene-ad and pathway-ad, Alzheimer's data);
    - datasets dropped "since insufficient computer memory was available", on a machine with "an Intel I7 4.0GHz CPU and 16GB of main memory";
    - compared against OBA, using code obtained from its authors (Acknowledgments: "We thank Nitish Keskar, Jorge Nocedal, Figen Öztoprak, and Andreas Wächter for providing the Matlab code of their OBA algorithm").
  - **FaRSA-Group (2020)**: "a Python implementation … available upon request", compared against gglasso on 200 instances.
- **Where it loses, said openly** [stated, collective, P]:
  - FaRSA: "OBA and our preliminary implementation of FaRSA will often be outperformed by LIBLINEAR when the second derivative matrices are diagonally dominant."
  - FaRSA-Group (*SIOPT* 2022 abstract): "For solving problems when the number of data points is smaller than the number of features, algorithms that focus on solving a dual problem may be more efficient than our approach, which solves the primal problem."
- **Promise versus record** [practice, P; contradiction kept below]:
  - FaRSA's conclusion promised "a future release of our solver" with coordinate-descent options.
  - A C version did appear: FaRSA-L1-C, 2017–2018.
  - The C++ "FaRSA" for (group) sparsity still reads "under development" with a "???" license, and was last pushed in July 2021 (U6).
- **Reception** [practice, S]: modest. FaRSA *SIOPT* has 30/15/15 citations and the group paper 6 (OpenAlex/Crossref). He still features it on his homepage, and it was funded by NSF DMS-2012243 [stated, P]. The thread continues in proximal-gradient methods with constraints (*SIOPT* 2025; arXiv 2512.23166).
- **Method shown** [inferred]: **M3. Active-set / reduced-space acceleration with an adaptive switch test.** **M5. Benchmark against the strongest available code**, obtained from its authors, and **say where you lose.**
- **Era and resources**:
  - FaRSA: JHU, with student Tianyi Chen; "IDIES Seed Funding at Johns Hopkins University" appears in the arXiv footnotes (in the extracted text it follows Robinson's affiliation; I did not verify which author it belongs to); a single desktop with 16 GB.
  - FaRSA-Group: Lehigh, with student Yutong Dai and NSF DMS-2012243; the implementation language moved from Matlab to Python and C++.

---

## 3. Patterns across the signature works (all [inferred]; each cites the evidence above)

| # | Pattern | Evidence |
|---|---|---|
| M1 | Refuse the unrealistic subproblem assumption: no global solutions of nonconvex QPs, and later inexact subproblems | S1 (2009 conclusion); S4 (stated assumption, then the inexact framework); S5 (inexact SQP sequel) |
| M2 | Move a mechanism or guarantee from one method family to another | S2 (exact-penalty steering → AL); S4 (ARC complexity → trust region); S5 (line-search SQP → stochastic) |
| M3 | Active-set / reduced-space acceleration with an adaptive switching test, applied to whatever the current workload is | S3 (ORGEN); S6 (FaRSA, FaRSA-Group) |
| M4 | Deterministic analogue first, then remove the intractable component | S5 abstract |
| M5 | Strong baselines given the advantage (tuned stepsizes, authors' own code, LANCELOT), plus an explicit statement of where the new method loses | S2, S5, S6 |
| M6 | Meet the field's yardstick, then question it | S4 → regional complexity |
| M7 | Sequel programmes that lift one admitted assumption per paper | S4 (exact → inexact); S5 (LICQ → rank-deficient; equality → inequality) |
| M8 | Report first, journal later; proofs lead, numerics follow and are often "preliminary" | S1 report chain; S4 has no numerics; S6 calls its implementations "preliminary" |

**Time and resource caveat** [inferred]: every experiment found is CPU- and desktop-scale (Matlab or Python, CUTE(r) or LIBSVM, at most 16 GB). None of these patterns has been tested in a GPU or deep-learning-scale setting. The CVPR 2025 pruning paper (DOI 10.1109/CVPR52734.2025.01419), where he is middle author with Microsoft co-authors, was not read.

---

## Contradictions (kept, not reconciled)

1. **Citation counts disagree across indexes**:
   - stochastic SQP: 95 (S2) vs 38 (OpenAlex) vs 39 (Crossref);
   - SSC-OMP: 385 / 394 / 274;
   - TRACE: 135 / 157 / 97.
   
   The rankings in §1.6 hold in all three, but the absolute numbers do not.
2. **Semantic Scholar profile quality**: profile 1780452 includes "Investigating the technical, economic and environmental performance of electric vehicles in the real…" (2011, DOI 10.1016/J.JPOWSOUR.2011.08.021), which is outside his field and almost certainly a different Robinson. Meanwhile his 2023–2025 papers sit in separate profiles (2207502084, 2287570749).
3. **Novelty claim of SSC-OMP**: arXiv v1 says "proposes a new subspace clustering method" that is "the only one that can handle 100,000 points". v3 and CVPR say "we study a subspace clustering method" and credit prior work: "the idea of using OMP for SSC had already been considered in [12]".
4. **Software promises versus delivery**:
   - 2008–09 reports announce GALAHAD packages TRIMSQP and then S2QP; neither is in GALAHAD today.
   - FaRSA (2016) promised a future release with coordinate-descent options; the 2020 C++ repository still says "under development" with a "???" license.
   - The C version FaRSA-L1-C does exist (2017–18).
5. **What he features versus what he published**:
   - The homepage highlights stochastic SQP, DPCP, FaRSA-Group and septic-shock prediction.
   - His deterministic SQP, augmented-Lagrangian, filter and funnel papers make up most of his 2010–2017 refereed record, and his most-cited optimization paper (TRACE) is not featured at all.
   - His bio singles out the concise trust-region paper because of its award.
6. **IJCAI 2016 title**: his homepage list gives "Incorporating user preferences in predictive models via structured regularizers"; DBLP gives "Trading-Off Cost of Deployment Versus Accuracy in Learning Predictive Models" (arXiv 1604.05819); ORCID gives "Incorporating end preferences in predictive models via structured regularizers". The proceedings title was not checked.
7. **Funding attribution in FaRSA**: the "IDIES Seed Funding" footnote follows Robinson's affiliation in the extracted arXiv text, but the footnote markers did not survive extraction, so the attribution is uncertain.
8. **Postdoc institution**: his bio says "the Mathematical Institute at the University of Oxford", while the 2008–09 reports give "Oxford University Computing Laboratory, Numerical Analysis Group".

## Gaps

- **Google Scholar**: no profile found. The author search requires login and no page links one, so the Scholar citation picture is missing.
- **OpenAlex full harvest**: no API key, so `fetch_publications.py` was not run and `references/sources/publications/` is still empty.
- **Journal versions** of the 2010 *SIOPT* SQP papers and the *MPC* 2010 subproblem paper were **not read**; only report versions or metadata. The 2010 *MPC* paper (trust-region and regularised subproblems, GALAHAD TRS/RQS) and Robinson's part in it are undissected.
- **Stabilized SQP / primal-dual augmented Lagrangian with Gill** (2012–2020): identified (DOIs above) but **not dissected** here. The *TOP* 2015 commentary was not re-read in this run.
- **DPCP line** (NeurIPS 2018, ICML 2019, ICML/AISTATS 2021): featured on his homepage, but **not read**.
- **His own account of origins**: no interview, oral history or essay explains why he chose stochastic SQP, FaRSA or subspace clustering. All origins beyond the documents quoted are labeled [inferred].
- **Who drove which vision paper**: not stated in any source found.
- **Rejections and referee exchanges**: none found. The SICON → *TAC* venue change (U2) and the pre-CVPR history of SSC-OMP are unexplained.
- **Advisor roles of students**: inferred from author order and affiliations only; no dissertation records were checked in this run.
- **The 2025 SIAM book**: metadata only; preface and content not read.
- **Talks after mid-2019**: the archived list stops there, so recent self-presentation comes from the homepage and bio only.

## Sources

1. Daniel P. Robinson, homepage "Who I am / What I do", Lehigh COR@L, fetched 2026-10-16, https://coral.ise.lehigh.edu/danielprobinson/ (primary)
2. Robinson, homepage "Current Research", undated (funding statements to 2021+), fetched 2026-10-16, https://coral.ise.lehigh.edu/danielprobinson/research/current-research/ (primary)
3. Robinson, publications list, Wayback snapshot 2025-08-09, http://web.archive.org/web/20250809173145/https://coral.ise.lehigh.edu/danielprobinson/research/publications/ (primary)
4. Robinson, talks list, Wayback snapshot 2025-08-09, http://web.archive.org/web/20250809174202/https://coral.ise.lehigh.edu/danielprobinson/research/talks/ (primary)
5. ICCOPT 2025 sched, speaker page and bio of Daniel P. Robinson, 2025, https://iccopt2025usc.sched.com/speaker/daniel.p.robinson (primary, self-bio)
6. D. P. Robinson, "Primal-Dual Methods for Nonlinear Optimization", PhD dissertation, UC San Diego, 2007, https://escholarship.org/uc/item/8hz1b6q0 (primary; full text read: front matter, §1.2, §6.1–6.4)
7. N. I. M. Gould, D. P. Robinson, "A Second Derivative SQP Method with Imposed Descent", Oxford University Computing Laboratory NA Technical Report 08/09, June 2008, https://www.cs.ox.ac.uk/files/715/NA-08-09.pdf (primary; read: abstract, §1, §5)
8. N. I. M. Gould, D. P. Robinson, "A Second Derivative SQP Method: Theoretical Issues", Oxford NA Technical Report 08/18, November 2008, https://www.cs.ox.ac.uk/files/1836/NA-08-18.pdf (primary; read: abstract, §5)
9. N. I. M. Gould, D. P. Robinson, "A second derivative SQP method: global convergence", RAL-TR-2009-001, February 9, 2009, https://epubs.stfc.ac.uk/manifestation/6616/grRAL2009001.pdf (primary; read: abstract, §1, §5)
10. N. I. M. Gould, D. P. Robinson, "A Second Derivative SQP Method: Global Convergence", SIAM J. Optim. 20(4):2023–2048, 2010, DOI 10.1137/080744542 (primary; Crossref abstract only)
11. N. I. M. Gould, D. P. Robinson, "A Second Derivative SQP Method: Local Convergence and Practical Issues", SIAM J. Optim. 20(4):2049–2079, 2010, DOI 10.1137/080744554 (primary; Crossref abstract only)
12. N. I. M. Gould, D. P. Robinson, H. S. Thorne, "On solving trust-region and other regularised subproblems in optimization", Math. Program. Comput. 2(1):21–57, 2010, DOI 10.1007/s12532-010-0011-7 (primary; metadata only, not read)
13. P. E. Gill, D. P. Robinson, "A primal-dual augmented Lagrangian", Comput. Optim. Appl. 51(1):1–25, 2012, DOI 10.1007/s10589-010-9339-1 (primary; metadata only)
14. P. E. Gill, D. P. Robinson, "A Globally Convergent Stabilized SQP Method", SIAM J. Optim. 23(4):1983–2010, 2013, DOI 10.1137/120882913 (primary; Crossref abstract only)
15. F. E. Curtis, H. Jiang, D. P. Robinson, "An adaptive augmented Lagrangian method for large-scale constrained optimization", Math. Program. 152:201–245, 2015, DOI 10.1007/s10107-014-0784-y; author copy http://coral.ise.lehigh.edu/frankecurtis/files/papers/CurtJianRobi15.pdf (primary; read: abstract, §1, §4 setup, §5)
16. F. E. Curtis, D. P. Robinson, M. Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε^{-3/2}) for nonconvex optimization", Math. Program. 162:1–32, 2017, DOI 10.1007/s10107-016-1026-2; author copy http://coral.ise.lehigh.edu/frankecurtis/files/papers/CurtRobiSama17.pdf (primary; read: abstract, §1, §4, acknowledgments, appendix opening)
17. Corrigendum to Curtis, Robinson, Samadi (2017), Lemma 3.19, http://coral.ise.lehigh.edu/frankecurtis/files/errata/CurtRobiSama17_corrigendum.pdf (primary)
18. T. Chen, F. E. Curtis, D. P. Robinson, "A Reduced-Space Algorithm for Minimizing ℓ1-Regularized Convex Functions", arXiv 1602.07018 (2016-02-23); SIAM J. Optim. 27(3):1583–1610, 2017, DOI 10.1137/16M1062259 (primary; arXiv full text read: §1, §4.1–4.2, §5, acknowledgments, references)
19. C. You, D. P. Robinson, R. Vidal, "Scalable Sparse Subspace Clustering by Orthogonal Matching Pursuit", arXiv 1507.01238 (v1 2015-07-05 abstract and v3 2016-05-05 text); CVPR 2016, pp. 3918–3927, DOI 10.1109/CVPR.2016.425 (primary)
20. C. You, C.-G. Li, D. P. Robinson, R. Vidal, "Oracle Based Active Set Algorithm for Scalable Elastic Net Subspace Clustering", arXiv 1605.02633 (2016-05-09); CVPR 2016, pp. 3928–3937, DOI 10.1109/CVPR.2016.426 (primary; abstract, §1 and §2.2 read)
21. A. S. Berahas, F. E. Curtis, D. P. Robinson, B. Zhou, "Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization", arXiv 2007.10525 (2020-07-20); SIAM J. Optim. 31(2):1352–1379, 2021, DOI 10.1137/20M1354556 (primary; arXiv full text read: abstract, §1, §2 opening, §4, §5)
22. Corrigendum to Berahas, Curtis, Robinson, Zhou (2021), Corollary 3.14(a), http://coral.ise.lehigh.edu/frankecurtis/files/errata/BeraCurtRobiZhou21_corrigendum.pdf (primary)
23. F. E. Curtis, Y. Dai, D. P. Robinson, "A Subspace Acceleration Method for Minimization Involving a Group Sparsity-Inducing Regularizer", arXiv 2007.14951 (2020-07-29); SIAM J. Optim. 32(2):545–572, 2022, DOI 10.1137/21M1411111 (primary; arXiv §1 and experiment sections read; Crossref abstract)
24. F. E. Curtis, D. P. Robinson, "Regional Complexity Analysis of Algorithms for Nonconvex Smooth Optimization", arXiv 1802.01062 (v1 2018-02-04, v2 2018-08-24); Math. Program. 187:579–615, DOI 10.1007/s10107-020-01492-3 (primary; arXiv abstract only)
25. P. E. Gill, V. Kungurtsev, D. P. Robinson, "Negative Curvature and Second-order optimality for regularized SQP", arXiv 1205.2304 (2012-05-10) (primary; abstract page only)
26. Y. Dai, D. P. Robinson, "Inexact Proximal-Gradient Methods with Support Identification", arXiv 2211.02214 (2022-11-04), and Y. Dai, X. Qu, D. P. Robinson, "A Proximal-Gradient Method for Constrained Optimization", arXiv 2404.07460 (2024-04-11) (primary; abstracts only)
27. arXiv listing entries (title, authors, date of latest version) for the recent preprints 2509.00888, 2510.00417, 2505.15788, 2512.23166, 2605.08616, 2608.12665; their abstract pages were not opened in this run (primary metadata)
28. GitHub user daniel-p-robinson: repositories FaRSA-L1-C (2017–18), FaRSA (2020–21), nonlinear-optimization-course (2021–22), READMEs fetched 2026-10-16, https://github.com/daniel-p-robinson (primary)
29. GALAHAD source tree and headers of src/trs, src/rqs, src/dqp, src/cdqp, https://github.com/ralna/GALAHAD (primary, observed: package histories)
30. ORCID record 0000-0003-0251-4227, works list, https://pub.orcid.org/v3.0/0000-0003-0251-4227/works (primary)
31. F. E. Curtis, publications (chronological) page with author-copy links, https://coral.ise.lehigh.edu/frankecurtis/publications/publications-chronological/ (primary, collaborator site)
32. S. Na, M. Anitescu, M. Kolar, "An Adaptive Stochastic Sequential Quadratic Programming with Differentiable Exact Augmented Lagrangians", arXiv 2102.05320 (v1 2021-02-10) (primary for timing only; observed)
33. DBLP SPARQL, author pid 20/8222 (85 records), via scripts/dblp_works.py, https://sparql.dblp.org/sparql (secondary)
34. OpenAlex works filtered by ORCID 0000-0003-0251-4227, sorted by citations, and works W2102577682 and W21261227, https://api.openalex.org (secondary)
35. Semantic Scholar Graph API, author search "Daniel P. Robinson" and author 1780452 papers, https://api.semanticscholar.org (secondary)
36. Crossref REST API metadata and citation counts for about 30 DOIs cited above, https://api.crossref.org (secondary)
37. arXiv author search "Daniel P. Robinson" (148 hits, many other Robinsons), https://arxiv.org/search/ (secondary)
38. Wayback Machine snapshots of the homepage pages; the snapshot URLs came from agent 06's note and were re-fetched in this run, http://web.archive.org (secondary)
39. WebSearch result summary for "Daniel P. Robinson Lehigh Google Scholar citations optimization", 2026-10-16 (secondary; it found no Scholar profile)
