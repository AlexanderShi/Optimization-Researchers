# Dimitris Bertsimas — publication list (Google Scholar primary)

Audited 2026-10-28: an independent year-sorted pass over the profile (932 rows; sortby=pubdate, 19 pages of 50 rows at cstart 0-900, plus pagesize=20 refetches at cstart 640, 660 and 680 and pagesize=10 refetches at cstart 660 and 670, because the cstart=650 page showed 49 rows for 50 slots) matched 931 profile rows one-to-one to the existing S rows (908 by normalised title at difflib ratio >= 0.9, 23 by hand where the harvest had replaced Scholar's title with the DBLP or Crossref title or WebFetch had cut it). Added: S932 'Leonid Kogan' (1997), a Scholar row whose title is the co-author's name; most WebFetch reads fold it into the row above, next to Scholar's error text, and it shows as its own row in one pagesize=10 read and in listings of the page's citation_for_view links (year-sorted position 667, citation-order position 803, i.e. the row the harvest could not recover in positions 801-810); its record page (1997/11, Leonid Kogan and D Bertsimas, PDF of the NBER paper 'Pricing and Hedging Derivative Securities in Incomplete Markets: An E-Aritrage Model') makes it the 1997 working paper, so it is dup_of S802. Corrected: S802 author line set to Scholar's 'L Kogan' and DOI 10.3386/w6250 added (Crossref NBER record, 1997-11, Bertsimas, Kogan, Lo); S341 DOI was stored URL-encoded ('%3c', '%3e') and is now the DOI name with '<' and '>'; S484 year null -> 2022 (Scholar's year); S625 truncated title restored from the year-sorted pass; S244 year 2014 -> 2015 (Crossref print year and the homepage list agree; Scholar showed the online-deposit year); S065 year 2013 -> 2012 and venue -> Mathematical Programming 134 (1), 23-70, and S120 year 2009 -> 2011 and venue -> Operations Research 59 (6), 1407-1419 (Crossref and the homepage list agree; Scholar shows a thesis or talk record merged with the article whose DOI the row carries); removed 10 dbertsim.mit.edu dropbox links that point to another paper's PDF (S098, S113, S155, S169, S170, S173, S300, S329, S802, S908; the homepage itself mislinks these entries). S006, S196 and S337 keep Scholar's year, which is the IEEE online year (Crossref print year one later, no second source agrees). Identifier checks: every DOI was compared with its registry record (387 Crossref DOIs fetched from api.crossref.org: titles match for all except S802, whose NBER DOI was accepted on the date and PDF evidence noted on the row; the Zenodo DOI of D013 matches its DataCite record); of a sample of 37 DOIs spread across the list, 36 resolved at doi.org with HTTP 302 and the URL-encoded S341 string gave 404 (the corrected DOI resolves), and the 35 per-DOI Crossref titles in the sample matched (D013 is registered with DataCite); all 126 arXiv ids (125 on listed works) agree with the arxiv.org author listing (124 papers) or, for the five papers retitled between versions, the duplicate row D014 (v1 title) and the robot-planning paper listed under 'D. Bertsimas', with their arxiv.org/abs pages (15 abs pages fetched, 0 mismatches). DBLP's SPARQL endpoint timed out during the audit, so DBLP was not re-queried.

Harvested 2026-10-28 from the Google Scholar profile https://scholar.google.com/citations?user=prKmkzMAAAAJ (read with WebFetch: 19 pages of 50 rows at cstart 0-900, plus 7 refetches with pagesize=20 and 3 with pagesize=10 for the two pages whose row counts did not add up), cross-checked against DBLP (pid 31/1258, 360 records via sparql.dblp.org), Crossref, the arxiv.org author listing (125 papers) and both homepage paper lists (www.mit.edu/~dbertsim/papers.html, 164 PDF links; dbertsim.mit.edu/published-papers, 395 entries). Counts: 932 Scholar rows (931 parsed by the harvest; the row it could not recover in positions 801-810 was added by the audit as S932), 21 DBLP-only items and 1 arXiv-only item (D ids), 11 homepage-only items (H ids), 186 rows marked as duplicates or junk (dup_of), 779 distinct works listed, 388 with a DOI and 125 with an arXiv id. Kinds of the listed works: journal 365, other 95, preprint 94, thesis 85, report 58, conference 49, book 9, chapter 7, talk 6, patent 4, review 4, errata 3. The list includes 85 theses (kind thesis; apart from his own 1988 thesis these are other authors' theses, mostly MIT, that Scholar attaches to the profile), MIT annual reports, NSF award abstracts and course pages (kind report/other), and 14 rows that are not works by Bertsimas (kind other, explained in the note field of works.json).

Profile identity: Dimitris Bertsimas — Boeing Professor of Operations Research, MIT; verified email at mit.edu; interests: Operations Research, Optimization, Stochastics, Analytics, Health Care (Scholar header on 2026-10-28: 80,782 citations, h-index 129).

Full records incl. duplicates: works.json

