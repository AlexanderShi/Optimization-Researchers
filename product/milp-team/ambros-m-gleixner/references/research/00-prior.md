# 00 - Prior snapshot

- Researcher: Ambros M. Gleixner (ORCID 0000-0003-0391-5903; DBLP pid 07/3479)
- Prior snapshot, written before research
- Date: 2026-11-14
- blind: yes

This file is a record of unaided belief. It is not a source and nothing in it may be cited.

## 1. Five characteristic methods or practices (belief)

1. **Research lives inside a production solver.** Ideas are implemented in SCIP / SoPlex / PaPILO and released with the SCIP Optimization Suite, so a method counts when it survives as a default or documented plugin, not as a standalone prototype.
2. **Exactness and certificates as a first-class goal.** He treats floating-point answers as claims to be checked: iterative refinement for LP, exact rational MIP, proof logs (VIPR) that an independent checker can verify, safe cuts and certified presolve.
3. **Curated, reproducible benchmarking.** Benchmark sets are built by a stated, data-driven selection procedure (MIPLIB 2017), and results are reported with shifted geometric means, several seeds or permutations, and affected-instance subsets.
4. **Refine an existing component rather than invent a new framework.** Typical papers take one solver component (OBBT, conflict analysis, cut selection, restarts, presolve) and add a few cheap, well-argued enhancements, each ablated separately.
5. **Large co-authored, student-driven teams.** Many papers come from PhD students and postdocs at ZIB with him as senior author; release reports with long author lists are the group's shared lab notebook.

## 2. Three facts I am most sure of

- He is a core developer and long-time project lead of SCIP at Zuse Institute Berlin, and a professor at HTW Berlin.
- He co-developed iterative refinement for linear programming in SoPlex (with Steffy and Wolter) and has pushed exact rational MIP solving in SCIP (with Eifler).
- He was lead author of MIPLIB 2017 and a co-author of the VIPR certificate format for MIP results.

## 3. Three things I am unsure of

- His doctoral advisor and thesis details: I believe TU Berlin around 2015, on exact and fast algorithms for MINLP, under Koch and/or Grötschel, but I may be mixing in other ZIB theses.
- How much of the machine-learning-for-MIP work (cut selection, heuristic scheduling, tree-size estimation and restarts) is his own direction versus that of students and co-authors such as Turner, Chmiela, Hendel or Berthold.
- His exact role in MINLP in SCIP and in applied projects (gas and water networks, open-pit mining) compared with Vigerske, Pfetsch and others; also any prizes and editorial roles.

## 4. The common one-sentence picture

The person who runs SCIP at ZIB: a computational MIP researcher who cares about numerically trustworthy, exactly verified solving and honest benchmarks.
