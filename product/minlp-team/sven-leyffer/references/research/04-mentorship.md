# Sven Leyffer · 04 Students, collaborators and group culture (research agent 04)

| Field | Value |
|---|---|
| Researcher | Sven Leyffer (Argonne National Laboratory, Mathematics and Computer Science Division; PhD Dundee with Roger Fletcher) |
| Dimension | 04 · Mentorship: students, postdocs, visitors and collaborators; supervision style, group habits, lab culture, tacit knowledge (framework §一 layer 7; §二 agent 4) |
| Research date | 2026-10-10 |
| Sources consulted | 41 (18 primary, 23 secondary). Inside them: 27 arXiv full texts and 58 Crossref records. Numbered M01–M41 under Sources |
| Web searches | 2 of the 2 allowed. Neither returned a student account; every finding below comes from direct fetches of known URLs, APIs and archives |
| User-supplied material | None. `references/sources/{papers,talks,essays,software}` held only `.gitkeep`; `private/` was not opened |

## How to read this file

- Tags: **[stated]** = Leyffer's own words; **[practice]** = what the record shows he did (papers, code, pages he maintains, author lists); **[observed]** = what other people say about him; **[inferred]** = my reading of the evidence. **P** = primary, **S** = secondary. As the task requires, every account by another person of his mentoring is marked secondary, even when it is first-hand.
- Page numbers are PDF page numbers of the file I read, unless "printed p." is given.
- **The structural fact behind everything here.** Leyffer has spent his career at a national laboratory, not in a university department. The Mathematics Genealogy Project lists him with "No students known" [M14]. His juniors are summer graduate students, visiting PhD students, postdocs and early-career staff, plus students of university colleagues. Where a source I read does not give a junior's job title (postdoc, staff), I give only the affiliation printed on the joint paper.
- **The evidence is thin where it matters most.** I found three first-hand statements by juniors, all thesis acknowledgements: Curtis 2007, Abhishek 2008 and Kim 2022. I found no memoir, blog post, interview, lab guide or Festschrift about his supervision. Several more dissertations were located but sit behind bot checks or 403 responses (see Gaps). Most of what follows is therefore **practice evidence** (who he wrote with, what code they used, how author lists and credits were set), with the first-hand statements layered on top.

## 0. Themes supported by two or more independent sources

| # | Theme | Evidence | Sources |
|---|---|---|---|
| T1 | A junior's project is built on the senior's solver stack, test libraries and baselines. It was done to him, and he does it in turn | Fletcher → Leyffer: bqpd "underlies this thesis" [M10 pp. 23, 77]. Leyffer → Abhishek: FilMINT is "motivated by the observation of Leyffer [1993]", runs filterSQP, tests on MacMINLP and uses MINLP-BB as the yardstick [M16 pp. 71, 72, 76]. MacMPEC was translated to CasADi for the Nurkanović–Leyffer paper [M33]. Kiessling tested Uno and then contributed code [M33, M29] | 4, all practice |
| T2 | Juniors arrive through the laboratory's programmes for graduate students, mostly for summers | Abhishek: "two summers ... under his guidance" [M16]. Givens Associate programme acknowledged [M33, arXiv:2204.05773]. NSF-MSGI fellowship [M33, arXiv:2111.10489]. DOE Office of Science Graduate Student Research programme [M33, arXiv:2410.11171]. "research opportunity at Argonne" [M18]. His homepage lists "Student and Postdoc Opportunities: Givens Associates" [M01] | 6 |
| T3 | The default author order is alphabetical, but the junior who did the work is often put first | DBLP: 50 of 86 records are alphabetical. The departures in mathematical papers mostly put a junior first (§4.5) [M34]. Shen moved from last author (2009 preprint) to first (journal) [M32, M36]. Uno: "designed and implemented by Charlie Vanaret" [M29] | 3, practice; counterexamples exist (§4.5, C8) |
| T4 | "Look at examples, look at numbers, software validates theory": received from Fletcher and visible in his own teaching | His recollection in the 2015 interview [M11 p. 4]. His 2016 obituary of Fletcher [M12 p. 2]. The memoir on single precision as an instability signal [M13 p. 12]. His 2018 exercise sheet asks students to plot a published model term and "What do you observe?" [M09] | 3 plus his own teaching artefact |
| T5 | Former juniors become independent, keep the line going, and the line feeds back to him | Mahajan: Argonne → IIT Bombay, first author of the Minotaur paper [M35, M36]. Manns: Argonne → TU Dortmund, where he supervises theses on total-variation-regularized integer optimization [M37]. Vanaret: Argonne → Zuse Institute Berlin, owns Uno [M29]. Yang: UCLA intern (2021) → Argonne (2025), then co-author with a Prague student and an IIT student [M33]. Yang, Leyffer & Bakenhus cite Manns & Severitt, Manns's own student [M33, arXiv:2508.05822] | 5, practice |

## 1. Lineage: how Leyffer was mentored (Dundee, about 1990–2002)

**1.1 The formal record**

- The thesis title page reads *Deterministic Methods for Mixed Integer Nonlinear Programming*, "PhD Thesis, Department of Mathematics & Computer Science, University of Dundee", "December 1993" [M10 p. 1; practice, P]. MGP gives "Ph.D. University of Dundee 1994", "Advisor 1: Roger Fletcher" [M14; S]. ORCID lists education at "University of Dundee", PhD, Mathematics [M38; S].
- His Bio page (last modified 16 March 2017) [M02; stated, P]: "Born in Hamburg, Germany, Sven obtained his Ph.D. in 1994 from the University of Dundee, working on mixed-integer nonlinear programming problems with Roger Fletcher. He has held postdoc positions at Dundee, Northwestern, and Argonne". His Appointments page (last edited 21 January 2025): "Research Fellow, Department of Mathematics, University of Dundee (1994-2002)" [M03; stated, P]. Argonne's 2021 news item: "After postdoctoral research positions at Dundee, Argonne, and Northwestern University, he joined the MCS division at Argonne in 2002." [M19; S]. The order of the postdoc posts differs between sources (C3).
- The memoir of Fletcher [M13 p. 13 (printed p. 139); observed, S]: "In their initial work on MINLP, which yielded Sven's PhD in 1994, Roger and Sven developed a reliable method of detecting infeasiblity [sic], and extended Duran & Grossmann's method (39) by using quadratic rather than linear models". The papers are Fletcher & Leyffer, "Solving mixed integer nonlinear programs by outer approximation", *Math. Program.* 66:327–349, 1994, DOI 10.1007/BF01581153; and Fletcher & Leyffer, "Numerical Experience with Lower Bounds for MIQP Branch-And-Bound", *SIAM J. Optim.* 8:604–616, 1998, DOI 10.1137/S1052623494268455 [M36].

**1.2 What the thesis shows about how the student worked** [practice, P]

- The advisor's code sits underneath: "The LP and QP solver that underlies this thesis is an implementation of a primal ASM with the additional feature of handling degeneracy." [M10 p. 23]. And: "The QP/LP problems are solved by bqpd." [M10 p. 77].
- Tools: "All code is written in FORTRAN 77 and uses the NAG library routine E04UCF [55] to solve the NLP problems." [M10 p. 77]. Tests were run "on a SUN-SPARC SLC using the FORTRAN 77 compiler with the -fast option" [M10 p. 43].
- A failure he reported rather than hid [M10 p. 79]: "There are no results for the quadratic outer-approximation code for the problems BATCH, GTD and GTD chain(3). This is due to severe growth of round-off error in the reduced Hessian matrix that can affect the QP solver bqpd. The solve for BATCH was aborted after more than an hour without obtaining a solution and the solves for the GTD problems were so inefficient that it was felt that they would otherwise distort the results. It is anticipated that this problem will be remedied in a future release of bqpd."
- How a side question became a chapter [stated, P]: "The introduction of MIQP master programs in Chapter 5 caused me to become interested in MIQP problems and a detailed study of branch-and-bound for MIQP problems is given." [M10 p. 16]. It became the 1998 *SIAM J. Optim.* paper above.
- The online copy (re-typeset with dvips in 2006, 118 pages) has **no acknowledgements page**, so his own thanks to Fletcher are **not read** (Gap).

