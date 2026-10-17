# Daniel P. Robinson: research trajectory (research agent 06)

- **Researcher**: Daniel P. Robinson. Lehigh University, Department of Industrial and Systems Engineering (ISE), since July 1, 2019. Earlier: Johns Hopkins University (JHU), Department of Applied Mathematics and Statistics (AMS), July 2011 to May 2019, as Assistant Professor. Before that, postdoctoral work at Oxford (with N. I. M. Gould) and Northwestern (with J. Nocedal). PhD in Mathematics, UC San Diego, 2007, advisor Philip E. Gill.
- **Dimension**: research trajectory. This covers the academic timeline, his lineage, the turns in direction and what triggered them, when he enters and leaves topics, and the last 12 months. It serves framework layer 2 (problem choice and timing) and gives evidence for layers 3 and 7.
- **Research date**: 2026-10-16
- **Sources consulted**: 58 (listed at the end). 44 are primary: his homepage and its archived publications and talks lists, his ORCID record, his own papers, abstracts and preprints, an essay-style commentary he wrote alone (TOP 2015), slides, errata, NSF award records, and Lehigh institutional pages that quote him. 14 are secondary: DBLP, OpenAlex, Crossref, MGP, and search-result summaries. **WebSearch calls used: 4.**
- **Local corpus**: `references/sources/papers/`, `talks/`, `essays/`, `software/` and `publications/` hold only `.gitkeep`. **Nothing here is from user-supplied material.** `private/` was not opened.
- **Sibling notes**: the Gill, Curtis and Wächter folders mention Robinson. I used them only as leads, for example the MGP id 112624 and the URLs of the Curtis errata. Every identifier below was re-checked with a tool in this run (DBLP SPARQL, Crossref, OpenAlex, arXiv abstract pages, NSF award API, or the document itself).

### How the evidence was gathered (and what failed)

- His homepage publications page (`/research/publications/`) and talks page (`/research/talks/`) are **broken today**. Each shows a raw `[bibtex file=bibsources/dpr.bib ...]` shortcode and no list. I recovered both lists from the Wayback Machine snapshots of 2025-08-09. Their content stops around 2020–21 for publications and mid-2019 for talks.
- DBLP's HTML and XML pages sit behind a bot wall (Anubis), so I used the DBLP SPARQL endpoint for pid 20/8222 (85 records, 2010–2026).
- The arXiv API returned HTTP 429. The arXiv `/abs/` pages worked and were used for nine preprints.
- The JHU AMS news page (Cloudflare 403) and the SIAM book front matter (403) **could not be read**.

### Tag legend

- **[stated]**: said by Robinson, or by a group whose voice includes him (co-authored abstracts, joint slides, a grant abstract he wrote as PI, quotes in institutional news, his own bio).
- **[practice]**: what the record shows he did (papers, dates, grants, talks, roles).
- **[observed]**: what other people report about him (department newsletters, prize committees, colleagues).
- **[inferred]**: my synthesis. Treat it as a hypothesis.
- **P / S**: primary / secondary source.

---

## 0. The trajectory in one paragraph (all [inferred], built from the sections below)

Robinson's career has a **stable methodological core**: second-order and active-set machinery for constrained optimization. The core includes regularized and convexified QP subproblems, active-set prediction with subspace "acceleration" phases, and merit, filter and funnel globalization. He has carried this core through **three application environments in turn**, and each one was set by **where he was and who was next door**, more than by a stated change of mind.

1. **Apprenticeship, 2003–2011 (UCSD, Oxford, Northwestern).** Under Gill he worked on primal-dual augmented Lagrangians, then on second-derivative SQP with Gould, then on LCP subspace acceleration with Nocedal and Pang. Each output line takes its senior partner's agenda.
2. **JHU, 2011–2019.** A split portfolio. (a) Classical NLP continued with Gould, Gill and Kungurtsev, and from 2014 more and more with Curtis. (b) A **second identity in computer vision and ML**, as optimization co-PI in René Vidal's subspace-clustering program, plus short excursions into healthcare (Saria) and power systems (Mallada).
3. **Lehigh, 2019–present.** The Curtis partnership becomes the centre. **Stochastic objectives under deterministic constraints** becomes the flagship (first preprint July 2020, funded by ONR since 2021). The sparse/active-set line grows from ℓ1 to group sparsity and then to proximal-gradient methods with general constraints. A new application turn goes to **fairness via hard constraints** (2024–26).

He tends to **enter a topic just after its foundations exist and then question its evaluation norms**. Examples: worst-case complexity entered about 4 years after ARC, followed by "regional" complexity; stabilized SQP, where he argued that the field's subproblem assumption is "unsatisfactory". His **exits are quiet**. No line is ever renounced. Collaborations simply stop after a move or after the partner's own move: Gould after 2017, Gill after 2020, Vidal after 2024. **The last 12 months** (2025-10-16 to 2026-10-16) are very active: four new arXiv preprints, two journal articles and one conference paper. The common thread is sampling, noise and constraints, plus the fairness application. He appears as "Professor" on the Lehigh faculty page, while his own homepage still says "Associate Professor".

---

## 1. Dated timeline

