# 04 · Students and collaborators: supervision style, group habits, tacit knowledge

> **Researcher**: Samuel A. (Sam) Burer, Tippie Rollins Professor and Chair/DEO, Department of Business Analytics, Tippie College of Business, University of Iowa. Google Scholar BScCde0AAAAJ; DBLP 96/4845; ORCID 0000-0001-5886-458X; Mathematics Genealogy Project (MGP) 114747.
> **Dimension**: research agent 04 of 06 (students and collaborators), framework §二. Mainly layer 7 (research organization). The tacit-knowledge items also feed layers 4 (experiment and execution), 5 (result judgment) and 6 (expression).
> **Research date**: 2026-10-10. **Sources consulted**: 35 (16 primary, 19 secondary), listed under "Sources". **WebSearch calls**: 2.
> **Run type**: first write. No earlier `04-mentorship.md` existed.
> **Local corpus**: `references/sources/papers`, `essays` and `software` hold no user-supplied files (only `.gitkeep`). `talks/` holds four YouTube auto-caption transcripts that sibling agents saved earlier today. They are not user-supplied. I read all four. I did not open `references/sources/private/`.
> **Labels**: [stated] = Burer said or wrote it. [practice] = what he did: papers, bylines, code, CV records. [observed] = what students, collaborators or the press report. [inferred] = my reading of a pattern, which nobody stated. **P** = primary (by Burer, or a record of his own actions). **S** = secondary. Student acknowledgements are first-hand student accounts, but they are secondary with respect to Burer, so they appear as "according to <student>, <source>" with S.
> **ASR** = YouTube automatic speech recognition transcript. Its wording can be wrong, so ASR text is quoted only with this marker and never cleaned up.
> **Quotation conventions**: a " / " inside a quotation marks a line break on a title page or slide. Line-break hyphens and PDF-extraction artifacts (a missing space, a garbled "ñ" or "×") are silently repaired. Nothing else is changed.
> **Scope note**: this note covers *how* he supervises and works with people. The content of the research is covered in 01, 03 and 06. 06-trajectory already holds the lineage timeline. Where I reuse a 06 fact without re-checking it, I say so.

---

## 0. Bottom line (for the synthesizer)

1. **A small, two-faculty "group".** The CV records 7 PhD advisees in 25 years, and MGP adds 2 more where he was second advisor. Their graduations are spread out: 2006, 2007, 2010, 2011, 2015, 2016, 2017, 2023 and 2026 (expected). Kurt Anstreicher co-supervised 2 of the 5 Burer-supervised theses I read and sat on the committee of the other 3. Students treat the pair as one unit: Park thanks "my academic fathers, Kurt and Sam" and Yang calls Anstreicher's ideas "big rescues when my research got stuck". [practice P; observed S]
2. **What students say he gave them** (acknowledgements, 2010–2023): patience; support when stuck; precise writing, including grammar corrections; presentation skills; how to *teach*; and, in one case, freedom to pick the topic. Concrete craft items appear too: "how to use SeDuMi" and "breaking down hard math problems into easier ones". [observed S]
3. **Credit norms visible in bylines.** Alphabetical order is the default in this field, and every advisee's surname sorts after "Burer". Even so, 6 of the 8 advisees with joint papers are first author on at least one paper with him, and so is a visiting PhD student (Eltved). Substantial suggestions are thanked in the acknowledgements rather than turned into co-authorship, in both directions: Gusmeroli's paper thanks Burer, and Burer's sole-author paper thanks Anstreicher. [practice P; inferred]
4. **The advisor packages the code.** The released code for student papers lives in, or was set up from, his GitHub account: QuadProgBB (Chen), ttrs/ttrsn2 (Yang) and the initial commits of Zhu's `extvdom`. From Dec 2025 the only written "onboarding" documents in his public footprint are instruction files for AI coding assistants. No student lab guide exists publicly. [practice P]
5. **One model of the advisor-advisee relationship that he chose to show.** In his 2023 prize lecture he put screenshots of the 22 May 2000 e-mails on slides titled "The Advisor-Advisee Relationship". They show a late-night student prototype ("a quick implemenation [sic]"), the advisor's reply 50 minutes later, and the advisor setting the bar ("compete with the bundle method"). I found no evidence on whether he runs his own group this way. [stated/practice P; inferred]
6. **Era and resources.** NSF CAREER money (2006–12) partly supported Dong's thesis research. The CV lists no external grant after 2012, while he directed master's programs (2014–20). All student experiments ran on single desktop or workstation machines with MATLAB/YALMIP, SeDuMi/MOSEK and CPLEX/Gurobi, with BARON as the benchmark. [practice P/S; inferred about funding]
7. **Biggest gap.** I found no first-person statement by Burer on how he advises PhD students, and no critical or negative account by any student. All student evidence comes from the acknowledgement genre, which is uniformly positive.

---

## 1. The roster: what the records show

### 1.1 PhD advisees

Sources: CV "Ph.D. Advisor" table (read in `pdftotext -table` mode; layout mode misaligns this table); thesis title pages; Iowa Research Online (IRO) records; MGP.

| Advisee | Degree, date | Burer's role (by source) | Placement (CV: initial → current) | Thesis (identifier) | Read? |
|---|---|---|---|---|---|
| Yilin Zhu | Mathematics, "2026 Spring (expected)" (CV, 12 Feb 2026) | CV: advisor. Not in MGP | — | Not deposited in IRO as of 2026-10-10 (repository search returned only his papers) | not read |
| Kyungchan Park | Business Administration (Business Analytics), Aug 2023 (title page). CV says "2023 Spring" | Title page: "Kurt M. Anstreicher, Thesis Supervisor / Samuel A. Burer, Thesis Supervisor". CV: "(with K. Anstreicher)". MGP: student | not listed | "Advances in convex relaxations for quadratic optimization: a study on conic programming relaxations including second-order-cone and semidefinite programming", DOI 10.25820/etd.007220 | front matter, computational sections |
| Guanglin Xu | Business Administration (Management Sciences), Aug 2017 | Sole thesis supervisor | Univ. of Minnesota → UNC Charlotte | "Optimization under uncertainty: conic programming representations, relaxations, and approximations", DOI 10.17077/etd.6m2pvuum | front matter, computational sections |
| Nathaniel Richmond | AMCS, Dec 2016 | Title page: co-supervisor with P. Krokhmal. MGP: advisor 2. **CV: "Ph.D. Committee" only** | — | "On stochastic network design: modeling approaches and solution techniques", DOI 10.17077/etd.lz5powef | front matter |
| Boshi Yang | AMCS, Aug 2015 | Sole thesis supervisor | Carnegie Mellon → Clemson | "A conic optimization approach to variants of the trust region subproblem", DOI 10.17077/etd.wvkyfp48 | front matter |
| Hongbo Dong | AMCS, Dec 2011 | Co-supervisor with Anstreicher (title page; CV) | Univ. of Wisconsin–Madison → Meta | "Copositive programming: separation and relaxations", DOI 10.17077/etd.kzq65y36 | front matter |
| Jieqiu Chen | Business Administration, July 2010 | Sole thesis supervisor | Argonne National Laboratory → Microsoft | "Convex relaxations in nonconvex and applied optimization", DOI 10.17077/etd.xz5r3ajb | front matter, computational sections |
| Changhui Choi | Management Sciences, Spring 2007 | CV: advisor. **Not in MGP** | Univ. of Colorado Denver → Korea Insurance Research Institute | not found in IRO | not read |
| Yi Zhang | Management Sciences, 2006 | MGP: advisor 2 (advisor 1 W. Nick Street). **CV: "Ph.D. Committee" only** | — | "Constructive and Destructive Optimization Methods for Predicative Ensemble Learning" (title from MGP), not found in IRO | not read |