**1.3 What he says he took from his mentor** [stated, P: his own words about Fletcher]

- In the 2015 interview he conducted [M11 p. 4], Fletcher says: "One thing I would say is to look at numbers: they're trying to tell you something." and "Now if you give an idea to a Ph.D. student and it doesn't work, you have no idea why he thinks it doesn't work." Leyffer answers: "So, I know when I was in Dundee, one of the things you always told us was to look at examples, so this is the same idea." Fletcher: "Part of it, yeah." (I assigned speakers from the flow of the conversation. I did not check the PDF's typographic speaker cues.)
- His obituary of Fletcher (*SIAM News* 49(10), December 2016) [M12 p. 2]:
  - "He believed that the problems people want to solve should ultimately drive applied mathematics research, and valued simple examples to expose a method's limitations."
  - "The second foundation of Roger's research philosophy was software, as he believed that software validates theory and is simultaneously a guide to good methods."
  - On bqpd supporting both precisions: "because numerical difficulties manifested themselves first in the single-precision version."
  - "However, Roger was just as suspicious of his own opinion, and not above changing his own mind."
  - Closing: "At the University of Dundee he fostered a happy environment for his many Ph.D. students and visitors. Roger selflessly provided guidance to his students, passing on to a new generation of researchers the luck and good ideas he felt he was given."
- [inferred] These are the values he chose to put on record for a mentor: problems driven by applications, small examples, code as the test of theory, self-doubt, a happy group, generosity toward students. That he names them shows what he values. It does not show that he practises them; §3–§5 report what the record shows.

**1.4 Postdoc years, and how credit flowed between mentor and junior**

- Memoir [M13 p. 13; observed, S]: "Roger's game-changing observation, in a collaboration with, his now postdoc, Sven Leyffer, is that an alternative is to consider objective function decrease and some measure of constraint violation as two separate entities." The paper is Fletcher & Leyffer, "Nonlinear programming without a penalty function", *Math. Program.* 91:239–269, 2002, DOI 10.1007/s101070100244 [M36].
- His own obituary also credits Fletcher: "(he acknowledged that his discovery of filter methods [5] made him "tingle when [he] thought about it")" [M12 p. 2; stated, P]. The INFORMS Farkas Prize citation credits Leyffer: "In later groundbreaking work with Roger Fletcher, Leyffer proposed a new class of methods for constrained nonlinear programs, which employ the innovative concept of a filter" [M22; observed, S]. Kept as contradiction C5.
- The former student kept the mentor's record: "We most appreciate the interviews and articles by Yu-Hong Dai and Sven Leyffer (Dai 2006; Leyffer 2015, 2016) as rich sources of background information. We wish to thank Sven for commenting on an earlier draft of this memoir." [M13 p. 17]. Figure 3 of the memoir: "Nick Gould, Roger Fletcher and Sven Leyffer in the Scottish Highlands, 2007 (photo courtesy of Sven Leyffer)." [M13 p. 16]. Photo caption in the interview: "Roger Fletcher and Sven Leyffer at on [sic] Meall Glas Munro in Scotland (Photo: Sven Leyffer's camera)" [M11 p. 3].
- The last joint paper with the mentor carries a junior as first author. The Argonne preprint ANL/MCS-P1679-0909 (14 October 2009) lists "Roger Fletcher, Sven Leyffer, and Chungen Shen", with Shen's footnote "Mathematics and Computer Science Division, Argonne National Laboratory" [M32 pp. 1–2]. The journal version is Shen, Leyffer & Fletcher, "A nonmonotone filter method for nonlinear optimization", *Comput. Optim. Appl.* 52:583–607, DOI 10.1007/s10589-011-9430-2 [M36]. Who decided the change is not documented. His Bio page calls the co-author "Chungen Chen" [M02] (C6).
- [inferred] The mentor relationship ran from the PhD (thesis 1993) through the 2012 paper to the memoir work after Fletcher's death in 2016. It was a working partnership for two decades, not a handover at graduation.

## 2. Who his juniors were

The status column gives the affiliation printed on the joint paper (from the paper itself, or from OpenAlex raw affiliation strings [M35]). Job titles are not verified unless a source says so.

