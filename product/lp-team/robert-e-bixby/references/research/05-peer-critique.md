# Robert E. Bixby: Peer Critique (blind spots, limits, contested judgements)

| Field | Value |
|---|---|
| Researcher | Robert E. Bixby. Rice University mathematician; wrote the original CPLEX simplex code; co-founded CPLEX Optimization (incorporated 1987, first release 1988) and Gurobi (2008; CEO until 3 September 2015, per team.json). Lens of this file: decision and measurement craft for LP (1987-2002) and for MIP progress measurement. Matroid and TSP work: context only, not searched for critique. Living status and present role: deliberately not stated (team.json) |
| Dimension | Research agent 05 of 06: peer critique. Outside objections, failed or partial replications, published exchanges, independent re-measurements of his progress numbers, rival schools, predictions, misreadings by citers, and how each was answered |
| Research date | 2026-11-05 |
| Sources consulted | 53 (19 primary: his own or co-signed papers, reports, decks, interview, caption transcripts; 34 secondary), listed under "Sources" |
| WebSearch calls | 5 (of 7 allowed) |
| User-supplied material | None. `references/sources/{papers,essays,software}/` hold only `.gitkeep`. `talks/` holds four caption transcripts saved earlier in this run by research agent 02; they are not user-supplied and are cited here as "caption" (S50-S53). `private/` was not opened. **Nothing in this file is from user-supplied material** |
| Transcripts saved | None by this agent. Slide decks and papers stay unsaved (copyrighted) |
| Language | English (team.json) |

**Correction (T2, 2026-11-19).** The ZIB reports SC 92-11 and SC-95-45, marked below as not reached (step 5 of "How the critiques were found", the authorship caveat on SC 92-11, §4, §6 and Gaps), were read in full by research agent 03 in the same research round: WebFetch received both PDFs without the bot check (03-process-evidence, access notes and sources S4, S5). SKILL.md cites their pages from that reading. Where this file says the crash evaluation or the parallel-dual design is known only through others, note 03 supersedes it.

**Tags.**
- [stated]: said or written by Bixby, or in a paper, report or deck he authored or co-signed. Caption transcripts are flagged "(caption)": speech-recognition or uploaded subtitles, not speaker-checked.
- [practice]: what his papers, decks, tests or records show was done.
- [observed]: what a third party wrote or reported. Close colleagues and co-authors (Grötschel, Cook, Martin, Rothberg) are not outside critics, and are flagged.
- [inferred]: my reading. The basis is given; do not quote it as anyone's view.
- (P) primary: read in the critic's or Bixby's own text at the page or slide cited. (S) secondary: abstract only, metadata only, a figure relayed by another author, or a Semantic Scholar citation context ("S2 context; full text not read").

**How the critiques were found.**
1. Read the Bixby-side texts that critics target, in full: OR 2002 [S1], Documenta 2012 [S2], the Optima 101 interview with the Grötschel and Cook comments [S3], the Hausdorff 2022 deck [S4] and the ECCO 2017 deck [S5] (the ECCO deck is new to this corpus). Read the caption transcripts saved by agent 02 [S50-S53] with grep for critique-relevant passages.
2. Pulled Semantic Scholar citation contexts for seven works (OR 2002: 431 citing records; initial basis 1992: 191; Bixby-Rothberg 2007: 236; progress report 2004: 124; 1994 commentary: 65; Bixby-Martin 2000: 43; closing-the-gap 2000: 17) and filtered them for critical wording [S48].
3. Opened every critic cited below in a legal open copy (arXiv, author pages, open-access journals, a university repository), except items marked (S).
4. Verified identifiers with Crossref, the arXiv API, Unpaywall (email parameter nuwa-skill@users.noreply.github.com), OpenAlex and the Rice repository API.
5. Not reached, and not routed around: ZIB OPUS (SC 92-11, SC-95-45) and DBLP sit behind an Anubis proof-of-work bot check; the INFORMS PDF of Lodi-Tramontani 2013 returned HTTP 403; the CIRRELT 2010 deck cited by Grace refused the connection; a Bath-hosted 2015 Bixby deck now redirects to the university homepage; web.archive.org was not used. Closed Springer, SIAM and INFORMS texts were not read (listed under Gaps).

**Attribution caveats that must survive into the skill.**
- **LP code authorship rests on his own dated statements.** All development at the 1988 first release ([S3] p. 3); still doing development at the 1997 ILOG sale ([S3] p. 4); "Absolutely zero development" at Gurobi, only testing and pestering the developers ([S3] pp. 4-5); main parts of the CPLEX simplex as of April 1992 (SC 92-11 p. 2, per team.json; not re-read here, bot wall). He says he implemented the Suhl-Suhl (1990) LU factorization in CPLEX himself ([S50] Part 3, caption). OR 2002 credits Gu, Lustig, Rothberg and Wunderling with fundamental contributions to the CPLEX LP algorithms ([S1] p. 14). Changes from CPLEX 5.0 to 7.1 and later (hyper-sparse solves, more aggressive perturbation, bound flipping) are **not shown to be his code**. A critique of their non-disclosure targets what his papers report, not his programming.
- **Dual steepest edge is Forrest and Goldfarb's method, which CPLEX implemented**, by his own texts: [S1] p. 8, [S2] p. 113, [S50] Part 3 (caption), [S51] (caption: Goldfarb told him which projected variant to use).
- **MIP.** "basically I bask in the reflected glory" ([S3] p. 4). Gu did the cuts and most of presolve; Rothberg did node presolve, probing, bound strengthening and the parallel barrier; heuristics followed, but who added them is unclear in the transcript ([S3] pp. 3-4). Bixby put strong branching into CPLEX after a discussion with Cook ([S3] p. 4). Early MIP codes such as MINTO solved problems CPLEX could not ([S3] p. 3). With no development at Gurobi, **a critique of CPLEX or Gurobi MIP performance targets other people's code; a critique of his progress numbers targets his measurement craft.**
- **Co-authored work, roles not divided:** Bixby and Schwabacher 1989 [S6]; Bixby and Martin 2000 [S9]; Bixby et al. 1992, 2000, 2004 [S13, S10, S11]; Bixby and Rothberg 2007 [S12]; MIPLIB 2010 [S15].

---

## 0. Summary for Phase 2

| # | Recurring critique (blind spot / limit) | Raised by | Bixby-side answer | Status |
|---|---|---|---|---|
| Q1 | **Progress reported, methods withheld.** Hyper-sparse solves, dual perturbation "as an algorithmic technique", bound flipping and bound shifting were announced as decisive but never written up; the 1992 "planned series" on the CPLEX simplex stopped after one paper | Hall-McKinnon 2002/2005 [S17]; Koberstein 2005 [S21]; Huangfu 2013 [S20]; Koch-Martin-Pfetsch 2013 [S41] (S) | No paper on shifting, "I just never got around to it" ([S3] p. 4). Public lectures in 2015 explain parts (caption [S50]); he says he leaves many tricks out from laziness, not secrecy | Partly answered orally. No written method paper found |
| Q2 | **Single-vendor, retrospective measurement on private libraries.** Easy-instance filters, time limits and instance selection move the speed-up factor | Koch-Berthold-Pedersen-Vanaret 2022 [S16]; Grace 2013 [S29]; Danna 2008 [S28] (general, not naming him) | Pre-emptive caveats in the papers ([S1] pp. 4, 11-12; [S2] p. 114); in 2021 he describes Gurobi's five-seed testing and admits biases toward difficult and solvable models ([S51], caption) | Open. No reply to Koch et al. found |
| Q3 | **Chained version-to-version products versus direct comparisons.** The "over 29,000" MIP factor is a product of eleven consecutive geometric means | [inferred] from Koch et al. 2022 relaying Lodi's direct 67.9 [S16, S44] | Bixby calls the 29,000 "projected" ([S2] p. 117) | Tension, not raised explicitly by any critic found |
| Q4 | **Parallel simplex: small or narrow gains.** Bixby-Martin speed-ups only for LPs with many more columns than rows; no bound flipping or hyper-sparsity; task parallelism rejected; an implementation recommendation failed to replicate | Hall 2007/2010 [S18]; Huangfu 2013 [S20]; Huangfu-Hall 2018 [S19]; Koberstein 2005 [S21] | Concedes: simplex algorithms "have not been successfully parallelized" ([S1] p. 7), "essentially no success" ([S2] p. 114) | Conceded. Direction abandoned in his texts after 2000 |
| Q5 | **Algorithm-choice verdicts drift** (barrier best for large LPs in 1998; no clear best around 2000; barrier narrowly best in 2002; dual steepest edge the "algorithm of choice" in 2022). His 2000 figures conceded a bias against barrier | Todd 2002 [S24] (observes, does not attack); Lustig-Marsten-Shanno rejoinder 1994 [S25] (not read) | Concessions in the texts themselves; OR 2002 note 10 accepts LMS's selection point | Kept as contradiction C1 |
| Q6 | **Special-purpose interior-point codes judged dominated by general dual simplex** ([S1] p. 9: "Castro's algorithms are now dominated") | Castro 2003, 2007 [S22, S23] | None found. He had pointed Castro to the hard Gridgen and Tripart instances ([S22] p. 47) | Castro's qualification stands |
| Q7 | **Crash basis (1992) judged on iterations.** Reimplemented, it cuts iterations but can raise solve time; newer sparse starting bases beat the CPLEX default crash | Fan et al. 2023 [S34]; Parker et al. 2026 [S35]; Ploskas et al. 2021 [S36] (S) | None (the 1992 paper predates them; not read here) | Open |
| Q8 | **Showcase numbers generalised.** The single production-planning model (43,500x) and PCAST's "43 million" | Grace 2013 [S29]; Sherry-Thompson 2020/2021 [S30] | He keeps the example in 2017 and 2022 decks next to test-set-wide factors ([S5] p. 14; [S4] p. 27) | Open |
| Q9 | **Predictions.** "LP is threatening in the future to again become a significant bottleneck", with no progress since 2004 (2012); MIP progress "shows no signs of stopping" (2012) | Outcomes from Koch et al. 2022 [S16], PDLP 2026 [S38], his own 2021-2022 talks | He revised the LP claim himself (about 3x on large models since about 2015: [S4] p. 28; [S51] caption) | Partly borne out, partly revised |
| Q10 | **Priority.** "Back then, dual didn't really exist" ([S3] p. 3) and 2022's "This led to the development of dual steepest edge" ([S4] p. 22) versus Forrest-Goldfarb 1992 | The interviewer's own question ([S3] p. 3); Forrest-Goldfarb abstract [S27]; [inferred] | Elsewhere he credits Forrest and Goldfarb plainly ([S1] p. 8; [S50], [S51] captions) | Tension. No published dispute found |
| Q11 | **Closed commercial codes and academic research.** Academics cannot test ideas without the internals; commercial non-publication causes the open-source gap | Optima interviewers Kaibel, Lee, Linderoth [S3] p. 6; Koberstein 2005 [S21] pp. 2-3 | Hard to test any idea; Gurobi has "no interest in making this hard"; little from academia reached the MIP code (2015, 2021, 2023) | Disagreement persists |

