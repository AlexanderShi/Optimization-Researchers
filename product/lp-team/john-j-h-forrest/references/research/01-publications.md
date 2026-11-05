# John J. H. Forrest · 01 · Publication landscape and signature works

| | |
|---|---|
| Researcher | John J. H. Forrest (DBLP pid 08/3168; OpenAlex A5061258306). Simplex and MIP code author: COIN-OR Clp (2002–), CoinFactorization, Sbb/Cbc (with others), Abc/Aboca (2012); earlier Scicon Ltd (UMPIRE, 1970s) and IBM Research (OSL, 1980s–2000s) |
| Dimension | Research agent 01 of 06: publication landscape and dissection of signature works (framework §二 Agent 1, §五), read through the code-first lens set in team.json |
| Research date | 2026-11-05 |
| Sources consulted | 46 (27 primary, 19 secondary), listed under Sources as W1–W15 (his papers) and S1–S31. 2 WebSearch calls; everything else was fetched with curl, WebFetch, public APIs and blobless git clones of the public coin-or repositories |
| Local corpus | `references/sources/{papers,talks,essays,software}` held only `.gitkeep`: there was no user-supplied material. `publications/` held the OpenAlex harvest made when the member was scaffolded (S7); it was read and used as an index, not as evidence of content. `private/` was not opened |
| OpenAlex | not re-queried: `OPENALEX_API_KEY` is not set. The pinned-author harvest in `references/sources/publications/` (A5061258306, fetched 2026-11-05) was used for counts and one abstract (W6) |
| Quote check | Every passage in double quotation marks below (quotations, titles, commit subjects) was matched by script against the extracted text of its source (PDF text, HTML text, Crossref or Zenodo JSON, git log, or the code file at the commit named), after whitespace, apostrophe, dash and line-break-hyphen normalisation. The count is given at the end of this file. Paraphrases carry no quotation marks. Page numbers are printed page numbers unless marked PDF p. |