| Junior | Status at the time (source) | Joint work (identifier, verified) | How the link is documented |
|---|---|---|---|
| Kumar Abhishek | Lehigh PhD student, advisor Linderoth. "two summers ... at Argonne National Laboratory under his guidance". Leyffer on the committee [M16 pp. 2, 4] | FilMINT, *INFORMS J. Comput.* 22:555–567, 2010, DOI 10.1287/ijoc.1090.0373 | First-hand acknowledgement [observed, S] |
| Gabriel López-Calva | Northwestern (Nocedal group); Curtis's officemate [M15 p. 5] | *SIAM J. Optim.* 17:52–77, 2006, DOI 10.1137/040621065 | Practice. Thesis not located |
| Frank E. Curtis | Northwestern PhD student of Nocedal; no joint paper with Leyffer in DBLP [M34] | — | First-hand acknowledgement [observed, S] |
| Chungen Shen | Argonne MCS on the 2009 preprint [M32]; Shanghai Finance University on the journal version [M35] | DOI 10.1007/s10589-011-9430-2 | Practice |
| Ashutosh Mahajan | Argonne MCS in 2011–2012 papers; IIT Bombay from 2013 [M35]. His May 2009 Lehigh thesis (director Ralphs) does not mention Leyffer [M17] | SC 2012, DOI 10.1109/SC.2012.62; *Acta Numer.* 22:1–131, 2013, DOI 10.1017/S0962492913000032; "Minotaur: a mixed-integer nonlinear optimization toolkit", *Math. Program. Comput.* 13:301–338, DOI 10.1007/s12532-020-00196-1 | Practice |
| Noam Goldberg | Argonne MCS (2013); Bar-Ilan University (2014 on) [M35] | SDM 2013, DOI 10.1137/1.9781611972832.50; *COAP* 58:523–541, 2014, DOI 10.1007/s10589-014-9647-y; *SIAM J. Optim.* 25:1455–1477, 2015, DOI 10.1137/140958025; *Networks* 66:145–158, 2015, DOI 10.1002/net.21619; *COAP* 79:223–233, 2021, DOI 10.1007/s10589-021-00268-5 | Practice. Joint papers continued for eight years after he left |
| Youngdae Kim | UW–Madison (2014); Argonne (2020–2021) [M35] | DOI 10.1007/s10589-014-9647-y; DOI 10.1007/s10589-021-00268-5 | Practice |
| Christian Kirches | Heidelberg; the *Acta Numerica* 2013 record lists Argonne and Heidelberg [M35]; later TU Braunschweig | "TACO: a toolkit for AMPL control optimization", *Math. Program. Comput.* 5:227–265, 2013, DOI 10.1007/s12532-013-0054-7; *SIAM J. Optim.* 32:75–99, 2022, DOI 10.1137/20M1370501 | Practice. Nature of the Argonne stay not verified |
| Fu Lin | Argonne MCS (fulin@mcs.anl.gov on the 2015 preprint) [M33, arXiv:1504.04589] | *COAP* 65:1–46, 2016, DOI 10.1007/s10589-016-9842-0; ACC 2016, DOI 10.1109/ACC.2016.7526801 | Practice |
| Zichao (Wendy) Di | Argonne MCS, 2016–2026 [M35] | *SIAM J. Imaging Sci.* 9:1–23, 2016, DOI 10.1137/15M1021404; *SIAM J. Sci. Comput.* 41:B497–B521, 2019, DOI 10.1137/18M121993X; ISBI 2026, DOI 10.1109/ISBI61048.2026.11515614 | Practice |
| Ashish Tripathi; Siwei Wang | Argonne MCS (2013–2015) [M35] | *Procedia Comput. Sci.* 51:815–824, 2015, DOI 10.1016/j.procs.2015.05.205; SIGGRAPH 2013 Posters, DOI 10.1145/2503385.2503481 | Practice |
| Prashant Palkar | IIT Bombay (2017) [M35] | e-Science 2017, DOI 10.1109/ESCIENCE.2017.27; *J. Glob. Optim.* 80:439–477, 2021, DOI 10.1007/s10898-020-00978-w | Practice. His advisor was not verified |
| Charlie Vanaret | Argonne MCS (2020 survey); Fraunhofer ITWM (2020); Argonne and ZIB (2024–2026) [M35, M29] | *Math. Methods Oper. Res.* 92:343–376, 2020, DOI 10.1007/s00186-020-00713-x; *INFOR* 58:342–373, 2020, DOI 10.1080/03155986.2020.1730676; *Math. Program. Comput.* 2026, DOI 10.1007/s12532-026-00310-9 (arXiv:2406.13454); *Math. Program.* 217:323–367, 2025, DOI 10.1007/s10107-025-02284-3 | Practice |
| Paul Manns | Argonne (2021 *COAP* paper); TU Dortmund from 2021 [M35, M33] | *COAP* 79:193–221, 2021, DOI 10.1007/s10589-020-00262-3; *ESAIM COCV* 28:66, 2022, DOI 10.1051/cocv/2022059; DOI 10.1137/20M1370501; *J. Nonsmooth Anal. Optim.* 4, 2023, DOI 10.46298/jnsao-2023-10164; *Math. Program.* 218:245–290, 2025, DOI 10.1007/s10107-024-02181-1, with its 2026 correction (§6) | Practice |
| Mirko Hahn | Magdeburg (Sager group) [M35]. Dissertation "Fast methods for mixed-integer PDE-constrained optimization" (2025) located, not read [M37] | *Math. Program.* 197:147–190, 2022, DOI 10.1007/s10107-021-01733-z; DOI 10.46298/jnsao-2023-10164 | Practice |
| Anna Thünen | Affiliation not checked | *Optim. Control Appl. Methods* 43:867–883, 2022, DOI 10.1002/oca.2861 | Practice |
| Ahmed Attia; Johannes J. Brust; Mohan Krishnamoorthy; Brian Dandurand; Bowen Li; Matt Menickelly | Argonne in their 2020–2025 joint papers [M35, M33] | e.g. *SIAM J. Sci. Comput.* 44:B395–B427, 2022, DOI 10.1137/21M1404363; *COAP* 80:55–88, 2021, DOI 10.1007/s10589-021-00297-0; *Comput. Phys. Commun.* 261:107663, 2021, DOI 10.1016/j.cpc.2020.107663; *SIAM J. Optim.* 31:702–726, 2021, DOI 10.1137/19M127611X; arXiv:2302.12306; DOI 10.1080/03155986.2020.1730676 | Practice |
| Ryan H. Vogt | 2022 affiliation not given in the metadata I read; NSA in 2025 [M35] | *SIAM J. Sci. Comput.* 44:B29–B50, 2022, DOI 10.1137/20M1315993; *COAP* 90:337–360, 2025, DOI 10.1007/s10589-024-00644-x | Practice |
| Dominic Yang | UCLA; "The first author was also supported through an NSF-MSGI fellowship." (2021) [M33, arXiv:2111.10489]. Argonne MCS by 2025 (dominic.yang@anl.gov) [M33, arXiv:2508.05822] | *COAP* 83:759–800, 2022, DOI 10.1007/s10589-022-00404-9; arXiv:2508.05822; arXiv:2509.19888 | Practice |
| Jongeun Kim | Minnesota PhD student, advisor J.-P. Richard [M18] | *INFORMS J. Comput.* 35:1383–1403, 2023, DOI 10.1287/ijoc.2022.0050 | First-hand acknowledgement [observed, S] |
| Xinyu Fei | Michigan IOE, Siqian Shen's group [M33, arXiv:2204.05773] | *Quantum* 7:892, 2023, DOI 10.22331/q-2023-01-04-892; *INFORMS J. Comput.* 37:86–106, 2025, DOI 10.1287/ijoc.2024.0560; *ACM Trans. Quantum Comput.* 6, 2025, DOI 10.1145/3670416 | The paper acknowledges the Givens programme |
| David Kiessling | KU Leuven and Flanders Make [M33, arXiv:2409.09208] | DOI 10.1007/s10107-025-02284-3 (arXiv:2409.09208) | Practice; tested Uno and contributed to it [M29, M33] |
| Karen Medlin | UNC Chapel Hill; DOE Office of Science Graduate Student Research programme [M33, arXiv:2410.11171] | arXiv:2410.11171; IJCNN 2025, DOI 10.1109/IJCNN64981.2025.11227944 | Practice |
| Armin Nurkanović | Freiburg (IMTEK) [M33, arXiv:2501.13835] | arXiv:2501.13835 | Practice |
| Harsh Choudhary; Miles Bakenhus | Czech Technical University in Prague, funded by GAČR; Illinois Institute of Technology [M33] | arXiv:2509.19888; arXiv:2508.05822 (both with Yang) | Practice |
| Thomas F. Lynn; Nicole Aretz | Johns Hopkins APL (2025 preprint), then Argonne (2026 paper); UT Austin, Oden Institute [M33, M35] | arXiv:2509.15961; DOI 10.1109/ISBI61048.2026.11515614 | Practice |

[inferred] The breadth is large: more than thirty juniors over 2006–2026. The depth per person is small: for most there is only a joint paper and an affiliation.

## 3. Supervision style

**3.1 What juniors said (first-hand, in thesis acknowledgements)** [observed, S]

- According to Kumar Abhishek (PhD thesis *Topics in Mixed Integer Nonlinear Programming*, Lehigh, April 2008, PDF p. 4): "Special thanks are due to Dr. Sven Leyffer for his guidance, knowledge and enthusiasm in discussing topics relevant to my work in this dissertation. The two summers that I spent at Argonne National Laboratory under his guidance were a great learning experience for me, as well as a lot of fun. He has been a great source of inspiration for me during this time." Leyffer sat on the committee (PDF p. 2: Ralphs, chair; Linderoth; Leyffer; Isaak). The advisor credited with day-to-day guidance is Linderoth (same page).
- According to Jongeun Kim (PhD thesis, Minnesota, May 2022, PDF p. 3): "I would like to thank Dr. Sven Leyffer and Dr. Prasanna Balaprakash for giving me a research opportunity at Argonne National Laboratory and introducing me to the topic of symbolic regression."
- According to Frank E. Curtis (PhD thesis, Northwestern, 2007, PDF p. 5), a student of another advisor: he thanks "Andreas Wächter and Sven Leyffer, for exhibiting to me the levels of creativity and intelligence in a researcher that I can only hope to achieve."
- [inferred] What the three share: Leyffer appears as the host who supplies the problem and the topic (symbolic regression; LP/NLP-based branch and bound on top of his own codes), and as a model of a researcher. He does not appear as the day-to-day thesis supervisor. None of the three says anything about meeting frequency, feedback on drafts, or how he handled a stuck student.

