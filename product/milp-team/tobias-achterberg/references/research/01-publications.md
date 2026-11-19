# Tobias Achterberg · 01 · Publication landscape and signature works

| | |
|---|---|
| Researcher | Tobias Achterberg (DBLP pid 71/6632; ORCID 0000-0002-0862-7065; Semantic Scholar author 1793775; MGP id 117695). Lens per team.json: MILP solver engineering (reliability and hybrid branching, conflict analysis, presolve), original author of SCIP, CPLEX and Gurobi developer |
| Dimension | Research agent 01 of 06: publication landscape and dissection of signature works (framework §二 Agent 1, §五) |
| Research date | 2026-11-08 |
| Sources consulted | 29, listed as S1–S29 under *Sources* (15 primary, 14 secondary). 5 of the 5 allowed WebSearch calls were used, only to find leads; every fact below was then checked on the page or record itself with curl, WebFetch, the Crossref, DataCite, ORCID, Unpaywall and Semantic Scholar APIs, ZIB OPUS OAI-PMH, and `scripts/dblp_works.py` |
| Local corpus | `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep` when this run began: no user-supplied material. `RESOURCES.md` is the T0 template. `private/` was not opened. During the run, research agent 04 saved `talks/subject-to-2023-interview.excerpt.transcript.txt` (excerpts of YouTube auto-captions of a 2023 interview); I read it and use it as S29, with timestamps. It is caption text, not speaker-checked, and not user-supplied |
| OpenAlex | not queried (`OPENALEX_API_KEY` is not set) |
| Google Scholar | not reachable: the author search redirects to a Google login page and the plain search stops at a session-verification page (2026-11-08). No Scholar counts are used |
| Living status / present role | Living (team.json). Vice President of R&D at Gurobi since a promotion announced on 22 April 2020 (S17); the SEA 2022 bio calls him VP of R&D (S13); ORCID lists employment at Gurobi Optimization GmbH from 2014-03 (S15). Gurobi's *Our People* page fetched 2026-11-08 does not mention him, so the 2026 title is not re-confirmed |
| Quotation policy | To respect copyright, findings are paraphrased with a pinpoint page; exactly one short verbatim phrase is quoted (marked with quotation marks). Check exact wording at the cited page before quoting downstream |

**Tags.**
- **[stated]**: said or written by Achterberg in a sole-author text or his own talk slides. **[stated, joint]**: a co-signed text whose *we* cannot be split among authors.
- **[practice]**: what the record shows was done (experiments, tables, test-set construction, code facts, the publication record itself).
- **[observed]**: what others recorded (prize citations, press releases, bios written by others, bibliographic databases, later papers).
- **[inferred]**: my inference; the basis is named.
- **P / S**: primary / secondary source.

**Page conventions.** Thesis (S1): printed page numbers of the revised ZIB copy (OPUS docId 1112, 426 PDF pages, revision dated 10 December 2008); the TU Berlin DepositOnce copy (2007, 418 PDF pages) uses Type 3 fonts and was not used for page references. ZIB-Reports (S2–S8): the report's own printed page numbers. RAMP 2014 (S9): the proceedings' page numbers (181–196). Slides (S10, S11): slide k = PDF page k. Citation counts: C = Crossref, SS = Semantic Scholar (SS is not a source label).

**Reading depth.**
- Read in full or nearly so: S2 (ZR 02-32, 16 pp.); S29 (all fourteen caption excerpts; the rest of the 84-minute video was not watched).
- Read in part: S1 (acknowledgements pp. ix–x, introduction pp. 1–6, ch. 5 pp. 61–66, ch. 11 pp. 165–166 and 178–181, appendix A pp. 319–322, bibliography), S3 (pp. 1–12, the main text before the tables), S4 (pp. 1–3), S5 (pp. 1–2, 14–18), S6 (pp. 1–2), S7 (pp. 1, 4, 7), S8 (pp. 1–4, 12, 16–17, 51, 56, 63–65), S9 (pp. 181, 190–191), S10 (all slide titles; slides 1–5, 17–26, 65), S11 (all slide titles; slides 1–2, 21–26).
- Abstract or metadata only: every other work in §1.2 (see its *Read* column).
- Not reached: Google Scholar (login wall), OpenAlex (no key), the ZIB OPUS search and export endpoints (HTTP 500 on 2026-11-08; the OAI-PMH interface worked), the journal versions behind paywalls (MPC 2009, ORL 2005, IJOC 2020, Facets 2013 are closed per Unpaywall, S24).

---

## 0. Authorship and role labels (must survive into the skill)

