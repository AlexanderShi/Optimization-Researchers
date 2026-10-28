# Qi Huangfu · Research note 04: students and collaborators (mentorship)

| Field | Value |
|---|---|
| Researcher | Qi Huangfu (皇甫琦; "Huangfu Qi" on his own 2025 slides). Edinburgh MSc in High Performance Computing 2008 and PhD 2013 ("High performance simplex solver", supervisor J. A. J. Hall, second supervisor J. Gondzio). Original author of HSOL, the simplex core of HiGHS. FICO Xpress, then Cardinal Operations (COPT). Living. Not the Zhejiang University medical researchers of the same name. |
| Dimension | Research agent 04 of 06: students and collaborators. Supervision style, group habits, lab culture and tacit knowledge (framework §二). In the seven-layer structure (§一) this note feeds mainly layer 7 (research organisation), and also layers 4 (execution) and 5 (result judgement). |
| Research date | 2026-10-27 |
| Sources consulted | 45 (15 primary, 30 secondary), listed under **Sources**. WebSearch calls: 5 of the 5 allowed. |
| Local corpus | `references/sources/papers`, `essays` and `software` held only `.gitkeep`. There was no user-supplied material. `talks/` held one caption transcript (JuliaCon 2022), which a sibling agent saved in this run; I used it, and it is not user-supplied. `private/` was not opened. |
| Scratch | Downloaded PDFs and clones are in `%TEMP%/lp-team-scratch/base-skills/qi-huangfu/04/`. Nothing copyrighted was added to the repository. |

**Tags.** **[stated]**: Huangfu's own words. **[practice]**: what his papers, code and records show he did. **[observed]**: what others reported, including his supervisor, later students, code maintainers, interviewers and journalists. **[inferred]**: my inference from the cited evidence and nothing more. **P** marks a primary document (by Huangfu, or a record of his own work); **S** marks a secondary one. Quotes are verbatim. Page numbers are the printed page numbers unless "PDF p." is given. Slide numbers are the decks' own numbers.

---

## Key findings (summary)