**Where the critiques land in the seven layers (framework §一)** [inferred grouping]

| Layer | What the critiques bear on | Items |
|---|---|---|
| 1 Taste (what counts as progress) | Machine-independent speed on private customer models; the best of three algorithms treated as one algorithm ([S2] p. 114); one showcase model as the lead example | Q2, Q3, Q8 |
| 2 Problem choice | Challenge models from customers, vendors and the literature (degen4/LAU2 from United via Cray Research; the American Airlines crew-scheduling LP; the PDS military logistics models); libraries biased toward hard, solvable models (his own admission, [S51]) | Q2, §1 |
| 3 Idea generation | Taking published methods into the code (Suhl-Suhl LU, Forrest-Goldfarb DSE, Harris's ratio test leading to shifting); credit and priority disputes | Q10 |
| 4 Experiments | Chained forward comparisons, geometric means, time-limit substitution, single runs per version, no seeds in public numbers | Q2, Q3, §3.3 |
| 5 Judging results | Verdicts such as "dominated", the barrier-versus-dual verdicts, predictions about LP and MIP progress | Q5, Q6, Q9 |
| 6 Expression | Results in surveys and talks, methods unpublished; printed slips | Q1, §11 |
| 7 Organisation | Company team writes the later code; the parallel-simplex line abandoned; the academia-versus-vendor divide | Q4, Q11 |

---

## 1. Era and resource context

- **1983-1987: one person, a PC, no literature.** He wrote a classroom LP code, then improved it for two years on Chesapeake's sequential-LP snapshots without consulting the literature ([S1] p. 3; [S3] pp. 1-2). The machine on his desk in late 1987 was a Sun 3/50 ([S1] p. 5). The 2022 deck says he could not get research funding for LP computation in 1987-1988, "zero success" ([S4] p. 9). [stated, P]
- **About 1989-1990: supercomputer time.** His first degen4/LAU2 attempts ran on a Cray at Cray Research with John Gregory ([S1] p. 8; [S3] p. 3). Thomborson (1991), relaying Bixby's correspondence of September 1990, reports typical Cray-versus-Sun-4 speed-ups of 30 to 40 ([S39] p. 3). The short Cray turnaround let him watch batches of LPs, abort them and adjust parameters; Bixby says that on a slower machine no experimenting with the LPs gets done ([S39] p. 4). A new vectorised CPLEX gave 15-66x on ten large LPs ([S39] p. 8). [observed, P; Bixby's words relayed by Thomborson]
- **1990s: a company team.** Gu, Lustig, Rothberg, Wunderling and others ([S1] p. 14). An SGI partnership produced the parallel barrier, about 40x faster than OSL on an airline fleet model ([S3] p. 3; [S4] pp. 18-19). [stated, P]
- **2002 measurement budget.** A CPLEX library of about 2,000 LPs collected over 13 years, screened to 680. Six default runs per model (barrier with crossover, primal and dual, for CPLEX 5.0 and 7.1), each capped at 350,000 s, on 667 MHz Compaq ES40 servers ([S1] p. 12). [practice, P]
- **2007 measurement budget.** A bank of identical machines; twelve CPLEX versions (1.2 to 11) recompiled; 1,892 models (1,852 in [S5] p. 30); 30,000-s cap per run ([S2] p. 116). [practice, P]
- **Gurobi era.** Six hundred web models collected in two days; about 10,000 models, of which about 3,500 form the real test set ([S3] p. 6); a "Gurobi MIP Library (3550 models)" ([S5] pp. 34-35). [stated, P]
- [inferred] Every progress number in his texts rests on vendor-scale compute and private model libraries. Outside groups could only re-measure on public sets (Koch et al. 2022, §3.2). No independent re-run of his own series was found.

---

## 2. Progress reported, methods withheld (Q1)

### 2.1 What critics said [observed]
- **Hall and McKinnon** (preprint 8 Oct 2002, pp. 2 and 23; published COAP 2005) [S17], (P).
  - p. 2: hyper-sparsity was reported independently by Bixby [S1] and Bixby et al. [S10].
  - p. 23: brief comments by Bixby show that CPLEX developed hyper-sparse FTRAN, BTRAN and PRICE, techniques "for which no details have been published", introduced between CPLEX 6 and 6.5.
  - p. 23: other unpublished CPLEX features may explain the performance gap to their EMSOL code.
- **Koberstein** (Paderborn thesis, Nov 2005) [S21], (P).
  - p. 2: Bixby says Gilbert-Peierls style sparse solves gave CPLEX enormous gains, but "he does not disclose implementation details".
  - pp. 2-3: the missing implementation descriptions created a large performance gap between open-source research codes and commercial LP systems.
  - p. 63: credits Bixby as, to Koberstein's knowledge, the first to report the hyper-sparse gains (credit, not critique).
- **Huangfu** (Edinburgh thesis 2013, printed p. 61) [S20], (P). Bixby proposed treating dual perturbation as an algorithmic technique rather than a cure for degeneracy, but gave no explanation or detail. Huangfu supplies his own explanation: perturbation spreads the break points and so makes the bound-flipping ratio test effective (p. 63).
- **Koch, Martin, Pfetsch** (2013) [S41], (S, S2 context; full text not read). Despite the LP speed-ups Bixby reported, only a few articles together contain what is needed to implement a simplex LP solver.

### 2.2 What Bixby said and did
- [stated, P] OR 2002 p. 9 explains the CPLEX 7.1 speed on the PDS models by three things: full exploitation of sparsity, more aggressive dual perturbation used as a technique, and bound flipping. For a description it points to "Applegate et al. (forthcoming)", listed as "Solving Traveling Salesman Problems. Forthcoming." (p. 14).
- [practice, (S)] The 1992 initial-basis paper calls itself the first two parts of a planned series on the CPLEX simplex implementation (abstract via OpenAlex, local `publications/abstracts.md`). An OpenAlex query on 2026-11-05 finds five simplex-titled works by him and no later part. [inferred: the series did not continue in print]
- [stated, P] Optima 101 p. 4: he names bound shifting as his most important contribution and says there is no paper on it: "I just never got around to it."
- [stated, caption] CO@Work 2015 lectures at ZIB (videos uploaded 2016) [S50].
  - Part 1: the slides plus pencil-and-paper work should suffice for a reasonable dual simplex implementation, and he says there is evidence for this.
  - Part 3: he explains shifting and perturbation (in his old code he perturbed basic variables, and nonbasic ones only on entering) and says the dual seems to like being perturbed, for reasons not fully understood.
  - Part 3: he says many tricks are left out, from laziness rather than secrecy, and he skips bound flipping.
