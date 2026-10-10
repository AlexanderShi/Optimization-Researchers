# 06 · Research trajectory: timeline, lineage, turns and their triggers, latest activity

> **Researcher**: Ignacio E. Grossmann (born 1949, Mexico City), Rudolph R. and Florence Dean University Professor of Chemical Engineering, Carnegie Mellon University (CMU); member and former director of the Center for Advanced Process Decision-making (CAPD). DBLP 31/5106 · Google Scholar `fiZryxEAAAAJ` · ORCID 0000-0002-7210-084X.
> **Dimension**: research agent 06 of 06, research trajectory (nuwa research-craft Phase 1; framework §二, agent 6: full academic timeline, advisor and student lineage, direction changes and their reasons, the last 12 months).
> **Research date**: 2026-10-10
> **Sources consulted**: 45 numbered under "Sources" (S1–S45): 24 primary, 19 secondary, 1 search log, 1 page that would not load. In addition, 93 publication identifiers (DOIs, arXiv ids, KiltHub DOIs) were checked by me on 2026-10-10 with the Crossref, DataCite and arXiv APIs; they are listed under "Papers cited and checked" (P1–P93). WebSearch: 2 of the 4 allowed calls used.
> **Local corpus**: no user-supplied material exists for this member. `references/sources/talks/` already held three caption transcripts saved earlier in this workflow run by agents 02 and 04 (2014 CMU video, 2024 interview, 2025 Royal Academy lecture). They are Grossmann's own words and are used here as primary, caption-derived evidence, **not** as user-supplied material. I added two transcripts to `talks/` (CAPEC 2014 lecture; PSE-2015 plenary). `references/sources/private/` was not opened.
> **Relation to the sibling notes**: 01 (publications), 02 (stated method) and 04 (mentorship) were read first. Where I rely on a finding of theirs that I did not re-check, I write "see 01/02/04". Every identifier and quotation in this file was re-checked by me in this run.
> **Tags**: [stated] his own words (speeches, interviews, slides he made, single-author texts; co-authored texts are marked "joint") · [practice] the record (papers, grants, software, appointments, author lists) · [observed] what others wrote about him · [inferred] my reading. **P** = primary, **S** = secondary.
> **Quoting**: verbatim. Caption quotes reproduce YouTube automatic captions exactly, errors included, with the start time [h:mm:ss] of the ~30 s block (Spanish lecture: ~60 s; "+" = the quote runs into the next block); glosses in parentheses ("ASR: ..."). Spanish quotes are followed by my translation ("tr."). Slide quotes come from `pdftotext` of his slide PDFs; the 1994 CAST-award slides are a scan, which I transcribed from the page images ("transcribed from scan"; " / " marks a line break on the slide). Every quotation, except the scan transcriptions, my translations and titles of papers or grants, was matched by script against the downloaded text on 2026-10-10 (curly apostrophes normalized to straight ones; "..." marks an elision).

---

## 0. The trajectory in one page [inferred, from §1–§8]

