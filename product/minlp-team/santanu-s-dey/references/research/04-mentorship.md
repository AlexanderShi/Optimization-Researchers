# Santanu S. Dey: students and collaborators (research note 04, mentorship)

| Field | Value |
|---|---|
| Researcher | Santanu S. Dey, H. Milton Stewart School of Industrial and Systems Engineering, Georgia Institute of Technology (living) |
| Dimension | 04: students and collaborators. Covers supervision style, group habits, lab culture and tacit knowledge (framework §二, agent 4) |
| Research date | 2026-10-10 |
| Sources consulted | 80 source entries (see Sources). One entry is a batch of 39 further theses. Five more lookups returned nothing usable: MGP id 94025 (a different Santanu Dey), OpenAlex (rate-limited), Purdue e-Pubs (HTTP 403), TUprints search (empty), and one WebSearch for interviews and podcasts |
| WebSearch calls | 2 of the 2 allowed |
| Local corpus | `references/sources/{papers,talks,essays,software,publications}` hold only `.gitkeep`, so there was no user-supplied material. `private/` was not opened |
| Quote check | All 126 quoted passages and quoted facts used below were checked by script as verbatim substrings of the downloaded source texts. Before matching, the script normalised ligatures, whitespace and curly quotes. An ellipsis "..." marks an elision. Thesis page numbers are the roman-numeral front-matter pages |

**Labels.** [stated] marks Dey's own words. [practice] marks what the record shows was done: theses, papers, his web pages, grant abstracts. [observed] marks what students and colleagues say about him. [inferred] marks my inference, not a finding.
**Primary** means Dey's own words or records he produced or controls: his web pages, his syllabus, grant abstracts, papers he co-authored. **Secondary** means other people's accounts of him: thesis acknowledgements, news framing, genealogy databases. A student's acknowledgement is first-hand for the student but secondary evidence about Dey. Student theses play a double role. Their acknowledgements are secondary evidence about Dey's style. Their technical content is a primary record of what the group actually did.

**What the evidence is.** The core corpus is the complete set of 17 PhD theses that Dey lists as "Past PhD Students" on his People page (2012–2025). All are openly downloadable from the Georgia Tech repository, and the handles are given below. Sixteen have acknowledgements; Dubey (2022) has none. Acknowledgements are a genre with strong conventions of gratitude and praise. They show what students chose to emphasise, not a neutral audit (see C3: at least one passage is template-like). I found no lab guide, onboarding document, group-meeting description, student blog post, memorial piece, interview or podcast about his mentoring.

---

## 0. Summary for the synthesizer

