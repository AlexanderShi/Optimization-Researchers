# Matteo Fischetti · Sealed holdout (test material)

- **Researcher**: Matteo Fischetti (University of Padova, DEI; ORCID 0000-0001-6601-0568; DBLP pid 47/4770). Not Martina Fischetti.
- **Date**: 2026-11-14
- **Rule**: Sealed until the validation is done: this is test material, not evidence. It must not appear in the Phase 2 record, in SKILL.md or among the Phase 4 exam's questions. To unseal an item after a validation, move it under a heading '## Unsealed (<date>)' at the end of this file.
- **Status when picked**: no `SKILL.md` existed for this member, so the items were picked before the synthesis. Research notes 01-06 and `00-prior.md` were read in full; nothing here is stated in `00-prior.md`.
- **How the points were taken**: from the source itself, not from the notes' summary. Each source was opened as the working copy the notes point to, in the scratch folder `milp-team-t1-scratch/base-skills/matteo-fischetti/` (PDF plus `pdftotext` output); the file used is named under each item. Page numbers are the printed page numbers of the author preprint. Quotes are verbatim and kept short; a word hyphenated at a line break in the PDF is rejoined. Everything outside quotation marks is paraphrase.
- **Authorship caveat for the grader**: H1-H4 are co-authored papers, so each decision is the team's and the "we" voice cannot be split among the authors. H5 is the sole-author 2026 manuscript, which is unreviewed and declares AI assistance in drafting and coding; the decision is his by his own declaration of responsibility.
- **Items**: 5 (H1-H5), spread over 2004, 2009, 2014, 2013-15 and 2026, and over five topics (cut management inside a solver, Benders cut selection, a competition heuristic, time accounting in a variability study, arm design in a factorial experiment).

---

## H1

**Source**: G. Codato and M. Fischetti, "Combinatorial Benders' Cuts for Mixed-Integer Linear Programming", author preprint dated May 24, 2004, revised February 16, 2005, https://www.dei.unipd.it/~fisch/papers/combinatorial_benders_cuts_for_milp.pdf, Section 5 (pp. 11-12) and Section 6 (p. 19). Journal version: Operations Research 54(4):756-766, 2006, DOI 10.1287/opre.1060.0286 (not read; the preprint was read). Working copy: `03/pdf/combinatorial_benders_cuts_for_milp.pdf`.

**Question**: In 2004 you are implementing combinatorial Benders (CB) cuts, with a master's student, inside the branch-and-cut of ILOG-Cplex 8.1. The cuts are globally valid, your separation procedures are heuristic, and the number of generated cuts grows steeply. Cplex 8.1 has no internal cut pool: a globally valid cut added at run time stays in the LP for good. You can add the cuts as they are and live with a growing LP, separate far less often, keep a pool of your own outside the solver, or find some other way to get cuts out of the LP again. What do you do, and why? Say what your choice costs you. A reader then asks why you project the continuous variables out at all, when you could leave them in the master and use CB cuts as ordinary cutting planes: what do you answer?

**What they actually said or did**:
1. They name the real obstacle precisely. The missing pool "is not really an issue in itself", since an external data structure can store the cuts. The issue is "the impossibility of removing a (globally valid) cut from the current LP", so the LP risks becoming too large (p. 12).
2. They exploit an exception in the solver: locally valid cuts are removed automatically the first time they are no longer guaranteed valid, after a backtracking step. The work-around is to define the CB and {0,1/2}-cuts "as local (as opposed to global) cuts", although they are globally valid, so that the solver purges them from time to time (pp. 11-12).
3. They state the price. The device gives no complete control over the cut removal mechanism or over the size of the LP; "it works reasonably well in practice", and it implies a memory overhead (p. 12).
4. They also limit separation so as not to overload the LP: the separators are not called at every node, but before each update of the incumbent, at nodes of depth at most 10, and after each backtracking step; all cuts are stored in a constraint pool that is purged from time to time (p. 11).
5. On decomposition versus plain cut generation (p. 19): leaving the continuous variables in the master and using CB cuts as cutting planes was tried, and its main drawback was "wild fractional points that are very difficult to separate" with their simple separation heuristics. A two-step use (run the decomposition for a while, then restart the original model with the collected cuts) is left to future investigation.

