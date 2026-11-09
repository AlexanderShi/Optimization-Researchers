# Matteo Fischetti: Peer Critique (blind spots, limits, contested judgements)

| Field | Value |
|---|---|
| Researcher | Matteo Fischetti (University of Padova, DEI; born 1958; living). Not Martina Fischetti, his co-author on wind-farm and other work: nothing in this file is hers. Lens: MILP primal heuristics (feasibility pump, local branching, proximity search), Benders cut selection and in-out stabilization, symmetry (orbital shrinking), performance variability (erraticism, bet-and-run), and the MILP models he built for neural networks, robust and bilevel problems |
| Dimension | Research agent 05 of 06: peer critique. Failed or partial replications, published comparisons with rival methods, counterexamples, independent re-measurements, vendor and open-source implementers' choices, rival schools, and how each critique was answered |
| Research date | 2026-11-08 |
| Sources consulted | 76 (24 written or co-signed by Fischetti, 52 by others), listed under "Sources". Read in the original text at the page cited (P): 32. Known only from an abstract, metadata or a Semantic Scholar citation context (S): 44 |
| WebSearch calls | 5 (of 5 allowed) |
| User-supplied material | None. `references/sources/{papers,talks,essays,software}/` hold only `.gitkeep`; `private/` was not opened. **Nothing in this file is from user-supplied material** |
| Transcripts saved | None. Slide decks and papers stay unsaved (copyrighted); working copies sit in the scratch folder only |
| Quotation policy | To stay within copyright limits, findings are paraphrased with a page, slide or file locator. The note holds **one** sentence-level verbatim quotation (13 words, §2.5, marked "verbatim"). Code identifiers and parameter names appear in backticks; titles appear only in the Sources list. Check the exact wording at the source before quoting downstream |
| Language | English (team.json) |

**Tags.**
- [stated]: written by Fischetti, or in a paper, preprint, slide deck or manuscript he authored or co-signed.
- [practice]: what his papers, code or experiments show was done.
- [observed]: what a third party wrote or reported. **Insiders are flagged**: Andrea Lodi (co-author of FP and LB), Domenico Salvagnin (former doctoral student, PhD Padova 2009 with Fischetti as advisor per research note 04; co-author of FP 2.0 and of the 2010 Benders note), Fred Glover (co-author of FP), Ivana Ljubić and Markus Sinnl (co-authors of the bilevel and UFL work), Michele Monaci (co-author of proximity search, erraticism and backdoor branching). They are not outside critics.
- [inferred]: my reading. The basis is given; do not quote it as anyone's view.
- (P): read in the critic's or Fischetti's own text at the page cited. (S): abstract only, metadata only, a claim relayed by another author, or a Semantic Scholar citation context ("S2 context"; full text not read).

**How the critiques were found.**
1. Pulled Semantic Scholar citation contexts for 17 of his works (FP 2005: 464 citing records; LB 2003: 748; FP 2.0: 113; proximity search: 89; Benders note 2010: 178; UFL Benders 2017: 256; erraticism: 80; orbital shrinking: 23 + 11; Fischetti-Jo: 360; bilevel 2017: 204; backdoor branching: 41; lexicographic Gomory: 41; first Chvátal closure: 134; three others with almost no contexts) and filtered them for critical wording [S75].
2. Opened every critic cited below in a legal open copy (arXiv, Optimization Online, author or university repositories, open-access journals), except items marked (S).
3. Read the Fischetti-side texts the critics target in his own preprints from www.dei.unipd.it/~fisch/papers/ and slides/ (the host answered on 2026-11-08), and the 2026 FP reproducibility package.
4. Read the implementers' code and documentation: CBC's feasibility pump (COIN-OR), SCIP's heuristic defaults, Gurobi's and CPLEX's parameter pages.
5. Verified identifiers with Crossref, the arXiv API, Unpaywall (email parameter nuwa-skill@users.noreply.github.com), OpenAlex, DataCite and the GitHub API.
6. Not reached, and not routed around: the full text of Achterberg-Berthold 2007 (ScienceDirect HTTP 403; ZIB OPUS sits behind an Anubis proof-of-work bot check, not bypassed); Lodi-Tramontani 2013 (INFORMS HTTP 403); closed Springer, INFORMS and Elsevier texts (listed under Gaps). web.archive.org was not used.

**Attribution caveats that must survive into the skill.**
- **Every method here is co-authored except the 2026 FP study.** FP with Glover and Lodi; LB with Lodi; proximity search, erraticism, backdoor branching and the robust study with Monaci; the 2010 Benders note with Salvagnin and Zanette; UFL Benders with Ljubić and Sinnl; bilevel with Ljubić, Monaci and Sinnl; orbital shrinking with Liberti; the neural-network MILP with Jason Jo. The papers do not divide roles. A critique of a method credited to Fischetti targets a team's paper. That he named the pump after the Electron Pump in Asimov's novel *The Gods Themselves* is relayed by Berthold, Lodi and Salvagnin ([S26] preprint p. 1, footnote) [observed, insiders].
- **The 2026 FP study** [S24] is self-declared: sole author in CITATION.cff and in both Zenodo records (DataCite creator: Fischetti, Matteo). The GitHub account `mfischetti-arch` was created on 2026-09-04 and holds one repository. I found no link to it in the homepage HTML; research note 03 grades the attribution a strong inference. The README says the manuscript was submitted to Mathematical Programming Computation; it is **unreviewed**. Its declarations say two AI assistants were used under the author's direction to draft and edit text, write and debug scripts, run internal adversarial reviews and audit the manuscript before submission, and that the author checked text, numbers and code and takes full responsibility ([S24] p. 25) [stated].
- **Code that critics measured is often not his.** CBC's pump is mostly John J. H. Forrest's code (lp-team guest; §2.3), SCIP's is the ZIB group's objective pump, CPLEX's is closed. A failed replication on CBC or SCIP measures that code, not the published algorithm.

---

## 0. Summary for Phase 2

| # | Recurring critique (blind spot / limit) | Raised by | Fischetti-side answer | Status |
|---|---|---|---|---|
| Q1 | **FP ignores the objective, so its solutions are poor.** The 2005 cutoff variant gave only mildly positive results and was never compared with local-search heuristics | Achterberg-Berthold 2007 [S25] (relayed); Berthold-Lodi-Salvagnin 2019 [S26] (insiders); Huang-Mehrotra 2013 [S27]; Lewis-Alidaee-Glover-Kochenberger 2009 [S32] (Glover an insider); Gurobi docs [S40] | Conceded, and the critic's fix adopted as baseline, in FP 2.0 (2009) [S3]. In 2026 he argues the 2005 cutoff plus recovery, dropped by implementers, should be restored, and measures it on top of SCIP's objective pump [S24] | Answered only in an unreviewed 2026 study whose headline comparison is post hoc |
| Q2 | **Cycling, stalling and no convergence theory.** The 2005 random flip can loop forever on a two-variable instance | Boland et al. 2012 [S30]; De Santis et al. 2013 [S31]; Geißler et al. 2017 [S29]; Dey et al. 2018 [S28] (Salvagnin an insider); Bonami-Kılınç-Linderoth 2012 [S34] | Theory came from others. He co-authored a follow-up with the Boland group (2014) [S4]; FP 2.0 cuts restarts with propagation [S3] | Drawback conceded in his own texts; counterexample not answered by him in print |
| Q3 | **Replication with other codes falls short; key details live only in source code** | Huang-Mehrotra 2013 on CBC 2.3 [S27]; Berthold-Lodi-Salvagnin 2019 [S26] | None found for the 2005-2007 papers; the 2026 package publishes every script, log and solution [S24] | Open for the original papers |
| Q4 | **Local branching beaten by RINS and DINS; off by default in solvers; slow as an LNS selector** | Danna-Rothberg-Le Pape 2005 (ILOG) [S42]; Ghosh 2007 [S44]; CPLEX docs [S41]; SCIP code [S39]; Huang et al. 2023 [S47, S48] | 2022: the neighbourhood size should be learned per instance [S7] | Mixed: Hendel 2022 finds LB among the two most successful neighbourhoods in SCIP's ALNS [S46] (C3) |
| Q5 | **Proximity search: few independent tests; standalone heuristic off in SCIP** | Rodrigues et al. 2021 [S50]; SCIP code [S39] | Trade-offs stated up front, 2014 [S8] | Open (thin evidence either way) |
| Q6 | **2010 Benders cut selection: cuts may be non-supporting; the choice depends on row scaling; later methods dominate** | Brandenberg-Stursberg 2021 [S51]; Larsen et al. 2026 [S52] (unrefereed) | None found; 2025-2026 slides stress stabilization instead [S11, S12] | Open |
| Q7 | **UFL Benders (2017): its heuristic bounds on Körkel-Ghosh instances beaten by a metaheuristic about two orders of magnitude faster** | Karapetyan-Goldengorin 2018 [S54] | None found | Open; the aims differ (exact versus heuristic) |
| Q8 | **Robust LP/MIP: the robust-MIP conclusion not replicated; no statistics, arithmetic means, cuts at every node** | Bertsimas-Dunning-Lubin 2016 [S55] | None found | Open (C4) |
| Q9 | **Erraticism and bet-and-run: baselines with CPLEX dynamic search off; needs solver internals; the backdoor method may miss small backdoors** | Lissovoi et al. 2017 [S58]; Khalil-Vaezipoor-Dilkina 2022 [S60]; [inferred] on baselines | Random-sampling follow-up, 2016, co-authored (listed under [S75]) | Bet-and-run confirmed by Carvajal et al. 2014 [S56]; backdoor critique open |
| Q10 | **Orbital shrinking is only a relaxation; exact only under extra conditions** | Own text [S16]; Knueven-Ostrowski-Watson 2018 [S61]; van Doornmalen-Hojny 2024 [S62] | Presented as a relaxation from the start; own result: the whole-group bound is no better than the LP bound on 31 of 39 instances | Limit conceded |
| Q11 | **Neural-network MILP: weak big-M relaxation; does not scale** | Anderson et al. 2020 [S63]; Khalil-Gupta-Dilkina 2018 [S64]; Grimstad-Andersson 2019 [S65] | Bound tightening; scale limit stated in the paper [S18] | Conceded; stronger formulations came from others |
| Q12 | **Bilevel MIX++: general-purpose claim versus later problem-specific solvers; assumptions narrow applicability** | Tanınmış-Sinnl 2022 [S68]; Furini et al. 2019 [S69]; Cerulli et al. 2023 [S70] (Ljubić and Sinnl insiders); Tanınmış-Aras-Altınel 2022 [S67] | Not needed: the co-authors wrote the problem-specific papers | Kept as contradiction C5 |
| Q13 | **Steiner (DIMACS 2014) records later beaten** | Rehfeldt-Koch-Maher 2019 (SCIP-Jack) [S71] | None found | Normal progress, not a dispute |