**3.2 How he scopes a project for a junior worker: a 2026 brief and session log**

Caveat first: this brief was written for an AI research assistant, not a human student. It is the only document I found in which he sets out, in his own words, how a junior should attack a research problem. Whether he briefs students the same way is unknown.

- From `CLAUDE.md` in github.com/leyffer/conDFO, July 2026 [M26; stated, P]:
  - "Design a sequential algorithm for constrained derivative-free optimization (DFO) and proof [sic] its convergence properties".
  - Two key references are given up front: a survey by his Argonne colleagues (Larson, Menickelly & Wild, "Derivative-free optimization methods", *Acta Numer.* 28:287–404, 2019, DOI 10.1017/S0962492919000060), and his own filter-convergence paper (Fletcher, Leyffer & Toint, "On the Global Convergence of a Filter--SQP Algorithm", *SIAM J. Optim.* 13:44–59, 2002, DOI 10.1137/S105262340038081X) [M36].
  - A "**Novelty:**" paragraph, a "Suggested Approach", and four numbered "Algorithmic Choices".
  - An "Outline of Convergence Proof" ending with "Transfer as much of the proofs from the DFO paper and the filter paper." and "Clearly identify gaps that may require new ideas, and discuss."
- The record-keeping he requires [M26; stated, P]: "Create a `LOGBOOK.md` file"; "After creating a plan, write a summary of the plan to plans/YEAR-MM-DD-shortTitle.md"; before ending each session, "Update the `LOGBOOK.md`" and "Create or overwite [sic] a `STATUS.md` file that captures the current status of the project"; when starting a session, read the brief, the logbook and the status file.
- How he rules on results. The logbook was written by the assistant and records his decisions; the wording is the log's, not his [M26, LOGBOOK.md, 2026-07-15; practice, P]:
  - "**Design decisions (with Sven):** Cauchy-decrease (FGLT-style) proof architecture with normal/tangential steps instead of FLT02's global-QP solves; restoration as an oracle assumption; explicit criticality safeguard".
  - "**Gap rulings (Sven, same day):** boundary-models, restoration realization, and complexity stay as documented open problems".
  - Also: "the stability-lemma constant tracking is scheduled for next session (constants must depend only on problem properties such as Lipschitz constants); LICQ on the whole feasible set is retained for now".
  - The same log records that the assistant found "an unstated existence assumption in its chain construction" in a proof of his own 2002 filter paper, "replaced by a compactness argument (Remark in the paper)". He left this criticism of his own earlier work in a public log. I did not check the claim.
- [inferred] The pattern: hand the junior the two papers whose proofs are to be combined, say what is new, list the design choices, require a written record, and then decide which gaps stay open and documented instead of being closed by overclaiming. "Constants must depend only on problem properties" is a standard of taste that he applies when he accepts a proof.

**3.3 Who brings the problem** [practice, P; observed, S]

- Problems often come from Argonne facility scientists and are worked on with juniors: "We are grateful to Stefan Vogt, Si Chen, Doga Gursoy, and Francesco De Carlo for introducing us to this problem" (Austin, Di, Leyffer & Wild, arXiv:1902.02027; *SIAM J. Sci. Comput.* 41, 2019, DOI 10.1137/18M121993X) [M33].
- Kim's acknowledgement (§3.1) says the hosts introduced the topic. Abhishek's FilMINT chapter: "Our work is motivated by the observation of Leyffer [1993] that a simplistic implementation of this algorithm often outperforms nonlinear branch-and-bound and outer approximation by an order of magnitude." [M16 p. 71]. The student was handed an open question from the host's own thesis.
- The programme that frames these summer projects: "Givens Associates will work actively with MCS scientists designing, analyzing, and implementing numerical algorithms." [M24; S].

**3.4 Formal roles** [stated, P, from his own appointments list M03, unless noted]

- External member of a Lehigh PhD committee (Abhishek, 2008) [M16 p. 2; practice].
- "Adjunct Professor in the Department of Electrical Engineering & Computer Science, Northwestern University (2006-2012)". I found no Northwestern student of his (Gap).
- Fellow (2004–2010), then Senior Fellow (2010–), of the Computation Institute, University of Chicago.
- Roles serving early-career people across the community: "Chair, SIAM/ICIAM Young Researcher Travel Awards (2011)"; "Member, SIAM Working Group on Professional Development (2015-2017)"; "Panelist, mid-career panel, SIAM Conference on Computational Science and Engineering (2019)".
- As SIAM president-elect, according to ICERM his plans were "to focus on expanding diversity, equity, and inclusion, enhancing membership and meetings, broadening the impact of the industry, and improving SIAM's global stature" [M20; reported, S]. His own quoted words at the time were about the field, not about mentoring: "SIAM provides a critical bridge between academia and industry, and this is an exciting time for the community as we delve into new areas such as machine learning where optimization may have a decisive impact." [M19; stated, reported in S].

## 4. Group habits and lab culture

**4.1 The channels juniors come through** [practice]

- His homepage (last edited 10 March 2023) lists "Student and Postdoc Opportunities:" → "Givens Associates", and the seminar "LISTn: LANS Informal Talks Network" [M01; P].
- The Givens Associates page (Argonne MCS, January 2017) [M24; S]: "The Givens Associate positions are intended to encourage graduate students who are beginning careers in numerical analysis or computational mathematics." "Appointments are made for 10 to 12 summer weeks and may be renewed for a second summer." Stipend: "$4,300 to $4,500 per month". [inferred] Abhishek's "two summers" [M16] fits the renewable format.
- Programmes named in joint papers [M33]:
  - "The authors gratefully acknowledge the support from the Givens Associate program in Argonne National Laboratory." (Fei, Brady, Larson, Leyffer & Shen, arXiv:2204.05773v3).
  - "The first author was also supported through an NSF-MSGI fellowship." (Yang, Balaprakash & Leyffer, arXiv:2111.10489v1).
  - "Office of Science Graduate Student Research program" (Medlin, Leyffer & Raghavan, arXiv:2410.11171v3).
  - "HC acknowledges support from GAČR under Project 24-11664S" (Choudhary, Leyffer & Yang, arXiv:2509.19888v2).
- Teaching abroad and at summer schools [M04; stated, P]: "GIAN course taught in January 2024 at IIT Bombay"; a "GIAN Course taught at Jabalpur Engineering College"; the "Optimization of Dynamical Systems" summer school, "September 3rd - 7th 2018, University of Bremen, Germany"; the "MINOA Summer School: Mixed-Integer PDE-Constrained Optimization"; the "2013 Graduate School in Systems,Optimization, Control and Networks". [inferred] The IIT Bombay link also runs through Mahajan (IIT Bombay from 2013) and Palkar (IIT Bombay; co-author in 2017 and 2021).

**4.2 Seminar culture (division level, not specific to Leyffer)** [practice, S]

- LISTn (January 2017): "LANS informal seminar talks provide an informal forum for the discussion of topics related to applied mathematics, scientific computing, and numerical analysis. Talks are held Wednesdays at 3pm". At that time it was run by Jeffrey Larson [M25].
- Its "Helpful Hints for Speakers" (author not stated) [M25]:
  - "The seminars are informal so talks do not have to be perfect!"
  - "Start with a 5-10 minute introduction of where your research fits into the larger scheme of things."
  - "Be prepared to answer "stupid questions" (possibly on what you consider to be textbook material)"
  - "We often ask lots of questions."
  - "Aim for 45 minutes of presentation time and allow plenty of time for questions."