**Why this one**: a design choice in code with a real fork and a stated price. A reader who knows the paper recalls the trick of declaring valid cuts local. A good researcher who does not know it will most likely propose an own cut pool or cut ageing, which the paper says does not solve the problem, because the solver of the time could not remove a global cut. It is a side decision: the method itself (no-good cuts from minimal infeasible subsystems) is not sealed.

**Where it appears in the notes**: `01-publications.md`, §2 SW3, table row "Minimum evidence (a)", the last clause only (Cplex 8.1 had no cut pool for removable global cuts, so the authors declared their cuts local). Points 4 and 5 are not in any note. The synthesis should leave that clause out; the rest of the row (map labelling, speed-ups, "simple implementation") is not sealed.

---

## H2

**Source**: M. Fischetti, D. Salvagnin and A. Zanette, "Minimal Infeasible Subsystems and Benders' cuts", extended draft, revised September 2009, https://www.dei.unipd.it/~fisch/papers/Benders_mis_extended_draft.pdf, Section 4 (pp. 10-11) and Section 5 (p. 12). Published in shortened form as "A note on the selection of Benders' cuts", Mathematical Programming 124:175-182, 2010, DOI 10.1007/s10107-010-0365-7 (not read; whether the passage survives in the note was not checked). Working copy: `03/pdf/Benders_mis_extended_draft.pdf`.

**Question**: In 2008-09 you select Benders cuts by optimising over the alternative polyhedron of the infeasible slave system: a cut-generating LP minimises a weighted sum of the multipliers, one per slave row plus one for the objective row. In the first version of the work (an Oberwolfach report of November 2008) every weight is 1, in the hope of a small-support vertex, that is, a small minimal infeasible subsystem. Then some instances behave pathologically. You can set them aside as outliers, tune the weights per problem class, fall back on the textbook cut-generating LP for them, or look inside the instances. What do you do, what do you change in the method, and how do you report the change?

**What they actually said or did**:
1. They say what the earlier choice was and why: in the previous version all weights were set to 1, aiming to reduce the cardinality of the support of the optimal vertex, a heuristic for a minimum-cardinality MIS (p. 10).
2. They looked inside: "By analyzing some specific pathological instances" they observed that "matrix T often has null rows". These are "static" conditions of the slave that are always active and do not depend on the master variables x (p. 10).
3. The change follows from that structure and is not a tuned number: for such rows "there is no reason to penalize the corresponding multiplier", so its weight is set to 0. The final rule is weight 0 for null rows of T, 1 for the others, and 1 for the objective-row multiplier, which is described as a scaling factor (pp. 10, 12).
4. They report it as a correction of their own earlier version, cited as such, and give the effect: a "quite substantial improvement of the generated cuts in many cases" (p. 10).

**Why this one**: a correction between two versions of the same paper, with the diagnosis stated. Someone who knows the note's history recalls the null rows. A good researcher who does not will answer in general terms (rescale, normalise, tune). The item is one bullet in the notes and is not the main evidence for the cut-selection method, which rests on the alternative-polyhedron idea and the computational comparison.

**Where it appears in the notes**: `03-process-evidence.md`, §5f, item PE-28 (the whole item). Nowhere else. The synthesis should leave PE-28 out. Not sealed: the same note's §9 row on the McDaniel-Devine warm start, `04-mentorship.md` §7 on the long draft becoming a short note, and `05-peer-critique.md` §5.1 on later critiques of the selection rule.

---

## H3

**Source**: M. Fischetti, M. Leitner, I. Ljubić, M. Luipersbeck, M. Monaci, M. Resch, D. Salvagnin and M. Sinnl, "Thinning out Steiner trees: a node-based model for uniform edge costs", technical report for the 11th DIMACS Implementation Challenge (PDF created 29 November 2014), https://www.dei.unipd.it/~fisch/papers/thinning_out_Steiner_trees_dimacs11.pdf, Section 3.2 (pp. 10-11) and Section 4.3 (pp. 15-18, Tables 3 and 6). Journal version: Mathematical Programming Computation 9(2):203-229, 2017, DOI 10.1007/s12532-016-0111-0 (not read). Working copy: `03/pdf/thinning_out_Steiner_trees_dimacs11.pdf`.

