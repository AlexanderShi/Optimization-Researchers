# Qi Huangfu · 02 Stated methodology (what he says research should be)

| Field | Value |
|---|---|
| Researcher | Qi Huangfu (皇甫琦; "Huangfu Qi" on his own 2025 slides). Original author of HSOL, the dual revised simplex code that became the simplex core of HiGHS; PAMI/SIP parallel dual simplex; implemented PAMI in the FICO Xpress simplex solver; COPT developer at Cardinal Operations (杉数科技). Living. |
| Dimension | Research agent 02 of 06: stated methodology. These are his claims about how solver research should be done, sorted into the seven layers of `references/research-extraction-framework.md` §一. Whether he practises them is agent 03's job. |
| Research date | 2026-10-27 |
| Sources consulted | 29 sources read and listed under Sources: 18 primary (4 written or spoken by Huangfu alone, 14 co-authored) and 11 secondary, observed or metadata. A further 9 press pages were checked and do not name him. WebSearch: 5 of 5 calls used. Everything else came from curl, WebFetch, the arXiv and Crossref APIs, `gh` and yt-dlp. |
| Local corpus | `references/sources/{papers,talks,essays,software}` held only `.gitkeep` placeholders, so there was no user-supplied material. `private/` was not opened. |
| Saved this run | `../sources/talks/juliacon-2022-copt-and-its-julia-interface.transcript.txt` (caption transcript with a provenance header) |

## Reading guide

**Tags.** Each item carries one of these tags:

| Tag | Meaning |
|---|---|
| [stated] | Huangfu said or wrote it himself. |
| [stated, co-authored] | Text co-authored with J. A. J. Hall (or a larger team). It is the partnership's stated position and cannot be attributed to Huangfu alone. |
| [stated, self-report] | His own account of what he did, which agent 03 should check against the code and papers. |
| [observed] | Another person's statement about him. |
| [inferred] | My own reading. |

"Primary" means his own text or talk, co-authored ones included. "Secondary" means a journalist's report of what he said.

**Voice warning.** Huangfu has left very few single-authored statements of method. Only four sources are his alone:

- the 2013 PhD thesis;
- the 2014 FICO blog post;
- the 2022 JuliaCon lightning talk;
- the 2025 HiGHS workshop slides.

The journal papers are co-authored with his PhD supervisor Julian Hall. The slide decks on Hall's Edinburgh pages probably carry Hall's voice: the EUROPT 2017 deck contains the first-person line "I've been updating for 30 years: time to reinvert!", which only fits Hall. The press items from 2019 and 2024 are journalists' renderings, and one of their attributions is contested (see Contradictions C1). Weigh single-authored items above co-authored ones.

**Page numbers.**

- Thesis citations use the printed page numbers (PDF page = printed + 1).
- The thesis carries a notice against extensive quotation, so quotations from it are kept to one or two sentences.
- MPC 2018 citations use the journal pages 119–142. The article is open access under CC BY 4.0.
- ERGO-11-007 citations use its printed pages.
- Slide citations use PDF page numbers.

---

## 0. Claims repeated three or more times (the real beliefs)

| # | Claim (faithful paraphrase) | Count | Where and when | Voice |
|---|---|---|---|---|
| R1 | A parallel (or any new) simplex technique must be built on a good, state-of-the-art serial solver. | 4 | Thesis p.16 (2013); FICO blog (13 May 2014); MPC p.120 (preprint 2015, published 2018); HiGHS WS 2025 slide 19 (27 Jun 2025), quoting the MPC sentence | 3 single-authored + 1 co-authored, across 12 years |
| R2 | Speedup or improvement shown on an inefficient implementation is worthless. A development has value only inside an efficient implementation, judged against the best serial codes. | 5 | Thesis p.15 and p.75 (2013); FICO blog (2014); MPC p.121 and p.134 | 3 single-authored + 2 co-authored |
| R3 | The final yardstick is absolute performance against the world-leading commercial solver or a public benchmark, not relative speedup. | ≥6 | Thesis abstract p.3, p.17, p.92, p.94 (2013); MPC p.140 (2018); JuliaCon 27 Jul 2022 (Mittelmann benchmarks) | single-authored + co-authored |
| R4 | "Why now": the context has changed (dual simplex now preferred; prior parallel work lacked BFRT and hyper-sparsity; multi-core desktops make any speedup useful), so a problem written off as unsuitable deserves new effort. | 4 | Thesis p.15–16 and p.78 (same passage twice); thesis p.89 (SIP); MPC p.120 | 3 single-authored (2 identical) + 1 co-authored |
| R5 | Find the mechanism behind an observed effect: "why does it work?" is a research question, and unsupported folklore is not accepted. | ≥5 | Thesis p.60, p.61 (three remarks), p.65, p.93 (2013); APMOD 2012 extended abstract and slides (co-authored) | mostly single-authored |
| R6 | Report where the method loses or does not apply (slowdowns, "not recommended", limited scope, abandoned variants). | ≥6 | Thesis p.45, p.66, p.67, p.94; MPC p.138; WS 2025 slide 10; JuliaCon 2022 (MIP "still in a catching up position") | single-authored + co-authored |
| R7 | Sub-problems such as the novel LU-update variants come from the needs of the solver being built, not from a free-standing theory programme. | 3 | Thesis p.38 (2013); ERGO-13-001 p.6 (2013, co-authored); WS 2025 slide 19 (2025) | 2 single-authored + 1 co-authored |
| R8 | Accept a known-worse algorithmic choice (suboptimization) because it opens parallel scope, then control its damage (candidate cutoff found by experiment). | 3 | Thesis p.17 and p.93–94; MPC p.141 | 2 single-authored + 1 co-authored |

---

## 1. Research taste (what is worth doing, what is a good result)

**1.1 The research problem is the implementation, not the textbook algorithm.** [stated] primary, plus one secondary item. Count 3 (2013, 2014, 2019).

- "While the theoretical idea behind the simplex algorithm is relatively simple, how to efficiently implement it in practice is more complex, and has been a major topic for research." FICO blog, 13 May 2014 (single-authored).
- "Though the basic logic (Gaussian elimination) is well established, the challenge is how to properly exploit sparsity and hyper-sparsity to achieve efficiency." Thesis p.16 (2013).
- The Paper, 8 Oct 2019 (secondary; a direct quote attributed to "杉数科技副总裁皇甫琦"): "像国外比较成熟的求解器，像IBM的Cplex，像美国的Gurobi,他们都是积累了几十年经验了，每一个环节都优化到了很难提高的地步。但我们现在只有一个很梗概的算法，里头每个细节怎么实现更高效率，你其实不清楚。"
  - My translation, not his words: mature foreign solvers such as Cplex and Gurobi have accumulated decades of experience, and every component is optimised to the point where it is hard to improve. "We" have only a rough outline of the algorithm and do not know how to implement each detail more efficiently.
