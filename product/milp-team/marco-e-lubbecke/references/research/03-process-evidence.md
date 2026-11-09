# Marco E. Lübbecke · 03 Process evidence (what he actually does)

- **Researcher**: Marco E. Lübbecke (RWTH Aachen University, Chair of Operations Research; GERAD), living
- **Dimension**: research agent 03, process evidence: behaviour visible in code, experiment sections, versions, dropped work
- **Research date**: 2026-11-08
- **Sources consulted**: 43 (42 primary, 1 secondary). Every source is listed under "Sources" (S1–S43). WebSearch calls used: 1 of 5.
- **Local corpus**: `references/sources/{papers,talks,essays,software,publications}` hold only `.gitkeep`, so there is no user-supplied material. `private/` was not opened. No transcripts were saved.
- **How the evidence was read**: the GCG repository was cloned (blobless) and its git history, CHANGELOG, release notes, `check/`, `doc/`, CI file and source tree were read directly. Full texts were read for S7, S8, S11 (GCG section), S12 (GCG section), S14 (Sect. 4.5), S15, S16, and the preface, author bios and Ch. 8 of S34. For S17–S32 only the abstract was read, from the publisher page or a repository record; their full texts were **not read**. Bibliographic data were checked against ORCID, OpenAlex, Crossref, DataCite and the arXiv API.
- **Blocked or unreachable on 2026-11-08** (not circumvented): HAL and DBLP (bot challenge), RWTH Publications (JavaScript challenge), CiteSeerX (blocked), and `or.rwth-aachen.de`, `gcg.or.rwth-aachen.de` and `git.or.rwth-aachen.de` (connection failed).

**Tags**: [stated] he said or wrote it · [practice] it shows in papers, code or records · [observed] a third party or a count or date in the record shows it · [inferred] my reading, stated nowhere. Each item also says **primary** or **secondary**, and who it can be attributed to: **sole** (Lübbecke alone), **co-authored** (a multi-author paper), or **group** (RWTH OR group code or reports). Most process evidence here is group-level. Lübbecke's personal traces are his own commits (S1), one sole-authored discussion paper (S16), one sole-authored status report (S20, abstract only) and a blog (S36).

Quotation policy: verbatim quotes are short and come mostly from openly licensed material: GCG under Apache-2.0, S15 under CC BY, S7/S8 under CC BY 4.0, S14 under CC BY 4.0. There is one fragment from S16. Everything else is paraphrased and carries no quotation marks.

---

## 0. The shape of the evidence

- **His hands-on code is maintainer work, not core algorithm work.** GCG's history runs from 2008-11-25 (first commit by Gerald Gamrath, converted from CVS) to 2026-10-30. It has 7,527 commits reachable from `master` and 67 distinct author names on all branches. The largest committers are M. Bergner (1,116), C. Puchert (1,050), E. Mühmer (922), M. Bastubbe (718), J. Witt (631), H. Franzen (530), G. Gamrath (404) and T. Donkiewicz (331 + 90 as `donkiewicz`). Lübbecke has 92 commits, dated 2018-06-11 to 2021-10-28 (2018: 4, 2019: 69, 2020: 12, 2021: 7). Of these, 43 are merges of merge requests (into `master` and `v30-bugfix`) and 49 are his own changes. No other author alias of his appears in the author list. [observed] primary (S1). Era: chair holder at RWTH since 2010, group of PhD students, internal GitLab.
- **He is named as the project's leader.** In the book's author bio he is said to have led, since 2008, the effort to build a decomposition-based solver that reformulates any MIP automatically: GCG, built on SCIP. The same bio says he was on the first team that ever used SCIP's column-generation capabilities (SCIP 0.81). [stated] primary (S34, "About the authors"; the bio is in third person and its writer is not named).
- **Reading these two together.** The record shows a researcher whose process lives mostly in how a group's code, test sets and papers are organised and edited, while students and postdocs write most of the code. Below, practices are attributed to the group unless his own commit or authorship shows them. [inferred]

---

## 1. Layer 4: experiments and execution

### 1.1 How test problems are chosen

