# Robert E. Bixby · 01 · Publication landscape and signature works

| | |
|---|---|
| Researcher | Robert E. Bixby (DBLP pid 75/1779; OpenAlex author A5012463224, with one MIP paper under a split record A5097662446 per team.json). Lens per team.json: decision and measurement craft for LP (1987–2002) and MIP (CPLEX and Gurobi progress measurement). Matroid and TSP work are context only |
| Dimension | Research agent 01 of 06: publication landscape and dissection of signature works (framework §二 Agent 1, §五) |
| Research date | 2026-11-05 |
| Sources consulted | 41, listed as S1–S41 under "Sources" (30 primary, 11 secondary). 6 of the 7 allowed WebSearch calls were used; everything else was fetched with curl, WebFetch, the Crossref REST API and `scripts/dblp_works.py` |
| Local corpus | `references/sources/{papers,talks,essays,software}` held only `.gitkeep`: no user-supplied material. `publications/` held an OpenAlex summary (`publications.md`, `abstracts.md`) generated on 2026-11-05 before this run; it is used here as a secondary source (S32). `private/` was not opened |
| OpenAlex | not re-queried (`OPENALEX_API_KEY` is not set) |
| Living status / present role | Not stated, by design. team.json deliberately omits the `living` key; the task prompt's "living" tag is overridden by team.json. The latest dated trace among the sources read is the September 2022 Hausdorff deck (S8) |
| Quotation policy | To respect copyright, findings are paraphrased with a pinpoint page; exactly one short verbatim phrase is quoted (marked with quotation marks). Check exact wording at the cited page before quoting downstream |

**Tags.**
- **[stated]**: said or written by Bixby in a sole-author text, interview or his own deck. **[stated, joint]**: a co-signed paper whose voice ("we") cannot be split among authors.
- **[practice]**: what the record shows was done (experiments, tables, test-set construction, dated runs, the publication record itself).
- **[observed]**: what others recorded (colleagues' comments, genealogy and bibliographic databases, later papers).
- **[inferred]**: my inference; the basis is named.
- **P / S**: primary / secondary source.

**Page conventions.** OR 2002 (S1): printed p. N = PDF p. N−2. Documenta (S2): printed pp. 107–121. Optima 101 (S3–S5): printed = PDF page. SC 92-11 (S6) and SC-95-45 (S7): printed p. N = PDF p. N+1. Hausdorff deck (S8): "slide k" = PDF page k (the printed slide numbers are k+1). ECCO 2017 (S9) and Fields 2012 (S10): slide = PDF page. IFIP 2000 (S11): the preprint's own printed page numbers, not the book pagination (pp. 19–49); text extraction splits printed p. 19 into three PDF chunks, so after it the extracted chunk number is printed + 2.

**Reading depth.**
- Read in full: S1, S2, S3 (interview pp. 1–6 and the two comments), S6 (German OCR text; tables skimmed), S7, S8 (incl. the image-only slide 11, rendered and read), S9, S10, S11 (appendix tables skimmed), S12 (MIPLIB 3.0 article, pp. 12–15).
- Abstract or metadata only: S13–S30 (see Sources for which).
- Not reached: the INFORMS journal pages (HTTP 403 per team.json; not retried), apps.dtic.mil (under maintenance on 2026-11-05), ScienceDirect (HTTP 403), the 2015 deck once hosted at people.bath.ac.uk (now redirects to the university home page), web.archive.org (not used).

---

## 0. Authorship and role labels (must survive into the skill)

These rest on his own dated statements. A progress number measured on a code is not evidence that he wrote what produced it.

### 0.1 LP

| Label | Evidence | Tag |
|---|---|---|
| Main parts of the CPLEX simplex implementation described in the planned paper series were written by him (as of April 1992) | S6 printed p. 2 | [stated] P |
| At the first release (1988) he was responsible for all of the development | S3 p. 3 | [stated] P |
| At the 1997 sale to ILOG he was still doing development and was still an academic | S3 p. 4 | [stated] P |
| At Gurobi he did no development: "Absolutely zero development." He did a lot of testing, pressed the developers about bad behaviour, and wanted to run the business | S3 pp. 4–5 | [stated] P |
| Later CPLEX LP changes (5.0 → 7.1 and after) are not shown to be his. OR 2002 credits Gu, Lustig, Rothberg and Wunderling with fundamental contributions to the CPLEX LP algorithms; Fenelon, Gregory and Klotz with insights | S1 p. 14 (acknowledgments) | [stated] P |
| The CPLEX 6.5 LP work (hyper-sparse solves, long-step dual, fast pricing update) is reported in a five-author paper in the "we" voice; roles are not divided | S11 pp. 5–6 | [stated, joint] P |
| Dual steepest edge is Forrest and Goldfarb's method (their version 1, Forrest & Goldfarb 1992) that CPLEX implemented | S1 pp. 6, 8; S2 p. 113; S7 pp. 3–4 (CPLEX implements two of the norms proposed there; default SE1 with initial norms 1); S8 slide 21 (Forrest's success with primal Devex led CPLEX to implement dual steepest edge; Goldfarb then suggested a simpler variant) | [stated] P |
| Sifting was John Forrest's idea, as his own slide credits it | S8 slide 14 | [stated] P |
| The 1989 American Airlines challenge work (sifting scheme, barrier/simplex hybrid, first fast crossover based on a result of Megiddo) is joint with Gregory, Lustig, Marsten, Shanno | S8 slides 14–15; S14 | [stated, joint] P |
| He worked on crossover and made a couple of observations that made it much faster | S3 p. 3 | [stated] P |
| Bound shifting: he says he thinks it was his most important contribution, that it came out of Harris's ratio-test idea (made known to him by Fourer), and that no paper exists | S3 p. 4 | [stated] P — but see Contradiction C5 |
| Perturbation entered CPLEX after the LAU2 failure and a student's (Sanjay Saigal's) degenerate max-cut problems | S3 p. 3 | [stated] P |
| His own version of partial pricing was in the first code | S3 p. 2 | [stated] P |
| The parallel barrier was Rothberg's (SGI partnership) | S3 p. 3; S8 slide 18 (the slide says the story is as Rothberg reported it) | [stated] P |
| OSL was John Forrest's (1992) / primarily Forrest's and Tomlin's (2012) | S6 printed p. 2; S2 p. 113 | [stated] P (see C18) |

### 0.2 MIP

| Label | Evidence | Tag |
|---|---|---|
| He says he did little of the MIP work and that the real contributions were Rothberg's and Gu's, later Achterberg's | S3 p. 4 | [stated] P |
| Todd Lowe gets the credit for deciding the product needed a MIP | S3 p. 3 | [stated] P |
| He helped design the callable library (around 1990/91), influenced by Grötschel's cutting-plane work and the TSP paper's complaint about MPSX | S3 p. 3; S1 p. 4; S2 p. 116 | [stated] P |
| Strong branching came out of the TSP work; after a discussion with Bill Cook he put it into CPLEX | S3 p. 4; S9 slide 29 (variable/node selection influenced by the TSP) | [stated] P |
| Gu implemented the cuts and most of presolve; Rothberg added node presolve, probing, bound strengthening and the first heuristics | S3 p. 4 | [stated] P |
| The MIP code crept along until Lustig (presolve) and took off with Rothberg and Gu: the CPLEX 6.5 story | S3 p. 3 | [stated] P |
| Early CPLEX MIP had knapsack cuts, and research codes such as MINTO solved problems CPLEX could not | S3 p. 3 | [stated] P |
| The 2012 MIP tricks are Gurobi's (the slides present them as the company's own trick); with no development by him at Gurobi they are company work, not his code | S10 slides 19–34 with S3 pp. 4–5 | [inferred] |
| His MIP lens is measurement and decision craft: the test-set design and version-to-version measurements in S2, S9, S10, S11 | — | [inferred], scope per team.json |

---

## 1. Publication landscape

### 1.1 Record coverage

- [observed, S] **DBLP** (S31): 38 records, 1974–2020 (29 articles, 6 conference papers, 2 chapters, 1 editorship); 35 carry a DOI; none carries an arXiv id. DBLP notes a 2007 Frederick W. Lanchester Prize (work not named there), a Rice homepage and a Mathematics Genealogy link. DBLP misses the 1973–76 game-theory papers, the 1981/1984 chapters, the 1988 Management Science paper, the DTIC and ZIB reports, the Optima pieces, the ICM 1998 TSP paper, the TSP book, Documenta 2012 and the 2006 ASMC paper.
- [observed, S] **OpenAlex summary** (S32, author A5012463224): 96 works (84 counted), 5,549 citations, h-index 36. The IFIP 2000 MIP chapter is absent from its top-25 although Crossref counts 128 citations to it; its Crossref author string reads "E. Robert Bixby". [inferred] This chapter is a plausible candidate for the split record A5097662446 named in team.json; not checked (OpenAlex not queried).
- [observed, S] **No arXiv presence**: no record in DBLP or Crossref carries an arXiv id; his preprints went out as Rice/DTIC and ZIB reports.
- [practice, P] **Homepage**: www.caam.rice.edu/~bixby/ redirects to www.cmor-faculty.rice.edu/~bixby/, a Flash-only page; no CV or list could be read (S41).

