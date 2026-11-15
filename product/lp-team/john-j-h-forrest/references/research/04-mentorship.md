# 04 · Students and collaborators: how Forrest worked with others, and what his collaborators know

- **Researcher:** John J. H. Forrest (also J. J. H. Forrest, John J. Forrest, John Forrest). Simplex-code author (Clp, Abc, CoinFactorization); a developer of Cbc, shared with others; Scicon Ltd in the 1970s; IBM Research later (retired, date not established here); founding "Benevolent Dictator" of COIN-OR. Code-first lens.
- **Dimension:** research agent 04 of 06: students and collaborators. Covers supervision style, group habits, project culture and tacit knowledge.
- **Research date:** 2026-11-05.
- **Sources consulted:** 110, listed one per line under "Sources".
  - 91 primary: his own words, co-authored texts, code and project records. Of these, 77 were read, in full or in part. The other 14 are co-authored works and bibliographic lists checked for metadata only.
  - 19 secondary. Of these, 15 were read, in full or in part, and 4 were checked for metadata only.
  - Not counted: 5 more sources could not be reached (see Gaps).
- **Tools:**
  - WebSearch: 6 calls of the 7 allowed. 3 of them found nothing usable.
  - Everything else came from curl and WebFetch on known URLs:
    - GitHub issue and PR pages (HTML) and 1 call to the GitHub REST API;
    - blobless git clones of Clp, Cbc, CoinUtils and Cgl;
    - Crossref, Unpaywall, OpenAlex and Semantic Scholar;
    - the Edinburgh Research Archive's DSpace API.
- **User-supplied material:** none. `references/sources/papers`, `talks`, `essays` and `software` hold only `.gitkeep`. `publications/` holds the generated OpenAlex summary, which is not user-supplied material. `private/` was not opened.
- **Identity caveat:** every issue comment quoted here was posted by the GitHub account `jjhforrest`.
  - The link between that account and John J. H. Forrest rests on strong inference, not on any document: the same display name, comments signed "John Forrest" or "JJHF", and the hand-over of the commit identity on 2020-05-11/12.
  - In git history the author names "John Forrest" and "jjhforrest" are both counted as his, with the same caveat.
  - 03-process-evidence.md has the full identity analysis. It also reconciles the comment count: 461 in the brief, 486 found by agent 03 across all repositories.

**What kind of evidence this is.** Forrest worked in industry, at Scicon and IBM Research, and then as an open-source maintainer. I found none of the following: a doctoral student, a lab or group page, a lab guide, a student memoir, a Festschrift, an interview or an oral history. Six WebSearch calls aimed at thesis acknowledgements, COIN-OR history, the Scicon period and "personal communication" citations found nothing about him as a supervisor.

So "mentorship" in this file means what he did in place of supervising:
- how code written by others entered the projects he owned;
- how he worked with co-maintainers;
- how he taught the users and researchers who came to him with questions.

The evidence comes from three places:
1. **Project records:** git history, AUTHORS files, READMEs and `config.yml` files, the 2004–2006 FAQs, and the CLP and CBC User's Guides.
2. **His own interaction record on GitHub.** I read 47 threads holding 90 of his comments. They were chosen, not sampled at random, for teaching, contributor and co-maintainer content. The pool was a cached index of the 291 issues and PRs in which `jjhforrest` commented (plus 1 for `johnjforrest`).
3. **What others wrote about him:** award citations, slides, a PhD thesis, a dissertation, a journal paper and a project FAQ.

**Tags.**
- **[stated]**: his own words. This includes code comments, commit messages, help text, his issue comments and FAQ entries initialled "JF".
- **[stated-joint]**: a text he co-authored.
- **[practice]**: what the code, the history or the threads show he did.
- **[observed]**: what others wrote about him.
- **[inferred]**: my reading; no source states it.
- **P / S**: primary / secondary. A student or colleague writing first-hand about him is still secondary evidence about Forrest.

**Quoting.**
- Quotations are verbatim and short.
- Longer passages are paraphrased, and a paraphrase is never put in quotation marks.
- Issue comments are cited as `repo#number (date)`. The URLs are in Sources.
- E-mail replies were stripped of their quoted text before reading.

---

## A. Who: students, co-authors, code collaborators

### A.1 Students: none found

- [practice] P. **Every paper is co-authored, and no co-author is identified anywhere as his student.**
  - DBLP (pid 08/3168) lists 7 records, 1972–2007.
  - OpenAlex (A5061258306) lists 13 works, 1972–2007.
- [inferred] **The "student signal" in `publications/publications.md` is a false positive.** That generated table flags two "other first author × Forrest last author" papers: Beale & Forrest 1976 and Dietrich & Forrest 2002. Neither is a student pairing:
  - Beale was the senior figure of the Scicon mathematical-programming group (§B.1).
  - Dietrich was an IBM colleague and a co-recipient of the 2014 INFORMS Impact Prize (§A.2).
- **Not checked:** the Mathematics Genealogy Project. Its search form, posted by curl, returned a results page with no rows.
- **Not established:** his own doctoral training.
- **The two nearest things to a junior collaborator.** Neither person's student or intern status is stated in any source.
  - **David de la Nuez.** The 2004 CLP User's Guide lists him with the affiliation "Columbia University & IBM Research", next to Forrest and Robin Lougee-Heimer. [stated-joint] P.
    - The git account `ddelanu` made 14 Clp commits, 2004-08-12 to 2004-10-17, all of them documentation: a DocBook user guide and the FAQ. [practice] P
    - One message shows how the work was split. The junior wrote the guide and Forrest supplied the example: "Edited a bunch of stuff, including presolve example (new one from JF in place)" (Clp `247b242`, 2004-09-01). [practice] P
    - The Clp FAQ answers are initialled "DN". [inferred] DN is de la Nuez: the initials match, and `ddelanu` committed the FAQ ("Added FAQ in clever manner", Clp `5b3ae5e`, 2004-09-01).
  - **Mahdi Namazifar.** Semantic Scholar (CorpusId 7320007) lists a 2009 report with no venue and no DOI: "Pivot-and-Fix; A Mixed Integer Programming Primal Heuristic", by Namazifar, R. Lougee-Heimer and J. J. H. Forrest.
    - The matching Cbc heuristics were set up by Forrest ("allow pivot and fix or randomized rounding", Cbc `c96c0ac`, 2008-09-05). Robin Lougee wrote the body ("adding the guts of the randomized rounding heuristic", Cbc `ca31fcd`, 2008-09-11). [practice] P
    - 01-publications.md lists a second report (CorpusId 15776028). Semantic Scholar refused that query in this run (HTTP 429), so it is not re-verified here.
    - Namazifar's affiliation and status are not established.

### A.2 Co-authors

Every identifier below was checked against Crossref in this run, except Optima 75, which has no DOI; its venue, year and title were checked on the PDF. The last column says how much I read.

| Year | Work (venue) | Co-authors | Identifier | Read |
|---|---|---|---|---|
| 1972 | Updated triangular factors of the basis to maintain sparsity in the product form simplex method (*Math. Programming* 2(1):263–278) | J. A. Tomlin | DOI 10.1007/BF01584548 | metadata |
| 1974 | Practical Solution of Large Mixed Integer Programming Problems with Umpire (*Management Science* 20(5):736–773) | J. P. H. Hirst, J. A. Tomlin | DOI 10.1287/mnsc.20.5.736 | abstract |
| 1976 | Global optimization using special ordered sets (*Math. Programming* 10(1):52–69) | E. M. L. Beale (first author) | DOI 10.1007/BF01580653 | metadata |
| 1990 | Vector processing in simplex and interior methods for linear programming (*Annals of OR* 22:71–100) | J. A. Tomlin | DOI 10.1007/BF02023049 | metadata |
| 1992 | Implementing the simplex method for the Optimization Subroutine Library (*IBM Systems Journal* 31(1):11–25) | J. A. Tomlin | DOI 10.1147/sj.311.0011 | abstract |
| 1992 | Implementing interior point linear programming methods in the Optimization Subroutine Library (*IBM Systems Journal* 31(1):26–38) | J. A. Tomlin | DOI 10.1147/sj.311.0026 | metadata |
| 1992 | Steepest-edge simplex algorithms for linear programming (*Math. Programming* 57:341–374) | D. Goldfarb | DOI 10.1007/BF01581089 | metadata |
| 1998 | Column generation and the airline crew pairing problem (*Documenta Math.*, Extra Vol. ICM 1998, III, 677–686) | R. Anbil, W. R. Pulleyblank | DOI 10.4171/dms/1-3/65 | full text |
| 2002 | A Column Generation Approach for Combinatorial Auctions (*IMA Volumes in Math. and its Applications*, pp. 15–26) | B. Dietrich (first author) | DOI 10.1007/978-1-4684-9277-4_2 | metadata |
| 2005 | CBC User Guide (INFORMS TutORials 2005, pp. 257–277) | R. Lougee-Heimer | DOI 10.1287/educ.1053.0020 | not read (closed); the web CBC User's Guide by the same two authors was read in part |
| 2006 | A Column-Generation Approach to the Multiple Knapsack Problem with Color Constraints (*INFORMS J. Comput.* 18(1):129–134) | J. Kalagnanam, L. Ladanyi | DOI 10.1287/ijoc.1040.0078 | abstract |
| 2006 | IBM Solves a Mixed-Integer Program to Optimize Its Semiconductor Supply Chain (*Interfaces* 36(5):386–399) | B. T. Denton, R. J. Milne | DOI 10.1287/inte.1060.0238 | abstract |
| 2007 (online 2006) | Branch and bound, integer, and non-integer programming (*Annals of OR* 149(1):81–87); a reminiscence | J. A. Tomlin | DOI 10.1007/s10479-006-0112-x | not read (closed) |
| 2007 | Rapid Development of an Open-source Minlp Solver with COIN-OR (*Optima* 75, December 2007, pp. 1–4) | P. Bonami, J. Lee, A. Wächter | no DOI; venue, year and title checked on the PDF | read |