MGP counts "7 students and 8 descendants", and Dong has 1 descendant. [observed S]

### 1.2 Committees, committee composition and other roles (CV, table mode) [practice P]

- **Thesis committees he sat on**: 40 PhD committees from 2006 to 2026. 10 of them were at other universities: Carnegie Mellon (Saxena 2008, Hoda 2010, Wang 2022), Georgia Tech (Liang 2022, Sujanani 2024), Columbia (Michalka 2013), Lehigh (Kuang 2017), National University of Singapore (Yan 2017), UT Austin (Mittal 2019), Université Paris 13 (Bettiol 2019). The 30 Iowa committees by unit: Management Sciences 10, AMCS 8, Computer Science 6, Business Analytics 2, Industrial Engineering 2, Mathematics 1, Health Informatics 1. He also sat on 47 qualifying, comprehensive or preliminary committee entries, advised 7 projects (graduate and undergraduate, 2006–2020) and supervised 6 directed readings (MBA/AMCS, 2012–2013).
- **His own students' committees.** [practice S, from the title pages]
  - Chen 2010: Burer, Anstreicher, N. Street, J. Ohlmann, P. Krokhmal.
  - Dong 2011: Anstreicher and Burer, L. Jay, Krokhmal, Ohlmann.
  - Yang 2015: Burer, Anstreicher, Jay, Krokhmal, **Akiko Takeda** (affiliation not checked in this run).
  - Xu 2017: Burer, Anstreicher, Q. Lin, T. Yang, **Luis F. Zuluaga** (Xu thanks him for an invitation to the COR@L Seminar).
  - Park 2023: Anstreicher and Burer, Q. Lin, B. Basciftci, Y. Chen.
  - Richmond 2016: Krokhmal and Burer, A. Campbell, W. Han, D. Stewart.
- **Postdoc**: Nayoung Cho, "Management Sciences (with A. Campbell)", Spring 2009 to Summer 2010. The CV lists one resulting paper: [J29] "Modifying Soyster's Model for the Traveling Salesman Problem with Interval Travel Times", with N. Cho and A.M. Campbell, *Far East Journal of Applied Mathematics* 86(2):117–144, 2014. This entry comes from the CV only; it is not in Crossref and I did not verify it elsewhere.
- **Sponsored short-term visitors** (CV, table mode): Mirjam Dür (Groningen), June 2007; Peter J.C. Dickinson (Groningen), March 2012; Nicolò Gusmeroli (Klagenfurt), April–May 2019; Anders Eltved (DTU), September 2019 to January 2020.
- **Pipeline and program roles.**
  - Director of Graduate Studies, Business Analytics Doctoral Program (2023–25), and Chair of the Business Analytics Ph.D. Committee (2023–25).
  - Advisory Board Member, FutureBAProf Workshop (2022–24).
  - Faculty in Applied Mathematical and Computational Sciences (AMCS) since 2004. He served on the AMCS Admission Committee (2011–12) and the AMCS Executive Committee (2012–18), and on the Management Sciences Graduate Committee (2003–05, 2006–07, 2013–15).
  - "Graduate Mentor (Ethnic Inclusion Effort for Iowa Engineering)": James Ratliff, Industrial Engineering, 2011–13.

---

## 2. Upstream: how he was supervised, in his own telling (lineage)

Context: PhD in Algorithms, Combinatorics, and Optimization at Georgia Tech, 2001, "advised by R.D.C. Monteiro" (CV). Five of his 2001–2003 journal papers are "with R.D.C. Monteiro and Y. Zhang" (CV [J50], [J52]–[J55]). The low-rank paper itself, [J51], is "with R.D.C. Monteiro" alone. [practice P]

- **The open door.** "Montero was very nice to me I would go by all the time and would talk to me as much as I wanted to talk um we thought you know it couldn't hurt to try" (ASR; "Montero" = Monteiro). Source: University of Iowa talk "Two Decades of Low-Rank Optimization", March 2023. [stated P]
- **The e-mails he chose to show** (slides 31–34 of 63, all titled "The Advisor-Advisee Relationship", SIAM OP23 test-of-time lecture, Seattle, 2 June 2023; read from the slide images). [practice P (record) + stated P (choice to present)]
  - Mon, 22 May 2000, 23:04:25. Burer to Monteiro, "Dr. Monteiro,": "I did a quick implemenation of the low-rank idea for the primal maxcut that we were talking about, and it looks promising. The convergence is good, and of course, the computation and memory requirements are less." Then: "One example: On G1, the new approach cuts the times for both the function and gradient evaluations by approximately 1/2." (The typo "implemenation" is in the original.)
  - Mon, 22 May 2000, 23:54:49. Monteiro to Burer, "Sam:": "This is really good news. Let us hope that this approach works well on all problems. If so, we may have some chance to compete with the bundle method on some maxcut problems."
  - Slides 32 and 34 repeat these screenshots with highlight boxes on "convergence is good, and of course, the computation and memory requirements are less" and on "well on all problems. If so, we may have some chance to compete with the bundle method on some maxcut problems".
  - The 2023 screenshot shows the archive open in a text-mode mail client: folder `./Monteiro.mbox`, "Message 1,371 of 2,501" (reply: 1,372 of 2,501). In the talk he says he "went back into my old emails which I actually still have" (ASR).
- **How he framed it for the audience** (same talk, ASR): "just for any graduate students in the room the time was about 11 pm", and "my advisor wrote back right before midnight on the same day". He goes on: "I wrote back another day later and I'd been able already to streamline it and get it roughly 30 times faster so so this was you know some quick stuff that we're doing just to get it the Prototype out there". He also recalls being "a little bit bold" in asking his advisor to come to the computer lab. The ASR for that passage is garbled, so I paraphrase it here outside quotation marks. [stated P]
- [inferred] The model he holds up has four parts: (a) an advisor who is always available; (b) a student who prototypes fast and reports a concrete number (G1, about 1/2) rather than an impression; (c) an advisor who replies within the hour and adds a benchmark target ("compete with the bundle method"); (d) "can't hurt to try" as the rule for deciding to start. I found **no** source on whether he reproduces (a)–(c) with his own students. The students' "always been helpful" (Chen) fits (a) but says nothing about response time.
- Era: Georgia Tech, 2000. The student wrote and ran the C code himself. The pair worked with a regular outside co-author at Rice (Y. Zhang). He held a "Presidential Fellowship, Georgia Institute of Technology, 1997-2001" (CV).

---

## 3. Supervision style as his students describe it [observed, S]

All quotes are verbatim from the dissertations' front matter. I removed line-break hyphens and fixed one character-encoding glitch ("Peña").

