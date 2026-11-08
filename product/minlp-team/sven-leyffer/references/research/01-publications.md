# Sven Leyffer · Research note 01 · Signature works and the publication landscape

| Field | Value |
|---|---|
| Researcher | Sven Leyffer (living). Scholar profile line on 2026-10-10: "Senior Computational Mathematician, Argonne National Laboratory" |
| Dimension | Phase 1, research agent 01 of 06 (nuwa research-craft): publication landscape plus 3-5 signature works dissected (framework §二, §五) |
| Research date | 2026-10-10 |
| Sources consulted | 31 (28 primary, 3 secondary); see "Sources". WebSearch calls used: 2 of 2 |
| Local corpus | `references/sources/papers`, `talks`, `essays`, `software` held only `.gitkeep` placeholders on 2026-10-10: no user-supplied material. `private/` was not opened |
| Full texts read | (a) Fletcher, Leyffer, Toint, "A Brief History of Filter Methods" (2006 preprint), in full; (b) Leyffer, Dundee report NA/182 (1998), pp. 1-2 and 10-12, read as page images; (c) Belotti et al., Acta Numerica preprint (2012): contents, §1.3, §2.1 and §3.4.1 only; (d) Leyffer, "Nonlinear Optimization and Beyond", INFORMS OS Today 7(2), 2017, pp. 3-10, in full; (e) the open-access 2026 Correction to Leyffer and Manns, in full. Everything else: abstracts and metadata only |

Tag legend. [stated] = Leyffer's own words, alone or as coauthor of a retrospective or survey; [practice] = what his papers, reports, code and records show he did; [observed] = what others (prize committees, coauthors, databases, solver pages) say; [inferred] = my inference, with its basis given. "primary" or "secondary" describes the source. Quotations are verbatim (whitespace normalised; typos are the source's), with page numbers where a full text was read. Page numbers for (a), (b) and (c) follow the preprint or report pagination, not the journal version.

---

## 0. How the record was assembled, and what it misses

| Source | What it gave | Status |
|---|---|---|
| Google Scholar `UubsxcAAAAAJ`, 100 rows in citation order | citation counts, most-cited works, report-type items | read 2026-10-10 |
| DBLP pid `91/745` via `scripts/dblp_works.py` (SPARQL) | 92 records, 1994-2026: 64 articles, 13 proceedings papers, 14 CoRR preprints, 1 encyclopedia entry; 92 with DOI, 14 with arXiv id | complete for DBLP |
| arXiv author search "Leyffer" | 35 items, from math/0310357 (2003) to 2509.19888 (v2, 6 Oct 2026); 8 abstract pages read | complete for arXiv |
| Optimization Online search "Leyffer" | 51 hits, 2000-08 to 2024-09; author lists checked on 8 entry pages, all with Leyffer as author | 43 hits not opened (the search also matches papers that only mention him) |
| Crossref REST API | metadata, deposited abstracts, citation counts for about 40 DOIs | as needed |
| Publisher landing pages (Springer) | 8 verbatim abstracts, submission dates, affiliations | as needed |
| Semantic Scholar API | HTTP 429 (rate limited) | not used |
| OpenAlex (`fetch_publications.py`) | not run: `OPENALEX_API_KEY` not set | not used |
| Homepage `wiki.mcs.anl.gov/leyffer`, `anl.gov` profile pages, SIAM pages | HTTP 403 to curl and to WebFetch | no homepage CV consulted |

Coverage caveats.
- DBLP holds only 2 records before 2000. The Dundee-era work (numerical-analysis reports NA/171 to NA/210, the thesis, the software manuals) is visible only through Scholar, Optimization Online and the reference lists of his own papers. [practice · primary]
- His Scholar profile contains at least one misattributed record ("The journals", A Bennett, F Swinnerton, 1971, 40 citations), so Scholar totals are slightly inflated. [observed · primary database]
- arXiv is a late habit: 5 arXiv postings from 2003 to 2016, 30 from 2019 on. Earlier preprints went to Dundee NA reports, the Argonne ANL/MCS-P series and, from 2000, Optimization Online. [practice · primary; that this is a habit is inferred]

---

## 1. Publication landscape

### 1.1 Headline numbers (2026-10-10)

- Scholar: 12,362 citations (3,743 since 2021); h-index 43 (27 since 2021); i10-index 113 (67). Listed interests: "Optimization, Nonlinear Optimization, Mixed-Integer Optimization, Nonlinear Programming". [observed · primary database]
- DBLP venues: CoRR 14, SIAM J. Optim. 10, Comput. Optim. Appl. 10, Math. Program. 9, Optim. Methods Softw. 5, SIAM J. Sci. Comput. 5, INFORMS J. Comput. 4, Math. Program. Comput. 2, SC 2, singletons elsewhere. [practice · primary]
- Most frequent DBLP coauthors (articles and proceedings with at most 12 authors, CoRR excluded): Todd S. Munson 13, Roger Fletcher 8, Stefan M. Wild 8, Noam Goldberg 5, Jeffrey Larson 5, Philippe L. Toint 4, Paul Manns 4; then Linderoth, Mahajan, Kirches, Balaprakash, Di, Vanaret, Alexeev, Fei, Brady and Siqian Shen with 3 each. [practice · primary]

### 1.2 Topics by five-year period

Every item carries an identifier checked in this run; "(Scholar)" marks report-type items whose venue, year and title were checked only on the Scholar profile, in Optimization Online or in his own reference lists.

**1989-1994 · PhD at Dundee with Roger Fletcher** (Vordiplom, Hamburg, 1989 [secondary: Wikipedia]).
- Deterministic methods for MINLP. Thesis "Deterministic methods for mixed integer nonlinear programming" (Scholar: University of Dundee, 1993; MGP: 1994, "...in Mixed Integer...", see Contradictions). [practice]
- Fletcher and Leyffer, "Solving mixed integer nonlinear programs by outer approximation", Math. Program. 66 (1994) 327-349, DOI 10.1007/BF01581153, received 15 June 1992. [practice · primary]
- Pattern [inferred]: two-author papers with the advisor.

**1995-1999 · Dundee after the PhD** (EPSRC grant GR/K51204, acknowledged in NA/182, p. 1).
- MIQP branch-and-bound: Fletcher and Leyffer, "Numerical experience with lower bounds for MIQP branch-and-bound", SIAM J. Optim. 8(2) (1998) 604-616, DOI 10.1137/S1052623494268455. Its abstract already commits to tree search: "The branch-and-bound approach is also shown to be superior to other approaches in solving MIQP problems." [stated · primary]
- The filter method is born: report NA/171 (Sept 1997, cited in NA/182); "User manual for filterSQP", NA/181 (April 1998); "On the global convergence of an SLP-filter algorithm", Fletcher, Leyffer, Toint, NA/183 (Aug 1998; Optimization Online 2000/08/209); "A bundle filter method for nonsmooth nonlinear optimization", NA/195 (1999) (Scholar). [practice · primary]
- SQP integrated with branch-and-bound: NA/182 (Aug 1998), see S2. "User manual for MINLP BB" (Scholar, 1999). [practice · primary]
- Grothey, Leyffer, McKinnon, "A note on feasibility in Benders decomposition", NA/188 (Scholar, 1999). Skrifvars, Leyffer, Westerlund, Comput. Chem. Eng. 22(12) (1998) 1829-1835, DOI 10.1016/S0098-1354(98)00238-5. [practice · primary]
- Pattern [inferred]: method papers together with the solver codes behind them, written in Dundee; technical reports first, journals 2-4 years later.

**2000-2004 · Move to Argonne** (Argonne preprint series in use by Sept 2003: ANL/MCS-P1091-0903, arXiv math/0310357; the start year 2002 is secondary only).
- Filter theory in print: Fletcher and Leyffer, Math. Program. 91(2) (2002) 239-269, DOI 10.1007/s101070100244; Fletcher, Leyffer, Toint, SIAM J. Optim. 13(1) (2002) 44-59, DOI 10.1137/S105262340038081X; Fletcher, Gould, Leyffer, Toint, Wächter, SIAM J. Optim. 13(3) (2002) 635-659, DOI 10.1137/S1052623499357258; Gould, Leyffer, Toint, multidimensional filter, SIAM J. Optim. 15(1) (2004) 17-38, DOI 10.1137/S1052623403422637. [practice · primary]
- MPECs solved as NLPs: Fletcher and Leyffer, Optim. Methods Softw. 19(1) (2004) 15-40, DOI 10.1080/10556780410001654241; MacMPEC test collection (Scholar, 2000); counterexample to the penalty interior-point method (NA/208, 2002; arXiv math/0310357; Optim. Methods Softw. 20(4-5) (2005) 559-568, DOI 10.1080/10556780500140078). [practice · primary]
- Computational grids: Goux and Leyffer, "Solving large MINLPs on computational grids", Optim. Eng. 3(3) (2002) 327-346, DOI 10.1023/A:1021047328089. [practice · primary]
- Applications and teaching: GARCH volatility, SIAM Rev. 45(3) (2003) 485-503, DOI 10.1137/S003614450140011; value-at-risk with J.-S. Pang, Optim. Methods Softw. 19(5) (2004) 611-631, DOI 10.1080/10556780410001704911; Gould and Leyffer, "An introduction to algorithms for nonlinear optimization" (2003), DOI 10.1007/978-3-642-55692-0_4. [practice · primary]
- Pattern [inferred]: the filter work reaches print; MPECs become the second extension of his NLP base.

