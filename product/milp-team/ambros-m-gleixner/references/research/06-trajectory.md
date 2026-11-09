# Ambros M. Gleixner: research trajectory (research agent 06)

- **Researcher**: Ambros M. Gleixner. Living. Professor at HTW Berlin since 1 October 2020; his homepage gives the subject as discrete mathematics and operations research [1], and the HTW people page lists mathematical optimization, operations research and computer-oriented mathematics [12]. ZIB lists him as a guest in the division Mathematical Algorithmic Intelligence (department Applied Optimization, group Prescriptive Systems) [15][16]. scipopt.org lists him as a current SCIP developer for the general framework, exact SCIP and SoPlex, and verification [24]. He co-maintains the MIPLIB 2017 website [27]. Dr. rer. nat., TU Berlin; defence 24 June 2015 [5]. He is **not** the A. Gleixner of the ANTARES neutrino-telescope collaboration: an arXiv `au:Gleixner_A` query returns only that physicist's 27 papers (see Contradictions).
- **Dimension**: research trajectory. This note covers the dated timeline, the lineage (formal and informal), the turns and what triggered them, when he enters and leaves topics, the resource context of each era, failures and unrealized plans, his hands-on coding over time, and the last 12 months. It serves framework layer 2 (problem choice and timing) and layer 7 (research organisation), with pointers for layers 1, 4 and 5.
- **Research date**: 2026-11-08
- **Sources consulted**: 115 numbered sources (102 primary, 13 secondary), listed at the end. Of these, 55 papers ([50]–[91] and [98]–[110]) were checked only through Crossref, DataCite or arXiv metadata and abstracts, not read in full. **WebSearch calls used: 5 of 5.** Everything else came from curl, WebFetch, and the APIs of ORCID, arXiv, Crossref, DataCite, DepositOnce and GitHub (unauthenticated), plus `scripts/dblp_works.py` (read-only).
- **Local corpus**: `references/sources/papers/`, `talks/`, `essays/`, `software/` and `publications/` hold only `.gitkeep`, and `RESOURCES.md` is the unfilled template. **Nothing below is from user-supplied material.** `private/` was not opened. No transcript was saved: no public talk recording or transcript was found.
- **Sibling notes**: `01-publications.md` appeared while this note was being written. I read only its headings and a few lines, as a cross-check. Every fact below was fetched independently in this run. Notes 02–05 were not present when I started and were not read.
- **Quotation policy**: for copyright reasons the findings are paraphrased with a pinpoint (page, section or line). One short verbatim phrase is quoted, in §3 T3, marked with quotation marks. Check exact wording at the cited place before quoting downstream. Titles of works are given as identifiers.

### How the evidence was gathered (and what failed)

- **Homepage** (`zib.de/userpage/gleixner/`): I read the visible text and also the HTML comments. The commented-out blocks hold older, undisplayed text: the SAP and Siemens cooperations, the startup felmo, the PhD students he mentored, and interns. These blocks are undated and are tagged as page-source text. The page links a **long CV** (`gleixner.pdf`) in a commented-out line. That PDF is still served: 7 pages, dated 31 July 2017 on its first page, with Ambros Gleixner in the PDF author field. I read all of it.
- **ORCID** public API: three employment entries with exact dates, and 93 works.
- **DBLP** pid 07/3479 via the SPARQL script: 74 records, 2009–2026.
- **arXiv API**: a full-name query returns 48 preprints, 2016-04-02 → 2026-07-17. Abstracts of 16 were read.
- **DepositOnce** (TU Berlin) REST API: the thesis metadata (advisor, referees, defence date) and a discovery search for "Gleixner" (37 items). I read the front matter of 11 PhD theses from ZIB-related students, plus the abstract, acknowledgements and introduction (pp. i–6) of Gleixner's own thesis.
- **Mathematics Genealogy Project**: a notice says most dynamic pages are down after a vulnerability, but the quick search and individual pages worked on 2026-11-08. I read records 206147 (Gleixner), 24939 (Grötschel), 117700 (Koch) and 342910 (Eifler) live.
- **GitHub API** (unauthenticated, read-only): the full commit history of `scipopt/vipr` (147 commits), commit-search counts by author name for `scipopt/scip`, `scipopt/soplex` and `scipopt/papilo` (per year for SCIP and SoPlex), repository metadata, the SCIP CHANGELOG and the release dates. Commit e-mail addresses in API payloads are deliberately not reproduced.
- **Crossref and DataCite**: metadata for 55 DOIs, plus 3 DataCite-registered DOIs (LIPIcs, Dagstuhl) [48][49].
- **Wayback Machine** [112]: scipopt.org snapshots of 2021-01-18 and 2023-01-04 were read. Later requests returned HTTP 429 and then a bot block, so I stopped. A Dec 2018 snapshot of scip.zib.de was fetched once and then lost when the next request overwrote it. Not used.
- **Blocked, not circumvented**: ZIB OPUS (ZIB-Reports) sits behind an Anubis bot wall, so ZIB-Report items are cited from his CV. The Argonne event page and the Simons Institute page show a Cloudflare challenge; both are known only from search snippets (see Gaps).
- **Google Scholar** (profile `DUFnBNcAAAAJ`, linked from the homepage): read through WebFetch, whose small model summarised the page. The numbers are reported as that tool returned them and were **not** independently checked.
- **Other primary institutional pages**: HTW Berlin (people page, research catalogue with 9 project pages), ZIB (member page, MAI division, project pages), MATH+, the MIPLIB 2017 site and paper, the MIP Workshop 2026 and its Land-Doig competition page, the ML4CO 2021 page, the MPC editorial board, the COST TD1207 site (his STSM report) and the COW 2025 programme.
- **Privacy**: phone numbers and e-mail addresses on the pages read are not reproduced. Neither are his birthplace (thesis title page), his school name (CV) or the names of HTW student assistants.

### Tag legend

- **[stated]**: Gleixner's own words in sole-authored or first-person text: the 2017 CV, the homepage text, the COST STSM report (2014), the PhD thesis (2015), his quote in the HTW–ZIB appointment news (2020), and the talk abstracts for MIP 2021 and COW 2025 (both first-person or speaker-attributed).
- **[stated-joint]**: co-authored text such as papers, release reports and the team text of the MIPLIB site. His individual voice cannot be separated in these.
- **[practice]**: what the record shows he did: papers, dates, code, commits, project lists, affiliations.
- **[observed]**: what others report about him: students' acknowledgements, team pages, MGP, Google Scholar, competition committees, editorial boards.
- **[inferred]**: my synthesis. Treat it as a hypothesis.
- **P / S**: primary / secondary source.

---

## 0. The trajectory in one paragraph (all [inferred], built from the sections below)

Gleixner's career is **one engineering programme carried by one code base**. The aim is to make LP-based MIP and MINLP solving in SCIP and SoPlex both faster and *trustworthy*, and to build the shared instruments the field uses to judge such progress: MIPLIB 2017, release reports, competitions and a delta debugger.

He entered through applied integer programming: open-pit mine scheduling in a UNSW honours project with Gary Froyland (2006), then a TU Berlin Diplom under Rolf Möhring (2008). He joined ZIB's SCIP team in September 2008. His first years there were spent on MINLP solver components, built with Berthold, Vigerske and Weltge.

The decisive turn came in **2012**. With Dan Steffy and Kati Wolter he carried iterative refinement into LP. His thesis gives two reasons. First, the instabilities of MINLP solvers sit in their LP relaxations. Second, multiscale biology models defeat double-precision LP solvers. An exact SoPlex followed (his SoPlex commits peak in 2013–2014). From a December 2014 research visit to Bologna he widened the question from exact LP to whether floating-point MIP *decisions* can be trusted. He started the VIPR certificates in November 2016.

He then spent nine years, mostly through students, moving exactness from a side branch into mainline SCIP. SCIP 10.0.0 (24 Nov 2025) ships a numerically exact solving mode with certificates, and his own SCIP commits jump to 411 in 2025.

In parallel he headed ZIB's Mathematical Optimization Methods group (Sept 2015 – Mar 2023) and was SCIP's head of development. In that role he led the community infrastructure: first author of the SCIP 5.0 and 6.0 reports and of MIPLIB 2017 (call Nov 2016, published 2021). He also brought in industrial and energy funding (SAP, Siemens, BMWi energy models run on supercomputers). His group followed the field's later waves:

- ML-for-MIP, 2021–2023, then left.
- GPU and first-order methods: 2020, 2023, and 2026, when the team won first place in the Land-Doig MIP Competition.
- Proof logging imported from pseudo-Boolean solving, with Jakob Nordström.

His base moved to HTW Berlin in October 2020, as the first step of an HTW–ZIB cooperation. Since 2025 the projects he starts are applied, third-party-funded work: GPU production scheduling for SAP, sepsis diagnostics with Charité, logistics, distribution grids and university timetabling.

**In the last 12 months**: SCIP 10.0 with the exact mode; seven new arXiv preprints (one of them the SCIP 10.0 report) and two journal papers; first place in the 2026 Land-Doig competition; two MIPLIB solution-file releases; four new funded HTW projects (a fifth, GoPPS, began in October 2025, just before the window); and his own commits to SCIP's exact linear constraint handler as late as 24–25 Oct 2026.

---

## 1. Dated timeline

