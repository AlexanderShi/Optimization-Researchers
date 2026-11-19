# Ambros M. Gleixner: students, collaborators and group (research agent 04)

| Field | Value |
|---|---|
| Researcher | Ambros M. Gleixner. Professor for discrete mathematics and operations research at HTW Berlin since 2020. Head of the research group Mathematical Optimization Methods at Zuse Institute Berlin (ZIB) 2015–2023, now a guest at ZIB. PhD TU Berlin 2015, "Exact and fast algorithms for mixed-integer nonlinear programming", DOI 10.14279/depositonce-4938. Living. DBLP 07/3479, ORCID 0000-0003-0391-5903 |
| Dimension | 04: students and collaborators. Covers supervision style, group habits, lab culture and tacit knowledge as students, peers and collaborators describe them. Each account is checked against the record: thesis metadata, CVs, job ads, code history and bylines |
| Research date | 2026-11-08 |
| Sources consulted | 53 in total. 44 were read: 23 primary (P1–P23) and 21 secondary (S1–S21; S16 gave nothing usable). The other 9 were tried but were unreadable, empty or blocked (X1–X9, see Gaps) |
| WebSearch calls used | 5 of 5. None found an interview, blog or memorial. They yielded: search 1, S19; search 2, S20 and P22; search 3, P11–P14, S17 and S18; search 4, P17 and S21; search 5, S10. Everything else came from curl, public APIs and `gh api` |
| User-supplied material | None. At the start of this run `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep`. I did not open `private/`, and I saved no transcripts to `talks/` |
| Language | English (per team.json) |

## Main findings in brief

1. **The formal record and the working record disagree about who supervised whom.** In 2016 Gleixner wrote that he was "mentoring" five TU Berlin PhD students: Hendel, Müller, Rehfeldt, Serrano and Witzig. All five theses name Thorsten Koch as their only advisor. The formal record gives Gleixner one completed doctorate, Leon Eifler (2024/25), as second supervisor and Gutachter (V2, V1). The students' own wording sits between the two: "my supervisors Thorsten Koch and Ambros Gleixner" (Müller), "the lead of the SCIP development team" (Witzig).
2. **Students describe his style the same way, in their own words.** He is available, "day and sometimes even night" (Hendel). He asks "the right – well challenging – questions" (Witzig). He has a "disciplined approach to research" (Miltenberger). He coordinates "not only the software development but also the research of all members of your group" (Gamrath). He takes "care of the boring administrative details" (Hendel). Writing was taught by someone else, Timo Berthold (O1–O8).
3. **He wrote the group's tacit engineering norms into a checklist.** In 2018 he committed the first SCIP merge-request template. In 2020 he rewrote it as tickable assertions, each with an explicit "or" escape clause: run performance tests on the internal test sets, pass ctest, bump the API version, and flag default-parameter changes for the industrial partner SAP (G4).
4. **Credit follows a byline convention.** Since 2016 he has been first author on arXiv only in alphabetical bylines (4 of 48). He is last author on 17, 12 of them deliberately placed last. Release reports are led by whoever coordinated the release, and this role rotated among group members; this is inferred from bylines and stated outright only for SCIP 7.0. The MIPLIB 2017 paper he led puts two of his PhD students in positions 2 and 3 (G5, T5).
5. **Thesis time competes with code maintenance.** Five accounts, including Gleixner's own acknowledgements, describe finishing a thesis by being freed from SCIP or SoPlex maintenance, given a protected writing period, or bridged by a release contract (G7).
6. **At HTW Berlin the model is small: student assistants plus third-party projects.** He asks bachelor students for their electives and programming level. He recruits student assistants who can program and read English research papers. A doctoral student (Hoen) works inside his GPU project GoPPS (H1–H4, V4).
7. **No critical first-hand account of his supervision was found.** Acknowledgements are a genre of gratitude. Three recent theses with chapters co-authored with him have no acknowledgements section at all (F1).

## What was read and how

I found no student blog, memorial piece, Festschrift, interview, lab handbook or onboarding guide about Gleixner. He is living and mid-career (PhD 2015), so none of these would be expected yet. Five WebSearch calls found none (see Gaps); that does not prove none exist.

The best first-hand evidence is the acknowledgements and front matter of the doctoral theses of the ZIB/SCIP group. A full-text search of TU Berlin's repository DepositOnce through its public REST API (`api-depositonce.tu-berlin.de/server/api`) for "Gleixner" returned 37 items. Sixteen are doctoral theses from the optimization group, including his own (2015). I downloaded all of these open PDFs. For each I read the front matter and acknowledgements and grepped the full text for every "Ambros". I added Timo Berthold's 2014 thesis from his ZIB userpage as the account of the peer cohort Gleixner was trained in. Text was extracted with pdftotext. "PDF p." means the page of the PDF file. Diacritics split by extraction ("Gro¨tschel", "Fr´ed´eric") and ligatures ("ﬁ", "ﬀ") are restored in quotes. Spelling is otherwise as in the source, including "assistents" and "the the".

Gleixner's own words come from:

- his homepage, both the current page and Internet Archive snapshots from 2014 to 2023. This includes paragraphs that are now commented out in the public HTML source; I say so wherever I use one
- his long CV of July 2017 and his thesis acknowledgements
- his HTW Berlin profile and its research-catalogue tabs
- a 2016 Opt-Net job post he signed
- three ZIB job advertisements that name him as the contact. These are institutional texts, and parts may be ZIB boilerplate

Group practice comes from:

- the GitHub history of the SCIP merge-request template (`scipopt/scip`). The anonymous API rate limit ran out, so I read it with `gh api`, read-only
- the bylines of the SCIP Optimization Suite reports and the open-access MIPLIB 2017 paper
- the arXiv API (48 preprints)
- a DBLP SPARQL harvest. Research agent 01 fetched it on 2026-11-08 and saved it in the shared scratch folder as `dblp.json`; I used it read-only

Two sites showed an Anubis proof-of-work bot check: the ZIB OPUS frontend and dblp.org. I did not try to get past it. I read OPUS metadata only through its public OAI-PMH interface, and DBLP only through the SPARQL harvest. Every journal or proceedings DOI I cite was checked against Crossref in this run (25 DOIs). Thesis DOIs (10.14279/depositonce-…) come from DepositOnce's own metadata. Every arXiv id was checked against the arXiv API.

**Division of labour.** Other notes cover the publication landscape (01), stated method (02), code process (03), critique (05) and trajectory (06). I touch their ground only where it bears on supervision, credit and group habits.

**Tags.** [stated] = Gleixner's own words. [practice] = what the record shows (thesis metadata, bylines, commits, CV entries). [observed] = what students, peers or collaborators say. [inferred] = my reading, not evidence. (P) = primary relative to Gleixner, (S) = secondary. A student's acknowledgement is first-hand for the student but **secondary** for Gleixner, so it is marked (S).

**Genre caveat.** Thesis acknowledgements are a genre of gratitude, and criticism is structurally absent from them. Counting a theme measures what students chose to thank him for. It does not measure how often he behaved that way. **No negative first-hand account of his supervision was found.** That absence is not evidence that none exist. Absence of thanks is not evidence either: three of the most recent theses with chapters co-authored with Gleixner have no acknowledgements section at all (Serrano 2021, Chmiela 2025, Mexi 2026; front matter checked page by page).

---

## 1. Lineage: how Gleixner himself was trained

**L1. Honours project in Sydney, Diplom in Berlin, and two people who opened doors.** [stated] (P) + [practice] (P)
- Thesis acknowledgements, p. iii (PDF p. 5): "I am indebted to Andreas Bley, without whom I might never have learned about this special place, and to Gary Froyland, who encouraged me during my first steps in discrete optimization at the University of New South Wales."
- CV 2017 (P3), pp. 1 and 6: UNSW Honours project with G. Froyland, "Integer programming techniques for large-scale open pit mine production scheduling". The CV prints the years without saying which entry they belong to; it lists a 2006 DAAD study-abroad scholarship. Diplom, TU Berlin 2008, supervisor Rolf H. Möhring, thesis "Solving large-scale open pit mining production scheduling problems by integer programming". The OPUS OAI record of that thesis, URN nbn:de:0297-zib-11389, lists "Rolf Möhring Prof. Dr." as contributor.
- His first journal paper is with his Sydney hosts: Boland, Dumitrescu, Froyland, Gleixner, "LP-based disaggregation approaches to solving the open pit mining production scheduling problem with block processing selectivity", Computers & Operations Research 36(4) 1064–1089 (2009), DOI 10.1016/j.cor.2007.12.006 (Crossref).
- Era: student years 2002–2008 (Bayreuth, Sydney, TU Berlin). German National Merit Foundation 2005–2008 (CV).

**L2. Trust and support from Grötschel and Koch.** [stated] (P)
- p. iii: "For their trust and for this support I wish to thank Martin Grötschel and Thorsten Koch and my colleagues at the Department of Optimization and the administration of the institute."
- The three records give the formal roles differently; see Contradiction C2.

