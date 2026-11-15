# Matteo Fischetti · 01 · Publication landscape and signature works

| | |
|---|---|
| Researcher | Matteo Fischetti, DEI, University of Padova (DBLP pid 47/4770; ORCID 0000-0001-6601-0568; Google Scholar user 5rOdaqAAAAAJ, linked from his DBLP page; Semantic Scholar author 2853454). Born 1958; Laurea (1982) and PhD (1987) at the University of Bologna, per his homepage (S8). Lens per team.json: MILP solver engineering (primal heuristics, Benders, cut loops, symmetry, performance variability) |
| Not to be confused with | Martina Fischetti (DBLP 166/3608, ORCID 0000-0002-7673-6917), his co-author on wind-farm, COVID-distancing and matheuristics papers; Massimo V. Fischetti (DBLP 51/2216, materials science); Mark Fischetti (science journalist; the 1999 book "Weaving the Web: The Original Design and Ultimate Destiny of the World Wide Web" sits in a Semantic Scholar split record under Matteo's name, and "The cellular phone scare", IEEE Spectrum 1993, DOI 10.1109/6.214586, comes up in a Crossref author query for "M. Fischetti"). Semantic Scholar split record 2259113410 also holds a 2025 compost-machine paper (Recycling 10(2), DOI 10.3390/recycling10020062) that is outside his field: a homonym [inferred, not verified] |
| Dimension | Research agent 01 of 06: publication landscape and dissection of signature works (framework §二 Agent 1, §五) |
| Research date | 2026-11-08 |
| Sources consulted | 47, listed as S1–S47 under "Sources" (36 primary, 11 secondary). WebSearch: 2 of the 5 allowed calls (leads only; no claim rests on a search snippet). Everything else: `scripts/dblp_works.py` (DBLP SPARQL), curl on his homepage, papers, slides and theses folders, WebFetch on Google Scholar, the Semantic Scholar, Crossref, arXiv (HTML), GitHub and Zenodo APIs |
| Local corpus | `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep` plus the `RESOURCES.md` template: no user-supplied material. No `private/` folder exists; nothing private was opened |
| OpenAlex | not run: `OPENALEX_API_KEY` is not set |
| Living status | Living (team.json). Latest dated traces: arXiv 2610.07844 v3 submitted by him on 4 Nov 2026 (S7); newest file in his slides folder dated 2026-11-02 (S10) |
| Quotation policy | Findings are paraphrased with a pinpoint (preprint page = PDF page of the author's preprint on his site, which matches its printed page numbers; slide deck page = PDF page of the deck, which counts build-up overlays separately). Exactly one short verbatim sentence is quoted (marked). Check exact wording at the source before quoting downstream |

**Tags.**
- **[stated]**: said or written by Fischetti alone (sole-author paper, his slides, his homepage). **[stated, joint]**: a co-signed paper or deck in the "we" voice; the voice cannot be split among authors.
- **[practice]**: what the record shows was done (experiments, test sets, dates, what was published, posted or left unpublished).
- **[observed]**: what others recorded (citation databases, other people's code and papers).
- **[inferred]**: my inference; the basis is named.
- **P / S**: primary / secondary source.

**Reading depth.**
- Read in full (text): S15 (FP paper), S16 (FP talk), S27 (in-out CPAIOR paper), S30 (CORS 2015 deck), S32 (EURO 2012 deck), S39 (bracket-and-fix deck).
- Read in large part: S12 (local branching preprint pp. 1–16 of 24, as page images), S14, S31 (erraticism preprint, all but the tables), S29 (pp. 1–3, 11–13), S34 (pp. 1–3, 11–12, 22–23), S23 (pp. 1–5, 11–12 and references), S25 (abstract, intro, conclusions), S26, S35.
- Opening pages only: S13, S17, S18, S19, S24, S28, S33, S36, S37, S38, S40, S41 (pp. 1–13 of 18), S42.
- Metadata or abstract only: S1–S7, S20–S22, S43–S46. Not read: everything listed under Gaps G7.

---

## 1. Publication landscape

### 1.1 Record coverage

| Record | What it holds | Tag |
|---|---|---|
| DBLP pid 47/4770 (S1) | 144 records, 1987–2026: 106 articles, 26 conference papers, 7 CoRR preprints, 2 editorships (IPCO 2007, LNCS 4513, DOI 10.1007/978-3-540-72792-7; ATMOS 2008, OASIcs 9), 2 book chapters, 1 handbook entry; 136 with a DOI. Venues by count: Math. Program. 26, Oper. Res. 14, IPCO 10 | [observed] S |
| Homepage list (S8) | 142 numbered entries plus [124bis], 1986–2026, plus 8 items under his *Technical reports* heading (6 of them 2026 items, see §1.8). The page header says 143 publications | [stated] P |
| Google Scholar (S3, S4) | 20,048 citations (6,626 since 2021); h-index 75 (44); i10-index 135 (94), read 2026-11-08 | [observed] S |
| Semantic Scholar (S5) | Main record 2853454: 197 papers, 13,594 citations, h-index 61. Three small split records (2259113410, 2341349824, 2065674176) mix his papers with homonyms | [observed] S |
| Crossref author query (S6) | 145 items under "Matteo Fischetti"/"M. Fischetti" in the top 400 hits; 30 are absent from DBLP (early ORL papers 1986/1988, JASA 2000, book chapters, the 2017 TOP comment, the 2017 bilevel chapter, 2015–2025 chapters) | [observed] S |
| arXiv (S7) | 9 preprints, 2017–2026 (listed across §1.8, §2.7, SW1 and F10) | [practice] P |

DBLP misses at least: ORL 6 (1986) 283–284 (DOI 10.1016/0167-6377(86)90065-9); ORL 7 (1988) 181–187, "A new dominance procedure for combinatorial optimization problems" (DOI 10.1016/0167-6377(88)90025-9); Management Science 43 (1997) 1520–1536, "A polyhedral approach to the asymmetric traveling salesman problem" (DOI 10.1287/mnsc.43.11.1520); JASA 95 (2000) 916–928 (DOI 10.1080/01621459.2000.10474282); Applied Energy 278 (2020) 115617 (DOI 10.1016/j.apenergy.2020.115617); the SIAM chapter "Integer (Linear) Optimization" with Balas (2017, DOI 10.1137/1.9781611974683.ch5) (all checked in Crossref, S6). The landscape statistics below use DBLP and therefore undercount book chapters and applications.

### 1.2 Topics by five-year period (DBLP titles, keyword-classified; approximate)

Counts exclude the two ATMOS front-matter records. Classification is by title keywords (script in the scratch folder), so a title can land in only one bin.

| Period | n | Dominant topics (count) | Representative verified works | Tag |
|---|---|---|---|---|
| 1985–1989 | 6 | Bounding and B&B for TSP, vehicle scheduling (3); fixed job scheduling (2) | "An Additive Bounding Procedure for Combinatorial Optimization Problems", Oper. Res. 37 (1989) 319–328, DOI 10.1287/opre.37.2.319 (with Toth); fixed job schedule papers with Martello and Toth, Oper. Res. 35 (1987) 849–858, DOI 10.1287/opre.35.6.849, and Oper. Res. 37 (1989) 395–403, DOI 10.1287/opre.37.3.395 | [practice] |
| 1990–1994 | 13 | TSP/arborescence polyhedra and B&B (11); 4 sole-author papers | "Facets of the Asymmetric Traveling Salesman Polytope", Math. Oper. Res. 16 (1991) 42–56, DOI 10.1287/moor.16.1.42 (sole); ATS lifting with Balas, Math. Program. 58 (1993) 325–352, DOI 10.1007/BF01581274; directed CVRP B&B, Oper. Res. 42 (1994) 846–859, DOI 10.1287/opre.42.5.846 | [practice] |
| 1995–1999 | 16 | Cuts ({0,1/2}, mod-k) (6); TSP variants by branch-and-cut (5); railway crew (2) | "{0, 1/2}-Chvátal-Gomory cuts", Math. Program. 74 (1996) 221–235, DOI 10.1007/BF02592196 (with Caprara); GTSP branch-and-cut, Oper. Res. 45 (1997) 378–394, DOI 10.1287/opre.45.3.378; orienteering, IJOC 10 (1998) 133–148, DOI 10.1287/ijoc.10.2.133; set covering heuristic, Oper. Res. 47 (1999) 730–743, DOI 10.1287/opre.47.5.730 | [practice] |
| 2000–2004 | 18 | Cuts and polyhedra (5); TSP variants (4); railway (4); first general-MIP heuristics (2); first Benders (1) | Train timetabling, Oper. Res. 50 (2002) 851–861, DOI 10.1287/opre.50.5.851.362; **Local branching** (2003, SW1); CB cuts at IPCO 2004 (SW3) | [practice] |
| 2005–2009 | 26 | Closures and cuts (9); general-MIP heuristics (5); robustness (4) | **Feasibility pump** (2005, SW2); first Chvátal closure, Math. Program. 110 (2007) 3–20, DOI 10.1007/s10107-006-0054-8; "Light Robustness" (LNCS 5868, 2009) 61–84, DOI 10.1007/978-3-642-05465-5_3; New Dutch Timetable, Interfaces 39 (2009) 6–17, DOI 10.1287/inte.1080.0409 | [practice] |
| 2010–2014 | 24 | Cutting-plane schemes, Gomory, closures (10); symmetry, variability, branching, parallelism (7); heuristics (3) | Benders cut selection (2010) and in-out (2010) (SW3); "Lexicography and degeneracy: can a pure cutting plane algorithm work?", Math. Program. 130 (2011) 153–176, DOI 10.1007/s10107-009-0335-0; orbital shrinking (2012, §2.6); erraticism (2014, SW4); proximity search (2014, SW5) | [practice] |
| 2015–2019 | 25 | Bilevel and interdiction (6); ML and SGD (5); Benders (3); variability and parallel (3) | Redesigning Benders (2017, SW3); MIBLP solver, Oper. Res. 65 (2017) 1615–1637, DOI 10.1287/opre.2017.1650; DNN as 0-1 MILP (2018, §2.7); SelfSplit, Comput. Oper. Res. 93 (2018) 101–112, DOI 10.1016/j.cor.2018.01.011 | [practice] |
| 2020–2026 | 12 | ML (4); wind farms (2); heuristics (2); applications | Mixed-integer bilinear B&C, EJOR 282 (2020) 506–514, DOI 10.1016/j.ejor.2019.09.043; "Integrated Layout and Cable Routing in Wind Farm Optimal Design", Manag. Sci. 69 (2023) 2147–2164, DOI 10.1287/mnsc.2022.4470; fix-propagate-repair heuristic, MPC 17 (2025) 111–139, DOI 10.1007/s12532-024-00269-5; 2026 preprints (§1.8) | [practice] |

Turning points visible in the record [inferred from the dated works above]:
- **TP1, 2002–2005:** from problem-specific polyhedral work and branch-and-cut (TSP family, railway crew, set covering, cell suppression) to general-purpose MIP methods that call a black-box MIP solver as a subroutine (local branching, feasibility pump, closures optimised by MIP). He named this program *MIPping* in a 2005 plenary (S40 p. 3) and surveyed it in "Just MIP it!" (S42 p. 1; Matheuristics, Annals of Information Systems 10, 2010, 39–70, DOI 10.1007/978-1-4419-1306-7_2).
- **TP2, 2008–2014:** from new cut families to the *search scheme* around the separator (pure cutting planes with Balas and Zanette, yoyo/in-out, Benders cut selection) and to the solver's run-to-run behaviour (erraticism, random sampling, backdoor branching, SelfSplit).
- **TP3, 2015–2019:** *thinning out* models by projection (Benders for facility location, node-based Steiner models) and general-purpose bilevel solvers (with Ljubić, Monaci, Sinnl).
- **TP4, 2017–2021:** machine learning (DNN as 0-1 MILP; SGD minibatch persistency; simulated annealing inside SGD; learning the local-branching neighbourhood).
- **TP5, 2026:** sole-author, replication-package studies that revisit his own earlier claims (FP objective cutoff, minibatch persistency eight years later) and the EndoWake series with Martina Fischetti (§1.8).

### 1.3 Author position: alphabetical by default, so no first→last signal

Of the multi-author DBLP records, 15 are not in alphabetical surname order; all others are (S1, script output checked by hand: the script also flagged the 2006 De Franceschi–Fischetti–Toth VRP paper and the 2003 UMTS paper with Salazar González, but both are alphabetical once compound surnames are read correctly) [practice]. The exceptions show who led:
- Bologna railway and set-covering papers: the FS co-author Guida placed last (Math. Program. 79 (1997) 125–141, DOI 10.1007/BF02614314); Caprara, then Toth, with Fischetti last (Oper. Res. 46 (1998) 820–830, DOI 10.1287/opre.46.6.820; Ann. Oper. Res. 2000).
- Project leads from elsewhere: Kroon (NS crew scheduling, HICSS 2000, DOI 10.1109/HICSS.2000.926668; Edelman paper 2009, nine authors); Ljubić (prize-collecting Steiner tree: ALENEX 2005, "Solving the Prize-Collecting Steiner Tree Problem to Optimality"; Math. Program. 105 (2006) 427–449, DOI 10.1007/s10107-005-0660-x; Fischetti last of six).
- Students or junior co-authors first: Zanette (IPCO 2008, DOI 10.1007/978-3-540-68891-4_29; Math. Program. 2011, DOI 10.1007/s10107-009-0335-0, with Balas last); Fischetti–Zanette–Salvagnin (ATMOS 2007, "Fast Approaches to Robust Railway Timetabling"); Liu (CoRR 2021, AAAI 2022; Fischetti second); Cavaliere (MPC 14 (2022) 749–779, DOI 10.1007/s12532-022-00224-2, Fischetti last); Salvagnin and Roberti (MPC 2025; JORS 76 (2025) 2060–2070, DOI 10.1080/01605682.2025.2451738; Fischetti last in both). Outside DBLP, the 2025 AIRO chapter puts Palasgo first and Fischetti second (S6).

Reading [inferred]: position carries information only when the order breaks the alphabet. Since 2022, in such breaks with Padova and Bologna co-authors he is last, behind a younger first author.

Sole-author papers: three in 1990–1991 (subset-sum approximation scheme, Discrete Appl. Math. 26 (1990) 61–77, DOI 10.1016/0166-218X(90)90021-4; ATS facets, DOI 10.1287/moor.16.1.42; Steiner arborescence facets, Math. Program. 51 (1991) 401–419, DOI 10.1007/BF01586946), a 1992 IPCO paper ("Three Facet-Lifting Theorems for the Asymmetric Traveling Salesman Polytope", IPCO II, 260–273) and a 1995 DAM paper (clique tree inequalities, Discrete Appl. Math. 56 (1995) 9–18, DOI 10.1016/0166-218X(93)E0082-A), plus the 1986 ORL note that DBLP lacks; then rare (CPAIOR 2010 invited abstract "Towards a MIP-Cut Metascheme", DOI 10.1007/978-3-642-13520-0_1; Discrete Optim. 22 (2016) 183–194 on SVM training, DOI 10.1016/j.disopt.2015.03.002; the TOP 2017 comment and the 2017 bilevel chapter, S6); then two sole-author studies in 2026 (§1.8) [practice].

### 1.4 Collaboration network and likely students

| Cluster | Co-authors (DBLP joint records) | Period | Tag |
|---|---|---|---|
| Bologna school | Paolo Toth 22, Alberto Caprara 14, Silvano Martello 6, Daniele Vigo 4, Carpaneto 2, Dell'Amico | 1987–2006 | [observed] S1 |
| Carnegie Mellon / polyhedral | Egon Balas 11 (ATS polytope 1992–1999; pure cutting planes 2008–2012) | 1992–2012 | [observed] S1 |
| Padova and Bologna MIP group | Michele Monaci 25, Domenico Salvagnin 24, Andrea Lodi 17, Arrigo Zanette 8, Tramontani | 2002–2026 | [observed] S1 |
| Vienna / ESSEC | Ivana Ljubić 9, Markus Sinnl 8, Leitner, Luipersbeck, Resch, Kahr, Ruthmair | 2005–2019 | [observed] S1 |
| Applications | Leo Kroon 3 and the NS team (Edelman 2008); Juan José Salazar González 7 (two DBLP name variants; statistical disclosure, GTSP, orienteering); Romanin-Jacur (telecom) | 1995–2009 | [observed] S1 |
| Since 2015 | Martina Fischetti 4 (wind, COVID distancing, matheuristics); Roberto Roberti 3; Francesco Cavaliere 2; Defeng Liu 2 (with Lodi) | 2015–2026 | [observed] S1 |

Likely students [inferred from theses hosted in his `ricop/tesi/` folder (S11) plus later co-authorship; no thesis acknowledgment was read]:
- Doctoral theses hosted: Bettin (1998), Lodi (1999, file named as a doctoral thesis), Luzzi (2002/2003; nesting paper, J. Heuristics 15 (2009) 201–226, DOI 10.1007/s10732-008-9088-9), Bertacco (2005; FP for general integers), Salvagnin (2008), Zanette (2008).
- Laurea or short theses hosted that became joint papers: Saturni 2000 (cyclic-group cuts, Math. Program. 109 (2007) 27–53, DOI 10.1007/s10107-006-0726-4); Polo 2002 and Scantamburlo 2003 (local branching for 2-level variables, Networks 44 (2004) 61–72, DOI 10.1002/net.20017); Codato 2003 (CB cuts; the paper states its thesis origin, S23 p. 4); De Franceschi 2003 (VRP refinement heuristic, Math. Program. 105 (2006) 471–499, DOI 10.1007/s10107-005-0662-8); Andreello 2003 ({0,1/2}-cut embedding, IJOC 19 (2007) 229–238, DOI 10.1287/ijoc.1050.0162); Sartor 2012 (smart-grid matheuristic, ITOR 22 (2015) 49–59, DOI 10.1111/itor.12034); Mandatelli 2018 (minibatch persistency, arXiv 1806.07353); Stringher 2019 (SA inside SGD, arXiv 1906.01504; OLA 2021, DOI 10.1007/978-3-030-85672-4_1).
- Pattern [practice]: a master's thesis becomes a co-authored paper with the student as co-author, often within 1–3 years (Codato 2003 → IPCO 2004; Polo/Scantamburlo → Networks 2004; Mandatelli 2018 → arXiv 2018).

### 1.5 Usual venues

Mathematical Programming (26 DBLP records), Operations Research (14), IPCO (10), then Mathematical Programming Computation, INFORMS Journal on Computing, Discrete Optimization, EJOR, Networks, Management Science, CPAIOR (S1) [observed]. He sat on the editorial boards of Operations Research and Mathematical Programming Computation (and of JOCO and 4OR until 2015), chaired the IPCO 2007 and ATMOS 2008 programme committees (S8) [stated]. Since 2017 he has also posted ML-side preprints on arXiv (cs.LG) and published at AAAI and OLA [practice].

### 1.6 Most cited (Google Scholar, read 2026-11-08; S3)

| Rank | Work (identifier) | Scholar | S2 (S5) | Crossref (S6) |
|---|---|---|---|---|
| 1 | Local branching, Math. Program. 98 (2003) 23–47, DOI 10.1007/s10107-003-0395-5 (with Lodi) | 1,352 | 748 (73 influential) | 722 |
| 2 | Modeling and solving the train timetabling problem, Oper. Res. 50 (2002), DOI 10.1287/opre.50.5.851.362 (Caprara, Fischetti, Toth) | 881 | 640 | 485 |
| 3 | Algorithms for the set covering problem, Ann. Oper. Res. 98 (2000) 353–371, DOI 10.1023/A:1019225027893 | 705 | 491 | — |
| 4 | A heuristic method for the set covering problem, Oper. Res. 47 (1999), DOI 10.1287/opre.47.5.730 | 649 | 483 | — |
| 5 | GTSP branch-and-cut, Oper. Res. 45 (1997), DOI 10.1287/opre.45.3.378 | 643 | 453 | — |
| 6 | Combinatorial Benders' cuts for MILP, Oper. Res. 54 (2006) 756–766, DOI 10.1287/opre.1060.0286 (with Codato) | 641 | 484 | 364 |
| 7 | The feasibility pump, Math. Program. 104 (2005) 91–104, DOI 10.1007/s10107-004-0570-3 (with Glover, Lodi) | 627 | 464 | 349 |
| 8 | Deep neural networks and mixed integer linear optimization, Constraints 23 (2018) 296–309, DOI 10.1007/s10601-018-9285-6 (with Jo) | 514 | 360 | 242 |
| 9 | Solving the orienteering problem through branch-and-cut, IJOC 10 (1998), DOI 10.1287/ijoc.10.2.133 | 476 | 445 (102 influential) | — |
| 10 | Light robustness (2009), DOI 10.1007/978-3-642-05465-5_3 (with Monaci) | 416 | 259 | — |
| 11 | Redesigning Benders decomposition for large-scale facility location, Manag. Sci. 63 (2017) 2146–2162, DOI 10.1287/mnsc.2016.2461 (with Ljubić, Sinnl) | 366 | 256 | 209 |

Other signature-relevant counts (Scholar / S2 / Crossref): FP for general integers (2007) 216 / 173 / 116; A note on the selection of Benders' cuts (2010) 242 / 178 / 132; FP 2.0 (2009) 147 / 113 / 85; proximity search (2014) 124 / 89 / 68; exploiting erraticism (2014) 107 / 80 / 52; random sampling (2016) 49 / 24 / 14; orbital shrinking ISCO 2012 — / 23 / 15 and DAM 2017 48 / 11 / 11 [observed].

Reading [inferred]: three of the top seven are application-born railway and covering papers with Caprara and Toth (1999–2002); the MILP-methods signature (LB, CB cuts, FP) sits at ranks 1, 6, 7.

### 1.7 Recognition he lists (homepage, S8) [stated]

INFORMS Edelman Award 2008 (New Dutch Timetable, with the Netherlands Railways team); Harold Larnder Prize 2015 (plenary at CORS/INFORMS 2015, S30); 11th DIMACS Implementation Challenge winner 2014 (Steiner tree codes, with Leitner, Ljubić, Luipersbeck, Monaci, Resch, Salvagnin, Sinnl); COAP best paper 2016 (indicator constraints, Comput. Optim. Appl. 65 (2016) 545–566, DOI 10.1007/s10589-016-9847-8); Wagner Prize finalist 2004 (NS crew scheduling, Interfaces 35 (2005) 393–401, DOI 10.1287/inte.1050.0158); Ferrovie dello Stato code competitions FASTER 1994 (very large set covering, with Caprara and Toth) and FARO 1995 (rostering, with Caprara, Toth, Vigo); ORSA prize for the best PhD dissertation on transportation and AIRO best young researcher, both 1987. Plenary or keynote talks include ISMP 1997 (semiplenary), ISMP 2009, EURO 2012 (semiplenary), ISCO 2014, RAMP 2014, OR2015, CORS/INFORMS 2015, ISMP 2018 keynote, IFORS distinguished speaker at INFORMS 2020.

### 1.8 Recent works (since November 2025) and latest traces

| Item | Identifier | Status | Tag |
|---|---|---|---|
| Cavaliere, Fischetti, Roberti, Salvagnin, "Models and algorithms for the Time Window Assignment Traveling Salesperson Problem with stochastic travel times" | EJOR 329 (2026) 96–111, DOI 10.1016/j.ejor.2025.07.034 | published | [practice] S1 |
| Roberti, Salvagnin, Fischetti, assortment optimization compact formulation | JORS 76 (2025) 2060–2070, DOI 10.1080/01605682.2025.2451738 | published | [practice] S1 |
| Palasgo, Fischetti, Roberti, "Column Generation Algorithms for the Pickup and Delivery Problem with Time Windows and Last-in-First-out Loading" | AIRO Springer Series 14 (2025) 75–86, DOI 10.1007/978-3-031-85894-9_6 | published | [practice] S6, S8 |
| Fischetti, Fischetti, "Matheuristics by Examples", Handbook of Heuristics | DOI 10.1007/978-3-319-07153-4_14-2 (Crossref dates it 2024); also 10.1007/978-3-032-00385-0_14 (2025) | published | [practice] S6 |
| Fischetti, "Feasibility Pump with Objective Cutoff: A Computational Study" (sole author) | Manuscript in GitHub mfischetti-arch/fp-objective-cutoff (`paper/manuscript.pdf`); code Zenodo 10.5281/zenodo.22810777 (MIT, version label mpc-submission-1), raw SCIP logs 10.5281/zenodo.22810848 (CC BY 4.0) | submitted to Mathematical Programming Computation per README; **unreviewed** | [practice] P S19–S21 |
| Fischetti, "Minibatch persistency, eight years later: what batch reuse costs in steps and joules, and what it saves in data" (sole author) | arXiv 2609.13922 (12 Sep 2026) | preprint; arXiv comment says pre-registered (OSF, embargoed) | [practice] P S7 |
| Fischetti, Fischetti, "EndoWake: Modeling Wind by Linear Programming for Wind Farm Layout Optimization" | arXiv 2609.40157 (30 Sep 2026) | preprint | [practice] P S7 |
| Fischetti, Fischetti, "GPU-accelerated wind farm layout search with a distilled endogenous wake model (EndoWake)" | arXiv 2610.07844 (v1 6 Oct, v2 27 Oct, v3 4 Nov 2026); replication Zenodo 10.5281/zenodo.23955408 (v2.1.0; the DOI 10.5281/zenodo.22017446 in the arXiv comment resolves to it) | preprint; the v2 note says formal terms replaced the metaphors of v1 | [practice] P S7, S22 |
| Fischetti, Fischetti, "A Dantzig-Wolfe reformulation of the EndoWake model for optimal wind farm layouts" | arXiv 2610.39503 (29 Oct 2026) | preprint; the arXiv comment says it is under submission to a journal | [practice] P S7 |
| Fischetti, "A digital twin of Fermat in 1637: reconstructing the marvellous proof and locating where it fails" | ResearchGate only (listed on homepage S8 and Scholar S4) | **not read** | [practice] P |

Other 2026 traces in his slides folder (S10, not read): two AIROyoung 2026 lecture decks (branch-and-cut plus Benders; intersection cuts and bilevel), videos on backpropagation, EndoWake and SVM/telecom (2026-10/11). Working practice visible in the 2026 FP repository [practice, S20]: pinned SCIP/SoPlex commits, every table regenerated by a script from raw files, script comments in Italian (the README calls it the author's working language).

---

## 2. Signature works (dissection, framework §五)

**Selection.** By citations: LB (rank 1), CB cuts (6), FP (7), DNN (8), Redesigning Benders (11). By turning point: LB (TP1), erraticism and in-out (TP2), Benders redesign (TP3), DNN (TP4). By his own foregrounding (no explicit self-ranking found, Gap G1) [practice]: his homepage shows a photo captioned as the first slide of the very first Feasibility Pump talk (S8); his Aussois 2007 deck opens with the title slides of the 2002 LB talk and the 2004 FP talk before presenting a new heuristic (S39 pp. 2–3); his 2015 Larnder plenary picks orbital shrinking for QAP, the DIMACS Steiner codes and Benders for facility location as examples of *thinning out* models (S30 pp. 13–16); his 2018 ISMP keynote is about implementation, with the line, quoted verbatim (S41 p. 4): "Describing an Algorithm without Implementation is like stating a Theorem without Proof". The hint's list (FP, LB, proximity search, Benders with in-out, orbital shrinking, erraticism) matches these choices.

### SW1 · Local branching (Fischetti and Lodi; Aussois Jan 2002 → Math. Program. 98 (2003) 23–47, DOI 10.1007/s10107-003-0395-5)

| Dimension | Finding | Evidence / tag |
|---|---|---|
| Origin | The paper traces the idea to *soft fixing*, used as a refining tool on top of TURNI, a crew-scheduling heuristic (set-partitioning model, Lagrangian relaxation, hard variable fixing). On a real NS Reizigers instance (800+ drivers, 8,000+ trips) TURNI stopped at 833 duties after 41 CPU minutes; soft fixing then reached 809 duties after 55 more minutes (AMD Athlon 2100+). The first talk shows the TURNI variable-fixing plot and the hard-fixing failure mode: wrong early fixings are hard to detect because the lower bound stays flat and then jumps after an innocent-looking late fixing | S12 p. 3; S14 p. 9 · [stated, joint] P |
| Why then | A general-purpose solver (ILOG-Cplex 7.0) was strong enough to be the *tactical* engine inside an external *strategic* branching (the paper's terms); the paper argues for staying in a generic MIP framework instead of writing ad-hoc heuristics, to profit from the effort invested in MIP solvers. Railway crew work (FS, NS) supplied hard instances | S12 pp. 1–2 [stated, joint]; railway context S1, S8 [practice]; link between the two [inferred] |
| Key insight | Do not choose *which* binaries to fix, only *how many*: one linear (invalid) constraint bounding the Hamming distance to the incumbent defines a k-OPT-like neighbourhood that the black-box solver searches; branching on Δ ≤ k versus Δ ≥ k+1 keeps the overall scheme exact | S12 pp. 3–5 · P |
| Minimum evidence | Aussois 2002 runs on MIPLIB seymour and arki001 (CPLEX 7.0 plus LB with k = 10 against CPLEX's optimality and feasibility emphases); in the paper, tr24-15 on a Digital Alpha 533 MHz: LB found better incumbents early and finished in 1,878 s against 3,827 s for CPLEX in optimality mode | S14 pp. 5–7; S12 p. 6 · [practice] P |
| Test design | 29 hard instances (7 from MIPLIB 3.0, 22 collected from colleagues across crew scheduling, lot-sizing, telecom, nesting, railway line planning), none solvable to optimality in 5 CPU hours; instances posted online; k = 20; the authors say they deliberately avoided fine-tuning LocBra's parameters; LocBra ranked first on 23 of 29 | S12 pp. 1, 11–13 · [practice; stated, joint] P |
| Abandoned paths and limits | Hard variable fixing (the TURNI approach) is the path LB replaced. The paper concedes that faster optimality proofs are not guaranteed and leaves this to another study; its REFINE step was disabled on arki001 (too slow with general integers). Extensions listed but not tested: tighter integration in the solver, tabu or VNS search by branch-and-cut, infeasible reference solutions with penalised slacks, general-integer distance | S12 pp. 6, 12, 14–16 · [stated, joint] P |
| Follow-ups | 2-level variables (Networks 2004, with Polo and Scantamburlo, both thesis students); infeasible start realised in "Repairing MIP infeasibility through local branching", Comput. Oper. Res. 35 (2008) 1436–1445, DOI 10.1016/j.cor.2006.08.004; "Local Branching: Basics and Extensions", the first article in Optima 72 (January 2006); learning the neighbourhood size with Liu and Lodi, AAAI 2022, DOI 10.1609/aaai.v36i4.20294 (arXiv 2112.02195, retitled in v2 "Revisiting local branching with a machine learning lens") | S1, S13, S7 · [practice] P |
| Reception | Most-cited work (Scholar 1,352; S2 748, 73 influential; Crossref 722). SCIP ships `heur_localbranching.c`, whose header describes it as local branching according to Fischetti and Lodi (commit 353584f) | S3, S5, S6, S43 · [observed] S |
| Method it shows | M1 (black-box solver as subroutine), M2 (application trick generalised to any MIP), M4 (no parameter tuning in the evaluation) | §5 |

### SW2 · The feasibility pump (Fischetti, Glover, Lodi; Aussois Jan 2004 → Math. Program. 104 (2005) 91–104, DOI 10.1007/s10107-004-0570-3) and its 21-year lineage

| Dimension | Finding | Evidence / tag |
|---|---|---|
| Origin | Motivation as stated: local-search MIP heuristics (local branching; RINS and guided dives) only work once an incumbent exists, so the earlier a first feasible solution is found the better. Who had the core idea, and Glover's part, is not documented in anything read (Gap G2). The paper thanks Dimitris Bertsimas for discussions on randomness in rounding | S16 pp. 2–7; S15 pp. 1–2, 14 · [stated, joint] P |
| Why then | LB (2002) and RINS (Danna, Rothberg, Le Pape, Math. Program. 102 (2005) 71–90, DOI 10.1007/s10107-004-0518-7, online May 2004) made the first incumbent the bottleneck | S15 p. 2 [stated, joint]; S46 · [inferred] for the causal link |
| Key insight | Call a point of the LP polyhedron feasible when it coincides with its rounding; alternate rounding with an L1 projection back onto the polyhedron, so two trajectories each satisfy one half of feasibility. The paper also reads FP as a relaxed local branching: the distance requirement moves from a constraint into the LP objective | S15 pp. 1–3 · P |
| Minimum evidence | January 2004 talk, Pentium M 1.6 GHz notebook: on 37 hard 0-1 MIPs FP failed once, ILOG-Cplex 8.1 failed 18 times with feasibility emphasis and 8 times by default (root node). Final paper: 83 hard 0-1 MIPs; FP succeeded on 96.3% against 77.1% for the best-tuned CPLEX root; 3 failures against 19 | S16 p. 47; S15 pp. 1, 6, 12 · [practice] P |
| Abandoned and moved paths | (a) The talk's first implementation flipped the T highest-score variables deterministically (S16 pp. 37–38); the paper flips a random number in [T/2, 3T/2] and adds random restarts (S15 pp. 4–5). (b) The talk said that, rather than metaheuristic anti-cycling rules, adding enumeration (truncated B&B around the closest fractional point) worked very well, with 1,003 B&B nodes overall against 224,576 and 13,016 for the two CPLEX settings (S16 pp. 54, 58). The paper drops the enumeration to a future-work sentence (S15 p. 14); it returns as Stage 3 of Bertacco, Fischetti, Lodi, Discrete Optim. 4 (2007) 63–76, DOI 10.1016/j.disopt.2006.10.001 (preprint 31 May 2005, rev. 3 Nov 2005; S17 pp. 1, 7). (c) General integers: preliminary experiments showed more stalling (S15 p. 14), which the 2007 paper addresses | [practice] P (see Contradiction C2) |
| Baseline handling | The CPLEX baseline was tuned after extensive experiments and contacts with ILOG staff (best root results with presolve off); Bixby suggested an ad-hoc tuning for the manpower instances; the talk credits Ed Rothberg with better results by switching preprocessing off | S15 pp. 6, 9; S16 p. 51 · [practice] P |
| Objective-awareness | §3.2 of the paper adds an objective cutoff and, because rounded points may then satisfy the original constraints but not the cutoff, a recovery LP with the integer components fixed | S15 pp. 10–11 · P |
| Lineage | Achterberg and Berthold, "Improving the feasibility pump", Discrete Optim. 4 (2007) 77–86, DOI 10.1016/j.disopt.2006.10.004 (objective FP; not Fischetti's); FP 2.0 with Salvagnin, MPC 1 (2009) 201–222, DOI 10.1007/s12532-009-0007-3 (rounding replaced by propagation-based diving; preprint 26 Oct 2008, rev. 8 May 2009); Boland et al., "Boosting the feasibility pump", MPC 6 (2014) 255–279, DOI 10.1007/s12532-014-0068-9; the 2026 sole-author study (unreviewed) argues that common implementations, SCIP's among them, drop the 2005 cutoff-plus-recovery prescription, and measures the cost on MIPLIB 2017 inside SCIP | S46, S18 p. 1, S1, S19 pp. 1–2 · [practice] P |
| Reception | Scholar 627, S2 464, Crossref 349. FP 2.0 states the method was by then implemented in several commercial and open-source solvers [stated, joint]. SCIP's `heur_feaspump.c` is titled Objective Feasibility Pump 2.0 (authors Berthold and Salvagnin); CBC has `CbcHeuristicFPump.cpp` with a 2004 IBM copyright line (author not named in the header) | S18 p. 1; S43; S44 · [observed] S |
| Method it shows | M1, M3 (move a requirement into the objective), M5 (randomness as a tool), M6 (returns to his own 2005 prescription in 2026) | §5 |

### SW3 · The Benders line: combinatorial Benders cuts (2004/2006) → cut selection (2008/2010) → yoyo/in-out search (2009/2010) → redesigned Benders with in-out stabilisation (2015/2017)

| Dimension | Finding | Evidence / tag |
|---|---|---|
| Origin (a) CB cuts | Codato and Fischetti, IPCO 2004 (DOI 10.1007/978-3-540-25960-2_14) and Oper. Res. 54 (2006) 756–766, DOI 10.1287/opre.1060.0286. The paper says it is based on Gianni Codato's 2003 Laurea thesis ("A Combinatorial Approach to Benders' Decomposition", Padova, AIRO Camerini-Carraresi prize 2003) and on Hooker's idea of Benders cuts from minimal inconsistent sets (Hooker, Logic-based Methods for Optimization, Wiley 2000; Hooker and Ottosson, Math. Program. 96 (2003) 33–60, as cited); its own contributions are a separation heuristic for minimal infeasible subsystems and the computational test | S23 pp. 1, 4, references · [stated, joint] P |
| Key insight (a) | Big-M implications make LP relaxations weak; project the continuous variables out and replace them by purely combinatorial no-good cuts over minimal infeasible subsystems, so the master is an ILP with no big-M left | S23 pp. 1–3 · P |
| Minimum evidence (a) | On map labelling and two-group statistical classification, the reformulation ran orders of magnitude faster than ILOG-Cplex 8.1, and the paper stresses that this held already for a simple implementation (p. 4); CPLEX 8.1 had no cut pool for removable global cuts, so the authors declared their cuts local to get them purged | S23 pp. 4, 11–12 · [practice] P |
| (b) Cut selection | Preprint "Minimal Infeasible Subsystems and Benders cuts" (2008) published as "A note on the selection of Benders' cuts", Math. Program. 124 (2010) 175–182, DOI 10.1007/s10107-010-0365-7 (with Salvagnin, Zanette). Stated motivation: textbook Benders disappoints when simple design issues are underestimated; choose the cut as a well-chosen vertex of the alternative polyhedron; measured by root gap closed on MIPLIB instances (CPLEX 11): speedups of 1–2 orders of magnitude over the textbook rule | S24 pp. 1–2, 10 · [stated, joint] P |
| (c) Search scheme | The yoyo manuscript (Fischetti, Salvagnin, 20 Nov 2009) presents a two-point bisection cutting-plane scheme as a new method; the Bertinoro talk (30 Nov–2 Dec 2009) attacks Kelley's always-cut-the-optimal-vertex loop. The CPAIOR 2010 paper (DOI 10.1007/978-3-642-13520-0_17), which reuses the yoyo introduction almost word for word, presents the scheme as in-out search recently proposed by Ben-Ameur and Neto (Networks 49 (2007) 3–17, DOI 10.1002/net.20137) and says the group's research focus is moving from the separation module to the search scheme | S25 p. 1; S26 pp. 1, 4; S27 pp. 1–2 · [practice] P (see C3) |
| Origin (d) Redesign | TR "Thinning out facilities: a Benders decomposition approach for the uncapacitated facility location problem with separable convex costs" (1 Apr 2015) → "Redesigning Benders Decomposition for Large-Scale Facility Location" (preprint 11 Feb 2016) → Manag. Sci. 63 (2017) 2146–2162, DOI 10.1287/mnsc.2016.2461; companion "Benders decomposition without separability", EJOR 253 (2016) 557–569, DOI 10.1016/j.ejor.2016.03.002 (both with Ljubić, Sinnl). Stated motivation: business analytics needs scalable exact methods; working hypothesis that decomposition methods proposed decades ago and dropped (*sleeping beauties*) should be redesigned for current hardware and software | S28 p. 1; S29 pp. 1–2 · [stated, joint] P |
| Key insight (d) | Thin the model out (generalised Benders cuts replace millions of allocation variables) and, as the most important ingredient by the paper's own account, stabilise the root cut loop instead of following Kelley: keep a stabilising point, move it halfway towards each LP optimum, separate a point near the stabiliser | S29 p. 12 · [stated, joint] P |
| Minimum evidence (d) | A quick first shot, plugging the separator into IBM ILOG Cplex 12.6, already solved the open UFLLIB instances 2500-10 and 3000-100 in under 15 minutes each on a PC. On instance gs250a-1, Kelley's loop was stopped after 15,000 s still at the root, while the in-out loop closed the root in 0.19 s (fat model) and 0.04 s with 4 cuts (slim model) | S29 pp. 11–13 · [practice] P |
| Abandoned paths and limits (d) | No real bundle method (a simple in-out variant instead); Kelley kept at non-root nodes because a better loop inside CPLEX was not easy to implement; perspective strengthening skipped near zero (threshold 1e-5) because cuts became numerically unreliable. In the 2015 plenary: the very first implementation of the stabiliser worked so well that the group had no incentive to improve it; plain Benders called unfashionable, with a hashtag questioning its *paperability*; *Old Benders* is the group's name for the original solve-master-to-optimality scheme, still best for some problems | S29 pp. 11–13; S30 pp. 16, 20, 26 · [stated, joint] / [stated] P |
| Reception | CB cuts: Scholar 641 + 52 (IPCO), S2 484, Crossref 364. Note on selection: Scholar 242, Crossref 132. Redesign: Scholar 366, Crossref 209. The unpublished yoyo report is still cited in 2022–2023 (Turner, Berthold, Besançon, Koch, arXiv 2212.07231 v3, ref. 14) | S3, S5, S6, S45 · [observed] S |
| Method it shows | M3 (change the search scheme, not the oracle), M6 (revive discarded methods with new machinery), M4 (simple first, stop when it works), M2 (application-born: map labelling; facility location from analytics) | §5 |

### SW4 · Exploiting erraticism (Fischetti and Monaci; EURO XXV July 2012 → Oper. Res. 62 (2014) 114–122, DOI 10.1287/opre.2013.1231), with random sampling and the 2012 single-cut demonstration

| Dimension | Finding | Evidence / tag |
|---|---|---|
| Origin | The paper credits Emilie Danna's 2008 talk at the 5th MIP Workshop (Columbia, 4–7 Aug 2008) as the first explicit report of run-to-run variability (the 2013 random-sampling preprint calls the talk highly influential); its working hypothesis is that erraticism is intrinsic because exponential tree search acts as a chaotic amplifier | S31 p. 1; S33 p. 2 · [stated, joint] P |
| Staged evidence | The EURO 2012 talk sets rules for *single-cut* methods (cut time comparable to the root LP; same black-box solver), reports nine single-cut methods with an average 25% speedup over CPLEX 12.2 on 38 hard MIPLIB 2003 and COR@L instances, then reveals the trick: the cut is redundant and removed, so the speedups come only from perturbed initial conditions (his *pinball effect*), which he flags as important for experiment design | S32 pp. 5, 10, 14 · [practice; stated] P |
| Key insight | Turn the drawback into a resource: *bet-and-run* — a few short runs with randomised initial conditions, bet on the most promising by simple criteria, finish that one | S31 pp. 1–2 · P |
| Minimum evidence | 58 medium-difficulty instances (COR@L, MIPLIB 2010) each solved 100 times with different seeds by IBM ILOG Cplex 12.3 (single thread, 3,600 s): one extra run cuts nodes by about 40% (geometric mean), 100 runs by about 7×; all 11 instances unsolved by the default run were solved within the 100 runs; MIPLIB 2010 buildingenergy was solved to proven optimality for the first time (then re-verified at zero tolerance with 8 threads) | S31 pp. 3–4 · [practice] P |
| Test hygiene | Intel i5-750, single-thread runs with nothing else on the machine for reliable timings; a (possibly dummy) callback in every arm so that CPLEX's proprietary dynamic search is off in all of them; shifted geometric means | S31 p. 6 · [practice] P |
| Limits stated | Better diversification would need complete access to the solver's source code; machine learning to separate good from bad sample runs, AI/CP-style restarts reusing information, and portfolios are left open | S31 p. 10 · [stated, joint] P |
| Follow-ups | "Tree Search Stabilization by Random Sampling" (Sept 2013) → "Improving branch-and-cut performance by random sampling", MPC 8 (2016) 113–132, DOI 10.1007/s12532-015-0096-0 (with Lodi, Monaci, Salvagnin, Tramontani of IBM): variability shown across CPLEX 12.5.0, Gurobi 5.1 and Xpress 23 with 10 row/column permutations each; the authors state that a commercial implementation entered the default of IBM ILOG CPLEX 12.5.1. Related: backdoor branching (IPCO 2011, DOI 10.1007/978-3-642-20807-2_15; IJOC 25 (2013) 693–700, DOI 10.1287/ijoc.1120.0531); SelfSplit (CPAIOR 2014, DOI 10.1007/978-3-319-07046-9_28; COR 2018) | S33 pp. 1, 4; S1 · [stated, joint] P; CPLEX release notes not checked (G10) |
| Reception | Scholar 107, S2 80, Crossref 52 (erraticism); 49 / 24 / 14 (random sampling) | S3, S5, S6 · [observed] S |
| Method it shows | M5 (variability as data and as a tool; seeds and permutations in the protocol), M8 (proof of concept on a closed commercial solver through callbacks) | §5 |

### SW5 · Proximity search (Fischetti and Monaci; EURO Rome July 2013 → J. Heuristics 20 (2014) 709–731, DOI 10.1007/s10732-014-9266-x)

| Dimension | Finding | Evidence / tag |
|---|---|---|
| Origin | The talk starts from the LNS family (local branching, RINS, polishing), asks why sub-MIPs are easier, and proposes improving the relaxation's *grip* (the talk's term) by changing the objective instead of adding risky invalid constraints; it calls the method a dual version of local branching and notes that FP has been read as a proximal method (Boland et al.). The paper frames it as imitating a primal method that steps to a nearby better solution, with the black-box solver making the step | S35 pp. 2–8, 11; S34 pp. 2–3 · [stated, joint] P |
| Why then | Talk claim: proximity ideas were known (augmented Lagrangian, a 2005 primal-proximal heuristic) but never analysed computationally nor embedded in a MIP solver | S35 p. 11 · [stated, joint] P |
| Key insight | Add an explicit cutoff f(x) ≤ f(x̃) − θ and replace the objective by the Hamming distance to the incumbent, then re-centre | S34 pp. 2–3 · P |
| Minimum evidence | Set covering, network design and classification instances; C code on IBM ILOG Cplex 12.4, single thread on an i5-750; the first incumbent taken from a short CPLEX run so it is neither unrealistically bad nor too good; an unexpected side effect was much faster node processing under the proximity objective | S34 pp. 3, 12 · [practice] P |
| Limits and choices | Hard cutoff value is the main weakness; the authors chose a very conservative setting to avoid overtuning and contaminating results; the primal nature can trap the search in small steps; mixed strategies left out to keep the test environment clean | S34 pp. 3, 23 · [stated, joint] P |
| Reception | Scholar 124, S2 89, Crossref 68. The paper says CBC and GLPK implementations already existed; SCIP's `heur_proximity.c` (author Gregor Hendel) states the heuristic was presented by Fischetti and Monaci; CBC has `CbcHeuristicProximity`. Extension: "Proximity Benders" with Boland, Monaci, Savelsbergh, J. Heuristics 22 (2016) 181–198, DOI 10.1007/s10732-015-9306-1 | S34 p. 23; S43; S44; S1 · [observed] S |
| Method it shows | M3 (change the objective, not the feasible set), M1, M4 (anti-overtuning) | §5 |

### 2.6 Orbital shrinking (short)

Fischetti and Liberti, ISCO 2012, LNCS 7422, 48–58, DOI 10.1007/978-3-642-32147-4_6 (preprint 12 July 2011); Fischetti, Liberti, Salvagnin, Walsh, Discrete Appl. Math. 222 (2017) 109–123, DOI 10.1016/j.dam.2017.01.015.
- **Stance [stated, joint]:** symmetry is a useful feature to preserve, broken only as a last resort; integer variables for orbit sums give a discrete relaxation and a bound (S36 p. 1). Experiments described as preliminary (S36 p. 1). The ISMP 2012 talk was titled "Compressive Symmetry" (S37 p. 1).
- **Use [stated]:** in the 2015 plenary he lists orbital shrinking as the cure that shrank the very symmetric QAPLIB esc instances ("Three Ideas for the Quadratic Assignment Problem", Oper. Res. 60 (2012) 954–964, DOI 10.1287/opre.1120.1073): all but two esc instances solved in minutes on a notebook (S30 p. 14).
- **Reception [observed]:** modest (Crossref 15 + 11; Scholar 48 for DAM).
- **Origin of the collaboration with Liberti:** not documented (Gap G4).

### 2.7 Deep neural networks as 0-1 MILPs (short; turning point TP4)

arXiv 1712.06174 (17 Dec 2017; the arXiv comment says it was under submission to a conference) → Fischetti and Jo, Constraints 23 (2018) 296–309, DOI 10.1007/s10601-018-9285-6.
- **[stated, joint]** An early version went to CPAIOR 2018 in November 2017. The authors then learned that similar 0-1 MILP models had been proposed independently at almost the same time, so they say they cannot claim the model is new and claim novelty only for the applications (feature visualisation, adversarial examples) and the bound tightening (S38 p. 2).
- **[practice]** IBM ILOG CPLEX 12.7 on a standard notebook, small DNNs for handwritten digits (S38 p. 2).
- **Reception [observed]:** his eighth most-cited work (Scholar 514).
- **The ML strand that follows [practice]:** "Faster SGD training by minibatch persistency" (arXiv 1806.07353, 2018); "Embedded hyper-parameter tuning by Simulated Annealing" (arXiv 1906.01504, 2019), published as "Embedding Simulated Annealing within Stochastic Gradient Descent", OLA 2021; the 2026 revisit of minibatch persistency (§3, F4).
- **Earlier trace [practice]:** a sole-author comment, "Comments on: On learning and branching: a survey", TOP 25 (2017) 237–238, DOI 10.1007/s11750-017-0449-0 (metadata only, not read).

---

## 3. Failures, abandoned directions, unpublished items and self-revisions

| # | Item | Evidence | Tag |
|---|---|---|---|
| F1 | **Yoyo search** (manuscript 20 Nov 2009, which presents the scheme as new) was not published under that name. Its introduction reappears in the CPAIOR 2010 paper, where the two-point scheme is credited to Ben-Ameur and Neto (2007). On Salvagnin's site the CPAIOR paper's file is named `yoyo_short.pdf`; it has the same title, text opening and size (208,310 bytes) as `inout_disjunctive.pdf` on Fischetti's site. The 2009 report is still cited in 2022–2023 | S25 p. 1; S27 pp. 1–2; S45 | [practice] P; reason for the reframing (they found the prior work) [inferred] |
| F2 | **Bracket-and-fix** heuristic (Aussois, 12 Jan 2007, with Lodi): a bracketing MIP decides how many and which variables to hard-fix. The deck shows a preliminary implementation with hardwired parameters, variants under investigation, one still to be tested, and preliminary results only. No publication under that name in DBLP, the homepage list or the Scholar rows read; the server lists the deck with a June 2025 date | S39 pp. 12–14; S1; S8; S3–S4; S10 | [practice] P; abandoned or absorbed elsewhere [inferred, G11] |
| F3 | **FP talk → paper**: the talk's enumeration step and deterministic flips were replaced by randomisation in the 2005 paper; enumeration came back in 2005/2007 as Stage 3 | SW2 | [practice] P |
| F4 | **Minibatch persistency, self-revised.** The 2018 preprint (CIFAR-10, AlexNet) reports significantly faster convergence for reuse factors K = 2 or 5, calls the premise a computational conjecture, and was under submission to a conference per its arXiv comment; no venue version is in DBLP. The 2026 sole-author, pre-registered study (49M-parameter Transformer on FineWeb-Edu, 8 seeds per cell, learning rate tuned per arm, cost in steps, fresh tokens, seconds and joules) concludes that reuse buys data, not speed or energy, and only at large minibatch size; at B = 32 it reads more fresh tokens than the baseline | S7 (abstracts of 1806.07353 and 2609.13922) | [practice] P; kept as Contradiction C4 |
| F5 | **The 2026 FP study's headline is post hoc by its own account**: the 116-of-176 win of cutoff-plus-recovery over SCIP's objective-weighted pump comes from a comparison added after the pre-declared design; twelve pre-declared paired comparisons with Holm correction are reported separately | S19 p. 1; S20 README (Table 3 row) | [stated] P, unreviewed |
| F6 | **Local branching** did not reliably speed up optimality proofs (left open); REFINE disabled on a general-integer instance | SW1 | [stated, joint] P |
| F7 | **Redesigned Benders**: no bundle method; Kelley's loop kept in the tree for want of an easy hook in CPLEX | SW3 | [stated, joint] P |
| F8 | **DNN as MILP**: novelty of the model conceded | §2.7 | [stated, joint] P |
| F9 | **Erraticism**: the method was limited by having no access to the solver's source code | SW4 | [stated, joint] P |
| F10 | Other preprints with no venue version in DBLP as of 2026-11-08: "Finding First and Most-Beautiful Queens by Integer Programming" (arXiv 1907.08246; the CPAIOR 2018 queens paper, DOI 10.1007/978-3-319-93031-2_16, is published). Not evidence of rejection | S1, S7 | [practice] |
| F11 | Rejected or withdrawn submissions, errata, retractions: none on public record. A Crossref author query (top 400 hits) found no erratum, correction or retraction | S6 | [practice]; G5 |

---

## 4. Era and resource context

| Period | Compute and tools | Team and setting | Evidence / tag |
|---|---|---|---|
| 1982–1992 | Not documented (G9) | Bologna: Laurea 1982, PhD 1987; assistant professor 1990–92; papers with Toth, Martello, Carpaneto, Dell'Amico; ORSA thesis prize 1987 | S8 [stated] |
| 1992–1999 | Not documented; competition codes for Ferrovie dello Stato (FASTER set covering 1994, FARO rostering 1995) | Padova (associate 1992–94), L'Aquila (1994–95), Udine (1995–97), Padova full professor since 1997; FS projects ALPI, FASTER, FARO; EU projects (SDC statistical disclosure, TRIS, TRIO); Balas collaboration | S8 [stated] |
| 2000–2005 | Commercial solver as black box: ILOG-Cplex 7.0 (2002), 8.1 (2004), 9.1 and Xpress 16 (2005); Digital Alpha 533 MHz workstation; AMD Athlon 2100+; Pentium M 1.6 GHz notebook; Pentium IV 2.4 GHz PC | 2–3 authors; direct contact with solver developers (ILOG staff, Bixby's personal communication 2003, Rothberg); Lodi listed at IBM T.J. Watson by 2005; Bertacco at Dash Optimization; NS crew-scheduling projects (Wagner finalist 2004; Edelman 2008) | S12 pp. 3, 6, 11; S15 pp. 6, 9; S16 p. 51; S17 p. 1 · [practice] |
| 2008–2014 | CPLEX 11 → 12.5 through callbacks; single-thread timings on an Intel i5-750 2.67 GHz; an IBM Power7 for one long run; cross-solver checks with Gurobi 5.1 and Xpress 23 | Padova group with PhD students Salvagnin and Zanette (theses 2008) and Monaci; a co-author at IBM (Tramontani); university project "Computational Integer Programming"; computers of a Padova Center of Excellence | S24 p. 10; S31 pp. 3–4, 6, 10; S33 pp. 1, 4 · [practice] |
| 2015–2019 | CPLEX 12.6–12.7; 4-thread runs for Benders; a notebook for DNN experiments; DIMACS challenge codes | Vienna and ESSEC collaboration (4–8 authors); MILA co-author for DNN | S29 p. 11; S38 p. 2; S8 · [practice] |
| 2020–2026 | A cluster: SCIP git snapshot dba4b2a and SoPlex f0dbc81 (pinned), Gurobi 13.0.3, Python 3.12, gcc-toolset-13; 424 MIPLIB 2017 instances × 12 variants × 5 seeds; Zenodo deposits; GPU-accelerated layout search; OpenFOAM RANS cases in the EndoWake package; a Transformer pre-training study measured in joules | Sole author on two 2026 studies; EndoWake with Martina Fischetti; Padova and Bologna co-authors (Salvagnin, Roberti, Cavaliere) | S20 README; S21; S22; S7 · [practice] |

---

## 5. Candidate methods surfaced by this dimension (for Phase 2 cross-checking; not conclusions)

| ID | Candidate (executable form) | Signature-work evidence | Other evidence to seek (agents 02/03/05) |
|---|---|---|---|
| M1 | *MIPping*: turn a decision inside a MIP algorithm (which neighbourhood, which cut, is this node dominated) into an auxiliary MIP or LP and give it to the black-box solver | SW1, SW2, SW5; S40 p. 3; S42 p. 1 | closures papers 2005–2010; "Pruning moves", IJOC 22 (2010) 108–119, DOI 10.1287/ijoc.1090.0329, which revives the 1988 Fischetti–Toth dominance procedure (S42 p. 2) |
| M2 | Take a trick that worked in one application and restate it for any MIP | SW1 (TURNI soft fixing), SW3 (map labelling, facility location) | railway papers 1997–2009 |
| M3 | Change the search scheme or the objective, not the oracle or the feasible set | SW2, SW3(c,d), SW5 | "Lexicography and degeneracy" (2011); relax-and-cut for Gomory cuts, MPC 3 (2011) 79–102, DOI 10.1007/s12532-011-0024-x |
| M4 | Simplest version first; evaluate with default or conservative settings and no fine tuning; stop improving once it works | SW1 (no LocBra tuning), SW2 (no LP tuning), SW3(d) (first stabiliser kept), SW5 (conservative cutoff); S30 pp. 9, 26 | |
| M5 | Treat run-to-run variability as data: seeds and permutations in the protocol, expose fake improvements, exploit randomness | SW4; SW2 (random flips); S32 p. 14; 2026: 5 seeds, Holm (F5) | |
| M6 | Revive old or discarded ideas, including his own, with current machinery, and re-test old claims | SW3(d) *sleeping beauties*; 1988 dominance → 2010 pruning moves; SW2 2005 → 2026; F4 2018 → 2026 | |
| M7 | Contrarian reframing of a received drawback as an asset | Orbital shrinking (§2.6); erraticism (SW4); "Can Pure Cutting Plane Algorithms Work?" (IPCO 2008, DOI 10.1007/978-3-540-68891-4_29) | |
| M8 | Prove the concept on top of a closed commercial solver through callbacks, then hand it to solver developers | SW4 (CPLEX 12.5.1 default, per authors); SW3 (CPLEX callbacks); S41 pp. 7–10 | |

---

## Contradictions (kept, not reconciled)

- **C1 · DNN at CPAIOR 2018.**
  - His homepage lists [124bis] as a CPAIOR 2018 proceedings paper (LNCS 10848) with the page number left as XX (S8).
  - DBLP's CPAIOR 2018 records include his "Chasing First Queens by Integer Programming" (pp. 232–244) but no DNN paper (S2).
  - The Constraints article says only that an early version was submitted to CPAIOR 2018 in November 2017 (S38 p. 2), and the arXiv comment says only that it was under submission to a conference (S7).
  - Unresolved. A journal-fast-track route is possible but unverified.
- **C2 · How to stop the pump cycling.**
  - January 2004 talk: enumeration around the closest fractional point worked very well, and was preferred over metaheuristic anti-cycling rules (S16 p. 54).
  - 2005 paper: random flips and restarts are the published mechanism; enumeration is only suggested as future work (S15 pp. 4–5, 14).
  - Bertacco et al. 2005/2007 make enumeration Stage 3 (S17 p. 7).
- **C3 · Novelty of the two-point cutting-plane scheme.**
  - Yoyo manuscript (Nov 2009): a new search method, Ben-Ameur and Neto not cited (S25 p. 1; grep of the full text).
  - CPAIOR 2010 paper with the same introduction: the scheme is called in-out search and attributed to a recent proposal by Ben-Ameur and Neto (S27 p. 1).
  - Later Benders papers list the in-out lineage as Applegate et al., Ben-Ameur and Neto, and Fischetti and Salvagnin (S29 p. 12).
- **C4 · Minibatch persistency.**
  - 2018: significantly faster convergence.
  - 2026 (pre-registered): no gain in steps, seconds or joules; a data saving only at large batch, and at B = 512 a registered control could not separate the reuse effect from the learning-rate schedule position (S7).
- **C5 · Dates and versions across databases.**
  - Redesigned Benders: 2016 on Scholar, 2017 in Crossref and DBLP (Manag. Sci. 63(7)).
  - "Thinning out Steiner trees": 2014 on Scholar (the technical report), MPC 9 (2017) 203–229 (DOI 10.1007/s12532-016-0111-0) in DBLP.
  - Fix-propagate-repair: 2024 on his homepage and in S2 (online first), 2025 in DBLP and on Scholar.
  - Matheuristics chapter: DBLP 2018 (DOI 10.1007/978-3-319-07124-4_14); Crossref versions 2016 (`_14-1`), 2024 (`_14-2`), 2025 (978-3-032-00385-0_14). Scholar shows one 2025 entry, "Matheuristics by Examples", with 131 citations, probably merged across versions [inferred].
  - arXiv 2112.02195: v1 "Learning to Search in Local Branching" (the AAAI title), v2 (Aug 2022) retitled "Revisiting local branching with a machine learning lens".
- **C6 · Bibliographic slips.**
  - Set covering algorithms: his homepage gives Ann. Oper. Res. vol. 89; Crossref and DBLP give 98.
  - "On the monotonization of polyhedra": DBLP gives Math. Program. vol. 77; Crossref and the homepage give 78.
  - JASA 2000: first page 915 on the homepage, 916 in Crossref.
- **C7 · Attribution of the 2026 FP repository.**
  - The GitHub account mfischetti-arch was created on 2026-09-04 with no name or bio.
  - The Zenodo software record names "Fischetti, Matteo" without an ORCID; the raw-log dataset lists ORCID 0000-0001-6601-0568.
  - His homepage lists the paper title (with a ResearchGate link).
  - The link from account to person therefore rests on the matching title and a depositor-entered ORCID. Separately, the README and Zenodo say MIT while the GitHub API reports the license as NOASSERTION.

## Gaps

- **G1** No source found in which Fischetti ranks his own works or names his most important paper. The selection in §2 rests on citations and his self-presentation choices (homepage photo, deck openings, plenary examples). One WebSearch for interviews found none.
- **G2** Division of labour in FP (Glover's and Lodi's parts) and in LB (Lodi's part): undocumented in everything read.
- **G3** Title and advisor of his 1987 PhD thesis: not found. The Mathematics Genealogy Project was not consulted (left to agent 06).
- **G4** First-hand origin stories for erraticism (beyond the Danna citation), orbital shrinking (the Liberti collaboration) and the DNN turn (the MILA connection): none found.
- **G5** No public record of rejected or withdrawn submissions, reviews or rebuttals.
- **G6** The theses in `ricop/tesi/` were not opened, so supervision is inferred from hosting plus co-authorship only (no acknowledgments read).
- **G7** Not read:
  - Papers: the FP 2.0 body; Boosting FP; the final MPC random-sampling paper; the RAMP 2014 proximity paper and slides; the TOP 2017 comment; the 2017 bilevel chapter (DOI 10.1007/978-3-319-67308-0_3).
  - Talks: the ISMP 2018 keynote beyond p. 13; the Lausanne 2005 plenary beyond p. 6; all other decks in the slides folder (e.g. ISCO 2014 *BRANCHstorming*, OR2015 plenary, AIROyoung 2026); the 2026 videos.
  - 2026 items: the Fermat digital-twin note and the FP-cutoff entry on ResearchGate; the EndoWake papers beyond their abstracts.
- **G8** OpenAlex not queried (no API key). Google Scholar rows beyond 100 (by citations) and 30 (by date) not read.
- **G9** Compute, tools and team size for 1982–1999: undocumented.
- **G10** The CPLEX 12.5.1 random-sampling default rests only on the authors' statement (S33 p. 4); IBM release notes not checked.
- **G11** Whether bracket-and-fix was absorbed into later work (a student thesis, "Just MIP it!") was not checked beyond a text search of "Just MIP it!" (no match).

## Sources

All fetched on 2026-11-08 unless noted. P = primary, S = secondary.

| # | Source | Author(s) | Date | Link / identifier | P/S |
|---|---|---|---|---|---|
| S1 | DBLP records for pid 47/4770, via `scripts/dblp_works.py` (sparql.dblp.org) | DBLP | 2026-11-08 | https://dblp.org/pid/47/4770.html | S |
| S2 | DBLP SPARQL query: CPAIOR 2018 records containing "neural", "deep" or "queens" | DBLP | 2026-11-08 | https://sparql.dblp.org/sparql | S |
| S3 | Google Scholar profile, sorted by citations, rows 1–100 | Google Scholar | 2026-11-08 | https://scholar.google.com/citations?user=5rOdaqAAAAAJ | S |
| S4 | Google Scholar profile, sorted by date, rows 1–30 | Google Scholar | 2026-11-08 | same profile, `sortby=pubdate` | S |
| S5 | Semantic Scholar author search and paper lists (2853454; split records 2259113410, 2341349824, 2065674176) | Semantic Scholar | 2026-11-08 | https://api.semanticscholar.org/graph/v1/author/2853454 | S |
| S6 | Crossref REST API: DOI lookups for the signature works, and an author query | Crossref | 2026-11-08 | https://api.crossref.org/works | S |
| S7 | arXiv author search (9 results) and abstract pages 1712.06174, 1806.07353, 2112.02195, 2609.13922, 2609.40157, 2610.07844, 2610.39503 | Fischetti et al. | 2017–2026 | https://arxiv.org/search/?query=Fischetti%2C+Matteo&searchtype=author | P |
| S8 | Homepage and CV (education, career, prizes, talks, publication list, technical reports, photo captions) | M. Fischetti | read 2026-11-08 | https://www.dei.unipd.it/~fisch/ | P |
| S9 | Papers folder listing (≈95 author preprints with upload dates) | M. Fischetti | read 2026-11-08 | https://www.dei.unipd.it/~fisch/papers/ | P |
| S10 | Slides folder listing (talks 1990–2026 with upload dates) | M. Fischetti | read 2026-11-08 | https://www.dei.unipd.it/~fisch/papers/slides/ | P |
| S11 | Theses folder listing (doctoral and Laurea theses 1998–2020) | M. Fischetti | read 2026-11-08 | http://www.dei.unipd.it/~fisch/ricop/tesi/ | P |
| S12 | "Local Branching", preprint (May 2002, rev. Dec 2002); Math. Program. 98 (2003) 23–47 | Fischetti, Lodi | 2002 | https://www.dei.unipd.it/~fisch/papers/local_branching.pdf · DOI 10.1007/s10107-003-0395-5 | P |
| S13 | "Local Branching: Basics and Extensions", Optima 72 | Fischetti, Lodi | Jan 2006 (dated 5 Jul 2005) | https://mathopt.zib.de/Optima-Issues/optima72.pdf | P |
| S14 | Slides "… or How to enhance the heuristic behaviour of your favourite 0-1 MIP solver", Aussois | Fischetti, Lodi | Jan 2002 | https://www.dei.unipd.it/~fisch/papers/slides/ (Aussois 2002 [local branching].PDF) | P |
| S15 | "The feasibility pump", preprint (revised version); Math. Program. 104 (2005) 91–104 | Fischetti, Glover, Lodi | 2004 | https://www.dei.unipd.it/~fisch/papers/feasibility_pump.pdf · DOI 10.1007/s10107-004-0570-3 | P |
| S16 | Slides "The feasibility pump", Aussois | Fischetti, Glover, Lodi | Jan 2004 | slides folder (2004 Aussois [feasibility pump].pdf) | P |
| S17 | "A Feasibility Pump heuristic for general Mixed-Integer Problems", preprint (31 May 2005, rev. 3 Nov 2005); Discrete Optim. 4 (2007) 63–76 | Bertacco, Fischetti, Lodi | 2005 | https://www.dei.unipd.it/~fisch/papers/fp_general_integer.pdf · DOI 10.1016/j.disopt.2006.10.001 | P |
| S18 | "Feasibility Pump 2.0", preprint (26 Oct 2008, rev. 8 May 2009); MPC 1 (2009) 201–222 | Fischetti, Salvagnin | 2009 | https://www.dei.unipd.it/~fisch/papers/feasibility_pump_201.pdf · DOI 10.1007/s12532-009-0007-3 | P |
| S19 | "Feasibility Pump with Objective Cutoff: A Computational Study", manuscript (unreviewed) | M. Fischetti | Sep 2026 | https://github.com/mfischetti-arch/fp-objective-cutoff/blob/main/paper/manuscript.pdf | P |
| S20 | GitHub repository mfischetti-arch/fp-objective-cutoff: API metadata, README | (account mfischetti-arch) | created 2026-09-04 | https://github.com/mfischetti-arch/fp-objective-cutoff | P (attribution: C7) |
| S21 | Zenodo: reproducibility package (software, MIT) and raw SCIP logs (CC BY 4.0) | Fischetti, Matteo | 2026-09-17 | DOI 10.5281/zenodo.22810777; DOI 10.5281/zenodo.22810848 | P |
| S22 | Zenodo: EndoWake replication package v2.1.0 | Martina Fischetti, Matteo Fischetti | 2026-11-04 | DOI 10.5281/zenodo.23955408 (cited as 10.5281/zenodo.22017446) | P |
| S23 | "Combinatorial Benders' Cuts for Mixed-Integer Linear Programming", preprint (24 May 2004, rev. 16 Feb 2005); Oper. Res. 54 (2006) 756–766 | Codato, Fischetti | 2005 | https://www.dei.unipd.it/~fisch/papers/combinatorial_benders_cuts_for_milp.pdf · DOI 10.1287/opre.1060.0286 | P |
| S24 | "Minimal Infeasible Subsystems and Benders cuts", preprint; published as "A note on the selection of Benders' cuts", Math. Program. 124 (2010) 175–182 | Fischetti, Salvagnin, Zanette | 2008 | https://www.dei.unipd.it/~fisch/papers/MIS_for_Benders.pdf · DOI 10.1007/s10107-010-0365-7 | P |
| S25 | "Yoyo search: a bisection cutting-plane method", manuscript (unpublished as such) | Fischetti, Salvagnin | 20 Nov 2009 | https://www.dei.unipd.it/~fisch/papers/2009_yoyo_search.pdf | P |
| S26 | Slides "Cutting planes: don't back yourself into the corner!", Bertinoro | Fischetti, Salvagnin | Nov–Dec 2009 | slides folder (2009 Bertinoro [yoyo search].pdf) | P |
| S27 | "An in-out approach to disjunctive optimization", CPAIOR 2010, LNCS 6140, 136–140 (preprint; identical file at Salvagnin's `yoyo_short.pdf`) | Fischetti, Salvagnin | 2010 | https://www.dei.unipd.it/~fisch/papers/inout_disjunctive.pdf · DOI 10.1007/978-3-642-13520-0_17 | P |
| S28 | "Thinning out facilities: a Benders decomposition approach for the uncapacitated facility location problem with separable convex costs", TR (title page) | Fischetti, Ljubić, Sinnl | 1 Apr 2015 | https://www.dei.unipd.it/~fisch/papers/thinning_out_facilities.pdf | P |
| S29 | "Redesigning Benders Decomposition for Large Scale Facility Location", preprint; Manag. Sci. 63 (2017) 2146–2162 | Fischetti, Ljubić, Sinnl | 11 Feb 2016 | https://www.dei.unipd.it/~fisch/papers/Benders_for_UFL.pdf · DOI 10.1287/mnsc.2016.2461 | P |
| S30 | Slides "The simpler the better: Thinning out MIP's by Occam's razor", Larnder plenary, CORS/INFORMS Montreal | M. Fischetti | Jun 2015 | slides folder (2015 CORS [Fischetti - Occam Razor].pdf) | P |
| S31 | "Exploiting erraticism in search", manuscript OPRE-2012-05-278(R) (25 May 2012, rev. 21 Mar 2013); Oper. Res. 62 (2014) 114–122 | Fischetti, Monaci | 2013 | https://www.dei.unipd.it/~fisch/papers/exploiting_erraticism_in_search.pdf · DOI 10.1287/opre.2013.1231 | P |
| S32 | Slides "On the role of randomness in exact tree search methods", EURO XXV, Vilnius | M. Fischetti (joint work with Monaci) | Jul 2012 | slides folder (2012 EURO [erraticism].pdf) | P |
| S33 | "Tree Search Stabilization by Random Sampling", preprint; published as "Improving branch-and-cut performance by random sampling", MPC 8 (2016) 113–132 | Fischetti, Lodi, Monaci, Salvagnin, Tramontani | Sep 2013 | https://www.dei.unipd.it/~fisch/papers/tree_search_stabilization_by_random_sampling.pdf · DOI 10.1007/s12532-015-0096-0 | P |
| S34 | "Proximity Search for 0-1 Mixed-Integer Convex Programming", preprint; J. Heuristics 20 (2014) 709–731 | Fischetti, Monaci | 31 Jul 2013 | https://www.dei.unipd.it/~fisch/papers/proximity_search.pdf · DOI 10.1007/s10732-014-9266-x | P |
| S35 | Slides "Proximity search", EURO Rome | Fischetti, Monaci | Jul 2013 | slides folder (2013 EURO Rome [Fischetti - proxy].pdf) | P |
| S36 | "Orbital shrinking", preprint; ISCO 2012, LNCS 7422, 48–58 | Fischetti, Liberti | 12 Jul 2011 | https://www.dei.unipd.it/~fisch/papers/orbital_shrinking.pdf · DOI 10.1007/978-3-642-32147-4_6 | P |
| S37 | Slides "Compressive Symmetry", ISMP Berlin | Fischetti, Liberti | Aug 2012 | slides folder (2012 ISMP [orbital shrinking].pdf) | P |
| S38 | "Deep Neural Networks and Mixed Integer Linear Optimization", preprint; Constraints 23 (2018) 296–309 | Fischetti, Jo | Apr 2018 | https://www.dei.unipd.it/~fisch/papers/deep_neural_networks_and_mixed_integer_linear_optimization.pdf · DOI 10.1007/s10601-018-9285-6 | P |
| S39 | Slides "MIP models for MIP heuristics, or the Bracket-and-Fix method", Aussois | Fischetti, Lodi | 12 Jan 2007 | slides folder (2007 Aussois [bracket-and-fix heuristic].pdf) | P |
| S40 | Plenary slides on hybrid MIP methods, EuroGP/EvoCOP, Lausanne | M. Fischetti | Mar–Apr 2005 | slides folder (2005 Lausanne [plenary on hybrid MIP methods].pdf) | P |
| S41 | Keynote slides "#post_modern Branch-and-Cut Implementation", ISMP Bordeaux | M. Fischetti | 6 Jul 2018 | slides folder (2018 ISMP [keynote Fischetti on BandC].pdf) | P |
| S42 | "Just MIP it!", preprint; Matheuristics, Annals of Information Systems 10 (2010) 39–70 | Fischetti, Lodi, Salvagnin | Oct 2008 | https://www.dei.unipd.it/~fisch/papers/justMIPit.pdf · DOI 10.1007/978-1-4419-1306-7_2 | P |
| S43 | SCIP source headers: `src/scip/heur_feaspump.c`, `heur_localbranching.c`, `heur_proximity.c` at commit 353584f2a48f39328acb3864f596580341a19aaa | SCIP developers (Berthold, Salvagnin, Pfetsch, Hendel) | 2026-11-08 snapshot | https://github.com/scipopt/scip | S ([observed]) |
| S44 | CBC source: `src/CbcHeuristicFPump.cpp` (2004 IBM copyright line), `src/CbcHeuristicLocal.cpp` (class CbcHeuristicProximity) at commit 4e30be6684941c90a1a4537d3c1ed8d8a5fbcff4 | COIN-OR Cbc | 2026-11-08 snapshot | https://github.com/coin-or/Cbc | S ([observed]) |
| S45 | "Cutting Plane Selection with Analytic Centers and Multiregression", arXiv 2212.07231 v3 (reference 14 cites the yoyo report) | Turner, Berthold, Besançon, Koch | 31 Jan 2023 | arXiv 2212.07231 | S ([observed]) |
| S46 | Crossref metadata of related works: Ben-Ameur, Neto, Networks 49 (2007) 3–17; Achterberg, Berthold, Discrete Optim. 4 (2007) 77–86; Danna, Rothberg, Le Pape, Math. Program. 102 (2005) 71–90 | various | 2004–2007 | DOI 10.1002/net.20137; DOI 10.1016/j.disopt.2006.10.004; DOI 10.1007/s10107-004-0518-7 | S |
| S47 | WebSearch, 2 queries (interviews on FP and LB origins; the yoyo report): leads only, no claim rests on them | — | 2026-11-08 | — | S |
