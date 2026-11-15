# Tobias Achterberg: research trajectory (research agent 06)

- **Researcher**: Tobias Achterberg. Dipl.-Math. and Dipl.-Inf. (both TU Berlin, per the thesis title page and the 2009 Tucker citation). Dr. rer. nat., TU Berlin; defence 12 July 2007; Berichter (referees) Martin Grötschel and Robert E. Bixby. Original author of SCIP (first commit 23 Oct 2002). ILOG CPLEX R&D from 2006, IBM after the acquisition, Gurobi from 4 March 2014 (self-asserted ORCID entry). At Gurobi he was Senior Developer, then Director of R&D, and from 22 April 2020 Vice President of R&D. Gurobi's webinar page for 18 Nov 2025 still lists him under that title. IDs: DBLP pid 71/6632 (23 records, 2005–2025); ORCID 0000-0002-0862-7065; OpenAlex A5016513861; Mathematics Genealogy Project (MGP) 117695. **Name collisions** seen in this run, none of them this person: Jascha Achterberg (neuroscience/ML), Jim Achterberg (synthetic health data), Massimo A. Achterberg (network science) and A. (Abraham) Achterberg (astrophysics), all on arXiv. The kickboxer Lukas Achterberg and other namesakes also turn up in web search.
- **Dimension**: research trajectory. Covered here: a dated timeline, lineage, the turns and what triggered each one, entry and exit relative to the consensus, the era and resources behind each practice, failures and abandoned lines, authorship and role labels by period, and the last 12 months. The note serves framework layer 2 (problem choice, timing) and layer 7 (organisation), with pointers for layers 1, 4 and 5.
- **Lens (team.json)**: MILP solver engineering. Branching (reliability, hybrid), conflict analysis, presolve, SCIP, CPLEX and Gurobi. Post-2014 work is closed Gurobi code, so Gurobi pages are used here only for dates and roles.
- **Research date**: 2026-11-08.
- **Sources consulted**: 68 distinct items listed under "Sources": 22 primary documents and records (P1–P22), 13 secondary items (S1–S13), and 33 of his own papers and reports (W1–W33). For every W item the identifier and dates were checked with a tool; most were read as metadata only. **WebSearch calls used: 5 of 5.** Everything else came through curl and WebFetch on known URLs and public APIs: DBLP SPARQL via `scripts/dblp_works.py`, ORCID, Crossref, OpenAlex, zbMATH Open, arXiv, and the GitHub REST and search APIs through the `gh` CLI.
- **Local corpus**: at the start of this run, `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep`. **Nothing below is from user-supplied material.** `private/` was not opened. I saved no transcript myself.
  - Late in this run a sibling agent (research agent 04) saved `sources/talks/subject-to-2023-interview.excerpt.transcript.txt`. It holds 14 excerpts of the YouTube auto-captions of the 2023 interview (P14), with passages redacted for privacy.
  - I read it after my first draft and cite it as **P21, caption text**: not speaker-checked, names garbled by the recogniser, quoted only by timestamp.
  - I checked the video identity, upload date and length myself (P14). I did not try to recover the redacted passages.
- **Sibling notes**: 01–05 for this member did not exist while most of this note was written (the `research/` folder held only `.gitkeep`). Notes 01, 02 and 04 appeared late in the run and were **not read**; the only sibling output used is the interview transcript excerpt (P21). Notes of other teams were used **only as leads**, and every fact taken from them was re-fetched here: lp-team (Bixby's 04-mentorship and RESOURCES) and nonlinear-team (Wächter's RESOURCES row 133). The one exception, the Gurobi 13.0 slide deck, is marked as not re-verified.
- **Living status**: team.json says living. The latest dated public trace found is the Gurobi 13.0 webinar listing of 18 Nov 2025 (§8).
- **Quotation policy**: findings are paraphrased with pinpoint pages or slides. The note has a few verbatim fragments, each under 15 words, copied from the source text or slide image named next to it.

### How the evidence was gathered (and what failed)

- **Read in full or in the relevant parts**:
  - P1, the thesis, from two copies:
    - The DepositOnce copy uses Type 3 fonts, so its title page and pp. ix–x were rendered to images and read.
    - The ZIB OPUS copy (docId 1112) extracts cleanly. Read: Introduction pp. 1–3, Ch. 12 p. 183, the Valse-XT passages, the bibliography.
  - P2: the 21 slides of "SCIP Origins" (2022), all read.
  - P18: Optima 80, pp. 1 and 10–12.
  - P12: ZR 16-44, paper pp. 1–2 (PDF pp. 3–4).
  - P13: arXiv 2211.13545v3 (title page, §5.7, §6, Funding).
  - S2: the Berthold 2011 deck, timeline slides.
  - P5, P6, P9: the Gurobi news releases of 2014, 2020 and 2025.
  - P7, P8: the speaker sections of Gurobi webinar pages.
  - P19, P20, P3, S1: the INFORMS award page, the SEA 2022 page, the SCIP-20 workshop page, and the MGP records.
  - P4: the ORCID record via the public API.
  - S3: the Substack post and its comments.
  - S8: Danna's MIP 2008 slide deck, title slide and PDF date only.
  - P21: all 14 excerpts of the sibling-saved interview transcript.
  - P22: the MIPLIB 2017 instance pages for aflow30a and aflow40b.
- **Code history (P10)**: commit metadata only; no source files were read.
  - The GitHub API lists **1,303 commits in `scipopt/scip` linked to the login `tobiasachterberg`**.
  - A commit search by author name "Achterberg" returns the same 1,303, so no commits sit under another login.
  - GitHub code search counts **467 files** carrying `@author Tobias Achterberg` (389 under `src/scip`), as of 2026-11-08.
- **Metadata only**:
  - The W items, through Crossref, DBLP, OpenAlex, zbMATH and Springer landing pages. Springer's `citation_author_institution` tags give the byline institution per paper.
  - OpenAlex abstracts were read for ZR 06-23, 08-29, 08-43 and 20-16. IDEAS gave the abstract of W25.
- **Not reached (not routed around)**:
  - **YouTube captions of the 2023 interview (P14)**: my own fetch of the caption track returned HTTP 404 without a proof-of-origin token, and I did not pursue it. The sibling agent's excerpt (P21) later covered 14 passages; the rest of the interview remains unread (Gaps G1).
  - **Gurobi CDN deck "What's New in Gurobi 13.0" (25 Nov 2025)**: HTTP 503 to curl and to WebFetch. A retry with browser-like headers was refused by the session's safety classifier and was not pursued. The nonlinear-team RESOURCES row 133 records the deck as "Nodet, Achterberg (Gurobi)". That entry was **not re-verified here**.
  - **ZIB OPUS**: curl hits an Anubis bot wall, and the OPUS search returns HTTP 500 to WebFetch. WebFetch did deliver the front doors of docIds 1112 and 699 and the PDFs of the thesis and of ZR 16-44.
  - **MOS prize page**: JavaScript-only, so not readable. The Beale–Orchard-Hays Prize was confirmed from Optima 80 instead.
  - **BusinessWire**: 403 or no response.
  - **Gurobi pages returning 404**: the 9.0 and 12.0 webinar pages, a "non-convex quadratic optimization" event page, and guessed URLs for the 2022 Bastert CTO release.
  - **Old Gurobi site**: www-old.gurobi.com returned 503.
- **Page conventions**:
  - Thesis: printed pages. In the OPUS copy PDF p. 9 = p. ix and PDF p. 10 = p. x. Ch. 12 starts on printed p. 183.
  - SCIP Origins: slide = PDF page.
  - Optima 80: printed = PDF.
  - ZR 16-44: paper p. N = PDF p. N+2.
  - Berthold 2011 deck: cited by the footer "N / 23" with the PDF page (slide 10 = PDF p. 11; slide 17 = PDF p. 19).
  - arXiv 2211.13545v3: printed pages.

### Tag legend

- **[stated]**: Achterberg's own words in his thesis front matter or introduction, his own slides, his self-asserted ORCID entry, or a quote attributed to him in a company release (marked "in a release").
- **[stated?]**: words attributed to him whose authorship could not be verified (a Substack comment).
- **[stated, caption]**: his words in the 2023 interview as rendered by YouTube auto-captions (P21, cited by timestamp). Always paraphrased here. Host and guest are not separated, and names are garbled, so read these as caption text.
- **[stated-joint]**: co-signed text whose "we" cannot be split among the authors.
- **[practice]**: what the record shows was done: papers and bylines, commits, releases, editorships.
- **[observed]**: what others recorded: prize citations, company bios and releases, colleagues' slides, databases, a listener's write-up.
- **[inferred]**: my synthesis, to be read as a hypothesis.
- **P / S**: primary / secondary source.

---

## 0. The trajectory in one paragraph (all [inferred], built from the sections below)

Achterberg came to MIP through code, not through theory. A textbook simplex for Grötschel's LP class and joining ZIB as a student (1999) led to a computer-science diploma project that needed a MIP solver. Alexander Martin's SIP supplied one. The project was machine learning to predict branching gains (2000–2001). Its lasting output was a negative-turned-positive finding: plain branching history predicts well. That produced history branching (ZR 02-32, Oct 2002) and then reliability branching (ORL 2005). Nineteen days after the history-branching report he started a new solver from scratch (first commit 23 Oct 2002). The idea came from his CS classes: logic programming, SAT and CP looked to him like MIP without the LP relaxation, and SIP's data structures could not hold their integration. He then built alone, without publishing, for almost two years. An industrial project that Grötschel arranged (the BMBF Valse-XT chip-verification project with Infineon and OneSpin, from Aug 2003) gave the framework a problem that needed both arithmetic and logic, plus clean data early. A chance contact from that project, the SAT researcher Yakov Novikov, brought in conflict analysis, watched literals and restarts. By 2007 those had become the thesis and the published papers. A 2005 workshop talk on conflict analysis led to an ILOG invitation, and Dash Optimization later counter-offered. By his account he chose CPLEX, the code he knew (caption text). He joined ILOG in 2006 before defending, and kept developing SCIP from his ZIB account until March 2009 (the MCF separator, presolve and heuristic tuning). At CPLEX, by his account, he first transplanted what he knew worked in SCIP: reliability branching, then conflict analysis. Prizes followed for the thesis (the 2008 Dantzig Dissertation Award, second place) and for the SCIP paper (Beale–Orchard-Hays 2009; INFORMS Optimization Society Young Researchers Prize 2011). At IBM he was, by Gurobi's account, lead MIP developer for CPLEX 12.0–12.6. His papers of that period are co-authored community work: MIPLIB 2010, ParaSCIP, CPAIOR 2011 as editor, and a published analysis of 12 years of CPLEX progress with Wunderling. In March 2014 he moved to Gurobi; by his account the pull was working with Gu again and with Rothberg for the first time. Its CTO and co-founder, Zonghao Gu, was a former ILOG CPLEX developer (his Gurobi bio, P8), and its president, Bixby, had refereed Achterberg's thesis. There he rose from Senior Developer to VP of R&D (2020). Since then his public research output is thin: a Gurobi presolve paper (2016/2020), MIPLIB 2017, ParaSCIP, an exact feedback-arc-set method with Baharev, Schichl and Neumaier, and RLT cuts with ZIB tested in both SCIP and Gurobi (2022–2025). Since 2014 his public voice is mainly release webinars. **In the last 12 months the only dated trace is a speaker listing for the Gurobi 13.0 webinar (18 Nov 2025).**