**L3. He grew up inside a peer-run team of PhD students who had inherited SCIP.** [observed] (S)
- Berthold 2014 (S10), PDF p. 7: "Taking over the development of a big academic software package that was someone else’s PhD project can be a burden. In our case, it was a blessing." Also: "“We” refers to the team of PhD students at ZIB who were responsible for the SCIP project, in particular Stefan Heinz who started at ZIB around the same time as I did and later Gerald Gamrath, Ambros Gleixner, and Stefan Vigerske."
- Same page, on the department head: "Thanks to Thorsten Koch for leaving me and the other members of his group the freedom to make our own decisions and design projects in the way that we wanted them to be."
- [practice] (P): as a PhD student Gleixner chaired CPAIOR 2011 in Berlin jointly with Berthold, Heinz and Koch (CV, homepage). Organising responsibility was handed to PhD students.
- [inferred] The pattern he later ran as group head is the one he was trained in: freedom from the department head, senior availability, and students running the shared code base. No source says he copied it on purpose.

**L4. A peer as sparring partner, who later co-mentors his students.** [stated] (P) + [practice] (P) + [observed] (S)
- p. iii: "I want to thank Timo Berthold for his creative, critical, and ambitious mind".
- Their two-author journal paper: Berthold & Gleixner, "Undercover: a primal MINLP heuristic exploring a largest sub-MIP", Mathematical Programming 144(1-2) 315–346, DOI 10.1007/s10107-013-0635-2. Crossref dates it 2013, online first; the CV gives 2014. In the 2008–2015 DBLP records Berthold is his most frequent co-author (3 of 8).
- Later roles: Berthold is "my former mentor Timo Berthold, who became my main teacher about academic writing at all stages of the process" for Hendel (S3, PDF p. 5). He is a formal advisor of Mexi and a Gutachter of Eifler (P23).

**L5. Credit given at the level of who built what.** [practice] (P)
- p. iii names collaborators by contribution: "Dan Steffy for his initiative to study iterative refinement using SoPlex, Benjamin Müller and Stefan Weltge for implementing and improving the OBBT components of SCIP, and Kati Wolter for her thorough testing and profiling of the exact extensions of SoPlex."
- It names student assistants: "I wish to thank Dennis Elbrächter, Luca Fabbri, Wei Huang, Leif Naundorf, and Frédéric Pythoud, who supported me during their time as student assistants."
- It names a student's tool and the maintenance relief: "Gregor Hendel for supporting me in the evaluation of the experiments in Chapters 6 and 7 by means of his excellent Ipet tool, and Gerald Gamrath and Matthias Miltenberger for freeing me from a lot of maintenance work on SCIP and SoPlex when I needed it."
- It names who helped structure the writing: "I am particularly indebted to Ralf Borndörfer, Steve Maher, and Marika Neumann for discussing the outline of the introduction." Fifteen people proofread the manuscript.

**L6. A network built through visits.** [stated] (P) + [inferred]
- p. iv (PDF p. 6) thanks hosts in:
  - Budapest (EGRES) and Sydney
  - Melbourne (NICTA)
  - Japan and Beijing
  - Chile ("Felipe Serrano and Carolina von Hausen and their families"; Serrano later became his mentee, V2)
  - Detroit (Steffy), Porto (Pedroso), London (Misener)
  - Bologna (Lodi, Fabbri, Schweiger), Magdeburg (Kaibel, Walter, Weltge)
  - Braunschweig (GAMS)
- CV: 2013 MERIT Visiting Scholar, University of Melbourne; 2007 ADONET Young Researcher Fellowship at ELTE Budapest.
- [inferred] Several hosts reappear in his students' work. Pedroso hosted Müller and led to the circle-packing paper (T8). Lodi sat on the committees of Müller and Lenz (P23).

## 2. Formal versus actual supervision

Item labels in this section are V1–V6, so they cannot be confused with the source ids S1–S21.

**V1. The formal record credits him with one doctorate, as second supervisor.** [practice] (P/S) + [observed] (S)
- DepositOnce (P23): Leon Eifler, "Algorithms and certificates for exact Mixed Integer Programming". Advisor Koch; referees Koch, Gleixner, Coniglio, Berthold. Title page: "Gutachter: Prof. Dr. Ambros Gleixner"; "Tag der wissenschaftlichen Aussprache: 08. November 2024"; "Berlin 2025"; DOI 10.14279/depositonce-23941.
- HTW research catalogue (P6), "Abgeschlossene Promotionen betreut von Prof. Dr. Ambros Gleixner", has one entry: "Algorithms and Certificates for Exact Mixed Integer Programming", "Betreute Promotion › 2024". The profile counter reads "Betreute Promotionen (1)" (P5).
- Math Genealogy Project (S20): "According to our current on-line database, Ambros Gleixner has 1 student and 1 descendant". The student is Eifler, TU Berlin 2025. Eifler's own record (MGP id 342910) reads "Advisor 1: Thorsten Koch" and "Advisor 2: Ambros M. Gleixner".
- Eifler (S1), PDF p. 4: "I want to thank Ambros Gleixner, my second supervisor, co-author, and fellow exact-solving enthusiast, for his guidance, the many fruitful discussions, and for being a great mentor and colleague. I honestly could not have done it without you."
- Era: Eifler co-authored with Gleixner as early as 2016 (arXiv 1609.02063). His thesis chapters are joint papers with him: ACM TOMS 48(2) 2022, DOI 10.1145/3485630; Math. Program. 197(2) 793–812, DOI 10.1007/s10107-021-01749-5; SIAM J. Optim. 34(1) 742–763, DOI 10.1137/23m156046x; IJOC 37(4) 933–944 (2025), DOI 10.1287/ijoc.2023.0409 (Eifler PDF pp. 11–12).

**V2. His own claim in 2016: mentoring five TU Berlin PhD projects.** [stated] (P) + [practice] (P) + [observed] (S)
- Homepage, Wayback snapshot of 2016-04-13: "Currently, I am mentoring Gregor Hendel, Benjamin Müller, Felipe Serrano, and Jakob Witzig, for their PhD projects at TU Berlin." By 2016-07-29 Daniel Rehfeldt has been added. From the 2017-01-20 snapshot on, the paragraph sits inside an HTML comment, and it is still in the page source today.
- Same 2016 paragraph, on earlier juniors: "I have supervised Dennis Elbrächter from TU München, Luca Fabbri from the Università di Bologna, Wei Huang from FU Berlin, Leif Naundorf from FU Berlin, Frédéric Pythoud from EPFL, and Stefan Weltge from the Otto-von-Guericke-Universität Magdeburg during their time as interns or student assistents at ZIB."
- DepositOnce (P23): all five 2016 mentees list Thorsten Koch as sole advisor, and Gleixner is a referee on none of them:
  - Müller, defence 18 Mar 2020, DOI 10.14279/depositonce-9889
  - Serrano, defence 21 Aug 2020, DOI 10.14279/depositonce-12180
  - Hendel, defence 28 Sep 2021, DOI 10.14279/depositonce-15958
  - Rehfeldt, defence 16 Aug 2021, DOI 10.14279/depositonce-12470
  - Witzig, defence 17 Dec 2021, DOI 10.14279/depositonce-15389
- How the five describe him:
  - Müller (S2), PDF p. 7: "First of all, I would like to thank my supervisors Thorsten Koch and Ambros Gleixner for enabling me to work in such an inspiring field of applied mathematics."
  - Witzig (S4), PDF p. 3: "In his role as the lead of the SCIP development team" (full quote at O2).
  - Hendel (S3), PDF p. 5: "an outstanding role in the group" (O1).
  - Rehfeldt (S7), PDF p. 7, lists him only among five proofreaders.
  - Serrano (S15) has no acknowledgements.
- [inferred] ZIB is a non-university institute. The degree-granting supervision sat with the TU Berlin professor (Koch). Gleixner, a group head without a professorship until 2020, did the day-to-day mentoring without the formal title. This is an institutional structure, not a judgement of either man.

**V3. Students of other advisors whose thesis chapters he co-authored.** [practice] (P/S)
- Antonia Chmiela. Advisor Pokutta; defence 2 Jun 2025; DOI 10.14279/depositonce-24040. Chapter 2 (PDF p. 24) is "joint work with Elias B. Khalil, Ambros Gleixner, Andrea Lodi, and Sebastian Pokutta": "Learning to Schedule Heuristics in Branch-and-Bound", NeurIPS 34 (2021) 24235–24246, arXiv 2103.10294. Chapter 3 (PDF p. 25) is "Online Learning for Scheduling MIP Heuristics", arXiv 2304.03755.
- Gioni Mexi. Advisors Pokutta and Berthold; defence 10 Sep 2026; DOI 10.14279/depositonce-26588. The chapter list is on PDF p. 14:
  - Chapter 3 integrates "Cut-Based Conflict Analysis in Mixed Integer Programming", INFORMS J. Comput. (2025), DOI 10.1287/ijoc.2024.0999.
  - It also integrates "Improving Conflict Analysis in MIP Solvers by Pseudo-Boolean Reasoning", arXiv 2307.14166 (CP 2023 per the thesis).
  - Chapter 6 is "partially based on a publication in the proceedings of the International Conference on Operations Research 2023" with Besançon, Bolusani, Chmiela, Hoen and Gleixner. The arXiv preprint "Scylla" (arXiv 2307.03466) has the same author set; that the two are the same paper is not checked.
- Neither thesis has an acknowledgements section.
- Witzig's Chapter 6 (PDF p. 15) is Witzig & Gleixner, "Conflict-Driven Heuristics for Mixed Integer Programming", INFORMS J. Comput. (2020), DOI 10.1287/ijoc.2020.0973.