| Date | Event | Tag | Source |
|---|---|---|---|
| 2002 | Abitur, grade 1.0 | [practice] P | CV 2017 p. 1 [2] |
| 2004 | Vordiplom (BSc) in mathematics, Universität Bayreuth | [practice] P | CV [2]; homepage [1] |
| 2004, 2005 | Siemens internships. Transportation Systems Locomotives: computer-aided simulation of engine-room fires (2004). Corporate Technology: efficient planning of wireless networks (2005) | [practice] P | CV p. 6 [2] |
| 2005–2008 | Member of the German National Merit Foundation | [practice] P | CV p. 6 [2] |
| 2006 | Study-abroad scholarship of the DAAD. Honours project at UNSW Sydney with Gary Froyland on integer programming for large-scale open-pit mine scheduling. In his thesis acknowledgements he credits Froyland with encouraging his first steps in discrete optimization | [practice] P; [stated] P | CV p. 6 [2]; thesis p. iii [4] |
| 2007 | ADONET Young Researcher Fellowship at ELTE Budapest. Member of the Berlin Mathematical School, 2007–2015 | [practice] P | CV p. 6 [2] |
| Jun 2008 | Diplom (MSc), TU Berlin, grade 1.0. Thesis: *Solving large-scale open pit mining production scheduling problems by integer programming*, supervisor Rolf H. Möhring (ZIB URN nbn:de:0297-zib-11389). The thesis acknowledgements name Andreas Bley as the person through whom he learned of ZIB | [practice] P; [stated] P | CV pp. 1, 3 [2]; thesis p. iii [4] |
| 1 Sep 2008 | Scientific employee at ZIB, until 31 Aug 2015 | [practice] P | ORCID [3] |
| 4 Sep 2008 / 26 Sep 2008 | First SoPlex commit under his name (a file rename; bug fixes follow on 22 Sep) and first SCIP commit (edits to documentation sections) | [practice] P | GitHub commit search [20] |
| Apr 2009 | First journal paper: Boland, Dumitrescu, Froyland, Gleixner, *LP-based disaggregation approaches to solving the open pit mining production scheduling problem with block processing selectivity*, Comput. Oper. Res. 36:1064–1089, DOI 10.1016/j.cor.2007.12.006. This is the UNSW line. Authors are in alphabetical order | [practice] P | Crossref [50] |
| Jul, Aug 2009 | Talks at EURO 2009 and ISMP 2009 on Lagrangean relaxation for open-pit scheduling | [practice] P | CV p. 6 [2] |
| 2009–2014 | Associated researcher in MATHEON B20, Optimization of Gas Transport (the homepage dates his MATHEON membership 2008–2014) | [practice] P | CV p. 6 [2]; homepage [1] |
| Jan–Apr 2010 | Undercover talks (Aussois 6 Jan 2010; EWMINLP Marseille, Apr 2010); first MINLP work, with Timo Berthold | [practice] P | CV pp. 5–6 [2] |
| May 2011 | Conference chair of CPAIOR 2011, Berlin, with Berthold, Heinz and Koch | [practice] P | homepage [1]; CV p. 4 [2] |
| Jun 2011 | Koch et al., *MIPLIB 2010*, Math. Program. Comput. 3:103–163, DOI 10.1007/s12532-011-0025-9. He is 9th of 16 authors (Koch first, then alphabetical) | [practice] P | Crossref [36] |
| 2011–2012 | MINLP for water networks (talks at OR 2011 and the Sino-German workshop, 2011). Gleixner, Held, Huang, Vigerske, *Towards globally optimal operation of water supply networks*, NACO 2(4):695–711 (2012), DOI 10.3934/naco.2012.2.695. Berthold, Gleixner, Heinz, Vigerske, *Analyzing the computational impact of MIQCP solver components*, NACO 2(4):739–748 (2012), DOI 10.3934/naco.2012.2.739 | [practice] P | CV [2]; Crossref [51][52] |
| Jan 2012 | Bley, Gleixner, Koch, Vigerske, *Comparing MIQCP Solvers to a Specialised Algorithm for Mine Production Scheduling*, HPSC 2009 proceedings, 25–39, DOI 10.1007/978-3-642-25707-0_3. This is the last mining paper | [practice] P | Crossref [53] |
| 22 Jul 2012 | Gleixner, Steffy, Wolter, *Improving the accuracy of linear programming solvers with iterative refinement*, ISSAC 2012, 187–194, DOI 10.1145/2442829.2442858. The start of the exactness line | [practice] P | Crossref [54] |
| Aug 2012 | Talk "Rapid optimality-based bound tightening", ISMP 2012, Berlin | [practice] P | CV p. 5 [2] |
| Oct 2012 | Sole-authored ZIB-Report 12-36, *Factorization and update of a reduced basis matrix for the revised simplex method*. Read from the CV; the OPUS record was not opened | [practice] P | CV p. 3 [2] |
| Mar 2013 | Berthold & Gleixner, *Undercover: a primal MINLP heuristic exploring a largest sub-MIP*, Math. Program. 144:315–346 (online 2013-03-03), DOI 10.1007/s10107-013-0635-2 | [practice] P | Crossref [55] |
| May–Jun 2013 | Gleixner & Weltge, *Learning and Propagating Lagrangian Variable Bounds for Mixed-Integer Nonlinear Programming*, CPAIOR 2013, DOI 10.1007/978-3-642-38171-3_26. Berthold & Gleixner, *Undercover Branching*, SEA 2013, DOI 10.1007/978-3-642-38527-8_20 | [practice] P | Crossref [56][57] |
| 2013 | MERIT Visiting Scholar, University of Melbourne. Talks on 24–25 Sep 2013. Member of the Research Campus MODAL from 2013 (CV) or 2014 (homepage); see Contradictions | [practice] P | CV pp. 4, 6 [2]; homepage [1] |
| 2013–2014 | Peak of his SoPlex coding: 171 commits (2013) and 369 (2014) | [practice] P | GitHub commit search [20] |
| Nov–Dec 2014 | Bologna visit (COST TD1207 short-term scientific mission) with host Andrea Lodi and his student Luca Fabbri; talk on 28 Nov 2014. On 13 Dec 2014 he gives the talk "SoPlex: A New Exact LP Solver" at GAMS. The STSM report is dated 31 Dec 2014 | [practice] P; [stated] P | CV p. 4 [2]; STSM report [7] |
| 24 Jun 2015 | PhD defence, TU Berlin. *Exact and fast algorithms for mixed-integer nonlinear programming*, DOI 10.14279/depositonce-4938. DepositOnce lists advisor Grötschel and referees Koch and Lodi; the CV adds summa cum laude | [practice] P | DepositOnce [5]; thesis title page [4]; CV p. 1 [2] |
| Jul 2015 | Talk "SoPlex: a new exact LP solver", ISMP 2015 | [practice] P | CV p. 5 [2] |
| 1 Sep 2015 | Head of a ZIB research group, until 31 Mar 2023. The homepage names it Mathematical Optimization Methods | [practice] P | ORCID [3]; homepage [1] |
| since 2015 | Technical Editor of Math. Program. Comput. (CV). In 2026 he is an Associate Editor (board page) | [practice] P; [observed] P | CV p. 7 [2]; MPC board [41] |
| 2015–2018 | PI of ZIB's sub-project of **BEAM-ME** (BMWi, grant 03ET4023D), on energy-system models. ZIB's page names Koch and Gleixner as heads and partners incl. the Stuttgart and Jülich HPC centres | [practice] P | CV p. 6 [2]; ZIB project page [17] |
| 2015–2019 | PI of the SAP project on LP/IP techniques for supply-chain management, with Koch and Martin. Output: Gamrath et al., *Tackling Industrial-Scale Supply Chain Problems by Mixed-Integer Programming*, J. Comput. Math. 37:866–888, DOI 10.4208/jcm.1905-m2019-0055 (ZIB-Report 16-45, Nov 2016) | [practice] P | CV pp. 2, 6 [2]; Crossref [58] |
| since 2015 | PI of the Siemens–ZIB cooperation (a member of it from 2008) | [practice] P | CV p. 6 [2] |
| Jul 2016 | Co-organizer of the 7ECM minisymposium "Exact Solutions and Certificates in Mathematical Optimization" (with Steffy) and of the ICMS 2016 stream "Mathematical Optimization" (with Kirches, Mitchell and Ralphs). The guest editors' preface appeared in Optim. Methods Softw. 33 (2018), DOI 10.1080/10556788.2018.1459255 | [practice] P | CV p. 4 [2]; Crossref [59] |
| Sep 2016 | D'Andreagiovanni & Gleixner, *Towards an Accurate Solution of Wireless Network Design Problems*, ISCO 2016, DOI 10.1007/978-3-319-45587-7_12 | [practice] P | Crossref [60] |
| Nov 2016 | Public call for MIPLIB 2017 contributions. A 21-member committee forms, including representatives of nine MIP solver teams | [stated-joint] P | MIPLIB 2017 paper p. 444 [35] |
| 20 Nov 2016 | **VIPR initial commit** by Gleixner; Steffy uploads the checker code the same day. The arXiv preprint 1611.08832 follows on 27 Nov 2016, then IPCO 2017: Cheung, Gleixner, Steffy, *Verifying Integer Programming Results*, DOI 10.1007/978-3-319-59250-3_13 | [practice] P | GitHub [19]; arXiv [30]; Crossref [61] |
| WS 2016/17 | Graduate course "Optimierung in Industrie und Wirtschaft", FAU Erlangen–Nürnberg | [practice] P | CV p. 6 [2] |
| Jun 2016 / Apr 2017 | Gleixner, Berthold, Müller, Weltge, *Three enhancements for optimization-based bound tightening*, J. Glob. Optim. 67:731–757, DOI 10.1007/s10898-016-0450-4. The order is not alphabetical, so this is a genuine first-author lead | [practice] P | Crossref [62] |
| Jun 2017 | Vigerske & Gleixner, *SCIP: global optimization of mixed-integer nonlinear programs in a branch-and-cut framework*, Optim. Methods Softw. 33:563–593, DOI 10.1080/10556788.2017.1335312 | [practice] P | Crossref [63] |
| Jul 2017 | CV: the group he heads has 2 senior researchers, 10 research assistants and 4 student assistants. The CV says SCIP has more than 8,000 downloads per year | [stated] P | CV pp. 1, 6 [2] |
| 1 Aug 2017 | MIPLIB 2017 submissions close: 128 submissions | [stated-joint] P | MIPLIB paper §3.1 [35] |
| Dec 2017 / Jul 2018 | **SCIP Optimization Suite 5.0** (ZIB-Report 17-61) and **6.0** (ZIB-Report 18-26). He is first author of both, ahead of an alphabetical list; the 4.0, 3.2 and 7.0 reports are led by others | [practice] P | scipopt.org citation list [24] |
| 2017–2018 | SCIP commit peaks: 144 (2017) and 134 (2018) | [practice] P | GitHub [20] |
| 18–23 Feb 2018 | Co-organizer of Dagstuhl Seminar 18081, "Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization" (with Bonami, Linderoth and Misener), DOI 10.4230/DagRep.8.2.64 | [practice] P | DataCite [64]; CV p. 4 [2] |
| 1 Apr 2018 – 30 Sep 2021 | Project lead of **EnBA-M** (BMWi EnEff:Stadt), on MIQCPs for the Berlin-Adlershof energy network. Partners: TU Berlin, RWTH Aachen, Siemens, WISTA, ZIB | [practice] P | HTW project page [14]; ZIB page [17] |
| Sep 2018 | Furini et al., *QPLIB: a library of quadratic programming instances*, Math. Program. Comput. 11 (2019), DOI 10.1007/s12532-018-0147-4. He is 5th of 13 authors | [practice] P | Crossref [65] |
| Dec 2018 | Gleixner, Maher, Müller, Pedroso, *Price-and-verify: a new algorithm for recursive circle packing using Dantzig–Wolfe decomposition*, Ann. Oper. Res. 284 (2020), DOI 10.1007/s10479-018-3115-5. First posted as arXiv 1702.07799 (Feb 2017) under the title *Exact Methods for Recursive Circle Packing* | [practice] P | Crossref [66]; arXiv [30] |
| 2019 | Only 2 SCIP commits under his name, both on 1 Mar 2019: one merges a branch into a branch named `sap-shootout`, the other fixes a CHANGELOG typo. No SoPlex commits | [practice] P | GitHub [20] |
| Apr 2019 / Nov 2019 | Gleixner & Steffy, *Linear Programming Using Limited-Precision Oracles*, IPCO 2019, DOI 10.1007/978-3-030-17953-3_30. Journal version in Math. Program. 183:525–554 (2020), DOI 10.1007/s10107-019-01444-6 | [practice] P | Crossref [67][68] |
| 25 Jul 2019 | MIPLIB 2017 paper received by MPC (accepted 10 Sep 2020; online 7 Jan 2021). Gleixner et al., *MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library*, Math. Program. Comput. 13:443–490, DOI 10.1007/s12532-020-00194-3. He is first author, followed by Hendel and Gamrath, then an alphabetical list | [practice] P | Crossref [34] |
| 1 Apr 2020 – 31 Mar 2023 | Project lead of **MODAL SynLab**, "Intelligente Algorithmen für High-Performance-Optimierung" (BMBF Forschungscampus). Partners: ZIB, FICO, GAMS, Gurobi, Siemens, SAP | [practice] P | HTW project page [14] |
| 2020 (news undated) | ZIB/MODAL news: an HTW–ZIB cooperation agreement, whose first step is his appointment; he is to teach in the business-mathematics bachelor programme from October. He is quoted on why he is glad to teach optimization at HTW (paraphrased in §3 T12) | [stated] P; [observed] P | ZIB news [10]; MODAL news [11] |
| **1 Oct 2020** | **Professor at HTW Berlin** | [practice] P | ORCID [3]; homepage [1] |
| Oct 2020 | Witzig & Gleixner, *Conflict-Driven Heuristics for Mixed Integer Programming*, INFORMS J. Comput. 33:706–720 (online 2020-10-08), DOI 10.1287/ijoc.2020.0973 | [practice] P | Crossref [69] |
| Nov 2020 | Sofranac, Gleixner, Pokutta, *Accelerating Domain Propagation: An Efficient GPU-Parallel Algorithm over Sparse Matrices*, IA3 workshop at SC20, DOI 10.1109/IA351965.2020.00007. Journal version in Parallel Comput. 109 (2022), DOI 10.1016/j.parco.2021.102874. His first GPU paper | [practice] P | Crossref [70][71] |
| 1 Jan 2021 – 31 Dec 2022 | MATH+ EF1-9, "Adaptive Algorithms through Machine Learning: Exploiting Interactions in Integer Programming". Heads: Gleixner and Pokutta. Members: Chmiela, Graczyk, Spiegel | [practice] P | MATH+ page [18]; HTW page [14] |
| 18 Jan 2021 | scipopt.org lists Sebastian Pokutta as Project Head and Gleixner as **Head of Development** | [observed] P | Wayback snapshot [25] |
| Jan 2021 | Devriendt, Gleixner, Nordström, *Learn to relax: Integrating 0-1 integer linear programming with pseudo-Boolean conflict-driven search*, Constraints 26:26–55 (online 2021-01-18), DOI 10.1007/s10601-020-09318-x. His first paper with Nordström | [practice] P | Crossref [72] |
| Feb / Apr 2021 | Public GitHub repositories created for SCIP (2021-02-26), SoPlex and PaPILO (2021-04-09) | [practice] P | GitHub repo metadata [21] |
| 5 May 2021 / 25 May 2021 | Eifler & Gleixner, *A Computational Status Update for Exact Rational Mixed Integer Programming*, IPCO 2021, DOI 10.1007/978-3-030-73879-2_12. Journal version in Math. Program. 197:793–812 (online 2022-01-07), DOI 10.1007/s10107-021-01749-5. On 25 May 2021 he gives the invited MIP 2021 talk on exact MIP | [practice] P; [stated] P | Crossref [73][74]; talk page [8] |
| 2021 | Chmiela, Khalil, Gleixner, Lodi, Pokutta, *Learning to Schedule Heuristics in Branch and Bound*, NeurIPS 2021, 24235–24246 (arXiv 2103.10294). He co-organizes the NeurIPS 2021 **ML4CO** competition; supporting organizations include ZIB and Google Research | [practice] P; [observed] P | DBLP [43]; arXiv [30]; ML4CO page [40] |
| 2020–2021 | SCIP commits: 156 (2020) and 165 (2021) | [practice] P | GitHub [20] |
| Dec 2021 / Jun 2023 | SCIP Optimization Suite 8.0 (arXiv 2112.08872). Journal version: *Enabling Research through the SCIP Optimization Suite 8.0*, ACM TOMS 49, DOI 10.1145/3585516 (35 authors, alphabetical) | [practice] P | arXiv [30]; Crossref [75] |
| 1 Jan 2022 – 31 Dec 2023 | **VetOpt**, commissioned by the veterinary-services startup felmo GmbH: optimization models and software for mobile veterinary services | [practice] P | HTW project page [14]; homepage comment [1] |
| 26 May 2022 | Eifler, Gleixner, Pulaj, *A Safe Computational Framework for Integer Programming Applied to Chvátal's Conjecture*, ACM TOMS 48, DOI 10.1145/3485630 (arXiv 1809.01572, Sep 2018; received 2020-09-01) | [practice] P | Crossref [76] |
| 4 Jan 2023 | scipopt.org still lists Pokutta as Project Head and Gleixner as Head of Development | [observed] P | Wayback snapshot [26] |
| 2023 | A dense year with students: Chmiela et al., *Online Learning for Scheduling MIP Heuristics*, CPAIOR 2023, DOI 10.1007/978-3-031-33271-5_8 (with Pawel Lichocki of Google). Mexi, Berthold, Gleixner, Nordström, CP 2023, DOI 10.4230/LIPIcs.CP.2023.27. Bestuzheva, Gleixner, Achterberg, *Efficient Separation of RLT Cuts for Implicit and Explicit Bilinear Products*, IPCO 2023, DOI 10.1007/978-3-031-32726-1_2, extended in Math. Program. 210 (2025), DOI 10.1007/s10107-024-02104-0. Bestuzheva, Gleixner, Vigerske, *A computational study of perspective cuts*, Math. Program. Comput. 15, DOI 10.1007/s12532-023-00246-4. Gleixner, Gottwald, Hoen, *PaPILO*, INFORMS J. Comput. 35, DOI 10.1287/ijoc.2022.0171 | [practice] P | Crossref, DataCite [77]–[82] |
| 31 Mar 2023 | End of the ZIB group-head role (ORCID). MODAL SynLab, which he led, ends the same day | [practice] P | ORCID [3]; HTW [14] |
| Nov 2023 | van Doornmalen, Eifler, Gleixner, Hojny, *A proof system for certifying symmetry and optimality reasoning in integer programming*, arXiv 2311.03877. Eifler, Nicolas-Thouvenin, Gleixner, precision boosting with LP iterative refinement, arXiv 2311.08037; journal version in INFORMS J. Comput. 37:933–944 (2025), DOI 10.1287/ijoc.2023.0409 | [practice] P | arXiv [30]; Crossref [83] |
| Feb 2024 | Eifler & Gleixner, *Safe and Verified Gomory Mixed-Integer Cuts in a Rational Mixed-Integer Program Framework*, SIAM J. Optim. 34:742–763, DOI 10.1137/23M156046X. The SCIP Optimization Suite 9.0 report appears (arXiv 2402.17702) | [practice] P | Crossref [84]; arXiv [30] |
| May–Jun 2024 | Hoen, Oertel, Gleixner, Nordström, *Certifying MIP-Based Presolve Reductions for 0–1 Integer Linear Programs*, CPAIOR 2024, DOI 10.1007/978-3-031-60597-0_20. Eifler, Witzig, Gleixner, *Branch and Cut for Partitioning a Graph into a Cycle of Clusters*, ISCO 2024, DOI 10.1007/978-3-031-60924-4_8. Bolusani et al., *The MIP Workshop 2023 Computational Competition on reoptimization*, Math. Program. Comput. 16:255–266, DOI 10.1007/s12532-024-00256-w | [practice] P | Crossref [85][86][87] |
| 8 Nov 2024 | Leon Eifler's PhD defence, *Algorithms and certificates for exact Mixed Integer Programming*. Gleixner is one of four referees; MGP lists him as Advisor 2 | [practice] P; [observed] S | DepositOnce [5]; Eifler thesis [93]; MGP [42] |
| 9 Jan 2025 | Talk at the 27th Aussois Combinatorial Optimization Workshop (COW 2025): "An a posteriori analysis of numerical correctness in LP-based branch and bound", with Hoen; affiliation HTW and ZIB | [stated] P | COW 2025 page and programme [9] |
| 2025 | His coding peaks: **411 SCIP commits**, 29 VIPR commits and 20 SoPlex commits | [practice] P | GitHub [19][20] |
| 2 Jun 2025 | Antonia Chmiela's PhD (advisor Pokutta; referees Pokutta and Dadush). Two of its chapters are joint work with him | [observed] P | DepositOnce [92]; Chmiela thesis [92] |
| 29 Jun 2025 | Hoen & Gleixner, *Analyzing the Numerical Correctness of Branch-and-Bound Decisions for Mixed-Integer Programming*, CPAIOR 2025, DOI 10.1007/978-3-031-95976-9_3 | [practice] P | Crossref [88] |
| 13 Oct 2025 | The 2026 Land-Doig MIP Competition publishes its topic: GPU-accelerated primal heuristics for MIP, supported by NVIDIA GPU cloud credits | [observed] P | competition page [39] |
| 1 Oct 2025 – 30 Sep 2027 | **GoPPS**, "GPU-accelerated optimization for Production Planning and Scheduling", funded by SAP SE. Project staff include Alexander Hoen and Berenike Masing | [practice] P | HTW project page [14] |
| 29 Oct 2025 | His last VIPR commit, a CHANGELOG revision | [practice] P | GitHub [19] |
| For Nov 2025 → Nov 2026 see §8 | | | |

