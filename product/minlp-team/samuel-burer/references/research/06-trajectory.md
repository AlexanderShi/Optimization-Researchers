# 06 · Research trajectory: timeline, lineage, turns and their triggers

> **Researcher**: Samuel A. (Sam) Burer. Google Scholar BScCde0AAAAJ; DBLP pid 96/4845; ORCID 0000-0001-5886-458X; Mathematics Genealogy Project (MGP) id 114747; OpenAlex A5002663715.
> **Dimension**: research agent 06 of 06, research trajectory (nuwa research-craft Phase 1).
> **Research date**: 2026-10-10.
> **Sources consulted**: 29, listed under "Sources" (14 primary, 15 secondary). Identifiers checked with a tool in this run:
> - 62 DOIs through Crossref (60 by direct lookup, 2 by bibliographic search). The file cites 59 of them, plus one DOI seen only in OpenAlex, which is marked where it appears;
> - 15 arXiv ids through the arXiv API (6 of them also through their abstract pages and version histories);
> - 48 Optimization Online entries through his author archive;
> - 2 NSF awards through the NSF API.
>
> WebSearch calls used: 2 of 2.
> **Local corpus**: `references/sources/papers`, `essays`, `software` and `publications` held only `.gitkeep` files, so there was no user-supplied material and nothing below is marked "from user-supplied material". During this run a sibling agent saved three YouTube auto-caption transcripts under `sources/talks/`. I read them and quote them only with the machine-transcription caveat. I did not open `private/`. I saved no transcript myself, because the caption endpoint returned an empty file to my request.
> **Method**:
> - His CV (18 pp., "updated February 12, 2026") and homepage (footer "Last updated 2026-03-20").
> - The git history of the homepage repository: every version of `index.html` since 2015, the 2015–2016 blog posts, the numbered paper archive `papers/001…062` and the new `aicourse/` pages.
> - Wayback snapshots of his first homepage `dollar.biz.uiowa.edu/~sburer/` (2005, 2007, 2008, a 2010 wiki), with a 2003 résumé and a January 2014 CV taken from those snapshots.
> - The GitHub API: 20 public repositories, with commit logs and co-author trailers.
> - Slides of his two talks on 2 June 2023 (SIAM OP23), and the YouTube feed plus the description of the plenary video.
> - arXiv (API, abstract pages, full texts of 2504.03996 v1 and v3 and of 2609.32017v1, front matter of three more), the Optimization Online author archive and 9 abstract pages, the Springer correction note of 2021, Crossref, NSF award records, MGP, OpenAlex and ORCID.
> - INFORMS award pages, and University of Iowa, Tippie and Georgia Tech news items.
> - A WebFetch read of his Google Scholar profile.
>
> DBLP could not be read (see §0).
> **Tags**: [stated] = he said or wrote it ([stated-joint] = co-authored text) · [practice] = what the record shows he did (papers, code, CV entries, dates) · [observed] = what others wrote or recorded · [inferred] = my reading, which no source states. Each item also carries **P** (primary) or **S** (secondary).
> **Quoting**: quotations are verbatim, including typos in the source ("millenium", "pointed about", "techiniques", "optimizaton"). Quotations from the auto-caption transcript are machine transcriptions and are marked "(machine transcript)". I removed only line breaks and Markdown bold markers.
> **Relation to 01–05**: when I wrote this file, `references/research/` held only `.gitkeep`, so nothing here depends on 01–05. I checked every identifier and quote below myself in this run.

---

## 0. Identity hygiene for the timeline

- **DBLP was unreadable.** Every DBLP endpoint (`dblp.org`, `dblp.uni-trier.de`, `dblp.dagstuhl.de`, and the search API) returned an Anubis "Making sure you're not a bot!" page to curl. I built the publication timeline from the CV, OpenAlex (88 works), Crossref, arXiv and Optimization Online instead. [practice, P]
- **The CV orders papers by manuscript, not by print year.** Its journal list is "listed in reverse chronological order by appearance of manuscript". The homepage archive `papers/001-maxcut.pdf … 062-submodular.pdf` uses the same order, and two files share number 022 (`022-qpbb2.pdf`, `022-COAP_best_paper.pdf`). Below, "worked on" dates come from the first Optimization Online or arXiv posting, and "appeared" dates from Crossref. [practice, P]
- **OpenAlex's Stanford tag is not a move.** OpenAlex attaches Stanford University, with the single year 2018, to his profile. The only 2018 candidate, Burer & Ye, arXiv 1802.02688v1, lists him only at "Department of Management Sciences, University of Iowa", and Stanford is Ye's affiliation. The CV lists no Stanford visit. [practice, P; OpenAlex S]
- **Optimization Online metadata misstates one authorship.** It lists the 2001 low-rank preprint (2001/03/296) under "Samuel Burer" alone. Crossref gives Burer & Monteiro. By the CV he has 7 sole-authored items, published 2003, 2009, 2010, 2012 (two), 2015 and 2025. [practice, P]
- **ORCID** holds 7 works and no employment or education entries, so it is not usable for the timeline. [practice, S]
- **The YouTube "Two Decades of Low-Rank Optimization" video (uploaded 2023-09-09, 2,648 s) is the March 2023 University of Iowa rehearsal of the talk**, not the SIAM lecture. The sibling transcript's header says so, and so does the speaker: "I'll be giving this talk a little bit a couple of months from now at a conference" (machine transcript). The CV lists the Iowa talk as P21. The SIAM OP23 prize lecture of 2 June 2023 is represented here by its slide PDF (created 1 June 2023). [practice, P]

---

## 1. Dated timeline

