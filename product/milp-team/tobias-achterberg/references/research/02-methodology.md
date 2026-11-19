# Tobias Achterberg · 02 Stated methodology (what he says research should be)

| Field | Value |
|---|---|
| Researcher | Tobias Achterberg (living). Wrote SCIP from scratch at ZIB from 2001/2002 (dates differ, see Contradictions C4). Doctoral thesis *Constraint Integer Programming*, TU Berlin, defended 12 July 2007 (advisor Martin Grötschel; second referee Robert E. Bixby). CPLEX developer at ILOG/IBM from 2006, lead MIP developer for CPLEX 12.0–12.6 according to Gurobi's 2014 press release. At Gurobi since 2014: Director of Development in the December 2019 webinar description, Vice President of R&D in the December 2020 one. DBLP 71/6632, ORCID 0000-0002-0862-7065 (team.json). |
| Dimension | Research agent 02 of 06: stated methodology. This note records his claims about how MIP-solver research and development should be chosen, run, measured, judged, written up and organised, sorted into the seven layers of `references/research-extraction-framework.md` §一. Whether he practises them is agent 03's job. |
| Research date | 2026-11-08 |
| Sources consulted | 31 sources, listed under Sources. 19 are primary. Four are written texts of his alone: the thesis, ZR 04-19, ZR 05-19 and the abstract of the MPC 2009 paper. Seven are co-authored texts. Seven are spoken or slide sources where he is the speaker: one interview, five Gurobi webinars and the SEA 2022 slides. One is a 2025 blog comment posted under his name. The other 12 are secondary, observed or metadata sources. WebSearch: 3 of the 5 allowed calls. Everything else came from curl, the ZIB OPUS file server, Crossref, DataCite, the Springer and INFORMS pages, the Substack API and yt-dlp, which fetched YouTube's automatic captions. |
| Local corpus | `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep` placeholders, plus the template `RESOURCES.md`. There was no user-supplied material. `private/` was not opened. |
| Saved this run | No transcript was written into `../sources/talks/`. The captions belong to copyrighted videos, so this note gives timestamped paraphrases instead. The raw caption files (`.vtt`) and timestamped conversions (`subject_to_ts.txt`, `web_<videoId>.txt`) stay in the scratch folder `C:\Users\sr881\AppData\Local\Temp\milp-team-t1-scratch\base-skills\tobias-achterberg\02\` (`subs\` and the folder itself) for later agents. Another agent of this run saved an excerpt of the same interview caption track at `../sources/talks/subject-to-2023-interview.excerpt.transcript.txt`. This note neither wrote nor relied on that file; its timestamps come from this agent's own caption download. |
| Quotation policy | The file contains exactly one verbatim quotation, R1, under 15 words and in quotation marks. Every other claim text is a faithful paraphrase, marked **≈**, with a page or timestamp locator. No paraphrase is put in quotation marks. Technical labels (for example *consistent win*) are in italics. |

## Reading guide

**Tags**

| Tag | Meaning |
|---|---|
| [stated] | He said or wrote it, in a text or talk of his alone. |
| [stated, co-authored] | A co-authored text: the authors' joint position, not attributable to him alone. |
| [stated, team] | He describes what *we* at Gurobi do, so it is team practice in his words. Agent 03 should check it against artefacts. |
| [stated, self-report] | His account of something he did, such as a test he ran, code he wrote or a failure. Agent 03 should check it. |
| [observed] | Someone else's statement about him (prize committees, colleagues, a blogger). |
| [inferred] | My reading, not his. |

P = primary (his own text or talk, co-authored included). S = secondary.

**Spoken-source warnings**

- The interview (P12) and the webinars (P13–P17) were read only as YouTube *automatic* captions. They were not speaker-checked, and names are garbled. In the captions `skip` is SCIP, `C Plex`/`suplex` is CPLEX, `grobi`/`kurobi`/`goobi` is Gurobi, `presoft`/`pre-salt` is presolve, `Gomery` is Gomory, `zip` is Alexander Martin's SIP, `Susan`/`Tuesday Institute` is ZIB, `Martin gotcha`/`Godzilla`/`Garage` is Martin Grötschel and `tors` is Thorsten Koch.
- Webinar speakers were identified from the description and on-screen hand-overs:
  - 9.0: sole presenter named in the description.
  - 9.1: the host addresses Toby after the MIQCP segment and in the Q&A.
  - 9.5: the engine speaker hands over to Michel Jaczynski.
  - 10.0: introduced by name.
  - 13.0: Xavier hands over to Tobias.
- The 11.0 webinar (Dec 2023) had no identifiable speaker in the captions or description and is **not used**.
- Webinars are product marketing as well as method talks: they show what he chooses to report and how he measures it, not neutral science.

**Era key (resource context)**

| Period | Position | Code and tools | Compute and test sets he reports |
|---|---|---|---|
| 1999–2004 | Student, master's theses and early ZIB research | Alexander Martin's SIP with CPLEX as the LP solver (P12 24:05; P3 p. 8) | The 2004 branching report ran on an Alpha 21264 workstation at 833 MHz. Test set: MIPLIB 2003 plus Mittelmann instances, filtered to those where CPLEX 9.0 needs at least 5,000 nodes and at most 1 h (P3 p. 8). |
| 2002–2007 | PhD researcher at ZIB, sole author of SCIP | SCIP 0.90 (about 223k lines of C plus 58k lines for the chip solver), CPLEX 10 as the LP solver (P1 pp. 6, 319) | Eight identical Pentium 4 PCs, partly colleagues' spare cycles. 244 instances out of 575 collected, 115 settings, 28,060 runs, more than one CPU-year, 1 h limit (P1 pp. x, 2, 319–320). Diploma students Wolter and Berthold built the cuts and heuristics (P1 pp. 3–4, x). |
| 2006–2014 | ILOG/IBM CPLEX developer, later lead MIP developer (S3) | CPLEX source | Not stated by him in the sources read. A colleague's January 2014 IBM deck reports CPLEX-team runs on 1,769–3,243 models with 5 seeds (S4, observed). |
| 2014– | Gurobi senior developer, then Director of Development (2019), then VP R&D (2020–) | Gurobi source, git and GitHub (P12 48:22) | 3,182 models on a 4-core i7 with a 1 h limit (P9, 2016). More than 5,000 MILP models (P15, 2021). 7,030 MIP models, 4 cores, 10,000 s (P18, July 2022). About 6,000 models and a 192-machine cluster running 24/7 (P12, 2023). About 8,500 models (P19, June 2025). Five random seeds per comparison (P14, P12, P17). |

---

## 1 Research taste (what is worth doing; what is a good or bad result)

- **T-1 Black-box usability is what makes a MIP solver valuable.**
  - ≈ The commercial success of MIP solvers comes from being a black box that people with no knowledge of algorithms can use: they model the business problem and get a solution. A branch-cut-and-price solver could therefore only be a framework, and only a tiny fraction of users write callbacks beyond logging or termination.
  - Source: P12 1:02:34–1:04:26, 2023. [stated] P.
  - Contrast: his 2004 and 2006 position, see C5.
- **T-2 Performance is the product.**
  - ≈ As always, the team works very hard on performance, because that is the main feature users need to see improve (P13 0:00:03–0:00:33, Dec 2019). [stated, team] P.
  - ≈ His own main contribution at Gurobi is still MIP performance across branching, cuts, presolve, the tree framework and parallelisation (P12 46:46, 2023). [stated, self-report] P.
- **T-3 Clean data-structure design is a pleasure in itself.**
  - ≈ He loves data structures and their clean design. Building the non-convex MIQCP machinery so that it plugged in and worked was very rewarding (P12 47:18–47:50, 2023).
  - ≈ Switching off inactive cuts during diving was a satisfying data-structure and implementation exercise (P16 0:11:42, Nov 2022).
  - [stated] P.
- **T-4 Robustness across formulations matters, not only best-case speed.**
  - ≈ Because minor formulation changes can swing solve time by more than a factor of 1,000, strategies that are independent of the formulation are worth finding. Branching is one candidate: SCIP's branching was slower in the best case but much less formulation-dependent.
  - Source: P8 pp. 1, 6, 10, 2008. [stated, co-authored] P.
- **T-5 Mathematical correctness beats a convenient answer.**
  - ≈ Fixing all integers and reading duals and reduced costs of the fixed LP as MIP sensitivity information is a wrong approach that makes no mathematical sense. That is why Gurobi built a proper MIP scenario analysis instead.
  - Source: P13 0:38:59–0:39:29, 2019. [stated] P.
- **T-6 Theory's worst case says little about practice, but code must still be safe for the worst case.**
  - ≈ On a 7,030-model MIP set there is no obvious relation between model size (non-zeros or integer variables) and solve time, and exponential worst-case bounds are far above observed times.
  - ≈ Polynomial is not automatically fast enough: even quadratic algorithms are too slow on big models, so one must always think about big models.
  - ≈ Exponential subproblems can still be useful, because a heuristic that often finds good solutions is usually good enough.
  - ≈ Design for practical instances, but always include safeguards against worst-case behaviour.
  - Source: P18 slides 5–19 and the two slides on consequences for MIP solvers, July 2022. [stated] P.
- **T-7 Things he calls worthless or bad.**
  - Most-infeasible (most-fractional) branching. See B1 (2004, 2007, 2023).
  - Unfair comparisons. See B9.
  - Reviewers who judge a technique only by whether it beats Gurobi (P12 51:29).
  - Uninterpretable ML models inside the solver. See B11.
- **T-8 Small wins are accepted as real progress.**
  - ≈ A new cut family that affects only 10% of models, with a 2.5% gain on them, is modest but still one more trick in the bag (P17 0:04:39, Dec 2025). [stated] P.
  - ≈ The other side of the ledger: a year of work on a new NLP heuristic for a 19% overall gain is, in his judgement, not very impressive (P15 0:15:53, Dec 2021). [stated, self-report] P.
- **T-9 [observed] What prize committees saw as his taste.**
  - ≈ The 2009 Beale–Orchard-Hays citation stresses techniques integrated after extensive computational experimentation, in a code base of over 250,000 lines that the author wrote alone.
  - ≈ The 2009 Tucker finalist text praises practical experiments and implementing all variants with high program quality and close attention to detail.
  - Source: S1, Optima 80, Sept 2009.
  - ≈ The 2011 INFORMS Optimization Society Young Researchers Prize citation calls the SCIP paper exemplary software documentation that conveys both the big picture and the details and documents extensive testing against other packages.
  - Source: S2.

## 2 Problem choice (where problems come from, timing, when to stop)

- **C-1 Pick a topic that joins your fields, then integrate two communities' views.**
  - ≈ Having studied both mathematics and computer science, he looked for a topic combining them. In 2002 the integration of IP and CP struck him as the perfect candidate (P1 p. ix, 2007). [stated, self-report] P.
  - ≈ He saw CP as the same thing as MIP viewed from a different angle, so why not combine them. He later learned John Hooker had the same idea (P12 26:39–27:09, 2023). [stated] P.
- **C-2 An application that fits the method, at the right moment.**
  - ≈ Grötschel's industry contact produced an ideally timed project: chip-design verification, a natural fit for CIP (P1 p. ix).
  - ≈ The SAT-based tools of the industrial partner struggled with arithmetic units (addition, multiplication), which is where CP plus MIP could help (P12 28:40–30:15).
  - ≈ Having the industrial contact made his project different: lots of test data, received early enough to be useful within the project (P1 p. ix).
  - [stated, self-report] P (2007, 2023).
- **C-3 Reproduction attempts are a source of problems.**
  - ≈ The minor-changes study began when the authors tried to reproduce a published TSP formulation and saw erratic solver behaviour. The formulation is from M. van Vyve and L. A. Wolsey, *Approximate extended formulations*, Math. Program. 105:501–522, DOI 10.1007/s10107-005-0663-7 (Crossref-checked; P8 gives pp. 501–511).
  - Source: P8 p. 1, 2008. [stated, co-authored] P.
- **C-4 Important but under-published engineering topics deserve a paper.**
  - ≈ Few papers exist on presolve despite its importance. Earlier feature studies found presolve and cutting planes to be by far the most important tools. So the paper documents all Gurobi 6.5 presolve steps with computations. The studies are:
    - Bixby et al., *Mixed-Integer Programming: A Progress Report* (2004), DOI 10.1137/1.9780898718805.ch18;
    - Bixby and Rothberg, *Progress in computational mixed integer programming—A look back from the other side of the tipping point* (2007), DOI 10.1007/s10479-006-0091-y;
    - Achterberg–Wunderling 2013 (P10).
  - Source: P9 p. 2, 2016. [stated, co-authored] P.
- **C-5 Users and customers set the agenda (commercial era).** See B12.
  - ≈ Many new features were requested by users (P15 0:16:55, 2021).
  - ≈ Customers repeatedly asked for the NoRel heuristic for models whose root LP alone exceeds the time limit (P12 58:42–59:44, 2023).
  - ≈ A few customers have models with many disconnected components, so that code was rewritten (P17 0:05:43, 2025).
  - [stated, team] P.
- **C-6 Benchmark libraries should stay concise and challenging.**
  - ≈ MIPLIB's purpose is a concise set of challenging problems. Instances that became too easy are purged. Real-world instances are solicited. Over-represented problem types are a concern. Yearly updates were planned.
  - Source: P6 pp. 1–2, 2005. [stated, co-authored] P.
  - [observed/inferred] The yearly updates did not happen: the next MIPLIB was MIPLIB 2010, published 2011 (DOI 10.1007/s12532-011-0025-9; metadata only).
- **C-7 What he decided *not* to pursue, or has not pursued, and why.** All from P12, 2023. [stated] P.
  - A general commercial branch-cut-and-price solver: the audience is too small (1:02:34–1:04:57). Application-specific solvers such as vehicle routing could work.
  - GPUs for the simplex core: the arithmetic is sparse, sequential and dependent, and Gurobi has not found a good way to use GPUs for it (1:10:58–1:12:43).
  - CP-style scheduling inside Gurobi: a possible benefit, but not yet tried (1:13:45–1:14:16).
  - Automatic Dantzig–Wolfe decomposition in default settings: GCG gives mixed results, excellent on some classes and useless on others. He does not yet know how to put it into defaults, so users supply the partition instead (1:00:45–1:02:20).

## 3 Idea generation (where ideas come from)

- **I-1 Transfer techniques from SAT and CP into MIP, and adapt them after testing.** Repeated in 2005, 2007 and 2023.
  - ≈ In a subway ride, Yakov Novikov explained SAT conflict analysis and two-watched-literals propagation. Within days he put watched literals into the set-covering handler, and within three weeks he had generalised conflict analysis to MIP (P1 p. x; retold in P12 30:45–32:18).
  - ≈ The 2005 report frames conflict analysis as remedying MIP solvers' habit of discarding infeasible subproblems (P5 abstract).
  - ≈ Inference branching was influenced by SAT/CP ideas for feasibility problems (P1 p. 2).
  - ≈ SAT solvers restart periodically, but tests showed that for MIP it is better to restart only right after the root (P1 p. 4).
  - ≈ Future work should borrow SAT clause-database management (P5, closing section).
  - [stated, self-report] P.
- **I-2 Use ML to find the one feature that matters, then discard the ML.**
  - ≈ His CS master's thesis (around 2000–2001, at ZIB on SIP) tried to learn branching with SVMs, neural networks, RBF networks and other learners. The disappointing result was that one hand-made feature, the *history value* (pseudocosts and a bit more), was all that mattered.
  - R-2 (≈) His summary: ignore the machine-learning part, here is the good feature. That became history branching (P2, 2002) and then reliability branching (P3, 2004).
  - Source: P12 23:35–25:39, 2023. [stated, self-report] P. See B11.
- **I-3 Generalise existing rules into one parameterised family.**
  - ≈ Reliability branching is presented as a generalisation containing strong, pseudocost and hybrid rules as parameter settings (P3 abstract and pp. 1–2, 2004; P1 p. 2).
  - [stated, co-authored] and [stated] P.
- **I-4 Gut feel, then try it; if it fails, try the opposite.**
  - ≈ Defaults come from huge amounts of tuning on the cluster. One has a gut feel, tries it, sees it fail, tries the opposite, and sometimes the opposite works without anyone knowing why. One then measures. This is more an engineering task than science.
  - ≈ Ideas such as using one setting for very big problems, or giving probing more weight on pure binary problems, become rules in the automatic settings.
  - Source: P12 1:04:57–1:06:00, 2023. [stated, team] P.
- **I-5 Take ideas from the literature and from colleagues, implement and measure them.**
  - ≈ PSD cuts were not their own invention but standard literature that they implemented (P14 1:08:53, Dec 2020).
  - ≈ He implemented Mark Turner's Gomory-cut-violation branching criterion in Gurobi, saw it help a little, and it became a tie-breaker that avoids falling back to most-fractional (P12 55:06–56:38, 2023).
  - ≈ His neural-network structure detection for OBBT was inspired by a paper of Matteo Fischetti and a co-author on adversarial examples for a digit-recognition network (P12 1:00:14–1:01:17). [inferred] He names no title. The description fits M. Fischetti and J. Jo, *Deep neural networks and mixed integer linear optimization*, Constraints 23:296–309 (2018), DOI 10.1007/s10601-018-9285-6 (Crossref-checked); the identification is not confirmed.
  - [stated, self-report] P. Contrast C6.
- **I-6 Build it yourself, from scratch.**
  - ≈ He is mainly interested in solving problems: having an idea and thinking it through. He is not good at knowing what is out there or at extending other people's work. He always wants to do it himself from scratch, which risks reinventing the wheel but can yield things others would not have considered.
  - Source: P12 1:20:24–1:21:28, 2023. [stated] P. See B13 and C6.
- **I-7 Look at real data before believing theory.**
  - ≈ The SEA 2022 talk compares theoretical worst-case bounds against runtimes on 2,397 LP and 7,030 MIP real-world instances.
  - Source: P18 slides 5–19, 2022. [stated] P.

## 4 Experiments and execution (how to test, baselines, ablations, iteration)

- **E-1 Measure a component by switching it off against the default.** This is B3.
  - ≈ Performance is measured as the geometric mean relative to SCIP's default settings. A 100% improvement for a default feature means the solve takes twice as long, in the geometric mean, when the feature is disabled (P1 p. 2 fn. 1, 2007).
  - ≈ Every chapter of Part II ends with such experiments (P1 pp. 2, 60).
  - ≈ For cuts he follows the three-way design of Bixby, Fenelon, Gu, Rothberg and Wunderling, *MIP: Theory and Practice — Closing the Gap* (2000), DOI 10.1007/978-0-387-35514-6_2 (P1 p. 111):
    1. all cuts off;
    2. one separator off at a time;
    3. one separator on alone.
  - [stated] P.
- **E-2 Isolate the component under study.**
  - ≈ The branching study used cut-and-branch, cuts at the root only, to emphasise branching. It deliberately did not pre-set optimal objective values, because finding good solutions early is a desirable property of a branching rule (P3 p. 8, 2004).
  - ≈ The CPLEX comparison run used SIP's preprocessing and cuts inside CPLEX, so both ran pure branch-and-bound on the same problems (P3 p. 8).
  - ≈ The presolve study disabled reductions in the master solve only, by editing source code, and kept them on in sub-MIPs to avoid implicitly changing heuristic behaviour (P9 p. 3, 2016).
  - [stated, co-authored] P.
- **E-3 Validate that the testbed is near the state of the art.**
  - ≈ The authors ran CPLEX 9.0 to verify that the SIP environment was state of the art (P3 p. 8, 2004).
  - ≈ SCIP with CPLEX as LP solver is not quite competitive with CPLEX, but not far from it (P5 p. 15, 2005).
  - ≈ SCIP 0.90i is on average 63% slower than CPLEX 10, and much slower with SoPlex (P1 pp. 6, 377, 2007).
  - Repeated 2004–2007. [stated] and [stated, co-authored] P.
- **E-4 Test-set construction is explicit and rule-based.**
  - ≈ The thesis rules (P1 p. 320, 2007):
    - drop instances neither solver solves in 1 h;
    - remove duplicates between sets;
    - drop instances both solvers solve in under 10 s;
    - in one set, sort by CPLEX time and drop every second instance;
    - drop numerically too-hard register widths.
  - ≈ Single-class test sets count as three pseudo-instances each, so they do not dominate the total (P1 p. 322).
  - ≈ In 2016: 3,182 public and commercial models solvable within 10,000 s by some Gurobi release (P9 p. 3).
- **E-5 Machine and timing discipline.**
  - ≈ He used identical machines, ran only on unloaded machines and reran suspicious benchmarks (P1 p. 319). [stated, self-report]
  - ≈ A model that hits the time limit is scored at the limit, which advantages time-outs but limits the influence of a single failure; he states both effects (P1 p. 319).
  - ≈ Memory-limit hits are treated as time-outs, with node counts scaled (P1 p. 319).
  - ≈ Historic speedups are computed on the same hardware, so they reflect software alone (P17 0:02:34, 2025).
  - ≈ Gurobi added deterministic *work units*, calibrated to one second on the team's test hardware, for reproducible limits (P15 0:25:35–0:28:41, 2021).
- **E-6 Use random seeds and a consistent-win rule.** This is B7.
  - ≈ Every change is run, old against new, with five random seeds. A model counts as a *consistent win* if the new version is at least 10% faster on at least four of the five seeds, and a consistent loss if it is almost always slower (P14 1:11:31–1:12:32, Dec 2020).
  - ≈ About 6,000 models with five seeds take roughly 12 hours on a free cluster (P12 1:05:30, 2023).
  - ≈ A 2025 heuristic study: about 4,600 hard models, five seeds, 60 s runs, about 23,000 tests. A win means a solution at least 1% better; consistent means four or five seeds (P17 0:11:49–0:12:51).
  - [stated, team] P.
- **E-7 Scale of experiments as a resource argument.**
  - ≈ In 2007: more than one CPU-year, 244 instances, 115 settings, 28,060 runs. He calls it, by his own estimate, among the most extensive computational studies on the topic (P1 p. 2).
  - ≈ In 2023: 192 machines testing 24/7, an advantage academics cannot copy (P12 52:01).
- **E-8 Tuning on sets, not instances.**
  - ≈ The tuning tool is a global search over parameter space that parallelises almost linearly. But one must tune on a *set* of instances, otherwise one over-tunes to random luck (P12 1:06:27–1:07:30, 2023).
  - ≈ The tuning tool is described the same way, over a set of models (P15 0:43:42–0:44:14, 2021).
  - [stated] P.
- **E-9 Fix the model before tuning.** This is B14.
  - ≈ Before parameter tuning, improve the model, especially numerics. Numerical trouble yields strange answers and also degrades performance. The art is a model faithful enough to reality yet simple and numerically stable.
  - Source: P12 1:07:30–1:08:30, 2023. [stated] P.
- **E-10 Interpretable ML for default rules.** This is B11.
  - ≈ Use decision trees, not SVMs, because he wanted to understand what was going on. One example is the rules for whether to dualise an LP and whether to use primal or dual simplex (P14 Q&A 0:59:59–1:00:31, Dec 2020; P12 1:16:16–1:17:18, 2023).
  - ≈ The learned rule is then reimplemented from scratch (P12 1:16:16).
  - [stated] P.
- **E-11 Algorithm engineering rules for solver internals.** P18, 2022. [stated] P.
  - ≈ Design for typical sparsity (2–30 non-zeros per row, 2–10 per column) but avoid blow-ups at 1,000 or more.
  - ≈ Implement in portable C on the solver's own data structures.
  - ≈ Tune to the structures of practical models.
  - ≈ Check work limits regularly.
  - ≈ Use a non-recursive Tarjan because recursion can overflow the stack.
  - ≈ Hidden quadratic loops are among the most frequent performance bugs the team has to fix.
  - ≈ Conclusion of the deck: they must implement all such algorithms themselves, which he presents as enjoyable.
- **E-12 Effort control for expensive components.**
  - ≈ Probing in the chip-verification solver might better be disabled. A better strategy is needed to control probing effort (P1 p. 312).
  - ≈ Conflict analysis pays off only when the analysis effort is kept moderate, and the policy for discarding useless conflicts is a key factor (P1 p. 181, 2007).
  - [stated] P.

## 5 Judging results (when to believe a result; negative results)

- **J-1 Averages over test sets, not single instances.** This is B8.
  - ≈ The authors do not base conclusions on single instances but on averages, and they regard the geometric mean as a generally accepted fair criterion (P3 p. 9, 2004).
  - ≈ How averages are defined matters. The geometric mean can be dominated by small absolute changes on easy instances, and the arithmetic mean ignores easy instances. He therefore reports the *shifted* geometric mean, with shift 10 s for time and 100 for nodes, as a compromise. A worked example shows the three means giving opposite verdicts on the same data (P1 pp. 321–322, 2007).
  - See C1 and C2.
- **J-2 Exclude trivial models and report solve-time brackets.** This is B6.
  - ≈ Use brackets of at least n seconds, in which the *slower* of two versions needs at least n seconds. Usually report the 10 s bracket because it excludes uninteresting easy models but stays large. Count models at least 10% faster and at least 10% slower. Report the models a change actually affects (P9 pp. 3–4, 2016, co-authored, crediting the form to Achterberg–Wunderling 2013).
  - The same brackets appear in webinars: at least 1 s for non-trivial and at least 100 s for hard models (P13 0:02:35; P14 1:26:02; P16 0:02:02; P17 0:01:04; 2019–2025).
  - [observed] A January 2014 IBM CPLEX deck explains the Achterberg–Wunderling *unbiased* scheme as keeping a model only if at least one run took at least 10 s. It measures feature impact by on/off runs, geometric-mean degradation, solved counts and affected models (S4, slides 7–8).
- **J-3 Local indicators do not prove a speedup; total time decides.** This is B4.
  - ≈ Full strong branching gives the smallest trees, but the node savings do not justify its cost (P1 pp. 69–70). The 2004 paper already notes strong branching does well on nodes but, as expected, not on time (P3 pp. 10–11).
  - ≈ Conflict analysis in 2005 cut nodes by about 50% but raised time by about 15% on feasible MIPs. The report says so in its abstract and gives per-instance counts: 21 instances with fewer nodes, 12 faster, and 16 faster with the default (P5 abstract and p. 15).
  - ≈ Disabling single cut separators increases nodes without always increasing time (P1 p. 113).
  - ≈ New cuts can tighten the dual bound and still lose overall; he treats this as normal for cutting planes (P14 1:19:14, 2020).
  - ≈ With a new cut everything can look great — it cuts off the LP point and tightens the bound — and performance still suffers, whereas presolve ideas usually do pay off (P12 41:08–41:38, 2023).
- **J-4 Size of the evidence base.**
  - ≈ Results from a few hundred non-convex models (400–500) should be taken with caution compared with a MILP set ten times larger (P15 0:12:16, 2021). [stated, team]
  - ≈ In 2007 he gives differences up to 2% in mean runtime as timing noise (P1 p. 319). [stated] See C3.
- **J-5 Fairness and the right baseline.** This is B9.
  - ≈ Use the same gap tolerances when comparing with CPLEX (P3 p. 8; P5 p. 15 fn. 4; P1 pp. 320, 377).
  - ≈ The SCIP–CPLEX comparison measures only the MIP part, because SCIP used CPLEX for LPs (P1 p. 377).
  - ≈ Comparing a non-convex-MIQCP-only solver with general MINLP solvers is a little unfair (P13 0:22:59, 2019).
  - ≈ CP-versus-MIP comparisons are only fair if both models are written by experts. Direct translations of one model into the other paradigm make the comparison meaningless (P12 1:14:46–1:15:46, 2023).
  - ≈ An academic technique should be shown to improve the framework it was built in, for example SCIP. Reviewers who demand that it beat Gurobi or Xpress miss the point (P12 51:29, 2023). See C7.
- **J-6 Numerics can make two answers both correct.**
  - ≈ Non-convex MIQCP results are preliminary because two solvers can report different optimal values (P13 0:21:55, 2019).
  - ≈ The 2016 study excludes models where the two versions disagree on the optimal value (P9 p. 3).
  - ≈ The feasibility tolerance (1e-6 absolute) is a grey zone, not a relaxed right-hand side. *Feasible* and *infeasible* can both be correct answers for the same model, and so can very different optimal values (P12 1:09:03–1:10:35, 2023).
- **J-7 One formulation's intractability is not the model's.**
  - ≈ Intractability of one formulation with one solver does not show the model is intractable, since slight modifications can change solvability dramatically (P8 p. 10, 2008). [stated, co-authored]
- **J-8 Pick the metric by the user's goal.**
  - ≈ Primal heuristics barely reduce time to optimality (disabling them costs 14%). Since users often want good feasible solutions fast, he ran a second experiment that stops at a target gap (P1 pp. 4, 129, 2007).
  - ≈ In the 2025 heuristic test, the metric is a better incumbent within 60 s (P17 0:11:49).
- **J-9 Label unsupported claims; be careful with novelty.**
  - ≈ He labels one experience-based claim as lacking detailed computational support (P1 p. 140).
  - ≈ He claims a product branching score is new only to the best of his knowledge (P1 p. 71).
  - [stated] P.
- **J-10 Historic comparisons depend on the measure.**
  - ≈ Long-horizon speedups depend heavily on the time limit and on how time-outs are scored, so the team uses one penalised measure it considers fair. The captions render its name as *part-time* (2021) and *part 10* (2022); probably PAR10, **not confirmed**.
  - Source: P15 0:03:02–0:04:04; P16 0:24:01.
- **J-11 Failures and negative results he reported himself.** [stated, self-report] P.
  - ML branching (around 2000–2001): disappointing as ML, salvaged as one feature (P12 25:07).
  - Conflict analysis (2005): slower on feasible MIPs at first (P5). In 2007 he reports more than 10% gain once implementation details and the discard policy were handled (P1 pp. 5, 181). See C9.
  - Delayed restarts during the tree (2007): inferior to default. Log inspection showed global fixings are rare and come too late, so new criteria would be needed (P1 p. 163).
  - Aggregating pairs of linear constraints: slight overall deterioration (P1 p. 161).
  - Implicit-integer declaration (2008): expected to help, did not, so SCIP's implementation could not yet exploit it (P8 p. 7).
  - Probing in chip verification: may be better off (P1 p. 312).
  - NLP heuristic (2021): 19% for almost a year of work (P15 0:15:53).
  - MIPLIB 2003's planned yearly updates (C-6): did not happen [observed].

## 6 Writing and talks

- **W-1 Writing up beats another 10%.**
  - ≈ After 250,000 lines of code he expected the thesis to be easy and was wrong. He overran his self-imposed deadline, and Thorsten Koch had to convince him that writing things down mattered more than another 10% of SCIP performance. He is grateful for that advice.
  - Source: P1 p. x, 2007. [stated, self-report] P.
- **W-2 Computational work is hard to publish and under-appreciated.**
  - ≈ Writing papers about practical computational work is tough: one does not prove theorems, one builds something and shows it works.
  - ≈ The community does not value computational work as much as it should, relative to the effort.
  - ≈ Much of solver progress, such as constant tweaks and software engineering, cannot be written up at all.
  - Source: P12 50:27–53:35, 2023. [stated] P.
- **W-3 Literature reviews are his weak point.**
  - ≈ Writing the introduction and literature overview, and being fair to other researchers, is the hardest part of a paper for him. Early in SCIP he missed John Hooker's closely related work and only learned of it at a conference, which cost a possible collaboration.
  - Source: P12 1:21:28–1:22:29, 2023. [stated] P.
- **W-4 State the model precisely so results can be reproduced.**
  - ≈ When reporting computations, state the exact model formulation, or reproducibility is hard to achieve.
  - Source: P8 p. 7, 2008. [stated, co-authored] P.
- **W-5 Standard reporting form.**
  - ≈ Summary tables of percentage changes in shifted geometric means, with detailed per-instance tables in an appendix (P1 pp. 2, 321–322).
  - ≈ In 2016 the bracket table form credited to Achterberg–Wunderling (P9 p. 3).
  - ≈ In webinars, the same summary table each release: all non-trivial models (at least 1 s) and hard models (at least 100 s), per problem class (P17 0:00:34–0:01:04).
- **W-6 Commercial papers leave gaps and say so.**
  - ≈ The presolve paper admits unanswered questions, especially implementation details, and hopes the ideas motivate further research.
  - Source: P9 p. 65, 2016. [stated, co-authored] P.
- **W-7 Talks show performance against the incumbent.**
  - ≈ His 2005 MIP-workshop talk on conflict analysis included his usual SCIP-versus-CPLEX performance comparison, and that talk led to the ILOG offer.
  - Source: P12 35:26–37:00, 2023. [stated, self-report] P.
- **W-8 [observed] How others read his writing.**
  - ≈ The 2011 committee singles out documentation of both overview and detail, plus documented testing (S2).
  - ≈ Prize texts stress extensive experimentation and code quality (S1).

## 7 Research organisation (time, tools, collaboration, students, long-term agenda)

- **O-1 Research needs the source code of a state-of-the-art solver.** This is B2.
  - **R1 (the one verbatim quotation):** branching research is "only possible if you have the source code of a state-of-the-art MIP solver" (P1 p. ix, 2007; fragment of a longer sentence). [stated] P.
  - ≈ Martin's SIP spared him from reinventing the wheel (P1 p. ix).
  - ≈ Proprietary commercial codes make it hard for academics to test ideas in a state-of-the-art environment. SCIP is an attempt to give the community a free, nearly competitive code (P1 p. 59).
  - ≈ He hopes source availability will foster research (P1 p. 6).
  - ≈ Black-box software does not teach scientific method. Students should be able to look inside and extend the tools (P7 p. 2, 2006, co-authored).
  - ≈ Retold: SIP's code made his master's study possible (P12 24:05, 2023).
- **O-2 Build the infrastructure first, with protected time.**
  - ≈ For almost two years he published nothing and coded all day to build a basis on which the real research could then be done. This was thanks to Grötschel's patience and freedom (P1 p. ix).
  - ≈ He could code for several years almost without interruption (P12 28:09–28:40).
  - [stated, self-report] P (2007, 2023).
- **O-3 Research is about 10% of solver development.**
  - ≈ Research is maybe 10% of the time. About 90% is software design, architecture, bug fixing, benchmarking and tweaking until it works, which academics lack the time and team for (P12 52:32–53:35, 2023). [stated, team]
  - ≈ He introduced git and later a GitHub-based issue workflow at Gurobi (P12 48:22). [stated, self-report]
- **O-4 Hire people who have built their own solver.**
  - ≈ At CPLEX he implemented everything he knew worked from SCIP and had one success after another. Someone who wrote their own solver arrives with an arsenal of proven ideas; later gains get harder (P12 40:04–41:08, 2023). [stated, self-report] P.
- **O-5 Collaborators complement his blind spots.**
  - ≈ He needs collaborators who know the literature better (P12 1:20:57). [stated] P.
  - ≈ He delegated components to diploma students and cites their theses for details: cuts to Kati Wolter, heuristics to Timo Berthold. He praises them as his students and credits SCIP's progress partly to them (P1 pp. 3–4, x). [stated] P.
  - Supervision itself is agent 04's topic.
- **O-6 Compute as a shared resource.**
  - ≈ He borrowed colleagues' spare CPU cycles on machines identical to his (P1 p. x, 2007).
  - ≈ Gurobi now runs a 192-machine cluster at full load around the clock (P12 52:01, 2023).
- **O-7 Licensing rationale.**
  - ≈ He considered SCIP's academic-only licence reasonable and fair: state-funded code should not undercut commercial vendors. Its later move to a full open-source licence is the new maintainers' decision.
  - Source: P12 33:21–34:52, 2023. [stated] P.
- **O-8 Advice on the PhD itself.**
  - ≈ Finishing a thesis while already working full-time in industry is not something he would recommend.
  - Source: P12 39:34, 2023. [stated] P. This is the only explicit PhD advice found.
- **O-9 Teaching.**
  - ≈ Teach real-world problem solving as an iterated cycle: model, solver run, solution analysis. Use real-size instances, because modelling pitfalls and running-time anomalies do not show up on toy models.
  - Source: P7 pp. 1–2, 2006. [stated, co-authored] P.
- **O-10 Long-term direction.**
  - ≈ Generative AI may lower the modelling barrier, which today needs about a master's or PhD. Whether it delivers remains to be seen (P12 1:17:42–1:19:54).
  - ≈ If he ever left solver development, he could imagine applying his knowledge of solver internals to applications (P12 1:22:30–1:23:30).
  - [stated] P (2023).

---

## Real beliefs (claims repeated at least 3 times)

| # | Belief (≈ paraphrase) | Repetitions (source, date) | Count |
|---|---|---|---|
| B1 | Most-infeasible branching is no better than random; there is no reason to use it | P3 pp. 4, 9 (2004); P1 pp. 3, 69 (2007); P12 56:07–56:38 (2023) | 5 statements, 3 sources, 2004–2023 |
| B2 | Solver research needs (open) source code of a state-of-the-art solver | P7 p. 2 (2006, co-authored); P1 pp. ix, 6, 59 (2007); P12 24:05 (2023) | 5 statements, 3 sources |
| B3 | Measure a component by turning it off against the default; report geometric-mean (later shifted) ratios | P1 p. 2 and Part II (2007); P10 abstract (2013); P9 §1.1 (2016); P14 ~1:20:16 (2020) | 4 sources, 2007–2020 |
| B4 | Fewer nodes, a better bound or a violated cut do not prove a speedup; total time decides | P3 pp. 10–11 (2004); P5 abstract (2005); P1 pp. 69–70, 113 (2007); P14 1:19:14 (2020); P12 41:08 (2023) | 5 sources, 2004–2023 |
| B5 | MIP progress is many small improvements that add up, a bag of tricks | P1 p. 2 (2007); P13 0:02:35 (2019); P14 1:06:18 (2020); P15 0:04:04 (2021); P16 0:11:12 (2022); P12 52:01 (2023); P17 0:03:06 (2025) | 7 sources, 2007–2025 |
| B6 | Exclude trivially easy models; report brackets by the slower run's time | P1 p. 320 (2007); P9 p. 3 (2016); webinars 2019, 2020, 2022, 2025; S4 for 2013 | 6+ sources |
| B7 | Judge changes across five random seeds; *consistent win* = at least 10% on at least 4 of 5 | P14 (2020); P12 1:05:30 (2023); P17 (2025) | 3 sources [stated, team] |
| B8 | Conclude from sets, not single instances; tune on sets or you over-tune | P3 p. 9 (2004); P1 pp. 321–322 (2007); P15 0:12:16 (2021); P12 1:07:30 (2023) | 4 sources |
| B9 | Fair comparisons: equal tolerances, isolated components, expert models on both sides, the right baseline | P3 p. 8 (2004); P5 p. 15 (2005); P1 p. 377 (2007); P13 0:22:59 (2019); P12 51:29, 1:15:16 (2023) | 6 statements, 5 sources |
| B10 | Presolve is the most dependable source of speedups | P1 p. 4 (2007); P9 pp. 2, 65 (2016, co-authored); P16 0:12:12 (2022); P12 41:08 (2023) | 4 sources |
| B11 | ML is for discovering interpretable rules that are then hand-implemented, not a black box in the solver | P12 25:07–25:39 and 1:16:16 (2023); P14 Q&A 0:59:59 (2020) | 3 statements, 2 sources |
| B12 | Users' and customers' problems steer the work | P1 p. ix (2007); P13 0:00:33 (2019); P15 0:16:55 (2021); P12 58:42 (2023); P17 0:05:43 (2025) | 5 sources |
| B13 | Do it yourself, from scratch | P1 p. ix (SCIP from scratch, 2007); P18 slide on implementation considerations (2022); P12 1:20:57 (2023) | 3 sources (but see C6) |
| B14 | Model quality and numerics come before solver settings | P8 (2008); P13 0:21:55 (2019); P12 1:07:30–1:10:35 (2023) | 3 sources |
| B15 | Design for practical instances, but guard against worst cases and control effort | P1 pp. 181, 312 (2007); P15 work limits (2021); P18 (2022, three separate bullets) | 3 sources |

Single or double mentions are not beliefs by the count rule but are recorded in the layers above. Examples: model-first advice to users; the 10/90 research/engineering split; hiring solver builders; avoiding a thesis while employed.

## Contradictions

Kept as found, not reconciled.

- **C1 — The mean (2004 vs 2007).**
  - 2004 (co-authored): the geometric mean is treated as a generally accepted fair criterion (P3 p. 9).
  - 2007 (solo): the plain geometric mean can be dominated by small absolute variations on easy instances; the shifted geometric mean is used instead (P1 pp. 321–322).
- **C2 — The shift values.**
  - The thesis sets the shift to 10 s for time and 100 for nodes (P1 p. 321, 2007).
  - The 2016 presolve paper uses a shift of 1 s and 1 node and cites the thesis for the method (P9 p. 4).
- **C3 — Variability (2007 vs 2020–2025).**
  - 2007: up to 2% difference in mean runtime is attributed to timing noise. Single runs, no seeds (P1 p. 319; the thesis has no random-seed protocol, checked by text search).
  - 2008: minor formulation changes cause factors of more than 1,000 (P8).
  - 2020–2025: five seeds and a ≥10%, four-of-five consistent-win rule (B7).
  - Evolution or contradiction left open.
- **C4 — When SCIP started.**
  - 2001: Ch. 3 of the thesis dates SCIP's development at ZIB from 2001 (P1 p. 23), and the interview puts the first commit in 2001 (P12 27:39).
  - 2002: the thesis Introduction says development started in October 2002 (P1 p. 6), and the acknowledgements say he started from scratch at the end of 2002 (P1 p. ix).
- **C5 — Black box vs. full control.**
  - 2004: SCIP is for experts who want total control down to the guts of the solver, not rapid prototyping (P4 pp. 1–2).
  - 2006 (co-authored): black-box software is unhelpful for teaching scientific method (P7 p. 2).
  - 2023: the commercial value of MIP solvers *is* black-box use, and a branch-cut-and-price framework reaches only a tiny audience (P12 1:02:34–1:04:26).
  - Different roles (academic framework vs commercial product) may explain it; recorded as found.
- **C6 — From scratch vs. reuse.**
  - 2023: he is bad at taking up others' work and always wants to build from scratch (P12 1:20:57).
  - But in 2007 SIP's code spared him from reinventing the wheel, and SCIP took over most of SIP's ideas (P1 pp. ix, 6).
  - In 2020 PSD cuts were taken straight from the literature (P14 1:08:53).
  - In 2023 he implemented Mark Turner's branching idea (P12 55:36), and at CPLEX he re-implemented what he had proven in SCIP (P12 40:37).
- **C7 — Which baseline counts.**
  - 2023: academic techniques should be judged against the framework they live in, not against Gurobi (P12 51:29).
  - His own academic papers nonetheless benchmarked against CPLEX each time, to show the testbed was near the state of the art (P3 2004, P5 2005, P1 2007).
  - Possibly two different purposes; left as tension.
- **C8 — Size of the Gurobi MIP test set.**
  - More than 5,000 (P15, Dec 2021).
  - 7,030 (P18, July 2022).
  - About 6,000 (P12, Aug 2023).
  - About 8,500 (P19, June 2025).
  - The 2022 to 2023 drop may reflect different subsets (full set vs a seed-run set); not resolved.
- **C9 — The value of conflict analysis.**
  - 2005: time +15% on feasible MIPs (P5 abstract).
  - 2007: more than 10% speedup with moderate effort (P1 pp. 5, 181).
  - 2023: all major solvers now use it to get faster (P12 32:18).
  - The change is attributed by him to implementation details (P1 p. 181).
- **C10 — Author list of ZR 02-32 (metadata).**
  - The cover names Achterberg and Koch.
  - The inner title page and the OPUS record name Achterberg, Koch and Martin.
  - A metadata discrepancy, not a methodological one.

## Gaps

- **G1** No essay, blog post or lecture by Achterberg on *how to do research* was found. A WebSearch for a Gurobi blog or article by him on testing practice found none, only Gurobi support pages not attributable to him.
  - Advice to students is limited to one remark (O-8).
  - No Beale–Orchard-Hays acceptance remarks, Tucker-finalist talk or recorded SEA 2022 talk were found.
- **G2** Achterberg & Wunderling 2013 (DOI 10.1007/978-3-642-38189-8_18) was **not read** (paywalled): abstract only, plus S4's second-hand description. Its *unbiased* scheme is known only through P9 and S4.
- **G3** The SCIP paper in MPC 2009 (DOI 10.1007/s12532-008-0001-1) was not read beyond its abstract (paywalled). The thesis covers the same ground.
- **G4** These were **not read** for stated method:
  - *Hybrid Solving Techniques* (Achterberg & Lodi 2010, DOI 10.1007/978-1-4419-1644-0_5); no open copy found, PolyPublie lists metadata only.
  - CPAIOR 2008 (DOI 10.1007/978-3-540-68155-7_4) and ZR 08-43, *Constraint Integer Programming: Techniques and Applications* (Achterberg, Berthold, Heinz, Koch, Wolter, 2008; https://opus4.kobv.de/opus4-zib/files/1095/ZR_08_43.pdf).
  - ZR 07-37, *Property Checking with Constraint Integer Programming* (Achterberg, Brinkmann, Wedler, 2007; https://opus4.kobv.de/opus4-zib/files/1037/ZR_07_37.pdf).
  - ZR 11-29, *Rounding and Propagation Heuristics for Mixed Integer Programming* (Achterberg, Berthold, Hendel, 2011; https://opus4.kobv.de/opus4-zib/files/1325/ZR-11-29.pdf).
  - The ParaSCIP papers (DOIs 10.1007/978-3-642-24025-6_12, 10.1109/IPDPSW.2014.174, 10.1109/IPDPS.2016.56; from the DBLP record list).
  - The Mcf-separator paper (DOI 10.1007/s12532-010-0015-3) and Hybrid Branching (DOI 10.1007/978-3-642-01929-6_23).
  - The CPAIOR 2013 IBM paper (DOI 10.1007/978-3-642-38171-3_1) and the RLT-cut papers (IPCO 2023, DOI 10.1007/978-3-031-32726-1_2; MP 2025, DOI 10.1007/s10107-024-02104-0).
  - MIPLIB 2010 (DOI 10.1007/s12532-011-0025-9) and MIPLIB 2017 (DOI 10.1007/s12532-020-00194-3), both collective texts with 16 authors.
- **G5** For the ILOG/IBM years (2006–2014) the only statements found are ZR 08-29 (2008) and the A&W abstract (2013). The IBM-era method is otherwise known only through a colleague's deck (S4).
- **G6** Interview and webinar evidence is ASR caption text and was not speaker-verified. The interview host is not identified in the metadata read.
  - The Gurobi 11.0 webinar (Dec 2023) was not used: speaker unidentifiable.
  - The 12.0 webinar was not searched.
  - The historic-measure name (*part 10* in the captions, probably PAR10) is unconfirmed.
- **G7** The promotion to VP R&D in April 2020 rests only on a search-result snippet (the old Gurobi press page returned 503). The webinar descriptions support only Director of Development (Dec 2019) and VP R&D (Dec 2020).
- **G8** The 2025 Substack comment is attributed by display name only. The author's identity was not verified.
- **G9** The DBLP list comes from another agent's SPARQL harvest (dblp.org showed a bot check to curl). DOIs used here were re-checked with Crossref and DataCite.
- **G10** Optima issues other than No. 80 and MIP-workshop slide archives were not searched systematically. One WebSearch for Achterberg workshop slides found none.

## Sources

Primary (his own words; co-authored texts marked):

- P1. *Constraint Integer Programming*, T. Achterberg, Dr. rer. nat. thesis, TU Berlin. Defended 12 July 2007; approved version 15 May 2007; revised version 10 Dec 2008, the one read: ZIB OPUS docId 1112. https://opus4.kobv.de/opus4-zib/files/1112/Achterberg_Constraint_Integer_Programming.pdf ; DOI 10.14279/depositonce-1634 (DataCite-checked). Read: abstract, acknowledgements pp. ix–x, Introduction pp. 1–6, Ch. 3 opening p. 23, Ch. 4 pp. 59–60, §5.11, §8.10 (pp. 111–113), §9.5 (p. 129), §10.10 (pp. 161–163), §11.3 conclusion (p. 181), §17.3 (p. 312), App. A (pp. 319–322), App. C (p. 377). Primary, solo.
- P2. *Branching on History Information*, T. Achterberg, T. Koch, A. Martin, ZIB-Report 02-32, Oct 2002. https://opus4.kobv.de/opus4-zib/files/699/ZR-02-32.pdf (abstract, conclusion). Primary, co-authored.
- P3. *Branching Rules Revisited*, T. Achterberg, T. Koch, A. Martin, ZIB-Report 04-13, May 2004. https://opus4.kobv.de/opus4-zib/files/788/ZR-04-13.pdf. Journal version: Oper. Res. Lett. 33(1):42–54, 2005, DOI 10.1016/j.orl.2004.04.002 (Crossref-checked). Read: abstract, §1, §2.1, §3.1–3.3, §4. Primary, co-authored.
- P4. *SCIP — a Framework to Integrate Constraint and Mixed Integer Programming*, T. Achterberg, ZIB-Report 04-19, June 2004 (text dated 2 Jan 2005). https://opus4.kobv.de/opus4-zib/files/794/ZR-04-19.pdf (abstract, §1). Primary, solo.
- P5. *Conflict Analysis in Mixed Integer Programming*, T. Achterberg, ZIB-Report 05-19, cover Aug 2005. https://opus4.kobv.de/opus4-zib/files/853/ZR-05-19.pdf. Journal version: Discrete Optim. 4(1):4–20, 2007, DOI 10.1016/j.disopt.2006.10.006 (Crossref-checked). Read: abstract, §1, results pp. 15ff., closing section. Primary, solo.
- P6. *MIPLIB 2003*, T. Achterberg, T. Koch, A. Martin, ZIB-Report 05-28, May 2005. https://opus4.kobv.de/opus4-zib/files/862/ZR-05-28.pdf. Journal version: Oper. Res. Lett. 34(4):361–372, 2006, DOI 10.1016/j.orl.2005.07.009 (Crossref-checked). Read: abstract, §1, §2.1. Primary, co-authored (Koch corresponding).
- P7. *Software for Teaching Modeling of Integer Programming Problems*, T. Achterberg, M. Grötschel, T. Koch, ZIB-Report 06-23, May/June 2006. https://opus4.kobv.de/opus4-zib/files/917/ZR-06-23.pdf (abstract, §1). Primary, co-authored.
- P8. *On the Effects of Minor Changes in Model Formulations*, T. Achterberg, T. Koch, A. Tuchscherer, ZIB-Report 08-29, Aug 2008. https://opus4.kobv.de/opus4-zib/files/1080/ZR_08_29.pdf (read in full). Primary, co-authored. Achterberg's affiliation on it: ILOG.
- P9. *Presolve Reductions in Mixed Integer Programming*, T. Achterberg, R. E. Bixby, Z. Gu, E. Rothberg, D. Weninger, ZIB-Report 16-44, Dec 2016. https://opus4.kobv.de/opus4-zib/files/6037/Presolve.pdf. Journal version: INFORMS J. Comput. 32(2):473–506, 2020, DOI 10.1287/ijoc.2018.0857 (Crossref-checked). Read: §1, §1.1, §9. Primary, co-authored.
- P10. *Mixed Integer Programming: Analyzing 12 Years of Progress*, T. Achterberg, R. Wunderling, in *Facets of Combinatorial Optimization* (Springer 2013), pp. 449–481, DOI 10.1007/978-3-642-38189-8_18 (Crossref-checked). Abstract only, from https://link.springer.com/chapter/10.1007/978-3-642-38189-8_18. Primary, co-authored.
- P11. *SCIP: Solving Constraint Integer Programs*, T. Achterberg, Math. Program. Comput. 1(1):1–41, published 20 Jan 2009, DOI 10.1007/s12532-008-0001-1 (Crossref-checked). Abstract only. Primary, solo.
- P12. *Subject to: Tobias Achterberg*, long-form interview on the YouTube channel *Subject to*, published 2023-08-17, 5,062 s. https://www.youtube.com/watch?v=8bhIW27vCUQ. Automatic English captions fetched 2026-11-08 with yt-dlp 2026.10.26 via uvx; read from 18:00 to the end. The personal and family parts at 0:00–18:00 were not used. Primary, spoken (ASR).
- P13. *What's New in Gurobi 9.0 (in English)*, Gurobi webinar, presenter T. Achterberg (Director of Development), 2019-12-18. https://www.youtube.com/watch?v=WkIcLO_d7aI (captions, targeted reading). Primary, spoken (ASR).
- P14. *Recent Developments in the Gurobi Optimizer 9.1*, Gurobi webinar (Z. Gu, T. Achterberg, E. Klotz), 2020-12-11. https://www.youtube.com/watch?v=EwuEPu-nBmg. His non-convex MIQCP segment 1:05–1:31 and the Q&A at 0:59:59 were used. Primary, spoken (ASR).
- P15. *Webinar: What's New in 9.5*, Gurobi (T. Achterberg, M. Jaczynski), 2021-12-09. https://www.youtube.com/watch?v=UFV4ZYsHFdY (captions, targeted reading). Primary, spoken (ASR).
- P16. *What's New in Gurobi 10.0*, Gurobi webinar, introduced as T. Achterberg (VP R&D) and M. Jaczynski, 2022-11-29. https://www.youtube.com/watch?v=n0sEYVtIqvw (captions, targeted reading). Primary, spoken (ASR).
- P17. *What's New in Gurobi 13.0*, Gurobi webinar, performance segment by T. Achterberg, 2025-12-01. https://www.youtube.com/watch?v=NdGUcuskm0w (captions 0:00–0:15:25). Primary, spoken (ASR).
- P18. *Combinatorial Algorithms Used Inside a MIP Solver*, T. Achterberg, invited talk at SEA 2022 (Heidelberg), slides dated 26 July 2022. https://sea2022.ifi.uni-heidelberg.de/talk_achterberg.pdf (65 slides, text read in full). Primary, solo slides.
- P19. Comment posted under the name Tobias Achterberg, 2025-06-15, on M. Watson's Substack post (S5). Read via https://miketalksai.substack.com/api/v1/post/137676066/comments. Primary (identity not verified).

Secondary, observed and metadata:

- S1. *Optima* 80 (MPS newsletter), Sept 2009: chair's column and the prizes section (Beale–Orchard-Hays Prize 2009 citation; Tucker Prize 2009 finalist text). https://mathopt.zib.de/Optima-Issues/optima80.pdf. Secondary (observed).
- S2. INFORMS award-recipient page for Tobias Achterberg: 2011 Optimization Society Young Researchers Prize citation (committee Bienstock, Boros, McCormick, Renegar) and 2008 Dantzig Dissertation Award, second place. https://www.informs.org/Recognizing-Excellence/Award-Recipients/Tobias-Achterberg. Secondary (observed).
- S3. Gurobi press release *Dr. Tobias Achterberg Joins the Gurobi Optimization R&D Team* (2014; no date in the page text). https://www.gurobi.com/company/newsroom/dr-achterberg-joins-gurobi. Secondary (used for role: lead MIP developer for CPLEX 12.0–12.6).
- S4. *Recent MIP Performance Improvements in IBM ILOG CPLEX Optimization Studio*, A. Tramontani (IBM), 22 Jan 2014, SlideShare. https://www.slideshare.net/IBMOptimization/2014-0122-vugmipperformance. Slides 7–8 cite Achterberg–Wunderling 2013. Secondary (observed).
- S5. *Five Ideas I'll use in my optimization class after listening to Gurobi's Tobias Achterberg*, M. Watson, Substack, 2023-10-05. https://miketalksai.substack.com/p/five-ideas-ill-use-in-my-optimization. Secondary (a listener's reading of P12).
- S6. SEA 2022 home and program pages (invited speaker, talk title and abstract, slides link). https://sea2022.ifi.uni-heidelberg.de/ and https://sea2022.ifi.uni-heidelberg.de/program.html. Secondary (metadata).
- S7. YouTube descriptions and metadata of P12–P17 (roles at dates; presenters), fetched 2026-11-08. Secondary (metadata).
- S8. DBLP record list, pid 71/6632 (23 records; SPARQL harvest file `dblp.json` in the member scratch folder). Secondary (metadata).
- S9. Crossref API records for the 14 DOIs cited above, and DataCite for 10.14279/depositonce-1634. Secondary (metadata).
- S10. Gurobi press release on promotion to VP R&D (old site; HTTP 503; search snippet only). https://www-old.gurobi.com/news/gurobi-optimization-announces-promotion-of-dr-tobias-achterberg-to-vice-president-of-rd/. Secondary, **unverified**.
- S11. PolyPublie record for *Hybrid Solving Techniques* (Achterberg & Lodi). https://publications.polymtl.ca/17383/. Secondary (metadata only; no full text).
- S12. *Whats New in Gurobi 11.0*, Gurobi webinar, 2023-12-15. https://www.youtube.com/watch?v=_TNKpaFTHl4. Checked; speaker not identifiable; **not used**.

Other works named in this note. Metadata was checked with Crossref in this run; none was read, and none is counted among the 31 sources:

- Bixby, Fenelon, Gu, Rothberg, Wunderling, *MIP: Theory and Practice — Closing the Gap*, System Modelling and Optimization (IFIP, Kluwer 2000), pp. 19–49. DOI 10.1007/978-0-387-35514-6_2. Cited by P1 as [46].
- Bixby, Fenelon, Gu, Rothberg, Wunderling, *Mixed-Integer Programming: A Progress Report*, The Sharpest Cut (MPS-SIAM 2004), ch. 18, pp. 309–325. DOI 10.1137/1.9780898718805.ch18. Cited by P9 as [11].
- Bixby, Rothberg, *Progress in computational mixed integer programming—A look back from the other side of the tipping point*, Ann. Oper. Res. 149:37–41, 2007. DOI 10.1007/s10479-006-0091-y. Cited by P9 as [12].
- van Vyve, Wolsey, *Approximate extended formulations*, Math. Program. 105:501–522. DOI 10.1007/s10107-005-0663-7. The starting point of P8.
- Fischetti, Jo, *Deep neural networks and mixed integer linear optimization*, Constraints 23:296–309, 2018. DOI 10.1007/s10601-018-9285-6. Inferred as the paper alluded to in P12 1:00:45 (not confirmed).
- The Achterberg works listed under G4, by DOI or ZIB OPUS URL.
