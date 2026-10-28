# Qi Huangfu · 03 Process evidence (what he actually does)

- **Researcher**: Qi Huangfu (living). University of Edinburgh PhD 2013, supervised by J. A. J. Hall. He wrote the original HSOL dual revised simplex code (later the simplex core of HiGHS), worked on FICO Xpress, and develops COPT (Cardinal Operations).
- **Dimension**: research-craft Phase 1, research agent 03 of 06: process evidence. This covers behaviour visible in code, experiment sections, version histories, and dropped or abandoned work.
- **Research date**: 2026-10-27
- **Sources consulted**: 41 (S1–S41 below). The identifiers of 6 further works he cites were also checked through the Crossref API. WebSearch calls used: 2.
- **Local corpus**: `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep`, so there was no user-supplied material. `private/` was not opened.
- **Tags**: [stated] = what Huangfu wrote or said about how he works. This includes co-authored text, marked "(co-authored)". [practice] = what the papers, code or records show was actually done. [observed] = what others recorded (Hall, the HiGHS team, FICO, conference pages). [inferred] = my inference, not established. Each item also says primary or secondary.
- **Attribution caveat (read first)**: almost all written evidence from 2010 to 2018 is co-authored with, or was presented by, his supervisor Julian Hall. The 2013 thesis (S1) and the 2014 FICO blog post (S9) are the only single-authored research texts found. HSOL's development history before 2017 is not public. The earliest public code snapshot (July 2017, S25/S26) already contains edits by Hall and Galabova, so individual lines cannot be attributed. Thesis page numbers below are the printed page numbers (PDF page = printed + 1). The thesis's terms of use forbid extensive quotation, so thesis quotes are kept short and the rest is paraphrased with page references.

---

## 0. Era and resource context (timeline used for every item below)

| Period | Role / setting | Compute, tools, team | Evidence |
|---|---|---|---|
| 2007–08 | MSc in High Performance Computing, Univ. of Edinburgh. Supervisors F. Reid, S. Geiger | Ported a C++ FE–FV code to two HPC systems (Ness, ECDF). Built a METIS-based mesh partitioner plus a Python verification program | S2 |
| 2009–2013 | PhD, Edinburgh. Supervisor J. Hall, second supervisor J. Gondzio. Funded by "Format International Ltd. and NAIS" (thesis p. 7) | C++ with OpenMP and the Intel C++ compiler. 2010–11 runs on a dual quad-core AMD Opteron 2378; thesis runs on a 16-core Intel Xeon E5620 workstation "compute64b" with Intel C++ 13.0 and OpenMP 3.1 (thesis p. 17). Sole developer of the solver (ParISS, then HSOL). Parallel-simplex group peers: E. Smith (GPU, block-angular), M. Lubin (distributed, block-angular) | S1, S3, S13–S16 |
| 2013–2018 | FICO Xpress. FICO House, Birmingham UK address on the 2015 report (S6). Hall's 2019 slide: "FICO Xpress (2013-2018)" (S22) | Commercial solver team. A FICO deck (© 2014) benchmarks "The parallel dual simplex method" in Xpress 7.7 against 7.6 (S33). Journal experiments on 2× Intel Xeon E5-2670 (16 cores) using 8 threads (S7 p. 133) | S6, S7, S9, S22, S33 |
| ~2019 | Contributes a primal simplex solver to HiGHS (Hall, 2019 slides) | no Git commits under his name in HiGHS (S28) | S22, S27, S28 |
| 2022–2024 at least | COPT developer at Cardinal Operations. Commits COPT release notes. JuliaCon 2022 lightning talk | Product team. Era of GPU first-order LP (co-author of cuPDLP-C, 2023) | S10, S11, S29–S32 |

His start date at Cardinal Operations is **not established** (see Gaps).

---

## 1. Research taste: what counts as worth doing (behavioural evidence)

**PE-01. A parallel or algorithmic idea only counts if tested inside an efficient serial solver.** [stated (co-authored)] [practice] primary
- Stated: "for novel computational developments to be of value they must be tested within an efficient implementation or good reasons given why they are applicable in such an environment. Any development which is only effective in the context of an inefficient implementation is not worthy of attention." (S7, MPC 2018, Sect. 2, p. 121.)
- Stated, single-authored, in the FICO blog of 13 May 2014: "A meaningful simplex parallelization has to be designed and developed based on a state-of-the-art sequential simplex solver and still allow for significant parallelization." (S9.)
- Practice: before making any parallel claim, every document benchmarks the serial code against Clp and usually Cplex:
  - May 2011 report: ParISS on one core vs Clp 1.06 (S3).
  - Jan/Jul 2013 report: hsol vs Clp 1.14/1.15 and Cplex 11.1/12.4 (S4, S5).
  - Thesis: HSOL vs Clp 1.14 and Cplex 12.4 (S1 p. 18).
  - 2018 paper: hsol vs Clp 1.15. The paper reports hsol "2.29 times faster than Clp" and an iteration speed 1.60 times Clp's (S7 p. 136).
- Context: PhD project. The baseline was the open-source solver his supervisor managed. Hall's PPAM 2011 slide on Clp says "H is now project manager" (S15, slide 34).

**PE-02. Ruling out a whole research path on efficiency grounds.** [practice] [stated] primary
- The thesis reviews the dense-algebra and tableau parallel simplex literature (Table 4.1). It concludes that even the best speedups cannot match a good sparse sequential solver: "Therefore, this path is excluded from future consideration." (S1 p. 75.)
- The 2014 blog post repeats the judgement: "good speedup ratios are related to less efficient sequential implementations of the simplex method." (S9.)
- Context: 2012–13. GPU and dense-simplex papers were frequent at the time, and his group's own GPU work (Smith) was running in parallel (S13 slides 25–29; S14 slide 15).

**PE-03. Taste for leaving the textbook rule only when there is a computational payoff.** [practice] primary
- PAMI deliberately uses a pivoting rule (suboptimization) that the thesis calls "generally inferior" to dual steepest edge. It is adopted purely to create task parallelism (S1 pp. 77–79, 93–94).
- The cost is then measured explicitly: serial PAMI is about 30% slower than HSOL (thesis p. 86), and the 2018 paper reports a mean factor of 0.64 (S7 p. 136).
- A pivot "quality control" cutoff was added to contain that cost (PE-16).

---

## 2. Problem choice and timing

**PE-04. "Why now" argued from a changed context, not from novelty alone.** [stated (thesis, single-authored); repeated co-authored] primary
- The thesis gives two reasons that the dual revised simplex method deserves renewed parallel effort (S1 pp. 15–16, 77–78):
  - The dual has replaced the primal as the preferred variant since DSE and BFRT. The only prior parallel dual work (Bixby & Martin, INFORMS J. Comput. 12(1):45–56, 2000, DOI 10.1287/ijoc.12.1.45.11902) had neither BFRT nor hyper-sparse solves.
  - Multicore desktops make "any speedup" useful.
- The same argument opens the 2018 paper: "Thus we have used a relatively standard architecture to perform computational experiments." (S7 p. 120.)
- Context: thesis written 2013.