1. **Structured problem classes come first, held in a curated library.** `check/testset/` holds 267 named test sets (266 `.test` and 75 `.solu` files). They cover bin packing (`bp-bison*`, `bp-orlibrary`), vertex colouring in several formulations (`coloring-*-bigm`, `-disaggr`), cutting stock (Wäscher, Schwerin, hard28), CVRP (Augerat, Taillard, Fisher, …), capacitated and single-source warehouse location, GAP (OR-Library, Yagiura), lot sizing (Trigeiro, Derstroff, Pimentel, Surie), capacitated p-median, resource allocation, temporal knapsack, unit commitment, multicommodity flow, stable set (DIMACS, BHOSLIB), MIPLIB 2010/2017 subsets and "staircase" variants of several libraries. The 75 `.solu` files (including a shared `_all.solu`) hold known optimal or best values for automatic correctness checks. strIPlib test files enter the repository on 2012-07-20 and 2013-04-04 (C. Puchert). By 2021 the SCIP 8.0 report still calls strIPlib unreleased while drawing its test set from it. [practice] primary, group (S1; S11 §10.2.3). Era: 2012 onward, RWTH group.
2. **Adversarial general MIPs, to test the claim of automation.** The journal test set `gcgjournal` was added on 2011-07-04 by M. Bergner, with the commit message "added journal version testset". It contains 39 instances: 23 from MIPLIB 2003 and 16 from MIPLIB 2010. The journal paper (S17) says it tests general MIPLIB 2003/2010 instances for which a decomposition would not be the first choice. [practice] primary, co-authored (S1; S17 abstract; S18 abstract). That `gcgjournal` is S17's test set is [inferred]; it is supported by the matching count of 38 + 1 in S15. The 2018 strength study reuses these instances, 38 after excluding `mine-166-5` "because some DW reformulations failed to solve" (S15 §4.1, CC BY). [practice] primary, co-authored.
3. **Exhaustive enumeration on toy models.** To study what happens between convexifying no constraints and convexifying all of them, the group built a GCG detector that writes out every one of the 2^|I| Dantzig-Wolfe reformulations. They used tiny models with at most 18 constraints: generated bin packing, colouring and VRPTW instances, shrunken literature instances, and the MIPLIB 3 instances flugpl, mod008 and p0033. Over a million LP relaxations were solved by column generation in about 100 hours. Four MIPLIB candidates (markshare1, markshare2, mas74, mas76) "turned out to be too hard to solve in preliminary experiments" and were dropped, and the paper says so. [practice] primary, co-authored (S15 §2). Era: GCG 2.1.4 development version, 2018.
4. **Difficulty-filtered, diversity-controlled sets on the MIPLIB 2017 pattern.** For the 2021 strong-branching evaluation they kept only strIPlib instances that needed at least 1,000 nodes with a previous GCG version, and controlled diversity much as the MIPLIB 2017 benchmark selection did (S11 §10.2.3, paraphrase). The group's documentation turns this into a tool: `striplib.py` selects a diverse set for a target experiment length (`--hours`) with per-group minimum and maximum counts and a cluster-strictness setting (Donkiewicz 2021). It also labels the older `goodinstances.test` "Not recommended for use anymore." [practice] primary, group (S3; S11).
5. **Test sets for a planned change.** The experiments guide tells developers to work out on which instances a change can be seen at all (for example root-solved or staircase instances). If they target a hand-picked set, they must also run a general-purpose set to show no harm elsewhere, and test sets should show both improvements and deteriorations. [practice] primary, group (S3; written by T. Donkiewicz in 2020, with small wording edits by Lübbecke on 2020-09-25).
6. **Public benchmarks of the application community.** Timetabling was tested on the Udine instances and the ITC-2007 data (S27). The k-vertex cut paper uses the 304-instance benchmark of Furini et al. (2020), each instance in an unweighted and a weighted version, 608 in all (S8 §4, App. E). [practice] primary, co-authored.
7. **Real data from industrial partners.** In-plant railroads, where planning was still done with pencil and paper; the method was tested on artificial and real-life data (S30, 2003). Coil coating at Salzgitter Flachstahl was implemented at the plant (S28, 2011). SBB Cargo Express used realistic data (S29, 2008). For the Kiel Canal, the software tool was also used to assess options for enlarging the canal (S31, 2019). [practice] primary (abstracts only), co-authored. Era: his PhD at TU Braunschweig (to 2001) and the TU Berlin postdoc and habilitation years (to 2007, per S34).

### 1.2 How baselines are chosen

1. **The host framework without the decomposition.** From the start, GCG was built by turning SCIP into a generic branch-price-and-cut solver, so as not to re-implement MIP machinery such as pseudo-cost branching, presolving, propagation, heuristics and separation (S19 abstract, paraphrase). The group's guide names GCG against SCIP as the most likely solver comparison (S3, "Comparing different Solvers"). [practice] primary, co-authored or group. Era: 2008–2010 (G. Gamrath's early GCG code on SCIP).
2. **A standard harness, the same for every solver.** `miplib2010-scripts/` (added 2011-07-04) wraps GCG into the MIPLIB 2010 test engine. That engine runs CBC, CPLEX, Gurobi, MOSEK, SCIP and Xpress with a solution checker; its defaults are `TIME=3600` and `HARDMEM=8192`. There are also cluster scripts for CPLEX and CBC (2011-11-29, Bergner) and for DIP, the competing generic decomposition code (2012-08-16, Gamrath: "added dip check scripts"). [practice] primary, group (S1). Whether a GCG-versus-DIP comparison was ever published is **not verified**.
3. **Competitors re-run on your own hardware, under identical conditions.** In the k-VCP paper, HYB and COMP (public code on GitHub, `paoloparonuzzi/k-Vertex-Cut-Problem`) were re-executed with the same time limit and a newer CPLEX (22.1.0). The previous branch-and-price code (Cornaz et al. 2019) came from its authors by personal communication and was re-run with CPLEX 22.1.0 as its LP solver. Where the re-runs solved fewer instances than the original study, the paper explains this by the earlier study's more powerful hardware: 7 and 3 fewer unweighted instances for HYB and COMP, 7 fewer weighted for each (S8 §4.2, §4.4). [practice] primary, co-authored (4 authors; Lübbecke is last author). Era: 2026, RWTH OR cluster.
4. **Versions against versions.** `check/compareversions.sh` (H. Franzen, 2017-12 to 2018-01) checks out tagged versions, builds them and runs them on the same test set. The guide warns that comparisons assembled by hand are comparable only if instances, settings, time limits and machine are the same (S3 §C). [practice] primary, group (S1, S3).
5. **The same criterion applied to others.** In his sole-authored comment on a timetabling survey, he notes that settings, machines and computing times differ widely between the papers compared. He wonders how the comparison would look "if all approaches were run under identical conditions" (S16, p. 360), and says that part of the survey should be read with caution. He also reports having been prompted to dig out the group's old code and install a current CPLEX to see what is possible in 2015 (S16, p. 361). [stated] primary, sole. This maps onto items 3 and 4. [inferred]

### 1.3 Protocol: limits, hardware, metrics

- **Time limit and threads.** One hour wall clock is the default in the MIPLIB 2010 harness (S1). The 2021 strong-branching study used 3600 s (S11). The 2026 k-VCP runs were single-threaded with one hour (S8). [practice] primary.
- **The same old cluster, kept for five years.** The 2021 GCG evaluation ran on Intel Xeon L5630 quad-core nodes (2.13 GHz, 16 GB). The 2026 k-VCP runs used the same processor type on the chair's Debian 11 cluster (S11 §10.2.3; S8 §4). [observed] primary. Whether this is done deliberately for comparability is not stated. [inferred]
- **Metrics.**
  - Shifted geometric means of time and nodes, with the shifts printed (example output in S3: `shifted geom. [ 100/10.0/5.0/2.0]`).
  - A primal-integral script, taken from G. Hendel and adapted to GCG logs in 2013 (C. Puchert).
  - Solved counts, performance profiles and per-component ablations (S8 §4.2).
  - Gap closed, normalised as (z_DW − z_LP)/(z_IP − z_LP) (S15 §3).
  - Root dual bounds against LP strength (S8 §4.5).

  [practice] primary, group or co-authored.
- **Logs as data.** Test runs write `.out`, `.res`, `.set`, `.pav`, `.tex` and `.vbc` files. The guide asks developers not to change existing log formats, because the parsers of the visualisation suite depend on them (S3). [practice] primary, group.

