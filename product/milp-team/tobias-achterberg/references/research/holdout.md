# Holdout: Tobias Achterberg

- **Researcher**: Tobias Achterberg (living; DBLP pid 71/6632; ORCID 0000-0002-0862-7065)
- **Date**: 2026-11-14
- **Rule**: Sealed until the validation is done: this is test material, not evidence. It must not appear in the Phase 2 record, in SKILL.md or among the Phase 4 exam's questions. To unseal an item after a validation, move it under a heading '## Unsealed (<date>)' at the end of this file.
- **Status when picked**: research notes 01–06 and `00-prior.md` existed; no `SKILL.md` existed for this member. The items were picked before the synthesis.
- **Sealed items**: 5 (H1–H5).

## How the items were checked

- Every point below was read in the source itself in this run, not taken from the notes. The copies opened are the ones the notes' agents downloaded on 2026-11-08 into the scratch folder `C:\Users\sr881\AppData\Local\Temp\milp-team-t1-scratch\base-skills\tobias-achterberg\` (`03\papers\`, `03\thesis\`, `02\subject_to_ts.txt`). Page numbers were re-checked here with `pdftotext` page by page.
- **Quotation policy**: to respect copyright this file carries one verbatim quotation (in H1, under 15 words). All other points are close paraphrases with a page or timestamp. Quotation marks elsewhere enclose only titles, table-column labels, labels taken from the notes, or the wording of a hypothetical test answer; none of them is a quotation of Achterberg. A grader who needs exact wording opens the source at the locator given.
- **Page conventions**: thesis = printed page of the revised ZIB copy (OPUS docId 1112; PDF page = printed + 14). ZR 04-13 = printed page (PDF page = printed + 1). ZR 16-44 = printed page (PDF page = printed + 2). Interview = timestamps of the 30-second caption lines in `02\subject_to_ts.txt`; the saved excerpt file uses slightly different line starts.
- **Authorship**: H1 and H4 are co-authored texts. Their "we" cannot be split among the authors; a grader should treat them as decisions Achterberg co-signed. H2 and H3 are from his sole-author thesis. H5 is his spoken answer, read as YouTube automatic captions (not speaker-checked).

| Id | Year | Topic | Kind | Source |
|---|---|---|---|---|
| H1 | 2004 | Protocol of a branching-rule benchmark | decision | ZIB-Report 04-13, pp. 8–9 |
| H2 | 2006–2007 | A cut separator tuned towards a competitor's root gap | decision | Thesis, pp. 112–113 |
| H3 | 2007 | A presolve default that disagrees with published advice | decision | Thesis, pp. 150, 161–162 |
| H4 | 2016 | Independent blocks inside a general-purpose solver | decision | ZIB-Report 16-44, pp. 51–53 |
| H5 | 2023 | Whether to build a commercial branch-and-price solver | argued answer | Interview, 1:02:20–1:05:00 |

---

## H1

**Source**: T. Achterberg, T. Koch, A. Martin, "Branching Rules Revisited", ZIB-Report 04-13, May 2004, §3.1–3.2, pp. 8–9 (including footnote 1 on p. 8). https://opus4.kobv.de/opus4-zib/files/788/ZR-04-13.pdf. Journal version: Oper. Res. Lett. 33(1):42–54, 2005, DOI 10.1016/j.orl.2004.04.002 (Crossref-checked on 2026-11-14; journal text not read). The 2002 protocol mentioned in the question is in ZIB-Report 02-32, text before Table 3 (https://opus4.kobv.de/opus4-zib/files/699/ZR-02-32.pdf).

**Question**: In 2004 you are setting up the computational comparison for a paper on branching rules, together with Thorsten Koch and Alexander Martin. The rules are implemented in Martin's solver SIP, which uses CPLEX as its LP solver. Comparing branching rules is confounded by everything else in the solver: a rule can look good on an instance only because its choices happened to run into a good solution early. In your 2002 study you dealt with this in a second test, by supplying the optimal solution in advance and freezing the root cuts. Your options now: give every run the optimal objective value up front again, or leave the primal side alone; and run full branch-and-cut, cuts at the root only, or no cuts. You also have to convince readers that results measured inside SIP say something about state-of-the-art solvers. What do you do, and why?