What the table shows:
- [practice] P. **Tomlin is the constant partner:** 6 of the 13 OpenAlex works, from Scicon (1972, 1974) through IBM (1990, 1992 ×2) to the 2007 reminiscence.
- [observed] S. **One academic pairing was recognised jointly.** The INFORMS Computing Society Prize page lists the 1995 First Place as John Forrest (IBM) and Donald Goldfarb (Columbia University). The citation text was not read.
- [observed] S. **Other honours** (INFORMS award-recipient page for him):
  - 2005 Daniel H. Wagner Prize, for "A Mixed Integer Program for Semiconductor Supply-Chain Optimization at IBM";
  - 2007 INFORMS Fellow;
  - 2014 INFORMS Impact Prize, shared by nine people: Brenda Dietrich, JP Fasano, John Forrest, Lou Hafer, Brady Hunsaker, Laszlo Ladanyi, Robin Lougee, Theodore K. Ralphs and Matthew Saltzman. The citation names them "for their pivotal role in the creation and widespread adoption of COIN-OR".

### A.3 Code collaborators (COIN-OR)

**Commit counts by author name**, whole history to 2026-11-05 [practice] P. Both "John Forrest" and "jjhforrest" are counted as his. Variants of one person's name are merged.

| Repo (commits) | Forrest | Others with the most commits |
|---|---|---|
| Clp (2,267) | 1,303 | Vigerske 321, Ralphs 225, H. G. Santos 110, Hafer 86, Wächter 78, Fasano 35, Ladanyi 34, Goossens 25, de la Nuez (`ddelanu`) 14 |
| Cbc (3,101 on master) | 1,060 | H. G. Santos 807, Ralphs 447, Vigerske 325, Hafer 106, Wächter 88, Kristjansson 54, Goossens 34, Fasano 32, Strayer 27, Ladanyi 25, Lubin 20, S. S. Brito 18, Lougee 10, Fylstra 9, Goncalves 7 |
| CoinUtils (1,906) | 533 | Vigerske 350, Ralphs 280, Ladanyi 184, Hafer 176, H. G. Santos 131, Wächter 81, Fasano 51, Tomlin 5 |
| Cgl (1,249) | 434 | Vigerske 166, Ralphs 126, H. G. Santos 110, Margot 92, Wächter 76, Hafer 59, Lougee 35, Ladanyi 28, Bonami 26, Fasano 23, Xu 10, Günlük 4 |

