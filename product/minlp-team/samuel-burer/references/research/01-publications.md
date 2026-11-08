# 01 · Signature works and the publication landscape

> **Researcher**: Samuel A. (Sam) Burer, Tippie Rollins Professor and Chair/Departmental Executive Officer, Department of Business Analytics, Tippie College of Business, University of Iowa. Google Scholar `BScCde0AAAAJ`; DBLP pid `96/4845`; ORCID `0000-0001-5886-458X`; homepage https://sburer.github.io/.
> **Dimension**: research agent 01 of 06: signature works and the publication landscape (nuwa research-craft Phase 1).
> **Research date**: 2026-10-10.
> **Sources consulted**: 49 numbered entries under "Sources" (25 primary, 24 secondary). Entry 48 bundles ten earlier papers by others that his papers name as their starting points. I checked their bibliographic data but did not read them.
> **Identifiers checked with a tool in this run**:
> - 83 DOIs through the Crossref REST API. All resolved. 64 are his own works or notes about them, and 19 are by others.
> - 19 arXiv ids through arxiv.org: the author search page plus abstract pages, including all three versions of 2504.03996.
> - 48 Optimization Online (OO) entries through his OO author archive, plus five original OO abstract pages through the Wayback Machine.
> - 53 DBLP records through `scripts/dblp_works.py` (SPARQL endpoint).
>
> **WebSearch calls used**: 2 of 2.
> **Local corpus**:
> - `sources/papers`, `essays`, `software` and `publications` hold only `.gitkeep`, so there is no user-supplied material and nothing below is marked "from user-supplied material".
> - `sources/talks/` holds two auto-caption transcripts of his research talks saved earlier in this run: the 2021 INFORMS Optimization Society (IOS) plenary, and the March 2023 Iowa version of "Two Decades of Low-Rank Optimization". It also holds two 2015 R-teaching transcripts, which are irrelevant here. I read the two research transcripts and quote them only as "(machine transcript)", with their ASR errors left in.
> - `private/` was not opened.
>
> **Full texts read**: author-posted copies in his homepage repository (`github.com/sburer/sburer.github.io/papers/`) and on Optimization Online and arXiv:
> - Burer–Monteiro 2003;
> - Burer 2009 (published version, and the OO revision of 18 Jul 2007);
> - Burer–Vandenbussche 2008;
> - the COAP 2009 best-paper award note;
> - Burer–Letchford 2012;
> - Burer–Anstreicher 2013 (preprint, revision of 16 Nov 2012).
>
> **Partly read**:
> - Burer–Monteiro 2005 (front matter, acknowledgments);
> - Burer–Vandenbussche 2009 (front matter);
> - Burer–Saxena 2012 (preprint of April 2010: introduction and Sections 5–6);
> - Burer–Yang 2015 (front matter, acknowledgments);
> - Burer 2015 "gentle introduction" (preprint, introduction);
> - Eltved–Burer arXiv 2009.12704v2 (abstract and the passages on Chen et al.);
> - the 2021 Burer–Ye correction (Springer page text);
> - the 2023 SIAM slide deck (text layer).
>
> **Skimmed for acknowledgments and implementation only**: OptDNN 2010, QuadProgBB 2012, the 2012 "Copositive Programming" chapter, Anstreicher–Burer 2005.
> **OpenAlex**: not used, because `OPENALEX_API_KEY` is not set.
> **Tags**:
> - [stated] = he said or wrote it; [stated-joint] = co-authored text;
> - [practice] = what the record shows he did (papers, code, dates, CV entries);
> - [observed] = what others wrote or measured;
> - [inferred] = my reading, which no source states.
>
> Each item also carries **P** (primary: his own text, records or code) or **S** (secondary: third parties, aggregators).
> **Quotes** are verbatim, including source typos ("techiniques", "millenium", "pointed about", "where encountered"). Page numbers are journal pages for published versions and PDF pages for preprints; transcript quotes carry the caption timestamp where the file has one.
> **Relation to 06-trajectory.md**: a sibling agent wrote `06-trajectory.md` earlier today. I read it for orientation only. Every identifier, number and quote below was re-checked by me in this run. Where we differ, I say so (Contradiction 10). Notes 02, 03 and 05 appeared while I was finishing. I took nothing from them, and only point to 05 for the competitive record of S1 and S3.

---

## 0. Data sources and how they disagree

