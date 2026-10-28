# Qi Huangfu: Peer Critique (blind spots, limits, contested judgements)

| Field | Value |
|---|---|
| Researcher | Qi Huangfu. PhD University of Edinburgh 2013 ("High performance simplex solver", advisor J. A. J. Hall); original author of HSOL, the dual revised simplex code that became the simplex core of HiGHS; at FICO (Xpress simplex) by May 2014 and on FICO-affiliated slides in 2016–2017; co-author of the COPT User Guide (Cardinal Operations) from 2022 and Cardinal Operations affiliation on cuPDLP-C (2023/24). Not the Zhejiang University medical researchers of the same name |
| Dimension | Research agent 05 of 06: peer critique. Covers outside objections, self-conceded limits, the fate of his code in the successor solver, benchmark evidence, rival schools, misreadings by citers, and how each was answered |
| Research date | 2026-10-27 |
| Sources consulted | 44 (27 primary, 17 secondary), listed under "Sources" |
| WebSearch calls | 1 (of 5 allowed) |
| User-supplied material | None. `references/sources/{papers,talks,essays,software}/` hold only `.gitkeep`. `private/` was not opened. **Nothing in this file is from user-supplied material.** |
| Transcripts saved | None by this agent. One caption transcript saved in this run by another agent (JuliaCon 2022) was read and is cited in §9. Slide decks stay unsaved because they are copyrighted |
| Language | English (per team.json) |

**Tags.**
- [stated]: said by Huangfu, or in a paper, slide deck, blog or manual he authored or co-signed.
- [practice]: what his papers, code, test sets or records show was done.
- [observed]: what a third party wrote. This includes **J. A. J. Hall speaking alone** (his advisor and co-author, later the HiGHS lead). Hall is not an outside critic, and each such item is flagged "co-author".
- [inferred]: my reading. The basis is given; do not quote it as anyone's view.
- (P) primary: the critic's or Huangfu's own text, read at the page or slide cited. (S) secondary: an aggregator, an abstract only, or a quotation seen only as a Semantic Scholar citation context ("S2 context; full text not read").

**How the critiques were found.**
1. Huangfu's works were identified with Crossref and the arXiv API. DBLP pid 116/5281 sat behind a bot wall, and OpenAlex merges him with a Zhejiang medical author (record A5074771751, 16 works, 3 of them his).
2. I pulled Semantic Scholar citation contexts for five works: MPC 2018 (653 citing records), COAP 2015 (12), PPAM 2011 (11), the COPT User Guide (67) and cuPDLP-C (49). I filtered them for critical wording.
3. I opened every critic quoted below in full text (arXiv, PMLR, open-access PDFs), except lines marked "S2 context".
4. I read the Huangfu-side texts the critiques target: the published MPC article and its arXiv v1, the thesis, the 2014 FICO blog, and co-presented slides.
5. I checked what happened to his code in HiGHS: docs history, issues and source at master `73cac48`.
6. I checked independent benchmark pages (Mittelmann; Wayback snapshots for past years) for context only.
Paywalled texts without a legal open copy were not read, and no login or paywall was bypassed (one Springer link redirected to an authorization endpoint and was not followed).

**Co-authorship and attribution caveats.**
- **Joint work.** Every simplex paper Huangfu published is joint with Hall, his supervisor. A critique of "Huangfu and Hall (2018)" targets the pair.
- **Citations mostly mean "we used HiGHS".** The MPC 2018 paper is what HiGHS users are asked to cite. Of the 421 citing records with contexts, 327 mention only HiGHS as a tool. Only 23 discuss parallel simplex at all (16 without HiGHS, 7 with it). Citations grew with HiGHS adoption: 61 (2023), 91 (2024), 166 (2025), 262 (2026). [practice, (S): S2 harvest, keyword classification by me]
- **Complaints about HiGHS are not complaints about Huangfu.** Most are about later HiGHS components (MIP, IPM, presolve) and are **not** attributed to him here. For example, arXiv:2603.28943 reports HiGHS "shows severe scalability issues starting at instance 4" on a MIP scheduling set (S2 context). Exceptions are made only where the complaint concerns the dual simplex, PAMI or SIP.
- **Multi-author COPT work.** COPT and cuPDLP-C have many authors in non-alphabetical order. Huangfu's personal role in any particular claim there is **not established**.

---

## 0. Summary for Phase 2

| # | Recurring critique (blind spot / limit) | Raised by | Huangfu-side answer | Status |
|---|---|---|---|---|
| Q1 | **Parallel speed-up of the dual revised simplex is small.** About 1.5× over the serial code on 8 cores, and "limited" scalability | Koch–Berthold–Pedersen–Vanaret (2022); Lange–Swoboda (2021); Thuerck et al. (2023); Lu (2024); self ("Though not extremely impressive", thesis 2013) | Pre-emptive defence in the paper: linear speed-up is "unreasonable" to expect; quality is measured by beating Clp and by FICO adopting the ideas | Substance conceded on both sides. No published reply by Huangfu to any critic found |
| Q2 | **Limits of applicability.** The bounds are memory bandwidth, serial INVERT, and "cheap components" left serial on hyper-sparse LPs. Thread counts beyond about 8 do not help. The benefit concentrates on LPs with many more columns than rows | Self (thesis p. 88; ICCOPT13 slides); Hall (co-author) in HiGHS docs and issues | Overlapped INVERT proposed as future work (thesis p. 94). Not found implemented | Open. The narrowed scope is now documented by HiGHS |
| Q3 | **Fate in the open-source successor.** PAMI and SIP are off by default in HiGHS and unmaintained. They are "not often faster" than the improved serial solver, and a stall has been reported | Hall (co-author) 2021–2026; HiGHS docs 2023–2026; user bug reports #780, #2991 | Hall: "Use pami tactically: switch it off if it is ineffective" (2021) | Unresolved. PAMI issue collated in open issue #3395 (Oct 2026) |
| Q4 | **Evaluation design.** Baselines were run without presolve or crash; a research code was compared with a commercial one; one test LP (dcp2) is not public; only 1 and 8 cores were reported; promotional framing appeared in the preprint | [inferred] from the texts; Galabova–Hall (2020) on dcp2; arXiv-to-journal revision | The authors themselves call the Cplex comparison "perhaps, unreasonable". The journal version drops the FICO-advertising sentences | Partly answered |
| Q5 | **Commercial-standing claims disputed.** "Comparable with Cplex", "now fastest commercial simplex solver" vs "commercial solvers outperform it with sequentially executed implementations". Mittelmann's July 2017 table ranks Gurobi ahead of Xpress | Abbas–Swoboda (2022); Mittelmann snapshot (context) | Hall (2021): Xpress simplex "best in the world" for "much of 2013-2018" | Contradiction kept |
| Q6 | **Suboptimization is a weaker pivot rule.** It needs a tuned cutoff and wastes computation. Serial PAMI is slower and, in HiGHS, less reliable (34/40 solved) | Self (MPC p. 140; thesis p. 86); Hall KTH21 slides | Candidate-quality cutoff (0.95) | Accepted limitation |
| Q7 | **First-order/GPU rival school.** Factorization-based simplex does not scale, and its multicore gains are "minimal" | Lu (2024); cuPDLP-C (2023, **co-signed by Huangfu**) | Huangfu co-signs the rival thesis while COPT keeps multi-threaded dual simplex as its default LP method (guide v8.0.1, 2026) | He sits in both camps. No reconciling statement found |
| Q8 | **Citers misread the PAMI numbers.** Claims include "pricing-only" parallelism, speed-ups "minimal after two or three cores", and "65% of the execution effectively parallelized" | Lu (2024); Mai et al. (2024) | None found | Phase 2 should cite the 1.51× figure (vs serial hsol), not 2.34× (pami8 vs pami1) |

---

## 1. Era and resource context