- [inferred] A junior in his group would present to an applied-mathematics audience that interrupts and asks basic questions. Whether Leyffer wrote or shaped these hints is unknown.

**4.3 Shared infrastructure that juniors plug into** [practice]

- His test libraries (MacMINLP, MacMPEC, the EPEC collection and the multiobjective test problems, listed on his Research page, last modified 27 September 2012 [M08; P]) serve as the juniors' test beds:
  - Abhishek's FilMINT experiments use "the MacMINLP collection of test problems (Leyffer [2003])". He sorts instances into easy, moderate and difficult "based on the time taken using MINLP-BB (Leyffer [1998])" [M16 p. 76].
  - Nurkanović & Leyffer: "A.N. thanks Anton Pozharskiy for translating MacMPEC to CasADi" (arXiv:2501.13835v5) [M33].
- His solvers serve as the junior's base: "FilMINT is built on top of MINTO's branch-and-cut framework, using filterSQP to solve the NLP subproblems." [M16 p. 72].
- Minotaur's developer mailing list is hosted at lists.mcs.anl.gov (coin-or/minotaur README) [M30].
- The teaching kit [M05, M06, M07; P]:
  - AMPL binaries, "COIN-OR Solvers", "Argonne's MINOTAUR Solver (incl binaries for Linux/MacOS", chapters of the AMPL book, and the AMPL newsgroup for questions.
  - Matlab teaching codes (2016): "Matlab for Armijo Search", "Corrected Steepest Descend", "quasi-Newton BFGS Implementation".
- [inferred] The arrangement he had at Dundee (the student builds on bqpd; §1.2) is repeated at Argonne (the student builds on filterSQP, MINLP-BB and MacMINLP). The unwritten lesson: do not write a solver from scratch; extend the group's codes and test on the group's libraries.

**4.4 Software credit and open code** [practice]

- The Uno README, "Credits" [M29; S, written by the Uno team]:
  - "The theoretical unification framework was developed by Charlie Vanaret (Argonne National Laboratory & Zuse-Institut Berlin) and Sven Leyffer (Argonne National Laboratory)."
  - "Uno itself was designed and implemented by Charlie Vanaret."
  - The JOSS software article is by Vanaret and Montoison, without Leyffer.
- The theory paper credits testers and outside contributors (Vanaret & Leyffer, arXiv:2406.13454v2) [M33]: "We would like to thank David Kiessling (KU Leuven) for fruitful discussions about constrained optimization and his extensive testing of Uno, ... and Gail Pieper (Argonne National Laboratory) for proofreading our manuscript. We are highly grateful to the following individuals who contributed their expertise and time to the open-source implementation of Uno". Kiessling then became first author of the funnel paper (DOI 10.1007/s10107-025-02284-3) [M36].
  - [inferred] A path from tester to co-author.
  - The proofreading credit appears once in the texts I read; I do not claim it is a habit.
- Code location: "The source code and data used to generate the numerical results reported in Section 5.1 are available at https://github.com/leyffer/m2dtIceSheet." (Aretz, Lynn, Willcox & Leyffer, arXiv:2509.15961v1) [M33]. On 2026-10-10 that repository is not among the 10 public repositories of the account [M28] (C9).
- INFORMS (2016) on his software record [M22; observed, S]: "Leyffer has made strong contributions in the development of practical and freely available software"; and "He has also embarked as a coauthor on the very ambitious project MINOTAUR". The Minotaur paper's acknowledgements, as shown on the publisher page, list only funding and name no student contributors [M40].

**4.5 Authorship conventions** [practice; counts from M34, the DBLP record]

- Of 86 DBLP records with 2–8 authors, 50 list the authors alphabetically by surname. Among the 36 that do not, the mathematical papers with juniors put the junior first:
  - Guerra, Newman & Leyffer 2011, DOI 10.1137/090778286; Shen, Leyffer & Fletcher 2012; Tripathi, Leyffer, Munson & Wild 2015.
  - Lin, Di & Leyffer 2016; Lin, Leyffer & Munson 2016; Mahajan et al. (Minotaur).
  - Kim, Leyffer & Balaprakash 2021/2023; Yang, Balaprakash & Leyffer 2021/2022; Vogt, Leyffer & Munson 2022/2025.
  - Fei, Brady, Larson, Leyffer & Shen (three papers, 2023–2025); Medlin, Leyffer & Raghavan (three items, 2024–2025).
  - Aretz, Lynn, Willcox & Leyffer 2025; Lu, Lynn, Du, Di & Leyffer 2026.
  - The remaining departures are mostly multi-team computing and application papers.
- Leyffer is first author in only one of the 36 non-alphabetical records, a 2016 position paper (arXiv:1610.02606). The arXiv-only items follow the same pattern: Vanaret & Leyffer 2024; Li, Kim & Leyffer 2023; Nurkanović & Leyffer 2025; Yang, Leyffer & Bakenhus 2025 [M33].
- Counterexamples: work done with a junior can stay alphabetical with Leyffer first, as in Leyffer & Manns (2022, 2025), Leyffer & Vanaret (2020) and Leyffer, Manns & Winckler (2021) [M36]. The rule is therefore not "junior always first" (C8).
- His own first-author share, by era (DBLP; "first" includes alphabetical placement) [M34]:

  | Era | Records | Leyffer first | Solo |
  |---|---|---|---|
  | 1994–2005 | 13 | 3 | 2 |
  | 2006–2012 | 16 | 5 | 2 |
  | 2013–2020 | 25 | 4 | 0 |
  | 2021–2026 | 38 | 3 | 0 |

- [inferred] The default is the mathematical convention he worked under with Fletcher (alphabetical). He departs from it mainly when a student or junior did most of the work. The table shows his output increasingly appearing under other people's names; this is consistent with a senior who leads through juniors, but alphabetical order makes the first-author count a weak measure. Who decides author order in a given paper is not documented.

**4.6 2026: a new kind of junior** [practice, P]

- His 2026 public repositories carry AI-assistant working files (`.claude/`, `CLAUDE.md`, `LOGBOOK.md`, `STATUS.md`, dated plans). The repositories are BestPractices4AI, conDFO, QuantumOpt26, scholar-report and BQPD_jll.jl [M26, M27, M28].
- BestPractices4AI (created 27 July 2026) [M27] calls itself "A curated collection of best practices, notes, and links for working with AI". It has sections on prompt engineering, agent design, evaluation, data privacy and "curated tools, papers, and links (including Argonne-specific tools)". On 2026-10-10 its content pages are stubs of 107–553 bytes [M28]. [inferred] It is meant for other readers (it is published as a documentation site), but it is too thin yet to count as a group guide.
- [inferred] The protocol in §3.2 (brief → plan → logbook → status → his rulings on gaps) is the most explicit public record of how he directs junior work. Because it directs an AI system, it is evidence of his habits as a director of research, not of how he treats students.

## 5. Tacit knowledge (what a junior would pick up that the papers do not say)

As tacit knowledge, each item is at most [inferred]; the evidence underneath carries its own tag.

- **K1. Start from the group's codes and libraries, and use the senior's code as the yardstick.**
  - Evidence: the thesis on bqpd [M10 pp. 23, 77, 79]; FilMINT on filterSQP, MacMINLP and MINLP-BB [M16 pp. 71, 72, 76]; MacMPEC reused for Nurkanović's work [M33]. [practice → inferred]
