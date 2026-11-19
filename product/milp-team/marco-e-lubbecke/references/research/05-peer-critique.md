# Marco E. Lübbecke: Peer Critique (blind spots, limits, contested judgements)

| Field | Value |
|---|---|
| Researcher | Marco E. Lübbecke, RWTH Aachen University (Chair of Operations Research) and GERAD. Lens (team.json): decomposition inside MILP solver engineering: column generation, Dantzig-Wolfe (DW) reformulation, branch-and-price (B&P) and the GCG solver. His applications (timetabling, railways, recoverable robustness) appear only where critics took them up. He is a living researcher, so only public academic output is used |
| Dimension | Research agent 05 of 06: peer critique. Covers benchmark studies that measure GCG or his B&P codes against rivals, published comments and replies, corrections to his texts, rival schools, predictions, and how each was answered |
| Research date | 2026-11-08 |
| Sources consulted | 52 (22 primary, 30 secondary), listed under "Sources" |
| WebSearch calls | 3 (of 5 allowed) |
| User-supplied material | None. `references/sources/{papers,essays,software,publications}/` hold only `.gitkeep`. `talks/` holds four caption transcripts that research agent 02 saved earlier in this run; they are not user-supplied. One of them is used here and flagged "(caption)" [S51]. `private/` was not opened. **Nothing in this file is from user-supplied material** |
| Transcripts saved | None by this agent. Downloaded papers stayed in the scratch folder and were not copied into `references/sources/` |
| Language | English (team.json) |

**Tags.**
- [stated]: said or written by Lübbecke, or in a text he co-signed. A co-signed text is marked "co-signed". The 2026 book has four authors, so no passage in it is his alone.
- [practice]: what his papers, code, documentation or records show was done. GCG is the RWTH group's code (see the caveats below).
- [observed]: what a third party wrote. Co-authors and close collaborators are flagged.
- [inferred]: my reading, with its basis given. Do not quote it as anyone's view.
- (P) primary: read in the critic's or the Lübbecke-side text at the page cited.
- (S) secondary: abstract or metadata only, a figure relayed by another author, or a Semantic Scholar citation context. The last kind is marked "S2 context; full text not read".
- Caption transcripts are speech recognition and were not checked against the audio. They are paraphrased with timestamps and never quoted.

**How the critiques were found.**
1. Publication landscape: the OpenAlex author record found by ORCID (A5082694588, 100 works), Crossref, and the zbMATH Open API (54 documents). zbMATH has one signed review, P. Brucker's of the 2001 thesis; all other entries carry author summaries only [S48].
2. Citation contexts: the Semantic Scholar Graph API returned contexts for 31 of his works (3,057 citing records, 1,715 of them with contexts). I filtered these for critical wording ("however", "fail", "outperform", "incorrectly", "not competitive", "drawback" and similar) [S47].
3. I opened every critic named below in a legal open copy: arXiv, publisher open access, institutional repositories (Bologna, Lancaster, TU Berlin DepositOnce, and a CONTENTdm repository linked by Semantic Scholar), INRIA RADAR and the GERAD cahier. The exceptions are marked (S).
4. Code: the GCG repository `scipopt/gcg` at commit `c0e230a` (2026-07-27): `CHANGELOG`, `README.md`, `doc/resources/users/why-gcg.md` and the file list under `src/gcg/` [S8]. The GitHub issue list of this mirror came back empty.
5. Identifiers were checked against Crossref, Unpaywall (email parameter nuwa-skill@users.noreply.github.com), OpenAlex and the arXiv API. A Crossref query for errata or corrections to his works found none; the one hit was a correction to a paper by the oceanographer Joke F. Lübbecke.
6. Not reached, and not routed around:
   - bot checks: DBLP, HAL and UWSpace sit behind an Anubis proof-of-work check, and DTU Orbit's file server behind a Cloudflare challenge;
   - restricted copy: the Milan repository serves its copy only on request;
   - timeouts: `or.rwth-aachen.de`, `www.or.rwth-aachen.de` and `gcg.or.rwth-aachen.de` timed out, also through WebFetch;
   - other failures: the Exeter repository returned an empty response, and the GitHub API hit its rate limit on the shared IP.

   web.archive.org was not used. Closed Springer, INFORMS, Elsevier, Wiley and Taylor & Francis texts were not read; they are listed under Gaps.

**Attribution caveats that must survive into the skill.**
- **GCG is group code.** The 2026 book credits Gerald Gamrath with the original "two communicating trees" design. It names as major contributors Martin Bergner, Michael Bastubbe, Christian Puchert, Jonas Witt, Steve Maher, Erik Mühmer "and many more", and says Lübbecke is "the one with the vision who keeps it all together" ([S4] p. 538). His author note says he has led the effort to build a decomposition-based solver since 2008, and that he was on the first team ever to use SCIP's column-generation capabilities, in version 0.81 ([S4] p. vi). **A benchmark of GCG measures one version of the group's code, built with one LP solver and run in one detection mode. It does not measure his personal programming.**
- **Co-signed texts, roles not divided:**
  - Selected Topics (with Desrosiers) [S2];
  - Villeneuve et al. (four authors) [S3];
  - Bergner et al. 2015 (seven authors) [S11];
  - Lach and Lübbecke [S6, S7];
  - Kruber et al. (three authors) [S5];
  - Bastubbe and Lübbecke [S10];
  - Liebchen et al. (four authors) [S13];
  - the 2026 book (four authors) [S4];
  - the 2026 k-vertex-cut preprint (four authors) [S9].
- **Critics who are close to him** (co-authorship checked against his OpenAlex works list):
  - Alberto Ceselli co-authored Bergner et al. 2015 and also signs [S32, S33].
  - Fabio Furini and Enrico Malaguti co-authored Bergner et al. 2015 and sign [S31]; Furini also co-signs the 2026 preprint [S9].
  - Stephen J. Maher has six co-authored works with him and is a GCG contributor [S38].
  - Sebastian Stiller co-authored the 2009 recoverable-robustness paper [S13] and is an author of [S39].
  - Clausen, Lusby and Røpke thank Lübbecke for comments ([S28] p. 39).
  - Uchoa and Sadykov thank him for a reference ([S40] p. 452).
  - The Bordeaux EDGE team (Vanderbeck, Sadykov, Pessoa, Uchoa and others) is a rival school but a friendly one: the book calls Vanderbeck a good friend of Jacques, Marco, Guy, Eduardo and others ([S4] p. 627).
- **No co-authorship found** in his OpenAlex list: Chen, Günlük and Lodi; Yıldız, Boland and Savelsbergh; Weiner, Ernst, Li and Sun; Khaniyev, Elhedhli and Erenay; Rambau and Schwarz; Phillips et al.; Bettinelli, Cacchiani, Roberti and Toth; Shu and Song.

---

## 0. Summary for Phase 2