- [stated, caption] In the 2023 interview excerpt [S53], he says people keep asking him to write a paper on the LP story and that he might.

### 2.3 How it was answered
- [inferred] Partly, and only orally. The 2015 lectures post-date every written complaint (2002-2013). No critic acknowledging them was found.
- No written account of bound flipping, hyper-sparse solves or shifting by him was found.
- Whether the TSP book that OR 2002 promised ("Applegate et al.") carries the missing details was not checked (Gaps).

---

## 3. How the progress numbers are measured (Q2, Q3, Q8)

### 3.1 His own design and self-caveats [stated / practice, P]
- **Vendor code, with a caveat.** He uses CPLEX throughout and believes other modern codes would show similar gains ([S1] p. 4).
- **Chained forward comparisons.** The ideal design is one representative set run with a 1987 code and a current one. He judges it impractical, since old codes would need a large fraction of a year on the large models. He chains comparisons forward in time across different test sets instead and argues they convince "when taken as a whole" ([S1] p. 11).
- **Summary statistic.** He rejects the total-time ratio (4.3) and the arithmetic mean of ratios (9.6) as too sensitive to single large entries. He uses the geometric mean of ratios (4.70) as more robust and more conservative ([S1] p. 11).
- **Direction of bias.** He thinks the small netlib models underestimate the XMP-to-CPLEX 1.0 gain ([S1] p. 12).
- **680-model set.** Built by removing near-duplicates and models solved in under 0.25 s by both versions and all three algorithms; three models no algorithm solved within 350,000 s were dropped ([S1] pp. 12-13). Row count was his best simple predictor of difficulty (p. 12).
- **Selection bias conceded.** Note 10 ([S1] p. 14) accepts Lustig-Marsten-Shanno's point that seven of the eight 1994 models were of interest because simplex found them hard. The note is attached to his remark that barrier dominates that set (pp. 11-12).
- **Best-of-three.** The LP algorithm measure is the best of primal, dual and barrier (with crossover) against 1988 primal: "One can argue whether this is a legitimate approach", but it is the one he used ([S2] p. 114). In 2021 he anticipated the objection that one algorithm is compared with three. He answered that only one algorithm existed in 1988 and that listeners may accept the comparison or not ([S51], caption).
- **MIP protocol.** Consecutive CPLEX versions are compared on models solved by at least one of the two, with the time limit substituted for unsolved runs, by geometric mean. The product of the pairs is the "projected" machine-independent factor of over 29,000 ([S2] pp. 116-117).

### 3.2 Independent re-measurement: Koch, Berthold, Pedersen, Vanaret (2022) [observed, P]
Authors: ZIB, TU Berlin and FICO (Berthold works for a competing vendor) [S16]. Read in full, arXiv v2.
- p. 4: they place his LP papers among "five studies that focus solely on the cplex solver". They summarise his figures neutrally, including OR 2002's 2.3 geometric-mean speed-up over 677 instances (1997-2001), rising to over 20 above 500,000 rows.
- **Design critiques**, stated as applying to all such studies including their own:
  - a higher "too easy" threshold raises the speed-up and a lower time limit lowers it (p. 5);
  - collections lean toward difficult instances and toward what current solvers can handle (p. 5);
  - "any speed-up factor can be attained" by adding instances the old code cannot solve and raising the time limit (p. 16);
  - PAR scores and long time limits inflate numbers arbitrarily (pp. 21-22);
  - tuning to MIPLIB favours newer solvers and may overestimate progress (p. 15);
  - feature contributions cannot be meaningfully isolated, because features interact (pp. 12-13).
- **Results.**
  - LP: about 9x algorithmic speed-up 2001-2020, comparing the virtual best of CPLEX 7, Xpress 14 and MOSEK 3 with the virtual best of 2017-2020 codes. Often no single algorithm got faster; the fastest choice did (p. 13). The main gains came from 64-bit memory and parallel barrier, with little theoretical progress (p. 25).
  - MILP: about 50x on instances both generations solve, about 22% a year. 62% of the MIPLIB 2017 benchmark is solvable only by the new codes (pp. 20, 25).
- **Relayed figures** (secondary for this file).
  - Achterberg-Wunderling: CPLEX 8.0 to 12.5 gives 4.71 on 2,928 models, an underestimate because the old version hit the time limit on 732 of them (p. 4; [S45] not read).
  - Lodi: CPLEX 1.2 to 11.0 gives a direct geometric mean of 67.9 on 1,734 MILPs; CPLEX 1.2 solved 15.0% of 1,852 and CPLEX 11.0 solved 67.1% (p. 5; [S44] not read).
- **Answer.** None found. [practice] His September 2022 deck still gives 3,300x (algorithms), 1,600x (machines) and about 5,300,000x in total, without reference to Koch et al. ([S4] p. 28).
- [inferred] Koch et al. defend a cross-vendor "virtual best" on the same logic he used across algorithms: why not use the best available solver for each instance (p. 6). That partly endorses his best-of-three choice.

### 3.3 Performance variability, and how Gurobi testing answered it
- **Danna** (ILOG CPLEX R&D, MIP 2008 workshop slides) [S28], [observed, P].
  - Slides 4 and 9-29: changes that should not matter (row and column permutations, random seeds, platforms) change MIP effort.
  - Slide 7: she measures simplex iterations because time is hard to measure precisely.
  - Slides 38-39: a code-A-versus-B difference mixes true effect and noise. She asks for large model sets and says "we need inferential statistics".
  - She does not name Bixby. [inferred] The critique applies to single-run, descriptive version-pair tables such as [S2] pp. 116-117, [S5] p. 36 and [S4] p. 28, which report no seeds or intervals.
- **Lodi-Tramontani** (2013 tutorial on the same topic) [S46]: not reached (HTTP 403).
- **Answer** [stated, caption, describing a team practice] (Toronto, 19 March 2021) [S51]. Asked how Gurobi avoids over-fitting to benchmark sets, he described the internal testing.
  - The test bed is constantly updated.
  - Admitted biases: toward the difficult models customers send, and toward models solvable in reasonable time.
  - Each test runs with five random seeds, averaged by geometric mean, on machines checked for comparability and kept free of other jobs.
  - He concedes that over-tuning can still be argued.
- [inferred] So by 2021 the variability critique had shaped the vendor's internal protocol. His public talk-level numbers still do not show it.

### 3.4 Chained products versus direct comparisons [inferred]
- [S2] pp. 116-117 multiplies eleven consecutive-version geometric means, each over a different subset (models solved by at least one of the pair), into "over 29,000". [S5] p. 32 prints 29,530x.
- Lodi's direct CPLEX 1.2-versus-11.0 geometric mean is 67.9, as relayed by Koch et al. [S16] p. 5.
- If both come from the same 2007 experiment, the gap shows how much the cumulative factor depends on chaining and on censoring at the time limit. The 30,000-s limit and the model counts match; Lodi was not read, so the shared source is not confirmed.
- No critic was found who makes this comparison explicitly. Bixby himself labels the 29,000 "projected" ([S2] p. 117).
- [stated, caption] In 2021 he criticised public benchmarks of an open-source solver whose ratios simply scale with the time limit because it times out on every model ([S51]). That is the censoring problem in another setting (see C10).

### 3.5 Showcase numbers and their generalisation (Q8)
- [practice, P] The production-planning model (401,640 rows, 1,584,000 columns) took 29.8 days with CPLEX 1.0, 1.5 hours with CPLEX 5.0 and 59.1 s with CPLEX 9.0, all on a 2.0 GHz Pentium 4: 43,500x ([S5] p. 14, 2017; [S4] p. 27, 2022).
- **Grace** (MIRI technical report 2013-3) [S29], [observed, P].
  - p. 36: of Grötschel's account of what appears to be the same model, the example was "very likely chosen to exhibit large speedups".
  - p. 4: retrospective analyses by interested authors should be read as optimistic, and assessments planned in advance are better.
  - p. 36: the 3,300x slide in a 2010 Bixby lecture did not specify the period or the class of LPs (that deck was not reached).
- **Sherry and Thompson** (NBER conference paper, July 2020, p. 1; journal version Proc. IEEE 2021) [S30], [observed, P]. PCAST 2010's claim that algorithms beat hardware rests on linear solvers, and they cite OR 2002 for it. That is one case study, so PCAST's sweeping conclusion is uncertain.
- [inferred] Neither critique faults his arithmetic. PCAST's 82 years equals 29.8 days times a machine factor of about 1,000, and its 43,000 matches his 43,500. What they fault is the use of a single, selected model. Bixby reports it next to test-set factors, but keeps it as the lead example (2017, 2022).