**2005-2009 · Argonne; adjunct professor at Northwestern (GT 2009 bio); Lagrange Prize 2006.**
- MPECs: interior methods with López-Calva and Nocedal, SIAM J. Optim. 17(1) (2006) 52-77, DOI 10.1137/040621065; local SQP convergence with Fletcher, Ralph, Scholtes, SIAM J. Optim. 17(1) (2006) 259-286, DOI 10.1137/S1052623402407382; electricity and NOx markets, Comput. Manag. Sci. 3(4) (2006) 307-330, DOI 10.1007/s10287-006-0020-1. [practice · primary]
- Filter retrospective (ANL/MCS-P1372-0906, 2006). Filter QP method with Friedlander, SIAM J. Sci. Comput. 30(4) (2008) 1706-1729, DOI 10.1137/060669930. [practice · primary]
- MINLP in team form: FilMINT preprint ANL/MCS-P1374-0906 (Scholar, 2006); "Branch-and-refine for mixed-integer nonconvex global optimization", ANL/MCS-P1547-0908 (Scholar, 2008); "Generalized Outer Approximation", Encyclopedia of Optimization (2009), DOI 10.1007/978-0-387-74759-0_211; "Applications and algorithms for mixed integer nonlinear programming", J. Phys. Conf. Ser. 180 (2009) 012014, DOI 10.1088/1742-6596/180/1/012014. [practice · primary]
- Sole-authored: multiobjective optimization via complementarity, INFORMS J. Comput. 21(2) (2009) 257-267, DOI 10.1287/ijoc.1080.0290. [practice · primary]
- Pattern [inferred]: sole-authored papers on his own lines; MINLP comes back as a team effort.

**2010-2014 · Argonne-centred MINLP team** (paper affiliations: Linderoth at Wisconsin on FilMINT 2010; Linderoth and Luedtke at Wisconsin and Munson at Argonne on Minotaur 2021; Mahajan "at Argonne" per Leyffer 2017).
- Consolidation: Lee and Leyffer (eds.), Mixed Integer Nonlinear Programming, IMA Vol. 154 (2012), DOI 10.1007/978-1-4614-1927-3; FilMINT, INFORMS J. Comput. 22(4) (2010) 555-567, DOI 10.1287/ijoc.1090.0373; Acta Numerica survey (2013), DOI 10.1017/S0962492913000032; branching rules, ACM J. Exp. Algorithmics 18 (2013), DOI 10.1145/2532568; TACO for mixed-integer optimal control (with Kirches), Math. Program. Comput. 5(3) (2013) 227-265, DOI 10.1007/s12532-013-0054-7. [practice · primary]
- MINLP applications: concrete design, SIAM J. Optim. 21(3) (2011) 833-863, DOI 10.1137/090778286; thermal insulation, Optim. Eng. 11(2) (2010) 185-212, DOI 10.1007/s11081-010-9109-z; oil-spill response, AIChE J. 57(12) (2011) 3555-3564, DOI 10.1002/aic.12536; distributed generation, Optim. Eng. 15(1) (2014) 167-197, DOI 10.1007/s11081-013-9226-6. [practice · primary]
- Argonne computational science: exascale failures, IJHPCA 28(2) (2014) 129-173, DOI 10.1177/1094342014522573; load balancing, SC 2012, DOI 10.1109/SC.2012.62; epidemics and cyber attacks, J. Complex Networks 1(2) (2013) 183-199, DOI 10.1093/comnet/cnt009. [practice · primary]
- Pattern [inferred]: team papers in alphabetical author order; widening into the lab's application areas.

**2015-2019 · Farkas Prize 2016.**
- Active-set method for SOC-constrained QP (with Goldberg), SIAM J. Optim. 25(3) (2015) 1455-1477, DOI 10.1137/140958025; two-level MIP for buildings, Comput. Optim. Appl. 65(1) (2016) 1-46, DOI 10.1007/s10589-016-9842-0. [practice · primary]
- Imaging with Wild and Di: SIAM J. Imaging Sci. 9(1) (2016) 1-23, DOI 10.1137/15M1021404; SIAM J. Sci. Comput. 41(3) (2019) B497-B521, DOI 10.1137/18M121993X. Inexact computing, arXiv 1610.02606. [practice · primary]
- PDE-constrained integer problems begin: Leyffer, Cay, Kouri, van Bloemen Waanders, "Mixed-integer PDE-constrained optimization", ANL/MCS-P5429-1015 (Nov 2015; known only from his 2017 reference list); Hahn, Leyffer, Zavala, gas networks (Optimization Online 2017/12/6381). [practice · primary]
- Minotaur preprint ANL/MCS-P8010-0817 (Optimization Online 2017/10/6275). Diesel, PV and battery system design with A. Newman, Optim. Eng. 18(3) (2017) 755-792, DOI 10.1007/s11081-017-9355-4. [practice · primary]
- Pattern [inferred]: junior first authors appear; applied lines with Wild and Di.

**2020-2024 · Senior roles** (Math. Program. B editor-in-chief 2017-2021 and SIAM President 2023-2024 [both secondary: Wikipedia]).
- Integer variables in function space: Gnegel et al., Math. Program. 188(2) (2021) 695-728, DOI 10.1007/s10107-021-01626-1; Leyffer, Manns, Winckler, Comput. Optim. Appl. 79(1) (2021) 193-221, DOI 10.1007/s10589-020-00262-3; Vogt, Leyffer, Munson, SIAM J. Sci. Comput. 44(1) (2022) B29-B50, DOI 10.1137/20M1315993; Leyffer and Manns, ESAIM COCV 28 (2022) 66, DOI 10.1051/cocv/2022059; Thünen, Leyffer, Sager, Optim. Control Appl. Methods 43(3) (2022) 867-883, DOI 10.1002/oca.2861; Hahn, Leyffer, Sager, Math. Program. 197(1) (2023) 147-190, DOI 10.1007/s10107-021-01733-z; Manns, Hahn, Kirches, Leyffer, Sager, arXiv 2202.07934. [practice · primary]
- MINLP software in print: Minotaur, Math. Program. Comput. 13(2) (2021) 301-338, DOI 10.1007/s12532-020-00196-1. [practice · primary]
- NLP globalization again: augmented-Lagrangian filter (with Vanaret), Math. Methods Oper. Res. 92(2) (2020) 343-376, DOI 10.1007/s00186-020-00713-X; the Uno solver, arXiv 2406.13454; funnel SQP, arXiv 2409.09208. Survey of nonlinear robust optimization, INFOR 58(2) (2020) 342-373, DOI 10.1080/03155986.2020.1730676. [practice · primary]
- Bilevel and MPEC: Kim, Leyffer, Munson (2020), DOI 10.1007/978-3-030-52119-6_12; Dandurand, Kim, Leyffer, SIAM J. Optim. 31(1) (2021) 702-726, DOI 10.1137/19M127611X; Kirches, Larson, Leyffer, Manns, SIAM J. Optim. 32(1) (2022) 75-99, DOI 10.1137/20M1370501. [practice · primary]
- Near machine learning and the lab's science: symbolic regression, INFORMS J. Comput. 35(6) (2023) 1383-1403, DOI 10.1287/ijoc.2022.0050; neural-network surrogates, Comput. Optim. Appl. 83(3) (2022) 759-800, DOI 10.1007/s10589-022-00404-9; binary optimal design of experiments, SIAM J. Sci. Comput. 44(2) (2022) B395-B427, DOI 10.1137/21M1404363; quantum control, Quantum 7 (2023) 892, DOI 10.22331/q-2023-01-04-892; convex black-box integer optimization, J. Glob. Optim. 80(2) (2021) 439-477, DOI 10.1007/s10898-020-00978-w. [practice · primary]
- Pattern [inferred]: arXiv-first; most papers have a junior first author.

**2025-2026** (details in §1.7): McCormick relaxations in function space plus a published Correction; funnel SQP in Math. Program.; filter methods for ADMM; MPEC B-stationarity; ADMM for integer topology optimization; experimental design; microscopy paths; quantum control. Pattern [inferred]: a late return to NLP globalization and MPECs, now through software architecture.

Reading of the trajectory [inferred from the periods above]: NLP globalization (filter, SQP) is the base. MINLP and MPECs are treated as extensions of it. From about 2010 the work becomes team MINLP software plus lab applications; from about 2015 the new frontier is integer variables in infinite dimensions (PDE- and ODE-constrained); in the 2020s he returns to NLP-solver design through modular software (Uno) and to MPECs. He states the base-and-extension logic himself (§2).

### 1.3 Authorship: from advisor papers to junior-first team papers

Author order in his field is often alphabetical, so a first-to-last shift cannot be read off positions directly. Of the 86 DBLP records (CoRR included) with 2 to 12 authors, 50 are fully alphabetical, 16 put one author first and the rest alphabetically (*junior first, alphabetical tail*), and 20 follow some other order. [practice · primary; classification computed on the DBLP record]

| Period | DBLP records (CoRR excluded) | sole | fully alphabetical | junior first, alphabetical tail | other order | mean authors (multi-author papers) |
|---|---|---|---|---|---|---|
| 1994-1999 | 2 | 0 | 2 | 0 | 0 | 2.0 |
| 2000-2004 | 9 | 1 | 6 | 1 | 1 | 2.9 |
| 2005-2009 | 9 | 3 | 6 | 0 | 0 | 2.8 |
| 2010-2014 | 17 (2 with more than 12 authors) | 0 | 10 | 0 | 5 | 3.7 |
| 2015-2019 | 11 | 0 | 4 | 3 | 4 | 4.4 |
| 2020-2024 | 20 | 0 | 10 | 5 | 5 | 4.2 |
| 2025-2026 | 10 | 0 | 5 | 4 | 1 | 3.4 |

What changes [practice · primary; interpretation inferred]:
- Sole-authored papers cluster in 2001-2009: SQP plus branch-and-bound (2001), the penalty interior-point counterexample (2005), multiobjective optimization via complementarity (2009), the encyclopedia entry (2009). There is no sole-authored DBLP record after 2009. A 2016 sole-authored report, "Augmented Lagrangian filter method" (ANL/MCS-P6082-1116, known from his own 2017 reference list), reappears as Leyffer and Vanaret (2020); that they are the same line is inferred from the title.
- From 2015 the non-alphabetical papers mostly put a junior author first and the seniors alphabetically after: Lin (2016), Mahajan (Minotaur, 2021), Yang (2021, 2022), Vogt (2022, 2025), Fei (2023, 2025, with Siqian Shen last), Medlin (2024, 2025).
- He is last outside alphabetical order in a few applied papers: Goldberg et al. 2021 (DOI 10.1007/s10589-021-00268-5), Aretz et al. (arXiv 2509.15961), Lu et al. (ISBI 2026, DOI 10.1109/ISBI61048.2026.11515614).
- The only DBLP item where he is first out of alphabetical order is the position paper "Doing Moore with Less" (arXiv 1610.02606, 2016).