---

## 2. Lineage

**Teachers and gatekeepers**

- **Gary Froyland** (UNSW, honours project 2006). The thesis acknowledgements credit him with encouraging Gleixner's first steps in discrete optimization (p. iii). The resulting paper is COR 2009, with Natashia Boland and Irina Dumitrescu. [stated] P [4]; [practice] P [50]
- **Rolf H. Möhring** (TU Berlin), supervisor of the 2008 Diplom thesis. [practice] P [2]
- **Andreas Bley**, named in the thesis acknowledgements as the person through whom he learned of ZIB (p. iii). He is also co-author of the 2012 mining chapter. [stated] P [4]; [practice] P [53]
- **PhD (TU Berlin, 2015)**:
  - DepositOnce: advisor **Martin Grötschel**; referees **Thorsten Koch** and **Andrea Lodi** [5].
  - Thesis title page: Grötschel, Koch and Lodi are all listed as Berichter (reviewers), with Reinhold Schneider as chair [4].
  - MGP 206147: Advisor 1 Grötschel, Advisor 2 Koch [42].
  - Grötschel's own student list includes Gleixner (2015) [44].
  - Upward: Grötschel's PhD was Bonn 1977 under Bernhard Korte (MGP 24939). Koch's was TU Berlin 2004, *Rapid Mathematical Programming*, under Grötschel and Alexander Martin (MGP 117700). [observed] S [42]
- **Peers who shaped the PhD era**, from the thesis acknowledgements (p. iii) [4]: Timo Berthold (co-author of the MINLP heuristics), Dan Steffy (the initiative for iterative refinement in SoPlex), Kati Wolter (testing and profiling of the exact SoPlex extensions), Stefan Vigerske (turned SCIP into an MINLP solver), Marc Pfetsch (first SoPlex debugging sessions), and Roland Wunderling and Tobias Achterberg, the creators of SoPlex and SCIP. [stated] P

**Students: the formal record is thin, the informal record is wide**

- **Formal**: only **Leon Eifler**. MGP 342910 gives Advisor 1 Koch, Advisor 2 Gleixner, year 2025. DepositOnce gives advisor Koch, with Gleixner one of four referees and acceptance on 2024-11-08. Eifler's acknowledgements call Gleixner his second supervisor, co-author and fellow enthusiast of exact solving. MGP counts **1 student and 1 descendant** for Gleixner. [practice/observed] P/S [5][42][93]
- **Mentored, not formally supervised**: a commented-out block in his homepage source (undated) says he was mentoring the PhD projects of **Gregor Hendel, Benjamin Müller, Daniel Rehfeldt, Felipe Serrano and Jakob Witzig** at TU Berlin. [stated] P [1]
  - DepositOnce gives **Koch** as the formal advisor of all five. Gleixner is not among their referees: Hendel 2021, Müller 2020, Rehfeldt 2021, Serrano 2020, Witzig 2021. [practice] P [45]
  - Their acknowledgements describe the informal role. Witzig names him the lead of the SCIP development team, available for discussion and asking challenging questions [95]. Hendel thanks him for the group's administrative work and for an open door, day and sometimes night, to discuss papers [94]. Miltenberger (PhD 2023, advisor Koch) thanks him as a model of disciplined research who always found time for questions [96]. [observed] P
- **Interns and student assistants**: a homepage source comment names six, from TU München, Bologna, FU Berlin (two), EPFL and OVGU Magdeburg. Among them are Luca Fabbri (the Bologna STSM co-worker) and Stefan Weltge (later his co-author on OBBT). The thesis acknowledgements (p. iii) name five of them as student assistants. The other names are not repeated here. [stated] P [1][4]
- **Later co-supervised students** (co-authors of chapters in their theses; formal advisors elsewhere):
  - Antonia Chmiela: advisor Pokutta, 2025; two chapters joint with him [92].
  - Gioni Mexi: advisors Pokutta and Berthold, defence 2026-09-10; chapters 3 and 6 joint with him [97].
  - Alexander Hoen: co-author of CPAIOR 2024, CPAIOR 2025, MIP-DD and the COW 2025 talk; HTW project staff from 2025. His thesis was not found.
  - Other frequent junior co-authors: Ksenia Bestuzheva, Boro Sofranac, Mohammed Ghannam, Jasper van Doornmalen, Sander Borst and Dominik Kamp; their theses were not checked. Mark Turner (PhD 2023, advisor Koch) co-maintains MIPLIB 2017 with him; his thesis front matter does not mention Gleixner.
  - [practice] P [30][14][27][45][92][97]