1. **One tool, a widening scale.** From 1977 to 2026 the constant is mixed-integer optimization, later generalized disjunctive programming (GDP). What changes is the size of the system the tool is pointed at: heat-exchanger network and single plant (1970s) → flowsheet and process network (1980s) → batch-plant schedules and production plans (1985–2010) → enterprise and supply chain (2003–) → energy systems and regional infrastructure (2009–) → decarbonization and CO2 logistics (about 2019–). He drew the same picture himself, in 2014 and again in 2019, as three arrows with named "drivers" (§3.1).
2. **Turns are triggered from outside the algorithm.** A new tool or computer (a MIP code at the Mexican Petroleum Institute, 1977–79; GAMS and the Cornell supercomputer, 1986–87; Pyomo and Julia, 2016–23), a person or place (Balas and Hooker at CMU → logic and GDP; Morari in 1980 → flexibility and resiliency; western Pennsylvania → shale gas), an industrial partner (Mobil/ExxonMobil, Dow, Praxair/Linde, EQT, Total, Shell, Aurubis), or his own reading of the field (the 2004 judgment that PSE's sustainability work was "rather timid"; the 2014 "pendulum" from bio and nano toward energy). Rejection and resistance did not change his direction; he says they hardened it (§3, §6).
3. **Early on algorithms, with or after the wave on applications.** He entered mixed-integer synthesis (1980), outer approximation (1983–86), LP/NLP-based branch and bound (1991–92) and GDP (1991–94) before they were accepted. He entered sustainability, shale gas and machine learning with or after the field (§4).
4. **Exits are quiet.** Metabolic networks (2000–03) and hybrid MILP/constraint programming (1999–2004) end without an announcement; shale-gas titles stop after 2023. His only stated rule for this is on his 2014 and 2019 "Lessons Learned" slides: "Be strategic: concentrate on few areas", with Porter's "The essence of strategy is choosing what not to do." (§3, §6)
5. **Agendas are written down years ahead.** The 1994 CAST-award slides list five research challenges. Four of them (logic, integration of design-planning-scheduling-control, uncertainty, large-scale solution) became his 1995–2015 program. The fifth, global optimization of mixed-integer differential-algebraic models, reappears as an open direction in his 2026 EJOR review (§5).
6. **The last twelve months** (Oct 2025 – Oct 2026): output continues at the pre-retirement rate, almost always as last author on co-advised or visitor-led papers (power-system reliability, refinery electrification, CO2 capture and storage logistics, industrial gases, copper, wind farms, pipelines), plus machine-learning and finance excursions through a student whose papers are co-authored with Carl Laird. Honours: Royal Academy of Sciences of Spain (lecture 16 Sep 2025), International Fellow of the Royal Academy of Engineering (announced 8 Oct 2026), 2026 INFORMS Saul Gass Expository Writing Award (to be presented Nov 2026) (§8).

---

## 1. Dated academic timeline

| Date | Event | Tag | Source |
|---|---|---|---|
| 1949 | Born in Mexico City to Swiss parents (father Donat, mother Marie Louise) | [stated] P; [observed] S | S1 [0:02:14]; S27 p. 1; S7 p. 27 |
| c. 1968 | Wanted to study mathematics; his father argued that "the best you can hope for is to be a teacher", so he chose chemical engineering. Chose the Universidad Iberoamericana (Ibero) because the 1968 Tlatelolco massacre was followed by a nine-month strike at UNAM | [stated] P (caption) | S1 [0:12:03]–[0:14:07] |
| 1973–74 | BS chemical engineering, Ibero (1974). Undergraduate thesis at the Mexican Petroleum Institute (IMP), supervised by Julián Castellanos: "Simulation model of multipass exchanger for condensation of multicomponent mixtures with noncondensible gases"; first paper 1974 (in Spanish, *Rev. Inst. Mex. Ing. Quím.* 15(5), 58; no DOI; not checked) | [stated] P | S6 p. 3; S7 p. 3; S13 |
| summer 1974 – Nov 1977 | Imperial College London on a British Council scholarship. MSc 1975, PhD 1977 with Roger W. H. Sargent; thesis "Problems in the Optimum Design of Chemical Plants". He came for an MSc; Sargent and a German friend talked him into the PhD | [stated] P | S1 [0:23:26]–[0:25:34]; S6 p. 4; S13 |
| 1977 | Marries Blanca Espinal (from Navarra); they move to Mexico | [observed] S | S27 p. 5 |
| late 1977 – Jan 1979 | Leads the Optimization Group at IMP and teaches graduate courses at Ibero. First hands-on access to a mixed-integer programming code (UNIVAC FMPS) | [stated] P; [observed] S | S1 [0:34:25]–[0:36:00]; S10; S27 p. 1 |
| 1978 | CMU job interview ("Carnegie Mellon interview slides (1978)"). He had met Art Westerberg "in Swansea at 4th IChemE Research Mtg."; the offer came mid-year, and the start waited for the year of service in Mexico required by the British Council | [stated] P | S6 pp. 4–5; S1 [0:38:06]–[0:39:10] |
| 1 Feb 1979 | Starts at CMU as assistant professor ("Started February, 1, 1979"), inside the Design Research Center (DRC) | [stated] P; [observed] S | S7 p. 5; S26; S25 |
| 1980 | First NSF grant as PI, on flexible plant design (CPE-7926398, from 15 Aug 1980). Meets Manfred Morari on the way to the 1st FOCAPD meeting at Henniker | [practice] P; [stated, joint] P | S23; S20 p. 2 |
| 1983 | Associate professor. DRC report "Mixed-integer programming: is it a useful tool in process synthesis?" (July 1983; presented at the AIChE Diamond Jubilee meeting, Nov 1983) | [observed] S; [stated] P | S26; S14 |
| 1984 | NSF Presidential Young Investigator award (CPE-8351237, 1984–89, "Optimal Synthesis of Integrated Chemical Processes"). His first CMU PhDs have graduated: Halemane and Papoulias (1982), Swaney (1983), Duran (1984) | [practice] P | S23; S7 p. 19 |
| 1985–86 | CAPD founded (1985 in CEE 2019; 1986 on his own 2019 slide and on the CAPD page). NSF funds the Engineering Design Research Center (EDRC), $21M for eleven years (1986) | see Contradictions | S27 p. 4; S7 p. 5; S25 |
| 1986 | Full professor. Outer-approximation paper with Marco Duran, *Math. Program.* 36(3):307–339 | [observed] S; [practice] | S26; P8 |
| 1986–87 | Mary Upson Visiting Professor at Cornell. DICOPT is written there with Gary Kocis on the Cornell Theory Center's IBM 3090, interfaced to GAMS with the World Bank GAMS team | [stated, joint] P | S15 p. 3 |
| 1986 or 1988 → | Director of the EDRC Synthesis Laboratory (start year differs between sources) | [observed] S | S25; S26 |
| 1989 | Co-chair, FOCAPD 1989. NSF grant "Planning and Scheduling of Multiproduct Continuous Processes" (8908735) | [stated] P; [practice] P | S10; S23 |
| 1990 | Dean Professorship | [observed] S | S27 p. 2 |
| 1994 | AIChE CAST Computing in Chemical Engineering Award (award slides: S8). Department Head, 1994 to the end of 2002 | [stated] P; [observed] S | S8; S10; S25 |
| 1997 | Textbook *Systematic Methods of Chemical Process Design* with Biegler and Westerberg; AIChE Walker Award; with Tepper, a minor in manufacturing management | [stated] P; [observed] S | S10; S25 |
| 1999 / spring 2000 | Mexican Academy of Engineering (1999); US National Academy of Engineering ("last spring" in a May 2001 article, i.e. 2000) | [observed] S | S26 |
| 2001 | University Professor, CMU's highest academic title; chairs Dow Chemical's Technical Advisory Board of Engineering Sciences | [observed] S | S26 |
| 2003 | INFORMS Computing Society Prize ("Ignacio Grossman", sic); chairs FOCAPO 2003 ("co-chair" in his biosketch) | [practice] S; [stated] P | S36; S10; S25 |
| 2003–04 | Fulbright Senior Lectureship at the Universidad de Cantabria, Santander, right after the headship; writes "Challenges in the new millennium" there | [stated] P | S18 pp. 1, 13 |
| c. 2004–05 | Starts the CAPD Enterprise-wide Optimization (EWO) interest group ("About 15 years ago" in 2019); EWO perspective in *AIChE J.* (2005); CAPD director 2005–2015 | [observed] S; [practice] | S27 p. 4; S19; S25 |
| 2005, 2008, 2011 | Co-organizes Pan-American Advanced Studies Institutes (Iguazú 2005; Mar del Plata 2008, whose NSF award title lists sustainability, energy, biosystems, multi-scale design and enterprise-wide optimization; 2011 energy and sustainability) | [practice] P; [observed] S | S23; S27 p. 4 |
| 2007–09 | AIChE Director; chairs the AIChE International Committee | [observed] S | S27 p. 5 |
| 2008 | CMU–IBM cyberinfrastructure for MINLP (NSF 0750826, $1.21M, 2008–13; minlp.org); named one of AIChE's "Hundred Chemical Engineers of the Modern Era" | [practice] P; [stated] P | S23; S10 |
| 2009; 2011 | AIChE Warren K. Lewis Award (2009); AIChE Research Excellence in Sustainable Engineering Award (2011) | [stated] P | S10 |
| 17 Nov 2014 | 65th-birthday sessions at the AIChE Annual Meeting, Atlanta; his talk "Reflections on 35 Years in Process Systems Engineering Research". *Comput. Chem. Eng.* tribute by Floudas and Pistikopoulos (vol. 72, 2015) | [stated] P; [observed] | S6; P56 |
| 2015 | First recipient of the IChemE Sargent Medal; Carathéodory Prize (International Society of Global Optimization); Sahinidis succeeds him as CAPD director | [stated] P; [observed] S | S13; S27 p. 3; S25 |
| 2017 | ETH Zürich Chemical Engineering Medal; EFCE CAPE Working Party long-term achievement award. Start of his last NSF award as PI (GOALI with Praxair, 2017–21) | [stated] P; [practice] P | S10; S23 |
| 11 Nov 2019 | 70th-birthday sessions, AIChE Annual Meeting, Orlando; talk "Reflections on 40 Years in Process Systems Engineering Research". 2019: AIChE Founders Award; honorary doctorate from Alicante, his seventh | [stated] P; [observed] S | S7; S10; S27 p. 4 |
| 2020–21 | Sahinidis leaves CMU for Georgia Tech (2020). "Carl Laird succeeds Ignacio Grossmann as director of the CAPD" (2021). Textbook *Advanced Optimization for Process Systems Engineering* (Cambridge, 2021) | [observed] S; [practice] | S25; P64 |
| 1 Sep 2023 | Phased retirement at 50% ("starting September the first I've actually taken what is called face retirement meaning 50% of the time"; ASR: phased). The year is inferred from the interview date (recorded after Thanksgiving 2023, published Feb 2024) | [stated] P (caption); year [inferred] | S1 [1:30:18] |
| 2024 | John M. Prausnitz AIChE Institute Lecturer | [stated] P | S10; S13 |
| 2025 | Biegler named CAPD director. Foreign Academic of the Royal Academy of Exact, Physical and Natural Sciences of Spain; admission lecture 16 Sep 2025 | [observed] S; [stated] P | S25; S2; S13 |
| 25 Nov 2025 | CMU announces the Howard Rosenbrock Prize (best 2024 paper in *Optimization and Engineering*: Kakkad, Grossmann et al.) | [observed] S | S30; S31 |
| 17–21 Aug 2026 | Keynote at IEEE CASE 2026, Shenyang: "Challenges in the Application of Mathematical Programming Approaches to Industrial Enterprise-wide Optimization" | [stated] P (abstract) | S24 |
| 8 Oct 2026 | Elected International Fellow of the Royal Academy of Engineering (UK); roll-signing ceremony on 19 October | [observed] S | S28; S29 |
| Nov 2026 (scheduled) | 2026 INFORMS Saul Gass Award for Expository Writing, to be presented at the INFORMS Annual Meeting in San Francisco. Only the CMU page says so; the INFORMS award page still lists the 2025 winner | [observed] S | S13; S35 |

Honorary doctorates (nine; most years not in the sources): Åbo Akademi, Maribor, TU Dortmund, Cantabria, Kazan National Research Technological University, Universidad Nacional del Litoral, Alicante (2019), RWTH Aachen, Universidad Nacional del Sur (S10, S13).

---

## 2. Lineage

### 2.1 Ancestry and the teachers he names

- **Mathematics Genealogy Project chain** [practice, S37]: John William Hinchley and William Arthur Bone → Dudley Maurice Newitt (PhD University of London 1924) → Roger W. H. Sargent (PhD Imperial College 1954; MSC 80, classical thermodynamics) → Ignacio E. Grossmann (PhD University of London 1977; MSC 90, operations research and mathematical programming). The subject codes record the turn his advisor made: Grossmann says Sargent's own PhD thesis was experimental ("he had not one not one equation") and that Sargent turned to optimization while working in France ("he started to read about you know mathematics"; both caption S1 [0:28:08]).
- **The CMU cluster was a Sargent cluster** [practice S37; observed S25]: Sargent's other MGP students are Arthur Westerberg (1964), B. Erik Ydstie (1982) and Constantinos Pantelides (1985). Westerberg joined CMU in 1976 and recruited Grossmann; Ydstie joined in 1992. Pantelides co-authored the State-Task Network paper whose rejections Grossmann tells as a lesson (§6). [inferred] Grossmann's move to Pittsburgh ran through his advisor's academic family.
- **What he inherited from Sargent** [stated, caption S1]: exposure to numerical optimization ("I was able to attend several meetings with people like Mike Powell Roger Fletcher", [0:27:38]); Sargent's 1967 vision paper "Integrated design and optimization of processes" (cited by him in S1 [0:26:04] and S2 [0:16:00]; not checked); and talk of mixed-integer methods before any code was available to him (§3.2, T2). He co-wrote a 2016 *AIChE J.* tribute to Sargent (P57; not read).
- **Teachers he credits at Ibero** [stated, S2 [0:13:01]; S6 p. 3]: Luis Vergara (advanced calculus), Alejandro Purón de la Borbolla (transport phenomena), Julián Castellanos (thesis). He also credits Dale Rudd's 1968 book on process engineering strategy; in 2025 he summarizes its three parts as creating and evaluating alternatives (synthesis), optimization, and engineering under uncertainty (S2 [0:17:01]; book not checked). [inferred] These are the three subjects of his three PhD papers (heat-exchanger synthesis, optimum design, design under uncertainty) and, later, of three of his five research lines (§2.2).
- **Egon Balas** is the "Source inspiration" for the move from MINLP to GDP (S6 p. 6; S7 p. 6, where Balas is dated 1922–2019). He sat in on Balas's integer-programming course after joining CMU ("after I joined car Millan I actually sat into his course on inter programming", caption S1 [0:41:45]; see 04 §B.1).

### 2.2 Descendants

- **How many** (see Contradictions): 68 PhD and 34 MS (CMU bio 2026; RAEng release Oct 2026), 68 PhD and 37 MS (his group's biosketch), 69 PhD theses and 40 master's (introduction at the Spanish Academy, Sep 2025), 65 PhD and 24 MS (his own 2019 slide). The Mathematics Genealogy Project lists only 8 students and 80 descendants (S37).
- **MGP-listed students** (S37): Floudas (1986; 9 descendants), Sahinidis (1990; 55 descendants), Varvarezos (1994), Türkay (1996; 8), Agarwal (2006), Kamath (2012), van Elzakker (2013, TU Eindhoven), Hongyu Zhang (2024, NTNU, third advisor after Tomasgard and Knudsen; their joint 2025 *EJOR* paper is P77).
- **Grandchildren who returned to his programs** [practice S37, S25; inferred link]: Floudas's MGP students include Claire Adjiman (1998), Costas Maranas (1995) and Chrysanthos Gounaris (2008). Gounaris joined CMU in 2013 and in 2026 leads the CAPD Enterprise-wide Optimization interest group, the program Grossmann started in about 2004. So the EWO program is now run by his academic grandson.
- **Inside this MINLP team**: Sahinidis is his student (MGP). Misener is listed in team.json as Floudas's PhD student, which would make her an academic granddaughter; MGP has no record for her, and I did not verify the link.
- **His own map of his career is a set of student lineages** [stated, P]. Both "Reflections" talks (S6 pp. 9–13; S7 pp. 9–13) list five research lines, each as a sequence of theses with the year:
  - I. Mixed-integer nonlinear programming: Duran (1984, outer approximation) → Kocis (1988) → Raman (1992, linear GDP) → Quesada (1993, LP/NLP-based branch and bound) → Varvarezos (1994) → Türkay (1996, logic-based OA) → Zamora (1997, global optimization) → Jain (1999, MILP and constraint programming) → Vecchietti (2000, LOGMIP) → Lee (2002, nonlinear GDP) → Agrawal (2006) → Sawaya (2006) → Ruiz (2011) → Trespalacios (2015) → Bernal (2021, conic GDP; 2019 slide only).
  - II. Process synthesis and energy systems: Papoulias (1982) → … → Yee (1990, P16) → … → Karuppiah (2007, water networks) → Kamath (2012) → Yang (2014, shale-gas water) → Drouven (2017) → Lara (2019, power planning) → Q. Chen (2020, software).
  - III. Batch and continuous scheduling: Vaselenak (1985) → … → Maravelias (2004) → Mouret (2010) → van Elzakker (2013) → Hubbs (reinforcement learning, dated 2022 on the 2019 slide).
  - IV. Planning and supply chain: Sahinidis (1990) → … → You (2009) → Garcia-Herreros (2016) → Q. Zhang (2016) → Brunaud (2019) → Perez (2022).
  - V. Design and planning under uncertainty: Halemane (1982) → Swaney (1983) → Pistikopoulos (1988) → … → Goel and Tarhan (2005) → Calfa (2015) → Apap (2016) → Ye (2020) → C. Li (2021).
  - Under the heading "Other", a single entry: "Optimization Models for Metabolic Networks: Soumitra Gosh(2006)" (S7 p. 13).
  - [inferred] He narrates his trajectory as lineages of students, one thesis per step. Topics enter his record when a student is assigned and leave when no successor is.
- **Placement in academia**: "16 of them have actually gone to academic positions" (caption S1 [1:18:11]+, 2024); "twelve" (CEE 2019); 13 roster lines (04). In 2024 he singles out Purdue hiring two of his students at once: "two of my students got hired by the same Department of same University by P University chemical engineering hired D Bernal and San Lee" (caption S1 [1:37:07]; ASR: Purdue, David Bernal, Can Li).

---

## 3. Turns and what triggered them

### 3.1 His own account: three arrows with named drivers (2014, repeated unchanged in 2019)

Three consecutive slides in both "Reflections" talks [stated, P; S6 pp. 6–8, S7 pp. 6–8]:

| Slide title | Driver (verbatim) | People pictured |
|---|---|---|
| "Evolution from Mixed-integer Nonlinear Programming (MINLP) to Generalized Disjunctive Programming (GDP)" | "Driver: Towards integration of symbolic logic" | Egon Balas ("Source inspiration") |
| "Evolution from Process Synthesis to Scheduling to Supply Chain" | "Drivers: From Design to Operations" | Rudd, Westerberg, Stephanopoulos, Rippin, Reklaitis |
| "Evolution from Process Flexibility to Stochastic Programming" | "Driver: From Deterministic to Probabilistic Approaches for Uncertainty" | Manfred Morari |

The opening "Goal in Research: Develop Mixed-integer Programming Techniques and apply to the Design and Operation of Chemical Processes" is the same on both. Between 2014 and 2019 only the student lists and the "Lessons Learned" changed (§6). [inferred] Over this period his self-account of the trajectory was fixed; the drivers he names are conceptual (logic, operations, probability), while the triggers documented below are mostly concrete (a code, a person, a company, a grant).

### 3.2 Turn by turn

Each turn gives: when; what triggered it, by type; the evidence; the records that mark the entry (identifiers under "Papers cited and checked").

**T1. The PhD agenda: three problems (1974–77).** Trigger: the advisor's program, a visitor, and the absence of tools.
- [stated, caption S1] Heat-exchanger networks were "like the travel and salesman problem for chemical engineers" ([0:31:16]); with no mixed-integer nonlinear programming available, he used implicit enumeration with Sargent's variable-metric projection NLP method ([0:31:48]).
- Multipurpose batch plants came from a visitor: "that was motivated to a large extent because we had the visit of Professor David trippin from the eth" ([0:32:19]; ASR: David Rippin, ETH Zürich).
- Uncertainty became the seed of his flexibility line: "my PhD work was also you know later on the foundation of research working" ([0:34:25]).
- Records: Grossmann & Sargent 1978 (P1, P2) and 1979 (P3). His first NSF grant (1980) is on flexible plant design (S23), so his first independent project continued PhD problem three. [practice]

**T2. To mixed-integer programming (1977–80).** Trigger: access to a tool.
- [stated, caption S1 [0:35:30]] "we would talk about the need for mixed IND digal programming but I never got my hands on a mix integer programming uh code" (ASR: mixed-integer). That changed at IMP, with UNIVAC's FMPS, "which we use for example to model the selection of uh you know processes in integrated networks" ([0:36:00]).
- Records: Grossmann & Santibanez 1980, "Applications of mixed-integer linear programming in process synthesis" (P4); Papoulias & Grossmann 1983 (P6). [practice]

**T3. From MILP to MINLP: outer approximation (1983–86).** Trigger: a limit of his own models, and an argument with the field.
- [stated, P, S14 p. 4] "In the recent past it is the first two approaches that have received most of the attention due to apparent limitations and failures with optimization techniques." (the two are heuristics and thermodynamic targets) and "It is the purpose of this paper to show that algorithmic methods can indeed play a very useful role in process synthesis."
- The limit that motivated MINLP [stated, S14 p. 24]: "rather than having to discretize these conditions at few selected points."
- The argument: a rejected MILP paper and a keynote titled "process synthesis a Utopia in mathematical programming or an adventure in heuristics" (caption S1 [0:47:29]). His reaction: "it was also motivation for us to try to see well can we prove him to be wrong" ([0:48:30]); the speaker's advice afterwards: "it's very clear that you like math maybe what you should do is to do research in process control" ([0:51:38]). Details in §6.
- Records: Duran & Grossmann 1986 (P8; erratum P9). For the anatomy of the algorithm see 01 SW1. [practice]

**T4. From algorithm to software (1986–90).** Trigger: a move (sabbatical) and new infrastructure.
- [stated, joint, S15 p. 3] "This work was performed at Cornell University in 1986-1987 while Ignacio Grossmann was the Mary Upson Visiting Professor", with Gary Kocis as a visiting scholar there. The report runs DICOPT on the Cornell Theory Center's IBM 3090 and thanks the World Bank GAMS team (Nielsen, Brooke, Meeraus).
- Records: Kocis & Grossmann 1989 (P13); Viswanathan & Grossmann 1990 (P15). From then on each major method gets a code in the modeling system of the day: LOGMIP (1999), Bonmin (P38, 2008), Pyomo.GDP (P63, 2022); see 01 §1.8. [practice]

**T5. From MINLP to logic and GDP (1990–2000).** Trigger: people and a place, plus a modeling failure.
- [stated, caption S1 [0:56:52]] "we had a very nice a sort of research effort in engineering design that was multi-disciplinary and as part of that professor John hooker was part of that and he was you know very much interested in logic", and a student, Ramesh Raman. The EDRC (from 1986) is that multidisciplinary effort; Grossmann directed its Synthesis Laboratory (S25, S26).
- The modeling failure: when a unit is not selected, flows go to zero and nonlinear input-output equations become singular; GDP removes the unselected equations (S1 [0:58:57]–[1:02:32], summarized; the same rationale appears in the 2026 EJOR review, S22 p. 13). The 1988 remark that MINLP modeling "still remains an area that is not very well understood" is quoted in 01 SW2.
- Records: Westerberg, Grossmann et al. 1990, "Applications of AI in design research at Carnegie Mellon University's EDRC" (P17); Raman & Grossmann 1991 (P18) and 1994 (P21); Hooker, Yan, Grossmann & Raman 1994 (P22); Türkay & Grossmann 1996 (P24); Lee & Grossmann 2000 (P28); Grossmann & Trespalacios 2013 on systematic GDP modeling (P47). The 1994 CAST slides list "Expand scope models / Integrate equations and symbolic logic" as challenge 1 (S8 p. 18, transcribed from scan). [practice; stated]

**T6. From design to operations: scheduling and planning (1985–2005).** Trigger: industry needs as he read them, plus funding.
- [stated, S8 p. 19, transcribed from scan] Under "Future Needs": "Chemical Industry: / - Greater economic pressures / - Globalization", "- Increased efficiency in operations", "- Integration of planning, production, marketing", "- Improved design capabilities", "⇒ Greater role for Mathematical Programming".
- NSF records mark the dates [practice, P, S23]: 1989 "Planning and Scheduling of Multiproduct Continuous Processes"; 1992 design and scheduling of multiproduct plants; 1993 US–Argentina cooperation on batch-plant planning and scheduling (the start of the Santa Fe connection, INTEC/INGAR); 1995 and 1998 grants on scheduling under uncertainty.
- Records: Sahinidis et al. 1989 long-range planning (P14); Kondili, Pantelides & Sargent 1993, the State-Task Network paper from his advisor's group (P20); Maravelias & Grossmann 2004 (P34).

**T7. Uncertainty: flexibility, then stochastic programming, then back to flexibility (1980–2020).** Triggers: a peer, industry, and a new literature.
- Flexibility (1980–1991): PhD problem three, the 1980 meeting with Morari ("Ignacio Grossmann met Manfred Morari in 1980 on their way to Hennicker to attend the 1st FOCAPD meeting", S20 p. 2, joint), NSF grants of 1980 and 1982 (S23). Records: Halemane & Grossmann 1983 (P5); Swaney & Grossmann 1985 (P7); Pistikopoulos & Grossmann 1988 (P12).
- To stochastic programming (1998–2017): his slide driver is "From Deterministic to Probabilistic Approaches for Uncertainty" (S6 p. 8). The entry is oilfield planning with industry co-authors (Iyer et al. 1998, P27) and endogenous ("decision dependent") uncertainty (Goel & Grossmann 2006, P37). In 2015 he tells the field's history in the same order: "during the 70s there were a number of interesting papers published in the area of optimal design under uncertainty and subsequently in the late 90s early 2000 it was the shift towards planning under uncertainty" (caption S4 [0:25:26]). On endogenous uncertainty he credits a Norwegian PhD thesis as the pioneer (ASR "John spratten", probably Jonsbråten, not verified) and adds "a good part of it has been done by our group at Carney Mellon related to oil and gas field process networks" (S4 [0:55:11]).
- Back to flexibility (2014–2020): after the robust-optimization literature introduced adjustable recourse [inferred from his own framing: Ben-Tal's adjustable robust optimization in the 2015 plenary, S4 [0:32:29], and "there's been lately in robust optimization the idea of quote adjustable robust optimization", S1 [1:04:06]]. Records: the Morari tribute (P53, 2014); Zhang et al. 2016 on adjustable robust optimization for interruptible load (P54); Zhang, Grossmann & Lima 2016 on flexibility analysis versus robust optimization (P55). In the 2024 interview he says that for two or more uncertain parameters robust optimization is more conservative and flexibility analysis "actually gives you better answers" (S1 [1:07:16]; see 02 Contradiction 4).
- His working rules on the topic, at two dates [stated, caption]: 2015: "by and large I would say short term is robust long-term stochastic programming" (S4 [1:19:20]); 2024: "first and foremost you need to have a robust and well- defined deterministic problem" (S1 [1:05:08]).

**T8. Hybrid MILP/constraint programming (1999–2004; residual to 2010).** Trigger: a CMU operations-research colleague and an NSF program.
- [practice, P, S23] NSF ITR/AP 0121497, "Model-Based Integration of Methods for the Optimization of Process Systems" (2001–05, $955,000, co-PI John Hooker), and a US–Argentina grant on integrating disjunctive programming with constraint logic programming (0104315, 2001–05).
- Records: Jain & Grossmann 2001 (P30); Harjunkoski & Grossmann 2002 (P31); Maravelias & Grossmann 2004 (P34); Castro, Grossmann & Rousseau 2010 (P41).
- Exit: no stated reason found. Constraint programming survives as a six-page chapter of his 2021 textbook (P65). [practice; exit inferred]

**T9. Biology: in and out (2000–2003, thesis 2006), and a technique that came back (2024).** Trigger in: a CMU colleague (Michael Domach) and the bio wave in chemical engineering. Trigger out: his judgment of industrial demand.
- Records: Lee, Phalakornkule, Domach & Grossmann 2000, "Recursive MILP model for finding all the alternate optima in LP models for metabolic networks" (P29); Phalakornkule et al. 2001 (P32); Zhu et al. 2003 (P33). Ghosh's 2006 thesis is the "Other" line on his slides.
- Stated reason for not making biology a focus [stated, P, S18 p. 13, 2004]: "There are many potential and exciting possibilities in biological related research in PSE. However, industrial growth in that area is unlikely to become sufficiently large so that it should become the major focus of PSE research." In 2014 he described the bio wave in faculty hiring ("the new young professors are even approaching close to 40% of the composition of the faculty", caption S5 [0:12:41]) and an industry poll that rated biotechnology low (S5 [0:12:11]).
- The technique came back: the 2000 idea of enumerating alternate optima of an LP with a recursive MILP reappears in Kakkad et al. 2024, "Iterative MILP algorithm to find alternate solutions in linear programming models" (P66), built for Aurubis supply chains to make optimization models explainable. That paper won the Howard Rosenbrock Prize (S30, S31). [practice; the link is inferred]

**T10. Enterprise-wide optimization (2003–).** Triggers: a change of role and place, industry, and solver progress.
- Context [stated]: the 2004 essay was written "having been department Head at Carnegie Mellon for the last eight and one half years" (S18 p. 1) and during a Fulbright Senior Lectureship in Santander (S18 p. 13). In 2001 he chaired Dow's Technical Advisory Board of Engineering Sciences (S26); Dow's John Wassick became co-PI of his 2006 NSF GOALI on integrating planning and scheduling (0556090, S23).
- The forecast was ten years older: "Integration of planning, production, marketing" (S8 p. 19, 1994).
- Launch text (2005, P36, journal p. 1846): "Enterprise-wide optimization (EWO) is a new emerging area that lies at the interface of chemical engineering and operations research, and has become a major goal in the process industries due to the increasing pressures for remaining competitive in the global marketplace." Twenty-one years later, his IEEE CASE 2026 keynote abstract opens almost identically, minus "new emerging" and "chemical": "Enterprise-wide optimization (EWO) is an area that lies at the interface of engineering and operations research, and has become a major goal in the process industries due to the increasing pressures for remaining competitive in the global marketplace." (S24) [practice: a stable framing]
- Records: P35 (2004), P36 (2005), P46 (2012 review).

**T11. Sustainability, water and biofuels (2008–2016 peak).** Triggers: his own critique, collaborators, funding, and the field's direction.
- His own critique, five years earlier [stated, P, S18 p. 12, 2004]: "Despite the great importance of sustainability and environmental issues, the research efforts from the PSE community have been rather timid."
- Collaborators and money: Gonzalo Guillén-Gosálbez (joint paper P42, 2010); Mariano Martín (Salamanca; his most frequent co-author in OpenAlex, 60 works, see 01); NSF 0966524, "Multiobjective Optimization Strategies for the Design of Sustainable Biofuel Processes" (2010–14, S23); the 2008 Pan-American institute whose award title starts with sustainability and energy (S23).
- His reading of the field in 2014 [stated, caption S5 [0:14:42]]: "both energy and sustainability will be probably emerging as new major trends that mainstream the pendulum somewhat away from bio and nano".
- Records: Martín & Grossmann 2011 (P43); Ahmetović & Grossmann 2011 (P44). By 2021 he was surveying the field's leaders himself ("Overview of Academic Research in Sustainability", with "Leaders in US and UK (Bahvik Bakshi and Adisa Azapagic)", S9 p. 1).

**T12. Shale gas (2013–2023).** Trigger: place.
- [stated, caption S3 [0:02:44], 2014] "Here in western Pennsylvania, shale gas is a major development that's taking place." He then describes work with "a company here in Western Pennsylvania" that cut water trucks "from 14,000 to less than 1,400" ([0:03:20]–[0:04:00]).
- NSF 1437668, "Optimization Models for Investment, Operation and Water Management in Shale Gas Supply Chains" (2014–18, S23). Drouven (PhD 2017) went to EQT, Pittsburgh (S7 p. 21).
- Records: Martín & Grossmann 2013 (P49); Cafaro & Grossmann 2014 (P50); Yang, Grossmann & Manno 2014 (P51). The last shale-gas title in OpenAlex is from 2023 (§4). No statement on why the line ended.

**T13. Electricity and power systems (2009–).** Triggers: industrial-gas partners and an oil company.
- Demand-side management for power-intensive plants came with Praxair (Linde), whose researcher José Pinto is a former student (PhD 1995, S7 p. 20); NSF GOALI 1159443 (2012–16) and 1705372 (2017–21) have Pinto as co-PI (S23). Records: Castro, Harjunkoski & Grossmann 2009 (P40); Mitra et al. 2012 (P45).
- Long-term power planning came from ExxonMobil [stated, S2 [0:51:01]]: "esto fue curiosamente una interacción con la compañía Exon Móvil" (tr.: "this was, curiously, an interaction with the company ExxonMobil"); he adds that the Department of Energy funded the project. Records: Lara et al. 2018 (P58); Cho, Tovar-Facio & Grossmann 2026 (P80), supported by NETL's IDAES and DOE (S32).
- An early outlier: Olsbu, Loeken & Grossmann 1988, power systems on oil platforms (P11).

**T14. Decarbonization and CO2 logistics (about 2019–).** Triggers: company climate targets and students.
- [stated, caption S1 [1:15:04]–[1:17:09], 2023/24] "the present emphasis I would say is now moving a lot more into Energy Systems"; with Total, "since about four or five years now we've been working on carbon capture and sequestration" ([1:16:37]); and on why industry matters: "we would probably never have run into that problem if we were just reading some papers" ([1:17:09]).
- [stated, S2, 2025] Shell's net-zero target and the question of what to do with existing refineries ([0:58:01]); his students' commitment to climate ([1:05:03]); and a political caveat: "en el momento en Estados Unidos no es exactamente el caso, tengo de que decir" (tr.: "at the moment in the United States that is not exactly the case, I have to say", [1:05:03]).
- Records: Chattopadhyay et al. 2025 (P69) and 2026 (P84); Shikha et al. 2025 (P70); Trucco et al. 2025 (P73); Vaidya et al. 2026 (P81); Xu et al. 2026 (P82).

**T15. Open-source modeling, preprints and machine learning (2016–).** Triggers: collaborators and co-authors from CMU and Sandia.
- Python and Julia: Pyomo.GDP with Sandia's John Siirola (2018, 2022; P63), DisjunctiveProgramming.jl (2023; see 01). His first arXiv preprint is OR-Gym (August 2020, P61); 16 arXiv records exist through July 2026 (S41). [practice]
- Machine learning: in the 2019 joint perspective he presented ML through others' work, "This is an area closely related to optimization as has been shown by Sahinidis and his group" and "reinforcement learning has been proposed by Lee for integrating planning and scheduling in process systems" (S21 pp. 15–16). His group's first reinforcement-learning paper followed in 2020, with Dow (Hubbs et al., P62). Later: NeurIPS 2025 (P72), GRAPSE (retrieval augmentation for PSE, ESCAPE-35, 2025; P71), convexification of Kolmogorov–Arnold networks (P91, 2026), and a finance paper, "Fragility of Minimum-Variance Portfolios" (P92, 2026). Three of these four are first-authored by Daniel Ovalle (a Grossmann PhD, 2026, per 04) and all four carry Carl Laird as co-author; the KAN paper is first-authored by Tianwei Li, with Ovalle second. Whether Laird was formally co-advisor was not checked. [practice]
- His stated stance in 2025 [stated, S2]: a neural network "no es otra cosa que un método de regresión" (tr.: "is nothing more than a regression method", [1:15:00]); where AI could matter most is explainability, "poder explicar en forma cualitativa las soluciones óptimas que se obtienen" (tr.: "being able to explain qualitatively the optimal solutions obtained", [1:16:03]), plus automating the routine writing of models, "son labores que son más de tipo mecánico" (tr.: "these are tasks of a more mechanical kind", [1:17:01]). The 2026 joint review: "MINLP/GDP-based training is not feasible today" (S22 p. 13).

### 3.3 What kind of trigger, how often [inferred, counting T1–T15]

| Trigger type | Turns | Comment |
|---|---|---|
| New tool or computing infrastructure | T2, T4, T15 | Each time the tool came first and the research line followed within two to three years |
| Person or place (advisor, colleague, visitor, region) | T1, T5, T7, T9, T10, T12 | Mostly people at CMU (Balas, Hooker, Domach, Westerberg, Laird) or met at meetings (Morari) |
| Industrial partner with a named problem | T6, T10, T12, T13, T14 (and T9's 2024 return) | Mobil/ExxonMobil, Dow, Praxair/Linde, EQT, Total, Shell, Aurubis |
| His own critique of the field | T3, T11 | 1983 (algorithmic methods neglected), 2004 (sustainability "rather timid") |
| Funding instrument | T6, T8, T11, T12, T13 | NSF GOALI, ITR, PASI, US–Argentina programs; in the 2010s, DOE/NETL |
| A failure or rejection | none | Resistance hardened existing directions (T3) rather than changing them |

---

## 4. Entry and exit timing relative to the field

Topic years come from title keywords in an OpenAlex snapshot of his works (885 distinct titles; my keyword classification; one title can count for several topics) [practice, S42; approximate]. "Verdict" is my reading of the evidence in the last column [inferred].

| Topic | His titles: first – last (count) | Field context when he entered | Verdict | Evidence |
|---|---|---|---|---|
| Mixed-integer synthesis | 1980 – | A reviewer called MILP "very inefficient"; heuristics and pinch analysis dominated | Before consensus | S1 [0:45:57]–[0:46:28]; S14 p. 4 |
| MINLP / outer approximation | 1986 – 2024 (15 with "outer approximation") | Earlier MINLP algorithms were "more theoretical than practical for OR practitioners" (S22 p. 3, on the early 1970s). In 1994 he lists "Mixed-integer nonlinear programming is not solvable" among "Mathematical Programming Taboos" to which "Chemical engineers have provided answers" (S8 pp. 15–16, transcribed from scan) | Before consensus; became a standard method | S22 p. 3; S8 pp. 15–16 |
| LP/NLP-based branch and bound | 1991–92 (P19) | No MILP solver callbacks until much later | 15–20 years ahead of the infrastructure | see 01 SW3 |
| Logic / GDP | 1991 – 2026 (102 with "disjunct" or "logic") | Balas's convex-hull result circulated as a 1974 report and was published in 1998 (S22 p. 3) | Early; still his central method | S22 p. 3 |
| Global optimization of special structures | 1988 – 2026 (40); peaks 1995–99 and 2005–14 (e.g. P23) | Floudas's and Sahinidis's general-purpose codes; he uses BARON in applications in 2025 (S2 [0:24:00], [0:33:00]) | Contemporary; narrowed to structure-specific methods | S42; S2 |
| Flexibility / resiliency | 1982 – 2025 (40); peak 1985–94, one title 2000–09, revival 2010–24 | Morari working on resiliency in 1980 | With the field; dormant, then revived after robust optimization | S20 p. 2; S42 |
| Batch scheduling | 1986 – 2019 (49); peak 2005–09 | His advisor's group's STN paper long rejected | Early in PSE | S1 [0:50:05]; S42 |
| Stochastic programming | 1988 – 2025 (42); peak 2005–19 | He credits a Norwegian thesis as pioneer of endogenous uncertainty | Follower, then a main contributor | S4 [0:55:11] |
| Hybrid MILP/CP | 2001 – 2021 (8; five in 2000–04) | Hooker's logic-based OR at CMU | With the OR wave; left by about 2010 | S23; S42 |
| Metabolic networks | 2000 – 2003 (3) | Bio boom in chemical engineering | With the wave; left with a stated reason (2004) | S18 p. 13 |
| Enterprise-wide optimization / supply chain | "supply chain" 2000 – 2025 (58); "enterprise" 2004 – 2021 (11) | Supply-chain management already established in OR; "a new frontier" in PSE | Early in chemical engineering, late relative to OR | P36; S42 |
| Biofuels / biomass | 2008 – 2025 (42); 24 in 2010–14 | He had called PSE's sustainability work "rather timid" (2004) | After pioneers he credits (Azapagic, Guillén-Gosálbez); peaked with the biofuel boom | S18 p. 12; S9 p. 1; S21 p. 16 |
| Shale gas | 2013 – 2023 (28) | Regional boom already under way | With the regional wave; left after 2023 | S3 [0:02:44] |
| Power / electricity | 1988; then 2009 – 2026 (56); peak 2015–19 | Long-established in power engineering and OR | Entered from the process-industry side | S42; S2 [0:51:01] |
| CO2 / decarbonization | 2001; then 2015 – 2026 (22; 17 since 2020) | Company net-zero targets | With industry demand | S1 [1:16:37]; S2 [0:58:01] |
| ML / RL / surrogates | 2008 (surrogates, P39) – 2025 (14; 9 in 2020–24) | In 2019 he cites others for RL and ML | After the wave, through co-authors | S21 pp. 15–16; P62 |
| Robust optimization (as a title word) | 2011 – 2018 (4) | Ben-Tal's adjustable robust optimization | Brief engagement, then reframed as flexibility | S4 [0:32:29]; P55 |

---

## 5. Agendas forecast versus what followed

| Year and source | What he forecast (verbatim where quoted) | What followed in his own record | Status [inferred] |
|---|---|---|---|
| 1994, CAST slides "Future Research Challenges" (S8 p. 18, transcribed from scan) | "1. Expand scope models / Integrate equations and symbolic logic" | GDP, 1994–2026 (T5) | Delivered by him |
| same | "2. Integration of diverse models / Design, planning, scheduling, control" | EWO (2005–); planning–scheduling integration. In 2004 he still calls "the integration of planning, scheduling and control" "The major pending research problem that still remains" (S18 p. 9) | Partly delivered |
| same | "3. Anticipate effects of uncertainty / Stochastic optimization" | Multistage stochastic programming with endogenous uncertainty (Goel, Tarhan, Gupta, Apap, C. Li; P37, P67) | Delivered |
| same | "4. Solution large-scale models / Orders of magnitude increase" | Decomposition: Lagrangean (17 titles, 10 of them 2010–14), Benders, nested decomposition (P58), bilevel (P85) | Delivered in part |
| same | "5. Global optimization of general models / Mixed-integer differential-algebraic" | Not a main line of his. The 2026 EJOR review lists "Nonlinear dynamic optimization with discrete decisions" as a future direction (S22 p. 14) | Still open 31 years later |
| 1994 (S8 p. 19) | "Integration of planning, production, marketing" | Enterprise-wide optimization (2005) | Delivered ten years later |
| 2000, with Westerberg (S17) | Product and molecular design, process intensification, supply chain, sustainable design | He took supply chain and intensification (reactive distillation; NSF GOALI 9710303 with Westerberg and Eastman's Siirola, 1997). Molecular design he left to others: in 2025 he presents Floudas's and Gounaris's molecular work and says "Obviamente yo no he trabajado directamente en eso" (tr.: "Obviously I have not worked directly on that", S2 [0:31:00]+) | Selective |
| 2004 (S18 pp. 12–13; and the joint retrospective P48) | Three themes: product discovery and design; enterprise and supply chain; global life-cycle assessment. Electronics "has received be little attention"; biology not "the major focus" | Enterprise (2005–) and life-cycle / sustainability (2009–) taken up; product discovery and electronics not; biology dropped | Two of three taken |
| 2014 (S6 p. 15) | Under "Emerging challenges": "Product and Process Design", "Energy and Sustainability", "Enterprise-wide Optimization" | Energy, sustainability and EWO dominate his 2014–2026 output | Delivered |
| 2026 EJOR (S22 pp. 13–14, joint) | Decomposition and multi-scale; interpretable hierarchical GDP; surrogate models; dynamic optimization with discrete decisions; GDP for AI | 2025–26 papers on decomposition (P79, P84, P85), interpretability (P66), surrogate and learned constraints (P72) | In progress |

---

## 6. Failures, rejections, abandoned directions (trajectory view)

- **Resistance at the start** [stated, caption S1]: a rejected MILP-synthesis paper, the reviewer arguing that mixed-integer programming was "very inefficient" ([0:45:57]); the keynote "process synthesis a Utopia in mathematical programming or an adventure in heuristics" ([0:47:29]); the speaker's advice to move to process control ([0:51:38]). His summary 40 years later: "I'm very happy to say that after you know almost 40 years definitely the answer is yes" ([0:49:02]). Speaker and year are not identified (Gaps).
- **The slow review of the outer-approximation paper**: "the review took you know long time" and "maybe it was our engineering type of slant that did not fit exactly with the one of math programming" (caption S1 [0:56:19]). An erratum followed (P9; see 01 SW1).
- **His advisor's group's State-Task Network paper**, by his account: "it was submitted for a second time got again rejected it was finally accepted for the third time" (caption S1 [0:50:05]). He dates the episode "maybe something like late 80s"; the paper appeared in 1993 (P20). [stated about others]
- **Abandoned directions** [practice; reasons inferred unless stated]: metabolic networks (2000–03; stated reason in 2004; T9); hybrid MILP/CP (main work 1999–2004; T8); shale gas (no titles after 2023; T12); robust optimization as a standalone framing (2015–18); electronics, proposed for PSE in 2004 and never entered; DICOPT's two-phase convexity tests, the OA "Part II" report and the grid-computing proposal for EWO (see 01 §2–3).
- **The "Lessons Learned" slides as his stated policy** [stated, P]. 2014 (S6 pp. 16–17): "1. It pays to dream and it pays to persevere; do not give up!"; "2. Be strategic: concentrate on few areas", with "The essence of strategy is choosing what not to do." (Michael E. Porter); "5. View industry as source of new research problems"; and under "To be avoided": "University (corporate) administrators: view them with suspicion" and "University IP lawyers: unless you really have to, ignore them." In 2019 (S7 pp. 17–18) the "To be avoided" box is gone and two lessons are added: "7. Need to promote the importance of rigorous education in mathematics" and "8. Need to celebrate scholarly work and academic excellence". The 2019 outline promises "Lessons learned and awareness of threats" (S7 p. 2).
- **Losses that ended collaborations**: three former students died in their mid-fifties, Duran, Floudas (2016) and Raman (caption S1 [1:18:11]–[1:21:51]); for Duran he co-wrote a 2021 biographical review (P68, not read); a memorial editorial for his collaborator Pedro Castro appeared in 2026 (P83). No retraction was found; errata are listed in 01 §3.
- **Funding trajectory** [practice, P, S23]: 26 NSF awards as PI with start dates from 1980 to 2017 (including conference and workshop grants); none starts after 2017. Later work is acknowledged to CAPD, DOE/NETL (IDAES) and companies (S32; 04 §E). [inferred] Over his career, federal single-PI grants gave way to consortium, DOE and company funding.

---

## 7. Era and resource context

| Period | His role | Compute and tools | Funding and partners | Group | What it helps explain [inferred] |
|---|---|---|---|---|---|
| 1974–79 | PhD student; IMP group leader | Punch cards and Fortran: "sometimes you have to wait a full day" (caption S1 [0:37:02]); Sargent's NLP method; UNIVAC FMPS at IMP | British Council; IMP | — | Small models whose structure is exploited by hand (convexifying a geometric program, analytic derivatives) |
| 1979–86 | Assistant, then associate professor (1983) | DRC computing; MILP codes; MINOS | NSF CPE grants (1980, 1982), PYI (1984); Exxon Education Foundation (see 01) | First PhDs 1982 | MILP superstructures, then OA |
| 1986–94 | Full professor; EDRC Synthesis Lab director; CAPD | GAMS, MINOS, MPSX on an IBM 3090 (Cornell); IBM OSL (see 01 SW4) | EDRC ($21M NSF, 1986–97); CAPD founded with five companies | 10 PhDs in the 1980s | DICOPT, logic, GDP |
| 1994–2002 | Department Head | Workstations; fast-improving MILP solvers | NSF GOALI with Eastman (1997); US–Argentina programs (1993, 1998); Dow TAB (2001) | 16 PhDs in the 1990s | Scheduling, logic-based OA, textbook (1997) |
| 2003–2015 | Fulbright in Spain (2003–04); CAPD director (2005–15) | Strong commercial MILP; COIN-OR (Bonmin, P38) | NSF ITR (2001), CMU–IBM MINLP cyberinfrastructure (2008), GOALIs with Dow and Praxair; Pan-American institutes | 16 PhDs in the 2000s, 17 in the 2010s; about 90 visitors over his career (see 04) | EWO, sustainability, shale gas |
| 2016–2026 | Senior; phased retirement from 2023 | Python (Pyomo.GDP), Julia (JuMP), BARON; desktop benchmarks (P59); arXiv from 2020 | DOE/NETL IDAES; CAPD (about 20 companies); Shell, Total, Aurubis, Dow, Linde | 8 PhDs 2020–26; in Oct 2026, 5 students and 5 visitors | ML and finance through co-authors; decarbonization; logistics |

PhD counts per decade are from 04 §A.1 (his group roster); company and agency names are from S23, S25, S27 and the 2024 interview (S1). Dates of computing tools come from the cited reports and captions.

---

## 8. The last twelve months (10 Oct 2025 – 10 Oct 2026), dated

### 8.1 Honours, roles, people

- 16 Sep 2025 (just before the window; the anchor of his current self-presentation): lecture at the Spanish Royal Academy of Sciences on his admission as foreign academician (S2).
- 25 Nov 2025: CMU announces the Howard Rosenbrock Prize for the best 2024 paper in *Optimization and Engineering* (P66), an explainability algorithm built with Aurubis; the prize announcement in the journal is dated 25 Oct 2025 (S30, S31).
- 17–21 Aug 2026: keynote at IEEE CASE 2026, Shenyang, on enterprise-wide optimization; his abstract lists batch plants, ethanol and gasoline supply chains, refinery decarbonization, CCS logistics, power-system expansion, lignocellulosic ethanol, shale gas, resilient supply chains, digital supply chains and reinforcement learning for scheduling (S24). [inferred] The conference contact address is at Northeastern University (Shenyang), the home institution of a 2026 visitor in his group (S12) and of an earlier visitor and 2025 co-author, Lijie Su (S7 p. 24; P78).
- 8 Oct 2026: elected International Fellow of the Royal Academy of Engineering; ceremony on 19 Oct (S28, S29). His statement in the CMU release: "I am incredibly humbled and grateful to be elected to the prestigious Royal Academy of Engineering." (S28)
- Nov 2026 (scheduled): 2026 INFORMS Saul Gass Award for Expository Writing (S13; not yet on the INFORMS page, S35).
- Conference talks listed on Google Scholar (titles as listed; abstracts not opened; S38): "Contributions By Tom Edgar to Education and Teaching in Process Systems Engineering" (2025 AIChE Annual Meeting); "Contributions of Stratos Pistikopoulos to Process Systems Engineering" and "Evaluating Supply Chain Resiliency Using Graph Neural Networks" (2026 AIChE Annual Meeting, upcoming).
- People: Laird is Department Head (S28); Biegler is CAPD director since 2025 (S25); Gounaris leads the EWO interest group (S25). His group page (read 10 Oct 2026, S12) lists five students (copper processing; supply-chain inventory management; refinery decarbonization retrofit; synthesis of pipelines; supply-chain optimization) and five visitors (two from INTEC Santa Fe, one each from Zhejiang University, Cantabria and Northeastern University Shenyang).

### 8.2 Publications with identifiers (Crossref publication date)

- **Methods and reviews**: Kronqvist, Bernal Neira & Grossmann, "50 years of mixed-integer nonlinear and disjunctive programming", *EJOR* 331(3), June 2026 (P75); Ovalle et al., logic-based decomposition with symmetry-breaking cuts for multiperiod blending, *I&ECR* 65(7), Feb 2026 (P79); Chattopadhyay et al., bounding algorithm for multi-time-scale decarbonization planning (refinery electrification), *Comput. Chem. Eng.* 213, Oct 2026 (P84); Hu et al., wind-farm layout and cable routing, MINLP to MIQCP with bilevel decomposition, *Comput. Chem. Eng.* 214, Nov 2026 (P85); Vaidya et al., computational strategies for a multiperiod MINLP for CCS, *I&ECR* 65(10), Mar 2026 (P81).
- **Power systems**: Cho & Grossmann, two-stage stochastic programming for resilient power systems, *Int. J. Electr. Power Energy Syst.* 173, Dec 2025 (P76); Cho, Tovar-Facio & Grossmann, reliability formulations, *IEEE Trans. Power Syst.* 41(2), Mar 2026 (P80); Cho, Grossmann, Omell & Burgard, probabilistic reliability-constrained generation and transmission expansion planning, SSRN preprint, Sep 2026 (P90).
- **Supply chains and operations**: Bonino et al., industrial-gas production and routing, *I&ECR* 64(45), Oct 2025 (P74), and fleet sizing and production-routing, *Comput. Chem. Eng.* 215, Dec 2026 (P87); Su, Tang, Grossmann & Huang, refinery-wide scheduling under uncertainty, *Optim. Eng.* 27(2), Dec 2025 (P78); Sun et al., crane scheduling for tankhouse copper processing, *Comput. Chem. Eng.* 211, Aug 2026 (P86; four co-authors overlap with the 2024 Aurubis prize paper).
- **CO2 and pipelines**: Trucco et al., deep saline aquifers for CO2 storage, *Comput. Chem. Eng.* 203, Dec 2025 (P73); Xu et al., optimization with discrete-event simulation for CCS supply logistics, *I&ECR* 65(13), Mar 2026 (P82); Trucco et al., multiphase fluid dynamics in oil and gas pipeline network design, *Comput. Chem. Eng.* 216, 109897 (issue dated Jan 2027 by Crossref; online 2026) (P88).
- **Machine learning, finance, reviews (preprints)**: Li, Ovalle, Póczos, Laird, Grossmann & Peña, convexification of Kolmogorov–Arnold networks, arXiv:2604.03871, Apr 2026 (P91); Ovalle, Laird, Grossmann & Peña, "Fragility of Minimum-Variance Portfolios", arXiv:2607.18624, Jul 2026 (P92); Vyas, Laird, Grossmann, Lima, Harjunkoski & Poland, unit commitment models and algorithms, arXiv:2607.19570, Jul 2026 (P93). The NeurIPS 2025 paper (P72) and GRAPSE (July 2025, P71) fall just before the window.
- **Book chapter and editorial**: Cho & Grossmann, chapter in *Optimization of Sustainable Process Systems* (Wiley, Apr 2026; P89); Grossmann & Matos, "Advances in the Optimization of Process Operations – In Memory of Pedro Castro", *I&ECR* 65(20), May 2026 (P83).
- **Volume** [practice, S38; mixed item types]: Google Scholar lists 28 items for 2025 and 18 for 2026 up to 10 October (papers, preprints, conference abstracts). OpenAlex has 129 works for 2020–24, about 26 a year (01 §1.2). [inferred] No visible drop in output after the move to 50% in September 2023.

### 8.3 Reading of the last year [inferred]

1. His role is now **senior and last author** on applications brought by CMU colleagues (Laird, Torres), former students (Pinto at Linde; Bernal Neira at Purdue), visitors (INTEC Santa Fe, Zhejiang, Northeastern) and companies (Shell, TotalEnergies, Aurubis, Dow). The algorithmic MINLP/GDP thread continues mainly through the EJOR review and co-authored student work.
2. **New domains arrive through co-authors' networks**: finance and KAN convexification (with CMU's Javier Peña and Barnabás Póczos), retrieval-augmented LLM tools (with John Kitchin), power-grid reliability (with NETL). These look like a co-advising effect rather than a turn of his own; his own 2025 statements on AI remain sceptical (T15).
3. His **public narrative is stable**: the 2025 lecture repeats the 2014 picture of PSE growing toward the molecular and the enterprise scale ("La tendencia últimamente ha sido por un lado ir a la parte molecular", tr.: "the recent trend has been, on one side, to go to the molecular level", S2 [0:29:00]; compare S5 [0:15:12] and S6 p. 14), and his 2026 keynote repeats the 2005 EWO definition (T10).

---

## 9. What the trajectory implies for the skill, by layer [inferred]

- **Layer 2, problem choice ("why now")**: a topic opens when one of three things appears: a tool that makes a formulation solvable (FMPS, GAMS, Pyomo), a partner who owns a problem and its data (Dow, ExxonMobil, EQT, Total, Shell, Aurubis), or a colleague who brings a missing theory (Balas, Hooker, Morari). A Grossmann lens asks of a new topic: who owns this problem, which tool just made it tractable, and which student lineage will carry it.
- **Layer 2, giving up**: exits are judged by industrial demand (biology, 2004) and by focus ("concentrate on few areas"), and are not announced; techniques are kept and reused later (alternate optima, 2000 → 2024).
- **Layer 3, idea sources**: failures of his own group's models (discretization, zero flows, an expensive master problem) and the next scale up the "chemical supply chain".
- **Layer 5, judging and persisting**: rejection is a reason to persist when the method is sound ("can we prove him to be wrong"); a deterministic model first, uncertainty second; robust optimization for the short term, stochastic programming for the long term (2015).
- **Layer 7, long-term organisation**: agenda statements every five to ten years (1994 slides, 2000, 2004, 2005, 2012, 2019, 2026), a career told as student lineages, and an industrial consortium that supplies problems; late in his career, co-authorship with younger colleagues is how new domains enter his record.

---

## Contradictions (kept, not reconciled)

1. **When CAPD started.** "Since the CAPD's founding in 1985" (CEE 2019, S27 p. 4) against "Biegler, Grossmann, Westerberg Founded CAPD Center 1986" (his own 2019 slide, S7 p. 5) and "CAPD started in 1986" (S25); the same CAPD page has Westerberg join CAPD "starting with five companies" in 1984. See also 04 Contradiction 3.
2. **When he became EDRC Synthesis Laboratory director.** "director of the Synthesis Laboratory at the university's Engineering Design Research Center (EDRC) ... in 1988" (CMU News 2001, S26) against "Grossmann is the Synthesis Lab Director for the first seven years" of the EDRC, which the same page dates to 1986 (S25).
3. **His CAPD directorship.** 2005–2015, then "2021 - Carl Laird succeeds Ignacio Grossmann as director of the CAPD" (S25), which implies a second term around 2020–21 that no other source mentions (also 04 Contradiction 4).
4. **Student counts, all from 2019–2026.** 65 PhD and 24 MS (2019 slide, S7 p. 22); 68 and 34 (CMU bio and RAEng release, 2026; S13, S28); 68 and 37 (egon biosketch, S10); 69 PhD theses and 40 master's (Spanish Academy introduction, Sep 2025, S2 [0:07:02], [observed]); 8 students in MGP (S37). Academic placements: 16 (S1, 2024), 12 (CEE 2019), 13 (04).
5. **Paper counts in the same year.** "more than 700" (CMU bio and RAEng release 2026; S13, S28) against "more than 800 papers" (IEEE CASE 2026 bio, S24). Citations: "more than 80,000" (S28), "over 79,000" with h-index 149 (S24), 80,981 with h-index 150 (Scholar on 2026-10-10, S38).
6. **The water-network example.** Fresh water cut "from 300 tons per hour down to only 14 tons per hour" (2014 video, caption S3 [0:02:00]) against "40 toneladas por hora" compared with 300 in the conventional system (2025 lecture, caption S2 [0:47:00]). Both are automatic captions; they may be different cases.
7. **Stated scepticism about AI against a growing ML output.** In 2025 a neural network "no es otra cosa que un método de regresión" (S2 [1:15:00]) and MINLP/GDP-based training "is not feasible today" (S22 p. 13); in the same year and the next his name is on a NeurIPS paper (P72), a retrieval-augmented LLM tool (P71) and KAN convexification (P91). The stated view and the co-authored practice differ in emphasis.
8. **Robust optimization versus flexibility analysis.** 2015: "short term is robust long-term stochastic programming" (S4 [1:19:20]); 2016: a paper adopting adjustable robust optimization (P54); 2024: flexibility analysis "actually gives you better answers" than robust optimization for two or more uncertain parameters (S1 [1:07:16]). Kept as a time series (see also 02 Contradiction 4).
9. **The State-Task Network story.** He places its triple submission "maybe something like late 80s" (S1 [0:50:05]+); the paper appeared in *Comput. Chem. Eng.* in 1993 (P20). Memory against record, or a long delay; not resolved.
10. **When biology mattered.** In 2004 biology is "unlikely" to become "the major focus of PSE research" (S18 p. 13), after his own 2000–03 metabolic papers (P29, P32, P33); in 2025 he features Floudas's protein design among PSE's successes and says molecular work is still "relativamente una fracción pequeña" (tr.: "relatively a small fraction", S2 [1:10:01]). Compatible readings exist; kept as stated.
11. **The date of the "CAST Award 1994" slides.** His site labels them 1994, and the cartoon on p. 20 carries a 1994 copyright, but the student list on p. 2 gives graduation year 1995 for Daichendt and Pinto (expected dates, or a later revision of the slides).

---

## Gaps

- **The "utopia" keynote**: speaker and year not identified; one WebSearch on the title found nothing. [inferred, unverified] It may have been the 1st FOCAPD (Henniker, 1980), the meeting at which he says he met Morari (S20 p. 2).
- **NAE election**: year taken from a 2001 CMU article ("last spring"); the NAE member page sits behind a bot check and its citation was not read.
- **Undated items on his CMU page**: the Cantabria talk "Computational Strategies for Optimizing Multiperiod Blending and Integrated Design of Wind Farms" ("September 14", year not shown; the topics match his 2026 papers, so 2026 is likely but unverified); the Shell Lecture at Rice University; the co-chairing of the NAE–Tecnológico de Monterrey conference on the North American supply chain (the event page did not load, S45).
- **Talks not watched or read**: the 2021 UNL lecture on energy systems (Spanish; YouTube xp6GSDxLqLA), the 2019 Tepper talk on nonconvex GDP (kiiRWXAlGqg), the Imperial College seminar on OA regularizations, and the ESCAPE 2018 talk. The CAPEC 2014 and PSE-2015 captions I saved were read only in part (keyword search and selected passages).
- **Stated reasons for exits**: none found for hybrid MILP/CP, shale gas, or global optimization as an algorithmic line. The exits in §4 are inferred from title counts.
- **Textbook sabbatical**: the 2021 textbook was written "on a sabatical leave and I would spent with a full PR program three months in Argentina" (caption S1 [1:27:36]; "full PR" may be "Fulbright"); year and host not found.
- **The 75th-birthday sessions (2024)**: see 01 Gaps (found by search, blocked).
- **The 2026 Saul Gass Award**: confirmed only by CMU; the award citation is not yet published.
- **Funding after 2017**: DOE, NETL and company contracts were not enumerated (no public database consulted beyond NSF).
- **Honorary doctorates**: years not found except Alicante (2019) and, per 02, UNL (2018).
- **The Mathematics Genealogy Project** lists 8 of 68 PhDs; the group's "Academic Family Tree" link (titan.princeton.edu/tree) was unreachable (04).
- **Advising arrangements of the newest students** (e.g. whether Laird formally co-advised Ovalle) were not checked.

---

## Sources

**Primary**
- S1. "Subject to: Ignacio Grossmann", interview, host Anand Subramanian; YouTube, uploaded 2024-02-08; https://www.youtube.com/watch?v=jNjqnsnUzhE; transcript `../sources/talks/2024-02-08_subject-to-interview_jNjqnsnUzhE.txt` (saved by agent 04). Primary, caption-derived.
- S2. I. E. Grossmann, "Evolution and Future Trends in Process Systems Engineering", Real Academia de Ciencias Exactas, Físicas y Naturales (Spain), 16 Sep 2025; https://www.youtube.com/watch?v=r9jdqigq59Q; transcript `../sources/talks/2025-09-16_rac-spain-evolution-future-trends-pse_r9jdqigq59Q_es-auto-captions.txt` (saved by agent 02). Primary, Spanish captions (the introduction by I. Ortiz is [observed]).
- S3. "Ignacio Grossmann: Optimization Models and Methods", CMU College of Engineering, 2014-10-07; https://www.youtube.com/watch?v=bx909_u-crY; transcript `../sources/talks/2014-10-07_cmu-optimization-models-and-methods_bx909_u-crY_auto-captions.txt` (saved by agent 02). Primary, caption-derived.
- S4. "Prof. Grossmann's Plenary Lecture + Opening session at PSE-2015/ESCAPE-25", uploaded 2015-06-01; https://www.youtube.com/watch?v=EqjnmhqEu1U; transcript `../sources/talks/2015-06-01_pse2015-escape25-plenary-optimization-under-uncertainty_EqjnmhqEu1U_auto-captions.txt` (saved by me). Primary, caption-derived, read in part.
- S5. "CAPEC PROCESS 2014 (full version)": I. E. Grossmann, "Role of Process Systems Engineering in Chemical Engineering", DTU, uploaded 2014-09-15; https://www.youtube.com/watch?v=gPD6VuTi3vE; transcript `../sources/talks/2014-09-15_capec-process-2014-role-of-pse_gPD6VuTi3vE_auto-captions.txt` (saved by me). Primary, caption-derived, read in part.
- S6. I. E. Grossmann, "Reflections on 35 Years in Process Systems Engineering Research", slides, AIChE Annual Meeting, Atlanta, 17 Nov 2014; http://egon.cheme.cmu.edu/pdf/Reflections_Grossmann.pdf. Primary, read in full.
- S7. I. E. Grossmann, "Reflections on 40 Years in Process Systems Engineering Research", slides, AIChE Annual Meeting, Orlando, 11 Nov 2019; http://egon.cheme.cmu.edu/pdf/Reflections_40_Grossmann_2019.pdf. Primary, read in full.
- S8. I. E. Grossmann, "On the Scope and Future of Mathematical Programming in Chemical Process Systems", slides (labelled "CAST Award 1994" on his site), scanned PDF; http://egon.cheme.cmu.edu/pdf/Scope%20and%20Future%20of%20Math.Prog.%20slides.pdf. Primary; page images viewed (pp. 1–22), transcriptions mine.
- S9. I. E. Grossmann, "Overview of Academic Research in Sustainability", slides, 15 Jun 2021; http://egon.cheme.cmu.edu/pdf/Review_Research_Sustainability.pdf. Primary, pp. 1–12 read.
- S10. Biosketch, Grossmann research group; http://egon.cheme.cmu.edu/biosketch.html (read 2026-10-10). Primary, self-maintained.
- S11. Presentations page and FOCAPD-2019 Sargent session page, Grossmann research group; http://egon.cheme.cmu.edu/presentations.html, http://egon.cheme.cmu.edu/focapd.html (read 2026-10-10). Primary.
- S12. People page, Grossmann research group; https://egon.cheme.cmu.edu/people.html (read 2026-10-10). Primary, group-maintained.
- S13. CMU Chemical Engineering bio page and media mentions; https://www.cheme.engineering.cmu.edu/directory/bios/grossmann-ignacio.html (read 2026-10-10). Primary (institutional self-presentation).
- S14. I. E. Grossmann, "Mixed-integer programming: is it a useful tool in process synthesis?", DRC-06-59-83, July 1983; KiltHub DOI 10.1184/R1/6467171.v1. Primary, pp. 1–4 and 24 read.
- S15. G. R. Kocis, I. E. Grossmann, "Computational experience with DICOPT solving MINLP problems in process systems engineering", EDRC-06-43-88, January 1988; KiltHub DOI 10.1184/R1/6466841.v1. Primary, pp. 1–3 and acknowledgments read.
- S16. C. A. Floudas, I. E. Grossmann, "Algorithmic approaches to process synthesis: logic and global optimization", EDRC 06-174-94, 1994; KiltHub DOI 10.1184/R1/6466703.v1. Primary, DataCite abstract only.
- S17. I. E. Grossmann, A. W. Westerberg, "Research challenges in process systems engineering", *AIChE J.* 46(9):1700–1703, 2000; 10.1002/aic.690460902; author copy http://egon.cheme.cmu.edu/Papers/GrossmannWestChall.pdf. Primary, joint, "Future Challenges" section read.
- S18. I. E. Grossmann, "Challenges in the new millennium: product discovery and design, enterprise and supply chain optimization, global life cycle assessment", *Comput. Chem. Eng.* 29(1):29–39, 2004; 10.1016/j.compchemeng.2004.07.016; author copy http://egon.cheme.cmu.edu/Papers/GrossmannChall.pdf. Primary, pp. 1, 6, 9, 12–13 read.
- S19. I. Grossmann, "Enterprise-wide optimization: A new frontier in process systems engineering", *AIChE J.* 51(7):1846–1857, 2005; 10.1002/aic.10617; copy http://egon.cheme.cmu.edu/Papers/GrossmannEWO.pdf. Primary, abstract read.
- S20. I. E. Grossmann, B. A. Calfa, P. Garcia-Herreros, "Evolution of concepts and models for quantifying resiliency and flexibility of chemical processes", *Comput. Chem. Eng.* 70:22–34, 2014; 10.1016/j.compchemeng.2013.12.013; author copy (Rev. Dec. 2013) http://egon.cheme.cmu.edu/Papers/Grossmann_Flexibility_in_Chemical_Process_Design.pdf. Primary, joint, pp. 1–2 read.
- S21. I. E. Grossmann, I. Harjunkoski, "Process Systems Engineering: Academic and industrial perspectives", *Comput. Chem. Eng.* 126:474–484, 2019; 10.1016/j.compchemeng.2019.04.028; extended copy http://egon.cheme.cmu.edu/Papers/Grossmann%20and%20Harjunkoski_Extended%20PSE2018.pdf. Primary, joint, pp. 14–16 read.
- S22. J. Kronqvist, D. E. Bernal Neira, I. E. Grossmann, "50 years of mixed-integer nonlinear and disjunctive programming", *Eur. J. Oper. Res.* 331(3):687–705, 2026; 10.1016/j.ejor.2025.07.016; copy https://egon.cheme.cmu.edu/Papers/Kronqvist_Bernal_Grossmann_EJOR.pdf. Primary, joint, pp. 1–3 and 13–14 read.
- S23. NSF Award Search API, query pdPIName=Grossmann (26 awards with Ignacio Grossmann as PI, starts 1980–2017; e.g. 7926398, 8351237, 8908735, 0121497, 0556090, 0750826, 0966524, 1159443, 1437668, 1705372); https://api.nsf.gov/services/v1/awards.json?pdPIName=Grossmann (queried 2026-10-10). Primary (funder's record).
- S24. IEEE CASE 2026, keynote speakers page (Grossmann's abstract and bio) and home page (dates 17–21 Aug 2026, Shenyang); https://2026.ieeecase.org/keynote-speakers/, https://2026.ieeecase.org/. Primary for the abstract, secondary for the event.

**Secondary**
- S25. CAPD, "About" page with history timeline (unsigned); https://capd.cheme.cmu.edu/about/index.html (read 2026-10-10). Secondary.
- S26. "Grossmann, McClelland and Siewiorek Earn Top Academic Distinction", *Carnegie Mellon News*, 10 May 2001; https://www.cmu.edu/cmnews/051001/051001_profs.html. Secondary.
- S27. L. T. Biegler, C. Gounaris, N. V. Sahinidis, B. E. Ydstie, "Educator Profile: Ignacio Grossmann of Carnegie Mellon University", *Chem. Eng. Educ.* 53(3), 2019; 10.18260/2-1-370.660-114401. Secondary, observed, read in full.
- S28. "Grossmann elected to Royal Academy of Engineering", CMU Chemical Engineering news, 8 Oct 2026; https://www.cheme.engineering.cmu.edu/news/2026/10/08-grossmann-elected-to-royal-academy-of-engineering.html. Secondary (contains a quote from him).
- S29. Royal Academy of Engineering, "New Fellows 2026"; https://raeng.org.uk/about-us/fellowship/new-fellows-2026/. Secondary.
- S30. L. Smith, "Industry collaboration yields top Optimization and Engineering paper", CMU Chemical Engineering news, 25 Nov 2025; https://www.cheme.engineering.cmu.edu/news/2025/11/25-grossmann-rosenbrock-prize.html. Secondary.
- S31. M. Ulbrich, "Announcement: Howard Rosenbrock Prize 2024", *Optim. Eng.* 26(4):2307–2309, 2025; 10.1007/s11081-025-10046-5. Secondary, metadata only (not read).
- S32. "Smarter math, better power grids", CMU Chemical Engineering news, 17 Jul 2026; https://www.cheme.engineering.cmu.edu/news/2026/07/16-smarter-math-better-power-grids.html. Secondary (contains a quote from him).
- S33. L. Smith, "Optimizing for early success in research", CMU Chemical Engineering news, 8 Jul 2026; https://www.cheme.engineering.cmu.edu/news/2026/07/08-optimizing-early-success-academia.html. Secondary.
- S34. "How an algorithm can cut the cost of going green", CMU College of Engineering news, 17 Sep 2026; https://engineering.cmu.edu/news-events/news/2026/09/17-cost-of-going-green.html. Secondary.
- S35. INFORMS, "Saul Gass Expository Writing Award" (2025 winner listed; 2026 not yet); https://www.informs.org/Recognizing-Excellence/INFORMS-Prizes/Saul-Gass-Expository-Writing-Award (read 2026-10-10). Secondary.
- S36. INFORMS, "INFORMS Computing Society Prize" (2003: "Ignacio Grossman, Carnegie Mellon University"); https://www.informs.org/Recognizing-Excellence/Community-Prizes/Computing-Society/INFORMS-Computing-Society-Prize (copy saved 2026-10-10). Secondary.
- S37. Mathematics Genealogy Project: I. E. Grossmann (id 36078), R. W. H. Sargent (96603), D. M. Newitt (147410), C. A. Floudas (81417), H. Zhang (311203); https://www.mathgenealogy.org/id.php?id=36078 (read 2026-10-10). Secondary, incomplete.
- S38. Google Scholar profile fiZryxEAAAAJ sorted by publication date; https://scholar.google.com/citations?user=fiZryxEAAAAJ&sortby=pubdate (WebFetch 2026-10-10; rows extracted by the fetch model). Secondary.
- S39. DBLP person 31/5106 via the DBLP SPARQL endpoint (`scripts/dblp_works.py`, 246 records, 2026-10-10). Secondary.
- S40. Crossref REST API: author query for works from 2025-08-01, and about 100 DOI and title lookups (2026-10-10). Secondary.
- S41. arXiv API, au:"Ignacio Grossmann" (16 records, Aug 2020 – Jul 2026; queried 2026-10-10). Secondary (index of primary records).
- S42. OpenAlex works snapshot for author A5056017028 (945 works, 885 distinct titles), saved by a sibling agent in the shared scratch folder on 2026-10-10 and reused read-only for keyword counts. Secondary.
- S43. DataCite API records for the KiltHub reports S14–S16 (2026-10-10). Secondary.

**Search log and unreadable**
- S44. WebSearch, 2 calls (2026-10-10): NAE election (led to S26); the "utopia ... adventure in heuristics" keynote title (no relevant result). Leads only.
- S45. Tecnológico de Monterrey event page for the NAE–Tec conference; https://eventos.tec.mx/s/lt-event?language=en_US&id=a5uUG000000NOrFYAW. Did not load (not read).

**Papers cited and checked** (identifiers checked by me on 2026-10-10 with Crossref, DataCite or the arXiv API; first author, year, title, venue, identifier; "(not read)" marks items checked as records only)
- P1. Grossmann & Sargent 1978, "Optimum design of heat exchanger networks", *Comput. Chem. Eng.* 2(1):1–7; 10.1016/0098-1354(78)80001-5
- P2. Grossmann & Sargent 1978, "Optimum design of chemical plants with uncertain parameters", *AIChE J.* 24(6):1021–1028; 10.1002/aic.690240612
- P3. Grossmann & Sargent 1979, "Optimum Design of Multipurpose Chemical Plants", *Ind. Eng. Chem. Process Des. Dev.* 18(2):343–348; 10.1021/i260070a031
- P4. Grossmann & Santibanez 1980, "Applications of mixed-integer linear programming in process synthesis", *Comput. Chem. Eng.* 4(4):205–214; 10.1016/0098-1354(80)85001-0
- P5. Halemane & Grossmann 1983, "Optimal process design under uncertainty", *AIChE J.* 29(3):425–433; 10.1002/aic.690290312
- P6. Papoulias & Grossmann 1983, "A structural optimization approach in process synthesis—I", *Comput. Chem. Eng.* 7(6):695–706; 10.1016/0098-1354(83)85022-4
- P7. Swaney & Grossmann 1985, "An index for operational flexibility in chemical process design. Part I: Formulation and theory", *AIChE J.* 31(4):621–630; 10.1002/aic.690310412
- P8. Duran & Grossmann 1986, "An outer-approximation algorithm for a class of mixed-integer nonlinear programs", *Math. Program.* 36(3):307–339; 10.1007/BF02592064
- P9. Duran & Grossmann 1987, erratum to P8, *Math. Program.* 39(3):337; 10.1007/BF02592081
- P10. Kocis & Grossmann 1988, EDRC-06-43-88 (= S15); 10.1184/R1/6466841.v1
- P11. Olsbu, Loeken & Grossmann 1988, "A mixed-integer programming model for the design and planning of power systems in oil production platforms", *Eng. Costs Prod. Econ.* 14(4):281–296; 10.1016/0167-188X(88)90033-X
- P12. Pistikopoulos & Grossmann 1988, "Stochastic optimization of flexibility in retrofit design of linear systems", *Comput. Chem. Eng.* 12(12):1215–1227; 10.1016/0098-1354(88)85072-5
- P13. Kocis & Grossmann 1989, "Computational experience with dicopt solving MINLP problems in process systems engineering", *Comput. Chem. Eng.* 13(3):307–315; 10.1016/0098-1354(89)85008-2
- P14. Sahinidis, Grossmann, Fornari & Chathrathi 1989, "Optimization model for long range planning in the chemical industry", *Comput. Chem. Eng.* 13(9):1049–1063; 10.1016/0098-1354(89)87046-2
- P15. Viswanathan & Grossmann 1990, "A combined penalty function and outer-approximation method for MINLP optimization", *Comput. Chem. Eng.* 14(7):769–782; 10.1016/0098-1354(90)87085-4
- P16. Yee & Grossmann 1990, "Simultaneous optimization models for heat integration—II. Heat exchanger network synthesis", *Comput. Chem. Eng.* 14(10):1165–1184; 10.1016/0098-1354(90)85010-8
- P17. Westerberg, Grossmann, Talukdar, Prinz, Fenves & Maher 1990, "Applications of AI in design research at Carnegie Mellon University's EDRC", *Artif. Intell. Eng.* 5(2):110–124; 10.1016/0954-1810(90)90005-O
- P18. Raman & Grossmann 1991, "Relation between MILP modelling and logical inference for chemical process synthesis", *Comput. Chem. Eng.* 15(2):73–84; 10.1016/0098-1354(91)87007-V
- P19. Quesada & Grossmann 1992, "An LP/NLP based branch and bound algorithm for convex MINLP optimization problems", *Comput. Chem. Eng.* 16(10–11):937–947; 10.1016/0098-1354(92)80028-8
- P20. Kondili, Pantelides & Sargent 1993, "A general algorithm for short-term scheduling of batch operations—I. MILP formulation", *Comput. Chem. Eng.* 17(2):211–227; 10.1016/0098-1354(93)80015-F
- P21. Raman & Grossmann 1994, "Modelling and computational techniques for logic based integer programming", *Comput. Chem. Eng.* 18(7):563–578; 10.1016/0098-1354(93)E0010-7
- P22. Hooker, Yan, Grossmann & Raman 1994, "Logic cuts for processing networks with fixed charges", *Comput. Oper. Res.* 21(3):265–279; 10.1016/0305-0548(94)90089-2
- P23. Quesada & Grossmann 1995, "A global optimization algorithm for linear fractional and bilinear programs", *J. Glob. Optim.* 6(1):39–76; 10.1007/BF01106605
- P24. Türkay & Grossmann 1996, "Logic-based MINLP algorithms for the optimal synthesis of process networks", *Comput. Chem. Eng.* 20(8):959–978; 10.1016/0098-1354(95)00219-7
- P25. Grossmann 1983, DRC-06-59-83 (= S14); 10.1184/R1/6467171.v1
- P26. Floudas & Grossmann 1994, EDRC 06-174-94 (= S16); 10.1184/R1/6466703.v1
- P27. Iyer, Grossmann, Vasantharajan & Cullick 1998, "Optimal Planning and Scheduling of Offshore Oil Field Infrastructure Investment and Operations", *Ind. Eng. Chem. Res.* 37:1380–1397; 10.1021/ie970532x (not read)
- P28. Lee & Grossmann 2000, "New algorithms for nonlinear generalized disjunctive programming", *Comput. Chem. Eng.* 24(9–10):2125–2141; 10.1016/S0098-1354(00)00581-0
- P29. Lee, Phalakornkule, Domach & Grossmann 2000, "Recursive MILP model for finding all the alternate optima in LP models for metabolic networks", *Comput. Chem. Eng.* 24(2–7):711–716; 10.1016/S0098-1354(00)00323-9 (not read)
- P30. Jain & Grossmann 2001, "Algorithms for Hybrid MILP/CP Models for a Class of Optimization Problems", *INFORMS J. Comput.* 13(4):258–276; 10.1287/ijoc.13.4.258.9733
- P31. Harjunkoski & Grossmann 2002, "Decomposition techniques for multistage scheduling problems using mixed-integer and constraint programming methods", *Comput. Chem. Eng.* 26(11):1533–1552; 10.1016/S0098-1354(02)00100-X (not read)
- P32. Phalakornkule, Lee, Zhu, Koepsel, Ataai, Grossmann & Domach 2001, "A MILP-Based Flux Alternative Generation and NMR Experimental Design Strategy for Metabolic Engineering", *Metab. Eng.* 3(2):124–137; 10.1006/mben.2000.0165 (not read)
- P33. Zhu, Phalakornkule, Ghosh, Grossmann, Koepsel, Ataai & Domach 2003, "A metabolic network analysis & NMR experiment design tool with user interface-driven model construction for depth-first search analysis", *Metab. Eng.* 5(2):74–85; 10.1016/S1096-7176(03)00023-5 (not read)
- P34. Maravelias & Grossmann 2004, "A hybrid MILP/CP decomposition approach for the continuous time scheduling of multipurpose batch plants", *Comput. Chem. Eng.* 28(10):1921–1949; 10.1016/j.compchemeng.2004.03.016 (not read)
- P35. Grossmann 2004, "Challenges in the new millennium ..." (= S18); 10.1016/j.compchemeng.2004.07.016
- P36. Grossmann 2005, "Enterprise-wide optimization: A new frontier in process systems engineering" (= S19); 10.1002/aic.10617
- P37. Goel & Grossmann 2006, "A Class of stochastic programs with decision dependent uncertainty", *Math. Program.* 108(2–3):355–394; 10.1007/s10107-006-0715-7 (not read)
- P38. Bonami, Biegler, Conn, Cornuéjols, Grossmann, Laird, Lee, Lodi, Margot, Sawaya & Wächter 2008, "An algorithmic framework for convex mixed integer nonlinear programs", *Discrete Optim.* 5(2):186–204; 10.1016/j.disopt.2006.10.011 (not read)
- P39. Caballero & Grossmann 2008, "An algorithm for the use of surrogate models in modular flowsheet optimization", *AIChE J.* 54(10):2633–2650; 10.1002/aic.11579 (not read)
- P40. Castro, Harjunkoski & Grossmann 2009, "New Continuous-Time Scheduling Formulation for Continuous Plants under Variable Electricity Cost", *Ind. Eng. Chem. Res.* 48(14):6701–6714; 10.1021/ie900073k (not read)
- P41. Castro, Grossmann & Rousseau 2010, "Decomposition Techniques for Hybrid MILP/CP Models applied to Scheduling and Routing Problems", Springer Optimization and Its Applications, pp. 135–167; 10.1007/978-1-4419-1644-0_4 (not read)
- P42. Grossmann & Guillén-Gosálbez 2010, "Scope for the application of mathematical programming techniques in the synthesis and planning of sustainable processes", *Comput. Chem. Eng.* 34(9):1365–1376; 10.1016/j.compchemeng.2009.11.012 (not read)
- P43. Martín & Grossmann 2011, "Energy optimization of bioethanol production via gasification of switchgrass", *AIChE J.* 57:3408–3428; 10.1002/aic.12544 (not read)
- P44. Ahmetović & Grossmann 2011, "Global superstructure optimization for the design of integrated process water networks", *AIChE J.* 57:434–457; 10.1002/aic.12276 (not read)
- P45. Mitra, Grossmann, Pinto & Arora 2012, "Optimal production planning under time-sensitive electricity prices for continuous power-intensive processes", *Comput. Chem. Eng.* 38:171–184; 10.1016/j.compchemeng.2011.09.019 (not read)
- P46. Grossmann 2012, "Advances in mathematical programming models for enterprise-wide optimization", *Comput. Chem. Eng.* 47:2–18; 10.1016/j.compchemeng.2012.06.038 (not read)
- P47. Grossmann & Trespalacios 2013, "Systematic modeling of discrete-continuous optimization models through generalized disjunctive programming", *AIChE J.* 59(9):3276–3295; 10.1002/aic.14088 (not read by me; see 01)
- P48. Biegler & Grossmann 2004, "Retrospective on optimization", *Comput. Chem. Eng.* 28(8):1169–1192; 10.1016/j.compchemeng.2003.11.003 (not read by me; see 01)
- P49. Martín & Grossmann 2013, "Optimal use of hybrid feedstock, switchgrass and shale gas for the simultaneous production of hydrogen and liquid fuels", *Energy* 55:378–391; 10.1016/j.energy.2013.04.005 (not read)
- P50. Cafaro & Grossmann 2014, "Strategic planning, design, and development of the shale gas supply chain network", *AIChE J.* 60:2122–2142; 10.1002/aic.14405 (not read)
- P51. Yang, Grossmann & Manno 2014, "Optimization models for shale gas water management", *AIChE J.* 60(10):3490–3501; 10.1002/aic.14526 (not read)
- P52. Grossmann & Westerberg 2000 (= S17); 10.1002/aic.690460902
- P53. Grossmann, Calfa & Garcia-Herreros 2014 (= S20); 10.1016/j.compchemeng.2013.12.013
- P54. Zhang, Morari, Grossmann, Sundaramoorthy & Pinto 2016, "An adjustable robust optimization approach to scheduling of continuous industrial processes providing interruptible load", *Comput. Chem. Eng.* 86:106–119; 10.1016/j.compchemeng.2015.12.018 (not read)
- P55. Zhang, Grossmann & Lima 2016, "On the relation between flexibility analysis and robust optimization for linear systems", *AIChE J.* 62:3109–3123; 10.1002/aic.15221 (not read)
- P56. Floudas & Pistikopoulos 2015, "Professor Ignacio E. Grossmann—Tribute", *Comput. Chem. Eng.* 72:1–2; 10.1016/j.compchemeng.2014.09.001 (not read)
- P57. Doherty, Grossmann & Pantelides 2016, "A tribute to professor Roger Sargent: Intellectual leader of process systems engineering", *AIChE J.* 62(9):2951–2958; 10.1002/aic.15425 (not read)
- P58. Lara, Mallapragada, Papageorgiou, Venkatesh & Grossmann 2018, "Deterministic electric power infrastructure planning: Mixed-integer programming model and nested decomposition algorithm", *Eur. J. Oper. Res.* 271(3):1037–1054; 10.1016/j.ejor.2018.05.039 (not read)
- P59. Kronqvist, Bernal, Lundell & Grossmann 2019, "A review and comparison of solvers for convex MINLP", *Optim. Eng.* 20(2):397–455; 10.1007/s11081-018-9411-8 (not read by me; see 01)
- P60. Grossmann & Harjunkoski 2019 (= S21); 10.1016/j.compchemeng.2019.04.028
- P61. Hubbs, Perez, Sarwar, Sahinidis, Grossmann & Wassick 2020, "OR-Gym: A Reinforcement Learning Library for Operations Research Problems"; arXiv:2008.06319 (not read)
- P62. Hubbs, Li, Sahinidis, Grossmann & Wassick 2020, "A deep reinforcement learning approach for chemical production scheduling", *Comput. Chem. Eng.* 141:106982; 10.1016/j.compchemeng.2020.106982 (not read)
- P63. Chen, Johnson, Bernal, Valentin, Kale, Bates, Siirola & Grossmann 2022, "Pyomo.GDP: an ecosystem for logic based modeling and optimization development", *Optim. Eng.* 23(1):607–642; 10.1007/s11081-021-09601-7 (not read)
- P64. Grossmann 2021, *Advanced Optimization for Process Systems Engineering*, Cambridge University Press; 10.1017/9781108917834 (not read)
- P65. Grossmann 2021, chapter "Constraint Programming", in P64, pp. 103–108; 10.1017/9781108917834.012 (not read)
- P66. Kakkad, Grossmann, Springub, Galanopoulos, Salsano de Assis, Tran & Wassick 2024, "Iterative MILP algorithm to find alternate solutions in linear programming models", *Optim. Eng.* 25(4):2401–2424; 10.1007/s11081-024-09887-3 (not read)
- P67. Li, Bernal, Furman, Duran & Grossmann 2021, "Sample average approximation for stochastic nonconvex mixed integer nonlinear programming via outer-approximation", *Optim. Eng.* 22(3):1245–1273; 10.1007/s11081-020-09563-2 (not read)
- P68. Furman & Grossmann 2021, "A biographical review of the research and impacts of Marco Duran", *Optim. Eng.* 22(3):1233–1244; 10.1007/s11081-021-09632-0 (not read)
- P69. Chattopadhyay, Karthikeyan, Gandhi, Grossmann & Torres 2025, "Optimal Retrofit of Carbon Capture and Electrification Technologies in Oil Refineries for Reducing Direct CO2 Emissions", *Ind. Eng. Chem. Res.* 64:10131–10147; 10.1021/acs.iecr.4c04995 (not read)
- P70. Shikha, Guisso, Robert, Dkhili, Kumar & Grossmann 2025, "Computational Strategies for RTN Model for Supply Logistics of Carbon Dioxide for Carbon Capture and Storage", *Ind. Eng. Chem. Res.* 64:11515–11530; 10.1021/acs.iecr.5c00695 (not read)
- P71. Ovalle, Seth, Kitchin, Laird & Grossmann 2025, "GRAPSE: Graph-Based Retrieval Augmentation for Process Systems Engineering", *Systems and Control Transactions* 4:1598–1604 (ESCAPE-35); 10.69997/sct.198790 (not read)
- P72. Ovalle, Biegler, Grossmann, Laird & Dulce Rubio 2025, "Conformal Mixed-Integer Constraint Learning with Feasibility Guarantees", *Advances in Neural Information Processing Systems* 38 (NeurIPS 2025), pp. 89193–89229; 10.52202/085713-2687; arXiv:2506.03531 (not read)
- P73. Trucco, Presser, Cafaro, Grossmann et al. 2025, "A mathematical programming model for the optimal utilization of deep saline aquifers for CO2 storage", *Comput. Chem. Eng.* 203:109343; 10.1016/j.compchemeng.2025.109343 (not read)
- P74. Bonino, Zeballos, Moolya, Laínez-Aguirre, Pinto, Grossmann & Méndez 2025, "A Three-Step Sequential Approach to Optimize the Production and Routing Problem of Complex Industrial Gas Supply Chains", *Ind. Eng. Chem. Res.* 64(45):21669–21683; 10.1021/acs.iecr.5c03144 (not read)
- P75. Kronqvist, Bernal Neira & Grossmann 2026 (= S22); 10.1016/j.ejor.2025.07.016
- P76. Cho & Grossmann 2025, "Two-stage stochastic programming model and solution strategy for proactive planning and reactive operations of resilient power systems under disruptions", *Int. J. Electr. Power Energy Syst.* 173:111419; 10.1016/j.ijepes.2025.111419 (not read)
- P77. Zhang, Grossmann, McKinnon, Knudsen, Garcia Nava & Tomasgard 2025, "Integrated investment, retrofit and abandonment energy system planning with multi-timescale uncertainty using stabilised adaptive Benders decomposition", *Eur. J. Oper. Res.* 325:261–280; 10.1016/j.ejor.2025.04.005 (not read)
- P78. Su, Tang, Grossmann & Huang 2025, "Optimization for refinery-wide scheduling under uncertainty", *Optim. Eng.* 27(2):1231–1264; 10.1007/s11081-025-10048-3 (not read)
- P79. Ovalle, Bhatia, Laird & Grossmann 2026, "A Logic-Based Decomposition for the Global Optimization of the Multiperiod Blending Problem Using Symmetry-Breaking Cuts", *Ind. Eng. Chem. Res.* 65(7):3981–3998; 10.1021/acs.iecr.5c02853 (not read)
- P80. Cho, Tovar-Facio & Grossmann 2026, "Impact of Reliability Formulations on the Optimal Planning and Operation of Power Systems", *IEEE Trans. Power Syst.* 41(2):927–941; 10.1109/tpwrs.2025.3614510 (not read; summarized in S32)
- P81. Vaidya, Dkhili, Yao & Grossmann 2026, "Computational Strategies for Multiperiod Mixed-Integer Nonlinear Programming Model for Optimal Carbon Capture and Storage", *Ind. Eng. Chem. Res.* 65(10):5521–5530; 10.1021/acs.iecr.5c03514 (not read)
- P82. Xu, Robert, Kumar, Méndez & Grossmann 2026, "Integration of Optimization and Discrete-Event Simulation in Supply Logistics of Carbon Dioxide Capture and Storage", *Ind. Eng. Chem. Res.* 65(13):7076–7091; 10.1021/acs.iecr.5c04890 (not read)
- P83. Grossmann & Matos 2026, "Advances in the Optimization of Process Operations – In Memory of Pedro Castro", *Ind. Eng. Chem. Res.* 65(20):10217; 10.1021/acs.iecr.6c02070 (not read)
- P84. Chattopadhyay, Gandhi, Grossmann & Torres 2026, "A novel algorithm for bounding the optimal solutions in multi-time scale decarbonization planning problems involving varying energy prices: Electrification of oil refineries as a case study", *Comput. Chem. Eng.* 213:109752; 10.1016/j.compchemeng.2026.109752 (not read; summarized in S34)
- P85. Hu, Xu, Meng, Yang & Grossmann 2026, "Integrated optimization of layout and cable routing for wind farms: From MINLP to MIQCP formulation and bilevel decomposition method", *Comput. Chem. Eng.* 214:109814; 10.1016/j.compchemeng.2026.109814 (not read)
- P86. Sun, Onyshkevych, Galanopoulos, Salsano de Assis, Springub, Wassick & Grossmann 2026, "Optimal crane scheduling for tankhouse copper processing", *Comput. Chem. Eng.* 211:109654; 10.1016/j.compchemeng.2026.109654 (not read)
- P87. Bonino, Zeballos, Moolya, Laínez-Aguirre, Pinto, Grossmann & Méndez 2026, "Optimization-based decision support for integrated fleet sizing and production-routing in industrial gas logistics", *Comput. Chem. Eng.* 215:109856; 10.1016/j.compchemeng.2026.109856 (not read)
- P88. Trucco, Presser, Cafaro, Grossmann et al. 2026/2027, "Addressing multiphase fluid-dynamics in the optimal design of oil and gas pipeline networks", *Comput. Chem. Eng.* 216:109897; 10.1016/j.compchemeng.2026.109897 (not read)
- P89. Cho & Grossmann 2026, "Optimization Models and Algorithms for Design and Planning of Sustainable Processes and Energy Systems", in *Optimization of Sustainable Process Systems* (Wiley), pp. 155–177; 10.1002/9781394205646.ch6 (not read)
- P90. Cho, Grossmann, Omell & Burgard 2026, "Probabilistic Reliability-Constrained Generation and Transmission Expansion Planning with an Efficient Solution Strategy", SSRN preprint; 10.2139/ssrn.7483163 (not read)
- P91. Li, Ovalle, Póczos, Laird, Grossmann & Peña 2026, "Efficient Convexification of Kolmogorov-Arnold Networks with Polynomial Functional Forms Via a Continuous Graham Scan Ap[proach]" (title truncated in my API printout); arXiv:2604.03871 (not read)
- P92. Ovalle, Laird, Grossmann & Peña 2026, "Fragility of Minimum-Variance Portfolios"; arXiv:2607.18624 (not read)
- P93. Vyas, Laird, Grossmann, Lima, Harjunkoski & Poland 2026, "Optimization models and algorithms for the Unit Commitment problem"; arXiv:2607.19570 (not read)