- **PhD (Edinburgh, thesis 2013).** [practice, P]
  - The code was C++ with OpenMP (HSOL 1.0 README).
  - The team was Huangfu and his supervisor Hall, with Edmund Smith and Miles Lubin (Argonne) on neighbouring parallel-simplex projects (ICCOPT13 title slide).
  - The test set was "a reference set of 30 LP problems", most from Mittelmann's list (MPC 2018 §5.1).
  - Hardware is described differently in the two versions (see Contradictions C12). The arXiv v1 says "a workstation with 16 (Intel Xeon E5620, 2.4GHz) processors, using eight for the parallel calculations" (p. 17). The journal says "a workstation with two Intel Xeon E5-2670s, 2.6 GHz (16 cores, 16 threads in total), using eight threads for the parallel calculations" (p. 133).
  - The setting was a desktop shared-memory machine, by deliberate choice. "Now, when every desktop computer is a multi-core machine, any speedup is desirable in terms of solution time reduction for daily use" (MPC arXiv v1 p. 2).
- **FICO (Xpress).** [practice, P]
  - The FICO blog post "Posted by Qi Huangfu" is dated 13 May 2014.
  - The KDnuggets author note calls him "the 'simplex guy' behind the FICO Xpress Optimization Suite" (13 June 2014).
  - The NLAO16 (Sept 2016) and SIOPT17 (May 2017) slides list his affiliation as FICO.
  - The Xpress code is closed. Only the papers, blog and slides describe it.
- **Cardinal Operations (COPT).** [practice, P]
  - He is co-author of the COPT User Guide (arXiv:2208.14314, v1 Aug 2022; v4 Jan 2026 for COPT 8.0.1).
  - His affiliation is "Cardinal Operations" on cuPDLP-C (arXiv:2312.14832v2, Jan 2024).
  - COPT is closed source. This is the GPU / first-order era (from 2023).
- **Seniority over time.** [inferred] He was a PhD student in the Edinburgh years, then an industrial solver developer. The Crossref and arXiv name queries run here found no single-author research paper by him after the thesis. His later public voice is a 2014 blog and co-signed product documents or papers. This is a limited search; agent 06 owns the full trajectory.

---

## 2. Is the parallel dual simplex worth it? (PAMI/SIP; thesis 2013, MPC 2018) (Q1)

### 2.1 What Huangfu and Hall claimed and conceded [stated, P]

- **Starting premise.** MPC 2018 p. 120: "Indeed, since scalable speedup for general large sparse LP problems appears unachievable, the revised simplex method has been considered unsuitable for parallelisation." The paper then argues that "any improvement in performance due to exploiting parallelism in the revised simplex method is a worthwhile goal."
- **The headline numbers.** MPC p. 138: "For more than 65% of the reference set pami is twice as fast in parallel, with a mean speedup of 2.34. However, relative to hsol, some of this efficiency is lost due to overcoming the wasted computation, lowering the mean relative solution time to 1.51." SIP: "mean speedup (1.15) of sip is inferior to that of pami. This is because sip exploits only limited parallelism" (p. 139).
- **The defence, written into the conclusion.** MPC p. 140: "Although the results in this paper are far from the linear speedup which is the hallmark of many quality parallel implementations of algorithms, to expect such results for an efficient implementation of the revised simplex method applied to general large sparse LP problems is unreasonable. The commercial value of efficient simplex implementations is such that if such linear speedup were possible then it would have been achieved years ago."
- **Self-assessment in the thesis.** Thesis p. 94: "For the reference set, PAMI provides an average speedup of 1.49. Though not extremely impressive, the performance of PAMI is comparable to the dual simplex implementation of Cplex, which is a world-leading commercial simplex solver."
- **The group's own verdict in 2013.** ICCOPT 2013 slides "Parallelizing the (revised) simplex method: Is it time to give up?" (authors Huangfu, Hall, Lubin, Smith; speaker Hall), slide 22:
  - "No "silver bullet" for general parallel simplex"
  - "Is this problem/method/architecture environment relevant?"
  - "Parallel research has yielded serial results", listing "Novel update techniques", "Insight into promoting hyper-sparsity", "Novel edge weight strategies" and "Huangfu's c++ solver hsol".
- [inferred] The team said before any outside critic did that the parallel gains were modest and that the lasting value lay in the serial solver. The outside critiques below repeat that verdict. They do not overturn a stronger claim.

### 2.2 Outside critics [observed]

- (P) **Koch, Berthold, Pedersen, Vanaret**, "Progress in mathematical programming solvers from 2001 to 2020", EURO J. Comput. Optim. 10 (2022) 100031, DOI 10.1016/j.ejco.2022.100031. arXiv:2206.09787v2 p. 13: "The parallelization of the barrier methods improved, and there exists nowadays a parallel variant of the simplex algorithm, although its scalability is limited [18]." Reference [18] is Huangfu & Hall MPC 2018. Note: co-author Berthold's affiliation is "Fair Isaac Germany GmbH" (p. 1). So a FICO author co-signs "limited", about the technique FICO adopted.
- (P) **Lange & Swoboda**, "Efficient Message Passing for 0–1 ILPs with Binary Decision Diagrams", ICML 2021, PMLR 139, 6000–6010 (arXiv:2009.00481v2, pp. 2–3): "Solving LP relaxations, which consumes a considerable portion of the overall computation time, is particularly difficult to parallelize. Although there have been efforts to exploit parallelization in the (dual) simplex method (Huangfu & Hall, 2018), the performance improvement over leading sequential implementations is relatively small (Gurobi Optimization, LLC, 2020)."
- (P) **Abbas & Swoboda**, "FastDOG: Fast Discrete Optimization on GPU", CVPR 2022, 439–449, DOI 10.1109/CVPR52688.2022.00053 (arXiv:2111.10270, p. 2): "The simplex method is less straightforward to parallelize. The work [28] reports a parallel implementation, however current state-of-the-art commercial solvers outperform it with sequentially executed implementations." [28] = Huangfu & Hall 2018. See C2 for the clash with the authors' Cplex comparison.
- (P) **Thuerck, Sofranac, Pfetsch, Pokutta**, "Learning Cuts via Enumeration Oracles", NeurIPS 36 (2023) 79108–79123, DOI 10.52202/075280-3461 (arXiv:2305.12197v2, p. 10): "Solving LPs has proved to be notoriously hard to parallelize, with only minor performance improvements reported in literature to date [40, 45]." [40] is Hall's 2010 survey (Comput. Manag. Sci. 7:139–170, as listed in their references); [45] is Huangfu & Hall 2018.
- (P) **Lu**, "First-Order Methods for Linear Programming", arXiv:2403.14535v1 (2024), p. 1: "For simplex, multiple cores are generally employed only in the "pricing" step that selects variables entering or leaving the basis, and the speedups are generally minimal after two or three cores [25]." [25] = Huangfu & Hall 2018. This item is from the first-order rival school (§8.4). Its fidelity to the cited source is examined in §10.
- (S) Readers outside the core LP community were **favourable**:
  - Mamalis & Perlitis, IJACSA 8(4) (2017), DOI 10.14569/IJACSA.2017.080449 (S2 context): "they have obtained speedup values comparable to those of the best commercial simplex solvers".
  - Mamalis & Pantziou, LNCS (2015) 281–307, DOI 10.1007/978-3-319-24024-4_17 (S2 context): "Till recently, no other valuable attempts have been made to parallelize the dual revised simplex method".
  - These authors build GPU or hybrid standard-simplex codes, so they are a sympathetic audience.

### 2.3 How it was answered

- [practice, P] **No reply found.** I found no published reply, comment, blog or talk by Huangfu answering any of these critics. The only defence is the pre-emptive one in the paper itself (p. 140).
- [practice, P] **Industrial adoption offered as validation.** In place of independent benchmarks, the paper offers adoption. MPC pp. 140–141: "A measure of the quality of the pami and sip schemes discussed in this paper is that they have formed the basis of refinements made by Huangfu to the Xpress solver which have been considered noteworthy enough to be reported by FICO."
- [observed, P] **Co-author's later answer in practice.** Hall stopped promoting the parallel solver (§4).

---

## 3. Limits of applicability (Q2)

