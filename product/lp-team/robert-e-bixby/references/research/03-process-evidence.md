# Robert E. Bixby · 03 Process evidence (what he actually does)

- **Researcher**: Robert E. Bixby. Rice University mathematician who wrote the original CPLEX simplex code and co-founded CPLEX Optimization and later Gurobi. **Living status and present role are not established** by any dated source after September 2022 (team.json leaves `living` out on purpose). This note states neither, and every role below carries its date.
- **Dimension**: research-craft Phase 1, research agent 03 of 06: process evidence. The lens follows team.json: decision and measurement craft for LP (1987–2002) and for MIP.
- **Research date**: 2026-11-05
- **Sources consulted**: 36 numbered sources (S1–S36 below). 13 of them are primary texts read in full or in the relevant part (S1–S13). The rest are secondary sources, metadata or abstracts. Crossref checks were also made of 12 works he cites (listed at the end). WebSearch calls used: 5.
- **Local corpus**: `references/sources/{papers,talks,essays,software}` hold only `.gitkeep`. `publications/` holds the OpenAlex harvest summary (`publications.md`, `abstracts.md`), which was read. There was no user-supplied primary material. `private/` was not opened.
- **Tags**:
  - [stated]: what Bixby said or wrote about his own work. Co-authored text is marked "co-authored".
  - [practice]: what his papers, decks, test sets and tables show was actually done.
  - [observed]: what others recorded.
  - [inferred]: my inference or my own arithmetic, not established.
  - Each item also says primary (P) or secondary (S).
- **Quotation policy of this note**: to stay within copyright limits, the note paraphrases and gives page references. It contains one sentence-level quotation (Q1, five German words). All other quotation marks enclose only verbatim labels, titles, column names or phrases of a few words. Numbers, model names, slide titles and table labels are reproduced as facts.
- **Page conventions**:
  - S1: printed page = PDF page + 2 (gwern mirror of the typeset pages).
  - S2: printed page = PDF page + 106.
  - S3: newsletter page = PDF page.
  - S4 and S5: the preprints' printed page numbers.
  - S7: the running-header page numbers of the ILOG preprint (the book's pages 19–49 were not seen).
  - S6: PDF page plus the footer slide number where there is one (the footers skip some slides).
  - S8 and S9: footer slide numbers.
- **Access notes (2026-11-05)**:
  - Anubis bot challenge to curl: ZIB OPUS (opus4.kobv.de) and dblp.org. No challenge was solved. WebFetch received the ZIB PDFs directly. dblp.org also denied WebFetch, so DBLP was not used.
  - AWS WAF challenge (curl) and HTTP 403 (WebFetch): the Rice repository (repository.rice.edu).
  - Request blocked: DTIC.
  - HTTP 403: one ScienceDirect page. INFORMS pages were not retried; team.json records 403s for them.
  - None of these was routed around.

---

## 0. Authorship labels (they must survive into the skill)

| Label | Evidence checked in this run | Tag |
|---|---|---|
| Main parts of the CPLEX simplex, as of April 1992, are his | S4 p. 2 introduces the paper as the first of a planned series on the CPLEX implementation of the simplex method. Q1, on that implementation: "deren Hauptteile vom Author geschrieben wurden" ("whose main parts were written by the author") | [stated] P |
| All development at the 1988 first release | S3 p. 3: at the first release in 1988 he was responsible for all of the development (paraphrase) | [stated] P |
| Still doing development in 1997 | S3 p. 4: at the 1997 ILOG acquisition he was doing development and was still an academic (paraphrase) | [stated] P |
| No development at Gurobi | S3 p. 4, answer continuing on p. 5: he did no development at all. He tested a lot and kept asking the developers why the code behaved badly (paraphrase). In Oct 2015 he described his own activity as running the code all the time and complaining (S3 p. 6) | [stated] P |
| CPLEX LP changes from 5.0 to 7.1 and later are not shown to be his | S1 p. 14 (acknowledgments) credits Gu, Lustig, Rothberg and Wunderling with fundamental contributions to the CPLEX LP algorithms. S7 (co-authored, five ILOG authors) presents the CPLEX 6.5 LP changes as "we" and names no implementer | [stated] P; [inferred] for "not shown" |
| Dual steepest edge is Forrest and Goldfarb's method, implemented in CPLEX | S1 pp. 6 and 8: Forrest and Goldfarb (1992) supplied dual steepest edge ("version 1"). S2 p. 113: a variant proposed by Forrest and Goldfarb. S5 pp. 2–3: both CPLEX steepest-edge variants (SE1, SE2) are from Forrest–Goldfarb; the default is SE1 with all initial norms 1 | [stated] P |
| MIP cuts and most presolve were Gu's. Node presolve, probing, bound strengthening and the first heuristics were Rothberg's. Parallel barrier was Rothberg's | S3 p. 4 (cuts and most presolve: Gu; node presolve, probing, bound strengthening, heuristics: Rothberg). S3 p. 3: Rothberg's parallel barrier was linked into CPLEX through the SGI partnership; the MIP code "took off" when Rothberg and Gu joined, which he calls the CPLEX 6.5 story | [stated] P |
| Early MIP codes such as MINTO beat CPLEX | S3 p. 3: early CPLEX versions had knapsack cuts, and solvers such as MINTO solved problems CPLEX could not | [stated] P |
| He put strong branching into CPLEX after a discussion with Cook | S3 p. 4: strong branching came out of the TSP work and came up in a talk with Bill Cook; he put it into CPLEX. He also tuned the CPLEX library to work with the TSP code. The real MIP contributions were Rothberg's and Gu's, and later Achterberg's | [stated] P |
| The decision to add MIP came from sales | S3 p. 3: Todd Lowe gets the credit for seeing that the business needed MIP | [stated] P |
| His own crossover contribution | S3 p. 3: he made a few small observations that made crossover much faster. S6 PDF p. 15 (slide 16): the first really fast crossover (based on a result of Megiddo) came out of the 1989 AA challenge, a team of five whose roles are not divided | [stated] P |
| His MIP lens is measurement and decision craft, not MIP code | Follows from the rows above. Every MIP progress number below was measured on code that he says he did not write (CPLEX 6.5 and later, Gurobi) | [inferred] |

---

## 1. Era and resource context (timeline for every item below)

| Period | Role and setting (dated) | Compute, tools, team | Evidence |
|---|---|---|---|
| Early 1980s – ~1986 | Theoretical researcher (matroids) at Northwestern, then Rice. LP was a hobby. First a classroom code (1983), then the LP module for Tom Baker's Chesapeake Decision Sciences (MIMI) | IBM PC, Fortran, then C (Baker's condition). Worked alone. Fourer gave advice in conversation; he did not read the literature | S1 p. 3; S3 pp. 1–2; S6 PDF p. 9 (slide 10) |
| ~1986–1988 | First benchmarks against XMP. Amoco licence (1986 or 1987, see C-15). Company founded (1987 or 1988, see C-15). CPLEX 1.0 released 1988, all development his | Sun 3/50 (his desk machine in late 1987), netlib, XMP as the external baseline. Research funding for LP computation 1987–88: none obtained | S1 pp. 3, 5, 11; S3 pp. 2–3; S6 PDF pp. 9, 11 |
| 1989–1992 | CPLEX Optimization plus Rice. Challenge models (AA crew scheduling, degen4/LAU2). Callable library (~1990/91). Visit to ZIB (S4 written there) | Cray Y-MP/X-MP time through John Gregory (Cray Research); 40 MHz SPARCstation 2. Grants NSF CCR-8815914 and AFOSR-90-0273 | S1 p. 8; S3 p. 3; S4 pp. 1, 19; S6 PDF pp. 14–22 |
| 1993–1997 | The dual simplex "matured" in 1994 (his dating). Parallel dual simplex with A. Martin (ZIB). ILOG bought CPLEX in 1997; he was still developing | SUN S20 workstations, a 10 Mb/s Ethernet LAN, IBM SP2 (8 × 66 MHz nodes), SGI Power Challenge (75 MHz R8000, 2 and 4 CPUs). NSF CCR-9407142; Rice CRPC | S3 pp. 3–4; S5 pp. 1, 6–9, 12, 17 |
| 1997–2008 | ILOG CPLEX. The MIP "breakthrough" of CPLEX 6.5 (Gu, Rothberg). His measurement studies: 2000 (co-authored), 2002, 2004 (co-authored, not read), late 2007 | 296/300 MHz Sun UltraSparc, 400 MHz Pentium II Linux (0.5 GB), 500 MHz Alpha 21264, 667 MHz Compaq ES40, 2.0 GHz Pentium 4. In 2007, "a bank of identical computing machines" | S1; S2 p. 116; S7 |
| 2008–2015 | Gurobi co-founder. By his account: no development, testing, sales, talks. Oct 2015: Chairman of the Board and CSO, half time (a dated statement, not evidence of any later role) | Gurobi MIP library: 600 models collected from public sources in two days, later ~10,000; the developers' test set ~3,500 (S3) or 3,550 models (S8) | S3 pp. 4–6; S8 slide 34; S9 |
| 2015–Sept 2022 | Talks (Imperial 2015, ECCO 2017). Co-author of the Gurobi presolve paper (ZIB report 2016, IJOC 2020). Hausdorff School deck, Sept 2022: the latest dated trace | Gurobi 6.5 on a 4-core i7-3770K, 3600 s limit (presolve paper) | S6; S8; S12; S17 |