| # | Recurring critique (blind spot / limit) | Raised by | Lübbecke-side answer | Status |
|---|---|---|---|---|
| Q1 | **Generic branch-and-price does not compete with branch-and-cut on general MIPs.** Critics call it "in their infancy", say it "cannot compete", and find it "rarely competitive" | Chen-Günlük-Lodi [S27]; Clausen-Lusby-Røpke [S28] (they thank him); INRIA EDGE reports 2022-2025 [S29]; Basso-Ceselli [S32], who find results "mixed" on average (Ceselli is a co-author); Hansknecht et al. [S39] (S) | The claim has narrowed. The GCG documentation says that without structure a decomposition can hurt performance [S8]. Kruber et al. say the solver "may completely fail" and that DW pays off on a small fraction of MIPs [S5]. The 2026 book says success hinges on finding a good decomposition, and presents GCG as a cheap first test before any implementation ([S4] pp. 238, 509) | Conceded in scope. The disagreement about the long-run promise persists |
| Q2 | **Automatic structure detection is fragile, slow or badly ranked** | Basso-Ceselli-Tettamanzi [S33] (S); Basso-Ceselli [S32] (crashes; data-driven decompositions better in about 23% of root-node cases, GCG's in about 10%); Yıldız-Boland-Savelsbergh [S30] (automatic detection "significantly worse" than supplying the structure); Khaniyev [S35] (S) (the number of blocks must be fixed in advance); Weiner et al. [S34] (ML rankers beat the RBA score and GCG's own score); Clausen et al. [S28] (only 2-10 blocks were tested) | Kruber et al. learn whether to decompose and which decomposition to use [S5]. The book warns that a good-looking decomposition is not the same as structure, and that randomly grouping constraints gives poor bounds ([S4] pp. 237-238) | Partly answered. No published reply to the crash reports was found |
| Q3 | **Solving pricing problems as generic MIPs is not competitive; specialized pricing is needed** | Rambau-Schwarz [S36] (S); EDGE [S29]; Kim-Dandurand [S37] (S); Maher [S38] (S, a colleague, about Benders structure) | The book says tailoring the pricing "may even be necessary" ([S4] p. 509) and also recommends other frameworks, VRPSolver and BaPCod (p. 538) | Conceded |
| Q4 | **Rival exact methods beat his group's B&P on chosen problem classes** | Yıldız et al. [S30]: decomposition branching more than 40 times faster than GCG on many instances. Furini et al. [S31]: branch-and-cut beats the Bastubbe-Lübbecke B&P on 2 of 4 classes, ties on 1 and loses on Random. Chen et al. [S27]: the DW bound is reached with cuts, with no B&P needed | The 2026 preprint "Branch-and-price strikes back" (for the k-vertex cut problem), co-signed with the critic Furini [S9] | Problem-dependent; the contest is ongoing |
| Q5 | **Historical misattribution**: the weak cutting-stock formulation was credited to Kantorovich | Uchoa-Sadykov 2026 [S40] | He pointed them to the earlier source, Eilon-Christofides 1971 ([S40] p. 452). The 2026 book adopts the correction ([S4] p. 91) | Corrected |
| Q6 | **Timetabling.** Four points: the competition benchmark is abstracted from practice; only one quality measure is used; room stability breaks the exactness of the two-stage split; and the case for B&P is disputed | Phillips et al. [S21]; the Bettinelli et al. overview [S17] (S) and their rejoinder [S16]; Ozkan et al. [S25] (S); Burke et al. [S22] (S) | His 2015 comment concedes the gap between theory and practice and the trouble with weighted objectives, and calls his own pro-B&P view possibly "personally biased" [S1] | On the practice gap, the two sides converged. On B&P, the rejoinder disagrees |
| Q7 | **Lübbecke as critic**: published comparisons run on unequal machines, time limits and solvers | Lübbecke [S1] | Bettinelli et al. agree in principle [S16]. Later comparisons against his own B&P still borrow numbers from his tables [S31] | Accepted in principle; practice unchanged [inferred] |
| Q8 | **Recoverable robustness**: limits of LP recovery, a delay cost based on the worst case, and a rival model | Shu-Song [S41] (S); Dewilde et al. [S42] (S); Cicerone et al. [S43] (S) | None found | Open |
| Q9 | **Row-reduced column generation may make the pricing problems harder** | Costa et al. [S44] (S) | None found | Open (minor) |
| Q10 | **2004-2005 claims and open questions**: generic integer column-generation codes solve problems that commercial MIP solvers could not; bundle and ACCPM methods "still to be evaluated" in integer programming; basic dual solutions are bad representatives | The 2020s verdicts in Q1; Briant et al. 2008 [S46] (not read); Bredström et al. [S45] (S) | The 2026 book is more guarded ([S4] pp. 238, 509) | Tension [inferred]. "Generic" may not mean the same thing in 2004 and in the 2020s |
| Q11 | **Failures on record**: wrong-result bugs, disabled features, crashes, a desk rejection | The GCG CHANGELOG and documentation [S8]; Basso-Ceselli [S32]; his podcast interview [S51] (caption) | Fixed in later releases; he tells the rejection story himself | Record |

**Where the critiques land in the seven layers (framework §一)** [inferred grouping]

| Layer | What the critiques bear on | Items |
|---|---|---|
| 1 Taste | What counts as "structure"; the attraction of well-drawn bordered decompositions (his own book warns against it); generality as the goal; fair comparison as a value he applies to others | Q1, Q2, Q7 |
| 2 Problem choice | Automatic DW for any MIP, versus problem classes with a pricing routine that already works well; benchmark timetabling versus real timetabling | Q1, Q3, Q6 |
| 3 Idea generation | Moving DW from hand-built codes into a generic solver; machine learning for deciding when to decompose; reading the timetabling two-stage split as Benders decomposition | Q2, Q6 |
| 4 Experiments | What the critics' GCG benchmarks fix: the GCG version (3.0.x or earlier), the LP solver (often CPLEX), automatic versus user-supplied structure, test sets chosen to suit the critic's method, numbers borrowed from his tables | Q2, Q4, §1 |
| 5 Judging results | "Personally biased" (his own words); the 2004 "success story"; the abstracts' hedging ("may completely fail"); when he accepts a correction | Q1, Q5, Q6, Q10 |
| 6 Expression | Historical attribution; a documentation claim backed by a single example log; titles that promised more than the abstract ("Optimal Solutions" in 2008, "new solutions" in 2012) | Q5, Q6, Q11 |
| 7 Organisation | 15+ years of group software; critics drawn from his own co-author network; a rival school that answers in its annual activity reports | Q1, Q4, caveats |

---

## 1. Era and resource context

- **2001, PhD (TU Braunschweig).** The zbMATH review describes a price-and-branch method: column generation at the root, then an integer phase, not B&P throughout the tree. The method handled instances with 35 transportation requests and six engines [S15]. [observed, P (review text)]
- **2003-2008, TU Berlin.** The column-generation surveys first appeared as TU Berlin Institut für Mathematik reports 2003/25 and 2004/08, co-signed with Desrosiers (GERAD) and others [S2, S3]. The timetabling work used an integer program solved with CPLEX [S6]. In 2015 he wrote that the overview inspired him to look into "our old code, install a fresh CPLEX" and see what was possible ([S1] p. 361). [practice; stated]
- **2008 onward, GCG.** The solver is built on SCIP, and the work is done by a group ([S4] pp. vi, 538). The critics ran these builds:
  - Rambau and Schwarz used a "pre-release version" [S36] (S2 context);
  - Basso and Ceselli ran GCG 2.1.1 for their simulations and GCG 3.0.1 with CPLEX 12.6.3 and SCIP 7.0.0 on a quad-core i7-6700K with 32 GB, with a 2 h limit at the root and 5 h for full runs ([S32] pp. 167-168, 171, 176);
  - Yıldız et al. ran GCG from the SCIP Optimization Suite 7.0, compiled with CPLEX as the LP solver, with default settings and their own block structure supplied, on a Xeon Gold 6134 ([S30] p. 16);
  - Furini et al. did not re-run the B&P; they took its numbers from the Bastubbe-Lübbecke tables, on a "comparable" i7 at 3.40 GHz with a 30-minute limit ([S31] p. 31).

  [practice of the critics]