**Where the critiques land in the seven layers (framework §一)** [inferred grouping]

| Layer | What the critiques bear on | Items |
|---|---|---|
| 1 Taste (what counts as a good result) | Feasibility first, objective later; a simple scheme on a black-box solver as the contribution; general-purpose solvers as the goal | Q1, Q4, Q12 |
| 2 Problem choice | MIPLIB-style 0-1 testbeds; binary-only neighbourhoods (LB, proximity); single showcase instances (gs250a-1) | Q4, Q5, Q7, §5.2 |
| 3 Idea generation | One device reused across problems (distance objectives, cutoffs, interior points, aggregation) without convergence theory | Q2, Q10 |
| 4 Experiments | Baselines with solver features disabled by callbacks; comparison with published numbers from other machines; arithmetic means; no significance tests; parameters hand-picked on the test set | Q8, Q9, §1, §8 |
| 5 Judging results | Verdicts that a variant beats its rivals, later reversed or qualified (robust MIP, LB, MIX++, Benders selection) | Q4, Q6, Q8, Q12 |
| 6 Expression | Algorithmic details in code but not in the paper (FP restarts); a long draft compressed into an 8-page note (Benders selection) | Q3, §5.1 |
| 7 Organisation | Co-authors and former students supply most of the later critique and theory; critics become co-authors | Q2, §13 |

---

## 1. Era and resource context

- **2003-2005: a notebook and a commercial solver.** FP 2005 ran on a Pentium M 1.6 GHz notebook with 512 MB of memory, with ILOG-Cplex 8.1, a 1,800-second limit and 83 0-1 MIPs (44 from MIPLIB 2003, 39 others) ([S1] preprint pp. 5-6) [practice, P]. Danna et al. say their RINS code also beat the LB version Fischetti and Lodi used, which ran on an earlier CPLEX release (S2 snippet, truncated at the version number) [S42] [observed, S].
- **Baselines tuned with the vendor.** For FP 2005 the CPLEX baseline ran without presolve, a setting chosen after extensive experiments and contacts with ILOG-Cplex staff ([S1] p. 6) [practice, P].
- **2008-2013: single-thread CPLEX through callbacks on a desktop.** FP 2.0: Cplex 11.2 as LP solver on an Intel Core2 Q6600 ([S3] p. 13). Benders note: Cplex 11.0 on a Q6600 ([S9] p. 10). Proximity search: Cplex 12.4 on an Intel i5-750, single thread ([S8] p. 12). Erraticism: Cplex 12.3 on an i5-750, single thread; every code installed a callback, possibly a dummy one, which switches off CPLEX's proprietary dynamic search ([S14] p. 6) [practice, P].
- **2016-2018: small clusters and 4-thread runs.** UFL Benders: Cplex 12.6 ([S10] p. 11); Karapetyan and Goldengorin name an Intel Xeon E3-1220V2 as the comparison machine (their citation key is broken, printed as "[?]") and note that FLS used four cores ([S54] arXiv p. 15). Bilevel: Cplex 12.6.3 on Xeon E5-2670v2 nodes, 4-thread runs ([S19] p. 13). Neural networks: CPLEX 12.7 on a standard 4-core notebook ([S18] p. 11) [practice, P].
- **2026: one author, a cluster, an AI-assisted pipeline.** A pinned SCIP snapshot (dba4b2a, 2026-08-24), Gurobi 13.0.3, 424 MIPLIB 2017 instances, comparisons declared in advance with Holm correction, every solution revalidated, raw logs on Zenodo ([S24] README; manuscript pp. 9, 13-14, 25) [practice, P].
- [inferred] Most of the methods critiqued below were judged on one commercial solver, single-threaded, with some of that solver's own advanced features switched off. Critics who measured on other codes (CBC, SCIP) or against modern defaults got weaker results. The pattern recurs in §2.3, §3 and §7.

---

## 2. Feasibility pump (Q1-Q3)

### 2.1 Solution quality: the critique

- [stated, P] FGL 2005's abstract presents FP as competitive with ILOG-Cplex in both speed and the quality of the first solution ([S1] p. 1). The comparison is against CPLEX root-node heuristics: CPLEX's solution was strictly better in 33 cases, FP's in 46 (p. 9). The same paper says FP pays no particular attention to solution quality (p. 10) and proposes an objective cutoff with a recovery LP (p. 11; §2.5 below).
- [observed, S] **Achterberg and Berthold (ZIB) 2007** [S25], full text not read. As relayed by insiders: they gave a simple fix for what the review calls FP's main weakness, the often poor quality of its solutions ([S26] p. 6); their objective pump finds better solutions on average, at the price of a slightly lower success rate and more iterations and running time ([S26] p. 7).
- [observed, P, insiders] **Berthold, Lodi, Salvagnin 2019** [S26] on the 2005 paper: FP's solutions are often of low quality, since the objective enters only at the start (p. 4). The 2005 cutoff variant gave only mildly positive results, and the 2005 paper compared it with no general-purpose local-search heuristic such as local branching (p. 4). This criticizes the original evaluation, not only the method.
- [observed, P] **Huang and Mehrotra** [S27] (Optimization Online preprint 2010; COAP 2013): FP's solutions are usually poor because it does not consider the objective (preprint p. 9).
- [observed, S, insider] **Lewis, Alidaee, Glover, Kochenberger 2009** [S32] (Glover co-authored FP): FP beat CPLEX at finding a first feasible solution but could not compete with CPLEX for optimal or near-optimal ones (S2 context).
- [observed, S] Baena, Castro and González 2015 [S33], on controlled tabular adjustment: their fix-and-relax heuristic outperformed FP and the other start heuristics in practice (S2 context).
- [observed, P] **Vendors in 2026.**
  - Gurobi's `PumpPasses` entry (default −1) calls the heuristic expensive, says it generally produces poor-quality solutions, and advises using it only when other means, default tree search included, fail to find a feasible solution [S40]. The same text appears under `ZeroObjNodes` and `MinRelNodes`, so it is boilerplate for last-resort heuristics, not an FP-specific study. Tobias Achterberg (team member) is Gurobi's VP of R&D per team.json; the docs are unsigned and nothing here is attributed to him.
  - CPLEX 22.1.2 [S41]: the FP switch defaults to 0 (CPLEX chooses). Setting 2, the objective emphasis, usually gives better objective values but fails more often to find a feasible solution (wording returned by the fetch tool; the IBM page is script-rendered and could not be cross-checked with curl).
  - [inferred] Both vendors keep FP as an automatic or last-resort component, and CPLEX documents the same quality-versus-success trade-off that Achterberg and Berthold reported.

### 2.2 Cycling, randomization and the missing theory

- [stated, P] The authors named the problem themselves: cycling is a main problem of the basic implementation ([S1] p. 5); the tendency to stall is a main drawback of the basic scheme ([S3] p. 2).
- [observed, P, insiders] The review adds that cycling is built into the idea of pulling the two sequences together and occurs very frequently in experiments ([S26] p. 4).
- [observed, S] **Boland, Eberhard, Engineer, Tsoukalas 2012** [S30], abstract:
  - FP is a discrete version of the proximal point algorithm.
  - Pump algorithms implicitly minimize a weighted mix of the objective and an integrality penalty with many local minima.
  - The random restarts are attempts to leave local minima that are not integral.
  - S2 snippet: in the original FP only the starting point biases the search toward good objective values, so random restarts risk leaving the good region.
- [observed, S] **De Santis, Lucidi, Rinaldi 2013** [S31]: FP is read as a Frank-Wolfe method on a nonsmooth concave merit function (abstract). A 2014 DAM paper generalizes the merit functions.
- [observed, P] **Geißler, Morsi, Schewe, Schmidt 2017** [S29]:
  - Despite FP's practical success, few works study its theory (arXiv p. 1).
  - The random perturbations are crucial in practice (p. 1).
  - None of the earlier FP papers they cite contains a theoretical result (p. 4).
  - They replace the random restarts by a penalty framework that keeps a convergence theory.