- Era: 2013–2014, a PhD student and then an industrial developer at FICO. 2019, vice-president of a start-up building a commercial solver from scratch.

**1.2 A technique counts only if it helps an efficient implementation (R2).** [stated] primary. Count 5. This is his sharpest and most repeated criterion.

- Single-authored:
  - Thesis p.15, on dense-matrix (tableau) parallelizations: they achieve "remarkable (from tens to up to a thousand) speedup, but the overall performance is still inferior to a good sparsity-exploiting sequential implementation of the revised simplex method."
  - Thesis p.75, his verdict: "Therefore, this path is excluded from future consideration."
  - FICO blog 2014: "However, good speedup ratios are related to less efficient sequential implementations of the simplex method. As a result, the overall performance of these parallelization efforts is still inferior when compared to world-leading sequential simplex solvers."
- Co-authored with Hall:
  - MPC p.121: "As a result, for novel computational developments to be of value they must be tested within an efficient implementation or good reasons given why they are applicable in such an environment. Any development which is only effective in the context of an inefficient implementation is not worthy of attention."
  - MPC p.134: "A high degree of parallel efficiency would be of little value if it came at the cost of severe serial inefficiency."
- Dates: 2013 (thesis), 2014 (blog), 2015 (arXiv:1503.01889 has the same sentences) and 2018 (published version keeps them).

**1.3 The mechanism must be explained, and claims need numbers (R5).** [stated] primary (thesis, single-authored). Count 3 in the thesis, plus co-authored echoes.

- On cost perturbation: "Nevertheless, despite its wide application, the discussion of why perturbation works is relatively rare." Thesis p.61.
- On Bixby's advice to treat perturbation as an algorithmic technique: he "unfortunately did not provide any further explanation or detail." Thesis p.61.
- On Koberstein's claim linking weighted perturbation and sparsity (Koberstein, *Computational Optimization and Applications* 41(2):185–204, 2008, DOI 10.1007/s10589-008-9207-4): "However, this claim is neither supported by any numerical results nor got confirmed during this research." Thesis p.61.
- Co-authored (APMOD 2012 extended abstract, Hall corresponding author): "Hitherto, there has been relatively little understanding of how it occurs and how greater degrees of hyper-sparsity may be achieved when solving a given problem." The APMOD 2012 slides (p.27) summarise the result as a "Partial answer to "why?"".

**1.4 Numerical robustness and determinism are first-class concerns.** [stated] Count 2 for numerics (2019, 2022) and 2 for determinism (2013 co-authored, 2022), so both are below the threshold of three.

- The Paper, 8 Oct 2019 (secondary; direct quote): "正常情况下，我们写一个方程式，求出一个解，这看起来是个很简单的事，但问题是一个方程，有很多系数。比如，系数有10的7次方，还有10的-7次方，两者差别就很大。这时候你用计算机算的时候，计算机本身就会产生误差，这种误差怎么去处理。其实我们这些做数学的人以前从来不去想这个问题的，做计算机的人也很少碰到这种极端的案例，但在实际应用中，怎么取解决，国外的求解器团队不会告诉你的，就需要自己想办法去解。"
  - My translation, not his words: coefficients spanning 10^7 to 10^-7 make the computer itself produce errors. Mathematicians never used to think about this and computer scientists rarely meet such extreme cases, but in practice foreign solver teams will not tell you how to handle it, so you have to find your own way.
- JuliaCon 2022 (primary, spoken; caption text at about 00:02:19 and 00:02:49):
  - "we have full parallelization in the simplex solver and we also support Quad-precision which can help to deal with very numerically hard instances."
  - "In COPT, we have parallel Cholesky which gives us deterministic and thread-independent results."
- ERGO-13-001 p.15 (co-authored, 2013): "To ensure deterministic performance, in hsol the interval is determined using a flop-based pseudo-clock".

**1.5 The simplex field is not finished.** [stated] Count 3 (two single-authored statements in one 2014 post, plus a co-authored deck in 2016).

- FICO blog 2014: he first describes the perceived lull, "as if hyper-sparsity is the final brick to the well-polished simplex building", then answers: "Inspecting the situation more carefully, the simplex research has never stopped."
  - The lull refers to Hall and McKinnon's hyper-sparsity work (*Computational Optimization and Applications* 32(3):259–283, 2005, DOI 10.1007/s10589-005-4802-0).
- The post closes: "After 70 years, we are finally realizing the promise of the algorithm that runs the world."
  - The phrase comes from R. Elwes, "The algorithm that runs the world", *New Scientist* 215(2877):32–37, 2012, DOI 10.1016/S0262-4079(12)62078-8. The same cover story opens his thesis (p.15) and the blog post, and introduces the simplex section of his JuliaCon 2022 talk.
- ERGO seminar deck, 30 Nov 2016 (co-authored, Huangfu listed first, presenter not stated), Conclusions slide p.41: "After 70 years, the simplex method still has research potential!"

**1.6 Fit the algorithm to the problem class.** [stated] Count 2.

- Thesis p.15: "The crucial advantage of the modern simplex method is its ability to directly exploit the inherent (hyper-)sparsity of LP problems."
- JuliaCon 2022 (about 00:01:54): "And in our experience, the simplex solver is very suitable for large and sparse LP problems and it is necessary for solving LP relaxations in MIP solver."
- JuliaCon 2022 (about 00:02:41): the barrier solver "is most suitable for denser problems, degenerate problems and numerically hard problems."

**1.7 Late view (2024): new hardware may make CPU-era sophistication unnecessary.** [stated] secondary, as a journalist's paraphrase without quotation marks in the source. Count 1.

- Tencent News, 15 Mar 2024. The page is published by the 数据猿 account and relays a TMTPost (钛媒体) report. Article wording (reported speech, not marked as his words): "杉数科技资深副总裁，技术负责人皇甫博士对钛媒体App表示，利用GPU硬件，现在cuPDLP-C可以让之前难以解决的大规模优化问题变得易于解决，推动了模型建立的精确度和规模。以前因CPU限制而采用的非常精密复杂的一些求解技巧可能不再需要。"
  - My translation: according to the report, Dr Huangfu (senior VP and technical lead) said that cuPDLP-C on GPUs makes previously intractable large problems solvable, and that some very elaborate solving tricks adopted because of CPU limits may no longer be needed.
