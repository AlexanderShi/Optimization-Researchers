# Qi Huangfu: research trajectory (research agent 06)

- **Researcher**: Qi Huangfu (皇甫琦). LP solver developer. MSc in High Performance Computing, University of Edinburgh, 2008. PhD, University of Edinburgh, 2013, thesis "High performance simplex solver", supervisors J. A. J. (Julian) Hall and Jacek Gondzio (second supervisor). He then worked on the FICO Xpress simplex solver (first dated evidence May 2014, last dated evidence July 2017), and then at Cardinal Operations (杉数科技) on the COPT solver, where he was "副总裁" (vice president) in August 2021. Living. **Not** the Qi Huangfu of the Second Affiliated Hospital of Zhejiang University (urology and biomaterials papers), with whom OpenAlex merges him (see Contradictions).
- **Dimension**: research trajectory. This covers the dated timeline, lineage, the turns in direction and what triggered them, when he enters and leaves topics, the resource context of each era, failures and abandoned lines, and the last 12 months. It serves framework layer 2 (problem choice and timing) and layer 7 (research organisation), with pointers for layers 1, 3, 4 and 5.
- **Research date**: 2026-10-27
- **Sources consulted**: 52 external sources (38 primary, 14 secondary), listed at the end, plus one sibling note in this repo used only as a lead. **WebSearch calls used: 5** (of 5 allowed).
- **Local corpus**: `references/sources/papers/`, `essays/`, `software/` and `publications/` hold only `.gitkeep`. **Nothing below is from user-supplied material.** During this run a sibling agent saved `talks/juliacon-2022-copt-and-its-julia-interface.transcript.txt`. It is the uploaded (non-automatic) caption track of Huangfu's JuliaCon 2022 talk. I read it, and checked the video's identity myself (YouTube oEmbed: "COPT and Its Julia interface | Qi Huangfu | JuliaCon 2022", channel The Julia Programming Language). Quotes from it are caption text, not speaker-checked. `private/` was not opened.
- **Sibling notes**: notes 01–05 for this member did not exist when this note was written. The nonlinear-team note on Roger Fletcher (`product/nonlinear-team/roger-fletcher/references/research/06-trajectory.md`) was read only as a lead for Julian Hall's lineage. Everything it suggested was re-checked here on Hall's own homepage.

### How the evidence was gathered (and what failed)

- **DBLP**: `dblp.org` returned the Anubis bot wall. The record for pid 116/5281 came from the DBLP SPARQL endpoint via `scripts/dblp_works.py` (run read-only, output in scratch). It holds 5 records, 2012–2022. It **misses** the cuPDLP-C report (arXiv 2312.14832), and no other DBLP "Qi Huangfu" pid holds it either.
- **arXiv API** (`au:Huangfu_Q`; `all:"Qi Huangfu"`): 3 records of this person: 1503.01889, 2208.14314 and 2312.14832.
- **Full texts read** (all public): the 2008 MSc dissertation; the 2013 PhD thesis; ERGO-11-007, ERGO-13-001 (header and abstract), ERGO-14-011 (header and abstract); the published MPC 2018 article (CC-BY, author-hosted copy); the APMOD 2012 extended abstract; 11 slide decks from Hall's site (2010–2017); cuPDLP-C v2; the front matter and overview of COPT User Guide v1, v3 and v4; Huangfu's 2014 FICO blog post (via the Wayback Machine); the 2021 QbitAI article co-written by Huangfu and Dongdong Ge; and the JuliaCon 2022 caption transcript (see Local corpus).
- **Not read**: the published COAP 2015 article (paywalled; the ERGO-13-001 report was read instead); the PPAM 2011 LNCS chapter (the ERGO-11-007 report was read instead); the COAP 2015 prize note (paywalled preview only); the JuliaCon video itself (the caption transcript was read instead); LinkedIn (behind a login, not attempted).
- **Mathematics Genealogy Project**: the live site has been **offline since 21 October 2026** (its notice cites a PHP vulnerability). The MGP record id 204105 was read from a Wayback Machine snapshot of 2025-05-14. After that the Internet Archive returned HTTP 429 to curl, and WebFetch cannot reach `web.archive.org`.
- **OpenAlex** merges this person with a Zhejiang University medical researcher (author A5074771751). Only three of its works are his: the 2008 MSc, the 2012 PPAM paper and the 2013 thesis. cuPDLP-C and the COPT guide sit on no linked author profile.
- **GitHub**: the API and commit search were used for HiGHS, h2gmp, COPT-Release and COPT.jl. Commit-author emails visible in API payloads are deliberately **not** reproduced here.

### Tag legend

- **[stated]**: Huangfu's own sole-authored or spoken words: the MSc dissertation, the PhD thesis, the FICO blog, and the JuliaCon 2022 talk (caption transcript). The JuliaCon 2022 speaker bio is also tagged [stated], but its authorship is presumed, not verified.
- **[stated-joint]**: words in co-authored text: papers, technical reports, joint slides, and the 2021 QbitAI article with Dongdong Ge. His individual voice cannot be separated in these.
- **[practice]**: what the record shows he did: papers, dates, code, commits, release notes, affiliations.
- **[observed]**: what others report about him: Julian Hall's pages and solo slides, the HiGHS team, Springer, MGP, survey authors, citation counts.
- **[inferred]**: my synthesis. Treat it as a hypothesis.
- **P / S**: primary / secondary source.

---

## 0. The trajectory in one paragraph (all [inferred], built from the sections below)

Huangfu's career is **one technical object carried through three institutions**: a high-performance implementation of the **dual revised simplex method**, built first for parallelism and then for products. He came to it from **HPC, not from optimization**. His 2008 Edinburgh MSc was about porting and partitioning an MPI finite-element/finite-volume code. In 2010 he joined his supervisor Julian Hall's decades-old parallel-simplex agenda, which runs from Hall & McKinnon's PARSMI and ASYNPLEX to hyper-sparsity. He entered it *against* the stated consensus that the revised simplex method was unsuitable for parallelisation. His stated reason was a changed context: dual simplex with DSE and BFRT had become the preferred variant, and every desktop was now multicore. His working rule was to build an excellent serial solver first (ParISS, then hsol) and parallelise only on that base (PAMI, SIP). Within about a year of the PhD (2013) the PAMI ideas were in a commercial product, FICO Xpress (May 2014). He kept publishing with Hall from industry until the 2015 MPC submission. After that, his academic output nearly stops. His code lived on in Edinburgh as HSOL, then h2gmp, then **HiGHS**, whose users are asked to cite his 2018 paper. That request plausibly explains why the paper's citations rise from 2 (2019) to 168 (2026 so far). By 2021 he was a vice president at Cardinal Operations, writing as a **MIP and full-suite** solver developer. COPT already had a CPU first-order LP method by July 2022. In December 2023 he took part in a fast-follower turn to **GPU** first-order LP, about a month after cuPDLP.jl. This reverses a GPU route he had left in 2010–2013, but by a different algorithm class. He has stayed visible mainly through product artefacts: release notes he committed until December 2024, and his co-authorship of the COPT user guide (v4, January 2026). **In the last 12 months, no new paper, talk or move under his own name was found.**

---

## 1. Dated timeline