- [observed, P, insider co-author] **Dey, Iroume, Molinaro, Salvagnin 2018** [S28], arXiv v1:
  - FP's theory is very limited; they know of no bound on its expected running time (p. 2).
  - Remark 2.3 gives a counterexample: max x2 s.t. 3x1 + x2 = 3, x binary. Without restarts, the original pump alternates between the rounded point (1, 1), the LP point (2/3, 1) and, after the flip, (0, 1), forever, and never finds the feasible point (1, 0). The cause: the original randomization never flips a variable with zero fractionality (p. 3).
  - Appendix B gives a subset-sum instance that still stalls when zero-fractionality flips are allowed (p. 16).
  - Their WalkSAT-style randomization beat the FP 2.0 code for virtually all seeds and instances tested (p. 4).
  - [inferred] I re-derived the cycle by hand in this run (LP optimum (2/3, 1); the L1 projections of (1, 1) and of (0, 1) both return (2/3, 1)): the counterexample holds. Their text has a variable-name slip: it says only x2 is fractional, then flips the first coordinate; the fractional variable is x1.
- [observed, S] **Bonami, Kılınç, Linderoth 2012** [S34]: unlike FGL's procedure, the outer-approximation pump for convex MINLP cannot cycle, so it is exact: it finds a solution or proves that none exists (S2 context).
- [observed, P, insiders] The review's verdict on theory: the pump can fail to converge when the perturbation flips only fractional variables ([S26] p. 8); serious theoretical work started about ten years after the first paper (p. 11).
- [observed, S] Newer work still treats cycling and rounding cost as open.
  - Mexi, Berthold, Salvagnin 2023 [S35]: no variant had used information across iterations; all steered toward a single reference point (abstract).
  - Çördük et al. 2025 [S37]: on the GPU, projection and rounding often cycle (S2 context).
  - Liu, Lu, Mazumder 2026 [S36]: once the projection runs on the GPU, FP 2.0's propagation rounding takes a large share of each iteration (abstract).

### 2.3 Replications and implementations (CBC, SCIP, vendors)

- [observed, P] **Huang and Mehrotra** [S27] ran all pump computations with the FP of COIN-OR CBC 2.3 (preprint p. 10).
  - On MIPLIB 2003 their runs found no feasible solution for four of the six mixed-integer instances, worse than the FP papers, which report solutions for every instance.
  - They blame CBC-FP for not fully implementing the published algorithm: its enumeration stage solves sub-MIPs with a small branch-and-bound tree, where Bertacco et al. used CPLEX (p. 13). The published version's S2 contexts carry the same two sentences.
- [practice, observed, P] **Who wrote CBC's pump** [S38].
  - `src/CbcHeuristicFPump.cpp` (commit 6e7feefda2, 2026-10-23) carries a 2004 IBM copyright line.
  - Commit history (GitHub API): on the older path `Cbc/src/CbcHeuristicFPump.cpp` (2006-2020), 59 of 75 commits are by the author name John Forrest. On `src/` since 2020, 12 of 32 are by John Forrest and 4 by `jjhforrest`.
  - Class defaults include `maximumPasses_(100)`, `maximumRetries_(1)` and `initialWeight_(0.0)`. The code has an optional objective weight scaled by `initialWeight_ * sqrt(numberIntegers) / ||c||` and decayed by `weightFactor_(0.1)`.
  - [inferred] The Huang-Mehrotra shortfall describes the lp-team guest's implementation. That code includes an objective weight of the Achterberg-Berthold kind, off in the class defaults.
- [observed, P, insiders] **Details only in code.** The review says only a careful reading of the source code of Bertacco et al. shows the elaborate restart scheme: how far one variable is perturbed and how many variables are changed ([S26] p. 8). It then reconstructs domain-dependent perturbation sizes, a 10 % cap and a randomized rounding threshold. [inferred] Readers of the general-integer pump [S2] had to learn these mechanisms from the code.
- [observed, P] **SCIP (ZIB) at master 353584f2a4, 2026-11-08** [S39]. `heur_feaspump.c`:
  - names itself `objective feasibility pump 2.0` in `HEUR_DESC`;
  - runs by default (`HEUR_FREQ 20`) with full initial objective weight (`DEFAULT_ALPHA 1.0`);
  - keeps FP 2.0's round-and-propagate (`DEFAULT_USEFP20 FALSE`) and the local-branching stage 3 (`DEFAULT_STAGE3 FALSE`) off.
  - [inferred] SCIP ships the critic's version, the objective pump, and leaves Fischetti's own 2009 improvement off by default. His 2026 manuscript reports the same defaults from the code ([S24] p. 9); this run confirmed them independently at a later commit.
- [observed, P, insiders] Adoption: at least ten MIP solvers implement a pump: CBC, CPLEX, GLPK, Gurobi, MIPCL, Mosek, SAS, SCIP, Sulum and Symphony ([S26] p. 11).

### 2.4 Self-reported failures and limits [stated, P]

- Instance p2756 is called a pathological case for FP that CPLEX solves easily, which the authors blame on its many big-M coefficients ([S1] p. 9).
- FP failed on 3 of the 83 instances, CPLEX's root heuristics on 19 ([S1] p. 7).
- FP 2.0 calls the often poor quality of the earlier pumps' solutions a drawback ([S3] p. 5). Measured average gaps to the best known solution, over 10 seeds on successful runs: original pump 77.2 %, 57.6 % with propagation; objective pump 52.4 %, 35.5 % with propagation (pp. 16-17).

### 2.5 How it was answered

- **2009, adopt the critic's fix** [stated, P]: FP 2.0 calls the Achterberg-Berthold objective pump the state-of-the-art pump for good-quality solutions ([S3] p. 16) and tests its propagation rounding inside both pumps.
- **2014, work with the theorists** [practice, P]: Fischetti co-authored the follow-up with Boland, Eberhard, Engineer, Savelsbergh and Tsoukalas [S4], the group whose 2012 analysis recast the pump's restarts [S30].
- **2026, return to the 2005 prescription** [stated, P; unreviewed; attribution self-declared]:
  - The 2005 paper warned that, with the cutoff in place, rounded points often satisfy the original constraints but not the cutoff, and it prescribed an LP with the integer variables fixed to recover them ([S1] p. 11).
  - The 2026 manuscript says later work replaced the cutoff by objective weighting (Achterberg-Berthold), mentioned it only in passing, or dropped the objective; SCIP's pump keeps neither the cutoff nor the recovery ([S24] p. 2).
  - Result: adding the 2005 cutoff and recovery to SCIP's objective pump wins on 116 of 176 instances, loses on 9 and lowers the median final gap from 59 % to 30 % (p. 1). This comparison was added after the pre-declared design and is one of the two post hoc rows of Table 3 (p. 14).
  - His verdict: the 2005 paper had said so, and SCIP dropped both parts (p. 19). Verbatim: "Our recommendation is therefore not a new heuristic but an old one, restored." ([S24] p. 19). He also marks where the evidence stops: the completion's advantage at a shallow target is a lead, not an established result (p. 19).
- [inferred] The answer to Q1 took 21 years and came as a controlled experiment, not a reply. It moves the question from whether FP ignores the objective to whether implementers dropped half of the 2005 scheme. It does not answer the 2019 point that the 2005 variant was never compared with local-search heuristics.

---

## 3. Local branching (Q4)

- [observed, S] **Danna, Rothberg, Le Pape (ILOG) 2005** [S42].
  - Abstract (Springer page): on very difficult MIPs, RINS and guided dives both beat default CPLEX and local branching on several metrics: quality within a time limit, improving a given solution, and time to diversify.
  - S2 snippets: RINS improves on LB in several ways; the testbed included 20 of the 24 models of the LB paper.
  - Affiliations: ILOG (OpenAlex raw affiliations).
  - [inferred] The commercial developers' school answered an academic method on the academic's own instances, with a newer CPLEX.
- [observed, S] **Ghosh 2007, DINS** [S44]: DINS beat RINS and LB on a testbed that included all instances of the RINS and LB papers plus other hard ones (S2 context).
- [observed, S] **Hansen, Mladenović, Urošević 2006** [S43]: the VNS school's variable neighbourhood branching, built on LB. Their comparative results were not read; the S2 contexts are only descriptive.
- [observed, S, team member] **Achterberg's thesis** [S45]: Fischetti and Lodi were the first to solve sub-MIPs inside a MIP heuristic, though they saw LB as an incumbent-guided form of branching rather than as a heuristic (S2 context; the S2 record misattributes the thesis to R. Bixby).
- [observed, P] **Defaults in 2026.**
  - CPLEX 22.1.2: the local branching heuristic is off by default [S41].
  - SCIP master: the standalone `heur_localbranching.c` has `HEUR_FREQ -1`, off [S39]. **But** SCIP's ALNS (`HEUR_FREQ 20`) runs the local-branching neighbourhood by default (`DEFAULT_ACTIVE_LOCALBRANCHING TRUE`) [S39].
- [observed, P] **Hendel 2022 (ZIB/SCIP), the counter-evidence** [S46].
  - DINS and LB were two of the most successful auxiliary problems in his experiments, though both had been inactive in SCIP (p. 218).
  - DINS, LB and proximity were then switched on by default inside ALNS for the first time (p. 219).
  - LB and proximity both need an incumbent and binary variables (table, p. 195).
- [observed, S] **The ML-LNS school.**
  - Huang, Ferber, Tian, Dilkina, Steiner [S47]: LB is often slow because it solves an ILP as large as the input. Their LP relaxation of LB is claimed to pick neighbourhoods as good as LB's, faster (arXiv abstract), so LB's choice is the yardstick being approximated.
  - The same group [S48]: hand-crafted destroy heuristics, LB among them, are often either slow to find good subsets or find poor ones (S2 context).