- [inferred] The gap between formal and informal lineage is structural. Through 2023 his group sat at ZIB, a research institute, and every ZIB doctorate checked here was granted by TU Berlin (DepositOnce [45]). Since 2020 he has been a professor at HTW, a university of applied sciences. The formal advisors were Koch, and later Pokutta. **MGP badly undercounts his supervision.** A skill built on him should present him as a group lead and day-to-day research supervisor, but not as the formal doctoral father of the SCIP generation of 2015–2023.

---

## 3. Turns and what triggered them

### T1. Applied IP (mining) → solver research at ZIB (2006–2008 → 2008–2012)
- [practice] The UNSW honours project (2006) became the 2009 COR paper; the Diplom (2008) was on the same problem. The mining line ends with the 2012 HPSC chapter, which compares MIQCP solvers with a specialised algorithm [50][53].
- [stated] The thesis names Bley as his route to ZIB (p. iii) [4]. No stated reason for leaving the mining application was found.
- [practice] His first ZIB code work, in September 2008, was bug fixes in SoPlex and documentation edits in SCIP [20].
- [inferred] The trigger was the move into a team that owned a solver. From then on, problems came from solver components and solver users, not from one application.

### T2. MINLP components inside SCIP (2009–2015)
- [practice] The papers in this phase: Undercover (EWMINLP 2010; Math. Program. 2014; SEA 2013), MIQCP component analysis (NACO 2012), water networks (NACO 2012), OBBT and Lagrangian variable bounds (CPAIOR 2013; JOGO 2017), and branching on multi-aggregated variables (CPAIOR 2015, DOI 10.1007/978-3-319-18008-3_10) [51][52][55]–[57][62][98].
- [stated] The thesis introduction (pp. 1–2) argues why MINLP is the right place to work now. MIP solvers matured over decades, while extensive computational global optimization only began in the 1990s, so substantial progress in MINLP should be within reach [4].
- Context [practice]: projects on gas transport (MATHEON B20, 2009–2014) and water networks (Siemens) [2]. The thesis acknowledgements (p. iii) credit Vigerske with making SCIP an MINLP solver [4].

### T3. MINLP → numerically exact LP (2012–2015)
- [stated] The thesis (p. 2) gives the trigger directly: in MINLP solvers, "numerical instabilities are frequently encountered when solving linear programming (LP) relaxations". He argues that improving LP accuracy is therefore a necessary and effective step towards stable MINLP solving (paraphrase of p. 2).
- [stated] A second trigger, from the same page: multiscale ME models of bacterial growth in systems biology defeat double-precision LP solvers, which often cannot even decide feasibility reliably [4].
- [stated] On who started it, the thesis acknowledgements credit Steffy's initiative to study iterative refinement with SoPlex. The test instances came from Ali Ebrahim (p. iii) [4].
- [practice] Results: ISSAC 2012 led to IJOC 2016 (DOI 10.1287/ijoc.2016.0692) [54][99]. The thesis reports an exact SoPlex 1.85 to 3 times faster than QSopt_ex (p. 3). It also says that SoPlex became a standard plug-in of COBRApy and was installed on NEOS with 80-bit precision (p. 6). That adoption claim is [stated] and was not checked independently [4]. His SoPlex commits peak at 171 in 2013 and 369 in 2014 [20].
- [practice] The line later extends to QP, in Weber, Sager, Gleixner, *Solving quadratic programs to high precision using scaled iterative refinement*, Math. Program. Comput. 11 (2019), DOI 10.1007/s12532-019-00154-6 [100], and to theory, in Gleixner & Steffy, MP 2020 [68].

### T4. Exact LP → can floating-point MIP decisions be trusted? → certificates (2014–2016)
- [stated] The COST STSM report "Numerically Robust Integer-Feasibility" (31 Dec 2014) [7] gives the motivation:
  - Fast MIP tools use limited-precision arithmetic. That is fine for most applications, but some need high-precision or exact answers. The report's example is the energy sector: validating fair capacity distribution in gas networks (§1).
  - The goal (§2) was to test efficiently whether the integer assignments of floating-point MIP solvers are reliable, by using exact LP inside SCIP.
- [practice] He did this work in Bologna with Lodi and Fabbri; it produced a three-case classification of reliability (§4) [7]. Two years later came VIPR: initial commit 20 Nov 2016, then the IPCO 2017 paper with Cheung and Steffy [19][61].
- [inferred] The trigger was an application-class argument (energy feasibility) combined with a new tool: his own exact LP solver. The joint paper planned in the report did not appear (§6).

### T5. Researcher → group head and infrastructure lead (2015–2023)
- [practice] Group head from 1 Sep 2015 [3]. First author of the SCIP 5.0 and 6.0 release reports (2017–2018) [24]. Leader of MIPLIB 2017 (call Nov 2016, paper 2021) [34][35]. Head of Development on scipopt.org in 2021 and 2023, under Project Head Pokutta [25][26].
- [stated-joint] The MIPLIB 2017 trigger, from the paper (p. 444) [35] and the site's history page [28]:
  - The MIPLIB 2010 benchmark set no longer reflected the frontier of new challenges.
  - Of 134 MIPLIB 2010 instances open at release, 64 were solved by the end of 2018 (70 remain open).
  - The virtual-best and virtual-worst commercial solvers had sped up by factors of 2.70 and 3.62 between 2011 and 2018, roughly 16% per year from algorithms alone.
- [practice] Author position shifts: after MIPLIB 2017 (2021) and PaPILO (2023, alphabetical) DBLP lists no formal paper with him first. Students lead, and he sits last or inside an alphabetical block (§9) [43].

### T6. Industrial and energy money, and HPC (2015 → 2026)
- [practice] BEAM-ME (BMWi, 2015–2018): energy-system LPs with block structure, run on the Stuttgart and Jülich supercomputers. Outputs:
  - Breuer et al., OR 2017 proceedings, DOI 10.1007/978-3-319-89920-6_85;
  - Gleixner et al., OR 2019 proceedings, DOI 10.1007/978-3-030-48439-2_13;
  - Rehfeldt et al., EJOR 296 (2022), DOI 10.1016/j.ejor.2021.06.063;
  - and, in **2026**, the distributed structure-aware presolve for PIPS-IPM++ (arXiv 2603.03498) [101]–[103][30].
- [practice] The other industrial lines: SAP supply chain (2015–2019), Siemens (since 2015), EnBA-M (MIQCP for an urban energy network, 2018–2021) and the MODAL SynLab with FICO, GAMS, Gurobi, Siemens and SAP (2020–2023) [2][14].
- [inferred] Solver-company and industrial partners stay remarkably stable [2][14].
  - Siemens: internships 2004–2005; member of the cooperation 2008–2015 and PI from 2015; partner in EnBA-M (2018–2021) and the SynLab (2020–2023); partner in OHA4flexgrid (from 2026).
  - SAP: PI project 2015–2019; SynLab partner 2020–2023; funder of GoPPS 2025–2027.

### T7. MINLP cutting planes through students (2019–2025)
- [practice] Müller, Serrano, Gleixner, SIAM J. Optim. 30 (2020), DOI 10.1137/19M1249825. Müller et al., *On generalized surrogate duality in MINLP*, IPCO 2020 / Math. Program. 192 (2022), DOI 10.1007/s10107-021-01691-6. Serrano, Schwarz, Gleixner, JOGO 78 (2020), DOI 10.1007/s10898-020-00906-y. Perspective cuts (MPC 2023). RLT cuts with **Tobias Achterberg** (Gurobi), IPCO 2023 / MP 2025. SONC relaxations (HUGO 2022, arXiv 2211.05518; arXiv 2304.12145) [104]–[106][80][79][30].
- [inferred] The MINLP half of his thesis continues as supervision, and becomes the doctorates of Müller and Serrano (2020) and the work of Bestuzheva.

### T8. ML for MIP (2021–2023), then exit
- [practice] The line: NeurIPS 2021 (heuristic scheduling), the ML4CO competition as co-organizer, CPAIOR 2023 (online learning, with Lichocki of Google), and MATH+ EF1-9 with Pokutta (2021–2022) [18][40][77]. A 2018 ZIB-Report listed on ORCID, *Feature-Based Algorithm Selection for Mixed Integer Programming* (URN nbn:de:0297-zib-68362), may be an earlier step; its authors were not verified.
- [inferred] The trigger was institutional: Pokutta's arrival at ZIB (by 2020 he was its Vice President [10]) and a MATH+ project with a fixed term. **Exit**: no ML-titled paper with him appears after CPAIOR 2023 in DBLP or arXiv, and Chmiela finished under Pokutta [92]. No stated reason found.

### T9. GPU and first-order methods (2020 → 2023 → 2026)
- [practice] The line: GPU domain propagation (2020/2022, with Sofranac and Pokutta) [70][71]; a measure of propagation progress (CP 2021, DOI 10.4230/LIPIcs.CP.2021.52) [107]; Scylla, a primal heuristic that uses matrix-free PDHG (arXiv 2307.03466; OR 2023 proceedings, DOI 10.1007/978-3-031-58405-3_9) [108]; GoPPS with SAP (2025–2027) [14]; and **CHAP**, a GPU-CPU hybrid heuristic portfolio with cuPDLPx (arXiv 2605.05086) [30], which took **first place** in the 2026 Land-Doig MIP Competition [39].
- [observed] The 2026 trigger is explicit. The competition topic, announced 13 Oct 2025, was GPU-accelerated primal heuristics, with NVIDIA GPU credits; the organisers cite a growing momentum of GPU methods (PDLP, cuOpt) [39].
- [inferred] Here he entered early (2020) and returned in the wave (2026).

### T10. Proof logging imported from pseudo-Boolean solving (2020 → 2025)
- [practice] Work with Jakob Nordström: Devriendt et al. (Constraints 2021); Mexi et al., CP 2023 and the cut-based conflict analysis in INFORMS J. Comput. (online 2025-11-12), DOI 10.1287/ijoc.2024.0999; Hoen, Oertel, Gleixner, Nordström (CPAIOR 2024) [72][78][85][89].
- [stated-joint] The 2023 proof-system preprint describes itself as a generalization of Bogaerts, Gocht, McCreesh and Nordström (2022) from binary programs to MIP (arXiv 2311.03877 abstract) [30].
- [inferred] The VIPR idea of 2016 met an external community that already had proof-logging practice. From about 2020 he imports its formats and people instead of building alone.

### T11. Exactness into the mainline (2021 → 2025)
- [practice] The papers: Eifler & Gleixner (IPCO 2021 / MP 2023); safe Gomory cuts (SIAM J. Optim. 2024); certified propagation and dual proofs (arXiv 2403.13567); precision boosting (IJOC 2025); a posteriori numerical correctness (CPAIOR 2025) [73][74][84][30][83][88].
- [practice] The release: **SCIP 10.0.0** (GitHub release 2025-11-24). Its CHANGELOG adds a numerically exact solving mode for MILP to the core, with certification of the branch-and-bound phase. New with it: a certificate data structure, the `exactlinear` and `exactsol` constraint handlers, safe dual-proof conflict analysis, certified MIR cuts in the Gomory separator, and rational presolve through PaPILO [22][23].
- [practice] His own work: 411 SCIP commits in 2025. The search returns the newest 100 of them (Apr–Dec 2025); 54 of those messages match a keyword search for exact, rational, certif or VIPR [20]. VIPR was dormant on its default branch in 2017 and 2019–2021, with no commits by anyone, and revived from 2022 to 2025 (66 commits in 2025) [19].
- [practice] His homepage still links a SCIP branch named `exact-rational`. The GitHub API answers "Branch not found" (2026-11-08) [1][21].
- [stated] The MIP 2021 abstract frames the programme: floating-point roundoff compromises the results of virtually all fast MIP solvers, and the last milestone for exact MIP was Cook, Koch, Steffy and Wolter (2013) (paraphrase) [8].