**PE-05. Building a new serial solver from scratch as the platform for the research question.** [stated] [practice] primary
- Thesis: existing public-domain codes "are either too complicated to be extended for parallelization or too simple to be based on", so HSOL "has been implemented from scratch" (S1 p. 16). The 2018 paper says the same (S7 p. 120).
- Practice: the code base grew in stages:
  - **Nov 2010.** RAL seminar slide "Prototype implementation" (S13, slide 22, 2 Dec 2010):
    - bullet "Written by Qi Huangfu (2010)";
    - it already used hyper-sparse PRICE and DSE pricing;
    - under "Does not (yet) use" the slide lists "Hyper-sparse operations with B-1" and "Bound-flipping ratio test";
    - "First run last week!"
  - **May 2011.** PF-update prototype ParISS (S3).
  - **Sep 2011.** "ParISS 2.0" (S15).
  - **2013.** HSOL with Forrest–Tomlin (FT) and novel updates (S1).
- Context: 2010, early in the PhD (2009–2013 per Hall's 2019 slide, S22). He was the sole implementer.

**PE-06. Choosing a forgotten 1970s technique at project start.** [practice] [observed] primary
- Suboptimization (Rosander, Mathematical Programming Studies 1975, pp. 108–117, DOI 10.1007/bfb0120714) is already on the slides of the Sept 2010 IMA talk, as "Dual: Rosander (1975)" (S12, slide p. 42). This was early in his PhD (2009–2013 per S22).
- The 2010 RAL slides frame it as "Dual: New, even in serial?" (S13, slide 18).
- Hall's later slides credit "Huangfu and H (2011-2014)" and note it was "Suggested by Rosander (1975) but never implemented efficiently in serial" (S19, S20, S22).
- [inferred] The research direction (suboptimization for parallelism) was set jointly with Hall. Hall's earlier PARSMI/ASYNPLEX work used the primal analogue, multiple pricing (S1 pp. 72–73). Huangfu's own contribution was the dual and serial-efficient realisation.

**PE-07. Problem class narrowed to what matters for desktops.** [practice] [stated] primary
- The thesis fixes a target of 8 cores from an Amdahl's-law estimate. Assuming a 30% sequential part, the best possible speedups on 8, 16, 32 and 64 cores are 2.6, 2.9, 3.1 and 3.2: "Therefore, in this research, a choice of 8 cores is assumed." (S1 p. 78.)
- All later results use 8 threads (S7). The HSOL README advises that "OMP_NUM_THREADS=8 is typically a good choice" (S25).

---

## 3. Idea generation

**PE-08. Ideas from anomalies seen while engineering: the hyper-sparsity-promotion episode.** [practice] [stated] primary
- Sequence (APMOD 2012 abstract, S8 p. 2): "After the DSE and BFRT components were implemented in ParISS, cost perturbation was introduced with the aim of mitigating the effects of dual degeneracy." Perturbation then sped things up "strikingly" on the pds problems.
- Thesis numbers for pds-20: 49,913 iterations and 46.2 s without perturbation, 38,517 iterations and 7.6 s with it (S1 p. 60).
- He then measured mechanism variables, not just the outcome:
  - hyper-sparse result rates per component (Table 3.5);
  - per-5000-iteration traces of dense BTRAN results (Fig. 3.2);
  - the count of iterations with actual bound flips: "10672 and 2286 respectively" (S1 p. 61).
- Explanation found: perturbation spreads the BFRT breakpoints, so bound flips reduce the attractiveness of dense rows (S1 pp. 61–63).
- Context: 2011–12, during the serial build.

**PE-09. Generating alternatives directly from the explanation.** [practice] primary
- From the explanation in PE-08 he derived two new pricing variants:
  - partial CHUZR;
  - "less-infeasibility DSE" (LiDSE): |x_i|/w_i instead of x_i²/w_i, generalised to |x_i|^t for 1 ≤ t ≤ 2.
- He tested them on pds-20 and on pds-30 to pds-100 (S1 pp. 63–67, Tables 3.6–3.11).

**PE-10. Need-driven derivation of linear-algebra variants.** [stated] [practice] primary
- The three update variants (APF, MPF, CFT) are "motivated by the requirements of the high performance implementation" (S1 p. 38; S5 p. 6). For example, CFT exists because suboptimization requires several FT updates at once (S1 p. 41).
- The APF first appears on the Dec 2010 RAL slides as a "Little-known (unknown?) alternative product form update [that] may offer a solution" for splitting work between CPU and GPU (S13, slides 29–31).
- By 2013 the APF is used instead to merge several FTRAN-BFRT solves into one inside the CPU-only PAMI (S1 pp. 82–83). The motive changed while the device was kept.
- Context: 2010–13.

**PE-11. Mining competitors' source code and folklore for undocumented techniques.** [practice] primary
- APMOD 2012 on partial CHUZR: "Although the Authors know of no published reference to this technique, it is used within Clp [8]." (S8 p. 5.)
- The 2018 revision adds a comparison with Forrest's Aboca, which was available only as source code and a talk: "Other than making the source code available [5], the authors believe that there is no published reference to this work." (S7 p. 124.)

---

## 4. Experiment design and execution

### 4a. Order of work

**PE-12. Serial code first and simple on purpose, then parallel, then (planned) serial polishing.** [stated] [practice] primary
- Development style (S1 p. 17): C++ was chosen to allow evolution "from a proof-of-idea prototype with simple but less efficient data structures to an efficient elaborated implementation".
- Explicit policy, with its acknowledged shortcut (S1 p. 94): "it has been intended to keep the serial implementation simple so that parallelization can be relatively easily designed and implemented". The shortcut: HSOL runs a BFRT even when no boxed variable exists, "to keep using the same software procedure" (p. 94).
- [inferred] The serial polishing listed as future work seems to have happened between 2013 and 2015. Thesis: HSOL "comparable" with Clp (p. 67). 2018 paper: hsol 2.29× faster than Clp (S7 p. 136). Hardware and Clp version also changed (1.14 → 1.15; E5620 → E5-2670), so the gain cannot be attributed to code changes alone.

**PE-13. Profiling before designing the parallel scheme.** [practice] primary
- Thesis §4.2 first builds a component-level profile of the serial solver on all 30 problems: Table 4.3, with per-iteration time and the percentage per component. It also reasons with Amdahl's law (Fig. 4.3). Only then is PAMI designed (S1 pp. 75–78).
- Design decisions are taken from that profile:
  - CHUZC2 costs 1.5% on average, "Therefore, chuzc2 is not parallelized." (p. 81)
  - The logical-part CHUZC1 runs on one thread beside the data-parallel structural part, because "Again, inspecting the performance profile gives a simple solution." (p. 81)
- Code evidence: `HTimer.h` defines one timer per component (INVERT, CHUZR1, CHUZC0–4, FTRAN, BTRAN, PRICE, FTRAN_DSE, FTRAN_MIX, UPDATE_DUAL/PRIMAL/WEIGHT/FACTOR, UPDATE_ROW_EP), matching the profile tables (S26).

### 4b. Test problems and baselines

**PE-14. Test-set construction with an explicit representativeness argument, filtered for what is meaningful.** [practice] [stated] primary
- **2011 prototype (S3 pp. 5–6).** Started from Netlib + Kennington (114 problems):
  - discarded the 84 solved in under 1 s;
  - of the remaining 30, "ParISS failed to solve 14 in one or more of the runs using 1, 2, 4 and 8 cores";
  - dropped 3 more where ParISS was more than 10× slower than Clp;
  - reported the remaining 13. The filter is stated openly.
- **Jan/Jul 2013 report.** 30 problems from Netlib, Kennington and other public sets. "The claim that the LP test set is representative is based on the range of values for these three measures, as well as problem size." The three measures are fill-in and the shares of hyper-sparse FTRAN and BTRAN results (S5 p. 13).
- **Thesis and 2018 paper.** A "reference set" of 30 problems, mostly from Mittelmann's list, chosen to span:
  - row count;
  - density;
  - column/row ratio, a proxy for PRICE cost;
  - hyper-sparsity (S1 pp. 17–18; S7 p. 132).
  The test files were published as a 90 MB zip, and dcp2 is the group's own problem (Hall's HuHa13 page, S24).