**Tags.**
- **[stated]**: said or written by Forrest. Code comments in files whose Authors block names him alone, the 2002 Clp notes, the Clp version log, Cbc FAQ answers signed "JF", and commit messages of his two GitHub accounts count as his voice. "joint" marks a co-authored paper, where voices cannot be separated.
- **[practice]**: what the record shows was done (papers' experiments, code, commits, dated files).
- **[observed]**: what others recorded (co-workers' FAQ answers, prize citations, third-party papers, README files written by maintainers).
- **[inferred]**: my inference, with its basis named.
- **P / S**: primary / secondary source.

**Reading depth.**
- Read in full: W9 (ICM 1998 chapter, 10 pp.), W15 (Optima 75 article, PDF pp. 1–4), the COIN-OR Cup 2005 citation (S18), the Clp FAQ (S17), the Cbc FAQ and the CLP/CBC revision-history pages (S19, S20), the 2002 Clp README and the dual-simplex design notes of the first Clp commit (S21).
- Read in part: Huangfu & Hall 2018 (S14: pp. 123–126, 132, 134, 140 and references); Galabova & Hall 2018 (S15: abstract, PDF pp. 2–3, references); Bixby 2012 (S16: pp. 109–111, 113, 115 and references); headers and design notes of the code files named below (S21–S23).
- Abstract and metadata only: W1, W2, W3, W5, W8, W12, W13 (publisher or Crossref abstracts); W6 (abstract from the OpenAlex harvest, S7); W7, W10, W11 (metadata only).
- Not read: the full texts of W1–W3 and W5–W14 (subscription access only; no legitimate open copy was found). W14, the first-person reminiscence of 2006/2007, is the most important unread item: only its reference list was read. W4 is known only from W14's reference list.

---

## 0. Identity and disambiguation

- [practice, S] **DBLP pid 08/3168** ("John J. H. Forrest", alias "John J. Forrest", affiliation "IBM Research") has 7 records, 1972–2007: W1, W3, W6, W7, W8, W12, W14. Co-authors: John A. Tomlin (4), Donald Goldfarb (1), E. M. L. Beale (1), plus Kalagnanam and Ladányi. The homepage field points to `http://www.research.ibm.com/people/f/forrest/internet/publications.html`, which now redirects to IBM Research's generic People page (S1, S11).
- [practice, S] **DBLP pid 51/5295** ("John Forrest") is a mixed record: it holds W13 (the 2006 IBM supply-chain paper) next to three papers by other John Forrests (embedded hardware 1994 and 1996; data-stream clustering 2014) (S2). W13 belongs to this researcher: Crossref prints his affiliation "IBM T. J. Watson Research Center, PO Box 218, Yorktown Heights" (S6), and OpenAlex A5061258306 includes it (S7).
- [practice, S] **Semantic Scholar author 33308287** ("John J. H. Forrest", DBLP-linked) has 16 items and 1,219 citations (S4). One item is another person's: "The impact of IT on design and construction" (Proc. ICE Civil Engineering 138(2), 2000, DOI 10.1680/CIEN.2000.138.2.87), whose Crossref record lists only T. Broyd of WS Atkins (S6). Two items have no venue or identifier (§1.3).
- [practice, S] **OpenAlex A5061258306** (pinned in team.json): 13 counted works, 1,099 citations, h-index 11 (S7). A name search returns other people (team.json).
- [practice, P] **Name forms in the primary record**: "J. J. H. Forrest" (W1–W3, W5–W7, W12, W14), "John J. Forrest" (W8, W9, W15; Cbc AUTHORS file "Forrest, John J."), "John Forrest" (W11, W13; CLP and CBC user guides; Cbc README), "J. Forrest" (Cbc parameter docs), "JF" (signed FAQ answers), "JJF"/"JJHF" (code comments). Not Jeffrey Yi-Lin Forrest (DBLP 97/3878) or the other Forrests in the DBLP name search (S3).
- [practice, P] **Code identities.** Git history converted from COIN-OR's CVS/SVN shows two identities, both with the author name "John Forrest": one with a fastercoin.com address from 2002-07-30 to 2020-05-11, and one with a gmail.com address (local part `jjhforrest`) from 2020-05-12 (Clp), 2020-05-16 (Cbc) and 2020-05-18 (CoinUtils) to October 2026 (S21–S23). [inferred] The fastercoin.com address on 2002 commits is an artifact of the SVN-to-git author map, not evidence that he used it in 2002. The link between the GitHub accounts `johnjforrest` and `jjhforrest` and this researcher rests on strong inference (team.json), not on any document found here.

---

## 1. Publication landscape

### 1.1 Verified works

Every identifier was resolved with a tool on 2026-11-05 (Crossref REST API, S6, for all DOIs; plus the source named). Position is given as k of n; **every author list of his is in alphabetical order** (§1.5).

| # | Year | Work | Venue | Identifier (how checked) | Position | Read | Tags |
|---|---|---|---|---|---|---|---|
| W1 | 1972 | Updated triangular factors of the basis to maintain sparsity in the product form simplex method | Mathematical Programming 2(1):263–278. Received 9 Sep 1971; both authors "Scientific Control Systems Ltd., Milton Court, London" | DOI 10.1007/BF01584548 (Crossref; DBLP; Springer page S12) | 1 of 2 (Tomlin) | abstract | [practice] [stated, joint] P |
| W2 | 1974 | Practical Solution of Large Mixed Integer Programming Problems with Umpire | Management Science 20(5):736–773. Forrest: Scicon Ltd., London; J. P. H. Hirst: British Petroleum Co. Ltd., London; J. A. Tomlin: "Presently affiliated with Stanford University" | DOI 10.1287/mnsc.20.5.736 (Crossref with abstract) | 1 of 3 | abstract | [practice] [stated, joint] P |
| W3 | 1976 | Global optimization using special ordered sets | Mathematical Programming 10(1):52–69. Received 26 Nov 1973, revised 20 May 1975; both authors "Scientific Control Systems Ltd., Milton Keynes" | DOI 10.1007/BF01580653 (Crossref; DBLP; Springer S12) | 2 of 2 (Beale first) | abstract | [practice] [stated, joint] P |
| W4 | 1978 | Global Optimization as an Extension of Integer Programming | in L. C. W. Dixon and G. P. Szegö (eds.), Towards Global Optimization 2, pp. 131–149, North-Holland | venue + year + title as listed in W14's reference list (Springer page, S12). No DOI; not in DBLP, OpenAlex, Semantic Scholar or Crossref (one Crossref bibliographic query) | 2 of 2 (Beale first) | not read | [practice] P, citation only |
| W5 | 1990 | Vector processing in simplex and interior methods for linear programming | Annals of Operations Research 22(1):71–100. Forrest: IBM T. J. Watson; Tomlin: IBM Almaden | DOI 10.1007/BF02023049 (Crossref; Springer S12) | 1 of 2 | abstract; reference list | [practice] [stated, joint] P |
| W6 | 1992 | Implementing the simplex method for the Optimization Subroutine Library | IBM Systems Journal 31(1):11–25 | DOI 10.1147/sj.311.0011 (Crossref; DBLP). IEEE Xplore page blocked (S13) | 1 of 2 (Tomlin) | abstract via S7 | [practice] [stated, joint] P |
| W7 | 1992 | Implementing interior point linear programming methods in the Optimization Subroutine Library | IBM Systems Journal 31(1):26–38 | DOI 10.1147/sj.311.0026 (Crossref; DBLP) | 1 of 2 (Tomlin) | metadata | [practice] P |
| W8 | 1992 | Steepest-edge simplex algorithms for linear programming | Mathematical Programming 57(1–3):341–374. Forrest: IBM Research Division, T. J. Watson; Goldfarb: Columbia IEOR. Springer: received 12 Sep 1991, revised 3 Aug 1992, issue May 1992 | DOI 10.1007/BF01581089 (Crossref; DBLP; Springer S12) | 1 of 2 | abstract; reference list | [practice] [stated, joint] P |
| W9 | 1998 | Column generation and the airline crew pairing problem | Documenta Mathematica, Extra Volume ICM 1998, III, 677–686 (EMS Press, open). All three authors: Mathematical Sciences, IBM Research, Yorktown Heights | DOI 10.4171/dms/1-3/65 (Crossref; full text from EMS Press, S31) | 2 of 3 (Anbil, Forrest, Pulleyblank) | in full | [practice] [stated, joint] P |
| W10 | 2002 | A Column Generation Approach for Combinatorial Auctions | in Mathematics of the Internet (IMA Volumes in Mathematics and its Applications), Springer New York, pp. 15–26 | DOI 10.1007/978-1-4684-9277-4_2 (Crossref) | 2 of 2 (Dietrich first) | metadata; reference list | [practice] P |
| W11 | 2005 | CBC User Guide | INFORMS TutORials volume "Emerging Theory, Methods, and Applications" (Sep 2005), pp. 257–277. The web version says its 0.2 of 2 May 2005 was the "Book chapter for CBC Tutorial at INFORMS 2005 annual meeting" (S20) | DOI 10.1287/educ.1053.0020 (Crossref) | 1 of 2 (Lougee-Heimer) | web version in part (S20); chapter not read | [stated, joint] [practice] P |
| W12 | 2006 | A Column-Generation Approach to the Multiple Knapsack Problem with Color Constraints | INFORMS Journal on Computing 18(1):129–134. All three at IBM T. J. Watson | DOI 10.1287/ijoc.1040.0078 (Crossref with abstract; DBLP) | 1 of 3 (Kalagnanam, Ladányi) | abstract | [practice] P |
| W13 | 2006 | IBM Solves a Mixed-Integer Program to Optimize Its Semiconductor Supply Chain | Interfaces 36(5):386–399. Denton: Mayo Clinic; Forrest: IBM T. J. Watson; Milne: IBM Systems and Technology Group | DOI 10.1287/inte.1060.0238 (Crossref with abstract; DBLP 51/5295) | 2 of 3 | abstract | [practice] P |
| W14 | 2006/2007 | Branch and bound, integer, and non-integer programming | Annals of Operations Research 149(1):81–87, online 2 Dec 2006, issue Feb 2007, in the issue "History of Integer Programming: Distinguished Personal Notes and Reminiscences" (guest editors K. Spielberg and M. Guignard-Spielberg). Forrest: IBM Watson, corresponding author; Tomlin: Yahoo! Research | DOI 10.1007/s10479-006-0112-x (Crossref; DBLP; Springer article and issue pages S12) | 1 of 2 | reference list only (subscription) | [stated, joint] P, not read |
| W15 | 2007 | Rapid Development of an Open-source Minlp Solver with COIN-OR | Optima 75 (Mathematical Programming Society newsletter), December 2007, lead article, PDF pp. 1–4; dated "November 2, 2007"; all four authors at IBM T. J. Watson | no DOI; OpenAlex W2607315627; PDF at mathopt.zib.de/Optima-Issues/optima75.pdf (fetched) | 2 of 4 (Bonami, Forrest, Lee, Wächter) | in full | [stated, joint] [practice] P |

### 1.2 Talks, essays, documentation and software

His talks and his one known essay survive only as entries in other texts' reference lists. The code is the main record.

| # | Date | Item | Evidence | Tags |
|---|---|---|---|---|
| T1 | 1987 | "Linear programming using IBM 3090 vector facility", E. M. L. Beale Memorial Symposium, The Royal Society, London | W5's reference list (Crossref, S6) | [practice] P, citation only |
| T2 | Oct 1989 | "Mathematical programming with a library of optimization subroutines", ORSA/TIMS Joint National Meeting, New York | W9, reference [16]: the source W9 gives for Sprint (p. 681) | [practice] P, citation only |
| T3 | 2012 | "Aboca: a bit of Clp accelerated", 21st International Symposium on Mathematical Programming (ISMP 2012) | Huangfu & Hall 2018, reference [4] (S14). The ISMP 2012 site no longer resolves; one WebSearch found nothing (S28) | [observed] S |
| T4 | before 2014 | a talk on the Idiot crash, which he called "a bad talk on it years ago" | relayed by Galabova & Hall (S15, PDF p. 2) from his 2014 Cbc mailing-list post E2 | [observed] S |
| E1 | 2012 | "Never Asked Questions", `http://www.fastercoin.com/f2_files/naqs.html` | Huangfu & Hall 2018, reference [5] (S14). The URL now redirects to a domain-sale page; not read (S29) | [observed] S, not reached |
| E2 | Mar 2014 | Cbc mailing-list post "[cbc] coinstructuredmodel crash" | Galabova & Hall, reference [4] (S15). `list.coin-or.org` refused the connection; not read (S29) | [observed] S, not reached |
| D1 | Nov 2003 – Oct 2004 | CLP User's Guide. Authors: John Forrest (IBM Research), David de la Nuez (Columbia University & IBM Research), Robin Lougee-Heimer (IBM Research); "Copyright: 2004 IBM Corporation". Versions 0.1 (Nov 2003) to 0.4 (18 Oct 2004); Markdown since 6 Mar 2019 | coin-or.org/Clp/ and /Clp/revhist (S19) | [stated, joint] [practice] P |
| D2 | Apr 2005 – Jun 2006 | CBC User's Guide (web; W11 is its 2005 book form). Authors: John Forrest, Robin Lougee-Heimer. Its FAQ holds answers signed "(JF 04/01/05)" to "(JF 06/15/06)" | coin-or.org/Cbc/ (= coin-or.github.io/Cbc/), /intro, /faq, /revhist (S20) | [stated] P |
| SW1 | 2002-07-30 – | **Clp.** First commit b42534866981c7939cf699bbc719338c76ceda87, "Adding Clp to development branch": 38 files, 14,913 lines, including dual and primal simplex, Dantzig and steepest-edge pivot classes, the non-linear-cost (bound-shifting) class, a stand-alone driver and a unit test. Recent release tags run from 1.17.4 (2020-01-31) to 1.17.11 (2026-03-11). Zenodo concept DOI 10.5281/zenodo.2720299 | S21, S24 | [practice] [stated] P |
| SW2 | 2002 – | **CoinFactorization** (CoinUtils): "Authors John Forrest"; Forrest–Tomlin update on by default (`doForrestTomlin_ = true`, CoinFactorization1.cpp line 228). The earliest CoinUtils history is a 2002-11-05 merge by Laci Ladanyi, so the file's creation cannot be dated to a Forrest commit | S22 | [practice] [stated] P |
| SW3 | 2002 – | **Idiot crash** (Clp, added 2002-11-25, commit 3303b30), **Sprint driver** (ClpSolve.cpp, design note first present at commit 91c5447 of 2003-09-19; absent at 2003-09-12), **Volume crash** (Clp 1.00.03, "April 8 2005" in the version log) | S21 | [practice] [stated] P |
| SW4 | 2004-10-29 – | **Sbb → Cbc.** Imported by Laci Ladanyi on 2004-10-29 as "Import of Coin Branch-and-Cut (formerly known as Sbb)"; Forrest's first commit "version 0.7" the same day. Dynamic pseudo-costs started by Forrest 2005-05-19; linked ordered sets (CbcLinked) 2006-12-01. Releases to 2.10.13 (2026-03-11). Zenodo concept DOI 10.5281/zenodo.2720283 | S23, S24 | [practice] [stated] P; shared code (§1.10) |
| SW5 | 2009 | **CoinOslFactorization**: "Copyright (C) 1987, 2009, International Business Machines"; "Authors John Forrest"; commits "osl" (2009-07-18) and "adding osl" (2009-11-05); Clp version log "1.11.00 November 5 2009 (Guy Fawkes) - OSL factorization and better ordering" | S21, S22 | [practice] P; a port (§1.10) |
| SW6 | 2012-08-30 – | **Abc / Aboca** (Clp's `Abc*` files): first commit dd95a067, "minor changes to implement Aboca"; 56 files in Clp's `src/` (the `Abc*` and `CoinAbc*` families) carry "Copyright (C) 2012, FasterCoin"; "Authors John Forrest" | S21 | [practice] [stated] P |
| SW7 | 2020-05-12 – 2026-10-24 | **Maintenance under `jjhforrest`**: Clp 187, Cbc 263 (one of them under a GitHub noreply address), CoinUtils 76 commits on master (§1.9) | S21–S23 | [practice] P |

### 1.3 Unverified leads (not counted)

- **Two MIP-heuristic reports.** Semantic Scholar lists "Pivot-and-Fix; A Mixed Integer Programming Primal Heuristic" (2009; M. Namazifar, R. Lougee-Heimer, J. J. H. Forrest; CorpusId 7320007) and "Randomized Rounding: A Primal Heuristic for General Mixed Integer Programming Problems" (2013; Namazifar, Lougee-Heimer, A. J. Miller, Forrest; CorpusId 15776028), with no venue and no DOI. Their open-access pointers (namazifar.com) now redirect to a home page (S5). They stay leads. The code they describe is real: Cbc's `CbcHeuristicPivotAndFix` and `CbcHeuristicRandRound` were created 2008-09-05 (stubs by Forrest: "adding dummy heuristic", "allow pivot and fix or randomized rounding"; stub and "guts" by Robin Lougee, 2008-09-05 to 2008-09-12). The guts files contain "Todo: Ask JJHF what this for." [practice] P (S23).
- **"J. Forrest and J. Lee (in preparation)"**: W15's reference 16, cited for "a method using linked ordered sets" that remodels a subclass of MINLP as MILP (PDF p. 2). No such paper appears in DBLP, OpenAlex or Semantic Scholar. Code with that aim exists: Cbc's `CbcLinked` (OsiSolverLink), first commit by Forrest 2006-12-01, "for quadratic integer etc" (S23). [inferred] The paper was never published.
- **Excluded**: the 2000 civil-engineering article in Semantic Scholar's profile (§0); all records of DBLP 51/5295 except W13.
- **Not found anywhere**: a sole-authored paper; any arXiv paper ("Forrest, John" returns no results, S9); any Optimization Online entry (S10); a Google Scholar profile (login redirect, not used, S8); an ORCID; a current homepage.

### 1.4 Topics by five-year period

| Period | Place (evidence) | Topics | Output |
|---|---|---|---|
| 1970–1974 | Scientific Control Systems Ltd (Scicon), Milton Court, London (W1, W2) | Sparse LU basis updating in a product-form code (W1); branch-and-bound devices for client MIPs in the UMPIRE system (W2) | W1, W2 |
| 1975–1979 | Scicon, Milton Keynes (W3) | Special ordered sets as a route to global optimization of separable nonconvex problems (W3, W4) | W3, W4 |
| 1980–1986 | not established | No indexed publication. The COIN-OR Cup citation names him "a developer of Alligator, Umpire, Sciconic, MPSX370, OSL" without dates [observed] (S18). The move to IBM is not dated by any source read here | none |
| 1987–1994 | IBM T. J. Watson Research Center (W5, W8) | LP on the IBM 3090 vector facility (T1, W5); OSL's simplex and interior-point codes (W6, W7); steepest edge (W8); Sprint (T2) | T1, T2, W5–W8 |
| 1995–1999 | IBM Research, Mathematical Sciences (W9) | A parallel simplex code "in the mid 90's", unpublished, later simplified into CoinFactorization (§3); airline crew pairing by column generation, Sprint and the Volume crash (W9) | W9 |
| 2000–2004 | IBM Research; COIN-OR "originally founded by IBM in 2000" (W15 PDF p. 1) | Clp (2002), Idiot (2002), the Sprint driver (2003), CLP User's Guide (D1); combinatorial auctions (W10); Sbb renamed Cbc (2004) | W10, D1, SW1–SW4 |
| 2005–2009 | IBM T. J. Watson at least to 2 Nov 2007 (W15); files created in 2008 still carry IBM copyright (S21, S23) | CBC User Guide (W11, D2), Cbc 1.0 (2005), dynamic pseudo-costs, linked ordered sets; MIP and column-generation applications (W12, W13); the history piece (W14); Bonmin (W15); OSL factorization port (2009) | W11–W15, SW4, SW5 |
| 2010–2014 | "FasterCoin" copyright on the 2012 Abc files; the fastercoin.com essay (E1) | Parallel dual simplex Abc/Aboca (SW6, T3); Idiot discussed on the mailing list (E2) | T3, E1, E2, SW6 |
| 2015–2019 | not established | Code maintenance; he committed Omer and Towhidi's positive-edge code to Clp ("add PE code", 2015-06-25) | code only |
| 2020–2026 | GitHub account `jjhforrest`; Cbc README: "now retired from IBM Research" | Maintenance and tuning of Clp, Cbc and CoinUtils (§1.9) | code only |

[inferred] Two threads run through the whole record: the simplex engine (W1 → W5–W8 → CoinFactorization, Clp, Abc) and MIP devices for structured client models (W2–W4 → W9–W13 → Cbc). Every published paper after 1992 is an application or an overview; the algorithmic work after 1992 lives in code.

### 1.5 Author position: alphabetical everywhere, so position carries no signal

- [practice] All 15 author lists are in alphabetical order: Forrest/Tomlin (W1, W5–W7, W14), Forrest/Hirst/Tomlin (W2), Beale/Forrest (W3, W4), Forrest/Goldfarb (W8), Anbil/Forrest/Pulleyblank (W9), Dietrich/Forrest (W10), Forrest/Lougee-Heimer (W11), Forrest/Kalagnanam/Ladányi (W12), Denton/Forrest/Milne (W13), Bonami/Forrest/Lee/Wächter (W15).
- [inferred] The OpenAlex "first / last" counts in S7 (e.g. "4 / 0" first-author papers in 1990–1994) reflect the alphabet, not roles. No first-to-last-author shift can be read from his record, and no supervising (last-author) pattern exists.
- [practice] Springer names him corresponding author of W14 ("Correspondence to J. J. H. Forrest", S12). No other corresponding-author information was seen.
- [practice] He has no sole-authored paper in any index. His sole-authored outputs are code (SW1–SW7), talks (T1–T4), one web essay (E1), mailing-list posts (E2) and signed FAQ answers (D2).

### 1.6 Collaboration network and students

- **John A. Tomlin**: six papers over 35 years (W1, W2, W5, W6, W7, W14) [practice]. In Clp, `ClpPdco.hpp` names "John Tomlin" as author and `ClpInterior.hpp` names "John Tomlin (pdco)" next to "John Forrest (standard predictor-corrector)" [practice] (S21). Bixby: OSL was "developed primarily by John Forrest and John Tomlin" (S16 p. 113) [observed].
- **E. M. L. (Martin) Beale**: W3, W4, both at Scicon. Bixby: "Among those who worked with Beale and were influenced by his vision of mathematical programming were R. E. Small and Max Shaw, followed by John Tomlin and John Forrest, both of whom continue to influence the field to this day." (S16 p. 109) [observed].
- **J. P. H. Hirst** (British Petroleum): W2 [practice].
- **Donald Goldfarb** (Columbia): W8 [practice].
- **IBM Research colleagues**: Ranga Anbil and William R. Pulleyblank (W9); Brenda Dietrich (W10); Jayant Kalagnanam and Laszlo Ladányi (W12); Brian T. Denton and R. John Milne (W13); Pierre Bonami, Jon Lee and Andreas Wächter (W15); Robin Lougee-Heimer (W11, D1, the 2008 Cbc heuristics); David de la Nuez (D1) [practice].
- **Code co-maintainers of Cbc** (S23): Cbc's AUTHORS file ("last been updated on Feb 10, 2020") lists "Forrest, John J.", "Hafer, Lou", "Goncalves, Joao P.: Diving heuristics", "Santos, Haroldo G.: MIPStart, Conflict Graphs related code" and "Brito, Samuel S.: Conflict Graphs related code". The README names the current managers as John Forrest, Ted Ralphs, Stefan Vigerske and Haroldo Gambini Santos [observed].
- **Students**: none documented. He worked in industry throughout; no thesis acknowledgement was searched (agent 04). Leads only: Mahdi Namazifar (§1.3) and David de la Nuez (D1).

### 1.7 Usual venues

- Journals: Mathematical Programming (W1, W3, W8), Management Science (W2), Annals of Operations Research (W5, W14), IBM Systems Journal (W6, W7), INFORMS Journal on Computing (W12), Interfaces (W13).
- Book chapters and proceedings: Towards Global Optimization 2 (W4), ICM 1998 (W9), IMA Volumes (W10), INFORMS TutORials (W11).
- Newsletter: Optima (W15).
- Talks at ORSA/TIMS, a Royal Society memorial symposium and ISMP (T1–T3).
- Absent: arXiv, Optimization Online, Mathematical Programming Computation, SIAM journals, conference proceedings. Documentation is published as web user guides and code (D1, D2, SW1–SW7).

### 1.8 Citation counts and most-cited works (fetched 2026-11-05)

| Work | Crossref | Semantic Scholar (influential) | OpenAlex (S7) |
|---|---|---|---|
| W3 Beale–Forrest 1976, SOS global optimization | 222 | 299 (13) | 276 |
| W1 Forrest–Tomlin 1972 | 169 | 224 (15) | 218 |
| W8 Forrest–Goldfarb 1992 | 146 | 235 (17) | 203 |
| W11 CBC User Guide 2005 | 125 | not in his S2 profile | not in his OpenAlex list |
| W2 UMPIRE 1974 | 103 | 157 (4) | 143 |
| W13 IBM supply chain 2006 | 49 | 55 (1) | 51 |
| W12 MKCP 2006 | 24 | 36 (3) | 28 |
| W5 vector processing 1990 | 20 | 34 (2) | 33 |
| W6 OSL simplex 1992 | 20 | 37 (3) | 31 |
| W9 ICM 1998 | 12 | 80 (6) | 60 |
| W7 OSL interior point 1992 | 10 | 28 (0) | 25 |
| W14 history piece 2006/07 | 10 | 19 (0) | 17 |
| W10 combinatorial auctions 2002 | 6 | 10 (0) | 10 |
| W15 Optima 2007 | — | 4 (0) | 4 |

- [observed] The three most-cited papers are the 1970s–1992 algorithm papers W3, W1 and W8. They are cited as methods (Bixby 2012 credits W1, W2 and W8; Huangfu & Hall 2018 build on W1 and W8; S16, S14).
- [inferred] W11 is cited as "the" reference for Cbc, much as Huangfu & Hall 2018 is cited for HiGHS. Its 125 Crossref citations measure the use of Cbc, not only the chapter. Neither Clp nor Cbc requests a paper citation; both READMEs give only a Zenodo code DOI (S21, S23).
- [observed] Indexes disagree by factors of up to 6.7 on the same work (W9: Crossref 12, Semantic Scholar 80). The counts are useful only for ranking.

### 1.9 Recent works (since November 2024)

- No paper since W15 (December 2007) appears in DBLP, Semantic Scholar, OpenAlex (S7), arXiv or Optimization Online.
- [practice] Commits on master by `jjhforrest` per year (Clp / Cbc / CoinUtils): 2020: 16 / 19 / 9; 2021: 65 / 76 / 11; 2022: 26 / 53 / 26; 2023: 20 / 34 / 7; 2024: 22 / 22 / 6; 2025: 23 / 28 / 11; 2026 to date: 15 / 31 / 6. Latest: Clp 2026-10-22 ("out dubious scaling and safer idiot"), Cbc 2026-10-24, CoinUtils 2026-10-22 (S21–S23).
- [practice] Recent commit subjects show tuning and fixing, often with a measurement attached:
  - Cbc 2026-10-24: "SppGrasp can be Very expensive - so default off". The message carries a profile of the model AIR03 (124 rows, 10,757 binary columns).
  - Clp 2026-05-13: "only check time every 10 iterations - can save 1%!"
  - Clp 2026-10-12: "fix odd lack of finding unbounded (in dual)".
  - CoinUtils 2026-01-04: "Stupidly I left in an assert which was helping debug another bug".
- [practice] Cbc's GitHub releases 2.10.12 (2024-08-20) and 2.10.13 (2026-03-11) were published by Ted Ralphs (GitHub releases API, S25). Clp's tags 1.17.10 and 1.17.11 carry the same dates; who published them was not checked (the GitHub API rate limit was reached).
- [practice] GitHub search (S25) counts 291 issues and PRs commented on by `jjhforrest` and 1 by `johnjforrest`. team.json gives 461 comments, 2017-11-20 to 2026-11-01; that count was not redone here and the comments were not read (agents 02 and 03).

### 1.10 The code record: what is his, what is shared, what is someone else's

Commit counts on master, all identities merged (S21–S23, clones of 2026-11-04):

| Repository | Commits on master | Forrest (both accounts) | Next contributors |
|---|---|---|---|
| Clp | 2,267 | 1,303 (1,116 + 187) | Vigerske 321, Ralphs 225, Haroldo Gambini Santos 110 |
| Cbc | 3,101 | 1,060 (797 + 263) | Haroldo Gambini Santos 807, Ralphs 447, Vigerske 325 |
| CoinUtils | 1,906 | 533 (457 + 76) | Vigerske 350, Ralphs 280, Ladanyi 184 |

Authorship labels, kept as team.json requires:
- **Clp is his, but not all of it.**
  - Of 200 source files (excluding Attic), 27 have an Authors block. 15 name "John Forrest" alone. `ClpPdco.hpp` names John Tomlin. `ClpInterior.hpp` names "John Tomlin (pdco)" and "John Forrest (standard predictor-corrector)". The 10 `ClpPE*` files name Jeremy Omer, or Jeremy Omer and Mehdi Towhidi (2014–2015), and those files say "See Forrest-Goldfarb paper for algorithm" [practice] (S21).
  - Presolve and other files without an Authors block were not attributed here.
- **CoinFactorization and CoinOslFactorization**: "Authors John Forrest" (S22). The OSL one is a port: "This is ripped off from OSL!!!!!!!!!", under "Copyright (C) 1987, 2009, International Business Machines". Who wrote the 1987 original is not stated.
- **Abc (2012)**: Authors "John Forrest"; copyright "2012, FasterCoin" (S21).
- **Cbc is shared code.**
  - README: "Cbc is developed by John Forrest, now retired from IBM Research, and others." [observed].
  - The 2005 COIN-OR Cup citation calls him "Author of the COIN-OR Linear Program (CLP) solver, the COIN-OR Branch-&-Cut (CBC) solver and components of the COIN-OR Cut Generation Library (CGL)" [observed] (S18).
  - The CBC guide's 2005 introduction: "CBC is an active open-source project led by John Forrest at www.coin-or.org." [stated, joint] (S20).
  - None of Cbc's 224 source files has an Authors block of the Clp kind. Six say "Authors: Cbc development team". `CbcSymmetry.cpp` says "Author:  Jim Ostrowski (the good bits - rest JJHF)". One file names Pietro Belotti (S23).
  - A Cbc part is therefore his only where history shows it. Shown: the 2004 "version 0.7" onward; dynamic pseudo-costs (2005-05-19, "starting dynamic pseudo costs"); CbcLinked (2006-12-01); the stubs of the 2008 heuristics.
  - Not his by the record: diving heuristics (Goncalves), MIPStart and conflict graphs (Santos, Brito), the guts of Pivot-and-Fix and Randomized Rounding (Lougee), symmetry "good bits" (Ostrowski).
- **OSL, LAMPS, UMPIRE, Sciconic, MPSX/370**: no code of his is visible.
  - OSL rests on others' credit (Bixby 2012 p. 113; COIN-OR Cup) and on co-authored papers (W5–W7).
  - His own 2002 notes add a first-person claim about one part of OSL: "I am using the modification of costs which I put in OSL and which was extended by Gill et al." (ClpSimplexDual.cpp, present in the first commit b425348) [stated] (S21).
  - The MIP part of OSL is not attributed to him by any source read.

---

## 2. Signature works (dissection, framework §五)

**Selection.**
- **W1** (1972): his most-cited LP paper. Its update is the default in his own factorization code, and two of the three third-party texts read here name it as a standard.
- **W8** (1992): the paper his code points readers to. The 2002 Clp notes list exactly two references, W8 and W6, both his own, and every steepest-edge class in Clp and Abc says "See Forrest-Goldfarb paper for algorithm". This is the nearest thing in the record to a work he calls most important; he has not ranked his works in any text read.
- **W2 with W3/W4** (1974–78): the origin of his MIP craft. W3 is his most-cited paper in every index.
- **W9** (1998) with Sprint, the Volume crash and Idiot: the turn from product LP code to technique-for-an-application, and one of only two of his papers read in full here (with W15).
- **Clp and Cbc (2002–2026)** with W11 and Abc: the code as the work, from Sbb to retirement.

The labels FM1–FM9 are candidate research methods for Phase 2 to test (§5), not conclusions.

### 2.1 W1 · The Forrest–Tomlin update (1972) and its afterlife in CoinFactorization

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin | **Both authors at Scicon.** Both were at "Scientific Control Systems Ltd., Milton Court, London"; received 9 Sep 1971 (S12). **What it builds on.** The reference list (S6) cites R. H. Bartels (1968), Bartels and Golub (1969), Markowitz (1957), Hellerman and Rarick (1970), Orchard-Hays (1968), and Tomlin's own report "Maintaining a sparse inverse in the simplex method" (Stanford TR 70-15, November 1970). **Where the problem came from is not stated in anything read.** [inferred] It came from the production LP inside Scicon's mathematical programming system, the system W2 calls UMPIRE. W14, the 2006/07 reminiscence, may tell the story but is paywalled | [practice] P; [inferred] |
| Why then | The abstract opens: "In recent years triangular factorization of the basis has greatly enhanced the efficiency of linear programming inversion routines, leading to greater speed, accuracy and a sparser representation." So LU inversion was new in production codes, and the update had to keep pace. [inferred] The 1969–1970 LU papers in the reference list mark the timing | [stated, joint] P; [inferred] |
| Key insight | "This paper describes a new product form method for updating the triangular factors at each iteration of the simplex method which has proved extremely effective in reducing the rate of growth of the transformation (eta) files, thus reducing the amount of work per iteration and the frequency of re-inversion." (abstract) | [stated, joint] P |
| Minimum evidence | "We indicate some of the programming measures required to implement the method and give computational experience on real problems of up to 3500 rows." (abstract). The test problems and comparisons are not known (text not read) | [practice] P |
| Abandoned paths | Not documented (text not read). **In his own later code the older product form survives as a switch, and he mocks its use.** CoinFactorization: "true if Forrest Tomlin update, false if PFI", default true (S22). Clp's parameter help: "By default clp uses Forrest-Tomlin L-U update.  If you are masochistic you can switch it off." (CbcOrClpParam.cpp line 3434, S21). **The factorization's own history is one of simplification.** "This class started with a parallel simplex code I was writing in the mid 90's.  The need for parallelism led to many complications and I have simplified as much as I could to get back to this." (CoinFactorization.hpp, lines 27–29). "I have taken out all outer loop unrolling, dense matrix handling and most of the book-keeping for slacks." (lines 36–38) | [stated] P (code) |
| Reception | **Counts.** Crossref 169; Semantic Scholar 224 (15 influential). **Bixby (2012)** lists among the early-1970s ideas "the use of sophisticated LU-updates, based upon the Forrest-Tomlin [18] variant of the Bartels-Golub [3] update" (S16 p. 110). **Huangfu and Hall (2018):** "The standard choices are the relatively simple product form (PF) update [20] or the efficient Forrest-Tomlin (FT) update [7]." (S14 p. 125). Their "collective Forrest-Tomlin (CFT) update" extends it (p. 126) | [observed] P |
| Method it shows | FM2: keep the efficient variant as default and the simple one as a switch. FM4: re-implement the core kernel for each machine and code generation. The chain UMPIRE → OSL → mid-90s parallel code → CoinFactorization is [inferred]; only the last two links are documented, in his own comment | [inferred] |

### 2.2 W8 · Steepest-edge simplex algorithms (1992), with the OSL papers W5–W7

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin | **Two lines meet in the reference list (S6).** Forrest was at the IBM Research Division, T. J. Watson Research Center, and Goldfarb at Columbia IEOR (S12). The list cites Goldfarb's steepest-edge line (Goldfarb 1976; Goldfarb and Reid 1977) and Harris's Devex (1973), next to Forrest's implementation line: W1, W5, W6, and IBM's "Optimizing subroutine library guide and reference" (1991). **The division of roles is not stated in anything read.** [inferred] Goldfarb brought steepest-edge theory and Forrest brought the OSL implementation and the large test models | [practice] P; [inferred] |
| Why then | **OSL was being engineered across hardware generations.** W5: "Preliminary computational results of experiments on the IBM 3090 vector facility will be presented." (abstract). W6: "In this paper we describe the simplex algorithm and briefly discuss the interaction of the detailed implementation of the algorithm with the changes in computer hardware over the last 30 years." and "For the later RISC System/6000™ implementation, it was necessary to rethink this yet again." (abstract via S7). **Bixby dates the context:** "The period around 1990 was a remarkably active period in LP." (S16 p. 113). [inferred] The timing came from a production code that needed better pricing on large real models. The papers do not say so (texts not read) | [stated, joint] P; [observed] P; [inferred] |
| Key insight | "We present several new steepest-edge simplex algorithms for solving linear programming problems, including variants of both the primal and the dual simplex method. These algorithms differ depending upon the space in which the problem is viewed as residing, and include variants in which this space varies dynamically." (abstract) | [stated, joint] P |
| Minimum evidence | **Real, large test models.** Comparisons "on truly large-scale realworld linear programs with as many as tens of thousands of rows and columns." **The claim:** "These results demonstrate unambiguously the superiority of steepest-edge pivot selection criteria to other pivot selection criteria in the simplex method." (abstract). The test set and timings were not read | [practice] P |
| Abandoned paths | Not documented in anything read. **In Clp (2002), steepest edge is one pricing choice among several, chosen per problem:** "B) Which outgoing variable to choose is a virtual base class. For difficult problems steepest edge is preferred while for very easy (large) problems we will need partial scan." (b425348, ClpSimplexDual.cpp). **The same notes record unfinished business:** "a) Better recovery procedures.  At present I never check on forward progress." and "At present we never check we are going forwards.  I overdid that in OSL so will try and make a last resort." | [stated] P (code) |
| Reception | **Counts.** Crossref 146; Semantic Scholar 235 (17 influential). **Bixby (2012)** lists "The development of dual steepest-edge algorithms (using a variant proposed in [16])" among the most important advances in CPLEX and OSL around 1990 (S16 p. 113; [16] = W8). **Huangfu and Hall (2018):** "The first is the dual steepest-edge (DSE) algorithm [6] which chooses the basic variable with greatest weighted infeasibility as the leaving variable." (S14 p. 123) and "In modern revised simplex implementations, the DSE and BFRT are together regarded as the best pivotal rules" (p. 125). **Metadata oddity:** Springer gives "Revised: 03 August 1992" after the "Issue date: May 1992" (Contradictions) | [observed] P |
| Self-reference in code | The 2002 notes end "References:" with "Forrest and Goldfarb, Steepest-edge simplex algorithms for linear programming - Mathematical Programming 1992" and "Forrest and Tomlin, Implementing the simplex method for the Optimization Subroutine Library - IBM Systems Journal 1992", plus Gill, Murray, Saunders and Wright (1988). The same references are repeated in Abc (2012). `ClpDualRowSteepest.hpp` and `ClpPrimalColumnSteepest.hpp` say "See Forrest-Goldfarb paper for algorithm" (lines 12–13 in 2002; 15–16 now). At master, the dual steepest-edge weight update also carries the basis update: "Also does FT update" (ClpDualRowSteepest.hpp line 29) | [stated] [practice] P |
| Method it shows | FM1: the method lives in a production code (OSL, then Clp) and the paper documents it. FM4: re-engineer for each hardware generation. FM8: judge on large real models. FM2: pricing as a swappable class | [inferred] |

### 2.3 W2 · UMPIRE (1974), with Beale–Forrest W3 (1976) and W4 (1978): the MIP craft at Scicon

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin | **A consultancy, an oil company and a production MP system.** Forrest at Scicon Ltd., Hirst at British Petroleum, Tomlin "Presently affiliated with Stanford University" (Crossref, S6). The methods are "implemented in the UMPIRE mathematical programming system" (abstract). **Lineage, per Bixby:** Beale's group at Scicon, "followed by John Tomlin and John Forrest" (S16 p. 109). [inferred] The problems came from Scicon's and BP's client models; the abstract speaks of "the nontrivial integer programming problems we encounter" | [practice] P; [observed] P; [inferred] |
| Why then | **First-generation codes.** Bixby: "The first generation of these new codes, developed and/or released around 1970, included FMPS [40], UMPIRE [17], MPSX [5], MPS III, and APEX." (S16 p. 111). **Integration into a full MP system was the enabler.** W3's abstract on W2: "Forrest, Hirst and Tomlin [3] show how they have benefitted from the vast improvements in branch and bound integer programming capabilities over the last few years, as a result of being incorporated in a general mathematical programming system." | [observed] P; [stated, joint] P |
| Key insight | **Sort the client's problems into classes first, then choose search devices for each class.** "We have found that the nontrivial integer programming problems we encounter tend to fall into two classes." The first class: "The first class of problems is characterized by a relatively small number (less than 100) of binary integer variables embedded in a very large and difficult linear program, with a few thousand constraints and complex matrix structure." For that class, "a number of heuristic estimation procedures are used to guide the branch and bound search". The abstract names priorities, the best projection criterion and pseudo-costs as the most important devices, useful also for the second class "where it is important to reach a good solution quickly to limit the search" (abstract). **W3 extends the system's device set.** Special ordered sets are used for global optimization of separable nonconvex problems: "Special Ordered Sets, introduced by Beale and Tomlin [1], have lived up to their early promise of being useful for a wide range of practical problems." (W3 abstract) | [stated, joint] P |
| Minimum evidence | "give details of computational experience with these methods" (W2 abstract); the tables were not read. W3: received November 1973, revised May 1975 (S12); text not read | [practice] P |
| Abandoned paths | **One rejected approach is stated.** The abstract says the first class of problems does not behave well under a simple-minded penalty approach "for reasons we will make clear", which is why heuristic estimates guide the search (paraphrase of the abstract). Nothing else is documented | [stated, joint] P |
| Reception | **Counts.** W2: Crossref 103, Semantic Scholar 157. W3: Crossref 222, Semantic Scholar 299, his most-cited paper. **Bixby (2012)** credits the era with "the important notion of pseudo-costs, still heavily in use today" (S16 p. 110). He dates "SCICONIC around 1976, an improved version of UMPIRE" (p. 111). His verdict on the whole generation: "However, the dominance of these codes also led to stagnation in the field." (p. 115). **His own retrospective:** W14 (2006/07, a reminiscence co-written with Tomlin) cites W2, W3, W4, and Beale's and Tomlin's ordered-set papers, among them Beale and Daniel (1979) "Chains of Linked Ordered Sets" (S12 reference list); its text was not read | [observed] P |
| Afterlife in his code | **The 1970s devices reappear in Cbc** [practice] (S23): dynamic pseudo-costs ("starting dynamic pseudo costs", Forrest, 2005-05-19); special ordered sets (`CbcSOS`); lot sizing (`CbcBranchLotsize`, already in the 2004 import); linked ordered sets for quadratic integer models (`CbcLinked`, Forrest, 2006-12-01); follow-on branching (author and date not traced). The follow-on class comment reads: "The idea of this is that in air-crew scheduling problems crew may fly in on flight A and out on flight B or on some other flight." **The SOS line also continued in print:** W15's unpublished "J. Forrest and J. Lee (in preparation)" was cited for "a method using linked ordered sets" (§1.3) | [practice] P |
| Method it shows | FM3: tie search devices to the problem class seen in client models. FM8: classify real problems before designing the method. FM6: client problems drive general system features | [inferred] |

### 2.4 W9 · Sprint, the Volume crash and Idiot: LP for models with very many columns (1989–2005)

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin | **The co-authored chapter credits him, citing a talk.** "John Forrest[16] introduced the so-called Sprint method." (W9 p. 681); [16] is his October 1989 ORSA/TIMS talk (T2). **His own account (Clp, 2003):** "This driver implements what I called Sprint when I introduced the idea many years ago.  Cplex calls it "sifting" which I think is just as silly." He goes on: "When I thought of this trivial idea it reminded me of an LP code of the 60's called sprint which after every factorization took a subset of the matrix into memory (all 64K words!) and then iterated very fast on that subset." (ClpSolve.cpp lines 2493–2498; first present 2003-09-19). **Cbc's parameter documentation, in the third person:** "The idea as 'Sprint' was introduced by J. Forrest after an LP code of that name of the 60's which tried the same tactic (not totally successfully). CPLEX calls it 'sifting'." (doc/cbc-parameters.md line 2139; who wrote this help text is not established) | [stated, joint] P; [stated] P (code); [observed] P |
| Why then | **The models.** Crew-pairing LPs have "several hundred rows (one for each flight to be covered) and many millions of columns" (W9 p. 679). The example is an American Airlines problem with 837 flights and 5.5 million feasible pairings, solved with "IBM's OSL Primal, Dual and Sprint", and "All times are minutes of solution time on a S/390 (in 1989)." (p. 681). **The fit, in his words:** the 1960s code "worked very well on aircrew scheduling problems where there were very large numbers of columns all with the same flavor." (ClpSolve.cpp lines 2499–2501) | [stated, joint] P; [stated] P |
| Key insight | **Sprint (W9 p. 681).** "It begins by solving the linear program obtained by keeping a small subset of the columns and then uses the optimal dual variables to price out all columns of the original problem." Columns are chosen "by first bucketing the columns based on the reduced cost, adding the columns in the best buckets, plus a random selection of columns from other buckets." **In Clp:** "The idea works best if you can get feasible easily.  To make it more general we can add in costed slacks" (ClpSolve.cpp lines 2504–2505). **Idiot crash, his framing:** "It is based on the idea that algorithms with terrible convergence properties may be okay at first." (Idiot.hpp lines 40–41) | [stated, joint] P; [stated] P |
| Minimum evidence | **Sprint.** The p. 681 table compares OSL primal, dual and Sprint iterations and minutes on growing column subsets, starting at 5,000 pairings. The extracted table layout is garbled, so its numbers are not used here. "Note that even though the number of Sprint iterations grows rapidly, they are performed very quickly, enabling our low solution times." **Volume crash.** On US Airways and Southwest Airlines problems (RS6000/590): "Using the Volume algorithm dual solution to crash the dual simplex is, on average, nine times faster than the dual simplex algorithm and two times faster than the interior method." (p. 684). **Use in practice:** "The methods we have described here are used successfully by several airlines to solve their monthly crew planning problems." (p. 684) | [practice] P |
| Abandoned paths and negative results | **The 1960s ancestor:** "On the problems of those days it did not work very well" (ClpSolve.cpp lines 2498–2499). **Primal simplex dropped for these models:** "We did not consider the primal simplex algorithm, since it performs very poorly for these problems." (W9 p. 684). **Simplex duals rejected for pricing in column generation:** "However, those used by the simplex algorithm tend to be very sparse, and do not work as well." (p. 684). **Idiot, self-deprecated:** "This class implements a very silly algorithm.  It has no merit apart from the fact that it gets an approximate solution to some classes of problems." Also: "It can also be used as a "crash" to get a problem started.  This is probably its most useful function." (Idiot.hpp lines 31–38). He reportedly gave "a bad talk on it years ago" (relayed, S15 PDF p. 2) | [stated] P; [stated, joint] P; [observed] S |
| Reception | **Counts.** W9: Crossref 12, Semantic Scholar 80. **Volume crash moved into Clp in 2005:** "1.00.03 April 8 2005.  Added Volume algorithm as crash and made code more robust on testing." (ClpMain.cpp line 322). **Idiot's first analysis came 16 years after the code.** Galabova and Hall (arXiv 1804.09172, 2018): "This paper provides the first meaningful documentation and analysis of an established technique which aims to obtain an approximate solution to linear programming problems prior to applying the primal simplex method." (abstract). They report that "for several test problems used in the Mittelmann benchmarks [11], Clp is significantly faster than at least one of the three major commercial solvers (Cplex, Gurobi and Xpress), and experiments in Section 3.2 show that the Idiot crash is a major factor in this relative performance." (PDF p. 2). **They correct his description:** "Although Forrest states that the Idiot crash minimizes a multiple of the LP objective plus a sum of squared primal infeasibilities [4], a more general quadratic function of constraint violations is minimized." (PDF p. 3) | [observed] P; [stated] P |
| Method it shows | FM3: exploit the shape of an application's models (few rows, millions of similar columns). FM6: the application yields a general solver option (Sprint, Volume and Idiot crashes in Clp). FM5: honest self-deprecation, and saying in the code what is undocumented or unsure. FM1: code first, paper (by others) later | [inferred] |

### 2.5 Clp and Cbc (COIN-OR, 2002–2026), with W11 and Abc (2012): the code as the work

| Dimension | Finding | Tags / sources |
|---|---|---|
| Origin | **Clp.** First commit 2002-07-30, 38 files (§1.2). COIN-OR was "originally founded by IBM in 2000 and a non-profit foundation since 2004" (W15 PDF p. 1). **Cbc, in his signed answer.** "SBB stands for Simple Branch and Bound. When COIN-OR LP was being written, the Osi interface demanded an integer solver. An exception could have been thrown but anyone can write a branch and bound code in a day. With Strong Branching it was 460 lines of code, without 300 lines. Somehow the code kept growing and eventually it was moved it to its own project." (Cbc FAQ, "(JF 06/03/06)", S20). The renaming followed name confusion with GAMS's SBB; the code "was frozen as of Halloween 2004" (same answer). The repository import is dated 2004-10-29 (S23) | [stated] P; [stated, joint] P; [practice] P |
| Why then | **Version 1.0.** "Version 1.0 was released in time for the 2004 INFORMS Annual Meeting (24-27 October, 2004)." (Clp FAQ, "(DN 08/27/04)", S17); the Clp version log starts "Version 1.00.00 October 13 2004." (ClpMain.cpp line 317). **The Cbc driver and a benchmark competition.** The 2004 Cbc README says "While the competition is on no work is being done on the cbc driver." and describes `sample2.cpp` as "the benchmark driver for the competition" (eeaed1e README). Which competition is not stated [gap]. No source read says why IBM had him write a new open-source simplex code in 2002 while it sold OSL [gap] | [observed] P; [stated] P; [inferred] |
| Key insight (design stance) | **Clp's dual design (2002 notes).** "OSL did not have a phase 1/phase 2 approach but instead effectively put fake bounds on variables and this is the approach here, although I had hoped to make it cleaner." And on the ratio test: "C) Sounds easy, but this is hardest part of algorithm." Bound flipping is already in view: "These mini iterations can increase speed by orders of magnitude but we may need to go to more of a bucket choice of variable rather than looking at them one by one (for speed)." **Readability over speed, as a colleague put it:** "The design criteria were for it not to be too slow. Some speed has been sacrificed to make the code less opaque OSL (not difficult!)." (Clp FAQ, "(DN 08/27/04)", S17). **Cbc's stance (signed JF):** to "Is CBC as fast as Cplex or Xpress?" he answers "No. However its design is much more flexible so advanced users will be able to tailor CBC to their needs." (04/01/05) | [stated] P; [observed] P |
| Minimum evidence | **2002 README:** "It can do a unit test and solve netlib problems." and "I do not guarantee that it will solve all netlib if you get too creative." **Robustness (Clp FAQ, S17):** "CLP has been tested on many problems of up to 1.5 million constraints and has shown itself as reliable as OSL." ("(DN 09/07/04)"). **Cbc's out-of-box speed, signed JF:** "It is not very fast out of the box, but is very flexible so it can be very effective with correct use of cut generators and heuristics." (06/15/06) | [stated] P; [observed] P |
| Abandoned paths | **The mid-1990s parallel simplex code** was "simplified" into CoinFactorization (§2.1). **The name Sbb** was frozen in 2004. **OSL's progress checks**, which he says he "overdid", became a last resort in Clp (§2.2). **Abc/Aboca (2012)** was never written up: "Other than making the source code available [5], the authors believe that there is no published reference to this work." (Huangfu & Hall, S14 p. 124). In Clp it stays an option, "Whether to visit Aboca" (CbcOrClpParam.cpp line 1655). **Linked ordered sets** (2006 code; "in preparation" in 2007) did not reach print (§1.3). **Heuristics kept private:** "I need to publish some more heuristic methods as I have several I use for my own work which at present are too problem specific." (Cbc FAQ, JF 05/24/06) | [stated] P; [observed] P; [inferred] |
| Reception | **COIN-OR INFORMS Cup 2005** (inaugural; S18). The citation names him "Founding Benevolent Dictator of COIN-OR" and says: "But particularly notable is John's ability to close the loop — using difficult real-world problems to drive the development of software tools that have wide applicability and availability as high-quality open-source libraries, while still having the focus and timeliness to have substantial impact on the original problems." **Co-authors in 2007:** "Cbc (Coin Branch and Cut) is a powerful, industrial-strength branch-and-cut code for MILP problems." (W15 PDF p. 2). **Huangfu and Hall (2018):** Clp 1.15 is "the world's leading open-source solver" (S14 p. 134) and "Clp, the best open-source simplex solver" (p. 140). Of Aboca: "Based on the little evidence available, Aboca needs an additional (partial) btran operation which is not necessary in sip" (p. 132). **Citations:** W11 has 125 (§1.8) | [observed] P; [stated, joint] P |
| Record-keeping | **The Clp version log (ClpMain.cpp lines 317–335) is terse and candid.** "1.03.01 May 24 2006.  Lots done but I can't remember what!" and "1.04.01 June 26 2007.  Lots of changes but I got lazy". The log stops at "1.11.00 November 5 2009 (Guy Fawkes) - OSL factorization and better ordering" | [stated] P |
| Method it shows | FM7: start with the smallest code that satisfies an interface, then let it grow. FM1: code as the primary publication. FM5: candour about limits in user-facing text. FM6: close the loop from applications (W9–W13) to general libraries (S18 citation). FM9: maintain your own code for decades, with dated, measured, small changes (§1.9) | [inferred] |

---

## 3. Failures, slowdowns, abandoned directions (consolidated)

1. **Parallel simplex, mid-1990s.** "The need for parallelism led to many complications and I have simplified as much as I could to get back to this." (CoinFactorization.hpp lines 27–29). No paper or released code from it was found. [stated] P; [inferred] unpublished.
2. **Over-engineering in OSL, by his own account.** "I overdid that in OSL so will try and make a last resort." (2002 Clp notes, ClpSimplexDual.cpp line 214 at master). [stated] P
3. **The dual's fake-bound design is not as clean as he wanted.** "although I had hoped to make it cleaner" (2002 notes). [stated] P
4. **Unfinished points listed in the 2002 notes**:
   - "At present I never check on forward progress."
   - On free variables: "I am undecided about free variables - there is coding but I am not sure about it."
   - On cost modification: "I am still not sure of the exact details."

   [stated] P
5. **Sprint's 1960s ancestor** "did not work very well" on the problems of its day; the Cbc docs say "not totally successfully". [stated] P; [observed] P
6. **Negative results in W9 (p. 684):**
   - primal simplex "performs very poorly" on crew-pairing LPs;
   - simplex duals "do not work as well" for column generation.

   [stated, joint] P
7. **Idiot**:
   - "a very silly algorithm" with "no merit" beyond approximate solutions;
   - "a bad talk on it years ago" (relayed);
   - undocumented for 16 years, until Galabova and Hall (2018), whose analysis corrects his stated objective (S15 PDF p. 3).

   [stated] P; [observed] P
8. **Unpublished work**:
   - Aboca (2012), per Huangfu & Hall p. 124;
   - Forrest and Lee on linked ordered sets ("in preparation", 2007);
   - "more heuristic methods" kept for his own work (2006);
   - the 2008 Pivot-and-Fix and Randomized Rounding reports, which have no venue.

   [observed] P; [stated] P; [inferred]
9. **Cbc's speed, in his own 2005–06 words**: "No" (not as fast as Cplex or Xpress); "not very fast out of the box". [stated] P
10. **Record-keeping lapses**: "Lots done but I can't remember what!" and "Lots of changes but I got lazy" (version log). Cbc's recent GitHub releases were published by Ted Ralphs (S25). [stated] P; [practice] P
11. **Recent self-corrections in commit messages**:
    - "fix my error in racing" (Clp, 2026-05-30);
    - "Apologies - put test in wrong place" (Cbc, 2026-10-06);
    - "Stupidly I left in an assert which was helping debug another bug" (CoinUtils, 2026-01-04).

    [stated] P
12. **Rejected or retracted papers**: none in the public record. W14 and the unread full texts may hold more.

---

## 4. Era and resource context

| Period | Compute | Tools, code base and test material | Team | Seniority |
|---|---|---|---|---|
| 1970–1976 (W1–W3) | not stated in what was read | The UMPIRE mathematical programming system at Scicon; "real problems of up to 3500 rows" (W1); client MIPs with "a few thousand constraints" (W2) | Scicon colleagues (Beale, Tomlin), a BP co-author (Hirst) | early career [inferred] |
| 1987–1992 (T1, W5–W8) | IBM 3090 vector facility (W5, T1); RISC System/6000 (W6) | OSL, IBM's product library; "truly large-scale realworld" LPs (W8); Netlib test problems in W8's references (Gay 1985; Lustig 1989) | IBM Research, with Tomlin at Almaden (W5) and Goldfarb at Columbia (W8) | senior industrial researcher [inferred] |
| 1989–1998 (T2, W9) | S/390 (1989 Sprint table); RS6000/590 (Volume table) | OSL primal, dual and Sprint; American Airlines, US Airways and Southwest Airlines models; a deployed system for several airlines | IBM Research Mathematical Sciences (Anbil, Pulleyblank) | senior |
| 2002–2007 (Clp, Sbb/Cbc, W10–W15) | Linux with g++, Windows with MSVC 6 and cygwin, AIX (Clp FAQ, 2004, S17) | C++ open source under CPL, later EPL, on COIN-OR; Osi and Cgl; Netlib unit tests; MIPLIB-based samples; a 2004 benchmark "competition" | IBM COIN-OR group (Ladanyi, Lougee-Heimer, de la Nuez) and IBM application teams | senior; "Founding Benevolent Dictator" (S18) |
| 2012 (Abc/Aboca) | multi-core; the Abc code has a pthreads mode (`ABC_PARALLEL == 1`, commented "Use pthreads") and Cilk support (`HAS_CILK`, CoinAbcCommon.hpp) | Clp code base; ISMP 2012 talk; a personal web page (E1) | apparently alone, under "FasterCoin" [inferred] | after IBM [inferred] |
| 2020–2026 (`jjhforrest`) | not stated; one 2026 commit is titled "option at compile time to allow many many cpus" (CoinUtils) | GitHub issues and PRs; profiles on named models (e.g. AIR03); Cbc releases published by Ralphs | a small volunteer team (README) | retired |

[inferred] The OSL papers' own framing, hardware changing "over the last 30 years", and the 2012 parallel Abc show a habit of re-engineering the same simplex kernels whenever the machine changes. Until at least late 2007 this work sat inside IBM: OSL as an IBM product, COIN-OR as an IBM initiative, and IBM co-workers on the guides and papers. The Abc files of 2012 and the commits since 2020 come from one person working beside volunteer maintainers.

---

## 5. Pointers into the seven layers (candidate evidence for Phase 2, not conclusions)

- **Layer 1, taste.**
  - A method counts when it is the default in a working code. Evidence: FT is the default, PFI is for the "masochistic"; steepest edge "is preferred" for difficult problems.
  - He is candid about his own techniques: Idiot is "very silly", Sprint "trivial", and "I overdid that in OSL".
  - Negative selection: the paper is not where the work lives. He has no sole-authored paper; Aboca and Idiot went unpublished.
- **Layer 2, problem choice.**
  - Problems come from client and application models: Scicon/BP MIPs (W2); airline crew pairing (W9); steel-industry MKCP (W12); IBM's semiconductor supply chain (W13).
  - Interfaces force problems too: "the Osi interface demanded an integer solver" (Sbb).
  - Hardware changes force problems: the 3090 vector facility, RS/6000, multi-core (W5, W6, Abc).
- **Layer 3, idea generation.**
  - Revive an old idea from memory: the 1960s "sprint" code.
  - Exploit model shape: few rows and very many columns.
  - Accept terrible asymptotics for a good start: Idiot, "algorithms with terrible convergence properties may be okay at first".
  - Simplify after a failed generalisation: the mid-90s parallel code simplified into CoinFactorization.
- **Layer 4, experiment and execution.**
  - Real models of growing size (W9 table).
  - Netlib unit tests shipped with the code (2002 README).
  - Swappable classes for pricing and branching.
  - Measured, small commits in 2026: the AIR03 profile; "can save 1%!".
- **Layer 5, judging results.**
  - Speed relative to commercial codes stated plainly ("No").
  - Self-correcting commit messages.
  - Third parties found his undocumented crash decisive on benchmarks (Galabova and Hall) but described it differently from him.
- **Layer 6, expression.**
  - The design rationale lives in long first-person comment blocks at the top of source files, with "TODO" lists and references.
  - Version logs and FAQ answers are signed and dated.
  - Papers are few, co-authored, alphabetical, and in implementation-oriented venues (IBM Systems Journal, Interfaces, TutORials, Optima).
- **Layer 7, research organisation.**
  - Long partnership with Tomlin (1972–2007).
  - Industrial teams at Scicon and IBM.
  - Founding "Benevolent Dictator" of COIN-OR.
  - Code shared with later maintainers (Ralphs, Vigerske, Gambini Santos).
  - No students documented.

Candidate method labels used above (for Phase 2 verification across agents 02–06):
- FM1 code first; the paper, if any, documents what the production code already does
- FM2 make the efficient variant the default and keep the simple one switchable
- FM3 tie the technique to the shape of an application's models
- FM4 re-engineer the same kernels for each hardware or code generation
- FM5 write candid, dated, first-person notes about limits and unfinished work
- FM6 close the loop from a client problem to a general library option
- FM7 start with the smallest code that satisfies an interface, then let it grow
- FM8 judge on large real models, not on toy sets
- FM9 keep maintaining the code yourself, with small measured changes

---

## Contradictions (kept, not reconciled)

1. **W8 dates (Springer page).** "Received: 12 September 1991 Revised: 03 August 1992 Issue date: May 1992": the revision date falls after the issue date. Not resolved.
2. **W14 year.** 2006 (online 2 Dec 2006; Crossref "issued"; Semantic Scholar and OpenAlex list 2006/2007) vs 2007 (print issue February 2007; DBLP key ForrestT07).
3. **Idiot's objective.** His account, as relayed by Galabova and Hall, is "a multiple of the LP objective plus a sum of squared primal infeasibilities". Their reading of his code: "a more general quadratic function of constraint violations is minimized" (S15 PDF p. 3).
4. **Two wordings of the Sprint note.** In ClpSolve.cpp: "Cplex calls it "sifting" which I think is just as silly." In examples/sprint.cpp (2003): "Cplex calls it "sifting" which is just as silly." The Cbc parameter help puts the same history in the third person ("introduced by J. Forrest").
5. **How good Cbc is.**
   - "No" to "as fast as Cplex or Xpress" and "not very fast out of the box" (JF, 2005–06).
   - "a powerful, industrial-strength branch-and-cut code" (W15, co-signed, 2007).
   - The claims differ in date and audience; neither is measured in the texts read.
6. **Clp's speed and robustness.**
   - The Clp FAQ (DN, 2004, S17): "Some speed has been sacrificed" and "as reliable as OSL".
   - Galabova and Hall (2018): Clp "significantly faster than at least one of the three major commercial solvers" on several Mittelmann problems, because of Idiot.
7. **Who wrote OSL.**
   - team.json: OSL is credit by others, with no code of his visible.
   - Bixby (2012 p. 113): OSL was "developed primarily by John Forrest and John Tomlin".
   - His own 2002 notes claim one part, "the modification of costs which I put in OSL", and say "I overdid that in OSL".
   - Kept as a refined label (§1.10), not a resolution.
8. **Retirement date.**
   - team.json: between 2006 and 2010.
   - In this run: IBM affiliation printed in W15 (dated 2 Nov 2007); files created in 2008 carry IBM copyright; the 2009 OSL port is IBM-copyrighted.
   - The 2012 Abc files carry "FasterCoin" copyright; the README's "now retired" is undated.
   - The evidence here puts retirement after November 2007; nothing here fixes the upper end before 2012.
9. **Name forms**: "John J. Forrest" (W8, W9, W15), "J. J. H. Forrest" (most papers) and "John Forrest" (W11, W13), within the same years.
10. **Index records.**
    - DBLP splits his work across 08/3168 and a mixed 51/5295.
    - Semantic Scholar merges in a civil-engineering article.
    - Citation counts differ by up to 6.7 times (W9).
11. **Cbc on Zenodo vs GitHub.** The latest Zenodo version record is "Release v2.933", dated 2026-08-14. GitHub's latest Cbc release and git tag is 2.10.13 of 2026-03-11, and no v2.933 tag exists in the repository (S24, S25).

## Gaps

- **Full texts.**
  - W1–W3 and W5–W14 were read only as abstracts, metadata or reference lists (subscription access).
  - W14, the 2006/07 first-person history of branch and bound with Tomlin, would supply origins and abandoned paths for §2.1 and §2.3. It was not read.
  - W4 is known only from W14's reference list.
- **Talks and essays.**
  - T1 (1987), T2 (1989), T3 (ISMP 2012) and the Idiot talk: no slides or abstracts found; the ISMP 2012 site does not resolve.
  - E1 ("Never Asked Questions", 2012): the domain is now for sale.
  - E2 and all Clp/Cbc mailing-list posts: list.coin-or.org refused connections.
  - Wayback copies were not used (WebFetch refuses web.archive.org; team.json says not to route around it).
- **Profiles and indexes.**
  - Google Scholar redirects to a login page.
  - No ORCID, homepage or CV found; the IBM page listed by DBLP is gone.
  - OpenAlex was not re-queried (no API key); the scaffold-time harvest (S7) was used.
  - IEEE Xplore (W6, W7) and INFORMS pages (W2, W11, W13; the Wagner page) were blocked or missing.
- **Wagner Prize.** Crossref's abstract of the prize note in the same issue says "The Wagner prize for 2005 goes to IBM, winning over strong competitors." (Interfaces 36(5):383–385, S26). That W13 (pp. 386–399, directly after it) is the winning paper is [inferred] from placement and the team.json lead. No source read names the project.
- **CPLEX reception of W8.** Bixby's Operations Research 2002 paper was not read: fetching its open mirror was refused in this session. The robert-e-bixby agents cover it.
- **Biography** (agent 06):
  - education;
  - start and end at Scicon;
  - the date he moved to IBM;
  - what "FasterCoin" is;
  - the retirement date.
- **Authorship of earlier codes.** Alligator, Sciconic, MPSX/370, LAMPS and OSL's MIP: no primary source on his part. Sbb's history before 2004-10-29 lives in the old COIN-OR repository, not checked.
- **Cbc parts not traced**: the origin of `CbcFollowOn`. Pickaxe searches on the blobless clone were too slow and were stopped.
- **The competition** named in the 2004 Cbc README: not identified.
- **Students and mentees**: none documented (agent 04). The Namazifar items are unverified.
- **GitHub comments** (461 per team.json) were not read here (agents 02 and 03).

## Sources

Primary = his own papers, code and signed texts, his co-authors' texts, publisher records, or third-party papers and code read directly. Secondary = indexes, search results and unreachable pages. All fetched 2026-11-05.

His papers (each DOI resolved with Crossref, S6):
- W1. Forrest, J. J. H., Tomlin, J. A., "Updated triangular factors of the basis to maintain sparsity in the product form simplex method", Mathematical Programming 2(1):263–278, 1972. DOI 10.1007/BF01584548. Primary (abstract).
- W2. Forrest, J. J. H., Hirst, J. P. H., Tomlin, J. A., "Practical Solution of Large Mixed Integer Programming Problems with Umpire", Management Science 20(5):736–773, 1974. DOI 10.1287/mnsc.20.5.736. Primary (abstract).
- W3. Beale, E. M. L., Forrest, J. J. H., "Global optimization using special ordered sets", Mathematical Programming 10(1):52–69, 1976. DOI 10.1007/BF01580653. Primary (abstract).
- W4. Beale, E. M. L., Forrest, J. J. H., "Global Optimization as an Extension of Integer Programming", in Dixon and Szegö (eds.), Towards Global Optimization 2, North-Holland, 1978, pp. 131–149. No DOI; from W14's reference list. Primary (citation only, not read).
- W5. Forrest, J. J. H., Tomlin, J. A., "Vector processing in simplex and interior methods for linear programming", Annals of Operations Research 22(1):71–100, 1990. DOI 10.1007/BF02023049. Primary (abstract, references).
- W6. Forrest, J. J. H., Tomlin, J. A., "Implementing the simplex method for the Optimization Subroutine Library", IBM Systems Journal 31(1):11–25, 1992. DOI 10.1147/sj.311.0011. Primary (abstract via S7).
- W7. Forrest, J. J. H., Tomlin, J. A., "Implementing interior point linear programming methods in the Optimization Subroutine Library", IBM Systems Journal 31(1):26–38, 1992. DOI 10.1147/sj.311.0026. Primary (metadata).
- W8. Forrest, J. J., Goldfarb, D., "Steepest-edge simplex algorithms for linear programming", Mathematical Programming 57(1–3):341–374, 1992. DOI 10.1007/BF01581089. Primary (abstract, references).
- W9. Anbil, R., Forrest, J. J., Pulleyblank, W. R., "Column generation and the airline crew pairing problem", Documenta Mathematica Extra Volume ICM 1998 III:677–686. DOI 10.4171/dms/1-3/65; https://ems.press/books/dms/248/4854 (PDF from content.ems.press). Primary (read in full).
- W10. Dietrich, B., Forrest, J. J., "A Column Generation Approach for Combinatorial Auctions", Mathematics of the Internet (IMA Volumes in Mathematics and its Applications), Springer, 2002, pp. 15–26. DOI 10.1007/978-1-4684-9277-4_2. Primary (metadata).
- W11. Forrest, J., Lougee-Heimer, R., "CBC User Guide", INFORMS TutORials "Emerging Theory, Methods, and Applications", 2005, pp. 257–277. DOI 10.1287/educ.1053.0020. Primary (web version, S20).
- W12. Forrest, J. J. H., Kalagnanam, J., Ladányi, L., "A Column-Generation Approach to the Multiple Knapsack Problem with Color Constraints", INFORMS Journal on Computing 18(1):129–134, 2006. DOI 10.1287/ijoc.1040.0078. Primary (abstract).
- W13. Denton, B. T., Forrest, J., Milne, R. J., "IBM Solves a Mixed-Integer Program to Optimize Its Semiconductor Supply Chain", Interfaces 36(5):386–399, 2006. DOI 10.1287/inte.1060.0238. Primary (abstract).
- W14. Forrest, J. J. H., Tomlin, J. A., "Branch and bound, integer, and non-integer programming", Annals of Operations Research 149(1):81–87, 2007 (online 2 Dec 2006). DOI 10.1007/s10479-006-0112-x. Primary (reference list only).
- W15. Bonami, P., Forrest, J. J., Lee, J., Wächter, A., "Rapid Development of an Open-source Minlp Solver with COIN-OR", Optima 75, December 2007, pp. 1–4 of the PDF. https://mathopt.zib.de/Optima-Issues/optima75.pdf (www.mathopt.org copy returned 404). Primary (read in full).

Indexes, profiles and search:
- S1. DBLP person "John J. H. Forrest", pid 08/3168, 7 records (sparql.dblp.org via `scripts/dblp_works.py`). https://dblp.org/pid/08/3168.html. Secondary.
- S2. DBLP person "John Forrest", pid 51/5295 (mixed record, holds W13). https://dblp.org/pid/51/5295.html. Secondary.
- S3. DBLP name search "John J. H. Forrest" (`dblp_works.py --name`). Secondary.
- S4. Semantic Scholar Graph API: author search and author 33308287 papers (16 items). https://api.semanticscholar.org/graph/v1/author/33308287. Secondary.
- S5. Semantic Scholar paper batch (open-access pointers; abstracts elided). Secondary.
- S6. Crossref REST API records for the 13 DOIs of W1–W3 and W5–W14, and for 10.1680/CIEN.2000.138.2.87, 10.1287/inte.1060.0240 (S26), 10.1287/opre.50.1.3.17780 (S30) and 10.1007/s12532-017-0130-5 (S14): abstracts, affiliations, reference lists, citation counts. https://api.crossref.org/works/. Secondary.
- S7. OpenAlex harvest for author A5061258306 in `references/sources/publications/publications.md` and `abstracts.md` (fetched 2026-11-05 at scaffold time; not re-queried). Secondary.
- S8. Google Scholar author search "John J. H. Forrest": redirected to accounts.google.com login, not used. Secondary.
- S9. arXiv author search "Forrest, John": "produced no results". https://arxiv.org/search/?query=Forrest%2C+John&searchtype=author. Secondary.
- S10. Optimization Online search "Forrest" (no author page; /author/john-forrest/ etc. 404). https://optimization-online.org/?s=Forrest. Secondary.
- S11. The IBM homepage listed by DBLP, http://www.research.ibm.com/people/f/forrest/internet/publications.html: redirects to https://research.ibm.com/people. Secondary (unavailable).
- S12. Springer Nature Link article pages for W1, W3, W5, W8, W14 (dates, affiliations, abstracts, W14 reference list) and the issue page of Annals of Operations Research 149(1). https://link.springer.com/article/10.1007/BF01584548 (and siblings); https://link.springer.com/journal/10479/volumes-and-issues/149-1. Primary (publisher metadata).
- S13. IEEE Xplore pages 5387455 (W6) and 5387456 (W7): HTTP 202 with empty body; WebFetch received empty content. Secondary (unavailable).

Third-party texts:
- S14. Huangfu, Q., Hall, J. A. J., "Parallelizing the dual revised simplex method", Mathematical Programming Computation 10(1):119–142, 2018, CC BY 4.0. DOI 10.1007/s12532-017-0130-5; https://webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf. Primary (third party; pp. 123–126, 132, 134, 140, references).
- S15. Galabova, I. L., Hall, J. A. J., "A quadratic penalty algorithm for linear programming and its application to linearizations of quadratic assignment problems", arXiv 1804.09172v1, 24 Apr 2018. https://arxiv.org/abs/1804.09172. Primary (third party; abstract, PDF pp. 2–3, references).
- S16. Bixby, R. E., "A Brief History of Linear and Mixed-Integer Programming Computation", Documenta Mathematica Extra Volume ISMP (2012) 107–121. https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-ismp/25_bixby-robert.pdf. Primary (observer; pp. 109–111, 113, 115, references).
- S17. Clp FAQ entries signed "DN" (David de la Nuez), 2004. https://www.coin-or.org/Clp/faq.html. Primary (colleague).
- S18. COIN-OR, "COIN-OR Cup 2005 Winners" page, citation headed "John J. H. Forrest" (undated; it refers to the CBC 1.0 release as just occurred). https://www.coin-or.org/coinCup/coinCup2005Winner.html. Primary (observer).
- S19. CLP User's Guide: index (authors, copyright) and revision history. https://www.coin-or.org/Clp/ and https://www.coin-or.org/Clp/revhist. Primary.
- S20. CBC User's Guide: index, Introduction, FAQ (answers signed JF 2005–2006) and revision history. https://www.coin-or.org/Cbc/ (= https://coin-or.github.io/Cbc/), /intro, /faq, /revhist. Primary.

Code (public, EPL):
- S21. coin-or/Clp, https://github.com/coin-or/Clp. Primary (code). Blobless clone; master 8744652 (2026-11-04).
  - First commit b42534866981c7939cf699bbc719338c76ceda87 (2002-07-30): README, ClpSimplexDual.cpp, include/ClpSimplexDual.hpp, include/ClpSimplexPrimal.hpp, include/ClpDualRowSteepest.hpp, include/ClpPrimalColumnSteepest.hpp.
  - Commits 3303b30 (Idiot, 2002-11-25), 2c65c32 and 91c5447 (ClpSolve, 2003-09-12 and 2003-09-19) and dd95a067 (Aboca, 2012-08-30).
  - Files at master: src/ClpSolve.cpp, Idiot.hpp, ClpMain.cpp, ClpSimplexDual.cpp, ClpDualRowSteepest.hpp, AbcSimplex.hpp, ClpPdco.hpp, ClpPE*.hpp, ClpInterior.hpp, ClpPredictorCorrector.hpp, CbcOrClpParam.cpp, ClpParameters.cpp, and examples/sprint.cpp.
  - Commit statistics by author and year.
- S22. coin-or/CoinUtils, https://github.com/coin-or/CoinUtils. Primary (code). Master 231b801 (2026-10-31): src/CoinFactorization.hpp, CoinFactorization1.cpp and CoinOslFactorization.hpp/.cpp, plus the history.
- S23. coin-or/Cbc, https://github.com/coin-or/Cbc. Primary (code). Master 001b861 (2026-11-04).
  - Files: README.md, AUTHORS, doc/cbc-parameters.md, and in src/ CbcSymmetry.cpp, CbcFollowOn.hpp, CbcLinked.hpp, CbcHeuristicPivotAndFix.cpp, CbcHeuristicRandRound.cpp and CbcGeneralDepth.cpp.
  - The import commit eeaed1e (2004-10-29; README, CbcModel.cpp), plus the history.
- S24. Zenodo records "coin-or/Clp: Release releases/1.17.11" (2026-03-11; DOI 10.5281/zenodo.18967769; concept DOI 10.5281/zenodo.2720299) and "coin-or/Cbc: Release v2.933" (2026-08-14; DOI 10.5281/zenodo.21939019; concept DOI 10.5281/zenodo.2720283). https://zenodo.org/api/records/. Secondary.
- S25. GitHub REST API: coin-or/Cbc releases, and issue search `commenter:jjhforrest` (291) and `commenter:johnjforrest` (1). https://api.github.com/. Secondary.

Prize, searches, unreachable pages:
- S26. "The Daniel H. Wagner Prize for Excellence in Operations Research Practice", Interfaces 36(5):383–385, 2006 (Crossref abstract only). DOI 10.1287/inte.1060.0240. Primary (abstract).
- S27. WebSearch, query `Denton Forrest Milne "semiconductor supply chain" Wagner Prize 2005 IBM`. It returned RePEc and EconBiz records of W13 and the INFORMS page of S26, none naming the winning project. Secondary.
- S28. WebSearch, query `"Aboca" Forrest ISMP 2012 Berlin "Clp" talk`: no relevant result. Secondary.
- S29. Not reached on 2026-11-05:
  - http://www.fastercoin.com/f2_files/naqs.html (redirects to a domain-sale page);
  - https://list.coin-or.org/pipermail/cbc/2014-March/001297.html (no connection);
  - https://ismp2012.mathopt.org/ (does not resolve);
  - https://pubsonline.informs.org/doi/10.1287/inte.1060.0238 (403);
  - the INFORMS Wagner Prize page (404).

  Secondary (unavailable).
- S30. Bixby, R. E., "Solving Real-World Linear Programs: A Decade and More of Progress", Operations Research 50(1):3–15, 2002, DOI 10.1287/opre.50.1.3.17780: the fetch of its open mirror was refused in this session; not read. Secondary (not read).
- S31. EMS Press chapter landing page for W9 (citation_pdf_url). https://ems.press/books/dms/248/4854. Secondary.

Quote check (run 2026-11-05 on this file): 323 double-quoted segments checked against the source texts listed above, 0 misses.
- The check normalised whitespace, curly quotes, dashes and line-break hyphens, and removed comment markers in code.
- It confirms presence in the fetched source, not the page or line attribution. Page and line numbers were set by hand from the PDF page breaks and the files at the commits named.
- Segments inside nested quotation marks were checked in pieces.
- Scratch copies of the source texts are outside the repository and are not committed.
