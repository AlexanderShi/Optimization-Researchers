# Matteo Fischetti — publication list (Google Scholar primary)

Audited 2026-11-26: an independent year-sorted pass over the profile (198 rows: cstart=0, 50 and 100 with 50 rows each, cstart=150 with 48, cstart=200 empty; every page's JSON-line count equals its TOTAL line, so no range was re-read at pagesize 20) matched every row one-to-one to an S record (difflib ratio 1.000 on normalised titles except S033, S035, S070, S083 and S188, where one side carries replacement characters or italics markup; all 198 years agree with the stored ones), so no row was missing and nothing was added. Identifiers were checked in full, not sampled: all 153 DOIs resolve at doi.org (302) and match their Crossref (149) or DataCite (4) titles with Fischetti among the authors or editors (ratio 1.000 except S145 at 0.844, whose Crossref title adds 'Chapter 5:', D004 at 0.968, whose DataCite title adds the paper number, and S122 at 0.986, whose Crossref title runs words together); the 18 other distinct doi.org links in `urls` (10 arXiv, 7 Zenodo, 1 Dagstuhl volume DOI) resolve as well; all 10 arXiv ids open on arxiv.org with matching titles and Fischetti among the authors (2112.02195 under its v1 title; v2 is retitled 'Revisiting local branching with a machine learning lens'), and the arxiv.org author search 'Fischetti, Matteo' returns exactly these 10. No identifier was wrong, so none was nulled. A fresh DBLP SPARQL pull (pid 47/4770, 146 records) maps every record to a row here, a fresh https fetch of the homepage maps all 143 list entries ([1]–[142] and [124bis]) and its 9 technical reports to rows here, and a Crossref title query for the 39 distinct works without DOI or arXiv id found no DOI to add. Corrected where two or more independent sources agree against Scholar (the evidence is in each row's `note`): years of S011 2016→2017, S040 2014→2017, S103 2022→2023, S107 1996→1997, S110 2019→2021 and S123 2014→2016 (Crossref and/or DBLP with the homepage list; for S107 DBLP, the homepage and Springer's dc.source and copyright line, against a July 1996 issue date that is out of order with Mathematical Programming 74(3) of September 1996), S037 2010→2011 and S151 2023→2025 (Crossref and the homepage), S047 and S056 2007→2002 (the homepage and Springer's page for the book: hardcover published 31 May 2002, so 2007 is the softcover date that Crossref and Scholar carry); venues of S038 (issue 31(3)→31(2): Crossref, DBLP, homepage), S103 (completed to 69(4), 2147-2164) and S151 (the published AIRO Springer Series 14 volume instead of the workshop name), and the year inside the venue string of S011, S047, S056 and S107. Also changed: S188's title (accented letters as this pass shows them, instead of replacement characters), S186's year (2026, from DataCite) and H003 (a scb.se PDF link found by web search added to `urls`; its note records that the Padua Research Archive gives Journal of Official Statistics 14, 553-566, 1998 against the homepage's '17, 4, 101-113', a venue left as printed because only one source read here disagrees). Kept, with the evidence in the notes: S096 (2009: Crossref, homepage; DBLP alone 2010), S102 (2002: homepage, Springer's book page) and S126 (2025: Crossref issue, DBLP; homepage 2024).

Harvested 2026-11-26 from the Google Scholar profile https://scholar.google.com/citations?user=5rOdaqAAAAAJ&hl=en, cross-checked against DBLP (pid 47/4770, https://dblp.org/pid/47/4770.html, read through the DBLP SPARQL endpoint), Crossref, DataCite (Dagstuhl and Zenodo DOIs), arXiv (the arxiv.org author search 'Fischetti, Matteo', 10 results) and the homepage http://www.dei.unipd.it/~fisch/ (publication list [1]–[142] plus [124bis], 9 technical reports, and the author PDFs in https://www.dei.unipd.it/~fisch/papers/). The Scholar author-search page redirected to a Google login, so the profile id was taken from the Scholar link that DBLP registers for pid 47/4770; the homepage links the same profile.

Counts: 198 Scholar rows, read from 4 pages of 50 (cstart=0, 50, 100, 150 with 50, 50, 50 and 48 rows; cstart=200 returned no rows), 5 fetches in all; every page's JSON-line count equals its TOTAL line, so no range was re-read at pagesize 20. 19 DBLP-only items (D001–D019: conference and workshop versions of journal rows, journal papers and a 2018 handbook chapter missing from the profile, two arXiv preprints, an ATMOS abstracts collection) and 5 homepage-only items (H001–H005). All 146 DBLP records map to a record here (merged into a Scholar row or added as a D item); all 152 homepage entries map to a record here. 21 rows are marked as duplicates or junk (`dup_of`), leaving 201 distinct works listed below; 153 of them have a DOI and 10 an arXiv id, and 82 have an author PDF from the homepage papers directory in `urls` (attached by file name). DBLP pid 47/4770.

Kinds among listed works: journal 118, conference 31, chapter 17, preprint 11, other 11, report 5, book 4, talk 3, thesis 1. Not identified anywhere but Scholar (kept, with a note): S154, S188, S189, S190, S192, S194, S196, S198; S188 is a Spanish-language item credited to P Toth and M Fischetti that may not be his own work. Talk or slide records: S146, S155, S193. Software and data: S186 (Zenodo replication package); S187 is a technical note whose Zenodo record has a different title (no DOI set).

The harvest left the years of S011, S040, S103, S107, S110, S123, S037, S151, S047, S056, S102, S096 and S126 and the issue of S038 to the audit; they are settled in the audit paragraph above. Repaired in the harvest from the fetch with evidence: S070 title (Crossref: {0, ½}), S083 title and authors (DBLP accents), author accents of S005, S073, S093, S114, S127, S135, S136; a stray replacement character before the ellipsis in the venues of S010, S037, S053. Venues filled where Scholar shows none: S040, S123 (DBLP), S110 (DBLP and homepage), S145 (Crossref and homepage). Crossref DOIs accepted outside the year-within-1 rule, with the reason in the note: S102 (same book and pages as S047/S056; Crossref's 2007 is the softcover date) and S151 (DOI printed on the homepage; its year is now Crossref's 2025); S145's Crossref title carries a 'Chapter 5:' label.