- **Group size and structure** [practice, primary]. Dey has 17 PhD graduates (2012–2025). As of October 2026 he has 8 current PhD students and 2 "Post-doc Mentees" (s2). In December 2019 he had "nine advisees" (s12). Nine of the 17 theses are formally co-advised. Co-advisors are chosen by domain: power systems (A. Sun), sustainability (V. Thomas, for Redder's "Power systems for sustainability"), mathematics (Blekherman, School of Mathematics), first-order and nonlinear methods (Lan), and global optimisation (Sahinidis). Marco Molinaro is a standing theory partner.
- **Traits students name most often** [observed, secondary]:
  - Patience: 6 of 16 acknowledgements, 4 of them in sole-Dey theses.
  - Enthusiasm and optimism.
  - Prompt feedback.
  - Humour.
  - Training in explaining ideas simply.
  - Respect for a student's limits and personal life.
- **Adoptive advisor** [observed + practice]. Four theses record a transition into or within his supervision:
  - a switch from another advisor (Monteiro to Dey, Santana);
  - the death of the first advisor (Shabbir Ahmed, 19 June 2019; Gu);
  - "difficult circumstances" (Johnson);
  - a change of research interests (Redder).
- **Craft passes through alumni and shared assets** [practice, primary]:
  - Earlier students help later ones. Kocuk supported Santana's research ("all the technical support"). Later he co-authored with Redder and sat on her committee.
  - An alumnus at Argonne co-authors with a current student: Qiu with Gu.
  - Test instances are reused: Johnson tested on the 300-bus case as modified in Kocuk et al. (2016).
  - An application problem is handed to the next student: Yang Wang's structural model-updating problem went from Santana (2018) to an NSF award (2023–2027) to current student Dahye Han (2026).
- **A tacit habit that lasts a decade** [practice + observed]. Compute small cases exactly with PORTA and write the observed pattern as a *conjecture*. When exact computation blows up, fall back to random-direction "shooting" bounds. This appears in Gupte (2012) and Q. Wang (2016). In 2024 a non-advisee credits Dey with "introducing me to PORTA, one of my new favorite tools".
- **Dey's own words** [stated]. His stated view is student-centred: "In the end, universities are for the students, and I want to assist them in any way I can." The lesson he says he took from his senior colleague Ahmed is persistence plus reframing: Ahmed "would encourage me to stick with it and consider the problem from a different angle."
- **Links to other MINLP-team members** [practice, primary]:
  - Sahinidis co-advised Li (2023) and sat on the committees of Gu (2022) and Shah (2025).
  - Leyffer mentored Li during an Argonne internship.

---

## 1. The group: roster, structure, placement

### R1. All 17 past PhD students [practice, primary: People page s2 + repository metadata s21–s37]

| Year | Student | Thesis (GT repository handle) | Advisor(s) in repository record | First position (Dey's People page) | Ack. |
|---|---|---|---|---|---|
| 2012 | Akshay Gupte | Mixed integer bilinear programming with applications to the pooling problem (hdl 1853/45761) | Ahmed; Dey | Asst. Prof., Clemson (now Lecturer, Edinburgh) | yes |
| 2013 | Feng Qiu | Probabilistic covering problems (1853/47567) | Ahmed; Dey | Postdoc, Argonne (now group leader, Argonne) | yes |
| 2014 | Gustavo Angulo | Integer programming approaches for semicontinuous and stochastic optimization (1853/51862) | Ahmed; Dey | Asst. Prof., PUC Chile, after one year at CORE (now Assoc. Prof.) | yes |
| 2014 | Diego A. Morán R. | Fundamental properties of convex mixed-integer programs (1853/52309) | Dey | Asst. Prof., Virginia Tech (now RPI) | yes |
| 2016 | Burak Kocuk | Global optimization methods for optimal power flow and transmission switching problems in electric power systems (1853/55633) | Dey; X. Andy Sun | Asst. Prof., Sabancı, after one-year CMU postdoc (now Assoc. Prof.) | yes |
| 2016 | Qianyi Wang | Theory and computation of sparse cutting planes (1853/56307) | Dey (thesis thanks "my advisors Prof. Santanu Dey and Prof. Marco Molinaro") | Data Scientist, Uber (now Google) | yes |
| 2017 | Andres Iroume | Sparsity in integer programming (1853/58207) | Dey | Consultant, Revenue Analytics (now Cox Automotive) | yes |
| 2019 | Asteroide Santana | Strong convex relaxations for quadratically constrained quadratic programs (1853/62680) | Dey | OR Scientist, Opex Analytics (now founder, Mip Wise) | yes |
| 2020 | Digvijay Boob | Convex and structured nonconvex optimization for modern machine learning: complexity and algorithms (1853/63673) | Guanghui Lan; Dey | Asst. Prof., SMU | yes |
| 2021 | Guanyi Wang | Approximation algorithms for mixed integer non-linear optimization problems (1853/64724) | Dey | Asst. Prof., NUS, after one-year postdoc with A. Lodi (Polytechnique Montréal) | yes |
| 2021 | Emma S. Johnson | Solution techniques for large-scale optimization problems on the transmission grid (1853/66178) | Dey | Sandia National Laboratories | yes |
| 2022 | Xiaoyi Gu | Topics in mixed integer nonlinear optimization (1853/67235) | Dey | Quantitative Researcher, SIG | yes |
| 2022 | Yatharth Dubey | Novel analysis of the branch-and-bound method for integer programming (1853/67247) | Dey; Marco Molinaro | Asst. Prof., UIUC, after one-year CMU postdoc with G. Cornuéjols (now Applied Scientist, Amazon) | **none** |
| 2023 | Shengding Sun | Some global relaxation methods for quadratic and semidefinite programming (1853/72665) | Grigoriy Blekherman; Dey | Research associate, DAMTP, Cambridge | yes |
| 2023 | Yijiang Li | Decomposition algorithms for certain integer problems over networks (1853/72737) | Nikolaos Sahinidis; Dey | Postdoc, Argonne | yes |
| 2025 | Prachi Shah | Closing the gap: a theoretical and practical exploration of branch-and-bound procedure for mixed-integer programs (1853/77883) | Dey | Applied Scientist, Amazon | yes |
| 2025 | Nicole Redder | Power systems for sustainability (1853/78723) | Dey; Valerie M. Thomas | (not listed) | yes |

Counts from the table:
- **Co-advising.** 9 of 17 theses are formally co-advised: Ahmed ×3, A. Sun, Lan, Molinaro, Blekherman, Sahinidis, V. Thomas. The other 8 are sole-advised, but one of them (Q. Wang) thanks Molinaro as a co-advisor (see C1).
- **First positions.** 7 faculty posts, 4 of them after a one-year postdoc (Angulo at CORE, Kocuk at CMU, G. Wang at Polytechnique Montréal, Dubey at CMU). 3 national-laboratory posts (Argonne ×2, Sandia). 1 university research post. 5 industry posts. 1 not listed.

### R2. Current group, October 2026 [practice, primary, s2]
- Post-doc mentees: Anna Deza, Jisun Lee.
- PhD students: Xiangxin An, Fabian Badilla, Berkay Becu, Sourabh Choudhary, Dahye Han, Apoorva Narula, April Niu, Jingye Xu.
- In December 2019, GT news reported "He currently has nine advisees." (s12). So the group holds steady at about 8–9 PhD students.

### R3. He keeps a public record of where alumni went [practice, primary, s2]
For each alum the People page lists thesis title, graduation year and first position, usually the current position, and any postdoc detour with its host. Example: "after spending one year at Carnegie Mellon University as a Postdoctoral researcher working with Prof. G. Cornuejols". [inferred] He treats placement as part of the advising record. The motive is not stated.

### R4. Genealogy databases undercount the group [observed, secondary, s18 s19]
- The Mathematics Genealogy Project (MGP id 119146) lists only 5 students: Angulo, Gupte, Hojny, Kocuk, Sun.
- MGP lists Dey as "Advisor 3" for Christopher Hojny (Dr. rer. nat., TU Darmstadt 2018, "Symmetries in Binary Programs - A Polyhedral Perspective"; Advisors 1–2 are Marc Pfetsch and Volker Kaibel).
- Hojny is not on Dey's People page. Dey's role (perhaps external referee) is **not confirmed**: the TUprints search returned nothing.

---

## 2. Supervision style as students describe it [observed, secondary]

Most co-advised acknowledgements credit the pair ("their"), so the trait cannot be assigned to Dey alone. This applies to Gupte, Qiu and Angulo (with Ahmed), Kocuk (with Sun), Q. Wang (with Molinaro), S. Sun (with Blekherman) and Li (with Sahinidis). Boob is the exception: he describes his two advisors separately. Lan "was always patient and kind with me, especially in the beginning of my PhD when I was getting introduced to advanced concepts in nonlinear optimization." Dey's part is in S5 (Boob 2020, p. iv, s29).

**S1. Patience. This is the most frequent trait (6 of 16 acknowledgements).**
- According to Morán (2014, sole advisor; p. iii, s24): "Without his guidance, enthusiasm, optimism and infinite patience, this thesis would have not been possible."
- According to Iroume (2017, sole; p. v, s27): "I am tremendously grateful for Santanu’s dedication and his patience, without which, this thesis would never have been finished."
- According to Santana (2019, sole; p. iv, s28): "I am thankful also for your patience, when I made mistakes or had computational bugs, and for your willingness to shift research direction to meet my goal of working closer to the application."
- According to G. Wang (2021, sole; p. iv, s30), Dey is thanked "for his kindness, patience, enthusiasm, and immense knowledge".
- Jointly with Ahmed, according to Qiu (2013; p. iv, s22): "I am eternally grateful for their patience and dedication as I progressed from a novice researcher, coming back to school after years of work in industry, to a seasoned researcher."
- Jointly with Molinaro, according to Q. Wang (2016; p. iv, s26): "for their patience, professional attitude and immense knowledge".

**S2. Enthusiasm, "crazy research ideas", seriousness.** Era: 2009–2014, when Dey was a new assistant professor.
- According to Morán (2014; p. iii, s24): "I am extremely happy I decided to start working with him on his crazy research ideas during my first semester at Georgia Tech; in spite of him being “only” a new assistant professor (now associate professor!), being unknown by the integer programming community (according to him, not to the community, of course :))". On Dey's early website photo he adds: "(none of which resulted true, except that he is a very serious researcher!)".
- Jointly with Ahmed, according to Qiu (2013; p. iv, s22): "Their brilliant insights into research, their relentless enthusiasm for exploring the unknown, and their persistence at solving difficult problems are traits that I strive to emulate."

**S3. Treated as a colleague, with fast turnaround.**
- Jointly with A. Sun, according to Kocuk (2016; p. iii, s25): "They always treated me as a colleague rather than a student. I appreciate their diligent and prompt feedback to my research, without which, I would not have had such a productive dissertation work in three years."
- Kocuk's power-systems papers with Dey and Sun include Operations Research 2016 (DOI 10.1287/opre.2016.1489, s55).

**S4. A calibrated push and explicit expectations.** This is weakened by C3 (template reuse).
According to Santana (2019; p. iv, s28):
- "During the nearly four years we have worked together, you always offered encouragement, guiding me to the edge of my productivity, yet respected my limitations, motivations, and personal life."
- "Over time, we exchanged feedback, improved communication of our expectations, and built a collaborative relationship, for which I am deeply grateful."
- "Besides teaching me how to do research and write papers, you helped me to be more professional, aim for the highest standards, understand the importance of seeking the big picture, set priorities, and develop many other skills now part of my personality."

**S5. Training in plain explanation.**
- Jointly with Lan, but this sentence is about Dey alone, according to Boob (2020; p. iv, s29): "Santanu has always been mentoring me through different phases of my PhD life and being with him has trained me on how to convey complex ideas in simple words."

**S6. Ideas exchanged on walks.**
- According to G. Wang (2021; p. iv, s30): "I am fortunate to have many research discussions and walkings with him around campus, during which he shared some exciting research ideas."

**S7. Humour, and meetings that motivate.**
- According to Shah (2025; p. iii, s36): "I am eternally grateful to my advisor, Santanu Dey, for all that you have taught me about research, life, and everything in between. Your jokes have always lifted my spirits, especially during stressful times, and I have always left our meetings feeling more motivated and inspired."
- Jointly with Sahinidis, according to Li (2023; p. v, s35): "I especially enjoyed their passion and intellectual depth during our meetings and their lighthearted sense of humors outside of work."

**S8. Disagreement is absorbed, not suppressed.** Era: 2019–2021, including the pandemic.
- According to Johnson (2021; p. iii, s31): "thank you to my advisor, Santanu Dey, for becoming my advisor under difficult circumstances, weathering uncountably many arguments, and most of all, being supportive, gentle, and motivating through everything (including a pandemic)."

**S9. Hands-on coaching for talks.** Era: 2009, within months of Dey joining Georgia Tech on 1 July 2009 (s15).
- Jointly with Ahmed, according to Qiu (2013; p. iv, s22): "The image of their sitting together with me in the lounge of the Hilton San Diego Bayfront Hotel in 2009, helping me correct my INFORMS presentation slides, is still as fresh as it was then."

**S10. Development of the whole person.**
- According to Morán (2014; p. iii): "I really have no words in English (or Spanish) to describe how grateful I am for everything I have learned from Santanu in all aspects of academic life in these 5 years in the Ph.D. program."
- Jointly with Molinaro, according to Q. Wang (2016; p. iv): "I not only learned how to be an excellent researcher, but also learned how to be a better person."
- Jointly with Blekherman, according to S. Sun (2023; p. iv, s34): "They have introduced me to different aspects of mathematical optimization, the research community, and the whole world of academia."
- Shah's "research, life, and everything in between" (S7) belongs here as well.

**S11. Material support and career direction.**
- According to Santana (2019; p. iv): "I acknowledge your financial support, which significantly improved the quality of life of my family."
- Jointly with Ahmed, according to Gupte (2012; p. iv, s21): "They have provided invaluable advice while conducting research and inspired me to pursue an academic career."

**S12. Adoptive advisor, flexible on direction** [observed + practice].
- Santana (2019; p. v) moved from Renato Monteiro, his first-year advisor. He thanks Monteiro for his "willingness to allow me to pursue new research opportunities", and thanks Dey for the "willingness to shift research direction" quoted in S1.
- Gu (2022; p. iv, s32): "I would like to thank late Dr. Shabbir Ahmed. As my advisor, he guided me through my first years as a Ph.D. student." Of Dey he writes: "His wisdom guided me through the challenges of this academic life, and his support helped me through many difficult times." Ahmed "passed away on June 19, 2019" (s13).
- Johnson (2021) thanks Dey "for becoming my advisor under difficult circumstances" (S8). She does not say what the circumstances were. Her chapter 2 work "is in collaboration with Shabbir Ahmed, Santanu Dey, and Jean-Paul Watson" (arXiv:2003.10565, s67). [inferred, unconfirmed] The circumstances may be related to Ahmed's death.
- Redder (2025; p. iii, s37): "my advisor Santanu, who supported me through the hardest years of the program and a change in research interests; my advisor Valerie, who joined later on to help me find projects and data in my field of interest".
- [inferred] Taking on students in transition is a recurring part of his advising: 4 of 17 theses document it.

**S13. What non-advisees say: teaching, job market, peer mentoring** [observed, secondary]
- **Teaching.**
  - Panageas (2016, s39): "Last but not least I would like to thank Santanu Dey for being a great instructor, always being there to answer my questions."
  - Ojha (2024, s43): "I want to thank Santanu Dey and Alejandro Toriello for teaching me discrete optimization, which will always remain my favorite course."
  - Boone (2026, s47) thanks a list of faculty, Dey among them, "for their incredible teaching and mentorship throughout my graduate career."
- **Course into research.** Greening (2024, s38): "Santanu, I genuinely appreciate you welcoming me into the world of integer programming (both in class and later in research), and for introducing me to PORTA, one of my new favorite tools." See T1.
- **Job-market help, three independent theses over seven years.**
  - Q. He (2013, s41) thanks a list including Dey "for all the support and advices during my job search."
  - W. Xie (2017, s40) thanks a list headed by Dey "for their great help with my job search."
  - Y. Yang (2020, s42) thanks four professors, Dey among them, "for their support for my academic job search."
- **Peer mentoring as a junior professor.** Dadush (2012, CS-side PhD, advisor Vempala; s44) thanks Dey and Vielma "for countless conversations about life, research, and all that jazz, and for being great friends and collaborators." A chapter of that thesis "is based on joint work with Santanu Dey and Juan Pablo Vielma which appeared in the proceeding of the conference on Integer Programming and Combinatorial Optimization, 2011". That is IPCO 2011, LNCS, DOI 10.1007/978-3-642-20807-2_11 (s79).
- **Committee help beyond the thesis.** S. Zhang (2022, s48), of the whole committee: "They have been of great assistance not only for my dissertation, but also for many other things about my research or my academic career."
- **Advice to a competition team led by a colleague.** Gholami (2021, advisor A. Sun; s45) was on the team Sun led in the ARPA-E Grid Optimization competition. He writes: "I must also thank Professor Santanu Dey and Professor Pascal Van Hentenryck for their constructive interactions."

---

## 3. What Dey says about mentoring [stated]

- **D1. On becoming Associate Chair for Graduate Studies** (GT news, created 2019-12-18; Dey quoted, article secondary; s12).
  - Dey's own words:
    - "I have always enjoyed engaging with graduate students – talking with them about their goals, their career plans, and their research,"
    - "This new role will be a good way for me to continue connecting with them and helping them to achieve everything they’re working so hard for."
    - "In the end, universities are for the students, and I want to assist them in any way I can."
    - "Georgia Tech is a challenging educational institution, and we need to make sure that students receive the help they need when they need it,"
  - The article adds that his focus "includes opportunities for increased financial support, as well as reinforcing areas like mental health services".
  - His "term as ACGS begins with the 2020 spring semester". In 2026 his homepage gives his role as "Anderson-Interface professor and director of doctoral recruiting and admissions" (s1).
- **D2. How he says he was mentored** (ISyE memorial for Shabbir Ahmed, 2019-07-01; Dey quoted as "associate professor"; s13): "As a junior ISyE faculty member, working with Shabbir broadened my thinking about solving problems in discrete optimization. I would be working through a particularly difficult problem, and he would encourage me to stick with it and consider the problem from a different angle. He always made me feel like I could succeed."
  - Dey and Ahmed co-advised Gupte, Qiu and Angulo (R1).
  - Qiu's joint description of both advisors includes "persistence at solving difficult problems" (S2).
- **D3. Educational plan in his NSF CAREER award** (award 1149400, 2012–2017; s8): "The key educational objective of this award is to develop an outside-classroom operations research puzzle competition to foster and enrich an environment for undergraduate research. Moreover a new graduate course will be designed with the aim of dissemination of research results directly to future practitioners and to bring students from different engineering communities together, thus providing opportunities for new research directions and collaborations."
  - Whether either plan was carried out is **not verified** (Gaps).
- **D4. One student per grant** (NSF award 1562578, Sparse Integer Programming, 2016–2020; s9): "This project will support and train one PhD student who will be involved with all aspects of the research and dissemination of the results." This shows the resource context: one funded PhD student per single-investigator grant.
- **D5. PhD-course expectations** (ISyE 6661 syllabus, Fall 2020; s5): "This is a PhD level class, you are expected to be thoroughly comfortable with undergraduate calculus and analysis, and basic proof techniques."
  - That semester's lectures were "remote asynchronous" because of the pandemic. Homework includes "possibly computational exercises".
  - His site lists 45 recorded linear-programming lectures (s4). Some titles are motivation-first, for example "Lecture 9 - What do optimal solutions look like" and "Lecture 10 - Why bother about extreme points". [practice, primary]
  - The homepage lists "Class of 1969 Teaching Fellow, Center for the Enhancement of Teaching and Learning (CETL), Georgia Institute of Technology 2010." (s1)
  - Teaching beyond his own students: a 136-frame tutorial, "Convexification in global optimization", for the IPCO 2020 summer school (June 2020; s7). The content is technical, with no advice to students; it belongs to notes 02 and 03.

---

## 4. Group habits and lab culture [practice unless labelled]

**H1. Co-advisors chosen by domain** (R1; s21–s37). There are four patterns.
- **Senior colleague.** In his early career he co-advised with Ahmed (3 of the first 4 graduates, 2012–2014). In 2012 Gupte still calls him "Asst. Prof. Santanu Dey" (s21).
- **Application expert.**
  - X. Andy Sun for power systems (Kocuk). By 2023 Sun is listed at MIT's School of Management (S. Sun's committee page, s34).
  - Valerie Thomas (ISyE) for Redder's sustainability topic.
  - Yang Wang (School of Civil and Environmental Engineering, per s49 and s50), first as collaborator for Santana and later as PI of NSF 2211343 (s10).
- **Mathematician.** Blekherman (School of Mathematics, per s34) for S. Sun.
- **Methods colleague.** Lan for first-order and nonlinear methods (Boob). Sahinidis (ISyE) for global optimisation (Li).

**H2. A standing theory partner, Marco Molinaro, supervising remotely later on.**
- Q. Wang (2016) thanks "my advisors Prof. Santanu Dey and Prof. Marco Molinaro" (s26). Paper: arXiv:1601.00198 (s63).
- Iroume (2017; p. v) describes Molinaro as "a fundamental part of most of the work in this thesis, both during his time in Georgia Tech as well as later on" (s27).
- Dubey's committee page (2022) lists "Dr. Marco Molinaro Computer Science Department Pontifical Catholic University of Rio de Janeiro" (s33). [inferred] Co-supervision continued across continents.
- Later papers with Molinaro:
  - Dubey: arXiv:2007.15192 (s71).
  - Dubey and Shah: arXiv:2110.10754 (s72). Shah writes: "Marco Molinaro, it is always a pleasure to work with you." (s36)
  - G. Wang: arXiv:2010.11152 (s66).
  - S. Sun with Blekherman: arXiv:2002.02988 (s75).

**H3. Alumni loops and senior-to-junior mentoring.**
- Kocuk to Santana. Santana (2019; p. iv): "Burak Kocuk for your contributions to our research, your kindness, all the technical support, and sharing with me your inspirational way of thinking and solving problems." [observed]
- Kocuk to Redder. Kocuk sits on Redder's committee as "Dr. Burak Kocuk Industrial Engineering Program Sabancı University". Redder writes: "Burak, whose paper I contributed to as the first published work of which I was a part". The paper is Dey, Kocuk, Redder, *Discrete Optimization* 2022, DOI 10.1016/j.disopt.2021.100683 (s57).
- Qiu (alumnus, Argonne) to Gu. Gu's fourth chapter is joint with Dey, Qiu and Á. S. Xavier: arXiv:2208.10028 (s70).
- Alumni with each other: Kocuk and Morán, SIAM J. Optim. 2019, DOI 10.1137/18m1210812 (s58).
- Shared instances. Johnson tests "on the 300-bus test system as modified in Kocuk, Jeon, et al. (2016)" (s31). That instance comes from Kocuk, Jeon, Dey, Linderoth, Luedtke, Sun, *Operations Research* 2016, DOI 10.1287/opre.2015.1471 (s56).

**H4. Application lines handed down across student generations.**
- **Structural model updating (Yang Wang, School of Civil and Environmental Engineering).**
  - Santana (2019; p. iv) thanks "Professor Yang Wang for introducing us to the Finite Element Updating Model Problem".
  - Paper: Dey, Santana, Wang, *Optimization and Engineering* 2018, DOI 10.1007/s11081-018-9402-9 (s59).
  - NSF award 2211343 (2023–2027; PI Y. Wang, co-PI Dey) studies "convex relaxation and branch-and-bound algorithms that can guarantee global optimality toward solving non-convex model updating problems" (s10).
  - Dey, Han, Wang, *J. Global Optim.* 2026, DOI 10.1007/s10898-026-01607-8 (s61). Dahye Han is a current PhD student (s2).
  - Dey also sat on the committees of Y. Wang's students X. Dong (2019, s49) and T. Schreiber (2025, s50).
- **Power transmission switching.** Kocuk (2016) to Johnson (2021) to Redder (2025): see H3 and s57.
- [inferred] A student's wish to work "closer to the application" (Santana) became a funded line that outlived the student.

**H5. Internships and partners outside academia.**
- Gupte had an ExxonMobil summer internship; his research was funded by "ExxonMobil Corporate Strategic Research" (s21). The paper Gupte, Ahmed, Cheon, Dey (SIAM J. Optim. 2013, DOI 10.1137/110836183, s52) has an ExxonMobil co-author.
- Angulo's vita: "Under the supervision of Shabbir Ahmed and Santanu Dey, he collaborated with ExxonMobil". He also interned at Kimberly-Clark (s23).
- Morán: "during my summer internship at IBM Research Watson" (s24).
- Johnson's Sandia colleagues are co-authors of a thesis chapter: "in collaboration with Santanu Dey, Jonathan Eckstein, Cynthia Phillips, and John Siirola" (s31).
- Li interned at Argonne and Amazon and names Sven Leyffer (s35).
- Shah writes of collaborator Arvind Raghunathan: "I have grown both as a researcher and professional under your mentorship" (s36).
- [inferred] Internships with industry or national laboratories are a normal part of a PhD in this group. No stated policy was found.

**H6. Students teach alongside him** [observed].
- Santana (2019; p. vii) thanks "Dr. Dawn Strickland, Timur Tankayev, Beste Basciftci, and Professor Santanu Dey for your companionship while teaching the Engineering Optimization course in fall 2018. Because of your enjoyable companionship, grading 200 exams was surprisingly one of the most entertaining parts of teaching the course." Dey's teaching page lists ISyE 3133 Engineering Optimization in Fall 2018 (s3).
- Non-advisee Y. Yang (2020): "Many thanks go to Professor Santanu Dey for making being an instructor of the course ISyE 3133-Engineering Optimization an amazing experience" (s42).

**H7. Author order is not uniform; no stated policy was found.**
- **Alphabetical:**
  - Dey, Iroume, Molinaro, Salvagnin (SIAM J. Optim. 2018, DOI 10.1137/16m1095962; arXiv:1609.08121; s62).
  - Dey, Dubey, Molinaro, Shah (arXiv:2110.10754).
  - Dey, Shah (arXiv:2112.03965; s73).
  - Blekherman, Dey, Sun (arXiv:2210.01722; s74).
  - Dey, Mazumder, Wang (arXiv:1810.09062; s64).
  - Dey, Kocuk, Redder (s57).
  - Dey, Santana, Wang (s59).
- **Student first:**
  - Kocuk, Dey, Sun (s55).
  - Santana, Dey (SIAM J. Optim. 2020, DOI 10.1137/19m1277333; s60).
  - Gu, Ahmed, Dey (SIAM J. Optim. 2020, DOI 10.1137/19m1271695; s68).
  - Gu, Dey, Richard (s69).
  - Johnson, Ahmed, Dey, Watson (s67).
  - G. Wang, Dey (ICML 2020; s65).
  - Gupte, Ahmed, Cheon, Dey (s52).
  - Qiu, Ahmed, Dey, Wolsey (s53).
  - Morán R., Dey, Vielma (SIAM J. Optim. 2012, DOI 10.1137/110840868; s54).
- The same student's work can appear both ways (C5).

**H8. Rewriting after the conference version.**
- Dubey (2022, ch. 2; s33): "An earlier version of this paper is published in the conference SODA [10]. The current paper is a significant improvement over [10]. Although the main result (Theorem 1) is the same, we have significantly simplified the proofs".
- G. Wang (2021, ch. 2; s30): "We note that a preliminary version of this paper was published in [68]. The current version has many new results, in particular CR1 and results on its strength are completely new, and the numerical experiments have also been completely revamped."
  - Ref. [68] is G. Wang and S. Dey, "Upper bounds for Model-Free Row-Sparse Principal Component Analysis", ICML 2020, PMLR 119:9868–9875 (s65).
  - The expanded version adds Molinaro and switches to alphabetical order (arXiv:2010.11152, s66).

**H9. Student paper competitions** (one documented instance). Angulo's vita: "In 2013 he obtained an honorable mention in the George Nicholson Student Paper Competition from INFORMS." Dey himself lists "First place, Nicholson student paper competition, INFORMS 2007." on his homepage (s1, s23). [inferred] There may be a habit of entering students; one case is not enough to claim it.

**H10. A postdoc year before a faculty job.** Four of seven faculty placements followed a one-year postdoc (R1, s2). [inferred] This may reflect his career advice; no advice text was found.

**H11. Meetings.** Students mention one-to-one "meetings" (Shah, Li) and walks (G. Wang). **No description** of group meetings, reading groups or a weekly rhythm was found (see Gaps).

**H12. Links to other MINLP-team members** [practice, primary].
- Sahinidis co-advised Li (2023). He also sat on the committees of Gu (2022) and Shah (2025). Shah: "Nick Sahinidis, your class helped me improve my computational skills, and your insights into solvers have been invaluable." (s32, s35, s36)
- Leyffer mentored Li at Argonne. Li: "I am grateful to my mentors and colleagues during my internships at Argonne National Laboratory and Amazon. In particular, I thank Sven Leyffer" (s35).

---

## 5. Tacit knowledge: what the students know but the papers do not say

Each item gives who reports it and where. All are secondary unless marked as a group-record practice.

- **T1. Compute small cases exactly, then write a conjecture; when exact computation fails, bound by "shooting".** [practice, from student theses as group records + observed]
  - Gupte (2012, ch. 3, before §3.7; s21): "Based on PORTA [32] experiments, we find that inequalities (90) along with variable bounds seem to be sufficient to characterize the convex hull of K(α, b), for all integers α ≥ 2 and all integers b." This is followed by "Conjecture 3.1" rather than a theorem.
  - Q. Wang (2016; s26) uses PORTA to get inequality descriptions. He then reports: "Unfortunately due to the large number of inequalities, we are unable to find the vertices". So the group bounds the distance "via a shooting experiment" ("We generated 20,000 random directions").
  - According to Greening (2024, non-advisee; s38), Dey introduced her to PORTA (S13).
  - Era: the habit spans 2012–2024, so it is not outdated within this group.
- **T2. Build your own prototype on commercial engines, and keep refinements that matter.** [practice; one thesis]
  - Santana (2019, ch. 3; s28): "We use Gurobi as LP solver and run IPOPT at each node to search for feasible solutions."
  - On extra tangent cuts: "More tangent lines could be added to better approximate conv(S0), but based on our preliminary experience on our instances it does not make significant difference."
- **T3. Report surprising and null computational findings plainly.** [practice; one thesis; whether this comes from Dey is unknown]
  - Johnson (2021, ch. 2; s31): "Surprisingly, the best solutions do not tend to be among the closest".
  - Also: "the superiority in performance is not statistically significant".
- **T4. Treat the conference version as a draft.** Simplify proofs, add results and redo experiments for the journal version (H8; Dubey and G. Wang).
- **T5. Rehearse and fix talk slides with the advisor before the conference** (Qiu, S9; 2009).
- **T6. Practise explaining complex ideas simply** (Boob, S5).
- **T7. Persist, then change the angle.** This is Dey's own account of what he learned from Ahmed (D2). Qiu's description of both advisors' "persistence at solving difficult problems" matches it.
- **T8. Reuse the group's instances and lines of work** rather than starting from scratch (H3, H4).
- **T9. Set expectations explicitly and revisit them** (Santana, S4). This item is weak because of C3.

---

## 6. Failures, pivots, difficulties

There are **no** rejected papers, retractions or abandoned group projects documented in the 17 theses or on his pages. What the record does show is difficulty and change on the student side:

- **F1. Santana: pivot and setbacks.** He moved away from his first advisor. Dey then agreed to shift his research direction to meet his goal of working "closer to the application" (S1, S12). He writes of "sometimes seeing my research going backwards rather than progressing" (p. vi). [observed]
- **F2. Redder: change of interests.** She changed research interests, and a second advisor joined later "to help me find projects and data in my field of interest" (S12). [observed]
- **F3. Johnson: unresolved results.**
  - She thanks her committee: "Thank you also to my committee members: Your ideas have improved this thesis greatly, (and, in the chapter on transmission switching, added to the mystery)."
  - In the kNN chapter, the premise that the best solutions come from the nearest neighbours did not hold (T3). [practice]
- **F4. Gu: death of the first advisor.**
  - The Gu, Ahmed, Dey paper was posted on 2019-07-01 (arXiv:1907.00920), twelve days after Ahmed's death (s13). It was published with Ahmed as co-author in SIAM J. Optim. 2020 (DOI 10.1137/19m1271695, s68).
  - Gu's thesis: "The first chapter is a joint work with Dr. Shabbir Ahmed and Dr. Santanu S. Dey." [practice]
- **F5. Iroume: a hard finish.**
  - He says the thesis "would never have been finished" without Dey's patience (S1).
  - His feasibility-pump chapter "was submitted to SIAM Journal on Optimization ... on September 30th, 2016" and appeared in 2018 (DOI 10.1137/16m1095962). [practice]
- **F6. Dubey: from academia to industry.** He took a faculty post at UIUC and is now an Applied Scientist at Amazon. Dey's page records this neutrally (s2).
- **F7. A stated plan with no visible outcome.** No evidence was found that the CAREER puzzle competition (D3) ran.

---

## 7. Lineage: how Dey was mentored, and where that reappears

- **L1. PhD advisor: Jean-Philippe P. Richard, Purdue 2007.** Dissertation "Strong Cutting Planes for Unstructured Mixed Integer Programs Using Multiple Constraints" (MGP, s18). [practice]
  - Papers with Richard: *Math. Oper. Res.* 2008, DOI 10.1287/moor.1070.0283 (s76); *INFORMS J. Comput.* 2009, DOI 10.1287/ijoc.1080.0284 (s77).
  - Richard later co-authors with Dey's student Gu: IPCO 2021 (DOI 10.1007/978-3-030-73879-2_11), *Math. Program.* 2022 (DOI 10.1007/s10107-021-01759-3) and *INFORMS J. Comput.* 2024 (DOI 10.1287/ijoc.2022.0230) (s69).
  - Gu's thesis: "The second and third chapters are joint works with Dr. Santanu S. Dey and Dr. JeanPhilippe P. Richard." That makes three academic generations on one line of work.
  - How Dey describes Richard's mentoring is **not read**: his own thesis acknowledgements were not accessible.
- **L2. Postdoc at CORE (Louvain).** GT news: "Since 2007, Dey has worked as a research fellow at the Center for Operations Research and Econometrics (CORE)" (s15). Paper: Dey and Wolsey, *Math. Program.* 2010, DOI 10.1007/s10107-010-0362-x (s78).
  - Later Qiu, Ahmed, Dey and Wolsey (*INFORMS J. Comput.* 2014, DOI 10.1287/ijoc.2013.0582, s53). Qiu thanks Wolsey "whose frank advice and clever suggestions considerably enhanced the quality of my work". Angulo spent a year at CORE before his faculty job (s2).
  - **Caveat:** Wolsey also taught at Georgia Tech in those years. Morán thanks "L. Wolsey" for "fun and challenging classes", and Q. He thanks "Laurence Wolsey, for teaching me lot-sizing" (s24, s41). So the link need not have run through Dey. [inferred, kept open]
- **L3. As a junior professor, mentored by Ahmed** (D2), with whom he co-advised three students. He now holds the "Anderson-Interface professor" title (s1); Ahmed was "the Anderson-Interface Chair and professor" (s13, s16). The fact is recorded; no meaning is inferred from it.
- **L4. Early peer mentoring of a CS-side PhD student** (Dadush, S13). Papers: Dadush, Dey, Vielma, IPCO 2011 and *Math. Oper. Res.* 2011 (DOI 10.1287/moor.1110.0488) (s79).

---

## 8. Era and resource context

| Period | Dey's position (source) | Graduates | Co-advisors and partners | Funding and partners named | Solvers and tools mentioned in the theses* |
|---|---|---|---|---|---|
| 2009–2014 | Assistant professor from 2009-07-01 (s15); "Asst. Prof." in 2012 (s21); "now associate professor!" in 2014 (s24) | Gupte, Qiu, Angulo, Morán | Ahmed (3 of 4); Wolsey (Qiu); IBM Research internship (Morán) | ExxonMobil (Gupte, Angulo); NSF convex MINLP 2010–2014 (s11); NSF CAREER 2012–2017 (s8) | CPLEX (Gupte, Qiu, Angulo), BARON and PORTA (Gupte) |
| 2015–2019 | Associate professor; promotion to professor announced 2019-03-18 (s14); still "associate professor" in the July 2019 memorial (s13) | Kocuk, Q. Wang, Iroume, Santana | A. Sun (Kocuk); Molinaro (Q. Wang, Iroume); Y. Wang (Santana) | NSF CAREER; NSF Sparse IP 2016–2020, "one PhD student" (s9) | CPLEX and BARON (Kocuk); CPLEX and PORTA (Q. Wang); Python, Gurobi and IPOPT (Santana) |
| 2020–2025 | Professor; Associate Chair for Graduate Studies from spring 2020 (s12); by 2026, Anderson-Interface professor and director of doctoral recruiting and admissions (s1); pandemic years | Boob, G. Wang, Johnson, Gu, Dubey, S. Sun, Li, Shah, Redder | Lan, Blekherman, Sahinidis, V. Thomas, Molinaro (at PUC-Rio by 2022), Richard; Sandia, Argonne, Amazon | DOE, ONR, AFOSR, Argonne and Sandia contracts, NSF with Y. Wang (s6, s10); DOE (Li); Net Zero Freight (Redder) | Gurobi (Gu, Johnson, Li, G. Wang, Shah), MOSEK (G. Wang), SCIP (Li, Shah), Julia/JuMP (Gu, Li), Pyomo (Johnson, Li) |

*Tool names were counted as string occurrences in the thesis texts. This is a rough signal, not a usage audit. The shift from CPLEX to Gurobi and SCIP follows the wider field's tooling. It is not presented here as a choice Dey made.

Seniority caveat for transfer to the skill:
- **Senior-only.** The adoptive-advisor pattern, the two graduate-program roles, the co-advising network and multi-funder support rest on seniority and a large department.
- **Portable at any career stage.** PORTA small-case computation, prompt feedback, coaching on talk slides and post-conference rewrites.

---

## 9. Mapping to the seven layers (for Phase 2)

| Layer | What this note contributes | Evidence strength |
|---|---|---|
| 1 Taste | "aim for the highest standards", "seeking the big picture" (S4, weakened by C3); "a very serious researcher" (S2) | weak |
| 2 Problem choice | "crazy research ideas" offered to a first-semester student (S2); willingness to move a student toward applications or a new interest (S12); application problems brought in through domain partners (H4) | medium |
| 3 Idea generation | ideas shared on walks (S6); small-case PORTA computation turned into a conjecture (T1) | medium |
| 4 Execution | own prototypes on commercial solvers (T2); reused instances (H3); shooting-experiment fallback (T1) | medium |
| 5 Judging results | a computational pattern stated as a conjecture, not a theorem (T1); surprising and null results reported (T3) | weak (2 theses) |
| 6 Expression | slide coaching (S9); plain explanation (S5); "how to do research and write papers" (S4); post-conference rewrites (H8) | medium |
| 7 Research organisation | co-advising by domain (H1); standing theory partner (H2); alumni loops (H3); adoptive advising (S12); placement record (R3); graduate-program roles (D1) | strong for structure, medium for style |

---

## Contradictions (kept, not reconciled)

- **C1. Formal and actual co-advising differ.**
  - The repository record lists Dey as the only advisor of Q. Wang (2016). The thesis thanks "my advisors Prof. Santanu Dey and Prof. Marco Molinaro" (s26).
  - Iroume's record also lists only Dey, but the thesis makes Molinaro "a fundamental part of most of the work" (s27).
- **C2. The genealogy record and Dey's own list disagree.**
  - MGP lists 5 students; Dey's page lists 17.
  - MGP lists Hojny (TU Darmstadt 2018) as Dey's student; Dey's page does not (s2, s18, s19).
- **C3. One acknowledgement passage looks like a template.**
  - Santana (2019) wrote about Dey: "Besides teaching me how to do research and write papers, you helped me to be more professional, aim for the highest standards, understand the importance of seeking the big picture, ..." and "Over time, we exchanged feedback, improved communication of our expectations, and built a collaborative relationship".
  - Cabral (2023) wrote about his advisor Andy Sun: "In addition to teaching me research skills and paper writing, he has helped me become more professional and strive for excellence, recognize the significance of a bigpicture perspective, and develop many other skills that have become integral parts of my personality. Over time, we have established a collaborative relationship built on mutual feedback, improved communication, and expectations, which I sincerely appreciate." (s46)
  - Both statements are kept. The overlap lowers the weight of these phrases as evidence of anything specific to Dey.
- **C4. Self-description versus the record.** Morán reports Dey describing himself as "unknown by the integer programming community (according to him, not to the community, of course :))". His own homepage lists a 2007 INFORMS Nicholson first prize, and the 2009 GT news cites a forthcoming *Math. Oper. Res.* paper (s1, s15). This is a humorous, second-hand self-assessment and is left as is.
- **C5. Author order** is alphabetical in some student papers and student-first in others, sometimes for the same student. G. Wang appears first on the ICML 2020 paper (s65) and last (alphabetical) on the expanded arXiv version (s66).
- **C6. Rank in 2019.** News of the promotion to professor appeared on 2019-03-18 (s14), but the 2019-07-01 memorial still calls him "associate professor" (s13). The effective date is probably the explanation; this is not confirmed.
- **C7. Errors in thesis citations** (evidence hygiene).
  - Kocuk's thesis reference [59] gives arXiv:1411.0359 for the Kocuk–Dey–Sun AC transmission-switching paper. That id is actually NESTA by Coffrin, Gordon and Scott (s80), so it must not be reused.
  - Titles of several arXiv records have changed since the theses cited them. arXiv:1810.09062 is now "Using L1-relaxation and integer programming to obtain dual bounds for sparse PCA". arXiv:2007.15192 is now "Branch-and-Bound Solves Random Binary IPs in Polytime". arXiv:2010.11152 is now "Solving sparse principal component analysis with global support". Cite the current records.

---

## Gaps (searched, not found)

- **G1.** No student blog post, memorial piece, lab guide, onboarding document, group page beyond the People list, collaborator interview or podcast was found. Of the two WebSearch calls, the first turned up only the 2019 Associate Chair news item and the second nothing relevant. The site of Santana's company Mip Wise was checked (s20) and has no recollection of Dey.
- **G2.** Dubey's deposited thesis has no acknowledgements. The 8 current students and 2 postdoc mentees have no public accounts.
- **G3.** Dey's own PhD thesis (Purdue 2007) was **not read**: Purdue e-Pubs returned HTTP 403 and OpenAlex was rate-limited. How he describes Richard's mentoring is therefore unknown.
- **G4.** The INFORMS Optimization Society's 2020 Egon Balas Prize citation was not found. The INFORMS page lists only the winner (s17).
- **G5.** Whether the CAREER plans (puzzle competition, new graduate course; D3) were carried out is unverified. His teaching page lists "ISyE 8813-DEY Global Optimization (Fall 2024)", but nothing links it to the CAREER plan.
- **G6.** Dey's role in Hojny's TU Darmstadt thesis is unconfirmed.
- **G7.** No collaborator-side accounts were found from Molinaro, A. Sun, Blekherman, Sahinidis, Y. Wang or Richard.
- **G8.** No accounts were found of his undergraduate mentoring (ISyE 4106 Senior Design, 2017–2019, s3).
- **G9.** No rejected papers, abandoned group projects or negative referee exchanges are documented.
- **G10.** Coverage of the 39 batch-scanned committee theses (s51) is partial. Only the first 20 pages of each were searched, and only for the string "Santanu", so mentions that use just his surname would be missed. Those found were formal thanks.
- **G11.** Nothing was found on group-meeting rhythm, shared code or data repositories, or how students are recruited into his group, despite his admissions role.

---

## Sources

Theses were retrieved through the Georgia Tech repository API: `repository.gatech.edu/server/api/discover/search/objects?query=Dey, Santanu` returned 124 items, 17 with Dey as advisor and 52 with Dey as committee member. Every PDF was openly downloadable. Paper identifiers were checked on 2026-10-10 against the arXiv API, the Crossref API or PMLR.

*Dey's own pages and records (primary)*
1. S. S. Dey, homepage, accessed 2026-10-10, https://www2.isye.gatech.edu/~sdey30/ (primary)
2. S. S. Dey, People page (students and postdoc mentees), accessed 2026-10-10, https://www2.isye.gatech.edu/~sdey30/students.html (primary)
3. S. S. Dey, Teaching page, accessed 2026-10-10, https://www2.isye.gatech.edu/~sdey30/teaching.html (primary)
4. S. S. Dey, Linear Programming course video list, accessed 2026-10-10, https://www2.isye.gatech.edu/~sdey30/CourseLinearProgramming.html (primary)
5. S. S. Dey, ISyE 6661 Linear Optimization syllabus, Fall 2020, http://www2.isye.gatech.edu/~sdey30/syllabus.pdf (primary)
6. S. S. Dey, Projects page, accessed 2026-10-10, https://www2.isye.gatech.edu/~sdey30/projects.html (primary)
7. S. S. Dey, Talks page, plus "Convexification in global optimization", IPCO 2020 summer-school slides (June 2020), https://www2.isye.gatech.edu/~sdey30/talks.html and http://www2.isye.gatech.edu/~sdey30/IPCOsummerschoolJune2020.pdf. Checked for advice to students: none, the content is technical (primary)
8. NSF award 1149400, "CAREER: Non-traditional Cutting-Plane Algorithms for Mixed-Integer Programs", PI Dey, 2012–2017, https://www.nsf.gov/awardsearch/showAward?AWD_ID=1149400 (primary)
9. NSF award 1562578, "Sparse Integer Programming", PI Dey, 2016–2020, https://www.nsf.gov/awardsearch/showAward?AWD_ID=1562578 (primary)
10. NSF award 2211343, "Frequency-Domain Model Updating through Branch and Bound with Convex Relaxation", PI Yang Wang, co-PI Dey, 2023–2027, https://www.nsf.gov/awardsearch/showAward?AWD_ID=2211343 (primary)
11. NSF awards 1030422 (convex MINLP, 2010–2014) and 1415460 (EAGER, PI Nemhauser, co-PI Dey, 2014–2017), abstracts, used for context only, https://www.nsf.gov/awardsearch/showAward?AWD_ID=1030422 and https://www.nsf.gov/awardsearch/showAward?AWD_ID=1415460 (primary)

*News, profiles, databases (secondary)*
12. "Santanu Dey Assumes Role of Associate Chair for Graduate Studies", Georgia Tech Mercury (ISyE), created 2019-12-18, https://tlwarc.hg.gatech.edu/node/630174 (secondary; contains Dey quotes)
13. "In Memoriam: Shabbir Ahmed", ISyE News, 2019-07-01, https://www.isye.gatech.edu/news/memoriam-shabbir-ahmed (secondary; contains a Dey quote)
14. "Santanu Dey Promoted to Professor", ISyE News, 2019-03-18, https://www.isye.gatech.edu/news/santanu-dey-promoted-professor (secondary)
15. "Santanu Dey Joins ISyE Faculty", Georgia Tech Mercury, created 2009-06-21, https://tlwarc.hg.gatech.edu/node/47640 (secondary)
16. Shabbir Ahmed, ISyE faculty profile (In Memoriam), accessed 2026-10-10, https://www.isye.gatech.edu/users/shabbir-ahmed (secondary)
17. INFORMS Optimization Society, Egon Balas Prize page (2020 winner listed, no citation text), https://www.informs.org/Recognizing-Excellence/Community-Prizes/Optimization-Society/Egon-Balas-Prize (secondary)
18. Mathematics Genealogy Project, Santanu Subhas Dey (id 119146), https://www.mathgenealogy.org/id.php?id=119146 (secondary)
19. Mathematics Genealogy Project, Christopher Hojny (id 261455), https://www.mathgenealogy.org/id.php?id=261455 (secondary)
20. Mip Wise, "About" page (Santana's company), checked and found to contain no recollection of Dey, https://www.mipwise.com/us/en/about (secondary)

*Theses of Dey's PhD students. For statements about Dey they are secondary; as records of group practice they are primary.*
21. A. Gupte, "Mixed integer bilinear programming with applications to the pooling problem", PhD, Georgia Tech, 2012, https://hdl.handle.net/1853/45761
22. F. Qiu, "Probabilistic covering problems", PhD, Georgia Tech, 2013, https://hdl.handle.net/1853/47567
23. G. Angulo Olivares, "Integer programming approaches for semicontinuous and stochastic optimization", PhD, Georgia Tech, 2014, https://hdl.handle.net/1853/51862
24. D. A. Morán Ramírez, "Fundamental properties of convex mixed-integer programs", PhD, Georgia Tech, 2014, https://hdl.handle.net/1853/52309
25. B. Kocuk, "Global optimization methods for optimal power flow and transmission switching problems in electric power systems", PhD, Georgia Tech, 2016, https://hdl.handle.net/1853/55633
26. Q. Wang, "Theory and computation of sparse cutting planes", PhD, Georgia Tech, 2016, https://hdl.handle.net/1853/56307
27. A. Iroume, "Sparsity in integer programming", PhD, Georgia Tech, 2017, https://hdl.handle.net/1853/58207
28. A. Santana, "Strong convex relaxations for quadratically constrained quadratic programs", PhD, Georgia Tech, 2019, https://hdl.handle.net/1853/62680
29. D. P. Boob, "Convex and structured nonconvex optimization for modern machine learning: Complexity and algorithms", PhD, Georgia Tech, 2020, https://hdl.handle.net/1853/63673
30. G. Wang, "Approximation Algorithms for Mixed Integer Non-Linear Optimization Problems", PhD, Georgia Tech, 2021, https://hdl.handle.net/1853/64724
31. E. S. Johnson, "Solution Techniques for Large-Scale Optimization Problems on the Transmission Grid", PhD, Georgia Tech, 2021, https://hdl.handle.net/1853/66178
32. X. Gu, "Topics in Mixed Integer Nonlinear Optimization", PhD, Georgia Tech, 2022, https://hdl.handle.net/1853/67235
33. Y. Dubey, "Novel Analysis of the Branch-and-Bound Method for Integer Programming", PhD, Georgia Tech, 2022, https://hdl.handle.net/1853/67247 (no acknowledgements)
34. S. Sun, "Some global relaxation methods for quadratic and semidefinite programming", PhD, Georgia Tech, 2023, https://hdl.handle.net/1853/72665
35. Y. Li, "Decomposition Algorithms for Certain Integer Problems over Networks", PhD, Georgia Tech, 2023, https://hdl.handle.net/1853/72737
36. P. Shah, "Closing the Gap: A Theoretical and Practical Exploration of Branch-and-Bound Procedure for Mixed-Integer Programs", PhD, Georgia Tech, 2025, https://hdl.handle.net/1853/77883
37. N. M. Redder, "Power Systems for Sustainability", PhD, Georgia Tech, 2025, https://hdl.handle.net/1853/78723

*Theses where Dey was committee member or reader (secondary)*
38. L. M. Greening, "Models and Algorithms for E-Commerce Fulfillment Network Design", PhD, Georgia Tech, 2024, https://hdl.handle.net/1853/75632
39. I. Panageas, "Evolutionary Markov chains, potential games and optimization under the lens of dynamical systems", PhD, Georgia Tech, 2016, https://hdl.handle.net/1853/55617
40. W. Xie, "Relaxations and approximations of chance constrained stochastic programs", PhD, Georgia Tech, 2017, https://hdl.handle.net/1853/58678
41. Q. He, "Topics in discrete optimization: models, complexity and algorithms", PhD, Georgia Tech, 2013, https://hdl.handle.net/1853/50237
42. Y. Yang, "Exploiting structure in mixed integer programming: Branching, cutting planes, and complexity", PhD, Georgia Tech, 2020, https://hdl.handle.net/1853/63665
43. R. Ojha, "Advances in tactical planning decision problems in trucking service networks", PhD, Georgia Tech, 2024, https://hdl.handle.net/1853/77759
44. D. N. Dadush, "Integer programming, lattice algorithms, and deterministic volume estimation", PhD, Georgia Tech, 2012, https://hdl.handle.net/1853/44807
45. A. Gholami, "Stability, control, and optimization of nonlinear dynamical systems with applications in electric power networks", PhD, Georgia Tech, 2021, https://hdl.handle.net/1853/66151
46. F. G. Cabral, "Optimal planning for electrification of public transit systems and infinite-dimensional linear programming", PhD, Georgia Tech, 2023, https://hdl.handle.net/1853/75081 (used only for C3)
47. H. Boone, "Secure Distribution Networks: From Design to Operations", PhD, Georgia Tech, 2026, https://hdl.handle.net/1853/82126
48. S. Zhang, "On Multistage Stochastic and Distributionally Robust Optimization: New Algorithms, Complexity Analysis, and Performance Comparison", PhD, Georgia Tech, 2022, https://hdl.handle.net/1853/67279
49. X. Dong, "Finite element model updating through smooth nonconvex optimization", PhD, Georgia Tech, 2019, https://hdl.handle.net/1853/62625 (used only for committee membership)
50. T. Schreiber, "Static and Dynamic Structural Model Updating through Branch-and-Bound Optimizations", PhD, Georgia Tech, 2025, https://hdl.handle.net/1853/81531 (used only for committee membership)
51. Batch of 39 further Georgia Tech theses (2010–2026) that list Dey as committee member. The first 20 pages of each were scanned for "Santanu"; the mentions found were formal thanks only. Found through the repository search above (secondary)

*Papers named in this note (primary records of practice; identifiers verified)*
52. A. Gupte, S. Ahmed, M. S. Cheon, S. Dey, "Solving Mixed Integer Bilinear Problems Using MILP Formulations", SIAM J. Optim., 2013, DOI 10.1137/110836183
53. F. Qiu, S. Ahmed, S. S. Dey, L. A. Wolsey, "Covering Linear Programming with Violations", INFORMS J. Comput., 2014, DOI 10.1287/ijoc.2013.0582
54. D. A. Morán R., S. S. Dey, J. P. Vielma, "A Strong Dual for Conic Mixed-Integer Programs", SIAM J. Optim., 2012, DOI 10.1137/110840868
55. B. Kocuk, S. S. Dey, X. A. Sun, "Strong SOCP Relaxations for the Optimal Power Flow Problem", Operations Research, 2016, DOI 10.1287/opre.2016.1489
56. B. Kocuk, H. Jeon, S. S. Dey, J. Linderoth, J. Luedtke, X. A. Sun, "A Cycle-Based Formulation and Valid Inequalities for DC Power Transmission Problems with Switching", Operations Research, 2016, DOI 10.1287/opre.2015.1471
57. S. S. Dey, B. Kocuk, N. Redder, "Node-based valid inequalities for the optimal transmission switching problem", Discrete Optimization, 2022, DOI 10.1016/j.disopt.2021.100683
58. B. Kocuk, D. A. Morán R., "On Subadditive Duality for Conic Mixed-integer Programs", SIAM J. Optim., 2019, DOI 10.1137/18m1210812
59. S. S. Dey, A. Santana, Y. Wang, "New SOCP relaxation and branching rule for bipartite bilinear programs", Optimization and Engineering, 2018, DOI 10.1007/s11081-018-9402-9
60. A. Santana, S. S. Dey, "The Convex Hull of a Quadratic Constraint over a Polytope", SIAM J. Optim., 2020, DOI 10.1137/19m1277333
61. S. S. Dey, D. Han, Y. Wang, "Aggregation of bilinear bipartite equality constraints and its application to structural model updating problem", J. Global Optim., 2026, DOI 10.1007/s10898-026-01607-8
62. S. S. Dey, A. Iroume, M. Molinaro, D. Salvagnin, "Improving the Randomization Step in Feasibility Pump", SIAM J. Optim., 2018, DOI 10.1137/16m1095962; arXiv:1609.08121
63. S. S. Dey, M. Molinaro, Q. Wang, "Analysis of Sparse Cutting-planes for Sparse MILPs with Applications to Stochastic MILPs", arXiv:1601.00198, 2016
64. S. S. Dey, R. Mazumder, G. Wang, "Using L1-relaxation and integer programming to obtain dual bounds for sparse PCA", arXiv:1810.09062, 2018
65. G. Wang, S. Dey, "Upper bounds for Model-Free Row-Sparse Principal Component Analysis", ICML 2020, PMLR 119:9868–9875, https://proceedings.mlr.press/v119/wang20a.html
66. S. S. Dey, M. Molinaro, G. Wang, "Solving sparse principal component analysis with global support", arXiv:2010.11152, 2020
67. E. S. Johnson, S. Ahmed, S. S. Dey, J.-P. Watson, "A K-Nearest Neighbor Heuristic for Real-Time DC Optimal Transmission Switching", arXiv:2003.10565, 2020
68. X. Gu, S. Ahmed, S. S. Dey, "Exact Augmented Lagrangian Duality for Mixed Integer Quadratic Programming", SIAM J. Optim., 2020, DOI 10.1137/19m1271695; arXiv:1907.00920 (posted 2019-07-01)
69. X. Gu, S. S. Dey, J.-P. P. Richard, "Lifting convex inequalities for bipartite bilinear programs", IPCO 2021 (LNCS), DOI 10.1007/978-3-030-73879-2_11, and Math. Program., 2022, DOI 10.1007/s10107-021-01759-3. Also by the same authors, "Solving Sparse Separable Bilinear Programs Using Lifted Bilinear Cover Inequalities", INFORMS J. Comput., 2024, DOI 10.1287/ijoc.2022.0230
70. X. Gu, S. S. Dey, Á. S. Xavier, F. Qiu, "Exploiting Instance and Variable Similarity to Improve Learning-Enhanced Branching", arXiv:2208.10028, 2022
71. S. S. Dey, Y. Dubey, M. Molinaro, "Branch-and-Bound Solves Random Binary IPs in Polytime", arXiv:2007.15192, 2020
72. S. S. Dey, Y. Dubey, M. Molinaro, P. Shah, "A Theoretical and Computational Analysis of Full Strong-Branching", arXiv:2110.10754, 2021
73. S. S. Dey, P. Shah, "Lower bound on size of branch-and-bound trees for solving lot-sizing problem", arXiv:2112.03965, 2021
74. G. Blekherman, S. S. Dey, S. Sun, "Aggregations of quadratic inequalities and hidden hyperplane convexity", arXiv:2210.01722, 2022
75. G. Blekherman, S. S. Dey, M. Molinaro, S. Sun, "Sparse PSD approximation of the PSD cone", arXiv:2002.02988, 2020
76. S. S. Dey, J.-P. P. Richard, "Facets of Two-Dimensional Infinite Group Problems", Math. Oper. Res., 2008, DOI 10.1287/moor.1070.0283
77. S. S. Dey, J.-P. Richard, "Linear-Programming-Based Lifting and Its Application to Primal Cutting-Plane Algorithms", INFORMS J. Comput., 2009, DOI 10.1287/ijoc.1080.0284
78. S. S. Dey, L. A. Wolsey, "Two row mixed-integer cuts via lifting", Math. Program., 2010, DOI 10.1007/s10107-010-0362-x
79. D. Dadush, S. S. Dey, J. P. Vielma, "On the Chvátal-Gomory Closure of a Compact Convex Set", IPCO 2011 (LNCS), DOI 10.1007/978-3-642-20807-2_11; and "The Chvátal-Gomory Closure of a Strictly Convex Body", Math. Oper. Res., 2011, DOI 10.1287/moor.1110.0488
80. C. Coffrin, D. Gordon, P. Scott, "NESTA, The NICTA Energy System Test Case Archive", arXiv:1411.0359. Checked only to document the citation error in C7