| Date | Event | Tag | Source |
|---|---|---|---|
| (childhood) | "I grew up in the small town of Hurleyville, New York, which is about 2 hours outside of New York City." | [stated] P | homepage |
| c. 1998–2002 (start year not verified) | Undergraduate at James Madison University (JMU): "When I started at James Madison University as a freshman undergraduate student, I intended to become a teacher." Undergraduate research posters: "Existence of a Derivative on a Finite Set" (MD-DC-VA Sectional Meeting, Loyola College, "? 2000"; Joint Mathematics Meetings undergraduate poster session, New Orleans, "? 2001") | [stated] P; [practice] P | homepage *Teaching*; archived talks list, section 3 |
| 2007 | PhD, UC San Diego, Mathematics. Dissertation "Primal-Dual Methods for Nonlinear Optimization", advisor Philip Edward Gill (MSC 65) | [practice] S | MGP id 112624; homepage ("in 2007") |
| Oct 2007 | First postdoc talk: "A Generalized Primal-dual Augmented Lagrangian", Oxford Computational Mathematics and Applications Seminar. This is the thesis topic, presented on arrival at Oxford | [practice] P | archived talks list |
| May 2008 | Talk "A Second Derivative SQP Method with Imposed Descent", SIAM Conference on Optimization, Boston. Same-titled report: Gould & Robinson, Oxford NA Report 08/09 (2008) | [practice] P | archived talks and publications lists |
| 2009 | Talks on "A Trust-funnel Algorithm for Nonlinear Programming" (Strathclyde, June 2009) and "An Interior-point Trust-funnel Algorithm for Large-scale Nonconvex Optimization" (INFORMS, Oct 2009). This idea reached print only in 2017 (see §5, F4) | [practice] P | archived talks list |
| 2010 (Jan–Mar online) | First three refereed papers, all with Gould: "A Second Derivative SQP Method: Global Convergence", *SIOPT* 20(4):2023–2048, DOI 10.1137/080744542; "… Local Convergence and Practical Issues", *SIOPT* 20(4):2049–2079, DOI 10.1137/080744554; Gould, Robinson, Thorne, "On solving trust-region and other regularised subproblems in optimization", *MPC* 2(1):21–57, DOI 10.1007/s12532-010-0011-7 | [practice] P | Crossref; DBLP |
| Aug 2010 online (2012 print) | Thesis line published: Gill & Robinson, "A primal-dual augmented Lagrangian", *COAP* 51(1):1–25, DOI 10.1007/s10589-010-9339-1 | [practice] P | Crossref |
| July 2010 | ICCOPT Santiago talk "High-order Methods for Overcoming Degeneracy in Interior-point Methods for Quadratic Programming". This became Gould, Orban, Robinson, "Trajectory-following methods for large-scale degenerate convex quadratic programming", *MPC* (2013), DOI 10.1007/s12532-012-0050-3 | [practice] P | archived talks list; DBLP |
| 2007–2011 | Postdoc years. Own bio: "He spent the next three years working with Nicholas I. M. Gould and Jorge Nocedal as a Postdoctoral Researcher in the Mathematical Institute at the University of Oxford and the Department of Industrial Engineering and Management Sciences at Northwestern University." Lehigh: "a Postdoctoral Researcher and Visiting Professor at Northwestern University". The exact dates are not verified (see Contradictions) | [stated] P; [observed] P | ICCOPT 2025 bio; Lehigh faculty page |
| Feb–Mar 2011 | Talks "Using Active-set Phases to Accelerate Optimization Algorithms" at JHU AMS (Feb 2011) and Lehigh ISE (Mar 2011). [inferred] These are job-market talks | [practice] P | archived talks list |
| July 2011 | Joins JHU AMS (ORCID employment: 2011-07 to 2019-05). Lehigh calls the rank "Assistant Professor" | [practice] P | ORCID; Lehigh welcome news 2019 |
| Jul 2011 (online) / 2012 print | Gould & Robinson, "A second-derivative SQP method with a 'trust-region-free' predictor step", *IMA J. Numer. Anal.* 32(2):580–601, DOI 10.1093/imanum/drq043 | [practice] P | Crossref |
| 2011 | "Corrigendum: Nonlinear programming without a penalty function or a filter" (Gould, Robinson, Toint), a technical report. The published erratum in *Math. Prog.* 131 (2011) 403–404, DOI 10.1007/s10107-011-0491-x, carries only Gould & Toint's names and cites the report (see Contradictions) | [practice] P | archived publications list; Springer erratum page; Crossref |
| Aug 2012 – Jul 2015 | First single-PI grant: NSF DMS-1217153, "New Active-Set Methods for Optimization and Complementarity Problems", JHU, $210,000. "The principal investigator and his student consider…" | [practice] P; abstract [stated] P | NSF award API |
| 2012 | Talks "Steering Augmented Lagrangian Methods" (ISMP Berlin, Aug 2012; INFORMS, Oct 2012). These became Curtis, Jiang, Robinson, "An adaptive augmented Lagrangian method for large-scale constrained optimization", *Math. Prog.* 152:201–245 (online Apr 2014), DOI 10.1007/s10107-014-0784-y | [practice] P | archived talks list; Crossref |
| 2012 | Professor Joel Dean Award for Excellence in Teaching, JHU (first of two) | [stated] P | ICCOPT 2025 bio |
| 2013 | Northwestern-era paper: Robinson, Feng, Nocedal, Pang, "Subspace Accelerated Matrix Splitting Algorithms for Asymmetric and Symmetric Linear Complementarity Problems", *SIOPT* 23(3):1371–1397, DOI 10.1137/110845094. Gill & Robinson, "A Globally Convergent Stabilized SQP Method", *SIOPT* 23(4):1983–2010, DOI 10.1137/120882913 | [practice] P | Crossref; DBLP |
| 2014 | First paper with Frank E. Curtis: Curtis, Johnson, Robinson, Wächter, "An Inexact Sequential Quadratic Optimization Algorithm for Nonlinear Optimization", *SIOPT* 24(3):1041–1074, DOI 10.1137/130918320. Filter SQP with Gould and Loh: *SIOPT* 24(1):175–209, DOI 10.1137/130920599, and *SIOPT* 25(3) (2015), DOI 10.1137/140996677 | [practice] P | DBLP |
| Sep 2014 – Aug 2018 | **Turn into computer vision and big data**: co-PI on NSF IIS-1447822 "BIGDATA: F: DKA: Learning a Union of Subspaces from Big and Corrupted Data" (PI René Vidal, JHU, $608,530) | [practice] P | NSF award API |
| 2014–2016 | INFORMS Vice-Chair for Nonlinear Optimization | [stated] P | ICCOPT 2025 bio |
| 2015 | First ML paper: Yang, Robinson, Vidal, "Sparse Subspace Clustering with Missing Entries", ICML 2015. Single-author papers: "Primal-Dual Active-Set Methods for Large-Scale Optimization", *JOTA* 166(1):137–171, DOI 10.1007/s10957-015-0708-x, and "Comments on: Critical Lagrange multipliers …", *TOP* 23(1):43–47, DOI 10.1007/s11750-015-0371-2. First student paper: Mohy-ud-Din & Robinson, "A Solver for Nonconvex Bound-Constrained Quadratic Optimization", *SIOPT* 25(4):2385–2407, DOI 10.1137/15M1022100 | [practice] P | DBLP; Crossref |
| 2014 | First (and only MGP-listed) PhD student graduates: Hassan Mohy-ud-Din, JHU 2014, "A Solver for Nonconvex Bound-Constrained Quadratic Optimization" | [practice] S | MGP id 203711 |
| May 2015 | Talk "A trust-region method with optimal complexity", CTU Prague. This is the first dated sign of the complexity line | [practice] P | archived talks list |
| 2015–2016 | **Healthcare excursion** with Suchi Saria: ISMP 2015 talk "Cost Sensitive Regularization in Model Prediction"; IJCAI 2016 paper (title discrepancy, see Contradictions); IET book chapter "Incorporating end-user preferences in predictive models" (2016); IDIES talks "Cost-sensitive Prediction: Applications in Healthcare" (Oct 2015, Oct 2016) | [practice] P | archived lists; DBLP |
| 2016 | Two CVPR papers with Chong You and Vidal (DOIs 10.1109/CVPR.2016.425, 10.1109/CVPR.2016.426). Cluster chair, ICCOPT 2016 Tokyo. Declined an invitation to the IMA "New Directions Short Course on Mathematical Optimization" (Aug 2016), recorded on his own talks list as "(invitation declined)" | [practice] P; [stated] P | DBLP; ICCOPT 2025 bio; archived talks list |
| 2017 | Peak year for the classical-NLP output: TRACE (Curtis, Robinson, Samadi, *Math. Prog.* 162, DOI 10.1007/s10107-016-1026-2); IPM trust funnel (Curtis, Gould, Robinson, Toint, *Math. Prog.*, DOI 10.1007/s10107-016-1003-9); stabilized SQP superlinear (Gill, Kungurtsev, Robinson, *Math. Prog.* 163, DOI 10.1007/s10107-016-1066-7) and global (*IMA JNA* 37, DOI 10.1093/imanum/drw004); FaRSA ℓ1 (Chen, Curtis, Robinson, *SIOPT* 27(3), DOI 10.1137/16M1062259). Last paper with Gould: "A dual gradient-projection method for large-scale strictly convex quadratic problems", *COAP* (2017), DOI 10.1007/s10589-016-9886-1 | [practice] P | DBLP; Crossref |
| Aug 2017 – Sep 2023 | Co-PI on NSF IIS-1704458 "III: Medium: Non-Convex Methods for Discovering High-Dimensional Structures in Big and Corrupted Data" (PI Vidal, $1,150,000). Co-PI on NSF 1736448 "AMPS: Dynamics-Aware Algorithms for Real-Time Structured Fault Detection in Power Systems" (PI Enrique Mallada, $230,728, 2017–21) | [practice] P | NSF award API |
| Fall 2017 | Hosts Curtis at JHU during Curtis's sabbatical: "with shorter stints at Johns Hopkins University in the Fall (hosted by Daniel P. Robinson)" | [observed] P | Lehigh OptML news, Aug 28, 2017 |
| 2018 | Second Joel Dean teaching award. "Concise complexity analyses for trust region methods" (Curtis, Lubberts, Robinson), *Optim. Lett.* 12(8), DOI 10.1007/s11590-018-1286-2, wins the **2018 Optimization Letters Best Paper Award** (announced Nov 12, 2019; "$1,000 USD prize and a plaque") | [stated] P (bio); [observed] P (newsletter) | ICCOPT 2025 bio; Lehigh ISE newsletter 2019–20; OptML news |
| Jan 2018 | Curtis & Robinson's joint talk "How to Characterize the Worst-Case Performance of Algorithms for Nonconvex Optimization" (U.S.–Mexico Workshop, Curtis presenting) questions the field's complexity yardstick. This led to "Regional complexity analysis of algorithms for nonconvex smooth optimization", *Math. Prog.* 187:579–615 (online Apr 2020), DOI 10.1007/s10107-020-01492-3 | [stated, collective] P; [practice] P | slides; Crossref |
| Oct 2018 – Apr 2019 | Seminar tour of **13 universities** (UNC Charlotte, Minnesota, Michigan, Colorado State, UW-Madison, Lehigh ISE in Feb 2019, Florida, Iowa, WPI, CU Denver, Rutgers, NYU Courant, SMU). Ten of the talks are titled "Effectively Using Negative Curvature in Optimization and Scalable Methods for Subspace Clustering". [inferred] This is a job-market tour, and the two-strand title is how he presented himself | [practice] P | archived talks list |
| July 1, 2019 | Joins Lehigh ISE as Associate Professor. "I plan to use my expertise in optimization to make impactful contributions to application areas in computer vision, healthcare, and beyond" | [practice] P; [stated] P | Lehigh welcome news; OptML news |
| 2019 | Curtis & Robinson, "Exploiting negative curvature in deterministic and stochastic optimization", *Math. Prog.* 176 (special issue on nonconvex optimization for statistical learning), DOI 10.1007/s10107-018-1335-8. This is his first stochastic-optimization paper in an optimization journal | [practice] P | DBLP; archived publications list |
| Jul 15, 2020 – Jun 30, 2024 | NSF DMS-2012243 "An Accelerated Decomposition Framework for Structured Sparse Optimization" (PI Robinson, co-PI Curtis, Lehigh, $200,000) | [practice] P | NSF award API |
| Jul 20, 2020 | **Stochastic SQP launched**: Berahas, Curtis, Robinson, Zhou, arXiv 2007.10525 (Lehigh ISE TR 20T-012); *SIOPT* 31(2):1352–1379 (2021), DOI 10.1137/20M1354556 | [practice] P | arXiv abs page; Crossref |
| Sep 2020 | Robinson and Curtis "won the call to organize" ICCOPT 2022 at Lehigh. Postdoc Michael O'Neill arrives, "supervised by OptML faculty members Frank E. Curtis and Daniel P. Robinson" | [observed] P | OptML news |
| 2021– | "This research is funded by the Office of Naval Research since 2021" (stochastic constrained thrust) | [stated] P | homepage *Current Research* |
| 2021–2022 | Last flurry of the Vidal line: ICML 2021 (×2), AISTATS 2021, *IEEE TIT* 2021 (DOI 10.1109/TIT.2021.3067280), *TPAMI* 2022 (DOI 10.1109/TPAMI.2020.3035599). Group-sparsity paper Curtis, Dai, Robinson, *SIOPT* 32(2):545–572 (2022), DOI 10.1137/21M1411111 | [practice] P | DBLP; Crossref |
| Feb 2022 | Co-founder (with Davison and Venkitasubramaniam) of Lehigh's new MS in Data Science (described as "associate professor") | [observed] P | Lehigh news, Feb 15, 2022 |
| July 23–28, 2022 | Co-chair (with Curtis) of ICCOPT 2022 + MOPTA at Lehigh | [practice] P | ICCOPT 2022 site |
| 2023–2024 | Stochastic-SQP family matures: complexity (*Math. Prog.* 205, DOI 10.1007/s10107-023-01981-1); inexact (*IJOO* 6(3–4), DOI 10.1287/ijoo.2022.0008); inequality + equality (*SIOPT* 34(4), DOI 10.1137/23M1556149); rank-deficient Jacobians (*MOR* 49(4), DOI 10.1287/moor.2021.0154). **Fairness entry**: Curtis, Liu, Robinson, "Fair machine learning through constrained stochastic optimization and an ε-constraint method", *Optim. Lett.* (2024), DOI 10.1007/s11590-023-02024-6 | [practice] P | Crossref; DBLP |
| Sep 2024 | ONR award, 3 years, $621K, Curtis and Robinson: "Stochastic Algorithms for Data-Driven Constrained Continuous Optimization" | [practice] P; quote [stated] P | Lehigh news, Sep 12, 2024 |
| Sep 2024 | As MS Program Director, he leads the redesign of the ISE master's portfolio, including a new "Master's Program in Optimization". Quote: "I am very excited about the redesign of our master's programs!" | [practice] P; [stated] P | Lehigh news, Sep 25, 2024 |
| 2024 | Last Vidal-line paper found: Shinde, Ding, Robinson, Vidal, "Geometric Analysis of Nonlinear Manifold Clustering", NeurIPS 2024 | [practice] S | DBLP |
| Jul 21, 2025 | ICCOPT 2025 (USC) talk in "Parallel Sessions 3C: Methods for Large-Scale Nonlinear Optimization III" (listed with O'Neill, Zhou, Chakraborty). Talk title not retrieved | [practice] P | ICCOPT 2025 sched page |
| Sep 22, 2025 | Book: Curtis & Robinson, *Practical Nonconvex Nonsmooth Optimization*, SIAM (MOS-SIAM Series), DOI 10.1137/1.9781611978599, xxvi + 483 pp. | [practice] P | Crossref; Lehigh news, Jan 22, 2026 |
| Oct 2025 – Oct 2026 | Last 12 months: see §7 | | |
| as of 2026-10-16 | Lehigh faculty page: "Professor"; "Ph.D., Mathematics, University of California, San Diego"; "Areas of Research: Computational Optimization, Machine Learning, Data Science, Computer Vision Applications". His homepage still says "Associate Professor" | [practice] P | Lehigh faculty page; homepage |

---

## 2. Lineage

### 2.1 Upward

- **PhD advisor**: Philip E. Gill (UCSD). [practice, S] MGP 112624.
  - The thesis idea runs through his later work, by his own account. In the TOP commentary (2015, p. 45 region; read in Springer's HTML full text) he traces the stabilized-SQP method back to "a certain BCQP subproblem whose objective approximates a primal–dual augmented Lagrangian function (Robinson 2007; Gill and Robinson 2012)". [stated] P
- **Postdoctoral mentors**: N. I. M. Gould (Oxford/RAL) and J. Nocedal (Northwestern), per his own bio. [stated] P
  - The output matches: 7 papers with Gould (2010–2017) and 1 with Nocedal (with Feng and Pang, *SIOPT* 2013). [practice] P (DBLP)

### 2.2 Downward (advisees)

- **MGP** lists one student: Hassan Mohy-ud-Din (JHU 2014). [practice] S
- **His own talks list** has a section "4. Undergraduate, Masters, PhD, and Postdoctoral Advisee Presentations" [stated] P. It names these JHU-era advisees, without distinguishing their roles:
  - Hao Jiang: adaptive / steering augmented Lagrangian, 2013–14
  - Yueling Loh: filter SQP 2014–15, and a stochastic-programming nurse-staffing talk in 2015
  - Hassan Mohy-ud-Din: nonconvex BCQP, 2015
  - Rachael E. Tappenden: flexible ADMM, 2014–15. [inferred] A postdoc (Tappenden & Robinson, *J. Sci. Comput.* 2017, DOI 10.1007/s10915-016-0306-6).
  - Tianyi Chen: FaRSA, 2016–17
  - Tianyu Ding: DPCP, 2019
- **Lehigh era**: OptML lists current PhD students who co-author with Robinson: Lingjun Guo, Zahra Khatti, Xiaoyi Qu, Qi Wang, Chia-Yuan Wu, Lara Zebiane. Yutong Dai is a former student, now at Salesforce. Formal advisor roles were **not verified**, because OptML students are often co-supervised with Curtis (see Gaps). [practice] P (OptML people page; DBLP author lists)
- **Postdocs supervised jointly with Curtis**: Albert Berahas (left Aug 2020 for Michigan) and Michael O'Neill (from Sep 2020). [observed] P (OptML news)
- **Where advisees went**: Tianyi Chen and Tianyu Ding later appear with Microsoft co-authors on "Automatic Joint Structured Pruning and Quantization…" (CVPR 2025, DOI 10.1109/CVPR52734.2025.01419). [practice] S (DBLP). [inferred] Former students pull him back into ML venues after the Vidal grants ended.

---

## 3. The turns and what triggered them

Each turn lists: trigger, entry timing, exit timing, evidence type.

### T1 (2007–2011): from the thesis topic to his postdoc hosts' agendas

- **Practice**. The 2007 Oxford talk is on the thesis topic, "A Generalized Primal-dual Augmented Lagrangian". Within 7 months he moves to second-derivative SQP with Gould: a SIAM OP08 talk, Oxford NA report 08/09, and two *SIOPT* papers in 2010.
- **Problem framing** [stated, collective, P] (Gould & Robinson, *SIOPT* 20(4) abstract): "Although second derivative information may often be calculated, there is little practical theory that justifies exact-Hessian SQP methods. In particular, the resulting quadratic programming (QP) subproblems are often nonconvex, and thus finding their global solutions may be computationally nonviable."
- **Trigger** [inferred]: the move to Oxford and Gould's group. The new topic sits right next to the thesis: SQP subproblems that need not be solved globally.
- **Northwestern**: the LCP and active-set "acceleration phase" work with Nocedal, Feng and Pang. Talks: "LCP and SQP" (SIAM OP11, May 2011); "Using Active-set Phases to Accelerate Algorithms" (Lehigh, Mar 2011). [practice] P

### T2 (2011–2015): subspace acceleration becomes his own research programme

- **Trigger, in his own words** [stated, PI-written NSF abstract, P; DMS-1217153, 2012]: "Subspace phases have been used with great success to enhance basic algorithms … This success, however, has masked a prevailing weakness: all iterates generated must remain in the subspace. An acceleration phase has the added flexibility of selectively enlarging the subspace, when deemed necessary."
- **What came out of it** [practice]:
  - Curtis, Han, Robinson, *COAP* 2015 (DOI 10.1007/s10589-014-9681-9)
  - Robinson, *JOTA* 2015 (single author)
  - Mohy-ud-Din & Robinson, *SIOPT* 2015
  - then FaRSA ℓ1 (*SIOPT* 2017; *OMS* 2018, DOI 10.1080/10556788.2017.1415336)
  - then group sparsity (*SIOPT* 2022)
  - then overlapping groups (Dai & Robinson, *OMS* 39(4), 2024, DOI 10.1080/10556788.2024.2346643)
  - then proximal-gradient for equality constraints (Dai, Qu, Robinson, *SIOPT* 35(4):2654–2683, 2025, DOI 10.1137/24M1653586)
  - then general constraints (Curtis, Qu, Robinson, arXiv 2512.23166).
- [inferred] **This is his longest-running self-owned thread, now 14 years.** It moved from LCP and QP into ML regularization when ℓ1 problems became the common workload.
- **The application motive is restated each time** [stated, P]:
  - Homepage on group sparsity: "Standard one-norm regularization techniques fail to achieve this goal."
  - NSF DMS-2012243 (2020): "Despite the success of existing methods for sparse problems, their inadequacy for many modern machine learning and other types of problems has gradually been noticed by researchers."

### T3 (2014–2024): the computer-vision identity, bought by grant co-PIship

- **Trigger** [practice, P]: co-PI on Vidal's NSF BIGDATA award (Sep 2014). The first paper followed in 2015 (ICML). The JHU setting matters: his 2011 seminar "Matrix Splitting Methods for BQP and LCP" was given at JHU's Center for Imaging Science (Oct 2011) [practice] P.
- **The research rationale (Vidal-led, collective)** [stated, P; NSF 1704458 abstract]: "existing theory and algorithms rely on the assumption that high-dimensional data can be well approximated by low-dimensional structures. While this assumption is adequate for some datasets, e.g., images of faces under varying illumination, it may be violated in many emerging datasets, e.g., 3D point clouds."
- **His homepage claim** [stated, P]: DPCP "has routinely been shown to outperform other state-of-the-art algorithms."
- **Entry timing** [inferred]: he joined an established program as its optimization specialist, rather than founding the topic.
- **Exit timing** [practice, S (DBLP)]:
  - 13 Vidal co-authored items fall in 2012–19 and 9 in 2020–26.
  - After 2021 there are only three: TPAMI 2022 (submitted 2020), IEEE TAC 2023 (a 2018 idea), and NeurIPS 2024.
  - The NSF grant ended 2023-09-30, and the NSF record now lists Vidal at upenn.edu.
  - [inferred] The line ended when the grant ended and the two PIs were in different places. No stated reason was found.
- **Self-presentation** [practice, P]:
  - 2016: "I have been particularly interested in applications in Computer Vision" (homepage; the page is undated).
  - 2018–19 job talks: "… and Scalable Methods for Subspace Clustering".
  - 2026 Lehigh profile: "Computer Vision Applications" is still listed among his research areas.

### T4 (2015–2021): complexity, entered late and then questioned

- **Entry** [practice, P]:
  - First complexity talk in May 2015 ("A trust-region method with optimal complexity").
  - TRACE (*Math. Prog.* 2017), inexact regularized Newton (*IMA JNA* 39(3), DOI 10.1093/imanum/dry022), trust-funnel complexity (*SIOPT* 28(2), DOI 10.1137/16M1108650), concise TR analyses (*Optim. Lett.* 2018; best paper award), and TR Newton-CG with Royer & S. J. Wright (*SIOPT* 31(1), DOI 10.1137/19M130563X).
- **Timing relative to consensus** [inferred]: the joint 2018 slides date the field's frame as "Cartis, Gould, Toint (2011), the ARC method" plus a 2017 ML wave. So he entered about 4 years after ARC set the O(ε^-3/2) target, and then matched it within a trust-region framework.
- **Turn against the yardstick** [stated, collective, P; slides of Jan 2018, Curtis presenting, "joint work with Daniel P. Robinson"]:
  - "However, there remains a large gap between theory and practice!"
  - "Is this the best way to characterize our algorithms?"
  - "We're admitting: Our approach does not give the complete picture. But we believe it is useful!"
  - and, on the summary slide, "For some functions, there are holes, but for others the characterization is complete."
- **Result**: regional complexity, *Math. Prog.* 2021.

### T5 (2013–2020): stabilized SQP, his most explicit statement of a minority position

- [stated, P; Robinson, *TOP* 23(1) 2015, single author]:
  - On method values: "As I believe that algorithms should be practically and theoretically sound, I will focus on the practical aspects of the globalization process."
  - On the field: "it is probably safe to say that the best way to globalize sSQP is not yet clear."
  - On the disputed assumption: "I belong to the second group of researchers who believe that the assumption placed on the subproblem solutions is unsatisfactory and should be avoided if possible."
  - An admission: "Although the synchronization of these two aspects into a practical single-phase algorithm proved more difficult than anticipated, the global and local convergence results do not require an assumption about which subproblem solutions are computed."
  - Criteria for the next method: "(i) They are applicable to problems with both equality and inequality constraints. (ii) The methods are superlinearly convergent under weak assumptions. (iii) … globally convergent under standard assumptions. (iv) … substantially outperform Newton-based methods on degenerate problems. (v) … comparable to Newton-based methods on nondegenerate problems." [The ellipses replace the repeated words "The methods are".] He adds: "I believe that the method proposed in Gill et al. (2013, 2014) comes the closest to satisfying these criteria, but I am sure that better methods are possible."
- **Exit** [practice, P]:
  - The last Gill paper is "A Shifted Primal-Dual Penalty-Barrier Method for Nonlinear Optimization", *SIOPT* 30(2):1067–1093 (2020), DOI 10.1137/19M1247425, first presented as "A Shifted Penalty-barrier Method for NLP" at MOPTA in July 2015.
  - After 2020 no stabilized-SQP or penalty-barrier paper appears.
  - Kungurtsev continues as a co-author on the stochastic interior-point line (*SIOPT* 35(2), 2025, DOI 10.1137/23M1569460).

### T6 (2019–present): stochastic objective, deterministic constraints

- **The stepping stone** [practice, P]: Curtis & Robinson, "Exploiting negative curvature in deterministic and stochastic optimization", *Math. Prog.* 2019. It sits in a special issue on statistical learning, and the talk was "Negative Curvature in Deterministic and Stochastic Nonconvex Optimization" (Jan 2018).
- **Launch** [practice, P]: arXiv 2007.10525, v1 2020-07-20.
- **Construction strategy** [stated, collective, P; abstract]: "As a starting point for this stochastic setting, an algorithm is proposed for the deterministic setting that is modeled after a state-of-the-art line-search SQP algorithm, but uses a stepsize selection scheme based on Lipschitz constants … This sets the stage for the proposed algorithm for the stochastic setting, for which it is assumed that line searches would be intractable."
- **Why now, in his framing** [stated, P; homepage *Current Research*]: "Such problems are just now emerging in data science since large-scale decision-making applications demand the ability to solve problems with more realistic, nonlinear systems of equations/inequalities that impose constraints on the decision variables." Applications listed there: constrained CNN training, PDE-constrained inverse problems, constrained MLE, multi-stage modelling, power engineering.
- **Funding trigger** [practice, P]: ONR from 2021; renewed with $621K in Sep 2024.
  - His 2024 rationale [stated, P]: "Machine learning and artificial intelligence will continue to play an increasing role in defense operations, such as for motion tracking systems and the operation of autonomous vehicles."
  - The project frame, in the department's words [observed, P]: "optimization algorithms for informed learning, where prior information about a system or process can be incorporated in the learning process rather than rely on purely data-driven techniques."
- **Entry timing** [inferred, partial check only]: Berahas et al. (arXiv July 2020) predates Na, Anitescu, Kolar, "An Adaptive Stochastic Sequential Quadratic Programming with Differentiable Exact Augmented Lagrangians" (arXiv 2102.05320, v1 Feb 10, 2021). This makes the Lehigh group an early entrant **before** the topic became crowded. I did not do a systematic priority search.
- **Status**: still active in 2026. See §7 for progressive sampling, the local-linear convergence result, and noisy active-set identification.

### T7 (2024–present): fairness through hard constraints

- **Bridge** [practice, P]: Curtis, Liu, Robinson, *Optim. Lett.* 2024 (ε-constraint method).
- **Stated logic of the turn** [stated, collective, P; Khatti, Robinson, Curtis, arXiv 2505.15788 abstract]: "Rather than rely on regularizers (that lead to optimization problems that are difficult to solve) and corresponding regularization parameters (that can be expensive to tune), we propose a strategy that employs hard constraints so that specific tolerances for unfairness can be enforced without the complications associated with the use of regularization."
- [inferred] A constrained-optimization specialist re-frames an ML problem as a constrained problem. The pattern matches T6.
- **Federated / collaborative branch** with student Chia-Yuan Wu:
  - arXiv 2409.09532 (Sep 2024)
  - *IJOO* 8(3):248–265 (2026), DOI 10.1287/ijoo.2025.0091
  - FLICS 2026, pp. 239–247, DOI 10.1109/FLICS70075.2026.11621940
  - arXiv 2605.08616
- **Earlier stated interest** [stated, P; Feb 2022]: "How do we understand and use data in a responsible way, and apply and improve algorithms to avoid bias?"

### Short excursions that ended (all [practice] P/S)

| Line | Window | Partners | Last item | Trigger (stated or inferred) |
|---|---|---|---|---|
| Cost-sensitive / healthcare prediction | 2014–2016 (publications); working paper listed in 2020 | Saria (JHU); Ahn and Pang (working paper) | IJCAI 2016; IET chapter 2016; the 2020 working paper "A mixed-integer nonlinear programming approach for cost-sensitive prediction" was never found in print | JHU environment. Septic-shock prediction is still cited as motivation in NSF DMS-2012243 (2020) and in the 2022 news piece [stated] |
| Power-system fault detection, sparse recovery on graph incidence matrices | 2017–2021 | Mallada, Kaba, Zhao, Vidal | *IEEE TIT* 2021; ICML 2021 | NSF AMPS 1736448 (2017–21) [practice] |
| Continuous-time and dynamical-systems views of ADMM and acceleration | 2018–2023 | França, Vidal, Sulam | *IEEE TAC* 2023 (DOI 10.1109/TAC.2023.3238857) | JHU/Vidal collaboration [inferred] |
| ADMM for big data | 2015–2017 | Tappenden | *J. Sci. Comput.* 2017 | [inferred] the postdoc's project |

---

## 4. Collaboration eras (counts from DBLP pid 20/8222, CoRR duplicates excluded; [practice] S)

| Era | Refereed records (optimization journals / ML-CV-engineering venues) | Top co-authors |
|---|---|---|
| 2010–2011 (postdoc) | 3 / 0 | Gould 3 |
| 2012–2019 (JHU) | 23 / 13 | Vidal 13, Curtis 11, C. You 7, Gould 6, Gill 3, H. Jiang 3 |
| 2020–2026 (Lehigh) | 13 / 12 | Curtis 11, Vidal 9 (mostly 2020–21), Y. Dai 5 |

- DBLP misses several journal papers I verified separately (*IMA JNA* 2012, 2017, 2019, 2020; *TOP* 2015; *Phys. Rev. E* 103 (2021) 053304, DOI 10.1103/PhysRevE.103.053304; *J. Stat. Mech.* 2020 124008, DOI 10.1088/1742-5468/abcaee; the 2025 book; *IJOO* 2026). The counts above are therefore lower bounds.
- **Author order**: papers with Curtis use alphabetical order (e.g. "Curtis, Guo, Robinson"). Student-driven ML papers put the student first (e.g. Dai, Qu, Robinson; Khatti, Robinson, Curtis). [practice] P (arXiv pages)
- [inferred] Robinson is last author only where alphabetical order happens to put him last, so author position says little about his role.

---

## 5. Failures, abandoned directions, corrections, retitlings

| # | Item | Evidence | Tag |
|---|---|---|---|
| F1 | **Five working papers listed around 2020 that never appeared** (absent from DBLP and OpenAlex through Oct 2026; no Crossref title match): (a) Robinson, "A primal-dual matrix-free algorithm for strictly convex quadratic problems", "in preparation for submission to Mathematical Programming Computation"; (b) Robinson, "A truncated-Newton algorithm for unconstrained optimization with strong global and local convergence properties", "in preparation for submission to the IMA Journal on Numerical Analysis" (talk "An Enhanced Truncated-Newton Algorithm for Large-scale Optimization", SIAM OP17, May 2017); (c) Basu, Ding, Robinson, "A reduced-space accelerated optimization algorithm for low-rank optimization" (talks "Low-rank Convex Optimization", ICCOPT 2016 and EUROPT 2017); (d) Ahn, Pang, Robinson, MINLP for cost-sensitive prediction; (e) You, Vidal, Robinson, "Basis pursuit and orthogonal matching pursuit for subspace-preserving recovery: theoretical analysis", "Under Review", JMLR, 2020 (arXiv 1912.13091; no journal record found). [inferred] Several are **single-author** projects that lost out to collaborative lines after the 2019 move | archived publications list (2025 snapshot); DBLP; OpenAlex; Crossref title queries | [practice] P |
| F2 | **Talk without any matching paper**: "Upper-Bounding Models for Optimization" (DIMACS/TRIPODS/MOPTA, Aug 2018) | archived talks list; DBLP | [practice] P |
| F3 | **Published corrections**: (a) TRACE, Curtis, Robinson, Samadi *Math. Prog.* 2017. Corrigendum: "A corrected statement and proof of Lemma 3.19 from the published paper is provided below." It adds: "This means that the inequality in the published paper is correct, but not as tight as it could have been." (b) Berahas, Curtis, Robinson, Zhou, *SIOPT* 2021: "A corrected statement of Corollary 3.14(a) from the published paper is below." (c) In 2011 he co-authored a corrigendum report for Gould & Toint's "Nonlinear programming without a penalty function or a filter" (published erratum DOI 10.1007/s10107-011-0491-x). [inferred] Correcting a senior colleague's paper as a postdoc shows close reading of others' proofs | errata PDFs on Curtis's Lehigh site; Springer erratum page | [practice] P |
| F4 | **Long incubation**: the interior-point trust funnel was first presented in 2009 (Strathclyde; INFORMS) and again in 2014 as "A Matrix-free Trust-funnel Barrier-SQP Method for Extreme-scale Constrained Optimization" (SIAM OP14). ORCID lists a 2014 item "An interior-point trust-funnel algorithm for nonlinear optimization using a squared-violation feasibility measure" (no identifier). It was published in *Math. Prog.* only in 2017, with "squared-violation" dropped from the title. Lag: about 8 years | archived talks list; ORCID; DBLP | [practice] P |
| F5 | **Admitted difficulty**: stabilized-SQP globalization "proved more difficult than anticipated" (TOP 2015) | TOP 2015 | [stated] P |
| F6 | **Admitted scope limit**: group-sparse subspace acceleration, *SIOPT* 2022 abstract: "For solving problems when the number of data points is smaller than the number of features, algorithms that focus on solving a dual problem may be more efficient than our approach, which solves the primal problem." | Crossref abstract | [stated, collective] P |
| F7 | **Venue change**: "A nonsmooth dynamical systems perspective on accelerated extensions of ADMM" was listed around 2020 as "SIAM J. Control Optim., 2020" (under "Working Papers"). It appeared in *IEEE Trans. Autom. Control* 2023. Whether this was a rejection is **unknown** | archived publications list; DBLP | [practice] P; reason not found |
| F8 | **Report → journal retitling (not a failure)**: the 2008 "Second Derivative SQP Method with Imposed Descent" report became *SIOPT* 2010 "… Global Convergence". The abstract keeps the idea: "an explicit descent-constraint is imposed on certain QP subproblems" | Crossref abstract; archived lists | [practice] P; link [inferred] |
| F9 | **Report without a journal version found**: Gill, Kungurtsev, Robinson, "Distance-to-solution estimates for optimization problems with constraints in standard form", CCoM 16-01 (April 2016) | archived publications list; DBLP (absent) | [practice] P |
| F10 | **Rejected papers, referee reports, retractions**: none found. He has no OpenReview presence relevant to this search. | — | gap |

---

## 6. Era and resource context

| Period | Position and seniority | Team and resources | Typical venues and tools |
|---|---|---|---|
| 2003?–2007 | PhD student, UCSD (Gill) | Gill group | thesis; later COAP 2010/12 |
| 2007–c.2011 | Postdoc, Oxford (Gould) then Northwestern (Nocedal), also "Visiting Professor" at Northwestern | single junior researcher with senior hosts; the Oxford NA and RAL report series | *SIOPT*, *MPC*, *IMA JNA*; talks in the UK (Bath–RAL, ERGO, Warwick) |
| 2011–2019 | Assistant Professor, JHU AMS; "founding member" of JHU MINDS; helped set up the JHU MS in Data Science | NSF single-PI grant $210K (2012–15, "his student"); co-PI on Vidal's $608K (2014–18) and $1.15M (2017–23) grants; Mallada's $231K (2017–21); a few PhD students plus a postdoc (Tappenden) | split portfolio: *SIOPT*, *Math. Prog.* + ICML, NeurIPS, CVPR, ICCV, ECCV, AISTATS, IJCAI |
| 2019–present | Associate Professor, Lehigh ISE (2019), later "Professor" (faculty page; date unknown); MS Program Director; MS Data Science co-founder (2022); Optimization Online "Area Coordinator" (2026 news); AE for *COAP*, *J. Sci. Comput.*, *Optim. Lett.*, *OMS*, *MOR* (homepage) | OptML group with Curtis and Vicente (10 PhD students listed); NSF DMS $200K (2020–24, PI); ONR since 2021, and $621K in 2024 with Curtis; shared postdocs (Berahas, O'Neill) | *SIOPT*, *Math. Prog.*, *MOR*, *IJOO*, *OMS*; ML venues now through students (CVPR 2025, FLICS 2026); Lehigh ISE technical-report series; arXiv math.OC |

- [inferred] Compute appears throughout as laptop-scale MATLAB- or Python-style prototypes on CUTEst-type and ML benchmark sets. **I did not verify** this from code or appendices; it is agent 03's remit.
- [practice] P: the 2012 NSF abstract promised "freely available software". The homepage has **no software page** today.

---

## 7. The last 12 months (2025-10-16 to 2026-10-16)

| Date | Item | Tag | Source |
|---|---|---|---|
| 2025-10-01 (v2 2026-05-13) | Curtis, Guo, Robinson, "Progressively Sampled Equality-Constrained Optimization", arXiv 2510.00417 (Lehigh ISE TR 25T-017). Claim: "solving a sequence of problems defined through progressive sampling yields a better worst-case sample complexity bound compared to solving a single problem with the full sets of samples" | [practice] P; claim [stated, collective] | arXiv abs |
| 2025-10-21 / 22 | v2 and v3 of Khatti, Robinson, Curtis, "Fair Supervised Learning Through Constraints on Smooth Nonconvex Unfairness-Measure Surrogates", arXiv 2505.15788 (TR 25T-007; v1 May 2025) | [practice] P | arXiv abs |
| 2025-12-05 | Dai, Qu, Robinson, "A Proximal-Gradient Method for Equality Constrained Optimization", *SIOPT* 35(4):2654–2683, DOI 10.1137/24M1653586 | [practice] P | Crossref |
| 2025-12-29 (v2 2026-01-15) | Curtis, Qu, Robinson, "A Proximal-Gradient Method for Solving Regularized Optimization Problems with General Constraints", arXiv 2512.23166. **Submitted by Robinson himself** (the other recent preprints were submitted by Curtis or by students). Experiments on "a subset of the CUTEst test problems and sparse canonical correlation analysis problems" | [practice] P | arXiv abs |
| 2026-01-22 | Lehigh news on the book. It describes "best paper awards at optimization and computational mathematics venues" (plural; only one verified) and "Area Coordinator for Optimization Online" | [observed] P | Lehigh news |
| 2026-01-29 online (vol. 8(3), Jul 2026) | Wu, Curtis, Robinson, "A Bilevel Optimization Approach for Computing Synthetic Data to Mitigate Unfairness in Collaborative Machine Learning", *IJOO* 8(3):248–265, DOI 10.1287/ijoo.2025.0091 | [practice] P | Crossref; OpenAlex |
| 2026-05-09 | Wu, Curtis, Robinson, "Robust Server Defense Against Unreliable Clients in One-Shot Fair Collaborative Machine Learning", arXiv 2605.08616, "Accepted at the 2nd International Conference on Federated Learning and Intelligent Computing Systems (FLICS 2026)". Proceedings version (Jun 2026): pp. 239–247, DOI 10.1109/FLICS70075.2026.11621940 | [practice] P | arXiv abs; Crossref |
| 2026-08-12 | Curtis, Guo, Robinson, "A Local-Linearly Convergent Algorithm for Nonconvex Equality-Constrained Optimization", arXiv 2608.12665 (TR 26T-013). It extends "a recent Gradient-Eigenstep Algorithm by Goyens et al." (Fletcher's augmented Lagrangian) and uses it "as an iteration-efficient subproblem solver in the context of a progressive sampling strategy" | [practice] P | arXiv abs |
| ongoing | ONR award (Sep 2024, 3 years) "Stochastic Algorithms for Data-Driven Constrained Continuous Optimization" | [practice] P | Lehigh news |
| as of 2026-10-16 | Faculty page title "Professor"; homepage not updated (still "Associate Professor"; broken publication and talk lists; *Current Research* still cites NSF-1704458 as continuing although the NSF record ends it on 2023-09-30) | [practice] P | pages fetched 2026-10-16 |
| not found | No 2026 talk listing was found. MOPTA 2026 (Lehigh, Aug 18–19, 2026) plenaries do not include him, according to a search-result summary only. No new grants or awards were found for 2025–26 | gap | WebSearch summary (S) |

- **Direction of the last year** [inferred]: (1) **sample-complexity and progressive-sampling theory for constrained finite-sum problems**, which has become a two-paper mini-programme with Guo; (2) **proximal methods with general constraints**, the sparse line meeting the constraints line; (3) **fair and collaborative ML**, driven by students Wu and Khatti; (4) **noise-robust active-set identification** (arXiv 2509.00888, Aug 31, 2025, just outside the window). His classical deterministic second-order SQP work is absent from the last 12 months.

---

## 8. Patterns for the skill (all [inferred]; each points back to the evidence above)

1. **Carry one toolkit across application regimes.** Turns in his career change the *setting* (deterministic → stochastic; LCP → ℓ1 → group sparsity → general constraints). The machinery stays the same: active-set and subspace phases, SQP decompositions, merit functions. (T2, T6)
2. **Build the deterministic analogue first, then remove the step that becomes intractable.** In stochastic SQP, the line search was replaced by Lipschitz-based steps. (T6 abstract)
3. **Prefer hard constraints to tuned regularizers when the requirement is a tolerance.** (T7)
4. **Question the field's evaluation yardstick once you have met it.** He matched optimal complexity first (TRACE), then argued that complexity "does not give the complete picture" and proposed regional analysis. (T4)
5. **Name the assumption you refuse to make.** The subproblem-solution assumption in sSQP: "unsatisfactory and should be avoided if possible". (T5)
6. **Let place and partners pick the application.** Vision at JHU via Vidal; defense-funded stochastic constrained learning at Lehigh via ONR and Curtis. Exits come without announcement, when the partner or the grant goes. (T3, §4)
7. **Expect long incubations.** Trust funnel 2009 → 2017; shifted penalty-barrier 2015 → 2020. Single-author side projects are the ones that stall. (F1, F4)

---

## Contradictions (kept, not reconciled)

1. **Current rank.** Lehigh faculty page (fetched 2026-10-16): "Professor". The Jan 2026 news story calls him "also a professor at Lehigh ISE", possibly a generic usage. The Sep 2024 master's news calls him "Professor Daniel P. Robinson, our MS Program Director". Against these: his homepage ("Associate Professor"); the ICCOPT 2025 bio header ("Associate Professor"); the Sep 2024 ONR news ("Associate Professor Daniel P. Robinson"); the Feb 2022 news ("an associate professor"). No dated promotion announcement was found.
2. **Postdoc duration.** His bio: "He spent the next three years" after 2007, and "In 2011 he joined" JHU, which leaves a year unaccounted for. Lehigh adds "Visiting Professor at Northwestern". The 2008 Oxford report is from the "Computational Laboratory", while the bio says "Mathematical Institute".
3. **The 2011 corrigendum.** On his publications list it is "Nicholas I. M. Gould, Daniel P. Robinson, and Philippe L. Toint. Corrigendum … Technical Report, Rutherford Appleton Laboratory, Chilton, England, 2011". The published erratum (*Math. Prog.* 131, DOI 10.1007/s10107-011-0491-x) lists Gould & Toint as its only authors and cites the report as "Technical Report naXys-07-2011, Namur Centre for Complex Systems (naXys)". The two sources disagree on both the issuing institution and who authored the printed erratum.
4. **The IJCAI 2016 paper's title.** His own lists give "Incorporating user preferences in predictive models via structured regularizers" (publications and poster). DBLP gives "Trading-Off Cost of Deployment Versus Accuracy in Learning Predictive Models" (IJCAI 2016; arXiv 1604.05819). ORCID lists both, plus a third variant, "Incorporating end preferences in predictive models via structured regularizers". The proceedings title was not checked.
5. **Stated plan versus practice.** In 2019 he planned contributions "in computer vision, healthcare, and beyond". From 2020 the dominant Lehigh output is stochastic constrained optimization and, later, fairness. Computer-vision papers taper after 2021, and no healthcare paper appears at Lehigh. His 2026 profile still lists "Computer Vision Applications".
6. **Homepage versus grant record.** *Current Research* says subspace clustering "continues to be funded by the USA National Science Foundation under grant number NSF-1704458 since 2017". The NSF record gives an end date of 09/30/2023.
7. **Awards.** The Jan 2026 Lehigh news says "best paper awards" (plural). I could verify only one: the 2018 *Optimization Letters* Best Paper Award. Two searches found no other.
8. **Publication counts.** OpenAlex gives 134 works and h = 24, but its affiliation list includes "Statistics Finland [2019]" and "UC Berkeley [2020]", and 32 works in 2020, all signs of author-merging errors. DBLP gives 85 records. Neither count is complete or clean.

## Gaps

- **CV**: "A complete list of my service is contained in my curriculum vitae (available upon request)". I did not obtain it. Exact postdoc dates, JHU promotion history (whether he was promoted before leaving), the year he moved to full Professor, and the undergraduate degree year and major are all unverified.
- **Thesis text** (UCSD 2007): not read. Its acknowledgements and stated motivation are unknown.
- **Advisor roles of Lehigh students** (Dai, Qu, Guo, Khatti, Zebiane, Wu, Q. Wang): not verified. MGP lists only Mohy-ud-Din.
- **Why he moved from JHU to Lehigh**: no stated reason found. The Curtis partnership and the Fall 2017 visit are context only.
- **Why the Gould (2017), Gill (2020) and Vidal (2024) lines ended**: no statements found.
- **Talks after mid-2019**: the archived talks list stops in 2019. I found only the ICCOPT 2025 session (title not retrieved). The ISMP 2024 schedule page could not be resolved (DNS failure). I found no 2026 talks.
- **Book preface** (SIAM, 2025): blocked (HTTP 403). The authors' stated reasons for writing the book were not read.
- **JHU AMS news** on seed funding for healthcare cost optimization: blocked (Cloudflare 403); not read.
- **arXiv author listing**: the API was rate-limited, so I relied on DBLP and OpenAlex for completeness. Preprints that appear in neither may be missing.
- **Software**: the 2012 NSF abstract promised "freely available software". I did not search for repositories (agent 03's remit).
- **Rejections and referee exchanges**: none found. The venue changes (F7) are not explained.
- **Second best-paper award**: not found.

## Sources

1. Daniel P. Robinson, homepage "Who I am / What I do", Lehigh COR@L, fetched 2026-10-16, https://coral.ise.lehigh.edu/danielprobinson/ (primary)
2. Robinson, homepage "Current Research", undated (mentions funding to 2021+), https://coral.ise.lehigh.edu/danielprobinson/research/current-research/ (primary)
3. Robinson, homepage "Teaching", https://coral.ise.lehigh.edu/danielprobinson/teaching/ (primary)
4. Robinson, homepage "Service" and "Associate Editor", https://coral.ise.lehigh.edu/danielprobinson/service/ and /service/associate-editor/ (primary)
5. Robinson, homepage "Publications" (live page shows only a broken shortcode), https://coral.ise.lehigh.edu/danielprobinson/research/publications/ (primary)
6. Robinson, publications list, Wayback snapshot 2025-08-09, http://web.archive.org/web/20250809173145/https://coral.ise.lehigh.edu/danielprobinson/research/publications/ (primary)
7. Robinson, talks list, Wayback snapshot 2025-08-09, http://web.archive.org/web/20250809174202/https://coral.ise.lehigh.edu/danielprobinson/research/talks/ (primary)
8. Lehigh Rossin College, faculty profile "Daniel P. Robinson", fetched 2026-10-16, https://engineering.lehigh.edu/faculty/daniel-p-robinson (primary, institutional)
9. Lehigh news, "ISE Welcomes Daniel Robinson as Associate Professor", 2019, https://engineering.lehigh.edu/news/article/ise-welcomes-daniel-robinson-associate-professor (primary for the quote)
10. Lehigh news, "Introducing Lehigh's new MS in Data Science program", K. Kackenmeister, 2022-02-15, https://engineering.lehigh.edu/news/article/introducing-lehighs-new-ms-data-science-program (primary for quotes)
11. Lehigh news, "Office of Naval Research awards more than $1M to Lehigh ISE", 2024-09-12, https://engineering.lehigh.edu/news/article/office-naval-research-awards-more-1m-lehigh-ise (primary)
12. Lehigh news, "Lehigh ISE redesigns its master's programs, creating a novel program in optimization", 2024-09-25, https://engineering.lehigh.edu/news/article/lehigh-ise-redesigns-its-master-s-programs-creating-novel-program-optimization (primary)
13. Lehigh news, "Lehigh ISE faculty publish new book on practical optimization methods", 2026-01-22, https://engineering.lehigh.edu/news/article/lehigh-ise-faculty-publish-new-book-practical-optimization-methods (primary, institutional)
14. Lehigh ISE Newsletter 2019–2020 Mid-Year Update (OPTL Best Paper Award 2018), 2020, https://engineering.lehigh.edu/sites/engineering.lehigh.edu/files/_DEPARTMENTS/ise/newsletters/Lehigh-ISE-Newsletter-2019-2020-Mid-Year-Update.pdf (primary, observed)
15. Lehigh OptML group, home page news (2017–2024), https://optml.lehigh.edu/ (primary, observed)
16. Lehigh OptML group, people page, https://optml.lehigh.edu/people/ (primary)
17. ICCOPT 2022 website (co-chairs; dates), https://iccopt2022.lehigh.edu/ (primary)
18. ICCOPT 2025 sched, speaker page and bio of Daniel P. Robinson, 2025, https://iccopt2025usc.sched.com/speaker/daniel.p.robinson (primary, self-bio)
19. ORCID record 0000-0003-0251-4227 (employment; works to 2018), https://pub.orcid.org/v3.0/0000-0003-0251-4227/record (primary)
20. Mathematics Genealogy Project, Daniel P. Robinson, id 112624, https://www.mathgenealogy.org/id.php?id=112624 (secondary)
21. Mathematics Genealogy Project, Hassan Mohy-ud-Din, id 203711, https://www.mathgenealogy.org/id.php?id=203711 (secondary)
22. DBLP SPARQL query, author pid 20/8222 (85 records), https://sparql.dblp.org/sparql (secondary)
23. OpenAlex author A5082367556 and works since 2024-06, https://api.openalex.org/authors/orcid:0000-0003-0251-4227 (secondary)
24. NSF award 1217153, "New Active-Set Methods for Optimization and Complementarity Problems", PI Robinson, 2012–15, https://api.nsf.gov/services/v1/awards/1217153.json (primary)
25. NSF award 1447822, "BIGDATA: F: DKA: Learning a Union of Subspaces from Big and Corrupted Data", PI Vidal, co-PI Robinson, 2014–18, https://api.nsf.gov/services/v1/awards/1447822.json (primary)
26. NSF award 1704458, "III: Medium: Non-Convex Methods for Discovering High-Dimensional Structures in Big and Corrupted Data", PI Vidal, co-PI Robinson, 2017–23, https://api.nsf.gov/services/v1/awards/1704458.json (primary)
27. NSF award 1736448, "AMPS: Dynamics-Aware Algorithms for Real-Time Structured Fault Detection in Power Systems", PI Mallada, co-PIs Vidal and Robinson, 2017–21, https://api.nsf.gov/services/v1/awards/1736448.json (primary)
28. NSF award 2012243, "An Accelerated Decomposition Framework for Structured Sparse Optimization", PI Robinson, co-PI Curtis, 2020–24, https://api.nsf.gov/services/v1/awards/2012243.json (primary)
29. D. P. Robinson, "Comments on: Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it", TOP 23(1):43–47, 2015, DOI 10.1007/s11750-015-0371-2 (primary; full text read in Springer HTML)
30. F. E. Curtis (joint with D. P. Robinson), slides "How to Characterize the Worst-Case Performance of Algorithms for Nonconvex Optimization", U.S.–Mexico Workshop, 2018-01-08, http://coral.ise.lehigh.edu/frankecurtis/files/talks/us-mex_18.pdf (primary)
31. Corrigendum to Curtis, Robinson, Samadi (Math. Prog. 2017), Lemma 3.19, http://coral.ise.lehigh.edu/frankecurtis/files/errata/CurtRobiSama17_corrigendum.pdf (primary)
32. Corrigendum to Berahas, Curtis, Robinson, Zhou (SIOPT 2021), Corollary 3.14(a), http://coral.ise.lehigh.edu/frankecurtis/files/errata/BeraCurtRobiZhou21_corrigendum.pdf (primary)
33. N. I. M. Gould, Ph. L. Toint, "Erratum to: Nonlinear programming without a penalty function or a filter", Math. Prog. 131:403–404, 2011, DOI 10.1007/s10107-011-0491-x; Springer page with references (primary)
34. N. I. M. Gould, D. P. Robinson, "A Second Derivative SQP Method: Global Convergence", SIOPT 20(4):2023–2048, 2010, DOI 10.1137/080744542 (primary; abstract read)
35. N. I. M. Gould, D. P. Robinson, "A Second Derivative SQP Method: Local Convergence and Practical Issues", SIOPT 20(4):2049–2079, 2010, DOI 10.1137/080744554 (primary; metadata only)
36. N. I. M. Gould, D. P. Robinson, H. S. Thorne, "On solving trust-region and other regularised subproblems in optimization", MPC 2(1):21–57, 2010, DOI 10.1007/s12532-010-0011-7 (primary; metadata only)
37. P. E. Gill, D. P. Robinson, "A primal-dual augmented Lagrangian", COAP 51(1):1–25, 2012 (online 2010), DOI 10.1007/s10589-010-9339-1 (primary; metadata only)
38. N. I. M. Gould, D. P. Robinson, "A second-derivative SQP method with a 'trust-region-free' predictor step", IMA JNA 32(2):580–601, 2012, DOI 10.1093/imanum/drq043 (primary; metadata only)
39. D. P. Robinson, L. Feng, J. Nocedal, J.-S. Pang, "Subspace Accelerated Matrix Splitting Algorithms for Asymmetric and Symmetric Linear Complementarity Problems", SIOPT 23(3):1371–1397, 2013, DOI 10.1137/110845094 (primary; abstract read)
40. H. Mohy-ud-Din, D. P. Robinson, "A Solver for Nonconvex Bound-Constrained Quadratic Optimization", SIOPT 25(4):2385–2407, 2015, DOI 10.1137/15M1022100 (primary; abstract read)
41. T. Chen, F. E. Curtis, D. P. Robinson, "A Reduced-Space Algorithm for Minimizing ℓ1-Regularized Convex Functions", SIOPT 27(3):1583–1610, 2017, DOI 10.1137/16M1062259 (primary; abstract read)
42. F. E. Curtis, D. P. Robinson, "Regional complexity analysis of algorithms for nonconvex smooth optimization", Math. Prog. 187:579–615, 2021, DOI 10.1007/s10107-020-01492-3 (primary; metadata only)
43. A. S. Berahas, F. E. Curtis, D. P. Robinson, B. Zhou, "Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization", arXiv 2007.10525 (2020-07-20); SIOPT 31(2):1352–1379, 2021, DOI 10.1137/20M1354556 (primary; abstract read)
44. F. E. Curtis, Y. Dai, D. P. Robinson, "A Subspace Acceleration Method for Minimization Involving a Group Sparsity-Inducing Regularizer", SIOPT 32(2):545–572, 2022, DOI 10.1137/21M1411111 (primary; abstract read)
45. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A Shifted Primal-Dual Penalty-Barrier Method for Nonlinear Optimization", SIOPT 30(2):1067–1093, 2020, DOI 10.1137/19M1247425 (primary; metadata only)
46. Crossref metadata checks for the other DOIs cited above (IMA JNA 10.1093/imanum/drw004, 10.1093/imanum/dry022, 10.1093/imanum/drz008; PRE 10.1103/PhysRevE.103.053304; JSTAT 10.1088/1742-5468/abcaee; MOR 10.1287/moor.2021.0154; IJOO 10.1287/ijoo.2022.0008; MP 10.1007/s10107-023-01981-1; SIOPT 10.1137/23M1556149, 10.1137/23M1569460; OMS 10.1080/10556788.2024.2346643), https://api.crossref.org (secondary)
47. F. E. Curtis, D. P. Robinson, *Practical Nonconvex Nonsmooth Optimization*, SIAM, 2025-09-22, DOI 10.1137/1.9781611978599 (primary; metadata and news description only, not read)
48. Z. Khatti, D. P. Robinson, F. E. Curtis, "Fair Supervised Learning Through Constraints on Smooth Nonconvex Unfairness-Measure Surrogates", arXiv 2505.15788 (v1 2025-05-21, v3 2025-10-22) (primary; abstract read)
49. F. E. Curtis, D. P. Robinson, L. Zebiane, "Active-Set Identification in Noisy and Stochastic Optimization", arXiv 2509.00888 (2025-08-31) (primary; abstract read)
50. F. E. Curtis, L. Guo, D. P. Robinson, "Progressively Sampled Equality-Constrained Optimization", arXiv 2510.00417 (v1 2025-10-01, v2 2026-05-13) (primary; abstract read)
51. F. E. Curtis, X. Qu, D. P. Robinson, "A Proximal-Gradient Method for Solving Regularized Optimization Problems with General Constraints", arXiv 2512.23166 (v1 2025-12-29, v2 2026-01-15) (primary; abstract read)
52. Y. Dai, X. Qu, D. P. Robinson, "A Proximal-Gradient Method for Equality Constrained Optimization", SIOPT 35(4):2654–2683, 2025-12-05, DOI 10.1137/24M1653586 (primary; metadata only)
53. C.-Y. Wu, F. E. Curtis, D. P. Robinson, "Using Synthetic Data to Mitigate Unfairness and Preserve Privacy in Collaborative Machine Learning", arXiv 2409.09532 (2024-09-14) (primary; abstract read); IJOO version "A Bilevel Optimization Approach for Computing Synthetic Data to Mitigate Unfairness in Collaborative Machine Learning", IJOO 8(3):248–265, 2026, DOI 10.1287/ijoo.2025.0091 (primary; metadata only)
54. C.-Y. Wu, F. E. Curtis, D. P. Robinson, "Robust Server Defense Against Unreliable Clients in One-Shot Fair Collaborative Machine Learning", arXiv 2605.08616 (2026-05-09); FLICS 2026 pp. 239–247, DOI 10.1109/FLICS70075.2026.11621940 (primary; abstract read)
55. F. E. Curtis, L. Guo, D. P. Robinson, "A Local-Linearly Convergent Algorithm for Nonconvex Equality-Constrained Optimization", arXiv 2608.12665 (2026-08-12) (primary; abstract read)
56. S. Na, M. Anitescu, M. Kolar, "An Adaptive Stochastic Sequential Quadratic Programming with Differentiable Exact Augmented Lagrangians", arXiv 2102.05320 (v1 2021-02-10) (primary; used only for entry timing)
57. WebSearch result summaries (4 calls: awards; journal best-paper awards; dissertation advisees; 2026 talks), 2026-10-16 (secondary)
58. Wayback CDX listings for the homepage, publications page and talks page (snapshot dates 2019–2025), http://web.archive.org/cdx/search/cdx (secondary)