- **2016–17 open-sourcing check (S19 slide 37; S20 slide 9).** 159 problems (98 Netlib, 16 Kennington, 4 industrial, 41 Mittelmann), with 7 "hard" problems excluded and 82 problems under 0.1 s ignored. Reliability is reported separately from performance (S20, slides 10–11).
- **At FICO (2014).** The Xpress parallel-dual deck uses Mittelmann's public LP set (40 instances) plus 120 custom instances (S33). [inferred] This continues his public-benchmark habit, but the deck names no author.

**PE-15. Fairness to baselines: same features off, same pivot path, benchmark not disfavoured.** [practice] primary
- Feature parity: "since hsol and pami have no preprocessing or crash facility, these are not used in the runs with Clp." Cplex is also run "without preprocessing or crash". The Xpress-vs-Cplex comparison is the only one run with presolve and crash, and it is labelled as such (S7 pp. 134, 139–140).
- Controlled comparison of the update methods:
  - Every method replays "the same sequence of basis changes from a 'logical' basis B = I to an optimal solution". This "eliminates variance" from changes in the simplex path (S1 pp. 44–45; S5 p. 15).
  - The FT-derived reinversion schedule is reused for all methods so that the FT benchmark "is not disfavoured" (S1 p. 45; S5 p. 15).
  - The report also justifies why FT, rather than Suhl–Suhl or Reid, is the benchmark (S5 p. 6, July revision).
- Code evidence: `HTester.cpp` (S26) loads a stored pivot "history" (entering column, leaving column, pivot value). It marks reinversion points with (−1, −1) and replays the sequence for FT, PF, MPF, APF and CFT. On each update it checks that the pivot from FTRAN agrees with the pivot from BTRAN plus a dot product, using tolerance 1e-6 scaled by (1 + magnitude) in `diff_double`. It prints the same kinds of statistics as the 2013 report's Tables 1 and 3: geometric-mean fill-in, reinversion interval, shares of hyper-sparse FTRAN/BTRAN results, average result densities, and the INVERT vs solve time split.

### 4c. Parameters, determinism and switches

**PE-16. Parameter choice by sweeping the full test set and taking the middle of the flat region.** [practice] primary
- The PAMI cutoff was swept over 21 values from 1.001 to 0.01 on all 30 problems, reporting the mean speedup and the number of problems above 1.6×, 1.8× and 2×. In the thesis's words, "experiments suggest that the any value in interval [0.9, 0.999] can be chosen as the cutoff ratio", and the median 0.95 was taken (S1 p. 85; S7 Table 2, pp. 130–131).
- Code default `DBLOPT_PAMI_CUTOFF = 0.95` (S26 `HModel.cpp`).
- Reinversion threshold: raised from t_U = t_I in serial to 1.5 t_I in PAMI (S1 p. 84).
- Insensitivity is stated rather than tuned further:
  - "computational experience shows that overall solution time is not sensitive to the reversion [sic] interval so a coarse model is sufficient" (S1 p. 38);
  - "The performance of pami is not sensitive to the thresholds of 5–10% which are used." (S7 p. 131)

**PE-17. Determinism engineered into timing-dependent decisions.** [practice] primary
- "To ensure deterministic performance, in hsol the interval is determined using a flop-based pseudo-clock and practical experience shows that performance is not sensitive to the parameters in the model." (S5 p. 15, July 2013 version.)
- This sentence is not in the January 2013 version (S4 p. 14), so it was added in revision (see V-2).
- The thesis likewise counts operations rather than wall time for t_I and t_U (S1 p. 38).

**PE-18. Adaptive switching instead of fixed strategies.** [practice] primary
- Hyper-sparse CHUZR "is initialized only when the LP problem is found to be hyper-sparse" (S1 p. 54).
- Parallel PRICE/CHUZC is switched off per iteration when e_p has under 1% density, because thread start-up costs more (S1 pp. 81–82). Code: `if (row_ep->count/numRow < 0.01) slice_PRICE = 0` in `HDualMulti.cpp` (S26).
- Factor solves pick hyper-sparse or standard kernels from current and historical density, with separate thresholds per solve type (`hyperFTRANL = 0.15`, `hyperBTRANL = 0.10`, `hyperFTRANU = 0.10`, `hyperBTRANU = 0.15`, `hyperCANCEL = 0.05` in `HFactor.cpp`, S26). Densities are tracked as exponential moving averages (`0.95*old + 0.05*new` in `HDualMulti.cpp` and `HTester.cpp`, S26).
- To avoid an "orphan task", minor iterations are limited to t = s − 1 when bound flips occurred (S1 p. 83).
- Load balance: columns are randomly shuffled before partitioning. "fome13" is used as the extreme case of a well-formed matrix that balances badly (S1 p. 80; S7 p. 127).

### 4d. Debugging and diagnosis

**PE-19. Forensic analysis of single iterations.** [practice] primary
- To explain aggregate behaviour he dissects individual iterations, for example iteration 26,887 of pds-20 (S1 pp. 61–63):
  - the BTRAN result is 15.7% dense;
  - the DSE weight is 8185 against 5323 nonzeros;
  - 12 BFRT candidates fall into 8 Harris groups, with 10 flips identified.
- He also shows the counterfactual: without perturbation, "all the 461 potential choices" collapse at a zero ratio (p. 63).
- He uses Gantt charts with one colour per component, at chosen iterations, to diagnose poor parallel speedup: watson_2 major iteration 20,000; pds-20 major iteration 5,800; dfl001 iteration 10,000 against the same iteration in serial HSOL. The diagnoses were "cheap components" kept serial, load imbalance and memory contention (S1 pp. 87–92, Figs 4.8–4.11).