### 1.4 What gets done first

1. **A smoke test before the big run.** Run `make test` on the default `short` test set before a large campaign, and check the summary line (S3 §1). CI was set up on 2019-11-05 by B. Meier. In its current form it builds release and debug versions with make and CMake, on Linux and Windows, and runs `make SETTINGS=default_feature test` (S1 `.gitlab-ci.yml`). [practice] primary, group.
2. **Preliminary experiments decide the variant, and only the winner is reported in full.** The k-VCP paper tried two symmetry-handling approaches and reports that preliminary experiments favoured the second, so only that one is analysed. Preliminary runs also showed that the construction of the edge-covering clique family matters, so three alternatives were ablated. A preliminary LP-solver test (SoPlex against CPLEX) settled the choice of SoPlex (S8 §3.2, §4.1, §4.2). [practice] primary, co-authored.
3. **A conference version first, then the journal.** The ORCID record holds at least six conference-to-journal pairs:
   - SODA 2004 → Discrete & Computational Geometry 2008 (stabbing number; arXiv cs/0310034)
   - LNCS 2005 → ACM JEA 2006 (rectangle covers)
   - LATIN 2006 → J. Discrete Algorithms 2008 (k-modal partitions)
   - WEA 2008 → Annals of OR 2012 (timetabling)
   - SEA 2010 → EJOR 2015 (multi-mode resource leveling)
   - IPCO 2011 → Math. Programming 2015 (automatic DW)

   Identifiers are in S5 and S26–S27. [practice] primary, co-authored. This matches a stated rule in his 2014 blog post: send abstracts or extended abstracts to refereed conferences first (S36, "How to write a paper", paraphrase). [stated] primary, sole.
4. **Theory first; computation where the theory stalls.** The SEA 2018 study starts from the group's characterisation, for stable set and related problems, of the DW reformulations that give the weakest or strongest bound (repORt 2015-029, published as S33). It says a generalisation is out of reach and nothing is known about what lies "in between", and then measures exactly that (S15 §1). It ends with conjectures and open questions for theory, such as a sparse sub-poset of minimal reformulations and possible Klee-Minty-like pathological instances (S15, final section). [practice] primary, co-authored. Era: GCG 2.1.x, 2015–2018.

### 1.5 Debugging and engineering discipline

His own commits, sole, primary, from S1:

- **He checks a measurement before reporting it.** On 2019-05-22 he removed per-detector timing output after finding that the total detection time looked right but "the time in the individual detectors seems to be wrong", because a clock is re-created in every detection round (commit 67dc6a57). Earlier he had made the reported total include classification and score computation (084594c6). [practice]
- **He traces regressions to the commit that caused them.** He "fixed the "GCG stalls in score computation" bug that came with commit 2742cfa4" (493fb6c0, 2019-05-22). [practice]
- **He keeps the meaning of reported statistics correct.** He stopped reporting master-only ("static") variables as linking variables, closing issue #369 (fe9edd67, 2018-06-13). [practice]
- **He keeps the repository and test sets clean.** He reverted merge request !163 (3f7cfe8f, 2019-07-08), which had brought in 1,333 files (about 4.4 million lines), among them merge-tool leftovers such as `depend.gcglib_BASE_11772.opt`. He "restored the original capitalized instance names so that they match their file names" in a test set (c80e2e74). He "adapted tests files to compile again after detector refactoring" (41f97aff, 2021). [practice]
- **He does release chores himself.** He set version numbers (3.0.3), ran the copyright-year script, synced to SCIP 6.0 and SoPlex 4.0, and noted "we still need to complete the CHANGELOG" (5f06afbd, cad39737). [practice]

Group practice, primary (S1): FlexeLint configuration (`lint/`), unit tests for the graph structures (`tests/`), `.solu`-based checking of solutions, and debug builds in CI. [practice] group.

### 1.6 Ablations and evaluation of components

- k-VCP: an ablation of three variants (two clique-family constructions and equality against inequality constraints), plus symmetry handling, initial solution and connectivity cut. There is also a check that column generation is not the bottleneck (S8 §4.2–4.3). [practice] primary, co-authored.
- 2021: ten branching-selection variants were compared by geometric and arithmetic means of time and nodes, timeouts, and the number of instances on which each variant was best (S11 Fig. 6, App. B). [practice] primary, group.
- SEA 2015 cuts: effects are evaluated on several problem classes, and the claim is limited to instances whose integrality gap is not too small (S21 abstract). [practice] primary (abstract), co-authored.

---

## 2. Layer 5: judging results (what is believed, what is reported)

1. **The claim is sized to what was measured.**
   - The automatic-DW paper claims strong dual bounds and calls itself a computational proof of concept; its abstract makes no claim about solving time (S17 abstract). The IPCO 2011 version said the process could be automated in principle (S18 abstract, paraphrase).
   - The cut paper limits its result to instances with a non-trivial gap (S21).
   - The hypergraph-separation paper says it complements earlier exact approaches for larger k and beats them only for k = ∞ (S23).
   - The 2021 strong-branching result is labelled preliminary, and further investigation is said to be needed (S11 §10.2.3).
   - The timetabling paper says its algorithm is not the overall winner, but deterministic and robust without tuning (S27 abstract, paraphrase).

   [practice] primary, co-authored.
2. **Failure modes are named.** The 2017 learning paper states that if the detected structure does not match the model, the solver on the reformulation may fail completely. That is the motivation for learning when to decompose, and the paper reports little deterioration on non-target instances (S22 abstract). [practice] primary (abstract), co-authored.
3. **Where the method loses, it is reported.** The k-VCP paper's Appendix G marks the instances on which the new branch-and-price fails while a method from Furini et al. (2020) succeeds (S8 §4.4). MIPLIB 2017's decomposition features come with a caveat: a low area score means only that GCG 3.0 finds no obvious structure, not that the model has none (S14 §4.5). [practice] primary, co-authored.
4. **Defaults stay conservative until the evidence is in.**
   - Strong branching is off by default: the 2021 report says so (S11), and in 2026 `DEFAULT_USESTRONG` is still `FALSE` in `branch_orig.c` and `branch_ryanfoster.c`. This holds even though the 2021 report found enabling it by default conceivable (S11, paraphrase).
   - Pricing parallelisation is on at compile time but runs one thread by default, because more threads make the run non-deterministic (S12 §4.6; `DEFAULT_NTHREADS 1`).
   - IPColGen is disabled by default (S12 §4.7).
   - Extended master constraints and the subset-row separator are shipped marked "experimental" (S12 §4.3; CHANGELOG 4.0–4.1).

   [practice] primary, group.