---

## 2. Research taste (layer 1): behavioural evidence

**PE-01. Real models, not random ones, carry the evidence.** [practice] [stated] P
- 1992: he used netlib because, as far as he knew, it held no randomly generated problems; all came from real modelling attempts (S4 p. 6).
- He also warned that some netlib models are there only because they once caused simplex trouble. That makes them useful for robustness work but poor for setting parameter values (S4 p. 6).
- 2002: the decisive test set was the CPLEX library of about 2,000 models gathered over 13 years from industry and academia (S1 p. 12).
- 1999/2000: a largely proprietary MIP set was preferred to MIPLIB 3.0 for judging performance (S7 p. 20, co-authored).
- 1998: most of the new MIPLIB 3.0 instances came from real applications, and a table gives each instance's originator, formulator and donor (S10 pp. 13–14, co-authored).
- Era: customer models reached him through CPLEX Optimization and ILOG. In 2015 he said that at Gurobi they collected 600 models from public sources within two days, with NEOS contributing many (S3 p. 6).

**PE-02. A default that seldom hurts beats an idea that sometimes wins big.** [stated] [practice] P (S4 sole-authored; S7 co-authored)
- S4 p. 17: the CPLEX starting basis is meant as a default start, not a crash procedure. The aim is to avoid a bad basis rather than find a good one, because a crash procedure on a model of unknown origin can be disastrous.
- S7 p. 3: MIP features should help where they can and hurt as little as possible elsewhere. The paper contrasts this with theory papers that test one idea in isolation.
- S7 pp. 6–7: in the CPLEX 6.5 LP work, the larger effort went into making sure the large-model gains did not get in the way on the middle range of models.
- S7 pp. 12–13, 15–16: every technique is applied to every model, and implementation effort then goes into detecting when a technique is not helping and switching it off. Node presolve runs for the first 100 nodes, is kept or dropped by its effect, and is reconsidered every 100 nodes. Five diving heuristics run at the root; only the most successful one is applied periodically afterwards.
- Authorship: the 6.5 features are Gu's and Rothberg's by S3 p. 4. What S7 shows of Bixby is the stated principle and the measurement, not the code.

**PE-03. Numerical robustness is the first deliverable.** [stated] [practice] P
- S3 p. 2: early on he was proudest of the code's stability. Chesapeake's models were snapshots from a sequential LP procedure, with condition numbers he puts at about 1e20. After two years of fixing breakages the code was very stable.
- S1 p. 3: his first comparison also found his code more stable than XMP.
- S4 pp. 7–14 (Part I): before evaluating any technique he audited netlib numerically:
  - condition numbers (infinity norm) of the optimal bases, scaled and unscaled;
  - objective differences between the default solve and a re-solve with tolerances of 1e-9 and pivot threshold 0.9999, started from the default optimal basis;
  - residuals, and bound and reduced-cost infeasibilities (Tables II–III, SPARCstation 2 with IEEE arithmetic).
- S7 pp. 4–5 (co-authored): the decade's most significant LP development is named as robustness (numerical difficulties, degeneracy), not speed.

**PE-04. Speed that matters commercially is "must-have" speed.** [stated] P
- S6 PDF pp. 18–19 (slides 20–21) and S3 p. 3 tell the same story:
  - The SGI-CPLEX parallel barrier was about 40 times faster than OSL on airline models.
  - Airlines did not switch, because OSL was fast enough for them.
  - A merger due-diligence study then needed fast turnaround (OSL 3–4 hours against 5 minutes, per the deck), and the speed became decisive.
- His lesson slide calls this the "must-have" story.
- The barrier code was Rothberg's (S3 p. 3). The craft attributable to Bixby is the reading of when speed changes a buyer's decision.

**PE-05. Engines are judged by how well they embed and re-solve, not only by from-scratch speed.** [stated] [practice] P
- S1 p. 3: integer-programming research needed a robust LP code that could be embedded and re-solved after added or deleted rows and columns and variable fixings. This was a fundamental motivation for the CPLEX callable library.
- S3 p. 3: the framework idea came from Grötschel's papers (callable library around 1990/91). S2 p. 116 makes the same point.
- S5 p. 1: the dual was parallelized rather than the primal for two reasons: the primal's partial pricing removes much of the parallelism, and the main application is re-optimization inside integer programming.
- S2 p. 114 and S1 p. 13: crossover is always counted as part of barrier. Commercial codes treat it as integral, and MIP needs a basis for warm starts.
- S1 p. 6: barrier's weak re-solve is why simplex stays dominant in practice.

**PE-06. Judging outside ideas by their effect inside a production solver.** [stated] P
- S3 p. 6 (Oct 2015): little had come out of research in the previous ten years, with two exceptions he weighed differently. RINS was "big". Symmetry handling was big but not huge, and a form of orbital branching went into Gurobi.
- Testing a small idea outside a commercial code can at most show it looks reasonable; the vendors then decide (S3 p. 6). Cut management (aggregation, which cuts to keep, interaction between MIR, Gomory and flow-cover cuts) is named as the hard open part (S3 p. 6).

---

## 3. Problem choice and timing (layer 2)

**PE-07. The customer's failures set the agenda (about 1984–1986).** [stated] P
- S1 p. 3 and S3 p. 2: for about two years Chesapeake sent practical LPs on which the code did badly or broke. Each time he examined the code and the LP. He did not consult the literature; this was not his research area (S1 p. 3), and he never actually read anything, although Fourer told him about the issues (S3 p. 2).
- Before that, Baker compared Bixby's network simplex with his own; Bixby's was about sixty times faster and was embedded in the product (S3 p. 2). The customer's head-to-head test made the choice.
- Era: alone, at home, as a hobby alongside matroid research (S3 p. 2).

**PE-08. Public challenge models as forcing problems.** [stated] P
- degen4 / LAU2 (S1 p. 8; S3 p. 3; S6 PDF pp. 20–22, slides 22–24). The airline fleet model (4,420 rows, 6,711 columns, 101,377 nonzeros) drove the sequence:
  - degeneracy handling,
  - solving the explicit dual,
  - a dual simplex code,
  - dual steepest edge.
- The AA crew-scheduling LP of 1989 (S6 PDF pp. 14–17, slides 15–16 and 19):
  - Size: 837 rows and 12,753,313 columns.
  - Method: sifting, an idea credited to Forrest. Subsets of columns are solved, the rest priced with the duals, and violated columns added.
  - Run: on a Cray Y-MP, after what the slide calls "Considerable experimentation". Ten major iterations (five barrier, then crossover, then five primal), 247 s in all (204 optimizing, 43 pricing; the iteration log is on PDF p. 16).
  - Lessons he drew: the first fast crossover, and enthusiasm for larger models.
  - The team was Bixby, Lustig, Marsten, Shanno and Gregory; roles are not divided.
- That model was reused: S5 builds a scalable test family from truncations of it (each "aaK" model is the first K columns; S5 p. 7 fn. 5).

**PE-09. A student's research need changed the production code.** [stated] P
- S3 p. 3: Sanjay Saigal's max-cut LPs were so degenerate that Bixby had to add something to the code or the student could not proceed. This, together with LAU2, is how perturbation entered CPLEX.

**PE-10. Size trends as the timing signal.** [stated, co-authored] P
- S7 p. 5: the 1999 LP work started from the observation that LPs had grown. That led to a focus on models with at least 10,000 constraints and on the simplex method, which was underperforming there. The bottleneck (the FTRAN/BTRAN solves) was found quickly. The paper calls this the same kind of observation that started the developments a decade earlier.
- Authorship: the CPLEX 6.5 LP code is not shown to be his (Section 0).

**PE-11. A stated expectation first, a measurement years later (MIP).** [stated] [practice] P
- S1 p. 4 (2002): he had little doubt that the improvement in integer-programming codes exceeded that for LP.
- S2 pp. 116–118 (2012): the late-2007 test on 1892 models, plus Gurobi releases, gave a combined machine-independent factor far above LP's.

---

## 4. Idea generation (layer 3)

**PE-12. Turn the model around.** [stated] P
- S1 p. 8: the key idea for degen4 was to look at the dual. Building the explicit dual and running the default primal on it removed the degeneracy and beat barrier. This was among the main motives for dual simplex in CPLEX.
- S6 PDF p. 21 (slide 23) gives the same idea: perhaps the dual is far less degenerate.

**PE-13. Ideas arrive through people, not through reading.** [stated] P
- Fourer:
  - general computational knowledge, passed on in conversation (S1 p. 3);
  - the Harris ratio-test tolerance idea behind shifting (S3 p. 4).
- Forrest:
  - his success with primal devex led to implementing dual steepest edge (S6 slide 23);
  - the sifting idea (S6 slide 15).
- Goldfarb: suggested a simpler steepest edge, which became a new dual steepest edge (S6 slide 23).
- Cook: strong branching (S3 p. 4).
- Randy Batsell (Rice business school): the least-squares growth-rate fits (S1 p. 9, endnote 8 on p. 14).
- Ashford, Gregory, Rothberg, Shaw and Tomlin: e-mail exchanges and private communications used as historical sources (S2 p. 118 and refs [2], [39], [43]).

