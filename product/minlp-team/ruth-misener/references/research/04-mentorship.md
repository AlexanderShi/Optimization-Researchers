# Ruth Misener: students, postdocs, fellows and collaborators (research agent 04)

| Field | Value |
|---|---|
| Researcher | Ruth Misener. Professor in Computational Optimisation, Department of Computing, Imperial College London. PhD Princeton 2012 with Christodoulos A. Floudas. Royal Academy of Engineering (RAEng) Research Fellow 2012–2017, hosted by Efstratios N. Pistikopoulos at Imperial's Centre for Process Systems Engineering (CPSE). EPSRC Early Career Fellow 2017–2022. BASF/RAEng Research Chair in Data-Driven Optimisation 2022–2027 |
| Dimension | 04: mentorship. Covers supervision style, group habits, lab culture and tacit knowledge as students, postdocs, fellows and industrial collaborators describe them, checked against the record (CV, thesis records, GitHub, papers) |
| Research date | 2026-10-10 |
| Sources consulted | 59. Of these, 50 were used: 27 primary (P1–P27) and 23 secondary (S1–S23). The other 9 were attempted but unreadable or unusable (X1–X9, see Gaps) |
| WebSearch calls used | 2 of 2. Both returned nothing relevant (no interview or student blog about her supervision) |
| User-supplied material | None. At the start of this run `references/sources/{papers,talks,essays,software}` held only `.gitkeep`. During the run a sibling research agent saved auto-generated (ASR) YouTube transcripts to `references/sources/talks/`. I used seven of them and label every quote from them "ASR". They are not user-supplied. I did not open `private/` |
| Language | English (per team.json) |

**What was read and how.** I found no student blog, memorial piece, Festschrift, lab handbook or onboarding guide about Misener. She is living and mid-career, so none of these would be expected yet.

The best first-hand evidence is the acknowledgements and front matter of her advisees' doctoral theses. Imperial's Spiral repository (DSpace REST API) lists **11 theses with `dc.contributor.advisor = Misener, Ruth`** (2018–2025). I downloaded all 11 open-access PDFs and read the acknowledgements and front matter in full, plus selected passages. Two of them, Wiebe 2021 and Olofsson 2020, have text layers that cannot be extracted (custom font encoding / no text). For those I rendered the acknowledgement pages to images and read them visually, at PDF p. 5 of each.

The other main sources:

- her own CV (32 pp., "Updated December 3, 2025") and her group web pages
- her 2016 memorial essay on Floudas, the most important first-person source on how she was supervised
- three Imperial News articles she wrote about her students
- ASR transcripts of her 2023 inaugural lecture (including the vote of thanks by Pistikopoulos) and six other talks
- Imperial News articles that quote her students and industrial collaborators
- the cog-imperial GitHub organisation and the Computational Optimisation Group (COG) public seminar sheet

Text was extracted with pdftotext. "PDF p." means the PDF page and "p. iii" the printed page. Ligatures dropped by extraction are restored (e.g. "di cult" → "difficult", "coﬀee" → "coffee"); spelling is otherwise as in the source.

**ASR quotes are verbatim auto-captions, errors included.** For example, "Flutus" = Floudas, "Mitten Mystery" = Miten Mistry, "MNG"/"Amen" = MEng, "Pistolus" = Pistikopoulos. Clarifications are in [square brackets].

**Division of labour with the other notes.** Publication analysis (01), stated research method (02) and code-process evidence (03) are covered elsewhere. I use them only where they bear on supervision, credit and group habits.

**Tags.**

- [stated] = Misener's own words.
- [practice] = what the record shows (CV entries, thesis metadata, author lists, GitHub).
- [observed] = what students, postdocs or collaborators say.
- [inferred] = my reading, not evidence.

(P) means primary relative to Misener and (S) means secondary. A student's acknowledgement is first-hand for the student but **secondary** for Misener, so it is marked (S).

**Genre caveat.** Thesis acknowledgements are a genre of gratitude. Criticism is structurally absent from them. Counting how often a theme appears measures what students chose to thank her for, not how often she behaved that way. **No negative first-hand account of her supervision was found anywhere.** That absence is not evidence that there are none.

---

## 1. Lineage: how she was supervised, and what she says she took from it

**L1. Choosing the advisor; the advisor's belief in students.** [stated] (P)
- Floudas memorial, SIAG/OPT Views and News 24(1), Oct 2016, p. 12: "My father often repeated in my childhood that choosing an advisor is the most important decision a graduate student makes. Whatever mistakes I made as a Ph.D. student, I did one thing exceptionally well: I was privileged to work for Professor Christodoulos Achilleus Floudas. Chris’s commitment to excellence was inspiring; his belief in his students was motivating; his enthusiasm for global optimization was contagious."
- Same essay, p. 12: Floudas "became the first recipient of Princeton University’s (now annual) Graduate Mentoring Award" (2007). He "supervised 34 Ph.D. students and 20 postdoctoral research associates."
- Era: Princeton chemical engineering, 2007–2012, NSF Graduate Research Fellowship (CV p. 1; homepage, Professional Activities).

**L2. Real instances, not toy problems; the student objects and the advisor insists.** [stated] (P)
- p. 13: "But Chris was never interested in toy problems or proofs of concept. If he was going to apply mathematical optimization to a new problem class, he would always push optimization to its limit via highly relevant, industrially motivated test cases."
- p. 13: "I remember raising some objections when Chris said that now we had to globally optimize a model with 15,439 continuous variables, 30 binary variables, 15,406 equality constraints, 230 inequality constraints, and 335 nonconvex terms [116]. But Chris absolutely insisted that his piecewise linear underestimation technique for bilinear terms [117–119] was not relevant unless it was effectively applied to real-world instances."
- p. 14: "But, more than anything, I appreciated how Chris made my work relevant by insisting that it could apply to realworld problems."

**L3. The software promise at the early-stage assessment.** [stated] (P) + [practice] (P)
- p. 14: "In 2008, when Chris told me that my early-stage Ph.D. assessment needed a promise to write and publicly release a global MINLP solver, I told him he was being unreasonable. He said to do it anyway; and I must have made a face, because I remember him telling me sharply: “you will not roll your eyes at your advisor!” He was right in the end, and we released ﬁrst GloMIQO [131] and then ANTIGONE [132] as global optimization solvers in the modeling language GAMS."
- Record: Misener & Floudas, "GloMIQO: Global mixed-integer quadratic optimizer", J. Global Optim. 57:3–50, DOI 10.1007/s10898-012-9874-7. Misener & Floudas, "ANTIGONE: Algorithms for coNTinuous / Integer Global Optimization of Nonlinear Equations", J. Global Optim. 59:503–526 (2014), DOI 10.1007/s10898-014-0166-2. Both checked on Crossref.
- Her CV (p. 10) still separates this PhD-era code, under "Numerical Software", from her team's code: "The following implementations are primarily written by me. Implementations of my group's optimisation algorithms, i.e. code primarily written by my team, are on our GitHub account." [stated] (P)
- [inferred] The requirement "ship a public solver as part of the thesis" reappears in her own group. Several advisee theses list an "Open-Source Software" section, and the group's code lives in a public organisation (H6). Whether she imposes it as a formal requirement, as Floudas did, is **not documented**.

**L4. A question carried for eight years, answered with her own PhD student.** [stated] (P) + [practice] (P)
- p. 13: "still Chris would push me: Why did these piecewise approximations work so well? How could we eliminate the computational dependence on parameters? Actually, thanks to work with Radu Baltean-Lugojan [127], I ﬁnally have a ﬁrst answer to these questions Chris asked me eight years ago; I had been so looking forward to upcoming conferences to tell him all about it."
- Record: Baltean-Lugojan & Misener, "Piecewise parametric structure in the pooling problem: from sparse strongly-polynomial solutions to NP-hardness", J. Global Optim. 71:655–690, DOI 10.1007/s10898-017-0577-y (Crossref). Her CV p. 4 marks it as an "Invited article for a special issue in memory of Professor C. A. Floudas".
- The student's thesis abstract describes the result as "validating a long-held and heuristically successful intuition" (Baltean-Lugojan 2019, PDF p. 3).
- [inferred] This is the clearest documented case of a question passing down an academic generation: an open question from her own supervision became her first-generation student's thesis chapter.

**L5. The advisor's reply to good news.** [stated] (P)
- p. 13: she emailed Floudas a result titled "good news" and got this reply on 12 March 2011: "Dear Ruth, This is great!!! I would like to see what you and Jamie have upon my return. I have some additional ideas that I would like to discuss too. With best regards, Chris". He had just been at Narita airport during the Tōhoku earthquake. "Chris was himself a force of nature: Just 24 hours after the aftershocks … had mostly stopped, Chris was back to actively encouraging his Ph.D. students in their projects" (pp. 13–14).

**L6. "People first", attributed to Floudas.** [stated] (P, ASR)
- Inaugural lecture, 13 Mar 2023 (ASR): "my PhD supervisor uh Chris Flutus extraordinary guy uh he died very young at the age of uh 56 in 2016. and he's when I do it correctly uh I remember to put uh the the people first and then what the things that we do here in the university the research and the teaching second and um he's the one who taught me that"