**V4. HTW Berlin: a doctoral student inside his own project.** [observed] (S) + [practice] (P)
- Hoen's homepage (S17): "I am a Ph.D. student at HTW Berlin, conducting research within the Go!PPS project, and a guest researcher at the Zuse Institute Berlin (ZIB)." He is "the maintainer of the presolving library PaPILO".
- HTW catalogue (P8): "GPU-accelerated optimization for Production Planning and Scheduling (GoPPS)", "Projektleitung: Prof. Dr. Ambros Gleixner", 01.10.2025–30.09.2027.
- Joint papers:
  - Hoen & Gleixner, CPAIOR 2025, LNCS pp. 35–50, DOI 10.1007/978-3-031-95976-9_3
  - Hoen, Kamp & Gleixner, "MIP-DD: Delta Debugging for Mixed-Integer Programming Solvers", INFORMS J. Comput. 38(2) 414–423 (2026), DOI 10.1287/ijoc.2024.0844
  - Hoen, Oertel, Gleixner & Nordström, CPAIOR 2024, DOI 10.1007/978-3-031-60597-0_20
  - von Holly-Ponientzietz, Hoen, Turner & Gleixner, "Clique Probing for Mixed-Integer Programs", arXiv 2512.17551
- Which university will confer Hoen's degree, and who his formal advisor is, was not found (Gaps).

**V5. The second generation.** [practice] (S) + [inferred]
- Eifler, PDF p. 12: Chapter 6 is joint work with Gleixner "and my former master’s student Jules Nicolas-Thouvenin (now at Orange S.A.)". This is a three-step chain: Gleixner, then Eifler (PhD), then Nicolas-Thouvenin (MSc).
- Ksenia Bestuzheva (S18) was a "Postdoctoral researcher, Zuse Institute Berlin" 2018–2023 (her CV does not name the group) and co-authored three papers with Gleixner: Math. Program. Comput. 15(4) 703–731 (2023), DOI 10.1007/s12532-023-00246-4; Math. Program. 210(1-2) 47–74 (2024), DOI 10.1007/s10107-024-02104-0; arXiv 2304.12145. As a postdoc she lists "MSc student and intern supervision". She then became "Head of research group, Zuse Institute Berlin & Research Campus MODAL" for 2023–2025, including "head of development of the SCIP Optimization Suite, leading a developer team distributed across universities and research organisations".
- [inferred] His homepage ends his headship in 2023 and her CV starts hers in 2023. So the headship most likely passed to a postdoc he had co-authored with, but neither source says it is the same group, and none says how a handover was arranged.

**V6. Size of the group, 2017.** [stated] (P)
- CV 2017, p. 1: "Our team currently consists of 2 senior researchers, 10 research assistants, and 4 student assistants."
- p. 7: "since 2016 Examiner for one PhD thesis and two bachelor's theses".
- Era: ZIB Department of Optimization (head Koch), funded through the Research Campus MODAL, MATHEON and industry (CV, "Research projects").

## 3. Supervision style as students describe it

**O1. Open door, including at night, and he absorbs the administration.** [observed] (S)
- Hendel (S3), PDF p. 5: "Ambros Gleixner has truly had an outstanding role in the group not only by taking care of the boring administrative details, but also keeping his door open day and sometimes even night to discuss paper ideas and progress. All of which he does with style."
- Era: Hendel's PhD period, which ended with his 2021 defence, with Gleixner as group head.

**O2. Challenging questions, and shared experience.** [observed] (S)
- Witzig (S4), PDF p. 3: "During my time at ZIB and as a part of the SCIP development team, I had the honor to work with Ambros Gleixner. In his role as the lead of the SCIP development team, he was always available for discussions and was interested in the current research questions I tried to answer. When working with Ambros, he shared all his experiences and always asked the right – well challenging – questions. I’m very happy that I still have the opportunity to collaborate with Ambros."

**O3. Discipline, time for questions, new perspectives.** [observed] (S)
- Miltenberger (S6), PDF p. 5: "Ambros, you have been a source of inspiration and a person to look up to with your disciplined approach to research. Thank you for always finding the time to answer my questions and providing new perspectives."
- Context: formal advisor Koch; topic "Linear programming in MILP solving". [inferred] The topic is close to Gleixner's own SoPlex work. Defence 31 Mar 2023; DOI 10.14279/depositonce-22309.

**O4. He coordinated research as well as code.** [observed] (S)
- Gamrath (S5), PDF p. 4: "Ambros, I was already impressed before by your mindful lead of the mathematical optimization methods group at ZIB and the SCIP development in the last years, but only now that I got the chance to try doing this myself, do I fully appreciate the hard work you did in coordinating not only the software development but also the research of all members of your group."
- What "doing this myself" refers to is on PDF p. 3: "I2DAMO hired me to manage the SCIP 7.0 release" (see G5).

**O5. Guidance and discussion as second supervisor.** [observed] (S)
- Eifler: see V1. He is the only student who calls Gleixner his supervisor in a formal sense ("my second supervisor").

**O6. Help for people outside the group who use the exact tools.** [observed] (S) + [practice] (P)
- Pulaj (S9), PDF p. 7: "I also want to thank Ambros Gleixner for his help with everything, in particular for his help with exact SCIP and VIPR." Pulaj's advisor was Grötschel; defence 6 Nov 2017; DOI 10.14279/depositonce-6534.
- The joint paper that followed: Eifler, Gleixner & Pulaj, "A Safe Computational Framework for Integer Programming Applied to Chvátal’s Conjecture", ACM Trans. Math. Softw. 48(2) 1–12 (2022), DOI 10.1145/3485630.

**O7. He proofreads theses.** [observed] (S)
- Hendel, PDF p. 5, lists him among nine proofreaders.
- Rehfeldt, PDF p. 7: "I would also like to thank Gerald Gamrath, Ambros Gleixner, Nils Kempke, Benjamin Müller, and Mark Turner for proof-reading parts of this thesis and providing many helpful comments."
- Lenz (S8), PDF p. 5: "The quality of the manuscript was greatly improved by the proofreading of Lovis Anderson, Bede Brown, Ambros Gleixner, …". Lenz's advisor was Koch; defence 6 May 2021; DOI 10.14279/depositonce-12765.

**O8. A division of mentoring labour: who taught what.** [observed] (S) + [inferred]
- Academic writing came from Berthold: "my main teacher about academic writing at all stages of the process" (Hendel, PDF p. 5).
- Freedom and trust came from Koch:
  - Eifler: "for the trust to develop my own research ideas and follow them" (PDF p. 4)
  - Witzig: "He gave me the freedom to work on many different ideas, a best of is summarized in this thesis." (PDF p. 3)
  - Turner (S12): "the amount of academic freedom you gave me while doing so" (PDF p. 8)
- Pace also came from Koch: "his constant encouragement to “get things done”" (Hendel, PDF p. 5).
- [inferred] In the students' accounts Gleixner is the group's research discussant, coordinator and administrator. None of the sixteen theses credits him specifically with teaching writing.

## 4. Group habits and lab culture

**G1. Team-oriented solver research as the group's identity.** [stated] (P) + [observed] (S)
- Opt-Net post signed by Gleixner, 25 Nov 2016 (P11): "Our group holds longstanding expertise in the design and implementation of mathematical optimization solvers and you will be part of the research team around the SCIP Optimization Suite". Also: "We expect creativity and a high degree of team spirit and commitment to problem solving."
- Job ads 2020/2021 (P13, P14): "ein hohes Maß an teamorientierter Forschung" [a high degree of team-oriented research; my translation].
- Hendel, PDF p. 5: "a unique work and research group, with an unprecedented dedication to the SCIP project".
- Miltenberger, PDF p. 5: "You all have created a unique and stimulating atmosphere and productive working environment at the Zuse Institute Berlin (ZIB)."

**G2. Postdocs set their own agenda and lead research assistants.** [stated] (P, institutional voice)
- IWA 70/20 (19 Nov 2020) and WA 12/21 (11 Feb 2021), both naming "Prof. Dr. Ambros Gleixner" as contact: "In diesem Rahmen definieren Sie Ihre Forschungsagenda eigenständig und arbeiten gemeinsam mit Forschungsassistenten aus der Arbeitsgruppe daran. Die Stelle ist langfristig angelegt und ermöglicht Ihnen die Übernahme von Führungsverantwortung." [Within this framework you define your research agenda independently and work on it together with research assistants from the group. The position is designed for the long term and allows you to take on leadership responsibility. My translation.]
- Required skills: "fortgeschrittene Kenntnisse in diskreter Optimierung und rechnerischem MIP" and "gute Programmierkenntnisse, idealerweise in C, C++, oder verwandten Sprachen".
- Opt-Net 2016 had already offered "a PostDoc researcher position (100% TV-L E14) with self-defined research agenda in the context of computational mixed-integer linear programming". In the same post the PhD track was topic-bound: "a PhD track research position (100% TV-L E13) on the topic of high-precision mixed-integer programming over the rational numbers".
- [inferred] The pattern is open agendas for postdocs and topic-bound PhD positions tied to his own exact-MIP line. Who filled the 2016 PhD position is not documented; Eifler is the plausible candidate, but this is unconfirmed.