| When | Event | Evidence | Tag |
|---|---|---|---|
| Jun 1997 | B.S. Mathematics, University of Georgia ("First Honor Graduate, Summa Cum Laude, With Highest Honors"). Strahan Mathematics Award 1996 | CV 2026 | [stated, P] |
| Jul–Oct 1997 | "Research Intern, Wolfram Research (makers of the software Mathematica)". Absent from the 2026 CV | 2003 résumé | [stated, P] |
| 1997–2001 | PhD, Algorithms, Combinatorics, and Optimization (ACO), Georgia Tech, on a Presidential Fellowship (1997–2001). Advisor R.D.C. Monteiro. Also TA in Mathematics (10/97–6/98), Research Assistant in ISyE (6/98–8/01) and Instructor/TA in ISyE (8/99–12/00) | CV; 2003 résumé; MGP 114747; GT repository record (issued 2001-08; departments "Mathematics" and "Algorithms, Combinatorics, and Optimization") | [stated, P]; [observed, S] |
| May 1999 | First listed talk (SIAM OP, Atlanta): the long-step framework, later *OMS* 18(1):1–38, 2003 (DOI 10.1080/1055678031000111227) | CV P120; Crossref | [practice, P] |
| Dec 1999 | Rice report with Monteiro and Yin Zhang on interior-point algorithms for SDP based on a nonlinear formulation, later *COAP* 22(1):49–79, 2002 (DOI 10.1023/A:1014834318702) | OpenAlex (Rice repository); Crossref | [practice, P/S] |
| 22 May 2000 | First e-mail exchange with Monteiro about the low-rank factorization. He reported the implementation "about 11 pm" and, a day later, a version "roughly 30 times faster" | March 2023 talk (machine transcript) | [stated, P] |
| Aug and Nov 2000 | Low-rank algorithm presented at ISMP (Atlanta) and at the DIMACS Seventh Implementation Challenge (Rutgers) | CV P115, P114 | [practice, P] |
| 2001–2003 | Low-rank preprint on Optimization Online, 9 Mar 2001 (2001/03/296), published as *Math. Program.* 95(2):329–357, 2003 (DOI 10.1007/s10107-002-0352-8). Companion papers: projected-gradient max-cut, *OMS* 15(3–4):175–200, 2001 (DOI 10.1080/10556780108805818); rank-two heuristics, *SIOPT* 12(2):503–521 (DOI 10.1137/S1052623400382467); stable set, *Math. Program.* 94(1):137–166, 2002 (DOI 10.1007/s10107-002-0356-4); SDP via NLP, *Math. Program.* 93(1):97–122, 2002 (DOI 10.1007/s101070100279); log-barrier computational study, *Math. Program.* 95(2):359–379, 2003 (DOI 10.1007/s10107-002-0353-7) | Optimization Online; Crossref | [practice, P] |
| Jan–Apr 2001 | Invited seminar series "The Maximum Cut and Maximum Stable Set Problems: New Approaches via Semidefinite Programming" at Stony Brook (Jan), Iowa (Feb, six months before he joined) and Kentucky (Apr), plus a stable-set talk at Rice (Mar). Listed in the 2003 résumé, dropped from the 2026 CV. That these were job talks is my reading | 2003 résumé | [practice, P]; "job talks" [inferred] |
| Aug 2001 | PhD awarded (thesis "New Algorithmic Approaches for Semidefinite Programming with Applications to Combinatorial Optimization"). Assistant Professor, Department of Management Sciences, University of Iowa (Tippie College of Business) | CV; GT repository | [stated, P] |
| 2002 | INFORMS Optimization Society Young Researchers Prize, winning material "Semidefinite Programming in the Space of Partial Positive Semidefinite Matrices" (*SIOPT* 14(1):139–172, 2003, DOI 10.1137/S105262340240851X). Old Gold Fellowships 2002–03 | INFORMS recipient page; CV; Crossref | [observed, S]; [stated, P] |
| 15 Jun 2002 – 31 May 2006 | NSF award 0203426, "Collaborative Research: Theory and Implementation of Semidefinite Programming and Its Application to Combinatorial Optimization", $255,818. The CV says "2000-05" (see Contradictions) | NSF API; CV | [practice, P] |
| May 2003 | First copositive paper: "D.C. Versus Copositive Bounds for Standard QP", with Anstreicher (Optimization Online 2003/05/660), published *JOGO* 33(2):299–312, 2005 (DOI 10.1007/s10898-004-4312-0) | Optimization Online; Crossref | [practice, P] |
| Sep 2003 | Last low-rank *theory* paper: "Local Minima and Convergence in Low-Rank Semidefinite Programming" (2003/09/740), published *Math. Program.* 103(3):427–444, 2005 (DOI 10.1007/s10107-004-0564-1) | Optimization Online; Crossref | [practice, P] |
| Sep 2003 | Résumé research interests: "Semidefinite programming, including its application to combinatorial optimization" and "Interior-point methods, nonlinear programming". Lists "Exploiting Structure in Mixed Conic Programming," with M.F. Anjos, as "in progress" | 2003 résumé (PDF created 2003-09-30) | [stated, P] |
| 2004 | ICCOPT-I Young Researcher honorable mention. Hesse Faculty Fellow (2004–12). Joins the Applied Mathematical and Computational Sciences (AMCS) faculty (2004–) | CV | [stated, P] |
| Jun–Jul 2004 | Lift-and-project for binary IPs with Vandenbussche (2004/06/890), published *SIOPT* 16(3):726–750, 2006 (DOI 10.1137/040609574). Last low-rank *algorithm* paper, with student Choi (2004/07/904), published *OMS* 21(3):493–512, 2006 (DOI 10.1080/10556780500286582) | Optimization Online; Crossref | [practice, P] |
| Jan–Jun 2005 | Four directions at once: (1) inventory games with Dror (2005/01/1042); (2) maximum-entropy sampling with J. Lee (2005/03/1079), *Math. Program.* 109(2–3):263–281, 2007 (DOI 10.1007/s10107-006-0024-1); (3) SDP-based branch-and-bound for nonconvex QP with Vandenbussche (2005/06/1167), *Math. Program.* 113(2):259–282, 2008 (DOI 10.1007/s10107-006-0080-6); (4) ensemble pruning via SDP with Yi Zhang and W.N. Street, *JMLR* 7:1315–1338, 2006, and ICDM'05 (DOI 10.1109/ICDM.2005.131) | Optimization Online; Crossref; CV | [practice, P] |
| 1 Jun 2006 – 31 May 2012 | NSF CAREER 0545514, "Computation, Theory, and Applications for Nonconvex Quadratic and Conic Optimization", $400,000 | NSF API; CV | [practice, P] |
| Aug–Oct 2006 | Free variables in conic IPMs with Anjos (2006/08/1456), *SIOPT* 18(4):1310–1325 (DOI 10.1137/06066847X). **Copositive representation of mixed binary QPs, sole author** (2006/10/1501), *Math. Program.* 120(2):479–495, 2009 (DOI 10.1007/s10107-008-0223-z) | Optimization Online; Crossref | [practice, P] |
| Jan–May 2007 | Visiting Assistant Professor, Tepper School, Carnegie Mellon. Taught "Seminar on Semidefinite Programming (Carnegie Mellon 47-837)". Talk series "Representing NP-Hard Problems as Convex Programs" (Pittsburgh, CMU, ICCOPT-II, Northwestern, 2007) | CV | [stated, P] |
| 2006–2007 | First doctoral graduates: Yi Zhang (2006; MGP gives Street as advisor 1 and Burer as advisor 2) and Changhui Choi (Spring 2007, CV) | MGP; CV | [observed, S]; [stated, P] |
| Jul 2007 | Associate Professor | CV | [stated, P] |
| 2007–2009 | Seven nonconvex-QP and conic papers: (1) convex hulls of low-dimensional quadratic forms with Anstreicher, *Math. Program.* 124:33–43, 2010 (DOI 10.1007/s10107-010-0355-9); (2) box-QP KKT relaxations with Chen, *COAP* 48(3):653–673, 2011 (DOI 10.1007/s10589-009-9273-2); (3) p-cone procedure for 0-1 IPs with Chen, *OMS* 24(4–5):523–548, 2009 (DOI 10.1080/10556780903057341); (4) 5×5 doubly nonnegative vs completely positive matrices with Anstreicher and Dür, *LAA* 431(9):1539–1552, 2009 (DOI 10.1016/j.laa.2009.05.021); (5) box QP with Letchford, *SIOPT* 20(2):1073–1089, 2009 (DOI 10.1137/080729529); (6) OptDNN, *MPC* 2(1):1–19, 2010 (DOI 10.1007/s12532-010-0010-8); (7) hypergraph bisection with Choi, *Optimization* 60(3):413–427, 2011 (DOI 10.1080/02331930903233744) | Optimization Online; Crossref | [practice, P] |
| 2009 | COAP Best Paper Award for the finite branch-and-bound on box QP, *COAP* 43(2):181–195 (DOI 10.1007/s10589-007-9137-6). Visiting Associate Professor, Sapienza Università di Roma (Apr–May 2009), with a "Short Course on Semidefinite Programming" | CV | [stated, P] |
| Jul 2009 | **First explicit MIQCP paper**: "Old Wine in a New Bottle: The MILP Road to MIQCP", with Saxena (2009/07/2338), published as "The MILP Road to MIQCP", IMA Vol. 154:373–405, 2012 (DOI 10.1007/978-1-4614-1927-3_13) | Optimization Online; Crossref | [practice, P] |
| 2010–2012 | Peak cluster, 9 preprints: (1) cones of quadratic forms with Dong, *Math. Program.* 137:343–370, 2013 (DOI 10.1007/s10107-011-0495-6); (2) QuadProgBB with Chen, *MPC* 4(1):33–52, 2012 (DOI 10.1007/s12532-011-0033-9); (3) SOC constraints for extended trust-region subproblems with Anstreicher, *SIOPT* 23(1):432–451, 2013 (DOI 10.1137/110826862); (4) generalized copositive QCQP with Dong, *ORL* 40(3):203–206, 2012 (DOI 10.1016/j.orl.2012.02.001); (5) unbounded convex sets for MIQP with Letchford, *Math. Program.* 143:231–256, 2014 (DOI 10.1007/s10107-012-0609-9); (6) college football rankings, *JQAS* 8(2), 2012 (DOI 10.1515/1559-0410.1405); (7) first-order smoothing for LP with Chen, *SIOPT* 24(2):598–620, 2014 (DOI 10.1137/110854400); (8) **non-convex MINLP survey with Letchford**, *SORMS* 17(2):97–106, 2012 (DOI 10.1016/j.sorms.2012.08.001); (9) "Copositive Programming" handbook chapter, 2012 (DOI 10.1007/978-1-4614-0769-0_8) | Optimization Online; Crossref | [practice, P] |
| 2010–2011 | Co-Editor of *Optima* (2010–18). Students Jieqiu Chen (2010) and Hongbo Dong (2011, co-advised with Anstreicher) graduate | CV; MGP | [stated, P]; [observed, S] |
| Jul 2012 | Professor; Henry B. Tippie Research Fellow (2012–16). The CAREER award ends in May 2012, and **the CV lists no external research grant after it** | CV; NSF API (only two awards with him as PI) | [practice, P] |
| Jan 2014 | CV research interests now open with "Analytics, operations research, management sciences". The TSP paper with N. Cho and A.M. Campbell is still "under review", dated "January 2010" | 2014 CV | [stated, P] |
| 2013–2016 | Teaching turn: (1) YouTube teaching videos (Excel PivotTables, Analytic Solver Platform, R/RStudio, RMarkdown; Sep 2013 – Feb 2016); (2) new courses "Optimization and Simulation Modeling" (Fall 2013) and "Data Programming in R" (Spring 2015); (3) Coursera "R Programming" Statement of Accomplishment with Distinction (2015); (4) Chair, Analytics Master's Proposal Committee (2013–15); (5) Faculty Director, Part-Time Business Analytics Graduate Program (2014–2019) | YouTube feed; CV | [practice, P] |
| 2013–2016 | Research in the same years: (1) TRS with non-intersecting linear constraints with B. Yang, *Math. Program.* 149:253–264, 2015 (DOI 10.1007/s10107-014-0749-1); (2) "Faster, but weaker" with Kim and Kojima, *COAP* 59:27–45, 2014 (DOI 10.1007/s10589-013-9618-8); (3) two-trust-region subproblem with Yang, *SIOPT* 26(1):661–680, 2016 (DOI 10.1137/130945880); (4) convexifying SOC ∩ nonconvex quadratic with Kılınç-Karzan (arXiv 1406.1031), *Math. Program.* 162:393–429, 2017 (DOI 10.1007/s10107-016-1045-z); (5) IV quantile regression branch-and-bound with Xu, *MPC* 9(4):471–497, 2017 (DOI 10.1007/s12532-017-0117-2); (6) "A gentle, geometric introduction to copositive optimization", *Math. Program.* 151(1):89–116, 2015 (DOI 10.1007/s10107-015-0888-z), given as an ISMP 2015 semi-plenary; (7) robust sensitivity of LP with Xu (arXiv 1509.04682), *OMS* 32(6):1187–1205, 2017 (DOI 10.1080/10556788.2016.1256400) | Optimization Online; arXiv; Crossref; CV | [practice, P] |
| May 2015 – May 2016 | Seven blog posts (R, ggplot2 and leaflet; MATLAB with YALMIP; Julia, JuMP and Cbc), syndicated to R-bloggers. The blog then stops | homepage repository `_posts` | [stated, P] |
| 2016 | George Daly Professor (2016–2021). Third place, INFORMS Syngenta Crop Challenge in Analytics. Papers: tuitions with Fethke, *Econ. Educ. Rev.* 55:182–197 (DOI 10.1016/j.econedurev.2016.09.003); quadratic programs with hollows with Yang and Anstreicher, *Math. Program.* 170:541–553, 2018 (DOI 10.1007/s10107-017-1157-0); copositive two-stage adjustable robust optimization (ARO) with Xu (arXiv 1609.07402), *COAP* 70:33–59, 2018 (DOI 10.1007/s10589-017-9974-x) | CV; INFORMS recipient page; Crossref | [practice, P]; [observed, S] |
| 2017–2019 | Data-driven DRO bound with Xu (arXiv 1708.07603), *CMS* 15:111–134, 2018 (DOI 10.1007/s10287-018-0298-9). Burer & Ye (arXiv 1802.02688), *Math. Program.* 181:1–17, 2020 (DOI 10.1007/s10107-019-01367-2). Robust grading with Piccialli, *EJOR* 272(1):364–371, 2019 (DOI 10.1016/j.ejor.2018.06.019). Faculty Director, Full-Time BA program (2018–2020) | arXiv; Crossref; CV | [practice, P] |
| Apr 2019 | "Department name was changed from Management Sciences to Business Analytics in April 2019." | CV footnote | [stated, P] |
| May–Jul 2019 | IPCO tutorial "An Introduction to Semidefinite Programming for Combinatorial Optimization" (materials on GitHub). Refereed tutorial "Python or R or Both" at PEARC 2019. **No Optimization Online posting in 2019** | CV; GitHub; Optimization Online | [practice, P] |
| 2020 | 2020 INFORMS Computing Society (ICS) Prize with Monteiro: "for his pioneering work on low-rank semi-definite programming" (Iowa Now). Area Editor, *Operations Research* (2020–). Vice Chair, SIAG/OPT (2020–23). Three preprints: switching variables with Anstreicher (arXiv 2002.04681), *Math. Program.* 188(2):421–441, 2021 (DOI 10.1007/s10107-021-01671-w); bounded products with Anstreicher and Park (arXiv 2004.07233), *JOGO* 80(4):757–778, 2021 (DOI 10.1007/s10898-021-01046-7); extended trust-region subproblem with an optimal-power-flow application, with Eltved (arXiv 2009.12704), *Math. Program.* 197:281–306, 2023 (DOI 10.1007/s10107-021-01737-9) | INFORMS ICS page; Iowa Now 2020-08-19; CV; arXiv; Crossref | [observed, S]; [practice, P] |
| Jan–Jul 2021 | Talk retitled to "…Nonconvex Diagonal QCQPs" (Peking University, Jan 2021). Correction of Burer–Ye Theorem 3 published online 8 Jul 2021, *Math. Program.* 190:845–848 (DOI 10.1007/s10107-021-01684-5). Mar 2021: INFORMS Optimization Society plenary "Convexification for Non-Convex Mixed-Integer Quadratic Programming", repeated 2022 at SMU, IIM Bangalore, SUTD, Florida and Lehigh | CV P26–P32; Crossref; Springer | [practice, P] |
| Oct 2021 | Tippie Rollins Professor | CV; homepage commit 2021-10-04 | [stated, P] |
| 2022 | Associate Editor, *Mathematical Programming*. MOS Treasurer-Elect. President and Provost Award for Teaching Excellence. JOGO Best Paper honorable mention. Stiefel-manifold preprints with Gilman and Balzano (arXiv 2205.13653) and with Park (arXiv 2208.03125) | CV; arXiv | [stated, P]; [practice, P] |
| 2023 | **Inaugural SIAM SIAG/OPT Test of Time Award with Monteiro** for the 2003 paper (Tippie news 31 Jan 2023; GT ARC news 18 Feb 2023). Also: (1) March Iowa talk and the 2 June SIAM OP23 lecture "Two Decades of Low-Rank Optimization"; (2) the same day, the "Kurt-Fest!" talk on ball constraints ("Happy Retirement, Kurt!"); (3) sole-author preprint arXiv 2303.01624, published *Math. Program.* 211:157–179, 2025 (DOI 10.1007/s10107-024-02076-1); (4) MOS Treasurer (2023–25) and Director of Graduate Studies, BA doctoral program (2023–25); (5) Park graduates | Tippie; GT ARC; slides; arXiv; Crossref; CV; MGP | [observed, S]; [practice, P] |
| Oct–Dec 2023 | SDPLR 1.03-beta published on GitHub (5–6 Oct 2023). An outside contributor (Benoît Legat) adds patches (12 Dec 2023) | GitHub commit log | [practice, P] |
| 2024 | Constraint-learning preprint with PhD student Yilin Zhu (arXiv 2406.10065, 14 Jun 2024). Encyclopedia chapter "Convex Hulls in Quadratic Space" with B. Yang (DOI 10.1007/978-3-030-54621-2_892-1, online 31 Oct 2023). Tippie Collegiate Research Impact Award | arXiv; Crossref; CV | [practice, P] |
| Apr 2025 | Submodular preprint v1 with Natarajan (arXiv 2504.03996v1) claims polynomial-time SDP solvability (see §6) | arXiv | [practice, P] |
| 2025 | Chair / Departmental Executive Officer (DEO), Business Analytics (2025–). Search Committee Chair for a visiting position (INFORMS Connect, posted 24 May 2025). Chair, Balas Prize committee. Constraint-learning talks (National Taiwan University, UC Irvine, Tennessee, HEC Montréal, HK PolyU) | CV; INFORMS Connect; Tippie faculty page ("Department Executive Officer, Tippie-Rollins Professor in Business Analytics") | [stated, P]; [observed, S] |
| 10 Oct 2025 → 10 Oct 2026 | See §7 | — | — |