**What they actually said or did**
1. The optimal values were not set beforehand. The reason given (p. 8, verbatim): "leading towards feasible solutions fast is a desirable property of branching rules".
2. The confound is named, not denied: a worse rule can need fewer nodes and less time on one instance because its variable choices happen to find a good or optimal solution early (p. 8). Footnote 1 lists four ways a better primal solution changes a run: earlier cutoff; less time per node, because the dual simplex and the strong-branching LPs can stop at the upper bound; a shift of node selection from depth-first-like towards best-first-like, which changes where strong branching is used; and the diving heuristic, during which pseudocosts are updated.
3. The isolation is done on the cut side instead: default settings, except that cuts are generated at the root only (cut-and-branch), which they say brings out the influence of the branching rule best (p. 8).
4. To show that the SIP environment is state of the art, CPLEX 9.0 is run on the same test set. SIP's preprocessing and cuts are used inside CPLEX in place of CPLEX's own, so that both codes run pure branch and bound on the same problems; CPLEX's absolute and relative gap tolerances are set to SIP's values (pp. 8–9).

**Why this one**: a real fork with a stated reason, and it reverses the authors' own 2002 choice. A reader of the paper gets it right. A good researcher who has not read it will most likely install the optimal value as a cutoff to isolate the rule (a later SCIP study reported in `05-peer-critique.md` §2.2 does exactly that), or answer in general terms about controlling confounders. It also probes whether the skill captures a judgement that runs against "isolate the component at any price".

**Where it appears in the notes** (leave these passages out of the synthesis; line numbers as of 2026-11-14)
- `01-publications.md`: §2 SW2, row "Abandoned paths", item (b) (line 201); Contradictions C2 (line 301).
- `02-methodology.md`: §4 E-2, first and second bullets (lines 168–169); E-3, first bullet (line 173); §5 J-5, first bullet, the "P3 p. 8" part (line 244); the B9 row cites the same page (line 358).
- `03-process-evidence.md`: PE-01, second bullet (line 77); §5b table, row 2004, "Baseline" cell (line 193); PE-24, first and second bullets (lines 239–240); F-3 (line 356); §10 first bullet, the clause on the protocol change (line 367); §12 table, row E-2, the verdict clause (line 392); Contradictions C-01 (lines 406–408).
- `05-peer-critique.md`: §2.1 "2004 report", the two "p. 8" bullets (lines 111–112); §2.2, last sentence of the closing [inferred] paragraph (line 145); §2.4, the [inferred] line under Shah–Dey (line 178); Contradictions C11 (line 488).
- `04-mentorship.md`, `06-trajectory.md`: not present.

---

## H2

**Source**: T. Achterberg, *Constraint Integer Programming*, Dr. rer. nat. thesis, TU Berlin, 2007 (revised 10 Dec 2008), §8.10, Table 8.1 (p. 112) and the text on p. 113, which also discusses Table 8.2. ZIB OPUS docId 1112, https://opus4.kobv.de/opus4-zib/files/1112/Achterberg_Constraint_Integer_Programming.pdf (DOI of the 2007 copy: 10.14279/depositonce-1634). The student's study is the thesis's reference [218]: K. Wolter, *Implementation of Cutting Plane Separators for Mixed Integer Programs*, Diplomarbeit, TU Berlin, 2006 (entry checked in the thesis bibliography; Wolter's text not read here).

**Question**: In 2006 your student Kati Wolter compares SCIP's cutting-plane separators with those of CPLEX and CBC. She finds that SCIP's Gomory mixed-integer cuts close less of the gap at the root node than the other two codes' do. You are settling SCIP's default settings for your thesis benchmarks. What do you do about the Gomory separator, how do you find out whether that was right, and what do you report?