- [observed, S] **Limits of applicability.**
  - Binary variables: Fischetti and Lodi 2008 say their repair method assumes 0-1 variables because its LB component does ([S6], S2 context) [stated].
  - Structure: LB was mainly applied to binary programs without special matrix structure (Altmanová, Knop, Koutecký 2019 [S49], S2 context).
- **How it was answered** [stated, P]: Liu, Fischetti and Lodi 2022 call the neighbourhood size critical. They say the original scheme started from a conservative value and that the best size depends strongly on the instance ([S7] arXiv v1, p. 1). [inferred] This revises the 2003 default 19 years later with a learned predictor; it does not engage the RINS comparison.

---

## 4. Proximity search (Q5)

- [stated, P] Trade-offs written into the 2014 paper ([S8] preprint, 31 July 2013):
  - Admitting there is no free lunch, they say that when a large improvement lies within a very small radius, LB gets it in one sub-MIP while proximity search needs a sequence of calls (p. 7).
  - Callback control may be unavailable in a given solver, or may switch off important solver features (p. 10).
  - A recentering variant was not tested because it needed a new parameter whose tuning could contaminate the results (pp. 10-11).
- [observed, P] **Rodrigues, Agra, Hvattum, Requejo 2021** [S50]: proximity search is promising and performs well when used, but applications remain scarce (p. 460). Their weighted Hamming distance beats classic proximity search in 75 % of the cases on p-median, set covering and stochastic lot-sizing instances (p. 459).
- [observed, P] SCIP: the standalone `heur_proximity.c` is off (`HEUR_FREQ -1`); the proximity neighbourhood runs inside ALNS by default (`DEFAULT_ACTIVE_PROXIMITY TRUE`) [S39]. Hendel finds that proximity and zero-objective show the largest gain in average reward as the fixing rate grows ([S46] p. 209).
- [inferred] Independent evidence on proximity search is thin and mostly favourable; the strongest stated weaknesses are the authors' own.

---

## 5. Benders: cut selection, in-out stabilization, UFL (Q6, Q7)

### 5.1 The 2010 cut-selection note

- [stated, P] The homepage preprints of the note ([S9]; titled after minimal infeasible subsystems):
  - Benders cuts often disappoint when simple design issues are underrated and the method is coded as in the textbook.
  - The classic approach picks feasibility cuts essentially at random (extended draft, revised Sept. 2009).
  - The extended draft's abstract also announces a proof that finding a violated optimality cut is strongly NP-hard when violated feasibility cuts exist. Whether the published 8-page note (Math. Program. 124:175-182) keeps that result was not checked.
- [observed, P] **Brandenberg and Stursberg (TU Munich) 2021** [S51].
  - The alternative-polyhedron view worked well empirically for FSZ, but it has fundamental issues (p. 385).
  - A cut from a vertex of the alternative polyhedron can fail even to support the epigraph, also when the vertex minimizes the all-ones objective that FSZ suggest (p. 386).
  - Scaling: the zero-one objective ignores row scaling, so rescaling one constraint can change the selected cut (p. 395).
  - Measured: their adaptive cuts reach any gap threshold 2-3 times faster than static cuts (p. 410). Static cuts are FSZ's approach, strengthened so that every cut is supporting (p. 408). Test bed: 14 power-system capacity-expansion instances, Gurobi 7.5, ten cores (p. 408).
  - Credit: FSZ's cut-generating LP is always feasible, though its cut may be weaker (p. 411). They also relay FSZ's own result that MIS-based selection beat the standard implementation by a factor of at least 2-3 (pp. 398-399).
- [observed, P; unrefereed] **Larsen, Cordeau, Frangioni, Frejinger 2026** [S52], 50 Benders variants on 153 Canad R MCFNDP instances.
  - The FSZ-based variants rank far behind the static Brandenberg-Stursberg and Hosseini-Turner cuts (p. 18).
  - On the literature, FSZ included: each study tends to crown its own, most elaborate cut, against a partial list of rivals on its own instance class (p. 3).
  - In FSZ's favour: direct branch-and-cut is fastest overall, and only FSZ and Glomb et al. 2026 had included it as a competitor, so the unified-cut literature may have underestimated its baseline (p. 3).
- [observed, S] Hosseini and Turner 2025 [S53], deepest cuts: one of the two leaders in [S52]; abstract only.
- **Answered?** [practice, P] No reply found. His 2025 Verolog slides shift the weight elsewhere.
  - Slow convergence is usually blamed on poor cuts, to be cured by cleverer selection such as Magnanti-Wong, but there is more to it ([S11] PDF p. 9).
  - Many implementations failed at the root cut loop (PDF p. 11).
  - Kelley's cut loop can be very slow, so stabilization is essential (PDF p. 14).
  - No slide in [S11] or [S12] names Brandenberg-Stursberg, Conforti-Wolsey or Hosseini-Turner (text search).

### 5.2 UFL Benders and in-out stabilization (2017)

- [stated, P] Credit is shared, not claimed: they built no real bundle method, only a simple in-out variant in the spirit of Applegate et al., Ben-Ameur and Neto, Fischetti and Salvagnin, and one further reference ([S10] preprint p. 12).
- [practice, P] Self-check against wrong cuts: a perturb-and-refix loop modelled on Margot's proposal found tolerance issues in earlier code versions (p. 16). On the 50 open Körkel-Ghosh instances, their upper bound was worse than the best known on 6, always by less than 0.04 % (p. 18).
- [observed, P] **Karapetyan and Goldengorin 2018** [S54] (arXiv v1).
  - FLS showed that many KG bounds could still be improved, but at significant computational effort (p. 3).
  - Their automatically composed metaheuristic improved 12 best-known upper bounds and matched all others (p. 15).
  - They call it about two orders of magnitude faster than FLS, with higher solution quality (p. 16).
  - Their own hardware caveat: FLS used four cores, a fourfold boost, and counting time units as equal favours FLS (p. 15).
  - [inferred] FLS aimed at exact solution and bounds; this critique measures only the heuristic side. No reply found.
- [practice, P] The same instance, gs250a-1, illustrates the in-out effect in 2016 ([S10] p. 13) and again in 2025 ([S11] PDF p. 13). [inferred] One showcase instance carried for a decade.

---

## 6. Robust optimization: cutting planes versus compact formulations (Q8)

- [observed, P] **Bertsimas, Dunning, Lubin (MIT) 2016** [S55], author manuscript.
  - Prior work: the only direct comparison they know, Fischetti-Monaci 2012, found cutting planes superior for robust LPs and reformulation superior for robust MIPs, without testing significance or trying cutting-plane variants (p. 2).
  - They replicate it on a larger instance set (p. 3).
  - Fischetti-Monaci seem to add cuts at every tree node, which they expect to be costly (p. 6).
  - They avoid skew-sensitive measures such as the arithmetic mean Fischetti-Monaci used (p. 11).
  - **Replicated:** for robust LPs, cutting planes were fastest on 76 % of the instances, matching the earlier observation (p. 12).
  - **Not replicated:** for robust MIPs, a slight edge for cutting planes contradicts the earlier finding that cutting planes were significantly worse. Possible causes they list: the larger test set, root-node cuts, the metric, or all three (p. 14).
  - Partial credit: the effect on infeasible instances was hinted at in 2012 but not explored (p. 15).
  - Abstract: for polyhedral sets neither method dominates, unlike earlier results (p. 1).
- [inferred] Bertsimas leads the Optimization Council (council-roundtable). The exchange is a ready-made cross-team disagreement on benchmarking practice: significance, summary means, cut placement.
- **Answered?** Fischetti-Monaci 2012 [S13] was not read, and no reply was found. The statement that [S13] found cutting planes significantly worse for robust MIPs is BDL's report and was not checked against [S13].

---

## 7. Erraticism, bet-and-run, backdoor branching (Q9)

- [stated, P] Fischetti and Monaci's working hypothesis: erraticism follows from the exponential nature of tree search, which amplifies small differences chaotically, so it is largely unavoidable ([S14] preprint p. 1). Their hybrid variant wastes some CPU time on every instance that needs more than the trial nodes (p. 10).
- [practice, P] The baseline was CPLEX 12.3 at default settings but without dynamic search, which the dummy callback disables (p. 6). [inferred] The gains are measured against a CPLEX with its proprietary dynamic search off. No critic raising this was found; proximity search used callbacks the same way (§4).
- [observed, S] **Confirmed:** Carvajal, Ahmed, Nemhauser, Furman, Goel, Shao 2014 [S56] confirm the earlier evidence that keeping the best of several differently configured solver runs can give large gains (S2 context).
- [observed, S] **Generalized, with a reservation.** Friedrich, Kötzing and Wagner 2017 [S57] made bet-and-run generic, using no problem knowledge and no tailoring to the algorithm (arXiv abstract). Lissovoi, Sudholt, Wagner and Zarges 2017 [S58] note that Fischetti and Monaci created diversity by reaching into CPLEX's internal mechanisms (S2 context).
- [observed, S; tension, not a rebuttal] Adegbindin, Dietrich, Pender, Lodi 2026 [S59]: variability is systematic and partly predictable from cheap early-run features, chiefly root degeneracy, matrix structure, coefficient ranges and presolve reductions (arXiv abstract). See C7.
- [observed, P] **Backdoor branching** (IPCO 2011; INFORMS JOC 2013 [S15]). Khalil, Vaezipoor and Dilkina 2022 [S60]:
  - The method collects many fractional vertices in arbitrary order, so it is unclear whether its information leads to backdoors at all, and it may exploit too aggressively (arXiv p. 2).
  - Because its set cover must cover every collected vertex, it may not return a backdoor of bounded size (p. 2).
  - In their tests, their reimplementation (p. 6) failed to return a size-8 backdoor on half of 142 instances (p. 8; the rest of that sentence is cut off in the extracted text).
  - No reply found.