- Identity: [inferred] "皇甫博士" at Cardinal Operations is taken to be Qi Huangfu, since the same company named "副总裁皇甫琦" in 2019.
- Context: he is a co-author of cuPDLP-C (arXiv:2312.14832, 2023). Its abstract (co-authored by 9) argues that the earlier comparison was unfair to both sides: "due to limitations in experimental hardware and the disadvantage of implementing the algorithm in Julia compared to C language, neither the commercial solver nor cuPDLP reached their maximum efficiency." That is R2's logic (judge inside efficient implementations) applied to a GPU first-order method.
- See Contradictions C2.

## 2. Problem choice (where problems come from, why now, when to stop)

**2.1 Choose a problem whose context has changed (R4).** [stated] Count 4.

- Thesis p.15–16 (repeated nearly verbatim on p.78). The dual simplex replaced the primal as the preferred variant after dual steepest edge and the bound-flipping ratio test. Yet the only published dual-simplex parallelization (Bixby and Martin, "Parallelizing the Dual Simplex Method", *INFORMS Journal on Computing* 12(1):45–56, 2000, DOI 10.1287/ijoc.12.1.45.11902) "neither included the BFRT nor the hyper-sparse linear system solution technique." This summary is a faithful paraphrase, with his words in quotation marks.
- Same passage: "nowadays, when every desktop computer is a multi-core machine, any speedup is desirable in terms of solution time reduction for daily usage."
- MPC p.120 (co-authored) adds the consequence for experiments: "Thus we have used a relatively standard architecture to perform computational experiments."
- Thesis p.89 applies the same move to a sub-problem. Because hyper-sparsity changed the relative costs of the FTRAN operations, "the parallelization scope of ftran operations deserves further consideration".

**2.2 Work on what the field has written off, if success would land in the efficient method.** [stated] Count 2 (2013 single-authored; 2015/2018 co-authored).

- Thesis p.15: parallelizing the revised simplex method has seen poor speedup, "Nevertheless, it is still worthwhile since it corresponds to the computationally efficient serial technique."
- MPC p.120: "However, since it corresponds to the computationally efficient serial technique, any improvement in performance due to exploiting parallelism in the revised simplex method is a worthwhile goal."

**2.3 Exclude directions that cannot beat the best serial code, even with large speedups.** [stated] Count 1 explicit exclusion (thesis p.75, quoted in 1.2), which instantiates R2.

**2.4 Accept a worse algorithmic choice if it opens the needed scope, then control it (R8).** [stated] Count 3.

- Thesis p.17: "Though it is inevitable that the suboptimization leads to a generally worse simplex path, it provides more scope for task parallelism."
- Thesis p.93–94 and MPC p.141 (co-authored): suboptimization "is generally inferior to the regular dual steepest-edge algorithm", so a cutoff on pivot quality "is necessary".
- Thesis p.17 also calls suboptimization "a less-known dual pivoting strategy". Choosing an obscure rule for a new purpose is part of the stance.

**2.5 Sub-problems are need-driven (R7).** [stated] Count 3.

- Thesis p.38, on the three novel LU-update variants: "Although applicable in general, all are motivated by the requirements of the high performance implementation introduced in Chapter 4."
- ERGO-13-001 p.6 (co-authored) has the same sentence.
- WS 2025 slide 19 lists the update variants by PhD year next to the quoted R1 sentence.

**2.6 Drop a direction when it does not pay in solution time.** [stated, self-report] Count 1 (see also Section 8).

- WS 2025 slide 10 shows a screenshot of an earlier write-up, with this passage highlighted: "Though experimental code proves the possibility of this approach, it also suggest that the LIU update is not an attractive choice in terms of the solution time. The LIU simplex update is not further studied or applied in the simplex solvers."

## 3. Idea generation

**3.1 A measured anomaly leads to a mechanism, which leads to a new rule.** [stated] Count ≥3.

- Thesis p.60: cost perturbation made iterations much faster on some problems. "This phenomenon, called hyper-sparsity promotion, is studied to reveal the underlying reason and search for alternative approaches."
- Thesis p.61: "This explanation is initially motivated by a direct observation that when pds-20 is solved with and without cost perturbation, the number of simplex iterations involving actual bound flips are 10672 and 2286 respectively."
- Thesis p.65, on the LiDSE rule: "This approach is proposed as a response to the observation that within the DSE framework, the dense rows are more attractive than they should be."
- Thesis p.93: "By following this explanation, two alternative approaches, partial chuzr and LiDSE (less infeasibility DSE), for promoting hyper-sparsity have been experimented."
- Thesis p.78, the origin of PAMI: DSE's top candidates tend to stay attractive for the next few iterations. "This motivates a dual simplex variant which chooses a small set P of attractive candidates".
- APMOD 2012 extended abstract (co-authored): "This talk presents evidence that some advanced algorithmic enhancements of the dual revised simplex method have remarkable and unintended consequences for hyper-sparsity and gives an insight into why they occur."

**3.2 Vary a classical construction when a new need appears.** [stated] Count 2 single-authored statements, plus a co-authored slide device.

- Thesis p.38: "Although the variants of the product form update set out below are relatively simple, the author is unaware of them having been described before. This is possibly because, until now, the scope for them to be useful has not arisen."
- Co-authored decks (ERGO seminar 30 Nov 2016, p.27–29; EUROPT 13 Jul 2017, p.13–15) present the variants as one-line algebraic moves, each followed by the same check:
  - APF: "Idea: Why not take it out on the right!"
  - MPF: "Idea: Substitute B = LU and take factors L on the left and U on the right!"
  - Both followed by "But: Is this useful?"
  - Then a later slide titled "Novel update procedures: are they useful?" (ERGO 2016 p.32; EUROPT 2017 p.19).
- [inferred] The EUROPT 2017 deck was presented by Hall (first-person line on p.22). The idea-then-usefulness device is therefore the partnership's, not necessarily Huangfu's own phrasing.

**3.3 Re-read the classic paper until it opens up.** [stated] primary, single-authored, 2025. Count 1.

- WS 2025 slide 16, in Chinese and English: "读书百遍，其义自见" / "Read a book a hundred times, and its meaning will become clear" (slide reference: "Chen S. Records of the Three Kingdoms").
- It sits right after slide 14 ("The early history: Year 4 … Still feels incomplete … Forrest-Tomlin update") and slide 15, an excerpt from J. J. H. Forrest and J. A. Tomlin, "Updated triangular factors of the basis to maintain sparsity in the product form simplex method", *Mathematical Programming* 2(1):263–278, 1972, DOI 10.1007/BF01584548.
- Slide 19 marks the product-form and Forrest–Tomlin updates with a book icon, and the L-Implicit-U, alternative product form, middle product form and collective Forrest–Tomlin updates with a light-bulb icon. [inferred] That reads as "learned from reading a classic" versus "own idea". The icon meaning is not stated in text.

**3.4 The failure of one design motivates its complement.** [stated] Count 1.