| Date | Event | Tag | Source |
|---|---|---|---|
| 2007–2008 (dated 22 Aug 2008) | MSc in High Performance Computing, The University of Edinburgh. Dissertation "Optimization of a large-scale parallel finite element - finite volume C++ code". He ported CSMP, a subsurface-flow simulator, to the Ness and ECDF machines and wrote a METIS-based hybrid-mesh partitioner. Acknowledgements: "I would like to thanks my supervisors Dr Fiona Reid and Dr Sebastian Geiger." | [practice] P; [stated] P | MSc dissertation, title page, abstract, acknowledgements |
| 2008–2010 (PhD start not verified) | PhD at Edinburgh, School of Mathematics. The start year is not found. The earliest LP record is Sep 2010 | — | Gap |
| 14 Sep 2010 | First dated LP record. He is co-author with Hall and Edmund Smith of the talk "Towards a practical parallelisation of the revised simplex method", IMA Conference on Numerical Linear Algebra and Optimisation. The slides print the name as "Huangfu Qi" | [practice] P | Hall, Talks page; IMA-NLAO_10 slides |
| 2 Dec 2010 | Talk "A high performance dual revised simplex solver" (Hall, Huangfu, Smith), Oxford CMA seminar at the Rutherford Appleton Laboratory. The prototype slide says: "Written by Qi Huangfu (2010)", "Tested on a dual quad-core AMD Opteron 2378 system", "First run last week!". It "Does not (yet) use" hyper-sparse operations with B⁻¹ or the bound-flipping ratio test | [stated-joint] P | RAL10 slides, slide "Prototype implementation" |
| 12 Apr 2011 | LANCS workshop talk (Hall, Huangfu, Smith). On dual suboptimization: "Dual: New, even in serial". Plan: "Outcome will inform planned CPU+GPU implementation of dual simplex with suboptimization." | [stated-joint] P | Lancs11 slides |
| 12 May 2011 | ERGO-11-007, "A high performance dual revised simplex solver" (Hall & Huangfu). The code is named **ParISS**: "efficient when run in serial and offers modest speed-up" | [practice] P | ERGO-11-007 |
| 13 Sep 2011 → 2012 | Talk at PPAM 2011 ("Average (best) of 18% (50%) relative to 1 core"; "There is scope for parallel simplex"). Paper: Hall & Huangfu, "A High Performance Dual Revised Simplex Solver", PPAM 2011, LNCS 7203, 143–151, 2012, DOI 10.1007/978-3-642-31464-3_15 | [practice] P | PPAM11 slides; DBLP; Crossref |
| 28–29 Mar 2012 | APMOD 2012 talk "Promoting hyper-sparsity in the revised simplex method" (Hall & Huangfu). The extended abstract records the observation that started a sub-line: cost perturbation in ParISS cut pds-10 iterations by about 10% but time by over 60% | [stated-joint] P | APMOD12 extended abstract and slides |
| Feb 2013 / 7 Jul 2013 | ERGO-13-001, "Novel update techniques for the revised simplex method" (Huangfu & Hall). Posted to Optimization Online in Feb 2013 according to Hall's HuHa12 page; that link was not opened. The report version is dated 7 July 2013 and lists both authors at Edinburgh | [practice] P | ERGO-13-001; Hall HuHa12 page |
| 2013-07-01 (deposited 2013-10-22) | PhD, The University of Edinburgh: "High performance simplex solver" (99 pp.). The code is now named **HSOL**. ERA lists Hall and Gondzio as contributors. Funding: "I am grateful to the Format International Ltd. and NAIS for their financial support." | [practice] P; [stated] P | ERA OAI record; thesis p. 7 |
| 23 Aug 2014 online / Apr 2015 print | Huangfu & Hall, "Novel update techniques for the revised simplex method", *Comput. Optim. Appl.* 60(3):587–608, DOI 10.1007/s10589-014-9689-1 | [practice] P | Crossref; DBLP |
| 13 May 2014 | FICO blog post by Huangfu, "The Algorithm that Runs the World". It says the parallel simplex "has been achieved in the most recent version of our optimization suite" (Xpress; version not named) and calls it "the first commercial parallel simplex solver". **First dated evidence of the FICO move** | [stated] P | FICO blog (Wayback snapshot 2017-08-03) |
| 6 Mar 2015 | ERGO-14-011, "Parallelizing the dual revised simplex method", with Huangfu at "FICO House, International Square, Starley Way, Birmingham". Posted the same day to arXiv (1503.01889) and Optimization Online; submitted to MPC the same day | [practice] P | ERGO-14-011; arXiv; MPC "Received: 6 March 2015" |
| 10 Feb 2016 | MPC acceptance | [practice] P | MPC article p. 119 |
| 9 Sep 2016 | NLAO16 talk "Parallelizing the dual revised simplex method" (Qi Huangfu, FICO; Julian Hall). Hall's talks list gives this talk under Hall's name alone, so Hall presumably presented. The slides say "pami ideas incorporated in FICO Xpress (Huangfu 2014)", and the conclusion says the work has "led to publicised advances in a leading commercial solver" | [stated-joint] P | NLAO16 slides; Hall Talks page |
| 1 Nov 2016 | COAP "2015 Best Paper Prize" note, *Comput. Optim. Appl.* 65(3):541–544, DOI 10.1007/s10589-016-9882-5 (not read, paywalled). Hall lists the prize as his and Huangfu's | [observed] S | Crossref; Springer preview; Hall Prizes page |
| 30 Nov 2016 | ERGO seminar, Edinburgh: "Novel update techniques for the revised simplex method (and their application)" (Q. Huangfu, FICO; J. A. J. Hall). Presenter not identified | [practice] P | ERGO_301116 slides; Hall Talks page |
| 16 and 22 May 2017 | Argonne seminar "Three high performance simplex solvers" and SIAM OP17 talk "An open-source high performance dual simplex solver". Both are by Hall, Huangfu (FICO) and Galabova. SIOPT17: "Xpress simplex solver now fastest commercial simplex solver" | [stated-joint] P | Argonne17, SIOPT17 slides |
| 13 Jul 2017 | EUROPT 2017 talk "Novel update techniques for the revised simplex method" (Huangfu, FICO; Hall). The title slide reads "In memory of Roger Fletcher", his academic grandfather. **Last dated evidence of the FICO affiliation** | [practice] P | EUROPT17 slides |
| 14 Aug 2017 | Hall's solo public lecture, Tokyo: "h2gmp (2011-date)", "Work-horse for consultancy" — "Huangfu, H and Galabova (2011-date)" | [observed] P | Tokyo17 slides |
| 11 Oct 2017 | h2gmp copy repository created (mattmilten/h2gmp). README: "Welcome to HSOL 1.0" … "HSOL was originally written by Qi Huangfu, with features such as presolve, crash and advanced basis start added by Julian Hall and Ivet Galabova." No commit by Huangfu among its 94 commits (2017-07-06 to 2018-03-23) | [observed] P; [practice] P | GitHub repo, README.md, commit list |
| 14 Dec 2017 online / Mar 2018 print | Huangfu & Hall, "Parallelizing the dual revised simplex method", *Math. Program. Comput.* 10(1):119–142, DOI 10.1007/s12532-017-0130-5, open access CC-BY. Affiliation: FICO House, Birmingham | [practice] P | MPC article; Crossref |
| 27 Mar 2018 | ERGO-Code/HiGHS repository created. A commit search on 2026-10-27 finds **no commit** under author name "Huangfu" or "Qi" | [practice] P | GitHub API |
| 2018 (print year) | MPC "Outstanding Paper of the Year": "2018 Winner Qi Huangfu, J. A. J. Hall: Parallelizing the dual revised simplex method" | [observed] P | Springer MPC award page |
| 2019 | "COPT, launched by Cardinal Operations in 2019". His joining date is **not verified** | [observed] S | Front. Eng. Manag. survey (2026) |
| 14 Aug 2021 | QbitAI article by "皇甫琦 葛冬冬", written from the COPT team's reading of DeepMind's neural-network MIP paper. Bio: "杉数科技副总裁，博士毕业于爱丁堡大学优化算法方向。" (translation: vice president of Cardinal Operations; PhD in optimization algorithms from the University of Edinburgh). Also: "曾在XPRESS求解器工作多年" (translation: worked on the Xpress solver for many years) | [stated-joint] P | QbitAI article |
| 27–29 Apr 2022 | First public commits as GitHub user `huangfu7` (account created 2022-03-22): COPT.jl README updates and COPT 4.0.7 release notes. COPT-Release has its initial commit on 2022-04-29 | [practice] P | GitHub API |
| 27 Jul 2022 | JuliaCon 2022 lightning talk "COPT and its Julia interface". Bio: "Qi Huangfu is the developer of COPT and has worked on many different optimization solvers, including HiGHS and FICO-Xpress." In the talk (captions): "My name is Huangfu Qi, I am one of COPT developer." He dates the product: "In the past three years, since 2019, we have introduced many mathematical solvers and functionalities." Simplex: "we have full parallelization in the simplex solver and we also support Quad-precision". On the MIP solver: "still in a catching up position", with the prediction "maybe by the mid of next year, 2023, we will be the best" (outcome not verified) | [stated] P | pretalx page; caption transcript in `talks/` |
| 30 Aug 2022 | arXiv 2208.14314v1, *Cardinal Optimizer (COPT) User Guide*, Ver 5.0.4 (D. Ge, Q. Huangfu, Z. Wang, J. Wu, Y. Ye). LP algorithms listed: "Dual simplex; Barrier" | [practice] P | arXiv v1 PDF |
| Oct–Nov 2022 | COPT 6.0 (MISOCP, convex MIQP/MIQCP, Tuner). Cardinal's site: "2022年10月发布求解器COPT6.0版". He committed the 6.0.1 release notes on 2022-11-04 | [practice] P; [observed] S | COPT-Release README-60.md; shanshu.ai/solver |
| 22 Dec 2023 (v2 7 Jan 2024) | arXiv 2312.14832, cuPDLP-C. 4th of 9 authors, affiliation "Cardinal Operations". This came **one month after** cuPDLP.jl (arXiv 2311.12180, 20 Nov 2023, Lu & Yang) | [practice] P | arXiv pages and PDF |
| 18 Feb 2024 | COPT 7.1.0 release notes committed by Qi Huangfu: "Main features of COPT 7.1: COPT first-order LP solver with GPU support" | [practice] P | COPT-Release commit aa44684aac, README-71.md |
| 16 Nov 2024 | arXiv 2208.14314v3, Ver 7.2.1, same five authors | [practice] P | arXiv v3 PDF |
| 6 Dec 2024 | **Last public commit found** under `huangfu7`: COPT 7.2.4 release notes. From Mar 2025 the release notes are committed by the org account `COPT-Public` | [practice] P | COPT-Release commit list |
| 24 Oct 2025 | COPT 8.0.1 README (org account). COPT 8.0.0 "Introduced global nonconvex (MI)QCQP solver" | [practice, team-level] P | COPT-Release README.md |
| 30 Jan 2026 | arXiv 2208.14314v4, Ver 8.0.1. He is still 2nd of 5 authors. LP algorithms: "Simplex, Barrier (CPU/GPU), First-order Method (PDLP)(CPU/GPU)" | [practice] P | arXiv v4 PDF |
| Mar 2026 | A survey by L. Huang, F. Xiao, D. Ge, W. Yin and Z. Liang cites "HiGHS ( Huangfu and Hall, 2018 )" | [observed] S | Front. Eng. Manag. 13(1) |
| 2026-07-01 | HiGHS README (latest commit touching it): "HiGHS has primal and dual revised simplex solvers, originally written by Qi Huangfu and further developed by Julian Hall." | [observed] P | ERGO-Code/HiGHS @ 9d12ffbb |
| 7 Aug and 20 Sep 2026 | COPT 8.0.6 ("Improved performance of the GPU barrier solver. Improved performance of advanced simplex routines.") and 8.0.7. Both committed by the org account | [practice, team-level] P | COPT-Release README.md |
| 2026-10-27 | OpenAlex: MPC 2018 cited 447 times; by year 2019: 2, 2020: 6, 2021: 15, 2022: 16, 2023: 48, 2024: 70, 2025: 117, 2026: 168. The COAP 2015 paper: 11. PPAM 2012: 10 | [observed] S | OpenAlex works API |