**L7. Placement through the advisor's network; a second "supervisor" after 2016.** [observed] (S, ASR) + [stated] (P, ASR)
- Vote of thanks by Pistikopoulos (same recording, ASR): Floudas, on Pistikopoulos's 2009 visit to Princeton, "introduced me to his next big thing who who had the name by Ruth Mer". Then, late 2011, "I get a phone call from Chris … you know, I have some breaking news", about her planned postdoctoral move to the UK: "said you know we'll make this happen".
- Misener (ASR): "my post-doal supervisor who will give the vote of thanks at the end uh this is Pistolus has been basically had to do double duty also as my uh PhD supervisor".
- Record: RAEng Research Fellowship 2012–2017; Imperial College Junior Research Fellowship "declined" (homepage, Professional Activities; CV p. 1).

**L8. Institutional mentoring she says she received at Imperial.** [stated] (P, ASR)
- Head of department: "she would sit in our uh coffee room uh from about 10 to 11:00 a.m. uh every morning and we could go and ask her questions and that was how I got a lot of my insider information."
- Grant culture: "Something that we do really well at Imperial is um or rather a lot of people have done very well for me um is reading each other's grants, telling each other where uh we're weak and uh really uh trying to uh improve things."
- Partner as grant coach (ASR): "his ace in the hole is grant rebuttals … the key is disappointment. You're disappointed that the the reviewer didn't understand." And: "we've we've shadow supervised everybody and then navigated life together". What "shadow supervised" means in practice is **not explained**.

**L9. A difference in style across the lineage.** [inferred]
- She reports a sharp, demanding Floudas ("you will not roll your eyes at your advisor!") whom she nonetheless credits with belief in students.
- Her own students mostly describe patience, availability, humour and adjusting to the student (§4).
- Both generations share three things:
  - insisting on real instances (L2; her industrial projects, S5)
  - public software (L3; H6)
  - pushing students past what they think they can do (Kouyialis: "pushed me to reach my full potential and exceed myself", §4)

---

## 2. Layer 7: supervision structure

**S1. Scale and composition of the team (as listed by her, Dec 2025).** [practice] (P: CV pp. 23–27; Alumni and Current Team pages)

| Role | Completed | Current (2025–26) | Notes |
|---|---|---|---|
| Research fellows (UK "intermediate between Postdoctoral Associate and Lecturer") | 2: Jan Kronqvist (Royal Society Newton International Fellow, 2019–21), Calvin Tsay (EPSRC David Clarke Postdoctoral Fellow + Imperial College Research Fellow, 2020–22) | — | "I collaborate with research fellows and assist in developing their independent research careers" (CV p. 23) [stated] |
| Postdoctoral research associates | 9: Oberdieck (primary supervisor Pistikopoulos), Letsios, Cyras (primary supervisor Toni), Campos Salazar, Mistry, Ceccon, Kappatou, Sedgwick, Qing | 3: Campos (rehired 2022–), Morozovska, Sandrin | Several were her own PhD graduates staying on briefly (Mistry 2020, Ceccon 2021, Sedgwick 2023–25) |
| PhD (Department of Computing; Spiral advisor field) | 11, awarded 2019–2025 | 1 listed on her page (Toby Boyne, 2023–). The COG people page lists more students shared across COG PIs | First PhD student started 2014 (Kouyialis) |
| PhD (Chemical Engineering, collaboration only) | 2: Fuentes-Garí, Savvopoulos (supervised by Mantalaris and Pistikopoulos) | — | She lists them as collaborations, not as her students |
| MSc / MEng / BEng / UROP projects | about 35 names, 2014–2025 (CV pp. 26–27) | — | Several theses became papers (C3) |

**S2. Recruitment channels: how people came to her.**

| Channel | Evidence | Tag |
|---|---|---|
| Her own taught courses → MEng/MSc project → PhD | Mistry: MEng 2014–15 → PhD 2015–20. Ceccon: MSc 2015 → PhD 2016–21 (CV pp. 25–26). Teaching page: "I strongly recommend that anyone who wants to do a research with project me [sic] take 60016 Operations Research and 70007 Computational Optimisation." CV p. 23: "The teaching innovation recognition is due to how frequently I discuss research in the classroom." Inaugural lecture (ASR) on Mistry: "He was the first MNG student that I al ever got to work with in this department and sort of that's where I learned how good the Amen students could be." | [practice] (P), [stated] (P) |
| A colleague's referral | Olofsson (PDF p. 5, page image): Deisenroth "agreeed [sic] to supervise my M.Sc. thesis project … When Ruth received funding for a new student, Marc introduced us and vouched for me." Baltean-Lugojan (PDF p. 4): Parpas "introduced me to Dr. Ruth Misener". Kouyialis (PDF p. 6): a former COG member introduced her to Rustem, who "kindly supported my PhD application". | [observed] (S) |
| Doctoral-training-centre (CDT) pools | Folch (PDF p. 6): "Having been chosen by both of you in the random selection process that is the StatML application pool was perhaps the luckiest thing that happened during my PhD." Mistry and Wiebe came through the HiPEDS CDT, Sedgwick through AI4Health (homepage Alumni page). | [observed] (S), [practice] (P) |
| Interview plus scholarship support | Zhang (PDF p. 5): "I am incredibly grateful that you were willing to interview me, offer me a position, and support my scholarship application during such a difficult time." (Hans Rausing Scholarship, CV p. 26) | [observed] (S) |
| Thesis examining → postdoc or fellowship | She examined Campos Salazar (Imperial, 11/2017), Kronqvist (Åbo Akademi, 09/2018) and Kappatou (RWTH Aachen, 11/2020) (CV p. 29). Each then joined her team: Campos 2018–20, Kronqvist 2019–21, Kappatou 2020–23 (CV pp. 23–24). | [practice] (P). The causal link is [inferred]; no source says the examining led to the hire |
| Public call | "We encourage prospective PhD candidates, MSc and undergraduate students, and postdoctoral associates interested in our research to contact Dr Ruth Misener; please include a CV and a brief statement of interest." (Research Team page) | [stated] (P) |

**S3. Formal co-supervision.** [practice] (P: Spiral advisor fields, homepage, CV) + [observed] (S)
- Imperial uses second supervisors. Parpas: Kouyialis, Baltean-Lugojan, Ceccon. Huth: Mistry.
  - Ceccon (PDF p. 4) on Parpas: "his comments on my research always proved to be helpful in understanding how to improve and clarify my work."
  - Baltean-Lugojan (PDF p. 4) on Parpas: "His relaxed approach is truly inspiring when one needs to take a step back and rethink".
- Co-supervisors from other departments for CDT and interdisciplinary students: van der Wilk (Folch; Sedgwick), Stevens (Sedgwick), Filippi (Odgers), Deisenroth (Olofsson, per the homepage; **not** in the Spiral advisor field, see Contradictions).
  - Sedgwick (PDF p. 6): "Starting with Ruth Misener for her excellent scientific guidance and always keeping me on track. Also to Mark van der Wilk for enriching conversations, clarity in his explanations and always asking the right questions."
  - Folch (PDF p. 6), to Misener and van der Wilk: "I hope you keep working together for many years as you make a fantastic duo."
- Co-supervised students also belong to a second lab (OccamLab, the Filippi Lab, the Stevens group). Folch (PDF p. 7): "The Computational Optimisation Group was the group I would frequent most on a daily basis."
- CDT students can be registered outside Computing. Folch's thesis is in Spiral under the Department of Mathematics (StatML CDT).

**S4. A mentoring layer of postdocs and fellows between PI and student.** [observed] (S) with record checks [practice]

| Student (thesis year) | Postdoc or fellow named as mentor | Words used (verbatim) |
|---|---|---|
| Kouyialis (2018) | Dimitrios Letsios | "He has been a tremendous mentor to me … I keep all his advice and move forward with his words: to set a big goal (that probably scares me) and to constantly work towards that." (PDF p. 5). Also on Campos: "I will never forget the guidance of Dr. Juan Campos Salazar on the ﬂow of my ﬁrst formal presentation." (PDF p. 6) |
| Mistry (2020) | Letsios, Kronqvist, Campos, Callia D'Iddio | "I thank my postdoctoral mentors: Dr Dimitrios Letsios for his support and guidance in academic writing and insight into approximation algorithms, Dr Jan Kronqvist for his willingness to discuss my ideas at length and for showing me what it means to be inquisitive, Dr Juan Campos Salazar for ensuring that my intuition was backed by rigour, and Dr Andrea Callia D’Iddio for his insight in logic-based methods." (PDF p. 7) |
| Thebelt (2023) | Kronqvist, Tsay | "The postdocs with whom I’ve had the privilege to collaborate, Dr. Jan Kronqvist and Dr. Calvin Tsay, have had a profound impact on my professional growth" (PDF p. 6) |
| Folch (2024) | Tsay | "Even though it is not official, I will always consider you as my third supervisor. Your help was invaluable and is present in every piece of work I have done in the last four years." (PDF p. 6) |
| Odgers (2025) | Kappatou | "I could not have asked for a better or kinder role model to aspire towards and I hope that I will be able to be half as good a post-doc to others as you were to me." (PDF p. 5) |
| Zhang (2025) | Campos; Tsay | Campos: "Beyond being a co-author and mentor for every paper in this thesis". Tsay: "a wonderful collaborator, and an unofficial supervisor … You made the process of doing research enjoyable, rather than stressful or publication-driven." (PDF pp. 5–6) |