### T12. Base moves to HTW (Oct 2020); ZIB group role ends (Mar 2023); applied portfolio (2025–2026)
- [stated] In the appointment news he says optimization is a key technology whose relevance will grow, and that he looks forward to teaching it at HTW and developing it further with students (paraphrase) [10].
- [observed] Pokutta, quoted in the same news, expects him to play a key role in the cooperation. The HTW president stresses applied research, third-party funding and partners [10].
- [practice] The projects he started from 2025 (§8) are all applied and externally funded: SAP (GoPPS); BMBF "Mathematik für Innovationen" with Charité, Labor Berlin and Vivantes (DaKoDi); EU EFRE-ProFIT (HOTSTEEL); BMWE's 8th Energy Research Programme (OHA4flexgrid); and university timetabling (OptiLEEP) [14].
- [inferred] HTW's mission and funding instruments now set many of his new problems. The solver core continues through former students and his own commits. No stated reason for ending the ZIB group role was found. That it ended on the same day as the SynLab project he led (31 Mar 2023) is noted as a coincidence, not as a cause.

---

## 4. Entry and exit timing relative to the consensus ([inferred] unless tagged)

| Topic | Entry | Exit / status | Timing relative to the field | Evidence |
|---|---|---|---|---|
| Open-pit mining IP | 2006 | after 2012 | Applied problem from his teachers; left when he joined solver work | [50][53] |
| MINLP solver components | 2009 | to students, about 2019 | Entered during MINLP's growth phase, which his thesis (pp. 1–2) argues was due | [4][55] |
| Exact and high-precision LP | 2012 | ongoing (2025 paper) | Ahead of the field. QSopt_ex (Applegate et al.) is the baseline his thesis beats; he stays 14 years | [4][54][83] |
| Verified and exact MIP | 2014–2016 | ongoing; mainline in SCIP 10 (2025) | Contrarian niche. His 2021 abstract dates the last milestone for exact MIP to 2013. Nine years from VIPR to a mainline release | [7][8][19][22] |
| Proof logging with PB/CP | about 2020 | ongoing | Importer: builds on an established external line (Bogaerts et al. 2022, as cited by his group) | [30][72] |
| Community benchmarks (MIPLIB 2017; MIP 2023 competition; ML4CO) | 2016 | MIPLIB maintenance ongoing (2026) | Consensus-maker: leads the shared instrument instead of entering a race | [27][34][40][87] |
| ML for MIP | 2021 | after 2023 | Follower. Co-organized a NeurIPS competition once the area was large enough for one; left after one funded project | [18][40][77] |
| GPU methods | 2020 | ongoing (2026) | Early first entry (2020); second entry in the 2025–2026 wave, which a competition triggered | [39][70] |
| Energy-system LP on HPC | 2015 | ongoing (2026 preprint) | Driven by funding and application; long-lived (11 years) | [2][101]–[103] |
| Applied HTW projects (medicine, logistics, grids, timetabling) | 2025–2026 | started 2025–2026 | New fields driven by funding calls and partners, not by the solver frontier | [14] |

---

## 5. Era and resource context of each practice

| Period | Position and seniority | Resources and tools | Team | Source |
|---|---|---|---|---|
| 2004–2008 | Student; scholarships (Merit Foundation, DAAD); Siemens internships | UNSW honours room; LP-based disaggregation for mining | Supervisors Froyland, Möhring | [2][4] |
| 2008–2015 | Research assistant in ZIB's Department of Optimization; PhD student | SCIP (Achterberg) and SoPlex (Wunderling) code bases; ZIB clusters; GMP rational arithmetic for exact LP; the Ipet evaluation tool (Hendel); test sets from MIPLIB and from Ebrahim (metabolic networks). Funding: BMS, MODAL (BMBF), COST TD1207 (EU), MATHEON, Siemens. He also did maintenance work on SCIP and SoPlex: the thesis thanks Gamrath and Miltenberger for taking it over when he needed it (p. iii) | The 2012 suite report (ZIB-Report 12-27) has 6 authors; the first large release reports, 3.2 (Feb 2016) and 4.0 (Mar 2017), have 21 each | [2][4][24] |
| 2015–2023 | Group head; SCIP head of development (2021, 2023); PI of third-party projects | HPC at Stuttgart and Jülich (BEAM-ME); industry money (SAP, Siemens); BMBF SynLab with FICO, GAMS, Gurobi, Siemens and SAP; MATH+; GitHub mirrors from 2021; Apache 2.0 licence from SCIP 8.0.3 (CHANGELOG) | Group of 16 in July 2017 (2 senior researchers, 10 research assistants, 4 student assistants); release-report author lists of 31–35 from 8.0 on | [2][14][17][21][22][24] |
| 2020– | Professor at HTW Berlin (teaching in business mathematics); ZIB guest or affiliated researcher | Applied funding instruments (SAP, BMBF, EU EFRE, BMWE); GPUs (NVIDIA credits in the 2026 competition; cuPDLPx in CHAP); SCIP 10 with exact mode | HTW project staff (Hoen, Masing) plus ZIB co-authors (Mexi, Kempke, Koch, Pokutta, Berthold) | [3][14][30][39] |

---

## 6. Failures, abandoned directions, unrealized plans (dated)

1. **A joint paper planned in 2014 that never appeared.** [stated] The STSM report (§5) plans a common publication with the Bologna group for a computational journal, to be submitted by autumn 2015. It also promises a SCIP constraint handler in a coming release [7]. [practice] No paper with Lodi and Fabbri on this topic is found in DBLP, ORCID or arXiv (checked 2026-11-08) [3][30][43]. [inferred] The question, whether floating-point B&B decisions are numerically correct, returned ten years later with a different student: Hoen & Gleixner (arXiv Dec 2024; CPAIOR 2025) [88]. Whether the constraint handler shipped was not verified.
2. **Application lines left after one to three papers** [practice]: open-pit mining (2006–2012); water supply networks (2011–2012); wireless network design (ISCO 2016 only; [inferred] it echoes his 2005 Siemens internship topic); recursive circle packing (2017–2020); Markov-process cycle detection (Multiscale Model. Simul. 16 (2018), DOI 10.1137/16M1091162 [109]), whose graph-partition side returns in ISCO 2024 [86]; dynamic vehicle routing (arXiv 2307.11800, published in the OR 2023 proceedings, DOI 10.1007/978-3-031-58405-3_35 [110]). No stated reasons found.
3. **ML for MIP left after 2023** (T8) [inferred]. No stated reason.
4. **SONC relaxations**: a 4-page HUGO 2022 proceedings paper (arXiv 2211.05518) and arXiv 2304.12145. No journal version found in DBLP or ORCID [practice]. Whether it was rejected is not observable.
5. **VetOpt for felmo (2022–2023)**: no publication found [practice] [14].
6. **Slow road to a mainline release (not a failure)**: exact MIP lived outside SCIP's release line from the 2013 Cook et al. framework [8] through the `exact-rational` branch named on his homepage [1], and reached a release only with SCIP 10.0.0 in November 2025 [22][23]. The VIPR repository had no commits in 2017 or 2019–2021 [19]. [inferred] Persistence over about nine years is itself a trait; so is accepting long dormancy.
7. **Long review paths** [practice]: Chvátal's conjecture paper, arXiv Sep 2018 → TOMS received Sep 2020 → published May 2022 [76]; perspective cuts, received Mar 2021 → accepted May 2023 [80]; MIPLIB 2017, received Jul 2019 → accepted Sep 2020 [34]. Earlier submissions elsewhere are not observable.
8. **Errata and retractions**: none found. A Crossref author query (156 items with a Gleixner author, 2026-11-08) showed no correction, erratum or retraction notice [111].
9. **No award found** [observed]:
   - One WebSearch for prizes returned nothing about him.
   - Grötschel's student list shows a dissertation award for Berthold but none for Gleixner [44].
   - The MPC Outstanding Paper award for 2021, the print year of the MIPLIB 2017 paper, went to the Minotaur paper [46].
   - The only competitive distinction found is the team first place in the 2026 Land-Doig competition [39].

   An absence of evidence is not evidence of absence.

---

## 7. Hands-on coding trajectory (practice)

GitHub commit search, author name containing "Gleixner", default branch, run on 2026-11-08 [19][20]. The counts are approximate: the search covers only the default branch, so commits that live only on other branches are missed. The per-year sums match the totals: 1608 for SCIP and 1038 for SoPlex. PaPILO: 7 commits, 2020-08-19 → 2022-07-15.

| Year | SCIP | SoPlex | VIPR (his / all) | Context [inferred] |
|---|---|---|---|---|
| 2008 | 7 | 33 | — | joins ZIB (Sept) |
| 2009 | 43 | 91 | — | MINLP components |
| 2010 | 69 | 65 | — | |
| 2011 | 59 | 72 | — | |
| 2012 | 124 | 79 | — | iterative refinement (ISSAC) |
| 2013 | 65 | 171 | — | exact SoPlex |
| 2014 | 83 | **369** | — | exact SoPlex; thesis experiments |
| 2015 | 23 | 58 | — | defence; group head from Sept |
| 2016 | 10 | 13 | 16 / 29 | VIPR starts |
| 2017 | **144** | 16 | 0 / 0 | SCIP 5.0 lead |
| 2018 | **134** | 8 | 2 / 2 | SCIP 6.0 lead |
| 2019 | 2 | 0 | 0 / 0 | MIPLIB 2017 paper submitted (Jul) |
| 2020 | 156 | 32 | 0 / 0 | HTW from Oct; SCIP 7.0 |
| 2021 | 165 | 5 | 0 / 0 | |
| 2022 | 43 | 2 | 2 / 11 | |
| 2023 | 53 | 2 | 9 / 10 | group role ends (Mar) |
| 2024 | 12 | 2 | 1 / 24 | |
| 2025 | **411** | 20 | **29 / 66** | exact mode, then SCIP 10.0 (Nov) |
| 2026 (to Nov 8) | 5 | 0 | 0 / 5 | `cons_exactlinear.c` and `certificate.cpp` (Aug, Oct) |

[inferred] He never stopped coding. Even as a professor he commits in bursts timed to releases and to the exactness push. The SoPlex peak belongs to his PhD; the SCIP peaks belong to his release-lead years (2017–2018), the years 2020–2021, and the exact-mode integration (2025).

---

## 8. The last 12 months (2025-11-08 → 2026-11-08)