**Question**: In 2014 you are in a joint Padova-Vienna team preparing for the 11th DIMACS Implementation Challenge on Steiner trees. For the hardest unsolved uniform-cost instances (hypercube and bipartite graphs of the PUC class) even the LP relaxation of the usual model is too slow. Your idea is to solve a set-covering relaxation heuristically and then repair the solution into a connected one with a branch-and-cut on a restricted model. The set-covering heuristic you trust on large hard instances is the Caprara-Fischetti-Toth (CFT) Lagrangian heuristic, but the only implementation you can get at is a binary executable inside a commercial crew-scheduling product, which your code cannot call. A preliminary study also shows that the hypercube instances are highly symmetric, and that one Steiner node could be fixed to 1 without loss of generality to reduce the symmetry group. What do you do first, what later, what goes into the paper, and what do you do about the symmetry?

**What they actually said or did**:
1. First a quick shot with what was at hand. The CFT heuristic was "only available to us as a binary executable", the TURNI commercial implementation, so it was used "off-line through input/output text files". The approach could not be iterated: a single set-covering solution was refined, and TURNI was run once with a short time limit (one minute; 30 minutes for hc11u) (p. 16).
2. The quick shot already told them what they needed. "To our pleasant surprise", even in this simplified setting the repair phase was fast and gave connected solutions whose cost was very close to that of the set-covering solution. Table 3 shows new best values on five of the seven instances listed (p. 16).
3. The proper implementation came after. "Significantly better results were obtained at a later stage", when they implemented the CFT heuristic themselves and embedded it fully in the iterated Benders-like scheme (p. 16; Table 6, pp. 17-18).
4. Both stages are in the paper. The first table is kept and labelled as very preliminary, next to the later one, so the reader sees the order of the work.
5. On symmetry they chose not to act. Because the goal was better heuristic solutions for the unsolved cases, they did not investigate symmetry further and "preferred not to apply the symmetry-breaking fixing". The reason given: symmetry "can even be of help when heuristics come into play", since it mitigates the impact of bad heuristic choices (p. 15).

**Why this one**: a decision about order of work under a deadline, with a second, smaller judgement (leave the symmetry alone) whose reason runs against the usual reflex. Someone who knows the Steiner work recalls the off-line TURNI run and the later re-implementation. A good researcher who does not will probably say "re-implement first" or "use a MIP solver for the set-covering step", and "break the symmetry". It is a side episode of the paper, whose main claim (the node-based model) is not sealed.

**Where it appears in the notes**: `03-process-evidence.md`, §9, table row "Steiner set-covering repair (2014)" (the whole row). The symmetry judgement (point 5) is in no note. Not sealed: the "blur" principle from the same Section 3.2 (`03-process-evidence.md` PE-09; `02-methodology.md` §3.5), the node-only model (PE-03), the 10-seed protocol (PE-19, PE-24), and the unrelated mentions of TURNI as the origin of local branching in `01-publications.md` SW1.

---

## H4

**Source**: M. Fischetti, A. Lodi, M. Monaci, D. Salvagnin and A. Tramontani, "Improving Branch-and-Cut Performance by Random Sampling", author preprint, submitted September 2013, revised January 2015 and 2 October 2015, https://www.dei.unipd.it/~fisch/papers/improving_branch_and_cut_performance_by_random_sampling.pdf, Section 4.3 "Branch-and-cut Stability" (pp. 10-11, with footnote 1 on p. 11). Journal version: Mathematical Programming Computation 8(1):113-132, 2016, DOI 10.1007/s12532-015-0096-0 (not read). Working copy: `03/pdf/improving_branch_and_cut_performance_by_random_sampling.pdf`.

**Question**: In 2013-15 you test, with four co-authors, a "sampling" scheme on top of CPLEX 12.5: the root node is processed K times from different sampled optimal bases, the cuts and solutions of the K-1 sampling rounds are pooled, and a final branch-and-cut run starts from the enriched root. The scheme is meant to mimic an implementation that solves the K root nodes concurrently on several threads, but your proof-of-concept code runs them one after another, and you measure deterministic time (ticks). Some instances are solved outright during sampling. You must decide which ticks to charge to the sampling scheme in the table that compares it with default CPLEX. What do you do, and why? Name the options you reject and the reason for each.