### 3.6 Design extensions and rival measurement schools
- **Fichte, Hecher, Szeider** (arXiv 2008.02215; CP 2020) [S31], [observed, P]. On p. 1 they cite Bixby's old-versus-new solver experiments, run on one modern computer, as inspiration (misspelt "Brixby"). Their "time leap" design runs new solvers on old hardware against old solvers on new hardware. [stated, P] Bixby posed the same thought experiment as a slide in 2017 and answered it: today's MIP technology on a 1991 machine would win by about 300x ([S5] p. 37). No experiment is shown.
- **Dolan and Moré** (Math. Program. 2002; arXiv cs/0102001) [S40], [observed, P]. pp. 1-2: averaging a metric forces either discarding failures or a subjective penalty. They propose performance profiles. They do not mention Bixby. [inferred] His time-limit substitution for unsolved models is such a penalty.
- **MIPLIB 2017** (Gleixner et al. 2021, p. 445) [S32], [observed, P]. Earlier MIPLIBs, including the 1992, 3.0 and 2010 editions he co-authored, were selected by hand by the committee; 2017 replaced this with a data-driven selection. Maher, Ralphs and Shinano (2021) [S33] stress how hard it is to know whether any test set is representative. Both points are general, not aimed at him.

---

## 4. Parallel simplex: an abandoned direction and its critics (Q4)

- [practice, (S)] **Bixby and Schwabacher**, Rice TR89-16, Nov 1989 [S6] (abstract only). One processor iterates while the other keeps refactorizing the basis. Some LPs solved in as little as 73% of one-processor time.
- [practice, (S)] **Bixby and Martin** (ZIB SC-95-45, Dec 1995; IJOC 2000) [S9]: not read, bot wall and INFORMS. Hall describes it as parallelising the column-related operations: PRICE, the dual ratio test and the dual update ([S18] p. 21).
- **Hall** (preprint 23 Apr 2007, p. 21; CMS 2010) [S18], [observed, P].
  - On the full Netlib set, the overhead of parallelism exceeded the gain, because few Netlib LPs have many more columns than rows.
  - Two networked Sun workstations gave little speed-up; up to 4 IBM SP2 processors gave 1 to 3. Four SGI processors gave near-linear speed-up on most LPs with more than 64 columns per row, oddly tailing off at the most extreme ratios.
  - Credit: the speed-ups were measured against a state-of-the-art serial code (CPLEX), and the paper is one of five that best represent the state of the art (p. 34).
  - Abstract: no parallel simplex for general large sparse LPs beats a good serial code by much.
- **Huangfu** (thesis 2013) [S20] and **Huangfu and Hall** (MPC 2018) [S19], [observed, P].
  - Bixby-Martin is the only published parallel dual simplex they know of. Though it appeared in the 2000s, it had neither bound flipping nor hyper-sparse solves ([S19] p. 120; [S20] p. 15).
  - Task parallelism of FTRAN and FTRAN-DSE was considered and rejected as computationally disadvantageous ([S19] pp. 124, 132).
  - Amdahl bound of about 1.5 on average, because the parallelised parts take under 35% of the time ([S20] p. 76). The profiling is Huangfu's, of his own code.
  - Overlapping INVERT (Ho-Sundarraj; Bixby-Schwabacher) reuses product-form etas, which Hall and McKinnon showed can be numerically unstable ([S20] p. 72).
- **Koberstein** (2005, p. 88) [S21], [observed, P]: **a failed replication.**
  - He tried the recommendation (cited to Bixby-Martin 2000, attributed to "Bixby") to keep a row-wise copy of only the nonbasic, nonfixed columns and update it at every basis change.
  - The result was bad on models with many more columns than rows, and no significant speed-up elsewhere. He switched to a complete row-wise copy.
- **Bixby's own verdict** [stated, P]. Simplex algorithms have not been parallelised successfully in the sense barrier has ([S1] p. 7). There has been essentially no success in parallelising simplex, while barrier parallelises well and the sequential crossover takes a growing share ([S2] p. 114).
- **How answered.** Conceded, and no reply to Hall or Huangfu was found. [inferred] The direction drops out of his texts after 2000. The 2022 deck draws "parallel barrier became the standard" from the AA/US Air story ([S4] p. 19), not parallel simplex.

---

## 5. Algorithm-choice verdicts and the interior-point school (Q5, Q6)

### 5.1 The 1994 published exchange
- ORSA J. Comput. 6(1), February 1994 [S25, S26], Crossref metadata only; texts not read (INFORMS).
  - Feature article by Lustig, Marsten, Shanno (pp. 1-14).
  - Commentaries by Bixby (pp. 15-22) [S8], Saunders (pp. 23-27), Todd (pp. 28-31) and Vanderbei (pp. 32-34).
  - LMS rejoinder "Rejoinder—The Last Word on Interior Point Methods for Linear Programming—For Now" (pp. 35-36).
- What is known from his side [stated, P]. The eight-model set he used in 1994 was motivated by LMS ([S1] p. 12). He later conceded their point that seven of those models were chosen for being hard for simplex ([S1] p. 14, note 10).
- Todd [S24] (preprint p. 10) observes that those problems were picked to be hard, which makes CPLEX 2.2's favourable showing more surprising. [observed, P]
- [observed] Lustig, a lead author on the interior-point side, later worked on CPLEX: credited in [S1] p. 14 and [S3] p. 3.

### 5.2 degen4 / LAU2 and John Gregory's advice
- [stated, P] Some concluded at the time that barrier was the right way and that further simplex work was pointless: "That conclusion was wrong." ([S1] p. 8).
- Named critic, in his later accounts: John Gregory (Cray Research). Gregory reported the OB1 barrier code solving the model in 1,200 s and advised giving up on simplex ([S4] p. 21; [S51], caption). Gregory's own account was not found (Gaps).
- **His answer, by experiment.** Primal on the explicit dual, then the dual with standard pricing, then dual steepest edge. On an HP9000/730 with CPLEX 3.0: dual steepest edge 273 s, barrier 1,400 s, dual with Dantzig pricing 2,440 s, primal with partial pricing 27,765 s ([S4] pp. 21-22).
- **Self-correction** [stated, P]. His own early conclusion that CPLEX 1.0 could not solve degen4 was "probably incorrect". It solved in about 1.5 days on the then-current 667 MHz ES40, and in about half an hour with perturbation ([S1] p. 8).

### 5.3 Verdicts that shift over time (see C1)
- **1998 to about 2000.**
  - Todd (preprint p. 6) [S24] quotes Bixby et al. (2000) [S10]: in 1998 they would have called barrier clearly best for large models; by about 2000 there was no clear best, and each algorithm won in many important instances.
  - Todd also reports that the authors said their figures could be read as biased against barrier, and summarises Bixby's seminar conclusion that dual steepest edge was fastest on a suite of large problems.
  - Todd sets this beside Koopmans' warning that any method good on one data set can be beaten on another (p. 3).
  - Status: [stated] via [observed], (S); the original 2000 text was not read.
- **2002.** For CPLEX, barrier is overall the most powerful single algorithm, by a narrow margin that grows with size. Dual is about twice as fast as primal, and each of the three wins often ([S1] pp. 7, 13). Simplex still dominates in practice because MIP needs warm re-solves (p. 7).
- **2012.** Primal now rarely wins; dual and barrier dominate; barrier increasingly wins large LPs solved from scratch ([S2] p. 114).
- **2021-2022.** Dual steepest edge is "today's LP algorithm of choice" ([S4] p. 22) and still the most common basic algorithm ([S51], caption).

### 5.4 Castro: specialized interior-point methods versus general dual simplex (Q6)
- [stated, P] OR 2002 p. 9 names Castro (2000) as the most recent and best special-purpose algorithm for the PDS multicommodity models, and says it is now dominated by general dual simplex codes. The tests were PDS and one mnetgen24 model.
- **Castro 2003** (Annals OR 124:35-48) [S22], [observed, P].
  - He compares CPLEX 6.5 with his specialized IPM on Mnetgen, PDS, Tripart and Gridgen instances.
  - p. 47: there seems to be no single best algorithm for multicommodity flows.
  - pp. 46-47: behaviour depends on structure more than size. Interior point suits sparse networks and simplex dense ones, and a decision rule is hard to state.
  - p. 47: he thanks Bixby for pointing him to the difficult Gridgen and Tripart instances.