5. **Heuristics go into production only with a certified bound.** The coil-coating heuristic, a genetic algorithm around a fast setup-scheduling heuristic, was certified within 10% of optimum by an IP built on a combinatorial relaxation. It was then deployed and cut makespan by over 13% on average (S28 abstract). On his blog he calls himself a fan of exact optimization who nonetheless teaches heuristics (S36, "Know your Heuristics!", paraphrase). [practice] primary (abstract), co-authored; [stated] sole.

---

## 3. Layer 6: expression (how texts are edited)

1. **Overclaims are cut from public text.** On 2020-09-23 a group member (T. Donkiewicz) added to the GCG landing page the line that no matter what problem you give it, GCG will try to decompose it efficiently to solve it quicker. On 2020-10-09 Lübbecke replaced it with a neutral description of structure detection (commit e21f41cc). In the same commit he changed the heading "Decomposition for everyone!" to "Welcome!" and made the figure captions more precise ("after detection" became "after re-arrangement"). [practice] primary, sole (S1).
2. **Citing is not the same as using.** In the same commit he removed 8 paper entries from the list of papers that use GCG (the page's list items fell from 51 to 43). His commit message reads: "not all papers that cite GCG or Gamrath (2010) actually *use* GCG". The removed entries include *Price-and-verify* and *Could we use a million cores to solve an integer program?*. Earlier, in 2019, he added references to the list himself (80ad3d62, 39480fd4, 231e1b9b). [practice] primary, sole (S1).
3. **Release notes lose their self-praise and gain a programme.** He removed "We are proud to release…" from the 3.0.2 notes (b147336e, 2019-06-13). He rewrote the draft 3.1.0 notes as an "ecosystem" release: modelling-language support, much better documentation, and a testing and visualisation suite to help users document their experiments. His commit message called this "added some dreams to the release notes" (011abcd0). The SCIP 8.0 report later calls GCG 3.5 (the first half of) an ecosystem release (S11 §10). [practice] primary, sole, then group.
4. **He writes user documentation himself.** In June 2019 he wrote a documentation use case, the capacitated dominating set: problem description, compact and extended models, ZIMPL files and a larger example (commits c486f369, f4c37688, 2400b26b, 3521fe25). He also added a TODO to describe GCG's architecture for developers (17dfcd9f). The 2025 SCIP 10.0 report states that architecture, two synchronised SCIP instances for the original and master problems, as GCG's central design paradigm (S12 §4, paraphrase). [practice] primary, sole, then group.
5. **How the book is built** (four authors, so no passage is his alone).
   - Each chapter runs from motivation to theory, then "Good to Know", then "More to Know", then a long examples section, then reference notes, then exercises. Solutions are given for all but two exercises (7.21, 8.2), and some exercises carry new theory.
   - Implementation hints are few and marked in the margin. The authors declare that no line was generated by a language model.
   - Chapters were read by four external readers. "Implementation" is listed as a subject for a future book (Ch. 8.2).
   - The book first appeared as an open GERAD cahier (June 2024, 657 pp.), was revised in January 2026, and came out open access with Springer (eBook 2026-02-06, 663 pp.).

   [practice] primary, co-authored (S34 preface and Ch. 8; S35).

---

## 4. Layer 7: research organisation

1. **The solver is a relay of theses.** Each generation of doctoral students owns one component, dated by its first commit and main author (S1, `git log` per file):

   | Component | Main author (commits) | Start |
   |---|---|---|
   | GCG base, relaxator design | G. Gamrath | 2008-11 |
   | Primal heuristics (`heur_xpcrossover`, formerly `heur_extremepoints`) | C. Puchert (38) | by 2012-02 |
   | Basis-based cut separation (`sepa_basis`) | J. Witt (45) | 2014-03 |
   | Detection loop and classification (`class_seeedpool`, `cons_decomp`) | M. Bastubbe (240, 232) | 2016-02 |
   | Version comparison and visualisation | H. Franzen | 2017-12 |
   | Strong branching in branch-and-price (`branch_bpstrong`) | O. Gaul (46) | 2020-12 |
   | Experiments documentation and visualisation suite | T. Donkiewicz | 2020–2021 |
   | Core of 3.5–4.x | E. Mühmer | 2018–2026 |

   The matching papers include S21 (Witt, SEA 2015), S25 (Puchert, OR Proceedings 2011) and the strong-branching work cited in S11 as Gaul's. [observed] primary, group.
2. **His own role in the code is maintainer and editor.** He merged 43 merge requests (2018–2021), ran the 3.0.x bugfix line, curated documentation and the paper list, and enforced repository hygiene (§1.5, §3). [observed] primary, sole.
3. **Infrastructure and openness.**
   - The first public release was GCG 1.0 on 2012-08-01, with release notes that read "This is the first release of GCG. It may contain bugs." The LGPL file came on 2012-07-20.
   - The licence changed to Apache-2.0 on 2025-03-28; per S12, all contributing authors agreed, so that the licence matches SCIP.
   - The GitHub mirror was created on 2023-06-28. Issues and merge requests live on the internal GitLab (the GitHub repository has 0 issues or PRs).
   - There is a Python interface (PyGCGOpt, GCG 3.5) and a HiGHS pricing solver (4.0).

   [observed] primary, group (S1, S4, S11, S12).
4. **Dissemination outside arXiv.** Only a handful of his works are on arXiv: cs/0310034 (2003), three SCIP Optimization Suite reports, and 2602.04984 (2026) (S6). He is an author of the 8.0 and 10.0 suite reports but not of 9.0 (S11–S13). The group uses its own report series, "repORt" (e.g. 2015-029, cited in S15), and GERAD cahiers (S34). [observed] primary.
5. **Community benchmarks.** MIPLIB 2017's ten block-decomposition features were computed with GCG 3.0 in a minimal detection configuration, chosen because full detection is too slow on huge instances, and decompositions were ranked by an area score. No submitter had supplied block-structure files (S14 §4.5). [practice] primary, co-authored (16 authors). That the RWTH co-authors (Bastubbe, Lübbecke) supplied this part is [inferred] from authorship and tool. When MIPLIB 2017 was done, the dedicated `write/miplib2017*` commands were removed in GCG 3.5.0 (CHANGELOG). [observed] primary, group.
6. **Long collaborations across institutions.**
   - Montréal: a six-paper series on primal degeneracy, positive edge and vector space decomposition, 2014–2018, with J. B. Gauthier and J. Desrosiers (S37).
   - The book, idea dating to 2001, an SVN repository from 2015-01-14, published 2024/2026 (S34).
   - Italian co-authors (Caprara, Ceselli, Furini, Malaguti, Traversi) on automatic DW (S17, S18), and Sapienza Rome and TU Eindhoven co-authors on k-VCP (S7, S8).

   [observed] primary.

---

## 5. Layers 2–3: choosing problems and generating ideas, as the record shows them

1. **A tool's sub-problem becomes a research problem.**
   - Re-arranging a matrix into single-bordered block-diagonal form, which is GCG's detection step, becomes an exact branch-and-price study of capacitated hypergraph vertex separation (S23 abstract).
   - The question of which decomposition to pick becomes the SEA 2018 strength study (S15) and the learned selector (S22).
   - A detector by F. Menge ("cutpacking detection for staircase matrices", 2011-12-07; "cutpacking detection via stoer-wagner", 2012-02-18) sits next to the group's experimental study of cut packing (S24). That the two are linked is [inferred].

   [practice] primary, co-authored or group.
2. **A method declared unsuitable is revisited by changing the formulation.** The k-VCP conclusions say that earlier results (Furini et al. 2020, S38, whose author list includes the present co-author F. Furini) suggested branch-and-price was not the right technique. The new paper relaxes the integrality of the extended variables, adds the natural binaries, and so simplifies branching. The title ("strikes back") states the reversal (S8 §5). [practice] primary, co-authored.
3. **From the planner's desk to a method.** Each applied paper starts from a real planning setting and ends with a method plus real-data experiments: in-plant railroads (S30), steel coil coating (S28), SBB Cargo (S29), Kiel Canal (S31). [practice] primary (abstracts), co-authored.
4. **What he looks for in other people's work** (Layer 1, from a sole-authored text). He asks for computational comparisons under identical conditions. He distrusts objectives built from many weighted soft-constraint penalties, which he calls apples and oranges: they make timetables hard to compare and runs unstable. He asks the authors to say which approaches work best for which purpose and to state a vision. He says openly that his own preference for column generation may be biased (S16, pp. 360–361, paraphrase). [stated] primary, sole.

---

## 6. Failures, abandoned directions, rejected work

| What was dropped or failed | Evidence | Tag |
|---|---|---|
| **GCG 3.1.0 never shipped.** Version bumped on 2019-01-15 (M. Walter), release notes drafted by Lübbecke on 2019-07-08, file removed on 2021-10-08 (E. Mühmer). The next minor release was 3.5.0 (2022-01-28). | S1 (git log of `release-notes/release-notes-3.1.0`; tags) | [observed] primary; that 3.1 became 3.5 is [inferred] from the shared "ecosystem" framing (S11) |
| **GAMS support** promised in the 3.1.0 draft does not appear anywhere in the CHANGELOG. A Python interface shipped instead. | S1 (grep, 2026-11-08), S11 §10.3 | [observed] absence; that Python replaced GAMS is [inferred] |
| **Legacy detection mode removed** with its detectors `connected`, `staircase`, `random`, `cutpacking`, `colors` and `mcl` (GCG 3.5.0). The `cutpacking` files were deleted in the 2020-05-14 detection refactoring. | CHANGELOG 3.5.0; commit ccb802f7 | [observed] primary, group |
| **One-off MIPLIB 2017 feature commands** removed; the "toolbox" explore feature removed. | CHANGELOG 3.5.0 | [observed] primary |
| **Eight built-in score types of GCG 3.0** (max white, border area, classic, …, experimental Benders score) replaced by score plugins; the old functions deleted. | CHANGELOG 3.0.0, 3.6.0 | [observed] primary |
| **Test set `goodinstances.test`** labelled "Not recommended for use anymore"; the guide's "custom logging" feature still reads "not yet implemented" in 2026 (file last changed 2020-10). | S3 | [observed] primary, group |
| **Exact separation of clique-partitioning constraints** implemented as a branch-price-and-cut variant, measured (bound almost the same as the cheap clique family), and left out of the final algorithm because separation is NP-hard and costly. | S8 §3.1.4, App. F (App. E in v1) | [practice] primary, co-authored |
| **First of two symmetry approaches** tried and not reported in full. | S8 §3.2 | [practice] primary |
| **Hard instances** (markshare1/2, mas74/76) and **one failing instance** (mine-166-5) excluded, with the reason given. | S15 §2, §4.1 | [practice] primary |
| **The learned selector of when to decompose** (S22, 2017) leaves no trace in GCG's CHANGELOG, docs or `src` (grep for Kruber, learning, supervised; 2026-11-08). Whether a prototype existed elsewhere is unknown. | S1, S22 | [observed] absence; that it was never transferred into GCG is [inferred] |
| **Strong branching on by default** called conceivable in 2021; still off in 2026. No reason is documented. | S11, S1 | [observed] primary |
| **Book timeline overrun.** The idea dates to January 2001. The first SVN commit (by `luebbecke`, 2015-01-14) planned a 2015–2017 publication year ("DDL1x"). Published as a cahier in 2024 and as a book in 2026. | S34 preface | [stated] primary, co-authored |
| **Blog abandoned** after 9 posts (2014-10-15 to 2016-03-02). | S36 (WordPress API) | [observed] primary |
| **Career rejections.** Postdoc applications in the US and Canada brought only rejections; the 2010 RWTH chair was offered to him after five others had declined it. | S34 author bio | [stated] primary |
| **Retractions or errata**: none found. Crossref searches for erratum, correction, corrigendum and retraction return only a different Lübbecke (an oceanographer). | S41 | [observed] absence |

---

## 7. Era and resources behind the practices

| Period | Position and team (per S34 bio) | Tools and compute | Practices visible then |
|---|---|---|---|
| to 2001 | PhD, TU Braunschweig | CPLEX era (first contact with solvers via CPLEX 3.0, per bio) | column generation with a custom label-correcting pricing algorithm; real-life railroad data (S30) |
| 2001–2010 | combinatorial optimization and graph algorithms group in Berlin; habilitation at TU Berlin 2007; visiting professor at TU Darmstadt | SCIP 0.81-era column generation; GCG started on SCIP in 2008 (first commit by G. Gamrath) | industrial projects with deployed or validated tools (S28, S29); SEA conference papers (S19, S26) |
| 2010–2018 | chair at RWTH Aachen (from 2010), PhD-student group | internal SVN, then git; hMETIS; MIPLIB 2010 harness; RWTH cluster scripts; strIPlib internal from 2012 | relay of thesis-built components; adversarial MIPLIB tests; conference-then-journal publishing |
| 2018–2022 | chair; personal maintainer phase 2018–2021 | GitLab CI from 2019; Xeon L5630 nodes (2.13 GHz, 16 GB); Python visualisation suite | documentation-first "ecosystem" release; MIPLIB 2017 features; diversity-controlled test sets |
| 2022–2026 | chair and GERAD; book with Montréal co-authors | GitHub mirror 2023; Apache-2.0 in 2025; HiGHS pricing; SCIP 9.2.3 and SoPlex 7.1.5 for project code; Zenodo deposits | open book first as a cahier; fair re-runs of competitors; ablations; components measured and then dropped |

---

## 8. Stated against practised: pointers for Phase 2 (to check against `02-methodology.md`)

| Stated | Practised | Fit |
|---|---|---|
| Send abstracts or extended abstracts to refereed conferences first (S36, 2014) | At least six conference-to-journal pairs, 2004–2015 (§1.4) | consistent |
| Know when to stop; he admits he is not very good at it (S36, 2014) | Book planned for 2015–2017, appeared as a cahier in 2024 and with Springer in 2026; the 3.1 release slipped from 2019 to 2022 as 3.5 (§6) | consistent with the self-assessment |
| Fair comparison needs identical conditions (S16, 2015) | Competitors re-run with the same CPLEX version and time limit; version-comparison tooling (§1.2) | consistent (co-authored and group) |
| Be honest, stick to supported results (S36, 2014) | Landing-page overclaim cut; paper list pruned; v2 abstract softened; MIPLIB area-score caveat (§2, §3) | consistent |
| Start writing early, because writing produces new questions (S36, 2014) | Book preface: writing exposed supposed facts that were wrong, and gaps in the literature (S34) | consistent (the book is co-authored) |
| His feedback style: question everything, try to misunderstand as much as possible (S36, 2014) | He rewrote a student's landing-page claims within 16 days (§3.1) | consistent, one instance |

---

## Contradictions (kept, not reconciled)

1. **The k-VCP paper's "fully open-source" goal against its artefacts** (co-authored; the code is the first author's).
   - The paper justifies SoPlex by the goal of a fully open-source algorithm (S8 §4.1).
   - Yet the instance preprocessing and filtering are implemented in Gurobi 11.0.3 (S8 App. E), and the README lists Gurobi for preprocessing and ILP warm start (S10).
   - The repository's licence is an "Academic and Research License" that forbids commercial use and distributing modified versions without permission (S10). The Zenodo record for the same code says CC BY 4.0 (S9).
