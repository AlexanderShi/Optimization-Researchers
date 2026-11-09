# Matteo Fischetti · Research note 04: students, collaborators and mentorship

| Field | Value |
|---|---|
| Researcher | Matteo Fischetti (University of Padova, DEI; born 1958; living), member of the MILP Team. Not Martina Fischetti, a separate researcher and frequent co-author (see §0) |
| Dimension | Research agent 04 of 06 (framework §二): students and collaborators. Supervision style, group habits, lab culture and tacit knowledge |
| Lens | MILP solver engineering and computation (team.json). Routing, railway and wind-farm work counts only as evidence of how he supervises and collaborates |
| Research date | 2026-11-08 |
| Sources consulted | 84: 39 primary (his own web space, his course material, his own or co-authored papers, preprints and decks) and 45 secondary (theses by students and visitors, repository records, colleagues' recollections, databases). Another 8 addresses could not be reached; one of these (Optima 91) was read from a mirror (see Gaps) |
| WebSearch calls | 5 of the 5 allowed. Everything else came from known URLs via curl, WebFetch, the arXiv, Crossref and OpenAlex APIs and the DBLP SPARQL endpoint |
| User-supplied material | None. `references/sources/papers`, `talks`, `essays`, `software` and `publications` hold only `.gitkeep`. `private/` was not opened. No transcript was saved to `talks/`, because no talk was transcribed (see Gaps) |
| Quotation policy | One verbatim quotation (from Salvagnin's acknowledgement, under 15 words), marked as such. Everything else is paraphrase with a PDF-page or slide locator and never appears in quotation marks. Labels the group itself uses as names (*MIPping*, *Old Benders*, a hashtag, a photo caption) are set in italics as names. Every source is open, so the wording can be checked at the locator |

**Tags.** [stated] = Fischetti's own words (slides, papers, homepage). [practice] = what a dated record shows was done (a thesis, a paper, a course file, a repository record). [observed] = what another person reports about him. [inferred] = this agent's reading, to be tested. "Primary" = his own or co-authored text, or a file in his own web space. "Secondary" = anyone else's account: first-hand for its author, secondary about Fischetti. L1–L7 are the seven layers of framework §一. This note serves mainly L7 (organisation), then L4 (execution) and L5 (judging results).

**Locators.** Theses and preprints are cited by PDF page ("PDF p."), since several have no printed page numbers. Slide decks are cited by slide number, which matches the PDF page except in the VeRoLog 2025 deck (footer = PDF page + 1). All files were opened on 2026-11-08.

---

## 0. Labels that must survive into the skill

- **Two Fischettis.** Martina Fischetti (DBLP 166/3608) is a separate researcher. Her joint papers with Matteo start in 2015 [practice, primary]: *Optimal Turbine Allocation for Offshore and Onshore Wind Farms* (Mathematics for Industry, Springer Japan, 2015, DOI 10.1007/978-4-431-55420-2_4, with Monaci); *Heuristic algorithms for the Wind Farm Cable Routing problem* (Applied Energy 278:115617, 2020, DOI 10.1016/j.apenergy.2020.115617, with Cazzaro); *Integrated Layout and Cable Routing in Wind Farm Optimal Design* (Management Science 69(4):2147–2164, 2023, DOI 10.1287/mnsc.2022.4470); *Safe distancing in the time of COVID-19* (EJOR 304(1):139–149, 2023, DOI 10.1016/j.ejor.2021.07.010, with Stoustrup); and EndoWake (arXiv:2609.40157, 2026). Crossref (S45) and arXiv list Martina before Matteo on each of these, while his homepage writes the pair as `M. Fischetti, M. Fischetti` (P1). **Trap:** *Learning MILP Resolution Outcomes Before Reaching Time-Limit* (CPAIOR 2019, LNCS, pp. 275–291, DOI 10.1007/978-3-030-19212-9_18) is by **Martina** Fischetti, Lodi and Zarpellon according to Crossref, but Defeng Liu's 2022 thesis cites it with the bare initial `M. Fischetti` (S37, ref. [39]). Do not credit it to Matteo. No source I read says whether the two are related, so this note asserts no relation.
- **Martina's master's thesis was not supervised by Matteo.** Her Padova thesis (*Mixed Integer Programming Models and Algorithms for Wind Farm Layout*, AA 2013–14) names Michele Monaci as relatore, with Jakob Stoustrup, John-Josef Leth (Aalborg) and Anders Bech Borchersen (Vattenfall) as co-supervisors. Its acknowledgements thank Monaci for following the work from Italy (S34 PDF p. 5). The Aalborg twin thesis lists the same supervisors (S35). Her DTU dissertation won the 2019 EURO Doctoral Dissertation Award (S36). [practice, secondary]
- **Formal versus informal mentorship.** Andrea Lodi was not Fischetti's PhD student. His Bologna thesis (1999) names Martello and Toth as tutors. Its acknowledgement thanks Fischetti, together with Dell'Amico, among the members of the enlarged Bologna group who spent much time with him (S4 PDF p. 7), and MGP lists Lodi under Toth (S42). Michele Monaci, Fischetti's most frequent co-author (25 papers, 2001–2020, DBLP; S44), appears in Lodi's acknowledgement as the one now asking Lodi the kind of questions Lodi once asked Caprara (S4 PDF p. 7), which makes him a younger member of the Bologna group [inferred]. Nothing I read makes him Fischetti's student. Defeng Liu (PhD, Polytechnique Montréal, 2022) had Lodi as his only director; Fischetti was a co-author (S37 PDF pp. 3, 5). Dario Palasgo (PhD, Padova, 2026) had Roberto Roberti as advisor (S38). [practice]
- **Doctoral advisees confirmed.** Bertacco (2005), Salvagnin (2009) and Zanette (2009) are confirmed by thesis title pages (S1–S3), and the latter two also by IRIS records naming Fischetti as advisor (S38). Ivan Luzzi's PhD dissertation (Dipartimento di Metodi Quantitativi, Padova, 2003) is described as such in a co-authored preprint (P26, ref. [25]), but I read no page that names its advisor. The 2004 report version names Matteo Fischetti and Ivan Luzzi as its two authors (P39 PDF p. 1). A 1998 file named as Bettin's doctoral thesis has no title page or acknowledgement in its text layer, so its degree type and Fischetti's role are not established (S5).
- **His own PhD advisor is not established.** MGP has no record of Fischetti: the quick search returned 0 records, and the site has been in partial recovery since 21 October 2026. Toth's MGP record (id 79649) lists seven students, and Fischetti is not among them (S42). His homepage records a PhD in Ingegneria dei Sistemi (Bologna, 1987), the 1987 ORSA prize for the best PhD dissertation on transportation, and first papers (1986–1989) with Martello and Toth (P1). The skill must not describe him as Toth's student. The sibling note 06 reaches the same result independently.

---

## 1. The supervision record

### 1.1 Doctoral theses in his dissertations folder (P2) and in IRIS (S38)

| Student | Degree, place, dates | Thesis | Fischetti's role (source) | Chapters that became papers (verified identifiers) | What it shows for this lens |
|---|---|---|---|---|---|
| Livio Bertacco | PhD in Matematica Computazionale (XVIII ciclo), Dip. di Matematica Pura ed Applicata, Padova; dated 30 Dec 2005 | *Exact and Heuristic Methods for Mixed Integer Linear Programs* | Supervisore on the title page (S1 PDF p. 1) | Ch. 2 → Bertacco, Fischetti, Lodi, *A feasibility pump heuristic for general mixed-integer problems*, Discrete Optimization 4(1):63–76, 2007, DOI 10.1016/j.disopt.2006.10.001. Ch. 3 → Bertacco, Brunetta, Fischetti, *The Linear Ordering Problem with cumulative costs*, EJOR 189(3):1345–1357, 2008, DOI 10.1016/j.ejor.2006.03.071 (preprint P29). Ch. 4 (*Branching on General Disjunctions*) → no paper found (§7) | The student extends the advisor's newest method (FP, 2005) to general integers. FP-cplex and FP-xpress are built on each commercial solver and compared with that same solver (§3.3) |
| Domenico Salvagnin | PhD in Matematica Computazionale (XXI ciclo), Padova. Acknowledgement dated 25 Jan 2009. IRIS: accepted 2009-01-27, advisor Fischetti, hdl 11577/3425690. Defended 26 Mar 2009 (his CV, S39) | *Constraint Programming Techniques for Mixed Integer Linear Programs* | Supervisor (S2 PDF pp. 1, 3; S38) | Ch. 2 → Fischetti, Salvagnin, *Pruning Moves*, INFORMS J. Comput. 22(1):108–119, 2010, DOI 10.1287/ijoc.1090.0329. Ch. 3 → Fischetti, Salvagnin, Zanette, *A note on the selection of Benders' cuts*, Math. Prog. 124(1–2):175–182, 2010, DOI 10.1007/s10107-010-0365-7. Ch. 4 → *Feasibility pump 2.0*, MPC 1(2–3):201–222, 2009, DOI 10.1007/s12532-009-0007-3. App. A → *Fast Approaches to Improve the Robustness of a Railway Timetable*, Transp. Sci. 43(3):321–335, 2009, DOI 10.1287/trsc.1090.0264 | His 2005 master's thesis, *A dominance procedure for Integer Programming* (S39), led to *Pruning Moves*, whose stated starting point is the Fischetti–Toth dominance procedure of the 1980s (S40): *A new dominance procedure for combinatorial optimization problems*, ORL 7(4):181–187, 1988, DOI 10.1016/0167-6377(88)90025-9. The advisor's old idea is handed to a student to re-examine with modern MIP tools [inferred] |
| Arrigo Zanette | Scuola di Dottorato in Scienze Matematiche, indirizzo Matematica Computazionale (XXI ciclo), Padova; dated 3 Nov 2008. IRIS: accepted 2009-01-28, advisor Fischetti, hdl 11577/3425623 | *Three Topics in Mixed Integer Programming* | Supervisore (S3 PDF p. 1; S38) | Ch. 2 → Zanette, Fischetti, Balas, *Lexicography and degeneracy: can a pure cutting plane algorithm work?*, Math. Prog. 130(1):153–176, 2011, DOI 10.1007/s10107-009-0335-0. Chs. 3–4 are the two papers he shares with Salvagnin. Also, outside the thesis: Balas, Fischetti, Zanette, *On the enumerative nature of Gomory's dual cutting plane method*, Math. Prog. 125(2):325–351, 2010, DOI 10.1007/s10107-010-0392-4 | He visited Egon Balas at Carnegie Mellon, and Balas co-authored ch. 2 (S3 PDF p. 9). The ch. 2 paper is the one student-first author list found before 2020 (§1.3) |
| Ivan Luzzi | PhD dissertation, Dip. di Metodi Quantitativi, Padova (2003), per P26 ref. [25]. Report version dated 1 Apr 2004 | *Exact and heuristic methods for nesting problems* | Co-author of the report version (P39). Advisor role not stated in what I read | → Fischetti, Luzzi, *Mixed-integer programming models for nesting problems*, J. Heuristics 15(3):201–226, 2009, DOI 10.1007/s10732-008-9088-9 | The thesis proposes a file format for nesting instances, converts the literature instances to it and publishes them on a website, NESTLIB (P39 PDF p. 72). Luzzi's MPL notes still sit in the OR1 course folder (P5) |
| (Bettin) | File `tesi_dottorato_Bettin_1998.pdf`, in Italian, on pallet loading | No title page in the text layer | Not established | none found | Listed only for completeness (S5) |
| *Not his student:* Andrea Lodi | PhD Bologna, AA 1996–99; acknowledgement dated 15 Jan 2000 | *Algorithms for Two-Dimensional Bin Packing and Assignment Problems* | Thanked as a member of the enlarged Bologna group (S4 PDF p. 7) | — | His thesis file sits in Fischetti's dissertations folder (P2), and its acknowledgement text was later reused by Bertacco (§2.1) |

The post-2020 PhD-level pattern is different. Cavaliere, Palasgo and Liu publish with Fischetti, but the records read name other advisors (Palasgo: Roberti; Liu: Lodi), or none was found (Cavaliere: no thesis record found) [practice]. Salvagnin's CV lists one PhD student he supervised (Matteo Zanella, 2025) and five dissertation committees at Liège and TU Berlin (S39).

### 1.2 Laurea and master's theses (Fischetti as relatore unless stated)

Sources: P2, the dissertations folder (29 files; last modified 2021-12-14), and S33, the Padua thesis archive (12 records for the query `Fischetti Matteo` on 2026-11-08). The two overlap only partly, so neither is a full list.

| Year (AA) | Student | Thesis (short title) | Where, and with whom | What came of it (verified) |
|---|---|---|---|---|
| 1998–99 | David Ciprian | Frequency planning for large mobile radio networks (S7) | Padova | Context for Fischetti, Lepschy, Minerva, Romanin Jacur, Toto, *Frequency Assignment in Mobile Radio Systems Using Branch-and-Cut Techniques*, EJOR 123:241–255, 2000 (title and venue checked against P1 [46] only, not in Crossref). No paper with Ciprian |
| 2000 | Cristiano Saturni | GA for packing with an uncertain future (S6) | Done at Aberdeen (ERASMUS, supervised there by Ken Brown); written in Padova under Fischetti (S6 PDF pp. 11–13) | Later a research topic of a different kind: Fischetti, Saturni, *Mixed-Integer Cuts from Cyclic Groups*, Math. Prog. 109(1):27–53, 2007, DOI 10.1007/s10107-006-0726-4 (IPCO 2005 version DOI 10.1007/11496915_1). The September 2005 preprint gives both authors at DEI Padova (P28 PDF p. 1) |
| 2000–01 | Carlo Polo | Heuristics for the design of a UMTS interconnection network (S8) | Padova | Fischetti, Polo, Scantamburlo, Networks 44(2):61–72, 2004, DOI 10.1002/net.20017 |
| 2001–02 | Massimo Scantamburlo | DRT, a general method for MIPs, on CPLEX 7.0 and GLPK (S11) | Padova | Same Networks 2004 paper |
| 2003 | Giuseppe Andreello | New separation procedures for ILP: {0,1/2}-cuts inside CPLEX (S9) | Padova | Andreello, Caprara, Fischetti, *Embedding {0, ½}-Cuts in a Branch-and-Cut Framework: A Computational Study*, INFORMS J. Comput. 19(2):229–238, 2007, DOI 10.1287/ijoc.1050.0162, building on Caprara, Fischetti, *{0, 1/2}-Chvátal-Gomory cuts*, Math. Prog. 74(3):221–235, 1996, DOI 10.1007/bf02592196 |
| 2003 | Gianni Codato | *A Combinatorial Approach to Benders' Decomposition* (in Italian; text layer not extractable, so not read; S12) | Padova | Codato, Fischetti, *Combinatorial Benders' Cuts for Mixed-Integer Linear Programming*, Oper. Res. 54(4):756–766, 2006, DOI 10.1287/opre.1060.0286. The thesis won AIRO's 2003 Camerini-Carraresi prize (P22 PDF p. 4) |
| 2003 | Roberto De Franceschi | SERR refinement heuristic for VRP (S10) | Supervised by Fischetti and by Paolo Toth of Bologna (S10 PDF p. 4) | De Franceschi, Fischetti, Toth, *A new ILP-based refinement heuristic for Vehicle Routing Problems*, Math. Prog. 105(2–3):471–499, 2006, DOI 10.1007/s10107-005-0662-8 (preprint received May 2004, P27) |
| 2003–04 | Luigi Bancaro; Davide Baracco | An LP-based MIP heuristic with open-source software; the CPLEX-based FP connected to other LP solvers (S13, S14) | Padova | none found |
| 2004 | Michele Aldà (tesina) | Heuristics for VRP (S15) | Padova | none |
| 2003–04 | Michele Gallina | Moulding-plant scheduling, after a short internship at the company (S16 PDF p. 3) | Company internship | none |
| 2007–08 | Tommaso Normani; Nicola Zago | C interface for COIN-OR CBC; the ellipsoid method in LP (S17, S18) | Padova | Zago later helped a 2011 student with suggestions and corrections (S25 PDF p. 65) |
| 2010–11 | Luca Zoggia | Interval scheduling (relatore Romanin Jacur; Fischetti correlatore) (S25) | Padova | none |
| 2012 | Lucia Petterle | Computational analysis of SVM models (S19) | Padova | Credited, not co-author: Fischetti, *Fast training of Support Vector Machines with Gaussian kernel*, Discrete Optimization 22:183–194, 2016, DOI 10.1016/j.disopt.2015.03.002 (§1.3) |
| 2012 | Giorgio Sartor | Smart home appliances by MILP (S20) | Hosted by M31 Italia S.r.l.; day-to-day oversight by the PhD graduate Arrigo Zanette (S20 PDF pp. 3, 76) | Fischetti, Sartor, Zanette, *MIP-and-refine matheuristic for smart grid energy management*, ITOR 22(1):49–59, 2015, DOI 10.1111/itor.12034 |
| 2012–13 | Gianluca Frison | Numerical methods for model predictive control (S26) | Padova | Outside his core area; Fischetti accepted to supervise it (S26 PDF p. 3) |
| 2013–14 | Paolo Marchezzolo | An ILP heuristic for the TSP (S27) | Padova | none |
| 2013–14 | Giovanni Di Liberto; Marco Collautti | DASH (switching heuristics); SNNAP (algorithm portfolios) (S28, S29) | Done at the Cork Constraint Computation Centre (ERASMUS). Co-advisors Yuri Malitsky and Barry O'Sullivan; Malitsky proposed DASH's topic (S28 PDF p. 5) | none with Fischetti |
| 2014–15 | Nicola Menon | TSPTW heuristics with proximity search; correlatore Monaci (S30) | Padova | none |
| 2014–15 | Alessandro Beltramin | Modern B&C solvers: CPLEX against Gurobi through a CPLEX-to-Gurobi C shim; UFL with callbacks, hard fixing and local branching (S31) | Padova | none |
| 2018 | Iacopo Mandatelli | Improved training methods for neural networks: minibatch persistency, adaptive Nesterov (S21) | Padova | arXiv:1806.07353 with Salvagnin, still listed as a technical report on his homepage in 2026 (§7) |
| 2019 | Matteo Stringher | Unconventional training of DNNs (S22) | Padova, on NVIDIA-donated GPUs | Fischetti, Stringher, *Embedding Simulated Annealing within Stochastic Gradient Descent*, CCIS (OLA 2021), pp. 3–13, 2021, DOI 10.1007/978-3-030-85672-4_1 |
| 2019–20 | Marco Calandro; Davide Martini | Metaheuristic frameworks for DNN training; a neural network for the knapsack problem (S23, S32) | Padova | none found |
| 2019–20 | Andrea Bugin | Ambulance deployment for the ULSS 8 Berica health district (S24) | Padova, local health authority data | none found |
| 2020–21 | Simone Dalla Valle | Fast ATSP procedures for last-mile delivery (archive record only, no full text; S33) | Padova | not read |

### 1.3 How a thesis becomes a paper, and how the student is credited [practice, primary]

- **Stated in the paper.** The Codato–Fischetti preprint says the paper is based on the first author's master's thesis, which won AIRO's 2003 Camerini-Carraresi prize, and that it was presented at IPCO X (New York, June 2004) (P22 PDF p. 4). The smart-grid paper cites Sartor's thesis as ref. [8] (P24). The nesting paper cites Luzzi's dissertation by the URL of its PostScript file in the homepage folder (P26 PDF p. 34). The homepage folder thus works as a citable archive.
- **Credited, not co-author.** The 2016 SVM paper has Fischetti as sole author. It says the telecommunication interpretation it uses was proposed together with Lucia Petterle in her master's thesis, and cites the thesis (P23 PDF p. 4). The other master's students whose work became papers were made co-authors (Codato, Polo, Scantamburlo, Andreello, De Franceschi, Sartor, Mandatelli, Stringher).
- **Code shared across the Padova–Bologna boundary.** The 2-level local-branching paper thanks Andrea Lodi for providing his implementation of the local-branching framework (P25 PDF p. 16).
- **Author order.** Through the 2019 preprints nearly every paper with a student is in alphabetical order (Codato; De Franceschi; Fischetti–Polo–Scantamburlo; Andreello–Caprara–Fischetti; Bertacco–Fischetti–Lodi; Fischetti–Salvagnin–Zanette; Fischetti–Sartor–Zanette; Fischetti–Mandatelli–Salvagnin; Fischetti–Stringher). The one student-first exception found is Zanette, Fischetti, Balas (Math. Prog. 2011). A non-alphabetical paper of another kind is Brigadoi, Salvagnin, Fischetti, Cooper, *Array Designer: automated optimized array design for functional near-infrared spectroscopy*, Neurophotonics 5(3), 2018, DOI 10.1117/1.NPh.5.3.035010, whose order looks like the neuroimaging habit of putting the senior author last [inferred]. From 2020, junior authors usually come first: Cavaliere, Bendotti, Fischetti (MPC 14(4):749–779, 2022, DOI 10.1007/s12532-022-00224-2; preprint of 14 June 2022, P31); Liu, Fischetti, Lodi (AAAI 36(4):3796–3803, 2022, DOI 10.1609/aaai.v36i4.20294); Salvagnin, Roberti, Fischetti (MPC 17(1):111–139, 2024, DOI 10.1007/s12532-024-00269-5); Roberti, Salvagnin, Fischetti (JORS 76(10):2060–2070, 2025, DOI 10.1080/01605682.2025.2451738); Palasgo, Fischetti, Roberti (AIRO Springer Series, pp. 75–86, 2025, DOI 10.1007/978-3-031-85894-9_6). Cavaliere, Fischetti, Roberti, Salvagnin (EJOR 329(1):96–111, 2026, DOI 10.1016/j.ejor.2025.07.034) fits both conventions. [practice] No source states the rule or the reason for the shift. A contradiction in Liu's case is kept below.

---

## 2. Supervision style, according to the students (all [observed], secondary)

### 2.1 First, how good is the evidence?

Bertacco's acknowledgement (2005) is not independent testimony about Fischetti's group. Its central sentence is identical, word for word, to the sentence in Lodi's 1999 Bologna acknowledgement about the Martello–Toth group (one pronoun changed). The sentence says the advisor built, over the years, a group where exciting research happens in a special and friendly setting, and the author is indebted to the whole enlarged group. Three more sentences are shared word for word: the thanks to department staff for supporting research so kindly, the closing thanks to the family, and the opening line that first thanks the advisor (or advisers). I compared both texts in full, and the four fragments occur verbatim in both (S1 PDF p. 5; S4 PDF p. 7). Lodi's thesis file sits in Fischetti's dissertations folder (P2). [practice, inferred: Bertacco used Lodi's acknowledgement as a template]. The parts of Bertacco's acknowledgement that are not in Lodi's do count as his own: Fischetti introduced him to OR and combinatorial optimization, and his suggestions and encouragement were indispensable. He also names brainstorming with fellow students, thesis discussions with Lodi and Lorenzo Brunetta, and the ADONET doctoral schools (S1 PDF p. 5).

### 2.2 What the students say

- **Salvagnin (PhD 2009).** He calls Fischetti's advice, ideas, support and manner fundamental. He describes the DEI OR group as a unique environment and thanks colleagues at the Padova mathematics department and at DEIS Bologna. He writes that Fischetti once jokingly called himself **"maestro di vita"** (the note's one verbatim quotation; roughly, a teacher of life). He adds that in part Fischetti really was one, and hopes the collaboration will continue (S2 PDF p. 9). It did: 24 joint papers from 2007 to 2026 (S44).
- **Zanette (PhD 2008/09).** He credits Fischetti's deep scientific understanding and enthusiasm for research, and an uncommonly friendly environment that made the PhD enjoyable. He names Salvagnin as co-author of two chapters, thanks Monaci and Valentina Cacchiani for help with the railway data, remembers Lorenzo Brunetta as someone the group misses (the thesis does not say what happened), and thanks Balas for the Carnegie Mellon visit (S3 PDF p. 9).
- **Petterle (MSc 2012).** She describes him as extremely available and kind. He put up with her many e-mails and her repeated discouragement without losing patience, and instead motivated her subtly and constantly. She thanks him for his trust (S19 PDF p. 145). This is the only account of supervision by e-mail and of coaching through discouragement.
- **Sartor (MSc 2012).** In English he ranks Fischetti as the best supervisor a student could have. In Italian he says Fischetti trusted him from the start and followed him with great availability. Zanette followed the whole project closely, and M31 Italia hosted him (S20 PDF pp. 3, 76).
- **Bugin (MSc 2020).** He calls Fischetti an excellent teacher and a still better person, who gave him the chance to do the thesis and was always available with advice and support (S24 PDF p. 7).
- **Beltramin (MSc 2016).** Availability, valuable advice and above all the passion for the subject that he passed on to the students (S31 PDF p. 133).
- **Frison (MSc 2013).** Fischetti agreed to supervise him and was always very accommodating of his limited availability (S26 PDF p. 3).
- **Collautti (MSc 2014, written at Cork).** Fischetti gave continuous support and encouragement from a distance, but Yuri Malitsky was the real supervisor of the work (S29 PDF p. 7). **Di Liberto** (same year and lab) thanks Fischetti for advice and suggestions; Malitsky proposed the topic (S28 PDF p. 5).
- **Saturni (2000, written at Aberdeen).** He thanks Fischetti for advice, trust and esteem; Ken Brown supervised the project in Aberdeen (S6 PDF p. 11).
- **De Franceschi (2003), Aldà (2004), Zoggia (2011).** Thanks for supervision, shared with Toth (S10 PDF p. 4); help and unconditional availability (S15 PDF p. 44); availability, material provided and support, shared with Romanin Jacur (S25 PDF p. 65).
- **Liu (PhD 2022, Montréal; co-author, not advisee).** He thanks his co-authors, Fischetti among them, for trust, patience and commitment. The thanks are collective and say nothing about Fischetti in particular (S37 PDF p. 5).
- **What no thesis says.** No acknowledgement describes meeting rhythm, group seminars, code review, rounds of feedback on writing, or criticism. Mandatelli (2018) and Calandro (2020) carry no acknowledgement, and Stringher's thesis thanks only NVIDIA for the GPU donation (S22 PDF p. 57). [practice]

