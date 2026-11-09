# Marco E. Lübbecke · 01 · Publication landscape and signature works

| | |
|---|---|
| Researcher | Marco E. Lübbecke, Chair of Operations Research, RWTH Aachen University (full professor since 2010), associate member of GERAD since December 2018 (S10). DBLP pid 24/5951, ORCID 0000-0002-2635-0522. Google Scholar profile `cYIpR60AAAAJ`: team.json has no Scholar id; the id comes from the DBLP person record (S2). Living (team.json). Lens per team.json: column generation, Dantzig-Wolfe reformulation, branch-and-price, the GCG solver |
| Dimension | Research agent 01 of 06: publication landscape and dissection of signature works (framework §二 Agent 1, §五) |
| Research date | 2026-11-08 |
| Sources consulted | 34, listed as S1–S34 under "Sources" (20 primary, 14 secondary). WebSearch: 2 of the 5 allowed calls. Everything else came from curl, WebFetch (Google Scholar), the Crossref, DataCite, ORCID, DNB-SRU, HAL and GitHub APIs, and `scripts/dblp_works.py` |
| Local corpus | `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep` when this run started, so there was no user-supplied material. Other T1 agents added talk transcripts to `talks/` during the run; this note does not use them. `private/` was not opened |
| OpenAlex | not queried (`OPENALEX_API_KEY` is not set) |
| Tool note | `python3 scripts/dblp_works.py --pid 24/5951` crashes with an IndexError at line 307. The upper-case DOI `10.48550/ARXIV.CS/0310034` passes the lower-cased prefix test, but the split uses the mixed-case string `arXiv.`. I ran a copy with a one-line fix from the scratch folder. The repo script is untouched and still has the bug |
| Quotation policy | Exactly one short verbatim phrase is quoted (S10, in SW2). Everything else is paraphrased with a pinpoint page. Check the wording at that page before quoting downstream |

**Tags.**
- **[stated]**: said or written by Lübbecke in a sole-author text (thesis, sole-author papers, his GERAD biography, his blog). **[stated, joint]**: a co-signed text whose "we" cannot be split among the authors. **[stated, joint; third person]**: the four-author book's author notes and its remarks about "Marco"; who wrote them is not known.
- **[practice]**: what the record shows was done: experiments, test sets, code tags, dates, author lists, the publication record itself.
- **[observed]**: what others recorded: bibliographic databases, library catalogues, later papers by others.
- **[inferred]**: my inference. The basis is named.
- **P / S**: primary / secondary source.

**Page conventions.**
- S15 (book, G-2024-36 revised January 2026): main matter printed p. N = PDF p. N+31. Front matter in roman numerals: author notes p. vi = PDF 11, Foreword p. xii = PDF 17, Preface pp. xiii–xv = PDF 18–20.
- S16 (thesis): printed p. N = PDF p. N+12 for the main matter. Preface p. v = PDF 5.
- S17–S21, S26, S29 and the MSLP preprint in S22: "p." is the PDF page.

**Reading depth.**
- **Read in full or in large part.** S16 (front matter, §4.3, §5.3 set-up, all of Ch. 7 "Reflections"; other chapters through the table of contents only). S17 (introduction, section list, conclusions). S18 (whole paper). S19 (all text, tables skimmed). S20 (§1, §4, the §6 profiles, §7). S15 (front matter, Foreword, Preface, pp. 238, 284, 509, 538, 551–552). S21 (abstract and motivation).
- **Abstract or metadata only.** S12–S14, S22 (except the MSLP set-up section), S23–S25, S27, S28.
- **Searched for specific passages only.** S26 (set-up section), S29 (committee footnote, contributor table, §4.5), S31 (where it cites the CPAIOR paper).
- **Not read.** The CPAIOR 2017 full text (no open copy found), the SEA 2012 status report, the Primer, the two Wiley encyclopedia entries, the published OR 2005 version (only the October 2004 preprint), the habilitation (not found).

---

## 0. Authorship and role labels (must survive into the skill)

| Label | Evidence | Tag |
|---|---|---|
| The original GCG architecture comes from Gerald Gamrath. It is the design with two synchronized SCIP instances (original and extended problem), each building the same tree, which the book says is still intact | S15 p. 538. S18 pp. 4–5 describes that design, and its implementation reference is Gamrath's TU Berlin master's thesis *Generic branch-cut-and-price* (2010) | [stated, joint] P |
| Lübbecke has led GCG since 2008. The book describes him as the one with the vision who keeps the project together | S15 pp. vi, 538 | [stated, joint; third person] P |
| Other major GCG contributors named: Bergner, Bastubbe, Puchert, Witt, Maher and Mühmer, with others left unnamed | S15 p. 538 | [stated, joint] P |
| GCG code is group work. Cite it as the RWTH group's practice, not as his personal code | S30; team.json chase hint | [practice] P |
| The automatic-DWR experiments (W29, W38) were not run in GCG. They used a CPLEX 12.2 column generation code with hMETIS partitioning. The book later says most of these detection concepts were implemented in GCG | S19 p. 5; S20 p. 10; S15 p. 238 | [practice, joint] P |
| The LP and degeneracy line (W34, W35, W39, W42, W46, W53) is Jean Bertrand Gauthier's doctoral work under Desrosiers (HEC Montréal, 2016). Lübbecke is the third author on every paper | S15 p. viii; S11 | [observed] P / [inferred] for the division of labour |
| Book (W64): four authors, so no passage can be attributed to Lübbecke alone. The Preface reports compromises and physically exhausting arguments among the authors | S15 p. xv | [stated, joint] P |
| His own voice: the thesis (W3) and the sole-author texts W9, W12, W27, W30, W41, plus S10 and S32 | S16; S5; S10; S32 | [stated] P |
| The two companion surveys alternate the lead. He is first author of *Selected Topics* (W10) and Desrosiers is first author of the *Primer* (W11) | S17 p. 1; S13 | [practice] P |
| MIPLIB 2017: one of 21 committee members and author 11 of 16. Bastubbe (RWTH; likely his doctoral student, see §1.5) contributed 19 instances. GCG 3.0 computed the library's ten decomposition features | S29 pp. 2, 6, 16 | [practice, joint] P |
| SCIP Optimization Suite reports: co-author of 4.0, 6.0, 8.0 and 10.0, but not 9.0, whose 31 authors include Erik Mühmer and not Lübbecke | S1; S6; S27; S28; S33 | [observed] S (5.0 and 7.0 not checked directly) |

---

## 1. Publication landscape

### 1.1 Record coverage and name forms

- [observed, S] **Google Scholar** (S1, as rendered by WebFetch on 2026-11-08): 118 rows. Totals: 7,111 citations, h-index 31, i10-index 54; since 2021: 3,223 / 21 / 30. Yearly citations rise almost steadily from 28 (2004) to 645 (2026). Some rows are duplicates, and one row carries no Lübbecke author string (*The Boat and Barge Routing Problem*, CTW 2011; S3 lists him as third author).
- [observed, S] **DBLP** (S2, SPARQL snapshot): 58 records, 1998–2023 (35 articles, 18 conference papers, 2 informal, 2 editorships, 1 chapter). 55 carry a DOI and 1 an arXiv id. The snapshot misses everything from 2024 on, as well as the thesis, the encyclopedia entries, the Primer and the book.
- [observed, S] **Semantic Scholar** (S3): author 1761286 has 100 papers, 4,695 citations and h = 26. The record is contaminated by a homonym: a 1994 veterinary paper on mares by another M. Lübbecke. Three further small split records exist. Per-paper calls failed with HTTP 429.
- [observed, S] **ORCID** (S4): 60 work groups, ending with the 2026 book and the 2026 SSRN preprint W66.
- [observed, S] **arXiv** (S6): only four papers with him: cs/0310034, 2112.08872, 2303.07101 and 2602.04984. His preprints went out instead as Les Cahiers du GERAD (11 with him, S11), as TU Berlin, RWTH and ZIB reports, and on Optimization Online (S33).
- [observed, S] **Name forms.**
  - Spellings: Lübbecke, Luebbecke and Lubbecke. Crossref name searches return unrelated Lübbeckes publishing in oceanography, medicine and laser optics, so every hit needs an author-list check (S5).
  - The middle initial: [stated, joint; third person] he has no middle name. The "E." is an initial he chose for the copyright form of his first paper (S15 p. vi). "Marco Lübbecke" and "Marco E. Lübbecke" are therefore the same person.

### 1.2 Verified works (W-numbers used below)

Every row was checked with at least one tool (DOI resolution or registry record, a publisher or preprint page, or two independent database rows). Position = his place in the author list.

