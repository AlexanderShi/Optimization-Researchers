# 02 · Stated methodology (what Grossmann SAID research should be)

- **Researcher:** Ignacio E. Grossmann (born 1949, Mexico City). Rudolph R. and Florence Dean University Professor of Chemical Engineering, Carnegie Mellon University (CMU), where he has been since 1979. He co-founded the Center for Advanced Process Decision-making (CAPD) in 1985 and later directed it. PhD from Imperial College London (1977), advised by Roger Sargent.
- **Dimension:** Agent 02, stated methodology: what he *claims* research should be. Whether he practises it is left to 03 (process evidence).
- **Research date:** 2026-10-10
- **Sources consulted:** 42 (numbered S1–S42 in the Sources section).
  - 26 primary sources, read: his own or co-authored texts, two speeches, one interview, one short video, lecture abstracts, institutional pages he chaired, and his 2007 publication list.
  - 8 secondary sources, read.
  - 8 sources attempted but not readable (paywall, HTTP 403, login, or YouTube rate limit).
  - WebSearch: 2 calls. Everything else came from curl, yt-dlp, the OpenAlex and Crossref APIs, and one WebFetch.
  - No user-supplied material existed. When this run started, `references/sources/papers|talks|essays|software` held only `.gitkeep` files. (The interview transcript now in `talks/` was saved during this run by agent 04.) `private/` was not opened.

**What the evidence base is, and what it is not.** Grossmann has no public essay, blog or lab guide on "how I do research". His stated method has to be read from seven kinds of source:

1. A run of agenda-setting "perspective / challenges" essays: 2000 (with Westerberg), 2004, 2005, 2012, and 2019 (with Harjunkoski).
2. Co-authored retrospectives and reviews (2004 ×2, 2014, 2017), and a solver benchmark (2019).
3. Two speeches in Spanish:
   - the written text of his 2019 honorary-doctorate address at the Universidad de Alicante;
   - his 2025 lecture and Q&A at the Spanish Royal Academy of Sciences (from automatic captions).
4. A 1 h 42 min oral-history interview (YouTube series *Subject to*, uploaded 2024-02-08; automatic captions).
5. A 5-minute 2014 CMU profile video.
6. Lecture abstracts (2017 Hougen Lectures, 2025 Academy talk).
7. Institutional pages he chaired or that present him (minlp.org; CMU bio).

Most of this material is about *what kind of research PSE (process systems engineering) should do* and *how optimization models should be built*. There is little on writing papers, and little on how he advises individual students. The file records what was said and marks the thin layers as thin.

**Tags.**
- **[stated]**: he said or wrote it alone (single-author text, his own speech, his own answer in an interview).
- **[stated-joint]**: it appears in a text he co-authored, so his individual voice cannot be separated. Where a co-authored text names him in the third person, the passage is marked as his.
- **[stated-inst]**: institutional page of a project he chaired or of his department. The author is not named.
- **[observed]**: other people said it about him.
- **[inferred]**: this agent's reading.
- **P / S**: primary / secondary.

**Citation conventions.**
- **Page numbers.**
  - *egon.cheme.cmu.edu preprints*: "p. N" is the page of the PDF file, which can differ from the journal pagination.
  - *2005 EWO article (S5) and 2019 EWO preface (S18)*: printed journal pages, because the copies read are the published versions.
  - *Alicante speech (S19)*: "p. N" is the page of the 21-page RUA PDF.
- **Video timestamps.** `[h:mm:ss]` is the start of the caption block in which the quote begins. A "+" means the quote runs into the next block. Block lengths: about 30 s for the interview, about 20 s for the 2014 video, about 60 s for the 2025 lecture. The interview file that agent 04 saved in `talks/` groups the blocks differently, so its timestamps can differ by up to about 30 s.
- **Caption-derived quotes.** They are copied verbatim from YouTube automatic speech recognition, recognition errors included. Glosses follow in parentheses ("ASR: …").
- **Spanish quotes.** They are verbatim. They are followed by this agent's translation, marked "tr.".
- **Verification.** Every quote in this file was checked by script against the downloaded text or caption file, after normalising whitespace. 155 of 157 strings matched. The two exceptions:
  - one quote crosses a page break and is cited as such (pp. 11–12);
  - one paraphrase test string was not used.

---

## A. Source corpus and its era / resource context

| # | Source | Date | Voice | Era / resource context |
|---|---|---|---|---|
| S1 | Grossmann & Westerberg, "Research Challenges in Process Systems Engineering", *AIChE J.* 46(9):1700–1703 | Sep 2000 | joint, 2 authors [stated-joint] P | Written while Grossmann was CMU department head (1994–2002). An AIChE Journal "perspective" written for a chemical-engineering-wide audience. |
| S2 | Grossmann, "Challenges in the new millennium: product discovery and design, enterprise and supply chain optimization, global life cycle assessment", *Comput. Chem. Eng.* 29(1):29–39 | Dec 2004 (Crossref). His 2007 list gives 2005. The text is a PSE2003 keynote. | single [stated] P | Written after "eight and one half years" as department head. Also from his work on a US National Research Council committee and as AIChE J. associate editor. Written during a Fulbright senior lectureship in Spain (from the acknowledgment). |
| S3 | Biegler & Grossmann, "Retrospective on optimization", *Comput. Chem. Eng.* 28(8):1169–1192 | Jul 2004 | joint [stated-joint] P | 25th-anniversary issue. The MINLP and decomposition sections are his field, but authorship of individual sections is not marked. |
| S4 | Grossmann & Biegler, "Part II. Future perspective on optimization", *Comput. Chem. Eng.* 28(8):1193–1218 | Jul 2004 | joint [stated-joint] P | Same issue as S3. |
| S5 | Grossmann, "Enterprise-wide optimization: A new frontier in process systems engineering", *AIChE J.* 51(7):1846–1857 | Jun 2005 | single [stated] P | CAPD director period (2005–2015). Launch statement of the EWO agenda. |
| S6 | Grossmann, "Advances in mathematical programming models for enterprise-wide optimization", *Comput. Chem. Eng.* 47:2–18 | Dec 2012 | single [stated] P | Written after five years of the CAPD EWO special-interest group: 14 companies; faculty from chemical engineering, industrial engineering and operations research. |
| S7 | Grossmann & Trespalacios, "Systematic modeling of discrete-continuous optimization models through generalized disjunctive programming", *AIChE J.* 59(9):3276–3295 | 2013 | joint with his PhD student [stated-joint] P; the acknowledgment is in his voice | Methodological "how to model" paper. NSF-funded (grant OCI-0750826). |
| S8 | Grossmann, Calfa & Garcia-Herreros, "Evolution of concepts and models for quantifying resiliency and flexibility of chemical processes", *Comput. Chem. Eng.* 70:22–34 | 2014 | joint with two students [stated-joint] P | Retrospective tribute to M. Morari. It tells the story of his own early-1980s work. |
| S9 | Chen & Grossmann, "Recent developments and challenges in optimization-based process synthesis", *Annu. Rev. Chem. Biomol. Eng.* 8:249–283 | 2017 | joint, student first author [stated-joint] P | Review written in the Pyomo/GDP period. |
| S10 | Grossmann & Harjunkoski, "Process Systems Engineering: Academic and industrial perspectives", *Comput. Chem. Eng.* 126:474–484 (egon copy: "Extended paper for the 13th International Symposium on Process Systems Engineering") | 2019 | joint with an ABB researcher [stated-joint] P. The acknowledgment speaks of him by name. Section 4.1 ("Industrial Perspective") is probably Harjunkoski's voice [inferred]. | Senior period, after the CAPD directorship. Includes a survey answered by 81 PSE people. |
| S11 | Kronqvist, Bernal, Lundell & Grossmann, "A review and comparison of solvers for convex MINLP", *Optim. Eng.* 20(2):397–455 (egon preprint dated June 3, 2018) | 2018/2019 | joint, he is the senior and last author [stated-joint] P | Desktop benchmark: Xeon 3.6 GHz, 32 GB, 8 threads, 900 s limit, 366 MINLPLib instances, 15 solvers. |
| S12 | Grossmann, Caballero & Yeomans, egon preprint "Advances in Mathematical Programming for the Synthesis of Process Systems" | 1999 | joint [stated-joint] P | It is probably the preprint of their *Korean J. Chem. Eng.* 16(4):407–426 (1999) paper: that is the only three-author review by them in his 2007 publication list, though the titles differ [inferred]. |
| S13 | Grossmann & Guillén-Gosálbez, "Scope for the application of mathematical programming techniques in the synthesis and planning of sustainable processes", ch. 5 in *Design for Energy and the Environment* (FOCAPD 2009, CRC), pp. 55–76; journal version *Comput. Chem. Eng.* 34(9):1365–1376 (2010) | 2009/2010 | joint [stated-joint] P | Biofuels and sustainability period. |
| S14 | Grossmann, van den Heever & Harjunkoski, "Discrete Optimization Methods and their Role in the Integration of Planning and Scheduling", *AIChE Symp. Ser.* 98(326):150–168 (venue from his 2007 publication list) | 2002 | joint [stated-joint] P | Department-head period. |
| S15 | Grossmann, "Review of nonlinear mixed-integer and disjunctive programming techniques", *Optim. Eng.* 3(3):227–252 (egon preprint "June 2001/Rev. April 2002") | 2002 | single [stated] P | Unified survey of MINLP and GDP methods. |
| S16 | Grossmann & Ruiz, "Generalized Disjunctive Programming: A Framework for Formulation and Alternative Algorithms for MINLP Optimization", IMA Volumes in Mathematics and its Applications, pp. 93–115 | 2011/2012 | joint [stated-joint] P | IMA MINLP workshop volume. |
| S17 | Grossmann & Pardalos, Preface, JOGO special issue in memory of C. A. Floudas, *J. Glob. Optim.* 71:1013 | 2018 | joint [stated-joint] P | Evaluation of a colleague's work (taste evidence). |
| S18 | Gounaris & Grossmann, "A preface to the special issue on enterprise-wide optimization", *Optim. Eng.* 20:965–968 | 2019 | joint [stated-joint] P | Editorial written with a younger CMU colleague. |
| S19 | Honorary-doctorate address ("Discurso"), Universidad de Alicante, 28 Jan 2019 (RUA hdl 10045/91533, Spanish PDF; his speech is on pp. 9–12) | 2019 | single, his own speech [stated] P | His seventh honorary doctorate (the CEE profile, S27, says "his seventh"). Written text, read aloud. |
| S20 | *Subject to: Ignacio Grossmann*, YouTube interview series @Subjectto_. The host is addressed as "Anan[d]" in the captions; agent 04's transcript header names him Anand Subramanian (not independently checked). Uploaded 2024-02-08, 1:42:05. | late 2023 / early 2024 [inferred from a mention of a recent Thanksgiving] | single, his answers [stated] P (captions) | Reflective oral history. He had started 50% phased retirement on "September the first" (2023 [inferred]). Counts: 68 PhD and 34 MS graduates, 16 of the PhDs in academia. |
| S21 | *Ignacio Grossmann: Optimization Models and Methods*, CMU College of Engineering video, uploaded 2014-10-07, 5:09 | 2014 | single [stated] P (captions) | Recorded while CAPD director. Public-facing pitch of his research. |
| S22 | *Evolution and Future Trends in Process Systems Engineering*, Real Academia de Ciencias Exactas, Físicas y Naturales (Spain), 16 Sep 2025 (date from the YouTube description). Spanish lecture from 9:22 and audience Q&A from 1:03:20, plus an English abstract in the video description. | 2025 | single [stated] P (Spanish captions; the abstract is a written text) | Admission as foreign academician. Most recent statement found. |
| S23 | Hougen Lectures 2016–2017, University of Wisconsin–Madison: abstracts of "Role of Process Systems Engineering in Chemical Engineering" (2 May 2017) and "Recent Advances in Computational Models for the Discrete and Continuous Optimization of Industrial Process Systems" (4 May 2017) | 2017 | single, lecture abstracts [stated] P | Lecture series for a general chemical-engineering audience. |
| S24 | minlp.org, "CMU-IBM Cyber-Infrastructure for MINLP" (front page, Goals, Participants, Instructions). Grossmann is listed as "Chair", Jon Lee as "Vice-Chair"; NSF grant OCI-0750826. | undated (grant-era site, still online) | institutional [stated-inst] P | Collaborative problem-library project with IBM. |
| S25 | CMU Chemical Engineering bio page (with embedded videos and media mentions) | read 2026-10-10 | institutional [stated-inst] P | Current self-presentation. |
| S26 | "PUBLICATIONS IGNACIO E. GROSSMANN, Augus[t] 2007" (egon PDF) | 2007 | bibliography P | Used only to check venues. |