**PE-20. Tracing a phenomenon to a concrete implementation detail.** [practice] primary
- APMOD 2012, using NETGEN problems because all pivots have unit absolute value: "In ParISS, there was no rule to break this 'second order' tie: the first candidate was chosen and no bound flipping occurred." (S8 p. 4.)
- The choice of NETGEN was itself methodological: they "permit a level of analysis that is intractable in more general LP problems" (S8 p. 3).

**PE-21. Safeguards that recompute and restart when an updated quantity is untrustworthy.** [practice] primary
- Thesis: after BTRAN, the leaving row's DSE weight is recomputed exactly. If the updated weight is much smaller, the row is rejected and CHUZR restarts: "In the implementation, r = 0.5 is used." (S1 p. 54.)
- Code (2017 snapshot) does the same with `if (u_weight >= 0.25 * c_weight) break;` in `HDual.cpp` (S26). See Contradictions C-4.
- Pivot agreement check in the replay harness: see PE-15.

**PE-22. Implementation pragmatism, with simplifications justified by experience.** [practice] [stated] primary
- Only the "exact zero step" part of EXPAND is kept: "implementation experience shows that the exact zero step approach is sufficient" (S1 p. 58).
- The Koberstein–Suhl dual phase-1 subproblem approach is used, with a clarification of the original paper added: boxed variables are fixed at zero, "This point was not clearly expressed in the original paper" (S1 p. 59). Koberstein & Suhl: COAP 37(1):49–65, 2007, DOI 10.1007/s10589-007-9022-3.
- Overlapping INVERT with iterations was left out of PAMI because of the numerical risk Hall & McKinnon had identified, and "because the difficulty of implementation" (S1 p. 84). See F-5.

**PE-23. Writing down hard implementation details that the literature omits.** [practice] [stated] primary
- Two procedures are singled out (S1 pp. 29, 35):
  - forming the row-wise copy of permuted LU factors, which "although it consists of only about 20 lines of code, is particularly hard to write correctly";
  - the Forrest–Tomlin update that keeps hyper-sparsity structures, where the detail "has never been documented before. Therefore, this report fills the gap."
- Both are given as C-style pseudo-code (Figs 2.4–2.10).
- He also adds the missing details of the DFS-based hyper-sparse FTRAN of Gilbert & Peierls "for completeness" (S1 p. 31).

---

## 5. Judging results

**PE-24. Speedup always measured against the best serial code, and normalised by iteration counts.** [stated (co-authored)] [practice] primary
- "A high degree of parallel efficiency would be of little value if it came at the cost of severe serial inefficiency." (S7 p. 134.)
- Both ratios are reported:

  | Source | PAMI8 / PAMI1 (self-relative) | PAMI8 / hsol (best serial) |
  |---|---|---|
  | Thesis (S1 pp. 86, 92) | 2.23 | 1.49 |
  | 2018 paper (S7 pp. 136–138) | 2.34 | 1.51 |

- Iteration counts are checked so that speedups are not flattered: "using solution times as the sole measure of computational efficiency is misleading if there is a significant difference in iteration counts for algorithmic reasons" (S7 p. 134).
  - The best speedups (qap12, stp3d) are rescaled by relative iteration counts, giving 1.74 and 1.75.
  - Only then: "Thus the greater solution efficiency due to exploiting parallelism is genuine." (S7 p. 138)
- Means are geometric. Performance profiles are used throughout (S5, S7).

**PE-25. Slowdowns and failures reported, not hidden.** [practice] primary
- 2011: 14 of 30 non-trivial problems failed in at least one run, and ParISS on one core "was slower by a factor of 2.7 on average" than Clp (S3 p. 6).
- Thesis and 2018 paper:
  - PAMI is slower than HSOL on maros-r7 and Linf_520c ("Parallel pami is not advantageous for all problems", S7 p. 138);
  - SIP slows down most hyper-sparse problems (S1 p. 90; S7 p. 139).
- The SIP scheme itself was motivated by PAMI's failure mode, a worse serial pivoting path (S1 p. 89). It is presented as "frequently complementary to PAMI in achieving speedup when PAMI results in slowdown" (S1 p. 91).
- The FICO 2014 deck likewise bins outcomes, including "Slightly worse" (3 public and 8 custom instances) (S33). This is company evidence; the author is not named.

**PE-26. Limiting the scope of his own techniques.** [practice] primary
- APF: "is not recommended as a valuable general technique" (S1 p. 45; also S5 conclusions). It is kept only for its role inside PAMI.
- Partial CHUZR: "found to be unsuitable for larger pds problems" (S1 p. 66).
- LiDSE: very helpful on pds, but "its scope for further application is fairly limited" (S1 p. 67), because its L1-norm approximation holds only for problems with ±1-like tableau entries.
- 2016 seminar slide, co-presented, assessing the 2015 prize paper: MPF is "Not used by pami! Used by Google in glop" (S19, slide 32). Impact is tracked honestly, including where his own technique did *not* go.

**PE-27. Literature claims tested and reported as not confirmed.** [practice] primary
- Koberstein's weighted cost perturbation (COAP 41(2):185–204, 2008, DOI 10.1007/s10589-008-9207-4): "no further numerical evidence or justification was provided in the original work, nor the expected effect was confirmed by computational experiences during this research" (S1 pp. 58–59).
- The claim about perturbation and sparsity was likewise "neither supported by any numerical results nor got confirmed during this research" (S1 p. 61).

**PE-28. Calibrated commercial comparison.** [practice] [stated (co-authored)] primary
- The thesis's single-authored headline is that PAMI is "comparable with the dual simplex implementation of Cplex" (S1 p. 88; abstract).
- The 2018 paper hedges and splits the claim:
  - "Since commercial LP solvers are now highly developed it is, perhaps, unreasonable to compare their performance with a research code." (S7 p. 139)
  - the claim is restricted to "the better of sip and pami" for "the majority of the test problems" (S7 pp. 139–140);
  - the abstract's headline is superiority over Clp.
- Pre-emptive defence against the objection that the speedup is far from linear: "if such linear speedup were possible then it would have been achieved years ago" (S7 p. 140). See C-1.