| W | Year | Full title | Authors (his position) | Venue | Identifier |
|---|---|---|---|---|---|
| W1 | 1998 | The vertex set of a 0/1-polytope is strongly P-enumerable | Bussieck, Lübbecke (2/2) | Computational Geometry 11(2):103–109 | DOI 10.1016/S0925-7721(98)00021-2 |
| W2 | 1998 | Optimal scrap combination for steel production | Bernatzki, Bussieck, Lindner, Lübbecke (4/4) | OR Spectrum 20(4):251–258 | DOI 10.1007/BF01539743 |
| W3 | 2001 | Engine Scheduling by Column Generation (Dr. rer. nat. thesis, TU Braunschweig; Cuvillier) | sole | — | DOI 10.24355/DBBS.084-200511080100-720 (DataCite); ISBN 3-89873-178-2 (DNB) |
| W4 | 2003 | Engine routing and scheduling at industrial in-plant railroads | Lübbecke, Zimmermann (1/2) | Transportation Science 37(2):183–197 | DOI 10.1287/trsc.37.2.183.15251 |
| W5 | 2003 | MaxFlow-MinCut duality for a paint shop problem | Epping, Hochstättler, Lübbecke (3/3) | Operations Research Proceedings 2002, 377–382 | DOI 10.1007/978-3-642-55537-4_61 |
| W6 | 2003 | Computer aided scheduling of switching engines | with Zimmermann | in *Mathematics — Key Technology for the Future* | DOI 10.1007/978-3-642-55753-8_52 (S3) |
| W7 | 2004 | A fast algorithm for near cost optimal line plans | Bussieck, Lindner, Lübbecke (3/3) | Math. Methods Oper. Res. 59(2):205–220 | DOI 10.1007/s001860300332 |
| W8 | 2004/2008 | Minimizing the stabbing number of matchings, trees, and triangulations | Fekete, Lübbecke, Meijer (2/3) | SODA 2004, 437–446; Discrete Comput. Geom. 40(4):595–621 (2008) | arXiv cs/0310034; DOI 10.1007/s00454-008-9114-6 |
| W9 | 2004 | Combinatorially simple pickup and delivery paths | sole | Central European J. Oper. Res. 12:405–417 (S1; S3 gives 2002) | venue + year + title (S1, S3) |
| W10 | 2005 | Selected topics in column generation | Lübbecke, Desrosiers (1/2) | Operations Research 53(6):1007–1023 | DOI 10.1287/opre.1050.0234; GERAD G-2002-64; OO 2002/12/580 |
| W11 | 2005 | A primer in column generation | Desrosiers, Lübbecke (2/2) | in *Column Generation* (eds. Desaulniers, Desrosiers, Solomon), Springer, 1–32 | DOI 10.1007/0-387-25486-2_1; GERAD G-2004-02 |
| W12 | 2005 | Dual variable based fathoming in dynamic programs for column generation | sole | EJOR 162(1):122–125 | DOI 10.1016/j.ejor.2003.05.006 |
| W13 | 2005 | On compact formulations for integer programs solved by column generation | Villeneuve, Desrosiers, Lübbecke, Soumis (3/4) | Annals of OR 139:375–388 | DOI 10.1007/s10479-005-3455-9; GERAD G-2003-06 |
| W14 | 2005 | Shunting minimal rail car allocation | Lübbecke, Zimmermann (1/2) | Comput. Optim. Appl. 31(3):295–308 | DOI 10.1007/s10589-005-3229-y |
| W15 | 2005/2006 | Rectangle covers revisited computationally | Heinrich-Litan, Lübbecke (2/2) | WEA 2005, 55–66; ACM J. Exp. Algorithmics 11 (2006) | DOI 10.1007/11427186_7; DOI 10.1145/1187436.1216583 |
| W16 | 2006/2008 | On minimum k-modal partitions of permutations | Di Stefano, Krause, Lübbecke, Zimmermann (3/4) | LATIN 2006, 374–385; J. Discrete Algorithms 6(3):381–392 (2008) | DOI 10.1007/11682462_36; DOI 10.1016/j.jda.2008.01.002 |
| W17 | 2007 | Solutions to real-world instances of PSPACE-complete stacking | König, Lübbecke, Möhring, Schäfer, Spenke (2/5) | ESA 2007, 729–740 | DOI 10.1007/978-3-540-75520-3_64 |
| W18 | 2008 | Optimal university course timetables and the partial transversal polytope | Lach, Lübbecke (2/2) | WEA 2008, 235–248 | DOI 10.1007/978-3-540-68552-4_18 |
| W19 | 2008 | Optimizing the cargo express service of Swiss Federal Railways | Ceselli, Gatto, Lübbecke, Nunkesser, Schilling (3/5) | Transportation Science 42(4):450–465 | DOI 10.1287/trsc.1080.0246 |
| W20 | 2008 | Sorting with complete networks of stacks | König, Lübbecke (2/2) | ISAAC 2008, 895–906 | DOI 10.1007/978-3-540-92182-0_78 |
| W21 | 2009 | The concept of recoverable robustness, linear programming recovery, and railway applications | Liebchen, Lübbecke, Möhring, Stiller (2/4) | *Robust and Online Large-Scale Optimization*, LNCS 5868, 1–27 | DOI 10.1007/978-3-642-05465-5_1 |
| W22 | 2009/2011 | Sequencing and scheduling in coil coating with shuttles (Dagstuhl seminar proceedings, 2009; Lübbecke 3/4); then *Integrated sequencing and scheduling in coil coating* (Höhn, König, Möhring, Lübbecke; 4/4) | see title | Management Science 57(4):647–666 (2011) | URN urn:nbn:de:0030-drops-21654 (DNB); DOI 10.1287/mnsc.1100.1302 |
| W23 | 2010 | Experiments with a generic Dantzig-Wolfe decomposition for integer programs | Gamrath, Lübbecke (2/2) | SEA 2010, LNCS 6049, 239–252 | DOI 10.1007/978-3-642-13193-6_21; OO 2010/03/2556 |
| W24 | 2010/2015 | A branch-and-price algorithm for multi-mode resource leveling (SEA 2010, 226–238); then *A branch-price-and-cut algorithm for multi-mode resource leveling* | Coughlan, Lübbecke, Schulz (2/3) | EJOR 245(1):70–80 (2015) | DOI 10.1007/978-3-642-13193-6_20; DOI 10.1016/j.ejor.2015.02.043 |
| W25 | 2010 | A constraint integer programming approach for resource-constrained project scheduling | Berthold, Heinz, Lübbecke, Möhring, Schulz (3/5) | CPAIOR 2010, 313–317 | DOI 10.1007/978-3-642-13520-0_34 |
| W26 | 2010 | ATMOS 2010 proceedings (OASIcs 14), co-editor with Erlebach | editor | Dagstuhl | ISBN 978-3-939897-20-0; DOI 10.4230/OASIcs.ATMOS.2010.i |
| W27 | 2011 | Column generation | sole | Wiley Encyclopedia of OR and MS | DOI 10.1002/9780470400531.eorms0158 |
| W28 | 2011 | Branch-price-and-cut algorithms | Desrosiers, Lübbecke (2/2) | Wiley Encyclopedia of OR and MS | DOI 10.1002/9780470400531.eorms0118 |
| W29 | 2011 | Partial convexification of general MIPs by Dantzig-Wolfe reformulation | Bergner, Caprara, Furini, Lübbecke, Malaguti, Traversi (4/6) | IPCO 2011, LNCS 6655, 39–51 | DOI 10.1007/978-3-642-20807-2_4; OO 2010/11/2819 |
| W30 | 2012 | Automatic decomposition and branch-and-price — a status report | sole | SEA 2012, 1–8 | DOI 10.1007/978-3-642-30850-5_1 |
| W31 | 2012 | Primal heuristics for branch-and-price algorithms | Lübbecke, Puchert (1/2) | OR Proceedings 2011, 65–70 | DOI 10.1007/978-3-642-29210-1_11 |
| W32 | 2012 | Curriculum based course timetabling: new solutions to Udine benchmark instances | Lach, Lübbecke (2/2) | Annals of OR 194(1):255–272 (online 2010-02-05) | DOI 10.1007/s10479-010-0700-7 |
| W33 | 2012 | Nested column generation applied to the crude oil tanker routing and scheduling problem with split pickup and split delivery | Hennig, Nygreen, Lübbecke (3/3) | Naval Research Logistics 59(3–4):298–310 | DOI 10.1002/nav.21489 |
| W34 | 2014 | Row-reduced column generation for degenerate master problems | Desrosiers, Gauthier, Lübbecke (3/3) | EJOR 236(2):453–460 | DOI 10.1016/j.ejor.2013.12.016; GERAD G-2013-09 (predecessor G-2011-66, *Improved column generation for highly degenerate master problems*) |
| W35 | 2014 | Decomposition theorems for linear programs | Gauthier, Desrosiers, Lübbecke (3/3) | Oper. Res. Lett. 42(8):553–557 | DOI 10.1016/j.orl.2014.10.001; GERAD G-2014-67 |
| W36 | 2014/2016 | A branch-price-and-cut algorithm for packing cuts in undirected graphs | Bergner, Lübbecke, Witt (2/3) | SEA 2014, 34–45; ACM JEA 21(1), 1.2 (2016) | DOI 10.1007/978-3-319-07959-2_4; DOI 10.1145/2851492 |
| W37 | 2014 | Zukunftsperspektiven des Operations Research (Festschrift for H.-J. Zimmermann), co-editor with Weiler and Werners. It contains Kirchner and Lübbecke, *Dynamische Vergabe von Patiententerminen in Krankenhäusern* | editor; chapter 2/2 | Springer Gabler | DOI 10.1007/978-3-658-05707-7; chapter DOI 10.1007/978-3-658-05707-7_6 |
| W38 | 2015 | Automatic Dantzig–Wolfe reformulation of mixed integer programs | Bergner, Caprara, Ceselli, Furini, Lübbecke, Malaguti, Traversi (5/7) | Math. Program. 149(1–2):391–424 | DOI 10.1007/s10107-014-0761-5; OO 2012/09/3614 |
| W39 | 2015 | About the minimum mean cycle-canceling algorithm | Gauthier, Desrosiers, Lübbecke (3/3) | Discrete Appl. Math. 196:115–134 | DOI 10.1016/j.dam.2014.07.005; GERAD G-2013-52 |
| W40 | 2015 | Separation of generic cutting planes in branch-and-price using a basis | Lübbecke, Witt (1/2) | SEA 2015, 110–121 | DOI 10.1007/978-3-319-20086-6_9; OO 2015/02/4790 |
| W41 | 2015 | Comments on: An overview of curriculum-based course timetabling | sole | TOP, 359–361 | DOI 10.1007/s11750-015-0364-1 |
| W42 | 2016 | Tools for primal degenerate linear programs: IPS, DCA, and PE | Gauthier, Desrosiers, Lübbecke (3/3) | EURO J. Transp. Logist. 5(2):161–204 | DOI 10.1007/s13676-015-0077-5; GERAD G-2013-51 |
| W43 | 2016 | An adaptive discretization MINLP algorithm for optimal synthesis of decentralized energy supply systems | Goderbauer, Bahl, Voll, Lübbecke, Bardow, Koster (4/6) | Comput. Chem. Eng. 95:38–48 | DOI 10.1016/j.compchemeng.2016.09.008 |
| W44 | 2016 | DESSLib – Benchmark Instances for Optimization of Decentralized Energy Supply Systems | Bahl, Goderbauer, Arnold, Voll, Lübbecke, Bardow, … (S1 order; list truncated there) | technical report | Optimization Online 2016/06/5503 |
| W45 | 2016 | Operations Research Proceedings 2014 (GOR conference at RWTH Aachen), co-editor | editor | Springer | DOI 10.1007/978-3-319-28697-6 |
| W46 | 2017 | A strongly polynomial Contraction-Expansion algorithm for network flow problems | Gauthier, Desrosiers, Lübbecke (3/3) | Comput. Oper. Res. 84:16–32 | DOI 10.1016/j.cor.2017.02.019; GERAD G-2016-18 |
| W47 | 2017 | Learning when to use a decomposition | Kruber, Lübbecke, Parmentier (2/3) | CPAIOR 2017, 202–210 | DOI 10.1007/978-3-319-59776-8_16 |
| W48 | 2017 | Optimization of the reconfiguration planning of handling systems based on parallel manipulators with Delta-like architecture (follow-up at ReMAR 2018) | Brinker, Lübbecke, Takeda, Corves (2/4) | IEEE Robot. Autom. Lett. 2(3):1802–1808 | DOI 10.1109/LRA.2017.2705286; DOI 10.1109/REMAR.2018.8449867 |
| W49 | 2017 | The SCIP Optimization Suite 4.0 | Maher et al. | ZIB report | Optimization Online 2017/03/5895 |
| W50 | 2018 | Polyhedral results on the stable set problem in graphs containing even or odd pairs | Witt, Lübbecke, Reed (2/3) | Math. Program. 171(1–2):519–522 | DOI 10.1007/s10107-017-1168-x |
| W51 | 2018 | The strength of Dantzig–Wolfe reformulations for the stable set and related problems | Lübbecke, Witt (1/2) | Discrete Optimization 30:168–187 | DOI 10.1016/j.disopt.2018.07.001; OO 2015/11/5208 |
| W52 | 2018 | A computational investigation on the strength of Dantzig-Wolfe reformulations | Bastubbe, Lübbecke, Witt (2/3) | SEA 2018, 11:1–11:12 | DOI 10.4230/LIPIcs.SEA.2018.11; OO 2018/02/6485 |
| W53 | 2018 | Vector space decomposition for solving large-scale linear programs | Gauthier, Desrosiers, Lübbecke (3/3) | Operations Research 66(5):1376–1389 | DOI 10.1287/opre.2018.1728; GERAD G-2015-26 |
| W54 | 2018 | The SCIP Optimization Suite 6.0 | Gleixner, Bastubbe, Eifler, et al. | ZIB report (opus4 docId 6936) | Optimization Online 2018/07/6692 |
| W55 | 2018 | Integrating line planning, timetabling and vehicle scheduling | Lübbecke, Puchert, Schiewe, Schöbel (1/4) | CASPT 2018 | venue + year + title (S1, S3) |
| W56 | 2019 | Ship traffic optimization for the Kiel Canal | E. Lübbecke, M. E. Lübbecke, Möhring (2/3) | Operations Research 67(3):791–812 | DOI 10.1287/opre.2018.1814; OO 2014/12/4681 |
| W57 | 2019 | Reform der Bundestagswahlkreise: Unterstützung durch mathematische Optimierung | Goderbauer, Lübbecke (2/2) | Zeitschrift für Parlamentsfragen 50(1):3–21 | DOI 10.5771/0340-1758-2019-1-3 |
| W58 | 2020 | A branch-and-price algorithm for capacitated hypergraph vertex separation | Bastubbe, Lübbecke (2/2) | Math. Program. Comput. 12(1):39–68 (online 2019-09-09) | DOI 10.1007/s12532-019-00171-5; OO 2017/11/6331 |
| W59 | 2020 | Welcome to SN Operations Research Forum! (journal launch editorial) | Lübbecke, Pardalos | SN Oper. Res. Forum 1(1) | DOI 10.1007/s43069-020-0001-1 |
| W60 | 2021 | Avoiding redundant columns by adding classical Benders cuts to column generation subproblems | Lübbecke, Maher, Witt (1/3) | Discrete Optimization 39:100626 | DOI 10.1016/j.disopt.2021.100626; OO 2019/02/7096 |
| W61 | 2021 | MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library | Gleixner, Hendel, Gamrath, Achterberg, Bastubbe, Berthold, Christophel, Jarck, Koch, Linderoth, Lübbecke, Mittelmann, Özyurt, Ralphs, Salvagnin, Shinano (11/16) | Math. Program. Comput. 13(3):443–490 | DOI 10.1007/s12532-020-00194-3; OO 2019/07/7285 |
| W62 | 2021/2023 | The SCIP Optimization Suite 8.0 (arXiv 2021); then *Enabling research through the SCIP Optimization Suite 8.0* | Bestuzheva et al. (18/35 in TOMS) | ACM Trans. Math. Softw. 49(2), 22:1–22:21 (2023) | arXiv 2112.08872; DOI 10.1145/3585516; arXiv 2303.07101 |
| W63 | 2022 | An image-based approach to detecting structural similarity among mixed integer programs | Steever, Murray, Yuan, Karwan, Lübbecke (5/5) | INFORMS J. Comput. 34(4):1849–1870 | DOI 10.1287/ijoc.2021.1117; SSRN DOI 10.2139/ssrn.3437981; OO 2020/04/7760 |
| W64 | 2024/2026 | Branch-and-Price | Desrosiers, Lübbecke, Desaulniers, Gauthier (2/4) | Les Cahiers du GERAD G-2024-36 (June 2024, revised January 2026); Springer Cham 2026, 663 pp., open access | DOI 10.1007/978-3-031-96917-1 (chapters …_1 to …_8) |
| W65 | 2025 | The SCIP Optimization Suite 10.0 | Hojny et al. (34 authors, including Lübbecke and Mühmer) | report | arXiv 2511.18580 |
| W66 | 2024/2026 | The multi-stop station location problem: exact approaches | Mühmer, Ganz, Lübbecke, Willamowski (3/4) | preprint (OO, posted 2024-04-17, updated 2026-07-23) | DOI 10.2139/ssrn.7177419 |
| W67 | 2026 | Branch-and-price strikes back for the k-vertex cut problem | Ciccarelli, Furini, Hojny, Lübbecke (4/4) | preprint (v1 2026-02-04, v2 2026-06-05) | arXiv 2602.04984; code and data at Zenodo DOI 10.5281/zenodo.17897865 |
| W68 | 2007/2008 | Editorial (European J. Combin. 28(8):2053–2056); Preface (Discrete Math. 308(8):1347–1349) | Felsner, Lübbecke, Nešetřil | special-issue editorials | DOI 10.1016/j.ejc.2007.04.003; DOI 10.1016/j.disc.2007.09.029 |
| W69 | 2009– | GCG (expanded as *generic column generation* in S18 p. 4), RWTH group code on SCIP | group | software | github.com/scipopt/gcg. Tag commit dates: v010 2009-06-17, v070 2010-02-13, v100 2012-07-31, v200 2014-02-27, v300 2018-07-02, v4.0.0 2025-11-20, v4.1.0 2026-09-14 (S30) |

