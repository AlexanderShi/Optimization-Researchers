# Matteo Fischetti · Research trajectory (research agent 06 of 06)

- **Researcher**: Matteo Fischetti, Full Professor of Operations Research, DEI (Department of Information Engineering), University of Padova; born 1958 [S1]. Not to be confused with **Martina Fischetti** (ORCID 0000-0002-7673-6917, now Ramón y Cajal tenure-track at the Universidad de Sevilla [S50]), his most frequent co-author since 2014.
- **Dimension**: 06, research trajectory (framework §二, Agent 6): academic timeline, advisor and student lineage, direction changes and what triggered them, when he enters and leaves a topic, and the last 12 months.
- **Research date**: 2026-11-08
- **Sources consulted**: 58 (S1–S58 under Sources; 50 primary, 8 secondary). WebSearch calls used: 2 of the 5 allowed.
- **Local corpus**: `references/sources/` held no user-supplied files (only `.gitkeep` placeholders and `RESOURCES.md`), so nothing below is "from user-supplied material". `private/` was not opened.
- **Access limits**: DBLP (pid 47/4770) answered every request with an Anubis bot-check page, which was not bypassed. The publication backbone is therefore his homepage list (143 entries) [S1], OpenAlex [S52], Crossref (about 60 DOIs resolved in this run) [S54] and the arXiv API [S35]. ResearchGate returned 403. The Mathematics Genealogy Project was partly offline: its status page says the PHP functions were disabled on 2026-10-21 and homepage search came back on 2026-11-04. Quick search worked [S55].
- **Tags**: [stated] what he said or wrote about his own work · [practice] what he did (papers, code, records, file dates) · [observed] what others recorded about him · [inferred] my reading of dates and patterns, not any source's claim. **P** = primary (his own documents and code, his students' theses, records kept by awarding bodies and universities); **S** = secondary (aggregators, search snippets).
- Quotes are verbatim and short, and everything else is paraphrase. Slide and PDF page numbers ("p.") are PDF page numbers of the file named. Paper titles are in italics.

---

## 0. The trajectory in brief

1. **1982–1993, Bologna.** Worst-case analysis, bounding procedures and routing and scheduling, working inside the Bologna group: 9 of his 11 works in 1985–89 have Paolo Toth or Silvano Martello as co-authors (the other two are his solo 1986 paper and a 1989 working paper with Balas) [S52]. PhD in 1987, and the thesis won the ORSA transportation dissertation prize [S1, S46]. [practice/observed, P/S]
2. **1989–2006, polyhedra and branch-and-cut for routing**, with Egon Balas as his longest collaborator (from a 1989 working paper to a 2017 chapter). Two lines ran in parallel. Railway crew and timetabling work (1993–2017) entered through Ferrovie dello Stato code competitions and later continued with Netherlands Railways. Statistical disclosure control (1998–2003) sits inside the windows of two EU projects. [practice, P; triggers inferred from dates]
3. **2002–2009, the turn to general-purpose MIP.** Local branching, the feasibility pump, combinatorial Benders cuts, and a habit of handing the separation or variable-fixing subproblem to the MIP solver itself. Each idea was premiered at the January Aussois workshop. [practice, P; stated motive S6, S9]
4. **2010–2016, the solver's own behaviour as the research object.** Erraticism, sampling, SelfSplit, backdoors and orbital shrinking. The trigger he names is that seed-only changes in CPLEX 12.2 produced very different run times [S8]. [stated, P]
5. **2014–2020, "thinning out" models** through Benders decomposition, a node-based Steiner model, and bilevel and interdiction problems with Ljubić and Sinnl. The trigger he names is an observation from the 2014 DIMACS Steiner challenge [S10]. [stated, P]
6. **2015–2022, machine learning, entered from the MILP side** (SVM training by MILP, deep neural networks as 0-1 MILPs). He arrived about one month after another group's MILP formulation of neural networks, so this was a concurrent start, not the first one. [practice + inferred]
7. **2014–2026, wind-farm layout with Martina Fischetti**, and by analogy COVID social-distancing layouts (2020) [S9, S13]. [stated, P]
8. **2020–2024, lower output.** His list shows 6 entries for 2020–24 against 25 for 2015–19 [S1]. The work runs through Padova colleagues and a PRIN 2022 grant [S15]. No reason for the dip was found. [practice; reason not stated]
9. **September–November 2026, a burst of solo and two-author preprints.** They come with full replication packages, pre-registered or pre-declared designs (OSF pre-registration for the minibatch study; pre-declared comparisons and test sets in the FP and EndoWake work), pinned solver versions and **declared AI assistants** (Anthropic Claude; OpenAI ChatGPT or Codex). Two of them revisit his own past claims: the 2005 feasibility-pump cutoff prescription and the 2018 minibatch-persistency speed-up [S23, S31–S34]. [stated/practice, P]

---

## 1. Academic timeline (education, positions, prizes, service)

| Year | Event | Evidence | Tag |
|---|---|---|---|
| 1982 | Laurea in Electronic Engineering, University of Bologna, 100/100 cum laude | homepage CV [S1] | [practice] P |
| 1986 | First paper, sole author: *Worst-case analysis of an approximation scheme for the subset-sum problem*, Operations Research Letters, DOI 10.1016/0167-6377(86)90065-9 | Crossref [S54], homepage [S1] | [practice] P |
| 1987 | PhD (Dottorato di Ricerca in Ingegneria dei Sistemi), University of Bologna. INFORMS lists the thesis as *Modelli ed Algorithmi per Problemi di Routing e di Scheduling* (spelling as on the INFORMS page) | [S1], [S46] | [observed] P |
| 1987 | ORSA prize for the best PhD dissertation on transportation; the homepage adds that it was the first such ORSA prize for a thesis done outside the USA. INFORMS records it as the TSL Dissertation Prize | [S1], [S46], [S48] prize 22765 | [observed] P |
| 1987 | AIRO "Best Young Researcher" first prize | [S1], [S48] | [observed] P |
| 1990–1992 | Assistant Professor of OR, DEIS, University of Bologna | [S1] | P |
| 1992–1994 | Associate Professor of OR, University of Padova | [S1] | P |
| 1994 | FS "FASTER" first prize: best code for very large railway set-covering problems (with Caprara and Toth) | [S1], [S48] | [observed] P |
| 1994–1995 | Full Professor, University of L'Aquila | [S1] | P |
| 1995 | FS "FARO" first prize: best code for a railway rostering problem (with Caprara, Toth and Vigo); IPCO 1995 programme committee member | [S1], [S48] | P |
| 1995–1997 | Full Professor, University of Udine | [S1] | P |
| 1997– | Full Professor, University of Padova. In November 2026 UNI-FIND still lists him as a first-band tenured professor (*Docenti di ruolo di Ia fascia*), DEI, group 01/MATH-06 Operations Research | [S1], [S48] | P |
| 1997 | Semiplenary, Mathematical Programming Symposium, Lausanne | [S1] | P |
| 2004 | Finalist, INFORMS Wagner Prize, with *Reinventing Crew Scheduling at Netherlands Railways* (Interfaces 35:393–401, 2005, DOI 10.1287/inte.1050.0158) | [S1], [S46], [S54] | [observed] P |
| 2007 | Chair of the IPCO 2007 programme committee and co-editor of its proceedings with D. P. Williamson (LNCS, DOI 10.1007/978-3-540-72792-7); ATMOS 2007 programme committee member | [S1], [S48], [S54] | P |
| 2008 | Chair, ATMOS 2008 programme committee | [S1], [S48] | P |
| 2008 | Franz Edelman Award with the Netherlands Railways team, for *The New Dutch Timetable: The OR Revolution* (Interfaces 39:6–17, 2009, DOI 10.1287/inte.1080.0409). The INFORMS citation credits the timetable with €40 million of additional annual profit in 2007 | [S1], [S46], [S54] | [observed] P |
| 2009 | Plenary speaker, ISMP Chicago | [S1] | P |
| 2012 | Semiplenary at EURO XXV; plenaries at VeRoLog 2012 and Matheuristics 2012 | [S1] | P |
| 2014 | Plenaries at ISCO (Lisbon) and RAMP (Tokyo); winner of the 11th DIMACS Implementation Challenge (Steiner tree) with the codes mozartballs, mozartduet and staynerd | [S1] | P |
| 2015 | Harold Larnder Prize (CORS) and the Larnder lecture at CORS/INFORMS, Montreal; EURO plenary at OR2015, Vienna. On the CORS list he sits between 2014 (Rosenhead) and 2016 (Bertsimas) | [S47], [S48] prize 22763, [S1], [S10] | [observed] P |
| till 2015 | Editorial boards of J. Combinatorial Optimization and 4OR; he remains on the boards of Operations Research and Mathematical Programming Computation | [S1] | P |
| 2017 | "2016 COAP Best Paper Award" (listed under 2017) for *On handling indicator constraints in mixed integer programming* (COAP 65:545–566, DOI 10.1007/s10589-016-9847-8); plenaries at LNMB (Lunteren) and AIRO/ODS (Sorrento) | [S1], [S54] | P |
| 2018 | Keynote at ISMP Bordeaux, 6 July 2018 | [S1], [S12] | P |
| 2019 | Self-published textbook *Introduction to Mathematical Optimization* (Scholar gives 2019); Italian textbook *Lezioni di Ricerca Operativa* | [S1], [S53] | P/S |
| 2020 | IFORS distinguished speaker at INFORMS 2020 (November 2020) | [S1], [S13] | P |
| 2025–2026 | Tutorial-style lectures at VeRoLog 2025 (Trento, 13 June 2025, in three parts), ODS 2025 (Milan, 4 September 2025) and AIROyoung (Padua, 9 February 2026, in two parts) | [S3], [S14], [S15], [S17], [S18] | [practice] P |
| 2026 | GitHub account `mfischetti-arch` created on 2026-09-04, with one repository | GitHub API [S24] | [practice] P |