**What they actually said or did**
1. First reaction: the Gomory separator's parameters were made more aggressive, so that it produces more cuts. That removed the root-gap deficit against CPLEX and CBC (p. 113).
2. The check came from the knock-out benchmark, which got an extra column, "cons Gom": the aggressive separator replaced by a conservative one that adds only cuts that appear numerically stable. The conservative variant improves on the default, and by more than switching Gomory cuts off altogether ("no Gom"). His own words for the earlier change are that they overshot the mark (p. 113; Table 8.1 on p. 112. The table's total row for runtime does not extract cleanly, so no figures are copied here).
3. He separates isolation from combination. With one separator switched on over pure branch-and-bound (Table 8.2), the conservative and the aggressive Gomory variant help about equally, and Gomory and flow cover cuts come second and third behind c-MIR. With all separators on, the conservative variant improves overall performance and the aggressive one worsens it (p. 113).
4. His reading: what Gomory and flow cover cuts do is sufficiently covered by the c-MIR cuts. He adds that Bixby et al. had found Gomory cuts the most effective in CPLEX 6.5, at a time when CPLEX had no complemented MIR cuts (p. 113).
5. The benchmarked default still contains the aggressive separator, and the thesis prints the overshoot. Whether the default was changed afterwards is not stated on these pages (not checked).

**Why this one**: a small judgement inside a long results section, with a correction of his own earlier move. Someone who knows the thesis chapter gets it. A good researcher who does not will stop at "tune it until it matches CPLEX's root gap", or say only "measure total time", without the conservative variant, the isolation-versus-combination contrast or the c-MIR explanation.

**Where it appears in the notes**
- `04-mentorship.md`: §2.3, last bullet, "A student's measurement changes the mentor's defaults…" (line 68); §7, bullet "Gomory overshoot" (line 113).
- Neighbouring material that is **not** sealed but should not be expanded with the Gomory details: `02-methodology.md` E-1 (the three-way cut design, P1 p. 111) and J-3 third bullet (P1 p. 113, nodes versus time when single separators are disabled); `03-process-evidence.md` PE-32, first bullet (non-additivity).
- `01`, `03`, `05`, `06`: the episode is not present.

---

## H3

**Source**: T. Achterberg, *Constraint Integer Programming* (as in H2), §10.2 p. 150 (Step 7 of the knapsack presolving Algorithm 10.8 and Example 10.12) and §10.10 pp. 161–162 (Table 10.1, column "no knap disaggreg", and the text that follows). The advice he sets his result against, as cited there: R. E. Bixby, M. Fenelon, Z. Gu, E. Rothberg, R. Wunderling, "MIP: Theory and Practice – Closing the Gap", in *System Modelling and Optimization*, Kluwer 2000, pp. 19–49, DOI 10.1007/978-0-387-35514-6_2; A. Fügenschuh, A. Martin, "Computational Integer Programming and Cutting Planes", in *Discrete Optimization*, Handbooks in OR & MS 12, 2005, pp. 69–121, DOI 10.1016/S0927-0507(05)12002-7 (both DOIs Crossref-checked on 2026-11-14; neither text read).

**Question**: In 2007 you are deciding the default for one step of SCIP's knapsack presolving. Using the clique table, the step tightens coefficients; on an aggregated precedence constraint such as q·y + x1 + … + xq ≤ q it ends up replacing the single row by the q set packing rows y + xl ≤ 1. The LP relaxation gets tighter and the model gets more rows. Published advice (Bixby, Fenelon, Gu, Rothberg and Wunderling 2000; Fügenschuh and Martin 2005) is to keep such constraints aggregated and to separate the implied bound cuts on demand. You can follow the literature and switch the step off, leave it on, or make it a parameter. How do you decide, what do you end up with, and how do you write it up if your result and the literature disagree?

**What they actually said or did**
1. When he describes the algorithm he sides with the caution: complete disaggregation of an aggregated precedence constraint is called usually not desirable in presolving, because the extra rows slow the LP even though the relaxation gets tighter. So the step can be switched off by a parameter (p. 150).
2. The decision is left to the knock-out benchmark: Table 10.1 has a column, "no knap disaggreg", in which the step is skipped (p. 161).
3. The result goes against the cited advice and is reported with its number: disaggregating in presolve improves overall performance by 5 %. The claim is scoped explicitly to SCIP and to his test sets; the step stays on in the default (pp. 161–162).
4. First mechanism offered: SCIP's default separates cutting planes at the root only, so missing implied bound cuts cannot be generated at local nodes (p. 162).
5. Second mechanism offered: the immediately stronger LP relaxation makes strong branching more effective, since no cuts are separated for the strong-branching LPs (p. 162). Both are labelled a possible explanation; neither is tested.

**Why this one**: a side decision in which his measurement contradicts two sets of authors close to him (Bixby was the second referee of this thesis, Martin his co-author on the branching papers) and his own stated expectation eleven pages earlier. Someone who knows the presolving chapter gets it. A good researcher who does not will either follow the literature or say "trust your own benchmark and scope the claim", without the two solver-specific mechanisms that make the result plausible.

**Where it appears in the notes**
- `03-process-evidence.md`: PE-31, third bullet (line 290).
- Not sealed, different columns of the same table: `02-methodology.md` J-11 (pairs of linear constraints, P1 p. 161); `03-process-evidence.md` PE-33 last bullet (aggregation step disabled, S1 p. 161).
- `01`, `04`, `05`, `06`: not present.

---

## H4

**Source**: T. Achterberg, R. E. Bixby, Z. Gu, E. Rothberg, D. Weninger, "Presolve Reductions in Mixed Integer Programming", ZIB-Report 16-44, 2016, §7.3 "Disconnected components", pp. 51–53 (Table 30 on p. 53). https://opus4.kobv.de/opus4-zib/files/6037/Presolve.pdf. Journal version: INFORMS J. Comput. 32(2):473–506, 2020, DOI 10.1287/ijoc.2018.0857 (Crossref-checked on 2026-11-14; journal text not read). Five authors in alphabetical order; who designed this part is not stated.

**Question**: In 2016 you and your co-authors at Gurobi describe what the solver (version 6.5) does when a MIP falls apart into independent blocks: sets of variables and constraints that share nothing with each other, whether from the original formulation or after earlier reductions. Mathematically the model is then several separate MIPs, and the obvious move is to solve them one after another and put the pieces together. You are building a general-purpose product that users run with time limits and gap limits. Do you take the obvious route, ignore the structure, or do something else? What do you do, and why?

**What they actually said or did**
1. The simple successive scheme is rejected for two stated reasons (p. 52). First, a feasible solution of the whole problem exists only once all components but the last are solved and the last has a solution; if one component is hard, the user sees no solution for a long time or hits the time limit. They grant that this does not lengthen the time to optimality and call it undesirable in practice all the same. Second, gap limits (by default 0.01 % relative) apply to the objective of the whole problem and cannot easily be broken down into limits per component.
2. First strategy, in presolve: try to solve every component except the largest to true optimality with zero gap, under fairly strict work limits that guard against one hard component; for each component solved this way, fix its variables in the master problem (p. 52).
3. In those component solves presolve is switched off, so that an optimal solution of a presolved component cannot turn out to violate the feasibility tolerances once it is mapped back to the master problem (p. 52).
4. Second strategy, at the end of the root cutting-plane loop, if the problem has independent components at that point (none was solved in presolve, or later modifications split it): the component MIPs are solved interleaved, each with a zero gap limit, 500 nodes per component per pass. Whenever a component improves its incumbent, the full incumbent is updated, and it is reported once every component has a solution. The procedure stops when the overall gap limits are reached or a component is infeasible; when all components but one are solved it is abandoned for the standard solve (pp. 52–53).
5. Measured (p. 53, Table 30): about 20 % of the 3,182 test models have disconnected components, more often after other presolve reductions or root fixings than in the original formulation. On those models the ≥ 10 s bracket is 36 % faster, 6 % overall. Most components are tiny; a few are not.

**Why this one**: a design choice in a product, with the reasons printed: what the user sees during the solve, and how a tolerance defined on the whole problem behaves when the problem is split. The notes do not use this section at all, so nothing has to be cut from the synthesis. A reader of the paper gets it. A good researcher who has not read it will propose exactly the scheme the paper rejects, or a parallel variant of it, and will miss the gap-limit argument, the presolve-off safeguard and the interleaving.

**Where it appears in the notes**
- Not used in any note. The paper itself is cited throughout (01 as S8, 02 as P9, 03 as S12, 04 as P7, 05 as S9, 06 as P12), for §1, §3–5 and §9 only.
- One nearby remark that is **not** sealed and should stay as short as it is: `02-methodology.md` C-5, third bullet (line 113: a 2025 webinar remark that the code for models with many disconnected components was rewritten for customers).

---

## H5

**Source**: "Subject to: Tobias Achterberg", long-form interview, YouTube channel Subject to, uploaded 17 Aug 2023, https://www.youtube.com/watch?v=8bhIW27vCUQ, 1:02:20–1:05:00. Read as YouTube automatic captions (fetched 2026-11-08 by research agent 02; `02\subject_to_ts.txt` in the scratch folder). Caption text: not speaker-checked, host and guest not separated, names garbled.

**Question**: In 2023 you lead R&D at a commercial MIP solver vendor. An interviewer asks whether it is worth developing a commercial branch-and-price solver. What do you answer, and how do you argue it?

**What they actually said or did** (paraphrase of caption text)
1. He starts from why MIP solvers succeed commercially: they are a black box. People who can model their business problem in variables and constraints, and know nothing about algorithms, plug the model in and get a solution (1:02:20–1:02:51).
2. A branch-cut-and-price solver can, in his view, only be a framework: the pricing rule, and the cutting planes that have to fit the pricing, must be hand-tailored to the problem. Every user would need strong mathematics and coding skills, which shrinks the audience to a tiny fraction (1:02:51–1:03:22).
3. He backs this with his own users: only a very small fraction of Gurobi users use callbacks; most of those use them only for information, such as messages, or to terminate a solve; those who separate cuts, add lazy constraints or write primal heuristics are a tiny fraction of all users (1:03:22–1:04:26).
4. Verdict: he does not think a big commercial success can be made of it (1:04:26).
5. The exception he allows: a code for one class of problems, such as vehicle routing, which uses branch and price inside while the user only supplies the application data. That could succeed if the application is important enough (1:04:26–1:05:00).

**Why this one**: a complete argued answer to one question about what is worth building, with his own evidence (callback usage) and a stated exception. A listener of the interview gets it. A good researcher who has not heard it will probably say "the market is small" or argue from the technical promise of decomposition, without the black-box premise, the callback evidence or the application-specific exception. It also touches a live difference with the branch-and-price member of this team, which makes a generic answer easy to tell from his.

**Where it appears in the notes**
- `02-methodology.md`: §1 T-1 (lines 53–56); §2 C-7, first bullet (line 120); Contradictions C5, third bullet (line 389).
- `references/sources/talks/subject-to-2023-interview.excerpt.transcript.txt`: the passage itself is not among the fourteen excerpts, but line 102 (the first line of excerpt L) carries the last clause of the answer. Do not quote that clause.
- **Not** sealed: the answer that precedes it in the interview, on automatic decomposition and GCG (excerpt K; `02` C-7 last bullet, `04` §4, `05` §11 item 7).
- `01`, `03`, `05`, `06`: not present.

---

## Selection record

Considered and not sealed, with the reason:
- The origin of reliability branching in a machine-learning thesis, conflict analysis learned on a subway ride, two years without a paper, writing versus another 10 %: reported by every account and by several notes; both test arms would score full marks.
- Knock-out ablation, shifted geometric mean, solve-time brackets, test-set rules: stated in `00-prior.md` or the core of the method; sealing them would hollow the skill out.
- Restarts only after the root (thesis pp. 160–163): a good argued passage, but it is used in more than fifteen passages of five notes and SCIP's root restarts are widely known, so the baseline arm would probably answer it.
- The conflict-analysis variants of thesis §11.3 and the 2008 study of minor formulation changes (ZR 08-29): each carries most of the evidence for a likely core method.
- The MCF separator (ZR 09-38): the main example of "no harm outside the target class".
- Commit-log reverts of September 2008: one-line messages, too thin for 3–5 points.
- Anything from the first 18 minutes of the interview and its redacted passages: personal, not research craft.