### 2.3 Reading the record [inferred, to be tested]

Two modes of supervision show in the record.

- **The doctoral track** (about 2003–2009). The group is small: Fischetti, two or three PhD students, junior colleagues (Brunetta, then Monaci) and the Bologna collaborators. Each thesis is assembled from co-authored papers, and the student usually extends a method the advisor had just published or once proposed: feasibility pump → general-integer FP and FP 2.0; the 1988 dominance test → pruning moves; Gomory's method revisited with Balas.
- **The master's track** (2000–2021). The traits the students name are availability, trust and encouragement. Students may bring their own topics (Frison's MPC) or do the work abroad (Aberdeen, Cork, Aalborg). Day-to-day guidance is often delegated to a former PhD student (Zanette for Sartor) or to the foreign host (Malitsky, Brown), with Fischetti as the home anchor who endorses the work.

Neither mode is described as such by any source.

---

## 3. Group habits: what the theses and papers show (practice)

1. **A PhD thesis is a bundle of papers.** Salvagnin's chapters keep each paper's own acknowledgements and funding lines: Padova Progetto di Ateneo CPDA051592 (integrating IP and CP), the EC FET project ARRIVAL (FP6-021235-2) and PRIN 2006 (S2 PDF pp. 41, 74). His railway appendix thanks Toth, Caprara and Cacchiani for the nominal timetables, and three anonymous referees (S2 PDF p. 107). A joint paper of two students of the same cycle appears as a chapter in both theses: the MIS–Benders and railway papers are in both Salvagnin's and Zanette's (S2, S3 tables of contents). [practice, secondary]
2. **Templates are handed down.** Bertacco's acknowledgement reuses Lodi's (§2.1). The text layer of PDF p. 1 of Salvagnin's thesis holds Bertacco's 2005 title page, with Bertacco's name, the XVIII ciclo, Conforti as coordinator and the date 30 Dec 2005, underneath Salvagnin's own (S2 PDF p. 1, two font sets). Salvagnin's and Zanette's inner title pages share the same misspelling of the supervisor's name, *Fishetti* (S2 PDF p. 3; S3 PDF p. 3). [practice, inferred: each student started from the previous student's files]
3. **Build on a commercial solver's callable library, and use that same solver as the baseline.**
   - 2001–02: Scantamburlo's DRT works on CPLEX 7.0 and GLPK (S11 PDF p. 2).
   - 2003: De Franceschi writes C++ on ILOG Concert (S10).
   - 2004–05: Bertacco builds FP-cplex against ILOG CPLEX 9.1 and FP-xpress against Xpress 16.01.05 on MIPLIB 2003, on a Pentium IV 2.4 GHz with 512 MB and a 3600 s limit (S1 PDF p. 31).
   - 2008: Salvagnin runs CPLEX 11.0 with default options as the black box on a Core2 Q6600 (2.4 GHz, 4 GB) (S2 PDF pp. 32, 52). For FP 2.0's propagation engine he borrows the advised-propagation design of the CP solver Gecode (S2 PDF p. 68). Zanette uses MIPLIB 3.0 and 2003 pure ILPs (S3).
   - 2014–15: the Steiner codes all run on CPLEX 12.6 (P21 slide 3). Beltramin notes that using callbacks switches off CPLEX's proprietary dynamic search (S31 PDF p. 29).
   - 2026: the AIROyoung tutorial teaches CPLEX's newer generic-callback contexts and calls the older names old-style (P11 slides 3–5).