| Source | What it holds for Burer | Gaps and errors found | Tag |
|---|---|---|---|
| CV, 18 pp., "updated February 12, 2026" | 57 journal articles [J01–J57] "listed in reverse chronological order by appearance of manuscript", 3 refereed chapters [B01–B03], 2 conference papers [C01–C02], 120 talks [P01–P120], 5 software items | Dates follow manuscripts, not print years: the rank-two max-cut paper is "2001" in the CV and January 2002 in Crossref; the two chapters are "2011" in the CV and 2012 in print | [practice, P] |
| DBLP (SPARQL, via `dblp_works.py --pid 96/4845`) | 53 records: 50 articles, 2 conference papers, 1 thesis. Burer is first author in 28 of the 47 multi-author records | Misses 9 of the 57 CV journal articles: J01 IJOC 2026, J14 EER 2016, **J21 the 2012 MINLP survey**, J23 JQAS 2012, J29 FEJAM 2014, J31 Optimization 2011, J33 LAA 2009, J44 TOP 2012 and J57 OMS 2001. Also misses all three chapters. No arXiv links | [practice, S] |
| Google Scholar `BScCde0AAAAJ` (WebFetch; a small model's summary of the page) | 70 rows. Citations 7,294 (2,885 since 2021), h-index 34, i10-index 52. The per-year citation histogram rises from 23 (2001) to 536 (2025) and 550 (2026 so far) | Counts as summarized by WebFetch, so treat them as approximate. The newsvendor paper is dated "2006" (Crossref: online 2010, print 2012). Two rows are NSF awards, one is the thesis, and one is a duplicate survey row ("Surveys in Operations Research and Management Science", 1 citation). The JMLR row lists the JMLR editors (Bennett, Parrado-Hernández) as authors | [observed, S] |
| Semantic Scholar (S2) Graph API | Two author records: 1691727 (86 papers, 5,631 citations, h = 32) and 2287317032 (4 papers) | Splits 1999 technical reports and 2005 OO preprints into separate items. Attributes two 2018 cell-therapy abstracts (*Cytotherapy*) to "S. Burer". Lists a 2008 auction-econometrics item with him as co-author that is in neither the CV nor DBLP (excluded; not checked) | [observed, S] |
| Optimization Online author archive | 48 entries, 2001-03-09 → 2026-09-24 | OO serves the latest uploaded PDF. The original 2006 copositive and 2011 SOC-TRS PDFs have been replaced by revisions; the Wayback Machine keeps the original abstract pages | [practice, P] |
| arXiv | 13 entries under "Burer, Samuel" (2015–2026), plus 1406.1031 and 2205.13653 under "Sam Burer" | Earliest arXiv id found: 1406.1031 (June 2014). A wider "Burer" sweep returned HTTP 429, so older items were not checked | [practice, P] |

**Working corpus for the counts in §1.** There are 64 research works: the 57 CV journal articles, the 2 conference papers, the 3 chapters (including the encyclopedia entry), and the 2 arXiv-only preprints (2504.03996 and 2609.32017). Excluded are the thesis (2001), the *Discrete Optimization* editorial (2017), the Burer–Ye correction (2021, counted with its paper) and the NSF award rows. Each work is dated by its **first public version**: the OO or arXiv posting when there is one, otherwise the earliest Crossref date. Print can lag by up to seven years: the newsvendor paper was posted in January 2005 and printed in 2012. [practice, P]

---

## 1. Publication landscape

### 1.1 Topics by five-year period (64 works, dated by first public version) [practice, P; classification inferred]

Categories:
- **A**: SDP algorithms (low-rank and NLP reformulations, interior-point methods, first-order methods).
- **B**: relaxations and bounds for binary or integer problems.
- **C**: global nonconvex QP by branch-and-bound, KKT relaxations and solver codes.
- **D**: copositive and completely positive (CP) theory and computation.
- **E**: copositive methods for robust or distributionally robust optimization (DRO).
- **F**: convex hulls, valid inequalities and exactness of relaxations for (MI)QCQP substructures.
- **G**: trust-region-subproblem (TRS) variants.
- **H**: surveys and expository pieces.
- **I**: applications, analytics and machine learning (ML).

| Period | n | A | B | C | D | E | F | G | H | I | Sole-authored | With student, postdoc or visitor¹ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2001–05 | 17 | 11 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 2 |
| 2006–10 | 13 | 1 | 1 | 3 | 4 | 0 | 1 | 0 | 1 | 2 | 2 | 4 |
| 2011–15 | 17 | 1 | 1 | 2 | 1 | 1 | 3 | 3 | 3 | 2 | 3 | 9 |
| 2016–20 | 9 | 0 | 0 | 0 | 0 | 2 | 3 | 2 | 0 | 2 | 0 | 5 |
| 2021–26 | 8 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 1 | 2 | 1 | 4 |
| **All** | 64 | 13 | 4 | 6 | 6 | 3 | 11 | 6 | 5 | 10 | 7 | 24 |

¹ CV "Ph.D. Advisor" students (Choi, Chen, Dong, Yang, Xu, Park, Zhu), Yi Zhang (whom the CV lists under "Ph.D. Committee"), postdoc N. Cho, and visiting PhD student A. Eltved (DTU).

What the periods contain:
- **2001–05**: the thesis line with Monteiro and Yin Zhang: nonlinear reformulations of SDP, low-rank factorization, rank-two heuristics. Then the first moves outward: copositive bounds with Anstreicher (May 2003), lift-and-project SDPs with Vandenbussche (2004), maximum-entropy sampling with J. Lee (2005), the finite branch-and-bound posting (June 2005), and ensemble pruning with Yi Zhang and Street (2005).
- **2006–10**: copositive and completely positive theory (the 2009 representation paper, the 5×5 doubly nonnegative (DNN) versus CP matrices paper, OptDNN, cones of quadratic forms), global box-QP and KKT work, the first convex-hull paper (Anstreicher–Burer 2010), and the MIQCP survey chapter.
- **2011–15**: the widest spread. TRS variants start (SOC-RLT, 2011), alongside MIQP convex sets, SOC ∩ nonconvex quadratic, both expository copositive pieces, the 2012 MINLP survey and the first analytics papers.
- **2016–20**: copositive methods for robust and DRO problems (with student Xu), and exactness and convex-hull results (Burer–Ye, switching variables, bounded products).
- **2021–26**: convex hulls and relaxations (Stiefel manifold, submodular quadratic, Lorentz positive cone), one TRS/ball paper, and two ML-adjacent papers (constraint learning; optimization over trained neural networks).

[inferred] The record runs from *how to solve SDPs fast* (2001–05), to *what SDP and copositive relaxations can represent exactly* (2006–15), to *exact convex hulls of small nonconvex substructures* (2011–26). The lifting x → (x, X = xxᵀ) runs through all three.

### 1.2 Where the citations sit [observed, S]

I matched Google Scholar counts to the 64 works. They sum to 7,290 of the 7,294; the remainder is the correction (3) and the duplicate survey row (1).

| Category | Works | Scholar citations | Share |
|---|---|---|---|
| A SDP algorithms | 13 | 2,930 | 40.2% |
| H Surveys and expository | 5 | 1,215 | 16.7% |
| D Copositive and CP | 6 | 862 | 11.8% |
| C Global QP branch-and-bound | 6 | 652 | 8.9% |
| I Applications, analytics, ML | 10 | 600 | 8.2% |
| F Hulls, inequalities, exactness | 11 | 402 | 5.5% |
| G TRS variants | 6 | 324 | 4.4% |
| B Binary/IP relaxations | 4 | 197 | 2.7% |
| E Copositive for robust/DRO | 3 | 108 | 1.5% |

- The top 10 works hold 67.0% of all citations.
- The top two, Burer–Monteiro 2003 and Burer–Letchford 2012, hold 30.6%.
- [inferred] The citation weight sits in the thesis-era SDP algorithms and in the expository pieces. His most frequent recent output, convex hulls and TRS (17 works), holds about 10%. Younger papers have had less time to accumulate citations, so this partly reflects age.

### 1.3 Most-cited works

| # | Work | Scholar | S2 (influential²) | Type |
|---|---|---|---|---|
| 1 | Burer & Monteiro, "A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization", *Math. Program.* 95(2):329–357, 2003, DOI 10.1007/s10107-002-0352-8 | 1,372 | 1,081 (158) | algorithm |
| 2 | Burer & Letchford, "Non-convex mixed-integer nonlinear programming: A survey", *Surveys in OR & MS* 17(2):97–106, 2012, DOI 10.1016/j.sorms.2012.08.001 | 859 | 636 (20) | survey |
| 3 | Burer & Monteiro, "Local minima and convergence in low-rank semidefinite programming", *Math. Program.* 103(3):427–444, 2005, DOI 10.1007/s10107-004-0564-1 | 635 | 434 (46) | theory behind #1 |
| 4 | Burer, "On the copositive representation of binary and continuous nonconvex quadratic programs", *Math. Program.* 120(2):479–495, 2009, DOI 10.1007/s10107-008-0223-z | 566 | 479 (81) | theory, sole author |
| 5 | Zhang, Burer & Street, "Ensemble pruning via semi-definite programming", *JMLR* 7:1315–1338, 2006 (DBLP record; no DOI) | 408 | 327 (27) | ML application |
| 6 | Burer, Monteiro & Zhang, "Rank-two relaxation heuristics for MAX-CUT and other binary quadratic programs", *SIAM J. Optim.* 12(2):503–521, 2002, DOI 10.1137/S1052623400382467 | 354 | 263 (42) | heuristic |
| 7 | Burer & Vandenbussche, "A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations", *Math. Program.* 113(2):259–282, 2008, DOI 10.1007/s10107-006-0080-6 | 217 | 178 (10) | global algorithm |
| 8 | Chen & Burer, "Globally solving nonconvex quadratic programming problems via completely positive programming", *Math. Program. Comput.* 4(1):33–52, 2012, DOI 10.1007/s12532-011-0033-9 | 170 | 133 (17) | solver (QuadProgBB) |
| 9 | Burer, "Copositive Programming", in *Handbook on Semidefinite, Conic and Polynomial Optimization*, 201–218, 2012, DOI 10.1007/978-1-4614-0769-0_8 | 153 | not in S2 list | expository |
| 10 | Anstreicher & Burer, "Computable representations for convex hulls of low-dimensional quadratic forms", *Math. Program.* 124(1–2):33–43, 2010, DOI 10.1007/s10107-010-0355-9 | 153 | 140 (17) | convex hull |
| 11 | Burer & Letchford, "On nonconvex quadratic programming with box constraints", *SIAM J. Optim.* 20(2):1073–1089, 2009, DOI 10.1137/080729529 | 136 | 109 (16) | polyhedral |
| 12 | Burer & Anstreicher, "Second-order-cone constraints for extended trust-region subproblems", *SIAM J. Optim.* 23(1):432–451, 2013, DOI 10.1137/110826862 | 134 | 120 (14) | relaxation |

² S2's own "influentialCitationCount" from the author-papers endpoint. The citations endpoint flags slightly different numbers of rows as influential: 154 for #1, 21 for #2, 87 for #4, 13 for #7 and 19 for #12.

What he himself foregrounds:
- His 2026 homepage names exactly two research honours: "His research has been recognized with the INFORMS Computing Paper Prize and the SIAM Optimization Test of Time Award". Both are for #1, and the INFORMS prize also covers #3 (S1 below). [stated, P]
- The CV ties the SDPLR software to "[J45], [J47], [J51], and [J57]", i.e. #1, #3 and their companions. [stated, P]
- His 2015 expository paper says of #4: "the basic ideas found in the paper [9] for the case of polyhedra are the core required for all results in this paper" (preprint rev. 17 Jan 2015, pp. 2–3; [9] = the 2009 paper). [stated, P]
- I found no list of "my most important papers" in his own words (see Gaps).

### 1.4 Who cites what [observed, S; S2 citation data fetched 2026-10-10]

- **Burer–Monteiro 2003, citing papers by year** (1,081 S2 rows): 24 (2000–04), 99 (2005–09), 148 (2010–14), 318 (2015–19), 344 (2020–24), 140 (2025–26) and 8 undated. 74% of the dated citations come from 2015 or later, 12 or more years after publication.
- **The 2012 survey and the 2009 copositive paper are cited by different communities.**
  - Survey citers by S2 field (a paper can have several): Computer Science 413, Engineering 410, Mathematics 182 (of 636). The most frequent named venues are *IEEE Trans. Vehicular Technology* (20), *EJOR* (14), *IEEE Trans. Mobile Computing* (11), *IEEE Trans. Wireless Communications* (11) and *J. Global Optim.* (11).
  - Copositive-paper citers: Mathematics 440 of 479. Top venues: *Math. Program.* (44), *JOGO* (36), *COAP* (19), *SIOPT* (17).
  - [inferred] The survey is a common general reference on MINLP difficulty for applied engineering papers. This would explain why it has many citations but few S2-influential ones (20 of 636). The 2009 paper is cited and built on inside the optimization field (81 or 87 influential of 479).
- The CV lists "Top 5 Most Downloaded, Surveys in Operations Research and Management Science journal, 2014". [stated, P]

### 1.5 Author order: there is no first-author → last-author shift [practice, P (DBLP: S); readings inferred]

- **The convention is alphabetical.** Of 47 multi-author DBLP records, 33 list authors alphabetically by surname. Burer is first in 28, second in 16, third in 2 and fourth in 1. With a surname starting "B", alphabetical order nearly always puts him first, so his position says little about his role.
- **Exceptions mark junior-led work.** 14 records are not alphabetical. 13 of them put a student or junior first:
  - Yi Zhang (ICDM 2005, JMLR 2006; ML venues);
  - Jieqiu Chen (MPC 2012, SIOPT 2014);
  - Boshi Yang (SIOPT 2016; *Math. Program.* 2018 with Anstreicher);
  - Guanglin Xu (four papers, 2017–2018);
  - Anders Eltved (2023);
  - Kyle Gilman (SIMAX 2025);
  - Jiatai Tong (CPAIOR 2026, Burer last).

  Outside DBLP, the same applies to Zhu & Burer (IJOC 2026) and Yang & Burer (encyclopedia 2023).
- **The practice is not uniform.** Student papers also appear in alphabetical order with Burer first: Burer & Choi 2006, Burer & Chen 2009/2011, Burer & Dong 2012/2013, Burer & Yang 2015, Burer & Park 2024.
- **The one non-alphabetical paper with a senior partner** is Burer & Anstreicher, SIOPT 2013. arXiv 2002.04681 (switching variables, 2020) and 2609.32017 (2026) also list "Burer, Samuel; Anstreicher, Kurt", while the published switching paper lists Anstreicher first (Contradiction 5).
- **Last position** appears only in CS- or ML-style venues: ICDM 2005 and CPAIOR 2026. He is in the middle in SIMAX 2025 with the Michigan electrical engineering (EE) group (Balzano last).
- **Sole-authored works (7)**: SIOPT 2003 (partial positive semidefinite (PSD) matrices), *Math. Program.* 2009 (copositive), MPC 2010 (OptDNN), the 2012 copositive chapter, JQAS 2012 (college football), *Math. Program.* 2015 (gentle introduction) and *Math. Program.* 2025 (ball constraints). Four of the seven belong to the copositive line.
- [inferred] Seniority shows in two ways, not as a move to the last author position: student-first orders from 2012 on, and senior-author placement only in non-optimization venues.

### 1.6 Collaboration network and students [practice, P]

| Partner | Relation (source) | Works in corpus (first public years) | Lines |
|---|---|---|---|
| R.D.C. Monteiro (Georgia Tech) | PhD advisor (CV) | 9 (2001–2004) | NLP reformulations of SDP, low-rank, long-step interior-point methods |
| Yin Zhang (Rice) | collaborator; the 2003 runs used "the computer" he made available (p. 356) | 5 (2001–2002) | SDP via NLP, rank-two and stable-set heuristics |
| K.M. Anstreicher (Iowa) | departmental colleague; co-advisor of Dong and Park (CV) | 8 (2003–2026) | copositive bounds, low-dimensional convex hulls, 5×5 DNN/CP, SOC-RLT/TRS, hollows, switching, bounded products, Lorentz cone |
| D. Vandenbussche (UIUC → Axioma) | collaborator 2002–2007 (award note) | 3 (2004–2007) | lift-and-project SDP, finite branch-and-bound for QP |
| A.N. Letchford (Lancaster) | collaborator | 3 (2008–2012) | box-QP polyhedra, MIQP convex sets, MINLP survey |
| Students (CV): C. Choi (2007), J. Chen (2010), H. Dong (2011, with Anstreicher), B. Yang (2015), G. Xu (2017), K. Park (2023, with Anstreicher), Y. Zhu (expected Spring 2026) | PhD advisees | Choi 2, Chen 4, Dong 2, Yang 4, Xu 4, Park 2, Zhu 2 | each student carried one strand: low-rank SDP (Choi); KKT and CP branch-and-bound, first-order LP (Chen); copositive separation (Dong); TRS variants (Yang); copositive robust/DRO and IV quantile regression (Xu); bounded products and Stiefel (Park); ML-embedded optimization (Zhu) |
| One-off senior partners | — | 1–2 each | J. Lee (MESP 2005), M.F. Anjos (2006), P.C. Jones & T.J. Lowe (2008), M. Dror (2005), M. Dür (2008), A. Saxena (2009), S. Kim & M. Kojima (2013), F. Kılınç-Karzan (2014), G. Fethke (2016), Y. Ye (2018), V. Piccialli (2019), L. Balzano & K. Gilman (2022), K. Natarajan & R. Willemsen (2025–26), T. Serra & J. Tong (2025) |

- There are 36 distinct co-authors across the 64 works.
- The share of works with a junior co-author rises over time: 2 of 17 (2001–05), 4 of 13 (2006–10), 9 of 17 (2011–15), 5 of 9 (2016–20) and 4 of 8 (2021–26). [practice, P]
- [inferred] Two senior partnerships carry the long threads: Monteiro for the low-rank line (2000–2005) and Anstreicher for the hulls/copositive/TRS lines (2003–2026). Most other senior partners appear once.

### 1.7 Usual venues and channels [practice, P]

- **Journals**: *Mathematical Programming* 19 of 64 works (Series A and B), *SIAM J. Optimization* 8, *Optimization Methods & Software* 5, *Computational Optimization & Applications* 5, *Math. Programming Computation* 3, *J. Global Optimization* 2, *EJOR* 2. *Math. Program.* and *SIOPT* together hold 27 of 64 (42%).
- **Single papers** appeared in *ORL*, *LAA*, *JOTA*, *SIMAX*, *IJOC*, *JMLR*, *TOP*, *JQAS*, *Economics of Education Review*, *CMS*, *Optimization*, *SORMS*, *Far East J. Appl. Math.*, an IMA volume, a handbook, an encyclopedia, ICDM and CPAIOR.
- **Editorial service in his core venues** (CV):
  - *Math. Program.* AE 2022–;
  - *SIOPT* AE 2011–2025;
  - *Operations Research* AE 2011–20 and Area Editor 2020–;
  - *MPC* AE 2008–13;
  - *SORMS* AE 2009–13;
  - *ORL* AE 2009–14;
  - *MOR* AE 2011–18.
- **Preprints**: Optimization Online was his only preprint channel from 2001 to 2014 (48 entries in total). The first arXiv posting found is 1406.1031 (June 2014). From 2015 nearly every new paper went to both OO and arXiv; the exceptions are hollows (2016) and the 2014 IV quantile regression and gentle-introduction postings (OO only).
- **Software accompanying papers** (CV):
  - SDPLR 1.03-beta ([J45], [J47], [J51], [J57]);
  - Max-AO ([J52]);
  - CirCut ([J53], "available from coauthor");
  - OptDNN ([J30]);
  - QuadProgBB "version 20120229" ([J27]).

  GitHub (API, 2026-10-10):
  - `sburer/QuadProgBB`: created 2014-01-20, last push 2016-07-08, 7 stars, 6 forks;
  - `sburer/sdplr`: created 2023-10-05, last push 2026-03-23, 4 stars;
  - `sburer/soctrust`: created 2016-05-11, described as "Software and scripts to accompany http://dx.doi.org/10.1137/110826862".

### 1.8 Which papers he toured: talk repetitions in the CV [practice, P]

The CV lists 120 talks. Titles given four or more times:
- "An Extended Validity Domain for Constraint Learning": 9 talks (2024–2026);
- "Convexification for Non-Convex Mixed-Integer Quadratic Programming": 6 (2021–22, including the IOS 2021 plenary);
- "(On / Towards) the Semidefinite Representability of Continuous Quadratic Submodular Minimization…": 6 (2025–26);
- "Robust Rankings for (American) College Football": 6 (2012–2019);
- "A Copositive Approach for Two-Stage Adjustable Robust Optimization…": 5 (2016–2022);
- "A Finite Branch-and-Bound Algorithm for Nonconvex Quadratic Programming via Semidefinite Programming": 5 (Nov 2005 – Jul 2006);
- "Representing NP-Hard Problems as Convex Programs": 4 (all 2007), plus "On the Copositive Representation…" 2 (2007–08);
- "A Nonlinear Programming Algorithm for Solving Semidefinite Programs via Low-Rank Factorization": 4 (2000–2002).

Other counts:
- **Copositive titles**: 22 of the 120 talks (2007–2022) carry "copositive", "completely positive" or the 2007 title "Representing NP-Hard Problems as Convex Programs".
- **Plenary and semi-plenary talks** (4):
  - ICCOPT 2013, "Copositive Optimization";
  - ISMP 2015, "A Gentle, Geometric Introduction to Copositive Optimization";
  - IOS 2021, "Convexification for Non-Convex MIQP";
  - SIAM OP23, "Two Decades of Low-Rank Optimization".

[inferred] By talk count, the copositive line is the one he promoted longest (2007–2022). The newest lines (constraint learning, submodular) are now being toured at the rate the finite branch-and-bound was in 2005–06.

### 1.9 Recent works, 2023–2026 [practice, P]

- Burer, "A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints", *Math. Program.* 211(1–2):157–179, 2025, DOI 10.1007/s10107-024-02076-1; arXiv 2303.01624. Sole author.
  - The abstract's method sentence: "The key idea of the relaxation is a simple lifting of the original problem into dimension $n+1$." [stated, P]
  - An outside follow-up already exists: Kılınç-Karzan & Sun, "On the strength of Burer's lifted convex relaxation to quadratic programming with ball constraints", arXiv 2407.14992. [observed, S]
- Burer & Park, "A strengthened SDP relaxation for quadratic optimization over the Stiefel manifold", *JOTA* 202(1):320–339, 2024, DOI 10.1007/s10957-023-02168-6; arXiv 2208.03125.
- Gilman, Burer & Balzano, "A semidefinite relaxation for sums of heterogeneous quadratic forms on the Stiefel manifold", *SIMAX* 46(2):1091–1116, 2025, DOI 10.1137/23M1545136; arXiv 2205.13653.
- Yang & Burer, "Convex Hulls in Quadratic Space", *Encyclopedia of Optimization*, online 31 Oct 2023, DOI 10.1007/978-3-030-54621-2_892-1.
- Zhu & Burer, "An Extended Validity Domain for Constraint Learning", *INFORMS J. Computing*, online 27 Jan 2026, DOI 10.1287/ijoc.2024.0815; arXiv 2406.10065.
- Tong, Zhu, Serra & Burer, "Optimization over Trained Neural Networks: Going Large with Gradient-Based Algorithms", CPAIOR 2026, LNCS pp. 596–613, DOI 10.1007/978-3-032-27242-3_35; arXiv 2512.24295.
- Burer, Natarajan (and Willemsen from v3), "On the Semidefinite Representability of Continuous Quadratic Submodular Minimization With Applications to (Pricing and) Moment Problems", arXiv 2504.03996. v1 4 Apr 2025, v2 5 Apr 2026, v3 31 Aug 2026. The claim was narrowed across versions (§3).
- Burer & Anstreicher, "Applications of the Lorentz positive cone in nonconvex quadratic optimization", arXiv 2609.32017 (25 Sep 2026), including the two-trust-region subproblem.

### 1.10 Era and resource context by period [practice, P unless marked]

| Period | Seniority and setting | Funding acknowledged or listed | Tools seen in the papers | Team pattern |
|---|---|---|---|---|
| 2001–05 | PhD student at Georgia Tech until Aug 2001, then assistant professor, Management Sciences, Iowa (CV) | NSF CCR-0203426, acknowledged in the 2005 paper. The CV lists the collaborative grant ($255,818, "2000-05") | ANSI C. The 2003 runs used an SGI Origin2000 with 16 300 MHz R12000 processors, but "each code uses only one processor" (2003, p. 341). The 2005 runs used a Pentium at 2.4 GHz with 1 GB RAM. Competitors' codes were freely available (2003, p. 356) | the advisor plus one Rice collaborator; then Iowa colleagues and external peers |
| 2006–10 | assistant → associate professor (Jul 2007); visits to CMU (Jan–May 2007) and Sapienza (Apr–May 2009) (CV) | NSF CAREER CCF-0545514 (2006–12), acknowledged in 2008–2013 papers | ILOG CPLEX 9 for convex-QP subproblems, on a Pentium 4 at 2.4 GHz under Linux (2008); MATLAB `R2008a` on a Linux PC (OptDNN); SeDuMi | 2-author papers with peers; the first students (Choi, Chen, Dong) |
| 2011–15 | associate → full professor (Jul 2012). In 2011 he held six associate editorships plus the *Optima* co-editorship (CV) | CAREER to 2012; **no later external research grant in the CV** | SeDuMi 1.3 under MATLAB `R2012a` on an Intel Core 2 Quad (SOC-TRS); the global solver Couenne used to verify a counterexample | Anstreicher, Letchford, Kim–Kojima, Kılınç-Karzan; students Yang and Xu |
| 2016–20 | full professor; faculty director of analytics master's programs 2014–2020 (CV) | none listed | OO and arXiv preprints | students Xu and Park, visitor Eltved; Ye; Anstreicher |
| 2021–26 | chaired professor; Director of Graduate Studies 2023–25; DEO 2025– (CV) | none listed | code released with papers; recent tooling is in `06-trajectory.md` and was not re-checked here | Anstreicher; students Park and Zhu; departmental colleague Serra; SUTD (Natarajan, Willemsen); Michigan (Gilman, Balzano) |

---

## 2. Signature works, dissected (framework §五)

| ID | Work | Why it is a signature work |
|---|---|---|
| S1 | Burer & Monteiro 2003 (with the 2005 follow-up) | Most cited (#1 and #3 in §1.3). Both of his named prizes are for it. He chose it for a retrospective lecture (2023) |
| S2 | Burer 2009, copositive representation | His most-cited sole-authored paper. It opens the copositive line (22 talks), and he calls it "the core" of his 2015 expository paper |
| S3 | Burer & Vandenbussche 2008 (with COAP 2009 and the award note) | The turn from SDP algorithms to global nonconvex QP, which leads into his MIQCP/MINLP work. COAP Best Paper Award 2009. The only first-hand (joint) origin narrative I found for any of his papers |
| S4 | Burer & Letchford 2012 survey (with Burer & Saxena, "The MILP Road to MIQCP") | #2 on Scholar. His stated view of non-convex MINLP and MIQCP, the field this team covers |
| S5 | Burer & Anstreicher 2013, SOC-RLT for extended TRS | Starts the longest live thread in his recent work (TRS/SOC-RLT, 2011 → 2026), and is the template for his later convex-hull papers |

### S1. "A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization" (2003), with "Local minima and convergence in low-rank semidefinite programming" (2005)

**Identifiers**:
- 2003 paper: *Math. Program.* Ser. B 95(2):329–357, DOI 10.1007/s10107-002-0352-8. Posted on OO 9 Mar 2001 (2001/03/296); "Received: March 22, 2001 / Accepted: August 30, 2002".
- 2005 follow-up: *Math. Program.* Ser. A 103(3):427–444, DOI 10.1007/s10107-004-0564-1. Posted on OO 29 Sep 2003; received 30 Sep 2003.

**Origin**:
- [stated, P] (2023 SIAM slides, slide 27 of 63): "The MaxCut SDP was derived by replacing U U T with X ⪰ 0; U was square" / "Peinado and Homer (1997) proposed to optimize directly with U (instead of X)" / "B and Monteiro (2001) saved time and space by taking U lower triangular" / "These papers converted the convex SDP into a nonconvex problem" / "It worked in practice, but why?" (the ⪰ is restored; the text layer drops it).
- [stated-joint, P] (2003 paper): "The current paper follows the path laid by these alternative methods and is specifically motivated by [15, 4]" (p. 330). Here [15] = Homer & Peinado, *J. Parallel Distrib. Comput.* 46(1):48–61, 1997, DOI 10.1006/jpdc.1997.1381, and [4] = Burer & Monteiro, *Optim. Methods Softw.* 15(3–4):175–200, 2001, DOI 10.1080/10556780108805818.
- The new step was to size the factor by a rank theorem: "To answer Q1, we appeal to a theorem of Barvinok [1] and Pataki [21]" (p. 331). These are Barvinok, *Discrete Comput. Geom.* 13(2):189–202, 1995, DOI 10.1007/BF02574037, and Pataki, *Math. Oper. Res.* 23(2):339–358, 1998, DOI 10.1287/moor.23.2.339. The 2023 slide 28 adds Shapiro 1982.
- First implementation [stated, P] (March 2023 talk, machine transcript):
  - "it looks like the day was the 22nd of May 2000";
  - "I told him I did it I implemented it and convergence is good";
  - a day later, "I'd been able already to streamline it and get it roughly 30 times faster".
- Decision rule: "Can't hurt to try" (2023 slides, slide 30 of 63) and "we thought you know it couldn't hurt to try" (machine transcript). [stated, P]
- Motive: "so we were very motivated by just sort of having a fast code" (machine transcript). [stated, P]
- How the advisor worked with him: "Montero was very nice to me I would go by all the time and would talk to me as much as I wanted to talk" (machine transcript). [stated, P]

**Why then**:
- "At the turn of the millenium, researchers were solving bigger SDPs more efficiently, often using first-order methods" (2023 slides, slide 26). [stated, P]
- In 2003: "in practice, the theoretically efficient algorithms developed for SDP are actually quite time- and memory-intensive" (p. 329). [stated-joint, P]
- The benchmark arena existed. The Seventh DIMACS Implementation Challenge (cited as [8]) supplied the torus max-cut instances, and he presented the algorithm there in November 2000 (CV P114). The competitors' codes were public: the paper thanks "Helmberg, Rendl, and Kiwiel as well as Benson, Ye, and Zhang for making their code freely available for comparison" (p. 356). [practice, P]
- Resources: a PhD student, ANSI C, and one processor of a borrowed SGI Origin2000 (p. 341). Part of the work was done in Japan, hosted by T. Tsuchiya (acknowledgments, pp. 355–356). [practice, P]

**Key insight**: "The algorithm's distinguishing feature is a change of variables that replaces the symmetric, positive semidefinite variable X of the SDP with a rectangular variable R according to the factorization X = RRT. The rank of the factorization, i.e., the number of columns of R, is chosen minimally so as to enhance computational speed while maintaining equivalence with the SDP." (abstract, p. 329; "RRT" = RRᵀ in the text layer) [stated-joint, P]

**Minimum evidence**:
- The first night's run ("convergence is good"). [stated, P]
- In the paper: max-cut SDPs on DIMACS torus graphs. For `toruspm3-15-50` (3,375 vertices) the times are 25.7 s (LR5) against 288.2 s (spectral bundle, SB) and 2,311.8 s (DSDP) (Table 11, p. 350). Lovász theta SDPs followed. [practice, P]
- The paper's own reading: "we believe that LR5 will make the solution of maxcut SDPs for sparse graphs with tens of thousands of vertices a routine activity", and on Lovász theta, "to the best of our knowledge, the computational results in this paper represent the best progress made on solving the Lovász SDP to date" (p. 355). [stated-joint, P]

**Abandoned paths** (all documented in the 2003 paper or the talk) [stated-joint / stated, P]:
- **Dynamic rank for the Lovász SDP**: dropped, because "the theoretical base for dynamically changing the rank is not strong" and convergence for small r was poor (p. 342).
- **One penalty parameter per constraint**: "we also tested a version of our algorithm in which each penalty was assigned its own penalty parameter, but even the individual parameters were likely to increase to high values" (p. 343). A single parameter with aggressive multiplier updates was kept.
- **No positive-semidefiniteness test of the dual slack**: partly because "an efficient routine for testing positive semidefiniteness was not readily available" (p. 343).
- **Second-order information never used**: "we only uh looked at first order methods we never did anything with the second or a second derivative of information" (machine transcript).
- **Theory deferred.**
  - 2003: "our belief that the method is not strongly affected by the inherent nonconvexity of (2) is largely experimental" (p. 331), and "Although we have some theoretical justification that explains the observed practical convergence, we do not currently have a formal convergence proof" (p. 355).
  - 2005: the follow-up proves "the optimal convergence of a slight variant of the successful, yet experimental, algorithm of Burer and Monteiro [5]" (abstract, p. 427).
  - 2023, looking back on that proof: "we had some kind of strong assumptions here but this was the best variable to do at that time" (machine transcript; probably "the best we were able to do", but I quote the caption as it stands).

**Reception**:
- **Slow, then large.** 74% of dated S2 citations come from 2015 or later (§1.4). [observed, S]
- **Prizes.**
  - INFORMS Computing Society Prize 2020 "for his pioneering work on low-rank semi-definite programming" (Iowa Now, 19 Aug 2020). According to Georgia Tech, ICS "particularly noted" the 2003 and 2005 papers (GT ISyE news, 14 Sep 2020).
  - Inaugural SIAM SIAG/OPT Test of Time Award 2023 for the 2003 paper (Tippie news, 31 Jan 2023; CV).

  [observed, S]
- **Why it was unusual**, in P. Van Hentenryck's words: "What is unusual here is the fact that these results were obtained almost two decades ago and have seen a new life in recent years." (GT ISyE news, 14 Sep 2020) [observed, S]
- **How others named it** (S2 citation snippets; full texts not read) [observed, S]:
  - "This technique is sometimes referred to as the Burer-Monteiro heuristic" (Davenport & Romberg 2016, *IEEE JSTSP* 10(4):608–622, DOI 10.1109/JSTSP.2016.2539100);
  - "a low-rank factorization heuristic proposed over a decade ago in [BM03]" (Bandeira 2016, *PNAS* 113(16):4238–4239, DOI 10.1073/pnas.1603405113);
  - "Burer and Monteiro [15, 16] popularized the idea of solving classic SDPs by representing the solution as a product of two factor matrices" (Bhojanapalli, Kyrillidis & Sanghavi, arXiv 1509.03917);
  - "demonstrated that it is often effective in practice" (Lemon, So & Ye 2016, *Found. Trends Optim.* 2(1–2):1–156, DOI 10.1561/2400000009).
- **Critique**: "The augmented Lagrangian approach introduced in [7], although quite effective in practice, has two intrinsic drawbacks, since a sequence of unconstrained minimizations need to be performed, and some a posteriori assumptions on the behavior of the sequence are needed in order to prove global…" (Grippo, Palagi & Piccialli 2011, *Math. Program.* 126(1):119–146, DOI 10.1007/s10107-009-0275-8; the S2 snippet ends at "global…"; full text not read). [observed, S]
- **Theory supplied by others**, which he presents in 2023 (machine transcript and slides): Boumal, Voroninski & Bandeira, "The non-convex Burer-Monteiro approach works on smooth semidefinite programs", arXiv 1606.04970 (NIPS 2016); Cifuentes & Moitra, "Polynomial time guarantees for the Burer-Monteiro method", arXiv 1912.01745. [observed, S]
- **His own reading**:
  - "we didn't really mean it but this was part of what people started to call benign non-convexity" (machine transcript);
  - "this is all up to maybe around 2003 or 2004" (machine transcript). His last low-rank *algorithm* paper was posted in July 2004 (OO 2004/07/904; Burer & Choi, *OMS* 21(3):493–512, 2006, DOI 10.1080/10556780500286582). [practice, P]

  [stated, P]

**Methods it shows**: P1 (lift or reformulate so the hard constraint disappears, and size the reformulation with a structural theorem) and P2 (prototype first, benchmark against the best public codes, accept partial theory) in §4.

### S2. "On the copositive representation of binary and continuous nonconvex quadratic programs" (2009, sole author)

**Identifiers**: *Math. Program.* Ser. A 120(2):479–495, DOI 10.1007/s10107-008-0223-z.
- Posted on OO 23 Oct 2006 (2006/10/1501). The manuscript is dated 25 Oct 2006 and revised 10 Jan 2007 and 18 Jul 2007.
- "Received: 27 November 2006 / Accepted: 26 March 2008 / Published online: 29 April 2008"; printed September 2009.

**Origin**:
- [stated, P] The paper places itself as the generalization of a short list: "as far as we are aware, the following is a complete list of all problems known to have representations as COPs: standard quadratic programming [3], the maximum stable set problem [7], and quadratic programs over transportation matrices satisfying specialized quadratic constraints [15]" (p. 479). It then asks: "Other than the handful of problems listed above, what types of problems can be represented as COPs or as CPPs?" (p. 480).
- [stated, P] The acknowledgments name who shaped it: "Janez Povh for clarifying and detailing earlier results on copositive representations; Kurt Anstreicher for insightful comments on a draft of this paper; Immanuel Bomze for pointing out an earlier error in Proposition 2.3; and Mirjam Dür for discussions concerning the extension to complementarity constraints" (p. 495).
- [practice, P] His first documented contact with copositivity is Anstreicher & Burer, "D.C. Versus Copositive Bounds for Standard QP", *J. Glob. Optim.* 33(2):299–312, 2005, DOI 10.1007/s10898-004-4312-0 (OO May 2003).
- **No first-person account of how the question arose was found.** That the Iowa work with Anstreicher led to it is [inferred].

**Why then** [inferred, on cited evidence]:
- The special cases had just accumulated: Bomze et al., de Klerk & Pasechnik, Povh, Povh & Rendl, all cited on p. 479.
- Approximation hierarchies for the copositive cone (Parrilo; Bomze & de Klerk) existed (p. 480).
- His NSF CAREER award (CCF-0545514, acknowledged on p. 479) had just started (June 2006, per the CV's 2006–12).
- Resources: an assistant professor, working alone, on theory; there are no experiments in the paper. [practice, P]

**Key insight**: [stated, P]
- Write all linear constraints as equations and assume (the "key assumption", p. 481) that the linear constraints imply 0 ≤ xⱼ ≤ 1 for the binary variables. Then the mixed-binary QP is a linear program over the completely positive cone.
- In his words: "While expressing a problem as a COP or CPP does not resolve the difficulty of the problem, it does allow one to "package" the difficulty completely inside the convex cones of copositive and/or completely positive matrices. Whatever knowledge is then gained about copositive or completely positive matrices can be applied uniformly to multiple types of NP-hard problems." (p. 480)
- He also states its limits:
  - "The primary purpose of the current paper is theoretical--to demonstrate that a broad class of NP-hard problems can be modeled as a specific class of well-structured convex programs. However, a long-term goal is certainly to provide new practical tools for computationally solving difficult optimization problems." (p. 493)
  - "So the results of this paper are not a "magic bullet" for solving NP-hard problems." (p. 493)

**Minimum evidence**:
- A proof. There is no computation for the main result. [practice, P]
- The first evidence of usefulness, as the paper reports it: Anstreicher and Burer used the result for the 2-variable box hull, "answering a fundamental open question in the field of global optimization"; Povh and Rendl derived a strong QAP relaxation from the CP representation (p. 494). [stated, P]
- Computation came in the follow-ups: OptDNN (*MPC* 2(1):1–19, 2010, DOI 10.1007/s12532-010-0010-8) and QuadProgBB (*MPC* 2012, §1.3 #8). [practice, P]

**Abandoned paths and version changes** [practice, P]:
- **Scope widened.** The original OO abstract (Wayback copy of 10 Nov 2006) reads: "We establish that any nonconvex quadratic program having a mix of binary and continuous variables over a bounded feasible set can be represented as a linear program over the dual of the cone of copositive matrices."
- By the 18 Jul 2007 revision, the main theorem no longer needs boundedness: unbounded feasible sets are handled through the recession cone of the linear part, and the bounded case becomes "Corollary 2.5 If Feas(P) is bounded, then Feas+(P) = Feas+(C)". The final abstract also adds "A simplification, which reduces the dimension of the linear conic program, and an extension to complementarity constraints".
- **An error caught before publication** by Bomze (Proposition 2.3). The October 2006 PDF is no longer on OO, so what the error was: **not read**.

**Reception**:
- The positive reception, quoted from S2 citation snippets (full texts not read) [observed, S]:
  - "Copositive optimization experienced a breakthrough with Burer's 2009 paper [25]." (Dür & Rendl 2021, *EURO J. Comput. Optim.* 9:100021, DOI 10.1016/j.ejco.2021.100021);
  - "a generalization of the celebrated result in Burer (2009)" (Bomze & Gabl 2021, *Math. Methods Oper. Res.* 93(1):115–151, DOI 10.1007/s00186-020-00726-6);
  - "A seminal result by Burer [11] shows that – under mild assumptions – binary quadratic problems can also be reformulated as optimization problems over the completely positive cone." (Badenbroek & de Klerk 2022, *INFORMS J. Comput.* 34(2):1115–1125, DOI 10.1287/ijoc.2021.1108);
  - Fawzi, Gouveia, Parrilo, Saunderson & Thomas call its 0/1-polytope consequence "a striking result" (*SIAM Rev.* 64(4):866–918, 2022, DOI 10.1137/20M1324417).
- Citation profile: 440 of 479 citing papers are in mathematics, and S2 counts 81 or 87 as influential (§1.4). [observed, S]
- His own continuation [practice, P]:
  - Burer & Dong, QCQP as generalized copositive programs, *ORL* 40(3):203–206, 2012, DOI 10.1016/j.orl.2012.02.001;
  - the 2012 chapter;
  - the 2015 "gentle introduction", *Math. Program.* 151(1):89–116, DOI 10.1007/s10107-015-0888-z;
  - copositive two-stage robust optimization with Xu, *COAP* 70(1):33–59, 2018, DOI 10.1007/s10589-017-9974-x.

**Methods it shows**: P1 (package the difficulty in one object, then study that object) and P5 (follow a representation result with computation and expository entry points).

### S3. "A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations" (2008), with the box-QP sequel (2009) and its award note

**Identifiers**:
- 2008 paper: *Math. Program.* Ser. A 113(2):259–282, DOI 10.1007/s10107-006-0080-6. Posted on OO 27 Jun 2005 as "Semidefinite-Based Branch-and-Bound for Nonconvex Quadratic Programming" (2005/06/1167); "Received: 27 June 2005 / Accepted: 30 October 2006".
- Sequel: "Globally solving box-constrained nonconvex quadratic programs with semidefinite-based finite branch-and-bound", *Comput. Optim. Appl.* 43(2):181–195, 2009, DOI 10.1007/s10589-007-9137-6.
- Award note: "COAP 2009 best paper award", *Comput. Optim. Appl.* 47(3):567–570, 2010, DOI 10.1007/s10589-010-9368-9.

**Origin** [stated-joint, P]:
- The award note is written in the third person. Its "we obtain" in the Axioma paragraph suggests that at least part was written by the awardees [inferred].
- "This paper describes work done by the authors during the years 2002-2007. It was part of a collaboration mostly motivated by the desire of each author to gain a greater understanding of the other's field of expertise." (p. 567)
- The starting problem was SDP relaxations of 0-1 integer programs in the Lovász–Schrijver line (*SIAM J. Optim.* 1(2):166–190, 1991, DOI 10.1137/0801013). For realistic instances these "posed a serious computational challenge for existing SDP algorithms" (p. 567). That led to their large-scale lift-and-project solver: Burer & Vandenbussche, *SIAM J. Optim.* 16(3):726–750, 2006, DOI 10.1137/040609574.

**Why then**:
- Vandenbussche & Nemhauser had just published a finite, LP-based branch-and-cut for box-constrained QP: *Math. Program.* 102(3):531–557 (DOI 10.1007/s10107-004-0549-0) and 559–575 (DOI 10.1007/s10107-004-0550-7), 2005. The award note names this as the second motivation (p. 568). [stated-joint, P]
- Their own augmented-Lagrangian/block-coordinate SDP solver was ready. [stated-joint, P]
- Resources [practice, P]:
  - Burer was an assistant professor at Iowa; Vandenbussche was at UIUC "until 2006", then at Axioma (note, p. 570).
  - Convex-QP subproblems were "solved using CPLEX by ILOG, Inc." (2008, p. 273).
  - The runs used a Pentium 4 at 2.4 GHz under Linux.

**Key insight**:
- "One idea, which guarantees a finite number of branching decisions, is to enforce the first-order Karush-Kuhn-Tucker (KKT) conditions through branching. … However, the LP relaxations are unbounded, a fact that precludes their use. In this paper, we propose and study semidefinite programming relaxations, which are bounded and hence suitable for use with finite KKT-branching." (abstract, p. 259) [stated-joint, P]
- In the award note's words: "The hard part was that the resulting LP and SDP relaxations were unbounded. However, by combining features of both relaxation types, the authors overcame this hurdle" (p. 568). [stated-joint, P]

**Minimum evidence**:
- From the earlier project: "Somewhat surprisingly, computational experiments showed that the dual multipliers converged reasonably well even when the subproblems were solved very loosely by only a few cycles of block coordinate descent." (note, p. 568) [stated-joint, P]
- In 2008: "when a 1% optimality tolerance is used, almost all instances can be solved at the root, which indicates the strength of the proposed SDP relaxations" (p. 280). [stated-joint, P]
- In 2009, on box QP with up to 100 variables, the method "far outperformed the LP-based branch-and-cut method of Vandenbussche and Nemhauser" (note, p. 569). [stated-joint, P]

**Abandoned paths** [stated-joint, P]:
- **The original target, 0-1 integer programs, was dropped**: "For globally optimizing linear IPs, the authors began to realize that, even with better techniques for the SDP relaxations, these relaxations could still be ineffective, either because the bounds might still be too weak on a given problem class, or because solving the SDPs, even approximately, might still be more time-consuming than a standard IP solver, which can evaluate many nodes of a branch-and-bound tree by quickly reoptimizing linear programming (LP) relaxations using the dual simplex method." Then: "So the authors shifted their focus away from IPs to continuous problems" (both p. 568).
- **Test instances were dropped**: after rescaling Globallib instances, "this rescaling introduced some occasional numerical failures in CPLEX when solving convex QP subproblems in the AL method. We have omitted instances where such issues where encountered." (2008, p. 281)
- **The title changed** from "Semidefinite-Based Branch-and-Bound…" (OO 2005) to "A finite branch-and-bound algorithm…" (2008). The reason is not stated [practice, P].

**Reception**:
- COAP Best Paper Award 2009 for the sequel (CV; note). [observed, S]
- Scholar 217 + 113 citations; S2 178 (10 influential) + 87 (5 influential). [observed, S]
- Self-reported influence: "the box-constrained case of non-convex QP has become a standard test case in mixed integer nonlinear programming (MINLP)" (note, p. 569). [stated-joint, P]
- The authors' lessons [stated-joint, P]:
  - "To the authors knowledge, this is one of the first clear examples in which an SDP-based branch-and-bound algorithm outperforms an LP-based one."
  - "it can be worthwhile to pay for a computationally expensive, but strong, relaxation compared to evaluating many inexpensive relaxations"
  - "simple, classic ideas such as augmented Lagrangian and block coordinate descent still have an important role to play in modern, large-scale optimization" (all p. 569).
- Successor: QuadProgBB (§1.3 #8). Later box-QP work by others: Bonami, Günlük & Linderoth, *Math. Program. Comput.* 10(3):333–382, 2018, DOI 10.1007/s12532-018-0133-x. In an S2 snippet, they write of SDP relaxations that "these relaxations have been successfully used in practice to obtain tight bounds for zboxqp"; full text not read. [observed, S] The head-to-head record against later MILP-based and spatial branch-and-bound codes is covered in `05-peer-critique.md` and was not re-checked here.

**Methods it shows**: P3 (import an exact or finite mechanism from a neighbouring field and pair it with the strongest bound one's own field offers) and P2. Contradiction 3 records a tension inside the paper.

### S4. "Non-convex mixed-integer nonlinear programming: A survey" (2012), with "The MILP Road to MIQCP" (2012)

**Identifiers**:
- Survey: *Surveys in Operations Research and Management Science* 17(2):97–106, DOI 10.1016/j.sorms.2012.08.001. Posted on OO 29 Feb 2012 (2012/02/3378); "Received 9 July 2012, Accepted 8 August 2012" (Contradiction 8).
- Companion: Burer & Saxena, "The MILP Road to MIQCP", in *Mixed Integer Nonlinear Programming* (IMA Vol. Math. Appl. 154, eds. J. Lee and S. Leyffer per the CV), 373–405, DOI 10.1007/978-1-4614-1927-3_13. Posted on OO 8 Jul 2009 as "Old Wine in a New Bottle: The MILP Road to MIQCP" (2009/07/2338).

**Origin**:
- Not documented by the authors (Gaps).
- Context [practice, P]: he was an associate editor of *SORMS* in 2009–13 (CV). He and Letchford had already written two papers together:
  - box QP, *SIOPT* 2009, posted July 2008;
  - "Unbounded convex sets for non-convex mixed-integer quadratic programming", *Math. Program.* 143(1–2):231–256, 2014, DOI 10.1007/s10107-012-0609-9, posted September 2011.
- Whether the survey was invited: not found.

**Why then**: "we pay particular attention to a special case that has attracted a great deal of attention recently, and which is also of interest to ourselves: namely, the case in which all of the nonlinear functions involved are quadratic" (p. 98). [stated-joint, P]

**Key insight and stance** [stated-joint, P]:
- "When non-convexities are present, however, things become much more difficult, since then even the continuous relaxation is a global optimization problem." (abstract, p. 97)
- On the scale of the difficulty: "some relatively small non-convex MINLPs, with just tens of variables, can cause existing methods to run into serious difficulties" (p. 98).
- The 2009 chapter sets the programme (preprint, PDF of 23 Apr 2010):
  - "although significant progress has been made in the field of MIQCP, the "breakthrough" results are yet to come and we believe that the past of MILP holds the clues to the future of MIQCP" (p. 1);
  - "In this sense, we view (MIQCP) as a natural progression from MILP rather than, say, a special case of MINLP" (p. 2);
  - "We are also not specifically concerned with the global optimization of (MIQCP). Rather, we focus on generating strong convex relaxations and valid inequalities, which could become the basis of efficient global techniques." (p. 2)
- The survey's conclusions take positions:
  - "We also advocate the development of algorithms for various special cases of non-convex MINLPs." (p. 103)
  - On convex hulls: "analyzing -- and generating cutting planes for -- the various convex hulls that arise in MINLPs (see Section 5.4) will require aspects of both polyhedral theory and convex analysis to achieve best results" (p. 103).
  - "Special cases can also allow the development of newer techniques (e.g., semidefinite relaxations), which may then progress to more general techniques." (p. 104)
  - "Finally, we believe there will be an increasing place for heuristics and approximation algorithms for non-convex MINLPs. Most techniques so far aim for globally optimal solutions, but in practice it would be valuable to have sophisticated approaches for finding near-optimal solutions." (p. 104)

**Minimum evidence**: not applicable for the survey. The chapter adds "brief computational results to indicate the strength and computational requirements of these methods" (abstract). It also judges the computational setting: "Such LP relaxations are extremely desirable for branch-and-bound algorithms for two reasons. One, they can be efficiently re-optimized using warm-starting capabilities of LP solvers…" (preprint p. 29), whereas the SDP-type relaxations "are currently solved by interior point methods that lack efficient re-optimization capabilities making them bottlenecks in a branch-and-bound procedure" (preprint p. 30). [stated-joint, P]

**Abandoned paths**: none documented. The chapter title lost "Old Wine in a New Bottle:" between the 2009 preprint and the book. The reason is not stated [practice, P].

**Reception**:
- Scholar 859 citations; S2 636, of which 20 influential. [observed, S]
- Citing fields and venues are mostly applied engineering (§1.4). [observed, S]
- The CV lists it as a 2014 top-5 download of the journal. [stated, P]
- His own output does not follow the call for heuristics (Contradiction 2) [practice, P; reading inferred]. It does follow the calls for special cases and convex hulls: categories F and G in §1.1, and the 2021 plenary on substructures (§4, P4).

**Methods it shows**: P4 (special cases and substructures as the route to general methods), P5 (write the entry point) and P3 (MILP as the template).

### S5. "Second-order-cone constraints for extended trust-region subproblems" (2013), and the thread it started

**Identifiers**:
- *SIAM J. Optim.* 23(1):432–451, DOI 10.1137/110826862.
- Posted on OO 7 Mar 2011 (2011/03/2957). The manuscript is dated 4 Mar 2011 and revised 7 Jul 2012 and 16 Nov 2012.
- The original OO abstract page (Wayback, 23 Apr 2011) matches the final abstract, so the headline claims survived two revisions. [practice, P]

**Origin** [stated-joint, P]:
- "(As far as we are aware, [21] is the only paper in the literature to study TRS2p formally, and in fact this paper motivated our study here.)" and "The authors of [21] asked whether there are exact convex formulations of TRS2p and TTRS." (preprint p. 3) Here [21] = Ye & Zhang, "New results on quadratic minimization", *SIAM J. Optim.* 14(1):245–267, 2003, DOI 10.1137/S105262340139001X.
- The constraint they generalize comes from Sturm & Zhang, *Math. Oper. Res.* 28(2):246–267, 2003, DOI 10.1287/moor.28.2.246.14485. Its derivation "appears to be unique in the literature" (preprint p. 2).
- They name the general construction: "We call an SOC constraint obtained in this fashion an "SOC-RLT" constraint." (p. 2)

**Why then** [inferred]:
- Both authors were at Iowa and had just finished joint convex-hull work (Anstreicher & Burer 2010, §1.3 #10).
- The CAREER grant is acknowledged.
- Resources: SeDuMi 1.3 under MATLAB `R2012a` on a quad-core desktop (preprint). [practice, P]

**Key insight**:
- Multiply a valid second-order-cone constraint by a nonnegative linear factor and linearize the product in the lifted space (x, X). This gives an exact SDP + SOC representation of TRS with two parallel cuts, and a polynomial-time separable family of cuts that strengthens the SDP relaxation of the two-trust-region subproblem (TTRS). [stated-joint, P]
- The general lesson they draw: "An important implication of our results is that the computational complexity of solving an extended trust-region problem is highly dependent on the geometry of the feasible set." (p. 3) [stated-joint, P]

**Minimum evidence** [stated-joint / practice, P]:
- The Sturm–Zhang one-cut result is re-proved first, because "Our proof of this result introduces important machinery that will be required later in the paper" (p. 3).
- The three Ye–Zhang TTRS instances with a relaxation gap are closed exactly: "we obtain r+(TTRS) = v(TTRS) for each of the three instances" (p. 16).
- Random TTRS instances were built from Martínez (*SIAM J. Optim.* 4(1):159–176, 1994, DOI 10.1137/0804009). The construction followed a suggestion credited in a footnote: "We thank Henry Wolkowicz for this valuable suggestion" (p. 18). Results (Table 1, p. 23):

  | n | solved by the basic SDP | solved after adding SOC-RLT cuts | unsolved |
  |---|---|---|---|
  | 5 | 92.2% | 3.7% | 4.1% |
  | 10 | 24.6% | 68.4% | 7.0% |
  | 20 | 4.1% | 85.5% | 10.4% |

**Abandoned and failed paths** [stated-joint, P]:
- **Two non-intersecting cuts: conjectured, not proved.** "We have not been able to prove whether v(TRS2) equals r(TRS2) in this case … we have tested many random instances of TRS2 with non-intersecting cuts in low dimensions (n ≤ 10) and have always found empirically that r(TRS2) does equal v(TRS2). So we conjecture that the two values are equal when the cuts do not intersect." (p. 13)
- **Intersecting cuts: a counterexample** with a gap of about 7%, verified with a global solver: "Using the global optimization software Couenne [3], one can verify…" (p. 13).
- **TTRS: not exact.** A two-dimensional example where the strengthened relaxation "still leaves a 0.9% gap to the true solution value" (p. 17), plus the unsolved shares in the table above.
- **Afterwards**: the conjecture was proved for any number of non-intersecting cuts by Burer & Yang, *Math. Program.* 149(1–2):253–264, 2015, DOI 10.1007/s10107-014-0749-1 (received 22 Feb 2013). Its acknowledgments thank Anstreicher "for suggesting first that the case m = 2 might be extensible to arbitrary m".

**Reception and continuation**:
- Scholar 134 citations; S2 120 (14 influential). [observed, S]
- His own thread [practice, P]:
  - Yang & Burer, TTRS, *SIOPT* 26(1):661–680, 2016, DOI 10.1137/130945880;
  - Yang, Anstreicher & Burer, hollows, *Math. Program.* 170(2):541–553, 2018, DOI 10.1007/s10107-017-1157-0;
  - Eltved & Burer, *Math. Program.* 197(1):281–306, 2023, DOI 10.1007/s10107-021-01737-9;
  - the 2025 ball-constraint paper;
  - arXiv 2609.32017 (2026), which returns to TTRS.
- Origin of the Eltved line, from the 2021 plenary (machine transcript): Chen, Atamtürk & Oren's AC-OPF cuts (*Math. Program.* 165(2):549–577, 2017, DOI 10.1007/s10107-016-1095-2) "to me they don't instantaneously tell you where these numbers coming from and what's really going on and that's where our motivation came from" [40:54]. The resulting paper shows those cuts are special cases of the new ones: "previously derived cuts capturing a convex hull important for OPF are actually just special cases of our cuts" (arXiv 2009.12704v2 abstract). [stated, P]
- Outside use: Anstreicher's later TTRS paper (*JOTA* 202(1):303–319, online 2022, DOI 10.1007/s10957-022-02064-5) takes as its test set "problems … that were considered to be unsolved using SOC-RLT cuts in both [10] and [23]" (S2 snippet; full text not read). [observed, S]

**Methods it shows**: P4 (study a small geometric substructure, let computation produce the conjecture, verify counterexamples with a global solver, hand the open case on) and P6 (report the residue).

---

## 3. Failures, corrections, abandoned directions and slow papers (the publication record)

1. **A published theorem withdrawn and replaced** (Burer & Ye). The paper is "Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", *Math. Program.* 181(1):1–17, 2020, DOI 10.1007/s10107-019-01367-2 (arXiv 1802.02688). The correction is *Math. Program.* 190:845–848, 2021, DOI 10.1007/s10107-021-01684-5, online 8 Jul 2021. [stated-joint, P]
   - "This note reports an error in Theorem 3 of [1], which was pointed about by Prof. Fatma Kılınç-Karzan and Mr. Alex Wang of Carnegie Mellon University, whom we sincerely thank for bringing this to our attention."
   - "However, in truth the proof fails because, with this setup, the systems cannot be simultaneously feasible."
   - "Instead of the purported Theorem 3, we now prove an analogous theorem, except that it only applies to diagonal instances of (1)."
   - The CV lists the erratum next to the paper. His January 2021 talk was already titled "Exact SDPs for a Class of (Random and Non-Random) Nonconvex Diagonal QCQPs" (CV P32). [practice, P]
2. **An overclaim narrowed across arXiv versions** (2504.03996) [stated-joint, P]:
   - v1 (4 Apr 2025): "We show that continuous quadratic submodular minimization with bounds is solvable in polynomial time using semidefinite programming".
   - v2 (5 Apr 2026): "propose a polynomially sized semidefinite relaxation, which is provably tight for dimension $n \le 3$ and empirically tight for larger $n$".
   - v3 (31 Aug 2026): "Via an explicit counterexample for n = 4, we show that the relaxation is not tight in general, although it remains empirically tight on randomly generated instances."
   - The talk titles followed: "Towards the …" in October 2025 (CV P07), then "On the …" in January 2026 (CV P02–P05). [practice, P]
3. **Pre-publication error and scope change** in the copositive paper (S2): Bomze's catch in Proposition 2.3, and "bounded feasible set" dropped between 2006 and 2007. [stated / practice, P]
4. **Options dropped in the 2003 low-rank paper** (S1): dynamic rank, per-constraint penalties, a PSD test, second-order steps. The formal convergence proof came two years later, under strong assumptions. [stated-joint, P]
5. **A target dropped and instances omitted** (S3): 0-1 integer programs were abandoned for continuous QP, and Globallib instances on which CPLEX failed numerically were left out. [stated-joint, P]
6. **Open cases left as conjectures** [stated-joint / stated, P]:
   - TRS with two non-intersecting cuts (2011; proved in 2015).
   - Switching variables, n = 2: "An alternative derivation for this representation leads to an appealing conjecture for a simplified representation of the convex hull for $n=2$ when the product term $y_1y_2$ is ignored" (arXiv 2002.04681 abstract). In the plenary: "unfortunately we weren't able to prove that conjecture" [37:02] and "so this conjecture is still to be proven" [38:41] (machine transcript). Whether it has been proved since: **not checked**.
7. **Slow passages to print** (posting → print) [practice, P]:
   - inventory/newsvendor: Jan 2005 → TOP online Oct 2010 → print Oct 2012 (20(3):707–728, DOI 10.1007/s11750-010-0160-x), retitled from "Convex Optimization of Centralized Inventory Operations" to "Newsvendor games: convex optimization of centralized inventory operations";
   - copositive: Oct 2006 → print Sep 2009;
   - finite branch-and-bound: Jun 2005 → print Jun 2008;
   - MILP road: Jul 2009 → print 2012;
   - SOC-TRS: Mar 2011 → print 2013 (two revisions).

   No referee reports or rejections are public (Gaps).
8. **Directions left with no stated reason** [practice, P; reasons not found]:
   - low-rank SDP algorithms after the July 2004 posting; he returned only as retrospective speaker and code maintainer;
   - global QP solver codes after QuadProgBB (posted Feb 2011; repository last pushed 2016);
   - copositive robust/DRO after student Xu graduated (last posting Aug 2017);
   - operations applications after 2005–2008.

---

## 4. Cross-cutting patterns: candidates for Phase 2 [all inferred from §§1–3]

| # | Pattern | Evidence (signature works and other papers) |
|---|---|---|
| P1 | **Lift, then package the difficulty in one object** that can be studied by itself: a factor sized by a rank theorem, the CP cone, an SOC-RLT constraint in (x, X), a slight lift to n+1 | S1, S2, S5; ball constraints 2025 ("a simple lifting of the original problem into dimension $n+1$") |
| P2 | **Prototype in days, benchmark against the best public codes, accept partial theory** and say so ("largely experimental", "successful, yet experimental") | S1, with dates from the talk; S3 ("Somewhat surprisingly…") |
| P3 | **Import an exact or finite mechanism from a neighbouring field and pair it with the strongest bound available**; use MILP as the template for MIQCP | S3 (KKT branching from the IP side plus SDP bounds); S4 (chapter) |
| P4 | **Shrink to a substructure with few variables or constraints, compute to get conjectures, verify counterexamples with a global solver, state the open case as a conjecture.** In 2021 he justifies the focus: "why do we focus on these substructures it's basically sometimes it's easier to focus on these on these simpler cases where you have" [08:41] "fewer variables and fewer constraints and these really can be the basis for them convexifying more complicated miqps this is a standard technique for example that has been adopted in mixed interlinear program when you look at a one row relaxation or two row relaxation" [09:14] (machine transcript) | S5; switching n = 2 ("we did a lot of computational experiments and we came up with a conjecture" [34:50], machine transcript); S4 ("We also advocate the development of algorithms for various special cases") |
| P5 | **Write the entry point after the core result**: chapter, gentle introduction, survey, tutorial | S2 → 2012 chapter, 2015 introduction, ISMP 2015 semi-plenary; S4; IPCO 2019 tutorial (CV P36) |
| P6 | **Report the residue and narrow claims publicly**: unsolved percentages, residual gaps, omitted instances, corrections that name the finder | S3, S5; §3 items 1–2 |
| P7 | **Treat bound strength against speed as a design choice**, but resolve it differently from paper to paper (Contradiction 1). In 2021 he describes the choice as two questions: "how many how many additional auxiliary variables am i willing to deal with" [09:47] and which constraint class (LP, SOCP, SDP) (machine transcript) | S3 lessons; S4 chapter; Burer, Kim & Kojima, *COAP* 59(1–2):27–45, 2014, DOI 10.1007/s10589-013-9618-8 |

---

## 5. Appendix: the 64-work corpus with checked identifiers [practice, P; bibliographic data from Crossref (S)]

All DOIs were resolved through Crossref in this run, and all arXiv ids on arxiv.org. "First public" is the Optimization Online or arXiv posting month; † marks the print, online or conference date where I found no posting (year only for JMLR and FEJAM). Categories as in §1.1. Authors, titles and page ranges are as Crossref returns them (hyphens in page ranges as given).

| First public | Cat. | Authors | Title | Venue, volume(issue):pages, year | Identifier |
|---|---|---|---|---|---|
| 2001-01 † | A | S. Burer, R. Monteiro | A projected gradient algorithm for solving the maxcut SDP relaxation | Optimization Methods and Software 15(3-4):175-200, 2001 | DOI 10.1080/10556780108805818 |
| 2001-03 | A | S. Burer, R. Monteiro | A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization | Mathematical Programming 95(2):329-357, 2003 | DOI 10.1007/s10107-002-0352-8 |
| 2001-06 | A | S. Burer, R. Monteiro, Y. Zhang | A computational study of a gradient-based log-barrier algorithm for a class of large-scale SDPs | Mathematical Programming 95(2):359-379, 2003 | DOI 10.1007/s10107-002-0353-7 |
| 2001-10 | A | S. Burer, R. Monteiro, Y. Zhang | Solving a class of semidefinite programs via nonlinear programming | Mathematical Programming 93(1):97-122, 2002 | DOI 10.1007/s101070100279 |
| 2002-01 † | A | S. Burer, R. Monteiro, Y. Zhang | Rank-Two Relaxation Heuristics for MAX-CUT and Other Binary Quadratic Programs | SIAM Journal on Optimization 12(2):503-521, 2002 | DOI 10.1137/S1052623400382467 |
| 2002-04 † | A | S. Burer, R. Monteiro, Y. Zhang | Interior-Point Algorithms for Semidefinite Programming Based on a Nonlinear Formulation | Computational Optimization and Applications 22(1):49-79, 2002 | DOI 10.1023/A:1014834318702 |
| 2002-05 | A | S. Burer | Semidefinite Programming in the Space of Partial Positive Semidefinite Matrices | SIAM Journal on Optimization 14(1):139-172, 2003 | DOI 10.1137/S105262340240851X |
| 2002-12 † | A | S. Burer, R. Monteiro, Y. Zhang | Maximum stable set formulations and heuristics based on continuous optimization | Mathematical Programming 94(1):137-166, 2002 | DOI 10.1007/s10107-002-0356-4 |
| 2003-02 † | A | S. Burer, R. Monteiro | A General Framework for Establishing Polynomial Convergence of Long-Step Methods for Semidefinite Programming | Optimization Methods and Software 18(1):1-38, 2003 | DOI 10.1080/1055678031000111227 |
| 2003-05 | D | K. Anstreicher, S. Burer | D.C. Versus Copositive Bounds for Standard QP | Journal of Global Optimization 33(2):299-312, 2005 | DOI 10.1007/s10898-004-4312-0 |
| 2003-09 | A | S. Burer, R. Monteiro | Local Minima and Convergence in Low-Rank Semidefinite Programming | Mathematical Programming 103(3):427-444, 2005 | DOI 10.1007/s10107-004-0564-1 |
| 2004-06 | B | S. Burer, D. Vandenbussche | Solving Lift-and-Project Relaxations of Binary Integer Programs | SIAM Journal on Optimization 16(3):726-750, 2006 | DOI 10.1137/040609574 |
| 2004-07 | A | S. Burer, C. Choi | Computational enhancements in low-rank semidefinite programming | Optimization Methods and Software 21(3):493-512, 2006 | DOI 10.1080/10556780500286582 |
| 2005-01 | I | S. Burer, M. Dror | Newsvendor games: convex optimization of centralized inventory operations | TOP 20(3):707-728, 2012 | DOI 10.1007/s11750-010-0160-x |
| 2005-03 | B | S. Burer, J. Lee | Solving maximum-entropy sampling problems using factored masks | Mathematical Programming 109(2-3):263-281, 2007 | DOI 10.1007/s10107-006-0024-1 |
| 2005-06 | C | S. Burer, D. Vandenbussche | A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations | Mathematical Programming 113(2):259-282, 2008 | DOI 10.1007/s10107-006-0080-6 |
| 2005-11 † | I | Yi Zhang, W. Street, S. Burer | Sharing Classifiers among Ensembles from Related Problem Domains | Fifth IEEE International Conference on Data Mining (ICDM'05):522-529, 2005 | DOI 10.1109/ICDM.2005.131 |
| 2006 † | I | Y. Zhang, S. Burer, W.N. Street | Ensemble Pruning Via Semi-definite Programming | J. Mach. Learn. Res. 7:1315-1338, 2006 | DBLP record (journals/jmlr); no DOI |
| 2006-08 | A | M. Anjos, S. Burer | On Handling Free Variables in Interior-Point Methods for Conic Linear Optimization | SIAM Journal on Optimization 18(4):1310-1325, 2008 | DOI 10.1137/06066847X |
| 2006-10 | D | S. Burer | On the copositive representation of binary and continuous nonconvex quadratic programs | Mathematical Programming 120(2):479-495, 2009 | DOI 10.1007/s10107-008-0223-z |
| 2007-02 | F | K. Anstreicher, S. Burer | Computable representations for convex hulls of low-dimensional quadratic forms | Mathematical Programming 124(1-2):33-43, 2010 | DOI 10.1007/s10107-010-0355-9 |
| 2007-10 | C | S. Burer, D. Vandenbussche | Globally solving box-constrained nonconvex quadratic programs with semidefinite-based finite branch-and-bound | Computational Optimization and Applications 43(2):181-195, 2009 | DOI 10.1007/s10589-007-9137-6 |
| 2007-10 | C | S. Burer, J. Chen | Relaxing the optimality conditions of box QP | Computational Optimization and Applications 48(3):653-673, 2011 | DOI 10.1007/s10589-009-9273-2 |
| 2008-02 † | I | S. Burer, P. Jones, T. Lowe | Coordinating the supply chain in the agricultural seed industry | European Journal of Operational Research 185(1):354-377, 2008 | DOI 10.1016/j.ejor.2006.12.015 |
| 2008-02 | B | S. Burer, J. Chen | A p-cone sequential relaxation procedure for 0-1 integer programs | Optimization Methods and Software 24(4-5):523-548, 2009 | DOI 10.1080/10556780903057341 |
| 2008-05 | D | S. Burer, K. Anstreicher, M. Dür | The difference between 5×5 doubly nonnegative and completely positive matrices | Linear Algebra and its Applications 431(9):1539-1552, 2009 | DOI 10.1016/j.laa.2009.05.021 |
| 2008-07 | C | S. Burer, A. Letchford | On Nonconvex Quadratic Programming with Box Constraints | SIAM Journal on Optimization 20(2):1073-1089, 2009 | DOI 10.1137/080729529 |
| 2008-12 | D | S. Burer | Optimizing a polyhedral-semidefinite relaxation of completely positive programs | Mathematical Programming Computation 2(1):1-19, 2010 | DOI 10.1007/s12532-010-0010-8 |
| 2009-07 | H | S. Burer, A. Saxena | The MILP Road to MIQCP | Mixed Integer Nonlinear Programming, IMA Vol. Math. Appl. 154:373-405, 2012 | DOI 10.1007/978-1-4614-1927-3_13 |
| 2010-05 | D | S. Burer, H. Dong | Separation and relaxation for cones of quadratic forms | Mathematical Programming 137(1-2):343-370, 2013 | DOI 10.1007/s10107-011-0495-6 |
| 2011-02 | C | J. Chen, S. Burer | Globally solving nonconvex quadratic programming problems via completely positive programming | Mathematical Programming Computation 4(1):33-52, 2012 | DOI 10.1007/s12532-011-0033-9 |
| 2011-03 † | B | C. Choi, S. Burer | A semidefinite programming approach to the hypergraph minimum bisection problem | Optimization 60(3):413-427, 2011 | DOI 10.1080/02331930903233744 |
| 2011-03 | G | S. Burer, K. Anstreicher | Second-Order-Cone Constraints for Extended Trust-Region Subproblems | SIAM Journal on Optimization 23(1):432-451, 2013 | DOI 10.1137/110826862 |
| 2011-07 | D | S. Burer, H. Dong | Representing quadratically constrained quadratic programs as generalized copositive programs | Operations Research Letters 40(3):203-206, 2012 | DOI 10.1016/j.orl.2012.02.001 |
| 2011-09 | F | S. Burer, A. Letchford | Unbounded convex sets for non-convex mixed-integer quadratic programming | Mathematical Programming 143(1-2):231-256, 2014 | DOI 10.1007/s10107-012-0609-9 |
| 2011-09 | H | S. Burer | Copositive Programming | Handbook on Semidefinite, Conic and Polynomial Optimization (Int. Ser. Oper. Res. Manag. Sci.):201-218, 2012 | DOI 10.1007/978-1-4614-0769-0_8 |
| 2011-10 | I | S. Burer | Robust Rankings for College Football | Journal of Quantitative Analysis in Sports 8(2), 2012 | DOI 10.1515/1559-0410.1405 |
| 2011-11 | A | J. Chen, S. Burer | A First-Order Smoothing Technique for a Class of Large-Scale Linear Programs | SIAM Journal on Optimization 24(2):598-620, 2014 | DOI 10.1137/110854400 |
| 2012-02 | H | S. Burer, A. Letchford | Non-convex mixed-integer nonlinear programming: A survey | Surveys in Operations Research and Management Science 17(2):97-106, 2012 | DOI 10.1016/j.sorms.2012.08.001 |
| 2013-02 | G | S. Burer, B. Yang | The trust region subproblem with non-intersecting linear constraints | Mathematical Programming 149(1-2):253-264, 2015 | DOI 10.1007/s10107-014-0749-1 |
| 2013-04 | F | S. Burer, S. Kim, M. Kojima | Faster, but weaker, relaxations for quadratically constrained quadratic programs | Computational Optimization and Applications 59(1-2):27-45, 2014 | DOI 10.1007/s10589-013-9618-8 |
| 2013-11 | G | B. Yang, S. Burer | A Two-Variable Approach to the Two-Trust-Region Subproblem | SIAM Journal on Optimization 26(1):661-680, 2016 | DOI 10.1137/130945880 |
| 2014 † | I | N. Cho, S. Burer, A.M. Campbell | Modifying Soyster's Model for the (Symmetric) Traveling Salesman Problem with Interval Travel Times | Far East J. Appl. Math. 86(2):117-144, 2014 | CV [J29] (title without "Symmetric") and Google Scholar row (with "Symmetric"); no DOI found |
| 2014-06 | F | S. Burer, F. Kılınç-Karzan | How to convexify the intersection of a second order cone and a nonconvex quadratic | Mathematical Programming 162(1-2):393-429, 2017 | DOI 10.1007/s10107-016-1045-z; arXiv 1406.1031 |
| 2014-08 | C | G. Xu, S. Burer | A branch-and-bound algorithm for instrumental variable quantile regression | Mathematical Programming Computation 9(4):471-497, 2017 | DOI 10.1007/s12532-017-0117-2 |
| 2014-09 | H | S. Burer | A gentle, geometric introduction to copositive optimization | Mathematical Programming 151(1):89-116, 2015 | DOI 10.1007/s10107-015-0888-z |
| 2015-09 | E | G. Xu, S. Burer | Robust sensitivity analysis of the optimal value of linear programming | Optimization Methods and Software 32(6):1187-1205, 2017 | DOI 10.1080/10556788.2016.1256400; arXiv 1509.04682 |
| 2016-01 | G | B. Yang, K. Anstreicher, S. Burer | Quadratic programs with hollows | Mathematical Programming 170(2):541-553, 2018 | DOI 10.1007/s10107-017-1157-0 |
| 2016-09 | E | G. Xu, S. Burer | A copositive approach for two-stage adjustable robust optimization with uncertain right-hand sides | Computational Optimization and Applications 70(1):33-59, 2018 | DOI 10.1007/s10589-017-9974-x; arXiv 1609.07402 |
| 2016-12 † | I | S. Burer, G. Fethke | Nearly-efficient tuitions and subsidies in American public higher education | Economics of Education Review 55:182-197, 2016 | DOI 10.1016/j.econedurev.2016.09.003 |
| 2017-08 | E | G. Xu, S. Burer | A data-driven distributionally robust bound on the expected optimal value of uncertain mixed 0-1 linear programming | Computational Management Science 15(1):111-134, 2018 | DOI 10.1007/s10287-018-0298-9; arXiv 1708.07603 |
| 2018-02 | F | S. Burer, Y. Ye | Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs | Mathematical Programming 181(1):1-17, 2020 | DOI 10.1007/s10107-019-01367-2; arXiv 1802.02688 |
| 2019-01 † | I | S. Burer, V. Piccialli | Three methods for robust grading | European Journal of Operational Research 272(1):364-371, 2019 | DOI 10.1016/j.ejor.2018.06.019 |
| 2020-02 | F | K. Anstreicher, S. Burer | Quadratic optimization with switching variables: the convex hull for n = 2 | Mathematical Programming 188(2):421-441, 2021 | DOI 10.1007/s10107-021-01671-w; arXiv 2002.04681 |
| 2020-04 | F | K. Anstreicher, S. Burer, K. Park | Convex hull representations for bounded products of variables | Journal of Global Optimization 80(4):757-778, 2021 | DOI 10.1007/s10898-021-01046-7; arXiv 2004.07233 |
| 2020-09 | G | A. Eltved, S. Burer | Strengthened SDP relaxation for an extended trust region subproblem with an application to optimal power flow | Mathematical Programming 197(1):281-306, 2023 | DOI 10.1007/s10107-021-01737-9; arXiv 2009.12704 |
| 2022-05 | F | K. Gilman, S. Burer, L. Balzano | A Semidefinite Relaxation for Sums of Heterogeneous Quadratic Forms on the Stiefel Manifold | SIAM Journal on Matrix Analysis and Applications 46(2):1091-1116, 2025 | DOI 10.1137/23M1545136; arXiv 2205.13653 |
| 2022-08 | F | S. Burer, K. Park | A Strengthened SDP Relaxation for Quadratic Optimization Over the Stiefel Manifold | Journal of Optimization Theory and Applications 202(1):320-339, 2024 | DOI 10.1007/s10957-023-02168-6; arXiv 2208.03125 |
| 2023-03 | G | S. Burer | A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints | Mathematical Programming 211(1-2):157-179, 2025 | DOI 10.1007/s10107-024-02076-1; arXiv 2303.01624 |
| 2023-10 † | H | B. Yang, S. Burer | Convex Hulls in Quadratic Space | Encyclopedia of Optimization:1-6, 2024 | DOI 10.1007/978-3-030-54621-2_892-1 |
| 2024-06 | I | Y. Zhu, S. Burer | An Extended Validity Domain for Constraint Learning | INFORMS Journal on Computing, online 27 Jan 2026 | DOI 10.1287/ijoc.2024.0815; arXiv 2406.10065 |
| 2025-04 | F | S. Burer, K. Natarajan, R. Willemsen (from v3) | On the Semidefinite Representability of Continuous Quadratic Submodular Minimization With Applications to Pricing and Moment Problems | arXiv preprint, v1 2025, v3 31 Aug 2026 | arXiv 2504.03996 |
| 2025-12 | I | J. Tong, Y. Zhu, T. Serra, S. Burer | Optimization over Trained Neural Networks: Going Large with Gradient-Based Algorithms | CPAIOR 2026, Lecture Notes in Computer Science:596-613, 2026 | DOI 10.1007/978-3-032-27242-3_35; arXiv 2512.24295 |
| 2026-09 | F | S. Burer, K. Anstreicher | Applications of the Lorentz positive cone in nonconvex quadratic optimization | arXiv preprint, 2026 | arXiv 2609.32017 |

---

## 6. Full-text coverage of the publication list (deep reading, added 2026-10-10)

Added at the deep-reading synthesis (stage T3.6). Sources: `../sources/publications/works.json` and `scholar.md` (the harvest, audited 2026-10-10), `../sources/papers/INDEX.md`, the paper cards indexed in [07-paper-cards.md](07-paper-cards.md) and the synthesis [08-deep-reading-synthesis.md](08-deep-reading-synthesis.md). Sections 1–5 above were written from web research before any full text was read; they are kept unchanged, and where the full texts correct them the correction is listed below rather than made in place.

**The harvested list.** 70 Google Scholar rows plus one DBLP-only item (D001) and two homepage-only items (H001, the 2010 award note; H002, the SDPLR user's guide) give 73 records; two Scholar rows are duplicates (S064 of S002, S066 of S058), leaving **71 distinct works**: 58 journal articles, 3 book chapters, 2 conference papers, 2 preprints, 1 thesis and 5 other items (two NSF award records, the award note, the software guide, an editorial). 63 have a DOI and 15 distinct arXiv ids appear (16 arXiv fields; the 2020 article and its 2021 correction share 1802.02688). By first year: 2000–04 11 works, 2005–09 17, 2010–14 18, 2015–19 12, 2020–24 7, 2025–26 6. This list (71) is wider than the 64-work corpus of §5, which was assembled from DBLP, Crossref and the CV before the harvest; the harvest adds the NSF records, the thesis, the award note and the SDPLR guide, among others.

**Open full texts.** 67 of the 71 works have an open full text, extracted to `papers/txt/` (git-ignored): 51 from author-hosted copies (mostly the numbered archive on sburer.github.io), 15 from arXiv and 1 supplied by hand. No open text was found for 4: the 2006 CAREER and 2002 collaborative NSF award records [S068; S069], the 2001 thesis [S070] and the 2017 editorial with Atamtürk [D001].

**Read levels** (`team_status.py --coverage`, 2026-10-10): 52 works read in full (full D1–D8 cards), 15 read in part (short supplement cards), 2 at abstract level (S068, S069), 2 at metadata level (S070, D001), 0 skipped. 73 card entries cover the 71 works (S061, the 2021 correction, has three: abstract, unreadable because the file held the 2020 article, then full). 138 quotations on the cards were checked verbatim against the texts (`verify_card_quotes.py`: 137 exact, 1 equal up to spacing and symbols, 0 not found). Works carded per period follow the publication curve above.

**Versions read** (bounding every page reference): 18 works were read from a substitute version, not the published text (preprint: S012, S014, S016, S024, S051; arXiv: S019, S023, S027, S038, S039, S044, S045, S048, S049, S050, S055, S056, S057; every card citation to them carries the version word). Among them: S012 (2013 SOC-RLT paper) and S016 (MILP road to MIQCP) as preprints; S019 as arXiv v2; S048 as arXiv v3; S049 (ball constraints) as arXiv v2, not the published text and not v1, which the web-research quotes in §2 S5 and in SKILL.md come from; S058 (submodular minimization) as arXiv v3 only, so the v1 → v2 narrowing is known from web research alone [card headers].

**Corrections to §§1–5 from the full texts** (details and cards: [09-evidence-ledger.md#corrections](09-evidence-ledger.md#corrections)):
- §2 S1 and §3 (exit after the July 2004 posting): low-rank algorithm papers continue to 2007 [S026 pp. 4-7, 19; S031 pp. 3-5], SDPLR is documented as software in 2009 [H002 pp. 1-4], and the line returns in 2025 through a global certificate for nonconvex solvers [S048 arXiv pp. 5-7, 14].
- Period dating (SKILL.md and note 06): the applied and robust-optimization period runs to 2019 (robust grading [S062 pp. 5-8]).
- SKILL.md and note 03 (⚠ on review): an explicit rational counterexample point already appears in 2009 [S011 pp. 15-16]; certification in exact arithmetic is documented in 2025 [S058 pp. 43-44], not first in 2026.
- SKILL.md (Method 1 stop rule; not in §§1–5): the 2014 "Faster, but weaker" paper is motivated by interior-point SDP cost and does not cite Bao, Sahinidis and Tawarmalani [S043 pp. 2, 19].
- Contradiction 2 below (heuristics): none in the core nonconvex-QP line after 2002, but heuristics appear in coauthored applied papers of 2006, 2011 and 2026 [S005 pp. 7-8; S063 pp. 4-5, 9; S056 arXiv pp. 6-9, 15].
- Code release: SDPLR and QuadprogBB were public by 2009–2012 [H002 pp. 1-3; S008 p. 11].

**Gaps that remain**: the four works without open text; the published versions of the 18 works read from a substitute version (preprint: S012, S014, S016, S024, S051; arXiv: S019, S023, S027, S038, S039, S044, S045, S048, S049, S050, S055, S056, S057); S058 and S065 exist only on arXiv; whether arXiv 1802.02688 was updated after the 2021 correction is checked only by web research (2026-10-10, v2 unchanged, `03` 5.5), not by a card; 15 works read only in part.

---

## Contradictions (kept, not reconciled)

1. **Pay for strength or buy speed?**
   - Strength (2010): "it can be worthwhile to pay for a computationally expensive, but strong, relaxation compared to evaluating many inexpensive relaxations" (COAP note, p. 569).
   - Speed (2010 preprint of the 2009 chapter): LP relaxations "are extremely desirable for branch-and-bound algorithms" because they warm-start, and SDP-type relaxations are "bottlenecks in a branch-and-bound procedure" (preprint pp. 29–30).
   - Speed, as a dial (2013, with Kim and Kojima): "our relaxations … solve more quickly than SDP. A downside is that the calculated bounds are weaker than those gotten by SDP. The framework allows one to choose a block-diagonal structure for the mixed SOCP-SDP, which in turn allows one to control the speed and bound quality." (OO abstract 2013/04/3845)
   - Both sides (2021): "i know some people um you know love solving lp relaxations for very good reasons because the software is so well developed and so numerically reliable" [10:19] (machine transcript), while noting that SDP "has very strong relaxations but it can be harder to solve in practice" (same segment).
2. **Said versus done on heuristics.** The 2012 survey predicts "an increasing place for heuristics and approximation algorithms" (p. 104). His own 64-work corpus has no heuristic paper after the 2002 rank-two and stable-set heuristics. [stated-joint vs practice]
3. **Finiteness as motivation versus as irrelevant**, in the same paper: "An open question of theoretical interest is how to develop a finite branch-and-bound algorithm for nonconvex QP" (2008, p. 259) against "Also, in practice, concerns of an infinite tree are quite irrelevant due to the inexact nature of floating-point arithmetic" (p. 261).
4. **Pioneer of benign nonconvexity, or not?**
   - Others: "pioneering work" (ICS 2020, via Iowa Now), "popularized" (Bhojanapalli et al.), "seminal" (several S2 snippets).
   - Him: "we didn't really mean it but this was part of what people started to call benign non-convexity" (machine transcript), and "In the early 2000's, this seemed challenging to answer" (2023 slide 38, on "Why should this work at all?").
5. **Author order of the switching-variables paper**: arXiv 2002.04681 lists "Burer, Samuel; Anstreicher, Kurt"; *Math. Program.* 188(2):421–441, 2021, DOI 10.1007/s10107-021-01671-w (Crossref and DBLP) lists Anstreicher first.
6. **Dates and counts by source**:
   - the CV puts the rank-two max-cut paper in "2001" while Crossref has print January 2002;
   - Scholar dates the newsvendor paper "2006" while Crossref has online 2010 and print 2012;
   - citation counts differ by source (Scholar 1,372 versus S2 1,081 for S1), and S2's influential counts differ by endpoint (§1.3, note ²).
7. **The copositive result's scope in his own words**: "over a bounded feasible set" (OO abstract, October 2006) versus "any nonconvex quadratic program having a mix of binary and continuous variables" (final abstract), with boundedness demoted to Corollary 2.5.
8. **The survey's dates**: posted on OO on 29 Feb 2012 (Wayback copy of the entry), but "Received 9 July 2012" at the journal. No explanation found.
9. **Title versus content after the correction**: the Burer–Ye title still says "(Random and Non-Random)" (Crossref, CV), while the corrected theorem "only applies to diagonal instances". `06-trajectory.md` records the same item.
10. **Between this note and `06-trajectory.md`**:
    - 06 reports that every DBLP endpoint returned a bot-check page, so it built its timeline without DBLP. In this run, `dblp_works.py` (SPARQL endpoint) returned all 53 records for pid 96/4845.
    - 06 gives OpenAlex citation counts (e.g. copositive paper 408, survey 567). This note uses Google Scholar and Semantic Scholar counts (566 and 479; 859 and 636). The sources differ; none is reconciled here.

## Gaps

- **Origin accounts.** None in his own words for S2 (copositive), S4 (survey) or S5 (SOC-TRS) beyond the papers' motivation sentences. No interview or oral history was found with the two WebSearch calls: one returned award news, the other the MIT 2022 talk page, which has an abstract but no recording link.
- **Early versions.** The October 2006 copositive PDF and the March 2011 SOC-TRS PDF are not available, because OO overwrote them; the Wayback Machine has the abstract pages only. What Bomze's "earlier error in Proposition 2.3" was: not read.
- **Whether the 2012 survey was invited**: not found. Why the OO posting predates the journal's "received" date: not found.
- **Referee reports, rejections, desk rejections**: none public. Only publication lags are available as indirect signals.
- **Citing papers**: the papers quoted for reception were seen only as S2 citation snippets; their full texts were not read.
- **Google Scholar figures** are from a WebFetch model summary and are approximate.
- **Coverage**: arXiv coverage before 2014 is unconfirmed (wider search hit HTTP 429). OpenAlex was not used (no key). DBLP lacks 9 journal articles and all chapters.
- **Not read**: the dissertation; the picture-only "Advisor-Advisee Relationship" slides (2023 slides 31–34).
- **His own ranking of his papers**: no ranked list found. Only indirect signals: the homepage awards sentence, talk counts, and the 2015 "core" sentence.
- **The 2002–2005 SDPLR and CirCut software**: distribution history before the 2023 GitHub repository was not checked.
- **Switching-variables conjecture** (n = 2, product term ignored): not checked whether proved since 2021.

## Sources

Primary (P): his own text, slides, code or records of his own works.

1. S. Burer, curriculum vitae, 18 pp., "updated February 12, 2026". https://sburer.github.io/files/cv.pdf (primary)
2. S. Burer, homepage, footer "Last updated 2026-03-20", fetched 2026-10-10. https://sburer.github.io/ (primary)
3. Homepage repository paper archive `papers/001-maxcut.pdf … 062-submodular.pdf` (GitHub contents API listing; author-posted copies). https://github.com/sburer/sburer.github.io/tree/master/papers (primary)
4. S. Burer & R.D.C. Monteiro, *Math. Program.* 95(2):329–357, 2003. DOI 10.1007/s10107-002-0352-8; full text read (author copy 007-lowrank.pdf) (primary)
5. S. Burer & R.D.C. Monteiro, *Math. Program.* 103(3):427–444, 2005. DOI 10.1007/s10107-004-0564-1; front matter and acknowledgments (primary)
6. S. Burer, *Math. Program.* 120(2):479–495, 2009. DOI 10.1007/s10107-008-0223-z; full text read, plus the OO revision of 18 Jul 2007 (https://optimization-online.org/2006/10/1501/) (primary)
7. S. Burer & D. Vandenbussche, *Math. Program.* 113(2):259–282, 2008. DOI 10.1007/s10107-006-0080-6; full text read (primary)
8. S. Burer & D. Vandenbussche, *Comput. Optim. Appl.* 43(2):181–195, 2009. DOI 10.1007/s10589-007-9137-6; front matter (primary)
9. "COAP 2009 best paper award", *Comput. Optim. Appl.* 47(3):567–570, 2010. DOI 10.1007/s10589-010-9368-9; full text read (author copy 022-COAP_best_paper.pdf) (primary, joint)
10. S. Burer & A.N. Letchford, *Surveys in OR & MS* 17(2):97–106, 2012. DOI 10.1016/j.sorms.2012.08.001; full text read (author's personal copy 040-ncminlp.pdf) (primary)
11. S. Burer & A. Saxena, "The MILP Road to MIQCP", IMA Vol. 154, 373–405, 2012. DOI 10.1007/978-1-4614-1927-3_13; author's preprint (PDF of 23 Apr 2010), read in part (primary)
12. S. Burer & K.M. Anstreicher, *SIAM J. Optim.* 23(1):432–451, 2013. DOI 10.1137/110826862; author's preprint rev. 16 Nov 2012, full text read (primary)
13. S. Burer & B. Yang, *Math. Program.* 149(1–2):253–264, 2015. DOI 10.1007/s10107-014-0749-1; front matter and acknowledgments (primary)
14. S. Burer, "A gentle, geometric introduction to copositive optimization", *Math. Program.* 151(1):89–116, 2015. DOI 10.1007/s10107-015-0888-z; preprint rev. 17 Jan 2015, introduction (primary)
15. A. Eltved & S. Burer, *Math. Program.* 197(1):281–306, 2023. DOI 10.1007/s10107-021-01737-9; arXiv 2009.12704v2, abstract and Chen et al. passages (primary)
16. S. Burer & Y. Ye, "Correction to: Exact semidefinite formulations…", *Math. Program.* 190:845–848, 2021. DOI 10.1007/s10107-021-01684-5; text from the Springer article page (primary)
17. Skimmed for acknowledgments and implementation: OptDNN, DOI 10.1007/s12532-010-0010-8; QuadProgBB, DOI 10.1007/s12532-011-0033-9; "Copositive Programming" chapter, DOI 10.1007/978-1-4614-0769-0_8; Anstreicher & Burer 2005, DOI 10.1007/s10898-004-4312-0 (primary)
18. Optimization Online author archive "Samuel Burer", 48 entries, 2001-03-09 → 2026-09-24. https://optimization-online.org/author/samuel-burer/ (primary)
19. Wayback copies of original OO abstract pages: DB_HTML/2001/03/296 (snapshot 2001-07-07), 2006/10/1501 (2006-11-10), 2009/07/2338 (2009-10-04), 2011/03/2957 (2011-04-23), 2012/02/3378 (2013-01-16); and the current OO page 2013/04/3845. https://web.archive.org/ (primary, archived)
20. arXiv author search "Burer, Samuel" (13 entries) and abstract pages of 1406.1031, 2205.13653, 2002.04681, 2303.01624, 2609.32017, 2504.03996 v1–v3. https://arxiv.org/a/ … , https://arxiv.org/abs/2504.03996 (primary)
21. S. Burer (with R.D.C. Monteiro), "Two Decades of Low-Rank Optimization", slides, SIAM Conference on Optimization, Seattle, 2 June 2023 (86 pp., text layer). https://github.com/sburer/2023-06_SIOPT (test-of-time.pdf) (primary)
22. "Two Decades of Low-Rank Optimization", University of Iowa, March 2023; YouTube auto-caption transcript in `sources/talks/2023-two-decades-of-low-rank-optimization_youtube-wSauUgRIQDg_auto-captions.txt`. https://www.youtube.com/watch?v=wSauUgRIQDg (primary; machine transcript)
23. "Convexification for Non-Convex Mixed-Integer Quadratic Programming", IOS plenary, 31 March 2021; transcript in `sources/talks/2021-03-31-ios-plenary-convexification-nonconvex-miqp_youtube-QfZLtPz5JBY_auto-captions.txt`. https://www.youtube.com/watch?v=QfZLtPz5JBY (primary; machine transcript)
24. GitHub API metadata for `sburer/sdplr`, `sburer/QuadProgBB`, `sburer/soctrust`, `sburer/ballconstraints`, fetched 2026-10-10. https://github.com/sburer (primary)
25. "Vignettes on Copositive Optimization", MIT Operations Research Center seminar, 3 Nov 2022: his abstract ("Copositive optimization is a tool for modeling (and approximating) difficult nonconvex problems using convex optimization.") and bio. https://orc.mit.edu/?p=5697 (primary)

Secondary (S): third parties, aggregators, bibliographic services.

26. Google Scholar profile BScCde0AAAAJ, read through WebFetch (model summary), 2026-10-10. https://scholar.google.com/citations?user=BScCde0AAAAJ&hl=en&pagesize=100 (secondary)
27. DBLP via SPARQL (`scripts/dblp_works.py --pid 96/4845`), 53 records, 2026-10-10. https://dblp.org/pid/96/4845.html (secondary)
28. Semantic Scholar Graph API: author records 1691727 and 2287317032; citation lists with contexts for S1–S5; field-of-study profiles of citing papers for S2 and S4; 2026-10-10. https://api.semanticscholar.org/graph/v1/ (secondary)
29. Crossref REST API records for the 83 DOIs checked, 2026-10-10. https://api.crossref.org/works/ (secondary)
30. INFORMS Computing Society Prize page (2020 winners: Burer, Monteiro). https://www.informs.org/Recognizing-Excellence/Community-Prizes/INFORMS-Computing-Society/INFORMS-Computing-Society-Prize (secondary)
31. Iowa Now, "Burer receives top INFORMS computing society honor", 19 Aug 2020. https://now.uiowa.edu/news/2020/08/burer-receives-top-informs-computing-society-honor (secondary)
32. Georgia Tech ISyE news, "Renato Monteiro Awarded 2020 INFORMS Computing Society Prize", 14 Sep 2020 (ICS citation details; Van Hentenryck quote). https://www.isye.gatech.edu/node/6830 (secondary)
33. Tippie College of Business news, "Burer honored for long-term impact of paper", 31 Jan 2023. https://tippie.uiowa.edu/news/2023/01/burer-honored-long-term-impact-paper (secondary)
34. M. Dür & F. Rendl, "Conic optimization: A survey with special focus on copositive optimization and binary quadratic problems", *EURO J. Comput. Optim.* 9:100021, 2021. DOI 10.1016/j.ejco.2021.100021 (S2 snippet only) (secondary)
35. H. Fawzi, J. Gouveia, P.A. Parrilo, J. Saunderson & R.R. Thomas, "Lifting for Simplicity: Concise Descriptions of Convex Sets", *SIAM Rev.* 64(4):866–918, 2022. DOI 10.1137/20M1324417 (snippet) (secondary)
36. R. Badenbroek & E. de Klerk, "An Analytic Center Cutting Plane Method to Determine Complete Positivity of a Matrix", *INFORMS J. Comput.* 34(2):1115–1125, 2022. DOI 10.1287/ijoc.2021.1108 (snippet) (secondary)
37. I. Bomze & M. Gabl, "Interplay of non-convex quadratically constrained problems with adjustable robust optimization", *Math. Methods Oper. Res.* 93(1):115–151, 2021. DOI 10.1007/s00186-020-00726-6 (snippet) (secondary)
38. M.A. Davenport & J. Romberg, "An Overview of Low-Rank Matrix Recovery From Incomplete Observations", *IEEE JSTSP* 10(4):608–622, 2016. DOI 10.1109/JSTSP.2016.2539100 (snippet) (secondary)
39. A.S. Bandeira, "Inference on graphs via semidefinite programming", *PNAS* 113(16):4238–4239, 2016. DOI 10.1073/pnas.1603405113 (snippet) (secondary)
40. L. Grippo, L. Palagi & V. Piccialli, "An unconstrained minimization method for solving low-rank SDP relaxations of the maxcut problem", *Math. Program.* 126(1):119–146, 2011. DOI 10.1007/s10107-009-0275-8 (snippet) (secondary)
41. A. Lemon, A.M.-C. So & Y. Ye, "Low-Rank Semidefinite Programming: Theory and Applications", *Found. Trends Optim.* 2(1–2):1–156, 2016. DOI 10.1561/2400000009 (snippet) (secondary)
42. S. Bhojanapalli, A. Kyrillidis & S. Sanghavi, "Dropping Convexity for Faster Semi-definite Optimization", arXiv 1509.03917 (snippet) (secondary)
43. N. Boumal, V. Voroninski & A.S. Bandeira, "The non-convex Burer-Monteiro approach works on smooth semidefinite programs", arXiv 1606.04970 (NIPS 2016); D. Cifuentes & A. Moitra, "Polynomial time guarantees for the Burer-Monteiro method", arXiv 1912.01745 (abstract pages only) (secondary)
44. P. Bonami, O. Günlük & J. Linderoth, "Globally solving nonconvex quadratic programming problems with box constraints via integer programming methods", *Math. Program. Comput.* 10(3):333–382, 2018. DOI 10.1007/s12532-018-0133-x (snippet) (secondary)
45. K.M. Anstreicher, "Solving Two-Trust-Region Subproblems Using Semidefinite Optimization with Eigenvector Branching", *JOTA* 202(1):303–319, 2024 (online 2022). DOI 10.1007/s10957-022-02064-5 (snippet) (secondary)
46. F. Kılınç-Karzan & S. Sun, "On the strength of Burer's lifted convex relaxation to quadratic programming with ball constraints", arXiv 2407.14992 (abstract page) (secondary)
47. Crossref records for his own works: the 64-work corpus with DOIs or arXiv ids is listed in §5. https://api.crossref.org/works/ (secondary bibliographic data for primary works)
48. Earlier works his papers name as starting points (Crossref-checked; not read): Homer & Peinado 1997, DOI 10.1006/jpdc.1997.1381; Barvinok 1995, DOI 10.1007/BF02574037; Pataki 1998, DOI 10.1287/moor.23.2.339; Lovász & Schrijver 1991, DOI 10.1137/0801013; Vandenbussche & Nemhauser 2005, DOIs 10.1007/s10107-004-0549-0 and 10.1007/s10107-004-0550-7; Ye & Zhang 2003, DOI 10.1137/S105262340139001X; Sturm & Zhang 2003, DOI 10.1287/moor.28.2.246.14485; Martínez 1994, DOI 10.1137/0804009; Chen, Atamtürk & Oren 2017, DOI 10.1007/s10107-016-1095-2 (secondary)
49. WebSearch result lists for two queries (Burer interview/origin; the 2007 and 2022 copositive talks), 2026-10-10. Used only to locate items 25 and 32. (secondary)
