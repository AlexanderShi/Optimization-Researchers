# Frank E. Curtis — publication list (Google Scholar primary)

Audited 2026-10-10: an independent year-sorted pass over the profile (96 rows; sortby=pubdate, pagesize=50, cstart=0 gave 50, cstart=50 gave 46, cstart=100 empty) matched every row to a works.json entry at normalised-title ratio >= 0.9, except four rows whose only difference is a stray Scholar author suffix (S014, S035, S051, S062; same works), so no rows were missing and nothing was added. Spot-checks: 20 DOIs (S001, S002, S005, S009, S011, S016, S026, S032, S039, S046, S058, S071, S072, S074, S078, S081, S088, S089, S094, H001) all resolve at doi.org (HTTP 302) with matching Crossref titles; 10 arXiv ids (S005, S026, S040, S046, S049, S065, S067, S087, S092, D003) all show the matching title; none nulled. Corrections: S002 year 2016 -> 2017 (DBLP + Crossref print); S039 year 2013 -> 2017 (DBLP + Crossref print); S026 venue 'Lehigh University ISE/COR@L' -> SIAM Journal on Optimization, year 2016 -> 2018 (DBLP + Crossref + homepage); S046 venue 'Technical Report 16T-010' -> IMA Journal of Numerical Analysis, year 2016 -> 2018 (homepage + Crossref print); S014 title: dropped stray Scholar suffix ': FE Curtis, DP Robinson' (year-sorted Scholar fetch + DBLP/Crossref show the plain title); S035 title: dropped stray Scholar suffix ': FE Curtis et al.' (year-sorted Scholar fetch + DBLP/Crossref show the plain title); D003 (arXiv 1402.1917) marked dup_of S050: arXiv abs page gives journal-ref SIOPT 25(1) 2015 and DOI 10.1137/130950239 = S050 DOI; arXiv id carried onto S050; S079 doi filled: 10.1007/978-1-4614-3924-0 (Crossref book record, editors Terlaky & Curtis, 2012; doi.org 302). Still open: S084 has no locatable identifier (see its note); the preprint/journal pairs S037/S045, S061/S060, D002/S063, D001/S031 and S069/S072 remain separate rows because the arXiv abs pages carry no journal-ref or DOI (checked again in this audit).

Harvested 2026-10-10 from the Google Scholar profile https://scholar.google.com/citations?user=Zfd6irsAAAAJ&hl=en (pagesize=50; cstart=0 gave 50 rows, cstart=50 gave 46, cstart=100 gave "There are no articles in this profile": 96 Scholar rows over 2 pages with rows, 3 pages fetched, no page needed the pagesize=20 refetch). Cross-checked against DBLP pid 61/7604 (76 records via the SPARQL endpoint: 57 Article, 17 Informal/CoRR, 2 Inproceedings), the homepage publication pages (https://coral.ise.lehigh.edu/frankecurtis/publications/ and .../publications-chronological/, 85 entries), Crossref (14 title queries, 14 DOIs accepted at title ratio >= 0.9 and year within 1) and the arXiv author listing (53 items). Counts: 96 Scholar rows; 2 DBLP-only items (D001–D002) plus 1 arXiv-listing-only item (D003); 1 homepage-only item (H001); 4 rows marked with dup_of (3 Scholar duplicates plus D003, linked to S050 by the audit); 96 distinct works listed below; 76 of them have a DOI and 53 an arXiv id. DBLP pid: 61/7604 (ORCID 0000-0001-7214-9187).

Profile identity (page 1): **Frank E. Curtis**, Professor, Lehigh University, verified email at lehigh.edu; interests as shown: Mathematical Optimization, Scientific Computing, Machine Learning. Matches the team.json hint (Lehigh ISE; SQP, inexact Newton-SQP, nonsmooth BFGS-SQP, stochastic SQP, TRACE; co-author of 'Optimization Methods for Large-Scale Machine Learning', SIAM Review 2018, which is the top row with 5921 citations). DBLP 61/7604 lists the same affiliation, ORCID, homepage and Scholar id.