2. **Headline claim against the body** (arXiv v1 → v2).
   - v1's abstract ends with a sentence saying the algorithm "consistently outperforms all competitors" on all 608 instances and solves 73 open ones (S7, CC BY 4.0). v2 deletes that sentence (S8).
   - Both versions keep the introduction's claim of outperforming all existing exact algorithms.
   - Both report instances that the earlier study solved and the new method does not (S8 §4.4, App. G).
3. **Decomposition for everyone, without user interaction, against documented failure modes.** The landing-page text Lübbecke wrote in 2020 says that, since no user interaction is necessary, GCG provides decomposition-based MIP solving to everyone (S1, e21f41cc). His 2017 co-authored paper says a wrongly detected structure can make the solver fail completely (S22). The group's guide warns that detectors disabled by default (e.g. arrowhead) can change results a lot (S3).
4. **strIPlib's status.** The 2020 guide tells users to filter instances in the strIPlib web front end (S3), while the 2021 SCIP 8.0 report calls strIPlib unreleased (S11). Test files built from it date back to 2012–2013 (S1).
5. **Strong branching by default.** The 2021 report finds a default-on setting conceivable (S11); the code still has it off in 2026 (S1). This is not a logical contradiction (more investigation was announced), but no follow-up evaluation was found.

---