- [stated, P] **Diagnosis of earlier codes (thesis pp. 75–76).** He explains the poor speed-up of earlier parallel revised simplex codes by three causes:
  - "1. Limited parallelization": Bixby and Martin's parallel components account for "less than 35%", "so that by Amdahl's Law, the best possible speedup is limited to 1.5 on average".
  - "2. Inferior pivoting rule and memory bound": "when many ftran (or btran) operations are performed in parallel, the competition for memory access will highly limit the parallelization efficiency".
  - "3. Cheap computational components".
- [inferred] The three causes he names for **others'** codes are the same bounds that later limit PAMI: memory, the serial share, and cheap components. They are spelled out in the next three bullets.
- [stated, P] **The major limitation, in his words (thesis p. 88).** "This illustration shows one major limitation of PAMI, that when the LP problem is hyper-sparse, then "cheap components" chuzr, price, chuzc (merely visible between btran and ftran) and even update-primal are all performed sequentially to avoid slowdown from the parallelization overhead. This arrangement inevitably limits the overall speedup as it is obviously counted as the sequential proportion in Amdahl's Law."
- [stated, P] **Serial INVERT and slow problems.**
  - MPC p. 138: "Parallel pami is not advantageous for all problems. Indeed, for maros-r7 and Linf_520c, pami is slower in parallel than hsol." Also, invert "runs in serial on one processor with no work overlapped."
  - ICCOPT13 slide 12 names the limits as "Memory bandwidth" and "Serial computation during INVERT". Slide 14 (SIP) names "Memory bandwidth" and "Amdahl's law".
- [stated, P] **SIP on hyper-sparse LPs.** MPC p. 139: "The worst cases when using sip are associated with the hyper-sparse LP problems where sip typically results in a slowdown."
- [observed, P; co-author] **Hall's later scoping in HiGHS.**
  - HiGHS docs `docs/src/parallel.md`, unchanged from the first docs commit (444998d, 2023-03-13) to the `latest` branch (2026-10-27): "Unless an LP has significantly more variables than constraints, the parallel dual simplex solver is unlikely to be worth using."
  - The live page adds on threads: "it is unlikely to be more than eight due to most computation in HiGHS being memory-bound."
  - Issue #477 (2021-03-03): "At best, speed-up is limited to the number of memory channels, rather than the number of cores." In the same comment he says parallel dual simplex was "available in HiGHS under Linux - only, I think, due to problems using OpenMP on Windows (and Mac?)". That is a portability cost of the original OpenMP design.
  - Issue #1192 (2023-03-03): "Parallel simplex is generally only a little faster, and will reduce beyond 4-8 threads."
- [inferred] **The scope narrowed toward the rival's regime.** The HiGHS rule ("significantly more variables than constraints") is the n ≫ m regime in which Bixby and Martin's data-parallel PRICE already gave "significant speed-up" (ICCOPT13 slide 9: "When n ≫ m significant speed-up was achieved — Bixby and Martin (2000)"). The general-purpose ambition of PAMI ("general large scale sparse" LPs, MPC abstract) has, in the successor code, been scoped back to the rival's niche.
- [practice] **Planned fix not found.** The thesis future work (p. 94) proposed overlapping INVERT: "One reason for the relative poor speedup of PAMI is that the time-consuming sequential LU factorization is not overlapped with the simplex iterations." A keyword search of HiGHS master (catch-up / overlapped invert) found no implementation. Whether Xpress or COPT did it is **not known** (closed source).

---

## 4. What happened to PAMI and SIP in HiGHS (Q3): the closest thing to a replication

**Context.** HiGHS grew out of HSOL. The HSOL 1.0 README: "HSOL was originally written by Qi Huangfu, with features such as presolve, crash and advanced basis start added by Julian Hall and Ivet Galabova." [practice, P] Huangfu was at FICO, then Cardinal Operations, during the HiGHS years. Every statement below is by others about his code.

- [practice, P] **Default and option values.** HiGHS option `simplex_strategy`: "0 => Choose; 1 => Dual (serial); 2 => Dual (SIP); 3 => Dual (PAMI); 4 => Primal". The default is `kSimplexStrategyDual` (HighsOptions.h, master `73cac48`). Docs: "By default, the HiGHS dual simplex solver runs in serial."
- [observed, P; co-author] **The verdict in the docs (2023–2026).** "The speed-up achieved using the dual simplex solver is normally bounded by the number of memory channels in the architecture, and typically less than the values achieved by Huangfu and Hall. This is because enhancements to the serial dual simplex solver in recent years have not been propagated to the parallel solver."
- [observed, P; co-author] **Hall in issues.**
  - #780 (2022-03-25), after a user's LP failed with `parallel=on`: "I fear that we may have to disable parallel simplex, as it's hard to maintain and, as features are added to the serial solver, the chance of getting better performance with the parallel code reduces." The bug was fixed by #924 (2022-07-27).
  - #1192 (2023-03-03): "Indeed, since the parallel simplex solver lacks some features that I've added to improve the serial solver, it may even be slower."
  - #1547 (2023-12-12): "Running the dual simplex solver in parallel - particularly for a problem of this size - is of questionable value".
  - #2913 (2026-03-14): "No, PAMI is not often faster than the serial dual simplex solver, because not all the enhancements I've made to the latter have also been extended to PAMI."
- [observed, P; co-author] **Re-measurement in HiGHS.** Hall, "HiGHS: Theory, software and Impact", KTH, 1 Oct 2021, slides 25–26:
  - "HiGHS pami solver in serial: solves 34/40 problems".
  - Serial solution-time increase: geomean 1.62 (max 5.36).
  - "Parallel speed-up of pami with 8 threads": geomean 1.88 (min 1.15, max 2.39).
  - "Performance enhancement using parallel pami with 8 threads" over the serial solver: geomean 1.16 (min 0.34, max 6.44).
  - Observations: "There is significant scope to improve pami performance further" and "Use pami tactically: switch it off if it is ineffective".
  - [inferred] This is a partial replication by a co-author on a different 40-LP set: self-speed-up 1.88 vs the published 2.34, and net gain 1.16 vs 1.51. Hardware is not stated on the slides.
- [observed, P] **A robustness failure report.** Issue #2991 (2026-04-24, user jkiviluo; the report says it was "written mostly by Opus 4.7"): "Parallel dual simplex (PAMI) stalls indefinitely after post-optimality residual rescan; serial EKK resolves the same problem in one extra pivot". It reproduces on HiGHS 1.11–1.14 for a 207,522 × 184,608 LP. Hall (2026-10-11): "Thanks, this will be studied, but it won't happen soon, so I'm collating simplex issues". It is listed under "PAMI" in open issue #3395. [inferred] This is a user report. The root cause is not confirmed by the maintainers, and I did not reproduce it.
- [observed, P] **Users disagree with the maintainer.**
  - #1547 (user NPC, 2024-01-11): "for our larger problems parallel was showing a significant improvement, and was one of the reasons we went with HiGHS."
  - #2913 (user sametcopur, 2026-03-14): "In my CG runs, I'm seeing something more like SIP < PAMI < serial, so serial is actually the slowest one."
  - These are kept as contradictions (C6).
- [stated, P] **The original README already hedged.** HSOL 1.0 README "Observations" (authorship not stated; repository maintained by Hall, Galabova and Miltenberger in 2017–2018): "Although hsol is slower when run in parallel than in serial for some problems, it is typically faster, with the `-pami` option usually faster than the `-sip` option."
- [practice, P] **What of the PhD survives in HiGHS code** (read 2026-10-27):
  - **CFT.** The collective Forrest–Tomlin update is in the PAMI path (`HEkkDualMulti.cpp`, `majorUpdateFactor`, comment "Update the factor by CFT").
  - **LiDSE** ("less infeasibility DSE", thesis §3.3) is on by default (`less_infeasible_DSE_check`, `less_infeasible_DSE_choose_row` = true). It is applied only when every matrix entry is ±1, the maximum column count is ≤ 24 and the average column count is ≤ 6 (`isLessInfeasibleDSECandidate`, HighsLpUtils.cpp).
  - **MPF and APF** exist as `HFactor` update methods (`kUpdateMethodMpf`, `kUpdateMethodApf`), but no simplex code calls them. FT is the default.
  - [inferred] The serial-side ideas survived in narrowed form; the parallel driver survived but stagnated.