### 1.3 Topics by five-year period

DBLP author records per period (S2, editorships excluded): 1995–99: 1, 2000–04: 5, 2005–09: 17, 2010–14: 12, 2015–19: 15, 2020–23: 6. These counts understate the early years (no thesis, no encyclopedia entries) and the years after 2023 (the snapshot ends there).

| Period | Place and seniority | Topics (works) | Character [practice, with my reading marked inferred] |
|---|---|---|---|
| 1996–2000 | TU Braunschweig: Diplom 1996, then research assistant with Zimmermann (S16 CV p. 181) | vertex enumeration of 0/1-polytopes (W1), steel scrap (W2) | polyhedral computation next to industry OR |
| 2001–2005 | PhD 2001 (Braunschweig), then TU Berlin (Möhring's combinatorial optimization group) | engine scheduling by column generation (W3, W4, W6, W14), line planning (W7), paint shop (W5), stabbing number (W8), rectangle covers (W15), pickup-delivery paths (W9), column generation surveys (W10, W11), compact formulations (W13), dual fathoming (W12) | column generation born from one industrial application. Synthesis with GERAD begins. Algorithmic combinatorics alongside |
| 2006–2010 | TU Berlin (habilitation 2007); visiting professor at TU Darmstadt 2009–10 (S10; S18 p. 1 affiliation) | permutations (W16), stacking and sorting (W17, W20), timetabling (W18), Swiss cargo (W19), recoverable robustness (W21), coil coating (W22), RCPSP via constraint integer programming (W25), resource leveling by branch-and-price (W24), GCG (W23, W69), ATMOS co-chair (W26) | algorithm engineering on industrial problems at algorithms venues (ESA, ISAAC, LATIN, WEA). Generic branch-and-price starts |
| 2011–2015 | RWTH Aachen chair (from 2010) | automatic DWR (W29, W38), status report (W30), branch-and-price heuristics (W31), nested column generation (W33), degeneracy and LP decomposition with GERAD (W34, W35, W39, W42), packing cuts (W36), generic cuts in branch-and-price (W40), encyclopedia entries (W27, W28), Festschrift (W37) | automation of DW; LP theory for degenerate masters (the GERAD side) |
| 2016–2020 | RWTH; GERAD associate member from December 2018 | vector space decomposition and contraction-expansion (W46, W53), strength of DW reformulations (W50, W51, W52), learning when to decompose (W47), hypergraph separation (W58), energy MINLP (W43, W44), robotics (W48), Kiel Canal (W56), electoral districting (W57), integrated line planning (W55), SN OR Forum (W59), SCIP 4.0/6.0 (W49, W54) | reformulation-strength theory, ML for solver decisions, application forays into engineering. [stated, joint; third person] The book also notes the engineering forays (S15 p. vi) |
| 2021–2026 | RWTH; GERAD | Benders cuts in pricing (W60), MIPLIB 2017 (W61), SCIP 8.0/10.0 (W62, W65), image-based MIP similarity (W63), the book (W64), tailored branch-price-and-cut for station location (W66) and the k-vertex cut problem (W67), GCG 4.x (W69) | consolidation (the book), community infrastructure, tailored branch-and-price built directly on SCIP |

### 1.4 Author order

- [practice] **Alphabetical order dominates.** 40 of 54 multi-author DBLP records list the authors alphabetically (computed on S2 with a strict surname check, which counts the large MIPLIB 2017 and SCIP 8.0 author lists as non-alphabetical), so author position says little. Optimization Online's author order sometimes differs from the byline (C8), so its metadata must not be used for position.
- [practice] **Non-alphabetical bylines, the only position signal:**
  - He leads the 2005 survey (W10).
  - He is placed last on the Management Science coil-coating paper (W22, 2011).
  - Gauthier, the doctoral student, comes first on the GERAD LP papers, with Lübbecke third (W35, W39, W42, W46, W53).
  - Witt, the student, comes first on W50.
  - The engineering papers use engineering order (W43, W48).
  - He is last on the US-led IJOC paper (W63).
  - On W66 the student Mühmer comes first, and the rest are alphabetical.
- [inferred] From about 2014, whenever the order is not alphabetical, a junior author leads and Lübbecke is not first. This is the senior-author pattern, though alphabetical lists hide it most of the time.
- [practice] **Sole-authored work clusters early:** the thesis (W3, 2001), W9 (2004), W12 (2005), the encyclopedia entry W27 (2011), the SEA 2012 status report W30 and the TOP comment W41 (2015). No sole-authored research paper appears after 2015 in S1–S5.

### 1.5 Collaboration network and students

| Cluster | People (DBLP joint records in S2 where counted) | Evidence |
|---|---|---|
| Braunschweig (1996–2001) | Uwe T. Zimmermann (doctoral advisor, 4), Michael R. Bussieck (2), Thomas Lindner, Klaus-P. Bernatzki, Stefan Krause, Gabriele Di Stefano | S16 p. vi (acknowledgments), title page; S2 |
| GERAD / Montréal (2001–) | Jacques Desrosiers (8; external co-referee of the 2001 thesis), Jean Bertrand Gauthier (6), Guy Desaulniers (book; co-referee of Witt's dissertation), François Soumis, Daniel Villeneuve | S16 title page; S10; S8; S2 |
| Algorithmic geometry (2003–2008) | Sándor P. Fekete (3; also co-referee of the 2001 thesis), Henk Meijer (3) | S2; S16 title page |
| TU Berlin (about 2002–2009) | Rolf H. Möhring (habilitation host, 6), Felix G. König (4), Jens Schulz (3), Wiebke Höhn (2), Christian Liebchen, Sebastian Stiller, Gerald Lach (2), Eamonn T. Coughlan (2), Elisabeth Lübbecke; ZIB colleagues Timo Berthold (2), Stefan Heinz, Gerald Gamrath (3) | S2; S16 title page; S8 |
| Italy, France, Netherlands (2010–) | Alberto Caprara, Fabio Furini, Enrico Malaguti, Emiliano Traversi, Alberto Ceselli (automatic DWR); Fabio Ciccarelli and Furini (Sapienza Rome) and Christopher Hojny (TU Eindhoven) on W67; Axel Parmentier (W47; affiliation not verified here) | S19; S20 p. 1 (Bologna, Milano, Paris affiliations); S23; S26 p. 1 |
| RWTH Aachen (2010–) | Martin Bergner (4), Jonas T. Witt (7), Michael Bastubbe (3), Christian Puchert, Markus Kruber, Sebastian Goderbauer, Erik Mühmer, Stephen J. Maher, Miriam Ganz, Felix Willamowski; colleagues Arie M. C. A. Koster, Britta Peis, Grit Walther; engineering partners André Bardow, Burkhard Corves | S2; S15 p. 538; S22 |
| Community infrastructure | the MIPLIB 2017 committee; the SCIP Optimization Suite author collectives | S29 p. 2; S27; S28 |

Doctoral students. Evidence decreases from top to bottom:
- [observed, S] **Confirmed by the national library.** DNB lists Lübbecke first among the *Akademischer Betreuer* (academic supervisors) for Jonas T. Witt (2019, *Polyhedral aspects of Dantzig-Wolfe reformulation*, with Koster and Desaulniers), Sebastian Goderbauer (2019), Sarah Katharina Roth (2020), Annika Thome (2021) and Christian Stefan Franzen (2022). DataCite's RWTH records give him the contributor type *Supervisor* for the same people (S7). Both catalogues lump advisors and referees together, so first place is the only advisor signal.
- [observed, S] **Co-supervisor or second referee at RWTH:** Florian H. W. Dahms (2016/17, Koster listed first), Asif Khan (2016), Astrid Dettenbach (2016), Andreas Braun (2017), Christian Wassermann (2023, computer science) (S7, S8).
- [observed, S] **External referee elsewhere:** Marc Goerigk (Göttingen 2013), Frank Fischer (Chemnitz 2013), Robert Voll (Dortmund 2014), Wiebke Höhn and Torsten J. Gellert (TU Berlin 2014 and 2015, both Möhring's students) (S8).
- [inferred] **Likely RWTH doctoral students or postdocs, with no dissertation record found here:** Bergner, Puchert, Bastubbe, Kruber, Mühmer. The basis is their RWTH affiliation on joint papers (S18–S21), their place in the GCG contributor list (S15 p. 538) and Bergner's funding through DFG grants LU770/4-1 and 4-2 (S20 p. 1; the LU prefix suggests Lübbecke held the grant, inferred). Gamrath wrote the 2010 TU Berlin master's thesis behind GCG (S18 ref. [6]); its supervisor is not verified.

### 1.6 Usual venues

- [practice] **Experimental-algorithms line:** SEA six times in DBLP (2010 twice, 2012, 2014, 2015, 2018), WEA twice (2005, 2008), ACM JEA twice. That is the most frequent single venue family.
- [practice] **OR journals:** Operations Research (W10, W53, W56), EJOR (W12, W24, W34), Annals of OR (W13, W32), Transportation Science (W4, W19), Discrete Optimization (W51, W60), Mathematical Programming (W38, W50), Math. Prog. Computation (W58, W61). One each in Management Science, INFORMS JoC, ACM TOMS, NRL, COAP, MMOR, DAM, ORL, COR and EURO J. Transp. Logist.
- [practice] **Algorithms conferences** in the Berlin years: SODA, ESA, ISAAC, LATIN. **IP/CP conferences:** IPCO 2011, CPAIOR 2010 and 2017.
- [stated] **Conference version first, journal later.** In a 2014 blog post he advises sending abstracts or extended abstracts to refereed conferences first, for feedback on both content and presentation (S32). The record shows that pipeline: W8, W15, W16, W24, W29→W38 and W36 all have a conference version followed by a journal version. Several SEA papers (W23, W40, W52) have no journal successor in S1–S5.

### 1.7 Most cited (S1, 2026-11-08; S3 in brackets where it has the record)

| Rank | Work | Google Scholar [Semantic Scholar] | Note |
|---|---|---|---|
| 1 | Selected topics in column generation (W10) | 1,716 [1,331] | survey |
| 2 | A primer in column generation (W11) | 720 [455] | didactic chapter |
| 3 | MIPLIB 2017 (W61) | 531 [347] | community library, author 11 of 16 |
| 4 | Recoverable robustness (W21) | 517 [343] | robust optimization, outside the MILP lens |
| 5 | SCIP Optimization Suite 6.0 (W54) | 429 | release report |
| 6 | SCIP Optimization Suite 8.0, arXiv (W62) | 417 [TOMS 93] | release report |
| 7 | Branch-price-and-cut algorithms, encyclopedia (W28) | 202 [120] | expository |
| 8 | Column generation, encyclopedia (W27) | 180 [see C6] | expository |
| 9 | Learning when to use a decomposition (W47) | 157 [104] | ML turn |
| 10 | Curriculum based course timetabling (W32) | 156, merged row [85] | application |
| 11 | Experiments with a generic Dantzig-Wolfe decomposition (W23) | 137 [88] | GCG origin |
| 12 | Near cost optimal line plans (W7) | 128 [100] | application |
| 13 | SCIP Optimization Suite 4.0 (W49) | 124 | release report |
| 14 | Enabling research through SCIP 8.0 (W62) | 116 [93] | release report |
| 15 | Automatic Dantzig–Wolfe reformulation (W38) | 105 [63] | automation |

- [observed] Four of the top eight works are expository: W10, W11, W27, W28.
- [observed] Community infrastructure (MIPLIB 2017, the SCIP reports) is the next block. There his share is small within large author lists.
- [observed] The GCG research papers (W23, W38, W47) sit between 105 and 157.
- [inferred] His citation footprint is dominated by synthesis and teaching texts rather than by the generic-solver research that he describes as his current focus (S10).

### 1.8 Recent works and latest traces (2023–2026)

- [practice] **The book:** W64. The Cahier came out June 2024 and was revised January 2026; Springer open access followed in February 2026, with GERAD news dated 2026-02-06 (S11).
- [practice] **Two tailored branch-price-and-cut studies:**
  - W66, on station location: preprint April 2024, updated July 2026, SSRN 2026.
  - W67, on the k-vertex cut problem: arXiv February 2026, v2 June 2026.
  - Both are implemented directly on SCIP, not in GCG. W67 uses SCIP 9.2.3 with custom plugins and SoPlex 7.1.5, chosen so that the algorithm is fully open source, and it publishes its code and data on Zenodo (S26 p. 23). W66 uses SCIP 8.0.2 for branch-price-and-cut and Gurobi 9.5.2 for the arc-based model (S22, MSLP PDF p. 22). Neither text mentions GCG.
- [practice] **SCIP Optimization Suite 10.0** (W65, November 2025) lists him; 9.0 (February 2024) does not (S27).
- [practice] **GCG releases:** the v4.0.0 tag commit is dated 2025-11-20 and v4.1.0 is dated 2026-09-14 (S30).
- [observed] **A lead for agent 02:** a 2021 Cassyni posting titled *SN Operations Research Forum* under his name (Crossref DOI 10.52843/cassyni.42wn2q, S5). It is probably a talk; not opened.

### 1.9 Preprint-to-publication lags [practice]

| Work | Preprint date | Publication | Lag |
|---|---|---|---|
| W10 | GERAD December 2002; revised 9 March 2004 and 21 October 2004 | OR, November–December 2005 | about 3 years |
| W38 | manuscript 20 September 2011; revised 20 September 2012 and 1 November 2013 | Math. Program. 2015 (2014 in the DOI) | about 3 years |
| W56 | Optimization Online December 2014, updated June 2018 | OR May 2019 | about 4.5 years |
| W51 | Optimization Online November 2015, updated July 2018 | Disc. Optim. November 2018 | 3 years |
| W58 | Optimization Online November 2017 | MPC online September 2019 | about 2 years |
| W60 | Optimization Online February 2019 | Disc. Optim. February 2021 | 2 years |
| W63 | SSRN 2019; Optimization Online April 2020 | IJOC July 2022 | about 3 years |
| W34 | the 2011 Cahier G-2011-66 under another title, re-issued as G-2013-09 | EJOR 2014 | — |
| W64 | first book email January 2001; repository started January 2015 | Cahier June 2024; Springer February 2026 | about 11 years from the start of writing |

Sources: S11, S17 p. 1, S20 p. 1, S22, S15 p. xiii.

---

## 2. Signature works (framework §五)

Selection rule: most cited (SW1), self-designated as central (SW2, SW4 via S10; SW5 via S10 and S15), and turning points (SW2, SW3, SW4). Secondary lines that are not dissected are listed in 2.6.

### SW1 · *Selected Topics in Column Generation* (W10, OR 2005), with the *Primer* (W11) as companion

| Dimension | Finding | Tag / source |
|---|---|---|
| Origin | Chapter 2 of his 2001 thesis carries the same title. It covers the same ground: decomposition, the restricted master and its duals, pricing, tailing off, stabilization, branching (S16 pp. vii–viii). The thesis claims that no compilation with comparable focus existed before (S16 p. 156). Desrosiers was the thesis's external co-referee (S16 title page), and the GERAD biography dates the collaboration to that request (S10) | [stated] P for each fact; [inferred] that the paper grew out of the thesis chapter |
| Why then | By 2002 generic treatments and an acceleration compendium existed, but the newer dual-side material (stabilization, dual cuts, initialization) was not yet in textbooks (S12 abstract; S17 pp. 1–2). He had just compiled it for the thesis | [stated, joint] P; [inferred] for the timing |
| Key insight | The dual point of view (dual solutions, stabilization, dual inequalities) is the recurring concept that organizes integer-programming column generation (S12; S17 p. 24) | [stated, joint] P |
| Minimum evidence | A survey, so no single experiment. The claim rests on the literature reviewed | — |
| Abandoned paths | It advises against the classical Dantzig-Wolfe implementation as a pricing scheme for large LPs, while recommending stabilized and dual-cut variants (S17 p. 24). Two revisions preceded acceptance (S17 p. 1). What changed between versions: not read | [stated, joint] P; revisions [practice] |
| Reception | His most cited work, with the Primer second (S1, S3). The 2026 book continues the programme (S15) | [observed] S |
| Method shown | CM4 (synthesis as a research instrument), CM6 (the dual lens) | — |

### SW2 · *Experiments with a Generic Dantzig-Wolfe Decomposition for Integer Programs* (W23, SEA 2010): the GCG origin

| Dimension | Finding | Tag / source |
|---|---|---|
| Origin | Almost every branch-and-price application was ad hoc, started from scratch and dependent on expert knowledge. The paper wants a generic implementation that decomposes when promising, as generic branch-and-cut already did (S18 p. 1). His thesis had asked for more generally valid column generation ideas (S16 p. 157). The book says he was in the first team to use SCIP's column generation (version 0.81) and has led GCG since 2008 (S15 p. vi). The first tag is dated 2009-06-17 (S30). His GERAD biography describes GCG as a code that "aims to make the useful Dantzig-Wolfe reformulation available to everyone" (S10) | [stated, joint] P; [stated] P (S16, S10); [practice] P (S30) |
| Why then | SCIP was a well-maintained open framework with pricing plugins. Among comparable codes only DIP was public, and only as trunk development without a release (S18 p. 2). Building on SCIP brings its presolve, branching, propagation, heuristics and cuts, plus all later improvements (S18 abstract, p. 2) | [stated, joint] P |
| Key insight | Turn a branch-price-and-cut framework into a solver: run two synchronized SCIP instances (original and extended), driven by a relaxation handler, instead of transforming the problem once (S18 pp. 4–5) | [stated, joint] P |
| Minimum evidence | GCG 0.7 against SCIP 1.2.0.5 on three structures (S18 pp. 8–10). (1) Capacitated p-median: GCG faster in shifted geometric mean; most-fractional branching doubles the time; a dynamic-programming knapsack pricer cuts it by more than 60%. (2) Bin packing: all 540 instances in under 90 minutes in total. (3) A temporal-knapsack resource-allocation problem with no block structure, where the capacity rows were split into blocks of 32 or 64: GCG solved 56 of 70 within an hour against 5 of 70 for SCIP, about four times faster | [practice, joint] P |
| Abandoned paths | The transform-then-solve design was rejected (S18 p. 5). In 0.7 the user had to supply the structure in a file (S18 p. 4); version 1.0 adds structure detectors (S30, CHANGELOG section 1.0). Test sets were thinned, e.g. every second p-median instance, to save computing time (S18 p. 9) | [stated, joint] P; [practice] P |
| Reception | 137 Google Scholar citations (S1). GCG 3.0's detection produced the ten decomposition features of MIPLIB 2017 (S29 p. 16). GCG is part of the SCIP Optimization Suite (S27 abstract; S28). The book's later motivation for GCG: a cheap estimate of whether branch-and-price will succeed, before investing in a custom implementation (S15 p. 509) | [observed] / [stated, joint] P |
| Method shown | CM1 (generic over a maintained framework) | — |

### SW3 · *Partial Convexification of General MIPs* (W29, IPCO 2011), then *Automatic Dantzig–Wolfe Reformulation of MIPs* (W38, Math. Program. 2015)

| Dimension | Finding | Tag / source |
|---|---|---|
| Origin | SEA 2010 closes on an open question: whether a significant share of MIPs benefit from decomposition even without known structure (S18 p. 11). IPCO 2011 asks three questions of increasing ambition and notes that the community leaned toward answering the last one in the negative (S19 pp. 1–2). The Bologna and Milano co-authors had supplied the SEA 2010 instances (S18 acknowledgment) | [stated, joint] P; [inferred] that the collaboration grew from the instance exchange |
| Why then | Matrix re-ordering into bordered block-angular form and hypergraph partitioning (hMETIS) had long existed but had never been combined with DWR for MIPs (S20 p. 2). MIPLIB 2010 and the new attention to performance variability set the test context (S20 p. 3) | [stated, joint] P |
| Key insight | Almost any MIP matrix can be forced into a single- or double-bordered block-diagonal form by hypergraph partitioning. A cheap proxy, the relative border area, then ranks the candidate decompositions (S20 pp. 2–3, 16–20) | [stated, joint] P |
| Minimum evidence | IPCO 2011 (S19 pp. 5–8). Dynamic 0-1 knapsack instances were solved in minutes where CPLEX 12.2 hit the one-hour limit. On eight selected MIPLIB 2003 instances the dual bounds beat CPLEX's root bound with cuts | [practice, joint] P |
| Abandoned paths | (a) A third of MIPLIB 2003 was set aside as too hard or too big (S19 p. 6). (b) Several candidate quality measures showed inconsistent effects and were dropped: coupling constraints, linking variables, integers per block, objective-gradient angle (S19 p. 8). (c) The assumption that a matrix has one correct decomposition was abandoned, as a lesson from the preliminary experiments (S20 p. 8). (d) A referee's feedback led to a more meaningful experimental set-up (S20 p. 28) | [stated, joint] P |
| Reception | MP 2015: 105 citations; IPCO: 31 (S1). Two revision rounds (S20 p. 1). The detection ideas went into GCG (S15 p. 238). MIPLIB 2017 uses an area score for GCG's decompositions (S29 p. 16). The co-authored book credits Bergner et al. with pioneering graph partitioning for automatic DWR (S15 p. 284); that is self-reception, not independent | [observed]; [inferred] lineage from relative border area to area score (both measure the share of the matrix outside the blocks) |
| Method shown | CM2 (proof-of-concept against the field's reservation), CM3 (map the choice space, then score it) | — |

### SW4 · *Learning When to Use a Decomposition* (W47, CPAIOR 2017)

| Dimension | Finding | Tag / source |
|---|---|---|
| Origin | MP 2015 ends with the hope that one could soon tell from the instance alone whether DWR pays (S20 p. 27). The CPAIOR abstract: a detected structure that fits makes the reformulated model much faster; one that does not can make the solver fail completely (S23). His GERAD biography gives this work as the example of his interest in machine learning for integer programming (S10) | [stated, joint] P; [stated] P |
| Why then | GCG had compared decompositions from several detectors since version 1.0 (S30, CHANGELOG section 1.0), and GCG 3.0 keeps a pool and selects by a score (S29 p. 16). A generic solver therefore needed a rule for choosing among candidates and for whether to decompose at all. The wider ML-for-MIP context was not researched here | [practice] P for the code facts; [inferred] for the motivation |
| Key insight | Treat the decision whether to decompose, and with which decomposition, as supervised classification on instance features (S23) | [stated, joint] P |
| Minimum evidence | Preliminary experiments: a significant improvement on structured instances, little deterioration on the others (S23). Features, learner and test set: not read | [stated, joint] P (abstract only) |
| Abandoned paths | Not known; the full text was not read | — |
| Reception | 157 Google Scholar citations, 104 in Semantic Scholar (S1, S3). Mitrai and Daoutidis (2023) list it among classification approaches to algorithm selection for MILP and MIQP, and extend the question to convex MINLP (branch-and-bound against outer approximation) (S31 p. 2; reference [40] on p. 9). The co-authored book calls machine learning the future and cites the paper (S15 pp. 238, 284, 552) | [observed] S |
| Method shown | CM3, third step: learn the choice | — |

### SW5 · *Branch-and-Price* (W64; Cahier G-2024-36, Springer 2026)

| Dimension | Finding | Tag / source |
|---|---|---|
| Origin | The book idea dates from around 2000; the first trace is a January 2001 email from Desrosiers. Nothing was written for 15 years. A subversion repository was opened on 14 January 2015, and its first commit, by luebbecke, expected completion in 2015, 2016 or 2017. A 16-chapter outline existed by 26 January 2015 (S15 p. xiii). The Foreword: column generation schools since 2006 (Montréal, Darmstadt, Paris) and workshops since 2008, with slides that evolved across editions (S15 p. xii) | [stated, joint] P; the Foreword is [observed] (Soumis) |
| Why then | The need for a standard text was more pressing than ever, and colleagues kept asking what to read (S15 pp. xiii, xv) | [stated, joint] P |
| Key insight | Unify the notation and concepts across hundreds of application papers. Branch-and-price is column generation at every node, and Dantzig-Wolfe is a reformulation, by convexification or by discretization (S14; S15 p. xiv) | [stated, joint] P |
| Minimum evidence | Not applicable (a book). The Preface says writing exposed supposed facts they had taken for granted that were wrong, missing details and never-formalized notions (S15 p. xiii) | [stated, joint] P |
| Abandoned paths | The 2015–17 target date. The 16 planned chapters became 8 (S15 p. xiii; contents). 25 advanced subjects are deferred to possible later books (S15 p. 552), including several from his own co-authored lines: row-reduced column generation, vector space decomposition, cycle-canceling, nested column generation, machine learning, implementation. The four authors compromised and left topics out (S15 p. xv). The book states that no line was generated by a language model (S15 p. xv) | [stated, joint] P; [inferred] the mapping to his own lines |
| Reception | Springer open access in February 2026 (S11; S15 p. xv). 86 Google Scholar citations on the book entry (S1), 31 in Semantic Scholar (S3) | [observed] S |
| Method shown | CM4 | — |

### 2.6 Secondary lines, not dissected

- (a) The GERAD LP and degeneracy line, 2011–2018 (W34, W35, W39, W42, W46, W53). It is Gauthier's doctoral programme (S15 p. viii), and most of it reaches Operations Research and EJOR.
- (b) DW reformulation strength, 2015–2018 (W50–W52), Witt's doctoral programme (S8). W52 computes and solves the relaxations of all subsets of constraints to convexify on small integer programs. It finds that only a few distinct dual bounds occur and that textbook-style constraint choices matter most (S21 p. 1). This is an exhaustive-enumeration style of experiment.
- (c) Applications: railways and logistics (W4, W14, W19, W33, W56), production (W22), timetabling (W18, W32, W41), energy (W43), robotics (W48), politics (W57), stations (W66).
- (d) Recoverable robustness (W21): his fourth most cited work, outside the MILP lens.

---

## 3. Failures, abandoned directions, rejections, renamed items

1. **Career rejections.** [stated, joint; third person] After the PhD he applied for postdoctoral posts in the US and Canada and received only rejections. The RWTH chair came to him in 2010, his first permanent position, after five others had declined it (S15 p. vi).
2. **Book scope and time overruns.** The book took about 11 years from the start of writing against a planned 1–3, shrank from 16 planned chapters to 8, and deferred topics (S15 pp. xiii, xv, 552). [stated, joint] P; [practice] P.
3. **Directions the thesis left out** [stated] (S16 pp. 116, 157). No branch-and-price: price-and-branch was enough, because the restricted master always came out integer on the data. It recommends branch-and-price as a fail-safe reserve in an industrial system. No polyhedral study of the weak compact model. Deterministic setting only. The pricing algorithm is the bottleneck when admissible patterns become many.
4. **Prediction against timeline.** In March 2010 a public generic implementation needing little user interaction was predicted within months rather than years (S18 p. 2). The GCG 1.0 tag, the first version with detectors, is dated July 2012 (S30). [practice] P; whether that date is the public release date is unverified (C3).
5. **Automatic DWR, limits stated in the papers** [stated, joint] P:
   - IPCO 2011: a third of MIPLIB 2003 excluded; computing time not competitive on two of the eight showcased instances (S19 pp. 6, 8).
   - MP 2015: the automatic choice was fastest on about 8% of the 39 instances, and up to two orders of magnitude slower on about half (S20 p. 25).
   - MP 2015 also warns that the ubiquitous arrowhead structure may be an artifact of the detection model (S20 p. 27), and that an a-priori theory of good decompositions is out of reach (S20 pp. 27–28).
   - It does not expect decomposition ever to be the single best approach to MIP (S20 p. 27).
6. **Bad structure means failure** (W47): the abstract states that a detected structure that does not fit can make the solver fail completely (S23).
7. **Limited efficacy** (W60): the Benders cuts help little on classical problems and mainly on temporally decomposable models (S22, OO 2019/02/7096 abstract).
8. **Not an overall winner** (W32): the algorithm is not the overall competition winner but is robust without tuning (S25). The 2008 preprint title promised optimal solutions to the Udine instances; the published title promises new ones (C10).
9. **A rejected recommendation** (W10): classical Dantzig-Wolfe as a pricing scheme for large LPs is not recommended (S17 p. 24). A rejected design (W23): transform-then-solve (S18 p. 5).
10. **Superseded or renamed working papers** [practice]:
    - G-2011-66 (*Improved column generation for highly degenerate master problems*) was followed by G-2013-09 and EJOR 2014 under a new title (S11).
    - Scholar rows without a venue look like earlier titles of later papers. *Eliminating redundant columns from column generation subproblems using classical Benders' cuts* corresponds to W60. *Vector Space Decomposition for Network Flow and Linear Problems* and *A minimum weighted mean cost cycle algorithm for linear programming* correspond to the W53/W39 line (S1) [inferred correspondence; not entered as works].
11. **Not found:** any public record of a rejected paper (journals publish no reviews). The process traces are revision dates (1.9) and acknowledgments (S20 p. 28).

---

## 4. Candidate methods surfaced by this dimension (for Phase 2 cross-checking)

These are candidates only. Each still needs the say-do check against 02 and 03.

| ID | Candidate | Evidence (said / done) | SWs |
|---|---|---|---|
| CM1 | Make a specialist method generic by building it into an existing, maintained open MIP framework, so that it inherits the framework's components. Benchmark it against that framework's own branch-and-cut on the same instances | said: S18 pp. 1–2, S15 p. 509. Done: S18 pp. 8–10, S30, S29 p. 16. Counter-evidence: W66 and W67 bypass GCG (1.8) | SW2 |
| CM2 | Treat the field's reservation as a hypothesis to test. Present the result as a computational proof of concept, not as a competitive tool, and list the method's disadvantages | said and done: S19 pp. 1–2, 9; S20 pp. 2, 27 | SW3 |
| CM3 | When success hinges on a choice with many options, first map the option space (parameter sweeps, exhaustive enumeration on small instances), then derive a cheap proxy score, then learn the choice | done: S19 p. 8 → S20 pp. 16–20 → S21 p. 1 → S23 → S29 p. 16 | SW3, SW4 |
| CM4 | Use synthesis writing as a research instrument: unify notation, consolidate a field, and let writing expose what is not understood | said: S16 p. 156, S15 pp. xiii–xv, S32. Done: W10, W11, W27, W28, W64 | SW1, SW5 |
| CM5 | Start from an industrial problem. Simplify pragmatically, but name the safeguard and list the limitations explicitly | said and done: S16 pp. 116, 153–158; S25; S22 (Kiel Canal abstract) | thesis, applications |
| CM6 | Read column generation through its duals: dual-based pruning, stabilization, dual inequalities | done: W12, S16 §4.2.5 (p. 109), S17, S15 Ch. 6 | SW1 |
| CM7 | Publish a conference version first for feedback, the journal version later | said: S32. Done: 1.6 | — |
| CM8 | Run a long-lived partnership with a division of labour: GERAD for LP and column generation theory, RWTH for code and generic experiments | done: S10, S15, the W34–W53 line against the GCG line | — |

---

## 5. Era and resource context

| Period | Compute and tools | Team | Seniority | Source |
|---|---|---|---|---|
| 1998–2001 | Research prototype on a 700 MHz Pentium III with 1 GB, Linux 2.2, CPLEX 7.0 callable library, gcc -O3. Three industrial data sets; BMBF grants 03-ZI7BR2-1 and 03-ZIM2BS | doctoral student in Zimmermann's group | PhD | S16 pp. vi, 124 |
| 2002–2005 | Survey writing between Berlin and Montréal | 2 authors | postdoc, TU Berlin | S17 p. 1 |
| 2009–2010 | GCG 0.7 on SCIP 1.2.0.5 with CPLEX 12.1 as LP solver; Core2 Quad 2.66 and 2.83 GHz, 4 and 16 GB; one-hour limit; shifted geometric means (shift 10 for time and nodes, 100 for gap) | master's student (Gamrath) and Lübbecke | visiting professor, Darmstadt | S18 pp. 1, 8 |
| 2010–2013 | CPLEX 12.2 single thread and hMETIS (seed 1); Intel i7-870 at 2.93 GHz with 8 GB; one-hour limit. DFG Priority Program *Algorithm Engineering*, grants LU770/4-1 and 4-2 | 7 authors across RWTH, Bologna, Milano, Paris | chair holder | S19 p. 5; S20 pp. 1, 10 |
| 2015–2018 | GCG 2.1.4 (2018); GCG 3.0 used for the MIPLIB 2017 features | RWTH doctoral students (Bastubbe, Witt) | chair holder | S21 p. 3; S29 p. 16 |
| 2015–2026 | Book written in a subversion repository by four authors in Aachen, Montréal and Mainz; no language-model use declared | 4 | senior | S15 pp. xiii–xv |
| 2024–2026 | SCIP 8.0.2 with Gurobi 9.5.2 on a 128 GB machine (W66). SCIP 9.2.3 with SoPlex 7.1.5 in C++, code on Zenodo (W67). One-hour limits | 4-author teams with doctoral students and external co-authors | senior | S22 (MSLP p. 22); S26 p. 23 |

---

## Contradictions

Kept as found; not reconciled.

- **C1 · Generic versus ad hoc.** The 2004 survey says generic integer-programming column generation codes already solve many problems of industrial difficulty that standard MIP solvers cannot (S17 p. 24). The 2010 GCG paper says almost every branch-and-price application is ad hoc and started from scratch (S18 p. 1). Both texts are joint. [inferred] The two may use *generic* in different senses: problem-class codes against MIP-generic ones. The sources do not say.
- **C2 · Tailoring versus automation.** In 2001 and 2004 column generation still needs customization and tailoring, and all components benefit from it (S16 p. 157; S17 p. 24). From 2010 the agenda is automatic, generic decomposition (S18 pp. 1–2; S10). The 2026 book calls branch-and-price in principle a general method for general MILPs and adds that tailoring still helps (S15 p. 238). Meanwhile his 2024–26 tailored studies (W66, all four authors at RWTH; W67, with Sapienza Rome and TU Eindhoven co-authors; affiliations per the title pages) were built directly on SCIP, not on GCG (S26 pp. 1, 23; S22).
- **C3 · The prediction and the timeline.** In March 2010 a public generic implementation was predicted within months, not years (S18 p. 2). The GCG 1.0 tag is dated 2012-07-31 (S30). The November 2013 revision of MP 2015 still calls the automatic approach a proof of concept, not a competitive tool (S20 p. 27). A tag date is not necessarily a release date.
- **C4 · Framing against numbers in the same paper.** MP 2015 lists among its contributions that a non-negligible fraction of instances get globally better performance than state-of-the-art solvers (S20 p. 3). Its own profile shows the automatic choice fastest on about 8% of instances (S20 p. 25). Both statements stand in the paper.
- **C5 · The book's page counts and dates.** The Cahier page gives 657 pages (S14). The GERAD book list gives 689 for the Cahier and 663 for Springer (S11). The PDF I read has 695 pages. The Cahier cover reads June 2026, the inner title page June 2024 (S15 PDF pp. 1–2).
- **C6 · Citation counts across databases.** *Selected Topics*: 1,716 (S1) against 1,331 (S3). MIPLIB 2017: 531 (S1), 347 (S3), 182 (Crossref, S5). For the encyclopedia entry *Column generation*, S1 gives 180, while S3 has a 595-citation *Column Generation* (2010) record under a SpringerReference DOI, likely a conflated record.
- **C7 · Years and volumes.**
  - *Combinatorially simple pickup and delivery paths*: 2004 in S1, 2002 in S3.
  - *Selected Topics*: dated 2002 in S3 (the Cahier date), published 2005.
  - Zeitschrift für Parlamentsfragen volume: 50 in Crossref and S1, 51 in the GERAD list (S11).
- **C8 · Author-order metadata.** Optimization Online sometimes lists authors in an order that contradicts the byline: Desrosiers before Lübbecke for W10, Karwan first for W63 (S22, S33). Other entries, e.g. W66, follow the byline. Scholar has a duplicate W47 row with Parmentier first (S1). Use bylines only.
- **C9 · A Scholar row in two forms.** S1 shows *Yet another note on "An efficient zero-one formulation of the multilevel lot-sizing problem"* (1998) both as sole-authored and as a three-author report (Bussieck, Fink, Lübbecke). No identifier, so it is not entered.
- **C10 · Timetabling title.** The 2008 preprint title speaks of optimal solutions to the Udine instances (S3, S8). The published title speaks of new solutions, and the abstract says the first set was solved to proven optimality and the competition set was not (S25). This is a scope change, not a retraction.

## Gaps

- **G1.** *Learning When to Use a Decomposition* (W47), full text not read: no open copy found on HAL, Optimization Online or through WebSearch. Only the Springer abstract was read.
- **G2.** Other full texts not read: the SEA 2012 status report (W30), the Primer (W11), the encyclopedia entries (W27, W28), the published OR 2005 version (only the October 2004 preprint was read).
- **G3.** Habilitation (TU Berlin, 2007): title and content not found. DNB SRU has no record. Agent 06 also found none.
- **G4.** First public GCG release date: the CHANGELOG is undated and GitHub has no release objects, only tag commit dates. gcg.or.rwth-aachen.de and www.or.rwth-aachen.de timed out again on 2026-11-08.
- **G5.** DBLP: the SPARQL snapshot ends in 2023, so DBLP entries for 2024–2026 were not seen. dblp.org itself was not queried (bot wall).
- **G6.** Semantic Scholar per-paper data (influential citations, open-access links): HTTP 429 on every batch call.
- **G7.** OpenAlex not queried (no API key).
- **G8.** Student list incomplete: no dissertation records found for Bergner, Puchert, Bastubbe, Kruber or Mühmer, and the supervisor of Gamrath's master's thesis is not verified.
- **G9.** No rejection or review record found for any paper; journals publish no reviews.
- **G10.** Scholar rows without identifiers, not entered as works:
  - the 1996 Diplom thesis (*Algorithmen zur Enumeration der Ecken und Facetten konvexer Polyeder*);
  - *Primal heuristics for mixed integer programs with a staircase structure* (RWTH report 2015);
  - *Using VRPSolver's Price-and-Cut Engine within GCG* (Mühmer, Lübbecke, Uchoa; no venue or year);
  - *Modular detection of model structure in integer programming* (SCIP Workshop 2018);
  - *Computational Mixed Integer Programming* (2008);
  - *Recoverable robustness* (ARRIVAL TR-0066, 2007);
  - the precursor titles in §3 item 10.
- **G11.** How the collaborations with Parmentier (W47) and on the Kiel Canal (W56) began: not documented here.
- **G12.** The 2021 Cassyni posting (DOI 10.52843/cassyni.42wn2q): not opened; probably a talk, so a lead for agent 02.
- **G13.** SCIP Optimization Suite 5.0 and 7.0 author lists: not checked directly. His absence is inferred from S1 and S33.

## Sources

- S1 — Google Scholar profile "Marco Lübbecke" (cYIpR60AAAAJ), list views by date (rows 1–118) and by citations (top 30), via WebFetch, 2026-11-08 — https://scholar.google.com/citations?user=cYIpR60AAAAJ — secondary
- S2 — DBLP person 24/5951 via sparql.dblp.org (`scripts/dblp_works.py`, patched local copy), 58 records 1998–2023, 2026-11-08 — https://dblp.org/pid/24/5951.html — secondary
- S3 — Semantic Scholar author 1761286, paper list (100 papers), 2026-11-08 — https://api.semanticscholar.org/graph/v1/author/1761286/papers — secondary
- S4 — ORCID 0000-0002-2635-0522, public works (60 groups) — https://pub.orcid.org/v3.0/0000-0002-2635-0522/works — secondary
- S5 — Crossref REST API: author queries (Lübbecke, Luebbecke, Lubbecke, from 2016 and 2021) and single-DOI checks — https://api.crossref.org — secondary
- S6 — arXiv author searches (Lübbecke, Luebbecke, Lubbecke): 6 results, 4 with Marco Lübbecke — https://arxiv.org/search/?searchtype=author&query=L%C3%BCbbecke — secondary
- S7 — DataCite API: thesis DOI 10.24355/DBBS.084-200511080100-720; RWTH dissertations listing Lübbecke as contributor — https://api.datacite.org — secondary
- S8 — Deutsche Nationalbibliothek SRU, query per=Lübbecke and per=Marco (53 records) — https://services.dnb.de/sru/dnb — secondary
- S9 — HAL API search, authFullName "Lübbecke" (14 records; no copy of W47) — https://api.archives-ouvertes.fr/search/ — secondary
- S10 — GERAD profile "Marco Lübbecke", first-person biography (undated; written after December 2018 and before June 2024, inferred from its text), accessed 2026-11-08 — https://www.gerad.ca/en/people/marco-lubbecke — primary
- S11 — GERAD publication list for Marco Lübbecke (26 items) and GERAD news of 2026-02-06 — https://www.gerad.ca/en/people/marco-lubbecke/publications — secondary
- S12 — GERAD Cahier G-2002-64 page, *Selected Topics in Column Generation* (December 2002, revised March 2004, 35 pp.) — https://www.gerad.ca/en/papers/G-2002-64 — primary
- S13 — GERAD Cahier G-2004-02 page, *A Primer in Column Generation* (January 2004, revised July 2004) — https://www.gerad.ca/en/papers/G-2004-02 — primary
- S14 — GERAD Cahier G-2024-36 page, *Branch-and-Price* (June 2024, revised January 2026) — https://www.gerad.ca/en/papers/G-2024-36 — primary
- S15 — Desrosiers, Lübbecke, Desaulniers, Gauthier, *Branch-and-Price*, Les Cahiers du GERAD G-2024-36, revised January 2026 (PDF, 695 pp.); Springer 2026, DOI 10.1007/978-3-031-96917-1 — https://www.gerad.ca/papers/G-2024-36.pdf — primary (joint)
- S16 — Lübbecke, *Engine Scheduling by Column Generation*, Dr. rer. nat. thesis, TU Braunschweig, submitted 16 May 2001, defended 12 July 2001 (DNB archive copy) — DOI 10.24355/DBBS.084-200511080100-720; https://d-nb.info/962821152/34 — primary (sole)
- S17 — Lübbecke and Desrosiers, *Selected Topics in Column Generation*, preprint of 2 December 2002, revised 9 March 2004 and 21 October 2004 — https://optimization-online.org/2002/12/580/ — primary (joint)
- S18 — Gamrath and Lübbecke, *Experiments with a Generic Dantzig-Wolfe Decomposition for Integer Programs*, TU Berlin preprint 2010/05 (posted 2010-03-01, updated 2010-04-13) — https://optimization-online.org/2010/03/2556/ — primary (joint)
- S19 — Bergner, Caprara, Furini, Lübbecke, Malaguti, Traversi, *Partial Convexification of General MIPs by Dantzig-Wolfe Reformulation*, preprint (2010-11-16) — https://optimization-online.org/2010/11/2819/ — primary (joint)
- S20 — Bergner, Caprara, Ceselli, Furini, Lübbecke, Malaguti, Traversi, *Automatic Dantzig-Wolfe Reformulation of Mixed Integer Programs*, manuscript of 20 September 2011, revised 20 September 2012 and 1 November 2013 — https://optimization-online.org/2012/09/3614/ — primary (joint)
- S21 — Bastubbe, Lübbecke, Witt, *A Computational Investigation on the Strength of Dantzig-Wolfe Reformulations*, RWTH report 2018-047 — https://optimization-online.org/2018/02/6485/ — primary (joint)
- S22 — Optimization Online abstract pages, joint works, 2026-11-08 — primary (joint):
  - 2014/12/4681 (Kiel Canal)
  - 2015/11/5208 (stable set strength)
  - 2015/02/4790 (generic cuts; metadata only)
  - 2017/11/6331 (hypergraph separation)
  - 2019/02/7096 (Benders cuts in pricing)
  - 2020/04/7760 (image-based similarity)
  - the 2024/04 MSLP page and PDF (set-up section p. 22)
  - https://optimization-online.org/
- S23 — Springer page, Kruber, Lübbecke, Parmentier, *Learning When to Use a Decomposition*, CPAIOR 2017, pp. 202–210 (abstract) — https://doi.org/10.1007/978-3-319-59776-8_16 — primary (abstract only)
- S24 — Springer page, Lübbecke, *Automatic Decomposition and Branch-and-Price—A Status Report*, SEA 2012, pp. 1–8 (abstract) — https://doi.org/10.1007/978-3-642-30850-5_1 — primary (abstract only)
- S25 — Springer page, Lach and Lübbecke, *Curriculum based course timetabling: new solutions to Udine benchmark instances*, Ann. Oper. Res. 194 (2012), online 2010-02-05 (abstract) — https://doi.org/10.1007/s10479-010-0700-7 — primary (abstract only)
- S26 — Ciccarelli, Furini, Hojny, Lübbecke, *Branch-and-price strikes back for the k-vertex cut problem*, arXiv 2602.04984 (abstract page; v2 PDF, set-up p. 23) — https://arxiv.org/abs/2602.04984 — primary (joint)
- S27 — *The SCIP Optimization Suite 9.0*, arXiv 2402.17702 (31 authors; Mühmer listed, Lübbecke not) — https://arxiv.org/abs/2402.17702 — secondary (observed authorship)
- S28 — *The SCIP Optimization Suite 10.0*, arXiv 2511.18580 (34 authors, including Lübbecke and Mühmer) — https://arxiv.org/abs/2511.18580 — primary (joint; author list and abstract only)
- S29 — Gleixner et al., *MIPLIB 2017* preprint: committee footnote p. 2, contributor table p. 6, §4.5 pp. 15–16 — https://optimization-online.org/2019/07/7285/ — primary (joint)
- S30 — scipopt/gcg on GitHub: CHANGELOG (release notes 0.4–5.0, undated) and tag commit dates via the GitHub API (`gh api repos/scipopt/gcg/commits/<sha>`), 2026-11-08 — https://github.com/scipopt/gcg — primary (group code)
- S31 — Mitrai and Daoutidis, *Taking the human out of decomposition-based optimization via artificial intelligence: Part I. Learning when to decompose*, arXiv 2310.07068 (2023-10-10) — https://arxiv.org/abs/2310.07068 — secondary (reception)
- S32 — Lübbecke, *How to write a paper*, blog post, 21 November 2014 — https://mluebbecke.wordpress.com/2014/11/21/how-to-write-a-paper/ — primary (stated)
- S33 — Optimization Online search listings (queries Lübbecke, Luebbecke, Lubbecke and four title queries), 2026-11-08 — https://optimization-online.org/?s=Luebbecke — secondary
- S34 — WebSearch result lists, 2 queries (open copies of W47 and of W10); used only as leads: MaRDI portal, IP Paris research portal, researchr, TU Berlin DepositOnce handle 11303/15544, TU Berlin COGA report 008-2004 — secondary, not used as evidence
