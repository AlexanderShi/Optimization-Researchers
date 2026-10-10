# 04 · Students and collaborators: supervision style, group habits, lab culture, tacit knowledge

> **Researcher**: Nikolaos V. ("Nick") Sahinidis. Google Scholar PTXe50QAAAAJ · DBLP pid 123/7012 · ORCID 0000-0003-2087-9131 · homepage https://sahinidis.coe.gatech.edu/
>
> **Dimension**: research agent 04 of 06 (framework §二, Agent 4). It covers how he supervises, how the group works, its culture, and the tacit knowledge his students report. Nuwa research-craft lens: how he trains and organizes people to do research, not what the group discovered.
>
> **Research date**: 2026-10-10 · **Sources consulted**: 46 (24 primary, 22 secondary; list at the end) · **WebSearch calls**: 3. All three returned only profiles and genealogy pages, so every finding below comes from curl or WebFetch on known URLs and repository APIs.
>
> **Core evidence**:
> - the acknowledgement sections of **13 of his 36 graduated PhD students' dissertations**, read in full and cited by page (§0);
> - his own written memory of his doctoral student Shabbir Ahmed (2019);
> - the acknowledgements of the Tawarmalani–Sahinidis book (2002), co-signed by student and advisor;
> - his CV (§III.B–C, §V);
> - the group website in Internet Archive snapshots from 1998, 2003, 2007, 2008, 2010 and 2013, and as live in 2026.
>
> **Local corpus**: `references/sources/{papers,talks,essays,software}` contain only `.gitkeep` placeholders, so there was no user-supplied material for this dimension. `private/` was not opened.
>
> **Access notes**:
> - Theses were located through the Figshare API (CMU KiltHub), the DSpace API of Georgia Tech's repository, OpenAlex and the Internet Archive CDX index. Every DOI was checked against Crossref.
> - UIUC's IDEALS repository answered HTTP 403 to both curl and WebFetch. One IDEALS thesis marked public (Elble 2010) was read from its Internet Archive copy. The two IDEALS files flagged restricted (`isAllowed=n`: Rios 2009, Chang 2006) were not attempted.
> - Password-protected areas of the old group sites were not accessed: the UIUC `invite/student/` area (HTTP 401) and the CMU member login.
> - Nothing was saved under `sources/talks/`: no talk, interview or recording about his supervision was found.
>
> **Labels**: [stated] = what Sahinidis said or wrote · [practice] = what the record shows he did (CV, rosters, theses, papers) · [observed] = what students or collaborators report · [inferred] = my reading, a hypothesis to test. **P** = primary, **S** = secondary.
> - As the task specifies, students' recollections are marked S. They are first-hand for the student but second-hand about him.
> - Framework §八 rates items "据学生回忆" (according to students' recollections) at **medium** confidence. That rating applies to every [observed, S] item below.
>
> **Relation to the other notes**: I cite these as cross-references and did not re-verify their numbers.
> - 01-publications.md documents the authorship pattern: one student first and Sahinidis last from 1995, then partners after him from 2010.
> - 06-trajectory.md documents lineage, cohorts and placements.
> - 02, 03 and 05 did not exist when this note was written.

---

## 0. Evidence base and its biases

| # | Student | PhD (field, institution, year; where and when signed, if given) | Co-advisor | Funding named in the acknowledgements | Industry or national-lab member of the committee | Pages read |
|---|---|---|---|---|---|---|
| 1 | Joseph M. Elble | Industrial Eng., UIUC, 2010 | — | NIH award GM072023 (Joint NSF/NIGMS initiative) | — | p. v |
| 2 | Aida Khajavirad | Mechanical Eng., CMU, 2011 | Jeremy Michalek | Pennsylvania Infrastructure Technology Alliance; NSF CMII-1030168 | — | PDF p. 6 |
| 3 | Satyajith Amaran | Chemical Eng., CMU, 2014 (MS with him, 2009) | — | NSF award 1033661; Dow | Bikram Sharda (Dow, per the internship thanks); Scott J. Bury (employer not stated in this thesis) | pp. v–vi |
| 4 | Nick D. Austin | Chemical Eng., CMU, 2017 | — | Dow | Daniel Trahan (Dow) | pp. v–vi |
| 5 | Sreekanth Rajagopalan | Chemical Eng., CMU, 2018 | — | Dow (turnaround planning) | Satya Amaran (his former student, then at Dow); Scott Bury | pp. iii–iv |
| 6 | Carlos J. Nohra Khouri | Chemical Eng., CMU, 2020 | — | CMU ChemE; CAPD | — | pp. iii–iv |
| 7 | Benjamin Sauk | Chemical Eng., CMU, 2020 (Pittsburgh, July 2020) | — | DOE IDAES; XSEDE "Bridges"; NVIDIA GPU donation | — | pp. i–ii |
| 8 | Christian Hubbs | Chemical Eng., CMU, 2021 (Chicago, Dec 2020) | Ignacio E. Grossmann | Dow (his employer, which funded the PhD) | — | pp. i–iii |
| 9 | Yijia Sun | Chemical Eng., CMU, 2021 | Lorenz Biegler, "co-advisor in the last year" (per Sun; not in the CV) | ExxonMobil (partial); CAPD; CMU ChemE | — | pp. iv–v |
| 10 | Brad J. Johnson | Chemical Eng., CMU, 2022 (Pittsburgh, Feb 2022) | — | CAPD; Eli Lilly | Salvador García-Muñoz (Lilly) | pp. iii–iv |
| 11 | Owais Sarwar | Chemical Eng., CMU, 2022 (Pittsburgh, Aug 2022) | — | DOE IDAES (through David Miller, NETL) | Anthony P. Burgard (NETL) | pp. i–ii |
| 12 | Yijiang Li | Industrial & Systems Eng., Georgia Tech, 2023 | Santanu S. Dey | DOE | — | pp. v–vi |
| 13 | Anatoliy Kuznetsov | Chemical & Biomolecular Eng., Georgia Tech, 2024 | — | NSF; AFOSR | — | p. iv |

Biases, kept in view in every section:
- **Genre**: acknowledgements are written to thank. None of the 13 criticizes him, and none would be expected to. The absence of criticism here is not evidence that there was nothing to criticize.
- **Coverage**: 12 of the 13 date from 2010–2024. The 1995–2001 UIUC cohort that produced his academic descendants (Ryoo, Shectman, Ahmed, Tawarmalani) appears in only three places:
  - the co-signed book acknowledgements (2002);
  - the December 1998 roster;
  - his own 2019 memory of Ahmed.
- **Independence**: Austin (2017) and Sun (2021) share phrases ("getting to the heart of" / "gets to the heart of"; "the power of intuition"). Sun may have echoed Austin's text, so I count them as two sources but not as fully independent ones.
- **Co-advised theses** (Khajavirad, Hubbs, Li) often thank both advisors in one sentence. I use as evidence about him only the statements addressed to Sahinidis alone, and I mark joint statements as such.
- **Committee-member mentions** in other advisors' theses (Huang 2010 and Vetukuri 2011, both Biegler students) are formulaic thanks and carry no information about style.

## 1. Supervision style

### 1.1 Freedom to choose directions, with insight on request
[observed, S] Five of the 13 acknowledgements use the word "freedom". All five are from CMU, 2014–2021:
- According to Amaran, thesis 2014, p. v: "I appreciate the research freedom you gave me and have enjoyed working in your group very, very much."
- According to Austin, thesis 2017, p. v: "Nick, thank you for giving me the freedom to pursue a wide range of research topics, for your knowledge and assistance whenever I needed it, and for your unwavering commitment to my professional career. I am a stronger researcher because you were so open to my exploring almost every idea I had (even the ones you had to know were bad), and I have been beyond fortunate to have had an advisor who took such an active and caring interest in my development as an engineer and a member of the academic community."
- According to Rajagopalan, thesis 2018, p. iii: "You gave me the freedom to explore a wide range of research topics and the resources to learn and build my professional experience both in the academic and the industrial research community, through conferences and internships."
- According to Sauk, thesis 2020, p. i: "I also thank Nick for the freedom he gave me to explore several different research directions on topics that I was passionate about."
- According to Sun, thesis 2021, p. iv: "Thank you for giving me the freedom to explore different ideas and for offering your acute insight when I needed it."

[inferred] This is a pull model of supervision: the student proposes, and the advisor supplies insight "whenever I needed it" (Austin) or "when I needed it" (Sun).
- Era: CMU Chemical Engineering, 2009–2021. The March 2013 roster lists 6 PhD students, 3 postdocs and 7 MS students.
- Most of these students were funded by a sponsor or a consortium (§0), so the freedom operated inside sponsored problem areas. This tension is kept as Contradiction 1.

### 1.2 Pressure on explanation, writing and presenting
- [observed, S] According to Sauk, thesis 2020, p. i: "Nick has constantly pushed me to become a better writer, presenter, and researcher. His insightful questions have challenged me to understand the fundamental concepts of my work, and to succinctly explain any conclusion that I reach." On the same page: "I fondly recall several Skype and Zoom calls where we spent hours improving manuscripts."
- [observed, S] According to Austin, thesis 2017, p. v: "I’ve learned a lot from you: about getting to the heart of a new concept, about effective communication as the true currency of one’s ideas, about the power of intuition, and about patience as the key to solving difficult problems."
- [observed, S] According to Sun, thesis 2021, p. iv: "I have also learnt from him about efficient and effective communication, which proves to be extremely helpful especially during the last 13 months of my PhD when working from home becomes the new normal as a result of the pandemic."
- [observed, S] According to Amaran, thesis 2014, p. v: "Your work ethic, responsiveness, communication, and efficiency are qualities that I aspire to."
- [observed, S] According to Kuznetsov, thesis 2024, p. iv: "Nick, thank you for constantly challenging me to be the best researcher possible and for providing me with invaluable guidance, opportunities, and mentorship."
- [observed, S] According to Rajagopalan, thesis 2018, p. iii: "You were always committed to my academic success; pulling me out of failures and pushing me to achieve more."
- Era: Sauk's thesis is signed July 2020, the month before Sahinidis started at Georgia Tech (15 Aug 2020, ISyE news). The manuscript sessions therefore ran over Skype and Zoom, during the move and the pandemic.

### 1.3 Patience with slow starts and with students new to optimization
- [observed, S] According to Hubbs, thesis 2021, pp. i–ii, speaking of both advisors (Sahinidis and Grossmann): "They helped me grow as a researcher and were patient with me as someone who was experienced in areas of data science and machine learning, but had never been exposed to the world of mathematical programming and optimization. There were many meetings where I struggled with elementary concepts and models, and they showed patience with me until things finally “clicked.”"
- [observed, S] According to Rajagopalan, thesis 2018, p. iii: "Nick, you were immensely patient in guiding me through all the milestones toward my Ph.D., which would not have been possible otherwise."
- [observed, S] According to Sauk, thesis 2020, p. i: "I appreciate Nick’s patience with me, and I value all of his feedback."
- [observed, S] According to Khajavirad, thesis 2011 (mechanical engineering, co-advised with Michalek), PDF p. 6: "I am grateful to Nick for taking me as his student in the first place. He introduced me to the intriguing world of global optimization, inspired me by his accomplishments and dedication, and influenced my research path and career goals."
  - The roles were divided: she thanks Michalek "for exposing me to a variety of mechanical engineering design problems that motivate and demand the convexification results presented in this thesis".
- [practice, P] Recruiting from outside optimization goes back to UIUC. The December 1998 roster lists seven graduate students, with their bachelor's degrees only. None lists a mathematics degree. The degrees were in:
  - mechanical engineering: Ahmed, Tawarmalani;
  - chemical engineering: Furman, Nanda, Vaia, Voudouris;
  - engineering: Shectman.

### 1.4 What the students say they took away
The table lists the descriptors that recur across the 13 acknowledgements. Counts are of theses, not of mentions.

| Descriptor | Theses | Count |
|---|---|---|
| freedom to explore | Amaran 2014, Austin 2017, Rajagopalan 2018, Sauk 2020, Sun 2021 | 5 |
| communication, explaining | Amaran ("communication"); Austin ("effective communication as the true currency of one’s ideas"); Sauk ("succinctly explain any conclusion"); Sun ("efficient and effective communication") | 4 |
| patience, shown to them or taught as a method | shown: Rajagopalan, Sauk, Hubbs (both advisors); taught: Austin ("patience as the key to solving difficult problems") | 4 |
| challenge, push | Rajagopalan, Sauk, Kuznetsov | 3 |
| intuition | Amaran ("amazing intuition"); Austin and Sun ("the power of intuition") | 3 |
| getting to the heart of a problem | Austin ("of a new concept"); Sun ("how he gets to the heart of a problem") | 2 |
| efficiency | Amaran; Sun ("the art of efficiency") | 2 |
| work ethic, responsiveness | Amaran; Nohra 2020, p. iii: "I truly admire his work ethic, dedication and responsiveness." | 2 |
| breadth | Amaran ("domain expertise, computing mastery"); Sun ("His extensive knowledge in many diverse research fields") | 2 |
| integrity, character | Sarwar; Hubbs (both advisors: "the highest integrity") | 2 |
| pragmatism | Rajagopalan: "I am still learning from you to be more pragmatic in work and in life." | 1 |
| leadership | Sarwar 2022, p. i: "He possesses an inspiring ability to win the hearts and minds of his group members. Professor Sahinidis is a man of high character, sophistication, and integrity, and is sort of leader that his students want to work hard for." | 1 |

[inferred] The descriptors fall into two groups:
- **Work-style traits** (efficiency, responsiveness, work ethic, communication): the students say they "aspire to" these.
- **Judgement traits** (intuition, getting to the heart, pragmatism): the students say they learned these by watching. Sun, p. iv: "It has been a privilege to work with him, to observe and learn from how he gets to the heart of a problem."

No student describes a procedure taught for either group. That marks both as tacit knowledge (§4).

### 1.5 Support for exposure and careers, including careers outside the field
- [observed, S] According to Amaran, thesis 2014, p. v: "Nick, you gave me the opportunity to work on some very interesting, open-ended, and wide-ranging problems, and have actively supported my professional exposure through conferences and internships." Rajagopalan says the same (§1.1).
- [observed, S] Internships named in the theses:
  - Dow: Amaran; Rajagopalan.
  - Mitsubishi Electric Research Laboratories: Rajagopalan; Nohra, for two summers ("A significant part of this work has been done in collaboration with Arvind", p. iii).
  - Morgan Stanley: Sun.
  - Argonne National Laboratory, where Li names Sven Leyffer among his mentors, and Amazon: Li (p. v).
  - Eli Lilly: Johnson describes a visit to Indianapolis (p. iv).
- [observed, S] According to Sun, thesis 2021, p. iv: "I am very fortunate to have an advisor who’s always been supportive of me pursuing my career goals both inside and outside of chemical engineering." Sun went to Morgan Stanley (CV).
- [practice, P] Most PhD graduates since 2002 went to industry (06 §3.2; CV).

### 1.6 His own words about students (the only first-person evidence found)
- [stated, P] **The recruiting text.** It is the same in substance at UIUC (2007 snapshot), CMU (2008 snapshot) and Georgia Tech (live 2026). The 2026 text reads: "Almost every year, there are openings in my research group for exceptional graduate students. However, I am unable to respond to requests for appraisals due to the tremendous interest we receive from domestic and international students. Applications for admission to the units with which I am affiliated are reviewed by admissions committees and individual professors cannot accept students directly into their research groups before students are admitted to a unit. Research advisor selection is done after a student has been offered admission and, in certain units, after the student has joined the program."
  - Wording: where 2026 says "units", the 2007 version says "departments" and the 2008 version says "departments, programs, and centers".
  - Units listed: ChBE, CS, Bioengineering and IESE at UIUC (2007); Chemical Engineering and the Joint CMU-Pitt Ph.D. Program in Computational Biology (2008); ISyE and ChBE (2026).
- [stated, P] **His memory of Shabbir Ahmed**, in "In Memoriam: Shabbir Ahmed" (Georgia Tech ISyE, 1 Jul 2019), signed "Nick Sahinidis, John E. Swearingen Professor, Carnegie Mellon":
  - "I first met Shabbir 24 years ago when he joined the graduate program at the University of Illinois. The department had never admitted anyone from his undergraduate institution before, so they gave me his file and asked for my opinion. I was immediately impressed by what he had accomplished in his early twenties. Not only did he make excellent grades, but he already had teaching experience […]"
  - "Shabbir was one of my most dedicated, hard-working, and inspirational doctoral students. He showed nothing but excellence during his time at UIUC and taught me a great deal about probabilistic analysis of algorithms and stochastic programming."
- [stated, S, quoted by a news writer] **CMU ChemE news, "Optimizing processes with AI" (July 2018).** He says: "We don't just use algorithms that others develop," and "In our group, we also develop the algorithms ourselves and then we apply them to many application domains, both within and outside of process systems engineering."
  - The same article shows how this was staffed [observed, S]: "a number of students in Sahinidis’ group are applying the ALAMO methodology, or similar approaches, to multiple chemical engineering problems". It names Zachary Wilson (fifth-year PhD, reaction engineering) and Marissa Engle (third-year PhD, thermodynamics).
  - Wilson's core paper is Wilson & Sahinidis, "The ALAMO approach to machine learning", *Comput. Chem. Eng.* 106:785–795, 2017, DOI 10.1016/j.compchemeng.2017.02.010 [practice, P].
- [stated, S] **ISyE news (2021)**: "It is truly exciting to be at Georgia Tech, where I can collaborate with world-class colleagues and graduate students on optimization and its applications".
- [inferred] What he praises in a student: accomplishment before admission, dedication, hard work, excellence, and having taught him a new field. No source I found has him describe how he runs meetings, picks student topics or reviews drafts (Gaps).

### 1.7 Co-supervision
- [practice, P] CV §V.B1 lists these joint supervisions:
  - with J. Michalek: Khajavirad (mechanical engineering, 2011);
  - with I. E. Grossmann: Hubbs (2021);
  - with S. S. Dey: Li (2023) and Choudhary (2026);
  - in progress: with J.-P. Correa-Baena, Oh (materials science); with G. Nemhauser, Bayramoglu; with Weijun Xie, Deng.
- [practice, P] The co-supervised share has grown: 2 of the 33 PhDs who graduated through 2022, 2 of the 3 graduated since, and 3 of the 5 students in progress.
- [observed, S] According to Li, thesis 2023, p. v, about Sahinidis and Dey: "I have had the great privilege to spend a lot [sic] time working with and learning from them who have always been supportive to me. I especially enjoyed their passion and intellectual depth during our meetings and their lighthearted sense of humors outside of work."
- [observed, S] According to Sun, thesis 2021, p. iv: "Thanks in particular to Larry for being my co-advisor in the last year of my PhD and for your valuable comments to my research proposal." The CV does not record this (Contradiction 3). [inferred] It was the hand-over arrangement for a CMU student who finished after the August 2020 move.
- [inferred] Era: at CMU co-advising was rare, 2 of 20 PhDs in 2011–2022.
  - One of the two, Hubbs, was a Dow-sponsored student shared with Grossmann, Sahinidis's own former advisor.
  - At Georgia Tech co-advising became the default, with co-advisors from ISyE's optimization faculty.
  - This fits what he said on arrival, that he was "excited that I am working with" Nemhauser and Dey (ISyE news 2021; 06 §4). That is a statement of enthusiasm, not a stated reason for the move.

## 2. Group habits and working arrangements

### 2.1 Group meetings and seminars
- [observed, S] According to Nohra, thesis 2020, p. iv: "Nick, Sree, Yash and Zach were senior Ph.D. students when I joined the group. I appreciate the very useful feedback that they always gave me at my group meeting presentations."
- [observed, S] According to Johnson, thesis 2022, p. iii: "The broader Process Systems Engineering community, through their weekly presentations on interesting researcher topics and their camaraderie, has helped me grow intellectually". This is a department-level PSE habit, not one specific to his group.
- Not found: meeting frequency, format, agenda, and whether students present to him alone or to the whole group.

### 2.2 Writing together
- [observed, S] Sauk describes spending "hours improving manuscripts" with him in remote calls (§1.2).
- [practice, P] On most papers a single student is first author and Sahinidis last (01-publications.md). No public document states his authorship rules.

### 2.3 Remote and split-site supervision (three episodes)
- **2007–2010, UIUC to CMU** [practice, P]. The July 2008 roster lists three groups:
  - seven CMU chemical-engineering graduate students, several of them MS students;
  - three students still at UIUC: Bao (ChBE), Elble and Rios (IESE);
  - two postdocs: A. B. Smith and P. Vouzis.

  All three UIUC students finished their degrees there in 2009–2010 (CV). Elble's acknowledgement (2010) does not mention the distance [observed, S].
- **2019–2020, Pittsburgh to Chicago** [observed, S]. According to Hubbs, thesis 2021, p. ii: "They have been supportive of me, even when I discussed continuing remotely from Chicago - a year before COVID".
- **2020–2022, CMU to Georgia Tech, and the pandemic** [observed, S; practice, P]:
  - Sun worked from home for 13 months and credits his "efficient and effective communication".
  - Sauk describes the Skype and Zoom manuscript sessions.
  - Sarwar's committee list (Aug 2022, p. i) gives Sahinidis both CMU and Georgia Tech affiliations.
  - Kuznetsov is listed as a group member at CMU (Nohra 2020, p. iv; Sauk 2020, p. ii) and finished a Georgia Tech ChBE PhD in 2024. He thanks friends from both universities (p. iv).

### 2.4 MS and BS projects: cheap, computational, on the group's own tools
- [practice, P] The CV (§V.B2) lists 86 graduated MS students. There were 9 in 2017, 10 in 2018 and 8 in 2019, then 1 in 2023 and 1 in 2025. Era: CMU ChemE's master's program. The channel almost vanished after the move to Georgia Tech (06 §2).
- [practice, P] In 2017–2019 four pairs of MS students shared one project each, listed as "joint work with" the partner (group page; CV):
  - Koranne and Panchal (2017);
  - Bhatia and Pandya (2018);
  - Dabhadkar and Ingale (2018);
  - Jia and Xie (2019).
- [practice, P] Many MS and BS titles are computational studies on the group's own software:
  - "Computational experiments with the branch-and-reduce algorithm for global optimization" (BS, 1999);
  - "Experiments with cutting planes in branch-and-reduce" (MS, 2001);
  - "Tuning BARON using derivative-free optimization (DFO) algorithms" (MS, 2012);
  - "A Fortran implementation of ALAMO" and "A web-based interface for ALAMO" (both MS, 2013);
  - "Model-And-Search: A derivative-free algorithm and computational experience" (MS, 2014);
  - "Branch-And-Model: A derivative-free optimization algorithm and computational experience" (MS, 2015);
  - "Computational investigation of the impact of A-optimal design on ALAMO" (MS, 2016), with D-optimal, I-optimal and Monte Carlo D-optimal companion theses the same year.
- [practice, P; the link is inferred] "A Fortran implementation of ALAMO" (MS, 2013) dates from the same year as this ALAMO release note on minlp.com: "2013.10 Initial public distribution of ALAMO-Fortran, to members of the CCSI Industrial Advisory Board". That the MS code became that release is my inference; the record does not say so.
- [practice, P] MS students published.
  - His first graduate student, Russ Vander Wiel (MS Industrial Eng., 1993), is first author of three journal papers with him:
    - "Heuristic bounds and test problem generation for the time-dependent traveling salesman problem", *Transportation Science* 29(2):167–183, 1995 (DOI 10.1287/trsc.29.2.167);
    - "An exact solution approach for the time-dependent traveling-salesman problem", *Naval Research Logistics* 43(6):797–820, 1996 (DOI 10.1002/(sici)1520-6750(199609)43:6<797::aid-nav2>3.0.co;2-#);
    - "The assignment problem with external interactions", *Networks* 30(3):171–185, 1997 (DOI 10.1002/(sici)1097-0037(199710)30:3<171::aid-net3>3.0.co;2-i).
  - Minrui Yu (MS 1998, "Optimal design of alternative refrigerants") is third author of Sahinidis, Tawarmalani & Yu, "Design of alternative refrigerants via global optimization", *AIChE J.* 49(7):1761–1775, 2003 (DOI 10.1002/aic.690490714). It appeared five years after the MS.
- [stated, P, unsigned group page] "Optimizing for fun" (December 2009) traces that first student project to his own doctoral work: Sahinidis & Grossmann, "MINLP model for cyclic multiproduct scheduling on continuous parallel lines", *Comput. Chem. Eng.* 15(2):85–103, 1991 (DOI 10.1016/0098-1354(91)87008-w). The page says: "Back in the early 1990s, Nick and his first graduate student, Russ Vander Wiel, addressed a natural extension of this problem, the case when transition times depend on sequence as well as the time of the day that the transition takes place." [inferred] His first student's project extended a problem from his own thesis.

### 2.5 MS-then-PhD path (mainly UIUC)
- [practice, P] 12 of his 36 graduated PhDs first wrote an MS thesis with him: Ryoo, Shectman, Ahmed, Tawarmalani, Furman, Vaia, Wei Xie, A. B. Smith, Bao, Elble, Amaran and Tong Zhang.
  - Elble wrote two MS theses in 2007, one in IE and one in CS.
  - A 13th, Xingjiang Tao (MS ISyE 2025), is now a PhD student.
  - By era: 10 of the 13 UIUC-era PhDs (1995–2010), 2 of the 20 CMU-era PhDs (2011–2022), and none of the 3 Georgia Tech PhDs so far. The counts come from cross-matching the CV's PhD and MS lists.
- [inferred] At UIUC the MS thesis worked as a complete first project before the PhD.
  - Sometimes the PhD changed topic. Tawarmalani moved from "Multistage network optimization and decomposition algorithms" (MS 1997) to MINLP theory. Ahmed moved from "Robust process planning under uncertainty" (MS 1997) to stochastic integer programming. Xie moved from "Robust dynamic facility layout under uncertainty" (MS 2003) to protein bioinformatics.
  - Sometimes the PhD continued the MS: Shectman, Furman, Vaia, Smith.

### 2.6 Keeping his own graduates as postdocs
- [practice, P] CV §V.B5: three of his own PhD graduates stayed on as postdocs: Elble, Chang and Khajavirad. Khajavirad "joined IBM TJ Watson Lab, New York after her first postdoc and The University of Texas at Austin after her second postdoc in my group". Postdocs and research staff were the group's day-to-day technical mentors (§3.2).

## 3. Lab culture

### 3.1 Atmosphere and space
- [observed, S] Three students describe the atmosphere:
  - Nohra, thesis 2020, p. iv: "I enjoyed the extremely friendly atmosphere of this group."
  - Johnson, thesis 2022, p. iii: "He has fostered a lively research group that has been a pleasure to interact with".
  - Amaran, thesis 2014, p. vi, thanks "my fellow Sahinidis group members for some good times together—be it the mid-afternoon office prattle, the late nights on the upper floors of Doherty Hall, or expeditions to local bars and restaurants".
- [observed, S] Students shared offices in CMU's Doherty Hall: "the third floor office" (Nohra, p. iv); "the fourth floor cohort" and "that aisle on the fourth floor" (Rajagopalan, p. iv).
- [observed, S] The tone was informal. According to Austin, thesis 2017, p. v: "I also never mentioned how much I like the Nick-symmetry of our emails."

### 3.2 Know-how passes through postdocs and senior students
- [observed, S] According to Rajagopalan, thesis 2018, p. iii: "I would like to thank Aida, Keith, Mustafa, and Yash in addition to Nick’s support with helping me understand global optimization and the workings of BARON. A special thanks to Mustafa for putting up with my incessant bugging and serving us all refreshing tea instead!"
- [observed, S] According to Nohra, thesis 2020, p. iv: "Mustafa, Nikos and Aida helped me during the early stages of my Ph.D. I thank Mustafa for answering some of the questions that I had about BARON at the beginning of my Ph.D. I am grateful to Nikos for helping me with several computer issues and for the interesting conversations that we used to have in the third floor office. I thank Aida for her guidance when I was starting to review the vast literature on convexification."
- [observed, S] According to Sauk, thesis 2020, p. ii: "I am especially indebted to Professor Nikolaos Ploskas. Throughout my entire PhD, Nikos has been incredibly patient and kind. He has been an essential contributor to several of my projects at CMU."
- [observed, S] According to Sun, thesis 2021, p. v: "Special thanks to Marissa Engle and Dr. Tong Zhang for being great mentors."
- [observed, S] According to Elble, thesis 2010, p. v: "Although he graduated halfway though [sic] my graduate studies, Wei Xie’s advice and support always proved to be invaluable." On the postdoc Panos Vouzis: "We taught ourselves the architecture of the graphics processing unit, but came together to learn what it is truly capable of achieving."
- [observed, S] According to Amaran, thesis 2014, p. vi, peers had recognized roles: "resident TEXperts", "presentation pundit Alison Cozad", "Linux gurus". He writes: "You introduced and helped me become comfortable with the primary non-programming tools that I use on an everyday basis." Of these, only Cozad appears in the group's rosters. The acknowledgement does not say where the others worked.
- [practice, P] Who these mentors were: Kılınç, Ploskas and Khajavirad were postdocs (CV §V.B5). Zorn and Puranik were senior PhD students, and the March 2013 roster lists Zorn as a postdoc.
- [inferred] Mentoring is layered: Sahinidis, then the postdocs and senior students, then the juniors. BARON know-how in particular passed by word of mouth.
  - Era: CMU 2009–2020. BARON was then maintained as a commercial product of The Optimization Firm (06).
  - How much source-code access students had is not documented.

### 3.3 UIUC: one cumulative code base, with the group as its first users (1991–2002)
[stated jointly with his student Tawarmalani, P] Source: the acknowledgements of Tawarmalani & Sahinidis, *Convexification and Global Optimization in Continuous and Mixed-Integer Nonlinear Programming*, Kluwer, 2002 (DOI 10.1007/978-1-4757-3532-1).
- **Students' algorithms underpin the book.** p. xvii: "It has been our good fortune to have had a number of students and labmates with whom we had beneficial technical discussions and collaborations over the years." … "We are also indebted to Vinay Ghildyal, Ming Long Liu, Hong S. Ryoo, Joseph P. Shectman, and Russ J. Vander Wiel who developed and tested optimization algorithms that laid the ground work for obtaining some of the results described in this book. Kevin C. Furman, Anastasia Vaia, and Yannis Voudouris provided useful feedback while using BARON."
- **Group members read the manuscript.** p. xviii: "The book has also benefited a great deal from careful readings and suggestions from YoungJung Chang, Kevin C. Furman, Lindsay Gardner, Yanjun Li, Arne J. Pearlstein, Armin Pruessner, Louis Miguel Rios, Anastasia Vaia, and Wei Xie." Several of these readers were group members at the time.
- **Lab-mates co-authored** [practice, P]. Per p. xvii, Chapter 3 and Section 6.3 "resulted from joint work with Shabbir Ahmed". The joint papers are:
  - Tawarmalani, Ahmed & Sahinidis, "Product Disaggregation in Global Optimization and Relaxations of Rational Programs", *Optim. Eng.* 3(3):281–303, 2002 (DOI 10.1023/A:1021043227181);
  - Tawarmalani, Ahmed & Sahinidis, "Global Optimization of 0-1 Hyperbolic Programs", *J. Global Optim.* 24(4):385–416, 2002 (DOI 10.1023/A:1021279918708).
- **The advisor learned alongside the student.** p. xvii: "Special thanks are due to Lynn McLinden for his course, Conjugate Analysis and Optimization, which helped both of us understand a lot of the background material needed for the convexification part of this work."
- **External users served as a test bed** [practice, P]. p. xviii: "Between October 1999 and August 2002, 164 researchers and users of optimization techniques submitted over 6100 problems to the BARON Web portal (an average of over six problems a day). We have learned a great deal and improved the algorithms and software considerably as a result of these submissions."
- **Era and resources.** UIUC, about seven graduate students (December 1998 roster). Funding named on p. xviii:
  - NSF awards DMI 95-02722, BES 98-73586, ECS 00-98770, DMI 01-15166 and CTS 01-24751;
  - a Lucent Technologies Industrial Ecology Fellowship;
  - two UIUC fellowships held by Tawarmalani.
- [inferred] Each student's algorithm went into one shared system, and later students used that system as their test bed. This is how a small industrial-engineering group of the 1990s built a general-purpose solver.

### 3.4 Industry inside supervision (CMU, 2009–2022)
- [practice, P] Of the 9 CMU theses from 2014–2022 that I read, 5 had an industry or national-lab member on the committee (§0): Amaran, Austin, Rajagopalan, Johnson, Sarwar.
- [observed, S] Sponsor staff acted as co-mentors:
  - Johnson, thesis 2022, p. iv: "Through my meetings with him, Dr. García-Muñoz has played a pivotal role in helping me form the direction of my research and network with other researchers in the field."
  - Austin, thesis 2017, p. v, on Dow's Daniel Trahan: "Daniel, you’ve been an incredible collaborator and mentor".
  - Hubbs, thesis 2021, p. i, on Dow's John Wassick: "our weekly discussions which are always fruitful and full of new research ideas and advice".
  - Rajagopalan, thesis 2018, p. iii: "Satya and Arvind have been great mentors throughout my Ph.D."
- [practice, P; observed, S] Former students fed back into the group:
  - Amaran (PhD 2014, then at Dow) sat on Rajagopalan's committee in 2018.
  - When Dow's Wassick encouraged Hubbs to do a PhD, he introduced him to "former students of both Prof. Grossmann and Prof. Sahinidis, namely Dr. Markus Drouven and Dr. Satya Amaran, who spoke highly of Carnegie Mellon University and the two men who would later become my advisors" (Hubbs, thesis 2021, p. i).
- [inferred] At CMU the advisor's role moved toward broker: the sponsor supplied the problem and a co-mentor, the student did the work, and the advisor kept the methods core. This matches the authorship pattern from 2010 onward: student first, Sahinidis second, partners after (01-publications.md).

### 3.5 How the group presents itself
- [stated, P, unsigned group page] The UIUC home page (2003 snapshot) is titled "The Sigma Optimization Group" and says: "We pursue fundamental developments in the field of optimization while providing solutions to complex problems at the interfaces among the computational, engineering, chemical, and biological sciences."
- [stated, P, unsigned group page] "Optimizing for fun" (December 2009) reports that *The Unofficial Guide to the Walt Disney World* (the page's name for it) thanks "Nick Sahinidis and his graduate students". The page links that thanks to the time-dependent TSP papers only with a hedge: the papers "apparently, are acknowledged in The Guide". It ends: "Who says research in optimization does not impact the life of everyday people?" I did not read the Guide itself.
- [practice, P] The group's name changed over time: "The Sigma Optimization Group" (UIUC, 2003); "Nick Sahinidis' Optimization Group" (CMU page footers, 2008–2010); "Sahinidis Optimization Group" (Georgia Tech, 2026).
- [practice, P] The live news page has 20 items from 2000–2022:
  - 12 are his own honours or appointments;
  - 3 are team or partnership items: the IDAES and CCSI R&D 100 awards, and the Eli Lilly partnership;
  - 4 are research stories;
  - 1 is the memorial for his former student Ahmed.

  No student award appears there. The CV records them instead; §III.C lists four:
  - Ahmed, INFORMS Dantzig Dissertation Award (2000);
  - Smith, IUCr Poster Prize (2006);
  - Samudra, INFORMS Interactive Session Winner (2011);
  - Cozad, Ken Meyer Research Award (2014).

### 3.6 Teaching as part of the group's system
- [practice, P; observed by students through course ratings] CV §III.B: "Listed in the Daily Illini “List of Teachers Ranked as Excellent by their Students” for S93, S96, F96, S99".
- [practice, P] The courses he developed run alongside the group's research lines:
  - "Computational Aspects of the Simplex Method" (F04, F09–F12), alongside the linear-programming theses: Elble's two MS theses (2007) and PhD (2010), and the MS thesis "Preprocessing in linear programming" (2008).
  - "Algorithms for Bioinformatics" (F03), alongside the bioinformatics PhDs: Chang 2006, Xie 2007, Shah 2011.
  - "Chemical Product Design" (S08–S13), alongside the molecular-design theses: Samudra 2012, Austin 2017, Sun 2021.
  - "Computational Methods: A GPU HPC course" (S22, S24, S25), after the GPU theses: Elble 2010, Sauk 2020.
- [inferred] At least the GPU course followed the research rather than leading it.
- [practice, P] Since 2008 he has taught a one-day short course on "Global Optimization and Optimization under Uncertainty" as part of the CAPD short course at CMU, "2008—present (20-50 students every year)". This is where industrial CAPD members meet the group's methods.

## 4. Tacit knowledge: what the students report learning that no paper states

Each item is a student's recollection [observed, S] at medium confidence (framework §八), unless the row says otherwise.

| # | Tacit rule (my wording) | According to (source, page) |
|---|---|---|
| T1 | Be able to explain any conclusion briefly and from fundamentals. Expect to be questioned until you can. | Sauk 2020, p. i |
| T2 | Communication is part of the research product, "the true currency of one’s ideas". Write and present efficiently. | Austin 2017, p. v; Amaran 2014, p. v; Sun 2021, p. iv |
| T3 | Go to the heart of a problem and trust intuition. These are learned by watching him, not from instruction. | Sun 2021, p. iv ("to observe and learn from how he gets to the heart of a problem"); Austin 2017, p. v; Amaran 2014, p. v |
| T4 | Bring your own directions. You will be allowed to try them, including ones the advisor expects to fail. Ask when you need insight. | Austin 2017, p. v; Sun 2021, p. iv; Sauk 2020, p. i |
| T5 | Patience is the method on hard problems. Be pragmatic about what to do. | Austin 2017, p. v; Rajagopalan 2018, p. iii |
| T6 | Learn BARON and global optimization from the postdocs and senior students, not only from the advisor. | Rajagopalan 2018, p. iii; Nohra 2020, p. iv |
| T7 | Get the convex-analysis background from mathematics courses outside the group. The pattern recurs over two decades: Tawarmalani took Lynn McLinden's "Conjugate Analysis and Optimization"; Khajavirad (2011) and Nohra (2020) took Javier Peña's convex analysis courses. | Book 2002, p. xvii [stated, P]; Khajavirad 2011, PDF p. 6; Nohra 2020, p. iii. The pattern itself is [inferred]. |
| T8 | Internships and conferences are part of the PhD, and the advisor backs them. They can feed the thesis directly. | Amaran 2014, p. v; Rajagopalan 2018, p. iii; Nohra 2020, p. iii |
| T9 | The sponsor's engineer is a second mentor who helps set direction and may sit on the committee. | Johnson 2022, p. iv; Austin 2017, p. v; Hubbs 2021, p. i; Rajagopalan 2018, p. iii |
| T10 | Manuscripts get finished in long working sessions with him, held remotely if necessary. | Sauk 2020, p. i |
| T11 | Senior students critique junior students' group-meeting talks. | Nohra 2020, p. iv |
| T12 | The advisor expects to learn the student's field alongside the student. | [stated, P] Ahmed memoriam 2019 ("taught me a great deal about probabilistic analysis of algorithms and stochastic programming"); book 2002, p. xvii (McLinden's course "helped both of us") |

**Not distillable from what was found** (framework §八):
- how he runs a meeting;
- how he decides which student idea to back or to stop;
- how he judges a draft or a computational result;
- anything said only in unrecorded group meetings.

## 5. Failures, setbacks, and what the record leaves out
- [observed, S] Rajagopalan (p. iii) thanks him for "pulling me out of failures" but names none.
- [observed, S] Austin (p. v) was free to explore ideas including "the ones you had to know were bad". [inferred] The advisor let students spend time on ideas he expected to fail instead of vetoing them. The cost in time to degree is not recorded.
- [observed, S] Hubbs (p. ii) recalls "many meetings where I struggled with elementary concepts and models".
- [practice, P] Research lines ended when their students graduated:
  - bioinformatics after Shah (2011);
  - text mining after Tong Zhang (2019);
  - deep reinforcement learning after Hubbs (2021).

  See 06 §4.2 and §6. No explanation from him or from the students was found.
- [practice, P] The MS channel collapsed after the 2020 move: 27 MS theses in 2017–2019, 2 in 2020–2025 (CV).
- [practice, P] The public group page is out of date (Contradiction 4), which suggests it is not kept up as a document for students.
- Unknown: students who left without a degree, conflicts, rejected student papers, retracted student results. Nothing is public.

## 6. Era and resource context

| Period | Setting | Group snapshot (source) | Resources named by students or in the book | Mentorship practices visible |
|---|---|---|---|---|
| 1991–1998 | UIUC, industrial-engineering program | first MS students: Vander Wiel (MS 1993); Ryoo and Shectman (MS 1995) | NSF (CAREER and other awards; 06 §2) | MS projects published in journals; students' algorithms built into BARON; MS-then-PhD path |
| 1998–2007 | UIUC, ChBE and IESE | 7 graduate students and 2 visitors (Dec 1998 roster) | NSF awards; Lucent fellowship; UIUC fellowships; NIH (Elble) | shared BARON code base; application students as its testers; group reads the book manuscript; BARON web portal (164 users, over 6100 problems, 1999–2002); recruiting through four UIUC units |
| 2007–2010 | move to CMU; UIUC students finish remotely | July 2008: 7 CMU graduate students, 3 at UIUC, 2 postdocs | NIH; NSF | split-site supervision; a student and a postdoc teach themselves GPU programming (Elble) |
| 2010–2020 | CMU ChemE (Swearingen Professor; CAPD director 2015–2020) | March 2013: 6 PhD students, 3 postdocs, 7 MS students; 27 MS theses in 2017–2019 | CAPD; DOE/NETL/IDAES; Dow; Eli Lilly; ExxonMobil; NSF; XSEDE; NVIDIA donation | freedom with insight on request; pressure on explanation; postdocs as technical mentors; industry co-mentors and committee members; internships; MS pairs; shared Doherty Hall offices |
| 2020– | Georgia Tech, ISyE and ChBE | CV, Oct 2026: 5 PhD students in progress and 1 postdoc (since 1 Nov 2025) | NSF; AFOSR; DOE; DARPA (per 06) | co-supervision with ISyE and materials colleagues as the default; CMU students finish remotely; Biegler co-advises during the hand-over |

## 7. Mapping onto the seven layers (framework §一)

| Layer | What this note adds | Evidence strength |
|---|---|---|
| 1 Taste | Only indirectly: "get to the heart", intuition (the students' words) | weak |
| 2 Problem choice | Students choose inside sponsored areas; his first student's problem extended his own thesis; MS projects as probes | medium |
| 3 Idea generation | He learns new fields through his students (Ahmed; the McLinden course); students are free to explore | weak to medium |
| 4 Execution | A shared code base (BARON, ALAMO) as the platform; MS computational studies; self-taught GPU work; postdocs as technical mentors | medium |
| 5 Result judgement | Questioning until a conclusion can be explained succinctly (Sauk) | weak (one source) |
| 6 Expression | Pressure on writing and presenting; long manuscript sessions; communication as currency | medium (4 theses) |
| 7 Organization | Supervision on request; layered mentoring; industry co-mentors; co-supervision at Georgia Tech; MS-then-PhD at UIUC; graduates kept as postdocs | strong |

## 8. Candidate mentorship heuristics for the skill
All are [inferred] from §§1–5.
1. **Let the student choose the direction inside a funded problem area, and answer when asked.** Evidence: §1.1, T4. Caveat: this needs sponsors or a consortium, and the grant bounds the freedom (Contradiction 1).
2. **Question the student until each conclusion fits in a sentence, then work on the manuscript together, at length.** Evidence: §1.2, T1, T10.
3. **Put one shared code base at the centre.** Each student's algorithm lands in it, and later students use it as their test bed. Evidence: §3.3, §2.4. Caveat: this needs a long-lived solver and someone to maintain it, here a company.
4. **Build a mentoring layer of postdocs and senior students, and keep your best graduates as postdocs for a while.** Evidence: §3.2, §2.6. Caveat: this needs postdoc funding.
5. **Start each student with a cheap, complete first project before committing to a long line**: an MS thesis at UIUC, MS pairs at CMU. Evidence: §2.4–2.5. Caveat: this needs a master's program.
6. **Make the sponsor's engineer a co-mentor and committee member, and send students on internships.** Evidence: §3.4, T8, T9.
7. **Expect to learn the student's new field with them**, and take or send them to the mathematics course it needs. Evidence: T7, T12.

## Contradictions (kept, not reconciled)
1. **Freedom vs. sponsored topics** [inferred tension]. Five students describe the freedom to explore (§1.1). Their own acknowledgements tie their topics to sponsors:
   - Dow for Amaran, Austin and Rajagopalan (Rajagopalan thanks Dow "for supporting the research on turnaround planning");
   - ExxonMobil, partly, for Sun;
   - IDAES for Sauk and Sarwar.
2. **Openness vs. pressure** [observed]. Austin: "so open to my exploring almost every idea I had". Sauk: "constantly pushed me". Kuznetsov: "constantly challenging me". These may describe different students, years or needs. The sources do not say.
3. **Sun's co-advisor**. Sun's thesis (p. iv) names Lorenz Biegler as "my co-advisor in the last year of my PhD". The CV (§V.B1, entry 29) lists Sun with no co-supervisor, although it records co-supervision for Khajavirad, Hubbs, Li and Choudhary.
4. **The group page disagrees with itself and with the CV**. The live "Group" page lists Kaiwen Ma, Owais Sarwar and Yijiang Li under "Current Group Members". It also lists the same three under "Past Members", with degree years 2022, 2022 and 2023. It lists Anatoliy Kuznetsov as current, while the CV has him graduating in 2024. (06 records the same staleness.)
5. **Placement**. For Zachary Wilson, the group page gives "The Dow Chemical Company, Freeport, Texas" and the CV gives "Air Liquide, Newark, Delaware".
6. **Thesis titles, group page vs. CV**.
   - Vaia: "Global optimization in least squares problems in FTIR spectroscopy and X-ray crystallography" (page) vs. "Least squares problems with applications in parameter estimation in FTIR spectroscopy and X-ray crystallography" (CV).
   - Xie: "Optimization in protein bioinformatics" (page) vs. "Optimization algorithms for protein bioinformatics" (CV). The IDEALS title indexed by OpenAlex is "Optimization Algorithms for Protein Bioinformatics".
7. **Shabbir Ahmed's birth year**. The group's news page says "Shabbir Ahmed (1970-2019)". The INFORMS Journal on Computing memoriam is titled "In Memoriam: Shabbir Ahmed (1969–2019)" (Crossref, DOI 10.1287/ijoc.2019.0931; its text was not read).
8. **Number of doctoral students**. The Mathematics Genealogy Project lists 9; the CV lists 36 (06, Contradiction 8; not re-checked here).

## Gaps
- **Theses not read: 23 of the 36 graduated PhDs.** Liu 1995, Ryoo 1999, Shectman 1999, Ahmed 2000, Tawarmalani 2001, Furman 2002, Vaia 2003, Chang 2006, Xie 2007, Smith 2008, Rios 2009, Bao 2009, Shah 2011, Samudra 2012, Zorn 2013, Yan Zhang 2013, Cozad 2014, Puranik 2016, Wilson 2019, Tong Zhang 2019, Engle 2021, Ma 2022 and Choudhary 2026. The reasons:
  - not deposited in KiltHub (Figshare searches by title and by author found none);
  - IDEALS returned HTTP 403, and its Chang and Rios files are flagged restricted;
  - Choudhary's thesis was not yet in Georgia Tech's repository on 2026-10-10.

  No circumvention was attempted.
- **No first-person account of his advising.** No interview, lecture, podcast or essay about how he supervises was found; two WebSearch calls aimed at interviews and recollections returned only profiles. Everything about his style comes from students, plus the recruiting page and the Ahmed memoriam.
- **No public lab guide or onboarding document.** The UIUC `invite/student/` area (HTTP 401) and the CMU member login were not accessed.
- **No student blog or memoir found.** Christian Hubbs's former blog domain (datahubbs.com) is now a parked domain-for-sale page.
- **No testimony from co-advisors or partners** about supervising with him: Grossmann, Dey, Nemhauser, Michalek, Raghunathan, Miller. The co-advised acknowledgements (Hubbs, Li) mostly praise both advisors together.
- **No Festschrift or tribute volume** for Sahinidis was found (Crossref queries).
- **Not read**:
  - J. C. Smith, "In Memoriam: Shabbir Ahmed (1969–2019)", *INFORMS J. Comput.* 31(4):633–635, 2019 (title and metadata only).
  - Biegler, Gounaris, Sahinidis & Ydstie, "Educator Profile: Ignacio Grossmann of Carnegie Mellon University", *Chem. Eng. Educ.* 53(3), 2019 (DOI 10.18260/2-1-370.660-114401). It has four co-authors, so nothing in it could be attributed to Sahinidis alone.
  - *The Unofficial Guide to the Walt Disney World* (the name used on his group page), which that page says thanks him and his students.
- **Not documented in anything found**: group-meeting frequency and format, authorship rules, code-review or software-engineering practice for students, how topics are assigned, time to degree, attrition, conflicts, and what MS students experienced (only their thesis titles are public).
- **The MS-to-release link** (ALAMO-Fortran, 2013) is inferred from matching dates only.
- **Era bias.** The 1995–2001 UIUC cohort, his academic descendants, is seen only through co-signed and roster material, never in a student's own words.

## Sources

**Primary (P)**
1. Sahinidis Optimization Group, "Student Openings" (Georgia Tech), undated, live 2026-10-10. https://sahinidis.coe.gatech.edu/student-openings. P
2. Sahinidis Optimization Group, "Group" (current and past members; PhD, MS and BS theses with placements), undated, live 2026-10-10. https://sahinidis.coe.gatech.edu/group. P
3. Sahinidis Optimization Group, "News" (20 items, 2000–2022), live 2026-10-10. https://sahinidis.coe.gatech.edu/news. P
4. Sahinidis, N. V., *Curriculum Vitae*, 76 pp., footer "Nick Sahinidis, 7 October 2026" (§III.B–C and §V.A–C read). https://sahinidis.coe.gatech.edu/sites/default/files/content/nikos/NVS%20cv.pdf. P
5. "Optimizing for fun" (unsigned group page, dated December 2009 on the news page), Wayback snapshot 2010-06-16. http://archimedes.cheme.cmu.edu/group/optifun.html. P
6. CMU group site, "Student openings", Wayback snapshot 2008-07-24. http://archimedes.cheme.cmu.edu/group/openings.html. P
7. CMU group site, "Group members", Wayback snapshot 2008-07-24. http://archimedes.cheme.cmu.edu/group/members.html. P
8. CMU group site, "Current Group Members", Wayback snapshot 2013-03-20. http://archimedes.cheme.cmu.edu/?q=currentgroup. P
9. UIUC group site, "Graduate Students" and "Visitors", Wayback snapshots 1998-12-07. http://archimedes.scs.uiuc.edu/group/students.html and http://archimedes.scs.uiuc.edu/group/visitors.html. P
10. UIUC group site, "The Sigma Optimization Group" home page, Wayback snapshot 2003-05-06. http://archimedes.scs.uiuc.edu/index.html. P
11. UIUC group site, "Student openings", Wayback snapshot 2007-06-21. http://archimedes.scs.uiuc.edu/group/openings.html. P
12. Tawarmalani, M. & Sahinidis, N. V., *Convexification and Global Optimization in Continuous and Mixed-Integer Nonlinear Programming*, Kluwer (Springer), 2002. DOI 10.1007/978-1-4757-3532-1. Front matter read: dedication, Preface pp. xiii–xvi, Acknowledgments pp. xvii–xviii. P
13. Sahinidis, N. V., his statement in "In Memoriam: Shabbir Ahmed", Georgia Tech ISyE news, 1 Jul 2019. https://www.isye.gatech.edu/news/memoriam-shabbir-ahmed. P (his own words)
14. The Optimization Firm, "Our Team", live 2026-10-10. https://minlp.com/our-team. P
15. The Optimization Firm, "ALAMO release notes" (entry 2013.10). https://minlp.com/alamo-release-notes. P
16. The Optimization Firm, "BARON user manual" web page, checked for contributor credits; none are listed. https://minlp.com/baron-user-manual. P
17. Vander Wiel, R. J. & Sahinidis, N. V., "Heuristic bounds and test problem generation for the time-dependent traveling salesman problem", *Transportation Science* 29(2):167–183, 1995. DOI 10.1287/trsc.29.2.167. P
18. Vander Wiel, R. J. & Sahinidis, N. V., "An exact solution approach for the time-dependent traveling-salesman problem", *Naval Research Logistics* 43(6):797–820, 1996. DOI 10.1002/(sici)1520-6750(199609)43:6<797::aid-nav2>3.0.co;2-#. P
19. Vander Wiel, R. J. & Sahinidis, N. V., "The assignment problem with external interactions", *Networks* 30(3):171–185, 1997. DOI 10.1002/(sici)1097-0037(199710)30:3<171::aid-net3>3.0.co;2-i. P
20. Sahinidis, N. V. & Grossmann, I. E., "MINLP model for cyclic multiproduct scheduling on continuous parallel lines", *Comput. Chem. Eng.* 15(2):85–103, 1991. DOI 10.1016/0098-1354(91)87008-w. P
21. Tawarmalani, M., Ahmed, S. & Sahinidis, N. V., "Product Disaggregation in Global Optimization and Relaxations of Rational Programs", *Optim. Eng.* 3(3):281–303, 2002. DOI 10.1023/A:1021043227181. P
22. Tawarmalani, M., Ahmed, S. & Sahinidis, N. V., "Global Optimization of 0-1 Hyperbolic Programs", *J. Global Optim.* 24(4):385–416, 2002. DOI 10.1023/A:1021279918708. P
23. Sahinidis, N. V., Tawarmalani, M. & Yu, M., "Design of alternative refrigerants via global optimization", *AIChE J.* 49(7):1761–1775, 2003. DOI 10.1002/aic.690490714. P
24. Wilson, Z. T. & Sahinidis, N. V., "The ALAMO approach to machine learning", *Comput. Chem. Eng.* 106:785–795, 2017. DOI 10.1016/j.compchemeng.2017.02.010. P

**Secondary (S): accounts by students and others**
25. Elble, J. M., "Computational experience with linear optimization and related problems", PhD thesis, Industrial Engineering, UIUC, 2010. hdl:2142/16820 (IDEALS); read from the Internet Archive copy of the public PDF, snapshot 2017-08-13. Acknowledgments p. v. S
26. Khajavirad, A., "Convexification Techniques for Global Optimization of Nonconvex Nonlinear Optimization Problems", PhD thesis, Mechanical Engineering, CMU, 2011. https://www.cmu.edu/me/ddl/publications/2011-Dissertation-Khajavirad.pdf. Acknowledgements PDF p. 6. S
27. Amaran, S., "Interactions of Uncertainty and Optimization: Theory, Algorithms, and Applications to Chemical Site Operations", PhD thesis, CMU, 2014. DOI 10.1184/R1/6720266.v1. pp. v–vi. S
28. Austin, N. D., "Tools for Computer-Aided Molecular and Mixture Design", PhD thesis, CMU, 2017. DOI 10.1184/R1/6723932.v1. pp. v–vi. S
29. Rajagopalan, S., "Design and Maintenance Planning Problems in Commodity Distribution and Chemical Site Networks", PhD thesis, CMU, 2018. DOI 10.1184/R1/6715784.v1. pp. iii–iv. S
30. Nohra Khouri, C. J., "Novel Relaxation Techniques for Global Optimization of NLPs and MINLPs", PhD thesis, CMU, 2020. DOI 10.1184/R1/12584804.v1. pp. iii–iv. S
31. Sauk, B., "GPU Algorithms for Large-Scale Optimization", PhD thesis, CMU, 2020. DOI 10.1184/R1/13194722.v1. pp. i–ii. S
32. Hubbs, C., "Methods and Applications of Deep Reinforcement Learning for Chemical Processes", PhD thesis, CMU, 2021. DOI 10.1184/R1/14718714.v1. pp. i–iii. S
33. Sun, Y., "Physical properties and chemical product design", PhD thesis, CMU, 2021 (KiltHub record 2022). DOI 10.1184/R1/19145945.v1. pp. iv–v. S
34. Johnson, B. J., "Time Series Analysis in Drug Product Development and Statistical Forecasting", PhD thesis, CMU, 2022. DOI 10.1184/R1/21520851.v1. pp. iii–iv. S
35. Sarwar, O., "Algorithms for Interpretable High-Dimensional Regression", PhD thesis, CMU, 2022 (KiltHub record 2023). DOI 10.1184/R1/22138049.v1. pp. i–ii. S
36. Li, Y., "Decomposition Algorithms for Certain Integer Problems over Networks", PhD thesis, ISyE, Georgia Tech, 2023. hdl:1853/72737. pp. v–vi. S
37. Kuznetsov, A., "Convexification and Global Optimization of Problems Involving the Euclidean Norm", PhD thesis, ChBE, Georgia Tech, 2024. hdl:1853/78549. p. iv. S
38. Huang, R., "Nonlinear Model Predictive Control and Dynamic Real Time Optimization for Large-scale Processes", PhD thesis, CMU, 2010. DOI 10.1184/R1/6720857.v1. Committee mention only; not informative. S
39. Vetukuri, S. R. R., "Advanced Optimization Strategies for Periodic Adsorption Processes", PhD thesis, CMU, 2011. DOI 10.1184/R1/6714614.v1. Committee mention only; not informative. S
40. CMU Chemical Engineering news, "Optimizing processes with AI", July 2018 (Wayback snapshot 2019-08-23). https://www.cmu.edu/cheme/news/2018/07_july/sahinidis-ai.html. S
41. Georgia Tech ISyE news, "Nick Sahinidis Joins ISyE as Inaugural Butler Family Chair", 2021. https://www.isye.gatech.edu/news/nick-sahinidis-joins-isye-inaugural-butler-family-chair. S
42. Georgia Tech ISyE news, "ISyE Welcomes Nick Sahinidis", 2020 (gives his start date, 15 Aug 2020). https://www.isye.gatech.edu/node/6837. S
43. Georgia Tech ISyE, "In Memoriam: Shabbir Ahmed", 1 Jul 2019. The page as a whole; other contributors' memories used only as context. https://www.isye.gatech.edu/news/memoriam-shabbir-ahmed. S
44. Smith, J. C., "In Memoriam: Shabbir Ahmed (1969–2019)", *INFORMS J. Comput.* 31(4):633–635, 2019. DOI 10.1287/ijoc.2019.0931. Crossref metadata only; text not read. S
45. CMU Chemical Engineering news, "Professor Nick Sahinidis to receive the Steven J. Fenves Award for Systems Research", 2012 (Wayback snapshot 2014-12-21). Award citation only; nothing on students. http://www.cmu.edu/cheme/news/archived-news/2012/sahinidis-fenves-award.html. S
46. CMU Chemical Engineering news, "Nick Sahinidis receives AIChE's Computing in Chemical Engineering Award", 2010 (Wayback snapshot 2014-12-20). Award citation only. http://www.cmu.edu/cheme/news/archived-news/2010/sahinidis-aiche-computing.html. S

Registries and indexes used to find or verify sources, not as sources of claims, all queried 2026-10-10: the Crossref REST API (14 DOIs checked in this run), the OpenAlex API, the Figshare API (CMU KiltHub), the DSpace API of Georgia Tech's repository, and the Internet Archive CDX API.