- Thesis p.89: "Experience with PAMI shows that, the sequential PAMI (which is essentially a dual simplex variant) frequently results in a worse simplex solving path compared to the regular version." He continues: "This issue motivated another approach which exploits purely single iteration parallelism (SIP)".

## 4. Experiments and execution

**4.1 Build the serial base first, from scratch, then parallelize (R1).** [stated] Count 4.

- Thesis p.16: "To achieve a worthwhile simplex parallelization, it should be based on a good sequential simplex solver."
- Thesis p.16 on why from scratch: existing public-domain codes "are either too complicated to be extended for parallelization or too simple to be based on."
- FICO blog 2014: "A meaningful simplex parallelization has to be designed and developed based on a state-of-the-art sequential simplex solver and still allow for significant parallelization."
- MPC p.120 (co-authored): "A worthwhile simplex parallelisation should be based on a good sequential simplex solver." The same paragraph gives a variant reason for starting from scratch: existing codes are "too inefficient for any parallelisation to be worthwhile".
- WS 2025 slide 19 quotes the MPC sentence verbatim, twelve years after the thesis.

**4.2 Evolve from a proof-of-idea prototype to an elaborated implementation, keeping the serial code simple until the parallel design is settled.** [stated] Count 3.

- Thesis p.17, on choosing C++: it "provides the opportunity of an evolutionary development process, from a proof-of-idea prototype with simple but less efficient data structures to an efficient elaborated implementation."
- Thesis p.94: "In this research, it has been intended to keep the serial implementation simple so that parallelization can be relatively easily designed and implemented. Now that the parallelization framework is ready, it is desirable to polish the serial implementation to achieve better performance in both serial and parallel simplex solvers."
- MPC p.130 (co-authored): "practical experience with pami prototypes demonstrated clearly that this is more than offset by the amount of wasted computation and an increase in the number of iterations required to solve the problem."
- [stated, self-report] WS 2025 slide 6 shows his Year-1 Gantt chart:
  - Tableau simplex: first in C, then refined in C++, NETGEN problems, then sparse tableau.
  - Revised simplex method, with milestones "20%→95% of NETLIB Solvable" and "95%→99% of NETLIB solvable".
  - Components added one at a time: scaling, Harris ratio test, steepest-edge pricing, a hyper-sparse "first try", "DEVEX, profiling framework".
  - Then "Different basis inverse algorithms": Tomlin LU, LIU, Markowitz LU and their integration.
  - The progress measure is the share of a standard test set solved. Agent 03 should check this against the code history.

**4.3 Isolate the factor under test.** [stated] Count 2 (thesis 2013; ERGO-13-001 2013, co-authored).

- Thesis p.44–45, comparing update procedures: the experiments used "the same sequence of basis changes from a "logical" basis B = I to an optimal solution of the LP."
- Thesis p.45: "This eliminates variance in the results due to the fact that a change in update technique typically leads to the simplex method taking a different path to an optimal solution."
- The reinversion interval chosen for FT was reused for all methods, which "ensures that the FT update is not disfavoured". The baseline is protected.
- The EUROPT 2017 deck (p.16) repeats "Same sequence of basis changes for all update techniques".

**4.4 Match the comparators' settings to what your own code has.** [stated, co-authored] Count 3.

- MPC p.134: "Note that since hsol and pami have no preprocessing or crash facility, these are not used in the runs with Clp."
- MPC p.139: "Again, Cplex is run without preprocessing or crash."
- MPC p.140: for the Xpress-versus-Cplex comparison, both "were run with both preprocessing and crash".
- ERGO 2016 deck p.37: "Benchmark against clp (v1.16) and cplex (v12.5) / Dual simplex / No presolve / No crash / Ignore results for 82 LPs with minimum solution time below 0.1s".

**4.5 Separate the algorithmic effect (iterations) from implementation speed (time per iteration).** [stated] Count 3.

- MPC p.134 (co-authored): "Thus, using solution times as the sole measure of computational efficiency is misleading if there is a significant difference in iteration counts for algorithmic reasons."
- MPC p.138: speedups are rescaled by relative iteration counts (see 5.5).
- Thesis p.66: LiDSE is within 6% of Cplex's time despite about 60% more iterations. "So it is safe to conclude the iteration speed is improved remarkably."

**4.6 Diagnose parallel performance with profiling, Amdahl's law and timeline charts.** [stated] Count 3 (thesis).

- Thesis p.75: "The relatively poor speedup of these parallelizations can be analysed with reference to Amdahl's Law and detailed profiling data of major computational components of the revised simplex method."
- Thesis p.78 derives the core count from that analysis: "Therefore, in this research, a choice of 8 cores is assumed."
- Thesis p.88: "This section further analyses the performance of PAMI, especially the relative poor speedup on sparse LP problems, by investigating real time behaviour of PAMI by using Gantt charts."

**4.7 Use a deliberately varied test set and robust summaries.** [stated] Count 3.

- Thesis p.17: the 30-problem reference set, mostly from Mittelmann's list, "reflects the wide spread of behaviour of the revised simplex method". It is classified by a hyper-sparsity measure.
- MPC p.133 (co-authored): "mean values of speedup or other relative performance measures are computed geometrically." The same page says solver comparisons are "well illustrated using the performance profiles in Figs. 3, 4 and 5."
- The ERGO 2016 deck drops instances with minimum solution time below 0.1 s (see 4.4).

**4.8 Set parameters by a sweep, take the stable middle, and do not over-model.** [stated] Count 3.

- Thesis p.85–86, faithful paraphrase: a sweep of the PAMI cutoff ratio from 1.001 down to 0.01 showed that any value in [0.9, 0.999] works, and the median 0.95 was chosen.
- Thesis p.94: "A suitable cutoff merit, 0.95, has been found via series of experiments."
- MPC p.141 (co-authored): "A suitable cutoff factor of 0.95, has been found via series of experiments."
- Thesis p.38, on the reinversion interval: "Of course, determining the optimal reinversion interval is not possible. However, computational experience shows that overall solution time is not sensitive to the reversion interval so a coarse model is sufficient." ("reversion" sic.)

**4.9 Tooling is part of the method.** [stated] Count 1.

- Thesis p.17: "A good compiler is important for software performance, especially the performance of the parallelization part." HSOL was built with Intel C++ 13.0 and OpenMP 3.1.

## 5. Judging results

**5.1 The yardstick is absolute performance against the best (R3).** [stated] Count ≥6.