4. **Master's theses that bridge solvers.** An open-source LP-based heuristic (Bancaro, 2004). The CPLEX-based FP connected to other LP solvers (Baracco, 2004). A C interface to COIN-OR CBC (Normani, 2008). A shim that redirects CPLEX C-library calls to Gurobi so that the same code can be compared on both (Beltramin, 2016; S31 PDF pp. 1–3). [practice, secondary]
5. **Comparisons are taught and tooled.**
   - The 2019–20 OR2 plan has a lecture on computational comparisons with random seeds and performance profiles (P7).
   - The OR2 checklist gives a point for extensive use of performance profiles (P6).
   - A performance-profile script by Salvagnin (2016) sits in the course folder. Its read-me cites Dolan and Moré, *Benchmarking optimization software with performance profiles*, Math. Prog. 91(2):201–213, 2002, DOI 10.1007/s101070100263. Its usage example sets a 2 s shift, a 3600 s time limit and a maximum ratio of 20 (P9). The script header carries a version date of 20 April 2026, so it is still maintained. The read-me marks the script for internal use and not for distribution, so the skill should describe it, not reproduce it.
   - The AIRO 2012 deck re-runs the comparison with Fischetti, Salvagnin and Zanette (Transp. Sci. 2009) at the same 1200 s limit (P16 slide 14).
   - The DIMACS deck says there was no single winner across the many variants and scores, and only claims first place in many categories (P21 slide 4). [practice and stated, primary]