---

## 5. Evaluation design and the framing of claims (Q4, Q5)

### 5.1 Baselines and protocol
- [practice, P] **Runs without presolve or crash.**
  - MPC p. 134: "Note that since hsol and pami have no preprocessing or crash facility, these are not used in the runs with Clp."
  - p. 139: "Again, Cplex is run without preprocessing or crash."
  - The SIOPT17 slides (Hall, Huangfu, Galabova, 22 May 2017), slide 9, repeat the protocol: "Dual simplex", "No presolve", "No crash", "Ignore results for 82 LPs with minimum solution time below 0.1s".
  - [inferred] Switching off presolve and crash removes part of the commercial baseline's strength. No outside critic was found who made this specific objection.
- [stated, P] **The authors flag the comparison themselves.** MPC p. 139: "Since commercial LP solvers are now highly developed it is, perhaps, unreasonable to compare their performance with a research code." It is followed by "Indeed, the performance of the better of sip and pami is comparable with that of Cplex for the majority of the test problems. For a research code this is a significant achievement." Note that the claim is about the **better of** two parallel codes chosen per problem.
- [stated, P] **The yardstick they apply to others.**
  - MPC p. 121: "Any development which is only effective in the context of an inefficient implementation is not worthy of attention."
  - p. 120: public-domain codes "are either too complicated to be used as a foundation for a parallel solver or too inefficient for any parallelisation to be worthwhile."
  - [inferred] HiGHS later applied the same yardstick to PAMI itself. Once the serial solver improved, PAMI became "not often faster" (§4).

### 5.2 Test set and reproducibility
- [observed, P] **One test problem is not public.** Galabova & Hall, Optim. Methods Softw. 35(3) (2020) 488–501, DOI 10.1080/10556788.2019.1604702 (arXiv:1804.09172v1, p. 6), reuse the Huangfu–Hall set "with qap15 replacing dcp2 due to QAP problems being of particular interest and the latter not being a public test problem". Hall's HuHa13 page: "With the exception of dcp2, the test problems used in this paper are drawn from a variety of public domain test sets." The other 29 are distributed as HuHa13_TestSet.zip.
- [practice, P] **No scaling curve.** Only serial and 8-core runs are reported. The candidate count was fixed: "s was chosen to be eight, whatever the number of processors" (MPC p. 130). The reason given is that larger multiples were "more than offset by the amount of wasted computation and an increase in the number of iterations required to solve the problem."

### 5.3 Preprint-to-journal revisions (MPC received 6 Mar 2015, accepted 10 Feb 2016, online 14 Dec 2017)
- [practice, P] **Removed in the journal version** (arXiv:1503.01889v1 vs DOI 10.1007/s12532-017-0130-5):
  - abstract: "This performance increase is sufficiently valuable for the achievement to be used as the basis of promotional material by FICO."
  - abstract: "and commercial importance" (in "first parallel revised simplex solver of general utility and commercial importance");
  - v1 p. 24: "leading to FICO announcing via advertising copy and blogs [13] that it has solved the long-standing problem of parallelising the simplex method";
  - v1 p. 25: "and used in advertising copy".
- [practice, P] **Kept in the journal version:**
  - "first parallel revised simplex solver of general utility" (p. 119, p. 141);
  - "Huangfu has raised the performance of the Xpress parallel revised simplex solver to that of the worlds best commercial simplex solvers" (p. 141).
- [practice, P] **Added in the journal version:** a discussion of Forrest's Aboca code (2012).
  - p. 124: "Other than making the source code available [5], the authors believe that there is no published reference to this work".
  - p. 132: "Based on the little evidence available, Aboca needs an additional (partial) btran operation which is not necessary in sip". No measured comparison with Aboca is reported.
- [practice, P] **Hardware description changed** between versions while the headline numbers (2.34, 1.51, 2.29, 1.15) stayed identical (C12).
- [inferred] Referee reports are not public. Whether referees asked for the removals or the Aboca discussion is **unknown**. The pattern is consistent with reviewer pressure against marketing language and for the missing related work, but that is a guess.

### 5.4 "First" and "world's best" claims vs independent benchmarks (Q5)
- [stated, P] **The claims.**
  - MPC p. 140: when it pays to run Xpress in parallel, "it enables FICO's solver to match the serial performance of Cplex (which has no parallel simplex facility)".
  - SIOPT17 slide 12 (22 May 2017): "pami ideas incorporated in FICO Xpress (Huangfu 2014)" and "Xpress simplex solver now fastest commercial simplex solver".
  - [observed, P; co-author] Hall, KTH21 slide 26 (2021): "For much of 2013-2018 the Xpress simplex solver was the best in the world".
- [observed, P; context] **Mittelmann's "Benchmark of Simplex LP solvers", 14 Jul 2017** (Wayback 20170717142400; i7-4790K). Scaled shifted geometric means were GUROBI 1, XPRESS 1.22, CLP 1.69, CPLEX 1.91 and MOSEK 3.65. So about seven weeks after the SIOPT17 slide, the independent table ranked Gurobi ahead of Xpress. Earlier snapshots (2013–2016) are not in the Wayback Machine, so "much of 2013-2018" could not be checked (Gaps).
- [observed, S] **Third parties echo the "first" claim.**
  - Berthold, Farmer, Heinz, Perregaard (FICO), Optim. Methods Softw. 33(3) (2018) 518–529, DOI 10.1080/10556788.2017.1333612 (S2 context): "the Xpress is the first commercial software using a parallel dual simplex algorithm [15]".
  - Tar, Stágel, Maros, Cent. Eur. J. Oper. Res. 25(4) (2017) 967–984, DOI 10.1007/s10100-016-0452-9 (S2 context): implemented in Xpress "as the first commercial parallel simplex implementation".
  - No counter-claim was found. [inferred] The echoes may rest on the authors' own statement, so they are not independent confirmation.

### 5.5 Huangfu's own public claims (2014)
- [stated, P] **FICO blog** "The Algorithm that Runs the World", 13 May 2014 (archived 2015-01-27):
  - "However, good speedup ratios are related to less efficient sequential implementations of the simplex method. As a result, the overall performance of these parallelization efforts is still inferior when compared to world-leading sequential simplex solvers."
  - "As the first commercial parallel simplex solver, it achieves speedup to a factor of two on various large-scale problems."
  - "After 70 years, we are finally realizing the promise of the algorithm that runs the world."
- [stated, P] **KDnuggets version**, 13 June 2014 (by-lined "By Qi Huangfu"):
  - "The algorithm can now solve massive problems much more efficiently, frequently twice as fast as was previously possible."
  - Later in the same piece: "medium- to large-sized linear programming problems can often be solved 30% faster on average, in the best case up to 2 times faster." (C4)
- [practice, P] The phrase "solved the long-standing problem of parallelising the simplex method", which arXiv v1 attributes to FICO "advertising copy and blogs", does **not** occur in the archived blog text. Its source was not found.

---

## 6. Suboptimization as a pivot rule (Q6)

- [stated, P] **Inferior to DSE, by the authors' own account.** MPC p. 140: "as a pivoting rule suboptimization is generally inferior to the regular dual steepest-edge algorithm. Thus, to control the quality of the pivots, which often declines during pami, a cutoff factor is necessary." The cutoff 0.95 was chosen by sweeping values from 1.001 to 0.01 on the same 30-LP reference set used for evaluation (MPC §3.3, Table 2). [inferred] So the tuning set and the test set are the same.
- [stated, P] **Wasted computation.**
  - MPC p. 136: "the mean value of 0.64 for the inferiority of pami relative to hsol in terms of solution time reflects the the lower iteration speed of pami due to wasted computation" (sic).
  - Thesis p. 86: serial PAMI is "generally the less efficient (about 30% slower) implementation".
  - MPC p. 138: on maros-r7 and Linf_520c, "serial pami is slower than hsol by factors of 3.48 and 2.75 respectively".