### 1.2 Verified works (LP and MIP lens)

Every identifier was resolved with a tool on 2026-11-05 (Crossref REST API unless "DBLP" is named). "Read" says what was read in this run.

| # | Year | Work | Venue | Identifier | Authors (alphabetical unless noted) | Read | Tags |
|---|---|---|---|---|---|---|---|
| W1 | 1980 | Converting Linear Programs to Network Problems | Math. Oper. Res. 5(3):321–357 | DOI 10.1287/moor.5.3.321 | Bixby, Cunningham | abstract (S32) | [practice, joint] P |
| W2 | 1981 | Hidden Structure in Linear Programs | Computer-Assisted Analysis and Model Simplification, pp. 327–360 | DOI 10.1016/b978-0-12-299680-1.50024-0 | Bixby | not read | [practice] P |
| W3 | 1983 | Hidden and Embedded Structure in Linear Programs | DTIC report (Northwestern IE/MS; AFOSR TR-84-0046), 1983-09-30 | DOI 10.21236/ada137773 | Bixby | not read (DTIC down) | [practice] P |
| W4 | 1984 | Recent Algorithms for Two Versions of Graph Realization and Remarks on Applications to Linear Programming | Progress in Combinatorial Optimization, pp. 39–67 | DOI 10.1016/b978-0-12-566780-7.50009-x | Bixby | not read | [practice] P |
| W5 | 1986 / 1988 | Finding Embedded Network Rows in Linear Programs I. Extraction Heuristics | DTIC report 1986-08-01; Management Science 34(3):342–376, 1988 | DOI 10.21236/ada455195; DOI 10.1287/mnsc.34.3.342 | Bixby, Fourer | abstract (Crossref, IDEAS) | [practice, joint] P |
| W6 | 1989 | Linear Programming Tools for Integer Programming | DTIC report (Rice Math. Sci.; AFOSR TR-90-0313), 1989-10-31 | DOI 10.21236/ada219013 | Bixby | not read | [practice] P |
| W7 | 1991 / 1992 | Implementing the Simplex Method: The Initial Basis | DTIC report 1991-09-01; ORSA J. Comput. 4(3):267–284, 1992; German version ZIB SC 92-11, April 1992 (translated by R. Weismantel, S6 p. 21) | DOI 10.21236/ada453079; DOI 10.1287/ijoc.4.3.267; SC 92-11 | Bixby | German version in full; English abstract | [stated] [practice] P |
| W8 | 1991 / 1992 | Very Large-Scale Linear Programming: A Case Study in Combining Interior Point and Simplex Methods | DTIC report 1991-05-01; Operations Research 40(5):885–897, 1992 | DOI 10.21236/ada452700; DOI 10.1287/opre.40.5.885 | Bixby, Gregory, Lustig, Marsten, Shanno | abstract only (+ S8 slides 14–17) | [practice, joint] P |
| W9 | 1992 | A Test Set of Real-World Mixed Integer Programming Problems | DTIC report (Rice; AFOSR), 1992 | DOI 10.21236/ada455431 | Bixby, Boyd, Indovina | not read | [practice, joint] P |
| W10 | 1992 | MIPLIB: A Test Set of Mixed Integer Programming Problems | SIAM News 25:2 (March 1992) | venue + year + title as cited in S12 ref. [1] only | Bixby, Boyd, Indovina | not read | [practice, joint] P |
| W11 | 1992 | Linear-Programming Tools in Integer Programming: The Traveling Salesman | DTIC report (AFOSR TR-93-0092), 1992-10-31 | DOI 10.21236/ada261398 | Bixby | not read | [practice] P |
| W12 | 1994 | Commentary—Progress in Linear Programming | ORSA J. Comput. 6(1):15–22 | DOI 10.1287/ijoc.6.1.15 | Bixby | abstract (Crossref) | [stated] P |
| W13 | 1994 | Recovering an optimal LP basis from an interior point solution | Oper. Res. Lett. 15(4):169–178 | DOI 10.1016/0167-6377(94)90074-4 | Bixby, Saltzman | not read (ScienceDirect 403) | [practice, joint] P |
| W14 | 1994 | Automatic Data Layout Using 0-1 Integer Programming | IFIP PACT 1994, pp. 111–122 | DBLP record (no DOI) | Bixby, Kennedy, Kremer | not read | [practice, joint] P |
| W15 | 1995 / 2000 | Parallelizing the Dual Simplex Method | ZIB SC-95-45, Dec 1995; INFORMS J. Comput. 12(1):45–56, 2000 | SC-95-45; DOI 10.1287/ijoc.12.1.45.11902 | Bixby, Martin | preprint in full | [stated, joint] [practice] P |
| W16 | 1998 | Solving a Truck Dispatching Scheduling Problem Using Branch-and-Cut | Operations Research 46(3):355–367 | DOI 10.1287/opre.46.3.355 | Bixby, Lee | not read | [practice, joint] P |
| W17 | 1998 | An Updated Mixed Integer Programming Library: MIPLIB 3.0 | Optima 58 (June 1998), pp. 12–15 | venue + year + title (S12, read) | Bixby, Ceria, McZeal, Savelsbergh | read | [stated, joint] [practice] P |
| W18 | 1999 | Computational experience with parallel mixed integer programming in a distributed environment | Annals of OR 90:19–43 | DOI 10.1023/A:1018960631213 | Bixby, Cook, Cox, Lee | not read | [practice, joint] P |
| W19 | 2000 | MIP: Theory and Practice — Closing the Gap | System Modelling and Optimization (19th IFIP TC7 conf., 1999), Kluwer 2000, pp. 19–49 (DBLP: 19–50) | DOI 10.1007/978-0-387-35514-6_2 | Bixby, Fenelon, Gu, Rothberg, Wunderling | preprint in full | [stated, joint] [practice] P |
| W20 | 2002 | Solving Real-World Linear Programs: A Decade and More of Progress | Operations Research 50(1):3–15 | DOI 10.1287/opre.50.1.3.17780 | Bixby | in full | [stated] [practice] P |
| W21 | 2004 | Mixed-Integer Programming: A Progress Report | The Sharpest Cut (MPS-SIAM), ch. 18, pp. 309–325 | DOI 10.1137/1.9780898718805.ch18 | Bixby, Fenelon, Gu, Rothberg, Wunderling | not read | [practice, joint] P |
| W22 | 2006 | Short-Interval Detailed Production Scheduling in 300mm Semiconductor Manufacturing using Mixed Integer and Constraint Programming | ASMC 2006, pp. 148–154 | DOI 10.1109/asmc.2006.1638740 | Bixby, Burda, Miller | not read | [practice, joint] P |
| W23 | 2007 | Progress in computational mixed integer programming—A look back from the other side of the tipping point | Annals of OR 149(1):37–41 | DOI 10.1007/s10479-006-0091-y | Bixby, Rothberg | not read | [practice, joint] P |
| W24 | 2008 | Technology that upsets the social order — a paradigm shift in assigning lots to tools in a wafer fabricator — the transition from rules to optimization | WSC 2008, pp. 2277–2285 | DOI 10.1109/WSC.2008.4736331 | Fordyce, Bixby, Burda (not alphabetical) | not read | [practice, joint] P |
| W25 | 2011 | MIPLIB 2010 | Math. Program. Comput. 3(2):103–163 | DOI 10.1007/s12532-011-0025-9 | Koch, Achterberg, … (16; Bixby 6th) | not read | [practice, joint] P |
| W26 | 2012 | A Brief History of Linear and Mixed-Integer Programming Computation | Documenta Math. Extra Vol. ISMP (2012) 107–121 | DOI 10.4171/dms/6/16 | Bixby | in full | [stated] [practice] P |
| W27 | 2020 | Presolve Reductions in Mixed Integer Programming | INFORMS J. Comput. 32(2):473–506 | DOI 10.1287/ijoc.2018.0857 | Achterberg, Bixby, Gu, Rothberg, Weninger | abstract (IDEAS) | [practice, joint] P |