Secondary sources (S27–S34) and unreadable items (S35–S42) are listed under Sources.

---

## B. Findings by the seven layers (framework §一)

### Layer 1: Research taste (what is worth doing, what counts as good)

**T1. Worthwhile PSE research is both intellectually challenging and relevant to industry. He sets the two side by side as a standing criterion.** [stated] / [stated-joint] P. Repeated on at least 8 occasions, 2000–2025 (see C1). The most stable claim found.
- 2000 [stated-joint], S1 p. 2: "While largely driven by industrial needs, it is important to understand that PSE research also deals with fundamental theoretical issues."
- 2000 [stated-joint], S1 p. 4:
  - "there are plenty of intellectually challenging problems in PSE that are awaiting solutions from individuals with creative minds."
  - "This will be essential if chemical engineering is to remain a vibrant profession that is of relevance to industry."
- 2003/04 [stated], S2 p. 13: "Finally, we hope that this paper has shown that in PSE there are many problems that are intellectually challenging and that are relevant to industry. The important goal is to make sure that new research directions in the "new millennium" emphasize both points."
- 2012 [stated], S6 p. 16: "It is clear that the challenges are non-trivial, but the payoff is that it is highly relevant as it can greatly help to strengthen the process industry."
- 2019 [stated-joint], S18 p. 966: "From the above, it is clear that EWO deals with problems that are of great practical significance to engineering and business applications, while giving rise to very challenging mathematical programming problems that require sophisticated and elegant methodologies to tackle them."
- 2019 [stated-joint], S10 p. 16: the field should "keep Process Systems Engineering a vibrant research area that is industrially relevant."
- 2019 [stated], S19 p. 12: "Una de las satisfacciones de hacer investigación en esta área es que podemos lograr un equilibrio entre la teoría y la práctica." (tr.: "One of the satisfactions of doing research in this area is that we can strike a balance between theory and practice.")
- 2024 [stated], S20 [0:58:31]: "so on the one hand we were of course interested in the math optimization part of these problems but they were driven by the need to solve these engineering problems"

**T2. Three kinds of contribution count as original, on an equal footing: new representations or models, efficient solution methods, and software that adds capability. PSE's intellectual challenge is decision-making for engineered systems, not the discovery of natural mechanisms.** [stated-joint] P (2000), with a matching single-author self-description in 2014.
- S1 p. 2: "Developing novel representations and models that capture non-trivial features, as well as developing computationally efficient solution methods and software tools that provide new capabilities, are all considered to be original contributions in PSE."
- S1 p. 2:
  - "In contrast the intellectual challenges for PSE area are the discovery of concepts and models for the prediction of performance and for decision making for an engineered system."
  - "Again in contrast PSE research strives to create representations and models to generate reasonable alternatives, and then select from among them a solution that meets constraints and ideally optimizes an objective."
  - "Computational efficiency is also an intellectual challenge in the PSE area."
- 2014 [stated], S21:
  - [0:00:25] "The major goal of my research is to develop optimization models and methods in order to address the variety of problems in process systems engineering"
  - [0:00:43+] "So, a good part of our work is devoted to developing algorithms for solving these problems. We apply them to a variety of problems and interesting applications"

**T3. Rigour is the default value: guaranteed bounds, global optimality, guaranteed feasibility. Heuristics are accepted, but they are always labelled non-rigorous and justified by their lower cost.** [stated] / [stated-joint] P. Repeated in at least 8 sources, 1999–2025 (C4).
- 1999 [stated-joint], S12 p. 2, on simulated annealing and genetic algorithms: they "do not make any assumptions on the functions, but then they cannot guarantee rigorous solutions, at least in finite amount of time."
  - Nearly the same sentence appears in 2002 [stated-joint], S14 p. 6: they "do not make any assumptions on the functions, but cannot guarantee rigorous solutions in a finite amount of time."
- 2002 [stated], S15 p. 15, on the augmented-penalty treatment of nonconvex MINLP: "While not being rigorous, this requires much less computational effort."
  - p. 17: "This is a heuristic that works reasonably well in many problems."
  - The first sentence also appears in S3 p. 24 (2004, joint).
- 2004 [stated-joint], S4 p. 2, on stochastic global methods: "Furthermore, these methods are not rigorous, and tend to have difficulty in handling complex constrained problems. However, stochastic methods are suitable for problems where the function evaluations are cheap, and often produce good suboptimal solutions."
- 2019 [stated], S19 pp. 10–11. Sargent "me enseñó a apuntar a los más altos estándares de calidad, de rigor y de excelencia en la investigación" (tr.: "taught me to aim for the highest standards of quality, rigour and excellence in research").
- 2024 [stated], S20 [1:04:30], on his max-min-max flexibility formalism: "it is a rigorous way of handling those type of problems"
- 2025 [stated], S22 [0:39:00], on a shale-gas MINLP that took about 8.5 hours: "lo importante es podría garantizar el óptimo global" (tr.: "the important thing is [that] it could guarantee the global optimum").
- [observed] S27 p. 2: colleagues call outer approximation "the first rigorous decomposition algorithm for solving MINLPs".

**T4. Modelling and formulation are "of paramount importance". The same problem can be formulated in many ways, the choice matters, and choosing well should be made systematic instead of left to "art".** [stated] / [stated-joint] P. Repeated on at least 6 occasions, 2000–2025 (C3).
- 2000 [stated-joint], S1:
  - p. 3: "In Process Systems Engineering modeling is of paramount importance."
  - p. 2: "As in operations research, developing good problem representation for the alternatives is central to the development of PSE models."
- 2004 [stated-joint], S3 p. 3: applications "have been facilitated not only by progress in optimization algorithms, but also by the advent of modeling techniques" (the sentence goes on to cite Williams 1985, GAMS and AMPL).
- 2005 [stated], S5:
  - "The modeling challenge" is the first of his four EWO challenges (p. 1848).
  - p. 1850, on modelling nonlinearities and logic with many auxiliary binary variables: "Also, with this approach, the combinatorial structure is obscured and it is not possible to take advantage of the structure."
  - p. 1850: "For such functions and constraints, the "textbook" approach implemented in the current software is often not practical."
- 2013 [stated-joint], S7:
  - p. 1: "how one formulates a model can have a major impact in the performance and capability to find a solution. Therefore, deriving "good" formulations or finding potential improvements in existing models is commonly regarded as an art and strongly depends on the modeler skills."
  - The remedy offered, p. 2: "Unlike direct MINLP formulations, this higher level modeling framework makes the formulation process more intuitive and systematic, while retaining in the model the underlying logic structure of the problem."
- 2025 [stated], S22 [0:22:01], on GDP (generalized disjunctive programming): "se trata de capturar la lógica antes de traducirlo en forma de ecuaciones" (tr.: "it is about capturing the logic before translating it into equations").
- 2025 [stated], S22 [1:14:02]: "el modelado no es solo escribir ecuaciones, sino también entender físicamente qué es lo que está tratando uno de hacer y qué puede uno explotar de propiedades" (tr.: "modelling is not only writing equations but also understanding physically what one is trying to do and which properties one can exploit").

**T5. Physical (domain) understanding is what lets you exploit problem structure. This is PSE's edge over a pure operations-research (OR) stance.** [stated] P. Explicit in 2025; consistent statements in 2002, 2005 and 2024 (C6).
- 2025 [stated], S22 [1:11:01–1:12:03], answering whether the methodology is independent of chemical engineering:
  - "la mejor combinación es tener gente de investigación operativa que tiene la metodología de optimización y gente de ingeniería de sistemas de procesos precisamente porque entienden físicamente cuál es el problema" (tr.: "the best combination is to have operations-research people, who have the optimization methodology, and process-systems-engineering people, precisely because they understand physically what the problem is").
  - "cuando uno modela un problema, si uno tiene un conocimiento de cuál es la la física, uno puede explotar más la estructura del problema" (tr.: "when one models a problem, if one knows the physics, one can exploit the structure of the problem more").
  - On OR researchers: "la actitud de ellos más que nada suele ser a mí dame el modelo, yo no es mi problema de dónde viene, ya que está el modelo, ya me ocupo como resolverlo" (tr.: "their attitude is usually: give me the model; where it comes from is not my problem; once the model is there, I take care of solving it").
  - He links this to his observation that most nonlinear codes came from chemical engineers.
- 2005 [stated], S5 p. 1854, after a hybrid MILP/CP method solved a scheduling problem in 5 s that MILP could not solve in 10 h: "This example then shows the importance of special solution methods that effectively exploit the structure of scheduling problems."
- 2002 [stated-joint], S14 p. 10: "When choosing a decomposition method it is important to consider how to exploit the structure of the model most efficiently and also to choose a degree of decomposition that allows solution in reasonable time while still finding an optimal or near-optimal solution."
- 2024 [stated], S20 [0:59:31]. GDP exploits the logic structure: "fix your binary variables anything that doesn't apply remove it from your formulation and you end up with a reduced nonlinear optimization problem that is well defined"