### 1.4 Collaboration network and likely students and postdocs

Clusters [practice · primary; grouping inferred]:
1. Dundee and the filter (1994-2012): Roger Fletcher (PhD advisor [observed: MGP; Farkas 2016 citation]), Philippe Toint, Nick Gould, Andreas Wächter, Chungen Shen.
2. MPECs and complementarity (2002-2010): Danny Ralph, Stefan Scholtes, Jorge Nocedal, Gabriel López-Calva, Jong-Shi Pang, Benjamin Hobbs, Yihsu Chen, Todd Munson.
3. MINLP algorithms and software (2006-2021): Jeff Linderoth, Jim Luedtke, Ashutosh Mahajan, Pietro Belotti, Christian Kirches, Kumar Abhishek, Pierre Bonami, Jon Lee, Andreas Wächter.
4. Argonne computational science (2011-2026): Todd Munson (his most frequent coauthor), Stefan Wild, Jeffrey Larson, Prasanna Balaprakash, Zichao (Wendy) Di, Yuri Alexeev, HPC groups (Snir et al.).
5. Mixed-integer optimal control and PDE-constrained integer problems (2013-2026): Christian Kirches, Sebastian Sager, Mirko Hahn, Paul Manns, Ryan Vogt, Bart van Bloemen Waanders, Armin Fügenschuh.
6. Applications with Alexandra Newman (Colorado School of Mines): concrete design (2011), distributed generation (2014), diesel-PV-battery systems (2017).
7. Recent NLP and MPEC work: Charlie Vanaret, David Kiessling, Armin Nurkanović, Robert Baraldi.

Junior collaborators. A national-laboratory researcher has no formal PhD students of his own; MGP lists "No students known". [observed · secondary]