**G3. Onboarding is promised, but the only written form found is the code-review checklist.** [stated] (P)
- Opt-Net 2016: "We are committed to an active onboarding process to facilitate new members with all the tools and the knowledge they need for success in our institute and their career. We provide a family-friendly work environment through flexible working hours and meeting times and the opportunity for part-time working arrangements."
- IWA 30/17 (P12) has the German equivalent: "Unser Team bietet einen aktiven Einarbeitungsprozess, um neuen MitarbeiterInnen die Fähigkeiten und das Wissen zu vermitteln, die für ihren Erfolg in unserem Institut und ihrer Karriere wichtig sind." [Our team offers an active onboarding process to give new staff the skills and knowledge that matter for their success at our institute and in their career. My translation.]
- [inferred] The wording recurs across ZIB ads and may be institutional boilerplate rather than Gleixner's own. No public onboarding document was found. The closest written artefact is G4.

**G4. The merge-request checklist he started and rewrote.** [practice] (P)
- Origin: `scipopt/scip`, file `.gitlab/merge_request_templates/Feature.md`, commit 8201ee1d1e, 2018-01-26, author Ambros Gleixner, message "add first merqe request template" [sic]. Among its items:
  - "Does ctest pass (jenkins ctest ...)?"
  - "Has performance impact been checked on mi(nl)pdev-solvable (if activated by default)?"
  - "Are coverage settings added to test new code (if necessary)?"
  - under "If this merge introduces an API change": "Look for a satisfactory solution that ensures backwards compatibility." and "Increase SCIP_APIVERSION after the merge."
- Later history: Hendel edited it on 2018-02-01 (commit 45744a12b1, adding "Interface changes must be documented in doc/xternal.c and the CHANGELOG."). Schlösser renamed it `Code_Review.md` on 2018-11-13 (commit 243c825695). By 2020 it had gained the line "Tag this MR with the label 'default parameter' and inform one of the developers responsible for SAP (default: Jakob) if a parameter was added/deleted/changed." Who added that line is not determined.
- The 2020 rewrite: on 2020-08-27 (commit 126c5d7984, "rephrase code review template", then four follow-ups the same day) Gleixner turned every question into an assertion to be ticked, each with an explicit escape clause:
  - "The performance impact has been checked on mi(nl)pdev-solvable *or* the changed code will not be executed by default."
  - "The naming and place of new methods is clear and consistent *or* no new methods have been added."
  - "No parameter was added/deleted/changed *or* the MR is tagged with the label 'default parameter' and at least one developer responsible for SAP is mentioned in a comment."
- Further edits by him: 2020-10-06 (059df82c21, "clarified code review template w.r.t. API changes": "No, **or** as far as possible, the code ensures backwards compatibility."), 2021-09-21 and 2021-09-24.
- Overall he is the most frequent committer to `Code_Review.md`: 8 of 26 commits, ahead of Schlösser (7) and Vigerske (6). Others extended it, for example Schlösser on 2022-10-05 (f1bab5d772): "Ensure that new code and features use randomization where necessary to account for performance variability." Vigerske made it the default template in 2025 (f92ac2cfb6).
- [inferred] These are tacit group norms made explicit. Any change that runs by default gets a performance run on the internal test sets before merging. Interface changes are versioned. Changes visible to the industrial partner (default parameters) are flagged to a named liaison. The test sets "mipdev-solvable"/"minlpdev-solvable" are internal and not public (not found).

**G5. Release coordination rotates, and the coordinator is credited as first author.** [practice] (P) + [observed] (S) + [inferred]
- SCIP Optimization Suite reports list the first author, then everyone else alphabetically:
  - 3.2: Gamrath (ZIB-Report 15-60, 2016)
  - 4.0: Maher (ZIB-Report 17-12, 2017)
  - 5.0: **Gleixner** (ZIB-Report 17-61, 2017)
  - 6.0: **Gleixner** (ZIB-Report 18-26, 2018)
  - 7.0: Gamrath (ZIB-Report 20-10, 2020)
  - 8.0: Bestuzheva (arXiv 2112.08872, 2021)
  - 9.0: Bolusani (arXiv 2402.17702, 2024)
  - 10.0: Hojny (arXiv 2511.18580, 2025)
- How this was checked: the reports for 3.2–7.0 were not read, because the OPUS frontend is behind a bot check. Their bylines come from the bibliographies of Witzig 2022 and Eifler 2025. The bylines for 8.0–10.0 come from the arXiv API. The journal version of 8.0, "Enabling Research through the SCIP Optimization Suite 8.0", ACM TOMS 49(2) 1–21 (2023), DOI 10.1145/3585516, keeps Bestuzheva first.
- Gamrath (S5), PDF p. 3: "Finally, I am happy that I2DAMO hired me to manage the SCIP 7.0 release, which allowed me to wrap-up some of my projects in SCIP and to spend a few more months on writing this thesis."
- [inferred] "First author of the release report = release coordinator" is a group convention, and the role rotates. Gamrath states it explicitly only for 7.0. Gleixner held the role for two consecutive releases while he headed the group.

**G6. Industry partners fund PhD positions and hold joint workshops.** [stated] (P) + [observed] (S) + [inferred]
- Homepage 2016-04-13: "I am mainly responsible for the ZIB cooperations with SAP and Siemens that support the development of SCIP and SoPlex with a special focus on their industrial applications."
- CV 2017: principal investigator of "SAP AG & Co. KG, 'Development of new Linear and Integer Programming Techniques to solve Supply Chain Management Problems'" (jointly with T. Koch and A. Martin) and of "Siemens AG, Corporate Technology, 'Siemens-ZIB-Cooperation'".
- Gamrath, PDF p. 3: "I wish to thank the optimization group at SAP SE for their interest in SCIP, for funding my position at ZIB, and for the fruitful cooperation."
- Müller, PDF p. 7: "I would like to thank our industry partner Siemens, in particular Kurt Majewski and Christoph Moll, for our great collaboration and financing the Ph.D. position that I was working on."
- Hendel, PDF p. 5: "I am very grateful to our collaboration partners from SAP. I always enjoyed our mutual workshops, as they gave us a unique opportunity to exchange new ideas and learn from their perspectives and expectations of the project."
- [inferred] The CV lists Gleixner as PI of both cooperations from 2015, so at least during his time as group head these grants paid the positions of Gamrath and Müller. Who was PI before 2015, while Gamrath was already SAP-funded, is not documented. The SAP liaison line in the code-review template (G4) is the engineering side of the same arrangement.

**G7. Thesis time competes with maintenance.** [stated] (P) + [observed] (S) + [inferred]
- Gleixner, thesis p. iii: Gamrath and Miltenberger "for freeing me from a lot of maintenance work on SCIP and SoPlex when I needed it".
- Rehfeldt, PDF p. 7, thanking Koch: "for giving me the opportunity to work almost exclusively on the creation of this thesis in the last one and a half years of my PhD studies". Also: "Even though the project I was working on for most of my time at TU and ZIB had nothing to do with Steiner trees, I learned a lot about programming, (parallel) algorithms, and perseverance, which turned out to also be quite useful for the creation of this thesis."
- Gamrath, PDF p. 3: the I²DAMO release contract (G5).
- Hendel, PDF p. 5: "these last few months of dual responsibility between Xpress and thesis writing".
- Berthold, PDF p. 7: "Oh boy, seven years a PhD student?" Turner, PDF p. 8: "my six year journey".
- [inferred] In this group, code maintenance and project work compete with thesis writing. Finishing tends to need someone to take over maintenance, a protected writing period, or a bridging contract. Era: 2008–2023, project-funded positions on fixed-term contracts (F4), and a shared code base of the size of SCIP. Which project Rehfeldt meant is not named. Gleixner was PI of ZIB's BEAM-ME sub-project (CV), and Rehfeldt co-authored a 2019 paper on parallel interior-point presolving for energy-system models with him (arXiv 1908.00796). The link between the two is only a hypothesis.

**G8. Shared tools built by students and used by the whole group.** [practice] (P) + [observed] (S)
- Ipet, Hendel's evaluation tool, carried Gleixner's own thesis experiments (L5).
- MIP-DD (Hoen, Kamp, Gleixner), arXiv 2405.19770 abstract: "In these versions, MIP-DD successfully contributed to 24 out of all 51 documented MIP-related bugfixes even for some long-known issues." The versions meant are SCIP 8.0.1 to 8.1.1.
- PaPILO: Gleixner, Gottwald & Hoen, arXiv 2206.10709. It is now maintained by Hoen (S17).
- [inferred] Tools a student builds become infrastructure for the whole group, and the group head uses them too.

**G9. Social rituals of the department.** [observed] (S)
- Müller, PDF p. 8: "I want to thank all the people who joined all those delicious BBQs, coffee breaks, bicycle tours, board game nights, friday afternoon beers, dinners, and our legendary Starcraft nights."
- Witzig, PDF p. 3: "all the joyful coffee breaks and after-work events".
- Berthold, PDF p. 8: "the daily coffee breaks, lunches and several BBQs and excursions over the years".
- These describe the department and the SCIP team, not Gleixner personally.

**G10. Big rewrites are done as named sub-teams.** [observed] (S)
- Müller, PDF p. 7: "In 2016, the so-called consexpr team decided to restructure and to rewrite the handling of nonlinear constraints in SCIP. Being part of this great team really taught me a lot about aspects of computational MINLP that I had not known before."
- He thanks Bestuzheva, Serrano, Vigerske and Wegscheider for it. Gleixner is not named in this sentence.
- The SCIP 8.0 report (arXiv 2112.08872, Bestuzheva first) lists "a complete rework of the way nonlinear constraints are handled". [inferred] This is the consexpr rewrite, released five years after the team was formed.

## 5. Tacit knowledge: what group members know but the papers do not say