**T6. Breakthroughs come from new theory combined with algorithms, not from faster computers alone.** [stated] P (2004, 2005) plus [stated-joint] (2004). Three occurrences (C11).
- 2004 [stated], S2 p. 13:
  - "there might be the temptation to think that faster and more advanced computers is all that is needed."
  - "While these developments will obviously have significant impact, the breakthroughs will come with synergy of new theories and algorithms as it has happened in the case of LP and MILP optimization (Bixby, 2002)."
- 2005 [stated], S5 p. 1850: "Capitalizing on theory developed during the last 20 years, it is now possible, using off-the-shelf LP-based branch-and-bound commercial software, to solve in a few seconds MILP instances that were unsolvable just five years ago."
- 2004 [stated-joint], S4 p. 44: "advances in scientific computing, both in hardware and software engineering, need to be harnessed to develop new optimization algorithms."

**T7. Systematic optimization beats intuition, heuristics and "engineering judgement", and finds solutions that are not obvious.** [stated] / [stated-joint] P. At least 5 occurrences (C10).
- 2014 [stated], S21 [0:03:44]: "Instead of using a heuristic schedule, that was essentially a schedule that was developed by intuition or engineering judgement, if you wish, our mathematical optimization model"
  - The result reported [0:04:00]: water trucks cut "from 14,000 to less than 1,400 trucks".
- 2014 [stated-joint], S8 p. 6: differences in dynamic resilience "may not be obvious on physical grounds and may not be suggested by heuristics."
- 2017 [stated-joint], S9 p. 1:
  - "The first synthesis techniques were evolutionary in nature (9), whereby heuristics and engineering judgement are used on an existing flowsheet to propose enhancements by adding or modifying process units one at a time. This strategy limits exploration to a neighborhood of the base case."
  - Later on the same page, with the limits stated too: "As an alternative, optimization-based strategies rigorously search through a proposed design space for the optimal configuration. Limitations here arise in our ability to define an appropriate search space, select a suitable degree of approximation, and solve the resulting optimization problems."
- 2024 [stated], S20 [0:46:30], recalling the 1980s debate with pinch-analysis advocates: "we can formulate a super structure and formulate the problem as say mix inte non programming and then systematically" (ASR: mixed-integer nonlinear programming).
- 2025 [stated], S22 [0:48:01], on an optimal water network: "ese tipo de esquema no es obvio" (tr.: "that kind of scheme is not obvious").

**T8. Choose where to work by the size of the industrial stake. Distrust shifts driven by scientific fashion.** [stated] P. Two sources, 2004 and 2017; consistent with each other.
- 2004 [stated], S2 p. 13:
  - "There are many potential and exciting possibilities in biological related research in PSE. However, industrial growth in that area is unlikely to become sufficiently large so that it should become the major focus of PSE research."
  - Also: "The electronics area has received be little attention by the PSE community despite the significant number of chemical engineers who have been hired by that industry."
- 2017 [stated], S23 (Lecture 1 abstract): "we highlight how academic research over the last decade has had a strong push towards science, largely due to emergence of areas like nanotechnology and biotechnology, which has caused some disconnect between academia and industry."

**T9. "High standards" and "excellence" are explicit values. He credits them to his mentors.** [stated] P. Stated on 2 occasions (2019, 2024), with at least 4 mentions in all. [observed] corroboration from colleagues.
- 2019, S19 pp. 10–11: Sargent taught him the "más altos estándares de calidad, de rigor y de excelencia" (see T3).
- 2024, S20 [0:42:00+], on Egon Balas: "he had very high standards and always aiming very high"
- 2024, S20:
  - [1:37:30] "especially try to keep standards of excellence"
  - [1:39:32] "please try to be passionate and try to keep the highest levels of Excellence of your work"
- [observed] S27 p. 1, four CMU colleagues: "Ignacio approaches both life and research with a great sense of high standards, dedication to his students and colleagues and caring for others."
- 2018 [stated-joint], S17, praising a colleague: Floudas's "superb academic reputation crossed the boundaries of Chemical Engineering, Optimization, Applied Mathematics and Operations Research, and Computational Chemistry and Biology." This is taste evidence: he values impact that crosses disciplines.

### Layer 2: Problem choice (where problems come from, why now)