- **K2. Look at small examples and plots before you trust a model or a method.**
  - Evidence: his recollection of Fletcher's teaching [M11 p. 4; stated]; the obituary on "simple examples to expose a method's limitations" [M12 p. 2; stated].
  - His own exercise sheet (Optimization of Dynamical Systems 2018) [M09; practice, P]. It takes a model term "published in an obscure paper" and asks: "(2.1) Plot this function (as a function of the difference d = x - y, e.g. using Matlab. What do you observe?" "(2.2) Can you deduce the modelers intention from the plot?" "(2.3) Model this expression as MIP not NLP!"
- **K3. Prove the one lemma that makes the method work, implement the method yourself in a modelling language, then compare solvers.** [M09; practice, P]
  - Exercise 3: "Show that no integer assignment can be generated twice by outer approximation. ... This essentially proves convergence of outer approximation (correctness follows from convexity)."
  - Exercise 4: "(4.2) Experiment with different solvers. What do you observe?" and "(4.3) Code outer approximation in AMPL for the quadratic facility location problem."
- **K4. Write down what is not yet proved: leave gaps documented, not papered over.**
  - Evidence: "Clearly identify gaps that may require new ideas, and discuss." [M26; stated]; the gap rulings [M26; practice, agent-written]; the 1993 thesis reporting where his code failed [M10 p. 79]; the 2026 correction (§6) [M31].
- **K5. Publish failures and corrections openly, including on papers with former juniors.** From the correction to Leyffer & Manns [M31; practice, P; mathematics rendered as plain text]:
  - "Assumption 2.7 2. in [2] lacks the box constraints on w. Without them, assuming a unique solution to (2) for all w ∈ BV(Ω) is unrealistic given that (2) may become an eigenvalue problem for suitable w."
  - "In the proof of Proposition 2.14, the limsup-inequality is incorrectly derived with a feasibility argument for the PDE (2) instead of the PDE constraining" the discretized McCormick problem.
  - Who found the errors is not stated.
- **K6. Credit goes to whoever did the work,** in author order and in software credits (§4.4–4.5). [practice → inferred]
- **K7. Keep working with juniors after they leave.** Goldberg: Argonne 2013, joint papers to 2021. Mahajan: Argonne, then the Minotaur paper in 2020/2021. Kirches: 2012 to 2022. Manns: to 2026. Vanaret: 2020 to 2026 [M34, M35, M36]. [practice]

Not recovered (see Gaps):
- how often he meets juniors;
- how he edits their drafts;
- how theory and code are split with postdocs;
- how he handles a stuck or failing junior;
- whether Fletcher's habit of using single precision as an early warning [M12; M13 p. 12] was passed on to his own juniors.

## 6. Failures, corrections and stalled items in the mentoring record

| Item | Date | What happened | Source | Tag |
|---|---|---|---|---|
| Quadratic outer-approximation runs failed on BATCH and GTD | 1993 | Round-off growth in the advisor's bqpd. BATCH "aborted after more than an hour"; the GTD runs were left out because "it was felt that they would otherwise distort the results" | M10 p. 79 | practice, P |
| Correction to Leyffer & Manns (*Math. Program.* 218:591–592, 2026, DOI 10.1007/s10107-026-02330-8) | 2026 | An assumption lacked box constraints; one proof step used the wrong PDE; both were corrected in print. The arXiv version went through five versions (v1 12 June 2024 to v5 5 January 2026) | M31, M33 | practice, P |
| Author order changed | 2009 → 2011 | The alphabetical preprint (Fletcher, Leyffer, Shen) became Shen, Leyffer, Fletcher in the journal | M32, M36 | practice, P |
| Code link not public | 2025 → 2026 | A 2025 preprint points to github.com/leyffer/m2dtIceSheet, which is not among his public repositories on 2026-10-10 | M33, M28 | practice |
| AI best-practice site | Jul–Aug 2026 | Created and published as a site; pages still stubs | M27, M28 | practice |
| Empty book repository | 2024 | The MINLO-book repository "is empty" (created 14 January 2024), with two sibling repositories (MINLO-book1, MINLPbook) created the same day | M28 | practice; purpose not verified |

I found no rejected paper, retracted claim or abandoned student project involving a junior.

## 7. Era and resource context

| Era | Role and seniority | Resources and setting | Juniors and channels |
|---|---|---|---|
| 1990–1994 | PhD student, Dundee | FORTRAN 77, SUN-SPARC SLC, NAG E04UCF, Fletcher's bqpd [M10]. Fletcher's group, including ECOSSE-funded students [M13 p. 13] | — |
| 1994–2002 | Research fellow at Dundee with Fletcher; postdoctoral posts at Northwestern and Argonne (order disputed, C3) | Filter methods; filterSQP | Fletcher's other students and visitors |
| 2002–2012 | Argonne MCS staff; Northwestern adjunct 2006–2012; Computation Institute Fellow 2004–2010; SIAM Vice President for Programs 2010–2013 [M03] | DOE ASCR funding (acknowledgements, M33); AMPL; MINTO. Abhishek's runs used a Lehigh cluster of "120 nodes of 64-bit AMD Opteron microprocessors" [M16] | Summer students (Abhishek); Northwestern contacts (López-Calva, Curtis); visitors (Shen); Argonne juniors (Mahajan, Goldberg) |
| 2013–2020 | Senior computational mathematician; editor-in-chief of *Math. Methods Oper. Res.* 2008–2014 and *Math. Program. B* 2018–2021 (dates disputed, C2) [M03] | SciDAC/FASTMath funding (acknowledgements, M33); Minotaur (Argonne, IIT Bombay, Wisconsin); X-ray imaging projects with Argonne beamline scientists | Imaging (Di, Tripathi, Wang); MINLP (Mahajan, Goldberg, Y. Kim); mixed-integer PDE-constrained optimization (Manns, Vogt, Hahn) |
| 2021–2026 | Deputy division director; SIAM President 2023–2024 (dates disputed, C1); "Argonne Distinguished Fellow" [M21] | GitHub open source (Uno, MIT licence); arXiv first; Julia packaging (BQPD_jll.jl); AI-agent workflows (2026) | Givens, MSGI and SCGSR students (Fei, Yang, Kim, Medlin); visiting PhD students (Kiessling, Choudhary); intern to staff (Yang); former juniors now professors (Manns, Mahajan) |

[inferred] Two things changed over his career: the channel (from co-supervised university students, to lab postdocs, to programme-funded summer students and visitors) and the tooling (from Fortran codes shared by licence, to open repositories with outside contributors, to AI-assisted logbooks). One thing did not change: juniors work on top of the senior's codes and libraries.

## Contradictions (kept, not reconciled)

