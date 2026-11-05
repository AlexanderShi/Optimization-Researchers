# Robert E. Bixby · Research note 04: students, collaborators and mentorship

| Field | Value |
|---|---|
| Researcher | Robert E. Bixby (lp-team member; also seated as a guest in the MILP Team) |
| Dimension | Research agent 04 of 06 (framework §二): students and collaborators. Supervision style, group habits, lab and company culture, tacit knowledge |
| Lens | Decision and measurement craft for LP and MIP (team.json). Matroid and TSP work are context only |
| Research date | 2026-11-05 |
| Sources consulted | 53 used: 18 primary (Bixby's own or co-authored texts, decks and talk transcripts) and 35 secondary (students', colleagues', prize committees' and databases' accounts). 7 more were tried and not reached (see Gaps) |
| WebSearch calls | 7 of the 7 allowed. Everything else was fetched with curl or WebFetch from known URLs and repository APIs |
| User-supplied material | None. `references/sources/papers`, `essays` and `software` hold only `.gitkeep`; `publications/` holds the generated OpenAlex harvest, which was read; `private/` was not opened. `talks/` holds four caption transcripts that another research agent saved during this run (not user-supplied, not speaker-checked); they were read and are cited as P15–P18 |
| Quotation policy | This note carries one short verbatim quote, marked as such. Everything else is paraphrase with a page or slide locator and is never put in quotation marks. Every source is open, so the wording can be checked at the locator |

**Tags.** [stated] = Bixby's own words. [practice] = what a dated record shows was done (a thesis, a report, a run). [observed] = what another person reports about him. [inferred] = this agent's reading, to be tested. "primary" = Bixby's own or co-authored text; "secondary" = anyone else's account (first-hand for its author, secondary about Bixby). L1–L7 = the seven layers of framework §一; this note serves mainly L7 (organisation), with L4 (execution) and L5 (judging results).

**Page conventions.** Optima 101: printed page = PDF page. OR 2002: printed page = PDF page + 2. Documenta 2012: printed page = PDF page + 106. Hausdorff 2022 deck: cited by the slide number in the footer (footer = PDF page + 1 from PDF p. 2 to p. 16, + 2 from p. 18). Rice theses: printed page where one is visible, otherwise PDF page.

---

## 0. Authorship and role labels this note supports (they must survive into the skill)

- **CPLEX code, dated.** [stated, primary, co-authored] In a Rice report dated November 1989 (inner date 1 December 1989), written with Mark Schwabacher, a footnote says the optimization routines in CPLEX were written by Bixby (TR89-16, PDF p. 6). [stated, primary] Optima 101: he did all of the development for the first release in 1988 (p. 3); he was still doing development and was still an academic at the 1997 sale to ILOG (p. 4); at Gurobi he did absolutely no development, only a great deal of testing and of pressing the developers about bad behaviour (pp. 4–5). [stated, primary, caption transcript] In the 2015 CO@Work lectures he says he himself implemented in CPLEX the LU factorization of a 1990 paper by Uwe and Leena Suhl, after talking to Uwe Suhl, and that it is more or less what is still used, also in Gurobi (P16, Part 3). The paper is presumably Suhl & Suhl, *Computing Sparse LU Factorizations for Large-Scale Linear Programming Bases*, ORSA J. Comput. 2(4):325–335, 1990, DOI 10.1287/ijoc.2.4.325 [identification inferred from his description of a dynamic Markowitz method]. In 2023, asked whether he coded the first version of the callable-library CPLEX himself, he says of course he did (P15).
- **When his CPLEX work ended, by a colleague's account.** [observed, secondary] Irv Lustig of ILOG, in a comment of 13 April 2008 on Michael Trick's blog, wrote that Bixby had not worked on CPLEX for four or five years and had been working, like Rothberg, on ILOG's FPO product. That places the end of his CPLEX work at about 2003–04. It neither shows nor refutes that he wrote the CPLEX 5.0–7.1 changes; OR 2002 p. 14 credits Gu, Lustig, Rothberg and Wunderling with fundamental contributions to the CPLEX LP algorithms.
- **MIP, by his own account.** [stated, primary] Optima 101 p. 4: he did little MIP work himself; the cuts and most of presolve were Gu's; node presolve, probing and bounds strengthening were Rothberg's, and in the same passage the first heuristics; later contributions are Achterberg's; strong branching came out of the TSP work, surfaced in a discussion with Bill Cook, and he put it into CPLEX; he spent much time tuning the CPLEX library to serve the TSP code. The first parallel barrier was Rothberg's, brought in through the SGI partnership; he himself made a couple of observations that sped up crossover (p. 3). [stated, primary, caption transcript, 2023] The first CPLEX MIP solver was planned after Todd Lowe saw that customers kept asking for MIP (around 1989, by his uncertain dating); the developer primarily responsible was Mary Fenelon, with his assistance, and an outside contractor was involved in the first version (P15; the contractor passage is redacted in the saved excerpt). Strong branching: Cook presented the idea, and Bixby, having the CPLEX source, implemented it efficiently (P15), which fits Optima 101 p. 4. He says he does not know all the details of CPLEX's later dynamic search (P15), and that he had no access to CPLEX after the 2008 departure, so his later testing used Gurobi (P17).
- **A measurement is not authorship.** [stated, primary] The late-2007 run of twelve CPLEX releases (1.2 to 11) on 1892 MIPs is told in the first person singular (Documenta 2012 p. 116); the Gurobi release-to-release figures are told in the first person plural (p. 118). By Lustig's account he was off the CPLEX team when he ran the 2007 test. A progress number measured on a code is not evidence that he wrote what produced it.
- **Third-party credit beyond his own texts.** [observed, secondary] The 2004 INFORMS Impact Prize citation says he discovered how to implement stable versions of steepest-edge pricing for the dual simplex. His own texts credit dual steepest edge to Forrest and Goldfarb (OR 2002 p. 8) and, in 2022, credit Forrest's success with primal Devex and a simpler steepest-edge suggestion from Goldfarb (Hausdorff 2022 slide 23). The skill should keep his own texts as the label (see Contradictions).
- **Living status and present role: not established; nothing here states either.** This agent's own searches found no dated trace after September 2022 (dated traces seen: ECCO deck of May 2017, Toronto seminar of March 2021, whose bio lists a Gurobi board seat as of then, and the Hausdorff School deck of September 2022). The `talks/` folder, filled by another agent during this run, holds a caption transcript of a long interview uploaded to YouTube on 7 December 2023, whose recording is dated to 2023 only by inference (P15). An upload date is not evidence of present role or of living status.

---

## 1. The supervision record

### 1.1 Formal advisees (MGP record 14993: 9 PhD students, 38 descendants; read 2026-11-05)

| Student | Degree, place, year | Thesis (as recorded) | Bixby's role | Identifiers | What it shows for this lens |
|---|---|---|---|---|---|
| Donald K. Wagner | PhD, Northwestern, 1983 | An Almost Linear-Time Graph Realization Algorithm | sole advisor | MGP 67627 | Matroid era. The topic became Bixby & Wagner, *An Almost Linear-Time Algorithm for Graph Realization*, Math. Oper. Res. 13(1):99–123, 1988, DOI 10.1287/moor.13.1.99. Thesis not read |
| Collette R. Coullard | PhD, Northwestern, 1985 | Minors of 3-Connected Matroids and Adjoints of Binary Matroids | sole advisor | MGP 67628 | Matroid era. Not read |
| Arvind Rajan | PhD, Northwestern, 1986 | Algorithmic Applications of Connectivity and Related Topics in Matroid Theory | sole advisor | MGP 143732 | Matroid era. Two joint Rice reports with Bixby (Nov 1986, hdl 1911/101610; Oct 1987, hdl 1911/101632; metadata only). Thesis not read |
| Sanjay Saigal | PhD, Rice, 1991 | Optimizing over the cut cone: a new polyhedral algorithm for the maximum-weight cut problem | sole advisor | MGP 39318; hdl 1911/16481 | CPLEX as the embedded LP engine; degeneracy; Cray time through John Gregory (§3, §4.2) |
| Zhijun Wu | PhD, Rice, 1991 | A subgradient algorithm for nonlinear integer programming and its parallel implementation | co-adviser with J. E. Dennis Jr. | MGP 29587; hdl 1911/16495 | Parallel branch and bound on an NCUBE, with the student's own sequential simplex (abstract, PDF p. 7) |
| Eva K. Lee | PhD, Rice, 1993 | Solving structured 0/1 integer programs arising from truck dispatching scheduling problems | sole advisor | MGP 39317; hdl 1911/16642; report TR93-18, hdl 1911/101796 | Texaco data; CPLEX callable library; joint paper Bixby & Lee, *Solving a Truck Dispatching Scheduling Problem Using Branch-and-Cut*, Oper. Res. 46(3):355–367, 1998, DOI 10.1287/opre.46.3.355 |
| Shireen S. Dadmehr | PhD, Rice, 1995 | An efficient simplex-based method for solving large linear programs | sole advisor | MGP 39316; hdl 1911/16813; report TR95-15, hdl 1911/101860 | Crash bases for staircase and block-angular LPs, built on his initial-basis method; CPLEX 3.0 and OSL baselines (§3) |
| Gwyneth Owens Butera | PhD, Rice, 1997 | The solution of a class of limited diversification portfolio selection problems | co-advisor with Dennis | MGP 29594; hdl 1911/19140 | Branch and bound for a mixed-integer QP; finished far from Rice (§2) |
| Cassandra M. McZeal | PhD, Rice, 1999 | Reoptimization in interior-point methods with application to integer programming | primary advisor and committee chairman, Yin Zhang co-chairman | MGP 37969; hdl 1911/19416; report TR99-28, hdl 1911/101933 | Interior-point warm starts inside branch and bound, CPLEX 4.0 on SGI, MIPLIB; co-author of MIPLIB 3.0 (§3) |

Also formally his: **Anne Kilgore**, MA, Rice (title page November 1993; repository year 1994), *Very large-scale linear programming: a case study in exploiting both parallelism and distributed memory*, hdl 1911/13851. The repository lists Bixby as advisor and the title page lists him as committee chairman, but her acknowledgments name Virginia Torczon as her advisor (PDF p. 7; see Contradictions).

[practice, secondary] No PhD advisee after 1999 appears in MGP or in the Rice repository's advisor field. The title pages of McZeal and Rich (both May 1999) already list him as Noah Harding Professor Emeritus. [stated, primary, caption transcript] The reason, by his 2023 account: when it was his turn to chair the department, CPLEX was doing well, so in 1998 he gave up tenure with the dean's help rather than keep a tenured post as security while a business took his time; Rice counts him as retired in 2000, and he expected to disengage slowly (P15). This is the organisational decision that ends his PhD supervision.

[inferred] The supervision record turns with his research: the three Northwestern theses (1983–86) are matroid theory; all six Rice PhD theses (1991–99) are computational LP or IP. Of the seven Rice degrees he advised or chaired (six PhDs and Kilgore's MA), five are shown to run on or against CPLEX (Saigal, Lee, Kilgore, Dadmehr, McZeal); Wu wrote his own simplex, and Butera's thesis was not checked for CPLEX. Three Rice PhDs were co-advised with numerical analysts (Dennis twice, Zhang once).

### 1.2 Committee, reviewer and visitor roles

| Person | Degree, year | Main advisor | Bixby's role | Identifier | What they record about him |
|---|---|---|---|---|---|
| Rodolfo Elizondo | MA, Rice, Sept 1993 | E. Andrew Boyd (co-chair with Richard Tapia) | committee member | TR93-48, hdl 1911/101818 | He shared his insight into OR, both the theory and the harder-to-pin-down practical side (PDF p. 7). The thesis cites a 1993 personal communication from him on a column-generation effect seen in large TSPs (ref. 34; context p. 30) |
| Clifford N. Click Jr. | PhD, Rice CS, Feb 1995 | Keith D. Cooper (chair) | committee member | TR95-252, hdl 1911/96451 | Thanks him for his large numerical C codes (PDF p. 3); which codes is not stated |
| Ulrich Kremer | PhD, Rice CS (report Oct 1995) | Ken Kennedy | committee member | TR96-261, hdl 1911/96457 | He gave the student insight into 0-1 integer programming (PDF p. 5). A joint 1994 Bixby–Kennedy–Kremer paper exists in OpenAlex, but its venue could not be verified, so it is not listed as an entry |
| Jennifer L. Rich | PhD, Rice, May 1999 | William J. Cook (chairman) | committee member | TR99-11, hdl 1911/101916 | His linear programming class in her first semester at Rice started her interest in OR (PDF p. 4) |
| Sanjeeb Dash | PhD, Rice, March 2001 | William J. Cook (chair) | committee member (with Vardi and Applegate) | TR01-08, hdl 1911/101970 | Thanked with Applegate, Dean and Zhang for discussions and insights (PDF p. 5) |
| Timothy A. Redl | Rice report Jan 2003; PhD May 2004 | Nathaniel Dean and Richard Tapia (co-chairs) | not on the committee | TR03-01, hdl 1911/101998; TR04-07, hdl 1911/102019 | 2003: thanked with Dean for guidance and advice (PDF p. 11). 2004: thanked for letting him use the OPL Studio constraint-programming software (PDF p. 4) |
| Benjamin McClosky | PhD, Rice, April 2008 | Illya V. Hicks (chair) | committee member | TR08-13, hdl 1911/102093 | Title page only (PDF p. 1) |
| Caleb Fast | MA, Rice, April 2014 | Illya V. Hicks | committee member | hdl 1911/76721 | Thanked with Tapia and Cooper for helpful guidance (PDF p. 5) |
| Tobias Achterberg | Dr. rer. nat., TU Berlin, defence 12 July 2007 | Martin Grötschel (first Berichter) | second Berichter (reviewer) | TU Berlin depositonce (URL in Sources) | Title page (PDF p. 1). The acknowledgments (pp. ix–x) do not mention Bixby; they thank the author's new employer ILOG and two ILOG proof-readers, Lloyd Clarke and Zonghao Gu |
| Petra Mutzel | visiting project, Rice report May 1990 | — | suggested the problem | TR90-29, hdl 1911/101693 | She thanks him for suggesting the problem and helping with the research (PDF p. 24). Her 2022 CV slide lists study at Augsburg 1983–1990 and no Rice post, so she was a student when she wrote it [inferred]. She and Bixby were both speakers at the 2022 Hausdorff School |

### 1.3 Co-authorship with students and junior visitors [practice, primary]

- Mark Schwabacher, *Solving Linear Programs with Two Processors*, Rice TR89-16, Nov 1989, hdl 1911/101665. Schwabacher's status at the time is not stated.
- Ronni R. Indovina (named among the CAAM graduate students in Dadmehr's acknowledgments and as a computer-lab comrade in Elizondo's), with E. Andrew Boyd: *A Test Set of Real-World Mixed Integer Programming Problems*, Rice TR91-38, Nov 1991, hdl 1911/101739.
- Shireen Dadmehr and Indovina, with Boyd: *The MIPLIB Mixed Integer Programming Library*, Rice TR92-36, Nov 1992, hdl 1911/101776.
- Eva K. Lee: Rice TR93-37 (Sept 1993, hdl 1911/101808), published as Oper. Res. 46(3):355–367, 1998, DOI 10.1287/opre.46.3.355. The acknowledgment says the work was completed while Lee was at Rice (PDF p. 23). After her PhD she co-authored the parallel MIP study with Bixby, Bill Cook and Alan Cox (Rice CS): *Computational experience with parallel mixed integer programming in a distributed environment*, Annals of OR 90:19–43, 1999, DOI 10.1023/a:1018960631213 (bibliographic record only; not read).
- Cassandra M. McZeal, with Sebastian Ceria and Martin Savelsbergh: *An Updated Mixed Integer Programming Library: MIPLIB 3.0*, Rice TR98-03, Feb 1998, hdl 1911/101898.
- [inferred] Students were brought in on test-set curation (all three MIPLIB reports read here have a Rice student co-author) as well as on algorithms.

---

## 2. Supervision style, according to the students (all secondary)

**S1. Patient discussion, reading drafts, implementation ideas.** [observed, secondary] According to Eva Lee (thesis acknowledgments, 1993, TR93-18 PDF p. 7), Bixby introduced her to linear and combinatorial optimization, discussed her work with her patiently, read her research reports, suggested improvements and gave her implementation ideas, and served as her model of a good researcher and teacher. According to Zhijun Wu (1991, acknowledgments, PDF p. 8), his co-adviser Bixby spent much time listening to his reports and giving suggestions; Wu learned most of his LP and combinatorial optimization from him and enjoyed all his classes. **Caution:** Wu's thanks to his main adviser Dennis on the same page use nearly the same phrases that Lee used two years later about Bixby (patient discussion, reading papers, a field he introduced). The phrasing looks like a shared Rice template, so it is weak evidence of anything specific to Bixby.

**S2. His teaching was the door into the field.** [observed, secondary] Four students say this: Lee (introduced to LP and combinatorial optimization), Wu (learned LP from his classes), McZeal (introduced to OR and urged to dive in; TR99-28 PDF p. 4), Rich (his LP class in her first semester; TR99-11 PDF p. 4). [stated, primary] His own account says the code that became CPLEX began as classroom code: he started by implementing elementary algorithms for teaching and wanted computation in his LP courses (OR 2002 p. 3; Optima 101 p. 2; Hausdorff 2022 slide 10 dates the classroom LP code to 1983). He also wrote course-style notes, *Notes on Combinatorial Optimization* (Rice TR87-21, Oct 1987, hdl 1911/101631: greedy, shortest paths, polyhedral combinatorics, the TSP polytope, ellipsoids; their teaching purpose is not stated in the pages read).

**S3. Freedom and confidence.** [observed, secondary] According to Gwyneth Butera (1997, acknowledgments, PDF p. 7), her committee gave her the freedom to work on her problem and find out for herself what research is like, and Bixby in particular believed in her abilities when she did not. McZeal (1999) credits him with urging her to dive in.

**S4. The practical side of OR.** [observed, secondary] Elizondo (1993) singles out his insight into the practical side of OR; Kilgore (1993) says his knowledge of CPLEX and LP proved invaluable (PDF p. 7); Dadmehr (1995) thanks him for valuable comments along the way (TR95-15 PDF p. 9).

**S5. Domain expert for other groups' students.** [observed, secondary] Compiler students in Rice CS had him on their committees for integer programming (Kremer) and for test inputs (Click: his large numerical C codes). A timetabling student used ILOG's OPL Studio through him (Redl 2004). A Cook student thanks him for discussions (Dash 2001).

**S6. Formal role and day-to-day role can differ.** [observed, secondary] Kilgore's MA lists him as chairman, but her acknowledgments name Virginia Torczon as the advisor who kept her on track; Dennis suggested the research (PDF p. 7).

**S7. Supervision at a distance.** [observed, secondary] Dadmehr calls herself a long-distance student (TR95-15 PDF p. 9). Butera thanks Dennis for backing her wish to finish while far from Rice, and thanks two people for handling the administrative side of being about a thousand miles from the Rice community (PDF p. 7). [inferred] Both late-era PhDs finished away from Rice during the years when Bixby was also running CPLEX Optimization (to 1997) and then working at ILOG.

**S8. What the students do not record.** No acknowledgment read here mentions group meetings, reading groups, code reviews, a lab guide or any routine of his. The evidence is of one-to-one advising plus a shared computational environment (§3).

---

## 3. Group habits: what the theses show the students actually did (practice)

**H1. Build on, and measure against, the advisor's production code.** [practice, secondary sources, dated]
- Saigal (1991) solved his LPs with the CPLEX Linear Optimizer, used its ability to restart from the previous optimal basis after column additions and right-hand-side changes, kept the default settings except pricing, and tested hybrid (reduced cost plus devex) against pure partial pricing on four instances: partial pricing won three of four (p. 47, PDF p. 60; Sun 4/490).
- Lee (1993) built a branch-and-cut system with CPLEX as the LP solver through its callable library and mixed-integer library, with tables of primal and dual pricing strategies (TR93-18 PDF pp. 47, 78).
- Kilgore (1993) ported CPLEX to an Intel distributed-memory multiprocessor to keep the whole 12,753,313-variable airline crew-scheduling LP in memory, and tested a greatest-decrease variant, an old idea she says had never been tried on LPs of significant size (abstract, PDF p. 6; Caltech machines, PDF p. 7).
- Dadmehr (1995) built crash bases for staircase and block-angular LPs from his initial-basis algorithm (TR95-15 PDF p. 41, citing Bixby, *Implementing the Simplex Method: The Initial Basis*, ORSA J. Comput. 4(3):267–284, 1992, DOI 10.1287/ijoc.4.3.267) and compared her code with CPLEX 3.0 primal, dual and barrier and with OSL (PDF p. 65).
- McZeal (1999) studied interior-point reoptimization inside branch and bound with CPLEX 4.0 on SGI Power Challenge machines and MIPLIB instances (TR99-28 PDF p. 53).
- Schwabacher and Bixby (1989) modified CPLEX itself to run optimization and refactorization on two processors of a Sequent Symmetry (TR89-16 PDF p. 6).
- [inferred] The pattern: students and visitors explored variants of ideas that mattered to a production LP or MIP code (sifting, parallel refactorization, crash bases, parallel simplex, interior-point warm starts), on real instances, with CPLEX as engine and baseline. Whether this was a deliberate pipeline into the product is not shown.

**H2. Real industrial instances, released with credit.** [practice, primary and secondary]
- Lee's instances came from Texaco: a Texaco employee explained the dispatching system and obtained the test problems, and Texaco allowed their release (thesis PDF p. 7; Bixby & Lee report PDF p. 23).
- Kilgore's crew-scheduling instance has 12,753,313 variables, the column count of the 1989 American Airlines challenge model (Kilgore abstract; Hausdorff 2022 slide 15). Mutzel's test problems are named aa… (TR90-29 contents), presumably from the same source [inferred].
- Saigal computed on a Cray through the support of John Gregory of Cray Research (acknowledgments, PDF p. 7).
- The MIPLIB reports name an originator, a formulator and a donor for every model and put much of the credit with them (TR92-36 PDF p. 4). They invite new models and new proofs of optimality (PDF p. 7). The 1991 test set marks each reported optimum as verified, not optimal, or reported optimal but not yet verified by the authors (TR91-38 PDF p. 5). The stated motive is that the lack of real models available to researchers held integer programming back, as netlib and TSPLIB had shown for LP and the TSP (PDF p. 3).

**H3. Losses and negative results are written down.** [practice, secondary]
- Dadmehr reports that her method never beats the CPLEX barrier on the staircase LPs (TR95-15, section 5.5).
- McZeal's abstract concludes that fast reoptimization cannot always be expected from interior-point methods in branch and bound (TR99-28 PDF p. 3).
- Saigal's algorithm declares failure when no violated cycle inequality is found, because neither branch and bound nor other facet classes were implemented; the thesis adds that failure is rare in its tests (p. 46).
- The 1989 two-processor report gives 73% to 92% of single-processor time and then names the niche cases where the idea still pays (TR89-16 PDF pp. 6–7).

**H4. Shared computational environment.** [observed, secondary] Elizondo thanks his computer-lab comrades, among them Indovina and Kilgore (PDF p. 7). Kilgore, Elizondo and McZeal each thank the same Rice computing-support person, who built Kilgore's data sets and managed her 530 MB of data. Funding lines in the reports: NSF CCR-8815914 and AFOSR-90-0273 to Rice (TR91-11, TR91-38); the Center for Research on Parallel Computation for Mutzel's 1990 visit (TR90-29 PDF p. 2); AFOSR F49620-92-J-0053 for the truck-dispatching work (TR93-37 PDF p. 23).

**H5. One hard instance serves many people for years.** [practice] The 1989 American Airlines LP (837 rows, 12,753,313 columns) runs through the 1989 challenge team, the 1992 case study, Kilgore (1993) and probably Mutzel (1990), and the 2022 deck still shows its 1989 iteration log (Hausdorff 2022 slides 15–16 and the unnumbered table that follows). Slide 19 then times primal, dual, barrier and sifting on an 837-row instance with 1,322,797 columns, which the deck does not identify further. The Cray fleet model (degen4, later called LAU2) runs from about 1989 to the 2022 deck (OR 2002 p. 8; slides 22–24).

---

## 4. Collaborators and company culture

### 4.1 How he learned: from colleagues and failing instances, not from the literature (L4)

- [stated, primary] At Northwestern, Bob Fourer, a colleague with practical LP experience, passed on much computational knowledge in informal conversation (OR 2002 p. 3). In 2015 he says he had hired Fourer and that Fourer made him aware of the issues (Optima 101 p. 2), including the Harris ratio-test idea behind bound shifting (p. 4).
- [stated, primary] For about two years Tom Baker of Chesapeake Decision Sciences kept sending him LPs on which his code broke; he fixed each in turn without looking in the literature, which was not his field (OR 2002 p. 3; Optima 101 p. 2, where he calls it his hobby and says Baker knew how to provoke him).
- [stated, primary] He paid David Applegate to improve the data structures of his network code (Optima 101 p. 2), years before their TSP collaboration, which he calls one of his most fruitful (OR 2002 p. 4).
- [stated, primary, caption transcript] When Baker asked for an LP code in C (about 1984, already at Rice), he had a computer-science student who knew C convert his Fortran code, and says that is how he learned C, the language he has programmed in ever since (P15). OR 2002 p. 3 says he converted it himself (see Contradictions).
- [stated, primary] A colleague in Rice's business school, Randy Batsell, suggested the growth-rate analysis of solve times (straight-line against parabolic fits) in OR 2002 (observation p. 9, credit in endnote 8, p. 14).

### 4.2 Problem suppliers, challenge teams and advice he did not take (L2, L5)

- [stated, primary] The 1989 American Airlines challenge was attacked by a five-person team across institutions: Bixby, Irv Lustig, Roy Marsten, Dave Shanno and John Gregory of Cray. They built a special algorithm, sifting, which he credits to an idea of John Forrest, ran it on a Cray Y-MP after considerable experimentation, and came away with the first fast crossover (Hausdorff 2022 slides 15–16; published as Oper. Res. 40(5):885–897, 1992, DOI 10.1287/opre.40.5.885).
- [stated, primary] The fleet model (degen4/LAU2) was a challenge from United Airlines that reached him through John Gregory of Cray Research, with the promise of computer sales if it was solved (Hausdorff 2022 slide 22; Optima 101 p. 3). When CPLEX stalled on it, Gregory reported a fast interior-point (OB1) solve, and the deck's next bullet under Gregory's step records a recommendation to give up on simplex. Bixby instead solved the explicit dual with the primal, implemented the dual simplex, then, prompted by Forrest's success with primal Devex, dual steepest edge, and then the simpler variant Goldfarb suggested (slide 23; OR 2002 p. 8). Advice from a collaborator that he did not take is part of how the dual became CPLEX's main engine.
- [stated, primary, caption transcript] Instance hunting at a meeting, 1999: at a meeting that Richard O'Neill of FERC convened to bring the power industry together with MIP researchers (Bixby and Sebastián Ceria were the researchers invited), a speaker presented the California seven-day unit-commitment model as hopeless as a MIP. Bixby pursued him all day for the instance, received it through a student, solved it to proven optimality with CPLEX 6.5 in 22 minutes on a DEC Alpha, and presented the result the next morning; he dates the use of MIP in that field from this episode (P15). Not corroborated by any other source read here.
- [stated, primary] A student's problem changed the product: his graduate student Saigal's max-cut LPs were so degenerate that he had to add something to the code or Saigal could not proceed, and that is when perturbation entered CPLEX (Optima 101 p. 3). **Partial corroboration:** Saigal's thesis names degeneracy as one of the two basic implementation issues and explains it by the zero right-hand side (pp. 55–56); it handles it by solving the explicit dual formulation with the primal simplex. The pages read (pp. 46–47, 55–57, 67) do not mention perturbation; the rest of the thesis was not read.

### 4.3 Building and keeping a team (L7)

- [stated, primary] To start the company he recruited Janet Lowe, his first choice among the two best students from his business-school modelling class, and gave her and her husband Todd Lowe 49 percent of the business, reasoning that good people would not stay committed on salary alone (Optima 101 p. 3). In his closing advice he repeats the point: get good people who are invested in the business (p. 6). This is said twice in one interview; no third statement was found.
- [stated, primary] Credit within the company: Todd Lowe pushed for MIP because customers needed it (p. 3); the 1997 sale to ILOG was Todd and Janet Lowe's idea (p. 4); OR 2002 thanks the Lowes for turning a collection of algorithms into a product (p. 14).
- [observed, secondary] The 2004 Impact Prize committee says he built a first-rate team of developers to bring current research into the code. Ed Rothberg's INFORMS profile of Gurobi (undated; about 2013 by its own count of five years since founding) says he developed the first CPLEX versions himself, then built and led the team, and at ILOG was CPLEX Development Team manager, president of the Technical Advisory Board and finally general manager of the Semiconductor Business Division. Michael Trick (13 April 2008) mentions a Chief Science Officer role and guesses a CPLEX development team of about 15.
- [inferred, from stated and observed facts] Several developers came out of collaborations: Lustig was on the 1989 challenge team (he co-wrote the OB1 interior-point code) and later joined CPLEX, where Bixby credits him with presolve (Optima 101 p. 3); Rothberg came through the SGI partnership on parallel barrier (Optima 101 p. 3; Hausdorff 2022 slide 20 reports that story as Rothberg tells it) and joined the CPLEX team in 1997 (Rothberg's profile); Gu came from LINDO Systems in 1998 (same profile). How Gu was recruited is not recorded.
- [observed, secondary] Lustig (2008) adds that founders of acquired companies rarely stay more than four years, that ILOG was fortunate Bixby stayed more than ten, and that Bixby, Rothberg and Lustig himself had all been replaced by new developers.
- [stated, primary] At Gurobi he joined, not started: within three or four weeks of leaving ILOG, Gu and Rothberg were planning something together, and he contacted them and asked whether he could help (Optima 101 p. 4). The 2023 interview tells it the same way: he left independently, for reasons close to theirs, then asked whether they would include him (P15). Rothberg's profile presents the three as co-founders in 2008, and a 2020 Gurobi clip has the three getting together and deciding quickly (P18).
- [stated, primary, caption transcript] The TSP team, by his 2023 account: Cook, Applegate and Chvátal came together around 1990, near the TSP 90 meeting he organized at Rice; Cook brought him the idea that became strong branching, he implemented it efficiently in CPLEX because he had the source, showed the results, and the team then took him on as its LP specialist (P15). He describes Cook as structured and careful, a planner who follows his plan, and scrupulous that every contributor gets credit, and Applegate as able to grasp a non-trivial idea while hearing it and compute with it almost at once (P15). This is his own role description, not a division of roles agreed by the four authors.

### 4.4 Division of labour and credit-giving habits (L6, L7)

- [stated, primary] OR 2002 p. 14 names Gu, Lustig, Rothberg and Wunderling as having made fundamental contributions to the CPLEX LP algorithms, and Mary Fenelon, John Gregory and Ed Klotz for persistent and significant insights. Endnotes cite private communications from John Tomlin and John Gregory (p. 14).
- [stated, primary] Documenta 2012 thanks Robert Ashford, John Gregory, Ed Rothberg, Max Shaw and John Tomlin for e-mail exchanges behind the history (p. 118). The 2022 deck attributes a story to Rothberg's telling (slide 20). [inferred] He checks history with the people who were there and says so.
- [practice, primary] Team papers from the CPLEX years carry the team's names: Bixby, Fenelon, Gu, Rothberg, Wunderling, *MIP: Theory and Practice — Closing the Gap*, System Modelling and Optimization (IFIP), 2000, DOI 10.1007/978-0-387-35514-6_2; the same five, *Mixed-Integer Programming: A Progress Report*, The Sharpest Cut, 2004, ch. 18, DOI 10.1137/1.9780898718805.ch18; Bixby and Rothberg, Annals of OR 149:37–41, 2007, DOI 10.1007/s10479-006-0091-y; Achterberg, Bixby, Gu, Rothberg, Weninger, *Presolve Reductions in Mixed Integer Programming*, INFORMS J. Comput. 32(2):473–506, 2020, DOI 10.1287/ijoc.2018.0857 (the paper he says in October 2015 they were writing; Optima 101 p. 6). In MIPLIB 2010 (Math. Prog. Comp. 3(2):103–163, 2011, DOI 10.1007/s12532-011-0025-9) he is one of many co-authors.
- [inferred, weak] Dieter Weninger, co-author of the 2020 presolve paper, taught at FAU Erlangen in 2023 (an FAU course file surfaced by a search; the paper's own affiliations were not checked). That fits Bixby's yearly Erlangen teaching (§4.8), but no source links the two.

### 4.5 After he stopped coding: tester, critic, measurer (L4, L5)

- [stated, primary] At Gurobi he did no development but a great deal of testing, and kept asking the developers why the code behaved badly here or there; what he really wanted to do was run the business (Optima 101 pp. 4–5). In 2015 he describes his role as half-time chairman and Chief Strategy Officer who manages the sales team, runs the code all the time and complains as he always has (p. 6). These are dated (October 2015) statements, not present roles.
- [stated, primary] Gurobi's test library: about 600 models gathered from the web within two days of starting, NEOS a major source, about 10,000 by 2015, of which the developers' real test set is about 3,500 (Optima 101 p. 6). The 2017 ECCO deck shows a Gurobi MIP library of 3,550 models (slides 34–35).
- [observed, secondary] When Rice colleagues compared their algorithm against CPLEX 6.5.2, three of their six test problems came from a private CPLEX test collection, cited to a 2001 private communication from him, and the same citation backs their caveat that CPLEX 7.0 with a well-chosen parameter setting solves the test problem smallm very quickly (Gao & Zhang, TR02-12, PDF pp. 12, 14).
- [observed, secondary] A colleague cited his steepest-edge results in 1991 as unpublished computational results (Boyd, TR91-21, PDF p. 6 and reference 2).

**Group habits inside the companies, as he describes them** (all [stated], caption transcripts, not speaker-checked):
- CPLEX, early 1990s: the MIP versions under development had colour names (blue MIP, green MIP), and every few months the team met at a whiteboard to review progress. He judged that most MIP progress in that period came from the LP code, above all the maturing dual simplex, until Gu and Rothberg joined in 1997–98 and, in his phrase, mined the theoretical backlog in one release (P15; compare ECCO 2017 slide 32 and Documenta 2012 p. 117).
- Gurobi, 2021: a test bed that is constantly updated and, he says, biased towards the hard models customers send and towards models solvable in reasonable time; each test run with five random seeds that are changed over time, summarized by geometric means; test machines checked regularly for comparability and kept free of other users, so that very small improvements can be measured (the captions give 0.2 without a unit); about 200 machines running comparisons; an idea passes four or five filters, and perhaps one idea in ten shows promise; developers who make first implementations very quickly (P17, Q&A).
- When an audience question in 2021 went beyond what he knew (callbacks), he said he would ask Rothberg rather than answer (P17), consistent with his account of having no development role.

### 4.6 What colleagues observed about his craft (secondary)

- [observed] Martin Grötschel (Optima 101 pp. 6–7) calls LP implementation a craft learned by experiment and imitation, and reads the interview as showing that Bixby learned it by studying failures, learning on the run, adapting, running small experiments and taking advice from others; he adds that Bixby humbly plays down his role.
- [observed] Bill Cook (Optima 101 p. 7) says the software revolution rested on methodical attention to detail, and gives Bixby's motto in his own words. Verbatim, the only quote in this note: "if you see something, then fix it!" Cook glosses it as: when numerical results are off, do not ignore or work around them; find the problem. Cook adds, as an anecdote of low weight, that Bixby sleeps very little and does his hard debugging while others sleep, and describes him and Applegate levelling a woodworking machine for hours, millimetre by millimetre.
- [observed] The Optima editors' caption (p. 5) and Grötschel both use his woodworking as an image of his attention to detail in code. This is an analogy, not evidence of method.
- [observed] Michael Trick (2008) calls him the most influential person in the field over the previous fifteen years, mainly through one code.
- [observed] Thorsten Koch's 2004 TU Berlin thesis re-ran a classical hard problem (Steiner tree packing) to test Bixby's claim of dramatic MIP progress (p. 123) and found his own speed-ups compatible with Bixby et al. 2000 and Bixby 2002, while calling the hardware factor a gross approximation (p. 139). An outside check, by the researcher who later led MIPLIB 2010, on which Bixby is a co-author.

### 4.7 The academia–industry boundary and field-building (L1, L7)

- [stated, primary] In 2015 he says little computational MIP research had come out of academia in the previous decade (RINS was a big exception, symmetry a smaller one); it is very hard for academics to test whether an idea is good, the most they can hope for is a promising small test, after which people at the commercial solvers look at it; he would welcome a way for outsiders to contribute to cut management, where cut families interact (Optima 101 p. 6).
- [observed, secondary] Achterberg wrote in 2007 that research on branching is only possible with the source code of a state-of-the-art MIP solver, and that Alexander Martin's SIP code gave him that (acknowledgments p. ix). [inferred] Both men describe the same barrier from the two sides.
- [stated, primary] Free academic licences at Gurobi: done without much deliberation, to establish the name against CPLEX and because about 60 percent of licences went to people outside OR (Optima 101 p. 5). [observed, secondary] The 2004 Impact Prize citation credits Janet Lowe's CPLEX plan with a reduced-price academic programme; Rothberg's profile presents free, self-service academic licences as a Gurobi founding principle.
- [stated, primary] MIPLIB as service: libraries of real models collected with students and colleagues, with yearly updates promised in 1998 (§6, F6).
- [observed, secondary; the bio was probably supplied by him] The 2021 Toronto bio lists service as Editor-in-Chief of *Mathematical Programming* Series A (1989–1994) and Chairman of the Mathematical Programming Society (2001–2004).

### 4.8 Teaching after Rice (L7)

- [stated, primary] He taught for a couple of years in a business school but found he did not enjoy it, although the course was popular; when he teaches, he wants to teach mathematics. Since about 2010–11, a course in Erlangen arranged by Alexander Martin, about a month each year, concentrated, on computational linear and mixed-integer programming, with proofs (Optima 101 p. 6). Martin is an old collaborator: Bixby and Martin, *Parallelizing the Dual Simplex Method*, INFORMS J. Comput. 12(1):45–56, 2000, DOI 10.1287/ijoc.12.1.45.11902 (the December 1995 ZIB preprint SC-95-45 was not reachable in this run). [observed, secondary] The March 2021 Toronto bio lists him as visiting Professor of Mathematics at FAU Erlangen-Nürnberg; the 2013 Waterloo citation lists a Research Professor of Management title at Rice's Jones School. No FAU course listing was found.
- [practice, primary, caption transcript] Summer-school teaching, 2015: three dual simplex lectures at CO@Work, ZIB Berlin. He states the aim that a listener who works through the formulas and a few suggested readings can write a reasonable dual simplex implementation, and says earlier deliveries of the talk have borne this out (P16, Part 1). He takes students' questions patiently, admits when he has misunderstood one, and thanks the asker (Part 3). He also says openly that he leaves many implementation tricks out, from laziness rather than secrecy, and then gives one of them (Part 3).
- [stated, primary, short clip, upload 2015, recording date not stated] Advice to technology people: listening is a skill to be learned; let the customer state the pain and give them what they want instead of arguing about what their problem is (P18).
- [stated, primary] Practitioner modelling, 2017: in a supply-chain scheduling example he first asked the client's current scheduling team how they decide, then used their two-step logic (fix the producible schedule by heuristics, then optimize the rest) as the decomposition (ECCO 2017 slide 26).

---

## 5. Tacit knowledge: what students and colleagues knew that the papers do not say

| # | Tacit practice | Evidence | Tag |
|---|---|---|---|
| T1 | Learn a production code from the instances that break it, and fix the cause rather than work around it | Cook's motto (Optima 101 p. 7); OR 2002 p. 3; Optima 101 p. 2 | [observed] + [stated] |
| T2 | A user's failing instance (Baker, Gregory, a student's max-cut LP) is the trigger for the next feature, and it stays a test case for decades | §4.1–4.2; H5 | [stated] + [practice] |
| T3 | Much of the craft travelled by talk, code and private communication, not papers: bound shifting was never written up because he never got round to it (Optima 101 p. 4); steepest-edge results were cited as unpublished in 1991 (Boyd); students and colleagues cite his personal communications (Elizondo 1993; Gao & Zhang 2002) | as cited | [stated] + [observed] |
| T4 | Students use CPLEX as engine and baseline, compare with every algorithm in it and with a competitor, and write down where they lose | H1, H3 | [practice] |
| T5 | Real test models are obtained from companies, released with credit to originator, formulator and donor, and their optimality is labelled as verified or not | H2 | [practice] |
| T6 | When outsiders benchmark against CPLEX, the comparison should use the current release and sensible parameters; he supplies the test models | Gao & Zhang 2002 | [observed] |
| T7 | Ownership keeps good people: equity for the Lowes; get people invested | Optima 101 pp. 3, 6 | [stated] |
| T8 | Developers came from collaborations: challenge teams and hardware partnerships | §4.3 | [inferred] |
| T9 | Once off the code, his job is to run it constantly and ask the developers why it misbehaves | Optima 101 pp. 4–6 | [stated] |
| T10 | Rice's computational OR is cross-disciplinary: co-advising with numerical analysts and sitting on compiler students' committees | §1.1–1.2 | [practice] |
| T11 | Even in teaching, many implementation tricks stay untold; a lecture aims to make the listener able to implement, not to hand over every trick | CO@Work 2015 (P16) | [stated] |
| T12 | Go after the practitioner's hopeless instance, run it on the current release, and show the result to the same audience | 1999 FERC meeting (P15); ECCO 2017 slide 26 | [stated] |
| T13 | Inside the companies, progress is reviewed against named versions and a large, changing model set, with seeds and machine checks against noise | P15; P17 | [stated] |

---

## 6. Failures, abandoned plans and negative results

- **F1. No research money for LP computation.** [stated, primary] In 1987–88 he could not get research funding for LP computation, with no success at all, and founded CPLEX Optimization in 1988 (Hausdorff 2022 slide 10). Context, not a contradiction: by 1989–91 his Rice work carried NSF, AFOSR and parallel-computing-centre funding (§3, H4).
- **F2. The early code kept breaking.** [stated, primary] For about two years the code broke on one problem after another and he thought it junk, until a customer wanted to buy it (Optima 101 p. 2).
- **F3. First benchmark lost.** [stated, primary] On the first model he tried against XMP he was about seven times slower, and was crushed before finding that XMP had been lucky with its starting basis (Optima 101 p. 2; four times slower in the 2023 retelling, P15). OR 2002 tells the same comparison differently (see Contradictions).
- **F4. Early CPLEX MIP was behind.** [stated, primary] Research codes such as MINTO solved problems CPLEX could not; the MIP code crept along until Lustig (presolve), then Rothberg and Gu (CPLEX 6.5) (Optima 101 p. 3).
- **F5. Unpublished core idea.** [stated, primary] Bound shifting, which he counts among his most important contributions, has no paper (Optima 101 p. 4). The interviewer urged him to write one (p. 6); none was found in this run.
- **F6. MIPLIB yearly updates did not happen.** [stated, primary] MIPLIB 3.0 (Feb 1998) planned yearly updates (TR98-03 PDF p. 3). The next update came from ZIB authors, not from his group: Achterberg, Koch, Martin, *MIPLIB 2003*, Oper. Res. Lett. 34(4):361–372, 2006, DOI 10.1016/j.orl.2005.07.009. He returned as one of many co-authors of MIPLIB 2010.
- **F7. Collaborator advised giving up on simplex.** [stated, primary] Rejected (Hausdorff 2022 slide 23; §4.2).
- **F8. Modest parallel result, 1989.** [practice, primary] The two-processor split gave 73–92% of single-processor time (TR89-16).
- **F9. Students' negative or bounded results**: Dadmehr against barrier, McZeal on interior-point reoptimization, Saigal's declared failures (H3).
- **F10. Business-school teaching dropped** in favour of teaching mathematics (Optima 101 p. 6).
- **F11. Selling to airlines failed until a must-have case.** [stated, primary] Being faster than OSL did not win the airlines; a merger evaluation that needed answers fast did (Optima 101 p. 3; Hausdorff 2022 slides 20–21).

---

## 7. Era and resource context

| Period | Setting | Resources, team, seniority | Form of mentoring or collaboration | Evidence |
|---|---|---|---|---|
| 1972 (PhD) to mid-1980s | Kentucky, then Northwestern (dates of each post not verified here); matroid theory | Theory; AFOSR and Exxon grants (TR86-18 PDF p. 3) | Sole advisor of three matroid PhDs; joint papers with them | MGP; DOI 10.1287/moor.13.1.99 |
| early 1980s | Northwestern; first IBM PCs | Teaching code; colleague Fourer | Learns computational LP from a colleague | OR 2002 p. 3; Optima 101 p. 2 |
| c.1983/85–1987 | Rice (move dated 1983 by the 2023 host and 84/85 by the 2015 interviewers; Contradiction 19); a Humboldt-funded leave in Bonn noted in TR86-18; consulting for Chesapeake | His own code, 32-bit PCs, customer SLP snapshots; a CS student converts the code to C | Customer-fed failing instances; pays Applegate for data-structure work | Optima 101 p. 2; TR86-18; P15 |
| 1987–c.1991 | CPLEX Optimization (with the Lowes) plus Rice | Sole developer; Cray Y-MP through Cray Research; Sequent Symmetry; Sun workstations; NSF, AFOSR and CRPC grants | Students and visitors explore variants with CPLEX (Schwabacher, Mutzel, Saigal); cross-institution challenge teams | TR89-16; TR90-29; Saigal 1991; slides 15–23 |
| c.1991–1997 | CPLEX grows (Lustig; SGI partnership; Rothberg 1997); MIPLIB; Rice PhDs | CPLEX 2.x–5.0; Intel distributed-memory machines; HP 9000; SGI | Students use CPLEX as engine and baseline (Lee, Kilgore, Dadmehr); test-set curation with students | theses; TR91-38; TR92-36 |
| 1997–2008 | ILOG owns CPLEX; emeritus at Rice by May 1999 | CPLEX R&D team (about 15 by 2008, per Trick); Rothberg led R&D 1998–2005, Gu 2005–2008 (Rothberg's profile) | Last PhD (McZeal 1999); committee roles; models and caveats supplied to Rice colleagues (2001); off CPLEX from about 2003–04 (Lustig); semiconductor division and FPO | McZeal; Gao & Zhang; Trick and Lustig; profile |
| 2008–2015 | Gurobi, CEO 2008–2015 (Toronto 2021 bio) | Gurobi developers; test library grown from 600 to about 10,000 models | No development; tester and critic; team papers | Optima 101 pp. 4–6; DOI 10.1287/ijoc.2018.0857 |
| c.2010–2022 | Erlangen teaching; CO@Work 2015 lectures at ZIB; talks (ECCO 2017, Toronto 2021, Hausdorff 2022) | A concentrated month a year in Erlangen (as of 2015) | Teaching computational LP and MIP with proofs; lectures meant to let listeners implement the dual simplex | Optima 101 p. 6; Toronto 2021 bio; P16 |

---

## Contradictions (kept, not reconciled)

1. **Kilgore's advisor.** The Rice repository lists Bixby as advisor and her title page lists him as committee chairman, but her acknowledgments name Virginia Torczon as her advisor (hdl 1911/13851, PDF pp. 5, 7).
2. **What drove perturbation into CPLEX.** Optima 101 p. 3 (2015) names two triggers, the Cray fleet model and Saigal's degenerate max-cut LPs. OR 2002 p. 8 (2002) tells the fleet-model story (degen4) with Gregory and a pseudorandom perturbation, and does not mention Saigal. Saigal's thesis (pp. 55–56) confirms the degeneracy but handles it by solving the dual formulation; the pages read do not mention perturbation.
3. **The Cray fleet model: name, date, machine, version.** OR 2002 p. 8: degen4, presented as a challenge in late 1989, CPLEX 1.0 on a Cray Y-MP. Optima 101 p. 3: LAU2 from Gregory, CPLEX 1.something or maybe 2, Cray YMP. Hausdorff 2022 slides 22–23: LAU2, late 1980s, 1987, CPLEX 1.0 on a Cray X-MP. The dimensions agree (4420 × 6711, 101,377 nonzeros), so this is one model; but CPLEX 1.0 was first released in 1988 by his own texts, so the 1987 date conflicts.
4. **The first XMP comparison.** OR 2002 p. 3: on a substantial subset of netlib his code ran on average about two times faster than XMP and looked more stable. Optima 101 p. 2: about seven times slower on the first model, a factor of two after two weeks of work, then about four times faster on almost all models. 2023 interview (P15): four times slower on the first model, then faster on every other model and about four times faster on all of them within a week. Three recollections of one benchmark; weigh his later anecdotes accordingly.
5. **Who hired Fourer.** OR 2002 p. 3: the Northwestern department had hired Fourer. Optima 101 p. 2: he himself had hired Fourer. A difference of framing.
6. **Literature.** OR 2002 p. 3 and Optima 101 p. 2: in the early years he never looked in the literature. The 2004 Impact Prize citation: he drew on his own research and an extensive literature. The two may refer to different periods; the sources do not say.
7. **Dual steepest edge.** The 2004 Impact Prize citation credits him with discovering how to implement stable dual steepest-edge pricing; his own texts credit Forrest and Goldfarb (OR 2002 p. 8; Hausdorff 2022 slide 23).
8. **Founding year of CPLEX Optimization.** 1987: incorporation (Optima 101 p. 3), the 2021 Toronto bio, the 2004 citation (code created in 1987), and the 2023 interview with a hedge (P15). 1988: Hausdorff 2022 slide 10, Rothberg's profile, and the 2020 Gurobi clip (P18).
9. **Gurobi's founding.** Optima 101 p. 4 and the 2023 interview (P15): Gu and Rothberg had already planned a company; he left separately and asked to be included. Rothberg's profile: the three founded Gurobi in 2008. 2020 Gurobi clip (P18): Rothberg and Gu left at about the same time, and the three got together and decided quickly. A difference of emphasis that grows in the company-facing versions.
10. **His ILOG-era role.** Rothberg's profile: CPLEX Development Team manager, then Technical Advisory Board president, then general manager of the Semiconductor Business Division. Trick (2008): roles including Chief Science Officer. Lustig (2008): off CPLEX for four or five years, working on FPO. Optima 101 p. 4: still doing development in 1997. Four snapshots that do not line up into one timeline.
11. **Test-set size for the CPLEX 1.2–11 MIP study** (outside this lens; for agents 03 and 05). Documenta 2012 p. 116: 1892 models. ECCO 2017 slide 30 and the 2021 Toronto talk (P17): 1852 models. The ECCO slide derives it from a 2,791-model library minus 559 easy, 348 duplicates and 22 hard LPs, which leaves 1,862. Same versions and the same 30,000-second limit in both, and the same cumulative factor (ECCO: 29,530; Documenta: over 29,000).
12. **Waterloo honorary doctorate.** The 2021 Toronto bio says 2012; the Waterloo citation is for the convocation of 14 June 2013.
13. **Advisor order for Butera.** MGP lists Dennis first and Bixby second; the Rice repository lists Bixby first.
14. **Acknowledgment wording** (a caution, not a contradiction): Lee's 1993 thanks to Bixby repeat the phrases of Wu's 1991 thanks to Dennis.
15. **The 2004 Impact Prize grouping.** INFORMS's page groups Bixby, Janet Lowe and Paul Green, but its citation recognizes Bixby and Lowe for CPLEX and Paul Green separately, for conjoint analysis. Green was not part of CPLEX. This answers the open question in 06-trajectory.md about Green's role.
16. **Who converted the first code to C.** OR 2002 p. 3: he converted his code to C (one of Baker's conditions). 2023 interview (P15): a computer-science student who knew C converted it, and that is how he learned C.
17. **Recruiting Janet Lowe.** Optima 101 p. 3: he picked the two best students from 3–4 years of teaching the business-school modelling class, and she was his first choice; her husband Todd Lowe shared the 49 percent. 2023 interview (P15): she was the outstanding student over the two years he had taught the class, and it was she and he who founded CPLEX, with her husband joining a little later.
18. **How long bound shifting took.** Optima 101 p. 4 (October 2015): he struggled for about two weeks. CO@Work 2015 lectures (P16, Part 3): about a month to see the simple fix.
19. **Year of the move to Rice.** 2023 interview (P15, Excerpt A): the host dates the move to 1983 (Bixby's reply is not in the excerpt). Optima 101 p. 2: the interviewers suggest 84/85 and he says he was probably already at Rice by then. The 2023 interview also places the C conversion at about 1984, already at Rice. OR 2002 and the Hausdorff deck (slide 10, classroom code from 1983) do not say where he was.
20. **Caption quality** (a caution, not a contradiction): the CO@Work captions are uploaded subtitles and the 2021 and 2023 captions are automatic; names are garbled in the automatic ones, so any wording from P15 and P17 is approximate.

---

## Gaps

- No student blog post, memorial piece, Festschrift, lab guide or onboarding document was found (WebSearch for a Festschrift or tribute, for recollection phrases such as `worked with Bob Bixby`, and for an oral history all came back empty).
- No account by a CPLEX-era developer (Gu, Wunderling, Fenelon, Klotz) of how he ran the team, beyond Rothberg's profile and Lustig's blog comment. Apart from his own mention of whiteboard progress reviews every few months (P15), nothing on group meetings, code review or onboarding.
- Northwestern-era theses (Wagner 1983, Coullard 1985, Rajan 1986) were not located openly and were not read.
- Saigal's thesis was read only in part (front matter and pp. 46–47, 55–57, 67), so the perturbation claim stays partly unchecked. Wu's, Kilgore's and Butera's theses were read only in their front matter (scanned PDFs, read as page images).
- Not reached: the DTIC copy of an AFOSR final report (ADA244641), which a search snippet says names Saigal's thesis as the grant's main result; curl got a maintenance page and WebFetch HTTP 403. This stays an unverified lead.
- Not read by this agent: ZIB reports SC 92-11 and SC 95-45 (the ZIB server served a bot-check page; not bypassed), and Roland Wunderling's 1996 thesis (same server).
- DBLP served a bot-check page, so the venue of the 1994 Bixby–Kennedy–Kremer paper could not be verified and it is not listed.
- Michael Trick's 2007 post on Bixby's IFORS Distinguished Lecture was not reached: its old permalink now resolves to an unrelated post.
- isre.informs.org award page: Cloudflare challenge, not reached. The MGP advanced search was offline (PHP outage notice dated 4 November 2026); the quick search and record pages worked.
- The 2021 Toronto and 2023 interview videos were not watched; only the caption transcripts in `talks/` were read. The 2023 excerpt leaves out the opening and closing parts of the interview (family, health, politics, student years) for privacy and relevance, and one redacted passage names an outside contractor for the first CPLEX MIP version, so that contractor's role is not recorded here.
- Later careers and recollections of Saigal, Dadmehr, Butera and McZeal were not found. Beyond MGP's lists of their own students (Lee at Georgia Tech, Wu at Iowa State, Coullard at Northwestern and Purdue, Wagner at Purdue), the lineage after his students was not traced.
- Erlangen course titles and years: only his own 2015 statement and the 2021 bio.
- Living status and present role: this agent's searches found no dated trace after September 2022; the only later item in the corpus is the caption transcript of an interview uploaded on 7 December 2023 (P15). Nothing is stated about either.

---

## Sources

Primary (Bixby's own or co-authored):

- P1. "You have to figure out who your customer is going to be — An interview with Bob Bixby", Optima 101 (MOS newsletter), pp. 1–6; questions by V. Kaibel, J. Lee, J. Linderoth, October 2015; issue September 2016. https://mathopt.zib.de/Optima-Issues/optima101.pdf — primary
- P2. R. E. Bixby, "Solving Real-World Linear Programs: A Decade and More of Progress", Operations Research 50(1):3–15, 2002. DOI 10.1287/opre.50.1.3.17780 (read via https://www.gwern.net/doc/cs/algorithm/2002-bixby.pdf) — primary
- P3. R. E. Bixby, "A Brief History of Linear and Mixed-Integer Programming Computation", Documenta Math. Extra Vol. ISMP (2012) 107–121. DOI 10.4171/dms/6/16 (read via https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-ismp/25_bixby-robert.pdf) — primary
- P4. R. E. Bixby, "Linear Programming: A Historical View", deck, Hausdorff School on Computational Combinatorial Optimization, Bonn, September 2022. https://www.or.uni-bonn.de/~held/hausdorff_school_22/slides/GUR_Hausdorff_Day1_LP_History.pdf — primary (Gurobi-branded deck, paraphrased only)
- P5. R. E. Bixby, "Computational Progress in Linear and Mixed Integer Programming", ECCO invited lecture deck, 5 May 2017. https://ecco2017.euro-online.org/en/resources/files/invited-speakers/robertbixby.pdf — primary
- P6. R. E. Bixby, M. Schwabacher, "Solving Linear Programs with Two Processors", Rice TR89-16, November 1989. https://hdl.handle.net/1911/101665 — primary
- P7. R. E. Bixby, E. A. Boyd, R. R. Indovina, "A Test Set of Real-World Mixed Integer Programming Problems" (MIPLIB), Rice TR91-38, November 1991 (revised January 1992). https://hdl.handle.net/1911/101739 — primary
- P8. R. E. Bixby, E. A. Boyd, S. S. Dadmehr, R. R. Indovina, "The MIPLIB Mixed Integer Programming Library", Rice TR92-36, November 1992. https://hdl.handle.net/1911/101776 — primary
- P9. R. E. Bixby, S. Ceria, C. M. McZeal, M. W. P. Savelsbergh, "An Updated Mixed Integer Programming Library: MIPLIB 3.0", Rice TR98-03, February 1998. https://hdl.handle.net/1911/101898 — primary
- P10. R. E. Bixby, E. K. Lee, "Solving a Truck Dispatching Scheduling Problem Using Branch-and-Cut", Rice TR93-37, September 1993 (https://hdl.handle.net/1911/101808); Operations Research 46(3):355–367, 1998, DOI 10.1287/opre.46.3.355 — primary
- P11. R. E. Bixby, R. Fourer, "Finding Embedded Network Rows in Linear Programs I: Extraction Heuristics", Rice TR86-18, August 1986 (https://hdl.handle.net/1911/101605; funding note only); Management Science 34(3):342–376, 1988, DOI 10.1287/mnsc.34.3.342 — primary
- P12. R. E. Bixby, J. W. Gregory, I. J. Lustig, R. E. Marsten, D. F. Shanno, "Very Large-Scale Linear Programming: A Case Study in Combining Interior Point and Simplex Methods", Rice TR91-11, May 1991 (https://hdl.handle.net/1911/101715; funding notes only); Operations Research 40(5):885–897, 1992, DOI 10.1287/opre.40.5.885 — primary
- P13. R. E. Bixby, "Notes on Combinatorial Optimization", Rice TR87-21, 16 October 1987. https://hdl.handle.net/1911/101631 — primary
- P14. D. Applegate, R. Bixby, V. Chvátal, W. Cook, "On the Solution of Traveling Salesman Problems", Documenta Math. Extra Vol. ICM 1998 III, 645–656. DOI 10.4171/dms/1-3/62 (checked for any mention of CPLEX or strong branching: none in the text) — primary
- P15. "Subject to: Robert Bixby", long-form YouTube interview (channel "Subject to"), uploaded 7 December 2023, https://www.youtube.com/watch?v=47BZgFhEFJ8; read as the excerpted automatic-caption transcript `references/sources/talks/subject-to-2023-interview.excerpt.transcript.txt`, saved by another agent in this run — primary (caption text, not speaker-checked)
- P16. R. E. Bixby, "Solving Linear Programs: The Dual Simplex Algorithm", three lectures at CO@Work 2015, Zuse Institute Berlin (videos uploaded July and October 2016: https://www.youtube.com/watch?v=z1xvqwQR6xU, https://www.youtube.com/watch?v=ZNf84y4M-Dw, https://www.youtube.com/watch?v=uccbVoamiUM); read as `references/sources/talks/co-at-work-2015-dual-simplex-lectures.transcript.txt` (uploaded subtitles), saved by another agent in this run — primary
- P17. R. E. Bixby, "Optimization: Past, Present, Future", University of Toronto MIE Distinguished Seminar, 19 March 2021, https://www.youtube.com/watch?v=_R8-nt5NyiE; read as `references/sources/talks/toronto-2021-optimization-past-present-future.transcript.txt` (automatic captions), saved by another agent in this run — primary (caption text, not speaker-checked)
- P18. Two short clips: "Bob Bixby States Importance Of Becoming a Good Listener and Giving Customer What They Want" (Prendismo Collection, uploaded 17 January 2015, https://www.youtube.com/watch?v=8SUuT1swJTs) and "How was Gurobi founded?" (Gurobi, uploaded 8 April 2020, https://www.youtube.com/watch?v=YoQ2h_G3PNM); read as `references/sources/talks/short-clips-2015-2020.transcript.txt`, saved by another agent in this run — primary (the 2020 clip from automatic captions)

Secondary (students, colleagues, committees, databases):

- S1. M. Grötschel, "Comments on Bob Bixby's interview: Mathematics and the Real World", Optima 101, pp. 6–7, September 2016 (P1 URL) — secondary
- S2. W. Cook, "Comments on Bob Bixby's interview: Beauty in the Details", Optima 101, p. 7, September 2016 (P1 URL); also the editors' note (p. 1) and photo caption (p. 5) — secondary
- S3. Mathematics Genealogy Project, record 14993 (R. E. Bixby) and student records 67627, 67628, 143732, 39318, 29587, 39317, 39316, 29594, 37969, read 2026-11-05. https://www.mathgenealogy.org/id.php?id=14993 — secondary
- S4. Rice University repository (DSpace API search for "Bixby": advisor and committee metadata of theses and reports). https://repository.rice.edu/ — secondary
- S5. S. Saigal, "Optimizing over the cut cone: a new polyhedral algorithm for the maximum-weight cut problem", PhD thesis, Rice, 1991. https://hdl.handle.net/1911/16481 — secondary
- S6. Z. Wu, "A subgradient algorithm for nonlinear integer programming and its parallel implementation", PhD thesis, Rice, 1991. https://hdl.handle.net/1911/16495 — secondary
- S7. E. K. Lee, "Solving structured 0/1 integer programs arising from truck dispatching scheduling problems", PhD thesis, Rice, 1993; report TR93-18. https://hdl.handle.net/1911/101796 (thesis record https://hdl.handle.net/1911/16642) — secondary
- S8. A. Kilgore, "Very large-scale linear programming: a case study in exploiting both parallelism and distributed memory", MA thesis, Rice, November 1993 (repository year 1994). https://hdl.handle.net/1911/13851 — secondary
- S9. R. Elizondo, "Solving Very Large Scale School/Student Assignment Problems", MA thesis, Rice, September 1993; TR93-48. https://hdl.handle.net/1911/101818 — secondary
- S10. S. S. Dadmehr, "An efficient simplex-based method for solving large linear programs", PhD thesis, Rice, 1995; TR95-15. https://hdl.handle.net/1911/101860 (thesis record https://hdl.handle.net/1911/16813) — secondary
- S11. U. Kremer, "Automatic Data Layout for Distributed Memory Machines", PhD thesis, Rice CS; TR96-261, October 1995. https://hdl.handle.net/1911/96457 — secondary
- S12. C. N. Click Jr., "Combining Analyses, Combining Optimizations", PhD thesis, Rice CS, February 1995; TR95-252. https://hdl.handle.net/1911/96451 — secondary
- S13. G. O. Butera, "The solution of a class of limited diversification portfolio selection problems", PhD thesis, Rice, 1997. https://hdl.handle.net/1911/19140 — secondary
- S14. C. M. McZeal, "Reoptimization in interior-point methods with application to integer programming", PhD thesis, Rice, May 1999; TR99-28. https://hdl.handle.net/1911/101933 (thesis record https://hdl.handle.net/1911/19416) — secondary
- S15. J. L. Rich, "A Computational Study of Vehicle Routing Applications", PhD thesis, Rice, May 1999; TR99-11. https://hdl.handle.net/1911/101916 — secondary
- S16. N. L. Williams, "On Eliminating Square Paths in a Square Lattice", MA thesis, Rice, April 2000; TR00-23. https://hdl.handle.net/1911/101951 — secondary (thanks him among others; he was not on the committee)
- S17. S. Dash, "On the Matrix Cuts of Lovász and Schrijver and Their Use in Integer Programming", PhD thesis, Rice, March 2001; TR01-08. https://hdl.handle.net/1911/101970 — secondary
- S18. T. A. Redl, "Graceful Graphs and Graceful Labelings: Two Mathematical Programming Formulations and Some Other New Results", Rice TR03-01, January 2003. https://hdl.handle.net/1911/101998 — secondary
- S19. T. A. Redl, "A Study of University Timetabling that Blends Graph Coloring with the Satisfaction of Various Essential and Preferential Conditions", PhD thesis, Rice, May 2004; TR04-07. https://hdl.handle.net/1911/102019 — secondary
- S20. B. McClosky, "Independence Systems and Stable Set Relaxations", PhD thesis, Rice, April 2008; TR08-13. https://hdl.handle.net/1911/102093 — secondary
- S21. C. Fast, "On the Integrality Gap of the Subtour Relaxation of the Traveling Salesman Problem for Certain Fractional 2-matching Costs", MA thesis, Rice, April 2014. https://hdl.handle.net/1911/76721 — secondary
- S22. P. Mutzel, "Computational Results with Another Method of Solving Very Long and Thin LPs", Rice TR90-29, May 1990. https://hdl.handle.net/1911/101693 — secondary
- S23. E. A. Boyd, "Resolving Degeneracy in Combinatorial Linear Programs: Steepest Edge, Steepest Ascent, and Closest Ascent", Rice TR91-21, July 1991. https://hdl.handle.net/1911/101722 — secondary
- S24. L. Gao, Y. Zhang, "Computational Experience with Lenstra's Algorithm", Rice TR02-12, August 2002. https://hdl.handle.net/1911/101992 — secondary
- S25. Z. Wu, Y. Zhang, "Solving the Double Digestion Problem as a Mixed-Integer Linear Program", Rice TR01-12, August 2001 (PDF p. 6: describes CPLEX as originally developed by Bixby). https://hdl.handle.net/1911/101974 — secondary
- S26. T. Achterberg, "Constraint Integer Programming", Dr. rer. nat. thesis, TU Berlin, 2007 (defence 12 July 2007). https://api-depositonce.tu-berlin.de/server/api/core/bitstreams/a301bdbc-d04d-4fd5-9e04-c0399908689c/content — secondary
- S27. T. Koch, "Rapid Mathematical Programming", Dr. rer. nat. thesis, TU Berlin, 2004. https://hdl.handle.net/11303/1272 — secondary
- S28. P. Mutzel, "Introduction" slides with CV, Hausdorff School, Bonn, September 2022. https://www.or.uni-bonn.de/~held/hausdorff_school_22/slides/Introduction-PetraMutzel-HCM2022.pdf — secondary
- S29. Hausdorff School on Computational Combinatorial Optimization, programme page, 12–16 September 2022 (speakers Biere, Bixby, Mutzel, Uchoa; organizers Cook and Held). https://www.or.uni-bonn.de/~held/hausdorff_school_22/ — secondary
- S30. INFORMS, 2004 Impact Prize citation (Bixby and Janet Lowe; Paul Green separately). https://www.informs.org/Recognizing-Excellence/Award-Recipients/Robert-E.-Bixby-Janet-Lowe-and-Paul-Green — secondary
- S31. E. Rothberg, "Gurobi Optimization" (INFORMS O.R. & Analytics Success Stories, industry profile), undated (about 2013 by its own text). https://www.informs.org/Impact/O.R.-Analytics-Success-Stories/Industry-Profiles/Gurobi-Optimization — secondary
- S32. M. Trick, "Bixby, Gu, and Rothberg leave ILOG", blog post, 13 April 2008, with the comment by Irv Lustig of the same date. https://mat.tepper.cmu.edu/blog/index.php/2008/04/13/bixby-gu-and-rothberg-leave-ilog/ — secondary
- S33. University of Waterloo, Mathematics convocation citation and biography, Robert Bixby (DMath honoris causa), 14 June 2013. https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/bixby_citation.pdf — secondary
- S34. University of Toronto MIE, Distinguished Seminar "Optimization: Past, Present, Future" by R. Bixby, 19 March 2021: abstract and bio. https://www.mie.utoronto.ca/?p=19855 — secondary
- S35. OpenAlex harvest summary, `references/sources/publications/publications.md` (author A5012463224, fetched 2026-11-05 by the harvest script; co-author counts) — secondary, local

Identifier checks: the 17 DOIs named in this note were resolved through the Crossref API on 2026-11-05 (title, venue, volume, pages and authors match). Rice handles and record contents were read through the Rice repository API; MGP records were read from the record pages.