**PE-14. The simplest fix after an instrumented struggle.** [stated] P
- S3 p. 4: non-monotone steps came from slightly negative basic variables. After two weeks of trying "all kinds of instrumentation" he moved the violated bound instead (bound shifting).
- At the end the bounds are restored and the basic variables re-solved. He says this left the solution feasible about 95% of the time.
- He calls shifting his most important contribution, says no paper was ever written on it, and that he never got around to it.

**PE-15. Borrow known algorithms from neighbouring fields.** [stated] P
- S1 p. 6 and S7 p. 5: sparse triangular solves whose work grows with the number of nonzeros touched were already known in sparse linear algebra (Gilbert and Peierls 1988), equivalent to a graph-reachability problem.
- Authorship of the CPLEX 6.5–7.1 implementation is not shown to be his.

**PE-16. Mine the theory backlog wholesale (MIP, 1998).** [stated] P
- S2 p. 117: about thirty years of relevant theory had not been implemented in commercial codes, so CPLEX 6.5 ran a systematic programme to include as many of these ideas as possible.
- S8 slide 31 labels the jump *Mined Theoretical Backlog: 1998*. S7 pp. 26–27 summarise it the same way.
- Who decided this is not named (the sentence is passive). The code was Gu's and Rothberg's (S3 pp. 3–4).

**PE-17. MIP "tricks" from staring at models.** [stated] P
- S9 slide 35: many tricks are found just by looking at models. They are cheap to apply and work on a small fraction of models.
- These are Gurobi's tricks (the slide says "Our trick", S9 slide 19); by S3 p. 4 they are not his code.

---

## 5. Experiment design and execution (layer 4)

### 5a. Order of work

**PE-18. Tolerances first, then a numerical audit of the test set, then the technique.** [practice] [stated] P
- S4 p. 7: fixing the tolerances is called one of the first tasks in implementing a numerical algorithm. The defaults he fixed are given on the same pages:
  - feasibility and optimality tolerances 1e-6;
  - Markowitz threshold pivoting following Suhl and Suhl, threshold 0.01.
- Part I (the netlib audit, PE-03) precedes Part II (the starting basis).

**PE-19. Profile, compute the parallel share, then pick the test models.** [practice] P
- S5 pp. 4–5 profiled the sequential dual on an SGI Power Challenge before any parallel code was written (Table 1). The parallelizable share came out at 24.0% for pilots and 97.3% for aa300000.
- The authors concluded that only models with many more columns than rows could gain.
- Their first thought was to target models too large for one processor's memory, which led to networked workstations and PVM.
- [inferred] Amdahl bounds from that profile: about 1.2 on 4 processors for pilots and 3.7 for aa300000. The 4-processor results (Table 11) were 1.1 and 4.6. The second exceeds the bound, which the paper reports as exceeding ideal speedup (p. 17).

**PE-20. Study small members of a model class before solving the class.** [stated] P
- S4 p. 6: it makes little sense to solve a whole class without first examining some smaller instances closely.
- Example: once fit1d proved much easier than its equivalent dual form fit1p, there was little reason to spend effort on fit2p.
- The pilot models are known to be badly scaled and are better handled with a stronger scaling than the CPLEX default.

**PE-21. The development path becomes the ablation.** [practice] P
- S4 p. 15 presents four starting bases: artificial, feasible slack, slack, and the CPLEX basis. The middle two are described as stations on the way to the CPLEX basis.
- All 90 netlib problems were run with all four (pp. 19–20).

### 5b. LP test sets and baselines

**PE-22. Baselines chosen with stated reasons.** [stated] [practice] P
- S1 p. 11: XMP was chosen because it was portable and embeddable, widely used in 1980s integer-programming research, and had state-of-the-art factorization.
- MPSX/370 and MPS III were rejected as baselines because they were tied to mainframes no more than 50 times slower than current workstations. His 1989 runs on an IBM 3090 had found MPSX/370 and CPLEX 1.0 comparable on several harder models.
- S1 p. 3: portability was also the reason for the first comparison in about 1986.
- S3 p. 2: at that time he thought XMP was the standard and did not know MPSX was much faster.

**PE-23. Screening rules for the library.** [practice] P
- S1 p. 12 (2002):
  - Near-duplicate instances were removed, generally keeping the largest two or three of a family.
  - Models solved in under 0.25 s by both CPLEX 5.0 and 7.1 with all three default algorithms were removed. 680 models remained.
- S7 pp. 8–9 (co-authored, 1999):
  - Large LPs were those with at least 10,000 rows after CPLEX 5.0 presolve.
  - Minor variants were removed, and a family of growing instances was represented by its largest member.
  - Models had to fit into 0.5 GB of memory in presolved form.
  - Proprietary models were given generic names (LP01–LP90).

**PE-24. A stable core of real models reused for a decade.** [inferred from matching size statistics] P
- The model "car" (43,387 rows, 107,164 columns, 189,864 nonzeros) appears as follows:
  - in the 1994 study (S1 Table 8),
  - as LP49 in the 1999 large-LP set (S7 Table 1),
  - as M39 in a re-hosted ILOG-era deck (S16 slide 39).
- "energy1" (16,223 × 28,568 × 88,340) is LP09 and M1.
- "initial" (27,441 × 15,128 × 96,118) is M19.
- The 2002 "very large model" of Example 3 (5,034,171 × 7,365,337 × 25,596,099) is M79.

**PE-25. Time limits sized to let old codes finish, and old codes run for weeks.** [practice] P
- Time limits: 350,000 s (about four days) in S1 p. 12; 500,000 s (about six days) in S7 p. 9. S7 says such a large limit was necessary, or the comparisons would not have been possible.
- S1 p. 9: CPLEX 1.0 ran on mnetgen24 for 1,221,920.3 s, just over two weeks. CPLEX 1.0 times for the largest PDS models were left out because of the run lengths expected.
- The production-planning model (401,640 constraints, 1,584,000 variables) on a 2.0 GHz Pentium 4 (S8 slides 9–14; S6 PDF pp. 24–27, slides 26–29):
  - CPLEX 1.0 was started in Houston on 13 Nov 2002.
  - Its elapsed days were reported at the next talks: Berlin (8.0 days, 21 Nov), Dagstuhl (15.0 days, 28 Nov), Amsterdam (19.0 days, 2 Dec) and Houston (23.0 days, 6 Dec).
  - It finished at 29.8 days.

**PE-26. Separate machine effects from algorithm effects by recompiling old code.** [practice] P
- S1 pp. 4–5: simplex machine speedups were estimated by running CPLEX 1.0, compiled on current machines, against 1988 results. Barrier machine speedups used the Linpack benchmarks.
- S2 p. 116: in late 2007, each of twelve released CPLEX versions was recompiled to run on one target machine type.

**PE-27. Controlled timing conditions, stated each time.** [practice] P
- S4 p. 20: batch mode on a dedicated system with no other jobs; user times from the `times` library function.
- S5 p. 7: wall-clock times for the presolved models, excluding reading and presolve.
- S1 p. 7: CPU seconds on one stated machine.

**PE-28. Like-for-like code paths.** [practice] P
- S5 p. 11: the shared-memory version went back to the sequential pivot rule so that results would be easier to compare.
- S5 p. 15: the partition count K was set identically in the sequential and parallel codes, after a superlinear speedup was traced to it (PE-49).
- S5 p. 16: the reorganisations also applied when the dual ran sequentially, keeping a single code base.

### 5c. LP measurement rules

**PE-29. Geometric mean of per-model ratios; how the practice evolved.** [practice] [stated] P
- 1992 (S4 pp. 19–20):
  - Totals of iterations and times are reported but called less informative than hoped, because a few hard problems dominate them.
  - Per-problem ratios against the CPLEX basis are added, with averages (the type of mean is not stated).
  - Losses are counted: the CPLEX basis was slower in 20 of 90 cases; 12 of these were less than 10% slower than the slack basis, and only one more than 30% slower. The average gain over the slack basis was about 35%.
- 2002 (S1 p. 11): on the 1988 data, the ratio of total times gives 4.3, the arithmetic mean of ratios 9.6, and the geometric mean 4.70. He judges the geometric mean better, more robust and more conservative.
- 2000 (S7 p. 3, co-authored): "mean" always denotes the geometric mean, because arithmetic means of ratios can mislead.
- 2012 (S2 p. 112): he re-analysed Sharda and Somarajan's published 1986 data with geometric means. LINDO came out about 166 times slower than MPSX/370, against a machine ratio of about 15 that he estimated from LINPACK.

**PE-30. Cumulative size brackets, with row count as the difficulty proxy.** [practice] [stated] P
- S1 p. 12: row count is the best simple predictor of difficulty he has found.
- Table 14 reports results for nested brackets of models with at least a given row count. S1 p. 13 explains each entry as a geometric mean over the models in the bracket.
- S7 pp. 7–10 uses "Biggest k" brackets, and segments small LPs by the old version's solve time (0–1, 1–10, 10–100 s).

**PE-31. Best-of-algorithms as "the algorithm", with crossover included.** [practice] [stated] P
- S1 Tables 11–12 and 14, and S2 p. 114: for each model the fastest of primal, dual and barrier (with crossover) counts.
- S2 p. 114 concedes that one can argue whether this is legitimate, and says it is the method he used.

**PE-32. Chained comparisons forward in time.** [practice] [stated] P
- S1 p. 11: running the big set on 1987-vintage code would take a large part of a year. He therefore chains comparisons that move forward in time and argues that they convince as a whole.
- S2 p. 117: the cumulative MIP factor is the product of the consecutive version-pair ratios, which he calls a projected, machine-independent improvement.
- S16 slide 38 (re-hosted ILOG deck): no single test can cover ten years, so several were combined.