- **2026.** The Branch-and-Price book: 663 pages, four authors, published open access (GERAD G-2024-36, June 2024, revised January 2026) [S4].
- [inferred] No benchmark found in this search ran a GCG release later than 3.0.x, and no critic re-measured a 2020s release (the CHANGELOG reaches 5.0 [S8]). Every verdict in Q1-Q4 is therefore tied to code of roughly 2020 or earlier, to one LP solver build and to one detection mode.

---

## 2. Generic branch-and-price against branch-and-cut on general MIPs (Q1)

### 2.1 What critics said [observed]
- **Chen, Günlük and Lodi** ([S27], arXiv v2 2023, p. 2; Operations Research 2025) (P).
  - They list generic B&P solvers, among them GCG (citing Gamrath and Lübbecke 2010), as "still in their infancy with respect to solving general MIPs with block structure".
  - Their alternative stays inside standard branch-and-cut. They run column generation only at the root and derive cutting planes that recover the DW bound in the original variables.
  - They tested on multiple-knapsack-assignment and temporal-knapsack instances with Gurobi and did not run GCG.
  - They are independent of his co-author network.
- **Clausen, Lusby and Røpke** ([S28], arXiv v1 2021, p. 33) (P).
  - They call solving generic MIPs by DW a direction that is "still in its infancy", naming Bergner et al. 2015 among the notable contributions.
  - They state that automatic-detection methods "cannot compete with state-of-the-art branch-and-cut solvers".
  - They thank Lübbecke for comments (p. 39).
- **INRIA EDGE project team, Bordeaux** ([S29], activity reports 2022, 2023, 2024 and 2025, §3.1 "Decomposition methods") (P).
  - Their numerical experience is that generic branch-cut-and-price with the subproblems solved as generic MIPs is "rarely competitive with the traditional branch-and-cut method". The works cited for this are Galati 2009 (DIP) and Gamrath and Lübbecke 2010 (GCG).
  - They add that specialized branch-cut-and-price codes are efficient but rarely used in practice because they are hard to implement.
  - The full sentence was read in the 2022 report. In the 2023, 2024 and 2025 reports I confirmed only that the phrase "rarely competitive" and the Gamrath-Lübbecke citation are present.
  - This is the rival school (BaPCod, Coluna, VRPSolver).
- **Basso and Ceselli** ([S32], Mathematical Programming Computation 2023, p. 155) (P).
  - They call Bergner et al. 2015 an "unexpected but fundamental result": detectors plus a generic decomposition solver beat a commercial solver on a subset of MIPLIB.
  - They then add: "On average, however, computational results are mixed."
  - Ceselli co-authored Bergner et al. 2015.
- **Hansknecht et al.** ([S39], EJOR 2023) (S2 context; full text not read).
  - Despite progress on generic column generation, they say, problem structure "cannot generally be automatically recognized", so integer-programming software must be adapted to each problem.
  - Stiller, one of the authors, is a former co-author of Lübbecke's.

### 2.2 The Lübbecke-side position [stated]
- **The aim.** In the 2021 interview he says the B&P idea started in his Berlin years. Cutting planes already run inside branch-and-cut without the user knowing; the goal was to make DW decomposition and B&P happen the same way, as a commodity. Structure detection was the missing piece, and he names automatic DW reformulation as maybe his favourite line of work ([S51] 0:52:16-0:53:20, caption, paraphrased).
- **The GCG documentation** ([S8], `why-gcg.md` at `c0e230a`; group text) [practice/stated].
  - It promises to solve problems "without requiring any input or knowledge from your side".
  - It concedes that if a problem has no structure at all, "it can be detrimental to performance to try to use a decomposition anyways".
  - With structure, it says there is a "good chance" that GCG solves the problem much faster than SCIP, and often at least as fast as Gurobi or CPLEX.
  - The evidence on the page is one pair of example logs, next to the line "@todo add performance profile between SCIP and GCG".
  - The README says GCG can solve "(potentially) structured MIPs faster".
- **Kruber, Lübbecke and Parmentier 2017** [S5] (co-signed).
  - The abstract, read on the IP Paris portal, says that if the detected structure does not match the model's real structure, "the solver may completely fail".
  - It reports a significant gain on structured instances, with little loss on the others.
  - A Semantic Scholar context from the paper itself says that DW will pay off in solver performance "only on a small fraction of MIPs" (S2 context; full text not read).
- **The 2026 book** [S4] (co-signed, four authors).
  - "in principle, branch-and-price is a general method to solve general MILPs", and whether it succeeds "hinges, in particular, on the question whether we find a good decomposition" (p. 238).
  - An implementation "may turn out to be fruitless in the end". One motivation of GCG is to estimate the chance of success before anyone writes a dedicated code, and tailoring, such as a specialized pricing solver, "may even be necessary" (p. 509).

### 2.3 Reading [inferred]
- The critics measure GCG as a general-purpose rival to branch-and-cut. Since 2017 the Lübbecke-side texts claim something narrower:
  - a solver to try first;
  - a way to predict whether a dedicated B&P code is worth writing;
  - a reformulation that a learned classifier switches on.
- No printed reply to Chen et al., to Clausen et al. or to the EDGE statement was found. The answer is the narrowed claim itself.

---

## 3. Structure detection: fragile, slow, badly ranked (Q2)

### 3.1 What critics said [observed]
- **Basso, Ceselli and Tettamanzi** ([S33], Annals of OR 2020) (S2 context; full text not read: HAL is behind a bot check and the Milan copy is request-only).
  - On perturbed copies of `p2756.mps`, "GCG detectors fail to provide a solution for most perturbations".
  - On `rout.mps`, GCG finds slightly better bounds, but only after hours; random decompositions reach comparable bounds in seconds.
- **Basso and Ceselli** ([S32]) (P).
  - Crashes: GCG with all detectors switched on "would crash with all the available detectors enabled". They had to switch off three detectors (dbscan, constype and compgreedily), and some decompositions crashed GCG "for undocumented internal reasons after few minutes" (p. 171).
  - Missing border: some of the decompositions GCG detected had no border (no linking constraints), so their local search could not modify them (p. 171).
  - Root node: in about half the instances both detectors give the same bound; data-driven detection is better in about 23%, GCG in another 10% (p. 175).
  - Full 5 h runs: the data-driven framework obtains better bounds in about 37% of the experiments, and GCG in 10% (p. 177).
  - Ceselli co-authored Bergner et al. 2015.
- **Yıldız, Boland and Savelsbergh** ([S30], Operations Research 2022; open manuscript, p. 16) (P).
  - Letting GCG detect the structure itself "resulted in significantly worse performance" than telling it which constraints link the blocks. This held even on an instance class with a single linking constraint.
  - On p. 2 they also speculate that Bergner et al.'s detectors may have found a different structure on some MIPLIB instances than the one with few linking constraints that they were looking for.
