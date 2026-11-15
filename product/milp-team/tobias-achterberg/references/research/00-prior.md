# 00 - Prior snapshot: Tobias Achterberg

- Researcher: Tobias Achterberg (ORCID 0000-0002-0862-7065; DBLP pid 71/6632)
- Status: prior snapshot, written before research
- Date: 2026-11-14
- blind: yes (no research notes, sources or skill about this person were read in this session; only file names in a git status listing were visible)

This file records unaided belief. Nothing here is verified and nothing here may be cited as a source.

## 1. Five most characteristic methods or practices

1. **Build the whole solver, then study its parts.** His research unit is a complete branch-and-cut code (SCIP, later CPLEX and Gurobi); ideas count once they live inside a full framework with plugins for branching, cuts, presolve, heuristics and propagation.
2. **Judge by large-testbed computation, not by examples.** Shifted geometric means over hundreds or thousands of instances, time-bracket subsets, counts of "affected" models, random seeds or permutations to separate real gains from performance variability.
3. **Ablate components.** Switch one feature off in a mature solver and report the degradation, so each technique's contribution is measured in context rather than in isolation.
4. **Import ideas across neighbouring fields.** Conflict analysis from SAT, domain propagation and constraint handlers from CP, merged into MIP as "constraint integer programming".
5. **Write up engineering detail.** Long, explicit descriptions of presolve reductions, branching scores and data structures that most solver developers leave unpublished.

## 2. Three facts I am most sure of

1. He wrote SCIP as his PhD work at ZIB / TU Berlin (thesis "Constraint Integer Programming", around 2007, advisor Martin Groetschel), and the SCIP paper in Mathematical Programming Computation won the Beale-Orchard-Hays Prize.
2. With Koch and Martin he wrote "Branching rules revisited", which introduced reliability branching, and he co-authored MIPLIB 2003 and MIPLIB 2010.
3. He moved to industry: CPLEX at ILOG/IBM, then Gurobi, where he leads R&D; with Wunderling he wrote the "12 years of progress" MIP paper, and with Bixby, Gu, Rothberg and Weninger the Gurobi presolve paper.

## 3. Three things I am unsure of

1. Exact dates and titles (joined ILOG about 2006, Gurobi about 2014; "VP of R&D"?), and how much of Gurobi's nonconvex MIQCP / global MINLP work is his own design.
2. Whether the shifted geometric mean and the feature-disabling protocol originate with him or with Bixby, Danna or Koch; I may be merging him with Timo Berthold (primal heuristics), Thorsten Koch (MIPLIB) and Roland Wunderling.
3. Whether he supervises students in any formal sense, and how he chooses problems now: customer models and bug reports versus literature.

## 4. The common one-sentence picture

The creator of SCIP who became the leading industrial MIP solver engineer, trusted for careful, large-scale computational evidence about what actually makes branch-and-cut fast.