- Record check [practice]: all four papers in Zhang's thesis list "Juan S. Campos" as co-author (thesis publication list). Tsay is a co-author on Folch's SnAKe (DOI 10.52202/068431-2553) and CACE 2023 (DOI 10.1016/j.compchemeng.2023.108194) papers.
- [inferred] Six of eleven theses name a postdoc or fellow, not the PI, as a day-to-day technical or writing mentor. **The group runs a two-level system:** Misener sets direction and standards, and postdocs or fellows do much of the line-by-line mentoring. She frames this as part of developing the fellows ("I mentored Dr Tsay in developing his independent research career", Alumni page) [stated] (P).

**S5. Industrial collaborators as co-advisors.** [observed] (S) + [practice] (P: funding lines, CV pp. 27–28)

| Student | Partner and funding | What the student says |
|---|---|---|
| Mistry | BASF (Robert M. Lee, Gerhard Krennrich) | "for their guidance in machine-learning concepts" (PDF p. 7) |
| Thebelt | BASF-funded studentship | "Their guidance was crucial not only for the successful completion of my industrial collaboration but also for providing a deeper understanding of the industrial perspective, which greatly improved my research and academic writing." (PDF p. 6) |
| Folch | BASF + StatML CDT | "Thank you for allowing me to always chase my curiosity and for providing invaluable feedback across the many projects we worked on together. After some years of working together, finally getting to meet you in person when I visited BASF was one of the highlights of my PhD." (PDF p. 6) |
| Zhang | Hans Rausing Scholarship + BASF | "I would like to thank my industrial advisors … Despite your demanding day jobs, you were always generous with your time and support. Your feedback consistently helped shape our work toward greater practical relevance and real-world impact." (PDF p. 6) |
| Wiebe | Schlumberger EPSRC Industrial CASE studentship | Thesis (page image, PDF p. 5): thanks his "supervisor at Schlumberger Cambridge Research" and colleagues "for listening to my presentations and always giving me great feedback and helping me to ground my work in practically relevant problems." Imperial News, 2 Jun 2021: "As part of my studentship, I got to spend time in the Schlumberger office in Cambridge … I appreciate the opportunities I received to present my work to my industrial collaborators several times. They gave me detailed, immediate and thoughtful feedback that helped me check my thinking and research in real time." |
| Odgers | Eli Lilly / EPSRC Prosperity Partnership | "the industry perspective you provided added a level of richness to my research which I would not have been capable of achieving otherwise … The trips I took to Lilly were some of the most interesting highlights of my PhD." (PDF p. 5) |
| Olofsson | ModLife Marie Skłodowska-Curie ITN | Hosted at RWTH Aachen (Apr–May 2017) and Bayer AG (Mar–Apr 2018) (PDF p. 6, page image) |
| Page (MSc), Suraj G (MEng) | Royal Mail | "On the Imperial side, Natasha was mentored by Dr Dimitrios Letsios and Dr Ruth Misener." (Imperial News, 15 May 2019, by Misener) |

- The collaborator's view [observed] (S): Robert M. Lee of BASF, Imperial News, 31 Oct 2022: "Our partnership with Ruth [Misener] is extremely valuable because her group has one foot in chemical engineering and one in AI, which is essential in this kind of work. It’s refreshing for us to collaborate with academia; it gives you a different way of looking at things. It’s stuff we couldn’t develop in-house."
- Her own account of the funding model [stated] (P, ASR, inaugural Q&A), answering how she combines fundamental work with industry: "it's basically you work with with CDTs and then the companies think, "Oh, I'm just putting a little bit of money and then they sort of don't chase me as much." So, I get really cool problems from industry". CDT = doctoral training centre; the company part-funds a CDT studentship.
- 2025 (Manchester talk, ASR): "I am funded by BSF [BASF] so uh I am also you know my my PhD students are paid to put it put it put their things in". "It" is BASF's open-source BoFire package, arXiv 2408.05040 (checked); the Folch thesis bibliography lists Boyne and Misener among its authors. [stated] (P)

**S6. Cascade supervision: students supervise students; code is reviewed before it is merged.** [practice] (P) + [observed] (S)
- Ceccon's thesis front matter (PDF p. 6) lists the galini-dashboard repository with "I supervised the undergraduate student project."
- Folch (PDF p. 8): "I would like to thank Clara and Stefan for all the patience given to me while I was learning how to be a supervisor." Her CV lists Clara Stoddart (MEng 2022–23) and Stefan Savulescu (MEng 2023–24).
- Outcome of a student-run project: Stoddart, Shrack, …, Misener, Folch, Sedgwick, "Gaussian Processes for Monitoring Air-Quality in Kampala", arXiv 2311.16625 (checked; NeurIPS 2023 Workshop on Tackling Climate Change with ML, per CV W02). The two undergraduate-level authors come first and the two PhD students who supervised them come last, after Misener.
- She says this collaboration came from the students (Manchester 2025, ASR): "I did not come up with this collaboration um my two of my PhD students went to this AI for good dog tool and they came back with this collaboration um with this team in uh in Uganda". [stated] (P)
- Code review of an undergraduate contribution:
  - OMLT pull request #91 "Support for max pooling layers" was opened 2022-09-19 by an undergraduate research (UROP) student. Calvin Tsay (`tsaycal`) reviewed it ("COMMENTED", 2022-09-26). Misener (`rmisener`) approved and merged it on 2022-10-01 (GitHub API). [practice] (P)
  - Imperial News, 23 Nov 2022: Misener, "who supervised Adi’s UROP explained that “not only did Adi successfully implement state-of-the-art research technology before taking the prerequisite modules, but he also proved his work’s excellence to everyone on our team by developing effective testing examples.”" [stated] (P, quoted in a secondary article)

**S7. Developing fellows' independence.** [stated] (P) + [practice] (P)
- Alumni page: "I collaborated with Dr Kronqvist and mentored him in developing his independent research career." and "I mentored Dr Tsay in developing his independent research career."
- CV p. 27 lists the fellowships under "Fellowships to my team members". Each line reads "Fellow … developed his independent research and collaborated with my team".
- Fellows lead papers, and she credits them in talks:
  - Kronqvist & Misener, "A disjunctive cut strengthening technique for convex MINLP", Optim. Eng. 22:1315–1345, DOI 10.1007/s11081-020-09551-6 (Rosenbrock Prize per homepage).
  - Kronqvist, Misener & Tsay, "Between Steps: Intermediate Relaxations Between Big-M and Convex Hull Formulations", CPAIOR 2021, LNCS pp. 299–314, DOI 10.1007/978-3-030-78230-6_19 (Distinguished Paper Award).
  - Sevilla seminar 2021 (ASR): "what i'm presenting today is work that is done uh primarily by calvin say [Tsay] and john cronquist [Jan Kronqvist] jan led one of the two papers that's going to appear in cpaior and calvin led a paper that is now posted to archive".
- Fellows co-organise with her: "Imperial Mixed-Integer Nonlinear Optimization Workshop (held virtually) … Joint with Prof M Anjos, Dr P Belotti, Dr J Kronqvist" (CV p. 30). The CogImperial YouTube feed has the 2021 talks.
- Outcome [practice]: Kronqvist is now Associate Professor at KTH. Tsay is faculty in the same department and recruits his own students into the same office. Zhang (PDF p. 8): "I don’t know how Calvin recruited three such excellent PhDs".

**S8. Freedom in direction, discipline on the track.** [observed] (S)
- Freedom:
  - Ceccon (PDF p. 4): "Since I started, she always provided the support I needed to take my research where I wanted."
  - Zhang (PDF p. 5): "Knowing that I had broad interests and intended to pursue a career in industry rather than academia, you gave me the freedom to explore various research directions, and encouraged me to get involved in many projects. Whenever I needed guidance, you were always there, helping me find the right path."
  - Folch (PDF p. 6): "opening so many doors and opportunities, while also allowing me to have fun and remain positive throughout."
- Discipline:
  - Sedgwick (PDF p. 6): "always keeping me on track".
  - Zhang (PDF p. 5): "I’ve been putting off writing this part for months. But now I have to do this because Ruth asked me to submit my thesis :)"
- Adapting to the student: Kouyialis (PDF p. 5): "Her willingness to invest time and adjust her training style to one’s needs and to guide with her valuable knowledge distinguishes her as an exceptional advisor."

**S9. Matching the student to the difficulty of the project.** [stated] (P, ASR, inaugural Q&A)
- On Sedgwick's diagnostics project: "one of the reasons that that is such a challenging project and she has to be a very strong PhD student to be doing this project is that uh the data is much messier than we typically uh see with some of the nice engineering problems uh that that um we set up um in in manufacturing or something like this. So um she has to wrestle with her data um in a in a really deep kind of way."
- Same lecture, on credit for that work: "I'm using this particular substory not because I led it but because it fits my story."