**P1. Problems come from industry, through the consortium, more than from the literature.** [stated] P. At least 7 occasions (C2).
- 2004 [stated], S2 p. 2: "it is important to identify the major facts and trends in industry that motivate the challenges for future research in this area."
- 2017 [stated], S23 (Lecture 2 abstract): his models and algorithms are for "a variety of challenging applications in Process Systems Engineering, and that have been largely the result of collaborations with industry."
- 2019, S10 p. 17 (a joint paper's acknowledgment in his individual voice): "Ignacio Grossmann would also like to thank companies of the Center of Advanced Process Systems Engineering who have motivated our research over the years and have made it to be industrially relevant." (The text names the centre this way; elsewhere it is CAPD.)
- 2019 [stated], S19 p. 12:
  - "La mayoría de estos temas a menudo han sido motivados por las aplicaciones en la industria química" (tr.: "most of these topics have often been motivated by applications in the chemical industry").
  - "nuestra comunidad no se ha olvidado del hecho de que como ingenieros químicos también apuntamos a problemas de relevancia práctica." (tr.: "our community has not forgotten that, as chemical engineers, we also aim at problems of practical relevance.")
- 2024 [stated], S20 [1:17:01], on a CO2 transport and sequestration problem posed by TotalEnergies: "we would probably never have run into that problem if we were just reading some papers"
- 2025 [stated], S22:
  - [1:02:01] "tenemos una interacción muy fuerte con la industria, es lo que motiva mucho de nuestro trabajo" (tr.: "we have a very strong interaction with industry; it is what motivates much of our work").
  - [0:51:01], on the origin of his power-system expansion work: "esto fue curiosamente una interacción con la compañía Exon Móvil" (tr.: "this was, curiously, an interaction with the company ExxonMobil"; ASR: Exon Móvil = ExxonMobil).
  - The written abstract of the same talk: "A number of these projects have been the result of collaborations with industry in our Center for Advanced Process Decision-making and have shown to lead to significant improvements through systematic application of Process Systems Engineering techniques."

**P2. Set the agenda from data about industry and from the vantage point of leadership roles.** [stated] P (2004); [stated-joint] (2000).
- S2 p. 1, his stated basis for speculating on future research: "my interactions with employers and advisory boards has given me a useful perspective on the educational and research needs of the chemical industry."
- S2 abstract (p. 1): revenue, R&D and job-placement facts "are used to argue that to support the "value preservation" and "value growth" industry three major future research challenges need to be addressed".
- S1 (2000) derives topics from "major drivers": globalization, investor pressure, e-commerce, environmental pressure, new chemistries.

**P3. Widen the scope along the chain of length and time scales, from molecules to the enterprise and the climate.** [stated-joint] 2000. [stated] 2004, 2017, 2025.
- S1 p. 1 (definition): "Process Systems Engineering is concerned with the improvement of decision making processes for the creation and operation of the chemical supply chain."
- S2 restates this definition and builds the 2004 agenda on it.
- S22 [0:29:00]: "La tendencia últimamente ha sido por un lado ir a la parte molecular" (tr.: "the trend lately has been, on one side, to go to the molecular level"). The talk then moves to the enterprise, the supply chain and "global" climate change.

**P4. Why now: industrial pressure meets an enabling tool that has a gap.** [stated] P (2005, 2009, 2025).
- 2005, S5 p. 1847: enterprise IT systems had made information sharing possible, but "these tools do not generally provide comprehensive decision making capabilities that account for complex tradeoffs and interactions across the various functions, subsystems and levels of decision making." That gap is the opening for EWO.
- 2009 [stated-joint], S13 p. 18: "sustainability offers a great opportunity to renew the interest in process synthesis since it appears that many of the new biofuel plants have not had the benefit of being subjected to more systematic and thorough optimizations as their petrochemical counterparts."
- 2025 [stated], S22 [1:04:02], asked for the main bottleneck: "cómo manejar a largo plazo la incertidumbre. Incertidumbre tanto en tecnología como en la parte económica" (tr.: "how to handle long-term uncertainty, both technological and economic").

**P5. Take on problems that others call hopeless, and treat public dismissal as motivation.** [stated] P (2024, early-1980s story).
- S20 [0:47:32]: a keynote at a "Foundation of computer edit design" (ASR: FOCAPD) meeting was titled "process synthesis a Utopia in mathematical programming or an adventure in heuristics".
  - Its argument as he recalls it [0:48:02]: "the problem we don't know how to solve these problems so what's the point why waste our time"
  - His reaction [0:48:30]: "it was also motivation for us to try to see well can we prove him to be wrong"
  - Later [0:49:02]: "after you know almost 40 years definitely the answer is yes"
  - He does not name the speaker. Not identified here.
- He also reports being advised to move to process control instead, [0:51:30]: "it's very clear that you like math maybe what you should do is to do research in process control"

**P6. The field has a social responsibility: energy, water and climate.** [stated] P (2004, 2019, 2025).
- 2004, S2 p. 12: "Despite the great importance of sustainability and environmental issues, the research efforts from the PSE community have been rather timid. A bolder and more creative approach is clearly needed."
- 2019, S19 p. 12: "nuestra área también ha reconocido que tiene una responsabilidad social y se ha concentrado en los grandes retos del siglo XXI: la energía, el agua y el calentamiento global." (tr.: "our area has also recognised that it has a social responsibility and has concentrated on the great challenges of the 21st century: energy, water and global warming.")

### Layer 3: Idea generation

**G1. Borrow from OR and mathematics through personal contact.** The routes: Sargent (NLP, and links with the optimization community), Balas (disjunctive programming, which led to GDP), Hooker (logic, which led to logic-based optimization), Westerberg (multidisciplinarity). [stated] P. At least 4 occasions: 2013 (acknowledgment), 2019, 2024, 2025.
- 2013, S7 p. 31 (acknowledgment in his voice): "Ignacio Grossmann also would like to acknowledge Professor Egon Balas from Carnegie Mellon for his inspiring and pioneering work in the area of disjunctive programming."
- 2019, S19 p. 11:
  - Balas's "trabajo de programación disyuntiva nos llevó a desarrollar un nuevo paradigma llamado Programación Generalizada Disyuntiva del cual estoy muy orgulloso" (tr.: "his disjunctive-programming work led us to develop a new paradigm called Generalized Disjunctive Programming, of which I am very proud").
  - Westerberg "me enseñó la importancia de la investigación multidisciplinar en la cual las interacciones con ciencias de la computación, matemáticas e investigación operativa han ayudado a enriquecer las metodologías de diseño y optimización de la Ingeniería de Sistemas de Procesos" (tr.: "taught me the importance of multidisciplinary research, in which interactions with computer science, mathematics and operations research have helped enrich PSE's design and optimization methodologies").
- 2024, S20:
  - He sat in on Balas's integer-programming course [0:42:32]: "that's where I learned of course about you know relaxations"
  - GDP came out of discussions with Balas and his PhD students [0:44:00]: "we actually developed something that we call later on generalized subjunctive programming" (ASR: disjunctive).
  - Logic-based optimization came from a multidisciplinary engineering-design research effort [0:57:00]: "professor John hooker was part of that and he was you know very much interested in logic"
- 2025, S22 [0:20:00], on PSE's many neighbouring fields: "Para nosotros es muy importante interaccionar con estas áreas, no es simplemente un área muy restringida." (tr.: "For us it is very important to interact with these areas; it is not simply a very restricted area.")

**G2. Look for the hidden mathematical structure in an applied problem, and reformulate it into a class you can solve exactly.** [stated] P (2024, a story from his PhD).
- S20 [0:32:31–0:33:30], on a multipurpose batch-plant problem brought by visiting professor David Rippin (ETH):
  - "I thought well this this is non differentiable"
  - Then: "that problem mathematically it was really a geometric programming problem". By an exponential transformation it became a convex NLP with a unique solution.
- S20 [0:36:00+], on his phase-equilibrium work in Mexico: "you can get explicitly the derivative and analytically without doing any numerical preservation so those were nice properties" (ASR: "preservation" probably stands for "perturbation" or "differentiation" [inferred]).

**G3. Counter-intuitive examples trigger new formal methods.** [stated-joint] P (2014).
- S8 p. 2: "We then provide two motivating examples that show the non-trivial nature of these areas, and which motivated much of the subsequent research."
- S8 p. 5: "This brilliant example by Saboo & Morari (1984) shows that it is possible to have non-vertex critical points, and consequently, that we need appropriate methods that will be able to predict such points."
- The practice being criticised, S8 p. 2: "The conventional approach is to consider only nominal conditions without anticipating effects of changes and uncertainties in plant operation. The remedy is to use overdesign to compensate for lack of anticipation."

**G4. A numerical pathology in the natural formulation motivates a new framework.** [stated] P (2024).
- S20 [0:59:02], on superstructure NLPs: "the problem is that when the flows go to zero okay the equations can become singular"
- GDP's answer is to drop the inactive equations from the subproblem (quote in T5).

**G5. Start from the application, then generalize.** [stated] P (2024), together with the 2000 and 2014 statements in T2.
- S20 [1:01:30]: "the work that we have developed again has been inspired by these applications but then you know we're able to fortunately make them sufficiently General so they are also being used in other disciplines"
- S20 [0:55:31]: "the motivation came from the fact that we wanted to solve you know engineering problems that were clearly nonlinear optimization that involved discrete variables"

**G6. Ideas take shape in discussion with strong students.** [stated] P (2019, 2024).
- S20 [0:55:31+], on Marco Duran and outer approximation: "I still remember with him having the discussions on what what later on became as the a approximation method" (ASR: outer approximation).
  - In the same passage he also credits Ramesh Raman (logic, GDP) and Keshava Halemane (flexibility).
- S19 p. 11: "tengo que agradecer y reconocer a mis estudiantes de doctorado y posdoctorado sin los cuales las contribuciones de investigación que el Profesor Caballero mencionó no habrían sido posibles." (tr.: "I must thank and acknowledge my doctoral and postdoctoral students, without whom the research contributions Professor Caballero mentioned would not have been possible.")

### Layer 4: Experiments and execution (modelling, formulation, algorithms, computation)

**E1. A three-step method for synthesis: (1) represent the alternatives (a superstructure), (2) formulate a mathematical program with discrete and continuous variables, (3) solve it.** [stated-joint] in writing (1999, 2009, 2017); [stated] in speech (2014, 2024, 2025). At least 6 occurrences (C7).
- 1999, S12 p. 1:
  - "The mathematical programming approach to design, integration and operation problems, or more generally synthesis problems, consists of three major steps."
  - The aim: "which offers the possibility of developing automated tools to support the exploration of alternatives and optimization of chemical processes by design engineers."
- 2009, S13 p. 4: "The first is the development of a representation of alternatives from which the optimum solution is to be selected."
- 2017, S9 p. 1: "Optimization-based strategies involve three major steps"
- 2014, S21 [0:01:41]: "we can construct a template where we consider all possible alternatives, and we model then that problem with mixed-integer optimization"
- 2024, S20 [0:48:02], describing his own early paper: "develop a super structureal representation that theory representation then formulated you know introduce discrete continuous variables formulated as a mixed integer optimization problem"
- 2025, S22 [0:25:01]:
  - "esto es lo que se llama una superestructura en donde ponemos todas las alternativas que queremos considerar" (tr.: "this is what is called a superstructure, where we put all the alternatives we want to consider").
  - "eso permite casi automatizar la generación de esquemas de procesos" (tr.: "that makes it possible almost to automate the generation of process flowsheets").
- A requirement on the superstructure, 1999, S12 p. 3:
  - "Most of the previous work has relied on representing the superstructure for each particular problem at hand, but without following some general principles."
  - "The second is, for a given representation that is selected, what are all the feasible alternatives that must be included to guarantee that the global optimum is not overlooked."

**E2. Choose the level of model detail on purpose: aggregated, shortcut, or rigorous. Detail is not always needed.** [stated-joint] P. 3 documents (C8).
- 1999, S12 pp. 3–4: "A common misconception about the mathematical programming approach is that models are always detailed and require a great deal of information. This, however, is not necessarily true."
- 2009, S13 p. 5: "synthesis models can be formulated at three major levels of detail"
- 2017, S9:
  - p. 8: "Models can be characterized into three main levels of detail: high-level aggregate models, shortcut models, and detailed rigorous models."
  - p. 9: "The modeler must contend with the tradeoff between solving approximate models exactly, versus solving more exact models only approximately."

**E3. Solve the deterministic problem well before adding uncertainty, and match the uncertainty method to the time horizon.** [stated] P (2024); [stated-joint] (2019).
- 2024, S20 [1:05:30], his message to industrial partners: "you want to solve a problem under uncertainty first and foremost you need to have a robust and well- defined deterministic problem"
  - Followed by: "if we cannot solve efficiently the teristic problem going that extra step to add the stochastic programming whether it's Su AG or multi-stage you know it's a major you know computational expense that you're going to incur" (ASR: "teristic" = deterministic; "Su AG" probably = two-stage [inferred]).
- 2019 [stated-joint], S18 p. 966:
  - "while initially EWO models are formulated as being deterministic, it is clear that there often exists the need to account for uncertainties"
  - "Problems of the former type are often addressed through robust optimization techniques, since their goal is to ensure feasibility over a range of possible realization for the near-term future. In contrast, for long-term strategic problems, stochastic programming is often used because of its probabilistic view of the future and its focus on optimizing outcomes in expectation"
- 2005 [stated], S5 p. 1848, on uncertainty: "Major issues here are the development of novel, meaningful and effective stochastic programming tools."

**E4. Rules of thumb for choosing a convex-MINLP method.** [stated-joint] P (2004). Stated with an explicit caveat about missing evidence.
- S3 p. 26: "It is difficult to make general remarks on the efficiency and reliability of all these codes and their corresponding methods since no systematic comparison has been made. However, one might anticipate that branch and bound codes are likely to perform better if the relaxation of the MINLP is tight. Decomposition methods based on OA are likely to perform better if the NLP subproblems are relatively expensive to solve, while GBD can perform with some efficiency if the MINLP is tight, and there are many discrete variables. ECP methods tend to perform well on mostly linear problems."
- He co-authored the "systematic comparison" this sentence calls for 14 years later (S11; see J2) [inferred link].

**E5. Reformulations trade size against tightness: big-M is smaller, hull is tighter.** [stated-joint] P (2013, 2012).
- S7 p. 31: "The former is smaller in size, but the latter exhibits stronger continuous relaxations, and hence stronger lower bounds, which may potentially translate into a more efficient solution times, although this is not always the case due to the increased size of the reformulation."
- S16 p. 14: "It is important to note, however, that in the last few years, MIP solvers have improved significantly in the use of the problem structure to reduce automatically the size of the formulation."

**E6. When a monolithic model is too large for commercial solvers, design a decomposition that follows the structure.** [stated] P (2025); [stated-joint] (2002, 2019).
- 2025, S22 [0:53:01], on a power-expansion model with 1.5 million constraints:
  - "Si uno trata de utilizar un software comercial directamente, es imposible resolver este problema." (tr.: "If one tries to use commercial software directly, it is impossible to solve this problem.")
  - "Entonces, aquí lo que hicimos aportunadamente fue desarrollar un método de descomposición" (tr.: "So what we did here was to develop a decomposition method"; ASR: "aportunadamente" = afortunadamente).
- 2019, S18 p. 966: "decomposition techniques (e.g., Benders, Lagrangean) become essential for effectively addressing these problems."
- 2002: see the S14 quote in T5.

**E7. Put methods into modelling systems so that others can use them.** [stated] P (2024, 2025).
- S20 [1:00:02]: "with outo approximation we developed this computer code called tyup tyup was was maybe the first at least commercial available in my NLP solver that we made available through Gams" (ASR: outer approximation; DICOPT; MINLP solver; GAMS). The GAMS link came from a sabbatical.
- In 2025 he presented Pyomo.GDP, where several GDP solution methods are automated (S22 [0:22:01]).

**E8. Craft discipline in the punch-card era** (context for an older generation's habits). [stated] P (2024).
- S20 [0:37:00]: "you have to be extremely extremely careful because if you made a mistake in the syntax" … "you want to lose one day just because of the cim mistake in the" (ASR: "you would lose one day just because of the syntax mistake").
- From the same passage [0:35:30]: during his PhD, "we would talk about the need for mixed IND digal programming but I never got my hands on a mix integer programming uh code". He first used one at the Mexican Petroleum Institute.

### Layer 5: Judging results (validation, benchmarking, claims of impact)

**J1. In PSE most "experiments" are virtual. The validation hierarchy runs from theorems, to provable properties, to demonstration on example problems.** [stated-joint] P (2000).
- S1 p. 2: "One can test the models, ideally by proving and disproving theorems about them, but more often one can only prove mathematically some useful properties or empirically demonstrate that the proposed model works for a set of example problems."

**J2. A stated protocol for comparing solvers.** [stated-joint] P (2018/2019, S11). Grossmann is the senior author; the individual author of each rule is unknown.
- Test set: the whole relevant library, not a hand-picked sample. p. 1: "As a test set, we have used all MINLP instances classified as convex in the problem library MINLPLib, resulting in a test set of 366 convex MINLP instances."
- No tuning, p. 44: "Note that we have not tried to fine tune any of the solvers; however, if there is a convex strategy, or recommended convex parameters we have used those."
- Realistic hardware, p. 13: "We have allowed the solvers to use a maximum of eight threads to replicate a real-world situation where one tries to solve the problems with all the available resources."
- Returned solutions checked independently with the PAVER tool, p. 19: "If some solution returned by a solver is wrong, these instances are given the status error"
- Choice of plot, p. 16: "We have not used performance profiles where the time is normalized with respect to best solver [40] since these are not necessarily good for comparing several solvers as noted by [62]."
- Fairness and scope caveats:
  - p. 29: "Comparing the global solvers (ANTIGONE, BARON, and Couenne) with the convex solvers is not completely fair since the global solvers are able to solve a wider class of problems."
  - p. 30: "Based on the results presented here, one should not draw any conclusions on how the solvers perform on nonconvex problems."
  - p. 12: "It should be noted that the solvers left out of the numerical comparison are not necessarily inferior compared to the other solvers."
- Relevance caveat and a call to the community, p. 31:
  - "However, it should be noted that many of the test instances are quite small and simple compared to industry-relevant problems."
  - "We also hope that this paper encourages MINLP users to submit their instances to the instances libraries"

**J3. A reporting standard for models and computational results.** [stated-inst] P (minlp.org; Grossmann chair, Jon Lee vice-chair; undated, NSF grant OCI-0750826).
- Goals:
  - "Create a library of optimization problems in different application areas in which one or several alternative models are presented with their derivation."
  - "Provide a forum of discussion for algorithm developers and application users where alternative formulations can be discussed as well as performance and comparison of algorithms."
- Contributor instructions:
  - "For uniformity, please use minimization of your objective function."
  - "For the former provide version of modeling system used, version of optimization solvers used, choice of values of special parameters (eg optimality tolerance)."
  - "Present comparisons among various solvers if appropriate."
  - "Also, try to supply data to create models of varying size."
  - (The instructions also ask for results tables with objective value, problem size, CPU time, and indicators such as nodes, relaxation and iterations.)

**J4. Show impact in physical and economic units, against the conventional or heuristic baseline.** [stated] P (2014, 2025).
- 2014, S21:
  - [0:02:00] water network: "This case actually from 300 tons per hour down to only 14 tons per hour."
  - [0:04:00] water trucks "from 14,000 to less than 1,400 trucks".
- 2025, S22: the same water-network theme (40 against 300 t/h) and cost figures for an intensified distillation column.
- The difficulty of attributing value inside a company, [stated-joint] S10 p. 9: "it may often be impossible to tell how much an investment in a better optimization actually contributes to a better profit."
- 2025, S22 [1:09:02], on companies: "están muy contentos de los resultados que han obtenido, pero no nos dicen los resultados que han tenido." (tr.: "they are very happy with the results they obtained, but they do not tell us what the results were.")

**J5. Guaranteed global optimality is worth hours of computing.** (See T3, S22 [0:39:00].) [stated] P (2025).

**J6. Claim modestly for long-horizon models: they guide decisions and are re-solved as data change.** [stated] P (2025).
- S22 [0:54:02]:
  - "este tipo de herramientas por lo menos sirven para guiar a los que toman decisiones" (tr.: "these kinds of tools at least serve to guide decision-makers").
  - "ese tipo de modelo se puede ir actualizando año por año con nueva información y nuevos costos" (tr.: "that kind of model can be updated year by year with new information and new costs").

**J7. An optimal answer should also be explainable, with equivalent alternatives shown. This is where he expects AI to matter most.** [stated] P (2025).
- S22 [1:16:03], quoting operators who receive a model's answer: "¿por qué tengo que creer que eso es óptimo?" (tr.: "why should I believe that this is optimal?").
- The research need he draws:
  - "poder explicar en forma cualitativa las soluciones óptimas que se obtienen" (tr.: "to be able to explain qualitatively the optimal solutions obtained").
  - "¿Qué otras alternativas puede haber que podrían ser equivalent?" (tr.: "what other alternatives might be equivalent?").
- On AI more broadly, [1:15:00]:
  - Models must remain "matemáticos con conocimiento físico" (tr.: "mathematical, with physical knowledge"): "Estos tipo de modelos son más bien una vez más matemáticos con conocimiento físico."
  - A neural network "no es otra cosa que un método de regresión" (tr.: "is nothing other than a regression method").
  - [1:17:01] Using AI to automate model writing in modelling languages counts as "labores que son más de tipo mecánico" (tr.: "tasks of a more mechanical kind"). Verbatim: "son labores que son más de tipo mecánico".
- Cross-reference for 03 [practice]: Kakkad, Grossmann, Springub, Galanopoulos et al., "Iterative MILP algorithm to find alternate solutions in linear programming models", *Optim. Eng.* 25(4):2401–2424 (2024), DOI 10.1007/s11081-024-09887-3. It was developed for an industrial partner; CMU news (S30) reports it won the journal's 2024 Rosenbrock Prize.

### Layer 6: Writing, talks and teaching

This layer is thin: there is no stated writing method beyond the items below.

**W1. Choose the venue by emphasis.** [stated] P (2024).
- S20 [0:54:30+], on where to submit: it "usually depends of course if the emphasis is more on the application then of course we'll go to the chemical engineering Journal but if not we definitely also submit it to a you know mathematical math Programming type of Journal"

**W2. His early talk style was mathematical-first ("British"), and he later learned that the US audience expected motivation.** [stated] P (2024, self-report about 1979).
- S20 [0:40:30]: at Imperial College the habit was to "go straight to the point not using so much you know introduction and motivation". His first slide at his CMU job talk showed an NLP formulation.
- A colleague later told him that people had wondered [0:40:03]: "does he really know how to communicate"
- Whether his later style changed is for 03 [inferred]. His perspective essays (S2, S5) do open with industry facts and motivation.

**W3. Writing a textbook takes protected time, consistent notation, and exercises drawn from teaching.** [stated] P (2024, about his 2021 Cambridge textbook, DOI 10.1017/9781108917834).
- S20 [1:27:30]: he wrote it on sabbatical ("three months in Argentina"). The notes had built up over "maybe 8ye period" (ASR: an 8-year period) [1:28:30].
- [1:27:30] "you need to have that type of concentration"
- [1:29:01] "you have to care about a lot of details especially notation and other things and to be consistent also also the exercises"
- [1:29:01+] "that's where I would take most of my exercises or from exams"

**W4. Teaching is half the job, process design is a science, and relevant projects motivate students.** [stated] P (2024).
- S20:
  - [1:28:01] "as academics we have to realize that it's both we're here why because of two things because of education and because of research so we have to do try to excel him both" (ASR: "excel in both").
  - [1:24:00] "there is say a science phase in process design and that's what we're trying to teach to our students" (ASR: "science base").
  - [1:25:30+] "I think the students also get highly motivated when they see that they're working on design projects that are relevant"
- When a dean warned him about student workload in the design course, he answered [1:36:01]: "isn't learning important". The students later gave him the teaching award.

**W5. Make deployed tools usable by non-experts ("PhD-free"), and keep the value case visible.** [stated-joint] P (2019).
- S10 p. 8: "Here, the main guarantee to keep the solutions available is to make them "PhD-free", i.e. ensure that you need not be an expert to be able to manage their daily use and configuration."
- This sits in the industrial-practice section, so it is probably Harjunkoski's voice [inferred].

**W6. Recognition for exposition.** [observed] S (S25 media mention): "Grossmann awarded 2026 Saul Gass Award for Expository Writing".
- The INFORMS award page fetched on 2026-10-10 (S33) did not list a 2026 recipient. Unconfirmed at the source.

### Layer 7: Research organisation (consortium, collaboration, students, time)

**O1. The industrial consortium is the core organising device: a "two-way street" that must still yield original, publishable PhD work.** [stated] P (2024, 2025). Consistent with the 2012 and 2019 texts.
- S20 [1:14:00]: "what we're looking for is a two-way street"
  - [1:14:00+]: "in many of them we do involve PhD students so they have to for to a PhD thesis and do some original work that you know can be published"
  - He reports "at least you know 15 maybe even 20 20 joint papers" with one industrial collaborator (John Wassick, Dow; name from agent 04's ASR glossary).
  - He adds that the process industries "do believe in research" [1:15:01].
- 2019 [stated-joint], S10 p. 8, the typical set-up: "The most typical setup (Fig. 7) is that a PSE group does a joint project with an industrial partner that first provides the problem requirements and some representative data for the development."
- 2025, S22 [1:07:03–1:09:02], on intellectual property:
  - "no queremos a los abogados porque tan pronto se toca el tema de propiedad intelectual" (tr.: "we don't want lawyers, because as soon as intellectual property comes up [it becomes a mess]").
  - "hemos hecho los contratos de tal forma que son contratos directos" (tr.: "we have written the contracts so that they are direct contracts"; he calls them restricted funds).
  - "lo importante para nosotros como académicos es divulgar la información" (tr.: "what matters for us as academics is to disseminate the information").
  - "para nosotros es importante estar expuestos a problemas de tipo real" (tr.: "for us it is important to be exposed to real problems").

**O2. Multidisciplinary teams that include OR people.** [stated] P (2005, 2012, 2025); [stated-joint] (2000).
- 2005, S5:
  - p. 1850: "We should note that collaboration between researchers in process systems engineering and operations research should be most fruitful in this area."
  - p. 1854: "chemical engineers can play a major role not only in the modeling part, but also in the algorithmic part given the strong and rich tradition that chemical engineers have built in mathematical programming."
- 2012, S6 p. 2, on the CAPD EWO group: "This research effort has been multidisciplinary in nature involving faculty from chemical engineering". The group also included industrial engineering (Lehigh, Pittsburgh) and OR (Tepper School) faculty and 14 companies.
- 2019 [stated-joint], S10 p. 14 (industrial section): "The thought that the PSE-community can handle this alone is unrealistic"
- Survey finding reported in S10 p. 12: "Frequently there have been complaints that academia does not get access to realistic industrial problem data, as well as, industry does not have a chance to test novel appearing methods early enough."

**O3. Students are the main asset. Give them credit, and hold them to new ideas and high standards.** [stated] P (2019, 2024).
- S20 [1:18:01+]: "the biggest gift I have received if you wish is to have all these very motivated highly talented students"
- S20 [1:37:30], on two former students hired by the same department: the group is "trying to promote Ste new ideas" and "especially try to keep standards of excellence" (ASR: "promote new ideas").
- S19 p. 11: credit to students (quote in G6).

**O4. Advice to young researchers: persevere, have a dream ("ilusión"), be passionate and creative, keep high standards.** [stated] P. 2 occasions (2019, 2024), with at least 6 mentions in all. [observed] corroboration of the 2019 emphasis (S28).
- 2019, S19 pp. 11–12:
  - "Creo que una de las lecciones más importantes que he aprendido es la importancia de tener una ilusión" (tr.: "I believe one of the most important lessons I have learned is the importance of having a dream / an aspiration"). He then quotes J. F. Kennedy on people "who can dream of things that never were".
  - "esto se refiere a la importancia de la pasión y creatividad para promover nuevas ideas y nuevas soluciones para resolver problemas técnicos y sociales." (tr.: "this refers to the importance of passion and creativity to promote new ideas and new solutions to technical and social problems.")
  - "es importante soñar y tener ilusión para resolver problemas que no han podido ser resueltos. Para que esto se consiga traducir en resultados concretos, se requiere de perseverancia, lo que significa trabajar fuerte y con esfuerzo continuo." (tr.: "it is important to dream and to have aspirations in order to solve problems that have not been solved. For this to translate into concrete results, perseverance is required, which means working hard with continuous effort.")
  - He follows this with an Einstein quote about spending more time on problems.
- 2024, S20 [1:38:01–1:39:32]:
  - "do not give up you know you have to be persistent"
  - "it was having that dream to say no yes we we can do it" (about mixed-integer programming once being dismissed)
  - "nothing great has ever been accomplished without passion" (attributed to Hegel)
  - "please try to be passionate and try to keep the highest levels of Excellence of your work"
- [observed] S28 (University of Cantabria PASEP group page, on the 2019 speech): he "devoted the last part of his speech to encourage future generations in the discovery of their PASSION and its achievement through PERSEVERANCE."

**O5. Time and attention: administrative overhead is the cost he regrets, and deep work needs blocks of concentration.** [stated] P (2024).
- S20 [1:33:33]: "we SP so much time reading email" (ASR: "we spend"). He wishes he had had more time to read books, especially on the history of mathematics.
- He also notes that secretarial support has disappeared.
- See W3 for the concentration needed to write books.

**O6. Open infrastructure for the community.** [stated-inst] P (minlp.org).
- The problem it addresses (Goals page): "This community, however, is largely disconnected, especially between algorithm developers and application domain researchers."
- Front page: "We look forward to collaborating with you!"
- Library material is released under CC-BY 3.0.

---

## C. Recurring stated claims (≥3 repetitions = real belief)

Counts are of distinct sources or occasions, not sentences. "Joint" means the claim also appears in co-authored texts, where his own voice is not separable.

| # | Claim | Occasions | Dates | Where |
|---|---|---|---|---|
| C1 | Good PSE research must be intellectually challenging **and** industrially relevant (theory–practice balance) | 8 (5 single-voice, 3 joint) | 2000–2024 | S1, S2, S6, S10, S18, S19, S20 (also S23 2017 implicitly) |
| C2 | Industry (CAPD partners) is the main source of problems, more than the literature | 7 | 2004–2025 | S2, S23, S10 (acknowledgment in his voice), S19, S20, S22 (talk and abstract) |
| C3 | Modelling and formulation are central; make "good formulation" systematic (GDP) instead of an art | 6 | 2000–2025 | S1, S3, S5, S7, S20, S22 |
| C4 | Rigour and guarantees are the default; heuristics allowed but labelled non-rigorous and justified by cost | 8 | 1999–2025 | S12, S14, S15, S3, S4, S19, S20, S22 |
| C5 | Work across disciplines, especially with OR, computer science and mathematics | 6 | 2000–2025 | S1, S5, S6, S19, S20, S22 |
| C6 | Exploit problem structure; domain physics is what reveals the structure | 4 | 2002–2025 | S14, S5, S20, S22 |
| C7 | Three-step synthesis method: superstructure → formulation → solution | 6 | 1999–2025 | S12, S13, S9 (written); S21, S20, S22 (spoken) |
| C8 | Three levels of model detail (aggregate / shortcut / rigorous); detail is not always needed | 3 | 1999, 2009, 2017 | S12, S13, S9 (all joint) |
| C10 | Systematic optimization beats intuition, heuristics and engineering judgement, and finds non-obvious designs | 5 | 2014–2025 | S21, S8, S9, S20, S22 |
| C11 | Breakthroughs need new theory and algorithms, not only faster computers | 3 | 2004–2005 | S2, S5, S4 (joint) |

**Below the threshold (fewer than 3 occasions; record, do not promote):**
- "Persevere, dream, be passionate, keep high standards": 2 occasions (2019, 2024), each with several mentions. One more occasion would make it C9.
- "Deterministic first, then uncertainty": 1 explicit statement (2024) plus 1 joint (2019).
- "Explainability of optimal solutions": 2025 only.
- "Venue by emphasis": 2024 only.
- "Choose fields by the size of the industrial stake": 2004 and 2017.

---

## D. Self-reported failures, rejections, resistance and open problems (stated)

- **Early rejection of MILP-based synthesis** [stated], S20 [0:45:30+]: "had one such paper that actually got rejected because one of the revie said well the authors are proposing mix line programming which you know we know it's very inefficient for solving so one would be much better off using some heuristics" (ASR: reviewers; mixed-integer linear programming). Early 1980s; the paper is not identified.
- **Public dismissal at a FOCAPD keynote and advice to change field** [stated], S20 [0:47:32–0:51:30]. See P5.
- **Resistance from pinch-analysis advocates**, S20 [0:45:30]–[0:46:30]:
  - "there was a lot of resistance of people"
  - The opponent he names by description only [0:46:01]: "in the area of feed exchanger networks there was a professor who actually did his PhD at leads in the UK" (ASR: heat exchanger networks; Leeds).
  - Not identified here.
- **Slow review of the outer-approximation paper.** Duran & Grossmann, "An outer-approximation algorithm for a class of mixed-integer nonlinear programs", *Math. Program.* 36(3):307–339 (1986), DOI 10.1007/BF02592064.
  - S20 [0:56:01]: "from the time we submitted until it was accepted it took three years"
  - His explanation [0:56:01+]: "maybe it was our engineering type of slant that did not fit exactly with the one of math programming"
  - [practice, for 03]: Crossref lists a one-page item with the same title in *Math. Program.* 39(3):337 (1987), DOI 10.1007/BF02592081, which appears to be an erratum. **Not read.**
- **A rejection reported second-hand (his mentor's paper)**, S20 [0:50:01]. The State-Task Network paper, Kondili, Pantelides & Sargent, "A general algorithm for short-term scheduling of batch operations—I. MILP formulation", *Comput. Chem. Eng.* 17(2):211–227 (1993), DOI 10.1016/0098-1354(93)80015-F.
  - As he tells it, it was rejected twice ("for scheduling we want to solve real problems not toy problem") and accepted on the third submission.
  - He uses the story as a lesson about persistence. Second-hand: [stated] about others.
- **Self-assessed limits of the field and of his own agenda** [stated] / [stated-joint]:
  - 2004: sustainability work "rather timid" (S2 p. 12).
  - 2004 [stated-joint]: "no systematic comparison has been made" of MINLP codes (S3 p. 26).
  - 2005: a general-purpose process scheduling model "is still elusive" (S5 p. 1849).
  - 2012: optimizing entire supply chains "still remains an elusive problem" (S6 p. 16).
  - c. 2008+ [stated-inst], minlp.org: "finding the global solution of large-scale MINLP models (e.g. above 1,000 variables) in reasonable computational times (a few hours) is a major challenge, and currently a largely unsolved problem."
  - 2019 [stated-joint]: benchmark instances "quite small and simple compared to industry-relevant problems" (S11 p. 31).
- **Standing of PSE** [stated-joint], S10 pp. 11–12: the survey's "most alarming signal" was that "industry feels that academia is not investing enough efforts into PSE" (the sentence crosses the page break).
- **Personal regret** [stated], S20 [1:33:33]: email and administration crowded out reading. No retractions found. Errata: see the outer-approximation item above.

---

## E. Era and resource context of the stated methods

- **1974–1979 (PhD at Imperial; Mexican Petroleum Institute).**
  - Computing: punch cards and Fortran. A run could take "a full day" (S20 [0:37:00]).
  - No MINLP code existed. He used an implicit enumeration scheme with Sargent's variable-metric-projection NLP method. His first MIP code (FMPS on a Univac) was at the petroleum institute (S20 [0:35:30]).
  - The stated habits from this period: "be extremely careful", and look for structure that makes a problem convex or analytically differentiable (G2). Both are rational under scarce, slow computing.
- **1979–1994 (CMU faculty).**
  - CMU's Design Research Center and later the Engineering Design Research Center gave him multidisciplinary teams (Hooker, logic). Balas's integer-programming course was on campus.
  - CAPD (founded 1985) supplied industrial problems.
  - The resistance stories (D) and the stated persistence ethic come from this period, when MIP solvers were weak.
- **1994–2002 (department head).** The stated agenda-setting habit (P2) comes from a leadership vantage point: advisory boards, employers, NRC and AIChE committees (S2 p. 1).
- **2005–2015 (CAPD director; EWO group; NSF CMU–IBM cyberinfrastructure).** The stated methods turn organisational: consortium, multidisciplinary group, problem library and reporting standard (O1, O2, J3). MILP solvers had become strong (S5 p. 1850); the bottlenecks moved to multiscale models, uncertainty and integration.
- **2016–2026 (senior; phased retirement from 1 Sept 2023 [inferred]).**
  - Statements turn reflective and value-laden: excellence, passion, perseverance; credit to mentors and students.
  - They also turn toward sustainability (decarbonization, CO2 logistics) and AI. He positions AI as regression underneath, plus explainability and automation of "mechanical" modelling work.
  - Resources: open-source Python stack (Pyomo.GDP), global solvers (BARON), and models with about 10^6 variables solved by decomposition (S22).

---

## Contradictions (kept, not reconciled)

1. **Rigour as the value, yet heuristics are recommended in practice.**
   - He repeatedly labels non-rigorous methods as such (C4) and recalls fighting the "adventure in heuristics" view (P5).
   - Yet he offers heuristics of his own:
     - for nonconvex MINLP, "a heuristic that works reasonably well in many problems" (S15 p. 17);
     - for large planning and scheduling, larger instances "require some type of decomposition, aggregation and/or the use of heuristics for their solution" (S14, 2002, joint).
   - Both are stated. Whether he treats heuristics as a stopgap or as a method is for 03.
2. **OR as essential partner vs OR's blind spot.**
   - 2005: collaboration with OR "should be most fruitful", and chemical engineers can lead "not only in the modeling part, but also in the algorithmic part" (S5).
   - 2025: OR researchers' typical attitude is "dame el modelo … no es mi problema de dónde viene" (S22).
   - 2024: his outer-approximation paper's "engineering type of slant" did not fit the mathematical-programming community (S20).
   - He resolves this himself in 2025 ("the best combination" is OR plus PSE), but the 2005 and 2025 emphases differ.
3. **"Textbook" MIP modelling: impractical (2005) vs adequate because solvers adapt (2012).**
   - 2005: the "textbook" approach of auxiliary binaries "is often not practical" and obscures the structure (S5 p. 1850).
   - 2012 [stated-joint]: "MIP solvers have improved significantly in the use of the problem structure to reduce automatically the size of the formulation" (S16 p. 14).
   - Possibly a change over time, not a contradiction.
4. **Flexibility analysis vs (adjustable) robust optimization.**
   - 2024: for two or more uncertain parameters, the robust-optimization route gives "more conservative results", while flexibility analysis "actually gives you better answers" (S20 [1:07:00]).
   - 2017: he adopts "affine-adjustable recourse to avoid overly conservative results" (S23).
   - 2019 [stated-joint]: robust optimization is the recommended tool for near-term scheduling feasibility (S18 p. 966).
   - Recorded as stated.
5. **How hard is MINLP?**
   - c. 2008+ (minlp.org): global solution of MINLPs above about 1,000 variables in a few hours is "currently a largely unsolved problem."
   - 2024: "after you know almost 40 years definitely the answer is yes" (superstructure MINLP and GDP work).
   - 2025: a shale-gas nonconvex MINLP is solved to guaranteed global optimality in about 8.5 h.
   - Different dates and problem classes. Kept as a time series.
6. **Talk style: "straight to the point" vs motivation-first.** In 1979 he gave a formulation-first job talk in the Imperial manner (S20 [0:40:30]); his later perspective essays open with industry facts (S2). This is a self-reported change, or a difference of genre; no statement of a deliberate change was found [inferred].
7. **Biology as a focus.**
   - 2004: biology is "unlikely" to grow enough industrially to be "the major focus of PSE research" (S2 p. 13).
   - 2000 [stated-joint]: metabolic networks and bioprocesses are areas "likely to receive increased attention" (S1).
   - 2025: he features protein design (Floudas) and says that "relativamente una fracción pequeña es de tipo molecular todavía" (S22 [1:10:01]).
   - The views are compatible ("attention" but not the "major focus"), but they are kept as stated.

---

## Gaps

- **No long-form methodology text** was found: no essay, lab guide, or written advice to PhD students on how to do research. Layers 6 (writing) and 7 (supervision) rest on a thin base: two speeches and one interview.
- **Not read (attempted):**
  - Furman & Grossmann, "A biographical review of the research and impacts of Marco Duran" (2021; Springer paywall). It is likely to contain the origin story of outer approximation.
  - The two 2016 *AIChE J.* tributes to Sargent (Wiley 403). The interviewer quoted a tribute sentence ("a Visionary scholar with very high standards who believed in the power of mathematical optimization"), but its source was not identified.
  - The 2010 *AIChE J.* teaching essay with Biegler and Westerberg, and the 2014 essay with Varma (Wiley 403).
  - The ESCAPE-27 keynote abstract "Evolution of Process Systems Engineering and Future Trends in Research" (2017; ScienceDirect 403).
  - The preface of *Advanced Optimization for Process Systems Engineering* (2021; Cambridge Higher Education login). Only the publisher blurb was seen.
  - The 2021 Imperial College seminar video on regularized outer approximation (YouTube HTTP 429 on every attempt).
- **Not attempted:**
  - the 11-author paper "Education in Process Systems Engineering: Why it matters more than ever…" (2019, DOI 10.1016/j.compchemeng.2019.03.036; an open copy exists), where his individual voice is not separable;
  - the CRC chapter "Modeling, Simulation, and Optimization in the Chemical Engineering Curriculum" (2014/2019/2025 editions);
  - the prefaces of *Systematic Methods of Chemical Process Design* (1997) and *Global Optimization in Engineering Design* (1996);
  - the 2012 *AIChE J.* or *Chem. Eng. Prog.* features he edited.
- **Speeches whose text was not found:** honorary-doctorate addresses at Åbo Akademi, Maribor, TU Dortmund, Cantabria, Kazan, UNL (2018), RWTH Aachen and Universidad Nacional del Sur; the Sargent Medal (2015) and AIChE Institute-lecture talks; his talk "Evolución y Tendencias en la Educación Universitaria de Ingeniería en los Estados Unidos" (UNL 2018; Cantabria, 29 May 2019), for which only titles were found. A third occasion for the "passion / perseverance" advice (O4) might be among them.
- **Writing:** the 2026 INFORMS Saul Gass Award is confirmed only by CMU's page. No citation text and no stated writing method were found.
- **Identities not established:** the FOCAPD keynote speaker of the "Utopia … or adventure in heuristics" talk, and its year; the early-1980s rejected paper; the authors of the individual rules in the co-authored benchmark paper (S11).
- **Caption reliability:**
  - The interview, the 2014 video and the 2025 lecture are machine captions. Wording is approximate, though the meaning was clear in every passage quoted.
  - The 2025 lecture was quoted only from the Spanish original-language track. The English track is a machine translation and was not quoted.
  - A rule from the house style applies: re-check against the audio before quoting verbatim in a published skill.
- **Joint authorship:** for S1, S3, S4, S7–S14, S16–S18 and S24, his individual voice cannot be separated, except where a passage names him.

---

## Implications for Phase 2 (for the synthesiser; all [inferred])

- **The core stated research stance is a two-key test:** "intellectually challenging AND relevant to industry". A matching operational loop goes with it:
  1. an industry partner poses a problem;
  2. represent all the alternatives (superstructure);
  3. formulate at the right level of detail and with the right logic (GDP; big-M against hull);
  4. exploit the structure the physics reveals (decomposition, convexification, reduced subproblems);
  5. solve with guarantees where possible and with labelled heuristics where not;
  6. generalize the method and release it in a modelling system;
  7. publish in the venue that matches the emphasis.

  03 should check this loop against the papers.
- **Quick taste tests a Grossmann lens would apply to a user's project:**
  - Is there a real decision-maker with data?
  - Is the formulation unique, or have you compared alternatives (relaxation gap, size)?
  - Is the claimed optimum guaranteed, and if not, is that said?
  - Did you solve the deterministic version well before adding uncertainty?
  - Can the result be explained to an operator, with alternative solutions shown?
- **Stated benchmarking controls usable directly:** whole library subsets, default settings with no tuning, independent verification of returned solutions, solution profiles, explicit fairness and scope caveats, and a check of instance size against industry-relevant size.
- **Contested points to keep open in the skill:** heuristics vs rigour (Contradiction 1); OR partnership vs OR's "give me the model" (2); flexibility analysis vs robust optimization (4).

---

## Sources

**Primary (read)**
1. S1. I. E. Grossmann, A. W. Westerberg, "Research Challenges in Process Systems Engineering", *AIChE J.* 46(9):1700–1703, Sep 2000, DOI 10.1002/aic.690460902. Read in full in the egon preprint https://egon.cheme.cmu.edu/Papers/GrossmannWestChall.pdf (primary, joint).
2. S2. I. E. Grossmann, "Challenges in the new millennium: product discovery and design, enterprise and supply chain optimization, global life cycle assessment", *Comput. Chem. Eng.* 29(1):29–39, 2004/2005, DOI 10.1016/j.compchemeng.2004.07.016. Egon preprint https://egon.cheme.cmu.edu/Papers/GrossmannChall.pdf, read in full except the reference list (primary).
3. S3. L. T. Biegler, I. E. Grossmann, "Retrospective on optimization", *Comput. Chem. Eng.* 28(8):1169–1192, 2004, DOI 10.1016/j.compchemeng.2003.11.003. Egon preprint https://egon.cheme.cmu.edu/Papers/BieglerOpt_I.pdf, read in part (primary, joint).
4. S4. I. E. Grossmann, L. T. Biegler, "Part II. Future perspective on optimization", *Comput. Chem. Eng.* 28(8):1193–1218, 2004, DOI 10.1016/j.compchemeng.2003.11.006. Egon preprint https://egon.cheme.cmu.edu/Papers/GrossmannOptII.pdf, read in part (primary, joint).
5. S5. I. Grossmann, "Enterprise-wide optimization: A new frontier in process systems engineering", *AIChE J.* 51(7):1846–1857, 2005, DOI 10.1002/aic.10617. Published version at https://egon.cheme.cmu.edu/Papers/GrossmannEWO.pdf, read (primary).
6. S6. I. E. Grossmann, "Advances in mathematical programming models for enterprise-wide optimization", *Comput. Chem. Eng.* 47:2–18, 2012, DOI 10.1016/j.compchemeng.2012.06.038. Egon preprint https://egon.cheme.cmu.edu/Papers/GrossmannFOCAPO_EWO_Nov_21.pdf, read in part (primary).
7. S7. I. E. Grossmann, F. Trespalacios, "Systematic modeling of discrete-continuous optimization models through generalized disjunctive programming", *AIChE J.* 59(9):3276–3295, 2013, DOI 10.1002/aic.14088. Egon preprint https://egon.cheme.cmu.edu/Papers/Grossmann_Trespalacios_Systematic_Modeling_of_Discrete-Continuous_Optimization_Models.pdf, read in part (primary, joint).
8. S8. I. E. Grossmann, B. A. Calfa, P. Garcia-Herreros, "Evolution of concepts and models for quantifying resiliency and flexibility of chemical processes", *Comput. Chem. Eng.* 70:22–34, 2014, DOI 10.1016/j.compchemeng.2013.12.013. Egon preprint https://egon.cheme.cmu.edu/Papers/Grossmann_Flexibility_in_Chemical_Process_Design.pdf, read in part (primary, joint).
9. S9. Q. Chen, I. E. Grossmann, "Recent Developments and Challenges in Optimization-Based Process Synthesis", *Annu. Rev. Chem. Biomol. Eng.* 8:249–283, 2017, DOI 10.1146/annurev-chembioeng-080615-033546. Egon preprint https://egon.cheme.cmu.edu/Papers/Chen_Grossmann_review_process_synthesis.pdf, read in part (primary, joint).
10. S10. I. E. Grossmann, I. Harjunkoski, "Process Systems Engineering: Academic and industrial perspectives", *Comput. Chem. Eng.* 126:474–484, 2019, DOI 10.1016/j.compchemeng.2019.04.028. Egon extended PSE2018 paper https://egon.cheme.cmu.edu/Papers/Grossmann%20and%20Harjunkoski_Extended%20PSE2018.pdf, read in full (primary, joint).
11. S11. J. Kronqvist, D. E. Bernal, A. Lundell, I. E. Grossmann, "A review and comparison of solvers for convex MINLP", *Optim. Eng.* 20(2):397–455, 2019 (online 2018), DOI 10.1007/s11081-018-9411-8. Preprint dated June 3, 2018 at https://egon.cheme.cmu.edu/Papers/ConvexMINLPReview2018_OO.pdf, benchmark sections and conclusions read (primary, joint).
12. S12. I. E. Grossmann, J. A. Caballero, H. Yeomans, egon preprint "Advances in Mathematical Programming for the Synthesis of Process Systems", https://egon.cheme.cmu.edu/Papers/GrossmannCaballeroYeoAdv.pdf, read in part (primary, joint). Probable published version [inferred]: "Mathematical programming approaches to the synthesis of chemical process systems", *Korean J. Chem. Eng.* 16(4):407–426, 1999, DOI 10.1007/BF02698263. Titles differ.
13. S13. I. E. Grossmann, G. Guillén-Gosálbez, "Scope for the Application of Mathematical Programming Techniques in the Synthesis and Planning of Sustainable Processes", in *Design for Energy and the Environment* (CRC, 2009), pp. 55–76, DOI 10.1201/9781439809136-c5. Journal version *Comput. Chem. Eng.* 34(9):1365–1376, 2010, DOI 10.1016/j.compchemeng.2009.11.012. Chapter version https://egon.cheme.cmu.edu/Papers/FOCAPDK10451_C005.pdf, read in part (primary, joint).
14. S14. I. E. Grossmann, S. A. van den Heever, I. Harjunkoski, "Discrete Optimization Methods and their Role in the Integration of Planning and Scheduling", *AIChE Symposium Series* No. 326, Vol. 98, pp. 150–168, 2002. Venue from S26; no DOI. Egon preprint https://egon.cheme.cmu.edu/Papers/GrossmannVanHHarDiscrete.pdf, read in part (primary, joint).
15. S15. I. E. Grossmann, "Review of Nonlinear Mixed-Integer and Disjunctive Programming Techniques", *Optim. Eng.* 3(3):227–252, 2002, DOI 10.1023/A:1021039126272. Egon preprint https://egon.cheme.cmu.edu/Papers/GrossmannReviewNon.pdf, searched, passages read (primary).
16. S16. I. E. Grossmann, J. P. Ruiz, "Generalized Disjunctive Programming: A Framework for Formulation and Alternative Algorithms for MINLP Optimization", *IMA Vol. Math. Appl.*, pp. 93–115, 2011/2012, DOI 10.1007/978-1-4614-1927-3_4. Egon preprint https://egon.cheme.cmu.edu/Papers/IMAGrossmannRuiz.pdf, searched, passages read (primary, joint).
17. S17. I. Grossmann, P. Pardalos, "Preface of the Special JOGO issue in Memory of Professor Christodoulos A. Floudas (1959–2016)", *J. Glob. Optim.* 71(4):1013, 2018, DOI 10.1007/s10898-018-0685-3. Read (primary, joint).
18. S18. C. E. Gounaris, I. E. Grossmann, "A preface to the special issue on enterprise-wide optimization", *Optim. Eng.* 20(4):965–968, 2019, DOI 10.1007/s11081-019-09468-9. Read (primary, joint).
19. S19. I. E. Grossmann (Discurso) and J. A. Caballero (Laudatio), "Solemne Acto de Investidura como Doctor Honoris Causa del Sr. Ignacio E. Grossmann", Universidad de Alicante, 28 Jan 2019, RUA https://hdl.handle.net/10045/91533. Spanish PDF fetched through the DSpace REST API (bitstream 688a321e-04e5-464d-9776-c0b6858aa3a8). The address on pp. 9–12 was read in full; the laudatio was skimmed (primary).
20. S20. *Subject to: Ignacio Grossmann*, YouTube @Subjectto_, uploaded 2024-02-08, https://www.youtube.com/watch?v=jNjqnsnUzhE. Automatic captions read in full. The transcript saved by agent 04 is at `../sources/talks/2024-02-08_subject-to-interview_jNjqnsnUzhE.txt` (primary, caption-derived).
21. S21. *Ignacio Grossmann: Optimization Models and Methods*, CMU College of Engineering, uploaded 2014-10-07, https://www.youtube.com/watch?v=bx909_u-crY. Read in full. Transcript saved by this agent at `../sources/talks/2014-10-07_cmu-optimization-models-and-methods_bx909_u-crY_auto-captions.txt` (primary, caption-derived).
22. S22. *Evolution and Future Trends in Process Systems Engineering*, Real Academia de Ciencias Exactas, Físicas y Naturales, 16 Sep 2025 (uploaded 2025-09-17), https://www.youtube.com/watch?v=r9jdqigq59Q. The Spanish captions were read in full, together with the English abstract in the description. Transcript saved by this agent at `../sources/talks/2025-09-16_rac-spain-evolution-future-trends-pse_r9jdqigq59Q_es-auto-captions.txt` (primary, caption-derived).
23. S23. University of Wisconsin–Madison, Hougen Lectureship 2016–2017, Ignacio Grossmann (lecture titles, dates and abstracts), https://hougen-programs.che.wisc.edu/hougen-lecture-2016-2017-grossman.html. Read (primary: his lecture abstracts).
24. S24. CMU-IBM Cyber-Infrastructure for MINLP, https://www.minlp.org/index.php plus goals/index.php, participants/index.php and goals/instructions.php. Read on 2026-10-10 (primary, institutional, collective voice).
25. S25. CMU Chemical Engineering, "Ignacio Grossmann" bio page, https://www.cheme.engineering.cmu.edu/directory/bios/grossmann-ignacio.html. Read on 2026-10-10 (primary-institutional, plus media-mention list).
26. S26. "PUBLICATIONS IGNACIO E. GROSSMANN", August 2007, https://egon.cheme.cmu.edu/Papers/PublicationsIEGrossmann.pdf. Searched for venues (primary bibliography).

**Secondary (read)**
1. S27. L. Biegler, C. Gounaris, N. V. Sahinidis, B. E. Ydstie, "ChE educator: Ignacio Grossmann … of Carnegie Mellon University", *Chemical Engineering Education* 53 (2019; the page footers read No. 2 Spring and No. 3 Summer), https://journals.flvc.org/cee/article/view/114401. Read in full (secondary, [observed]; contains no direct quotes from him).
2. S28. University of Cantabria PASEP group, "Honoris Causa: Prof. Ignacio E. Grossmann" (https://grupos.unican.es/pasep/?p=1417) and "Conference: Prof. Ignacio E. Grossmann" (https://grupos.unican.es/pasep/?p=1643), 2019. Read (secondary).
3. S29. UNL Noticias, "La UNL distinguirá con el Honoris Causa a Ignacio Grossmann", 25 Sep 2018 (two URL variants under https://www.unl.edu.ar/noticias/news/view/). Read (secondary; biographical, no quotes).
4. S30. CMU ChemE news, "Industry collaboration yields top Optimization and Engineering paper", 25 Nov 2025, https://www.cheme.engineering.cmu.edu/news/2025/11/25-grossmann-rosenbrock-prize.html. Read (secondary; no Grossmann quotes).
5. S31. CMU ChemE news, "Optimizing for early success in research", 8 Jul 2026, https://www.cheme.engineering.cmu.edu/news/2026/07/08-optimizing-early-success-academia.html. Read (secondary; about his former students; no Grossmann statements; relevant to 04).
6. S32. Cambridge University Press, *Advanced Optimization for Process Systems Engineering* book page (publisher blurb only), DOI 10.1017/9781108917834. Read (secondary).
7. S33. INFORMS, "Saul Gass Expository Writing Award" page, https://www.informs.org/Recognizing-Excellence/INFORMS-Prizes/Saul-Gass-Expository-Writing-Award. Read on 2026-10-10; no 2026 recipient listed (secondary).
8. S34. CAPD homepage, https://capd.cheme.cmu.edu/. Read; institutional text not attributable to him; not used (secondary).

**Attempted, not readable**
1. S35. K. C. Furman, I. E. Grossmann, "A biographical review of the research and impacts of Marco Duran", *Optim. Eng.* 22(3):1233–1244, 2021, DOI 10.1007/s11081-021-09632-0. **Not read: Springer paywall.**
2. S36. I. E. Grossmann, M. F. Doherty, M. P. Harold, "A tribute to Roger Sargent", *AIChE J.* 62(9):2950, 2016, DOI 10.1002/aic.15423. **Not read: Wiley 403.**
3. S37. M. F. Doherty, I. E. Grossmann, C. C. Pantelides, "A tribute to professor Roger Sargent: Intellectual leader of process systems engineering", *AIChE J.* 62(9):2951–2958, 2016, DOI 10.1002/aic.15425. **Not read: Wiley 403.** Only the abstract was seen, via OpenAlex.
4. S38. L. T. Biegler, I. E. Grossmann, A. W. Westerberg, "Issues and trends in the teaching of process and product design", *AIChE J.* 56(5):1120–1125, 2010, DOI 10.1002/aic.12256. **Not read: Wiley 403.**
5. S39. A. Varma, I. E. Grossmann, "Evolving trends in chemical engineering education", *AIChE J.* 60(11):3692–3700, 2014, DOI 10.1002/aic.14613. **Not read: Wiley 403.**
6. S40. I. E. Grossmann, "Evolution of Process Systems Engineering and Future Trends in Research", *Computer Aided Chemical Engineering* (ESCAPE-27), p. 1, 2017, DOI 10.1016/B978-0-444-63965-3.50001-5. **Not read: ScienceDirect 403.**
7. S41. I. E. Grossmann, *Advanced Optimization for Process Systems Engineering*, Cambridge University Press, 2021, DOI 10.1017/9781108917834; Preface DOI 10.1017/9781108917834.001. **Preface not read: Cambridge Higher Education login.**
8. S42. *Ignacio Grossmann: Alternative Regularizations for Outer-Approximation Algorithms for Convex MINLP*, CogImperial, uploaded 2021-06-21, https://www.youtube.com/watch?v=u5LyNS_LS9U. **Not read: YouTube caption download returned HTTP 429 on four attempts.**

**Other works named in this file** (identifier checked against Crossref, content not read unless stated)
- M. A. Duran, I. E. Grossmann, "An outer-approximation algorithm for a class of mixed-integer nonlinear programs", *Math. Program.* 36(3):307–339, 1986, DOI 10.1007/BF02592064. A same-title one-page item exists: *Math. Program.* 39(3):337, 1987, DOI 10.1007/BF02592081 (not read).
- E. Kondili, C. C. Pantelides, R. W. H. Sargent, "A general algorithm for short-term scheduling of batch operations—I. MILP formulation", *Comput. Chem. Eng.* 17(2):211–227, 1993, DOI 10.1016/0098-1354(93)80015-F.
- D. Kakkad, I. E. Grossmann, B. Springub, C. Galanopoulos et al., "Iterative MILP algorithm to find alternate solutions in linear programming models", *Optim. Eng.* 25(4):2401–2424, 2024, DOI 10.1007/s11081-024-09887-3.
- Bibliographic tools: OpenAlex API (author A5056017028, found through ORCID 0000-0002-7210-084X; 945 works scanned for perspective, education and tribute titles) and the Crossref REST API (every DOI above was resolved on 2026-10-10).