Profile identity: Matteo Fischetti, University of Padova; verified email at unipd.it; homepage http://www.dei.unipd.it/~fisch; interests: Discrete Optimization, Operations Research, Integer Programming, Mathematical Optimization (20127 citations, h-index 75, i10-index 135 at harvest). The homepage (DEI, University of Padova; 'Born in 1958') links this profile, DBLP pid 47/4770 carries the ORCID 0000-0001-6601-0568 and this Scholar link, and the rows include Local branching, The feasibility pump, Feasibility pump 2.0, Proximity search, Exploiting erraticism in search, Orbital shrinking and the Benders papers. Martina Fischetti appears as a separate co-author profile in the sidebar and as a co-author on rows such as S051, S103 and S143.

Ids: S### = Scholar row in citation order, D### = not on Scholar but in DBLP, H### = only on the homepage. Sorted by Scholar citations; items without a count go last, in id order. Full records incl. duplicates: works.json.

| # | Year | Title | Venue | Cites | DOI | arXiv | Kind |
|---|---|---|---|---|---|---|---|
| S001 | 2003 | Local branching | Mathematical programming 98 (1), 23-47, 2003 | 1357 | 10.1007/s10107-003-0395-5 |  | journal |
| S002 | 2002 | Modeling and solving the train timetabling problem | Operations research 50 (5), 851-861, 2002 | 883 | 10.1287/opre.50.5.851.362 |  | journal |
| S003 | 2000 | Algorithms for the set covering problem | Annals of Operations Research 98 (1), 353-371, 2000 | 708 | 10.1023/a:1019225027893 |  | journal |
| S004 | 1999 | A heuristic method for the set covering problem | Operations research 47 (5), 730-743, 1999 | 652 | 10.1287/opre.47.5.730 |  | journal |
| S005 | 1997 | A branch-and-cut algorithm for the symmetric generalized traveling salesman problem | Operations Research 45 (3), 378-394, 1997 | 645 | 10.1287/opre.45.3.378 |  | journal |
| S006 | 2006 | Combinatorial Benders' cuts for mixed-integer linear programming | Operations Research 54 (4), 756-766, 2006 | 644 | 10.1287/opre.1060.0286 |  | journal |
| S007 | 2005 | The feasibility pump | Mathematical programming 104 (1), 91-104, 2005 | 631 | 10.1007/s10107-004-0570-3 |  | journal |
| S008 | 2018 | Deep neural networks and mixed integer linear optimization | Constraints 23 (3), 296-309, 2018 | 524 | 10.1007/s10601-018-9285-6 |  | journal |
| S009 | 1998 | Solving the orienteering problem through branch-and-cut | INFORMS Journal on Computing 10 (2), 133-148, 1998 | 478 | 10.1287/ijoc.10.2.133 |  | journal |
| S010 | 2009 | Light robustness | Robust and online large-scale optimization: Models and techniques for… | 417 | 10.1007/978-3-642-05465-5_3 |  | chapter |
| S011 | 2017 | Redesigning Benders decomposition for large-scale facility location | Management Science 63 (7), 2146-2162, 2017 | 368 | 10.1287/mnsc.2016.2461 |  | journal |
| S012 | 1997 | Algorithms for railway crew management | Mathematical programming 79 (1), 125-141, 1997 | 361 | 10.1007/bf02614314 |  | journal |
| S013 | 2001 | Solving the asymmetric travelling salesman problem with time windows by branch-and-cut | Mathematical programming 90 (3), 475-506, 2001 | 346 | 10.1007/pl00011432 |  | journal |
| S014 | 2006 | An algorithmic framework for the exact solution of the prize-collecting Steiner tree problem | Mathematical programming 105 (2), 427-449, 2006 | 321 | 10.1007/s10107-005-0660-x |  | journal |
| S015 | 2009 | The new Dutch timetable: The OR revolution | Interfaces 39 (1), 6-17, 2009 | 297 | 10.1287/inte.1080.0409 |  | journal |
| S016 | 2017 | A new general-purpose algorithm for mixed-integer bilevel linear programs | Operations Research 65 (6), 1615-1637, 2017 | 296 | 10.1287/opre.2017.1650 |  | journal |
| S017 | 1998 | Modeling and solving the crew rostering problem | Operations research 46 (6), 820-830, 1998 | 294 | 10.1287/opre.46.6.820 |  | journal |
| S018 | 2009 | Fast approaches to improve the robustness of a railway timetable | Transportation Science 43 (3), 321-335, 2009 | 271 | 10.1287/trsc.1090.0264 |  | journal |
| S019 | 1994 | A branch-and-bound algorithm for the capacitated vehicle routing problem on directed graphs | Operations Research 42 (5), 846-859, 1994 | 271 | 10.1287/opre.42.5.846 |  | journal |
| S020 | 1993 | The delivery man problem and cumulative matroids | Operations Research 41 (6), 1055-1064, 1993 | 255 | 10.1287/opre.41.6.1055 |  | journal |
| S021 | 1989 | A branch and bound algorithm for the multiple depot vehicle scheduling problem | Networks 19 (5), 531-548, 1989 | 254 | 10.1002/net.3230190505 |  | journal |
| S022 | 1996 | {0, 1/2}-Chvátal-Gomory cuts | Mathematical Programming 74 (3), 221-235, 1996 | 251 | 10.1007/bf02592196 |  | journal |
| S023 | 2016 | Benders decomposition without separability: A computational study for capacitated facility location problems | European Journal of Operational Research 253 (3), 557-569, 2016 | 243 | 10.1016/j.ejor.2016.03.002 |  | journal |
| S024 | 2010 | A note on the selection of Benders’ cuts | Mathematical Programming 124 (1), 175-182, 2010 | 243 | 10.1007/s10107-010-0365-7 |  | journal |
| S025 | 1995 | The precedence-constrained asymmetric traveling salesman polytope | Mathematical programming 68 (1), 241-265, 1995 | 241 | 10.1007/bf01585767 |  | journal |
| S026 | 2007 | A feasibility pump heuristic for general mixed-integer problems | Discrete Optimization 4 (1), 63-76, 2007 | 216 | 10.1016/j.disopt.2006.10.001 |  | journal |
| S027 | 2018 | On the use of intersection cuts for bilevel optimization | Mathematical Programming 172 (1), 77-103, 2018 | 187 | 10.1007/s10107-017-1189-5 |  | journal |
| S028 | 2000 | A polyhedral study of the asymmetric traveling salesman problem with time windows | Networks: An International Journal 36 (2), 69-79, 2000 | 185 | 10.1002/1097-0037(200009)36:2<69::aid-net1>3.0.co;2-q |  | journal |
| S029 | 2016 | On handling indicator constraints in mixed integer programming | Computational Optimization and Applications 65 (3), 545-566, 2016 | 184 | 10.1007/s10589-016-9847-8 |  | journal |
| S030 | 1995 | The symmetric generalized traveling salesman polytope | Networks 26 (2), 113-123, 1995 | 184 | 10.1002/net.3230260206 |  | journal |
| S031 | 1989 | An additive bounding procedure for combinatorial optimization problems | Operations Research 37 (2), 319-328, 1989 | 178 | 10.1287/opre.37.2.319 |  | journal |
| S032 | 2006 | A new ILP-based refinement heuristic for vehicle routing problems | Mathematical Programming 105 (2), 471-499, 2006 | 174 | 10.1007/s10107-005-0662-8 |  | journal |
| S033 | 2007 | Optimizing over the first Chvátal closure | Mathematical Programming 110 (1), 3-20, 2007 | 173 | 10.1007/s10107-006-0054-8 |  | journal |
| S034 | 2005 | Reinventing crew scheduling at Netherlands Railways | Interfaces 35 (5), 393-401, 2005 | 173 | 10.1287/inte.1050.0158 |  | journal |
| S035 | 1994 | Weighted k-cardinality trees: Complexity and polyhedral structure | Networks 24 (1), 11-21, 1994 | 171 | 10.1002/net.3230240103 |  | journal |
| S036 | 1993 | Heuristic algorithms for the multiple depot vehicle scheduling problem | Management Science 39 (1), 115-125, 1993 | 159 | 10.1287/mnsc.39.1.115 |  | journal |
| S037 | 2011 | Heuristics in mixed integer programming | Wiley Encyclopedia of Operations Research and Management Science. John Wiley… | 158 | 10.1002/9780470400531.eorms0376 |  | chapter |
| S038 | 2019 | Interdiction Games and Monotonicity, with Application to Knapsack Problems | INFORMS Journal on Computing 31 (2), 390-410, 2019 | 154 | 10.1287/ijoc.2018.0831 |  | journal |
| S039 | 1987 | The fixed job schedule problem with spread-time constraints | Operations Research 35 (6), 849-858, 1987 | 150 | 10.1287/opre.35.6.849 |  | journal |
| S040 | 2017 | Thinning out Steiner trees: a node-based model for uniform edge costs | Math. Program. Comput. 9(2), 203-229 | 148 | 10.1007/s12532-016-0111-0 |  | journal |
| S041 | 2009 | Feasibility pump 2.0 | Mathematical Programming Computation 1 (2), 201-222, 2009 | 148 | 10.1007/s12532-009-0007-3 |  | journal |
| S042 | 2012 | A Lagrangian heuristic for robustness, with an application to train timetabling | Transportation Science 46 (1), 124-133, 2012 | 147 | 10.1287/trsc.1110.0378 |  | journal |
| S043 | 1997 | A polyhedral approach to the asymmetric traveling salesman problem | Management Science 43 (11), 1520-1536, 1997 | 146 | 10.1287/mnsc.43.11.1520 |  | journal |
| S044 | 1992 | An additive bounding procedure for the asymmetric travelling salesman problem | Mathematical programming 53 (1), 173-197, 1992 | 146 | 10.1007/bf01585701 |  | journal |
| S045 | 2012 | Cutting plane versus compact formulations for uncertain (integer) linear programs | Mathematical Programming Computation 4, 239-273, 2012 | 140 | 10.1007/s12532-012-0039-y |  | journal |
| S046 | 2009 | Mixed-integer programming models for nesting problems | Journal of Heuristics 15 (3), 201-226, 2009 | 140 | 10.1007/s10732-008-9088-9 |  | journal |
| S047 | 2002 | The generalized traveling salesman and orienteering problems | The traveling salesman problem and its variations, 609-662, 2002 | 140 | 10.1007/0-306-48213-4_13 |  | chapter |
| S048 | 1989 | The fixed job schedule problem with working-time constraints | Operations Research 37 (3), 395-403, 1989 | 140 | 10.1287/opre.37.3.395 |  | journal |
| S049 | 1988 | An additive approach for the optimal solution of the prize-collecting traveling salesman problem | Publication of: Dalctraf, 1988 | 136 |  |  | chapter |
| S050 | 1997 | Branch-and-cut algorithms | Annotated bibliographies in combinatorial optimization, 45-64, 1997 | 135 |  |  | chapter |
| S051 | 2025 | Matheuristics by Examples | Handbook of Heuristics, 1-35, 2025 | 131 | 10.1007/978-3-319-07153-4_14-2 |  | chapter |
| S052 | 2014 | Proximity search for 0-1 mixed-integer convex programming | Journal of Heuristics 20 (6), 709-731, 2014 | 125 | 10.1007/s10732-014-9266-x |  | journal |
| S053 | 1999 | Solution of large-scale railway crew planning problems: The Italian experience | Computer-Aided Transit Scheduling: Proceedings, Cambridge, MA, USA, August…, 1999 | 123 | 10.1007/978-3-642-85970-0_1 |  | chapter |
| S054 | 2017 | Deep neural networks as 0-1 mixed integer linear programs: A feasibility study | arXiv preprint arXiv:1712.06174, 2017 | 109 |  | 1712.06174 | preprint |
| S055 | 2014 | Exploiting erraticism in search | Operations Research 62 (1), 114-122, 2014 | 108 | 10.1287/opre.2013.1231 |  | journal |
| S056 | 2002 | Exact methods for the asymmetric traveling salesman problem | The traveling salesman problem and its variations, 169-205, 2002 | 108 | 10.1007/0-306-48213-4_4 |  | chapter |
| S057 | 2001 | A polyhedral approach to simplified crew scheduling and vehicle scheduling problems | Management Science 47 (6), 833-850, 2001 | 108 | 10.1287/mnsc.47.6.833.9810 |  | journal |
| S058 | 2000 | On the separation of maximally violated mod-k cuts | Mathematical Programming 87 (1), 37-56, 2000 | 104 | 10.1007/s101079900107 |  | journal |
| S059 | 2017 | Using a general-purpose mixed-integer linear programming solver for the practical solution of real-time train rescheduling | European Journal of Operational Research 263 (1), 258-264, 2017 | 102 | 10.1016/j.ejor.2017.04.057 |  | journal |
| S060 | 1995 | Exact and approximate algorithms for the index selection problem in physical database design | IEEE Transactions on Knowledge and Data Engineering 7 (6), 955-967, 1995 | 98 | 10.1109/69.476501 |  | journal |
| S061 | 2001 | Crew scheduling for Netherlands railways “destination: customer” | Computer-aided scheduling of public transport, 181-201, 2001 | 95 | 10.1007/978-3-642-56423-9_11 |  | chapter |
| S062 | 1993 | A lifting procedure for the asymmetric traveling salesman polytope and a large new class of facets | Mathematical Programming 58 (1), 325-352, 1993 | 94 | 10.1007/bf01581274 |  | journal |
| S063 | 2013 | Backdoor branching | INFORMS Journal on Computing 25 (4), 693-700, 2013 | 93 | 10.1287/ijoc.1120.0531 |  | journal |
| S064 | 2004 | A local branching heuristic for mixed‐integer programs with 2‐level variables, with an application to a telecommunication network design problem | Networks: An International Journal 44 (2), 61-72, 2004 | 91 | 10.1002/net.20017 |  | journal |
| S065 | 2000 | Frequency assignment in mobile radio systems using branch-and-cut techniques | European Journal of Operational Research 123 (2), 241-255, 2000 | 89 | 10.1016/s0377-2217(99)00254-4 |  | journal |
| S066 | 1996 | A heuristic algorithm for the set covering problem | International Conference on Integer Programming and Combinatorial…, 1996 | 89 | 10.1007/3-540-61310-2_6 |  | conference |
| S067 | 2012 | Three ideas for the quadratic assignment problem | Operations research 60 (4), 954-964, 2012 | 87 | 10.1287/opre.1120.1073 |  | journal |
| S068 | 2011 | On the separation of disjunctive cuts | Mathematical Programming 128 (1), 205-230, 2011 | 87 | 10.1007/s10107-009-0300-y |  | journal |
| S069 | 1999 | Models and algorithms for the 2-dimensional cell suppression problem in statistical disclosure control. | Mathematical Programming 84 (2), 1999 | 87 | 10.1007/s10107980022a |  | journal |
| S070 | 2007 | Embedding {0, ½}-Cuts in a Branch-and-Cut Framework: A Computational Study | INFORMS Journal on Computing 19 (2), 229-238, 2007 | 85 | 10.1287/ijoc.1050.0162 |  | journal |
| S071 | 1991 | Facets of the asymmetric traveling salesman polytope | Mathematics of Operations Research 16 (1), 42-56, 1991 | 84 | 10.1287/moor.16.1.42 |  | journal |
| S072 | 2001 | Solving the cell suppression problem on tabular data with linear constraints | Management Science 47 (7), 1008-1027, 2001 | 80 | 10.1287/mnsc.47.7.1008.9805 |  | journal |
| S073 | 2000 | Models and algorithms for optimizing cell suppression in tabular data with linear constraints | Journal of the American Statistical Association 95 (451), 916-928, 2000 | 80 | 10.1080/01621459.2000.10474282 |  | journal |
| S074 | 2011 | Lexicography and degeneracy: can a pure cutting plane algorithm work? | Mathematical programming 130 (1), 153-176, 2011 | 77 | 10.1007/s10107-009-0335-0 |  | journal |
| S075 | 1992 | Approximation algorithms for fixed job schedule problems | Operations Research 40 (1-supplement-1), S96-S108, 1992 | 76 | 10.1287/opre.40.1.s96 |  | journal |
| S076 | 2022 | Learning to search in local branching | Proceedings of the aaai conference on artificial intelligence 36 (4), 3796-3803, 2022 | 68 | 10.1609/aaai.v36i4.20294 | 2112.02195 | conference |
| S077 | 2002 | Exact algorithms for minimum routing cost trees | Networks: An International Journal 39 (3), 161-173, 2002 | 68 | 10.1002/net.10022 |  | journal |
| S078 | 2020 | Heuristic algorithms for the wind farm cable routing problem | Applied Energy 278, 115617, 2020 | 67 | 10.1016/j.apenergy.2020.115617 |  | journal |
| S079 | 2020 | A branch-and-cut algorithm for mixed-integer bilinear programming | European Journal of Operational Research 282 (2), 506-514, 2020 | 67 | 10.1016/j.ejor.2019.09.043 |  | journal |
| S080 | 1993 | An efficient algorithm for the min-sum arborescence problem on complete digraphs | ORSA Journal on Computing 5 (4), 426-434, 1993 | 67 | 10.1287/ijoc.5.4.426 |  | journal |
| S081 | 2001 | Solution of real-world train timetabling problems | Proceedings of the 34th annual Hawaii international conference on system…, 2001 | 63 | 10.1109/hicss.2001.926325 |  | conference |
| S082 | 2018 | Array designer: automated optimized array design for functional near-infrared spectroscopy | Neurophotonics 5 (3), 035010-035010, 2018 | 62 | 10.1117/1.nph.5.3.035010 |  | journal |
| S083 | 2008 | Projected Chvátal–Gomory cuts for mixed integer linear programs | Mathematical Programming 113 (2), 241-257, 2008 | 62 | 10.1007/s10107-006-0051-y |  | journal |
| S084 | 2000 | A polyhedral approach to an integer multicommodity flow problem | Discrete Applied Mathematics 101 (1-3), 13-36, 2000 | 62 | 10.1016/s0166-218x(99)00187-0 |  | journal |
| S085 | 2008 | Repairing MIP infeasibility through local branching | Computers & operations research 35 (5), 1436-1445, 2008 | 61 | 10.1016/j.cor.2006.08.004 |  | journal |
| S086 | 2016 | Proximity Benders: a decomposition heuristic for stochastic programs | Journal of Heuristics 22 (2), 181-198, 2016 | 60 | 10.1007/s10732-015-9306-1 |  | journal |
| S087 | 2005 | Solving the prize-collecting Steiner tree problem to optimality | ALENEX/ANALCO 2005, 68-76, 2005 | 57 |  |  | conference |
| S088 | 2019 | Introduction to mathematical optimization | M. Fischetti, 2019 | 54 |  |  | book |
| S089 | 1991 | Facets of two Steiner arborescence polyhedra | Mathematical Programming 51 (1-3), 401-419, 1991 | 54 | 10.1007/bf01586946 |  | journal |
| S090 | 2018 | A dynamic reformulation heuristic for Generalized Interdiction Problems | European Journal of Operational Research 267 (1), 40-51, 2018 | 53 | 10.1016/j.ejor.2017.11.043 |  | journal |
| S091 | 2004 | Combinatorial Benders’ cuts | International Conference on Integer Programming and Combinatorial…, 2004 | 52 | 10.1007/978-3-540-25960-2_14 |  | conference |
| S092 | 2018 | Least cost influence propagation in (social) networks | Mathematical Programming 170 (1), 293-325, 2018 | 51 | 10.1007/s10107-018-1288-y |  | journal |
| S093 | 2003 | Partial cell suppression: a new methodology for statistical disclosure control | Statistics and Computing 13 (1), 13-21, 2003 | 51 | 10.1023/a:1021927424942 |  | journal |
| S094 | 2016 | Improving branch-and-cut performance by random sampling | Mathematical Programming Computation 8 (1), 113-132, 2016 | 50 | 10.1007/s12532-015-0096-0 |  | journal |
| S095 | 2011 | A relax-and-cut framework for Gomory mixed-integer cuts | Mathematical Programming Computation 3 (2), 79-102, 2011 | 50 | 10.1007/s12532-011-0024-x |  | journal |
| S096 | 2009 | Just MIP it! | MATHEURISTICS: Hybridizing metaheuristics and mathematical programming, 39-70, 2009 | 50 | 10.1007/978-1-4419-1306-7_2 |  | chapter |
| S097 | 2017 | Orbital shrinking: Theory and applications | Discrete applied mathematics 222, 109-123, 2017 | 49 | 10.1016/j.dam.2017.01.015 |  | journal |
| S098 | 2014 | Boosting the feasibility pump | Mathematical Programming Computation 6 (3), 255-279, 2014 | 49 | 10.1007/s12532-014-0068-9 |  | journal |
| S099 | 1989 | New lower bounds for the symmetric travelling salesman problem | Mathematical Programming 45 (1), 233-254, 1989 | 49 | 10.1007/bf01589105 |  | journal |
| S100 | 2023 | Safe distancing in the time of COVID-19 | European journal of operational research 304 (1), 139-149, 2023 | 47 | 10.1016/j.ejor.2021.07.010 |  | journal |
| S101 | 2008 | The linear ordering problem with cumulative costs | European Journal of Operational Research 189 (3), 1345-1357, 2008 | 46 | 10.1016/j.ejor.2006.03.071 |  | journal |
| S102 | 2002 | Polyhedral theory for the asymmetric traveling salesman problem | The traveling salesman problem and its variations, 117-168, 2002 | 45 | 10.1007/0-306-48213-4_3 |  | chapter |
| S103 | 2023 | Integrated layout and cable routing in wind farm optimal design | Management Science 69 (4), 2147-2164, 2023 | 44 | 10.1287/mnsc.2022.4470 |  | journal |
| S104 | 1988 | A new dominance procedure for combinatorial optimization problems | Operations Research Letters 7 (4), 181-187, 1988 | 42 | 10.1016/0167-6377(88)90025-9 |  | journal |
| S105 | 2003 | Solving real-world ATSP instances by branch-and-cut | Combinatorial Optimization—Eureka, You Shrink! Papers Dedicated to Jack… | 40 | 10.1007/3-540-36478-1_8 |  | conference |
| S106 | 2010 | An in-out approach to disjunctive optimization | International Conference on Integration of Artificial Intelligence (AI) and… | 38 | 10.1007/978-3-642-13520-0_17 |  | conference |
| S107 | 1997 | On the monotonization of polyhedra | Mathematical Programming 78 (1), 59-84, 1997 | 38 | 10.1007/bf02614506 |  | journal |
| S108 | 1987 | Worst-case analysis of the differencing method for the partition problem | Mathematical Programming: Series A and B 37 (1), 117-120, 1987 | 38 | 10.1007/bf02591687 |  | journal |
| S109 | 2016 | Fast training of support vector machines with Gaussian kernel | Discrete Optimization 22, 183-194, 2016 | 35 | 10.1016/j.disopt.2015.03.002 |  | journal |
| S110 | 2021 | Embedding Simulated Annealing within Stochastic Gradient Descent | OLA 2021 (Communications in Computer and Information Science 1443), 3-13 | 34 | 10.1007/978-3-030-85672-4_1 |  | conference |
| S111 | 2014 | Self-splitting of workload in parallel computation | International Conference on Integration of Constraint Programming… | 34 | 10.1007/978-3-319-07046-9_28 |  | conference |
| S112 | 2009 | Minimal infeasible subsystems and Benders cuts | Mathematical Programming to appear, 2009 | 34 |  |  | report |
| S113 | 1992 | The fixed-outdegree 1-arborescence polytope | Mathematics of Operations Research 17 (4), 1001-1018, 1992 | 34 | 10.1287/moor.17.4.1001 |  | journal |
| S114 | 1995 | Experiments with a multi-commodity formulation for the symmetric capacitated vehicle routing problem | Proceedings of the 3rd Meeting of the EURO Working Group on Transportation… | 33 |  |  | conference |
| S115 | 2008 | How tight is the corner relaxation? | Discrete Optimization 5 (2), 262-269, 2008 | 30 | 10.1016/j.disopt.2006.11.010 |  | journal |
| S116 | 1995 | Clique tree inequalities define facets of the asymmetric traveling salesman polytope | Discrete Applied Mathematics 56 (1), 9-18, 1995 | 30 | 10.1016/0166-218x(93)e0082-a |  | journal |
| S117 | 2015 | MIP‐and‐refine matheuristic for smart grid energy management | International Transactions in Operational Research 22 (1), 49-59, 2015 | 28 | 10.1111/itor.12034 |  | journal |
| S118 | 2007 | Mixed-integer cuts from cyclic groups | Mathematical Programming 109 (1), 27-53, 2007 | 25 | 10.1007/s10107-006-0726-4 |  | journal |
| S119 | 2000 | Scheduling train drivers and guards: the Dutch" Noord-Oost" case | Proceedings of the 33rd Annual Hawaii International Conference on System… | 25 | 10.1109/hicss.2000.926668 |  | conference |
| S120 | 1999 | Lifted cycle inequalities for the asymmetric traveling salesman problem | Mathematics of Operations Research 24 (2), 273-292, 1999 | 24 | 10.1287/moor.24.2.273 |  | journal |
| S121 | 1997 | A branch‐and‐cut algorithm for the resource‐constrained minimum‐weight arborescence problem | Networks: An International Journal 29 (1), 55-67, 1997 | 24 | 10.1002/(sici)1097-0037(199701)29:1<55::aid-net6>3.0.co;2-b |  | journal |
| S122 | 1988 | A hybrid algorithm for finding the kth smallest of n elements in O (n) time | Annals of Operations Research 13 (1), 399-419, 1988 | 24 | 10.1007/bf02288326 |  | journal |
| S123 | 2016 | Mixed-Integer Linear Programming Heuristics for the PrePack Optimization Problem | Discret. Optim. 22, 195-205 | 23 | 10.1016/j.disopt.2015.03.004 |  | journal |
| S124 | 2010 | Pruning moves | INFORMS Journal on Computing 22 (1), 108-119, 2010 | 23 | 10.1287/ijoc.1090.0329 |  | journal |
| S125 | 2001 | A branch-and-cut algorithm for the multiple depot vehicle scheduling problem |  | 21 |  |  | report |
| S126 | 2025 | A fix-propagate-repair heuristic for mixed integer programming | Mathematical Programming Computation 17 (1), 111-139, 2025 | 20 | 10.1007/s12532-024-00269-5 |  | journal |
| S128 | 1992 | Three Facet-Lifting Theorems for the Asymmetric Traveling Salesman Polytope. | IPCO, 260-273, 1992 | 17 |  |  | conference |
| S129 | 2006 | Robust optimization through branch-and-price | Proceedings of the 37th annual conference of the Italian operations research… | 16 |  |  | conference |
| S130 | 2022 | An integrated local-search/set-partitioning refinement heuristic for the capacitated vehicle routing problem | Mathematical Programming Computation 14 (4), 749-779, 2022 | 14 | 10.1007/s12532-022-00224-2 |  | journal |
| S131 | 2015 | Optimal turbine allocation for offshore and onshore wind farms | Optimization in the Real World: Toward Solving Real-World Optimization… | 13 | 10.1007/978-4-431-55420-2_4 |  | chapter |
| S132 | 2007 | Integer Programming and Combinatorial Optimization: 12th International IPCO Conference, Ithaca, NY, USA, June 25-27, 2007, Proceedings | Springer, 2007 | 12 | 10.1007/978-3-540-72792-7 |  | book |
| S133 | 2018 | Faster SGD training by minibatch persistency | arXiv preprint arXiv:1806.07353, 2018 | 11 |  | 1806.07353 | preprint |
| S134 | 2010 | On the knapsack closure of 0-1 Integer Linear Programs | Electronic Notes in Discrete Mathematics 36, 799-804, 2010 | 10 | 10.1016/j.endm.2010.05.101 |  | journal |
| S135 | 2003 | Optimisation of the interconnecting network of a UMTS radio mobile telephone system | European Journal of Operational Research 144 (1), 56-67, 2003 | 10 | 10.1016/s0377-2217(01)00383-6 |  | journal |
| S137 | 2018 | Chasing first queens by integer programming | International Conference on the Integration of Constraint Programming… | 8 | 10.1007/978-3-319-93031-2_16 |  | conference |
| S139 | 1999 | On the Separation of Maximally Violated mod-k Cuts | International Conference on Integer Programming and Combinatorial… | 8 | 10.1007/3-540-48777-8_7 |  | conference |
| S140 | 2006 | New facets of the STS polytope generated from known facets of the ATS polytope | Discrete Optimization 3 (1), 3-19, 2006 | 6 | 10.1016/j.disopt.2005.10.001 |  | journal |
| S141 | 1990 | A new linear storage, polynomial-time approximation scheme for the subset-sum problem | Discrete applied mathematics 26 (1), 61-77, 1990 | 5 | 10.1016/0166-218x(90)90021-4 |  | journal |
| S142 | 2007 | Mipping closures: An instant survey | Graphs and Combinatorics 23 (Suppl 1), 233-243, 2007 | 4 | 10.1007/s00373-007-0711-6 |  | journal |
| S143 | 2026 | EndoWake: Modeling wind by linear programming for wind farm layout optimization | arXiv preprint arXiv:2609.40157, 2026 | 3 |  | 2609.40157 | preprint |
| S144 | 2026 | Models and algorithms for the time window assignment traveling salesperson problem with stochastic travel times | European Journal of Operational Research 329 (1), 96-111, 2026 | 3 | 10.1016/j.ejor.2025.07.034 |  | journal |
| S145 | 2017 | Integer (Linear) Optimization | Advances and Trends in Optimization with Engineering Applications (MOS-SIAM Series on Optimization), chapter 5 | 3 | 10.1137/1.9781611974683.ch5 |  | chapter |
| S146 | 2014 | Branchstorming (brainstorming about tree search) | ISCO 2014: 3rd International Symposium on Combinatorial Optimization, Lisbon, 2014 | 3 |  |  | talk |
| S147 | 1998 | An LP-based heuristic approach to the crew scheduling problem | Proceedings TRISTAN III, 1998 | 3 |  |  | conference |
| S150 | 2026 | GPU-accelerated wind farm layout search with a distilled endogenous wake model (EndoWake) | arXiv preprint arXiv:2610.07844, 2026 | 1 |  | 2610.07844 | preprint |
| S151 | 2025 | Column Generation Algorithms for the Pickup and Delivery Problem with Time Windows and Last-in-First-out Loading | Beyond Frontiers of Operations Research: Emerging Technologies and Innovative Optimization Paradigms (AIRO Springer Series 14), 75-86, 2025 | 1 | 10.1007/978-3-031-85894-9_6 |  | chapter |
| S152 | 2017 | Comments on: On learning and branching: a survey | Top 2 (25), 237-238, 2017 | 1 | 10.1007/s11750-017-0449-0 |  | journal |
| S154 | 2014 | Proximity search heuristics for Mixed Integer Programs |  | 1 |  |  | other |
| S155 | 2006 | MIP models for MIP heuristics | Talk presented at Matheuristics, 2006 | 1 |  |  | talk |
| S161 | 2026 | Just sort it! A note on the LP behind rank-one anti-loop edits | arXiv preprint arXiv:2611.21432, 2026 |  |  | 2611.21432 | preprint |
| S162 | 2026 | A Dantzig-Wolfe reformulation of the EndoWake model for optimal wind farm layouts | arXiv preprint arXiv:2610.39503, 2026 |  |  | 2610.39503 | preprint |
| S163 | 2026 | Minibatch persistency, eight years later: what batch reuse costs in steps and joules, and what it saves in data | arXiv preprint arXiv:2609.13922, 2026 |  |  | 2609.13922 | preprint |
| S164 | 2026 | Feasibility Pump with Objective Cutoff: A Computational Study |  |  |  |  | preprint |
| S165 | 2026 | A digital twin of Fermat in 1637: reconstructing the marvellous proof and locating where it fails |  |  |  |  | preprint |
| S166 | 2025 | An improved compact formulation for the assortment optimization problem with small consideration sets | Journal of the Operational Research Society 76 (10), 2060-2070, 2025 |  | 10.1080/01605682.2025.2451738 |  | journal |
| S168 | 2022 | A Vehicle Routing heuristic based on accelerated LKH-3 coupled with Set Partitioning | 12th DIMACS Implementation Challenge: Vehicle Routing Problems, 2022 |  |  |  | conference |
| S170 | 2013 | Proximity Search | 10th Metaheuristics International Conference, 42-42, 2013 |  |  |  | conference |
| S171 | 2013 | Alberto Caprara (1968-2012): Scientific Contributions | OPTIMA, 1-11, 2013 |  |  |  | other |
| S172 | 2012 | A Benders Decomposition Approach to the Time Window Assignment Traveling Salesperson Problem with Stochastic Travel Times | Book of Abstracts 60 (4), 228, 2012 |  |  |  | conference |
| S173 | 2010 | Towards a MIP-Cut metascheme | International Conference on Integration of Artificial Intelligence (AI) and… |  | 10.1007/978-3-642-13520-0_1 |  | conference |
| S174 | 2009 | Yoyo search: a bisection cutting-plane method |  |  |  |  | report |
| S176 | 2008 | 8th Workshop on Algorithmic Approaches for Transportation Modeling, Optimization, and Systems (ATMOS'08) | Schloss Dagstuhl-Leibniz-Zentrum für Informatik GmbH, 2008 |  |  |  | book |
| S178 | 2008 | ATMOS 2008 Preface--8th Workshop on Algorithmic Approaches for Transportation Modeling, Optimization, and Systems | 8th Workshop on Algorithmic Approaches for Transportation Modeling… |  | 10.4230/oasics.atmos.2008.1593 |  | other |
| S180 | 2001 | Combining complete and partial cell suppression methodologies in statistical disclosure control | Statistical Journal of the United Nations Economic Commission for Europe 18… |  | 10.3233/sju-2001-18410 |  | journal |
| S184 | 1994 | Odd cut-sets, odd cycles, and 0-1/2 Chvatal-Gomory cuts | Univ. of Michigan, Ann Arbor, MI (United States), 1994 |  |  |  | conference |
| S185 | 1987 | Modelli e algoritmi per problemi di routing e di scheduling dottorato di ricerca in ingegneria dei sistemi | Alma Mater Studiorum-Università di Bologna, 1987 |  |  |  | thesis |
| S186 | 2026 | Replication package for" EndoWake: Modeling Wind by Linear Programming for Wind Farm Layout Optimization" | Zenodo, 0 |  | 10.5281/zenodo.22017424 |  | other |
| S187 |  | Technical note for GPU-accelerated wind farm layout search with a distilled endogenous wake model (EndoWake) |  |  |  |  | report |
| S188 |  | Optimización combinatoria poliédrica: problemas de rutas-localización |  |  |  |  | other |
| S189 |  | Exact and approximate algorithms for bus driver scheduling problems in Logistique: Production, Distribution, Transport. Logistics: Manufacturing, Distribution, Transportation |  |  |  |  | chapter |
| S190 |  | Intersection Cuts for Quadratic Mixed-Integer Optimization |  |  |  |  | other |
| S192 |  | Metaheuristic frameworks for deep neural network training |  |  |  |  | other |
| S193 |  | Simplified Benders cuts for facility location | Speaker, 9, 0 |  |  |  | talk |
| S194 |  | Exact Algorithms for Mixed-Integer Bilevel Linear Programming |  |  |  |  | other |
| S195 |  | Thinning out facilities: Lagrange, Benders, and |  |  |  |  | report |
| S196 |  | Solving Congested Facility Location by Branch-and-Cut |  |  |  |  | other |
| S198 |  | Exact and Heuristic Methods for Nesting Problems |  |  |  |  | other |
| D001 | 1993 | On the monotonization of polyhedra | IPCO, 23-38 |  |  |  | conference |
| D002 | 2005 | Mixed-Integer Cuts from Cyclic Groups | IPCO, 1-11 |  | 10.1007/11496915_1 |  | conference |
| D003 | 2005 | Optimizing over the First Chvàtal Closure | IPCO, 12-22 |  | 10.1007/11496915_2 |  | conference |
| D004 | 2007 | Fast Approaches to Robust Railway Timetabling | ATMOS |  | 10.4230/oasics.atmos.2007.1176 |  | conference |
| D005 | 2008 | ATMOS 2008 Abstracts Collection - 8th Workshop on Algorithmic Approaches for Transportation Modeling, Optimization, and Systems | ATMOS |  | 10.4230/oasics.atmos.2008.1592 |  | other |
| D006 | 2008 | Can Pure Cutting Plane Algorithms Work? | IPCO, 416-434 |  | 10.1007/978-3-540-68891-4_29 |  | conference |
| D007 | 2009 | Robustness in Train Timetabling | CTW, 171-174 |  |  |  | conference |
| D008 | 2010 | A Relax-and-Cut Framework for Gomory's Mixed-Integer Cuts | CPAIOR, 123-135 |  | 10.1007/978-3-642-13520-0_16 |  | conference |
| D009 | 2010 | On the enumerative nature of Gomory's dual cutting plane method | Math. Program. 125(2), 325-351 |  | 10.1007/s10107-010-0392-4 |  | journal |
| D010 | 2011 | Backdoor Branching | IPCO, 183-191 |  | 10.1007/978-3-642-20807-2_15 |  | conference |
| D011 | 2012 | A hard integer program made easy by lexicography | Math. Program. 135(1-2), 509-514 |  | 10.1007/s10107-011-0450-6 |  | journal |
| D012 | 2012 | Branching on nonchimerical fractionalities | Oper. Res. Lett. 40(3), 159-164 |  | 10.1016/j.orl.2012.01.008 |  | journal |
| D013 | 2012 | Orbital Shrinking | ISCO, 48-58 |  | 10.1007/978-3-642-32147-4_6 |  | conference |
| D014 | 2013 | Approximating the Split Closure | INFORMS J. Comput. 25(4), 808-819 |  | 10.1287/ijoc.1120.0543 |  | journal |
| D015 | 2016 | Intersection Cuts for Bilevel Optimization | IPCO, 77-88 |  | 10.1007/978-3-319-33461-5_7 |  | conference |
| D016 | 2018 | Matheuristics | Handbook of Heuristics, 121-153 |  | 10.1007/978-3-319-07124-4_14 |  | chapter |
| D017 | 2018 | SelfSplit parallelization for mixed-integer linear programming | Comput. Oper. Res. 93, 101-112 |  | 10.1016/j.cor.2018.01.011 |  | journal |
| D018 | 2019 | Embedded hyper-parameter tuning by Simulated Annealing | arXiv preprint arXiv:1906.01504 |  |  | 1906.01504 | preprint |
| D019 | 2019 | Finding First and Most-Beautiful Queens by Integer Programming | arXiv preprint arXiv:1907.08246 |  |  | 1907.08246 | preprint |
| H001 | 1986 | Worst-Case Analysis of an Approximation Scheme for the Subset-Sum Problem | Operations Research Letters 6, 283-284 |  | 10.1016/0167-6377(86)90065-9 |  | journal |
| H002 | 1996 | Odd Cut-sets, Odd Cycles, and 0-1/2 Chvatal-Gomory Cuts | Ricerca Operativa 26, 51-80 |  |  |  | journal |
| H003 | 1998 | Experiments with Controlled Rounding for Statistical Disclosure Control in Tabular Data with Linear Constraints | Journal of Official Statistics 17, 4, 101-113 |  |  |  | journal |
| H004 | 1999 | I Turni delle Locomotive | in S. Pallottino, A. Sciomachen (eds.), Scienze delle Decisioni per i Trasporti, Collana Trasporti, Franco Angeli, 476-494 |  |  |  | chapter |
| H005 |  | Lezioni di Ricerca Operativa |  |  |  |  | book |

## Rows marked as duplicates or junk (21)

| Row | dup_of | Title | Venue |
|---|---|---|---|
| S127 | S010 | Robust and online large-scale optimization | Lecture notes in computer science 5868, 61-84, 2009 |
| S136 | S073 | Complementary cell suppression for statistical disclosure control in tabular data with linear constraints | Journal of the American Statistical Association 95 (451), 916-928, 2000 |
| S138 | S132 | Proceedings of the 12th international conference on Integer Programming and Combinatorial Optimization | Springer-Verlag, 2007 |
| S148 | S066 | Integer Programming and Combinatorial Optimization: 5th International IPCO Conference, Vancouver, British Columbia, Canada, June 3-5, 1996: Proceedings | Springer, 1996 |
| S149 | S062 | A Lifting Procedure For The Asymmetric Traveling Saleman Polytope And A Large New Class Of Facets | GSIA Working Papers, 1989 |
| S153 | S097 | Orbital shrinking | Discrete Applied Mathematics 222 (C), 109-123, 2017 |
| S156 | S026 | A feasibility pump heuristic for general mixed-integer problems livio bertacco, matteo fischetti◦, andrea lodi |  |
| S157 | S034 | Reinventing Crew Scheduling at Netherlands Railways | Technical Report, Turni, Padova, 2004 |
| S158 | S017 | Modeling and solving the crew rostering problem | Operations Research 46 (10.1287), 1998 |
| S159 | S005 | A branch and bound algorithm for the symmetric generalised TSP | Oper. Res 45, 378-394, 1997 |
| S160 | S035 | Weighted k-cardinality trees |  |
| S167 | S151 | Column Generation Algorithms for the Pickup and Delivery Problem | Beyond Frontiers of Operations Research: Emerging Technologies and… |
| S169 | S098 | Boosting the feasibility pump | Mathematical Programming Computation, 2014 |
| S175 | S015 | The new Dutch timetable: The OR revolution Cg: 250 | Operations Research Management Science 49 (3), 231, 2009 |
| S177 | S178 | ATMOS 2008 Preface: Algorithmic Approaches for Transportation Modeling, Optimization, and Systems | OpenAccess Series in Informatics (OASIcs) 9, 2008 |
| S179 | S032 | A new ILP-based refinement heuristic for Vehicle Routing Problems | Mathematical Programming, 2006 |
| S181 | S102 | Polyhedral Theory for the Asymmetric Traveling Salesman Problem (Book Chapter) |  |
| S182 | S119 | Scheduling Train Drivers and Guards: The Dutch" Noord-Oost" Case-TRACK: Decision Technologies for Management | Proceedings of: HICSS 2000-33nd Hawaii International Conference on System… |
| S183 | S058 | On the Separation of Maximally Violated mod |  |
| S191 | S049 | AN ADDITIVE APPROACH FOR THE OPTIMAL SOLUTION OF THE PRIZE-COLLECTING TRAVELLING SALESMAN PROBLEM |  |
| S197 | S040 | Thinning out Steiner trees |  |

## Homepage papers-directory files not attached to a work (13)

Not works: `000_copyright_notice.txt` and `2016-COAP_best_paper_award.pdf` (by its name the award for S029, which the homepage lists under Prizes). The other files are not attached because their names do not identify one work with confidence (a conference and a journal version could share the name, or the name is generic), and their first pages were not read in this step (WebFetch returned only compressed PDF streams for the files it tried): `2025_ODS2025_Fischetti.pdf`, `Benders_mis_extended_draft.pdf`, `MIPdominance.pdf`, `Uncertain_SCP.pdf`, `knuth_lexico.pdf`, `prize_collecting_steiner_tree.pdf`, `proxy_RAMP.pdf`, `robust_train_timetabling.pdf`, `teoria_poliedrale.pdf`, `theory_on_012_cuts.pdf`, `tree_search_stabilization_by_random_sampling.pdf`.