- **C1. SIAM presidency dates.** "SIAM President (2023-2024)" on his Appointments page, edited 21 January 2025 [M03]. Argonne in 2021: he will "serve as president from January 1, 2023, to December 31, 2024" [M19]; ICERM has the same dates [M20]. But the Argonne profile captured 30 November 2025 says "He was SIAM President from 2022-2024" [M21].
- **C2. *Mathematical Programming B* editor-in-chief.** "Editor-in-Chief, Mathematical Programming B (2018-2021)" [M03] against "From 2017 to 2021" on Wikipedia [M23].
- **C3. Order of the postdoctoral posts.** His Bio (2017) says "Dundee, Northwestern, and Argonne" [M02]. Argonne's news item (2021) and profile (2025) say "Dundee, Argonne, and Northwestern University" [M19, M21]. His Appointments page has a continuous "Research Fellow ... University of Dundee (1994-2002)" [M03]. Whether the Argonne and Northwestern posts overlapped the Dundee fellowship cannot be told from these sources.
- **C4. PhD date and title.** The thesis title page says "December 1993" and "Deterministic Methods for Mixed Integer Nonlinear Programming" [M10]. MGP and Wikipedia say 1994 and "Deterministic Methods in Mixed Integer Nonlinear Programming" [M14, M23].
- **C5. Credit for the filter idea between mentor and junior.** The memoir says "Roger's game-changing observation, in a collaboration with, his now postdoc, Sven Leyffer" [M13 p. 13], and Leyffer's own obituary calls it Fletcher's "discovery of filter methods" [M12]. The INFORMS citation says "Leyffer proposed a new class of methods" with Fletcher [M22].
- **C6. Co-author's name.** His Bio page: "with Chungen Chen and Roger Fletcher" [M02]. The paper and Crossref: Chungen Shen [M36].
- **C7. Formal record against practice record.** MGP: "No students known" [M14]. A student writes of "two summers ... under his guidance" and lists him on the committee [M16], and more than thirty juniors appear in the publication record (§2). The genealogy undercounts mentoring at a national laboratory.
- **C8. Author order.** Junior-first departures from alphabetical order (§4.5) sit beside alphabetical papers with former juniors in which Leyffer comes first (Leyffer & Manns; Leyffer & Vanaret).
- **C9. Code availability.** A 2025 preprint says its code "are available at https://github.com/leyffer/m2dtIceSheet" [M33]. The public repository list of that account on 2026-10-10 does not include it [M28].
- **C10. Bibliographic years.** DBLP dates "Binary optimal control by trust-region steepest descent" to 2023 and the McCormick paper to 2026; Crossref gives 2022 (vol. 197) and 2025 (vol. 218) [M34, M36]. This only affects era counts by one year.

## Gaps (what I could not find or read)

- **No student memoir, blog post, Festschrift, lab guide, onboarding document or interview about his supervision** was found, and no essay by Leyffer giving advice to students. Two WebSearch calls (the full allowance) returned nothing of this kind.
- **Dissertations located but not read:**
  - Mirko Hahn, *Fast methods for mixed-integer PDE-constrained optimization*, Magdeburg 2025 (DNB record; the Share_it repository is behind an Anubis proof-of-work bot check, which I did not try to get around).
  - Paul Manns, *Approximation properties of Sum-Up Rounding*, TU Braunschweig 2020 (security check).
- **Dissertations not located or blocked:**
  - Xinyu Fei (Michigan Deep Blue returned 403 to curl and WebFetch).
  - Dominic Yang (UCLA eScholarship returned 403 / empty).
  - Ryan Vogt (the NC State repository timed out three times).
  - Karen Medlin, David Kiessling, Prashant Palkar, Andres Guerra and Gabriel López-Calva (not located).
  - Their acknowledgements are the best missing evidence on his supervision style from 2010 to 2025.
- **Leyffer's own thesis acknowledgements:** the online 2006 re-typeset copy has none.
- **Job titles** (postdoc or staff) for Mahajan, Goldberg, Vanaret, Manns, Lin, Di, Attia, Brust, Krishnamoorthy, Dandurand, Youngdae Kim, Li, Lynn and Yang are not verified; only paper affiliations are.
- **Advisor and status of some co-authors are not verified:** the advisor of Palkar; the nature of Kirches's Argonne affiliation in 2013; whether Choudhary, Bakenhus and Lynn were visitors or interns.
- **Northwestern adjunct period (2006–2012):** no student supervised or co-supervised by him was found.
- **SIAM presidential columns (2023–2024) and any statements on early-career researchers:** not read (siam.org returns 403; no search budget left). Argonne's own pages also return 403 to curl and WebFetch; only Wayback copies were read.
- **The 2024 GIAN lecture videos (YouTube): not read.** The lecture notes "Optimization: Applications, Algorithms, and Computation" (2016): not read (agent 02 territory).
- **Givens Associates lists with mentors:** not found; the 2024 page capture is a 404.
- **Uno and Minotaur commit histories:** not read; the GitHub API rate limit was reached.
- **No evidence was found on** meeting frequency, group meetings, how drafts are edited, how problems are assigned in person, how a stuck junior is handled, or how he reacts when a junior's result contradicts him.
- **OpenAlex full-text search** (for acknowledgements naming him) returned HTTP 429 for the second half of this run.
- **DataCite:** a search for "Leyffer" (64 records) returned no dissertation that lists him as a contributor.

## Sources

Each line gives title, author, date, URL or DOI, and P/S.