6. **The group enters computational competitions.** Winner of the 11th DIMACS Implementation Challenge (Steiner trees, 2014), with Vienna (P1). Finalist in the MIP 2022 computational competition with Salvagnin and Roberti (S39). The joint paper is *Thinning out Steiner trees: a node-based model for uniform edge costs*, MPC 9(2):203–229, 2017, DOI 10.1007/s12532-016-0111-0.
7. **Industry, data and abroad.** Company internships (Gallina; Sartor at M31 Italia). Public-health data (Bugin). ERASMUS theses abroad (Saturni, Collautti, Di Liberto; Martina Fischetti with Monaci). A PhD visit to a senior collaborator (Zanette to Balas). European doctoral schools (Bertacco, ADONET). EU and PRIN projects that fund the chapters (ARRIVAL, PRIN 2006). [practice, secondary]
8. **Course material outlives its authors.** The OR1 folder still holds a former PhD student's MPL notes (Luzzi) and an errata file in Brunetta's name. The OR2 folder holds Salvagnin's performance-profile script (P5, P9). [practice, primary]

---

## 4. Collaborators

### 4.1 The network in numbers [practice, DBLP SPARQL, S44]

88 distinct co-authors. The most frequent, with years of joint papers:

| Co-author | Joint papers | Years | Relation (from the sources in this note) |
|---|---|---|---|
| Michele Monaci | 25 | 2001–2020 | Younger member of the Bologna group (S4); colleague at DEI Padova in 2013 (P38); at Bologna by 2018 (P13 slide 11) |
| Domenico Salvagnin | 24 | 2007–2026 | His PhD student, then DEI colleague (S39) |
| Paolo Toth | 22 | 1987–2006 | Bologna senior; formal relation unknown (§0) |
| Andrea Lodi | 17 | 2001–2022 | Bologna PhD of Martello and Toth (S4) |
| Alberto Caprara | 14 | 1995–2012 | Bologna, Toth's student (S42); died 2012 |
| Egon Balas | 11 | 1992–2012 | Senior collaborator; host of Zanette |
| Ivana Ljubić | 9 | 2005–2019 | Vienna |
| Arrigo Zanette | 8 | 2007–2015 | His PhD student |
| Markus Sinnl | 8 | 2016–2019 | Vienna |
| Juan José Salazar González | 7 | 1995–2003 | La Laguna; visitor to Bologna (S4) |
| Silvano Martello | 6 | 1987–2001 | Bologna senior |
| Martina Fischetti | 4 (DBLP; more on arXiv) | 2018–2026 | See §0 |
| Daniele Vigo | 4 | 1994–1998 | Bologna |
| Leo Kroon | 3 | 2000–2009 | Netherlands Railways and Erasmus University |
| Roberto Roberti | 3 | 2025–2026 | Padova colleague; Palasgo's advisor |

The partners come in overlapping waves: Toth and Martello (Bologna, from 1987); then Caprara, Salazar and Vigo (1994–2003); then Lodi and Monaci (2001–2022); then his own students Salvagnin and Zanette (2007–); then Vienna (2014–2019); then Martina Fischetti, Roberti and Cavaliere (2018–2026). [practice; the wave reading is inferred, and the sibling note 06 draws the same picture]

### 4.2 The Bologna lineage [practice and observed]

- He studied at Bologna (Laurea 1982, PhD 1987) and was assistant professor there in 1990–92 (P1). His first papers (1986–1989) are with Martello and Toth (P1 [2]–[10]).
- The *Memories* section of Optima 91 (2013) describes the Bologna group's working conditions around Caprara: PhD students' desks in the department corridor, a DECstation 5000/240 in the days of CPLEX 1 (Salazar-González, p. 12), and visits arranged without formal proposals, with modest offices that kept visitors visible to the whole group (Pferschy, pp. 11–12) (S41). This describes the group in which Fischetti was formed and worked until 1992. It is not about him.
- The cultural continuity into Padova shows in Bertacco's reuse of Lodi's acknowledgement (§2.1). It also shows in De Franceschi's thesis, co-supervised with Toth, and in the 2-level LB paper running on Lodi's code (§1.3).

### 4.3 The junior-colleague pattern: long co-authorships with younger researchers he did not formally supervise [practice]

