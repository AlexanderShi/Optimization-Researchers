# Qi Huangfu · 01 · Publication landscape and signature works

| | |
|---|---|
| Researcher | Qi Huangfu (DBLP pid 116/5281): LP solver developer. University of Edinburgh PhD 2013 (supervisor J. A. J. Hall), original author of the hsol/HSOL dual revised simplex code (the simplex core of HiGHS), implementer of the parallel dual simplex in FICO Xpress, now at Cardinal Operations (COPT) |
| Dimension | Research agent 01 of 06: publication landscape and dissection of signature works (framework §二 Agent 1, §五) |
| Research date | 2026-10-27 |
| Sources consulted | 47 (32 primary, 15 secondary), listed as S1–S47 under "Sources". 3 WebSearch calls; everything else was fetched with curl/WebFetch from known URLs, APIs and repositories |
| Local corpus | `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep`: there was no user-supplied material. `private/` was not opened |
| OpenAlex | not queried (`OPENALEX_API_KEY` is not set) |
| Quote check | Every quotation below was matched verbatim, by script, against the extracted text of its source (PDF page, HTML or transcript file): 134 checks, 0 misses. Page numbers are printed page numbers unless "PDF p." or "slide" is written; slide numbers are PDF page numbers of the slide file |

**Tags.**
- **[stated]**: said by Huangfu. Sole-author texts (thesis, FICO blog, JuliaCon bio) are his own voice. "joint" marks a paper he co-signed with Hall, where the two voices cannot be separated.
- **[practice]**: what the record shows was done (experiments, code, dated slides, datasets).
- **[observed]**: what others recorded (Hall's pages and slides, the HiGHS README, Google's code, prize records).
- **[inferred]**: my inference, with its basis named.
- **P / S**: primary / secondary source.

**Reading depth.**
- Read in full: the PPAM report ERGO-11-007 (S9), the APMOD 2012 extended abstract (S13) and the FICO blog post (S16).
- Read in part:
  - Thesis (S8): pp. 3–18, 75–86, 93–94.
  - MPC paper (S11): pp. 119–121, 130, 133–134, 136, 138–142.
  - COAP technical report, 7 July 2013 version (S10): pp. 1–2, 15–18.
  - COPT guide v1 (S19): front pages and §1.
  - cuPDLP-C v2 (S20): pp. 1–4.
  - Slides S22–S29: title slides and the slides cited.
- Also read in full: the JuliaCon 2022 caption transcript (S47).
- Not read: the published COAP version, the COAP prize article (paywalled), the SPE 2009 paper (closed) and the 2014 dataset spreadsheet. The JuliaCon 2022 video was not watched.

---

## 0. Identity and disambiguation

- [practice, S] **DBLP pid 116/5281** has exactly 5 records, 2012–2022: PPAM 2012, COAP 2015, CoRR 1503.01889, MPC 2018 and CoRR 2208.14314. Co-authors: J. A. Julian Hall (4); Dongdong Ge, Jian Wu, Zizhuo Wang, Yinyu Ye (1 each). DBLP holds no ORCID and no homepage for him. [S1]
- [observed, S] **Semantic Scholar author 2513024303**, the profile DBLP-linked to "Qi Huangfu", merges at least two people. Six of its 17 items are Chinese-language history and agronomy items (1998, 2001, 2008, 2010, 2014, and a 2020 chapter with M. Kohrman in *Poisonous Pandas*) by someone else. Its totals (810 citations, h-index 6) are therefore unusable for him.
  - S2 author 2841156 (12 urology/oncology items, 2006–2026) and author 2056477171 ("Huangfu Qi", biomedical) are other people.
  - The only ORCID found for "Qi Huangfu" (0009-0004-4351-0956) is affiliated with the Second Affiliated Hospital of Zhejiang University, i.e. the medical researcher that team.json excludes. [S2, S6]
- [practice, P] **Name variants in primary material.** "Q. Huangfu" in the papers, "Huangfu Qi" on the IMA-NLAO slides of 14 Sep 2010 [S24, slide 1], and "Qi" used as a surname ("H and Qi", Lancs11 [S26, slide 15]). Name searches must cover all three.
- [inferred] **The 2009 SPE paper** (W1) is credited in Crossref's author metadata to Q. Huangfu, with affiliation The University of Edinburgh, next to F. Reid, also of Edinburgh. It is about parallel scientific C++ code and appeared about 18 months before his first co-listing on a simplex talk. That makes it plausibly the same person, but no primary source links the two, so it carries "identity inferred" below.

---

## 1. Publication landscape

### 1.1 Verified works

Every identifier was resolved with a tool on 2026-10-27; the "how checked" column says which. "Hall corresponding" means Hall's e-mail is the contact address printed on the paper.

