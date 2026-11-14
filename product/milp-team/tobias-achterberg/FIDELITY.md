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