1. **He has no public supervision record.** No PhD or MSc student, lab page, onboarding guide or student recollection naming him as a supervisor was found. Since 2013 he has worked in industry: FICO Xpress, then Cardinal Operations, where he was vice-president by 2019 and "senior vice-president and technical lead" by 2024. This dimension is therefore documented mostly through **how he was mentored**, **how his code and know-how passed to the next generation**, and **how he behaves as an alumnus, adviser and team member**.
2. **He was trained by apprenticeship-through-reimplementation.** He entered optimization from HPC. He was at EPCC when he saw that "Julian Hall from upstairs is hiring". In Year 1 he rebuilt the simplex method from a C tableau code upward and measured progress by the share of NETLIB he could solve (20%→95%→99%). He then wrote HSOL "from scratch", although his supervisor was at that time the project manager of Clp, the best open-source baseline. [stated] P (2025 slides, thesis), [observed] S (Hall's 2011 slides).
3. **His group was organised as a portfolio of parallel bets with honest verdicts.** Hall ran six parallel-simplex projects with Huangfu, Edmund Smith and Miles Lubin. In 2013 he presented them under the title "Is it time to give up?". His conclusion was "Parallel research has yielded serial results", and "Huangfu's c++ solver hsol" is listed among those serial results. [observed] S
4. **Supervisor credit and authorship followed a visible pattern.** Hall presented the work (the slides list "Written by Qi Huangfu (2010)"). The first paper had Hall first; both journal papers have Huangfu first. Hall stayed the contact author and kept presenting the work during 2014–2017, while Huangfu was at FICO. The journal versions were finished after Huangfu left academia. [practice] P/S
5. **The successors describe the inheritance as single-person code with undocumented choices.** HSOL in 2013 was 24 files and 5,752 lines of code [stated] P. Ivet Galabova calls it "a computer program, written and used by a single person" [observed] S. The maintainers' comments in HiGHS still read "TODO: Check with Qi what this is doing" (added by Hall in 2018) and name a "Qi-trick" (2021). Tacit numerical choices lived only in the code: an update-count tolerance schedule, a finite "infinity" used in scaling, and a logical-basis assumption in dual phase 1. [practice + observed]
6. **He kept advising after he left.** Galabova (PhD 2023) thanks him "for writing the core dual simplex solver, and some valuable advice over the years". He co-authored talks with the group from FICO (2016–2017) and was listed in "Team HiGHS" in 2019. In 2025 he gave an invited "memory piece" talk dedicated "to Julian's 60th birthday". [observed] S, [stated] P
7. **In industry he speaks about training as a problem of tacit pitfalls.** In a 2019 press interview he said the decisive implementation details are "坑" (pitfalls) that appear in neither patents nor papers. He also said graduates "do not know the solver's pitfalls" while companies cannot wait for talent to mature. A second article attributes the training quote to Dongdong Ge, so the attribution is contested. [stated, via journalist] S
8. **His group work in industry shows a lead/integrator role.** In the COPT Julia interface, Lukas Schork wrote 112 commits. He is presumably the Edinburgh PhD alumnus of that name (supervisors Gondzio and Hall per ERA; identity [inferred] from name and field). Huangfu wrote README and release commits and gave the JuliaCon talk. Huangfu authored the public COPT release notes from 2022 to 2024. He has no commits in the cuPDLP-C repository, whose report he co-authored with an SUFE group. [practice] P; the role reading is [inferred].

---

## 1. Scope: an industrial solver developer with no supervision record

- [observed] S. No students are recorded. The Mathematics Genealogy entry (id 204105) was unreachable from here (404). A sibling agent in this run (06-trajectory.md) read a 2025-05-14 Wayback snapshot that says "No students known". I did not see that snapshot myself.
- [practice] P. **Career frame.** He was at FICO from 2013 to 2018, per Hall's slide (ICCOPT 2019, slide 3: "FICO Xpress (2013–2018)"). The MPC paper gives his affiliation as "FICO House, International Square, Starley Way, Birmingham". The Paper of 2019-10-08 calls him "杉数科技副总裁" (Cardinal Operations vice-president). The 2024 press item calls him "杉数科技资深副总裁，技术负责人" (senior vice-president, technical lead). It names him only as "皇甫博士" (Dr Huangfu), so the identification is [inferred].
- [inferred] **The kind of mentoring this dimension can show is limited.** Any mentoring by him happened inside closed industrial teams (Xpress, COPT) or informally toward his old group. The public record shows its traces only: acknowledgements, commit logs, co-authorships and press quotes. Supervision style in the academic sense cannot be distilled from his own practice, so that layer must stay thin in the skill.

## 2. How he was mentored: the Edinburgh path (2007–2013)

### 2.1 Entry route: from HPC into optimization
- [stated] P. The HiGHS Workshop 2025 slides, slide 5 ("The early history: before Year 1"), give the route. Beihang Computer Science and Technology "2003.9-2007.7". Edinburgh EPCC High performance computing "2007.9-2008.8", which "Turned out to be a rather good choice". Then "Got a short-term six-month contract to work in EPCC", "Got an advertisement that Julian Hall from upstairs is hiring", "2008.9-2009.1 Application consultant", "Attended optimization courses (two minutes away from EPCC)" and "Attended courses and started tableau simplex implementation".
- [stated] P. **MSc supervision.** MSc dissertation (22 Aug 2008), acknowledgements (PDF p. 7): "I would like to thanks my supervisors Dr Fiona Reid and Dr Sebastian Geiger. Without their help, it is impossible to finish this project." He also thanks "the SAMG team who gives free libraries and licence, and ECDF team who gives lots of help on using ECDF".
- [practice] P. The MSc project fed a multi-author HPC paper with both MSc supervisors as co-authors: Geiger, Huangfu, Reid, Matthäi, Coumou, Belayneh, Fricke, Schmid, "Massively Parallel Sector Scale Discrete Fracture and Matrix Simulations", SPE Reservoir Simulation Symposium, 2009, DOI 10.2118/118924-MS. I checked only the metadata and abstract (OpenAlex, Crossref) and did not read the paper. [inferred] His first research apprenticeship was in an HPC engineering team. He came to LP solver work as a programmer first.

### 2.2 PhD supervision structure and sponsor
- [stated] P. Thesis acknowledgements (p. 7): "I would like to thank my PhD supervisor, Julian Hall for his support and encouragement over the years. I would also like to thank other staff members in the School of Maths for their help and conversation, in particular, my second PhD supervisor Jacek Gondzio." and "I am grateful to the Format International Ltd. and NAIS for their financial support." (The thesis does not expand NAIS, and I did not verify the expansion.)
- [observed] S. The Edinburgh Research Archive metadata lists the advisors as "Hall, Julian; Gondzio, Jacek".
- [observed] S. **The sponsor was his supervisor's long-standing industrial user.** Galabova's thesis (p. 41): "Format International Ltd. had been using EMSOL as the LP solver in their software for almost twenty years". EMSOL is described there as Hall's "legacy FORTRAN primal simplex solver". In the 2025 interview, Hall's own solver has long been used "in animal feed formulation software produced by Format Solutions". [inferred] The PhD sponsorship came through Hall's consultancy relationship. The sources show the link but do not state that it was the channel.
- [practice] P + [observed] S. **The sponsor's problem sat in the student's test set.** Thesis Table 1.1 (p. 18) includes `dcp2` (32388 rows, 21087 columns, 559390 nonzeros). Hall's HuHa13 page says that "With the exception of dcp2, the test problems used in this paper are drawn from a variety of public domain test sets". Galabova (p. 41) identifies dcp2 as "Format International's Multimix feed formulation test LP problem dcp2". See Contradictions, C2.

### 2.3 Apprenticeship through reimplementation (the Year-1 curriculum)
- [stated] P. **Year-1 Gantt chart, months 1–10** (2025 slides, slide 6, read as an image). It runs in this order: "First tableau simplex (C)" → "Refined tableau simplex (C++)" → "Study NETGEN type problems" → "Sparse tableau simplex" → revised simplex ("20%→95% of NETLIB Solvable", "First working RSM", "Tomlin LU basis inverse", "Scaling algorithm", "Harris' ratio test", "Steepest-edge price", "Hyper-sparse study and first try", "95%→99% of NETLIB solvable", "DEVEX, profiling framework") → "Different basis inverse algorithms" (LIU, row-wise LIU, "Markowitz LU basis inverse", "Integrating different inverse methods", "Refined RHS hyper-sparse").
- [stated] P. Years 2–3 (slide 11, 2009.2–2012.2): tableau solver, primal solver ("Year 1 report"), study of basis factorization, simplex update, "Talk: LIU simplex update", sequential dual solver, preliminary parallel dual solver, "Talk: parallel dual solver", parallel dual solver refinement, hyper-sparsity research. Year 4 (slide 14): "Things start to converge", "Experiments and minor improvements", "Started to work on PhD thesis", "Still feels incomplete".
- [stated] P. The thesis states the from-scratch decision (p. 16): "Though there are many public domain simplex implementations, they are either too complicated to be extended for parallelization or too simple to be based on. Thus, a sequential dual simplex solver, named HSOL, has been implemented from scratch." It also names the method of growth (p. 17): "using C++ provides the opportunity of an evolutionary development process, from a proof-of-idea prototype with simple but less efficient data structures to an efficient elaborated implementation."
- [observed] S. At that time **the supervisor managed the obvious alternative.** Hall's PPAM 2011 slide 34 on Clp says: "Written by John Forrest (IBM)", "Best open-source simplex solver", "H is now project manager".
- [inferred] **Supervision style as received.** The student rebuilt the textbook method himself, one classical technique at a time, and measured each step against NETLIB solvability. He did this instead of extending the supervisor's managed code base. The skill can carry this as "learn a solver by rebuilding it, with a solve-rate metric", tagged era-bound (2009, single developer, NETLIB-sized problems).

### 2.4 Lineage: three generations on one problem
- [observed] S. Hall's homepage: "PhD 1992, supervisor Prof. Roger Fletcher". (His publication list dates the thesis 1991.)
- [stated] P. **The grandfather's idea entered Year 1.** Slide 8 of the 2025 talk quotes the RAL Numerical Analysis Group progress report for 2008–2009. That report lists "Roger Fletcher (Dundee). L-Implicit-U factorization and the Simplex Update" at the meeting of 15–16 July 2009. Slides 9–10 then present his LIU simplex-update work. [inferred] The topic came down the lineage, from Fletcher's talk, through Hall's group, to the first-year student.
- [practice] P/S. The joint EUROPT 2017 talk (Huangfu, FICO; Hall) carries the line "In memory of Roger Fletcher" (title slide).
- [stated] P. **He places himself in his supervisor's tradition.** Thesis (p. 73): "Besides this work, the author knows of only two other full parallel implementations of the the revised simplex method, are all due to Hall and McKinnon." (sic). The FICO blog (KDnuggets repost, 13 June 2014) says that "new ground-breaking research has been published roughly every decade, with the latest one being Hall and McKinnon's hyper-sparsity algorithm in the first decade of the 21st Century." The post's "About the author" note (whose author is not stated) adds: "Notably, his PhD supervisor in Edinburgh, Julian Hall is the one who published the research on hyper-sparsity, resulting in the previous simplex performance leap."
- Lineage papers, each checked with Crossref or on Hall's publication page:
  - Hall & McKinnon, "Hyper-Sparsity in the Revised Simplex Method and How to Exploit it", Comput. Optim. Appl. 32(3):259–283, 2005, DOI 10.1007/s10589-005-4802-0
  - Hall & McKinnon, "ASYNPLEX, an asynchronous parallel revised simplex algorithm", Ann. Oper. Res. 81, 1998, DOI 10.1023/A:1018957107705
  - Hall & McKinnon, "PARSMI, a parallel revised simplex algorithm incorporating minor iterations and Devex pricing", Springer LNCS 1184, 1996 (venue and year from Hall's publication page; page numbers differ between sources)
  - Hall, "Towards a practical parallelisation of the simplex method", Comput. Manag. Sci. 7(2):139–170, 2010, DOI 10.1007/s10287-008-0080-5

### 2.5 How the supervisor presented, credited and published the student's work
- [observed] S. **The implementer is credited by name and year on the supervisor's slides.** RAL seminar, 2 Dec 2010 (Hall, Huangfu, Smith), PDF p. 23: "Written by Qi Huangfu (2010)". LANCS workshop, 12 Apr 2011, PDF p. 21: "Written by Huangfu (2010)". On PDF p. 15 the task-parallel dual variant is "(H and Qi)", and the GPU and block-angular items are "(H and Smith)".
- [practice] S. **The supervisor presented.** Hall's talks page is headed "Talks by J A Julian Hall" and lists the co-authored talks of 2010–2017 with Huangfu. On some decks Huangfu is listed first and with a FICO affiliation (NLAO 2016, ERGO 2016, EUROPT 2017). Even there Hall's voice appears, for example EUROPT 2017 slide 22: "I've been updating for 30 years: time to reinvert!" For the 2014–2016 parallel-dual-simplex talks (ICMS June 2014, NLAO14 Sept 2014, Google Paris 11 Sep 2015, NLAO16 Sept 2016), the talks page lists only "J. A. J. Hall", even where the slides list Huangfu as co-author or first author (Google15, NLAO16).
- [practice] P. **Authorship order changed over time.**
  - PPAM 2011 put the supervisor first: Hall & Huangfu, "A high performance dual revised simplex solver", LNCS 7203:143–151, 2012, DOI 10.1007/978-3-642-31464-3_15.
  - Both journal papers put the student first: "Novel update techniques for the revised simplex method", Comput. Optim. Appl. 60(3):587–608, 2015, DOI 10.1007/s10589-014-9689-1; and "Parallelizing the dual revised simplex method", Math. Prog. Comp. 10(1):119–142, 2018, DOI 10.1007/s12532-017-0130-5, arXiv:1503.01889.
  - Hall's e-mail is the only contact address on all three, and the MPC paper marks him as corresponding author.
- [practice] P. **The papers were finished after he left.** ICCOPT 2013 (1 Aug 2013) lists "Parallelizing the dual revised simplex method with suboptimization … in preparation". The MPC paper was "Received: 6 March 2015 / Accepted: 10 February 2016 / Published online: 14 December 2017", with Huangfu at FICO. Its conclusion speaks of him in the third person (p. 141): "With the techniques described in this paper, Huangfu has raised the performance of the Xpress parallel revised simplex solver to that of the worlds best commercial simplex solvers." [inferred] The supervisor drove the publication process after graduation. The text does not say who wrote which sentence.

### 2.6 Group organisation: a portfolio of parallel bets, judged in public
- [observed] S. The ICCOPT 2013 talk (1 Aug 2013) was titled "Parallelizing the (revised) simplex method: Is it time to give up?". Its authors were Huangfu, Hall, Lubin and Smith, and it was presented by Hall. It reviews six projects:
  - 1 PAMI and 2 SIP: "Huangfu and H"
  - 3 block structure: "H and Smith (2010-12)"
  - 4 stochastic block structure: "Lubin and H (2012)"
  - 5 and 6 GPU and multicore standard simplex: "H and Smith (2012)"

  The sibling bet with Lubin was published as Lubin, Hall, Petra, Anitescu, "Parallel distributed-memory simplex for large-scale stochastic LP problems", Comput. Optim. Appl. 55(3):571–596, 2013, DOI 10.1007/s10589-013-9542-y. It won COAP's best paper of 2013 (Hall's prizes page). The verdicts are plain. Project 3 reports "For Netlib problems: average speed-up 0.5". PAMI "average speed-up 1.5; best 2.63"; SIP "average speed-up 1.1; best 2.05". Slide 22 concludes: "No "silver bullet" for general parallel simplex"; "Is this problem/method/architecture environment relevant?"; "Parallel research has yielded serial results" (listing "Novel update techniques", "Insight into promoting hyper-sparsity", "Novel edge weight strategies", "Huangfu's c++ solver hsol").
- [practice] P/S. **The parallel projects were siloed per student.** Edmund Smith's thesis ("Parallel solution of linear programs", Edinburgh 2013; supervisors Hall and Grothey) never mentions Huangfu. Huangfu's thesis bibliography has no Smith entry. Both were in the same group under the same first supervisor in 2009–2013. [inferred] Each student owned one bet end to end, and the supervisor was the only integrator.
- [observed] S. **The supervisor's stated values set the culture.** Stirling 2019, slide 37: "Novel techniques of practical value are hard to find but get noticed" and "Having a high-performance solver is good for consultancy, Impact and kudos". The 2025 School interview by Michael Forward reports "Julian's focus on coding and consultancy" and that "he regrets that prowess in research is seen by many as the only objective of an academic career". It also notes "15 papers in 32 years", "four have won their journal's best paper prize". Two of those four are the Huangfu–Hall papers: COAP best paper 2015 and MPC best paper 2018, per Hall's prizes page and Springer's MPC prize page.

### 2.7 The supervisor's verdict on the student
- [observed] S. Google Paris, 11 Sep 2015, conclusions slide 43: "Helped develop two really talented young researchers: Qi Huangfu and Miles Lubin".
- [observed] S. The 2025 interview, a journalist's paraphrase of Hall that does not name the student: "With barely a hint of lamentation, he admits that his solver was bested by a PhD student of his, and it was this solver that eventually grew into the HiGHS software that he is currently developing with current PhD students." [inferred, strong] The student is Huangfu. The HiGHS README says the simplex solvers were "originally written by Qi Huangfu", and Galabova (p. 41) traces HiGHS to "Huangfu's serial dual simplex solver".
- [observed] S. Hall's homepage: "based on solvers written by Leona Gottwald and former PhD students Michael Feldmeier and Qi Huangfu, I am managing the development of the world's best open-source linear optimization software HiGHS." KTH 2021, slide 26: "Huangfu applied the parallel dual simplex techniques within the Xpress solver" and "For much of 2013-2018 the Xpress simplex solver was the best in the world".

## 3. Hand-over: how his code and know-how passed to the next generation

### 3.1 What was handed over
- [stated] P. The 2025 slides, slide 2, give the "Code stats of HiGHS 2013 (hsol)": 24 files, 916 blank, 704 comment and 5,752 code lines (C++ 4,825; headers 860). The same slide gives "HiGHS now": 689 files and 278,573 code lines.
- [observed] S. Galabova's thesis (p. 41): "The transformation of a computer program, written and used by a single person, into a well maintained product, used by multiple people, is a non-trivial task."
- [observed] S. The ERGO seminar of 30 Nov 2016 (slides list "Qi Huangfu (FICO), Julian Hall, Others"), slide 36, frames the open-sourcing question: "Useful open-source resource?", "Reliable?", "Well-written?", "Better than clp?". It also lists the limitations: "No presolve", "No crash", "No advanced basis start".
- [observed] S. HSOL 1.0 README (first commit `67647f4`, 2017-07-06, in `mattmilten/h2gmp`; the `galabovaa/h2gmp` original now returns 404): "HSOL was originally written by Qi Huangfu, with features such as presolve, crash and advanced basis start added by Julian Hall and Ivet Galabova." The git history starts with that import. Huangfu has no commits in it, and none in the 15,343 commits of `ERGO-Code/HiGHS`: I checked author names and commit messages.

### 3.2 HiGHS as the inheritance
- [observed] S. Galabova (p. 41): "The development of HiGHS can be traced back to the autumn of 2016, when I combined Huangfu's serial dual simplex solver [31] with my prototype presolve implementation." The prototype was benchmarked against EMSOL on dcp2. "A three-year £46k consultancy contract was signed to fund the development of an industrial strength presolve and rudimentary MIP solver."
- [observed] S. **The name keeps the student.** ICCOPT 2019 slide 3, Fields 2021 and KTH 2021 slide 2 all say: "What's in a name? HiGHS: Hall, ivet Galabova, Huangfu and Schork". The HiGHS `AUTHORS` file lists "Main Authors" as Hall, Galabova, Huangfu, Gottwald, Feldmeier. `CITATION.cff` and the README ask users to cite Huangfu & Hall (MPC 2018). The README (master `73cac48`, 2026-08-19) says: "HiGHS has primal and dual revised simplex solvers, originally written by Qi Huangfu and further developed by Julian Hall."

### 3.3 His thesis and test set became the group's reference material
- [observed] S. Feldmeier's thesis (2025, p. 27): "An overview and example of such a basis matrix factorization is given in Huangfu's 2013 dissertation: [27]."
- [observed] S. Schork's thesis (2019, p. 84): "The test set were the 30 LP models used by Huangfu and Hall [38], which represent a wide range of structural properties." Galabova's thesis (2023, p. 33): "This is the set used by Huangfu and Hall in [31], with qap15 replacing dcp2 because QAP problems are of particular interest and dcp2 is not a public test problem".
- [practice] S. **The test set was shared.** Hall's HuHa13 page: "For convenience, they are collected in HuHa13_TestSet.zip (90MB)".
- [inferred] **A group habit.** One student's 30-problem reference set became the default benchmark of three later students. It was kept for 2013–2023 and modified only where the problems were not public or not of interest.

### 3.4 What the successors did not carry forward
- [observed] S. The HiGHS documentation (`docs/src/parallel.md`, master `73cac48`) says the parallel speed-up is "typically less than the values achieved by [Huangfu and Hall]". It gives the reason: "This is because enhancements to the serial dual simplex solver in recent years have not been propagated to the parallel solver." It adds: "Unless an LP has significantly more variables than constraints, the parallel dual simplex solver is unlikely to be worth using."
- [observed] S. ICCOPT 2019, slide 20, "Immediate enhancements": "Resurrect pami". [inferred] Once the author had left, the parallel part (PAMI) was the hardest piece for the successors to maintain. The serial core was the part they adopted.

### 3.5 His behaviour toward the next generation: alumnus and informal adviser
- [observed] S. Galabova's thesis acknowledgements (p. 4): "I would like to express my gratitude to Qi Huangfu for writing the core dual simplex solver, and some valuable advice over the years, and to Lukas Schork for his contributions and style." What the advice was is not recorded.
- [practice] S. Talks with the group while he was at FICO:
  - ERGO seminar, 30 Nov 2016: "Qi Huangfu (FICO), Julian Hall, Others". The slides list him first. Who presented is unclear (see C6).
  - SIAM OP17, 22 May 2017: Hall, Huangfu (FICO), Galabova, "An open-source high performance dual simplex solver".
  - EUROPT, 13 Jul 2017: Huangfu (FICO) and Hall.
- [observed] S. ICCOPT 2019, slide 3, "Team HiGHS", lists "Qi Huangfu" with three sub-bullets: "PhD (2009–2013)", "FICO Xpress (2013–2018)", "MSc (2018–date)". These are verbatim, and "MSc" is not explained. Slide 21, "HiGHS: The future": "Add primal simplex solver (Huangfu)". The 2021 decks (Fields, 11 Aug; KTH, 1 Oct) list "Team HiGHS" as Hall, Galabova, Feldmeier and Gottwald, without Huangfu. The same decks still credit "Dual simplex (Huangfu and Hall)".
- [stated] P. **He returned as an invited speaker.** "Early history and recent observations of HiGHS", HiGHS Workshop 2025, Edinburgh, 27 June 2025. The last slide: "I dedicate this memory piece to Julian's 60th birthday. Thank you". (The workshop schedule lists him at 11:30.)
- [inferred] **Mentoring after graduation was informal and slowly faded.** It ran through advice, co-authored talks, a team listing and a commemorative talk, not through code contributions. The decline from 2019 to 2021 coincides with his industrial move to Cardinal Operations. The record does not show the cause.

## 4. Tacit knowledge: what lived in his code and talk but not in the papers

Each item is labelled with who reports it. All code facts were checked in the cloned repositories at the stated commits.

| # | Tacit item | Evidence | Tag |
|---|---|---|---|
| T1 | **An update-count-dependent pivot tolerance in CHUZC.** `Ta = 1e-9` if fewer than 10 updates since reinversion, `3e-8` if fewer than 20, otherwise `1e-6`. | HSOL `HDualRow.cpp` lines 59–60 and 238–239 at commit `67647f4` (2017 import of his code). Still in HiGHS `highs/simplex/HEkkDualRow.cpp` at `73cac48`. A text search of the thesis finds no description of this schedule. Hall wrote above it "TODO: Check with Qi what this is doing" (and on `createFreemove`: "TODO: Check with Qi what this is doing and why it's expensive"). He added both in commit `ee4971d2a` (2018-11-01, "After cleaning up some unused code in HDual.h/cpp and adding a lot of documentation"), and both comments remain in 2026. | [practice] P; [observed] S (Hall, code comments); [inferred]: the rationale was never written down, and the maintainer needed the author to explain it |
| T2 | **The "Qi-trick" in scaling.** A finite "infinity" (`HSOL_CONST_INF = 1e200`). Running minima start at `inf`, maxima at `1/inf`, and scale factors are `1/sqrt(min*max)`. Empty rows or columns therefore get a unit scale with no special case. The same routine skips scaling if every abs(a_ij) lies in [0.2, 5], includes costs if the smallest nonzero abs(c_j) < 0.1, and makes up to 6 passes. | HSOL `HModel::scaleModel()` and `HConst.h` at `67647f4`. HiGHS `HighsLpUtils.cpp` comment added by Hall in commit `ace075e4` (2021-08-09): "Now that kHighsInf = std::numeric_limits<double>::infinity(), this Qi-trick doesn't work so, in recognition, use the old value of kHighsInf". The thesis does not describe matrix scaling (checked). His Year-1 chart has a "Scaling algorithm" bar. | [practice] P; [observed] S (Hall named it after him); [inferred]: what the trick is for, read from the arithmetic |
| T3 | **Repeatable performance was preserved by keeping his random sequence.** | HiGHS `HEkk.cpp` (master `73cac48`): "Re-initialise the random number generator and generate the random vectors in the same order as hsol to maintain repeatable performance" | [observed] S (maintainers) |
| T4 | **An implicit starting-basis assumption in dual phase 1.** hsol did not change phase-1 bounds for free rows. This works from a logical basis or crash, but failed when SCIP made a nonbasic row free. | HiGHS `HEkk.cpp` comment added by Hall in commit `3ccac325` (2022-10-28, "Fix in dual phase 1 to handle nonbasic free rows from an advanced start"): "Phase 1 bounds were not modified for free rows in hsol. Why?". HSOL had "No advanced basis start" (ERGO 2016, slide 36). | [observed] S; [inferred]: the design assumption was implicit in a single-user code and surfaced only in new uses, nine years later |
| T5 | **The serial code was kept simple on purpose, to make parallel design tractable.** | Thesis p. 94: "In this research, it has been intended to keep the serial implementation simple so that parallelization can be relatively easily designed and implemented." He gives a concrete shortcut: a BFRT pass is run even when no variable is boxed. 2025 slide 19 restates the principle: "A worthwhile simplex parallelisation should be based on a good sequential simplex solver." | [stated] P |
| T6 | **A learning habit: re-read the classic until it opens.** | 2025 slides: slide 15 cites Forrest & Tomlin (1972); slide 16: "读书百遍，其义自见 / Read a book a hundred times, and its meaning will become clear". Year 4 lists "Forrest-Tomlin update" (slide 14). | [stated] P; [inferred]: the link between slides 15 and 16 is read from their order |
| T7 | **Industrial know-how is pitfalls that are never published.** | The Paper, 2019-10-08. A journalist's paraphrase introduced by "据皇甫琦介绍" (according to Huangfu): "这些细节说白了就是坑，这些坑国外这些人走了30年，坑都踩了，人家怎么踩的，专利里论文里都没有，我们只能一个个去踩坑。" My translation: put plainly, these details are pitfalls; foreign teams walked into them over 30 years, how they did it is in neither patents nor papers, and we can only step into them one by one. A direct quote in the same article, on extreme coefficients such as 10^7 next to 10^-7: "…怎么取解决，国外的求解器团队不会告诉你的，就需要自己想办法去解。" My translation: how to solve it, the foreign solver teams will not tell you; you have to find your own way. | [stated] S (press) |
| T8 | **Training solver developers: what graduates lack.** | The Paper, 2019-10-08. His three requirements, paraphrased by the journalist: strong mathematics and optimization; strong coding and systems engineering; ideally solver-development experience. Direct quote: "高校培养的同学，可能最大的问题是学生解决能够多方兼顾能力不太够，求解器里面有哪些坑，他们不知道。而国内企业培养人才又有点急功近利，等不起一个人才慢慢成熟。" My translation: graduates' biggest problem may be that they cannot balance many aspects at once, and they do not know the solver's pitfalls; domestic companies, for their part, are too eager for quick results to wait for talent to mature. **The attribution is contested** (C1). | [stated] S, contested |

[inferred] **The common thread.** The knowledge he holds that is hardest to transfer is numerical and implementation detail. Examples are tolerances, scaling idioms and basis assumptions. His successors met it as comments that ask "Check with Qi". He himself describes it as unpublished "pitfalls" learned by experience. A skill built from him should treat "ask the code's author, or read the code, before trusting the paper" as a real working rule in solver engineering, and say plainly that the paper trail under-describes the implementation.

## 5. Collaborators and roles (who, when, and what the record shows)

| Collaborator | Period | Relation and evidence | Tag |
|---|---|---|---|
| Fiona Reid (EPCC), Sebastian Geiger (Heriot-Watt) | 2007–2009 | MSc supervisors (acknowledgements). Co-authors of the SPE 2009 paper (DOI 10.2118/118924-MS) | [stated] P, [practice] P |
| Julian Hall | 2008/9–2017, plus 2025 | PhD supervisor; co-author of all three published simplex papers (PPAM 2011, COAP 2015, MPC 2018) and of talks from 2010 to 2017; corresponding author. Hall's slides still credit him in 2021 | [practice] P, [observed] S |
| Jacek Gondzio | 2009–2013 | Second PhD supervisor (acknowledgements, ERA) | [stated] P |
| Edmund Smith | 2010–2013 | Fellow PhD student, co-listed on Hall's talks of 2010, 2011 and 2013. The two theses do not cite each other | [practice] S |
| Miles Lubin (then Argonne/MIT) | 2013–2015 | Co-listed on ICCOPT 2013 and Google 2015. Named by Hall with Huangfu as "two really talented young researchers" | [observed] S |
| Ivet Galabova | 2016–2017, plus advice "over the years" | Co-author of talks (SIOPT17). Inherited his code. Acknowledges his advice | [observed] S |
| FICO Xpress team | 2013–2018 | Membership not public. Third-person record that "Huangfu has implemented them within the FICO Xpress simplex solver" (MPC p. 140) | [observed] S |
| Dongdong Ge, Zizhuo Wang, Jian Wu, Yinyu Ye | 2022– | Co-authors of the COPT User Guide (arXiv:2208.14314, Cardinal Operations). The 2024 press item describes "葛冬冬教授领导的杉数COPT团队" (the COPT team led by Prof. Ge), with Huangfu as "资深副总裁，技术负责人" | [practice] P, [observed] S |
| Lukas Schork and Joachim Dahl. Schork is presumably the Edinburgh PhD alumnus (2015–2018 per ICCOPT19 slide 3; supervisors Gondzio and Hall per ERA; HiGHS interior point author per the README); the identity is [inferred] from name and field | 2022– | `COPT-Public/COPT.jl`. Schork has 112 commits from 2022-04-05 (the wrapper; "Copy MOI_wrapper.jl from CPLEX interface") and Dahl 53+7. Huangfu has 5 commits on 2022-04-27/29 (README and release links) plus 1 as `huangfu7` on 2024-09-03. Huangfu gave the JuliaCon 2022 talk on it. Who recruited whom is not documented | [practice] P; [inferred]: a lead/representative role for Huangfu, an implementer role for Schork |
| Haihao Lu, Jinwen Yang (University of Chicago); SUFE: Haodong Hu, Jinsong Liu, Tianhao Liu, Chuwen Zhang, Dongdong Ge; Yinyu Ye | 2023–2024 | cuPDLP-C report (arXiv:2312.14832; Huangfu's affiliation "Cardinal Operations"; NSFC-funded per the footnote). There are no Huangfu commits in `COPT-Public/cuPDLP-C`; the authors who commit there are the SUFE and other contributors | [practice] P; [inferred]: a senior or advisory role in that report, not an implementing one |
| COPT release management | 2022-04-29 to 2024-12-06 | 16 commits in `COPT-Public/COPT-Release` by "Qi Huangfu" or `huangfu7` (release notes and links); later commits come from the shared `COPT-Public` account | [practice] P |

- [stated] P. **Self-description in the team.** JuliaCon 2022 caption transcript: "My name is Huangfu Qi, I am one of COPT developer." He also says the Julia interface "is maintained directly by the COPT team", and he invites outside contributors: "Going forward, we may need your help to get COPT Julia interface better. You can start by trying out our interface, report issues and bugs." The pretalx speaker bio says instead "Qi Huangfu is the developer of COPT" (see C4).

## 6. Failures, abandoned directions and unfinished work

| # | What | Evidence | Tag |
|---|---|---|---|
| F1 | **The L-Implicit-U simplex update was abandoned in Years 1–2.** | 2025 slide 10 shows an earlier write-up with this passage highlighted: "Though experimental code proves the possibility of this approach, it also suggest that the LIU update is not an attractive choice in terms of the solution time. The LIU simplex update is not further studied or applied in the simplex solvers." The slide says the work was reported at the 2nd IMA NLAO conference (Sept 2010, Birmingham). I did not verify that talk. | [stated] P |
| F2 | **The ParISS prototype (2011) was superseded.** | ERGO-11-007 / PPAM 2011: "ParISS, is efficient when run in serial and offers modest speed-up". It was replaced by HSOL, PAMI and SIP by 2013. | [practice] P |
| F3 | **The planned CPU+GPU dual simplex was not pursued.** | LANCS 2011 (Hall's slides, PDF p. 24): "Outcome will inform planned CPU+GPU implementation of dual simplex with suboptimization." The 2013 thesis is CPU/OpenMP only. It judges dense GPU-style parallel simplex work (p. 70): "none is of real novelty". | [observed] S + [stated] P; [inferred]: abandoned, see C3 |
| F4 | **Hyper-sparsity promotion and LiDSE were left at an early stage.** | APMOD 2012 talk "Promoting hyper-sparsity in the revised simplex method" (Hall & Huangfu, Paderborn, 28 Mar 2012, per Hall's talks page). Thesis p. 94: "Although the investigation into hyper-sparsity promotion though led to the successful LiDSE approach, it still at an initial stage." No journal paper appears on Hall's publication list (checked). | [stated] P; [inferred]: not carried to publication |
| F5 | **Overlapping INVERT remained future work.** | Thesis p. 94 lists overlapping the LU factorization as future work. I found no public evidence that it was done (it may exist inside closed Xpress or COPT code). | [stated] P; gap |
| F6 | **Modest speed-ups, judged in public.** | Thesis p. 94: "For the reference set, PAMI provides an average speedup of 1.49. Though not extremely impressive, the performance of PAMI is comparable to the dual simplex implementation of Cplex". ICCOPT 2013: "Is it time to give up?" | [stated] P; [observed] S |
| F7 | **The parallel solver decayed after hand-over.** | HiGHS docs: "unlikely to be worth using". ICCOPT 2019: "Resurrect pami" | [observed] S |
| F8 | **The thesis ran past its deadline.** | 2025 slide 20, "The early history: … the two extra months", shows a university e-mail of 16 Jan 2013 saying the thesis was due "by 31st January 2013" and that an extension must be discussed "with your supervisor urgently". The repository date is 2013-07-01. | [stated] P; [inferred]: an extension of about two months |
| F9 | **There was a long publication lag.** | MPC paper: received 6 Mar 2015, accepted 10 Feb 2016, online 14 Dec 2017 (front page). It was "in preparation" in Aug 2013 (ICCOPT 2013). | [practice] P |

## 7. Era and resource context

| Period | Setting | Resources and team | Seniority |
|---|---|---|---|
| 2007–2008 | EPCC MSc in HPC | University HPC systems (ECDF and others named in the dissertation acknowledgements); two supervisors; external library team (SAMG) | MSc student |
| 2009–2013 | ERGO group, School of Mathematics, Edinburgh | 2010–2011: "dual quad-core AMD Opteron 2378 system" (Hall's 2010–11 slides). Thesis: "compute64b", "a workstation with 16 (Intel Xeon E5620, 2.4GHz) cores"; "Intel C++ Compiler (version 13.0) with OpenMP 3.1" (p. 17). Baselines Clp 1.14 and Cplex. Team: Hall plus 2–3 students and collaborators (Smith, Lubin). Industrial sponsor Format International, plus NAIS | PhD student, single developer of his code |
| 2013–2018 | FICO, Birmingham (Xpress) | Commercial code base and team (size not public). MPC experiments with Xpress | Industrial developer ("simplex guy", 2014 blog bio) |
| 2016–2023 | HiGHS productization (successors) | Format consultancy £46k over 3 years (Galabova). Later Google and Huawei funding (2025 interview) | Alumnus adviser |
| 2019–2026 | Cardinal Operations (COPT), Shanghai | Company team led publicly by D. Ge. SUFE academic partners. GPU (H100) work by 2023–24. NSFC grants on cuPDLP-C | VP (2019), senior VP and technical lead (2024) |

[inferred] **Transfer warnings for the skill.** The apprenticeship-by-reimplementation route (2.3) assumes a single developer, NETLIB-scale tests and years of PhD time. The "ask the author" route (§4) assumes the author is reachable. In a company, both are replaced by team code review and release discipline, and the public record does not show how he runs those.

## 8. Mapping to the seven layers (what this note can feed into the skill)

| Layer | Findings | Strength |
|---|---|---|
| 7 Research organisation | 2.5 (credit and authorship), 2.6 (portfolio of bets, siloed students), 3.5 (alumnus advice), 5 (industry roles), T8 (training views) | Medium. Mostly the supervisor's practice and the industry record; his own supervision style is not documented |
| 4 Execution | 2.3 (rebuild from the tableau upward, NETLIB solve-rate milestones), T1–T5 (code-level tacit knowledge), 3.3 (shared test set) | Medium-high (code and self-report) |
| 5 Result judgement | 2.6 ("Is it time to give up?"), F1, F6, F7 | Medium |
| 1 Taste | T5, T7 (implementation details decide outcomes) | Low-medium |

---

## Contradictions

Recorded as found and not reconciled.

- **C1. Who said the training quote?** The Paper (王心馨, 2019-10-08) attributes the three talent requirements and the quote "高校培养的同学…等不起一个人才慢慢成熟" to 皇甫琦, who is introduced as Cardinal Operations vice-president. The Science and Technology Daily article (马爱平, 2019-11-15, reprinted on The Paper) gives almost the same quote to 葛冬冬 (Dongdong Ge), with slightly different wording ("学生解决问题的能力能够多方兼顾的不太多").
- **C2. Is dcp2 public, and what is it?** Galabova (p. 41, p. 33) calls it "Format International's Multimix feed formulation test LP problem" and "not a public test problem". Hall's HuHa13 page treats it as the one non-public problem. Yet Hall's PublicLP page offers `DCP2` (32388 × 21087, 559390 nonzeros, the same dimensions) for download, described as a "Decentralised planning problem".
- **C3. GPU stance over time.** In 2011 the group planned a "CPU+GPU implementation of dual simplex with suboptimization" (Hall's LANCS slides). The 2013 thesis judges dense or GPU parallel simplex work "none is of real novelty" (p. 70). In 2023–24 he co-authored cuPDLP-C, a GPU first-order LP solver. In 2024 he is reported as saying that elaborate tricks adopted because of CPU limits "可能不再需要" (may no longer be needed).
- **C4. "the developer" or "one of" the developers.** The JuliaCon 2022 pretalx bio says "Qi Huangfu is the developer of COPT". In the talk itself he says "I am one of COPT developer". The 2024 press item places him under a COPT team "led by" Ge.
- **C5. Claimed parallel performance versus the successors' verdict.** The thesis and MPC say PAMI performance is "comparable to the dual simplex implementation of Cplex", and the paper describes the work as "the first parallel revised simplex solver of general utility". The current HiGHS docs say the parallel dual simplex "is unlikely to be worth using" unless there are many more variables than constraints, because serial improvements were not propagated. Different code versions are involved. Kept as a tension.
- **C6. Who presented the 2016 ERGO seminar?** Hall's talks page and the slides list "Q. Huangfu and J. A. J. Hall" (Huangfu first, FICO). A search-result snippet titles the ERGO abstract page "Julian Hall (University of Edinburgh)". The page now redirects, so it could not be read.
- **C7. Bibliographic disagreements found while checking.**
  - The COAP 2015 prize note: Hall's publication page gives "65 (1), 1-4, 2016" and the DOI prefix "10.1016". Crossref gives 65(3):541–544 (Dec 2016), DOI 10.1007/s10589-016-9882-5.
  - The COAP update paper: Crossref gives issue 60(3). Hall's 2019 and 2021 slides give "60(4)".
  - PARSMI: pages 359–368 on Hall's publication page, pp. 67–76 in the thesis and MPC references.
  - Hall's PhD: "PhD 1992" on his homepage; the thesis is dated 1991 on his publication list.
- **C8. Team membership over time.** In 2019 Huangfu is listed in "Team HiGHS" with the unexplained "MSc (2018–date)". In 2021 he is not listed. The `AUTHORS` file still lists him among the "Main Authors", and the acronym still contains his name.

## Gaps

- **Supervision by Huangfu.** I found no student, intern, postdoc, lab guide or recollection naming him as a mentor, at FICO, Cardinal Operations or any university. The search budget was 5 calls: Chinese name plus COPT; English name plus Cardinal plus talk/interview; FICO blog; acknowledgement phrases; HiGHS history.
- **The content of his "valuable advice"** to Galabova is not recorded.
- **Hiring and recruitment** in COPT (Schork, Dahl) is not documented. Whether Huangfu recruited former Edinburgh colleagues is unknown.
- **The COAP 2015 Best Paper Prize note** (DOI 10.1007/s10589-016-9882-5) is paywalled and was not read. Hall's page describes it as an "Article written about the work leading to the award". It is probably the best first-hand account of how the student–supervisor work arose, and a good candidate for user-supplied material.
- **Not readable here:**
  - the original FICO blog (bot wall; read via the KDnuggets repost only; a sibling note reports a Wayback copy dated 13 May 2014)
  - the Edinburgh news item "An advance in the parallel simplex algorithm for linear programming" (content no longer served; search snippet only)
  - the Mathematics Genealogy id 204105 (404)
  - Hager's COAP best-paper page (gone; Wayback unavailable)
  - the DBLP 116/5281 record (bot wall; co-authors rebuilt from OpenAlex, arXiv and Crossref)
  - the REF 2021 impact case study on Format/Cargill mentioned by Galabova (not located)
- **No recording of the 2025 workshop talk** was found, so his spoken commentary on the slides (e.g. on the Year-4 "Still feels incomplete") is unknown. Slides 21–22 of that deck contain personal social-media screenshots and were deliberately not used.
- **The meaning of "MSc (2018–date)"** on Hall's 2019 slide is unexplained.
- **NAIS** (thesis funder) is not expanded or verified.
- **Who wrote the third-person sentences** about Huangfu in the MPC conclusion is not stated.
- **Whether the thesis's future-work items** (overlapping INVERT, polishing serial code) were done inside Xpress or COPT cannot be checked (closed source).
- **Lukas Schork's thesis acknowledgements** were not printed (only his citations of Huangfu were checked). Michael Feldmeier's acknowledgements do not mention Huangfu.

## Sources

**Primary (P): Huangfu's own words, works, code and records**

1. Q. Huangfu, "Optimization of a large-scale parallel finite element – finite volume C++ code", MSc in High Performance Computing dissertation, University of Edinburgh, 22 Aug 2008. https://static.ph.ed.ac.uk/dissertations/hpc-msc/2007-2008/Qi_Huangfu.pdf (front matter and acknowledgements read). P
2. Q. Huangfu, "High performance simplex solver", PhD thesis, University of Edinburgh, 2013. http://hdl.handle.net/1842/7952 (front matter, ch. 1, ch. 5, selected passages of ch. 2–4 and the bibliography read). P
3. J. A. J. Hall, Q. Huangfu, "A high performance dual revised simplex solver", PPAM 2011, LNCS 7203:143–151, 2012. DOI 10.1007/978-3-642-31464-3_15. Technical report ERGO-11-007 (12 May 2011) read in part. P
4. Q. Huangfu, J. A. J. Hall, "Novel update techniques for the revised simplex method", Comput. Optim. Appl. 60(3):587–608, 2015. DOI 10.1007/s10589-014-9689-1. ERGO-13-001 (7 Jul 2013) front matter read. P
5. Q. Huangfu, J. A. J. Hall, "Parallelizing the dual revised simplex method", Math. Prog. Comp. 10(1):119–142, 2018 (CC BY 4.0). DOI 10.1007/s12532-017-0130-5; arXiv:1503.01889 (ERGO-14-011). Front matter, §5.4, §6 and references read. P
6. Q. Huangfu, "The Algorithm that Runs the World Can Now Run More of It", KDnuggets, 13 Jun 2014 (repost of the FICO blog post). https://www.kdnuggets.com/2014/06/fico-algorithm-that-runs-world.html P
7. Q. Huangfu, "COPT and its Julia interface", JuliaCon 2022 lightning talk, 27 Jul 2022. Talk page and bio: https://pretalx.com/juliacon-2022/talk/XRDNVT/. Caption transcript: `../sources/talks/juliacon-2022-copt-and-its-julia-interface.transcript.txt` (saved by a sibling agent from the YouTube subtitle track; not speaker-checked). P
8. Huangfu Qi, "Early history and recent observations of HiGHS", HiGHS Workshop 2025, Edinburgh, 27 Jun 2025. Slides (23 pp., PDF author "Huangfu Qi") at https://drive.google.com/file/d/18lPElo2ga37ugFEoKJh3w3auag5UXd7Q/view, linked from https://workshop25.highs.dev/schedule. Slides 1–20 and 23 read; 21–22 not used. Kept local only. P
9. S. Geiger, Q. Huangfu, F. Reid, S. Matthäi, D. Coumou, M. Belayneh, C. Fricke, K. Schmid, "Massively Parallel Sector Scale Discrete Fracture and Matrix Simulations", SPE Reservoir Simulation Symposium, 2009. DOI 10.2118/118924-MS (metadata and abstract only; not read). P
10. D. Ge, Q. Huangfu, Z. Wang, J. Wu, Y. Ye, "Cardinal Optimizer (COPT) User Guide", arXiv:2208.14314 (v1 30 Aug 2022; v4 30 Jan 2026). Author list and front matter checked. P
11. H. Lu, J. Yang, H. Hu, Q. Huangfu, J. Liu, T. Liu, Y. Ye, C. Zhang, D. Ge, "cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language", arXiv:2312.14832 (v2, 7 Jan 2024). Authors, affiliations and funding read. P
12. HSOL 1.0 source and README, first import commit `67647f40b03a30e93c363d329ad2a710df2766e3` (2017-07-06), https://github.com/mattmilten/h2gmp (copy of the now-404 `galabovaa/h2gmp`). P (code; README written by others)
13. COPT-Public/COPT.jl git history, https://github.com/COPT-Public/COPT.jl (cloned 2026-10-27). P
14. COPT-Public/COPT-Release git history, https://github.com/COPT-Public/COPT-Release (cloned 2026-10-27). P
15. COPT-Public/cuPDLP-C git history, https://github.com/COPT-Public/cuPDLP-C (cloned 2026-10-27; no Huangfu commits). P

**Secondary (S): supervisor, successors, maintainers, press**

16. J. A. J. Hall, homepage, https://webhomes.maths.ed.ac.uk/hall/ (read 2026-10-27). S
17. J. A. J. Hall, Publications page, Prizes page and project pages HuHa13/, HuHa12/, HaHu11/, COAP_Prize_2015/, PublicLP/ under https://webhomes.maths.ed.ac.uk/hall/. S
18. J. A. J. Hall, Talks page, https://webhomes.maths.ed.ac.uk/hall/Talks.html. S
19. Hall, Huangfu, Smith, "A high performance dual revised simplex solver", RAL seminar, 2 Dec 2010, https://webhomes.maths.ed.ac.uk/hall/RAL10/RAL10.pdf. S
20. Hall, Huangfu, Smith, "High performance computing and the simplex method", LANCS workshop, 12 Apr 2011, https://webhomes.maths.ed.ac.uk/hall/Lancs11/Lancs11.pdf. S
21. Hall, Huangfu, "A high performance dual revised simplex solver", PPAM 2011, 13 Sep 2011, https://webhomes.maths.ed.ac.uk/hall/PPAM11/PPAM11.pdf. S
22. Huangfu, Hall, Lubin, Smith, "Parallelizing the (revised) simplex method: Is it time to give up?", ICCOPT 2013, 1 Aug 2013, https://webhomes.maths.ed.ac.uk/hall/ICCOPT13/ICCOPT13.pdf. S
23. Hall, Huangfu, Lubin, "High performance simplex solvers for linear programming problems", Google Paris, 11 Sep 2015, https://webhomes.maths.ed.ac.uk/hall/Google15/Google15.pdf. S
24. Huangfu, Hall, "Parallelizing the dual revised simplex method", NLAO16, Birmingham, Sep 2016, https://webhomes.maths.ed.ac.uk/hall/NLAO16/NLAO16.pdf (title page only). S
25. Huangfu, Hall, "Others", "Novel update techniques for the revised simplex method (and their application)", ERGO seminar, 30 Nov 2016, https://webhomes.maths.ed.ac.uk/hall/ERGO_301116/ERGO_301116.pdf. S
26. Hall, Huangfu, Galabova, "An open-source high performance dual simplex solver", SIAM OP17, 22 May 2017, https://webhomes.maths.ed.ac.uk/hall/SIOPT17/SIOPT17.pdf. S
27. Huangfu, Hall, "Novel update techniques for the revised simplex method", EUROPT, 13 Jul 2017 ("In memory of Roger Fletcher"), https://webhomes.maths.ed.ac.uk/hall/EUROPT17/EUROPT17.pdf. S
28. J. Hall, "HiGHS: a high-performance linear optimizer", ICCOPT 2019, Berlin, 6 Aug 2019, https://webhomes.maths.ed.ac.uk/hall/ICCOPT19/ICCOPT19.pdf. S
29. J. Hall, "High performance solution of large-scale linear programming problems", Stirling seminar, 1 Nov 2019, https://webhomes.maths.ed.ac.uk/hall/Stirling19/Stirling19.pdf. S
30. J. Hall, "HiGHS: Theory, software and Impact", Fields Institute, 11 Aug 2021, https://www.fields.utoronto.ca/talk-media/1/41/79/slides.pdf. S
31. J. Hall, "HiGHS: Theory, software and Impact", KTH seminar, 1 Oct 2021, https://webhomes.maths.ed.ac.uk/hall/KTH21/KTH21.pdf. S
32. I. L. Galabova, "Presolve, crash and software engineering for HiGHS", PhD thesis, University of Edinburgh, 2023, http://hdl.handle.net/1842/39725 (acknowledgements, §4.1.2, ch. 5 read). S
33. M. Feldmeier, "Going quadratic: applying advanced techniques from linear programming to convex quadratic programming", PhD thesis, University of Edinburgh, 2025, http://hdl.handle.net/1842/43008 (acknowledgements and citations read). S
34. L. M. Schork, "Basis preconditioning in interior point methods", PhD thesis, University of Edinburgh, 2019, http://hdl.handle.net/1842/35682 (citations of Huangfu read). S
35. E. Smith, "Parallel solution of linear programs", PhD thesis, University of Edinburgh, 2013, http://hdl.handle.net/1842/8833 (front matter read; full-text search: no mention of Huangfu). S
36. HiGHS repository, https://github.com/ERGO-Code/HiGHS. Master `73cac48c5340d775a477087198611862559be250` (2026-08-19): README.md, AUTHORS, CITATION.cff, docs/src/{index,parallel,solvers}.md, source comments. History commits `ee4971d2a702549ef0dc93aa33d38dfaf3bc735e` (2018-11-01), `ace075e4caa602cdd45395021c52bcddd7f8bc0e` (2021-08-09), `3ccac3255d59018aca1af1afa0af7a9415abe982` (2022-10-28). S (maintainers) and inherited code
37. M. Forward, "Academic Interviews: Julian Hall", School of Mathematics, University of Edinburgh, 22 Apr 2025, https://maths.ed.ac.uk/about-us/academic-interview-series/data-decisions/julian-hall. S
38. Springer, Mathematical Programming Computation best paper prize list (2018 winner: Huangfu & Hall), https://www.springer.com/journal/12532/updates/17226372. S
39. "COAP 2015 Best Paper Prize", Comput. Optim. Appl. 65(3):541–544, 2016, DOI 10.1007/s10589-016-9882-5. Crossref metadata and the Springer reference list only; full text paywalled, **not read**. S
40. Edinburgh Research Archive record for hdl 1842/7952 (DSpace API; advisors "Hall, Julian; Gondzio, Jacek"). S
41. Optimization Online author page, https://optimization-online.org/author/qi-huangfu/. S
42. 王心馨, "杉数科技创始人葛冬冬：'数学规划求解器'为什么需要国产化", 澎湃新闻 (The Paper), 2019-10-08, https://www.thepaper.cn/newsDetail_forward_4618351. S (press; quotes 皇甫琦)
43. 马爱平 (科技日报), "这个跻身世界前列的求解器到底是个什么神器？", reprinted on The Paper, 2019-11-15, https://m.thepaper.cn/newsDetail_forward_4970883. S (press; gives the talent quote to 葛冬冬)
44. 数据猿 (Tencent News account) relaying TMTPost (钛媒体), "杉数科技用GPU芯片开启运筹学新的'大航海时代'，发布支持GPU的一阶算法求解器", 2024-03-15, https://news.qq.com/rain/a/20240315A042OG00. S (press)
45. Bibliographic services used to rebuild the co-author list because DBLP was blocked: OpenAlex (author A5076220947 and work records), arXiv API (au:Huangfu), Crossref (DOIs above, including the lineage papers 10.1007/s10589-005-4802-0, 10.1023/A:1018957107705, 10.1007/s10287-008-0080-5, 10.1007/s10589-013-9542-y). S