**PE-33. Time limits, memory failures and unsolved models, handled explicitly.** [practice] P
- S1 pp. 12–13: three models solved by no algorithm within the limit were omitted. They were omitted even though barrier without crossover solved them, because crossover is part of the default.
- S7 p. 9: memory failures were excluded; timeouts were scored at the limit, so the improvements are underestimated.
- S2 p. 116: for MIP, unsolved models are scored at the time limit.

**PE-34. Win counts next to the means.** [practice] P
- S7 p. 11: dual against primal won 56 to 30; dual against barrier 41 to 37; overall, primal won 18, dual 33 and barrier 39 of 90 models.
- S1 p. 13 and S4 p. 20 report losses in the same way.

### 5d. MIP test sets and measurement

**PE-35. The late-2007 CPLEX MIP progress protocol.** [practice] [stated] P
- Protocol (S2 p. 116):
  - 1892 models selected from a library of real problems collected from academia and industry over almost twenty years;
  - each of twelve CPLEX releases, from 1.2 (the first with MIP) to 11, recompiled for one target machine and run on a bank of identical machines;
  - a 30,000 s limit;
  - consecutive versions compared on the models that at least one of the two solved to optimality, with timeouts scored at the limit;
  - the geometric mean of the time ratios for each pair.
- He says he undertook the test himself ("I undertook", first person). Results:
  - a bar for each version pair; 6.0 is the arguable exception, and 2.1 to 3.0 gives about 5.5, which he ties to the maturing of the dual simplex (S2 p. 117);
  - a cumulative product over 29,000 (S2 p. 117; 29,530 on S8 slide 31 and S9 slide 7).

**PE-36. How the MIP test set was derived from the library.** [practice] P
- S8 slide 30 (2017):
  - full library of 2,791 MIPs;
  - removed: 559 "Easy" MIPs, 348 "Duplicates" and 22 "Hard" LPs (0.8%);
  - pure default settings and a 30,000 s limit; versions CPLEX 1.2 (1991) to 11.0 (2007).
- The slide names the result "1852 real-world MIPs" (see C-11 for the count).

**PE-37. Partition the test set by outcome class, with a metric per class.** [practice] P (co-authored)
- S7 p. 20, CPLEX 6.0 against 6.5 on MIPLIB 3.0 (500 MHz Alpha 21264, 7200 s):
  - 22 models solved by both in under 10 s were set aside;
  - 10 solved only by 6.5 (geometric-mean time 48.5 s);
  - 8 solved by neither, compared by final gap (6.5 better by a factor of 3.3 in the geometric mean; 6.0 better in one case);
  - 19 solved by both (11.2 times faster).

**PE-38. A test set of "difficult but solvable, assuming tuning was allowed".** [practice] P (co-authored)
- S7 pp. 20–21 describe how the proprietary 80-model set was built about two years earlier:
  1. Each model of the CPLEX model library was run with defaults on the fastest machine then available.
  2. Models solved in under 100 s were dropped.
  3. The rest got extensive runs, some lasting several days, with varied settings.
  4. Everything solved this way was kept, except fewer than five models that took more than about half a day.

**PE-39. New defaults against the old version's best tuned settings.** [practice] P (co-authored)
- S7 p. 21: CPLEX 6.5 defaults against 6.0 defaults: 6.5 faster on 66 models, 6.0 on 10, geometric-mean speedup 22.3.
- Against 6.0 with the best settings known to the authors: 6.5 faster on 56, 6.0 on 22, mean 3.8.
- Exclusions are disclosed: MIP45 was dropped because 6.0 stopped early on basis singularities (footnote 7).

**PE-40. Ablation in two directions, and attribution of a breakthrough to features.** [practice] P (co-authored)
- S7 pp. 21–22 ran two experiments:
  - each feature switched off in turn from the defaults;
  - all six cut classes switched off, then each switched back on alone.
  - Gomory cuts were the "biggest surprise".
- S9 slide 11 (2012) gives feature factors for 78 models that were not solvable before CPLEX 6.5 and solvable in under 1,000 s after:
  - cutting planes 33.3x,
  - presolve 7.7x,
  - variable selection 2.7x,
  - node presolve 1.3x,
  - heuristics and dive probing 1.1x each.
  - The slide does not name the source study.
- S15 p. 4 [observed, S] relays the 2004 Progress Report (S26, not read): 758 instances; CPLEX 5.0 against 8.0 gave a geometric-mean speedup of about 12, and about 528 on the instances the old code needed over 27 hours for.

**PE-41. Curating a public benchmark: MIPLIB 3.0.** [practice] P (co-authored: Bixby, Ceria, McZeal, Savelsbergh)
- S10 p. 14: "easy" was measured with a deliberately plain branch-and-bound. The setting was CPLEX 3.0 on a SPARC 10/41 with no preprocessing, largest-infeasibility branching, best-bound node selection, and no cuts or heuristics.
- Models solved in 11 s or less were deleted; every other model needed at least 25 s.
- air06 was removed because it solves as an LP.
- Families were thinned to avoid duplication. For the bell and set1 families the more difficult members were kept (bell3a, which is relatively easy, also stayed). Of three similar randomly generated fixnet models, one was kept more or less at random.
- A constraint classification was added to help research on reformulation (S10 pp. 12, 14).
- The Rice-hosted page dates MIPLIB 3.0 to January 1996, names McZeal as the maintainer, was last updated on 19 Oct 1998 and says it is no longer maintained (S11).

**PE-42. The Gurobi-era library and the co-authored benchmarking protocol.** [stated] [practice] P
- S3 p. 6: 600 models gathered in two days, about 10,000 later, and a developers' test set of about 3,500. S8 slide 34 plots a library of 3,550 models by rows and columns.
- The presolve paper's protocol (S12 §1.1; co-authored with Achterberg, Gu, Rothberg and Weninger; his role not divided; Gurobi code not his):
  - reference: Gurobi 6.5 defaults, 3600 s limit;
  - each reduction disabled in the master MIP only, kept on in sub-MIPs to avoid changing heuristic behaviour;
  - 3,182 models that some Gurobi release solved within 10,000 s;
  - models on which the two versions disagree about the optimal value are excluded;
  - nested time brackets, preferring the bracket of models that took at least 10 s;
  - "faster" and "slower" counted at a 10% threshold;
  - shifted geometric means with a shift of 1;
  - "affected" models identified by differing simplex iteration counts;
  - the presolve result was checked against an independent CPLEX study (Achterberg and Wunderling).
- The same paper reports null results. Chvátal–Gomory strengthening and simple probing did not help at all (S12 pp. 12, 16). The SOS sample was called too small to conclude anything (S12 p. 17).

**PE-43. Rare-but-huge effects reported with counts and medians.** [practice] P
- S9 slide 26: the disjoint-subtree fix affected 35 of 510 test models. One model went from more than 10,000 s to 0.01 s. The slide warns that this makes mean improvements over a small set hard to quote, and gives the median for affected models: about 1%.
- S9 slide 29: the modular-inverse reduction affected under 3% of models, with one model dropping from 10,000+ s to 0.05 s and a small positive effect overall.

**PE-44. Third-party public benchmarks to anchor comparisons across vendors.** [practice] P
- S2 pp. 117–118: in 2009 Hans Mittelmann's public benchmarks showed Gurobi 1.0 roughly equal to CPLEX 11.0. Gurobi's later gains (16.2 to version 5.0) were then measured internally, and the same public benchmarks are cited for XpressMP and SCIP.
- S9 slide 19: the cross-vendor times for a knapsack instance are taken "from Mittelmann".

### 5e. Debugging and diagnosis

**PE-45. A customer-driven repair loop.** [stated] P
- S1 p. 3 and S3 p. 2: fix one breakage, then wait for the next one. It was mostly numerical stability, two years of problems sent by a customer who "knew how to push my buttons".

**PE-46. Read the counts before trusting a timing.** [stated] P
- S3 p. 2: in his first benchmark against XMP he picked standata as his best case and was about seven times slower. Two weeks of work brought that to a factor of two.
- He then noticed that XMP needed only about 70 iterations, which he read as luck in the starting basis.
- Over the rest of the set, standata was the only model on which his code was slower.
- The 1986 hand-written results sheet confirms this: standata is the only loss among 13 models (S6 PDF p. 11; [inferred] from my reading of the sheet).

**PE-47. Instrument, then take the simplest fix.** [stated] P
- S3 p. 4: see PE-14 (bound shifting).

**PE-48. Isolate hardware effects with controlled duplicate runs.** [practice] P
- S5 p. 12: to explain poor parallel results on a SUN S20-502, the authors ran CPLEX alone and twice in parallel on the same machine. It slowed by about 40%, which points to the memory bus.
- Footnote 6: Sun let them repeat the test on its own machines. The S20-502 behaved the same; an S20-712 with a 1 MB cache per processor lost at most 20%.

**PE-49. Explain an anomaly by changing the baseline, not the claim.** [practice] P
- S5 p. 15: a superlinear speedup on aa400000 (2,864.1 s sequential against 1,300.4 s on two processors with K = 2) was traced to cache effects of the column partition: K = 2 in the sequential code alone gave 2,549.4 s.
- After "considerable testing", K was set by the same rule in both codes. The change also helped a PC (fit2d: 204.5 s down to 183.7 s).