- **Caprara.** Prizes with Toth (and Vigo) from Ferrovie dello Stato: FASTER 1994 for very large set covering, FARO 1995 for rostering (P1). *A Heuristic Method for the Set Covering Problem*, Oper. Res. 47(5):730–743, 1999, DOI 10.1287/opre.47.5.730, presented at IPCO 1996 (LNCS DOI 10.1007/3-540-61310-2_6).
- **Lodi.** *Local branching*, Math. Prog. 98(1–3):23–47, 2003, DOI 10.1007/s10107-003-0395-5. With Glover, *The feasibility pump*, Math. Prog. 104(1):91–104, 2005, DOI 10.1007/s10107-004-0570-3. The FP preprint thanks Dimitris Bertsimas for discussions on the role of randomness in rounding (P30, acknowledgements). The earliest FP deck in his slides folder is from Aussois 2004 (P20). The homepage shows the opening slide of the very first FP talk without naming its venue (P1), so the two may or may not be the same talk. *Optimizing over the first Chvátal closure*, Math. Prog. 110(1):3–20, 2007, DOI 10.1007/s10107-006-0054-8.
- **Monaci.** *Exploiting Erraticism in Search*, Oper. Res. 62(1):114–122, 2014, DOI 10.1287/opre.2013.1231. *Proximity search for 0-1 mixed-integer convex programming*, J. Heuristics 20(6):709–731, 2014, DOI 10.1007/s10732-014-9266-x. With Lodi, Salvagnin and Tramontani, *Improving branch-and-cut performance by random sampling*, MPC 8(1):113–132, 2016, DOI 10.1007/s12532-015-0096-0.
- In the 2018–2025 decks, the ongoing-work and joint-work lines name Monaci, and also Salvagnin in 2018 (P13 slide 11; P14 slide 1; P12 PDF p. 11).
- Salvagnin later worked for IBM ILOG CPLEX: scientific consultant in 2014, lead development scientist 2015–17, consultant 2017–19. He then consulted for FICO Xpress (2019–21) and has led department consultancy projects with FICO since 2021 (S39). This is one documented route from the group into commercial solver development. [observed, secondary]

### 4.4 Senior collaborators and peers [practice]

- **Balas.** Eleven papers (1992–2012). The background of the homepage photo wall is Balas's own handwritten notes (P1). Zanette visited him at CMU, and Balas co-authored a chapter of Zanette's thesis (§2.2). At the Balas memorial symposium (Pittsburgh, 28 Oct 2019) Fischetti gave a technical talk on intersection cuts with Monaci, not a personal tribute (P14).
- **Glover** (FP), **Grötschel** (ATSP with time windows, 2000–01), **Pulleyblank**, **Cornuéjols**, and **Liberti and Walsh** (orbital shrinking) appear on the homepage list (P1).

### 4.5 Partner organisations [practice, primary]

- **Netherlands Railways.** *Reinventing Crew Scheduling at Netherlands Railways*, Interfaces 35(5):393–401, 2005, DOI 10.1287/inte.1050.0158, a Wagner Prize finalist. *The New Dutch Timetable: The OR Revolution*, Interfaces 39(1):6–17, 2009, DOI 10.1287/inte.1080.0409, part of the 2008 Edelman Award entry.
- **Ferrovie dello Stato** (the FASTER and FARO competitions); consulting for the World Bank, FS, Agip-Petroli and others (P1).
- **Vienna (2014–2019).** The DIMACS deck says Vienna's team first supplied a set of effective codes. All codes were then re-engineered and re-tuned, new exact and heuristic codes were added, and an initial filter chose which code to run by instance type (P21 slide 3). The December 2017 DNN preprint says Fischetti's research was partly funded by the Vienna WWTF project ICT15-014 (P33, acknowledgements). Joint papers include *Redesigning Benders Decomposition for Large-Scale Facility Location*, Management Science 63(7):2146–2162, 2017, DOI 10.1287/mnsc.2016.2461.
- **Montréal (2017–2022).** Jason Jo, funded by IVADO, co-authored *Deep neural networks and mixed integer linear optimization* (Constraints 23(3):296–309, 2018, DOI 10.1007/s10601-018-9285-6; preprint arXiv:1712.06174). Its acknowledgement thanks Yoshua Bengio and Andrea Lodi for discussions (P33). Liu's local-branching work was supported by Lodi's CERC chair, with Fischetti funded by MiUR (P36, acknowledgements).
- **GPUs.** NVIDIA donated the Titan Xp GPUs used in the 2019–20 theses (S22 PDF p. 57; S23 PDF pp. 40–41).

### 4.6 What colleagues observed (secondary)

- **Woeginger, Optima 91, p. 13** [observed]. After an Aussois talk by Caprara whose last slide reported Berlusconi's latest misdeeds, Fischetti grew worried and told Caprara to be more cautious and diplomatic in his public statements (S41). This is the only observed instance found of advice he gave a junior colleague about public conduct.
- **Lodi, 1999** [observed]. Fischetti was among the senior members of the group who spent much time with him (S4 PDF p. 7).
- **The AIRO 2012 session** [practice]. The deck whose file name reads `in memoriam Alberto Caprara` is a technical talk on the three authors' joint work, *A Lagrangian Heuristic for Robustness, with an Application to Train Timetabling*, Transp. Sci. 46(1):124–133, 2012, DOI 10.1287/trsc.1110.0378 (P16). Fischetti also co-authored the scientific obituary *Alberto Caprara (1968–2012): Scientific Contributions*, Optima 91 (April 2013) pp. 1–11, with Bansal, Lancia, Letchford, Lodi, Monaci, Pferschy, Pisinger, Salazar-González, Sviridenko and Toth (P38). It has eleven authors, so no passage in it is his alone.

---

## 5. Teaching as onboarding: the OR2 pipeline and tutorials for young researchers

- **One running problem, the full ladder** [practice, primary]. The 2019–20 OR2 plan (P7) takes a single problem, the TSP, through every stage, then ends with a lecture on the structure of the *tesina*:
  1. project setup and a TSPLIB parser, then solution plotting;
  2. a CPLEX model, then compact models (MTZ and flow);
  3. a Benders *loop* with SEC generation;
  4. computational comparisons with random seeds and performance profiles;
  5. lazy-constraint and user-cut callbacks;
  6. matheuristics (hard fixing, local branching);
  7. constructive heuristics with GRASP, then metaheuristics (VNS, tabu search, simulated annealing) and genetic algorithms;
  8. MIP heuristics (diving, RINS, local branching, polishing), then a glance at CP and AI.

  The 2021–22 videos follow the same order in 25 lessons; the last two cover the structure of the thesis and the exam rules (P8; not watched).
- **The checklist** (P6, posted 24 May 2023) [practice, primary]. Mandatory: the C project with TSPLIB parser, solution check and plot; GRASP greedy; 2-OPT; tabu search; VNS; the basic CPLEX model without SECs; Benders' loop with SEC separation for integer solutions; branch-and-cut through callbacks; hard fixing; local branching. One point each for: extra-mileage, simulated annealing, a genetic algorithm, patching, posting heuristic solutions with user cuts, extensive performance profiles, and writing style. The maximum is 31 points. Every OR2 student thus builds heuristics, an exact branch-and-cut and matheuristics for one problem in C on CPLEX, and compares them with profiles. The master's theses above draw on this stock.
- **Where the material sits.** All decks cited here are in his slides folder (P3), and the preprints in his papers folder (P4).
- **Course folder** (P5). It provides a CPLEX project template (2020), example C files for lazy and generic callbacks, guides for CPLEX on Windows and Mac and for Gurobi at DEI, and readings: tabu search, VNS, matheuristics surveys, Bixby's MIP-heuristics slides, and a file titled *Metaheuristics—the metaphor exposed*, which I did not open. It also holds a copy of the ministry's 2018 bibliometric threshold tables for the national habilitation (P10). The folder does not say why that copy is there.
- **For young researchers, 2026** [stated, primary]. The AIROyoung tutorial (Padua, 9 Feb 2026) sorts Benders confusion into two parts: papers that announce a new Benders-like scheme refer to the cut loop, while students frightened of implementing Benders refer to the Farkas technicality of computing the cuts (P11 slide 8). He suggests the formula-heavy cut derivation may be why students find Benders too sophisticated (slide 13). He then gives a recipe for letting the solver do the calculations, via reduced costs inside a callback (slide 14). He closes with two points: Benders cuts are easy inside modern branch-and-cut, and Kelley's loop is so slow that stabilization is a must (slide 19).
- **Implementation as part of the result** [stated, primary, repeated]. In ISMP 2018 (P13 slides 4–5) and VeRoLog 2025 (P12 PDF pp. 4–5), he likens describing an algorithm without its implementation to stating a theorem without proof, tagging it *#just_a_computational_conjecture*. In 2006 he said he teaches engineers to use MIP models for their hard problems, and urged them to model the critical steps of their own algorithms as MIPs solved by a general-purpose solver (P19 slide 6). Coining the verb *to MIP* (P19 slide 3) gave the group a word that later appears in paper titles. The ISCO 2014 plenary opens with a mock-gospel account of tree search as it is taught (P18 slide 2). *Old Benders* is the group's name for solving the master to optimality before generating cuts (P17 slide 20).