[inferred] **The counts fall into eras:**
- **The 2002–2009 group around him:**
  - Ladanyi (an IBM address in CoinUtils' `config.yml`);
  - Lougee (IBM Research, per the user guides);
  - de la Nuez ("Columbia University & IBM Research");
  - Fasano and Goncalves (affiliations not checked).
- **Build-system people and outside contributors:**
  - Wächter's 2006 autotools work: 73 Cbc and 65 Clp commits in 2006. Cbc's `Makefile.am` files still carry the header "Author: Andreas Waechter IBM 2006-04-13".
  - A 2009 burst from outside the IBM group: Kristjansson (50 Cbc commits that year), Strayer (27) and Fylstra (9). Their affiliations were not checked in this run.
- **Long-term co-maintainers:** Hafer (from 2006), Ralphs (from 2006), Vigerske (from 2009), H. G. Santos (from 2013).
- **The GitHub era:** Goossens (from 2020) and outside contributors.

**AUTHORS files** [practice] P:
- **Cgl.** Each cut generator has its own contributors and a "PM" (project manager).
  - Forrest is "contributor & PM" for CglAllDifferent, CglCutGenerator, CglDuplicateRow, Gomory, CglMessage, MixedIntegerRounding2, OddHole, PreProcess, Probing and CglStored.
  - He is "PM" alone where someone else wrote the code: CglGMI and CglRedSplit2 (contributor Giacomo Nannicini) and CglZeroHalf (contributor Alberto Caprara).
  - Others are PM of their own generators:
    - Ladanyi: Clique;
    - Yan Xu: FlowCover, with contributors Linderoth and Savelsbergh;
    - Robin Lougee: KnapsackCover, LiftAndProject, SimpleRounding;
    - Bonami: LandP;
    - Goncalves: MixedIntegerRounding;
    - Margot: RedSplit;
    - Barahona: ResidualCapacity;
    - Günlük: Twomir, with Dash and Goycoolea.
  - The Cgl README says "Each cut generator is in a separate directory with its own maintainer". It names Robin Lougee and François Margot as the project managers of Cgl as a whole.
- **Cbc AUTHORS** (updated Feb 10, 2020): Forrest; Hafer; Goncalves ("Diving heuristics"); H. G. Santos ("MIPStart, Conflict Graphs related code"); S. S. Brito ("Conflict Graphs related code").
- **Osi AUTHORS** (05/24/2007): Fasano, Forrest, Hafer, Ladanyi, Lannez, Margot, Saltzman, Ralphs, Walton.
- **Clp AUTHORS** at tag `releases/1.17.0` (2019) holds one line: "Forrest, John J.". At master there is no AUTHORS file (HTTP 404).

**Credit lines inside the code** [stated] P, at HEAD:

| Where | Credit line |
|---|---|
| Clp `ClpCholeskyBase.cpp` | "Ordering code - courtesy of Anshul Gupta" |
| Clp `ClpPdco.cpp` / `ClpPdco.hpp` | "AUTHOR: … Michael Saunders"; "John Tomlin" |
| Clp `ClpPE*` (Positive Edge) | headers "Jeremy Omer, Mehdi Towhidi"; help text "Code donated by Jeremy Omer", pointing users to Towhidi, Desrosiers and Soumis (*Comput. Oper. Res.* 49:41–46, 2014, DOI 10.1016/j.cor.2014.03.020) and Omer, Towhidi and Soumis (*Comput. Oper. Res.* 61:135–142, 2015, DOI 10.1016/j.cor.2015.03.009) |
| Cbc help (zero-half cuts) | "This implementation was written by Alberto Caprara." |
| Cbc `CbcSymmetry.cpp` | "hacked from CouenneSymmetry.cpp" … "Author: Jim Ostrowski (the good bits - rest JJHF)". Added to Cbc by Forrest on 2014-07-16 (`72cfa4f`, "oops forgot to add files") |
| Cbc `CbcSymmetry.hpp` | "Author: Pietro Belotti, Lehigh University" |
| Cbc `Cbc_C_Interface.h` | "Original version contributed by Bob Entriken" |
| Cbc `CbcHeuristicPivotAndFix.cpp`, `CbcHeuristicRandRound.cpp` (Lougee's code) | "Todo: Ask JJHF what this for." and "Todo: Ask JJHF what "number of times …" |

### A.4 Who took over what

- **Clp: Julian Hall.**
  - [observed] S. Hall and Huangfu's PPAM talk of 13 September 2011 (PDF p. 34) describes Clp as "Written by John Forrest (IBM)" and "Best open-source simplex solver", and adds "H is now project manager".
  - [observed] S. The COIN-OR Annual Report 2011 lists "Clp, COIN-OR LP, a linear program solver. (Julian Hall)".
  - [practice] P. Clp's `.coin-or/config.yml` today: "Manager: Julian Hall".
  - [practice] P. **He was still Clp's largest committer long after the hand-over.** In every year from 2021 to 2025 he made more commits than everyone else combined (2025: 23 against 5). In 2026 the balance flipped: 15 against 110, 82 of them by H. G. Santos. In earlier years the balance went both ways (2012, 2014, 2015 and 2017 in his favour; 2011, 2013, 2016 and 2018–2020 not).
- **Cbc: Ted Ralphs.**
  - [observed] S. The 2011 report lists Cbc "(Ted Ralphs)".
  - [practice] P. Cbc's `config.yml` says "Manager: Ted Ralphs". The Cbc README says the project "is currently managed by John Forrest, Ted Ralphs, Stefan Vigerske, Haroldo Gambini Santos, and the rest of the Cbc team". See Contradiction H1.
- **CoinUtils: Laszlo Ladanyi** (2011 report; `config.yml`).
- **Lead, unverified.** A search result titled "[Clp] Stepping down as Project Manager for Cbc and Clp" points to list.coin-or.org (pipermail clp, February 2010, message 001068). The list server timed out on 2026-11-05, so the post was not read.

---

## B. Layer 7: how he organised work with others

### B.1 The model he came from: Scicon, Beale and Tomlin

- [stated] P. **In 2020 he passed the Scicon lineage on to a user.** A user had dug into Cbc's code and asked why `OsiSolverLink` exists (Cbc#297, 2020-04-14). Forrest explained it through Beale: "Linked Ordered Sets were developed by Martin Beale in the late 1970's". He credited special ordered sets to "Beale & Tomlin". He then pointed to two example programs, which he called "more than ten years old".
- [observed] S. **Bixby places him in Beale's line.** In *Documenta Math.* Extra Volume ISMP 2012, p. 109, Bixby lists R. E. Small and Max Shaw among "those who worked with Beale and were influenced by his vision of mathematical programming", "followed by John Tomlin and John Forrest". On p. 113 he describes OSL as "developed primarily by John Forrest and John Tomlin".
- [observed] S. **The systems he worked on** (COIN-OR Cup 2005 citation): "a developer of Alligator, Umpire, Sciconic, MPSX370, OSL".
- [practice] P. **His Scicon-era papers:** UMPIRE with Hirst and Tomlin (1974); the FT update with Tomlin (1972); special ordered sets with Beale as first author (1976).
- [observed] S, **about Beale, not Forrest.** The OR Society's Beale biography is taken from M. J. D. Powell's Royal Society memoir (DOI 10.1098/rsbm.1987.0002). It says:
  - Beale stayed at CEIR/Scicon as its scientific adviser;
  - he is best remembered for "mathematical programming systems for applying optimisation algorithms painlessly in practice";
  - "he believed in open publication of useful discoveries".
- [observed] S, **about Tomlin.** The INFORMS profile says that, as a senior analyst at Scicon, Tomlin "created the Forrest-Tomlin method" (see Contradiction H5). It then traces him to Stanford's Systems Optimization Laboratory (1972), NASA Ames (1977), Ketron (most of the 1980s), IBM Research (until 2005) and Yahoo!.
- [inferred, weak] **What may carry over.**
  - The pattern is a consultancy group that built mathematical-programming systems for client models, with implementers who published jointly with the senior figure.
  - His later habits match it:
    - client problems driving code (§B.8);
    - joint papers only;
    - credit lines for every contributor (§B.3).
  - No source I could read says that Beale shaped these habits. The two sources that might are closed and were not read:
    - the Forrest–Tomlin reminiscence (*Annals of OR* 149, 2007);
    - Tomlin's chapter on Beale in *Profiles in Operations Research* (2011, DOI 10.1007/978-1-4419-6281-2_37). Only its abstract and reference list were read. The list cites Beale & Forrest 1976 and Forrest & Tomlin 2007.

### B.2 Founding and running COIN-OR: the "Benevolent Dictator"

- [observed] S. **The COIN-OR Cup 2005 citation names him "Founding Benevolent Dictator of COIN-OR".** It also credits him with:
  - authorship of CLP, CBC and components of CGL, "including active maintenance and continued development";
  - design contributions to the original suite (OSI and CGL);
  - his ability to "close the loop". Paraphrased: hard real-world problems drive tools of wide use, while the tools stay timely enough to matter for the original problems.
- [observed] S. **The INFORMS 2014 Impact Prize citation** says COIN-OR was launched at ISMP 2000 as a three-year experiment by IBM Research and became a non-profit foundation in 2004. It names nine people (§A.2).
- [stated-joint] P. **CBC User's Guide, introduction:** "CBC is an active open-source project led by John Forrest".
- [stated-joint] P. **Optima 75 (December 2007) tells the Bonmin story.**
  - An IBM–Carnegie Mellon joint study on MINLP began in 2004 and was extended in 2006 under IBM's Open Collaborative Research programme.
  - The solver was built quickly by reusing Cbc, Clp and Ipopt.
  - The acknowledgements thank nine CMU/IBM participants: Belotti, Biegler, Conn, Cornuéjols, Grossmann, Laird, Lodi, Margot and Sawaya.
- [stated] P. **Users as the drivers of development.** Cbc FAQ (JF 04/01/05): some ten people who do not always post to the mailing list are constantly "improving" the code by demanding performance, bug fixes or enhancements. The quoted word, with its scare quotes, is his.
- **Leads, unverified.** A search-engine summary (not the page) says:
  - in a 2010 Clp-list post he recalled announcing COIN-OR at ISMP 2000 "as Benevolent Dictator";
  - in a 2012 post he joked that the role amounts to doing nothing.

  list.coin-or.org was not reachable, so neither post was read. Do not quote them.

### B.3 The integrator: donated code enters through him, with credit (SVN era, 2002–2019)

- [practice] P. **He committed other people's code himself and named the source in the message.**

| Repo | Commit | Date | Message | Whose work |
|---|---|---|---|---|
| Cbc | `8fb0c2a` | 2008-02-13 | "adding diving heuristics from Joao" | Joao Goncalves |
| Clp | `8ea97a0` | 2009-05-30 | "changes for cholesky including code from Anshul Gupta" | Anshul Gupta |
| Cbc | `88147dd` | 2012-03-26 | "New mipstart provided by Haroldo Santos" | Haroldo Santos |
| Cgl | `18d1a34` | 2013-01-10 | "add first try at zero half cuts" | Caprara's implementation (AUTHORS; help text) |
| Cgl | `ec19755` | 2013-03-19 | "add two cuts and fix a few accuracy issues" | GMI and RedSplit2, contributor Nannicini (AUTHORS) |
| Clp | `fa95787` | 2015-06-25 | "add PE code" | Jeremy Omer: "Code donated by Jeremy Omer" (help text) |

- [practice] P. **He also credited the people who found bugs:**

| Repo | Commit | Date | Message |
|---|---|---|---|
| Clp | `a394453` | 2005-06-29 | "thanks to Francois" |
| Cgl | `3599d09` | 2005-01-11 | "fix bug found by gams client" |
| CoinUtils | `54e1ce4` | 2006-02-09 | "bug found by John Tomlin" |
| Clp | `d1ddc42` | 2010-08-11 | "changes to help SCIP" |

- [practice] P. **Scaffold first, then let a colleague fill it.**
  - The pivot-and-fix and randomized-rounding heuristics began as his stubs (Cbc `c96c0ac`, 2008-09-05). Robin Lougee wrote the bodies (`ca31fcd`, 2008-09-11).
  - Her code keeps two "Ask JJHF" to-dos (§A.3). [inferred] The person who knew what a field was for was a person, not a document.
- [inferred] **The working rule these records show:**
  1. A contributor writes a component in their own area: cuts, heuristics, pricing or orderings.
  2. Forrest brings it in and takes on the "PM" bookkeeping for it.
  3. The credit stays where users see it: AUTHORS, file headers and the help text, together with the contributor's paper.

  Exclusivity is modest: many projects credit their contributors. The per-generator "PM" bookkeeping and the credit inside the user-facing help text are the distinctive part.

### B.4 From contributor to co-maintainer

- [practice] P. **Haroldo G. Santos** is the clearest path. The record (git history; AUTHORS; README; arXiv 1909.07780):

| Year | Step | Evidence |
|---|---|---|
| 2012 | First code reaches Cbc through Forrest's commit (mipstart) | Cbc `88147dd` |
| 2013 | First own commit in Cbc (2013-06-05) | git history |
| 2019–2022 | Conflict-graph work with Samuel S. Brito, published as Brito & Santos, *Comput. Oper. Res.* 128:105176, 2021 (DOI 10.1016/j.cor.2020.105176; arXiv 1909.07780). The acknowledgements of the arXiv v3 do not mention Forrest | arXiv full text |
| 2019 | Largest Cbc committer of the year (134 commits, against Forrest's 30) | git history |
| 2020 | AUTHORS credits him with "MIPStart, Conflict Graphs related code" | Cbc AUTHORS |
| 2026 | 493 of the 588 Cbc commits since 2026-01-01, across all branches (Forrest: 34). These are raw counts over all branches; 03-process-evidence.md counts 477 distinct Santos commits | git history |
| now | Co-manager in the README | Cbc README |

- [practice] P. **Stefan Vigerske.**
  - First Cbc commit 2009-09-13.
  - [inferred] He moved the old Trac tickets to GitHub. In the index, Clp #23–#86 and Cbc #89–#205 were opened by `svigerske` on 2019-03-02/03 and carry old content (e.g. "CBC 2.6.0 crashing").
  - He cherry-picks Forrest's fixes to the stable branches (Cbc#504, Cbc#774).
- [practice] P. **Ted Ralphs.**
  - Cbc manager (`config.yml`; the 2011 report).
  - Opened the Cbc refactoring PR (Cbc#374, 2021) and merged "next" into master on 2026-10-22 (Cbc `955a23f`).
- [inferred] **No succession plan is documented.** Succession shows up as role labels moving (Clp to Hall and Cbc to Ralphs, by 2011), while he stayed a leading Clp committer through 2025.

### B.5 Working with co-maintainers on GitHub (2019–2026)

- **A pragmatic patch against a root-cause fix** (CoinUtils#206, 2023-03-31 to 04-03) [practice] P; [observed] S.
  - Ralphs reported an MPS file that failed to read. Forrest proposed a workaround: "Odd - but easy to get round".
  - Ralphs argued that the flag could not be trusted and asked for the root cause.
  - Forrest replied "That won't work", added "feel free to run it through a debugger", and then posted a gdb breakpoint dump showing the buffer state.
  - Ralphs: "Anyway, you know better than me, feel free to commit."
  - Forrest: "I will commit just to master for now." Ralphs then tested it and cherry-picked it to stable/2.11 himself.
- **Waiting for the general solution against merging the specific one** (Cbc#656, 2024-07-02 to 08-13) [practice] P.
  - A contributor offered a C-interface function. Forrest first asked "Does it help you go faster?", then "Why not do Osi as well".
  - He proposed to "Wait to see if anyone wants to do this from Osi C interface. If so, I can help."
  - Six weeks later Ralphs: "This looks reasonable to add just as it is."
  - Forrest then made the change in Cbc_C and in Osi himself. The contributor: "Thanks for making the change!"
- **Declining work far from his code** (CoinUtils#233, 2024-07-31) [stated] P.
  - Asked about moving to C++ streams, he said it "would be a lot of work - mostly on code I have little connection to".
  - If it were done, he wanted it done through CoinMessageHandler. The contributor agreed.
- **Low-ceremony approvals** [practice] P:
  - "Looks fine - can't do any harm" (Cbc#504, 2022);
  - "Looks fine to me" (CoinUtils#191, 2022, Hafer's PR);
  - "The change is correct" (Cbc#570, 2023);
  - "Deleted" (Cbc#362, 2021);
  - "Fine by me" (Cbc#622, 2024-08-16, about ten and a half months after the PR was opened).
- **Explaining design history to co-maintainers, and asking before committing** (Cbc#374, May 2021) [stated] P.
  - By e-mail reply he told Vigerske why a second solve changes the answer: branch and bound runs on a copy, and the model passed in is "drastically altered".
  - He then offered: "If you think it worthwhile, I can commit the code which recomputes objective value. Do you want me to?"
- **Measuring before arguing** (Cbc#774, 2026) [practice] P.
  - On Vigerske's time-limit PR he posted `time` tables (real/user/sys) for his MIPLIB unit-test run, comparing the current code with a copy stripped of the "micro management" of the time limit. They showed what frequent clock checks cost in system time: with a time limit set, from 1.2 s to 5.3 s across the configurations he tried.
  - Vigerske's reply was a joke about checking your watch.
- **The 2026 "next" branch.**
  - [practice] P. Cbc had 588 commits since 2026-01-01 across all branches. 68 of them carry a "Co-authored-by: Claude" trailer: 37 by Ralphs, 31 by H. G. Santos. None of Forrest's do. 03-process-evidence.md reports 79 messages containing the word "Claude"; the two measures differ.
  - [practice] P. The same trailer appears in Clp (26 of 152 commits), CoinUtils (19 of 105) and Cgl (30 of 131).
  - [stated] P. His comments that October:
    - Cbc#809 (2026-10-17): "I am worried about the speed with which all the changes are happening." He asked that someone decide whether "next" is really the next master, and asked "Are we getting much feedback from users (apart from claude)?". In the same comment: "I cant see any harm in making the changes."
    - Cbc#807 (2026-10-20): "Fine - I don't mind clunky." What he did mind was "not knowing whether to look at master or next" and "the enormous number of changes in next". His debug output had changed and become confusing.
  - [practice] P. Ralphs merged next into master on 2026-10-22 (`955a23f`).
  - [stated] P. Clp#358 (2026-10-23): the main thing is "to get next moved to master". He deferred a design question until he was "more in the mood (i.e. not having a pleasant evening with my family)".
  - [inferred] **He objected to the volume and to the branch ambiguity, not to the individual changes.** His way of reviewing:
    1. read the diff;
    2. compare the debug output with what he knows;
    3. run his MIPLIB unit test.

    That method does not scale to hundreds of commits a month.

### B.6 Outside contributors' PRs: approve the small ones, rewrite the large ones

- **Cbc#787** (2026-08-08 to 10-05) [practice] P.
  - A contributor submitted a root-cause analysis and, when Goossens asked for one, a regression test.
  - Santos said he was reviewing it. The contributor sent three "Friendly ping"s.
  - Forrest then fixed the bug his own way: "Does that fix in CbcSolver.cpp work for you?"
  - The contributor verified the fix and closed the PR: "The remaining changes in this PR are redundant now".
  - Forrest, on the maximization case: "My mistake - I thought that was not too important."
- **Cbc#748** (2025) [practice] P.
  - He reshaped a contributed parameter so that it would be "more like other string parameters", and renamed it.
  - His commit (Cbc `c9a14f0`, "add precisionoutput parameter") did not compile. Vigerske fixed it in the next commit (`9b91e2c`). Forrest: "I am an idiot. Put in tiny change at end before commit."
- **Cbc#656** (2024): he made the change himself (§B.5).
- **Invitations he then carried out himself** [practice] P:
  - "unless someone else wants to get involved with C interface" (Cbc#618, 2023);
  - "Feel free to suggest more CbcEventHandler events to be activated on -DCOIN_MORE_INFORMATION." (Cbc#327, 2020).
- [observed] S. **A colleague's account from about 2005–06.** In the "Lessons from the Trenches" section of the Cbc FAQ (unsigned), the author reports that a `-csv` option does not combine with `-miplib` "according to John", that "John sugggests [sic] creating a CbcCsv class", and adds "<hint, hint>" for would-be contributors.
- [inferred] **He treats an outside PR as a bug report with a proposed patch; the code that lands is usually his own version.**
  - The cost: contributors' PRs are closed unmerged (Cbc#787), after weeks of pings.
  - The gain: the code stays consistent with conventions only he holds in full (parameter naming, option handling).

### B.7 A peer to other projects: how he reports bugs upstream

- **PaPILO, the presolve library of the SCIP project, September 2024** (scipopt/papilo#59 and #62) [practice] P; [observed] S.
  - He reported a near-endless loop: the run was killed after more than a day. He gave a gdb stack and the variable values.
  - He suggested a stopgap but wrote: "I don't know enough about the code to really fix it."
  - He tested the maintainers' patch and reported a name mismatch in it; the maintainer had renamed the function on purpose. He also flagged a suspicious assert. The maintainer judged the constructor holding that assert unnecessary, and both issues were resolved in PaPILO commit `d942d4e`.
  - His second report began "Apologies for thinking there is another bug when variables have large upper bounds." He had reduced the instance and isolated one bound change that flips the answer.
  - The maintainer said that running PaPILO in rational mode had pinpointed the error, and added: "we appreciate your work to reduce the instance size".
  - The same day as that second report, he committed optional PaPILO support to Cbc and Cgl (Cbc `729e751`, Cgl `2725b26`, 2024-09-10). The message reads: "Not much work has been done recently in Coin on pre-processing for integer problems and this does well on some problems."
- **SHOT#159** (2022). For a Cbc crash that Vigerske found through SHOT, he proposed a one-argument change. Vigerske confirmed that it helped, and Forrest committed it (Cbc `07f2287`, 2022-07-09). [practice] P
- **Bonmin#31** (2023). He fixed the Cbc lazy-constraint bookkeeping behind a Bonmin B-Ecp failure (Cbc `11e6a79`, 2023-01-25, "fix? for lazy constraints"). A returning Bonmin developer (account `pobonomo`; identity not verified) then pointed to the Bonmin side. [practice] P

### B.8 Application partners in the IBM era (co-authored records)

- [stated-joint] P. **Airlines** (ICM 1998 chapter).
  - "John Forrest[16] introduced the so-called Sprint method". Reference [16] is a talk at the ORSA/TIMS Joint National Meeting, New York, October 1989.
  - The example is an American Airlines problem: 837 flights and 5.5 million pairings, with times "on a S/390 (in 1989)".
  - The conclusion says the methods "are used successfully by several airlines".
- [stated-joint] P. **Steel** (abstract of the IJOC 2006 paper). The work was motivated by "a real application from the steel industry". The instance mkc is in MIPLIB; mkc7 was posted on the COIN site.
- [stated-joint] P; [observed] S. **Semiconductor supply chain:** the *Interfaces* 2006 paper and the 2005 Wagner Prize.
- [stated] P. **His own unpublished methods** (Cbc FAQ, JF 05/24/06): "I need to publish some more heuristic methods as I have several I use for my own work which at present are too problem specific." See §E.

---

## C. How he teaches users and learners (the closest thing to supervision)

### C.1 Reading paths through the code, and example programs

- [stated] P. **A path through the code** (Clp#262, 2023-03-28). Asked how to implement a custom pivoting rule, he said he had searched the web and "was not impressed". He then laid out a path:
  1. the base class `ClpDualRowPivot`;
  2. the simplest implementation, `ClpDualRowDantzig`;
  3. the efficient one, `ClpDualRowSteepest`;
  4. for the primal method, the `ClpPrimalColumn` classes.

  On the Abc files he advised: "I would only look at Clp versions" (see §E).
- [stated] P. **Example programs as teaching material:**
  - "It may be worth looking at the example in Clp/examples - sprint.cpp." (Clp#271, 2023);
  - `Clp/examples/addRows.cpp` "is there just to explain why it is not a good idea to add one row at a time for many rows" (Cbc#301, 2020);
  - `link.cpp` and `gear.cpp` for linked ordered sets (Cbc#297, 2020);
  - Cbc FAQ (JF 05/24/06): the sample drivers are the way in, and "sample2.cpp and sample3.cpp expose more of the strategy as user code".
- [practice] P. At HEAD, `Clp/examples` holds 36 C/C++ programs and `Cbc/examples` holds 52.
- [stated-joint] P. **The CLP User's Guide (2004) sets a documentation order.** It is to be used "in conjunction with the files in the examples subdirectory". Where the guide or Doxygen disagrees with the code, "the comments in the Clp header files are the ultimate reference".

### C.2 Built-in help as documentation

- [stated] P. **A complete answer can be a help query.** Asked what Clp's "one phase" method is, he replied in full: run clp and enter "primalweight?? or dualbound??" (Clp#263, 2023). When pressed, he followed up with two short numbered explanations.
- [stated] P. **Another one-line answer:** `model.setLogLevel(63)` (Clp#266, 2023).
- [practice] P. **The way to the hidden options** (Cbc FAQ; this entry carries no initials, so it is a project text, not necessarily his): set verbose to 15 and enter "?" to list all commands.
- [observed] S. **The 2004 Clp FAQ (DN)** asks the community to link the executable's help to the sample programs, so that a query like "presol???" would point users to the relevant samples.

### C.3 Explaining a failure with the user's own numbers

[stated] P throughout.

- **A tolerance accident** (Cbc#689, 2025):
  - a variable sat at 20.000003, just outside the integer tolerance;
  - an extrapolated bound tightening then cut off the true optimum ("about three computations went the wrong way");
  - "Dealing with tolerances is tricky".
  - The fix is a one-line extra condition, which he posted as a diff.
- **A memory blow-up** (CoinUtils#103, 2019): 160,000 list entries but only 300 unique ones; the code "thought it had about a billion zero elements!"
- **A segfault from integer overflow** (Clp#90, 2017):
  - his first reply guessed at memory and offered a workaround;
  - his second worked from the numbers: 303,061,248 matrix elements take 2,424,489,984 bytes, so an offset stored in an `int` would overflow, and he suggested building with `-DCOIN_BIG_INDEX=2`;
  - in 2019 he reported it "Should be fixed": an `int` had been used for the size of a double array in bytes.
- **A histogram as first diagnosis** (Cbc#338, 2020). His first reply to a researcher's hard-to-trace node-pruning problem was a histogram of the instance's coefficient magnitudes, ranging from 1e-15 to 100.
- **Explaining the default gap** (Cbc#703, 2025):
  - Cbc's default gap is 0.0;
  - another solver's "optimal" answer was 6000 worse because it used a 0.01 gap;
  - he showed what the output looks like once `ratioGap` is set.

### C.4 Fix first, then explain; side channels

- [stated] P. **Private side channels:** "I will send you the basis" (Clp#157, 2020); "I will send you some updated code" (Cbc#338, 2020).
- [stated] P. **Fix first, then ask:** "Does change to ClpSimplexDual.cpp in master fix this?" (Clp#341, 2026, on a report signed "ChipLab").
- [stated] P. **"Dirty fixes" with line numbers.** For a user who could rebuild from source, he gave an `if` statement to add near a named line of `ClpSolve.cpp` (Clp#90, 2017). After checking with gdb he revised it ("On looking more carefully (and using gdb) the simplest is …").
- [practice] P. **From e-mail to the web UI.** In the 2018–2020 threads he answered by e-mail. All 10 of his 2020 comments in the sample are signed "John Forrest" or "John", and 9 quote the message they answer. In 2022–2026 none of his 69 sampled comments is signed or e-mail-quoted. These are counts over the sample, not over all his comments.

### C.5 How fast he answers (sample statistics; the sample is not random)

- [practice] P. **Time from the opening post to his first comment**, over the 43 sampled threads opened by others:

| Measure | Value |
|---|---|
| Median | 16.7 hours |
| Within 24 hours | 25 threads |
| Within 72 hours | 36 threads |

- **The outliers:**
  - Bonmin#31: about 11 months. He joined after Vigerske reproduced the failure.
  - Cbc#622: about 10.5 months.
  - Cbc#787: about 44 days, after Santos had said he was reviewing.
  - Cbc#362: about 12 days.
- [observed] S. Four different users thanked him for a "quick" reply or fix (Clp#262, Cbc#616, Cbc#689, Clp#341).
- **Caveat:** this measures the delay to *his* first comment, not to the first answer from any maintainer.

### C.6 Tone, and open limits of competence

- [stated] P. **Self-deprecating apologies:**
  - "Apologies - my stupidity." (Cbc#759, 2026-01-04). A debugging assert he had added to CoinUtils on 2025-12-15 (`df3e486`) broke debug builds and Windows CI. The commit that removed it reads: "Stupidly I left in an assert which was helping debug another bug" (CoinUtils `7183322`).
  - "I am an idiot." (Cbc#748, 2025).
- [stated] P. **Open limits:**
  - "I am not an expert in flow cover cuts" (Cbc#769, 2026). He found the bug, posted a fix and asked "can someone check it".
  - "I have not got the energy to dig into the Julia interfaces" (Cbc#301, 2020).
  - "code I have little connection to" (CoinUtils#233, 2024).
- [stated] P. **Humour:**
  - "stressing my small laptop" (Cbc#837, 2026);
  - "Have you got a tiny model i.e. only a million variables?" (Cbc#837);
  - Clp help text: "If you are masochistic you can switch it off." (about turning off the Forrest–Tomlin update);
  - Cbc FAQ (JF 04/01/05) on documentation: "If you can see this you have the best there is:-)".
- [observed] S. **A 2004 colleague on the boundary of his expertise** (Clp FAQ, DN 09/16/04). The barrier code is less mature partly because "the principal author, John Forrest, knows more about simplex algorithms than interior point algorithms".

---

## D. Tacit knowledge: what his collaborators know that the papers do not say

### D.1 Techniques that live in code, talks and e-mail, and were written up by others

| Technique | How he passed it on | Who wrote it up, and what they said |
|---|---|---|
| **Sprint (sifting)** | A talk at the ORSA/TIMS meeting, New York, October 1989; implemented in OSL (per the ICM table) | The co-authored ICM 1998 chapter, with the American Airlines table [stated-joint] P |
| **Idiot crash** | Clp code (from 2002); comments in the source; a 2014 mailing-list e-mail that refers to "a bad talk on it years ago" (quoted by Galabova & Hall; the e-mail was not reached) | Galabova & Hall, arXiv:1804.09172 v1 (24 Apr 2018), PDF p. 2: beyond the source and that e-mail, the Idiot crash "lacks documentation or analysis". Published in *Optim. Methods Softw.* 35(3):488–501, DOI 10.1080/10556788.2019.1604702. Galabova's PhD thesis (Edinburgh, 2022), pp. 9–10: because there was "no published scientific study of it" (ligatures restored from the text layer), Google funded a research project to carry one out. Neither the thesis's acknowledgements nor its text names Forrest; it cites Clp by repository [observed] S |
| **Aboca / Abc (parallel dual)** | Code (2012) and an ISMP 2012 talk; a fastercoin.com "Never Asked Questions" page (cited by Huangfu & Hall; not reached) | Huangfu & Hall, *Math. Program. Comput.* 10(1):119–142, 2018, DOI 10.1007/s12532-017-0130-5, p. 124: other than the source code, the authors "believe that there is no published reference to this work" [observed] S |
| **Clp's dual simplex internals** | Code only | Koberstein, *The Dual Simplex Method, Techniques for a fast and stable implementation* (Dissertation, Universität Paderborn, 2005). Footnote on p. 2: the COIN LP code "is largely undocumented" and nothing has been published about its internals. On p. 29 he presents a bound-flipping version "motivated by the dual simplex implementation in the COIN LP code" [observed] S |
| **Linked ordered sets (`OsiSolverLink`)** | Example programs `link.cpp` and `gear.cpp`; reference [16] in Optima 75, "J. Forrest and J. Lee (in preparation)" | No Forrest–Lee paper exists in DBLP or OpenAlex (2026-11-05). In 2020 he wrote "it is possible that it is a half finished project" (Cbc#297) [stated] P |

[inferred] **So the people who know his methods best are of three kinds:**
- co-maintainers who read his code;
- researchers who reverse-engineered parts of it from the source (Edinburgh, Paderborn);
- users he answered in issues and on the mailing lists.

His craft travels through code and conversation, not through papers.

### D.2 Hidden switches and hooks

- [practice] P. **Option bit masks documented only in header comments.**
  - `ClpSimplex.hpp`, at `setMoreSpecialOptions`, lists 28 entries, from "1 bit" up to "268435456 bit" (one entry, "131072 bit (*3)", spans two bits). An example: "8192 bit - don't even think of using primal if user asks for dual (and vv)".
  - [stated] P. In issues he gives users the exact bits:
    - specialOptions 32, to get a ray even inside branch and bound (Clp#286, 2024);
    - moreSpecialOptions 256 and specialOptions 2048 ("no crunch"), plus a new bit 0x08000000 he added for the user (Clp#291, 2024).
  - He also recalls two bits from years before: 0x01000000 "is Cbc" and 0x02000000 is "a different branch and bound". By his account the second is unused (Clp#291).
- [practice] P. **Compile-time defines as the release channel for experimental code:**
  - `-DCOIN_MORE_INFORMATION`, which he suggested for extra event hooks (Cbc#327, 2020);
  - `-DCBC_USE_PAPILO=1` (Cbc `729e751`, 2024);
  - `CBC_MANY_NODE_COUNTS` and `CBC_FEW_NODE_COUNTS` (Cbc `6f83969`, 2023; `8cbc80a`, 2024);
  - `-DTREAT_AS_OPTIMAL_TOLERANCE` (Clp#90, comment of 2021);
  - `-DCOIN_BIG_INDEX=2` (Clp#90).

  In 2026: "I am modifying stable - any modifications would be on -D........ in build" (Cbc#837).
- [practice] P. **A debugging hook he then advertised.** The environment variable `COIN_CBC_OPTIONS` (Cbc `efdc0d9`, 2023-08-29) feeds standard cbc options through the C interface. He added it to debug C++ called from Python, then announced it as "of interest to people using Cbc master and python-mip" (Cbc#618).

### D.3 His own test harness and build habits

- [stated] P. **A MIPLIB unit test, timed.** He runs it from the command line, e.g. `-dirmiplib ~/miplib3++level0-3 -optionfile … -unittest`, and times it with `time` (Cbc#774, 2026).
- [stated] P. **He builds with his own non-default options:**
  - "With my normal options the error does not occur." (Cbc#769, 2026);
  - he asks reporters exactly how they build: "It would be useful to know exactly how you build cbc". He adds that the default build is reasonably optimized and seems to switch off asserts (Cbc#711, 2025).
- [practice] P. **When he cannot reproduce, he sends instrumentation.** "Unable to reproduce" (Cbc#711, Cbc#759) is followed by a debug patch for the reporter to run (Cbc#759).

### D.4 Branch etiquette

- [practice] P. **He commits to master; co-maintainers carry fixes to stable** (CoinUtils#206, Cbc#504, Cbc#774).
- [practice] P. **In 2026 he worked on stable**, with `-D` switches, while others built "next" (Cbc#837; §B.5).

---

## E. Failures, abandoned directions, friction (collaboration side)

1. **Abc/Aboca.** [stated] P (Clp#262, 2023): Abc was "a partially successful attempt to parallelize the simplex method". By the same account it was written more than ten years earlier "for a conference" and "not kept up to date". He told a learner to look only at the Clp versions. Compare his 2026 remark in H4.
2. **Linked ordered sets and the Forrest–Lee paper.**
   - Optima 75 (2007) cites "J. Forrest and J. Lee (in preparation)" for remodeling a broad subclass of MINLPs as MILPs with linked ordered sets.
   - No such paper appears in DBLP or OpenAlex as of 2026-11-05.
   - In 2020 `gear.cpp` needed a fix in master before it would run. The comment in `gear.cpp` says the column-generation generalization "is not yet in CBC". He wrote: "it is possible that it is a half finished project" (Cbc#297). [stated] P; [practice] P
3. **Heuristics kept private.** "I need to publish some more heuristic methods …" (Cbc FAQ, JF 05/24/06). No later publication of them was found in DBLP or OpenAlex. [stated] P
4. **Contributors' work absorbed and closed.** Cbc#787 was closed as redundant after weeks of pings. Cbc#622 waited about 10.5 months for a "Fine by me". [practice] P
5. **A debugging assert left in** (CoinUtils `df3e486`, 2025-12-15). It broke debug runs and Windows CI. The cause was found from a reporter's crash, Goossens' CI check and Vigerske's pointer to the commit. He removed it on 2026-01-04 with an apology (Cbc#759). [practice] P
6. **Hand-over of roles.** Clp went to Hall and Cbc to Ralphs by 2011 (§A.4). There is also the 2010 "Stepping down" post, known from its title only.
7. **The 2026 "next" branch.** He raised concerns on 10-17 and 10-20; next was merged on 10-22 (§B.5).
8. **Failed ideas admitted in commit messages** [stated] P. 03-process-evidence.md has the full list. Three examples:
   - "my clever idea on branching seems to have failed" (Cbc `fd36bf5`, 2007-10-09);
   - "not a good idea - revert idea of updating best solution in small b&b for ctrl-c" (Cbc `bf207ad`, 2013-01-25);
   - "mistake on Nauty idea" (Cbc `28fdb3f`, 2022-01-26).

---

## F. Era and resource context

| Period | Setting | People he worked with | Compute and tools | Evidence |
|---|---|---|---|---|
| 1970s | Scicon Ltd, London: consultancy and mathematical-programming systems (UMPIRE, Sciconic) | Beale (senior), Tomlin, Hirst (British Petroleum) | Mainframe MP systems | 1972, 1974 and 1976 papers; Cup 2005; Tomlin profile; Bixby 2012 p. 109 |
| c. 1980s–2000s | IBM Research: OSL, application projects | Tomlin; Goldfarb (Columbia); Anbil, Pulleyblank, Barahona; Dietrich; Kalagnanam, Ladanyi; Denton, Milne; the IBM–CMU MINLP group (2004–07) | S/390 (1989 Sprint timings); IBM 3090 vector and RISC System/6000 (1992 abstract) | Papers; ICM 1998; OpenAlex abstract |
| 2000–2004 | COIN-OR as a three-year IBM Research experiment | COIN-OR's founders and incorporators named in the 2014 Impact Prize; de la Nuez (documentation) | CVS/SVN, mailing lists, DocBook user guides | INFORMS 2014; Cup 2005; Clp history |
| 2004–2019 | COIN-OR Foundation, hosted by INFORMS; Trac and mailing lists | Hafer, Ralphs, Vigerske, H. G. Santos; a 2009 burst of outside contributors (Kristjansson, Strayer, Fylstra; affiliations not checked) | SVN, then git (2019) | git history; 2011 annual report |
| 2019–2026 | GitHub: issues, PRs, CLA assistant, CI | Ralphs, Vigerske, H. G. Santos, Goossens; outside contributors; systematic reporters (a 2025 series of parameter-combination crash reports from `zxt5`; a 2026 report signed "ChipLab") | His "small laptop"; e-mail replies in 2018–20, web comments later | Issue sample; git history |
| 2026 | AI-assisted co-maintenance by others | Ralphs, H. G. Santos | 68 Cbc commits with "Co-authored-by: Claude" | git history |

- **Retirement:** the Cbc README says he is "now retired from IBM Research". The date is not established here; team.json places it between 2006 and 2010.

---

## G. Layer map (where these findings feed the seven layers)

| Layer | Findings in this file |
|---|---|
| 1 Taste | Credit kept at the point of use (B.3). "Close the loop" (B.2). A 2004 project value: "Some speed has been sacrificed to make the code less opaque OSL (not difficult!)", from the Clp FAQ (DN), [observed] S |
| 2 Problem choice | Client and partner problems drove the techniques: airlines, steel, semiconductors (B.8) |
| 3 Idea generation | No new evidence here (see 02 and 03) |
| 4 Execution | Experimental code behind switches and defines (D.2); his MIPLIB unit test; builds with his own options (D.3) |
| 5 Judging results | Reproduce first; if he cannot, send instrumentation (D.3). Measure the cost of a process change before accepting it (B.5, Cbc#774) |
| 6 Expression | Few papers, all co-authored. Help text, examples and header comments as the documentation (C.1–C.2). Techniques written up by others (D.1) |
| 7 Research organisation | B.1–B.8 and C |

**Candidate heuristics for Phase 2.** [inferred] Each still needs the four-way check: recurrence, say/do consistency, executability, distinctiveness.

| # | Candidate | Evidence | Caution |
|---|---|---|---|
| 1 | Give credit at the point of use: when absorbing someone's code, put their name, role and paper in the help text, the header and AUTHORS | B.3 | |
| 2 | Answer a learner with a path into the code: base class, then the simplest implementation, then the efficient one, then an example program | C.1 | |
| 3 | Diagnose from the reporter's own instance and explain with its numbers | C.3 | |
| 4 | Ship experiments behind switches and tell the users who need them | D.2 | |
| 5 | Report upstream with a minimized instance, a one-change diff and a debugger trace, and say what you do not know | B.7 | |
| 6 | Re-implement contributions to fit the conventions | B.6, E.4 | Has visible costs. Do not recommend it without its downside |

---

## H. Contradictions (kept, not reconciled)

- **H1. Who manages Cbc.**
  - The README (read 2026-11-05) lists "John Forrest, Ted Ralphs, Stefan Vigerske, Haroldo Gambini Santos".
  - The same repository's `.coin-or/config.yml`, from which the README says it is generated, names one manager: Ted Ralphs.
  - The 2011 annual report lists Cbc under Ted Ralphs.
  - A 2010 post is titled as his stepping down as project manager for Cbc and Clp. Only the title was seen.
- **H2. Authorship of Cbc and Clp against the history.**
  - The COIN-OR Cup 2005 calls him "Author of" CLP and CBC. The README says Cbc is "developed by John Forrest … and others".
  - Git author names give him 1,060 of 3,101 Cbc commits on master, with H. G. Santos at 807 and Ralphs at 447.
  - The team.json split by GitHub account (johnjforrest 797, jjhforrest 263) adds up to the same 1,060, divided differently.
  - The Clp 1.17.0 AUTHORS file (2019) names only him. The history to 2026 shows eight other committers with 25 or more commits each, several of them active mainly after 2019.
- **H3. Where his Cgl role is recorded.** The Cgl AUTHORS file lists him as "PM" for 13 generators. The Cgl README names Robin Lougee and François Margot as the project's managers.
- **H4. Abc, then and now.**
  - 2023 (Clp#262): Abc was only "partially successful" and is not kept up to date; "I would only look at Clp versions".
  - 2026-11-01 (Cbc#837), on solving huge set-partitioning LPs: "the answer may be as simple as abc."
- **H5. Credit for the Forrest–Tomlin update.** The INFORMS profile says Tomlin "created the Forrest-Tomlin method". The 1972 paper is joint, with Forrest as first author.
- **H6. A patch or the root cause** (CoinUtils#206). Forrest's position: the workaround is correct and harmless. Ralphs' position: the flag cannot be trusted and should not be used. The thread ends with Ralphs deferring ("you know better than me"); the disagreement itself is not settled.
- **H7. Inviting contributions against doing the work himself.** He invites others ("unless someone else wants to …", "Feel free to suggest …"), yet in Cbc#656 and Cbc#787 he made the change himself. Cbc#748 is a related case: he did merge the contributor's parameter, but only after reshaping and renaming it.
- **H8. His stance on "next" within one week.** On 2026-10-17 he questioned whether "next" is really the next master and worried about the pace. On 2026-10-23 he said the main thing is to get next moved to master.
- **H9. Speed.** Users repeatedly thank him for quick fixes (C.5). He objected to the speed of changes made by others (B.5).

---

## I. Gaps (not found, not read, not reached)

- **Supervision.** No doctoral students, interns, postdocs, lab guide, onboarding text, student blog post, interview, oral history, Festschrift or memoir about him was found. WebSearch: 6 calls, 3 of them unusable.
  - One returned only pages already known.
  - One returned baseball pages.
  - One returned physics and rail-accident pages.
- **Mathematics Genealogy Project:** the POST search returned an empty results page to curl. Not checked.
- **His own training:** how Beale or anyone else trained him is not documented in anything I could read. The sources that might say were not read:
  - Forrest & Tomlin, *Annals of OR* 149 (2007): closed.
  - Tomlin's 2011 profile of Beale: closed; abstract and references only.
  - Powell's Royal Society memoir of Beale: the PDF returned HTTP 403; only the OR Society summary was read.
  - Haley's 1986 JORS appreciation (DOI 10.1057/jors.1986.179): closed.
- **The mailing lists** (list.coin-or.org): timed out on 2026-11-05.
  - [inferred] Most of his pre-2017 teaching and user contact probably happened there: the Cbc FAQ sends users to the coin-discuss list, and Galabova & Hall cite a 2014 list e-mail of his.
  - Two search-result leads (2010-02/001068; 2012-10/001326–001327) were not read.
  - The archive copy (web.archive.org) was not used, as instructed.
- **fastercoin.com** ("Never Asked Questions", cited by Huangfu & Hall): not tried. team.json records the domain as parked.
- **Not read:** the 2005 TutORials CBC User Guide (closed) and Lougee-Heimer's 2003 IBM J. Res. Dev. paper on COIN-OR (DOI 10.1147/rd.471.0057, closed).
- **Not reached:** `coin-or.org/Presentations/COIN.ORMSToday.092004.FINAL.doc` (HTTP 404; the site was rebuilt in 2026).
- **Not identified:** an unidentified PDF from a search (core.ac.uk/download/429720904.pdf) returned HTTP 403.
- **Thesis acknowledgements:** none found that name him.
  - Checked and negative: Galabova (2022); Koberstein (2005, Danksagung); Brito & Santos (arXiv 1909.07780).
  - Not checked: the Positive Edge papers' acknowledgements (Towhidi 2014; Omer 2015), and any Lehigh, CMU or Columbia thesis of his COIN-OR or IBM collaborators.
- **Status of de la Nuez and Namazifar** (student, intern or employee): not established. Semantic Scholar rate-limited the second Namazifar record.
- **IBM-era team practice** (OSL group size, how work was divided with Tomlin): no readable source.
- **Search-engine snippet not confirmed:** a summary claimed that a Clp page says the project is managed by "John Forrest, Julian Hall, and the rest of the Clp team". I could not find that text on any page I fetched (Clp README, `coin-or.github.io/Clp/`, the Clp FAQ), so it is not used.
- **Sample bias:** the 47 threads were chosen for teaching, contributor and co-maintainer content. The statistics in C.4–C.5 describe this sample, not all 461 (or 486) of his comments.

---

## Sources

### Primary: his own words, joint texts, code and project records

**GitHub threads (47).** All comments are by the account `jjhforrest`, unless a thread is noted as opened by another user. Read on 2026-11-05.

1. coin-or/Clp#90, "Segmentation fault with increasing problem size" (opened 2017-12-20). https://github.com/coin-or/Clp/issues/90 (P)
2. coin-or/Clp#141, "Querying MaximumSeconds returns un-interpretable value" (2020-04-07). https://github.com/coin-or/Clp/issues/141 (P)
3. coin-or/Clp#157, "Inconsistent results and long resolve times…" (2020-08-02). https://github.com/coin-or/Clp/issues/157 (P)
4. coin-or/Clp#262, "Guidence to add user customed pivoting rule" (2023-03-28). https://github.com/coin-or/Clp/issues/262 (P)
5. coin-or/Clp#263, "Which simplex method does CLP actually use?" (2023-03-31). https://github.com/coin-or/Clp/issues/263 (P)
6. coin-or/Clp#266, "Clp print information … for each pivoting iteration" (2023-04-18). https://github.com/coin-or/Clp/issues/266 (P)
7. coin-or/Clp#271, "Warm start best practice" (2023-06-21). https://github.com/coin-or/Clp/issues/271 (P)
8. coin-or/Clp#272, "What is a singleton column exactly?" (2023-07-04). https://github.com/coin-or/Clp/issues/272 (P)
9. coin-or/Clp#286, "Interpreting infeasibility/unboundedness ray in CLP" (2024-03-07). https://github.com/coin-or/Clp/issues/286 (P)
10. coin-or/Clp#291, "Objective value from dual feasible solution mismatch…" (2024-03-22). https://github.com/coin-or/Clp/issues/291 (P)
11. coin-or/Clp#336 (PR), "Fix memory corruption, wrong heap access" (2026-09-03). https://github.com/coin-or/Clp/pull/336 (P)
12. coin-or/Clp#341, "Default and direct dual report optimality for an unbounded LP…" (2026-10-12). https://github.com/coin-or/Clp/issues/341 (P)
13. coin-or/Clp#358, "Produce the tabular output through an en_tabular message language" (2026-10-23). https://github.com/coin-or/Clp/issues/358 (P)
14. coin-or/Cbc#297, "the purpose of OsiSolverLink" (2020-04-14). https://github.com/coin-or/Cbc/issues/297 (P)
15. coin-or/Cbc#301, "Obtaining duals for LP on Cbc - Clp's performance lagging" (2020-04-30). https://github.com/coin-or/Cbc/issues/301 (P)
16. coin-or/Cbc#313, "How to know if an LP problem has multiple optimal solutions?" (2020-06-17). https://github.com/coin-or/Cbc/issues/313 (P)
17. coin-or/Cbc#327, "Tracking nodes pruned by bound and by infeasibility" (2020-08-25). https://github.com/coin-or/Cbc/issues/327 (P)
18. coin-or/Cbc#338, "Branch-and-bound node incorrectly pruned by infeasibility" (2020-09-24). https://github.com/coin-or/Cbc/issues/338 (P)
19. coin-or/Cbc#616, "Suboptimal MIP Solution with LazyConstraints due to analyzeObjective?" (2023-08-25). https://github.com/coin-or/Cbc/issues/616 (P)
20. coin-or/Cbc#618, "Lazy and generated constraint model much slower than complete model" (2023-08-30). https://github.com/coin-or/Cbc/issues/618 (P)
21. coin-or/Cbc#689, "Incorrect Optimal Solution by calling Cbc from pulp" (2025-02-01). https://github.com/coin-or/Cbc/issues/689 (P)
22. coin-or/Cbc#703, "Duality gap of the solution found by CBC for MILPs" (2025-04-16). https://github.com/coin-or/Cbc/issues/703 (P)
23. coin-or/Cbc#711, "cbc crashes if twoMirCuts is enabled" (2025-04-26). https://github.com/coin-or/Cbc/issues/711 (P)
24. coin-or/Cbc#759, "CoinIndexedVector.cpp:1892 … getCapacity" (2025-12-30). https://github.com/coin-or/Cbc/issues/759 (P)
25. coin-or/Cbc#769, "Unit test fails with some compile options (bad CglFlowCover cut)" (opened by him, 2026-02-25). https://github.com/coin-or/Cbc/issues/769 (P)
26. coin-or/Cbc#837, "Using idiot crash repeatedly for set partitioning" (2026-10-27). https://github.com/coin-or/Cbc/issues/837 (P)
27. coin-or/Cbc#362 (PR), "delete unused file src/CbcBranchBase.cpp" (2021-02-10). https://github.com/coin-or/Cbc/pull/362 (P)
28. coin-or/Cbc#374 (PR), "Refactor Cbc" (2021-03-15), read through the REST API. https://github.com/coin-or/Cbc/pull/374 (P)
29. coin-or/Cbc#504 (PR), "Fix SOS2 branching" (2022-05-23). https://github.com/coin-or/Cbc/pull/504 (P)
30. coin-or/Cbc#570 (PR), "CbcSolver callback returncode not used" (2023-01-21). https://github.com/coin-or/Cbc/pull/570 (P)
31. coin-or/Cbc#622 (PR), "precision in solution file 'all'" (2023-10-04). https://github.com/coin-or/Cbc/pull/622 (P)
32. coin-or/Cbc#656 (PR), "Add Cbc_modifyCoefficient to C interface." (2024-07-02). https://github.com/coin-or/Cbc/pull/656 (P)
33. coin-or/Cbc#658 (PR), "Remove {CBC,COIN}_HAS_CLP checks" (2024-07-25). https://github.com/coin-or/Cbc/pull/658 (P)
34. coin-or/Cbc#748 (PR), "Add outputPrecision parameter…" (2025-10-20). https://github.com/coin-or/Cbc/pull/748 (P)
35. coin-or/Cbc#774 (PR), "fix time measurement and time limit" (2026-03-13). https://github.com/coin-or/Cbc/pull/774 (P)
36. coin-or/Cbc#787 (PR), "fix: use the solver's objective sense when a MIP start sets the cutoff" (2026-08-08). https://github.com/coin-or/Cbc/pull/787 (P)
37. coin-or/Cbc#807 (PR), "Don't restrict cuts for models with branching objects from another solver" (2026-10-16). https://github.com/coin-or/Cbc/pull/807 (P)
38. coin-or/Cbc#809 (PR), "Set the model status when bound propagation proves infeasibility" (2026-10-17). https://github.com/coin-or/Cbc/pull/809 (P)
39. coin-or/CoinUtils#103, "Massive memory use in presolve" (2019-08-05). https://github.com/coin-or/CoinUtils/issues/103 (P)
40. coin-or/CoinUtils#206, "CoinUtils fails to read valid MPS file" (2023-03-31). https://github.com/coin-or/CoinUtils/issues/206 (P)
41. coin-or/CoinUtils#191 (PR), "Tweak code in CoinPresolveDoubleton…" (2022-03-02). https://github.com/coin-or/CoinUtils/pull/191 (P)
42. coin-or/CoinUtils#233 (PR), "Use C++ streams for error messages" (2024-07-29). https://github.com/coin-or/CoinUtils/pull/233 (P)
43. coin-or/Osi#193, "basisIsAvailable and tableau operations after clone" (2024-07-07). https://github.com/coin-or/Osi/issues/193 (P)
44. coin-or/Bonmin#31, "On basic problem, 'B-Ecp' terminates with libc++abi.dylib exception" (2022-03-03). https://github.com/coin-or/Bonmin/issues/31 (P)
45. coin-or/SHOT#159, "invalid read in CbcModel::setBestSolution()" (2022-07-08). https://github.com/coin-or/SHOT/issues/159 (P)
46. scipopt/papilo#59, "Close to infinite loop in ParallelColDetection" (opened by him, 2024-09-06). https://github.com/scipopt/papilo/issues/59 (P)
47. scipopt/papilo#62, "Incorrect answer with large upper bounds" (opened by him, 2024-09-10). https://github.com/scipopt/papilo/issues/62 (P)

**Code and project records.**

48. coin-or/Clp git history: 2,267 commits, blobless clone, read 2026-11-05. https://github.com/coin-or/Clp (P)
49. coin-or/Cbc git history: 3,101 commits on master; all branches fetched for the 2026 counts. https://github.com/coin-or/Cbc (P)
50. coin-or/CoinUtils git history: 1,906 commits. https://github.com/coin-or/CoinUtils (P)
51. coin-or/Cgl git history: 1,249 commits. https://github.com/coin-or/Cgl (P)
52. Cbc `AUTHORS` (updated Feb 10, 2020). https://raw.githubusercontent.com/coin-or/Cbc/master/AUTHORS (P)
53. Cgl `AUTHORS` (per-generator contributors and PMs). https://raw.githubusercontent.com/coin-or/Cgl/master/AUTHORS (P)
54. Osi `AUTHORS` (05/24/2007). https://raw.githubusercontent.com/coin-or/Osi/master/AUTHORS (P)
55. Clp `Clp/AUTHORS` at tag releases/1.17.0. https://github.com/coin-or/Clp/tree/releases/1.17.0 (P)
56. Cbc `README.md` (read 2026-11-05). https://github.com/coin-or/Cbc (P, project record)
57. Clp `README.md`. https://github.com/coin-or/Clp (P, project record)
58. CoinUtils `README.md`. https://github.com/coin-or/CoinUtils (P, project record)
59. Cgl `README.md`. https://github.com/coin-or/Cgl (P, project record)
60. Osi `README.md`. https://github.com/coin-or/Osi (P, project record)
61. Clp `.coin-or/config.yml` ("Manager: Julian Hall"). https://github.com/coin-or/Clp/blob/master/.coin-or/config.yml (P)
62. Cbc `.coin-or/config.yml` ("Manager: Ted Ralphs"). https://github.com/coin-or/Cbc/blob/master/.coin-or/config.yml (P)
63. CoinUtils `.coin-or/config.yml` ("Manager: Laszlo Ladanyi"). https://github.com/coin-or/CoinUtils/blob/master/.coin-or/config.yml (P)
64. Clp `src/ClpCholeskyBase.cpp` header (Gupta credit), HEAD 2026-11-05 (P)
65. Clp `src/ClpParameters.cpp` and `src/CbcOrClpParam.cpp` help strings (Positive Edge credit; "masochistic"), HEAD (P)
66. Clp `src/ClpPdco.cpp/.hpp`, `src/ClpInterior.hpp`, `src/ClpPE*` headers (Saunders, Tomlin, Omer, Towhidi), HEAD (P)
67. Clp `src/ClpSimplex.hpp`: the `setMoreSpecialOptions` bit list, HEAD (P)
68. Clp `examples/` (36 programs; `addRows.cpp` header), HEAD (P)
69. Cbc `src/CbcSymmetry.cpp/.hpp` (Ostrowski / "rest JJHF"; Belotti); first version `72cfa4f`, 2014-07-16 (P)
70. Cbc `src/Cbc_C_Interface.h` (Entriken), `src/CbcParameters.cpp` (Caprara), `src/CbcHeuristicPivotAndFix.cpp` and `src/CbcHeuristicRandRound.cpp` ("Ask JJHF"), HEAD (P)
71. Cbc `examples/` (52 programs), HEAD (P)
72. *CLP User's Guide*: John Forrest, David de la Nuez, Robin Lougee-Heimer; IBM, 2004. https://coin-or.github.io/Clp/ (P, joint)
73. *CBC User's Guide*: John Forrest, Robin Lougee-Heimer (front page and Introduction). https://coin-or.github.io/Cbc/ and https://coin-or.github.io/Cbc/intro (P, joint)
74. Cbc FAQ: answers initialled "JF" (2005–2006) and an unsigned "Lessons from the Trenches" section. https://coin-or.github.io/Cbc/faq (P for the JF entries; S for the rest)

**Co-authored texts read.**

75. P. Bonami, J. J. Forrest, J. Lee, A. Wächter, "Rapid Development of an Open-source Minlp Solver with COIN-OR", *Optima* 75, December 2007, pp. 1–4. https://mathopt.zib.de/Optima-Issues/optima75.pdf (P, joint; read)
76. R. Anbil, J. J. Forrest, W. R. Pulleyblank, "Column generation and the airline crew pairing problem", *Documenta Math.* Extra Vol. ICM 1998, III, 677–686. DOI 10.4171/dms/1-3/65; PDF at https://ems.press/content/book-chapter-files/27279 (P, joint; read)

**Thread index.**

77. GitHub search index, `commenter:jjhforrest` (291 issues/PRs) and `commenter:johnjforrest` (1). Fetched earlier in this run by agent 03 and read from its scratch folder (P, record)

**Co-authored works checked for metadata only** (Crossref, Unpaywall; abstracts from OpenAlex where noted).

78. J. J. H. Forrest, J. A. Tomlin, *Math. Programming* 2(1):263–278, 1972. DOI 10.1007/BF01584548 (P, metadata)
79. J. J. H. Forrest, J. P. H. Hirst, J. A. Tomlin, *Management Science* 20(5):736–773, 1974. DOI 10.1287/mnsc.20.5.736 (P, abstract)
80. E. M. L. Beale, J. J. H. Forrest, *Math. Programming* 10(1):52–69, 1976. DOI 10.1007/BF01580653 (P, metadata)
81. J. J. H. Forrest, J. A. Tomlin, *Annals of OR* 22:71–100, 1990. DOI 10.1007/BF02023049 (P, metadata)
82. J. J. H. Forrest, J. A. Tomlin, *IBM Systems Journal* 31(1):11–25, 1992. DOI 10.1147/sj.311.0011 (P, abstract)
83. J. J. H. Forrest, J. A. Tomlin, *IBM Systems Journal* 31(1):26–38, 1992. DOI 10.1147/sj.311.0026 (P, metadata)
84. J. J. Forrest, D. Goldfarb, *Math. Programming* 57:341–374, 1992. DOI 10.1007/BF01581089 (P, metadata)
85. B. Dietrich, J. J. Forrest, *IMA Volumes in Mathematics and its Applications*, pp. 15–26, 2002. DOI 10.1007/978-1-4684-9277-4_2 (P, metadata)
86. J. Forrest, R. Lougee-Heimer, "CBC User Guide", INFORMS TutORials 2005, pp. 257–277. DOI 10.1287/educ.1053.0020 (P, metadata; closed)
87. J. J. H. Forrest, J. Kalagnanam, L. Ladanyi, *INFORMS J. Comput.* 18(1):129–134, 2006. DOI 10.1287/ijoc.1040.0078 (P, abstract)
88. B. T. Denton, J. Forrest, R. J. Milne, *Interfaces* 36(5):386–399, 2006. DOI 10.1287/inte.1060.0238 (P, abstract)
89. J. J. H. Forrest, J. A. Tomlin, "Branch and bound, integer, and non-integer programming", *Annals of OR* 149(1):81–87, 2007 (online 2006). DOI 10.1007/s10479-006-0112-x; Springer landing page, metadata only (P; closed)

**Bibliographic lists.**

90. DBLP person 08/3168: 7 records, 1972–2007. SPARQL export cached in this run's scratch (P, list)
91. OpenAlex author A5061258306: 13 works. https://api.openalex.org/works?filter=author.id:A5061258306 (P, list)

### Secondary

92. "COIN-OR Cup 2005 Winners: John J. H. Forrest", COIN-OR. https://www.coin-or.org/coinCup/coinCup2005Winner.html (S)
93. INFORMS, award-recipient page "John Forrest" (2014 Impact Prize citation; 2007 Fellow; 2005 Wagner Prize; 1995 ICS Prize). https://www.informs.org/Recognizing-Excellence/Award-Recipients/John-Forrest (S)
94. INFORMS Computing Society Prize, list of past winners (1995: Forrest and Goldfarb). https://www.informs.org/Recognizing-Excellence/Community-Prizes/Computing-Society/INFORMS-Computing-Society-Prize (S)
95. COIN-OR Foundation, "COIN-OR 2011 Annual Report", November 12, 2011. https://www.coin-or.org/coin-or-foundation/annual_report2011.pdf (S)
96. Clp FAQ, answers initialled "DN", Aug–Sep 2004. https://coin-or.github.io/Clp/faq (S)
97. J. Hall, Q. Huangfu, "A high performance dual revised simplex solver", PPAM talk slides, 13 September 2011 (PDF p. 34). https://webhomes.maths.ed.ac.uk/hall/PPAM11/PPAM11.pdf (S)
98. Q. Huangfu, J. A. J. Hall, "Parallelizing the dual revised simplex method", *Math. Program. Comput.* 10(1):119–142, 2018. DOI 10.1007/s12532-017-0130-5; read at https://webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf (S)
99. I. L. Galabova, J. A. J. Hall, "A quadratic penalty algorithm for linear programming and its application to linearizations of quadratic assignment problems", arXiv:1804.09172 (v1, 24 Apr 2018). Published as "The 'Idiot' crash quadratic penalty algorithm…", *Optim. Methods Softw.* 35(3):488–501, DOI 10.1080/10556788.2019.1604702 (S)
100. I. Galabova, *Presolve, crash and software engineering for HiGHS*, PhD thesis, University of Edinburgh, 2022 (deposited 2023). https://era.ed.ac.uk/handle/1842/39725 (S)
101. A. Koberstein, *The Dual Simplex Method, Techniques for a fast and stable implementation*, Dissertation, Universität Paderborn, 2005. https://digital.ub.uni-paderborn.de/hsmig/download/pdf/3885 (S)
102. S. S. Brito, H. G. Santos, "Preprocessing and cutting planes with conflict graphs", arXiv:1909.07780 (v3); *Comput. Oper. Res.* 128:105176, 2021. DOI 10.1016/j.cor.2020.105176. Checked: no mention of Forrest (S)
103. M. Towhidi, J. Desrosiers, F. Soumis, "The positive edge criterion within COIN-OR's CLP", *Comput. Oper. Res.* 49:41–46, 2014. DOI 10.1016/j.cor.2014.03.020 (S, metadata)
104. J. Omer, M. Towhidi, F. Soumis, "The positive edge pricing rule for the dual simplex", *Comput. Oper. Res.* 61:135–142, 2015. DOI 10.1016/j.cor.2015.03.009 (S, metadata)
105. INFORMS, "Brief Biography: John Tomlin" (History of O.R. Excellence). https://www.informs.org/Explore/History-of-O.R.-Excellence/Biographical-Profiles/Tomlin-John (S)
106. The OR Society, "Martin Beale" (biography, taken from M. J. D. Powell's Royal Society memoir). https://theorsociety.com/common/Uploaded%20files/Awards/BealeBiography.pdf (S)
107. M. J. D. Powell, "Evelyn Martin Lansdowne Beale, 8 September 1928 – 23 December 1985", *Biogr. Mems Fell. R. Soc.*, 1987. DOI 10.1098/rsbm.1987.0002 (S, metadata only; PDF HTTP 403)
108. J. A. Tomlin, "Evelyn Martin Lansdowne Beale", in *Profiles in Operations Research*, Springer, 2011, pp. 677–691. DOI 10.1007/978-1-4419-6281-2_37. Springer page: abstract and references only (S)
109. B. Haley, "Evelyn Martin Lansdowne Beale, F.R.S.: … An Appreciation", *J. Oper. Res. Soc.*, 1986. DOI 10.1057/jors.1986.179 (S, metadata only; closed)
110. R. E. Bixby, "A Brief History of Linear and Mixed-Integer Programming Computation", *Documenta Math.* Extra Vol. ISMP 2012, 107–121 (pp. 109 and 113 used). https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-ismp/25_bixby-robert.pdf (S)

Also checked, with no mention of Forrest found: three COIN-OR Foundation pages ("About", "Technical Leadership Council", "Former Board and Council Members"), https://www.coin-or.org/about-the-foundation/ (S; not counted).