Identity records [S51, S52]. His ORCID was created on 2016-04-15 and holds 13 works imported from Crossref, with no affiliation entries, so it is not maintained. OpenAlex attributes to him the affiliations Vattenfall (Denmark), DTU, Polytechnique Montréal and Universidad de Sevilla. These come from co-authors (Martina Fischetti's employers; Defeng Liu's and Andrea Lodi's) and are not his moves; see Contradictions. OpenAlex also attributes to him an IEEE Spectrum item from 1993, *The cellular phone scare* (DOI 10.1109/6.214586), whose Crossref author is only "M. Fischetti". It is not in his own list and is probably by another M. Fischetti [inferred]; it is excluded everywhere below.

---

## 2. Advisor and student lineage

### 2.1 His own training
- **PhD advisor: not found.** The MGP quick search for "Matteo Fischetti" returns 0 records. Paolo Toth's MGP page (id 79649) lists seven students (Bianchini, Cacchiani, Caprara, Lodi, Salazar-González, Smith, Vigo), and Fischetti is not among them [S55]. [observed, S]
- His early co-authors were Toth (7 of 11 works in 1985–89) and Martello (4) [S52]. A Bologna mentorship by Toth and Martello is plausible but **not confirmed** by any source. [practice S; mentor link inferred]
- **Egon Balas**: their joint papers run from a 1989 working paper (RePEc record in OpenAlex), through *A lifting procedure for the asymmetric traveling salesman polytope and a large new class of facets* (MPA 58:325–352, 1993, DOI 10.1007/bf01581274) and the Gomory/lexicography papers with Zanette (2009–2012), to the chapter *Integer (Linear) Optimization* (SIAM 2017, DOI 10.1137/1.9781611974683.ch5) [S52, S54]. The homepage background shows handwritten notes by Balas, and the slides folder holds a 2019 "Balas Memorial" talk file (2019-10-18) [S1, S3]. [practice, P]

### 2.2 Doctoral students (supervision confirmed on the thesis title page)
| Student | Thesis | Supervision evidence | Later joint work |
|---|---|---|---|
| Livio Bertacco | *Exact and Heuristic Methods for Mixed Integer Linear Programs*, PhD in Computational Mathematics (XVIII ciclo), Padova, 30 Dec 2005 | title page: "Il Supervisore … Matteo Fischetti" [S36] | *A feasibility pump heuristic for general mixed-integer problems*, Discrete Optimization 4:63–76 (2007), DOI 10.1016/j.disopt.2006.10.001 |
| Domenico Salvagnin | *Constraint Programming Techniques for Mixed Integer Linear Programs*, PhD (XXI ciclo), Padova; title page dated 25 Jan 2009, inner page 2008 | supervisor Fischetti [S37] | FP 2.0, MPC 1:201–222 (2009), DOI 10.1007/s12532-009-0007-3. He is now a Padova colleague and was still a co-author in 2026: EJOR 329:96–111, DOI 10.1016/j.ejor.2025.07.034 |
| Arrigo Zanette | *Three Topics in Mixed Integer Programming*, PhD (XXI ciclo), Padova, 3 Nov 2008 | supervisor Fischetti [S38] | *Lexicography and degeneracy: can a pure cutting plane algorithm work?*, MPA 130:153–176 (2011), DOI 10.1007/s10107-009-0335-0 |
| Ivan Luzzi | PhD thesis files dated 2002 (.ps) and 2003 (.pdf) in his folder. The PDF I opened is a joint report, *Exact and Heuristic Methods for Nesting Problems* (Fischetti and Luzzi, 1 Apr 2004) | **not confirmed** from a title page [S39] | *Mixed-integer programming models for nesting problems*, J. Heuristics 15:201–226 (2009), DOI 10.1007/s10732-008-9088-9 |

**Not his doctoral students** (to prevent misreadings):
- **Andrea Lodi**: MGP gives PhD Bologna 1999 with advisors Martello and Toth, even though Lodi's thesis file sits in Fischetti's dissertations folder [S4, S55]. [observed]
- **Defeng Liu**: PolyPublie gives PhD Polytechnique Montréal 2022, *Machine Learning Algorithms for Combinatorial Optimization*, director Andrea Lodi only. Fischetti is a co-author of the AAAI 2022 paper (DOI 10.1609/aaai.v36i4.20294), not a director [S49]. [observed, P]
- **Martina Fischetti**: her ORCID gives an MSc at Padova and Aalborg (2011–2014), then an industrial PhD at DTU Management with Vattenfall (2015–2018), Vattenfall Lead Engineer (2018–21), the EU Joint Research Centre (2021–23), and Sevilla (postdoc 2024; Ramón y Cajal from 2025) [S50]. She is a separate researcher. Any wind-farm or EndoWake statement is joint work and cannot be credited to Matteo alone. [observed, P]

### 2.3 Laurea and master's theses: the thesis-to-paper pipeline
- **Supervisor confirmed on the title page** [S40–S44]. [practice, P]
  - Carlo Polo (AY 2000–01, heuristics for designing a UMTS interconnection network) and Massimo Scantamburlo (AY 2001–02, *DRT: a General Method for Mixed Integer Problems*) led to Fischetti, Polo and Scantamburlo, *A local branching heuristic for mixed-integer programs with 2-level variables, with an application to a telecommunication network design problem*, Networks 44:61–72 (2004), DOI 10.1002/net.20017.
  - Giuseppe Andreello (24 Mar 2003, new separation procedures for integer linear programming) led to *Embedding {0, ½}-Cuts in a Branch-and-Cut Framework: A Computational Study*, IJOC 19:229–238 (2007), DOI 10.1287/ijoc.1050.0162.
  - Iacopo Mandatelli (2018, *Improved Training Methods for Neural Networks*) led to arXiv:1806.07353 (June 2018).
  - Matteo Stringher (AY 2018/19, *Unconventional Training of Deep Neural Networks*) led to arXiv:1906.01504 (2019) and CCIS 1443:3–13 (2021), DOI 10.1007/978-3-030-85672-4_1.
- **In the folder listing only, supervision not checked** [S4]:
  - Saturni (2000) → *Mixed-Integer Cuts from Cyclic Groups* (IPCO 2005, DOI 10.1007/11496915_1; MPA 109:27–53, 2007, DOI 10.1007/s10107-006-0726-4)
  - Codato (2003) → *Combinatorial Benders' Cuts* (IPCO 2004, DOI 10.1007/978-3-540-25960-2_14; OR 54:756–766, 2006, DOI 10.1287/opre.1060.0286)
  - De Franceschi (2003) → *A new ILP-based refinement heuristic for Vehicle Routing Problems* (MPB 105:471–499, 2006, DOI 10.1007/s10107-005-0662-8)
  - Sartor (2012) → *MIP-and-refine matheuristic for smart grid energy management* (ITOR 22:49–59, 2015, DOI 10.1111/itor.12034)
  - Ciprian 2000, Baracco 2004, Bancaro 2004, Aldà 2004, Gallina 2005, Zago 2008, Normani 2008 ("cbc" in the file name), Petterle 2012, Bugin 2020, Calandro 2020: no paper checked.
  - The Bettin (1998) and De Franceschi (2003) files have no supervisor line in their first pages [S45].
- **Pattern [inferred]**: between 2000 and 2019 a laurea or master's thesis regularly became a co-authored paper within 0–4 years. Often a general-purpose MIP idea was first tested on the student's application (a UMTS network design became 2-level local branching). The dissertations folder holds no thesis after 2020; it was last modified on 2021-12-14 [S4].

### 2.4 Collaboration phases (from authorship data)
Counts below are OpenAlex works deduplicated by title, with the misattributed IEEE Spectrum item removed [S52]. They are approximate. [practice, S]

| Window | Works | Mean authors | Solo | Main co-authors (number of joint works) |
|---|---|---|---|---|
| 1985–89 | 11 | 2.36 | 1 | Toth 7, Martello 4, Carpaneto 2 |
| 1990–94 | 14 | 2.29 | 4 | Toth 5, Hamacher 2, Jörnsten 2, Maffioli 2 |
| 1995–99 | 21 | 2.81 | 2 | Toth 11, Caprara 9, Salazar-González 5, Vigo 5, Balas 3 |
| 2000–04 | 20 | 2.75 | 0 | Salazar-González 5, Toth 4, Lodi 3, Caprara 3 |
| 2005–09 | 39 | 3.10 | 0 | Lodi 12, Salvagnin 5, Zanette 4, Balas 4 |
| 2010–14 | 21 | 2.48 | 1 | Monaci 7, Salvagnin 7, Zanette 4 |
| 2015–19 | 29 | 3.21 | 3 | Monaci 15, Salvagnin 10, Sinnl 8, Ljubić 7 |
| 2020–24 | 8 | 2.75 | 0 | Martina Fischetti 2, Liu 2, Lodi 2 |
| 2025–26 | 8 | 2.38 | 1 | Martina Fischetti 4, Roberti 3, Salvagnin 2 |

Each main partnership lasts about 10 years and overlaps the next one: Toth, then Caprara and Salazar, then Lodi, then Salvagnin and Zanette (his own students), then Monaci, then Ljubić and Sinnl, then Martina Fischetti with the Padova colleagues Roberti and Salvagnin [inferred]. The homepage list has solo papers in 1986, 1990, 1991 (two), 1992, 1995 and 2016 [S1]. The 2026 solo manuscripts (FP cutoff, minibatch persistency, the Fermat note) return to sole authorship after a decade [practice]. Alberto Caprara, a co-author from 1994 [S1], is the subject of the AIRO 2012 talk file named "in memoriam Alberto Caprara" (2012-09-07) [S7, S3]. [practice, P]

---

## 3. Research phases, turns and their triggers (dated)

| Period | Line of work | First evidence | Trigger (tag) | Last item or exit | Context |
|---|---|---|---|---|---|
| 1986–1993 | Approximation, worst-case analysis, additive bounding, routing and scheduling | ORL 1986 (above); *An Additive Bounding Procedure for Combinatorial Optimization Problems*, OR 37:319–328 (1989), DOI 10.1287/opre.37.2.319 | PhD work in the Bologna group [practice; mentor inferred] | *An additive bounding procedure for the asymmetric travelling salesman problem*, MPA 53 (1992), DOI 10.1007/bf01585701 | 2–3 authors per paper |
| 1989–2006 | Polyhedral theory of the ATSP and arborescences; branch-and-cut codes (ATSP, generalized TSP, orienteering, VRP) | *Facets of the Asymmetric Traveling Salesman Polytope*, MOR 16:42–56 (1991), sole author, DOI 10.1287/moor.16.1.42 | the Balas collaboration from 1989 [practice] | *New facets of the STS polytope generated from known facets of the ATS polytope*, DO 3 (2006), DOI 10.1016/j.disopt.2005.10.001 | TSP-book chapters 2002 [S1] |
| 1993–2002 | Italian railways: crew management, rostering, timetabling | FS projects ALPI (1993–96), FASTER (1994–97), FARO (1995–98); FS code prizes 1994 and 1995 [S1] | industrial code competitions with real data [practice; trigger inferred] | *Modeling and Solving the Train Timetabling Problem*, OR 50:851–861 (2002), DOI 10.1287/opre.50.5.851.362 | Caprara, Toth, Vigo; FS staff (Guida) |
| 2000–2017 | Netherlands Railways crew, timetable and robustness; real-time rescheduling | *Crew Scheduling for Netherlands Railways "Destination: Customer"*, LNEMS 2001, DOI 10.1007/978-3-642-56423-9_11 | collaboration with Leo Kroon; EU project ARRIVAL (2005–08) [S1] [practice] | *A Lagrangian Heuristic for Robustness, with an Application to Train Timetabling*, TS 46:124–133 (2012), DOI 10.1287/trsc.1110.0378; *Using a general-purpose MILP solver for the practical solution of real-time train rescheduling*, EJOR 263:258–264 (2017), DOI 10.1016/j.ejor.2017.04.057 | Wagner finalist 2004, Edelman 2008 |
| 1998–2003 | Statistical disclosure control (cell suppression, controlled rounding) | *Models and Algorithms for Optimizing Cell Suppression in Tabular Data with Linear Constraints*, JASA 95:916–928 (2000), DOI 10.1080/01621459.2000.10474282 | EU Esprit "SDC" (1995–97) and EU "CASC" (2000–04) [S1]; trigger and exit match these windows [inferred] | *Partial cell suppression*, Statistics and Computing 13:13–21 (2003), DOI 10.1023/a:1021927424942 | with J.-J. Salazar-González |
| 1996–2011 | General MIP cuts and closures | *{0, 1/2}-Chvátal-Gomory cuts*, MPA 74:221–235 (1996), DOI 10.1007/bf02592196 | moving from TSP odd-structure cuts to general MIP [inferred] | *A relax-and-cut framework for Gomory mixed-integer cuts*, MPC 3:79–102 (2011), DOI 10.1007/s12532-011-0024-x | Caprara, Lodi, Salvagnin, Zanette, Balas |
| 2002–2009 (plus 2014, 2026) | General-purpose MIP heuristics: local branching, feasibility pump, "just MIP it" | Aussois talk Jan 2002 and Oberwolfach 2002 [S3]; *Local branching*, MPB 98:23–47 (2003), DOI 10.1007/s10107-003-0395-5; *The feasibility pump*, MPA 104:91–104 (2005), DOI 10.1007/s10107-004-0570-3 | black-box solvers had become usable tools [stated S6, S9] | FP 2.0 (2009, above); *Boosting the feasibility pump*, MPC 6:255–279 (2014), DOI 10.1007/s12532-014-0068-9; return in 2026 [S23] | Lodi; students Bertacco and Salvagnin |
| 2008–2012 | Gomory's cutting planes revisited (lexicography, pure cutting planes) | Aussois 2008 talk; *Can pure cutting plane algorithms work?*, IPCO 2008, DOI 10.1007/978-3-540-68891-4_29 | reading the method closely ("looking inside Gomory", talk title) [practice] | *On the enumerative nature of Gomory's dual cutting plane method*, MPB 125:325–351 (2010), DOI 10.1007/s10107-010-0392-4; MPA 130 (2011, above) | Balas, Zanette |
| 2010–2016 | Behaviour of tree search: erraticism, sampling, parallel SelfSplit, backdoors, symmetry | EURO 2012 talk "erraticism" [S3]; *Exploiting Erraticism in Search*, OR 62:114–122 (2014), DOI 10.1287/opre.2013.1231 | seed-only performance swings in CPLEX 12.2 [stated S8 p.7] | *Improving branch-and-cut performance by random sampling*, MPC 8:113–132 (2016), DOI 10.1007/s12532-015-0096-0; *SelfSplit parallelization for mixed-integer linear programming*, COR 93:101–112 (2018), DOI 10.1016/j.cor.2018.01.011 | Monaci, Salvagnin; CPLEX developers (Tramontani) |
| 2014–2020 | "Thinning out": Benders, node-based Steiner, bilevel, interdiction, bilinear | DIMACS 2014; *Thinning out Steiner trees*, MPC 9:203–229 (2017), DOI 10.1007/s12532-016-0111-0 | a DIMACS challenge observation plus Occam's razor [stated S10 pp.2,13,15] | *A branch-and-cut algorithm for Mixed-Integer Bilinear Programming*, EJOR 282:506–514 (2020), DOI 10.1016/j.ejor.2019.09.043 | Ljubić, Sinnl, Monaci |
| 2015–2022 (return 2026) | Machine learning: SVM by MILP, DNN as 0-1 MILP, SGD training, learning in local branching | *Fast training of Support Vector Machines with Gaussian kernel*, DO 22:183–194 (2016), DOI 10.1016/j.disopt.2015.03.002; arXiv:1712.06174 | his argument that implementation is part of the method, with deep learning's success as the example [stated S12 p.3]; B&C framed as overfitting [stated S8 p.19] | *Learning to Search in Local Branching*, AAAI 36:3796–3803 (2022), DOI 10.1609/aaai.v36i4.20294 | master's students; Lodi's group |
| 2014–2026 | Wind-farm layout and cabling; COVID distancing by analogy; EndoWake | IMI talk Oct 2014 [S9]; *Optimal Turbine Allocation for Offshore and Onshore Wind Farms*, Mathematics for Industry (Springer Japan), DOI 10.1007/978-4-431-55420-2_4 | co-author Martina Fischetti's MSc and then industrial PhD at Vattenfall [inferred from S9 p.1 and S50] | *Integrated Layout and Cable Routing in Wind Farm Optimal Design*, MS 69:2147–2164 (2023), DOI 10.1287/mnsc.2022.4470; EndoWake 2026 [S32–S34] | an industrial setting (Vattenfall) |
| 2019–2026 | Padova applied MIP: VRP, home delivery, assortment, pickup and delivery | *An integrated local-search/set-partitioning refinement heuristic for the CVRP*, MPC 14:749–779 (2022), DOI 10.1007/s12532-022-00224-2 | the PRIN 2022 grant "REWIND" (home delivery) [stated S15 p.1] | *Models and algorithms for the TWATSP with stochastic travel times*, EJOR 329:96–111 (2026), DOI 10.1016/j.ejor.2025.07.034 | Cavaliere, Roberti, Salvagnin, Palasgo |
| Sep–Nov 2026 | AI-assisted revisits plus reproducibility packages | FP manuscript [S23]; arXiv:2609.13922, 2609.40157, 2610.07844, 2610.39503 | declared AI assistants [stated S23 p.25, S32 p.27, S33 p.28, S34 p.23]; a prescription the field left untested [stated S23 pp.1–2]; a standing objection to his 2018 claim [stated S31 pp.1–2] | ongoing; all unrefereed | solo, or with Martina Fischetti |

### 3.1 Turn by turn: what moved him

- **Into railways (1993–94), through competitions and data.** Ferrovie dello Stato ran the projects ALPI, FASTER and FARO and gave prizes to the best computer codes: set covering in 1994, rostering in 1995 [S1, S48]. The published methods followed: *Modeling and Solving the Crew Rostering Problem* (OR 46:820–830, 1998, DOI 10.1287/opre.46.6.820) and *A Heuristic Method for the Set Covering Problem* (OR 47:730–743, 1999, DOI 10.1287/opre.47.5.730). [practice P; trigger inferred: competition first, journal paper 3–5 years later]
- **Into general-purpose MIP heuristics (2002), because a new tool had matured.** The 2007 Aussois deck states the aim as embedding a black-box 0-1 MIP solver inside a heuristic framework that helps it find improved solutions. Its slogan for choosing which variables to fix is "just MIP it!" [S6 pp.4, 9]. In 2014 he gives the era reason: MILP had recently become a feasible tool for huge real problems, and MIP-based heuristics can be easier to design than ad-hoc ones [S9 pp.2–3]. The ideas were premiered at the January Aussois workshop, year after year: local branching 2002, {0,½}-cuts 2003, the feasibility pump and a VRP heuristic 2004, cyclic-group cuts 2005, knapsack closure 2006, bracket-and-fix 2007, "looking inside Gomory" 2008, then SelfSplit 2014, Steiner trees 2015 and bilevel 2016 [S3]. The homepage shows a photo of "the first slide of the very first Feasibility Pump talk" [S1]. [stated + practice, P]
- **Into the solver's behaviour (2012), because of an anomaly.** His ISCO 2014 plenary sets two runs of IBM ILOG CPLEX 12.2 side by side: default parameters, deterministic runs on the same PC, "only change is the initial random seed", and node counts and times that differ by large factors [S8 p.7]. He credits the chaotic-system reading to E. Danna (2008; that source was not checked) [S8 p.8]. He reframes branching and cutting decisions taken on one fractional point as a statistical sample prone to overfitting [S8 p.19], which is machine-learning vocabulary already in 2014. The same deck says the concurrent root cut loops from the random-sampling work (Fischetti, Lodi, Monaci, Salvagnin, Tramontani) have been in the CPLEX default since version 12.5 [S8 p.11]. So this line reached a commercial solver through co-authors in the CPLEX team. [stated, P]
- **Into Benders, bilevel and thinning out (2014–15), because of a challenge observation and a contrarian bet.** His Larnder lecture traces the Steiner work to the DIMACS 11 challenge, where many hard instances had uniform arc costs, so the edge variables could be projected out [S10 p.15]. He presents Benders as a perfect fit for facility location that was unfashionable at the time: "not sexy nowadays as more complicated schemes are preferred #paperability?" [S10 p.16]. He adds that few MIP people actually use it [S10 p.17]. For the root-node stabilization he reports that the first quick in-out ("chase the carrot") implementation worked well enough that they did not try to improve it [S10 p.26, paraphrase]. [stated, P]
- **Into machine learning (2015–2018), through an implementation argument and students.** The 2015 Larnder lecture opens with MILP-based SVM training as an overfitting case study, with results computed in CPLEX 12.5 [S10 pp.3–10]. At ISMP 2018 he argues that implementation is not just coding, asking whether deep learning would have succeeded without efficient backpropagation implementations [S12 p.3]. On the same deck: "Describing an Algorithm without Implementation is like stating a Theorem without Proof" [S12 p.4]. The Dagstuhl deck of February 2018 presents a ReLU network as a 0-1 MILP for fixed weights and uses it for adversarial instances; it cites arXiv:1712.06174, accepted at CPAIOR 2018 [S11 pp.3–7]. The published version is *Deep neural networks and mixed integer linear optimization*, Constraints 23:296–309 (2018), DOI 10.1007/s10601-018-9285-6. Master's students Mandatelli (2018) and Stringher (2019) carried the SGD-training studies [S40, S41]. [stated + practice, P]
- **Into wind farms (2014), through a co-author.** The IMI talk of October 2014 credits joint work with Martina Fischetti and Michele Monaci and walks from ad-hoc 1-opt and 2-opt heuristics to MIP-based proximity search [S9 pp.1, 7–20]. Martina Fischetti was then finishing an MSc at Padova and Aalborg, and she spent 2015–2018 as an industrial PhD at Vattenfall [S50]. Linking the timing to her career is my inference. [practice P + inferred]
- **Into COVID distancing (2020), by analogy.** He presents facility location under distancing constraints as "similar" to turbine layout, so "we can borrow models and algorithms from wind farm literature" [S13 p.23]. The results were produced by wind-farm layout software from Double-Click SRL, Padua; his relation to that company was not checked [S13 p.16]. Published as *Safe distancing in the time of COVID-19*, EJOR 304:139–149 (2023), DOI 10.1016/j.ejor.2021.07.010. [stated, P]
- **Into Padova applied work (2022–2025), through a grant and a local team.** The ODS 2025 deck acknowledges PRIN 2022 project 20229ZWC97 "REWIND" (home delivery services) [S15 p.1]. Its workflow, in order: compare models with CPLEX as a black box, then with CPLEX's built-in Benders, and only then code a specialized Benders with CPLEX callbacks [S15 pp.7–11]. [stated, P]
- **Into the 2026 revisits, through a new tool and two unexamined claims.**
  - *Feasibility Pump with Objective Cutoff* (sole author; submitted to Mathematical Programming Computation). The 2005 FGL paper had prescribed a recovery step together with the cutoff. Common implementations, SCIP's included, do not follow that prescription, and its cost had never been measured. Its conclusion recommends "not a new heuristic but an old one, restored" [S23 pp.1–2, 19].
  - *Minibatch persistency, eight years later* (sole author) accepts, as correct and methodological, the 2019 objection that the 2018 study had not tuned its baseline. He met that objection with a pre-registered design [S31 pp.1–2].
  - The AI-use declarations say that Anthropic Claude models (named "Claude Fable 5.1", "Claude Opus 5", "Claude Fable 5") drafted and edited text, wrote and debugged code, and served as internal adversarial readers. ChatGPT ("GPT-5.6 sol") or OpenAI Codex provided independent adversarial audits. The authors say they verified all content and take responsibility [S23 p.25; S32 p.27, "as programming assistants for the experimental code"; S33 p.28; S34 p.23].
  - [stated, P] The declarations say how the tools were used, not why he took them up. The why is a gap.

---

## 4. Entry and exit relative to the field

| Topic | When he entered | Relative timing (tag) | When he left |
|---|---|---|---|
| MIP neighbourhood search | Local branching, Aussois Jan 2002; MPB 98 (online 2003) | **earlier** than RINS by Danna, Rothberg and Le Pape (*Exploring relaxation induced neighborhoods to improve MIP solutions*, MP 102:71–90, online May 2004, DOI 10.1007/s10107-004-0518-7), which his 2007 deck presents as a later fixing heuristic [S6 p.8, S54] [practice + inferred] | heuristics papers to 2009; joint FP paper 2014; LB with ML 2022; FP again 2026 |
| Performance variability | 2012 talk, OR 2014 paper | **after** the observation, which he credits to Danna 2008, and as the first to exploit it (bet-and-run, sampling, SelfSplit) [stated S8 pp.8, 12] | last SelfSplit paper 2018 |
| Benders revival | 2014–15 (UFL and CFL) | **contrarian**: he called Benders unfashionable at the time [S10 p.16]; his 2026 lecture notes that Benders has been in the CPLEX general MIP solver since version 12.7 [S17 p.19] [stated; ordering inferred] | still in use 2025–26 (TWATSP; the Benders cut in DW-EndoWake [S34]) |
| MILP models of neural networks | arXiv:1712.06174, 17 Dec 2017 | **concurrent**: Tjeng, Xiao and Tedrake, *Evaluating Robustness of Neural Networks with Mixed Integer Programming*, arXiv:1711.07356, posted 20 Nov 2017 [S56] [inferred] | no further DNN-as-MILP paper after 2018 |
| Minibatch reuse | arXiv:1806.07353, June 2018 | **early**: the 2026 paper places it about 13 months before Choi et al. generalized it as data echoing (*Faster Neural Network Training with Data Echoing*, arXiv:1907.05550) [S31 p.1, S56] | left after 2018; came back in 2026 to test it under the objection |
| Bilevel and interdiction | IPCO 2016 (DOI 10.1007/978-3-319-33461-5_7) | not assessed in this run | last paper IJOC 31:390–410 (2019), DOI 10.1287/ijoc.2018.0831; afterwards only as tutorial material (VeRoLog 2025 part 2; AIROyoung 2026 part 2) [S3, S18] [practice] |
| Polyhedral ATSP | 1989–1991 | not assessed | last 2006 (STS from ATS facets) [practice] |
| Statistical disclosure control | 1998 | not assessed | 2003; matches the end of the EU funding windows [inferred] |
| Railways | 1993 | not assessed | 2017 (real-time rescheduling; TRISTAN 2016 talk) [practice] |

---

## 5. Failures, abandoned directions, unpublished work, revisions and retractions

- **Yoyo search (2009), never published as a paper, later absorbed.** *Yoyo search: a bisection cutting-plane method* (Fischetti and Salvagnin, working paper, 20 Nov 2009) describes two convergent sequences of points, LP vertices and internal points; the point to be cut "swings in and out of the oracle's reach" [S20 p.1]. Its abstract calls the computational results preliminary. It is not in his publication list [S1], and the file was posted in 2019 [S2]. The idea appears in short form as *An In-Out Approach to Disjunctive Optimization* (CPAIOR 2010, LNCS 6140:136–140, DOI 10.1007/978-3-642-13520-0_17). The 2016 Benders preprint then says that, instead of a real bundle method, they used a simple in-out variant in the spirit of earlier work including that 2010 paper [S22 p.12]. That variant is the stabilization of the Management Science paper (DOI 10.1287/mnsc.2016.2461). [practice P; the yoyo-to-in-out link is my inference from content]
- **An extended draft shrunk to a note.** *Minimal Infeasible Subsystems and Benders' cuts* (Fischetti, Salvagnin, Zanette; a Mathematical Programming manuscript, revised Sept 2009, 17 pp.) [S21] appeared as *A note on the selection of Benders' cuts*, MPB 124:175–182 (2010), DOI 10.1007/s10107-010-0365-7. Why it was shortened is not stated. [practice P]
- **The 2018 minibatch claim, narrowed eight years later.** The 2018 abstract reported "significantly faster convergence" for small reuse factors [S35, abstract of arXiv:1806.07353]. Its arXiv comment says it was submitted to an international conference, and the homepage lists it only as a technical report [S1, S35]. Whether it was rejected is not stated. In 2026 he concedes that the 2018 evidence could not settle the question [S31 p.2]. He now concludes that reuse buys "neither speed nor energy but data" [S31 p.1, abstract], and only at large batch sizes. [stated, P] See Contradictions.
- **Other preprints left as technical reports.** *Finding First and Most-Beautiful Queens by Integer Programming* (arXiv:1907.08246) extends *Chasing first queens by integer programming* (CPAIOR 2018, DOI 10.1007/978-3-319-93031-2_16) and stays a technical report [S1, S35]. The bracket-and-fix heuristic (Aussois 2007 [S6]) has no stand-alone paper in his list; whether it went into *Just MIP it!* (2009, DOI 10.1007/978-1-4419-1306-7_2) was not checked. [practice]
- **Negative results he reports himself.**
  - ISMP 2018: his callback-based MIQP code was as fast as SCIP, but SCIP solved more instances in the time limit, so he calls SCIP the more robust solver; he also says a bilinear-specific heuristic was still missing [S12 p.16, paraphrase].
  - 2026 FP study [S23 pp.19–20]: a cheap fallback is harmful everywhere. The shallow-target advantage is called a lead, not an established result, after Holm correction. Using the cutoff as the pump's perturbation solved 147 instances against 158 for random flips. The embedded branch-and-cut experiment was not run.
  - DW-EndoWake: the earlier branch-and-check had left the larger grids open after one hour, and the new paper is the fix [S34 abstract].
  - [stated, P]
- **Revisions made in the open (2026).**
  - GPU-EndoWake v2: "formal terms replace the metaphors of v1"; v3 states the fixed wake expansion rate and its effect [S33, arXiv comment].
  - Its Zenodo package withheld the local searches, sector quadrature and fast evaluator in v1, then released them in v2.0.0 under the PolyForm Noncommercial License [S29].
  - The FP README says earlier exploratory campaigns were contaminated by a SCIP defect and were left out of the package [S24].
  - A commit of 2026-09-16 adds three campaigns that answer a "fresh-context audit" [S24].
  - [stated/practice, P]
- **Retracted papers or errata: none found.**

---

## 6. Era and resource context

| Era | Tools and compute (as documented) | Team | Seniority | Evidence |
|---|---|---|---|---|
| 1982–1993 | not documented in the sources read | Bologna group, 2–3 authors | PhD student, then assistant professor | [S1, S52] |
| 1993–2003 | industrial and EU project funding (FS ALPI, FASTER, FARO; Esprit SDC; CASC); code competitions | Caprara, Toth, Vigo, Salazar-González | associate, then full professor at three universities | [S1] |
| 2002–2009 | commercial black-box MIP solvers (CPLEX is named in his later decks); Aussois as the launch venue | Lodi; PhD students Bertacco, Salvagnin, Zanette; a stream of laurea students | full professor, Padova | [S3, S6, S36–S38] |
| 2010–2016 | CPLEX 12.2 to 12.5 with callbacks; clusters for SelfSplit; co-authors in the CPLEX team | Monaci, Salvagnin, Lodi, Tramontani | senior, prize-winning | [S8, S10] |
| 2014–2020 | CPLEX callbacks for Benders and bilevel; large UFL instances; DIMACS challenge | the Vienna and ESSEC group (Ljubić, Sinnl) | Larnder Prize 2015 | [S10, S22] |
| 2015–2022 | CPLEX 12.5 (SVM study) and 12.8 (ISMP 2018); deep-learning experiments (CIFAR-10, AlexNet in 2018) | master's students; Lodi's group | ISMP 2018 keynote | [S10, S12, S35] |
| 2022–2025 | CPLEX as a black box, CPLEX's own Benders, CPLEX callbacks; PRIN 2022 funding | Padova colleagues (Salvagnin, Roberti), Cavaliere, Palasgo | about 65 | [S15, S16] |
| 2026 | SCIP and SoPlex at pinned git commits (dba4b2a, 24 Aug 2026; f0dbc81), Gurobi 13.0.3, the DEI SLURM cluster (4 cores and 14 GB per task); GPUs and CUDA, OpenFOAM RANS and Hexaly for EndoWake; OSF pre-registration; GitHub and Zenodo; AI assistants | solo, or with Martina Fischetti | 67–68 (born 1958), still a full professor | [S23–S34, S48] |

[inferred] The 2026 practice of pre-registration, factorial designs with Holm correction, independent revalidation of every solution and scripts that regenerate every number appears only after the AI assistants were adopted. It should not be projected back onto his 2002–2019 practice, which the sources show as quick prototypes, CPLEX callbacks and MIPLIB-style tables.

---

## 7. Latest activity (2025-11-08 to 2026-11-08)

| Date | Item | Evidence | Tag |
|---|---|---|---|
| 2026 (print) | *Models and algorithms for the TWATSP with stochastic travel times*, EJOR 329(1):96–111, DOI 10.1016/j.ejor.2025.07.034 (online August 2025) | [S54], [S1] | [practice] P |
| 2026-02-09 | AIROyoung lectures, Padua: *Branch-and-Cut is our swiss army knife* (part 1: B&C and Benders; part 2: intersection cuts and bilevel). These reuse the 2018 and 2025 material | [S17], [S18] | [practice] P |
| 2026-04-29 and 2026-10-31 | OR2 and OR1 teaching folders updated, so he is still teaching | [S5] | [practice] P |
| 2026-09-04 to 2026-09-17 | GitHub repo `mfischetti-arch/fp-objective-cutoff`: 13 commits, manuscript v3 dated 2026-09-07, tag `mpc-submission-1`; Zenodo package 10.5281/zenodo.22810777 (MIT) and raw SCIP logs 10.5281/zenodo.22810848 (CC BY 4.0), from a factorial campaign on 424 MIPLIB 2017 instances, 12 variants and 5 seeds | [S24], [S25], [S26] | [practice] P |
| 2026-09-12 | *Minibatch persistency, eight years later: what batch reuse costs in steps and joules, and what it saves in data*, arXiv:2609.13922 (sole author; pre-registered on OSF, embargoed). A text search of v1 found no AI-use statement | [S31] | [practice] P |
| 2026-09-10 and 2026-09-28/30 | *EndoWake: Modeling Wind by Linear Programming for Wind Farm Layout Optimization*, arXiv:2609.40157, with Martina Fischetti; Zenodo preprint 10.5281/zenodo.23001174 marked as submitted to EJOR (revised 2026-09-11); replication package 10.5281/zenodo.22017424 | [S27], [S28], [S32] | [practice] P |
| 2026-10-03 | Uploads to the slides folder: two EndoWake videos (one titled for OR, one for wind); *Backpropagation for people suffering from derivative allergy* (slides and video, "the circuit engineer's way to see it") | [S3], [S19] | [practice] P |
| 2026-10-06 to 2026-11-04 | *GPU-accelerated wind farm layout search with a distilled endogenous wake model (EndoWake)*, arXiv:2610.07844, versions v1 to v3; replication v2.1.0, 10.5281/zenodo.23955408 | [S29], [S33] | [practice] P |
| 2026-10-29 | *A Dantzig-Wolfe reformulation of the EndoWake model for optimal wind farm layouts*, arXiv:2610.39503 (submitted to a journal); package 10.5281/zenodo.23636074, whose script regenerates all 2167 macros | [S30], [S34] | [practice] P |
| 2026-10-30 | Homepage updated (HTTP Last-Modified header) | [S1] | [practice] P |
| 2026-11-02 | Video `2026_svm_telecom_video.mp4` uploaded; not viewed. The file name suggests a return to the "telecommunication interpretation" of the Gaussian kernel from the 2015 SVM study [S10 p.5] | [S3] | [inferred] |
| 2026 (date unknown) | *A digital twin of Fermat in 1637: reconstructing the marvellous proof and locating where it fails*, ResearchGate technical report, sole author; **not read** (403) | [S1], [S53] | [practice] P |
| 2026 | *Feasibility Pump with Objective Cutoff: A Computational Study*, ResearchGate technical report and GitHub manuscript, sole author, submitted to Mathematical Programming Computation; unrefereed | [S1], [S23], [S24] | [practice] P |

Scholar snapshot on 2026-11-08: 20,048 citations, h-index 75 [S53]. [S]

---

## 8. Notes for the Phase-2 synthesis (all [inferred])

- **Layer 2 (choosing problems).** His problems come from four places:
  1. industrial code competitions and projects (FS 1994–95, NS 2000–08, PRIN 2022);
  2. anomalies in the tool he uses (seed variability; Kelley's slow convergence);
  3. a co-author's application (wind farms);
  4. his own old ideas that the field adopted only in part (the FP cutoff and its recovery; minibatch reuse).

  Why now: when the black-box tool matured (2002), when a method was unfashionable but fitted the problem (Benders 2015), and when a critique stood unanswered (2026).
- **Layer 3 (generating ideas).** Ideas come by analogy and transfer: wind farms to COVID, telecom signals to kernels, circuit amplifiers to backpropagation, machine-learning overfitting to branching. Another recurring move is to "MIP it", that is, to hand the design subproblem of a heuristic or separation step to the MIP solver.
- **Layer 7 (organizing research).**
  - The yearly Aussois workshop served as the launch venue.
  - A laurea or master's thesis turned into a paper within 0–4 years.
  - Partnerships of about 10 years overlapped.
  - In 2026 the work moved to solo and two-author projects with declared AI assistants and public replication packages.
- **Caution for the skill.** The 2026 practices are new, unrefereed and tied to new tools; treat them as a separate era. The wind-farm and EndoWake work is joint with Martina Fischetti and is not his voice alone.

---

## 9. The trajectory as the full texts show it (deep reading, added 2026-11-28)

Source: the paper cards and their synthesis, `08-deep-reading-synthesis.md` §8–§9. Card citations such as `[S001 p. 3]` are paper-card ids (a letter and three digits, as in `../sources/papers/INDEX.md`) at the `[[page N]]` file pages of the texts the cards read; they are not the S1–S53 source keys of this note. Nothing in §0–§8 is changed; where this section refines an item above, it says so. Coverage on 2026-11-28: 202 distinct works indexed, 132 open full texts, 130 read in full and 1 in part, 56 abstract only, 11 metadata only, 4 skipped; 165 studies after merging versions, 112 of them with a full or partial text. Nothing that `holdout.md` seals is used here.

### 9.1 Work groups per period (all read levels; S188 and S192, supervised theses, excluded)

| Period | Groups | Main topics (groups) |
|---|---|---|
| 1986–1990 | 12 | approximation and complexity 6; bounding and branch-and-bound for routing and scheduling 6 |
| 1991–1995 | 19 | polyhedral combinatorics 10; bounding and branch-and-bound 5; branch-and-cut codes 1; cutting planes 1; complexity 1; other applications 1 |
| 1996–2000 | 22 | railway and crew planning 6; polyhedral 4; branch-and-cut codes 4; statistical disclosure control 3; set covering heuristics 2; cutting planes 2; bibliography 1 |
| 2001–2005 | 18 | branch-and-cut codes 6; railway and crew 4; general-purpose primal heuristics 3; disclosure control 2; cutting planes 1; polyhedral 1; other applications 1 |
| 2006–2010 | 30 | cutting planes, closures and the cut loop 10; primal heuristics 5; railway robustness 4; Benders 3; robustness and uncertainty 2; other applications 2; tree search 1; branch-and-cut 1; polyhedral 1; editorial 1 |
| 2011–2015 | 16 | cutting planes and the cut loop 5; tree search, variability and parallelism 4; primal heuristics 4; symmetry 1; wind farms 1; survey 1 |
| 2016–2020 | 29 | machine learning from the MILP side 5; bilevel and interdiction 4; primal heuristics 3; Benders 3; other applications 3; books and surveys 3; nonlinear MIP 2; tree search 2; branch-and-cut 1; railway 1; symmetry 1; wind farms 1 |
| 2021–2026 | 16 | primal heuristics and matheuristics 5; wind farms 3; Benders and decomposition 3; other applications 3; machine learning 2 |

The Bologna years are thin in the full texts: 27 of the 31 work groups of 1986–1995 are abstract or metadata only, so how he worked then is read off a few texts [S049 pp. 4, 22; S030 pp. 5–6; S060 p. 11; S114 pp. 2, 4] and the later surveys [S056; S102].

### 9.2 Turns visible in the full texts

- **1996–2001, problem-specific codes for partners**: {0,1/2} and mod-k cuts [S022 pp. 5–10; S139 pp. 3–9]; routing branch-and-cut [S005; S009; S013; S125]; Lagrangian codes for the Italian and Dutch railways [S012 pp. 9–11; S017 pp. 12–16; S004 pp. 5–14]; statistical disclosure control [H003; S069; S073]. No general-purpose MIP solver as subroutine in these codes [S012 pp. 9, 11; S013 pp. 18, 22, 26], at most an LP engine or a referee for bounds [S004 p. 21], but projection into cuts [S069 pp. 3, 5–6], an in-out precursor credited to Reinelt [S125 pp. 11–12] and same-code ablation [S060 p. 11] are already there.
- **Turn 1, 2000–2003: the solver becomes the subroutine.** The 2000 survey finds general-purpose ILP solvers competitive with special-purpose exact codes for set covering [S003 p. 9]; the soft-fixing refiner of the crew code becomes one constraint on a generic MIP [S001 p. 3]; general codes are a third the size of the problem-specific one [S064 p. 12].
- **2002–2010, general-purpose devices**: local branching, the pump and its general-integer and propagation versions [S001; S007; S026; S041]; MIPping closures [D003; S033; S142]; {0,1/2}-cuts inside CPLEX [S070]; the MIPping survey [S096]; robust railway timetabling with a separate validator [D004; S018; S010; D007].
- **Turn 2, 2008–2011: from the cut to the loop.** After component-side cures [D003 pp. 8–9; S024 pp. 2, 4] the loop becomes the object [S174 p. 1; S106 p. 2; D009 p. 8; S074 p. 14; S095 pp. 2–6].
- **2010–2016, tree search and variability**: pruning moves, nonchimerical branching, backdoors [S124; D012; S063]; erraticism and sampling [S055; S094 p. 5]; self-splitting [S111; D017]; symmetry by aggregation [S067; D013]; proximity search [S052; S154; S086].
- **Turn 3, 2015–2018: thinning out and general-purpose solvers for harder classes**: the Steiner and UFL redesigns [S195 p. 2; S011; S040]; bilevel and interdiction on top of a MILP solver [S016 p. 6; S027; S090; S038]; machine learning seen from the MILP side [S109; S054; S008; S133; D018].
- **2019–2025, applied Padova MIP and students**: vehicle routing with set-partitioning recombination [S130; S168]; learning in local branching [S076]; wind farms and distancing with Martina Fischetti [S078; S100]; fix-propagate-repair moved into a commercial solver [S126 pp. 24, 26]; time-window TSP with Benders [S144; S172].
- **Turn 4, September–November 2026: re-tests and the apparatus.** Sole-author re-tests of his own 2005 and 2018 claims [S164; S163]; two-author wind-farm preprints with a trusted judge and certificates [S143; S150; S162]; an AI-written note [S161 p. 4]; pre-registration [S163 pp. 8–9], declared families with Holm's correction [S164 p. 13].
- **What stayed constant**: the relaxation drives the heuristic, from Lagrangian costs in 1997–2001 [S012 p. 10; S004 pp. 5–14] to the LP point and the relaxation grip of 2005–2016 [S007 p. 3; S052 p. 5; S086 p. 2]; ablation by removal from 1995 to 2025 [S060 p. 11; S126 pp. 24–25]; same-machinery comparisons from the 1990s [S060 p. 11; S077 p. 10] to the dummy callback [S070 p. 10] and the 2026 harnesses [S164 pp. 11, 13]; the closing lesson from 1996 to 2026 [S022 p. 16; S164 p. 19]; instances made public from 2001 [S013 p. 22; S125 pp. 24–25].

### 9.3 Collaboration by period (work groups; 08 §9)

| Period | Groups | Sole-author | Most frequent coauthors (groups) |
|---|---|---|---|
| 1986–1990 | 12 | 3 | Toth 7, Martello 4, Carpaneto 2, Dell'Amico 1 |
| 1991–1995 | 19 | 4 | Toth 7, Balas 4, Martello 2, Caprara 2, Salazar González 2 |
| 1996–2000 | 22 | 0 | Toth 9, Caprara 8, Vigo 5, Salazar González 5, Guida (FS) 3 |
| 2001–2005 | 18 | 0 | Toth 6, Lodi 6, Salazar González 4, Caprara 2, Kroon (NS) 2 |
| 2006–2010 | 30 | 1 | Salvagnin 7, Lodi 5, Monaci 4, Zanette 3, Balas 2, Bertacco 2, Caprara 2 |
| 2011–2015 | 17 | 0 | Monaci 9, Salvagnin 4, Zanette 3, Lodi 3, Balas 2, Martina Fischetti 2 |
| 2016–2020 | 29 | 4 | Monaci 13, Salvagnin 10, Sinnl 8, Ljubić 7, Lodi 3, Martina Fischetti 2 |
| 2021–2026 | 16 | 4 | Martina Fischetti 5, Roberti 4, Salvagnin 3, Cavaliere 3 |

Totals over all periods: Toth 32 groups, Monaci 27, Salvagnin 24, Lodi 18, Caprara 14, Salazar González 12, Balas 11, Martina Fischetti 9, Martello 9. The "we" of co-signed texts cannot be split; in one 2014 paper he is fourth of six and the text refers to Fischetti and Salvagnin in the third person [S098 p. 18]; several author lists are alphabetical [S040; S059; S097]. Partners appear as coauthors or data sources: Ferrovie dello Stato planners [S012; S053; S081], Netherlands Railways [S061; S034; S015], an Alstom instance set [S059 p. 2].

### 9.4 Refinements of items above

- **§2.3 (thesis-to-paper pipeline, inferred)**: confirmed in the full texts: Salvagnin's 2005 master's thesis into the 2009 *Just MIP it!* chapter [S096 pp. 19, 27–28]; a 2003 dissertation into a 2009 paper, supervision not stated [S046 pp. 2, 34]; Martina Fischetti's thesis into a 2014 paper [S154 p. 2]; variant: a 2012 master's thesis into a sole-authored paper that credits the student in the text [S109 pp. 1, 4, 8, 14–15, 19].
- **§3 (2002–2009 row) and §3.1 (into general-purpose heuristics)**: the turn is signalled in print in 2000 [S003 p. 9]; the soft-fixing origin is in the paper [S001 p. 3].
- **§3.1 (into Padova applied work)**: the workflow order of the ODS 2025 deck is in the 2026 paper: CPLEX as a black box, its built-in Benders to screen splits, then a specialized Benders in callbacks [S144 pp. 4–8, 12].
- **§3.1 (the 2026 revisits)**: AI assistance is declared in S143 [S143 p. 27], S150, S161 and S164; S163 carries no statement on it; in S161 the assistant did everything but the idea and the supervision [S161 p. 4].
- **§5 (failures and revisions)**: an erratum of their own 1998 definition printed inside a 2002 survey [S047 p. 50]; an implementation error of an earlier submission corrected in 2026, every dependent number recomputed [S150 pp. 10, 30]; the pump's enumeration from the almost-feasible point by local branching is in a preprint of 16 February 2004 [S085 pp. 1, 4], published 2008.
- **§6 (era and resources)**: code was mostly closed before 2026, with exceptions: the 2017 bilevel solver, its instances and optimal values, announced as released through co-author Sinnl's page (availability not checked by the reader) [S016 pp. 3, 7, 22, 37, 42], and three 2022 GitHub repositories from papers led by Liu and Cavaliere [S076 arXiv v2 pp. 17, 25; S130 pp. 7, 22; S168 p. 1]; 2025 code on request [S126 p. 27]; QAP model files and logs on request only [S067 p. 10].
- **The Benders and cut-loop line**: the gs250a-1 traces are already in the April 2015 report [S195 pp. 15–17]; the controlled-oracle test is in the 2009 yoyo manuscript [S174 pp. 6–7].

---

## Contradictions

1. **Minibatch persistency, 2018 against 2026.** In 2018 small reuse factors gave "significantly faster convergence" with comparable or better generalization (abstract of arXiv:1806.07353 [S35]). In 2026 reuse buys "neither speed nor energy but data", and only at large batch sizes; at B = 32 it reads more fresh tokens than the baseline (abstract of arXiv:2609.13922 [S31]). He accepts the critique as methodological [S31 p.2]. Both claims are kept as they stand. [stated, P]
2. **"Theorem" or "Conjecture" on the same slide.** In 2018 and 2025 the branch-and-cut slide reads "Theorem. Using cuts within an enumerative scheme is good." (VeRoLog 2025, p.6 [S14]; same wording ISMP 2018 p.6 [S12]). In 2026 the same slide reads "Conjecture: Using cuts within an enumerative scheme is good." while still followed by "Proof." (AIROyoung, p.2 [S17]). Not reconciled. [practice, P]
3. **The simplicity ethos against the 2026 apparatus.** In 2015 he urged simplicity ("Be simple (if you can)!" closes the Larnder lecture) and said the first quick implementation was good enough not to improve [S10 pp.26, 29]. In 2026 the same author ships pre-registered factorial campaigns: 25,440 runs, Holm-corrected comparison families, 2167 regenerated macros [S24, S30]. This tension is my reading, not a stated self-contradiction. [inferred]
4. **His homepage against Crossref.**
   - First paper: ORL volume 6 on the homepage, volume 5 in Crossref.
   - *Integrated layout and cable routing*: 2022 on the homepage (online), MS 69 (2023) in Crossref.
   - *Fix-propagate-repair*: 2024 on the homepage, MPC 17 (2025) in Crossref and Scholar.
   - *Optimal Turbine Allocation*: 2015 on the homepage, 2016 in Crossref.
   - JASA 95: pages 915–928 on the homepage, 916–928 in Crossref.
   - The COAP award is named "2016 COAP Best Paper Award" but listed under 2017.
   - [S1, S54]
5. **Name of the 1987 prize.** The homepage and UNI-FIND call it ORSA's "Best Ph.D. Dissertation on Transportation"; INFORMS records it as the "TSL Dissertation Prize" [S1, S46, S48].
6. **His career against OpenAlex affiliations.** OpenAlex gives Vattenfall, DTU, Polytechnique Montréal and Universidad de Sevilla. His homepage and UNI-FIND show only Bologna, Padova, L'Aquila, Udine and Padova again. The extra affiliations belong to co-authors [S1, S48, S50, S52].
7. **Inconsistent AI-use disclosure across 2026 manuscripts.** Four of the five 2026 manuscripts read carry an AI-use declaration (FP; the three EndoWake papers). A text search of the v1 PDF of the sole-author minibatch paper found none [S23, S31–S34]. The tool names also differ from paper to paper: "Claude Fable 5.1" and "GPT-5.6 sol"; "Claude Opus 5" and "Claude Fable 5"; "Anthropic Claude" and "OpenAI Codex".
8. **Counts of his publications.** 143 on the homepage, 176 on UNI-FIND, 185 OpenAlex records (including Zenodo items and duplicates) [S1, S48, S52]. These are counting differences, not errors of fact.

## Gaps

- PhD advisor not found: MGP has no record of him, and INFORMS gives only the thesis title. The 1987 thesis itself was not read.
- DBLP not consulted (Anubis bot check, not bypassed). ResearchGate pages unreadable (403), so the content of the Fermat "digital twin" note is unknown.
- No stated reason found for:
  - entering or leaving statistical disclosure control;
  - leaving polyhedral ATSP work after 2006, railways after 2017, bilevel after 2019;
  - the 2020–24 drop in output;
  - moving from CPLEX to SCIP and Gurobi in 2026;
  - opening a GitHub account in September 2026;
  - taking up AI assistants and pre-registration (the declarations say how, not why).
- No interview, oral history or obituary-style retrospective found. Only 2 WebSearch calls were spent; the slide decks were the main stated-voice source.
- No rejection is documented. The fates of the 2018 minibatch submission, the 2009 yoyo paper and the 2009 extended Benders draft are not stated.
- Not viewed or read: the 2026 MP4 videos (two EndoWake, backprop, SVM-telecom); the 2017 TOP comment *Comments on: On learning and branching: a survey* (TOP 25:237–238, DOI 10.1007/s11750-017-0449-0).
- Supervision checked on title pages for only 9 theses (3 PhD, 6 laurea/master); the rest is folder-listing evidence. Luzzi's PhD supervision is not confirmed.
- Not checked: his relation to Double-Click SRL; the funding history beyond the homepage project list, PRIN 2022 REWIND and "MiUR" in the 2026 FP declaration; the identity and affiliation of co-author Jason Jo; the computing environment of the 1980s–90s codes; his retirement or emeritus horizon.
- All 2026 manuscripts are under review or unrefereed; outcomes unknown.

## Sources

Primary: his own documents, code and data
- S1 · *Curriculum vitae* homepage, M. Fischetti, Last-Modified 2026-10-30, https://www.dei.unipd.it/~fisch/ · P
- S2 · Papers directory listing with file dates, https://www.dei.unipd.it/~fisch/papers/?C=M;O=D (read 2026-11-08) · P
- S3 · Slides directory listing with file dates, https://www.dei.unipd.it/~fisch/papers/slides/?C=M;O=D (read 2026-11-08) · P
- S4 · Dissertations directory listing, https://www.dei.unipd.it/~fisch/ricop/tesi/?C=M;O=D · P
- S5 · Teaching directory listing, https://www.dei.unipd.it/~fisch/ricop/?C=M;O=D · P
- S6 · *MIP models for MIP heuristics or the Bracket-and-Fix method*, M. Fischetti and A. Lodi, 11th Combinatorial Optimization Workshop, Aussois, 2007-01-12 (slides; file posted 2025-06-23), …/papers/slides/2007 Aussois [bracket-and-fix heuristic].pdf · P
- S7 · *A Lagrangian Heuristic for Robust Train Timetabling*, V. Cacchiani, A. Caprara, M. Fischetti, AIRO 2012 (file "in memoriam Alberto Caprara", 2012-09-07), …/papers/slides/2012 AIRO [in memoriam Alberto Caprara].pdf · P
- S8 · *BRANCHstorming (brainstorming about tree search)*, M. Fischetti, ISCO 2014 plenary, Lisbon, March 2014, …/papers/slides/2014 ISCO [plenary Fischetti BRANCHstorming].pdf · P
- S9 · *Proximity-driven MIP heuristics with an application to wind farm layout optimization*, M. Fischetti, IMI Workshop, October 2014, …/papers/slides/2014 IMI [Fischetti - proxy heuristics for wind farm layout].pdf · P
- S10 · *The simpler the better: Thinning out MIP's by Occam's razor*, M. Fischetti, Harold Larnder lecture, CORS/INFORMS 2015, Montreal, June 2015, …/papers/slides/2015 CORS [Fischetti - Occam Razor].pdf · P
- S11 · *Deep Learning and Mixed Integer Optimization*, M. Fischetti, Dagstuhl seminar on MINLO algorithms, February 2018 (short deck), …/papers/slides/2018 Dagstuhl [short Fischetti on DL].pdf · P
- S12 · *#post_modern Branch-and-Cut Implementation*, M. Fischetti, ISMP 2018 keynote, Bordeaux, 2018-07-06, …/papers/slides/2018 ISMP [keynote Fischetti on BandC].pdf · P
- S13 · *Mathematical Optimization for Social Distancing*, M. Fischetti, INFORMS annual meeting, November 2020, …/papers/slides/2020 INFORMS [Fischetti on optimal social distancing].pdf · P
- S14 · *Branch-and-Cut is our swiss army knife* (part 1, B&C implementation and bilinear), M. Fischetti, VeRoLog 2025, Trento, 2025-06-13, …/papers/slides/2025 Verolog - Fischetti part 1 [BC implementation - bilinear].pdf · P
- S15 · *A Benders Decomposition Approach to the Time Window Assignment Traveling Salesperson Problem with Stochastic Travel Times*, M. Fischetti (with Cavaliere, Roberti, Salvagnin), ODS 2025, Milan, 2025-09-04 (slides), …/papers/slides/2025 ODS [Fischetti on TWATSP].pdf · P
- S16 · ODS 2025 abstract, F. Cavaliere, M. Fischetti, R. Roberti, D. Salvagnin, file 2025-04-22, https://www.dei.unipd.it/~fisch/papers/2025_ODS2025_Fischetti.pdf · P
- S17 · *Branch-and-Cut is our swiss army knife* (AIROyoung part 1, B&C and Benders), M. Fischetti, Padua, 2026-02-09, …/papers/slides/2026 AIROyoung - Fischetti part 1 [BC + Benders].pdf · P
- S18 · AIROyoung part 2 (intersection cuts and bilevel), M. Fischetti, Padua, 2026-02-09, …/papers/slides/2026 AIROyoung - Fischetti part 2 [ICs and bilevel].pdf · P
- S19 · *Backpropagation for people suffering from derivative allergy*, M. Fischetti, slides, file 2026-10-03, …/papers/slides/2026_backprop_slides.pdf · P
- S20 · *Yoyo search: a bisection cutting-plane method*, M. Fischetti and D. Salvagnin, working paper, 2009-11-20 (file posted 2019-12-08), https://www.dei.unipd.it/~fisch/papers/2009_yoyo_search.pdf · P
- S21 · *Minimal Infeasible Subsystems and Benders' cuts*, M. Fischetti, D. Salvagnin, A. Zanette, extended draft, revised Sept 2009 (file 2010-06-20), https://www.dei.unipd.it/~fisch/papers/Benders_mis_extended_draft.pdf · P
- S22 · *Redesigning Benders Decomposition for Large Scale Facility Location*, M. Fischetti, I. Ljubić, M. Sinnl, preprint 2016-02-11, https://www.dei.unipd.it/~fisch/papers/Benders_for_UFL.pdf (published version: Management Science 63:2146–2162, 2017, DOI 10.1287/mnsc.2016.2461) · P
- S23 · *Feasibility Pump with Objective Cutoff: A Computational Study*, M. Fischetti, manuscript, September 2026, submitted to Mathematical Programming Computation, https://github.com/mfischetti-arch/fp-objective-cutoff/blob/main/paper/manuscript.pdf · P
- S24 · GitHub repository mfischetti-arch/fp-objective-cutoff (README, CITATION.cff, 13 commits from 2026-09-04 to 2026-09-17, tag mpc-submission-1), https://github.com/mfischetti-arch/fp-objective-cutoff · P
- S25 · *Feasibility Pump with Objective Cutoff: reproducibility package*, M. Fischetti, Zenodo, 2026-09-17, DOI 10.5281/zenodo.22810777 (concept DOI 10.5281/zenodo.22810776) · P
- S26 · *Raw SCIP logs of "Feasibility Pump with Objective Cutoff: A Computational Study"*, M. Fischetti, Zenodo, 2026-09-17, DOI 10.5281/zenodo.22810848 (concept 10.5281/zenodo.22810847) · P
- S27 · *EndoWake: Modeling Wind by Linear Programming for Wind Farm Layout Optimization*, Martina Fischetti and Matteo Fischetti, Zenodo preprint (v1 as submitted to EJOR, revised 2026-09-11), 2026-09-28, DOI 10.5281/zenodo.23001174 · P
- S28 · Replication package for *EndoWake: Modeling Wind by Linear Programming…*, Martina Fischetti and Matteo Fischetti, Zenodo, 2026-09-10, DOI 10.5281/zenodo.22017424 (concept 10.5281/zenodo.22017423) · P
- S29 · Replication package and technical note for *GPU-accelerated wind farm layout search…*, v2.1.0, Martina Fischetti and Matteo Fischetti, Zenodo, 2026-11-04, DOI 10.5281/zenodo.23955408 (concept 10.5281/zenodo.22017446) · P
- S30 · Replication package for *A Dantzig–Wolfe reformulation of the EndoWake model…*, Martina Fischetti and Matteo Fischetti, Zenodo, 2026-10-29, DOI 10.5281/zenodo.23636074 (concept 10.5281/zenodo.23636073) · P
- S31 · *Minibatch persistency, eight years later: what batch reuse costs in steps and joules, and what it saves in data*, M. Fischetti, 2026-09-12, arXiv:2609.13922v1 (PDF read) · P
- S32 · *EndoWake: Modeling Wind by Linear Programming for Wind Farm Layout Optimization*, Martina Fischetti and Matteo Fischetti, 2026-09-30, arXiv:2609.40157v1 (PDF read) · P
- S33 · *GPU-accelerated wind farm layout search with a distilled endogenous wake model (EndoWake)*, Martina Fischetti and Matteo Fischetti, v1 2026-10-06, v3 2026-11-04, arXiv:2610.07844v3 (PDF read) · P
- S34 · *A Dantzig-Wolfe reformulation of the EndoWake model for optimal wind farm layouts*, Martina Fischetti and Matteo Fischetti, 2026-10-29, arXiv:2610.39503v1 (PDF read) · P
- S35 · arXiv API: author listing (9 preprints, 2017-12-17 to 2026-10-29) with metadata and abstracts of arXiv:1712.06174 (Fischetti and Jo), 1806.07353 (Fischetti, Mandatelli, Salvagnin), 1906.01504 (Fischetti and Stringher), 1907.08246 (Fischetti and Salvagnin), 2112.02195 (Liu, Fischetti, Lodi), http://export.arxiv.org/api/query · P

Primary: theses by his students
- S36 · L. Bertacco, *Exact and Heuristic Methods for Mixed Integer Linear Programs*, PhD thesis, Università di Padova, 2005-12-30, https://www.dei.unipd.it/~fisch/ricop/tesi/2005_Bertacco_PhD_thesis.pdf · P
- S37 · D. Salvagnin, *Constraint Programming Techniques for Mixed Integer Linear Programs*, PhD thesis, Università di Padova (XXI ciclo), 2008/2009, …/tesi/2008_Salvagnin_PhD_thesis.pdf · P
- S38 · A. Zanette, *Three Topics in Mixed Integer Programming*, PhD thesis, Università di Padova, 2008-11-03, …/tesi/2008_Zanette_PhD_thesis.pdf · P
- S39 · M. Fischetti and I. Luzzi, *Exact and Heuristic Methods for Nesting Problems*, report, Padova, 2004-04-01, …/tesi/tesi_dottorato_Luzzi_2003.pdf · P
- S40 · I. Mandatelli, *Improved Training Methods for Neural Networks*, master's thesis, Padova, 2018, …/tesi/2018_Mandatelli_Thesis.pdf · P
- S41 · M. Stringher, *Unconventional Training of Deep Neural Networks*, master's thesis, Padova, AY 2018/19, …/tesi/2019_Stringher_Thesis.pdf · P
- S42 · C. Polo, *Algoritmi euristici per il progetto ottimo di una rete di interconnessione*, laurea thesis, Padova, AY 2000–2001, …/tesi/tesi_Polo_2002.pdf · P
- S43 · M. Scantamburlo, *DRT: a General Method for Mixed Integer Problems*, thesis, Padova, AY 2001/2002, …/tesi/tesi_Scantamburlo_2003.pdf · P
- S44 · G. Andreello, *Nuove procedure di separazione per la programmazione lineare intera*, laurea thesis, Padova, 2003-03-24, …/tesi/tesi_Andreello_2003.pdf · P
- S45 · Bettin (1998) and De Franceschi (2003) thesis files, opened; no supervisor line in the first pages, …/tesi/tesi_dottorato_Bettin_1998.pdf, …/tesi/tesi_De_Franceschi_2003.pdf · P

Primary: records kept by awarding bodies and institutions
- S46 · INFORMS award-recipient pages: Matteo Fischetti (1987 TSL Dissertation Prize; 2004 Wagner finalist), Matteo Fischetti 2 (2008 Edelman, with citation), Netherlands Railways, https://www.informs.org/Recognizing-Excellence/Award-Recipients/Matteo-Fischetti and …/Matteo-Fischetti2 and …/Netherlands-Railways2 · P
- S47 · CORS, list of Harold Larnder Prize recipients (French page), https://cors.ca/fr/content/prix-harold-larnder · P
- S48 · Università di Padova, UNI-FIND person page "FISCHETTI MATTEO" and prize records 22763 (Larnder 2015) and 22765 (ORSA 1987), https://unifind.unipd.it/resource/prize/22763 and https://unifind.unipd.it/resource/prize/22765 · P
- S49 · Polytechnique Montréal, PolyPublie: record 10460 (D. Liu, *Machine Learning Algorithms for Combinatorial Optimization*, PhD thesis 2022, director A. Lodi), record 52942 (AAAI 2022), and D. Liu's author page, https://publications.polymtl.ca/10460/ · P
- S50 · ORCID public record of Martina Fischetti, 0000-0002-7673-6917 (education and employment), https://pub.orcid.org/v3.0/0000-0002-7673-6917/record · P

Secondary
- S51 · ORCID public record of Matteo Fischetti, 0000-0001-6601-0568 (created 2016-04-15; 13 works imported from Crossref; no affiliations), https://orcid.org/0000-0001-6601-0568 · S
- S52 · OpenAlex author A5019439480 and its 185 works (affiliations, counts per year, authorship), https://api.openalex.org/authors/A5019439480 · S
- S53 · Google Scholar profile user=5rOdaqAAAAAJ, sorted by date (read via WebFetch on 2026-11-08), https://scholar.google.com/citations?user=5rOdaqAAAAAJ · S
- S54 · Crossref REST API, about 60 DOIs cited here resolved on 2026-11-08, https://api.crossref.org/works/ · S
- S55 · Mathematics Genealogy Project: quick searches (Matteo Fischetti, Salvagnin, Zanette, Monaci: 0 records; Andrea Lodi id 177176; Paolo Toth id 79649) and the server-status page, https://www.mathgenealogy.org/ · S
- S56 · arXiv records for outside context: V. Tjeng, K. Xiao, R. Tedrake, *Evaluating Robustness of Neural Networks with Mixed Integer Programming*, arXiv:1711.07356 (2017-11-20); D. Choi, A. Passos, C. J. Shallue, G. E. Dahl, *Faster Neural Network Training with Data Echoing*, arXiv:1907.05550 (2019-07-12) · S
- S57 · Crossref record of E. Danna, E. Rothberg, C. Le Pape, *Exploring relaxation induced neighborhoods to improve MIP solutions*, Mathematical Programming 102:71–90, DOI 10.1007/s10107-004-0518-7 · S
- S58 · WebSearch result snippets (2 queries: the 2015 Larnder Prize; Defeng Liu's thesis), used only as leads to S47, S48 and S49 · S

Not consulted (blocked): DBLP pid 47/4770 (Anubis bot check); ResearchGate publications 414856876 and 414775591 (HTTP 403); the ISCO 2014 speaker biography page at lamsade.dauphine.fr (HTTP 403).