**PE-50. What colleagues observed.** [observed] P (comments in the same newsletter)
- Grötschel (S3 p. 7): Bixby built his LP and IP codes by looking at failures, learning as he went, adapting, making small experiments and taking advice.
- Cook (S3 p. 7): when numerical results look wrong, Bixby identifies the cause rather than ignoring or working around the bad values. Cook also notes that he sleeps only a few hours a night and has an eye for detail.

**PE-51. At Gurobi: the tester who asks why.** [stated] P
- S3 pp. 4–6 (Oct 2015): he did much testing, pressed the developers about bad behaviour, ran the code constantly and complained "like I always have".

---

## 6. Judging results (layer 5)

**PE-52. Say which way each bias runs.** [stated] [practice] P
- S1 p. 5: his speedup figure relative to the IBM 3090 is surely an overestimate against MPSX, because the 3090's C compilers were weak and MPSX was hand-tuned assembler.
- S1 p. 12: the tiny 1988 netlib models probably underestimate the XMP-to-CPLEX 1.0 gap.
- S7 p. 9: scoring timeouts at the limit underestimates the gains.
- S7 p. 12 (co-authored): all the comparisons are biased against barrier, because x86 floating point is weak and the parallel barrier was not used.

**PE-53. Averages hide winners; report both.** [stated] P
- S1 p. 13: Table 15 measures only average performance. Primal, dual and barrier each win a significant number of cases, and the best of the three beats each of them by a clear margin.
- S7 p. 12: no algorithm is clearly best.

**PE-54. Drop a conclusion when new measurements contradict it.** [stated] P
- S1 p. 8: his own first conclusion was that CPLEX 1.0 could not solve degen4. He now calls it probably wrong, because the run was cut short by the cost of Cray time.
- S1 p. 8: others concluded that barrier was the right method and that simplex was not worth pursuing. He states plainly that this conclusion was wrong.
- S7 p. 12: asked in 1998 they would have said barrier was best for large models; asked in 1999/2000, no algorithm is clearly best.

**PE-55. Growth rates, not just ratios.** [practice] P
- S1 pp. 9–10: on the PDS family he fitted straight lines and parabolas by least squares.
  - CPLEX 1.0: adjusted R² 0.796 (line) against 0.994 (parabola).
  - CPLEX 7.1: 0.954 for the line.
- He read this as roughly quadratic growth for 1.0 and roughly linear for 7.1. He explained it as iterations multiplied by time per iteration, the latter now roughly constant thanks to the sparse solves.

**PE-56. Report surprises and unexplained anomalies as such.** [practice] P
- S5 p. 12: differences in iteration counts between the parallel and sequential codes were unexpected; they were traced to the reordering of columns.
- S5 p. 17: some anomalies remained unexplained, both superlinear speedups and sublinear ones on the largest aa models. They are left at a guess about R8000 cache and memory-bus behaviour.
- S4 p. 17: the starting basis helped easy problems more than hard ones, the opposite of what one would naturally expect.
- S7 p. 7: the small-model gains were "a pleasant surprise". S7 p. 10: the size of the large-model gains was unexpected.

**PE-57. A yardstick for interpreting iteration counts.** [stated] P
- S4 pp. 20–21: an iteration count close to the number of rows counts as good, because unless the optimal columns can be guessed, at least that many iterations are needed.
- On this basis stocfor3 counts as easy; greenbea, greenbeb, pilots, fit2p and pilot87 are not; and fit2d is a poor example, because of its many bound flips.

**PE-58. Answer a published benchmark claim with a counter-measurement, and later state its limits.** [stated] [practice] P/S
- 1994 commentary (S25, abstract only): in his view the results of Lustig, Marsten and Shanno somewhat overstated barrier's performance relative to simplex. He presented a view in which barrier does not dominate on large problems.
- S1 pp. 12–13 later reuse the eight models of that study (CPLEX 1.0 through 7.1). Footnote 10 notes that LMS had picked seven of them because they looked hard for simplex. He calls the set no longer large and dominated by barrier, and moves to the larger, less biased 680-model set.

**PE-59. One code measured; generality stated only as a "sense".** [stated] P
- S1 p. 4: the paper uses CPLEX throughout. He says only that he believes similar gains could be shown with other modern codes; no other code is measured.

---

## 7. Expression (layer 6)

**PE-60. Anecdotes first, then test sets; tables ordered as chronology.** [practice] P
- S1 p. 6 announces anecdotal examples first, then larger test sets.
- Table 3 (degen4) is ordered roughly as the chronology of attempts. For the record:
  - CPLEX 1.0 primal: 119,364.0 s; with perturbation: 1,545.7 s;
  - CPLEX 2.2 barrier: 125.8 s; primal: 170.2 s; primal on the explicit dual: 33.4 s;
  - CPLEX 2.2 dual with standard pricing: 102.3 s; dual default (steepest edge): 12.0 s (S1 p. 8).

**PE-61. Factors translated into everyday terms.** [practice] P
- S1 p. 14: a model that might have taken a year can now be solved in under 30 seconds.
- S6 slide 30: two months divided by 5,300,000 is about one second.
- S9 slide 9: like investing $1 at 92% annual interest for 20 years.
- S8 slide 37: today's software on a 1991 machine beats 1991 software on today's machine by about 300 times.

**PE-62. The same examples reused across two decades of talks.** [practice] P
- The production-planning run appears in the re-hosted ILOG-era deck (S16 slide 37), the 2017 ECCO deck (S8 slides 9–14) and the 2022 Hausdorff deck (S6 slides 26–29).
- The LAU2/degen4 dimensions appear in S1, S8 slide 6 and S6 slides 9 and 22.
- The 1988 LP progress numbers (3,300x algorithm, 1,600x machine) recur in S2, S16 slide 40 and S6 slide 30. S2 p. 113 and S6 slide 30 describe them as the 2002 study updated in 2004; S16 cites only the 2002 paper.

**PE-63. Credits named; history from first-hand informants.** [practice] P
- S1 p. 14: CPLEX algorithm contributors are named, and non-algorithmic contributors are credited too.
- S2 builds its 1960s–80s history on private communications and e-mail exchanges with practitioners (Shaw, Tomlin, Ashford, Gregory, Rothberg; S2 p. 118).

**PE-64. Much of the craft never written up.** [stated] [inferred] P
- S3 p. 4: there is no paper on bound shifting; he never got around to writing it.
- S4 p. 2 (1992) announced further parts of a series: Wolfe's composite simplex in Phase I, a time-saving partial pricing, a simple bound-perturbation method against stalling, vectorization and other topics.
- No later part appears among the 85 works in OpenAlex (A5012463224 plus the split record A5097662446); DBLP was not reachable. [inferred] The series was not continued.
- Short descriptions do exist: dual cost shifting in S5 p. 2, and primal shifting and perturbation in S1 p. 7.

---

## 8. Research organisation (layer 7)

**PE-65. Building the team before the code scaled.** [stated] P
- S3 p. 3: after about six months of failing to sell on his own, he recruited Janet Lowe, one of the two best students from his business-school modelling class. He gave her and her husband Todd Lowe 49% of the business, reasoning that committed people need a stake and not only a salary.
- He credits Todd Lowe with seeing that MIP was needed (S3 p. 3).

**PE-66. Collaborations formed by need: machines, platforms, people.** [stated] [practice] P
- John Gregory at Cray provided supercomputer time and the challenge models (S1 p. 8; S6 slide 22).
- The SGI partnership brought Rothberg's parallel barrier (S3 p. 3).
- A ZIB visit produced S4 (Weismantel helped translate it, S4 p. 21) and the joint work with Martin (S5).
- Sun Microsystems provided test machines (S5 fn. 6).
- Collaboration with Applegate, Chvátal and Cook on the TSP fed strong branching and the tuning of the library (S3 p. 4; S1 p. 3). Roles in the TSP work are not divided.

**PE-67. Funding and its failure.** [stated] P
- S6 PDF p. 9 (slide 10): attempts in 1987–88 to fund research in LP computation had "zero success".
- Later work was supported by NSF and AFOSR (S4 p. 1) and by NSF and Rice's CRPC (S5 p. 1).

**PE-68. Customer-use survey done himself.** [stated] P
- S3 p. 5: he classified one year's customers into about 40 application areas, putting each into a bucket himself. Supply chain came first and electrical power second.
- S8 slide 19 dates the period to Q4 2011 to Q3 2012.

---

## 9. Failures, abandoned directions and unwritten work