| # | Tacit item | Evidence | Label | Confidence |
|---|---|---|---|---|
| T1 | Bring him a research question and expect to be challenged rather than handed answers | Witzig: "always asked the right – well challenging – questions"; Miltenberger: "providing new perspectives" | [observed] (S) | medium (two accounts) |
| T2 | A change that runs by default is merged only after a performance run on the internal test sets, ctest against several LP solvers, and a version bump for API changes; default-parameter changes are flagged to the SAP liaison | Merge-request template that Gleixner created (2018) and rewrote (2020), G4 | [practice] (P) | high (written) |
| T3 | Writing is learned from Berthold; Gleixner discusses ideas and progress | Hendel PDF p. 5 | [observed] (S) | low–medium (one account) |
| T4 | Protect thesis time from maintenance, or finishing slips | G7: five accounts including Gleixner's own | [observed] (S) + [stated] (P) | medium–high |
| T5 | Bylines encode roles: whoever did the work goes first, the group head goes last, the release coordinator leads the release report, large committees go alphabetical after the leads | arXiv bylines: 48 preprints, first author on 4, all alphabetical; last on 17, 12 of them non-alphabetical (crude surname check). DBLP 2021–2026: first on 2 of 32 non-informal records, last on 11. MIPLIB 2017 order is Gleixner, Hendel, Gamrath, then alphabetical; its acknowledgements credit the MODAL work "in particular by the first, second, third, ninth, and last author" (p. 486) | [practice] (P), convention [inferred] | medium |
| T6 | The way in is student assistant, then co-author, then PhD | Weltge was a student assistant (homepage 2016, P2), then co-author: CPAIOR 2013, DOI 10.1007/978-3-642-38171-3_26; J. Glob. Optim. 67(4) 731–757, DOI 10.1007/s10898-016-0450-4. Wei Huang was a student assistant, then co-author: Numer. Algebra Control Optim. 2(4) 695–711 (2012), DOI 10.3934/naco.2012.2.695. Eifler co-authored arXiv 1609.02063 in 2016, before his PhD. HTW job note (H2). Berthold recalls the same route under Achterberg (S10, PDF p. 7) | [practice] (P) + [observed] (S) | medium |
| T7 | Exact SCIP and VIPR are offered as a service to people with a mathematical question | Pulaj (O6) and the TOMS paper; Eifler's thesis frames exact MIP "as a tool for computer-assisted mathematics" (abstract); the HTW topic "Schranken für Covering Codes mit ganzzahliger Programmierung" (H3) | [observed] (S) + [practice] (P) | low–medium |
| T8 | Doctoral students are hosted by collaborators abroad, and joint papers follow | Müller, PDF p. 7: "Thanks to João Pedro Pedroso, who invited me to his apartment in Porto and introduced me to the recursive circle packing problem and the board game Shogi." Then Gleixner, Maher, Müller & Pedroso, arXiv 1702.07799. Also: "Thanks to Andrea Lodi for inviting my family and me to Montreal and for the amazing time that we had there." Then Müller, Muñoz, Gasse, Gleixner, Lodi & Serrano, arXiv 1912.00356 | [observed] (S) + [practice] (P) | medium. Whether Gleixner arranged the visits is not documented |

## 6. Students at HTW Berlin (since 2020)