- M01 · "Sven Leyffer" (homepage, Svenleyffer MediaWiki) · S. Leyffer · last edited 10 Mar 2023, Wayback 27 Dec 2025 · https://web.archive.org/web/20251227082342/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer · P
- M02 · "Sven Leyffer's Bio" · S. Leyffer · last modified 16 Mar 2017, Wayback 17 Oct 2019 · https://web.archive.org/web/20191017082514/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer%27s_Bio · P
- M03 · "Sven Leyffer's Appointments" · S. Leyffer · last edited 21 Jan 2025, Wayback 12 Aug 2025 · https://web.archive.org/web/20250812091025/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer%27s_Appointments · P
- M04 · "Sven Leyffer's Lectures" · S. Leyffer · last edited 30 Jul 2024, Wayback 9 Oct 2024 · https://web.archive.org/web/20241009003848/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer%27s_Lectures · P
- M05 · "Course Material: Lecture Notes, Slides, Software" · S. Leyffer · last edited 1 Dec 2016, Wayback 2 Mar 2024 · https://web.archive.org/web/20240302091752/https://wiki.mcs.anl.gov/leyffer/index.php/Course_Material:_Lecture_Notes,_Slides,_Software · P
- M06 · "Course Material for ODS18: Software, Slides, Exercises, Solutions" · S. Leyffer · last edited 4 Sep 2018, Wayback 2 Mar 2024 · https://web.archive.org/web/20240302092438/https://wiki.mcs.anl.gov/leyffer/index.php/Course_Material_for_ODS18:_Software,_Slides,_Exercises,_Solutions · P
- M07 · "GianCode" (Matlab teaching codes) · S. Leyffer · last edited 14 Sep 2016, Wayback 16 Apr 2024 · https://web.archive.org/web/20240416010910/https://wiki.mcs.anl.gov/leyffer/index.php/GianCode · P
- M08 · "Sven Leyffer's Research" (test-problem libraries) · S. Leyffer · last modified 27 Sep 2012, Wayback 20 Jan 2021 · https://web.archive.org/web/20210120234151/https://wiki.mcs.anl.gov/leyffer/index.php/Research · P
- M09 · "Optimization of Dynamical Systems 2018: MINLP Exercises" (3 pp.) · S. Leyffer · 4 Sep 2018, Wayback 16 Apr 2024 · https://web.archive.org/web/20240416014915/https://wiki.mcs.anl.gov/leyffer/images/5/5d/ExercisesMINLP1.pdf · P
- M10 · *Deterministic Methods for Mixed Integer Nonlinear Programming*, PhD thesis, University of Dundee · S. Leyffer · Dec 1993 (PDF re-typeset 2006) · https://www.mcs.anl.gov/~leyffer/papers/thesis.pdf (host returns 403; read from a copy saved in this run by a sibling agent) · P
- M11 · "It's to Solve Problems – An Interview with Roger Fletcher", *Optima* 99, pp. 1–5 · S. Leyffer (interviewer), R. Fletcher · Dec 2015 · https://www.mathopt.org/optima/99/optima_99.pdf · P (Leyffer's own lines; Fletcher's words are primary for Fletcher)
- M12 · "Obituaries" (Roger Fletcher), *SIAM News* 49(10), p. 2 · S. Leyffer · Dec 2016 · https://web.archive.org/web/20240513063315/https://sinews.siam.org/Portals/Sinews2/Issue%20Pdfs/sn_December2016.pdf · P (his writing; secondary about Fletcher)
- M13 · "Roger Fletcher. 29 January 1939—15 July 2016", *Biogr. Mems Fell. R. Soc.* 78:127–146 · N. I. M. Gould, J. A. J. Hall · 2025 · DOI 10.1098/rsbm.2024.0037 (read from the Wayback copy of 2 Aug 2025) · S
- M14 · Mathematics Genealogy Project, "Sven Leyffer", id 282807 · MGP · fetched 2026-10-10 · https://www.mathgenealogy.org/id.php?id=282807 · S
- M15 · *Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization*, PhD thesis, Northwestern · F. E. Curtis · 2007 · DOI 10.21985/n2r99v (DataCite); PDF http://coral.ise.lehigh.edu/frankecurtis/files/dissertations/Curt07.pdf · S
- M16 · *Topics in Mixed Integer Nonlinear Programming*, PhD thesis, Lehigh University · K. Abhishek · Apr 2008 · https://web.archive.org/web/20100617083653/http://coral.ie.lehigh.edu/pubs/files/abhishek_phd_thesis.pdf · S
- M17 · *On Selecting Disjunctions for Solving Mixed Integer Programming Problems*, PhD thesis, Lehigh University · A. Mahajan · May 2009 · https://web.archive.org/web/20220120153944/https://coral.ise.lehigh.edu/~ted/files/papers/AshutoshMahajanDissertation09.pdf · S (negative evidence)
- M18 · *Discrete Optimization Models and Techniques for Problems in Data-Driven Prescriptive Analytics*, PhD thesis, University of Minnesota · J. Kim · May 2022 · https://hdl.handle.net/11299/252329 · S
- M19 · "Leyffer named SIAM president-elect" · Argonne National Laboratory (MCS news) · 30 Nov 2021 · https://web.archive.org/web/20221128071313/https://www.anl.gov/mcs/article/leyffer-named-siam-presidentelect · S
- M20 · "Sven Leyffer named President-Elect of SIAM" · ICERM · 20 Dec 2021 · https://web.archive.org/web/20221210045034/https://icerm.brown.edu/news/article/2021-12-leyffer · S
- M21 · "Sven Leyffer" (staff profile) · Argonne National Laboratory · Wayback 30 Nov 2025 · https://web.archive.org/web/20251130204501/https://www.anl.gov/profile/sven-leyffer · S
- M22 · 2016 Optimization Society Farkas Prize citation (committee: Sofer, chair; Grossmann; Ralphs; Shapiro) · INFORMS · 2016, Wayback 3 Nov 2024 · https://web.archive.org/web/20241103165359/https://www.informs.org/Recognizing-Excellence/Award-Recipients/Sven-Leyffer · S
- M23 · "Sven Leyffer" · Wikipedia · revision of 26 Dec 2025 · https://en.wikipedia.org/wiki/Sven_Leyffer · S
- M24 · "Givens Associates" · Argonne MCS Division · Wayback 30 Jan 2017 · https://web.archive.org/web/20170130080608/http://www.mcs.anl.gov/career-opportunities/givens-associates · S
- M25 · "Listn: LANS Informal Seminar Talks Network" and "Helpful Hints for Speakers" · Argonne LANS (contact J. Larson) · Wayback 6 Jan 2017 and 29 Jun 2017 · https://web.archive.org/web/20170106075249/http://www.mcs.anl.gov/research/LANS/events/listn/ ; https://web.archive.org/web/20170629082209/http://www.mcs.anl.gov/research/LANS/events/listn/HelpfulHints.htm · S
- M26 · conDFO repository: README.md, CLAUDE.md (project brief), LOGBOOK.md · S. Leyffer (brief); session log written by his AI assistant · Jul 2026, fetched 2026-10-10 · https://github.com/leyffer/conDFO · P
- M27 · BestPractices4AI repository: README.md, mkdocs.yml, docs/index.md · S. Leyffer · created 27 Jul 2026, last push 4 Aug 2026 · https://github.com/leyffer/BestPractices4AI · P
- M28 · Public repository list and file trees of the GitHub account "leyffer" (10 repositories) · GitHub API · fetched 2026-10-10 · https://api.github.com/users/leyffer/repos · P (practice)
- M29 · Uno README, "Credits" and "Cite Uno" · C. Vanaret et al. · fetched 2026-10-10 · https://github.com/cvanaret/Uno · S
- M30 · Minotaur website and coin-or/minotaur README · Minotaur Toolkit contributors · fetched 2026-10-10 · https://minotaur-solver.github.io/ ; https://github.com/coin-or/minotaur · S
- M31 · "Correction: McCormick envelopes in mixed-integer PDE-constrained optimization", *Math. Program.* 218:591–592 (CC BY 4.0) · S. Leyffer, P. Manns · 2026 · DOI 10.1007/s10107-026-02330-8 · P
- M32 · "Nonmonotone Filter Method for Nonlinear Optimization", Argonne preprint ANL/MCS-P1679-0909 · R. Fletcher, S. Leyffer, C. Shen · 14 Oct 2009 · https://optimization-online.org/wp-content/uploads/2009/10/2439.pdf · P
- M33 · Full texts of 27 joint arXiv papers (acknowledgements, affiliations, credits) · Leyffer and co-authors · 2012–2026 · arXiv:1207.0133, 1504.04589, 1902.02027, 1903.11366, 1912.02272, 2009.09498, 2009.14047, 2101.05958, 2102.08351, 2103.05751, 2106.13453, 2111.10489, 2202.07934, 2204.05773, 2208.00057, 2302.12306, 2310.09409, 2406.07891, 2406.13454, 2407.16796, 2409.09208, 2410.11171, 2501.13835, 2508.05822, 2509.01869, 2509.15961, 2509.19888 · P
- M34 · DBLP person record pid 91/745 (92 records, via the DBLP SPARQL endpoint; dump saved by a sibling agent and analysed in this run) · DBLP · fetched 2026-10-10 · https://dblp.org/pid/91/745 · S
- M35 · OpenAlex works of author A5084814006 (160 works; authorships and raw affiliation strings) · OpenAlex · fetched 2026-10-10 · https://api.openalex.org/works?filter=author.id:A5084814006 · S
- M36 · Crossref metadata for the 58 DOIs cited in this file · Crossref · fetched 2026-10-10 · https://api.crossref.org/works/ · S
- M37 · Deutsche Nationalbibliothek SRU records: Hahn dissertation (2025); Manns thesis (2020); theses supervised by Manns (Schiemann 2024, hdl 2003/43372; Severitt 2025, hdl 2003/44735) · DNB · fetched 2026-10-10 · https://services.dnb.de/sru/dnb · S
- M38 · ORCID public record 0000-0001-8839-5876 (employment, education) · ORCID · fetched 2026-10-10 · https://orcid.org/0000-0001-8839-5876 · S
- M39 · DataCite search "Leyffer" (64 records) and record 10.21985/n2r99v · DataCite · fetched 2026-10-10 · https://api.datacite.org/dois?query=Leyffer · S
- M40 · Article page of "Minotaur: a mixed-integer nonlinear optimization toolkit" (acknowledgements visible; full text paywalled) · Springer · fetched 2026-10-10 · DOI 10.1007/s12532-020-00196-1 · S
- M41 · Mathematics Genealogy Project, "Roger Fletcher", id 52148 (used to reach Leyffer's entry) · MGP · fetched 2026-10-10 · https://www.mathgenealogy.org/id.php?id=52148 · S