---

## 2. Lineage

| Relation | Person | Evidence | Tag |
|---|---|---|---|
| PhD supervisor | **J. A. J. (Julian) Hall**, Edinburgh (MGP id 52149) | Thesis acknowledgements: "I would like to thank my PhD supervisor, Julian Hall for his support and encouragement over the years." ERA contributor. MGP "Advisor 1: Julian Hall". Hall's homepage calls him one of the "former PhD students" | [stated] P; [observed] P/S |
| Second PhD supervisor | **Jacek Gondzio**, Edinburgh | Thesis: "in particular, my second PhD supervisor Jacek Gondzio". ERA contributor. MGP omits him (see Contradictions) | [stated] P |
| Academic grandfather | **Roger Fletcher** (Hall's PhD supervisor, Dundee), a member of this repo's nonlinear-team | Hall's homepage: "(PhD 1992, supervisor Prof. Roger Fletcher )". The EUROPT 2017 talk by Huangfu and Hall is titled "In memory of Roger Fletcher" | [observed] P; [practice] P |
| Inherited agenda | Hall & McKinnon's parallel and hyper-sparse simplex: PARSMI (1996), ASYNPLEX (1998), hyper-sparsity (2005); and Hall's "Towards a practical parallelisation of the simplex method" (*CMS* 2010) | The thesis cites all four and places PAMI against them. **[inferred]** He entered through his supervisor's long-running research programme rather than choosing the topic from outside | [practice] P; [inferred] |
| MSc supervisors | Fiona Reid and Sebastian Geiger | MSc acknowledgements | [stated] P |
| Peers in the group | Edmund Smith (co-author of the 2010–2011 talks; his GPU standard-simplex "i8" and GPU work for a matrix-free IPM appear on those slides); Ivet Galabova (presolve "Galabova (2016)"; HiGHS); later Matthias Miltenberger (build system of h2gmp, 2017) | Slides; h2gmp commits | [practice] P |
| Industrial collaborators | Dongdong Ge (Cardinal Operations co-founder; co-author of the QbitAI article, the COPT guide and cuPDLP-C); Yinyu Ye, Zizhuo Wang, Jian Wu (COPT guide); Haihao Lu, Jinwen Yang and SUFE co-authors (cuPDLP-C) | arXiv 2208.14314; 2312.14832; QbitAI | [practice] P |
| Students | **None known.** MGP snapshot of 2025-05-14: "No students known." No supervision record was found at FICO or Cardinal | MGP | [observed] S |
| Code descendants | ParISS (2011–12) → hsol/HSOL (2013–17) → h2gmp (2017) → HiGHS (2018–). HiGHS asks academic users to cite Huangfu & Hall 2018 | Reports; slides; READMEs; HiGHS docs | [practice] P; [observed] P |

**[inferred]** His descendants, in the lineage sense, are code and citations, not students. The lineage that matters for the skill is method lineage: Fletcher → Hall (sparse active-set and LP linear algebra) → Huangfu (dual simplex, update techniques, parallel suboptimization). After 2013 it continues as an industrial line into Xpress and COPT, while the Edinburgh code line continues without him into HiGHS.

---

## 3. Turns and what triggered them

### T1. HPC → LP solver research (2008 → 2010)

- **What changed**: from porting and partitioning an MPI finite-element/finite-volume code (MSc, 2008) to the parallel dual revised simplex method (first record Sep 2010). [practice] P
- **Trigger**: **no stated reason was found** for choosing simplex. [inferred] The skill set carries over directly: profiling, scaling studies, partitioning, compilers, and parallel environments on Ness and ECDF. His thesis later uses exactly that toolkit: Amdahl's-law analysis and per-component profiling.
- **The PhD's own "why now"** [stated] P, thesis pp. 15–16: "However, the context for simplex parallelization has changed." … "nowadays, when every desktop computer is a multi-core machine, any speedup is desirable in terms of solution time reduction for daily usage. Therefore, the simplex method, especially, the dual revised simplex method deserves renewed parallelization effort."
- The joint slides of 2 Dec 2010 give the same trigger [stated-joint] P: "Moore's law drives core counts per processor, but clock speeds will stabilise"; "Can't wait for faster serial processors or algorithmic improvement"; "Simplex method must try to exploit parallelism".

### T2. Parallel first → serial quality first (2010–2011 → 2012–2013)

- **What changed**: the December 2010 prototype parallelised the dual simplex with suboptimization before it had BFRT or hyper-sparse B⁻¹ solves. ParISS (May 2011) gave "modest speed-up". By 2013 the serial solver, now HSOL, had Suhl–Suhl LU, hyper-sparse FTRAN/BTRAN, the Forrest–Tomlin update, DSE, BFRT and cost perturbation, and PAMI and SIP were built on it. [practice] P. The record does not say whether the 2010 prototype was extended or rewritten; the thesis says HSOL "has been implemented from scratch".
- **Trigger** [stated] P, thesis p. 16: "To achieve a worthwhile simplex parallelization, it should be based on a good sequential simplex solver. Though there are many public domain simplex implementations, they are either too complicated to be extended for parallelization or too simple to be based on. Thus, a sequential dual simplex solver, named HSOL, has been implemented from scratch."
- The same rule recurs in the 2014 blog [stated] P: "A meaningful simplex parallelization has to be designed and developed based on a state-of-the-art sequential simplex solver and still allow for significant parallelization." It also appears in MPC 2018, p. 120 [stated-joint]. **That makes three separate statements, 2013 to 2018, one of them co-authored.**

### T3. Observation-driven side line: hyper-sparsity promotion (2012–2013), then dropped

- **Trigger**: an unexpected measurement. APMOD 2012 extended abstract [stated-joint] P: "Cost perturbation in ParISS was found to be strikingly effective for a range of sparse problems, notably the pds problems [6]. For example, the iteration count for pds-10 was reduced by about 10% but the solution time decreased by over 60%!" The explanation offered: "column perturbation changes the nature of pivot selection so that hyper-sparsity increases."
- **Development**: the thesis (§3.3) turns this into two variants, partial CHUZR and LiDSE. Thesis p. 16 [stated]: "The application of cost perturbation leads to the discovery of a phenomenon called hyper-sparsity promotion."
- **Exit**: thesis p. 94 [stated] (verbatim, grammar as printed): "Although the investigation into hyper-sparsity promotion though led to the successful LiDSE approach, it still at an initial stage." **No later paper on it** appears in DBLP or in Hall's publication list. [inferred] The line was abandoned or left unpublished when he moved to industry.

### T4. GPU considered and dropped (2010–2013)

- **2010–2011 plans** [stated-joint] P. RAL10 lists "Alternative product form update for GPU extension" and a CPU/GPU work-split diagram. Lancs11 says: "Outcome will inform planned CPU+GPU implementation of dual simplex with suboptimization." and "Scope for combined CPU+GPU solver should be explored". The same RAL10 deck, judging Smith's GPU standard simplex: "Not (really) of practical value but a good learning exercise"; "No hope of beating serial solvers on sparse LP problems".
- **2013 verdict** [stated] P, thesis p. 75, on parallel simplex with dense matrix algebra: "Although it has been demonstrated many times that simplex parallelization using dense matrix algebra achieves good speedup, even with the best speedup, it can hardly be comparable to a revised simplex implementation with modern computational enhancements for general LP problems. Therefore, this path is excluded from future consideration."
- **Outcome** [practice] P. The thesis platform is shared-memory CPU only (C++ with OpenMP 3.0 tasks). The alternate product-form update survives, but as a PAMI component on CPUs, not as a GPU vehicle. [inferred] The planned CPU+GPU dual simplex was abandoned. See T8 for the 2023 reversal by a different algorithm class.

### T5. Academia → commercial solver (2013 → 2014)

- **What changed**: from the research code HSOL/PAMI to the FICO Xpress simplex solver. MPC 2018, p. 140 [stated-joint] P: "Since developing and implementing the techniques described in this paper, Huangfu has implemented them within the FICO Xpress simplex solver [15]." Reference [15] is his own blog post.
- **Dating**: between 7 July 2013 (ERGO-13-001 lists Edinburgh) and 13 May 2014 (FICO blog). The exact start date is not verified.
- **Stated framing** [stated] P, blog, 13 May 2014: "As the first commercial parallel simplex solver, it achieves speedup to a factor of two on various large-scale problems." … "The implementation in our optimization suite is an adaption and further development of this key idea." … "After 70 years, we are finally realizing the promise of the algorithm that runs the world."
- **Trigger**: not stated anywhere found. [inferred] There is a value argument in the joint paper, MPC p. 140 [stated-joint] P: "The commercial value of efficient simplex implementations is such that if such linear speedup were possible then it would have been achieved years ago." Commercial uptake is treated as the yardstick of quality, p. 140–141: "they have formed the basis of refinements made by Huangfu to the Xpress solver which have been considered noteworthy enough to be reported by FICO."

### T6. FICO → Cardinal Operations: from component developer to suite builder (between Jul 2017 and Aug 2021)

- **What changed**: from one component (parallel dual simplex) in an established solver to a new full-suite solver, COPT. The earliest guide version found (v5.0.4, 2022; COPT itself dates from 2019) lists the LP algorithms as "Dual simplex; Barrier". By v8.0.1 (2026) the guide lists simplex, CPU/GPU barrier, CPU/GPU PDLP, conic, SDP, NLP and global nonconvex QCQP. [practice] P (product record; his personal share is not separable)
- **Dating**: the move is **not verified**. The last FICO evidence is 13 Jul 2017; the first Cardinal evidence is 14 Aug 2021, as vice president. COPT launched in 2019 [observed] S, and Huangfu himself dates the product's development that way (JuliaCon 2022 [stated] P): "In the past three years, since 2019, we have introduced many mathematical solvers and functionalities." He speaks of "we" and does not date his own arrival. [inferred] A 2017–2019 move is consistent with this, but unconfirmed.
- **Continuity of his own technique**: the same talk says COPT has "full parallelization in the simplex solver" [stated] P. [inferred] The parallel dual simplex line (PAMI → Xpress) carried into COPT, though the talk does not say which scheme COPT uses.
- **Trigger**: no stated reason found. Company context only [observed] S. Jiemian quotes co-founder Ge on the company's choice of in-house development ("从一开始，我们就很注重自主研发"; translation: from the start we put great weight on our own R&D). That is the company's voice, not Huangfu's.

### T7. LP → MIP and ML-in-the-solver (by 2021)

- In August 2021 he writes (jointly with Ge) as a MIP solver developer [stated-joint] P: "作为MIP求解器开发人员，一般不把一定时间内能拿到的Gap作为主要衡量标准。" (translation: as MIP solver developers we do not usually take the gap reached within a fixed time as the main measure). On the accepted standard: "一般来说，根据目前公认的测试标准，一般是在MIPLIB的问题集上，以两小时为限，考虑能求解的问题数量和平均求解时间进行比较。" (translation: MIPLIB, a two-hour limit, number solved and mean time).
- **ML inside the LP solver** [stated-joint] P: "此外我们的线性规划LP求解器开发也得益于机器学习。例如我们对部分有特殊结构的LP使用机器学习的方式，预测一个变量是否在最优解的基解的一部分，并通过小幅的目标函数扰动将这个预测结果应用到LP问题上，实现快速求解。" (translation: for some structured LPs, ML predicts whether a variable is basic at the optimum, and the prediction is applied through a small objective perturbation). [inferred] This re-uses his 2012 lever, objective (cost) perturbation, as the channel that steers pivoting.
- **Judgment on ML hype** [stated-joint] P: ML adds "昂贵（算力资源需求）而有力的武器" (translation: expensive, in compute, but powerful weapons) to two of the six MIP modules, and is "远远谈不上攻破OR" (translation: far from "cracking OR").

### T8. GPU first-order LP: fast-follower turn (Dec 2023 → Feb 2024)

- **Precondition**: first-order LP was already in COPT before the GPU turn. JuliaCon, July 2022 [stated] P: "And that we have this first order method which are very useful for some type of problems." What turned in 2023–24 is the **GPU implementation**, not the adoption of first-order methods as such.
- **Trigger**: an external public result. cuPDLP.jl was posted on 20 Nov 2023 (arXiv 2311.12180) [S]. The cuPDLP-C report with Huangfu as co-author followed on 22 Dec 2023 [practice] P. The COPT 7.1.0 notes he committed on 18 Feb 2024 list "COPT first-order LP solver with GPU support" [practice] P. **Hardware**: "We run COPT on AMD Ryzen 9 5900X with 512GB RAM, whereas the GPU-based cuPDLP-C is tested on NVIDIA H100 80GB." [stated-joint] P
- **Position taken** [stated-joint] P, cuPDLP-C v2, p. 4 and p. 6 (the hardware sentence above is on p. 2): "As interior-point and simplex methods heavily rely on matrix factorization, which is computationally infeasible at this magnitude, cuPDLP currently stands as the only realistic method for finding nearly optimal solutions in such challenging scenarios." And: "GPUs have a revolutionary impact on traditional LP solvers". It also reports against its own product: "Both simplex and barrier methods of COPT fail to provide solutions, while cuPDLP-C efficiently solves all five relaxations."
- **[inferred]** This reverses T4's 2013 exclusion of GPUs, but by a different, matrix-free algorithm. He did not return to GPU simplex. The simplex itself stays in the product: COPT 8.0.6 (Aug 2026) still ships "Improved performance of advanced simplex routines" (team-level record).

### T9. Visibility recedes into product channels (2025–2026)

- Release notes moved from his account to the org account after Dec 2024. He remains a user-guide author through v4 (Jan 2026). No talk, paper or role change under his name was found for 2025–2026. [practice] P; [inferred] This is a workflow change, not evidence of a departure. **Do not read it as a move.**

---

## 4. Entry and exit timing relative to the consensus ([inferred] unless tagged)

| Topic | Entered | Relative to consensus | Left | Evidence |
|---|---|---|---|---|
| Parallel dual revised simplex | 2010 | **Before / against.** His own thesis records the consensus: "Because of the generally poor speedup gained with the revised simplex method, it has been considered not suitable for parallelization." (p. 15, [stated]). The thesis also says the dual had only one published parallelisation, Bixby & Martin (2000) ([stated], p. 15) | Academic exit after the 2015 submission. The work continued in Xpress (2014) and lives on in HiGHS (without him) | Thesis; MPC; slides |
| Suboptimization (multiple CHUZR) | 2010 | **Revival of an old rule** (Orchard-Hays 1968 primal; Rosander 1975 dual), presented as "a less-known dual pivoting rule" (thesis abstract, p. 3) and "Dual: New, even in serial" (Lancs11) | Not left: it is the core of PAMI | Thesis; slides |
| Hyper-sparsity promotion | 2012 (from an observation) | **Own discovery**, no consensus existed | 2013 ("still at an initial stage"); no paper after | APMOD12; thesis |
| GPU for simplex | 2010 (planned) | **With the 2010 GPU wave**, but judged against serial sparse simplex | 2011–2013 (excluded in the thesis) | RAL10, Lancs11; thesis p. 75 |
| Commercial parallel simplex | 2013/14 | **Claimed first.** The 2014 blog says "first commercial parallel simplex solver". The priority claim was not cross-checked against other vendors | ≥ Jul 2017 (FICO affiliation last seen) | Blog; slides |
| Full-suite commercial solver (COPT) | ≤ 2021 (VP), product 2019 | **With a national wave**: the 2026 survey lists COPT (2019), MindOpt (2020), OptVerse (2021), LeOPT (2022), TAYLOR (2024) | Ongoing | Survey [S]; QbitAI; COPT guide |
| First-order LP, then GPU first-order LP | CPU first-order method in COPT by Jul 2022; GPU version Dec 2023 → Feb 2024 | First-order: timing relative to the PDLP literature not established. **GPU: fast follower**, about 1 month after cuPDLP.jl and about 3 months to a shipped product | Ongoing at product level | JuliaCon 2022 captions; arXiv; COPT 7.1 notes |

---

## 5. Era and resource context of each practice

| Era | Setting | Compute and tools | Team and money | Seniority |
|---|---|---|---|---|
| 2007–2008 MSc | MSc in HPC, Edinburgh (static.ph.ed.ac.uk dissertations area) | EPCC's Ness and the ECDF cluster, MPI, SAMG (licensed library), METIS, PGI/GCC/Intel compilers (dissertation bibliography). Porting to ECDF took "about 8 weeks, because of the incorrect SAMG libraries and license" (p. 59) | Two supervisors; external library team | Student |
| 2010–2013 PhD | ERGO group, School of Mathematics | 2010 prototype on "a dual quad-core AMD Opteron 2378 system" (RAL10). Thesis: "C++ … OpenMP directives"; OpenMP chosen for "the task directive introduced in OpenMP version 3.0 in 2008"; Intel C++ 13.0 with OpenMP 3.1; "compute64b … a workstation with 16 (Intel Xeon E5620, 2.4GHz) cores" (p. 17). Test set: 30 LPs, "Most … taken from a comprehensive list [48] provided by Mittelmann"; baselines Cplex 12.4 and Clp 1.14 (pp. 17–18) | Hall plus a second supervisor; peers Smith and Galabova. Funding: "Format International Ltd. and NAIS" (the funders' business and the NAIS acronym were not verified) | PhD student |
| 2014–2017 (evidence window) FICO, Xpress | Commercial solver team. Postal affiliation "FICO House, … Birmingham" | MPC experiments: "two Intel Xeon E5-2670s, 2.6 GHz (16 cores, 16 threads in total), using eight threads"; Clp 1.15, Cplex 12.4; Xpress run in serial and with 8 threads. NLAO16: "Extended testing using 159 test problems", baselines Clp v1.16 and Cplex v12.5 | Commercial team (size not found); continued joint work with Hall and Galabova | Early-career industrial developer |
| Start not verified (≤ Aug 2021) to 2026: Cardinal Operations, COPT | Company founded 2016 (Jiemian, company sources) | Full-suite product on Windows, Linux and macOS; GPU paths from COPT 7.1 (2024); cuPDLP-C used NVIDIA H100; COPT GPU barrier improvements in 8.0.x (2025–26). Company voice (Xinhua, 2026-04-28, co-founder Wang Xi, **not** Huangfu): GPU heterogeneous computing base and a "自主可控的加速计算数学库（CAML）" (translation: a self-controlled accelerated math library, CAML) | Company R&D. NSFC grants to Ge are acknowledged in cuPDLP-C. The cuPDLP-C co-authors are from UChicago, SUFE and Stanford | VP (2021) |

---

## 6. Failures, abandoned directions, limits (dated)

1. **2008, MSc plan vs outcome** [stated] P, pp. 59–60: "The optimization of the CSMP native parallel code was not carried out, mainly because of two reasons: one is that the porting / profiling phase takes too much time, the other one is that there is not too much parallel code, which has been well developed." Appendix F compares the original plan with what happened. [inferred] This plan-versus-outcome record is an early habit of self-audit.
2. **2010–2011, first parallel prototype was weak**: "modest speed-up" (ERGO-11-007), and in PPAM11 "Average (best) of 18% (50%) relative to 1 core" [stated-joint] P. The response was T2: rebuild the serial base first.
3. **2010–2013, CPU+GPU dual simplex planned, never reported**: see T4. [practice/inferred]
4. **2012–2013, hyper-sparsity promotion and LiDSE left at "an initial stage"**, never published as a paper. [stated] P; absence checked in DBLP and Hall's list.
5. **2013, PAMI's limits stated plainly** [stated] P, thesis p. 94: "For the reference set, PAMI provides an average speedup of 1.49. Though not extremely impressive, the performance of PAMI is comparable to the dual simplex implementation of Cplex". Also "when solving the LP problem Linf 520c of the reference set, PAMI solved 25% slower than the sequential solver". MPC p. 140 [stated-joint]: "the results in this paper are far from the linear speedup which is the hallmark of many quality parallel implementations".
6. **2013, overlapping inversion proposed as future work** (thesis p. 94: "One reason for the relative poor speedup of PAMI is that the time-consuming sequential LU factorization is not overlapped with the simplex iterations."). No later paper implementing it was found. [inferred] Not pursued in print.
7. **2016, reliability failures and missing features reported in public** [stated-joint] P, NLAO16: "hsol, sip and pami fail on cycle"; "pami with 8 threads fails on stat96v1"; limitations "No presolve", "No crash", "No advanced basis start".
8. **2016–2017, publication delay**: MPC accepted 10 Feb 2016, online 14 Dec 2017, a 22-month gap. No reason stated. [practice] P
9. **Impact asymmetry**: the COAP 2015 best-paper article has 11 citations, while MPC 2018 has 447. [observed] S. [inferred] His influence flows through software (HiGHS's citation request) more than through the update-technique paper.
10. **2023, own product shown failing**: in cuPDLP-C, COPT's simplex and barrier fail on five large QAP LP relaxations within 3600 s (see T8). [stated-joint] P
11. **2022, MIP lag admitted in public, with a dated prediction**: JuliaCon 2022 [stated] P: "according to public benchmarking, our MIP solver is still in a catching up position." Also: "if we can reproduce the same improvement as we've done in the past year, maybe by the mid of next year, 2023, we will be the best." Whether the prediction came true was **not checked** (it would need archived Mittelmann MIP benchmark pages, which are context only).
12. **Not found**: rejected papers, retractions or errata. This means none were found, not that none exist.

---

## 7. The last 12 months (2025-10-27 → 2026-10-27)

| Date | Item | Tag | Source |
|---|---|---|---|
| 2025-12-01, 2026-01-13, 2026-04-24, 2026-05-30, 2026-08-07, 2026-09-20 | COPT 8.0.2 → 8.0.7 release READMEs, all committed by the org account `COPT-Public`. Highlights: GPU barrier improvements (8.0.2, 8.0.6), "advanced simplex routines" (8.0.6), CUDA 13 support (8.0.6). **His personal part is not verified** | [practice, team-level] P | COPT-Release README.md and commit list |
| 2026-01-30 | arXiv 2208.14314v4, COPT User Guide Ver 8.0.1; Huangfu still 2nd author | [practice] P | arXiv |
| Mar 2026 | Front. Eng. Manag. 13(1) survey (Huang, Xiao, Ge, Yin, Liang) cites his MPC paper as the HiGHS reference and dates COPT's launch to 2019 | [observed] S | Crossref; journal page |
| 2026-04-28 | Xinhua interview with Cardinal co-founder Wang Xi on COPT and the company's GPU stack. Huangfu is not named | [observed] S, company context | news.cn |
| 2026-07-01 | HiGHS README still credits him as the original author of its simplex solvers | [observed] P | GitHub |
| 2026 (to 27 Oct) | MPC 2018 cited 168 times this year (OpenAlex) | [observed] S | OpenAlex |
| — | **Not found**: any new paper (arXiv, DBLP, Crossref), talk (two WebSearches, English and Chinese), public commit (last 2024-12-06), or change of position | — | Gaps |

---

## 8. Pointers for the synthesis (all [inferred])

- **Layer 2, problem choice**: he picks a classic method whose *context* has changed (hardware, preferred variant) and states the changed context explicitly ("the context for simplex parallelization has changed"). The test of worth is whether practitioners on ordinary machines get faster solves ("any speedup is desirable … for daily usage").
- **Layer 3, idea generation**: he revives old pivoting rules (suboptimization, 1968/1975) for new hardware, and follows anomalies in measurements (cost perturbation → hyper-sparsity → LiDSE). He reuses levers: objective perturbation appears in 2012 and again in 2021.
- **Layer 4, execution**: serial excellence before parallelism. Amdahl's-law profiling decides what to parallelise. Development is evolutionary ("from a proof-of-idea prototype with simple but less efficient data structures to an efficient elaborated implementation", thesis p. 17). He uses a fixed reference set drawn from Mittelmann's list, and Clp/Cplex as baselines.
- **Layer 5, judging results**: the bar is the best commercial solver (Cplex, Xpress). He reports slowdowns and failures. He measures with geometric means and performance profiles. He distrusts metrics that a fixed time cut-off can game (2021, "Gap" critique).
- **Layer 6, expression**: a recurring public framing, "the algorithm that runs the world". It appears three times over nine years: thesis p. 15 (2013, citing *New Scientist* 2012), the FICO blog title (2014), and the JuliaCon talk (2022: "Simplex algorithm is called "the algorithm that runs the world" in a New Scientist article from 2012"). He writes and speaks for practitioners (company blog, QbitAI, JuliaCon) as well as for journals.
- **Layer 7, organisation**: he moves the method to where it will be used: academic code → commercial solver → his own company's suite. He keeps collaborating with his supervisor after leaving (2014–2017). His lineage runs through software rather than students.

---

## Contradictions (kept, not reconciled)

1. **Who wrote hsol.** MPC 2018, p. 120: "Thus the authors have implemented a sequential dual simplex solver (hsol) from scratch." By contrast, RAL10 (2010): "Written by Qi Huangfu (2010)"; HSOL 1.0 README: "HSOL was originally written by Qi Huangfu". The thesis (p. 16, sole author) uses the passive "has been implemented from scratch".
2. **The code's name over time.** It was "ParISS" in 2011–2012 (ERGO-11-007, APMOD12), "HSOL/hsol" in 2013–2017, and "h2gmp (2011-date)" in Hall's 2017 Tokyo slides, which back-dates the later name to 2011.
3. **What PAMI stands for.** "parallelism across multiple iterations (PAMI)" in the thesis abstract versus "parallel minor iterations" (PAMI) in the HSOL 1.0 README.
4. **Headline claim and numbers, thesis versus journal.** Thesis (2013): PAMI mean speed-up 1.49, SIP 1.13, PAMI "comparable to … Cplex". MPC (2015/2018): PAMI 1.51, SIP 1.15. The abstract claims superiority to "the leading open-source simplex solver" (Clp), and the Cplex comparison is softened to "the better of sip and pami is comparable with that of Cplex for the majority of the test problems". The hardware differs (Xeon E5620 workstation versus 2×E5-2670 with 8 threads).
5. **Priority claims.** Blog 2014: "the first commercial parallel simplex solver". MPC 2018: "the first parallel revised simplex solver of general utility". Neither was checked against other vendors' histories here.
6. **Stance on simplex across eras.** Thesis p. 15 (2013): "the advanced dual revised simplex method is still frequently the preferred choice for solving LP problems". JuliaCon (Jul 2022, spoken): "in our experience, the simplex solver is very suitable for large and sparse LP problems and it is necessary for solving LP relaxations in MIP solver". cuPDLP-C (Dec 2023/Jan 2024, joint): "GPUs have a revolutionary impact on traditional LP solvers", and simplex and IPM rely on factorization that is "computationally infeasible at this magnitude". The problem scales differ, and the last text is nine-author joint text.
7. **Supervisors.** The thesis and ERA give two supervisors (Hall; Gondzio as second). MGP lists only "Advisor 1: Julian Hall".
8. **Hall's PhD year** (lineage detail). The Huangfu thesis bibliography [27] gives Hall's Dundee thesis as 1991. Hall's homepage gives "PhD 1992".
9. **The JuliaCon bio versus the HiGHS commit record.** JuliaCon 2022 bio: he "has worked on many different optimization solvers, including HiGHS and FICO-Xpress". The HiGHS repository (created 2018-03-27) has no commit under his name. His code entered via HSOL/h2gmp, and HiGHS credits him as the original author.
10. **Bibliographic details of the COAP items.** Hall's publication page lists the prize note as "Computational Optimization and Applications 65 (1) , 1-4, 2016. DOI: 10.1016/s10589-016-9882-5". Crossref gives 65(3):541–544 and DOI 10.1007/…. The COAP paper is cited as "60(4):587-608" in the SIOPT17 slides and as "60(587-608), 1-22 (2014)" in the MPC references. Crossref gives 60(3):587–608.
11. **Identity conflation in indexes.** OpenAlex author A5074771751 merges him with the Zhejiang University medical researcher, carrying that profile's ORCID iD and its 2022–2026 medical papers. The ORCID iD shown on A5074771751 **must not** be copied into `team.json` for this member.

---

## Gaps

- **Education before 2007** (undergraduate degree, institution, years): not found.
- **PhD start year**: not found (between Aug 2008 and Sep 2010).
- **FICO dates**: start between Jul 2013 and May 2014; end after Jul 2017. Neither is verified. Titles at FICO were not found. The Xpress version that first shipped the PAMI-based parallel simplex is not named in any source read.
- **Joining Cardinal Operations**: not dated (between Jul 2017 and Aug 2021). Titles other than "副总裁" (2021) and "developer of COPT" (2022) were not found; the current title is not verified.
- **Stated reasons** for the moves (academia → FICO, FICO → Cardinal): none found.
- **MGP**: live site offline; record read from a 2025-05-14 snapshot; Hall's own MGP page could not be re-read (HTTP 429).
- **COAP 2015 prize note** (paywalled) and Hager's COAP best-paper page (moved; Wayback unreachable): not read. These may hold winner bios.
- **JuliaCon 2022 talk**: the video was not watched. Only the caption transcript was read, and the slides were not seen. The arXiv paper he mentions on a barrier-side "technique to reduce the support of solutions" was not identified. The outcome of his 2022 MIP prediction ("by the mid of next year, 2023") was not checked.
- **Funders**: the business of Format International Ltd. and the expansion of "NAIS" were not verified.
- **Last 12 months**: no talks or papers found beyond the user-guide revision. Two WebSearches (English and Chinese) and arXiv/DBLP/Crossref checks returned nothing.
- **Rejected papers or failed submissions**: not observable in public records.
- **His personal contributions inside COPT** (which solver components he wrote): not documented publicly. Product features are team-level records.

---

## Sources

**Primary: by or with Huangfu, his code, institutional records of his work**

1. Q. Huangfu, "Optimization of a large-scale parallel finite element - finite volume C++ code", MSc in High Performance Computing dissertation, The University of Edinburgh, 22 Aug 2008. https://static.ph.ed.ac.uk/dissertations/hpc-msc/2007-2008/Qi_Huangfu.pdf (full text read). P
2. Q. Huangfu, "High performance simplex solver", PhD thesis, The University of Edinburgh, 2013. http://hdl.handle.net/1842/7952, PDF https://era.ed.ac.uk/bitstream/1842/7952/2/Huangfu2013.pdf (full text read). P
3. Edinburgh Research Archive OAI-PMH record oai:era.ed.ac.uk:1842/7952 (dates 2013-07-01 / 2013-10-22; contributors Hall, Gondzio). P
4. J. A. J. Hall, Q. Huangfu, "A high performance dual revised simplex solver", Technical Report ERGO-11-007, 12 May 2011. https://webhomes.maths.ed.ac.uk/hall/HaHu11/ERGO-11-007.pdf (read). P
5. J. A. J. Hall, Q. Huangfu, "A High Performance Dual Revised Simplex Solver", PPAM 2011, LNCS 7203, 143–151, Springer, 2012. DOI 10.1007/978-3-642-31464-3_15 (metadata via DBLP and Crossref; chapter not read). P
6. Q. Huangfu, J. A. J. Hall, "Novel update techniques for the revised simplex method", Technical Report ERGO-13-001, 7 Jul 2013. https://webhomes.maths.ed.ac.uk/hall/HuHa12/ERGO-13-001.pdf (header and abstract read). P
7. Q. Huangfu, J. A. J. Hall, "Novel update techniques for the revised simplex method", Comput. Optim. Appl. 60(3):587–608 (online 2014-08-23; print 2015). DOI 10.1007/s10589-014-9689-1 (Crossref; published version not read). P
8. Q. Huangfu, J. A. J. Hall, "Parallelizing the dual revised simplex method", Technical Report ERGO-14-011 (version of 6 Mar 2015), arXiv:1503.01889, Optimization Online 2015/03/4836. https://webhomes.maths.ed.ac.uk/hall/HuHa13/ERGO-14-011.pdf (header and abstract read). P
9. Q. Huangfu, J. A. J. Hall, "Parallelizing the dual revised simplex method", Math. Program. Comput. 10(1):119–142, 2018 (received 2015-03-06, accepted 2016-02-10, online 2017-12-14). DOI 10.1007/s12532-017-0130-5, CC-BY. Author copy https://webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf (full text read). P
10. Q. Huangfu, "The Algorithm that Runs the World", FICO Blog, 13 May 2014. http://www.fico.com/en/blogs/analytics-optimization/the-algorithm-that-runs-the-world/ (read via Wayback snapshot 20170803233453). P
11. J. A. J. Hall, Q. Huangfu, "Promoting hyper-sparsity in the revised simplex method", APMOD 2012, extended abstract (29 Mar 2012) and slides (28 Mar 2012). https://webhomes.maths.ed.ac.uk/hall/APMOD12/ P
12. J. Hall, E. Smith, Q. Huangfu, slides "Towards a practical parallelisation of the revised simplex method", IMA NLAO, 14 Sep 2010. https://webhomes.maths.ed.ac.uk/hall/IMA-NLAO_10/IMA-NLAO_10.pdf P
13. J. Hall, Q. Huangfu, E. Smith, slides "A high performance dual revised simplex solver", Oxford CMA seminar at RAL, 2 Dec 2010. https://webhomes.maths.ed.ac.uk/hall/RAL10/RAL10.pdf P
14. J. Hall, Q. Huangfu, E. Smith, slides "High performance computing and the simplex method", LANCS workshop, 12 Apr 2011. https://webhomes.maths.ed.ac.uk/hall/Lancs11/Lancs11.pdf P
15. J. Hall, Q. Huangfu, slides "A high performance dual revised simplex solver", PPAM 2011, 13 Sep 2011. https://webhomes.maths.ed.ac.uk/hall/PPAM11/PPAM11.pdf P
16. Q. Huangfu, J. Hall, slides "Parallelizing the dual revised simplex method", NLAO16, 9 Sep 2016. https://webhomes.maths.ed.ac.uk/hall/NLAO16/NLAO16.pdf P
17. Q. Huangfu, J. Hall, slides "Novel update techniques for the revised simplex method (and their application)", ERGO seminar, 30 Nov 2016. https://webhomes.maths.ed.ac.uk/hall/ERGO_301116/ERGO_301116.pdf P
18. J. Hall, Q. Huangfu, I. Galabova, slides "Three high performance simplex solvers", Argonne National Laboratory, 16 May 2017. https://webhomes.maths.ed.ac.uk/hall/Argonne17/Argonne17.pdf P
19. J. Hall, Q. Huangfu, I. Galabova, slides "An open-source high performance dual simplex solver", SIAM Conference on Optimization, 22 May 2017. https://webhomes.maths.ed.ac.uk/hall/SIOPT17/SIOPT17.pdf P
20. Q. Huangfu, J. Hall, slides "Novel update techniques for the revised simplex method", EUROPT 2017, "In memory of Roger Fletcher", 13 Jul 2017. https://webhomes.maths.ed.ac.uk/hall/EUROPT17/EUROPT17.pdf P
21. HSOL 1.0 README and commit history, https://github.com/mattmilten/h2gmp (repo created 2017-10-11, last push 2018-03-26; the original galabovaa/h2gmp returns 404). P
22. D. Ge, Q. Huangfu, Z. Wang, J. Wu, Y. Ye, "Cardinal Optimizer (COPT) User Guide", arXiv:2208.14314 (v1 2022-08-30, Ver 5.0.4; v2 2022-10-28; v3 2024-11-16, Ver 7.2.1; v4 2026-01-30, Ver 8.0.1; front matter and overview read). P
23. H. Lu, J. Yang, H. Hu, Q. Huangfu, J. Liu, T. Liu, Y. Ye, C. Zhang, D. Ge, "cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language", arXiv:2312.14832 (v1 2023-12-22, v2 2024-01-07; read). P
24. 皇甫琦, 葛冬冬 (撰稿), "DeepMind激起千层浪的这篇论文，并非无所不能", 量子位 (qbitai.com web article), 2021-08-14. https://www.qbitai.com/2021/08/27579.html P
25. JuliaCon 2022, "COPT and its Julia interface", lightning talk, 2022-07-27, speaker page. https://pretalx.com/juliacon-2022/talk/XRDNVT/ P
26. Q. Huangfu, talk "COPT and its Julia interface", JuliaCon 2022 (2022-07-27), video https://www.youtube.com/watch?v=iqiBXoJQVD8 (identity checked via YouTube oEmbed, 2026-10-27). Read as the uploaded caption transcript saved in this run at `references/sources/talks/juliacon-2022-copt-and-its-julia-interface.transcript.txt` (not speaker-checked). P
27. COPT-Public/COPT-Release, GitHub: README.md (COPT 8.0) and README-40/50/60/65/70/71/72.md; 68 commits 2022-04-29 → 2026-09-20 (16 by `huangfu7`, 2022-04-29 → 2024-12-06), incl. commit aa44684aac (2024-02-18). https://github.com/COPT-Public/COPT-Release P
28. COPT-Public/COPT.jl, GitHub: commits by `huangfu7`, 2022-04-27 → 2024-09-03 (via commit search). https://github.com/COPT-Public/COPT.jl P
29. GitHub API, user `huangfu7` (created 2022-03-22; no public repos). P
30. ERGO-Code/HiGHS, GitHub: README.md at master, last README commit 9d12ffbb12bcef7ab1fcae90178906cf20e85326 (2026-07-01); repo created 2018-03-27; commit search for author-name Huangfu/Qi: 0 results (2026-10-27). https://github.com/ERGO-Code/HiGHS P
31. COPT documentation index, https://guide.coap.online/copt/en-doc/ (no release-history page found). P

**Primary: first-hand observers (supervisor and team pages)**

32. J. A. J. Hall, homepage, https://webhomes.maths.ed.ac.uk/hall/ (Hall's own bio, and his description of Huangfu as a former PhD student). P
33. J. A. J. Hall, Publications page, https://webhomes.maths.ed.ac.uk/hall/Publications.html. P
34. J. A. J. Hall, Talks page, https://webhomes.maths.ed.ac.uk/hall/Talks.html. P
35. J. A. J. Hall, Academic prizes page, https://webhomes.maths.ed.ac.uk/hall/Prizes. P
36. J. A. J. Hall, folder pages HuHa13/, HuHa12/, HaHu11/, COAP_Prize_2015/ on webhomes.maths.ed.ac.uk/hall/. P
37. J. A. J. Hall, slides "Three high performance simplex solvers", public lecture, Tokyo, 14 Aug 2017. https://webhomes.maths.ed.ac.uk/hall/Tokyo17/Tokyo17.pdf P
38. HiGHS documentation index, https://ergo-code.github.io/HiGHS/dev/ (generated 2026-10-27), and https://highs.dev/ (history paragraph and team list). P

**Secondary**

39. DBLP person 116/5281 via SPARQL (sparql.dblp.org), fetched 2026-10-27: 5 records, 2012–2022. S
40. arXiv API queries au:Huangfu_Q and all:"Qi Huangfu" (2026-10-27); arXiv:2311.12180 metadata (H. Lu, J. Yang, cuPDLP.jl, 2023-11-20). S
41. OpenAlex: author A5074771751 and its works; works by DOI with counts_by_year (2026-10-27). S
42. Crossref metadata for DOIs 10.1007/s12532-017-0130-5, 10.1007/s10589-014-9689-1, 10.1007/978-3-642-31464-3_15, 10.1007/s10589-016-9882-5, 10.1007/s42524-026-5153-z. S
43. Mathematics Genealogy Project, id 204105 (Qi Huangfu), Wayback snapshot 2025-05-14 (https://mathgenealogy.org/id.php?id=204105); live-site outage notice read 2026-10-27. S
44. Springer, Mathematical Programming Computation "Outstanding Paper of the Year" Award page, https://www.springer.com/journal/12532/updates/17226372. S
45. "COAP 2015 Best Paper Prize", Comput. Optim. Appl. 65(3):541–544, online 2016-11-01. DOI 10.1007/s10589-016-9882-5 (paywalled preview; not read). S
46. L. Huang, F. Xiao, D. Ge, W. Yin, Z. Liang, "An overview of mathematical programming solvers: Theory, development, and recent advances", Frontiers of Engineering Management 13(1):1–16, 2026. DOI 10.1007/s42524-026-5153-z (journal page text read). S
47. Optimization Online, author page "Q. Huangfu", https://optimization-online.org/author/qi-huangfu/. S
48. Cardinal Operations, COPT solver page, https://www.shanshu.ai/solver ("2022年10月发布求解器COPT6.0版"). S
49. 新华网, "杉数科技王曦：以自主创新驱动“人工智能+”落地，引领智能经济新业态发展", 2026-04-28. https://www.news.cn/info/20260428/27ebb473b50c4502b74d403581a80797/c.html (company context; Huangfu not named). S
50. 界面新闻, "在复杂问题中求解，杉数科技想用AI帮更多中国企业找到最优决策｜界面创新家⑤", https://m.jiemian.com/article/4615329.html (date not determined; company context; Huangfu not named). S
51. WebSearch result lists (5 queries, 2026-10-27), used as leads only: one supplied the MGP id 204105, another the QbitAI article. S
52. Internet Archive Wayback availability API responses (FICO blog, MGP), 2026-10-27. S

*Lead only, not counted*: `product/nonlinear-team/roger-fletcher/references/research/06-trajectory.md` (this repo).