- Thesis abstract p.3: "The performance of PAMI is comparable to a world-leading commercial simplex solver."
- Thesis p.92: "Though the speedup is not extremely impressive, the overall performance of PAMI is comparable to the dual simplex implementation of Cplex, which is a world-leading commercial simplex solver." He says the same on p.17 and p.94.
- MPC p.139–140 (co-authored): "Indeed, the performance of the better of sip and pami is comparable with that of Cplex for the majority of the test problems. For a research code this is a significant achievement."
- JuliaCon 2022 (about 00:01:00–00:01:24): "It is based on results from Benchmarks for Optimization Software, which is maintained by Professor Hans Mittelman." Then: "According to the public benchmark, COPT is leading on many categories and we are catching up on the important MIP benchmark." (Caption spelling "Mittelman".)

**5.2 Expect modest speedups; linear speedup would be suspicious.** [stated] Count 2.

- MPC p.140 (co-authored): "Although the results in this paper are far from the linear speedup which is the hallmark of many quality parallel implementations of algorithms, to expect such results for an efficient implementation of the revised simplex method applied to general large sparse LP problems is unreasonable. The commercial value of efficient simplex implementations is such that if such linear speedup were possible then it would have been achieved years ago."
- Thesis p.78, faithful paraphrase: assuming a 30% serial part, Amdahl bounds the speedup at 2.6, 2.9, 3.1 and 3.2 for 8, 16, 32 and 64 cores, and overheads make even those unlikely.

**5.3 Independent benchmarks and industrial adoption count as evidence.** [stated] Count 4.

- MPC p.140 (co-authored): "The newly-competitive performance of parallel Xpress relative to Cplex is also reflected in Mittelmann's independent benchmarking".
- MPC p.140–141: "A measure of the quality of the pami and sip schemes discussed in this paper is that they have formed the basis of refinements made by Huangfu to the Xpress solver which have been considered noteworthy enough to be reported by FICO."
- FICO blog 2014: "As the first commercial parallel simplex solver, it achieves speedup to a factor of two on various large-scale problems."
- JuliaCon 2022 (see 5.1).

**5.4 Say where it loses (R6).** [stated] Count ≥6.

- Thesis p.94, faithful paraphrase: on Linf_520c PAMI was 25% slower than the serial solver, while SIP gave a speedup of 1.31.
- MPC p.138: "Parallel pami is not advantageous for all problems."
- Thesis p.45, on the APF update: "The APF is very inefficient for some problems and is not recommended as a valuable general technique."
- Thesis p.66: "Partial chuzr is found to be unsuitable for larger pds problems."
- Thesis p.67: "Although the LiDSE approach is very helpful for the pds problems, its scope for further application is fairly limited." For problems without hyper-sparsity, "there is simply no hyper-sparsity to be promoted."
- JuliaCon 2022 (about 00:04:02): "However, according to public benchmarking, our MIP solver is still in a catching up position."

**5.5 Check whether a good number is genuine.** [stated, co-authored] Count 1 explicit.

- MPC p.138: "For the two problems where pami performs best in parallel, it is flattered by requiring significantly fewer iterations than hsol." After rescaling by iteration counts the speedups remain, so: "Thus the greater solution efficiency due to exploiting parallelism is genuine."

**5.6 Treat prior negative experience as data.** [stated] Count 1.

- Thesis p.75: "Previous research into parallelizing the simplex method provides much valuable experience for future simplex parallelization."

**5.7 The 2025 "Observations" slides.** [stated] Count 1. What he concluded is not recoverable.

- Slides 2–4 show three things:
  - HiGHS code size in 2013 (hsol) against now;
  - pypistats download counts for `highspy` against `gurobipy`;
  - a "MIPLIB 2017 Benchmark revision (screenshot in 2024, now deleted)" table comparing solver results on original and "MODIFIED" instances.
- The slide text states no conclusion and no recording was found, so I record only what was shown. I do not interpret it.

## 6. Writing and talks (thin evidence)

- **Chapter pattern.** [stated] Thesis p.16: "For each of these topics, the corresponding chapter firstly gives brief introduction to existing techniques and then reports novel developments during this research." Count 1.
- **Summary figures.** [stated, co-authored] Performance profiles are used for solver-level comparisons (MPC p.133). Geometric means are used for relative measures (4.7).
- **Claim language changed between preprint and journal.** [stated, co-authored] See C3. The FICO-advertising sentences of 2015 are gone from the 2018 version. Whether this reflects the authors' choice or the referees' is not stated.
- **Talk construction.** [inferred, from what he chose to present] JuliaCon 2022 goes in this order: public-benchmark standing first, then capabilities by solver class, then a concrete roadmap, then an invitation to contribute. The 2025 workshop talk is a personal history built from Gantt charts and screenshots of his own earlier write-ups, dedicated to Julian Hall's 60th birthday (slide 23).
- No writing advice of his own was found.

## 7. Research organisation (time, teams, students, long-term agenda)

**7.1 Sequence the work: simple serial code, then parallel framework, then polish.** [stated] Thesis p.94, quoted in 4.2.

**7.2 Plan and track a PhD in work packages with milestones.** [stated, self-report] WS 2025 slides 6 and 11 show Gantt charts.

- Year 1: tableau, then revised simplex, then basis-inverse variants.
- Years 2–3 (2009.2–2012.2): tableau solver, primal solver, basis factorization study, simplex updates, a talk on the LIU update, sequential dual solver, preliminary parallel dual solver, refinement, and hyper-sparsity research.
- Slide 14 (Year 4): "Things start to converge", "Experiments and minor improvements", "Started to work on PhD thesis", "Still feels incomplete".
- Slide 20 shows a university email of 16 Jan 2013 reminding him of a 31 Jan 2013 submission date, under the title "The early history: … the two extra months". The thesis is dated July 2013 in the repository; the dates are left as recorded.

**7.3 What a solver developer needs.** [stated] secondary. Count 1. The attribution is contested (C1).

- The Paper, 8 Oct 2019: "皇甫琦认为，开发求解器需要的人才具备三个特点。第一是数学功底好，优化算法功底扎实，第二是代码能力强，有系统工程开发能力。第三是最好具有求解器开发经验。"
  - My translation: solid mathematics and optimization-algorithm grounding; strong coding and systems-engineering ability; ideally solver-development experience.
- Direct quote in the same article: "高校培养的同学，可能最大的问题是学生解决能够多方兼顾能力不太够，求解器里面有哪些坑，他们不知道。而国内企业培养人才又有点急功近利，等不起一个人才慢慢成熟。" (sic)
  - My translation: graduates often cannot balance many aspects at once and do not know the solver's pitfalls, while companies are too eager for quick results to wait for talent to mature.

**7.4 The decisive knowledge is tacit and unpublished.** [stated] secondary, a journalist's paraphrase. Count 1.