| # | What failed or was dropped | Evidence | Tag |
|---|---|---|---|
| F-01 | Research funding for LP computation, 1987–88: none obtained | S6 PDF p. 9 (slide 10) | [stated] P |
| F-02 | First benchmark against XMP on standata, his chosen best case: about 7 times slower; he was "crushed" (his word) | S3 p. 2 | [stated] P |
| F-03 | degen4/LAU2 with CPLEX 1.0 on a Cray: 7 hours, still infeasible and stalled; his conclusion that it could not be solved was later called probably wrong | S1 p. 8; S3 p. 3; S6 slide 23 | [stated] P |
| F-04 | Early competitive position: OSL was better until about 1992. The airlines did not switch on speed alone | S3 p. 3 | [stated] P |
| F-05 | Early CPLEX MIP was behind MINTO; the MIP part "creeping along" until Lustig, then Rothberg and Gu | S3 p. 3 | [stated] P |
| F-06 | Parallel dual simplex: the first PVM version was 3.3 times slower than sequential. Results on the S20-502 were "unexpectedly bad". The System V semaphore version was unsatisfactory. Distributed memory was judged to offer little hope except for models too large for one processor. Parallel FTRAN pairs were tried and dropped (always slower). Parallel Update-x was dropped (marginal, sometimes worse) | S5 pp. 7, 9, 11–12, 15, 17 | [practice] P |
| F-07 | The announced series of simplex papers (Phase I, partial pricing, perturbation, vectorization) was not continued | S4 p. 2; OpenAlex list | [stated] P / [inferred] |
| F-08 | Bound shifting, his self-described main contribution, was never written up | S3 p. 4 | [stated] P |
| F-09 | MIPLIB 3.0: yearly updates were promised. Six instances were added by 19 Oct 1998 (65 on the Rice page against 59 in the June 1998 note); then the page "is no longer maintained". The next MIPLIB (2003) came from Achterberg, Koch and Martin | S10 p. 12; S11; S32 | [practice] P; [inferred] |
| F-10 | An early two-processor LP attempt (1989; speedup 1.3) is relayed by Huangfu, citing an unpublished Rice report | S14 p. 72 | [observed] S, **unverified** (see Gaps) |

---

## 10. Early versus final versions, and second-hand relays checked

**V-01. The initial-basis paper.**
- The German ZIB preprint of April 1992 (S4) says on p. 21 that it was translated from English, with Robert Weismantel's help.
- An English Rice/DTIC report is dated 1991 in OpenAlex (DOI 10.21236/ada453079; not reachable). The journal version is ORSA J. Comput. 4(3):267–284, 1992 (S33; not read).
- The ORSA abstract (via OpenAlex) matches S4's: two parts of a planned series, netlib numerics, and the CPLEX initial basis.

**V-02. The parallel dual paper.**
- Preprint December 1995 (S5); journal February 2000 (S34).
- The journal abstract, read via OpenAlex, repeats the preprint's except that the Sun S20-502, where results were "unexpectedly bad", is no longer listed among the test platforms. Whether the body changed is not known, because the journal text was not read.
- [inferred] Small slip inside the preprint: p. 5 says gains need many more variables than constraints, but the conclusions (p. 20) say "ratio of rows to columns was very large".

**V-03. The 2000 MIP paper.**
- Only the ILOG preprint (S7; PDF dated 30 Mar 2000) was read; the book version (pp. 19–49) was not compared.
- Crossref lists a 2017 erratum to the volume (DOI 10.1007/978-0-387-35514-6_15). Its content was not read, and whether it concerns this chapter is unknown.

**V-04. MIPLIB 3.0.**
- Released January 1996 according to its own page (S11), but described in Optima in June 1998 (S10).
- The Optima note and S7 p. 20 count 59 models. The Rice page lists 65 by 19 Oct 1998, adding markshare1, markshare2, mas74, mas76, mkc and swath.

**V-05. The presolve paper.**
- The ZIB report is dated December 2016 (S12); the IJOC version is from 2020 (S35; not read).
- The interview of October 2015 already mentions the paper in progress (S3 p. 6).

**V-06. One talk example, edited over the years.**
- The re-hosted ILOG-era deck (S16 slide 37) lists the production-planning times as:
  - 1997 (CPLEX 5.0): 1.5 hours;
  - 2002 (CPLEX 8.0): 86.7 s;
  - 2003 (February): 59.1 s, with no version given.
- The 2017 and 2022 decks drop the 8.0 line and label the 59.1 s run "2003 (CPLEX 9.0)" (S8 slide 14; S6 slide 29). See C-12.

**V-07. The 1986 sheet against the 1988 table.**
- The 1986 sheet (S6 PDF p. 11, slide title "1st Public CPLEX Results -1986") is handwritten and headed "LOPT" against XMP, run on a Sun 3/50.
- On the 13 models it shares with the 1988 table (S1 p. 11, CPLEX 1.1 against XMP), the XMP columns agree to within small differences: gfrd-pnc is 983 iterations and 144.1 s in both. Bixby's own column improves: gfrd-pnc goes from 80.5 s (LOPT) to 43.9 s (CPLEX 1.1).
- [inferred] He kept the external baseline fixed and re-measured his own code.
- [inferred, my reading of the handwriting] On the 13 models the 1986 sheet gives a geometric mean of 1.79 times faster than XMP, an arithmetic mean of 2.00 and a ratio of totals of 2.13.

**V-08. Claims relayed in Huangfu's 2013 thesis (S14), checked against the originals.**
- (a) Thesis p. 61 relays S1 as saying that the major gain from CPLEX 5.0 to 7.1 came from more aggressive dual perturbation, especially on the PDS models. S1 p. 9 actually names three causes together: full exploitation of sparsity, more aggressive dual perturbation used as an algorithmic technique, and bound flipping. **The relay narrows the original.** The quoted fragment itself is accurate.
- (b) Thesis p. 61: Bixby gave no further detail on perturbation as an algorithmic technique. This is correct for S1, which points to a forthcoming book for the description (book not checked).
- (c) Thesis p. 71, Table 4.2, gives the Bixby–Martin speedup as between 1 and 3. Table 11 of the 1995 preprint shows 4-processor speedups from 1.1 to 5.3, the 5.3 values (aa200000, imp1) flagged as superlinear anomalies on p. 17. **The relay does not match the preprint.** The published 2000 version was not read.
- (d) Thesis p. 73: the task-parallel FTRAN pair was not used because it was slower than the combined sequential solve. This matches S5 p. 17.
- (e) Thesis p. 72: an unpublished 1989 two-processor report, speedup 1.3. Not verified (F-10).

---

## 11. Code and data artifacts (what exists to inspect)

- **No public code.** CPLEX and Gurobi are closed source. There is no repository, commit history or release log in his name, so code-level practice cannot be read off any artifact. All process evidence here comes from papers, decks, the interview and data pages.
- **Logs as evidence.** Solver logs are printed verbatim in papers and decks: CPLEX 6.5 runs in S7 pp. 23–24, and CPLEX 5.0 against 11.0 in S8 slide 27. The AA iteration log appears in S6 PDF p. 16.
- **Data artifact: MIPLIB 3.0** (S10, S11): per-instance statistics, origins, constraint classes and MPS files; the Rice page carries the history described in F-09 and V-04.
- **Proprietary names.** Test-set models were given generic names because they were proprietary: LP01–LP90 and MIP01–MIP80 in S7, M1–M82 in S16. The sets themselves were never released.

---

## Contradictions (kept, not reconciled)

**C-01. degen4/LAU2 machine, date and version.**
- S1 p. 8: first attempt in late 1989 with CPLEX 1.0 on a Cray Y-MP.
- S3 p. 3: CPLEX "1.something or maybe 2" on a Cray Y-MP.
- S6 slide 23: "1987", CPLEX 1.0, 7 hours on a Cray X-MP, stuck in Phase I.

**C-02. Did the textbook dual help on degen4?**
- S1 p. 8 and Table 3: the dual with standard (maximum-infeasibility) pricing did markedly worse than the primal on the explicit dual (102.3 s against 33.4 s).
- S6 slide 23 lists "dual simplex, with standard pricing" as getting closer still to barrier, after the explicit-dual step.

**C-03. Who said to give up on simplex for degen4.** S1 p. 8 attributes it to "some at the time". S6 slide 23 names John Gregory as recommending giving up on simplex.

**C-04. Where shifting came from.**
- S5 p. 2 (1995): Gill, Murray, Saunders and Wright (1989) are named as suggesting the dual cost shifting.
- S3 p. 4 (2015): it grew out of Paula Harris's ratio-test idea, which Bob Fourer had made him aware of, and there is no paper on it. (Short descriptions do exist: S5 p. 2, S1 p. 7.)

**C-05. How much faster than XMP, about 1986.**
- S1 p. 3: on average about two times faster on a large subset of netlib.
- S3 p. 2: within about a week, four times faster on almost all models.
- The 1986 sheet gives about 1.8 (geometric) to 2.1 (totals) [inferred]. The 1988 CPLEX 1.1 table gives a geometric mean of 4.70 (S1 p. 11).

**C-06. The size of standata.** S3 p. 2 recalls about a thousand rows and 70 XMP iterations. The 1986 sheet (S6 PDF p. 11) lists 359 rows and 75 XMP iterations [my reading].

**C-07. OR 2002, text against Table 14.**
- S1 p. 13 says the entry for models with at least 25,000 rows covers 182 models and equals 3.7.
- Table 14 shows 5.0 for that bracket and 3.7 for the bracket of models with at least 10,000 rows.
- [inferred] The 182 count matches the 25,000-row bracket (Table 13: 184 models minus 2 unsolved).

**C-08. OR 2002, the "960" chain.**
- S1 p. 13 multiplies the simplex-only chain (4.7 × 22.0 ≈ 103) by the 5.0-to-7.1 factor for models with at least 50,000 rows to get "960".
- [inferred, my arithmetic] 103.4 × 9.3 = 962 uses the best-of-three column. The best-simplex column (6.7) would give about 693.