**S10. Career orientation: industry is a normal outcome.** [practice] (P) + [observed] (S)
- Destinations of the 11 Department of Computing PhD graduates (homepage Alumni page; CV Dec 2025): Dataiku; Millennium / Eisler Capital; minimax labs; Facebook / Meta; co-founder (Auclantis / Apibara); Flexciton; QuantCo; Xyme; SOLVE (co-founder and CSO); a postdoc at Helmholtz Munich; ByteDance.
- **10 of 11 are outside academia; none holds a faculty post.** The academic placements come from postdocs and fellows instead: Kronqvist (KTH), Tsay (Imperial), Letsios (King's College London), Qing (Lancaster).
- Students say the training was meant to serve either path:
  - Olofsson (PDF p. 5): "for teaching me invaluable skills for my future career in or outside academia".
  - Baltean-Lugojan (PDF p. 4): "valuable independent skills I can draw on beyond my PhD".
  - Ceccon (PDF p. 4): "skills that will serve me through my career".
  - Zhang's industry intention was explicitly supported (S8).
- [inferred] The doctoral programme is not built to reproduce academics. PhDs are trained for industry or startups (two co-founders), while the fellowship and postdoc tier is where academic careers are built.

---

## 3. Layer 7: group habits and lab culture

**H1. One shared office over seven years: Huxley 302.** [observed] (S) + [practice]
- Kouyialis 2018 names colleagues "from 302 oﬃce" (PDF p. 6).
- Olofsson 2020: "the Huxley 302 office a great place to spend 3.5 years" (PDF p. 5, page image).
- Thebelt 2023: "my former oﬃce 302 colleagues" (PDF p. 6).
- Odgers 2025: "The members of 302 and the Computational Optimisation Group is the group which I have had the chance to share an office with" (PDF p. 5).
- Zhang 2025: "As I sit at my desk in Huxley 302, just like on any ordinary day over the past four years" (PDF p. 5).
- The office is shared across COG PIs (Rustem, Parpas, Wiesemann, Paccagnan, Tsay). Students from other COG groups appear in her students' thanks.

**H2. Tea, coffee, lunch, pub and celebrations.** [observed] (S) + [stated] (P) + [practice] (P)
- Ceccon (PDF p. 4): "with our discussions over tea they helped shape my research and fill in the knowledge gaps I had".
- Wiebe (PDF p. 5, page image): "You have made the office such a friendly and enjoyable space. Thank you for our valuable discussions and for helping me procrastinate over coffee/tea/hot water and biscuits."
- Mistry (PDF p. 7): "the many coffee breaks, lunches, dinners, pub trips, and hours of laughter". Thebelt (PDF p. 6) uses near-identical wording: "countless coffee breaks, lunches, dinners, pub trips, and hours of laughter".
- Sedgwick (PDF p. 6): "great lunchtime chats and their help when my experiments weren’t performing as expected".
- Zhang (PDF p. 8): "We celebrated every birthday, welcomed new members, and bid heartfelt farewells to those moving on."
- Kouyialis (PDF p. 6): "Dr. Ruth Misener manages to attract the nicest people in her group. There is a strong spirit of support and collaboration (among related and unrelated topics!) within all the group members which made a great environment to spend most of my everyday time during the PhD."
- Her own words (inaugural Q&A, ASR): "basically I'm a person who chooses my my my my vision in some part by my pub buddies. Um so basically um anyone who wants to come to the pub with me we will end up writing a paper together after after some amount of time." Later: "So in some ways very opportunistic."
- Record: the Research Team page's photo captions are "Christmas lunch, December 2023", "Builders Arms, December 2019", "Builders Arms, December 2018", "Hyde Park, December 2016", and campus photos from 2017 and 2021. The COG home page adds "group dinner (Aug, 2025)" and "relaxing after NeurIPS 2023".
- She "Organise[d] departmental entry to the London Duathlon, 2015, 2016" (College Service page).

**H3. A weekly group seminar with a rota, practice talks and external speakers.** [practice] (P)
- The public COG events page links a "COG weekly seminars" sheet; I read the public CSV export, covering 10 Oct 2025 to Dec 2026. It shows a near-weekly Friday slot.
- The slot rotates among PhD students, postdocs and Tsay. There are external speakers (for example Ryan Cory-Wright, David Bernal, Johannes Köhler).
- There are explicit **conference practice sessions**: "Practice talks for AIChE Meeting" (17 and 24 Oct 2025), "IFAC practice talks" (14 Aug 2026), "AIChE Practice" (23 Oct 2026).
- Breaks are scheduled for exams, Easter, the start of term and "Undergraduate project presentations".
- Scope: this is the COG-wide seminar (Misener, Tsay, Paccagnan, Parpas), **not hers alone**. I found no record for earlier years.

**H4. Internal workshops where early work is shown.** [practice] (P)
- Her own Imperial News article (13 Oct 2022) has the photo caption: "Alexander Thebelt presents an early-stage version of his NeurIPS 2022 paper at an internal Imperial workshop in 2019". The paper is Thebelt et al., "Tree Ensemble Kernels for Bayesian Optimization with Known Constraints Over Mixed-Feature Spaces", NeurIPS 2022, DOI 10.52202/068431-2711.
- [inferred] Work was shown internally about three years before the top-venue paper.

**H5. A presentation and competition culture from the first year.** [practice] (P) + [stated] (P)
- Her CV p. 2 has a section titled **"Additional Awards to my Team under my Leadership"**. It lists the Department of Computing Google Poster Competition (Kouyialis 2015, Baltean-Lugojan 2016, Olofsson 2018, as first- or second-year students), CPSE Industrial Consortium poster prizes, PSE@ResearchDayUK, the UK/Ireland SIAM poster prize, STEM for Britain in Parliament (Mistry and Olofsson 2019, Kronqvist 2021, Zhang 2025), and MSc/MEng thesis prizes.
- She judged the Google Poster Competition in 2015 and 2016 and sat on the Undergraduate Prize Committee in 2015 (College Service page).
- As an elected AIChE CAST Director, 2016–18 (CV p. 30) [stated]: "During my tenure, I (i) overhauled the Student Travel Award, (ii) created an online Poster Kiosk to increase poster session prestige, (iii) initiated the Software Tools & Implementations session at the annual meeting, and (iv) reworked the Student Presentation Award process."
- [inferred] Getting students in front of audiences early, and making student venues prestigious, is a deliberate habit at both group and community level.

**H6. Every paper gets code, a video and an announcement.** [stated] (P) + [practice] (P, partly verified)
- Stated:
  - CV p. 1, "Reproducibility & Accessibility": "My research team develops and maintains open-source code on GitHub, releases video presentations on YouTube, and announces new research on LinkedIn".
  - SciTalk, Mar 2024 (ASR): "my group makes YouTube videos for every research paper that we do".
- Practice, from the GitHub API, 2026-10-10:
  - The `cog-imperial` organisation has 33 public repositories. Several are described as "Repository for paper: …". Several were **forked from the student's own account** (`PoolingProblemDetection`, `hens`, `StdPooling-PolyAlgos`, `SDPCutSel-via-NN`, among others), so the student keeps authorship of the code.
  - Contributor counts show **the code is written by students and postdocs**: galini — Ceccon 547 commits; suspect — Ceccon 306; romodel — Wiebe 225 (Misener 1); GPdoemd — Olofsson 293; entmoot — 333 by `spiralulam` (identity not checked), Thebelt 245, Boyne 52; OMLT — Jalving 86, Ceccon 85, Laird 75, Zhang 41, …, Misener 21.
- Videos (CogImperial YouTube RSS, latest 15 uploads): students present their own papers under their own names, e.g. "Jose Folch: SnAKe …" (2022-10-13), "Alexander Thebelt: Tree ensemble kernels …" (2022-10-18), "Shiqiang Zhang: Optimizing over trained GNNs via symmetry breaking" (2023-11-01). The **latest upload is 2024-11-04** (see Contradictions).
- Earlier theses carry the habit into their front matter. Ceccon 2021, Wiebe 2021 and Olofsson 2020 have an "Open-Source Software" section, and Baltean-Lugojan 2019 gives a "Code:" link per paper. Later theses in my sample do not, so this is a 2019–2021 cluster, not a fixed rule.

**H7. She writes the news about her students.** [practice] (P)
Imperial News lists three articles with "Ruth Misener" as author:
- "Department of Computing researchers selected to present research in Parliament" (21 Feb 2019; Mistry and Olofsson). She quotes the BASF collaborator and co-supervisor praising each student. Lee on Mistry: "the success of our project is due in large part to his strong grasp of complex concepts across different fields and the creativity with which he combined different approaches."
- "Department of Computing MSc student honoured for her joint work with Royal Mail" (15 May 2019; Natasha Page).
- "Imperial researchers publish 17 papers at the NeurIPS 2022 conference" (13 Oct 2022). It lists papers by all Imperial departments, not only her group.

**H8. Equality, diversity and visibility roles.** [practice] (P) + [stated] (P, ASR)
- Roles: Staff Ambassador for Women, Department of Computing (2022–, joint with Toni); EDI committee 2017–20; panel chair at ACM-W UK Inspire 2015; speed-mentoring for AnitaB.org 2018; WISDOM panellist at EURO 2021; mentor, RAEng Research Fellowship Access Mentoring Programme 2023 (Service pages; CV pp. 30–31).
- Inaugural lecture (ASR), on female colleagues as "best observed solutions": "how these people are is roughly along the lines of be better. You have to be as good as we are. Um, because otherwise you're a letdown. And they are very, very intense. Um, and they, uh, make me be better a lot."

---

## 4. What students say they learned from her (theme table)

Counts are the number of the 11 advisee theses whose acknowledgements contain the theme. All entries are [observed] (S). Page references are as in §2–§3.

| Theme | Theses (n) | Representative verbatim wording |
|---|---|---|
| Pragmatism, staying grounded, "fail fast" | 2 | Baltean-Lugojan: "coupled with a pragmatic ’aim high but fail fast’ approach to research, pushed me to take on challenges, grow and persevere through many ups-and-downs" (PDF p. 4). Mistry: "Dr Misener’s pragmatic approach to conducting research ensured that I remained grounded" (PDF p. 7) |
| Strategy and hard work, not luck | 2 | Ceccon: "She taught me that good research is not the result of luck, but of hard work and proper strategy." (PDF p. 4). Kouyialis: "My advisor has shown me that career success takes hard work, dedication and the willingness to take personal responsibility for your actions." (PDF p. 5) |
| Rigorous standards | 1 (+1 about a postdoc) | Thebelt: "not only taught me how to navigate scientific research but also the importance of maintaining rigorous standards in our work" (PDF p. 6). Mistry, about postdoc Campos: "ensuring that my intuition was backed by rigour" |
| Writing, presenting, communicating | 4 | Olofsson: "for helping me improve as a researcher and writer of scientific texts" (PDF p. 5). Baltean-Lugojan: "how to critically assess and present work and vision" (PDF p. 4). Kouyialis: "be able to command an audience as well as she does" (PDF p. 5). Odgers: "how to be an effective researcher, collaborator, and communicator" (PDF p. 5) |
| Engaging with the research community | 1 | Baltean-Lugojan: "how to constructively engage with your research community" (PDF p. 4) |
| Time and availability | 3 | Mistry: "her constant willingness to make time in her schedule ensured that I was always supported" (PDF p. 7). Kouyialis: "Her willingness to invest time" (PDF p. 5). Folch: "the frequent advice, help, friendship, and also patience whenever I needed it" (PDF p. 6) |
| Belief in the student; pushing | 3 | Kouyialis: "believed in my abilities and pushed me to reach my full potential and exceed myself" (PDF p. 5). Olofsson: "I am grateful for her belief in me" (PDF p. 5). Baltean-Lugojan: "pushed me to take on challenges" (PDF p. 4) |
| Care and well-being | 4 | Thebelt: "Professor Misener’s kindness and genuine concern for the well-being of everyone in our group, especially during difficult times" (PDF p. 6). Olofsson: "goes to great lengths to look after her students" (PDF p. 5). Odgers: "a lot of life was happening and I truly could not have asked for better support from you both" (PDF p. 5). Wiebe: "an incredibly supportive mentor and always having words of advice for me" (PDF p. 5) |
| Humour | 1 | Mistry: "her sense of humour ensured that I was always smiling" (PDF p. 7) |
| Keeping on track | 2 | Sedgwick: "always keeping me on track". Zhang: "because Ruth asked me to submit my thesis :)" |
| Freedom and opportunities | 3 | Ceccon, Zhang, Folch (S8) |
| Skills beyond academia | 3 | Olofsson, Baltean-Lugojan, Ceccon (S10) |
| She enjoys supervising | 1 | Kouyialis: "I have learned that what she loves most about her job is working with her students." (PDF p. 5) |

[inferred] No theme is dominant. Care and well-being, and writing and communication, are each named in 4 of 11 theses. A practical-yet-ambitious stance ("aim high but fail fast", "pragmatic", "proper strategy", "hard work") recurs in 4.

The phrase "fail fast" also appears in her own mouth, about primal heuristics, not about research management. NMPC 2021 (ASR): "what i have learned from these jedi masters is that you ought to fail fast". [stated] (P) Whether the student's phrase echoes a stated lab motto **cannot be determined** from the sources.

---

## 5. Tacit knowledge: what the students know that the papers never say

All items below are secondary except where marked, and are labelled by who says them.

- **T1. Your daily technical mentor is often a postdoc or fellow, not the PI.** According to Mistry ("my postdoctoral mentors"), Kouyialis (Letsios, Campos), Thebelt (Kronqvist, Tsay), Folch ("third supervisor"), Odgers (Kappatou as "role model") and Zhang (Campos "mentor for every paper", Tsay "unofficial supervisor"). Source: thesis acknowledgements 2018–2025, §2 S4. (S)
- **T2. Industrial partners are co-advisors you present to repeatedly; visits to the company are part of the PhD.** According to Wiebe (Schlumberger office in Cambridge; "detailed, immediate and thoughtful feedback"), Folch (visit to BASF), Odgers (trips to Lilly), Olofsson (hosted at Bayer AG) and Zhang ("Every meeting with you was insightful"). Source: theses; Imperial News 2 Jun 2021. (S)
- **T3. Projects and code pass between student generations.**
  - Thebelt (PDF p. 6) thanks Mistry, "who not only helped me integrate into the project". Both were BASF-funded tree-ensemble projects: Mistry et al., "Mixed-Integer Convex Nonlinear Optimization with Gradient-Boosted Trees Embedded", INFORMS J. Comput. 33:1103–1119, DOI 10.1287/ijoc.2020.0993; Thebelt et al., "ENTMOOT: A framework for optimization over ensemble tree models", Comput. Chem. Eng. 151:107343, DOI 10.1016/j.compchemeng.2021.107343.
  - The next BASF+StatML student, Boyne, has 52 commits to entmoot (GitHub API).
  - Misener (inaugural, ASR): "the reason my slide is exploding with people is then what happened is that a lot of people got excited about Mitten's work."
  - (S) + [practice] (P)
- **T4. Onboarding is peer-led.**
  - Zhang (PDF p. 7), about Thebelt: "the first person I met when I joined COG, you helped me get everything set up, answered every single question I had, and showed me what an outstanding PhD student is."
  - Thebelt (PDF p. 6): Ceccon and Olofsson "welcomed me on my first day in the office".
  - Ceccon (PDF p. 4) chose the group partly because of the people who helped with his MSc project: "Knowing I would work alongside such talented and approachable researchers was one of the deciding factors in joining the Computational Optimization Group."
  - (S)
- **T5. Turn the industrial case into a general open-source tool, a paper and a video.**
  - According to Imperial News, 2 Jun 2021, Wiebe "went through an iterative process of developing his theory, and applying it to Schlumberger’s needs" and then "realised that the tools he had developed for geothermal energy might also solve broader optimisation problems involving uncertainty". He released ROmodel and explained it on YouTube.
  - Records: Wiebe, Cecílio, Dunlop & Misener, "A robust approach to warped Gaussian process-constrained optimization", Math. Program. 196:805–839, DOI 10.1007/s10107-021-01762-8 (arXiv 2006.08222). Wiebe & Misener, "ROmodel: modeling robust optimization problems in Pyomo", Optim. Eng. 23:1873–1894, DOI 10.1007/s11081-021-09703-2 (arXiv 2105.08598).
  - The same arc runs Mistry/BASF → ENTMOOT → OMLT: Ceccon et al., "OMLT: Optimization & Machine Learning Toolkit", arXiv 2202.02414. Misener (inaugural, ASR): "we tried to make this real at BSF [BASF] and two we tried to make this real with respect to doing reasonable software engineering."
  - (S) + [practice] (P) + [stated] (P)
- **T6. Collaborations start informally.**
  - Misener: "pub buddies" (H2) [stated].
  - Zhang (PDF p. 8): "I never expected that some casual chats with Calvin and BASF colleagues would turn into a real project."
  - Misener on students bringing back the Uganda collaboration (S6) [stated].
  - (S)/(P)
- **T7. Problems are routed to the colleague best suited to them.** Misener, Imperial Business Partners panel, Feb/Mar 2021 (ASR): "when a new problem comes in uh we sort of figure out what are the components that the stakeholder needs" … "we then sort of try to deploy the individual problem to the person who is uh best suited to it". [stated] (P)
- **T8. Rehearse before conferences.** Weekly-seminar practice talks before AIChE and IFAC (H3). [practice] (P)
- **T9. Students may find that the supervisor's idea does not work, and the fix becomes their contribution.**
  - Misener, Manchester seminar, Jan 2025 (ASR): "the the PHD student came to me and was explaining to me you know this doesn't actually work". "I took a global optimization algorithm I turned it into a path-based algorithm but that's a local optimization algorithm … I should have understood this the way that um uh Jose fixed this is that he developed um something called uh Point deletion".
  - The SnAKe abstract (arXiv 2202.00060, read) says: "We show the method is robust to the choice of its single hyper-parameter and provide a parameter-free alternative." The paper body was not read.
  - [stated] (P)
- **T10. Push the mathematics as far as it goes before approximating.** Inaugural Q&A (ASR), attributing the habit to a current PhD student whose name the ASR renders as "Shung" (identity uncertain): "you sometimes you want to see how far you can get mathematically before we start making approximations". [stated] (P, ASR, attribution uncertain)
- **T11. The thesis is a deadline she enforces, gently.** Zhang: "Ruth asked me to submit my thesis :)". Sedgwick: "always keeping me on track". (S)
- **T12. Credit language.** In talks she names the student or fellow who led each piece (S7, H6). Manchester 2025 (ASR): "I'm presenting the work of three uh super smart uh PhD students if at any point I refer to my work I actually mean their work". [stated] (P)

What could **not** be recovered:

- how often she meets students one to one
- how drafts are reviewed and how many rounds
- how thesis topics are fixed
- what happens when a student struggles
- how authorship order is negotiated (only the outcome is visible, §6 C2)

---

## 6. Layer 6: credit, authorship and publicity

**C1. Stated norms.** [stated] (P)
- In talks, "if at any point I refer to my work I actually mean their work" (Manchester 2025, ASR). Also "our project was led by francesco chikon [Ceccon] and jordan chalving [Jalving] with the help of many of us other researchers" (OMLT introduction video, 2022, ASR).
- On awards, BCS, 11 Dec 2023: "I’m honoured to be recognised in this way and receiving this accolade is wonderful though it could only have been achieved through the support and collaboration of my excellent colleagues."
- The CV separates "primarily written by me" code from "code primarily written by my team" (L3).

**C2. Author order in the record.** [practice] (P, Crossref author lists checked 2026-10-10)
- **Usual pattern: the student or postdoc lead first, Misener last.**
  - Mistry & Misener, Comput. Chem. Eng. 94:1–17 (2016), DOI 10.1016/j.compchemeng.2016.07.001.
  - Ceccon, Kouyialis & Misener, AIChE J. 62:3085–3095 (2016), DOI 10.1002/aic.15308.
  - Baltean-Lugojan & Misener, DOI 10.1007/s10898-017-0577-y.
  - Folch, Zhang, Lee, Shafei, Walz, Tsay, van der Wilk, Misener (SnAKe).
  - Zhang, Feldmann, Sandfort, Mathea, Campos, Misener, "Limeade: Let integer molecular encoding aid", Comput. Chem. Eng. 199:109115 (2025), DOI 10.1016/j.compchemeng.2025.109115.
- **A group paper: postdoc lead first, four PhD students in alphabetical order, Misener last.** Letsios, Baltean-Lugojan, Ceccon, Mistry, Wiebe & Misener, "Approximation algorithms for process systems engineering", Comput. Chem. Eng. 132:106599 (2020), DOI 10.1016/j.compchemeng.2019.106599.
- **The venue's convention can win.** The Royal Mail conference paper is fully alphabetical: Bradley, Letsios, Misener & Page, "Approximating Bounded Job Start Scheduling with Application in Royal Mail Deliveries Under Uncertainty", LNCS (COCOA 2019) pp. 69–81, DOI 10.1007/978-3-030-36412-0_6. The journal version puts the postdoc lead first and the rest alphabetically: Letsios, Bradley, G, Misener & Page, J. Scheduling 24:237–258 (2021), DOI 10.1007/s10951-021-00678-7.
- **Undergraduate-supervised paper: the PhD student supervisors take the last positions after the PI.** Kampala paper, arXiv 2311.16625 (S6).
- **Exception from her postdoc years: she is first author with undergraduates as co-authors.** Misener, Allenby, Fuentes-Garí, Gupta, Wiggins, Panoskaltsis, Pistikopoulos & Mantalaris, "Stem cell biomanufacturing under uncertainty: A case study in optimizing red blood cell production", AIChE J. 64:3011–3022, DOI 10.1002/aic.16042. CV p. 27: "Thesis of KG & TW published in AIChE Journal" (see Contradictions for the reference number).

**C3. Student project theses become papers.** [practice] (P: CV pp. 26–27, verified DOIs)
- MEng → Comput. Chem. Eng. 2016 (Mistry).
- MSc → AIChE J. 2016 (Ceccon). The CV notes "Invited article for Tribute to Founders: Roger Sargent".
- MSc (Page) and MEng (Suraj G) → COCOA 2019 and J. Scheduling 2021.
- Undergraduate (Gupta, Wiggins) → AIChE J.
- Undergraduate and MEng (Stoddart, Shrack) → NeurIPS 2023 workshop (arXiv 2311.16625).
- She credits project students on the CV with the venue each thesis reached ("Thesis published in …").

**C4. Group-wide papers.** [practice] (P) + [inferred]
- Letsios et al. 2020 (C2) puts one postdoc and four PhD students on one paper.
- Thebelt, Wiebe, Kronqvist, Tsay & Misener, "Maximizing information from chemical engineering data sets: Applications to machine learning", Chem. Eng. Sci. 252:117469 (2022), DOI 10.1016/j.ces.2022.117469.
- [inferred] These read as cohort exercises (a survey or perspective in which each member writes a section). **No source describes how they were written.**

---

## 7. Failures, corrections, abandoned or reshaped work

**F1. A neural-network cut-selection paper with no peer-reviewed version found.** [practice] (P) + [inferred]
- Baltean-Lugojan, Bonami, Misener & Tramontani, "Scoring positive semidefinite cutting planes for quadratic optimization via trained neural networks", Optimization Online 2018/11/6943 (page checked: "Published: 2018/11/26"; a citation line dated November 2019).
- The 2019 thesis lists it as "Reviewed and resubmitted, Nov 2019" (PDF p. 6, printed p. v).
- Her Dec 2025 CV lists the work only under invited seminars (e.g. S26, Cardiff, 12/2019; CV p. 14). A Crossref title search on 2026-10-10 returned no match. DBLP returned a bot check and was not searched.
- [inferred] It apparently never appeared in a peer-reviewed venue. The cause (rejection or abandonment after the student left for industry) is **not documented**. The code survives as `cog-imperial/SDPCutSel-via-NN`, a fork, last pushed 2019-10-14.

**F2. A general solver preprint, published as a narrower pooling paper.** [practice] (P) + [inferred]
- The preprint: Ceccon, Baltean-Lugojan, Bynum, Li & Misener, "GALINI: An extensible mixed-integer quadratically-constrained optimization solver", Optimization Online 2021/01/8207 (page checked). Its abstract claims a general solver that "performs comparably to existing open source solvers".
- The peer-reviewed outcome is two-author and problem-specific: Ceccon & Misener, "Solving the pooling problem at scale with extensible solver GALINI", Comput. Chem. Eng. 159:107660 (2022), DOI 10.1016/j.compchemeng.2022.107660. The thesis abstract (PDF p. 3) reports results "comparable to or better than the best available commercial solver on dense instances" with the pooling extensions.
- [inferred] The general claim was not carried into a journal and the narrower, stronger claim was. The repository is not archived (last push 2026-02-05), but its history is almost entirely one student's (547 of 556 listed contributions).

**F3. A supervisor's idea that failed, caught by the student.** [stated] (P, ASR) — see T9. Misener: "I should have understood this."

**F4. She was wrong as a student, and says so.** [stated] (P) — L2 and L3: she objected to the large instance and to the solver promise. "He was right in the end."

**F5. The supervisor's own stated limits, offered to the audience.** [stated] (P, ASR, inaugural Q&A)
- "I have not seen at this point how the kind of mathematics that I do could sort of design the drugs. Um, but perhaps that's just I'm not imaginative enough."
- On generative AI: "I don't understand it well enough to know if one that that any of this work would how it would morph for change yet."

**F6. Which tools outlive their student.** [practice] (P) + [inferred]
- Single-student tools stop when the student leaves. Last pushes: GPdoemd 2019-03-15, pypopt 2021-05-05, suspect 2022-07-14, romodel 2022-11-11.
- Tools that span cohorts or institutions continue: OMLT 2026-07-09 (Imperial, CMU, Sandia), entmoot 2026-02-19 (BASF, Thebelt, Boyne).
- [inferred] For software, the group's continuity mechanism is the multi-generation or industrial partnership, not the individual PhD.

---

## 8. Era and resource context

| Period | Position and resources | Team | Supervision practice visible |
|---|---|---|---|
| 2007–2012 | PhD student, Princeton (Floudas). NSF Graduate Research Fellowship | — | Received: a demanding, application-first advisor (L1–L5). Co-supervised a Princeton undergraduate project with Floudas, 2011–12 (CV p. 27). Volunteer algebra instructor, Princeton Prison Teaching Initiative, 2010–12 (Teaching page) |
| 2012–2014 | RAEng Research Fellow, Imperial CPSE (Chemical Engineering; host Pistikopoulos) | Undergraduate and MSc projects co-supervised with Mantalaris, Pistikopoulos and Adjiman (CV p. 27) | Undergraduate theses → AIChE J. paper with her as first author (C2) |
| 2014–2017 | Lecturer (then Senior Lecturer) in Computing. Course leader for 70007 (from 2014) and 60016 (from 2016). RAEng fellowship to 2017 | First PhD students: Kouyialis 2014, Baltean-Lugojan and Mistry 2015, Olofsson and Ceccon 2016. Funding: EPSRC DTA, HiPEDS CDT, ModLife ITN. Postdocs on consortium grants (U², 2015–19) | Second supervisors from COG (Parpas, Huth). MEng/MSc → PhD pipeline from her courses. Poster competitions from year 1 |
| 2017–2022 | EPSRC Early Career Fellowship "GALINI", "Software development for novel engineering research; Includes 6 years postdoc funding; £984k (PI)" (CV p. 27). Professor by 2020 | Fellows Kronqvist and Tsay. Postdocs Letsios, Campos, Kappatou. BASF-funded students (Thebelt 2019), Schlumberger iCASE (Wiebe 2017), StatML CDT + BASF (Folch 2020), AI4Health CDT (Sedgwick 2019), Lilly Prosperity Partnership (Odgers 2020) | Postdoc and fellow mentoring layer (S4). Industrial co-advisors (S5). Software and video dissemination (H6). Turn towards ML and Bayesian optimisation |
| 2022–2027 | BASF/RAEng Research Chair. IConIC Prosperity Partnership with BASF (postdoc funding). Co-director of an EPSRC CDT (CCMI, 2024–2033) and of the AI for Chemistry hub (CV p. 28) | Zhang (Hans Rausing + BASF, 2021–25), Boyne (2023–), IConIC postdocs (2025–). Tsay now runs his own students in the same office | Students contribute code to the partner's open-source package (S5). Student-initiated collaborations (S6). COG-wide weekly seminar with practice talks (H3) |

Resource notes:
- No information on computing infrastructure, cluster use, or lab budget for student travel.
- Travel funding is visible only indirectly: Kouyialis credits EPSRC for "Attending major events and conferences" (PDF p. 6), and Zhang credits the Hans Rausing Scholarship and BASF for letting him travel "for academic conferences" (PDF p. 6).

---

## Contradictions (kept, not reconciled)

1. **Kouyialis's thesis title.** The homepage Alumni page and Spiral (10.25560/67897) give "Symmetry and Degeneracy in Nonconvex Optimisation Problems: Application to Heat Recovery Networks". Her CV (Dec 2025, p. 25) gives "Exploiting Symmetry in Mixed-Integer Nonlinear Optimisation".
2. **Olofsson's co-supervision.** The homepage says "Joint supervision with Dr Marc Deisenroth". Spiral lists only "Misener, Ruth" as advisor. Olofsson thanks Deisenroth for "continued support and supervision during my postgraduate studies".
3. **Alumni destinations differ between the homepage and the Dec 2025 CV.** Baltean-Lugojan: "Quantitative Researcher, Millennium" vs "Portfolio Manager at Eisler Capital". Ceccon: "Co-Founder, Auclantis" vs "Co-Founder, Apibara". Kouyialis: "Health & Life Sciences Solutions Lead, Dataiku" vs "Data Science Consultant at Dataiku". Probably different update dates; not resolved.
4. **Calvin Tsay's title.** Her Alumni page and CV: "Associate Professor, Department of Computing, Imperial College London". COG People page: "Assistant Professor and BASF/RAEng Senior Research Fellow".
5. **The reference for the undergraduate thesis paper.** CV p. 27: "Thesis of KG & TW published in AIChE Journal (J32), 2013". In the same CV's publication list, J32 is the 2018 Baltean-Lugojan JOGO paper. Gupta and Wiggins appear on J33 (AIChE J. 64:3011–3022; Crossref issue year 2017; CV year 2018).
6. **"Every research paper" gets a video vs the channel record.** She said in Mar 2024 (ASR): "my group makes YouTube videos for every research paper that we do". The CogImperial channel RSS shows no upload after 2024-11-04, so 2025 papers such as Limeade (DOI 10.1016/j.compchemeng.2025.109115) have no video **on that channel**. Videos elsewhere were not checked.
7. **Freedom vs keeping on track** (S8). Students report both "take my research where I wanted" and "always keeping me on track". This may be a tension rather than a contradiction; kept as reported.
8. **Lineage style** (L9). She describes a sharp, demanding advisor whose "belief in his students was inspiring". Her own students describe patience and adapting to the student. Both may be true; not reconciled.
9. **"Fail fast": method or management?** The student uses it for her research approach (Baltean-Lugojan). She uses it, in the sources found, for primal heuristics (NMPC 2021). No source links the two.

## Gaps (what I could not find)

- **Her own PhD thesis acknowledgements (X1).** The Princeton DataSpace ARK `ark:/88435/dsp015q47rn787` resolves behind a bot verification (HTTP 401, "Verification required"). I did not try to get around it. **Not read.**
- **First-hand accounts by postdocs and fellows** (Kronqvist, Tsay, Letsios, Campos, Kappatou, Qing). None found. They appear only through students' thanks and her statements.
- **No student blog, lab handbook, onboarding document, Festschrift or interview about her supervision.** Two WebSearch calls returned nothing relevant.
- **Imperial "Featured Academic: Dr Ruth Misener" profile (X2).** HTTP 404; the Wayback Machine returned HTTP 429. Not read.
- **AIChE profiles (X3, X4).** The CAST Outstanding Young Researcher Award 2020 blog and the AIChE CEP "35 Under 35" 2017 profile returned HTTP 403. Not read.
- **Three outreach videos (X5–X7)** listed on her Community Service page: RAEng 2017, AIChE Journal 2019, RAEng 2015. I retrieved captions, but they are multi-speaker montages with no speaker labels, so quotes cannot be attributed to her. **Not used.** The EURO 2021 "WISDOM" embed (X8) is a 54-second promotional clip; I found no words of hers in it.
- **DBLP (X9)** returned a bot check, so F1's status could not be cross-checked there.
- **Inaugural lecture slides** (the slide listing the PhD students, postdocs and fellows she thanks) were not seen. Only the ASR audio transcript was read, and it has transcription errors.
- **Not documented:**
  - one-to-one meeting cadence
  - draft-review practice
  - how thesis topics are assigned
  - how authorship is negotiated
  - how failing projects are stopped
  - the group's computing resources
- **Current students** (Boyne and others) have no theses yet. MSc and undergraduate students' views are available only through Page's quote in her article and the UROP news piece.
- **Collaboration-only Chemical Engineering theses** (Fuentes-Garí 2015, Savvopoulos 2018) were found on Spiral but not read; she was not their formal supervisor.

## Sources

Primary (relative to Misener):
- P1. Ruth Misener, homepage "Optimization Models, Algorithms, and Software", accessed 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/ — primary
- P2. Misener, "Research Team" and "Current Research Team" pages, accessed 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/research-group/ and …/current/ — primary
- P3. Misener, "Alumni & Completed Projects", accessed 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/research-group/completed/ — primary
- P4. Misener, "Teaching", accessed 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/teaching/ — primary
- P5. Misener, "College Service", accessed 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/service/college-service/ — primary
- P6. Misener, "Community Service", accessed 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/service/community-service/ — primary
- P7. Misener, "Professional Activities", accessed 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/professional-activities/ — primary
- P8. Misener, Curriculum vitae, 32 pp., "Updated December 3, 2025". http://www.doc.ic.ac.uk/~rmisener/Misener_CV.pdf — primary
- P9. Ruth Misener, "Christodoulos Achilleus Floudas", SIAG/OPT Views and News 24(1), Oct 2016, pp. 12–16. https://siagoptimization.github.io/assets/views/ViewsAndNews-24-1.pdf — primary
- P10. Ruth Misener, "Department of Computing researchers selected to present research in Parliament", Imperial News, 21 Feb 2019. https://www.imperial.ac.uk/news/190330/department-computing-researchers-selected-present-research/ — primary
- P11. Ruth Misener, "Department of Computing MSc student honoured for her joint work with Royal Mail", Imperial News, 15 May 2019. https://www.imperial.ac.uk/news/191227/department-computing-msc-student-honoured-joint/ — primary
- P12. Ruth Misener, "Imperial researchers publish 17 papers at the NeurIPS 2022 conference", Imperial News, 13 Oct 2022. https://www.imperial.ac.uk/news/240475/imperial-researchers-publish-17-papers-neurips/ — primary
- P13. Ruth Misener, inaugural lecture "Just relax, Or: How I’m bad at my own algorithmic advice.", Imperial College London, published 2023-03-13, includes the vote of thanks by E. N. Pistikopoulos. https://www.youtube.com/watch?v=dN860HNsAs0 ; ASR transcript at `references/sources/talks/2023-03-13-inaugural-lecture-just-relax-dN860HNsAs0.txt` (saved by a sibling agent); chapter metadata read from the watch page — primary (vote of thanks: secondary observer within it)
- P14. Misener, seminar on BASF collaboration, Manchester, Jan 2025, ASR transcript `talks/2025-01-manchester-autonomous-research-machines-2br7KspcQXk.txt` — primary
- P15. Misener, SciTalk on Bayesian optimisation and design of experiments, Mar 2024, ASR transcript `talks/2024-scitalk-bayesian-optimization-design-of-experiments-9aLOEJNOCho.txt` — primary
- P16. Misener, online seminar "machine learning needs mathematical optimization" (Sevilla), Apr 2021, ASR transcript `talks/2021-04-sevilla-partition-based-formulations-relu-UcNXm24uQjE.txt` — primary
- P17. Imperial Business Partners panel "Decision making under uncertainty", 2021, ASR transcript `talks/2021-03-12-imperial-panel-decision-making-under-uncertainty-Cbnfz00SHLg.txt` — primary
- P18. Misener, "Developing spatial branch & bound solvers", NMPC 2021, 2021-08-05, ASR transcript `talks/2021-08-05-nmpc2021-developing-spatial-branch-and-bound-solvers-Z5hbKPx9YDE.txt` — primary
- P19. Misener, "Introduction to OMLT", 2022-03-22, ASR transcript `talks/2022-03-22-introduction-to-omlt-8IpM42mSsWE.txt` — primary
- P20. Computational Optimisation Group website: home, Join us, People, Alumni, Events, accessed 2026-10-10. https://optimisation.doc.ic.ac.uk/ — primary (group record)
- P21. COG weekly seminar schedule (public Google Sheet linked from the Events page), CSV export, accessed 2026-10-10. https://docs.google.com/spreadsheets/d/1z7lhVcsIFM6_mGdn6Xz8OFQ0xSMkaY-7zBICGHHe9lI — primary (group record)
- P22. GitHub organisation cog-imperial: repository list, contributor statistics and push dates via the GitHub API, accessed 2026-10-10. https://github.com/cog-imperial — primary (practice)
- P23. OMLT pull request #91 "Support for max pooling layers" and its reviews, GitHub API, accessed 2026-10-10. https://github.com/cog-imperial/OMLT/pull/91 — primary (practice)
- P24. CogImperial YouTube channel RSS (latest 15 uploads), accessed 2026-10-10. https://www.youtube.com/feeds/videos.xml?channel_id=UCXRdjQRm9XfZj2c4XW1xpzg — primary (practice)
- P25. Spiral (Imperial repository) thesis records with advisor "Misener, Ruth", DSpace REST API, accessed 2026-10-10. https://spiral.imperial.ac.uk/ — primary (record)
- P26. Optimization Online preprint pages 2018/11/6943 and 2021/01/8207, accessed 2026-10-10. https://optimization-online.org/2018/11/6943/ ; https://optimization-online.org/2021/01/8207/ — primary (record)
- P27. Bibliographic verification: Crossref REST API (25 DOIs) and arXiv API (2202.02414, 2202.00060, 2006.08222, 1912.06862, 2105.08598, 2408.05040, 2311.16625), queried 2026-10-10 — primary (record)

Secondary:
- S1. Georgia Kouyialis, "Symmetry and degeneracy in nonconvex optimisation problems: Application to heat recovery networks", PhD thesis, Imperial, awarded 2019-02. DOI 10.25560/67897 — secondary
- S2. Radu Baltean-Lugojan, "Exploiting structure in nonconvex quadratic optimisation", PhD thesis, Imperial, 2019. DOI 10.25560/79281 — secondary
- S3. Miten Narendra Mistry, "Branching strategies for mixed-integer programs containing logical constraints and decomposable structure", PhD thesis, Imperial, 2020. DOI 10.25560/88099 — secondary
- S4. Simon Olofsson, "Gaussian processes for hybridisation of analytical and data-driven approaches for design of experiments", PhD thesis, Imperial, submitted Dec 2019 / revised May 2020. DOI 10.25560/85413 (acknowledgements read from page images) — secondary
- S5. Francesco Ceccon, "GALINI: an extensible solver for mixed-integer quadratically-constrained problems", PhD thesis, Imperial, 2021. DOI 10.25560/91504 — secondary
- S6. Johannes Wiebe, "Formulations, algorithms and software for robust optimisation", PhD thesis, Imperial, 2021. DOI 10.25560/92915 (acknowledgements read from page image) — secondary
- S7. Alexander Thebelt, "Sequential black-box optimization via global optimization of tree ensembles", PhD thesis, Imperial, 2023. DOI 10.25560/113203 — secondary
- S8. Ruby Sedgwick, "Bayesian design of experiments for biomolecular assay design", PhD thesis, Imperial, 2023. DOI 10.25560/131038 — secondary
- S9. Jose Pablo Folch, "Towards improving Bayesian optimisation for the physical sciences via long-term planning", PhD thesis, Imperial (Mathematics/StatML), 2024. DOI 10.25560/117358 — secondary
- S10. James Odgers, "Spectroscopy motivated probabilistic latent variable models", PhD thesis, Imperial, 2025. DOI 10.25560/121327 — secondary
- S11. Shiqiang Zhang, "Optimizing over trained graph neural networks: mixed-integer programming, symmetry-breaking, and applications", PhD thesis, Imperial, 2025. DOI 10.25560/121917 — secondary
- S12. Ahmed Idle, "Major contribution by Imperial undergraduate to open-source research software", Imperial News, 23 Nov 2022. https://www.imperial.ac.uk/news/241732/major-contribution-imperial-undergraduate-open-source-research/ — secondary (contains a primary Misener quote)
- S13. David Silverman, "Machine learning models to support chemical R&D recognised with Best Paper Award", Imperial News, 27 Aug 2024. https://www.imperial.ac.uk/news/255753/machine-learning-models-support-chemical-rd/ — secondary
- S14. Ahmed Idle, "Professor Ruth Misener honoured with 2023 BCS Roger Needham Award", Imperial News, 20 Dec 2023. https://www.imperial.ac.uk/news/250395/professor-ruth-misener-honoured-with-2023/ — secondary
- S15. BCS, "Professor Ruth Misener awarded the 2023 BCS Roger Needham Award", 11 Dec 2023. https://www.bcs.org/articles-opinion-and-research/professor-ruth-misener-awarded-the-2023-bcs-roger-needham-award/ — secondary
- S16. David Silverman, "Machine learning techniques from Imperial and BASF advance experimental design", Imperial News, 31 Oct 2022. https://www.imperial.ac.uk/news/241071/machine-learning-techniques-from-imperial-basf/ — secondary
- S17. Natasha Martineau, "New open-source software for making better decisions", Imperial News, 2 Jun 2021. https://www.imperial.ac.uk/news/222853/new-open-source-software-making-better-decisions/ — secondary
- S18. David Silverman, "Worldwide uncertainty a chance for more efficient and resilient decisions", Imperial News, 12 Mar 2021. https://www.imperial.ac.uk/news/216673/worldwide-uncertainty-chance-more-efficient-resilient/ — secondary
- S19. Imperial Enterprise, "Decision-making under uncertainty" (Imperial Stories long read), early 2021 (accompanies a 25 Feb 2021 event). https://www.imperial.ac.uk/stories/decision-making/ — secondary
- S20. Caroline Brogan, "Imperial scoops three new Royal Academy of Engineering research chairs", Imperial News, 24 Mar 2022. https://www.imperial.ac.uk/news/235034/imperial-scoops-three-royal-academy-engineering/ — secondary
- S21. David Silverman, "Imperial and BASF in major partnership to advance future of chemical production", Imperial News, 18 Jul 2022. https://www.imperial.ac.uk/news/238391/imperial-basf-major-partnership-advance-future/ — secondary
- S22. Royal Academy of Engineering, "New industry-academia partnerships announced to address major engineering challenges", 24 Mar 2022. https://raeng.org.uk/news/new-industry-academia-partnerships-announced-to-address-major-engineering-challenges — secondary
- S23. Wikipedia, "Ruth Misener", revision of 2026-09-01. https://en.wikipedia.org/wiki/Ruth_Misener — secondary (used only for the thesis ARK link)

Papers cited, each checked on Crossref or arXiv on 2026-10-10: DOIs 10.1007/s10898-012-9874-7; 10.1007/s10898-014-0166-2; 10.1007/s10898-017-0577-y; 10.1016/j.compchemeng.2016.07.001; 10.1002/aic.15308; 10.1002/aic.16042; 10.1007/978-3-030-36412-0_6; 10.1007/s10951-021-00678-7; 10.1016/j.compchemeng.2019.106599; 10.1016/j.ces.2022.117469; 10.1287/ijoc.2020.0993; 10.1016/j.compchemeng.2021.107343; 10.1007/s10107-021-01762-8; 10.1007/s11081-021-09703-2; 10.1016/j.compchemeng.2022.107660; 10.1007/s11081-020-09551-6; 10.1007/978-3-030-78230-6_19; 10.52202/068431-2553; 10.52202/068431-2711; 10.1016/j.compchemeng.2023.108194; 10.1016/j.compchemeng.2025.109115. arXiv 2202.02414; 2202.00060; 2006.08222; 2105.08598; 1912.06862; 2408.05040; 2311.16625. Optimization Online 2018/11/6943 and 2021/01/8207.

Attempted but unreadable or unusable (see Gaps): X1 Princeton DataSpace thesis (bot check); X2 Imperial "Featured Academic" page (404; Wayback 429); X3 AIChE CAST award blog (403); X4 AIChE CEP 35 Under 35 (403); X5 RAEng video 2gYp1nm6D3M; X6 AIChE Journal video I1dPxAj6-fg; X7 RAEng video fFW1wWgsSNY; X8 EURO 2021 WISDOM clip 4da8PA2Y8Zw; X9 DBLP search (bot check).