Further MIP-adjacent items (DBLP/Crossref, not read): Solving Nonlinear Integer Programs with a Subgradient Approach on Parallel Computers, SIAM 1996, pp. 277–286, DOI 10.1137/1.9780898719659.ch25 (Bixby, Dennis, Wu); Market Split and Basis Reduction, IPCO 1999 (DOI 10.1007/3-540-48777-8_1) and INFORMS J. Comput. 12(3):192–202, 2000 (DOI 10.1287/ijoc.12.3.192.12635) (Aardal, Bixby, Hurkens, Lenstra, Smeltink); IPCO 1998 proceedings, LNCS 1412, editor (DOI 10.1007/3-540-69346-7); Numerical Optimization at the Center for Research on Parallel Computation, IJHPCA 8(2):143–153, 1994 (DOI 10.1177/109434209400800206; 14 authors).

**Talks and interviews (no DOI; title, venue and date checked on the source itself).**

| # | Date | Title | Venue | Read | Tags |
|---|---|---|---|---|---|
| T1 | 1986 | Handwritten "Test Runs" table, code labelled LOPT vs XMP, 13 netlib problems, Sun 3/50 | shown as slide 11 "1st Public CPLEX Results -1986" in S8 | image read | [practice] P |
| T2 | 1988 | Talk at Columbia University (CPLEX 1.1 vs XMP) | known only as Table 7 of S1 (p. 11) | via S1 | [practice] P |
| T3 | 12 June 2012 | 1000X MIP Tricks | Fields Institute, Bill Cunningham's 65th (S10) | in full | [stated] P |
| T4 | 13 May 2015 | Computational Progress in Linear and Mixed Integer Programming | Imperial College CPSE seminar (S37) | listing only; the deck once at people.bath.ac.uk is unreachable | [observed] S |
| T5 | Oct 2015 / Sept 2016 | Interview (Kaibel, Lee, Linderoth), with comments by Grötschel and Cook | Optima 101 pp. 1–7 (S3–S5) | in full | [stated] [observed] P |
| T6 | May 2017 | Computational Progress in Linear and Mixed Integer Programming | ECCO 2017 invited lecture (S9) | in full | [stated] P |
| T7 | Sept 2022 | Linear Programming: A Historical View | Hausdorff School on Computational Combinatorial Optimization, Bonn, 12–16 Sept 2022 (Monday) (S8, S35) | in full | [stated] P |

The Hausdorff program page (S35) links only this one Bixby deck; the slide folder listing returns HTTP 403, so no other day's Bixby deck (e.g. a MIP deck) was found.