---

## 2. Periods and their resource context

| Period | Seniority and setting | Funding and tools | Team | Output pattern |
|---|---|---|---|---|
| 1997–2001 | PhD student, Georgia Tech ACO | Presidential Fellowship. C code with a MATLAB interface (SDPLR); DIMACS challenge benchmarks. Era: "At the turn of the millenium, researchers were solving bigger SDPs more efficiently, often using first-order methods" (2023 slides) [stated, P] | Monteiro (advisor) on all 8 thesis-era papers; Yin Zhang (Rice) on 5 of them | All papers co-authored with Monteiro. Computation-driven SDP algorithms and heuristics |
| 2001–2007 | Assistant professor in a **business school** department (Management Sciences, Tippie) | NSF collaborative grant (2002–06), Old Gold fellowships, CAREER from 2006 | Iowa colleagues Anstreicher and Street; co-authors Jones and Lowe (affiliations not checked); external partners (Vandenbussche at UIUC, J. Lee, Anjos, Dror); first students (Yi Zhang, Choi) | Breadth: binary IP relaxations, nonconvex QP, maximum-entropy sampling, supply chain, ML ensembles. 11 Optimization Online postings in 2001–05 |
| 2007–2012 | Associate professor | CAREER ($400k). Visits to CMU (2007) and Sapienza (2009). Software in MATLAB with C MEX subroutines: QuadProgBB (version "20120229" in the CV), which bundles OptDNN (`opt_dnn.m`) | Students Chen and Dong; collaborators Anstreicher, Letchford, Saxena, Dür, Kim and Kojima | Densest period: copositive/CP theory and computation, MIQCP/MINLP surveys. 10 postings in 2006–10 and 14 in 2011–15. Rising editorial load: six associate editorships active in 2011 (*MPC*, *ORL*, *SORMS*, *SIOPT*, *OR*, *MOR*), and *Optima* co-editor from 2010 |
| 2012–2020 | Full professor in a department pivoting to analytics | **No external grant listed.** MATLAB research code (soctrust, ttrs, grades repositories), YALMIP, R, Julia/JuMP for the crop challenge | Students Yang (2015) and Xu (2017); Park in progress | TRS variants, copositive methods for robust optimization, applied analytics papers, teaching materials. Postings drop to 7 in 2016–20, with none in 2019 |
| 2020–2026 | Chaired professor, then DGS (2023–25) and DEO (2025–). Area Editor, *OR*; Associate Editor, *Math. Program.*; SIAG/OPT vice chair; MOS treasurer | Python code with Gurobi, MOSEK and cvxpy/Clarabel. GitHub Copilot instructions (Dec 2025), then Claude Sonnet 4.6 (Mar 2026) and Claude Opus 5 (Jul–Sep 2026) as commit co-authors. "Claude (Anthropic) and Codex (OpenAI)" acknowledged in the Sep 2026 preprint | Anstreicher (retired 2023, still co-authoring); students Park and Zhu; visitor Eltved; Natarajan and Willemsen (SUTD); departmental colleague Serra; Tong (Northwestern) | 6 postings in 2021–26 (none in 2021). Mix of QCQP relaxation theory, ML-embedded optimization and submodular/DRO work |