---

## 8. Orbital shrinking (Q10)

- [stated, P] The 2011 preprint argues that symmetry is an asset to preserve and exploit, to be broken only as a last resort. The method yields a discrete relaxation whose solution bounds the optimum ([S16] p. 1).
- [stated, P] Own negative result: with the whole symmetry group, the bound is no better than the LP bound on 31 of 39 instances, and on the other 8 no better than CPLEX's root bound (p. 6).
- [practice, P] They then hand-picked a subgroup setting per instance and derived the automatic rule from those picks (an average ratio of 0.82), evaluated on the same instances (pp. 6, 9). [inferred] Tuning set and test set coincide; no critic raising it was found.
- [observed, S] Exactness needs extra structure. Knueven, Ostrowski and Watson 2018 [S61] give conditions under which orbital shrinking is exact for unit commitment (S2 context). Van Doornmalen and Hojny 2024 [S62] describe it as aggregation along orbits that yields a relaxation (S2 context).
- Answered [practice, S]: the 2017 theory paper with Salvagnin and Walsh [S17] (metadata only). Whether Pfetsch and Rehn's 2019 comparison [S74] tested orbital shrinking is unknown (Gaps).

---

## 9. MILP models of trained neural networks (Q11)

- [stated, P] Fischetti and Jo 2018 [S18]: small networks solve to proven optimality in seconds on a notebook, but larger, more realistic ones can take too long. Their examples, networks with six and eight hidden layers, need an hour or more (preprint p. 14).
- [observed, P] Anderson, Huchette, Ma, Tjandraatmadja, Vielma 2020 [S63]: the MIP models of trained networks they list, Fischetti-Jo among them, mostly use big-M formulations. Even for a single neuron these are neither ideal nor an exact convex relaxation (arXiv v4 p. 5). The critique targets the formulation class, not F&J alone.
- [observed, S] Khalil, Gupta, Dilkina 2018 [S64] attribute the MILP's difficulty mainly to its weak LP relaxation and credit that observation to Fischetti and Jo (S2 context). Grimstad and Andersson 2019 [S65]: such formulations yield very hard MIP instances (S2 context).

---

## 10. Bilevel: general-purpose solver versus problem-specific methods (Q12)

- [stated, P] FLMS 2017 claims MIX++ consistently, often by a large margin, outperforms state-of-the-art MIBLP methods, including methods that exploit problem-specific information ([S19] preprint p. 1).
- [practice, P] Part of the evidence compares against published numbers from other machines (pp. 22-23):
  - Xu and Wang's times, on a 2.4 GHz desktop that FLMS estimate to be 2 to 5 times slower than theirs;
  - Tang et al.'s best results, obtained on a 3.30 GHz PC with CPLEX 12.5.