- **Castro 2007** (COAP 36, p. 196) [S23], [observed, P]. He cites OR 2002 both for calling his method the most efficient IPM and for simplex now solving formerly hard models in seconds. He adds that specialized IPMs still do better on some recent multicommodity instances, citing his own 2003 and 2005 papers.
- **How answered.** No reply by Bixby found. [inferred] Castro's 2003 tests used CPLEX 6.5, not the 7.1 of OR 2002, so they qualify the claim rather than refute it like for like.

### 5.5 The first-order (PDLP) school and "LP is a solved problem" [inferred link]
- [stated, P] Practitioners consider LP a solved problem, and large models are solved robustly and quickly ([S5] p. 15; [S4] p. 29). In 2017 he also warned that some LP applications remain hard: about 2% of MIPs are blocked by LP, and he cites financial transmission-right auctions ([S5] p. 16).
- **PDLP** (Applegate et al., arXiv 2501.07018v2, March 2026) [S38], [observed, P].
  - Eleven LPs with 125 million to 6.3 billion nonzeros.
  - Gurobi barrier hit the 1 TB memory limit on eight of them; primal and dual simplex were too slow (abstract, p. 1).
  - PDLP solved eight of the eleven to a 1% gap, under looser termination than Gurobi's defaults (results, p. 17).
  - The paper does not cite Bixby's progress papers. [inferred] It bounds his claim at extreme scale, where factorization memory is the limit.
- [stated, caption] In 2021 he called a large Google study of machine learning for MIP largely unsuccessful in practice ([S51]). The paper is not identified in the caption.

---

## 6. The initial (crash) basis and its benchmarks (Q7)
- **The 1992 paper itself** [S7]: only its abstract was read; the full text and SC 92-11 were not reached. Todd (preprint pp. 9-10) [S24] relays its iteration evidence: CPLEX 1.0 on 90 Netlib LPs needed at most three times the row count in iterations on 72 of them. [observed, (S)]
- **Fan et al.** (ICML 2023, PMLR 202, pp. 7-8) [S34], [observed, P].
  - They reimplemented "CPLEX Crash (CA) (Bixby, 1992)" in HiGHS and in Huawei's OptVerse, presolve off, dual simplex.
  - OptVerse (their Table 1): on STOCH, CA cut iterations from 75.3K to 52.5K but time rose from 44.6 to 61.3 s; on SC-2, time rose from 348.7 s to 1.3K s.
  - HiGHS (Table 2): CA improved STOCH (718.7 to 553.9 s) but slowed SC-1 (21.3 to 62.9 s) and SC-2 (194.4 to 336.6 s).
  - Their diagnosis (p. 7): CA aims at good numerical properties rather than nearness to the optimum, so only the first iterations speed up and the iteration count need not fall. They also claim CA only works for problems with equality constraints, which I did not check against the 1992 paper.
  - Caveats: reimplementation fidelity unknown; two of the six data sets are private; the authors propose a rival (a GNN).
- **Parker et al.** (arXiv 2610.20892v1, 14 Oct 2026, p. 3) [S35], [observed, P]. Crash bases, Bixby 1992 among them, can cut iterations without cutting time: denser bases slow each iteration, and steepest-edge weights are costly to initialise. They attribute the point to Koberstein (2005).
- **Ploskas, Sahinidis, Samaras** (MPC 2021) [S36], [observed, (S), abstract only]. Their METIS-based sparse starting bases beat CPLEX 12.6.1's default crash: 5% lower geometric-mean primal time over 95 benchmarks, 37% on hard instances, 10% for dual on hard instances, and more than 10x on numerically difficult ones. Whether CPLEX 12.6.1's default crash is still the 1992 procedure is not established.
- **Maros and Mitra** (IJOC 1998) [S37] review earlier crash procedures and propose three new ones (Crossref abstract). Their comparison with the CPLEX basis was not read.
- [inferred] The common thread: evidence for crash procedures is often given in iterations, and later critics show that iterations mislead. Whether Bixby 1992 also reported times is not known (not read).

---

## 7. Priority and credit for the dual simplex (Q10)
- [stated, P] Asked in 2015 whether dual steepest edge was already in OSL, he answered "Back then, dual didn't really exist." He described the dual as a weak sister used only inside MIP, and its use as a first-class LP algorithm as a new idea ([S3] p. 3). In the same interview he says OSL was "certainly better" than CPLEX until about 1992.
- [stated, P] The 2022 deck says of the LAU2 episode: "This led to the development of dual steepest edge" ([S4] p. 22).
- **Counter-evidence** [observed, (S), abstract]. Forrest and Goldfarb (Math. Program. 57, May 1992) [S27] present new steepest-edge algorithms, dual variants included, tested on large real-world LPs, with steepest edge unambiguously superior.
- **His own hedged versions** [stated, P]:
  - OR 2002 p. 8: the final piece of the puzzle came from Forrest and Goldfarb (1992).
  - Documenta p. 113: CPLEX's dual steepest edge uses the variant of [16] (Forrest-Goldfarb).
  - Documenta p. 110: an explicit dual phase I did not seem to emerge until the mid-1990s.
  - The 2015 and 2021 lectures credit Goldfarb by name ([S50], [S51], captions).
- [inferred] The defensible claim is narrower: CPLEX made the dual (with dual steepest edge and a dual phase I) the default general-purpose LP algorithm. The pricing method is Forrest and Goldfarb's. No published objection by Forrest, Goldfarb or IBM was found.

---

## 8. Closed commercial codes and academic research (Q11)
- **The challenge** [observed, P]. The Optima interviewers (Kaibel, Lee, Linderoth; October 2015) said commercial solvers had put academic computational integer programming nearly out of business. They added that impactful ideas are hard to show without the solver internals ([S3] p. 6).
- **His answer** [stated, P]:
  - it is hard to test whether any idea is good;
  - the most an academic can expect is a little supportive testing, after which commercial developers try the idea;
  - Gurobi has "no interest in making this hard";
  - cut management is one area where outside help would be welcome;
  - relatively little has come from research in about the last ten years: RINS was big, symmetry less so ([S3] p. 6).
- **Repeated** [stated, caption]. In 2021: not a single idea from the published literature entered the MIP code in the last five years, though LP gained "soft symmetry" ([S51]). In the 2023 interview excerpt: much the same, soft symmetry in LP and nothing recent in MIP that he knows of ([S53]).
- **Counterpoints.**
  - Koberstein [S21] pp. 2-3 blames the open-source gap on commercial non-publication [observed, P].
  - [inferred] Koch et al. [S16] p. 13 attribute MILP gains partly to ideas from the open literature (local branching, MCF cuts, conflict analysis, orbital symmetry), but they do not date when each entered which code. The tension is weak.

---

## 9. Predictions and how they fared (Q9)
- **P1, 2012** ([S2] p. 115): no improvement in standard LP algorithms since 2004, and LP is "threatening in the future to again become a significant bottleneck"; about 2% of MIPs are blocked by LP.
  - His own follow-ups: 2017 repeats little progress since 2004 ([S5] p. 16). By 2021-2022 nothing happened from 2004 to about 2015, then about 3x on large models ([S4] p. 28; [S51], caption).
  - Outside evidence: Koch et al. find about 9x for the virtual best over 2001-2020, from algorithm choice, 64-bit memory and parallel barrier ([S16] pp. 13, 25). The PDLP study shows barrier memory limits at extreme scale ([S38]).
  - [inferred] Partly borne out; revised by him in talks, not in print.
- **P2, 2012** ([S2] p. 118): MIP progress "shows no signs of stopping".
  - Outcome: Gurobi 1.0 to 7.0 gave 43.2x cumulative by 2017 ([S5] p. 36). Koch et al.: about 50x over 2001-2020, solvers "still going strong", but each new idea helps a smaller subset of instances ([S16] p. 27).
  - [inferred] Continued, but slower than the 1998 CPLEX 6.5 jump. The test sets differ.
- **P3, about 1998**: barrier clearly best for large models. Withdrawn by about 2000 ([S24] p. 6, quoting [S10]).
- **P4, 2002**: the PDS-type models have become easy LPs and Castro's specialized IPMs are dominated ([S1] pp. 9-10). Qualified by Castro ([S22], [S23]).
- **P5, 2002**: LP application remains largely the domain of experts, with abstraction the hurdle ([S1] p. 14). No critique found.

---

