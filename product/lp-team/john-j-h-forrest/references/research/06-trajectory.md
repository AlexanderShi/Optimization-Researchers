# 06 · Research trajectory: timeline, lineage, turns and their triggers

> **Researcher**: John J. H. Forrest (also John J. Forrest, J. J. H. Forrest, John Forrest; DBLP pid 08/3168; OpenAlex A5061258306). Not Jeffrey Yi-Lin Forrest (grey systems), Stephanie Forrest or the other Forrests that name searches return.
> **Dimension**: research agent 06 of 06, research trajectory (nuwa research-craft Phase 1). Serves framework layer 2 (problem choice and timing) and layer 7 (organisation), with pointers for layers 1, 4 and 5.
> **Research date**: 2026-11-05
> **Sources consulted**: 39, listed under "Sources" (22 primary, 17 secondary). Identifiers checked with a tool in this run: 15 DOIs (Crossref REST API), 1 arXiv id (arXiv API), 7 DBLP records (DBLP SPARQL endpoint through `scripts/dblp_works.py`), 2 venue + year + title records taken from Springer reference lists. **WebSearch calls used: 4 of 7.**
> **Local corpus**: `references/sources/papers/`, `talks/`, `essays/` and `software/` held only `.gitkeep`. `publications/` holds the OpenAlex harvest summary (`publications.md`, `abstracts.md`), which the pipeline generated; it is not user-supplied. **Nothing below is from user-supplied material.** `private/` was not opened. No talk recording or transcript was found, so nothing was saved under `sources/talks/`.
> **Method (code-first lens)**: blobless clones of eight COIN-OR repositories (Clp, Cbc, CoinUtils, Cgl, Osi, Bonmin, Couenne, CoinMP) and shallow clones of the first four, all read on 2026-11-05: commit counts by year and author, file-creation commits, the first Clp commit `b4253486` (2002-07-30), README and AUTHORS histories, copyright lines, design notes. GitHub REST API without login: the two account profiles, commit search, issue search (`commenter:jjhforrest`), 22 issue threads, and every issue comment created in Cbc, Clp, CoinUtils, Cgl and Osi between 2025-11-05 and 2026-11-05. Crossref and Springer article pages for affiliations, abstracts and reference lists. Full texts read: the ICM 1998 chapter, Optima 75, Bixby's 2012 history, Huangfu & Hall (2018), Galabova & Hall (arXiv v1). INFORMS award pages, COIN-OR web pages and the Mathematics Genealogy Project.
> **Tags**: [stated] = Forrest's own words in text he wrote alone: code comments under his Authors line or in his commits, his commit messages, his GitHub comments. [stated-joint] = co-authored text, where his voice cannot be separated. [practice] = what the record shows he did (commits, file creation, affiliations in print, copyright lines, releases). [observed] = what others wrote (award citations, maintainers' READMEs, third-party papers, other users' issue text). [inferred] = my reading, which no source states. Each item also carries **P** (primary) or **S** (secondary).
> **Quoting**: quotations are verbatim. In code comments, commit messages and GitHub comments I collapsed runs of spaces and line breaks to single spaces. I changed nothing else, except the ligature "ﬀ" in one aggregator abstract, which I wrote as plain letters (marked where it occurs). Commit and account e-mail addresses are deliberately not reproduced; only the domain named in the task (fastercoin.com) is mentioned.
> **Sibling notes**: `01-publications.md` and `03-process-evidence.md` appeared in this folder while this note was being written. I used them only as leads for two items (the 1978 Beale–Forrest chapter and the 1987 Royal Society talk) and re-checked both myself on the Springer reference lists (S6, S9).

---

## 0. Identity, accounts and authorship hygiene