---

## 3. Lineage

### 3.1 Upstream

- **George B. Dantzig → Ilan Adler** (Stanford 1971, "Abstract Polytopes") **→ Renato D.C. Monteiro** (UC Berkeley 1988) **→ Samuel Burer** (Georgia Tech 2001). MGP records 132760, 19778 and 114747. [observed, S]
- Monteiro's other MGP students are Zhaosong Lu (2005), Guanghui Lan (2009), Camilo Ortiz (2014), Weiwei Kong (2021) and Jiaming Liang (2022). Burer later sat on Liang's PhD committee (GT, 2022) and on Arnesh Sujanani's (GT, 2024). Sujanani's advisor was not checked. [practice, P; MGP S]
- On how the advisor worked with him [stated, P] (machine transcript): "Montero was very nice to me I would go by all the time and would talk to me as much as I wanted to talk". The 2023 slides include a section titled "The Advisor-Advisee Relationship" (picture-only slides; contents not readable as text).
- **Yin Zhang** (Rice) co-authored five thesis-era papers. [practice, P]
- The host of the March 2023 Iowa talk says they "went to grad school together so I've known him for 26 years" (machine transcript), and Burer refers to "my thesis with Professor Renato Montero that Anne mentioned". [observed, P] I take the host to be his departmental colleague Ann M. Campbell (co-author of the 2014 TSP paper and co-sponsor of postdoc N. Cho, 2009–10). [inferred; not verified]

### 3.2 Downstream (CV advisee table, read in table mode; cross-checked with MGP)