| Student (year, role) | What they say (verbatim) | Where |
|---|---|---|
| **Jieqiu Chen** (2010, sole advisee) | "Sam is the most effective teacher I have encountered in my academic life. During my first year at the University of Iowa, I took Sam's Linear Programming class, which I found was one of the easiest graduate classes. It is not because the subject of linear program itself was easy, but that Sam had explained complicated theories in a way easy for students to understand that made the class easy." / "Sam also taught me numerous other things: from basic concepts of semidefinite programming to how to use SeDuMi to solve an optimization problem, and from breaking down hard math problems into easier ones to how to make a research presentation. I am especially thankful for that he corrected the grammar errors in my thesis and has always been helpful when I face difficulties with research." | Acknowledgements, p. iii (PDF p. 9) |
| **Hongbo Dong** (2011, co-advised with Anstreicher) | "I sincerely thank them for introducing me to this area and helping me realize doing research is of great fun and rewarding. I feel extremely fortunate be their student, not only because they are very successful, brilliant researchers, but also in many other aspects in life, they are my exemplar models." / "During the work of research included in this thesis, I communicated with Professor Javier Peña, Carnegie Mellon University, USA and Professor Monique Laurent, CWI, The Netherlands. Professor Pablo Parrilo provided his great insights when I talked to him during an Oberwolfach Seminar in May, 2010." / "part of research in this thesis was supported by NSF Grant CCF-0545514." | Acknowledgements, p. iii (PDF p. 9) |
| **Boshi Yang** (2015, sole advisee) | "First of all, I would like to sincerely thank my advisor, Professor Sam Burer, who guided me into this wonderful world of optimization." / "None of my achievements during these years would have been accomplished without his support. To me, Sam is not only my advisor, but also a kind friend, a caring family and a remarkable role model. In addition to his knowledge in optimization, I have learned much more from his character. His patience, professionalism and responsibility will benefit me for the rest of my life." On Anstreicher: "His ideas have always been big rescues when my research got stuck, and his handshake is awesome." He also thanks former Burer student Hongbo Dong, among others, "for their kind support". | Acknowledgements, p. iii (PDF p. 6) |
| **Nathaniel Richmond** (2016, co-supervised; primary advisor Krokhmal) | "I would like to thank my advisor, Dr. Pavlo Krokhmal, for his expert guidance over several years. I would also like to thank the other outstanding professors who taught me to love operations research: Dr. Samuel Burer, …" / "I am especially grateful to all of the above people for their personal mentorship throughout my graduate career." | Acknowledgements, p. ii (PDF p. 5) |
| **Guanglin Xu** (2017, sole advisee) | "I cannot imagine that I could complete this thesis without his insightful discussions, continued encouragement, and unconditional support. I am extremely thankful for his incredible patience and extraordinary enthusiasm, which are contagious and motivational for me, even during the toughest times. He taught me how to think critically, write precisely, and present clearly. He encouraged me to explore research topics that I am interested in. He also showed me how to be a rigorous and effective teacher. "More importantly", he set up an excellent example as a cool professor, which is demanding in the research community." On Anstreicher: "I also appreciate his warm encouragement to my presentation." On Zuluaga: "for inviting me to present my research at COR@L Seminar". | Acknowledgements, pp. iii–iv (PDF pp. 6–7) |
| **Kyungchan Park** (2023, co-advised with Anstreicher) | "Lastly, I'd like to express my deepest gratitude to my academic fathers, Kurt and Sam, for their invaluable guidance and unwavering support throughout this journey." | Dedication page, p. ii (PDF p. 4) |

How often each theme appears across the five Burer-supervised theses I read (Chen, Dong, Yang, Xu, Park), plus Richmond where noted. [inferred from the table]

- Support or help when stuck: 4 of 5 (Chen, Yang, Xu, Park).
- Role model or character: 3 (Dong, Yang, Xu).
- Teaching, both as a teacher and as a model for teaching: 2 (Chen, Xu), plus Richmond.
- Writing and presentation: 2 (Chen, Xu).
- Patience: 2 (Yang, Xu).
- Research as fun: 1 (Dong).
- Freedom to choose the topic: 1 (Xu).

Caveat: acknowledgements are a thanking genre. They show what students chose to name, not how often or how intensely he supervised. No student describes meeting frequency, deadlines or conflicts.

Topic origin differs by student. [practice P; inferred]
- Yang's TRS topic continues Burer and Anstreicher's own SOC-RLT line (see 06, T5).
- Xu's robust and distributionally robust work was a new area for Burer, which fits Xu's "encouraged me to explore research topics that I am interested in".
- Chen's first papers (2009) extend Burer's earlier lines on KKT-based branch-and-bound and lift-and-project. Her 2011/12 QuadProgBB paper then makes her first author (§4.3).

---

## 4. Group habits visible in the record

### 4.1 Burer and Anstreicher work as a two-person group [practice P/S; observed S]

- Anstreicher co-supervised Dong (2011) and Park (2023), and sat on the committees of Chen (2010), Yang (2015) and Xu (2017) (title pages). So he appears on all five Burer-supervised theses I read.
- Joint student papers with both of them:
  - Yang, Anstreicher, Burer, "Quadratic programs with hollows", *Math. Program.* 170:541–553 (online 2 May 2017), DOI 10.1007/s10107-017-1157-0.
  - Anstreicher, Burer, Park, "Convex hull representations for bounded products of variables", *J. Global Optim.* 80(4):757–778, 2021, DOI 10.1007/s10898-021-01046-7.
- A co-advisee publishing with one co-advisor only: Dong and Anstreicher, "Separating doubly nonnegative and completely positive matrices", *Math. Program.* (online 23 Aug 2011), DOI 10.1007/s10107-011-0485-8.
- How Burer credits Anstreicher:
  - Slide: "Theorem (B 2023 -- but gifted to Kurt)" and "Proof. Leverages key idea of Ye-Zhang (2003) with a key assist from Kurt." ("Kurt-Fest!" slides, SIAM OP23, 2 June 2023, slide 24/27.) [stated P]
  - Paper: "The author expresses his sincere thanks to Kurt Anstreicher for an important observation, which ultimately led to the establishment of Theorem 1." (S. Burer, "A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints", arXiv:2303.01624v2, Acknowledgments; *Math. Program.* 211:157–179, DOI 10.1007/s10107-024-02076-1.) [stated P]
- The partnership continues after Anstreicher's retirement ("Happy Retirement, Kurt!", Kurt-Fest slide 3, 2 June 2023): Burer and Anstreicher, "Applications of the Lorentz positive cone in nonconvex quadratic optimization", arXiv:2609.32017v1, 25 Sep 2026. [practice P]
- What students say: Yang ("big rescues when my research got stuck"), Xu ("inspirational suggestions to my research", "warm encouragement to my presentation"), Park ("my academic fathers, Kurt and Sam"). [observed S]
- [inferred] For a student, "working with Burer" in practice means working with the Burer–Anstreicher pair. Anstreicher is the default second reader, and the person who gets a student unstuck.
- Era and resources: two senior faculty in one small business-school operations research department (Management Sciences, renamed Business Analytics in April 2019 per the CV) from 2001 to 2023. There was no lab, and only a handful of advisees in 25 years (§7). How many overlapped is unknown, because their start dates were not found.

### 4.2 How students reach him [practice P; observed S]

- **From the classroom.** Chen first met him as the teacher of her first-year Linear Programming class (Chen, p. iii). That this is how she came to choose him as advisor is [inferred]. The CV lists that course under "Course Design and Development": "Linear Programming (Iowa 06K:286/MSCI:6600), Fall 2004".
- **Two degree channels**, plus mathematics:
  - The business PhD (Management Sciences / Business Analytics): Choi, Chen, Xu, Park.
  - The interdisciplinary AMCS program, where he has been faculty since 2004 and served on its admission and executive committees: Dong, Yang, Richmond.
  - Mathematics: Zhu.
  - [inferred] The AMCS channel brings in mathematically trained students for the theory-heavy theses (Dong's copositive separation work, Yang's trust-region variants).