- The Paper, 8 Oct 2019. Article wording, introduced by "据皇甫琦介绍" and not in quotation marks: "这些细节说白了就是坑，这些坑国外这些人走了30年，坑都踩了，人家怎么踩的，专利里论文里都没有，我们只能一个个去踩坑。"
  - My translation: the details are pitfalls. Foreign teams spent 30 years stepping into them, how they did so is in neither patents nor papers, and "we" can only step into them one by one.

**7.5 Users and community as part of development.** [stated] Count 1.

- JuliaCon 2022: "Going forward, we may need your help to get COPT Julia interface better. You can start by trying out our interface, report issues and bugs."
- He also says the interface "is maintained directly by the COPT team".

**7.6 Publish findings made during product development.** [stated] Count 1.

- JuliaCon 2022 (about 00:03:06): "And during our development, we also found that there is a technique to reduce the support of solutions and we published that on arXiv already." That arXiv paper was not identified in this run.

**7.7 Supervision and student training.** No statement found. He has worked in industry since his PhD, and no supervision record was found. This layer stays empty apart from 7.3.

---

## 8. Failures, abandoned directions and negative results he reports

| What | His words / source | Tag |
|---|---|---|
| L-Implicit-U (LIU) simplex update, Year 1–2 of the PhD | "not an attractive choice in terms of the solution time … not further studied or applied in the simplex solvers" (WS 2025 slide 10, screenshot of an earlier write-up). The same slide says the work "was reported in a talk at the 2nd IMA Conference on Numerical Linear Algebra and Optimisation, in September 2010, Birmingham" (not verified: see Gaps). | [stated, self-report] primary |
| Alternate product form (APF) update as a general technique | "not recommended as a valuable general technique", though valuable inside PAMI (thesis p.45; same in ERGO-13-001) | [stated] primary |
| Middle product form (MPF) update | Decks: "Not used by pami!" (ERGO 2016 p.32) and "Not used by h2gmp!" (EUROPT 2017 p.19), each with "Used by Google in glop" | [stated, co-authored] |
| Partial CHUZR for hyper-sparsity promotion | "found to be unsuitable for larger pds problems" (thesis p.66) | [stated] |
| LiDSE beyond pds-type problems | "its scope for further application is fairly limited" (thesis p.67) | [stated] |
| Serial PAMI path | Serial PAMI is slower than the regular dual simplex. Slowdowns on maros-r7 and Linf_520c. Overlapping the LU factorization was left undone, "partially because of its complicity [sic] and partially because of the potential numerical issues" (thesis p.86, p.94) | [stated] |
| Dense / tableau parallel simplex | "this path is excluded from future consideration" (thesis p.75) | [stated] |
| Block-angular "BALP" solver (2011) | "BALP simplex solver of little value" (Lancaster deck, 12 Apr 2011, p.25, co-authored with Hall and Smith; whose work BALP was is not stated) | [stated, co-authored] |
| COPT MIP standing (2022) | "still in a catching up position", with a forecast: "maybe by the mid of next year, 2023, we will be the best." Not checked here; a falsifiable forecast for agent 05. | [stated] primary |

## 9. Era and resource context

| Period | Setting (as stated in the sources) | Bearing on the stated methods |
|---|---|---|
| 2003–2009 | BSc in Computer Science and Technology at Beihang (2003.9–2007.7). MSc in high-performance computing at EPCC, Edinburgh (2007.9–2008.8), which "Turned out to be a rather good choice". Then an EPCC application consultant, who "Attended courses and started tableau simplex implementation" (WS 2025 slide 5, self-report). | He came from HPC and computer science into optimization, which fits the profiling and Amdahl style of argument. |
| 2009–2013 (PhD) | Edinburgh School of Mathematics. Supervisor Julian Hall, second supervisor Jacek Gondzio. Funded by "Format International Ltd. and NAIS" (thesis p.7). Sole author of HSOL, in C++ with OpenMP, on a 16-core Intel Xeon E5620 workstation using 8 threads, with Intel C++ 13.0. Baselines Cplex 12.4 and Clp 1.14 (thesis p.17–18). | A single developer on one shared-memory workstation, which explains "keep the serial implementation simple" and "8 cores". |
| about 2013–2018 (FICO) | The arXiv preprint (2015) lists a FICO address in Birmingham. He implemented PAMI ideas in Xpress (FICO blog 2014; MPC p.140). The 2016–2017 decks list him under FICO. | Industrial adoption becomes a stated measure of quality (5.3). |
| 2019– (Cardinal Operations) | Vice-president in 2019 (The Paper); "资深副总裁，技术负责人" in 2024 (Tencent/TMTPost); "the developer of COPT" (JuliaCon 2022 bio). He works in a company team, judged on Mittelmann's public benchmarks. | Benchmark standing, numerics and determinism appear in his statements; GPU first-order methods appear from 2023–24. |

---

## Contradictions (kept, not reconciled)

**C1. Who said the "three traits of solver talent"?**

- The Paper, 8 Oct 2019 (journalist 王心馨), attributes the three-traits statement and the quote about graduates and impatient companies to **皇甫琦**.
- Science and Technology Daily (科技日报, journalist 马爱平), reprinted on The Paper on 15 Nov 2019, attributes nearly the same words to co-founder **葛冬冬** (Ge Dongdong): "杉数科技创始人葛冬冬认为，开发求解器需要的人才具备三个特点。" Its quote differs slightly: "…学生解决问题的能力能够多方兼顾的不太多…".
- Both articles mention a group media interview. Item 7.3 therefore stays [contested attribution].

**C2. GPUs and the dense path, by date.**

- RAL deck, 2 Dec 2010 (co-authored with Hall and Smith): "Shown that the standard simplex method will run fast on a GPU" and "Standard approach to linear algebra bad for CPU-GPU combination".
- Lancaster deck, 12 Apr 2011: "Standard simplex GPU solver may be valuable" and "Scope for combined CPU+GPU solver should be explored".
- Thesis, 2013 (single-authored): the dense-matrix path "is excluded from future consideration".
- FICO blog, 2014: GPU and other parallel attempts are inferior to world-leading serial solvers.
- Press paraphrase, 2024: GPU first-order methods may make CPU-era sophistication unnecessary.
- The algorithms differ (tableau simplex on GPU versus PDLP on GPU), and the 2010–11 decks may be Hall's voice. Still, the stated stance on GPUs moved over 14 years.

**C3. Commercial claims, preprint (2015) versus journal (2018).**

- The arXiv:1503.01889v1 abstract says: "This performance increase is sufficiently valuable for the achievement to be used as the basis of promotional material by FICO." It ends "of general utility and commercial importance".
- Its p.24 says FICO announced "via advertising copy and blogs [13] that it has solved the long-standing problem of parallelising the simplex method"; reference [13] is his own FICO blog post.
- The published MPC 2018 version drops the promotional sentence, ends "of general utility", and reads "considered noteworthy enough to be reported by FICO" without "and used in advertising copy".
- His 2014 blog calls Xpress "the first commercial parallel simplex solver". The "first" claim is for agent 05 to check against the earlier parallel dual simplex work.

