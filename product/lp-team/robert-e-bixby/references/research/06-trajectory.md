# Robert E. Bixby: research trajectory (research agent 06)

- **Researcher**: Robert E. Bixby (Robert Eugene Bixby in the Mathematics Genealogy Project; "Bob" in interviews and bios). BS UC Berkeley 1968; MS 1971 and PhD 1972 in operations research, Cornell, with a matroid dissertation under Louis J. Billera. Faculty posts at Kentucky, Northwestern and Rice, where he is Noah Harding Professor Emeritus of Computational and Applied Mathematics. Co-founder of CPLEX Optimization (1987 or 1988; the sources disagree) and of Gurobi Optimization (2008). DBLP pid 75/1779; OpenAlex A5012463224, plus the split record A5097662446 that holds the 2000 IFIP MIP paper. **Name collisions** found in this run: a different Robert Bixby (Concord Coalition) in a stock-insider listing, and the NSF-funded neuroscientist John L. Bixby. Neither is this person.
- **Dimension**: research trajectory. The note covers the dated timeline, lineage, the turns and what triggered them, entry and exit relative to the consensus, the era and resource context, failures and abandoned lines, the authorship and role labels by period, and the latest dated traces and last 12 months. It serves framework layer 2 (problem choice, timing) and layer 7 (organisation), with pointers for layers 1, 4 and 5.
- **Lens (team.json)**: decision and measurement craft for LP (1987–2002) and for MIP (CPLEX and Gurobi progress measurement). Matroid and TSP work are context only, used here where they explain a turn.
- **Research date**: 2026-11-05.
- **Sources consulted**: 49 (38 primary, 11 secondary), numbered P1–P23, O1–O15 and S1–S11 under "Sources". **WebSearch calls used: 7 of 7.** Everything else was fetched with curl, WebFetch, the NSF Award API, the Crossref and OpenAlex APIs, and `scripts/dblp_works.py` (read-only, with output in scratch).
- **Local corpus**: `references/sources/{papers,talks,essays,software}` held only `.gitkeep`. **Nothing below is from user-supplied material.** `publications/` holds an OpenAlex summary generated on 2026-11-05, used only as a lead (S10). `private/` was not opened. I saved no transcript myself.
- **Transcripts saved during this run by a sibling agent** (in `talks/`; not user-supplied): the 2023 *Subject to* interview (excerpt), the 2021 Toronto talk, the 2015 CO@Work lectures, and two short clips. All are YouTube caption text and not speaker-checked. Three use automatic captions, which garble names; the CO@Work lectures use uploaded subtitles. I read the 2023 and 2021 transcripts for trajectory statements, and I checked each video's identity and upload date myself through YouTube oEmbed and the watch-page metadata (P20–P23). Everything from them is paraphrased and tagged as caption text.
- **Sibling notes**: `01-publications.md` appeared while this note was being written. I read it only as a lead. It pointed me to the Fields 2012 deck and two early LP-structure chapters, and I re-fetched or re-verified each of them myself. Notes 02–05 did not exist at writing time.
- **Living status and present role: not established by any source read here. This note states neither.** team.json leaves out the `living` key by design and overrides the task prompt's "living" tag. §8 lists the latest dated traces neutrally.
- **Quotation policy**: findings are paraphrased with pinpoint pages. The note quotes exactly one short verbatim phrase, in §7. Check the exact wording at the cited page before quoting downstream.

### How the evidence was gathered (and what failed)

- **Read in full** (curl or WebFetch-saved PDF, then pdftotext):
  - P1–P3: Optima 101, the interview and both comments.
  - P4: OR 2002, from the gwern mirror.
  - P5: Documenta 2012.
  - P6: ZIB SC 92-11, the German OCR text. I read the text pages and skimmed the tables.
  - P7: ZIB SC-95-45.
  - P8: the Hausdorff 2022 deck, including the image-only 1986 results slide, which I rendered and transcribed.
  - P9: the ECCO 2017 deck.
  - P10: the Fields 2012 deck.
  - P11: Optima 58, the MIPLIB 3.0 article and the p. 2 notice.
  - Institutional pages O1–O15.
  - MGP records S4.
- **Read as abstract, metadata or byline only**: P12–P19, plus Crossref records for every DOI cited.
- **Page conventions**:
  - OR 2002: printed p. N = PDF p. N−2.
  - Documenta: printed p. = PDF p. + 106 (pp. 107–121).
  - Optima 101 and 58: printed = PDF.
  - SC 92-11 and SC-95-45: printed p. N = PDF p. N+1.
  - Hausdorff deck: cited by the printed slide footer, with the PDF page added. Slide = PDF p. + 1 up to PDF p. 15, and + 2 from PDF p. 17. PDF p. 11, the 1986 sheet, has no footer and is slide 12 by sequence.
  - ECCO 2017 and Fields 2012: slide = PDF p.
- **Not reached (not routed around)**:
  - ZIB OPUS PDFs: curl hit an Anubis bot wall. WebFetch then delivered both PDFs and the SC 92-11 front-door page.
  - profiles.rice.edu: HTTP 406 to curl. Read via WebFetch instead. A retry with browser-like headers was refused by the session's safety classifier and was not pursued.
  - The 2015 Gurobi CEO-to-CSO release: PRWeb returned 403 and www-old.gurobi.com returned 503. The gurobi.com newsroom page did not render its text. Only the title and a snippet were seen in search results.
  - A Gurobi GOR 2024 event page: 404.
  - A "Subject to" podcast page on player.fm: 403.
  - The NAE member profile: it sits behind a confirmation gate, so it was not read.
  - DTIC PDFs: 403.
  - INFORMS journal full texts: not attempted, since team.json records 403.
  - web.archive.org: not used.
- **MGP**: on 2026-11-05 the site was recovering from an outage. Its notice is dated 4 Nov 2026, and the quick search and individual pages worked. Records 14993 (Bixby), 26980 (Billera) and the nine students' pages were read.

### Tag legend

- **[stated]**: Bixby's own words in a sole-author text, his interview, his own deck, or a grant abstract filed under his name as sole PI.
- **[stated-joint]**: co-signed text whose voice ("we") cannot be split among the authors.
- **[practice]**: what the record shows was done: papers and their bylines, test runs, grants, releases.
- **[observed]**: what others recorded: colleagues, institutions, prize lists, databases, event bios. An event bio may have been supplied by the speaker, but its author is not identified.
- **[inferred]**: my synthesis, to be treated as a hypothesis.
- **P / S**: primary / secondary source.

---

## 0. The trajectory in one paragraph (all [inferred], built from the sections below)

Bixby spent about the first fifteen years of his career (1970–1985) as a **matroid theorist**. The bridge out ran through **hidden network structure in LPs** (1980–1986), a theory-to-LP line whose grant and report titles already named linear programs. It also produced the personal contact (Tom Baker) that later pulled him into industrial code. The **PC** (early 1980s) and a **teaching need** started a classroom LP code (1983). A **customer channel** (Chesapeake's MIMI, 1985–87) fed it failing real LPs for two years. **External validation** (a buyer, then a first benchmark against XMP, 1986) turned the hobby into research. A **funding failure** for LP computation in 1987–88 is followed, on his own slide, by the founding of CPLEX Optimization. From then on the pattern is stable. A hard instance from a partner or customer (the AA crew model, LAU2, Saigal's degenerate max-cut LPs) exposes a failure. He or the team fixes it in the production code. Then he **measures the gain across versions on large real test sets** and publishes the history (OR 2002, Documenta 2012, the 2012/2017/2022 decks). His grants show the move from LP toward **MIP** early: LP tools *for integer programming* (1989) and a MIP research code (1994). But by his own account the MIP code that made CPLEX 6.5's 1998 jump was written by Gu and Rothberg. After the 1997 sale to ILOG he moved from developer to manager and strategist. He **left ILOG in 2008 because MIP was not strategic there**, and joined Gu and Rothberg's new venture (Gurobi) as CEO with no development role. After 2015 he was strategist, chairman, teacher in Erlangen and narrator of computational progress. In April 2020 Gurobi labelled him co-founder and advisor. His last paper is the 2020 presolve paper. His last dated lecture found is of 12 Sep 2022. The latest dated trace of his own is a long interview published on 6 Dec 2023. In it he describes himself as retired, though not completely, still voicing opinions on Gurobi's management and direction, with his research days over. **In the last 12 months no paper, talk, code or role statement under his name was found.**

---

## 1. Dated timeline