| Label | Evidence | Tag |
|---|---|---|
| Sole author of the thesis (2007), of *Conflict analysis in mixed integer programming* (2007) and of *SCIP: solving constraint integer programs* (2009), plus their ZIB-Report precursors ZR 04-19 and ZR 05-19 | S1, S4, S5, S18 | [practice] P |
| SCIP development began in October 2002; most ideas and algorithms of Alexander Martin's SIP solver went into the first version; SCIP 0.90i had 223,178 lines of C (145,676 framework, 77,502 plugins) plus 58,363 lines for the chip-verification plugins | S1 p. 6 | [stated] P |
| He wrote more than 250,000 lines of C for SCIP and the chip verification solver; Kati Wolter and Timo Berthold, whom he calls his students, also improved SCIP | S1 p. x | [stated] P |
| Chapter 5 (branching) of the thesis is mostly joint work with Thorsten Koch and Alexander Martin | S1 p. 61 | [stated] P |
| The cutting-plane and primal-heuristic details of SCIP are in Wolter's and Berthold's diploma theses (TU Berlin 2006); the thesis covers them only briefly | S1 pp. 3–4 | [stated] P |
| History branching (2002) and reliability branching (2004) were both implemented and tested in SIP, not SCIP, as each report says | S2 p. 1; S3 p. 12 | [stated, joint] P |
| CPLEX R&D member from 2006; lead MIP developer for CPLEX 12.0 through 12.6 (Gurobi's 2014 announcement); the SEA 2022 bio says CPLEX developer for versions 11 to 12.6 | S16; S13 | [observed] S (see Contradiction C6) |
| Gurobi: senior developer from 2014; VP of R&D from April 2020, leading the R&D department and overseeing development of the Gurobi Optimizer | S13; S16; S17 | [observed] S |
| Gurobi-era papers describe Gurobi as a company code (*Presolve reductions*, 2014 and 2016/2020). Author lists are alphabetical (Achterberg, Bixby, Gu, Rothberg, Weninger), so the order does not show who did what | S8 p. 1; S9 p. 181 | [practice] P; role split [inferred] |
| Post-2014 code is closed. A published Gurobi result is evidence of the team's practice, not of his personal code | S8, S9, S10, S11 | [inferred] |
| At CPLEX his first project was adding reliability branching, the second conflict analysis; he says he ported what he knew worked from SCIP and later worked on all MIP parts of CPLEX except the LP solver | S29 0:40:00–0:42:00 (captions) | [stated] P |
| For Gurobi 9.0's non-convex MIQCP solver he says he did most of the work on handling the non-convex constraints in the tree and the LP relaxation, with colleagues contributing other parts | S29 0:47:00–0:47:30 (captions) | [stated] P |

**Author order caveat.** His surname sorts first. In all 10 multi-author DBLP records where he is listed first, the whole list is alphabetical (§1.4). First position therefore says nothing about who led those papers. [practice] P (S18), conclusion [inferred]

---

## 1. Publication landscape

### 1.1 Record coverage

- [observed, S] **DBLP** (S18, fetched 2026-11-08): 23 records, 2005–2025 (11 articles, 10 conference papers, 1 book = the thesis with ISBN 978-3-89963-892-9, 1 editorship = CPAIOR 2011). 22 carry a DOI; none carries an arXiv id. Coauthors with the most joint records: Koch 9, Berthold 9, Heinz 5. DBLP misses all ZIB-Reports, the 2003 UMTS chapter, *Teaching MIP Modeling and Solving* (2006), the 2009 AIChE J. paper, the 2010 *Hybrid Solving Techniques* chapter, the 2013 *Analyzing 12 Years of Progress* chapter and the 2014 RAMP paper.
- [observed, S] **Semantic Scholar** (S20): main author record 1793775 with 38 papers, 4,827 citations, h-index 20. Two split records exist: 2137115989 (MIPLIB 2003 report, *Hybrid Solving Techniques*, an INFORMS *Authors group* dataset entry) and 2091309794 (two Japanese ParaSCIP articles from 2013).
- [observed, S] **Crossref** (S19): a `query.author` search adds 4 DOIs beyond DBLP (AIChE J. 2009, Hybrid Optimization 2010, Facets 2013, an INFORMS bio dataset 10.1287/308b9ee6-…). Two more, OR/MS Today 2006 and the UMTS chapter of 2003, came from Semantic Scholar and were then checked by DOI on Crossref.
- [practice, P] **ZIB OPUS** (S14): 22 records with Achterberg as creator, found by OAI-PMH harvesting of MSC sets 90C11, 90C10, 90C57, 90C27, 90C05, 90C35, 65Y05, 90C59 and 90-XX, plus GetRecord scans of docIds 690–1111. Records outside those sets and ranges may be missed.
- [observed, S] **arXiv** (S23): one preprint, 2211.13545 (RLT cuts, 2022/2024). Before 2022 his preprint channel was the ZIB-Report series.
- [practice, P] **ORCID** (S15): sparse. One employment entry (Gurobi Optimization GmbH, from 2014-03) and two works (IJOC 2020, IPCO 2023). No biography, no homepage.
- **Homepage**: none (team.json). The thesis-era ZIB page was not searched for (the Wayback Machine was not used).

### 1.2 Verified works (every identifier checked with a tool on 2026-11-08)

Citation counts: Crossref `is-referenced-by-count` (C) and Semantic Scholar (SS), both as of 2026-11-08; a dash means no count. *Read* says how much of the work I read.

| # | Year | Work (authors in printed order) | Venue | Identifier | C / SS | Read |
|---|---|---|---|---|---|---|
| W1 | 2002 | *Branching on History Information* (Achterberg, Koch, Martin; the cover page lists only Achterberg and Koch) | ZIB-Report 02-32 | urn:nbn:de:0297-zib-6990 | — / 0 | full (S2) |
| W2 | 2003 | *Modelling Feasible Network Configurations for UMTS* (Eisenblätter, Wessäly, Martin, Fügenschuh, Wegel, Koch, Achterberg) | Operations Research/Computer Science Interfaces Series (book chapter), pp. 1–23 | 10.1007/978-1-4757-3762-2_1 | 13 / 69 | metadata |
| W3 | 2004 (journal 2005) | *Branching Rules Revisited* (Achterberg, Koch, Martin) | ZR 04-13; Operations Research Letters 33(1):42–54 | urn:nbn:de:0297-zib-7886; 10.1016/j.orl.2004.04.002 | 382 / 584 | ZR main text (S3) |
| W4 | 2004 | *SCIP – a framework to integrate Constraint and Mixed Integer Programming* (Achterberg) | ZIB-Report 04-19 | urn:nbn:de:0297-zib-7947 | — / 108 | pp. 1–3 (S4) |
| W5 | 2005 (journal 2007) | *Conflict Analysis in Mixed Integer Programming* (Achterberg) | ZR 05-19; Discrete Optimization 4(1):4–20 | urn:nbn:de:0297-zib-8537; 10.1016/j.disopt.2006.10.006 | 79 / 127 | ZR in part (S5); journal not read |
| W6 | 2005 (journal 2006) | *MIPLIB 2003* (Achterberg, Koch, Martin) | ZR 05-28; Operations Research Letters 34(4):361–372 | urn:nbn:de:0297-zib-8625; 10.1016/j.orl.2005.07.009 | 144 / 152 | ZR pp. 1–2 (S6) |
| W7 | 2005 (journal 2007) | *Improving the Feasibility Pump* (Achterberg, Berthold) | ZR 05-42; Discrete Optimization 4(1):77–86 | urn:nbn:de:0297-zib-8754; 10.1016/j.disopt.2006.10.004 | 137 / 159 | abstract |
| W8 | 2006 | *Teaching MIP Modeling and Solving* (Achterberg, Grötschel, Koch) | OR/MS Today 33(6), pp. 14–15 (pages per S1's bibliography) | 10.1287/orms.2006.06.06 | 0 / 3 | metadata |
| W9 | 2006 | *Software for Teaching Modeling of Integer Programming Problems* (Achterberg, Grötschel, Koch) | ZIB-Report 06-23 | urn:nbn:de:0297-zib-9176 | — / 0 | abstract |
| W10 | 2007 | *Constraint Integer Programming* (PhD thesis, TU Berlin; referees Grötschel and Bixby; defended 12 July 2007; revised 10 December 2008) | TU Berlin DepositOnce; ZIB OPUS 1018 and 1112 | 10.14279/depositonce-1634; urn:nbn:de:kobv:83-opus-16117; urn:nbn:de:0297-zib-11129 | — / 642 | in part (S1) |
| W11 | 2007 | *Property Checking with Constraint Integer Programming* (Achterberg, Brinkmann, Wedler) | ZIB-Report 07-37 | urn:nbn:de:0297-zib-10376 | — / 9 | abstract |
| W12 | 2008 | *Constraint Integer Programming: A New Approach to Integrate CP and MIP* (Achterberg, Berthold, Koch, Wolter) | CPAIOR 2008, LNCS, pp. 6–20 (ZR 08-01) | 10.1007/978-3-540-68155-7_4 | 104 / 216 | abstract |
| W13 | 2008 | *Counting Solutions of Integer Programs Using Unrestricted Subtree Detection* (Achterberg, Heinz, Koch) | CPAIOR 2008, pp. 278–282 (ZR 08-09) | 10.1007/978-3-540-68155-7_22 | 9 / 18 | abstract |
| W14 | 2008 | *On the Effects of Minor Changes in Model Formulations* (Achterberg, Koch, Tuchscherer) | ZIB-Report 08-29 | urn:nbn:de:0297-zib-10808 | — / 10 | pp. 1, 4, 7 (S7) |
| W15 | 2008 | *A Dynamic Load Balancing Mechanism for New ParaLEX* (Shinano, Achterberg, Fujie) | IEEE ICPADS 2008, pp. 455–462 | 10.1109/ICPADS.2008.75 | 6 / 14 | metadata |
| W16 | 2008 | *Constraint Integer Programming: Techniques and Applications* (Achterberg, Berthold, Heinz, Koch, Wolter) | ZIB-Report 08-43 | urn:nbn:de:0297-zib-10950 | — / 6 | abstract |
| W17 | 2009 | *SCIP: solving constraint integer programs* (Achterberg) | Mathematical Programming Computation 1(1):1–41 (online 20 January 2009) | 10.1007/s12532-008-0001-1 | 907 / 1,397 | abstract (S22); closed |
| W18 | 2009 | *Hybrid Branching* (Achterberg, Berthold) | CPAIOR 2009, LNCS 5547, pp. 309–311 | 10.1007/978-3-642-01929-6_23 | 56 / 111 | abstract |
| W19 | 2009 | *Computation of an extractive distillation column with affine arithmetic* (Baharev, Achterberg, Rév) | AIChE Journal 55(7):1695–1704 | 10.1002/aic.11777 | 17 / 20 | metadata |
| W20 | 2009 (journal 2010) | *The Mcf-separator: detecting and exploiting multi-commodity flow structures in MIPs* (Achterberg, Raack) | ZR 09-38; Mathematical Programming Computation 2(2):125–165 | urn:nbn:de:0297-zib-11592; 10.1007/s12532-010-0015-3 | 31 / 36 | abstract |
| W21 | 2010 | *Hybrid Solving Techniques* (Achterberg, Lodi) | in *Hybrid Optimization* (Springer Optimization and Its Applications), pp. 169–190 | 10.1007/978-1-4419-1644-0_5 | 0 / 1 | abstract |
| W22 | 2010 (book 2011) | *ParaSCIP: A Parallel Extension of SCIP* (Shinano, Achterberg, Berthold, Heinz, Koch) | Competence in High Performance Computing 2010, pp. 135–148 (ZR 10-27) | 10.1007/978-3-642-24025-6_12 | 23 / 81 | abstract |
| W23 | 2011 | *MIPLIB 2010* (Koch, Achterberg, Andersen, Bastert, Berthold, Bixby, Danna, Gamrath, Gleixner, Heinz, Lodi, Mittelmann, Ralphs, Salvagnin, Steffy, Wolter) | Mathematical Programming Computation 3(2):103–163 | 10.1007/s12532-011-0025-9; urn:nbn:de:0297-zib-12953 | 299 / 128+64 | metadata |
| W24 | 2011 | CPAIOR 2011 proceedings, LNCS 6697 (editors Achterberg, Beck) | Springer | 10.1007/978-3-642-21311-3 | — | metadata |
| W25 | 2011 (book 2012) | *Rounding and Propagation Heuristics for Mixed Integer Programming* (Achterberg, Berthold, Hendel) | Operations Research Proceedings 2011, pp. 71–76 (ZR 11-29) | 10.1007/978-3-642-29210-1_12 | 33 / 63 | abstract |
| W26 | 2013 | *Stronger Inference through Implied Literals from Conflicts and Knapsack Covers* (Achterberg, Sabharwal, Samulowitz) | CPAIOR 2013, pp. 1–11 | 10.1007/978-3-642-38171-3_1 | 2 / 5 | metadata |
| W27 | 2013 | *Mixed Integer Programming: Analyzing 12 Years of Progress* (Achterberg, Wunderling) | in *Facets of Combinatorial Optimization* (Springer), pp. 449–481 | 10.1007/978-3-642-38189-8_18 | 148 / 260 | abstract (S22); closed |
| W28 | 2013 | Japanese article on parallelising SCIP (Shinano, Achterberg, Berthold, Heinz, Koch, Vigerske, Winkler) | ZIB OPUS 1813 (journal venue not checked) | urn:nbn:de:0297-zib-18130 | — / 0 | metadata |
| W29 | 2014 | *Solving Hard MIPLIB2003 Problems with ParaSCIP on Supercomputers: An Update* (Shinano, Achterberg, Berthold, Heinz, Koch, Winkler) | IPDPS Workshops 2014, pp. 1552–1561 (ZR 13-66) | 10.1109/IPDPSW.2014.174 | 7 / 16 | abstract |
| W30 | 2014 | *Multi-Row Presolve Reductions in Mixed Integer Programming* (Achterberg, Bixby, Gu, Rothberg, Weninger) | Proceedings of the Twenty-Sixth RAMP Symposium, Hosei University, Tokyo, 16–17 October 2014, pp. 181–196 | venue + year + title (open PDF on orsj.org) | — / 10 | in part (S9) |
| W31 | 2016 | *Solving Open MIP Instances with ParaSCIP on Supercomputers Using up to 80,000 Cores* (Shinano, Achterberg, Berthold, Heinz, Koch, Winkler) | IPDPS 2016, pp. 770–779 (ZR 15-53) | 10.1109/IPDPS.2016.56 | 26 / 45 | abstract |
| W32 | 2016 (journal 2020) | *Presolve Reductions in Mixed Integer Programming* (Achterberg, Bixby, Gu, Rothberg, Weninger) | ZR 16-44; INFORMS Journal on Computing 32(2):473–506 | urn:nbn:de:0297-zib-60370; 10.1287/ijoc.2018.0857 | 138 / 196 | ZR in part (S8) |
| W33 | 2021 | *An Exact Method for the Minimum Feedback Arc Set Problem* (Baharev, Schichl, Neumaier, Achterberg) | ACM Journal of Experimental Algorithmics 26, 1.4:1–28 | 10.1145/3446429 | 27 / 42 | metadata |
| W34 | 2021 | *MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library* (Gleixner, Hendel, Gamrath, Achterberg, Bastubbe, Berthold, Christophel, Jarck, Koch, Linderoth, Lübbecke, Mittelmann, Özyurt, Ralphs, Salvagnin, Shinano) | Mathematical Programming Computation 13(3):443–490 | 10.1007/s12532-020-00194-3 | 182 / 347 | metadata |
| W35 | 2023 | *Efficient Separation of RLT Cuts for Implicit and Explicit Bilinear Products* (Bestuzheva, Gleixner, Achterberg) | IPCO 2023, LNCS, pp. 14–28 | 10.1007/978-3-031-32726-1_2 | 2 / 3 | metadata |
| W36 | 2022–2025 | *Efficient separation of RLT cuts for implicit and explicit bilinear terms* (Bestuzheva, Gleixner, Achterberg) | Mathematical Programming 210(1):47–74 (2025; online 16 July 2024) | 10.1007/s10107-024-02104-0; arXiv 2211.13545 | 2 / 4 | metadata |
| T1 | 2022 | Invited talk *Combinatorial Algorithms Used Inside a MIP Solver*, SEA 2022, Heidelberg, 26 July 2022 | slides on the SEA 2022 site | sea2022.ifi.uni-heidelberg.de/talk_achterberg.pdf | — | in part (S10) |
| T2 | 2025 | Talk *From Infeasibility to Feasibility – Improvement Heuristics to Find First Feasibles for MIPs*, MIP Workshop 2025, University of Minnesota, 4 June 2025 | slides on mixedinteger.org | mixedinteger.org/2025/ | — | in part (S11, S12) |

Further records that I verified only through one database (they are listed but not used as evidence): a 2020 ZIB-Report *Solving Previously Unsolved MIP Instances with ParaSCIP on Supercomputers by using up to 80,000 Cores* (Semantic Scholar record, cited as ZIB TR 20-16 in S28; OPUS record not checked).

### 1.3 Topics by five-year period, with era and resource context

| Period | Position and resources | Topics (works) | Tag |
|---|---|---|---|
| 2000–2004 | Student and then researcher at ZIB under Grötschel. Before SCIP: Martin's SIP source code, with CPLEX as the embedded LP solver; DEC Alpha 21264 workstations (750 MHz in 2002, 833 MHz in 2004, 2 GB) | Mathematics diploma (2000): polyhedral study of the arborescence flow problem from IP routing, with self-built instances that he says became MIPLIB's aflow30a and aflow40b (S29 0:21:30–0:23:00); computer-science diploma about a year later: learning branching rules from node features with machine learning inside SIP (S1 p. ix; S29 0:23:00–0:26:00); both titles not found; UMTS network configuration models (W2); history branching in SIP (W1); reliability branching (W3); the SCIP framework design (W4, started October 2002 per S1, 2001 per S29; see C13) | [stated] P (S1 pp. ix, 6; S29 captions); [practice] P (S2 p. 10; S3 p. 8) |
| 2005–2009 | ZIB, then ILOG CPLEX R&D from 2006 while finishing the thesis (S1 p. ix calls ILOG his new employer, May 2007). Thesis benchmarks on eight identical Pentium 4 desktops (3.8 GHz, 2 GB) using colleagues' spare cycles, more than one CPU year in total | SAT-style conflict analysis (W5); MIPLIB 2003 (W6); feasibility pump objective variant with Berthold (W7); teaching software (W8, W9); thesis (W10) and the chip-design property-checking application with OneSpin/Infineon partners (W11); the CIP paradigm (W12, W16, W17); counting all solutions (W13); performance erraticism under minor reformulations (W14); parallel search (W15); hybrid branching (W18); interval methods for a chemical-engineering model (W19); Mcf separator, implemented in both SCIP and CPLEX (W20) | [practice] P (S1 pp. x, 319); [stated] P |
| 2010–2014 | CPLEX lead MIP developer for 12.0–12.6 (S16); output mostly co-authored with ZIB colleagues | Hybrid CP/OR solving survey with Lodi (W21); ParaSCIP (W22, W28, W29); MIPLIB 2010 (W23); CPAIOR 2011 co-editor (W24); cheap rounding and propagation heuristics and the primal integral measure (W25); implied literals with IBM Research authors (W26); CPLEX 8.0→12.5 progress measurement (W27); Gurobi multi-row presolve (W30) | [practice] P/S |
| 2015–2019 | Gurobi senior developer. Benchmarks on 4-core Intel i7-3770K, 32 GB, with Gurobi's internal model library (2,974 models in 2014, 3,182 in 2016) | ParaSCIP on up to 80,000 cores of the Titan supercomputer (W31); Gurobi presolve taxonomy (W32) | [practice] P (S8 p. 2; S9 p. 190) |
| 2020–2026 | Gurobi VP of R&D (April 2020). Talk benchmarks: Gurobi 9.5.0 on 2,397 LP and 7,030 MIP models (2022), 8,611 MIP models (2025); 4-core Xeon E3-1240, 32 GB, 10,000 s limit. In 2023 he describes a 192-machine benchmark cluster running around the clock, a test set of about 6,000 instances run with five random seeds in about 12 hours, and estimates that research is about 10 % of the development time, the rest being design, bug fixing, benchmarking and tuning (S29 0:52:00–0:53:00, 1:05:00–1:05:30) | IJOC presolve paper in print (W32); feedback arc set exact method with Vienna coauthors (W33); MIPLIB 2017 (W34); RLT cut separation for bilinear terms with ZIB coauthors (W35, W36); combinatorial sub-algorithms inside a MIP solver (T1); improvement heuristics started from infeasible vectors (T2); the 2023 *Subject to* interview (S29) | [practice] P (S10 slide 5; S11 slides 25–26); [stated] P (S29) |

### 1.4 First-author to last-author shift

- [practice, P] Of the 23 DBLP records (S18), he is the sole author of 3 (thesis, DO 2007, MPC 2009) and listed first in 10 more (W3, W6, W7, W12, W13, W18, W20, W25, W26, W32). All 10 of those lists are alphabetical. The CPAIOR 2011 editor list (Achterberg, Beck) is alphabetical too.
- [practice, P] The non-alphabetical lists put him later: ParaLEX/ParaSCIP (Shinano first; W15, W22, W29, W31), MIPLIB 2010 (Koch first, then alphabetical; W23), MIPLIB 2017 (Gleixner, Hendel, Gamrath, then alphabetical; W34), AIChE 2009 (Baharev first, then alphabetical; W19), and in the three most recent papers he is last: JEA 2021 (W33), IPCO 2023 and Math. Prog. 2025 (W35, W36).
- [inferred] There is no first-author to last-author shift that author order can show: the ZIB- and company-era convention is alphabetical. What the record shows instead is (a) sole-author works only in the thesis period (2004–2009); (b) from 2021, a last position behind academic first authors (Baharev; Bestuzheva with Gleixner). That is consistent with an industry senior-collaborator role, but no source states his role on those papers.

### 1.5 Collaboration network and likely students

- [practice, P] Core ZIB circle 2002–2016: Thorsten Koch (W1, W3, W6, W8, W9, W12–W14, W16, W22, W23, W29, W31), Alexander Martin (W1, W3, W6), Timo Berthold (W7, W12, W16, W18, W22, W25, W29, W31), Stefan Heinz (W13, W16, W22, W29, W31), Kati Wolter (W12, W16, W23), Christian Raack (W20), Gregor Hendel (W25, W34), Yuji Shinano (W15, W22, W28, W29, W31), Michael Winkler (W28, W29, W31).
- [practice, P] Industry and application partners: Raik Brinkmann (chip verification, Infineon/OneSpin) and Markus Wedler (TU Kaiserslautern) on W11. S1 p. ix says the industry contact supplied test data early enough to be useful within the project.
- [practice, P] CPLEX era: Roland Wunderling (W27); Ashish Sabharwal and Horst Samulowitz (W26); Andrea Lodi (W21). Gurobi era: Robert E. Bixby, Zonghao Gu, Edward Rothberg, Dieter Weninger of Erlangen (W30, W32); Ali Baharev, Hermann Schichl and Arnold Neumaier of Vienna (W19, W33); Ksenia Bestuzheva and Ambros Gleixner of ZIB (W35, W36). Library consortia W23 and W34 span solver vendors and academia.
- [stated, P] Students: S1 p. x refers to Kati Wolter and Timo Berthold as his students. Their diploma theses (TU Berlin 2006) are cited as the detailed sources for SCIP's cuts and heuristics (S1 pp. 3–4).
- [observed, S] The Mathematics Genealogy Project lists Grötschel as his advisor and no known students (S25). Supervision of Hendel, Bestuzheva or others: not verified.

### 1.6 Usual venues and preprint channel

- [practice, P] Preprints: the ZIB-Report series (W1, W3–W7, W9, W11–W14, W16, W20, W22, W25, W29, W31, W32: 18 reports found, 2002–2016); the first arXiv preprint appears in 2022 (W36).
- [practice, P] Journals: Mathematical Programming Computation (W17 is the first article of volume 1, issue 1; W20, W23, W34), Operations Research Letters (W3, W6), Discrete Optimization (W5, W7: both in the 2007 special issue on mixed integer programming), INFORMS J. Computing (W32), Mathematical Programming (W36), ACM JEA (W33), AIChE J. (W19).
- [practice, P] Conferences: CPAIOR is the most frequent (W12, W13, W18, W26, plus the 2011 co-editorship); IPCO 2023 (W35); parallel computing venues (ICPADS 2008, IPDPS/IPDPSW 2014, 2016); RAMP 2014; SEA 2022 (invited); MIP Workshop 2025.

### 1.7 Most-cited works (2026-11-08)

| Rank (Crossref) | Work | Crossref | Semantic Scholar |
|---|---|---|---|
| 1 | W17 SCIP (MPC 2009) | 907 | 1,397 |
| 2 | W3 Branching rules revisited (ORL 2005) | 382 | 584 |
| 3 | W23 MIPLIB 2010 | 299 | 128 + 64 (split records) |
| 4 | W34 MIPLIB 2017 | 182 | 347 |
| 5 | W27 Analyzing 12 years of progress | 148 | 260 |
| 6 | W6 MIPLIB 2003 | 144 | 152 |
| 7 | W32 Presolve reductions (IJOC 2020) | 138 | 196 |
| 8 | W7 Improving the feasibility pump | 137 | 159 |
| 9 | W12 CIP, CPAIOR 2008 | 104 | 216 |
| 10 | W5 Conflict analysis (DO 2007) | 79 | 127 (16 influential) |
| — | W10 thesis (DataCite DOI, no Crossref count) | — | 642 |

[observed, S] (S19, S20). Google Scholar and OpenAlex counts: not available (see header).

### 1.8 Recent works (2021–2026)

- [practice, P] W33 (JEA 2021), W34 (MPC 2021), W35/W36 (IPCO 2023; Math. Prog. 2025, arXiv last revised 19 July 2024).
- [stated, P] T1 (SEA 2022, S10): a talk on the combinatorial sub-problems inside a MIP solver (median, DFS, shortest path, min-cut/max-flow, vertex separators, max clique, dynamic programming, graph automorphism, union-find). Slides 20–21: polynomial is not fast enough at scale, since even quadratic loops are too slow on big models. He calls quadratic loops one of the most frequent performance bugs they fix, asks for safeguards against corner cases, and says that exponential worst-case bounds say nothing about practical instances. Slide 26: all algorithms are implemented in C, on the solver's own data structures. Every slide carries a Gurobi copyright footer marked confidential, although the conference posted the deck publicly.
- [stated, P] T2 (MIP Workshop 2025, S11, S12): improvement heuristics (RINS and other LNS) normally need a feasible start. The talk feeds them infeasible integral vectors instead, which the abstract describes as similar in spirit to the feasibility pump. Slides 25–26 measure it on 8,611 models (102 dropped for inconsistent answers or failures; 2,861 dropped as unsolved by every version; the speed-up is taken on the >100 s bracket with 1,658 models), with ablations of no heuristics, no RINS and no infeasible solutions, and metrics for first feasible, 10 % gap, 1 % gap and optimality.
- [stated, P] *Subject to: Tobias Achterberg*, a long-form YouTube interview uploaded 2023-08-17 (S29; title and channel confirmed by YouTube oEmbed). Read only as caption excerpts; it supplies the origin stories used in SW1–SW4 and the 2023 resource figures in §1.3.
- [practice, P] No 2026 work was found in DBLP, Crossref, Semantic Scholar, arXiv or the MIP 2026 workshop page (S12's sibling page, fetched 2026-11-08).

### 1.9 Reception markers

- [observed, S] MOS Beale–Orchard-Hays Prize 2009, winner (S26; jury Andersen, Gill, Linderoth, Sahinidis as chair). The MOS list does not name the honoured work. He sat on the 2018 jury (S26).
- [observed, S] INFORMS: 2008 George B. Dantzig Dissertation Award, second place, for *Constraint Integer Programming*; 2011 INFORMS Optimization Society Young Researchers Prize for W17 (S27). The 2011 committee (Bienstock, Boros, McCormick, Renegar as chair) praised the paper, in paraphrase, for showing both the overview and the details, for documenting extensive tests against other packages, and for the chip-verification example (S27).
- [observed, S] Gurobi's 2014 press release calls SCIP generally regarded as the best academic MIP code (S16; promotional). S28 (Koch, Berthold, Pedersen, Vanaret 2022) cites W27 as the CPLEX 8.0→12.5 progress study and his thesis, W5 and W20 as algorithmic references.

---

## 2. Signature works (framework §五)

Selection: the two most-cited works (W17 with its thesis W10; W3), the work he tells an origin story about (W5), and the turning point into commercial-code publishing (W32 with W30). W27 is added as a partial fifth, because it carries the measurement method, but its full text was not read. No source was found in which he ranks his own works; the importance he gives each work is read from the space and story he gives each topic in the thesis acknowledgements and introduction (S1 pp. ix–x, 1–6) and in the 2023 interview, which tells origin stories for SCIP, reliability branching and conflict analysis (S29). [inferred]

### SW1. Constraint integer programming and SCIP (thesis W10, 2007; MPC paper W17, 2009; first report W4, 2004)

| Dimension | Finding | Tag |
|---|---|---|
| Origin | Work began in 2000 with his computer-science diploma thesis on learning branching strategies with neural networks, which needed the source of a state-of-the-art MIP solver; Martin made SIP available, and he learned by analysing its algorithms with Koch. Having studied both mathematics and computer science, in 2002 he looked for a topic joining them and chose integrating integer and constraint programming. SIP could not host that integration, so at the end of 2002 he started from scratch and named the new code SCIP to mark its relation to SIP (S1 p. ix). Development started in October 2002, with most SIP ideas carried over (S1 p. 6). In 2023 he adds that CP looked to him like MIP seen from another viewpoint, that SIP's data structures put the LP relaxation at the centre so tightly that general constraints did not fit, and that he did not then know John Hooker was pursuing the same idea (S29 0:26:30–0:27:30) | [stated] P |
| Why then | Grötschel gave him the freedom to build the code first: "For almost two years, I did not publish a single paper!" (S1 p. ix). Grötschel's contacts then brought the Valse-XT chip-verification project with Wolfram Büttner's group at Infineon (later OneSpin Solutions), which he calls the right project at the right moment (S1 p. ix). Contemporary SAT techniques (conflict learning, watched literals) were ready to borrow (S1 p. x). Mittelmann's benchmark pages gave SCIP public visibility (S1 p. x) | [stated] P; the ready-to-borrow reading [inferred] from the SAT references S1 pp. 165–166 |
| Key insight | Generalise MIP to any constraint that becomes linear in the continuous variables once all integer variables are fixed, and let CP, SAT and MIP techniques work on one search tree at a low level, sharing statistics and LP dual information (S1 abstract and pp. 1–2). The 2004 report pitched the framework at experts who want full control of the solve and high performance, not at easy prototyping (S4 abstract, p. 2) | [stated] P |
| Minimum evidence | Two demonstrations: (a) as a pure MIP solver, SCIP 0.90i is on average 63 % slower than CPLEX 10 (S1 p. 6, Appendix C); (b) on chip-design property checking, the CIP approach can be several orders of magnitude faster than the SAT approach, depending on circuit and property, although SAT finds counter-examples faster (S1 p. 6). An early sign: on infeasible ALU verification IPs, conflict analysis in SCIP 0.79a cut nodes by 90 % and time by 60 % (S5 abstract, 2005). Example of why CP handling matters: a reasonable LP relaxation of one 64-bit shift-left constraint needs 2,145 auxiliary variables, 6,306 constraints and 16,834 non-zeros (S1 p. 5) | [practice] P |
| Scale of evidence | 244 instances × 115 parameter settings = 28,060 runs, more than one CPU year (S1 p. 2); 575 public instances filtered to 244 by a stated procedure that uses CPLEX 10.0.1 and SCIP 0.82d (S1 p. 320); 1 h limit for MIP and 2 h for chip runs, 1.5 GB memory limit (180 of 28,060 runs hit it), timeouts counted at the limit, timing noise up to 2 % (S1 p. 319) | [practice] P |
| Abandoned paths | SIP as the platform (dropped in 2002 because the integration was beyond its scope, S1 p. ix). Thorsten Koch had to convince him that writing up mattered more than another 10 % speed-up (S1 p. x); I read this as a pull towards continual tuning over writing up. A missed path: he learned only later, at a conference, that Hooker had a similar framework, and regrets that they did not collaborate directly; he calls not knowing the literature a weakness of his, prefers building from scratch, and finds the literature part of a paper the hardest to write (S29 1:20:30–1:22:00). No abandoned SCIP design was found in the parts read | [stated] P; the pull [inferred]; none found for design |
| Reception | Dantzig Dissertation Award second place 2008; BOH Prize 2009 (work not named); 2011 INFORMS OS Young Researchers Prize for W17 (S26, S27). W17 opens MPC volume 1 (S19). Most cited of his works (907 Crossref / 1,397 SS). By 2007 the thesis cites 15 references to other projects already using SCIP (S1 p. 6) | [observed] S; [stated] P |
| Method it shows | Build the complete research platform before the research; transfer techniques across fields (CP/SAT→MIP) at the level of shared data structures; use an application with an industrial partner as the stress test; evaluate every component by switching it off over a broad test set | cross-index: threads A, B, E, G in §5 |

### SW2. Reliability branching: *Branching Rules Revisited* (W3, ZR 2004 / ORL 2005), and its precursor *Branching on History Information* (W1, 2002)

| Dimension | Finding | Tag |
|---|---|---|
| Origin | Thread from the computer-science diploma thesis on learning branching strategies (S1 p. ix). In 2023 he tells it this way: inside SIP, with Koch, he extracted features at each node and trained several learners (support vector machines, neural networks, radial basis functions and others) to predict the objective change of a branching; the learners ended up pointing to one feature only, a pseudocost-like quantity of his own that he called the history value; that feature, not the learning, became *Branching Rules Revisited* (S29 0:23:30–0:26:00). The first public step is *history branching* in SIP (W1, October 2002): history values that mix pseudocosts and strong-branching estimates, with dynamic scaling factors, a three-level fallback (variable, variable class, global), and strong branching repeated on variables whose history counts are still low, which the report already calls unreliable (S2 pp. 6–8). The ZR 04-13 / ORL 2005 paper then presents *reliability branching* as a generalisation of strong and pseudocost branching, still implemented in SIP (S3 abstract, p. 12) | [stated] P; [practice] P |
| Why then | Strong branching was standard in CPLEX, and the CPLEX API exposed `CPXstrongbranch()`, which the 2004 runs used (S3 p. 8). Linderoth and Savelsbergh's study of pseudocost initialisation was the baseline to beat (S2 p. 5) | [practice] P; why-then [inferred] |
| Key insight | Call a variable's pseudocosts unreliable until both directions have been observed η_rel times; for unreliable candidates, taken in order of pseudocost score and stopped by a lookahead λ, run limited strong branching. One parameter nests the old rules: η_rel = 0 is pseudocost branching, 1 is pseudocost with strong-branching initialisation, ∞ is strong branching (S3 §2.6–2.7; S1 pp. 65–66). In SCIP, η_rel (default 8) is adjusted so that strong-branching simplex iterations stay below half the node-LP iterations plus 100,000 (S1 pp. 65–66) | [stated, joint] P |
| Minimum evidence | 2002: on 22 MIPLIB 3.0 instances, history branching in SIP needed 3,533.5 s in total against 12,966.7 s for hybrid pseudocost branching and 12,342.1 s for CPLEX 7.5 (S2 p. 10, Table 2). To explain the gain, at each node he solved all candidates' children and measured how close the chosen variable's score and rank came to full strong branching (score and position quotients, S2 pp. 12–13). 2004: the setting η_rel = 8, λ = 4 is singled out as the best nodes-versus-time trade-off (S3 p. 12) | [practice] P |
| Abandoned paths | (0) The machine-learning route itself: he calls the learning result disappointing and kept only the feature it singled out (S29 0:25:00–0:26:00). (a) The history-branching machinery (variable classes grouped by model names, with a planned link to Zimpl; exponentially forgetting scaling factors with τ_max = 0.995; a global history value; no updates after node preprocessing or cuts; S2 pp. 7–8) does not appear in reliability branching. ZR 04-13 never mentions history branching, and the thesis does not cite W1 (S3; S1 bibliography). Why it was dropped: no source; [inferred] the simpler rule kept the gain. (b) Experimental control: in 2002 the optimal solution was supplied in advance and root cuts fixed, to isolate branching (S2 pp. 10–11); in 2004 they deliberately did not supply the optimum, arguing that a branching rule should also find good solutions fast, and used cut-and-branch instead (S3 p. 8). (c) Test-set rule: in 2002 the set was conditioned on the new rule solving the instance within 3,600 s (S2 p. 9); in 2004, only on CPLEX 9.0 needing at least 5,000 nodes and at most one hour (S3 p. 8). (d) Negative result kept: most infeasible branching is about as good as random branching (S3 p. 9; S1 pp. 3, 62) | [practice] P; motives [inferred] |
| Reception | 382 Crossref / 584 SS citations. Becomes SCIP's default branching basis and is extended to hybrid reliability/inference branching (S1 pp. 66–67; W18 with Berthold, 2009). The 2004 conclusion names an open gap to full strong branching's node counts (S3 p. 12). Adding reliability branching to CPLEX was his first project there (S29 0:40:00–0:40:30). In 2023 he says that in his experience plain pseudocost branching is what works best in the end; the caption excerpt stops before he explains this (S29 0:53:30; see C15) | [observed] S; [stated, joint] P; [stated] P |
| Method it shows | Treat the expensive rule (full strong branching) as the oracle and measure how closely a cheap rule tracks it; build a parameter family that contains the existing rules; let effort adapt to a budget; judge on geometric means over a test set, not on single instances (S3 p. 9) | threads B, C, D |

### SW3. *Conflict Analysis in Mixed Integer Programming* (W5: ZR 05-19, 2005; Discrete Optimization 2007; thesis ch. 11)

| Dimension | Finding | Tag |
|---|---|---|
| Origin | During the Valse-XT project, the SAT researcher Yakov Novikov explained conflict analysis and the two-watched-literals scheme to him in about ten minutes on a subway ride; within days he put watched literals into SCIP's set-covering constraint handler, and the generalisation of conflict analysis to MIP followed after three weeks; conflict analysis then proved a key ingredient for chip verification (S1 p. x). The May 2004 SCIP report already lists conflict analysis among SCIP's features (S4 p. 3), so the transfer happened before mid-2004 | [stated] P; dating [practice] P |
| Why then | SAT conflict learning was mature (Marques-Silva and Sakallah; Goldberg and Novikov's BerkMin, both cited in S5). The chip-verification IPs are infeasible, so proving infeasibility, where learning pays most, was the task (S5 p. 15). Owning SCIP gave access to the LP duals and the propagation history | [practice] P; why-then [inferred] |
| Key insight | An infeasible or bound-exceeding node LP can be explained by a small subset of local bound changes found from dual information; that subset seeds a SAT-style conflict graph, from which conflict constraints are cut. Non-binary variables are handled with bound-disjunction constraints (S1 pp. 5, 165–166; S5 pp. 1–2) | [stated] P |
| Minimum evidence | 2005, SCIP 0.79a on a Pentium-4EE 3.2 GHz: ALU verification instances, nodes −90 % and time −60 %; but on feasible MIPs (MIPLIB 2003 and Mittelmann instances where CPLEX 9.03 needs at least 1,000 nodes and 30 s), nodes −50 % while time rose 15 % in geometric mean; the abstract reports the slowdown openly (S5 abstract, pp. 14–15) | [practice] P |
| Abandoned paths | (a) In 2005 conflict clauses were added on demand to the LP relaxations at local nodes (S5 p. 14). The thesis default does not separate conflict constraints as cuts at all and uses them only for domain propagation, with at most 10 conflict constraints per infeasible subproblem and an aging rule to delete useless ones (S1 pp. 178–179). (b) Variants measured and not adopted: analysing bound-exceeding LPs cuts nodes but not runtime; strong-branching LP analysis makes runtime slightly worse; the aggressive full setting raises runtime on almost all test sets (S1 pp. 180–181). (c) A CPLEX API limit: `CPXstrongbranch()` returns no dual information, so strong-branching LPs had to be re-solved before analysis (S1 pp. 180–181) | [practice] P |
| Reception | 79 Crossref / 127 SS (16 of them counted as influential by Semantic Scholar). The thesis records that Sandholm and Shields developed the same generalisation independently (CMU-CS-06-155, September 2006; S1 p. 165). The final thesis result is a performance gain of more than 10 % with a reasonable analysis effort (S1 p. 5). In his 2023 account, a conflict-analysis talk squeezed into the 2005 MIP workshop programme in Minneapolis (including a comparison of SCIP with CPLEX 9.0) led ILOG people in the audience to approach him; after competing offers from ILOG and Dash Optimization he joined ILOG in September or October 2006, and conflict analysis was his second CPLEX project (S29 0:35:30–0:38:30, 0:40:30) | [stated] P; [observed] S |
| Method it shows | Cross-field transfer triggered by a conversation; report the net slowdown in the abstract; then tune the effort (what to analyse, how many constraints, how long to keep them) until node savings turn into time savings | threads E, F, D |

### SW4. *Presolve Reductions in Mixed Integer Programming* (W32: ZR 16-44, 2016; IJOC 2020), with *Multi-Row Presolve Reductions* (W30, RAMP 2014)

| Dimension | Finding | Tag |
|---|---|---|
| Origin | No primary account of the origin was found. The paper's stated motive is that the number of presolve publications is surprisingly small given the topic's importance (S8 p. 2, paraphrase). The 2016 work was supported by the Research Campus MODAL (BMBF grant 05M14ZAM), and Weninger (Erlangen) is the academic coauthor (S8 p. 1) | [stated, joint] P; origin not found |
| Why then | He joined Gurobi in March 2014 (S15); the RAMP 2014 paper (October 2014) is the first Gurobi-era publication, describing Gurobi 5.6.3; the 2016 report extends it to Gurobi 6.5 (S9 p. 190; S8 p. 2). In 2023 he calls presolve the most enjoyable part of the solver to work on, because an idea that shrinks the problem usually pays off in performance, while new cuts or branching rules often look good and still lose (S29 0:41:30–0:42:00) | [practice] P; [inferred] link to the move; [stated] P (2023 view) |
| Key insight | A complete taxonomy of Gurobi's presolve: more than thirty techniques in six classes, each with an ablation (S8 p. 64) | [stated, joint] P |
| Minimum evidence | Turning presolve off in Gurobi 6.5: 504 models need presolve to finish within 3,600 s, and the shifted-geometric-mean time in the ≥10 s bracket rises about ninefold, in line with the factor 11.4 that W27 measured for CPLEX (S8 pp. 3–4). RAMP 2014 (Gurobi 5.6.3, 2,974 models, 10,000 s): 289 models need presolve (S9 pp. 190–191) | [practice] P |
| Abandoned paths and negative results | Chvátal-Gomory strengthening affects many models but brings no gain in solved models or speed, yet stays on by default (S8 p. 12); simple probing on single equations finds reductions on about 20 % of models with no performance gain (S8 p. 16); SOS reductions show 25 % on 48 affected models, a set the authors call too small to conclude from (S8 p. 17); coefficient lifting is restricted because the added non-zeros hurt LP speed and stability (S8 p. 51); global probing at local nodes is performance neutral (S8 p. 63) | [practice] P; [stated, joint] P |
| Reception | 138 Crossref / 196 SS. Print came about 3.3 years after the ZIB-Report (December 2016 → April 2020); the DOI suffix 2018.0857 suggests a 2018 submission | [observed] S; the submission year [inferred] from the DOI |
| Method it shows | The bracket protocol: brackets of models by solve time (≥0, 1, 10, 100, 1,000 s); affected models, judged by a changed simplex-iteration count; counts of models at least 10 % faster or slower; time-limit hits; ratios of shifted geometric means with a shift of 1. Each feature is disabled in the source code for the master solve only, keeping it in sub-MIPs so heuristics are not changed implicitly, and models where the two versions disagree on the optimum are excluded (S8 pp. 2–4; S9 pp. 190–191). The same protocol reappears in the 2025 talk (S11 slides 25–26) | threads B, F, H |

### SW5 (partial). *Mixed Integer Programming: Analyzing 12 Years of Progress* (W27, with Roland Wunderling, 2013)

| Dimension | Finding | Tag |
|---|---|---|
| Origin | The abstract frames it as an update of Bixby et al.'s 2001 CPLEX study for Grötschel's 65th-birthday Festschrift (S22) | [stated, joint] P (abstract) |
| Key insight | The abstract promises an unbiased way to analyse benchmark results, applied to the contribution of CPLEX 12.5's main components, with emphasis on the deterministic parallel optimizer (S22) | [stated, joint] P (abstract) |
| Minimum evidence | As reported by S28: 2,928 MILP models; CPLEX 8.0→12.5 geometric-mean speed-up 4.71, up to 78.6 on models hard for 8.0; 732 vs 87 timeouts at 10,000 s | [observed] S |
| Method | W32 states that its tables follow W27's form and points to W27's Section 2 on minimum test-set size (S8 pp. 3, 17), so the bracket protocol of SW4 probably originates here | [inferred] from S8 |
| Not read | Full text (closed, S24). Abandoned paths and reception beyond citations: unknown | gap |

---

## 3. Failures, abandoned directions and negative results (consolidated)

| # | Item | Evidence | Tag |
|---|---|---|---|
| F1 | History branching (2002) dropped by name and in most of its machinery by 2004 | S2 pp. 6–8; S3 (no mention); S1 bibliography | [practice] P; why [inferred] |
| F2 | Conflict analysis first made feasible-MIP solving 15 % slower (2005) | S5 abstract, p. 15 | [practice] P |
| F3 | Conflict constraints as LP cuts (2005) replaced by propagation-only use (thesis) | S5 p. 14; S1 p. 179 | [practice] P |
| F4 | Aggressive conflict-analysis variants slower; bound-exceeding-LP analysis no runtime gain | S1 pp. 180–181 | [practice] P |
| F5 | Most infeasible branching ≈ random | S3 p. 9; S1 p. 3 | [practice] P |
| F6 | Primal heuristics contribute only 14 % to time-to-optimality in SCIP 0.90 | S1 p. 4 | [practice] P |
| F7 | Simple cut-selection rules (all cuts; one cut per round) cost 70 % and 80 % runtime | S1 p. 4 | [practice] P |
| F8 | Several Gurobi presolve reductions neutral or disappointing (CG strengthening, single-equation probing, node global probing) | S8 pp. 12, 16, 63 | [practice] P |
| F9 | Minor model changes alter MIP solve time by more than a factor of 1,000; omitting seemingly useful redundant information can help (found while trying to reproduce van Vyve and Wolsey's TSP results) | S7 pp. 1, 7 | [practice] P; [stated, joint] P |
| F10 | MIPLIB 2003 promised yearly updates; the next library was MIPLIB 2010 | S6 p. 1; W23 | [stated, joint] P; outcome [practice] |
| F11 | Writing was postponed for performance tuning until Koch intervened; the thesis came after the self-imposed deadline | S1 p. x | [stated] P |
| F12 | Rejected papers or retracted claims: none found | — | gap |
| F13 | Machine-learned branching (computer-science diploma, about 2001) gave way to the single hand-made feature it singled out; in 2023 he describes using machine learning at Gurobi in the same spirit, to find an explainable rule (for example, decision trees for whether to dualize an LP and which simplex to use) that is then implemented directly | S29 0:25:00–0:26:00, 1:16:00–1:17:30 | [stated] P |

---

## 4. Era and resource context (by work)

| Year | Hardware and software | Test sets and limits | Source |
|---|---|---|---|
| 2002 | Alpha 21264 750 MHz, 2 GB; SIP + CPLEX LP; CPLEX 7.5 as reference | MIPLIB 3.0 subset (22), 3,600 s | S2 pp. 9–10 |
| 2004 | Alpha 21264 833 MHz, 4 MB cache, 2 GB; SIP + CPLEX 9.0 LP | MIPLIB 2003 + collected instances, 3,600 s | S3 p. 8 |
| 2005 | Pentium-4EE 3.2 GHz, 2 GB; SCIP 0.79a + CPLEX LP; CPLEX 9.03 as reference | MIPLIB 2003 + Mittelmann instances; ALU verification IPs at tolerance 10^-9 | S5 pp. 14–15 |
| 2007 | 8 × Dell Precision 370 (Pentium 4 3.8 GHz, 2 GB), SUSE 10.2, gcc 4.1.2 -O3; SCIP 0.90f/0.90i + CPLEX 10.0.1 LP | 244 instances in 10 sets, 1 h (MIP) / 2 h (chip), 1.5 GB; shifted geometric mean with s = 10 (time) and s = 100 (nodes) | S1 pp. 319–322 |
| 2008 | Pentium 4 3.6 GHz PC; CPLEX 10.0.1, SCIP 0.90e; Zimpl 2.07 | TSP formulation variants | S7 p. 4 |
| 2014 | Intel i7-3770K, 4 cores, 32 GB; Gurobi 5.6.3 | 2,974 models, 10,000 s; shift 1 | S9 pp. 190–191 |
| 2016 | Intel i7-3770K, 4 cores, 32 GB; Gurobi 6.5 | 3,182 models, 3,600 s; shift 1 | S8 pp. 2–4 |
| 2015/16 | Titan supercomputer, up to 80,000 cores; ParaSCIP | open MIPLIB instances (12 solved) | W31 abstract (S14) |
| 2022 | Xeon E3-1240 v3, 4 cores / 8 threads, 32 GB; Gurobi 9.5.0 | 2,397 LP, 7,030 MIP, 10,000 s | S10 slide 5 |
| 2025 | Xeon E3-1240 v5, 4 cores / 8 threads, 32 GB; Gurobi (version not stated) | 8,611 MIP models, 10,000 s | S11 slides 25–26 |

[practice] P. The ZIB-era work used single desktops or workstations and colleagues' spare cycles; the Gurobi era uses a model library 12–35 times larger than the thesis set on equally modest 4-core machines, plus, through the ZIB collaboration, supercomputers. [inferred] from the table.

---

## 5. Method threads visible in the record (for Phase 2, not yet validated)

Cross-index for the signature works; each needs Agent 2 (stated method) and Agent 3 (process evidence) before it can become a core method.

- **A. Platform first.** He built a complete solver before publishing research on it, and his first experiments ran inside another group's solver (SIP). SW1; S1 pp. ix, 6; S29 0:28:00 (several years of almost uninterrupted coding).
- **B. Ablation over broad model libraries.** Every component is evaluated by switching it off, on shifted geometric means and solved-count tallies, never on single instances. SW1, SW2, SW4, T2; S1 p. 2, S3 p. 9, S8 pp. 2–4, S11 slides 25–26. (Consistent from 2004 to 2025; the shift parameter changed, see C5.)
- **C. Oracle-fidelity diagnostics.** To learn why a cheap rule works, measure its decisions against the expensive rule it approximates. SW2; S2 pp. 12–13.
- **D. Nesting parameter and effort budget.** One parameter spans the old rules, and effort is tied to a budget (strong-branching iterations, conflict limits). SW2, SW3.
- **E. Cross-field transfer (SAT/CP→MIP).** Conflict analysis, watched literals, restarts, inference branching. SW1, SW3; S1 pp. 3–5.
- **F. Negative results reported and acted on.** SW3 (the 2005 slowdown in the abstract), SW4 (disappointing reductions), F5–F8, F13 (the machine-learning route dropped for the one feature that mattered).
- **G. Industrial application as stress test, with data delivered early.** SW1, SW3; S1 p. ix.
- **H. Benchmark curation and reproducibility.** MIPLIB 2003, 2010 and 2017 (W6, W23, W34); minor reformulations (W14), whose conclusion is that reporting the exact model formulation is essential for reproducibility (S7 p. 7, joint).
- **I. Engineering for scale.** Worry about quadratic loops, keep safeguards for corner cases, and write algorithms on the solver's own data structures. T1; S10 slides 20–26 (2022, stated only; no practice evidence in the closed code).

---

## Contradictions

Kept as found; not reconciled.

- **C1. Thesis date and version.** DataCite records issue, submission and availability on 17 July 2007, and the defence was on 12 July 2007 (S21; S1 title page). MGP and DBLP say 2007. The ZIB copy is a revised version of 10 December 2008, posted 2009-01-28 (S14, docId 1112), and S28 cites the thesis as 2009 with the 2007 DOI. The two copies differ (418 vs 426 PDF pages).
- **C2. Isolating the branching rule.** 2002: supply the optimal solution in advance and fix root cuts, so that branching alone is compared (S2 pp. 10–11). 2004: deliberately do not supply the optimum, because a good branching rule should also lead to good solutions fast (S3 p. 8).
- **C3. Payoff of conflict analysis.** 2005: on feasible MIPs nodes −50 % but time +15 % (S5 p. 15). 2007: more than 10 % performance improvement with reasonable effort (S1 p. 5). Different SCIP versions (0.79a vs 0.90f) and test sets.
- **C4. What conflict constraints are for.** 2005: cutting planes added to the LP (S5 pp. 2, 14). 2007 default: never separated, propagation only (S1 p. 179).
- **C5. Shift of the shifted geometric mean.** Thesis: s = 10 s for time and s = 100 for nodes (S1 p. 321). Gurobi papers: a shift of 1 for both, citing the thesis as the source of the measure (S8 p. 4; S9 p. 191).
- **C6. CPLEX role.** Gurobi 2014: R&D member since 2006 and lead MIP developer for CPLEX 12.0–12.6 (S16). SEA 2022: CPLEX developer for versions 11 to 12.6 (S13).
- **C7. Who invented strong branching.** 2002: invented by CPLEX, citing the CPLEX 7.5 reference manual of 2001, with a see-also reference to Applegate et al. (S2 p. 4). 2004: introduced in CPLEX 7.5 (S3 p. 4). 2007 thesis: developed in the context of the TSP by Applegate et al., then soon standard in codes such as CPLEX (S1 p. 63).
- **C8. Authors of ZR 02-32.** The cover page lists Achterberg and Koch; the title page lists Achterberg, Koch and Martin (S2 cover and p. 1).
- **C9. The work behind the 2009 BOH Prize.** The MOS list names no work (S26); the SEA 2022 bio groups the prize with awards for his dissertation and for SCIP (S13); Gurobi 2014 names the prize only (S16).
- **C10. Value of primal heuristics (tension, not strict contradiction).** Thesis: disabling all primal heuristics costs only 14 % in time to optimality, though heuristics matter when users want good solutions fast (S1 p. 4). 2025: the talk abstract ranks RINS-type neighbourhood search first among Gurobi's heuristics for reaching good solutions fast (S12), and the slides measure first-feasible and gap targets rather than time to optimality (S11 slides 25–26). The metric differs.
- **C11. Intended audience of SCIP (tension).** 2004: tailored to experts wanting full control and high performance, not easy prototyping (S4 p. 1). 2006–2007: used for teaching graduate students and offered as a library for others' branch-cut-and-price research (S1 p. 6; W8, W9).
- **C12. ZR 05-19 date.** The OPUS record is dated 2005-03-22; the report itself is dated 3 August 2005, and its cover says August 2005 (S14; S5 p. 1).
- **C13. When SCIP started.** Thesis: development started in October 2002 (S1 p. 6), from scratch at the end of 2002 (S1 p. ix). 2023 interview captions: first commit to a CVS repository in 2001, as he remembers it (S29 0:27:30). Caption text may be misrecognised.
- **C14. SCIP's standing against CPLEX in 2005.** 2005 report: SCIP with CPLEX as LP solver is not strictly competitive with CPLEX 9.03, though not far away (S5 p. 15). 2023 recollection of the 2005 MIP workshop talk: roughly similar performance to CPLEX 9.0 (S29 0:36:30).
- **C15. Which branching rule works best.** 2004 and 2007: reliability branching beats pseudocost branching and pseudocost branching with strong-branching initialisation (S3 pp. 11–12; S1 p. 3). 2023: in his experience plain pseudocost branching works best in the end (S29 0:53:30). The caption excerpt is cut right after this sentence, so what he meant by it is unknown.

---

## Gaps

- Google Scholar profile: not reachable (login redirect and session verification); no Scholar counts or full list. OpenAlex: not queried (no API key).
- The two diploma theses (mathematics, 2000, on the arborescence flow problem; computer science, about a year later, on machine-learned branching, per S1 p. ix and S29): titles and texts not found, and the thesis bibliography does not cite them. Their topics rest on his own account only.
- S29 is caption text excerpted by another agent; the full video was not watched, and the excerpt leaves gaps (for example 0:54:00–0:55:00, right after his remark on pseudocost branching).
- Full texts not read: W17 (MPC 2009, closed; the thesis W10 was read instead), W3 journal version (the ZR was read), W5 journal version (the ZR and thesis ch. 11 were read; the journal abstract was not retrieved), W27 (closed; abstract plus S28's summary), W32 journal version (the ZR was read), and W7, W12, W13, W18, W20–W26, W29, W31, W33–W36 (abstracts or metadata only). The RLT papers (arXiv 2211.13545) are open but were not read.
- No statement found in which he ranks his own works or names his most important contribution.
- No account of how the Gurobi presolve paper (SW4) or the 2013 progress study (SW5) began. The CPLEX-era (2006–2014) work is largely unpublished company code.
- Rejected papers, withdrawn claims, errata: none found.
- Patents: one web search found none; Google Patents was not queried directly.
- ZIB OPUS search and export endpoints failed (HTTP 500) on 2026-11-08. Report coverage rests on OAI harvesting of selected MSC sets and docId scans 690–1111; later untagged reports may be missing.
- Supervision: only Wolter and Berthold are named as his students (S1 p. x); MGP lists none. Hendel, Bestuzheva and others: not verified.
- 2026 activity: nothing found (latest dated items: the MIP Workshop talk of 4 June 2025 and the 2025 Math. Prog. issue).
- His role on the 2021–2025 papers where he is last author: not stated in any source read.

---

## Sources

Primary (P) and secondary (S). All fetched 2026-11-08.

- **S1** (P) Tobias Achterberg, *Constraint Integer Programming*, PhD thesis, TU Berlin, approved 15 May 2007, defended 12 July 2007, revised 10 December 2008. ZIB OPUS docId 1112, urn:nbn:de:0297-zib-11129 (copy read); TU Berlin DepositOnce handle 11303/1931, DOI 10.14279/depositonce-1634 (2007 copy).
- **S2** (P) T. Achterberg, T. Koch, A. Martin, *Branching on History Information*, ZIB-Report 02-32, October 2002, urn:nbn:de:0297-zib-6990.
- **S3** (P) T. Achterberg, T. Koch, A. Martin, *Branching Rules Revisited*, ZIB-Report 04-13, May 2004, urn:nbn:de:0297-zib-7886 (journal: ORL 33 (2005) 42–54, DOI 10.1016/j.orl.2004.04.002).
- **S4** (P) T. Achterberg, *SCIP – a framework to integrate Constraint and Mixed Integer Programming*, ZIB-Report 04-19, May 2004, urn:nbn:de:0297-zib-7947.
- **S5** (P) T. Achterberg, *Conflict Analysis in Mixed Integer Programming*, ZIB-Report 05-19, August 2005, urn:nbn:de:0297-zib-8537 (journal: Discrete Optimization 4 (2007) 4–20, DOI 10.1016/j.disopt.2006.10.006).
- **S6** (P) T. Achterberg, T. Koch, A. Martin, *MIPLIB 2003*, ZIB-Report 05-28, May 2005, urn:nbn:de:0297-zib-8625 (journal: ORL 34 (2006) 361–372, DOI 10.1016/j.orl.2005.07.009).
- **S7** (P) T. Achterberg, T. Koch, A. Tuchscherer, *On the Effects of Minor Changes in Model Formulations*, ZIB-Report 08-29, August 2008, urn:nbn:de:0297-zib-10808.
- **S8** (P) T. Achterberg, R. E. Bixby, Z. Gu, E. Rothberg, D. Weninger, *Presolve Reductions in Mixed Integer Programming*, ZIB-Report 16-44 (cover: September 2016; title page dated 9 December 2016), urn:nbn:de:0297-zib-60370 (journal: INFORMS J. Computing 32 (2020) 473–506, DOI 10.1287/ijoc.2018.0857; abstract via Crossref).
- **S9** (P) T. Achterberg, R. E. Bixby, Z. Gu, E. Rothberg, D. Weninger, *Multi-Row Presolve Reductions in Mixed Integer Programming*, Proceedings of the Twenty-Sixth RAMP Symposium, Hosei University, Tokyo, 16–17 October 2014, pp. 181–196, https://orsj.org/ramp/wp-content/uploads/sites/9/2021/03/paper2014_4-4.pdf
- **S10** (P) T. Achterberg, *Combinatorial Algorithms Used Inside a MIP Solver*, invited talk slides, SEA 2022, Heidelberg, 26 July 2022, https://sea2022.ifi.uni-heidelberg.de/talk_achterberg.pdf
- **S11** (P) T. Achterberg, *From Infeasibility to Feasibility – Improvement Heuristics to Find First Feasibles for MIPs*, slides, MIP Workshop 2025, Minneapolis, 4 June 2025, https://www.mixedinteger.org/2025/ (slides linked there)
- **S12** (P) MIP Workshop 2025 home page, talk abstract by Achterberg (University of Minnesota, 3–6 June 2025), https://www.mixedinteger.org/2025/
- **S13** (S) SEA 2022 home page (speaker bio) and programme page (talk abstract; session chair Leo Liberti), https://sea2022.ifi.uni-heidelberg.de/ and /program.html
- **S14** (P) ZIB OPUS OAI-PMH records for 22 Achterberg works (titles, dates, abstracts, URNs, file names), https://opus4.kobv.de/opus4-zib/oai
- **S15** (P) ORCID public record 0000-0002-0862-7065 (employment Gurobi Optimization GmbH from 2014-03; 2 works), https://pub.orcid.org/v3.0/0000-0002-0862-7065/record
- **S16** (S) Gurobi Optimization, *Dr. Tobias Achterberg Joins the Gurobi Optimization R&D Team*, newsroom (2014; page undated), https://www.gurobi.com/company/newsroom/dr-achterberg-joins-gurobi
- **S17** (S) Gurobi Optimization, *Gurobi Optimization Announces Promotion of Dr. Tobias Achterberg to Vice President of R&D*, Beaverton OR, 22 April 2020, https://www.gurobi.com/company/newsroom/gurobi-optimization-announces-promotion-of-dr-tobias-achterberg-to-vice-president-of-rd
- **S18** (S) DBLP, person pid 71/6632, 23 records, via sparql.dblp.org (`scripts/dblp_works.py --pid 71/6632`), https://dblp.org/pid/71/6632.html
- **S19** (S) Crossref REST API, works by DOI and `query.author=Tobias Achterberg` (metadata and `is-referenced-by-count`), https://api.crossref.org/
- **S20** (S) Semantic Scholar Graph API, authors 1793775, 2137115989, 2091309794 (paper lists and citation counts), https://api.semanticscholar.org/
- **S21** (S) DataCite record for DOI 10.14279/depositonce-1634 (dates, rights statement In Copyright, Grötschel as related person), https://api.datacite.org/dois/10.14279/depositonce-1634
- **S22** (S) Springer landing pages (abstracts and metadata) for 10.1007/s12532-008-0001-1, 10.1007/978-3-642-38189-8_18, 10.1007/978-3-642-01929-6_23, 10.1007/978-1-4419-1644-0_5, https://link.springer.com/
- **S23** (S) arXiv author search (Achterberg; one Tobias Achterberg preprint, 2211.13545), https://arxiv.org/search/
- **S24** (S) Unpaywall API, open-access status of six DOIs (email parameter nuwa-skill@users.noreply.github.com), https://api.unpaywall.org/
- **S25** (S) Mathematics Genealogy Project, Tobias Achterberg, id 117695, https://www.mathgenealogy.org/id.php?id=117695
- **S26** (S) Mathematical Optimization Society, Beale–Orchard-Hays Prize winners and juries, https://mathopt.zib.de/?nav=boh
- **S27** (S) INFORMS, Award Recipients: Tobias Achterberg (2011 OS Young Researchers Prize with citation; 2008 Dantzig Dissertation Award second place), https://www.informs.org/Recognizing-Excellence/Award-Recipients/Tobias-Achterberg
- **S28** (S) T. Koch, T. Berthold, J. Pedersen, C. Vanaret, *Progress in Mathematical Programming Solvers from 2001 to 2020*, arXiv 2206.09787v1, 20 June 2022.
- **S29** (P, caption text) *Subject to: Tobias Achterberg*, interview on the YouTube channel Subject to (@Subjectto_), uploaded 2023-08-17, https://www.youtube.com/watch?v=8bhIW27vCUQ (title and channel confirmed via YouTube oEmbed); read as the auto-caption excerpts in `references/sources/talks/subject-to-2023-interview.excerpt.transcript.txt`, saved by research agent 04 in this run. Not speaker-checked; cited by timestamp.
