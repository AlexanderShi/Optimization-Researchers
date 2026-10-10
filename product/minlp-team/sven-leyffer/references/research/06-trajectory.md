# Sven Leyffer · Research note 06 · Research trajectory

| Field | Value |
|---|---|
| Researcher | Sven Leyffer (living). Argonne National Laboratory, Mathematics and Computer Science (MCS) Division. Argonne profile title (capture of 30 Nov 2025): "Deputy Division Director/Senior Computational Mathematician/Argonne Distinguished Fellow" |
| Dimension | Phase 1, research agent 06 of 06 (nuwa research-craft): research trajectory. Academic timeline, lineage, direction changes and what triggered them, entry and exit timing, the last 12 months (framework §二 agent 6; feeds layer 2 选题 and layer 7 研究组织 of §一) |
| Research date | 2026-10-10 |
| Sources consulted | 41 (38 primary, 3 secondary), numbered T01–T41 under "Sources". WebSearch calls: 3 of 3 |
| Local corpus | `references/sources/{papers,talks,essays,software}` held only `.gitkeep` on 2026-10-10, so there was no user-supplied material. `private/` was not opened |
| Read in full or in part | The 2017 OS Today article (pp. 3–10, in full). The PhD thesis (title page and PDF pp. 12, 16, 23, 27, 43, 59, 77, 104). Dundee report NA/182 pp. 1–2 (read as page images; its fonts do not extract). The 2006 filter history (pp. 1, 4, 7, 8, 15). The Acta Numerica preprint (pp. 1, 11–12). The 2026 Correction (p. 1). First pages and acknowledgments of five arXiv papers. 41 homepage and profile captures from 2001 to 2026. The GitHub files listed under T14 |
| Sibling notes | Notes 01 (publications) and 04 (mentorship) from this run were read as leads only. Every fact below was re-fetched or re-checked in this run, except where it is marked "(note 01/04, not re-checked)" |

**Tags.** [stated] = Leyffer's own words, alone or as coauthor (marked "coauthored"). [practice] = what papers, reports, code, commit records, page edits and seminar records show he did. [observed] = what institutions, prize committees, databases or other people say about him. [inferred] = my reading, with its basis. "primary" or "secondary" refers to the source. Quotations are verbatim (whitespace normalised). Page numbers refer to the PDF or report pagination named in each source line. A web-page edit date ("last edited …") is the date the page itself prints. A capture date is the date of the Wayback Machine snapshot I read.

---

## 0. The trajectory in brief

- **One base, changing extensions.** From at least December 2008 to 2026 his research statement keeps the same first sentence: "I am interested in the development of reliable methods for solving large-scale nonlinear optimization problems and in the implementation and analysis of filter type algorithms." Only the list of areas he is "extending" into changes. It reads MINLP and complementarity until a page edit on 13 September 2021, and design of experiments, machine learning, quantum computing and MINLP after it (§3). [stated · primary]
- **Phases** [practice · primary; the grouping is inferred]:
  1. Dundee, about 1990–2002: deterministic MINLP thesis (title page dated December 1993), then filter methods with Fletcher (1996–2002), SQP-based branch-and-bound (1998), and MPECs solved as NLPs (2000–2002).
  2. Argonne from 2002: MPEC theory, 2002–2009.
  3. MINLP as team science, 2006–2013: FilMINT, the IMA workshop and volume, the Acta Numerica survey.
  4. Side lines tied to the lab's computing mission, 2012–2016.
  5. Mixed-integer optimal control, then mixed-integer PDE-constrained optimization (MIPDECO), from 2013 to now.
  6. Applications in machine learning, experimental design, quantum control and imaging, from 2018.
  7. A return to NLP-solver architecture: augmented-Lagrangian filter, Uno and funnel SQP (2016–2026), plus MPEC B-stationarity (2025–2026).
  8. In July–September 2026, a burst of AI-assisted research projects on his GitHub account.
- **What triggered the turns.** The documented triggers are:
  - owning his own solver (1998);
  - numerical evidence that went against the prevailing view (MPECs, about 2000);
  - collaborators bringing a problem or an idea (Fletcher; Linderoth's student; Kirches and Sager; Vanaret; Gould in 2025; Nurkanović);
  - the laboratory's facilities and programmes (Advanced Photon Source, DOE AI and quantum programmes);
  - a new tool (AI coding and proof agents in 2026).

  No trigger is documented for the move from Dundee to Argonne or for any exit (§4, §5). [mixed tags, given per item below]
- **Timing.**
  - He co-created the filter line.
  - He entered MPEC-as-NLP while it was "commonly regarded as numerically unsafe".
  - He named and promoted MIPDECO as a "new class of problems" in 2019.
  - He consolidated MINLP (survey, edited volume, software) once the field was growing.
  - He entered machine learning (2018–2021) and AI-assisted research (2026) after those waves had started, bringing his own formulations and tools with him.

  [stated quotes + inferred reading; §5]
- **Exits are silent.** Grid computing (2001–2002), computational economics (2004–2007), HPC/exascale and network epidemics (2012–2016) and nonconvex "branch-and-refine" (2008–2009) leave no later papers in the records checked, and I found no statement of why. [inferred from absence]
- **The last 12 months** (10 Oct 2025 to 10 Oct 2026) [practice · primary]:
  - no new arXiv preprint after 24 September 2025, and none on Optimization Online since September 2024;
  - seven dated outputs: five new papers (Math. Program., JOTA, Math. Program. Comput., COAP, ISBI), a published Correction and a CRAN package, plus the print issue of the 2025 McCormick paper;
  - arXiv revisions;
  - five new or updated GitHub repositories; three of the four new ones are run with an AI assistant (Claude);
  - hosting LANS seminars, including one on agentic AI (§7).
- **Seniority.** Senior computational mathematician by March 2013, "R&D Leader" by December 2022, deputy division director by March 2023, SIAM President 2023–2024, Argonne Distinguished Fellow (announced 15 December 2023). [stated/observed · primary]

---

## 1. Lineage

### 1.1 Upward: academic ancestry

| Generation | Person | Degree | Source | Tag |
|---|---|---|---|---|
| Advisor's advisor | Colin M. Reeves | (Fletcher's "Advisor 1") | MGP id 52148 [T38] | [observed · secondary] |
| Advisor | Roger Fletcher (1939–2016) | Ph.D. University of Leeds 1963 | MGP id 52148 [T38]; dates in the Royal Society memoir title, DOI 10.1098/rsbm.2024.0037 (Crossref-checked; memoir not read by me) | [observed · secondary] |
| Leyffer | Sven Leyffer | Ph.D. University of Dundee, "Deterministic Methods for Mixed Integer Nonlinear Programming". Title page: "December 1993" [T10 p. 1]. MGP: 1994, title "Deterministic Methods in Mixed Integer Nonlinear Programming", "Advisor 1: Roger Fletcher" [T38] | T10, T38 | [practice · primary] / [observed · secondary] |

- Fletcher's other MGP-listed students are Robert Womersley (1981), Mehiddin Al-Baali (1984), Chengxian Xu (1987) and Julian Hall (1992). MGP counts "5 students and 23 descendants" for Fletcher [T38]. MGP undercounts Dundee students, so this is a floor. [observed · secondary; that it is a floor is inferred, because the 2017 article cites the Dundee thesis of C. Zoppke-Donaldson, ref. [43], who is not in the list]
- Before Dundee: "Born in Hamburg, Germany" [T04, stated · primary]. A Vordiplom in Pure and Applied Mathematics from the University of Hamburg in 1989 appears only on Wikipedia, which cites no source for it [T39, observed · secondary, unverified].
- **What the advisor's group handed over, in its own words.**
  - The thesis runs on Fletcher's QP code: "The LP and QP solver that underlies this thesis is an implementation of a primal ASM with the additional feature of handling degeneracy." [T10 p. 23, practice · primary]
  - It solves the NLPs with a packaged library: "All code is written in FORTRAN 77 and uses the NAG library routine E04UCF [55] to solve the NLP problems." [T10 p. 77, practice · primary]
  - The filter line began with the advisor: "Roger Fletcher had been unhappy with the performance of classical penalty functions for NLP, and had been playing around with methods that instead use the Lagrangian as a merit function within a tolerance tube around the constraints [43], similar to the funnel ideas [24] developed later by Nick Gould and Philippe Toint. Our filter method [17] grew out of these early experiments." [T09 pp. 3–4, stated · primary]
- **How he frames the whole career:** "Throughout my career, I had the great fortune to work with some of the brightest optimizers, and this article is a tribute to their influence, guidance, and inspiration." [T09 p. 3, stated · primary]

### 1.2 Downward: students and juniors

- **Formal record.** MGP lists "No students known." [T38, observed · secondary]. He has worked at a national laboratory since 2002 and held a Northwestern adjunct professorship in 2006–2012 [T05]. I found no PhD student formally supervised by him (see note 04 for the fuller search).
- **Practice record.** Juniors reach him through the laboratory. His homepage has carried "Student and Postdoc Opportunities: Givens Associates" (captures 2016–2026) [T03, practice · primary]. His 2026 QuantumOpt26 write-up, coauthored with David Linnet, proposes "a short (six-week) student project" (`docs/project.tex`) [T14, practice · primary]. Juniors who coauthored with him (affiliations as printed on the papers I read in this run; current posts mostly not checked):

| Junior | Joint line with Leyffer | Affiliation evidence (this run) | Tag |
|---|---|---|---|
| Kumar Abhishek | FilMINT (preprint 2006 per note 01, not re-checked; INFORMS J. Comput. 2010, DOI 10.1287/ijoc.1090.0373) | "a student of Jeff Linderoth's" [T09 p. 5]. By 2010: "Enterprise Optimization, United Airlines" (Crossref affiliation of the 2010 paper) [T18] | [stated + practice · primary] |
| Ashutosh Mahajan | Minotaur ("developed by Ashutosh Mahajan at Argonne together with Jeff Linderoth, Jim Luedtke, and Todd Munson") | T09 p. 6; current post not re-checked here (note 04 gives IIT Bombay) | [stated · primary] |
| Chungen Shen | nonmonotone filter, COAP 52(3) (2012) 583–607, DOI 10.1007/s10589-011-9430-2, COAP Best Paper award | T32, T18 | [practice · primary] |
| Charlie Vanaret | augmented-Lagrangian filter (2020); Uno (2018–2026); funnel SQP (2024–2026) | arXiv 2406.13454v2 p. 1: Argonne MCS and "Department of Mathematical Optimization, Zuse-Institut Berlin" [T17] | [practice · primary] |
| Paul Manns | sum-up rounding (2021), SLIP (2022), McCormick envelopes (2024–2026) | arXiv 2406.07891v5 p. 1: "Faculty of Mathematics, TU Dortmund University" [T17] | [practice · primary] |
| Dominic Yang | neural-network surrogates (2021–2022), TV-regularized integer programs (2025), ADMM for topology optimization (2025–2026) | arXiv 2509.19888v2 p. 1: Argonne [T17] | [practice · primary] |
| External PhD students and early-career researchers who carry a line with him | David Kiessling (funnel SQP; "KU Leuven"), Armin Nurkanović (MPEC B-stationarity; "University of Freiburg"), Harsh Choudhary (ADMM topology optimization; "Czech Technical University in Prague") | first pages of arXiv 2409.09208v1, 2501.13835v5, 2509.19888v2 [T17] | [practice · primary]; whether he co-supervised any of them is not documented |

- [inferred] The lineage is carried by software and lines of work more than by degrees. Mahajan carried Minotaur, Vanaret carries Uno, and Manns carries the MIPDECO analysis. In the 2025–2026 MPEC paper, Nurkanović "thanks Anton Pozharskiy for translating MacMPEC to CasADi" [T17, arXiv 2501.13835v5 acknowledgments], so the test library Leyffer built in 2000 still serves his newest coauthors.
- [practice · primary; the link is inferred] Nurkanović appears in the programme of the MINOA Doctoral School (online, 21–29 June 2021) as giving an industrial presentation "from Siemens", in the same Part I in which Leyffer lectured [T34]. That this is where the 2025 collaboration began is a possibility, not a documented fact.

---

## 2. Dated timeline

Every paper carries an identifier checked in this run through Crossref, arXiv or DBLP [T17–T19]. "Report" items (Dundee NA and Argonne ANL/MCS-P series) are dated from the homepage lists that carry them [T01–T02] or from his own reference list [T09].