## 10. Misreadings and relay errors by citers (check before reuse)
- **Huangfu** ([S20] p. 61) says Bixby attributed the major CPLEX 5.0-to-7.1 gain to more aggressive dual perturbation. OR 2002 p. 9 lists perturbation as one of three causes (with sparsity and bound flipping), and for the PDS models only.
- **Huangfu** ([S20] p. 72) gives Bixby-Schwabacher a speed-up of 1.3. The report's abstract gives a best case of 73% of one-processor time, about 1.37x ([S6]).
- **Koberstein** ([S21] p. 88) attributes a Bixby-Martin (2000) recommendation to Bixby alone.
- **Tar, Stágel, Maros** (CEJOR 2017) [S43], (S2 context) credit Bixby 2002 with LP software becoming 10^5 times faster over 50 years. OR 2002 claims about six orders of magnitude over roughly 1987-2002 ([S1] p. 14).
- **Fan et al.** ([S34] p. 7) say CA works only for problems with equality constraints. This is unchecked: the 1992 paper was not read.
- **Grace** ([S29] p. 36) reads a May 2010 slide as showing little LP progress from 2004 to 2011. A 2010 lecture cannot cover 2011; the deck was not reached, so it is unknown whether the slide or the reading is at fault.
- **Fichte et al.** ([S31] p. 1) spell him "Brixby". Trivial, but it breaks name searches.

---

## 11. Reporting slips found in this run [inferred; no critic found raising them]
- [S2] p. 114 table: "Total improvement (3300 · 2000): 5,280,000×", while the machine row prints 1600×. Since 3,300 x 1,600 = 5,280,000, the "2000" is a misprint. Checked on the rendered PDF page.
- [S2] reference [7] gives OR 2002 as pp. 1-13. Crossref gives pp. 3-15.
- The 2007 MIP test set is 1,892 models in [S2] p. 116 and 1,852 in [S5] p. 30. The ECCO slide's own arithmetic (2,791 - 559 - 348 - 22) gives 1,862.
- Gurobi 1.0 to 5.0: 16.2x in [S2] p. 118, but 9.3x cumulative in [S5] p. 36. Neither text explains the difference (different sets or years are likely).
- [S5] p. 36 says "over 1.3 million X" since 1991. The two printed factors give 29,530 x 43.2, about 1.28 million ([S5] pp. 32, 36).

---

## 12. How Bixby handles critique (pattern for Phase 2)
1. **Names the contestable choice and keeps it**: the vendor-code caveat ([S1] p. 4), the best-of-three aside ([S2] p. 114), "accept it or not" ([S51], caption), the LMS selection point (note 10).
2. **Answers rivals with new runs, not argument**: the 1994 re-runs of the LMS models, the forward chain in 2002, the twelve-version re-run in 2007, the LAU2 timing table.
3. **Concedes candidly where his own data show limits**: parallel simplex; OSL better until about 1992; MINTO ahead early; no anti-degeneracy in early CPLEX; figures biased against barrier around 2000.
4. **Revises in talks, not in print**: LP progress after 2004 (2012, 2017, 2021, 2022). No erratum or retraction found.
5. **Withholds method detail in print and explains it selectively in lectures** (2015). He attributes the gaps to laziness or to never getting round to it, not to secrecy.
6. **Hands rivals hard instances**: Castro's Gridgen and Tripart ([S22] p. 47).
7. **No published reply to any critic after 1994 was found.**
8. **His own targets as a critic**: the advice to give up on simplex (1989), special-purpose interior-point codes (2002), academic MIP research output (2015-2023), open-source benchmarks (2021), a large ML-for-MIP study (2021).

---

## Contradictions (kept, not reconciled)
- **C1. Which LP algorithm is best.**
  - About 1998: barrier clearly best for large models (Bixby et al., via [S24] p. 6).
  - About 2000: no clear best (same source).
  - 2002: barrier the most powerful single algorithm, by a narrow margin ([S1] pp. 7, 13).
  - 2012: dual and barrier dominate, barrier increasingly ([S2] p. 114).
  - 2022: dual steepest edge "today's LP algorithm of choice" ([S4] p. 22).
- **C2. degen4 versus LAU2.** The dimensions agree in [S1] p. 8 and [S4] p. 20: 4,420 rows, 6,711 columns, 101,377 nonzeros. The details do not:
  - Name: "degen4" in 2002, "LAU2" in 2015 and 2022.
  - Date: a challenge set in late 1989 ([S1] p. 8) versus a first run in 1987 ([S4] p. 21).
  - Machine for his CPLEX run: Cray Y-MP ([S1] p. 8; [S3] p. 3) versus X-MP ([S4] p. 21).
  - CPLEX version: 1.0 ([S1], [S4]) versus "1.something or maybe 2" ([S3] p. 3).
  - Machine for the OB1 run: Y-MP ([S1] p. 8) versus X-MP ([S51], caption).
- **C3. Who originated the dual-simplex approach.** "dual didn't really exist" ([S3] p. 3) and "This led to the development of dual steepest edge" ([S4] p. 22), against Forrest-Goldfarb 1992 [S27] and his own credit to them ([S1] p. 8; [S2] p. 113).
- **C4. MIP test-set size.** 1,892 ([S2] p. 116) versus 1,852 ([S5] p. 30), with the slide's arithmetic giving 1,862. Lodi, via [S16] p. 5: 1,734 for the speed-up and 1,852 for the solved shares.
- **C5. Gurobi 1.0 to 5.0.** 16.2x ([S2] p. 118) versus 9.3x ([S5] p. 36).
- **C6. Chained versus direct.** "Over 29,000", projected ([S2] p. 117), versus a direct 67.9 (Lodi via [S16] p. 5). These are different estimands; the tension is kept.
- **C7. LP progress after 2004.** "Essentially no improvements" (2012) and "little progress" (2017), versus about 3x on large models since about 2015 (2021, 2022), versus about 9x for the virtual best over 2001-2020 (Koch et al.).
- **C8. Self-account versus others' accounts.**
  - He says he basked in others' MIP glory and did zero development at Gurobi ([S3] p. 4). Grötschel (a close colleague, not an outside critic; [S3] p. 7) says he very humbly plays down his role. Cook (co-author; [S3] p. 7) stresses his motto "if you see something, then fix it" and his attention to detail.
  - He calls bound shifting his most important contribution, yet it is unpublished ([S3] p. 4).
- **C9. What Bixby-Martin parallelised, and how well.**
  - Components: PRICE, dual ratio test, dual update ([S18] p. 21); spmv, chuzc, update-dual ([S19] p. 132); Huangfu's thesis adds chuzr ([S20] p. 76).
  - Speed-up: near linear on 4 SGI processors for more than 64 columns per row ([S18] p. 21), against an Amdahl bound of about 1.5 on average from Huangfu's own profiling ([S20] p. 76).
- **C10. Censoring at the time limit.** He criticises public benchmark ratios that scale with the time limit ([S51], 2021, caption). His MIP version-pair ratios substitute the time limit for unsolved runs, limited to models solved by at least one version ([S2] p. 116).
- **C11. Dominated (OR 2002) versus structure-dependent (Castro).** [S1] p. 9 versus [S22] pp. 46-47 and [S23] p. 196.
- **C12. team.json premise versus this run's corpus.** team.json calls the September 2022 Hausdorff deck the latest dated trace. Agent 02 saved a caption excerpt of an interview uploaded 2023-12-07 [S53], with the recording year inferred as 2023 by that agent. **This file states nothing about living status or present role.** The discrepancy is for the user to weigh.

---

## Gaps
- **ZIB reports not reached.** SC 92-11 (crash basis, German) and SC-95-45 (parallel dual) sit behind an Anubis bot check on opus4.kobv.de, which was not bypassed. The crash evaluation and the parallel-dual design are known here only through others ([S18], [S19], [S20], [S24]).
- **INFORMS texts not read**: Bixby's 1994 commentary, the LMS feature and rejoinder and the other commentaries, Bixby-Martin 2000, the Maros-Mitra 1998 comparisons, and Lodi-Tramontani 2013 (HTTP 403).
- **Closed chapters not read**: Bixby et al. 2000 and 2004; Bixby-Rothberg 2007; MIPLIB 2010 (co-signed; whether it treats performance variability was not checked); Lodi 2010; Achterberg-Wunderling 2013; Koch-Martin-Pfetsch 2013; Mittelmann-Pruessner 2006 (its S2 context may cite OR 2002 as an example of multiple test sets, so the valence is unknown); Tar et al. 2017; the published version of Todd 2002 (the preprint was read).
- **No critic found who explicitly objects to the private model libraries** behind his LP and MIP numbers; the point is [inferred]. No independent re-run of his CPLEX 1.0-to-7.1 or 1.2-to-11 series, and no replication of the 43,500x model, which is not public.
- **No published reply by Bixby to any critic after 1994**, and no errata or retractions. Publisher erratum pages were not searched systematically. Referee reports and rejected submissions are not public; none were found.
- **John Gregory's own account** of the degen4/LAU2 advice was not found.
- **Gurobi-era claims not independently checked**: Gurobi 1.0 roughly equal to CPLEX 11.0 on the 2009 Mittelmann runs ([S2] pp. 117-118; [S5] p. 36) and the version factors. Archived Mittelmann pages were not consulted (web.archive.org not used).
- **Decks not reached**: the 2010 CIRRELT lecture cited by Grace (connection refused) and the Bath-hosted 2015 deck (redirect). Tutte 2013 and Imperial 2015 decks were not found in this run.
- **Not checked**: whether the TSP book ("Applegate et al. (forthcoming)" in OR 2002) holds the promised simplex details.
- **Koberstein 2005 read only at pp. 2-3, 63 and 88**; his dual phase I comparisons, which may involve CPLEX, were not read.
- **No MIP-specific critique found** of the 1998 CPLEX 6.5 jump attribution or of the component-ablation tables of 2004 and 2007, beyond Koch et al.'s general remark on feature attribution ([S16] pp. 12-13).
- **About five minutes without useful results, so moved on**: critiques by other vendors of the 2009 claim that Gurobi 1.0 roughly matched CPLEX 11.0; academic replies to his remarks that little from research reached the MIP code.
- **Out of scope by instruction**: living status and present role.