## Gaps (what could not be found or read)

- **Full texts not read** (closed access, or mirrors blocked): S17 (HAL blocked by a bot challenge; only the abstract was read via IRIS Bologna/Sapienza), S18–S33, the EJOR 2015 resource-leveling paper (title only), and the stable-set report repORt 2015-029 (host unreachable). So the test sets, baselines and time limits of the automatic-DW journal paper are known only from the repository's `gcgjournal` set, not from the paper.
- **Reviews and rebuttals**: no OpenReview reviews exist. OpenReview holds only seven DBLP-imported records (S40). No published rejoinder exchange was read: the authors' rejoinder to S16 in TOP 2015 was not read.
- **Issue tracker**: the group's GitLab (`git.or.rwth-aachen.de`) was unreachable, so issue discussions (e.g. #342, #369) and merge-request reviews (!163) could not be read. GitHub has no issues or PRs.
- **The GCG website and chair pages** (`gcg.or.rwth-aachen.de`, `or.rwth-aachen.de`) timed out, as on 2026-11-05. strIPlib is a JavaScript-only app, so its content and release date could not be read.
- **SCIP Optimization Suite 4.0–7.0 reports** (GCG 2.x–3.0 sections, ZIB-Reports) were not checked. Optimization Online was not searched.
- **Theses of the GCG developers** (Gamrath 2010, Bergner, Puchert, Witt, Bastubbe, Gaul, Donkiewicz) were not read. Their experiment chapters would show the group's protocol in more detail; this belongs to agent 04.
- **A GCG-versus-DIP comparison** in print: none located, although the scripts exist (2012).
- **Early versions of the IJOC 2022 paper** (SSRN 2019 versus final) and of the Branch-and-Price cahier (June 2024 original against the January 2026 revision) were not compared. Only the revised cahier was read.
- **His personal share of co-authored experimental design** cannot be separated from his co-authors' in any paper read. Every co-authored practice above is the team's.