| When | Event | Evidence | Tag |
|---|---|---|---|
| — | Born in Hamburg, Germany | Bio page [T04] | [stated · primary] |
| 1989 | Vordiplom, University of Hamburg | Wikipedia only [T39] | [observed · secondary, unverified] |
| Dec 1993 / 1994 | PhD thesis, Dundee (title page "December 1993"); degree year 1994 per MGP, his Bio and Argonne | T10 p. 1; T38; T04; T23 | [practice · primary]; see Contradiction C1 |
| Aug 1994 | Fletcher & Leyffer, "Solving mixed integer nonlinear programs by outer approximation", Math. Program. 66(1–3) 327–349, DOI 10.1007/BF01581153 | T18 | [practice · primary] |
| 1994–2002 | Post-doctoral years in Dundee. Appointments page: "Research Fellow, Department of Mathematics, University of Dundee (1994-2002)". His Dundee homepage (versions of Feb 2001 and Feb 2002): "Position: Research Assistant" | T05; T01 | [stated · primary]; Contradiction C2 |
| May 1996 | "NLP filter methods were first proposed by Fletcher in a plenary talk at the SIAM Optimization Conference in Victoria in May 1996" | T12 p. 7 | [stated · primary, coauthored] |
| Sep 1997 | Report NA/171, Fletcher & Leyffer, "Nonlinear Programming without a penalty function", with "Detailed results of all 186 small nonlinearly constraint CUTE problems" | T01 | [practice · primary] |
| Dec 1997 | Report NA/178, "Generalized Outer Approximation" (later an Encyclopedia of Optimization entry, DOI 10.1007/978-0-387-74759-0_211, 2nd ed. 2008) | T01; T18 | [practice · primary] |
| Apr 1998 | Report NA/181, "User manual for filterSQP" | T01 | [practice · primary] |
| May 1998 | Fletcher & Leyffer, "Numerical Experience with Lower Bounds for MIQP Branch-And-Bound", SIAM J. Optim. 8(2) 604–616, DOI 10.1137/S1052623494268455 | T18 | [practice · primary] |
| Aug 1998 | Report NA/182, "Integrating SQP and branch-and-bound for Mixed Integer Nonlinear Programming" (6 Aug 1998; "Support by the EPSRC under grant number GR/K51204 is gratefully acknowledged."); NA/183, SLP-filter convergence with Toint | T11 p. 1; T01 | [practice · primary] |
| Nov 1998 | Skrifvars, Leyffer, Westerlund, Comput. Chem. Eng. 22(12) 1829–1835, DOI 10.1016/S0098-1354(98)00238-5 (MINLP algorithms compared on a chemical-engineering estimation problem) | T18 | [practice · primary] |
| 1999 | NA/188 (Jan), Grothey, Leyffer, McKinnon, "A note on feasibility in Benders Decomposition"; NA/195 (Dec), Fletcher & Leyffer, "A bundle filter method for nonsmooth nonlinear optimization" | T01 | [practice · primary] |
| by Apr 2001 | Dundee homepage lists research interests in this order: "Mathematical Programs with Equilibrium Constraints", "Large Scale Nonlinear Programming", "Mixed Integer Nonlinear Programming", "Branch-and-bound for Mixed Integer Quadratic Programming". Test libraries: MINLP and MacMPEC | T01 (capture 4 Apr 2001; page last modified 20 Feb 2001) | [stated · primary] |
| Mar 2001 | Leyffer, COAP 18(3) 295–309, DOI 10.1023/A:1011241421041 (journal version of NA/182) | T18 | [practice · primary] |
| May 2001 → Sep 2002 | NA/200, Goux & Leyffer, grid computing → "Solving Large MINLPs on Computational Grids", Optim. Eng. 3(3) 327–346, DOI 10.1023/A:1021047328089 | T02; T18 | [practice · primary] |
| Jan 2002 | The filter papers in print: Math. Program. 91(2) 239–269, DOI 10.1007/s101070100244; SIAM J. Optim. 13(1) 44–59, DOI 10.1137/S105262340038081X; SIAM J. Optim. 13(3) 635–659, DOI 10.1137/S1052623499357258 | T18 | [practice · primary] |
| Feb–Aug 2002 | NA/208 "The Penalty Interior Point Method fails to converge for Mathematical Programs with Equilibrium Constraints" (Feb); NA/209 local SQP convergence for MPECs with Ralph and Scholtes (May); NA/210 "Numerical experience with solving MPECs as NLPs" (Aug) | T02 | [practice · primary] |
| 2002 | Joins Argonne MCS: "he joined the MCS division at Argonne in 2002" (Argonne). The Dundee page captured on 28 Nov 2002 reads "This page has moved to my new location at Argonne." | T23; T25; T01 | [observed + practice · primary] |
| Sep 2003 | Co-chair, Global Optimization Theory Institute, Argonne, 8–10 Sep 2003 | T05 | [stated · primary] |
| 2004–2006 | Fletcher & Leyffer, MPCCs as NLPs, Optim. Methods Softw. 19(1) 15–40 (2004), DOI 10.1080/10556780410001654241; Leyffer, "The penalty interior-point method fails to converge", Optim. Methods Softw. 20(4–5) 559–568 (2005), DOI 10.1080/10556780500140078; Leyffer, López-Calva, Nocedal, SIAM J. Optim. 17(1) 52–77 (2006), DOI 10.1137/040621065; Fletcher, Leyffer, Ralph, Scholtes, SIAM J. Optim. 17(1) 259–286 (2006), DOI 10.1137/S1052623402407382; Chen, Hobbs, Leyffer, Munson, electricity and NOx allowance markets, Comput. Manag. Sci. 3(4) 307–330 (2006), DOI 10.1007/s10287-006-0020-1 | T18 | [practice · primary] |
| 2004–2010 | Fellow of the Computation Institute (Senior Fellow from 2010); SIAM Activity Group on Optimization programme director 2004–2007; INFORMS Optimization Society vice-chair for NLP 2004–2006 | T05 | [stated · primary] |
| Aug 2005 | Homepage: "I am a computer scientist in the Mathematics and Computer Science Division at Argonne National Laboratory." | T02 (page "Last updated on 08/19/05") | [stated · primary] |
| 2005–2007 | Co-chair, Institute on Computational Economics (Chicago and Argonne) | T05 | [stated · primary] |
| 2006 | Lagrange Prize in Continuous Optimization with Fletcher and Toint (committee: M. Todd, chair; J. Dennis; N. Gould; A. Lewis) | T29; T30 | [observed · primary] |
| 2006–2012 | Adjunct Professor, Department of Electrical Engineering & Computer Science, Northwestern University | T05 | [stated · primary] |
| Sep–Oct 2006 | "A Brief History of Filter Methods", ANL/MCS-P1372-0906 (with Fletcher, Toint) | T12 | [practice · primary] |
| Mar 2008 | Homepage: "I am a computational mathematician in the Mathematics and Computer Science Division at Argonne National Laboratory." | T02 (page "Last updated on March 6, 2008") | [stated · primary] |
| 2008 | Co-chair, SIAM Conference on Optimization (Boston, 10–13 May 2008); co-chair, IMA Hot Topics Workshop "Mixed-Integer Nonlinear Optimization" (17–21 Nov 2008); Editor-in-Chief, Math. Methods Oper. Res. (2008–2014) | T05 | [stated · primary] |
| Dec 2008 | Research page states the base-and-extension programme (quoted in §3) | T02 research.htm (capture 2 Dec 2008) | [stated · primary] |
| 10 Mar 2009 | Georgia Tech seminar "A Tale of Two Problems: Integer and Nonlinear Optimization" (FilMINT; "a new method, branch-and-refine") | T31 | [stated · primary] |
| 18 May 2009 | SIAM Fellow, first class: "For contributions to large-scale nonlinear optimization." | T27; T24 | [observed · primary] |
| Jul 2009 | Leyffer, Linderoth, Luedtke, Miller, Munson, "Applications and algorithms for mixed integer nonlinear programming", J. Phys. Conf. Ser. 180 012014, DOI 10.1088/1742-6596/180/1/012014 | T18; T37 | [practice · primary] |
| 2009 | Cluster chair for nonlinear mixed-integer programming, ISMP 2009 | T05 | [stated · primary] |
| 2010–2013 | SIAM Vice President for Programs | T05; T04 | [stated · primary] |
| Nov 2010 | FilMINT, INFORMS J. Comput. 22(4) 555–567, DOI 10.1287/ijoc.1090.0373 | T18 | [practice · primary] |
| 2011–2017 | Co-editor, Mathematical Programming A | T05 | [stated · primary] |
| Oct 2011 / 2012 | Shen, Leyffer, Fletcher, "A nonmonotone filter method for nonlinear optimization", COAP 52(3) 583–607, DOI 10.1007/s10589-011-9430-2; listed on the COAP Best Paper Awards page; his Bio: "In 2013, Sven won the 2012 COAP Best Paper Prize" | T18; T32; T04 | [observed + stated · primary] |
| 2012 | Lee & Leyffer (eds.), Mixed Integer Nonlinear Programming, IMA Vol. 154, DOI 10.1007/978-1-4614-1927-3 | T18 | [practice · primary] |
| Nov 2012 | Alexeev, Mahajan, Leyffer, Fletcher, Fedorov, load balancing for the fragment molecular orbital method, SC 2012, DOI 10.1109/SC.2012.62 | T18 | [practice · primary] |
| Jan 2012 → Mar 2013 | Homepage title changes from "computational mathematician" (edit of 23 Jan 2012) to "senior computational mathematician" (edit of 4 Mar 2013) | T03 | [stated · primary] |
| Apr 2013 | Belotti, Kirches, Leyffer, Linderoth, Luedtke, Mahajan, "Mixed-integer nonlinear optimization", Acta Numerica 22 1–131, DOI 10.1017/S0962492913000032; Kirches & Leyffer, "TACO: a toolkit for AMPL control optimization", Math. Program. Comput. 5(3) 227–265, DOI 10.1007/s12532-013-0054-7 | T18 | [practice · primary] |
| Jul 2013 | Leyffer & Safro, "Fast response to infection spread and cyber attacks on large-scale networks", J. Complex Networks 1(2) 183–199, DOI 10.1093/comnet/cnt009 | T18 | [practice · primary] |
| 2013 | Graduate course on MINLP, Graduate School in Systems, Optimization, Control and Networks (Louvain) | T06 | [stated · primary] |
| Mar 2014 | Snir et al., "Addressing failures in exascale computing", IJHPCA 28(2) 129–173, DOI 10.1177/1094342014522573 | T18 | [practice · primary] |
| 2015–2022 | Secretary of ICIAM | T05; T04 | [stated · primary] |
| Nov 2015 | Leyffer, Cay, Kouri, van Bloemen Waanders, "Mixed-integer pde-constrained optimization", ANL/MCS-P5429-1015 | his reference [31] in T09 | [stated · primary] |
| 2016 | INFORMS Optimization Society Farkas Prize (committee: Sofer, chair; Grossmann; Ralphs; Shapiro); GIAN course "Optimization: Applications, Algorithms, and Computation" at Jabalpur Engineering College (year from the brochure's file name) | T28; T06 | [observed + stated · primary] |
| Oct 2016 | Leyffer, Wild, Fagan, Snir, Palem, Yoshii, Finkel, "Doing Moore with Less -- Leapfrogging Moore's Law with Inexactness for Supercomputing", arXiv 1610.02606 | T17 | [practice · primary] |
| Nov 2016 | Leyffer, "Augmented Lagrangian filter method", ANL/MCS-P6082-1116 | his reference [30] in T09 | [stated · primary] |
| Oct 2017 | Retrospective "Nonlinear Optimization and Beyond", INFORMS OS Today 7(2) 3–10 | T09 | [stated · primary] |
| 2018–2021 | Editor-in-Chief, Mathematical Programming B (his Appointments page; Wikipedia says 2017–2021) | T05; T39 | Contradiction C5 |
| Sep 2018 | Summer school "Optimization of Dynamical Systems", Bremen, 3–7 Sep 2018 | T06 | [stated · primary] |
| 15–17 Oct 2018 | Ten commits authored "leyffer" in the code base that became Uno, among them "Sven's attempt at writing C++ code", "changes on f77", "augLag version hs015.mod" and "Merge branch 'master' of gitlab.com:argonot/argonot" | T15 | [practice · primary] |
| 28 Nov 2018 | LANS seminar "Optimization for Machine Learning" | T22 | [stated · primary] |
| Mar 2019 | Larson, Leyffer, Palkar, Wild, arXiv 1903.11366 → J. Glob. Optim. 80(2) 439–477 (2021), DOI 10.1007/s10898-020-00978-w | T17; T18 | [practice · primary] |
| 11 Dec 2019 | LANS seminar "Mixed-Integer PDE-Constrained Optimization" | T22 | [stated · primary] |
| 2020 | Leyffer & Vanaret, "An augmented Lagrangian filter method", Math. Methods Oper. Res. 92(2) 343–376, DOI 10.1007/s00186-020-00713-x; Leyffer, Menickelly, Munson, Vanaret, Wild, "A survey of nonlinear robust optimization", INFOR 58(2) 342–373, DOI 10.1080/03155986.2020.1730676 | T18 | [practice · primary] |
| Nov 2020 / Jun 2021 | Minotaur, Math. Program. Comput. 13(2) 301–338, DOI 10.1007/s12532-020-00196-1 | T18 | [practice · primary] |
| Feb–Mar 2021 | MIPDECO in print: Leyffer, Manns, Winckler, COAP 79(1) 193–221, DOI 10.1007/s10589-020-00262-3; Gnegel, Fügenschuh, Hagel, Leyffer, Stiemer, Math. Program. 188(2) 695–728, DOI 10.1007/s10107-021-01626-1. ML and OED preprints: arXiv 2101.05958, 2102.08351 | T18; T17 | [practice · primary] |
| 21–29 Jun 2021 | Lecturer, MINOA Doctoral School (online), Part I "Nonlinear Optimal Control Problems: Methods and Applications"; his Lectures page lists "MINOA Summer School: Mixed-Integer PDE-Constrained Optimization" | T34; T06 | [practice + stated · primary] |
| 13 Sep 2021 | Homepage research statement re-edited: the extension list now names design of experiments, machine learning and quantum computing (§3) | T03 | [stated · primary] |
| 29 Sep 2021 | GitHub repository cvanaret/Uno created (MIT licence) | T15 | [practice · primary] |
| 2021 | "Chair, SIAM Climate Task Force (2021)" | T05 | [stated · primary] |
| 3 Nov 2021 | Virtual talk in the Computing Research Leadership Council (CRLC) seminar series, advertised by the UC Merced SIAM Student Chapter (flyer) and the Charles University SIAM chapter. The flyer promises questions about "his nearly twenty years of professional experiences in a National Laboratory" | T36 | [observed · primary] |
| 30 Nov 2021 | Elected SIAM president-elect; to "serve as president from January 1, 2023, to December 31, 2024" | T23 | [observed · primary] |
| 2022 | Vogt, Leyffer, Munson, SIAM J. Sci. Comput. 44(1) B29–B50, DOI 10.1137/20M1315993; Kirches, Larson, Leyffer, Manns, SIAM J. Optim. 32(1) 75–99, DOI 10.1137/20M1370501; Leyffer & Manns, ESAIM COCV 28 66, DOI 10.1051/cocv/2022059; Attia, Leyffer, Munson, SIAM J. Sci. Comput. 44(2) B395–B427, DOI 10.1137/21M1404363; Yang, Balaprakash, Leyffer, COAP 83(3) 759–800, DOI 10.1007/s10589-022-00404-9 | T18 | [practice · primary] |
| 6 Jul 2022 | Leyffer & Mahajan (Salil), "Improving Earth System Predictability with Artificial Intelligence", SIAM News 55(6) | T33 | [stated · primary, coauthored] |
| Dec 2022 | Argonne profile title "Senior Computational Mathematician / R&D Leader" | T25 (capture 7 Dec 2022) | [observed · primary] |
| Jan 2023 | Fei, Brady, Larson, Leyffer, Shen, "Binary Control Pulse Optimization for Quantum Systems", Quantum 7 892, DOI 10.22331/q-2023-01-04-892 | T18 | [practice · primary] |
| 2023–2024 | SIAM President | T23; T05 | [observed + stated · primary]; Contradiction C4 |
| by Mar 2023 | Deputy division director: homepage edit of 10 Mar 2023; Argonne profile capture of 26 Mar 2023 | T03; T25 | [stated + observed · primary] |
| Nov 2023 | Kim, Leyffer, Balaprakash, symbolic regression, INFORMS J. Comput. 35(6) 1383–1403, DOI 10.1287/ijoc.2022.0050 | T18 | [practice · primary] |
| 15 Dec 2023 | Named an Argonne Distinguished Fellow (2023 class of five; "about three percent" of research staff) | T26 | [observed · primary] |
| Jan 2024 | GIAN course "Mixed-Integer Nonlinear Optimization" at IIT Bombay (lectures on YouTube) | T06 | [stated · primary] |
| 14 Jan 2024 | Three empty GitHub repositories created: "MINLO-book", "MINLO-book1", "MINLPbook" | T14 | [practice · primary]; purpose not documented |
| Jun–Sep 2024 | arXiv: McCormick envelopes (2406.07891, 12 Jun); Uno (2406.13454, 19 Jun); funnel SQP (2409.09208, 13 Sep) | T17 | [practice · primary] |
| 3 Jul 2024 | XSCOPE/LANS seminar "Solving Inverse Problems at the Advanced Photon Source by Machine Learning and Optimization" | T22 | [stated · primary] |
| 6 Jan 2025 | McCormick paper online, Math. Program. 218(1–2) 245–290 (print July 2026), DOI 10.1007/s10107-024-02181-1 | T18 | [practice · primary] |
| Jan–May 2025 | arXiv 2501.13835 with Nurkanović (23 Jan); quantum-control papers in INFORMS J. Comput. 37(1) 86–106, DOI 10.1287/ijoc.2024.0560, and ACM Trans. Quantum Comput. 6(1), DOI 10.1145/3670416; Vogt, Leyffer, Munson, COAP 90(2) 337–360, DOI 10.1007/s10589-024-00644-x; Attia, Leyffer, Munson, SIAM/ASA J. Uncertain. Quantif. 13(2) 744–774, DOI 10.1137/24M1667543 | T17; T18 | [practice · primary] |
| 2 May 2025 | Meet-and-greet with the ASU SIAM Student Chapter ("career path, experience leading SIAM") | T35 | [observed · primary] |
| 25–30 May 2025 | BQPD_jll.jl 1.0.0, a Julia package of Fletcher's QP solver, created with Alexis Montoison | T14 | [practice · primary] |
| 3 Jul 2025 | LANS blackboard talk "Raiders of the lost penalty function" | T22 | [stated · primary] |
| Aug–Sep 2025 | arXiv 2508.05822 (7 Aug), 2509.01869 (2 Sep), 2509.15961 (19 Sep), 2509.19888 (24 Sep), the last new submissions found | T17 | [practice · primary] |
| Sep 2025 | Contributor, DOE report "Basic Research Needs for Inverse Methods for Complex Systems under Uncertainty", DOI 10.2172/2583339 (Crossref record created 23 Dec 2025) | T18 | [practice · primary]; his role not read |
| 22 Oct 2025 → Oct 2026 | The last 12 months: see §7 | T14–T22 | — |

---

## 3. How he has described his own agenda over time

His homepages survive in the Wayback Machine from 2001 onward. They give a dated record of his stated agenda, written in the first person, that is independent of any publication count. Third-person institutional bios are listed separately; they were most likely supplied by him, but that is not documented.

| Date (page edit or capture) | Verbatim self-description | Source | Tag |
|---|---|---|---|
| Feb 2001 (Dundee) | "Position: Research Assistant"; research interests listed in the order MPECs, large-scale NLP, MINLP, "Branch-and-bound for Mixed Integer Quadratic Programming" | T01 | [stated · primary] |
| Aug 2005 (Argonne) | "I am a computer scientist in the Mathematics and Computer Science Division at Argonne National Laboratory. I am interested in numerical optimization, and enjoy hill-walking." | T02 | [stated · primary] |
| Mar 2008 | "I am a computational mathematician in the Mathematics and Computer Science Division at Argonne National Laboratory. I am interested in numerical optimization, and enjoy hill-walking." | T02 | [stated · primary] |
| Dec 2008 (research page) through 10 Nov 2019 (wiki homepage; still live in the capture of 21 May 2021) | "I am interested in the development of reliable methods for solving large-scale nonlinear optimization problems and in the implementation and analysis of filter type algorithms. This forms the basis from which I am extending nonlinear optimization methodologies to emerging areas such as mixed-integer nonlinear optimization and optimization problems with complementarity constraints." | T02 research.htm; T03 (edits of 19 Mar 2009, 23 Jan 2012, 4 Mar 2013, 18 Dec 2015, 9 Sep 2019, 10 Nov 2019); T07 | [stated · primary] |
| 10 Mar 2009 (Georgia Tech bio, third person) and 18 May 2009 (Argonne news) | Georgia Tech repeats the two sentences in the third person: "This forms the basis from which he is extending nonlinear optimization methodologies to emerging areas such as mixed-integer nonlinear optimization and optimization problems with complementarity constraints." Argonne: "Leyffer is developing and applying nonlinear optimization methodologies to emerging areas such as mixed-integer nonlinear optimization and optimization problems with complementarity constraints." It gives as an example "seeing how electricity producers maximize profit in a deregulated market while exploiting government- allocated NOx permits to drive up costs of their competitors." | T31; T24 | [stated/observed · primary] |
| 4 Mar 2013 | "I am a senior computational mathematician and part of the Laboratory for Advanced Numerical Simulations (LANS) …" | T03 | [stated · primary] |
| 13 Sep 2021 (edit; first captured 29 Nov 2021) | "This forms the basis from which I am extending nonlinear optimization methodologies to other areas such as design-of-experiments, machine learning, quantum computing, and mixed-integer nonlinear optimization." | T03 | [stated · primary] |
| 30 Nov 2021 (quoted in Argonne news) | "SIAM provides a critical bridge between academia and industry, and this is an exciting time for the community as we delve into new areas such as machine learning where optimization may have a decisive impact." | T23 | [stated · primary] |
| 10 Mar 2023 (edit; still the live text in the capture of 18 Sep 2026) | "I am a senior computational mathematician and deputy division director in the Mathematics and Computer Science Division at Argonne National Laboratory." Research statement unchanged from 2021 | T03 | [stated · primary] |
| 15 Dec 2023 (Argonne, third person) | "His research interests include developing reliable methods for solving large-scale nonlinear optimization problems in applications including experimental design, resilience of the power grid and inverse problems arising at the APS. He is extending nonlinear optimization methodologies to emerging areas, such as discrete optimization for topology design and optimization problems involving digital twins." | T26 | [observed · primary] |
| capture 30 Nov 2025 (Argonne profile, third person) | "Extending nonlinear optimization methodologies to emerging areas such as mixed-integer nonlinear optimization, optimization problems with PDE constraints, and optimization problems with complementarity constraints" | T25 | [observed · primary] |
| 15 Jul 2026 (project brief in his own repository) | "Novelty: Derivative-free or simulation-based optimization is a well-studied area. However, most solvers assume that the constraints $c(x)$ are either absent or simple (e.g. bounds, or affine)." | T14 (conDFO `CLAUDE.md`) | [stated · primary] |

What the series shows:

- [inferred from the series] The base clause (reliable large-scale NLP methods plus filter algorithms) is constant for nearly 18 years in the first-person record (Dec 2008 to the capture of Sep 2026). The extension clause is where turns become visible.
- [inferred] The 2021 edit is the only documented re-statement. It drops complementarity from the homepage list, adds design of experiments, machine learning and quantum computing, and moves MINLP from first to last place. It came after two of the turns it names and before the third:
  - the "Optimization for Machine Learning" talk (Nov 2018) and the OED preprint (Jan 2021) came before it;
  - his first quantum-control preprint (Apr 2022) came after it.

  So the statement trails some turns and announces others. The third-person bios of 2023 and 2025 disagree with the 2021 list (Contradiction C7).
- [inferred] The job title tracks seniority, not research content: "computer scientist" (2005) → "computational mathematician" (2008) → "senior computational mathematician" (2013) → "deputy division director" (2023).

---

## 4. The turns: what changed, what triggered it, and when he entered and left

Each turn lists its window, the evidence for its trigger and for its timing relative to the field, and how it ended. "Trigger type" uses the framework's categories: new tool, new data or problem, failure, move, plus two I needed in addition, collaborator and institution/programme.

### Turn A · into deterministic MINLP from the NLP side (about 1990–1994)

- **What.**
  - Thesis on deterministic MINLP methods (Dec 1993).
  - Outer approximation generalized "by treating nonlinearities in the integer variables directly" (1994 abstract, DOI 10.1007/BF01581153, read on the publisher page, T41).
  - Mature NLP machinery carried into MINLP. The same abstract considers an approach "in which exact penalty functions are used to solve the NLP subproblems" and develops theory "for a large class of nonsmooth MINLPs based on the use of convex composite functions and subdifferentials" (T41). The thesis has a section "Penalty Functions and their Optimality Conditions" (T10 contents) and runs on Fletcher's QP solver.

  [practice · primary]
- **Trigger.** Not documented: who chose the topic is not stated anywhere I read. [gap]
- **Timing.** [stated · primary] "Since the size of MINLP problems that is manageable is rather small, ASMs are used in this thesis." (T10 p. 23, 1993). [inferred] He entered while MINLP was a small-scale field whose base algorithm came from chemical engineering (Duran and Grossmann 1986, DOI 10.1007/BF02592064; Quesada and Grossmann 1992, DOI 10.1016/0098-1354(92)80028-8; both Crossref-checked), and he came to it from the numerical-analysis side.
- **A failure that steered the work.** [stated · primary] "A worst case example, in which linear outer approximation visits all integer assignments is derived that motivates the introduction of a second order term into the MILP master program relaxations." (T10 p. 59). In his conclusion: "The derivation of the MILP master program has been simplified and inaccuracies concerning the treatment of infeasible subproblems have been corrected." (T10 p. 104)
- **Era.** Fortran 77, the NAG routine E04UCF for the NLPs (T10 p. 77), Fletcher's QP code (T10 p. 23).

### Turn B · a side question becomes a line: MIQP branch-and-bound (thesis 1993 → journal 1998)

- **Trigger: an artefact of his own method.** [stated · primary] "The introduction of MIQP master programs in Chapter 5 caused me to become interested in MIQP problems and a detailed study of branch-and-bound for MIQP problems is given." (T10 p. 16). Elsewhere: "MIQP problems are not only interesting as master problems in the aforementioned algorithms but also in their own right" (T10 p. 27).
- **Outcome.** Fletcher & Leyffer, SIAM J. Optim. 8(2) (1998), DOI 10.1137/S1052623494268455; the MIQP line is still on his 2001 research-interest list (T01). [practice · primary]
- **Also stated in the thesis**, and relevant to his later portfolio-style software: "This shows that no one solver outperforms all other solvers on all problems. However, the test problems can be grouped into classes of problems and a "rule of thumb" is motivated which indicates which solver is likely to perform best for each class of problem." (T10 p. 16). [stated · primary]

### Turn C · filter methods with Fletcher (1996–2002), the line that defines his base

- **Trigger: the advisor's dissatisfaction plus an empirical observation.** [stated · primary]
  - "Roger Fletcher had been unhappy with the performance of classical penalty functions for NLP … Our filter method [17] grew out of these early experiments." (T09 pp. 3–4)
  - "NLP filter methods were first proposed by Fletcher in a plenary talk at the SIAM Optimization Conference in Victoria in May 1996" (T12 p. 7)
  - The observation behind it: "Yet we have noticed that the unmodified SQP method is able to quickly solve a large proportion of test problems without the need for modifications to induce global convergence." (T12 p. 4)
  - [observed · primary] Fletcher: "Discovering the filter idea was a real "eureka" moment for me" (T30). The idea is Fletcher's by Fletcher's own account. Leyffer's share is the joint code (filterSQP manual, Apr 1998), the experiments and the convergence theory with Toint, Gould and Wächter (T01, T09 p. 4).
- **Timing: before any consensus, against the established tool.** [stated · primary] "Traditionally, penalty or merit functions have been used to enforce convergence from remote starting points." (T09 p. 3). Uptake was quick according to the prize committee: "This new approach to balancing feasibility and optimality has been quickly picked up by other researchers" (Lagrange Prize 2006, T29) [observed · primary].
- **Later stance.**
  - 2006: "We believe filter methods achieve this goal." (T12 p. 4)
  - 2006 prediction: "We believe that filter methods will continue to grow and find application in more diverse areas." (T12 p. 15)
  - 2017: "At this point, I do not believe that there exists a big difference between filter methods and modern penalty function methods, and the choice of method is really a question of personal preference." (T09 p. 5)

  He never left the line. Filter ideas reappear in the 2007 MPEC filter preprint (T09 ref. [29]), the 2012 nonmonotone filter, the 2016/2020 augmented-Lagrangian filter, the 2024–2026 funnel and filter-ADMM papers, and the 2026 conDFO project (§7). [stated + practice · primary]

### Turn D · own the solver, then redesign the algorithm around it: SQP inside branch-and-bound (1997–2001)

- **Trigger: a new tool, his own SQP code (filterSQP, manual Apr 1998).** [stated · primary] "In [1] two QP problems are solved before branching. This restriction is due to the fact that a packaged SQP solver is used. By using our own solver we are able to remove this unnecessary restriction, widening the scope for early branching." (T11 p. 2; "two" is italic in the original). He diagnoses the field's habit the same way: "Classical methods for the solution of (P) “decompose” the problem by separating the nonlinear part from the integer part. This approach is largely due to the existence of packaged software for solving Nonlinear Programming (NLP) and Mixed Integer Linear Programming (MILP) problems." (T11 p. 2)
- **The contrast with the thesis.** In 1993 he used a packaged NLP routine (NAG E04UCF, T10 p. 77). By 1998 owning the NLP code is what makes the new algorithm possible. [practice · primary; the link between the two is inferred]
- **Timing.** [stated · primary] The idea itself is credited to others: "This idea was first presented by Borchers and Mitchell [1]." (T11 p. 2). He enters as an improver with a better instrument.
- **Funding.** "Support by the EPSRC under grant number GR/K51204 is gratefully acknowledged." (T11 p. 1)

### Turn E · MPECs solved as NLPs, against the prevailing view (about 2000–2009)

- **What.** The MacMPEC test collection (2000, T09 ref. [27]). MPECs first on his Dundee research-interest list by Feb 2001 (T01). Then three Dundee reports, all in 2002 (T02):
  - NA/208, a counterexample to the penalty interior-point method;
  - NA/209, local SQP convergence;
  - NA/210, numerical experience.

  These led to the 2004–2006 journal papers and the electricity/NOx market application (§2), and then a sole-authored multiobjective-via-complementarity paper, INFORMS J. Comput. 21(2) (2009), DOI 10.1287/ijoc.1080.0290. [practice · primary]
- **Trigger: favourable numerical evidence from his own solver, against the consensus.** [stated · primary]
  - "Until recently, it had been assumed that these problems were too difficult for standard nonlinear solvers. However, as long as we take care with the problem formulation and the algorithm design, modern NLP solvers can tackle these problems." (T09 p. 7)
  - "As a consequence, solving MPECs via NLPs such as (3.9) has been commonly regarded as numerically unsafe. In contrast, our initial numerical experience with filterSQP was very positive [19], and we investigated the convergence of SQP methods applied to (3.9) together with Roger Fletcher, Danny Ralph, and Stefan Scholtes [20]." (T09 p. 7)
- **Timing.** He entered against the consensus [stated]. In his 2017 account the positive numerical experience came first and the convergence analysis followed. The report dates are closer than that: the local-convergence report NA/209 (May 2002) predates the numerical-experience report NA/210 (Aug 2002), although the MacMPEC test set already existed in 2000 (T02, T09). Kept as Contradiction C12.
- **Dormancy and return.** [inferred from the records]
  - I found no new MPEC algorithm paper between 2009 and 2020.
  - He returned with bilevel/MPEC methods (Kim, Leyffer, Munson 2020, note 01, not re-checked), a sequential linearization method for bound-constrained MPCCs (2022, DOI 10.1137/20M1370501) and the B-stationarity method with Nurkanović (arXiv 2501.13835 → COAP 2026, DOI 10.1007/s10589-026-00832-x). [practice · primary]
  - His 2017 outlook announces the return: "Software and solvers for MPECs are far less mature than NLP or MINLP. … To develop better solvers we need to build on our existing NLP solver infrastructure." (T09 p. 9) [stated · primary]

### Turn F · the move to Argonne (2002) and the computing side lines (2001–2016)

- **The move.** [observed + practice · primary] "he joined the MCS division at Argonne in 2002" (T23). The Dundee page reads "This page has moved to my new location at Argonne." (capture 28 Nov 2002, T01). In 2005 he describes himself as "a computer scientist" there (T02).
- **Trigger: not documented.** [gap]
  - [inferred, weak] Two Argonne links already appear in 2001. His Dundee page links the "Optimization Technology Center at Argonne National Laboratory and Northwestern University" and the NEOS Server (T01). His 2001 report with Goux studies MINLP on "computational grids" (NA/200 → Optim. Eng. 2002, DOI 10.1023/A:1021047328089).
  - The sequence of his postdoc posts is contradictory (C3).
- **Side lines that the new institution supplied, then dropped.** [practice · primary; the exits are inferred from absence]

| Line | Window | Identifiers | Later papers found? |
|---|---|---|---|
| Grid computing for MINLP | 2001–2002 | DOI 10.1023/A:1021047328089 | none |
| Computational economics (Institute on Computational Economics co-chair 2005–2007; NOx markets 2006; value-at-risk with Pang, arXiv math/0401063) | 2004–2007 | DOI 10.1007/s10287-006-0020-1; arXiv math/0401063 | none found after 2009 |
| Load balancing, exascale resilience, network epidemics | 2012–2014 | DOI 10.1109/SC.2012.62; DOI 10.1177/1094342014522573; DOI 10.1093/comnet/cnt009 | none |
| Inexact (reduced-precision) computing | 2016 | arXiv 1610.02606 | none |

  [inferred] These lines match Argonne's computing mission of their period: grids, exascale and energy-efficient computing. None became a sustained research programme, and none has a stated reason for ending.

### Turn G · MINLP as team science and consolidation (about 2006–2013)

- **What.** [practice · primary]
  - FilMINT (preprint 2006 per note 01, not re-checked; INFORMS J. Comput. 2010, DOI 10.1287/ijoc.1090.0373).
  - Co-chair of the IMA Hot Topics Workshop on MINLP (Nov 2008, T05).
  - Cluster chair at ISMP 2009 (T05).
  - SciDAC 2009 paper (DOI 10.1088/1742-6596/180/1/012014).
  - The edited IMA volume (2012, DOI 10.1007/978-1-4614-1927-3).
  - Acta Numerica survey (2013, DOI 10.1017/S0962492913000032).
  - Branching rules (ACM JEA 18, 2013, DOI 10.1145/2532568).
  - Minotaur (wiki page cited as 2011 in T09 ref. [33]; GitHub coin-or/minotaur created 1 Jun 2016, T16; paper 2020/21, DOI 10.1007/s12532-020-00196-1).
- **Trigger: collaborators from discrete optimization, a growing field and DOE funding.** [stated · primary]
  - "Over the last 10 years or so, I have been fortunate to collaborate with some very smart discrete optimizers. With a student of Jeff Linderoth's, we built FilMINT [1]" (T09 p. 5).
  - "Algorithmic advances over the last decade or so have often taken advantage of the special structure of problems, which motivated us to develop the Minotaur software framework [33]." (T09 p. 6).
  - The survey names the field's growth: "The past 20 years or so have seen a dramatic increase in new mixed-integer nonlinear models and applications, which has motivated the development of a broad range of new techniques to tackle this challenging class of problems." (T13 p. 11, coauthored).
  - The 2009 SciDAC paper (DOE's scientific-computing programme) closes on tractability: "These algorithmic advances are making increasingly larger instances of this important family of problems tractable." (T37, coauthored).
- **Timing.** [inferred] A re-entry in the role of consolidator: workshop, volume, 131-page survey, shared software. It came after the field had grown, as his own survey sentence says, not before it. Compare his 1993 remark that manageable MINLPs were "rather small" (Turn A).
- **A nonconvex branch that stopped.** [stated · primary] In March 2009 he presented "a new method, branch-and-refine that decomposes the nonlinear functions into one- and two- dimensional components for which piecewise linear envelopes are constructed using ideas similar to special ordered sets" (T31). A Crossref bibliographic query on 2026-10-10 found no journal article with that title and his name [practice · primary; a negative search, not proof of non-publication]. Its preprint (ANL/MCS-P1547-0908, note 01) was not read.

### Turn H · from mixed-integer optimal control to mixed-integer PDE-constrained optimization (2013 → now)

- **What.** [practice · primary]
  - TACO with Kirches (2013, DOI 10.1007/s12532-013-0054-7), and mixed-integer optimal control as a section of the 2013 survey.
  - MIPDECO preprint with Cay, Kouri and van Bloemen Waanders (ANL/MCS-P5429-1015, Nov 2015, T09 ref. [31]; coauthor affiliations not checked).
  - Journal papers 2021–2026: sum-up rounding, DOI 10.1007/s10589-020-00262-3; linear PDE-constrained MIP, DOI 10.1007/s10107-021-01626-1; cloaking, DOI 10.1137/20M1315993 and DOI 10.1007/s10589-024-00644-x; SLIP with TV regularization, DOI 10.1051/cocv/2022059; state elimination, DOI 10.1002/oca.2861; trust-region steepest descent, DOI 10.1007/s10107-021-01733-z and DOI 10.46298/jnsao-2023-10164; McCormick envelopes, DOI 10.1007/s10107-024-02181-1.
  - 2025–2026 preprints on topology optimization and TV-regularized integer programs: arXiv 2509.19888 and 2508.05822.
- **Trigger: collaborators and DOE applications [inferred from coauthors and application areas]. He names the class early [stated · primary]:**
  - 2017: "In addition, new classes of MINLPs are emerging, such as MIPs with second-order cone constraints [12, 11] and MINLPs with partial-differential equation constraints [31], which necessitate novel approaches." (T09 p. 7).
  - 2019 seminar: "This new class of problems, called mixed-integer PDE-constrained optimization (MIPDECO), must overcome the combinatorial challenge of integer decision variables combined with the numerical and computational complexity of PDE constrained optimization." and "We show how existing methods for solving mixed-integer optimization problems can be adapted to solve this new class of problems." (T22, 11 Dec 2019).
- **Timing: early.** [stated · primary] Even in 2024 the McCormick abstract can say that such relaxations "have not gained much attention in PDE-constrained optimization so far" (arXiv 2406.07891, T17). He also teaches the line at doctoral level, at the MINOA Doctoral School in June 2021 (T34, T06).
- **Era and team.** [practice · primary] The papers carry German coauthors and German funding: for example, Manns acknowledges DFG project 540198933, and computing time on the TU Dortmund cluster LiDO3 is credited (arXiv 2406.07891v5 acknowledgments, T17). Most papers in this line have a junior first author (note 01 authorship analysis, not re-checked).
- **Status.** Active. The 2026 Correction of the McCormick paper is the one published correction found in this run (§6).

### Turn I · applications pulled in by the laboratory: machine learning, design of experiments, inverse problems, quantum control (2018 → now)

- **What.** [practice · primary]
  - 2018 review seminar "Optimization for Machine Learning" (T22).
  - Tomography and sensing (arXiv 1902.02027).
  - Black-box integer optimization (DOI 10.1007/s10898-020-00978-w).
  - Optimal experimental design (DOI 10.1137/21M1404363; DOI 10.1137/24M1667543; arXiv 2509.15961).
  - Symbolic regression (DOI 10.1287/ijoc.2022.0050).
  - Neural-network surrogates (DOI 10.1007/s10589-022-00404-9).
  - Imbalanced classification (arXiv 2410.11171; IJCNN 2025, DOI 10.1109/IJCNN64981.2025.11227944; arXiv 2506.11315).
  - Quantum control (DOI 10.22331/q-2023-01-04-892; DOI 10.1287/ijoc.2024.0560; DOI 10.1145/3670416).
  - APS microscopy paths (ISBI 2026, DOI 10.1109/ISBI61048.2026.11515614).
- **Trigger: the laboratory's facilities and programmes plus junior collaborators.**
  - [stated · primary] 2018: "We review optimization methods that underpin machine-learning approaches. Our goal is to provide an overview of the connections between optimization and machine learning." The same abstract says: "Our goal is to highlight both the limitations and promises of optimization methodologies and formulations." (T22)
  - [stated · primary] 2021: "this is an exciting time for the community as we delve into new areas such as machine learning where optimization may have a decisive impact." (T23)
  - [stated · primary, coauthored] 2022, on DOE's AI4ESP workshops: "AI/ML models—while likely incapable of replacing years of climate model research—can help integrate more small-scale phenomena into existing models." (T33)
  - [stated · primary] 2024: "I will review some recent approaches to solving inverse problems arising at the Advanced Photon Source (APS). These approaches combine traditional optimization techniques for inverse problems with machine-learning (ML) techniques for faster reconstruction." (T22)
  - [observed · primary] The 2023 Distinguished Fellow citation lists "experimental design, resilience of the power grid and inverse problems arising at the APS" (T26).
- **Timing: after the wave, with his own formulations.** [inferred] He entered machine learning after it was already a mass movement, by a 2018 review talk and 2021 papers. He did not bring new learning algorithms. He recast ML objects into his home classes: "two alternative formulations of these problems in the specific case of feedforward neural networks with ReLU activation: as a mixed-integer optimization problem and as a mathematical program with complementarity constraints" (arXiv 2111.10489 abstract, T17) [stated · primary, coauthored]. In the same way, the quantum-control work uses total-variation regularization, ADMM, rounding and a trust-region method, the toolkit of his MIOC/MIPDECO line (arXiv 2204.05773 abstract, T17) [stated · primary, coauthored].
- **Status.** Active through 2026 (ISBI 2026; experimental-design and imbalance preprints of 2025).

### Turn J · back to the base: NLP-solver architecture, and penalty functions revisited (2016 → now)

- **What.** [practice · primary]
  - Augmented-Lagrangian filter: a sole-authored report in Nov 2016 (T09 ref. [30]), then with Vanaret in 2020 (DOI 10.1007/s00186-020-00713-x).
  - His own commits in the code base that became Uno, 15–17 Oct 2018, including "Sven's attempt at writing C++ code" (T15).
  - The Uno repository (created 29 Sep 2021; MIT licence; 513 stars on 2026-10-10, T15). The Uno paper: arXiv 2406.13454 → Math. Program. Comput. 2026, DOI 10.1007/s12532-026-00310-9. The CRAN package `Uno` (DOI 10.32614/cran.package.uno, 8 Jun 2026).
  - Funnel SQP (arXiv 2409.09208 → Math. Program. 217, DOI 10.1007/s10107-025-02284-3).
  - Filter-guided ADMM (Optimization Online Feb 2024 → JOTA 2026, DOI 10.1007/s10957-026-02983-7).
  - BQPD_jll.jl (May 2025, T14).
- **Trigger, as stated.** [stated · primary] The 2017 MPEC outlook says better solvers must "build on our existing NLP solver infrastructure" (T09 p. 9). The Uno abstract states the aims, ending with "(4) reduce the cost of development and maintenance of multiple optimization solvers" (arXiv 2406.13454, coauthored). The first two aims, "(1) organize mathematical optimization strategies into a coherent hierarchy; (2) offer a wide range of efficient and robust methods that can be compared for a given instance", echo his 1993 finding that "no one solver outperforms all other solvers on all problems" (T10 p. 16). The link across 31 years is my reading [inferred].
- **Trigger, as practised.** [practice · primary; reading inferred] A collaborator carried the C++ code: Charlie Vanaret, listed in Aug 2022 as "Research Assistant, Berlin Institute of Technology" when he presented "Uno: A Modular Open-Source C++ Solver for Unifying Nonlinear Optimization" at Argonne (T22). By Nov 2025 he was affiliated with Argonne MCS and the Zuse-Institut Berlin (arXiv 2406.13454v2, T17). The repository sits under his account (T15). The funnel paper presents itself as an extension of the filter theory: "We prove global convergence of the trust-region funnel SQP method, building on known results from filter methods." (arXiv 2409.09208, T17)
- **Packaging Fletcher's code for a new ecosystem.** [practice · primary] The BQPD_jll.jl README says: "The underlying solver is a closed-source product. Although its source code is not publicly available, the precompiled binaries are freely redistributable under the BSD 3-Clause license." On 8 Jul 2026 Leyffer added "bqpd latex manual" to the repository (T14). [inferred] About 27 years after the filterSQP manual (1998), he is the steward who moves his late advisor's solver into the Julia and Uno ecosystem.
- **Penalty functions revisited (2025–2026).** [stated · primary] Abstract of his 3 July 2025 blackboard talk, "Raiders of the lost penalty function": "During the 1970s hay days of constrained optimization, many globalization strategies were proposed including the famous barrier function and the exact penalty function. At the time, many lesser-known cousins of these functions were discarded due to numerical issues. Recently, the Indiana Jones of optimization (aka Nick Gould) found an old map of these functions, and became fascinated by the exponential penalty function that has some favorable theoretical properties." (T22). In Aug–Sep 2026 his QuantumOpt26 brief reads: "Experiments with QHDOPT optimizer with a goal of tackling constraints via an exact penalty function." (T14). [inferred] The author of "Nonlinear programming without a penalty function" (2002) returns to penalty functions, as he anticipated in 2017 when he said the choice between filters and modern penalty methods "is really a question of personal preference". The trigger named in the abstract is a collaborator (Gould) rediscovering discarded methods. No paper on the exponential penalty was found on arXiv as of 2026-10-10 (T17).

### Turn K · seniority and service at their peak (2021–2025)

- **What.** [stated/observed · primary]
  - Secretary of ICIAM, 2015–2022 (T05).
  - Chair, SIAM Climate Task Force, 2021 (T05).
  - SIAM president-elect from 30 Nov 2021, and president from 1 Jan 2023 to 31 Dec 2024 (T23).
  - "R&D Leader" by Dec 2022 (T25).
  - Deputy division director by 10 Mar 2023 (T03, T25).
  - Argonne Distinguished Fellow, 15 Dec 2023 (T26).
- **What happened to the research.** [practice · primary; reading inferred] Publication did not stop: Crossref and arXiv show 2023–2025 papers in every active line (§2). Most have a junior first author (note 01's authorship analysis, not re-checked). The items in this period where he appears alone or first are the McCormick paper (Leyffer & Manns, alphabetical order) and the 2025 penalty talk. [inferred] Service and management shifted his role towards directing lines carried by juniors and external doctoral students (§1.2). No statement of his own about this shift was found.

### Turn L · AI-assisted research (July 2026 → now)

- **What.** [practice · primary] Four new repositories on his GitHub account in nine weeks: scholar-report (9 Jul), conDFO (15 Jul), BestPractices4AI (27 Jul–4 Aug) and QuantumOpt26 (24 Aug–3 Sep). Three of them (conDFO, BestPractices4AI, QuantumOpt26) carry a `CLAUDE.md` brief or a `.claude/` folder of session logs, plans and status files. The fourth, scholar-report, is a Python tool for collecting and verifying publication lists; whether it was written with an assistant is not stated. He also co-hosted a LANS seminar on "Trustworthy Agentic AI for Multidisciplinary Design Optimization" (23 Jul 2026, T22). Details in §7.
- **Trigger, as he records it.** [stated · primary] His BestPractices4AI site keeps a dated "News" list with two items: "08/01/26: OpenAI - Ten advances in mathematics and theoretical computer science" and "06/02/26: Leiden Declaration on Artificial Intelligence and Mathematics" (the date format is not stated). Under "Argonne-Specific Resources" it lists institutional tools ("Argo API Documentation", "Vibe Coding Hackathon — 2025 Vibe Coding Workshop at Argonne"). Under tools it lists "Claude Code 101 Hackathon — Claude Code as a co-scientist: workshop" (T14). [inferred] The triggers are a new tool, made available institutionally at Argonne in 2025–2026, and the 2026 public debate on AI in mathematics.
- **Timing.** [inferred] He entered while the wave was under way, not ahead of it. What is distinctive is what he points the tool at: his own oldest instruments. Filter global convergence goes into constrained DFO in conDFO, explicitly "following the Fletcher–Leyffer–Toint filter–SQP proof structure" (logbook, T14). Exact penalty functions and integer variables go into quantum Hamiltonian descent (QuantumOpt26).

---

## 5. Entry and exit timing at a glance

"Consensus at entry" cites the evidence for where the field stood when he came in. Rows without a quoted statement are [inferred] from dates.

| Line | First dated evidence | Where the field stood at entry | Trigger type | Exit, dormancy or status | Tag |
|---|---|---|---|---|---|
| Convex MINLP (OA, B&B) | thesis Dec 1993; paper 1994 | small: manageable MINLPs "rather small" (T10 p. 23) | advisor's toolbox; failure-driven redesign (worst-case example) | consolidated 2006–2013; his own classic-algorithm papers cluster 1994–2013; taught 2013, 2016, 2024 (T06) | [stated + practice] |
| MIQP B&B | thesis chapter → 1998 | (not documented) | artefact of his own method (T10 p. 16) | last listed as a research interest on the Feb 2003 Argonne homepage (T02); absent from the research statement from Dec 2008 onward (T02, T03) | [stated + practice] |
| Filter methods | 1996 (Fletcher's plenary) → 1997 report | penalty functions were the established tool (T09 p. 3); filter was new | advisor's idea + empirical observation (T12 p. 4) | never left; self-deflated in 2017; extended into AL (2016/20), ADMM (2024/26), DFO (2026) | [stated + practice] |
| SQP inside B&B | 1998 report | the idea existed (Borchers and Mitchell); the field "decompose[d]" because of packaged software | new tool: his own SQP solver (T11 p. 2) | became the NEOS "MINLP" solver (note 01, not re-checked); no later B&B-interleaving paper found | [stated + practice] |
| MPEC/MPCC as NLP | MacMPEC 2000; Dundee interests Feb 2001; reports 2002 | "commonly regarded as numerically unsafe" (T09 p. 7) | counter-consensus numerical evidence from his own solver | dormant about 2010–2019 [inferred]; returned 2020–2026 | [stated + practice] |
| Grid computing | report May 2001 | — | not documented | one paper (2002) | [practice; exit inferred] |
| Computational economics | 2004–2007 | — | institution (institutes he co-chaired) | none found after 2009 | [practice; exit inferred] |
| HPC, exascale, networks, inexact computing | 2012–2016 | — | institution (lab computing mission) [inferred] | none after 2016 | [practice; exit inferred] |
| Nonconvex MINLP by piecewise-linear refinement | 2008–2009 | — | (not documented) | presented 2009; no journal record found | [stated + practice] |
| Mixed-integer optimal control → MIPDECO | 2013 (TACO) → 2015 preprint → 2019 talk | "new class of problems" (2019); McCormick relaxations "have not gained much attention in PDE-constrained optimization so far" (2024) | collaborators (Kirches, Sager, Manns); DOE applications | active | [stated + practice] |
| Machine learning (formulations) | 2018 talk; 2021 papers | ML a mass movement already [inferred]; "new areas such as machine learning where optimization may have a decisive impact" (2021) | institution + juniors; reformulation into MINLP/MPCC | active | [stated + practice] |
| Design of experiments, inverse problems, APS imaging | 2019–2021 | — | institution (APS; DOE UQ); in 2025 contributor to DOE's inverse-methods report | active | [practice] |
| Quantum control and quantum optimization | 2022 preprint | — | collaborators (Larson, Shen, Fei, Brady); in 2026 a student project | active | [practice] |
| NLP-solver architecture (Uno) | Oct 2018 commits | his own diagnosis: MPEC solvers "far less mature" (2017) | own code base + postdoc carrier | active (MPC 2026, CRAN 2026) | [stated + practice] |
| Penalty functions revisited | Jul 2025 talk | discarded "cousins" of the 1970s (2025 abstract) | collaborator (Gould) | active (QuantumOpt26, 2026); no paper yet | [stated + practice] |
| AI-assisted research | Jul 2026 | public debate under way (his "News" list, 2026) | new tool + institution | active | [stated + practice] |

---

## 6. Failures, abandoned directions and corrections along the trajectory

Only items that bear on the trajectory are listed. Note 01 §1.9 has the full catalogue of failures in the papers themselves.

| # | When | What | Evidence | Tag |
|---|---|---|---|---|
| F1 | 1993 | His first algorithm's worst case redirects the thesis toward second-order master problems | T10 p. 59 (quoted in Turn A) | [stated · primary] |
| F2 | 1994 → 2008, told in 2017 | His 1994 convergence proof was corrected by others: "Later, Bonami et al. corrected our convergence proof [4], and Pierre developed a much nicer example that showed that outer approximation can take an exponential number of iterations [26]." Refs: DOI 10.1016/j.disopt.2006.10.011; DOI 10.1287/ijoc.1120.0545 | T09 p. 5; T18 | [stated · primary] |
| F3 | late 1990s | A hope in the filter line was given up: "However, the following example shattered the hope that filter methods can avoid the Maratos effect in general" (2006). The early proof was repaired by coauthors, "who corrected many errors in the early proof" (2017) | T12 p. 8; T09 p. 4 | [stated · primary] |
| F4 | 2006 → 2017 | His claim for filters was scaled back: from "We believe filter methods achieve this goal" to "I do not believe that there exists a big difference between filter methods and modern penalty function methods" | T12 p. 4; T09 p. 5 | [stated · primary] |
| F5 | 2001–2016 | Lines entered and left without a stated reason: grid computing, computational economics, HPC/exascale, network epidemics, inexact computing | §4 Turn F | [practice; exits inferred from absence] |
| F6 | 2008–2009 | Nonconvex "branch-and-refine": presented in 2009, no journal article found | T31; Crossref query | [practice · primary; negative search] |
| F7 | 2024 → 2026 | Published Correction: "We correct two mistakes in the paper [S. Leyffer and P. Manns, Math. Prog. 2025]." One is a missing box constraint in Assumption 2.7. Without it, "assuming a unique solution to (2) for all w … is unrealistic given that (2) may become an eigenvalue problem for suitable w"; the other is a proof step in Proposition 2.14. Online 17 Feb 2026, DOI 10.1007/s10107-026-02330-8 | correction p. 1 (T18 record; PDF read) | [practice · primary] |
| F8 | 2026 (unpublished) | The AI-assisted conDFO logbook records a flaw found in his own 2002 filter proof: "FLT02's own Corollary-to-Lemma-1 proof has an unstated existence assumption in its chain construction (succ(i) may fail to exist); replaced by a compactness argument (Remark in the paper)." The logbook is written in the assistant's voice; I have not verified the mathematical claim, and it is not a published erratum | T14 (conDFO `LOGBOOK.md`, 15 Jul 2026) | [practice · primary record; claim unverified] |
| F9 | 2024 → 2026 | Slow publication of the newest work (not a failure; shown for scale): Uno, arXiv 19 Jun 2024 → "first revision" 9 Nov 2025 → published 10 Jun 2026; filter-ADMM, Optimization Online 6 Feb 2024 → JOTA May 2026; MPEC B-stationarity, arXiv 23 Jan 2025 → v5 "Final accepted version" 8 Sep 2026 → COAP 29 Sep 2026 | T17; T18; T21 | [practice · primary] |
| F10 | 14 Jan 2024 → now | Three book-named repositories ("MINLO-book", "MINLO-book1", "MINLPbook") were created the same day and are still empty on 2026-10-10. A book plan is a reasonable guess from the names, but nothing documents it | T14 | [practice · primary; purpose unknown] |
| F11 | no evidence found | No rejected paper, withdrawn preprint or abandoned software release was found in the public record checked in this run | — | [gap] |

---

## 7. The last 12 months (10 Oct 2025 – 10 Oct 2026)

Sources: arXiv API (T17), Crossref (T18), DBLP SPARQL (T19), Google Scholar sorted by date (T20), Optimization Online (T21), Argonne LANS seminar records (T22), GitHub (T14–T15). Dates are online-publication or event dates.

### 7.1 Publications and revisions

| Date | Item | Identifier | Tag |
|---|---|---|---|
| 22 Oct 2025 | Kiessling, Leyffer, Vanaret, "A unified funnel restoration SQP algorithm", Math. Program. 217(1–2) 323–367 (print May 2026) | DOI 10.1007/s10107-025-02284-3; arXiv 2409.09208 | [practice · primary] |
| 9 Nov 2025 | Uno preprint v2, comment "Submitted to Mathematical Programming Computation journal (first revision)" | arXiv 2406.13454v2 | [practice · primary] |
| 5 Jan 2026 | McCormick paper preprint v5 | arXiv 2406.07891v5 | [practice · primary] |
| 17 Feb 2026 | Leyffer & Manns, "Correction: McCormick envelopes in mixed-integer PDE-constrained optimization", Math. Program. 218(1–2) 591–592 | DOI 10.1007/s10107-026-02330-8 | [practice · primary] |
| 8 Apr 2026 | Lu, Lynn, Du, Di, Leyffer, "Optimizing Paths for Adaptive Fly-Scan Microscopy", ISBI 2026, 1–5 | DOI 10.1109/ISBI61048.2026.11515614 | [practice · primary] |
| 14 May 2026 | Baraldi, Leyffer, Wild, "Using Filter Methods to Guide Convergence for ADMM, with Applications to Nonnegative Matrix Factorization Problems", J. Optim. Theory Appl. 209(2) 66 | DOI 10.1007/s10957-026-02983-7 | [practice · primary] |
| 8 Jun 2026 | Narasimhan, Vanaret, Leyffer, "Uno: R Interface to the 'Uno' Nonlinear Optimization Solver", CRAN package | DOI 10.32614/cran.package.uno | [practice · primary] |
| 10 Jun 2026 | Vanaret & Leyffer, "Implementing a unified solver for nonlinearly constrained optimization", Math. Program. Comput. | DOI 10.1007/s12532-026-00310-9 | [practice · primary] |
| Jul 2026 | McCormick paper and its Correction in print, Math. Program. vol. 218 (online since 6 Jan 2025) | DOI 10.1007/s10107-024-02181-1 | [practice · primary] |
| 8 Sep 2026 | MPEC B-stationarity preprint v5, comment "Final accepted version of the paper" | arXiv 2501.13835v5 | [practice · primary] |
| 29 Sep 2026 | Nurkanović & Leyffer, "A globally convergent method for computing B-stationary points of mathematical programs with equilibrium constraints", Comput. Optim. Appl. (online) | DOI 10.1007/s10589-026-00832-x | [practice · primary] |
| 6 Oct 2026 | Choudhary, Leyffer, Yang, "An Alternating Direction Method of Multipliers for Topology Optimization", v2 | arXiv 2509.19888v2 | [practice · primary] |

- **What is absent.** [practice · primary] arXiv shows no new submission with Leyffer as author after 24 Sep 2025 (2509.19888v1). The arXiv API returned 35 entries sorted by submission date; every later event is a revision. The newest Optimization Online posting with his name is from 3 Sep 2024. The year's output therefore consists of earlier work reaching journals: four journal papers, one conference paper, one Correction and one software package. [inferred] This is consistent with a pipeline that runs 1–2.5 years from preprint to print (F9), and with the shift of his own time in July–September 2026 to the AI-assisted projects below. Whether new preprints are in preparation is unknown.
- **Possible item not verified.** Scholar lists "Rapport de Prospective du GDR Recherche Opérationnelle et Décision (ROD)" (CNRS, 2026, authors "C Artigues, N Brauner, P Fouilhoux, et al.") on his profile (T20). His authorship is not confirmed and could be a profile error.

### 7.2 Software and repositories (GitHub account "leyffer", created 8 Jul 2014; commit author name "Sven Leyffer")

| Dates | Repository | What it is (from its own files) | Tag |
|---|---|---|---|
| 25 May 2025 → 8 Jul 2026 | BQPD_jll.jl | Julia package of Fletcher's QP solver, created with Alexis Montoison. Copyright line: "Copyright (c) 2025 Alexis Montoison, Sven Leyffer". The binaries are "freely redistributable under the BSD 3-Clause license". Last commits: "adding bqpd latex manual", "Update README.md" (8 Jul 2026) | [practice · primary] |
| 9 Jul 2026 | scholar-report | A Python tool: "Given a list of researchers and a list of keywords, search free scholarly APIs, collect each author's most-cited keyword-relevant papers plus a total hit count, verify titles/journals against the live landing page, and emit a compilable LaTeX report." It includes an "Authorship harness" that drops wrong-person papers | [practice · primary] |
| 15 Jul 2026 | conDFO | "Constrained Derivative-Free Optimization": a model-based trust-region filter method with a convergence proof. Files: `CLAUDE.md` (his brief), `LOGBOOK.md`, `STATUS.md`, `paper/`, `plans/`, `refs/`. Four commits, all on 15 Jul 2026 | [practice · primary] |
| 27 Jul → 4 Aug 2026 | BestPractices4AI | "A curated, evolving collection of best practices, notes, and links for working with AI", published with MkDocs at leyffer.github.io/BestPractices4AI; 28 commits | [practice · primary] |
| 24 Aug → 3 Sep 2026 | QuantumOpt26 | With David Linnet. "Experiments with QHDOPT optimizer with a goal of tackling constraints via an exact penalty function." Direction A: "an exact/$L_1$ penalty paired with non-smooth QHD". Direction B: "native binary/integer decision variables on the Ising backend" (`.claude/STATUS.md`). The paper skeleton "Quantum Optimization: Constraint Handling for Quantum Hamiltonian Descent" had empty sections on 3 Sep 2026 | [practice · primary] |

- **How the conDFO project was run.** These files describe his research workflow in 2026; agent 03's dimension, recorded here because it is the newest dated activity.
  - [stated · primary] He wrote the brief himself; it carries his own typing. It sets the task: "Design a sequential algorithm for constrained derivative-free optimization (DFO) and proof its convergence properties". It sets the proof method: "Transfer as much of the proofs from the DFO paper and the filter paper." It also asks: "Clearly identify gaps that may require new ideas, and discuss." The two papers it names are Larson, Menickelly and Wild, "Derivative-free optimization methods", Acta Numerica 28 (2019) 287–404 (DOI 10.1017/S0962492919000060, Crossref-checked) and his own 2002 SIAM J. Optim. filter paper (DOI 10.1137/S105262340038081X).
  - [practice · primary; written in the assistant's voice] The logbook records "Design decisions (with Sven)" and "Gap rulings (Sven, same day)". The status file says: "Three sessions so far, each ending with multi-agent adversarial review and all confirmed findings repaired". The draft grew to 23 pages on 15 Jul 2026, with five open "Gap" remarks.
  - [inferred] The division of labour is: the senior researcher sets the problem, the novelty claim and the proof plan, and makes the design and gap rulings; the agents draft and attack the proofs. The project re-uses his 2002 filter theory as the backbone.

### 7.3 Talks, seminars, service

- **No talk by him as speaker was found in the window.** The last talks found are the 3 Jul 2025 LANS talk and a 2 May 2025 student-chapter meet-and-greet (T22, T35). Searches covered the LANS records and two web searches; the SIAM OP26 programme (Edinburgh, 2–5 Jun 2026) could not be searched (Gaps). [practice · primary; negative result with limited coverage]
- **Seminars hosted.** [practice · primary] He co-hosted "Trustworthy Agentic AI for Multidisciplinary Design Optimization" (Ping He, 23 Jul 2026; "Host: Marco Mangano/Sven Leyffer") and hosted "Recent results on nonconvex Frank-Wolfe splitting algorithms" (Zev Woodstock, 2 Sep 2026) (T22). He was also the listed host of twelve LANS seminars in 2022–2023 (T22).
- **Titles and roles current in the window.** [observed · primary] The Argonne profile (capture 30 Nov 2025) reads "Deputy Division Director/Senior Computational Mathematician/Argonne Distinguished Fellow" (T25). His homepage (capture 18 Sep 2026; edit of 10 Mar 2023) reads "senior computational mathematician and deputy division director" (T03). Google Scholar on 2026-10-10 reads "Senior Computational Mathematician, Argonne National Laboratory" (T20).
- **DOE strategy work.** [practice · primary] He is listed among the contributors to "Basic Research Needs for Inverse Methods for Complex Systems under Uncertainty" (dated Sep 2025; Crossref record created 23 Dec 2025; DOI 10.2172/2583339). His role is not stated in the record I read.

---

## 8. Era and resource context, phase by phase

| Phase | Computing and tools | Money and institution | Team and seniority | Evidence | Portability today [inferred] |
|---|---|---|---|---|---|
| Dundee PhD (about 1990–1993) | Fortran 77; NAG E04UCF for NLPs; Fletcher's QP code; tests "on a SUN-SPARC SLC using the FORTRAN 77 compiler with the -fast option" (T10 p. 43) | University of Dundee numerical-analysis group | student with advisor; two-author papers | T10 pp. 23, 43, 77 | high: small decisive examples and owning the code need no special resources |
| Dundee postdoc (1994–2002) | own Fortran solvers (filterSQP manual 1998; MINLP branch-and-bound); test problems posted on his own web pages (MINLP_TP, MacMPEC) | EPSRC grant GR/K51204 (1998) | Research Assistant/Fellow with Fletcher, Toint, Gould and Wächter; reports first, journals about 2–4 years later (NA/171 1997 → 2002; NA/182 1998 → 2001; NA/210 2002 → 2004) | T11 p. 1; T01; T18 | high |
| Argonne, early (2002–2010) | NEOS-served solvers (note 01, not re-checked); grid computing; AMPL test libraries | DOE Office of Science ASCR (contract W-31-109-ENG-38 in the 2006 history, p. 1); UChicago Computation Institute fellow; Northwestern adjunct | "computer scientist" (2005) → "computational mathematician" (2008); coauthors from several universities (names in §2; their affiliations not re-checked here) | T12 p. 1; T02; T05 | medium: depends on a lab that hosts software services |
| Argonne, team MINLP (2006–2016) | MINTO + filterSQP (FilMINT); C++ framework (Minotaur, "developed by Ashutosh Mahajan at Argonne", T09 p. 6) | DOE ASCR (contract DE-AC02-06CH11357, Acta preprint p. 1) and SciDAC (2009 paper) | senior by Mar 2013; editor-in-chief of MMOR (2008–2014); SIAM VP (2010–2013) | T13 p. 1; T37; T03; T05 | low for one person: needs postdocs and long-lived software teams |
| Argonne, applications and MIPDECO (2015–2022) | DOE facilities (APS); collaborators' clusters (TU Dortmund LiDO3); arXiv-first | DOE ASCR Applied Mathematics; partners' DFG funding | Farkas Prize (2016); editor-in-chief of MP B (2018–2021); juniors as first authors | T17 acknowledgments; T05; T28 | low: depends on lab facilities and an international network |
| Seniority (2022–2026) | Julia/R packaging (BQPD_jll.jl, CRAN Uno); AI assistants (Claude Code; Argonne's Argo API listed on his site) | DOE ASCR; external funders of coauthors (Flanders Make, DFG, GAČR) | R&D Leader (2022), deputy division director (2023), SIAM President (2023–2024), Distinguished Fellow (2023); most papers led by juniors or external doctoral students (note 01 authorship analysis, not re-checked) | T14; T17; T25; T26 | the AI-assisted workflow is portable now; the network and the stature are not |

---

## 9. Patterns across the turns (for Phase 2; all [inferred], each with its basis)

1. **Fixed base, migrating extensions.** He keeps one core competence: reliable large-scale NLP methods and filter-type globalization. He turns by naming a new "extension" area for it. *Basis:* the unchanged first sentence of his research statement from Dec 2008 to 2026 and the 2021 swap of the extension list (§3). *Skill hook:* when choosing a new topic, ask what the home toolkit can carry into it.
2. **Own the instrument, then redesign around it.** New algorithms followed from controlling the solver internals. *Basis:* 1993 packaged NAG solver → 1998 "By using our own solver we are able to remove this unnecessary restriction" (T11 p. 2). Later the same logic drives Minotaur ("Algorithmic advances … have often taken advantage of the special structure of problems, which motivated us to develop the Minotaur software framework", T09 p. 6) and Uno (aim "(3) enable researchers to experiment with novel optimization strategies", arXiv 2406.13454).
3. **Enter on numerical evidence against the received view.** *Basis:* MPECs "commonly regarded as numerically unsafe" versus "our initial numerical experience with filterSQP was very positive" (T09 p. 7). Filters began from "the unmodified SQP method is able to quickly solve a large proportion of test problems" (T12 p. 4). For filters the numerical report (NA/171, Sep 1997) preceded the first convergence proof (NA/183, Aug 1998). For MPECs his own account puts the numbers first, but the report dates do not settle it (C12).
4. **Consolidate after the field has grown.** He writes the survey, edits the volume and builds shared software once a line is established. *Basis:* the 2006 filter history, the 2008 IMA workshop and 2012 volume, the 2013 Acta survey ("The past 20 years or so have seen a dramatic increase…", T13 p. 11), the 2017 retrospective, the 2020 robust-optimization survey.
5. **Collaborators and institutions supply the turns; the method stays his.** *Basis:* the triggers documented for turns C, G, H, I, J and L name a person (Fletcher, Linderoth's student, Kirches and Sager, Vanaret, Gould, Nurkanović) or a lab programme (APS, DOE AI4ESP and the DOE inverse-methods report, quantum). What he contributes in each is a reformulation into his home classes: ReLU networks as MINLP or MPCC (arXiv 2111.10489); TV-regularized binary control for quantum pulses (arXiv 2204.05773); filters for ADMM and DFO; exact penalties for quantum Hamiltonian descent.
6. **Silent exits; loud self-corrections.** He leaves lines without comment (Turn F; F5–F6). He states openly when he or others got something wrong: the 1994 proof corrected by Bonami et al.; the Maratos hope "shattered"; the scaled-back filter claim; the 2026 Correction. *Basis:* §6.
7. **Return to the base when the extensions mature.** After about 2016 the agenda swings back to globalization and solver architecture: augmented-Lagrangian filter, Uno, funnel SQP, penalty functions revisited, MPEC B-stationarity. In 2026 even the AI-assisted projects re-use the filter and the exact penalty. *Basis:* Turn J, Turn L.
8. **Software medium follows the era, stewardship continues.** Own Fortran codes (1990s) → assembled hybrid (FilMINT) → C++ frameworks built mainly by junior collaborators (Minotaur by Mahajan, Uno by Vanaret) → Julia and R packaging and AI-assisted drafting (2025–2026). Fletcher's BQPD moves with him into the Julia ecosystem in 2025–2026. *Basis:* §2, §7.2.

---

## Contradictions (kept, not reconciled)

- **C1. PhD date and title.**
  - Thesis title page: "Deterministic Methods for Mixed Integer Nonlinear Programming", "December 1993" (T10 p. 1).
  - MGP: "Ph.D. University of Dundee 1994", title "Deterministic Methods in Mixed Integer Nonlinear Programming" (T38).
  - His Bio and Argonne: "Ph.D. in 1994" (T04, T23, T25).
- **C2. His Dundee post.**
  - Dundee homepage (versions of Feb 2001 and Feb 2002): "Position: Research Assistant" (T01).
  - Appointments page (edited Jan 2025): "Research Fellow, Department of Mathematics, University of Dundee (1994-2002)" (T05).
  - Bio: "He has held postdoc positions at Dundee, Northwestern, and Argonne" (T04).
- **C3. Order of the postdoctoral posts.**
  - Bio: "Dundee, Northwestern, and Argonne" (T04).
  - Argonne news (2021), Argonne profile (2025) and the LANS bios (2024, 2025): "Dundee, Argonne, and Northwestern University" (T23, T25, T22).
  - His Appointments page lists Northwestern only as "Adjunct Professor … (2006-2012)" and Dundee as continuous 1994–2002 (T05). None of these sources dates the Argonne or Northwestern postdoctoral posts.
- **C4. SIAM presidency dates.**
  - "SIAM President (2023-2024)" on his Appointments page (T05).
  - Argonne 2021: "serve as president from January 1, 2023, to December 31, 2024" (T23).
  - Argonne profile (capture 30 Nov 2025): "He was SIAM President from 2022-2024" (T25).
  - ASU event page (2 May 2025): "former SIAM President (2022–2024)" (T35).
  - The LANS speaker bios of 3 Jul 2024 and 3 Jul 2025 both say "He is the current SIAM President" (T22); by the 2021 dates the second one is after the term ended.
  - The Bio page (edited 17 Nov 2023) says "He is the current SIAM President" (T04).
- **C5. Mathematical Programming B editor-in-chief.** "(2018-2021)" (T05) against "From 2017 to 2021" (Wikipedia, T39). Argonne in Nov 2021: "he currently is editor-in-chief of Mathematical Programming B" (T23).
- **C6. A coauthor's name.** His Bio: "the 2012 COAP Best Paper Prize with Chungen Chen and Roger Fletcher" (T04); the 2017 article: "a nonmonotone filter, developed by Chungen Chen at Argonne" (T09 p. 5). The paper, Crossref and the COAP award page give "Chungen Shen" (T18, T32).
- **C7. His agenda as listed by different pages at nearly the same time.**
  - Homepage from 13 Sep 2021: "design-of-experiments, machine learning, quantum computing, and mixed-integer nonlinear optimization"; complementarity is gone (T03).
  - Argonne Distinguished Fellow text (Dec 2023): "discrete optimization for topology design and optimization problems involving digital twins" (T26).
  - Argonne profile (capture Nov 2025): "mixed-integer nonlinear optimization, optimization problems with PDE constraints, and optimization problems with complementarity constraints" (T25).
  - The 2025–2026 MPEC paper shows complementarity is still active in practice (T17).
- **C8. His view of filter methods.** 2006: "We believe filter methods achieve this goal." (T12 p. 4). 2017: "I do not believe that there exists a big difference between filter methods and modern penalty function methods" (T09 p. 5). 2024–2026: new filter-based papers and the filter-DFO project continue the line (T17, T14).
- **C9. Credit for the filter idea.**
  - Fletcher: "Discovering the filter idea was a real "eureka" moment for me" (Dundee release, T30).
  - The 2006 history: "first proposed by Fletcher in a plenary talk … May 1996" (T12 p. 7).
  - The Farkas citation: "In later groundbreaking work with Roger Fletcher, Leyffer proposed a new class of methods for constrained nonlinear programs, which employ the innovative concept of a filter" (T28).
- **C10. Penalty functions.** The 2002 flagship is titled "Nonlinear programming without a penalty function" (DOI 10.1007/s101070100244). In 2025 he gives "Raiders of the lost penalty function" (T22). His 2026 quantum project targets "an exact penalty function" (T14). The 2017 article already treats the two as interchangeable ("a question of personal preference"). Kept as a tension in the record; how he reconciles them is not stated.
- **C11. Lagrange Prize committee year.** "Chair, Selection committee, Lagrange Prize in Continuous Optimization (2020)" (T05) against the MOS record listing "Sven Leyffer (chair)" for the 2021 award (T29). Probably the same committee labelled by working year and award year; not resolved.
- **C12. Which came first for MPECs, numbers or theory.** 2017: "our initial numerical experience with filterSQP was very positive [19], and we investigated the convergence of SQP methods applied to (3.9) together with Roger Fletcher, Danny Ralph, and Stefan Scholtes [20]" (T09 p. 7). The Dundee report series dates the convergence report NA/209 to May 2002 and the numerical report NA/210 to Aug 2002 (T02).

---

## Gaps (not found, not read, or not verifiable)

- **Stated reasons for the big moves.** None found for:
  - going from Hamburg to Dundee and to Fletcher;
  - who chose the thesis topic;
  - leaving Dundee for Argonne in 2002;
  - leaving the grid, computational-economics, HPC and network lines;
  - entering quantum control.

  The 2017 retrospective covers filters, MINLP and MPECs only. No interview about his own career was found. The 2021 CRLC talk on his "professional experiences in a National Laboratory" has no recording or transcript that I found.
- **Hamburg Vordiplom (1989):** Wikipedia only, without a source.
- **Postdoc dates:** the dates of his Argonne and Northwestern postdoctoral posts, and how they fit the 1994–2002 Dundee fellowship (C2, C3).
- **Talks in the last 12 months.** None found as speaker. Coverage was limited: the Argonne LANS records and two web searches. Not checked:
  - SIAM OP26 (Edinburgh, 2–5 Jun 2026): no Leyffer item in search results; a sibling agent's direct fetch of the programme hit a Cloudflare challenge;
  - INFORMS 2025;
  - ICCOPT 2025;
  - other 2026 meetings.

  The LANS search is reliable only for Argonne-internal seminars.
- **SIAM presidential columns (2023–2024)** and the 2021 Climate Task Force article: not read in this run. Sibling copies were seen only as leads, and their content is about SIAM rather than his research turns.
- **Exponential-penalty line (2025):** no paper, preprint or slides found. The arXiv author query of 2026-10-10 has none.
- **conDFO and QuantumOpt26 outcomes:** unknown. No public paper as of 2026-10-10. The proof gap that the conDFO logbook reports in the 2002 filter proof was not checked mathematically (F8).
- **"MINLO-book" repositories (Jan 2024):** empty. Whether a book is in preparation is not documented.
- **Branch-and-refine (2008–2009):** preprint not read; publication status unknown beyond a negative Crossref query.
- **DBLP HTML and XML endpoints** returned a bot-check page, which I did not try to get around. I used the public SPARQL endpoint instead.
- **Affiliations and roles of juniors** beyond the first pages read here, including Mahajan's current post and the status of Choudhary and Linnet (visitor, intern or student): not verified. See note 04.
- **Scholar item "Rapport de Prospective du GDR ROD" (2026):** his authorship not confirmed.
- **The DOE "Basic Research Needs" report (2025):** his role in it not read.
- **The thesis acknowledgments:** absent from the online copy, so the thesis offers no first-hand account of how he came to Fletcher.

---

## Sources

Primary (T01–T37, T41)

- T01 · S. Leyffer, Dundee homepage ("Mathematics Staff: Sven Leyffer") · page versions last modified 20 Feb 2001 and 12 Feb 2002; captures 4 Apr 2001, 30 Oct 2001, 22 May 2002, 30 Sep 2002; "page has moved" notice captured 28 Nov 2002 · https://web.archive.org/web/20010404011354/http://www.mcs.dundee.ac.uk/~sleyffer/ and https://web.archive.org/web/20021128095856/http://www.maths.dundee.ac.uk/~sleyffer/ · primary
- T02 · S. Leyffer, Argonne homepage and research page · captures 21 Feb 2003, 20 Dec 2005 ("Last updated on 08/19/05"), 27 Mar 2008 ("March 6, 2008"); research.htm captured 2 Dec 2008 · https://web.archive.org/web/20030221112214/http://www-unix.mcs.anl.gov/~leyffer/ ; https://web.archive.org/web/20081202102447/http://www-unix.mcs.anl.gov/~leyffer/research.htm · primary
- T03 · S. Leyffer, wiki homepage "Sven Leyffer" · 16 captures read, 7 May 2009 – 18 Sep 2026 (page edits of 19 Mar 2009, 23 Jan 2012, 4 Mar 2013, 18 Dec 2015, 9 Sep 2019, 10 Nov 2019, 13 Sep 2021, 10 Mar 2023) · https://web.archive.org/web/20260918072958/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer · primary
- T04 · S. Leyffer, "Sven Leyffer's Bio" · last edited 17 Nov 2023; capture 29 Apr 2026 · https://web.archive.org/web/20260429015425/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer%27s_Bio · primary
- T05 · S. Leyffer, "Sven Leyffer's Appointments" · last edited 21 Jan 2025; capture 12 Aug 2025 · https://web.archive.org/web/20250812091025/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer%27s_Appointments · primary
- T06 · S. Leyffer, "Sven Leyffer's Lectures" · last edited 30 Jul 2024; capture 2 Apr 2025 · https://web.archive.org/web/20250402030454/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer%27s_Lectures · primary
- T07 · S. Leyffer, "Sven Leyffer's Research" / "Research" · last modified 5 Mar 2009 (capture 5 Apr 2012) and 27 Sep 2012 (capture 20 Jan 2021) · https://web.archive.org/web/20120405054533/http://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer%27s_Research · primary
- T08 · ORCID public record 0000-0001-8839-5876 (employment: Argonne; education: University of Dundee, PhD, Mathematics; membership: SIAM; no dates given) · fetched 2026-10-10 · https://pub.orcid.org/v3.0/0000-0001-8839-5876 · primary (self-entered)
- T09 · S. Leyffer, "Nonlinear Optimization and Beyond", INFORMS Optimization Society Newsletter (OS Today) 7(2), Oct 2017, pp. 3–10 · https://higherlogicdownload.s3.amazonaws.com/INFORMS/9a2da56a-3917-4600-a0e3-84cfb0d2b004/UploadedFiles/09uQ9yCcRT5ZSlbtKE74_OStoday2017v2.pdf · primary (read in full)
- T10 · S. Leyffer, "Deterministic Methods for Mixed Integer Nonlinear Programming", PhD thesis, University of Dundee, Dec 1993 (PDF re-typeset; 119 pp.) · originally https://www.mcs.anl.gov/~leyffer/papers/thesis.pdf (host returns 403); read from a copy saved earlier in this run by a sibling agent · primary (pp. 1, 12, 16, 23, 27, 43, 59, 77, 104 read)
- T11 · S. Leyffer, "Integrating SQP and branch-and-bound for Mixed Integer Nonlinear Programming", University of Dundee report NA/182, 6 Aug 1998 · https://optimization-online.org/wp-content/uploads/2000/08/208.pdf · primary (pp. 1–2 read as page images)
- T12 · R. Fletcher, S. Leyffer, Ph. L. Toint, "A Brief History of Filter Methods", Argonne preprint ANL/MCS-P1372-0906, 26 Sep 2006, rev. 9 Oct 2006 · https://optimization-online.org/wp-content/uploads/2006/10/1489.pdf · primary (pp. 1, 4, 7, 8, 15)
- T13 · P. Belotti, C. Kirches, S. Leyffer, J. Linderoth, J. Luedtke, A. Mahajan, "Mixed-Integer Nonlinear Optimization", Argonne preprint ANL/MCS-P3060-1121, 22 Nov 2012 · https://optimization-online.org/wp-content/uploads/2012/12/3698.pdf · primary (pp. 1, 11–12)
- T14 · GitHub account "leyffer": user and repository metadata, commit records, and files of BQPD_jll.jl (README, LICENSE, Artifacts.toml), scholar-report (README), conDFO (README, CLAUDE.md, STATUS.md, LOGBOOK.md), BestPractices4AI (README, docs/index.md, docs/development/agent-design.md, docs/resources/links.md, .claude/CLAUDE.md), QuantumOpt26 (.claude/CLAUDE.md, .claude/STATUS.md, .claude/plans/PLAN-2026-09-03-QuantumOpt-Skeleton.md, docs/project.tex) · fetched 2026-10-10 · https://github.com/leyffer · primary
- T15 · GitHub cvanaret/Uno: repository metadata (created 29 Sep 2021, MIT) and commit search author-name:leyffer (10 commits, 15–17 Oct 2018) · fetched 2026-10-10 · https://github.com/cvanaret/Uno · primary
- T16 · GitHub coin-or/minotaur: repository metadata (created 1 Jun 2016; last push 10 Aug 2026) · fetched 2026-10-10 · https://github.com/coin-or/minotaur · primary
- T17 · arXiv API query au:Leyffer sorted by submission date (35 entries with abstracts, comments, journal refs) plus PDFs 2406.13454v2, 2406.07891v5, 2409.09208v1, 2501.13835v5, 2509.19888v2 (first pages and acknowledgments) · fetched 2026-10-10 · https://export.arxiv.org/api/query?search_query=au:Leyffer&sortBy=submittedDate · primary
- T18 · Crossref REST API: 66 DOIs checked, plus query.author=Leyffer from 2025-06-01 (10 records) and two bibliographic queries · fetched 2026-10-10 · https://api.crossref.org/works · primary (bibliographic metadata)
- T19 · DBLP SPARQL endpoint, records of pid 91/745 dated 2025–2026 (13 rows) · fetched 2026-10-10 · https://sparql.dblp.org/sparql · primary (bibliographic database)
- T20 · Google Scholar profile UubsxcAAAAAJ, sorted by date (40 rows; affiliation and interests line) · fetched 2026-10-10 via WebFetch · https://scholar.google.com/citations?user=UubsxcAAAAAJ&sortby=pubdate · primary (database record)
- T21 · Optimization Online, search "Leyffer" (10 newest entries, latest 3 Sep 2024) · fetched 2026-10-10 · https://optimization-online.org/?s=Leyffer · primary
- T22 · Argonne LANS seminar records (Events Calendar API, search "Leyffer": 18 events, 2018–2026; event 3806 "Raiders of the lost penalty function", 3 Jul 2025) · fetched 2026-10-10 · https://wordpress.cels.anl.gov/lans-seminars/wp-json/tribe/events/v1/events?search=Leyffer · primary
- T23 · Argonne National Laboratory, "Leyffer named SIAM president-elect" · 30 Nov 2021 (capture 28 Nov 2022) · https://web.archive.org/web/20221128071313/https://www.anl.gov/mcs/article/leyffer-named-siam-presidentelect · primary (institutional; includes his quote)
- T24 · Argonne National Laboratory, "Leyffer named SIAM fellow" · 18 May 2009 (capture 22 Mar 2021) · https://web.archive.org/web/20210322152019/https://www.anl.gov/mcs/article/leyffer-named-siam-fellow · primary (institutional)
- T25 · Argonne National Laboratory staff profile "Sven Leyffer" · 11 captures read, 21 Jun 2019 – 30 Nov 2025 · https://web.archive.org/web/20251130204501/https://www.anl.gov/profile/sven-leyffer · primary (institutional)
- T26 · Argonne National Laboratory via Newswise, "Five researchers named Argonne Distinguished Fellows for 2023" · 15 Dec 2023 · https://www.newswise.com/doescience/five-researchers-named-argonne-distinguished-fellows-for-2023 · primary (institutional release)
- T27 · SIAM, "Class of 2009" Fellows page · capture 17 Oct 2022 · https://web.archive.org/web/20221017194050/https://www.siam.org/prizes-recognition/fellows-program/all-siam-fellows/class-of-2009 · primary
- T28 · INFORMS Optimization Society, "Farkas Prize 2016" citation and committee · fetched 2026-10-10 · https://connect.informs.org/optimizationsociety/prizes/farkas-prize/2016 · primary
- T29 · Mathematical Optimization Society, Lagrange Prize records (2006 citation; 2021 committee) · fetched 2026-10-10 · https://www.mathopt.org/api/awards/lagrange-prize · primary
- T30 · University of Dundee press office, "International recognition for Dundee maths research" · June 2006 · https://app.dundee.ac.uk/pressoffice/contact/2006/june/maths.html · primary (institutional; quotes Fletcher)
- T31 · Georgia Tech CSE Seminar, "A Tale of Two Problems: Integer and Nonlinear Optimization" (abstract and bio) · 10 Mar 2009 · https://hg.gatech.edu/node/52545 · primary
- T32 · W. Hager (ed.), "COAP Best Paper Awards" list · capture 8 Aug 2015 · https://web.archive.org/web/20150808195458/http://users.clas.ufl.edu:80/hager/coap/Best/ · primary
- T33 · S. Leyffer, S. Mahajan, "Improving Earth System Predictability with Artificial Intelligence", SIAM News 55(6) · 6 Jul 2022 (capture 17 Jul 2022) · https://web.archive.org/web/20220717233752/https://sinews.siam.org/Details-Page/improving-earth-system-predictability-with-artificial-intelligence · primary (coauthored)
- T34 · MINOA Doctoral School 2021, online, 21–29 June 2021 (programme overview, speakers) · capture 17 Jun 2021 · https://web.archive.org/web/20210617234210/https://conference2.aau.at/event/79/ · primary
- T35 · Arizona State University, School of Mathematical and Statistical Sciences, "SIAM Student Chapter at ASU Talk Series with Sven Leyffer" · 2 May 2025 · https://math.asu.edu/node/9351 · primary
- T36 · UC Merced SIAM Student Chapter, flyer for a CRLC virtual talk by S. Leyffer · 3 Nov 2021 · https://siam.karlin.mff.cuni.cz/files/events/284_CRLCTalk_SvenLeyffer.pdf · primary
- T37 · S. Leyffer, J. Linderoth, J. Luedtke, A. Miller, T. Munson, "Applications and algorithms for mixed integer nonlinear programming", J. Phys. Conf. Ser. 180 (2009) 012014 (abstract page) · DOI 10.1088/1742-6596/180/1/012014 · primary

Secondary (T38–T40)

- T38 · Mathematics Genealogy Project, "Sven Leyffer" (id 282807) and "Roger Fletcher" (id 52148) · fetched 2026-10-10 · https://www.mathgenealogy.org/id.php?id=282807 ; https://www.mathgenealogy.org/id.php?id=52148 · secondary
- T39 · Wikipedia, "Sven Leyffer" (raw wikitext; last revision 26 Dec 2025) · fetched 2026-10-10 · https://en.wikipedia.org/wiki/Sven_Leyffer · secondary
- T40 · WebSearch result lists, 3 queries on 2026-10-10 ("Sven Leyffer" 2026 talk; OP26 Edinburgh; "Argonne Distinguished Fellow"); used only to find T22, T26, T35 and T36, which were then fetched directly · secondary (leads only)

- T41 · Springer landing page of R. Fletcher, S. Leyffer, "Solving mixed integer nonlinear programs by outer approximation", Math. Program. 66 (1994) 327–349 (abstract) · fetched 2026-10-10 · https://link.springer.com/article/10.1007/BF01581153 (DOI 10.1007/BF01581153) · primary (listed last because it was added after the audit)

Leads read but not counted as sources: research notes 01 (publications) and 04 (mentorship) of this run, and a sibling agent's saved copies of SIAM News issues (2017–2023).
