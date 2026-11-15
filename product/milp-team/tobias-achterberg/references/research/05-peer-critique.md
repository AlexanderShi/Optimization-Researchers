# Tobias Achterberg: Peer Critique (blind spots, limits, contested judgements)

| Field | Value |
|---|---|
| Researcher | Tobias Achterberg. Original author of SCIP and of the thesis *Constraint Integer Programming* (TU Berlin 2007). Joined ILOG CPLEX development in September or October 2006 (by his own account, [S59] 0:38:30); left IBM for Gurobi in 2014 (the podcast host's statement, not contradicted, [S59] 0:42:30); Gurobi VP of R&D as listed in November 2025 (team.json). Living. DBLP 71/6632, ORCID 0000-0002-0862-7065 |
| Dimension | Research agent 05 of 06: peer critique. Replications and re-measurements, published objections, counterexamples, rival methods and schools, benchmark studies that compare his methods with others, judgements later revised, and whether and how each was answered |
| Research date | 2026-11-08 |
| Sources consulted | 59 (15 primary: his own or co-signed texts, slides, records, a caption transcript and the SCIP code; 44 secondary), listed under "Sources" |
| WebSearch calls | 5 (of 5 allowed) |
| User-supplied material | None. `references/sources/{papers,essays,software,publications}/` hold only `.gitkeep`; `RESOURCES.md` is the template. `talks/` holds one caption excerpt saved during this run by a sibling research agent (04), not by the user; it is cited here as [S59] (caption). `private/` was not opened. **Nothing in this file is from user-supplied material** |
| Transcripts saved | None by this agent |
| Language | English (team.json) |

**Tags.**
- [stated]: said or written by Achterberg, or in a paper, report, thesis or deck he authored or co-signed. Caption transcripts are flagged "(caption)": speech recognition, not speaker-checked.
- [practice]: what his papers, code or records show was done, including SCIP source files that name him as an author.
- [observed]: what a third party wrote or measured. Relationship flags: (successor) = SCIP developer at ZIB building on his code; (co-author) = has published with him; (colleague) = same employer at the time; (team) = member of a skill team in this repository.
- [inferred]: my reading. The basis is given; do not quote it as anyone's view.
- (P) primary reading: read in the source's own text at the page, slide or timestamp cited. (S) secondary: abstract only, metadata only, a relay by another author, a search-result summary, or a Semantic Scholar citation context ("S2 context; full text not read").

**How the critiques were found.**
1. Verified his main works with Crossref (10 DOIs) and listed his works through OpenAlex by ORCID (42 records) [S15].
2. Read the Achterberg-side texts that critics target:
   - the thesis (DepositOnce copy as page images; the ZIB copy as text);
   - the ZIB-Report preprints of the 2005 branching paper, the 2007 conflict-analysis and feasibility-pump papers, the 2008 report on minor formulation changes and the 2016 presolve report;
   - the SEA 2022 deck, MIPLIB 2017, and the 2023 *Subject to* interview (caption excerpt).

   The ZIB OPUS landing pages sit behind an Anubis proof-of-work bot check, but the direct `/files/` links recorded in sibling research notes of this run return the PDFs without any challenge; nothing was bypassed. Journal versions (ScienceDirect, Springer, INFORMS) were not read.
3. Found critics through:
   - Semantic Scholar citation contexts for the SCIP paper (1,000 citing records) and hybrid branching (111) [S58]; the other six works hit HTTP 429;
   - the critics' related-work sections and reference lists;
   - arXiv title searches;
   - the SCIP CHANGELOG and source, which show what his successors changed in his code [S14];
   - five WebSearch calls.
4. Read each critic in a legal open copy where one exists (arXiv, DepositOnce, the Padova and Bologna repositories, Springer open access, Dagstuhl, GitHub, Zenodo). Otherwise I used the abstract from the publisher page, Crossref, OpenAlex or a university repository.
5. Not reached, and not routed around:
   - the AAAI proceedings site (bot check);
   - ScienceDirect (HTTP 403) and the INFORMS PDF of Lodi-Tramontani (HTTP 403);
   - the Aussois 2018 slides (redirect to a host with a self-signed certificate; not bypassed);
   - Fischetti's Padova host (unreachable);
   - Semantic Scholar (rate-limited);
   - the ZIB-Report versions of Hendel 2015 and Berthold 2013 (no direct file link known; a guessed path returned 404).

**Attribution caveats that must survive into the skill.**
- **SCIP code is group work.** In SCIP master (commit 353584f, 8 Nov 2026):
  - `branch_relpscost.c` names Achterberg, Berthold, Gamrath, Mexi, Pfetsch and Patel;
  - `conflict_graphanalysis.c` names Achterberg, Berthold, Heinz, Pfetsch, Winkler and Witzig;
  - `heur_feaspump.c` names only Berthold and Salvagnin, so a critique of SCIP's feasibility pump targets the objective-pump *method* he co-authored, not his code;
  - `treemodel.c` (Anderson, Le Bodic), `event_estim.c` (Hendel) and `conflict_dualproofanalysis.c` (Berthold, Witzig, Borst) are his successors' work [practice, P; S14].
- **Gurobi code is closed.** Statements about Gurobi internals come from his own deck and interview ([S12], [S59]), from a co-signed report ([S9], 2016 version), or from third parties ([S32], [S57]). None of them is a reading of the code.
- **Most critics are successors or collaborators.**
  - Berthold co-authored hybrid branching and the objective feasibility pump, then moved to FICO.
  - Gamrath, Hendel, Witzig and Mexi are ZIB SCIP developers.
  - Heinz was a Gurobi employee when [S32] appeared (its conflict-of-interest note, p. 782).
  - Danna worked in ILOG CPLEX R&D in 2008, while he worked at ILOG [S40].
  - Three critics sit in this repository: Fischetti and Gleixner (milp-team) and Dey (minlp-team).

  Read most of this file as a dialogue inside one lineage, not as an outside school's attack.

---

## 0. Summary for Phase 2

| # | Critique (blind spot / limit) | Raised by | Achterberg-side answer | Status |
|---|---|---|---|---|
| Q1 | Strong branching's small trees come mostly from side effects (domain reductions, cutoffs), so node counts overstate the quality of its decisions | Gamrath-Schubert 2018 [S17]; Gamrath 2020 [S16] (successor) | He had named the confounder (thesis pp. 69-70) and bounded part of it (2004 report, p. 9), without measuring the domain-reduction part. No reply to the measurement | Replicated and refined; the design stands |
| Q2 | Reliability is a fixed count of observations and ignores pseudocost variance | Hendel 2015 [S18] (successor) | None from him; his own 2007 change made the threshold dynamic. Hendel's tests entered SCIP 3.2, off by default | Absorbed as options, not defaults |
| Q3 | The product score is an empirical choice without theory and not uniformly better than the linear score | Le Bodic-Nemhauser 2017 [S19]; Anderson-Le Bodic-Morgan 2020 [S20]; Shah-Dey 2025 [S22] (team: Dey) | None. The SCIP default is still product; the tree-model rule ships with SCIP since 7.0 but is off | Gains confined to large trees |
| Q4 | Worst cases: strong branching can need exponentially larger trees; branching only on fractional variables is a structural limit | Dey-Dubey-Molinaro-Shah 2023 [S21] (team: Dey) | Indirect: his 2022 deck says worst-case bounds say nothing about practical instances [S12] | Open in theory; within a factor of two of the optimal tree on the tested classes |
| Q5 | One LP optimum carries too little information under dual degeneracy | Berthold-Salvagnin 2013 [S23]; Berthold-Gamrath-Salvagnin 2019 [S25]; Gamrath-Berthold-Salvagnin 2020 [S24]; Fischetti-Monaci 2012 [S26] (team: Fischetti) | Practice, relayed: PumpReduce (MIP 2010 talk, patent) and a 2018 Aussois talk on degeneracy in Gurobi (neither read) | Absorbed: degeneracy-aware hybrid branching is SCIP default since 7.0 |
| Q6 | Hand-tuned, input-agnostic rules tuned for average performance on heterogeneous test beds | Khalil et al. 2016 [S27]; Lodi-Zarpellon 2017 [S29]; Gasse et al. 2019 [S28] | Yes, in the 2023 interview (caption): his own 2000 learning experiment collapsed onto one feature, which became reliability branching; he prefers explainable ML that yields rules implemented by hand [S59] | Open; ML wins are on generated families with altered solver settings |
| Q7 | Graph-based conflict analysis reasons with clauses (resolution), weaker than cut-based reasoning; complemented by dual proofs | Witzig-Berthold-Heinz 2017, 2021 [S31, S32]; Mexi et al. 2023, 2024-25 [S33, S34] (team: Gleixner) | In 2005 he reported that it slowed feasible MIPs by 15% and named better LP-conflict heuristics and clause-database management as future work [S3]. Gurobi's reliance on dual proofs is relayed by [S32] but not found in the 2016 presolve report | Extended; graph analysis is still SCIP default and the fallback of the cut-based method |
| Q8 | Restart only after the root | Anderson-Hendel-Le Bodic-Viernickel 2019 [S36] (successors) | He posed the open question himself: delayed restarts need different criteria (thesis p. 163) | His open question, answered by successors; in-tree restarts in SCIP since 7.0, uncapped in 11.0 |
| Q9 | Objective-weighted feasibility pump: lower success rate, more iterations; SCIP's version never tests the rounded point and has no cutoff | Berthold-Lodi-Salvagnin 2019 [S37] (co-author); Fischetti 2026, unreviewed [S38] (team) | None. His 2005 report compared only against the pump without an objective cutoff | Open |
| Q10 | Benchmark method: performance variability, descriptive statistics only, knock-out attributions confounded by interaction, time-limit censoring, heuristics measured by time to optimality | Danna 2008 [S40] (colleague); Lodi-Tramontani 2013 [S41]; Fischetti-Monaci 2014 [S42]; Koch et al. 2022 [S43]; Berthold 2013 [S44] | His 2008 report documented factor-1000 swings from minor formulation changes [S13]. Gurobi tests about 6,000 models with five seeds when the cluster is free (caption, [S59]) | Partly answered in practice; no published reply |
| Q11 | MIPLIB 2003 was hand-picked, with benchmark instances still unsolved 15 years later | MIPLIB 2017 paper [S11], co-signed by him | Collective self-revision: data-driven, solvable-only benchmark set | Conceded collectively |
| Q12 | SCIP is almost competitive with commercial MIP solvers | Danna 2008 [S40]; Song et al. 2020 [S54] | His caveat: CPLEX was SCIP's LP solver in the comparison (thesis p. 377). In 2023 he argued that academic work should be judged against its base solver, not against commercial codes [S59] | Contradiction C1 |
| Q13 | Floating-point MIP solving without certificates can return wrong answers; presolve correctness is not certifiable in general | Cook et al. 2013 [S47]; Cheung-Gleixner-Steffy 2017 [S48]; Eifler-Gleixner 2022 [S49]; Hoen et al. 2024 [S50] (team: Gleixner); user reports [S52, S53] | His 2016 presolve report excludes models on which solver versions disagree; in 2023 he advised improving the model's numerics before tuning [S9, S59] | Open; exact solving built by others inside SCIP |
| Q14 | Cut selection by fixed weighted-sum scores set by grid search; no theory for parallelism or cut counts | Turner-Koch-Serrano-Winkler 2023 [S55]; Dey-Molinaro 2018 [S56] (team: Dey) | He warns that cuts that look strong often fail to speed up the solve (caption, [S59]); he helped Dey-Molinaro with their manuscript | Open |

---

## 1. Era and resource context

- **ZIB, to 2007.**
  - 2000-2001: a computer-science diploma project to learn branching with machine learning inside Alexander Martin's solver SIP ([S1] p. ix; [S59] 0:23:30-0:26:00, caption).
  - SCIP was started from scratch because SIP's LP-centred data structures could not take the CP integration (thesis p. ix; [S59] 0:27:00-0:28:30); then almost two years without publishing.
  - Thesis experiments: more than one CPU year, 244 instances times 115 settings, 28,060 runs ([S1] p. 2).
  - The 2004 branching study ran on an 833 MHz Alpha workstation, with SIP calling CPLEX 9.0 as LP solver ([S2] report p. 8).
- **ILOG and IBM (CPLEX).** At CPLEX he first ported reliability branching and conflict analysis, then worked on cuts, MIR and presolve ([S59] 0:40:00-0:42:00, caption). With Wunderling he measured CPLEX 8.0 to 12.5 on 2,928 models (relayed by [S43] p. 4).
- **Gurobi.**
  - The 2016 presolve report used 3,182 models, Gurobi 6.5, a single 4-core i7 machine and a 3,600 s limit ([S9] report pp. 2-3).
  - His 2022 deck reports 2,397 LP and 7,030 MIP instances, Gurobi 9.5.0, a 10,000 s limit ([S12] slide 5).
  - In 2023 he described 192 machines testing around the clock, about 6,000 MIP instances, and five random seeds when the cluster is free ([S59] 0:52:00, 1:05:00-1:06:00, caption).
  - In his estimate, about 10% of the work is research and 90% software design, bug fixing, benchmarking and tweaking ([S59] 0:52:30-0:53:30, caption).
- **The critics' context.**
  - SCIP successors work with open code and public sets (MMMC, MIPLIB 2017).
  - Theory critics use abstract tree models, or instances small enough that optimal trees can be computed by a 3^O(n) dynamic program ([S21] p. 4).
  - ML critics train on generated families and change solver settings (root-only cuts, restarts off) ([S28] p. 6).
  - Fischetti 2026 runs a patched SCIP snapshot and Gurobi 13.0.3 ([S38] README).
- [inferred] After about 2007 his evidence is private (vendor test sets, closed code), while his critics' evidence is public. Public critique therefore mostly targets his ZIB-era methods as they live on in SCIP, not what he builds now.

---

## 2. Branching (Q1-Q6)

### 2.1 Achterberg-side claims that critics target [stated, P]

**2004 report** ([S2], ZIB-Report 04-13; journal version not read).
- p. 4-5: full strong branching picks the locally best variable and works very well in node counts; most other rules can be read as fast estimates of what full strong branching measures.
- p. 8: benchmarking branching is hard because cuts, heuristics and node selection interact. They chose **not** to install optimal values beforehand, because leading quickly to feasible solutions is a desirable property of a branching rule.
- p. 8: the test set is the MIPLIB 2003 instances, plus some from another source, on which CPLEX 9.0 needs at least 5,000 nodes and at most one hour. Runs use cut-and-branch (cuts only at the root).
- p. 9: the geometric mean is treated as the common-sense fair criterion. Most-infeasible branching is about as good as random branching.
- pp. 10-12: reliability branching beats hybrid strong/pseudocost branching in time for every setting. Performance rises up to η_rel = 8 and then falls; (η_rel = 8, λ = 4) is the new sweet spot.
- p. 12: a gap to full strong branching's node counts remains; whether it can be closed without much more time per node is left open.

**Thesis** ([S1]).
- p. 2: impact is measured by knock-out, as the slowdown in the geometric mean when a default feature is switched off.
- p. 3:
  - a hybrid of reliability and inference branching beats pseudocost branching with strong-branching initialization by 8%, by more than 50% on feasibility problems;
  - most-infeasible branching is barely better than random;
  - the product score beats the linear score by 14%, even against the best of five weights.
- pp. 69-70: full and plain strong branching need by far the fewest nodes. **One reason he names is that strong-branching sub-LPs sometimes detect infeasibility and tighten a bound, which is not counted as a node**; he still reads the results as showing that the local greedy rule builds small trees.
- The thesis made η_rel dynamic ([S16] p. 22). SCIP now keeps η_rel between 1 and 5, adjusted dynamically, with λ = 9 ([S16] p. 22; [S14] `branch_relpscost.c` lines 83-93).

**Origin of reliability branching** ([S59] 0:23:30-0:26:00, caption). He extracted node features in SIP and trained support vector machines, neural networks, radial basis functions and other learners to predict branching gains. The learners pointed to one feature only, a pseudocost-like quantity of his own that he called the history value, and that feature, not the learning, became the 2005 paper.

### 2.2 Replication and re-measurement: tree size versus decision quality (Q1) [observed, P; successor]

**Gamrath's thesis, chapter 2** ([S16] pp. 57-59), developed with Schubert (OR Proceedings version [S17], abstract only).
- **Setup** (pp. 57-58): SCIP 4.0 with SoPlex 3.0; 153 MMMC instances solved by all rules and not at the root; 8 h limit; optimal value installed as cutoff; primal heuristics off.
- **Replication** (p. 58): full strong branching shrinks the tree 15-fold against pseudocost branching, in line with Achterberg et al. 2005.
- **Correction** (p. 58): most of that reduction comes from side effects. Domain reductions average 2.6 times the node count and cutoffs 41% of it. The fair node number is more than six times the reported count (1,250.9 against 192.7). Better decisions alone cut the tree by 59% against pseudocost branching; side effects cut it by a further 84%.
- **Reliability and hybrid branching** (pp. 58-59, Table 2.1).
  - Reliability branching reports almost five times as many nodes as full strong branching (945.6) but needs only 34% more fair nodes (1,678.7).
  - Hybrid branching is the fastest rule (33.1 s, against 36.8 for reliability, 44.1 for pseudocost, 78.7 for full strong, 132.2 for most infeasible), with a fair node number 20.5% above full strong branching.
- **Conclusion** (p. 59): strong branching matters for early decisions; later use of pseudocosts and history costs little decision quality and simply produces fewer side effects.

**How this meets his own text.**
- The 2004 footnote 3 ([S2] p. 9) counted only fathomed strong-branching children. It put the saving at about a factor of one half in nodes for full strong branching, and negligible for other rules.
- In Gamrath's data, cutoffs are indeed small for reliability branching (2% of nodes). The domain reductions the footnote did not count still put its fair node number at 1.78 times the reported count (my arithmetic from Table 2.1).
- The thesis named the bound-tightening effect but did not measure it (pp. 69-70).
- **Answer:** none from him.

[inferred] The study supports his design (spend strong branching early, while pseudocosts are uninitialized). It also largely dissolves his 2004 open question: much of the remaining node gap to full strong branching was side effects, not worse decisions. Node counts are not a clean measure of branching quality, which applies to every node-ranked table in the 2004 report and the thesis. The two studies also disagree on method: the 2004 report deliberately did not install optimal values, while Gamrath did (contradiction C11).

### 2.3 Reliability as a count (Q2) [observed, S; successor]
- **Hendel 2015** ([S18], abstract): thresholds built on fixed counts can produce poor decisions when objective gains vary strongly. Two statistical notions:
  - the relative error of a pseudocost confidence interval, which directs extra strong branching to high-variance variables;
  - a two-sample t-test that filters out candidates unlikely to beat the best history candidate.

  Both are implemented in SCIP.
- **SCIP practice** [practice, P; S14].
  - SCIP 3.2.0 added relative-error reliability, the hypothesis test, a confidence level and a skip of poor initialization candidates (CHANGELOG lines 5540-5549); SCIP 8.0.0 fixed the t-test variance (line 3019).
  - Current defaults (`branch_relpscost.c` lines 102-110): relative-error reliability FALSE, hypothesis test FALSE, skip of poor initialization candidates TRUE.
- **Answer:** none from him.
- [inferred] His count-based reliability with the 2007 dynamic threshold remains the default. The statistical refinements survive as opt-in options, except the candidate skip, whose origin in Hendel's paper is not confirmed here.
- **Patel 2024** ([S30], abstract, preprint): discounted pseudocosts with a forward-looking term. The SCIP 10.0.0 notes add discount-factor parameters for ancestral pseudocosts (CHANGELOG line 1003); whether they are active by default was not checked.

### 2.4 Scoring the two children: the product function (Q3) [observed]

**Le Bodic-Nemhauser** ([S19], arXiv v3, P pp. 3-5, 27-29).
- p. 4 (relay): he reported that moving from the linear to the product function cut time by 14% and nodes by 34%.
- p. 5: both functions were established experimentally, and no theory favours one over the other. The product prefers balanced gains, and some instance types favour the linear function, so the product does not systematically win. Example: gains (10, 10) and (2, 50) get equal scores, yet their tree sizes differ with the gap.
- pp. 27-29: their ratio and svts scores in SCIP 3.1.1 are slightly better on the MIPLIB 2010 benchmark set and clearly better on its 52-instance tree set. That run used a 12 h limit and 10 permutations each, about 19 CPU-months.

**Anderson-Le Bodic-Morgan** ([S20], arXiv v2, P p. 17).
- On the whole MIPLIB 2017 benchmark set, svts is only 1% faster in geometric mean and ratio is 1-2% slower.
- On instances needing at least 50,000 nodes, svts is 11% faster.

**SCIP defaults** [practice, P; S14].
- The score function default is still `p`, the product (`set.c` line 85).
- The tree-model rule has existed since SCIP 7.0.0 (CHANGELOG 3572, 3736) and is off by default (`treemodel.c` line 72).

**Shah-Dey 2025** ([S22], abstract, preprint; team: Dey).
- Full-strong-branching scores can overestimate the global bound gain when pruning is possible, and are myopic.
- Their modified scores cut mean tree size on solved MIPLIB 2017 benchmark instances by 22-35% for full strong branching and by 5-13% for reliability branching, depending on primal bound quality.
- [inferred] The pruning point echoes his own 2004 decision not to install optimal values.

**Answer:** none found. [inferred] The critique is about theoretical grounding and a subset of instances; on broad test sets the product default has held in SCIP for about 19 years.

### 2.5 Worst-case limits of strong and fractional branching (Q4) [observed, P; team: Dey]

Dey-Dubey-Molinaro-Shah ([S21], arXiv v2 pp. 1-5; Math. Program. 205:303-336, Crossref issue year 2023).
- p. 3: the small-tree property of strong branching is an experimental fact credited to [S2]; most ML branching work imitates it.
- p. 4, positive: for vertex cover, strong branching provably works well. There is a tree-size bound in terms of the additive gap, it recursively applies Nemhauser-Trotter fixing, and on one instance not using it costs exponentially more nodes.
- p. 4, negative: there is a class where the strong-branching tree is exponentially larger than another tree. Any rule that branches only on fractional variables shares the blow-up; the small tree branches on variables that are integral in the LP solution.
- p. 4, computational: on lot sizing, packing and covering IPs, chance-constrained IPs and vertex cover, the strong-branching tree stays within a factor of two of the optimal tree. The analysis uses his product score (p. 5).

**Answer:** none.
- **His stance** [stated, P; S12 slides 20-21]: exponential worst-case run time says nothing about practical instances, so algorithms should be designed for practical instances, with safeguards in the code against worst cases.
- [inferred] That stance anticipates this critique but does not meet its structural point, which binds reliability branching too.

### 2.6 One LP optimum and dual degeneracy (Q5)
- **Berthold-Salvagnin 2013** ([S23], abstract; co-author): standard rules branch on variables fractional in a single LP optimum. A cloud of alternative optima extends strong, pseudocost and hybrid branching; applied to full strong branching, it cuts mean running time by up to 30%.
- **Berthold-Gamrath-Salvagnin 2019** ([S25], ZIB-Report 19-17, abstract read): cloud modifications speed up full strong branching by more than 10%. Exploiting degeneracy improves the state-of-the-art hybrid branching rule and cuts solving time on affected instances by almost 20% on average.
- **Gamrath-Berthold-Salvagnin 2020** ([S24], P pp. 244, 246, 259; CC BY):
  - p. 246: they used reliability branching as the state-of-the-art rule found, in variants, in many solvers.
  - p. 259: dual degeneracy is common. Under high degeneracy many candidates are integral in alternative optima, which makes them poor branching candidates. Their measure has already been used to improve SCIP's hybrid branching.
- **SCIP practice** [practice, P; S14]: SCIP 7.0.0 added degeneracy-based weights and skips strong branching at very high degeneracy (CHANGELOG 3246-3247, 3656). The default is 1, i.e. active after the root (`branch_relpscost.c` line 120).
- **Achterberg side, relayed** [S, not read]:
  - [S24] p. 244 cites his pump-reduce procedure (US patent 8463729, 2013). It builds an LP solution with fewer fractional values and uses both solutions to select cuts. [S24] p. 244 also cites an Aussois 2018 talk on exploiting degeneracy in Gurobi.
  - [S37] p. 5 credits the procedure to Achterberg and Gu (MIP 2010 talk; patent application US20110131167).
  - Dey and Molinaro cite both talks on collecting cuts from several bases of the optimal face ([S56] p. 8).
- **Fischetti-Monaci 2012** ([S26], abstract via the Bologna repository; team: Fischetti): heuristics to speed up strong branching and shrink the candidate set. Even a proof-of-concept is reported faster than state-of-the-art strategies. Full text not read.
- **Adegbindin-Dietrich-Pender 2026** ([S46], abstract, preprint): the LP state handed to the tree acts as an initial condition. Steering among alternative states cut the shifted geometric mean node count on a 130-instance MIPLIB 2017 set from 2,574.7 to 1,198.0.
- [inferred] This is the critique he visibly took up in his own industrial practice (per the relays), while his successors absorbed it into SCIP. Status: answered in practice.

### 2.7 The learning school (Q6)
- **Khalil et al. 2016** ([S27], abstract; Le Bodic and Nemhauser co-authors): branching strategies are designed through cycles of parameter tuning and offline experiments on very heterogeneous test beds, judged by average performance. They then ignore the input instance. Khalil et al. learn an instance-specific surrogate of strong branching.
- **Lodi-Zarpellon 2017** ([S29], abstract): for lack of deep mathematical understanding, the branching literature rests on computational studies and heuristic, often problem-specific rules.
- **Gasse et al. 2019** ([S28], P pp. 6, 8):
  - The baseline is reliability pseudocost branching, a variant of hybrid branching and SCIP's default. The setup is SCIP 6.0.1, a 1 h limit, cuts only at the root, restarts off (p. 6).
  - Their GCNN beats it in time in almost every configuration. On maximum independent set, however, every ML method solves fewer instances than the default rule (p. 8).
- **His answer** [stated, P, caption; S59].
  - He tried exactly this program in 2000-2001: node features fed to several learners. It collapsed onto one feature, which became reliability branching (0:23:30-0:26:00).
  - In 2023 he favours explainable ML, such as decision trees, used offline to find rules that become defaults and are then implemented from scratch. His example is the choice whether to dualize an LP and which simplex to use (1:16:00-1:17:30).
  - He describes default-setting as heavy tuning: try an idea, often see it fail, try the opposite, keep what the test set shows, without always knowing why. He calls it an engineering task more than science (1:05:00-1:06:00).
- [inferred] Khalil's description of how rules are made matches his own account; the disagreement is about whether a learned policy should run inside the solver. His rule stays the yardstick these papers must beat, under non-default solver settings and on generated families rather than MIPLIB.

### 2.8 What SCIP kept (code evidence for Q1-Q6) [practice, P; S14]
- **Kept from him:** the product score; count-based reliability with a dynamic threshold; hybrid-branching history scores (conflict weight 0.01, inference 0.0001, cutoff 0.0001, pseudocost 1.0; `branch_relpscost.c` lines 75-82).
- **On by default, added after the thesis:**
  - degeneracy-aware weights (SCIP 7.0, by successors);
  - the skip of poor initialization candidates (SCIP 3.2);
  - dynamic score weights (who added them, and when, was not checked).
- **Added but off by default:** Hendel's relative-error reliability and t-test, the tree model (ratio and svts), symmetry-based candidate filtering.
- **Gurobi practice** [stated, caption; S59 0:55:00-0:56:00]: he implemented a successor's idea in Gurobi. Mark Turner's Gomory-cut-violation branching criterion helped performance a little and was announced for the next Gurobi release, with a joint paper planned.

---

## 3. Conflict analysis (Q7)

### 3.1 Achterberg side [stated, P]

**2005 report** ([S3], ZIB-Report 05-19; journal version not read).
- Abstract: on feasible MIPs conflict analysis cut nodes by 50% in geometric mean, but total time rose by 15%. On infeasible chip-verification MIPs it cut nodes by 90% and time by 60%.
- p. 2: further enhancements are needed for an overall speed-up on feasible instances.
- p. 16: the node savings bought a 10% saving in basic solution time, but the cost of the analysis (solving LPs to optimality) and longer switching times outweighed it.
- p. 18 (future work): faster heuristics for deriving conflicts from infeasible LPs, and better management of large numbers of conflict clauses, following SAT clause-database work.

**Thesis** ([S1]).
- p. 5: by 2007, more than 10% speed-up at reasonable effort.
- p. 179, design choice: conflicts with non-binary variables are kept as non-linear bound-disjunction constraints. Conflicts are never separated as cuts, not even pure binary ones; they are used only for propagation.

**Origin** ([S59] 0:30:30-0:32:30, caption): he learned SAT conflict analysis from Yakov Novikov during the chip-verification project and generalized it to MIP.

### 3.2 Witzig-Berthold-Heinz 2017 ([S31], P, arXiv PDF pp. 4-10; successors)
- PDF p. 7: SCIP managed conflicts by aging, borrowed from SAT and CP. MIP differs: propagation is not the expensive part, and node selection jumps across the tree.
- PDF p. 9: with conflict analysis (the then SCIP default) as baseline, dual-ray analysis alone is worse. The combination gives 3% (MIPLIB 2010 benchmark) and 18% (a conflict-prone set) less time, and 5% and 25% fewer nodes.
- PDF p. 10: a conflict pool on top of aging made hardly any difference. [inferred] This is a test of his own 2005 future-work item (clause management), with a null result.

### 3.3 Witzig-Berthold-Heinz 2021 ([S32], P pp. 755, 757, 773, 776, 778, 782)
- p. 755: they follow his concepts and notation.
- p. 757: his strategy (conflicts for all unique implication points along the path, keeping the promising ones) beat using only the last-level point that SAT practice favours.
- p. 776, results:
  - all LP-infeasibility analyses beat none; combined beats conflict graph, which beats none;
  - dual proofs alone barely change time (6.2% fewer nodes);
  - success rates: combined 83%, dual proof 67%, conflict graph 34% (strict size limit);
  - on 24 infeasible instances conflict-graph analysis beats dual proofs; on feasibility instances the graph gains 10.9% and the combination 24.5%.
- p. 776, Gurobi: they contrast their dual-proof result with the presolve paper [S9], where dual proofs reportedly cut time by 6% on affected instances. They attribute the gap to test sets and to a Gurobi implementation tuned to rely solely on dual-proof analysis. **A text search of the 2016 ZIB-Report version of [S9] finds no mention of dual proofs or conflict analysis; the journal version was not read. The claim about Gurobi stays unconfirmed.**
- p. 778: FICO Xpress uses the combination by default. p. 782: conflict-of-interest note (Berthold FICO; Heinz Gurobi, formerly FICO; Witzig ZIB).

### 3.4 Mexi et al. 2023 [S33] and 2024-25 [S34] [observed, P; team: Gleixner co-author]
- [S34] p. 2: graph-based conflict analysis, as introduced in MIP by [S3], works on clauses extracted from the linear constraints, in effect the resolution proof system, which is weak. Cut-based (pseudo-Boolean) analysis is exponentially stronger in principle.
- p. 18: for general integer variables his conflicts are bound disjunctions that no single linear inequality expresses, so solvers use them only for propagation. This is the design choice of thesis p. 179, now read as a limitation.
- p. 19: their cut-based method falls back to his graph-based analysis in about 19% of calls on MIPLIB 2017.
- pp. 20-21: in isolation, cut-based variants solve eight more instances at comparable time, and their conflicts propagate more (nw04: 864 against 26 bound changes).
- Abstract: as an addition to SCIP's default, the method improves time, node count and instances solved. The 2023 paper ([S33], abstract) finds the MIR-based variant better than the clause-based method on 0-1 programs.
- SCIP practice [practice, P; S14]: SCIP 10.0.0 added generalized-resolution conflict analysis, off by default (`set.c` line 119; CHANGELOG line 1026). The defaults analyse infeasible and bound-exceeding LPs with both conflict graph and dual ray (`set.c` lines 120-124).

### 3.5 A learning rival from CP [observed, S]
- **Berthold-Feydy-Stuckey 2010** ([S35], abstract): a heuristic CP search at the root learns nogoods, bound changes, solutions and branching statistics for the later IP search. It complements, rather than replaces, his analysis of infeasible subproblems.

### 3.6 Answer and status
- He published his method's 2005 weakness himself and named the fixes; successors then tested them (pools, dual proofs) and added stronger reasoning (cuts).
- [inferred] Its weakness is proof strength; its strength is generality (general integers, arbitrary propagators), which is why it remains SCIP's default and the fallback of the newer method.

---

## 4. Restarts (Q8)
- **Thesis** [stated, P; S1 pp. 4, 160, 163].
  - p. 160: he doubted that extensive SAT-style restarts help MIP, because discarding the tree throws away the stored LP warm-start bases. He restarts only after the root, when enough fixings have been found; restarts add almost 10% (p. 4).
  - p. 163: in-tree restarts triggered when 10% or 5% of the integer variables were globally fixed were inferior. Such fixings come late, when the search is nearly done. To make good use of delayed restarts, different criteria for applying them would have to be invented.
- **Anderson-Hendel-Le Bodic-Viernickel 2019** ([S36], abstract via Crossref; successors): online tree-size estimation drives a clairvoyant restart rule. It outperforms a state-of-the-art solver on public benchmark instances and is implemented in SCIP.
- **SCIP practice** [practice, P; S14].
  - SCIP 7.0.0 enabled an in-tree restart when the estimated remaining tree is large (CHANGELOG 3416; its new-parameter list gives restart policy `n` and limit 1, lines 3714-3716).
  - In master the default policy is `e` (estimation), with no fixed limit and a growth factor of 1.5 (`event_estim.c` lines 254-262); SCIP 11.0.0 removed the cap of one (CHANGELOG 224).
- **Status:** an open question he posed in print, answered by successors with a new tool (tree-size estimation). It is a revision of his default, not a refutation of his experiment.

---

## 5. Objective feasibility pump (Q9)

**His paper** ([S4], ZIB-Report 05-42; journal version not read) [stated, P].
- Abstract: the original pump finds feasible solutions, but of poor quality.
- Report p. 6:
  - the objective feasibility pump found a strictly better solution on 89 of 121 instances and a worse one on 17, tied on 11, and both versions failed on 4;
  - only on acc-6 did it fail where the original succeeded;
  - mean gap fell from 55.0% to 29.5%, with running time only slightly higher.
- The baseline is the Fischetti-Bertacco-Lodi pump. A text search of the report finds no mention of an objective cutoff, so the cutoff-plus-recovery remedy proposed by Fischetti, Glover and Lodi was not a baseline.

**Berthold-Lodi-Salvagnin 2019** ([S37], P pp. 5-8; co-author).
- p. 7: better solution quality on average, at the price of a slightly lower success rate and more iterations and time; cycling is avoided as a side effect.
- p. 8: no perturbation is needed while the weight still changes.

**Rival route: Fischetti-Salvagnin 2009** ([S39], abstract): better rounding through propagation (FP 2.0) improves success rate and quality. SCIP offers it as an option, off by default ([S14] `heur_feaspump.c` line 89).

**Fischetti 2026** ([S38], P pp. 1-2, 8; unreviewed, submitted to Mathematical Programming Computation; team).
- p. 2: later work, starting with [S4], replaced the original cutoff by a weighted objective.
- p. 8: SCIP's pump is the objective-weighted pump of [S4]. It adds no cutoff, never tests the rounded point, and offers a solution only when the LP iterate is integral.
- pp. 1-2: adding a mid-gap cutoff and the completion LP to SCIP's pump wins on 116, ties on 51 and loses on 9 of the 176 instances (of 424) where it reaches a solution. The median final gap falls from 59% to 30%. The author notes that this comparison was added after the pre-declared design.
- p. 2: where the plain pump finds nothing, no variant helps.
- Artefact: GitHub mfischetti-arch/fp-objective-cutoff; Zenodo 10.5281/zenodo.22810777 (MIT, 2026-09-17).

**Answer:** none (a manuscript of September 2026). The SCIP pump code is Berthold's and Salvagnin's.

[inferred] Two separate points.
- Objective weighting trades a little success rate for quality, which both the 2005 report (acc-6) and his co-author concede.
- Ignoring feasible rounded points is an implementation omission. The 2005 evaluation, however, never put the cutoff remedy beside the weighting, which is the comparison Fischetti now supplies.
- The two "gap halved" results (55.0 to 29.5% in 2005; 59 to 30% in 2026) measure different things against different baselines; do not equate them.

---

## 6. Measurement and benchmarking (Q10-Q12)

### 6.1 His measurement design [stated, P]
- **Knock-out attribution** ([S1] p. 2): geometric-mean slowdown when a feature is disabled.
- **Presolve report method** ([S9] report pp. 2-3):
  - solve-time brackets, with discussion focused on models taking at least 10 s;
  - a model counts as "affected" when the simplex iteration count changes;
  - models on which two versions give inconsistent optimal values, due to floating point, are excluded;
  - one 4-core machine, a 3,600 s limit, and 3,182 models drawn from Gurobi's library, chosen as those some Gurobi release solved within 10,000 s;
  - a text search finds no mention of seeds or variability.
- **Shifted geometric mean.** It became a community standard: MIPLIB 2017 cites his thesis for its 1 s shift ([S11] p. 444), and Le Bodic-Nemhauser cite the thesis appendix ([S19]).
- **2013 progress chapter** ([S8], abstract): it presents an unbiased way to analyse benchmark results.
- **Its finding, as relayed** ([S16] p. 2): branching ranks second of nine components. Replacing it by a textbook rule made solving more than four times slower and solved more than 25% fewer instances.

### 6.2 Performance variability
- **His 2008 report with Koch and Tuchscherer** ([S13], ZIB-Report 08-29, P pp. 1-2) [stated].
  - Trying to reproduce van Vyve and Wolsey's TSP results, they met erratic solver behaviour.
  - Minor formulation changes moved performance by more than a factor of 1,000, and it was not predictable which changes would help.
  - Dropping seemingly useful redundant information sometimes sped up solving.

  He was thus among those who documented the variability problem, starting from a failed reproduction of someone else's computational result.
- **Danna 2008** ([S40], P slides 7, 19-20, 38-39; colleague, ILOG CPLEX R&D).
  - The test set is 368 models that CPLEX 11 solves in 10-100 s.
  - SCIP, run with CPLEX as LP solver on a 135-model subset, varies under row and column permutations about as much as CPLEX, but in an uncorrelated way.
  - Most papers use only descriptive statistics, and observed differences mix effect with noise; inferential statistics are needed.
- **Lodi-Tramontani 2013** ([S41], abstract; full text HTTP 403): variability across platforms, permutations and neutral changes, and serious misreadings of careless benchmarks.
- **Fischetti-Monaci 2014** ([S42], abstract; team: Fischetti): erraticism is the tree search amplifying small differences and is largely unavoidable; their bet-and-run scheme exploits it.
- **Adegbindin-Dietrich-Pender-Lodi 2026** ([S45], abstract, preprint): in 100 randomized runs per instance on MIPLIB 2017, root degeneracy, matrix structure, coefficient ranges and presolve reductions drive variability.
- **Gurobi practice, in his words** ([S59] 1:05:00-1:08:00, caption).
  - About 6,000 instances, run with five random seeds when the cluster is free (around 12 hours).
  - Defaults come from trial and measurement.
  - Tuning should use a set of instances, never one, to avoid over-tuning and random luck.

  No statement was found on statistical tests or confidence intervals.
- [inferred] By 2023 the variability critique had shaped his group's protocol (seeds, large sets). His published papers through 2016 show no seeds (text search of [S9]); the thesis pages read do not mention seeds or permutations, and the thesis tables were not checked for them.

### 6.3 Censoring and component attribution ([S43], P pp. 4, 12-13; authors from ZIB and FICO, including Berthold)
- p. 4: the 2013 chapter's geometric-mean speed-up of 4.71 (CPLEX 8.0 to 12.5, 2,928 models), and up to 78.6 on models hard for 8.0, is an underestimate. The old version hit the 10,000 s limit on 732 models, the new one on 87.
- pp. 12-13: per-feature contributions have no easy meaningful answer. Features interact and the whole exceeds the sum of its parts, a point for which they cite his thesis. Switching one feature off lets others recover part of its effect.
- [inferred] This undercuts the knock-out percentages in the thesis, the 2013 chapter and the presolve report as additive attributions, though not their rankings.

### 6.4 Primal heuristics and the time-to-optimality yardstick
- **Thesis** ([S1] p. 4) [stated, P]: disabling all primal heuristics raises time to optimality by only 14%. In the same paragraph he adds that proving optimality is not always the user's goal.
- **Berthold 2013** ([S44], S; his former student): time to optimality and node counts reflect heuristics badly; introduces the primal integral. The source here is zbMATH keywords on MaRDI plus a search summary of the abstract; the full text was not read.
- [inferred] A limit he flagged himself; his student built the metric that fixes it.

### 6.5 MIPLIB 2003 (Q11) [stated, co-signed, P; S11]
- p. 445: earlier MIPLIB editions were selected by hand by the committee.
- p. 467: the new benchmark rule that every instance must be solvable avoids the MIPLIB 2003 situation, where four instances were still unsolved 15 years after release.
- p. 444: he sat on the committee. [inferred] A collective self-revision of a design he co-edited [S5].

### 6.6 "Almost competitive" (Q12; contradiction C1)
- **The claim.** The thesis (p. 1) and the SCIP paper's abstract [S6] call SCIP almost competitive with state-of-the-art commercial MIP solvers.
- **His thesis numbers** ([S1] pp. 377-378).
  - SCIP 0.90f was 115% slower and SCIP 0.90i 63% slower than CPLEX 10.0.1 (shifted geometric mean, ten test sets).
  - For 0.90i: 44% slower on MIPLIB, 350% on ACC, faster on ENLIGHT, ALU and MIK.
  - SCIP used CPLEX for LPs, so only the MIP part was compared; with SoPlex SCIP is usually much slower. He reads the result as evidence that SCIP's algorithms are close to the state of the art.
- **His 2023 recollection** ([S59] 0:36:30, caption): in his 2005 workshop talk, SCIP with CPLEX as LP solver performed about like CPLEX 9.0.
- **Danna 2008** ([S40] slides 7, 20): about 4 times slower than CPLEX 11 on a 135-model subset, and about 20 times on the 368 models, a set chosen by CPLEX 11 solve times.
- **Song et al. 2020** ([S54], S2 context): usually 10 or more times slower than Gurobi and CPLEX, citing public benchmarks (SCIP 6-7 era, with SoPlex; public benchmark pages are solver context only).
- **His yardstick** ([S59] 0:50:30-0:51:30, caption): reviewers who reject academic work for not beating Gurobi or Xpress miss the point. A technique should show that it improves its base solver, for example SCIP.
- [inferred] Each number depends on version, LP solver, and whose solve times selected the test set. His 2023 yardstick is the one that makes his 2007 claim defensible: SCIP's MIP machinery against CPLEX's, with the LP engine held equal.

---

## 7. Numerics and certificates (Q13)
- **Achterberg side** [stated, P].
  - The thesis treats numerical issues in propagating linear constraints ([S1] p. 3).
  - His presolve report drops models on which two Gurobi versions disagree on the optimal value because of floating point ([S9] report p. 3).
  - In 2023 he advised fixing a model's numerics before tuning: numerical trouble causes strange answers and usually degrades performance badly ([S59] 1:07:30-1:08:00, caption).
- **Cook-Koch-Steffy-Wolter 2013** ([S47], abstract): existing software suffers from floating-point inaccuracy. An exact rational branch-and-bound inside SCIP is only moderately slower. They also assemble a set of numerically difficult instances.
- **Cheung-Gleixner-Steffy 2017** ([S48], abstract; team: Gleixner): MIP software can return incorrect results, from floating point and from programming errors. They define the VIPR certificate format and extend exact SCIP to emit it.
- **Eifler-Gleixner 2022** ([S49], abstract): exact SCIP is 10.7 times faster than the 2013 framework and emits verifiable certificates.
- **Hoen-Oertel-Gleixner-Nordström 2024** ([S50], abstract): there is no established way to verify that two MIPs are equivalent, so presolve correctness cannot be certified in general. They take a first step for 0-1 programs.
- **Miltenberger-Ralphs-Steffy 2018** ([S51], abstract): a first study of how LP conditioning evolves during branch-and-cut.
- **User reports** (S2 contexts; full texts not read):
  - Grimm et al. [S52]: with Gurobi, CPLEX and SCIP on their MIQPs, constraints held only within large tolerances, objective values were wrong, and infeasibility was reported falsely.
  - Kobayashi et al. [S53]: SCIP returned incorrect optimal values on one data set because of numerical instability.
- **MIPLIB 2017** ([S11] p. 467, co-signed): the benchmark excludes numerically difficult instances and requires consistent results across solvers.
- **Answer:** none on certification.
- [inferred] His line (SCIP's original design, CPLEX, Gurobi) stays with floating point plus safeguards. He places the remedy in modelling and in excluding inconsistent cases from benchmarks, while exactness and certificates were built by others inside the framework he designed.

---

## 8. Cut selection (Q14)
- **Thesis** ([S1] p. 4) [stated, P].
  - Adding all cuts, or one cut per round, costs 70% or 80% more time than careful selection.
  - Preferring nearly orthogonal cuts gains 20% over selecting by violation alone.
- **His own warning** ([S59] 0:41:30-0:42:00, caption): presolve ideas usually pay off. New cuts and branching rules often do not, even when a cut looks great (it cuts off the LP solution and tightens the bound a lot) and performance still gets worse.
- **Turner-Koch-Serrano-Winkler 2023** ([S55], P p. 3 and abstract).
  - Cut scoring rules are weighted sums whose weights are usually set by a grid search, as in his thesis and later SCIP studies.
  - They build MILP families on which any finite grid misses every good parameter value, and argue for instance-dependent parameters.
  - They grant that no fixed parameter can be good everywhere and that cut selection is a small part of the solve.
- **Dey-Molinaro 2018** ([S56], P pp. 8-9; team: Dey).
  - No theory exists for the parallelism measure; they relay from [S6] that parallelism to the objective may be ineffective.
  - A fixed cap on cuts per round, as in his thesis, is one common choice whose correctness is unclear and untested.
  - They thank him for help with the manuscript (acknowledgements).
- **Answer:** none in print. [inferred] The critique is cooperative (he helped the critics), and his own warning about proxy measures sides with the critics' call for instance-aware choices only as far as the test set confirms them.

---

## 9. Presolve (Gurobi era)
- **The paper** ([S9]): the 2016 ZIB-Report version was read for its method (pp. 1-3) and searched as text; the journal version was not read.
- **Critique reaching it:**
  - [S32] p. 776 attributes to it a dual-proof result that the report version does not contain (section 3.3).
  - [S50] states the general gap in certifying presolve (section 7).
  - Koch et al.'s general caveats about studies on vendor-selected sets apply ([S43] pp. 4-5, 12-13).
- No critique of specific reductions was found.
- He calls presolve the most rewarding part of the solver to work on, because good presolve ideas usually turn into speed ([S59] 0:41:30, caption).

---

## 10. Judgements revisited and predictions

| Year | His judgement or open question | Later evidence | By whom | Status |
|---|---|---|---|---|
| 2000-2001 | Learned branching collapsed onto one feature; learning dropped ([S59], caption) | ML branching returns 2016-2019, with his rule as baseline | [S27], [S28] | Open; he now uses explainable ML for defaults |
| 2004 | (η_rel = 8, λ = 4) sweet spot ([S2] p. 12) | Dynamic threshold (2007); SCIP: η_rel 1-5 dynamic, λ = 9 | Himself; SCIP team | Revised |
| 2004 | Open question: can the node gap to full strong branching be closed cheaply? ([S2] p. 12) | Much of the gap is side effects; hybrid branching is only 20.5% above full strong in fair nodes | [S16] | Largely answered |
| 2004/2007 | Strong-branching side effects modest: leaf savings about a factor ½ for full strong, negligible for others; bound tightening named but not measured | Full strong: fair nodes 6.5 times reported; reliability 1.78 times | [S16] | Refined |
| 2005 | Conflict analysis slows feasible MIPs by 15%; fixes named ([S3]) | More than 10% faster by 2007; pools null; dual proofs and cuts add more | Himself; [S31]-[S34] | Answered and extended |
| 2007 | Product score beats linear by 14% ([S1] p. 3) | Not uniformly; svts 11% better on very large trees, 1% overall; product kept | [S19], [S20] | Stands on broad sets |
| 2007 | Restart only after the root; delayed restarts need new criteria ([S1] pp. 160, 163) | Tree-size-based restarts pay off; SCIP 7.0 and 11.0 defaults | [S36] | His open question, answered |
| 2007 | Primal heuristics add little to time to optimality (14%) | Yardstick judged inadequate; primal integral | [S44] | Measure changed; he had flagged the limit |
| 2005/2007 | SCIP almost competitive (CPLEX as LP solver) | 4-20 times slower on CPLEX-selected sets (2008); about 10 times (2020) | [S40], [S54] | Contested (C1) |
| 2005 | Objective pump beats the original on quality; cutoff remedy not compared | Lower success rate (co-author); cutoff plus recovery beats SCIP's pump (unreviewed) | [S37], [S38] | Open |
| 2006 | MIPLIB 2003 hand-selected, with unsolved benchmark instances | Data-driven, solvable-only benchmark | MIPLIB 2017 committee, including him | Conceded |

- No failed replication of a headline result was found; the direct replication found ([S16] p. 58) confirms his 2005 ranking.
- No retraction, erratum, comment or reply under his name appears in Crossref (author query in this run).

---

## 11. How Achterberg handles critique (pattern for Phase 2) [inferred unless tagged]
1. **He publishes his own weak spots and open questions, and successors answer them.** The node gap to full strong branching (2004), conflict analysis slowing feasible MIPs plus its fixes (2005), and the need for new restart criteria (2007) were each answered later by successors: Gamrath's fair nodes, Witzig's pools and dual proofs, Anderson et al.'s clairvoyant restarts. Most critique in this file is a successor's answer to a question he left in print.
2. **No published replies; answers come as code and defaults.** By 2007 the reliability threshold was dynamic; in 2009 hybrid branching added SAT and CP history scores ([S7]; [S16] pp. 21-22). He adopts a successor's idea when the test set confirms it, as with Turner's branching criterion in Gurobi ([S59] 0:55:00).
3. **Practice over worst-case theory** [stated, P; S12 slides 20-21, 26]: design for practical instances, and treat worst-case bounds as reasons for safeguards rather than verdicts. He also distrusts proxies: a cut or branching rule that looks strong often does not speed up the solve ([S59] 0:41:30, caption).
4. **Measures privately at vendor scale, increasingly with seeds:** 2,928 models (2013), 3,182 (2016), 7,030 (2022 deck), about 6,000 with five seeds (2023, caption). Public critics cannot rerun these, so public critique reaches mainly his ZIB-era methods.
5. **Joins collective revisions.** He co-signed MIPLIB 2010 and 2017 ([S10], [S11]) and documented variability himself in 2008 ([S13]); he helped Dey and Molinaro with their cut-selection critique ([S56]).
6. **A self-declared blind spot** [stated, caption; S59 1:20:00-1:22:00, 0:27:00]. He follows the literature poorly, prefers to build from scratch, relies on collaborators for related work, and finds the literature review the hardest part of a paper. He started constraint integer programming unaware that John Hooker had pursued the same CP-MIP integration idea.
7. **Adoption criterion: robust as a default.** In his view automatic Dantzig-Wolfe decomposition (GCG) works very well on some classes and produces garbage on others, so it is not ready for default settings; Gurobi lets users supply the block structure instead ([S59] 1:01:30-1:02:00, caption). [inferred] This is a live disagreement inside milp-team with Lübbecke's GCG line.
8. **Durable defaults.** The product score, count-based reliability, graph-based conflict analysis and hybrid branching are still SCIP defaults in November 2026. Successors' refinements often ship off by default (Hendel's tests, the tree model, cut-based conflict analysis) [practice, P; S14], and their gains concentrate on subsets (very large trees, 0-1 programs, degenerate instances).
9. **For the skill:** challenged with a theoretically better rule, the expected Achterberg move is to ask for its effect on the shifted geometric mean of a broad, multi-seed test set and on the hardest bracket, and whether it is robust enough to be a default, rather than for a proof.

---

## Contradictions (kept, not reconciled)
- **C1. Competitiveness of SCIP.** All different sets, versions and LP solvers:
  - "almost competitive" ([S1] p. 1; [S6] abstract) and about on a par with CPLEX 9.0 in 2005 ([S59] 0:36:30, caption);
  - 63% or 115% slower than CPLEX 10.0.1, with CPLEX as LP solver ([S1] p. 377);
  - Danna: about 4 times slower on 135 models and 20 times on 368 CPLEX-selected models ([S40] slides 7, 20);
  - Song et al.: usually 10 or more times slower ([S54], 2020).
- **C2. Unbiased progress measurement.** The 2013 chapter claims an unbiased analysis scheme ([S8] abstract). Koch et al. call its 4.71 an underestimate because of time-limit censoring, and hold that component contributions cannot be isolated ([S43] pp. 4, 12-13).
- **C3. Product score.** His 14% gain (34% in nodes, relayed in [S19] p. 4) against the best of five linear weights ([S1] p. 3), versus "not systematically better" and no theoretical basis ([S19] p. 5), versus near parity on the whole MIPLIB 2017 benchmark set ([S20] p. 17). SCIP keeps the product score.
- **C4. Strong branching and tree size.** Smallest trees, as the empirical consensus credited to [S2] ([S21] p. 3) and replicated ([S16] p. 58), versus mostly side effects, with better decisions alone giving 59% ([S16] p. 58), versus exponentially larger trees on a constructed class, versus within a factor of two of the optimal tree on tested classes ([S21] p. 4). His own text gives the leaf savings as about a factor ½ ([S2] p. 9) and names bound tightening without measuring it ([S1] pp. 69-70).
- **C5. Restarts.** Only after the root, with delayed restarts inferior on a fixing-count trigger ([S1] pp. 160, 163), versus clairvoyant in-tree restarts outperforming ([S36]), now SCIP defaults ([S14]).
- **C6. Value of conflict analysis.**
  - Over time in his own texts: 15% slower on feasible MIPs in 2005 ([S3] abstract), more than 10% faster in 2007 ([S1] p. 5).
  - Graph analysis gains 20.1% on affected instances in SCIP ([S32] p. 776), while Gurobi reportedly relies solely on dual proofs, which in SCIP alone barely change time ([S32] p. 776). The dual-proof claim is not found in the 2016 report version of [S9].
- **C7. Objective feasibility pump.** Better solutions on 89 of 121 instances, mean gap 55.0% to 29.5%, one instance lost ([S4] report p. 6), versus losing to cutoff plus recovery on 116 of 176 instances, median final gap 59% against 30% ([S38] pp. 1-2; unreviewed; comparison added after the pre-declared design).
- **C8. Heuristics.** Small effect on time to optimality (14%, [S1] p. 4) versus a large effect on the primal bound under the primal integral ([S44], abstract-level only). He concedes the yardstick's limit in the same paragraph.
- **C9. Practice-first versus theory-first.** Worst-case results say nothing about practical instances ([S12] slides 20-21), versus critiques built on worst-case or proof-complexity results ([S21]; [S34] p. 2; [S55] p. 3).
- **C10. MIPLIB 2003 versus MIPLIB 2017 design**, both co-signed by him ([S5]; [S11] pp. 445, 467).
- **C11. Installing the optimal value when comparing branching rules.** Deliberately not done in 2004, because reaching feasible solutions fast is part of a rule's job ([S2] p. 8), versus done in 2020 to isolate decision quality ([S16] pp. 57-58). Shah-Dey argue that scores should account for pruning by the primal bound ([S22]).
- **C12. Size of the Gurobi MIP test set.** 7,030 instances (July 2022 deck, [S12] slide 5) versus about 6,000 (2023 interview, caption, [S59] 1:05:30). Different dates, and possibly different subsets; not reconciled.

## Gaps
- **Not read (journal versions).**
  - "Branching rules revisited" (ORL 2005), "Conflict analysis in mixed integer programming" (Discrete Optimization 2007), "Improving the feasibility pump" (Discrete Optimization 2007) and "Presolve Reductions in Mixed Integer Programming" (IJOC 2020). Their ZIB-Report versions were read instead, so findings may miss changes made in revision.
  - "MIPLIB 2003" [S5], "MIPLIB 2010" [S10], the SCIP paper beyond its abstract [S6], and the 2013 progress chapter [S8].
- **The thesis** was read on pp. ix, 1-5, 64, 69-70, 160, 163, 179 and 377-378 only.
- **Not reached.**
  - The Aussois 2018 slides (self-signed certificate; not bypassed), his MIP 2010 talk and the pump-reduce patent documents.
  - Full texts of Hendel 2015 [S18], Fischetti-Monaci 2012 [S26] (host down), Berthold 2013 [S44] (HTTP 403; no direct ZIB file link found), Khalil et al. 2016 [S27] (bot check) and Lodi-Tramontani 2013 [S41] (HTTP 403).
  - The OR Proceedings full text of Gamrath-Schubert [S17] (its content is covered by [S16]).
- **His own voice.** Only the 14 caption excerpts of the 2023 interview saved by agent 04 were read; the rest of the interview was not. No published reply, rejoinder or erratum was found.
- **Coverage.** Semantic Scholar citation contexts were fetched for only 2 of 8 core works (HTTP 429). Critiques citing the 2005 and 2007 papers, MIPLIB 2003, the 2013 chapter or the presolve paper may be missing.
- **Gurobi era.** No public critique of Gurobi algorithms attributable to him was found, and vendor benchmark disputes were not examined (public benchmark pages are solver context only). Witzig et al.'s statement that Gurobi relies solely on dual proofs is unconfirmed.
- **Not searched within the time budget.** Critiques of the ParaSCIP and supercomputer papers he co-authored; of the MCF separator, node selection or specific presolve reductions; and a CP-side assessment of constraint integer programming as a paradigm (only his own concession about Hooker was found).
- **Unconfirmed details.** Whether SCIP's default skip of poor strong-branching candidates derives from Hendel 2015; whether the thesis experiments used seeds or permutations.

## Sources
One line each: title, author(s), date, identifier or URL, primary or secondary, and what was read. Identifiers were checked in this run with Crossref, DataCite resolution through doi.org, the arXiv API, OpenAlex, Zenodo, YouTube oEmbed, GitHub or the repository landing page.

1. [S1] "Constraint Integer Programming", T. Achterberg, PhD thesis, TU Berlin, 2007 (DepositOnce date 2007-07-17), DOI 10.14279/depositonce-1634; DepositOnce copy read as page images (pp. ix, 1-5, 377-378), ZIB copy opus4.kobv.de/opus4-zib/files/1112/Achterberg_Constraint_Integer_Programming.pdf read as text (pp. 64, 69-70, 160, 163, 179) (primary)
2. [S2] "Branching rules revisited", T. Achterberg, T. Koch, A. Martin, Operations Research Letters 33(1):42-54, 2005, DOI 10.1016/j.orl.2004.04.002; journal not read; ZIB-Report 04-13 (May 2004), opus4.kobv.de/opus4-zib/files/788/ZR-04-13.pdf, read pp. 1-12 (primary)
3. [S3] "Conflict analysis in mixed integer programming", T. Achterberg, Discrete Optimization 4(1):4-20, 2007, DOI 10.1016/j.disopt.2006.10.006; journal not read; ZIB-Report 05-19 (Aug 2005), opus4.kobv.de/opus4-zib/files/853/ZR-05-19.pdf, read abstract, pp. 1-2, 16, 18 (primary)
4. [S4] "Improving the feasibility pump", T. Achterberg, T. Berthold, Discrete Optimization 4(1):77-86, 2007, DOI 10.1016/j.disopt.2006.10.004; journal not read; ZIB-Report 05-42 (Sept 2005), opus4.kobv.de/opus4-zib/files/875/ZR-05-42.pdf, read abstract, pp. 1-2, 6 and a text search (primary)
5. [S5] "MIPLIB 2003", T. Achterberg, T. Koch, A. Martin, Operations Research Letters 34(4):361-372, 2006, DOI 10.1016/j.orl.2005.07.009; metadata only, not read (primary)
6. [S6] "SCIP: solving constraint integer programs", T. Achterberg, Mathematical Programming Computation 1(1):1-41, 2009, DOI 10.1007/s12532-008-0001-1; abstract (Springer page) (primary)
7. [S7] "Hybrid Branching", T. Achterberg, T. Berthold, CPAIOR 2009, LNCS pp. 309-311, DOI 10.1007/978-3-642-01929-6_23; abstract (primary)
8. [S8] "Mixed Integer Programming: Analyzing 12 Years of Progress", T. Achterberg, R. Wunderling, Facets of Combinatorial Optimization (Springer 2013) 449-481, DOI 10.1007/978-3-642-38189-8_18; abstract (primary)
9. [S9] "Presolve Reductions in Mixed Integer Programming", T. Achterberg, R. E. Bixby, Z. Gu, E. Rothberg, D. Weninger, INFORMS J. Comput. 32(2):473-506, 2020, DOI 10.1287/ijoc.2018.0857; journal not read; ZIB-Report 16-44 (version of 9 Dec 2016), opus4.kobv.de/opus4-zib/files/6037/Presolve.pdf, read pp. 1-3 and a text search (primary, co-signed)
10. [S10] "MIPLIB 2010", T. Koch, T. Achterberg, E. Andersen et al., Mathematical Programming Computation 3(2):103-163, 2011, DOI 10.1007/s12532-011-0025-9; metadata only (primary, co-signed)
11. [S11] "MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library", A. Gleixner, G. Hendel, G. Gamrath, T. Achterberg et al., Mathematical Programming Computation 13:443-490, 2021, DOI 10.1007/s12532-020-00194-3 (open access); read pp. 443-446, 467 (primary, co-signed by 16 authors)
12. [S12] "Combinatorial Algorithms Used Inside a MIP Solver", T. Achterberg, talk deck, SEA 2022, 26 July 2022, sea2022.ifi.uni-heidelberg.de/talk_achterberg.pdf; read slides 1-29 (cited 5, 20-21, 26, 29) (primary)
13. [S13] "On the Effects of Minor Changes in Model Formulations", T. Achterberg, T. Koch, A. Tuchscherer, ZIB-Report 08-29, August 2008, opus4.kobv.de/opus4-zib/files/1080/ZR_08_29.pdf; read abstract and pp. 1-2 (primary)
14. [S14] SCIP source and release notes, GitHub scipopt/scip, master commit 353584f (8 Nov 2026): `branch_relpscost.c`, `set.c`, `treemodel.c`, `event_estim.c`, `heur_feaspump.c`, `conflict_graphanalysis.c`, `conflict_dualproofanalysis.c`, `CHANGELOG`; read the cited lines (primary for files naming him; observed for successors' changes)
15. [S15] OpenAlex author record A5016513861 (via ORCID 0000-0002-0862-7065), 42 works, fetched 2026-11-08 (secondary, tool data)
16. [S16] "Enhanced predictions and structure exploitation in branch-and-bound", G. Gamrath, PhD thesis, TU Berlin, 2020, DOI 10.14279/depositonce-10710; read pp. ii, 2-3, 18, 21-23, 41, 57-60 (secondary)
17. [S17] "Measuring the Impact of Branching Rules for Mixed-Integer Programming", G. Gamrath, C. Schubert, Operations Research Proceedings 2017 (2018) 165-170, DOI 10.1007/978-3-319-89920-6_23; abstract (secondary)
18. [S18] "Enhancing MIP Branching Decisions by Using the Sample Variance of Pseudo Costs", G. Hendel, CPAIOR 2015, LNCS pp. 199-214, DOI 10.1007/978-3-319-18008-3_14; abstract (secondary)
19. [S19] "An abstract model for branching and its application to mixed integer programming", P. Le Bodic, G. Nemhauser, Mathematical Programming 166:369-405, 2017, DOI 10.1007/s10107-016-1101-8; arXiv 1511.01818v3 read pp. 1-5, 27-29 (secondary)
20. [S20] "Further results on an abstract model for branching and its application to mixed integer programming", D. Anderson, P. Le Bodic, K. Morgan, Mathematical Programming 190:811-841 (Crossref issue year 2020), DOI 10.1007/s10107-020-01556-4; arXiv 1909.01472v2 read abstract, pp. 3, 17 (secondary)
21. [S21] "A theoretical and computational analysis of full strong-branching", S. S. Dey, Y. Dubey, M. Molinaro, P. Shah, Mathematical Programming 205:303-336 (Crossref issue year 2023), DOI 10.1007/s10107-023-01977-x; arXiv 2110.10754v2 read pp. 1-5 (secondary)
22. [S22] "Improving Full Strong Branching Decisions by Incorporating Additional Information", P. Shah, S. S. Dey, arXiv 2507.09455v1, July 2025; abstract (secondary, preprint)
23. [S23] "Cloud Branching", T. Berthold, D. Salvagnin, CPAIOR 2013, LNCS pp. 28-43, DOI 10.1007/978-3-642-38171-3_3; abstract (secondary)
24. [S24] "An exploratory computational analysis of dual degeneracy in mixed-integer programming", G. Gamrath, T. Berthold, D. Salvagnin, EURO J. Comput. Optim. 8:241-261, 2020, DOI 10.1007/s13675-020-00130-z (CC BY); read pp. 241, 244, 246, 259 (secondary)
25. [S25] "Exploiting Dual Degeneracy in Branching", T. Berthold, G. Gamrath, D. Salvagnin, ZIB-Report 19-17, April 2019 (OpenAlex record), opus4.kobv.de/opus4-zib/files/7302/ZR-19-17.pdf; abstract read (secondary)
26. [S26] "Branching on nonchimerical fractionalities", M. Fischetti, M. Monaci, Operations Research Letters 40(3):159-164, 2012, DOI 10.1016/j.orl.2012.01.008; abstract from cris.unibo.it/handle/11585/542478 (secondary)
27. [S27] "Learning to Branch in Mixed Integer Programming", E. Khalil, P. Le Bodic, L. Song, G. Nemhauser, B. Dilkina, AAAI 2016, DOI 10.1609/aaai.v30i1.10080; abstract (Crossref) (secondary)
28. [S28] "Exact Combinatorial Optimization with Graph Convolutional Neural Networks", M. Gasse, D. Chételat, N. Ferroni, L. Charlin, A. Lodi, NeurIPS 2019, arXiv 1906.01629v3; read pp. 1, 3, 6, 8 (secondary)
29. [S29] "On learning and branching: a survey", A. Lodi, G. Zarpellon, TOP 25:207-236, 2017, DOI 10.1007/s11750-017-0451-6; abstract (secondary)
30. [S30] "Discounted Pseudocosts in MILP", K. K. Patel, arXiv 2407.06237v1, July 2024; abstract (secondary, preprint)
31. [S31] "Experiments with Conflict Analysis in Mixed Integer Programming", J. Witzig, T. Berthold, S. Heinz, CPAIOR 2017, LNCS pp. 211-220, DOI 10.1007/978-3-319-59776-8_17; arXiv 1611.07887v1 read in full (secondary)
32. [S32] "Computational aspects of infeasibility analysis in mixed integer programming", J. Witzig, T. Berthold, S. Heinz, Mathematical Programming Computation 13:753-785, 2021, DOI 10.1007/s12532-021-00202-0 (open access); read pp. 754-758, 773, 776-778, 782 (secondary)
33. [S33] "Improving Conflict Analysis in MIP Solvers by Pseudo-Boolean Reasoning", G. Mexi, T. Berthold, A. Gleixner, J. Nordström, CP 2023, LIPIcs, DOI 10.4230/LIPIcs.CP.2023.27; arXiv 2307.14166v1 read abstract and pp. 1-3 (secondary)
34. [S34] "Cut-based Conflict Analysis in Mixed Integer Programming", G. Mexi, F. Serrano, T. Berthold, A. Gleixner, J. Nordström, arXiv 2410.15110v2 (October 2025); read pp. 1-2, 18-21 (secondary)
35. [S35] "Rapid Learning for Binary Programs", T. Berthold, T. Feydy, P. J. Stuckey, CPAIOR 2010, LNCS pp. 51-55, DOI 10.1007/978-3-642-13520-0_8; abstract (secondary)
36. [S36] "Clairvoyant Restarts in Branch-and-Bound Search Using Online Tree-Size Estimation", D. Anderson, G. Hendel, P. Le Bodic, M. Viernickel, AAAI 2019, pp. 1427-1434, DOI 10.1609/aaai.v33i01.33011427; abstract (Crossref) (secondary)
37. [S37] "Ten years of feasibility pump, and counting", T. Berthold, A. Lodi, D. Salvagnin, EURO J. Comput. Optim. 7:1-14, 2019, DOI 10.1007/s13675-018-0109-7 (open copy hdl.handle.net/11577/3339187); read pp. 5-8, 11 (secondary)
38. [S38] "Feasibility Pump with Objective Cutoff: A Computational Study", M. Fischetti, manuscript dated September 2026, submitted to Mathematical Programming Computation (unreviewed), github.com/mfischetti-arch/fp-objective-cutoff (paper/manuscript.pdf; README), Zenodo DOI 10.5281/zenodo.22810777 (reproducibility package, 2026-09-17); read pp. 1-2, 8 and the README (secondary)
39. [S39] "Feasibility pump 2.0", M. Fischetti, D. Salvagnin, Mathematical Programming Computation 1(2-3):201-222, 2009, DOI 10.1007/s12532-009-0007-3; abstract (secondary)
40. [S40] "Performance variability in mixed integer programming", E. Danna (ILOG CPLEX R&D), MIP 2008 workshop slides (PDF created 7 Aug 2008), coral.ie.lehigh.edu/~jeff/mip-2008/talks/danna.pdf; read slides 1-8, 18-21, 38-40 (secondary)
41. [S41] "Performance Variability in Mixed-Integer Programming", A. Lodi, A. Tramontani, INFORMS TutORials 2013, pp. 1-12, DOI 10.1287/educ.2013.0112; abstract (OpenAlex), full text HTTP 403 (secondary)
42. [S42] "Exploiting Erraticism in Search", M. Fischetti, M. Monaci, Operations Research 62(1):114-122, 2014, DOI 10.1287/opre.2013.1231; abstract (secondary)
43. [S43] "Progress in mathematical programming solvers from 2001 to 2020", T. Koch, T. Berthold, J. Pedersen, C. Vanaret, EURO J. Comput. Optim. 10:100031, 2022, DOI 10.1016/j.ejco.2022.100031; arXiv 2206.09787v2 read pp. 1-5, 12-13 (secondary)
44. [S44] "Measuring the impact of primal heuristics", T. Berthold, Operations Research Letters 41(6):611-614, 2013, DOI 10.1016/j.orl.2013.08.007; metadata and zbMATH keywords (MaRDI portal), abstract seen only as a search summary, not read (secondary)
45. [S45] "When Solvers Get Moody: Quantifying and Predicting Performance Variability in Mixed Integer Programming", M. Adegbindin, B. Dietrich, J. Pender, A. Lodi, arXiv 2610.12876v1, October 2026; abstract (secondary, preprint)
46. [S46] "Mitigating Performance Variability in Mixed-Integer Programming Solvers via LP State Steering", M. Adegbindin, B. Dietrich, J. Pender, arXiv 2610.17268v1, October 2026; abstract (secondary, preprint)
47. [S47] "A hybrid branch-and-bound approach for exact rational mixed-integer programming", W. Cook, T. Koch, D. E. Steffy, K. Wolter, Mathematical Programming Computation 5(3):305-344, 2013, DOI 10.1007/s12532-013-0055-6; abstract (secondary)
48. [S48] "Verifying Integer Programming Results", K. K. H. Cheung, A. Gleixner, D. E. Steffy, IPCO 2017, LNCS pp. 148-160, DOI 10.1007/978-3-319-59250-3_13; abstract (secondary)
49. [S49] "A computational status update for exact rational mixed integer programming", L. Eifler, A. Gleixner, Mathematical Programming 197(2):793-812 (Crossref issue year 2022), DOI 10.1007/s10107-021-01749-5; abstract (secondary)
50. [S50] "Certifying MIP-Based Presolve Reductions for 0-1 Integer Linear Programs", A. Hoen, A. Oertel, A. Gleixner, J. Nordström, CPAIOR 2024, LNCS pp. 310-328, DOI 10.1007/978-3-031-60597-0_20; abstract (secondary)
51. [S51] "Exploring the Numerics of Branch-and-Cut for Mixed Integer Linear Optimization", M. Miltenberger, T. Ralphs, D. E. Steffy, Operations Research Proceedings 2017 (2018) 151-157, DOI 10.1007/978-3-319-89920-6_21; abstract (secondary)
52. [S52] "Optimal price zones of electricity markets: a mixed-integer multilevel model and global solution approaches", V. Grimm, T. Kleinert, F. Liers, M. Schmidt, G. Zöttl, Optimization Methods and Software 34:406-436 (Crossref issue year 2017), DOI 10.1080/10556788.2017.1401069; S2 context only, full text not read (secondary)
53. [S53] "Cardinality-constrained Distributionally Robust Portfolio Optimization", K. Kobayashi, Y. Takano, K. Nakata, arXiv 2112.12454v2, 2021-2022; S2 context only (secondary)
54. [S54] "A General Large Neighborhood Search Framework for Solving Integer Linear Programs", J. Song, R. Lanka, Y. Yue, B. Dilkina, arXiv 2004.00422v3, 2020; S2 context only (secondary)
55. [S55] "Adaptive Cut Selection in Mixed-Integer Linear Programming", M. Turner, T. Koch, F. Serrano, M. Winkler, Open Journal of Mathematical Optimization 4:1-28, 2023, DOI 10.5802/ojmo.25; arXiv 2202.10962v3 read abstract and p. 3 (secondary)
56. [S56] "Theoretical challenges towards cutting-plane selection", S. S. Dey, M. Molinaro, arXiv 1805.02782v1, May 2018; read abstract, pp. 8-9, acknowledgements and references (secondary)
57. [S57] "Five Ideas I'll use in my optimization class after listening to Gurobi's Tobias Achterberg", M. Watson, Substack blog, 5 Oct 2023, miketalksai.substack.com/p/five-ideas-ill-use-in-my-optimization; read the post (secondary; relays [S59])
58. [S58] Semantic Scholar Graph API citation contexts for [S6] (1,000 citing records) and [S7] (111), fetched 2026-11-08, filtered by keyword (secondary, tool data)
59. [S59] "Subject to: Tobias Achterberg", interview on the YouTube channel "Subject to", uploaded 2023-08-17, youtube.com/watch?v=8bhIW27vCUQ (title and channel checked via oEmbed); automatic-caption excerpts A-N saved during this run by research agent 04 at `references/sources/talks/subject-to-2023-interview.excerpt.transcript.txt`; read all excerpts, cited by timestamp (primary, caption, not speaker-checked)