- [observed, S, insiders] Later problem-specific methods beat MIX++ on their own classes (all three are S2 contexts; Sinnl and Ljubić are Fischetti's bilevel co-authors):
  - Tanınmış and Sinnl 2022 [S68], submodular interdiction: MIX++ solves no instance within an hour, average gap 93.5 %, against below 1 % for their method.
  - Furini, Ljubić, Martin and San Segundo 2019 [S69], clique interdiction: their approach beats the general-purpose bilevel solver by several orders of magnitude.
  - Cerulli, Serra, Sorgente, Archetti and Ljubić 2023 [S70], collapsed k-core: their problem-specific methods beat it.
- [observed, S] Applicability. The interdiction algorithm of Fischetti et al. 2019 [S20] needs down-monotonicity. Tanınmış, Aras and Altınel 2022 [S67] say this restricts its applicability, since important applications such as misinformation-spread minimization violate it (S2 context).
- [stated, P] The 2017 solver's main cut classes need its Assumption 1, integrality of Ax + By − b on high-point-relaxation solutions, with hypercube cuts as the fallback ([S19] pp. 4, 7).
- [observed, P] MibS (Ralphs group) [S66]:
  - It reuses 21 of the FLMS instances, the IBLP-FIS set (arXiv p. 29).
  - It notes that the FLMS intersection cuts can cut off a bilevel-infeasible point, but not with a guarantee when the point also lies outside the relaxation's feasible set (p. 20).
  - It defers testing the cut classes to future work (p. 29).
  - No head-to-head result with MIX++ was found in the parts read.

---

## 11. Steiner trees (DIMACS 2014) and later records (Q13)

- [observed, P] Rehfeldt, Koch and Maher 2019 [S71] (preprint) name the solver of Fischetti et al. [S22] as the other empirically strong prize-collecting solver besides SCIP-Jack (PDF p. 2). With their new reductions, SCIP-Jack solves all eight ACTMOD instances at least three times faster than any Challenge participant. On the 20 JMPALMK instances it beats every participant on 15 and loses on one (PDF p. 28). The comparison is against Challenge records in the Challenge environment, not a rerun of Fischetti et al.'s code. [inferred] Records superseded by a rival school's reductions; not a dispute.

---

## 12. Fischetti as commentator; published exchanges

- [practice, S] The only published comment of his found: on Lodi and Zarpellon's survey of learning and branching, TOP 25(2):237-238, 2017 [S23], with a rejoinder by Lodi and Zarpellon, TOP 25(2):247-248 [S72]. Both are closed and **not read**. Other commentators in the same issue: Louveaux; Dilkina, Khalil and Nemhauser (Crossref).
- [stated, P] He criticizes textbook practice in his own papers: textbook Benders (§5.1) and, in 2026, implementers' black-box use of an objective cutoff (§2.5).
- No erratum, corrigendum, retraction, reply or rejoinder appears among the 190 works OpenAlex links to his ORCID [S76]. Crossref author queries mix in Massimo V. Fischetti and are not conclusive.

---

## 13. How Fischetti handles critique (pattern for Phase 2)

1. **Names the drawback himself, first** [stated, P]:
   - cycling (2005) and the p2756 failure (2005);
   - stalling and poor quality (2009);
   - the LB-versus-proximity trade-off (2014);
   - relaxation-only orbital shrinking (2011);
   - the DNN model's scale limit (2018).
2. **Adopts the critic's fix as the new baseline** instead of defending the old one: the objective pump in FP 2.0 (2009) [S3].
3. **Co-authors with the people who analysed or improved his method** [practice]:
   - the Boland group (2014) [S4];
   - his former student Salvagnin co-authors the WalkSAT critique of his randomization (2018) [S28];
   - Lodi and Salvagnin co-author the review that calls the 2005 cutoff results only mildly positive (2019) [S26].
4. **Revisits his own defaults years later with new tools**: the LB neighbourhood size learned (2022) [S7]; the 2005 cutoff and recovery restored and measured (2026) [S24].
5. **In 2026, builds the critique into the design** [stated, P]: comparisons declared in advance, Holm correction, post hoc rows labelled, every solution revalidated, raw logs public, AI-run internal adversarial reviews before submission ([S24] pp. 14, 19, 25).
6. **Shifts the frame instead of replying**: in 2025 he moves Benders' slow convergence from cut quality to the cut loop, with stabilization as the remedy [S11].
7. **No published reply found** to Danna et al. (2005), Dey et al.'s counterexample (2018), Bertsimas-Dunning-Lubin (2016), Karapetyan-Goldengorin (2018), Anderson et al. (2020), Brandenberg-Stursberg (2021) or Khalil et al. (2022).

---

## 14. Relay checks and slips found in this run [inferred unless stated]

- Dey et al. say FP found feasible solutions on 96.3 % of MIPLIB 2003 instances ([S28] p. 2). FGL 2005 tested 83 instances, only 44 of them from MIPLIB 2003, and failed on 3 ([S1] pp. 5-7); 80/83 is 96.4 %. The testbed description is imprecise; the percentage is a truncation.
- The 2026 manuscript renders FGL's recovery condition with variable bounds (l ≤ x ≤ u) that the 2005 author preprint does not show; the preprint states the system Ax ≤ b ([S24] p. 2 versus [S1] p. 11). The published 2005 text was not checked.
- The S2 record of Achterberg's thesis lists R. Bixby as its author [S45].
- Karapetyan and Goldengorin's arXiv v1 has unresolved citation keys ("[?]") where it compares with FLS ([S54] pp. 15-16).

---

## Contradictions (kept, not reconciled)

- **C1. FP solution quality.**
  - 2005: competitive with CPLEX in speed and in the quality of the first solution ([S1] p. 1).
  - 2005, same paper: no particular attention paid to solution quality (p. 10).
  - 2009: the earlier pumps' solutions are often of poor quality ([S3] p. 5).
  - 2009, with Glover: FP cannot compete with CPLEX for optimal or near-optimal solutions ([S32], S2).
  - 2026 vendor docs: generally poor-quality solutions ([S40], boilerplate shared with two other heuristics).
  - The 2005 claim concerns the first solution against root heuristics; the others concern final quality.
- **C2. Which objective device is right.**
  - 2009: the objective pump is the state of the art for good solutions ([S3] p. 16).
  - 2019, insiders: the 2005 cutoff results were only mildly positive, without comparisons ([S26] p. 4).
  - 2026: SCIP's objective pump without the 2005 cutoff and recovery leaves 116 of 176 instances improvable (post hoc), and the 2005 scheme should be restored ([S24] pp. 1, 19).
- **C3. Local branching's worth.**
  - Beaten by RINS and guided dives on very difficult models ([S42], 2005) and by DINS ([S44], 2007).
  - Often slow as an LNS selector ([S47], 2023).
  - Off by default as a standalone heuristic in CPLEX and SCIP ([S41], [S39]).
  - One of the two most successful neighbourhoods in SCIP's ALNS, and on by default there ([S46] p. 218; [S39]).
  - Different roles (full scheme, sub-MIP neighbourhood with limits, reference neighbourhood for ML-guided LNS) and solver generations.
- **C4. Robust LP/MIP.** Fischetti-Monaci 2012, as BDL report it: cutting planes superior for robust LPs, reformulation superior for robust MIPs. BDL 2016: the robust-LP result replicated, the robust-MIP result contradicted, neither method dominant for polyhedral sets ([S55] pp. 1, 2, 12, 14).
- **C5. General-purpose bilevel claim.** MIX++ claimed to beat even problem-specific methods ([S19] p. 1), against later problem-specific methods that beat it by orders of magnitude or on classes where it solves nothing ([S68], [S69], [S70]).
- **C6. Benders cut selection.**
  - FSZ: MIS-based selection beats the standard by a factor of at least 2-3 (relayed in [S51] pp. 398-399).
  - Adaptive cuts beat a strengthened FSZ by 2-3 times on power systems ([S51] p. 410).
  - FSZ-based variants rank far behind on MCFNDP, while direct branch-and-cut is fastest overall and FSZ was one of only two studies to test it ([S52] pp. 3, 18; unrefereed).
- **C7. Variability: chaos or structure.** Largely unavoidable, a chaotic amplification by tree search ([S14] p. 1), against systematic and partly predictable from cheap early-run features ([S59] abstract, 2026). Not a direct exchange; both claims can hold.
- **C8. Symmetry as asset versus bound quality.** Symmetry is to be preserved ([S16] p. 1), yet the whole-group relaxation is no better than the LP bound on 31 of 39 instances (p. 6).
- **C9. Attribution of the 2026 study.** Self-declared in CITATION.cff and DataCite; a new account with one repository; no homepage link found in this run (note 03 reports a ResearchGate link from the homepage). The content is treated as his [stated], with this caveat attached.

---

## Gaps

- **Achterberg-Berthold 2007 not read** (ScienceDirect 403; ZIB OPUS bot check not bypassed). Their claims are known only through FP 2.0 and the 2019 review, both by insiders.
- **Closed or unreached texts:**
  - Danna-Rothberg-Le Pape 2005: abstract and S2 snippets only; the snippet naming the CPLEX version is truncated.
  - Hansen-Mladenović-Urošević 2006; Ghosh 2007; Boland et al. 2012; De Santis et al. 2013 and 2014.
  - Fischetti-Monaci 2012: BDL's characterization unverified.
  - Lodi-Tramontani 2013 (INFORMS 403). A search-engine summary said it cites a Fischetti-Monaci talk as an example of misread benchmarks: **unverified lead**.
  - Pfetsch-Rehn 2019: whether it tests orbital shrinking is unknown.
  - The TOP 2017 comment and the Lodi-Zarpellon rejoinder.
  - The published versions of the FP, LB and Benders-note papers: author preprints read instead. The LB preprint uses Type 3 fonts and could not be extracted.
- **Leads dropped for lack of a verifiable venue:**
  - a 2015 PhD thesis by Amin Dehghanian (S2 CorpusId 152533251), which reports that even a state-of-the-art FSZ-style Benders implementation was ineffective for its kidney-exchange game;
  - a Cacchiani-Hemmelmayr WU working paper, which says RINS and LB do not extend easily to branch-and-price;
  - Rekik-Cordeau-Soumis 2008, which relays that reference [10] (unidentified) beat a slightly different LB implementation and CPLEX 8.
- **No outside critique found** of: self-splitting (2014, 2018); random sampling (2016); the lexicographic pure cutting-plane work (2011); the first Chvátal closure work (2007), beyond general remarks on the cost of MIP-based separation; light robustness. The early TSP, ATSP, GTSP and crew-scheduling work was not searched (about five minutes without leads, then moved on).
- **No public referee reports, rejected papers or retractions** were found. Errata were checked only through OpenAlex's ORCID-linked list (190 works) and through noisy Crossref author queries.
- **Not verified:** the 2026 manuscript's claim that SCIP's pump never tests the rounded point; only the defaults were checked here. Whether CbcSolver overrides the defaults of CBC's FP class was not checked.
- **Vendor-internal evaluations** of FP and LB (CPLEX, Gurobi, Xpress) were not found beyond parameter documentation.

---

## Sources

One line each: title, author(s), date, identifier or URL, primary (by Fischetti or co-signed) or secondary, and what was read. Identifiers were checked with Crossref, arXiv, Unpaywall, OpenAlex, DataCite or the GitHub API in this run. Page numbers in the text refer to the version named here.

1. [S1] "The feasibility pump", M. Fischetti, F. Glover, A. Lodi, Mathematical Programming 104(1):91-104, 2005, DOI 10.1007/s10107-004-0570-3; author preprint "Revised version" (dei.unipd.it/~fisch/papers/feasibility_pump.pdf) read pp. 1-12 (primary)
2. [S2] "A feasibility pump heuristic for general mixed-integer problems", L. Bertacco, M. Fischetti, A. Lodi, Discrete Optimization 4(1):63-76, 2007, DOI 10.1016/j.disopt.2006.10.001; metadata only, not read (primary)
3. [S3] "Feasibility pump 2.0", M. Fischetti, D. Salvagnin, Mathematical Programming Computation 1(2-3):201-222, 2009, DOI 10.1007/s12532-009-0007-3; preprint (26 Oct 2008, rev. 8 May 2009) read pp. 1-2, 5, 13, 16-17, 20 (primary)
4. [S4] "Boosting the feasibility pump", N. L. Boland, A. C. Eberhard, F. G. Engineer, M. Fischetti, M. W. P. Savelsbergh, A. Tsoukalas, Mathematical Programming Computation 6(3):255-279, 2014, DOI 10.1007/s12532-014-0068-9; preprint read pp. 1-2 (primary)
5. [S5] "Local branching", M. Fischetti, A. Lodi, Mathematical Programming 98(1-3):23-47, 2003, DOI 10.1007/s10107-003-0395-5; metadata only (homepage PDF not text-extractable) (primary)
6. [S6] "Repairing MIP infeasibility through local branching", M. Fischetti, A. Lodi, Computers & Operations Research 35(5):1436-1445, 2008, DOI 10.1016/j.cor.2006.08.004; S2 context only (primary)
7. [S7] "Learning to Search in Local Branching", D. Liu, M. Fischetti, A. Lodi, AAAI 36(4):3796-3803, 2022, DOI 10.1609/aaai.v36i4.20294; arXiv 2112.02195v1 read p. 1 (v2 retitled "Revisiting local branching with a machine learning lens") (primary)
8. [S8] "Proximity search for 0-1 mixed-integer convex programming", M. Fischetti, M. Monaci, Journal of Heuristics 20(6):709-731, 2014, DOI 10.1007/s10732-014-9266-x; preprint (31 Jul 2013) read pp. 1-2, 7, 10-12, 21, 24 (primary)
9. [S9] "A note on the selection of Benders' cuts", M. Fischetti, D. Salvagnin, A. Zanette, Mathematical Programming 124(1-2):175-182, 2010, DOI 10.1007/s10107-010-0365-7; homepage preprints "Minimal Infeasible Subsystems and Benders cuts" (MIS_for_Benders.pdf) and its extended draft (revised Sept. 2009) read abstracts and p. 10 (primary)
10. [S10] "Redesigning Benders Decomposition for Large-Scale Facility Location", M. Fischetti, I. Ljubić, M. Sinnl, Management Science 63(7):2146-2162, 2017, DOI 10.1287/mnsc.2016.2461; preprint (11 Feb 2016) read pp. 1, 11-13, 16, 18 (primary)
11. [S11] Verolog 2025 lecture, part 3 [Benders], M. Fischetti, Trento, 13 June 2025, dei.unipd.it/~fisch/papers/slides/ ("2025 Verolog - Fischetti part 3 [Benders].pdf"); all 14 PDF pages read (primary)
12. [S12] AIROyoung 2026 lecture, part 1 [BC + Benders], M. Fischetti, file dated 2026-02-08 in the slides directory; 19 pages text-searched (primary)
13. [S13] "Cutting plane versus compact formulations for uncertain (integer) linear programs", M. Fischetti, M. Monaci, Mathematical Programming Computation 4(3):239-273, 2012, DOI 10.1007/s12532-012-0039-y; not read (closed) (primary)
14. [S14] "Exploiting Erraticism in Search", M. Fischetti, M. Monaci, Operations Research 62(1):114-122, 2014, DOI 10.1287/opre.2013.1231; preprint OPRE-2012-05-278(R) (25 May 2012, rev. 21 Mar 2013) read pp. 1, 3, 6-7, 10 (primary)
15. [S15] "Backdoor Branching", M. Fischetti, M. Monaci, IPCO 2011, LNCS pp. 183-191, DOI 10.1007/978-3-642-20807-2_15; and INFORMS Journal on Computing 25(4):693-700, 2013, DOI 10.1287/ijoc.1120.0531; metadata only (primary)
16. [S16] "Orbital Shrinking", M. Fischetti, L. Liberti, ISCO 2012, LNCS pp. 48-58, DOI 10.1007/978-3-642-32147-4_6; preprint (12 Jul 2011) read pp. 1, 4-6, 9 (primary)
17. [S17] "Orbital shrinking: Theory and applications", M. Fischetti, L. Liberti, D. Salvagnin, T. Walsh, Discrete Applied Mathematics 222:109-123, 2017, DOI 10.1016/j.dam.2017.01.015; metadata only (primary)
18. [S18] "Deep neural networks and mixed integer linear optimization", M. Fischetti, J. Jo, Constraints 23(3):296-309, 2018, DOI 10.1007/s10601-018-9285-6; preprint read pp. 1-2, 5, 11-14 (primary)
19. [S19] "A New General-Purpose Algorithm for Mixed-Integer Bilevel Linear Programs", M. Fischetti, I. Ljubić, M. Monaci, M. Sinnl, Operations Research 65(6):1615-1637, 2017, DOI 10.1287/opre.2017.1650; preprint read pp. 1-5, 7, 13, 22-23 (primary)
20. [S20] "Interdiction Games and Monotonicity, with Application to Knapsack Problems", M. Fischetti, I. Ljubić, M. Monaci, M. Sinnl, INFORMS Journal on Computing 31(2):390-410, 2019, DOI 10.1287/ijoc.2018.0831; metadata only (primary)
21. [S21] "On the use of intersection cuts for bilevel optimization", M. Fischetti, I. Ljubić, M. Monaci, M. Sinnl, Mathematical Programming 172:77-103, 2018, DOI 10.1007/s10107-017-1189-5; metadata only (primary)
22. [S22] "Thinning out Steiner trees: a node-based model for uniform edge costs", M. Fischetti, M. Leitner, I. Ljubić, M. Luipersbeck, M. Monaci, M. Resch, D. Salvagnin, M. Sinnl, Mathematical Programming Computation 9:203-229, 2017, DOI 10.1007/s12532-016-0111-0; metadata only (primary)
23. [S23] "Comments on: On learning and branching: a survey", M. Fischetti, TOP 25(2):237-238, 2017, DOI 10.1007/s11750-017-0449-0; not read (closed) (primary)
24. [S24] "Feasibility Pump with Objective Cutoff: A Computational Study", M. Fischetti (self-declared), manuscript, September 2026, submitted to Mathematical Programming Computation per README, unreviewed; github.com/mfischetti-arch/fp-objective-cutoff at commit 52544adb82 (2026-09-17); Zenodo DOIs 10.5281/zenodo.22810777 (code, MIT, version mpc-submission-1) and 10.5281/zenodo.22810848 (raw SCIP logs, CC BY 4.0), both checked on DataCite; manuscript read pp. 1-3, 8-9, 13-14, 19, 25; README and CITATION.cff read (primary)
25. [S25] "Improving the feasibility pump", T. Achterberg, T. Berthold (ZIB), Discrete Optimization 4(1):77-86, 2007, DOI 10.1016/j.disopt.2006.10.004; not read (HTTP 403; bot wall), claims via S3 and S26 (secondary)
26. [S26] "Ten years of feasibility pump, and counting", T. Berthold, A. Lodi, D. Salvagnin, EURO Journal on Computational Optimization 7(1):1-14, 2019, DOI 10.1007/s13675-018-0109-7; preprint dated 20 Feb 2018 (Padova IRIS, hdl 11577/3339187) read in full (secondary; insiders)
27. [S27] "An empirical evaluation of walk-and-round heuristics for mixed integer linear programs", K.-L. Huang, S. Mehrotra, Computational Optimization and Applications 55(3):545-570, 2013, DOI 10.1007/s10589-013-9540-0; Optimization Online preprint 2010/09/2734 read pp. 1, 9-13, 22 (secondary)
28. [S28] "Improving the Randomization Step in Feasibility Pump", S. S. Dey, A. Iroume, M. Molinaro, D. Salvagnin, SIAM Journal on Optimization 28(1):355-378, 2018, DOI 10.1137/16M1095962; arXiv 1609.08121v1 read pp. 1-4, 16 (secondary; Salvagnin an insider)
29. [S29] "Penalty Alternating Direction Methods for Mixed-Integer Optimization: A New View on Feasibility Pumps", B. Geißler, A. Morsi, L. Schewe, M. Schmidt, SIAM Journal on Optimization 27(3):1611-1636, 2017, DOI 10.1137/16M1069687; arXiv 1707.09891v1 read pp. 1-4 (secondary)
30. [S30] "A New Approach to the Feasibility Pump in Mixed Integer Programming", N. Boland, A. Eberhard, F. Engineer, A. Tsoukalas, SIAM Journal on Optimization 22(3):831-861, 2012, DOI 10.1137/110823596; abstract (OpenAlex) and S2 context (secondary)
31. [S31] "A New Class of Functions for Measuring Solution Integrality in the Feasibility Pump Approach", M. De Santis, S. Lucidi, F. Rinaldi, SIAM Journal on Optimization 23(3):1575-1606, 2013, DOI 10.1137/110855351, abstract; and "Feasibility Pump-like heuristics for mixed integer problems", same authors, Discrete Applied Mathematics 165:152-167, 2014, DOI 10.1016/j.dam.2013.06.018, metadata (secondary)
32. [S32] "A note on xQx as a modelling and solution framework for the Linear Ordering Problem", M. Lewis, B. Alidaee, F. Glover, G. Kochenberger, International Journal of Operational Research 5(2):152, 2009, DOI 10.1504/IJOR.2009.025005; S2 context (secondary; Glover an insider)
33. [S33] "Fix-and-relax approaches for controlled tabular adjustment", D. Baena, J. Castro, J. A. González, Computers & Operations Research 58:41-52, 2015, DOI 10.1016/j.cor.2014.11.018; S2 context (secondary)
34. [S34] "Algorithms and Software for Convex Mixed Integer Nonlinear Programs", P. Bonami, M. Kılınç, J. Linderoth, IMA Volumes in Mathematics and its Applications, pp. 1-39, 2012, DOI 10.1007/978-1-4614-1927-3_1; S2 context (secondary)
35. [S35] "Using multiple reference vectors and objective scaling in the Feasibility Pump", G. Mexi, T. Berthold, D. Salvagnin, EURO Journal on Computational Optimization 11:100066, 2023, DOI 10.1016/j.ejco.2023.100066; abstract (secondary)
36. [S36] "PDFP: GPU-Accelerated Feasibility Pump via PDHG", R. Liu, H. Lu, R. Mazumder, arXiv 2611.03629v1, 2 Nov 2026; abstract (secondary)
37. [S37] "GPU-Accelerated Primal Heuristics for Mixed Integer Programming", A. Çördük, P. Sielski, A. Boucher, K. Aatish, arXiv 2510.20499v2, 2025; S2 context (secondary)
38. [S38] COIN-OR CBC, src/CbcHeuristicFPump.cpp at commit 6e7feefda2 (2026-10-23), github.com/coin-or/Cbc; constructor defaults and objective scaling read; commit authorship via the GitHub API for Cbc/src (2006-2020) and src/ (since 2020) (secondary; code)
39. [S39] SCIP at master commit 353584f2a4 (2026-11-08), github.com/scipopt/scip: src/scip/heur_feaspump.c, heur_localbranching.c, heur_proximity.c, heur_rins.c, heur_alns.c, #define lines read (secondary; code)
40. [S40] Gurobi Optimizer Parameter Reference (current), docs.gurobi.com/projects/optimizer/en/current/reference/parameters.html, entries PumpPasses, ZeroObjNodes, MinRelNodes, fetched 2026-11-08 (secondary; vendor documentation)
41. [S41] IBM ILOG CPLEX 22.1.2 documentation, local branching heuristic and feasibility pump switch parameter pages, ibm.com/docs/en/icos/22.1.2, fetched 2026-11-08 with WebFetch (secondary; vendor documentation; wording as returned by the tool)
42. [S42] "Exploring relaxation induced neighborhoods to improve MIP solutions", E. Danna, E. Rothberg, C. Le Pape (ILOG), Mathematical Programming 102(1):71-90, 2005, DOI 10.1007/s10107-004-0518-7; abstract (Springer page) and S2 contexts (secondary)
43. [S43] "Variable neighborhood search and local branching", P. Hansen, N. Mladenović, D. Urošević, Computers & Operations Research 33(10):3034-3045, 2006, DOI 10.1016/j.cor.2005.02.033; S2 context only (secondary)
44. [S44] "DINS, a MIP Improvement Heuristic", S. Ghosh, IPCO 2007, LNCS pp. 310-323, DOI 10.1007/978-3-540-72792-7_24; S2 context (secondary)
45. [S45] "Constraint Integer Programming", T. Achterberg, PhD thesis, TU Berlin, 2007 (S2 record dated 2008, author field wrong); S2 context only (secondary; team member)
46. [S46] "Adaptive large neighborhood search for mixed integer programming", G. Hendel, Mathematical Programming Computation 14(2):185-221, 2022, DOI 10.1007/s12532-021-00209-7 (open access); read pp. 185, 195, 209-210, 218-219 (secondary)
47. [S47] "Local Branching Relaxation Heuristics for Integer Linear Programs", T. Huang, A. Ferber, Y. Tian, B. Dilkina, B. Steiner, LNCS pp. 96-113, 2023, DOI 10.1007/978-3-031-33271-5_7; arXiv 2212.08183 abstract (secondary)
48. [S48] "Searching Large Neighborhoods for Integer Linear Programs with Contrastive Learning", T. Huang, A. Ferber, Y. Tian, B. Dilkina, B. Steiner, arXiv 2302.01578v1, 2023; abstract and S2 context (secondary)
49. [S49] "Evaluating and Tuning n-fold Integer Programming", K. Altmanová, D. Knop, M. Koutecký, ACM Journal of Experimental Algorithmics 24:1-22, 2019, DOI 10.1145/3330137; S2 context (secondary)
50. [S50] "Weighted proximity search", F. Rodrigues, A. Agra, L. M. Hvattum, C. Requejo, Journal of Heuristics 27(3):459-496, 2021, DOI 10.1007/s10732-021-09466-0 (open access); read pp. 459-460 (secondary)
51. [S51] "Refined cut selection for benders decomposition: applied to network capacity expansion problems", R. Brandenberg, P. Stursberg (TU Munich), Mathematical Methods of Operations Research 94(3):383-412, 2021, DOI 10.1007/s00186-021-00756-8 (open access; arXiv 1906.05583); read pp. 383-386, 393-395, 398-399, 407-411 (secondary)
52. [S52] "Empirical Comparison of Unified Benders Cuts for Multi-Commodity Fixed-Charge Network Design", E. Larsen, J.-F. Cordeau, A. Frangioni, E. Frejinger, arXiv 2607.07899v1, 8 Jul 2026, unrefereed; read pp. 2-3, 18, 20 (secondary)
53. [S53] "Deepest Cuts for Benders Decomposition", M. Hosseini, J. Turner, Operations Research 73:2591-2609, 2025, DOI 10.1287/opre.2021.0503; abstract (secondary)
54. [S54] "Conditional Markov Chain Search for the Simple Plant Location Problem Improves Upper Bounds on Twelve Körkel-Ghosh Instances", D. Karapetyan, B. Goldengorin, Springer Optimization and Its Applications, pp. 123-147, 2018, DOI 10.1007/978-3-319-94830-0_7; arXiv 1711.06347v1 read pp. 1, 3, 15-16 (secondary)
55. [S55] "Reformulation versus cutting-planes for robust optimization", D. Bertsimas, I. Dunning, M. Lubin (MIT), Computational Management Science 13(2):195-217, 2016, DOI 10.1007/s10287-015-0236-z; MIT author manuscript (DSpace handle 1721.1/103105) read pp. 1-3, 6, 11-15 (secondary)
56. [S56] "Using diversification, communication and parallelism to solve mixed-integer linear programs", R. Carvajal, S. Ahmed, G. Nemhauser, K. Furman, V. Goel, Y. Shao, Operations Research Letters 42(2):186-189, 2014, DOI 10.1016/j.orl.2013.12.012; S2 context (secondary)
57. [S57] "A Generic Bet-and-Run Strategy for Speeding Up Stochastic Local Search", T. Friedrich, T. Kötzing, M. Wagner, AAAI 31(1), 2017, DOI 10.1609/aaai.v31i1.10645; arXiv 1609.03993v1 abstract (secondary)
58. [S58] "Theoretical results on bet-and-run as an initialisation strategy", A. Lissovoi, D. Sudholt, M. Wagner, C. Zarges, GECCO 2017, pp. 857-864, DOI 10.1145/3071178.3071329; S2 context (secondary)
59. [S59] "When Solvers Get Moody: Quantifying and Predicting Performance Variability in Mixed Integer Programming", M. Adegbindin, B. Dietrich, J. Pender, A. Lodi, arXiv 2610.12876v1, 9 Oct 2026; abstract (secondary)
60. [S60] "Finding Backdoors to Integer Programs: A Monte Carlo Tree Search Framework", E. B. Khalil, P. Vaezipoor, B. Dilkina, AAAI 36(4):3786-3795, 2022, DOI 10.1609/aaai.v36i4.20293; arXiv 2110.08423 read pp. 1-2, 6, 8-9 (secondary)
61. [S61] "Exploiting Identical Generators in Unit Commitment", B. Knueven, J. Ostrowski, J.-P. Watson, IEEE Transactions on Power Systems 33(4):4496-4507, 2018, DOI 10.1109/TPWRS.2017.2783850; S2 context (secondary)
62. [S62] "A unified framework for symmetry handling", J. van Doornmalen, C. Hojny, Mathematical Programming 212:217-271, 2025 (online 2024), DOI 10.1007/s10107-024-02102-2; S2 context (secondary)
63. [S63] "Strong mixed-integer programming formulations for trained neural networks", R. Anderson, J. Huchette, W. Ma, C. Tjandraatmadja, J. P. Vielma, Mathematical Programming 183(1-2):3-39, 2020, DOI 10.1007/s10107-020-01474-5; arXiv 1811.01988v4 read p. 5 (secondary)
64. [S64] "Combinatorial Attacks on Binarized Neural Networks", E. B. Khalil, A. Gupta, B. Dilkina, arXiv 1810.03538v1, 2018; S2 context (secondary)
65. [S65] "ReLU networks as surrogate models in mixed-integer linear programs", B. Grimstad, H. Andersson, Computers & Chemical Engineering 131:106580, 2019, DOI 10.1016/j.compchemeng.2019.106580; S2 context (secondary)
66. [S66] "A branch-and-cut algorithm for mixed integer bilevel linear optimization problems and its implementation", S. Tahernejad, T. K. Ralphs, S. T. DeNegre, Mathematical Programming Computation 12(4):529-568, 2020, DOI 10.1007/s12532-020-00183-6; arXiv 2104.09010 read pp. 8, 20, 29 (secondary)
67. [S67] "Improved x-space algorithm for min-max bilevel problems with an application to misinformation spread in social networks", K. Tanınmış, N. Aras, İ. K. Altınel, European Journal of Operational Research 297:40-52, 2022, DOI 10.1016/j.ejor.2021.05.008; S2 context (secondary)
68. [S68] "A Branch-and-Cut Algorithm for Submodular Interdiction Games", K. Tanınmış, M. Sinnl, INFORMS Journal on Computing 34:2634-2657, 2022, DOI 10.1287/ijoc.2022.1196; S2 context (secondary; Sinnl an insider)
69. [S69] "The maximum clique interdiction problem", F. Furini, I. Ljubić, S. Martin, P. San Segundo, European Journal of Operational Research 277:112-127, 2019, DOI 10.1016/j.ejor.2019.02.028; S2 context (secondary; Ljubić an insider)
70. [S70] "Mathematical programming formulations for the Collapsed k-Core Problem", M. Cerulli, D. Serra, C. Sorgente, C. Archetti, I. Ljubić, European Journal of Operational Research 311:56-72, 2023, DOI 10.1016/j.ejor.2023.04.038; S2 context (secondary; Ljubić an insider)
71. [S71] "Reduction techniques for the prize collecting Steiner tree problem and the maximum-weight connected subgraph problem", D. Rehfeldt, T. Koch, S. J. Maher, Networks 73(2):206-233, 2019, DOI 10.1002/net.21857; Lancaster eprint 129080 preprint read PDF pp. 1-2, 27-28 (secondary)
72. [S72] "On learning and branching: a survey", A. Lodi, G. Zarpellon, TOP 25(2):207-236, 2017, DOI 10.1007/s11750-017-0451-6, and "Rejoinder on: On learning and branching: a survey", TOP 25(2):247-248, DOI 10.1007/s11750-017-0452-5; metadata only (secondary)
73. [S73] "Performance Variability in Mixed-Integer Programming", A. Lodi, A. Tramontani, in Theory Driven by Influential Applications (INFORMS TutORials in Operations Research), pp. 1-12, 2013, DOI 10.1287/educ.2013.0112 (Crossref-checked); not reached (HTTP 403) (secondary)
74. [S74] "A computational comparison of symmetry handling methods for mixed integer programs", M. E. Pfetsch, T. Rehn, Mathematical Programming Computation 11:37-93, 2019, DOI 10.1007/s12532-018-0140-y; S2 context only, not read (secondary)
75. [S75] Semantic Scholar Graph API citation contexts, fetched 2026-11-08, for S1, S3, S5, S8, S9, S10, S13, S14, S15 (journal), S16, S17, S18, S19, S22, "SelfSplit parallelization for mixed-integer linear programming" (Computers & Operations Research 93:101-112, 2018, DOI 10.1016/j.cor.2018.01.011), "Lexicography and degeneracy: can a pure cutting plane algorithm work?" (Mathematical Programming 130:153-176, 2011, DOI 10.1007/s10107-009-0335-0) and "Optimizing over the first Chvátal closure" (Mathematical Programming 110:3-20, 2007, DOI 10.1007/s10107-006-0054-8). The random-sampling follow-up "Improving branch-and-cut performance by random sampling" (M. Fischetti, A. Lodi, M. Monaci, D. Salvagnin, A. Tramontani, Mathematical Programming Computation 8:113-132, 2016, DOI 10.1007/s12532-015-0096-0) appears in them (secondary; tool data)
76. [S76] OpenAlex works filtered by ORCID 0000-0001-6601-0568 (190 works), fetched 2026-11-08, titles screened for errata, comments and replies (secondary; tool data)
