# Validation record

Test date 2026-11-14. Answers and judgements were produced by separate agents of the kit's T1 workflow. Both arms answered with the session's model. The judge was not told which set had the skill (set X turned out to be the skill arm, set Y the unaided arm). The skill was tested as it stood after the refine step.

## What the test rests on

- **Prior snapshot**: yes. `references/research/00-prior.md` exists, dated 2026-11-14, status "prior snapshot, written before research", and marked `blind: yes`. Its header says the file "records unaided belief" and may not be cited. The header does not list what the writing session could see beyond that.
- **Sealed items**: yes, 5 (H1-H5), in `references/research/holdout.md` (dated 2026-11-14). Its header says that no `SKILL.md` existed for this member when they were picked, so they were picked **before** the skill was built, not after. Notes 01-06 and `00-prior.md` had been read, and nothing in the items is stated in `00-prior.md`. Each point was taken from the source itself (the author preprint or the 2026 manuscript), not from the notes. They cover 2004, 2009, 2014, 2013-15 and 2026 and five topics. The header adds an authorship caveat: H1-H4 are co-authored, so each decision is the team's; H5 is the sole-author 2026 manuscript, which is unreviewed and was written with declared AI assistance.
- Only the headers of these two files were read for this record. (The read tool returned the first H1 item along with the holdout header. Nothing from it is used here beyond what the judge's reasons below already say.)

## Retention test

The exam set from the notes was answered from SKILL.md alone. These results hold one round.

**Round 1**: 6 questions: 5 pass, 1 partial. Citations failed: none. Findings 7, serious 0, searches used 0.

| Question | Verdict | What the judge found missing or off |
|---|---|---|
| Q1 | pass | Has every core element: a redundant cut that is removed, so the gain comes from perturbed initial conditions; a placebo arm (redundant cut, permutation or seed only) with only gains beyond it counted; the baseline's spread over seeds; the cost tie; the same machinery in every arm; bet-and-run with the 2014 paper cited correctly. Small gaps: no "chaotic amplifier / pinball" framing; the quick selection criterion (positive correlation with the best run, H6) is not stated, and neither is the single-thread, unloaded-machine condition. |
| Q2 | pass | Direction matches: soft fixing; one Hamming-distance constraint around black-box Cplex 7.0; the complementary branch for exactness; the move from the application to general 0-1 MIP; k fixed at 20; a practitioner baseline; traces before tables; joint credit with Lodi. Missing: the Aussois 2002 diagnosis of hard fixing (wrong early fixings are hard to detect; feasible solutions appear only deep in the tree), the 833 -> 809 outcome, the 29-instance 5-hour testbed, and the conceded limits. "RINS beat it on its own instances" is stated as fact, where SKILL.md hedges it as resting on abstracts and citation contexts. |
| Q3 | partial | Right: blame the loop, not the cuts; in-out stabilisation halfway to the LP optimum, with its lineage credited; root only, Kelley in the tree; no Pareto selection, bundle or in-tree stabilisation; the first stabiliser kept. Weak on fat versus slim: the answer admits that SKILL.md does not say which model wins, then guesses a trade-off that the documented gs250a-1 evidence contradicts (slim in-out 0.04 s with 4 cuts against 0.19 s fat). The documented rule is missing (slim wins clearly for separable quadratic costs, fat is better for linear costs). Also missing: why the tree keeps Kelley, the stabilising point initialised at all ones, the 2-epsilon perturbation, and the same separator in every compared loop. |
| Q4 | pass | Picks (b) for the right reasons (adopt the critic's fix as the baseline, swap test, practitioner baseline, the rounding isolated as one module, 10 seeds with a success rule) and avoids the era error. Minor: it repeats an unsupported phrase from SKILL.md heuristic H9 by calling "Boosting the feasibility pump" a paper with "the critics' group". The gap figures (77.2% -> 57.6%, 52.4% -> 35.5%) are absent, and they are not in SKILL.md either. |
| Q5 | pass | Properly hedged: only experiment-design rules transfer, and there is no Fischetti evidence on quantum hardware. Each point is tied to a named method. Small gaps: no explicit status label (lead or computational conjecture, H7); no fair stochastic control (k short randomised MILP runs, bet-and-run at an equal budget); "each could produce 100x alone" slightly overstates. |
| Q6 | pass | Concrete and ordered, with a method label on each step: the dropped instances restored, with exclusions fixed in advance; a disjoint tuning set and a swap-test checkpoint; SCIP default with ALNS as the baseline; the primal integral; 5-10 seeds plus a placebo arm and a paired test; the restriction reported as scope; a stop rule. Weaker: only one checkpoint is marked, and with no 🔴 marker; there are no traces before the table (H8); losses and the instances where the method does not pay are not explicitly printed. |

**What the fix changed**: the results do not record it. They hold one round and do not say which edits answered which finding. A pre-refine copy (`SKILL.before-refine.md`, 18:31) sits in the scratch folder, saved after the exam file (18:24) and the round-1 grading folder (18:27). So round 1 most likely graded the pre-refine skill. That is inferred from file times, not recorded. A diff of that copy against the tested SKILL.md, read for this record, shows that the refine:
- added Workflow S (stuck-project triage) and its routing row, a routing row for "no feasible solution", and an "outside the lens" row that hands numerics, exactness, presolve, conflict analysis and column generation to other members;
- changed Step 3 to one workflow per answer, stopping at its 🔴 checkpoint;
- tightened the activation rules (the roundtable answer format; co-authors named; the 2026 apparatus not credited to 2002-2019 work);
- added the 58-instance, single-thread detail and ERR14 p.10 to Method 3;
- removed the Signature Work Anatomy tables for *Exploiting Erraticism in Search* and for local branching, and shortened the trajectory table and several other passages.

Seen in that diff: the Q3 fat-versus-slim rule was not added, the gs250a-1 numbers were cut from the Benders anatomy table (only "gs250a-1 (M2)" remains), and the "critics' group" phrase in H9 is unchanged. Whether the Q2 local-branching details would now come through is not tested: the table that held part of them was removed.

## Increment test (sealed items)

Each item is scored 0-2.

| item | with the skill | without | the judge's reason |
|---|---|---|---|
| H1 | 2 | 0 | With: "Add the CB cuts as local cuts ... let the solver itself drop them" is the sealed work-around, and "a private pool ... still cannot remove a cut once it has been added" matches the sealed obstacle. It rejects separating far less often, although the paper also limited separation, and the cost it states (repeated separation) is not the sealed one (no full control, memory overhead). Without: "keep my own pool outside the solver and restart" goes in a different direction, and the paper says an own pool is not the issue. Its answer to the reader ("useless fractional points") is close to the paper's "wild fractional points" but does not save the main decision. |
| H2 | 2 | 1 | With: it looks inside and finds that unit weights count rows present in every infeasible subsystem, which is the sealed diagnosis (null rows of T, static rows that are always active). It changes only the weights and reports the unit-weight first version with the diagnosis, but does not say the weight becomes 0. Without: same direction (look inside, change the weights, report the first version openly), but the diagnosis and fix are scaling (each weight tied to its row norm), not the sealed null rows with weight 0. It only touches the sealed mechanism by mentioning "bound rows". |
| H3 | 1 | 1 | With: the order is right (offline runs of the executable through files first, a lean CFT reimplementation later). But it would leave the black-box results out of the paper, where the sealed record keeps both tables, and it applies the symmetry fixing, where the authors chose not to. Without: the order roughly matches (the binary only a "preliminary check"), but "I fix it" on symmetry contradicts the sealed decision. |
| H4 | 2 | 0 | With: it rejects charging nothing as unfair and rejects removing the instances solved during sampling because that favours the scheme (the sealed reasons), charges the solving round when sampling solves the instance, and labels the parallel idealisation as ignoring overhead. Where sampling does not solve the instance it also charges the slowest round, which is more than the sealed final-run-only rule. Without: it charges all K-1 sampling rounds plus the final run and rejects both the final-run-only and the parallel-maximum accounting, which is the opposite of the sealed parallel-mimicking rule. It shares only the rejection of dropping or zero-charging the instances solved during sampling. |
| H5 | 2 | 1 | With: the null result "measured the delivery code, not the cutoff". It submits each integral point when found through "one submission routine shared by all arms, the stock-behaviour arm included", which is the sealed "in every cell alike" fix. The after-check uses counters and log matching, not the sealed equal-time-to-first-solution check. Without: the diagnosis (points found in the loop never reach SCIP) and the fix (submit each point when it appears) match, but keeping the no-cutoff, no-test arm "exactly as the stock behaviour" keeps the confound that the sealed fix removes. |

**Totals**: with the skill 9 of 10, without 3 of 10. Difference +6.

Rule: a difference of 2 points or less is a tie. **Result: not a tie; the skill arm is 6 points higher.**

## Boundary test

**Question (B1)**: three open MIPLIB 2017 instances were closed with a long floating-point SCIP run (default tolerances, eight threads), and a referee asks for proof that the optimal values are not round-off artefacts. The options: re-solve with an exact rational MIP solver and have a separate checker such as VIPR verify a certificate; compute safe dual bounds a posteriori by directed rounding on the LP duals of the final tree; or re-run with tightened tolerances and re-check the incumbents independently. Which for a paper whose contribution is the computational claim, what does each guarantee, and how is the residual risk reported?

| Arm | Verdict | Reason |
|---|---|---|
| With the skill | pass | It opens with "Exactness and floating-point certification are outside this territory" and limits the lens to the adjacent documented practice: re-checking incumbents with a fresh solver, and stopping when a primal value is on the wrong side of the bound. It keeps primal checks apart from dual certification and does not invent a Fischetti position on certificates. |
| Without | fail | A confident first-person ladder in Fischetti's voice ("I would treat the three options as a ladder and go as high as the instances allow", "I would try it first"). Nothing tells the reader that the notes hold no Fischetti statement on exact solving or certificates, or that this is extrapolation. Overclaim flagged: the ladder sentence is a position on exact certification, stated in his voice, where the notes document none. |

## Task test

**Question (T1)**: a new SCIP sub-MIP improvement heuristic (needs an incumbent, fixes binaries) lowers shifted geometric mean time by 6% on 40 MIPLIB 2017 instances with one seed. It was measured after dropping 9 instances that default SCIP solves in under 10 s, and its parameters were tuned on the same 40 instances. The reviewer: within variability, wrong baseline, binaries only, needs an incumbent. Three more seeds give +6%, -2%, +9%, +1%. What next, in what order, with which checkpoints, and when to stop or change the claim?

| Arm | Researcher-specific grounds | Supported | Unverified | Fabricated | Blind spot of the lens named |
|---|---|---|---|---|---|
| With the skill | 10 | 8 | 2 | 0 (none) | no |
| Without | 6 | 6 | 0 | 0 (none) | no |

- **With the skill, supported**: check which neighbourhoods SCIP already runs, with local branching and proximity search inside ALNS ("do not duplicate"); removing instances that are easy for the competitor is not fair; the swap test; no tuning on the test set, or conservative untuned settings; a placebo arm with the same hook doing nothing (the dummy callback); median over seeds per instance, then a paired test; the primal integral; stop with a stated lesson or an "inconclusive" claim. **Unverified**: the specific second baseline (aggressive heuristic emphasis, or ALNS with the same budget); conceding the restriction in the paper's first pages. The answer names the method's limits, not a limit of the lens.
- **Without, supported**: tune on a separate training set; restore the easy instances or class them in advance; five or more seeds; the primal integral for an improvement heuristic; compare against the neighbourhoods SCIP already has, local branching inside ALNS included; needing an incumbent "as local branching does". Pooling over instance-seed pairs differs from his 2026 rule (median per instance, with the instance as the unit of inference), but the judge counts it as generic advice, not a Fischetti ground. No placebo arm, no swap test, no stop rule tied to the lessons-learned practice. No lens limit named.

The judge's sentence on the difference: "On T1 X carries more Fischetti-specific grounds (placebo or dummy callback, swap test, per-instance median, lessons-learned stop), and only X passes the boundary question."

## Reading

On the sealed items the skill arm is 6 points higher (9 against 3 of 10). That is far more than the tie margin of 2, so by the rule the skill adds what the model lacked. The gain comes from documented decisions that a capable but uninformed answer gets wrong or reverses. On H1 the skill arm declares the cuts local where the unaided arm reaches for its own pool and a restart. On H2 it finds the always-active static rows where the unaided arm rescales. On H4 it gives the hybrid charging rule and both rejections where the unaided arm charges every round. On H5 it delivers points alike in every arm where the unaided arm keeps the stock-behaviour confound. These are side decisions that the sealed points say are not in the notes' summary, so the skill seems to carry his way of deciding, not just the facts it states. The task test shows a visible difference too: 10 researcher-specific grounds with the skill (8 supported, 2 unverified, none fabricated) against 6 without (all supported). The skill-only grounds are the ones the judge names: the placebo or dummy callback, the swap test, the per-instance median and the lessons-learned stop. So the methods and cases reach the answers. The with-skill arm has no fabricated ground and does not fail on that rule. Only the skill arm passes the boundary test: the "outside the lens" routing seems to work there, where the unaided arm speaks confidently in his voice. Both arms miss the H3 decision to leave the symmetry alone. One test run per arm on one model does not measure the spread of these scores.

## Known weak points

Left open by the fix rounds (round-1 retention findings; the results do not say what was changed in response, and the diff above shows most of them unaddressed):
- **Benders case (Q3, the one partial)**: the skill does not say which of the fat and slim models wins in which cost regime (slim for separable quadratic costs, fat for linear costs), and the gs250a-1 timing that would correct a guess was cut from the anatomy table in the refine. Also absent: why the tree keeps Kelley, the all-ones starting point, the 2-epsilon perturbation, and the same separator in all compared loops.
- **Local branching (Q2)**: the Aussois 2002 diagnosis of hard fixing, the 833 -> 809 outcome, the 29-instance 5-hour testbed and the conceded limits do not come through. The refine removed the local-branching anatomy table that held part of them. The skill's hedge on "RINS beat it" is lost in answers.
- **Erraticism (Q1)**: the selection criterion (positive correlation, H6) and the single-thread, unloaded-machine condition are not used. The refine also removed the erraticism anatomy table, though Method 3 gained the single-thread detail.
- **H9 wording (Q4)**: "a joint paper with the critics' group" for "Boosting the feasibility pump" is unsupported and is echoed in answers. It is still in SKILL.md.
- **Status labels and stochastic controls (Q5)**: no lead/conjecture label (H7), and no fair stochastic control at an equal budget.
- **Agentic answers (Q6)**: few explicit checkpoints, no 🔴 marker, no traces before tables (H8), losses not printed. The refine's one-workflow, stop-at-checkpoint rule targets this but was not re-tested in a retention round.

Added by this test:
- **H3, missed by both arms**: the authors chose not to apply the symmetry fixing, and they kept the black-box results next to the reimplementation's. The skill arm applies the fixing and drops the black-box table. The skill's "don't break my symmetries" heuristic did not reach this case.
- **Over-reach in the skill arm's accounting (H4)**: it also charges the slowest round when sampling does not solve the instance, which is more than the documented final-run-only rule.
- **After-checks (H5)**: the skill arm verifies the fix with counters and log matching rather than an equal time-to-first-solution check.
- **Blind spot**: neither arm names a limit of the lens in the task test, although the Roundtable Card lists binary-only neighbourhoods and no statistical tests before 2026 as blind spots.
- **Task-test unverified grounds**: the specific second baseline (heuristic emphasis or ALNS at the same budget) and conceding the restriction early in the paper are not backed by the notes.
- No change was made to SKILL.md beyond the validation line: fixing these from the sealed items would copy test material into the skill, and what to do about the result is the user's decision.