- **Khaniyev, Elhedhli and Erenay** ([S35], INFORMS JoC 2018, and Khaniyev's 2018 Waterloo thesis) (S2 context; full texts not read).
  - The main disadvantage they see in graph-partitioning detectors, Bergner et al.'s included, is "the need to specify the number of partitions beforehand".
  - Their own method uses community detection with a modularity-based quality score.
- **Clausen, Lusby and Røpke** ([S28] p. 34) (P).
  - Bergner et al. examined decompositions with 2 to 10 blocks.
  - Clausen et al. add 20 and 50 blocks, because many small blocks worked for the temporal knapsack problem.
- **Weiner, Ernst, Li and Sun** ([S34], arXiv v1 2022; EURO J. Comput. Optim. 2023) (P).
  - On Kruber et al.: the approach "only helps to address whether or not a decomposition approach may be appropriate", not which decomposition to choose (p. 2).
  - In a ranking benchmark on 14 instances (score 0 for the best decomposition, 1 for the worst), the average scores were:
    - Bergner et al.'s relative border area: 0.283;
    - the score from GCG's source code: 0.284;
    - a random forest: 0.112;
    - a voting ensemble: 0.119.

    (p. 15)
  - Their conclusion: ML "can significantly outperform current benchmark heuristic methods" (p. 21).
  - [inferred] Caveat: the yardstick is the quality of a Lagrangian relaxation, and GCG's score was lifted from its code to rank decompositions with linking constraints only. It is being judged outside the job it was written for.

### 3.2 The Lübbecke-side answer [stated]
- Kruber et al. 2017 [S5] answer the "whether" question with supervised learning. Weiner et al. say it leaves open the "which" question (§3.1).
- The 2026 book ([S4] pp. 237-238, co-signed):
  - A small border with many blocks gives "visually appealing decompositions (Bergner et al., 2015)". The book then adds: "But don't be deluded by the beauty". The subproblems may simply be smaller general MILPs, and it calls such models "unstructured". Graph-based methods may suit unstructured models; methods based on constraint and variable classes may work best for structured ones (p. 237).
  - It cites results by Bastubbe et al. (2018) suggesting that randomly grouping constraints gives poor dual bounds, and points to learning (Basso and Ceselli 2023; Kruber et al. 2017) for finding a structure and deciding whether to use it (p. 238).
  - [inferred] The "beauty" warning is self-critique: it is aimed at the group's own 2015 figures and agrees with the points made by Khaniyev and by Yıldız et al.
- No reply to the crash reports of Basso and Ceselli was found in print. Fixes may be in later CHANGELOG entries, but the CHANGELOG has no item that can be matched to their report [S8].

---

## 4. Solving pricing problems as generic MIPs (Q3)

- **Rambau and Schwarz** ([S36], Optimization Methods and Software 2014) (S2 context; full text not read). They ran their experiments with a pre-release version of GCG and wrote: "Solving all pricing problems by ILP (as GCG does) is most probably not competitive." [observed]
- **EDGE** ([S29]) (P). Same judgement about generic MIP subproblems (§2.1). [observed]
- **Kim and Dandurand** ([S37], MPC 2022) (S2 context). For stochastic MIPs, they note that B&P methods, GCG among them, need branching constraints on integer variables in both the first and the second stage. They use this to motivate their dual-decomposition branching. [observed]
- **Maher** ([S38], EJOR 2021) (S2 context; colleague and GCG contributor). The structures detected by BaPCod, DIP, G12 and GCG serve DW and Lagrangian relaxation and are "not always suitable for the application of BD" (Benders decomposition). [observed]
- **Answer [stated, co-signed]:**
  - The book says that tailoring, for example with a specialized pricing solver, "may even be necessary" ([S4] p. 509).
  - It recommends other general B&P frameworks too, VRPSolver and BaPCod ([S4] p. 538).
  - The GCG documentation also presents GCG as a framework for implementing column-generation algorithms [S8].
  - The 2026 k-vertex-cut B&P [S9] uses tailored branching rules that keep the structure of the pricing problems, not generic MIP pricing. [practice]
- **Status:** conceded. [inferred]

---

## 5. Rival exact methods on chosen problem classes (Q4)

- **Decomposition branching** (Yıldız, Boland and Savelsbergh [S30]) (P).
  - On their weighted set-covering instances, run with the structure supplied to GCG, they report "many instances where DBE is more than 40 times faster than DW" (p. 19). DBE is their enhanced decomposition branching; DW is GCG.
  - On their facility-location instances, GCG's performance is "less consistent", even though those instances have a single linking constraint (p. 24).
  - The abstract claims orders of magnitude over both a commercial solver and an automatic DW approach (p. 1).
  - The two instance classes are theirs, built for their method. [observed]
- **Bilevel branch-and-cut on the capacitated vertex separator problem** (Furini, Ljubić, Malaguti and Paronuzzi [S31], Bologna postprint) (P).
  - They used the same 1,397 instances as Bastubbe and Lübbecke [S10]. The B&P results "are directly borrowed from the tables reported by the authors" (p. 31).
  - Instances solved (their branch-and-cut / Bastubbe-Lübbecke B&P / CPLEX):

    | Class (instances) | B&C | B&P | CPLEX |
    |---|---|---|---|
    | DIMACS (296) | 182 | 164 | 124 |
    | MIPLIB (303) | 138 | 109 | 73 |
    | Netlib (436) | 354 | 351 | 237 |
    | Random (362) | 266 | 322 | 168 |

    CPLEX is best for small k (p. 31).
  - In the introduction they call their method "competitive" against the state-of-the-art B&P (p. 5).
  - Furini and Malaguti co-authored Bergner et al. 2015. [observed]
- **DW bounds from cutting planes** (Chen, Günlük and Lodi [S27]) (P). The DW bound is enforced in the original variables, "without the need to implement branch and price" (abstract, p. 1). [observed]
- **Answer [practice]:** "Branch-and-price strikes back for the k-vertex cut problem" (Ciccarelli, Furini, Hojny and Lübbecke [S9], arXiv v2, June 2026; not yet peer-reviewed).
  - The earlier B&P (Cornaz et al. 2019) and B&C (Furini et al. 2020) methods "still fail to solve many benchmark instances" (p. 3).
  - The new extended formulation dominates the earlier ones in LP bound, and the new B&P solves 73 open instances within one hour (p. 7).
  - [inferred] The pattern: a rival beats a Lübbecke B&P on one class (2022), and he then co-signs a stronger B&P on a related class with that rival (2026). It is not the same problem: the capacitated vertex separator versus the k-vertex cut.

---

## 6. The Kantorovich attribution (Q5)

- **Critique** (Uchoa and Sadykov [S40], Mathematical Programming 217 (2026), p. 443) (P).
  - "After the 2000s", almost all authors "incorrectly attribute the weak formulation to Kantorovich". Their three examples are De Carvalho 2002, Lübbecke and Desrosiers 2005 [S2] and Villeneuve et al. 2005 [S3].
  - They admit making the same mistake in their own courses. Reading the classic cutting-stock literature for a forthcoming book on column generation in 2022, they found no trace of the weak formulation in Kantorovich's original or in its translation.
  - The formulation seems to have been proposed first by Eilon and Christofides (1971) for bin packing. [observed]
- **Confirmed in the Lübbecke-side texts** [practice, P]:
  - Selected Topics (preprint 2004/08, p. 11): the reformulation procedure "leads to Kantorovich's formulation (1960)".
  - Villeneuve et al. (preprint 2003/25, p. 9): "Formulation (14) of the cutting stock problem is due to Kantorovich (1960)."
  - The published journal versions were not compared.
- **Answer.**
  - Uchoa and Sadykov write: "We thank Marco Lübbecke for pointing out reference [12]" (p. 452). Reference [12] is Eilon and Christofides 1971. He supplied the earlier source that settles the correction.
  - The 2026 book says Kantorovich was "until recently, mistakenly associated with a weak formulation". It credits Uchoa and Sadykov (their 2024 LOGIS report) with correcting the historical perspective ([S4] p. 91). It attributes the integer master problem to Kantorovich and Zalgaller (1951) and to Gilmore and Gomory ([S4] p. 71). [stated, co-signed]
- **Status:** corrected about two years after the 2024 report. This is the only published correction of a Lübbecke text found in this search. [inferred]

---

## 7. Timetabling and the 2015 TOP exchange (Q6, Q7)

### 7.1 Lübbecke as discussant ([S1], TOP 23 (2015) 359-361) [stated, P]
- **Theory versus practice.** The competition's problem definition "may be quite far from timetabling reality" (p. 359). He wishes the next overview would cover the "dirty side" of timetabling.
- **Many objectives.** Soft constraints with penalty weights mix "apples and oranges" (p. 360). The penalties differ by orders of magnitude and runs stop before optimality, so slightly different data give very different timetables. Computing all Pareto-optimal solutions, and presenting them to users, is hardly practical.
- **Fair comparison.** Settings, machines and time limits differ between the papers compared. "This part of the overview needs to be taken with a grain of salt." (p. 360)
- **His own work.** The Lach-Lübbecke two-stage approach "(it actually is a Benders' decomposition)" (p. 360).
- **His bias.** Column generation and B&P still deserve deeper investigation, but "this perception may be personally biased" (p. 360).
- **Requests.**
  - He challenges the authors to give more vision, and calls for a new timetabling competition.
  - He would like to see how integer programming fares against the metaheuristic state of the art.
  - He will rerun his old code with a fresh CPLEX, and holds that the challenges "still lie on the modeling and algorithmic side" (p. 361).

### 7.2 The authors' answer (Bettinelli, Cacchiani, Roberti and Toth, rejoinder [S16], TOP 23 (2015) 366-368) [observed, P]
- **The benchmark definition.** They accept that the CB-CTT problem (curriculum-based course timetabling) may be far from other universities' problems, but say a precise definition stimulated research and made comparisons possible (p. 367).
- **Robustness.** The concept "cannot be directly extended to university timetabling": a lecture is not delayed because the previous one ran late. Uncertainty in student numbers and room availability is the relevant kind (p. 367).
- **Fairness.** "We fully agree that it is very hard to make a really fair comparison" (p. 367). They found no single winning method.
- **B&P.** "We do not completely agree that the overview supports investigating a branch-and-price like approach" (p. 368). Column generation behaves well for lower bounds but is "certainly not the single best method" (p. 368).
- **The other discussants.** Asín, Burke-Drake-McCollum-Özcan and Schaerf [S18-S20] do not mention Lach and Lübbecke (all three read in full).

### 7.3 Critics of the Lach-Lübbecke timetabling work [observed]
- **Phillips, Waterer, Ehrgott and Ryan** ([S21] p. 2, submitted version) (P). Lach and Lübbecke 2012 give comprehensive results but are "only concerned with the abstract problems from the ITC", and they use a single measure of quality where practice needs several. [inferred] This is the critique Lübbecke himself made of the field in 2015 (§7.1).
- **Bettinelli et al.** ([S17], overview) (S2 context). A two-stage method like Lach and Lübbecke's has clear advantages only when the problem has no constraints on groups of rooms, such as room stability. **Ozkan et al.** ([S25], 2025) (S2 context): earlier work, Lach and Lübbecke's included, handled room stability only in the second stage of a two-stage method.
  - [inferred] The 2008 report claims exactness "with respect to hard constraints" ([S6] p. 2). Room stability is a soft constraint, so the critique bounds the claim rather than refuting it.
- **Burke, Mareček, Parkes and Rudová** ([S22], 2012) (S2 context). When comparing lower bounds, they normalise Lach and Lübbecke's run times using a machine benchmark.
- **Bagger, Sørensen and Stidsen** ([S23], 2018) (S2 context). They tabulate lower and upper bounds against Lach and Lübbecke 2012 under limits of 1, 10 and 40 CPU units, on the first fourteen instances of the competition set. The fragment says their upper bounds are better "on six out of the", and is cut off there, so the denominator is not known.
- **A positive verdict.** Lindahl, Sørensen and Stidsen ([S24], 2018) (S2 context) build on the Lach-Lübbecke model, which they believe is currently the best model when the goal is a feasible solution.
- **Titles, 2008 versus 2012** [inferred].
  - The 2008 TU Berlin report is titled "Optimal Solutions to the Udine Benchmark Instances". Its abstract limits proven optimality to the first set (the four 2002-competition instances); for the second set it gives solutions with no hard-constraint violations ([S6] p. 1).
  - The 2012 journal version is titled "new solutions" [S7].
  - Whether the change answered a referee is not known: the journal text and its reviews were not read.
- **His 2015 call.** There was a new competition, ITC 2019, where a MIP formulation was used (Holm et al. abstract [S26], S). Whether integer-programming methods beat the metaheuristics there was not checked.

---

## 8. Recoverable robustness (Q8)

The paper is Liebchen, Lübbecke, Möhring and Stiller 2009 [S13], four authors with roles undivided; not read.

- **Shu and Song** ([S41], INFORMS JoC 2014) (S2 context). They show that a robust model is always infeasible, which in their words explains why the approach of Liebchen et al. "cannot handle general linear programs with equality constraints" under right-hand-side uncertainty. [observed]
- **Dewilde, Sels, Cattrysse and Vansteenwegen** ([S42], EJOR 2014) (S2 context). Liebchen et al. put planned travel time and possible delays into the objective, but "the delay cost is purely based on the worst case values". [observed]
- **Cicerone et al.** ([S43], same 2009 volume) (S2 context). They offer a rival recoverable-robustness model, which they say is better suited to comparing robust algorithms by their price of robustness. Which of their references they contrast it with was not checked. [observed]
- **Answer:** none found. [inferred] No later recoverable-robustness paper by Lübbecke appears in his OpenAlex works list; for his turns see `06-trajectory.md`.

---

## 9. Degeneracy tools (Q9)

- **Costa, Contardo, Desaulniers and Yarkony** ([S44], INFORMS JoC 2022) (S2 context). Methods against primal degeneracy may not be straightforward to implement: some need changes to the column-generation process, and row-reduced column generation (Desrosiers, Gauthier and Lübbecke 2014 [S14]) may "yield harder PSs", that is, harder pricing subproblems. [observed]
- No other critique of the IPS, DCA, PE or vector-space-decomposition papers (degeneracy methods co-signed with Desrosiers and Gauthier) turned up in the citation contexts. **Answer:** none found.

---

## 10. Claims and open questions from 2004-2005 (Q10)

- **Selected Topics** ([S2], preprint 2004/08; co-signed with Desrosiers) [stated, P].
  - Column generation is "a success story in large scale integer programming", and "generic integer programming column generation codes solve many large scale problems" of industrial difficulty that no standard commercial MIP solver could cope with (p. 24).
  - On the same page, the authors cannot recommend the classical DW implementation for large linear programs.
  - Bundle and analytic-centre (ACCPM) alternatives are "still to be evaluated in the context of integer programming" (p. 9).
  - A basic (extreme-point) dual solution "may be a bad representative of all the dual solutions obtainable" (p. 12).
- **Later outcomes.**
  - The outside verdicts on generic B&P for general MIPs in the 2020s are negative (§2). [inferred] In 2004 "generic codes" probably meant problem-class codes with specialized pricing; the sentence names none, and that was not checked further. If so, the 2004 claim and the 2020s verdicts are not about the same kind of software.
  - Briant et al. 2008 [S46] later compared bundle methods with classical column generation (title checked; not read).
  - Bredström, Jörnsten, Rönnqvist and Bouchard ([S45], ITOR 2014) (S2 context) cite Lübbecke and Desrosiers 2005 for the claim that "basic solutions to the LP relaxation are not suitable for column generation". Their counter-argument was not read.
- **The 2026 book** ([S4] p. 46) says the method, once called generalized linear programming, never became competitive for solving linear programs except in special cases. This agrees with the 2004 caveat. [stated, co-signed]

---

## 11. Failures, bugs and rejections on record (Q11)

- **GCG CHANGELOG** ([S8], group code) [practice].
  - 3.7.2: "fix bug in symmetry detection that could lead to wrong results" (line 241).
  - 2.0.1: "CPLEX pricing solver is disabled as it is incompatible with generic branching" (line 993); stabilization disabled when linking variables or variables in no block are present (line 992); wrong aggregation with bliss fixed (line 999).
  - 3.5.0: legacy mode removed together with six detectors, among them 'staircase' and 'mcl' (line 556).
  - A staircase detector still exists at master (`src/gcg/dec_staircase_lsp.cpp`), so this was a rewrite of the detection loop, not an abandoned direction.
- **Documentation** ([S8]). The speed claim for structured problems rests on one example; the performance profile is still a "@todo" (§2.2).
- **Crashes.** Reported by Basso and Ceselli with GCG 3.0.1 ([S32] p. 171; §3.1).
- **Desk rejection.** His first journal paper came out of his diploma thesis and was written with another PhD student. A prestigious journal sent it straight back as not a good fit. He was told this was normal, they resubmitted, and it was accepted in Computational Geometry: Theory and Applications ([S51] 0:30:20-0:32:22, caption, paraphrased) [stated]. [inferred] That paper is Bussieck and Lübbecke 1998 [S52].
- **Suspicious results.** In the same interview he says that results which look too good make him hunt for a bug, and that he is glad when one is found ([S51] 0:09:03-0:09:49, caption, paraphrased) [stated]. This bears on layer 5; see notes 02 and 03.
- **Errata.** None found on Crossref for his works (query of 2026-11-08).

---

## 12. Positive peer verdicts (kept for balance) [observed]

- **Basso and Ceselli** ([S32]) (P).
  - They call GCG "the state-of-the-art" for generic decomposition (p. 154).
  - Their local search improves only 13% of GCG's decompositions (p. 177).
  - Their own framework's computing time is "still far from state of the art" (p. 178).
- **Furini et al.** ([S31] p. 31) (P). The Bastubbe-Lübbecke B&P solves the most Random instances, and both decomposition methods dominate CPLEX for medium and large k.
- **Lindahl et al.** ([S24]) (S). They rate the Lach-Lübbecke model the best for finding feasible timetables.

---

## Contradictions (kept, not reconciled)

- **C1. A general method versus narrow success.**
  - The Lübbecke-side aim is B&P as a commodity that runs without the user knowing ([S51] caption). The book says B&P is "in principle" a general method for general MILPs ([S4] p. 238).
  - Outside verdicts call generic B&P "in their infancy" [S27], unable to "compete" [S28] and "rarely competitive" [S29].
  - Yet Basso and Ceselli, co-authors of the 2015 work, call its result "unexpected but fundamental" and the average "mixed" [S32].
  - Kruber et al., co-signed by Lübbecke, say DW pays off on a small fraction of MIPs [S5].
- **C2. "No input needed" versus "supply the structure".** The GCG documentation promises results without input or knowledge from the user [S8]. Yıldız et al. got much better results by supplying the linking constraints themselves [S30], and the same documentation warns that decomposing without structure can hurt.
- **C3. B&P in timetabling.** Lübbecke sees B&P as worth deeper study and flags his own bias [S1]; the overview's authors "do not completely agree" [S16].
- **C4. What he asks of others versus how his work is compared.** In 2015 he wanted comparisons under identical conditions [S1]. In 2022 his own B&P was compared through numbers borrowed from his tables, on a "comparable" machine [S31]. [inferred] This is a tension in the field's practice, not his own inconsistency.
- **C5. Quality of GCG's detection, judged by two yardsticks.** ML rankers beat GCG's score on a Lagrangian-relaxation yardstick [S34]. On a DW yardstick, GCG's decompositions are hard to improve, and static detection is fast [S32].
- **C6. Titles.** "Optimal Solutions" (2008 report) versus an abstract that limits proven optimality to one instance set, versus "new solutions" (2012 journal) [S6, S7]. [inferred]
- **C7. 2004 versus the 2020s.** "Generic" column-generation codes "solve many large scale problems" (2004, [S2] p. 24) versus "infancy" (2023, [S27]). The two may mean different kinds of software (§10).
- **C8. Kantorovich.** The weak formulation is attributed to him in 2003-2005 [S2, S3] and declared mistaken in the 2026 book [S4]. Resolved; kept as a record.

---

## Gaps (what could not be found or read)

**Lübbecke-side full texts not read:**
- Gamrath and Lübbecke 2010 [S12]; Bergner et al. 2015 [S11] (HAL copy behind a bot check); the 2012 SEA status report (Springer, closed). The RWTH preprint "Generic Decomposition and Branch-and-Price: A Status Report" (repORt 2012-005) is listed by a search engine, but the RWTH hosts timed out.
- Kruber et al. 2017 [S5]: abstract and one citation context only.
- Lach and Lübbecke 2012 [S7]; Liebchen et al. 2009 [S13]; Bastubbe and Lübbecke 2020 [S10]; the published Operations Research and Annals of OR versions of [S2, S3]. The preprints were read.

**Critic full texts not read** (closed, or behind bot checks):
- Basso et al. 2020 [S33]; Khaniyev et al. 2018 and Khaniyev's thesis [S35]; Rambau and Schwarz [S36]; Kim and Dandurand [S37]; Maher 2021 [S38]; Hansknecht et al. [S39];
- Shu and Song [S41]; Dewilde et al. [S42]; Cicerone et al. [S43]; Costa et al. [S44]; Bredström et al. [S45]; Briant et al. [S46];
- the Bettinelli et al. overview [S17]; Burke et al. 2012 [S22]; Bagger et al. 2018 [S23] (DTU Orbit behind a Cloudflare challenge); Lindahl et al. [S24]; Ozkan et al. [S25];
- Wang and Ralphs 2013 [S49] (DIP school; its citation contexts show no criticism); Coluna.jl 2026 [S50] (does it benchmark against GCG? not known).

**An unverified lead, not used:** slides by Markus Kruber hosted on the RWTH site (`markus_IMA_talk.pdf`). A search snippet attributes to them a test set of 131 MIPs on which GCG beat SCIP on 34, but the host timed out. The figures are unconfirmed.

**Missing kinds of evidence:**
- No public peer reviews: there is no OpenReview-type venue, zbMATH has one descriptive review [S15], and no review of the 2026 book was found.
- No published exchange in which a Lübbecke paper is the target. The 2015 TOP exchange has him as a discussant.
- No reply by Lübbecke to EDGE, to Chen et al. or to the crash reports.
- No issue tracker. The GitHub mirror's issue list was empty, and the RWTH GitLab and the mailing lists were not checked.

**Not checked:**
- whether integer-programming methods did well in ITC 2019;
- which references Cicerone et al. contrast with;
- whether the 2008-to-2012 title change answered a referee;
- whether any study has benchmarked a 2020s GCG release (4.x or 5.0).

DBLP was not used (bot check).

---

## Sources

Each line gives the authors, year, title, venue, identifier, a P/S mark, and what was read. Pages are those of the copy read.

- [S1] Lübbecke (2015). "Comments on: An overview of curriculum-based course timetabling". TOP 23(2):359-361. DOI 10.1007/s11750-015-0364-1. P (read in full, publisher free copy)
- [S2] Lübbecke, Desrosiers. "Selected Topics in Column Generation". TU Berlin Inst. für Mathematik preprint 2004/08 (DepositOnce 10.14279/depositonce-14317); Oper. Res. 53(6):1007-1023 (2005), DOI 10.1287/opre.1050.0234. P (preprint, pp. 9, 11, 12, 24)
- [S3] Villeneuve, Desrosiers, Lübbecke, Soumis. "On Compact Formulations for Integer Programs Solved by Column Generation". TU Berlin preprint 2003/25 (DepositOnce 10.14279/depositonce-14266); Ann. Oper. Res. 139:375-388 (2005), DOI 10.1007/s10479-005-3455-9. P (preprint p. 9)
- [S4] Desrosiers, Lübbecke, Desaulniers, Gauthier. "Branch-and-Price". Les Cahiers du GERAD G-2024-36 (June 2024, revised January 2026), gerad.ca/papers/G-2024-36.pdf; Springer 2026, DOI 10.1007/978-3-031-96917-1. P (pp. vi, 46, 71, 91, 237-238, 509, 538, 627)
- [S5] Kruber, Lübbecke, Parmentier (2017). "Learning When to Use a Decomposition". CPAIOR 2017, LNCS 10335:202-210. DOI 10.1007/978-3-319-59776-8_16. S (abstract on researchportal.ip-paris.fr; one S2 context)
- [S6] Lach, Lübbecke (2008). "Curriculum Based Course Timetabling: Optimal Solutions to the Udine Benchmark Instances". TU Berlin report, DOI 10.14279/depositonce-14423. P (pp. 1-2)
- [S7] Lach, Lübbecke (2012). "Curriculum based course timetabling: new solutions to Udine benchmark instances". Ann. Oper. Res. 194(1):255-272. DOI 10.1007/s10479-010-0700-7. S (metadata only)
- [S8] RWTH group. GCG repository github.com/scipopt/gcg at commit c0e230a34ab8 (2026-07-27): CHANGELOG (lines 241, 556, 992-999), README.md, doc/resources/users/why-gcg.md, src/gcg/dec_staircase_lsp.cpp. Apache-2.0. P (practice)
- [S9] Ciccarelli, Furini, Hojny, Lübbecke (2026). "Branch-and-price strikes back for the k-vertex cut problem". arXiv:2602.04984v2. P (pp. 1-7; unreviewed preprint)
- [S10] Bastubbe, Lübbecke (2020). "A branch-and-price algorithm for capacitated hypergraph vertex separation". Math. Prog. Comput. 12(1):39-68. DOI 10.1007/s12532-019-00171-5. S (metadata; results relayed by [S31])
- [S11] Bergner, Caprara, Ceselli, Furini, Lübbecke, Malaguti, Traversi (2015). "Automatic Dantzig-Wolfe reformulation of mixed integer programs". Math. Prog. 149:391-424. DOI 10.1007/s10107-014-0761-5. S (not read; relayed by [S28, S30, S34])
- [S12] Gamrath, Lübbecke (2010). "Experiments with a Generic Dantzig-Wolfe Decomposition for Integer Programs". SEA 2010, LNCS 6049:239-252. DOI 10.1007/978-3-642-13193-6_21. S (not read)
- [S13] Liebchen, Lübbecke, Möhring, Stiller (2009). "The Concept of Recoverable Robustness, Linear Programming Recovery, and Railway Applications". LNCS 5868:1-27. DOI 10.1007/978-3-642-05465-5_1. S (not read)
- [S14] Desrosiers, Gauthier, Lübbecke (2014). "Row-reduced column generation for degenerate master problems". EJOR. DOI 10.1016/j.ejor.2013.12.016. S (metadata only)
- [S15] Lübbecke (2001). "Engine Scheduling by Column Generation". PhD thesis, TU Braunschweig, DOI 10.24355/dbbs.084-200511080100-720; zbMATH review 0976.68014 by P. Brucker. P (review text)
- [S16] Bettinelli, Cacchiani, Roberti, Toth (2015). "Rejoinder on: an overview of curriculum-based course timetabling". TOP 23(2):366-368. DOI 10.1007/s11750-015-0367-y. P (read in full)
- [S17] Bettinelli, Cacchiani, Roberti, Toth (2015). "An overview of curriculum-based course timetabling". TOP 23(2):313-349. DOI 10.1007/s11750-015-0366-z. S (S2 contexts; closed)
- [S18] Burke, Drake, McCollum, Özcan (2015). "Comments on: An overview of curriculum-based course timetabling". TOP 23(2):355-358. DOI 10.1007/s11750-015-0362-3. P (read in full)
- [S19] Schaerf (2015). "Comments on: An overview of curriculum-based course timetabling". TOP 23(2):362-365. DOI 10.1007/s11750-015-0365-0. P (read in full)
- [S20] Asín (2015). "Comments on: An overview of curriculum-based course timetabling". TOP 23(2):350-354. DOI 10.1007/s11750-015-0363-2. P (read in full)
- [S21] Phillips, Waterer, Ehrgott, Ryan (2015). "Integer programming methods for large-scale practical classroom assignment problems". Comput. Oper. Res. 53:42-53. DOI 10.1016/j.cor.2014.07.012. P (Lancaster eprint 75294, submitted version, p. 2)
- [S22] Burke, Mareček, Parkes, Rudová (2012). "A branch-and-cut procedure for the Udine Course Timetabling problem". Ann. Oper. Res. 194:71-87. DOI 10.1007/s10479-010-0828-5. S (S2 context)
- [S23] Bagger, Sørensen, Stidsen (2018). "Benders' decomposition for curriculum-based course timetabling". Comput. Oper. Res. 91:178-189. DOI 10.1016/j.cor.2017.10.009. S (S2 context)
- [S24] Lindahl, Sørensen, Stidsen (2018). "A fix-and-optimize matheuristic for university timetabling". J. Heuristics 24(4):645-665. DOI 10.1007/s10732-018-9371-3. S (S2 context)
- [S25] Ozkan, Ulucan, Dirik, Atici (2025). "University course timetabling with multi-section courses, room stability and lecturer preferences: an application in a business school". Comput. Manag. Sci. 22(1), article 3. DOI 10.1007/s10287-025-00529-2. S (S2 context; full title checked on Crossref)
- [S26] Holm, Mikkelsen, Sørensen, Stidsen (2022). "A graph-based MIP formulation of the International Timetabling Competition 2019". J. Sched. 25:405-428. DOI 10.1007/s10951-022-00724-y. S (abstract)
- [S27] Chen, Günlük, Lodi (2025). "Recovering Dantzig-Wolfe Bounds by Cutting Planes". Oper. Res. 73(2):1128-1142. DOI 10.1287/opre.2023.0048; arXiv:2301.13149v2. P (arXiv v2 pp. 1-2)
- [S28] Clausen, Lusby, Røpke (2022). "Consistency Cuts for Dantzig-Wolfe Reformulations". Oper. Res. 70(5):2883-2905. DOI 10.1287/opre.2021.2160; arXiv:2105.13076v1. P (arXiv v1 pp. 33-34, 39)
- [S29] INRIA EDGE project-team (Sadykov, Vanderbeck, Pessoa, Uchoa et al.). Activity reports 2022-2025, §3.1 "Decomposition methods", radar.inria.fr/report/2022/edge/ (also /2023/, /2024/, /2025/). P
- [S30] Yıldız, Boland, Savelsbergh (2022). "Decomposition Branching for Mixed Integer Programming". Oper. Res. 70(3):1854-1872. DOI 10.1287/opre.2021.2210. P (open manuscript via S2 link, pp. 1-2, 4, 16, 19, 24)
- [S31] Furini, Ljubić, Malaguti, Paronuzzi (2022). "Casting Light on the Hidden Bilevel Combinatorial Structure of the Capacitated Vertex Separator Problem". Oper. Res. 70(4):2399-2420. DOI 10.1287/opre.2021.2110. P (Bologna postprint, pp. 5, 31-33)
- [S32] Basso, Ceselli (2023). "A data driven Dantzig-Wolfe decomposition framework". Math. Prog. Comput. 15:153-194. DOI 10.1007/s12532-022-00230-4. P (CC BY; pp. 154-155, 167-168, 171, 175-178)
- [S33] Basso, Ceselli, Tettamanzi (2020). "Random sampling and machine learning to understand good decompositions". Ann. Oper. Res. 284(2):501-526. DOI 10.1007/s10479-018-3067-9. S (S2 contexts)
- [S34] Weiner, Ernst, Li, Sun (2023). "Ranking constraint relaxations for mixed integer programs using a machine learning approach". EURO J. Comput. Optim. 11:100061. DOI 10.1016/j.ejco.2023.100061; arXiv:2207.00219v1. P (arXiv v1 pp. 2, 4-6, 15, 21)
- [S35] Khaniyev, Elhedhli, Erenay (2018). "Structure Detection in Mixed-Integer Programs". INFORMS J. Comput. 30(3):570-587. DOI 10.1287/ijoc.2017.0797; with Khaniyev (2018), "Data-driven Structure Detection in Optimization: Decomposition, Hub Location, and Brain Connectivity", PhD thesis, Waterloo, hdl 10012/13476. S (S2 context)
- [S36] Rambau, Schwarz (2014). "Solving a vehicle routing problem with resource conflicts and makespan objective with an application in car body manufacturing". Optim. Methods Softw. 29(2):353-375. DOI 10.1080/10556788.2013.768993. S (S2 context)
- [S37] Kim, Dandurand (2022). "Scalable branching on dual decomposition of stochastic mixed-integer programming problems". Math. Prog. Comput. 14(1):1-41. DOI 10.1007/s12532-021-00212-y. S (S2 context)
- [S38] Maher (2021). "Implementing the branch-and-cut approach for a general purpose Benders' decomposition framework". EJOR 290(2):479-498. DOI 10.1016/j.ejor.2020.08.037. S (S2 context)
- [S39] Hansknecht, Joormann, Korn, Morscheck, Stiller (2023). "Feeder routing for air-to-air refueling operations". EJOR 304(2):779-796. DOI 10.1016/j.ejor.2022.04.016. S (S2 context)
- [S40] Uchoa, Sadykov (2026). "Kantorovich and Zalgaller (1951): the 0-th column generation algorithm". Math. Prog. 217:439-456. DOI 10.1007/s10107-026-02350-4. P (CC BY; pp. 443, 452)
- [S41] Shu, Song (2014). "Dynamic Container Deployment: Two-Stage Robust Model, Complexity, and Computational Results". INFORMS J. Comput. 26(1):135-149. DOI 10.1287/ijoc.2013.0552. S (S2 context)
- [S42] Dewilde, Sels, Cattrysse, Vansteenwegen (2014). "Improving the robustness in railway station areas". EJOR 235:276-286. DOI 10.1016/j.ejor.2013.10.062. S (S2 context)
- [S43] Cicerone, D'Angelo, Di Stefano, Frigioni, Navarra, Schachtebeck (2009). "Recoverable Robustness in Shunting and Timetabling". LNCS 5868:28-60. DOI 10.1007/978-3-642-05465-5_2. S (S2 context)
- [S44] Costa, Contardo, Desaulniers, Yarkony (2022). "Stabilized Column Generation Via the Dynamic Separation of Aggregated Rows". INFORMS J. Comput. 34(2):1141-1156. DOI 10.1287/ijoc.2021.1094. S (S2 context)
- [S45] Bredström, Jörnsten, Rönnqvist, Bouchard (2014). "Searching for optimal integer solutions to set partitioning problems using column generation". Int. Trans. Oper. Res. 21(2):177-197. DOI 10.1111/itor.12050. S (S2 context)
- [S46] Briant, Lemaréchal, Meurdesoif, Michel, Perrot, Vanderbeck (2008). "Comparison of bundle and classical column generation". Math. Prog. 113:299-344. DOI 10.1007/s10107-006-0079-z. S (title checked; not read)
- [S47] Semantic Scholar Graph API, citation contexts for 31 Lübbecke works (3,057 citing records), harvested 2026-11-08. S
- [S48] zbMATH Open API, author lubbecke.marco-e (54 documents; one signed review), queried 2026-11-08. S
- [S49] Wang, Ralphs (2013). "Computational Experience with Hypergraph-Based Methods for Automatic Decomposition in Discrete Optimization". CPAIOR 2013, LNCS 7874:394-402. DOI 10.1007/978-3-642-38171-3_31. S (S2 context)
- [S50] Vanderbeck, Marques, Sadykov, Nesello, Javerzat, Pessoa et al. (2026). "Coluna.jl: A Branch-Cut-and-Price Framework in Julia". INFORMS J. Comput. DOI 10.1287/ijoc.2025.1130. S (metadata only)
- [S51] "Subject to" podcast, Marco Lübbecke interviewed by Anand Subramanian (2021-09-23), youtube.com/watch?v=JzWAAvryTKA. Caption transcript saved in talks/ by research agent 02. P (caption; paraphrased; 0:09:03-0:09:49, 0:30:20-0:32:22, 0:52:16-0:53:20)
- [S52] Bussieck, Lübbecke (1998). "The vertex set of a 0/1-polytope is strongly P-enumerable". Comput. Geom. 11(2):103-109. DOI 10.1016/S0925-7721(98)00021-2. S (metadata only)
