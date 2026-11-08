# Ruth Misener · 06 Research trajectory (timeline, lineage, turns, last 12 months)

| Field | Value |
|---|---|
| Researcher | Ruth Misener. Professor in Computational Optimisation, Department of Computing, Imperial College London; BASF/Royal Academy of Engineering Research Chair in Data-Driven Optimisation (2022–27); Amazon Scholar (2025–) |
| Dimension | Research agent 06 of 06: research trajectory (nuwa research-craft Phase 1, framework §二, Agent 6) |
| Research date | 2026-10-10 |
| Sources consulted | 61: 46 used (27 primary relative to Misener, 11 secondary, 8 field reference papers by others; all listed under Sources) and 15 attempted but unusable (listed under Gaps) |
| WebSearch calls used | 3 of 4. One returned only namesakes, one found no 2025–2026 honour, one found no Mathematics Genealogy entry for her |
| User-supplied material | None. `references/sources/{papers,essays,software,publications}` hold only `.gitkeep`. `references/sources/talks/` holds YouTube auto-caption (ASR) transcripts that sibling agents saved earlier in this workflow run; they are not user-supplied. I quote seven of them, marked [ASR captions]. `private/` was not opened |
| Language | English (team.json) |

## How to read this note

- **Tags.** [stated] = what Misener said or wrote. [practice] = what the record shows she did (CV entries, papers, author lists, repositories, grant dates). [observed] = what others said or recorded about her. [inferred] = my reading; no source says it. (P) = primary relative to Misener, (S) = secondary.
- **Quotes are verbatim.** ASR quotes match the caption track word for word, fillers included; misrecognitions are flagged [sic, ASR: ...]. Curly quotes and apostrophes are normalised to straight ones; in PDF text, ligatures and dropped diacritics are restored (e.g. "Mišić") and words or citation ranges split at a line break are rejoined (e.g. "[117-" + "119]"). Nothing paraphrased is inside quotation marks. Before this note was finalised, a script re-matched 66 sentence-length quotes and 48 short quoted labels and titles against the saved source texts; the only mismatches were the restorations just listed and one HTML link artifact.
- **Identifiers.** Every paper named carries a DOI, an arXiv id, or venue + year + full title, checked in this run against Crossref, the arXiv API, DBLP (SPARQL endpoint), Optimization Online, her CV, or the PDF itself. "Online YYYY-MM-DD" is Crossref's online or issued date.
- **Division of labour.** 01-publications.md dissects the signature works, 03-process-evidence.md covers how she works, 04-mentorship.md covers supervision. This note is about time: when things happened, what turned her, and when she entered and left topics relative to the field. Where I lean on a sibling note's finding that I did not re-check, I say so.
- **The CV.** "Ruth Misener; Curriculum vitae; Updated December 3, 2025" (32 pp.), downloaded from her homepage and read with `pdftotext -table`. Plain extraction misaligns the award years of its two-column layout; table mode aligns them (e.g. "CAST Outstanding Young Researcher Award ... 2020", which matches the 2021 Sevilla host's "the 2020 cast outstanding yan [sic, ASR: young] researcher award"). CV item codes (J journal, C CS conference, E engineering conference, K keynote, S seminar, I invited talk, Sc school) are hers.

---

## 0. The trajectory in brief [inferred, from §1–§5]

- **Phase A, 2007–2012 (Princeton chemical engineering, with Floudas).** Problems and deliverables came from the advisor: pooling problems with piecewise-linear MILP relaxations (one of his "more recent intuitions", essay p.13), then a public global solver (his 2008 demand). Output: APOGEE (2010), GloMIQO (2012), the MIQCQP relaxation paper (2012), ANTIGONE (2013).
- **Phase B, 2012–2017 (Imperial: chemical-engineering fellow, then Computing lecturer).** A move to the UK that the record attributes to a couple's decision; a fellowship titled on chemotherapy; biomedical collaborations; then, from 2014, a lectureship in Computing that she says the structure-detection solver work earned her. Her first students brought heat recovery, symmetry and structure detection.
- **Phase C, 2017–2022 (EPSRC "GALINI" fellowship, first BASF money).** The widest spread: uncertainty, scheduling, explainability, approximation algorithms, learning inside solvers, Python/Pyomo tools, and the start of optimisation over trained models (BASF seed project, summer 2017).
- **Phase D, 2022–2026 (BASF/RAEng chair, hubs, Amazon).** Consolidation into data-driven optimisation for chemistry: OMLT, Bayesian optimisation over trees and graphs, GNN and molecule formulations, a benchmark dataset. Her own PhD cohort shrinks to one student while hub, doctoral-centre and industry roles grow.
- **The constant she names herself:** relaxation and formulation strength. "So all I've been doing here at Imperial uh is basically figuring out how to relax better." [stated, ASR captions, inaugural lecture 2023, 05:37]
- **The variable she names herself:** domains and collaborators. "So in some ways very opportunistic." [stated, ASR captions, 46:34; full passage in §3, T6]

---

## 1. Dated timeline

### 1.1 Education, positions, honours, roles

| When | What | Tag | Source |
|---|---|---|---|
| 2003-09 – 2007-06 | S.B. Chemical Engineering, MIT. Robert C. Byrd Honors Scholarship (2003–07); Tau Beta Pi (2007) | [practice] (P) | ORCID educations (self-asserted, 2003-09 to 2007-06); Imperial profile ("1 Sep 2003 - 8 Jun 2007"); CV pp.1–2 |
| 2007-09 – 2012 | PhD Chemical Engineering, Princeton, "Advised by Professor C. A. Floudas". Thesis "Novel Global Optimization Methods: Theoretical & Computational Studies on Pooling Problems with Environmental Constraints" (**not read**). NSF Graduate Research Fellowship (2007–12, $120k); Princeton Gordon Y. S. Wu Fellowship | [practice] (P) | CV pp.1, 26; ORCID (end "2012-10"); Imperial profile (end "17 Nov 2012"); see Contradictions C1, C2 |
| 2008 | Early-stage PhD assessment: Floudas requires "a promise to write and publicly release a global MINLP solver" | [stated] (P) | Floudas essay, p.14 |
| 2009-05-07 | First paper online: C. E. Gounaris, R. Misener, C. A. Floudas, "Computational Comparison of Piecewise−Linear Relaxations for Pooling Problems", *Ind. Eng. Chem. Res.* 48(12):5742–5766. DOI 10.1021/ie8016048 | [practice] (P) | Crossref |
| c. 2009 | Pistikopoulos meets her on a visit to Princeton; Floudas "introduced me to his next big thing" | [observed] (P, ASR) | inaugural lecture, vote of thanks [47:36] |
| 2010 | APOGEE released, "Freely available tool" (CV S01). Excellence in Teaching, Princeton School of Engineering & Applied Sciences | [practice] (P) | CV pp.2, 10 |
| 2011-03-12 | Floudas replies "This is great!!!" to her "good news" on facets of bilinear functions | [stated] (P) | essay p.13 |
| 2011-07 | Invited seminar at Imperial's Centre for Process Systems Engineering (CPSE), "Invited by Prof E Pistikopoulos" (CV S01). Her first recorded Imperial contact | [practice] (P) | CV p.15 |
| late 2011 | Floudas phones Pistikopoulos: "the couple has been deciding to move to to the UK and they are thinking about post-doctoral studies here" | [observed] (P, ASR) | vote of thanks [48:06–48:37] |
| 2012-03-07 | GloMIQO paper online (*J. Global Optim.* 57(1):3–50, 2013; DOI 10.1007/s10898-012-9874-7). GloMIQO software (2012): "Commercial through Princeton & GAMS Development Corp." | [practice] (P) | Crossref; CV S02 |
| 2012-05-24 | MIQCQP relaxation paper online, *Math. Program.* 136(1):155–182. DOI 10.1007/s10107-012-0555-6 | [practice] (P) | Crossref |
| 2012-10 – 2017-10 | Royal Academy of Engineering (RAEng) Research Fellowship, £539k. Project title: "Towards rational chemotherapy strategies: a hybrid computational / experimental approach". She declined an Imperial Junior Research Fellowship (2012–15, £114k), "declined in favour of the RAEng Fellowship" | [practice] (P) | ORCID funding record (self-asserted, created Dec 2014); CV pp.1, 26 |
| 2012–2014 | RAEng Research Fellow, CPSE (Chemical Engineering), Imperial | [practice] (P) | CV p.1 |
| 2013 | ANTIGONE software, "Commercial through Princeton & GAMS Development Corp." (CV S03). Four invited talks on ANTIGONE (07–12/2013), including "Architecting ANTIGONE: Design Choices and Tradeoffs" (ZIB MODAL workshop, 11/2013; slides **not found**). First keynote: "Making and Healing Blood: An Engineer's Approach" (RAEng Research Forum, 09/2013). Best Paper, *J. Global Optim.* | [practice] (P) | CV pp.2, 10–12, 18 |
| 2014-03 | Job talk, Department of Computing: "Mixed-Integer Nonlinear Optimization: Foundations and Applications" | [practice] (P) | CV S03 |
| 2014-03-20 | ANTIGONE paper online, *J. Global Optim.* 59(2–3):503–526. DOI 10.1007/s10898-014-0166-2 | [practice] (P) | Crossref |
| 2014 | Lecturer, Department of Computing (2014–17). W. David Smith, Jr. award. First PhD student (Kouyialis, 2014–18) and first MEng student (Mistry, 2014–15). Joins INFORMS; member of CPSE (2014–) | [practice] (P) | CV pp.1–2, 24–26; homepage, Professional Activities |
| 2015 | Co-investigator on EPSRC U2 (2015–19, £765k) and on the EU H2020 networks ModLife and SyMBioSys (2015–19). First Bayesian-optimisation item: an MSc project co-supervised with M. P. Deisenroth (arXiv:1511.05385, 17 Nov 2015) | [practice] (P) | CV p.28; arXiv API |
| 2016-08-14 | Floudas dies. Essay: "Born August 31, 1959"; "In 2015, Chris moved to Texas A&M University" | [stated] (P) | essay p.12 |
| 2016-10 | Essay "Christodoulos Achilleus Floudas", *SIAG/OPT Views and News* 24(1):12–16 | [stated] (P) | PDF |
| 2016–2018 | Elected Director, AIChE Computing & Systems Technology (CAST) Division; then programming coordinator (2018–21) | [practice] (P) | CV p.29 |
| 2017 | Senior Lecturer (2017–20). EPSRC Early Career Fellowship "GALINI" (Sept 2017 – Aug 2022; £984k; "Includes 6 years postdoc funding"). BASF seed funding (May–Aug 2017, £40k). EPSRC First Grant (Mar 2017 – Mar 2018, £101k). ROAD2H (May 2017 – Apr 2020). Schlumberger CASE studentship (Oct 2017 – Mar 2021). IBM PhD Fellowship to Baltean-Lugojan (Sept 2017 – May 2018). Sir George Macfarlane Medal and RAEng Engineers Trust Young Engineer of the Year (group-site post, 30 June 2017); AIChE 35 Under 35. Joins the British Computer Society. Associate Editor, *Optimization and Engineering* (2017–) | [practice] (P) | CV; homepage, Grants; group-site post |
| 2017-08 → 2018-04 | The `cog-imperial` GitHub organisation starts: first repositories Aug 2017, GPdoemd Nov 2017, `suspect` 28 Mar 2018, `galini` 2 Apr 2018 | [practice] (P) | GitHub API |
| 2018-02 | Co-organises Dagstuhl Seminar 18081 on MINLP algorithms (with Bonami, Gleixner, Linderoth) | [practice] (P) | CV p.30 |
| 2018-03-02 | First preprint on optimising over a trained model (gradient-boosted trees; arXiv:1803.00952v1) | [practice] (P) | arXiv API |
| 2018 | First CS-conference paper (ICML 2018; CV C01). Editorial boards: *J. Global Optim.* (2018–20), *Math. Program. B* (2018–21), *Comput. Chem. Eng.* (2018–). GAMS Advisory Board (2018–25). Mellichamp Distinguished Lecture, Georgia Tech | [practice] (P) | CV |
| 2018-11-26 | Learning-based SDP cut-selection preprint (Optimization Online) | [practice] (P) | Optimization Online |
| 2019 | Opening plenary, Oberwolfach MINLP workshop: "Developing spatial branch & bound solvers" (06/2019). BASF PhD studentship (Apr 2019 – Mar 2022, £270k). Co-I of the StatML doctoral training centre (2019–27). Kronqvist joins as a Royal Society Newton Fellow (2019–21). *I&EC Research* Class of Influential Researchers. Chartered Engineer. Associate Editor, *INFORMS J. Computing* (2019–) | [practice] (P) | CV; homepage |
| 2020 | Professor (2020–). Eli Lilly Prosperity Partnership (homepage: Feb 2020 – Jan 2025; CV: "2019 - 2027"). Tsay's fellowships (2020–24). CAST Outstanding Young Researcher Award; AAMAS Best (Innovative) Demo. Fellow of the BCS. Vice Chair, INFORMS Optimization Society (2020–21) | [practice] (P) | CV; homepage |
| 2021 | CPAIOR Distinguished Paper; Rosenbrock Prize. Semi-plenary EURO 2021 "Computational Mixed-Integer Nonlinear Optimization"; plenary NMPC 2021. Virtual Imperial MINLP workshop (with Anjos, Belotti, Kronqvist; talks uploaded to the group's YouTube channel June–July 2021). Joins the Mathematical Optimization Society. ADOPT grant (homepage: Oct 2021 – Sept 2025) | [practice] (P) | CV; homepage; YouTube feed |
| 2022 | COIN-OR Cup (OMLT). BASF/RAEng Research Chair (Mar 2022 – Feb 2027; announced 24 Mar 2022). IConIC Prosperity Partnership with BASF announced 18 Jul 2022 (project July 2023 – June 2028). GAMS 40.1.0 (1 Aug 2022) drops GloMIQO. First "Autonomous research machines" talk (ICML workshop, 07/2022). HUGO plenary "Between formulations or: How I Learned to Stop Worrying and Love Parameters" (09/2022). NeurIPS Top Reviewer (2022, 2023) | [practice] (P); GAMS note [observed] (S) | CV; Imperial News; GAMS release notes |
| 2023 | Saville Lecture, Princeton (02/2023). Inaugural lecture "Just Relax" (13 Mar 2023). Joint FOCAPO/CPC keynote with L. Biegler (01/2023). SIAM OP23 organising committee. *Comput. Chem. Eng.* Best Paper (Folch et al.). BCS Roger Needham Award (announced 20 Dec 2023; presented 10 Jan 2024). Wellcome cholera-surveillance project (Sept 2023 – Aug 2026). BASF studentship #2 (Oct 2023 – Sept 2027). Talk "Professor Floudas' continuing legacy: Automatically designing microreactor experiments" (ESCAPE 33, 06/2023, CV I44) | [practice] (P) | CV; Imperial News; homepage |
| 2024 | Mellichamp Lectureship, Purdue (10/2024). NeurIPS 2024 Area Chair. EPSRC AI hub AIchemy (2024–29; CV: "one of six co-directors"; the hub site lists her in its "Leadership Team"). EPSRC doctoral centre CCMI (2024–33; "one of 8 co-directors and one of 2 Directors of Research"). Natural History Museum project "Space optimization for NHM Unlocked" (6 months postdoctoral funding). Associate Editor, *Operations Research* (2024–25). Member, UKRI Turing AI World-Leading Researcher Fellowships panel | [practice] (P); hub site [observed] (S) | CV; AIchemy site |
| 2025 | Amazon Scholar (2025–). Plenary or semi-plenary talks at EUROPT (06/2025), ICCOPT (07/2025) and OR 2025 (09/2025), all titled "Bayesian optimization for mixed feature spaces using tree kernels and graph kernels". Papers at AISTATS, GECCO, ICML and NeurIPS (Datasets & Benchmarks). The CV closes the GAMS Advisory Board (2018–25) and the *Operations Research* AE post (2024–25). CV updated 3 Dec 2025 | [practice] (P) | CV; homepage; Imperial profile; DBLP |
| 2026 | ICLR 2026 paper (BoGrape). P-split appears in *Math. Program.* vol. 218. SIAM OP26 first plenary (IP1, 2 June 2026, Edinburgh; scheduled). Preprints in May and October 2026 | [practice] (P) | DBLP; Crossref; SIAM program; arXiv API |

### 1.2 What she chose to talk about, by date (CV keynote, seminar and invited-talk lists) [practice] (P)

Talk titles are the cleanest dated record of what she wanted to be known for. The table counts talks she gave herself: keynotes (K), seminars (S), and invited conference talks (I) where the CV marks her as presenter ("Misener R.*") or lists her alone.

| First → last dated use | Theme (title as in the CV) | CV items |
|---|---|---|
| 07/2011 | Her thesis ("Novel Global Optimization Methods ... Pooling Problems with Environmental Constraints"), at CPSE | S01 |
| 07/2013 → 12/2013 | ANTIGONE, four talks | I01–I04 |
| 09/2013 → 02/2015 | "Making and Healing Blood: An Engineer's Approach"; "Stem Cell Bioprocessing under Uncertainty ..." | K01, S02, S06 |
| 03/2014 → 01/2016 | MINLP foundations, formulations and implementation: "Relating MINLP Model Formulations to Algorithmic Solution Strategies"; "Deterministic Global Optimisation for Process Optimisation"; "Implementing algorithmic advances in mixed-integer nonlinear optimisation" | S03, S04, I05, S05, S08 |
| 07/2015 → 03/2019 | Heat exchangers and energy efficiency: "Solving MINLP with Heat Exchangers: Special Structure Detection and Large-Scale Global Optimisation"; "Mixed-Integer Nonlinear Optimisation: Energy Efficiency Applications"; heat recovery network heuristics | I06, S07, S09, S10, K02, I16, K12 |
| 10/2015 → 08/2016 | Structure detection: "Detecting Pooling Network Structure"; "Using Functional Programming to recognize Named Structure in an Optimization Problem" | I07, I09, I10 |
| 05/2016 → 10/2018 | Pooling, parametric structure and complexity (incl. the 2017 Floudas memorial talks): "A Parametric Approach to the Pooling Problem"; "Globally Optimising Pooling Problems"; "Piecewise Parametric Structure in the Pooling Problem ..."; "The pooling problem with a view towards gas transport" | I08, I13, I14, I15, K10 |
| 01/2017 | "Integrating Mixed-Integer Optimization and Satisfiability Modulo Theories: Application to Planning and Scheduling" | I12 |
| 12/2017 → 10/2022 | Lexicographic optimisation for rescheduling; Royal Mail; explainable scheduling | S11, S12, S16, S22, S38 |
| 01/2018 → 03/2018 | "Optimisation for Gradient Boosted Trees with Risk Control" | K03, S14, S15 |
| 03/2018 → 12/2019 | Learning-based SDP cut selection ("Online generation via offline selection ..."; "Learning-based Cutting Plane Approximation ..."; "Scoring positive semidefinite cutting planes ...") | K05, K06, S17, I22, S20, S23, S26 |
| 06/2018 → 03/2021 | "Approximation Algorithms for Process Systems Engineering" | K07, S21, S27 |
| 09/2018 → 12/2018 | "Gaussian Processes for Hybridizing Analytical & Data-Driven Decision-Making" | S18, K11, S19 |
| 06/2019 → 07/2021 | "Developing spatial branch & bound solvers"; "Numerical approaches to mixed-integer nonlinear optimization"; "Computational Mixed-Integer Nonlinear Optimization" | K13, K16, K17 |
| 10/2019 → 09/2021 | "Artificial intelligence approaches towards hybridizing analytical & data-driven decision-making" | S24, S25, S31, S32 |
| 09/2020 → 11/2020 | "Mixing analytical and data-driven optimization"; ENTMOOT | K14, K15 |
| 04/2021 → 06/2021 | Partition-based formulations for trained ReLU networks; partial Lasserre relaxation | S28–S30 |
| 03/2022 → 01/2024 | "OMLT: Optimization and Machine Learning Toolkit", incl. P&G, Aspen Technology, ExxonMobil and Bosch audiences | S34–S36, K18, K19, I38, I39, S45, I48, I49 |
| 03/2022 → 04/2023 | "Between formulations or: How I Learned to Stop Worrying and Love Parameters" | S33, K20, S41, S42, I43 |
| 07/2022 → 03/2025 | "Autonomous research machines: Self-optimizing new chemistry" (ten uses) | I40, S40, K22, I42, S44, S47, S48, I53, S50, I54 |
| 10/2021 → 03/2024 | Bayesian optimisation for experiments: "Design of flow chemistry experiments using batch Bayesian optimization"; "Bayesian optimization & design of experiments" | I37, S37, S39, S46 |
| 07/2023 | "Optimization for ML and ML for optimization" (overview, Institut Mittag-Leffler) | I46 |
| 10/2023 → 10/2024 | Optimising over and verifying graph neural networks | I47, I51, S49 |
| 04/2024 → 09/2024 | "Optimal decision-making with trained neural networks embedded" / "... trained surrogate models embedded" | I50, K23, I52 |
| 02/2025 → 09/2025 | "Bayesian optimization for mixed feature spaces using tree kernels and graph kernels" | K24–K27, S51 |
| 06/2026 | "Optimizing over graphs: Challenges, Formulations, and Applications" (SIAM OP26, IP1) | K28; SIAM program |

**Reading** [inferred]: three overlapping waves. MINLP solvers and formulations run 2011–2021; hybrid analytical/data-driven decision-making runs 2018–2024; chemistry-facing Bayesian optimisation, autonomy and graph spaces run 2022–2026. Her last CV talks on MINLP solvers date from 2021: the NMPC plenary and EURO semi-plenary (both 07/2021; the NMPC talk is the YouTube video "Developing spatial branch & bound solvers") and a GALINI pooling talk at INFORMS (10/2021, I34).

### 1.3 Venue and identity markers by year [practice]

- **arXiv primary categories** of the 46 records the arXiv API returns for "Ruth Misener" (P). Her PhD-era work is not on arXiv; the first record is November 2015.

  | Year | math.OC | ML (cs.LG, stat.ML, stat.AP, cs.AI) | other |
  |---|---|---|---|
  | 2015 | 0 | 1 | 0 |
  | 2017 | 3 | 0 | 0 |
  | 2018 | 3 | 2 | 1 (cs.MS) |
  | 2019 | 2 | 0 | 1 (cs.DS) |
  | 2020 | 1 | 1 | 1 (q-bio.QM) |
  | 2021 | 4 | 2 | 0 |
  | 2022 | 1 | 5 | 0 |
  | 2023 | 1 | 2 | 1 (cs.CE) |
  | 2024 | 1 | 4 | 2 (cs.CE, q-bio.QM) |
  | 2025 | 2 | 3 | 0 |
  | 2026 (to 10 Oct) | 1 | 1 | 0 |

- **DBLP non-preprint records** (S; DBLP misses her early chemical-engineering journals, e.g. the 2009 *Ind. Eng. Chem. Res.* paper): journals only from 2010 to 2016; first conference record 2017 (the SEA keynote abstract); then journal/conference counts of 4/1 (2018), 4/2 (2019), 2/2 (2020), 5/2 (2021), 3/2 (2022), 3/1 (2023), 2/2 (2024), 2/4 (2025), 1/1 (2026 so far).
- **Memberships** (homepage, P): Senior Member AIChE "2008 –"; INFORMS "2014 –"; BCS "2017 –"; Chartered Engineer "2019 –"; "Since 2020, I am also a Fellow of the British Computer Society (FBCS)"; Mathematical Optimization Society "2021 –". She joined MOS nine years after her first *Math. Program.* paper.
- **Service drift** (CV, P): AIChE CAST Director (2016–18) and programming coordinator (2018–21) → INFORMS Optimization Society Vice Chair (2020–21), *INFORMS J. Computing* AE (2019–), *Operations Research* AE (2024–25) → NeurIPS Top Reviewer (2022, 2023) and Area Chair (2024).
- **Reading** [inferred]: the 2014 move to Computing changed her venues slowly. ML-category preprints outnumber math.OC ones from 2022, eight years after the move. In February 2023 she still introduced herself to an ML seminar with "I am a chemical engineer and I come from that Community" [stated, ASR captions, Cornell 2023].

---

## 2. Lineage

### 2.1 Ancestors

| Generation | Person | Degree (Mathematics Genealogy Project, S) | Note |
|---|---|---|---|
| great-grand-advisor | Roger W. H. Sargent (MGP 96603, linked from Grossmann's MGP page) | — | Imperial's process systems engineering centre bears his name: her homepage lists the "Sargent Centre for Process Systems Engineering" among her affiliations |
| grand-advisor | Ignacio E. Grossmann (MGP 36078) | Ph.D., University of London, 1977, advisor Sargent | team member of this MINLP team |
| advisor | Christodoulos A. Floudas (MGP 81417) | Ph.D., Carnegie Mellon University, 1986, "Synthesis and Analysis of Flexible Energy Recovery Systems", advisor Grossmann | her essay: "Chris's Ph.D. thesis, supervised by Professor Ignacio Grossmann at CMU, investigated the automatic synthesis of heat exchanger networks [67]." (p.12) |
| — | Ruth Misener | PhD Princeton 2012 (CV) | **no MGP entry found** (see Gaps G2) |

- **MGP is incomplete for this branch** [observed] (S): Floudas's MGP page lists nine students (Adjiman 1998, Georgiou 1990, Gounaris 2008, Kallrath 2004, Khoury 2015, Klepeis 2002, Maranas 1995, Paules 1990, Visweswaran 1995), not Misener. Her essay says he "supervised 34 Ph.D. students and 20 postdoctoral research associates" (p.12).
- **Within this team** [practice] (S): Grossmann's MGP page lists Floudas (CMU 1986) and Sahinidis (CMU 1990) among his students. Grossmann is her academic grandfather and Sahinidis her academic uncle.
- **Memorial publishing** [practice] (P): the CV marks three of her group's papers as invited for Floudas memorial issues (J30 and J32, 2018; J42, 2020) and three for Sargent tributes: J26, 2016 ("Invited article for Tribute to Founders: Roger Sargent"); J40, 2019; J41, 2020.
- **A lineage echo** [inferred]: her first own student's paper (Mistry and Misener 2016, heat exchanger network synthesis; §3 T5) returns to the topic of her advisor's own thesis. Her SEA 2017 plenary on heat recovery networks lists Floudas as a co-author a year after his death (DBLP).

### 2.2 Postdoctoral host and the Floudas network

- **Pistikopoulos.** "the two met as undergraduates and forged a tight connection while both were Ph.D. students at CMU" [stated, essay p.14]. That friendship was the channel for her move: Floudas phoned him in late 2011 [observed, ASR]. After 2016 she says he "has been basically had to do double duty also as my uh PhD supervisor" [stated, ASR captions, 03:34–04:05].
- **Floudas's other students in her career** [practice] (P, CV + MGP):
  - Gounaris (Floudas PhD 2008) co-authored her first papers (2009, 2010) and invited her to CMU's Enterprise-wide Optimization seminar (03/2021, S27).
  - Adjiman (Floudas PhD 1998, Imperial Chemical Engineering) invited her to teach CPSE global-optimisation courses (2015–2017; Sc1, Sc3, Sc4, Sc6) and is PI of the Eli Lilly partnership she joined.
  - Boukouvala co-authored the 2016 review with her and Floudas and co-invited her to the Floudas Memorial Symposium (05/2017, I13).
- **Reading** [inferred]: the Floudas network placed her (2012), hosted her teaching (2015–17) and brought her into partnerships (2019/2020–), long after her own research had moved away from his topics.

### 2.3 Descendants

Her completed PhD students, from Imperial's Spiral repository (11 theses with `dc.contributor.advisor = Misener, Ruth`; P) and her CV (years, destinations as of Dec 2025; P):

| PhD (CV years) | Thesis title (Spiral date) | Co-advisor (Spiral) | Destination (CV) |
|---|---|---|---|
| G. Kouyialis (2014–18) | "Symmetry and degeneracy in nonconvex optimisation problems: Application to heat recovery networks" (2018-08) | Parpas | Data Science Consultant, Dataiku |
| R. Baltean-Lugojan (2015–19) | "Exploiting structure in nonconvex quadratic optimisation" (2019-10) | Parpas | Portfolio Manager, Eisler Capital |
| M. Mistry (2015–20) | "Branching strategies for mixed-integer programs containing logical constraints and decomposable structure" (2020-02) | — | minimax labs |
| S. Olofsson (2016–20) | "Gaussian processes for hybridisation of analytical and data-driven approaches for design of experiments" (2020-06) | — | Software Engineer, Meta |
| F. Ceccon (2016–21) | "GALINI: an extensible solver for mixed-integer quadratically-constrained problems" (2021-01) | — | Co-Founder, Apibara (PhD list) or Auclantis (postdoc list); see C5 |
| J. Wiebe (2017–21) | "Formulations, algorithms and software for robust optimisation" (2021-08) | — | Flexciton |
| A. Thebelt (2019–23) | "Sequential black-box optimization via global optimization of tree ensembles" (2023-08) | — | Machine Learning Engineer, QuantCo |
| R. Sedgwick (2019–23) | "Bayesian design of experiments for biomolecular assay design" (2023-10-27) | Stevens; van der Wilk | Research Scientist, Xyme |
| J. P. Folch (2020–24) | "Towards improving Bayesian optimisation for the physical sciences via long-term planning" (2024-10-03) | van der Wilk | Chief Scientific Officer and Co-Founder, SOLVE |
| J. Odgers (2020–25) | "Spectroscopy motivated probabilistic latent variable models" (2025-01-17) | Filippi | Postdoc, Helmholtz Munich |
| S. Zhang (2021–) | "Optimizing over trained graph neural networks: mixed-integer programming, symmetry-breaking, and applications" (2025-05-14) | — | Data Scientist, ByteDance |

- **Current team** (homepage, fetched 2026-10-10; P): postdocs J. S. Campos (2022–, EPSRC ADOPT), M. Sandrin (2025–) and K. Morozovska (2025–), both on the BASF Prosperity Partnership; one PhD student, T. Boyne (2023–, StatML CDT and BASF).
- **Academic descendants come from fellows and postdocs, not PhD students** [practice] (P, CV): Kronqvist (Newton Fellow 2019–21) "Now Associate Professor, KTH Royal Institute of Technology"; Tsay (fellow 2020–22) "Now Associate Professor, Imperial"; Letsios (postdoc 2016–19), now Lecturer, King's College London; Qing (postdoc 2023–25), now Lecturer, Lancaster University. None of the 11 PhD alumni holds a faculty post in the December 2025 CV.
- **Alumni firms come back as partners** [practice] (P): postdoc Sandrin is "Funded by the EPSRC Prosperity Partnership IConIC with SOLVE" (CV), and SOLVE is the company Folch co-founded.
- **Cohort size** [practice, counted from CV years]: own PhD students active in a year rose from 1 (2014) to 6 (2017) and peaked at 7–8 (2019–2021). It fell to 4 (2024) and to 1 by December 2025. No source gives a reason (Gaps G3).
- **Reading** [inferred]:
  - The thesis titles trace the turn from nonconvex structure (2018–2021) to probabilistic modelling and Bayesian optimisation (2020–2025) and then to GNN optimisation (2025).
  - Co-supervision with ML, statistics and materials colleagues (van der Wilk, Filippi, Stevens) becomes the norm for theses finishing after 2023.

---

## 3. Direction changes and what triggered them

Each turn gives: what changed, the trigger (tagged), entry or exit timing, and the resource context.

### T1. Into global optimisation through the advisor's programme (2007–2011)

- **What** [practice]: pooling problems and piecewise-linear MILP relaxations. Papers:
  - Gounaris, Misener, Floudas, *Ind. Eng. Chem. Res.* 2009 (DOI 10.1021/ie8016048);
  - Misener, Floudas, "Piecewise-Linear Approximations of Multidimensional Functions", *J. Optim. Theory Appl.* 145(1):120–147 (online 2009-11-05; DOI 10.1007/s10957-009-9626-0);
  - Misener, Thompson, Floudas, "APOGEE: Global optimization of standard, generalized, and extended pooling problems via linear and logarithmic partitioning schemes", *Comput. Chem. Eng.* 35(5):876–892, 2011 (DOI 10.1016/j.compchemeng.2011.01.026).
- **Trigger: the advisor's intuition** [stated] (P, essay p.13): "Chris had made major contributions to this problem since 1990 [74], but one of his more recent intuitions was that piecewise linear underestimators seemed to be effective in solving the pooling problem [117-119]."
- **Trigger: the advisor's bar for relevance** [stated] (P, essay p.13): "I remember raising some objections when Chris said that now we had to globally optimize a model with 15,439 continuous variables, 30 binary variables, 15,406 equality constraints, 230 inequality constraints, and 335 nonconvex terms [116]. But Chris absolutely insisted that his piecewise linear underestimation technique for bilinear terms [117-119] was not relevant unless it was effectively applied to real-world instances."
- **Timing** [practice/inferred]:
  - She started right after Meyer and Floudas's "Global optimization of a combinatorially complex generalized pooling problem" (*AIChE J.* 52:1027–1037; online 2005-10-28; DOI 10.1002/aic.10717). She entered inside her advisor's programme, not in response to a field-wide consensus.
  - The field-level analysis of MILP techniques for pooling came later: Dey and Gupte, "Analysis of MILP Techniques for the Pooling Problem", *Oper. Res.* 63:412–427, 2015 (DOI 10.1287/opre.2015.1357). In 2016 she cites it as having "further unpacked this relationship between the NLP pooling problem and MIP approximations [126]" (essay p.13).
- **She kept the question for eight years** [stated + practice]: "still Chris would push me: Why did these piecewise approximations work so well? How could we eliminate the computational dependence on parameters? Actually, thanks to work with Radu Baltean-Lugojan [127], I finally have a first answer to these questions Chris asked me eight years ago; I had been so looking forward to upcoming conferences to tell him all about it." (essay p.13). The answer: Optimization Online 2016/05/5457 (posted 2016-05-22), published as "Piecewise parametric structure in the pooling problem: from sparse strongly-polynomial solutions to NP-hardness", *J. Global Optim.* 71(4):655–690 (online 2017-10-25; DOI 10.1007/s10898-017-0577-y).
- **Context**: PhD student on an NSF fellowship in a group of, by her count, 34 PhD students over Floudas's career.

### T2. From relaxations to solvers: a deliverable the advisor imposed (2008 → 2012/2013)

- **Trigger** [stated] (P, essay p.14): "In 2008, when Chris told me that my early-stage Ph.D. assessment needed a promise to write and publicly release a global MINLP solver, I told him he was being unreasonable. He said to do it anyway; and I must have made a face, because I remember him telling me sharply: "you will not roll your eyes at your advisor!" He was right in the end, and we released first GloMIQO [131] and then ANTIGONE [132] as global optimization solvers in the modeling language GAMS."
- **Outputs** [practice]:
  - "Global optimization of mixed-integer quadratically-constrained quadratic programs (MIQCQP) through piecewise-linear and edge-concave relaxations", *Math. Program.* 136(1):155–182 (online 2012-05-24; DOI 10.1007/s10107-012-0555-6);
  - "GloMIQO: Global mixed-integer quadratic optimizer", *J. Global Optim.* 57(1):3–50 (online 2012-03-07; DOI 10.1007/s10898-012-9874-7);
  - "ANTIGONE: Algorithms for coNTinuous / Integer Global Optimization of Nonlinear Equations", *J. Global Optim.* 59(2–3):503–526 (online 2014-03-20; DOI 10.1007/s10898-014-0166-2);
  - with Smadbeck, "Dynamically generated cutting planes for mixed-integer quadratically constrained quadratic programs and their incorporation into GloMIQO 2", *Optim. Methods Softw.* 30(1):215–249 (online 2014-05-21; DOI 10.1080/10556788.2014.916287).
- **Timing relative to the field** [practice/inferred]: general global MINLP solvers already existed when she started. Reference points:
  - BARON: the GAMS BARON manual's reference list includes Tawarmalani and Sahinidis, "A polyhedral branch-and-cut approach to global optimization", *Math. Program.* 103(2):225–249, 2005 (DOI 10.1007/s10107-005-0581-8).
  - Couenne: its README says "This project was initiated in 2006 within a collaboration between IBM and Carnegie Mellon University" and names Pietro Belotti as maintainer. Belotti, Lee, Liberti, Margot and Wächter published "Branching and bounds tightening techniques for non-convex MINLP", *Optim. Methods Softw.* 24:597–634, 2009 (DOI 10.1080/10556780903087124); I did not read it, so I do not claim what it describes.

  She was a later entrant, and she describes her contribution narrowly: "Adding these equations which were redundant in the original problem formulation tightened the relaxation. This was already known. But what we did was that we actually um found ways of getting these equations." [stated, ASR captions, 12:44]
- **Career effect** [stated, ASR captions]: "So this is the work that got me hired uh by this department." [11:12] and "So uh this one uh best paper in the journal of global optimization and got me this job." [12:44]
- **Exit from the commercial solver line** [practice]:
  - No ANTIGONE paper after 2014. The GAMS 40 release notes list "ANTIGONE 1.1" in their platform table.
  - GAMS 40.1.0 (1 Aug 2022): "As announced, dropped GLOMIQO. The use of ANTIGONE is equivalent." [observed] (S)
  - Her solver building resumed in open-source Python on the EPSRC fellowship (`galini` repository from 2 Apr 2018). She left the C++/GAMS line quietly; **no stated reason** in anything read.
- **Context** [practice]: the CV still separates this PhD-era code from her team's: "The following implementations are primarily written by me. Implementations of my group's optimisation algorithms, i.e. code primarily written by my team, are on our GitHub account." (CV p.10)

### T3. A move for personal reasons and a fellowship framed on medicine (2011–2018)

- **Trigger** [observed] (P, ASR): Pistikopoulos's account of the late-2011 call (the couple moving to the UK). She had already given a CPSE seminar in July 2011, at his invitation (CV S01) [practice]. She herself gives no reason in the sources read.
- **Framing** [practice] (P): RAEng fellowship "Towards rational chemotherapy strategies: a hybrid computational / experimental approach" (ORCID, 2012-10 to 2017-10).
- **Outputs** [practice]: biomedical and bioprocess papers with Mantalaris, Panoskaltsis and Pistikopoulos, e.g.
  - "Global superstructure optimisation of red blood cell production in a parallelised hollow fibre bioreactor", *Comput. Chem. Eng.* 71:532–553, 2014 (DOI 10.1016/j.compchemeng.2014.10.004);
  - "Stem cell biomanufacturing under uncertainty: A case study in optimizing red blood cell production", *AIChE J.* 64(8):3011–3022 (online 2017-12-07; DOI 10.1002/aic.16042).

  The solver line ran in parallel (ANTIGONE 2013–2014).
- **Exit from the Mantalaris/Pistikopoulos collaboration** [practice]: its last paper went online in December 2017 (the *AIChE J.* paper above, CV J33), and ModLife/SyMBioSys ended in 2019. Her talk theme stops at 02/2015 (S06), apart from an AIChE "Futures Series" talk in 10/2018 (I23). **Reason not stated.**
- **But the biomedical line did not simply stop; it turned into Bayesian optimisation** [practice] (P, CV). Through the ModLife network, Olofsson (ModLife-funded PhD) and the KU Leuven group of L. Geris applied Bayesian optimisation to tissue engineering:
  - Mehrian, Guyot, Papantoniou, Olofsson, Sonnaert, Misener, Geris, "Maximizing Neotissue Growth Kinetics in a Perfusion Bioreactor: An In Silico Strategy Using Model Reduction and Bayesian Optimization", *Biotechnology & Bioengineering* 115:617–629, 2018 (CV J29);
  - Olofsson, Mehrian, Calandra, Geris, Deisenroth, Misener, "Bayesian Multi-Objective Optimisation with Mixed Analytical and Black-Box Functions: Application to Tissue Engineering", *IEEE Transactions on Biomedical Engineering* 66:727–739, 2019 (CV J35).

  She still used this tissue-engineering case to explain Bayesian optimisation in 2024 ("with the tissue engineering example it was an expensive simulation takes a while while to run" [stated, ASR captions, SCI 03/2024]). [inferred]: the biomedical application domain was the bridge from deterministic global optimisation to Bayesian optimisation.
- **Later re-entries in another form** [practice]: biomolecular assay design through Bayesian optimisation (Sedgwick, co-advised with Stevens, thesis 2023) and cholera surveillance (Wellcome 2023–26). Homepage: "This Wellcome Trust-funded project is part of a much larger consortium, I contribute to the design of experiments work." [stated]

### T4. Chemical Engineering → Computing (2014), and its slow consequences

- **Event** [practice]: job talk 03/2014; Lecturer from 2014.
- **How others saw it** [observed, ASR captions, Pistikopoulos 2023, 51:13]: "we're not very happy that you know Ruth was hijacked by the department of computing we wanted to her to stay within the chemical engineering department".
- **How she tells it** [stated, ASR captions, SCI public lecture 03/2024]: "my undergraduate and my PhD are uh both in chemical engineering uh small but embarrassing secret um all of my worst marks are in chemistry" and "this whole I like chemistry though I'm not great at it has gotten me to a computer science department where I spend a lot of time collaborating with chemists who are very good at what they do uh at uh BSF [sic, ASR: BASF]".
- **Consequences, dated** [practice]: the identity shift took four to eight years (§1.3). First arXiv item: Nov 2015. First CS conference paper: ICML 2018. BCS member 2017, Fellow 2020. MOS member 2021. ML categories dominate her arXiv output from 2022. NeurIPS reviewing from 2022, area chair 2024.

### T5. Students' projects become lines: heat recovery, symmetry, structure detection (2014–2020)

- **What** [practice]:
  - Mistry's MEng project (2014–15) became M. Mistry, R. Misener, "Optimising heat exchanger network synthesis using convexity properties of the logarithmic mean temperature difference", *Comput. Chem. Eng.* 94:1–17, 2016 (DOI 10.1016/j.compchemeng.2016.07.001). It led to an EPSRC First Grant (2017–18) and the SEA 2017 plenary "Designing Energy-Efficient Heat Recovery Networks using Mixed-Integer Nonlinear Optimisation" (Baltean-Lugojan, Floudas, Misener, Mistry; DOI 10.4230/LIPIcs.SEA.2017.1, from DBLP).
  - Ceccon's MSc (2015) became F. Ceccon, G. Kouyialis, R. Misener, "Using functional programming to recognize named structure in an optimization problem: Application to pooling", *AIChE J.* 62(9):3085–3095, 2016 (DOI 10.1002/aic.15308), and then "SUSPECT: MINLP special structure detector for Pyomo" (Ceccon, Siirola, Misener), *Optim. Lett.* 14(4):801–814 (online 2019-02-16; DOI 10.1007/s11590-019-01396-y).
  - Kouyialis's symmetry work: Kouyialis, Misener, "Symmetry Detection for Quadratically Constrained Quadratic Programs Using Binary Layered Graphs" (arXiv:1712.05222), published as Kouyialis, Wang, Misener, "Symmetry Detection for Quadratic Optimization Using Binary Layered Graphs", *Processes* 7(11), 2019 (CV J40). The heat-recovery follow-up: Letsios, Kouyialis, Misener, "Heuristics with Performance Guarantees for the Minimum Number of Matches Problem in Heat Recovery Network Design" (arXiv:1709.04688; CV J30, *Comput. Chem. Eng.* 113:57–85, 2018).
- **Trigger** [practice]: MEng and MSc projects. Her own verdict [stated, ASR captions, 45:33]: "where we were able to jump forward on a more academic problem was in uh where Mitten [sic, ASR: Miten] figured out uh the convexity uh of this one structure and basically then it was that these problems that had been super difficult were now quite easy."
- **Exit** [practice]: the heat-recovery and symmetry line ends with the 2018 Kouyialis thesis and the 2018–2019 papers. Pooling continues separately (01-publications.md SW1; GALINI 2022).

### T6. Computer-science neighbours and grants widen the portfolio (2015–2021): uncertainty, scheduling, approximation, explainability, verification

- **Trigger, in her words** [stated, ASR captions, 2023, 46:04–46:34], answering whether her vision had changed since she was hired: "basically I'm a person who chooses my my my my vision in some part by my pub buddies. Um so basically um anyone who wants to come to the pub with me we will end up writing a paper together after after some amount of time." Then: "quite a lot of investigations into uncertainty and then quite a lot of investigations into datadriven constraints that basically came from being in a computer science department and being introduced to some of this stuff. Um and then things like getting to work with computational argumentation with Francesca. These kind of things come from just being in a department full of really cool researchers. So in some ways very opportunistic."
- **A named introduction** [stated, ASR captions, 21:25]: "The way that Allesio [sic, ASR: Alessio Lomuscio] and his team introduced me to this problem is maybe I don't want to solve the forward problem all the time where I set the x's and I figure out the y's."
- **Grants and partners that carried it** [practice] (CV, homepage): U2 (EPSRC, 2015–19), whose research-associate funding brought postdoc Letsios; ROAD2H (2017–20, with Toni); the Schlumberger CASE studentship (2017–21); Royal Mail (Bradley).
- **Outputs** [practice], for example:
  - Cyras, Letsios, Misener, Toni, "Argumentation for Explainable Scheduling", AAAI 2019 (DOI 10.1609/aaai.v33i01.33012752);
  - Botoeva, Kouvaros, Kronqvist, Lomuscio, Misener, "Efficient Verification of ReLU-Based Neural Networks via Dependency Analysis", AAAI 2020 (DOI 10.1609/aaai.v34i04.5729);
  - Wiebe, Cecílio, Misener, "Data-Driven Optimization of Processes with Degrading Equipment", *Ind. Eng. Chem. Res.* 57(50):17177–17191, 2018 (DOI 10.1021/acs.iecr.8b03292);
  - Campos, Misener, Parpas, "A multilevel analysis of the Lasserre hierarchy", *Eur. J. Oper. Res.* 277(1):32–41, 2019 (DOI 10.1016/j.ejor.2019.02.016);
  - Letsios et al., "Approximation algorithms for process systems engineering", *Comput. Chem. Eng.* 132:106599, 2020 (DOI 10.1016/j.compchemeng.2019.106599);
  - Letsios, Mistry, Misener, "Exact lexicographic scheduling and approximate rescheduling", *Eur. J. Oper. Res.* 290(2):469–478, 2021 (DOI 10.1016/j.ejor.2020.08.032);
  - Letsios, Bradley, Suraj G, Misener, Page, "Approximate and robust bounded job start scheduling for Royal Mail delivery offices", *J. Sched.* 24(2):237–258, 2021 (DOI 10.1007/s10951-021-00678-7);
  - Wiebe, Cecílio, Dunlop, Misener, "A robust approach to warped Gaussian process-constrained optimization", *Math. Program.* 196(1–2):805–839 (online 2022-01-19; DOI 10.1007/s10107-021-01762-8).
- **Exit** [practice]:
  - The scheduling, argumentation and approximation papers stop after 2021. Their ends coincide with the ends of U2 (2019) and ROAD2H (2020) and with Letsios's move to King's College London [inferred link].
  - The Lasserre line ends with Campos, Misener, Parpas, "Partial Lasserre relaxation for sparse Max-Cut", *Optim. Eng.* 24:1983–2004 (online 2022-08-17; DOI 10.1007/s11081-022-09763-y).
- **Her own 2023 agenda for these strands** [stated, ASR captions, 38:03]: "maybe I've gotten to do some work in the last few years that is now including these datadriven constraints and sort of including a lot of um sort of learning constraints from data and also incorporating uncertainty. Um, and those have kind of been a little bit separate in my in my career and I would like them to be a little bit more together."

### T7. Machine learning inside the solver: tried early, then dropped (2017–2019)

- **Trigger** [practice + stated]: collaboration with co-authors P. Bonami and A. Tramontani, and the IBM PhD Fellowship to Baltean-Lugojan (2017–18). The Couenne README lists Bonami's affiliation as "IBM Cplex"; Tramontani's affiliation was not checked. In 2023 she listed IBM among her industrial partners: "I've also had smaller projects uh with IBM" [stated, ASR captions, 33:08–33:39].
- **Output** [practice]: Baltean-Lugojan, Bonami, Misener, Tramontani, "Scoring positive semidefinite cutting planes for quadratic optimization via trained neural networks", Optimization Online, posted 2018-11-26 (page shows "Citation November 2019"). She gave seven talks on it between 03/2018 and 12/2019 (§1.2), and Baltean-Lugojan presented it at ISMP 2018 (I20).
- **Timing** [practice]: the preprint appeared 11 days after Bengio, Lodi and Prouvost's survey "Machine Learning for Combinatorial Optimization: a Methodological Tour d'Horizon" (arXiv:1811.06128, 2018-11-15). She was there at the start of the learning-for-solvers wave.
- **Exit** [practice]: a Crossref title search on 2026-10-10 finds no journal version, and no later learning-inside-the-solver work appears in her arXiv (46) or DBLP (93) records. **Reason not stated.** 01-publications.md §1.9 reaches the same conclusion independently.

### T8. Optimisation over trained models: the turn that defines her 2020s (2017–)

- **Triggers:**
  1. **Industrial** [stated] (P, homepage Grants): the entry "BASF Seed Funding", dated May 2017 – August 2017, reads "We studied optimisation problems with functions learnt from data, e.g. gradient boosted trees, embedded." The first preprint's abstract states the users' motive [stated] (arXiv:1803.00952v1): "Decision trees effectively represent the sparse, high dimensional and noisy nature of chemical data from experiments. Having learned a function from this data, we may want to thereafter optimize the function, e.g., picking the best chemical process catalyst. In this way, we may repurpose legacy predictive models."
  2. **Prior interest, a year before the seed money** [stated] (P, essay p.14), on Floudas's grey-box work with Boukouvala and Hasan: "his new work was especially exciting because it develops optimization methodology for applications where some of the governing equations are known but others have to be determined using a data-driven methodology [138]." She co-authored the survey F. Boukouvala, R. Misener, C. A. Floudas, "Global optimization advances in Mixed-Integer Nonlinear Programming, MINLP, and Constrained Derivative-Free Optimization, CDFO", *Eur. J. Oper. Res.* 252(3):701–727, 2016 (DOI 10.1016/j.ejor.2015.12.018).
  3. **Colleagues in Computing**: Lomuscio's verification group (T6).
  4. **People with fellowships**: Kronqvist (2019–21) and Tsay (2020–22) [practice].
  5. **An open-source partner lab**: "omelette [sic, ASR: OMLT] was developed in collaboration with researchers from imperial college in london carnegie mellon in pittsburgh and zandia [sic, ASR: Sandia] national laboratories in albuquerque" [stated, ASR captions, OMLT introduction video, 03/2022]. In 2023: "I collaborate with quite a number of people from uh Sandas [sic, ASR: Sandia] National Laboratories in the area of open source software." [stated, ASR captions, 33:08]. The Pyomo link predates OMLT: SUSPECT (2019) is co-authored with J. D. Siirola (T5).
- **Timing relative to the field** [practice]:
  - Trees: V. V. Mišić posted "Optimization of Tree Ensembles" on 2017-05-30 (arXiv:1705.10883; *Oper. Res.* 68(5):1605–1624, 2020; DOI 10.1287/opre.2019.1928). Her first preprint came nine months later and cites it: "Mišić, V. V. Optimization of Tree Ensembles. ArXiv eprints, 2017. arXiv:1705.10883." (arXiv:1803.00952v1, references).
  - ReLU networks: Fischetti and Jo posted "Deep Neural Networks as 0-1 Mixed Integer Linear Programs: A Feasibility Study" on 2017-12-17 (arXiv:1712.06174; published as "Deep neural networks and mixed integer linear optimization", *Constraints* 23(3):296–309, 2018; DOI 10.1007/s10601-018-9285-6). Anderson, Huchette, Ma, Tjandraatmadja and Vielma posted "Strong mixed-integer programming formulations for trained neural networks" on 2018-11-05 (arXiv:1811.01988; *Math. Program.* 183:3–39, 2020; DOI 10.1007/s10107-020-01474-5).
  - In 2021 she positioned her network formulations against the latter [stated, ASR captions, Sevilla seminar 04/2021]: "there's a really nice paper of anderson at all that recently appeared in operations research [sic: the paper appeared in *Math. Program.*; slip or ASR not resolved] that's going to develop exponentially many cuts from a node's convex hull".
  - **Reading** [inferred]: an early follower for trees, a second-wave entrant for ReLU networks, and the toolmaker of the field (OMLT, 2022; COIN-OR Cup 2022).
- **The first paper was reshaped** [practice]:
  - arXiv v1 (2018-03-02): "Optimization with Gradient-Boosted Trees and Risk Control", authors Mistry, Letsios, Misener, Krennrich, Lee.
  - Published as "Mixed-Integer Convex Nonlinear Optimization with Gradient-Boosted Trees Embedded", *INFORMS J. Comput.* 33(3):1103–1119, 2021 (DOI 10.1287/ijoc.2020.0993), authors Mistry, Letsios, Krennrich, Lee, Misener. Misener moved from third to last author.
  - Reasons not stated.
- **The chain that followed** [practice]:
  1. Thebelt et al., "ENTMOOT: A framework for optimization over ensemble tree models", *Comput. Chem. Eng.* 151:107343, 2021 (DOI 10.1016/j.compchemeng.2021.107343; arXiv:2003.04774).
  2. Kronqvist, Misener, Tsay, "Between Steps: Intermediate Relaxations Between Big-M and Convex Hull Formulations", CPAIOR 2021, LNCS pp. 299–314 (online 2021-06-17; DOI 10.1007/978-3-030-78230-6_19).
  3. Tsay, Kronqvist, Thebelt, Misener, "Partition-based formulations for mixed-integer optimization of trained ReLU neural networks", NeurIPS 2021 (arXiv:2102.04373).
  4. Ceccon et al., "OMLT: Optimization & Machine Learning Toolkit", *J. Mach. Learn. Res.* 23(349), 2022 (arXiv:2202.02414).
  5. Misener, Biegler, "Formulating data-driven surrogate models for process optimization", *Comput. Chem. Eng.* 179:108411, 2023 (DOI 10.1016/j.compchemeng.2023.108411).
  6. Kronqvist, Misener, Tsay, "P-split formulations: a class of intermediate formulations between big-M and convex hull for disjunctive constraints", *Math. Program.* 218(1–2):57–94 (online 2025-06-09; DOI 10.1007/s10107-025-02232-1; arXiv:2202.05198, v1 2022-02-10).
- **She brought MINLP habits into the new domain** [stated, ASR captions, Sevilla 04/2021]: "i mean optimization based bounce [sic, ASR: bounds] tightening has always been important to me because i really like minlp".
- **Industry let the code go open** [stated, ASR captions, Imperial panel 2021]: "what they've let us do is they've let us release this software open source".

### T9. Bayesian optimisation and design of experiments: an early seed, a late full entry (2015 → 2020 →)

- **Seeds** [practice]:
  - D. Ulmasov et al., "Bayesian Optimization with Dimension Scheduling: Application to Biological Systems" (arXiv:1511.05385, MSc project co-supervised with Deisenroth).
  - Olofsson, Deisenroth, Misener, "Design of Experiments for Model Discrimination Hybridising Analytical and Data-Driven Approaches", ICML 2018 (arXiv:1802.04170). Olofsson's PhD was ModLife-funded (2016–20).
  - The tissue-engineering applications with Geris's group (CV J29, 2018; J35, 2019; titles in T3).
- **Full entry** [practice]:
  - ENTMOOT (2020) used tree models as surrogates.
  - Folch et al., "SnAKe: Bayesian Optimization with Pathwise Exploration", NeurIPS 2022 (arXiv:2202.00060).
  - Thebelt et al., "Tree ensemble kernels for Bayesian optimization with known constraints over mixed-feature spaces", NeurIPS 2022 (arXiv:2207.00879).
  - Folch et al., "Combining multi-fidelity modelling and asynchronous batch Bayesian Optimization", *Comput. Chem. Eng.* 172:108194, 2023 (DOI 10.1016/j.compchemeng.2023.108194); the journal's Best Paper (CV).
  - Folch et al., "Transition Constrained Bayesian Optimization via Markov Decision Processes", NeurIPS 2024 (arXiv:2402.08406), with Krause and Mutný.
  - Dürholt et al. (BASF-led), "BoFire: Bayesian Optimization Framework Intended for Real Experiments", *J. Mach. Learn. Res.* 26(204), 2025 (arXiv:2408.05040).
  - Boyne et al., "BARK: A Fully Bayesian Tree Kernel for Black-box Optimization", ICML 2025 (arXiv:2503.05574).
- **Triggers** [practice + stated]:
  - BASF studentships (homepage and CV): "Global optimisation with ensemble machine learning models" (2019–22), "Time-Indexed, Batch Bayesian Optimization for Flow Chemistry" (2020–24), "active learning with mixed-feature input spaces" (2023–27).
  - The StatML doctoral centre (2019–27).
  - BASF's own vision [stated, ASR captions, Manchester 01/2025]: "the guy who is the boss of the guy the people who I collaborate with has this idea of what he calls autonomous research machines where instead of a human going into the lab and sort of doing experiments to for instance optimize uh reactions or improve uh yield for for a particular product or uh improved selectivity you should instead um have everything uh automated".
  - Her 2022 public framing [stated] (Imperial News, 18 Jul 2022): "Like many fields, industrial chemistry is undergoing a digital transformation in the 21st century, and one of our strengths at Imperial is in applying digital technologies to automate and optimise chemical R&D and manufacturing. This can greatly benefit from new algorithms that can be used in research, for example, to make decisions on which experiments should be carried out next."
- **Timing** [stated + inferred]: she treats the method as established machine learning, so this was an entry after the ML consensus: "maybe we sometimes forget that the that the technology we're presenting is actually pretty old and it's been around for a while in the case of um basing [sic, ASR: Bayesian] optimization and gaussian processes" [stated, ASR captions, SCI 03/2024]. Her differentiators [inferred, consistent with 01-publications.md SW4]: acquisition functions over trees, graphs and mixed spaces optimised with MINLP technology, and chemistry constraints (transitions, paths, asynchronous batches, multi-fidelity).
- **Funding and software are coupled, by her account** [stated, ASR captions, Manchester 01/2025], on BoFire: "I use it all the time I am funded by BSF [sic, ASR: BASF] so uh I am also you know my my PhD students are paid to put it put it put their things in".
- **A failure inside the line** [stated, ASR captions, Manchester 01/2025], on path-based BO (SnAKe): "the PHD student came to me and was explaining to me you know this doesn't actually work um and what was crazy about it is what I like so much about Bas opt is that it's a global optimization method and all I had done with this set of ideas is I had taken a global optimization method and I had turned it into a local optimization method". Later: "I took a global optimization algorithm I turned it into a path-based algorithm but that's a local optimization algorithm so I mean that's that's what we know from first order optimization that's not so tough I should have understood this the way that um uh Jose fixed this is that he developed um something called uh Point deletion".
- **Collaborations can come from students** [stated, ASR captions, Manchester 01/2025]: "I did not come up with this collaboration um my two of my PhD students went to this AI for good dog tool [sic, ASR] and they came back with this collaboration um with this team in uh in Uganda". The output: Stoddart et al., "Gaussian Processes for Monitoring Air-Quality in Kampala" (arXiv:2311.16625; NeurIPS 2023 workshop, CV W02).

### T10. Graph-structured spaces (2023–2026)

- **What** [practice]:
  - Zhang et al., "Optimizing over trained GNNs via symmetry breaking", NeurIPS 2023 (arXiv:2305.09420).
  - Hojny, Zhang, Campos, Misener, "Verifying message-passing neural networks via topology-based bounds tightening", ICML 2024 (arXiv:2402.13937).
  - Zhang et al., "Augmenting optimization-based molecular design with graph neural networks", *Comput. Chem. Eng.* 186:108684, 2024 (DOI 10.1016/j.compchemeng.2024.108684; arXiv:2312.03613).
  - Zhang et al., "Limeade: Let integer molecular encoding aid", *Comput. Chem. Eng.* 199:109115, 2025 (DOI 10.1016/j.compchemeng.2025.109115).
  - Xie et al., "Global optimization of graph acquisition functions for neural architecture search" (arXiv:2505.23640).
  - Xie et al., "BoGrape: Bayesian optimization over graphs with shortest-path encoded", ICLR 2026 (arXiv:2503.05642).
  - Zhang, Misener, "Beyond adjacency: Graph encoding with reachability and shortest paths" (arXiv:2509.20247, 2025-09-24; code repository `graph_encoding` created 2025-08-18).
- **Trigger** [practice]: Zhang's PhD (Hans Rausing Scholarship, 2021–) and BASF co-authors (Feldmann, Sandfort, Mathea, Walz on the 2023–2025 papers).
- **Her 2026 statement of the agenda** [stated] (P, SIAM OP26 IP1 abstract): "Applications involving optimization over graphs include molecular design, graph neural network verification, neural architecture search, etc. This talk discusses formulating graph spaces using mixed-integer optimization and incorporating application-specific constraints. We discuss computational challenges with these mixed-integer optimization formulations and zoom in on the practical implications for these applications. We mention what has been done (by both ourselves and others) and what other research still needs to be done."
- **Reading** [inferred]: graph spaces are where her MINLP formulation toolkit (encodings, symmetry breaking, bounds tightening) meets her Bayesian-optimisation line. They are the clearest realisation of the 2023 wish to bring her strands "a little bit more together" (T6).

### T11. Hubs, benchmarks and industry posts (2022–2026)

- **Chair** [stated] (Imperial News, 24 Mar 2022): "My existing collaboration with BASF colleagues is already very rewarding. Together with Imperial researchers and the Data Science for Materials and Chemicals teams at BASF, we have already made contributions in data-driven optimisation and developed open source software. I'm looking forward to an increased and intensified collaboration with BASF through this Research Chair."
- **Hubs and centres** [practice] (CV):
  - IConIC (2023–28; "To RM: 6 years of postdoctoral funding"; £6.865M co-I);
  - AIchemy (2024–29; £12M co-I; "one of six co-directors"; hub site: Leadership Team);
  - CCMI doctoral centre (2024–33).
- **Field-level outputs** [practice]:
  - Mroz et al. (19 authors incl. Misener), "Cross-disciplinary perspectives on the potential for artificial intelligence across chemistry", *Chem. Soc. Rev.* 54:5433–5469, 2025 (DOI 10.1039/d5cs00146c).
  - Boyne et al., "The Catechol Benchmark: Time-series Solvent Selection Data for Few-shot Machine Learning", NeurIPS 2025 Datasets & Benchmarks (arXiv:2506.07619). It is the only datasets-and-benchmarks entry among her 16 CS conference papers (CV C01–C16).
- **Industry posts** [practice]: Amazon Scholar from 2025 (CV; homepage; Imperial profile: "I also hold a post as an Amazon Scholar."). Earlier Amazon contacts in the CV are the "Amazon Supply Chain Optimization Summit 09/10/2017" and a 10/2022 seminar for "Research Science Amazon Transportation Services" (S38). Whether these led to the post is my guess [inferred]. What the role involves is **not public** in anything read.
- **Generative AI, 2023 → 2025** [stated, ASR captions]:
  - March 2023, asked whether generative AI might make her redundant: "Generative AI, you know, um, generative AI will do. I mean, it'll I don't know. It's a good question. Probably not. Probably not. I just don't understand. I don't I I I mean we we um I don't understand it well enough to know if one that that any of this work would how it would morph for change yet. We're starting to think about it, but I don't have any ideas at this point really." [40:57–41:28]
  - January 2025: "in terms of what molecule to develop that's basically a generative AI problem and you know we were we were making fun of some sort of approaches for this uh earlier but ultimately it's what you want to do it is it is a generated AI problem then I'm an optimization person I'm interested in design of experiments".
  - [practice, absence]: no paper on large language models or agents appears among her 46 arXiv or 93 DBLP records as of 2026-10-10.

---

## 4. Entering and leaving topics relative to the field

| Topic | Field reference point (checked) | Her entry | Her exit or status | Reading [inferred] |
|---|---|---|---|---|
| Piecewise-linear MILP relaxations for pooling | Meyer & Floudas, *AIChE J.* (online Oct 2005); Dey & Gupte, *Oper. Res.* 2015 | 2008–2009 (first paper May 2009) | Main line to 2011 (APOGEE); returned 2016–2018 with complexity results; pooling again in GALINI (2022) and a 10/2018 gas-transport plenary (K10) | Early, inside the advisor's programme; she came back after the field had analysed it |
| General global MIQCQP/MINLP solvers | BARON (2005 branch-and-cut paper in its GAMS manual); Couenne (project begun 2006, per its README) | 2008 promise; GloMIQO 2012; ANTIGONE 2013 | ANTIGONE stays 1.x; GAMS drops GloMIQO (Aug 2022); Python GALINI 2018–2022, general paper unpublished (§5); last solver plenaries 2019–2021 | A later entrant with a structure-detection niche, who left commercial development without explanation |
| Bioprocess and biomedical optimisation | — | 2012–2013 (fellowship) | Mantalaris/Pistikopoulos papers to 2017/2018; grants to 2019; tissue-engineering Bayesian optimisation with Geris 2018–2019 | Entered with the move and the host; the deterministic line ended with the grants (reason not stated), while the domain carried her into Bayesian optimisation |
| Scheduling under uncertainty, explainable scheduling | — | 2016–2017 (Letsios, Royal Mail, Toni) | Last papers 2021 | "Very opportunistic" by her own account |
| Learning inside the solver (cut selection) | Bengio, Lodi & Prouvost survey, 2018-11-15 | Preprint 2018-11-26 | Unpublished; last talk 12/2019 | Early, then abandoned |
| Optimisation over trained tree ensembles | Mišić preprint, 2017-05-30 | Preprint 2018-03-02 (cites Mišić) | Ongoing (OMLT, tree kernels, BARK 2025) | Early follower who became the toolmaker |
| MIP over trained ReLU networks | Fischetti & Jo preprint 2017-12-17; Anderson et al. preprint 2018-11-05 | AAAI 2020 (verification), NeurIPS 2021 | Ongoing (P-split in *Math. Program.* 2025/2026; OMLT) | Second wave; her contribution is parametric intermediate formulations plus a toolkit |
| Bayesian optimisation and design of experiments | (her 2024 view: the technology is "pretty old") | Seed Nov 2015; full from 2020 | Ongoing; her main line 2022–2026 | After the ML consensus, set apart by MINLP-solved acquisition and chemistry constraints |
| Graph and molecule spaces | — | NeurIPS 2023 | Ongoing; SIAM OP26 plenary 2026 | Her current frontier |
| Large language models and generative AI | — | Not entered (no paper by Oct 2026) | — | Positioned as adjacent to her work (2025) |

---

## 5. Failures, abandoned and reshaped work (trajectory view)

1. **The general GALINI solver paper never appeared** [practice] (P).
   - Preprint: Baltean-Lugojan, Bynum, Ceccon, Li, Misener, "GALINI: An extensible mixed-integer quadratically-constrained optimization solver", Optimization Online, posted 2021-01-14. A Crossref title search on 2026-10-10 finds no journal version.
   - The published GALINI paper narrows the scope: F. Ceccon, R. Misener, "Solving the pooling problem at scale with extensible solver GALINI", *Comput. Chem. Eng.* 159:107660, 2022 (DOI 10.1016/j.compchemeng.2022.107660; arXiv:2105.01687).
   - Compare the fellowship's stated aim [stated] (homepage): "This fellowship develops GALINI, new decision-making software constructing and deploying next generation process optimisation tools dealing with combinatorial complexity, disparate temporal/spatial scales, and safety considerations."
   - Whether the general paper was submitted and rejected: **not known**.
2. **Learning-based SDP cut selection was left as a preprint** (T7).
3. **The gradient-boosted-tree paper was retitled and its author order changed** (T8). It took 3.3 years from preprint to journal. The v1 PDF uses ML-conference typesetting ("*Equal contribution", numbered affiliations, "Correspondence to"). Whether it went to an ML venue first is **not documented**; this is a weak inference.
4. **Path-based Bayesian optimisation first behaved as a local method**, by her account; the student found the flaw and fixed it (T9).
5. **Her solvers were retired or frozen** [observed] (S): GAMS dropped GloMIQO on 1 Aug 2022, and ANTIGONE is listed as version 1.1.
6. **Lines closed without a stated reason** [practice]: the deterministic biomedical-systems work with Mantalaris and Pistikopoulos (2013–2018; its domain continued in Bayesian optimisation, T3), heat recovery and symmetry (2014–2020), scheduling and argumentation (2017–2021), Lasserre hierarchies (2019–2022). Each end coincides with a grant end or a person's departure [inferred].
7. **Corrections and retractions**: none of the 31 DOIs of her papers that I looked up directly on Crossref carries an update-to (correction or retraction) record. A dedicated Retraction Watch search was not done.
8. **Rejections**: none documented in the public sources read.

---

## 6. Era and resource context by period

| Period | Seniority | Money (CV, homepage) | People (CV) | Tools and outputs [practice] |
|---|---|---|---|---|
| 2007–2012 | PhD student | NSF Graduate Research Fellowship ($120k); advisor's grants | Floudas group | C++ solvers linked to GAMS and sold through Princeton and GAMS; chemical-engineering and OR journals (*Ind. Eng. Chem. Res.*, *Comput. Chem. Eng.*, *J. Optim. Theory Appl.*, *J. Global Optim.*, *Math. Program.*). Hardware: see 01-publications.md (single workstation; not re-checked here) |
| 2012–2014 | RAEng Research Fellow, CPSE | Fellowship £539k (2012–17) | Collaborates with the Mantalaris/Pistikopoulos lab (PhD students Fuentes-Garí 2012–15, Savvopoulos 2013–18) | ANTIGONE release; bioreactor superstructure models |
| 2014–2017 | Lecturer, Computing | Co-I on U2 (£765k), ModLife and SyMBioSys (£507k each) | 1 → 6 own PhD students; MEng and MSc projects as the pipeline | Students lead the papers; first arXiv items |
| 2017–2020 | Senior Lecturer | EPSRC fellowship £984k incl. 6 postdoc-years; First Grant £101k; BASF seed £40k → studentship £270k; ROAD2H (£1.516M co-I); IBM and Schlumberger studentships | Peak of 7–8 PhD students; postdocs Letsios, Cyras, Campos; fellow Kronqvist | Open-source Python and Pyomo on GitHub; first CS venues (ICML 2018, AAAI 2019 and 2020) |
| 2020–2022 | Professor | Eli Lilly partnership (£4.182M co-I); StatML CDT (£6.159M co-I); BASF studentships; ADOPT (£1.318M co-I) | Fellows Kronqvist and Tsay; postdocs Kappatou, Ceccon, Mistry | NeurIPS papers; OMLT (COIN-OR Cup) |
| 2022–2026 | Professor; BASF/RAEng Chair; Amazon Scholar from 2025 | Chair £216k; IConIC (£6.865M co-I); AIchemy (£12M co-I); CCMI; Wellcome cholera (£2.683M co-I); Natural History Museum; BASF molecular-design studentship £42k | Own PhD students fall to 1; 3 postdocs; theses co-supervised with ML and statistics colleagues | ML venues dominate; a benchmark dataset; BoFire with BASF; OMLT maintained by collaborators in 2025–26 (§7) |

Compute resources over time (GPUs, clusters) are not documented in the sources read (Gaps G12).

---

## 7. The last 12 months (2025-10-10 to 2026-10-10)

| Date | Item | Tag | Source |
|---|---|---|---|
| 2025-09-24 (just before the window) | "Beyond adjacency: Graph encoding with reachability and shortest paths" (Zhang, Misener; arXiv:2509.20247); repository `graph_encoding` last pushed 2025-10-25 | [practice] (P) | arXiv API; GitHub API |
| 2025-11-12/13 | Postdoc Campos commits to `Bin-Packing-Optimization-Storage` (created 2025-02-12): a two-dimensional level bin-packing model "extended" with furniture types and same-level/same-bin constraints, solved with Gurobi (README). Possibly the Natural History Museum space-optimisation project; the README does not say [inferred] | [practice] (P) | GitHub API |
| 2025-11-27 | Catechol Benchmark arXiv v2; the paper is in NeurIPS 2025 (Datasets & Benchmarks track) | [practice] (P) | arXiv API; CV C16; DBLP |
| 2025 | Conference talk "A Meta-Learning Approach for Few-Shot Bayesian Optimization of Batch Chemical Processes" (Langdon et al.), 2025 AIChE Annual Meeting (month not verified) | [practice] (P) | Google Scholar |
| 2025-12-03 | CV updated: lists Amazon Scholar (2025–), closes the GAMS Advisory Board (2018–25) and the *Operations Research* AE post (2024–25), announces the OP26 plenary as "Upcoming" | [practice] (P) | CV |
| 2025-12-27 → 2026-07-09 | OMLT commits by collaborators (logins bammari, emsunshine, dovallev): "Patch issue 173", "Tree surrogates with multiple outputs" (2026-01-11), "Add conformal prediction notebooks" (2026-06-24), "Resolve Failing Tests And Patch For Bounds in Linear Tree" (2026-07-09) | [practice] (P) | GitHub API |
| 2026-02-19 | PhD student Boyne modernises ENTMOOT packaging (three commits, "Switch to pyproject.toml") | [practice] (P) | GitHub API |
| 2026 (ICLR 2026) | "BoGrape: Bayesian optimization over graphs with shortest-path encoded" (Xie, Zhang, Qing, Misener, Tsay); arXiv v2 2026-04-21 | [practice] (P) | DBLP; arXiv API |
| 2026-05-06 | "Meta-learning for sample-efficient Bayesian optimisation of fed-batch processes" (Langdon, Patrón, Kappatou, Lee, Shafei, Qing, Misener, van der Wilk, Tsay; arXiv:2605.05382, math.OC). Co-authors include BASF's Lee and Shafei and former postdoc Kappatou (now at BASF per the CV) | [practice] (P) | arXiv API; CV |
| 2026-06-02 | SIAM Conference on Optimization (OP26), Edinburgh: IP1, the first plenary after the opening remarks, "Optimizing over graphs: Challenges, Formulations, and Applications", 8:15–9:00 AM, McEwan Hall, chair Monique Laurent. Delivery **not independently confirmed**; the program is evidence of scheduling | [practice] (P) | SIAM conference program and session page |
| 2026 (vol. 218) | P-split in *Math. Program.* 218(1–2):57–94 (online since 2025-06-09) | [practice] (P) | Crossref; DBLP |
| 2026-08-04 | Misener herself (login `rmisener`) adds an MIT licence to `hens`, the 2016 heat-exchanger-network code | [practice] (P) | GitHub API |
| 2026-08 | End of the Wellcome cholera-surveillance project (homepage dates) | [practice] (P) | homepage, Grants |
| 2026-10-02 | "Amortized Structured Stochastic Variational Inference for Gaussian Process Latent Variable Models" (Tretiakov, Filippi, Fortuin, Misener, Sedgwick, Odgers; arXiv:2610.03647, stat.ML; v2 2026-10-05) | [practice] (P) | arXiv API |
| as of 2026-10-10 | Homepage team: 3 postdocs, 1 PhD student. Group YouTube channel: newest upload 2024-11-04, none in the window. Google Scholar: 6,188 citations, h-index 36, interests "Computational Optimization, MINLP, Bayesian Optimization, Open-source Software" (as extracted by WebFetch) | [practice] (P) | homepage; YouTube feed; Scholar |

**Reading** [inferred, with caution about publication lag]:
- Within the window: one journal volume (already online in 2025), one ICLR paper, one NeurIPS datasets paper and two new preprints. That is thinner than calendar 2025 (AISTATS, GECCO, ICML, NeurIPS, *Comput. Chem. Eng.*, *Chem. Soc. Rev.*, *Biotechnol. Bioeng.*, *J. Mach. Learn. Res.*).
- Topically the window continues graphs, BO for chemical processes and probabilistic latent-variable models. No new MINLP solver or formulation paper appeared, apart from the P-split journal version.
- Her visible maintenance act in the window is licensing old code. Day-to-day upkeep of OMLT sits with collaborators.

---

## Contradictions (kept, not reconciled)

- **C1. PhD end date.** ORCID (self-asserted) gives "2012-10". The Imperial profile gives "17 Nov 2012". The RAEng fellowship starts "2012-10" (ORCID funding). The fellowship and the doctorate overlap by one or two months.
- **C2. Wu Fellowship span.** CV awards block "2007-12" and homepage "(2007 – 2012)", against the CV's financial section "2007 - 2009" ($12k).
- **C3. ADOPT dates.** Homepage "October 2021 - September 2025" against the CV grants list "2022 - 2026".
- **C4. Eli Lilly partnership dates.** Homepage "February 2020 - January 2025" against the CV "2019 - 2027".
- **C5. Ceccon's destination.** The CV's PhD list says "Now Co-Founder, Apibara"; its postdoc list says "Now Co-Founder, Auclantis".
- **C6. Award name.** CV "W. David Smith, Jr. Graduate Student Paper Award" (2014); homepage "W. David Smith, Jr. Graduation Publication Award" (2014).
- **C7. Stated disinterest in proofs vs proof-bearing work.**
  - 2023 [stated, ASR captions, 30:35]: "if anybody needs uh uh sort of uh just a convergence proof or something to just work because you're going to use one of those components that I that I presented probably you got to find somebody else because it's boring and I'm not interested."
  - Practice: her group publishes complexity and formulation theory. The 2016 pooling preprint is tagged "p/np boundary" and "strongly-polynomial algorithms" on Optimization Online, and P-split builds a hierarchy of formulations.
  - The remark may target isolated proofs rather than theory; that reading is mine [inferred].
- **C8. Constancy vs opportunism, same lecture.** "all I've been doing here at Imperial uh is basically figuring out how to relax better" [05:37] against "So in some ways very opportunistic" [46:34]. Both stated in 2023. The first describes method, the second domains [inferred].
- **C9. When the UK move began.** Pistikopoulos dates Floudas's call "towards the end of 2011". The captions garble the date ("around summer of 200, you know, towards 11"). The CV shows she had already given a CPSE seminar at his invitation in 07/2011 (S01).
- **C10. Stale secondary.** Wikipedia (revision of 2026-09-01) says she "is the director of the Computing & Systems Technology Division of the American Institute of Chemical Engineers"; the CV dates that post 2016–18.
- **C11. Stated vs current practice on videos.** CV header and homepage: her team "releases video presentations on YouTube". The group channel's newest upload is 2024-11-04.
- **C12. GALINI as general software vs the published outcome.** See §5, item 1.
- **C13. Generative AI, 2023 vs 2025.** "I don't have any ideas at this point really" (03/2023) against a 2025 position that molecule discovery "is a generated AI problem" while she is "an optimization person". She also joined the AIchemy leadership in 2024. This is evolution rather than reversal; I keep both.

## Gaps

- **G1.** The PhD thesis was not read. Princeton DataSpace returned HTTP 401; ProQuest was not used (paywall).
- **G2.** No Mathematics Genealogy Project entry for Misener was found.
  - The MGP name search is a POST form; curl could not connect to mathgenealogy.org, and a GET query returns "You must enter a non-null query".
  - A WebSearch restricted to the MGP domains found no Misener page.
  - The Floudas academic tree cited in her essay's footnote (titan.engr.tamu.edu/tree/caf/) no longer resolves.
- **G3.** No stated reason was found for:
  - the move to the UK (only Pistikopoulos's account);
  - joining Computing rather than staying in Chemical Engineering;
  - stopping ANTIGONE development;
  - ending the biomedical, Royal Mail, argumentation and SDP-cut lines;
  - the shrinking own-PhD cohort;
  - taking the Amazon Scholar post.
- **G4.** What the Amazon Scholar role involves is not public in the sources read.
- **G5.** Delivery of the OP26 plenary (2 June 2026) is not independently confirmed.
- **G6.** Three Princeton Chemical and Biological Engineering news items returned HTTP 403: "Misener GS5 Awarded Two UK Fellowships", "Misener *12 Receives Sir George Macfarlane Medal", "Misener and Floudas release ANTIGONE". The date and wording of her 2012 fellowship news are therefore missing.
- **G7.** LinkedIn, where her team says it announces new research, was not used (login required).
- **G8.** Rejections: none documented. The venue history of the 2018 gradient-boosted-tree preprint is unknown.
- **G9.** No 2025–2026 news item about her was found. Two WebSearch calls found none, and Imperial's news search URL returned 404.
- **G10.** The month of the 2025 AIChE talk was not verified.
- **G11.** The supervision status of recent co-authors (Xie, Langdon, Tretiakov) was not established. They are not on her homepage team list.
- **G12.** Compute resources by period (GPUs, clusters) are not documented in the sources read.
- **G13.** Also unusable this run: siam.org's plenary page (403; the SIAM meetings program was used instead), dblp.org person pages (bot wall; the SPARQL endpoint was used instead), the Imperial profile's sub-tabs (404), the publisher landing pages of the 2005 BARON and 2009 Belotti et al. papers (login redirect; 403), their Semantic Scholar abstracts (elided by the publishers), and the GAMS Couenne manual page (404). So I cite those two papers only as dated field markers, not for their content.

## Sources

**Primary relative to Misener (27)**

1. R. Misener, Curriculum vitae, "Updated December 3, 2025", 32 pp. http://www.doc.ic.ac.uk/~rmisener/Misener_CV.pdf (read in full via pdftotext). P
2. R. Misener, homepage "Ruth Misener | Optimization Models, Algorithms, and Software", fetched 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/ P
3. Homepage, "Current Research Team", fetched 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/research-group/current/ P
4. Homepage, "Professional Activities", fetched 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/professional-activities/ P
5. Homepage, "Grants" (project dates and one-line descriptions), fetched 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/grants/ P
6. Imperial College London profile, "Professor Ruth Misener", fetched 2026-10-10. https://profiles.imperial.ac.uk/r.misener P
7. ORCID public record 0000-0001-5612-5417 (educations, employments, fundings; self-asserted entries), public API v3.0, fetched 2026-10-10. https://pub.orcid.org/v3.0/0000-0001-5612-5417 P
8. R. Misener, "Christodoulos Achilleus Floudas", *SIAG/OPT Views and News* 24(1):12–16, October 2016. https://siagoptimization.github.io/assets/views/ViewsAndNews-24-1.pdf P
9. R. Misener, inaugural lecture "Just Relax", Imperial College London, 13 Mar 2023, YouTube dN860HNsAs0. ASR captions saved as `../sources/talks/2023-03-13-just-relax-inaugural-lecture-asr.md` (includes Pistikopoulos's vote of thanks). P (machine transcript)
10. R. Misener, "Autonomous research machines: Self-optimising new chemistry", Manchester Centre for AI Fundamentals seminar, 01/2025 (CV S50), YouTube 2br7KspcQXk. ASR file `../sources/talks/2025-01-manchester-autonomous-research-machines-2br7KspcQXk.txt`. P (machine transcript)
11. R. Misener, "Bayesian optimization & design of experiments", Society of Chemical Industry public lecture, 03/2024 (CV S46), YouTube 9aLOEJNOCho. ASR file `../sources/talks/2024-scitalk-bayesian-optimization-design-of-experiments-9aLOEJNOCho.txt`. P (machine transcript)
12. Imperial online panel "Decision making under uncertainty", 2021 (CV P1), YouTube Cbnfz00SHLg. ASR file `../sources/talks/2021-03-12-imperial-panel-decision-making-under-uncertainty-Cbnfz00SHLg.txt`. P (machine transcript)
13. R. Misener, "Partition-based formulations for mixed-integer optimization of trained ReLU neural networks", Machine Learning NeEDS Mathematical Optimization seminar, 04/2021 (CV S29), YouTube UcNXm24uQjE. ASR file `../sources/talks/2021-04-sevilla-partition-based-formulations-relu-UcNXm24uQjE.txt`. P (machine transcript)
14. R. Misener, "Developing spatial branch & bound solvers", NMPC 2021 plenary, 07/2021 (CV K16), YouTube Z5hbKPx9YDE. ASR file `../sources/talks/2021-08-05-nmpc2021-developing-spatial-branch-and-bound-solvers-Z5hbKPx9YDE.txt` (searched; not quoted). P (machine transcript)
15. R. Misener, "Between formulations or: How I Learned to Stop Worrying and Love Parameters", Cornell seminar, 02/2023 (CV S42), YouTube bC4PDG9EZA8. ASR file `../sources/talks/2023-02-17-cornell-between-formulations-love-parameters-bC4PDG9EZA8.txt`. P (machine transcript)
16. M. Mistry, D. Letsios, R. Misener, G. Krennrich, R. M. Lee, "Optimization with Gradient-Boosted Trees and Risk Control", arXiv:1803.00952v1, 2 Mar 2018 (full text: abstract, introduction, references). P
17. Google Scholar profile AQxtWHoAAAAJ, sorted by date, first 40 rows, fetched 2026-10-10 via WebFetch. https://scholar.google.com/citations?user=AQxtWHoAAAAJ P
18. arXiv API, `au:"Ruth Misener"` (46 records), plus id_list queries, fetched 2026-10-10. https://export.arxiv.org/api/query P
19. GitHub API: `cog-imperial` organisation repositories (33), commits since 2025-10-01 for five repositories, and the README of `Bin-Packing-Optimization-Storage`, fetched 2026-10-10. https://github.com/cog-imperial P
20. CogImperial YouTube channel feed (latest 15 uploads), fetched 2026-10-10. https://www.youtube.com/feeds/videos.xml?channel_id=UCXRdjQRm9XfZj2c4XW1xpzg P
21. SIAM Conference on Optimization (OP26) program and session IP1 (abstract by Misener), fetched 2026-10-10. https://meetings.siam.org/program.cfm?CONFCODE=OP26 and https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=88083 P
22. C. Brogan, "Imperial scoops three new Royal Academy of Engineering research chairs", Imperial News, 24 Mar 2022 (contains Misener's quote). https://www.imperial.ac.uk/news/235034/imperial-scoops-three-royal-academy-engineering/ P
23. D. Silverman, "Imperial & BASF in major partnership to advance future of chemical production", Imperial News, 18 Jul 2022 (contains Misener's quote). https://www.imperial.ac.uk/news/238391/imperial-basf-major-partnership-advance-future/ P
24. Computational Optimisation Group website: post "Sir George Macfarlane Medal" (posted 30 June 2017 by Ruth Misener) and front page, fetched 2026-10-10. https://optimisation.doc.ic.ac.uk/?p=951 and https://optimisation.doc.ic.ac.uk/ P
25. Imperial Spiral repository, discovery API query `dc.contributor.advisor:"Misener, Ruth"` (11 theses), fetched 2026-10-10. https://spiral.imperial.ac.uk/ P
26. Optimization Online pages: 2016/05/5457 (posted 2016-05-22, updated 2018-11-26), 2018/11/6943 (posted 2018-11-26), 2021/01/8207 (posted 2021-01-14). https://optimization-online.org/ P
27. R. Misener, "Introduction to OMLT", CogImperial YouTube channel, 2022-03-22, YouTube 8IpM42mSsWE. ASR file `../sources/talks/2022-03-22-introduction-to-omlt-8IpM42mSsWE.txt`. P (machine transcript)

**Secondary (11)**

28. A. Idle, "Professor Ruth Misener Honoured with 2023 BCS Roger Needham Award", Imperial News, 20 Dec 2023. https://www.imperial.ac.uk/news/250395/professor-ruth-misener-honoured-with-2023/ S
29. AIchemy hub, "The team" page (Leadership Team), fetched 2026-10-10. https://aichemy.ac.uk/the-team/ S
30. DBLP person 04/8800, 93 records via the DBLP SPARQL endpoint (repository script `scripts/dblp_works.py`), fetched 2026-10-10. https://dblp.org/pid/04/8800 S
31. Crossref REST API, DOI metadata and title queries, 2026-10-10. https://api.crossref.org/works S
32. GAMS Development Corp., Release Notes 40 ("40.1.0 Major release (August 01, 2022)"). https://www.gams.com/latest/docs/RN_40.html S
33. Mathematics Genealogy Project, Christodoulos Floudas, id 81417. https://www.mathgenealogy.org/id.php?id=81417 S
34. Mathematics Genealogy Project, Ignacio E. Grossmann, id 36078. https://www.mathgenealogy.org/id.php?id=36078 S
35. Wikidata entities Q47501291 (Misener), Q95989389 (Floudas), Q101554042 (Grossmann), Q7359062 (Sargent). https://www.wikidata.org/ S
36. Wikipedia, "Ruth Misener" (revision of 2026-09-01). https://en.wikipedia.org/wiki/Ruth_Misener S
37. GAMS Development Corp., BARON solver manual and the GAMS documentation bibliography (entry [182], Tawarmalani and Sahinidis 2005), fetched 2026-10-10. https://www.gams.com/latest/docs/S_BARON.html and https://www.gams.com/latest/docs/citelist.html S
38. COIN-OR Couenne README (project history, maintainer, contributor affiliations), fetched 2026-10-10 via the GitHub API. https://github.com/coin-or/Couenne S

**Field reference papers by others (8; metadata checked)**

39. C. A. Meyer, C. A. Floudas, "Global optimization of a combinatorially complex generalized pooling problem", *AIChE J.* 52:1027–1037 (online 2005-10-28). DOI 10.1002/aic.10717 (S)
40. S. S. Dey, A. Gupte, "Analysis of MILP Techniques for the Pooling Problem", *Oper. Res.* 63:412–427, 2015. DOI 10.1287/opre.2015.1357 (S)
41. M. Tawarmalani, N. V. Sahinidis, "A polyhedral branch-and-cut approach to global optimization", *Math. Program.* 103:225–249, 2005. DOI 10.1007/s10107-005-0581-8 (S)
42. P. Belotti, J. Lee, L. Liberti, F. Margot, A. Wächter, "Branching and bounds tightening techniques for non-convex MINLP", *Optim. Methods Softw.* 24:597–634, 2009. DOI 10.1080/10556780903087124 (S)
43. V. V. Mišić, "Optimization of Tree Ensembles", arXiv:1705.10883 (v1 2017-05-30); *Oper. Res.* 68(5):1605–1624, 2020. DOI 10.1287/opre.2019.1928 (S)
44. M. Fischetti, J. Jo, "Deep Neural Networks as 0-1 Mixed Integer Linear Programs: A Feasibility Study", arXiv:1712.06174 (2017-12-17); published as "Deep neural networks and mixed integer linear optimization", *Constraints* 23(3):296–309, 2018. DOI 10.1007/s10601-018-9285-6 (S)
45. R. Anderson, J. Huchette, W. Ma, C. Tjandraatmadja, J. P. Vielma, "Strong mixed-integer programming formulations for trained neural networks", arXiv:1811.01988 (v1 2018-11-05); *Math. Program.* 183:3–39, 2020. DOI 10.1007/s10107-020-01474-5 (S)
46. Y. Bengio, A. Lodi, A. Prouvost, "Machine Learning for Combinatorial Optimization: a Methodological Tour d'Horizon", arXiv:1811.06128 (v1 2018-11-15) (S)

**Papers by Misener cited above (identifiers checked in this run; practice records)**

- Gounaris, Misener, Floudas, *Ind. Eng. Chem. Res.* 48(12):5742–5766, 2009. DOI 10.1021/ie8016048
- Misener, Floudas, *J. Optim. Theory Appl.* 145(1):120–147, 2010. DOI 10.1007/s10957-009-9626-0
- Misener, Thompson, Floudas (APOGEE), *Comput. Chem. Eng.* 35(5):876–892, 2011. DOI 10.1016/j.compchemeng.2011.01.026
- Misener, Floudas (MIQCQP), *Math. Program.* 136(1):155–182, 2012. DOI 10.1007/s10107-012-0555-6
- Misener, Floudas (GloMIQO), *J. Global Optim.* 57(1):3–50, 2013. DOI 10.1007/s10898-012-9874-7
- Misener, Floudas (ANTIGONE), *J. Global Optim.* 59(2–3):503–526, 2014. DOI 10.1007/s10898-014-0166-2
- Misener, Smadbeck, Floudas (GloMIQO 2), *Optim. Methods Softw.* 30(1):215–249, 2015. DOI 10.1080/10556788.2014.916287
- Misener et al. (red blood cell bioreactor), *Comput. Chem. Eng.* 71:532–553, 2014. DOI 10.1016/j.compchemeng.2014.10.004
- Misener et al. (stem cell biomanufacturing), *AIChE J.* 64(8):3011–3022, 2018. DOI 10.1002/aic.16042
- Ulmasov, Baroukh, Chachuat, Deisenroth, Misener, arXiv:1511.05385, 2015
- Mistry, Misener, *Comput. Chem. Eng.* 94:1–17, 2016. DOI 10.1016/j.compchemeng.2016.07.001
- Ceccon, Kouyialis, Misener, *AIChE J.* 62(9):3085–3095, 2016. DOI 10.1002/aic.15308
- Boukouvala, Misener, Floudas, *Eur. J. Oper. Res.* 252(3):701–727, 2016. DOI 10.1016/j.ejor.2015.12.018
- Misener, "Christodoulos Achilleus Floudas", *SIAG/OPT Views and News* 24(1):12–16, 2016 (venue + year + title; PDF read)
- Baltean-Lugojan, Misener, *J. Global Optim.* 71(4):655–690, 2018. DOI 10.1007/s10898-017-0577-y (Optimization Online 2016/05/5457)
- Baltean-Lugojan, Floudas, Misener, Mistry, SEA 2017 keynote abstract. DOI 10.4230/LIPIcs.SEA.2017.1 (DBLP; not resolvable via the Crossref API)
- Letsios, Kouyialis, Misener, min-matches heuristics, arXiv:1709.04688; CV J30, *Comput. Chem. Eng.* 113:57–85, 2018
- Kouyialis, Misener, "Symmetry Detection for Quadratically Constrained Quadratic Programs Using Binary Layered Graphs", arXiv:1712.05222; published as Kouyialis, Wang, Misener, "Symmetry Detection for Quadratic Optimization Using Binary Layered Graphs", *Processes* 7(11), 2019 (CV J40)
- Mehrian, Guyot, Papantoniou, Olofsson, Sonnaert, Misener, Geris, "Maximizing Neotissue Growth Kinetics in a Perfusion Bioreactor: An In Silico Strategy Using Model Reduction and Bayesian Optimization", *Biotechnology & Bioengineering* 115:617–629, 2018 (venue + year + title from the CV, J29)
- Olofsson, Mehrian, Calandra, Geris, Deisenroth, Misener, "Bayesian Multi-Objective Optimisation with Mixed Analytical and Black-Box Functions: Application to Tissue Engineering", *IEEE Transactions on Biomedical Engineering* 66:727–739, 2019 (venue + year + title from the CV, J35)
- Olofsson, Deisenroth, Misener, ICML 2018, arXiv:1802.04170
- Mistry, Letsios, Krennrich, Lee, Misener, *INFORMS J. Comput.* 33(3):1103–1119, 2021. DOI 10.1287/ijoc.2020.0993; arXiv:1803.00952
- Wiebe, Cecílio, Misener, *Ind. Eng. Chem. Res.* 57(50):17177–17191, 2018. DOI 10.1021/acs.iecr.8b03292
- Baltean-Lugojan, Bonami, Misener, Tramontani, "Scoring positive semidefinite cutting planes for quadratic optimization via trained neural networks", Optimization Online 2018/11/6943, 2018
- Cyras, Letsios, Misener, Toni, AAAI 2019. DOI 10.1609/aaai.v33i01.33012752
- Campos, Misener, Parpas, *Eur. J. Oper. Res.* 277(1):32–41, 2019. DOI 10.1016/j.ejor.2019.02.016
- Ceccon, Siirola, Misener (SUSPECT), *Optim. Lett.* 14(4):801–814, 2020. DOI 10.1007/s11590-019-01396-y
- Letsios et al., *Comput. Chem. Eng.* 132:106599, 2020. DOI 10.1016/j.compchemeng.2019.106599
- Botoeva, Kouvaros, Kronqvist, Lomuscio, Misener, AAAI 2020. DOI 10.1609/aaai.v34i04.5729
- Letsios, Mistry, Misener, *Eur. J. Oper. Res.* 290(2):469–478, 2021. DOI 10.1016/j.ejor.2020.08.032
- Letsios, Bradley, Suraj G, Misener, Page, *J. Sched.* 24(2):237–258, 2021. DOI 10.1007/s10951-021-00678-7
- Baltean-Lugojan, Bynum, Ceccon, Li, Misener, "GALINI: An extensible mixed-integer quadratically-constrained optimization solver", Optimization Online 2021/01/8207, 2021
- Thebelt et al. (ENTMOOT), *Comput. Chem. Eng.* 151:107343, 2021. DOI 10.1016/j.compchemeng.2021.107343; arXiv:2003.04774
- Kronqvist, Misener, Tsay, CPAIOR 2021. DOI 10.1007/978-3-030-78230-6_19
- Tsay, Kronqvist, Thebelt, Misener, NeurIPS 2021, arXiv:2102.04373
- Wiebe, Cecílio, Dunlop, Misener, *Math. Program.* 196(1–2):805–839, 2022. DOI 10.1007/s10107-021-01762-8
- Ceccon, Misener, *Comput. Chem. Eng.* 159:107660, 2022. DOI 10.1016/j.compchemeng.2022.107660; arXiv:2105.01687
- Ceccon et al. (OMLT), *J. Mach. Learn. Res.* 23(349), 2022, arXiv:2202.02414
- Folch et al. (SnAKe), NeurIPS 2022, arXiv:2202.00060
- Thebelt et al. (tree-ensemble kernels), NeurIPS 2022, arXiv:2207.00879
- Campos, Misener, Parpas, *Optim. Eng.* 24:1983–2004 (online 2022). DOI 10.1007/s11081-022-09763-y
- Folch et al., *Comput. Chem. Eng.* 172:108194, 2023. DOI 10.1016/j.compchemeng.2023.108194
- Misener, Biegler, *Comput. Chem. Eng.* 179:108411, 2023. DOI 10.1016/j.compchemeng.2023.108411
- Zhang et al. (GNN symmetry breaking), NeurIPS 2023, arXiv:2305.09420
- Stoddart et al. (Kampala air quality), arXiv:2311.16625, 2023
- Zhang et al., *Comput. Chem. Eng.* 186:108684, 2024. DOI 10.1016/j.compchemeng.2024.108684; arXiv:2312.03613
- Folch et al. (transition-constrained BO), NeurIPS 2024, arXiv:2402.08406
- Hojny, Zhang, Campos, Misener, ICML 2024, arXiv:2402.13937
- Dürholt et al. (BoFire), *J. Mach. Learn. Res.* 26(204), 2025, arXiv:2408.05040
- Mroz et al., *Chem. Soc. Rev.* 54:5433–5469, 2025. DOI 10.1039/d5cs00146c
- Boyne et al. (BARK), ICML 2025, arXiv:2503.05574
- Xie et al. (BoGrape), ICLR 2026, arXiv:2503.05642
- Xie et al. (graph acquisition functions for NAS), arXiv:2505.23640, 2025
- Zhang et al. (Limeade), *Comput. Chem. Eng.* 199:109115, 2025. DOI 10.1016/j.compchemeng.2025.109115
- Boyne et al. (Catechol Benchmark), NeurIPS 2025 Datasets & Benchmarks, arXiv:2506.07619
- Zhang, Misener, arXiv:2509.20247, 2025
- Langdon et al., arXiv:2605.05382, 2026
- Tretiakov et al., arXiv:2610.03647, 2026
- Kronqvist, Misener, Tsay (P-split), *Math. Program.* 218(1–2):57–94. DOI 10.1007/s10107-025-02232-1; arXiv:2202.05198
- Langdon et al., "A Meta-Learning Approach for Few-Shot Bayesian Optimization of Batch Chemical Processes", 2025 AIChE Annual Meeting (venue + year + title from Google Scholar)
