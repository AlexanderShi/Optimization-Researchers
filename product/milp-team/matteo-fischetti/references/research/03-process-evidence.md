# Matteo Fischetti · 03 Process evidence (what he actually does)

- **Researcher**: Matteo Fischetti, Full Professor of Operations Research at DEI, University of Padova (since 1997; born 1958, by his homepage S1). Not Martina Fischetti, who is first author of the wind-farm papers cited below and, with Michele Monaci, author of one proximity-search paper (see §0).
- **Dimension**: research-craft Phase 1, research agent 03 of 06: process evidence. The lens follows team.json: MILP solver engineering and computation (primal heuristics, branch-and-cut components, Benders, symmetry, performance variability, measurement).
- **Research date**: 2026-11-08
- **Sources consulted**: 40 numbered sources (S1–S40 below). 35 are primary (his homepage and file directories, his preprints, talk decks, code repository, his arXiv and Zenodo deposits, and two co-author or group code pages). 5 are metadata services (Crossref, OpenAlex, OpenReview, Wayback, one web-search pointer). WebSearch calls used: 1.
- **Local corpus**: `references/sources/{papers,talks,essays,software,publications}` hold only `.gitkeep`. There was no user-supplied primary material. `private/` was not opened.
- **Tags**:
  - [stated]: what Fischetti said or wrote about his own work. Co-authored text is marked "co-authored" with the co-authors named.
  - [practice]: what his papers, decks, code, test sets and tables show was actually done.
  - [observed]: what others recorded (co-authors' pages, acknowledgements by other teams).
  - [inferred]: my inference, not established.
  - Each item also says primary (P) or secondary (S).
- **Quotation policy of this note**: to stay within copyright limits the note paraphrases and gives page, slide or file references. It contains one sentence-level quotation (Q1, 13 words, §6). Other quotation marks enclose only short labels, titles, identifiers or parameter names as they appear in the source.
- **Status of the 2026 work**: the 2026 feasibility-pump study (S3–S5) is a submitted manuscript (Mathematical Programming Computation, tag `mpc-submission-1`, 17 Sept 2026). No review record exists in anything read. Every 2026 item below is unreviewed practice.
- **Access notes (2026-11-08)**:
  - www.dei.unipd.it/~fisch/ answered over https; three downloads were reset ("Recv failure") and succeeded over http on retry.
  - OpenAlex marks all 11 key journal DOIs checked as closed access (S37). The journal versions of local branching (2003), the feasibility pump (2005), proximity search (2014), Redesigning Benders (2017) and Just MIP it! (2009) were therefore not read. Except for the 2015 preprint of Redesigning Benders (read as S12), their author preprints are not in his papers directory.
  - The StayNerd code page (univie.ac.at) returned HTTP 503. Its Wayback snapshot (2024-04-14) was refused with HTTP 429 (bot block), and the block was not routed around.
  - The OpenReview profile search returned HTTP 403 (S38).
  - Google Scholar and DBLP were not used (S1 and Crossref gave the identifiers).

---

## 0. Authorship and identity labels (they must survive into the skill)

| Label | Evidence checked in this run | Tag |
|---|---|---|
| Almost every MILP paper is co-authored; the main methodological partners change by era | S1: Toth and Martello (late 1980s–1990s), Caprara, Toth and Vigo (railway codes 1994–2002), Lodi (local branching, FP, closures; mainly 2002–2011), Monaci and Salvagnin (from 2008–09 on), Ljubić and Sinnl (Benders, bilevel, Steiner trees, 2014–2019), Roberti, Salvagnin and Cavaliere (2022–2026) | [practice] P |
| The 2026 FP study is sole-authored, with AI assistants declared | S4 p. 25 (declarations): Claude Fable 5.1 drafted and edited text, wrote and debugged the experiment scripts, and ran internal adversarial reviews; ChatGPT (GPT-5.6 sol) ran an independent adversarial audit before submission. The author says he reviewed text, numbers and code and takes responsibility (paraphrase) | [stated] P |
| The 2026 commits carry AI co-author trailers | S3 (GitHub API, 13 commits, 4–17 Sept 2026): 8 commits end with a "Co-Authored-By: Claude …" trailer (7 × Fable 5.1, 1 × Opus 5); 5 commits have none. All are authored as "Matteo Fischetti" | [practice] P |
| The GitHub account `mfischetti-arch` is his | Account created 2026-09-04, one public repository; CITATION.cff gives his name and unipd address; the Zenodo deposits (S5) have him as sole creator and the manuscript's declarations point to the repository. His homepage links the study's ResearchGate entry, not the GitHub account | [inferred] (strong) |
| "Proximity search heuristics for wind farm optimal layout" is not his | Crossref: Martina Fischetti and Michele Monaci, J. Heuristics 22(4):459–474, DOI 10.1007/s10732-015-9283-4 | [practice] P (metadata) |
| The EndoWake preprints (2026) are Martina Fischetti's first-authored papers, submitted to arXiv by him | S25: 2609.40157, 2610.07844, 2610.39503 list Martina Fischetti first; the submission history of 2610.07844 shows "From: Matteo Fischetti" | [practice] P |
| CPLEX-team adoption is stated, not shown | S11 §1 (co-authored with Lodi, Monaci, Salvagnin, Tramontani): a commercial implementation of the sampling idea is said to be in the CPLEX 12.5.1 default. S17 §3: the CPLEX team is said to have taken a first step with the nonchimerical-branching idea. No CPLEX document was read | [stated] P; adoption unverified |

---

## 1. Era and resource context (timeline for every item below)

| Period | Role and setting (dated) | Compute, tools, team (as the sources state them) | Evidence |
|---|---|---|---|
| 1982–1992 | Laurea (1982) and PhD (1987), Bologna; assistant professor 1990–92 | Combinatorial branch-and-bound with additive bounding (Fischetti–Toth). The 1992 ATSP code is FORTRAN, about 3,000 lines (as described in 2018) | S1; S14 §5.1 |
| 1992–1999 | Padova, L'Aquila, Udine, Padova again (full professor from 1994) | Railway projects for Ferrovie dello Stato (FASTER 1994–97, FARO 1995–98) won as "best computer code" competitions; EU projects; consulting (World Bank, FS, Agip and others) | S1 |
| 2002–2009 | Padova; local branching, FP, closures, Gomory studies; with Lodi, Glover, Balas; PhD theses in his directory: Bertacco (2005), Salvagnin and Zanette (2008) | ILOG CPLEX 7.0 (2002), 8.1 (2004), 9.0.3 (2005), 11.x (2008–09) used as a black box; a Pentium M 1.6 GHz notebook (2004–05); an Intel Core2 Q6600 2.40 GHz PC with 4 GB (2008–09) | S6, S7, S8, S9, S30, S31; S2 (theses) |
| 2010–2014 | Erraticism, sampling, nonchimerical branching, proximity search, orbital shrinking; with Monaci, Salvagnin, Lodi, Tramontani (IBM) | CPLEX 12.2–12.5 through callbacks; an Intel i5 2.67 GHz PC; an IBM power7 workstation; "deterministic ticks" on a shared cluster | S10, S11, S17, S22, S32 |
| 2014–2019 | Benders for facility location, bilevel B&C, DIMACS 2014 Steiner challenge, SelfSplit; with the Vienna group (Ljubić, Sinnl, Leitner, Luipersbeck) | a cluster of identical Xeon E3-1220V2 3.10 GHz nodes with 16 GB (the CPU model of the 2026 DEI blades); a cluster of Xeon E5-2670v2 2.5 GHz nodes with 12 GB for the bilevel paper (location not stated); a cluster of 20-core 2.3 GHz nodes for DIMACS; CPLEX 12.6–12.8 | S12, S13, S14, S16, S18 |
| 2017–2021 | Machine-learning side line (DNNs as MILPs, minibatch persistency, SA inside SGD), with Jo and master students (Mandatelli 2018, Stringher 2019) | MNIST on a 4-core i7 2.3 GHz notebook with CPLEX 12.7; CIFAR-10/AlexNet (2018 preprint) | S15, S25; S2 (thesis file names) |
| 2022–2026 | Matheuristics with Roberti, Salvagnin, Cavaliere; wind farms with Martina Fischetti; in 2026 sole-authored studies with AI assistants | SCIP development snapshot `dba4b2a` + SoPlex `f0dbc81`, patched; Gurobi 13.0.3 via gurobipy; Python 3.12; SLURM on DEI blades (Xeon E5-2623 v3 and E3-1220 v2, 4 exclusive cores, 14 GB per task); the main campaign also ran on a partition that belongs to a colleague; a GPU for EndoWake; OSF pre-registration for the ML study | S3, S4, S25, S26 |

---

## 2. Research taste (layer 1): behavioural evidence

**PE-01. Build on the strongest available solver and add as little as possible.** [practice] [stated] P (co-authored in every case)
- 2002: local branching wraps a black-box CPLEX 7.0 and steers it with one linear constraint (S7, slides 4–7).
- 2004: the first FP talk compares against CPLEX 8.1 halted at the root (S6, slide 10).
- 2013: the erraticism study is a proof-of-concept on top of CPLEX 12.3 (S10 §1).
- 2015: for Benders on UFL, the first version only plugged a cut separator into CPLEX 12.6, and that alone solved open instances; the extra ingredients came after (S12 §3).
- 2015: the paper's stated motive is that a sound Lagrangian relaxation is far from trivial to implement, so a simpler approach on an off-the-shelf solver was tried (S12 §5). The plenary says the first stabilization worked so well that there was no incentive to improve it, under the tag "#OccamPrinciple" (S19, slide 26).
- 2018: SelfSplit parallelizes his own 1992 FORTRAN ATSP code with 46 added lines (S14 §5.1).

**PE-02. Old, neglected tools are fair game when a computational test shows they work.** [practice] [stated] P
- Benders is called folklore that recent computational studies of UFL do not use (S12 §5). The 2015 plenary adds the label "#paperability?" for why simpler schemes are passed over (S19, slide 16).
- 2026: the main result is to restore the FP's own 2005 cutoff-plus-recovery prescription rather than to propose a new heuristic (S4 §8; Q1 in §6).

**PE-03. Simplify the model before complicating the algorithm ("thin out").** [practice] P
- QAP: orbital shrinking plus slim models (S19, slide 14).
- Steiner trees: a node-only model for uniform costs (S13).
- UFL: drop the assignment variables through Benders projection (S12).
- SVM training: fewer parameters beat the full MILP, as the 2015 plenary reports (S19, slides 8–10).
- The 2015 plenary names the same move four times (S19, slides 13–16).

**PE-04. Variability is studied as a resource, not only as noise.** [practice] P
- 2012–14: 100 seeds per instance first showed the spread. Then bet-and-run: short randomized clones, keep the most promising (S10 §§2–4).
- 2013–15: sampling of several root nodes to stabilize B&C (S11).
- 2014–18: SelfSplit uses deterministic sampling to split work without communication (S14).

---

## 3. Problem choice and timing (layer 2)

**PE-05. Problems come from what a solver visibly fails to do on real instances.** [stated] [practice] P (co-authored)
- FP (2004): a solver may spend a very large effort before its first incumbent, and local branching and RINS need one to start. Hence the bet on an early first solution (S6, slide 1).
- Local branching (2002): users otherwise play with emphasis parameters or write ad hoc heuristics (S7, slide 3).
- Proximity search (2013): the stated case for novelty is that, as far as the authors knew, the idea had never been analyzed computationally or embedded in a solver (S22, slide 11).
- Erraticism (2012): high sensitivity to initial conditions is usually treated as a drawback; the working hypothesis is that it is unavoidable (S10 abstract).

**PE-06. External competitions and industry contracts set some problems.** [practice] P
- Code competitions: FASTER 1994 and FARO 1995 for FS (railway set covering and rostering), and the DIMACS 2014 Steiner challenge (codes mozartballs, mozartduet, staynerd) (S1).
- Netherlands Railways work: Edelman Award 2008, Wagner Prize finalist 2004 (S1).
- In the Steiner paper the instances are the challenge's, and the hardware is reported through the DIMACS benchmark program (360.07 trees per second, S13 appendix).

**PE-07. He returns to his own earlier claims years later and tests them harder.** [practice] P
- FP (2005 → 2026): the 2026 study measures what his 2005 paper's warning about the cutoff is worth, on MIPLIB 2017 and inside SCIP (S4 §1).
- Minibatch persistency (2018 → 2026): the 2018 preprint was submitted to a conference and is still listed only as a technical report. In 2026 he runs a sole-authored, pre-registered re-test that tunes the baseline as carefully as the method (S25, 2609.13922 abstract). Outcome in §6.

---

## 4. Idea generation (layer 3)

**PE-08. New heuristics are read as variants of the previous one.** [stated] P (co-authored decks)
- 2004: FP is presented as a modified local branching, with the neighbourhood constraint moved into the LP objective (S6, slide 9).
- 2013: proximity search is listed as a dual version of local branching (S22, slide 11).
- 2026: local branching and the variable-neighbourhood pump are both read as invalid constraints in the projection LP (S4 §3).

**PE-09. Analogies from other fields name the diagnosis and the fix.** [practice] P (his decks; S13 co-authored)
- Gomory's cuts in a Kelley loop are read as a closed-loop system that needs a filter (lexicographic reoptimization). The analogy with metaheuristics then gives the idea of a cut "META-SCHEME" (S23, slides 21–23, Aussois 2008 material reused at CPAIOR 2010).
- The "blur" principle drops details from a relaxation used only to feed a repair phase (S13 §3.2).
- The "chase the carrot" image names the in-out cut loop (S19, slide 27).

**PE-10. The same cut-loop device recurs under new names.** [practice] P; continuity [inferred]
- "yoyo search" (Bertinoro 2009: cut the midpoint between the LP vertex and an interior point; S21, slide 7).
- "in-out approach" (CPAIOR 2010 short paper, DOI 10.1007/978-3-642-13520-0_17; not read).
- In-out stabilization for Benders, moving the stabilizer halfway at each step (S12 §3.2; S19, slide 27).
- "Frank-Wolfe cut loop" (AIROyoung 2026 deck, slide 18).
- That these are one device is my reading of the update rules shown; the sources do not say so.

**PE-10b. A surprising comparison is dissected, and the winner's behaviour is transplanted.** [practice] P (co-authored with Belotti (FICO), Bonami (IBM), Lodi, Monaci, Nogales-Gómez, Salvagnin)
- Indicator constraints (2015 preprint): open-source Couenne, run out of the box on a nonconvex MINLP model, beat IBM CPLEX on the big-M MILP model of the same SVM problem.
- The paper's plan follows that order: show the surprising result, explain why it surprises, analyze why Couenne wins, then make CPLEX mimic it. The key ingredient found is aggressive bound tightening (S33 §1 outline, Table 1).
- The paper won the 2016 COAP Best Paper award (S1).

---

## 5. Experiment design and execution (layer 4)

### 5a. Order of work

**PE-11. First a talk at a small workshop, then the paper.** [practice] P
- Local branching: Aussois, January 2002 (S7) → Math. Program. 98 (2003) 23–47, DOI 10.1007/s10107-003-0395-5.
- FP: Aussois, January 2004 (S6) → Math. Program. 104 (2005) 91–104, DOI 10.1007/s10107-004-0570-3. His homepage shows a photo captioned as the first slide of the very first FP talk (S1); that it is this Aussois talk is [inferred], since it is the earliest FP deck in his directory.
- Bracket-and-fix: Aussois, January 2007 (S20; no paper followed, §9).
- Gomory analysis: Aussois, January 2008 (S23 footers).
- Yoyo search: Bertinoro 2009 (S21, closing slide "Work in progress").

**PE-12. Single-instance traces before the testbed table.** [practice] P
- 2002: incumbent-versus-time traces on seymour and arki001, CPLEX 7.0 in two emphasis settings against CPLEX + local branching, runs up to 18,000 s (S7, slides 5–7).
- 2008–10: LP-solution trajectories and basis-determinant growth on stein15 (S23, slides 10–20).
- 2013: ramos3 timings for three proximity variants against CPLEX (S22, slide 16).
- 2015: the cut-loop comparison on the single instance gs250a-1 (S12 §3.2).
- 2026: the "ping-pong" figure on scpnrh3 (S4 §2, Figure 1).

**PE-13. A "controlled setting first", then real separators.** [practice] P (co-authored)
- 2009: yoyo search was first tested on an LP whose constraint list plays the separation oracle, with three artificial cut-quality rules, before set covering, MIPLIB and Benders (S21, slides 11–20).

**PE-14. Start with the vanilla version and leave implemented extras switched off.** [practice] P
- 2018 non-convex MIQP: lazy callback for McCormick, no user cuts, spatial branching. Intersection cuts and semi-spatial branching were implemented but not used in the vanilla version (S18, slide 15).
- 2013: proximity search deliberately avoided hybrids, under the labels "Stay clean" and "Frankenstein effect" (S22, slide 12).
- 2018: SelfSplit in its simplest variant (S14 §5.1).

### 5b. Implementation platform: black box → gray box → source patch

**PE-15. Callbacks of a closed solver, with fairness devices.** [practice] P (co-authored)
- 2013: every code, the baseline included, gets a (possibly dummy) callback, which switches off CPLEX's proprietary dynamic search in all arms alike (S10 §5).
- 2012: branching rules are compared as in Karzan–Nemhauser–Savelsbergh: root preprocessing applied once, then further preprocessing, heuristics and cuts disabled, and the optimal value given as cutoff (S17 §3).
- 2016: CPLEX preprocessing is disabled because intersection cuts need LP bases in the original space (S16 §6).
- Limits stated by the authors: in 2013, better diversification would need access to the solver's source (S10 §§5–6). In 2013, proximity search with callbacks is called gray-box, with some solver features switched off automatically (S22, slide 13).

**PE-16. 2026: the open-source code is read line by line and patched against a pinned commit.** [practice] P (sole author)
- The paper reads SCIP's `heur_feaspump.c` from the code rather than from the papers. It cites line numbers for the one `SCIPtrySol` call (1271), the cutoff query (795) and the objective-limit reset (1104) (S4 §4).
- The patches replace textual anchors in that file. SCIP and SoPlex are pinned by hash because a newer master would break the anchors (S3 `scip/README.md`).
- Every added parameter defaults to upstream behaviour, so all arms run one binary that differs only in parameter values (S4 §4; S3 `scip/README.md`).
- A separate minimal diff (13 hunks, +341/−3) contains only what the paper recommends. Its Italian report lists the choices made while cleaning it up, what was left out and why, and how it was checked against the campaign binary (S3 `scip/minimal/REPORT_it.md`; `scip/README.md`).
- The same habit in 2009: FP 2.0 documents the restart rule of the original FP by reading its source code (S8 p. 11).

**PE-17. A second, from-scratch implementation where the solver's design would confound the test.** [stated] [practice] P (2026)
- The target experiment is rewritten on Gurobi because, in SCIP, the cutoff row follows the incumbent and the needed contortions looked like overfitting (S3 `campaign_gurobi/README.md`, paraphrase).

### 5c. Test sets: how they are chosen, and what is excluded

**PE-18. Public libraries, with every exclusion declared.** [practice] P
- 2009 (FP 2.0): the 78 instances of the predecessor paper. stp3d was dropped because its first LP was too demanding, and momentum* for numerical problems (S8 §6).
- 2013 (erraticism): COR@L (372, minus one pure LP, one unreadable file and three duplicates) plus MIPLIB 2010 benchmark, tree and hard, with 41 overlaps counted once. The 148 instances that the oracle "best" (the faster of default and bet-and-run) could not solve in 10,000 s were dropped, leaving 344 (S10 §5).
- 2016 (bilevel): download months are recorded for each library. Instances in the MibS repository are avoided because, per its maintainer, some have wrong coefficients (S16 §7).
- 2026: all 463 MIPLIB 2017 instances with at least 80% binaries; none chosen on solution quality. 37 + 2 exclusions are declared and listed (first LP not solved in 600 s; LP numerical failures in SCIP) (S4 §5; S3 `campaign_scip/excluded_instances.txt`).

**PE-19. Difficulty is defined by a baseline run, and subsets are fixed before the variants run.** [practice] P
- Nonchimerical branching: the testbed is what full strong branching solves in 10,000 s (S17 §3).
- Steiner: instances that exact B&C does not solve in one hour with a fixed seed count as difficult; the heuristics then get 10 seeds (S13 §4).
- 2026: one pilot run of the plain pump splits the testbed into E1 (pilot finds a solution, 176) and E2 (248). The pilot gates nothing, and the whole design was fixed before any variant result was seen (S4 §5).
- 2026 census: a stratified sample (20 per family, three size classes, fixed seed) gave 58 distinct instances, 37 usable (S4 §2; S3 `prototype/README.md`).
- 2026 target experiment: the split is exogenous. The MIPLIB 2017 Benchmark Set is primary; 20 random others tune the single knob and are excluded from evaluation; 91 are secondary (S4 §7).

**PE-20. Data availability moves from "on request" to deposited.** [practice] P
- 2009: the generated network-design instances are available on request from the second author (S9 §5).
- 2014: orbital-shrinking instances are available from the authors on request (S32).
- 2017: bilevel instances and the solver are on a co-author's page (S28).
- 2026: everything except the public instances is deposited: the solution files, the raw logs (436 MB, CC BY 4.0) and the code (MIT) (S5).

### 5d. Baselines: how they are chosen

**PE-21. The baseline is what a practitioner would run, including the solver's own heuristic setting.** [practice] P
- 2002: CPLEX 7.0 with MIP emphasis "integer feasibility" next to "optimality" (S7).
- 2004: CPLEX 8.1 default and emp=1, both halted at the root (S6, slide 10).
- 2013: CPLEX 12.4 in several variants (S22, slide 18).
- 2026: SCIP's own objective-weighted pump is the literature baseline. The cell closest to a user who adds the cutoff to the model is kept as the black-box arm (S4 §5).

**PE-22. The previous state of the art on its own terms.** [practice] P
- FP 2.0 compares against the objective FP of Achterberg and Berthold (Discrete Optim. 4 (2007) 77–86, DOI 10.1016/j.disopt.2006.10.004), named as the state of the art (S8 p. 15).
- Bilevel B&C runs the instance classes on which each competitor was originally tested, with no tuning for those subclasses. Published times are compared after a stated hardware factor (Xu and Wang's machine taken as 2 to 5 times slower) (S16 §7).

**PE-23. Ideal oracles and the commercial ceiling are reported beside the method.** [practice] P
- Erraticism: the "best" and "ideal" oracle algorithms are given as benchmarks only (S10 §5).
- Nonchimerical branching: CPLEX 12.2 is reported as significantly faster than all the new rules, because its proprietary search is integrated in the solver (S17 §3).
- 2018 MIQP: SCIP 5.0 is called the more robust solver, although the vanilla B&C is as fast on the instances both solve (S18, slide 16).

### 5e. Measurement rules

**PE-24. Seeds are part of the design.** [practice] P
- FP 2.0 (2009): 10 seeds per instance and variant; a variant counts as successful when it finds a solution in more than 6 of 10 (S8 pp. 13–14).
- Erraticism (2013): 100 runs per instance in the preliminary study (S10 §2).
- Steiner (2014): 10 seeds for the heuristics (S13 §4).
- 2026: 5 seeds; the unit of inference is the instance; median over seeds, then an exact sign test on paired instances (S4 §5).

**PE-25. Time measurement follows the machine actually available.** [practice] P
- 2013: on a workstation with varying load, CPU times are not given; nodes and simplex iterations are (S10 §2).
- 2015: on the shared cluster, CPLEX deterministic ticks with a limit of 10^7 (about 3 hours) (S11 §4.1).
- Steiner: five 4-core runs shared a node to save wall time, with the slowdown stated (S13 §4).
- 2026: each instance's variants and seeds run on one blade, never split across blade types. The budget is 20 × the instance's own first-LP time, clamped to [20, 300] s, so that instances get comparable numbers of pump rounds (S4 §5).

**PE-26. Aggregates and metrics are named.** [practice] P
- Shifted geometric means with the shift stated (0.01 s in S10; 10^3 ticks and 10 nodes in S11).
- Primal integral and the pairwise probability of being 1% better (S22, slides 20–23).
- Performance profiles (S16).
- 2026: W/T/L counts paired per instance, Holm's correction within each pre-declared family of twelve. Post hoc comparisons are marked and kept out of the family (S4 §5, Table 3).

### 5f. Debugging and validation

**PE-27. Instrument the failing algorithm on a toy instance.** [practice] P (co-authored with Balas, Zanette)
- 2008–10: plotted the LP trajectories and the LP-basis determinant of Gomory's method on stein15. Exponential determinant growth was read as the cause of saturation, and lexicographic reoptimization as the remedy (S23, slides 10–21).

**PE-28. Pathological instances correct the method between versions.** [practice] P (co-authored with Salvagnin, Zanette)
- 2009: an earlier version of the MIS-based Benders paper set all CGLP weights to 1. Pathological instances showed null rows in the technology matrix, and their weights were set to 0, a substantial improvement by the authors' account (S9 §4).

**PE-29. A validity test for generated cuts.** [practice] P (co-authored with Ljubić, Sinnl)
- 2015: at the end of each run the incumbent is fixed, perturbed and separated 10,000 times, in the spirit of Margot's test. A model that becomes infeasible is written to file. The check found tolerance issues in earlier code versions (S12 §3).
- Tolerances were set conservatively: CPLEX integrality tolerance 0, other tolerances 10^-9 (S12 §3).

**PE-30. Warm starts isolate a missing component.** [practice] P
- 2018: giving the best-known MINLPlib solution to both codes made the vanilla B&C 2–10 times faster than SCIP. The authors read this as a missing bilinear heuristic, left as TODO (S18, slide 16).

**PE-31. 2026: defects, invariants and revalidation are written into the build and the aggregators.** [practice] P (sole author, AI-assisted)
- A defect found by an external audit: the patches passed a transformed-space solution to `SCIPrecomputeSolObj`, a routine meant for original solutions. It produced 205 runs on 15 instances with a primal bound below the LP bound from perfectly feasible vectors; the value was wrong, not the point (S3 `scip/scip_build_all.sh`, Italian comment, paraphrase).
- The fix builds solutions from scratch. The fixed binaries get new names (suffix "f") so that no result file can mix passes, and the build script asserts after every stage that the faulty call is gone (same file).
- The closed validation run re-read 28,198 `.sol` files with a fresh SCIP on the original model: 0 infeasible, 0 worse, 6 better (S3 `campaign_scip/README.md`). The reason given is that Release builds of SCIP do not re-check the incumbent on the original problem, and that dual reductions preserve an optimum, not the feasible set (same file). A fatal invariant (primal ≥ z_LP − tol) has 0 violations over the 10,218 runs with a solution.
- In the Gurobi experiment, one accepted point in 2,891 failed the recheck and was counted as a failure (S4 §7).
- Treatment-blind delivery: the bare arm used to report only at the time limit, which by itself produced a false conclusion that the cutoff is inert. The fix hands every integral iterate to SCIP at once, in all arms (S3 `campaign_scip/README.md`; S4 §5).
- An instrumented binary is used only after a byte-for-byte identity check against the campaign binary on deterministic runs (S3 `campaign_scip/REPORT_lpft_it.md`).

---

## 6. Judging results (layer 5)

**PE-32. Failures and non-wins stay in the results.** [practice] P
- 2004: on the 49 hard 0-1 instances of the first FP talk, 12 were solved by none of the three codes. On the other 37, FP failed once, CPLEX emp=1 18 times and default CPLEX 8 times (S6, slide 12).
- 2013: bet-and-run does not pay on easy instances. Exploring one sampling node instead of five gave worse results (S10 §5).
- 2012: CPLEX beats the new branching rules on time; reliability branching does not improve time in the authors' implementation (S17 §3).
- 2026: "What this does not show" is a named paragraph. It says that no embedded B&C experiment was run and that E1 is the ground most favourable to the pump. It also lists what was not varied (S4 §8).

**PE-33. A lead is kept apart from an established result.** [practice] P (2026)
- The shallow-target advantage of the completion is called a lead and not an established result, because nothing in the declared family survives Holm (S4 §8).
- An exploratory arm is marked as such in the tables (S4 §7).
- In the adaptive-moat follow-up, one rule was declared primary before the campaign, one secondary, and one exploratory after the smoke test. All 16 declared tests had Holm p = 1 (S3 `campaign_gurobi/REPORT_adapt_it.md`).

**PE-34. A positive recommendation can be a restoration.** [stated] P (2026)
- Q1: "Our recommendation is therefore not a new heuristic but an old one, restored." (S4 p. 19)

**PE-35. His own earlier claim is reversed in public when a stricter test does not hold it up.** [practice] P
- 2018: minibatch persistency was presented as giving significantly faster convergence on CIFAR-10/AlexNet (S25, 1806.07353 abstract).
- 2026: the pre-registered re-test (49M-parameter Transformer, 8 seeds per cell, baseline tuned per batch size and arm) finds no gain in speed or energy, only in fresh data, and only at large batch size. At B = 512 it cannot separate reuse from the schedule position (S25, 2609.13922 abstract). See C-2.

---

## 7. Expression (layer 6)

**PE-36. Implementation details get their own section "for reproducibility".** [practice] [stated] P
- The bilevel paper describes the implementation in terms of CPLEX 12.6.3 for the sake of reproducibility (S16 §6).
- The FP 2.0 paper documents the original FP restart rule from its source code (S8 p. 11).
- 2018 keynote: an algorithm described without implementation is likened to a theorem stated without proof (S18, slides 4–5; paraphrase).

**PE-37. In 2026, the result tables are regenerated by scripts from the shipped raw results.** [practice] [stated] P
- The README states that no number in the paper is typed by hand, and maps every table and figure to the command that regenerates it (S3 README §1, §3). Its own map qualifies this (see C-8).
- Each generated `.tex` opens with two `%%` provenance lines. Numbers quoted in the text carry a `%%` comment naming the report line they come from (S3 README §3).
- The table script checks 14 hard-wired values against the tables (S3 README §3).
- Script comments and output are in Italian, his working language; file names and documentation are in English (S3 README).

**PE-38. Talk decks are versioned public records.** [practice] P
- 120 files in `papers/slides/`, with server dates from January 2002 to November 2026. From 2008 on most decks have the `.ppt`/`.pptx` source next to the PDF. Two 2026 videos are included (S2).
- One slide is reused across eight years with a change. The 2018 keynote labels the claim that cuts inside an enumerative scheme are good a "Theorem", with a proof sketch; the 2026 AIROyoung deck labels the same claim a "Conjecture" (S18, slide 6; S24, slide 2).
- The 2026 deck updates the callback names to CPLEX's generic-callback contexts (`CPX_CALLBACKCONTEXT_CANDIDATE`, `…_RELAXATION`) (S24, slides 4–5).

**PE-39. Metaphors go out of the final text.** [practice] P (co-authored with Martina Fischetti)
- GPU EndoWake: v1 named two artifacts with metaphors ("sirens", "mermaid cells"). v2 replaced them with formal terms and added comparisons with TOPFARM and a second site, Horns Rev 1. v3 states a fixed wake-expansion rate and its effect (S25, 2610.07844 version notes).

---

## 8. Research organisation (layer 7)

**PE-40. A small rotating core of co-authors, with industry engineers inside some papers.** [practice] P
- Lodi was the partner through the heuristics decade (S1).
- Industry co-authors sit inside papers: Tramontani (CPLEX Optimization, IBM Italy) on the sampling paper (S11); Bonami (IBM Spain) and Belotti (FICO) on the indicator-constraint paper (S33). Affiliations are as printed on the preprints.
- The Vienna group carried Benders, bilevel and the DIMACS codes, and hosts the bilevel solver and the UFL data (S28).

**PE-41. Students' theses as an exploration engine.** [inferred] from S2
- The thesis directory holds Mandatelli 2018 and Stringher 2019, whose surnames match the co-authors of the 2018 minibatch preprint and the 2019/2021 SA-SGD work (S25). The theses were not read.
- PhD theses of Bertacco (2005), Salvagnin (2008) and Zanette (2008) match the FP, FP 2.0 and Gomory lines (S2; not read).

**PE-42. Code is shared with competing or neighbouring teams.** [observed] P
- The authors of "Boosting the feasibility pump" thank Salvagnin for his FP-with-propagation source code (S34, acknowledgements). Fischetti is a co-author of that paper (DOI 10.1007/s12532-014-0068-9).
- The 2005 FP code (feaspump.zip) sat in the Bologna OR group's code library. The page cites the FP paper, the general-integer FP report and Achterberg and Berthold's improvement report (S27).

**PE-43. 2026: one senior author, AI assistants, a departmental cluster.** [practice] [stated] P
- Declared roles of the AI assistants: §0 (S4 p. 25).
- Pre-submission audit: two commit messages call it a "fresh-context MPC audit". On 16 Sept 2026, the day before the submission tag, three new campaigns answered three numbered "referee" questions (Q2: α = 0 rerun; M14: cost of the completion; Q3: adaptive moat). Each report gives the question, a short answer, the SLURM job ids and run counts, binary checksums where a binary is involved, and caveats, such as one partition being a colleague's (S3 commits `b3d92aa`, `9f20841`; `REPORT_*_it.md`).
- That this "referee" is the AI audit of the declaration is [inferred] from the dates and wording; the reports do not say who asked.

---

## 9. Failures, abandoned directions and unpublished work

| Item | What the record shows | Tag |
|---|---|---|
| Bracket-and-fix heuristic (with Lodi, Aussois, Jan 2007) | A preliminary BF1 implementation, variants "under investigation" and one "still to be tested" (S20, slides 10–13). No paper with this name is among the 143 entries of his list (S1). The server copy of the deck is dated 23 June 2025 (S2) | [practice] P; abandoned [inferred] |
| Yoyo search (with Salvagnin, Bertinoro 2009) | Ends with "Work in progress" (S21). The name does not reappear in his list; the in-out device does (§4 PE-10) | [practice] P; absorbed [inferred] |
| Pure cutting-plane methods (2008–2012) | IPCO 2008 "Can Pure Cutting Plane Algorithms Work?" (DOI 10.1007/978-3-540-68891-4_29) → Math. Program. 130 (2011) 153–176 (DOI 10.1007/s10107-009-0335-0); "On the enumerative nature of Gomory's dual cutting plane method" (DOI 10.1007/s10107-010-0392-4); the last entry of the line in S1 is a 2012 note on lexicography. A research programme whose question was why a classical method fails | [practice] P; ending [inferred] |
| Minibatch persistency (2018) | arXiv 1806.07353 was submitted to a conference and is still listed as a technical report in 2026 (S1, S25); the 2026 re-test contradicts its headline (PE-35) | [practice] P |
| "Embedded hyper-parameter tuning by Simulated Annealing" (arXiv 1906.01504, 2019) | Not on the homepage list; a 2021 CCIS chapter "Embedding Simulated Annealing within Stochastic Gradient Descent" (DOI 10.1007/978-3-030-85672-4_1) carries the line | [practice] P; same work [inferred] |
| "Finding First and Most-Beautiful Queens by Integer Programming" (arXiv 1907.08246) | Still a technical report; the CPAIOR 2018 paper "Chasing First Queens by Integer Programming" (DOI 10.1007/978-3-319-93031-2_16) is the published part | [practice] P |
| Steiner set-covering repair (2014) | First run in an "over-simplified" form: the Caprara–Fischetti–Toth (CFT) set-covering heuristic was available to the team only as the binary of the commercial TURNI implementation, so it was used off-line through text files and not iterated. Significantly better results came later, after the team re-implemented CFT and embedded it (S13 §3.2, §4, Table 3). A quick shot with what is at hand first, the proper re-implementation after | [practice] P |
| Pieces switched off or left unshipped | McDaniel–Devine warm start, deactivated for all methods (S9 §5); a real bundle method, not implemented (S12 §3.2); ICs and semi-spatial branching, not used in the vanilla MIQP (S18); the 2026 `rcut` arm, kept in the binary but producing no number; exploratory campaigns job00–job22, not shipped because some are contaminated by the defect of PE-31 (S3 README §4) | [practice] P |
| FP cutoff loss in his own later work | The 2026 paper puts FP 2.0 (his, 2009) among works that mentioned the cutoff only in passing, and "Boosting the feasibility pump" (co-authored, 2014) among those that dropped the objective (S4 §1, refs [7], [14]) | [practice] P |

No erratum, correction or retraction is registered in Crossref for his DOIs: the hits for "Fischetti" are other people's (S36). OpenReview holds only a DBLP import of the 2018 preprint, with no review thread (S38).

---

## 10. Early versus final versions

| Work | Early version (read) | Final version | What changed (as far as read) | Tag |
|---|---|---|---|---|
| Local branching | Aussois slides, Jan 2002 (S7) | Math. Program. 98 (2003) 23–47, DOI 10.1007/s10107-003-0395-5 (not read) | Only the early experiments are known here: CPLEX 7.0, single-instance traces | [practice] P |
| Feasibility pump | Aussois slides, Jan 2004 (S6): 49 hard 0-1 MIPs, Pentium M notebook, an added truncated-enumeration stage | Math. Program. 104 (2005) 91–104, DOI 10.1007/s10107-004-0570-3 (not read); S4 quotes its §3.2 on the cutoff and the recovery LP | The 2004 slides already credit Ed Rothberg with better results obtained by avoiding preprocessing (S6, slide 12) | [stated] P; Rothberg's runs [observed] |
| Benders cut selection | "Minimal Infeasible Subsystems and Benders' cuts", extended draft revised Sept 2009, 17 pp (S9) | "A note on the selection of Benders' cuts", Math. Program. 124 (2010) 175–182, DOI 10.1007/s10107-010-0365-7 (not read) | Retitled and published as an 8-page note; the draft already thanks two referees and records the weight correction of PE-28 | [practice] P |
| Random sampling | "Tree Search Stabilization by Random Sampling", Sept 2013 (PDF metadata title: "Randomness and Tree Search") (S11) | "Improving branch-and-cut performance by random sampling", MPC 8 (2016) 113–132, DOI 10.1007/s12532-015-0096-0; preprint revised Jan and Oct 2015 (PDF metadata title: "Branch-and-Cut Stabilization by Random Sampling") | Four titles. §4 renamed from "Tuning for Computational Stability" to "Implementation"; the experiments were re-run on different hardware (i7-2600 3.40 GHz → Xeon E3-1220V2 3.10 GHz) | [practice] P |
| Benders for UFL | "Thinning out facilities: …", 1 April 2015 (S12) | "Redesigning Benders Decomposition for Large-Scale Facility Location", Manag. Sci. 63(7) (2017) 2146–2162, DOI 10.1287/mnsc.2016.2461 (not read) | Retitled. After publication, the co-author's data page added better heuristic solutions for three instances, found with a more aggressive local-branching setting (S28) | [practice] P; [observed] |
| DNNs as MILPs | arXiv 1712.06174v1, "…: A Feasibility Study", submitted to CPAIOR in Nov 2017 | Constraints 23(3) (2018) 296–309, DOI 10.1007/s10601-018-9285-6 | The journal preprint concedes that similar models appeared independently at about the same time and that the model cannot be claimed as new; it moves the contribution to the applications (S15 §1) | [practice] P |
| Learning to search in LB (first author D. Liu) | arXiv 2112.02195v1 (Dec 2021), same title as the AAAI paper | AAAI 36(4) (2022) 3796–3803, DOI 10.1609/aaai.v36i4.20294; arXiv v2 (Aug 2022) retitled "Revisiting local branching with a machine learning lens", a much larger submission (858 KB against 67 KB) | v2 not read | [practice] P (co-authored) |
| GPU EndoWake (first author Martina Fischetti) | A ResearchGate preprint of Sept 2026 → arXiv v1 (6 Oct 2026) | v3 (4 Nov 2026) | v1 recomputed the RANS reference with the published closure constants and kept the conclusions; v2 and v3 as in PE-39 (S25) | [practice] P |
| 2026 FP study | Manuscript v3 of 7 Sept, v3 of 16 Sept (twice) | `mpc-submission-1`, 17 Sept 2026 (25 pp) | Primal-integral columns removed from Tables 4–5; two post hoc rows added to Table 3; a new Table 7; a corrected Section 2 sentence about which blades ran the census (S3 commit log) | [practice] P |

---

## 11. Code and data artifacts (what exists to inspect)

| Artifact | Status (2026-11-08) | Tag |
|---|---|---|
| FP code `feaspump.zip`, "updated 26/10/2005" (Bologna DEIS OR library) | Seen only in a Wayback snapshot of 4 Mar 2015; the live URL redirects (S27). Not downloaded | [practice] P |
| Bilevel MILP solver (Fischetti, Ljubić, Monaci, Sinnl) | Binary only, compiled with CPLEX 12.7, for academic use, with a license file on request; instances downloadable (S28) | [observed] P (co-author's page) |
| UFL and qUFL instances and solutions | On S28; no code listed | [observed] P |
| StayNerd/Mozartballs (DIMACS 2014) | The page is down (HTTP 503); not read | — |
| `mfischetti-arch/fp-objective-cutoff` | MIT; 2,198 tree entries; 13 commits (4–17 Sept 2026); 32,627 `.sol` files; scripts that regenerate every table; Zenodo 10.5281/zenodo.22810777 (software) and 10.5281/zenodo.22810848 (raw logs, 435,658,633 bytes, md5 matching the README) (S3, S5) | [practice] P |
| EndoWake replication packages | Zenodo 10.5281/zenodo.22017424 (CC BY 4.0, 10 Sept 2026); concept 10.5281/zenodo.22017446 → v2.1.0 at 10.5281/zenodo.23955408 (4 Nov 2026); 10.5281/zenodo.23636074 (29 Oct 2026). Metadata only (S26) | [practice] P |

The change from "on request" or binary-only releases (2009–2017) to fully open packages (2026) is the clearest change in his practice in the record.

---

## Contradictions (kept, not reconciled)

**C-1. The cutoff that FP 2.0 used, and the 2026 critique of that use.**
- 2009: FP 2.0 tested solution quality by adding cᵀx ≤ z*(1+δ), δ ∈ {0.1, 1.0, +∞}, to the model before running the pump (S8 p. 14). Its recovery handling is not described in the passages read.
- 2026: the same author measures this static black-box use of the cutoff as lossy without the recovery. He groups FP 2.0 with the works that mentioned the cutoff only in passing (S4 §1).
- Both are [practice] P; the 2026 study is unreviewed.

**C-2. Minibatch persistency, 2018 against 2026.**
- 2018: significantly faster convergence with comparable or better generalization, on CIFAR-10/AlexNet (S25, 1806.07353).
- 2026: no gain in steps, seconds or joules; a saving in fresh data only at large batch; the B = 512 effect cannot be separated from the learning-rate schedule (S25, 2609.13922).
- Both abstracts are his. The 2026 one says the earlier tests lacked a baseline tuned as carefully as the method.

**C-3. Stabilization: "no incentive to improve" against continued redesign.**
- 2015 talk: the first stabilization worked so well that there was no incentive to improve it (S19, slide 26).
- The 2015 preprint itself presents the in-out loop as a stand-in for a real bundle method (S12 §3.2). The 2026 tutorial teaches the device as a Frank–Wolfe cut loop (S24, slide 18).
- Kept as a tension between the stated stopping rule and the later reframing.

**C-4. Black-box versus source access.**
- 2013: the authors write that the next step would need the solver's source code (S10 §6). They label callback implementations gray-box (S22, slide 13).
- 2017: they still release their own solver as a closed binary with a license on request (S28).
- 2026: he patches open-source SCIP at the source level and publishes everything (S3).
- Kept as a tension: in 2013 the team asked for source access to others' solvers, and in 2017 released its own as a binary.

**C-5. The 2026 package documentation contradicts itself.**
- README §4, item 5, says `chk_mixed.py` does not exist as a separate file and is not included.
- README §3, `campaign_scip/README.md` and the repository tree list `campaign_scip/chk_mixed.py`, added in commit `b73d062` on 7 Sept 2026 (GitHub API).
- §4.5 was apparently not updated after the file was added [inferred].

**C-6. Declared AI tools against commit trailers.**
- The manuscript's declaration names Claude Fable 5.1 and ChatGPT (GPT-5.6 sol) (S4 p. 25).
- Commit `cd40ec2` (17 Sept 2026, "Realign with the final manuscript") carries a "Co-Authored-By: Claude Opus 5" trailer. That model is not named in the declaration.

**C-7. Who audited.**
- `scip/README.md` attributes the `SCIPrecomputeSolObj` defect (fixed 2 Sept 2026) to "an external audit". The declaration names one independent adversarial audit, of the manuscript, by ChatGPT (S4 p. 25).
- Whether the code defect was found by that audit, by another tool or by a person is not stated.

**C-8. "No number typed by hand" against numbers "quoted by hand".**
- The README's opening says no number in the paper is typed by hand (S3 README §1).
- Its own table says that several numbers are printed by a script and then quoted by hand in the text: the two paragraphs after Figure 1 and the pure-versus-mixed numbers of Section 6. It also says that Table 2 is written by hand in the manuscript (S3 README §3).
- The script-generated tables and the `%%` provenance comments still hold. The absolute claim does not.

---

## Gaps (what could not be found or verified)

**Not read (closed journal versions, no author preprint in his directory):**
- Local branching (2003); The feasibility pump (2005, known here from the 2004 deck and the 2026 paper's quotation of its §3.2); proximity search (J. Heuristics 20(6) 709–731, 2014, DOI 10.1007/s10732-014-9266-x, known from the 2013 deck); Redesigning Benders (2017, known from the 2015 preprint); Just MIP it! (DOI 10.1007/978-1-4419-1306-7_2).
- "Comments on: On learning and branching: a survey", his two-page published comment (TOP 25(2) 237–238, 2017, DOI 10.1007/s11750-017-0449-0). This is the only published exchange found, so how he comments on others' work in print is unread.

**Not found:**
- Referee reports or rebuttals for any journal paper. OpenReview holds none (S38). The 2009 draft and the 2016 bilevel preprint only thank anonymous referees.
- Released code for local branching, proximity search, the Benders UFL code, orbital shrinking, or the erraticism and sampling studies. None is in his directories or on the co-author pages checked (S27, S28). The search was not exhaustive (one web search, spent on the bilevel solver).
- What happened to bracket-and-fix (no paper, no later mention found).
- Whether CPLEX 12.5.1 really adopted the sampling idea, and whether CBC and GLPK 4.51 implemented proximity search. The 2013 deck says they did (S22, slide 24); none of these claims was checked.

**Not done:**
- The 2026 videos in `papers/slides/` (`2026_svm_telecom_video.mp4`, 17 MB; `2026_backprop_video.mp4`, 10 MB) were not transcribed: no transcription tool was available. No transcript was saved under `references/sources/talks/`.
- Theses in `ricop/tesi/` were not read; that is agent 04's ground.
- The ResearchGate entries (the 2026 FP study, the "digital twin of Fermat" essay) were not opened; ResearchGate is login-walled for full texts. The Fermat essay is outside MILP and was not read.
- The rest of the 120 decks was not read, including the 2014 ISCO "BRANCHstorming" plenary, the 2012 EURO erraticism deck, the 2015 ISMP proxy-Benders deck, the 2016–2017 bilevel decks and the 2025 VeRoLog parts 2–3. Only file names and dates are known.

**Unclear:**
- Which assistant did what, commit by commit, in 2026 beyond the declaration (C-6, C-7). The two Claude-Session links in the commit trailers were not opened; they are private session URLs.
- Who posed the "referee" questions Q2, Q3 and M14 (PE-43).
- The 2026 package ships 32,627 `.sol` files, while its validation file has 28,198 `VALID|` rows and the manuscript counts 10,218 solutions reported by the grid runs plus 237 others (S3 README §4; S4 §5). How the three counts relate is not explained in what was read. They may count different things (every incumbent file, validated rows, final incumbents per run); this is unverified.

---

## Sources

| # | Title · author · date · location | Use | P/S |
|---|---|---|---|
| S1 | Homepage CV and publication list (143 entries, numbered to [142] plus [124bis]; technical reports; prizes; career) · M. Fischetti · read 2026-11-08 · https://www.dei.unipd.it/~fisch/ | read in full | P |
| S2 | Directory listings with file dates: `papers/` (64 files), `papers/slides/` (120 files), `ricop/tesi/` (16 files) · read 2026-11-08 · www.dei.unipd.it/~fisch/papers/, …/papers/slides/, …/ricop/tesi/ | listings read | P |
| S3 | `mfischetti-arch/fp-objective-cutoff`, reproducibility package · M. Fischetti · 4–17 Sept 2026 · https://github.com/mfischetti-arch/fp-objective-cutoff (README, CITATION.cff, LICENSE, scip/README.md, scip/NOTICE.md (head), scip/scip_build_all.sh, scip/minimal/REPORT_it.md, campaign_scip/README.md, REPORT_alpha0_it.md, REPORT_lpft_it.md, campaign_gurobi/README.md, REPORT_adapt_it.md, prototype/README.md, paper/README.md; GitHub API for metadata, tree and the 13 commits) | files read; commits listed | P |
| S4 | "Feasibility Pump with Objective Cutoff: A Computational Study" · M. Fischetti · manuscript, September 2026, 25 pp, submitted to Math. Prog. Comp. (unreviewed) · `paper/manuscript.pdf` in S3 | abstract, §1, §§3–5 and §8 read in full; parts of §2 and §7; references and declarations read | P |
| S5 | Zenodo deposits: "Feasibility Pump with Objective Cutoff: reproducibility package", DOI 10.5281/zenodo.22810777 (software, MIT, 2026-09-17); "Raw SCIP logs of …", DOI 10.5281/zenodo.22810848 (dataset, CC BY 4.0) · M. Fischetti | metadata read | P |
| S6 | "The feasibility pump" · M. Fischetti, F. Glover, A. Lodi · talk deck, Aussois, January 2004 · …/papers/slides/2004 Aussois [feasibility pump].pdf | read in full (incremental builds collapsed) | P (co-authored) |
| S7 | "Local branching, or how to enhance the heuristic behaviour of your favourite 0-1 MIP solver" · M. Fischetti, A. Lodi · talk deck, Aussois, 6–11 January 2002 · …/papers/slides/Aussois 2002 [local branching].PDF | slides 1–10 read | P (co-authored) |
| S8 | "Feasibility Pump 2.0" · M. Fischetti, D. Salvagnin · preprint 26 Oct 2008, revised 8 May 2009 · …/papers/feasibility_pump_201.pdf; journal: Math. Prog. Comp. 1(2–3):201–222, 2009, DOI 10.1007/s12532-009-0007-3 | §§5–6 read; journal not read | P (co-authored) |
| S9 | "Minimal Infeasible Subsystems and Benders' cuts" · M. Fischetti, D. Salvagnin, A. Zanette · extended draft, revised Sept 2009 · …/papers/Benders_mis_extended_draft.pdf; journal: "A note on the selection of Benders' cuts", Math. Program. 124:175–182, 2010, DOI 10.1007/s10107-010-0365-7 | §§3–6 read; journal not read | P (co-authored) |
| S10 | "Exploiting erraticism in search" · M. Fischetti, M. Monaci · OR manuscript OPRE-2012-05-278(R), March 2013 · …/papers/exploiting_erraticism_in_search.pdf; journal: Oper. Res. 62(1):114–122, 2014, DOI 10.1287/opre.2013.1231 | §§1–2 and 5–6 read; §§3–4 not read; journal version not read | P (co-authored) |
| S11 | "Tree Search Stabilization by Random Sampling" (Sept 2013) and "Improving Branch-and-Cut Performance by Random Sampling" (revised Jan and 2 Oct 2015) · M. Fischetti, A. Lodi, M. Monaci, D. Salvagnin, A. Tramontani · …/papers/tree_search_stabilization_by_random_sampling.pdf, …/improving_branch_and_cut_performance_by_random_sampling.pdf; journal: Math. Prog. Comp. 8(1):113–132, DOI 10.1007/s12532-015-0096-0 | §§1, 4 read and compared; headings compared | P (co-authored) |
| S12 | "Thinning out facilities: a Benders decomposition approach for the uncapacitated facility location problem with separable convex costs" · M. Fischetti, I. Ljubić, M. Sinnl · preprint, 1 April 2015 · …/papers/thinning_out_facilities.pdf; journal: "Redesigning Benders Decomposition for Large-Scale Facility Location", Manag. Sci. 63(7):2146–2162, 2017, DOI 10.1287/mnsc.2016.2461 | §§3–5 read; journal not read | P (co-authored) |
| S13 | "Thinning out Steiner trees: a node-based model for uniform edge costs" · M. Fischetti, M. Leitner, I. Ljubić, M. Luipersbeck, M. Monaci, M. Resch, D. Salvagnin, M. Sinnl · tech report, Nov 2014 · …/papers/thinning_out_Steiner_trees_dimacs11.pdf; journal: Math. Prog. Comp. 9(2):203–229, DOI 10.1007/s12532-016-0111-0 | §3.2, §4, appendix header read | P (co-authored) |
| S14 | "SelfSplit parallelization for Mixed-Integer Linear Programming" · M. Fischetti, M. Monaci, D. Salvagnin · preprint, Jan 2018 · …/papers/self_split_for_MIPs.pdf; journal: Comput. Oper. Res. 93:101–112, 2018, DOI 10.1016/j.cor.2018.01.011 | §3 (assumptions) and §5.1 read | P (co-authored) |
| S15 | "Deep Neural Networks and Mixed Integer Linear Optimization" · M. Fischetti, J. Jo · preprint, April 2018 · …/papers/deep_neural_networks_and_mixed_integer_linear_optimization.pdf; journal: Constraints 23(3):296–309, DOI 10.1007/s10601-018-9285-6; early version arXiv 1712.06174 | §§1, 3–5 read | P (co-authored) |
| S16 | "A new general-purpose algorithm for mixed-integer bilevel linear programs" · M. Fischetti, I. Ljubić, M. Monaci, M. Sinnl · preprint, Dec 2016 · …/papers/bilevel_branch_and_cut.pdf; journal: Oper. Res. 65(6):1615–1637, 2017, DOI 10.1287/opre.2017.1650 | §§6–7 (parts) and acknowledgements read | P (co-authored) |
| S17 | "Branching on nonchimerical fractionalities" · M. Fischetti, M. Monaci · preprint, Oct 2011 · …/papers/nonchimerical-branching.pdf; journal: Oper. Res. Lett. 40(3):159–164, 2012, DOI 10.1016/j.orl.2012.01.008 | §3 and appendix read | P (co-authored) |
| S18 | "#post_modern Branch-and-Cut Implementation" · M. Fischetti · ISMP 2018 keynote deck, Bordeaux, 6 July 2018 · …/papers/slides/2018 ISMP [keynote Fischetti on BandC].pdf | read in full | P |
| S19 | "The simpler the better: Thinning out MIP's by Occam's razor" · M. Fischetti · CORS/INFORMS 2015 plenary deck, Montreal, June 2015 · …/papers/slides/2015 CORS [Fischetti - Occam Razor].pdf | read in full | P |
| S20 | "MIP models for MIP heuristics, or the Bracket-and-Fix method" · M. Fischetti, A. Lodi · deck, Aussois, 12 Jan 2007 · …/papers/slides/2007 Aussois [bracket-and-fix heuristic].pdf | read in full | P (co-authored) |
| S21 | "Cutting planes: don't back yourself into the corner!" (yoyo search) · M. Fischetti, D. Salvagnin · deck, Bertinoro, 30 Nov–2 Dec 2009 · …/papers/slides/2009 Bertinoro [yoyo search].pdf | read in full | P (co-authored) |
| S22 | "Proximity search" · M. Fischetti, M. Monaci · deck, EURO Rome, July 2013 · …/papers/slides/2013 EURO Rome [Fischetti - proxy].pdf | read in full | P (co-authored) |
| S23 | "Toward a MIP-cut metascheme" (opening with "Looking inside Gomory", Aussois 2008 material) · M. Fischetti · CPAIOR 2010 deck, June 2010 · …/papers/slides/2010 Toward a MIP-cut metascheme [Fischetti CPAIOR].pdf; abstract LNCS 6140 pp. 1–2, DOI 10.1007/978-3-642-13520-0_1 | slides 9–23 read; abstract not read | P |
| S24 | "Branch-and-Cut is our swiss army knife" · M. Fischetti · AIROyoung deck, Padua, 9 Feb 2026 · …/papers/slides/2026 AIROyoung - Fischetti part 1 [BC + Benders].pdf | read in full | P |
| S25 | arXiv records (API and abstract pages, 2026-11-08): 1712.06174v1; 1806.07353v1; 1906.01504v1; 1907.08246v1; 2112.02195v1–v2; 2609.13922v1; 2609.40157v1; 2610.07844v1–v3; 2610.39503v1 · arxiv.org | metadata, version notes, abstracts read | P |
| S26 | Zenodo EndoWake replication packages: DOI 10.5281/zenodo.22017424; concept 10.5281/zenodo.22017446 (current 10.5281/zenodo.23955408, v2.1.0); DOI 10.5281/zenodo.23636074 · Martina Fischetti, Matteo Fischetti · 2026 | metadata read | P |
| S27 | Bologna DEIS OR group, "Library of Codes – Feasibility Pump" (FP code updated 26/10/2005) · Wayback snapshot 2015-03-04 of www.or.deis.unibo.it/research_pages/ORcodes/FP-gen.html | read | P (group artifact) |
| S28 | M. Sinnl's pages "Bilevel Integer Programming and Interdiction Problems", "Facility Location Problems", "Instances, Codes, etc" · read 2026-11-08 · https://msinnl.github.io/pages/bilevel.html, …/fl.html, …/instancescodes.html | read | P (co-author's host) |
| S29 | "Combinatorial Benders' Cuts for Mixed-Integer Linear Programming" · G. Codato, M. Fischetti · preprint, 7 Mar 2005 · …/papers/combinatorial_benders_cuts_for_milp.pdf; journal: Oper. Res. 54(4):756–766, 2006, DOI 10.1287/opre.1060.0286 | setup lines only | P (co-authored) |
| S30 | "Repairing MIP infeasibility through local branching" · M. Fischetti, A. Lodi · preprint, Sept 2005 · …/papers/repairing_MIP_infeasibility_through_local_branching.pdf; journal: Comput. Oper. Res. 35(5):1436–1445, 2008, DOI 10.1016/j.cor.2006.08.004 | setup lines only | P (co-authored) |
| S31 | "On the enumerative nature of Gomory's dual cutting plane method" · E. Balas, M. Fischetti, A. Zanette · preprint, Dec 2009 · …/papers/Enumerative_nature_Gomory.pdf; journal: Math. Program. 125(2):325–351, 2010, DOI 10.1007/s10107-010-0392-4 | setup lines only | P (co-authored) |
| S32 | "Orbital Shrinking: Theory and Applications" · M. Fischetti, L. Liberti, D. Salvagnin, T. Walsh · preprint, Jan 2014 · …/papers/orbital_shrinking_theory_and_applications.pdf; journal: Discrete Appl. Math. 222:109–123, 2017, DOI 10.1016/j.dam.2017.01.015 | setup lines only | P (co-authored) |
| S33 | "On handling indicator constraints in mixed integer programming" · P. Belotti, P. Bonami, M. Fischetti, A. Lodi, M. Monaci, A. Nogales-Gómez, D. Salvagnin · preprint, April 2015 · …/papers/indicator_constraints.pdf; journal: Comput. Optim. Appl. 65(3):545–566, 2016, DOI 10.1007/s10589-016-9847-8 | setup lines only | P (co-authored) |
| S34 | "Boosting the feasibility pump" · N. Boland, A. Eberhard, F. Engineer, M. Fischetti, M. Savelsbergh, A. Tsoukalas · preprint, Sept 2011 · …/papers/boosting_the_feasibility_pump.pdf; journal: Math. Prog. Comp. 6(3):255–279, 2014, DOI 10.1007/s12532-014-0068-9 | acknowledgements and setup lines only | P (co-authored); [observed] |
| S35 | "Integer (Linear) Optimization" · E. Balas, M. Fischetti · preprint, Nov 2016 · …/papers/Integer_(Linear)_Optimization.pdf; book chapter in Advances and Trends in Optimization with Engineering Applications (SIAM 2017) pp. 49–63, DOI 10.1137/1.9781611974683.ch5 | two passages read | P (co-authored) |
| S36 | Crossref REST API: DOI and title checks for every identifier in this note; searches for errata, corrections, retractions and comments by Fischetti · queried 2026-11-08 | identifier checks | S |
| S37 | OpenAlex API: open-access status of 11 key DOIs (all closed) · queried 2026-11-08 | access checks | S |
| S38 | OpenReview API: profile search (HTTP 403); notes search (only a DBLP-import record of 1806.07353) · queried 2026-11-08 | review-record check | S |
| S39 | Web search pointer (1 call) to the bilevel solver page, verified by reading S28 directly · 2026-11-08 | pointer only | S |
| S40 | Wayback Machine availability API (FP code page: snapshot 2015-03-04; StayNerd page: snapshot 2024-04-14, fetch refused with HTTP 429) · 2026-11-08 | access checks | S |

**Works cited as context, identifiers checked with Crossref (2026-11-08), not sources about his process:**
- Achterberg & Berthold, "Improving the feasibility pump", Discrete Optim. 4:77–86, 2007, DOI 10.1016/j.disopt.2006.10.004.
- Danna, Rothberg & Le Pape, "Exploring relaxation induced neighborhoods to improve MIP solutions", Math. Program. 102(1):71–90, 2004 per Crossref (cited as 2005 in S20), DOI 10.1007/s10107-004-0518-7.
- Bertacco, Fischetti & Lodi, "A feasibility pump heuristic for general mixed-integer problems", Discrete Optim. 4(1):63–76, 2007, DOI 10.1016/j.disopt.2006.10.001.
- Berthold, Lodi & Salvagnin, "Ten years of feasibility pump, and counting", EURO J. Comput. Optim. 7(1):1–14, 2019, DOI 10.1007/s13675-018-0109-7.
- Koch et al., "MIPLIB 2010", Math. Prog. Comp. 3(2):103–163, 2011, DOI 10.1007/s12532-011-0025-9.
- Gleixner et al., "MIPLIB 2017", Math. Prog. Comp. 13(3):443–490, 2021, DOI 10.1007/s12532-020-00194-3.
- Caprara, Fischetti & Toth, "A Heuristic Method for the Set Covering Problem", Oper. Res. 47(5):730–743, 1999, DOI 10.1287/opre.47.5.730.
- Fischetti & Toth, "An additive bounding procedure for the asymmetric travelling salesman problem", Math. Program. 53:173–197, 1992, DOI 10.1007/bf01585701 (the FORTRAN code reused in S14).
- Fischetti & Monaci, "A branch-and-cut algorithm for Mixed-Integer Bilinear Programming", Eur. J. Oper. Res. 282(2):506–514, 2020, DOI 10.1016/j.ejor.2019.09.043 (the journal outcome of the S18 MIQP work [inferred]).
- Liu, Fischetti & Lodi, "Learning to Search in Local Branching", AAAI 36(4):3796–3803, 2022, DOI 10.1609/aaai.v36i4.20294.
- Fischetti & Stringher, "Embedding Simulated Annealing within Stochastic Gradient Descent", CCIS 1443:3–13, 2021, DOI 10.1007/978-3-030-85672-4_1.
- Fischetti & Salvagnin, "Chasing First Queens by Integer Programming", LNCS (CPAIOR 2018) pp. 232–244, DOI 10.1007/978-3-319-93031-2_16.
- Fischetti & Salvagnin, "An In-Out Approach to Disjunctive Optimization", LNCS 6140 (CPAIOR 2010) pp. 136–140, DOI 10.1007/978-3-642-13520-0_17.
- Zanette, Fischetti & Balas, "Can Pure Cutting Plane Algorithms Work?", LNCS (IPCO 2008) pp. 416–434, DOI 10.1007/978-3-540-68891-4_29; journal "Lexicography and degeneracy: can a pure cutting plane algorithm work?", Math. Program. 130(1):153–176, DOI 10.1007/s10107-009-0335-0.
- Fischetti & Monaci, "Proximity search for 0-1 mixed-integer convex programming", J. Heuristics 20(6):709–731, 2014, DOI 10.1007/s10732-014-9266-x.
- Fischetti, Monaci & Salvagnin, "Self-splitting of Workload in Parallel Computation", LNCS (CPAIOR 2014) pp. 394–404, DOI 10.1007/978-3-319-07046-9_28.
- Fischetti & Liberti, "Orbital Shrinking", LNCS 7422 (ISCO 2012) pp. 48–58, DOI 10.1007/978-3-642-32147-4_6.
- Fischetti, Lodi & Salvagnin, "Just MIP it!", Annals of Information Systems 10, pp. 39–70, 2009, DOI 10.1007/978-1-4419-1306-7_2.
- Salvagnin, Roberti & Fischetti, "A fix-propagate-repair heuristic for mixed integer programming", Math. Prog. Comp. 17(1):111–139, DOI 10.1007/s12532-024-00269-5.
- M. Fischetti (Martina) & M. Fischetti, "Integrated Layout and Cable Routing in Wind Farm Optimal Design", Manag. Sci. 69(4):2147–2164, 2023, DOI 10.1287/mnsc.2022.4470.
- Martina Fischetti & M. Monaci, "Proximity search heuristics for wind farm optimal layout", J. Heuristics 22(4):459–474, DOI 10.1007/s10732-015-9283-4 (not Matteo Fischetti's, see §0).