Years are as Scholar shows them (Scholar sometimes takes the online-first year) except where two independent sources agree on a different year or venue (S002, S026, S039, S046, corrected by the audit); where DBLP, the homepage or Crossref give a different venue or year, the works.json row carries a `note`. Rows with dup_of (S080 -> S003, S085 -> S057, S095 -> S040, D003 -> S050) are omitted here.

| # | Year | Title | Venue | Cites | DOI | arXiv | Kind |
|---|------|-------|-------|-------|-----|-------|------|
| S001 | 2018 | Optimization methods for large-scale machine learning | SIAM Review | 5921 | 10.1137/16M1080173 | 1606.04838 | journal |
| S002 | 2017 | A trust region algorithm with a worst-case iteration complexity of for nonconvex optimization | Mathematical Programming | 240 | 10.1007/S10107-016-1026-2 |  | journal |
| S003 | 2012 | A sequential quadratic programming algorithm for nonconvex, nonsmooth constrained optimization | SIAM Journal on Optimization | 190 | 10.1137/090780201 |  | journal |
| S004 | 2017 | A BFGS-SQP Method for Nonsmooth, Nonconvex, Constrained Optimization and its Evaluation using Relative Minimization Profiles | Optimization Methods and Software | 173 | 10.1080/10556788.2016.1208749 |  | journal |
| S005 | 2020 | Gradient sampling methods for nonsmooth optimization | Numerical nonsmooth optimization: State of the art algorithms | 157 | 10.1007/978-3-030-34910-3_6 | 1804.11003 | chapter |
| S006 | 2008 | An inexact SQP method for equality constrained optimization | SIAM Journal on Optimization | 136 | 10.1137/060674004 |  | journal |
| S007 | 2021 | Sequential quadratic optimization for nonlinear equality constrained stochastic optimization | SIAM Journal on Optimization | 133 | 10.1137/20M1354556 | 2007.10525 | journal |
| S008 | 2015 | A quasi-Newton algorithm for nonconvex, nonsmooth optimization with global convergence guarantees | Mathematical Programming Computation | 130 | 10.1007/S12532-015-0086-2 |  | journal |
| S009 | 2010 | Infeasibility detection and SQP methods for nonlinear optimization | SIAM Journal on Optimization | 111 | 10.1137/080738222 |  | journal |
| S010 | 2010 | An interior-point algorithm for large-scale nonlinear optimization with inexact step computations | SIAM Journal on Scientific Computing | 101 | 10.1137/090747634 |  | journal |
| S011 | 2017 | Optimization methods for supervised machine learning: From linear models to deep learning | Leading developments from INFORMS communities | 99 | 10.1287/educ.2017.0168 | 1706.10207 | chapter |
| S012 | 2013 | An adaptive gradient sampling algorithm for nonsmooth optimization | Optimization Methods and Software | 91 | 10.1080/10556788.2012.714781 |  | journal |
| S013 | 2024 | Worst-case complexity of an SQP method for nonlinear equality constrained stochastic optimization | Mathematical Programming | 84 | 10.1007/S10107-023-01981-1 | 2112.14799 | journal |
| S014 | 2019 | Exploiting negative curvature in deterministic and stochastic optimization | Mathematical Programming | 81 | 10.1007/S10107-018-1335-8 | 1703.00412 | journal |
| S015 | 2019 | A stochastic trust region algorithm based on careful step normalization | Informs Journal on Optimization | 77 | 10.1287/IJOO.2018.0010 | 1712.10277 | journal |
| S016 | 2023 | An inexact column-and-constraint generation method to solve two-stage robust optimization problems | Operations Research Letters | 73 | 10.1016/J.ORL.2022.12.002 | 2207.03291 | journal |
| S017 | 2010 | An inexact Newton method for nonconvex equality constrained optimization | Mathematical Programming | 71 | 10.1007/S10107-008-0248-3 |  | journal |
| S018 | 2020 | ADMM for multiaffine constrained optimization | Optimization Methods and Software | 70 | 10.1080/10556788.2019.1683553 | 1802.09592 | journal |
| S019 | 2015 | An adaptive augmented Lagrangian method for large-scale constrained optimization | Mathematical Programming | 70 | 10.1007/S10107-014-0784-Y |  | journal |
| S020 | 2021 | Trust-region Newton-CG with strong second-order complexity guarantees for nonconvex optimization | SIAM Journal on Optimization | 68 | 10.1137/19M130563X | 1912.04365 | journal |
| S021 | 2024 | A stochastic sequential quadratic optimization algorithm for nonlinear-equality-constrained optimization with rank-deficient Jacobians | Mathematics of Operations Research | 63 | 10.1287/MOOR.2021.0154 | 2106.13015 | journal |
| S022 | 2014 | A sequential quadratic optimization algorithm with rapid infeasibility detection | SIAM Journal on Optimization | 63 | 10.1137/120880045 |  | journal |
| S023 | 2023 | Recent developments in security-constrained AC optimal power flow: Overview of challenge 1 in the ARPA-E grid optimization competition | Operations research | 62 | 10.1287/OPRE.2022.0315 | 2206.07843 | journal |
| S024 | 2015 | A globally convergent primal-dual active-set framework for large-scale convex quadratic optimization | Computational Optimization and Applications | 61 | 10.1007/S10589-014-9681-9 |  | journal |
| S025 | 2009 | A matrix-free algorithm for equality constrained optimization problems with rank-deficient Jacobians | SIAM Journal on Optimization | 61 | 10.1137/08072471X |  | journal |
| S026 | 2018 | Complexity analysis of a trust funnel algorithm for equality constrained optimization | SIAM Journal on Optimization | 57 | 10.1137/16M1108650 | 1707.00337 | journal |
| S027 | 2018 | A sequential algorithm for solving nonlinear optimization problems with chance constraints | SIAM Journal on Optimization | 54 | 10.1137/16M109003X |  | journal |
| S028 | 2016 | A self-correcting variable-metric algorithm for stochastic optimization | Proceedings of The 33rd International Conference on Machine Learning | 52 |  |  | conference |
| S029 | 2014 | An inexact sequential quadratic optimization algorithm for nonlinear optimization | SIAM Journal on Optimization | 52 | 10.1137/130918320 |  | journal |
| S030 | 2024 | Sequential quadratic optimization for stochastic optimization with deterministic nonlinear inequality and equality constraints | SIAM Journal on Optimization | 51 | 10.1137/23M1556149 | 2302.14790 | journal |
| S031 | 2020 | Adaptive stochastic optimization: a framework for analyzing stochastic optimization algorithms | IEEE Signal Processing Magazine | 50 | 10.1109/MSP.2020.3003539 |  | journal |
| S032 | 2008 | Flexible penalty functions for nonlinear constrained optimization | IMA Journal of Numerical Analysis | 49 | 10.1093/imanum/drn003 |  | journal |
| S033 | 2012 | A penalty-interior-point algorithm for nonlinear constrained optimization | Mathematical Programming Computation | 48 | 10.1007/S12532-012-0041-4 |  | journal |
| S034 | 2025 | Stochastic optimization approaches for an operating room and anesthesiologist scheduling problem | Operations research | 47 | 10.1287/OPRE.2022.0258 | 2204.11374 | journal |
| S035 | 2018 | Concise complexity analyses for trust region methods | Optimization Letters | 45 | 10.1007/S11590-018-1286-2 | 1802.07843 | journal |
| S036 | 2012 | A note on the implementation of an interior-point algorithm for nonlinear optimization with inexact step computations | Mathematical Programming, Series B | 43 | 10.1007/S10107-012-0557-4 |  | journal |
| S037 | 2021 | Inexact sequential quadratic optimization for minimizing a stochastic objective function subject to deterministic nonlinear equality constraints | arXiv preprint arXiv:2107.03512 | 40 |  | 2107.03512 | preprint |
| S038 | 2016 | A reduced-space algorithm for minimizing ℓ-regularized convex functions | SIAM Journal on Optimization | 35 | 10.1137/16M1062259 | 1602.07018 | journal |
| S039 | 2017 | An interior-point trust-funnel algorithm for nonlinear optimization | Mathematical Programming | 34 | 10.1007/S10107-016-1003-9 |  | journal |
| S040 | 2016 | Adaptive augmented Lagrangian methods: Algorithms and practical numerical experience | Optimization Methods and Software | 31 | 10.1080/10556788.2015.1071813 | 1408.4500 | journal |
| S041 | 2022 | A fully stochastic second-order trust region method | Optimization Methods and Software | 26 | 10.1080/10556788.2020.1852403 | 1911.06920 | journal |
| S042 | 2016 | Handling nonpositive curvature in a limited memory steepest descent method | IMA Journal of Numerical Analysis | 25 | 10.1093/imanum/drv034 |  | journal |
| S043 | 2023 | Worst-case complexity of trace with inexact subproblem solutions for nonconvex smooth optimization | SIAM Journal on Optimization | 24 | 10.1137/22M1492428 | 2204.11322 | journal |
| S044 | 2025 | A stochastic-gradient-based interior-point algorithm for solving smooth bound-constrained optimization problems | SIAM Journal on Optimization | 23 | 10.1137/23M1569460 | 2304.14907 | journal |
| S045 | 2024 | A stochastic inexact sequential quadratic optimization algorithm for nonlinear equality-constrained optimization | INFORMS Journal on Optimization | 23 | 10.1287/IJOO.2022.0008 |  | journal |
| S046 | 2018 | R-Linear Convergence of Limited Memory Steepest Descent | IMA Journal of Numerical Analysis | 20 | 10.1093/imanum/drx016 | 1610.03831 | journal |
| S047 | 2007 | Steplength selection in interior-point methods for quadratic programming | Applied Mathematics Letters | 20 | 10.1016/J.AML.2006.05.020 |  | journal |
| S048 | 2021 | Practical optimal control of a wave-energy converter in regular wave environments | Renewable Energy | 19 | 10.1016/j.renene.2021.02.134 | 2012.08049 | journal |
| S049 | 2020 | A self-correcting variable-metric algorithm framework for nonsmooth optimization | IMA Journal of Numerical Analysis | 19 | 10.1093/imanum/drz008 | 1708.02552 | journal |
| S050 | 2015 | Iterative reweighted linear least squares for exact penalty subproblems on product sets | SIAM Journal on Optimization | 19 | 10.1137/130950239 | 1402.1917 | journal |
| S051 | 2022 | Limited-memory BFGS with displacement aggregation | Mathematical Programming | 17 | 10.1007/S10107-021-01621-6 | 1903.03471 | journal |
| S052 | 2018 | FaRSA for ℓ1-regularized convex optimization: local convergence and numerical experience | Optimization Methods and Software | 17 | 10.1080/10556788.2017.1415336 |  | journal |
| S053 | 2022 | A subspace acceleration method for minimization involving a group sparsity-inducing regularizer | SIAM Journal on Optimization | 15 | 10.1137/21M1411111 | 2007.14951 | journal |
| S054 | 2025 | Almost-sure convergence of iterates and multipliers in stochastic sequential quadratic optimization | Journal of Optimization Theory and Applications | 14 | 10.1007/S10957-024-02568-2 | 2308.03687 | journal |
| S055 | 2024 | Fair machine learning through constrained stochastic optimization and an ε-constraint method | Optimization Letters | 12 | 10.1007/S11590-023-02024-6 |  | journal |
| S056 | 2021 | An accelerated communication-efficient primal-dual optimization framework for structured machine learning | Optimization Methods and Software | 12 | 10.1080/10556788.2019.1650361 | 1711.05305 | journal |
| S057 | 2020 | Inexact sequential quadratic optimization with penalty parameter updates within the QP solver | SIAM Journal on Optimization | 11 | 10.1137/18M1176488 | 1803.09224 | journal |
| S058 | 2004 | Central groupoids, central digraphs, and zero-one matrices A satisfying A^2 = J | Journal of Combinatorial Theory, Series A | 11 | 10.1016/J.JCTA.2003.10.001 |  | journal |
| S059 | 2025 | An interior-point algorithm for continuous nonlinearly constrained optimization with noisy function and derivative evaluations | arXiv preprint arXiv:2502.11302 | 10 |  | 2502.11302 | preprint |
| S060 | 2023 | A decomposition algorithm with fast identification of critical contingencies for large-scale security-constrained AC-OPF | Operations Research | 10 | 10.1287/OPRE.2023.2453 |  | journal |
| S061 | 2021 | A decomposition algorithm for large-scale security-constrained AC optimal power flow | arXiv preprint arXiv:2110.01737 | 10 |  | 2110.01737 | preprint |
| S062 | 2021 | Regional complexity analysis of algorithms for nonconvex smooth optimization | Mathematical Programming | 10 | 10.1007/S10107-020-01492-3 | 1802.01062 | journal |
| S063 | 2026 | A single-loop stochastic feasible interior-point algorithm for nonlinear inequality-constrained optimization | Mathematical Programming | 9 | 10.1007/S10107-025-02320-2 |  | journal |
| S064 | 2016 | Globally convergent primal-dual active-set methods with inexact subproblem solves | SIAM Journal on Optimization | 8 | 10.1137/140993314 |  | journal |
| S065 | 2022 | Gradient sampling methods with inexact subproblem solutions and gradient aggregation | INFORMS Journal on Optimization | 6 | 10.1287/IJOO.2022.0073 | 2005.07822 | journal |
| S066 | 2017 | Solving nearly-separable quadratic optimization problems as nonsmooth equations | Computational Optimization and Applications | 6 | 10.1007/S10589-017-9895-8 |  | journal |
| S067 | 2015 | Primal-dual active-set methods for isotonic regression and trend filtering | arXiv preprint arXiv:1508.02452 | 6 |  | 1508.02452 | preprint |
| S068 | 2026 | Projected stochastic momentum methods for nonlinear equality-constrained optimization for machine learning | arXiv preprint arXiv:2601.11795 | 4 |  | 2601.11795 | preprint |
| S069 | 2024 | Using synthetic data to mitigate unfairness and preserve privacy in collaborative machine learning | arXiv preprint arXiv:2409.09532 | 4 |  | 2409.09532 | preprint |
| S070 | 2023 | A variance-reduced and stabilized proximal stochastic gradient method with support identification guarantees for structured optimization | International Conference on Artificial Intelligence and Statistics | 4 |  | 2302.06790 | conference |
| S071 | 2018 | Fast market clearing algorithms | Energy Markets and Responsive Grids: Modeling, Control, and Optimization… | 4 | 10.1007/978-1-4939-7822-9_7 |  | chapter |
| S072 | 2026 | A Bilevel Optimization Approach for Computing Synthetic Data to Mitigate Unfairness in Collaborative Machine Learning | INFORMS Journal on Optimization | 3 | 10.1287/ijoo.2025.0091 |  | journal |
| S073 | 2025 | Equity-promoting integer programming approaches for medical resident rotation scheduling | Health Care Management Science | 3 | 10.1007/s10729-025-09736-4 |  | journal |
| S074 | 2025 | Practical Nonconvex Nonsmooth Optimization | Society for Industrial and Applied Mathematics | 3 | 10.1137/1.9781611978599 |  | book |
| S075 | 2024 | Derivative-free bound-constrained optimization for solving structured problems with surrogate models | Optimization Methods and Software | 3 | 10.1080/10556788.2024.2329588 | 2202.12961 | journal |
| S076 | 2024 | Incremental quasi-Newton algorithms for solving a nonconvex, nonsmooth, finite-sum optimization problem | Optimization Methods and Software | 3 | 10.1080/10556788.2023.2296432 | 2207.09788 | journal |
| S077 | 2016 | Accelerating convergence to competitive equilibrium in electricity markets | 2016 IEEE Power and Energy Society General Meeting (PESGM) | 3 | 10.1109/pesgm.2016.7741162 |  | conference |
| S078 | 2024 | Insights and innovations from the SSMCDAT 2023: bridging solid-state materials chemistry and data science | Chemistry of Materials | 2 | 10.1021/acs.chemmater.4c01318 |  | journal |
| S079 | 2012 | Modeling and Optimization: Theory and Applications; Selected Contributions from the MOPTA 2010 Conference | Springer | 2 | 10.1007/978-1-4614-3924-0 |  | book |
| S081 | 2006 | Determinant optimization on binary matrices | American Journal of Mathematical and Management Sciences | 2 | 10.1080/01966324.2006.10737660 |  | journal |
| S082 | 2025 | A Proximal-Gradient Method for Solving Regularized Optimization Problems with General Constraints | arXiv preprint arXiv:2512.23166 | 1 |  | 2512.23166 | preprint |
| S083 | 2025 | Fair supervised learning through constraints on smooth nonconvex unfairness-measure surrogates | arXiv preprint arXiv:2505.15788 | 1 |  | 2505.15788 | preprint |
| S084 | 2025 | Informed Machine Learning with a Stochastic-Gradient-based Algorithm for Training with Hard Constraints |  | 1 |  |  | other |
| S086 | 2003 | Special classes of zero-one matrices | College of William and Mary | 1 |  |  | thesis |
| S087 | 2026 | A Local-Linearly Convergent Algorithm for Nonconvex Equality-Constrained Optimization | arXiv preprint arXiv:2608.12665 |  |  | 2608.12665 | preprint |
| S088 | 2026 | NonOpt: Nonconvex, Nonsmooth Optimizer | Mathematical Programming Computation |  | 10.1007/s12532-026-00322-5 | 2503.22826 | journal |
| S089 | 2026 | Robust Server Defense Against Unreliable Clients in One-Shot Fair Collaborative Machine Learning | arXiv preprint arXiv:2605.08616 |  | 10.1109/flics70075.2026.11621940 | 2605.08616 | conference |
| S090 | 2026 | Low-Order Explicit Hessian Imitation Method for Large-Scale Supervised Machine Learning | arXiv preprint arXiv:2605.06945 |  |  | 2605.06945 | preprint |
| S091 | 2026 | A Gradient Sampling Algorithm for Noisy Nonsmooth Optimization | arXiv preprint arXiv:2604.00278 |  |  | 2604.00278 | preprint |
| S092 | 2025 | Progressively Sampled Equality-Constrained Optimization | arXiv preprint arXiv:2510.00417 |  |  | 2510.00417 | preprint |
| S093 | 2025 | Active-Set Identification in Noisy and Stochastic Optimization | arXiv preprint arXiv:2509.00888 |  |  | 2509.00888 | preprint |
| S094 | 2022 | Hybrid Interior-Point/Active-Set SCOPF Algorithms Exploiting Power System Characteristics | Lehigh University, Bethlehem, PA (United States) |  | 10.2172/2323339 |  | report |
| S096 | 2007 | Inexact sequential quadratic programming methods for large-scale nonlinear optimization | Northwestern University |  |  |  | thesis |
| D001 | 2020 | Adaptive Stochastic Optimization | CoRR |  |  | 2001.06699 | preprint |
| D002 | 2024 | Single-Loop Deterministic and Stochastic Interior-Point Algorithms for Nonlinearly Constrained Optimization | CoRR |  |  | 2408.16186 | preprint |
| H001 | 2019 | An Inexact Regularized Newton Framework with a Worst-Case Iteration Complexity of O(epsilon^-3/2) for Nonconvex Optimization | IMA Journal of Numerical Analysis, vol. 39, no. 3, pp. 1296–1327 |  | 10.1093/imanum/dry022 | 1708.00475 | journal |

Full records incl. duplicates: works.json