**C-09. Documenta 2012, the LP totals.**
- S2 p. 114 tabulates machine improvement as 1600× but writes the total as "(3300 · 2000)" = 5,280,000×. The product 5,280,000 matches 3300 × 1600; 3300 × 2000 would be 6,600,000.
- S6 slide 30 and S16 slide 40 give 3,300x, 1,600x and 5,300,000x.

**C-10. The CPLEX 6.0-to-6.5 MIP jump.**
- S2 p. 117 says it exceeded a factor of 10.0, and S3 p. 4 calls 6.5 "a 10 times improvement".
- The bar in S2's own chart stands at about 9.5 [my reading of the figure], and the chart's product (≈29,000) fits about 9.5 [inferred].

**C-11. Size of the CPLEX MIP test set.**
- 1892 models: S2 p. 116.
- 1852: S8 slide 30; S13 Fig. 2 caption ("internal test set of 1,852 instances"); S15 p. 4, relaying Lodi.
- 2,791 − 559 − 348 − 22 = 1862: the arithmetic of S8 slide 30's own breakdown [inferred].

**C-12. The version label of the 59.1 s production-planning run.** "2003 (February)" with 2002 CPLEX 8.0 at 86.7 s (S16 slide 37), against "2003 (CPLEX 9.0)" (S8 slide 14; S6 slide 29).

**C-13. Gurobi 1.0 to 5.0.**
- S2 p. 118 gives 16.2. S9 slide 8 gives pairs of 2.2, 2.9, 1.3 and 1.9, cumulative 16.2.
- S8 slide 36 gives 2.2, 1.9, 1.3 and 1.7 for the same version pairs, cumulative 9.3.

**C-14. LP as a MIP blocker.** "Roughly 2%" of real-world MIPs are blocked by hard LPs (S2 p. 115; S8 slide 16). The same deck's test-set slide removes 22 "hard LP" models, 0.8% of the library (S8 slide 30).

**C-15. Company dates.**
- Amoco licence: around 1986 in S3 p. 3; the first sale to Amoco in 1987 in S6 slide 10.
- Incorporation in 1987 in S3 p. 3; "1988: Founded CPLEX optimization" in S6 slide 10.

**C-16. PDS-30 timings on near-identical machines.**
- S7 p. 4 (296 MHz Sun UltraSparc): CPLEX 1.0 57,840 s; CPLEX 5.0 (dual) 3,835 s.
- S1 Table 5 (300 MHz Sun UltraSparc): CPLEX 1.0 15,891.9 s; CPLEX 5.0 dual 1,154.9 s.
- The ratios are 3.6 and 3.3 [inferred]. Neither source explains the difference.

**C-17. Two readings of the same span, CPLEX 1.2 to 11.**
- The chained product of version-pair ratios gives 29,530 (S8 slide 31; S9 slide 7).
- A direct comparison of 1.2 with 11.0, relayed from Lodi (S30) by S15 p. 4, gives a geometric mean of 67.9 on 1,734 MILPs. On 1,852 models with a 30,000 s limit, 1.2 solved 15.0% and 11.0 solved 67.1%.
- Whose runs the direct figures are is not stated in what I read.

**C-18. Algorithm rankings on large LPs.**
- S1 Table 15 (CPLEX 7.1): for models with at least 50,000 rows, the dual/barrier time ratio is 1.4, so barrier is faster.
- S16 slide 41 (re-hosted, version and date not stated): for at least 50,000 rows, dual 1.06x faster than barrier.
- S7 p. 11 (CPLEX 6.5): dual faster than barrier by 1.2 (mean ratio) over all large models.

**C-19. Small slips in his citations.**
- S2 cites S1 as Operations Research 50(1) pp. 1–13; the actual pages are 3–15 (Crossref).
- S1 and S2 cite Marsten (1981) under a title that differs from the Crossref record ("The Design of the XMP Linear Programming Library", ACM TOMS 7:481–497).

---

## Gaps (what could not be found or verified)

**Not reached:**
- The English initial-basis paper (ORSA J. Comput. 1992) and the published parallel-dual paper (IJOC 2000). INFORMS was not retried after the 403s recorded in team.json. The German and 1995 preprints were read instead.
- The 1992 OR case study with sifting (S24): INFORMS; Rice TR91-11 sits behind an AWS WAF challenge; DTIC blocked. Its content is known only from S6 slides 14–19 and the abstract.
- The 1994 commentary (S25): INFORMS. The Rice report version of 1993 (hdl 1911/101811) sits behind the same WAF. Abstract only; its study is relayed in S1 pp. 12–13.
- Basis recovery from an interior point (S22): ScienceDirect 403; no open copy; no abstract in OpenAlex. Only his own one-line accounts of crossover exist (S3 p. 3; S6 slide 16).
- Embedded network rows, 1988 (S23): abstract only. The abstract reports comparing several heuristic implementations on realistic problems, and notes that the effectiveness of simpler and costlier variants was hard to explain.

**Not read, no open copy found:**
- The 2004 Progress Report (S26; known only through the S15 relay).
- The 2007 Bixby–Rothberg paper (S27).
- The 1999 parallel MIP paper (S28).
- The 1992 MIPLIB test-set report (S29; DTIC blocked).
- Lodi's 2009/2010 chapter (S30).
- Achterberg and Wunderling (S31).

**Not found:**
- The 2004 update of the LP progress study, cited in S2 p. 113 and on S6 slide 30. No paper or deck with that update was found.
- How the "2%" figure for MIPs blocked by LP (S2 p. 115) was measured; no method is given.
- Talks: no trace of a 2013 Tutte Colloquium talk. The Imperial talk of 13 May 2015 exists only as an event listing (S17), with no deck. The ECCO 2017 deck (S8) is the closest dated MIP deck.
- No dedicated document on bound shifting or perturbation (stated as never written, S3 p. 4).

**Gurobi and later:**
- Gurobi's internal test protocol is known only from co-authored papers (S12, S13) and his interview. Who ran the Gurobi version comparisons (S2 p. 118; S8 slide 36) is not stated beyond "we".
- The CPLEX 12.x extension in S13 (55,000x up to 12.2) postdates his time at CPLEX. Who measured it is not stated, so it is not used as his practice.

**Unverified lead:** the 1989 Rice report with M. Schwabacher on two-processor LP, cited only by S14 p. 72 (ref. [6]). No identifier could be checked, so it is not used as evidence.

**Hosting and provenance:**
- S16 is a 2024 re-host on a third-party slide site. Its original venue and date are not stated on the slides read (a related entry on the same page names 15 September 2003 and Ed Rothberg). It is used only for comparisons and never for an authorship label.
- DBLP (pid 75/1779) could not be read (Anubis "access denied"). The publication list rests on OpenAlex.

**Not applicable:** OpenReview, rebuttals and public review histories do not exist for this era and these venues. No errata were found for S1 or S2.

**Not addressed:** living status and present role, deliberately (team.json).

---

## Sources