---

## Sources

One line each: title, author(s), date, identifier or URL, primary/secondary, and what was read. Identifiers were checked with Crossref, arXiv, Unpaywall, OpenAlex, Semantic Scholar or the Rice repository in this run. Page numbers in the text refer to the read version named here.

1. [S1] "Solving Real-World Linear Programs: A Decade and More of Progress", R. E. Bixby, Operations Research 50(1):3-15, Jan-Feb 2002, DOI 10.1287/opre.50.1.3.17780; read in full via the open mirror gwern.net/doc/cs/algorithm/2002-bixby.pdf (printed p. N = PDF p. N-2) (primary)
2. [S2] "A Brief History of Linear and Mixed-Integer Programming Computation", R. E. Bixby, Documenta Math. Extra Vol. ISMP (2012) 107-121, DOI 10.4171/dms/6/16; read in full via maths.tcd.ie/EMIS/journals/DMJDMV/vol-ismp/25_bixby-robert.pdf (primary)
3. [S3] "You have to figure out who your customer is going to be - An interview with Bob Bixby" (questions by V. Kaibel, J. Lee, J. Linderoth, October 2015), with comments by M. Grötschel and W. Cook, Optima 101, September 2016, mathopt.zib.de/Optima-Issues/optima101.pdf; read pp. 1-7 (primary: interview; secondary: comments)
4. [S4] "Linear Programming: A Historical View", R. E. Bixby, Hausdorff School deck, September 2022 (PDF created 13 Sep 2022), www.or.uni-bonn.de/~held/hausdorff_school_22/slides/GUR_Hausdorff_Day1_LP_History.pdf; read all 30 pages (primary)
5. [S5] "Computational Progress in Linear and Mixed Integer Programming", R. E. Bixby, ECCO 2017 invited lecture deck (PDF title "ECCO_Lecture_5May2017", 38 pages), ecco2017.euro-online.org/en/resources/files/invited-speakers/robertbixby.pdf; read all (primary; new to this corpus)
6. [S6] "Solving Linear Programs with Two Processors", R. E. Bixby, M. Schwabacher, Rice University Technical Report TR89-16, November 1989, hdl.handle.net/1911/101665; abstract read via the repository API, full text not read (primary)
7. [S7] "Implementing the Simplex Method: The Initial Basis", R. E. Bixby, ORSA J. Comput. 4(3):267-284, 1992, DOI 10.1287/ijoc.4.3.267; abstract only (OpenAlex), not read (primary)
8. [S8] "Commentary—Progress in Linear Programming", R. E. Bixby, ORSA J. Comput. 6(1):15-22, 1994, DOI 10.1287/ijoc.6.1.15; Crossref metadata only, not read (primary)
9. [S9] "Parallelizing the Dual Simplex Method", R. E. Bixby, A. Martin, INFORMS J. Comput. 12(1):45-56, 2000, DOI 10.1287/ijoc.12.1.45.11902; metadata only, not read (primary)
10. [S10] "MIP: Theory and Practice — Closing the Gap", R. E. Bixby, M. Fenelon, Z. Gu, E. Rothberg, R. Wunderling, System Modelling and Optimization (IFIP), 2000, pp. 19-49, DOI 10.1007/978-0-387-35514-6_2; not read, one passage via [S24] (primary)
11. [S11] "Mixed-Integer Programming: A Progress Report", R. E. Bixby, M. Fenelon, Z. Gu, E. Rothberg, R. Wunderling, The Sharpest Cut, ch. 18, SIAM 2004, pp. 309-325, DOI 10.1137/1.9780898718805.ch18; not read, figures via [S16] (primary)
12. [S12] "Progress in computational mixed integer programming—A look back from the other side of the tipping point", R. E. Bixby, E. Rothberg, Annals of OR 149:37-41, 2007, DOI 10.1007/s10479-006-0091-y; not read (primary)
13. [S13] "Very Large-Scale Linear Programming: A Case Study in Combining Interior Point and Simplex Methods", R. E. Bixby, J. Gregory, I. J. Lustig, R. E. Marsten, D. F. Shanno, Operations Research 40(5):885-897, 1992, DOI 10.1287/opre.40.5.885; metadata only, not read (primary)
14. [S14] "Recovering an optimal LP basis from an interior point solution", R. E. Bixby, M. J. Saltzman, Operations Research Letters 15(4):169-178, 1994, DOI 10.1016/0167-6377(94)90074-4; metadata only, not read (primary)
15. [S15] "MIPLIB 2010", T. Koch, T. Achterberg, E. Andersen, O. Bastert, T. Berthold, R. E. Bixby et al., Mathematical Programming Computation 3(2):103-163, 2011, DOI 10.1007/s12532-011-0025-9; metadata only, not read (primary, co-signed)
16. [S16] "Progress in mathematical programming solvers from 2001 to 2020", T. Koch, T. Berthold, J. Pedersen, C. Vanaret, EURO J. Comput. Optim. 10:100031, 2022, DOI 10.1016/j.ejco.2022.100031; arXiv 2206.09787v2 read in full (secondary)
17. [S17] "Hyper-sparsity in the revised simplex method and how to exploit it", J. A. J. Hall, K. I. M. McKinnon, preprint 8 Oct 2002 (webhomes.maths.ed.ac.uk/hall/HyperSparsity/HyperSparsityOctober2002.pdf), published COAP 32(3):259-283, 2005, DOI 10.1007/s10589-005-4802-0; preprint read pp. 1-2, 23 (secondary)
18. [S18] "Towards a practical parallelisation of the simplex method", J. A. J. Hall, preprint 23 Apr 2007 (webhomes.maths.ed.ac.uk/hall/ParSimplexRevised/ParSimplexApril2007.pdf), published Computational Management Science 7(2):139-170, DOI 10.1007/s10287-008-0080-5; preprint read pp. 1, 20-22, 34 (secondary)
19. [S19] "Parallelizing the dual revised simplex method", Q. Huangfu, J. A. J. Hall, Mathematical Programming Computation 10(1):119-142, 2018, DOI 10.1007/s12532-017-0130-5 (open access, webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf); read pp. 120, 124, 132 (secondary)
20. [S20] "High performance simplex solver", Q. Huangfu, PhD thesis, University of Edinburgh, 2013, era.ed.ac.uk/handle/1842/7952; read printed pp. 15, 61, 63, 71-73, 76, 89 (PDF page = printed + 1) (secondary)
21. [S21] "The dual simplex method, techniques for a fast and stable implementation", A. Koberstein, PhD thesis, Universität Paderborn, submitted Nov 2005, digital.ub.uni-paderborn.de/hsmig/download/pdf/3885; read pp. 2-3, 63, 88 (secondary)
22. [S22] "Solving Difficult Multicommodity Problems with a Specialized Interior-Point Algorithm", J. Castro, Annals of OR 124:35-48, 2003, DOI 10.1023/B:ANOR.0000004761.99649.a5; read in full (author copy www-eio.upc.edu/~jcastro/publications/papers/anor2003.pdf) (secondary)
23. [S23] "An interior-point approach for primal block-angular problems", J. Castro, Computational Optimization and Applications 36:195-219, 2007, DOI 10.1007/s10589-006-9000-1; read pp. 195-196 and references (author copy coap2007.pdf) (secondary)
24. [S24] "The many facets of linear programming", M. J. Todd, Mathematical Programming 91(3):417-436, 2002, DOI 10.1007/s101070100261; preprint (7/00, people.orie.cornell.edu/miketodd/ismplp3.ps) read pp. 1-10 (secondary)
25. [S25] "Feature Article—Interior Point Methods for Linear Programming: Computational State of the Art", I. J. Lustig, R. E. Marsten, D. F. Shanno, ORSA J. Comput. 6(1):1-14, 1994, DOI 10.1287/ijoc.6.1.1; with their "Rejoinder—The Last Word on Interior Point Methods for Linear Programming—For Now", 6(1):35-36, DOI 10.1287/ijoc.6.1.35; Crossref metadata only, not read (secondary)
26. [S26] The other 1994 commentaries: M. A. Saunders, "Commentary—Major Cholesky Would Feel Proud", 6(1):23-27, DOI 10.1287/ijoc.6.1.23; M. J. Todd, "Commentary—Theory and Practice for Interior-Point Methods", 6(1):28-31, DOI 10.1287/ijoc.6.1.28; R. J. Vanderbei, "Commentary—Interior-Point Methods: Algorithms and Formulations", 6(1):32-34, DOI 10.1287/ijoc.6.1.32; metadata only, not read (secondary)
27. [S27] "Steepest-edge simplex algorithms for linear programming", J. J. Forrest, D. Goldfarb, Mathematical Programming 57:341-374, May 1992, DOI 10.1007/BF01581089; abstract read on the Springer page (secondary)
28. [S28] "Performance variability in mixed integer programming", E. Danna (ILOG CPLEX R&D), MIP 2008 workshop slides (PDF created 7 Aug 2008), coral.ie.lehigh.edu/~jeff/mip-2008/talks/danna.pdf; read all 40 slides (secondary)
29. [S29] "Algorithmic Progress in Six Domains", K. Grace, MIRI Technical Report 2013-3, last modified 9 Dec 2013, intelligence.org/files/AlgorithmicProgress.pdf; read pp. 2-4, 35-36 (secondary)
30. [S30] "Measuring the Pace of Innovation: Evidence from Algorithms", Y. Sherry, N. C. Thompson, NBER conference paper (PDF dated 6 Jul 2020), conference.nber.org/conf_papers/f138756.pdf; read p. 1. Journal version "How Fast Do Algorithms Improve? [Point of View]", Proc. IEEE 109(11):1768-1777, 2021, DOI 10.1109/JPROC.2021.3107219, metadata only (secondary)
31. [S31] "A Time Leap Challenge for SAT Solving", J. K. Fichte, M. Hecher, S. Szeider, arXiv 2008.02215v2 (2020), CP 2020, LNCS pp. 267-285, DOI 10.1007/978-3-030-58475-7_16; arXiv read p. 1 (secondary)
32. [S32] "MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library", A. Gleixner et al., Mathematical Programming Computation 13:443-490, 2021, DOI 10.1007/s12532-020-00194-3 (CC BY-SA); read pp. 444-445 and the benchmark-criteria section (secondary)
33. [S33] "Assessing the Effectiveness of (Parallel) Branch-and-bound Algorithms", S. J. Maher, T. K. Ralphs, Y. Shinano, arXiv 2104.10025v1, April 2021; read the test-set section (secondary)
34. [S34] "Smart Initial Basis Selection for Linear Programs", Z. Fan, X. Wang, O. Yakovenko, A. A. Sivas, O. Ren, Y. Zhang, Z. Zhou, ICML 2023, PMLR 202, proceedings.mlr.press/v202/fan23d.html; read pp. 1-2, 7-8 (secondary)
35. [S35] "Learning Warm Starts for the Simplex Method from Measured Solver Cost", F. Parker, D. A. Ripsman, E. Springer, K. Ghobadi, arXiv 2610.20892v1, 14 Oct 2026; read pp. 1-3 (secondary)
36. [S36] "A triangulation and fill-reducing initialization procedure for the simplex algorithm", N. Ploskas, N. Sahinidis, N. Samaras, Mathematical Programming Computation 13(3):491-508, 2021, DOI 10.1007/s12532-020-00188-1; abstract read (secondary)
37. [S37] "Strategies for Creating Advanced Bases for Large-Scale Linear Programming Problems", I. Maros, G. Mitra, INFORMS J. Comput. 10(2):248-260, 1998, DOI 10.1287/ijoc.10.2.248; Crossref abstract only (secondary)
38. [S38] "PDLP: A Practical First-Order Method for Large-Scale Linear Programming", D. Applegate, M. Díaz, O. Hinder, H. Lu, M. Lubin, B. O'Donoghue, W. Schudy, arXiv 2501.07018v2, 18 Mar 2026; read abstract, introduction, results p. 17 (secondary)
39. [S39] "Does Your Computation Belong on a Supercomputer?", C. Thomborson, University of Minnesota Duluth, Technical Report 91-04, May 1991, www.cs.auckland.ac.nz/~cthombor/Pubs/Old/9104.pdf; read pp. 1-4, 8 (secondary; relays Bixby's private correspondence of September 1990)
40. [S40] "Benchmarking optimization software with performance profiles", E. D. Dolan, J. J. Moré, Mathematical Programming 91(2):201-213, 2002, DOI 10.1007/s101070100263; arXiv cs/0102001v2 read pp. 1-2 (secondary)
41. [S41] "Progress in Academic Computational Integer Programming", T. Koch, A. Martin, M. E. Pfetsch, Facets of Combinatorial Optimization (Springer 2013) 483-506, DOI 10.1007/978-3-642-38189-8_19; S2 citation context only (secondary)
42. [S42] "A server for automated performance analysis of benchmarking data", H. Mittelmann, A. Pruessner, Optimization Methods and Software 21(1):105-120, 2006, DOI 10.1080/10556780500065366; S2 citation context only, valence unclear (secondary)
43. [S43] "Parallel search paths for the simplex algorithm", P. Tar, B. Stágel, I. Maros, Central European Journal of OR 25(4):967-984, 2017, DOI 10.1007/s10100-016-0452-9; S2 citation context only (secondary)
44. [S44] "Mixed Integer Programming Computation", A. Lodi, in 50 Years of Integer Programming 1958-2008, Springer, pp. 619-645, DOI 10.1007/978-3-540-68279-0_16; not read, figures via [S16] p. 5 (secondary)
45. [S45] "Mixed Integer Programming: Analyzing 12 Years of Progress", T. Achterberg, R. Wunderling, Facets of Combinatorial Optimization (Springer 2013) 449-481, DOI 10.1007/978-3-642-38189-8_18; not read, figures via [S16] p. 4 (secondary)
46. [S46] "Performance Variability in Mixed-Integer Programming", A. Lodi, A. Tramontani, INFORMS TutORials 2013, DOI 10.1287/educ.2013.0112; not reached (HTTP 403) (secondary)
47. [S47] "George B. Dantzig and systems optimization", P. E. Gill, W. Murray, M. A. Saunders, J. A. Tomlin, M. H. Wright, Discrete Optimization 5(2):151-158, 2008, DOI 10.1016/j.disopt.2007.01.002; S2 citation context only (praises OR 2002 as a careful analysis) (secondary)
48. [S48] Semantic Scholar Graph API citation contexts for S1, S7, S8, S9, S10, S11 and S12, fetched 2026-11-05 (431, 191, 65, 43, 17, 124 and 236 citing records), api.semanticscholar.org; filtered by keyword (secondary, tool data)
49. [S49] "An Overview of GPU-based First-Order Methods for Linear Programming and Extensions", H. Lu, J. Yang, arXiv 2506.02174v1, 2 Jun 2025; consulted for rival-school context, no Bixby-specific content, not used (secondary)
50. [S50] "Robert Bixby: Solving Linear Programs: The Dual Simplex Algorithm" (three parts), CO@Work 2015 lectures, Zuse Institute Berlin, YouTube z1xvqwQR6xU, ZNf84y4M-Dw, uccbVoamiUM (uploaded 2016); uploaded-subtitle caption transcript saved by agent 02 at `references/sources/talks/co-at-work-2015-dual-simplex-lectures.transcript.txt`; read Part 1 opening and Part 3 passages (primary, caption)
51. [S51] "Optimization: Past, Present, Future", R. E. Bixby, MIE Distinguished Seminar, University of Toronto, 19 March 2021, YouTube _R8-nt5NyiE; automatic caption transcript saved by agent 02 at `references/sources/talks/toronto-2021-optimization-past-present-future.transcript.txt`; read lines on LAU2, LP progress and the Q&A (primary, caption)
52. [S52] Two short clips (Prendismo 2015; Gurobi channel 2020, "How was Gurobi founded?"), caption transcript saved by agent 02 at `references/sources/talks/short-clips-2015-2020.transcript.txt`; skimmed, nothing critique-relevant (primary, caption)
53. [S53] "Subject to: Robert Bixby", YouTube 47BZgFhEFJ8, uploaded 2023-12-07; automatic caption excerpt saved by agent 02 at `references/sources/talks/subject-to-2023-interview.excerpt.transcript.txt`; read the passages on academic ideas and on a possible LP paper only (primary, caption)