| Date | Item | Tag | Source |
|---|---|---|---|
| 10 Nov 2025 | arXiv 2511.07143, *Branch and price for nonlinear production-maintenance scheduling in complex machinery* (Dionísio, Gleixner, Pedroso, Bestuzheva) | [practice] P | [30] |
| 12 Nov 2025 | Online in INFORMS J. Comput.: Mexi, Serrano, Berthold, Gleixner, Nordström, *Cut-Based Conflict Analysis in Mixed Integer Programming*, DOI 10.1287/ijoc.2024.0999 | [practice] P | [89] |
| 23–24 Nov 2025 | *The SCIP Optimization Suite 10.0* (arXiv 2511.18580, 34 authors; he is 9th, with Hojny first and the rest alphabetical), with the exact solving mode, cut-based conflict analysis and MIP-DD. SCIP v10.0.0 released on GitHub on 24 Nov | [practice] P | [32][23] |
| 19 Dec 2025 | arXiv 2512.17551, *Clique Probing for Mixed-Integer Programs* (von Holly-Ponientzietz, Hoen, Turner, Gleixner), in PaPILO | [practice] P | [30] |
| 26 Jan 2026 | MIPLIB 2017 solution file 36 (40 better incumbents). He is a listed maintainer, with Mark Turner | [observed] P | [27] |
| 1 Feb 2026 | **DaKoDi** starts (BMBF, to 31 Jan 2029): cost- and data-based optimization of early diagnosis for clinically relevant, poorly understood diseases, with Charité, Labor Berlin, Vivantes and ZIB | [practice] P | [14] |
| Mar 2026 | INFORMS J. Comput. 38:414–423: Hoen, Kamp, Gleixner, *MIP-DD: Delta Debugging for Mixed-Integer Programming Solvers*, DOI 10.1287/ijoc.2024.0844 | [practice] P | [90] |
| 3 Mar 2026 (v2 20 Oct) | arXiv 2603.03498, *Distributed Parallel Structure-Aware Presolving for Arrowhead Linear Programs* (ZIB-Report 26-01). The 2015 BEAM-ME line, still alive | [practice] P | [30][15] |
| 1 Apr 2026 | **HOTSTEEL** starts (EU EFRE-ProFIT with the Land Berlin, to 31 Mar 2029): energy-efficient logistics, with TU Berlin, JCMwave and PSI | [practice] P | [14] |
| 6 May 2026 | arXiv 2605.05086, *CHAP: A Hybrid GPU-CPU Heuristic for MIP* (8 authors incl. Berthold, Koch, Pokutta) | [practice] P | [33] |
| 19 May 2026 | **First place, 2026 Land-Doig MIP Competition**, for CHAP. The MIP Workshop 2026 ran 18–21 May at the University of Connecticut, Stamford; the results were presented on 19 May. Gioni Mexi received the award for the team. No evidence that Gleixner attended | [observed] P | [38][39] |
| 28 May 2026 | arXiv 2605.29686, *Boolean Algebra -- Driven Sepsis Diagnosis* (Weber, Kappert, Reidelbach, Gleixner, Fackeldey, Bauer). HTW lists it as a DaKoDi publication | [practice] P | [30][14] |
| 17 Jul 2026 | arXiv 2607.15837, *A Numerically-safe Branch-Price-and-Cut Algorithm for the Length-Constrained Cycle Partition Problem* (Ghannam, Gleixner, Mexi, Lam). It closes 14 previously unsolved instances with numerically safe bounds (abstract) | [practice] P | [30] |
| 1 Aug 2026 | **OptiLEEP** starts (to 31 Jan 2027): decision support for teaching-load and exam planning at universities; co-led with Berenike Masing | [practice] P | [14] |
| 22 Aug 2026 | SCIP commit by him (fix for an assertion in `sorttpl.c`) | [practice] P | [20] |
| 10 Sep 2026 | Gioni Mexi's PhD defence (advisors Pokutta and Berthold). Chapters 3 and 6 are joint with Gleixner | [observed] P | [97] |
| 24 Sep 2026 | MIPLIB 2017 solution file 37 (51 better incumbents) | [observed] P | [27] |
| 1 Oct 2026 | **OHA4flexgrid** starts (BMWE, 8th Energy Research Programme, to 30 Sep 2029): higher utilisation of medium-voltage distribution grids, with OTH Regensburg, Siemens and others | [practice] P | [14] |
| 23–25 Oct 2026 | SCIP commits by him in `cons_exactlinear.c` (removing an unnecessary invalidation of absolute values) and `certificate.cpp`. **Latest dated hands-on trace** | [practice] P | [20] |
| standing, 2026-11-08 | ZIB position "Guest". The SCIP site lists him as a contact for "other groups"; Gioni Mexi (ZIB) is the primary contact. MPC Associate Editor | [observed] P | [15][24][41] |

**Not found in the window**: no talk with him as speaker (two WebSearches [113] and the MIP Workshop pages [38][39]); no sole-authored paper; no move.

---

## 9. Pointers for the synthesis (all [inferred])