| Student | Year | Program, co-advisor | Placement (CV: initial → current) | Thread (from co-authored papers) | MGP |
|---|---|---|---|---|---|
| Yi Zhang | 2006 | Management Sciences | — | Ensemble pruning via SDP (*JMLR* 2006, ICDM'05) | Advisor 1 W.N. Street, advisor 2 Burer. The CV lists Yi Zhang under "Ph.D. Committee" only |
| Changhui Choi | 2007 | Management Sciences | Univ. of Colorado Denver → Korea Insurance Research Institute | Low-rank SDP enhancements (2006); hypergraph bisection (2011) | not in MGP |
| Jieqiu Chen | 2010 | Management Sciences | Argonne → Microsoft | Box-QP KKT relaxations, p-cone, QuadProgBB, first-order smoothing | Advisor 1 Burer |
| Hongbo Dong | 2011 | AMCS, with K. Anstreicher | Univ. of Wisconsin–Madison → Meta | Copositive separation and relaxation (thesis "Copositive Programming: Separation and Relaxations") | Advisors Anstreicher and Burer. One student (Wei Li, Washington State 2018) |
| Boshi Yang | 2015 | AMCS | Carnegie Mellon → Clemson | TRS variants (thesis "A conic optimization approach to variants of the trust region subproblem") | Advisor 1 Burer |
| Nathaniel Richmond | 2016 | AMCS | — | "On Stochastic Network Design" | Advisor 1 P. Krokhmal, advisor 2 Burer. The CV lists Richmond under "Ph.D. Committee" only |
| Guanglin Xu | 2017 | Management Sciences | Univ. of Minnesota → UNC Charlotte | Copositive methods for robust/DRO problems; IV quantile regression | Advisor 1 Burer |
| Kyungchan Park | 2023 | Business Analytics, with K. Anstreicher | — | Bounded products; Stiefel SDP (thesis "Advances in convex relaxations for quadratic optimization") | Advisors Anstreicher and Burer |
| Yilin Zhu | Spring 2026 (expected) | Mathematics | — | Constraint learning (*IJOC* 2026); optimization over trained NNs (CPAIOR 2026) | not in MGP |

- Sponsored postdoc: Nayoung Cho (Spring 2009 – Summer 2010, with A. Campbell). Sponsored short-term visitors: Anders Eltved (DTU), Nicolò Gusmeroli (Klagenfurt), Peter J.C. Dickinson and Mirjam Dür (Groningen). The CV gives no dates for the visitors. [stated, P]
- MGP totals: 7 students and 8 descendants. [observed, S]
- Placement pattern [inferred]: early graduates started in academia or national labs. Three of the four with a "current" entry from before 2016 (Chen, Dong, Choi) are now in industry or an applied institute.

---

## 4. Turns and what triggered them

| # | Turn (when) | What changed | Trigger, with evidence | Tag |
|---|---|---|---|---|
| T1 | Into large-scale SDP algorithms (1998–2001) | Interior-point methods → first-order NLP reformulations → low-rank factorization | (a) The research area of his advisor's group and the period's push to solve "bigger SDPs … often using first-order methods" (2023 slides). (b) A chain of ideas, as he lists it: "Peinado and Homer (1997) proposed to optimize directly with U (instead of X)"; "B and Monteiro (2001) saved time and space by taking U lower triangular"; then the rank bound "(Shapiro 1982, Barvinok 1995, Pataki 1998)". (c) The decision rule: "Can't hurt to try" (slides), and "we thought you know it couldn't hurt to try" (machine transcript). (d) A speed motive: "so we were very motivated by just sort of having a fast code" (machine transcript) | [stated, P]; that the topic came from the advisor's group is [inferred] |
| T2 | From SDP solvers to relaxations of hard discrete and nonconvex problems (2003–2006) | SDP as a modelling and bounding tool for nonconvex QP and binary IPs | (a) Arrival at Iowa, where colleague Anstreicher co-wrote his first copositive paper (May 2003). (b) A collaborator's prior method: the 2005 B&B paper says "The method is motivated by a recent branch-and-cut approach for the box-constrained case that employs linear relaxations of the first-order KKT conditions". The branch-and-cut paper is Vandenbussche & Nemhauser, *Math. Program.* 102:559–575, 2005 (DOI 10.1007/s10107-004-0550-7) | [stated-joint, P]; [practice, P]; the Iowa link [inferred] |
| T3 | Copositive/completely positive programming as a unifying lens (2006–2015) | One exact convex (copositive) representation for mixed binary QPs, then computation (OptDNN, QuadProgBB), then exposition | (a) Unifying scattered results: "This result can be viewed as an extension of earlier separate results, which have established the copositive representation of a small collection of NP-hard problems" (2006 abstract). (b) Funding: the CAREER plan names "linear programs over convex cones, which are one of the main tools to solve nonconvex quadratic programs" (NSF abstract). (c) Consolidation through teaching: the 2015 paper is aimed at "readers new to the area" | [stated, P]; [practice, P] |
| T4 | Into MIQCP / non-convex MINLP (2007–2014) | Relaxations and valid inequalities for mixed-integer quadratic problems; surveys | (a) Transfer framing: "These methods can be viewed as generalizations of techiniques for mixed-integer linear programming" (2009 abstract). (b) The 2012 survey's stated reason: "When non-convexities are present, however, things become much more difficult, since then even the continuous relaxation is a global optimisation problem". (c) Circumstance [inferred]: the CMU visit (Jan–May 2007), Saxena (CMU) on his PhD-committee list (2008), and the joint preprint (Jul 2009); the Letchford line started from box QP (2008) | [stated-joint, P]; [inferred] |
| T5 | Trust-region subproblem (TRS) variants as a long thread (2011 → 2026) | SOC-RLT constraints for extended TRS → TRS with linear cuts → two-trust-region subproblem (TTRS) → OPF application → ball constraints → Lorentz positive cone | Carried forward by successive partners: Anstreicher (2011), student Yang (2013–2018), visitor Eltved (2020), sole author (2023, presented as a "Kurt-Fest!" gift: "gifted to Kurt"; proof "with a key assist from Kurt"), Anstreicher again (2026) | [practice, P]; [stated, P] |
| T6 | Analytics and applications in a renamed department (about 2011–2020) | Program director roles, R and Excel teaching, applied papers (football rankings, tuitions, crop portfolios, grading) | (a) The institution: "The Department of Business Analytics began a self-renewal process 10 years ago with a shift from Management Sciences to a more broadly scoped view of using analytics to solve real-world business problems" (Dean Kristof-Brown, Apr 2021); undergraduate enrollment grew "from 100 students in 2013-14 to nearly 500 in 2019-20". (b) Funding: the CAREER grant ended in May 2012. (c) His own stated motive for a 2015 blog analysis: "I wanted to reproduce their basic analysis but with a simpler approach and easier-to-obtain data set, and I also wanted to complete the full analysis in R." | [observed, S]; [practice, P]; [stated, P] |
| T7 | Copositive methods carried into robust and data-driven optimization (2014–2018) | LP sensitivity, two-stage ARO and DRO bounds expressed as copositive programs | Student Xu's dissertation line: "we prove that they equal the optimal values of two separate, but related, copositive programs" (2015 abstract). The line ends when Xu graduates (2017) | [stated-joint, P]; exit [inferred] |
| T8 | Exactness and convex hulls (2018–2025) | When is the Shor SDP exact; convex hulls for switching variables and bounded products; Stiefel SDPs; slight liftings | Co-author-driven: Ye (2018), Anstreicher and Park (2020), Gilman and Balzano (2022). The Kurt-Fest slides (2 June 2023) credit the Kronecker relaxation as "Introduced by Anstreicher (2017)" | [practice, P]; driver [inferred] |
| T9 | ML-adjacent optimization (2023 →) | Constraint learning, gradient methods over trained ReLU networks, submodular minimization for DRO and pricing | (a) His 2023 framing: "Describe an active area of research at the intersection of optimization and machine learning" (slides). (b) A Mathematics PhD student (Zhu, 2024) and a departmental colleague (Serra, CPAIOR 2026). (c) The constraint-learning paper opens: "The fields of optimization and machine learning (ML) are closely intertwined" and thanks "Paul Grigas for discussions on the relationship between constraint learning and contextual optimization" | [stated, P]; [stated-joint, P] |
| T10 | AI-assisted research code and AI teaching (Dec 2025 →) | Copilot instructions, Claude co-authored commits, exact-arithmetic certificates in released code, a non-technical AI course | New tools. The acknowledgment: "The AI assistants Claude (Anthropic) and Codex (OpenAI) were used to write the code for the computational experiments and for light editing of the text." (arXiv 2609.32017v1). The course: "Thinking Outside the Chat Box" (Tippie Leadership Collaborative, rev. 2026.10.09.1). Its timing right after two outside-found errors (2021, 2026) is [inferred] | [stated-joint, P]; [practice, P] |

### 4.1 What the turns share [inferred]

1. **One machine, many problem classes.** Every turn from T2 on lifts x to a matrix (Shor, completely positive, SOC-RLT, Kronecker or Lorentz-separable) and asks how tight the relaxation is. New problem classes arrive with collaborators, students or the institution; the method stays the same.
2. **Collaborators bring the problems.** Vandenbussche brought box-QP KKT branch-and-cut, Saxena MILP cut machinery, Letchford combinatorial QP, Xu robust optimization, Eltved OPF, Zhu and Serra ML models, and Natarajan DRO and moment problems. I found no turn that he described as self-originated, except T1 ("Can't hurt to try").
3. **Turns coincide with institutional events**: the move to Iowa in 2001 (T2), the CAREER award in 2006 (T3), the CMU visit in 2007 (T4), the department's renewal from about 2011 (T6), and the DGS/DEO roles from 2023 (T9–T10 run alongside administration).
4. **Long threads survive through people.** Anstreicher appears in 2003, 2007, 2008, 2011, 2016, 2020, 2023 and 2026.

### 4.2 How his self-description changed [stated, P unless marked]

- **2003 résumé**: "Operations research, especially discrete and continuous optimization"; "Semidefinite programming, including its application to combinatorial optimization"; "Interior-point methods, nonlinear programming".
- **Jan 2014 CV**: "Analytics, operations research, management sciences" now comes first, then "Convex, copositive, semidefinite, and nonlinear optimization" and "Decision making and optimization under uncertainty".
- **2015 homepage**: "his research and teaching interests include analytics, operations research, management sciences, and optimization."
- **2016, Iowa Now** [observed, S]: "who researches business analytics".
- **2023 video bio**: "his research focuses on convex optimization, especially semidefinite and copositive programming."
- **2026 homepage**: "has spent his career working on mathematical optimization — developing theory and algorithms for hard problems that arise in operations research and beyond." The same page adds: "A dedicated teacher, he has been founding faculty director of two Master's programs".
- **Reading** [inferred]: the analytics-first wording of 2014–2016 tracks the department's renewal (T6). From 2023 the wording returns to optimization, after the 2020 and 2023 awards for his thesis-era work.

---

## 5. Entry and exit relative to the field

| Topic | Entry | Exit or status | Relative to consensus | Evidence |
|---|---|---|---|---|
| Low-rank SDP (Burer–Monteiro) | 2000, early. Factorization ideas existed (Peinado–Homer 1997; their own lower-triangular variant); the low-rank rank-bound version was theirs | **Left as algorithm author around 2004–2006**: last paper submitted Jul 2004, printed 2006. He dates his part "up to maybe around 2003 or 2004" (machine transcript) | Left a decade **before** the 2016+ "benign nonconvexity" and ML wave, which his 2023 slides credit to others (Ge–Lee–Ma 2016, Bhojanapalli et al. 2016, Boumal, Cifuentes–Moitra 2021). On their role: "we didn't really mean it but this was part of what people started to call benign non-convexity" (machine transcript). Recognition came 17–20 years later (ICS Prize 2020; Test of Time 2023). He returned as code maintainer (2023, 2026) and retrospective speaker, not with new low-rank papers | [practice, P]; [stated, P]; [observed, S] |
| Copositive / completely positive | 2003 (with Anstreicher). Central paper 2006/2009 | Active through 2018 (ARO, DRO). Still lectured on in 2022 ("Vignettes on Copositive Optimization", MIT). The 2026 Lorentz-positive-cone paper reuses the cone-duality pattern [inferred] | Entered after special cases existed ("earlier separate results", his own wording), then **wrote the field's entry points** (2012 handbook chapter; 2015 gentle introduction "for readers new to the area"). The copositive representation paper has 408 citations in OpenAlex [observed, S] | [practice, P]; [stated, P] |
| Global nonconvex QP by branch-and-bound | 2005 | Last solver paper 2011/2012 (QuadProgBB). GitHub repository last pushed 2016-07-08; BoxQP instances posted 2019 | Did not join later QP-solver development; reasons not stated | [practice, P] |
| MIQCP / non-convex MINLP | 2009 | Surveys 2009–2012, MIQP theory 2014, convexification talks 2021–22, switching-variable hull 2021 | Entered as a **surveyor and relaxation theorist**, not a solver builder. The 2012 survey has 567 citations in OpenAlex [observed, S] | [practice, P] |
| TRS variants | 2011 | Still active in 2026 (TTRS in arXiv 2609.32017) | Long-running niche thread | [practice, P] |
| Robust / data-driven optimization | 2014 | 2018 | Entered a mature area. The abstract places the work as one that "unifies and extends multiple approaches for LP sensitivity analysis in the literature and has close ties to worst-case linear optimization and two-stage adaptive optimization". Exit coincides with Xu's graduation [inferred] | [stated-joint, P] |
| Business-analytics applications | 2011 | Last applied paper 2019 (grading) | Driven by the department, not by a field consensus [inferred] | [practice, P] |
| Constraint learning / optimization over trained NNs | 2024 | Active | **Late entrant.** The paper cites the survey of Fajemisin et al. (2023) and Maragno et al. (2025). He brings convex-hull geometry: "a standard convex-hull idea but in an extended space" | [stated-joint, P] |
| Continuous submodular minimization (with DRO and pricing uses) | 2025 | Active; core claim narrowed (§6) | New area for him. It opened with an overclaim that he corrected (§6) | [practice, P] |

---

## 6. Failures, corrections, abandoned directions and slow papers

1. **Error in a published theorem (Burer & Ye 2020, corrected 2021).** The correction note (published online 8 Jul 2021) says:
   - "This note reports an error in Theorem 3 of [1], which was pointed about by Prof. Fatma Kılınç-Karzan and Mr. Alex Wang of Carnegie Mellon University, whom we sincerely thank for bringing this to our attention."
   - "However, in truth the proof fails because, with this setup, the systems cannot be simultaneously feasible."
   - "Instead of the purported Theorem 3, we now prove an analogous theorem, except that it only applies to diagonal instances of (1)."

   His Jan 2021 talk title already reads "…Nonconvex Diagonal QCQPs" (CV P32; the word "Diagonal" is the change), six months before the correction appeared. Alex Wang later had Burer on his CMU PhD committee (CV, 2022). The CV keeps the original title and lists the erratum beside it. [stated-joint, P]; [practice, P]
2. **Overclaim retracted across arXiv versions (2504.03996, 2025–2026).**
   - v1 (4 Apr 2025, Burer & Natarajan): "We show that continuous quadratic submodular minimization with bounds is solvable in polynomial time using semidefinite programming". Its §2.2 states that the relaxation "is tight for every submodular" data instance, and adds: "Our proof is by induction on n with base case n = 1."
   - INFORMS talk (Oct 2025): hedged title "Towards the Semidefinite Representability…" (CV P07). In the Jan 2026 talks the title is again "On the…" (CV P02–P05).
   - v2 (5 Apr 2026): "propose a polynomially sized semidefinite relaxation, which is provably tight for dimension n ≤ 3 and empirically tight for larger n" (math rendered).
   - v3 (31 Aug 2026; Rick Willemsen added as third author; pricing application added): "Via an explicit counterexample for n = 4, we show that the relaxation is not tight in general, although it remains empirically tight on randomly generated instances." The acknowledgement reads: "We thank Shaoning Han for pointing out an error in an earlier version of this paper." The paper adds that "Section 6.4 verifies these claims in exact rational arithmetic", and reframes the failure as one of "this particular semidefinite certificate, not necessarily tractability itself".

   Response pattern [practice, P]: narrow the theorem to what is provable, construct and certify the counterexample, thank the outside finder by name, add an application, and release code that "reproduces every computational claim the paper makes" (`submodular-tests` README).
3. **Post-publication counterexamples to his own paper's natural conjectures** (Aug 2026). The `ballconstraints` README adds "a self-contained exact verification of two projection counterexamples discovered after the paper" and states plainly: "These conjectures are not statements made in the paper." Also: "Consequently, the reported separations do not depend on an SDP solver's numerical tolerance." [stated, P]
4. **Slow papers** (indirect signals only; no reviews or rejections are public) [practice, P; reading inferred]:
   - Inventory games with Dror: posted 11 Jan 2005 as "Convex Optimization of Centralized Inventory Operations", online in *TOP* 8 Oct 2010 as "Newsvendor games: …" (DOI 10.1007/s11750-010-0160-x), print 2012. That is 5.7 years plus a retitling.
   - TSP with interval travel times: manuscript "January 2010", still "Submitted to Far East Journal of Applied Mathematics" in the Jan 2014 CV, published there in 86(2):117–144, 2014. That venue is outside his usual journals, and the paper has no DOI in Crossref.
   - IV quantile regression: 2.4 years. Two-variable TTRS: 2.3 years. SOC for extended TRS: 2.0 years.
5. **Narrowed or renamed projects.**
   - "Exploiting Structure in Mixed Conic Programming" with Anjos ("in progress", 2003). Their only joint paper is the narrower free-variables paper (2006/2007) [mapping inferred].
   - "Old Wine in a New Bottle" was dropped from the MIQCP chapter title.
   - "Semidefinite-Based Branch-and-Bound" became "A finite branch-and-bound algorithm…".
   - [practice, P]
6. **Directions dropped without later papers** [practice, P]: low-rank SDP algorithms (after 2006); global QP solver codes (after 2012); operations-management applications (supply chain 2008, inventory 2012); ML ensembles (2005–06, dormant until 2024); robust optimization (after 2018). **No stated reason for any exit was found.**
7. **Acknowledged theory gaps in the low-rank work.** The slides say "In the early 2000's, this seemed challenging to answer" (why the factorization works). In the talk: "we had some kind of strong assumptions here" (machine transcript), about the convergence result that needs local minima at every augmented-Lagrangian step. [stated, P]
8. **Funding gap.** No external research grant appears after the CAREER award ended in May 2012 (CV; NSF API lists two awards in total). Reasons unknown. [practice, P]

---

## 7. The last 12 months (10 Oct 2025 → 10 Oct 2026)

| Date | Item | Tag |
|---|---|---|
| Oct 2025 | INFORMS Annual Meeting (Atlanta) talk: "Towards the Semidefinite Representability of Continuous Quadratic Submodular Minimization with Applications To Moment Problems" (CV P07) | [practice, P] |
| 1 Oct 2025 | Tippie news lists him in the lifetime category of the Stanford "top 2%" study (also listed Oct 2023 and Jan 2025) | [observed, S] |
| 28 Nov – 12 Dec 2025 | `submodular-tests` repository created; "Add Github Copilot instructions" | [practice, P] |
| 30 Dec 2025 → 1 Jun 2026 | arXiv 2512.24295 (Tong, Zhu, Serra, Burer), "Optimization over Trained Neural Networks: Going Large with Gradient-Based Algorithms". Optimization Online 3 Jan; v2 18 Mar. Published at CPAIOR 2026 in LNCS, pp. 596–613, online 1 Jun 2026 (DOI 10.1007/978-3-032-27242-3_35) | [practice, P] |
| Jan 2026 | Talk tour: HK PolyU, Cornell, Lehigh and Rice (submodular paper); University of Hong Kong (constraint learning) (CV P02–P06) | [practice, P] |
| 6 and 27 Jan 2026 | Code-and-data record (DOI 10.1287/ijoc.2024.0815.cd, seen in OpenAlex only), then "An Extended Validity Domain for Constraint Learning" online in *INFORMS J. Computing* (DOI 10.1287/ijoc.2024.0815; arXiv 2406.10065) | [practice, P] |
| 12 Feb 2026 | CV updated (PDF metadata) | [practice, P] |
| 20 Mar 2026 | Homepage redesign, in a commit with a "Claude Sonnet 4.6" co-author trailer. New bio (§4.2) | [practice, P] |
| 23 Mar 2026 | SDPLR hardening sprint: 11 commits carrying a "Co-Authored-By: Claude Sonnet 4.6" trailer (NULL checks, error exit codes, a five-problem test suite, a `CLAUDE.md` developer reference, README rewrite) | [practice, P] |
| 5 Apr 2026 | arXiv 2504.03996v2: claim narrowed to n ≤ 3 | [practice, P] |
| Jun 2026 | SIAM Conference on Optimization (Edinburgh), invited talk on the submodular paper, listed in the Feb 2026 CV. **Delivery not verified** | [stated, P] |
| 7–9 Jul 2026 | "Business Analytics Research Rankings" website, "Built for the Tippie College of Business" (data 2020–2024): DEO-side work | [practice, P] |
| 29 Jul – 28 Aug 2026 | `ballconstraints` maintenance and "Add exact projection counterexample certificates" (two commits with "Claude Opus 5" trailers) | [practice, P] |
| 24–26 Aug 2026 | `submodular-tests` rebuilt around the paper's artifacts (six commits with "Claude Opus 5" trailers) | [practice, P] |
| 31 Aug 2026 | arXiv 2504.03996v3: counterexample, third author, acknowledgement to S. Han (§6) | [practice, P] |
| 15–25 Sep 2026 | `lorentz-positive` repository (three levels of reproducibility, committed raw results, provenance checks, a standalone TTRS counterexample verifier; reuses `ballconstraints` as a git submodule). Optimization Online 24 Sep; **arXiv 2609.32017** (25 Sep) with Anstreicher, "Applications of the Lorentz positive cone in nonconvex quadratic optimization", which acknowledges Claude and Codex | [practice, P]; [stated-joint, P] |
| 9–10 Oct 2026 | Course site "Thinking Outside the Chat Box" ("AI for Real Work"), Tippie Leadership Collaborative, two four-hour sessions co-taught with Alice Wang. Schedule marked "Planning draft". Blocks include "Asking well, verifying hard" and "Research that holds up". It warns: "Context is not permission." Participants use ChatGPT Work or Claude Cowork ("You will not use a terminal, Claude Code, or Codex in this course.") | [stated-joint, P] |

**Reading of the window** [inferred]:

- Three research lines are active: QCQP relaxations with Anstreicher, submodular minimization for DRO and pricing with the SUTD group, and ML-embedded optimization with Zhu and Serra.
- The tooling has visibly shifted to AI-assisted code with exact-arithmetic certificates and multi-level reproducibility scripts, which no earlier repository of his has.
- The administrative load is high (DEO).
- Yilin Zhu's graduation (expected Spring 2026) and any new student were not verified.

---

## 8. Candidate trajectory heuristics for the skill (all [inferred] from §§1–7)

- **H1. Keep one lifting machine and carry it to new problem classes.** Let partners bring the class (QP, MIQCP, TRS, robust LP, OPF, ML surrogates, submodular functions) and ask each time how tight the lifted relaxation is.
- **H2. Prototype first, explain later.** "Can't hurt to try": implement in a day, then measure. Leave the slide's question "Why should this work at all?" open if needed. In his case others answered it 15 years later.
- **H3. Write the entry point once the core result is in.** He wrote the copositive handbook chapter (2012), the gentle introduction (2015), the MINLP survey (2012) and the IPCO SDP tutorial (2019) after his own core papers.
- **H4. Exit quietly; return through retrospectives, code or a new student, not through incremental papers.** Low-rank (2006 → 2023), B&B codes (2012), robust optimization (2018).
- **H5. Keep long threads alive through people** (the Anstreicher line, 2003–2026; TRS through Yang, Eltved and solo work).
- **H6. When an error is found, narrow the theorem to what is provable, name the finder, and (from 2026) certify the counterexample in exact rational arithmetic in released code.**
- **H7. Absorb institutional demands without abandoning the core line.** The analytics pivot, program directorships and the DEO role changed what he taught and how he described himself. His relaxation-theory output continued, at a lower rate.

---

## 9. Trajectory as seen in the full texts (added 2026-10-10)

Added at the deep-reading synthesis (stage T3.6) from [08-deep-reading-synthesis.md](08-deep-reading-synthesis.md) §§8–9 and the paper cards indexed in [07-paper-cards.md](07-paper-cards.md): 71 works, 52 read in full and 15 in part. Sections 1–8 above were written from web research and are kept unchanged; where the full texts change a date, the change is listed in §9.3 and the earlier wording stays where it is.

### 9.1 Topics per period (works carded)

| Period | Works carded | Main topics (cards) |
|---|---|---|
| 2000–04 | 11 | SDP algorithms by change of variables: projected gradient on a factor, rank-two max-cut, Cholesky elimination, rank-one/two stable set, low-rank SDPLR, partial matrices, long-step framework [S014, S006, S017, S025, S030, S001, S029, S032, S051] |
| 2005–09 | 17 | Low-rank theory and enhancements [S003, S026, S031, H002]; lift-and-project bounds for 0-1 IP [S013, S041]; finite SDP B&B for QP [S007, S018]; copositive representation and CP/DNN [S004, S034, S028]; box-QP polyhedra [S011]; applied (ensembles, seed supply chain) [S005, S054, S015] |
| 2010–14 | 18 | CP/DNN computation and QuadprogBB [S020, S008, S047, H001]; hulls, cones and TRS with cuts [S010, S009, S022, S040, S037, S012]; MIQCP framing and survey [S016, S002]; "middle way" relaxations [S043]; analytics side papers [S042, S052, S053, S060, S063] |
| 2015–19 | 12 | TRS and quadratic hulls with Yang and Kılınç-Karzan [S021, S024, S033, S027, S036]; copositive robust/DRO and statistics with Xu [S045, S023, S044, S059]; applied [S046, S062] |
| 2020–24 | 7 | SDP exactness and its correction [S019, S061]; hulls of switching and bounded products [S038, S039, S067]; strengthened SDPs (OPF substructure, Stiefel) [S050, S055] |
| 2025–26 | 6 | Ball constraints, TTRS, Lorentz-positive cone [S049, S065]; submodular QP [S058]; Stiefel certificate [S048]; constraint learning and trained networks [S057, S056] |

### 9.2 Turns visible in the texts

1. **From algorithms for convex SDP to bounds for nonconvex and integer problems, about 2005–06** (T2 above): the 0-1 lift-and-project paper names mixed binary-continuous and nonconvex QP as next targets [S013 p. 24]; the award note describes the shift away from IPs [H001 p. 2].
2. **From finite B&B solvers to a single strong relaxation as the product** (new): [inferred] the single-strong-relaxation aim is stated by 2011/12, "We are also not specifically concerned with the global optimization of (MIQCP)." [S016 preprint p. 2], and pursued in the hull papers from 2009 [S011; S010]; it ran alongside the KKT-branching line (2008–2012) [S007; S018; S008; S047], after which the cards hold no new global QP solver; restated in 2023, "In this paper, however, we seek a relaxation that is strong irrespective of the data." [S049 arXiv p. 2].
3. **Applied and analytics papers with Iowa colleagues and students, 2012–2019** (T6, T7 above) [S042, S052, S053, S060, S046, S045, S023, S044, S059, S062].
4. **ML-adjacent work with students and colleagues from 2025** (T9 above) [S048, S057, S056].
5. **A return of the low-rank line through certificates, 2025** (new): a cheap LMI certificate for the output of any Stiefel-manifold solver [S048 arXiv pp. 5-7, 14], the pattern of the 2001–2006 factorization papers (Method 6 in SKILL.md), absent from the cards between 2007 and 2024.

What stayed constant: the lifted matrix [1 xᵀ; x X] from the ensemble-pruning SDP [S005 pp. 7-8] to the Lorentz cone [S065 pp. 2-7]; the Pataki rank bound from 2003 [S001 p. 5] to 2026 [S065 p. 10]; losses printed with a hypothesis from 2001 [S014 preprint p. 17] to 2026 [S056 arXiv pp. 13-15]; claims graded by level from 2002 [S025 pp. 17-18] to 2026 [S065 pp. 10, 14, 16].

### 9.3 Dates that the full texts change (earlier wording kept above)

- **Low-rank exit** (§5 table "around 2004–2006"; §6 item 6 "after 2006"; §8 H4): algorithm papers continue to 2007 [S026 pp. 4-7, 19; S031 pp. 3-5]; SDPLR is documented as software in 2009 [H002 pp. 1-4] and used in a 2011 application [S063 pp. 7-8]; the line returns in 2025 [S048 arXiv pp. 5-7, 14].
- **Robust optimization** (T7 "2014–2018"; §5 table "2018"; §6 item 6 "after 2018"): the robust/applied period runs to 2019 [S062 pp. 5-8].
- **Exact certificates** (§8 H6 "from 2026"): an explicit rational counterexample point already appears in 2009 [S011 pp. 15-16] (rational counterexample data in 2010 [S010 p. 8]); certification in exact arithmetic is documented in 2025 [S058 pp. 43-44]; the 2026 counterexamples are certified by exhaustive stationary-point enumeration and a second solver, not in exact arithmetic [S065 p. 16] (⚠, downgraded from ✗ on review).
- **KKT B&B line** (not dated above): 2008–2012 [S007; S018; S008; S047].
- **Heuristics**: no heuristic paper in the core nonconvex-QP line after 2002, but heuristics recur in coauthored applied papers (2006 [S005 pp. 7-8], 2011 [S063 pp. 4-5, 9], 2026 [S056 arXiv pp. 6-9, 15]).

### 9.4 Collaboration pattern in the cards

Monteiro coauthors 8 of the 11 carded works of 2000–04 and Yin Zhang 5; Kurt Anstreicher coauthors 8 works from 2005 to 2026 [S034, S028, S010, S012, S036, S038, S039, S065], supplies the observation behind the 2025 main theorem [S049 arXiv p. 24] and a conjecture credited in 2009 [S011 p. 14]. Students appear as coauthors by line: Chen [S041, S047, S008, S060], Choi [S026, H002, S063], Dong [S022, S040], Yang [S021, S033, S036, S067], Xu [S045, S059, S023, S044], Park [S039, S055], Zhu [S057, S056]; student lines tend to carry the toolkit into a new domain. The founding CP theory is sole-authored [S004; S009; S020; S024], its solver went to a student [S008]. No full text states why any line ended (§6 above stays the reference for the web-research view).

---

## Contradictions (kept, not reconciled)

1. **Dates of the collaborative NSF grant.** The CV says "$255,818, 2000-05". The NSF record for award 0203426 gives 06/15/2002 → 05/31/2006.
2. **Student roster.**
   - MGP lists Yi Zhang (2006) and Nathaniel Richmond (2016) as his students (advisor 2); the CV puts both under "Ph.D. Committee" only.
   - The CV lists Changhui Choi (2007) as an advisee; MGP does not list Choi.
   - MGP shows a 2018 Washington State student under Hongbo Dong, but the CV's placement columns for Dong read only "University of Wisconsin Madison (initial)" and "Meta (current)".
3. **Date of the SIAM OP23 talks.** The CV says "May 2023"; the slides and the repository README say "June 2, 2023".
4. **Self-description.**
   - 2014–2016: analytics first ("his research and teaching interests include analytics, operations research, management sciences, and optimization"; Iowa Now: "who researches business analytics").
   - 2023: "his research focuses on convex optimization, especially semidefinite and copositive programming".
   - 2026: "has spent his career working on mathematical optimization".
5. **Department name in recent preprints.** The CV says the department became Business Analytics in April 2019. arXiv 2504.03996 v1 (2025) and v3 (Aug 2026) still give "Department of Management Sciences, University of Iowa". arXiv 2406.10065v2 (2025) and 2609.32017v1 (2026) give "Department of Business Analytics".
6. **The submodular claim across versions** (left as three statements):
   - v1: "solvable in polynomial time using semidefinite programming";
   - v2: "provably tight for dimension n ≤ 3 and empirically tight for larger n" (math rendered);
   - v3: "not tight in general".
7. **Burer–Ye title vs content.** The published title keeps "(Random and Non-Random)" and the CV keeps it unchanged. After the 2021 correction, the replacement theorem "only applies to diagonal instances".
8. **Prize names.** "INFORMS Computing Paper Prize" (homepage 2026, video bio 2023), "ICS Prize" (CV) and "INFORMS Computing Society Prize" (INFORMS).
9. **Year of the rank-two max-cut paper.** The CV says *SIOPT* 12:503–521, "2001"; Crossref print date is January 2002.
10. **Which talk the YouTube video is.** The video title matches the SIAM lecture, but the speaker places it "a couple of months" before "a conference" (machine transcript), i.e. it is the March 2023 Iowa version.

## Gaps

- **DBLP**: unreadable (bot challenge on every endpoint). The DBLP-only record, including any DBLP-only items, was not checked.
- **Dissertation full text**: the Georgia Tech repository returned HTTP 401 for the PDF, so the acknowledgments and introduction were **not read**. Only the metadata was used.
- **Why he moved or stayed**: no stated reason was found for choosing Iowa (2001), a business school, the visits to CMU and Rome, or the 2025 DEO role, and none for leaving low-rank SDP, global QP codes, robust optimization or OM applications. The 2023 slides and talk explain only how the low-rank idea arose. No interview or oral history was found (both WebSearch calls were spent: one on the Test of Time award, one on recent Tippie news).
- **SIAM award page**: HTTP 403 to curl and WebFetch, with no Wayback copy. The award is confirmed through the CV, Tippie and GT ARC news, the slide file name, and the 2023 bio.
- **Plenary transcript**: I could not retrieve captions myself. The sibling-saved auto-caption transcript covers the **March 2023 Iowa** version only. The SIAM version of 2 June 2023 is known from its slides.
- **Last 12 months**: delivery of the June 2026 SIAM OP26 talk, Yilin Zhu's graduation, and any new advisee were not verified. Conference programs (INFORMS 2025, OP26) were not searched.
- **Rejections and reviews**: none are public. Publication lags are the only indirect signal.
- **Anstreicher's retirement date**: known only from the 2 June 2023 slide "Happy Retirement, Kurt!".
- **Arrival dates of colleague Thiago Serra and visitor Anders Eltved at Iowa**: not verified.
- **Affiliations of Gilman and Balzano**: not checked, so not stated.
- **Google Scholar numbers** (7,294 citations, h-index 34, per-year histogram from 23 in 2001 to 536 in 2025 and 550 in 2026 so far) come from a WebFetch summary by a small model. Treat them as approximate.
- **His *Optima* co-editor columns (2010–18) and his LinkedIn page** (login wall): not read.

## Sources

Primary = his own writing, slides, code history or bibliographic records of his own papers. Secondary = third parties, aggregators or institutional pages.

1. S. Burer, curriculum vitae, 18 pp., "updated February 12, 2026". https://sburer.github.io/files/cv.pdf (primary)
2. S. Burer, homepage, footer "Last updated 2026-03-20", fetched 2026-10-10. https://sburer.github.io/ (primary)
3. sburer.github.io repository history: `index.html` versions of 2015-05-10, 2016-10-03, 2019-07-03 and 2021-10-04; seven blog posts 2015-05-10 → 2016-05-11 (`_posts`); numbered paper archive `papers/001…062`. https://github.com/sburer/sburer.github.io (primary)
4. Wayback snapshots of his first homepage, 2005-02-12, 2007-08-19 and 2008-03-04, the 2010 DokuWiki raw exports, the 2003 résumé (snapshot 2004-01-04; PDF created 2003-09-30) and the January 2014 CV (snapshot 2014-03-11). https://web.archive.org/web/2008/http://dollar.biz.uiowa.edu/~sburer/ (primary, archived)
5. S. Burer, GitHub profile and repositories (sdplr, ballconstraints, submodular-tests, lorentz-positive, business-analytics-rankings, 2023-06_SIOPT, ipco-2019-sdp-tutorial, QuadProgBB, soctrust and others): READMEs, `CLAUDE.md`, commit logs and co-author trailers, fetched 2026-10-10. https://github.com/sburer (primary)
6. S. Burer and R.D.C. Monteiro, "Two Decades of Low-Rank Optimization", slides, SIAM Conference on Optimization, Seattle, 2 June 2023 (86 pp.). https://github.com/sburer/2023-06_SIOPT (test-of-time.pdf) (primary)
7. S. Burer, "On Nonconvex Quadratic Programming with Ball Constraints" ("Kurt-Fest!"), slides, Seattle, 2 June 2023 (53 pp.). https://github.com/sburer/2023-06_SIOPT (kurt-fest.pdf) (primary)
8. "Two Decades of Low-Rank Optimization" video (March 2023 Iowa version, uploaded 2023-09-09): description and bio, and the sibling-saved auto-caption transcript `sources/talks/2023-two-decades-of-low-rank-optimization_youtube-wSauUgRIQDg_auto-captions.txt`. YouTube channel feed (teaching videos 2013–2016). https://www.youtube.com/watch?v=wSauUgRIQDg (primary; machine transcript)
9. arXiv API author listing (15 entries, 1406.1031 → 2609.32017). Abstract pages and version histories of 2609.32017, 2504.03996 (v1–v3), 2512.24295 and 2406.10065. Full texts read: 2504.03996v1, 2504.03996v3 and 2609.32017v1; front matter of 2512.24295v2, 2406.10065v2 (with acknowledgments) and 1802.02688v1. https://arxiv.org/abs/2504.03996 etc. (primary)
10. Optimization Online author archive "Samuel Burer" (48 entries, 2001-03-09 → 2026-09-24) and 9 abstract pages (2003/05/660, 2005/06/1167, 2006/10/1501, 2009/07/2338, 2011/03/2957, 2011/10/3199, 2012/02/3378, 2014/09/4558, 2015/09/5106). https://optimization-online.org/author/samuel-burer/ (primary)
11. S. Burer and Y. Ye, "Correction to: Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", *Math. Program.* 190:845–848, 2021. DOI 10.1007/s10107-021-01684-5 (primary)
12. "Thinking Outside the Chat Box" course site (index, modules, instructors, context and setup pages), revision 2026.10.09.1. https://sburer.github.io/aicourse/ (primary, joint)
13. NSF award records 0545514 (CAREER, 2006–2012) and 0203426 (collaborative, 2002–2006), with abstracts, via the NSF API. https://api.nsf.gov/services/v1/awards.json?pdPIName=Burer (primary records)
14. Crossref records for the 59 Crossref-verified DOIs cited above (62 checked), fetched 2026-10-10, including Vandenbussche & Nemhauser, DOI 10.1007/s10107-004-0550-7, and the ICDM'05 paper, DOI 10.1109/ICDM.2005.131. https://api.crossref.org/works/ (secondary bibliographic data for primary papers)
15. Mathematics Genealogy Project records 114747 (Burer), 132760 (Monteiro), 19778 (Adler), 171258, 161093, 323999, 243710, 250620, 323166 and 108903 (students). https://www.mathgenealogy.org/id.php?id=114747 (secondary)
16. OpenAlex author A5002663715 and its 88 works (dates, DOIs, citation counts). https://api.openalex.org/authors/A5002663715 (secondary)
17. ORCID public record 0000-0001-5886-458X (7 works). https://orcid.org/0000-0001-5886-458X (secondary)
18. INFORMS award-recipient page "Samuel Burer" and the INFORMS Computing Society Prize page. https://www.informs.org/Recognizing-Excellence/Award-Recipients/Samuel-Burer (secondary)
19. Georgia Tech ARC news, "SIAM Activity Group on Optimization Test of Time Award for Prof. Rentao Monteiro", 18 Feb 2023. https://www.tlwarc.hg.gatech.edu/node/665928 (secondary)
20. Tippie College of Business, "Burer honored for long-term impact of paper", 31 Jan 2023. https://tippie.uiowa.edu/news/2023/01/burer-honored-long-term-impact-paper (secondary)
21. Iowa Now, "Burer receives top INFORMS computing society honor", 19 Aug 2020. https://now.uiowa.edu/news/2020/08/burer-receives-top-informs-computing-society-honor (secondary)
22. Iowa Now (T. Snee), "Data mining for better farming", 31 Mar 2016. https://now.uiowa.edu/news/2016/03/data-mining-better-farming (secondary, with quotes attributed to him)
23. Tippie College of Business, "Tippie Analytics wins major international analytics award", 14 Apr 2021 (Dean Kristof-Brown's statement on the department's renewal). https://tippie.uiowa.edu/news/2021/04/tippie-analytics-wins-major-international-analytics-award (secondary)
24. Tippie news on the Stanford top-2% lists, 13 Oct 2023, 2 Jan 2025 and 1 Oct 2025. https://tippie.uiowa.edu/news/2025/10/tippie-faculty-named-among-top-scientific-researchers-stanford-study (secondary)
25. Tippie Business Analytics "Tenured & Tenure-Track Faculty" page ("Department Executive Officer, Tippie-Rollins Professor in Business Analytics"), fetched 2026-10-10. https://tippie.uiowa.edu/about/business-analytics-department/tenured-and-tenure-track-faculty (secondary)
26. INFORMS Connect job posting, Visiting Assistant Professor, Business Analytics, Iowa, posted 2025-05-24 (Burer as Search Committee Chair). https://connect.informs.org/cai/discussion/visiting-assistant-professor-department-of-business-analytics-tippie-college-of-business-university-of-iowa-2 (secondary)
27. Google Scholar profile BScCde0AAAAJ, read through WebFetch (model summary) on 2026-10-10. https://scholar.google.com/citations?user=BScCde0AAAAJ (secondary)
28. Georgia Tech repository record for the dissertation (DSpace API metadata only; PDF returned HTTP 401). http://hdl.handle.net/1853/30268 (secondary)
29. WebSearch result lists for 2 queries (the Test of Time award; recent Tippie news), 2026-10-10. They were used only to locate items 19–21 and 23–26. (secondary)