**Context only (verified, not read).** Game theory with his advisor L. J. Billera, 1973–76 (e.g. A characterization of polyhedral market games, IJGT 1973, DOI 10.1007/bf01737574; Pareto Surfaces of Complexity 1, SIAM J. Appl. Math. 1976, DOI 10.1137/0130009). Matroids 1974–88 (e.g. ℓ-matrices and a characterization of binary matroids, Discrete Math. 8(2):139–145, 1974, DOI 10.1016/0012-365X(74)90060-0; On Reid's characterization of the ternary matroids, JCT B 26(2):174–204, 1979, DOI 10.1016/0095-8956(79)90056-X; An Almost Linear-Time Algorithm for Graph Realization, MOR 13(1):99–123, 1988, DOI 10.1287/moor.13.1.99, with Wagner). TSP with Applegate, Chvátal, Cook, roles not divided (ICM 1998, DOI 10.4171/dms/1-3/62; TSP Cuts Which Do Not Conform to the Template Paradigm, 2001, DOI 10.1007/3-540-45586-8_7; Math. Program. 97:91–153, 2003, DOI 10.1007/s10107-003-0440-4; ORL 37(1):11–15, 2009, DOI 10.1016/j.orl.2008.09.006; The Traveling Salesman Problem, Princeton, 2011 edition DOI 10.1515/9781400841103).

### 1.3 Topics by five-year period

| Period | What appears (verified items) | Reading |
|---|---|---|
| 1970–74 | Game theory with Billera (1973–74); first sole matroid paper (1974) | [practice] Thesis-era theory (PhD Cornell 1972, advisor Billera, S34) |
| 1975–79 | Sole-author matroid and connectivity papers (Networks 1975; Discrete Math. 1977, 1978; JCT B 1977, 1979); one more game-theory paper with Billera (SIAM J. Appl. Math. 1976) | [practice] The matroid papers are all solo |
| 1980–84 | Matroid methods applied to LP structure: W1 (1980), W2 (1981), W3 (1983, AFOSR-funded), W4 (1984) | [practice] First LP items; [stated] Tom Baker (Exxon, later Chesapeake) met him after hearing him talk on W1's topic at SUNY Binghamton (S3 p. 1) |
| 1985–89 | Matroids with students (Coullard, Wagner); embedded network rows with Fourer (W5); LP tools for IP (W6, 1989). CPLEX incorporated 1987, first release 1988 (S3 p. 3) | [practice] Turn toward computation; no publication on the simplex code itself yet |
| 1990–94 | CPLEX simplex internals (W7), IPM/simplex hybrid (W8), MIPLIB (W9, W10), LP tools for TSP (W11), commentary on barrier vs simplex (W12), basis recovery (W13), 0-1 IP data layout (W14) | [practice] The densest LP-computation period |
| 1995–99 | Parallel dual simplex (W15 preprint), MIPLIB 3.0 (W17), truck dispatching B&C (W16), parallel MIP (W18), market split, IPCO 1998 editor, TSP | [practice] Shift toward MIP and test libraries |
| 2000–04 | CPLEX 6.5 MIP and LP report (W19), IJOC version of W15, LP progress retrospective (W20), MIP progress report (W21), TSP | [practice] Measurement retrospectives as ILOG CPLEX |
| 2005–09 | Semiconductor MIP/CP applications (W22, W24), look-back with Rothberg (W23), TSP book, 85,900-city TSP | [practice] Applications and history; Gurobi founded 2008 (team.json; not verified here) |
| 2010–14 | MIPLIB 2010 (W25), Documenta history (W26), Fields talk (T3) | [practice] History and benchmark library |
| 2015–20 | Optima interview (T5), Imperial and ECCO talks (T4, T6), presolve in Gurobi (W27) | [stated] In Oct 2015 he said he no longer did research except the Gurobi presolve paper (S3 p. 6) |
| 2021– | Hausdorff deck, Sept 2022 (T7) | Latest dated trace found; no later item searched for (by design) |

### 1.4 Author position: alphabetical, so no first→last shift signal

- [practice, S] In DBLP, 26 of 28 multi-author records list authors in alphabetical surname order (computed from S31). The two exceptions are W24 (Fordyce first) and W25 (Koch first, the rest alphabetical). Bixby is never last author. He is first in 18 records because his surname sorts early, and in a middle position in the other 10: where a co-author's surname sorts before his (Aardal, Achterberg, Applegate, Averick, Bischof) or the order is not alphabetical (Fordyce, Koch).
- [inferred] The first-author → last-author heuristic of the framework carries no information for him. The usable signal is **solo → team**. His solo works are:
  - the matroid papers (1974–79);
  - LP-structure chapters and reports (W2–W4, 1981–84) and two AFOSR reports on LP tools for integer programming (W6, W11);
  - four LP-computation statements: W7 (1991/92), W12 (1994), W20 (2002), W26 (2012).
  From 1995 on, every paper except the two retrospectives W20 and W26 is joint.
- [observed, S] The OpenAlex co-author heuristic (other first × self last) flags Louis Billera five times (S32); Billera was his doctoral advisor (S34), so the heuristic points the wrong way here.

### 1.5 Collaboration network and students

- **CPLEX/ILOG core** (W19, W21, W23, W27; S1 p. 14): Zonghao Gu, Ed Rothberg, Roland Wunderling, Mary Fenelon; Irv Lustig; John Gregory (Cray Research, then CPLEX); later Tobias Achterberg and Dieter Weninger (Gurobi presolve).
- **Barrier/IPM** (W8): Gregory, Lustig, Marsten, Shanno.
- **LP structure**: Cunningham (W1), Fourer (W5; also his informal teacher on computational LP, S1 p. 3, S3 p. 2), Saltzman (W13).
- **Parallel**: Alexander Martin (W15, ZIB; later arranged his yearly Erlangen teaching, S3 p. 6); Cook, Cox, Lee (W18); Kennedy, Kremer (W14); CRPC (Rice).
- **Test libraries**: Boyd, Indovina (W9, W10); Ceria, McZeal, Savelsbergh (W17); Koch et al. (W25).
- **TSP** (context): Applegate, Chvátal, Cook.
- **Students** [observed, S] per the Mathematics Genealogy Project (S34): Donald Wagner (Northwestern 1983), Collette Coullard (Northwestern 1985), Arvind Rajan (Northwestern 1986), Zhijun Wu (Rice 1991), Sanjay Saigal (Rice 1991), Eva Lee (Rice 1993), Shireen Dadmehr (Rice 1995), Gwyneth Owens-Butera (Rice 1997), Cassandra McZeal (Rice 1999). Co-authored with Wagner, Coullard (matroids), Wu (1996 subgradient IP), Lee (W16, W18), McZeal (W17). [stated] Saigal's degenerate max-cut problems forced the first anti-degeneracy code in CPLEX (S3 p. 3).

### 1.6 Usual venues

- [practice, S] ORSA/INFORMS J. Comput. (W7, W12, W15, W27, market split), Operations Research (W8, W16, W20), Math. Oper. Res. (W1, 1985, 1988), Annals of OR (W18, W23), Oper. Res. Lett. (W13, TSP 2009), Documenta Math. (ICM 1998, W26), Optima newsletter (W17, interview), DTIC reports (W3, W6, W9, W11 and preprint versions of W5, W7, W8), ZIB preprints (S6, S7). No arXiv.
- [inferred] For the LP code itself, the channel is a few retrospective or invited papers (W7, W12, W20, W26) and many talks; internals were rarely written up (see §3).

### 1.7 Most cited

Crossref counts fetched 2026-11-05; OpenAlex counts from the S32 summary (same day). Both are relative indicators only.

| Work | Crossref | OpenAlex |
|---|---|---|
| The Traveling Salesman Problem (book, 2011 DOI) — context | 333 | 402 |
| W25 MIPLIB 2010 | 299 | 321 |
| W20 OR 2002 LP progress | 261 | 380 |
| W23 Bixby & Rothberg 2007 | 150 | 195 |
| TSP 85,900 cities (ORL 2009) — context | 147 | 176 |
| W27 Presolve 2020 | 138 | 179 |
| W19 IFIP 2000 MIP | 128 | not in top 25 (see §1.1) |
| W26 Documenta 2012 | 127 | 228 |
| W8 OR 1992 IPM/simplex case study | 116 | 164 |
| W7 IJOC 1992 initial basis | 111 | 166 |
| W12 1994 commentary | 85 | 87 |
| W1 MOR 1980 | 85 | 118 |
| W21 Sharpest Cut 2004 | 72 | 110 |
| W15 IJOC 2000 parallel dual | 22 | — |

### 1.8 Recent works and latest traces

- [practice, S] Last research paper in DBLP: W27 (INFORMS J. Comput. 32(2), 2020; OpenAlex dates it 2019). [stated] In October 2015 he said he no longer did research except that presolve paper (S3 p. 6).
- [practice, P] Latest dated public items read: ECCO deck (May 2017, S9) and Hausdorff deck (Sept 2022, S8). Nothing later was searched for (living status and present role are out of scope by team.json).

---

## 2. Signature works (framework §五)

Chosen as: the most cited LP work (SW3), the sole-authored statement of his MIP version-to-version measurement (SW5), the only published part of his planned CPLEX series (SW1), the turning-point case study (SW2), and the MIP measurement paper of the CPLEX 6.5 breakthrough (SW4). §2.6 covers the contribution he himself calls most important, which has no paper; §2.7 the failure exemplar. Candidate methods (CM1–CM9) are defined in §4 and cross-referenced here.

### SW1 · Implementing the Simplex Method: The Initial Basis (W7; DTIC TR 1991, IJOC 1992, ZIB SC 92-11)

- **Origin.** [stated, P] The paper is announced as the first of a series on the CPLEX simplex implementation, whose main parts he says he wrote (S6 p. 2); the start basis is its Part II. Why the start basis came first: not stated (S6). [inferred] It was the most self-contained piece to publish.
- **Why then.** [stated, P] The intro says that ten years earlier computational LP was thought mature, that this expectation had been refuted by computer advances, by demands from integer programming, and by Karmarkar-inspired interior-point methods (S6 pp. 1–2). [practice] Grants: NSF CCR-8815914 and AFOSR-90-0273 (S6 p. 1 footnote); written during a stay at ZIB (S6 title page).
- **Key insight.** [stated, P] The CPLEX basis is not a crash procedure but a default start basis; he warns that a crash procedure applied to a problem of unknown origin can have catastrophic effects, so the aim is to avoid a bad basis rather than to find a good one (S6 p. 17). Construction: all slacks first, then the remaining variables sorted by bound width (cost as tie-breaker), with a triangularity-seeking pivot rule that limits artificials (S6 pp. 17–19).
- **Minimum evidence.** [practice, P] All 90 netlib problems solved from four start bases (artificial, feasible-slack, slack, CPLEX) on a 40 MHz SPARCstation 2, batch mode, no other jobs, user times (S6 pp. 19–20). On average 52.9% of slacks were still in the optimal basis and only 13.1% of rows needed artificials. Because totals were dominated by a few hard problems, he added per-problem iteration and time ratios. He also checked that the average was not hiding many ratios far below 1: the CPLEX basis was slower in 20 of 90 cases, 12 of them by less than 10%, and only one by more than 30%. The average gain over the slack basis was about 35% (S6 p. 20). He also says the CPLEX basis helps easy problems much more than hard ones, against intuition (S6 pp. 17, 20–21).
- **Abandoned paths.** [practice, P] The planned later parts were Wolfe's composite simplex in Phase I, a time-saving partial pricing, a simple bound-perturbation method against stalling, and vectorization (S6 p. 2). No later part was found in DBLP, Crossref or the OpenAlex summary. [stated] On bound shifting he later said he never got around to writing it (S3 p. 4). [inferred] The series stopped after Part II.
- **Test-set craft shown.** [stated, P] Netlib contains, as far as he knew, only real models, but some were included only because they troubled the simplex method; such problems help make a code robust but are poor for setting parameters. Solve a few small members of a model class before the whole class (S6 p. 6). Tolerances (1e-6 default) and the Markowitz threshold (0.01 default) are stated; optimal values were re-checked with tighter settings from the default basis (S6 pp. 7–8).
- **Reception.** [observed, S] 111 Crossref / 166 OpenAlex citations (§1.7). Nothing else checked.
- **Era and resources.** One-person core code in C on a workstation; netlib as the only shared test set; a visiting stay at ZIB.
- **Method it shows.** CM2 (per-problem ratios plus a distribution check), CM6 (a default that avoids harm on unknown models).

### SW2 · Very Large-Scale Linear Programming: A Case Study in Combining Interior Point and Simplex Methods (W8; OR 1992, joint)

Full text **not read** (INFORMS). Evidence: the publisher abstract (S14 via Crossref/IDEAS) and his own 2022 slides on the same work (S8 slides 14–17).

- **Origin.** [stated, P] American Airlines made a huge crew-scheduling LP available in 1989 as a challenge: 837 rows and about 12.75 million columns; size dictated a special-purpose algorithm (S8 slide 14). The team: Bixby, Lustig, Marsten, Shanno, Gregory (S8 slide 14).
- **Why then.** [inferred from S2 pp. 112–113, S8 slide 14] OB1's primal-dual barrier code (Lustig, Marsten, Shanno) and CPLEX's simplex existed side by side around 1990, and Cray hardware was reachable through Gregory.
- **Key insight.** [stated, joint, P] Successive small subproblems give little growth of solution time with the number of variables (S14 abstract). In his 2022 summary: sifting (Forrest's idea) — solve a column subset, price the rest with the optimal duals, add a good set of violated columns, repeat — combined with barrier from scratch and primal simplex near the end, where an advanced basis helps (S8 slide 14).
- **Minimum evidence.** [stated, P] On a Cray Y-MP, after considerable experimentation, 10 applications of the subproblem step (5 barrier, 5 primal), 247 s in total (204 optimization, 43 pricing) (S8 slide 15); a 13-million-column iteration log (S8 slide 16).
- **Abandoned paths.** Not read. [stated] He lists the lessons as a first really fast crossover (based on a result of Megiddo) and enthusiasm for larger models (S8 slide 15).
- **Reception.** [observed, S] 116 Crossref / 164 OpenAlex citations. [practice, P] He still shows sifting in 2022: on an 837-row, 1,322,797-column instance, sifting 11.9 s against barrier 25.9 s, primal 93.1 s, dual 416.0 s; the solver, version and machine are not named on the slide (S8 slide 17). [practice, P] Initial K-variable segments of the same AA model became the aa-series test models of W15 (S7 p. 7 fn. 5).
- **Era and resources.** Cray time, an academic-industrial team of five, two codes (OB1, CPLEX).
- **Method it shows.** CM5 (change the algorithm class: combine barrier, simplex and column subsets).

### SW3 · Solving Real-World Linear Programs: A Decade and More of Progress (W20; OR 2002, sole author)

- **Origin.** [stated, P] An invited paper for the 50th-anniversary issue of Operations Research, written as one person's perspective (S1 p. 3 abstract). He began LP computation as a newcomer: a classroom tableau code, about two years of breaking LPs from Chesapeake Decision Sciences that he fixed one by one without reading the literature, then a first comparison against Marsten's XMP (S1 p. 3).
- **Why then.** [inferred] The anniversary invitation, about 14 years of CPLEX versions (1.0 in 1988 to 7.1), and a library of real models collected over 13 years (S1 p. 12).
- **Key insight.** [stated, P] Machine speed and algorithmic speed each contributed about three orders of magnitude, together about six (S1 p. 14). Machine gains must be estimated separately for simplex and barrier, since barrier gained about ten times more from hardware (S1 p. 5).
- **Minimum evidence and measurement design.** [stated] [practice, P]
  - Anecdotes first: degen4, PDS, a 5-million-row customer LP, a barrier-only car model (S1 pp. 8–11).
  - He rejects the ideal design, running a 1987 code and a current code on one large representative set, because old-code runs on large models would take significant fractions of a year. Instead he chains comparisons forward in time (S1 p. 11).
  - Baseline choice argued: XMP, because MPSX ran on mainframes at most 50 times slower than current workstations and 1989 tests showed MPSX and CPLEX 1.0 comparable on an IBM 3090 (S1 p. 11).
  - Statistics: on the 1988 CPLEX 1.1 vs XMP table, the ratio of totals gives 4.3 and the arithmetic mean of ratios 9.6; he prefers the geometric mean of ratios (4.70) as more robust and more conservative (S1 p. 11).
  - Test set: from the roughly 2,000-model CPLEX LP library, keep only the largest two or three of each model family and drop models solved in under 0.25 s by both versions and all three algorithms, leaving 680 models. Segment by row count, which he found the best simple predictor of difficulty. Use a 350,000-s limit, and report and omit the three models no algorithm solved (S1 pp. 12–13).
  - Chain result: XMP → CPLEX 5.0 about 103; about 960 for models with at least 50,000 rows, close to the machine factor; about 2,400 with barrier included (S1 p. 13).
  - Algorithm comparison: dual about twice as fast as primal, barrier fastest by a narrow, growing margin; but each algorithm wins a significant number of models, so best-of-three beats every single one (S1 p. 13).
- **Abandoned paths.** [stated, P] The degen4 episode: CPLEX 1.0 on a Cray Y-MP made no progress for seven hours, and some concluded that simplex should be dropped for barrier, which he calls wrong (S1 p. 8). A re-run of CPLEX 1.0 on the paper's 667 MHz Compaq ES40 solved it in about 1.5 days after a stall of 4,897,095 iterations; perturbation alone cut that to about half an hour (S1 p. 8). Simplex-internals detail is deferred to a then-forthcoming Applegate–Bixby–Chvátal–Cook book (S1 pp. 6, 9); whether the published TSP book contains it was not checked.
- **Reception.** [observed, S] His most cited LP work (§1.7). [practice, P] He reuses it as the reference for every later LP progress slide, noting an update made in 2004 (S2 p. 113; S8 slide 28). The 2004 update itself was not found as a publication.
- **Era and resources.** ILOG CPLEX division; a 667 MHz Compaq ES40 bank; the CPLEX model library; old binaries recompiled or re-run.
- **Method it shows.** CM1, CM2, CM3, CM4, CM5.

### SW4 · MIP: Theory and Practice — Closing the Gap (W19; IFIP 2000, five authors, "we")

- **Origin.** [stated, joint, P] Commercial MIP had stayed with LP-based branch-and-bound while decades of theory had not reached commercial codes; CPLEX 6.5 changed that (S11 pp. 1–3). [stated, P] In his own later words, 6.5 was a systematic programme to mine that backlog, done by Gu and Rothberg (S2 p. 117; S3 pp. 3–4).
- **Why then.** [stated, joint, P] For LP, the 1999 starting observation was simply that LPs had become larger. That led them to models with at least 10,000 rows and to the simplex bottleneck in the FTRAN/BTRAN solves (S11 p. 5).
- **Key insight.** [stated, joint, P] MIP needs a barrage of different but cooperating techniques with good defaults, each implemented to help when it can and hurt as little as possible, with automatic switch-off; unlike theoretical studies that test one idea in isolation (S11 pp. 3, 12–13). For LP the target was robustness and scalability, with no degradation on the middle range of models that dominates practice (S11 p. 6).
- **Minimum evidence.** [practice, joint, P]
  - LP: small models segmented by CPLEX 5.0 solve time (0–1, 1–10, 10–100 s) with geometric means; the gains there were a surprise (S11 p. 7).
  - Large LPs: at least 10,000 rows after presolve, near-duplicates and smaller family members removed, a 0.5 GB memory limit, a 500,000-s time limit, and time-outs counted at the limit, which they state underestimates the gain (S11 pp. 8–9).
  - Win counts are reported beside the geometric means. Biases against barrier are stated: x86 floating point and an unused parallel barrier (S11 pp. 10–12).
  - MIP on MIPLIB 3.0 is partitioned into: 22 easy models, 10 solved only by 6.5, 8 solved by neither (compared by gap, 3.3), and 19 hard but solved by both (11.2× faster) (S11 p. 20).
  - A preferred proprietary set of 80 models that looked difficult but were solvable when tuning was allowed. It was built by dropping models solved under 100 s and then running the rest for days with varied parameters (S11 pp. 20–21).
  - 6.5 defaults vs 6.0 defaults: 22.3×; vs tuned 6.0: 3.8× (S11 p. 21).
  - Two-direction ablation: switch features off one at a time, and add cut classes one at a time to a no-cuts base. Gomory cuts were the biggest winner and the biggest surprise (S11 pp. 21–22).
  - Counter-examples where defaults are not enough, such as probing (S11 pp. 22–24).
- **Abandoned paths.** [stated, joint, P] The historical neglect of Gomory cuts is explained as a wrong usage (one cut at a time, no branching), not a weak cut (S11 pp. 17–18). [stated, joint, P] Their own 1998 verdict that barrier was clearly best for large LPs was replaced by the view that no single algorithm is clearly best (S11 p. 12).
- **Reception.** [observed, S] 128 Crossref citations; a copy is kept in the MIPLIB 2003 bibliography (S36). Achterberg and Wunderling (S38) describe the 2004 follow-up (W21) as an analysis of MIP features up to CPLEX 8.0 prepared in 2001, and propose their own way to analyze benchmark results, which they call unbiased — a continuation and implicit critique of the method.
- **Era and resources.** ILOG CPLEX division team; 400 MHz Pentium II and 500 MHz Alpha 21264 machines; the proprietary CPLEX library.
- **Method it shows.** CM2, CM6, CM7. **Authorship:** joint; not evidence that Bixby wrote the MIP or LP code described (see §0).

### SW5 · A Brief History of Linear and Mixed-Integer Programming Computation (W26; Documenta 2012, sole author) and the deck series (T3, T6, T7)

- **Origin.** [stated, P] An invited history for the ISMP 2012 volume, built partly on e-mail exchanges with Ashford, Gregory, Rothberg, Shaw and Tomlin (S2 p. 118).
- **Why then.** [inferred] 2012 ISMP history volume; Gurobi had reached version 5.0.
- **Key insight.** [stated, P] Consecutive-version ratios, multiplied, give a projected machine-independent MIP speed-up of over 29,000 from CPLEX 1.2 to 11. The biggest single steps were 3.0/2.1 (about 5.5, the maturing dual simplex) and 6.5/6.0 (over 10, 1998). CPLEX 6.0 was the arguable exception to a significant gain (S2 p. 117). With 6.5, he writes, an out-of-the-box solver with default settings could, arguably for the first time, solve a significant fraction of non-trivial real MIPs (S2 p. 117).
- **Minimum evidence (protocol).** [stated] [practice, P] In late 2007 he ran the test himself:
  - a library collected over almost twenty years, a 1,892-model test set, a bank of identical machines;
  - the twelve CPLEX releases from 1.2 to 11 recompiled for the target machine, a 30,000-s limit;
  - each consecutive pair compared on the models solved to optimality by at least one of the two, with the time limit used for unsolved runs, and geometric means of the ratios (S2 p. 116).
  - Gurobi 1.0 was about equivalent to CPLEX 11.0 on Mittelmann's 2009 benchmarks; Gurobi 1.0 → 5.0 gave 16.2 with the same ratio method (S2 pp. 117–118).
  - The ECCO deck adds the screening: 2,791 MIPs, minus 559 easy ones, 348 duplicates and 22 models blocked by hard LPs; pure defaults (S9 slide 30).
  - For LP he restates 3,300 algorithmic × 1,600 machine, about 5.3 million, 1988–2004. The algorithmic factor compares old primal with the new best of primal, dual and barrier — a choice he says one can argue about (S2 pp. 113–114; S8 slide 28).
- **Abandoned paths / open problems.** [stated, P] About 2% of real MIPs are blocked by LP difficulty, and since 2004 there have been essentially no improvements in standard LP algorithms (S2 p. 115; same in S9 slide 16). In 2022 he amends this: no significant gains 2004 to about 2015, then about 3× for simplex on large models in the last seven years (S8 slide 28).
- **Reception.** [observed, S] 127 Crossref / 228 OpenAlex citations.
- **Era and resources.** The measurement was run in late 2007 on twelve old CPLEX releases that he recompiled (his affiliation at that moment was not checked), and later presented under Gurobi copyright in the decks.
- **Method it shows.** CM2, CM3, CM4. Numbers differ across the deck series (C7–C9).

### 2.6 The missing signature work: bound shifting

- [stated, P] He says he thinks shifting was his most important contribution. He says it came from tolerance-based ideas (Harris's ratio test, which Fourer pointed him to), took about two weeks of struggle with non-monotone steps, and ended with a simple fix: change the bound, then reset the bounds and re-solve at the end. He adds that there is no paper because he never got around to it (S3 p. 4).
- [practice, P] Written traces are one paragraph in OR 2002, where shifting, perturbation and Harris's ratio test form CPLEX's anti-degeneracy package (S1 p. 7), and the dual-side cost shifting described in W15 (S7 p. 3). The 1992 paper had listed a bound-perturbation part as planned (S6 p. 2).
- [observed, P] The interviewer urged him to write a paper about bound shifting (S3 p. 6).
- [inferred] The work he values most is visible only as practice and interview statements, not as a publication — a gap the skill must state, not fill.

### 2.7 Failure exemplar: Parallelizing the Dual Simplex Method (W15; SC-95-45, joint with Martin)

- [stated, joint, P] They chose the dual over the primal because primal partial pricing removes parallelism and because the target was reoptimization in integer programming (S7 p. 1). They profiled first: 24.0% of the work was parallelizable on pilots, 97.3% on aa300000 (S7 p. 4).
- [practice, joint, P] Negative results are reported in full:
  - The first PVM version on Ethernet was about 3.3 times slower than sequential (S7 p. 7). A SUN S20-502 was worse than Ethernet (S7 p. 9). They saw little hope for distributed memory on general problems (S7 p. 9). They judged the System V semaphore version unsatisfactory, with about 40% degradation from the memory bus alone (S7 pp. 11–12).
  - Attempts to run the two FTRANs in parallel degraded performance (S7 p. 17). Superlinear and sublinear anomalies were left unexplained (S7 p. 17).
  - A control in the sequential code: a superlinear speedup on aa400000 turned out to come partly from the column partition, so they applied the same partition to the sequential baseline (S7 p. 15).
  - The reorganised code was kept identical for sequential runs, to preserve code unity (S7 p. 16).
- [stated, joint, P] Only the thread-based PowerC version on SGI gave good results over a wide range of models (S7 p. 20).
- [practice] Preprint December 1995, journal 2000 (S16). The review history is unknown.
- [stated, P] Later he writes that simplex has not been parallelized successfully in the sense barrier has (S1 p. 7), and that there has been essentially no success (S2 p. 114). See C12.

---

## 3. Failures, abandoned directions, unwritten papers

| # | Item | Evidence | Tag |
|---|---|---|---|
| F1 | Planned CPLEX simplex series stopped after Part I/II (start basis); planned parts (composite Phase I, partial pricing, bound perturbation, vectorization) not found | S6 p. 2; DBLP/Crossref/OpenAlex search | [practice] P; abandonment [inferred] |
| F2 | Bound shifting, his self-declared most important contribution, never written up | S3 p. 4 | [stated] P |
| F3 | First self-test against XMP on standata: about 7× slower, then about 2× after two weeks; XMP was lucky with its start basis (iteration counts) | S3 p. 2; T1 shows LOPT 181 iterations / 14.7 s vs XMP 75 / 8.1 s on STANDAT, the only problem XMP won | [stated] [practice] P |
| F4 | degen4/LAU2: CPLEX 1.0 stuck for seven hours on a Cray; barrier recommended instead; led to anti-degeneracy work and the dual simplex | S1 p. 8; S3 p. 3; S8 slides 20–22 | [stated] P |
| F5 | OSL was better until about 1992; CPLEX could not break into airlines until a merger due diligence made parallel barrier a must-have (until then a 40× gain had been only a nice-to-have) | S3 p. 3; S8 slides 18–19 | [stated] P |
| F6 | Early CPLEX MIP lagged research codes such as MINTO; CPLEX 6.0 was the arguable exception to version-to-version progress | S3 p. 3; S2 p. 117 | [stated] P |
| F7 | Distributed-memory and semaphore parallel dual simplex failed; anomalies unexplained | S7 pp. 7–17 | [practice, joint] P |
| F8 | 1987–88: no success at all in getting funding for LP-computation research | S8 slide 9 | [stated] P (see C14) |
| F9 | "Finding Embedded Network Rows … I" announces a second part (augmentation) that was not found in Crossref or DBLP | S18 abstract | [practice] P; not established |
| F10 | MIPLIB 3.0 promised yearly updates; the next library found is MIPLIB 2003 by Achterberg, Koch and Martin (ORL 2006), without him | S12 p. 12; S39 | [practice] P; [inferred] |
| F11 | The 2004 update of the LP progress figures is cited but not found as a publication | S2 p. 113; S8 slide 28 | [practice]; not found |
| F12 | Retracted claims, rejected papers, errata | none found | — |

---

## 4. Candidate methods surfaced by this dimension (for Phase 2 cross-checking)

Not yet validated (Agents 02–03 and Phase 2 decide). Each lists where it appears.

- **CM1 Instance-driven development: real models that break the code set the agenda.** Chesapeake's breaking LPs (S1 p. 3; S3 p. 2), degen4/LAU2 and Saigal's max-cut problems (S1 p. 8; S3 p. 3), the AA challenge (S8 slides 14–15), and the 1999 observation that LPs had become larger (S11 p. 5). [stated] ×4 and [stated, joint] ×1.
- **CM2 Measure on a screened library of real models with geometric means of per-model ratios.** Remove easy models, duplicates and smaller family members; segment by size or baseline time; state how time-outs and failures are counted. Sources: S6 pp. 20–21; S1 pp. 11–13; S11 pp. 3, 7–9, 20–21; S2 p. 116; S9 slide 30; S12 p. 14. Spans 1992–2017.
- **CM3 Chain version comparisons forward in time when direct runs are impractical, and label products as projections.** Anchor them with occasional full old-code runs: CPLEX 1.0 ran for 29.8 days on a 401,640-row production-planning LP, starting in Houston on 13 Nov 2002 (S9 slides 9–14; S8 slides 24–27). [inferred] The slides' place-and-date stamps (Berlin, Dagstuhl, Amsterdam, Houston) suggest he checked the run while travelling, finishing around 12 December. Sources: S1 p. 11; S2 p. 117.
- **CM4 Separate machine from algorithm, and treat algorithm classes separately.** Simplex and barrier get separate machine factors (S1 p. 5); a best-of-three caveat (S2 p. 114); win counts beside means (S1 p. 13; S11 pp. 10–11); heavy-tailed effects make means over small sets misleading (S10 slide 26).
- **CM5 When stuck, change the algorithm or formulation class.** Look at the dual (S1 p. 8; S8 slide 21); combine barrier, simplex and sifting (S8 slides 14–15).
- **CM6 Defaults that help when they can and hurt as little as possible.** Non-regression on the middle range and automatic switch-off (S11 pp. 3, 6–7, 12–13); a start basis that avoids a bad basis rather than seeking a good one (S6 p. 17).
- **CM7 Two-direction ablation** (S11 pp. 21–22; S10 slide 11 shows per-feature factors on 78 models without stating the protocol).
- **CM8 Report negative results, controls and anomalies** (S7 throughout; S1 p. 8; S2 p. 117).
- **CM9 Decide what to build from how solvers are embedded.** The callable library served IP research (S1 p. 4; S2 p. 116; S3 p. 3). Crossover is integral because MIP needs a basis (S1 p. 13; S2 p. 114). The dual is chosen for reoptimization (S7 p. 1).

---

## 5. Era and resource context

| Period | Compute | Team and position | Test material |
|---|---|---|---|
| Early 1980s – 1987 | IBM PC, Sun 3/50 (on his desk late 1987) | Matroid theorist at Northwestern, then Rice; the code was a home hobby (S3 p. 2); Fourer as informal teacher | Chesapeake SLP snapshots (condition numbers up to about 10^20, S3 p. 2); netlib (about 20 tiny problems at first, S3 p. 2) |
| 1988–1997 | SPARCstation 2, Cray X-MP/Y-MP via Gregory, HP9000/730, SGI Power Challenge, IBM SP2 | CPLEX Optimization founder; sole developer at first, still developing in 1997; Rice professor; NSF/AFOSR/CRPC grants | netlib; proprietary CPLEX customer models (S7 p. 7) |
| 1997–2008 | 300 MHz UltraSparc, 400 MHz Pentium II, 500 MHz Alpha, 667 MHz Compaq ES40, 2.0 GHz Pentium 4 | ILOG CPLEX division with Gu, Rothberg, Wunderling, Fenelon, Lustig, Gregory | CPLEX LP library (about 2,000 models over 13 years, S1 p. 12); MIP library (2,791 models, S9 slide 30) |
| Late 2007 – | A bank of identical machines for the 2007 version test (S2 p. 116); a 4-core i7-920 for the 2012 trick timings (S10 slide 34) | Gurobi co-founder from 2008; no development; testing and business (S3 pp. 4–5) | 600 models in two days from the web and NEOS, about 10,000 by 2015, about 3,500 in the real test set (S3 p. 6); a Gurobi MIP library of 3,550 models plotted in 2017 (S9 slides 34–35) |

---

## Contradictions

Kept as found; not reconciled.

- **C1 Size of the first LP solved (Stigler diet).** 9 constraints and 77 variables (S1 p. 5; S8 slide 4; S9 slide 4) vs 21 constraints and 77 variables (S2 p. 107).
- **C2 First XMP comparison.** About twice as fast on average over a netlib subset (S1 p. 3) vs about four times faster on almost all models within a week (S3 p. 2).
  - The 1986 handwritten table (T1, 13 problems) gives, by my reading of the handwriting and my computation, a geometric mean of 1.79 (arithmetic 2.01, ratio of totals 2.14) [inferred].
  - The 1988 CPLEX 1.1 vs XMP table gives a geometric mean of 4.70 (S1 p. 11).
- **C3 standata.** About a thousand rows, solved by XMP in 70 iterations (S3 p. 2) vs 359 rows and 75 XMP iterations in the 1986 table (T1) and 359 rows in S6 Table I.
- **C4 degen4 vs LAU2 (same dimensions: 4,420 × 6,711, 101,377 nonzeros).**
  - OR 2002: degen4, presented late 1989 as a challenge; CPLEX 1.0 on a Cray Y-MP, seven hours, still infeasible (S1 p. 8).
  - Optima: LAU2 from John Gregory; CPLEX version 1.x or perhaps 2; seven hours on a Cray Y-MP, stuck in Phase I (S3 p. 3).
  - Hausdorff: LAU2, late 1980s, a challenge from United Airlines; Step 1 dated 1987, CPLEX 1.0 on a Cray X-MP (S8 slides 20–21), although CPLEX 1.0 was released in 1988 (S1 p. 4).
  - That degen4 and LAU2 are one model is [inferred] from the identical sizes.
- **C5 Origin of shifting.** He developed bound shifting himself after two weeks of struggle, starting from Harris's ratio test (S3 p. 4) vs a joint 1995 preprint pointing to Gill, Murray, Saunders and Wright (1989) for the approach that suggested this shifting (S7 p. 3).
- **C6 Company dates.** Incorporated 1987 (S3 p. 3) vs founded 1988 (S8 slide 9). The Amoco licence went through around 1986, he thinks (S3 p. 3), vs first sale to Amoco in 1987 (S8 slide 9).
- **C7 Size of the CPLEX MIP version test set.** 1,892 models (S2 p. 116) vs 1,852 (S9 slide 30). The slide's own counts give 2,791 − 559 − 348 − 22 = 1,862 [inferred arithmetic].
- **C8 Gurobi 1.0 → 5.0.** 16.2× (S2 p. 118; S10 slide 8: 2.2, 2.9, 1.3, 1.9) vs 9.3× (S9 slide 36: 2.2, 1.9, 1.3, 1.7) for the same version pairs. Neither source states the test set or machine behind the factors.
- **C9 ECCO arithmetic.** Over 1.3 million times since 1991 (S9 slide 36) vs the product of the displayed factors, 29,530 × 43.2 ≈ 1.28 million [inferred arithmetic]. The Fields deck gives 475,000 = 29,530 × 16.2 (S10 slide 9).
- **C10 Barrier vs simplex verdicts, by date.**
  - 1994: Lustig, Marsten and Shanno overstate barrier, which does not dominate large problems (S13 abstract).
  - 1998 (as recalled in 2000): barrier clearly best for large models; 2000: no clear best (S11 p. 12).
  - 2002: barrier is CPLEX's most powerful single algorithm by a narrow, growing margin, but simplex dominates in practice because of MIP re-solves (S1 pp. 7, 13).
  - 2012: barrier increasingly the winner for large LPs from scratch (S2 p. 114).
- **C11 LP progress after 2004.** Essentially none (2012, S2 p. 115) and little (2017, S9 slide 16) vs about 3× on large models in the seven years before 2022 (S8 slide 28). The 2015–2017 window conflicts between S9 and S8.
- **C12 Parallel simplex.** The thread-based dual worked well over a wide range of models (S7 p. 20) vs simplex not successfully parallelized (S1 p. 7) and essentially no success (S2 p. 114).
- **C13 Theory vs LP research.** LP was not research for him, only play, and he never looked in the literature (S3 p. 2; S1 p. 3) vs his 1980–1989 publications and AFOSR-funded reports on LP structure and LP tools (W1–W6). A tension between computational and structural LP; not resolved here.
- **C14 Funding.** No success at all funding LP-computation research in 1987–88 (S8 slide 9) vs AFOSR reports on LP tools for IP dated October 1989 and October 1992 (W6, W11) and NSF CCR-8815914 plus AFOSR-90-0273 acknowledged in 1992 (S6 p. 1). Different years; left open.
- **C15 Size of the AA model.** 12,753,313 variables (S14 abstract; S8 slide 14) vs 12,753,312 (S7 p. 7 fn. 5).
- **C16 Citation slip.** Documenta cites OR 2002 as pp. 1–13 (S2 ref. [7]); the paper is pp. 3–15 (Crossref).
- **C17 Page range of W19.** 19–49 (Crossref) vs 19–50 (DBLP; S36).
- **C18 OSL attribution.** OSL credited to John Forrest alone (S6 p. 2, 1992, German original) vs developed primarily by John Forrest and John Tomlin (S2 p. 113, 2012).
- **C19 Code name.** The 1986 slide is titled "1st Public CPLEX Results", but the handwritten table names the code LOPT (S8 slide 11). That LOPT was the pre-CPLEX name is [inferred].

## Gaps

- **Not read (paywall or not reached):**
  - full texts of W8 (OR 1992), W12 (1994 commentary), the English journal versions of W7 and W15 (the German translation and the preprint were read), W13 (ScienceDirect 403), W5 (abstract only), W21, W23, W25, W18, W16, W27 (abstract only);
  - all DTIC reports (apps.dtic.mil under maintenance on 2026-11-05), the 1981 and 1984 chapters, SIAM News 1992 (W10).
- **Not found:**
  - the 2004 update of the LP progress figures (F11);
  - any later part of the planned CPLEX series (F1) or of the embedded-network-rows paper (F9);
  - a Tutte Colloquium 2013 deck;
  - any Bixby deck for days other than Monday at the 2022 Hausdorff School (folder listing 403).
- **Unreachable:** the 2015 deck once at people.bath.ac.uk (redirects); the Rice homepage content (Flash only).
- **Unknown:**
  - the test set and machine behind the 2017 Gurobi factors (C8);
  - the protocol behind the 78-model feature factors (S10 slide 11);
  - the solver, version and machine of the 2022 sifting table (S8 slide 17);
  - the review history of SC-95-45 → IJOC 2000.
- **OpenAlex** not re-queried: the split record A5097662446 was not inspected (§1.1 gives only a candidate).
- **Huangfu's 2013 thesis**, which relays Bixby second-hand: not read (the originals were read instead).
- **No rejected papers, referee reports, errata or retractions** were found.
- **Living status and present role:** not addressed, by design (team.json).

## Sources

Primary — read:
- S1 Bixby, "Solving Real-World Linear Programs: A Decade and More of Progress", Operations Research 50(1):3–15, 2002, DOI 10.1287/opre.50.1.3.17780; read via www.gwern.net/doc/cs/algorithm/2002-bixby.pdf — primary
- S2 Bixby, "A Brief History of Linear and Mixed-Integer Programming Computation", Documenta Math. Extra Vol. ISMP (2012) 107–121, DOI 10.4171/dms/6/16; www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-ismp/25_bixby-robert.pdf — primary
- S3 "You have to figure out who your customer is going to be: An interview with Bob Bixby" (Kaibel, Lee, Linderoth, Oct 2015), Optima 101, Sept 2016, pp. 1–6, mathopt.zib.de/Optima-Issues/optima101.pdf — primary
- S4 M. Grötschel, "Comments on Bob Bixby's interview: Mathematics and the Real World", Optima 101, Sept 2016, pp. 6–7 (same URL) — primary (observed)
- S5 W. Cook, "Comments on Bob Bixby's interview: Beauty in the Details", Optima 101, Sept 2016, p. 7 (same URL) — primary (observed)
- S6 Bixby, "Das Implementieren des Simplex-Verfahrens: Die Startbasis", ZIB Preprint SC 92-11, April 1992, opus4.kobv.de/opus4-zib/files/81/SC-92-11.pdf (via WebFetch; scanned with OCR layer) — primary
- S7 Bixby and A. Martin, "Parallelizing the Dual Simplex Method", ZIB Preprint SC-95-45, December 1995, opus4.kobv.de/opus4-zib/files/211/SC-95-45.pdf (via WebFetch) — primary
- S8 Bixby, "Linear Programming: A Historical View" (deck), Hausdorff School on Computational Combinatorial Optimization, Bonn, September 2022, www.or.uni-bonn.de/~held/hausdorff_school_22/slides/GUR_Hausdorff_Day1_LP_History.pdf — primary
- S9 Bixby, "Computational Progress in Linear and Mixed Integer Programming" (deck), ECCO 2017, May 2017, ecco2017.euro-online.org/en/resources/files/invited-speakers/robertbixby.pdf — primary
- S10 Bixby, "1000X MIP Tricks" (deck), Fields Institute, 12 June 2012, av.fields.utoronto.ca/programs/scientific/11-12/bc65/rbixby.pdf — primary
- S11 Bixby, Fenelon, Gu, Rothberg, Wunderling, "MIP: Theory and Practice — Closing the Gap", System Modelling and Optimization, Kluwer 2000, pp. 19–49, DOI 10.1007/978-0-387-35514-6_2; preprint read at miplib2010.zib.de/miplib2003/paper/bixbyfenelongurothbergwunderling2000.pdf — primary
- S12 Bixby, Ceria, McZeal, Savelsbergh, "An Updated Mixed Integer Programming Library: MIPLIB 3.0", Optima 58, June 1998, pp. 12–15, mathopt.zib.de/Optima-Issues/optima58.pdf — primary

Primary — abstract or metadata only:
- S13 Bixby, "Commentary—Progress in Linear Programming", ORSA J. Comput. 6(1):15–22, 1994, DOI 10.1287/ijoc.6.1.15 (abstract via Crossref) — primary
- S14 Bixby, Gregory, Lustig, Marsten, Shanno, "Very Large-Scale Linear Programming: A Case Study in Combining Interior Point and Simplex Methods", Operations Research 40(5):885–897, 1992, DOI 10.1287/opre.40.5.885 (abstract via Crossref and IDEAS) — primary
- S15 Bixby, "Implementing the Simplex Method: The Initial Basis", ORSA J. Comput. 4(3):267–284, 1992, DOI 10.1287/ijoc.4.3.267; report DOI 10.21236/ada453079 (abstract via Crossref) — primary
- S16 Bixby and Martin, "Parallelizing the Dual Simplex Method", INFORMS J. Comput. 12(1):45–56, 2000, DOI 10.1287/ijoc.12.1.45.11902 (Crossref) — primary
- S17 Bixby and Saltzman, "Recovering an optimal LP basis from an interior point solution", Oper. Res. Lett. 15(4):169–178, 1994, DOI 10.1016/0167-6377(94)90074-4 (Crossref) — primary, not read
- S18 Bixby and Fourer, "Finding Embedded Network Rows in Linear Programs I. Extraction Heuristics", Management Science 34(3):342–376, 1988, DOI 10.1287/mnsc.34.3.342; report DOI 10.21236/ada455195 (abstract via Crossref/IDEAS) — primary
- S19 Bixby and Cunningham, "Converting Linear Programs to Network Problems", Math. Oper. Res. 5(3):321–357, 1980, DOI 10.1287/moor.5.3.321 (abstract via S32) — primary
- S20 Bixby, Fenelon, Gu, Rothberg, Wunderling, "Mixed-Integer Programming: A Progress Report", The Sharpest Cut, MPS-SIAM 2004, pp. 309–325, DOI 10.1137/1.9780898718805.ch18 — primary, not read
- S21 Bixby and Rothberg, "Progress in computational mixed integer programming—A look back from the other side of the tipping point", Annals of OR 149(1):37–41, 2007, DOI 10.1007/s10479-006-0091-y — primary, not read
- S22 Koch et al., "MIPLIB 2010", Math. Program. Comput. 3(2):103–163, 2011, DOI 10.1007/s12532-011-0025-9 — primary, not read
- S23 Achterberg, Bixby, Gu, Rothberg, Weninger, "Presolve Reductions in Mixed Integer Programming", INFORMS J. Comput. 32(2):473–506, 2020, DOI 10.1287/ijoc.2018.0857 (abstract via IDEAS) — primary
- S24 Bixby, Boyd, Indovina, "A Test Set of Real-World Mixed Integer Programming Problems", DTIC report, 1992, DOI 10.21236/ada455431 — primary, not read
- S25 Bixby, DTIC reports: "Hidden and Embedded Structure in Linear Programs" (1983, DOI 10.21236/ada137773); "Linear Programming Tools for Integer Programming" (1989, DOI 10.21236/ada219013); "Linear-Programming Tools in Integer Programming: The Traveling Salesman" (1992, DOI 10.21236/ada261398); report versions of W7 and W8 (DOIs 10.21236/ada453079, 10.21236/ada452700) — primary, not read
- S26 Bixby, "Hidden Structure in Linear Programs", 1981, DOI 10.1016/b978-0-12-299680-1.50024-0; "Recent Algorithms for Two Versions of Graph Realization and Remarks on Applications to Linear Programming", 1984, DOI 10.1016/b978-0-12-566780-7.50009-x — primary, not read
- S27 Bixby, Cook, Cox, Lee, "Computational experience with parallel mixed integer programming in a distributed environment", Annals of OR 90:19–43, 1999, DOI 10.1023/A:1018960631213 — primary, not read
- S28 Bixby and Lee, "Solving a Truck Dispatching Scheduling Problem Using Branch-and-Cut", Operations Research 46(3):355–367, 1998, DOI 10.1287/opre.46.3.355 — primary, not read
- S29 Other MIP and application items (W14, W22, W24, the 1996 subgradient chapter, market split, IPCO 1998), identifiers in §1.2 — primary, not read
- S30 Context items: Billera–Bixby game theory, matroids, TSP (identifiers in §1.2) — primary, not read

Secondary:
- S31 DBLP person 75/1779 via `scripts/dblp_works.py` (sparql.dblp.org), 2026-11-05 — secondary
- S32 OpenAlex author A5012463224 summary in `references/sources/publications/` (generated 2026-11-05, before this run) — secondary
- S33 Crossref REST API records for all DOIs above, api.crossref.org, 2026-11-05 — secondary
- S34 Mathematics Genealogy Project, "Robert Eugene Bixby", id 14993, mathgenealogy.org/id.php?id=14993 — secondary
- S35 Hausdorff School on Computational Combinatorial Optimization 2022, program page, www.or.uni-bonn.de/~held/hausdorff_school_22/ — secondary
- S36 MIPLIB 2003 bibliography, miplib2010.zib.de/miplib2003/biblio.html — secondary
- S37 Imperial College, seminar listing "Computational Progress in Linear and Mixed Integer Programming", 13 May 2015, optimisation.doc.ic.ac.uk/events/2015-05-13 — secondary
- S38 Achterberg and Wunderling, "Mixed Integer Programming: Analyzing 12 Years of Progress", Facets of Combinatorial Optimization, Springer 2013, pp. 449–481, DOI 10.1007/978-3-642-38189-8_18 (abstract via IDEAS) — secondary
- S39 Achterberg, Koch, Martin, "MIPLIB 2003", Oper. Res. Lett. 34(4):361–372, 2006, DOI 10.1016/j.orl.2005.07.009 (Crossref) — secondary
- S40 IDEAS/RePEc abstract pages for Operations Research 40(5), Management Science 34(3) and INFORMS J. Comput. 32(2), ideas.repec.org — secondary
- S41 Rice homepage, www.cmor-faculty.rice.edu/~bixby/ (redirect from www.caam.rice.edu/~bixby/), Flash only, not read — secondary