**H1. What he asks of bachelor students.** [stated] (P)
- HTW profile (P5), "Infos zur Lehre": "Wenn Sie bei mir die Bachelorarbeit schreiben möchten, dann schreiben Sie mir bitte immer, welche relevanten Wahlpflichtfächer und Seminare Sie bereits gehört haben und was der Stand Ihrer Programmierkenntnisse ist." [If you would like to write your bachelor's thesis with me, please always tell me which relevant electives and seminars you have already taken and what your level of programming skills is. My translation.]

**H2. Student assistants for small research projects.** [stated] (P)
- Same page, "Jobs": "Für kleine Forschungsprojekte suche ich immer nach studentischen Hilfskräften, die Interesse an Optimierung und computerorientierter Mathematik haben. Voraussetzungen sind gute Programmierkenntnisse und die Fähigkeit, englische Forschungsartikel zu lesen. Sprechen Sie mich an!" [For small research projects I am always looking for student assistants who are interested in optimization and computer-oriented mathematics. The prerequisites are good programming skills and the ability to read English research articles. Talk to me! My translation.]
- The 2016 ZIB homepage had the same invitation in English: "If you are interested to work in our research group as a student, research assistant, or postdoc, send me an e-mail." It is visible in the 2016-07-29 and 2017-01-20 snapshots and commented out in the current source.

**H3. How he scopes undergraduate topics.** [practice] (P)
- HTW Wirtschaftsmathematik topic list (P9), section "Prof. Dr. A. Gleixner", nine topics:
  - "Die Integer Round-Up Property für Cutting Stock und verwandte Probleme"
  - "Heuristiken und exakte Methoden für optimierte Schichtplanung"
  - "Schranken für Covering Codes mit ganzzahliger Programmierung"
  - "Branch-and-Price für Vehicle Routing"
  - "Branch-and-Cut für das Hamiltonkreisproblem"
  - "Cycle Partitioning für Graphen mit Längenbeschränkungen"
  - "Die FeasibilityPump-Heuristik für gemischt-ganzzahlige Programme"
  - "Modelle und Algorithmen für optimierte Stundenplanung"
  - "Logische Datenanalyse mittels Boolescher Algebra"
- [inferred] Each topic mirrors a live research line:
  - cycle partitioning: arXiv 2401.17937 and arXiv 2607.15837 with Ghannam, Mexi and Lam
  - Boolean-algebra data analysis: arXiv 2605.29686 with Weber et al.
  - integer programming for mathematical bounds: the exact-MIP line (T7)
  - textbook MIP methods: branch-and-price, branch-and-cut, feasibility pump
- Whether undergraduates feed into the papers is not documented.

**H4. Formal roles and how to reach him.** [practice] (P)
- HTW profile: "Praktikumsbeauftragte*r" (internship coordinator) for Wirtschaftsmathematik (B), and "Hochschullehrer*in" for Wirtschaftsmathematik (B) and Finanzdienstleistungen - Risikomanagement (M).
- Office hours are booked through an online planner: "Wenn Ihr Anliegen dringlich ist oder kein Termin passt, schicken Sie mir bitte eine E-Mail." [If your matter is urgent or no slot fits, please e-mail me. My translation.]
- Teaching and research area: "Mathematische Optimierung, Operations Research, computerorientierte Mathematik".
- Project base (P8), all with "Projektleitung: Prof. Dr. Ambros Gleixner":
  - running: GoPPS 2025–2027; DaKoDi 2026–2029; HOTSTEEL 2026–2029; OptiLEEP 2026–2027 (jointly with Berenike Masing); OHA4flexgrid 2026–2029
  - completed: EnBA-M 2018–2021; MODAL SynLab 2020–2023; MATH+ EF1-9 "Adaptive Algorithms through Machine Learning: Exploiting Interactions in Integer Programming" 2021–2022; VetOpt 2022–2023
- Era: a university of applied sciences, teaching-heavy, with research run through third-party projects. A contrast with the 2015–2023 ZIB group of 2 senior researchers, 10 research assistants and 4 student assistants (V6).

## 7. Collaborators and how he works with them

**K1. The co-author network shifts with his role.** [practice] (P)

DBLP harvest (P20): 74 records, of which 59 are non-informal author records. "Middle" includes alphabetical bylines.

| Period | Records | First | Last | Middle | Most frequent co-authors (papers with ≤15 authors) |
|---|---|---|---|---|---|
| 2008–2015 (PhD at ZIB) | 8 | 2 | 3 | 3 | Berthold 3; one each with Boland, Dumitrescu, Froyland, Bley, Koch, Vigerske, Steffy, Wolter, Weltge, Gamrath, Melchiori |
| 2016–2020 (group head at ZIB) | 19 | 7 | 5 | 7 | Steffy 4, Müller 4, Serrano 3; Koch, Rehfeldt, Vigerske, Lodi 2 each |
| 2021–2026 (HTW professor, ZIB guest) | 32 | 2 | 11 | 19 | Pokutta 7, Eifler 6, Hoen 5, Chmiela 4; Sofranac, Witzig, Nordström, Lodi, Bestuzheva 3 each |

[inferred] The move from first author to last author coincides with his move into the group-head role.

**K2. Exact-LP and IP partners outside the group; the iterative-refinement line began with Steffy's initiative.** [stated] (P) + [practice] (P) + [observed] (S)
- Daniel E. Steffy (Oakland University), the "initiative to study iterative refinement using SoPlex" (L5). Joint papers:
  - Gleixner, Steffy & Wolter, ISSAC 2012, DOI 10.1145/2442829.2442858
  - Gleixner, Steffy & Wolter, INFORMS J. Comput. 28(3) 449–464 (2016), DOI 10.1287/ijoc.2016.0692
  - Cheung, Gleixner & Steffy, "Verifying Integer Programming Results", IPCO 2017, LNCS pp. 148–160, DOI 10.1007/978-3-319-59250-3_13
  - Gleixner & Steffy, "Linear programming using limited-precision oracles", Math. Program. 183(1-2) 525–554, DOI 10.1007/s10107-019-01444-6
- Kati Wolter, later Jarck. Jarck (S11), PDF p. 147: "The development of the basic iterative refinement idea for feasible instances of the linear programming problem is joint work with Ambros M. Gleixner and Daniel E. Steffy". Her advisor was Grötschel, with referees Grötschel and Cook; defence 1 Jul 2019; DOI 10.14279/depositonce-9955.

**K3. Proof logging with SAT researchers, after a SAT programme visit.** [practice] (P) + [inferred]
- Simons Institute (P22): Gleixner was a "Visiting Scientist" in "Satisfiability: Theory, Practice, and Beyond", Spring 2021.
- Jakob Nordström first co-authors with him in 2023, through Mexi (arXiv 2307.14166) and later Hoen (DOI 10.1007/978-3-031-60597-0_20).
- [inferred] The programme visit preceded the first joint paper. No source says the visit started the collaboration.

**K4. Running a 21-person, multi-company committee: MIPLIB 2017.** [practice] (P)
- Gleixner, Hendel, Gamrath, Achterberg, Bastubbe, Berthold, Christophel, Jarck, Koch, Linderoth, Lübbecke, Mittelmann, Ozyurt, Ralphs, Salvagnin, Shinano, "MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library", Math. Program. Comput. 13(3) 443–490 (2021), DOI 10.1007/s12532-020-00194-3 (open access).
- p. 444: "In November 2016, a public call for contributions was launched and a group of 21 interested researchers, including representatives of the development teams of nine MIP solvers formed a committee in order to steer the process of compiling an updated library."
- p. 485, on why selection was formalised as a MIP: "this formalization of the selection criteria has served to increase the transparency of the selection process."
- p. 486: "The work for this article, in particular by the first, second, third, ninth, and last author, has been conducted within the Research Campus MODAL".
- [inferred] Contrast this with MIPLIB 2010 (Koch first, the rest alphabetical, Gleixner among them as a PhD student): Math. Program. Comput. 3(2) 103–163 (2011), DOI 10.1007/s12532-011-0025-9. In the MIPLIB 2017 paper, two of his PhD students moved up the byline.

**K5. Co-authors from other institutions, often students.** [practice] (P) + [observed] (S)
- Anna Melchiori (Padova). Gamrath, PDF p. 177: "A preliminary version of the branching rule was presented in Anna Melchiori’s master’s thesis “Experiments with branching on general disjunctions” (Melchiori, 2014)." This became Gamrath, Melchiori, Berthold, Gleixner & Salvagnin, CPAIOR 2015, DOI 10.1007/978-3-319-18008-3_10.
- Jasper van Doornmalen, a TU/e PhD student "Advised by Christopher Hojny and Frits Spieksma" (S19): van Doornmalen, Eifler, Gleixner & Hojny, arXiv 2311.03877.
- Edward Lam (Monash): arXiv 2401.17937 and arXiv 2607.15837.
- Andy Oertel and Jakob Nordström (affiliations not checked): DOI 10.1007/978-3-031-60597-0_20.

**K6. Machine-learning partners.** [practice] (P)
- Pokutta (ZIB/TU Berlin, formal advisor of Chmiela and Mexi), Lodi and Khalil: NeurIPS 2021, arXiv 2103.10294.
- Propagation work with Sofranac and Pokutta: arXiv 2009.07785 (GPU-parallel domain propagation) and arXiv 2106.07573 (an algorithm-independent measure of progress for linear constraint propagation).
- The ML4CO competition results paper: arXiv 2203.02433 (41 authors).

**K7. Interdisciplinary partner inside ZIB.** [stated] (P) + [practice] (P)
- Homepage 2016-04-13: "The exact solving features of SoPlex are available on the NEOS Server for Optimization and have been interfaced to the Python package cobraPy in order to solve multi-scale linear programming formulations over metabolic networks. This has triggered my interest in the use of optimization methodology for questions from computational biology."
- With Marcus Weber (ZIB), jointly in the ZIB Bridge Project "Mixed-Integer Programming for Cycle Detection in Nonreversible Markov Processes" (CV, P3): cycle detection in 2016 with Eifler and Witzig as co-authors (arXiv 1609.02063); sepsis diagnosis in 2026 (arXiv 2605.29686).

## 8. Training at community level

**M1. CO@Work 2024 summer school.** [practice] (P)
- P18: held "from September 16 to 27, 2024, at Zuse Institute Berlin with over 120 participants". Organizers: "Timo Berthold, Ralf Borndörfer, Ambros Gleixner, Thorsten Koch, and Milena Petkovic". Audience: "advanced masters students, PhD students, and post-docs". The page's HTML meta author is "Ambros Gleixner".
- His lectures:
  - "Organization and Overview of the Summer School" (with Petkovic)
  - "Linear Programming & Polyhedral Theory"
  - "Aspects of MIP Modelling", whose abstract ends "formulate some best practices in MIP modelling"
  - "Numerics in LP & MIP Solvers", whose abstract promises to "provide best practices for avoiding numerically troublesome computations"
- His earlier CO@Work talks were in 2009 and 2015 (CV). Videos exist on YouTube; I did not watch them (02 territory).

**M2. "Let's SCIP it!" (4 Nov 2022), SCIP's 20th anniversary.** [practice] (P)
- P17: organizers "Ambros Gleixner, Zuse Institute and HTW Berlin; Marc Pfetsch, TU Darmstadt; Sebastian Pokutta, Zuse Institute and TU Berlin; Franziska Schlösser, Zuse Institute Berlin". The programme's 09:30 "Opening" slot shows no speaker. Gleixner's name sits next to it only inside an HTML comment, so whether he gave the opening is not confirmed.
- The speakers included ZIB researchers (Besançon, Bestuzheva, Chmiela, Graczyk, Eifler, Rehfeldt) and outside co-authors (Hojny, van Doornmalen, Lam, Walter).
- ZIB news (S21) reported "almost 80 participants" and that "it was announced that SCIP will become truly open-source under the Apache 2.0 license starting with the upcoming release".

**M3. Computational competitions.** [practice] (P)
- "The MIP Workshop 2023 Computational Competition on Reoptimization", arXiv 2311.14834 (Bolusani, Besançon, Gleixner, Berthold, D'Ambrosio, Muñoz, Paat, Thomopulos). Its abstract: "Our goal is to establish a methodology for the generation of benchmark instances and an evaluation framework, along with benchmark datasets, to foster future research on reoptimization of mixed integer linear optimization problems."
- ML4CO results paper (arXiv 2203.02433), with Chmiela.
- His exact role on the organising committees was not verified beyond co-authorship.

**M4. Seminars and schools.** [practice] (P)
- CV 2017: co-organised Dagstuhl Seminar 18081, "Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization" (18–23 Feb 2018, with Bonami, Linderoth and Misener).
- COST TD1207 Training School "Optimization and Data", Novi Sad, 13–17 March 2017.
- Lectures at the MINO/COST Spring School on MINLP (Paris, 2016) and at the 5th Porto Meeting on Mathematics for Industry (2014).
- Graduate course "Optimierung in Industrie und Wirtschaft", FAU Erlangen-Nürnberg, winter semester 2016/17.

**M5. Editorial roles.** [practice] (P)
- HTW catalogue (P7): "Technical Editor Mathematical Programming Computation" (since 2015); Associate Editor INFORMS Journal on Computing (2019); Associate Editor Operations Research Forum (2019); Associate Editor Mathematical Programming Computation (2024).
- What he does as technical editor (code and reproducibility review) was not read (Gaps).

## 9. Failures, frictions and limits

**F1. No negative first-hand account found.** See the genre caveat. Mark Turner, a student of the same department and Gleixner's later co-author (arXiv 2512.17551), does not mention Gleixner in his acknowledgements at all.

**F2. Distress at department level, not about Gleixner.** [observed] (S)
- Turner, PDF p. 8: "This peaked during the the lock-downs of 2020, and was compounded with me having not yet found a research topic I wanted to work on. That was outright not a good year, with me being unhappy both personally and professionally." His advisor was Koch.
- This is the only account in the corpus of a student struggling to find a topic in the ZIB optimization environment. It concerns the department's freedom-heavy model, not Gleixner's supervision.

**F3. The funded project and the thesis topic can diverge.** [observed] (S)
- Rehfeldt (G7): the project he worked on "for most of my time" "had nothing to do with Steiner trees". He finished in a protected final 18 months.

**F4. Fixed-term contracts and re-advertised positions.** [practice] (P)
- IWA 30/17: "zunächst befristet auf ein Jahr (mit der Möglichkeit der Verlängerung)" [initially limited to one year, with the possibility of extension; my translation].
- The SynLab postdoc text of IWA 70/20 (19 Nov 2020) was re-issued almost unchanged as WA 12/21 (11 Feb 2021). The outcome is not documented. [inferred] The first round may not have filled the post, or there were two posts; this is unconfirmed.

**F5. A public correction under his lead.** [practice] (P)
- MIPLIB 2017, p. 485: "Despite all the care that was taken to exclude numerically critical instances from the benchmark set, problematic numerical properties of the two instances neos-5075914-elvire and neos-3754224-navua remained undetected during the selection process." p. 486: "An accordingly updated version of the benchmark set was published in June 2019."
- This is team-level error handling, not a student failure. It is recorded here because the fix was published openly in the paper he led.

**F6. No maintained public list of his students.** [practice] (P) His only list of mentees (2016) has been hidden in an HTML comment since January 2017 and never updated. There is no alumni page.

**F7. Structural limit.** [inferred] At ZIB he could not award doctorates. His students' degrees went through TU Berlin with Koch, Pokutta or Berthold as formal advisors. His formal footprint (one doctorate) understates his mentoring role, and any count of "his students" depends on which definition is used (Contradiction C1).

## 10. Era and resource context

| Period | Position | Resources and conditions (source) |
|---|---|---|
| 2002–2008 | Student in Bayreuth, UNSW Sydney and TU Berlin | Merit Foundation; DAAD scholarship; Honours project with Froyland; Siemens internships (CV) |
| 2008–2015 | Research assistant and PhD student at ZIB | Peer team of PhD students running SCIP after Achterberg left for ILOG (S10); MATHEON, BMS, MODAL and COST funding (thesis p. iv); ZIB clusters; CPAIOR 2011 chair as a PhD student |
| 2015–2023 | Head of Mathematical Optimization Methods, ZIB | 2017: 2 senior researchers, 10 research assistants, 4 student assistants (CV). PI for SAP, Siemens and BEAM-ME (CV); MODAL SynLab 2020–2023 (P8). By 2020 the group sat in the ZIB department "KI in Gesellschaft, Wissenschaft und Technologie" (P13). Release coordinator for SCIP 5.0 and 6.0 (G5) |
| 2020– | Professor at HTW Berlin (university of applied sciences); now listed as a guest at ZIB (P10) | Teaching load; bachelor theses; student assistants; third-party projects (P8); a doctoral student in GoPPS (S17); CO@Work co-organiser (P18). Bestuzheva head of a ZIB research group 2023–2025 (S18); that this is his former group is inferred (V5) |

## 11. Mapping to the seven layers (framework §一)

| Layer | What this note contributes | Strength |
|---|---|---|
| 1 Taste | Little: "fellow exact-solving enthusiast" (Eifler); exact tools offered for mathematical questions (T7) | weak |
| 2 Problem choice | PhD positions topic-bound to exact MIP, postdocs with open agendas (G2); industry funding shapes PhD positions (G6); HTW topics mirror live research lines (H3) | medium |
| 3 Idea generation | Challenging questions (O2); visits to collaborators lead to papers (T8) | weak–medium |
| 4 Experiments and execution | Merge-request checklist: performance runs, ctest, coverage, randomization (G4); student-built tools Ipet, MIP-DD and PaPILO (G8) | strong (written) |
| 5 Judging results | MIPLIB benchmark correction (F5); numerics best practices taught at CO@Work (M1) | weak in this note |
| 6 Writing | Berthold taught writing (O8); Gleixner proofreads (O7); byline conventions (T5); credit by contribution (L5) | medium |
| 7 Research organisation | Group head without formal title (V1–V2), coordination (O4), rotating release role (G5), funding (G6), the maintenance trade-off (G7), HTW model (H1–H4), community schools (M1–M4) | strong |

---

## Contradictions (kept, not reconciled)

**C1. Who supervised the 2016 mentees.**
- Gleixner (2016): "Currently, I am mentoring" Hendel, Müller, Rehfeldt, Serrano and Witzig "for their PhD projects at TU Berlin".
- Müller: "my supervisors Thorsten Koch and Ambros Gleixner".
- DepositOnce lists Koch as sole advisor for all five. MGP lists only Eifler as Gleixner's student. HTW lists one supervised doctorate.
- All of these hold at once. They count different things.

**C2. Gleixner's own doctoral roles.**
- Homepage and CV: "Committee: Martin Grötschel, Andrea Lodi, Thorsten Koch".
- DepositOnce: advisor Grötschel; referees Koch and Lodi.
- MGP: "Advisor 1: Martin Grötschel", "Advisor 2: Thorsten Koch".
- His own acknowledgements thank Grötschel and Koch "for their trust and for this support" and Lodi for "agreeing to be a member of my PhD committee".

**C3. "Long-term" and "fixed-term" in the same advert.** IWA 70/20 and WA 12/21 say both "Die Stelle ist langfristig angelegt" [the position is designed for the long term] and "befristet bis zum 31.03.2025" [fixed-term until 31 March 2025].

**C4. The year of Eifler's doctorate.** HTW lists 2024; DepositOnce and MGP list 2025. The title page gives the defence as 8 November 2024 and the publication as "Berlin 2025". The two dates count different events; I keep both.

**C5. Independent agendas versus coordinated research.** Postdocs are told "definieren Sie Ihre Forschungsagenda eigenständig" [you define your research agenda independently] (G2), while Gamrath credits Gleixner with "coordinating not only the software development but also the research of all members of your group" (O4). No source says how the two fitted together day to day.

**C6. Author order changed between versions of one paper.** "Strengthening SONC Relaxations with Constraints Derived from Variable Bounds" appeared as arXiv 2211.05518 (Bestuzheva, Gleixner, Völker; "4 pages … published in proceedings of the Hungarian Global Optimization Workshop HUGO 2022") and as arXiv 2304.12145 (Bestuzheva, Völker, Gleixner). The longer version moves Völker ahead of Gleixner. The reason, and Völker's career stage, are not documented.

## Gaps (what I could not find)

- No interview, student blog, memorial, Festschrift, lab handbook or onboarding guide. The five WebSearch queries were:
  1. interview/Porträt + SCIP + supervision
  2. "supervised/advised by Ambros Gleixner"
  3. blog + Ambros + SCIP + ZIB + PhD/postdoc
  4. "Let's SCIP it" programme
  5. news features on zib.de, htw-berlin.de, mathplus.de, forschungscampus-modal.de and math-berlin.de
- Master's and bachelor's theses he supervised at ZIB, TU Berlin or HTW are not identified. The OPUS frontend is behind an Anubis bot check, which I did not bypass. The OPUS OAI sets doc-type:masterThesis (87 records) and doc-type:bachelorThesis (13) contain only his own Diplom thesis. I found no public list of HTW bachelor theses.
- Alexander Hoen's formal doctoral arrangement (degree-granting university, advisor) was not found. iol.zib.de/team/alexander-hoen.html returned 404.
- No thesis or first-hand account was found on how Sofranac, Gottwald, Ghannam, Schlösser, Bolusani, Besançon or Graczyk experienced working with him.
- Internal group records are not public: the ZIB GitLab merge-request discussions, developer meetings, an internal wiki, and the "mipdev-solvable"/"minlpdev-solvable" test sets.
- I did not watch Gleixner's recorded lectures (CO@Work 2024 videos on YouTube); they belong to note 02. I found no talk in which he speaks about supervising.
- I did not read the SCIP Optimization Suite reports 3.2–7.0 (bylines taken from bibliographies), nor his work as MPC technical editor.
- No rejected paper, abandoned thesis or withdrawn student project is on public record. Who filled the 2016 PhD position (WA 28/16) and the 2020/21 postdoc post is not documented.
- Who added the "inform one of the developers responsible for SAP" line to the merge-request template before 2020 was not determined. It is absent from Gleixner's first version and from Hendel's 2018-02-01 edit (which added "Interface changes must be documented in doc/xternal.c and the CHANGELOG."). It does not appear as an added line in the per-commit patches the GitHub API returns for Code_Review.md, so it possibly came in through a merge commit.

## Sources

Primary (relative to Gleixner):
- P1. Gleixner, homepage "projects and research / cv / publications", current version (footer "© 2008-2022"), including the HTML comments in the source; accessed 2026-11-08. https://www.zib.de/userpage/gleixner/ — primary
- P2. Same homepage, Internet Archive snapshots of http://www.zib.de/gleixner/ from 2014-07-23 to 2023-02-03; used: 2016-04-13, 2016-07-29, 2017-01-20. http://web.archive.org/web/20160413181237/http://www.zib.de/gleixner/ — primary
- P3. Gleixner, "Curriculum Vitae of Ambros Gleixner", updated 31 July 2017 (7 pp.). https://www.zib.de/userpage/gleixner/gleixner.pdf — primary
- P4. Gleixner, "Exact and fast algorithms for mixed-integer nonlinear programming", PhD thesis, TU Berlin, 2015, acknowledgements pp. iii–iv (PDF pp. 5–6). DOI 10.14279/depositonce-4938 — primary
- P5. HTW Berlin, profile "Prof. Dr. Ambros Gleixner"; accessed 2026-11-08. https://www.htw-berlin.de/hochschule/personen/person/?eid=12822 — primary
- P6. HTW Online-Forschungskatalog, "Abgeschlossene Promotionen betreut von Prof. Dr. Ambros Gleixner". https://www.htw-berlin.de/forschung/online-forschungskatalog/promotionen/person/?eid=12822 — primary
- P7. HTW Online-Forschungskatalog, "Begutachtungen von Prof. Dr. Ambros Gleixner". https://www.htw-berlin.de/forschung/online-forschungskatalog/begutachtungen/person/?eid=12822 — primary
- P8. HTW Online-Forschungskatalog, "Projekte von Prof. Dr. Ambros Gleixner". https://www.htw-berlin.de/forschung/online-forschungskatalog/projekte/person/?eid=12822 — primary
- P9. HTW Wirtschaftsmathematik, "Aktuelle Themenvorschläge für Bachelorarbeiten", section "Prof. Dr. A. Gleixner". https://wm.htw-berlin.de/studium/bachelorarbeit/aktuelle-themenvorschlaege-fuer-bachelorarbeiten/#c92786 — primary
- P10. ZIB, member page "Gleixner, Ambros, Prof. Dr." (Position: Guest; Group: Prescriptive Systems). https://www.zib.de/members/gleixner — primary (institutional)
- P11. Gleixner, "[Opt-Net] Two open positions at Zuse Institute Berlin, Mathematical Optimization Methods", 25 Nov 2016. https://listserv.zib.de/pipermail/opt-net/2016-November/001282.html — primary
- P12. ZIB job advertisement IWA 30/17, 24 Aug 2017 (contact: Dr. Ambros Gleixner). https://www.zib.de/sites/default/files/jobad_attachments/IWA30_17_Wiss%20Angestellter_Optimierung%20Gleixner.pdf — primary (institutional)
- P13. ZIB job advertisement IWA 70/20 (SynLab postdoc), 19 Nov 2020. https://www.zib.de/sites/default/files/jobad_attachments/IWA70-20_SynLab_Postdoc_deutsch.pdf — primary (institutional)
- P14. ZIB job advertisement WA 12/21 (SynLab postdoc), 11 Feb 2021. https://www.zib.de/sites/default/files/jobad_attachments/WA%2012-21%20SynLab_Postdoc_Gleixner_deutsch.pdf — primary (institutional)
- P15. scipopt/scip, `.gitlab/merge_request_templates/` history (Feature.md, then Code_Review.md, then Default.md): commits 8201ee1d1e (2018-01-26), 126c5d7984 / 2cbce2c29b / 1d65082bed / e4e67068e1 / 94e02e518e (2020-08-27), 059df82c21 (2020-10-06), 3d1ffa8e2c (2021-09-21), feab05a3bd (2021-09-24), f1bab5d772 (2022-10-05), f92ac2cfb6 (2025-08-16). https://github.com/scipopt/scip — primary (practice)
- P16. Gleixner, Hendel, Gamrath et al., "MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library", Math. Program. Comput. 13(3) 443–490, 2021 (open access). DOI 10.1007/s12532-020-00194-3 — primary
- P17. "Let's SCIP it! A workshop to celebrate 20 years of Solving Constraint Integer Programs", programme and organizers, 4 Nov 2022. https://scipopt.org/20years/ — primary
- P18. CO@Work 2024 summer school page (organizers, schedule, abstracts), September 2024. https://co-at-work.zib.de/ — primary
- P19. arXiv API, author query "Ambros Gleixner" (48 preprints, 2016-04 to 2026-07); fetched 2026-11-08. http://export.arxiv.org/api/query?search_query=au:%22Ambros%20Gleixner%22 — primary (bylines)
- P20. DBLP SPARQL harvest for pid 07/3479 (74 records), fetched 2026-11-08 via sparql.dblp.org by research agent 01 (shared scratch file `dblp.json`) — primary (bylines)
- P21. Crossref REST API metadata for the journal and proceedings DOIs cited in this note (25 checked), 2026-11-08. https://api.crossref.org/works/ — record
- P22. Simons Institute, people page "Ambros Gleixner" (Visiting Scientist, Satisfiability: Theory, Practice, and Beyond, Spring 2021). https://simons.berkeley.edu/people/ambros-gleixner — primary (institutional)
- P23. DepositOnce (TU Berlin) REST API search "Gleixner" (37 items), with advisor and referee fields for 16 doctoral theses; 2026-11-08. https://api-depositonce.tu-berlin.de/server/api/discover/search/objects?query=Gleixner — record

Secondary (students, peers, collaborators, third-party records):
- S1. Leon Eifler, "Algorithms and certificates for exact Mixed Integer Programming", PhD thesis, TU Berlin, 2025 (defence 8 Nov 2024); acknowledgements PDF p. 4, chapter notes PDF pp. 11–12. DOI 10.14279/depositonce-23941 — secondary
- S2. Benjamin Müller, "Tighter relaxations in mixed-integer nonlinear programming", PhD thesis, TU Berlin, 2020; acknowledgements PDF pp. 7–8. DOI 10.14279/depositonce-9889 — secondary
- S3. Gregor Hendel, "Adaptive solver behavior in mixed-integer programming", PhD thesis, TU Berlin, 2022 (defence 28 Sep 2021); acknowledgements PDF p. 5. DOI 10.14279/depositonce-15958 — secondary
- S4. Jakob Witzig, "Infeasibility analysis for MIP", PhD thesis, TU Berlin, 2022 (defence 17 Dec 2021); acknowledgements PDF p. 3, chapter note PDF p. 15. DOI 10.14279/depositonce-15389 — secondary
- S5. Gerald Gamrath, "Enhanced predictions and structure exploitation in branch-and-bound", PhD thesis, TU Berlin, 2020; acknowledgements PDF pp. 3–4, Melchiori note PDF p. 177. DOI 10.14279/depositonce-10710 — secondary
- S6. Matthias Miltenberger, "Linear programming in MILP solving", PhD thesis, TU Berlin, 2023; acknowledgements PDF p. 5. DOI 10.14279/depositonce-22309 — secondary
- S7. Daniel Rehfeldt, "Faster algorithms for Steiner tree and related problems", PhD thesis, TU Berlin, 2021; acknowledgements PDF p. 7. DOI 10.14279/depositonce-12470 — secondary
- S8. Ralf Lenz, "Optimization of stationary expansion planning and transient network control by mixed-integer nonlinear programming", PhD thesis, TU Berlin, 2021; acknowledgements PDF p. 5. DOI 10.14279/depositonce-12765 — secondary
- S9. Jonad Pulaj, "Cutting planes for union-closed families", PhD thesis, TU Berlin, 2017; acknowledgements PDF p. 7. DOI 10.14279/depositonce-6534 — secondary
- S10. Timo Berthold, "Heuristic algorithms in global MINLP solvers", PhD thesis, TU Berlin, 2014 (defence 6 Nov 2014); acknowledgements PDF pp. 7–8. https://www.zib.de/userpage/berthold/Berthold2014.pdf — secondary (peer)
- S11. Kati Jarck, "Exact mixed-integer programming", PhD thesis, TU Berlin, 2020 (defence 1 Jul 2019); joint-work note PDF p. 147. DOI 10.14279/depositonce-9955 — secondary
- S12. Mark Ruben Turner, "Cutting plane selection for mixed-integer linear programming", PhD thesis, TU Berlin, 2024 (defence 1 Dec 2023); acknowledgements PDF p. 8. DOI 10.14279/depositonce-19742 — secondary
- S13. Gioni Mexi, "The two faces of mixed-integer programming: primal and dual progress", PhD thesis, TU Berlin, 2026 (defence 10 Sep 2026); chapter notes PDF p. 14; no acknowledgements. DOI 10.14279/depositonce-26588 — secondary
- S14. Antonia Chmiela, "Advancing mixed-integer programming using data-driven and deduction-based methods", PhD thesis, TU Berlin, 2025; chapter notes PDF pp. 24–25; no acknowledgements. DOI 10.14279/depositonce-24040 — secondary
- S15. Felipe Serrano Musalem, "On cutting planes for mixed-integer nonlinear programming", PhD thesis, TU Berlin, 2021 (defence 21 Aug 2020); no acknowledgements. DOI 10.14279/depositonce-12180 — secondary
- S16. Jesco Humpola, "Gas network optimization by MINLP", PhD thesis, TU Berlin, 2014; consulted, with no relevant mention of Gleixner outside the references. https://depositonce.tu-berlin.de/handle/11303/4552 — secondary
- S17. Alexander Hoen, personal homepage; accessed 2026-11-08. https://alexhoen.github.io/ — secondary
- S18. Ksenia Bestuzheva, CV; accessed 2026-11-08. https://kbestuzheva.github.io/assets/CV.pdf — secondary
- S19. Jasper van Doornmalen, résumé; accessed 2026-11-08. https://jaspervandoornmalen-nl.pages.dev/MJ_Jasper_van_Doornmalen_resume.pdf — secondary
- S20. Mathematics Genealogy Project, "Ambros M. Gleixner" (MGP id 206147) and "Leon Eifler" (MGP id 342910); accessed 2026-11-08. https://mathgenealogy.org/id.php?id=206147 and https://mathgenealogy.org/id.php?id=342910 — secondary (third-party record)
- S21. ZIB news, "Let's SCIP it: A workshop to celebrate 20 years of Solving Constraint Integer Programs", 2022-11-16. https://www.zib.de/news/lets-scip-it-workshop-celebrate-20-years-solving-constraint-integer-programs — secondary

Attempted, unreadable, blocked or empty:
- X1. ZIB OPUS frontend search (opus4.kobv.de/opus4-zib/solrsearch/…). Showed an Anubis proof-of-work bot check; not bypassed
- X2. dblp.org person XML (https://dblp.org/pid/07/3479.xml). Showed an Anubis bot check; not bypassed; P20 used instead
- X3. OPUS OAI-PMH sets doc-type:masterThesis and doc-type:bachelorThesis (https://opus4.kobv.de/opus4-zib/oai). The only match was Gleixner's own Diplom thesis (URN nbn:de:0297-zib-11389)
- X4. OPUS OAI-PMH set doc-type:report. Has 47 records; the SCIP and MIPLIB reports are not in this set
- X5. https://iol.zib.de/team/alexander-hoen.html. Returned 404
- X6. SCIP blog (https://www.scipopt.org/blog/, five posts from 2026). No mentorship content
- X7. CO@Work 2020 page (https://co-at-work.zib.de/berlin2020/). No Gleixner listing found by text search
- X8. scipopt/scip CONTRIBUTING.md. Does not exist (404); the merge-request template (P15) is the closest equivalent
- X9. WebSearch, 5 calls (queries listed under Gaps). None found an interview, student blog or memorial; the leads they did give are listed in the header