- **Two GitHub accounts, one display name.** `johnjforrest` was **created 2019-06-14** and last updated 2020-05-12. `jjhforrest` was **created 2014-03-31** and last updated 2026-09-02 (S2). The commits of 2002–2019 are attributed to `johnjforrest` only because COIN-OR's 2019 SVN-to-git conversion mapped them to one identity with a fastercoin.com address. That domain appears on every commit of his from 2002-03-08 to 2020-05-11 17:11 UTC, so **the commit e-mail cannot date any change of employer**. From 2020-05-12 09:26 the same name commits with a webmail address, under `jjhforrest` (S1). `jjhforrest` was already commenting on GitHub issues from 2017 (the first issue he commented on was opened 2017-11-15), and `johnjforrest` has commented on one issue (Clp, 2020). The link between the two accounts and the person is strong inference (same name, the hand-over of 2020-05-11/12, comments signed "John Forrest" or "JJHF"). No document states it. [practice, P; link inferred]
- **Committer is not author.** File-creation commits can mislead. `CbcModel.cpp` and `CbcNode.cpp` enter Cbc in a 2004-10-29 commit by Laci Ladanyi, "Import of Coin Branch-and-Cut (formerly known as Sbb)". `ClpPESimplex.cpp` was committed by Forrest on 2015-06-25, but its header reads "Authors Jeremy Omer Last update: june 10, 2014" (S1). He says the same about himself: "I presume that whoever wrote the code (which might be me years ago) was not sure if the code included by the ifdef was correct" (Cbc #332, 2020-09-08) (S3). [stated/practice, P]
- **Copyright lines are templated** and lag. `CglZeroHalf.hpp` carries "Copyright (C) 2010, International Business Machines", but its first commit is Forrest's "add first try at zero half cuts" of 2013-01-10. So the one non-IBM holder he used, "Copyright (C) 2012, FasterCoin" on the 56 Abc files, is suggestive about his employer, but it is not proof. [practice, P]
- **Living**: rests on account activity. His latest commit is 2026-11-03 (Cgl `stable/0.60`). His latest comment is 2026-11-01 (Cbc #837) (S1, S3). [practice, P]

---

## 1. The trajectory in one paragraph (all [inferred], built from §§2–8)

Forrest's career is **one craft carried across four institutional forms**, which the 2005 COIN-OR Cup citation lists as "from proprietary consulting tools, to commercial solvers, to commercial libraries, to flexible extensible open-source libraries" (S26). The craft is to make LP and MIP codes survive real customer models. At CEIR/Scicon (by 1972, until at least 1976) he worked in E. M. L. Beale's circle on product-form LP updates (Forrest–Tomlin 1972) and on branch and bound inside a full mathematical programming system (UMPIRE 1974; special ordered sets for global optimization, 1976 and 1978). A gap of more than a decade follows, for which only others' credits survive ("Sciconic, MPSX370"). By 1987 he was giving a talk on LP on the IBM 3090 vector facility. Around 1988–1991 he and Tomlin produced IBM's OSL, which Bixby calls "the designated replacement for MPSX/370, developed primarily by John Forrest and John Tomlin" (S23 p. 113). Then came steepest edge with Goldfarb (1992), and Sprint and the volume crash for airline crew pairing (1989–1998). Each of these turns was triggered by **hardware or by a class of customer model** (3090 vector, then RISC; then millions of crew-pairing columns), not by a theoretical question. In 2000–2002 IBM Research launched COIN-OR, and he became its "Founding Benevolent Dictator" (S26). He restarted from scratch in C++: Clp (first commit 2002-07-30), Sbb, which became Cbc (2003–2004), and an internal reliability campaign on "IBM Burlington problems". His design notes of that first day reckon openly with OSL ("I overdid that in OSL"). Through 2004–2009 the open-source code became the vehicle for his applied IBM work (semiconductor supply chain, Wagner Prize 2005) and for the IBM–CMU MINLP project (Bonmin, 2006–2007). Between December 2007 and August 2012 he left IBM; no source gives the date. He kept working as an independent volunteer maintainer. Aboca/Abc, a parallel dual simplex (2012), was presented at a conference and never written up, and he later called it "partially successful". From about 2017 on, GitHub issues are where most of his visible work happens. He became the most frequent committer to Cbc and Clp masters (2021–2025). In 2023–2024 he turned to SCIP's open presolve (PaPILO) after SCIP's license change, instead of building MIP presolve himself. In 2026 a new lead committer (Haroldo Santos) dominates Cbc, and Forrest is visible as the person who **profiles, sets defaults and fixes old corners**: he switched off a costly new heuristic with a gprof profile, and he measured the system-time overhead of time checks. He also reaches back to his own oldest tools (Idiot, Sprint, Abc) for a 2026 set-partitioning request.

---

## 2. Dated timeline

| When | Event | Evidence | Tag |
|---|---|---|---|
| 1961 (context) | Beale is a founder member of CEIR, which BP bought and renamed Scicon | Wikipedia "Martin Beale" (S35) | [observed, S] |
| by Feb 1972 | At **Scientific Control Systems Ltd., Milton Court, London**, with J. A. Tomlin: "Updated triangular factors of the basis to maintain sparsity in the product form simplex method", *Math. Program.* 2:263–278 (DOI 10.1007/BF01584548). The abstract reports "computational experience on real problems of up to 3500 rows" | Springer page (affiliations, abstract) (S6); Crossref (S4) | [practice, P]; [stated-joint, P] |
| 1972 (context) | Tomlin returns to Stanford (Dantzig's Systems Optimization Laboratory); he is at NASA Ames from 1977 and at Ketron for most of the 1980s before joining IBM Research | INFORMS biographical profile of Tomlin (S33) | [observed, S] |
| Jan 1974 | "Practical Solution of Large Mixed Integer Programming Problems with Umpire", *Management Science* 20(5):736–773 (DOI 10.1287/mnsc.20.5.736). Forrest at Scicon Ltd., London; J. P. H. Hirst at British Petroleum; Tomlin "Presently affiliated with Stanford University". The abstract names the devices: "The most important devices used are “priorities,” the “best projection criterion” and “pseudo-costs.”" | Crossref record with abstract (S4) | [practice, P]; [stated-joint, P] |
| Dec 1976 | Beale & Forrest, "Global optimization using special ordered sets", *Math. Program.* 10:52–69 (DOI 10.1007/BF01580653). Both at Scicon, **Milton Keynes** | Springer page (S6) | [practice, P] |
| 1978 | Beale & Forrest, "Global Optimization as an Extension of Integer Programming", in Dixon & Szegö (eds.), *Towards Global Optimization 2*, pp. 131–149, North-Holland (no DOI) | Reference list of the 2007 Annals note on Springer (S9) | [practice, P; not read] |
| 1979–1986 | **No paper or talk found.** Others credit him as "a developer of Alligator, Umpire, Sciconic, MPSX370, OSL" (2005 Cup). Bixby dates "SCICONIC around 1976, an improved version of UMPIRE" and "MPSX/370 (for the IBM 370) around 1974" (S23 p. 111). The date he moved to IBM is not established | S26, S23 | [observed, S] |
| 1987 | Talk "Linear programming using IBM 3090 vector facility", E. M. L. Beale Memorial Symposium, The Royal Society, London. It is also the copyright year on the OSL factorization code he later ported ("Copyright (C) 1987, 2009, International Business Machines") | Reference list of the 1990 Annals paper (S9); CoinUtils source (S1) | [practice, P; talk not read; authorship of the 1987 code not shown] |
| Oct 1989 | Talk "Mathematical programming with a library of optimization subroutines", ORSA/TIMS, New York. The ICM chapter cites it for "John Forrest[16] introduced the so-called Sprint method." (p. 681) and gives a 1989 Sprint table: American Airlines, 5.5 million pairings, OSL, "All times are minutes of solution time on a S/390 (in 1989)." | ICM 1998 full text (S7) | [stated-joint, P; talk not read] |
| Dec 1990 | Forrest & Tomlin, "Vector processing in simplex and interior methods for linear programming", *Ann. Oper. Res.* 22:71–100 (DOI 10.1007/BF02023049). Forrest at **IBM T. J. Watson**, Tomlin at IBM Almaden. "Preliminary computational results of experiments on the IBM 3090 vector facility will be presented." | Springer page (S6) | [practice, P] |
| c. 1988–1991 | OSL released by IBM "At about the same time" as CPLEX ("first released in 1988"), "the designated replacement for MPSX/370, developed primarily by John Forrest and John Tomlin". The 1992 steepest-edge paper cites the OSL "guide and reference", document SC23-0519-2 (1991) | Bixby 2012, p. 113 (S23); reference list of DOI 10.1007/BF01581089 (S6) | [observed, S]; [practice, P] |
| c. 1992 (date inferred from "ten years ago" in 2002) | Probing in OSL. His 2002 comment: "This is a simplification of probing ideas put into OSL about ten years ago. The only known documentation is a copy of a talk handout - we think Robin Lougee-Heimer has a copy!" (who put them in is not said) | `CglProbing.hpp`, his commit "A bit of explanation", 2002-03-12 (S1) | [stated, P] |
| 1992 | Two OSL papers in *IBM Systems Journal* 31(1): simplex (11–25, DOI 10.1147/sj.311.0011) and interior point (26–38, DOI 10.1147/sj.311.0026). The OpenAlex abstract of the first describes changes of design for the IBM 3090 vector architecture and again for RISC System/6000 | Crossref (S4); OpenAlex abstract (S39); IEEE Xplore blocked | [practice, P]; abstract [S] |
| May 1992 | Forrest & Goldfarb, "Steepest-edge simplex algorithms for linear programming", *Math. Program.* 57:341–374 (DOI 10.1007/BF01581089). "These results demonstrate unambiguously the superiority of steepest-edge pivot selection criteria to other pivot selection criteria in the simplex method." | Springer page (S6) | [stated-joint, P] |
| 1995 | **INFORMS Computing Society Prize, First Place: John Forrest (IBM) and Donald Goldfarb (Columbia).** Neither page gives the citation; the co-winner suggests the steepest-edge work [inferred] | INFORMS award page; ICS prize lists (S27, S28) | [observed, S] |
| 1998 | ICM Berlin chapter with Anbil and Pulleyblank (all IBM Research), *Doc. Math.* Extra Vol. ICM III, 677–686 (DOI 10.4171/dms/1-3/65): Sprint, the volume algorithm "as a crash procedure for the simplex method when the Sprint method performs poorly" (p. 684), RS6000/590 timings. It ends: "Presently attention is switching to the schedule repair problem." (p. 684) | full text (S7) | [stated-joint, P] |
| summer 2000 | COIN-OR "launched at the 2000 International Symposium on Mathematical Programming as a three-year experiment by IBM Research"; he is credited as "Founding Benevolent Dictator of COIN-OR" | INFORMS 2014 Impact Prize citation (S27); COIN-OR Cup 2005 page (S26); COIN-OR Foundation page (S30) | [observed, S] |
| 2002-03-08 | Earliest commit under his name in the five repositories that hold his commits (Cgl), then Osi (2002-03-12) | git (S1) | [practice, P] |
| 2002-07-30 | **Clp added**, commit `b4253486` "Adding Clp to development branch": 38 files, 14,913 lines, with the design notes at the top of `ClpSimplexDual.cpp` / `ClpSimplexPrimal.cpp` (§5 T5) | git (S1) | [practice, P] |
| 2002-08-05 → 10-28 | "Improving reliability using IBM Burlington problems (Primal)", "Still trying to make more rugged on IBM Burlington problems", "After more IBM Burlington tests" | Clp commits (S1) | [stated, P] |
| 2002-10-10 | Example that runs Clp inside OSL ("ekk") programs: "written so that calls to osl in the middle of complex algorithms could easily be swapped for Clp code. This was to stress test Clp (and Osl :-))." | `examples/ekk.cpp` (S1) | [stated, P] |
| 2002-11-25 | Idiot crash added ("Idiot and modifications for Visual C++") | Clp commit (S1) | [practice, P] |
| 2003-01-21 | Tag `sbb-0-60-0` in Osi and Clp; commits "For Sbb" (2003-01-07), "64 bit, Sbb etc" (2003-08-13) | git tags and commits (S1) | [practice, P] |
| 2003-09-19 | Sprint driver comment: "This driver implements what I called Sprint when I introduced the idea many years ago. Cplex calls it "sifting" which I think is just as silly." | `ClpSolve.cpp`, his commit "Trying" (S1) | [stated, P] |
| 2003-10 → 2004-09 | Interior-point and barrier work in Clp: "ClpInterior compiles", "pdco seems to work", "Barrier + "improvements" in dual", "Wssmp cholesky", "hardening barrier", "improving interior point code" | Clp commits (S1) | [practice, P] |
| Oct 2004 | Clp 1.0. His version log: "Version 1.00.00 October 13 2004." The FAQ: "Version 1.0 was released in time for the 2004 INFORMS Annual Meeting (24-27 October, 2004)." | `ClpMain.cpp` (S1); Clp FAQ by "DN" (S31) | [stated, P]; [observed, S] |
| 2004-10-29 | Cbc imported "(formerly known as Sbb)" by Ladanyi. His first Cbc commit is "version 0.7" the same day | git (S1) | [practice, P] |
| 2004 | "In 2004, IBM and Carnegie Mellon University initiated a joint study aimed at Mixed Integer Nonlinear Programming (MINLP), with the goal of releasing the resulting software under the CPL on COIN-OR." | Optima 75, PDF p. 1 (S8) | [stated-joint, P] |
| 2005 | Peak commit year (600 commits on master across five repositories, §3). CBC tutorial chapter for INFORMS 2005 (TutORials, pp. 257–277, DOI 10.1287/educ.1053.0020). **Inaugural COIN-OR INFORMS Cup** ("The official release of CBC version 1.0 has just occurred."). **Daniel H. Wagner Prize** (winning material "A Mixed Integer Program for Semiconductor Supply-Chain Optimization at IBM") | git (S1); Crossref (S4); Cbc guide revision history (S32); S26; INFORMS award pages (S27, S29) | [practice, P]; [observed, S] |
| 2006 | IBM-affiliated papers: IJOC 18(1):129–134 (DOI 10.1287/ijoc.1040.0078; "Motivated by a real application from the steel industry") and *Interfaces* 36(5):386–399 (DOI 10.1287/inte.1060.0238; "IBM uses the model and method daily"). Cbc commits "for nonlinear" (from 2006-03-06) and "for bonmin" (from 2006-04-19) | Crossref with abstracts (S4); git (S1) | [practice, P] |
| Dec 2006 / Feb 2007 | Forrest & Tomlin, "Branch and bound, integer, and non-integer programming", *Ann. Oper. Res.* 149:81–87 (DOI 10.1007/s10479-006-0112-x), a history note. Forrest at "IBM Watson Research Center", Tomlin at Yahoo! Research. Its 24 references run from 1957 to 1991 | Springer page (S9) | [practice, P; full text not read] |
| 2007 | INFORMS Fellow. Threads in Cbc ("add threaded to trunk", 2007-07-15). **Optima 75 (Dec 2007): all four authors, him included, at IBM T. J. Watson** (PDF p. 5). Reference "16. J. Forrest and J. Lee (in preparation)." (PDF p. 4) for a MINLP-as-MILP "method using linked ordered sets" (PDF p. 2) | S27; git (S1); Optima 75 (S8) | [observed, S]; [practice, P] |
| 2009-07 → 11 | Port of the OSL factorization into CoinUtils ("This is ripped off from OSL!!!!!!!!!"). Version log: "1.11.00 November 5 2009 (Guy Fawkes) - OSL factorization and better ordering" | CoinUtils and Clp source (S1) | [stated, P] |
| 2010 | Commits fall to 56 on master (from 222 in 2009). "changes to help SCIP" (2010-08-11) | git (S1) | [practice, P] |
| **between Dec 2007 and Aug 2012** | **Leaves IBM** (no source dates it). The upper bound comes from the FasterCoin copyright on the 2012 Abc files; that bound is weak (§0) | §0 | [inferred from P] |
| 2012-08-28/30 | Aboca/Abc enters CoinUtils and Clp ("stuff for Aboca - shouldn't affect anyone"; "minor changes to implement Aboca"), "Copyright (C) 2012, FasterCoin". Talk "Aboca: a bit of Clp accelerated", 21st ISMP (2012), as cited by Huangfu & Hall | git and source (S1); S24 | [practice, P]; [observed, S] |
| 2013-01-10 | "add first try at zero half cuts" (Andreello–Caprara–Fischetti method) | Cgl (S1) | [practice, P] |
| 2014 | **INFORMS Impact Prize** to nine people, him included, "for their pivotal role in the creation and widespread adoption of COIN-OR" | INFORMS award page (S27) | [observed, S] |
| 2015-06-21 | "stuff from stable and start aboca_lite"; "allow for mkl factorization" | git (S1) | [practice, P] |
| 2017-01 → 2020-02 | "new attempts to go parallel" (2017-01-05), "for AVX instructions alignment" (2017-03-22), "more coding of avx instructions" (2020-02-17) | git (S1) | [practice, P] |
| 2017-11 | First GitHub issue threads with his comments (CoinUtils, Clp) | issue search (S3) | [practice, P] |
| 2019-02-22/23 | Clp 1.17.0 and Cbc 2.10.0: **the last minor releases**. Since then only 1.17.x / 2.10.x maintenance releases, prepared by the co-maintainers (the 2026 ones by Ted Ralphs) | git tags and release commits (S1) | [practice, P] |
| 2019-03-06 | Clp README (by Stefan Vigerske): "The code is written primarily by John J. Forrest, now retired from IBM Research." Removed 2020-07-15. Cbc README from 2019-03-09: "Cbc is developed by [John Forrest](http://www.fastercoin.com), now retired from IBM Research." | README histories (S1) | [observed, P] |
| 2020-05-11/12 | Commit identity switch (§0) | git (S1) | [practice, P] |
| 2023-02-20 → 03-09 | "Scip changed license in November - first attempt to use" (on `master`), then "rubbish attempt to use Scip presolve" (two commits that stay on the unmerged branch `usescip`) | Cbc commits and branches (S1) | [stated, P] |
| 2023-03-28 | "The Abc versions were a partially successful attempt to parallelize the simplex method which were implemented more than 10 years ago for a conference and not kept up to date (Abc was short for Aboca - "A Bit Of Clp Accelerated" - Aboca actually being a small Italian frazione)." | Clp #262 (S3) | [stated, P] |
| 2024-06-25 | Design note signed JJHF on fathomMany and deterministic parallel (§5 T8) | `CbcGeneralDepth.cpp` (S1) | [stated, P] |
| 2024-09 | PaPILO hooked into Cbc ("Not much work has been done recently in Coin on pre-processing for integer problems and this does well on some problems."). He opens two issues on `scipopt/papilo` (2024-09-06, 2024-09-10) | Cbc and Cgl commit 2024-09-10 (S1); issue search (S3) | [stated, P] |
| 2025-05-23 | "I am not going to bother to fix this. The OSL factorization predates Coin." | Cbc #719 (S3) | [stated, P] |
| 2025-10-30 | "Changed depth parameter default to +1 from -1. This uses Clp in a more sophisticated way and does seem to faster. A user can always change it back." | Cbc commit (S1) | [stated, P] |
| 2026-03-11 | Maintenance releases Clp 1.17.11, Cbc 2.10.13, CoinUtils 2.11.13, Cgl 0.60.10, tagged by Ted Ralphs | git tags (S1) | [practice, P] |
| 2026-10-24 | Switches off Haroldo Santos's new SppGrasp heuristic (added 2026-10-18), with a gprof profile pasted into the commit (§8) | Cbc commits (S1) | [stated, P] |
| 2026-11-01 / 11-03 | Latest comment (Cbc #837) and latest commit (Cgl `stable/0.60`) | S3, S1 | [practice, P] |

---

## 3. Periods and their resource context

Commits under his name on `master` (SVN trunk before 2019), by year, for Clp, Cbc, CoinUtils, Cgl and Osi together (S1; distinct commits; branch copies excluded). He has **0** commits in Bonmin, Couenne and CoinMP.

| 2002 | 2003 | 2004 | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 67 | 269 | 401 | **600** | 221 | 262 | 269 | 222 | **56** | 127 | 48 | 92 | 90 |

| 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 (to 11-05) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 86 | 31 | 75 | 99 | 78 | 113 | **186** | 104 | 77 | 62 | 83 | 64 |

His share of each master: Clp 1303 of 2267 commits, Cbc 1060 of 3101, CoinUtils 533 of 1906, Cgl 434 of 1249, Osi 452 of 1798 (S1).

| Period | Setting and seniority | Resources and constraints | What it produced | Evidence |
|---|---|---|---|---|
| ≤1972–1976+, CEIR/Scicon (London, then Milton Keynes); the 1978 chapter with Beale shows the collaboration continuing, affiliation not seen | Developer (job title not found) in a consulting and software firm owned by BP, in Beale's group; Tomlin as peer until 1972 | Mainframe product-form codes, eta files; real client models ("up to 3500 rows"; MIPs with "a few thousand constraints"; BP co-author) | FT update; UMPIRE branch and bound; SOS global optimization | S6, S4, S23, S35 [practice/observed] |
| 1979–1986 | Not documented | — | Credited by others: Sciconic, MPSX/370 | S26, S23 [observed, S] |
| IBM Research (Yorktown) from at least 1990 in print (a 1987 talk on the IBM 3090 suggests earlier) to at least late 2007 | Title not found; product library (OSL), then research projects with clients (airlines, IBM's own semiconductor supply chain, steel) | IBM 3090 vector facility, then RISC System/6000; S/390 (1989), RS6000/590 (1990s); Tomlin at Almaden; IBM-internal models ("IBM Burlington problems", 2002) | OSL simplex and IPM; steepest edge; Sprint; volume crash; then Clp, Sbb/Cbc and Idiot as COIN-OR open source; applied MIP and column generation | S6, S7, S9, S1 |
| c. 2008–2012 → 2026, retired from IBM; "FasterCoin"; volunteer | Independent maintainer of a code base he largely wrote, inside a project the Clp README describes as "maintained by a small group of volunteers" [observed] | pthreads and Cilk keywords in Abc (`cilk_spawn`, `cilk_sync` in `AbcSimplexParallel.cpp`); MKL and OpenBLAS; AVX (2017–2020); in 2026 "stressing my small laptop" | Abc (2012); zero-half and symmetry/orbital code; deterministic parallel Cbc; PaPILO hook; defaults and bug fixes | S1, S3 |

---

## 4. Lineage

### 4.1 Upstream and formation

- **Advisor or degree: not found.** The Mathematics Genealogy Project (quick search "Forrest", 2026-11-05, while the site was only partly back online after its PHP outage) lists 12 people surnamed Forrest, none named John (S36). I found no education record (§ Gaps). [practice, S]
- **Formed in Beale's school at CEIR/Scicon.** Bixby: "A key figure in motivating these developments was E. M. L. (Martin) Beale in the UK. Among those who worked with Beale and were influenced by his vision of mathematical programming were R. E. Small and Max Shaw, followed by John Tomlin and John Forrest, both of whom continue to influence the field to this day." (S23 p. 109). Beale is first author of the 1976 paper and co-author in 1978. [observed, S; practice, P]
- **Tomlin is the career-long partner.** OpenAlex counts 6 joint papers, 1972–2006/07 (S39). The pair moved apart in 1972, when Tomlin went to Stanford, and came together again at IBM (by 1990, Watson and Almaden). Their last joint text is the 2007 history note, written when Tomlin had moved to Yahoo! (S9, S33). [practice, P]

### 4.2 Collaborators by period (from bylines; roles not divided)

Hirst (BP, 1974); Beale (1976, 1978); Goldfarb (Columbia, 1992); Anbil and Pulleyblank (IBM, 1998); Dietrich (IBM, 2002); de la Nuez and Lougee-Heimer (IBM; the Clp guide of 2004 and the Cbc guide of 2005, S31, S32); Kalagnanam and Ladányi (IBM, 2006); Denton and Milne (IBM STG, 2006); Bonami, Lee and Wächter (IBM, 2007). Every author list of his is alphabetical (01-publications §1.5, re-seen in S4), so byline order says nothing about roles. [practice, P]

### 4.3 Downstream

- **No doctoral students found**, and no university post. [practice, absence]
- **Code heirs, not students.** The co-maintainers named by the Cbc README are Ted Ralphs, Stefan Vigerske and Haroldo Gambini Santos (S1). In 2026 Santos is the dominant Cbc committer (478 master commits against Forrest's 31) and runs a fork, `h-g-s/mipster`, "a lightweight, streamlined Mixed-Integer Programming solver forked from COIN-OR CBC" (S2). In July and August 2026 Santos also removed dead code blocks from `CbcSolver.cpp` and `CbcModel.cpp` ("remove 685 lines of dead #if 0 / JJF_ZERO code"). The `JJF_ZERO`/`JJF_ONE` markers were Lou Hafer's 2009 labels for such blocks, "as a historical reference point" (S1). [practice/observed, P]
- **Third-party uptake of his undocumented devices.** Huangfu & Hall treat Aboca as prior art and note that "Other than making the source code available [5], the authors believe that there is no published reference to this work." (S24, PDF p. 8). Galabova & Hall analyse Idiot because "the Idiot crash is a major factor in this relative performance" on Mittelmann benchmarks (S25, p. 2). Bixby's history credits the DSE variant of Forrest–Goldfarb as one of "the most important advances" of the early 1990s (S23 p. 113), and Huangfu & Hall call DSE and BFRT "key reasons for the dual simplex algorithm being preferred" (S24, PDF p. 4). [observed, S]

---

## 5. Turns and what triggered them

**T1. Basis updates → branch and bound in a production system (Scicon, 1972 → 1974 → 1976/78).** Trigger: the integration of MIP into a general mathematical programming system, with client models in two classes, one with fewer than 100 binaries in a hard LP and one with several hundred SOS-structured integers in a simple LP (1974 abstract, S4). The 2007 history note says its emphasis is "the use of branch and bound to handle discrete constructs, which, while often formally representable in terms of zero-one integer variables, can be handled more elegantly and effectively by applying branch and bound to the actual dichotomies in the model" (abstract as reproduced on sciweavers.org, S38; the "ﬀ" ligature in "effectively" written as plain letters). [stated-joint, P for 1974; S for 2007]

**T2. Scicon → IBM (between 1976 and 1987; undated).** No stated reason found. The only bridges are others' credits ("Sciconic, MPSX370", S26) and the 1987 Royal Society talk on the IBM 3090 vector facility (S9). [observed; gap]

**T3. Hardware-driven redesigns at IBM (1987–1992).** Trigger stated in co-authored text: the OSL simplex paper discusses the interaction of implementation with hardware change, gives the redesign for the IBM 3090 vector architecture, and says the code had to be rethought again for RISC System/6000 (OpenAlex abstract, S39). The 1990 paper: "experiments on the IBM 3090 vector facility" (S6). [stated-joint, S abstract / P metadata]

**T4. A class of customer models → new LP strategies (1989–1998).** Trigger: crew-pairing LPs with millions of columns. The 1989 Sprint table uses 5.5 million American Airlines pairings (S7 p. 681). His own retrospective (2003): the idea "reminded me of an LP code of the 60's called sprint … On the problems of those days it did not work very well, but it worked very well on aircrew scheduling problems where there were very large numbers of columns all with the same flavor." (`ClpSolve.cpp`, S1). The volume algorithm entered as a crash "when the Sprint method performs poorly" (S7 p. 684). [stated, P; stated-joint, P]

**T5. Proprietary library → open source, restarted from scratch (2000 → 2002).** Trigger: IBM Research's COIN-OR initiative (S27, S30). No first-person reason for writing a new code rather than opening OSL was found. The first-day notes show the move as **a deliberate re-do of OSL**: "OSL did not have a phase 1/phase 2 approach but instead effectively put fake bounds on variables and this is the approach here, although I had hoped to make it cleaner." "I am using the modification of costs which I put in OSL and which was extended by Gill et al." "At present we never check we are going forwards. I overdid that in OSL so will try and make a last resort." (`ClpSimplexDual.cpp`, `ClpSimplexPrimal.cpp` at `b4253486`, 2002-07-30, S1). The FAQ entries signed "DN" (presumably David de la Nuez, a listed author of the Clp guide) state the design trade: "The design criteria were for it not to be too slow. Some speed has been sacrificed to make the code less opaque OSL (not difficult!)." They also claim Clp "has shown itself as reliable as OSL" (S31). He validated the new code **against the old one inside running applications** (`ekk.cpp`, 2002-10-10) and on IBM's internal "Burlington" models (S1). [stated, P; observed, S]

**T6. LP → MIP → MINLP, carried by the open code and by IBM's applied projects (2003–2007).** Sbb (2003), then Cbc (2004–2005). The semiconductor supply-chain MIP (Wagner Prize 2005; the paper's Milne sits at IBM's Essex Junction, Vermont site, S4) [practice]. Bonmin through IBM–CMU (2004 study, 2006 Open Collaborative Research; commits "for nonlinear"/"for bonmin" from 2006). His Clp version log ties LP work to the MIP driver: "Also modifications to make faster with sbb (I hope I haven't broken anything)." (1.00.01, October 2004, S1). Threads entered Cbc in 2007. *Inferred link*: the 2002 "IBM Burlington problems" and the Vermont semiconductor MIP are probably the same family of models (Essex Junction is in the Burlington area; general knowledge, not checked). No source states this. [inferred]

**T7. A short barrier excursion (2003–2004), then mostly upkeep.** Interior-point, pdco and Cholesky interfaces (WSSMP, TAUCS, AMD per the FAQ, S31) were built in 2003–2004. Later barrier commits are occasional: in 2009 "start Mumps cholesky", "try and improve quadratic and barrier" and "long double interior point"; in 2017 dense columns; in 2023 "exit barrier if not making progress"; in 2026 "use simplex not barrier if presolve says infeasible or unbounded" (S1). This repeats a pattern from the 1990s: he co-wrote OSL's IPM paper (1992), but his own published line stayed with the simplex method. [practice, P; pattern inferred]

**T8. IBM → retired volunteer; the parallel and SIMD turn without a paper (c. 2008–2020).** Trigger for Aboca: a conference talk (his own 2023 words: implemented "for a conference", S3) at ISMP 2012 (S24), in the multicore and Cilk era. He later downgraded it ("partially successful … not kept up to date"). Parallel work then moved into Cbc's tree search: deterministic parallel; fathomMany, described by him as "This does a few branches using Clp and tries to be much more efficient as it knows about Clp. It will also lend itself well to deterministc parallel and that is what this update to master is all about." (`CbcGeneralDepth.cpp`, 2024-06-25, S1). [stated, P]

**T9. Reuse over rebuild for MIP presolve (2023–2024).** Trigger stated in the commit itself: SCIP's license change, "Scip changed license in November - first attempt to use" (2023-02-20). The first route failed ("rubbish attempt to use Scip presolve", branch `usescip`, never merged). The second, PaPILO as an optional build flag, landed in 2024 with the stated gap "Not much work has been done recently in Coin on pre-processing for integer problems" (S1). [stated, P]

**What the turns share** [inferred]: (a) every turn has an external trigger: hardware (3090, RISC, multicore, AVX), a model class (crew pairing, semiconductor, set partitioning), an institution (IBM's COIN-OR experiment), a license (SCIP), or a conference (ISMP 2012). None is triggered by an open theoretical question. (b) He does not discard old devices. Sprint (1989), Idiot (2002) and Abc (2012) are the tools he reaches for in October 2026 (§8), and the volume crash is still in `ClpSolve.cpp` (`solveWithVolume`). (c) Write-ups come from co-authors or are skipped. His sole-authored record is code, comments, talks and issue answers.

---

## 6. Entry and exit relative to the field

| Topic | Entered | Relative to consensus | Left | Evidence |
|---|---|---|---|---|
| Sparse LU update for the simplex method | 1972 (FT update) | Early. Bixby lists "sophisticated LU-updates, based upon the Forrest-Tomlin [18] variant of the Bartels-Golub [3] update" among the ideas of the first-generation codes (S23 p. 110) | Never: `CoinFactorization` ("Authors John Forrest") is still Clp's default ("Normally the default is to use the normal CoinFactorization", parameter help). Which update it uses was not checked in this run | S6, S23, S1 [practice/observed] |
| Branch and bound in commercial systems | ≤1974 (UMPIRE) | Among "The first generation of these new codes, developed and/or released around 1970" (S23 p. 111) | Returned in 2003 (Sbb/Cbc) | S4, S23 |
| Steepest edge (primal and dual) | 1992 | Before the consensus: a 2018 account calls a "modern dual simplex implementation" one that adopts DSE (S24, PDF p. 7) | Never (Clp and Abc DSE pivots) | S6, S24, S1 |
| Sifting/Sprint | 1989 (talk) | His 2003 comment presents "sifting" as CPLEX's name for his idea ("Cplex calls it "sifting""); the relative dates were not checked | Never; reconsidered in 2026 for set partitioning | S7, S1, S3 |
| Interior point | 1990/1992 (OSL papers with Tomlin), Clp barrier 2003–2004 | After Karmarkar (1984) and OB1 (c. 1991, per S23 p. 113); as a component, not a research line | Upkeep only after 2004 | S6, S4, S1 |
| Open-source solvers | 2000–2002 (COIN-OR founder; Clp, Sbb) | Early | Still there in 2026 | S26, S27, S1 |
| Parallel dual simplex | 2012 (Aboca) | After Bixby–Martin's parallel dual work; Huangfu & Hall's later paper treats Aboca as prior art | De facto left by 2023 ("not kept up to date") | S24, S3 |
| GPU / first-order LP (PDLP type) | **Not entered**: none of his commit messages in the five repositories (all branches) mentions GPU, CUDA, PDLP, PDHG or "first order" (grep, 2026-11-05) | — | — | S1 [practice, absence] |
| MIP presolve | Cgl preprocessing from 2005 (`CglPreProcess.cpp`, first commit his, 2005-02-25); PaPILO hook 2024 | Late, by reuse | — | S1 |

---

## 7. Failures, abandoned directions and unfinished items

- **Self-critique of OSL carried into Clp's first day**: "I overdid that in OSL so will try and make a last resort." (2002, S1). [stated, P]
- **A reformulation idea he dropped because another method won**: "I did some work on this many years ago on "grade" problems, but while it improved primal interior point algorithms were much better for that particular problem." (`ClpNonLinearCost.hpp`, present in the 2002-07-30 commit, S1). [stated, P]
- **The 1960s Sprint code "did not work very well" on the problems of its day.** His idea succeeded only on a model class he found later (S1). [stated, P]
- **Unpublished works.** "J. Forrest and J. Lee (in preparation)" on MINLP via linked ordered sets (Optima 75, 2007). Linked ordered sets go back to "Beale and Daniel (1979) Chains of Linked Ordered Sets", cited in the 2007 note (S9). I found no such Forrest–Lee paper in Crossref, DBLP or OpenAlex (S4, S5, S39), although the code lives in Cbc (`CbcLinked.hpp`, "Copyright (C) 2006"; on the Cbc master under his name since at least 2007-06-26, S1). Aboca: no paper, and the "Never Asked Questions" page cited for it (fastercoin.com) is gone (S24; domain parked). Idiot: Galabova & Hall quote a 2014 mailing-list post in which Forrest refers to having given "a bad talk on it years ago" (S25, p. 2; the post itself is unreachable). [practice/observed]
- **A forecast he did not follow**: "Presently attention is switching to the schedule repair problem." (1998, S7). No later work of his on schedule repair was found. [stated-joint, P; absence]
- **Abandoned attempt, documented in its own commit**: "rubbish attempt to use Scip presolve" (2023-03-09, branch `usescip`, unmerged) (S1). [stated, P]
- **Parked code he declines to maintain**: "I am not going to bother to fix this. The OSL factorization predates Coin." (2025-05-23); the Abc downgrade of 2023; "only useful one is =4 anyway" (2020-03-29, of `--enable-aboca`) (S1, S3). [stated, P]
- **Releases stalled**: no Clp or Cbc minor release since February 2019. In October 2026 he writes "However - the main thing is to get next moved to master." (Clp #358, S3). [practice, P; stated, P]
- **Abandoned change logs**: "1.03.01 May 24 2006. Lots done but I can't remember what!" and "1.04.01 June 26 2007. Lots of changes but I got lazy" (`ClpMain.cpp`, S1). [stated, P]

---

## 8. The last 12 months (2025-11-05 → 2026-11-05)

- **Commits**: 83 across all branches, 73 of them on `master` (Clp 22, Cbc 37, CoinUtils 7, Cgl 16, Osi 1) (S1). Themes, in order:
  - asserts and memory leaks (Nov 2025 – Jan 2026);
  - the cost of reading the clock: "Try and reduce system overhead of getting time" (2026-04-29, in Clp, Cbc and Cgl), "speed up code by fewer calls to time (if no time limit set)" (2026-05-12), "only check time every 10 iterations - can save 1%!" (2026-05-13);
  - output and messages: "Try and make messages bear some resemblance to truth" (2026-06-01), "allow old style messages" (2026-10-07);
  - semi-continuous variables, SOS and lot-sizing tolerances (June–September). On the semi-continuous bug he wrote "Hopefully fixed. I should look more into those ideas from fifty years ago." (Cbc #784, 2026-06-25, S3), which points back to the Scicon era of the 1970s [inferred reading of "fifty years"];
  - MIP starts when maximizing (September–October);
  - Idiot and scaling: "out dubious scaling and safer idiot" (2026-10-22);
  - a preprocessing bug with too many singletons (2026-10-22/23, with "not sure what disaster last push was");
  - a stable-branch fix to `Cgl012Cut` (2026-11-03): "(I would like there to be a compile time option in master to disable minor time checks - it is a large overhead.)". [stated/practice, P]
- **Issue comments**: **43 comments in 25 threads** (37 on Cbc, 6 on Clp), 2025-11-16 → 2026-11-01. That puts him second among commenters in the five repositories in that window (Ted Ralphs 45). Monthly: Nov 1, Dec 3, Jan 5, Feb 2, Mar 4, Apr 1, Jun 6, Jul 1, Sep 6, Oct 13, Nov 1 (S3). Measurement as argument: on PR #774 ("fix time measurement and time limit") he posted real/user/sys timings for four settings and concluded that "when max time is set the system time varies a lot ranging from 1.2 seconds to 5.3 seconds" (Cbc #774, 2026-04-01). [practice/stated, P]
- **Handing on and gatekeeping (new in 2026).** Santos made 478 Cbc master commits in 2026 (S1). When Santos's GRASP heuristic for set partitioning landed (2026-10-18), Forrest switched it off with "SppGrasp can be Very expensive - so default off". His commit carries a gprof flat profile on a model named AIR03 (124 rows, 10,757 binary columns), with 91.92% of time in `CbcSppGrasp::localSearch` (2026-10-24). Santos answered with "Default SppGrasp to the validated AUTO policy with FPump retained" (2026-10-28) (S1). [practice, P]
- **Back to his oldest tools.** Ashutosh Mahajan reported set-partitioning models with 500,000–900,000 columns, where "CLP's idiot crash … is blazing fast on these models" (Cbc #837, 2026-10-27, S3) [observed, P]. Forrest replied: "Looking into it - stressing my small laptop. However I am also looking at using sprint. To solve initial Lp that was faster and I think will be more suited to branch and bound." (2026-10-28). And: "Have you got a tiny model i.e. only a million variables? Looking at various things - the answer may be as simple as abc." (2026-11-01). [stated, P]
- **Releases**: Clp 1.17.11, Cbc 2.10.13, CoinUtils 2.11.13 and Cgl 0.60.10 on 2026-03-11, tagged by Ralphs (S1). [practice, P]
- **Papers, talks, moves**: none found. The last indexed paper is from 2007 (DBLP 7 records, 1972–2007; OpenAlex none after 2007) (S5, S39). [practice, absence]

---

## 9. Pointers for the synthesis (all [inferred])

1. **Timing rule**: enter when a machine or a model class changes, and stay with the simplex method. The record shows him adding IPM, parallel and SIMD paths as components and then returning to simplex, crash and sifting devices.
2. **Never delete an old device; re-test it on the new model class.** Sprint (1989) → Clp 2003 → 2026 set partitioning. Volume (1990s) → Clp crash 2005. Idiot (2002) → 2026.
3. **Write-ups are optional; the code and its comments are the record.** The skill should cite code and commits, label talk-only work (Aboca, Idiot) as unpublished, and not invent the papers.
4. **Authorship labels by period**: Scicon codes and OSL rest on others' credit, except the pieces he claims in 2002 (cost modification, "going forwards" checks). Clp, Abc and CoinFactorization are his code. Cbc is shared, and the share is shrinking in 2026.
5. **Late-career role**: a maintainer of last resort ("it is quite likely that I was last person to modify it - so I can modify code if nobody else volunteers", Cgl #63, 2021) and a performance gatekeeper (2026). This is not a research-agenda setter, and the skill should not present him as one after 2012.

---

## Contradictions (kept, not reconciled)

1. **When he left IBM.** team.json says "retired, date unknown, between 2006 and 2010". Print shows him at IBM T. J. Watson in Optima 75 (December 2007; S8). The first non-IBM copyright he used is 2012 (Abc). The first written "now retired" in the repositories is dated 2019-03-06 (S1). Nothing I read supports the 2010 upper bound, and nothing contradicts it either. A copyright line is weak evidence (§0).
2. **What "Aboca" stands for.** His parameter help: "Decide whether to use A Basic Optimization Code (Accelerated?) and whether to try going parallel!" (`ClpParameters.cpp`). His 2023 comment: "A Bit Of Clp Accelerated". The 2012 talk title as cited by Huangfu & Hall: "Aboca: a bit of Clp accelerated" (S1, S3, S24).
3. **Abc: written off and still recommended.** "partially successful … not kept up to date" (2023). "the answer may be as simple as abc" (2026-11-01) (S3).
4. **OSL authorship.** team.json labels OSL as "credit by others or co-authored papers (no code of his visible)", and Bixby credits OSL to "John Forrest and John Tomlin" (S23 p. 113). His own 2002 notes claim specific pieces: "the modification of costs which I put in OSL" and "I overdid that in OSL" (S1). The label holds for visible code. His statements show partial authorship of OSL's simplex.
5. **Idiot: his valuation against others' measurement.** His header says "This class implements a very silly algorithm. It has no merit apart from the fact that it gets an approximate solution to some classes of problems." (`Idiot.hpp`). Galabova & Hall find "the Idiot crash is a major factor" in Clp beating at least one commercial solver on some Mittelmann tests (S25).
6. **Cbc credit.** The README says "Cbc is developed by John Forrest, now retired from IBM Research, and others"; the 2005 Cup says "Author of … the COIN-OR Branch-&-Cut (CBC) solver". The commit record: the import commit is Ladanyi's (2004), he has 1060 of 3101 master commits, and he made 31 commits in 2026 against Santos's 478 (S1, S26).
7. **Founding role.** The 2005 Cup names him the single "Founding Benevolent Dictator of COIN-OR". The 2014 Impact Prize credits nine people for its "creation and widespread adoption" (S26, S27).
8. **Account dates in team.json.** It has "johnjforrest (2002-2020) … jjhforrest (2020-)". The API shows `johnjforrest` created only in 2019, with the 2002–2019 commits mapped onto it by the SVN conversion, and `jjhforrest` created in 2014 and commenting from 2017 (S2, S3).

---

## Gaps

- **Education, degrees and birth year**: not found. MGP has no entry. The author biographies of the 1992 *IBM Systems Journal* papers (IEEE Xplore returned an empty bot-check response) and of the 2006 *Interfaces* paper (pubsonline 403; Denton's site 403) were not reachable. Two WebSearch calls found nothing.
- **c. 1976–1987**: the move from Scicon to IBM, and his roles on Sciconic, Alligator and MPSX/370, are undocumented beyond others' one-line credits. **LAMPS and YKTLP** (named in team.json) were **not verified** in this run; no source I read mentions them.
- **The 2007 history note's full text** (paywalled). The IBM Research Report version (RC22890, dominoweb.draco.res.ibm.com) refused the connection. Tomlin's site thetomlins.org does not resolve. Read: metadata, reference list and an aggregator's abstract only.
- **Talks not read**: Royal Society 1987; ORSA/TIMS 1989 (Sprint); ISMP 2012 (Aboca); the Idiot talk.
- **The exact retirement date and the nature of FasterCoin**: fastercoin.com is a parked domain. list.coin-or.org (mailing-list archives) refused connections. web.archive.org was not used, as instructed.
- **"IBM Burlington problems"**: what the models were is not stated; the link to the semiconductor MIP is my inference.
- **The competition** named in Cbc's first README (2004: "While the competition is on no work is being done on the cbc driver") is not identified.
- **Comments by year**: I counted his comments exactly only for the last 12 months (43). For 2017–2026 I have only issue-level proxies (291 issues and PRs with his comments; by the year each issue was opened: 2017 2, 2018 24, 2019 37, 2020 33, 2021 41, 2022 36, 2023 29, 2024 25, 2025 45, 2026 19). I did not reproduce the task's figure of 461 comments.
- **Beale–Orchard-Hays or other MOS prizes**: the mathopt.org prize pages returned an empty script shell, so not checked.

---

## Sources

Primary (P):
- S1. COIN-OR git histories and sources, read 2026-11-05 through blobless and shallow clones: github.com/coin-or/Clp, Cbc, CoinUtils, Cgl, Osi (also Bonmin, Couenne, CoinMP). Files cited: Clp commit `b42534866981c7939cf699bbc719338c76ceda87` (2002-07-30); `ClpMain.cpp` (version log); `ClpSolve.cpp`; `Idiot.hpp`; `ClpNonLinearCost.hpp`; `AbcSimplex.hpp`; `AbcSimplexDual.cpp`; `AbcSimplexParallel.cpp`; `ClpParameters.cpp`; `ClpPESimplex.hpp`; `examples/ekk.cpp`; `CbcGeneralDepth.cpp`; `CbcLinked.hpp`; Cbc `README.md` and `AUTHORS` with their histories; `CoinOslFactorization.hpp`; `CglProbing.hpp`; `CglZeroHalf.hpp`. P
- S2. GitHub REST API, users `johnjforrest` and `jjhforrest` (profiles), commit search and the repository record of `h-g-s/mipster`, read 2026-11-05. P
- S3. GitHub issue threads (coin-or): Cbc #837, #714, #774, #787, #769, #784, #719, #332, #421, #449, #461, #376, #412, #485, #273; Clp #358, #262, #291, #251, #316; Cgl #63, #45; plus issue search `commenter:jjhforrest` and all issue comments in Cbc, Clp, CoinUtils, Cgl and Osi from 2025-11-05 on, read 2026-11-05. P
- S4. Crossref REST API records for DOIs 10.1007/bf01584548, 10.1287/mnsc.20.5.736, 10.1007/bf01580653, 10.1007/bf02023049, 10.1147/sj.311.0011, 10.1147/sj.311.0026, 10.1007/bf01581089, 10.4171/dms/1-3/65, 10.1007/978-1-4684-9277-4_2, 10.1287/educ.1053.0020, 10.1287/ijoc.1040.0078, 10.1287/inte.1060.0238, 10.1007/s10479-006-0112-x, 10.1147/rd.471.0057, 10.1007/s12532-017-0130-5, read 2026-11-05. P
- S5. DBLP pid 08/3168 via sparql.dblp.org (`scripts/dblp_works.py --pid 08/3168`): 7 records, 1972–2007, read 2026-11-05. P
- S6. Springer article pages (affiliations, abstracts, reference lists) for 10.1007/BF01584548, 10.1007/BF01580653, 10.1007/BF02023049, 10.1007/BF01581089, read 2026-11-05. P
- S7. Anbil, Forrest, Pulleyblank, "Column generation and the airline crew pairing problem", *Doc. Math.* Extra Vol. ICM 1998 III, 677–686, DOI 10.4171/dms/1-3/65 (full text, content.ems.press). P
- S8. Bonami, Forrest, Lee, Wächter, "Rapid Development of an Open-source Minlp Solver with COIN-OR", *Optima* 75, December 2007 (mathopt.zib.de/Optima-Issues/optima75.pdf; full text). P
- S9. Springer page of Forrest & Tomlin, "Branch and bound, integer, and non-integer programming", *Ann. Oper. Res.* 149:81–87, DOI 10.1007/s10479-006-0112-x (metadata and reference list); the reference list of DOI 10.1007/BF02023049 (1987 talk). Full text not read. P
- S10. Forrest & Tomlin, "Implementing the simplex method for the Optimization Subroutine Library", *IBM Syst. J.* 31(1):11–25, 1992, DOI 10.1147/sj.311.0011 (metadata only; IEEE Xplore blocked). P
- S11. Forrest & Tomlin, "Implementing interior point linear programming methods in the Optimization Subroutine Library", *IBM Syst. J.* 31(1):26–38, 1992, DOI 10.1147/sj.311.0026 (metadata only). P
- S12. Forrest & Goldfarb, "Steepest-edge simplex algorithms for linear programming", *Math. Program.* 57:341–374, 1992, DOI 10.1007/BF01581089 (abstract and references). P
- S13. Forrest, Hirst, Tomlin, "Practical Solution of Large Mixed Integer Programming Problems with Umpire", *Management Science* 20(5):736–773, 1974, DOI 10.1287/mnsc.20.5.736 (abstract via Crossref). P
- S14. Forrest & Tomlin, "Updated triangular factors of the basis to maintain sparsity in the product form simplex method", *Math. Program.* 2:263–278, 1972, DOI 10.1007/BF01584548 (abstract). P
- S15. Beale & Forrest, "Global optimization using special ordered sets", *Math. Program.* 10:52–69, 1976, DOI 10.1007/BF01580653 (abstract). P
- S16. Beale & Forrest, "Global Optimization as an Extension of Integer Programming", in Dixon & Szegö (eds.), *Towards Global Optimization 2*, North-Holland, 1978, pp. 131–149 (venue + year + title from S9; not read). P
- S17. Forrest & Tomlin, "Vector processing in simplex and interior methods for linear programming", *Ann. Oper. Res.* 22:71–100, 1990, DOI 10.1007/BF02023049 (abstract and references). P
- S18. Dietrich & Forrest, "A Column Generation Approach for Combinatorial Auctions", IMA Vol. Math. Appl., 2002, pp. 15–26, DOI 10.1007/978-1-4684-9277-4_2 (metadata). P
- S19. Forrest & Lougee-Heimer, "CBC User Guide", INFORMS TutORials 2005, pp. 257–277, DOI 10.1287/educ.1053.0020 (metadata; web version S32). P
- S20. Forrest, Kalagnanam, Ladányi, "A Column-Generation Approach to the Multiple Knapsack Problem with Color Constraints", *INFORMS J. Comput.* 18(1):129–134, 2006, DOI 10.1287/ijoc.1040.0078 (abstract). P
- S21. Denton, Forrest, Milne, "IBM Solves a Mixed-Integer Program to Optimize Its Semiconductor Supply Chain", *Interfaces* 36(5):386–399, 2006, DOI 10.1287/inte.1060.0238 (abstract). P
- S22. Clp `README.md` history: initial version by Stefan Vigerske, 2019-03-06 ("now retired" sentence), removed 2020-07-15 (in S1). P (project document, written by others)

Secondary (S):
- S23. R. E. Bixby, "A Brief History of Linear and Mixed-Integer Programming Computation", *Doc. Math.* Extra Vol. ISMP 2012, 107–121 (full text, maths.tcd.ie/EMIS mirror), pp. 109–113. S
- S24. Q. Huangfu & J. A. J. Hall, "Parallelizing the dual revised simplex method", *Math. Program. Comput.* 10(1):119–142, 2018, DOI 10.1007/s12532-017-0130-5 (author-hosted PDF, webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf). S
- S25. I. L. Galabova & J. A. J. Hall, "A quadratic penalty algorithm for linear programming and its application to linearizations of quadratic assignment problems", arXiv 1804.09172 (v1, 2018-04-24). S
- S26. COIN-OR, "COIN-OR Cup 2005 Winners: John J. H. Forrest", www.coin-or.org/coinCup/coinCup2005Winner.html (read 2026-11-05). S
- S27. INFORMS, award-recipient page "John Forrest" (1995 ICS Prize, 2005 Wagner Prize, 2007 Fellow, 2014 Impact Prize citation), www.informs.org/Recognizing-Excellence/Award-Recipients/John-Forrest. S
- S28. INFORMS Computing Society Prize winner lists: www.informs.org/Recognizing-Excellence/Community-Prizes/INFORMS-Computing-Society/INFORMS-Computing-Society-Prize and connect.informs.org/computing/awards/ics-prize. S
- S29. INFORMS, award-recipient page "R. John Milne" (2005 Wagner Prize winning material). S
- S30. COIN-OR Foundation pages: about-the-foundation, former-board-and-council-members, coincup (www.coin-or.org). S
- S31. COIN-OR, CLP User's Guide pages: www.coin-or.org/Clp/ (authors list, 2004), /Clp/faq (entries signed "DN", 2004), /Clp/revhist. S
- S32. COIN-OR, CBC User's Guide pages: www.coin-or.org/Cbc/, /Cbc/intro, /Cbc/revhist. S
- S33. INFORMS, "Brief Biography: John Tomlin" (History of O.R. Excellence). S
- S34. Optimization-Researchers repo sibling notes `01-publications.md` and `03-process-evidence.md` (2026-11-05), used as leads only. S
- S35. Wikipedia, "Martin Beale" (raw wikitext, read 2026-11-05). S
- S36. Mathematics Genealogy Project, quick search "Forrest" (mathgenealogy.org, 2026-11-05, site partly back online since 4 Nov 2026). S
- S37. WebSearch result listings (4 calls), used only to find S27, S29, S33 and S38. S
- S38. Sciweavers record of Forrest & Tomlin (2007), with the abstract (www.sciweavers.org/node/243664). S
- S39. OpenAlex author A5061258306 summary (`../sources/publications/publications.md`, `abstracts.md`, harvested 2026-11-05). S

Not reached (recorded, not routed around): list.coin-or.org; web.archive.org; fastercoin.com (redirects to a domain-sale page, checked 2026-11-05); dominoweb.draco.res.ibm.com (RC22890, connection refused); thetomlins.org (non-existent domain); IEEE Xplore (empty bot-check response); pubsonline.informs.org and btdenton.engin.umich.edu (403); mathopt.org prize pages (script shell only).