---

## 1. Dated timeline

| Date | Event | Tag | Source |
|---|---|---|---|
| 1999 | Joins ZIB while studying mathematics and computer science at TU Berlin. Before that he had implemented a textbook simplex in Grötschel's "Linear Optimization" class, with Utz-Uwe Haus; by his account the hardest part was the LP file-format parser | [stated] P | P2 slide 4 |
| 2000 | Mathematics diploma thesis under Grötschel, "Arboreszenz-Flüsse in Graphen: polyedrische Untersuchungen" (title from his slide; not checked in a library catalogue). In 2023 he describes it as facet work on an arborescence-flow problem from shortest-path routing, plus test instances he built. MIPLIB lists him as submitter of the "Arborescence flow" instances aflow30a and aflow40b | [stated] P; [stated, caption]; [practice] P | P2 slide 4; P21 0:22:00–0:23:00; P22 |
| 2000–2001 | Computer-science diploma thesis in AI under Klaus Obermayer: neural networks to speed up branch-and-bound. He says the thesis work "began already in 2000" (P1 p. ix); the slide dates the CS thesis 2001. Experiments ran inside Alexander Martin's SIP, to which Thorsten Koch introduced him | [stated] P | P1 p. ix; P2 slides 4–7 |
| 4 Oct 2002 | ZIB-Report 02-32 "Branching on History Information" (with Koch and Martin): history branching, a pseudocost variant implemented in SIP (abstract as summarised by WebFetch) | [practice] P | P11; W1 |
| 23 Oct 2002 | First SCIP commit, a CVS import: "initial directory structure and configuration files" | [practice] P | P10; P2 slides 2–3 |
| end 2002 – ~mid 2004 | Builds SCIP alone from scratch. He writes that he published no paper for almost two years | [stated] P | P1 p. ix |
| 2003 | Seventh of eight authors on a UMTS network-configuration chapter in *Telecommunications Network Design and Management* | [practice] P | W2 |
| from Aug 2003 (two years) | BMBF project Valse-XT, work package 1: property checking for chip verification with Infineon, OneSpin Solutions and TU Kaiserslautern. Grötschel's contact to Infineon brought it in | [stated] P; date [observed] S | P1 pp. ix, 183; P2 slide 12; S2 slide 17 |
| during Valse-XT (undated) | Meets Yakov Novikov. A few days later he has the two-watched-literals scheme in the set-covering handler; three weeks later he has conflict analysis generalised to MIP. Root restarts are kept; tree restarts did not help in SCIP | [stated] P | P1 p. x; P2 slide 14 |
| Jan 2004; Mar 2004; Jan 2005 | First commits by Marc Pfetsch, Kati Wolter and Timo Berthold: SCIP stops being a one-person code | [stated] P (his own list) | P2 slide 15 |
| 28 May 2004 | ZIB-Report 04-19, "SCIP – a framework to integrate Constraint and Mixed Integer Programming" | [practice] P | W3 |
| Jun 2004 (DOI registered); Jan 2005 print | "Branching rules revisited" (*Oper. Res. Lett.*), with reliability branching | [practice] P | W4; P16 |
| 2005 (month not stated) | Gives a conflict-analysis talk at the MIP 2005 workshop (IMA, Minneapolis). He thinks Grötschel got him a late slot. The talk compared SCIP (with CPLEX as LP solver) with CPLEX 9.0. People in the audience asked about his plans and invited him to ILOG. The event itself was not independently checked | [stated, caption] | P21 0:35:30–0:37:00 |
| Sep 2005 | SCIP 0.80, the first public version | [observed] S | S2 slide 17 |
| Sep 2005 (DOI registered); Jul 2006 print | MIPLIB 2003 (*Oper. Res. Lett.*), as first author | [practice] P | W5; P16 |
| May 2006 | ZIB-Report 06-23 on a teaching tool, an algebraic modelling language plus a MIP solver, free for academics; plus "Teaching MIP modeling and solving", *ORMS Today* 33(6) 2006 | [practice] P | W6 |
| 2006 | ILOG company off-site meeting, then an offer. Dash Optimization (Xpress) counter-offers. He decides on grounds other than money: he had used CPLEX since his studies and liked it. He joins ILOG in Sept/Oct 2006, before finishing the PhD | [stated, caption] | P21 0:37:00–0:38:30 |
| 2006 | Starts in industry: ILOG CPLEX R&D | [observed] P (company) | P5; P6; P7 |
| 2006–2014 (sequence undated) | CPLEX work, in his account. First project: reliability branching (Gu had held it back for him). Next: conflict analysis, then cutting planes and MIR, then presolve, and in time all MIP parts except the LP solver. He carried over what he knew already worked in SCIP, and had one success after another | [stated, caption] | P21 0:40:00–0:42:30 |
| Dec 2006 (DOIs registered); Mar 2007 print | "Conflict analysis in mixed integer programming" (sole author) and "Improving the feasibility pump" (with Berthold), *Discrete Optim.* 4(1) | [practice] P | W7; W8; P16 |
| May 2007 | Signs the thesis acknowledgments in Berlin and calls ILOG "my new employer ILOG". Reports more than 250,000 lines of C for SCIP plus the chip-verification solver. He missed his self-imposed deadline because he kept improving SCIP, and Koch persuaded him that writing came first | [stated] P | P1 pp. ix–x |
| 12 Jul 2007 | Thesis defence, TU Berlin, Fakultät II. Berichter: Grötschel (TU Berlin) and Bixby (Rice) | [observed] P | P1 title page |
| Sep 2007 | SCIP 1.00, released in the ZIB Optimization Suite | [observed] S | S2 slide 17 |
| Nov 2007 | ZIB-Report 07-37, "Property Checking with Constraint Integer Programming" (with Brinkmann and Wedler) | [practice] P | W9 |
| May 2008 | Two CPAIOR 2008 papers (CIP as a new CP–MIP integration; counting solutions). Byline: ILOG Deutschland | [practice] P | W10; W11; P17 |
| Jun – Nov 2008 | Keeps committing to SCIP from his ZIB address: the MCF cut separator (adds Christian Raack as its author on 9 Jul 2008), linear-constraint presolve, feasibility-pump timing. On 3 Sep 2008 he reverts two default changes that "did not seem to be good overall" | [practice] P | P10 |
| 5 Aug 2008 (OpenAlex date) | ZIB-Report 08-29 "On the Effects of Minor Changes in Model Formulations" (with Koch and Tuchscherer). Small variants of one TSP formulation change solver performance by more than a factor of 1000 (abstract only) | [practice] P; abstract S | W12; S4 |
| 2008 | INFORMS George B. Dantzig Dissertation Award, second place, for *Constraint Integer Programming* | [observed] P | P19 |
| 2008 | Book edition of the thesis, Dr. Hut Verlag, ISBN 978-3-89963-892-9 | [observed] | P1 (OPUS record); P15 |
| Dec 2008 | Dynamic load balancing for ParaLEX (ICPADS), with Yuji Shinano and Tetsuya Fujie | [practice] P | W14 |
| 20 Jan 2009 | "SCIP: solving constraint integer programs" online as the first paper of *Math. Program. Comput.* Received 6 Oct 2008, accepted 8 Dec 2008. Byline: ZIB | [practice] P | W15; P17 |
| 18 Mar 2009 | Last SCIP commit from the ZIB address (MCF separator) | [practice] P | P10 |
| May 2009 | "Hybrid Branching" (CPAIOR 2009, with Berthold). Byline: "ILOG, an IBM company" | [practice] P | W16; P17 |
| 2009 | *AIChE Journal* paper on an extractive distillation column with affine arithmetic, with Ali Baharev and Endre Rév | [practice] P | W17 |
| 23 Aug 2009 | Beale–Orchard-Hays Prize at the ISMP 2009 opening ceremony in Chicago, for the MPC SCIP paper. Also a Tucker Prize finalist, with the note that he was then with IBM-CPLEX as a software developer | [observed] P | P18 pp. 1, 10, 11–12 |
| Nov 2009 – Jul 2010 | "The Mcf-separator" (*Math. Program. Comput.*, with Raack): received 30 Nov 2009, online 3 Jul 2010. Byline: IBM, Böblingen | [practice] P | W18; P17 |
| Oct 2010 online (2011 book) | "Hybrid Solving Techniques" (with Andrea Lodi) in *Hybrid Optimization: The Ten Years of CPAIOR*. Byline: "CPLEX Optimization" | [practice] P | W19; P17 |
| May 2011 | Co-editor, with J. Christopher Beck, of the CPAIOR 2011 proceedings (Berlin), LNCS 6697 | [practice] P | W21 |
| Jun 2011 | MIPLIB 2010, second author of 16. Byline: IBM Deutschland, Böblingen | [practice] P | W20; P17 |
| 2011 | INFORMS Optimization Society Young Researchers Prize for the MPC SCIP paper. Committee: Bienstock, Boros, McCormick, Renegar (chair) | [observed] P | P19 |
| Aug 2011 | A ZIB deck lists "Tobias Achterberg (IBM)" in the SCIP team, and "Start of SCIP development (T. Achterberg [now IBM])" for 10/2002 | [observed] S | S2 slides 10, 13 |
| 2011–2012 | ParaSCIP (CHPC 2010 proceedings) and rounding and propagation heuristics (OR 2011 proceedings, with Berthold and Hendel). Byline: IBM Deutschland | [practice] P | W22; W23; P17 |
| 2013 | CPAIOR 2013, implied literals from conflicts and knapsack covers, with IBM Watson's Ashish Sabharwal and Horst Samulowitz (byline IBM). "Mixed Integer Programming: Analyzing 12 Years of Progress" with Roland Wunderling, in the Grötschel Festschrift: CPLEX 8.0 → 12.5, an "unbiased" benchmark analysis, the deterministic parallel optimizer (abstract only) | [practice] P; abstract S | W24; W25; S7 |
| 4 Mar 2014 | Employment at Gurobi Optimization GmbH begins (self-asserted ORCID entry, created 6 Feb 2020; no end date) | [stated] P | P4 |
| 2014 (page undated) | Gurobi announces he has joined its development team. It credits him with CPLEX R&D since 2006 and as lead MIP developer for CPLEX 12.0 through 12.6. Bixby is quoted as President | [observed] P; quote [stated, in a release] | P5 |
| 2014 (his account) | Bixby had invited him to Gurobi a few years earlier, and he had declined to stay with CPLEX and its team. In 2014 he called Bixby back. His reasons: personal reasons (in the video, redacted in P21), the chance to work again with Gu, and to work for the first time with Rothberg | [stated, caption] | P21 0:42:30–0:45:30 |
| 2014 or soon after (his account) | Among his first contributions at Gurobi: moving development from Subversion to git, later with a GitHub-based issue system | [stated, caption] | P21 0:48:00–0:48:30 |
| May 2014 | ParaSCIP update on hard MIPLIB 2003 instances (IPDPS workshops), co-author | [practice] P | W26 |
| 2 Nov 2014 | One SCIP commit from a Gurobi address: "Fixed lpi_none.c." | [practice] P | P10 |
| May 2016 | ParaSCIP on up to 80,000 cores (IPDPS 2016), co-author | [practice] P | W27 |
| Sep 2016 (cover), 9 Dec 2016 (title page) | ZIB-Report 16-44 "Presolve Reductions in Mixed Integer Programming" (Achterberg, Bixby, Gu, Rothberg, Weninger). Byline: Gurobi Optimization. It aims at a complete overview of every presolve step in Gurobi 6.5; supported by Research Campus MODAL | [stated-joint] P | P12 pp. 1–2 |
| 29 Nov – 16 Dec 2016 | 23 SCIP commits on the Gurobi LP interface (issue #1093): ranged rows, dual norms, basis handling. The last is on 16 Dec 2016: presolve is turned off for dual LP solves with an iteration limit. Credits "Micha and Tobi" as authors of the Gurobi LPI | [practice] P | P10 |
| 8 Nov 2019 (DOI registered); Apr 2020 issue | Presolve paper in *INFORMS J. Comput.* 32(2). Byline: Gurobi GmbH, Berlin | [practice] P | W28; P16 |
| by Apr 2020 | "managed the recent release of Gurobi 9.0", whose bilinear solver enables non-convex quadratic optimization. In his own 2023 account he did most of the work handling the non-convex constraints in the tree search and the LP relaxation, while a colleague wrote the nonlinear interior-point part. He calls the clean data-structure design of that work rewarding | [observed] P (company); [stated, caption] | P6; P21 0:47:00–0:48:00 |
| 22 Apr 2020 | Promoted to VP of R&D, to lead the R&D department and join senior management; previously Senior Developer and Director of R&D. Announced by Zonghao Gu (CTO, co-founder) | [observed] P; quote [stated, in a release] | P6 |
| May 2020 | ZIB-Report 20-16: ParaSCIP solves 21 previously unsolved MIPLIB instances on up to 80,000 cores (Titan), co-author | [practice] P | W29; S4 |
| Jan 2021 | MIPLIB 2017 (*Math. Program. Comput.*), 4th of 16 authors. Byline: Gurobi GmbH, Frankfurt am Main | [practice] P | W31; P17 |
| Apr 2021 | "An Exact Method for the Minimum Feedback Arc Set Problem" (*ACM J. Exp. Algorithmics*), last author, with Baharev, Schichl and Neumaier. Byline: Gurobi GmbH, Frankfurt | [practice] P | W30; P15 |
| 25–27 Jul 2022 | Invited speaker at SEA 2022 (Heidelberg); listed as VP of R&D at Gurobi | [observed] P | P20 |
| 4 Nov 2022 | "SCIP Origins" talk at the "Let's SCIP it!" workshop, ZIB, for SCIP's 20th birthday | [stated] P | P2; P3 |
| 24 Nov 2022 | arXiv 2211.13545 v1 on RLT cuts (Bestuzheva, Gleixner, Achterberg). Tested by independent implementations in SCIP and in Gurobi 10.0 beta, on Gurobi's internal test set | [practice] P | P13 |
| 9 Jun 2023 | Mark Turner's preprint on GMI-violation-based branching (arXiv 2306.06050). Authors: Turner, Berthold, Besançon, Koch; **not** Achterberg. In the interview he says he implemented Turner's idea in Gurobi, where it helped a little and was planned for the next version | [practice] S; [stated, caption] | S13; P21 0:55:00–0:56:00 |
| Jun 2023 | IPCO 2023 version (Madison) | [practice] P | W32 |
| 17 Aug 2023 | "Subject to: Tobias Achterberg", 5,062 s (YouTube channel Subject to); recording date not stated. Fourteen excerpts read as captions (P21). Positions as of the interview:<br>(a) VP of R&D, but his main contribution is still MIP performance: branching, cuts, presolve, tree, parallelism;<br>(b) Gurobi benchmarks on 192 machines running around the clock, with about 6,000 test instances and five seeds;<br>(c) he estimates about 10 % research and 90 % software engineering and benchmarking;<br>(d) ML is used to find explainable rules (decision trees) that are then hand-coded into defaults, e.g. whether to dualize an LP and which simplex to use;<br>(e) neural-network structure detection for OBBT, with Pierre Bonami;<br>(f) he is weak at knowing the literature and relies on collaborators | [stated] P (video metadata); [stated, caption] | P14; P21 0:46:30–1:22:00 |
| 5 Oct 2023 | A listener (Michael Watson, a former ILOG/IBM colleague by his own account) summarises the interview | [observed] S | S3 |
| 16 Jul 2024 online; Mar 2025 print | Extended RLT paper, *Math. Program.* 210, 47–74. Byline: Gurobi GmbH, Monheim am Rhein | [practice] P | W32 |
| 15 Jun 2025 | Substack comment signed "Tobias": Gurobi has "about 8500 models in our MIP test set" | [stated?] S | S3 |
| 18 Nov 2025 | Listed as speaker, "Vice President of Research and Development", for the Gurobi 13.0 webinar | [observed] P | P7 |
| Nov 2025 | The Gurobi 13.0 release text quotes CTO Oliver Bastert and CEO Duke Perrucci. Achterberg is not named | [observed] P | P9 |
| 2026 (to 8 Nov) | No paper, preprint, SCIP commit, ORCID change, DBLP or zbMATH record, or talk found | — | P4; P10; P15; S4–S6 |

---

## 2. Lineage

- **Doctoral lineage** [observed, S1]: Bernhard Korte → Martin Grötschel (Bonn 1977; MGP 24939, 51 students listed) → Tobias Achterberg (TU Berlin 2007; MGP 117695). MGP lists **no students** for Achterberg.
- **Referees and advisor labels**:
  - The title page names Grötschel and Bixby as Berichter (P1 title page).
  - ZIB OPUS lists both in its "Advisor" field (P1 OPUS record).
  - The acknowledgments call Grötschel "my advisor" and thank him for patience and the freedom to do whatever he liked (P1 p. ix).
  - Bixby does not appear in the acknowledgments. Kept as a labelling discrepancy (Contradictions C3).
- **CS diploma**: the AI group of Klaus Obermayer (P2 slide 4) [stated].
- **Code lineage (the closest thing to an apprenticeship)** [stated, P2 slide 5]:
  - Alexander Martin's SIP (1998) used CPLEX as its LP solver.
  - Bob Bixby helped SIP use CPLEX well, including a hidden "FastMIP" setting and strong branching.
  - SIP was comparable to CPLEX 6.0.
  - Martin moved to TU Darmstadt in 2000. Thorsten Koch introduced Achterberg to SIP, and Martin allowed him to use it.
  - [inferred] He learned MIP by reading a strong code that already embodied Bixby-era CPLEX practice, then rewrote it.
- **Students**:
  - [stated, P1 p. x] He calls Kati Wolter and Timo Berthold "my great students".
  - [practice, P1 bibliography] Their 2006 TU Berlin diploma theses (cutting-plane separators in SCIP; primal heuristics) are cited for SCIP chapters 8 and 9.
  - His formal supervisory role is **not verified**.
- **The SCIP successor community** [stated, P2 slides 15–20]: his slides list 107 committer identities by first-commit date. 17 of them, himself and 16 others, made their first commit before his last ZIB commit (18 Mar 2009). The last of these is Ambros Gleixner (26 Sep 2008). SCIP continued without him after 2009. His own record there is 1,303 commits (P10).
- **Industrial line**:
  - CPLEX R&D colleagues appear as co-authors: Roland Wunderling (W25).
  - Emilie Danna, at ILOG CPLEX R&D in 2008 (S8), is context only.
  - At Gurobi he joined Bixby, President in 2014 (P5), and Zonghao Gu, CTO and co-founder in 2020 (P6). Gu's Gurobi bio says he joined ILOG CPLEX R&D in 1998 and was lead developer for CPLEX 11 (P8, 9.1 page). The CPLEX backgrounds of Bixby and Rothberg were not re-checked here (see lp-team notes, S11). Gu, Bixby and Rothberg are co-authors of the presolve paper (P12).
  - [inferred] Bixby links both ends of this lineage: thesis referee in 2007, and the president who announced his hiring in 2014.
- **Long-running external collaborations**:
  - Yuji Shinano, on parallel B&B: 2008 → 2020 (W14, W22, W26, W27, W29).
  - Ali Baharev, on chemical-process and feedback-arc-set computation: 2009 → 2021 (W17, W30).
  - ZIB's Gleixner and Bestuzheva, on RLT: 2022 → 2025 (W32).

---

## 3. Turns and what triggered them

### T1. Student → MIP solver work (1999 → 2001)
- **What happened**:
  - [stated] Implementing a simplex for a class, a ZIB job (1999), and two diploma theses, one in each of his two subjects (P2 slide 4).
  - [stated] He looked for a topic that combined mathematics and computer science (P1 p. ix).
- **Trigger**: a tool, plus access. He "Needed MIP code!" (P2 slide 4), and SIP was available through Koch and Martin (P2 slide 5).

### T2. Machine-learned branching → history and reliability branching (2000 → 2005)
- **What happened**:
  - [stated] He needed a reason to do optimization in his CS thesis, so he proposed AI methods to learn a branching rule in SIP: predict the down and up objective gains from candidate features (P2 slide 6).
  - The models tried were PCA, MLP, autoencoder, RBF with k-means, SVM and mixtures of experts.
  - Slide 7 states the result as "History values are good predictors", with an arrow to "Reliability Branching".
  - [practice] ZR 02-32 (4 Oct 2002, history branching in SIP; W1) → "Branching rules revisited" (ORL, DOI registered Jun 2004; W4) → thesis ch. 5 (P1 pp. 2–3).
- **Trigger**: a **result of the ML experiment**. It showed that the learned models were not needed, because the history features themselves carried the signal. The ML line was dropped.
- **His 2023 telling** [stated, caption, P21 0:24:00–0:26:00] adds detail:
  - He hoped ML would find a good combination of features. The models did select a rule, but the result disappointed him: one feature mattered and the rest did not.
  - That feature was his own "history value", pseudocosts plus a little more.
  - The outcome of the thesis was to drop the ML and keep the feature, which became reliability branching.
- **Exit and return**: ML for branching left as a research topic with the CS thesis. [inferred] No ML paper of his follows.
  - [stated, caption] In 2023 he describes ML at Gurobi in the 2001 shape: use explainable ML, e.g. decision trees, to *find* a rule, then implement the rule by hand in the defaults. The example given is whether to dualize an LP and which simplex to use (P21 1:16:00–1:17:30).
  - A listener reports the same (S3) [observed, S].
  - [inferred] The 2001 move (learn, read off the feature, hand-code the rule) is still his way of using ML 22 years later.

### T3. SIP → a new solver, SCIP (late 2002)
- **What happened**:
  - [stated] The CS classes taught logic programming, SAT and CP. His slide calls them "Pretty much the same as MIP, just without LP relaxation!" Combining them was impossible in SIP's data structures, so he wrote a new solver from scratch and named it after SIP (P2 slide 8; P1 p. ix).
  - He chose C because in 2002 "C++ was a mess" (P2 slide 11).
  - [practice] First commit 23 Oct 2002, 19 days after ZR 02-32 (P10; P11).
  - [stated, caption] In 2023 he adds three points (P21 0:26:30–0:29:00; 1:21:30–1:22:00):
    - John Hooker had the same CP–MIP idea at the time, but he did not know Hooker's work. He learned of it only later, at a conference, and calls the missed collaboration a pity.
    - Grötschel gave him complete freedom, with no other task, for several years.
    - He dates his first commit to 2001 (Contradictions C13).
- **Trigger**: an **idea that the tool could not hold**. The old code's architecture blocked the integration, so he rebuilt.

### T4. Framework → application pull (from Aug 2003, two years)
- **What happened**: [stated] He calls it "Extraordinary luck" (P2 slide 12) and "the miracle" (P1 p. ix).
  - Grötschel's contact to Infineon in Munich brought chip-verification problems with arithmetic circuits: MIP and LP handle the arithmetic, CP and SAT the logic.
  - Unlike most applied projects, the partner had many clean data sets and delivered them early (P2 slide 12; P1 p. ix).
  - [practice] BMBF project Valse-XT, work package 1, partners Infineon, OneSpin and TU Kaiserslautern (P1 p. 183). ZR 07-37 (W9). Thesis part III.
- **Trigger**: a **project and data, through the advisor's network**, arriving when the framework existed.

### T5. Into SAT techniques (during Valse-XT)
- **What happened**: [stated] Grötschel asked him to pick up the SAT researcher Yakov Novikov. On the way to ZIB, Novikov explained watched literals, conflict analysis and restarts (P1 p. x; P2 slides 13–14).
  - He implemented all three soon after. Watched literals went into the set-covering handler within days, and conflict analysis was generalised to MIP for infeasible LP relaxations within three weeks.
  - Restarts were kept only at the root: tree restarts did not help in SCIP.
- **Trigger**: a **person met by chance through the project**.
- **Continuation**: [practice] the conflict line runs from the 2007 sole-author paper (W7) to the 2013 implied-literals paper with IBM Watson SAT/CP researchers (W24).

### T6. Academia → industry: ILOG CPLEX (2006), with an overlap to 2009
- **What happened**:
  - [observed] Gurobi bios: industry from 2006, CPLEX developer for versions 11–12.6 (P5–P7).
  - [stated] In May 2007 ILOG is "my new employer" (P1 p. ix). Two ILOG developers, Zonghao Gu and Lloyd Clarke, proof-read the thesis (P1 p. x).
  - [practice] SCIP commits from his ZIB address continue to 18 Mar 2009, with 189 commits in 2007 and 75 in 2008 (P10). CPAIOR 2008 bylines read ILOG Deutschland; the 2009 MPC byline still reads ZIB (P17).
- **Trigger** [stated, caption, P21 0:35:30–0:38:30]: **a conference talk that worked as an audition**.
  - At the MIP 2005 workshop he showed conflict analysis and a head-to-head of SCIP (with CPLEX as LP solver) against CPLEX 9.0. Afterwards people from ILOG asked about his plans and invited him.
  - About a year later the offer came. Dash Optimization (Xpress) counter-offered.
  - He says he stopped the bidding and decided on other grounds: he had used CPLEX since his studies and liked it.
  - He joined in Sept/Oct 2006 with the PhD unfinished.
- **His first years at CPLEX** [stated, caption, P21 0:40:00–0:42:30]:
  - First project: reliability branching. Next: conflict analysis. He transplanted what he already knew worked in SCIP, and success followed success.
  - When the transplants ran out, gains got harder: cuts and MIR, then presolve, which he calls the most rewarding part because reductions usually pay off, unlike cuts that look strong yet slow the solver.
  - [inferred] **The move turned a research code into a stock of tested ideas for a commercial solver.**

### T7. Exit from SCIP development (2009)
- **What happened**:
  - [practice] After March 2009 there are no ZIB-address commits (P10). He stays a co-author of ZIB community work: MIPLIB 2010, ParaSCIP, heuristics 2012, MIPLIB 2017.
  - [observed] 2009: "currently with IBM-CPLEX as a software developer" (P18 p. 12). 2014: lead MIP developer for CPLEX 12.0–12.6 (P5).
- **Trigger**: not stated. [inferred] The CPLEX MIP lead role absorbed the time he had given to SCIP.

### T8. IBM → Gurobi (March 2014)
- **What happened**:
  - [stated, in a release] He had been "impressed with both the strength of their team and the performance of their solver" (P5).
  - [stated] ORCID gives the start as 4 Mar 2014 (P4).
- **Trigger**: per the release, **the team and the product**. [stated, caption, P21 0:42:30–0:45:30] In 2023 he adds three points:
  - Bixby had invited him a few years earlier, and he declined out of loyalty to CPLEX and its team.
  - The 2014 decision followed personal reasons, which are redacted in P21 and not pursued here.
  - A main pull was working again with Gu and, for the first time, with Rothberg. He had known Rothberg as a source of ideas at CPLEX off-site meetings.

  He also reports that Bixby no longer coded at Gurobi and handled sales and organisation.

### T9. Developer → R&D manager (by April 2020)
- **What happened**: [observed] Senior Developer → Director of R&D → VP of R&D on 22 Apr 2020 (P6). He managed the 9.0 release (P6).
  - [practice] His public research becomes collaborative and sparse after the promotion: the presolve paper (written 2016), MIPLIB 2017, the feedback-arc-set paper, RLT.
- **Trigger**: company growth, in the release's words. [inferred] This is a seniority-driven change of role.
- [stated, caption, P21 0:46:30–0:47:00] In 2023 he says the title means leading the development team. His own main contribution is still MIP performance work across branching, cuts, presolve, the tree framework and parallelism. **Manager by title, MIP developer by his own account.**

### T10. MIP → non-convex MIQCP and MINLP inside the product (2019 → 2025)
- **What happened**:
  - [observed] Gurobi 9.0 added a bilinear solver for non-convex quadratic problems; he managed that release (P6).
  - [practice] RLT cuts for implicit and explicit bilinear products were tested in Gurobi 10.0 beta: larger impact in Gurobi than in SCIP, and no MILP slowdown (P13 §5.7, pp. 21–22).
  - [observed] The Gurobi 13.0 release reports large MINLP and non-convex MIQCP speed-ups, from company benchmarks. Achterberg is not named (P9).
- **Trigger**: product scope. [inferred] Which 13.0 components are his own work is unknown.

---

## 4. Entry and exit timing relative to the consensus ([inferred] unless tagged)

| Line | Entry | Exit or status | Relative to the consensus | Basis |
|---|---|---|---|---|
| ML for branching | 2000–2001 (CS thesis) | By 2002, replaced by history-based rules. Kept as a tool: in 2023, explainable ML for deriving default rules at Gurobi (P21) | **About 15 years before** the published ML-for-branching wave, e.g. Khalil et al., AAAI 2016 (S9), and Alvarez, Louveaux and Wehenkel, IJOC 2017 (S10). In 2023 he remarks that what he did in 2001 has since become popular (caption text, P21 0:24:00). **He left the research topic before that wave formed, and kept ML only as a rule-finding tool** | P2 slides 6–7; W1; S9; S10; P21 |
| History, reliability and hybrid branching | 2002 | 2009 (hybrid branching) | Built on pseudocosts and strong branching, which SIP already had (P2 slide 5). Its later uptake by others was not assessed here; minlp-team cards cite his branching work, but those are unchecked leads | W1; W4; W16 |
| CP–SAT–MIP integration in one search tree | 2002 (idea) | Last CPAIOR paper 2013; CPAIOR 2011 editor | **Contemporaneous** with the CP–OR integration community. His thesis cites Coupe, Scil and Simpl as earlier frameworks (P1 pp. 1–2). His distinguishing claim is the **level of integration**: everything on one tree (P1 p. 2) | P1 pp. 1–2; W10; W19; W21; W24 |
| Conflict analysis in MIP | ~2004 (Valse-XT) | Continued to 2013 (W24) | **Early**: the thesis calls it a novel concept in MIP solving (P1 p. 1) [stated]. Uptake in commercial codes was not checked | P1 pp. 1, x; W7; W24 |
| Performance variability ("minor changes") | ZR 08-29, 5 Aug 2008 (OpenAlex date) | Not a continuing line of his | **Same week** as Danna's MIP 2008 talk "Performance variability in mixed integer programming" (ILOG CPLEX R&D; PDF dated 7 Aug 2008), so at the onset of the topic, not after it | W12; S8 |
| MIPLIB benchmark libraries | MIPLIB 2003, first author | MIPLIB 2017, 4th author | Author on three successive editions, across three employers (ZIB → IBM → Gurobi). The lp-team notes report that MIPLIB 3.0's promised yearly updates lapsed before 2003 (S11; not re-checked here) | W5; W20; W31 |
| Parallel tree search | ParaLEX 2008 | ParaSCIP to 2020, co-author | The CPLEX "deterministic parallel optimizer" is highlighted in W25 (abstract) | W14; W22; W26; W27; W29; S7 |
| Presolve | Thesis ch. 10 (SCIP presolving) | Gurobi presolve paper 2016/2020 | The paper says presolve publications are surprisingly few given the subject's importance (P12 p. 1) [stated-joint]. It documents a commercial code: **late in time, early in openness** | P1 p. 1; P12 pp. 1–2; W28 |
| Non-convex bilinear / RLT | Gurobi 9.0 (2019, managed) | RLT 2022–2025 | Commercial entry after academic global solvers already existed (SCIP itself had MINLP by then; not re-checked here) | P6; P13 |

---

## 5. Era and resource context of each practice

| Period | Setting | Compute, tools, data | Team, seniority | Practices affected |
|---|---|---|---|---|
| 1999–2002 | ZIB student, two diploma theses | SIP in C, with CPLEX as LP solver; an ML toolkit (PCA, MLP, SVM…) for the CS thesis (P2 slides 5–6) | Student, mentored in code by Koch | Learning MIP by instrumenting someone else's state-of-the-art code; feature collection from branching decisions |
| 2002–2006 | ZIB PhD | New C code (C over C++, P2 slide 11) under CVS (git came only in 2011, P2 slide 3). Benchmarks on colleagues' identical machines using spare cycles (P1 p. x). Industrial data from Infineon and OneSpin (P1 p. ix). More than one CPU-year for the thesis benchmarks: 244 instances × 115 settings = 28,060 runs, measured as geometric mean relative to SCIP defaults (P1 p. 2 and footnote) | Single developer until 2004, then with students and colleagues (P2 slide 15). An advisor who allowed two years without papers (P1 p. ix) | *build first, publish later* (my label); ablation of each component against the default; open, free academic code (P18 p. 10) |
| 2006–2014 | ILOG → IBM CPLEX R&D (Germany) | Commercial code and test sets; nothing documented by him except the CPLEX 8.0 → 12.5 analysis (W25 abstract) | Developer, then lead MIP developer for 12.0–12.6 (P5) | Kept SCIP research going to 2009 from a ZIB account (P10); thereafter co-authorship with ZIB and IBM Research |
| 2014–present | Gurobi GmbH (Germany) | The 2016 presolve study ran on one 4-core i7-3770K with 32 GB, Gurobi 6.5 defaults, a 3600 s limit (P12 p. 2). The 2022 RLT study used Gurobi's internal test set of customer and public models with a 10,000 s limit (P13 p. 21). In the 2023 interview he describes 192 benchmark machines running around the clock, and a test set of about 6,000 instances run with five seeds, about 12 hours when the cluster is free (P21 0:52:00, 1:05:30; caption). A listener reports the same machines and prints the set size as "6,00" (S3). A 2025 comment attributed to him gives about 8,500 (S3) | Senior Developer → Director → VP of R&D (P6) | Code closed; public output is documentation of components (presolve), community benchmarks, and joint work with ZIB |

[inferred] Each solver-design practice in his record carries the resources of its period. A single developer with a free code and colleagues' idle CPUs (2002–2006) works differently from a commercial team with one or two hundred test machines and thousands of customer models (2014–). A skill built on him should say which era a practice belongs to.

---

## 6. Failures, abandoned directions, revised assessments (dated)

1. **ML-learned branching was dropped (2001–2002).**
   - [stated] The ML models were not the outcome. The finding was that history values predict well, which became reliability branching (P2 slide 7).
   - [inferred] This failure set the direction of his branching work.
2. **Tree restarts did not help in SCIP**, so only root restarts were kept (P2 slide 14) [stated].
3. **Almost two years without a paper (end 2002 – 2004)** while he built infrastructure (P1 p. ix) [stated]. He presents it as a cost his advisor tolerated.
4. **Missed self-imposed thesis deadline.** He kept improving SCIP instead of writing; Koch convinced him that writing mattered more than another 10 % of speed (P1 p. x) [stated, paraphrased].
5. **A common default rejected.** Most-infeasible branching was shown to be "almost as poor as selecting the branching variable randomly" (P1 p. 3) [stated].
6. **Reverted tuning.** The 3 Sep 2008 commit undid default changes for `minorthoroot` and `cmir/maxroundsroot` because they "did not seem to be good overall" (P10) [practice]. [inferred] Negative tuning results stayed in the code log; none of them was published.
7. **Self-criticism of the name.** He calls the name SCIP "a sub-optimal choice" (P2 slide 8) [stated].
8. **Uneven reception** (Crossref counts on 2026-11-08) [observed]: MPC SCIP paper 907; "Branching rules revisited" 382; CPAIOR 2013 implied literals 2; CPAIOR 2008 counting paper 9.
9. **A slow path to the journal.** The presolve report is dated Sep/Dec 2016 (P12); the journal version's DOI was registered on 8 Nov 2019 (W28; P16). The review history is **unknown**.
10. **SCIP left behind (2009).**
    - The 2014 and 2016 commits are maintenance of SCIP's Gurobi LP interface only (P10).
    - His `@author` lines remain in 467 files (P10).
    - [inferred] The founder moved away from the code base he created, and the community kept it going.

11. **Things he names in 2023 as setbacks or limits** [stated, caption, P21]. All paraphrased.
    - The ML result disappointed him (0:25:00).
    - He did not know Hooker's CP–MIP work when he started SCIP, and missed a collaboration (1:21:30–1:22:00).
    - Cuts can look strong yet slow the solver, and gains got harder once the SCIP transplants were used up (0:41:00–0:42:00).
    - Default tuning often fails, and sometimes the opposite of the intended change works, for reasons nobody knows (1:05:00–1:05:30).
    - He is weak at following the literature and needs collaborators. He finds writing the related-work part of a paper the hardest task (1:20:30–1:21:30).
    - Academic reviewers demand wins over commercial solvers, which devalues computational papers (0:51:00–0:51:30).
12. **Declined offer.** He turned down Bixby's first invitation to Gurobi, years before 2014 [stated, caption, 0:43:00].

No retraction, erratum or documented rejection was found (G9).

---

## 7. Authorship and role labels by period (what the record lets the skill say)

| Period | Typical byline | Role the record supports |
|---|---|---|
| 2002–2007 | First or sole author: W1, W4, W5, W7, W8, the thesis | Originator and sole developer of SCIP until 2004 (P2 slide 15); lead author of the branching, conflict and MIPLIB 2003 work |
| 2008–2009 | First author on the CPAIOR and MPC papers; bylines ZIB → ILOG → "ILOG, an IBM company" | Still the SCIP architect while employed at ILOG. Co-author with Berthold and Wolter (whom he calls his students, P1 p. x) and with Heinz |
| 2010–2013 | Co-author: second on MIPLIB 2010, first on hybrid techniques with Lodi and on the 12-years analysis with Wunderling; editor (CPAIOR 2011) | CPLEX developer and MIP lead (P5); bridge between ZIB and the CP–OR community |
| 2014–2021 | First of five, in alphabetical order (presolve); middle or last author (ParaSCIP, MIPLIB 2017, MFAS) | Gurobi developer and then manager; [inferred] in the joint papers his share cannot be separated from the others' |
| 2022–2025 | Last author (RLT, with ZIB) | Industry co-author who ran the Gurobi implementation and tests (P13 §5.7). Which of the authors wrote which parts is **not stated** |

Rule for the skill: "Achterberg did X" can be backed for SCIP up to 2009 (commits, sole-author papers). For CPLEX (2006–2014) and Gurobi (2014–) claims rest on company bios and a few co-authored papers. These should be written as "Gurobi/IBM say…" or "[stated-joint]".

---

## 8. Latest dated traces and the last 12 months (2025-11-08 → 2026-11-08)

- **Inside the window**:
  - **18 Nov 2025**: the "What's New in Gurobi 13.0" webinar page lists him as speaker, "Vice President of Research and Development", with Xavier Nodet and Steven Edwards (P7) [observed]. **Whether he spoke and what he said is not verified.**
    - The nonlinear-team RESOURCES records the 25 Nov 2025 deck as "Nodet, Achterberg" (S11). Not re-fetched here (HTTP 503).
  - **Nov 2025**: the 13.0 release text does not name him (P9).
- **Nothing found in the window**:
  - No paper or preprint: DBLP's last record is *Math. Program.* 210, print Mar 2025 (P15), and the only arXiv preprint is 2211.13545 (S6).
  - No SCIP commit (the last is 16 Dec 2016, P10).
  - No ORCID change (works last modified 21 May 2023, P4).
  - No talk listing on the Gurobi Days Digital 2026 page (16–17 Jun 2026), nor on the Summit EMEA 2025 page (28–29 Oct 2025, just before the window). Only the static HTML was checked; see P8.
  - A web search for "Tobias Achterberg" 2026 returned only namesakes.
- **Just before the window**:
  - **15 Jun 2025**: Substack comment signed "Tobias" on the 8,500-model MIP test set (S3) [stated?].
  - **17 Aug 2023**: the long interview (P14, 84 min). Read only as 14 caption excerpts (P21). By length it is the longest public self-account found.
- **Flag for the synthesis**: the most recent first-hand statements on method and career are from 2022 (slides, read) and 2023 (interview, caption excerpts read). Everything later is a company listing.

---

## 9. Pointers for the synthesis (all [inferred])

- **Turns are triggered by people, code, projects and talks, not by literature.** Evidence: T1–T8.
  - SIP via Koch and Martin.
  - The Infineon project via Grötschel.
  - SAT techniques via Novikov.
  - ILOG via the audience of a 2005 workshop talk.
  - Gurobi via Bixby's standing offer and the chance to work with Gu and Rothberg.

  He says himself that he does not track the literature well (P21 1:20:30).
- ***Instrument first, then measure, then publish* (my label).** SCIP was built for two years before any paper. Every thesis chapter ends with an ablation against the defaults (P1 p. 2). The same reporting form recurs:
  - CPLEX component analysis, 2013 (W25 abstract);
  - Gurobi presolve, disabling components against Gurobi 6.5 defaults, 2016 (P12 p. 2);
  - RLT on/off with shifted geometric means, 2022 (P13 p. 21).

  [inferred] This is the steadiest method signal across 20 years. 03-process-evidence should test it.
- **A negative result reframed into a method** (ML → history values → reliability branching) is his own origin story (P2 slide 7; P21 0:24:00–0:26:00). He applies it again at Gurobi in 2023: explainable ML yields a rule, and the rule is hand-coded into the defaults (P21 1:16:00–1:17:30). This is a candidate layer-5 heuristic with two dated instances 22 years apart: when a learned model works, find out which raw feature or split carries it and build the rule on that.
- **Move by transplanting a tested arsenal.** At CPLEX he first ported what he knew worked from SCIP (P21 0:40:00–0:41:00). [inferred] His job changes carried a stock of proven ideas into a new code base. That is a career-level analogue of *build first, publish later*.
- **Builder, not surveyor** [stated, caption]: he prefers to build from scratch, knows the literature poorly and needs collaborators for it (P21 1:20:30–1:21:30). This is consistent with:
  - SCIP rebuilt from scratch rather than extending SIP (P2 slide 8);
  - missing Hooker's parallel work (P21 1:21:30);
  - co-authors who carry the related-work side, e.g. ZIB colleagues on MIPLIB and RLT.

  [inferred] A skill should pair his lens with a literature check.
- **Seniority caveat**: the post-2014 practices rest on Gurobi's data and machines (§5). A skill using his lens for a single researcher should translate them, e.g. a test set of hundreds of instances instead of thousands, and seeds and permutations instead of a machine farm.
- **Openness vs closed code tension**: free academic code from 2002–2009, closed commercial code from 2006/2014 onwards. Reported from the interview by a listener (S3, paraphrase): academics cannot publish the detailed engineering improvements, so open-source solvers lag. One interview chapter is titled "Computational work is not appreciated as much at it should be" [sic] in Academia (P14). It fits this.

---

## Contradictions (kept, not reconciled)

- **C1. Who wrote SCIP by 2009.**
  - The Beale–Orchard-Hays citation says the 250,000+ lines were "all written by the author himself" (P18 p. 10).
  - His own commit list shows other committers from Jan 2004: Pfetsch, Wolter, Berthold and 13 more before 2009 (P2 slide 15). The thesis credits Wolter's and Berthold's contributions to SCIP's improvement, and says the 250,000 lines cover SCIP *and* the chip-verification solver (P1 p. x).
- **C2. "Almost two years" without a paper (P1 p. ix) vs. a 2003 co-authored chapter** (W2; he is 7th of 8 authors). The chapter may predate SCIP; not resolved.
- **C3. Advisor labels.**
  - Title page: Grötschel and Bixby as Berichter (referees).
  - ZIB OPUS record: both in the "Advisor" field.
  - MGP: Grötschel only.
  - Acknowledgments: Grötschel as "my advisor"; Bixby not mentioned.
- **C4. The CS diploma thesis is dated 2000 in one account and 2001 in the other.** The thesis says work "began already in 2000" (P1 p. ix); the 2022 slide dates the CS thesis 2001 (P2 slide 4). Both can hold (start 2000, finish 2001); kept as two datings.
- **C5. The meeting with Novikov is told differently.** In 2007 he was picked up at a subway station after arriving at Berlin-Ostbahnhof (P1 pp. ix–x). In 2022 it was Berlin Zoologischer Garten (P2 slides 13–14). In 2023 it is an unnamed train station, followed by a subway ride of about 30 minutes (P21 0:31:00–0:31:30, caption). Recollection drift over 16 years; the substance is the same in all three.
- **C6. Date of the Beale–Orchard-Hays Prize.** 23 Aug 2009, at the ISMP opening ceremony (P18 pp. 1, 10), against "09/2009" on a ZIB slide (S2 slide 17).
- **C7. The Gurobi bio contradicts its own header.** The header reads "Vice President of Research and Development"; the text says "Since 2014 he has been involved as a Senior Developer" (P7; same bio on P8). The SEA 2022 bio adds that he "is currently the VP of R&D at Gurobi" (P20). The 2023 YouTube description has "currently being the Vice President of R&D" (P14).
- **C8. Same-year byline conflict (2013).** Springer metadata gives Konrad-Zuse-Zentrum (ZIB) for the Facets chapter (W25) but IBM for CPAIOR 2013 (W24) (P17). Possibly a metadata artefact.
- **C9. Who leads R&D.** In 2020 he "will lead Gurobi's growing R&D department" (P6). In Nov 2025 the CTO, Oliver Bastert, speaks for the technology in the 13.0 release (P9). A search-engine summary (S12) claimed Bastert leads the R&D team; that claim **was not verified** (the release was not reached).
- **C10. Size of the test set: about 6,000 (2023) or 8,500 (2025)?** A listener's write-up gives "6,00 benchmark models" (S3, 2023). The caption text of the interview has about 6,000 instances in the test set (P21 1:05:30). The 2025 comment attributed to him says a zero was missing and gives "about 8500" (S3). The two reports agree on 6,000 in 2023, so the likeliest reading is growth to about 8,500 by mid-2025. The commenter's identity is still unverified.
- **C11. Search-engine misattributions (do not reuse).**
  - A WebSearch summary credited him with CPLEX 11 lead development, the CPLEX QP simplex and MIQP solvers, and presolve and cut routines. On the Gurobi 9.1 page that text is **Zonghao Gu's** bio.
  - Another summary gave him a BA from Oberlin and a PhD from Stanford. That is **Ed Klotz's** bio, on the same page.
- **C12. Three editions of the thesis.** TU Berlin 2007 (DepositOnce, DOI 10.14279/depositonce-1634), the Dr. Hut book of 2008, and ZIB OPUS first published 28 Jan 2009 (P1). Citation years differ by edition.
- **C13. Year of the first SCIP commit: 2001 or 2002?** In the 2023 interview he dates it, with a hedge, to 2001 (P21 0:27:30, caption). The repository (P10), his own 2022 slide (P2 slide 2) and a ZIB deck (S2 slide 13) give 23 Oct 2002. The 2007 thesis says the idea came in 2002 and coding started at the end of 2002 (P1 p. ix). The record is 2002; the interview date is a slip or a mis-captioning.
- **C14. Did the thesis use ML to drop ML?** The 2022 slide frames the outcome positively: history values are good predictors, leading to reliability branching (P2 slide 7). In 2023 he calls the same result disappointing, because the ML only pointed to one feature (P21 0:25:00). Same finding, opposite tone; kept as is.
- **C15. Who brought in the application.** The thesis (P1 p. ix) and the 2022 slides (P2 slide 12) credit Grötschel's contact to Infineon. In 2023 he also credits Grötschel with his late slot at the MIP 2005 workshop, which led to the ILOG offer. He hedges this himself (P21 0:36:00, caption). Not a contradiction, but it makes the advisor's network a trigger at two turns (T4, T6). Kept here because the second claim is uncertain even in his own words.

---

## Gaps

- **G1 (partly closed).** The "Subject to" interview (17 Aug 2023, 84 min; P14) is known only through the 14 caption excerpts a sibling saved (P21): ASR text, not speaker-checked, never compared with the audio. Still unread:
  - The chapter "Why commercial MIP solvers do not support GPU?" (1:10:58). It is worth reading against Gurobi 13.0's GPU PDHG for LP (P9), since a change of stance may show there.
  - The CP-for-MIP chapter (1:13:03) and the GenAI chapter (1:17:42) beyond the excerpt.
  - The opening biography, which was redacted.

  The recording date is unknown, so "as of 2023" means "published 2023".
- **G2 (partly closed).** Reasons for the moves:
  - ZIB → ILOG: the MIP 2005 talk led to an invitation, there were competing offers, and he chose CPLEX on familiarity (P21; caption).
  - IBM → Gurobi: the release quote (P5), Gu and Rothberg (P21), and personal reasons. The personal reasons are deliberately not pursued here.
  - Still missing: any account of why he stopped SCIP work in 2009.
- **G3. Dates still open**:
  - the month of the ILOG start in 2006;
  - the IBM end date;
  - when he became Director of R&D at Gurobi;
  - whether he kept a ZIB appointment after 2006 (he committed from a ZIB address until Mar 2009).
- **G4. CPLEX-era specifics** beyond "lead MIP developer for CPLEX releases 12.0 through 12.6" (P5): which features were his, and his role in the deterministic parallel optimizer (W25 abstract only). Patents were not searched.
- **G5. The Gurobi 13.0 deck** (25 Nov 2025) was not reached (CDN 503). Whether he presented, and which slides are his, is unknown.
- **G6. ZIB-Reports 04-13, 05-19 and 05-42** (team.json chase hints) were not identified: OPUS search returned 500 and curl hit the bot wall. They are not cited.
- **G7. Diploma-thesis titles** (2000, 2001) come only from his slides; no library record was checked.
- **G8. Prizes**: the MOS prize page could not be read (JavaScript). Beale–Orchard-Hays 2009 is confirmed via Optima 80, Dantzig 2008 (second place) and the INFORMS Optimization Society prize 2011 via INFORMS. No later honours were found; fellowships were not checked.
- **G9.** No rejected papers, errata or retractions were found. No public review records exist for this field.
- **G10. 2026 activity**: none found. Talks at Gurobi events may exist without being indexed. One WebSearch was spent on this.
- **G11.** Whether he co-supervised any PhD (MGP lists none; Berthold's later PhD was not checked).
- **G12.** No information on teaching beyond the 2006 teaching tool and the *ORMS Today* note.
- **G13.** The Bastert CTO appointment release (2022) was not read (403/404), so the reporting line of the VP of R&D is unknown.

---

## Sources

**Primary (P)**
- P1. T. Achterberg, *Constraint Integer Programming*, Dr. rer. nat. thesis, TU Berlin, defence 12 Jul 2007. Read: title page and pp. ix–x (as images), pp. 1–3, 183, bibliography.
  - DepositOnce copy: https://api-depositonce.tu-berlin.de/server/api/core/bitstreams/a301bdbc-d04d-4fd5-9e04-c0399908689c/content ; DOI 10.14279/depositonce-1634.
  - ZIB OPUS copy: https://opus4.kobv.de/opus4-zib/frontdoor/index/index/docId/1112 (record: URN urn:nbn:de:0297-zib-11129; book edition Dr. Hut 2008, ISBN 978-3-89963-892-9). Primary.
- P2. T. Achterberg, "SCIP Origins", slides, "Let's SCIP it!" workshop, ZIB, 4 Nov 2022 (PDF created 22 Nov 2022), https://www.scipopt.org/20years/slides/achterberg.pdf. All 21 slides read. Primary.
- P3. "Let's SCIP it! A workshop to celebrate 20 years of Solving Constraint Integer Programs", event page, https://www.scipopt.org/20years/ (speaker list). Primary.
- P4. ORCID 0000-0002-0862-7065, public API v3.0 record. Self-asserted employment at Gurobi Optimization GmbH from 2014-03-04 (entry created 2020-02-06); 2 works. Fetched 2026-11-08. Primary.
- P5. Gurobi Optimization, "Dr. Tobias Achterberg Joins the Gurobi Optimization R&D Team" (page undated; 2014 by content), https://www.gurobi.com/company/newsroom/dr-achterberg-joins-gurobi. Primary (company; contains his quote).
- P6. Gurobi Optimization, "Gurobi Optimization Announces Promotion of Dr. Tobias Achterberg to Vice President of R&D", Beaverton OR, 22 Apr 2020, https://www.gurobi.com/company/newsroom/gurobi-optimization-announces-promotion-of-dr-tobias-achterberg-to-vice-president-of-rd. Primary (company).
- P7. Gurobi, "What's New in Gurobi 13.0" webinar page (event 18 Nov 2025, 10:00 ET), https://www.gurobi.com/resources/webinar-events/whats-new-in-gurobi-13-0. Primary (listing).
- P8. Gurobi webinar pages listing him as speaker. The CMS dates on these pages are unreliable. Primary (listing).
  - 9.1: https://www.gurobi.com/resources/webinar-events/whats-new-in-the-gurobi-optimizer-9-1
  - 9.5: https://www.gurobi.com/resources/webinar-events/whats-new-in-gurobi-9-5
  - 10.0: https://www.gurobi.com/resources/webinar-events/webinar-whats-new-in-gurobi-10-0
  - 11.0: https://www.gurobi.com/resources/webinar-events/whats-new-in-gurobi-11-0
  - Also checked, with no Achterberg in the static HTML: Summit EMEA 2025 (https://www.gurobi.com/microsite/gurobi-summit-emea-2025/speakers) and Gurobi Days Digital 2026 (https://www.gurobi.com/resources/webinar-events/gurobi-days-digital-2026).
- P9. Gurobi, "Gurobi Releases Version 13.0 with Improved Performance and New Solving Capabilities" (Nov 2025; BusinessWire id 20251118616985), https://www.gurobi.com/company/newsroom/gurobi-releases-version-13-0-with-improved-performance-and-new-solving-capabilities. Primary (company).
- P10. GitHub scipopt/scip commit history via the REST API and commit search (login `tobiasachterberg`; 1,303 commits, 2002-10-23 to 2016-12-16), and code search (467 files with `@author Tobias Achterberg`), retrieved 2026-11-08, https://github.com/scipopt/scip. Commits cited (SHA prefixes):
  - 147d536 (first commit)
  - ed966d2 (9 Jul 2008)
  - 7827f4f (3 Sep 2008)
  - 7469d3f (18 Mar 2009)
  - 5c2951b (2 Nov 2014)
  - ce4f13c (12 Dec 2016)
  - 14b4e0a (16 Dec 2016)

  Primary.
- P11. T. Achterberg, T. Koch, A. Martin, "Branching on History Information", ZIB-Report 02-32, published 2002-10-04, https://opus4.kobv.de/opus4-zib/frontdoor/index/index/docId/699 (record and abstract). Primary.
- P12. T. Achterberg, R. E. Bixby, Z. Gu, E. Rothberg, D. Weninger, "Presolve Reductions in Mixed Integer Programming", ZIB-Report 16-44 (cover Sep 2016; title page 9 Dec 2016), https://opus4.kobv.de/opus4-zib/files/6037/Presolve.pdf. Paper pp. 1–2 read. Primary.
- P13. K. Bestuzheva, A. Gleixner, T. Achterberg, "Efficient Separation of RLT Cuts for Implicit and Explicit Bilinear Terms", arXiv:2211.13545 (v1 24 Nov 2022; v3 19 Jul 2024). Read: title page, §5.7 (pp. 21–22), §6, Funding (p. 22). Primary.
- P14. "Subject to: Tobias Achterberg", YouTube channel Subject to, video 8bhIW27vCUQ, published 2023-08-17, 5,062 s, https://www.youtube.com/watch?v=8bhIW27vCUQ. Metadata and chapter list read; audio not reviewed. Primary (unread content).
- P15. DBLP pid 71/6632 via the SPARQL endpoint (`scripts/dblp_works.py --pid 71/6632`), 23 records, fetched 2026-11-08, https://dblp.org/pid/71/6632.html. Primary (bibliographic).
- P16. Crossref REST API records for every DOI below (dates, Crossref citation counts; affiliations for W28 and W30), queried 2026-11-08, https://api.crossref.org. Primary (bibliographic).
- P17. Springer landing-page metadata (`citation_author_institution`, publication history) for W10, W11, W15, W16, W18–W20, W22–W25, W31, W32, https://link.springer.com. Primary (bibliographic).
- P18. *Optima* 80 (Mathematical Programming Society newsletter), Sep 2009. Read: p. 1 (chair's column, 6 Sep 2009), p. 10 (Beale–Orchard-Hays citation and committee), pp. 11–12 (Tucker finalists). https://mathopt.zib.de/Optima-Issues/optima80.pdf. Primary (society record).
- P19. INFORMS, "Award Recipients: Tobias Achterberg" (2008 Dantzig Dissertation Award, second place; 2011 Optimization Society Young Researchers Prize, with citation), https://www.informs.org/Recognizing-Excellence/Award-Recipients/Tobias-Achterberg. Primary (official record).
- P20. SEA 2022, 20th Symposium on Experimental Algorithms (Heidelberg, 25–27 Jul 2022), invited speakers, https://sea2022.ifi.uni-heidelberg.de/. Primary (listing).
- P21. Transcript excerpt of "Subject to: Tobias Achterberg" (YouTube 8bhIW27vCUQ, published 2023-08-17), `../sources/talks/subject-to-2023-interview.excerpt.transcript.txt`.
  - Saved on 2026-11-08 by sibling research agent 04 from YouTube's automatic English captions (yt-dlp): 14 excerpts with timestamps, privacy redactions marked "[...]".
  - Caption text, not speaker-checked, never compared with the audio. Not user-supplied.
  - Primary (his spoken words via ASR).
- P22. MIPLIB 2017 instance pages for aflow30a and aflow40b (submitter "T. Achterberg"; "Arborescence flow problem"; imported from MIPLIB 2010), https://miplib.zib.de/instance_details_aflow30a.html ; https://miplib.zib.de/instance_details_aflow40b.html. Read 2026-11-08. Primary (record).

**Secondary (S)**
- S1. Mathematics Genealogy Project, Tobias Achterberg (id 117695) and Martin Grötschel (id 24939), https://www.mathgenealogy.org/id.php?id=117695 ; https://www.mathgenealogy.org/id.php?id=24939. Read 2026-11-08 (site partly restored after the Oct 2026 outage). Secondary.
- S2. T. Berthold, "SCIP – Solving Constraint Integer Programs", slides (PDF 19 Aug 2011), https://www.zib.de/berthold/Berthold_SCIP.pdf. Slides 10, 13, 17 read. Secondary.
- S3. M. Watson, "Five Ideas I'll use in my optimization class after listening to Gurobi's Tobias Achterberg", *Mike Talks AI* (Substack), 5 Oct 2023, with a comment signed "Tobias Achterberg" of 15 Jun 2025 (identity not verified), https://miketalksai.substack.com/p/five-ideas-ill-use-in-my-optimization. Secondary.
- S4. OpenAlex author A5016513861: 42 works, with landing pages and abstracts for ZR 06-23, 08-29, 08-43 and 20-16, https://api.openalex.org/authors/A5016513861. Secondary.
- S5. zbMATH Open API, author `achterberg.tobias`: 19 documents, https://api.zbmath.org. Secondary.
- S6. arXiv API queries (`au:Tobias_Achterberg` and others): one preprint, 2211.13545, https://export.arxiv.org/api/query. Secondary.
- S7. IDEAS/RePEc abstract of W25, https://ideas.repec.org/h/spr/sprchp/978-3-642-38189-8_18.html. Secondary.
- S8. E. Danna, "Performance variability in mixed integer programming", MIP 2008 slides (ILOG CPLEX R&D; PDF 7 Aug 2008), https://coral.ise.lehigh.edu/mip-2008/talks/danna.pdf. Title slide and date only. Secondary (context).
- S9. E. B. Khalil, P. Le Bodic, L. Song, G. Nemhauser, B. Dilkina, "Learning to Branch in Mixed Integer Programming", *Proc. AAAI* 30 (2016), DOI 10.1609/aaai.v30i1.10080 (Crossref checked). Secondary (context).
- S10. A. M. Alvarez, Q. Louveaux, L. Wehenkel, "A Machine Learning-Based Approximation of Strong Branching", *INFORMS J. Comput.* 29(1) (2017), DOI 10.1287/ijoc.2016.0723 (Crossref checked). Secondary (context).
- S11. Sibling-team notes used as leads only:
  - lp-team `robert-e-bixby/references/research/04-mentorship.md` and `sources/RESOURCES.md` (thesis referee and Achterberg-related rows; re-verified here);
  - nonlinear-team `andreas-wachter/references/sources/RESOURCES.md` row 133 (13.0 deck; **not re-verified**).

  Secondary.
- S12. WebSearch result summaries (5 calls, 2026-11-08), used as leads only. Two misattributions found (C11). Secondary.
- S13. M. Turner, T. Berthold, M. Besançon, T. Koch, "Branching via Cutting Plane Selection: Improving Hybrid Branching", arXiv:2306.06050 (v1 9 Jun 2023), https://arxiv.org/abs/2306.06050. Author list checked via the arXiv API; not read. Secondary (context: the idea he says he ported to Gurobi; he is not an author).

**His own papers and reports (identifiers checked with a tool; read as metadata unless stated)**
- W1. Achterberg, Koch, Martin, "Branching on History Information", ZIB-Report 02-32 (2002). OPUS docId 699 (see P11).
- W2. Eisenblätter, Wessäly, Martin, Fügenschuh, Wegel, Koch, Achterberg, Koster, "Modelling Feasible Network Configurations for UMTS", in *Telecommunications Network Design and Management* (OR/CS Interfaces Series), 2003, DOI 10.1007/978-1-4757-3762-2_1.
- W3. Achterberg, "SCIP – a framework to integrate Constraint and Mixed Integer Programming", ZIB-Report 04-19 (2004), https://opus4.kobv.de/opus4-zib/files/794/ZR-04-19.pdf (via OpenAlex; not opened).
- W4. Achterberg, Koch, Martin, "Branching rules revisited", *Oper. Res. Lett.* 33(1):42–54 (2005), DOI 10.1016/j.orl.2004.04.002.
- W5. Achterberg, Koch, Martin, "MIPLIB 2003", *Oper. Res. Lett.* 34(4):361–372 (2006), DOI 10.1016/j.orl.2005.07.009.
- W6. Achterberg, Grötschel, Koch, "Software for Teaching Modeling of Integer Programming Problems", ZIB-Report 06-23 (2006), https://opus4.kobv.de/opus4-zib/files/917/ZR-06-23.pdf (abstract via OpenAlex). Also "Teaching MIP modeling and solving", *ORMS Today* 33(6):14–15 (2006), per P1 bibliography [3].
- W7. Achterberg, "Conflict analysis in mixed integer programming", *Discrete Optim.* 4(1):4–20 (2007), DOI 10.1016/j.disopt.2006.10.006.
- W8. Achterberg, Berthold, "Improving the feasibility pump", *Discrete Optim.* 4(1):77–86 (2007), DOI 10.1016/j.disopt.2006.10.004.
- W9. Achterberg, Brinkmann, Wedler, "Property Checking with Constraint Integer Programming", ZIB-Report 07-37 (2007), https://opus4.kobv.de/opus4-zib/files/1037/ZR_07_37.pdf (via OpenAlex; not opened).
- W10. Achterberg, Berthold, Koch, Wolter, "Constraint Integer Programming: A New Approach to Integrate CP and MIP", CPAIOR 2008, pp. 6–20, DOI 10.1007/978-3-540-68155-7_4.
- W11. Achterberg, Heinz, Koch, "Counting Solutions of Integer Programs Using Unrestricted Subtree Detection", CPAIOR 2008, pp. 278–282, DOI 10.1007/978-3-540-68155-7_22.
- W12. Achterberg, Koch, Tuchscherer, "On the Effects of Minor Changes in Model Formulations", ZIB-Report 08-29 (2008) (OpenAlex record and abstract; not opened).
- W13. Achterberg, Berthold, Heinz, Koch, Wolter, "Constraint Integer Programming: Techniques and Applications", ZIB-Report 08-43 (2008), https://opus4.kobv.de/opus4-zib/frontdoor/deliver/index/docId/1095/file/ZR_08_43.pdf (abstract via OpenAlex).
- W14. Shinano, Achterberg, Fujie, "A Dynamic Load Balancing Mechanism for New ParaLEX", ICPADS 2008, pp. 455–462, DOI 10.1109/ICPADS.2008.75.
- W15. Achterberg, "SCIP: solving constraint integer programs", *Math. Program. Comput.* 1(1):1–41 (2009), DOI 10.1007/s12532-008-0001-1.
- W16. Achterberg, Berthold, "Hybrid Branching", CPAIOR 2009, pp. 309–311, DOI 10.1007/978-3-642-01929-6_23.
- W17. Baharev, Achterberg, Rév, "Computation of an extractive distillation column with affine arithmetic", *AIChE J.* (2009), DOI 10.1002/aic.11777.
- W18. Achterberg, Raack, "The Mcf-separator: detecting and exploiting multi-commodity flow structures in MIPs", *Math. Program. Comput.* 2(2):125–165 (2010), DOI 10.1007/s12532-010-0015-3.
- W19. Achterberg, Lodi, "Hybrid Solving Techniques", in *Hybrid Optimization* (Springer Optimization and Its Applications), online 2010, DOI 10.1007/978-1-4419-1644-0_5.
- W20. Koch, Achterberg, Andersen, Bastert, Berthold, Bixby, Danna, Gamrath, Gleixner, Heinz, Lodi, Mittelmann, Ralphs, Salvagnin, Steffy, Wolter, "MIPLIB 2010", *Math. Program. Comput.* 3(2):103–163 (2011), DOI 10.1007/s12532-011-0025-9.
- W21. Achterberg, Beck (eds.), *CPAIOR 2011*, Berlin, LNCS 6697 (2011), DOI 10.1007/978-3-642-21311-3.
- W22. Shinano, Achterberg, Berthold, Heinz, Koch, "ParaSCIP: A Parallel Extension of SCIP", *Competence in High Performance Computing 2010* (2011/2012), pp. 135–148, DOI 10.1007/978-3-642-24025-6_12.
- W23. Achterberg, Berthold, Hendel, "Rounding and Propagation Heuristics for Mixed Integer Programming", *Operations Research Proceedings 2011* (2012), pp. 71–76, DOI 10.1007/978-3-642-29210-1_12.
- W24. Achterberg, Sabharwal, Samulowitz, "Stronger Inference through Implied Literals from Conflicts and Knapsack Covers", CPAIOR 2013, pp. 1–11, DOI 10.1007/978-3-642-38171-3_1.
- W25. Achterberg, Wunderling, "Mixed Integer Programming: Analyzing 12 Years of Progress", *Facets of Combinatorial Optimization* (2013), pp. 449–481, DOI 10.1007/978-3-642-38189-8_18 (abstract via S7).
- W26. Shinano, Achterberg, Berthold, Heinz, Koch, Winkler, "Solving Hard MIPLIB2003 Problems with ParaSCIP on Supercomputers: An Update", IPDPS Workshops 2014, pp. 1552–1561, DOI 10.1109/IPDPSW.2014.174.
- W27. Shinano, Achterberg, Berthold, Heinz, Koch, Winkler, "Solving Open MIP Instances with ParaSCIP on Supercomputers Using up to 80,000 Cores", IPDPS 2016, pp. 770–779, DOI 10.1109/IPDPS.2016.56.
- W28. Achterberg, Bixby, Gu, Rothberg, Weninger, "Presolve Reductions in Mixed Integer Programming", *INFORMS J. Comput.* 32(2):473–506 (2020), DOI 10.1287/ijoc.2018.0857 (journal text not read; report P12 read in part).
- W29. Shinano et al., "Solving Previously Unsolved MIP Instances with ParaSCIP on Supercomputers by using up to 80,000 Cores", ZIB-Report 20-16 (2020), https://opus4.kobv.de/opus4-zib/files/7839/ZIB-Report_20-16.pdf (abstract via OpenAlex).
- W30. Baharev, Schichl, Neumaier, Achterberg, "An Exact Method for the Minimum Feedback Arc Set Problem", *ACM J. Exp. Algorithmics* 26, 1.4 (2021), DOI 10.1145/3446429.
- W31. Gleixner, Hendel, Gamrath, Achterberg, Bastubbe, Berthold, Christophel, Jarck, Koch, Linderoth, Lübbecke, Mittelmann, Ozyurt, Ralphs, Salvagnin, Shinano, "MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library", *Math. Program. Comput.* 13(3):443–490 (2021), DOI 10.1007/s12532-020-00194-3.
- W32. Bestuzheva, Gleixner, Achterberg, "Efficient Separation of RLT Cuts for Implicit and Explicit Bilinear Products", IPCO 2023, pp. 14–28, DOI 10.1007/978-3-031-32726-1_2. Extended version: *Math. Program.* 210:47–74 (2025), DOI 10.1007/s10107-024-02104-0, and arXiv:2211.13545 (P13).
- W33. Achterberg, *Constraint Integer Programming* (thesis; see P1), DOI 10.14279/depositonce-1634.