---

## 6. Tacit knowledge: what students and colleagues knew that the papers do not say

Each item names its source and tag. None of them is stated as a rule anywhere.

1. **Write each chapter as a paper.** It keeps its own acknowledgements, funding lines and referees, and can be shared by two theses (§3.1). [practice, secondary]
2. **Start from the previous student's files.** Title page, acknowledgement and template (§3.2). [practice, inferred]
3. **Implement inside the solver.** Use the CPLEX callable library and callbacks, compare with the same solver in default mode on MIPLIB, and know that callbacks switch off CPLEX's dynamic search (§3.3). [practice]
4. **Compare with performance profiles over random seeds, under one time limit.** The group's own script supplies a time shift and the cap; re-run old competitors at the same limit (§3.5). [practice and stated]
5. **Ask the solver to compute Benders cuts from reduced costs** instead of coding the duality formulas by hand (P11 slide 14). [stated]
6. **Shared vocabulary:** *MIPping* or *to MIP* (turn a hard sub-decision into a MIP and solve it, even heuristically, with a black-box solver); *Old Benders*; *#just_a_computational_conjecture*; and *Deve funzionare!* (Italian for it has to work), the caption under the thumbs-up photo on his homepage (P1). [stated]
7. **Report a competition result as it was.** Say there was no single winner, then say in which categories you came first (P21 slide 4). [stated]
8. **Supervision by proxy.** For a master's student, the daily contact may be a former PhD student or the foreign host (Zanette; Malitsky; Brown) (§2.2). [observed]
9. **Funnel from the OR2 project to the thesis.** The OR2 project builds the skills, and the thesis topic usually comes from the advisor's newest method or an industrial contact (§1.2, §5). [inferred]
10. **Be careful in public.** In the one recorded case, Fischetti advised a junior colleague to be cautious and diplomatic in public statements (S41 p. 13). [observed, secondary, single instance]

---

## 7. Failures, abandoned directions and negative results

- **Bertacco's chapter 4, *Branching on General Disjunctions*.** It proposes two disjunction-selection schemes, each modelled as a MIP and solved by truncated search. Preliminary tests on 15 instances suggest smaller trees, and the chapter lists future work (S1 PDF pp. 62–69). No paper on it appears in Fischetti's homepage list or in his DBLP co-authorship with Bertacco (2 papers, 2007–2008). [practice; why it stopped is not known]
- **The long Benders paper became a short note.** *Minimal Infeasible Subsystems and Benders cuts* exists as a 17-page manuscript (June 2008) and as a 17-page extended draft (file `Benders_mis_extended_draft.pdf`) revised in September 2009. The draft announces a strong NP-hardness result for finding a violated optimality cut (P32 PDF p. 1). The published version is the 8-page *A note on the selection of Benders' cuts* (Math. Prog. 124:175–182, 2010). The extended draft is still in the papers folder (P4). [practice] The published note was not read, so whether the NP-hardness result survived it is not known. Reasons for the cut are not stated anywhere.
- **Minibatch persistency, 2018 → 2026.** Mandatelli's thesis says its test accuracies are not competitive with the state of the art, because momentum and learning rate were fixed in advance (S21 PDF p. 19). The joint preprint (arXiv:1806.07353, whose arXiv comment says it was submitted to an international conference) still appears among the homepage's technical reports in 2026, not among publications (P1, P34). In September 2026 Fischetti alone ran the missing test (arXiv:2609.13922). His abstract says the idea had been absorbed into data echoing in 2019, and that it still lacked a baseline tuned as carefully as the method itself. The new study is pre-registered, uses 8 seeds per cell and tunes the learning rate separately for each arm (P35). [practice and stated] A weakness the student's thesis admitted was thus taken up and re-tested by the advisor alone eight years later, in a preprint not yet reviewed [inferred framing].
- **The DNN-training master's line produced few papers.** Mandatelli's work gave the preprint still listed as a technical report, and Stringher's gave the CCIS paper; nothing was found from Calandro or Martini (2020). [practice; absence of evidence, not evidence of failure]
- **Losses.** Lorenzo Brunetta, a co-author (2000; 2008) and a helper on Bertacco's thesis, is remembered in 2008 as someone the group misses (S3 PDF p. 9; the cause is not stated). Caprara died in a mountaineering accident in April 2012, as stated in Optima 91, p. 1 (P38).
- **Not found:** rejected papers, retracted claims, or a student's account of a failed project.

---

## 8. Era and resource context

| Period | Setting | Resources visible in the record |
|---|---|---|
| 1982–1992 | Bologna DEIS (Toth, Martello); Laurea, PhD, then assistant professor | Corridor desks, a DECstation 5000/240, CPLEX 1 (Optima 91 on the Bologna group; S41) |
| 1992–1997 | Associate professor at Padova, then full professor at L'Aquila and Udine (P1) | No students' records from these years were found |
| 1997–2009 | Padova DEI. PhD students enrolled in the mathematics department's doctorate (Matematica Computazionale). Railway, telecom and EU projects (ADONET, ARRIVAL), MIUR/CNR, PRIN; Netherlands Railways work (Wagner finalist 2004, Edelman 2008) | CPLEX 7.0–11.0, Xpress 16, GLPK; Pentium IV 2.4 GHz with 512 MB (2005); Core2 Q6600 with 4 GB (2008); MIPLIB 3.0 and 2003 |
| 2009–2016 | Monaci at DEI; Salvagnin postdoc (2009–11), then assistant professor (2011–18); Vienna partnership | CPLEX 12.6; WWTF funding; DIMACS 2014 |
| 2017–2022 | Machine-learning turn through Montréal (IVADO, CERC DS4DM) | One GTX 1080 Ti with PyTorch 0.4 (2018); two NVIDIA-donated Titan Xp on a department machine (2019–20) (S21–S23) |
| 2022–2026 | Papers with Roberti, Salvagnin, Cavaliere and Palasgo; solo 2026 preprints with pre-registration or replication packages (P35, P37); tutorials for young researchers (P11, P12, P15) | The course still uses C on CPLEX, a Python 2 profile script (version dated 20 Apr 2026) and recorded lessons (P5, P8, P9) |

---

## Contradictions (kept, not reconciled)

1. **A special and friendly group: testimony or template?** Bertacco's 2005 description of Fischetti's group is Lodi's 1999 description of the Martello–Toth group, word for word (§2.1). Zanette's and Salvagnin's independent wordings (uncommonly friendly; a unique environment) say something similar. Count Bertacco's sentence as evidence of template reuse, not of the group's climate.
2. **Author order.** Students' papers are alphabetical to 2019 except Zanette, Fischetti, Balas (2011), and mostly junior-first from 2020 (§1.3). For the same Liu paper, Liu's thesis lists the article with the authors in the order Fischetti, Liu, Lodi, submitted to MPC on 28 July 2022 (S37 PDF p. 52). The arXiv v2 and AAAI records list Liu first (P36; Crossref).
3. **Theorem or conjecture.** The ISMP 2018 keynote states, as a *Theorem*, that using cuts within an enumerative scheme is good (P13 slide 6). The AIROyoung 2026 deck states the same sentence as a *Conjecture* (P11 slide 2).
4. **Who supervised.** Collautti's formal relatore is Fischetti, yet the student names Malitsky as the real supervisor (S29 PDF p. 7). Sartor's relatore is Fischetti, yet Zanette followed the whole project (S20 PDF p. 76).
5. **Credit for a student's idea.** Petterle's contribution is credited in the text of a sole-authored paper (P23 PDF p. 4). Comparable master's contributions became co-authorships (Codato, Sartor, Mandatelli, Stringher).
6. **Dates of the 2008 theses.** Salvagnin's thesis says 2008 inside, its title page says 25 Jan 2009, IRIS says accepted 27 Jan 2009, and his CV says defended 26 Mar 2009. Zanette's says 3 Nov 2008 on the front, 2008–2009 inside, and IRIS says accepted 28 Jan 2009 (S2, S3, S38, S39).
7. **De Franceschi's supervisor.** The sibling note 06 found no supervisor line in the first pages of the De Franceschi file. Its acknowledgement on PDF p. 4 names Fischetti as relatore and thanks Toth for joint supervision (S10).
8. **One Liu reference, two Fischettis.** Liu's bibliography attributes the CPAIOR 2019 paper to `M. Fischetti` with Lodi and Zarpellon. Crossref gives Martina (§0).

---

## Gaps

- **No Festschrift, birthday workshop or volume** in his honour was found (one search). No interview with Fischetti about research or supervision was found (one search). No interview with Lodi describing him as a mentor was found (one search). No student blog, lab guide or onboarding document was found beyond the OR2 course material.
- **Formal advisee list incomplete.**
  - MGP has no record of him, its advanced search was offline (partial recovery after a PHP vulnerability, status page dated 4 Nov 2026), and his own advisor remains unknown.
  - IRIS cannot be filtered by advisor through a URL, so the PhD list comes only from the dissertations folder and named-student searches.
  - Where Bertacco, Zanette (after 2012), Luzzi, Codato and Saturni went is not established, and Cavaliere's degree record was not found.
