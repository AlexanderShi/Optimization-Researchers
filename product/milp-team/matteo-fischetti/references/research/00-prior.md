# 00 - Prior snapshot: Matteo Fischetti

- Researcher: Matteo Fischetti (ORCID 0000-0001-6601-0568; DBLP pid 47/4770)
- Status: prior snapshot, written before research
- Date: 2026-11-14
- blind: yes

This file records unaided belief. It is not a source and nothing in it may be cited.

## 1. Five most characteristic methods or practices

1. **Use the MIP solver as a black box.** New ideas are phrased as an auxiliary MIP handed to a general solver ("MIPping", "Just MIP it"): local branching, separation of Chvatal-Gomory or disjunctive cuts by MIP, proximity search.
2. **Simple idea first, proof of concept next.** A thin, almost one-line change (a rounding loop, a distance constraint, a changed objective) is tested quickly; engineering comes only if the first experiment is promising.
3. **Revisit a classical method and repair its known weakness.** Benders cut selection and normalization, pure Gomory cutting planes with lexicographic simplex, the corner relaxation: he asks why the textbook method fails in practice and changes one ingredient.
4. **Distrust small computational differences.** He treats performance variability (random seeds, "erraticism") as a first-class effect: both a threat to benchmark claims and something to exploit by sampling runs.
5. **Start from real applications and competitions.** Railway crew and timetable planning, wind-farm layout, Steiner tree and other challenge instances feed back into general MIP techniques; codes are written to win on the instances, then explained.

## 2. Three facts I am most sure of

- He co-authored the feasibility pump (with Glover and Lodi) and local branching (with Lodi).
- He is at the University of Padova, was a student of Paolo Toth, and worked for years with Toth, Caprara, Lodi, Salazar-Gonzalez, Balas, Monaci, Salvagnin, and later Ljubic and Sinnl (Benders for facility location, bilevel MILP with intersection cuts).
- Early work was branch-and-cut and bounding for routing problems (asymmetric TSP, generalized TSP, orienteering) and set covering for Italian railways crew scheduling.

## 3. Three things I am unsure of

- How deep his formal tie to CPLEX is (consultant or only close collaborator), and which of his ideas ship in which solver.
- His awards: I believe the Edelman (Netherlands Railways team) and the Harold Larnder Prize; a EURO Gold Medal I may be confusing with another person.
- Which machine-learning items are his rather than his daughter Martina Fischetti's or Lodi's (deep networks as 0-1 MILP with Jo is his; wind-park prediction and learning-to-branch work may not be). RINS and solution polishing are not his, though I tend to group them with him.

## 4. The common one-sentence picture

The Padova master of simple, clever MIP heuristics and cut ideas (feasibility pump, local branching) that work on top of any solver and end up inside the commercial ones.