| # | Year | Title | Venue | Cites | DOI | arXiv | Kind |
|---|---|---|---|---|---|---|---|
| S001 | 2004 | The price of robustness | Operations research 52 (1), 35-53 | 7185 | 10.1287/opre.1030.0065 |  | journal |
| S002 | 1997 | Introduction to linear optimization | Athena scientific 6, 479-530 | 5688 |  |  | book |
| S003 | 2011 | Theory and applications of robust optimization | SIAM review 53 (3), 464-501 | 3831 | 10.1137/080734510 | 1010.5445 | journal |
| S004 | 2003 | Robust discrete optimization and network flows | Mathematical programming 98 (1), 49-71 | 2690 | 10.1007/s10107-003-0396-4 |  | journal |
| S005 | 1993 | Simulated annealing | Statistical science 8 (1), 10-15 | 2436 | 10.1214/ss/1177011077 |  | journal |
| S006 | 2012 | Adaptive robust optimization for the security constrained unit commitment problem | IEEE transactions on power systems 28 (1), 52-63 | 2153 | 10.1109/tpwrs.2012.2205021 |  | journal |
| S007 | 2000 | Moment problems and semidefinite optimization | Handbook of Semidefinite Programming: Theory, algorithms, and applications… | 1858 | 10.1007/978-1-4615-4381-7_16 |  | chapter |
| S008 | 2020 | From predictive to prescriptive analytics | Management Science 66 (3), 1025-1044 | 1626 | 10.1287/mnsc.2018.3253 | 1402.5481 | journal |
| S009 | 1998 | Optimal control of execution costs | Journal of financial markets 1 (1), 1-50 | 1606 | 10.1016/s1386-4181(97)00012-8 |  | journal |
| S010 | 2016 | Best subset selection via a modern optimization lens | The annals of statistics, 813-852 | 1284 | 10.1214/15-aos1388 | 1507.03133 | journal |
| S011 | 2017 | Optimal classification trees | Machine Learning 106 (7), 1039-1082 | 1223 | 10.1007/s10994-017-5633-9 |  | journal |
| S012 | 2011 | The price of fairness | Operations research 59 (1), 17-31 | 1063 | 10.1287/opre.1100.0865 |  | journal |
| S013 | 2018 | Data-driven robust optimization | Mathematical programming 167 (2), 235-292 | 1055 | 10.1007/s10107-017-1125-8 | 1401.0212 | journal |
| S014 | 2006 | A robust optimization approach to inventory theory | Operations research 54 (1), 150-168 | 992 | 10.1287/opre.1050.0238 |  | journal |
| S015 | 1998 | The air traffic flow management problem with enroute capacities | Operations research 46 (3), 406-422 | 883 | 10.1287/opre.46.3.406 |  | journal |
| S016 | 1991 | A stochastic and dynamic vehicle routing problem in the Euclidean plane | Operations Research 39 (4), 601-615 | 739 | 10.1287/opre.39.4.601 |  | journal |
| S017 | 1992 | A Vehicle Routing Problem with Stochastic Demand | Operations Research 40 (3), 574-585 | 733 | 10.1287/opre.40.3.574 |  | journal |
| S018 | 2005 | Optimal inequalities in probability theory: A convex optimization approach | SIAM Journal on Optimization 15 (3), 780-804 | 703 | 10.1137/s1052623401399903 |  | journal |
| S019 | 2004 | Robust linear optimization under general norms | Operations Research Letters 32 (6), 510-516 | 691 | 10.1016/j.orl.2003.12.007 |  | journal |
| S020 | 2005 | Optimization over integers | (No Title) | 649 |  |  | book |
| S021 | 2022 | Evaluation of individual and ensemble probabilistic forecasts of COVID-19 mortality in the United States | Proceedings of the National Academy of Sciences 119 (15), e2113561119 | 554 | 10.1073/pnas.2113561119 |  | conference |
| S022 | 2006 | Tractable approximations to robust conic optimization problems | Mathematical programming 107 (1), 5-36 | 552 | 10.1007/s10107-005-0677-1 |  | journal |
| S023 | 2022 | Integrated multimodal artificial intelligence framework for healthcare applications | NPJ digital medicine 5 (1), 149 | 540 | 10.1038/s41746-022-00689-4 | 2202.12998 | journal |
| S024 | 2009 | Constructing uncertainty sets for robust linear optimization | Operations research 57 (6), 1483-1495 | 536 | 10.1287/opre.1080.0646 |  | journal |
| S025 | 1996 | A new generation of vehicle routing research: robust algorithms, addressing uncertainty | Operations research 44 (2), 286-304 | 527 | 10.1287/opre.44.2.286 |  | journal |
| S026 | 2012 | On the efficiency-fairness trade-off | Management Science 58 (12), 2234-2250 | 492 | 10.1287/mnsc.1120.1549 |  | journal |
| S027 | 2006 | Robust and data-driven optimization: modern decision-making under uncertainty | INFORMS Tutorials in Operations Research: Models, Methods, and Applications… | 489 | 10.1287/educ.1063.0022 |  | chapter |
| S028 | 2019 | Adaptive distributionally robust optimization | Management Science 65 (2), 604-618 | 480 | 10.1287/mnsc.2017.2952 |  | journal |
| S029 | 2006 | Robust game theory | Mathematical programming 107 (1), 231-273 | 458 | 10.1007/s10107-005-0686-0 |  | journal |
| S030 | 2018 | From predictive methods to missing data imputation: an optimization approach | Journal of Machine Learning Research 18 (196), 1-39 | 449 |  |  | journal |
| S031 | 2004 | Shortfall as a risk measure: properties, optimization and applications | Journal of Economic Dynamics and control 28 (7), 1353-1381 | 446 | 10.1016/s0165-1889(03)00109-x |  | journal |
| S032 | 1993 | Stochastic and dynamic vehicle routing in the Euclidean plane with multiple capacitated vehicles | Operations Research 41 (1), 60-76 | 442 | 10.1287/opre.41.1.60 |  | journal |
| S033 | 1998 | Semidefinite relaxations, multivariate normal distributions, and order statistics | Handbook of Combinatorial Optimization: Volume1–3, 1473-1491 | 430 | 10.1007/978-1-4613-0303-9_24 |  | chapter |
| S034 | 2003 | Revenue management in a dynamic network environment | Transportation science 37 (3), 257-277 | 425 | 10.1287/trsc.37.3.257.16047 |  | journal |
| S035 | 2023 | Finding neurons in a haystack: Case studies with sparse probing | arXiv preprint arXiv:2305.01610 | 420 |  | 2305.01610 | journal |
| S036 | 1994 | The multi-airport ground-holding problem in air traffic control | Operations Research 42 (2), 249-261 | 415 | 10.1287/opre.42.2.249 |  | journal |
| S037 | 2011 | An integer optimization approach to large-scale air traffic flow management | Operations research 59 (1), 211-227 | 407 | 10.1287/opre.1100.0899 |  | journal |
| S038 | 1990 | A priori optimization | Operations Research 38 (6), 1019-1033 | 403 | 10.1287/opre.38.6.1019 |  | journal |
| S039 | 2018 | Robust sample average approximation | Mathematical Programming 171 (1), 217-282 | 397 | 10.1007/s10107-017-1174-z | 1408.4445 | journal |
| S040 | 2009 | Algorithm for cardinality-constrained quadratic optimization | Computational Optimization and Applications 43 (1), 1-22 | 388 | 10.1007/s10589-007-9126-9 |  | journal |
| S041 | 2018 | Surgical risk is not linear: derivation and validation of a novel, user-friendly, and machine-learning-based predictive optimal trees in emergency surgery risk (POTTER) calculator | Annals of surgery 268 (4), 574-583 | 382 | 10.1097/sla.0000000000002956 |  | journal |
| S042 | 2010 | Optimality of affine policies in multistage robust optimization | Mathematics of Operations Research 35 (2), 363-394 | 363 | 10.1287/moor.1100.0444 | 0904.3986 | journal |
| S043 | 2000 | The traffic flow management rerouting problem in air traffic control: A dynamic network flow approach | Transportation Science 34 (3), 239-255 | 360 | 10.1287/trsc.34.3.239.12300 |  | journal |
| S044 | 2013 | Fairness, efficiency, and flexibility in organ allocation for kidney transplantation | Operations research 61 (1), 73-87 | 354 | 10.1287/opre.1120.1138 |  | journal |
| S045 | 2004 | Solving convex programs by random walks | Journal of the ACM (JACM) 51 (4), 540-556 | 354 | 10.1145/1008731.1008733 |  | journal |
| S046 | 2019 | Online vehicle routing: The edge of optimization in large-scale applications | Operations Research 67 (1), 143-162 | 339 | 10.1287/opre.2018.1763 |  | journal |
| S047 | 2019 | Machine learning under a modern optimization lens | Dynamic Ideas LLC | 338 |  |  | book |
| S048 | 1988 | Probabilistic combinatorial optimization problems | Massachusetts Institute of Technology | 329 |  |  | thesis |
| S049 | 2010 | Finite adaptability in multistage linear optimization | IEEE Transactions on Automatic Control 55 (12), 2751-2766 | 326 | 10.1109/tac.2010.2049764 |  | journal |
| S050 | 2008 | Algorithmic prediction of health-care costs | Operations Research 56 (6), 1382-1392 | 324 | 10.1287/opre.1080.0619 |  | journal |
| S051 | 2000 | Restless bandits, linear programming relaxations, and a primal-dual index heuristic | Operations Research 48 (1), 80-90 | 321 | 10.1287/opre.48.1.80.12444 |  | journal |
| S052 | 1993 | Survivable networks, linear programming relaxations and the parsimonious property | Mathematical programming 60 (1), 145-166 | 315 | 10.1007/bf01580607 |  | journal |
| S053 | 2010 | Models for minimax stochastic linear optimization problems with risk aversion | Mathematics of Operations Research 35 (3), 580-602 | 309 | 10.1287/moor.1100.0445 |  | journal |
| S054 | 2020 | COVID-19 mortality risk assessment: An international multi-center study | PloS one 15 (12), e0243262 | 301 | 10.1371/journal.pone.0243262 |  | journal |
| S055 | 2004 | A robust optimization approach to supply chain management | International conference on integer programming and combinatorial… | 299 | 10.1007/978-3-540-25960-2_7 |  | conference |
| S056 | 2002 | On the relation between option and stock prices: a convex optimization approach | Operations Research 50 (2), 358-374 | 292 | 10.1287/opre.50.2.358.424 |  | journal |
| S057 | 1996 | Conservation laws, extended polymatroids and multiarmed bandit problems; a polyhedral approach to indexable systems | Mathematics of Operations Research 21 (2), 257-306 | 288 | 10.1287/moor.21.2.257 |  | journal |
| S058 | 2015 | Data-driven estimation in equilibrium using inverse optimization | Mathematical Programming 153 (2), 595-633 | 287 | 10.1007/s10107-014-0819-4 | 1308.3397 | journal |
| S059 | 2008 | Robust multiperiod portfolio management in the presence of transaction costs | Computers & Operations Research 35 (1), 3-17 | 286 | 10.1016/j.cor.2006.02.011 |  | journal |
| S060 | 2012 | On the power and limitations of affine policies in two-stage adaptive optimization | Mathematical programming 134 (2), 491-531 | 281 | 10.1007/s10107-011-0444-4 |  | journal |
| S061 | 2020 | Sparse high-dimensional regression: Exact scalable algorithms and phase transitions | The Annals of Statistics 48 (1), 300-323 | 280 | 10.1214/18-aos1804 | 1709.10029 | journal |
| S062 | 2019 | Health information management: implications of artificial intelligence on healthcare data and information management | Yearbook of medical informatics 28 (01), 056-064 | 274 |  |  | other |
| S063 | 2020 | Ensemble forecasts of coronavirus disease 2019 (COVID-19) in the US | MedRXiv, 2020.08. 19.20177493 | 266 |  |  | preprint |
| S064 | 2010 | A soft robust model for optimization under ambiguity | Operations research 58 (4-part-2), 1220-1234 | 251 | 10.1287/opre.1100.0821 |  | journal |
| S065 | 2012 | Tractable stochastic analysis in high dimensions via robust optimization | Mathematical Programming 134 (1), 23-70 | 249 | 10.1007/s10107-012-0567-2 |  | journal |
| S066 | 2005 | Simulation-based booking limits for airline revenue management | Operations Research 53 (1), 90-106 | 248 | 10.1287/opre.1040.0164 |  | journal |
| S067 | 2021 | Interpretable clustering: an optimization approach | Machine Learning 110 (1), 89-138 | 247 | 10.1007/s10994-020-05896-2 |  | journal |
| S068 | 1994 | Dynamic ground-holding policies for a network of airports | Transportation Science 28 (4), 275-291 | 241 | 10.1287/trsc.28.4.275 |  | journal |
| S069 | 2001 | Hedging derivative securities and incomplete markets: An ϵ-arbitrage approach | Operations research 49 (3), 372-397 | 240 | 10.1287/opre.49.3.372.11218 |  | journal |
| S070 | 2002 | An approximate dynamic programming approach to multidimensional knapsack problems | Management Science 48 (4), 550-565 | 239 | 10.1287/mnsc.48.4.550.208 |  | journal |
| S071 | 2006 | Dynamic pricing: A learning approach | Mathematical and computational models for congestion charging, 45-79 | 236 | 10.1007/0-387-29645-x_3 |  | chapter |
| S072 | 1994 | Optimization of multiclass queueing networks: Polyhedral and nonlinear characterizations of achievable performance | The Annals of Applied Probability 4 (1), 43-75 | 234 | 10.1214/aoap/1177005200 |  | journal |
| S073 | 2007 | Classification and regression via integer optimization | Operations research 55 (2), 252-271 | 211 | 10.1287/opre.1060.0360 |  | journal |
| S074 | 2003 | Restaurant Revenue Management | Operations Research 51 (3), 472-486 | 209 | 10.1287/opre.51.3.472.14956 |  | journal |
| S075 | 2011 | A hierarchy of near-optimal policies for multistage adaptive optimization | IEEE Transactions on Automatic Control 56 (12), 2809-2824 | 204 | 10.1109/tac.2011.2162878 |  | journal |
| S076 | 2016 | Fairness and collaboration in network air traffic flow management: An optimization approach | Transportation Science 50 (1), 57-76 | 202 | 10.1287/trsc.2014.0567 |  | journal |
| S077 | 2009 | Optimal bidding in online auctions | Journal of Revenue and Pricing Management 8 (1), 21-41 | 202 | 10.1057/rpm.2008.49 |  | journal |
| S078 | 2016 | An analytics approach to designing combination chemotherapy regimens for cancer | Management Science 62 (5), 1511-1531 | 201 | 10.1287/mnsc.2015.2363 |  | journal |
| S079 | 2017 | Personalized diabetes management using electronic medical records | Diabetes care 40 (2), 210-217 | 200 | 10.2337/dc16-0826 |  | journal |
| S080 | 2000 | When is time continuous? | Journal of Financial Economics 55 (2), 173-204 | 200 | 10.1016/s0304-405x(99)00049-5 |  | journal |
| S081 | 2016 | OR forum—an algorithmic approach to linear regression | Operations Research 64 (1), 2-16 | 198 | 10.1287/opre.2015.1436 |  | journal |
| S082 | 2015 | Design of near optimal decision rules in multistage adaptive mixed-integer optimization | Operations Research 63 (3), 610-627 | 198 | 10.1287/opre.2015.1365 |  | journal |
| S083 | 2022 | Where to locate COVID‐19 mass vaccination facilities? | Naval Research Logistics (NRL) 69 (2), 179-200 | 194 | 10.1002/nav.22007 | 2102.07309 | journal |
| S084 | 2022 | Robust and Adaptive Optimization | Dynamic Ideas | 192 |  |  | book |
| S085 | 2018 | Characterization of the equivalence of robustification and regularization in linear and matrix regression | European Journal of Operational Research 270 (3), 931-942 | 192 | 10.1016/j.ejor.2017.03.051 | 1411.6160 | journal |
| S086 | 2012 | Inverse optimization: A new perspective on the Black-Litterman model | Operations research 60 (6), 1389-1403 | 192 | 10.1287/opre.1120.1115 |  | journal |
| S087 | 2016 | Multistage robust mixed-integer optimization with adaptive partitions | Operations Research 64 (4), 980-998 | 189 | 10.1287/opre.2016.1515 |  | journal |
| S088 | 2016 | Reformulation versus cutting-planes for robust optimization: A computational study | Computational Management Science 13 (2), 195-217 | 185 | 10.1007/s10287-015-0236-z |  | journal |
| S089 | 1995 | Computational approaches to stochastic vehicle routing problems | Transportation science 29 (4), 342-352 | 183 | 10.1287/trsc.29.4.342 |  | journal |
| S090 | 2010 | Robust optimization for unconstrained simulation-based problems | Operations research 58 (1), 161-178 | 180 | 10.1287/opre.1090.0715 |  | journal |
| S091 | 1993 | Stochastic and dynamic vehicle routing with general demand and interarrival time distributions | Advances in Applied Probability 25 (4), 947-978 | 180 | 10.2307/1427801 |  | journal |
| S092 | 2022 | Online mixed-integer optimization in milliseconds | INFORMS Journal on Computing 34 (4), 2229-2248 | 179 | 10.1287/ijoc.2022.1181 | 1907.02206 | journal |
| S093 | 2019 | Exact first-choice product line optimization | Operations Research 67 (3), 651-670 | 176 | 10.1287/opre.2018.1825 |  | journal |
| S094 | 2019 | Development and validation of an optimized prediction of mortality for candidates awaiting liver transplantation | American Journal of Transplantation 19 (4), 1109-1118 | 174 | 10.1111/ajt.15172 |  | journal |
| S095 | 2020 | Sparse Regression: Scalable Algorithms and Empirical Performance | Statistical Science 35 (4), 555-578 | 173 | 10.1214/19-sts701 | 1902.06547 | journal |
| S096 | 2019 | Optimal prescriptive trees | INFORMS Journal on Optimization 1 (2), 164-183 | 173 | 10.1287/ijoo.2018.0005 |  | journal |
| S097 | 2025 | Mixed-integer optimization with constraint learning | Operations Research 73 (2), 1011-1028 | 172 | 10.1287/opre.2021.0707 | 2111.04469 | journal |
| S098 | 1995 | Fluid models of sequencing problems in open queueing networks; an optimal control approach | Institute for Mathematics and its Applications 71, 199 | 171 | 10.1007/978-1-4757-2418-9_11 |  | chapter |
| S099 | 2021 | From predictions to prescriptions: A data-driven response to COVID-19 | Health care management science 24 (2), 253-272 | 169 | 10.1007/s10729-020-09542-0 | 2006.16509 | journal |
| S100 | 2024 | Robust optimization | Intelligent Optimization: Principles, Algorithms and Applications, 239-251 | 168 |  |  | other |
| S101 | 1999 | Portfolio construction through mixed-integer programming at Grantham, Mayo, Van Otterloo and Company | Interfaces 29 (1), 49-66 | 168 | 10.1287/inte.29.1.49 |  | journal |
| S102 | 1993 | Further results on the probabilistic traveling salesman problem | European Journal of Operational Research 65 (1), 68-95 | 168 | 10.1016/0377-2217(93)90145-d |  | journal |
| S103 | 2023 | Forecasting COVID-19 and analyzing the effect of government interventions | Operations Research 71 (1), 184-201 | 165 | 10.1287/opre.2022.2306 |  | journal |
| S104 | 2019 | Robust classification | INFORMS Journal on Optimization 1 (1), 2-34 | 165 | 10.1287/ijoo.2018.0001 |  | journal |
| S105 | 2017 | Logistic regression: From art to science | Statistical Science, 367-384 | 161 | 10.1214/16-sts602 |  | journal |
| S106 | 2007 | A learning approach for interactive marketing to a customer segment | Operations Research 55 (6), 1120-1135 | 161 | 10.1287/opre.1070.0427 |  | journal |
| S108 | 1995 | Locating discretionary service facilities, II: maximizing market size, minimizing inconvenience | Operations Research 43 (4), 623-632 | 159 | 10.1287/opre.43.4.623 |  | journal |
| S109 | 2008 | The air traffic flow management problem: An integer optimization approach | International Conference on Integer Programming and Combinatorial… | 158 | 10.1007/978-3-540-68891-4_3 |  | conference |
| S110 | 2023 | Predictive performance of multi-model ensemble forecasts of COVID-19 across European nations | Elife 12, e81916 | 156 | 10.7554/elife.81916 |  | journal |
| S111 | 2020 | Machine learning in oncology: methods, applications, and challenges | JCO clinical cancer informatics 4, CCI. 20.00072 | 156 | 10.1200/cci.20.00072 |  | journal |
| S112 | 2021 | The voice of optimization | Machine Learning 110 (2), 249-277 | 154 | 10.1007/s10994-020-05893-5 | 1812.09991 | journal |
| S113 | 2023 | A data-driven approach to multistage stochastic linear optimization | Management Science 69 (1), 51-74 | 153 | 10.1287/mnsc.2022.4352 |  | journal |
| S114 | 2012 | Equitable and efficient coordination in traffic flow management | Transportation science 46 (2), 262-280 | 152 | 10.1287/trsc.1110.0393 |  | journal |
| S115 | 2022 | Predicting inpatient flow at a major hospital using interpretable analytics | Manufacturing & Service Operations Management 24 (6), 2809-2824 | 151 | 10.1287/msom.2021.0971 |  | journal |
| S116 | 2010 | Nonconvex robust optimization for problems with constraints | INFORMS journal on computing 22 (1), 44-58 | 151 | 10.1287/ijoc.1090.0319 |  | journal |
| S117 | 2018 | Binary decision rules for multistage adaptive mixed-integer optimization | Mathematical Programming 167 (2), 395-433 | 147 | 10.1007/s10107-017-1135-6 |  | journal |
| S118 | 2007 | Constrained stochastic LQC: a tractable approach | IEEE Transactions on automatic control 52 (10), 1826-1841 | 145 | 10.1109/tac.2007.906182 |  | journal |
| S119 | 2015 | Robust queueing theory | Operations Research 63 (3), 676-700 | 143 | 10.1287/opre.2015.1367 |  | journal |
| S120 | 2011 | Optimal Selection of Airport Runway Configurations | Operations Research 59 (6), 1407-1419 | 142 | 10.1287/opre.1110.0956 |  | journal |
| S121 | 1999 | On dependent randomized rounding algorithms | Operations Research Letters 24 (3), 105-114 | 142 | 10.1016/s0167-6377(99)00010-3 |  | journal |
| S122 | 2005 | A data-driven approach to newsvendor problems | Working Papere, Massachusetts Institute of Technology 51, 79 | 141 |  |  | report |
| S123 | 2001 | Performance of multiclass Markovian queueing networks via piecewise linear Lyapunov functions | Annals of Applied Probability, 1384-1428 | 141 | 10.1214/aoap/1015345407 |  | journal |
| S124 | 2015 | The power of optimization over randomization in designing experiments involving small samples | Operations Research 63 (4), 868-876 | 139 | 10.1287/opre.2015.1361 |  | journal |
| S125 | 2009 | Depression and costs of health care | Psychosomatics 50 (4), 392-401 | 132 | 10.1176/appi.psy.50.4.392 |  | journal |
| S126 | 1993 | On central limit theorems in geometrical probability | The Annals of Applied Probability 3 (4), 1033-1046 | 132 | 10.1214/aoap/1177005271 |  | journal |
| S127 | 2021 | Machine learning for real-time heart disease prediction | IEEE Journal of Biomedical and Health Informatics 25 (9), 3627-3637 | 131 | 10.1109/jbhi.2021.3066347 |  | journal |
| S128 | 2000 | Data, models, and decisions: The fundamentals of management science | (No Title) | 130 |  |  | book |
| S129 | 1995 | The distributional Little's law and its applications | Operations Research 43 (2), 298-310 | 130 | 10.1287/opre.43.2.298 |  | journal |
| S130 | 1999 | Asymptotically optimal algorithms for job shop scheduling and packet routing | Journal of Algorithms 33 (2), 296-318 | 128 | 10.1006/jagm.1999.1047 |  | journal |
| S131 | 2023 | Optimization-based scenario reduction for data-driven two-stage stochastic optimization | Operations Research 71 (4), 1343-1361 | 126 | 10.1287/opre.2022.2265 |  | journal |
| S132 | 2024 | Universal neurons in gpt2 language models | arXiv preprint arXiv:2401.12181 | 125 |  | 2401.12181 | journal |
| S133 | 2022 | Data-driven optimization: A reproducing kernel hilbert space approach | Operations Research 70 (1), 454-471 | 124 | 10.1287/opre.2020.2069 |  | journal |
| S134 | 2010 | On the power of robust solutions in two-stage stochastic and adaptive optimization problems | Mathematics of Operations Research 35 (2), 284-305 | 124 | 10.1287/moor.1090.0440 |  | journal |
| S135 | 1995 | Models and algorithms for transient queueing congestion at airports | Management Science 41 (8), 1279-1295 | 122 | 10.1287/mnsc.41.8.1279 |  | journal |
| S136 | 2022 | A scalable algorithm for sparse portfolio selection | INFORMS Journal on Computing 34 (3), 1489-1511 | 121 | 10.1287/ijoc.2021.1127 | 1811.00138 | journal |
| S137 | 2019 | Optimizing schools' start time and bus routes | Proceedings of the National Academy of Sciences 116 (13), 5943-5948 | 121 | 10.1073/pnas.1811462116 |  | journal |
| S138 | 2016 | Duality in two-stage adaptive linear optimization: Faster computation and stronger bounds | INFORMS Journal on Computing 28 (3), 500-511 | 121 | 10.1287/ijoc.2016.0689 |  | journal |
| S139 | 2022 | Bootstrap robust prescriptive analytics | Mathematical Programming 195 (1), 39-78 | 120 | 10.1007/s10107-021-01679-2 | 1711.09974 | journal |
| S140 | 1998 | Asymptotic buffer overflow probabilities in multiclass multiplexers: An optimal control approach | IEEE Transactions on Automatic Control 43 (3), 315-335 | 120 | 10.1109/9.661587 |  | journal |
| S141 | 2010 | Robust optimization with simulated annealing | Journal of Global Optimization 48 (2), 323-334 | 119 | 10.1007/s10898-009-9496-x |  | journal |
| S142 | 2005 | Special Issue Papers: Dynamic pricing and inventory control for multiple products | Journal of Revenue and Pricing Management 3 (4), 303-319 | 118 | 10.1057/palgrave.rpm.5170117 |  | journal |
| S143 | 2016 | Inventory management in the era of big data | Production and Operations Management 25 (12), 2006-2009 | 116 | 10.1111/poms.2_12637 |  | journal |
| S144 | 2020 | Machine learning and natural language processing methods to identify ischemic stroke, acuity and location from radiology reports | PloS one 15 (6), e0234908 | 114 | 10.1371/journal.pone.0234908 |  | journal |
| S145 | 1999 | Optimal control of execution costs for portfolios | Computing in Science & Engineering 1 (6), 40-53 | 113 | 10.1109/5992.805135 |  | journal |
| S146 | 2022 | Hurricane forecasting: A novel multimodal machine learning framework | Weather and forecasting 37 (6), 817-831 | 109 | 10.1175/waf-d-21-0091.1 | 2011.06125 | journal |
| S147 | 2001 | Probabilistic service level guarantees in make-to-stock manufacturing systems | Operations Research 49 (1), 119-133 | 109 | 10.1287/opre.49.1.119.11183 |  | journal |
| S148 | 1990 | The probabilistic minimum spanning tree problem | Networks 20 (3), 245-275 | 107 | 10.1002/net.3230200302 |  | journal |
| S149 | 2023 | Learning Sparse Nonlinear Dynamics via Mixed-Integer Optimization | Nonlinear Dynamics 111 (7), 6585-6604 | 105 | 10.1007/s11071-022-08178-9 | 2206.00176 | journal |
| S150 | 2023 | Dynamic optimization with side information | European Journal of Operational Research 304 (2), 634-651 | 101 | 10.1016/j.ejor.2022.03.030 | 1907.07307 | journal |
| S151 | 2019 | Travel time estimation in the age of big data | Operations Research 67 (2), 498-515 | 101 | 10.1287/opre.2018.1784 |  | journal |
| S152 | 2019 | Prescriptive analytics for human resource planning in the professional services industry | European Journal of Operational Research 272 (2), 636-641 | 101 | 10.1016/j.ejor.2018.06.035 |  | journal |
| S153 | 2013 | Robust and adaptive network flows | Operations Research 61 (5), 1218-1242 | 100 | 10.1287/opre.2013.1200 |  | journal |
| S154 | 2006 | Tight bounds on expected order statistics | Probability in the Engineering and Informational Sciences 20 (4), 667-686 | 100 | 10.1017/s0269964806060414 |  | journal |
| S155 | 2006 | Solving asymmetric variational inequalities via convex optimization | Operations Research Letters 34 (5), 481-490 | 100 | 10.1016/j.orl.2005.09.006 |  | journal |
| S156 | 1998 | A new algorithm for state-constrained separated continuous linear programs | SIAM Journal on control and optimization 37 (1), 177-210 | 100 | 10.1137/s0363012995292664 |  | journal |
| S157 | 2021 | A pre-registered short-term forecasting study of COVID-19 in Germany and Poland during the second wave | Nature communications 12 (1), 5173 | 99 | 10.1038/s41467-021-25207-0 |  | journal |
| S158 | 1992 | The minimum spanning tree constant in geometrical probability and under the independent model: a unified approach | The Annals of Applied Probability, 113-130 | 99 | 10.1214/aoap/1177005773 |  | journal |
| S159 | 2013 | A hybrid approach to beam angle optimization in intensity-modulated radiation therapy | Computers & Operations Research 40 (9), 2187-2197 | 97 | 10.1016/j.cor.2012.06.009 |  | journal |
| S160 | 2006 | Persistence in discrete optimization under data uncertainty | Mathematical programming 108 (2), 251-274 | 94 | 10.1007/s10107-006-0710-z |  | journal |
| S161 | 1989 | Worst-case examples for the spacefilling curve heuristic for the Euclidean traveling salesman problem | Oper. Res. Lett 8, 241-244 | 94 | 10.1016/0167-6377(89)90047-3 |  | journal |
| S162 | 2022 | Optimal survival trees | Machine learning 111 (8), 2951-3023 | 93 | 10.1007/s10994-021-06117-0 | 2012.04284 | journal |
| S163 | 2022 | Two-stage sample robust optimization | Operations Research 70 (1), 624-640 | 93 | 10.1287/opre.2020.2096 | 1907.07142 | journal |
| S164 | 2017 | Robust product line design | Operations Research 65 (1), 19-37 | 93 | 10.1287/opre.2016.1546 |  | journal |
| S165 | 2011 | A geometric characterization of the power of finite adaptability in multistage stochastic and adaptive optimization | Mathematics of Operations Research 36 (1), 24-54 | 93 | 10.1287/moor.1110.0482 |  | journal |
| S166 | 1998 | Rounding algorithms for covering problems | Mathematical Programming 80 (1), 63-89 | 93 | 10.1007/bf01582131 |  | journal |
| S167 | 2004 | Robust discrete optimization under ellipsoidal uncertainty sets | Manuscript, MIT 9, 1-23 | 92 |  |  | preprint |
| S168 | 1990 | An analytic approach to a general class of G/G/s queueing systems | Operations Research 38 (1), 139-155 | 92 | 10.1287/opre.38.1.139 |  | journal |
| S169 | 2004 | Probabilistic Combinatorial Optimization: Moments, Semidefinite Programming, and Asymptotic Bounds | SIAM J. Optim 15, 185–209 | 92 | 10.1137/s1052623403430610 |  | journal |
| S170 | 2021 | Sparse classification: a scalable discrete optimization perspective | Machine Learning 110 (11), 3177-3209 | 91 | 10.1007/s10994-021-06085-5 | 1710.01352 | journal |
| S171 | 2014 | Robust option pricing | European Journal of Operational Research 239 (3), 842-853 | 91 | 10.1016/j.ejor.2014.06.002 |  | journal |
| S172 | 2014 | Optimal design for multi-item auctions: A robust optimization approach | Mathematics of Operations Research 39 (4), 1012-1038 | 91 | 10.1287/moor.2014.0645 |  | journal |
| S173 | 1997 | Transient laws of non-stationary queueing systems and their applications | Queueing systems 25 (1), 115-155 | 90 | 10.1023/a:1019100301115 |  | journal |
| S174 | 2020 | Personalized treatment for coronary artery disease patients: a machine learning approach | Health care management science 23 (4), 482-506 | 89 | 10.1007/s10729-020-09522-4 | 1910.08483 | journal |
| S175 | 2021 | A unified approach to mixed-integer optimization problems with logical constraints | SIAM Journal on Optimization 31 (3), 2340-2367 | 88 | 10.1137/20m1346778 |  | journal |
| S176 | 2015 | A tight characterization of the performance of static solutions in two-stage adjustable robust linear optimization | Mathematical Programming 150 (2), 281-319 | 88 | 10.1007/s10107-014-0768-y |  | journal |
| S177 | 1998 | On the large deviations behavior of acyclic networks of queues | The Annals of Applied Probability 8 (4), 1027-1069 | 88 | 10.1214/aoap/1028903373 |  | journal |
| S178 | 2014 | Least quantile regression via modern optimization | The Annals of Statistics | 87 | 10.1214/14-aos1223 | 1310.8625 | journal |
| S179 | 2021 | Validation of the Artificial Intelligence-Based Predictive Optimal Trees in Emergency Surgery Risk (POTTER) Calculator in Emergency General Surgery and Emergency Laparotomy Patients | Journal of the American College of Surgeons 232 (6), 912-919. e1 | 86 | 10.1016/j.jamcollsurg.2021.02.009 |  | journal |
| S180 | 2020 | Joint frequency-setting and pricing optimization on multimodal transit networks at scale | Transportation Science 54 (3), 839-853 | 86 | 10.1287/trsc.2019.0959 |  | journal |
| S181 | 1996 | Stability conditions for multiclass fluid queueing networks | IEEE Transactions on Automatic Control 41 (11), 1618-1631 | 86 | 10.1109/9.543999 |  | journal |
| S182 | 2017 | Certifiably optimal low rank factor analysis | Journal of Machine Learning Research 18 (29), 1-53 | 85 |  | 1604.06837 | journal |
| S183 | 2022 | Solving large-scale sparse PCA to certifiable (near) optimality | Journal of Machine Learning Research 23 (13), 1-35 | 82 |  | 2005.05195 | journal |
| S184 | 2019 | Certifiably optimal sparse principal component analysis | Mathematical Programming Computation 11 (3), 381-420 | 82 | 10.1007/s12532-018-0153-6 |  | journal |
| S185 | 1995 | The achievable region method in the optimal control of queueing systems; formulations, bounds and policies | Queueing systems 21 (3), 337-389 | 79 | 10.1007/bf01149167 |  | journal |
| S186 | 1989 | Traveling salesman facility location problems | Transportation science 23 (3), 184-191 | 78 | 10.1287/trsc.23.3.184 |  | journal |
| S187 | 1999 | Large deviations analysis of the generalized processor sharing policy | Queueing Systems 32 (4), 319-349 | 77 | 10.1023/a:1019151423773 |  | journal |
| S188 | 2021 | Trauma outcome predictor: an artificial intelligence interactive smartphone tool to predict outcomes in trauma patients | Journal of Trauma and Acute Care Surgery 91 (1), 93-99 | 76 | 10.1097/ta.0000000000003158 |  | journal |
| S189 | 2020 | Machine learning provides evidence that stroke risk is not linear: The non-linear Framingham stroke risk score | PloS one 15 (5), e0232414 | 75 | 10.1371/journal.pone.0232414 |  | journal |
| S190 | 2018 | Applied informatics decision support tool for mortality predictions in patients with cancer | JCO clinical cancer informatics 2, 1-11 | 74 | 10.1200/cci.18.00003 |  | journal |
| S191 | 2016 | On the power of randomization in network interdiction | Operations Research Letters 44 (1), 114-120 | 74 | 10.1016/j.orl.2015.11.005 | 1312.3478 | journal |
| S192 | 2015 | On the performance of affine policies for two-stage adaptive optimization: a geometric perspective | Mathematical Programming 153 (2), 577-594 | 74 | 10.1007/s10107-014-0818-5 |  | journal |
| S193 | 2019 | From predictions to prescriptions in multistage optimization problems | arXiv preprint arXiv:1904.11637 | 73 |  | 1904.11637 | preprint |
| S194 | 2013 | Revealing rival marginal offer prices via inverse optimization | IEEE Transactions on Power Systems 28 (3), 3056-3064 | 73 | 10.1109/tpwrs.2012.2234144 |  | journal |
| S195 | 1990 | An asymptotic determination of the minimum spanning tree and minimum matching constants in geometrical probability | Operations Research Letters 9 (4), 223-231 | 73 | 10.1016/0167-6377(90)90066-e |  | journal |
| S196 | 2021 | Computation of convex hull prices in electricity markets with non-convexities using dantzig-wolfe decomposition | IEEE Transactions on Power Systems 37 (4), 2578-2589 | 70 | 10.1109/tpwrs.2021.3122000 | 2012.13331 | journal |
| S197 | 2017 | A comparison of Monte Carlo tree search and rolling horizon optimization for large-scale dynamic resource allocation problems | European Journal of Operational Research 263 (2), 664-678 | 70 | 10.1016/j.ejor.2017.05.032 |  | journal |
| S198 | 2021 | A simple and fast spectroscopy-based technique for Covid-19 diagnosis | Scientific reports 11 (1), 16740 | 68 | 10.1038/s41598-021-95568-5 |  | journal |
| S199 | 2019 | The price of interpretability | arXiv preprint arXiv:1907.03419 | 68 |  | 1907.03419 | preprint |
| S200 | 2017 | Data-driven learning in dynamic pricing using adaptive optimization | Optimization Online 20 | 66 |  |  | preprint |
| S201 | 2016 | Unified optimization of traffic flows through airports | Transportation Science 50 (1), 77-93 | 66 | 10.1287/trsc.2015.0590 |  | journal |
| S202 | 2013 | Optimal routes for electric vehicles facing uncertainty, congestion, and energy constraints | Massachusetts Institute of Technology | 66 |  |  | thesis |
| S203 | 1992 | Deducing queueing from transactional data: the queue inference engine, revisited | Operations Research 40 (3-supplement-2), S217-S228 | 66 | 10.1287/opre.40.3.s217 |  | journal |
| S204 | 2020 | Learning mixed-integer convex optimization strategies for robot planning and control | 2020 59th IEEE Conference on Decision and Control (CDC), 1698-1705 | 65 | 10.1109/cdc42340.2020.9304043 | 2004.03736 | conference |
| S205 | 2002 | From fluid relaxations to practical algorithms for job shop scheduling: the makespan objective | Mathematical Programming 92 (1), 61-102 | 65 | 10.1007/s101070100272 |  | journal |
| S206 | 2015 | Or forum—tenure analytics: Models for predicting research impact | Operations Research 63 (6), 1246-1261 | 64 | 10.1287/opre.2015.1447 |  | journal |
| S207 | 2003 | From fluid relaxations to practical algorithms for high-multiplicity job-shop scheduling: The holding cost objective | Operations Research 51 (5), 798-813 | 64 | 10.1287/opre.51.5.798.16748 |  | journal |
| S208 | 2021 | Data-driven transit network design at scale | Operations Research 69 (4), 1118-1133 | 63 | 10.1287/opre.2020.2057 |  | journal |
| S209 | 2016 | The analytics edge | Dynamic Ideas LLC | 63 |  |  | book |
| S210 | 2014 | Dynamic resource allocation: A flexible and tractable modeling framework | European Journal of Operational Research 236 (1), 14-26 | 63 | 10.1016/j.ejor.2013.10.063 |  | journal |
| S211 | 2013 | Learning preferences under noise and loss aversion: An optimization approach | Operations Research 61 (5), 1190-1199 | 63 | 10.1287/opre.2013.1209 |  | journal |
| S212 | 1999 | Optimization of Multiclass Queueing Networks with Changeover Times Via the Achievable Region Approach: Part I, the Single-Station Case | Math. Oper. Res 24, 306-330 | 63 | 10.1287/moor.24.2.306 |  | journal |
| S213 | 2000 | A new algebraic geometry algorithm for integer programming | Management Science 46 (7), 999-1008 | 62 | 10.1287/mnsc.46.7.999.12033 |  | journal |
| S214 | 1998 | From valid inequalities to heuristics: A unified view of primal-dual approximation algorithms in covering problems | Operations Research 46 (4), 503-514 | 62 | 10.1287/opre.46.4.503 |  | journal |
| S215 | 2021 | Probabilistic guarantees in robust optimization | SIAM Journal on Optimization 31 (4), 2893-2920 | 61 | 10.1137/21m1390967 |  | journal |
| S216 | 2016 | Decomposable Markov decision processes: A fluid optimization approach | Operations Research 64 (6), 1537-1555 | 60 | 10.1287/opre.2016.1531 |  | journal |
| S217 | 2013 | On the approximability of adjustable robust convex optimization under uncertainty | Mathematical Methods of Operations Research 77 (3), 323-343 | 60 | 10.1007/s00186-012-0405-6 |  | journal |
| S218 | 2023 | Sparse plus low rank matrix decomposition: A discrete optimization approach | Journal of Machine Learning Research 24 (267), 1-51 | 58 |  | 2109.12701 | journal |
| S219 | 2021 | Adverse outcomes prediction for congenital heart surgery: a machine learning approach | World Journal for Pediatric and Congenital Heart Surgery 12 (4), 453-460 | 58 | 10.1177/21501351211007106 |  | journal |
| S220 | 1992 | Transient and busy period analysis of the_GI/G_/1 queue: The method of stages | Queueing Systems 10 (3), 153-184 | 58 | 10.1007/bf01159205 |  | journal |
| S221 | 2007 | Adaptability via sampling | 2007 46th IEEE Conference on Decision and Control, 4717-4722 | 57 | 10.1109/cdc.2007.4434596 |  | conference |
| S222 | 2019 | Robust maximum likelihood estimation | INFORMS Journal on Computing 31 (3), 445-458 | 56 | 10.1287/ijoc.2018.0834 |  | journal |
| S223 | 2023 | The power and limits of predictive approaches to observational data-driven optimization: The case of pricing | INFORMS Journal on Optimization 5 (1), 110-129 | 55 | 10.1287/ijoo.2022.0077 | 1605.02347 | journal |
| S224 | 2019 | Robust and stochastic formulations for ambulance deployment and dispatch | European Journal of Operational Research 279 (2), 557-571 | 54 | 10.1016/j.ejor.2019.05.011 |  | journal |
| S225 | 2017 | The trimmed lasso: Sparsity and robustness | arXiv preprint arXiv:1708.04527 | 54 |  | 1708.04527 | preprint |
| S226 | 2023 | Validation of the Al-based Predictive OpTimal Trees in Emergency Surgery Risk (POTTER) calculator in patients 65 years and older | Annals of Surgery 277 (1), e8-e15 | 53 | 10.1097/sla.0000000000004714 |  | journal |
| S227 | 2011 | Performance analysis of queueing networks via robust optimization | Operations research 59 (2), 455-466 | 52 | 10.1287/opre.1100.0879 | 1009.3948 | journal |
| S228 | 2021 | Imputation of clinical covariates in time series | Machine Learning 110 (1), 185-248 | 51 | 10.1007/s10994-020-05923-2 | 1812.00418 | journal |
| S229 | 1991 | Probabilistic analysis of the Held and Karp lower bound for the Euclidean traveling salesman problem | Mathematics of operations research 16 (1), 72-89 | 51 | 10.1287/moor.16.1.72 |  | journal |
| S230 | 2020 | Balancing efficiency and fairness in liver transplant access: tradeoff curves for the assessment of organ distribution policies | Transplantation 104 (5), 981-987 | 50 | 10.1097/tp.0000000000003017 |  | journal |
| S231 | 2019 | Comparison of machine learning optimal classification trees with the pediatric emergency care applied research network head trauma decision rules | JAMA pediatrics 173 (7), 648-656 | 50 | 10.1001/jamapediatrics.2019.1068 |  | journal |
| S232 | 2012 | An integer optimization approach to associative classification | Advances in neural information processing systems, 269-277 | 50 |  |  | conference |
| S233 | 2010 | Robust and data-driven approaches to call centers | European Journal of Operational Research 207 (2), 1072-1085 | 50 | 10.1016/j.ejor.2010.05.040 |  | journal |
| S234 | 2007 | Robust optimization in electromagnetic scattering problems | Journal of Applied Physics 101 (7) | 50 | 10.1063/1.2715540 |  | journal |
| S235 | 2022 | Using artificial intelligence to find the optimal margin width in hepatectomy for colorectal cancer liver metastases | JAMA surgery 157 (8), e221819 | 49 | 10.1001/jamasurg.2022.1819 |  | journal |
| S236 | 2021 | Sparse convex regression | INFORMS Journal on Computing 33 (1), 262-279 | 49 | 10.1287/ijoc.2020.0954 |  | journal |
| S237 | 1995 | Branching bandits and Klimov's problem: Achievable region and side constraints | IEEE Transactions on Automatic Control 40 (12), 2063-2075 | 48 | 10.1109/9.478231 |  | journal |
| S238 | 2021 | Selecting children with vesicoureteral reflux who are most likely to benefit from antibiotic prophylaxis: application of machine learning to RIVUR | The Journal of Urology 205 (4), 1170-1179 | 47 | 10.1097/ju.0000000000001445 |  | journal |
| S239 | 1988 | An exact FCFS waiting time analysis for a general class of G/G/_s_ queueing systems | Queueing Systems 3 (4), 305-320 | 46 | 10.1007/bf01157853 |  | journal |
| S240 | 2017 | Regression and classification using optimal decision trees | 2017 IEEE MIT undergraduate research technology conference (URTC), 1-4 | 45 | 10.1109/urtc.2017.8284195 |  | conference |
| S241 | 1997 | A critical survey of optimization models for tactical and strategic aspects of air traffic flow management |  | 45 |  |  | other |
| S242 | 2023 | Artificial intelligence versus surgeon gestalt in predicting risk of emergency general surgery | Journal of Trauma and Acute Care Surgery 95 (4), 565-572 | 44 | 10.1097/ta.0000000000004030 |  | journal |
| S243 | 2022 | Course scheduling under sudden scarcity: Applications to pandemic planning | Manufacturing & Service Operations Management 24 (2), 727-745 | 44 | 10.1287/msom.2021.0996 |  | journal |
| S244 | 2015 | Robust fluid processing networks | IEEE Transactions on Automatic Control 60 (3), 715-728 | 44 | 10.1109/tac.2014.2352711 |  | journal |
| S245 | 2014 | Scheduling, revenue management, and fairness in an academic-hospital radiology division | Academic radiology 21 (10), 1322-1330 | 43 | 10.1016/j.acra.2014.05.009 |  | journal |
| S246 | 2003 | Dynamic classification of online customers | Proceedings of the 2003 SIAM international conference on data mining, 107-118 | 43 | 10.1137/1.9781611972733.10 |  | conference |
| S247 | 2021 | Near-optimal nonlinear regression trees | Operations Research Letters 49 (2), 201-206 | 42 | 10.1016/j.orl.2021.01.002 |  | journal |
| S248 | 2017 | Accept or decline? An analytics-based decision tool for kidney offer evaluation | Transplantation 101 (12), 2898-2904 | 42 | 10.1097/tp.0000000000001824 |  | journal |
| S249 | 2018 | Optimal healthcare decision making under multiple mathematical models: application in prostate cancer screening | Health care management science 21 (1), 105-118 | 41 | 10.1007/s10729-016-9381-3 |  | journal |
| S250 | 2022 | Mixed-projection conic optimization: A new paradigm for modeling rank constraints | Operations Research 70 (6), 3321-3344 | 40 | 10.1287/opre.2021.2182 | 2009.10395 | journal |
| S251 | 2022 | Ethics-by-design: efficient, fair and inclusive resource allocation using machine learning | Journal of Law and the Biosciences 9 (1), lsac012 | 40 | 10.1093/jlb/lsac012 |  | journal |
| S252 | 2024 | Interpretable artificial intelligence to optimise use of imatinib after resection in patients with localised gastrointestinal stromal tumours: an observational cohort study | The Lancet Oncology 25 (8), 1025-1037 | 39 | 10.1016/s1470-2045(24)00259-6 |  | journal |
| S253 | 2024 | Hospital-wide inpatient flow optimization | Management Science 70 (7), 4893-4911 | 39 | 10.1287/mnsc.2023.4933 |  | journal |
| S254 | 2020 | Scalable holistic linear regression | Operations Research Letters 48 (3), 203-208 | 39 | 10.1016/j.orl.2020.02.008 |  | journal |
| S255 | 2007 | A semidefinite optimization approach to the steady-state analysis of queueing systems | Queueing Systems 56 (1), 27-39 | 39 | 10.1007/s11134-007-9028-7 |  | journal |
| S256 | 2001 | Multistage lot sizing problems via randomized rounding | Operations Research 49 (4), 599-608 | 39 | 10.1287/opre.49.4.599.11222 |  | journal |
| S257 | 2017 | Automated dynamic resource allocation for wildfire suppression | Lincoln Laboratory Journal 22 (2), 38-59 | 38 |  |  | journal |
| S258 | 1995 | Decomposition algorithms for analyzing transient phenomena in multiclass queueing networks in air transportation | Operations Research 43 (6), 995-1011 | 38 | 10.1287/opre.43.6.995 |  | journal |
| S259 | 2024 | Reshaping national organ allocation policy | Operations Research 72 (4), 1475-1486 | 37 | 10.1287/opre.2022.0035 |  | journal |
| S260 | 2018 | Optimization over continuous and multi-dimensional decisions with observational data | Advances in neural information processing systems 31 | 37 |  | 1807.04183 | conference |
| S261 | 1989 | The dynamic traveling repairman problem | Sloan School of Management, Massachusetts Institute of Technology | 37 |  |  | report |
| S262 | 2020 | Bus routing optimization helps Boston public schools design better policies | INFORMS Journal on Applied Analytics 50 (1), 37-49 | 36 | 10.1287/inte.2019.1015 |  | journal |
| S263 | 2008 | An analysis of the guaranteed withdrawal benefits for life option | Available at SSRN 1312727 | 35 |  |  | preprint |
| S264 | 2006 | Bounds on linear PDEs via semidefinite optimization | Mathematical programming 108 (1), 135-158 | 35 | 10.1007/s10107-006-0702-z |  | journal |
| S266 | 2025 | Global optimization: a machine learning approach | Journal of Global Optimization 91 (1), 1-37 | 33 | 10.1007/s10898-024-01434-9 | 2311.01742 | journal |
| S267 | 2024 | A machine learning approach to two-stage adaptive robust optimization | European Journal of Operational Research 319 (1), 16-30 | 33 | 10.1016/j.ejor.2024.06.012 | 2307.12409 | journal |
| S268 | 2018 | Robust transient analysis of multi-server queueing systems and feed-forward networks | Queueing Systems 89 (3), 351-413 | 33 | 10.1007/s11134-017-9566-6 |  | journal |
| S269 | 1994 | A technique for speeding up the solution of the Lagrangean dual | Mathematical Programming 63 (1), 23-45 | 33 | 10.1007/bf01582057 |  | journal |
| S270 | 2023 | Pediatric cervical spine injury following blunt trauma in children younger than 3 years: the PEDSPINE II study | JAMA surgery 158 (11), 1126-1132 | 32 | 10.1001/jamasurg.2023.4213 |  | journal |
| S271 | 2023 | An interpretable AI model for recurrence prediction after surgery in gastrointestinal stromal tumour: an observational cohort study | EClinicalMedicine 64 | 32 | 10.1016/j.eclinm.2023.102200 |  | journal |
| S272 | 2022 | POTTER-ICU: An artificial intelligence smartphone-accessible tool to predict the need for intensive care after emergency surgery | Surgery 172 (1), 470-475 | 32 | 10.1016/j.surg.2022.03.023 |  | journal |
| S273 | 2002 | A robust optimization approach to finance | Massachusetts Institute of Technology | 32 |  |  | thesis |
| S274 | 2023 | A new perspective on low-rank optimization | Mathematical Programming 202 (1), 47-92 | 31 | 10.1007/s10107-023-01933-9 | 2105.05947 | journal |
| S275 | 2011 | Multistage air traffic flow management under capacity uncertainty: a robust and adaptive optimization approach |  | 31 |  |  | other |
| S276 | 2021 | Prediction of neutropenic events in chemotherapy patients: A machine learning approach | JCO Clinical Cancer Informatics 5, 904-911 | 30 | 10.1200/cci.21.00046 |  | journal |
| S277 | 2019 | Prediction of cervical spine injury in young pediatric patients: an optimal trees artificial intelligence approach | Journal of pediatric surgery 54 (11), 2353-2357 | 30 | 10.1016/j.jpedsurg.2019.03.007 |  | journal |
| S278 | 2008 | Robust chirped mirrors | Applied optics 47 (14), 2630-2636 | 30 | 10.1364/ao.47.002630 |  | journal |
| S279 | 2005 | Improving air traffic management during thunderstorms | 24th digital avionics systems conference 1, 3. D. 2-31 | 30 | 10.1109/dasc.2005.1563353 |  | conference |
| S280 | 1997 | Multiclass queueing systems in heavy traffic: an asymptotic approach based on distributional and conservation laws | Operations Research 45 (3), 470-487 | 30 | 10.1287/opre.45.3.470 |  | journal |
| S281 | 2019 | Targeted workup after initial febrile urinary tract infection: using a novel machine learning model to identify children most likely to benefit from voiding cystourethrogram | The Journal of Urology 202 (1), 144-152 | 29 |  |  | journal |
| S282 | 2017 | A practically efficient approach for solving adaptive distributionally robust linear optimization problems | Manag. Sci | 29 |  |  | preprint |
| S283 | 2023 | Robust convex optimization: A new perspective that unifies and extends | Mathematical Programming 200 (2), 877-918 | 28 | 10.1007/s10107-022-01881-w |  | journal |
| S284 | 2014 | Optimization-based regimen method and system for personalized diabetes and diet management | US Patent App. 13/587,093 | 28 |  |  | patent |
| S285 | 2023 | Development of a machine learning–based prescriptive tool to address racial disparities in access to care after penetrating trauma | JAMA surgery 158 (10), 1088-1095 | 27 | 10.1001/jamasurg.2023.2293 |  | journal |
| S287 | 2022 | World-class interpretable poker | Machine Learning 111 (8), 3063-3083 | 27 | 10.1007/s10994-022-06179-8 |  | journal |
| S288 | 2020 | Certifiably optimal sparse inverse covariance estimation | Mathematical Programming 184 (1), 491-530 | 27 | 10.1007/s10107-019-01419-7 | 1906.10283 | journal |
| S289 | 1997 | On the worst case complexity of potential reduction algorithms for linear programming | Mathematical Programming 77 (2), 321-333 | 27 | 10.1007/bf02614620 |  | journal |
| S290 | 2024 | Compressed sensing: A discrete optimization approach | Machine Learning 113 (9), 6725-6764 | 26 | 10.1007/s10994-024-06577-0 | 2306.04647 | journal |
| S291 | 1988 | On the steady-state solution of the M/C 2 (a, b)/s queueing system | Transportation science 22 (2), 125-138 | 26 | 10.1287/trsc.22.2.125 |  | journal |
| S292 | 2019 | Clinical benefit, toxicity and cost of metastatic breast cancer therapies: systematic review and meta-analysis | Breast cancer research and treatment 176 (3), 535-543 | 25 | 10.1007/s10549-019-05208-w |  | journal |
| S293 | 1993 | Optimization of polling systems and dynamic vehicle routing problems on networks | Massachusetts Institute of Technology, Operations Research Center | 25 |  |  | report |
| S294 | 2022 | National and subnational short-term forecasting of COVID-19 in Germany and Poland during early 2021 | Communications medicine 2 (1), 136 | 24 | 10.1038/s43856-022-00191-8 |  | journal |
| S295 | 2022 | Validation of the artificial intelligence–based trauma outcomes predictor (TOP) in patients 65 years and older | Surgery 171 (6), 1687-1694 | 24 | 10.1016/j.surg.2021.11.016 |  | journal |
| S296 | 2022 | Machine learning models for mitral valve replacement: a comparative analysis with the Society of Thoracic Surgeons risk score | Journal of cardiac surgery 37 (1), 18-28 | 24 | 10.1111/jocs.16072 |  | journal |
| S297 | 2016 | Advances in robust and adaptive optimization: algorithms, software, and insights | Massachusetts Institute of Technology | 24 |  |  | thesis |
| S298 | 2026 | Global optimization via optimal decision trees | Journal of Global Optimization 95 (1), 23-63 | 23 | 10.1007/s10898-023-01311-x | 2202.06017 | journal |
| S299 | 2022 | Tabtext: A flexible and contextual approach to tabular data representation | arXiv preprint arXiv:2206.10381 10 | 23 |  | 2206.10381 | preprint |
| S300 | 2022 | The backbone method for ultra-high dimensional sparse machine learning | Machine Learning 111 (6), 2161-2212 | 23 | 10.1007/s10994-021-06123-2 | 2006.06592 | journal |
| S301 | 2020 | Fast exact matrix completion: A unified optimization framework for matrix completion | Journal of Machine Learning Research 21 (231), 1-43 | 23 |  | 1910.09092 | journal |
| S302 | 2020 | On polyhedral and second-order cone decompositions of semidefinite optimization problems | Operations Research Letters 48 (1), 78-85 | 23 | 10.1016/j.orl.2019.12.003 | 1910.03143 | journal |
| S303 | 2019 | Covariate-adaptive optimization in online clinical trials | Operations Research 67 (4), 1150-1161 | 23 | 10.1287/opre.2018.1818 |  | journal |
| S304 | 2019 | The airlift planning problem | Transportation Science 53 (3), 773-795 | 23 | 10.1287/trsc.2018.0847 |  | journal |
| S305 | 2007 | Robust nonconvex optimization for simulation-based problems | Operations Research | 23 |  |  | preprint |
| S306 | 1999 | Applications of optimization in probability, finance and revenue management | Massachusetts Institute of Technology | 23 |  |  | thesis |
| S307 | 2025 | Decarbonizing ocp | Manufacturing & Service Operations Management 27 (6), 1760-1778 | 22 | 10.1287/msom.2022.0467 | 2209.06341 | journal |
| S308 | 2023 | A prescriptive machine learning approach to mixed-integer convex optimization | INFORMS Journal on Computing 35 (6), 1225-1241 | 22 | 10.1287/ijoc.2022.0188 |  | journal |
| S309 | 2023 | Global flood prediction: a multimodal machine learning approach | arXiv preprint arXiv:2301.12548 | 22 |  | 2301.12548 | preprint |
| S310 | 2021 | Simple Imputation Rules for Prediction with Missing Data: Contrasting Theoretical Guarantees with Empirical Performance | arXiv preprint arXiv:2104.03158 | 22 |  | 2104.03158 | journal |
| S311 | 2020 | The rise and fall of the model for end-stage liver disease score and the need for an optimized machine learning approach for liver allocation | Current opinion in organ transplantation 25 (2), 122-125 | 22 | 10.1097/mot.0000000000000734 |  | journal |
| S312 | 2020 | Stable regression: On the power of optimization over randomization | Journal of Machine Learning Research 21 (230), 1-25 | 22 |  |  | journal |
| S313 | 2018 | A scalable algorithm for two-stage adaptive linear optimization | arXiv preprint arXiv:1807.02812 | 22 |  | 1807.02812 | preprint |
| S314 | 2016 | Data, models and decisions for large-scale stochastic optimization problems | Massachusetts Institute of Technology | 22 |  |  | thesis |
| S315 | 2013 | An accelerated first-order method for solving SOS relaxations of unconstrained polynomial optimization problems | Optimization Methods and Software 28 (3), 424-441 | 22 | 10.1080/10556788.2012.656114 |  | journal |
| S316 | 2025 | Solving Large‐Scale Weapon Target Assignment Problems in Seconds Using Branch‐Price‐And‐Cut | Naval Research Logistics (NRL) 72 (5), 735-749 | 21 | 10.1002/nav.22249 |  | journal |
| S317 | 2025 | Slowly varying regression under sparsity | Operations Research 73 (3), 1581-1597 | 21 | 10.1287/opre.2022.0330 | 2102.10773 | journal |
| S318 | 2022 | Benchmarking in congenital heart surgery using machine learning-derived optimal classification trees | World Journal for Pediatric and Congenital Heart Surgery 13 (1), 23-35 | 21 | 10.1177/21501351211051227 |  | journal |
| S319 | 2020 | Short-term forecasting of COVID-19 in Germany and Poland during the second wave–a preregistered study | medRxiv, 2020.12. 24.20248826 | 21 | 10.1101/2020.12.24.20248826 |  | preprint |
| S320 | 2015 | Foundations and trends� | Mach. Learn 8 (3-4), 231-357 | 21 |  |  | other |
| S321 | 2008 | Data-driven approach to health care: applications using claims data | Massachusetts Institute of Technology | 21 |  |  | thesis |
| S322 | 1999 | Decomposition results for general polling systems and their applications | Queueing Systems 31 (3), 295-316 | 21 | 10.1023/a:1019118516504 |  | journal |
| S323 | 1997 | Estimation of time-varying parameters in statistical models: an optimization approach | Proceedings of the tenth annual conference on Computational learning theory�… | 21 | 10.1145/267460.267519 |  | conference |
| S324 | 1995 | Nonlinear formulations and improved randomized approximation algorithms for multicut problems | International Conference on Integer Programming and Combinatorial�… | 21 | 10.1007/3-540-59408-6_39 |  | conference |
| S325 | 2021 | Personalized prescription of ACEI/ARBs for hypertensive COVID-19 patients | Health Care Management Science 24 (2), 339-355 | 20 | 10.1007/s10729-021-09545-5 |  | journal |
| S326 | 2019 | Identifying exceptional responders in randomized trials: An optimization approach | INFORMS Journal on Optimization 1 (3), 187-199 | 20 | 10.1287/ijoo.2018.0006 |  | journal |
| S327 | 2016 | Scalable robust and adaptive inventory routing | Optim. Online, 1-29 | 20 |  |  | preprint |
| S328 | 2013 | A new local search algorithm for binary optimization | INFORMS Journal on Computing 25 (2), 208-221 | 20 | 10.1287/ijoc.1110.0496 |  | journal |
| S329 | 1988 | Analysis of the stationary Ek/C2/s queueing system | European Journal of Operational Research 37 (2), 272-287 | 20 | 10.1016/0377-2217(88)90336-0 |  | journal |
| S330 | 2024 | Robust and adaptive optimization under a large language model lens | arXiv preprint arXiv:2501.00568 | 19 |  | 2501.00568 | preprint |
| S331 | 2024 | Holistic deep learning | Machine Learning 113 (1), 159-183 | 19 | 10.1007/s10994-023-06482-y | 2110.15829 | journal |
| S332 | 2023 | Policy analytics in public school operations | Operations Research 71 (1), 289-313 | 19 | 10.1287/opre.2022.2373 |  | journal |
| S333 | 2022 | Distributionally robust causal inference with observational data | arXiv preprint arXiv:2210.08326 | 19 |  | 2210.08326 | preprint |
| S334 | 2022 | Queueing Theory: Classical and Modern Methods |  | 19 |  |  | book |
| S335 | 2019 | Predictive and prescriptive methods in operations research and machine learning: an optimization approach | Massachusetts Institute of Technology | 19 |  |  | thesis |
| S336 | 1996 | A unified method to analyze overtake free queueing systems | Advances in applied probability 28 (2), 588-625 | 19 | 10.2307/1428073 |  | journal |
| S337 | 2024 | Marginal pricing in adaptive robust unit commitment under load and capacity uncertainty | IEEE Transactions on Power Systems 40 (1), 341-354 | 18 | 10.1109/tpwrs.2024.3406504 |  | journal |
| S338 | 2023 | Ensemble modeling for time series forecasting: an adaptive robust optimization approach | arXiv preprint arXiv:2304.04308 | 18 |  | 2304.04308 | preprint |
| S339 | 2022 | Toward global food security: Transforming OCP through analytics | INFORMS Journal on Applied Analytics 52 (1), 90-107 | 18 | 10.1287/inte.2021.1111 |  | journal |
| S340 | 2014 | A comparison of Monte Carlo tree search and mathematical optimization for large scale dynamic resource allocation | arXiv preprint arXiv:1405.5498 | 18 |  | 1405.5498 | preprint |
| S341 | 1999 | Analysis of LP relaxations for multiway and multicut problems | Networks: An International Journal 34 (2), 102-114 | 18 | 10.1002/(sici)1097-0037(199909)34:2<102::aid-net3>3.0.co;2-x |  | journal |
| S342 | 1995 | Airline yield management in a dynamic network environment | Massachusetts Institute of Technology | 18 |  |  | thesis |
| S343 | 2020 | Prescriptive analytics for reducing 30-day hospital readmissions after general surgery | PloS one 15 (9), e0238118 | 17 | 10.1371/journal.pone.0238118 |  | journal |
| S344 | 2020 | Relative robust and adaptive optimization | INFORMS Journal on Computing 32 (2), 408-427 | 17 | 10.1287/ijoc.2018.0860 |  | journal |
| S345 | 1997 | The parsimonious property of cut covering problems and its applications | Operations Research Letters 21 (3), 123-132 | 17 | 10.1016/s0167-6377(97)00032-1 |  | journal |
| S346 | 1991 | Transient and busy period analysis of the GIG/1 Queue as a Hilbert factorization problem | Journal of applied probability 28 (4), 873-885 | 17 | 10.1017/s0021900200042789 |  | journal |
| S347 | 2025 | A stochastic benders decomposition scheme for large-scale stochastic network design | INFORMS Journal on Computing 37 (5), 1163-1181 | 16 | 10.1287/ijoc.2023.0074 | 2303.07695 | journal |
| S348 | 2024 | Pareto adaptive robust optimality via a Fourier–Motzkin elimination lens | Mathematical Programming 205 (1), 485-538 | 16 | 10.1007/s10107-023-01983-z | 2012.04419 | journal |
| S350 | 2002 | Joint network pricing and resource allocation | Working paper, Massachusetts Institute of Technology, Cambridge, MA | 16 |  |  | report |
| S351 | 2024 | M3H: multimodal multitask machine learning for healthcare | arXiv preprint arXiv:2404.18975 | 15 |  | 2404.18975 | preprint |
| S352 | 2023 | Patient outcome predictions improve operations at a large hospital network | arXiv preprint arXiv:2305.15629 | 15 |  | 2305.15629 | preprint |
| S353 | 2022 | Data-driven interpretable policy construction for personalized mobile health | 2022 IEEE international conference on digital health (ICDH), 13-22 | 15 | 10.1109/icdh55609.2022.00010 |  | conference |
| S354 | 2021 | Algorithmic insurance | arXiv preprint arXiv:2106.00839 | 15 |  | 2106.00839 | preprint |
| S355 | 2020 | Sparse hierarchical regression with polynomials | Machine Learning 109 (5), 973-997 | 15 | 10.1007/s10994-020-05868-6 | 1709.10030 | journal |
| S356 | 2023 | Explainable vs. interpretable artificial intelligence frameworks in oncology | Translational Cancer Research 12 (2), 217 | 14 | 10.21037/tcr-22-2427 |  | journal |
| S357 | 2020 | Computation of exact bootstrap confidence intervals: Complexity and deterministic algorithms | Operations Research 68 (3), 949-964 | 14 | 10.1287/opre.2019.1904 |  | journal |
| S358 | 2019 | Learning a mixture of gaussians via mixed-integer optimization | INFORMS Journal on Optimization 1 (3), 221-240 | 14 | 10.1287/ijoo.2018.0009 |  | journal |
| S359 | 2018 | From physical properties of transportation flows to demand estimation: An optimization approach | Transportation Science 52 (4), 1002-1011 | 14 | 10.1287/trsc.2017.0802 |  | journal |
| S360 | 2015 | Optimizing over coherent risk measures and non-convexities: a robust mixed integer optimization approach | Computational Optimization and Applications 62 (3), 613-639 | 14 | 10.1007/s10589-015-9755-3 |  | journal |
| S361 | 2012 | System-level optimization in wireless networks: managing interference and uncertainty via robust optimization | IEEE/ACM Transactions on Networking 20 (2), 339-352 | 14 |  |  | other |
| S362 | 1995 | Dynamic slot allocation with airline participation | Massachusetts Institute of Technology | 14 |  |  | thesis |
| S363 | 1990 | The departure process from a | GI/G 1, 245-91 | 14 |  |  | report |
| S364 | 2022 | Improving quality in cardiothoracic surgery: exploiting the untapped potential of machine learning | The Annals of Thoracic Surgery 114 (6), 1995-2000 | 13 | 10.1016/j.athoracsur.2022.06.058 |  | journal |
| S365 | 2022 | Stable classification | Journal of Machine Learning Research 23 (296), 1-53 | 13 |  |  | journal |
| S366 | 2021 | Frequency estimation in data streams: Learning the optimal hashing scheme | IEEE Transactions on Knowledge and Data Engineering 35 (2), 1541-1553 | 13 | 10.1109/tkde.2021.3103819 | 2007.09261 | journal |
| S368 | 1999 | Bounds and policies for dynamic routing in loss networks | Operations research 47 (3), 379-394 | 13 | 10.1287/opre.47.3.379 |  | journal |
| S369 | 2023 | Improving stability in decision tree models | arXiv preprint arXiv:2305.17299 | 12 |  | 2305.17299 | preprint |
| S370 | 2022 | Ensemble machine learning for personalized antihypertensive treatment | Naval Research Logistics (NRL) 69 (5), 669-688 | 12 | 10.1002/nav.22040 |  | journal |
| S371 | 2014 | Introduction to the special issue on business analytics | Management Science 60 (6), 1351-1351 | 12 | 10.1287/mnsc.2014.1990 |  | journal |
| S372 | 2012 | Integer optimization methods for machine learning | Massachusetts Institute of Technology | 12 |  |  | thesis |
| S373 | 2011 | Applications of robust optimization to queueing and inventory systems | Massachusetts Institute of Technology | 12 |  |  | thesis |
| S374 | 2009 | A robust optimization approach to statistical estimation problems by Apostolos G. Fertis. | Massachusetts Institute of Technology | 12 |  |  | thesis |
| S375 | 2024 | Congenital heart surgery machine learning-derived in-depth benchmarking tool | The Annals of Thoracic Surgery 118 (1), 199-206 | 11 | 10.1016/j.athoracsur.2023.10.034 |  | journal |
| S376 | 2023 | High-performance pediatric surgical risk calculator: a novel algorithm based on machine learning and pediatric NSQIP data | The American Journal of Surgery 226 (1), 115-121 | 11 | 10.1016/j.amjsurg.2023.03.009 |  | journal |
| S377 | 2023 | A novel algorithm for a broad class of nonconvex optimization problems | Optimization Online | 11 |  |  | preprint |
| S378 | 2020 | A Look at Robustness and Stability of \-versus \-Regularization: Discussion of Papers by Bertsimas et al. and Hastie et al. |  | 11 |  |  | other |
| S379 | 2020 | Stochastic optimization in supply chain networks: averaging robust solutions | Optimization Letters 14 (4), 839-855 | 11 | 10.1007/s11590-019-01405-0 |  | journal |
| S380 | 2014 | Closure to the discussion of “adaptive robust optimization for the security constrained unit commitment problem” | IEEE Transactions on Power Systems 29 (2), 996-997 | 11 | 10.1109/tpwrs.2014.2301352 |  | journal |
| S381 | 2025 | An artificial intelligence interpretable tool to predict risk of deep vein thrombosis after endovenous thermal ablation | Journal of Vascular Surgery: Venous and Lymphatic Disorders 13 (5), 102253 | 10 | 10.1016/j.jvsv.2025.102253 |  | journal |
| S382 | 2023 | Applying analytics to design lung transplant allocation policy | INFORMS journal on applied analytics 53 (5), 350-358 | 10 | 10.1287/inte.2023.0036 |  | journal |
| S383 | 2023 | Interpretable matrix completion: A discrete optimization approach | INFORMS Journal on Computing 35 (5), 952-965 | 10 | 10.1287/ijoc.2022.0022 | 1812.06647 | journal |
| S384 | 2023 | Reducing air pollution through machine learning | arXiv preprint arXiv:2303.12285 | 10 |  | 2303.12285 | preprint |
| S385 | 2023 | Optimal low-rank matrix completion: Semidefinite relaxations and eigenvector disjunctions | arXiv preprint arXiv:2305.12292 | 10 |  | 2305.12292 | preprint |
| S386 | 2021 | A robust optimization approach to deep learning | arXiv preprint arXiv:2112.09279 | 10 |  | 2112.09279 | preprint |
| S387 | 2013 | Airport operations optimization | US Patent App. 13/176,033 | 10 |  |  | patent |
| S388 | 1998 | Multiperiod portfolio optimization in the presence of transaction costs | Massachusetts Institute of Technology | 10 |  |  | thesis |
| S389 | 1990 | Relations between the prearrival and postdeparture state probabilities and the fcfs waiting time distribution in the _E__k_/_G/s_ queue | Naval Research Logistics (NRL) 37 (1), 135-149 | 10 | 10.1002/1520-6750(199002)37:1<135::aid-nav3220370109>3.0.co;2-f |  | journal |
| S390 | 2026 | Holistic AI in medicine; improved performance and explainability | NPJ Digital Medicine 9 (1), 120 | 9 | 10.1038/s41746-025-02298-3 |  | journal |
| S391 | 2025 | Adaptive optimization for prediction with missing data | Machine Learning 114 (5), 124 | 9 | 10.1007/s10994-025-06757-6 | 2402.01543 | journal |
| S392 | 2025 | The benefit of uncertainty coupling in robust and adaptive robust optimization | INFORMS Journal on Optimization 7 (2), 105-141 | 9 | 10.1287/ijoo.2023.0007 | 2302.10369 | journal |
| S393 | 2024 | The ROAD to precision medicine | npj Digital Medicine 7 (1), 307 | 9 | 10.1038/s41746-024-01291-6 | 2311.01681 | journal |
| S394 | 2023 | Automated segmentation of sacral chordoma and surrounding muscles using deep learning ensemble | International Journal of Radiation Oncology* Biology* Physics 117 (3), 738-749 | 9 | 10.1016/j.ijrobp.2023.03.078 |  | journal |
| S395 | 2021 | Toward an optimized staging system for pancreatic ductal adenocarcinoma: a clinically interpretable, artificial intelligence–based model | JCO clinical cancer informatics 5, 1220-1231 | 9 | 10.1200/cci.21.00001 |  | journal |
| S396 | 2020 | Novel mixed integer optimization sparse regression approach in chemometrics | Analytica Chimica Acta 1137, 115-124 | 9 | 10.1016/j.aca.2020.08.054 |  | journal |
| S397 | 2020 | The edge of optimization in large-scale vehicle routing for paratransit | Tech. rept. https://dbertsim. mit. edu/pdfs/papers/2020-yan-transporation… | 9 |  |  | report |
| S398 | 2014 | Data-driven models for uncertainty and behavior | Massachusetts Institute of Technology | 9 |  |  | thesis |
| S399 | 2011 | Decomposition methods for large scale stochastic and robust optimization problems | Massachusetts Institute of Technology | 9 |  |  | thesis |
| S400 | 2025 | Constructing uncertainty sets from covariates in power systems | IEEE Transactions on Power Systems 40 (5), 3943-3954 | 8 | 10.1109/tpwrs.2025.3530410 |  | journal |
| S401 | 2024 | Towards stable machine learning model retraining via slowly varying sequences | arXiv preprint arXiv:2403.19871 | 8 |  | 2403.19871 | preprint |
| S402 | 2023 | Optimal control of multiclass fluid queueing networks: A machine learning approach | arXiv preprint arXiv:2307.12405 | 8 |  | 2307.12405 | preprint |
| S403 | 2023 | Multistage stochastic optimization via kernels | arXiv preprint arXiv:2303.06515 | 8 |  | 2303.06515 | preprint |
| S407 | 2020 | Optimizing influenza vaccine composition: From predictions to prescriptions | Machine Learning for Healthcare Conference, 121-142 | 8 |  |  | conference |
| S408 | 2020 | Novel target discovery of existing therapies: Path to personalized cancer therapy | Informs Journal on Optimization 2 (1), 1-13 | 8 | 10.1287/ijoo.2019.0019 |  | journal |
| S409 | 2019 | Tensor completion with noisy side information for the predcition of anti-cancer drug response | Submitted | 8 |  |  | preprint |
| S411 | 2014 | Reformulations versus cutting planes for robust optimization: A computational and machine learning perspective | Optimization Online | 8 |  |  | preprint |
| S412 | 2010 | A discrete optimization approach to supervised ranking | Proceedings of the 5th INFORMS workshop on data mining and health… | 8 |  |  | conference |
| S413 | 2008 | Approximating integrals of multivariate exponentials: A moment approach | Operations Research Letters 36 (2), 205-210 | 8 | 10.1016/j.orl.2007.07.002 |  | journal |
| S414 | 2006 | Option pricing without price dynamics: a probabilistic approach | arXiv preprint math/0612075 | 8 |  | math/0612075 | preprint |
| S415 | 2026 | Cone product reformulation for global optimization | INFORMS Journal on Computing | 7 | 10.1287/ijoc.2023.0345 |  | journal |
| S416 | 2024 | Optimization automates emergency department nurse scheduling at Hartford hospital | INFORMS Journal on Applied Analytics 54 (6), 553-574 | 7 | 10.1287/inte.2023.0071 |  | journal |
| S418 | 2023 | Holistic prescriptive analytics for continuous and constrained optimization problems | INFORMS Journal on Optimization 5 (2), 155-171 | 7 | 10.1287/ijoo.2022.0080 |  | journal |
| S419 | 2022 | Multi-objective optimization for public policy | Massachusetts Institute of Technology | 7 |  |  | thesis |
| S420 | 2021 | Optimizing influenza vaccine composition: A machine learning approach | Naval Research Logistics (NRL) 68 (7), 857-870 | 7 | 10.1002/nav.21974 |  | journal |
| S421 | 2021 | The price of diversity | arXiv preprint arXiv:2107.03900 | 7 |  | 2107.03900 | preprint |
| S422 | 2019 | Machine learning for problems with missing and uncertain data with applications to personalized medicine | Massachusetts Institute of Technology | 7 |  |  | thesis |
| S423 | 2014 | An analytics approach to hypertension treatment | Massachusetts Institute of Technology | 7 |  |  | thesis |
| S424 | 2009 | On the equivalence of robust optimization and regularization in statistics | Submitted to Operations Research | 7 |  |  | preprint |
| S426 | 2025 | Efficient domain adaptation of multimodal embeddings using constrastive learning | arXiv preprint arXiv:2502.02048 | 6 |  | 2502.02048 | preprint |
| S427 | 2024 | Ensembling wind forecasting models to construct data-driven uncertainty sets in robust optimization | 2024 IEEE Power & Energy Society General Meeting (PESGM), 1-5 | 6 | 10.1109/pesgm51994.2024.10688592 |  | conference |
| S428 | 2023 | Data-driven COVID-19 vaccine development for Janssen | INFORMS Journal on Applied Analytics 53 (1), 70-84 | 6 | 10.1287/inte.2022.1150 |  | journal |
| S429 | 2022 | Sparse PCA: A geometric approach | arXiv preprint arXiv:2210.06590 | 6 |  | 2210.06590 | journal |
| S430 | 2022 | Machine learning reimagined: the promise of interpretability to combat bias | Annals of Surgery 275 (6), e738-e739 | 6 | 10.1097/sla.0000000000005396 |  | journal |
| S432 | 2018 | Multitarget tracking via mixed integer optimization | IEEE Transactions on Automatic Control 63 (11), 3627-3642 | 6 | 10.1109/tac.2018.2832468 |  | journal |
| S433 | 2011 | Network information theory via robust optimization | Submitted for publication | 6 |  |  | preprint |
| S434 | 2000 | Moment problems via semidefinite programming: Applications in probability and finance | INSEAD | 6 |  |  | report |
| S435 | 1996 | Improved randomized approximation algorithms for lot-sizing problems | International Conference on Integer Programming and Combinatorial… | 6 | 10.1007/3-540-61310-2_27 |  | conference |
| S436 | 1995 | Optimization of queueing networks: an optimal control appraoch | Massachusetts Institute of Technology | 6 |  |  | thesis |
| S438 | 1992 | Probability and algorithms | National Academies Press | 6 |  |  | report |
| S439 | 2026 | Leveraging multimodal machine learning for accurate risk identification of intimate partner violence | npj Women's Health 4 (1), 15 | 5 | 10.1038/s44294-025-00126-3 |  | journal |
| S440 | 2025 | From Data to Uncertainty Sets: a Machine Learning Approach | arXiv preprint arXiv:2503.02173 | 5 |  | 2503.02173 | preprint |
| S442 | 2023 | Accelerating vaccine innovation for emerging infectious diseases via parallel discovery | Entrepreneurship and Innovation Policy and the Economy 2 (1), 9-39 | 5 | 10.1086/723234 |  | journal |
| S443 | 2022 | Stochastic cutting planes for data-driven optimization | INFORMS Journal on Computing 34 (5), 2400-2409 | 5 | 10.1287/ijoc.2022.1205 | 2103.02506 | journal |
| S444 | 2021 | Prescriptive machine learning for public policy: The case of immigration enforcement | Computer Sciences. Under Review | 5 |  |  | preprint |
| S445 | 2019 | The K-server problem via a modern optimization lens | European Journal of Operational Research 276 (1), 65-78 | 5 | 10.1016/j.ejor.2018.12.044 |  | journal |
| S446 | 2015 | Distributionally robust control and optimization | ETH Zurich | 5 |  |  | thesis |
| S447 | 2013 | Personalized diabetes management | Massachusetts Institute of Technology | 5 |  |  | thesis |
| S448 | 2012 | Ordered rules for classification: A discrete optimization approach to associative classification | Poster in Proceesings of Neural Information Processing Systems Foundations… | 5 |  |  | conference |
| S449 | 2008 | Analysis and Optimization of the Emergency Department at Beth Israel Deaconess Medical Center via Simulation | Massachusetts Institute of Technology | 5 |  |  | thesis |
| S450 | 2004 | Option pricing without price dynamics: a geometric approach | Operations Research Center, MIT, working paper | 5 |  |  | report |
| S451 | 2003 | Integer optimization in data mining | Massachusetts Institute of Technology | 5 |  |  | thesis |
| S452 | 2002 | Applications of semidefinite optimization in stochastic project scheduling |  | 5 |  |  | other |
| S453 | 1998 | Greedy, randomized and approximate dynamic programming algorithms for facility location problems |  | 5 |  |  | other |
| S456 | 2025 | Should We Relax Stability in Matching Markets? | arXiv preprint arXiv:2509.14475 | 4 |  | 2509.14475 | preprint |
| S457 | 2025 | Multimodal prescriptive deep learning | arXiv preprint arXiv:2501.14152 | 4 |  | 2501.14152 | journal |
| S458 | 2024 | Robust linear algebra | European Journal of Operational Research 314 (3), 1174-1184 | 4 | 10.1016/j.ejor.2023.11.036 |  | journal |
| S459 | 2022 | Sparse regression over clusters: SparClur | Optimization Letters 16 (2), 433-448 | 4 | 10.1007/s11590-021-01770-9 |  | journal |
| S460 | 2020 | Learning high order feature interactions with fine control kernels | arXiv preprint arXiv:2002.03298 | 4 |  |  | other |
| S461 | 2020 | Interpretable machine learning methods with applications to health care | Massachusetts Institute of Technology | 4 |  |  | thesis |
| S462 | 2012 | On the power of nature in robust discrete optimization | preparation | 4 |  |  | preprint |
| S463 | 2010 | Patterns of heart attacks | Massachusetts Institute of Technology | 4 |  |  | thesis |
| S464 | 2006 | Robust and Adaptive Optimization; a Tractable Approach to Optimization Under Uncertainty | NSF Award 5 (556106), 56106 | 4 |  |  | other |
| S465 | 2006 | No-arbitrage bounds on american put options with a single maturity | Massachusetts Institute of Technology | 4 |  |  | thesis |
| S466 | 2006 | Multistage finite adaptability: Application to air traffic control | Working Paper, Massachusetts Institute of Technology | 4 |  |  | report |
| S467 | 2003 | Finance without price dynamics | Massachusetts Institute of Technology | 4 |  |  | thesis |
| S468 | 1994 | Bounds for loss networks | preparation | 4 |  |  | preprint |
| S470 | 1812 | Interpretable Clustering via Optimal Trees | arXiv | 4 |  | 1812.00539 | preprint |
| S474 | 2026 | RocketPFN: Accurate Time Series Classification via In-Context Learning | arXiv preprint arXiv:2606.21786 | 3 |  | 2606.21786 | preprint |
| S475 | 2026 | Predictive low rank matrix learning under partial observations: Mixed-projection ADMM | Machine Learning 115 (6), 131 | 3 | 10.1007/s10994-026-07005-1 | 2407.13731 | journal |
| S476 | 2025 | Modernizing the design process for us organ allocation policy: Toward a continuous distribution policy for kidneys | Transplantation Direct 11 (9), e1780 | 3 | 10.1097/txd.0000000000001780 |  | journal |
| S477 | 2024 | Deep Trees for (Un) structured Data: Tractability, Performance, and Interpretability | arXiv preprint arXiv:2410.21595 | 3 |  | 2410.21595 | preprint |
| S478 | 2024 | Binary Classification: Is Boosting stronger than Bagging? | arXiv preprint arXiv:2410.19200 | 3 |  | 2410.19200 | preprint |
| S479 | 2024 | An exact method for a class of robust nonlinear optimization problems | 25th International Symposium on Mathematical Programming (ISMP2024) | 3 |  |  | talk |
| S480 | 2024 | Interpretable algorithmic fairness in structured and unstructured data | Journal of Machine Learning Research 25 (215), 1-42 | 3 |  |  | journal |
| S481 | 2023 | Personalized breast cancer screening | JCO Clinical Cancer Informatics 7, e2300026 | 3 | 10.1200/cci.23.00026 |  | journal |
| S482 | 2022 | THEMIS: a framework for cost-benefit analysis of COVID-19 non-pharmaceutical interventions | MedRxiv, 2022.04. 09.22273656 | 3 | 10.1101/2022.04.09.22273656 |  | preprint |
| S483 | 2022 | Disease diagnosis using spectroscopy and machine learning | US Patent App. 17/368,793 | 3 |  |  | patent |
| S485 | 2020 | From data to decisions in urban transit and logistics | Massachusetts Institute of Technology | 3 |  |  | thesis |
| S486 | 2019 | MP64-03 SELECTING CHILDREN WITH VUR WHO ARE MOST LIKELY TO BENEFIT FROM ANTIBIOTIC PROPHYLAXIS: APPLICATION OF MACHINE LEARNING TO RIVUR DATA | The Journal of Urology 201 (Supplement 4), e941-e941 | 3 | 10.1097/01.ju.0000556895.20387.16 |  | conference |
| S487 | 2019 | New Methods of Natural Language Processing using Machine Learning Methods to Identify Ischemic Stroke Presence, Acuity and Location from Clinical Radiology Reports |  | 3 |  |  | other |
| S488 | 2019 | The price of flexibility | Unpublished manuscript | 3 |  |  | preprint |
| S489 | 2013 | Measuring quality in diabetes care: an expert-based statistical approach | SpringerPlus 2 (1), 226 | 3 | 10.1186/2193-1801-2-226 |  | journal |
| S490 | 2013 | Personalized diabetes management: A robust optimization approach | Submitted | 3 |  |  | preprint |
| S491 | 2012 | Call for Papers Special Issue of Management Science: Business Analytics: Submission deadline: September 16, 2012 Expected publication date: First Quarter 2014 | Management Science 58 (7), 1422-1422 | 3 | 10.1287/mnsc.1120.1637 |  | journal |
| S492 | 2012 | Unified Optimization of Traffic Flows through Airports | Proceedings of the 52 nd AGIFORS Annual Symposium, Scottsdale, United States | 3 |  |  | conference |
| S494 | 2009 | Max-min fairness in the air traffic flow management problem | Working Paper | 3 |  |  | report |
| S496 | 2008 | Quality of care and drug surveillance: A data-driven perspective | Massachusetts Institute of Technology | 3 |  |  | thesis |
| S497 | 2008 | Empirical comparison of robust, data driven and stochastic optimization | Massachusetts Institute of Technology | 3 |  |  | thesis |
| S498 | 2007 | Optimal data fitting: a moment approach | Research report, Sloan School of Management, MIT, Boston, MA | 3 |  |  | report |
| S499 | 2006 | Multivariate exponential integral approximations: a moment approach | Technical Report, Operations Research Center, MIT | 3 |  |  | report |
| S500 | 2002 | Geometry, moments, and semidefinite optimization | Proceedings of the 15th International Symposium on MTNS | 3 |  |  | conference |
| S501 | 2001 | Solving linear partial differential equations via semidefinite optimization | Massachusetts Institute of Technology | 3 |  |  | thesis |
| S502 | 2000 | Simulation-based optimization for airline network yield management' | Working Paper, Massachusetts Institute of Technology, USA | 3 |  |  | report |
| S504 | 1999 | Optimal bounds in finance: An optimization approach | Working paper, MIT, http://www. insead. fr/facultyresearch/tm/popescu | 3 |  |  | report |
| S505 | 1997 | Optimal control of queueing networks: A singular pertubation approach | 9th INFORMS Applied Probability Conference | 3 |  |  | talk |
| S506 | 1996 | A Critical Review of Optimization Models and Their Potential Application to the European Air Traffic Flow Management System | prepared for the NOAA Project of the European Commission (unpublished) | 3 |  |  | report |
| S507 | 1994 | A linear control approach to optimization of multiclass queueing networks | preparation | 3 |  |  | preprint |
| S516 |  | Code for generating the HAIM multimodal dataset of MIMIC-IV clinical data and x-rays. 2022 | DOI | 3 |  |  | other |
| S522 | 2026 | Wfdronebench: A benchmark for sensor placement and drone routing for wildfire detection | arXiv preprint arXiv:2609.11829 | 2 |  | 2609.11829 | preprint |
| S523 | 2025 | Adaptive forests for classification | arXiv preprint arXiv:2510.22991 | 2 |  | 2510.22991 | preprint |
| S524 | 2025 | Holistic Artificial Intelligence in Medicine; improved performance and explainability | arXiv preprint arXiv:2507.00205 | 2 |  | 2507.00205 | preprint |
| S525 | 2025 | PO-05-166 AI-enabled multi-class diagnosis of left ventricular ejection fraction from electrocardiograms | Heart Rhythm 22 (4), S540 | 2 | 10.1016/j.hrthm.2025.03.1350 |  | conference |
| S526 | 2025 | Using Interpretable Artificial Intelligence Algorithms in the Management of Blunt Splenic Trauma: Applications of Optimal Policy Trees as a Treatment Prescription Aid to Improve Patient Mortality | Bioengineering 12 (4), 336 | 2 | 10.3390/bioengineering12040336 |  | journal |
| S527 | 2025 | The ROAD to clinical trial emulation | Research Square, rs. 3. rs-5576146 | 2 | 10.21203/rs.3.rs-5576146/v1 | 2412.03528 | preprint |
| S528 | 2024 | Skip Transformers: Efficient Inference through Skip-Routing | NeurIPS 2024 Workshop on Fine-Tuning in Modern Machine Learning: Principles�… | 2 |  |  | conference |
| S529 | 2023 | Use of artificial intelligence for nonlinear benchmarking of surgical care | Surgery 174 (6), 1302-1308 | 2 | 10.1016/j.surg.2023.08.025 |  | journal |
| S530 | 2023 | Robust Regression over Averaged Uncertainty | arXiv preprint arXiv:2311.06960 | 2 |  | 2311.06960 | preprint |
| S531 | 2023 | Adaptive pricing in unit commitment under load and capacity uncertainty | arXiv preprint arXiv:2309.08162 | 2 |  | 2309.08162 | preprint |
| S532 | 2023 | Multimodality: Models, Algorithms, and Applications | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S533 | 2023 | Optimal decision making for healthcare operations: models and implementation | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S536 | 2022 | Data-driven healthcare via constraint learning and analytics | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S537 | 2022 | Global and Robust Optimization for Engineering Design | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S540 | 2021 | Essays on decision making under uncertainty | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S541 | 2021 | Optimizing school operations | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S543 | 2020 | Time series that are robust to regime changes | J. Mach. Learn. Res. 21, 1-31 | 2 |  |  | journal |
| S546 | 2020 | Mortality risk calculatory | URL https://www. covidanalytics. io/calculator | 2 |  |  | other |
| S547 | 2019 | Data-driven dynamic optimization with auxiliary covariates | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S548 | 2019 | Accounting for significance and multicollinearity in building linear regression models | arXiv 2019 | 2 |  | 1902.03272 | preprint |
| S549 | 2018 | Sparsity and robustness in modern statistical estimation | Massachusetts Institute of Technology, Sloan School of Management�… | 2 |  |  | thesis |
| S550 | 2018 | Optimal Trees for Prediction and Prescription | Dynamic Ideas | 2 |  |  | book |
| S551 | 2018 | Learning under uncertainty: an adaptive optimization perspective | Woking Paper | 2 |  |  | report |
| S554 | 2015 | Channel coding via robust optimization, part 1: The case of a single channel | Submitted for publication | 2 |  |  | preprint |
| S555 | 2015 | Analytics for improved cancer screening and treatment | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S557 | 2014 | Semi-supervised approach to predictive analysis using temporal data | Military Operations Research 19 (1), 37-50 | 2 | 10.5711/1082598319137 |  | journal |
| S558 | 2013 | Weapon coordination in a fleet: Centralized and distributed optimization | MIT Lincoln Laboratory. Working paper | 2 |  |  | report |
| S559 | 2011 | ORC; Ordered rules for classification | Oper. Res. Center, Mass. Inst. Tech., Working Paper OR 386-11 | 2 |  |  | report |
| S560 | 2011 | On the complexity of constructing adaptive policies in two-stage linear optimization | Working Paper | 2 |  |  | report |
| S561 | 2011 | Integer optimization methods for supervised ranking | Operations Research Center Working Paper Series OR, 388-11 | 2 |  |  | report |
| S563 | 2010 | Optimization under moment, robust, and data-driven models of uncertainty | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S564 | 2009 | Optimization methods | Technical report, MIT, 2009. Disponible � http://ocw. mit. edu/courses | 2 |  |  | other |
| S566 | 2009 | Optimality of Affine Policies in Multi-Stage Robust Optimization LIDS Tech | Rep | 2 |  |  | report |
| S567 | 2009 | Fairness in the Air Traffic Flow Management Problem | Transportation Science, submitted for publication | 2 |  |  | preprint |
| S569 | 2004 | Reducing variability in equipment availability at Intel using systems optimization | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S571 | 2002 | Optimal control of fluid tandem networks | Manuscript in preparation | 2 |  |  | preprint |
| S573 | 1999 | Scheduling multiclass queueing networks and job shops using fluid and semidefinite relaxations | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S574 | 1998 | Queues: Theory & Applications | MIT | 2 |  |  | other |
| S575 | 1998 | Tax-Aware Multiperiod Portfolio Optimization | MIT Sloan School of Management, Cambridge, Mass | 2 |  |  | report |
| S577 | 1996 | Constructing approximation algorithms via linear programming relaxations | Doctoral Thesis, MIT, Cambridge, MA., D. Bertsimas. 1996. On improved�… | 2 |  |  | thesis |
| S580 | 1994 | A mathematical programming approach to stochastic optimization problems | Operations Research Center, MIT, working paper | 2 |  |  | report |
| S581 | 1994 | Polling model and vehicle routing problem | Technical Report, MIT | 2 |  |  | report |
| S582 | 1993 | On a characterization of the minimum assignment and matching in the independent random model. | IPCO, 161-169 | 2 |  |  | conference |
| S584 | 1993 | Scheduling of multiclass queueing networks: Bounds on achievable performance | MIT | 2 |  |  | thesis |
| S585 | 1993 | Problems in discrete optimization | MIT | 2 |  |  | thesis |
| S587 | 1992 | Scheduling of M ulticlass Networks: Bounds on Achievable Performance | Workshop on Hierarchical Control for Real—time Scheduling of Man ufacturing… | 2 |  |  | conference |
| S588 | 1991 | How much cash should a bank maintain?: an optimization approach | Massachusetts Institute of Technology | 2 |  |  | thesis |
| S591 | 1988 | The probabilistic assignment problem and the probabilistic shortest path problem | preparation | 2 |  |  | preprint |
| S596 |  | Data-driven assortment optimization. 2015 | URL: http://silkrouteglobal. com/files/4314/4404/7411�… | 2 |  |  | other |
| S597 |  | Stochastic and Dynamic Vehicle Routing in the Euclidean Plane: The Multiple-Server, Capacitated Vehicle Case. 1990 |  | 2 |  |  | other |
| S599 |  | CH. and TSITSIKLIS, JN (1992a). Optimization of multiclass queueing networks: Polyhedral and nonlinear characterizations of achievable performance | Technical Report LIDS-P-2155, Laboratory for Information and Decision… | 2 |  |  | report |
| S605 |  | Velibor V | Misic (b) | 2 |  |  | other |
| S607 |  | The optimality of the GS> rule under quadratic holding costs, December 1999 | Private conversation | 2 |  |  | other |
| S614 | 2026 | Fifty years of Robust Linear and Convex Optimization | European Journal of Operational Research | 1 | 10.1016/j.ejor.2026.08.042 |  | journal |
| S615 | 2026 | Towards optimal valve prescription for transcatheter aortic valve replacement (TAVR) surgery: a machine learning approach | Health Care Management Science 29 (3), 27 | 1 | 10.1007/s10729-026-09768-4 | 2512.09198 | journal |
| S616 | 2026 | A Causal DAG Prior for Synthetic Time-Series Classification Datasets | arXiv preprint arXiv:2606.21776 | 1 |  | 2606.21776 | preprint |
| S617 | 2026 | Patient outcome predictions improve operations at Hartford HealthCare | INFORMS Journal on Applied Analytics 56 (3), 224-242 | 1 | 10.1287/inte.2024.0170 |  | journal |
| S618 | 2026 | Artificial Intelligence for Automated, Highly Accurate, and Scalable Multimodal EHR Data Abstraction | medRxiv, 2026.03. 16.26348522 | 1 | 10.64898/2026.03.16.26348522 |  | preprint |
| S619 | 2026 | When is More Better? Efficient and Adaptive Modality Acquisition in Multimodal Learning | Transactions on Machine Learning Research | 1 |  |  | journal |
| S620 | 2026 | Improving survival models in health care by balancing imbalanced cohorts: a novel approach | JCO clinical cancer informatics 10 (1), e2500190 | 1 | 10.1200/cci-25-00190 | 2510.02137 | journal |
| S621 | 2025 | Early Warning Index for Patient Deteriorations in Hospitals | arXiv preprint arXiv:2512.14683 | 1 |  | 2512.14683 | preprint |
| S622 | 2025 | Early detection of opioid over-procurement: A semisupervised machine learning approach | Manufacturing & Service Operations Management 27 (6), 1889-1904 | 1 | 10.1287/msom.2020.0369 |  | journal |
| S623 | 2025 | Overfitting in Adaptive Robust Optimization | arXiv preprint arXiv:2509.16451 | 1 |  | 2509.16451 | preprint |
| S624 | 2025 | Global nonconvex optimization with integer variables | arXiv preprint arXiv:2508.07018 | 1 |  | 2508.07018 | preprint |
| S626 | 2024 | Policy Trees for Prediction: Interpretable and Adaptive Model Selection for Machine Learning | arXiv preprint arXiv:2405.20486 | 1 |  | 2405.20486 | preprint |
| S627 | 2024 | A novel approach for a broad class of nonconvex optimization problems |  | 1 |  |  | other |
| S628 | 2023 | Hartford HealthCare improves hospital operations with patient outcome predictions | To be submitted | 1 |  |  | preprint |
| S629 | 2022 | Disease diagnosis using spectroscopy and machine learning | US Patent App. 17/368,803 | 1 |  |  | patent |
| S630 | 2022 | Sparsity in Machine Learning: Theory and Applications | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S631 | 2021 | ECHSA Presidential Address, CHSS-ECHSA Joint Meeting; Oct 24-25, 2020 | World Journal for Pediatric and Congenital Heart Surgery 12 (2), 164-167 | 1 |  |  | other |
| S632 | 2020 | Algorithmic advancements in discrete optimization: applications to machine learning and healthcare operations | Massachusetts Institute of Technology, Sloan School of Management�… | 1 |  |  | thesis |
| S633 | 2020 | Novel machine learning proves stroke risk is not linear | Stroke 51 (Suppl\_1), A153-A153 | 1 | 10.1161/str.51.suppl_1.153 |  | conference |
| S634 | 2020 | Prescriptive methods for adaptive learning | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S635 | 2020 | Dynamic optimization in the age of big data | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S636 | 2020 | Early Detection of Opioid Over-Procurement: A Machine Learning Approach |  | 1 |  |  | other |
| S637 | 2019 | Machine Learning and Optimization: Introduction to the Special Issue | Informs Journal on Optimization 1 (3), 185-186 | 1 | 10.1287/ijoo.2019.0024 |  | journal |
| S638 | 2019 | The edge of large-scale optimization in transportation and machine learning | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S641 | 2017 | A robust optimization approach to online problems | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S642 | 2017 | Combinatorial structures in online and convex optimization | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S643 | 2016 | Stochastic analysis via robust optimization | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S644 | 2016 | Moneyball for professors: models for predicting research impact | MIT Initiative on the Digital Economy 2016 (11) | 1 |  |  | report |
| S645 | 2015 | From data to decisions through new interfaces between optimization and statistics | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S651 | 2007 | Introduction to Queueing Systems, monograph in preparation |  | 1 |  |  | other |
| S652 | 2003 | Advances in airline revenue management and pricing | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S653 | 2002 | An Optimization Approach to Credit Risk | Work | 1 |  |  | report |
| S654 | 2000 | On the Relation Between Option and Stock Prices: A Convex Optimization Approach | WORKING PAPERS-INSEAD R AND D | 1 |  |  | report |
| S655 | 1999 | Relaxation and exact algorithms for solving mixed integer-quadratic optimization problems | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S656 | 1996 | Buffer overflow probabilities in multiclass ATM switches | PROCEEDINGS OF THE ANNUAL ALLERTON CONFERENCE ON COMMUNICATION CONTROL AND�… | 1 |  |  | conference |
| S657 | 1995 | RSS Research Workshop in Stochastic Networks | Edinburgh, August | 1 |  |  | talk |
| S658 | 1995 | Nonlinear formulations and improved randomized approximation algorithms for multiway and multicut problems | Sloan School of Management, Massachusetts Institute of Technology\] | 1 |  |  | report |
| S659 | 1993 | Decomposition algorithms for analyzing transient phenomena in multi-class queuing networks in air transportation | Cambridge, Mass.: Alfred P. Sloan School of Management, Massachusetts�… | 1 |  |  | report |
| S662 | 1991 | Stochastic and dynamic vehicle routing in Euclidean service regions | Massachusetts Institute of Technology | 1 |  |  | thesis |
| S663 | 1990 | On the characteristic equation of general queueing systems | Massachusetts Institute of Technology, Operations Research Center | 1 |  |  | report |
| S664 | 1989 | Transient and busy period analysis of the GI/G/1 queue: Part II, solution as a Hilbert problem | Cambridge, Mass.: Center for Computational Research in Economics and�… | 1 |  |  | report |
| S665 |  | Sloan School of Management | Massachusetts Institute of Technology 50 | 1 |  |  | other |
| S666 | 2026 | Online LLM Personalization from Pairwise Preferences Across Users | arXiv preprint arXiv:2610.17203 |  |  | 2610.17203 | preprint |
| S667 | 2026 | Bespoke: Generating MOOC-Quality Industry-Personalized Lecture Videos at Scale | arXiv preprint arXiv:2609.26540 |  |  | 2609.26540 | preprint |
| S668 | 2026 | Rapid drone-based wildfire detection at a fraction of current prevention spending | arXiv preprint arXiv:2609.18556 |  |  | 2609.18556 | preprint |
| S669 | 2026 | Catastrophe Insurance Pricing: An Adaptive Robust Optimization Approach | Variance 19 |  | 10.66573/001c.167995 | 2405.07068 | journal |
| S670 | 2026 | Identifying subsets of patients with retroperitoneal sarcoma who benefit from radiotherapy: an Interpretable AI reanalysis of the STRASS randomised trial | The Lancet Digital Health 8 (8) |  | 10.1016/j.landig.2026.101021 |  | journal |
| S671 | 2026 | Report to the President for year ended June 30, 2026, MIT Open Learning |  |  |  |  | report |
| S672 | 2026 | Robust Optimization for Green Ammonia Production | arXiv preprint arXiv:2606.08335 |  |  | 2606.08335 | preprint |
| S675 | 2026 | Lung Allocation Policy Optimization to Equalize Transplant Access Across Blood Types | American Journal of Transplantation 26 (7), S1028 |  | 10.1016/j.ajt.2026.05.2240 |  | conference |
| S676 | 2026 | A Unified, Fast, and Transparent System for Designing Organ Allocation Policies | American Journal of Transplantation 26 (7), S257 |  | 10.1016/j.ajt.2026.05.216 |  | conference |
| S677 | 2026 | Empowering Health in Aging Populations: A Multimodal Vulnerability Tool for Frail Patients | Machine Learning for Health 2025 |  |  |  | conference |
| S678 | 2026 | A Multimodal and Explainable Machine Learning Approach to Diagnosing Multi-Class Ejection Fraction from Electrocardiograms | arXiv preprint arXiv:2604.25942 |  |  | 2604.25942 | preprint |
| S679 | 2026 | Robustifying and Selecting Cohort-Appropriate Prognostic Models under Distributional Shifts | arXiv preprint arXiv:2604.16537 |  |  | 2604.16537 | preprint |
| S680 | 2026 | Observing the unobserved confounding through its effects: toward randomized trial-like estimates from real-world survival data | arXiv preprint arXiv:2604.12137 |  |  | 2604.12137 | preprint |
| S681 | 2026 | Optimal Control of Fluid Restless Multi-armed Bandits: A Machine Learning Approach | Machine Learning 115 (3), 70 |  | 10.1007/s10994-026-07022-0 | 2502.03725 | journal |
| S682 | 2025 | An Interpretable AI Tool for SAVR vs TAVR in Low to Intermediate Risk Patients with Severe Aortic Stenosis | arXiv preprint arXiv:2512.10308 |  |  | 2512.10308 | preprint |
| S683 | 2025 | Detection and Localization of Subdural Hematoma Using Deep Learning on Computed Tomography | arXiv preprint arXiv:2512.09393 |  |  | 2512.09393 | preprint |
| S684 | 2025 | Sparse Multiple Kernel Learning: Alternating Best Response and Semidefinite Relaxations | arXiv preprint arXiv:2511.21890 |  |  | 2511.21890 | journal |
| S685 | 2025 | Can artificial intelligence deliver on the promise of precision medicine? | Hepatobiliary Surgery and Nutrition 14 (5), 847 |  | 10.21037/hbsn-2025-455 |  | journal |
| S686 | 2025 | Can Artificial Intelligence Improve the Appropriate Use and Decrease the Misuse of REBOA? | Bioengineering 12 (10), 1025 |  | 10.3390/bioengineering12101025 |  | journal |
| S688 | 2025 | Prescribe-then-Select: Adaptive Policy Selection for Contextual Stochastic Optimization | Transactions on Machine Learning Research |  |  | 2509.08194 | journal |
| S689 | 2025 | A novel exact approach to polynomial optimization | arXiv preprint arXiv:2507.02120 |  |  | 2507.02120 | preprint |
| S690 | 2025 | Report to the President for year ended June 30, 2025, Open Learning |  |  |  |  | report |
| S691 | 2025 | Mark Francis Magazu | Massachusetts Institute of Technology |  |  |  | other |
| S692 | 2025 | Interpretable AI-driven Guidelines for Type 2 Diabetes Treatment from Observational Data | arXiv preprint arXiv:2504.12417 |  |  | 2504.12417 | preprint |
| S694 | 2025 | A Unified Adaptive Robust Optimization Approach to Electricity Markets Under Uncertainty | Massachusetts Institute of Technology |  |  |  | thesis |
| S695 | 2025 | The Analytics Edge in Healthcare | Dynamic Ideas |  |  |  | book |
| S696 | 2024 | Improving survival models in healthcare: a novel matching approach | Research Square, rs. 3. rs-5467577 |  | 10.21203/rs.3.rs-5467577/v1 |  | preprint |
| S697 | 2024 | Investigating hidden influences on treatment for gastrointestinal stromal tumours with AI: diet, chronic conditions, and mental health–Authors' reply | The Lancet Oncology 25 (10), e470 |  |  |  | journal |
| S698 | 2024 | Convex Hull Pricing in Electricity Markets: Evidence from a Large US Market | 2024 INFORMS Optimization Society (IOS) |  |  |  | talk |
| S699 | 2024 | Predictive and Prescriptive Trees for Optimization and Control Problems | Massachusetts Institute of Technology |  |  |  | thesis |
| S700 | 2024 | Advances in Sparse and Low Rank Matrix Optimization for Machine Learning Applications | Massachusetts Institute of Technology |  |  |  | thesis |
| S701 | 2024 | A Simulated Annealing Approach to Designing Optimal Decision Trees for Classification, Prescriptive, and Survival Analysis | Massachusetts Institute of Technology |  |  |  | thesis |
| S702 | 2024 | Integrating Optimization and Modern Machine Learning: Theory, Computation, and Healthcare Applications | Massachusetts Institute of Technology |  |  |  | thesis |
| S703 | 2024 | Multimodal Machine Learning for Climate Adaptation | Massachusetts Institute of Technology |  |  |  | thesis |
| S704 | 2023 | Powerful New Methods and Tools for Designing Allocation Policy for Deceased-Donor Organs | AMERICAN JOURNAL OF TRANSPLANTATION 23 (6), S474-S474 |  |  |  | conference |
| S706 | 2023 | Evaluation of individual and ensemble probabilistic forecasts of COVID-19 mortality in the United States (vol 119, e2113561119, 2022) | PROCEEDINGS OF THE NATIONAL ACADEMY OF SCIENCES OF THE UNITED STATES OF�… |  |  |  | errata |
| S707 | 2023 | Renalase Identified by Machine Learning Methods As A Novel Independent Predictor Of Mortality In Hospitalized Patients With COVID-19 |  |  | 10.21203/rs.3.rs-2492699/v1 |  | preprint |
| S708 | 2023 | Reformulation-Perspectification Technique for nonconvex optimization problems | Optimization Online |  |  |  | preprint |
| S709 | 2023 | Harnessing External Data in Public and Private Market Investing | Massachusetts Institute of Technology |  |  |  | thesis |
| S710 | 2023 | Analytics under Variability, Volume, and Velocity with Applications to Sustainability and Healthcare | Massachusetts Institute of Technology |  |  |  | thesis |
| S711 | 2022 | Integer and Matrix Optimization: A Nonlinear Approach | Massachusetts Institute of Technology |  |  |  | thesis |
| S712 | 2022 | Algorithms for Large-scale Data Analytics and Applications to the COVID-19 Pandemic | Massachusetts Institute of Technology |  |  |  | thesis |
| S713 | 2022 | Machine Learning Algorithms and Applications in Health Care | Massachusetts Institute of Technology |  |  |  | thesis |
| S714 | 2022 | Stable Machine Learning | Massachusetts Institute of Technology |  |  |  | thesis |
| S715 | 2021 | Improving Efficiency and Fairness in Machine Learning: a Discrete Optimization Approach | Massachusetts Institute of Technology |  |  |  | thesis |
| S716 | 2021 | Novel Machine Learning Algorithms for Personalized Medicine and Insurance | Massachusetts Institute of Technology |  |  |  | thesis |
| S717 | 2020 | Development of a Multivariable Proxy Model for Six-Minute Walk Distance (6MWD) in Duchenne Muscular Dystrophy (DMD) Using Machine Learning Methods (682) | Neurology 94 (15_supplement), 682 |  | 10.1212/wnl.94.15_supplement.682 |  | conference |
| S718 | 2019 | A Unified Approach to Mixed-Integer Optimization: Nonlinear Formulations and Scalable Algorithms |  |  |  | 1907.02109 | preprint |
| S719 | 2019 | Introduction to the Issue | INFORMS Journal on Optimization 1 (4), 265-266 |  | 10.1287/ijoo.2019.0028 |  | journal |
| S720 | 2019 | Report to the President for year ended June 30, 2019, Operations Research Center |  |  |  |  | report |
| S721 | 2019 | Integrated robust and adaptive methods in the heating oil industry | Massachusetts Institute of Technology |  |  |  | thesis |
| S722 | 2019 | Advances in data-driven models for transportation | Massachusetts Institute of Technology |  |  |  | thesis |
| S723 | 2019 | The Rise and Fall of MELD: Are We Ready for an Optimized Prediction of Mortality (OPOM) for Liver Transplant Allocation? | AMERICAN JOURNAL OF TRANSPLANTATION 19, 15-16 |  |  |  | conference |
| S724 | 2018 | Personalized Treatment for Coronary Artery Disease: A Machine Learning Approach | Circulation 138 (Suppl_1), A11213-A11213 |  |  |  | conference |
| S725 | 2018 | A scalable algorithm for sparse and robust portfolios |  |  |  |  | other |
| S726 | 2018 | Report to the President for year ended June 30, 2018, Dean, Operations Research Center |  |  |  |  | report |
| S727 | 2018 | Abstract P3-15-03: Clinical benefit, toxicity, and cost of metastatic breast cancer drug therapies: Visualizing randomized and non-randomized evidence | Cancer Research 78 (4_Supplement), P3-15-03-P3-15-03 |  | 10.1158/1538-7445.sabcs17-p3-15-03 |  | conference |
| S730 | 2018 | New algorithms in machine learning with applications in personalized medicine | Massachusetts Institute of Technology |  |  |  | thesis |
| S732 | 2017 | Report to the President for year ended June 30, 2017, Operations Research Center |  |  |  |  | report |
| S736 | 2017 | An analytics approach to problems in health care | Massachusetts Institute of Technology |  |  |  | thesis |
| S737 | 2017 | From data to decisions in healthcare: an optimization perspective | Massachusetts Institute of Technology |  |  |  | thesis |
| S738 | 2016 | Continuous Optimization: Challenges and Applications |  |  |  |  | other |
| S739 | 2016 | Report to the President for year ended June 30, 2016, Operations Research Center |  |  |  |  | report |
| S740 | 2016 | Computational management science special issue on “Robust Optimization and Applications” | Computational Management Science 13 (2), 147-149 |  |  |  | other |
| S741 | 2016 | THE ANALYTICS EDGE | Mathematics and Computer Education 50 (2), 139 |  |  |  | review |
| S743 | 2016 | Supply chain network strategy for consumer medical device introduction | Massachusetts Institute of Technology |  |  |  | thesis |
| S745 | 2015 | Channel Coding via Robust Optimization Part 2: The Multi-User Channel |  |  |  |  | other |
| S746 | 2015 | Report to the President for year ended June 30, 2015, Dean, Operations Research Center |  |  |  |  | report |
| S747 | 2015 | Note on the Reformulation for Static Robust Problems for Convex Uncertainty Sets | Rn 500, 1 |  |  |  | other |
| S749 | 2015 | Multivariate Statistics and Machine Learning Under a Modern Optimization Lens | Georgia Institute of Technology |  |  |  | talk |
| S753 | 2015 | Recensione dell'articolo:(Bertimas, Dimitris; Nasrabadi, Ebrahim; Paschalidis, Ioannis-" Robust fluid processing networks."-IEEE Trans. Automat. Control 60 (2015), no. 3, 715�… |  |  |  |  | review |
| S754 | 2014 | Report to the President for year ended June 30, 2014, Operations Research Center |  |  |  |  | report |
| S761 | 2013 | Report to the President for year ended June 30, 2013, Operations Research Center |  |  |  |  | report |
| S763 | 2012 | SHB: Type II (INT): Collaborative Research: Algorithmic Approaches to Personalized Health Care | NSF Award Number 1237136. Directorate for Computer and Information Science�… |  |  |  | other |
| S764 | 2012 | Report to the President for year ended June 30, 2012, Operations Research Center |  |  |  |  | report |
| S765 | 2011 | OPERA TIONS RESEARCH CENTER | Journal of Machine Learning Research |  |  |  | other |
| S766 | 2011 | Report to the President for year ended June 30, 2011, Operations Research Center |  |  |  |  | report |
| S770 | 2010 | Fairness and Optimality in Trading | Massachusetts Institute of Technology |  |  |  | thesis |
| S771 | 2010 | Algebraic, Geometric, and Combinatorial Methods for Optimization |  |  |  |  | other |
| S772 | 2010 | Report to the President for year ended June 30, 2010, Operations Research Center |  |  |  |  | report |
| S777 | 2009 | Report to the President for year ended June 30, 2009, Operations Research Center |  |  |  |  | report |
| S778 | 2009 | Robust optimization in high dimensions | Optimal Device Design, 149-188 |  | 10.1017/cbo9780511691881.007 |  | chapter |
| S779 | 2008 | Report to the President for year ended June 30, 2008, Operations Research Center |  |  |  |  | report |
| S780 | 2008 | Algorithmic issues in queueing systems and combinatorial counting problems | Massachusetts Institute of Technology |  |  |  | thesis |
| S782 | 2008 | Analysis of employee stock options and guaranteed withdrawal benefits for life | Massachusetts Institute of Technology |  |  |  | thesis |
| S783 | 2007 | 2007 Index IEEE Transactions on Automatic Control Vol. 52 | IEEE Transactions on Automatic Control 52 (12), 2397 |  |  |  | other |
| S784 | 2007 | EFRI-ARESCI: Theory and Algorithms for Autonomous Reconfigurability of the National Air Transportation System | NSF Award 7 (735905), 35905 |  |  |  | other |
| S785 | 2007 | Bounds on some contingent claims with non-convex payoff based on multiple assets |  |  |  |  | other |
| S786 | 2007 | Report to the President for year ended June 30, 2007, Operations Research Center |  |  |  |  | report |
| S787 | 2007 | Robust Optimization of Aperiodic Photonic Structures | APS March Meeting Abstracts, S43. 011 |  |  |  | talk |
| S788 | 2007 | Lutowanie próżniowe element�w węglikowych ze stalą nierdzewną za pomocą lutu miedziano-manganowego | Przegląd Spawalnictwa 79, 138-141 |  |  |  | other |
| S789 | 2005 | The Value of Adaptability | Proceedings 43, 630 |  |  |  | conference |
| S791 | 2004 | The issue number is given in front of the page numbers | Operations Research Letters 32, 595-599 |  |  |  | other |
| S792 | 2004 | 15.083 J/6.859 Integer Programming and Combinatorial Optimization, Fall 2004 |  |  |  |  | other |
| S793 | 2004 | 15.093/2.098 Optimization Methods (SMA 5213), Fall 2004 |  |  |  |  | other |
| S794 | 2003 | UNILEVER DATA ANALYSIS PROJECT |  |  |  |  | other |
| S795 | 2003 | Dynamic Optimization for Adaptive Customized Marketing | Massachusetts Institute of Technology, Sloan School of Management�… |  |  |  | thesis |
| S796 | 2003 | Fluid Models for Parallel Processor Allocation | Computational Modeling and Problem Solving in the Networked World�… |  | 10.1007/978-1-4615-1043-7_14 |  | chapter |
| S797 | 2002 | 15.060 Data, Models, and Decisions, Fall 2002 |  |  |  |  | other |
| S798 | 1999 | An asymptotically optimal algorithm for job shop scheduling | Proceedings of the 38th IEEE Conference on Decision and Control (Cat. No�… |  | 10.1109/cdc.1999.832823 |  | conference |
| S800 | 1998 | BOOK NOTICES1 | Journal of Optimization Theory and Applications 96 (3), 723 |  |  |  | review |
| S802 | 1997 | PRICING AND HEDGING DERIVATIVE SECURITIES IN INCOMPLETE MARKETS: AN 6-ARBITRAGE APPROACH |  |  | 10.3386/w6250 |  | report |
| S804 | 1997 | Optimization of Multiclass Queueing Networks | NSF Award Number 9610486. Directorate for Engineering 96 (9610486), 10486 |  |  |  | other |
| S805 | 1997 | Sarah Stock Patterson | Massachusetts Institute of Technology |  |  |  | other |
| S806 | 1997 | Decentralized and Tactical Air Traffic Flow Management | NASA Contractor Report, 27689 |  |  |  | report |
| S807 | 1996 | Large deviations in high speed communication networks | Massachusetts Institute of Technology |  |  |  | other |
| S809 | 1994 | The flow management problem in air traffic control | Univ. of Michigan, Ann Arbor, MI (United States) |  |  |  | other |
| S810 | 1994 | From valid inequalities to heuristics: A unified view of primal-dual methods in approximation algorithms | Univ. of Michigan, Ann Arbor, MI (United States) |  |  |  | other |
| S816 | 1994 | TSS Dissertation Abstracts—Abstracts for the 1993 Transportation Science Section Dissertation Prize Competition | Transportation Science 28 (1), 82-89 |  | 10.1287/trsc.28.1.82 |  | other |
| S818 | 1994 | The following is a list of individuals who served as referees for papers reviewed between March 1, 1993 and June 10, 1994. | Mathematical Programming 64, 371-373 |  |  |  | other |
| S819 | 1994 | On the large deviations behaviour of acyclic networks of GIGII queues | LIDS Report: LIDS-P-2278 |  |  |  | report |
| S821 | 1993 | Location and inventory optimization for service centers | Massachusetts Institute of Technology |  |  |  | thesis |
| S823 | 1992 | Date of Birth: October 3, 1962 Place of birth: Greece Citizenship: US Personal: Married | Stanford University |  |  |  | other |
| S825 | 1992 | The following is a list of individuals who served as referees for papers in review during the period from July 1, 1989… | Mathematical Programming 55, 125-128 |  |  |  | other |
| S826 | 1992 | Models and algorithms for transient queueing congestion at a hub airport | Massachusetts Institute of Technology, Operations Research Center |  |  |  | report |
| S827 | 1991 | Presidential Young Investigator Award: Analysis of Stochastic in Dynamic Models in Combinatorial Optimization in Queueing Networks | NSF Award Number 9158118. Directorate for Engineering 91 (9158118), 58118 |  |  |  | other |
| S829 | 1991 | A central limit theorem for the exodic tree and exodic matching in geometrical probability | Alfred p. Sloan School of Management, Massachusetts Institute of Technology |  |  |  | report |
| S830 | 1990 | Probabilistic and Dynamic Combinatorial Optimization Problems | NSF Award 90 (9014751), 14751 |  |  |  | other |
| S831 | 1990 | Research Initiation: Analysis of Linear Programming Relaxations of Combinatorial Optimization Problems | NSF Award Number 9010322. Directorate for Engineering 90 (9010322), 10322 |  |  |  | other |
| S832 | 1990 | The greedy algorithm in combinatorial optimization and its probabilistic analysis | Unpublished manuscript |  |  |  | preprint |
| S833 | 1988 | The Probabilistic Minimum Spanning Tree, Part II: Probabilistic Analysis and Asymptotic Results | Massachusetts Institute of Technology, Operations Research Center |  |  |  | report |
| S834 | 1953 | PRINCIPAL FIELDS OF INTEREST |  |  |  |  | other |
| S835 |  | Optimization-Based Design of Organ Allocation Policy: Mitigating Biological Access Disparities in Lung Transplantation |  |  |  |  | other |
| S836 |  | Signed Budget Uncertainty for Robust Mixed-Integer Optimization |  |  |  |  | other |
| S838 |  | \_? \_I\_? \_ I\_ IL \_YI? Lg\_YLLIILLL\_.-. lly? l-IP~ L---Y~----IC--\_ \_ I\_ \_ \_ |  |  |  |  | other |
| S840 |  | MIT Libraries logo DSpace@ MIT |  |  |  |  | other |
| S841 |  | Stability conditions for multiclass fluid queueing networks D. Bertsimas, D. Gamarnik and J. Tsitsiklis… |  |  |  |  | report |
| S844 |  | SUBMITTED TO THE SLOAN SCHOOL OF MANAGEMENT IN PARTIAL FULFILLMENT OF THE REQUIREMENTS OF THE DEGREE OF |  |  |  |  | other |
| S849 |  | OF TECHNOLOGY SEP 2 6 2013 LIBRARIES 2 Robust Planning for Unmanned Underwater Vehicles |  |  |  |  | other |
| S852 |  | Cambridge, MA 02139, USA Michael Lingzhi Li mlli@ mit. edu Operations Research Center Massachusetts Institute… |  |  |  |  | other |
| S855 |  | SUBMITTED TO THE SLOAN SCHOOL OF MANAGEMENT IN PARTIAL FULFILLMENT OF THE REQUIREMENTS OF THE DEGREE OF |  |  |  |  | other |
| S858 |  | A Robust Optimization Approach to Supply Chains and Revenue Management |  |  |  |  | other |
| S860 |  | OPERATIONS RESEARCH INFORMS |  |  |  |  | other |
| S861 |  | The Achievable Region Method in the Optimal Control of Queueing Systems; Formulations, Bounds and Policies Dimitris Bertsimas OR 310-95 June 1995 |  |  |  |  | report |
| S863 |  | Cambridge, MA 02139, USA Ivan Paskov ipaskov@ mit. edu Operations Research Center Massachusetts Institute of Technology… |  |  |  |  | other |
| S866 |  | Ying Daisy Zhuo zhuo@ mit. edu Sloan School of Management and Operations Research Center Massachusetts Institute of Technology… |  |  |  |  | other |
| S867 |  | Distributionally Robust Optimization with General Uncertainty Structure |  |  |  |  | other |
| S869 |  | Policy Trees for Prediction: Interpretable and Adaptive Model Selection for Machine Learning | NeurIPS 2024 Workshop on Regulatable ML |  |  |  | conference |
| S872 |  | Predicting Concurrence of Heatwaves, Droughts, and Wildfires with Spatiotemporal Deep Learning |  |  |  |  | other |
| S873 |  | Optimized Oversampling |  |  |  |  | other |
| S874 |  | Informing national immigration policy through interpretable machine learning |  |  |  |  | other |
| S881 |  | A practicable framework for distributionally robust linear optimization, 2014. Optimization Online www. optimization-online. org | DB FILE/2013/07/3954. html |  |  |  | preprint |
| S884 |  | Fast and Scalable Inference of Dynamical Systems via Integral Matching | NeurIPS 2023 AI for Science Workshop |  |  |  | conference |
| S896 | 1993 | Conservation laws, extended polymatroids and multi-armed bandit problems: a unified approach to ind exable systems | Proceedings of the 3rd IPCO Conference, 355-384 |  |  |  | conference |
| S899 |  | Dimitris Bertsimas |  |  |  |  | other |
| S900 |  | Dimitris Bertsimas, Vishal Gupta & |  |  |  |  | other |
| S901 |  | Secondary Logo Journal Logo |  |  |  |  | other |
| S902 |  | Hirshleifer, Jack Anticipatory Savings Denizer, Cevdet Anxiety Grant, Simon |  |  |  |  | other |
| S905 |  | Imbalanced classification via robust optimization |  |  |  |  | other |
| S906 |  | The Power and Limits of Decision Making with Confounded Data: The Case of Pricing |  |  |  |  | other |
| S907 |  | Multiperiod and Online Optimization for Fleet Defense: Centralized and Distributed Approaches |  |  |  |  | other |
| S908 |  | Optimal Predictive Clustering |  |  |  |  | other |
| S909 |  | Optimal Selection of Health Care Providers |  |  |  |  | other |
| S910 |  | THE ANNALS |  |  |  |  | other |
| S911 |  | Shock Capturing with Discontinuous Galerkin Method |  |  |  |  | other |
| S912 |  | 6.436 J/15.085 J Fundamentals of Probability, Fall 2008 |  |  |  |  | other |
| S914 |  | A General Purpose Local Search Algorithm for Binary Optimization |  |  |  |  | other |
| S916 |  | New Books Raymond Yeung Introduction to Linear Optimization |  |  |  |  | review |
| S917 |  | THE ANNALS |  |  |  |  | other |
| S918 |  | Lead Time Distribution of Three-Machine Two-Buffer Lines with Unreliable Machines and Finite Buffers |  |  |  |  | other |
| S920 |  | of days)• H. Bidkhori, S. Kim, On dual stable Grothendieck polynomials, Preprinted, 2009.• H. Bidkhori, S… |  |  |  |  | other |
| S921 |  | Models and algorithms for transient queueing congestion in airline hub and spoke networks. |  |  |  |  | other |
| S923 |  | The Editorial Board would like to thank the following individuals who acted as referees for papers considered… |  |  |  |  | other |
| S925 |  | LIDS Publication# 2658 Constrained Stochastic LQC: A Tractable Approach |  |  |  |  | report |
| S926 |  | LIDS Publication# 2659 Robust linear optimization and coherent risk measures |  |  |  |  | report |
| S928 |  | Trading off Efficiency and Fairness |  |  |  |  | other |
| S929 |  | Basestock Policies in Supply Chain Networks: Robust vs. Stochastic Optimization |  |  |  |  | other |
| S930 |  | INVESTIGACI�N OPERATIVA OBSERVACIONES |  |  |  |  | other |
| D001 | 1990 | On the Parsimonious Property of Connectivity Problems | SODA, 388-396 |  |  |  | conference |
| D002 | 1992 | A Technique for Speeding up the Solution of the Lagrangian Dual | IPCO, 435-452 |  |  |  | conference |
| D003 | 1995 | From Valid Inequalities to Heuristics: A Unified View of Primal-Dual Approximation Algorithms in Covering Problems | SODA, 102-111 |  |  |  | conference |
| D004 | 1996 | On Dependent Randomized Rounding Algorithms | IPCO, 330-344 |  | 10.1007/3-540-61310-2_25 |  | conference |
| D005 | 1997 | Correction to "Stability Conditions for Multiclass Fluid Queueing Networks" | IEEE Trans. Autom. Control. 42(1), 128 |  | 10.1109/tac.1997.553697 |  | errata |
| D006 | 1999 | Estimation of Time-Varying Parameters in Statistical Models: An Optimization Approach | Mach. Learn. 35(3), 225-245 |  | 10.1023/a:1007586831473 |  | journal |
| D007 | 1999 | Performance analysis of multiclass queueing networks | SIGMETRICS Perform. Evaluation Rev. 27(3), 11-14 |  | 10.1145/340242.340299 |  | journal |
| D008 | 2000 | Performance of multiclass Markovian queueing networks | CDC, 534-539 |  | 10.1109/cdc.2000.912819 |  | conference |
| D009 | 2002 | Solving convex programs by random walks | STOC, 109-115 |  | 10.1145/509907.509926 |  | conference |
| D010 | 2009 | Optimality of affine policies in multi-stage robust optimization | CDC, 1131-1138 |  | 10.1109/cdc.2009.5399533 |  | conference |
| D011 | 2012 | Call for Papers - Special Issue of Management Science: Business Analytics: Submission deadline: September 16, 2012 Expected publication date: First Quarter 2014 | Manag. Sci. 58(7), 1422 |  | 10.1287/mnsc.1120.1596 |  | journal |
| D012 | 2013 | Network Analysis for Predicting Academic Impact | ICIS |  |  |  | conference |
| D013 | 2018 | lauren897/Optimal-SPCA: Initial Release |  |  | 10.5281/zenodo.2025842 |  | other |
| D015 | 2019 | From the Editor | INFORMS J. Optim. 1(1), 1 |  | 10.1287/ijoo.2019.0011 |  | journal |
| D016 | 2019 | Machine Learning and Optimization: Introduction to the Special Issue | INFORMS J. Optim. 1(2), 91 |  | 10.1287/ijoo.2019.0017 |  | journal |
| D017 | 2019 | Optimal Explanations of Linear Models | CoRR abs/1907.04669 |  |  | 1907.04669 | preprint |
| D018 | 2022 | Frequency Estimation in Data Streams: Learning the Optimal Hashing Scheme (Extended Abstract) | ICDE, 1565-1566 |  | 10.1109/icde53745.2022.00159 |  | conference |
| D019 | 2023 | Publisher Correction to: A new perspective on low-rank optimization | Math. Program. 202(1), 93-94 |  | 10.1007/s10107-023-01947-3 |  | errata |
| D020 | 2023 | Tensor completion with noisy side information | Mach. Learn. 112(10), 3945-3976 |  | 10.1007/s10994-023-06338-5 |  | journal |
| D021 | 2025 | An Exact Solution to Wordle | Oper. Res. 73(3), 1384-1394 |  | 10.1287/opre.2022.0434 |  | journal |
| D022 | 2026 | Strike Price Optimization for ISO New England's Day-Ahead Ancillary Services | arXiv preprint arXiv:2608.29366 |  |  | 2608.29366 | preprint |
| H001 | 2023 | Adaptive Linear Algebra |  |  |  |  | other |
| H002 | 2023 | A Simulated Annealing Approach to Designing Optimal Policy Trees | submitted to Machine Learning |  |  |  | preprint |
| H003 | 2023 | Interpretable Prescriptive Neural Networks | submitted to Machine Learning |  |  |  | preprint |
| H004 | 2023 | Probabilistic Robust Optimization | submitted to Operations Research |  |  |  | preprint |
| H005 | 2022 | Optimal policy trees | Machine Learning, 111, 2741–2768 |  |  |  | journal |
| H006 | 2021 | Interpretable Machine Learning for Policy Analysis: The Case of National Immigration Policy | submitted to MSOM |  |  |  | preprint |
| H007 | 2021 | Robust Optimization with Side Data | submitted to Mathematical Programming |  |  |  | preprint |
| H008 | 2019 | Prescriptive Analytics for Observational Data | submitted to Management Science |  |  |  | preprint |
| H009 | 2018 | Optimal classification and regression trees with hyperplanes are as powerful as classification and regression neural networks | submitted to Journal of Machine Learning Research |  |  |  | preprint |
| H010 | 1999 | Optimization of multiclass queueing networks with changeover times via the achievable region approach: Part II, the multi-station case | Mathematics of Operations Research |  | 10.1287/moor.24.2.331 |  | journal |
| H011 | 2004 | Optimal mean-variance bounds on the expectation of the highest order statistics |  |  |  |  | preprint |