- **Not read, or unreadable.**
  - Codato's 2003 thesis (bitmap fonts in both the PDF and the PS); Luzzi's 2002 PS (30 MB); Polo's ZIP. Bettin 1998 has no front matter.
  - The published 2010 Benders note, and the Interfaces papers (only their metadata was read).
  - Martina Fischetti's DTU PhD thesis: DTU Orbit returned 403.
  - Markus Sinnl's and other Vienna students' theses: not found in OpenAlex.
- **Lectures not transcribed.** The OR2 lessons on thesis structure and exam rules (27 May 2022, mediaspace.unipd.it) and the 2026 videos in the slides folder were not watched. A request for the captions of the hosted lectures was refused by this session's permission settings and was not retried, so nothing was saved to `talks/`.
- **Pages not reached.** The ISCO 2014 speaker bio (403). The DBLP person page (bot check; the SPARQL endpoint was used instead). A 2018 Padova hiring report (404). The paduaresearch EPrints host (certificate error). Optima 91 at mathopt.org (404; read from mathopt.zib.de instead). The CORS page lists him as the 2015 Larnder laureate but gives no citation text (S43).
- **Absent from every source.** Meeting rhythm, group seminars, code review, how drafts are revised with students, and how co-authors divide the writing.

---

## Sources

**Primary** (his own web space, course material, own or co-authored texts; all opened 2026-11-08)

- P1 · M. Fischetti, homepage and CV with publication and prize lists, https://www.dei.unipd.it/~fisch/ · primary
- P2 · Dissertations folder listing (29 files, last modified 2021-12-14), http://www.dei.unipd.it/~fisch/ricop/tesi/ · primary
- P3 · Slides folder listing, https://www.dei.unipd.it/~fisch/papers/slides/ · primary
- P4 · Papers folder listing (98 entries), https://www.dei.unipd.it/~fisch/papers/ · primary
- P5 · Course folders `ricop/`, `OR1/`, `OR2/`, `OR2_2021_2022/`, `OR2/PerfProf/`, https://www.dei.unipd.it/~fisch/ricop/ · primary
- P6 · Check list for the OR2 thesis (2022–2023), `ricop/OR2/Checklist_OR2_thesis.pdf` (posted 2023-05-24) · primary
- P7 · Programma di massima del corso di RO2, a.a. 2019–2020, `ricop/OR2/` · primary
- P8 · OR2 Videos from 2021–2022, `ricop/OR2_2021_2022/Fischetti_OR2_videos_2022.pdf` · primary
- P9 · `ricop/OR2/PerfProf/read_me.txt` and `perfprof.py` (script by D. Salvagnin, 2016; version line 20-apr-2026; marked internal use) · primary (course file; author Salvagnin)
- P10 · D.M. 8 agosto 2018 n. 589, valori-soglia tables (ministry document) in `ricop/OR2/` · primary as a record of the folder only
- P11 · M. Fischetti, *Branch-and-Cut is our swiss army knife*, AIROyoung, Padua, 9 Feb 2026, part 1 (BC + Benders), slides folder · primary
- P12 · M. Fischetti, *Branch-and-Cut is our swiss army knife*, VeRoLog 2025, Trento, 13 Jun 2025, part 1 (BC implementation, bilinear), slides folder (footer = PDF page + 1) · primary
- P13 · M. Fischetti, *#post_modern Branch-and-Cut Implementation*, ISMP 2018 keynote, Bordeaux, 6 Jul 2018, slides folder · primary
- P14 · M. Fischetti, *Intersection cuts from bilinear disjunctions* (joint work with M. Monaci), Dr. Egon Balas Academic Symposium, Tepper School, Pittsburgh, 28 Oct 2019, slides folder · primary
- P15 · M. Fischetti, AIROyoung, Padua, 9 Feb 2026, part 2 (intersection cuts and bilevel optimization), slides folder · primary
- P16 · V. Cacchiani, A. Caprara, M. Fischetti, *A Lagrangian Heuristic for Robust Train Timetabling*, AIRO 2012 (file name `2012 AIRO [in memoriam Alberto Caprara].pdf`), slides folder · primary
- P17 · M. Fischetti, Harold Larnder lecture deck, CORS/INFORMS 2015, Montréal (file name `2015 CORS [Fischetti - Occam Razor].pdf`), slides folder · primary
- P18 · M. Fischetti, *BRANCHstorming*, ISCO 2014 plenary, Lisbon, slides folder · primary
- P19 · M. Fischetti, *I MIP you!*, COFIN–Matheon workshop, Villa Vigoni, May 2006, slides folder · primary
- P20 · M. Fischetti, F. Glover, A. Lodi, *The feasibility pump*, Aussois 2004 deck, slides folder · primary
- P21 · M. Fischetti et al. (Padova and Vienna), *Thinning out Steiner Trees*, Aussois, Jan 2015, slides folder · primary
- P22 · G. Codato, M. Fischetti, *Combinatorial Benders' Cuts for Mixed-Integer Linear Programming*, preprint (May 2004, rev. Feb 2005); Oper. Res. 54(4):756–766, 2006, DOI 10.1287/opre.1060.0286 · primary
- P23 · M. Fischetti, *Fast training of Support Vector Machines with Gaussian kernel*, preprint; Discrete Optim. 22:183–194, 2016, DOI 10.1016/j.disopt.2015.03.002 · primary
- P24 · M. Fischetti, G. Sartor, A. Zanette, *A MIP-and-refine matheuristic for smart grid energy management*, preprint (Oct 2012, rev. Mar 2013); ITOR 22(1):49–59, 2015, DOI 10.1111/itor.12034 · primary
- P25 · M. Fischetti, C. Polo, M. Scantamburlo, local branching with 2-level variables, preprint; Networks 44(2):61–72, 2004, DOI 10.1002/net.20017 · primary
- P26 · M. Fischetti, I. Luzzi, *Mixed-integer programming models for nesting problems*, preprint; J. Heuristics 15(3):201–226, 2009, DOI 10.1007/s10732-008-9088-9 · primary
- P27 · R. De Franceschi, M. Fischetti, P. Toth, preprint; Math. Prog. 105(2–3):471–499, 2006, DOI 10.1007/s10107-005-0662-8 · primary
- P28 · M. Fischetti, C. Saturni, *Mixed-Integer Cuts from Cyclic Groups*, preprint (Sep 2005); Math. Prog. 109(1):27–53, 2007, DOI 10.1007/s10107-006-0726-4 · primary
- P29 · L. Bertacco, L. Brunetta, M. Fischetti, preprint; EJOR 189(3):1345–1357, 2008, DOI 10.1016/j.ejor.2006.03.071 · primary
- P30 · M. Fischetti, F. Glover, A. Lodi, *The feasibility pump*, preprint; Math. Prog. 104(1):91–104, 2005, DOI 10.1007/s10107-004-0570-3 · primary
- P31 · F. Cavaliere, E. Bendotti, M. Fischetti, preprint (Jun 2022); MPC 14(4):749–779, 2022, DOI 10.1007/s12532-022-00224-2 · primary
- P32 · M. Fischetti, D. Salvagnin, A. Zanette, *Minimal Infeasible Subsystems and Benders cuts*, manuscript (2008) and extended draft (rev. Sep 2009), `papers/MIS_for_Benders.pdf`, `papers/Benders_mis_extended_draft.pdf`; published as DOI 10.1007/s10107-010-0365-7 · primary
- P33 · M. Fischetti, J. Jo, arXiv:1712.06174 (2017), acknowledgements · primary
- P34 · M. Fischetti, I. Mandatelli, D. Salvagnin, *Faster SGD training by minibatch persistency*, arXiv:1806.07353 (2018), metadata · primary
- P35 · M. Fischetti, *Minibatch persistency, eight years later…*, arXiv:2609.13922 (12 Sep 2026), metadata and abstract · primary
- P36 · D. Liu, M. Fischetti, A. Lodi, *Revisiting local branching with a machine learning lens*, arXiv:2112.02195v2, acknowledgements; AAAI 36(4):3796–3803, 2022, DOI 10.1609/aaai.v36i4.20294 · primary
- P37 · Martina Fischetti, Matteo Fischetti, *EndoWake…*, arXiv:2609.40157 (30 Sep 2026), metadata · primary
- P38 · N. Bansal, M. Fischetti, G. Lancia, A. N. Letchford, A. Lodi, M. Monaci, U. Pferschy, D. Pisinger, J.-J. Salazar-González, M. Sviridenko, P. Toth, *Alberto Caprara (1968–2012): Scientific Contributions*, Optima 91 (April 2013) pp. 1–11, https://mathopt.zib.de/Optima-Issues/optima91.pdf · primary (co-authored)
- P39 · M. Fischetti, I. Luzzi, *Exact and Heuristic Methods for Nesting Problems*, report, Padova, 1 Apr 2004, `ricop/tesi/tesi_dottorato_Luzzi_2003.pdf` · primary (co-authored)