- [stated, P] **Some gains are flattered.** MPC p. 138: for the two best problems pami "is flattered by requiring significantly fewer iterations than hsol". After rescaling, the iteration-speed speed-ups were still 1.74 and 1.75.
- [observed, P; co-author] **Serial PAMI in HiGHS (KTH21).** It solved 34/40 problems and was 1.62× slower in geometric mean. The HSOL README says of serial `-pami`: "performance will typically be diminished".

---

## 7. Novel update techniques (COAP 2015): reception and what survived

- [observed, P/S] **Recognition.**
  - Crossref lists "COAP 2015 Best Paper Prize", Comput. Optim. Appl. 65(3) (2016) 541–544, DOI 10.1007/s10589-016-9882-5. The prize text was **not read** (closed).
  - Hall's HuHa12 page: "Awarded the prize for the best paper of 2015 in Computational Optimization and Applications".
  - Hall's HuHa13 page claims an MPC best-paper prize for 2018. That was **not verified** independently (Gaps).
- [stated, P] **Claims, abstract vs thesis.**
  - Journal abstract (Hall's HuHa12 page): one product-form variant is "significantly more efficient than the traditional approach, with its performance approaching that of the Forrest-Tomlin update for some problems. The other is less efficient, but valuable in the context of the dual revised simplex method with suboptimization."
  - Thesis p. 93 is stronger: MPF "is comparable with the established FT (Forrest-Tomlin) update in terms of efficiency, but implementationally is much more straightforward" (C9).
- [stated, S] **Numerical stability.** The COAP paper's own sentence, seen as an S2 context (full text not read): "in the context of Huangfu and Hall's FT-based simplex solver hsol [16], PF-like updates are only used for very limited numbers of basis changes and no numerical instability has been observed." [inferred] Stability is asserted from limited use, not tested at length.
- [observed, S] **Outside readers.**
  - Tar–Stágel–Maros (2017, S2 context): "Most of the solvers today rely on the LU form but it is not absolutely superior (Huangfu and Hall 2015a; Tar and Maros 2012)." They use the paper as support, not as a target.
  - Fukasawa & Poirrier, INFORMS J. Comput. 31(3) (2019) 612–632, DOI 10.1287/IJOC.2018.0862 (S2 context), list Huangfu and Hall among Forrest–Tomlin alternatives.
  - Leyffer & Vanaret, Math. Methods Oper. Res. 92(2) (2020) 343–376, DOI 10.1007/s00186-020-00713-x (S2 context): "current active-set methods rely on pivoting approaches and do not readily scale to multicore architectures (though some successful parallel approaches to linear programming (LP) active-set solvers can be found in the series of papers [49, 67, 55])". The S2 index attaches this context to the COAP paper.
  - No critique of the update techniques themselves was found.
- [practice, P] **Uptake.** FT remained the default in HSOL (SIOPT17 slide 4 lists "Forrest-Tomlin update") and in HiGHS. CFT survives in the PAMI path; MPF and APF are uncalled (§4). [inferred] The "much more straightforward" MPF did not displace FT in the authors' own production code.

---

## 8. Rival schools and competing methods

### 8.1 Bixby–Martin data-parallel dual simplex (CPLEX, 2000)
- [stated, P] **Huangfu's critique of the rival.**
  - Thesis p. 76: Amdahl bound of 1.5.
  - MPC p. 120: "their implementation included neither the BFRT nor hyper-sparse linear system solution techniques".
  - MPC p. 132: "parallelised only the spmv, chuzc and update-dual operations, having rejected the task parallelism of ftran and ftran-dse as being computationally disadvantageous".
- (S) Bixby & Martin, "Parallelizing the Dual Simplex Method", INFORMS J. Comput. 12(1) (2000) 45–56, DOI 10.1287/ijoc.12.1.45.11902; only the abstract was read. No reply by Bixby or Martin to Huangfu was found.
- [inferred] See §3: the HiGHS guidance now confines the parallel solver's useful regime to roughly where the rival's approach already worked (n ≫ m).

### 8.2 Parallel search paths (Tar, Stágel, Maros; Pannon/Szeged school)
- (S) CEJOR 2017, closed; S2 contexts only. They group parallelism within iterations and overlapping iterations, including "Hall and Huangfu 2012", as approaches from which "a few were successful … but these approaches do not affect the robustness of the…". The context is truncated, and the full text was **not read**.
- [inferred] Their alternative targets robustness rather than per-iteration speed. Whether they measured against PAMI is unknown.

### 8.3 Structure-exploiting and dense/GPU simplex (including Hall's own other projects)
- [stated, P] **Where parallelism does pay.** ICCOPT13 slide 22: "Good parallel performance is possible", "For small LPs distributed across multi-core cache", "For structured LPs distributed on supercomputer", "For dense LPs on GPU".
- [inferred] In the authors' own map, general sparse LPs on desktops, PAMI's target, are the least favourable case.

### 8.4 First-order / GPU PDLP school
- [observed, P] **Lu (2024).** See §2.2 and §10.
- [stated, P] **cuPDLP-C, co-signed by Huangfu.** Lu, Yang, Hu, Huangfu, Liu, Liu, Ye, Zhang, Ge, arXiv:2312.14832v2 (Jan 2024):
  - p. 4: "As interior-point and simplex methods heavily rely on matrix factorization, which is computationally infeasible at this magnitude, cuPDLP currently stands as the only realistic method for finding nearly optimal solutions in such challenging scenarios."
  - p. 6, on five huge instances with a 3600 s limit: "Both simplex and barrier methods of COPT fail to provide solutions, while cuPDLP-C efficiently solves all five relaxations."
  - p. 6: "GPUs have a revolutionary impact on traditional LP solvers".
  - The same paper concedes, p. 4: "COPT solves the most instances and thus achieves the smallest SGM10. cuPDLP-C performs around 2 to 4 times slower than COPT with different presolvers under 10-4 accuracy."
- [practice, P] **The rival method inside COPT.** COPT User Guide v8.0.1 (arXiv:2208.14314v4): `LpMethod` value "6: First-order method (PDLP)"; GPU support for LP via PDLP or barrier.
- [inferred] Huangfu did not answer the first-order school's critique of simplex scalability. He co-authored it, and the company he works for shipped the rival method next to its simplex.

### 8.5 Users who cite him as the limit of LP parallelism
- [observed, P] Lange–Swoboda (2021), Abbas–Swoboda (2022) and Thuerck et al. (2023) cite Huangfu & Hall 2018 as the canonical evidence that LP solving parallelizes poorly. They use it to motivate decomposition, message-passing or LP-free alternatives (§2.2).
- [inferred] In this literature his paper functions as the "best effort" benchmark whose modest outcome justifies leaving LP-based methods.

---

## 9. COPT era (2019–): benchmark context only; no peer critique found

- [practice, P] **COPT's default LP method.** COPT User Guide v8.0.1, `LpMethod` default −1: "For Linear Programming, choose dual simplex method". `SimplexThreads`: "Number of threads used by dual simplex. If value is -1, the thread count is determined by parameter Threads." (maximum 128). The example log reads "Starting the simplex solver using up to 8 threads". So, unlike HiGHS, COPT keeps a multi-threaded dual simplex as its default LP method. Whether it descends from PAMI or SIP is **not public**.
- [observed, P; context only] **Mittelmann tables.** These measure products built by teams; Huangfu's individual contribution cannot be separated.
  - Simplex benchmark, 21 Aug 2019: COPT-1.0.1beta scaled 1 (40/40 solved); MOSEK 3.04; CLP 1.54; HiGHS-1.0.0 5.42 (37 solved). Gurobi, CPLEX and Xpress were not in the table.
  - 15 Dec 2021: MindOpt-0.15.0 1, COPT-3.0.0 1.25, Gurobi-9.5.0 1.37, Optverse-0.2.1 1.38, CLP 8.73, HiGHS-1.1.0 20.1.
  - LPopt ("find optimal basic solution", any method), 22 Oct 2026: COPT-9.0.0 1 (65/65), MOSEK 5.27, XOPT 6.63, HiGHS-1.15.0 12.8, CLP 27.4.
- [stated, P] **Huangfu at JuliaCon 2022** ("COPT and its Julia interface", 27 July 2022). Source: the caption transcript `../sources/talks/juliacon-2022-copt-and-its-julia-interface.transcript.txt`. It was saved in this run by another research agent from the video's uploaded subtitle track; it is a caption transcript, not speaker-checked, and **not** user-supplied material.
  - On the simplex: "in our experience, the simplex solver is very suitable for large and sparse LP problems and it is necessary for solving LP relaxations in MIP solver".
  - On parallelism and accuracy: "we have full parallelization in the simplex solver and we also support Quad-precision which can help to deal with very numerically hard instances".
  - On the rival method: "we have this first order method which are very useful for some type of problems".
  - On standing: he uses Mittelmann's public benchmark as the arbiter ("According to the public benchmark, COPT is leading on many categories and we are catching up on the important MIP benchmark") and concedes "according to public benchmarking, our MIP solver is still in a catching up position".
  - [inferred] Here he answers comparative judgements by pointing to an independent benchmark and conceding where COPT trails. That differs from the 2014–2018 pattern of pointing to commercial adoption (§11).
- [inferred] By late 2021 an Alibaba code had overtaken COPT's simplex in this benchmark. No published critique of COPT's simplex design was found. Closed source leaves outsiders only benchmark tables to judge by.

---

## 10. Misreadings by citers (Q8)

- **Lu (2024)** vs the cited paper:
  - [practice, P] PAMI is not "pricing"-only. It uses "Task-parallel multiple BTRAN", "Data-parallel PRICE" and "Task-parallel multiple FTRAN for primal, dual and weight updates" (SIOPT17 slide 8; ICCOPT13 slide 11).
  - The MPC paper reports only serial and 8-core runs, so it contains no data on "two or three cores".
  - The nearest supporting statement found is Hall's own, later and qualitative: "will reduce beyond 4-8 threads" (#1192, 2023).
  - [inferred] The sentence overstates what [25] shows.
- **Mai, Wang, Abouzied, Brucato, Haas, Meliou**, PVLDB 17(5) (2024) 1146–1158, DOI 10.14778/3641204.3641222 (arXiv:2307.02860v6, p. 6): "Specifically, in [15], the authors observed a 2.34x speedup at 8 cores, with 65% of the execution effectively parallelized."
  - [inferred, computed] Their 65% equals the Amdahl inversion of 2.34× on 8 cores, p = (1 − 1/2.34)/(1 − 1/8) = 0.6545. Their own 4.79× on 80 cores gives 0.8012, matching their "80%".
  - Huangfu & Hall's "65%" is a different quantity: the share of the reference set on which pami is twice as fast in parallel (MPC p. 138).
  - They also quote 2.34× (pami8 vs pami1) rather than 1.51× (vs the serial baseline hsol).
- **ICML 2025 paper**, "Hierarchical Refinement: Optimal Transport to Infinity and Beyond", arXiv:2503.03025 (S2 context): "the dual revised simplex solver (Huangfu & Hall, 2018), a solver which only scales up to 512 points (Table S4)". This is about HiGHS on an optimal-transport LP, not about PAMI. It is listed only to show the attribution problem; it was not read.

---

## 11. How Huangfu handles critique (pattern for Phase 2)

1. **[practice] Concede the speed-up, change the yardstick.**
   - The papers admit modest parallel speed-ups (1.5×, "not extremely impressive").
   - They then measure worth against a strong serial baseline ("not worthy of attention" otherwise) and against open-source Clp.
   - They take the realistic ceiling to be set by commercial incentives: "if such linear speedup were possible then it would have been achieved years ago".
2. **[practice] Industrial adoption as evidence.**
   - FICO's reporting and advertising is cited as a "measure of the quality" (MPC pp. 140–141).
   - The marketing wording was trimmed in the refereed version (§5.3).
   - In the 2014 blog the same results appear as "a factor of two" and "finally realizing the promise".
3. **[inferred, from absence] Silence toward outside critics.** No reply, comment, rejoinder, erratum or public talk by Huangfu answering a critic was found in the sources searched here. After 2014 his public statements found here are product communications and co-signed papers. Absence of evidence is not proof; closed venues (FICO or Cardinal Operations internal material, conference Q&A) were not searchable.
4. **[inferred] He moved on rather than defend.**
   - The ICCOPT13 lesson ("No "silver bullet"", "Parallel research has yielded serial results") anticipated the later critiques.
   - His subsequent path was to productize the ideas in Xpress (2014), build COPT's simplex (multi-threaded by default), and co-sign the GPU first-order alternative (2023).
   - His open-source parallel code was left to others, who stopped extending it.
5. **[inferred] The test he set for others was later applied to his own code.** His 2014 critique of earlier parallel codes, that "good speedup ratios are related to less efficient sequential implementations", is exactly the reason HiGHS gives for PAMI's decline once the serial solver improved.

---

## Contradictions (kept, not reconciled)

- **C1. PAMI and hyper-sparsity.**
  - Thesis p. 86: better-than-average speed-ups are "more associated with the relatively dense LP problems".
  - ICCOPT13 slide 12 (Aug 2013): PAMI "Best for hyper-sparse problems", SIP "Best for non hyper-sparse problems".
  - MPC p. 138: "there is no real relation between the performance of pami and problem hyper-sparsity … although the more extreme performances are for dense problems".
- **C2. Standing against commercial codes.**
  - Thesis abstract and p. 94: PAMI "comparable" to Cplex.
  - MPC pp. 139–140: the **better of** SIP and PAMI is comparable with Cplex "for the majority", with Cplex run without presolve or crash.
  - Abbas–Swoboda (2022): commercial solvers "outperform it with sequentially executed implementations".
  - Lange–Swoboda (2021): the improvement "is relatively small".
- **C3. The speed-up figures drift across sources.**

  | Source | PAMI self speed-up (8 cores vs serial PAMI) | Net speed-up vs serial dual simplex | Best | SIP |
  |---|---|---|---|---|
  | Thesis (2013) | 2.23 | ≈1.5 (1.49) | 2.53 | 1.13 |
  | ICCOPT13 slides (2013) | — | "average speed-up 1.5" | 2.63 | 1.1 |
  | MPC (2018) | 2.34 | 1.51 | — | 1.15 |
  | HiGHS, KTH21 slides (2021) | 1.88 | 1.16 | — | — |

  HiGHS docs (2023–26) say speed-ups are "typically less than the values achieved by Huangfu and Hall".
- **C4. Huangfu's 2014 claims.** "a factor of two" (blog) and "frequently twice as fast" (KDnuggets headline) vs "30% faster on average, in the best case up to 2 times faster" (same KDnuggets piece).
- **C5. Xpress ranking.** SIOPT17 (May 2017): "now fastest commercial simplex solver". Hall (2021): "best in the world" for "much of 2013-2018". Mittelmann (14 Jul 2017): Gurobi 1, Xpress 1.22.
- **C6. Maintainer vs users on the value of parallel simplex in HiGHS.** Hall (2021–2026): "unlikely to be significant", "only a little faster", "may even be slower", "not often faster". Users NPC (2024): "significant improvement". User sametcopur (2026): serial slowest in column-generation runs.
- **C7. Lu (2024) vs the cited source.** He says "only in the pricing step" and "minimal after two or three cores". The paper parallelizes multiple BTRAN/FTRAN and reports only 1 and 8 cores.
- **C8. hsol vs Clp.** MPC p. 136: hsol "2.29 times faster than Clp" (no presolve or crash, 30 LPs, 2015 hardware). Mittelmann's simplex table puts HiGHS-1.0.0 at 5.42 vs CLP 1.54 (Aug 2019) and HiGHS-1.1.0 at 20.1 vs CLP 8.73 (Dec 2021), with default settings on 40 LPs. Different code generations and settings; not reconciled.
- **C9. MPF.** Thesis p. 93: "comparable with the established FT … update in terms of efficiency". Journal abstract: "approaching that of the Forrest-Tomlin update for some problems". Production code kept FT.
- **C10. Huangfu's own stance on simplex parallelism over time.**
  - 2014: "After 70 years, we are finally realizing the promise of the algorithm that runs the world".
  - 2022 (JuliaCon caption transcript): "full parallelization in the simplex solver"; the first-order method is "very useful for some type of problems".
  - 2023/24, co-signed: factorization-based simplex "computationally infeasible at this magnitude"; GPUs "revolutionary".
  - 2026, COPT guide: multi-threaded dual simplex remains the default LP method.
- **C11. Expected vs actual evolution.** Thesis p. 94: polishing the serial code would "achieve better performance in both serial and parallel simplex solvers". HiGHS docs: serial enhancements "have not been propagated to the parallel solver".
- **C12. Hardware description.** arXiv v1 p. 17: "16 (Intel Xeon E5620, 2.4GHz) processors". MPC p. 133: "two Intel Xeon E5-2670s, 2.6 GHz (16 cores, 16 threads in total)". ICCOPT13 slide 12: "shared memory four quad-core machine". The headline numbers are the same in both paper versions.

## Gaps

- **Referee reports and rebuttals** for MPC 2018 and COAP 2015 are not public. The MPC timeline (received 6 Mar 2015, accepted 10 Feb 2016, online 14 Dec 2017) is known, but not who asked for the revisions in §5.3.
- **Failed replications:** none found. The only re-measurement is Hall's KTH21 slides (co-author, different 40-LP set, hardware not stated). No independent group re-ran PAMI and published the result. Users' issue reports (#1547, #2913, #2991) are anecdotal.
- **Published comment/rejoinder exchanges:** none found. **Retractions or errata:** none found.
- **Closed full texts not read:**
  - Tar–Stágel–Maros (2017);
  - Berthold–Farmer–Heinz–Perregaard (2018);
  - Mamalis–Pantziou (2015);
  - Leyffer–Vanaret (2020);
  - Fukasawa–Poirrier (2019);
  - Bixby–Martin (2000), abstract only;
  - the COAP 2015 paper (abstract only, via Hall's page);
  - Hall & Huangfu PPAM 2011 (DOI 10.1007/978-3-642-31464-3_15);
  - the COAP 2015 Best Paper Prize notice;
  - Mittelmann, "Benchmarking Optimization Software – a (Hi)Story", SN Oper. Res. Forum 1 (2020), DOI 10.1007/s43069-020-0002-0.
- **Open but read only as S2 contexts:** Mamalis–Perlitis 2017 (IJACSA) and 2022 (arXiv:2211.10979).
- **MPC best-paper prize (2018):** claimed on Hall's HuHa13 page. Not found on the MPC (mpc.zib.de) or MOS prize pages, and a Crossref query for an MPC prize notice returned nothing. Unverified.
- **Xpress internals and claims:**
  - The code is closed. FICO release notes were not checked.
  - Mittelmann's simplex page has no Wayback snapshots before 17 Jul 2017, so the 2013–2016 part of "best in the world for much of 2013-2018" could not be checked.
  - The FICO "advertising copy" containing "solved the long-standing problem" was not found.
- **COPT simplex:**
  - The code is closed. No technical paper by Huangfu on COPT's dual simplex was found, and no peer critique specific to it.
  - Whether COPT's multi-threaded dual simplex uses PAMI or SIP ideas is not public.
- **Overlapped INVERT** (thesis future work): not found in HiGHS by keyword search. Status in Xpress and COPT unknown.
- **Leads without a verified identifier (not entered as findings):**
  - a 2019 thesis "Basis preconditioning in interior point methods" and a 2017 report "Permuting Spiked Matrices to Triangular Form and its Application to the Forrest-Tomlin Update". Both reuse the Huangfu–Hall 30-LP set; S2 shows no venue or DOI;
  - "Two dimensional search algorithms for linear programming" (2019 thesis; S2 context only);
  - "Promoting hyper-sparsity in the revised simplex method" (2012; S2 lists no venue; the APMOD12 talk exists). This is the LiDSE line, apparently never published as a journal paper; journal publication not verified.
- **Insider accounts of the HSOL-to-HiGHS transition** (for example Galabova's PhD thesis) were not located within the time box.
- **Bibliography tools:** DBLP (pid 116/5281) was behind a bot wall. OpenAlex conflates the author with a Zhejiang medical researcher. The critique harvest therefore covers only the five works checked in Semantic Scholar.
- **Funding and lab size during the PhD:** not checked.

## Sources

One line each: title, author(s), date, identifier or URL, primary/secondary. "Read" means the text was opened at the pages or slides cited.

1. Huangfu, Hall, "Parallelizing the dual revised simplex method", Math. Program. Comput. 10(1) (2018) 119–142, DOI 10.1007/s12532-017-0130-5 (open access; author copy https://webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf), read (primary)
2. Huangfu, Hall, "Parallelizing the dual revised simplex method", arXiv:1503.01889v1 (6 Mar 2015; ERGO-14-011), read (primary)
3. Huangfu, "High performance simplex solver", PhD thesis, University of Edinburgh, 2013, https://era.ed.ac.uk/handle/1842/7952, read abstract, §4.2–4.4, ch. 5 (primary)
4. Huangfu, Hall, "Novel update techniques for the revised simplex method", Comput. Optim. Appl. 60(3) (2015) 587–608, DOI 10.1007/s10589-014-9689-1; abstract read at https://webhomes.maths.ed.ac.uk/hall/HuHa12/ (ERGO-13-001); full text not read (primary, abstract only)
5. Hall, Huangfu, "A High Performance Dual Revised Simplex Solver", PPAM 2011, LNCS 7203 (2012) 143–151, DOI 10.1007/978-3-642-31464-3_15, Crossref-checked; not read (secondary)
6. Huangfu, "The Algorithm that Runs the World", FICO Blog, 13 May 2014, http://www.fico.com/en/blogs/analytics-optimization/the-algorithm-that-runs-the-world/ (Wayback 20150127063109), read (primary)
7. Huangfu, "The Algorithm that Runs the World Can Now Run More of It", KDnuggets, 13 June 2014, https://www.kdnuggets.com/2014/06/fico-algorithm-that-runs-world.html, read (primary)
8. Huangfu, Hall, Lubin, Smith (speaker Hall), "Parallelizing the (revised) simplex method: Is it time to give up?", ICCOPT 2013 slides, 1 Aug 2013, https://webhomes.maths.ed.ac.uk/hall/ICCOPT13/ICCOPT13.pdf, read (primary)
9. Huangfu, Hall, "Parallelizing the dual revised simplex method", NLAO16 slides, Sept 2016, https://webhomes.maths.ed.ac.uk/hall/NLAO16/NLAO16.pdf, read slides 8–13 (primary)
10. Hall, Huangfu, Galabova, "An open-source high performance dual simplex solver", SIAM Conference on Optimization slides, 22 May 2017, https://webhomes.maths.ed.ac.uk/hall/SIOPT17/SIOPT17.pdf, read (primary)
11. Huangfu, Hall et al., "Novel update techniques for the revised simplex method (and their application)", ERGO seminar slides, 30 Nov 2016, https://webhomes.maths.ed.ac.uk/hall/ERGO_301116/ERGO_301116.pdf, keyword-searched only (primary, partial)
12. Ge, Huangfu, Wang, Wu, Ye, "Cardinal Optimizer (COPT) User Guide", arXiv:2208.14314v4 (30 Jan 2026; COPT 8.0.1), read parameter sections LpMethod, SimplexThreads (primary)
13. Lu, Yang, Hu, Huangfu, Liu, Liu, Ye, Zhang, Ge, "cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language", arXiv:2312.14832v2 (7 Jan 2024), read pp. 1–6 (primary)
14. HSOL 1.0 README, repository https://github.com/mattmilten/h2gmp (last push 2018-03-26), read 2026-10-27 (primary)
15. Hall, "HiGHS: Theory, software and Impact", KTH slides, 1 Oct 2021, https://webhomes.maths.ed.ac.uk/hall/KTH21/KTH21.pdf, read slides 24–26 (primary)
16. Hall, "Three high performance simplex solvers", Tokyo public lecture slides, 14 Aug 2017, https://webhomes.maths.ed.ac.uk/hall/Tokyo17/Tokyo17.pdf, keyword-searched (primary, partial)
17. Hall, web pages HuHa12/, HuHa13/ and Talks.html, https://webhomes.maths.ed.ac.uk/hall/, read 2026-10-27 (primary)
18. HiGHS documentation "Parallelism", docs/src/parallel.md at commits 444998d (2023-03-13), dd4a9a2 (2024-01-29), 6c482a4 (2026-06-24) and branch latest (d76287b, 2026-10-27); live page https://ergo-code.github.io/HiGHS/dev/parallel/, read (primary)
19. HiGHS GitHub issues #477 (2021), #780 (2022), #1192 (2023), #1547 (2023–24), #2913 (2026), #2991 (2026), #3395 (2026), https://github.com/ERGO-Code/HiGHS/issues, read (primary)
20. HiGHS source at master 73cac48 (2026-08-19): highs/lp_data/HighsOptions.h, highs/lp_data/HighsLpUtils.cpp, highs/simplex/HEkkDual.cpp, highs/simplex/HEkkDualMulti.cpp, highs/util/HFactorConst.h, https://github.com/ERGO-Code/HiGHS, read (primary)
21. Galabova, Hall, "The 'Idiot' crash quadratic penalty algorithm for linear programming and its application to linearizations of quadratic assignment problems", Optim. Methods Softw. 35(3) (2020) 488–501, DOI 10.1080/10556788.2019.1604702; arXiv:1804.09172v1 read p. 6 (primary)
22. Koch, Berthold, Pedersen, Vanaret, "Progress in mathematical programming solvers from 2001 to 2020", EURO J. Comput. Optim. 10 (2022) 100031, DOI 10.1016/j.ejco.2022.100031; arXiv:2206.09787v2 read p. 13 (primary)
23. Lange, Swoboda, "Efficient Message Passing for 0–1 ILPs with Binary Decision Diagrams", ICML 2021, PMLR 139, 6000–6010 (https://proceedings.mlr.press/v139/lange21a.html); arXiv:2009.00481v2 read pp. 2–3 (primary)
24. Abbas, Swoboda, "FastDOG: Fast Discrete Optimization on GPU", CVPR 2022, 439–449, DOI 10.1109/CVPR52688.2022.00053; arXiv:2111.10270 read p. 2 (primary)
25. Thuerck, Sofranac, Pfetsch, Pokutta, "Learning Cuts via Enumeration Oracles", NeurIPS 36 (2023) 79108–79123, DOI 10.52202/075280-3461; arXiv:2305.12197v2 read p. 10 (primary)
26. Lu, "First-Order Methods for Linear Programming", arXiv:2403.14535v1 (21 Mar 2024), read p. 1 (primary)
27. Mai, Wang, Abouzied, Brucato, Haas, Meliou, "Scaling Package Queries to a Billion Tuples via Hierarchical Partitioning and Customized Optimization", Proc. VLDB Endow. 17(5) (2024) 1146–1158, DOI 10.14778/3641204.3641222; arXiv:2307.02860v6 read p. 6 (primary)
28. Bixby, Martin, "Parallelizing the Dual Simplex Method", INFORMS J. Comput. 12(1) (2000) 45–56, DOI 10.1287/ijoc.12.1.45.11902, abstract only via OpenAlex (secondary)
29. Tar, Stágel, Maros, "Parallel search paths for the simplex algorithm", Cent. Eur. J. Oper. Res. 25(4) (2017) 967–984, DOI 10.1007/s10100-016-0452-9, S2 contexts only (closed) (secondary)
30. Berthold, Farmer, Heinz, Perregaard, "Parallelization of the FICO Xpress-Optimizer", Optim. Methods Softw. 33(3) (2018) 518–529, DOI 10.1080/10556788.2017.1333612, S2 contexts only (closed) (secondary)
31. Mamalis, Pantziou, "Advances in the Parallelization of the Simplex Method", Algorithms, Probability, Networks, and Games, LNCS (2015) 281–307, DOI 10.1007/978-3-319-24024-4_17, S2 contexts only (secondary)
32. Mamalis, Perlitis, "Simplex Parallelization in a Fully Hybrid Hardware Platform", IJACSA 8(4) (2017), DOI 10.14569/IJACSA.2017.080449, S2 contexts only (secondary)
33. Mamalis, Perlitis, "A Hybrid Multi-GPU Implementation of Simplex Algorithm with CPU Collaboration", IJETAE (2022), DOI 10.46338/ijetae0322_06; arXiv:2211.10979, S2 contexts only (secondary)
34. Leyffer, Vanaret, "An augmented Lagrangian filter method", Math. Methods Oper. Res. 92(2) (2020) 343–376, DOI 10.1007/s00186-020-00713-x, S2 context only (secondary)
35. Fukasawa, Poirrier, "Permutations in the Factorization of Simplex Bases", INFORMS J. Comput. 31(3) (2019) 612–632, DOI 10.1287/IJOC.2018.0862, S2 context only (secondary)
36. "COAP 2015 Best Paper Prize", Comput. Optim. Appl. 65(3) (2016) 541–544, DOI 10.1007/s10589-016-9882-5, Crossref metadata only; not read (closed) (secondary)
37. "Hierarchical Refinement: Optimal Transport to Infinity and Beyond", ICML 2025, arXiv:2503.03025, S2 context only (secondary)
38. "Differentiable Initialization-Accelerated CPU-GPU Hybrid Combinatorial Scheduling", arXiv:2603.28943 (2026), S2 context only; out-of-scope example (secondary)
39. Mittelmann, "Benchmark of Simplex LP solvers", snapshots of 14 Jul 2017, 21 Aug 2019 and 15 Dec 2021 (Wayback 20170717142400, 20190927182649, 20211220190645 of http://plato.asu.edu/ftp/lpsimp.html), read; context only (secondary)
40. Mittelmann, "LPopt Benchmark" (22 Oct 2026, https://plato.asu.edu/ftp/lpopt.html) and "LPfeas Benchmark" (25 Oct 2026, https://plato.asu.edu/ftp/lpfeas.html), read; context only (secondary)
41. Mittelmann, "Benchmarking Optimization Software - a (Hi)Story", SN Oper. Res. Forum 1 (2020) 2, DOI 10.1007/s43069-020-0002-0, not read (closed) (secondary)
42. Semantic Scholar Graph API citation contexts: MPC 2018 (653 citing records), COAP 2015 (12), PPAM 2011 (11), COPT guide (67), cuPDLP-C (49), https://api.semanticscholar.org/graph/v1/, retrieved 2026-10-27 (secondary)
43. Huangfu (speaker), "COPT and its Julia interface", JuliaCon 2022 lightning talk, 27 July 2022, https://pretalx.com/juliacon-2022/talk/XRDNVT/ ; caption transcript saved in this run by another agent at ../sources/talks/juliacon-2022-copt-and-its-julia-interface.transcript.txt, read (primary; caption text, not speaker-checked)
44. Tools, all 2026-10-27 (secondary):
    - Crossref REST checks of 17 DOIs, https://api.crossref.org/works/;
    - OpenAlex author and works queries (author A5074771751 is a conflated record), https://api.openalex.org/;
    - arXiv API;
    - Wayback CDX, https://web.archive.org/cdx/search/cdx;
    - one WebSearch (locating the 2014 blog republication on KDnuggets).