1. **Problem source**: his problems come from the solver he maintains and from its numerics. Applications (systems biology, energy and gas networks, computer-assisted mathematics such as Chvátal's conjecture) serve as arguments for exactness, not as the destination. A skill should ask: what does this do to the solver, and can it be trusted in exact arithmetic?
2. **Timing**: he enters early and stays long where the solver core is at stake (exactness: 2012 →), but follows the waves and leaves them (ML, 2021–2023). GPU work came in twice: early in 2020, and in the 2025–2026 wave, when a competition supplied the trigger.
3. **Infrastructure as research**: the most-cited items on his Google Scholar profile are MIPLIB 2010, MIPLIB 2017 and SCIP release reports (WebFetch summary, unverified [47]). He invests in shared instruments: libraries, release reports, competitions and a delta debugger.
4. **Organisation**: a group lead whose name is absent from the formal doctoral records (§2), who codes in release-timed bursts (§7), and who imports outside expertise (Nordström; Achterberg on RLT; Lodi and Khalil on ML).
5. **Since 2025**: an applied-project portfolio at HTW sits alongside the ZIB solver core. The skill should mark which voice is meant: the exact-MIP and solver-engineering voice, or the applied-OR project lead.
6. **Layer 5 (judging results)**: he answers the question of whether a solver result can be trusted in two ways: rational re-checking (the STSM's three cases; the a posteriori analysis of 2024–2025) and independently checkable certificates (VIPR).

---

## Contradictions (kept, not reconciled)

1. **Who were his PhD advisors?**
   - DepositOnce: advisor Grötschel only; Koch and Lodi are referees [5].
   - MGP: Advisor 1 Grötschel, Advisor 2 Koch [42].
   - Thesis title page: all three are listed equally as Berichter (reviewers) [4].
   - Homepage and CV: all three as "Committee" [1][2].
2. **Eifler's supervision.**
   - DepositOnce: advisor Koch, with Gleixner one of four referees [5].
   - MGP: Gleixner is Advisor 2, and the year is 2025, although the defence date is 2024-11-08 [42].
   - Eifler: calls him his second supervisor [93].
3. **Mentoring versus the formal record.** His homepage source says he mentored the PhD projects of Hendel, Müller, Rehfeldt, Serrano and Witzig [1]. DepositOnce lists Koch as their advisor, and Gleixner is not among their referees [45].
4. **MODAL membership start**: the 2017 CV lists 2013–2019 as a member of the research campus [2]; the homepage says 2014–present [1].
5. **MATHEON period**: homepage 2008–2014 [1]; CV project list 2009–2014 (B20) [2].
6. **The thesis's "accepted" date**: DSpace gives dc.date.accepted 2015-06-24, the defence date [5]. DataCite gives "Accepted" 2016-01-13, the repository accession date [6].
7. **Current ZIB status**: the homepage says affiliated researcher in the MAI division [1]; the ZIB member page says "Guest" in group Prescriptive Systems [15]. According to the WebFetch summary (unverified), Google Scholar's affiliation line still reads Department Optimization, ZIB, six years into the HTW professorship [47].
8. **The homepage is current and stale at once.** It lists the 2015–2023 group-head role, so it was edited in 2023 or later, yet its footer says © 2008–2022. It also still points to an `exact-rational` branch that GitHub reports as not found [1][21].
9. **VIPR dates**: the CV says VIPR has existed since 2016, and the initial commit is 2016-11-20. The GitHub repository `scipopt/vipr` was created on 2024-02-22, so the history was imported [2][19][21].
10. **Year of the supply-chain paper**: ORCID dates it 2019; Crossref gives volume 37 and an online/issued date of 2021-07-01 [3][58].
11. **arXiv identity**: the `au:Gleixner_A` query returns 27 ANTARES astroparticle papers of another A. Gleixner [31]. A full-name query returns his 48 [30]. DBLP and ORCID are clean [43][3].

## Gaps

- **Stated reasons not found** for: leaving open-pit mining (2012); leaving ML for MIP (after 2023); ending the ZIB group-head role (31 Mar 2023); the shift from "Head of Development" (2023-01 snapshot) to being one of the contact persons for "other groups" (2026). That shift happened between Jan 2023 and Nov 2026; later Wayback snapshots returned HTTP 429.
- **The HTW move**: only the cooperation framing and his teaching quote were found [10]. The news item is undated; 2020 is inferred from the October start and the ORCID date.
- **Talks**: no talk with him as speaker found for Nov 2025 → Nov 2026. Two talks are known only from search snippets: a Simons Institute talk, apparently Spring 2021, titled "Exact Mixed-Integer Programming over the Rational Numbers", and an Argonne MCS talk, "Hybrid-precision algorithms in a safe and verified MIP framework", whose date was not found. Both pages are behind a Cloudflare challenge and were not opened. Post-2017 talks in general are thinly covered; the CV lists talks only until early 2017.
- **ZIB-Reports**: ZIB OPUS sits behind an Anubis wall, so items such as ZIB-Report 12-36 rest only on his CV. The authors of the 2018 ZIB-Report *Feature-Based Algorithm Selection for Mixed Integer Programming* were not verified.
- **Outputs not found**: gas-transport work (MATHEON B20; no paper under his name found); the Siemens cooperation; VetOpt; the constraint handler promised in the 2014 STSM report.
- **Teaching at HTW**: which courses he teaches was not verified. Whether he supervises doctorates through HTW was not verified.
- **Kempke's PhD** (2026, co-author of the presolve and CHAP work): the thesis is not in DepositOnce yet, so Gleixner's formal role is unknown. Hoen's thesis was not found.
- **Rejected papers**: not observable in public records.
- **Google Scholar numbers** (5496 citations, h-index 31; yearly counts rising to 799 in 2026): from a WebFetch model summary, not independently checked [47].

---

## Sources

**Primary: by or with Gleixner, his records and code**

1. A. Gleixner, homepage, https://www.zib.de/userpage/gleixner/ (visible text and HTML source comments; read 2026-11-08). P
2. A. Gleixner, *Curriculum Vitae of Ambros Gleixner*, updated 31 July 2017, 7 pp., https://www.zib.de/userpage/gleixner/gleixner.pdf (read in full). P
3. ORCID record 0000-0003-0391-5903, https://pub.orcid.org/v3.0/0000-0003-0391-5903/record (employments; 93 works). P
4. A. M. Gleixner, *Exact and fast algorithms for mixed-integer nonlinear programming*, PhD thesis, TU Berlin, 2015, DOI 10.14279/depositonce-4938 (title page, abstract, acknowledgements pp. iii–iv, introduction pp. 1–6 read). P
5. DepositOnce REST metadata, items 11303/5244 (Gleixner) and the Eifler item, https://api-depositonce.tu-berlin.de/server/api/ (advisor, referees, dc.date.accepted). P
6. DataCite record for DOI 10.14279/depositonce-4938, https://api.datacite.org/dois/10.14279/depositonce-4938. P
7. A. M. Gleixner, *Scientific Report on the STSM "Numerically Robust Integer-Feasibility"*, COST TD1207, 31 Dec 2014, https://cost-td1207.zib.de/sites/default/files/scientific_report_gleixner.pdf (read in full). P
8. A. Gleixner, talk "Exact mixed-integer programming: a status update on MIP solving without numerical errors", MIP Workshop 2021 (online), 25 May 2021, https://researchseminars.org/talk/MIP2021/8/ (abstract). P
9. A. Gleixner, A. Hoen, abstract "An a posteriori analysis of numerical correctness in LP-based branch and bound", COW 2025, https://cow25.sciencesconf.org/601453; programme https://cow25.sciencesconf.org/program (talk on 9 Jan 2025). P
10. ZIB news, "Cooperation starts with a professorial appointment" (undated; 2020), https://www.zib.de/news/htw-berlin-enters-cooperation-zuse-institute-berlin. P
11. Research Campus MODAL news, same text, https://forschungscampus-modal.de/htw-berlin-kooperiert-mit-zuse-institut-berlin?lang=en. P
12. HTW Berlin, Wirtschaftsmathematik people page, https://wm.htw-berlin.de/personen (subject areas). P
13. HTW Berlin research catalogue, "Projekte von Prof. Dr. Ambros Gleixner", https://www.htw-berlin.de/forschung/online-forschungskatalog/projekte/person/?eid=12822. P
14. HTW Berlin project pages eid 3135 (MODAL SynLab), 3136 (MATH+ EF1-9), 3137 (EnBA-M), 3153 (VetOpt), 3767 (GoPPS), 3802 (DaKoDi), 3895 (HOTSTEEL), 3939 (OptiLEEP), 3949 (OHA4flexgrid), https://www.htw-berlin.de/forschung/online-forschungskatalog/projekte/projekt?eid=…; funders, partners and durations read 2026-11-08. P
15. ZIB member page, https://www.zib.de/members/gleixner (position "Guest"; division, department and group; projects; 2025–2026 publications incl. ZIB-Report 26-01). P
16. ZIB division page, Mathematical Algorithmic Intelligence, https://www.zib.de/research/mai. P
17. ZIB project pages BEAM-ME (https://www.zib.de/research/projects/beam-me) and EnBA-M (https://www.zib.de/research/projects/energienetz-berlin-adlershof). P
18. MATH+, project EF1-9, "Adaptive Algorithms through Machine Learning: Exploiting Interactions in Integer Programming", https://mathplus.de/research-2/emerging-fields/ef1-extracting-dynamical-laws-from-complex-data/ef1-9/. P
19. GitHub scipopt/vipr, commit history (147 commits, 2016-11-20 → 2026-10-24; 59 by Gleixner), https://github.com/scipopt/vipr. P
20. GitHub commit search, `repo:scipopt/{scip,soplex,papilo} author-name:Gleixner`, totals and per-year counts, plus samples of the 2019, 2025 and 2026 messages (run 2026-11-08). P
21. GitHub API repository metadata for scipopt/vipr, soplex, scip and papilo (creation dates, licence), and `branches/exact-rational` ("Branch not found"). P
22. SCIP CHANGELOG (master): sections for 10.0.0 (exact solving) and 8.0.3 (Apache 2.0 licence), https://raw.githubusercontent.com/scipopt/scip/master/CHANGELOG. P
23. GitHub releases scipopt/scip (v10.0.0 2025-11-24; v10.0.1 2026-02-03; v10.0.2 2026-04-02; v10.0.3 2026-07-06; v10.1.0 2026-09-18). P
24. scipopt.org, live page (citation list of release reports; contact persons; current developers), https://www.scipopt.org/ (2026-11-08). P
25. scipopt.org, Wayback snapshot 2021-01-18, http://web.archive.org/web/20210118191607/https://www.scipopt.org/. P
26. scipopt.org, Wayback snapshot 2023-01-04, http://web.archive.org/web/20230104101425/https://www.scipopt.org/. P
27. MIPLIB 2017 website, index page, https://miplib.zib.de/ (maintainers Gleixner and Turner; news incl. solution files 36 and 37; read 2026-11-08). P
28. MIPLIB 2017 website, history page, https://miplib.zib.de/history.html (why the 2017 edition; automated selection). P
29. MIPLIB 2017 website, news page, https://miplib.zib.de/news.html (dated entries from Nov 2018). P
30. arXiv API, full-name query "Ambros Gleixner" OR "Ambros M. Gleixner" (48 preprints, 2016-04-02 → 2026-07-17). Metadata read for all; abstracts read for 2511.18580, 2605.05086, 2605.29686, 2603.03498, 2512.17551, 2511.07143, 2607.15837, 2412.14710, 2307.11800, 2307.03466, 1702.07799, 2403.13567, 2401.17937, 2311.03877, 2304.12145. P
32. C. Hojny et al. (34 authors incl. A. Gleixner), *The SCIP Optimization Suite 10.0*, arXiv 2511.18580 (2025-11-23; abstract read). P
33. G. K. Tjusila, A. Hoen, N.-C. Kempke, G. Mexi, T. Berthold, A. Gleixner, T. Koch, S. Pokutta, *CHAP: A Hybrid GPU-CPU Heuristic for MIP*, arXiv 2605.05086 (2026-05-06; abstract read). P
35. A. Gleixner, G. Hendel, G. Gamrath, T. Achterberg, M. Bastubbe, T. Berthold, P. Christophel, K. Jarck, T. Koch, J. Linderoth, M. Lübbecke, H. D. Mittelmann, D. Ozyurt, T. K. Ralphs, D. Salvagnin, Y. Shinano, *MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library*, Math. Program. Comput. 13:443–490 (2021), DOI 10.1007/s12532-020-00194-3 (open-access full text; pp. 443–446 read: motivation, committee, submission phase). P
36. T. Koch et al., *MIPLIB 2010*, Math. Program. Comput. 3:103–163 (2011), DOI 10.1007/s12532-011-0025-9. P
37. MIP Workshop 2025 home page, https://www.mixedinteger.org/2025/ (the competition renamed Land-Doig in 2025). P
38. MIP Workshop 2026 home page, https://www.mixedinteger.org/2026/ (18–21 May 2026, UConn Stamford; winners). P
39. MIPcc26, *The 2026 Land-Doig MIP Competition*, https://www.mixedinteger.org/2026/competition/ (topic, timeline, NVIDIA support, results, committee). P
40. ML4CO competition page (NeurIPS 2021), https://www.ecole.ai/2021/ml4co-competition/ (organizers; supporting organizations). P
41. Mathematical Programming Computation, editorial board, https://link.springer.com/journal/12532/editorial-board (Gleixner, Associate Editor; read 2026-11-08). P
44. M. Grötschel, list of PhD students, https://www.zib.de/userpage/groetschel/students/doctoralstudents.html. P
45. DepositOnce metadata for the PhD theses of G. Hendel (2021), B. Müller (2020), D. Rehfeldt (2021), F. Serrano Musalem (2020), J. Witzig (2021), M. Miltenberger (2023), M. Turner (2023), G. Gamrath (2020), K. Jarck (2019), R. Lenz (2021), J. Pulaj (2017), via https://api-depositonce.tu-berlin.de/server/api/discover/search/objects?query=Gleixner. P
50. N. Boland, I. Dumitrescu, G. Froyland, A. M. Gleixner, *LP-based disaggregation approaches to solving the open pit mining production scheduling problem with block processing selectivity*, Comput. Oper. Res. 36:1064–1089 (2009), DOI 10.1016/j.cor.2007.12.006. P
51. A. M. Gleixner, H. Held, W. Huang, S. Vigerske, *Towards globally optimal operation of water supply networks*, NACO 2(4):695–711 (2012), DOI 10.3934/naco.2012.2.695. P
52. T. Berthold, A. M. Gleixner, S. Heinz, S. Vigerske, *Analyzing the computational impact of MIQCP solver components*, NACO 2(4):739–748 (2012), DOI 10.3934/naco.2012.2.739. P
53. A. Bley, A. M. Gleixner, T. Koch, S. Vigerske, *Comparing MIQCP Solvers to a Specialised Algorithm for Mine Production Scheduling*, HPSC 2009 proceedings, Springer 2012, 25–39, DOI 10.1007/978-3-642-25707-0_3. P
54. A. M. Gleixner, D. E. Steffy, K. Wolter, *Improving the accuracy of linear programming solvers with iterative refinement*, ISSAC 2012, 187–194, DOI 10.1145/2442829.2442858. P
55. T. Berthold, A. M. Gleixner, *Undercover: a primal MINLP heuristic exploring a largest sub-MIP*, Math. Program. 144:315–346 (2014), DOI 10.1007/s10107-013-0635-2. P
56. A. M. Gleixner, S. Weltge, *Learning and Propagating Lagrangian Variable Bounds for Mixed-Integer Nonlinear Programming*, CPAIOR 2013, LNCS 7874, 355–361, DOI 10.1007/978-3-642-38171-3_26. P
57. T. Berthold, A. M. Gleixner, *Undercover Branching*, SEA 2013, LNCS, 212–223, DOI 10.1007/978-3-642-38527-8_20. P
58. G. Gamrath, A. Gleixner, T. Koch, M. Miltenberger, D. Kniasew, D. Schlögel, A. Martin, D. Weninger, *Tackling Industrial-Scale Supply Chain Problems by Mixed-Integer Programming*, J. Comput. Math. 37:866–888, DOI 10.4208/jcm.1905-m2019-0055. P
59. A. Gleixner, C. Kirches, J. Mitchell, T. K. Ralphs, *Preface*, Optim. Methods Softw. 33(3):419 (2018), DOI 10.1080/10556788.2018.1459255. P
60. F. D'Andreagiovanni, A. M. Gleixner, *Towards an Accurate Solution of Wireless Network Design Problems*, ISCO 2016, LNCS, 135–147, DOI 10.1007/978-3-319-45587-7_12. P
61. K. K. H. Cheung, A. Gleixner, D. E. Steffy, *Verifying Integer Programming Results*, IPCO 2017, LNCS, 148–160, DOI 10.1007/978-3-319-59250-3_13 (arXiv 1611.08832). P
62. A. M. Gleixner, T. Berthold, B. Müller, S. Weltge, *Three enhancements for optimization-based bound tightening*, J. Glob. Optim. 67:731–757 (2017), DOI 10.1007/s10898-016-0450-4. P
63. S. Vigerske, A. Gleixner, *SCIP: global optimization of mixed-integer nonlinear programs in a branch-and-cut framework*, Optim. Methods Softw. 33:563–593 (2018), DOI 10.1080/10556788.2017.1335312. P
64. P. Bonami, A. M. Gleixner, J. Linderoth, R. Misener, *Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization (Dagstuhl Seminar 18081)*, Dagstuhl Reports 8(2):64–87 (2018), DOI 10.4230/DagRep.8.2.64. P
65. F. Furini et al., *QPLIB: a library of quadratic programming instances*, Math. Program. Comput. 11:237–265 (2019), DOI 10.1007/s12532-018-0147-4. P
66. A. Gleixner, S. J. Maher, B. Müller, J. P. Pedroso, *Price-and-verify: a new algorithm for recursive circle packing using Dantzig–Wolfe decomposition*, Ann. Oper. Res. 284:527–555 (2020), DOI 10.1007/s10479-018-3115-5. P
67. A. Gleixner, D. E. Steffy, *Linear Programming Using Limited-Precision Oracles*, IPCO 2019, LNCS, 399–412, DOI 10.1007/978-3-030-17953-3_30. P
68. A. Gleixner, D. E. Steffy, *Linear programming using limited-precision oracles*, Math. Program. 183:525–554 (2020), DOI 10.1007/s10107-019-01444-6. P
69. J. Witzig, A. Gleixner, *Conflict-Driven Heuristics for Mixed Integer Programming*, INFORMS J. Comput. 33:706–720 (2021), DOI 10.1287/ijoc.2020.0973. P
70. B. Sofranac, A. Gleixner, S. Pokutta, *Accelerating Domain Propagation: An Efficient GPU-Parallel Algorithm over Sparse Matrices*, IA3 workshop at SC20, 2020, 1–11, DOI 10.1109/IA351965.2020.00007. P
71. B. Sofranac, A. Gleixner, S. Pokutta, *Accelerating domain propagation: An efficient GPU-parallel algorithm over sparse matrices*, Parallel Comput. 109:102874 (2022), DOI 10.1016/j.parco.2021.102874. P
72. J. Devriendt, A. Gleixner, J. Nordström, *Learn to relax: Integrating 0-1 integer linear programming with pseudo-Boolean conflict-driven search*, Constraints 26:26–55 (2021), DOI 10.1007/s10601-020-09318-x. P
73. L. Eifler, A. Gleixner, *A Computational Status Update for Exact Rational Mixed Integer Programming*, IPCO 2021, LNCS 12707, 163–177, DOI 10.1007/978-3-030-73879-2_12. P
74. L. Eifler, A. Gleixner, *A computational status update for exact rational mixed integer programming*, Math. Program. 197:793–812 (2023), DOI 10.1007/s10107-021-01749-5. P
75. K. Bestuzheva et al., *Enabling Research through the SCIP Optimization Suite 8.0*, ACM Trans. Math. Softw. 49 (2023), DOI 10.1145/3585516 (arXiv 2112.08872; 2303.07101). P
76. L. Eifler, A. Gleixner, J. Pulaj, *A Safe Computational Framework for Integer Programming Applied to Chvátal's Conjecture*, ACM Trans. Math. Softw. 48 (2022), DOI 10.1145/3485630 (arXiv 1809.01572). P
77. A. Chmiela, A. Gleixner, P. Lichocki, S. Pokutta, *Online Learning for Scheduling MIP Heuristics*, CPAIOR 2023, LNCS, 114–123, DOI 10.1007/978-3-031-33271-5_8 (arXiv 2304.03755). P
78. G. Mexi, T. Berthold, A. Gleixner, J. Nordström, *Improving Conflict Analysis in MIP Solvers by Pseudo-Boolean Reasoning*, CP 2023, LIPIcs, DOI 10.4230/LIPIcs.CP.2023.27 (DataCite). P
79. K. Bestuzheva, A. Gleixner, T. Achterberg, *Efficient Separation of RLT Cuts for Implicit and Explicit Bilinear Products*, IPCO 2023, LNCS, 14–28, DOI 10.1007/978-3-031-32726-1_2; extended as *Efficient separation of RLT cuts for implicit and explicit bilinear terms*, Math. Program. 210:47–74 (2025), DOI 10.1007/s10107-024-02104-0. P
80. K. Bestuzheva, A. Gleixner, S. Vigerske, *A computational study of perspective cuts*, Math. Program. Comput. 15:703–731 (2023), DOI 10.1007/s12532-023-00246-4. P
81. A. Gleixner, L. Gottwald, A. Hoen, *PaPILO: A Parallel Presolving Library for Integer and Linear Optimization with Multiprecision Support*, INFORMS J. Comput. 35:1329–1341 (2023), DOI 10.1287/ijoc.2022.0171 (arXiv 2206.10709). P
82. B. Müller, G. Muñoz, M. Gasse, A. Gleixner, A. Lodi, F. Serrano, *On Generalized Surrogate Duality in Mixed-Integer Nonlinear Programming*, IPCO 2020, DOI 10.1007/978-3-030-45771-6_25; Math. Program. 192:89–118 (2022), DOI 10.1007/s10107-021-01691-6. P
83. L. Eifler, J. Nicolas-Thouvenin, A. Gleixner, *Combining Precision Boosting with LP Iterative Refinement for Exact Linear Optimization*, INFORMS J. Comput. 37:933–944 (2025), DOI 10.1287/ijoc.2023.0409 (arXiv 2311.08037). P
84. L. Eifler, A. Gleixner, *Safe and Verified Gomory Mixed-Integer Cuts in a Rational Mixed-Integer Program Framework*, SIAM J. Optim. 34:742–763 (2024), DOI 10.1137/23M156046X (arXiv 2303.12365). P
85. A. Hoen, A. Oertel, A. Gleixner, J. Nordström, *Certifying MIP-Based Presolve Reductions for 0–1 Integer Linear Programs*, CPAIOR 2024, LNCS, 310–328, DOI 10.1007/978-3-031-60597-0_20. P
86. L. Eifler, J. Witzig, A. Gleixner, *Branch and Cut for Partitioning a Graph into a Cycle of Clusters*, ISCO 2024, LNCS, 97–108, DOI 10.1007/978-3-031-60924-4_8. P
87. S. Bolusani, M. Besançon, A. Gleixner, T. Berthold, C. D'Ambrosio, G. Muñoz, J. Paat, D. Thomopulos, *The MIP Workshop 2023 Computational Competition on reoptimization*, Math. Program. Comput. 16:255–266 (2024), DOI 10.1007/s12532-024-00256-w. P
88. A. Hoen, A. Gleixner, *Analyzing the Numerical Correctness of Branch-and-Bound Decisions for Mixed-Integer Programming*, CPAIOR 2025, LNCS, 35–50, DOI 10.1007/978-3-031-95976-9_3 (arXiv 2412.14710). P
89. G. Mexi, F. Serrano, T. Berthold, A. Gleixner, J. Nordström, *Cut-Based Conflict Analysis in Mixed Integer Programming*, INFORMS J. Comput., online 2025-11-12, DOI 10.1287/ijoc.2024.0999 (arXiv 2410.15110). P
90. A. Hoen, D. Kamp, A. Gleixner, *MIP-DD: Delta Debugging for Mixed-Integer Programming Solvers*, INFORMS J. Comput. 38:414–423 (2026), DOI 10.1287/ijoc.2024.0844 (arXiv 2405.19770). P
91. N.-C. Kempke, S. J. Maher, D. Rehfeldt, A. Gleixner, T. Koch, S. Uslu, *Distributed Parallel Structure-Aware Presolving for Arrowhead Linear Programs*, arXiv 2603.03498 (v1 2026-03-03, v2 2026-10-20). P

**Primary: first-hand observers (students' theses)**

92. A. Chmiela, *Advancing mixed-integer programming using data-driven and deduction-based methods*, PhD thesis, TU Berlin, 2025, DOI 10.14279/depositonce-24040 (front matter and contributions list read). P
93. L. Eifler, *Algorithms and certificates for exact Mixed Integer Programming*, PhD thesis, TU Berlin, defended 2024-11-08, DOI 10.14279/depositonce-23941 (committee page and acknowledgements read). P
94. G. C. Hendel, *Adaptive solver behavior in mixed-integer programming*, PhD thesis, TU Berlin, 2021, DOI 10.14279/depositonce-15958 (acknowledgements read). P
95. J. Witzig, *Infeasibility analysis for MIP*, PhD thesis, TU Berlin, 2021, DOI 10.14279/depositonce-15389 (acknowledgements and contributions list read). P
96. M. Miltenberger, *Linear programming in MILP solving*, PhD thesis, TU Berlin, 2023, DOI 10.14279/depositonce-22309 (acknowledgements read). P
97. G. Mexi, *The two faces of mixed-integer programming: primal and dual progress*, PhD thesis, TU Berlin, defended 2026-09-10, DOI 10.14279/depositonce-26588 (contributions list read). P

**Primary: further papers named in the text**

98. G. Gamrath, A. Melchiori, T. Berthold, A. M. Gleixner, D. Salvagnin, *Branching on Multi-aggregated Variables*, CPAIOR 2015, LNCS, 141–156, DOI 10.1007/978-3-319-18008-3_10. P
99. A. M. Gleixner, D. E. Steffy, K. Wolter, *Iterative Refinement for Linear Programming*, INFORMS J. Comput. 28(3):449–464 (2016), DOI 10.1287/ijoc.2016.0692. P
100. T. Weber, S. Sager, A. Gleixner, *Solving quadratic programs to high precision using scaled iterative refinement*, Math. Program. Comput. 11:421–455 (2019), DOI 10.1007/s12532-019-00154-6. P
101. T. Breuer et al. (incl. A. Gleixner), *Optimizing Large-Scale Linear Energy System Problems with Block Diagonal Structure by Using Parallel Interior-Point Methods*, OR 2017 proceedings, Springer 2018, 641–647, DOI 10.1007/978-3-319-89920-6_85. P
102. A. Gleixner, N.-C. Kempke, T. Koch, D. Rehfeldt, S. Uslu, *First Experiments with Structure-Aware Presolving for a Parallel Interior-Point Method*, OR 2019 proceedings, Springer 2020, 105–111, DOI 10.1007/978-3-030-48439-2_13. P
103. D. Rehfeldt, H. Hobbie, D. Schönheit, T. Koch, D. Möst, A. Gleixner, *A massively parallel interior-point solver for LPs with generalized arrowhead structure, and applications to energy system models*, Eur. J. Oper. Res. 296:60–71 (2022), DOI 10.1016/j.ejor.2021.06.063. P
104. B. Müller, F. Serrano, A. Gleixner, *Using Two-Dimensional Projections for Stronger Separation and Propagation of Bilinear Terms*, SIAM J. Optim. 30:1339–1365 (2020), DOI 10.1137/19M1249825. P
105. F. Serrano, R. Schwarz, A. Gleixner, *On the relation between the extended supporting hyperplane algorithm and Kelley's cutting plane algorithm*, J. Glob. Optim. 78:161–179 (2020), DOI 10.1007/s10898-020-00906-y. P
106. K. Bestuzheva, A. Gleixner, H. Völker, *Strengthening SONC Relaxations with Constraints Derived from Variable Bounds*, HUGO 2022 proceedings, arXiv 2211.05518; extended preprint arXiv 2304.12145 (Bestuzheva, Völker, Gleixner). P
107. B. Sofranac, A. Gleixner, S. Pokutta, *An Algorithm-Independent Measure of Progress for Linear Constraint Propagation*, CP 2021, DOI 10.4230/LIPIcs.CP.2021.52 (DataCite); Constraints 27 (2022), DOI 10.1007/s10601-022-09338-9. P
108. G. Mexi, M. Besançon, S. Bolusani, A. Chmiela, A. Hoen, A. Gleixner, *Scylla: A Matrix-Free Fix-Propagate-and-Project Heuristic for Mixed-Integer Optimization*, OR 2023 proceedings, Springer 2025, 65–72, DOI 10.1007/978-3-031-58405-3_9 (arXiv 2307.03466). P
109. J. Witzig, I. Beckenbach, L. Eifler, K. Fackeldey, A. Gleixner, A. Grever, M. Weber, *Mixed-Integer Programming for Cycle Detection in Nonreversible Markov Processes*, Multiscale Model. Simul. 16:248–265 (2018), DOI 10.1137/16M1091162. P
110. M. Ghannam, A. Gleixner, *Hybrid Genetic Search for Dynamic Vehicle Routing with Time Windows*, OR 2023 proceedings, Springer 2025, 273–280, DOI 10.1007/978-3-031-58405-3_35 (arXiv 2307.11800). P

**Secondary**

31. arXiv API query `au:Gleixner_A` (27 results, all ANTARES astroparticle papers of another A. Gleixner; used only to document the name clash), 2026-11-08. S
34. Crossref record for DOI 10.1007/s12532-020-00194-3 (MIPLIB 2017 paper: received 2019-07-25, accepted 2020-09-10, online 2021-01-07; author order). S
42. Mathematics Genealogy Project, ids 206147 (Gleixner), 24939 (Grötschel), 117700 (Koch), 342910 (Eifler), https://www.mathgenealogy.org/id.php?id=… (read live 2026-11-08; the site notice says most dynamic pages are down). S
43. DBLP person 07/3479 via SPARQL (`scripts/dblp_works.py`, 74 records, 2009–2026), fetched 2026-11-08. S
46. Springer, MPC "Outstanding Paper of the Year" award page, https://www.springer.com/journal/12532/updates/17226372 (2018–2025 winners). S
47. Google Scholar profile DUFnBNcAAAAJ, https://scholar.google.com/citations?user=DUFnBNcAAAAJ (via WebFetch model summary; numbers not independently checked). S
48. Crossref REST API metadata, batch of 55 DOIs (titles, authors, dates, history), 2026-11-08. S
49. DataCite REST API for 10.4230/LIPIcs.CP.2023.27, 10.4230/DagRep.8.2.64, 10.4230/LIPIcs.CP.2021.52. S
111. Crossref author query "Ambros Gleixner" (200 rows; 156 items with a Gleixner author), scanned for correction, erratum and retraction notices, 2026-11-08. S
112. Internet Archive Wayback availability API for scipopt.org (2019–2026 timestamps); 429 and bot-block responses after two snapshots. S
113. WebSearch result lists (5 queries, 2026-11-08), used as leads only. One supplied the HTW research-catalogue and ZIB-news URLs; another supplied the MIP 2021, COST STSM, COW 2025, Argonne and Simons leads. S
114. MATH+ site search for "Gleixner", https://mathplus.de/?s=Gleixner, and the AA4-7 page it lists (he is cited there but is not a head). S
115. Research Campus MODAL news pages (Academy course, 24–28 Aug 2026; news list including Mexi's defence), https://forschungscampus-modal.de/ (context only; neither page names Gleixner). S

*Attempted, not read, not counted*: the ZIB OPUS search (Anubis wall); Argonne event 389 and Simons Institute node 17354 (Cloudflare challenge); a Dec 2018 Wayback snapshot of scip.zib.de (overwritten before reading).

*Counting*: entries [1]–[115] are all used; the numbers are not grouped by type. Primary: [1]–[30], [32], [33], [35]–[41], [44], [45], [50]–[110] (102 entries). Secondary: [31], [34], [42], [43], [46]–[49], [111]–[115] (13 entries).