| # | Title · author · date · location | Use | P/S |
|---|---|---|---|
| S1 | "Solving Real-World Linear Programs: A Decade and More of Progress" · R. E. Bixby · Operations Research 50(1):3–15, 2002 · DOI 10.1287/opre.50.1.3.17780 (read via www.gwern.net/doc/cs/algorithm/2002-bixby.pdf) | read in full | P |
| S2 | "A Brief History of Linear and Mixed-Integer Programming Computation" · R. E. Bixby · Documenta Math. Extra Vol. ISMP (2012) 107–121 · DOI 10.4171/dms/6/16 (read via www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-ismp/25_bixby-robert.pdf) | read in full | P |
| S3 | "You have to figure out who your customer is going to be – An interview with Bob Bixby" (questions Oct 2015, Oberwolfach; Kaibel, Lee, Linderoth), with comments by M. Grötschel and W. Cook · Optima 101, Sept 2016, pp. 1–7 · mathopt.zib.de/Optima-Issues/optima101.pdf | read in full | P (interview); observed (comments) |
| S4 | "Das Implementieren des Simplex-Verfahrens: Die Startbasis" · R. E. Bixby · ZIB Preprint SC 92-11, April 1992 · opus4.kobv.de/opus4-zib/files/81/SC-92-11.pdf | read in full (German, OCR) | P |
| S5 | "Parallelizing the Dual Simplex Method" · R. E. Bixby, A. Martin · ZIB Preprint SC-95-45, Dec 1995 · opus4.kobv.de/opus4-zib/files/211/SC-95-45.pdf | read in full | P |
| S6 | "Linear Programming: A Historical View" · R. E. Bixby · deck, Hausdorff School on Computational Combinatorial Optimization, Bonn, Sept 2022 · www.or.uni-bonn.de/~held/hausdorff_school_22/slides/GUR_Hausdorff_Day1_LP_History.pdf | read in full | P |
| S7 | "MIP: Theory and Practice — Closing the Gap" · R. E. Bixby, M. Fenelon, Z. Gu, E. Rothberg, R. Wunderling · in System Modelling and Optimization (IFIP TC7), Kluwer 2000, pp. 19–49 · DOI 10.1007/978-0-387-35514-6_2 (read as the ILOG preprint mirrored at miplib2010.zib.de/miplib2003/paper/bixbyfenelongurothbergwunderling2000.pdf) | read in full | P (co-authored) |
| S8 | "Computational Progress in Linear and Mixed Integer Programming" · R. E. Bixby · ECCO 2017 invited lecture deck, 5 May 2017 · ecco2017.euro-online.org/en/resources/files/invited-speakers/robertbixby.pdf | read in full | P |
| S9 | "1000X MIP Tricks" · R. E. Bixby · deck, 12 June 2012, Bill Cunningham's 65th (Fields Institute) · av.fields.utoronto.ca/programs/scientific/11-12/bc65/rbixby.pdf | read in full | P |
| S10 | "An Updated Mixed Integer Programming Library: MIPLIB 3.0" · R. E. Bixby, S. Ceria, C. M. McZeal, M. W. P. Savelsbergh · Optima 58, June 1998, pp. 12–15 · mathopt.zib.de/Optima-Issues/optima58.pdf | read | P (co-authored) |
| S11 | MIPLIB 3.0 web pages (miplib.html, miplib3.html, miplib_prev.html) · Rice, maintained by C. McZeal · dated Jan 1996, last updated 19 Oct 1998 · www.cmor-faculty.rice.edu/~bixby/miplib/ | read | P (data artifact) |
| S12 | "Presolve Reductions in Mixed Integer Programming" · T. Achterberg, R. E. Bixby, Z. Gu, E. Rothberg, D. Weninger · ZIB-Report 16-44, Dec 2016 · opus4.kobv.de/opus4-zib/files/6037/Presolve.pdf | §1.1 and parts of the results read | P (co-authored) |
| S13 | "MIPLIB 2010" · T. Koch, T. Achterberg, … R. E. Bixby, … K. Wolter (16 authors) · ZIB-Report 10-31 (2011) · opus4.kobv.de/opus4-matheon/files/969/miplib5.pdf | §1, Fig. 2, §5.3 read | P (co-authored, collective) |
| S14 | "High performance simplex solver" · Q. Huangfu · PhD thesis, University of Edinburgh, 2013 · era.ed.ac.uk/handle/1842/7952 | pp. 61, 63, 71–73 read | S |
| S15 | "Progress in Mathematical Programming Solvers from 2001 to 2020" · T. Koch, T. Berthold, J. Pedersen, C. Vanaret · ZIB-Report 21-20, Jan 2022; EURO J. Comput. Optim. 10:100031, 2022 · DOI 10.1016/j.ejco.2022.100031 | §1.1 and §3 (part) read | S |
| S16 | "Solving Linear and Integer Programs" · R. E. Bixby (ILOG and Rice) · deck re-hosted 5 Mar 2024 at api.sambuz.com/doc/solving-linear-and-integer-programs-ppt-presentation-841245; original venue and date not stated | slides 37–41 read | S (third-party host; provenance not established) |
| S17 | Seminar "Computational Progress in Linear and Mixed Integer Programming" · R. Bixby (Gurobi) · 13 May 2015 · optimisation.doc.ic.ac.uk/events/2015-05-13 | listing read | observed |
| S18 | Hausdorff School on Computational Combinatorial Optimization, 12–16 Sept 2022, programme and slides page · www.or.uni-bonn.de/~held/hausdorff_school_22/ | read (one Bixby deck listed) | observed |
| S19 | OpenAlex records: authors A5012463224 (84 works) and A5097662446 (1 work), and abstracts of DOIs 10.1287/ijoc.6.1.15, 10.1287/opre.40.5.885, 10.1287/mnsc.34.3.342, 10.1137/1.9780898718805.ch18, 10.1287/ijoc.12.1.45.11902, 10.1287/ijoc.2018.0857 · queried 2026-11-05 | metadata, abstracts | S |
| S20 | Crossref API records for every DOI in this table and in the list below · queried 2026-11-05 | identifier checks | S |
| S21 | Unpaywall and Semantic Scholar API checks for open copies (none, except a Rice TR link for S24 that leads to a WAF-protected repository) · 2026-11-05 | access checks | S |
| S22 | "Recovering an optimal LP basis from an interior point solution" · R. E. Bixby, M. J. Saltzman · Oper. Res. Lett. 15(4):169–178, 1994 · DOI 10.1016/0167-6377(94)90074-4 | not read | P (not read) |
| S23 | "Finding Embedded Network Rows in Linear Programs I. Extraction Heuristics" · R. E. Bixby, R. Fourer · Management Science 34(3):342–376, 1988 · DOI 10.1287/mnsc.34.3.342 | abstract only | P (abstract) |
| S24 | "Very Large-Scale Linear Programming: A Case Study in Combining Interior Point and Simplex Methods" · R. E. Bixby, J. W. Gregory, I. J. Lustig, R. E. Marsten, D. F. Shanno · Operations Research 40(5):885–897, 1992 · DOI 10.1287/opre.40.5.885 | abstract only | P (abstract) |
| S25 | "Commentary—Progress in Linear Programming" · R. E. Bixby · ORSA J. Comput. 6(1):15–22, 1994 · DOI 10.1287/ijoc.6.1.15 | abstract only | P (abstract) |
| S26 | "Mixed-Integer Programming: A Progress Report" · R. E. Bixby, M. Fenelon, Z. Gu, E. Rothberg, R. Wunderling · The Sharpest Cut, MPS-SIAM 2004, pp. 309–325 · DOI 10.1137/1.9780898718805.ch18 | abstract; relayed by S15 | P (not read) |
| S27 | "Progress in computational mixed integer programming—A look back from the other side of the tipping point" · R. E. Bixby, E. Rothberg · Annals of OR 149(1):37–41, 2007 · DOI 10.1007/s10479-006-0091-y | not read | P (not read) |
| S28 | "Computational experience with parallel mixed integer programming in a distributed environment" · R. E. Bixby, W. Cook, A. Cox, E. K. Lee · Annals of OR 90:19–43, 1999 · DOI 10.1023/a:1018960631213 | not read | P (not read) |
| S29 | "A Test Set of Real-World Mixed Integer Programming Problems" · R. E. Bixby, E. A. Boyd, R. R. Indovina · 1992 report · DOI 10.21236/ada455431 | not read (DTIC blocked) | P (not read) |
| S30 | "Mixed Integer Programming Computation" · A. Lodi · in 50 Years of Integer Programming 1958–2008, pp. 619–645 (Crossref issue year 2009) · DOI 10.1007/978-3-540-68279-0_16 | not read; relayed by S15 | S |
| S31 | "Mixed Integer Programming: Analyzing 12 Years of Progress" · T. Achterberg, R. Wunderling · Facets of Combinatorial Optimization, 2013, pp. 449–481 · DOI 10.1007/978-3-642-38189-8_18 | not read; cited by S12, S15 | S |
| S32 | "MIPLIB 2003" · T. Achterberg, T. Koch, A. Martin · Oper. Res. Lett. 34(4):361–372, 2006 · DOI 10.1016/j.orl.2005.07.009 | metadata (dates the next MIPLIB) | S |
| S33 | "Implementing the Simplex Method: The Initial Basis" · R. E. Bixby · ORSA J. Comput. 4(3):267–284, 1992 · DOI 10.1287/ijoc.4.3.267 | not read (English version of S4) | P (not read) |
| S34 | "Parallelizing the Dual Simplex Method" · R. E. Bixby, A. Martin · INFORMS J. Comput. 12(1):45–56, 2000 · DOI 10.1287/ijoc.12.1.45.11902 | abstract only (journal version of S5) | P (abstract) |
| S35 | "Presolve Reductions in Mixed Integer Programming" · Achterberg, Bixby, Gu, Rothberg, Weninger · INFORMS J. Comput. 32(2):473–506, 2020 · DOI 10.1287/ijoc.2018.0857 | journal version not read (S12 read) | P (co-authored) |
| S36 | "MIPLIB 2010" · Koch et al. · Math. Prog. Comp. 3(2):103–163, 2011 · DOI 10.1007/s12532-011-0025-9 | journal version not read (S13 read) | P (co-authored) |

**Works he cites, identifiers checked with Crossref (2026-11-05), not sources about him:**
- Forrest & Goldfarb, Math. Programming 57:341–374, 1992, DOI 10.1007/BF01581089.
- Gilbert & Peierls, SIAM J. Sci. Stat. Comput. 9(5):862–874, 1988, DOI 10.1137/0909058.
- Gill, Murray, Saunders & Wright, Math. Programming 45:437–474, 1989, DOI 10.1007/BF01589114.
- Harris, "Pivot selection methods of the Devex LP code", Math. Programming 5:1–28, 1973, DOI 10.1007/BF01580108.
- Lustig, Marsten & Shanno, ORSA J. Comput. 6:1–14, 1994, DOI 10.1287/ijoc.6.1.1.
- Sharda & Somarajan, Computers & OR 13:131–147, 1986, DOI 10.1016/0305-0548(86)90004-3.
- Grötschel & Holland, Math. Programming 51:141–202, 1991, DOI 10.1007/BF01586932.
- Carolan, Hill, Kennington, Niemi & Wichmann, Operations Research 38(2):240–248, 1990, DOI 10.1287/opre.38.2.240.
- Castro, SIAM J. Optim. 10:852–877, 2000, DOI 10.1137/S1052623498341879.
- Marsten, ACM TOMS 7:481–497, 1981, DOI 10.1145/355972.355976.
- Lustig, Computers & OR 16:173–184, 1989, DOI 10.1016/0305-0548(89)90018-X.
- Suhl & Suhl, "Computing Sparse LU Factorizations for Large-Scale Linear Programming Bases", ORSA J. Comput. 2(4):325–335, 1990, DOI 10.1287/ijoc.2.4.325.