---

## Sources

- S1. GCG repository `scipopt/gcg` (RWTH Aachen OR group and contributors), git history 2008-11-25 to 2026-10-30, `master` c0e230a3. https://github.com/scipopt/gcg (Apache-2.0). Primary.
- S2. GCG `CHANGELOG` (0.4–5.0) and `release-notes/` 1.0.0–3.0.2, in S1. Primary.
- S3. GCG docs `doc/resources/devs/howtouse/conduct-experiments.md` (T. Donkiewicz 2020, edits by Lübbecke 2020-09-25) and `diverse-testset-generation.md` (Donkiewicz 2021), in S1. Primary.
- S4. GitHub REST API metadata for `scipopt/gcg` (created 2023-06-28; Apache-2.0; 0 issues or PRs), queried 2026-11-08. Primary.
- S5. ORCID public record 0000-0002-2635-0522, works list (60 groups). https://orcid.org/0000-0002-2635-0522. Primary (bibliographic).
- S6. arXiv API author query (Lübbecke, Lubbecke, Luebbecke), 2026-11-08. Primary (bibliographic).
- S7. F. Ciccarelli, F. Furini, C. Hojny, M. Lübbecke, "Branch-and-price strikes back for the k-vertex cut problem", arXiv:2602.04984v1, 2026-02-04 (CC BY 4.0). Primary.
- S8. Same paper, arXiv:2602.04984v2, 2026-06-05. Primary.
- S9. Zenodo, "FabioCiccarelli/BP_k-vertex-cut: v1.0.2", 2026-01-13, DOI 10.5281/zenodo.18224768 (concept DOI 10.5281/zenodo.17897865). Primary.
- S10. GitHub `FabioCiccarelli/BP_k-vertex-cut`, README and LICENSE, read 2026-11-08. Primary.
- S11. K. Bestuzheva et al. (incl. M. E. Lübbecke), "The SCIP Optimization Suite 8.0", arXiv:2112.08872, 2021-12-16, GCG section 10. Primary (group).
- S12. C. Hojny et al. (incl. M. E. Lübbecke), "The SCIP Optimization Suite 10.0", arXiv:2511.18580, 2025-11-23, GCG section 4. Primary (group).
- S13. "The SCIP Optimization Suite 9.0", arXiv:2402.17702, 2024, author list only. Primary (bibliographic).
- S14. A. Gleixner et al. (incl. M. Bastubbe, M. E. Lübbecke), "MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library", Mathematical Programming Computation 13 (2021) 443–490, DOI 10.1007/s12532-020-00194-3, Sect. 4.5 (CC BY 4.0). Primary.
- S15. M. Bastubbe, M. E. Lübbecke, J. T. Witt, "A Computational Investigation on the Strength of Dantzig-Wolfe Reformulations", SEA 2018, LIPIcs 103, 11:1–11:12, DOI 10.4230/LIPIcs.SEA.2018.11 (CC BY). Primary.
- S16. M. E. Lübbecke, "Comments on: An overview of curriculum-based course timetabling", TOP 23 (2015) 359–361, DOI 10.1007/s11750-015-0364-1. Primary (sole author).
- S17. M. Bergner, A. Caprara, A. Ceselli, F. Furini, M. E. Lübbecke, E. Malaguti, E. Traversi, "Automatic Dantzig–Wolfe reformulation of mixed integer programs", Mathematical Programming 149 (2015) 391–424, DOI 10.1007/s10107-014-0761-5. Abstract only, via https://hdl.handle.net/11585/250075 and https://hdl.handle.net/11573/1571737. Primary.
- S18. M. Bergner, A. Caprara, F. Furini, M. E. Lübbecke, E. Malaguti, E. Traversi, "Partial Convexification of General MIPs by Dantzig-Wolfe Reformulation", IPCO 2011, LNCS, DOI 10.1007/978-3-642-20807-2_4. Abstract only. Primary.
- S19. G. Gamrath, M. E. Lübbecke, "Experiments with a Generic Dantzig-Wolfe Decomposition for Integer Programs", SEA 2010, LNCS 6049, pp. 239–252, DOI 10.1007/978-3-642-13193-6_21. Abstract only. Primary.
- S20. M. E. Lübbecke, "Automatic Decomposition and Branch-and-Price—A Status Report", SEA 2012, LNCS, DOI 10.1007/978-3-642-30850-5_1. Abstract only. Primary (sole author).
- S21. M. E. Lübbecke, J. Witt, "Separation of Generic Cutting Planes in Branch-and-Price Using a Basis", SEA 2015, LNCS, DOI 10.1007/978-3-319-20086-6_9. Abstract only. Primary.
- S22. M. Kruber, M. E. Lübbecke, A. Parmentier, "Learning When to Use a Decomposition", CPAIOR 2017, LNCS, DOI 10.1007/978-3-319-59776-8_16. Abstract only. Primary.
- S23. M. Bastubbe, M. E. Lübbecke, "A branch-and-price algorithm for capacitated hypergraph vertex separation", Mathematical Programming Computation (2020; online 2019), DOI 10.1007/s12532-019-00171-5. Abstract only. Primary.
- S24. M. Bergner, M. E. Lübbecke, J. Witt, "A Branch-Price-and-Cut Algorithm for Packing Cuts in Undirected Graphs", SEA 2014, LNCS, DOI 10.1007/978-3-319-07959-2_4. Abstract only. Primary.
- S25. M. E. Lübbecke, C. Puchert, "Primal Heuristics for Branch-and-Price Algorithms", Operations Research Proceedings 2011 (2012), DOI 10.1007/978-3-642-29210-1_11. Abstract only. Primary.
- S26. E. T. Coughlan, M. E. Lübbecke, J. Schulz, "A branch-and-price algorithm for multi-mode resource leveling", SEA 2010, DOI 10.1007/978-3-642-13193-6_20 (abstract), and "A branch-price-and-cut algorithm for multi-mode resource leveling", EJOR (2015), DOI 10.1016/j.ejor.2015.02.043 (title only). Primary.
- S27. G. Lach, M. E. Lübbecke, "Curriculum based course timetabling: new solutions to Udine benchmark instances", Annals of Operations Research (2012; online 2010), DOI 10.1007/s10479-010-0700-7. Abstract only. Conference precursor: "Optimal university course timetables and the partial transversal polytope", WEA 2008, DOI 10.1007/978-3-540-68552-4_18. Primary.
- S28. W. Höhn, F. G. König, R. H. Möhring, M. E. Lübbecke, "Integrated Sequencing and Scheduling in Coil Coating", Management Science (2011), DOI 10.1287/mnsc.1100.1302. Abstract only. Primary.
- S29. A. Ceselli, M. Gatto, M. E. Lübbecke, M. Nunkesser, H. Schilling, "Optimizing the Cargo Express Service of Swiss Federal Railways", Transportation Science (2008), DOI 10.1287/trsc.1080.0246. Abstract only. Primary.
- S30. M. E. Lübbecke, U. T. Zimmermann, "Engine Routing and Scheduling at Industrial In-Plant Railroads", Transportation Science 37(2) (2003), DOI 10.1287/trsc.37.2.183.15251. Abstract only. Primary.
- S31. E. Lübbecke, M. E. Lübbecke, R. H. Möhring, "Ship Traffic Optimization for the Kiel Canal", Operations Research (2019), DOI 10.1287/opre.2018.1814. Abstract only. Primary.
- S32. Z. Steever, C. C. Murray, J. Yuan, M. H. Karwan, M. E. Lübbecke, "An Image-Based Approach to Detecting Structural Similarity Among Mixed Integer Programs", INFORMS Journal on Computing (2022), DOI 10.1287/ijoc.2021.1117 (SSRN version DOI 10.2139/ssrn.3437981). Abstract only. Primary.
- S33. M. E. Lübbecke, J. T. Witt, "The strength of Dantzig–Wolfe reformulations for the stable set and related problems", Discrete Optimization (2018), DOI 10.1016/j.disopt.2018.07.001. Metadata only. Earlier report: J. T. Witt, M. E. Lübbecke, "Dantzig-Wolfe reformulations for the stable set problem", repORt 2015-029, RWTH Aachen OR, November 2015 (as cited in S15; not read). Primary.
- S34. J. Desrosiers, M. Lübbecke, G. Desaulniers, J. B. Gauthier, "Branch-and-Price", Les Cahiers du GERAD G-2024-36 (June 2024, revised January 2026). https://www.gerad.ca/en/papers/G-2024-36. Preface, "About the authors" and Ch. 8 read. Primary (four authors).
- S35. Same book, Springer Cham 2026 (eBook 2026-02-06, XV + 663 pp., open access), DOI 10.1007/978-3-031-96917-1. Publisher page only. Primary.
- S36. M. E. Lübbecke, blog "café opt", https://mluebbecke.wordpress.com: 9 posts, 2014-10-15 to 2016-03-02, listed via the WordPress public API. Read: "Where are we heading?" (2014-11-04), "How to write a paper" (2014-11-21), "Know your Heuristics!" (2014-12-19), "Aussois" (2015-01-07), "Are we too complicated?" (2015-03-23). Primary (sole, stated).
- S37. J. B. Gauthier, J. Desrosiers, M. E. Lübbecke, degeneracy series. Metadata only. Primary.
  - Row-reduced column generation for degenerate master problems, EJOR, DOI 10.1016/j.ejor.2013.12.016 (author order Desrosiers, Gauthier, Lübbecke)
  - Decomposition theorems for linear programs, ORL, DOI 10.1016/j.orl.2014.10.001
  - About the minimum mean cycle-canceling algorithm, DAM, DOI 10.1016/j.dam.2014.07.005
  - Tools for primal degenerate linear programs: IPS, DCA, and PE, EJTL, DOI 10.1007/s13676-015-0077-5
  - A strongly polynomial Contraction-Expansion algorithm for network flow problems, C&OR, DOI 10.1016/j.cor.2017.02.019
  - Vector Space Decomposition for Solving Large-Scale Linear Programs, Operations Research, DOI 10.1287/opre.2018.1728