**Secondary** (students', visitors' and colleagues' texts, repository and database records; all opened 2026-11-08 unless marked)

- S1 · L. Bertacco, *Exact and Heuristic Methods for Mixed Integer Linear Programs*, PhD thesis, Padova, 30 Dec 2005, `ricop/tesi/2005_Bertacco_PhD_thesis.pdf` · secondary
- S2 · D. Salvagnin, *Constraint Programming Techniques for Mixed Integer Linear Programs*, PhD thesis, Padova (XXI ciclo), 2008/2009, `ricop/tesi/2008_Salvagnin_PhD_thesis.pdf` · secondary
- S3 · A. Zanette, *Three Topics in Mixed Integer Programming*, PhD thesis, Padova, 3 Nov 2008, `ricop/tesi/2008_Zanette_PhD_thesis.pdf` · secondary
- S4 · A. Lodi, *Algorithms for Two-Dimensional Bin Packing and Assignment Problems*, PhD thesis, Bologna, AA 1996–99, `ricop/tesi/tesi_dottorato_Lodi_1999.pdf` · secondary
- S5 · Bettin, document on pallet loading (1998), `ricop/tesi/tesi_dottorato_Bettin_1998.pdf` · secondary
- S6 · C. Saturni, *Design and implementation of a genetic algorithm for a packing with an uncertain future problem*, tesi di laurea, Dec 2000 (PS in `ricop/tesi/`; also Padua thesis archive hdl 20.500.12608/12415) · secondary
- S7 · D. Ciprian, tesi di laurea, AA 1998–99, `ricop/tesi/tesi_Ciprian_2000.pdf` · secondary
- S8 · C. Polo, tesi di laurea, AA 2000–01, `ricop/tesi/tesi_Polo_2002.pdf` · secondary
- S9 · G. Andreello, tesi di laurea, 24 Mar 2003, `ricop/tesi/tesi_Andreello_2003.pdf` · secondary
- S10 · R. De Franceschi, tesi di laurea, 2003, `ricop/tesi/tesi_De_Franceschi_2003.pdf` · secondary
- S11 · M. Scantamburlo, *DRT: a General Method for Mixed Integer Problems*, AA 2001–02, `ricop/tesi/tesi_Scantamburlo_2003.pdf` · secondary
- S12 · G. Codato, tesi di laurea, 2003, `ricop/tesi/tesi_Codato_2003.pdf` and `.ps` (text not extractable; not read) · secondary
- S13 · L. Bancaro, tesi di laurea, AA 2003–04, `ricop/tesi/Tesi_Bancaro_2004.pdf` · secondary
- S14 · D. Baracco, tesi di laurea, AA 2003–04, `ricop/tesi/Tesi_Baracco_2004.pdf` · secondary
- S15 · M. Aldà, tesina, 22 Jul 2004, `ricop/tesi/tesina_2004_Aldà.pdf` · secondary
- S16 · M. Gallina, tesi di laurea, AA 2003–04, `ricop/tesi/Tesi_Gallina_2005.pdf` · secondary
- S17 · T. Normani, tesina 2008 (CBC interface), `ricop/tesi/` · secondary
- S18 · N. Zago, tesina 2008 (ellipsoid method), `ricop/tesi/` · secondary
- S19 · L. Petterle, *A Computational Analysis of Optimization Models for Support Vector Machines*, MSc thesis, 2012, `ricop/tesi/tesi_Petterle_2012.pdf` (also archive hdl 20.500.12608/16465) · secondary
- S20 · G. Sartor, *Optimal Scheduling of Smart Home Appliances using MILP*, MSc thesis, 10 Dec 2012, `ricop/tesi/tesi_Sartor_2012.pdf` (also archive hdl 20.500.12608/16475) · secondary
- S21 · I. Mandatelli, *Improved Training Methods for Neural Networks*, MSc thesis, 28 Sep 2018, `ricop/tesi/2018_Mandatelli_Thesis.pdf` · secondary
- S22 · M. Stringher, *Unconventional Training of Deep Neural Networks*, MSc thesis, 1 Apr 2019, `ricop/tesi/2019_Stringher_Thesis.pdf` · secondary
- S23 · M. Calandro, *Metaheuristic frameworks for deep neural network training*, MSc thesis, 1 Dec 2020, `ricop/tesi/2020_Calandro_Marco_thesis.pdf` · secondary
- S24 · A. Bugin, *Mathematical Programming for the Optimisation of Ambulances Deployment*, MSc thesis, 6 Apr 2020, `ricop/tesi/2020_Tesi_di_laureaAndrea_Bugin_1180044.pdf` · secondary
- S25 · L. Zoggia, *Interval scheduling problem: analisi teorica e test*, MSc thesis, AA 2010–11, Padua thesis archive hdl 20.500.12608/14122 · secondary
- S26 · G. Frison, *Numerical Methods for Model Predictive Control*, MSc thesis, AA 2012–13, hdl 20.500.12608/16283 · secondary
- S27 · P. Marchezzolo, *An Integer Linear Programming Heuristic for the Travelling Salesman Problem*, AA 2013–14, hdl 20.500.12608/16072 · secondary
- S28 · G. Di Liberto, *DASH: Dynamic Approach for Switching Heuristics*, AA 2013–14, hdl 20.500.12608/17484 · secondary
- S29 · M. Collautti, *SNNAP: Solver-based Nearest Neighbor for Algorithm Portfolios*, AA 2013–14, hdl 20.500.12608/17492 · secondary
- S30 · N. Menon, TSPTW heuristics, AA 2014–15, hdl 20.500.12608/18290 · secondary
- S31 · A. Beltramin, *Modern branch-and-cut solvers for MILP: a computational comparison*, AA 2014–15, hdl 20.500.12608/19950 · secondary
- S32 · D. Martini, *Application of Neural Network for the Knapsack Problem*, AA 2019–20, hdl 20.500.12608/23979 · secondary
- S33 · Padua Thesis and Dissertation Archive, query `Fischetti Matteo` (12 records, with supervisor and co-advisor fields; S. Dalla Valle 2020–21, hdl 20.500.12608/850, no full text), https://thesis.unipd.it/ · secondary
- S34 · Martina Fischetti, *Mixed Integer Programming Models and Algorithms for Wind Farm Layout*, MSc thesis, Padova, AA 2013–14, https://thesis.unipd.it/retrieve/f428eb1a-8b44-4b0e-a0a1-70ef3bb9abde/tesi_Fischetti.pdf · secondary
- S35 · Martina Fischetti, *Mixed Integer Programming Models and Algorithms for Wind Farm Layout and Cable Routing*, MSc thesis, Aalborg, 2013–14, https://projekter.aau.dk/projekter/files/198432593/thesis_Fischetti.pdf · secondary
- S36 · EURO, *EDDA Winner 2019* (Martina Fischetti), https://www.euro-online.org/web/pages/1645/edda-winner-2019 · secondary
- S37 · D. Liu, *Machine Learning Algorithms for Combinatorial Optimization*, PhD thesis, Polytechnique Montréal, Aug 2022 (director A. Lodi), https://publications.polymtl.ca/10460/ · secondary
- S38 · IRIS Università di Padova records: Salvagnin thesis hdl 11577/3425690; Zanette thesis hdl 11577/3425623; Palasgo thesis hdl 11577/3583534 (advisor R. Roberti, 12 Feb 2026); Palasgo–Fischetti–Roberti chapter hdl 11577/3555881, https://www.research.unipd.it/ · secondary
- S39 · D. Salvagnin, Curriculum Vitae, July 2026, http://www.dei.unipd.it/~salvagni/pdf/mycv.pdf (career, prizes, supervision, consulting; contact details not used) · secondary
- S40 · D. Salvagnin, homepage and publication abstracts, http://www.dei.unipd.it/~salvagni/ · secondary
- S41 · V. Cacchiani, A. Lodi, E. Malaguti, U. Pferschy, J.-J. Salazar-González, E. Traversi, G. Woeginger, *Alberto Caprara (1968–2012): Memories*, Optima 91 (April 2013) pp. 11–13, https://mathopt.zib.de/Optima-Issues/optima91.pdf · secondary
- S42 · Mathematics Genealogy Project: quick search (0 records for Matteo Fischetti), P. Toth record id 79649, status page, https://www.mathgenealogy.org/ · secondary
- S43 · CORS, Harold Larnder Prize recipients (2015: Matteo Fischetti), https://www.cors.ca/content/harold-larnder-prize · secondary
- S44 · DBLP SPARQL endpoint, co-author counts for pid 47/4770 (88 co-authors), https://sparql.dblp.org/sparql · secondary (database)
- S45 · Crossref REST API, metadata for every DOI cited in this note, https://api.crossref.org/ · secondary (database)