**PE-29. Later re-evaluation by others.** [observed] primary (Hall's slides), secondary for Huangfu's process
- Hall, Oct 2021, on PAMI inside the refactored HiGHS:
  - "HiGHS pami solver in serial: solves 34/40 problems";
  - parallel gain over serial dual has geometric mean 1.16 in solution time;
  - "Use pami tactically: switch it off if it is ineffective".
  (S23, slides 25–26.)
- Different code base and test set, so this is not a replication of the 2018 numbers.
- HiGHS still exposes the two schemes as `simplex_strategy` values "2 => Dual (SIP); 3 => Dual (PAMI)" (S27).

---

## 6. Expression and documentation

**PE-30. Algorithms written as code-level pseudo-code, with data structures named.** [practice] primary
- In the thesis, chapter 2 explains linear algebra through C-style pseudo-code with array names (Ustart, Uend, Uindex, Ulookup, URspace and so on). The stated reason: "it is clearer and move [sic] convenient to discuss them by pseudo code" (S1 p. 28).
- Results come as per-problem tables with hyper-sparsity columns, geometric means and performance profiles (S1, S5, S7). Real-time behaviour is shown with per-component colour Gantt charts (S1 Table 4.6).

**PE-31. Terse, user-facing software documentation.**
- HSOL README (S25): a usage block with flags for edge weight (Dan/Dvx/DSE), PAMI cutoff, SIP and partition file, plus an "Observations" section of practical guidance on threads. [practice] primary
- COPT release notes in the commits posted under his name (S29) are one-line items, for example "Introduced LPMETHOD=5 which chooses the best LP solver automatically" (COPT 6.0.3, committed 14 Dec 2022) and "Added CROSSOVER=-1 which runs crossover to cleanup LP solutions" (COPT 6.0.1, committed 4 Nov 2022). Simplex-specific items such as "Revised simplex stalling handling" (COPT 7.0) were posted by the `COPT-Public` account, not by him. [practice] primary; company documentation; authorship of the underlying changes unknown.

---

## 7. Research organisation and collaboration

**PE-32. Division of labour: he builds solver cores, others add the surrounding functionality.** [observed] primary
- HSOL README: "HSOL was originally written by Qi Huangfu, with features such as presolve, crash and advanced basis start added by Julian Hall and Ivet Galabova." (S25.)
- HiGHS README: "HiGHS has primal and dual revised simplex solvers, originally written by Qi Huangfu and further developed by Julian Hall." (S27.)
- 2016–17 slides list the open-sourcing work as Galabova (presolve) and Hall/Galabova (crash, advanced basis) (S19 slide 40; S20 slide 5).
- 2019: slide 6 lists "Primal simplex solver" against the name Huangfu. Slide 13 plans "Add primal simplex solver (Huangfu)" alongside "Resurrect pami" (S22).

**PE-33. Moving research to a commercial solver, then reporting it in the paper.** [stated] [observed] primary
- Blog of 13 May 2014: the Xpress implementation is "an adaption and further development of this key idea", and "As the first commercial parallel simplex solver, it achieves speedup to a factor of two on various large-scale problems." (S9.)
- The 2018 paper adds an Xpress-vs-Cplex profile, run with presolve and crash, and notes independent confirmation in Mittelmann's benchmarks (S7 p. 140).
- Hall 2021: "Huangfu applied the parallel dual simplex techniques within the Xpress solver" (S23, slide 26).
- Context: the Xpress work happened in 2013–14, before the journal paper was submitted (6 Mar 2015).

**PE-34. Public-facing product work at COPT.** [practice] primary
- GitHub commit metadata (S28, S29, S30):
  - 12 commits by "Qi Huangfu" posting COPT release notes and download links, for releases 4.0.7 (29 Apr 2022) through 7.2.1 (18 Oct 2024);
  - 4 more commits in late 2024 by an account named `huangfu7`. That this is the same person is **not verified**;
  - 5 README/version commits to COPT.jl in late April 2022.
- JuliaCon 2022 lightning talk (27 Jul 2022), with the speaker bio: "Qi Huangfu is the developer of COPT and has worked on many different optimization solvers, including HiGHS and FICO-Xpress." (S32.)
- [inferred] His role includes release management and external communication, not only algorithm work. The notes do not show which code he wrote.

**PE-35. Early-career habit: plan vs actual written down honestly (MSc, 2008).** [practice] primary
- MSc Appendix F compares the original plan with what happened (S2 pp. 59–60):
  - porting on ECDF "finally takes about 8 weeks" because of incorrect libraries and licence;
  - "The optimization of the CSMP native parallel code was not carried out, mainly because of two reasons: one is that the porting / profiling phase takes too much time, the other one is that there is not too much parallel code, which has been well developed."
- Same document: a separate Python verification program checks the partitioner's output (S2 §3.5). A third-party library bug that caused deadlocks was diagnosed with the vendor (App. E).
- Context: student project on university HPC clusters. It shows HPC-engineering habits before the simplex PhD.

---

## 8. Failures, abandoned directions and dropped techniques

| # | What | Evidence | Tag |
|---|---|---|---|
| F-1 | **GPU extension of the dual simplex with suboptimization.** Dec 2010 slides plan CPU/GPU work-splitting and introduce the APF for it. Apr 2011: "Scope for combined CPU+GPU solver should be explored". The thesis and all later work are CPU multicore only. Dense or GPU parallel simplex is "excluded from future consideration" (thesis p. 75) | S13 slides 26–31; S14 slide 24; S1 p. 75 | [practice] primary. *Why* it was dropped is [inferred]: no statement found |
| F-2 | **First prototype ParISS (PF update, May 2011).** Failed on 14 of 30 non-trivial problems in at least one run, 2.7× slower than Clp in serial. Rebuilt into ParISS 2.0 by Sep 2011, then HSOL; the 2018 paper says pami "out-performs ParISS by almost an order of magnitude in serial" | S3 p. 6; S15 slides 34–36; S7 p. 126 | [practice] primary |
| F-3 | **Hyper-sparsity promotion / LiDSE line.** APMOD 2012 talk plus a 5-page extended abstract ("Preprint submitted to Elsevier", 29 Mar 2012) and thesis §3.3 ("still at an initial stage", p. 94). No resulting paper appears in Hall's publication list (checked 2026-10-27) or among his arXiv preprints | S8; S1 pp. 59–67, 94; S24; S36 | [practice] primary. Whether it was abandoned or simply never written up is [inferred] |
| F-4 | **Techniques tried and set aside:** partial CHUZR (unsuitable for larger pds), weighted perturbation (effect not confirmed), APF as a general update (not recommended), full EXPAND (exact zero step sufficient) | S1 pp. 45, 58–59, 66 | [practice] primary |
| F-5 | **Overlapping INVERT with iterations** was left out of PAMI (numerical risk and implementation difficulty). A "recompute-and-catchup" FT-based version is proposed as future work. No evidence it was done | S1 pp. 84, 94 | [practice] primary; outcome unknown |
| F-6 | **Replay test harness (HTester) disabled after his departure.** In 2017 it sits behind `#ifdef JAJH_dev`, with a note that its setup "needs to be re-written" if used again | S26 `HTester.cpp` | [observed] primary (Hall's edits) |
| F-7 | **PAMI in HiGHS was on Hall's 2019 plan as "Resurrect pami"**, and in 2021 he advises "Use pami tactically: switch it off if it is ineffective" | S22 slide 13; S23 slide 26 | [observed] primary |

No retracted claims, errata or rejected papers were found (see Gaps).

---

## 9. Early versus final versions (how the work changed under review and over time)

**V-1. PPAM report (12 May 2011) → PPAM talk (13 Sep 2011).** [practice] primary
- The May report shows a weak prototype (PE-25). Four months later the talk reports "ParISS 2.0", summarised as "Average (best) of 18% (50%) relative to 1 core" and "Average (best) of 10% (50%) relative to Clp" (S15 slide 41).
- The talk adds a diagnosis list under "Limits on performance": "Memory bound", "Wasted work", "Load imbalance" and "Inversion of B", the last one annotated "Serial" and "Not overlapped with other operations" (S15 slides 36–40).
- The LNCS published version (DOI 10.1007/978-3-642-31464-3_15) was **not read**, so which numbers went to print is unknown.

**V-2. COAP report, 28 Jan 2013 (S4) → 7 Jul 2013 (S5).** [practice] primary
- Changes made by the sentence-level diff:
  - baselines upgraded from Clp 1.14 / Cplex 11.1 to Clp 1.15 / Cplex 12.4;
  - a solution-time / iteration-count / iteration-time table and a second performance profile (iteration time) added for hsol vs Clp vs Cplex;
  - a paragraph added on the numerical stability of product-form updates ("no numerical instability has been observed" in hsol, S5 p. 10);
  - a justification added for FT as the benchmark over Suhl–Suhl and Reid;
  - the deterministic flop-based pseudo-clock sentence added (PE-17);
  - Table 3 added (average densities) with an "intuitive explanation" of why MPF beats PF and APF.
- Both versions use the same 30 problem names (checked by name).
- [inferred] These look like answers to referee questions about stability, about baseline strength and about whether conclusions carry over to fast solvers. The referee reports are not public.
- Journal: COAP 60(3):587–608, online 23 Aug 2014 (Crossref). The journal text was **not read**.

**V-3. MPC report, ERGO-14-011 = arXiv:1503.01889 v1 (6 Mar 2015) → MPC 2018 (accepted 10 Feb 2016, online 14 Dec 2017).** [practice] primary
- Additions in the journal version:
  - a quantified distinction from the 2011 prototype ("out-performs ParISS by almost an order of magnitude in serial" and "new levels of task parallelism and parallel algorithmic control techniques", p. 126);
  - positioning against Forrest's Aboca, which was available only as source code and a talk (pp. 124, 132);
  - a mention of Wunderling's suboptimization;
  - the sentence on insensitivity to 5–10% thresholds;
  - the missing hardware description;
  - a reference to his own FICO blog post (accessed 20 Jan 2016).
- Editing slips fixed: the report has "The of pami was introduced" and "performed on a workstation with Numerical results".
- arXiv was never updated beyond v1; the CC-BY journal version is the final text.
- [inferred] The ParISS and Aboca additions answer novelty questions from review.

**V-4. Thesis (2013) → MPC paper (2018).** [practice] primary
- Main experiments re-run on new hardware: E5620 → E5-2670, Clp 1.14 → 1.15. The results shift slightly:
  - PAMI vs serial: 1.49 → 1.51;
  - PAMI8/PAMI1: 2.23 → 2.34;
  - SIP: 1.13 → 1.15.
- The cutoff-sweep table is **identical** in both (thesis Table 4.4 = paper Table 2: 1.001 → 1.12; 0.999 → 1.52; and so on), and the paper gives no separate hardware for it.
- [inferred] The sweep was not re-run. Its numbers come from the thesis-era machine while the main results come from the newer one.
- The headline comparison moved from "comparable to a world-leading commercial simplex solver" (thesis abstract) to "superior to that of the leading open-source simplex solver" (paper abstract). See C-1.

**V-5. Test set in the 2013 report vs the thesis.** [practice] primary
- The update-technique experiments use two different 30-problem sets:
  - Jan/Jul 2013 report: includes GEN4, OSA-60, PDS-20, STAT96V1;
  - thesis Table 2.4: instead has dbic1, fome13, nug12, pds-80.
- So the summary ratios differ slightly. MPF over the better of PF and APF: 42% (thesis p. 45) vs 40% (S5 p. 16). FT over MPF: 35% vs 34%. APF worst on 15 vs 16 of 30 problems. The thesis does not mention the difference.

---

## 10. Code evidence summary (what the repositories show)

- **What survives**:
  - HSOL 1.0 (copy at `mattmilten/h2gmp`; `galabovaa/h2gmp` now returns 404). 94 commits from 2017-07-06 to 2018-03-23 by Hall, Galabova and Miltenberger;
  - the HiGHS history, whose first commit `67647f40b0` (2017-07-06) is the same as h2gmp's.
- **No commits** are authored under the name Huangfu in HiGHS (GitHub commit search, 2026-10-27). The original HSOL development (2010–2014) has no public version history (S25, S26, S28).
- **Structure** (S26): one class per concern:
  - `HDual` (serial dual; variants PLAIN/TASKS/MULTI = serial/SIP/PAMI);
  - `HDualMulti.cpp` (PAMI);
  - `HDualRow` (CHUZC/BFRT);
  - `HDualRHS` (CHUZR, infeasibility lists);
  - `HFactor` (LU, hyper-sparse solves, updates);
  - `HMatrix` (row-wise and column-wise A);
  - `HVector` (indexed sparse vectors);
  - `HTimer` (per-component timing);
  - `HTester` (pivot-history replay);
  - `KktCheck` (KKT verification, probably from presolve work).
  This mirrors the component vocabulary of the thesis and papers one to one. [practice] primary; authorship per file not provable.
- **Experiment scaffolding** found in the 2017 snapshot: `SolveAllMl`, `SolveAllQAP`, `TestMl`. These are Hall's scripts (paths under `/home/jajhall/`), **not** evidence of Huangfu's workflow. [observed]

---

## Contradictions (kept, not reconciled)

- **C-1. Headline strength of the commercial comparison.** Thesis abstract and conclusion (single-authored, 2013): PAMI "comparable" to Cplex's dual simplex. 2018 paper (co-authored): comparing a research code with commercial solvers is "perhaps, unreasonable". Only the better of PAMI and SIP is comparable to Cplex "for the majority", and the abstract claims superiority over Clp (S1 p. 88; S7 pp. 119, 139–140).
- **C-2. Serial standing of HSOL against Clp.**
  - Thesis: "comparable with Clp" (S1 p. 67).
  - July 2013 report: hsol "competitive with cplex and clp, both overall and per iteration" (S5 p. 13).
  - 2018 paper: hsol 2.29× faster than Clp (S7 p. 136).
  - Different hardware, Clp versions and possibly code versions.
- **C-3. Density thresholds for switching off data parallelism.**
  - Thesis: a 1% e_p density threshold for PRICE/CHUZC, with "the same switching off consideration" applied elsewhere (S1 p. 82).
  - 2018 paper: "thresholds of 5–10%" for vector operations (S7 p. 131).
  - 2017 code: 1% for sliced PRICE (S26).
  - These may refer to different operations. The texts do not say.
- **C-4. DSE weight-rejection ratio.** The thesis says r = 0.5 (S1 p. 54). The 2017 code rejects only when the updated weight is below 0.25 × the computed weight (S26 `HDual.cpp`). Who changed it, and when, is unknown; Hall's `JAJH_dev` annotations surround that code.
- **C-5. "From scratch" vs continuity.** The thesis says HSOL was "implemented from scratch" (S1 p. 16). The 2012 APMOD abstract calls the group's efficient solver "ParISS … developed by the Authors" (S8). The 2018 paper describes PAMI as the result of "revisions and refinements" of ParISS (S7 p. 126). Whether HSOL is a rewrite or a renamed, refined ParISS is unclear.
- **C-6. Bibliographic details in the authors' own documents.**
  - The COAP paper is cited as 60(4) in the 2016–17 slides (S19, S20) but is 60(3) in Crossref.
  - The prize article is "65 (1), 1-4, 2016" (with DOI prefix "10.1016") on Hall's publication page, but 65(3):541–544, Dec 2016, DOI 10.1007/… in Crossref (S24, S34).
- **C-7. Test sets differ between the 2013 report and the thesis** for the same update experiments (V-5), with slightly different summary percentages.

---

## Gaps (what could not be found or verified)

- **Unread published versions**: the COAP 2015 journal text, the LNCS 2012 text and the COAP 2015 Best Paper Prize article (DOI 10.1007/s10589-016-9882-5). The prize article is described on Hall's page as written by Huangfu and Hall "about the work leading to the award". It is probably the richest first-person process account, but there is no open-access copy and Springer redirects to a login, so it was **not read**. The Edinburgh Pure copy of the PPAM paper is the wrong file (a 37-page slide deck).
- **No referee reports or rebuttals** exist publicly (no OpenReview in this field). The reasons given for revisions in V-2 and V-3 are inferred.
- **No pre-2017 version history of HSOL.** How he debugged and tested day to day (test scripts, regression suites) during 2009–2014 cannot be seen. The thesis's LaTeX source on ERA returned an HTML page instead of the archive and was not read; no access controls were bypassed.
- **FICO period (2013–2018)**: no Huangfu-authored technical document beyond the 2014 blog post. The FICO benchmark deck (S33) names no author. An Edinburgh news item from September 2014 surfaced by WebSearch returned HTTP 403 (not read).
- **COPT period**: no paper, talk transcript or design document by him on COPT's simplex was found. The JuliaCon 2022 video was not watched. The COPT User Guide (arXiv:2208.14314) was not read beyond its metadata. His role in the cuPDLP-C report (9 authors) is unknown, and he has no commits in its repository. His start date at Cardinal Operations is not established.
- **Identity of the GitHub account `huangfu7`** is not verified.
- **Publication landscape**: the DBLP page for pid 116/5281 is behind a bot challenge (Anubis), which blocks both curl and WebFetch. OpenAlex merges him with a Zhejiang University medical researcher (author A5074771751). The arXiv author search, Hall's publication list and Crossref were used instead.
- **Retractions, errata, rejected submissions**: none found. Absence is not evidence they do not exist.
- **Who presented the co-authored talks**: slide footers show Hall on several (ICCOPT13, INFORMS19, KTH21). For most co-authored decks the presenter is unknown, so "stated" slide content is weak evidence of Huangfu's personal views.
- **EUROPT17 and the APMOD12 slides** were downloaded but not read. NLAO14, NLAO16 and OR18 were only scanned for mentions.

---

## Sources

Primary documents: by or with Huangfu, his code, and records of his work.

- **S1**. Q. Huangfu, *High performance simplex solver*, PhD thesis, University of Edinburgh, 2013. hdl:1842/7952. PDF https://era.ed.ac.uk/bitstreams/89189894-a7d5-4c7f-bf31-752301865c26/download. Primary, read in full (99 pp.).
- **S2**. Q. Huangfu, *Optimization of a large-scale parallel finite element - finite volume C++ code*, MSc in HPC dissertation, University of Edinburgh, 22 Aug 2008. https://static.ph.ed.ac.uk/dissertations/hpc-msc/2007-2008/Qi_Huangfu.pdf. Primary, partly read (contents, App. E–F).
- **S3**. J. A. J. Hall, Q. Huangfu, *A high performance dual revised simplex solver*, Tech. Rep. ERGO-11-007, 12 May 2011. https://webhomes.maths.ed.ac.uk/hall/HaHu11/ERGO-11-007.pdf. Published PPAM 2011 Part I, LNCS 7203, 143–151, 2012, DOI 10.1007/978-3-642-31464-3_15. Primary, report read in full; LNCS text not read.
- **S4**. Q. Huangfu, J. A. J. Hall, *Novel update techniques for the revised simplex method*, ERGO-13-001, version of 28 Jan 2013. Optimization Online 2013/02/3774, https://optimization-online.org/2013/02/3774/. Primary, results read and diffed.
- **S5**. Same title, ERGO-13-001 version of 7 Jul 2013. https://webhomes.maths.ed.ac.uk/hall/HuHa12/ERGO-13-001.pdf. Published Computational Optimization and Applications 60(3):587–608, 2015, DOI 10.1007/s10589-014-9689-1. Primary, report read; journal text not read.
- **S6**. Q. Huangfu, J. A. J. Hall, *Parallelizing the dual revised simplex method*, ERGO-14-011, 6 Mar 2015. https://webhomes.maths.ed.ac.uk/hall/HuHa13/ERGO-14-011.pdf. Also arXiv:1503.01889 (v1 only). Primary, read and diffed.
- **S7**. Same title, Mathematical Programming Computation 10(1):119–142, 2018 (received 6 Mar 2015, accepted 10 Feb 2016, online 14 Dec 2017), DOI 10.1007/s12532-017-0130-5, CC BY 4.0. Primary, read in full.
- **S8**. J. A. J. Hall, Q. Huangfu, *Promoting hyper-sparsity in the revised simplex method*, extended abstract, APMOD 2012, Paderborn (talk 28 Mar 2012). https://webhomes.maths.ed.ac.uk/hall/APMOD12/APMOD12_ExtendedAbstract.pdf. Primary, read in full.
- **S9**. Q. Huangfu, *The Algorithm that Runs the World*, FICO Blog, 13 May 2014. Wayback snapshot 2017-08-03: http://web.archive.org/web/20170803233453/http://www.fico.com:80/en/blogs/analytics-optimization/the-algorithm-that-runs-the-world. Primary [stated], read.
- **S10**. D. Ge, Q. Huangfu, Z. Wang, J. Wu, Y. Ye, *Cardinal Optimizer (COPT) User Guide*, arXiv:2208.14314 (v1 2022-08-30, v4 2026-01-30). Primary, metadata only.
- **S11**. H. Lu, J. Yang, H. Hu, Q. Huangfu, J. Liu, T. Liu, Y. Ye, C. Zhang, D. Ge, *cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language*, arXiv:2312.14832 (v1 2023-12-22, v2 2024-01-07). Primary, abstract only.
- **S12**. J. Hall, E. Smith, Huangfu Qi, *Towards a practical parallelisation of the revised simplex method*, IMA NLAO talk slides, 14 Sep 2010. https://webhomes.maths.ed.ac.uk/hall/IMA-NLAO_10/IMA-NLAO_10.pdf. Primary (co-authored slides), scanned.
- **S13**. J. Hall, Q. Huangfu, E. Smith, *A high performance dual revised simplex solver*, Oxford/RAL seminar, 2 Dec 2010. https://webhomes.maths.ed.ac.uk/hall/RAL10/RAL10.pdf. Primary, slides 16–31 read.
- **S14**. J. Hall, Q. Huangfu, E. Smith, *High performance computing and the simplex method*, LANCS workshop, 12 Apr 2011. https://webhomes.maths.ed.ac.uk/hall/Lancs11/Lancs11.pdf. Primary, scanned.
- **S15**. J. A. J. Hall, Q. Huangfu, *A high performance dual revised simplex solver*, PPAM 2011 talk, 13 Sep 2011. https://webhomes.maths.ed.ac.uk/hall/PPAM11/PPAM11.pdf. Primary, results and summary read.
- **S16**. Q. Huangfu, J. Hall, M. Lubin, E. Smith, *Parallelizing the (revised) simplex method: Is it time to give up?*, ICCOPT 2013, 1 Aug 2013. https://webhomes.maths.ed.ac.uk/hall/ICCOPT13/ICCOPT13.pdf. Primary (Hall named in footer), relevant slides read.
- **S17**. J. Hall, Q. Huangfu, M. Lubin, *Parallel implementation of the dual revised simplex method for large-scale LP problems*, NLAO14 slides, 4 Sep 2014. https://webhomes.maths.ed.ac.uk/hall/NLAO14/NLAO14.pdf. Primary, scanned.
- **S18**. Q. Huangfu, J. Hall, *Parallelizing the dual revised simplex method*, NLAO16 slides, Sep 2016. https://webhomes.maths.ed.ac.uk/hall/NLAO16/NLAO16.pdf. Primary, scanned.
- **S19**. Q. Huangfu (FICO), J. Hall, *Novel update techniques for the revised simplex method (and their application)*, ERGO seminar, 30 Nov 2016. https://webhomes.maths.ed.ac.uk/hall/ERGO_301116/ERGO_301116.pdf. Primary, read in full.
- **S20**. J. Hall, Q. Huangfu (FICO), I. Galabova, *An open-source high performance dual simplex solver*, SIAM OP17, 22 May 2017. https://webhomes.maths.ed.ac.uk/hall/SIOPT17/SIOPT17.pdf. Primary, read in full.
- **S21**. J. Hall, Q. Huangfu, I. Galabova, L. Schork, M. Feldmeier, *HiGHS: A High-Performance Linear Optimizer*, OR60, Sep 2018. https://webhomes.maths.ed.ac.uk/hall/OR18/OR18.pdf. Primary, scanned.
- **S22**. J. Hall, *HiGHS: a high-performance linear optimizer*, INFORMS Seattle, 21 Oct 2019. https://webhomes.maths.ed.ac.uk/hall/INFORMS-HiGHS19/INFORMS-HiGHS19.pdf. Primary document; [observed] evidence about Huangfu.
- **S23**. J. Hall, *HiGHS: Theory, software and Impact*, KTH, 1 Oct 2021. https://webhomes.maths.ed.ac.uk/hall/KTH21/KTH21.pdf. Primary document; [observed].
- **S24**. J. A. J. Hall, web pages: home, Publications.html, Talks.html, HuHa13/, HuHa12/, HaHu11/, COAP_Prize_2015/, PublicLP/ (https://webhomes.maths.ed.ac.uk/hall/), accessed 2026-10-27. Primary record.
- **S25**. HSOL 1.0 / h2gmp (README.md, src/, check/; 94 commits 2017-07-06…2018-03-23), https://github.com/mattmilten/h2gmp (the `galabovaa/h2gmp` original returns 404). Primary code.
- **S26**. HiGHS repository at first commit `67647f40b0` (2017-07-06): `HTester.cpp`, `HTimer.h`, `HDualMulti.cpp`, `HDual.cpp`, `HFactor.cpp`, `HModel.cpp`, `HApp.cpp`, scripts. https://github.com/ERGO-Code/HiGHS/tree/67647f40b0. Primary code; line-level authorship unknown.
- **S27**. HiGHS `README.md` and `docs/src/options/definitions.md` (master, accessed 2026-10-27), https://github.com/ERGO-Code/HiGHS. Primary documentation, [observed].
- **S28**. GitHub commit-search API: author-name "Qi Huangfu" (17 commits, COPT-Public org) and `repo:ERGO-Code/HiGHS author-name:Huangfu` (0), accessed 2026-10-27. Primary metadata.
- **S29**. COPT-Release repository (README-40…72, README.md; 68 commits), https://github.com/COPT-Public/COPT-Release. Primary, company release notes.
- **S30**. COPT.jl repository, https://github.com/COPT-Public/COPT.jl (Huangfu commits Apr 2022). Primary metadata.
- **S31**. cuPDLP-C repository, https://github.com/COPT-Public/cuPDLP-C (commit authors; none by Huangfu). Primary metadata.
- **S32**. JuliaCon 2022, *COPT and its Julia interface* (lightning talk, 27 Jul 2022), https://pretalx.com/juliacon-2022/talk/XRDNVT/. Primary (speaker bio); video not watched.
- **S33**. FICO, *The parallel dual simplex method* (Xpress 7.6 vs 7.7 benchmark slides, © 2014, PDF created 10 Nov 2014), https://msi-jp.com/xpress/doc/Xpress-ParallelSimplex-Performance.pdf. Primary company document; author not named.

Secondary sources, metadata and attempts:

- **S34**. Crossref API records for DOIs 10.1007/s12532-017-0130-5, 10.1007/s10589-014-9689-1, 10.1007/978-3-642-31464-3_15 and 10.1007/s10589-016-9882-5, plus bibliographic checks of cited works. Cited works: Bixby & Martin 2000, DOI 10.1287/ijoc.12.1.45.11902; Rosander 1975, DOI 10.1007/bfb0120714; Koberstein 2008, DOI 10.1007/s10589-008-9207-4; Koberstein & Suhl 2007, DOI 10.1007/s10589-007-9022-3; Hall & McKinnon 2005, DOI 10.1007/s10589-005-4802-0; Lubin, Hall, Petra & Anitescu 2013, DOI 10.1007/s10589-013-9542-y. Secondary metadata.
- **S35**. Unpaywall API (DOIs in S3, S5, S40): OA status. Secondary metadata.
- **S36**. arXiv API (1503.01889, 2208.14314, 2312.14832; author search "Huangfu"). Secondary metadata.
- **S37**. Optimization Online: author page https://optimization-online.org/author/qi-huangfu/ and entry 2013/02/3774. Secondary record.
- **S38**. ERA landing page hdl:1842/7952. The thesis PDF downloaded; the LaTeX-source bitstream returned HTML, not read. Secondary record.
- **S39**. OpenAlex author A5074771751. This record conflates Huangfu with a medical researcher; it surfaced S2. Secondary metadata.
- **S40**. *COAP 2015 Best Paper Prize*, Computational Optimization and Applications 65(3):541–544, Dec 2016, DOI 10.1007/s10589-016-9882-5. **Not read** (no OA copy).
- **S41**. Edinburgh Research Explorer (Pure) file for the PPAM paper, https://www.pure.ed.ac.uk/ws/files/17773114/A_high_performance_dual_revised_simplex_solver.pdf. Contains a slide deck, not the paper; not used.