| Person | Evidence | Status |
|---|---|---|
| Kumar Abhishek | "With a student of Jeff Linderoth's, we built FilMINT" (Leyffer 2017, p. 5); FilMINT first author | [stated · primary]: Linderoth's student, co-supervised in practice |
| Ashutosh Mahajan | Minotaur "was developed by Ashutosh Mahajan at Argonne together with Jeff Linderoth, Jim Luedtke, and Todd Munson" (2017, p. 6); at IIT Bombay by 2021 (Springer affiliation); top Minotaur committer (554 commits) | [stated + practice · primary]; his Argonne role (postdoc?) not stated |
| Chungen Shen | the nonmonotone filter was "developed by Chungen Chen at Argonne" (2017, p. 5; the article's own reference [38] spells "C. Shen") | [stated · primary]; role not stated |
| Paul Manns | Argonne affiliation on the 2021 Comput. Optim. Appl. paper; TU Dortmund on the 2025 Math. Program. paper | [practice · primary]; postdoc role inferred |
| Charlie Vanaret | coauthor of the 2020 augmented-Lagrangian filter and the 2024 Uno and funnel papers; lead Uno developer (2,337 commits) | [practice · primary]; role inferred |
| Noam Goldberg, Fu Lin, Youngdae Kim, Ahmed Attia, Zichao Di, Dominic Yang, Ryan Vogt, Karen Medlin, Harsh Choudhary; Minotaur committers Meenarli Sharma (423) and Prashant Palkar (252) | junior first authors or code contributors on joint work | [inferred] from author position and coauthorship only |
| Mirko Hahn (Magdeburg), Xinyu Fei (Siqian Shen last author), David Kiessling, Armin Nurkanović | students of other groups who wrote papers with him | [inferred]; hosting or co-advising not verified (agent 04) |

### 1.5 Usual venues

- Theory and algorithms: SIAM J. Optim., Math. Program. (including Series B), Comput. Optim. Appl., Optim. Methods Softw., J. Optim. Theory Appl. (2026). [practice · primary]
- Computation and software: INFORMS J. Comput., Math. Program. Comput., ACM J. Exp. Algorithmics, ACM Trans. Math. Softw. [practice · primary]
- Scientific computing and applications: SIAM J. Sci. Comput., SIAM J. Imaging Sci., Optim. Eng., AIChE J., Optics Express, SC, IPDPS workshops, eScience, CCGRID, ISBI, Quantum, ACM Trans. Quantum Comput. [practice · primary]
- Surveys and expository pieces: Acta Numerica (2013), INFOR (2020), Encyclopedia of Optimization (2009), Frontiers in Numerical Analysis (2003), SIAG/OPT Views-and-News (2003 MPCC note; 2010 oil-spill note with F. You), Oberwolfach Reports ("The return of the active set method", 2005), INFORMS OS Today (2017). [practice · primary; non-DOI items checked on Scholar]
- Preprint outlets: Dundee NA reports (1990s), the ANL/MCS-P series (2003 onward), Optimization Online (from 2000), arXiv (mostly from 2019). [practice · primary]

### 1.6 Most-cited works (Scholar, 2026-10-10; Crossref `is-referenced-by` counts where fetched)

| Rank | Work | Identifier | Scholar | Crossref |
|---|---|---|---|---|
| 1 | Fletcher and Leyffer, "Nonlinear programming without a penalty function", Math. Program. 91(2) (2002) 239-269 | DOI 10.1007/s101070100244 | 1449 | 651 |
| 2 | Belotti, Kirches, Leyffer, Linderoth, Luedtke, Mahajan, "Mixed-integer nonlinear optimization", Acta Numerica 22 (2013) 1-131 | DOI 10.1017/S0962492913000032 | 1138 | 640 |
| 3 | Fletcher and Leyffer, "Solving mixed integer nonlinear programs by outer approximation", Math. Program. 66 (1994) 327-349 | DOI 10.1007/BF01581153 | 982 | 546 |
| 4 | Lee and Leyffer (eds.), Mixed Integer Nonlinear Programming, IMA Vol. 154 | DOI 10.1007/978-1-4614-1927-3 | 643 | 169 |
| 5 | Fletcher, Leyffer, Toint, "On the global convergence of a filter--SQP algorithm", SIAM J. Optim. 13(1) (2002) 44-59 | DOI 10.1137/S105262340038081X | 622 | 264 |
| 6 | Snir et al., "Addressing failures in exascale computing", IJHPCA 28(2) (2014) | DOI 10.1177/1094342014522573 | 543 | not fetched |
| 7 | Fletcher, Gould, Leyffer, Toint, Wächter, "Global convergence of a trust-region SQP-filter algorithm for general nonlinear programming", SIAM J. Optim. 13(3) (2002) 635-659 | DOI 10.1137/S1052623499357258 | 474 | not fetched |
| 8 | Fletcher, Leyffer, Ralph, Scholtes, "Local convergence of SQP methods for mathematical programs with equilibrium constraints", SIAM J. Optim. 17(1) (2006) 259-286 | DOI 10.1137/S1052623402407382 | 393 | not fetched |
| 9 | Leyffer, "Integrating SQP and branch-and-bound for mixed integer nonlinear programming", Comput. Optim. Appl. 18(3) (2001) 295-309 | DOI 10.1023/A:1011241421041 | 360 | 190 |
| 10 | Fletcher and Leyffer, "Numerical experience with lower bounds for MIQP branch-and-bound", SIAM J. Optim. 8(2) (1998) 604-616 | DOI 10.1137/S1052623494268455 | 308 | 151 |

The software manuals have their own citation records: "User manual for filterSQP" (NA/181, 1998) 200; "User manual for MINLP BB" (1999) 96; MacMPEC (2000) 83. The thesis (Scholar: 1993) has 174 and the 2006 filter history 119. [observed · primary database]. Scholar and Crossref differ by a factor of about 2 because they count different things.

### 1.7 Recent works (about the last 12-18 months)

- Kiessling, Leyffer, Vanaret, "A unified funnel restoration SQP algorithm", Math. Program. 217(1) (2026) 323-367, DOI 10.1007/s10107-025-02284-3 (arXiv 2409.09208). Abstract: "We prove global convergence of the trust-region funnel SQP method, building on known results from filter methods." [practice · primary]
- Leyffer and Manns, "McCormick envelopes in mixed-integer PDE-constrained optimization", Math. Program. 218(1) (2026) 245-290, DOI 10.1007/s10107-024-02181-1 (arXiv 2406.07891), with its Correction, Math. Program. 218(1) (2026) 591-592, DOI 10.1007/s10107-026-02330-8. See S5. [practice · primary]
- Baraldi, Leyffer, Wild, "Using Filter Methods to Guide Convergence for ADMM, with Applications to Nonnegative Matrix Factorization Problems", J. Optim. Theory Appl. 209(2) (2026) 66, DOI 10.1007/s10957-026-02983-7. [practice · primary]
- Nurkanović and Leyffer, "A Globally Convergent Method for Computing B-stationary Points of Mathematical Programs with Equilibrium Constraints", arXiv 2501.13835 (v1 23 Jan 2025; v5 8 Sep 2026 with the comment "Final accepted version"; venue not named on arXiv). [practice · primary]
- Choudhary, Leyffer, Yang, "An Alternating Direction Method of Multipliers for Topology Optimization", arXiv 2509.19888 (v2 6 Oct 2026). Yang, Leyffer, Bakenhus, "Augmentation Algorithms for Integer Programs with Total Variation-like Regularization", arXiv 2508.05822. [practice · primary]
- Vanaret and Leyffer, "Implementing a unified solver for nonlinearly constrained optimization", arXiv 2406.13454 (v2 9 Nov 2025: "Submitted to Mathematical Programming Computation journal (first revision)"). [practice · primary]
- Applications: Lu, Lynn, Du, Di, Leyffer, ISBI 2026, DOI 10.1109/ISBI61048.2026.11515614 (extended version arXiv 2509.01869); Aretz, Lynn, Willcox, Leyffer, arXiv 2509.15961; Attia, Leyffer, Munson, SIAM/ASA J. Uncertain. Quantif. 13(2) (2025) 744-774, DOI 10.1137/24M1667543; Medlin, Leyffer, Raghavan, IJCNN 2025, DOI 10.1109/IJCNN64981.2025.11227944, and arXiv 2506.11315; Fei, Brady, Larson, Leyffer, Shen, INFORMS J. Comput. 37(1) (2025) 86-106, DOI 10.1287/ijoc.2024.0560, and ACM Trans. Quantum Comput. 6(1) (2025), DOI 10.1145/3670416; Vogt, Leyffer, Munson, Comput. Optim. Appl. 90(2) (2025) 337-360, DOI 10.1007/s10589-024-00644-x. [practice · primary]

### 1.8 Software and test sets as part of the output

| Artifact | Evidence | Tag |
|---|---|---|
| filterSQP (Fletcher and Leyffer) | manual NA/181, April 1998 (reference [10] in NA/182); NEOS: "filter was developed by Roger Fletcher and Sven Leyffer"; COIN-OR keeps only a build harness, `coin-or-tools/ThirdParty-FilterSQP` (EPL-1.0, last push 2020-02-15); licence of the source itself not checked | [practice · primary] |
| MINLP_BB, served on NEOS as "MINLP" | NEOS: "The software package MINLP solves mixed integer nonlinear programming (MINLP) problems by branch-and-bound." The NLP relaxations "are solved using filterSQP" | [practice · primary] |
| Public MINLP test problems (1998) | "The test-problems are available at http://www.mcs.dundee.ac.uk:8080/~sleyffer/MINLP_TP/." (NA/182, p. 10) | [practice · primary] |
| MacMPEC, an AMPL collection of MPECs (2000) | Scholar; his 2017 reference [27] | [practice · primary] |
| FilMINT | "combines the MINTO branch-and-cut framework for MILP with filterSQP" (abstract, INFORMS J. Comput. 2010) | [practice · primary] |
| TACO, AMPL extension for mixed-integer optimal control (with Kirches) | Math. Program. Comput. 5(3) (2013), DOI 10.1007/s12532-013-0054-7 | [practice · primary] |
| Minotaur | GitHub `coin-or/minotaur`, created 2016-06-01, last push 2026-08-10, about 1,674 commits on master. Committers: ashutoshmahajan 554, meenarli 423, ppalkar 252, mustafa712 238, and others. The commit search finds no commit authored under the name "Leyffer" (history before 2016 is not visible) | [practice · primary] |
| Uno (lead developer: Vanaret) | GitHub `cvanaret/Uno`, created 2021-09-29, MIT licence, 513 stars on 2026-10-10. Ten commits authored "leyffer" on 15-17 Oct 2018, merged from `gitlab.com:argonot/argonot` (the predecessor repository), with messages including "Sven's attempt at writing C++ code", "changes on f77", "augLag version hs015.mod" and "added comments by Sven" | [practice · primary]; reading this as a Fortran-era author prototyping in a C++ code base is inferred |

### 1.9 Failures, corrections, abandoned paths and negative results

| # | When | What | Source | Tag |
|---|---|---|---|---|
| F1 | 1994 | Worst case of outer approximation: "an example is given for which it visits all integer assignments", and "This behaviour leads us to include curvature information into the relaxed MILP master problem, giving rise to a new quadratic outer approximation algorithm." | abstract, DOI 10.1007/BF01581153 | [practice · primary] |
| F2 | 2008, reported 2017 | The 1994 proof was corrected by others: "Later, Bonami et al. corrected our convergence proof [4], and Pierre developed a much nicer example that showed that outer approximation can take an exponential number of iterations [26]." Ref. [4] is Bonami et al., Discrete Optim. 5(2) (2008) 186-204, DOI 10.1016/j.disopt.2006.10.011 (Grossmann is a coauthor); ref. [26] is Hijazi, Bonami, Ouorou, INFORMS J. Comput. 26(1) (2014) 31-44, DOI 10.1287/ijoc.1120.0545 | Leyffer 2017, p. 5 | [stated · primary] |
| F3 | 1996-2002 | Early filter features dropped: "The initial filter method contained features, such as the NW/SE corner rule and unblocking, that were shown to be redundant in the subsequent convergence analysis." The prize committee concurs: "The earlier algorithm is simplified" (2006 Lagrange citation) | 2006 history, p. 5; MOS citation | [stated + observed · primary] |
| F4 | late 1990s | A hoped-for property abandoned: "Early on, we conjectured that filter methods may be able to avoided the Maratos effect." Then "the following example shattered the hope that filter methods can avoid the Maratos effect in general". In 2017: "Originally, we had believed that filter methods avoid the Maratos effect [34] ... However, Nick and Philippe developed an example that showed that filter methods also suffer from the Maratos effect" | 2006, p. 6; 2017, p. 5 | [stated · primary] |
| F5 | 1998-2002, reported 2017 | Errors in the early filter proof: the SLP proof "was later generalized to sequential quadratic programming (SQP) methods in [21, 15] together with Nick Gould and Andreas Wächter, who corrected many errors in the early proof." Also: "One undesirable assumption in [10] is the need for global solution to the QP subproblem (2.1)." | 2017, p. 4; 2006, p. 6 | [stated · primary] |
| F6 | 1998 | His own method fails on a nonconvex problem: "For the nonconvex problem FEEDLOC, Algorithm 2 did not find an integer feasible point." He ends: "However, better heuristics for nonconvex MINLP problems remain an open problem." Table 3 also shows the new method slower on BATCH (14.8 s against 8.9 s for nonlinear branch-and-bound) | NA/182, p. 11 | [practice · primary] |
| F7 | 1998 to 2001 | Headline claim softened from "a factor of about 3 improvement" (NA/182 abstract, p. 1) to "a factor of up to 3 improvement" (journal abstract). The reason is not documented | NA/182; Springer abstract | [practice · primary] |
| F8 | 2002-2005 | Counterexample to others' theory: "This paper presents a small example for which PIPA converges to a nonstationary point, providing a counterexample to the established theory." | arXiv math/0310357 | [practice · primary] |
| F9 | 2006, reported 2017 | Pitfalls in MPEC reformulation: "In [20] we give an example that shows that an SQP method applied to a nonlinear complementarity constraint can converge to a nonstationary point." A colleague's SQPEC idea was dropped: "Remarkably, this approach can be shown to fail for MPECs as demonstrated by the following example" | 2017, p. 9 | [stated · primary] |
| F10 | 2026 | Published Correction to the 2025 McCormick paper: "We correct two mistakes in the paper [S. Leyffer and P. Manns, Math. Prog. 2025]." (1) Assumption 2.7 2. "lacks the box constraints on w"; without them, a unique PDE solution for every w "is unrealistic given that (2) may become an eigenvalue problem for suitable w". (2) In Proposition 2.14 the limsup inequality had been derived with a feasibility argument for the wrong PDE; the corrected statement adds a compatibility assumption (paraphrase). Who found the errors is not stated | DOI 10.1007/s10107-026-02330-8 (open access) | [practice · primary] |
| F11 | 2006 to 2017 | Stance revised. 2006: "We believe filter methods achieve this goal" (safeguards that interfere little with Newton's method, p. 2). 2017: "At this point, I do not believe that there exists a big difference between filter methods and modern penalty function methods, and the choice of method is really a question of personal preference." (p. 5) | 2006; 2017 | [stated · primary] |
| F12 | various | Lines with no later papers in DBLP or arXiv: grid-computing branch-and-bound (2002), HPC load balancing (2012-2015), inexact computing (2016), network epidemics and cyber response (2011-2015). Reasons not documented | DBLP, arXiv | [inferred] from absence |
| F13 | 1997-2000 | No rejected paper found in the public record. The filter paper took about 34 months from submission to acceptance (received 17 Oct 1997, accepted 17 Aug 2000, online 3 Sep 2001); why is not documented | Springer article history | [practice · primary] |

### 1.10 Era and resource context

- Dundee, early 1990s to about 2001 (PhD, then EPSRC-funded research; the postdoc title is secondary): the methods came with code he and Fletcher wrote themselves. "Nonlinear branch-and-bound and Algorithm 2 have been implemented in Fortran 77 using filterSQP [10] as the underlying NLP solver." Hardware: "All runs were performed on a SUN SPARCstation 4 with 128 Mb memory, using the compiler options -r8 -O and SUN's f77 Fortran compiler." The test set was small (8 MINLPs with 6 to 142 variables) and read from SIF files "plus an additional file to identify the integer variables". Two-author papers; technical reports came first. (NA/182, p. 10) [practice · primary]
- Argonne, from the early 2000s, on DOE Office of Science ASCR funding (contract W-31-109-ENG-38 in the 2006 history; DE-AC02-06CH11357 in the 2012 Acta preprint and the 2017 article): computational grids (Goux and Leyffer 2002 consider "a parallel implementation of nonlinear branch-and-bound on a computational grid or meta-computer"); multi-institution teams with Wisconsin, Northwestern and German groups (Magdeburg, Dortmund, Duisburg-Essen affiliations on the papers); C++ frameworks built mainly by postdocs and collaborators (Minotaur, Uno), with Leyffer as co-designer and coauthor. [practice · primary; the co-designer role is inferred from authorship plus the commit record]
- Senior period (Farkas Prize 2016; editorial and society roles, secondary): applications driven by the lab's science programmes (imaging, quantum control, experimental design, event-generator tuning, power grids); papers led by juniors; arXiv-first with several versions (the McCormick paper had 5 arXiv versions). [practice · primary; roles secondary]
- Portability [inferred]: the late-career breadth rests on lab-wide collaboration and on postdocs who carry the software, which a single early-career researcher cannot copy. The Dundee-era pattern (own the code, small decisive test sets, reports first) needs no such resources.

---

## 2. What he presents as his main work, and what others single out

- [stated · primary] In his own retrospective (the 2017 Farkas article) he picks three topics: "The remainder of this article provides a personal view of three topics in nonlinear optimization. Starting with filter methods for global convergence of nonlinear solvers, we consider two extensions of nonlinear optimization, namely mixed-integer nonlinear programming (MINLP), and mathematical programs with equilibrium constraints." (p. 3). He frames the career as collaborative: "Throughout my career, I had the great fortune to work with some of the brightest optimizers, and this article is a tribute to their influence, guidance, and inspiration." (p. 3)
- [stated in a third-person bio whose author is not given; likely supplied by him · primary] The Georgia Tech seminar page (10 Mar 2009, talk "A Tale of Two Problems: Integer and Nonlinear Optimization") gives the same base-and-extension logic: "Sven is interested in the development of reliable methods for solving large-scale nonlinear optimization problems and in the implementation and analysis of filter type algorithms. This forms the basis from which he is extending nonlinear optimization methodologies to emerging areas such as mixed-integer nonlinear optimization and optimization problems with complementarity constraints."
- [practice · primary] He co-wrote a historical retrospective of filter methods (2006) and an invited 131-page MINLP survey (2013): both show which lines he considers worth consolidating.
- [observed · primary] The 2006 Lagrange Prize in Continuous Optimization (MOS and SIAM) went to Fletcher, Leyffer and Toint "for the papers" Fletcher and Leyffer, Math. Program. 91(2) (2002), and Fletcher, Leyffer and Toint, SIAM J. Optim. 13 (2002) 44-59. The citation: "In the development of nonlinear programming over the last decade, an outstanding new idea has been the introduction of the filter." and "Currently, some of the most effective nonlinear optimization codes are based on filter methods."
- [observed · primary] The 2016 INFORMS Optimization Society Farkas Prize was "for his fundamental contributions to the design and analysis of computational algorithms for large-scale nonlinear optimization and mixed-integer nonlinear optimization problems". The citation singles out the thesis extension of outer approximation, then "Subsequently, he laid the ground for the first SQP-based branch and bound method for MINLP", the filter methods, MPECs solved as NLPs, and the software ("filter", MINLP, FilMINT, "the very ambitious project MINOTAUR"). Committee: Ariela Sofer (chair), Ignacio Grossmann, Ted Ralphs, Alex Shapiro.
- [observed · primary] A Dundee press release (June 2006) on the Lagrange Prize says "Professor Leyffer was at the University of Dundee when the research was carried out." and quotes Fletcher: "Discovering the filter idea was a real "eureka" moment for me and I am very gratified by the interest that it has generated."

---

## 3. Signature works

| # | Work | Why selected |
|---|---|---|
| S1 | Fletcher and Leyffer (1994), outer approximation generalized | rank 3 by citations; the PhD work; named first by the Farkas committee and by him in 2017 |
| S2 | Leyffer (2001; report NA/182, 1998), SQP integrated with branch-and-bound | his sole-authored MINLP method; "the first SQP-based branch and bound method for MINLP" (Farkas 2016); the full report is public, so its origin and failures are documented first-hand |
| S3 | Fletcher and Leyffer (2002), the filter method, with the 2002 convergence papers | rank 1 by citations; Lagrange Prize 2006; the first of his "three topics" |
| S4 | Belotti et al. (2013), Acta Numerica survey, read with FilMINT (2010) and Minotaur (2021) | rank 2 by citations; marks the turn to Argonne team science; carries the software line |
| S5 | Leyffer and Manns (2026), McCormick envelopes in mixed-integer PDE-constrained optimization, with the 2026 Correction, as anchor of the PDE-constrained integer line (2015-2026) | the most recent turn, announced in his 2017 outlook; includes the one published correction found |

### S1. Outer approximation generalized (1994)

Identifier: Fletcher, R., Leyffer, S., "Solving mixed integer nonlinear programs by outer approximation", Mathematical Programming 66(1-3) (1994) 327-349, DOI 10.1007/BF01581153. Received 15 June 1992; issue August 1994. Full text: not read (abstract and article history read on the publisher page).

- Origin. [stated · primary] "During my PhD studies with Roger Fletcher, we generalized outer approximation by Duran and Grossmann [13], see [16], "simplified" its convergence analysis, and provided a one-dimensional example where outer approximation visits all integer points." (2017, p. 5). The base algorithm is Duran and Grossmann, Math. Program. 36(3) (1986) 307-339, DOI 10.1007/BF02592064. [observed · primary] Farkas 2016: "In his PhD thesis under the direction of the late Roger Fletcher, Leyffer made significant contributions in extending the outer approximation method developed by Duran and Grossmann ...". Who proposed the topic, advisor or student: not documented, and no inference is made.
- Why then. [inferred] By 1992 OA covered only "a class of MINLPs that are linear in the integer variables" (abstract). Fletcher's own toolbox, exact penalty functions and nonsmooth (convex composite) optimization, is exactly what the abstract's last two sentences deploy: an approach "in which exact penalty functions are used to solve the NLP subproblems", and theory for "a large class of nonsmooth MINLPs based on the use of convex composite functions and subdifferentials". (Fletcher's "Practical Methods of Optimization", 2nd ed., 1987, is cited in NA/182.) Basis: the abstract's wording only; there is no first-person account of the timing.
- Key insight. [practice · primary, abstract] "Their idea is generalized by treating nonlinearities in the integer variables directly, which allows a much wider class of problem to be tackled, including the case of pure INLPs. A new and more simple proof of finite termination is given and a rigorous treatment of infeasible NLP subproblems is presented which includes all the common methods for resolving infeasibility in Phase I."
- Minimum evidence. [practice · primary] A worst case: "The worst case performance of the outer approximation algorithm is investigated and an example is given for which it visits all integer assignments." (abstract). In 2017 he calls it "a one-dimensional example". Numerical experiments in the paper: not read.
- Abandoned paths. [practice · primary] The abstract offers two routes for infeasible subproblems: the Phase-I treatment and "An alternative approach ... in which exact penalty functions are used". Which route later practice kept: not checked. The quadratic OA variant ("a new quadratic outer approximation algorithm") answered the worst case; its later uptake: not checked. The "simplified" proof was later corrected (F2). [stated · primary]
- Reception. Scholar 982, Crossref 546. Others later corrected the proof (Bonami et al. 2008) and sharpened the worst case to exponentially many iterations (Hijazi, Bonami, Ouorou 2014) [stated by Leyffer 2017, p. 5]. The Farkas committee (2016, with Grossmann as a member) credits the work with "a rigorous treatment of infeasibilities and convergence proof to the methodology" [observed · primary]. He kept the topic as his own: the encyclopedia entry "Generalized Outer Approximation" (2009, DOI 10.1007/978-0-387-74759-0_211; content not read) and the "multitree" class of the Acta survey (S4). [practice · primary]
- Method it shows (cross-index §4): M1 redesign driven by a counterexample (the worst case leads to curvature in the master problem); M7 carrying NLP theory (exact penalties, nonsmooth analysis) into an MINLP decomposition; M5 acknowledging later corrections of his own proof in public.
- Era and resources: Dundee PhD; two authors, the advisor first by alphabet; computational set-up not read.

### S2. SQP integrated with branch-and-bound (report 1998, journal 2001)

Identifiers: Leyffer, S., "Integrating SQP and branch-and-bound for mixed integer nonlinear programming", Computational Optimization and Applications 18(3) (2001) 295-309, DOI 10.1023/A:1011241421041. First version: University of Dundee Numerical Analysis Report NA/182, dated August 6, 1998 (Optimization Online 2000/08/208; read: pp. 1-2 and 10-12).

- Origin. [stated · primary] "The basic idea underlying the new approach is to branch early – possibly after a single QP iteration of the SQP solver. This idea was first presented by Borchers and Mitchell [1]. The present paper improves on their idea in a number of ways:" (NA/182, p. 2). The source idea is Borchers and Mitchell, Comput. Oper. Res. 21(4) (1994) 359-367, DOI 10.1016/0305-0548(94)90024-8. He also positions the work against the nearest competitor: "The ideas presented in this paper have a similar motivation as a recent algorithm by Quesada and Grossmann [21]. ... The difference to the approach considered here is that Quesada and Grossmann still solve NLP problems at some nodes, whereas the new solver presented here usually solves one quadratic programming (QP) problem at each node." (p. 2; Quesada and Grossmann, Comput. Chem. Eng. 16(10-11) (1992) 937-947, DOI 10.1016/0098-1354(92)80028-8)
- Why then. [stated · primary] He reads the field's habit of decomposition as a by-product of how software was packaged: "Classical methods for the solution of (P) “decompose” the problem by separating the nonlinear part from the integer part. This approach is largely due to the existence of packaged software for solving Nonlinear Programming (NLP) and Mixed Integer Linear Programming (MILP) problems." (p. 2). What had just become available was his own solver: "In [1] two QP problems are solved before branching. This restriction is due to the fact that a packaged SQP solver is used. By using our own solver we are able to remove this unnecessary restriction, widening the scope for early branching." (p. 2). The filterSQP manual is dated April 1998 (NA/181). [practice · primary]
- Key insight. [stated · primary] Interleave the tree search with the iterations of the NLP solver: "In Section 3 it is shown that there is no need to compute a lower bound if the linearizations in the SQP solver are interpreted as cutting planes." and "A new heuristic for deciding when to branch early is introduced which does not rely on a fixed parameter, but takes the second order rate of convergence of the SQP solver into account when deciding whether to branch or continue with the SQP iteration." (p. 2)
- Minimum evidence. [practice · primary] Eight problems, from process synthesis to trim loss, with 6 to 142 variables (Table 2, p. 11); the test set was posted on the web (p. 10). Result: "For the largest problem, Algorithm 2 is is 3 times faster than nonlinear branch-and-bound." (p. 11). The implementation touches the NLP code as little as possible: "The implementation of Algorithm 2 uses a callback routine that is invoked after each step of the SQP method. ... The use of this routine has kept the necessary changes to filterSQP to a minimum." (p. 10)
- Abandoned paths and failures. [stated · primary] Borchers and Mitchell's Lagrangian-dual lower bound is replaced by reading the SQP linearizations as cutting planes (p. 2). A "nonconvex mode" guards against wrong fathoming: "This heuristic is motivated by the success of nonlinear branch-and-bound in solving some nonconvex MINLP problems. It ensures that a node is only fathomed if it would have been fathomed by nonlinear branch-and-bound." (p. 10). [practice · primary] The method fails on the nonconvex FEEDLOC instance and is slower on BATCH, and the open problem is stated on p. 11 (F6); the headline claim softened between report and journal (F7).
- Reception. Report August 1998, Optimization Online August 2000 (updated May 2001), journal March 2001. Scholar 360, Crossref 190. The solver became NEOS "MINLP" [practice · primary]. The NEOS page, whose author is not named, says that on nonconvex problems "the solver is more robust than outer approximation or Benders Decomposition, which usually cut away large parts of the feasible region" [observed · primary]. The Farkas committee calls this the ground for "the first SQP-based branch and bound method for MINLP" [observed · primary].
- Method it shows: M3 own the solver and integrate at the iteration level; M2 a small, public, decisive test set; M5 report where the method fails; positioning by an enumerated list of improvements over the closest prior work. [labels inferred]
- Era and resources: sole author, EPSRC-funded; Fortran 77, a 128 MB workstation, SIF-format inputs (§1.10).

### S3. The filter method (1997 report; journal 2002) and its convergence theory

Identifiers: Fletcher, R., Leyffer, S., "Nonlinear programming without a penalty function", Mathematical Programming 91(2) (2002) 239-269, DOI 10.1007/s101070100244 (first as Dundee report NA/171, September 1997, cited in NA/182). Companions: Fletcher, Leyffer, Toint, "On the global convergence of a filter--SQP algorithm", SIAM J. Optim. 13(1) (2002) 44-59, DOI 10.1137/S105262340038081X; Fletcher, Gould, Leyffer, Toint, Wächter, SIAM J. Optim. 13(3) (2002) 635-659, DOI 10.1137/S1052623499357258. The full text of the 2002 paper was not read; its abstract and history were, and the 2006 retrospective and 2017 article were read in full.

- Origin. [stated · primary] "Roger Fletcher had been unhappy with the performance of classical penalty functions for NLP, and had been playing around with methods that instead use the Lagrangian as a merit function within a tolerance tube around the constraints [43], similar to the funnel ideas [24] developed later by Nick Gould and Philippe Toint. Our filter method [17] grew out of these early experiments." (2017, pp. 3-4; ref. [43] is C. Zoppke-Donaldson's Dundee PhD thesis, "A Tolerance-Tube Approach to Sequential Quadratic Programming with Applications"). "NLP filter methods were first proposed by Fletcher in a plenary talk at the SIAM Optimization Conference in Victoria in May 1996; the methods are described in [8]." (2006, p. 5). [observed · primary] Fletcher on the discovery: "Discovering the filter idea was a real "eureka" moment for me and I am very gratified by the interest that it has generated." (Dundee release, June 2006). So the idea is Fletcher's. Leyffer's own share (the filterSQP implementation, the experiments, the theory) cannot be separated out from the sources read.
- Why then. [stated · primary] The motivating observation: "Yet we have noticed that the unmodified SQP method is able to quickly solve a large proportion of test problems without the need for modifications to induce global convergence." (2006, p. 2). [inferred] A working SQP code and competitor codes (LANCELOT and an Sl1QP implementation, named in the abstract) made a numerical comparison possible at once.
- Key insight. [practice · primary, abstract] "The aim of the present work is to promote global convergence without the need to use a penalty function. Instead, a new concept of a “filter” is introduced which allows a step to be accepted if it reduces either the objective function or the constraint violation function." [stated · primary] The design principle behind it: "Our goal therefore is the development of global optimization safeguards that interfere as little as possible with Newton's method. We believe filter methods achieve this goal." (2006, p. 2)
- Minimum evidence. [practice · primary] The numbers came first: "Numerical tests on a wide range of test problems are very encouraging and the new algorithm compares favourably with LANCELOT and an implementation of Sl1QP." (abstract; report September 1997). The first convergence proof came later, for an SLP variant: "The first global convergence proof of a filter method was given in [11] for a sequential linear programming (SLP) method. This proof was later generalized to SQP methods in [10]." (2006, p. 5; [11] is NA/183, August 1998). He still prefers that early proof: "I still regard this as the most easily understood proof." (2017, p. 4). That numerics preceded theory by about a year is inferred from the report dates. He still cites NA/183 as a report in 2017, so it was probably never published in a journal [inferred, not verified].
- Abandoned paths. [stated · primary] Redundant features dropped (F3); the hope of avoiding the Maratos effect dropped (F4). In 2006 the authors preferred second-order corrections: "We currently prefer to use SOC steps to obtain fast local convergence because this approach allows us to keep the original filter definition with f (x), rather than the Lagrangian L(x, y)." (2006, p. 7); in 2017 Leyffer writes that "a more appealing approach is to use a nonmonotone filter" (p. 5). The need for globally solved QP subproblems, called "undesirable" (2006, p. 6), was later removed in the trust-region SQP-filter variant: "the algorithm in [6] removes the need for a global solution of the QP" (2006, p. 7). Coauthors corrected errors in the early proof (F5).
- Reception. Received 17 Oct 1997, accepted 17 Aug 2000, issue January 2002 (F13). Lagrange Prize 2006 [observed · primary]: "The paper includes extensive numerical results, which attest to the potential of the algorithm. The second paper complements the first, using novel techniques to provide a satisfying proof of correctness for the filter approach in its original SQP context. The earlier algorithm is simplified, and in so doing the analysis plays its natural role with respect to algorithmic design." Scholar 1449, his most cited work. Uptake in other solvers: "Wächter and Biegler [30] have successfully incorporated a filter mechanism in the NLP solver IPOPT [31]." (2006, p. 9) [stated · primary]. Spread beyond NLP: "Filter methods were initially designed for nonlinear programming problems but have quickly become popular in other areas such as nonlinear equations, nonsmooth optimization, and derivative-free methods." (2006, p. 13) [stated · primary]. His own later deflation of the claim (F11) sits beside 2024-2026 papers (funnel SQP, filter-guided ADMM) that still build on the idea. [practice · primary]
- Method it shows: M2 numerics first, proof second; M10 minimal interference with Newton's method as the design criterion; M1 counterexamples that kill a hoped-for property (Maratos); simplification of the algorithm through the convergence analysis (observed by the Lagrange committee); M8 writing the field's history himself (2006).
- Era and resources: Fletcher's group in Dundee; 2-5 authors; the 34-month review shows the time scale of journals at the time.

### S4. The MINLP survey (2013) and the team software line (FilMINT 2010, Minotaur 2021)

Identifiers: Belotti, P., Kirches, C., Leyffer, S., Linderoth, J., Luedtke, J., Mahajan, A., "Mixed-integer nonlinear optimization", Acta Numerica 22 (2013) 1-131, DOI 10.1017/S0962492913000032 (preprint ANL/MCS-P3060-1121, November 22, 2012; Optimization Online 2012/12/3698). Abhishek, K., Leyffer, S., Linderoth, J., "FilMINT: An Outer Approximation-Based Solver for Convex Mixed-Integer Nonlinear Programs", INFORMS J. Comput. 22(4) (2010) 555-567, DOI 10.1287/ijoc.1090.0373. Mahajan, A., Leyffer, S., Linderoth, J., Luedtke, J., Munson, T., "Minotaur: a mixed-integer nonlinear optimization toolkit", Math. Program. Comput. 13(2) (2021) 301-338, DOI 10.1007/s12532-020-00196-1 (preprint ANL/MCS-P8010-0817; Optimization Online 2017/10/6275).

- Origin. [stated · primary, coauthored] "The past 20 years or so have seen a dramatic increase in new mixed-integer nonlinear models and applications, which has motivated the development of a broad range of new techniques to tackle this challenging class of problems." (preprint, p. 8). How the invitation came about and who drafted what: not documented.
- Why then. [inferred] The team had just built and tested its own tools: FilMINT (preprint 2006, journal 2010), the branching study (Optimization Online 2011/09, published 2013), QP-diving (2012), TACO (2013), Minotaur in development; and the IMA volume he co-edited (Lee and Leyffer, 2011/2012) had gathered the field. Basis: the dates in §1.2.
- Key insight. [stated · primary, abstract] "We distinguish two broad classes of methods: single-tree and multitree methods." and "The most efficient class of methods for convex MINLP are hybrid methods that combine the strengths of both classes of classical techniques." In 2017 he restates the taxonomy and reduces all these algorithms to two building blocks: "All these MINLP algorithms share a range of common building blocks, namely relaxation and constraint enforcement." (p. 6)
- Positions stated in the survey [stated · primary, coauthored]: "Modeling plays a fundamental role in MILP (see the textbook by Williams (1999)) and is arguably more critical in MINLP, because of the additional nonlinear relationships." (p. 11); "A common theme of these reformulation is that convex formulations are typically preferred over nonconvex ones, and linear formulations over nonlinear formulations." (p. 12); "In many practical instances, the MINLP solvers fail, because the nonlinear solver generates an iterate at which the nonlinear functions cannot be evaluated." (p. 12). The scope is cut on purpose: "Given the wide applicability of MINLP and the ensuing explosion of numerical methods, it would be prohibitive to discuss all methods. Instead, we focus this survey on deterministic methods that tackle both integer variables and nonlinear constraints." (p. 9); polynomial-time algorithms in fixed dimension, closures of convex integer sets and mixed-integer derivative-free optimization are excluded (pp. 9-10).
- Minimum evidence. [practice · primary] The survey shows its own solver's numbers where it argues a point: a presolve reformulation for synthesis problems ("The effect of this reformulation is dramatic") and "In addition, the presolve enables MINOTAUR to solve 20% more instances than the version without presolve." (p. 39)
- The software line. [practice · primary] FilMINT is assembled from the best available parts: "The new solver, FilMINT, combines the MINTO branch-and-cut framework for MILP with filterSQP to solve the nonlinear programs that arise as subproblems in the algorithm." and "By carefully incorporating and tuning all these enhancements, an effective solver for convex MINLPs is constructed." (abstract). [stated · primary] He calls the algorithm it implements, Quesada and Grossmann's, "arguably the best approach to solving MINLPs", and credits "computational refinements that proved critical to its performance, such as efficient cut management to remove redundant cuts and a more aggressive cut generation strategy that generates cuts at non-integer points" (2017, pp. 5-6). Minotaur's aims (2017, p. 6): "(1) implement a range of algorithms in a common framework; (2) provide fast and usable MINLP solver; (3) provide flexibility for developing new efficient algorithms; and (4) reduce the burden of developing new algorithms by providing a common software infrastructure." The Minotaur paper argues from necessity: "Without a flexible framework that enables structure exploitation, finding global solutions to difficult nonconvex MINLP problems will remain out of reach for many applications." (abstract). On nonconvexity: "In general, nonconvex forms are more challenging and diverse than integer variables, which motivates a more tailored approach." (2017, p. 7)
- Abandoned paths. Not documented for the survey. For Minotaur, the GitHub record starts in 2016, and the paper took about three years from preprint (2017) to print (online November 2020); reasons not documented. [practice · primary]
- Reception. Acta: Scholar 1138, Crossref 640, his second most cited work. FilMINT: Scholar 189 for the journal paper plus 88 for the 2006 preprint. Minotaur: Scholar 71; repository still active in 2026 [practice · primary]. The Farkas committee (2016) names FilMINT and "the very ambitious project MINOTAUR" [observed · primary].
- Method it shows: M4 build from best-in-class components; M9 a taxonomy by building blocks; M8 consolidate a field with a survey plus shared software; M6 formulation as part of the algorithm.
- Era and resources: a DOE-funded national-laboratory team spanning several universities; the software was written mainly by a postdoc and later his students (Mahajan's commits dominate); Leyffer is coauthor and co-designer, not the main committer. [practice · primary; role inferred]

### S5. Integer variables in function space: the MIPDECO line, anchored on Leyffer and Manns (2026) and its Correction

Identifiers: Leyffer, S., Manns, P., "McCormick envelopes in mixed-integer PDE-constrained optimization", Mathematical Programming 218(1) (2026) 245-290, online 6 January 2025, DOI 10.1007/s10107-024-02181-1; arXiv 2406.07891 (v1 12 June 2024; v5 5 January 2026). Correction: Math. Program. 218(1) (2026) 591-592, online 17 February 2026, open access, DOI 10.1007/s10107-026-02330-8 (read in full). The line:
- Leyffer, Cay, Kouri, van Bloemen Waanders, "Mixed-integer PDE-constrained optimization", ANL/MCS-P5429-1015 (November 2015; known only from his 2017 reference list; status not checked);
- Hahn, Leyffer, Zavala, "Mixed-Integer PDE-Constrained Optimal Control of Gas Networks" (Optimization Online 2017/12/6381);
- Leyffer, Manns, Winckler (2021), DOI 10.1007/s10589-020-00262-3; Gnegel et al. (2021), DOI 10.1007/s10107-021-01626-1;
- Vogt, Leyffer, Munson (2022), DOI 10.1137/20M1315993, and (2025), DOI 10.1007/s10589-024-00644-x; Leyffer and Manns (2022), DOI 10.1051/cocv/2022059;
- Hahn, Leyffer, Sager (2023), DOI 10.1007/s10107-021-01733-z; Manns, Hahn, Kirches, Leyffer, Sager, arXiv 2202.07934; Choudhary, Leyffer, Yang, arXiv 2509.19888.

- Origin. [stated · primary] The 2017 outlook names this frontier: "In addition, new classes of MINLPs are emerging, such as MIPs with second-order cone constraints [12, 11] and MINLPs with partial-differential equation constraints [31], which necessitate novel approaches." (p. 7; [31] is the 2015 preprint). The 2013 survey had already given mixed-integer optimal control its own section and described it in the abstract as "an emerging area of mixed-integer optimal control that adds systems of ordinary differential equations to MINLP" [stated · primary, coauthored]. Where the McCormick idea itself came from: not documented.
- Why then. [stated · primary, abstract] McCormick relaxations "have not gained much attention in PDE-constrained optimization so far. This lack of attention may be due to the distributed nature of such problems, which on the one hand leads to infinitely many linear constraints ... and renders bound-tightening procedures that successively improve the resulting convex relaxations computationally intractable." [inferred] Argonne applications with integer design fields (electromagnetic cloaking, gas networks, source inversion) and the collaboration with the mixed-integer optimal-control community (Sager, Kirches, Manns) supplied the problems and the tools at the same time.
- Key insight. [practice · primary, journal abstract] "We approximate the nonlinearity and in turn the McCormick envelopes by averaging the involved terms over the cells of a partition of the computational domain on which the PDE is defined. This yields convex relaxations that underestimate the original problem up to an a priori error estimate that depends on the mesh size of the discretization." Minimizers of these relaxations converge to minimizers of a pointwise limit problem as the mesh size goes to zero. The earlier papers of the line make the same move away from the discretized integer program: "A first-discretize-then-optimize approach results in a large-scale mixed-integer nonlinear program that is in general intractable because of the large number of integer variables that arise from the discretization of the domain." (Leyffer, Manns, Winckler 2021, abstract) [stated · primary]
- Minimum evidence. [stated · primary] "We provide a computational example, for which we certify all of our imposed assumptions." (abstract)
- Abandoned paths and corrections. [stated · primary] The paper ends on its own limits: "The results point to both the potential of the methodology and the gaps in the research that need to be closed." [practice · primary] The 2026 Correction repairs an assumption and a proof step (F10). In the cloaking work the mixed-integer formulation is offered as "an alternative to the topology optimization formulation of electromagnetic cloaking design" (Vogt et al. 2022, abstract) [stated · primary]. Whether arXiv v5 (5 January 2026) already contains the corrections: not checked.
- Reception. Too recent to judge: Scholar 14 on 2026-10-10. The line keeps producing papers with several groups (Magdeburg, Dortmund, Duisburg-Essen, Argonne).
- Method it shows: M7 carrying mature finite-dimensional tools (McCormick envelopes, trust regions, sum-up rounding) into infinite dimensions; analysis in function space first, discretization second; M5 publishing the correction; certifying the assumptions on a worked example.
- Era and resources: senior period; a two-author paper with a junior who had an Argonne affiliation in 2021 and was at TU Dortmund by 2025; arXiv-first with five versions.

---

## 4. Cross-index: candidate research methods suggested by the signature works (for Phase 2)

These are leads for agents 02-03 and for Phase 2, not established methods. Each still needs the check of stated against done.

| ID | Candidate method | Evidence | Tag |
|---|---|---|---|
| M1 | Use counterexamples as a design tool: build the smallest example that breaks the method (or a rival's theory), then redesign | S1: the worst case leads to quadratic OA; S3: the Maratos example leads to second-order corrections and then the nonmonotone filter; F8 PIPA counterexample; F9 SQP and SQPEC failure examples | [practice + stated · primary] |
| M2 | Numbers first, theory second: a convincing run on a modest test set, then the convergence analysis that explains it | S3: report NA/171 (Sept 1997) before the first proof NA/183 (Aug 1998); MPECs: "In contrast, our initial numerical experience with filterSQP was very positive [19], and we investigated the convergence of SQP methods applied to (3.9)" (2017, p. 7) | [stated · primary; ordering for S3 inferred from dates] |
| M3 | Own the solver code and integrate at the iteration level instead of calling packages as black boxes | S2: "By using our own solver we are able to remove this unnecessary restriction"; the callback design (NA/182, p. 10) | [stated + practice · primary] |
| M4 | Build on existing best-in-class infrastructure | FilMINT = MINTO + filterSQP; MPECs: "In my opinion, reliable NLP solvers are still the best approach for solving MPECs ... To develop better solvers we need to build on our existing NLP solver infrastructure." (2017, p. 9) | [stated + practice · primary] |
| M5 | Publish the failures and the corrections | F6, F7, F10; F2 and F5 reported by himself | [practice + stated · primary] |
| M6 | Treat the formulation as part of the algorithm | Acta §2.1 (pp. 11-12); "The use of slacks in (3.9) is critical for the convergence of SQP methods." (2017, pp. 8-9, section "The Importance of Being Slack"); MPECs: "as long as we take care with the problem formulation and the algorithm design, modern NLP solvers can tackle these problems." (2017, p. 7) | [stated · primary] |
| M7 | Extend mature NLP machinery to a new problem class (MINLP, then MPECs, then PDE-constrained integer problems) | GT 2009 bio; the structure of the 2017 article; S1, S2, S5 | [stated + practice · primary] |
| M8 | Consolidate a field through surveys, retrospectives, test libraries and shared software | 2006 filter history; 2013 Acta survey; IMA volume; MacMPEC; the 1998 MINLP test set; Minotaur and Uno; the 2020 robust-optimization survey | [practice · primary] |
| M9 | Organize algorithms by building blocks | Acta: single-tree versus multitree; 2017: "relaxation and constraint enforcement"; Uno: "a unifying framework with eight building blocks that abstracts the workflows of Lagrange-Newton methods" (arXiv 2406.13454); funnel SQP: "a generic double-loop framework consisting of four algorithmic ingredients" (arXiv 2409.09208) | [stated · primary] |
| M10 | Safeguards should interfere as little as possible with Newton's method | 2006, p. 2; S3 | [stated · primary] |

---

## Contradictions (kept, not reconciled)

1. PhD year and thesis title. Scholar: "Deterministic methods for mixed integer nonlinear programming", University of Dundee, 1993. MGP and Wikipedia: Ph.D. 1994, "Deterministic Methods in Mixed Integer Nonlinear Programming". The GT 2009 bio says PhD 1994. [observed]
2. Page range of the 2002 filter paper: 239-269 (Springer, Crossref, DBLP, the MOS prize citation) against 239-270 in his own reference lists (2006 history, ref. [8]; 2017 article, ref. [17]).
3. Speed-up of SQP plus branch-and-bound: "a factor of about 3" (1998 report, abstract and conclusions) against "a factor of up to 3" (2001 journal abstract). Table 3 of the report has its best ratio at about 2.8 (TRIMLOSS) and one instance where the new method is slower (BATCH).
4. What the "MINLP" code is. Farkas 2016 citation: "the packages MINLP and FilMINT (also coauthored), which illustrate different implementations of the outer-approximation method for MINLPs". NEOS: MINLP "solves mixed integer nonlinear programming (MINLP) problems by branch-and-bound" and "is more robust than outer approximation or Benders Decomposition"; the 2001 paper describes a branch-and-bound method.
5. The 1994 convergence proof. Farkas 2016: the thesis work "provided a rigorous treatment of infeasibilities and convergence proof to the methodology". Leyffer 2017: "Later, Bonami et al. corrected our convergence proof".
6. The filter convergence proof. Lagrange 2006: the SIOPT paper gives "a satisfying proof of correctness". Leyffer 2017: Gould and Wächter "corrected many errors in the early proof" (which proof "the early proof" means is ambiguous).
7. His view of filter methods. 2006: "We believe filter methods achieve this goal." 2017: "I do not believe that there exists a big difference between filter methods and modern penalty function methods, and the choice of method is really a question of personal preference." (also F11)
8. Preferred route to fast local convergence. 2006: "We currently prefer to use SOC steps". 2017: "a more appealing approach is to use a nonmonotone filter".
9. The best approach to MINLP. 2017: the Quesada-Grossmann algorithm "is arguably the best approach to solving MINLPs" (in a passage on convex MINLP). NEOS MINLP page: branch-and-bound "is more robust than outer approximation or Benders Decomposition" (in a passage on nonconvex problems). Both kept: they may refer to different problem classes.
10. A name. The 2017 article's text credits the nonmonotone filter to "Chungen Chen at Argonne"; its own reference [38] and DBLP give "C. Shen" or "Chungen Shen".
11. Springer's article history for the 1994 paper lists "Revised: 01 December 1994", after the August 1994 issue date.
12. Year of the IMA volume: 2011 (Scholar; cited as "Lee and Leyffer, 2011" in the Acta preprint) against 2012 (Crossref print date).
13. Credit for the Maratos counterexample: the 2006 history presents "the following example" in the authors' collective voice; the 2017 article credits "Nick and Philippe".

## Gaps (not found or not read)

- PhD thesis (1993 or 1994): no public copy found; the CiteSeerX id given by Wikipedia no longer resolves. Not read.
- Full texts of the 1994 OA paper, the 2002 filter paper, the 2001 journal version of SQP plus branch-and-bound, FilMINT, Minotaur and the McCormick paper: paywalled or not attempted. Only abstracts, article histories and, for S2, the 1998 report were read. The numerical sections of S1 and S3 were not read.
- Acta Numerica survey: only the contents, §1.3, §2.1 and §3.4.1 of the preprint were read.
- Homepage and CV (wiki.mcs.anl.gov/leyffer) and the Argonne profile: HTTP 403 throughout. The year he joined Argonne (2002) and his postdoc stations (Dundee, Argonne, Northwestern) come only from a search-result summary of an Argonne page (secondary, unverified).
- SIAM Fellow 2009, Mathematical Programming B editor-in-chief 2017-2021 and SIAM President 2023-2024: Wikipedia only (secondary); SIAM pages blocked.
- Semantic Scholar (HTTP 429) and OpenAlex (no API key) not used, so no influential-citation data.
- Rejected submissions: none found. Why the filter paper's review took 34 months: unknown.
- Leyffer's own share relative to Fletcher in the OA and filter work cannot be separated out from the sources read; the filter idea is credited to Fletcher by Fletcher.
- The roles of junior collaborators (postdoc, student, visitor) are mostly inferred from coauthorship and affiliations; only Abhishek ("a student of Jeff Linderoth's") and Mahajan ("at Argonne") are stated.
- Journal publication of the SLP-filter report NA/183 (1998) and of the 2015 preprint ANL/MCS-P5429-1015: not verified.
- Whether arXiv v5 of the McCormick paper (January 2026) already contains the corrections: not checked.
- Why he left the grid-computing, HPC load-balancing, inexact-computing and network-epidemics lines: no source found (F12 is an inference from absence).
- Optimization Online: 43 of the 51 search hits were not opened, so a few more preprints may be his.

## Sources

Primary
1. Google Scholar profile of Sven Leyffer, `UubsxcAAAAAJ` (100 rows, citation order), read 2026-10-10, https://scholar.google.com/citations?user=UubsxcAAAAAJ&hl=en&pagesize=100. Primary (database record).
2. DBLP person pid 91/745 (92 records) via sparql.dblp.org with `scripts/dblp_works.py`, 2026-10-10, https://dblp.org/pid/91/745.html. Primary (bibliographic database).
3. arXiv author search "Leyffer" (35 results) and abstract pages for 2406.13454, 2501.13835, 2409.09208, 2406.07891, 2509.19888, 2508.05822, 2202.07934, math/0310357; 2026-10-10; https://arxiv.org/search/?query=Leyffer&searchtype=author. Primary.
4. Optimization Online search "Leyffer" (51 hits) and entries 2000/08/208, 2000/08/209, 2001/05/330, 2006/10/1489, 2007/09/1777, 2011/09/3191, 2012/12/3698, 2017/10/6275; https://optimization-online.org/?s=Leyffer. Primary.
5. Crossref REST API records for the DOIs cited here (metadata, deposited abstracts, citation counts), https://api.crossref.org/works/. Primary (bibliographic metadata).
6. R. Fletcher, S. Leyffer, Ph. L. Toint, "A Brief History of Filter Methods", Preprint ANL/MCS-P1372-0906, 26 Sept 2006, rev. 9 Oct 2006, https://optimization-online.org/wp-content/uploads/2006/10/1489.pdf. Primary (read in full).
7. S. Leyffer, "Integrating SQP and branch-and-bound for Mixed Integer Nonlinear Programming", University of Dundee NA/182, 6 Aug 1998, https://optimization-online.org/wp-content/uploads/2000/08/208.pdf. Primary (pp. 1-2 and 10-12 read).
8. P. Belotti, C. Kirches, S. Leyffer, J. Linderoth, J. Luedtke, A. Mahajan, "Mixed-Integer Nonlinear Optimization", Preprint ANL/MCS-P3060-1121, 22 Nov 2012, https://optimization-online.org/wp-content/uploads/2012/12/3698.pdf. Primary (parts read).
9. S. Leyffer, "Nonlinear Optimization and Beyond", INFORMS OS Today 7(2), October 2017, pp. 3-10, https://higherlogicdownload.s3.amazonaws.com/INFORMS/9a2da56a-3917-4600-a0e3-84cfb0d2b004/UploadedFiles/09uQ9yCcRT5ZSlbtKE74_OStoday2017v2.pdf. Primary (read in full).
10. Springer landing page, Fletcher and Leyffer (1994), https://doi.org/10.1007/BF01581153. Primary (abstract, article history).
11. Springer landing page, Fletcher and Leyffer (2002), https://doi.org/10.1007/s101070100244. Primary (abstract, article history).
12. Springer landing page, Leyffer (2001), https://doi.org/10.1023/A:1011241421041. Primary (abstract).
13. Springer landing page, Mahajan et al. (2021), https://doi.org/10.1007/s12532-020-00196-1. Primary (abstract, affiliations).
14. Springer landing page, Leyffer and Manns (2026), https://doi.org/10.1007/s10107-024-02181-1. Primary (abstract, affiliations).
15. S. Leyffer, P. Manns, "Correction: McCormick envelopes in mixed-integer PDE-constrained optimization", 17 Feb 2026, https://doi.org/10.1007/s10107-026-02330-8. Primary (open access, read in full).
16. Springer landing page, Hahn, Leyffer, Sager (2023), https://doi.org/10.1007/s10107-021-01733-z. Primary (abstract, affiliations).
17. Springer landing page, Leyffer, Manns, Winckler (2021), https://doi.org/10.1007/s10589-020-00262-3. Primary (abstract, affiliations).
18. Mathematical Optimization Society, 2006 Lagrange Prize citation (the award record behind https://www.mathopt.org/awards/lagrange-prize, read from the site's public endpoint https://www.mathopt.org/api/awards/lagrange-prize), 2026-10-10. Primary (official citation).
19. INFORMS Optimization Society, "Farkas Prize 2016" citation, https://connect.informs.org/optimizationsociety/prizes/farkas-prize/2016. Primary (official citation).
20. INFORMS Optimization Society, Farkas Prize winners and committees, https://connect.informs.org/optimizationsociety/prizes/farkas-prize. Primary.
21. INFORMS OS Today 7(1), May 2017, Chair's Column (announces Leyffer's prize article), https://higherlogicdownload.s3.amazonaws.com/INFORMS/9a2da56a-3917-4600-a0e3-84cfb0d2b004/UploadedFiles/gojzpMS4ilkAykawItVw_OStoday2017v1.pdf. Primary.
22. University of Dundee press office, "International recognition for Dundee maths research", June 2006, https://app.dundee.ac.uk/pressoffice/contact/2006/june/maths.html. Primary (institutional release with Fletcher's quote).
23. Georgia Tech CSE Seminar, "A Tale of Two Problems: Integer and Nonlinear Optimization" (Sven Leyffer), 10 Mar 2009, https://hg.gatech.edu/node/52545. Primary (talk abstract and bio).
24. NEOS Server, solver page "MINLP", https://neos-server.org/neos/solvers/minco:MINLP/AMPL.html. Primary (solver documentation).
25. NEOS Server, solver page "filter", https://neos-server.org/neos/solvers/nco:filter/AMPL.html. Primary (solver documentation).
26. GitHub `coin-or/minotaur` (repository metadata, contributors, commit search), https://github.com/coin-or/minotaur. Primary.
27. GitHub `cvanaret/Uno` (metadata, contributors, commits authored "leyffer"), https://github.com/cvanaret/Uno. Primary.
28. GitHub `coin-or-tools/ThirdParty-FilterSQP`, https://github.com/coin-or-tools/ThirdParty-FilterSQP. Primary.

Secondary
29. Mathematics Genealogy Project, Sven Leyffer, id 282807, https://mathgenealogy.org/id.php?id=282807. Secondary.
30. Wikipedia, "Sven Leyffer", read 2026-10-10, https://en.wikipedia.org/wiki/Sven_Leyffer. Secondary.
31. WebSearch summaries (2 queries, 2026-10-10) of Argonne pages that return HTTP 403 (anl.gov/node/76866; wiki.mcs.anl.gov/leyffer). Secondary; used only for the 2002 Argonne start and the postdoc stations, marked unverified.

Third-party works cited for context, checked through Crossref (part of source 5): Duran and Grossmann 1986, DOI 10.1007/BF02592064; Quesada and Grossmann 1992, DOI 10.1016/0098-1354(92)80028-8; Borchers and Mitchell 1994, DOI 10.1016/0305-0548(94)90024-8; Bonami et al. 2008, DOI 10.1016/j.disopt.2006.10.011; Hijazi, Bonami, Ouorou 2014, DOI 10.1287/ijoc.1120.0545.