**What they actually said or did**:
1. They state the accounting the idea would ideally call for: since the sampling phase stands for a parallel root, one would not report its deterministic time, only that of the final branch-and-cut (p. 10).
2. They reject it, because "this would give an unfair advantage to ksample": the method would be charged 0 ticks whenever it solves an instance during sampling (p. 11).
3. They also reject the obvious repair of removing those instances, which "would be unfair as well", because on those instances the sampling scheme is by design superior to default CPLEX (p. 11).
4. The rule adopted: the reported time is that of the final branch-and-cut run when the instance is not solved during sampling, and that of the sampling root node that solved the instance when it is (p. 11).
5. The idealisation is declared and then checked. A footnote says that even a parallel sampling phase would bring "unavoidable overhead", disregarded in this section and taken into account in Section 5, where a real parallel implementation is evaluated. The table is given for five seeds, with one instance (glass4) discarded for numerical reasons (p. 11).

**Why this one**: a small measurement judgement where both easy options are biased, one for the authors' method and one against it, and where the paper says so for each. Someone who knows how this group writes experimental sections will get the two rejections and the hybrid rule. A good researcher who does not will most likely charge all sampling ticks (which defeats the stated purpose of mimicking a parallel root) or charge none (which the paper calls unfair). It is one of about nine pieces of evidence for the fairness rule and not the main one.

**Where it appears in the notes**: `02-methodology.md`, §4.1, the bullet on RS16, its second sentence only (the "dilemma both ways" on p. 11), and the "RS16 pp.11" half of the reference in §0 row R4. The synthesis should leave that sentence out. Not sealed: the RS16 p. 13 rule on difficulty classes in the same bullet, and everything else the notes take from this paper (`01-publications.md` SW4 follow-ups; `03-process-evidence.md` PE-04, PE-25, PE-26, §10).

---

## H5

**Source**: M. Fischetti, "Feasibility Pump with Objective Cutoff: A Computational Study", manuscript of September 2026 (25 pp., submitted to Mathematical Programming Computation, unreviewed), `paper/manuscript.pdf` in https://github.com/mfischetti-arch/fp-objective-cutoff (tag `mpc-submission-1`; software DOI 10.5281/zenodo.22810777), Section 5 "Experimental setup", paragraph "Solution delivery is treatment-blind" (p. 12); and the same repository's `campaign_scip/README.md`, list "Design decisions worth knowing when reading the results". Working copies: `06/fpc/manuscript.pdf` and `03/repo/campaign_scip/README.md`.

**Question**: In 2026 you patch the feasibility pump inside SCIP for a factorial experiment on an objective cutoff. In your variants the pump no longer stops at its first integral point: it goes on under the cutoff. Some variants test each rounded point against the original constraints, and one arm has neither cutoff nor test. SCIP's stock pump passes a solution to the solver only once, after its loop ends, on the integral iterate that stopped it. An early campaign with this arrangement suggests that the cutoff makes no difference. Before you believe or report that, what do you check, what do you change in the code, and why? How do you show afterwards that the change did its job?

**What they actually said or did**:
1. He traced the result to the reporting path, not to the pump. With the continuation the loop does not stop, so a variant with no recovery would report a solution only when the clock ran out, while a variant with the test would report every integral iterate as it passed (manuscript p. 12).
2. He names the fault as a confound: this was "confounding the treatment with the bookkeeping" (p. 12).
3. The fix is placed before anything that differs between arms: every integral iterate is handed to the solver the moment it appears, at the top of the loop and before any variant-specific code runs, "in every cell alike" (p. 12). All twelve variants are one binary that differs only in parameter values (p. 12).
4. The wrong conclusion is written down in the package: the bare arm used to deliver only at the time limit, and "that alone produced the false conclusion that the cutoff is inert" (`campaign_scip/README.md`).
5. He reports a check that the arms are now level on this point: the median time to the first solution lies "between 3.99 and 4.61 seconds" for all ten variants of the grid on the subset where the pilot finds a solution (p. 12).

**Why this one**: a null result that turned out to be an artefact of the harness, with the mechanism, the fix and the check all stated. It is the 2026 counterpart of a device he used in 2013 (a callback in every arm, dummy if need be), so a reader who knows his experimental habits can reason to it. A good researcher who does not will answer in general terms (re-run, check for bugs, add seeds). It is one bullet in the notes; the study's main findings and its other safeguards are not sealed.

**Where it appears in the notes**: `03-process-evidence.md`, §5f, item PE-31, the bullet "Treatment-blind delivery" only. The `campaign_scip/README.md` list is also cited there for other bullets, which are not sealed. Not sealed: the rest of PE-31 (the `SCIPrecomputeSolObj` defect, the revalidation of the solution files, the invariant, the instrumented binary), PE-16 (one binary, pinned commits) and PE-15 (the 2013 dummy callback).