**C4. Why existing codes could not be the base.** The thesis (p.16, 2013) says they were "too simple to be based on". MPC p.120 says they were "too inefficient for any parallelisation to be worthwhile".

**C5. APF's stated motivation.** The RAL deck (Dec 2010, co-authored) says "Alternative product form update may offer a solution" to CPU–GPU linear algebra. The thesis (p.38, 2013) says all three novel updates are "motivated by the requirements of the high performance implementation introduced in Chapter 4", that is, PAMI.

**C6. Reported numbers differ between the thesis and the papers.** These are not reconciled and are passed to agent 03.

- MPF update: 42% more efficient (thesis p.45) versus 40% (ERGO-13-001 p.16). FT over the better product form: 63% versus 61%.
- PAMI mean speedup: 1.49 (thesis) versus 1.51 (MPC). SIP: 1.13 versus 1.15.
- Hardware: "a workstation with 16 (Intel Xeon E5620, 2.4GHz) cores" (thesis p.17; the arXiv preprint has the same machine) versus "two Intel Xeon E5-2670s, 2.6 GHz (16 cores, 16 threads in total)" (MPC p.133). This suggests the experiments were re-run for the journal version [inferred].

**C7. Bibliographic detail.** The co-authored decks of 2016–2017 cite the COAP paper as 60(4):587–608. Crossref gives volume 60, issue 3, pages 587–608.

---

## Gaps (what I could not find or verify)

- **No long-form statement of method.** I found no essay, interview or lecture in which Huangfu discusses how to do research, choose problems, write, or supervise. Layers 6 and 7 rest on thin or secondary evidence.
- **No recording of the 2025 talk.** For the HiGHS Workshop 2025 talk I found slides only. A YouTube search via yt-dlp found only the JuliaCon 2022 video, and the workshop pages link no recordings. His spoken commentary, including the point of the benchmark-revision slide, is unknown.
- **The LIU talk is unverified.** I could not verify the 2010 IMA NLAO talk on the LIU update claimed on WS 2025 slide 10. Hall's deck from the same conference (IMA-NLAO_10) has no LIU content in its extractable text, and Huangfu's own slides for that talk were not found.
- **Presenters of the co-authored decks are not established.** EUROPT 2017 is inferred to be Hall's. For ERGO 2016 the presenter is unknown.
- **Chinese-language coverage is partial.**
  - Three Chinese web searches found one interview that quotes him directly (The Paper, 2019) and one paraphrase (2024).
  - Zhihu, WeChat official accounts and Baidu Baike were excluded by rule, and some Chinese interviews may exist only there.
  - Company launch events and webinars, for example on Bilibili, were not searched.
  - The TMTPost original of the 2024 report was not read; I used the Tencent News reprint.
  - Nine other press pages were checked by grepping the raw HTML for "皇甫" and gave no hit. Some may render by script, so a zero count is not conclusive.
- **Access limits.**
  - The live FICO blog page is behind an Incapsula bot wall, which I did not try to get around. I read the Internet Archive capture of 27 Jan 2015 instead.
  - DBLP (pid 116/5281) showed a bot challenge, which I did not try to get around either. Identifiers were checked on Crossref and arXiv instead.
- **Not read:**
  - the published COAP 2015 and PPAM 2012 versions (I read the ERGO-13-001 and ERGO-11-007 preprints);
  - the cuPDLP-C full text (abstract only);
  - the COPT User Guide beyond Chapter 1 of v1 (it is a product manual with no research-method statements);
  - FICO Xpress manuals;
  - the arXiv paper on "reduc[ing] the support of solutions" mentioned at JuliaCon 2022 (not identified);
  - talks from his FICO and COPT years at INFORMS, ISMP or ICCOPT (none found).
- **Privacy.** WS 2025 slides 21–22 show personal social-media screenshots. I did not use them.

---

## Sources

Primary, his alone:

1. Qi Huangfu, *High performance simplex solver*, PhD thesis, University of Edinburgh, 2013 (repository date 2013-07-01). hdl:1842/7952, https://era.ed.ac.uk/handle/1842/7952. Primary, single-authored. Read: Ch. 1, §§2.4–2.6, 3.3–3.4, 4.2–4.5, Ch. 5, front matter.
2. Qi Huangfu, "The Algorithm that Runs the World", FICO Blog, 13 May 2014. http://www.fico.com/en/blogs/analytics-optimization/the-algorithm-that-runs-the-world/, read via the Internet Archive capture http://web.archive.org/web/20150127063109/http://www.fico.com/en/blogs/analytics-optimization/the-algorithm-that-runs-the-world/. Primary, single-authored.
3. Qi Huangfu, "COPT and its Julia interface", JuliaCon 2022 lightning talk (JuMP track), 27 Jul 2022. https://pretalx.com/juliacon-2022/talk/XRDNVT/ and https://www.youtube.com/watch?v=iqiBXoJQVD8. Transcript saved at `../sources/talks/juliacon-2022-copt-and-its-julia-interface.transcript.txt`. Primary, spoken (caption text).
4. Huangfu Qi, "Early history and recent observations of HiGHS", HiGHS Workshop 2025, Edinburgh, 27 Jun 2025. Slides (PDF author "Huangfu Qi", 23 pp.) at https://drive.google.com/file/d/18lPElo2ga37ugFEoKJh3w3auag5UXd7Q/view, linked from https://workshop25.highs.dev/schedule. Kept local only. Primary, single-authored.

Primary, co-authored:

5. Q. Huangfu, J. A. J. Hall, "Parallelizing the dual revised simplex method", *Mathematical Programming Computation* 10(1):119–142, 2018. DOI 10.1007/s12532-017-0130-5 (Crossref-checked; read the CC BY version from https://webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf). Primary, co-authored.
6. Same title, arXiv:1503.01889v1, 6 Mar 2015 (ERGO-14-011). Primary, co-authored; read in full for the preprint–journal comparison.
7. Q. Huangfu, J. A. J. Hall, "Novel update techniques for the revised simplex method", *Computational Optimization and Applications* 60(3):587–608, 2015. DOI 10.1007/s10589-014-9689-1 (Crossref-checked). Read as ERGO-13-001 (7 Jul 2013), https://webhomes.maths.ed.ac.uk/hall/HuHa12/ERGO-13-001.pdf. Primary, co-authored.
8. J. A. J. Hall, Q. Huangfu, "A high performance dual revised simplex solver", PPAM 2011, LNCS 7203:143–151, 2012. DOI 10.1007/978-3-642-31464-3_15 (Crossref-checked). Read as ERGO-11-007 (12 May 2011), https://webhomes.maths.ed.ac.uk/hall/HaHu11/ERGO-11-007.pdf. Primary, co-authored.
9. J. A. J. Hall, Q. Huangfu, "Promoting hyper-sparsity in the revised simplex method", APMOD 2012 extended abstract (dated 29 Mar 2012) and slides (28 Mar 2012), https://webhomes.maths.ed.ac.uk/hall/APMOD12/. Primary, co-authored.
10. J. Hall, E. Smith, Huangfu Q., "Towards a practical parallelisation of the revised simplex method", IMA NLAO slides, 14 Sep 2010, https://webhomes.maths.ed.ac.uk/hall/IMA-NLAO_10/IMA-NLAO_10.pdf. Primary, co-authored (presenter not stated).
11. J. Hall, Q. Huangfu, E. Smith, "A high performance dual revised simplex solver", RAL slides, 2 Dec 2010, https://webhomes.maths.ed.ac.uk/hall/RAL10/RAL10.pdf. Primary, co-authored.
12. J. Hall, Q. Huangfu, E. Smith, "High performance computing and the simplex method", Lancaster slides, 12 Apr 2011, https://webhomes.maths.ed.ac.uk/hall/Lancs11/Lancs11.pdf. Primary, co-authored.
13. J. Hall, Q. Huangfu, "A high performance dual revised simplex solver", PPAM 2011 slides, 13 Sep 2011, https://webhomes.maths.ed.ac.uk/hall/PPAM11/PPAM11.pdf. Primary, co-authored.
14. Q. Huangfu, J. Hall, "Others", "Novel update techniques for the revised simplex method (and their application)", ERGO seminar slides, 30 Nov 2016, https://webhomes.maths.ed.ac.uk/hall/ERGO_301116/ERGO_301116.pdf. Primary, co-authored (presenter not stated).
15. J. Hall, Q. Huangfu, I. Galabova, "An open-source high performance dual simplex solver", SIAM Conference on Optimization slides, 22 May 2017, https://webhomes.maths.ed.ac.uk/hall/SIOPT17/SIOPT17.pdf. Primary, co-authored.
16. Q. Huangfu, J. Hall, "Novel update techniques for the revised simplex method", EUROPT slides, 13 Jul 2017, https://webhomes.maths.ed.ac.uk/hall/EUROPT17/EUROPT17.pdf. Primary, co-authored (Hall's first-person line on p.22).
17. D. Ge, Q. Huangfu, Z. Wang, J. Wu, Y. Ye, "Cardinal Optimizer (COPT) User Guide", arXiv:2208.14314 (v1 30 Aug 2022; v4 30 Jan 2026). Primary, co-authored product manual; Ch. 1 of v1 read; no method statements.
18. H. Lu, J. Yang, H. Hu, Q. Huangfu, J. Liu, T. Liu, Y. Ye, C. Zhang, D. Ge, "cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language", arXiv:2312.14832 (v2, 7 Jan 2024). Primary, co-authored (9 authors); abstract only.

Secondary, observed and metadata:

19. 王心馨, "杉数科技创始人葛冬冬：'数学规划求解器'为什么需要国产化", 澎湃新闻 (The Paper), 2019-10-08, https://www.thepaper.cn/newsDetail_forward_4618351. Secondary (press; quotes 皇甫琦).
20. 马爱平 (科技日报), "这个跻身世界前列的求解器到底是个什么神器？", reprinted on The Paper, 2019-11-15, https://m.thepaper.cn/newsDetail_forward_4970883. Secondary (does not name Huangfu; gives the talent quote to 葛冬冬).
21. 数据猿 account on Tencent News, relaying a TMTPost (钛媒体) report, "杉数科技用GPU芯片开启运筹学新的'大航海时代'，发布支持GPU的一阶算法求解器", 2024-03-15, https://news.qq.com/rain/a/20240315A042OG00. Secondary (paraphrases "皇甫博士").
22. 环球财经网 via 凤凰网, "杉数科技COPT线性规划求解器取得单纯形法世界第一", 2020-08-28, https://finance.ifeng.com/c/7zJ5WjgrXeP. Secondary (benchmark context only; does not name Huangfu).
23. HSOL 1.0 README.md, h2gmp repository (copy at https://github.com/mattmilten/h2gmp, last push 2018-03-26). Observed (co-developers' text; says "HSOL was originally written by Qi Huangfu"; author of the README not stated).
24. HiGHS website, "Background / Authorship", https://highs.dev/ (read 2026-10-27). Observed ("HiGHS is based on the high performance dual revised simplex solver for LP developed by Qi Huangfu").
25. Julian Hall's pages https://webhomes.maths.ed.ac.uk/hall/HuHa13/, /HuHa12/, /HaHu11/: abstracts, publication history, and the best-paper notes (MPC 2018, COAP 2015) as stated by Hall's pages, not checked with the journals. Observed.
26. Optimization Online author page, https://optimization-online.org/author/qi-huangfu/ (one entry, 2015/03/06). Index.
27. pretalx JuliaCon 2022 records via the API (talk XRDNVT; speaker ZF7V93, bio "Qi Huangfu is the developer of COPT and has worked on many different optimization solvers, including HiGHS and FICO-Xpress."). Metadata.
28. HiGHS Workshop 2025 schedule and speaker pages, https://workshop25.highs.dev/schedule and /speakers (Huangfu listed as invited speaker, Fri 27 Jun 2025, 11:30). Metadata.
29. COPT-Release README, https://github.com/COPT-Public/COPT-Release (COPT 8.0.7 notes). Team voice; no method statements.

External papers named above, each with its identifier checked on Crossref in this run:

- Forrest and Tomlin 1972, DOI 10.1007/BF01584548
- Bixby and Martin 2000, DOI 10.1287/ijoc.12.1.45.11902
- Koberstein 2008, DOI 10.1007/s10589-008-9207-4
- Hall and McKinnon 2005, DOI 10.1007/s10589-005-4802-0
- Elwes 2012, *New Scientist*, DOI 10.1016/S0262-4079(12)62078-8

Press pages checked with no mention of "皇甫" (2026-10-27):

- geekpark.net/news/267689
- techwalker.com/2022/0930/3144677.shtml
- news.qq.com/rain/a/20220930A01W5700
- news.qq.com/rain/a/20230406A05TXV00
- community.aijishu.com/a/1060000000212651
- jiemian.com/article/6287793.html
- 21jingji.com/article/20230313/herald/0b26f15b847786e1eae22458f3fcc5f8.html
- guancha.cn/wangzizhuo/2019_10_06_520352.shtml
- m.leiphone.com/category/academic/rArjum9yhqL4G9Rc.html
