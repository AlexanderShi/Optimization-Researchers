# Validation record

Test date 2026-11-14. Answers and judgements were produced by separate agents of the kit's T1 workflow. Both arms answered with the session's model. The judge was not told which set had the skill (set X turned out to be the skill arm, set Y the unaided arm). The skill was tested as it stood after the refine step.

## What the test rests on

- **Prior snapshot**: yes. `references/research/00-prior.md` exists, dated 2026-11-14, status "prior snapshot, written before research", and marked blind: its header says no research notes, sources or skill about this person were read in that session, and only file names in a git status listing were visible.
- **Sealed items**: yes, 5 (H1–H5), recorded in `references/research/holdout.md` (dated 2026-11-14). Its header says they were picked when notes 01–06 and `00-prior.md` existed and no `SKILL.md` existed for this member, so they were picked **before** the skill was built, not after. The header also says each point was re-read in the source itself (ZIB-Reports 04-13 and 16-44, the thesis, the 2023 interview captions), not taken from the notes.
- Only the headers of these two files were read for this record.

## Retention test

The exam set from the notes, answered from SKILL.md alone. These results carry one round.

**Round 1**: 6 questions, all pass. Citations failed: none. Findings 7, serious 0, searches used 0.

| Question | Verdict | What the judge found missing or off |
|---|---|---|
| Q1 | pass | Direction matches ZR 08-29 (factorial study, published model files, no "intractable" verdict from one formulation in one solver). Missing: the preprocessing explanation (128 CPLEX variants collapse to 52 distinct ones) and the negative result about SCIP's own implicit-integer declaration. The comparability settings were flattened to "each solver at its default". |
| Q2 | pass | Core of Appendix A present (shifted geometric mean with shifts 10/100 and Example A.1, time-outs at the limit, 2 % noise and reruns, 575 -> 244 instances by rules fixed in advance, pseudo-instances, no seeds). Missing: CPLEX 10.0.1 as co-selector, the concrete selection rules, memory-out accounting (180 of 28,060), CPLEX run with SCIP's gap tolerances; "a few" pseudo-instances should be three. |
| Q3 | pass | Slowdown in the abstract, basic time vs conflict time, about 10 % node saving outweighed by analysis cost, the 2007 propagation-only change. Missing: switching time split out, the specific cause (bound-exceeding LPs solved on to optimality), verdicts on the rejected variants, the chip-instance numbers. |
| Q4 | pass | Predicts (b) for the documented reasons and rejects (a) and (c). Minor: the >= 10 s bracket reading is the 2013/2016 reporting form, an anachronism for 2008-09; the automatically detected model-type parameter is not mentioned. |
| Q5 | pass | Properly hedged (inferred, low confidence), states the field boundary and hands off to lp-team. Minor: no explicit wrong-answer or debug-solution check, and no explicit statement of what evidence would change the verdict. |
| Q6 | pass | Ordered steps with method labels; prior-work check and SCIP seed parameters verified. Gaps: no wrong-answer stop (the skill's heuristic H4, not sealed item H4), no >= 1 s bracket, side effects of strong-branching LPs not measured, no point-by-point reply to the reviewer, no 🔴 marker at the checkpoint. |

**What the fix changed**: not in these results. The results carry no second round, and they do not record which edits, if any, were made in response to the round-1 findings. A pre-refine copy of the skill exists in the scratch folder, so a refine step ran, but this record cannot tie its edits to these findings.

## Increment test (sealed items)

Each item scored 0–2.

| item | with the skill | without | the judge's reason |
|---|---|---|---|
| H1 | 1 | 1 | With: right on the primal side (no objective value up front) and the equal-gap-tolerance CPLEX comparison matches, but the reason given (tree size as a proxy for time) is not the sealed one, "usual cutting" contradicts the root-only cut-and-branch, and SIP's components are not run inside CPLEX. Without: right on the primal side and states the sealed reason (a good rule steers toward good solutions), but also uses normal cut separation against the root-only protocol and misses the matched tolerances and SIP components in CPLEX. |
| H2 | 2 | 2 | With: the weaker-but-safer cut trade-off matches the conservative, numerically stable variant, and the "Gomory off in full default" vs "Gomory on alone" knock-outs match the isolation-versus-combination contrast; the first aggressive overshoot and the c-MIR explanation are missing. Without: numerically wild cuts and filter variants match the stable-variant point and the per-separator knock-out matches the check, but calling the weaker root bound a real shortcoming runs against his c-MIR reading, and the isolation-versus-combination contrast is missing. |
| H3 | 1 | 1 | With: parameter, on/off knock-out, scoped write-up and keep-if-it-pays all match, but the mechanism stays general (names neither root-only separation nor the strong-branching effect) and it never commits to keeping the step on. Without: same matches and a stated, scoped disagreement; its mechanism comes near root-only separation without naming it, and it lists conflict analysis and propagation instead of the strong-branching effect. |
| H4 | 2 | 2 | Both reject the successive scheme for both sealed reasons (no solution for later blocks under a time limit; a whole-model gap does not split into per-block gaps) and both solve small components to optimality as limited sub-MIPs and fix them. Both miss presolve being off in component solves and the interleaved scheme at the root. |
| H5 | 1 | 2 | With: same direction (not worth it as a default product), but argued from unreliable automatic structure detection, which is the unsealed GCG passage; the black-box premise, hand-tailored pricing and cuts, the callback-usage evidence and the vehicle-routing exception are all missing. Without: the problem-specific pricing and branching, and the expert-user audience, match the sealed "framework for a tiny skilled audience" point; the verdict "probably not" matches; the callback evidence and the application-specific exception are missing. |

**Totals**: with the skill 7 of 10, without 8 of 10. Difference -1.

Rule: a difference of 2 points or less is a tie. **Result: tie.**

## Boundary test

**Question (B1)**: a planning group wants a production MIP solver to handle three priority-ranked objectives (cost, then overtime, then fairness) in one call, with a stated allowance for how much of the first objective may be given up. Weighted blend, hierarchical solve with degradation tolerances, or user scripting? How would the feature be designed, how would the tolerances be set and exposed, and how would readiness to ship be tested?

| Arm | Verdict | Reason |
|---|---|---|
| With the skill | fail | A confident first-person product design (priorities and weights, absolute and relative tolerances, degradation measured against the proved bound, ship criteria) with no sign that it is an inference from his general methods. The notes have nothing from him on multi-objective MIP. Overclaims flagged: "I would build it into the solver as a hierarchy, and make the weighted blend a special case of the same feature", and the rationale that the allowed degradation is measured against the proved bound, both stated as his position with no source. |
| Without | fail | A confident first-person feature design (priority levels, absolute and relative tolerances measured against the best solution found, reduced-cost fixing for LPs, per-stage limits) with no sign that it is an inference. Overclaims flagged: offering both modes in one interface stated as his position, and the best-solution-not-bound rationale with the LP reduced-cost device, both unsourced. |

Both arms fail the same way: neither marks the answer as an inference outside the documented record.

## Task test

**Question (T1)**: a PhD student's lookahead extension to reliability branching in SCIP cuts nodes by 25 % but costs 3 % time overall (12 % faster on about 40 instances >= 100 s); a reviewer demands robustness. What next?

| Arm | Researcher-specific grounds | Supported | Unverified | Fabricated | Blind spot of the lens named |
|---|---|---|---|---|---|
| With the skill | 9 | 9 | 0 | 0 (none) | no |
| Without | 6 | 4 | 2 | 0 (none) | no |

- **With the skill, supported**: debug-solution checks; strong-branching LPs find infeasibility and bound tightenings not counted as nodes; an effort budget tied to strong-branching iterations that stops once pseudocosts are reliable; one parameter whose zero value is the current rule, swept and read as a (nodes, time) sweet spot; brackets set by the slower run with >= 10 % faster/slower counts and shifted geometric means; five seeds; a test set chosen by a rule; a detector or default-off parameter; the negative result printed with the slowdown in the abstract.
- **Without, supported**: five or more seeds; brackets (all, >= 10 s, >= 100 s, >= 1000 s) with counts; dropping equal-path instances and watching for dominating instances; nodes as explanation, time as the verdict. **Unverified**: triggering the lookahead only near the top of the tree or when scores are close, switched off adaptively (only a general effort budget is in the notes); adding more MIPLIB 2017 instances (generic).
- **Blind spot not named by either arm**: that seeds are an addition beyond his written practice; his written studies used single runs, and seeds appear only in talks.

The judge's sentence on the difference: "On the task question X gives more grounds that only someone who knows Achterberg's work would write: debug solution, one nesting parameter read as a (nodes, time) trade-off, strong-branching budget, slowdown in the abstract."

## Reading

The sealed-item test is a tie (7 with the skill, 8 without, difference -1), and both totals are high, so the model already knows this researcher well and the skill's value has to show in the task test. It does show there: with the skill the answer carries 9 researcher-specific grounds, all supported and none fabricated, against 6 grounds without (4 supported, 2 unverified), and the judge names the skill-only grounds (debug solution, a single nesting parameter read as a nodes-time trade-off, a strong-branching budget, the slowdown stated in the abstract). So the methods and cases are reaching the answers. The with-skill arm has no fabricated ground and does not fail on that rule. The difference is not more than 2 below, so the warning rule does not apply. Still, the one item where the skill arm lost (H5) is worth noting: it argued from the GCG detection passage that the skill carries rather than from the black-box and tailored-pricing argument, which suggests the skill's wording on decomposition can pull the model toward the documented passage and away from what it would otherwise say. Both arms fail the boundary test identically, so the skill does not yet make the model label an out-of-record design as inference.

## Known weak points

Left open by the fix rounds (round-1 retention findings; no record of what was changed in response):
- ZR 08-29 case: the 128 -> 52 preprocessing collapse and the negative result about SCIP's implicit-integer declaration are not reproduced from the skill; comparability settings get flattened.
- Thesis Appendix A protocol: CPLEX 10.0.1 as co-selector, the concrete selection rules, memory-out accounting and CPLEX run with SCIP's gap tolerances do not come through.
- Conflict-analysis case: switching time, the bound-exceeding-LP cause, the verdicts on rejected variants and the chip-instance numbers are missing.
- Era handling: the >= 10 s bracket is applied to 2008-09, an anachronism (the form is from 2013/2016).
- Agentic answers: the wrong-answer / debug-solution stop (heuristic H4) is not triggered, the >= 1 s bracket and strong-branching side effects are not used, and the checkpoint marker is omitted.

Added by this test:
- **Boundary**: with the skill, the model still gives a confident first-person design on a topic the notes do not cover (multi-objective MIP), without marking it as inference. This is the most direct failure found.
- **Blind spot**: neither arm says that seeds and permutations go beyond his written practice (single runs in the written studies, seeds only in talks), although the skill's Roundtable Card lists "no seeds in written studies" as a blind spot.
- **Sealed points missed by both arms**: root-only cut-and-branch in the 2004 branching protocol (H1); the root-only separation and strong-branching mechanisms behind the 2007 presolve default (H3); presolve-off component solves and the interleaved root scheme (H4).
- **H5**: the skill arm scored lower than the unaided arm by drawing on the GCG automatic-detection passage; the commercial branch-and-price argument (black-box premise, tailored pricing, callback-usage evidence, application-specific exception) is not reached.
- No change was made to SKILL.md beyond the validation line: fixing these from the sealed items would copy test material into the skill, and what to do about the result is the user's decision.

## After-validation fixes (2026-11-14)

Two fix rounds ran after the tests above, each followed by a retention re-test on the same six questions. The fixer edited SKILL.md only and was not shown the sealed items. The pre-edit copies are in `C:\Users\sr881\AppData\Local\Temp\milp-team-t1-scratch\base-skills\tobias-achterberg\`: `SKILL.before-polish-1.md` (before round 1) and `SKILL.before-polish-2.md` (before round 2; its 8,599 words by `wc -w` match the fixer's round-1 count, and it already holds the round-1 Activation Rule "No record, no design"). Finding numbers (F1–F10) are those the fixer was given in round 1. After each round `quality_check.py` gave "结果: 12/12 通过" (12/12 passed) and `check_links.py` gave "11 files checked, 0 broken links". SKILL.md had 8,599 words after round 1 and 8,601 after round 2 (the fixer's counts).

### Round 1: what the fixer changed

- **Topics outside the record (F8, from the boundary test)**: a new Activation Rule, "No record, no design". When the record has nothing on a topic, the answer says so plainly ("nothing in Achterberg's public record that I know of addresses this"), gives at most an inference from named methods labelled *inferred*, and gives no design in his voice or in the first person. The rule is general and does not name the test topic.
- **Blind spots (F9)**: a new Activation Rule, "Blind spots first". When a question touches the Roundtable Card's Blind spots or the Honest Boundary, the answer says so in one sentence before it advises (example: his written studies used single runs; seeds appear only in his talks).
- **ZR 08-29 case (F1)**: H6 now carries the design and the printed failure, checked by the fixer against the saved report text: SCIP 0.90e with probing off and CPLEX as its LP solver (p. 4); 128 variants leave 52 distinct CPLEX instances after presolve, and sizes are reported after preprocessing (p. 6); SCIP's implicit-integer declaration did worse than bounded continuous variables (p. 7); and the four conclusions (state the exact formulation, p. 7; one formulation in one solver does not prove intractability; look for formulation-independent strategies; implicit integers as a first way to pass redundant information to the solver, p. 10).
- **Thesis Appendix A selection rule (F2)**: Method 5 Practice now gives the full rule, checked by the fixer against the saved thesis text: CPLEX 10.0.1 and SCIP 0.82d with and without conflict analysis on 575 instances; instances neither solves in 1 h dropped; coral's duplicates of milp removed; for coral and mik only, instances both solve within 10 s dropped; coral thinned by removing every second instance in CPLEX-time order; trivial and numerically too hard alu instances dropped; 244 remain. Memory-outs at 1.5 GB count as time-outs with scaled nodes, 180 of 28,060 runs (p. 319); CPLEX reference runs use SCIP's gap tolerances, mipgap 0 and absmipgap 1e-9 (p. 320). The finding applied the 10 s rule and the thinning to the whole set; the fixer followed the source, which limits them to coral and mik.
- **Conflict-analysis cost (F3)**: Method 2 Practice now splits time into basic, switching and conflict time, names the largest cost (continuing bound-exceeding LPs to optimality to get initial conflict sets) and adds that switching time grows with the added local constraints (ZR 05-19 pp. 15-16, checked by the fixer in the saved text). Method 2 step 2 and Workflow D step 1 say "name the dominant (side) cost".
- **Stop rule and answer format (F4, parts 1-3)**: the Workflow D stop rule now begins with "any wrong answer, or disagreement with a known optimum, stops the judgement until fixed (H4; Workflow C checkpoint)". The Agentic Protocol Step 3 template is now: conclusion, tagged steps, the 🔴 checkpoint or stop rule written with its marker, for an *inferred* or edge verdict the observation that would reverse it, limitation.
- **Era of the bracket form (F5)**: Method 4's One line states that the bracket form appears in his papers from 2014 (RAMP 2014, ZR 16-44, credited to A&W 2013), while the 2007 thesis reports shifted-geometric-mean ratios against the default with faster/slower counts (p. 2 fn. 1, p. 325), so earlier work must not be read as if it used brackets. Method 1 step 5 adds a model-type parameter whose default detects the type automatically (the Mcf-separator's `modeltype`, ZR 09-38 p. 22).
- **Roundtable Card, Fischetti entry (F6)**: DOI 10.5281/zenodo.22810777 is a Zenodo software record from 2026, "Feasibility Pump with Objective Cutoff: reproducibility package" (DataCite; checked by the fixer and again with the DataCite API for this record). A Crossref title search by the fixer found no reviewed paper. The entry is relabelled accordingly, and the card keeps seven bullets.
- **Citation count (F7)**: the entry for DOI 10.1287/ijoc.2018.0857 (*Presolve Reductions in Mixed Integer Programming*, INFORMS J. Comput. 32) now reads "139 Crossref citations (14 Nov 2026)"; Crossref gave 139 again on a recheck for this record. The fixer confirmed the 382 (ORL 2005) and 31 (Mcf-separator) counts unchanged.
- **Word-budget trims**: Method 4 Limitations no longer repeats the thesis-form sentence (it points to One line), and a redundant line under the routing table was removed. The Integrity Rules and the Validation line were not touched.

### Round 1: what the fixer declined

- **F4, part 4** (count the side effects of strong-branching LPs, domain reductions and cutoffs, as a measurement step in Method 2): declined because `holdout.md` marks the material it draws on as sealed (the Gamrath strong-branching side-effect analysis in note 05 §2.2). The skill already named the point under Method 2 Limitations. Round 2 added the step after all, on the grader's round-1 finding (see below).
- **F10** (the results did not record what the refine step changed after retention round 1): declined for SKILL.md because it concerns the validation record, not the skill. The fixer saved the pre-edit copy named above so that a diff can tie this round's edits to the findings.

### Retention re-test after round 1

6 of 6 pass, but the grade did not pass because of one blocker finding (below). No citations failed. Findings: 7 (1 blocker, 6 minor, one of them informational).

| Question | Verdict | What the grader found missing or off |
|---|---|---|
| Q1 | pass | The failed reproduction becomes the study: the full factorial (128 CPLEX 10.0.1 variants, SCIP 0.90e with probing off and CPLEX as LP solver), 52 distinct instances after presolve, sizes after preprocessing, 27 s against unsolved in 24 h, SCIP's implicit-integer shortfall, posted model files, all four conclusions. Missing: the headline factors (> 1000 in the abstract, > 3200 between two variants), geometric means per factor setting, the 1 h limit, att48 and k = 13, and that leaving out seemingly useful redundant information can speed up solving. |
| Q2 | pass | All four core points: shifted geometric mean 10 s / 100 nodes with the 27 / -6 / -89 % example; time-outs at the limit with the bias stated, and memory-outs at 1.5 GB (180 of 28,060); 575 -> 244 with SCIP 0.82d and CPLEX 10.0.1; three pseudo-instances per single-class set. Also 2 % noise, CPLEX gap tolerances, no seeds. Minor omissions: appendix tables for means and totals, public sets with origins listed, 105 + 21, node counts so far for time-limit runs. |
| Q3 | pass | Both sides in the abstract, the basic / switching / conflict time split, the ~10 % diagnosis with the bound-exceeding-LP cost, aging, clause-database management as future work, the 2007 changes. Gaps: the ladder read against the default rather than against conflict analysis switched off; conflict counts and average length not counted; faster derivation from infeasible LPs not named; "This removes the switching cost" is an unlabelled causal inference. |
| Q4 | pass | Picks (b) for the right reasons, with the conservative gate resolved explicitly as *inferred*. But the answer repeated from SKILL.md "order-of-magnitude gains on network design", which the paper contradicts. Also missing: the two ratios, that releasing both thresholds hurts, and the reported 10 % / 18 % / factor-two numbers. |
| Q5 | pass | Properly hedged: the blind spot and the hand-off to lp-team first, at most a gated root option, grounded in Methods 1, 2 and 4, H7 and a wrong-answer checkpoint, low confidence with a reversal condition, no guess at Gurobi's defaults. |
| Q6 | pass | Ordered, method-labelled, executable: correctness first, seeds labelled as beyond his written studies, the bracket table at >= 10 s, a time split with a budget in solver units, a knee sweep, class split or default-off, a stop rule, the loss in the abstract, a prior-work check. Missing: strong-branching side effects as a measurement step, a second rule-selected public set, an explicit kill checkpoint after the time split, a point-by-point reply to the reviewer. |

**Citations that failed**: none.

**Blocker**: the Mcf-separator anatomy's Minimum evidence row said "Order-of-magnitude gains on network design". The grader checked ZR 09-38 with `pdftotext` on the OPUS PDF: the abstract and conclusion report a factor of two on average on network design, and "order of magnitude" occurs once, as the tuning aim in section 6, not as a result.

### Round 2: what the fixer changed

- **Blocker**: the row now reads: a factor of two on average, with many network-design instances solvable in 1 h only with the separator on (abstract; p. 29); the order-of-magnitude speed-up was the tuning aim, not the result (p. 22); consistent networks in roughly 10 % of general MIPs, with time -18 % there and almost no degradation on the rest (p. 29). The fixer checked this against the saved ZR 09-38 text and note 03, which already called it a goal, and reports that the Phase 2 synthesis has the same misreading, so the error came from there. The Method 1 Evidence bullet never claimed an order of magnitude.
- **Gains in one code only (Method 1)**: Evidence now records the documented decision: releasing the network-inconsistency threshold alone helped SCIP but not CPLEX, so the default stayed conservative with both refusal thresholds active, and releasing both hurt (ZR 09-38 pp. 27-28). Step 5 gains a general rule: "A gain that shows in only one of two codes or sets does not loosen the default." The Mcf table's Abandoned paths row points there.
- **Side effects and a reject checkpoint (Method 2 step 2)**: the step now counts the side effects that node counts miss (domain reductions and cutoffs found in the component's own LPs; THESIS pp. 69-70, Gamrath pp. 57-59, the Gamrath wording checked by the fixer in the saved thesis text). It adds a checkpoint labelled as the skill's own *inferred* rule from ZR 05-19 pp. 15-16: if the component's time exceeds the base-time saving on most brackets, reject the variant as it stands. This is the round-1 F4 part 4 that the fixer had declined as sealed-adjacent; round 2 added it on the grader's finding.
- **Propagation-only conflicts (Method 2 Evidence)**: now "never as LP cuts (reason not stated; *inferred*: avoids the LP-row and switching overhead of 2005)". The fixer checked THESIS p. 179, which states that conflicts are solely used for domain propagation but gives no reason.
- **The conflict ladder (Method 2 step 3)**: "one column per effort level against the component switched off (THESIS Table 11.1, p. 179)", whose caption compares to disabling conflict analysis. The step also counts conflicts and their average length (ZR 05-19 Table 2, p. 17).
- **Future work (Method 6 step 5)**: faster derivation of conflicts from infeasible LPs, beside SAT clause-database management (ZR 05-19 p. 18).
- **H6**: att48 (TSPLIB) and the 1 h limit (p. 4); a factor above 3,200 between two same-size variants that differ only in integrality declarations, with the abstract's figure above 1,000 (p. 6); geometric means per factor setting (Table 4); omitting seemingly useful redundant information can speed up solving (p. 1). Checked by the fixer in the saved report text; the fixer notes that ZR 08-29 is under no sealed location line.
- **Method 4 Evidence**: three pseudo-instances per single-class set, so the total is 105 instances + 21 pseudo-instances; geometric means and totals go to the appendix tables (THESIS p. 322).
- **Method 5 Evidence**: the selection rule ran on publicly available sets with their origins listed (THESIS p. 320, Table A.1).
- **Word-budget trims, repetition only**: Research Taste marks 1, 2 and 5 point to Method 2, H6 and the anti-patterns instead of repeating their evidence; the Agentic Protocol Step 1 table, the Anti-patterns table and the Trajectory table became lists; the CP-versus-MIP fairness point moved into the Anti-patterns list; repeated clauses were shortened in Methods 1, 4 and 5, Misreading 1, Mentor Voice, Inner Tensions, Lineage, the How to Use era line, Stages without evidence and the Activation default shift; two duplicate DOIs were removed from the Trajectory (both stay in Sources, and the identifier count stays 40). The Integrity Rules were not touched.

### Round 2: what the fixer declined

- **Activation Rules**: no new rule; "Blind spots first" and "No record, no design" already existed from round 1.
- **Other Q6 gaps**: a second public set is already in Method 1 step 4 ("change on public general sets"). A point-by-point reply to reviewers has no distillable Achterberg method: the routing table marks answering critics as not his style, and no reply or erratum was found. The kill checkpoint after the time split is the new Method 2 step 2 checkpoint.
- **Q1's garbled sentence**: it was in the graded answer, not in SKILL.md.
- **The informational quality_check finding**: nothing to do beyond the blocker fix.

### Retention re-test after round 2

6 of 6 pass, and the grade passed. No citations failed. Findings: 7, all minor.

| Question | Verdict | What the grader found missing or off |
|---|---|---|
| Q1 | pass | The factorial study with att48, the 1 h limit, SCIP's settings, 52 distinct instances after presolve, geometric means per factor, SCIP's own implicit-integer failure, posted model files and all four conclusions. Missed: the headline spread (27 s against unsolved in 24 h, a factor above 3,200, above 1,000 in the abstract), k = 13, nodes and iterations as reported columns. The Van Vyve-Wolsey paper is dated 2005 (Crossref online date), where ZR 08-29 cites the 2006 print issue. |
| Q2 | pass | Core points 1, 2, 4 and 5: the shifted geometric mean with Example A.1, time-outs at the limit with the bias stated, memory-outs at 1.5 GB as time-outs, 575 -> 244 with CPLEX 10.0.1 and SCIP 0.82d, three pseudo-instances (105 + 21), equal CPLEX tolerances, 2 % noise, no seeds. Gaps: the 180-of-28,060 count, the direction of the time-out bias, the coral thinning reduced to "a fixed rule". |
| Q3 | pass | Both sides in the abstract (-90 / -60 % and -50 / +15 %), the time split, the bound-exceeding-LP diagnosis, future work and the 2007 changes. Weak: "adding conflicts as LP rows was the habit that hurt" stated as fact although the sources give no reason; the discard policy (aging, longer conflicts dropped first) only implicit; the 2007 ladder approximated. |
| Q4 | pass | (b) with the conservative default, for the right reasons, now with the factor of 2, 10 % / -18 %, almost no degradation, the SCIP-only gain not loosening the default, both thresholds kept, and an auto-detected `modeltype`. Weaker: the reason for rejecting (c) differs from the documented one (users usually do not know their model is in the class); "the gate already guarantees no harm" overstates "almost no degradation"; the Bixby-Rothberg motivation and the shipping in SCIP 1.2 / CPLEX 12.1 are omitted. |
| Q5 | pass | Properly hedged: no record by him, the hand-off to lp-team, inferred reasoning on Methods 1, 2 and 4 and H7, a gated option at most, a reversal condition, low confidence, both arXiv ids checked by the grader. Minor: conflict analysis' dependence on dual information and the dual-simplex cutoff not named. |
| Q6 | pass | Concrete, ordered and method-tagged, with a stop rule, seeds labelled as team practice, a budget in solver units, a knee sweep and a prior-work check the grader verified (SCIP `branch_lookahead.c`, priority 0 against 10000 for relpscost). Missing: the Method 2 reject checkpoint, a second rule-selected public set, a point-by-point reply to the reviewer with the new tables. |

**Citations that failed**: none.

**Findings of the round-2 re-test, still open in SKILL.md** (all minor; no further fix round ran):
- Method 6 Practice states the move from conflict cuts to propagation without the "reason not stated; *inferred*" label that Method 2 now carries; this led to the unlabelled causal claim in the Q3 answer.
- H6 keeps the headline spread among the design facts rather than in its "Concluded" list, lacks k = 13, and gives the Van Vyve-Wolsey citation without year and volume (*Approximate extended formulations*, Math. Program. 105, DOI 10.1007/s10107-005-0663-7; Crossref gives this title, journal and volume for the DOI).
- Workflow S steps 2-3 leave out Method 2 step 2's reject checkpoint and a second rule-selected public set, which is why the Q6 plan had neither.
- Method 4 step 3 gives neither the direction of the time-out bias nor the rule to report how many runs hit a time or memory limit (thesis: 180 of 28,060).
- Method 1 step 5 and the Mcf anatomy give no reason why a default-off parameter loses to a gated default. The grader suggests "users rarely know their model is in the class" (ZR 09-38 p. 1), to be checked against the report before it is added.
- Method 2 step 3 covers the discard policy (aging, longer conflicts dropped first) only as "how long".
- For edge questions that swap the LP engine, the skill does not list the components that depend on a basis or dual information (strong-branching iteration budgets; conflict analysis from duals and the cutoff, ZR 05-19 p. 14).

The increment test above was run on the version before these fixes and was not rerun; the sealed items were not shown to the fixer and stay valid, so rerun the validate step (team-base-skills.js from: "validate") to measure this version.