- S38. F. Furini, I. Ljubić, E. Malaguti, P. Paronuzzi, "On integer and bilevel formulations for the k-vertex cut problem", Mathematical Programming Computation 12 (2020), DOI 10.1007/s12532-019-00167-1. Metadata only (the baseline study of S7/S8). Primary.
- S39. D. Cornaz, F. Furini, M. Lacroix, E. Malaguti, A. R. Mahjoub, S. Martin, "The vertex k-cut problem", Discrete Optimization 31 (2019), DOI 10.1016/j.disopt.2018.07.003. Metadata only. Primary.
- S40. OpenReview API note search "Lübbecke", 2026-11-08: 7 DBLP-imported records, no reviews. Primary (absence).
- S41. Crossref API searches with author Lübbecke for erratum, correction, corrigendum and retraction, 2026-11-08: no hit for M. E. Lübbecke. Primary (absence).
- S42. strIPlib web app, https://striplib.or.rwth-aachen.de (JavaScript only; build 2026-03-13). Primary, minimal.
- S43. CMU Tepper "Listing of OR Blogs", as surfaced by WebSearch (used only to locate S36). Secondary.

Other conference-to-journal pairs cited in §1.4, all from S5:

- S. P. Fekete, M. E. Lübbecke, H. Meijer, "Minimizing the Stabbing Number of Matchings, Trees, and Triangulations": SODA 2004 (no DOI in ORCID; arXiv cs/0310034) → Discrete & Computational Geometry 2008, DOI 10.1007/s00454-008-9114-6.
- "Rectangle covers revisited computationally": LNCS 2005 (no DOI in ORCID) → ACM JEA 2006, DOI 10.1145/1187436.1216583.
- "On minimum k-modal partitions of permutations": LATIN 2006, DOI 10.1007/11682462_36 → J. Discrete Algorithms 2008, DOI 10.1016/j.jda.2008.01.002.