| Date | Event | Tag | Source |
|---|---|---|---|
| 1968 | BS, UC Berkeley. Rice's profile names the subject Industrial Engineering. Other bios (2013, 2015, the undated Berkeley page) say Industrial Engineering and Operations Research | [observed] P | O1; O2; O9; O12 |
| 1971 | MS in OR, Cornell; mathematics instructor at Cornell | [observed] P | O1 |
| 1972 | PhD in OR, Cornell. Dissertation *Composition and Decomposition of Matroids and Related Topics* (MGP misspells "Decompostion"). Advisor Louis Joseph Billera (PhD CUNY 1968, under Moses Richardson and Michel Balinski) | [observed] S | S4 (MGP 14993, 26980); O1 |
| 1973–1977 | Assistant professor of mathematics at Kentucky; visiting assistant professor at UW–Madison in 1974; tenured associate professor at Kentucky in 1976 | [observed] P | O1 |
| Apr 1974 | First paper in DBLP: *ℓ-matrices and a characterization of binary matroids*, Discrete Math. 8(2):139–145, DOI 10.1016/0012-365x(74)90060-0 | [practice] P | S1; S3 |
| Jul 1976–Dec 1978 | NSF award 7607640, *Applications of Matroids*: Kentucky, Algebra/Number Theory/Combinatorics program, $12,000 | [practice] P | P14 |
| 1977 | Visiting associate professor at Cornell, then moves to Northwestern. The department is inferred: OR 2002 says Northwestern's Dept. of Industrial Engineering and Management Sciences hired Fourer, and the interview says Bixby hired him | [observed] P; [inferred] | O1; P4 p. 3; P1 p. 2 |
| Jul 1978–Nov 1983 | NSF 7802270 and 8104881, *Combinatorial Investigations in Mathematical Programming*: Northwestern, Theoretical Computer Science program, $55,000 and $73,788 | [practice] P | P14 |
| Apr 1979 | *On Reid's characterization of the ternary matroids*, JCTB 26(2):174–204, DOI 10.1016/0095-8956(79)90056-x. Waterloo's 2013 citation picks this out as a highlight | [practice] P; [observed] P | S3; O2 |
| Aug 1980 | With W. H. Cunningham: *Converting Linear Programs to Network Problems*, MOR 5(3):321–357, DOI 10.1287/moor.5.3.321. By his account, Tom Baker (then at Exxon) heard him talk on it at a meeting at SUNY Binghamton, which led to Exxon consulting on network optimization | [practice] P; [stated] P | S3; P1 p. 1 |
| 1981 | *Hidden Structure in Linear Programs*, in *Computer-Assisted Analysis and Model Simplification* (Academic Press), pp. 327–360, DOI 10.1016/b978-0-12-299680-1.50024-0 (not read) | [practice] P | S3 |
| Early 1980s | Teaching at Northwestern when IBM PCs appeared. Rather than pay for an academic LINDO licence, he wrote his own classroom code, in Fortran, initially a tableau code. He wrote a network simplex for Baker's new firm, Chesapeake Decision Sciences (MIMI). By his account it was about 60 times faster than Baker's own and was later embedded in Aspen products. He paid David Applegate to improve its data structures | [stated] P | P1 pp. 1–2; P4 p. 3 |
| 1982–Sep 1983 | AFOSR grant AFOSR-82-0004. Its final summary report is titled *Hidden and Embedded Structure in Linear Programs* (DTIC, 30 Sep 1983, DOI 10.21236/ada137773). The listed contents include graph-realization algorithms with an application to LP (abstract only) | [practice] P | P15 |
| 1983 | Joins Rice as professor of computational and applied mathematics (Rice profile; contradicts both interviews, see Contradictions). His 2022 slide dates the start of the classroom LP code to 1983. In 2023 he dated his return to programming to the arrival of IBM PCs in 1983, after hating punch-card programming as a Berkeley undergraduate (caption text) | [observed] P; [stated] P | O1; P8 slide 10; P1 p. 2; P20 |
| 1984 | *Recent Algorithms for Two Versions of Graph Realization and Remarks on Applications to Linear Programming*, *Progress in Combinatorial Optimization*, pp. 39–67, DOI 10.1016/b978-0-12-566780-7.50009-x (not read) | [practice] P | S3 |
| Jun 1985–Nov 1987 | NSF 8416187, *Efficient Detection and Solution of Partial-Network Linear Programs (Computer Research)*: Rice, Software Engineering program, $73,317. In parallel, NSF 8519204, *Connectivity in Matroids* (May 1986–Oct 1987, $12,691) | [practice] P | P14 |
| 1985–1987 | Baker invites him to supply the LP code for MIMI. The code is converted to C (Baker's condition). About two years follow of failing customer LPs, which were snapshots from sequential LP and badly conditioned. He fixes failures one at a time, at home, as a hobby, without reading the literature. In 2023 he added detail, as caption text: Baker had earlier had him and Fourer consult for a summer at Exxon; a computer-science student converted the Fortran code to C, which is how he learned C; and he dated the request to about 1984, when he was already at Rice | [stated] P | P8 slide 10; P1 pp. 2–3; P4 p. 3; P20 |
| Aug 1986 → Mar 1988 | Bixby and Robert Fourer: report *Finding Embedded Network Rows in Linear Programs I: Extraction Heuristics* (DTIC, DOI 10.21236/ada455195), published in Management Science 34(3):342–376, DOI 10.1287/mnsc.34.3.342. Earliest LP-computation paper found. No Part II was found in DBLP or OpenAlex | [practice] P | S1; S3; S2 |
| 1986 | First public results of his code. The handwritten sheet labels the code column LOPT: 13 netlib LPs against XMP on a Sun 3/50. My transcription: LOPT faster on 12 of 13; ratio XMP/LOPT time from 0.55 (STANDAT) to 4.2 (BANDM), geometric mean ≈ 1.8 | [practice] P (image); [inferred] (arithmetic) | P8 slide 12 (PDF p. 11) |
| ~1986–1987 | A Chesapeake customer wants the code: Amoco around 1986 (2015 interview), 1987 (2021 talk, caption text; 2022 slide). He then made his first comparisons with other codes (XMP). He states that this comparison, together with integer programming, turned LP computation into a serious part of his research | [stated] P | P1 p. 3; P23; P8 slide 10; P4 p. 3 |
| Mar 1987 | Bixby and D. K. Wagner, *A note on detecting simple redundancies in linear systems*, ORL 6(1):15–17, DOI 10.1016/0167-6377(87)90004-6 | [practice] P | S3 |
| 1987–1988 | His 2022 slide reports a complete failure to obtain research funding for LP computation in these years. In 2021 he said friends called the idea crazy because LP was done, and that the lack of funding is why he started a company (caption text). In 2023 he recalled a senior colleague asking why he was spending time on something with no visible future, which he ignored because he had tenure. The automatic captions garble the colleague's name, so it is not given here (caption text) | [stated] P | P8 slide 10; P23; P20 |
| 1987 / 1988 | CPLEX Optimization: incorporated in 1987 (2015 interview; 1987 also, with hesitation, in 2023). Founded in 1988 (2020 Gurobi clip; 2021 talk; 2022 slide; Rothberg's INFORMS story). He recruited Janet Lowe from his Rice business-school class, and her husband Todd Lowe, and gave them 49%. In 2023 he said he and Janet founded it, that Todd joined soon after and became CEO, and that Janet named the code CPLEX, replacing his name for it, LOPT (caption text) | [stated] P; [observed] P | P1 p. 3; P20; P21; P23; P8 slide 10; O4 |
| 1987 (late) | A Sun 3/50 is the machine on his desk; it is the baseline of OR 2002's machine-speedup tables | [stated] P | P4 p. 5 |
| 1988 | CPLEX 1.0 released; he was responsible for all development | [stated] P | P4 p. 4; P1 p. 3 |
| Feb 1989–Jan 1993 | NSF CCR-8815914, *Linear Programming Tools for Integer Programming*: Rice, $161,739. The plan: reoptimization data structures for sequences of related LPs, large-scale degeneracy in combinatorial applications, and C sparse LU and update routines in LOPT, a simplex code the abstract says he developed. It names a collaboration with Grötschel (Augsburg) and a parallel max-cut project with Barahona (Waterloo) | [stated] P | P12 |
| 1989 | American Airlines crew-scheduling challenge (837 rows, about 12.75 M columns). Team: Bixby, Lustig, Marsten, Shanno, Gregory. Methods: sifting (an idea he credits to John Forrest), barrier steps then primal steps on a Cray Y-MP, and a fast crossover based on a Megiddo result. Published as OR 40(5):885–897, Oct 1992, DOI 10.1287/opre.40.5.885 (report May 1991, DOI 10.21236/ada452700) | [stated] P; [practice] P | P8 slides 15–16; S3 |
| 1989–1994 | Editor-in-Chief of *Mathematical Programming* Series A (event bios only, not verified) | [observed] P | O9; O10 |
| Oct 1989 | DTIC report *Linear Programming Tools for Integer Programming*, DOI 10.21236/ada219013 (not read) | [practice] P | S3 |
| ~1989 (his estimate, possibly off by a year) | CPLEX starts building a MIP solver because Todd Lowe, in sales, saw that customers asked for it. By his 2023 account the developer primarily responsible was Mary Fenelon, with his assistance, and most MIP progress in that period came from the LP code, above all the maturing dual simplex (caption text) | [stated] P | P20 |
| ~1990 | He organizes a TSP meeting at Rice (TSP 90). By his 2023 account, Applegate, Chvátal and Cook came together as a group around then. Cook later proposed what became strong branching, and he implemented it in CPLEX because he had the source code (caption text) | [stated] P | P20; P1 p. 4 |
| ~1990–91 | CPLEX callable library. He attributes the idea to Grötschel's early-1990s IP work and to complaints about MPSX in TSP work | [stated] P | P1 p. 3; P4 p. 4 |
| 1991 | CPLEX MIP first released; CPLEX 1.2 was the first version with MIP | [stated] P | P5 p. 116 |
| 1991 | PhD students Sanjay Saigal (max-cut) and Zhijun Wu (co-advised with J. E. Dennis Jr.) graduate at Rice | [observed] S | S4 |
| ~1992 | CPLEX catches IBM's OSL in LP (his estimate) | [stated] P | P1 p. 3 |
| Apr 1992 | ZIB visit. SC 92-11 (front door dates it 24 Apr 1992) is the German version of the initial-basis paper: Rice affiliation, written while visiting ZIB, translated with help from Robert Weismantel. It says the main parts of the CPLEX simplex were written by the author. It announces a series covering Wolfe's composite Phase I, a cheap partial pricing, a bound-perturbation method against stalling, vectorization and more. Tests ran on a 40-MHz SPARCstation 2. Grants acknowledged: NSF CCR-8815914 and AFOSR-90-0273 | [stated] P; [practice] P | P6 pp. 1–2, 19, 21; S11 |
| Aug 1992 | English version, ORSA J. Comput. 4(3):267–284, DOI 10.1287/ijoc.4.3.267 (report Sep 1991, DOI 10.21236/ada453079) | [practice] P | S3 |
| 1992 | Bixby, Boyd, Indovina, *A Test Set of Real-World Mixed Integer Programming Problems* (MIPLIB; DTIC, DOI 10.21236/ada455431, not read). Oct 1992: DTIC report *Linear-Programming Tools in Integer Programming: The Traveling Salesman*, DOI 10.21236/ada261398 (not read), the earliest TSP-linked item in his record | [practice] P | S3 |
| Late 1980s–1994 | LAU2, a United Airlines fleet model passed on by John Gregory (Cray). CPLEX 1.x sat stuck in Phase I for 7 hours on a Cray. The fix went step by step: degeneracy handling, then the explicit dual, then a dual simplex, then dual steepest edge (after Forrest's primal Devex success), then Goldfarb's simpler variant. On CPLEX 3.0: dual steepest edge 273 s against 27,765 s for primal | [stated] P | P8 slides 22–24; P1 p. 3 |
| 1994 | By his account the dual simplex reached maturity in CPLEX (CPLEX 3.0 about 5.5× faster than 2.1). At an Oberwolfach meeting around 1993/94 he urged dual steepest edge on airline researchers | [stated] P | P1 p. 3; P5 p. 117 |
| Feb 1994 | *Commentary—Progress in Linear Programming*, ORSA J. Comput. 6(1):15–22, DOI 10.1287/ijoc.6.1.15. The abstract argues that Lustig–Marsten–Shanno overstated barrier against simplex | [stated] P | P16 |
| May 1994 | Bixby and Saltzman, *Recovering an optimal LP basis from an interior point solution*, ORL 15(4):169–178, DOI 10.1016/0167-6377(94)90074-4 (not read) | [practice] P | S3 |
| 1994 | Rice parallel-computing context: *Numerical Optimization at the Center for Research on Parallel Computation* (14 authors), Int. J. Supercomputer Appl. 8(2):143–153, DOI 10.1177/109434209400800206. Bixby, Kennedy, Kremer, *Automatic Data Layout Using 0-1 Integer Programming*, IFIP PACT 1994, pp. 111–122 (DBLP; no DOI) | [practice] P | S1; S3 |
| Dec 1994–Nov 1997 | NSF CCR-9407142, *Mathematical Sciences: Investigations in Mixed Integer Programming*: Rice, $140,000. The plan was a research code joining standard practice with recent theory, aimed at real MIPs that current codes could not solve | [stated] P | P13 |
| Dec 1995 | Bixby and Alexander Martin, ZIB SC-95-45, *Parallelizing the Dual Simplex Method*. Bixby's affiliation is Rice and CPLEX Optimization Inc.; Martin's is ZIB. Three implementations derived from the CPLEX dual (PVM, System V shared memory, SGI PowerC) were run on workstation clusters, a Sun S20-502, SGI multiprocessors and an IBM SP2. Supported by NSF CCR-9407142 and Rice's CRPC. Published Feb 2000, INFORMS J. Comput. 12(1):45–56, DOI 10.1287/ijoc.12.1.45.11902, with the byline Rice and ILOG CPLEX Division | [practice] P; [stated-joint] P | P7 pp. 1, 20; P18 |
| Early–mid 1990s | SGI–CPLEX parallel barrier, by Rothberg. AA–US Air merger due diligence turned it from nice-to-have into must-have, at 5 minutes against 3–4 hours for OSL | [stated] P | P8 slides 20–21; P1 p. 3 |
| 1996 | Bixby, Dennis, Wu, *Solving Nonlinear Integer Programs with a Subgradient Approach on Parallel Computers*, SIAM proceedings chapter, DOI 10.1137/1.9780898719659.ch25 | [practice] P | S1 |
| 1997 | ILOG buys CPLEX Optimization. The idea was Todd and Janet Lowe's: an IPO-like exit, and Todd did not want to run a larger, international firm. He says he was still developing and still an academic then. Elected to the NAE the same year | [stated] P; [observed] P | P1 p. 4; O2; O13 |
| 1997–2008 | CPLEX R&D leadership: Rothberg joins the team in 1997 and leads CPLEX R&D 1998–2005; Gu joins in 1998 and leads 2005–2008 | [observed] P | O4 |
| 1998 / 2000 | Gives up his tenured position at Rice in 1998; the university counts him as retired from 2000. This was confirmed by him in 2023 to the interviewer's question. His stated reason: his turn to chair the department had come, while CPLEX was going well, and he would not keep tenure as security while his main work was elsewhere (caption text). Rice affiliations still appear on later bylines (2002–2008) | [stated] P; [practice] P | P20; P19 |
| 1998 | CPLEX 6.5 gives a MIP speed-up above 10×. He credits Gu (cuts, most of presolve) and Rothberg (node presolve, probing, bound strengthening, heuristics). His own part was small: strong branching, which came out of a TSP discussion with Cook, and tuning the library for the TSP code | [stated] P | P5 p. 117; P1 p. 4 |
| Jun 1998 | Bixby, Ceria, McZeal, Savelsbergh, *An Updated Mixed Integer Programming Library: MIPLIB 3.0*, Optima 58, pp. 12–15. The article plans yearly updates. The same issue has a notice signed by him as chair of the MPS Publications Committee | [practice] P; [stated-joint] P | P11 pp. 2, 12 |
| Jun 1998 | Co-editor of IPCO VI (Houston), LNCS 1412, DOI 10.1007/3-540-69346-7 | [practice] P | S1; S3 |
| 1998 | Applegate, Bixby, Chvátal, Cook, *On the solution of traveling salesman problems*, ICM 1998 (Doc. Math. Extra Vol. III, 645–656), DOI 10.4171/dms/1-3/62 | [practice] P | S3 |
| 1998–1999 | With his student Eva K. Lee: *Solving a Truck Dispatching Scheduling Problem Using Branch-and-Cut*, OR 46(3):355–367, DOI 10.1287/opre.46.3.355. Bixby, Cook, Cox, Lee, *Computational experience with parallel mixed integer programming in a distributed environment*, Annals OR 90:19–43, DOI 10.1023/a:1018960631213 | [practice] P | S3 |
| 2000 | Beale–Orchard-Hays Prize, with Applegate, Chvátal and Cook | [observed] P | O8 |
| 2000 | Bixby, Fenelon, Gu, Rothberg, Wunderling, *MIP: Theory and Practice — Closing the Gap*, IFIP AICT, pp. 19–49, DOI 10.1007/978-0-387-35514-6_2. Byline: Rice CAAM and ILOG CPLEX Division | [practice] P | P19; S3 |
| 2001–2004 | Chairman of the Mathematical Programming Society (event bios only, not verified) | [observed] P | O9; O10 |
| Feb 2002 | OR 50(1):3–15, DOI 10.1287/opre.50.1.3.17780, byline ILOG and Rice. Measures LP progress on a 680-model test set. Credits Gu, Lustig, Rothberg and Wunderling with fundamental contributions to the CPLEX LP algorithms. INFORMS Fellow, class of 2002 | [stated] P; [observed] P | P4 pp. 3–15; O5 |
| 13 Nov–Dec 2002 | Re-runs CPLEX 1.0 (1988) on a production-planning LP (401,640 × 1,584,000) on a 2.0 GHz Pentium 4. The run started in Houston on 13 Nov 2002, was checked from Berlin, Dagstuhl, Amsterdam and Houston, and took 29.8 days, against 1.5 h for CPLEX 5.0 and 59.1 s for CPLEX 9.0 | [practice] P | P9 slides 9–14; P8 slides 26–29 |
| Jul 2003 | Applegate, Bixby, Chvátal, Cook, *Implementing the Dantzig-Fulkerson-Johnson algorithm for large traveling salesman problems*, Math. Program. 97(1–2):91–153, DOI 10.1007/s10107-003-0440-4 (byline Rice CAAM) | [practice] P | S3; P19 |
| 2004 | Updates his LP progress figures; the venue was not found. INFORMS Impact Prize, team listed as Bixby, Janet Lowe and Paul Green. Co-organizes the Oberwolfach workshop *Mathematics in the Supply Chain* (Oberwolfach Reports 1(2):963–1036, DOI 10.4171/owr/2004/19). *Mixed-Integer Programming: A Progress Report*, The Sharpest Cut, ch. 18, DOI 10.1137/1.9780898718805.ch18 (byline ILOG and Rice) | [stated] P; [observed] P; [practice] P | P5 p. 113; O7; S3; P17 |
| Jun 2006 | Bixby, Burda, Miller, semiconductor scheduling with MIP and CP, ASMC 2006, DOI 10.1109/asmc.2006.1638740. Byline: CSO, ILOG | [practice] P | P19; S3 |
| 2006 (print year per Wikipedia, S7; OpenAlex dates one record 2007; the ebook DOI is dated 2011) | *The Traveling Salesman Problem: A Computational Study* (Applegate, Bixby, Chvátal, Cook; Princeton UP; ebook DOI 10.1515/9781400841103). Chapters 12 (*Managing the Linear Programming Problems*, DOI 10.1515/9781400841103.345) and 13 (*The Linear Programming Solver*, DOI 10.1515/9781400841103.373); chapters not read | [practice] P | S3 |
| Jan 2007 | Bixby and Rothberg, *Progress in computational mixed integer programming—A look back from the other side of the tipping point*, Annals OR 149(1):37–41, DOI 10.1007/s10479-006-0091-y (byline ILOG, Mountain View; not read). Lanchester Prize 2007, with Applegate, Chvátal and Cook | [practice] P; [observed] P | S3; P19; O6 |
| 16 Nov 2007 | Seminar at Korea University Business School, described as ILOG's Chief Science Officer | [observed] S | S5 |
| Late 2007 | A massive test of 12 CPLEX releases (1.2 to 11.0), recompiled for a bank of identical machines, with a 30,000 s limit. Documenta gives 1,892 models; the 2017 deck gives 1,852 | [practice] P; [stated] P | P5 p. 116; P9 slide 30 |
| 2008 | Leaves ILOG before IBM's acquisition of ILOG. His stated reason: MIP was never strategic for ILOG. In 2015 he said Gu and Rothberg had started working together within 3–4 weeks of leaving and that he contacted them and asked to help. In 2023 he said they had planned the new company and that he left independently around the same time; he added that ILOG's revenue had come to be dominated by business rules, giving his own estimate (caption text). Gurobi was founded in 2008. Papers that year: WSC 2008, DOI 10.1109/wsc.2008.4736331 (byline ILOG), and ORL 37(1):11–15, DOI 10.1016/j.orl.2008.09.006, the 85,900-city certification (byline Rice Graduate School of Management) | [stated] P; [observed] P; [practice] P | P1 p. 4; O4; P19 |
| May 2009 | Gurobi 1.0 released, roughly equivalent to CPLEX 11.0 on Mittelmann's public benchmarks | [stated] P | P10 slide 8; P5 pp. 117–118 |
| 2008–2015 | Gurobi CEO. By his account: no development, much testing, pressing the developers about bad behaviour, running the business | [observed] P; [stated] P | O10; P1 pp. 4–5 |
| ~2010/11–2021 | Teaches a concentrated month-long class in Erlangen each year, arranged by Alexander Martin. Billed as visiting professor in 2015, 2017 and 2021 | [stated] P; [observed] P | P1 p. 6; O9; O11; O10 |
| Jun 2011 | Co-author (16 authors), *MIPLIB 2010*, Math. Program. Comput. 3(2):103–163, DOI 10.1007/s12532-011-0025-9 (byline Gurobi, Houston) | [practice] P | S3; P19 |
| Q4 2011–Q3 2012 | Classifies Gurobi customers' application areas over one year: about 40 areas, supply chain first and electrical power second | [stated] P | P1 p. 5; P9 slide 19 |
| 12 Jun 2012 | Fields Institute talk *1000X MIP Tricks* (Bill Cunningham's 65th): opens with a matroid reminiscence, then gives Gurobi 1.0→5.0 = 16.2× and CPLEX 1991–2007 = 29,530× | [stated] P | P10 |
| 2012 | *A Brief History of Linear and Mixed-Integer Programming Computation*, Documenta Math. Extra Vol. ISMP, 107–121, DOI 10.4171/dms/6/16 | [stated] P | P5 |
| 14 Jun 2013 | Honorary DMath, Waterloo. The citation describes his early matroid work and a shift to linear optimization in the 1980s, and lists him as research professor of management (Jones School) and president of Gurobi | [observed] P | O2; O3 |
| 13 May 2015 | Imperial College seminar *Computational Progress in Linear and Mixed Integer Programming*; bio still says CEO | [observed] P | O9 |
| 2015 | Three-part lecture *Solving Linear Programs: The Dual Simplex Algorithm* at the CO@Work 2015 summer school, Zuse Institute Berlin. The videos were uploaded 6 Oct 2016, and their description calls him co-founder and former CEO of Gurobi. The school's exact dates were not verified | [practice] P; [observed] P | P22 |
| May–Oct 2015 | Moves from CEO to Chief Strategy Officer and stays Chairman. The window is bounded by the May 2015 bio and the October 2015 interview. A Gurobi release on the change was seen only as an undated search snippet, so team.json's 3 Sep 2015 was not re-verified | [inferred] from P/O | O9; P1 p. 6; S6 |
| Oct 2015 | Oberwolfach interview, published Sep 2016. He is Chairman and CSO, about half time, managing the sales team and running the code. He holds an emeritus title but no longer goes to the department. He says he does no research, except a paper on presolve in Gurobi | [stated] P | P1 p. 6 |
| 5 May 2017 | ECCO 2017 invited lecture: Gurobi 1.0→7.0 = 43.2×, and a machine-independent MIP gain above 1.3 million× since 1991 | [stated] P | P9; O11 |
| Nov 2019 / Apr 2020 | Last paper: Achterberg, Bixby, Gu, Rothberg, Weninger, *Presolve Reductions in Mixed Integer Programming*, INFORMS J. Comput. 32(2):473–506, DOI 10.1287/ijoc.2018.0857 (byline Gurobi, Beaverton) | [practice] P | S1; S3; P19 |
| 8 Apr 2020 | Gurobi's YouTube video *How was Gurobi founded?* (200 s). Its description calls him co-founder and advisor. In it he dates CPLEX Optimization to 1988, says he stayed about ten years with ILOG, and gives as his main reason for leaving that CPLEX would never be strategic for ILOG (caption text) | [observed] P; [stated] P | P21 |
| 19 Mar 2021 | University of Toronto MIE Distinguished Seminar (online), *Optimization: Past, Present, Future*. Bio: CEO 2008–2015, now on the Gurobi board. Video uploaded 22 Mar 2021; read here as a caption transcript | [observed] P; [stated] P | O10; P23 |
| 12 Sep 2022 | Hausdorff School (Bonn) lecture *Linear Programming: A Historical View*: deck dated Sept 2022, PDF created 13 Sep 2022. Latest dated lecture found | [stated] P | P8; O15 |
| 6 Dec 2023 (published; recording date not stated) | Long interview *Subject to: Robert Bixby* (YouTube channel Subject to, 8,024 s). Its description reuses the 2021 Toronto bio. By the transcriber's reading of internal references it was recorded in 2023. In it he says he is retired but not completely; that he expects to keep voicing opinions on how Gurobi is managed and where it goes for a few more years; that he might write a paper on the LP story; and that his research days are over (caption text). **Latest dated trace of his own found** | [stated] P | P20 |
| 2 Jan 2023 | Gurobi release: Rothberg appointed Chairman of the Board. Bixby is not mentioned and no previous chairman is named | [observed] P | O14 |
| 29 Sep 2024 | NAE induction programme lists him among the Anniversary Members of 25–29 years. This is a listing, not an activity | [observed] P | O13 |
| 2025-11-05 → 2026-11-05 | No new paper, talk, code, interview or role statement found | — | §8 |

---

## 2. Lineage

| Relation | Person | Evidence | Tag |
|---|---|---|---|
| PhD advisor | **Louis Joseph Billera** (Cornell; PhD CUNY 1968, under Moses Richardson and Michel L. Balinski) | MGP 14993 and 26980. OpenAlex lists five Billera–Bixby papers, 1973–1976, all in alphabetical author order, so author position carries no seniority signal | [observed] S |
| PhD students, Northwestern (theory era) | **Donald K. Wagner** 1983, *An Almost Linear-Time Graph Realization Algorithm*; **Collette R. Coullard** 1985, *Minors of 3-Connected Matroids and Adjoints of Binary Matroids*; **Arvind Rajan** 1986, *Algorithmic Applications of Connectivity and Related Topics in Matroid Theory* | MGP student pages. Co-authored papers: Bixby–Wagner, MOR 13(1):99–123, 1988, DOI 10.1287/moor.13.1.99, and ORL 1987; Bixby–Coullard 1986–1988, e.g. Combinatorica 7(3), 1987, DOI 10.1007/bf02579300 | [observed] S; [practice] P |
| PhD students, Rice (computation era) | **Sanjay Saigal** 1991, max-cut via the cut cone; **Zhijun Wu** 1991, parallel subgradient for nonlinear IP (advisor 1 J. E. Dennis Jr.); **Eva K. Lee** 1993, structured 0/1 IPs from truck dispatching; **Shireen S. Dadmehr** 1995, *An Efficient Simplex-Based Method for Solving Large Linear Programs*; **Gwyneth Owens-Butera** 1997, limited-diversification portfolio selection (advisor 1 Dennis); **Cassandra M. McZeal** 1999, reoptimization in interior-point methods for IP (advisor 2 Yin Zhang) | MGP. Co-authored papers: Bixby–Lee (OR 1998; Annals OR 1999), Bixby–Dennis–Wu (1996), and McZeal on MIPLIB 3.0 (1998). MGP counts 9 students and 38 descendants | [observed] S; [practice] P |
| Student problem changes the production code | Saigal's degenerate max-cut LPs forced perturbation into CPLEX, by Bixby's account | P1 p. 3 | [stated] P |
| Formative colleague | **Robert Fourer**, hired at Northwestern by Bixby. He passed on computational LP knowledge in conversation and co-wrote the 1986/88 embedded-network-rows paper | P4 p. 3; P1 p. 2; S3 | [stated] P; [practice] P |
| Industrial channel | **Tom Baker** (Exxon, then Chesapeake Decision Sciences, MIMI): commissioned the network and LP codes and supplied failing LPs for two years | P1 pp. 1–3; P4 p. 3; P8 slide 10 | [stated] P |
| Company co-founders and team | Janet and Todd Lowe (CPLEX, 1987/88); Irv Lustig (presolve), Ed Rothberg (parallel barrier, later MIP), Zonghao Gu (MIP cuts and presolve), Roland Wunderling, Mary Fenelon, John Gregory, Ed Klotz; Gurobi with Gu and Rothberg (2008) | P1 pp. 3–4; P4 p. 14; O4 | [stated] P; [observed] P |
| Long collaboration | David Applegate, Vašek Chvátal, Bill Cook (TSP/Concorde; roles not divided). Alexander Martin (ZIB 1995 paper; later arranged his Erlangen teaching). Martin Grötschel (named in the 1989 NSF plan) | P4 p. 4; P7; P1 p. 6; P12 | [stated] P; [practice] P |

**Supervision turn ([inferred] from MGP titles).** All three Northwestern dissertations (1983–86) are matroid or graph-realization theory. All six Rice dissertations (1991–99) are computational LP or IP. The supervision record turns with his research about 5–8 years after the first LP-structure work (1980–81), and three of the Rice students were co-advised (Dennis, Zhang), which embeds him in Rice CAAM's computational culture.

---

## 3. Turns and what triggered them

### T1. Matroid theory → hidden network structure in LPs (1980 → 1987)
- [practice] The 1980 Bixby–Cunningham MOR paper converts LPs to network problems by matroid methods (graphicness testing). It is followed by *Hidden Structure in Linear Programs* (1981), the AFOSR summary report *Hidden and Embedded Structure in Linear Programs* (1983), the 1984 graph-realization chapter with remarks on LP, NSF 8416187 on partial-network LPs (1985–87, Software Engineering program) and Bixby–Fourer on embedded network rows (1986/88).
- **Trigger** ([inferred] from [practice] and [stated]): a technical bridge rather than a break. Graph realization and binary-matroid recognition gave an algorithm for finding network structure inside LPs. The funded framing moved with it: NSF programmes went from algebra/combinatorics (1976) to theoretical CS (1978–83) to software engineering (1985). The talk on the 1980 result produced the Exxon and Baker contact (P1 p. 1).
- Matroid work continued in parallel until 1988 (NSF 8519204, 1986–87; Coullard papers to 1988). The turn was gradual, not a switch.

### T2. PC classroom code → industrial code (early 1980s → 1987)
- [stated] Triggers: a new tool (the IBM PC), a teaching need (LP in his classes), cost avoidance (he would not pay for the academic LINDO licence) (P1 p. 1; P4 p. 3; P8 slide 10). Then a customer channel: Chesapeake wanted a network code and then a small LP code, because XMP was too big for MIMI (P1 p. 2).
- [stated] Method in this phase: fix each failing customer LP as it comes, without reading the literature. The failures were badly conditioned SLP snapshots (P1 pp. 2–3; P4 p. 3).

### T3. Hobby → research programme → company (1986 → 1988)
- [stated] Triggers, in his order. External validation came first: a Chesapeake customer wanted the code. The first benchmark against XMP followed, and he names this comparison as what made LP computation part of his research (P4 p. 3). Integer programming was the equal second reason: researchers needed an embeddable, robust LP (P4 pp. 3–4). His 2022 slide places the founding of CPLEX Optimization directly after a 1987–88 failure to get research funding for LP computation (P8 slide 10).
- [stated] Organisational move: six months of failing to sell it alone. He then recruited his two best business-school modelling students and gave them 49% (P1 p. 3).
- [inferred] The funding failure has a time edge. NSF did fund LP-structure work in 1985–87 (8416187) and LP tools *for integer programming* from Feb 1989 (8815914). The 1989 success came under an IP framing.
- [stated, caption text] The same story recurs in later retellings. In 2021, friends told him LP was done and funding failed, so he started a company (P23). In 2023, a senior colleague questioned the move and he ignored the advice, secure in tenure. He also says Janet Lowe named the product (P20).

### T4. Production LP engineering driven by hard instances (1988 → 1994)
- [stated] Each named advance has a named instance behind it:
  - the AA crew model (1989), behind sifting, barrier then primal, and fast crossover (P8 slides 15–16);
  - LAU2, behind degeneracy handling, the dual, and dual steepest edge (P8 slides 22–24; P1 p. 3);
  - Saigal's max-cut LPs, behind perturbation and, by his account, bound shifting (P1 pp. 3–4).
- Competitive and academic pressure: OSL was better until about 1992 (P1 p. 3). The callable library (about 1990–91) answered IP researchers' needs (P1 p. 3; P4 p. 4).
- Resource triggers: NSF 1989; ZIB visit 1992 (P6 p. 1); Cray machines through partners (P4 p. 5; P8).

### T5. Parallel computing at Rice (1994 → 1999), then exit
- [practice] CRPC paper (1994), data layout by 0-1 IP (1994), parallel subgradient (1996), parallel dual simplex (Dec 1995 / 2000), parallel MIP in a distributed environment (1999). The SGI partnership produced Rothberg's parallel barrier (P1 p. 3; P8 slides 20–21).
- **Trigger** [inferred]: an institutional context. Rice's Center for Research on Parallel Computation supported Martin's side of the 1995 work (P7 p. 1). The NSF MIP award came partly through HPCC-coded programmes (P13 records). Hardware vendors (SGI) wanted their machines sold (P1 p. 3).
- **Exit**: no parallel-simplex paper after the 2000 journal version. In 2012 he judged that parallelizing simplex had had essentially no success (P5 p. 114, paraphrased).

### T6. LP → MIP as diagnostician, test-set builder and measurer (1989 → 2007)
- [stated] He calls IP the dominant application of LP (P4 p. 4). His MIP grant (Dec 1994) diagnosed that general MIP solvers used few ideas from theory (P13). He describes 1998 (CPLEX 6.5) in the same terms: thirty years of theory finally implemented (P5 p. 117; P9 slide 32 label *Mined Theoretical Backlog: 1998*).
- [practice] MIPLIB 1992 and MIPLIB 3.0 (1998); parallel MIP (1999); co-authored progress reports in 2000, 2004 and 2007; the late-2007 version-by-version test (P5 p. 116).
- [stated] Early CPLEX MIP lagged MINTO (P1 p. 3). The 6.5 code was Gu's and Rothberg's (P1 p. 4).
- [stated, caption text, 2023] He dates the start of MIP development to about 1989. Todd Lowe pushed for it from sales, and Mary Fenelon was the primary developer, with his assistance. He credits most of the MIP gains of that period to the LP code (P20).
- **Trigger** [inferred]: IP research needed LP tools (the 1989 grant), MINTO showed that cutting planes worked, and a commercial-strategy push came from Todd Lowe, who saw that selling required a MIP (P1 p. 3).

### T7. TSP collaboration (by 1992 → 2009), context only
- [stated] He presents the TSP work as his IP research programme grown into one of his most fruitful collaborations (P4 p. 4). He tuned the CPLEX library to work with the TSP code, and strong branching came out of it (P1 p. 4; P9 slide 29).
- [practice] DTIC report 1992; ICM 1998; MP 2003; book 2006; ORL 2008/2009. Joint with Applegate, Chvátal and Cook; **roles not divided.**
- [stated, caption text, 2023] By his account the group formed around 1990, near a meeting he organized at Rice (TSP 90). He implemented Cook's strong-branching idea in CPLEX because he had the source code (P20).

### T8. Developer → manager and strategist inside ILOG (1997 → 2008)
- [stated] The sale was the Lowes' idea, for an IPO-like exit and because Todd did not want to run a larger international firm. Bixby kept developing and stayed an academic (P1 p. 4).
- [observed] After 1997, Rothberg leads CPLEX R&D from 1998 to 2005 and Gu from 2005 to 2008 (O4). Bixby's ILOG titles, by source:
  - ILOG Board of Directors, CPLEX Development Team manager, President of the Technical Advisory Board, and General Manager of the Semiconductor Business Division (O12; O4 without the board);
  - "CSO, ILOG" (2006 byline, P19) and Chief Science Officer (2007 news, S5).
- [practice] His output shifts to measurement (OR 2002, Sharpest Cut 2004, Annals 2007) and to semiconductor and supply-chain applications (Oberwolfach 2004; ASMC 2006; WSC 2008).
- [stated, caption text, 2023] He gave up tenure at Rice in 1998 rather than take his turn as department chair while CPLEX grew, and was officially retired by Rice in 2000 (P20). [inferred] So the academic side of the trajectory ends about a year after the sale, even though Rice still appears on his bylines until 2008.
- [stated, caption text, 2023] On the sale: the stated reason was internationalization and Todd's reluctance to run an international firm; the real reason, in his view, was a hot stock market (P20).

### T9. ILOG → Gurobi (2008)
- [stated] Trigger: MIP was never a strategic product for ILOG, whose strategic thinking started from constraint programming (P1 p. 4). Gu and Rothberg started first; he asked to join (P1 p. 4). He gives the same reason in 2020 (P21, caption text). In 2023 he said he left independently around the same time, for reasons not identical to theirs (P20, caption text).
- [stated] He took a role with no development: testing, pressing the developers, running the business (P1 pp. 4–5). On the free academic licences he gave two reasons: brand-building against CPLEX, and spreading the technology to non-OR users (P1 p. 5).
- [stated] Measurement infrastructure was rebuilt fast. Within two days Gurobi had 600 models gathered from the web, with large contributions from NEOS. By 2015 the library held about 10,000 models, with a working test set of about 3,500 (P1 p. 6). His 2017 deck shows a library of 3,550 models (P9 slides 34–35).

### T10. CEO → CSO and chairman; out of research (2015 → 2022)
- [stated] Half time; sales team; runs the code; teaches mathematics in Erlangen. He found business-school teaching less satisfying (P1 p. 6). He no longer does research except the presolve paper (P1 p. 6), which appeared in 2019/2020.
- [practice] From 2012 his public output is retrospective progress talks: Fields 2012, Imperial 2015, ECCO 2017, Toronto 2021, Hausdorff 2022. He also gave an implementation lecture series at CO@Work 2015 (P22). The numbers are updated from deck to deck (see Contradictions).
- [observed] Role labels after 2015: co-founder and advisor (Gurobi video, Apr 2020, P21); on the Gurobi board (Toronto bio, Mar 2021, O10).
- [stated, caption text, Dec 2023] Retired but not completely; voicing opinions on Gurobi's management and direction; research days over; a paper on the LP story possible (P20). No such paper was found.

---

## 4. Entry and exit timing relative to the consensus ([inferred] unless tagged)

- **LP computation: entered against the consensus.** [stated] In 1992 he wrote that a decade earlier LP computation had been thought almost fully developed (P6 p. 1). In 2012 he wrote that mid-1980s PC results confirmed the belief that LP codes were mature (P5 p. 112). He entered in the mid-1980s as an outsider, without the literature (P4 p. 3), before the late-1980s and 1990s revival that he later documents.
- **Barrier against simplex: moved with the evidence, not ahead of it.**
  - 1989–92: an early hybrid with the barrier group (P8 slides 15–16; OR 1992).
  - 1994: publicly resisted claims of barrier dominance (P16).
  - 2002: barrier fastest overall by a narrow but growing margin on large models (P4 p. 13).
  - 2012: barrier increasingly wins from scratch, and crossover is the sequential bottleneck (P5 p. 114).
  - 2017 and 2022: he narrates the 1990s as barrier resetting the bar while simplex unexpectedly kept pace (P9 slide 7; P8 slide 13).
- **Dual simplex as a first-class algorithm: early, but shared.** CPLEX 3.0 (1994) and his Oberwolfach remark of about 1993/94 (P1 p. 3). The method was Forrest–Goldfarb's dual steepest edge, by his own texts (P4 p. 6; P5 p. 113), and OSL had dual steepest edge in the same period, by the interviewer's question (P1 p. 3).
- **Parallel simplex: entered 1995, left by 2000, and judged negatively in 2012 before others' later parallel dual simplex results.** For example: Huangfu & Hall, *Parallelizing the dual revised simplex method*, Math. Program. Comput., 2017/2018, DOI 10.1007/s12532-017-0130-5 (seen in an OpenAlex search). Whether those results answer his 2012 judgment is a question for agent 05, not settled here.
- **MIP: diagnosis before the consensus, implementation by others.** The theory-backlog diagnosis is in his 1994 grant (P13), four years before CPLEX 6.5 (1998). By his account most top MIP researchers would have said before 1998 that out-of-the-box solving was impossible (P5 p. 117). CPLEX itself was a follower of MINTO on cuts in the early 1990s (P1 p. 3; P5 p. 116).
- **Research exit**: stated in Oct 2015 (P1 p. 6). Last paper 2020 (S1). Last dated lecture Sep 2022 (P8).

---

## 5. Era and resource context of each practice

| Period | Compute and tools | Team and money | Seniority and role | Evidence |
|---|---|---|---|---|
| 1970–1985 matroid theory | Pen and paper | NSF $12k (1976–78), $55k (1978–81), $73.8k (1981–83); AFOSR-82-0004 | Assistant to tenured associate professor (Kentucky); Northwestern faculty; 3 PhD students | P14; P15; O1; S4 |
| Early 1980s classroom and network code | IBM PC; Fortran, then C | Alone; paid Applegate to improve the network code | Professor, hobby work | P1 pp. 1–2 |
| 1985–1988 LOPT → CPLEX 1.0 | Sun 3/50 (1986; late 1987); Chesapeake's failing LPs; netlib | Alone as developer; NSF $73.3k for partial-network LPs (1985–87); no LP-computation funding 1987–88 | Rice professor; company founder with two former students | P8 slides 10, 12; P4 pp. 3, 5; P14 |
| 1989–1994 production LP | Cray X-MP/Y-MP via partners; SPARCstation 2 (1992); HP9000/730 (CPLEX 3.0 tests) | NSF $161.7k (1989–93); AFOSR-90-0273; ZIB visit; Rice students | Professor and company technical head | P12; P6 pp. 2, 19; P8 slides 16, 24 |
| 1994–1999 parallel and MIP | PVM clusters, Sun S20-502, SGI multiprocessors, IBM SP2; SGI partnership | NSF $140k MIP (1994–97); Rice CRPC; CPLEX team growing (Lustig, Rothberg 1997, Gu 1998) | Professor and CPLEX lead, until the 1997 sale | P7; P13; P1 pp. 3–4; O4 |
| 1997–2008 ILOG | A 680-model LP set, the largest above 6 M rows (2002). A bank of identical machines; a 1,892/1,852-model MIP set from about 20 years of collected models (2007) | Corporate R&D led by Rothberg, then Gu | Manager, TAB president, CSO, GM of the semiconductor division; Rice and Jones School affiliations | P4 p. 6; P5 p. 116; O4; O12; P19 |
| 2008–2015 Gurobi CEO | Rebuilt library: 600 → about 10,000 models; test set about 3,500 | Start-up of three founders, growing to an international firm by about 2013 | CEO, no development | P1 pp. 4–6; O4 |
| 2015–2022 | Talks; customer survey; Erlangen teaching | — | CSO and chairman, half time (2015); board member (2021 bio) | P1 p. 6; O10 |

---

## 6. Failures, abandoned directions, revised assessments (dated)

1. **Mid-1980s, episodes when he judged his own code worthless** [stated]. Two years of a constantly breaking code. His first XMP test, on standata, was about 7× slower; two weeks of work brought it to about 2× (P1 p. 2).
2. **1987–88 funding failure** for LP computation [stated] (P8 slide 10).
3. **Early CPLEX MIP was weaker than MINTO** [stated] (P1 p. 3). **CPLEX 6.0 was an arguable non-improvement** over 5.0 in his 2007 MIP test [stated] (P5 p. 117).
4. **Losing the airlines to OSL** [stated]. A 40× faster barrier was nice-to-have, not must-have, until the merger due diligence (P8 slides 20–21; P1 p. 3).
5. **LAU2**: 7 hours stuck in Phase I. A partner advised giving up on simplex; the advice was overturned by dual steepest edge [stated] (P8 slides 22–24).
6. **Unwritten papers.**
   - The 1992 announced series on the CPLEX simplex (Phase I, partial pricing, bound perturbation, vectorization) was not continued as a series (P6 p. 2).
   - Bound shifting, which he names as perhaps his most important contribution, has no paper. He says he simply never got round to it (P1 p. 4).
   - OR 2002 deferred the simplex details to a forthcoming four-author TSP book (P4 p. 6), which has LP chapters 12–13 (S3). [practice + stated]
7. **Embedded network rows "I" without a Part II** [inferred from absence in DBLP and OpenAlex searches].
8. **Parallel dual simplex**: PVM gave acceptable speed-ups only for very large row/column ratios, and some results showed unexplained anomalies such as superlinear speed-ups. Only the thread-based version did well (P7 pp. 17, 20). By 2012 he judged parallel simplex essentially unsuccessful (P5 p. 114). The published 2000 version was not read. [stated-joint; stated]
9. **MIPLIB 3.0's planned yearly updates** (P11 p. 12) did not happen. The next editions were MIPLIB 2003 (Achterberg, Koch, Martin, ORL 34(4):361–372, 2006, DOI 10.1016/j.orl.2005.07.009) and MIPLIB 2010 (2011). [observed]
10. **ILOG**: MIP never became strategic, so he left [stated] (P1 p. 4).
11. **The LP-stagnation assessment was revised**:
    - 2012: no improvements in the standard LP algorithms since 2004, with LP threatening to become a bottleneck again (P5 p. 115).
    - 2017: still little progress since 2004, more research needed (P9 slide 16).
    - 2022: none 2004–~2015, then about 3× on large models in the last 7 years (P8 slide 30).
    - [stated, across time]
12. **Business-school teaching was dropped** in favour of teaching mathematics in Erlangen [stated] (P1 p. 6).
- **Not found**: retractions, published errata, rejected submissions.

---

## 7. Authorship and role labels by period (what the record lets the skill say)

- **1983–1988, sole developer.** He wrote the classroom code (LOPT, named in the 1986 sheet and the 1989 NSF abstract) and CPLEX 1.0, and was responsible for all development at the 1988 release [stated] (P1 p. 3; P12; P8 slide 12). Rothberg's INFORMS story says he developed the initial versions himself [observed] (O4). Applegate improved the earlier network code's data structures, paid by Bixby [stated] (P1 p. 2).
- **April 1992.** He wrote the main parts of the CPLEX simplex [stated] (P6 p. 2, German).
- **1997.** He was still doing development [stated] (P1 p. 4).
- **Not his, by his own texts.**
  - Dual steepest edge is the Forrest–Goldfarb method, which CPLEX implemented (P4 p. 6; P5 p. 113). The 2022 slide credits Forrest's primal Devex success and a simpler steepest-edge variant suggested by Goldfarb (P8 slide 23).
  - Sifting was Forrest's idea (P8 slide 15).
  - Presolve came with Lustig, and the parallel barrier was Rothberg's (P1 p. 3).
  - OR 2002 credits Gu, Lustig, Rothberg and Wunderling with fundamental contributions to the CPLEX LP algorithms (P4 p. 14).
  - CPLEX R&D was led by Rothberg (1998–2005) and Gu (2005–2008) [observed] (O4).
  - **Later CPLEX LP changes (5.0 to 7.1 and after) are not shown to be his.**
- **MIP in CPLEX.** He calls his own MIP role small: strong branching, which came out of TSP discussions with Cook, and tuning the library for the TSP code. The cuts and most of presolve were Gu's; node presolve, probing, bound strengthening and heuristics were Rothberg's (P1 p. 4). For the early CPLEX MIP (from about 1989) his 2023 account names Mary Fenelon as the primary developer, with his assistance. An outside contractor supplied a first version; the sibling transcriber redacted the name (P20, caption text). He implemented strong branching himself (P20; P1 p. 4). His MIP practice is grants, test sets (MIPLIB 1992, 3.0, 2010), a parallel MIP research code (1999) and progress measurement [practice].
- **Gurobi, 2008 onward: no development.** The one verbatim quote in this note, in answer to whether he did development at Gurobi: "No. Absolutely zero development." (Optima 101, p. 4). He tested and ran the business (P1 pp. 4–5). In the Fields 2012 deck, the MIP tricks are presented in the first person plural, the Gurobi team's voice (P10 slides 19, 33). **A progress number measured on CPLEX or Gurobi is not evidence that he wrote the code that produced it.**
- **Measurement is his own.**
  - [stated] He ran the late-2007 CPLEX test (P5 p. 116), the Nov–Dec 2002 CPLEX 1.0 run (P9 slides 9–14) and the OR 2002 test sets (P4).
  - [observed] The Gurobi version-to-version figures in his decks (P10; P9) are measurements of a team's code that he presents.
- **TSP and Concorde**: joint with Applegate, Chvátal and Cook; roles not divided.

---

## 8. Latest dated traces and the last 12 months (2025-11-05 → 2026-11-05)

- **Latest dated trace of his own**: the long interview *Subject to: Robert Bixby*, published on YouTube on 6 Dec 2023 (Pacific time; 8,024 s), with the recording date not stated (P20). He describes himself there as retired but not completely, expects to keep voicing opinions on Gurobi's management and direction for a few more years, and says his research days are over (caption text). This post-dates the Sept 2022 deck that team.json names as the latest dated trace. **Flag for the user**: it extends the record by about 15 months, but it is still a 2023 self-description, not a 2026 one.
- **Latest dated lecture**: the Hausdorff School lecture on Monday 12 Sep 2022 (O15; deck P8 dated Sept 2022, PDF created 13 Sep 2022).
- **Latest paper**: the 2020 presolve paper (S1; S3). OpenAlex and DBLP list nothing later.
- **Later documents that name him, none recording an activity of his**:
  - Gurobi's release of 2 Jan 2023 names Rothberg Chairman of the Board. Bixby is not mentioned, so when or whether he left the chair is not documented (O14).
  - The NAE induction programme of 29 Sep 2024 (PDF created 25 Sep 2024) lists him among the Anniversary Members of 25–29 years (O13). The programme does not say whether such lists include only living members. I did not verify NAE practice, and this listing **does not establish** living status or role.
  - The undated UC Berkeley IEOR page calls him President and Co-founder of Gurobi (O12). It is stale against the 2015 change and is not a dated trace.
  - Gurobi's April 2020 video description calls him co-founder and advisor (P21). The March 2021 Toronto bio says he serves on the Gurobi board (O10). The latest dated role statement found is his own, from the Dec 2023 interview (P20).
- **Last 12 months**: no paper, talk, code, interview or role statement found.
  - Basis: three WebSearches aimed at recent activity ("Bob Bixby" OR "Robert Bixby" optimization 2026; "Bob Bixby" Gurobi 2025; Robert Bixby CPLEX Gurobi co-founder news 2026), plus the DBLP, OpenAlex and NSF records and the upload dates of the videos in `talks/`.
  - Unused leads: a third-party aggregator claim about the co-founders, and a search-tool summary of an unreachable Gurobi GOR 2024 page that called him Advisor and Co-founder. Neither was verifiable, so neither is used.
- **Living status and present role: not established. Not stated.**

---

## 9. Pointers for the synthesis (all [inferred])

1. **Trigger pattern for choosing problems**: a named, failing real instance from a partner or customer, then a fix in the production code, then a version-to-version measurement. This repeats from 1985 to 1994 (Chesapeake SLPs, AA, LAU2, Saigal) and is the best-evidenced account of how he chose what to build next.
2. **Measurement career arc**:
   - 1986: hand-recorded table against one competitor on 13 netlib LPs.
   - 2002: 680 real LP models, ratios and geometric means binned by size.
   - 2007: 12 recompiled versions × about 1,900 MIPs, with a time limit.
   - 2012–2022: deck series re-measuring Gurobi releases.
   - The numbers move between editions (Contradictions). A skill should teach his method and flag that his published figures are edition-dependent.
3. **Funding and institutions shaped the framing**: matroids → LP structure → LP tools *for IP* → MIP. NSF programme names track the turns.
4. **Role boundary for the skill**: hands-on code until about 1997. Then team leadership and measurement. From 2008 no code at all.
5. **For agent 05**: test his 2012 parallel-simplex judgment and his 1994 barrier stance against later evidence. Ask whether his best-of-barrier/primal/dual yardstick, which he himself calls arguable (P5 p. 114), inflates the progress figures. In 2021 he defended that yardstick: in 1988 there was only one algorithm (P23, caption text).
6. **For the synthesis of the skill's honest boundary**: his 2023 remark that he might write a paper on the LP story is an open item, and his statement that his research days are over is the latest first-person scope statement (P20).

---

## Contradictions (kept, not reconciled)

1. **CPLEX Optimization founding year**:
   - 1987: the 2015 interview (incorporated, P1 p. 3), the 2023 interview with hesitation (P20), the 2021 Toronto bio (O10) and the Berkeley page (O12).
   - 1988: his 2020 Gurobi clip (P21), his 2021 talk itself (P23), his 2022 slide (P8 slide 10) and Rothberg's INFORMS story (O4).
   - The 2021 event bio and the 2021 talk disagree with each other.
2. **First Amoco sale**: around 1986 in the 2015 interview (P1 p. 3); 1987 in the 2021 talk (P23) and on the 2022 slide (P8 slide 10). OR 2002 dates the customer interest to about 1986 without naming Amoco (P4 p. 3).
3. **Co-founders**:
   - 2022 slide: Janet Lowe only (P8 slide 10).
   - Interview: Janet and Todd Lowe, with 49% of the equity between them (P1 p. 3).
   - INFORMS Impact Prize 2004 team: Bixby, Janet Lowe and Paul Green (O7). Paul Green's role was not found.
4. **When he joined Rice**: 1983 per the Rice profile (O1). In 2015 the interviewer said 84/85, and Bixby thought he was probably already at Rice by then (P1 p. 2). In 2023 he placed the C conversion at about 1984, when he was already at Rice (P20). He places the start of the classroom code at Northwestern (P1 p. 1; P20), while his slide dates that start to 1983 (P8 slide 10).
5. **LAU2 episode**:
   - Interview: CPLEX version 1.x or maybe 2, on a Cray Y-MP (P1 p. 3).
   - 2022 slide: 1987, CPLEX 1.0, on a Cray X-MP (P8 slide 23).
   - OR 2002 dates the CPLEX 1.0 release to 1988 (P4 p. 4).
6. **His first comparison with XMP**:
   - 2015 interview: 4× faster on almost all models within a week or so (P1 p. 2).
   - OR 2002: about 2× faster on average over a substantial subset of netlib (P4 p. 3), and 4.7× for CPLEX 1.0 against XMP (P4 p. 13).
   - My transcription of the 1986 sheet: geometric mean ≈ 1.8×, and only BANDM at ≥ 4× (P8 slide 12).
   - The interview also recalls standata as about a thousand rows; the sheet shows 359.
7. **Parallel simplex**: the 1995 preprint reports quite good results for the thread-based dual on a wide range of models (P7 p. 20). In 2012 he judged that parallelizing simplex had essentially no success (P5 p. 114).
8. **LP progress since 2004**:
   - 2012 and 2017: essentially no progress since 2004 (P5 p. 115; P9 slide 16).
   - 2022: about 3× on large models over the previous 7 years, i.e. since about 2015 (P8 slide 30).
   - The May 2017 deck falls inside that later 7-year window and still says little progress.
9. **Machine factor in Documenta's LP table**: the machine-improvement line reads 1600×, but the total is computed as 3300 · 2000 (P5 p. 114).
10. **Size of the late-2007 MIP test set**: 1,892 models (P5 p. 116) against 1,852 (P9 slide 30). The slide's own subtraction (2,791 − 559 − 348 − 22) gives 1,862.
11. **Gurobi 1.0→5.0 cumulative speed-up**: 16.2× in 2012 (P5 p. 118; P10 slide 8). 9.3× in 2017 (P9 slide 36), which also re-states 2.0→3.0 as 1.9× instead of 2.9× and 4.0→5.0 as 1.7× instead of 1.9×.
12. **Gurobi role in 2017**: the ECCO invited-speaker bio says co-founder and CEO (O11). The 2015 interview says Chairman and CSO (P1 p. 6). The 2021 bio says CEO 2008–2015 (O10).
13. **Waterloo honorary doctorate**: 2012 in the 2017 and 2021 bios (O11; O10). 14 June 2013 in Waterloo's citation and news item (O2; O3).
14. **ILOG titles**: board member, CPLEX Development Team manager, TAB president and GM of the semiconductor division (O12; O4 without the board). "CSO, ILOG" (2006 byline, P19) and Chief Science Officer (2007 news, S5) appear in neither list.
15. **Wording of the NAE citation**: Waterloo's citation and the Berkeley page give the reason as contributions to optimization theory and practice (O2; O12). Wikipedia and the search summary of the NAE profile give contributions to combinatorial optimization and to developing and commercializing high-performance optimization software (S7; S6). The NAE page itself was not read.
16. **BS subject**: Industrial Engineering (Rice profile, O1) against Industrial Engineering and Operations Research (O2; O9; O12).
17. **His MIP role**: by his 2015 account he did little on MIP, crediting Todd Lowe with the push for a MIP and Gu and Rothberg with the 6.5 code (P1 pp. 3–4). In 2023 he named Mary Fenelon as primary developer of the early CPLEX MIP *with his assistance* (P20, caption text). OR 2002 says Fenelon did not contribute directly to the LP algorithms (P4 p. 14), which is consistent with a MIP role. The record shows him as PI of a 1994–97 NSF MIP grant with a research-code plan (P13), MIPLIB builder (1992, 1998) and co-author of the 2000, 2004 and 2007 MIP progress reports. This is kept as a tension; it is compatible with his not having written the CPLEX 6.5 MIP code.
18. **Funding failure**: the 2022 slide reports total failure to fund LP computation in 1987–88 (P8 slide 10), and the 2021 and 2023 retellings say no one was interested in funding simplex work (P23; P20). NSF records show an LP-structure award running to Nov 1987 (8416187) and LP-tools-for-IP funding from Feb 1989 (P14; P12). The dates are compatible, but the retellings omit both awards.
19. **How Gurobi began for him**: in 2015, Gu and Rothberg started within weeks of leaving ILOG and he contacted them and asked to help (P1 p. 4). In 2023, they had planned the company and he left independently at about the same time, for overlapping but not identical reasons (P20, caption text).
20. **Rice status against bylines**: he gave up tenure in 1998 and Rice counts him as retired from 2000 (P20, caption text). Yet Rice appears on his bylines in 2000 (CAAM), 2002, 2003 (CAAM), 2004 and 2008 (Graduate School of Management) (P19; P4). Later bios list emeritus and research-professor-of-management titles (O2; O12). These may be compatible titles; they are not reconciled here.

---

## Gaps

- **Rice dates**: the exact appointment date, the Noah Harding chair date, the emeritus date and the dates of his Jones School research professorship were not found in any Rice document. The only dates for giving up tenure (1998) and retiring (2000) come from the 2023 interview captions.
- **Unverified bio items**: Editor-in-Chief of Math. Programming Series A 1989–1994, MPS Chair 2001–2004, and a Humboldt Senior Scientist award (year not given). They appear only in event bios (O9; O10) and were not checked against MOS, Springer or Humboldt records.
- **2015 CEO→CSO date**: team.json's 3 Sep 2015 was not re-verified. The release could not be read (PRWeb 403, www-old.gurobi.com 503, the newsroom page did not render); only the undated title and snippet were seen.
- **ILOG**: the dates of each title, and the month he left in 2008, were not found. The date of IBM's acquisition of ILOG was seen only in Wikipedia (S7).
- **Unread full texts**: *Closing the Gap* (2000; agent 01 read a preprint), Sharpest Cut 2004, Annals 2007, IJOC 2000 (could its conclusions differ from the 1995 preprint?), the 1994 commentary, the TSP book's LP chapters, and the DTIC reports (403).
- **Talk recordings**:
  - The Toronto 2021 and 2023 *Subject to* recordings were read only as automatic-caption transcripts saved by a sibling agent. The videos were not watched, and the 2023 text is an excerpt.
  - The 2023 recording date is an inference from internal references by the transcriber; the omitted opening part was not re-checked here.
  - The *Subject to* channel's host was not identified. The player.fm page for the same series returned 403.
  - Tutte Colloquium 2013: not found.
- **The 2004 update of his LP progress figures**: venue not found.
- **Possible sequels**: no Part II of *Embedded Network Rows* found. No Part III or later of the 1992 simplex series found.
- **Dadmehr 1995 dissertation** (simplex-based method for large LPs): not read. Its relation to sifting or CPLEX is unknown.
- **Last 12 months**: no trace found. **Living status and present role: not established** (see §8).
- **Two leads from search tools that could not be verified, and are therefore not used**: GOR 2024 Advisor and Co-founder (404), and an aggregator claim (2026).

---

## Sources

**Primary: his own texts, decks, grants and bylines**

- P1. V. Kaibel, J. Lee, J. Linderoth (questions, Oct 2015, Oberwolfach), "You have to figure out who your customer is going to be — An interview with Bob Bixby", *Optima* 101, Sept 2016, pp. 1–6. https://mathopt.zib.de/Optima-Issues/optima101.pdf — primary
- P2. M. Grötschel, "Comments on Bob Bixby's interview: Mathematics and the Real World", *Optima* 101, pp. 6–7 (same URL) — primary (observed)
- P3. W. Cook, "Comments on Bob Bixby's interview: Beauty in the Details", *Optima* 101, p. 7 (same URL) — primary (observed)
- P4. R. E. Bixby, "Solving Real-World Linear Programs: A Decade and More of Progress", *Operations Research* 50(1):3–15, Feb 2002, DOI 10.1287/opre.50.1.3.17780; read at www.gwern.net/doc/cs/algorithm/2002-bixby.pdf — primary
- P5. R. E. Bixby, "A Brief History of Linear and Mixed-Integer Programming Computation", *Documenta Math.* Extra Vol. ISMP (2012) 107–121, DOI 10.4171/dms/6/16; www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-ismp/25_bixby-robert.pdf — primary
- P6. R. E. Bixby, "Das Implementieren des Simplex-Verfahrens: Die Startbasis", ZIB Preprint SC 92-11, April 1992 (OPUS front door dates it 1992-04-24), https://opus4.kobv.de/opus4-zib/files/81/SC-92-11.pdf (via WebFetch; OCR layer) — primary
- P7. R. E. Bixby, A. Martin, "Parallelizing the Dual Simplex Method", ZIB Preprint SC-95-45, December 1995, https://opus4.kobv.de/opus4-zib/files/211/SC-95-45.pdf (via WebFetch) — primary
- P8. R. E. Bixby, "Linear Programming: A Historical View", deck, Hausdorff School on Computational Combinatorial Optimization, Bonn, Sept 2022. https://www.or.uni-bonn.de/~held/hausdorff_school_22/slides/GUR_Hausdorff_Day1_LP_History.pdf — primary
- P9. R. E. Bixby, "Computational Progress in Linear and Mixed Integer Programming", deck, ECCO 2017 (PDF title "ECCO_Lecture_5May2017"). https://ecco2017.euro-online.org/en/resources/files/invited-speakers/robertbixby.pdf — primary
- P10. B. Bixby, "1000X MIP Tricks", deck, 12 June 2012 (Bill Cunningham's 65th), Fields Institute. https://av.fields.utoronto.ca/programs/scientific/11-12/bc65/rbixby.pdf — primary
- P11. R. E. Bixby, S. Ceria, C. M. McZeal, M. W. P. Savelsbergh, "An Updated Mixed Integer Programming Library: MIPLIB 3.0", *Optima* 58, June 1998, pp. 12–15; plus the publications-committee notice, p. 2. https://mathopt.zib.de/Optima-Issues/optima58.pdf — primary
- P12. NSF Award 8815914, "Linear Programming Tools for Integer Programming", PI R. E. Bixby, Rice, 1989-02-15 to 1993-01-31, record and abstract. https://api.nsf.gov/services/v1/awards/8815914.json — primary
- P13. NSF Award 9407142, "Mathematical Sciences: Investigations in Mixed Integer Programming", PI R. E. Bixby, Rice, 1994-12-01 to 1997-11-30, record and abstract. https://api.nsf.gov/services/v1/awards/9407142.json — primary
- P14. NSF Awards 7607640, 7802270, 8104881, 8416187, 8519204 (PI R. E. Bixby): titles, dates, programmes, amounts; no abstracts. https://api.nsf.gov/services/v1/awards.json?pdPIName=Bixby — primary
- P15. R. E. Bixby, "Hidden and Embedded Structure in Linear Programs", DTIC report, 1983-09-30, DOI 10.21236/ada137773 (abstract via OpenAlex; PDF 403) — primary
- P16. R. E. Bixby, "Commentary—Progress in Linear Programming", *ORSA J. Comput.* 6(1):15–22, 1994, DOI 10.1287/ijoc.6.1.15 (abstract and byline via OpenAlex) — primary
- P17. Bixby, Fenelon, Gu, Rothberg, Wunderling, "Mixed-Integer Programming: A Progress Report", *The Sharpest Cut* (MPS-SIAM 2004), ch. 18, pp. 309–325, DOI 10.1137/1.9780898718805.ch18 (abstract and byline via OpenAlex) — primary
- P18. Bixby, Martin, "Parallelizing the Dual Simplex Method", *INFORMS J. Comput.* 12(1):45–56, 2000, DOI 10.1287/ijoc.12.1.45.11902 (abstract and byline via OpenAlex) — primary
- P19. Paper bylines (raw affiliation strings via the OpenAlex works API) for DOIs 10.1007/978-0-387-35514-6_2, 10.1007/s10479-006-0091-y, 10.1109/asmc.2006.1638740, 10.1109/wsc.2008.4736331, 10.1016/j.orl.2008.09.006, 10.1007/s10107-003-0440-4, 10.1007/s12532-011-0025-9, 10.1287/ijoc.2018.0857 — primary (bylines)
- P20. "Subject to: Robert Bixby", long interview, YouTube channel "Subject to", published 2023-12-06 (Pacific time), 8,024 s, https://www.youtube.com/watch?v=47BZgFhEFJ8. Identity checked via oEmbed; date and length from the watch-page metadata. Read as the automatic-caption excerpt saved in this run by a sibling agent at `references/sources/talks/subject-to-2023-interview.excerpt.transcript.txt` (not speaker-checked; names garbled; private passages omitted by the transcriber) — primary (caption text)
- P21. "How was Gurobi founded?", YouTube channel "Gurobi", published 2020-04-08, 200 s, https://www.youtube.com/watch?v=YoQ2h_G3PNM. The description calls him co-founder and advisor. Read as the automatic-caption transcript in `references/sources/talks/short-clips-2015-2020.transcript.txt` — primary (caption text; description observed)
- P22. "Robert Bixby: Solving Linear Programs: The Dual Simplex Algorithm (1/3)" and parts 2–3, CO@Work 2015, Zuse Institute Berlin YouTube channel, part 1 published 2016-10-06, https://www.youtube.com/watch?v=z1xvqwQR6xU. Identity, date and description were checked here; content read only as the header of `references/sources/talks/co-at-work-2015-dual-simplex-lectures.transcript.txt` — primary (used for dating only)
- P23. R. E. Bixby, talk "Optimization: Past, Present, Future", U of T MIE, 19 Mar 2021, video published 2021-03-22, 4,314 s, https://www.youtube.com/watch?v=_R8-nt5NyiE. Read as the automatic-caption transcript `references/sources/talks/toronto-2021-optimization-past-present-future.transcript.txt` (saved by a sibling agent; searched for dated statements, not read in full) — primary (caption text)

**Primary: institutions and first-hand observers**

- O1. Rice University faculty profile "Robert Bixby", https://profiles.rice.edu/faculty/robert-bixby (via WebFetch; undated) — primary
- O2. University of Waterloo, "Citation and biography — Mathematics a.m. convocation, June 14 2013: Robert Bixby (DMath)", https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/bixby_citation.pdf — primary
- O3. University of Waterloo C&O, "Bob Bixby awarded an honorary DMath degree", 14 June 2013, https://uwaterloo.ca/combinatorics-and-optimization/node/1730 — primary
- O4. E. Rothberg, "Gurobi Optimization" (INFORMS O.R. & Analytics Success Stories; undated, about 2013), https://www.informs.org/Impact/O.R.-Analytics-Success-Stories/Industry-Profiles/Gurobi-Optimization — primary (observed, co-founder)
- O5. INFORMS, "Fellows: Alphabetical List" (Bixby, class of 2002), https://www.informs.org/Recognizing-Excellence/Fellows/Fellows-Alphabetical-List — primary
- O6. INFORMS, Frederick W. Lanchester Prize winners (2007), https://www.informs.org/Recognizing-Excellence/INFORMS-Prizes/Frederick-W.-Lanchester-Prize — primary
- O7. INFORMS, Impact Prize winners (2004 team), https://www.informs.org/Recognizing-Excellence/INFORMS-Prizes/Impact-Prize — primary
- O8. Mathematical Programming Society, "Past Winners of the Beale-Orchard Hays Prize" (2000), http://www.mathprog.org/prz/boh.htm — primary
- O9. Imperial College London, seminar "Computational Progress in Linear and Mixed Integer Programming (Robert Bixby, Gurobi)", 13 May 2015, https://imperial.ac.uk/events/104423/computational-progress-in-linear-and-mixed-integer-programming-robert-bixby-gurobi — primary
- O10. University of Toronto MIE, "MIE Distinguished Seminar Series with Dr. Robert Bixby: Optimization: Past, Present, Future", 19 March 2021, https://www.mie.utoronto.ca/?p=19855; video https://youtu.be/_R8-nt5NyiE (identity via YouTube oEmbed; not watched) — primary
- O11. ECCO 2017, Invited speakers page, https://ecco2017.euro-online.org/en/invited-speakers.html — primary
- O12. UC Berkeley IEOR, Advisory Board, "Bob Bixby" (undated), https://ieor.berkeley.edu/advisory_board/bob-bixby/ — primary
- O13. National Academy of Engineering, "Induction Ceremony, September 29, 2024" programme (PDF created 2024-09-25), https://www.nae.edu/File.aspx?id=323166 — primary
- O14. Gurobi Optimization, "Gurobi Appoints Duke Perrucci as Chief Executive Officer", Beaverton, 2 Jan 2023, https://www.gurobi.com/company/newsroom/gurobi-appoints-duke-perrucci-as-chief-executive-officer — primary
- O15. Hausdorff School on Computational Combinatorial Optimization, 12–16 Sept 2022, programme page, https://www.or.uni-bonn.de/~held/hausdorff_school_22/ — primary

**Secondary**

- S1. DBLP person 75/1779 via `scripts/dblp_works.py` (sparql.dblp.org), 2026-11-05: 38 records, 1974–2020 — secondary
- S2. OpenAlex: author A5012463224 (96 works; affiliation years), split author A5097662446, works 1986–1993, title searches, 2026-11-05 — secondary
- S3. Crossref REST API metadata for every DOI cited in this note, incl. the TSP book chapter DOIs (10.1515/9781400841103.345, .373) and MIPLIB 2003 (10.1016/j.orl.2005.07.009), 2026-11-05 — secondary
- S4. Mathematics Genealogy Project: records 14993 (Bixby), 26980 (Billera), 67627, 67628, 143732, 39318, 29587, 39317, 39316, 29594, 37969 (students), https://www.mathgenealogy.org/ — secondary
- S5. Korea University Business School news no. 620, SCM/logistics seminar, 2007-11-16, https://biz.korea.ac.kr/eng/news/news_view?no=620 (via WebFetch) — secondary
- S6. WebSearch result lists (7 queries, 2026-11-05): leads only. These include the undated title and snippet of the 2015 Gurobi CEO→CSO release and a summary of the NAE member page — secondary
- S7. Wikipedia: "Robert Bixby", "Václav Chvátal", "William J. Cook", "ILOG", "Frederick W. Lanchester Prize" (raw wikitext, 2026-11-05): leads only — secondary
- S8. Daily Research News Online, Gurobi leadership news, 3 Jan 2023, https://www.mrweb.com/drno/news34378.htm (via WebFetch) — secondary
- S9. `product/lp-team/robert-e-bixby/references/research/01-publications.md` (sibling note, this run): lead only; every item used was re-verified here — secondary
- S10. `product/lp-team/robert-e-bixby/references/sources/publications/{publications,abstracts}.md` (OpenAlex summary generated 2026-11-05): lead only — secondary
- S11. ZIB OPUS front door for SC 92-11, https://opus4.kobv.de/opus4-zib/frontdoor/index/index/docId/81 (via WebFetch): date metadata — secondary
