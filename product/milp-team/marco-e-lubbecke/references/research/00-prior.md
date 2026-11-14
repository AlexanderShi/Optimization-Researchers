# 00 Prior snapshot: Marco E. Lübbecke

- Researcher: Marco E. Lübbecke (ORCID 0000-0002-2635-0522; DBLP pid 24/5951)
- Prior snapshot, written before research
- Date: 2026-11-14
- blind: yes (no research notes, sources or skill about this person read in this session; only source file names in the git status were visible)

This file is a record of unaided belief. Nothing in it may be cited as a source.

## 1. Five most characteristic methods or practices

1. **Decomposition as the default lens.** He asks whether a MIP has block structure that Dantzig-Wolfe reformulation can exploit, and treats column generation and branch-and-price as general MIP technology, not a per-application craft.
2. **Make it generic and automatic.** Instead of hand-built branch-and-price codes, he builds a solver (GCG, on top of SCIP) that detects structure in the constraint matrix, reformulates and solves without user input.
3. **Experiment on broad instance sets.** He tests decomposition on general MIP libraries and on instances with no known structure, and reports where it loses as well as where it wins; he uses learning to predict when to decompose.
4. **Problems from practice.** Many projects start from an industrial or public-sector scheduling problem (rail, logistics, production, timetabling) and are taken to a model that is actually solved.
5. **Synthesis and teaching.** He writes surveys, primers and a textbook that unify scattered column generation folklore, and invests in lectures, talks and public outreach about OR.

## 2. Three facts I am most sure of

1. He co-authored "Selected Topics in Column Generation" with Jacques Desrosiers (Operations Research, mid-2000s), the standard survey of the field.
2. He leads the Chair of Operations Research at RWTH Aachen, where GCG, the generic branch-cut-and-price solver in the SCIP ecosystem, is developed (begun with Gerald Gamrath).
3. He co-authored the work on automatic Dantzig-Wolfe reformulation of MIPs, detecting bordered block-diagonal structure with (hyper)graph partitioning.

## 3. Three things I am unsure of

1. Which generic branch-and-price ideas are his and which belong to François Vanderbeck (BaPCod, generic branching) or to the GERAD group; I may blur them.
2. His exact role in the degeneracy line (improved primal simplex, row-reduced column generation, vector space decomposition) with Desrosiers and Gauthier, and in Benders support in GCG, which I think is mainly Stephen Maher's.
3. Career and service details: PhD at TU Braunschweig on engine scheduling, then TU Berlin with Möhring, Aachen from about 2010; MIPLIB 2017 co-authorship; editorial roles; the strIPlib library. Dates and details are uncertain.

## 4. The common one-sentence picture

The column generation and branch-and-price person: co-author of the standard survey and the mind behind GCG, who wants Dantzig-Wolfe decomposition to work automatically inside a general MIP solver.