- **Undergraduates and mixed teams.** For the 2016 Syngenta Crop Challenge: "Ling Tong, Bhupesh Shetty, and I formed a team and entered the contest. Ling is a senior in the Business Analytics and Information Systems major, and Bhupesh is a third-year Ph.D. student in the Department of Management Sciences." (Blog post "Syngenta Crop Challenge", 11 May 2016. The post's tags include "fun" and "students".) They placed third of 36 teams (CV; blog). Iowa Now (T. Snee, 31 Mar 2016): "Burer's team, which also includes UI doctoral student Bhupesh Shetty and undergraduate business analytics and information systems (BAIS) major Ling Tong, is one of six invited to the finals April 11 in Orlando, Florida." [stated P; observed S]
- **Stated education plan** in the 2006 CAREER award, NSF 0545514 (2006-06-01 to 2012-05-31, $400,000): "Educational activities of the project include: (i) outreach efforts to strengthen K-12 education, engage the community, and encourage the participation of underrepresented groups in computer science and information technology; (ii) course development activities that provide modern, high-quality instruction in optimization and related disciplines for undergraduate, graduate, and professional students." [stated P] I did not verify whether the K-12 outreach happened.

### 4.3 Authorship and credit norms [practice P (bylines); inferred (reading)]

Author order below comes from Crossref, plus the JMLR page for the 2006 paper. The CV writes every entry as "with X", so the CV hides author order and marks no student co-authors.

| Advisee | Student-first papers (non-alphabetical) | Burer-first or alphabetical papers |
|---|---|---|
| Yi Zhang | "Ensemble Pruning Via Semi-definite Programming", *JMLR* 7(48):1315–1338, 2006 (Zhang, Burer, Street); "Sharing Classifiers among Ensembles from Related Problem Domains", ICDM 2005, DOI 10.1109/icdm.2005.131 (Zhang, Street, Burer) | — |
| Changhui Choi | "A semidefinite programming approach to the hypergraph minimum bisection problem", *Optimization* 60(3), 2011, DOI 10.1080/02331930903233744 | "Computational enhancements in low-rank semidefinite programming", *OMS* 21(3), 2006, DOI 10.1080/10556780500286582 |
| Jieqiu Chen | "Globally solving nonconvex quadratic programming problems via completely positive programming", *MPC* 4(1), 2012 (online Nov 2011), DOI 10.1007/s12532-011-0033-9; "A first-order smoothing technique for a class of large-scale linear programs", *SIOPT* 24(2), 2014, DOI 10.1137/110854400 | "A p-cone sequential relaxation procedure for 0-1 integer programs", *OMS* 24(4), 2009, DOI 10.1080/10556780903057341; "Relaxing the optimality conditions of box QP", *COAP* 48, 2011 (online Jul 2009), DOI 10.1007/s10589-009-9273-2 |
| Hongbo Dong | only with Anstreicher, without Burer: DOI 10.1007/s10107-011-0485-8 | "Separation and relaxation for cones of quadratic forms", *Math. Program.* 137(1), 2013, DOI 10.1007/s10107-011-0495-6; "Representing quadratically constrained quadratic programs as generalized copositive programs", *ORL* 40(3), 2012, DOI 10.1016/j.orl.2012.02.001 |
| Boshi Yang | "A two-variable approach to the two-trust-region subproblem", *SIOPT* 26(1), 2016, DOI 10.1137/130945880; "Quadratic programs with hollows" (Yang, Anstreicher, Burer), DOI 10.1007/s10107-017-1157-0; "Convex Hulls in Quadratic Space", *Encyclopedia of Optimization* (online 31 Oct 2023), DOI 10.1007/978-3-030-54621-2_892-1 | "The trust region subproblem with non-intersecting linear constraints", *Math. Program.* 149, 2015 (online Feb 2014), DOI 10.1007/s10107-014-0749-1 |
| Guanglin Xu | "Robust sensitivity analysis of the optimal value of linear programming", *OMS* 32(6), 2017, DOI 10.1080/10556788.2016.1256400; "A branch-and-bound algorithm for instrumental variable quantile regression", *MPC* 9, 2017, DOI 10.1007/s12532-017-0117-2; "A copositive approach for two-stage adjustable robust optimization with uncertain right-hand sides", *COAP* 70, 2018, DOI 10.1007/s10589-017-9974-x; "A data-driven distributionally robust bound on the expected optimal value of uncertain mixed 0-1 linear programming", *CMS* 15, 2018, DOI 10.1007/s10287-018-0298-9 | — |
| Kyungchan Park | — | DOI 10.1007/s10898-021-01046-7 (Anstreicher, Burer, Park); "A strengthened SDP relaxation for quadratic optimization over the Stiefel manifold", *JOTA* 202, 2024 (online Mar 2023), DOI 10.1007/s10957-023-02168-6 (Burer, Park) |
| Yilin Zhu | "An extended validity domain for constraint learning", *INFORMS J. Comput.* (online 27 Jan 2026), DOI 10.1287/ijoc.2024.0815 | "Optimization over trained neural networks: going large with gradient-based algorithms", CPAIOR 2026, LNCS, DOI 10.1007/978-3-032-27242-3_35 (Tong, Zhu, Serra, Burer: Burer last) |
| Visitor A. Eltved | "Strengthened SDP relaxation for an extended trust region subproblem with an application to optimal power flow", *Math. Program.* 197 (online Jan 2022), DOI 10.1007/s10107-021-01737-9 | — |

What the bylines show [practice P]:
- Every advisee's surname sorts after "Burer", so a student-first byline always departs from alphabetical order.
- 6 of the 8 advisees with joint papers (Zhang, Choi, Chen, Yang, Xu, Zhu) are first author on at least one paper with Burer. Dong is first author only on his paper with Anstreicher, and Park on none.
- For 3 advisees the order flips over time, from Burer-first to student-first: Choi (2006 → 2011), Chen (2009 → 2011/2014) and Yang (2014 → 2016–2023). Xu and Zhu are first author from their first paper on.

[inferred] The default is alphabetical order, and the student goes first when the student led the paper. No stated policy was found. An alternative explanation for Zhang is the venues: JMLR and ICDM use contribution order.

**Thanks in the acknowledgements versus co-authorship, in both directions** [observed S; practice P]:
- Visitor Gusmeroli's paper: "Part of this work has been carried out during a research stay of the first author at the University of Iowa hosted by Sam Burer. The authors would like to thank Sam Burer for discussions and suggestions that improved the results significantly." (Gusmeroli and Wiegele, "EXPEDIS: An exact penalty method over discrete sets", arXiv:1912.09739v4, Acknowledgments; *Discrete Optimization* 44, 2022, DOI 10.1016/j.disopt.2021.100622.)
- Burer's own sole-author paper thanks Anstreicher for "an important observation" (§4.1).
- [inferred] Suggestions, even ones that improve a paper "significantly", earn thanks rather than authorship.

**Credit in talks** [stated P]. The 2021 INFORMS Optimization Society plenary (31 Mar 2021) opens with: "i want to first thank my co-authors this is joint work with kurt and striker at the university of iowa anders alved at t dtu in copenhagen and gyeongcheng park who's a phd student at the university of iowa so he's a great co-authors and i i want to acknowledge their contributions this this talk definitely would not be possible without them" (ASR; = Kurt Anstreicher, Anders Eltved, Kyungchan Park). Later: "this is where where anders and i really started to to try to derive something new" (ASR, [45:18]).

### 4.4 The advisor packages and keeps the code [practice P]

Checked through the GitHub API on 2026-10-10.

- **QuadProgBB** (the code of Chen and Burer, MPC 2012): `github.com/sburer/QuadProgBB`, created 2014-01-20, four years after Chen graduated. Contributors: `sburer` 29 commits, `jieqchen` 3. Last push 2016-07-08.
- **ttrs** (created 2016-05) and **ttrsn2** (created 2024-06): the README reads "Software and scripts to accompany the paper "A Two-Variable Approach to the Two-Trust-Region Subproblem", Boshi Yang and Samuel Burer". Only `sburer` commits.
- **extvdom** (Zhu and Burer, IJOC 2026): the repository sits under the student's account, `yillzhu/extvdom`.
  - The first commits are Burer's: "Initial commit" (2024-06-10), "Add files from spring-2024. Rename some files and directories", "Remove section_6_avocado.R", "Some tweaks to README.md", "Update for new table in paper" (2024-06-13).
  - The student made the 2025 updates. Commit authors in the history: Burer 7 (as "Samuel Burer" and "sburer"), Zhu 12 (as "Yilin Zhu" and "yzhu139").
  - The journal snapshot `INFORMSJoC/2024.0815` (DOI 10.1287/ijoc.2024.0815.cd) says: "This code is being developed on an on-going basis at https://github.com/yillzhu/extvdom."
- [inferred] He packages the reproducibility artifacts of student papers himself, either at submission (extvdom, June 2024, the week of the arXiv posting) or years later (QuadProgBB 2014, ttrs 2016). From 2024 the code lives in the student's account, with him committing.
- **The only written "onboarding" documents in his public footprint are for AI assistants.** No lab guide, group page or student onboarding document exists on his homepage, in its site repository (blog posts, course material, `aicourse`, `papers`), or on his GitHub. [practice P]
  - `submodular-tests/.github/copilot-instructions.md` ("Add Github Copilot instructions", Samuel Burer, 2025-12-12) includes: "Numerical tolerances (`tol_general`, `tol_rel_gap`, `tol_mosek`) - modify here to adjust precision across all solvers"; "**Reproducibility**: Default is seeded (`reproducible=True`)."; and "Check `M.getProblemStatus() == 'PrimalAndDualFeasible'` before extracting solutions."
  - `sdplr/CLAUDE.md` (added 2026-03-23): "Do not attempt to normalize to pure 0-based indexing without first building a comprehensive test suite — a single missed conversion produces silent wrong answers in the numerics."
- **Who writes the code, 2025–26.** The acknowledgement of arXiv:2609.32017v1 (Burer and Anstreicher, 25 Sep 2026) reads: "The AI assistants Claude (Anthropic) and Codex (OpenAI) were used to write the code for the computational experiments and for light editing of the text." [stated P] [inferred] In the 2005–2017 theses the students wrote and ran the experiments (§4.5). In his 2025–26 papers with a senior colleague, the code is written with AI assistants. I found nothing on whether this changes what his current students do.

### 4.5 Computational habits in the student theses [practice S: student-authored records of group practice]

- Chen 2010, p. 51: "The SOCPs were solved using MOSEK 5.0, and the LPs were solved using both CPLEX 9.0 and MOSEK 5.0. Pre-solving was turned off for all solvers, and computations were performed under the Linux operating system with a single 2.8 GHz AMD Opteron processor and 4 GB of RAM."
- Xu 2017, pp. 74–75: "We implement our tests in Python (version 3.5.2) with Mosek (version 8.0.0.28 beta, limited to 1 thread) as our convex-optimization solver. All of Mosek's settings are set at their defaults, and computations are conducted on a Macintosh OS X El Capitan system with a quad-core 3.20GHz Intel Core i5 CPU and 8 GB RAM."
- Park 2023, p. 56: "All experiments were coded in MATLAB (version 9.14.0.2206163 64-bit, `R2023a` February 22), and all SDP relaxations were solved with SeDuMi (version 1.30 20100405)." On p. 79 the setup is MOSEK 9.3.10 and Manopt 7.0 on "a single-core Xeon Gold 6330 running at 2.0 GHz with 16 GB of memory".
- The habits these share: exact solver versions and full hardware are reported; comparisons are controlled (presolve off for all solvers, a single thread, default settings); everything runs on one modest machine.
- [inferred] These are group norms that persist across students from 2010 to 2023, and they match the "reproduces every computational claim" READMEs of his own 2025–26 code (see 03). He never states them as rules for students; journal norms may also explain part of them.

### 4.6 The toolchain students inherit [practice S/P]

Case-insensitive term counts in the extracted thesis texts:

| Thesis | Term counts |
|---|---|
| Chen 2010 | BARON 29, MOSEK 18, CPLEX 14, MATLAB 9, QuadProgBB 7, SeDuMi 4 |
| Dong 2011 | SeDuMi 4, YALMIP 3, MATLAB 3, BARON 2 |
| Xu 2017 | MOSEK 8, MATLAB 6, YALMIP 3 (plus Python in one chapter) |
| Park 2023 | MOSEK 6, YALMIP 5, Gurobi 4, BARON 3, MATLAB 3, SeDuMi 1 |
| Yang 2015 | none (a theory thesis) |

- His own stated preference: "From the software point of view, I used YALMIP---which always makes my optimization life easier." (Blog post "YALMIP: Making Optimization Easier Since 2004", 24 Sep 2015.) [stated P]
- Chen was taught "how to use SeDuMi". [observed S]
- [inferred] The kit passed on from about 2005 to 2023: MATLAB with YALMIP for modelling, SeDuMi and later MOSEK for conic problems, CPLEX and later Gurobi for MILP/QP, and BARON as the global-solver benchmark to beat. Python enters with Xu (2017). For the 2016 competition he chose "all open-source tools such as R, Cbc, Julia, and JuMP" (blog).

### 4.7 Sending students outward [practice P/S; observed S]

- **External committee members from the student's subfield**: Takeda on Yang's committee (2015), Zuluaga on Xu's (2017). Xu says Zuluaga invited him to present at the COR@L Seminar.
- **Outside experts named in the theses**:
  - Dong communicated with Peña (CMU) and Laurent (CWI), and met Parrilo at an Oberwolfach seminar (May 2010).
  - Chen thanks "Dr. Miguel Anjos at the University of Waterloo for being supportive on my career". Anjos is an earlier Burer co-author (06). Chen also thanks Krokhmal "for his short-term mentorship that inspired my interests in second-order cone programming".
  - [inferred] Students are put in touch with outside experts in their subarea. No source says who arranged these contacts.
- **Reciprocity**: he sat on 10 external PhD committees (§1.2), several for students of researchers in his own area.

### 4.8 Papers that outlive the PhD [practice P]

- **Publication dates after graduation.**
  - Choi (graduated Spring 2007): *Optimization* paper issued 2011.
  - Chen (Summer 2010): *SIOPT* paper, 2014.
  - Yang (Summer 2015): *Math. Program.* "hollows" paper online May 2017; encyclopedia chapter online Oct 2023; `ttrsn2` repository 2024.
  - Xu (Summer 2017): *COAP* online Dec 2017; *CMS* 2018.
  - Caveat: I did not check submission dates, so most of these lags may be review time. The exception is the 2023 encyclopedia chapter with Yang, which is new joint work eight years after his PhD.
- [inferred] Advisor and former student keep finishing and maintaining joint work after the student leaves.

### 4.9 Hosting visitors and what came of each visit [practice P; observed S]

| Visitor | Dates (CV) | Outcome |
|---|---|---|
| Mirjam Dür (Groningen) | June 2007 | Burer, Anstreicher and Dür, "The difference between 5×5 doubly nonnegative and completely positive matrices", *Linear Algebra Appl.* 431:1539–1552, 2009, DOI 10.1016/j.laa.2009.05.021. The 5×5 doubly-nonnegative versus completely-positive question continues in student Dong's separation work: his thesis abstract (pp. iv–v) says he will "prove some new results in low dimensions of 5 × 5 matrices". The continuity is [inferred] |
| Peter J.C. Dickinson (Groningen) | March 2012 | No joint paper on the CV |
| Nicolò Gusmeroli (Klagenfurt) | April–May 2019 | Burer is thanked in EXPEDIS (§4.3); not a co-author |
| Anders Eltved (DTU) | Sep 2019 – Jan 2020 | Joint paper with the visiting student as **first author**. The acknowledgement reads: "The authors acknowledge the support of their respective universities, which allowed the first author to visit the second author in 2019-20, when this research was initiated." (arXiv:2009.12704v2.) The paper connects the visitor's application area (optimal power flow) with Burer's SOC-RLT cut machinery for trust-region problems |

[inferred] A visiting PhD student is treated like a home student: the visitor gets a problem where the visitor's application meets his tools, and leads the paper.

### 4.10 Teaching as part of mentoring [stated P; observed S; practice P]

- **A rule he teaches.** In two 2015 teaching videos for his R course he gives "one key Rule": "you should use relative paths not absolute paths always use relative paths inside your project folders that's because if you send it to somebody else and you use absolute paths they may not have those paths on their computer" (ASR; "Sharing RStudio Projects", 8 Feb 2015).
- **Tutorials for the wider student community** (CV; repository README):
  - IPCO 2019 Summer School tutorial, "An Introduction to Semidefinite Programming for Combinatorial Optimization". The README's abstract ends: "Finally, we'll explore the boundary of current research, especially in the area of mixed-integer nonlinear programming."
  - "A Gentle, Geometric Introduction to Copositive Optimization" (invited tutorial, Singapore University of Technology and Design, Oct 2014), later published as *Math. Program.* paper DOI 10.1007/s10107-015-0888-z (sole author, per Crossref).
  - An INFORMS International tutorial (2007), and a PEARC 2019 tutorial, "Python or R or Both: Tools for Your Data Analytics Workflow".
- **Teaching recognition** (CV): President and Provost Award for Teaching Excellence (2022), Collegiate Teaching Award (2020), Innovations in Teaching Award for Data Programming in R (2017), and others. The press items name awards and his master's-program building but quote no students (Iowa Now, 10 Mar 2022; Tippie, 22 Feb 2022).
- **What students say about teaching**: Chen ("most effective teacher"), Xu ("showed me how to be a rigorous and effective teacher") and Richmond ("taught me to love operations research").
- [inferred] For his PhD students, teaching is part of the training, not a separate duty.

---

## 5. Tacit knowledge: what his students know that the papers never say

Each item gives the claim, the source and the label. Confidence reflects the number and independence of sources.

| # | Tacit item | Evidence | Label | Confidence |
|---|---|---|---|---|
| K1 | **Break a hard problem into easier pieces, and prove what you can in small dimension first.** | According to Chen (2010, p. iii): Burer taught "breaking down hard math problems into easier ones". His own words (2021 plenary, ASR): "now this conjecture again you know it's for dimension two so it seems small but we're just trying to prove uh what we can in small dimensions to give us an idea of what the how strong these inequalities are and how valuable they could be in computation". In practice: "Case m = 2 Theorem" (Kurt-Fest, 2023) and the n = 2 convex-hull results discussed in the 2021 plenary | [observed S] + [stated P, ASR] + [practice P] | medium-high: three independent kinds of source |
| K2 | **Solver craft**: how to set up an SDP in YALMIP and solve it with SeDuMi or MOSEK, with BARON as the benchmark | Chen ("how to use SeDuMi"); toolchain counts (§4.6); his 2015 YALMIP post | [observed S], [practice S], [stated P] | medium |
| K3 | **Fair computational comparisons**: presolve off, one thread, default settings, versions and hardware stated | Chen p. 51, Xu pp. 74–75, Park pp. 56 and 79 | [practice S]; never stated as a rule | medium (could partly be journal norms) |
| K4 | **He edits your prose** down to the grammar, and expects precise writing | Chen ("corrected the grammar errors in my thesis"); Xu ("write precisely") | [observed S] | medium |
| K5 | **Talks are coached**, by him and by Anstreicher | Chen ("how to make a research presentation"); Xu ("present clearly"; Anstreicher's "warm encouragement to my presentation") | [observed S] | medium |
| K6 | **When stuck, see Kurt** | Yang ("big rescues when my research got stuck"); co-advising (§4.1) | [observed S] + [practice P] | low-medium: one explicit statement |
| K7 | **Learning to teach is part of the PhD** | Xu; Chen; Richmond; Yang's eight semesters as a student or TA in mathematics | [observed S] | medium |
| K8 | **Code is released with the paper, and he will package it** | QuadProgBB, ttrs/ttrsn2, extvdom (§4.4) | [practice P] | medium-high |
| K9 | **Credit rules**: you go first on a paper you led; suggestions get thanks, not authorship | Bylines (§4.3); EXPEDIS and the 2023 acknowledgements | [practice P] + [inferred] | low-medium: no stated policy |
| K10 | **Prototype fast, report a number, let the advisor set the target** | His own 2000 e-mails, presented as "The Advisor-Advisee Relationship" (§2) | [stated P] about his own studentship. Transfer to his students is [inferred] and unevidenced | low |

Partly distillable (framework §八): K1–K7 rest on student recollections (medium confidence). Not distillable from public material: meeting rhythm, how he gives feedback on drafts, how he chooses or hands out problems, and how he handles a stalled student.

---

## 6. Values he states about his closest collaborator [stated, S: a news quotation]

Tippie College of Business, "Kurt Anstreicher honored with Board of Regents Award for Faculty Excellence", 30 Apr 2020:

> "Throughout Kurt’s research, you can see a deep interest in the mathematics of optimization, and he always strives to the answer the important practical questions: are we really solving the problem we care about; are we using expensive computing resources wisely; what is the next obstacle?" … "Kurt also believes that the algorithms need to be good, not just useful, i.e., they need to be well researched and their behavior should be transparent to their users. These are guiding principles that we need now more than ever."

("strives to the answer" is in the original.)

[inferred] These are the stated values of the two-person group a student joins. "we need now more than ever" signals that Burer endorses them, not merely reports them. They feed layer 1 (taste: "are we really solving the problem we care about") and layer 5 (results judgment: "transparent to their users").

---

## 7. Era and resource context (framework §七)

| Period | His position and resources | Students and visitors | Computing (from the theses) |
|---|---|---|---|
| 1997–2001 | PhD student, Georgia Tech (ACO). Advisor Monteiro, plus a Rice co-author (Y. Zhang) | — | C code; first-order methods (2023 slides) |
| 2001–2012 | Assistant, then associate professor, Management Sciences (a business school). NSF collaborative grant (CV "2000-05"; NSF record 2002–06 per 06) and NSF CAREER 0545514 (2006–12, $400,000), which supported Dong's thesis research. Visiting position at CMU (Jan–May 2007) | Zhang (2006, co-advised), Choi (2007), Chen (2010), Dong (2011, co-advised); visitor Dür (2007); postdoc Cho (2009–10) | Single-machine Linux: 2.8 GHz Opteron with 4 GB RAM (Chen); a 2.40 GHz Linux machine (Dong) |
| 2012–2020 | Full professor. **No external grant on the CV after 2012.** Faculty director of the part-time (2014–19) and full-time (2018–20) Business Analytics master's programs. The department became Business Analytics in April 2019 | Yang (2015), Richmond (2016, co-supervised), Xu (2017); visitors Dickinson (2012), Gusmeroli and Eltved (2019–20) | Windows desktop, i3 with 4 GB RAM (Xu); Mac, i5 with 8 GB RAM (Xu) |
| 2020–2026 | Chaired professor; DGS of the doctoral program (2023–25); Chair/DEO (2025–). Anstreicher retired in 2023 and still co-authors. AI coding assistants from Dec 2025 | Park (2023, co-advised), Zhu (expected 2026, Mathematics) | Windows 11 desktop, i7 with 16 GB; single-core Xeon node with 16 GB (Park) |

- **Group size.** About 9 doctoral advisees with some formal role in 25 years. Graduations fell in 2006, 2007, 2010, 2011, 2015, 2016, 2017, 2023 and an expected 2026. Students' start dates were not found, so the overlap is unknown. [practice P; inferred]
- **Funding after 2012** [inferred]. Yang's account of "eight semesters with Professor David Stewart. Either as a student or a teaching assistant" fits, but does not prove, support through teaching assistantships once the CAREER grant ended.
- **Transfer** (framework §七).
  - Transfers readily: one-on-one supervision with a co-advisor colleague, small-dimension theory first (K1), single-machine experiments.
  - Was resource-bound: CAREER-funded research support (2006–12).
  - Is era-bound: the MATLAB/SeDuMi stack (today Python with MOSEK or Gurobi, as in his 2025–26 code), and the 2025–26 AI-assisted coding.

---

## 8. Failures, abandoned directions and things that did not happen

- **Lines that ended with a student.**
  - Copositive approaches to robust and distributionally robust optimization: the last joint papers with Xu appeared in 2018. 06 notes the line ends when Xu graduates; DRO returns in 2025–26 with other collaborators (06).
  - The global QP branch-and-bound code QuadProgBB built with Chen: last push 2016-07-08, not continued. 06 also lists the 2012 exit from B&B codes.
  - [practice P; inferred]
- **The counter-case**: a student's line that outlived the student. The trust-region line Yang worked on continued with Eltved (2020), as a sole-author paper (2023) and with Anstreicher (2026) (06, T5). [practice P]
- **Visits without a joint paper**: Dickinson (2012) and Gusmeroli (2019, who thanks Burer instead). [practice P]
- **Errors found by other groups' students.**
  - The correction to Burer and Ye, "Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs" (*Math. Program.*, original DOI 10.1007/s10107-019-01367-2; correction DOI 10.1007/s10107-021-01684-5, online 8 Jul 2021; both checked in Crossref). According to 06-trajectory, it thanks Prof. Fatma Kılınç-Karzan and Mr. Alex Wang of Carnegie Mellon University for pointing out the error. I did **not** re-read the correction text: Springer redirected to an authorization page.
  - The CV shows that Burer sat on Alex Wang's CMU PhD committee in Summer 2022 [practice P]. [inferred] Being corrected by a student and later examining that student's thesis is consistent with treating such corrections as normal scholarly exchange.
- **Not found**: any rejected paper involving a student, any student who left the program, any falling-out, and any critical student account. See Gaps.

---

## 9. Where these findings go in the seven layers

| Layer | Findings |
|---|---|
| L1 Taste | §6 ("are we really solving the problem we care about"; "good, not just useful") |
| L2 Topic choice | §3 on topic origin (continuation versus student interest); §4.9 (visitor's application meets his tools) |
| L3 Idea generation | K1 (decompose; small dimension first); §2 ("can't hurt to try") |
| L4 Experiment and execution | §4.4–4.6; K2, K3, K8 |
| L5 Result judgment | §6 ("transparent to their users"); §8 (handling of corrections) |
| L6 Expression | K4, K5; §4.3 (credit in talks) |
| L7 Research organization | §1, §4.1–4.2, §4.7–4.10, §7 |

---

## Contradictions (kept, not reconciled)

1. **Richmond's advisor of record.** The thesis title page lists "Thesis Supervisors: Professor Pavlo Krokhmal / Professor Samuel Burer", and IRO lists both as primary advisors. MGP lists Burer as advisor 2. The CV lists Richmond only under "Ph.D. Committee" (2016 Fall). Richmond's acknowledgements call Krokhmal "my advisor" and list Burer among the "outstanding professors who taught me to love operations research".
2. **Yi Zhang's advisor of record.** MGP lists Burer as advisor 2 (advisor 1 Street). The CV lists Zhang only under "Ph.D. Committee" (2006 Summer). The JMLR paper's byline is Zhang, Burer, Street.
3. **Changhui Choi.** The CV lists him as a PhD advisee (Spring 2007); MGP does not list him at all.
4. **Park's graduation term.** The CV says "2023 Spring"; the thesis title page says "August 2023"; IRO says "Summer 2023".
5. **Visitor dates.** 06-trajectory says "The CV gives no dates for the visitors". Read in table mode, the CV does give them (June 2007; March 2012; April–May 2019; September 2019 to January 2020). Layout-mode text extraction misaligns that table, which is the likely cause.
6. **Teaching award year.** The CV and Iowa Now (10 Mar 2022) say 2022; Tippie news (22 Feb 2022) calls it "the 2021 President and Provost Award for Teaching Excellence".
7. **Title of CV item [J18].** The CV says "A Two-Variable Analysis of the Two-Trust-Region Subproblem"; the published title (Crossref; the ttrs README) is "A Two-Variable Approach to the Two-Trust-Region Subproblem".
8. **Who leads.** The model he presents (§2) is a fast-turnaround, advisor-sets-the-target relationship. Xu credits him with "encouraged me to explore research topics that I am interested in". These are not strictly incompatible, but they describe different degrees of advisor direction, and no source shows which mode he uses with whom.

## Gaps

- **No student blog posts, memorial pieces, Festschrift contributions about Burer, lab guide, group page or onboarding document** were found. I checked the homepage, its site repository, the GitHub account and one WebSearch for recollections, which returned only award news. The Kurt-Fest session slides (2023) are the only tribute-type item, and they honor Anstreicher, not Burer.
- **No first-person statement by Burer on how he advises PhD students** was found. The only first-person material is about *being* advised (§2), the CAREER education plan, a teaching-video rule and the 2016 team blog post.
- **Burer's own PhD thesis acknowledgements** (Georgia Tech 2001): the repository page returned HTTP 403 in this run (06 got HTTP 401 for the PDF). Not read.
- **Dissertations not read**: Yi Zhang (2006) and Changhui Choi (2007), not found in IRO; Yilin Zhu (expected 2026), not yet deposited.
- **External-committee theses not read**: Bettiol (HAL tel-03227417; the full text and record page were blocked by a bot check, "Access Denied"), and Wang, Kuang, Mittal, Yan, Michalka, Saxena, Hoda, Liang and Sujanani (no Crossref or OpenAlex dissertation records found; not pursued further).
- **No source** on meeting frequency, response times, how problems are assigned, how drafts are reviewed, students' start dates or time-to-degree, or how students were funded after 2012.
- **No critical or negative account** by any student or collaborator. The acknowledgement genre is uniformly positive, so this is a known blind spot, not evidence of its absence.
- **The 2021 Burer–Ye correction text** was not re-read (Springer authorization redirect). Its thanks to Kılınç-Karzan and Wang is taken from 06-trajectory.
- **Not read**: his *Optima* co-editor columns (2010–18).
- **Not verified**: whether the CAREER K-12 and underrepresented-group outreach took place; the postdoc paper [J29] beyond its CV entry.
- **Not used**: a WebSearch summary said Anstreicher received a 2024 career research award and is now emeritus. I did not verify this.

## Sources

**Primary**

1. S. Burer, Curriculum vitae, updated 12 Feb 2026. https://sburer.github.io/files/cv.pdf (read in layout, raw and table modes) — primary
2. S. Burer, homepage (last updated 2026-03-20) and its site repository. https://sburer.github.io/ ; github.com/sburer/sburer.github.io — primary
3. S. Burer, "Two Decades of Low-Rank Optimization", University of Iowa talk, March 2023. YouTube wSauUgRIQDg (ASR transcript in `references/sources/talks/`) — primary
4. S. Burer and R.D.C. Monteiro, "Two Decades of Low-Rank Optimization", slides, SIAM Conference on Optimization, Seattle, 2 June 2023. https://github.com/sburer/2023-06_SIOPT (test-of-time.pdf; slides 30–35 viewed as images) — primary
5. S. Burer, "On Nonconvex Quadratic Programming with Ball Constraints" ("Kurt-Fest!"), slides, Seattle, 2 June 2023. https://github.com/sburer/2023-06_SIOPT (kurt-fest.pdf) — primary
6. S. Burer, "Convexification for Non-Convex Mixed-Integer Quadratic Programming", plenary, INFORMS Optimization Society conference (virtual), 31 Mar 2021. YouTube QfZLtPz5JBY (ASR transcript) — primary
7. S. Burer, "Relative Paths and the Working Directory in R", teaching video, 8 Feb 2015. YouTube fe6GA200dks (ASR) — primary
8. S. Burer, "Sharing RStudio Projects", teaching video, 8 Feb 2015. YouTube mV9vd5urqdU (ASR) — primary
9. S. Burer, "Syngenta Crop Challenge", blog post, 11 May 2016. github.com/sburer/sburer.github.io, `_posts/2016-05-11-Syngenta-Crop-Challenge.md` — primary
10. S. Burer, "YALMIP: Making Optimization Easier Since 2004", blog post, 24 Sep 2015. Same repository, `_posts/2015-09-24-YALMIP-making-optimization-easier.md` — primary
11. NSF award 0545514, "CAREER: Computation, Theory, and Applications for Nonconvex Quadratic and Conic Optimization", PI S. Burer, 2006-06-01 to 2012-05-31. https://api.nsf.gov/services/v1/awards/0545514.json — primary
12. S. Burer, "A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints", arXiv:2303.01624v2; *Math. Program.* 211:157–179, DOI 10.1007/s10107-024-02076-1 (acknowledgements) — primary
13. S. Burer and K.M. Anstreicher, "Applications of the Lorentz positive cone in nonconvex quadratic optimization", arXiv:2609.32017v1, 25 Sep 2026 (acknowledgement) — primary
14. A. Eltved and S. Burer, "Strengthened SDP relaxation for an extended trust region subproblem with an application to optimal power flow", arXiv:2009.12704v2; *Math. Program.* 197:281–306, DOI 10.1007/s10107-021-01737-9 (acknowledgements) — primary
15. GitHub account `sburer`, via the GitHub API, 2026-10-10: repositories QuadProgBB, ttrs, ttrsn2, soctrust, ipco-2019-sdp-tutorial, BoxQP_instances, submodular-tests (`.github/copilot-instructions.md`, 2025-12-12), sdplr (`CLAUDE.md`, 2026-03-23), with contributor and commit lists — primary
16. Y. Zhu and S. Burer code: `github.com/yillzhu/extvdom` (commit history) and the `INFORMSJoC/2024.0815` README, DOI 10.1287/ijoc.2024.0815.cd — primary (record of practice)

**Secondary**

17. J. Chen, "Convex relaxations in nonconvex and applied optimization", PhD thesis, University of Iowa, 2010. DOI 10.17077/etd.xz5r3ajb — secondary (first-hand student account)
18. H. Dong, "Copositive programming: separation and relaxations", PhD thesis, University of Iowa, 2011. DOI 10.17077/etd.kzq65y36 — secondary (first-hand student account)
19. B. Yang, "A conic optimization approach to variants of the trust region subproblem", PhD thesis, University of Iowa, 2015. DOI 10.17077/etd.wvkyfp48 — secondary (first-hand student account)
20. N. Richmond, "On stochastic network design: modeling approaches and solution techniques", PhD thesis, University of Iowa, 2016. DOI 10.17077/etd.lz5powef — secondary (first-hand student account)
21. G. Xu, "Optimization under uncertainty: conic programming representations, relaxations, and approximations", PhD thesis, University of Iowa, 2017. DOI 10.17077/etd.6m2pvuum — secondary (first-hand student account)
22. K. Park, "Advances in convex relaxations for quadratic optimization: a study on conic programming relaxations including second-order-cone and semidefinite programming", PhD thesis, University of Iowa, 2023. DOI 10.25820/etd.007220 — secondary (first-hand student account)
23. Iowa Research Online (Esploro) records for items 17–22, and repository searches for Park, Choi and Zhu, 2026-10-10. https://iro.uiowa.edu — secondary (metadata)
24. Mathematics Genealogy Project, records 114747 (Burer), 108903 (Yi Zhang) and 243710 (Richmond). https://www.mathgenealogy.org/id.php?id=114747 — secondary
25. N. Gusmeroli and A. Wiegele, "EXPEDIS: An exact penalty method over discrete sets", arXiv:1912.09739v4; *Discrete Optimization* 44 (2022), DOI 10.1016/j.disopt.2021.100622 (acknowledgements) — secondary
26. Crossref metadata for the bylines in §4.3, the Dür paper (DOI 10.1016/j.laa.2009.05.021) and the Burer–Ye paper and its correction (DOIs 10.1007/s10107-019-01367-2, 10.1007/s10107-021-01684-5); the JMLR page https://www.jmlr.org/papers/v7/zhang06a.html — secondary (bibliographic)
27. T. Snee, "Data mining for better farming", Iowa Now, 31 Mar 2016. https://now.uiowa.edu/news/2016/03/data-mining-better-farming — secondary
28. Tippie College of Business, "Kurt Anstreicher honored with Board of Regents Award for Faculty Excellence", 30 Apr 2020. https://tippie.uiowa.edu/news/2020/04/kurt-anstreicher-honored-board-regents-award-faculty-excellence — secondary (quotes Burer)
29. Tippie College of Business, "Burer receives University President and Provost Teaching Award, faculty award", 22 Feb 2022. https://tippie.uiowa.edu/node/4236 — secondary
30. Office of Strategic Communication, "Four instructors earn UI's highest teaching honor", Iowa Now, 10 Mar 2022. https://now.uiowa.edu/node/53151 — secondary
31. Tippie College of Business, "Burer honored for long-term impact of paper", 31 Jan 2023. https://tippie.uiowa.edu/news/2023/01/burer-honored-long-term-impact-paper — secondary (no mentorship content)
32. Office of Strategic Communication, "Burer receives top INFORMS computing society honor", Iowa Now, 19 Aug 2020. https://now.uiowa.edu/news/2020/08/burer-receives-top-informs-computing-society-honor — secondary (no mentorship content)
33. Georgia Tech ARC news, "SIAM Activity Group on Optimization Test of Time Award for Prof. Rentao Monteiro", 18 Feb 2023. https://www.tlwarc.hg.gatech.edu/node/665928 — secondary (no mentorship content)
34. Iowa Now, "Anstreicher named senior associate dean of Tippie College of Business", 29 May 2012. https://now.uiowa.edu/node/21196 — secondary (no mentorship content)
35. HAL record tel-03227417: E. Bettiol, "Column generation methods for quadratic mixed binary programming", thesis, 2019. https://theses.hal.science/tel-03227417 — secondary (metadata only; full text blocked)

Leads, not counted as sources: `06-trajectory.md` (sibling note, same run), used for the 2021 correction text and the lineage context; and the result lists of the 2 WebSearch queries, used only to locate items 28–30 and 34.