| # | Year | Work | Venue / type | Identifier (how checked) | Author position | Read | Tags |
|---|---|---|---|---|---|---|---|
| W1 | 2009 | Massively Parallel Sector Scale Discrete Fracture and Matrix Simulations | SPE Reservoir Simulation Symposium, The Woodlands TX, 2–4 Feb 2009 (proceedings article) | DOI 10.2118/118924-MS (Crossref; S2) | 2nd of 8 (S. Geiger first) | not read (closed access) | [practice] P · identity inferred |
| W2 | 2012 | A High Performance Dual Revised Simplex Solver | PPAM 2011, Part I, LNCS 7203, pp. 143–151 (Springer, 2012); technical report ERGO-11-007, 12 May 2011 | DOI 10.1007/978-3-642-31464-3_15 (DBLP; Crossref; Hall's page) | 2nd of 2 (Hall, Huangfu; Hall corresponding) | report in full | [practice] [stated, joint] P |
| W3 | 2012 | Promoting hyper-sparsity in the revised simplex method | APMOD 2012 talk; extended abstract dated 29 Mar 2012 ("Preprint submitted to Elsevier") | PDF on Hall's site (S13); S2 CorpusId 64348098; no DOI | 2nd of 2 (Hall corresponding) | in full | [practice] [stated, joint] P |
| W4 | 2013 | High performance simplex solver | PhD thesis, University of Edinburgh; ERA date 2013-07-01; PDF and LaTeX sources deposited | hdl:1842/7952 (ERA record) | sole author | in part | [stated] [practice] P |
| W5 | 2014/2015 | Novel update techniques for the revised simplex method | Computational Optimization and Applications 60(3):587–608 (online 23 Aug 2014, issue Apr 2015). ERGO-13-001 exists in a 28 Jan 2013 version (cited in Glop) and a 7 July 2013 version (on Hall's site). Optimization Online, 14 Feb 2013 | DOI 10.1007/s10589-014-9689-1 (DBLP; Crossref; Hall's page; Optimization Online) | 1st of 2 (Hall corresponding) | 7 July 2013 report in part | [stated, joint] [practice] P |
| W6 | 2014 | Parallel simplex benchmarking results [dataset] | Edinburgh DataShare, 23 Dec 2014. Files HsolNov14-17.xlsx and ERGO-14-011.pdf; "Data used to generate results in" W7 | DOI 10.7488/ds/196 (DataShare record) | 1st of 2 | record only | [practice] P |
| W7 | 2015/2018 | Parallelizing the dual revised simplex method | Mathematical Programming Computation 10(1):119–142. Received 6 Mar 2015, accepted 10 Feb 2016, online 14 Dec 2017, issue Mar 2018; CC BY 4.0. ERGO-14-011; arXiv 1503.01889 (6 Mar 2015) | DOI 10.1007/s12532-017-0130-5; arXiv 1503.01889 (DBLP; Crossref; arXiv; Hall's page; Optimization Online) | 1st of 2 (Hall corresponding) | in part | [stated, joint] [practice] P |
| W8 | 2016 | COAP 2015 Best Paper Prize | Computational Optimization and Applications 65(3):541–544 (online 1 Nov 2016) | DOI 10.1007/s10589-016-9882-5 (Crossref lists no authors; Hall's publication page credits "Q. Huangfu and J. A. J. Hall") | 1st of 2 per Hall's page | not read (paywalled); reference list read | [observed] P |
| W9 | 2022–2026 | Cardinal Optimizer (COPT) User Guide | arXiv documentation: v1 30 Aug 2022 (Ver 5.0.4), v2 28 Oct 2022, v3 16 Nov 2024, v4 30 Jan 2026 | arXiv 2208.14314 (arXiv record; DBLP; S2) | 2nd of 5; the order (Ge, Huangfu, Wang, Wu, Ye) is alphabetical | v1 front pages | [practice] P |
| W10 | 2023/2024 | cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language | arXiv report: v1 22 Dec 2023, v2 7 Jan 2024. His affiliation: "Cardinal Operations" | arXiv 2312.14832 (arXiv record; S2). Not in DBLP under pid 116/5281 | 4th of 9 (Lu and Yang lead; Ge last, corresponding) | v2 pp. 1–4 | [practice] P |

### 1.2 Talks, essay, software and other public outputs

| # | Date | Item | Listed authors (affiliation as printed) | Source | Tags |
|---|---|---|---|---|---|
| T-a | 14 Sep 2010 | "Towards a practical parallelisation of the revised simplex method", IMA-NLAO 2010 | Hall, Smith, "Huangfu Qi" | S24 | [observed] P |
| T-b | 2 Dec 2010 | "A high performance dual revised simplex solver", RAL10 | Hall, Huangfu, Smith | S25 | [observed] [practice] P |
| T-c | 12 Apr 2011 | "High performance computing and the simplex method", Lancs11 | Hall, Huangfu, Smith | S26 | [observed] P |
| T-d | 13 Sep 2011 | "A high performance dual revised simplex solver", PPAM 2011 talk | Hall, Huangfu | S27 | [observed] P |
| T-e | 11 Sep 2015 | "High performance simplex solvers for linear programming problems", Google, Paris | Hall (Edinburgh), Huangfu (FICO), Lubin (MIT); slide footers name Julian Hall as presenter | S22 | [observed] P |
| T-f | 30 Nov 2016 | "Novel update techniques for the revised simplex method (and their application)", ERGO seminar, Edinburgh | Huangfu (FICO), Hall, "Others" | S23 | [observed] P |
| T-g | 22 May 2017 | "An open-source high performance dual simplex solver", SIAM Conference on Optimization | Hall, Huangfu (FICO), Galabova | S28 | [observed] P |
| T-h | 13 Jul 2017 | "Novel update techniques for the revised simplex method", EUROPT 2017 ("In memory of Roger Fletcher") | Huangfu (FICO), Hall. The closing slide, "I've been updating for 30 years: time to reinvert!", is in Hall's voice, so the presenter was probably Hall [inferred] | S29 | [observed] P |
| T-i | 27 Jul 2022 | "COPT and its Julia interface", JuliaCon 2022 lightning talk (10 min) | Huangfu | S21; caption transcript S47 (saved by agent 02, read for this note) | [stated] P · video not watched |
| E1 | 13 May 2014 | "The Algorithm that Runs the World", FICO Blog; the only post listed on his FICO author page (archived 2018-06-29) | Huangfu | S16, S17 | [stated] P |
| SW1 | 2010–2018 | ParISS (prototype, 2010–2012), then hsol/HSOL 1.0, then h2gmp: a C++/OpenMP dual revised simplex solver | README: "HSOL was originally written by Qi Huangfu, with features such as presolve, crash and advanced basis start added by Julian Hall and Ivet Galabova." | S35, S25 | [observed] [practice] P |
| SW2 | 2018– | HiGHS (ERGO-Code/HiGHS, MIT licence, repository created 2018-03-27) | README: "HiGHS has primal and dual revised simplex solvers, originally written by Qi Huangfu and further developed by Julian Hall." | S37 | [observed] P |
| SW3 | by May 2014 | Parallel dual simplex in FICO Xpress (closed source) | W7 pp. 140–141; E1 | S11, S16 | [stated] P |
| SW4 | by 2022 | COPT (Cardinal Operations; closed source) | JuliaCon bio: "Qi Huangfu is the developer of COPT and has worked on many different optimization solvers, including HiGHS and FICO-Xpress." | S21 | [stated] P · his individual contribution is not documented |

### 1.3 Unverified leads (not counted)

- **2008 report.** "Optimization of a large-scale parallel finite element - finite volume C++ code" is listed in S2 with sole author "Qi Huangfu" (CorpusId 123954943; no venue, no DOI). One WebSearch (S43) found no copy and no venue, so identity and venue are unknown.
- **Not a paper.** S2 lists "High performance simplex solvers for linear programming problems" (2015; Hall, Huangfu, Lubin) as a paper. It is the slide deck of talk T-e.
- **Résumé lead, discarded.** A WebSearch summary (S44) said a student's résumé names Huangfu as a supervisor of a 2023–2024 COPT project. The current résumé does not mention him (S46).
- **Misattribution claim, not used.** The same summary said a third-party site attributes cuPDLP-C to a different "Huangfu". The arXiv PDF itself prints "Qi Huangfu" with affiliation "Cardinal Operations" (S20), so the claim was not used.

### 1.4 Topics by five-year period

| Period | Role and place (evidence) | Topics | Output |
|---|---|---|---|
| 2008–2009 | Identity inferred: University of Edinburgh affiliation (W1, Crossref) | Massively parallel discrete-fracture reservoir simulation | W1 |
| 2010–2014 | PhD student at Edinburgh: first co-listed talk Sep 2010 (T-a), thesis July 2013 (W4). Then at FICO: blog May 2014 (E1) | Dual revised simplex engineering: hyper-sparse FTRAN/BTRAN, DSE and BFRT; LU update variants (APF, MPF, CFT); "hyper-sparsity promotion" (cost perturbation, partial CHUZR, LiDSE); parallel dual simplex (ParISS, then PAMI and SIP) | W2–W6, T-a to T-d, E1, SW1 |
| 2015–2019 | FICO, Birmingham UK (W7 address "FICO House, International Square, Starley Way, Birmingham B37 7GN, UK"; slide affiliations Sep 2015 to Jul 2017) | Publishing the PhD work (W7, 2015 to 2018); talks with Hall; HSOL handed to Edinburgh and turned into HiGHS. No new research topic appears in the public record | W7, W8, T-e to T-h, SW2, SW3 |
| 2020–2026 | Cardinal Operations (W10 affiliation; JuliaCon 2022 bio) | Commercial solver COPT (LP, MIP, conic); co-author of a GPU first-order LP (PDLP) implementation | W9, W10, T-i, SW4 |

[inferred] All of his research output (W2–W8) concerns the computational core of the revised simplex method. The only departure visible in the record is W10 (GPU first-order LP, 2023), and his role in it is not stated.

### 1.5 Author position: no first-to-last-author shift

- [practice] Positions by period:
  - Second author behind his supervisor on the earliest items, W2 and W3 (that order also happens to be alphabetical).
  - Sole author of the thesis, W4.
  - First author of the two journal papers and the dataset, W5, W6 and W7.
- [practice] Hall is the corresponding author throughout: W2, W3, W5 and W7 all print Hall's e-mail address, including W7, where Huangfu is first author.
- [practice] In the industry period he is credited inside alphabetical author lists:
  - W9: Ge, Huangfu, Wang, Wu, Ye.
  - W10: in the alphabetical middle block (Hu, Huangfu, J. Liu, T. Liu, Ye, Zhang), between the lead authors Lu and Yang and the corresponding author Ge, placed last.
- No last-author (supervising) paper was found. [inferred] The record shows lead authorship as a PhD student and early-career developer (2013–2018), then team credit inside companies. The research thread effectively ends with the publication of the PhD work.

### 1.6 Collaboration network and students

- **J. A. Julian Hall**: PhD supervisor. Co-author of every academic item (W2–W8) and co-listed on all eight talks T-a to T-h. [practice] His homepage lists Huangfu among "former PhD students" (S30).
- **Jacek Gondzio**: "my second PhD supervisor" (thesis p. 7) [stated]. No co-authored item was found.
- **Edmund Smith**: co-listed on the 2010–2011 talks, where he ran the GPU standard-simplex code ("i8") and the block-angular revised-simplex code ("i7") (S24–S26) [observed]. No joint paper.
- **Ivet Galabova**: added presolve, crash and advanced-basis start to HSOL (S35 README) and is co-listed on the 2017 SIAM talk (S28) [observed]. No joint paper.
- **Miles Lubin**: co-listed only on the 2015 Google talk (S22) [observed].
- **Industry co-authors**: D. Ge, Z. Wang, J. Wu, Y. Ye (W9); H. Lu, J. Yang, H. Hu, J. Liu, T. Liu, C. Zhang, Y. Ye, D. Ge (W10) [practice].
- **2009 co-authors (identity inferred)**: S. Geiger, F. Reid, S. Matthäi, D. Coumou, M. Belayneh, C. Fricke, K. Schmid.
- **Students**: none found, and there is no public record of supervision; the one lead failed verification (§1.3). In the public cuPDLP-C repository none of the commits from Dec 2023 to Oct 2026 are his. The listed contributors are bzhangcw, hannes-uppman, SkyLiu0, JinsongLiu6, yinxd15 and others (S39). [practice]

### 1.7 Usual venues

- **Journals and proceedings**: Springer LNCS (PPAM), Computational Optimization and Applications and Mathematical Programming Computation.
- **Preprint and deposit channels**: ERGO technical reports, Optimization Online and arXiv (math.OC); the Edinburgh Research Archive (thesis) and DataShare (data).
- **Other outlets**: an industry blog (FICO) and a developer conference (JuliaCon).
- **Absent**: no conference paper after 2012; no paper in Mathematical Programming, SIAM journals or INFORMS JOC.

### 1.8 Citation counts and most-cited works (fetched 2026-10-27)

| Work | Crossref | Semantic Scholar (influential) |
|---|---|---|
| W7 MPC 2018 | 445 | 654 (73) |
| W9 COPT User Guide | n/a (DataCite DOI) | 67 (7) |
| W10 cuPDLP-C | n/a | 49 (5) |
| W1 SPE 2009 (identity inferred) | 9 | 16 (1) |
| W5 COAP 2015 | 5 | 12 (1) |
| W2 PPAM 2012 | 8 | 11 (3) |
| W4 thesis | n/a | 6 (0) |
| W3 APMOD 2012 | n/a | 1 |
| W6 dataset | n/a | 0 |

Google Scholar could not be used: the author search redirects to a login page (S7).

- [observed] **The two most-cited items are citation requests for software.**
  - HiGHS: "If you use HiGHS in an academic context, please acknowledge this and cite the following article." The article is W7 (S37).
  - COPT: "If you used COPT in your research work, please mention us in your publication." The reference given is W9 (S19, §1.3).
  - [inferred] These counts therefore measure use of HiGHS and COPT as much as the influence of the papers.
- [observed] **Influence is not tracked by citations.** W5 has only 5 to 12 citations, yet its middle product form update is implemented in Google OR-Tools' Glop (S38), and its APF and CFT updates are components of PAMI (S29 slide 19).

### 1.9 Recent works (since October 2024)

- W9 v3 (16 Nov 2024) and v4 (30 Jan 2026): revisions of the documentation.
- No new research paper appears in DBLP, arXiv (author search) or Semantic Scholar after cuPDLP-C v2 (7 Jan 2024).
- [observed, company] For context only, not attributable to him individually: the COPT 8.0.x release notes include "Improved performance of advanced simplex routines" next to GPU barrier and first-order solver items (S40).

---

## 2. Signature works (dissection, framework §五)

**Selection.**
- **W7**: most cited, prize-winning, and the paper HiGHS asks users to cite.
- **W5**: prize-winning, and adopted in Google's code.
- **W4 with the hsol code base**: the work he himself points to. His blog sends readers to the thesis: "A detailed introduction to this approach is available here", linking to hdl:1842/7952 (S16). The code became HiGHS's simplex core, and the thesis holds the unpublished hyper-sparsity-promotion line.
- **The two industrial turning points**: FICO Xpress (2014) and COPT (by 2022).

W2 (ParISS) is dissected inside W7 as its minimum evidence. The labels PM1 to PM9 are candidate research methods for Phase 2 to test (§5), not conclusions.

### 2.1 W7 · Parallelizing the dual revised simplex method (PAMI and SIP), with W2 as its first evidence

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin | **(1) Suboptimization was on the supervisor's agenda before the prototype existed.** Hall's IMA-NLAO slides (14 Sep 2010) list "Perform standard simplex suboptimization", with "Dual: Rosander (1975)", as a way to improve "scope for parallelism" (S24 slide 42). Hall's earlier primal schemes PARSMI (1996) and ASYNPLEX (1998) are on his publication page (S31) and are cited in W2 and W7. **(2) The paper names its own motivation:** "Two main factors motivated the work in this paper to develop a parallelisation of the dual revised simplex method for standard desktop architectures." (W7 p. 120). The first factor is that Bixby and Martin (2000) was the only dual parallelisation and had neither BFRT nor hyper-sparse solves. The second is that desktops are now multi-core. **(3) Who chose suboptimization as the vehicle is not stated** in anything read. The dated slides suggest [inferred] that the direction came from Hall's programme and that Huangfu built the code: the RAL10 prototype is "Written by Qi Huangfu (2010)" (S25 slide 23). The COAP prize article (W8), which may tell the origin story, was not read | [observed] P (S24, S25, S31); [stated, joint] P (W7); [inferred] |
| Why then | "nowadays, when every desktop computer is a multi-core machine, any speedup is desirable in terms of solution time reduction for daily usage" (thesis p. 15). "OpenMP is chosen partially because the resulting simplex parallelization framework is based on a memory-sharing model, and partially because of its simple and powerful parallel directive, especially the task directive introduced in OpenMP version 3.0 in 2008." (thesis p. 17). DSE and BFRT, both from the 1990s, had made the dual the preferred variant (W7 p. 120) | [stated] P |
| Key insight | **Merge several dual iterations into one parallel "meta" iteration.** In his own words: "The key idea behind this implementation is to create more parallelizable scope by combining multiple simplex iterations into one meta simplex iteration." (S16). **Accept a worse pivot path in exchange:** "Though it is inevitable that the suboptimization leads to a generally worse simplex path, it provides more scope for task parallelism." (thesis p. 17). The loss is controlled by a cutoff on candidate attractiveness. **SIP is the complementary scheme:** it keeps the regular DSE rule and overlaps components within one iteration. The underlying device is "a relatively unknown pivoting strategy called suboptimization" (W7 p. 119). Hall's slides add "Suggested by Rosander (1975) but never implemented efficiently in serial" (S22 slide 26) | [stated] P; [stated, joint] P; [observed] P |
| Minimum evidence | **First run.** The RAL10 slides of 2 Dec 2010 say "Written by Qi Huangfu (2010)" and "First run last week!": C++ with OpenMP, a dual quad-core AMD Opteron 2378, one pivotal row per core (S25 slide 23). **First reported results (W2 report, 12 May 2011, pp. 5–6).** The test set was 114 Netlib and Kennington problems; the 84 solved in under a second were discarded. "Of the remaining 30, ParISS failed to solve 14 in one or more of the runs using 1, 2, 4 and 8 cores". Three more were dropped because ParISS was over ten times slower than "version 1.06 of the COIN-OR [13] (serial) dual simplex solver Clp". On the 13 problems left, "the (geometric) mean speed-up was about 30% on 4 and 8 cores". On one core, "ParISS was faster for only one problem and was slower by a factor of 2.7 on average." Even so: "For a prototype solver with the limited parallel efficiency recognised in Section 3, the results in Table 1 are very encouraging" | [practice] P (S25, W2) |
| Abandoned paths | **(a) GPU route.** The Dec 2010 talk outline contains "Alternative product form update for GPU extension" (S25 slide 2). The Apr 2011 slides say "Outcome will inform planned CPU+GPU implementation of dual simplex with suboptimization." (S26 slide 24). No later paper, slide or code on a GPU dual simplex was found [inferred from absence]. **(b) Dense-algebra parallel simplex,** ruled out by analysis: "Therefore, this path is excluded from future consideration." (thesis p. 75). **(c) Overlapping INVERT with the iterations.** "One reason for the relative poor speedup of PAMI is that the time-consuming sequential LU factorization is not overlapped with the simplex iterations." (thesis p. 94). It was left as future work and is not in W7. **(d) Cutoff values outside [0.9, 0.999].** Twenty-one cutoffs from 1.001 to 0.01 were tried. A cutoff of 1.001 gave a mean speed-up of 1.12, and values below 0.9 degraded it (thesis Table 4.4, p. 86; the same sweep is in W7 p. 130). **(e) Prototype shortcuts, later replaced:** ParISS "for convenience, it identifies a "master" core that is used for computation when an alternative core might be preferable on grounds of data locality." (W2 p. 5); INVERT ran serially with no overlap | [practice] P; [stated] P; [inferred] |
| Reception | **Publication timeline.** Received 6 Mar 2015, accepted 10 Feb 2016, online 14 Dec 2017: 22 months from acceptance to online publication, reason not found. **Prize.** "Awarded the prize for the best paper of 2018 in Mathematical Programming Computation", per Hall's pages (S31, S33); not independently confirmed. **Citations.** Crossref 445, S2 654 (§1.8; inflated by the HiGHS citation request). **Transfer to Xpress.** "Since developing and implementing the techniques described in this paper, Huangfu has implemented them within the FICO Xpress simplex solver" (W7 p. 140). The authors add that the refinements were "considered noteworthy enough to be reported by FICO" (p. 141). Hall's slides of 2016–2017 claim "Xpress simplex solver now fastest commercial simplex solver" (S23 slide 34). W7 says Mittelmann's benchmarks reflect this; I did not check that | [practice] [observed] P; [stated, joint] P |
| Method it shows | PM1 efficient baseline first. PM2 bound the speed-up before building (profiling plus Amdahl). PM3 revive an under-used classical device and pay its price explicitly. PM5 sweep a parameter, then choose a robust value. PM6 honest accounting. PM8 transfer into production code. PM9 a complementary fallback scheme | [inferred] |

### 2.2 W5 · Novel update techniques for the revised simplex method (APF, MPF, CFT)

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin | "Motivated by the requirements of the high performance implementation of the revised simplex method (hsol) developed by Huangfu and Hall [16], this paper introduces three novel procedures" (W5 report p. 2). The thesis gives a second source: "Study and implementation of classic update procedures led to the development of three novel update techniques." (p. 16). APF appears first in the 2 Dec 2010 talk as "Alternative product form update for GPU extension" (S25 slide 2): it began as a device for a CPU–GPU scheme | [stated, joint] P; [stated] P; [practice] P |
| Why then | PAMI makes several basis changes per major iteration. It needed an update that handles several changes at once (CFT) and a cheap way to apply the updated inverse to many vectors (APF). So the techniques were needed once the parallel scheme existed [inferred]; W5 p. 2 and W7 §2.4 tie them to the parallel solver | [inferred] |
| Key insight | Re-factor the rank-one basis change so that the eta factor sits in a new place: on the right (APF, B̄ = T B), between the LU factors (MPF, B̄ = L T U), or collect several Forrest–Tomlin eliminations into one (CFT). On the slides: "Idea: Why not take it out on the right!" (S29 slide 13) | [stated, joint] P |
| Minimum evidence | **Controlled replay.** All five updates were run on the same sequence of basis changes, from a logical basis to an optimum, on 30 problems, with the same reinversion intervals. Reasons given: "This eliminates variance in the results due to the fact that a change in update technique typically leads to the simplex method taking a different path to an optimal solution", and the setup "ensures that the FT update is not disfavoured" (report p. 15). **Results.** "The superiority of the MPF update over the PF and APF updates is clear: it is the best for 26 of the 30 problems." It is 40% more efficient (geometric mean) than the better of PF and APF; FT is 61% more efficient again (report p. 16). The EUROPT 2017 summary of geometric-mean times: PFI 1.00, FT 0.30, APF 0.95, MPF 0.45, CFT 0.29 (S29 slide 16) | [practice] P |
| Abandoned paths | **APF as a general technique:** "The APF is very inefficient for some problems and is not recommended as a valuable general technique." (report p. 17). **The GPU motivation of APF** (2010) is absent from all later texts [inferred]. **MPF was not used in their own solvers:** "Not used by pami! Used by Google in glop" (S23 slide 32) and "Not used by h2gmp! Used by Google in glop" (S29 slide 19). Their code kept the Forrest–Tomlin update | [stated, joint] P; [practice] P; [inferred] |
| Reception | **Prize.** COAP best paper of 2015 (Hall's pages S31 and S33; prize article W8). **Adoption at Google, verified in the code.** OR-Tools Glop has `MiddleProductFormUpdate`, commented "Updates the factorization using the middle product form update." and citing "Qi Huangfu, J. A. Julian Hall, "Novel update techniques for the revised / simplex method", 28 january 2013, Technical Report ERGO-13-0001" (S38, lines 325–329; this file has lived under `ortools/` since 2017-04-26). Hall's 2017 slides list "Google (techniques in glop)" under commercial involvement (S28 slide 13). **Citations** are low: Crossref 5, S2 12 | [observed] P |
| Method it shows | PM4 re-factor the algebra for implementation simplicity. MPF "is very much easier to implement than the FT update so is an attractive update procedure when developing a simple, relatively efficient implementation of the revised simplex method for either research studies or in an industrial context where an independent code-base is necessary." (report p. 18). PM5 controlled replay. PM6 an honest negative verdict on one's own technique | [inferred] |

### 2.3 W4 · High performance simplex solver (thesis) and the hsol code base

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin | "Though there are many public domain simplex implementations, they are either too complicated to be extended for parallelization or too simple to be based on. Thus, a sequential dual simplex solver, named HSOL, has been implemented from scratch." (thesis p. 16). W7 repeats the point: "Although there are many public domain simplex implementations, they are either too complicated to be used as a foundation for a parallel solver or too inefficient for any parallelisation to be worthwhile." (p. 120). Funding: "I am grateful to the Format International Ltd. and NAIS for their financial support." (thesis p. 7). Supervisors: Hall, and Gondzio as second supervisor | [stated] P |
| Why then | As in 2.1. On development style he writes that "using C++ provides the opportunity of an evolutionary development process, from a proof-of-idea prototype with simple but less efficient data structures to an efficient elaborated implementation." (thesis p. 17) | [stated] P |
| Key insight | **A serial solver kept simple on purpose, but efficient.** It has Suhl–Suhl LU, hyper-sparse solves, the Forrest–Tomlin update, DSE, BFRT, the Harris ratio test and cost perturbation, so that parallel schemes can be layered on top: "In this research, it has been intended to keep the serial implementation simple so that parallelization can be relatively easily designed and implemented." (thesis p. 94). **A side discovery:** "The application of cost perturbation leads to the discovery of a phenomenon called hyper-sparsity promotion." (thesis p. 16) | [stated] P |
| Minimum evidence | **Serial benchmark.** The techniques "lead to serial performance which is comparable with one of the best public domain simplex solvers" (thesis p. 16). The baselines were "Cplex 12.4" and "Clp 1.14" (p. 18), on a 30-problem reference set mostly taken from Mittelmann's list. **Hyper-sparsity promotion.** "After the DSE and BFRT components were implemented in ParISS, cost perturbation was introduced with the aim of mitigating the effects of dual degeneracy." (W3 PDF p. 2). On the NETGEN set, "The total iteration count over the 50 problems reduced by 5%, but the total solution time reduced by 36%." For netgen108, "Cost perturbation reduced the iteration count by 10% but improved the solution time by a factor of 2.2!" (W3 PDF p. 3) | [stated] [practice] P |
| Abandoned paths | **Hyper-sparsity promotion (partial CHUZR, LiDSE) was left unfinished.** "The LiDSE approach has been found very successful for certain families of LP problems." (thesis p. 93), yet "Although the investigation into hyper-sparsity promotion though led to the successful LiDSE approach, it still at an initial stage." (p. 94). Its only other output is the APMOD 2012 abstract; no journal paper was found [inferred from absence]. **Serial polish was deferred:** "but in HSOL, a BFRT is still performed to keep using the same software procedure." (p. 94) | [stated] P; [inferred] |
| Reception | **The code's lineage, in other people's words.** HSOL 1.0 README: "HSOL was originally written by Qi Huangfu, with features such as presolve, crash and advanced basis start added by Julian Hall and Ivet Galabova." (S35). HiGHS README: "HiGHS has primal and dual revised simplex solvers, originally written by Qi Huangfu and further developed by Julian Hall." (S37). Hall's homepage says HiGHS is "based on solvers written by Leona Gottwald and former PhD students Michael Feldmeier and Qi Huangfu" (S30). Hall's 2016 slides list hsol's limitations: "Limitations No presolve No crash No advanced basis start" (S23 slide 36). **Authorship rests on the README.** The surviving public h2gmp history (94 commits from 2017-07-06, by Galabova, Hall and Miltenberger) contains no commit by Huangfu. The core files (HDual.cpp, HDualMulti.cpp, HFactor.cpp) carry no author header, while HCrash.cpp says "Author: Julian", created 20 Oct 2016 [practice]. **Citations:** the thesis has 6 in S2 | [observed] P; [practice] P |
| Method it shows | PM1 efficient baseline first, owned from scratch. PM7 an anomaly explained on a tractable subclass: "Initial experiments were carried out using the NETGEN [7] network LP problems since they are known to be hyper-sparse and their algebraic properties when solved using the simplex method permit a level of analysis that is intractable in more general LP problems." (W3 PDF p. 3). Learning from other people's code: "Although the Authors know of no published reference to this technique, it is used within Clp" (W3 PDF p. 5, on partial CHUZR). An evolutionary path from prototype to elaborated implementation | [inferred] |

### 2.4 Turning point 1 · The FICO Xpress parallel dual simplex (2014)

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin | Not documented. [inferred] He joined FICO between the July 2013 thesis and the May 2014 blog post | [inferred] |
| Why then | Not documented beyond the blog's framing that, after hyper-sparsity, "the simplex world has been relatively quiet" while parallelisation stayed active (S16) | [stated] P |
| Key insight (his words) | "A meaningful simplex parallelization has to be designed and developed based on a state-of-the-art sequential simplex solver and still allow for significant parallelization." "The implementation in our optimization suite is an adaption and further development of this key idea." (S16) | [stated] P |
| Minimum evidence | "As the first commercial parallel simplex solver, it achieves speedup to a factor of two on various large-scale problems." (S16, 13 May 2014). W7 Fig. 5 profiles Cplex, Xpress and Xpress with 8 threads, all with preprocessing and crash (p. 140) | [stated] P; [stated, joint] P |
| Abandoned paths | Not found | — |
| Reception | Only the authors' own claims are available (W7 pp. 140–141; slides from 2015 to 2017). The Xpress version that first shipped the feature was not identified | [stated, joint] P |
| Method it shows | PM8 transfer into production code | [inferred] |

### 2.5 Turning point 2 · Cardinal Operations and COPT (by 2022)

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin, why then | The date he joined and his reasons were not found. The talk dates the company's solver work: "In the past three years, since 2019, we have introduced many mathematical solvers and functionalities." (S47, caption transcript) | [stated] P; gap |
| Record | **Bio.** JuliaCon 2022: "Qi Huangfu is the developer of COPT and has worked on many different optimization solvers, including HiGHS and FICO-Xpress." (S21). Who wrote the bio is not stated; on pretalx it is normally the speaker. **The talk itself (S47).** "My name is Huangfu Qi, I am one of COPT developer." On the simplex solver: "in our experience, the simplex solver is very suitable for large and sparse LP problems and it is necessary for solving LP relaxations" in the MIP solver, and "we have full parallelization in the simplex solver and we also support Quad-precision which can help to deal with very numerically hard instances." Yardstick and forecast: "According to the public benchmark, COPT is leading on many categories and we are catching up on the important MIP benchmark." and "But if we can reproduce the same improvement as we've done in the past year, maybe by the mid of next year, 2023, we will be the best." This forecast was not checked against Mittelmann's later results; it is a lead for agent 05. A team publication is mentioned without a title: "during our development, we also found that there is a technique to reduce the support of solutions and we published that on arXiv already." It was not identified, and it is not among the two arXiv papers under his name. **Self-presentation.** [inferred] He presents himself through solvers and public benchmarks, not papers. **Product scope.** COPT guide v1 (Ver 5.0.4, 30 Aug 2022) lists dual simplex and barrier as the LP algorithms (S19, Table 1.1). **cuPDLP-C (W10).** The report compares a C/CUDA PDLP implementation with COPT's interior-point optimizer, running COPT on an AMD Ryzen 9 5900X and cuPDLP-C on an NVIDIA H100 (S20 pp. 1–2). His role is not stated, and he has no commits in the public repository (S39) | [stated] P; [practice] P; [inferred] |
| Context | In 2010–2011 Hall's group judged GPU standard simplex "Not (really) of practical value but a good learning exercise" (S24 slide 56) with "No hope of beating serial solvers on sparse LP problems" (S26 slide 16). W10 (2023) is a GPU first-order method, not a simplex method, so this is no contradiction. It does show the GPU question returning for LP with a different algorithm [inferred] | [observed] P; [inferred] |
| Abandoned paths, reception | Not found. W9 has 67 citations in S2, mostly as COPT's requested citation (§1.8) | gap; [observed] |
| Method it shows | None can be attributed to him individually | gap |

---

## 3. Failures, slowdowns, abandoned directions (consolidated)

1. **ParISS, 2011** (W2 pp. 5–6). 14 of 30 problems failed in at least one run, 3 more were discarded as more than ten times slower than Clp, and serial runs were 2.7 times slower than Clp on average. [practice] P
2. **PAMI slowdowns** (W7 p. 138). On maros-r7 and Linf_520c, pami is slower in parallel than hsol, and serial pami is slower than hsol by factors of 3.48 and 2.75. On the two best problems the speed-up is "flattered": "For the two problems where pami performs best in parallel, it is flattered by requiring significantly fewer iterations than hsol." The authors therefore rescale those speed-ups (2.58 and 2.33) by the relative iteration counts, to 1.74 and 1.75 (p. 138). Thesis: on Linf 520c "PAMI solved 25% slower than the sequential solver" (p. 94). [practice] P
3. **SIP slowdowns on hyper-sparse problems**, e.g. sgpf5y6, where FTRAN-DSE takes over 80% of the time (W7 p. 139). [practice] P
4. **APF is "not recommended as a valuable general technique"** (W5 report p. 17). [stated, joint] P
5. **The GPU line was dropped.** APF was proposed "for GPU extension" (2010) and a "planned CPU+GPU implementation of dual simplex with suboptimization" was announced (2011); no follow-up was found. [practice] P + [inferred]
6. **Hyper-sparsity promotion (LiDSE, partial CHUZR)** never reached a journal paper. [inferred]
7. **Overlapping INVERT** stayed future work (thesis p. 94). [stated] P
8. **Self-assessment of the results.**
   - Thesis (p. 94): "Though not extremely impressive, the performance of PAMI is comparable to the dual simplex implementation of Cplex, which is a world-leading commercial simplex solver."
   - W7 (p. 140): "Although the results in this paper are far from the linear speedup which is the hallmark of many quality parallel implementations of algorithms, to expect such results for an efficient implementation of the revised simplex method applied to general large sparse LP problems is unreasonable."
   - W7 (p. 140), on why: "The commercial value of efficient simplex implementations is such that if such linear speedup were possible then it would have been achieved years ago." [stated] P
9. **Rejected or withdrawn papers**: none in the public record. The 22-month gap between W7's acceptance and its online publication is unexplained. [gap]

---

## 4. Era and resource context

| Period | Compute | Tools and baselines | Team | Seniority |
|---|---|---|---|---|
| 2010–2011 (ParISS) | dual quad-core AMD Opteron 2378, 8 cores (S25; W2 p. 5) | C++, OpenMP, Intel C++ compiler; Netlib and Kennington test sets; Clp 1.06 | PhD student and supervisor. A fellow student (Smith) worked on GPU and block-angular simplex in the same group (S24–S26) | first PhD years |
| 2013 (thesis) | "It is a workstation with 16 (Intel Xeon E5620, 2.4GHz) cores." (thesis p. 17) | Intel C++ 13.0, OpenMP 3.1; Cplex 12.4 and Clp 1.14; a 30-problem reference set mostly from Mittelmann's list | same; industrial funding (Format International Ltd., NAIS) | PhD |
| 2014–2017 (W7, Xpress) | W7: "two Intel Xeon E5-2670s, 2.6 GHz (16 cores, 16 threads in total), using eight threads for the parallel calculations" (p. 133) | Clp 1.15, called "the world's leading open-source solver" (p. 134); Cplex 12.4; W7 runs without preprocessing or crash; the Xpress commercial code base | FICO development team (size unknown) for Xpress; Hall for the publication | early-career industry developer |
| 2016–2017 (hsol testing in Hall's slides) | not stated | 159 problems (98 Netlib, 16 Kennington, 4 industrial, 41 Mittelmann); clp 1.16, cplex 12.5 (S23 slide 37; S28 slide 9) | Hall and Galabova in Edinburgh; Huangfu listed as FICO | — |
| 2022–2024 (COPT, cuPDLP-C) | NVIDIA H100 80GB for cuPDLP-C; COPT on an AMD Ryzen 9 5900X with 512 GB (S20) | COPT; CUDA C; report funded by NSFC grants (S20 p. 1) | company team plus academic co-authors (SUFE, Chicago, Stanford) | senior industry developer [inferred] |

---

## 5. Pointers into the seven layers (candidate evidence for Phase 2, not conclusions)

- **Layer 1, taste.**
  - "for novel computational developments to be of value they must be tested within an efficient implementation or good reasons given why they are applicable in such an environment. Any development which is only effective in the context of an inefficient implementation is not worthy of attention." (W7 p. 121; the same text is in the 2015 report ERGO-14-011).
  - From the blog: "good speedup ratios are related to less efficient sequential implementations of the simplex method." (S16).
  - Negative selection: dense-algebra parallelism "is excluded" (thesis p. 75).
  - Tagged [stated, joint] / [stated]. This is the strongest repeated criterion, appearing in 4 sources: W2 p. 5, thesis pp. 15–16, S16 and W7 pp. 120–121.
- **Layer 2, problem choice.** A gap in prior work (Bixby–Martin lacked BFRT and hyper-sparsity) plus a hardware shift (multi-core desktops) gave the "why now" (W7 p. 120; thesis p. 15). The suboptimization agenda was already in the supervisor's 2010 programme (S24) [observed].
- **Layer 3, idea generation.** Reviving a forgotten device ("relatively unknown pivoting strategy", W7 p. 119; Rosander 1975). Algebraic re-placement of a factor ("Why not take it out on the right!", S29). Following an anomaly: cost perturbation led to hyper-sparsity promotion (W3; thesis p. 16).
- **Layer 4, experiment and execution.**
  - Building one's own solver from scratch, starting with an evolutionary prototype (thesis pp. 16–17).
  - Profiling plus Amdahl's law to bound the attainable speed-up (thesis §4.2, pp. 75–76).
  - Controlled replay of the same basis sequence (W5 p. 15).
  - A 21-value parameter sweep, choosing the median of the flat region rather than the best value: "any value in interval [0.9, 0.999] can be chosen as the cutoff ratio" (thesis p. 85); 0.95 was chosen although 0.94 gave the highest mean (1.56, Table 4.4).
  - Public test sets and named baseline versions; raw data deposited (W6).
- **Layer 5, judging results.**
  - Reporting the failures and the filtering steps (W2).
  - Correcting a "flattered" speed-up by iteration counts (W7 p. 138).
  - Valuing the parallel scheme only if serial efficiency survives: "A high degree of parallel efficiency would be of little value if it came at the cost of severe serial inefficiency." (W7 p. 134).
  - Declining to oversell: "Though not extremely impressive" (thesis p. 94); comparing with commercial codes only with a caveat: "Since commercial LP solvers are now highly developed it is, perhaps, unreasonable to compare their performance with a research code." (W7 p. 139).
- **Layer 6, expression.**
  - Papers run background → design → results → conclusions, with performance profiles (W7 Figs. 3–5) and per-iteration timelines ("Real time behaviour", thesis §4.3.7, §4.4.3; W7 §5).
  - The thesis abstract and the blog restate one key idea in one sentence.
  - Preprints were posted the day the paper was submitted: arXiv 1503.01889 and W7 receipt both on 6 Mar 2015.
  - Benchmark data and test problems were made public (W6; HuHa13_TestSet.zip on S33).
- **Layer 7, research organisation.**
  - A PhD with industrial funding (thesis p. 7) and a supervisor who acted as corresponding author throughout.
  - The results moved into a commercial code (Xpress) while the academic code went back to the supervisor's group (HSOL to HiGHS).
  - Later work was credited as team authorship in industry.
  - No students documented.
  - The supervisor's observation: "Helped develop two really talented young researchers: Qi Huangfu and Miles Lubin" (S22 slide 43) [observed].

Candidate method labels used above (for Phase 2 verification across agents 02–06):
- PM1 efficient baseline first, owned from scratch
- PM2 bound the speed-up before building (profiling plus Amdahl)
- PM3 revive an under-used classical device and pay its price explicitly
- PM4 re-factor the algebra for implementation simplicity
- PM5 controlled replay and robust parameter choice
- PM6 honest accounting of failures and flattering effects
- PM7 explain an anomaly on a tractable subclass
- PM8 transfer into production code
- PM9 a complementary fallback scheme

---

## Contradictions (kept, not reconciled)

1. **What PAMI is benchmarked against.**
   - Thesis abstract (p. 3, 2013): "The performance of PAMI is comparable to a world-leading commercial simplex solver."
   - W7 abstract (p. 119): "Computational results show that the performance of PAMI is superior to that of the leading open-source simplex solver".
   - In W7 itself, only "the performance of the better of sip and pami is comparable with that of Cplex" (p. 139).
2. **The headline numbers differ between thesis and paper.**
   - PAMI's mean speed-up over the serial solver: "For the reference set, PAMI provides an average speedup of 1.49." (thesis p. 94) vs "pami provides a mean speedup of 1.51 which enables it to out-perform Clp, the best open-source simplex solver." (W7 p. 140).
   - SIP: "Though the average speedup, 1.13, is worse than that of PAMI" (thesis p. 94) vs "Although its mean speedup of 1.15 is worse than that of pami" (W7 p. 140).
   - PAMI over its own serial version: "with an average of 2.23" (thesis p. 86) vs "with a mean speedup of 2.34" (W7 p. 138).
   - The hardware (16-core Xeon E5620 vs two Xeon E5-2670) and the Clp version (1.14 vs 1.15) also differ. [inferred] The experiments were re-run; neither text says so.
3. **Where PAMI does well.**
   - Thesis (p. 86): "It is worth noting that the instances with better speedup (greater than the average) are more associated with the relatively dense LP problems".
   - W7 (p. 138): "Interestingly, there is no real relation between the performance of pami and problem hyper-sparsity".
4. **ParISS and hsol.**
   - The APMOD abstract (W3 PDF p. 1, Mar 2012) says "ParISS is a highly efficient dual revised simplex solver [2] developed by the Authors".
   - The thesis (p. 16) and W7 (p. 120) say hsol was implemented "from scratch".
   - Whether hsol is ParISS renamed and evolved, or a rewrite, is not stated.
5. **Credit for the prototype.** Hall's slides credit Huangfu alone ("Written by Qi Huangfu (2010)", S25 slide 23; "Written by Huangfu (2010)", S26 slide 21). The papers credit "the Authors" (W3) and put Hall first (W2).
6. **Names of the techniques.**
   - PAMI is "parallelism across multiple iterations" in the thesis and W7, but "parallel minor iterations" in the HSOL 1.0 README: "exploiting parallelism using either "parallel minor iterations" (PAMI) or "single iteration parallelism" (SIP)" (S35).
   - APF is the "alternate product form" in the thesis and W5, but the "Alternative product form" on the 2010–2017 slides.
7. **Priority claims.**
   - The blog: "As the first commercial parallel simplex solver" (S16).
   - W7: "In developing the first parallel revised simplex solver of general utility" (p. 119).
   - W7 itself cites Bixby and Martin (2000) as earlier dual simplex parallelisation and says Cplex "(which has no parallel simplex facility)" (p. 140). The priority claims were not checked independently.
8. **Size of the speed-up.** The blog says "speedup to a factor of two on various large-scale problems" for Xpress. The academic PAMI shows a mean of about 1.5 over hsol. The code bases and baselines differ.
9. **Bibliographic details.**
   - COAP issue: 60(3) in Crossref, DBLP and Hall's publication page; "60(4):587-608" on Hall's slides (S22 slide 44; S23 slide 42).
   - Prize article (W8): 65(3):541–544 per Crossref and Springer; "65 (1), 1-4" per Hall's publication page. Crossref lists no authors; Hall's page credits Huangfu and Hall.
   - ERGO-13-001: a 28 Jan 2013 version (cited in Glop as "ERGO-13-0001") and a 7 July 2013 version (the PDF on Hall's site).
   - Optimization Online lists Hall before Huangfu for both W5 and W7, while the reports put Huangfu first.
10. **Record counts.** DBLP has 5 records. Semantic Scholar's merged profile has 17 items, of which 11 concern this researcher (2 of them with identity inferred).
11. **His role in COPT.** The JuliaCon 2022 bio says "Qi Huangfu is the developer of COPT" (S21). In the talk itself he says "I am one of COPT developer." (S47, caption transcript).

## Gaps

- **Profiles.** Google Scholar redirects to a login page, so no profile was found or used. OpenAlex was not queried (no key). No homepage, CV or ORCID was found for this researcher.
- **Early years.** Education before Edinburgh is unknown. The PhD start date is unknown; his first appearance on slides is 14 Sep 2010. The 2008 FE–FV item is unverified, and the identity behind W1 (2009) is unconfirmed.
- **FICO period.** Start and end dates at FICO are unknown. The Xpress version that first shipped the parallel dual simplex was not identified, and FICO release notes were not checked.
- **COPT period.** The date he joined Cardinal Operations is unknown, and so is COPT's first release. One WebSearch gave no dated answer, and the COPT-Release repository starts at COPT 4.0 (created 2022-04-29). The only dating is his "since 2019" in the 2022 talk (S47). The COPT-team arXiv paper on reducing solution support that he mentions was not identified.
- **Individual contributions** inside COPT (simplex? barrier? MIP?) and inside cuPDLP-C are not documented in any source found.
- **The COAP 2015 prize article (W8)** is paywalled and was not read. It probably holds the authors' own account of where the update techniques came from.
- **Review history.** The reason for W7's 22-month gap between acceptance and publication was not found. No referee reports, rejections or retractions are public.
- **Unretrieved material.**
  - The JuliaCon 2022 video was not watched. Its uploaded caption transcript (S47, saved by agent 02) was read; the captions are not speaker-checked, and the slides shown in the talk were not seen.
  - Mittelmann's 2015 benchmark pages.
  - The DataShare spreadsheet HsolNov14-17.xlsx (left for the process-evidence agent).
- **Partly read texts.** The thesis was read selectively: chapters 2–3 and §4.1 mostly not read. W7 §§2–4 were not read in full, and the published COAP version was not read.
- **Talk presenters.** The presenter of each co-listed talk is unknown except for T-e (Hall) and T-h (probably Hall, inferred).
- **Patents** were not searched.

## Sources

Primary = the researcher's own texts, code and records, a collaborator's first-hand pages and slides, or third-party code. Secondary = indexes and search results. All fetched 2026-10-27.

- S1. DBLP person record "Qi Huangfu", pid 116/5281 (via sparql.dblp.org, `scripts/dblp_works.py`), 5 records. https://dblp.org/pid/116/5281.html. Secondary.
- S2. Semantic Scholar Graph API: author search "Qi Huangfu"; authors 2513024303, 2841156 and 2056477171; paper batch details. https://api.semanticscholar.org/graph/v1/. Secondary.
- S3. Crossref REST API records for 10.1007/978-3-642-31464-3_15, 10.1007/s10589-014-9689-1, 10.1007/s12532-017-0130-5, 10.1007/s10589-016-9882-5 and 10.2118/118924-MS. https://api.crossref.org/works/. Secondary.
- S4. arXiv author searches "Huangfu, Qi" and "Huangfu". https://arxiv.org/search/?query=Huangfu&searchtype=author. Secondary.
- S5. arXiv abstract page and submission history of 2208.14314. https://arxiv.org/abs/2208.14314. Secondary.
- S6. ORCID public search, family-name Huangfu and given-names Qi (one hit, Zhejiang University). https://pub.orcid.org/v3.0/expanded-search/. Secondary.
- S7. Google Scholar author search "Qi Huangfu": redirected to a login page, not used. https://scholar.google.com/citations?view_op=search_authors&mauthors=Qi+Huangfu. Secondary.
- S8. Huangfu, Q., "High performance simplex solver", PhD thesis, University of Edinburgh, 2013. hdl:1842/7952, https://era.ed.ac.uk/handle/1842/7952. Primary.
- S9. Hall, J. A. J. and Huangfu, Q., "A high performance dual revised simplex solver", ERGO-11-007 (12 May 2011); PPAM 2011, LNCS 7203:143–151 (2012). DOI 10.1007/978-3-642-31464-3_15; https://webhomes.maths.ed.ac.uk/hall/HaHu11/ERGO-11-007.pdf. Primary.
- S10. Huangfu, Q. and Hall, J. A. J., "Novel update techniques for the revised simplex method", ERGO-13-001 (7 July 2013); COAP 60(3):587–608 (2015). DOI 10.1007/s10589-014-9689-1; https://webhomes.maths.ed.ac.uk/hall/HuHa12/ERGO-13-001.pdf. Primary.
- S11. Huangfu, Q. and Hall, J. A. J., "Parallelizing the dual revised simplex method", Math. Prog. Comp. 10(1):119–142 (2018), CC BY 4.0. DOI 10.1007/s12532-017-0130-5; https://webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf. Primary.
- S12. The same paper as ERGO-14-011, dated 6 Mar 2015, and arXiv 1503.01889. https://webhomes.maths.ed.ac.uk/hall/HuHa13/ERGO-14-011.pdf. Primary.
- S13. Hall, J. A. J. and Huangfu, Q., "Promoting hyper-sparsity in the revised simplex method", APMOD 2012 extended abstract, 29 Mar 2012. https://webhomes.maths.ed.ac.uk/hall/APMOD12/APMOD12_ExtendedAbstract.pdf. Primary.
- S14. Huangfu, Q. and Hall, J. A. J., "Parallel simplex benchmarking results" [dataset], Edinburgh DataShare, 23 Dec 2014. DOI 10.7488/ds/196 (https://hdl.handle.net/10283/680). Primary.
- S15. "COAP 2015 Best Paper Prize", COAP 65:541–544 (2016). DOI 10.1007/s10589-016-9882-5; only the landing page and reference list were read. Primary (text not read).
- S16. Huangfu, Q., "The Algorithm that Runs the World", FICO Blog, 13 May 2014; Wayback copy of 27 Jan 2015. https://web.archive.org/web/20150127063109/http://www.fico.com/en/blogs/analytics-optimization/the-algorithm-that-runs-the-world/. Primary.
- S17. FICO Blog author page "Qi Huangfu" (one post), Wayback copy of 29 Jun 2018. https://web.archive.org/web/20180629070334/http://www.fico.com:80/en/blogs/author/qi-huangfu/. Secondary.
- S18. Geiger, S., Huangfu, Q., Reid, F., Matthäi, S., Coumou, D., Belayneh, M., Fricke, C., Schmid, K., "Massively Parallel Sector Scale Discrete Fracture and Matrix Simulations", SPE Reservoir Simulation Symposium, Feb 2009. DOI 10.2118/118924-MS; Crossref metadata only. Primary (not read; identity inferred).
- S19. Ge, D., Huangfu, Q., Wang, Z., Wu, J., Ye, Y., "Cardinal Optimizer (COPT) User Guide", arXiv 2208.14314, v1 30 Aug 2022 (read) to v4 30 Jan 2026. https://arxiv.org/pdf/2208.14314v1. Primary.
- S20. Lu, H., Yang, J., Hu, H., Huangfu, Q., Liu, J., Liu, T., Ye, Y., Zhang, C., Ge, D., "cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language", arXiv 2312.14832v2, 7 Jan 2024. https://arxiv.org/pdf/2312.14832v2. Primary.
- S21. JuliaCon 2022, "COPT and its Julia interface" (Qi Huangfu, 27 Jul 2022), talk and speaker pages. https://pretalx.com/juliacon-2022/talk/XRDNVT/ and https://pretalx.com/juliacon-2022/speaker/ZF7V93/. Primary.
- S22. Hall, J., Huangfu, Q., Lubin, M., "High performance simplex solvers for linear programming problems", Google, Paris, 11 Sep 2015 (slides). https://webhomes.maths.ed.ac.uk/hall/Google15/Google15.pdf. Primary (collaborator).
- S23. Huangfu, Q., Hall, J., "Novel update techniques for the revised simplex method (and their application)", ERGO seminar, 30 Nov 2016 (page and slides). https://webhomes.maths.ed.ac.uk/hall/ERGO_301116/. Primary.
- S24. Hall, J., Smith, E., Huangfu Qi, "Towards a practical parallelisation of the revised simplex method", IMA-NLAO, 14 Sep 2010 (slides). https://webhomes.maths.ed.ac.uk/hall/IMA-NLAO_10/IMA-NLAO_10.pdf. Primary (collaborator).
- S25. Hall, J., Huangfu, Q., Smith, E., "A high performance dual revised simplex solver", RAL10, 2 Dec 2010 (slides). https://webhomes.maths.ed.ac.uk/hall/RAL10/RAL10.pdf. Primary (collaborator).
- S26. Hall, J., Huangfu, Q., Smith, E., "High performance computing and the simplex method", Lancs11, 12 Apr 2011 (slides). https://webhomes.maths.ed.ac.uk/hall/Lancs11/Lancs11.pdf. Primary (collaborator).
- S27. Hall, J. A. J., Huangfu, Q., "A high performance dual revised simplex solver", PPAM 2011 talk, 13 Sep 2011 (slides). https://webhomes.maths.ed.ac.uk/hall/PPAM11/PPAM11.pdf. Primary.
- S28. Hall, J., Huangfu, Q., Galabova, I., "An open-source high performance dual simplex solver", SIAM Conference on Optimization, 22 May 2017 (slides). https://webhomes.maths.ed.ac.uk/hall/SIOPT17/SIOPT17.pdf. Primary.
- S29. Huangfu, Q., Hall, J., "Novel update techniques for the revised simplex method", EUROPT 2017, 13 Jul 2017 (slides). https://webhomes.maths.ed.ac.uk/hall/EUROPT17/EUROPT17.pdf. Primary.
- S30. Julian Hall, homepage (the HiGHS attribution). https://webhomes.maths.ed.ac.uk/hall/. Primary (collaborator).
- S31. Julian Hall, Publications page. https://webhomes.maths.ed.ac.uk/hall/Publications.html. Primary (collaborator).
- S32. Julian Hall, Prizes page. https://webhomes.maths.ed.ac.uk/hall/Prizes. Primary (collaborator).
- S33. Julian Hall, per-paper pages HuHa13/, HuHa12/, HaHu11/ and COAP_Prize_2015/. https://webhomes.maths.ed.ac.uk/hall/HuHa13/ (and siblings). Primary (collaborator).
- S34. Optimization Online author page "Q. Huangfu", and the entry "Novel update techniques for the revised simplex method" (14 Feb 2013). https://optimization-online.org/author/qi-huangfu/ and http://www.optimization-online.org/DB_HTML/2013/02/3774.html. Secondary.
- S35. HSOL 1.0 README, sources and commit history, GitHub mattmilten/h2gmp (created 2017-10-11; head d1472d1e92 of 2018-03-23). https://github.com/mattmilten/h2gmp. Primary (code).
- S36. GitHub galabovaa/h2gmp: HTTP 404 on 2026-10-27. https://github.com/galabovaa/h2gmp. Secondary (unavailable).
- S37. HiGHS README and repository metadata, ERGO-Code/HiGHS master branch (MIT; created 2018-03-27). https://github.com/ERGO-Code/HiGHS. Primary.
- S38. Google OR-Tools, `ortools/glop/basis_representation.h`, stable branch, lines 325–329. The last commit touching the file is b4b226801bebda9fdbdac8b53d905c8da6dbb143 (2025-11-05). https://github.com/google/or-tools/blob/stable/ortools/glop/basis_representation.h. Primary (third-party code).
- S39. GitHub COPT-Public/cuPDLP-C: contributors and commits, 2023-12-12 to 2026-10-02. https://github.com/COPT-Public/cuPDLP-C. Primary (code record).
- S40. GitHub COPT-Public/COPT-Release: README with the COPT 8.0 release notes; repository created 2022-04-29. https://github.com/COPT-Public/COPT-Release. Primary (company).
- S41. COPT online user guide, "Introduction" (citation entry). https://guide.coap.online/copt/en-doc/intro.html. Primary (company).
- S42. W. Hager, COAP best paper page (no mention of Huangfu found). http://clas.ufl.edu/users/hager/coap/Best/. Secondary.
- S43. WebSearch: "Optimization of a large-scale parallel finite element" Huangfu, EPCC MSc 2008. No match. Secondary.
- S44. WebSearch: "Qi Huangfu" simplex, COPT, Cardinal Optimizer, talks. Leads: S21, S23, a résumé (S46) and a third-party author page. Secondary.
- S45. WebSearch: COPT first release, 2019. No dated first release found. Secondary.
- S46. A student's public résumé surfaced by S44. Checked; it does not mention Huangfu, so the lead was discarded. URL omitted (a third-party personal page unrelated to the researcher). Secondary.
- S47. "COPT and its Julia interface", caption transcript, Qi Huangfu, JuliaCon 2022, 27 Jul 2022. Uploaded en-US subtitle track of https://www.youtube.com/watch?v=iqiBXoJQVD8, saved by agent 02 at `references/sources/talks/juliacon-2022-copt-and-its-julia-interface.transcript.txt`. Primary (caption text, not speaker-checked).
