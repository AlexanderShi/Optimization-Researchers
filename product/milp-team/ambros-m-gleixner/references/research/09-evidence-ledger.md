# Ambros M. Gleixner · Evidence ledger

## Contents

- [How to Use, front matter and disclaimer](#how-to-use) · [Routing and protocol](#routing)
- [Taste: marks of good research](#taste-marks) · [Taste: warning signs and quick-check](#taste-warnings)
- Methods: [1](#method-1) · [2](#method-2) · [3](#method-3) · [4](#method-4) · [5](#method-5) · [6](#method-6) · [7](#method-7)
- [Stage Workflows](#workflows): [A](#workflow-a) · [B](#workflow-b) · [C](#workflow-c) · [D](#workflow-d) · [E](#workflow-e) · [F](#workflow-f)
- Heuristics: [1](#heuristic-1) · [2](#heuristic-2) · [3](#heuristic-3) · [4](#heuristic-4) · [5](#heuristic-5) · [6](#heuristic-6) · [7](#heuristic-7) · [8](#heuristic-8) · [9](#heuristic-9) · [10](#heuristic-10) · folded: [HA](#heuristic-11) · [HB](#heuristic-12)
- [Common Misreadings](#misreadings)
- Anatomies: [iterative refinement](#anatomy-iterative-refinement) · [VIPR](#anatomy-vipr) · [MIPLIB 2017](#anatomy-miplib-2017) · [status update](#anatomy-status-update) · [limited-precision oracles](#anatomy-limited-precision-oracles) · [decision analysis](#anatomy-decision-analysis)
- [Anti-patterns](#anti-patterns) · [Trajectory](#trajectory) · [Lineage and collaboration](#lineage) · [Inner tensions](#inner-tensions) · [Roundtable Card](#roundtable-card)
- [Honest Boundary](#honest-boundary) · [Corrections](#corrections) · [Rejected and held-back updates](#rejected) · [Sources](#sources) · [Card key](#card-key)

> Date: 2026-11-28 (stage T3.6, team-synthesize). The full evidence behind `../../SKILL.md`. SKILL.md keeps, per item, the strongest statement and cards, a one-clause say–do line, at most two ⚠ scope bullets (after the review fixes; corrections are marked once, in SKILL.md's Corrections list) and a pointer to the matching section here. Each section has up to five parts: **Full-text evidence** (copied word for word from `08-deep-reading-synthesis.md`, which is traceable to the paper cards), **T3.6 long form** (the item as first written in this pass, before it was condensed to fit SKILL.md's word budget; every card cite in it was checked by `check_citations.py`), **Changes made in SKILL.md (T3.6)**, and **Before T3.6 (moved verbatim)** (the SKILL.md item as it stood on 2026-11-14, built from web research, so nothing is lost; its `[02 I5]`-style keys point to the web-research notes `01-…06-*.md` in this folder, its headings are set in bold and its links are re-pointed to work from this folder). Copied 08 text is left as copied; where SKILL.md differs, the Changes block says so (08 itself is edited only for links, counts and the review fixes below). After the read-only review of 2026-11-28, a **T3.6 review fixes** block in each affected section records what changed in SKILL.md and holds the replaced SKILL.md text verbatim; six 08 passages were corrected in 08 and in their copies here, and long forms were corrected where the review found an error.

**How to read.** `[S022 p. 17]` is paper card S022 at the `[[page N]]` page of the file the card read. That file is often a report or arXiv version even where the citation carries no version word, so the [card key](#card-key) names it for every card, with the printed-page offset where the file is the journal's own. A version word (`TR`, `arXiv`, `report`, `draft`) marks cards always cited with their version (08 §1). Abstract- and metadata-level cards are cited by id only. Every card id used here, in SKILL.md and in the technique catalog is listed in the [card key](#card-key), with the SKILL.md source key where one exists. Keys such as `[SU23 p. 809]` are SKILL.md's source keys with printed pages (Sources appendix of SKILL.md). PD, DM, EP and WM ids are the proof devices, design moves, experiment protocols and writing moves of [../technique-catalog.md](../technique-catalog.md). Quotation marks enclose only text copied from a card's verified quote list or card text (`verify_card_quotes.py`, 2026-11-28: 197 quotes, 197 exact), or from the pre-synthesis SKILL.md, whose quotes come from the web-research notes (MIP 2021 and CO@Work 2024 quotes are automatic captions). SKILL.md's own T3.6 wording, where a review-fix block names it, is set in italics, never in quotation marks; the T3.6 text replaced by the review fixes is copied as block quotes.

**Voice.** Most SCIP Optimization Suite reports and many papers are ZIB group work. What Gleixner wrote or led (the thesis S032, rational SoPlex and the exact-LP papers with Steffy, the oracle paper S029, VIPR, the MIPLIB 2017 lead S002, the SCIP 5.0 and 6.0 reports as first author) is kept apart from what he co-signed or supervised (08, house rules). The Suite reports S010, S014, S003, D004, S005, S004, S007 and S021 (with S015 and S096) are one series and count once toward the three-paper threshold; H001/S028 are one study, S071 is the Japanese version of S023 (08 §1).

**Sealed material and reading notes.** Passages of the cards that restate the sealed validation items in `holdout.md` are not used here or in SKILL.md, and the card that would carry one of them (S048) is cited nowhere (08 §1, §10). Inconsistencies that card readers noted inside single works are reading notes, not findings about the researcher; they are not repeated here. Two pre-synthesis SKILL.md clauses that restated such notes are left out of the moved-verbatim copies below, which say so where it happens (08 §3.3).

**Coverage** (`team_status.py --coverage`, 2026-11-28): 107 Scholar rows · 103 distinct works indexed · 92 open full texts · 90 read in full · 2 in part · 6 abstract only · 2 metadata only (incl. unreadable) · 3 skipped · 0 book material · 197 quotes verified.

<a id="how-to-use"></a>

## How to Use, front matter and the first-activation disclaimer

### Full-text evidence (08, copied)

- **Consequence for How to Use**: the entry `proof design` under *Not good for* should be narrowed to polyhedral and cutting-plane theory; proofs for mixed-precision LP algorithms are now in scope through Method 7.

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Attribution | PaPILO shows his group and agenda, not his coding | The 8.0 report makes Hoen and Gleixner jointly responsible for PaPILO's dual postsolving: "AH and AG are responsible for the new dual postsolving functionality in PaPILO (Section 6)." [S004 p. 83]; he is first author of the PaPILO paper [S026 p. 1] | Qualify: one credited PaPILO feature, joint |

### T3.6 long form

**Good for** (stages with evidence): whether a solver answer can be trusted and how to make it exact or certified; mixed-precision LP algorithms and their proofs against a stated floating-point contract (Method 7); computational experiments for solver components; benchmarks and competitions; debugging and default decisions; programmes that end in a release.

**Not good for**: polyhedral or cutting-plane theory, decomposition as a research topic, ML for MIP, commercial-solver internals; literature review, writing craft, supervision and referee responses (no distillable Gleixner method).

**Field fit**: the evidence is LP-based branch and bound in the open-source SCIP Optimization Suite (SCIP, SoPlex, PaPILO, VIPR). Closed solvers and hand-offs: see Activation Rules.

**Evidence format.** `[SU23 p. 809]` = source key (Sources appendix) and printed page. `[S022 p. 17]` = paper card S022 at the page of the file the card read; `TR`, `arXiv`, `report` or `draft` in the citation names a version other than the listed one; ids without pages are abstract- or metadata-level cards. Every card id resolves in the ledger's [card key](#card-key); "full evidence" pointers lead to the [evidence ledger](09-evidence-ledger.md), and PD, DM, EP and WM ids to the proof devices, design moves, experiment protocols and writing moves of the [technique catalog](../technique-catalog.md). **stated** = his own words; **co-authored** = joint-paper text; **practice** = papers, code, records; **group** = done mainly by his students; **observed** = others; **inferred** = our reading.

**Attribution.** From about 2016 students or postdocs lead almost every paper: he is first-listed or sole in 4 of 13 carded works of 2008–2012, 5 of 13 of 2013–2017, 7 of 41 of 2018–2022 and 1 of 33 of 2023–2026 [08 §8]. His own hand: the thesis (2015), the 2014 visit report, the Steffy papers (exact LP, limited-precision oracles), the MIPLIB 2017 lead, his SCIP, SoPlex and VIPR commits, the merge-request template, mailing-list and GitHub replies, three talks; release reports credit him with named features [S010 p. 28; S003 p. 37; S004 p. 83]. PaPILO (Gottwald; he is first author of the paper [S026 p. 1] and shares the dual postsolving with Hoen [S004 p. 83]), MIP-DD (Hoen, Kamp) and exact SCIP's code (mostly Eifler) show his group and agenda more than his coding. Byline order is no reliable signal of his role (Common Misreading 4). His own voice is thin after 2021.

---

### Changes made in SKILL.md (T3.6)

- **Front matter**: `researched:` 2026-11-14 → 2026-11-28. The description now opens with the coverage (92 works read in full or in part) and adds the seventh method (write and audit the floating-point solver's accuracy contract); "build benchmarks from written admission rules" became "from written rules" and "until the method ships in the default solver" became "until the method ships by default", to keep the description well under 1024 characters. Name, type and trigger phrases are unchanged.
- **First-activation disclaimer** (the only Activation Rules line changed): it now carries the coverage numbers of `team_status.py --coverage` (92 of 103 indexed works read in full or in part; 8 more known only from abstracts or metadata) and the research date 2026-11-28.
- **Good for / Not good for**: proofs for mixed-precision LP algorithms are in scope through Method 7, so "proof design" left *Not good for*; "polyhedral or cutting-plane theory" stays there (08 §4.1, consequence for How to Use) [S029 pp. 8–17].
- **Evidence format**: card citations, version words, the card key, the ledger and the technique catalog explained. The 07 card index and the cards are not offered to the user: they hold passages that restate sealed validation items (Sources appendix of SKILL.md).
- **Attribution**: the first-listed-or-sole count per period from 08 §8 (1 of 33 carded works in 2023–2026 is in SKILL.md; the full series 4 of 13, 5 of 13, 7 of 41, 1 of 33 is in the long form and in 08 §8); PaPILO qualified: one credited feature, the dual postsolving, jointly with Hoen [S004 p. 83] (08 §3.2); he is first author of the PaPILO paper [S026 p. 1] (long form). The sentence "Byline order is no reliable signal" moved to Common Misreading 4.

### T3.6 review fixes (2026-11-28)

- **Evidence format** (review: unmarked card cites such as [S034 pp. 17–19] are report pages, and the Answer Standard sends the user to *the paper cards* that the Sources appendix forbids opening): every card page is a page of the file the card read, often a report or arXiv version; the [card key](#card-key) now names that file, the published form and, for journal files, the printed-page offset. Cards are read through the card key and the technique catalog only, in roundtable turns too.
- **Attribution**: the 1-of-33 count is qualified as byline position, alphabetical bylines included (review: Common Misreading 4 says byline order is no signal of his role).
- **First-activation disclaimer** shortened, same numbers (review: 45 words, the number 92 twice).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> **Evidence format.** `[SU23 p. 809]` = source key (Sources appendix) and printed page; `[S022 p. 17]` = paper card S022 at the page of the file it read (`TR`, `arXiv`, `report`, `draft` name another version), resolved in the ledger's [card key](#card-key); "full evidence" pointers lead to the [evidence ledger](#contents); PD, DM, EP and WM ids to the [technique catalog](../technique-catalog.md). **stated** = his own words; **co-authored** = joint-paper text; **practice** = papers, code, records; **group** = done mainly by his students; **observed** = others; **inferred** = our reading.
> **Attribution.** From about 2016 students or postdocs lead almost every paper (he is first-listed or sole in 1 of 33 carded works of 2023–2026 [08 §8]). His own hand: the thesis (2015), the 2014 visit report, the Steffy papers, the MIPLIB 2017 lead, his SCIP, SoPlex and VIPR commits, the merge-request template, mailing-list and GitHub replies, three talks. PaPILO (Gottwald; one credited feature shared with Hoen [S004 p. 83]), MIP-DD (Hoen, Kamp) and exact SCIP's code (mostly Eifler) show his group and agenda, not his coding. His own voice is thin after 2021. ([full evidence](#how-to-use))
> - On first activation say once: "This is distilled from public work, not Gleixner's own advice: 92 of his works read in full or in part (92 open full texts among 103 indexed works; 8 more known only from abstracts or metadata), his talks, commits, GitHub replies and students' theses, researched on 2026-11-28." Never repeat it, nor in roundtable turns. In the reply it is one sentence in the Basis footer, not an opening paragraph (Answer Standard).


### Before T3.6 (moved verbatim)

**Front matter** (description and date):

```
name: ambros-m-gleixner
description: |
  Ambros M. Gleixner's research craft in MILP solver engineering, distilled from his thesis, papers, talks, commits and GitHub replies, his students' theses and critics' work. Use it to plan, test or review solver work the Gleixner way: count a belief about solver numerics per decision, build a like-for-like baseline and report both factors, let floating point produce and exact arithmetic decide, attach certificates an independent checker can verify (and test that checker), build benchmarks from written admission rules, and keep a ledger of printed gaps until the method ships in the default solver. Triggers: "Gleixner lens", "ask Gleixner", "how would Gleixner approach this", "what would Gleixner say about our exact MIP / certificate / benchmark / speed-up", "Gleixner-style review", "Gleixner.skill". Also loaded by milp-roundtable. Not for routine SCIP or SoPlex usage help, or for questions that name neither Gleixner nor the MILP Team.
type: research-craft
researched: 2026-11-14
```

**First-activation line of Activation Rules:**

- On first activation say once: "This is distilled from public work, not Gleixner's own advice." Never repeat it, nor in roundtable turns. In the reply it is one sentence in the Basis footer, not an opening paragraph (Answer Standard).

**How to Use:**

**Good for** (stages with evidence): whether a solver answer can be trusted and how to make it exact or certified; computational experiments for solver components; benchmarks and competitions; debugging and default decisions; programmes that end in a release.

**Not good for**: polyhedral or cutting-plane theory, proof design, decomposition as a research topic, ML for MIP, commercial-solver internals; literature review, writing craft, supervision and referee responses (no distillable Gleixner method).

**Field fit**: the evidence is LP-based branch and bound in the open-source SCIP Optimization Suite (SCIP, SoPlex, PaPILO, VIPR). Closed solvers and hand-offs: see Activation Rules.

**Evidence format.** `[SU23 p. 809]` = source key (Sources appendix) and page. **stated** = his own words; **co-authored** = joint-paper text; **practice** = papers, code, records; **group** = done mainly by his students; **observed** = others; **inferred** = our reading.

**Attribution.** From about 2016 students or postdocs lead almost every paper. His own hand: the thesis (2015), the 2014 visit report, the Steffy papers, the MIPLIB 2017 lead, his SCIP, SoPlex and VIPR commits, the merge-request template, mailing-list and GitHub replies, three talks. PaPILO (Gottwald), MIP-DD (Hoen, Kamp) and exact SCIP's code (mostly Eifler) show his group and agenda, not his coding. His own voice is thin after 2021.

---

<a id="routing"></a>

## Research Task Routing and Agentic Protocol

### Changes made in SKILL.md (T3.6)

- New routing row for designing or proving a mixed-precision LP algorithm: Method 7 for the contract, proof and failure audit, Method 5 for the split (08 §4.1).
- Disagreement row: a tolerance-only answer now also points to Heuristic 11 (check and report in the original model, tolerances in its units; 08 §5 HA). Debugging row: H11 added. "Exact / verified / certified" row: H12 added (presolve serves its consumer, certificate coverage; 08 §5 HB).
- No-method row: "proofs" narrowed to "polyhedral proofs" (Method 7 covers proofs for mixed-precision algorithms).
- Agentic Protocol Step 2: a **Contract (Method 7)** bullet (what the floating-point solver is assumed to deliver; how a violation is detected and escalated).
- A ledger pointer after the "More than one row fits" line.

### T3.6 review fixes (2026-11-28)

- The Method 7 row now routes to Method 7 in full and then Workflow B, whose checkpoint carries a Method 7 condition (review: Workflow A's output, a problem-choice paragraph, does not fit a design or proof task).
- H11 and H12 left the disagreement, debugging and "exact / verified / certified" rows, since both were folded into steps (see [Rejected and held-back updates](#rejected)); the rows read as before T3.6 apart from the Method 7 row.
- Declined: changing the Activation Rules line *continue with Methods 4–6* for closed solvers to 4–7; that section stays verbatim by rule (`check_ledger.py --allow frontmatter,activation-disclaimer`). Method 7's *Applies to stage* now says a closed floating-point solver can be the oracle (inferred).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> | "Design or prove a mixed-precision LP algorithm (refinement, boosting)" | A step 2; Method 7 for the contract, proof and failure audit, Method 5 for the split | 7, 5 |
> | "Solvers, seeds or tolerances disagree" "Exact mode says infeasible, X found a solution" | Check each claimed solution against the original file in exact arithmetic (Method 4 step 4). Exactly feasible: the other answer is wrong; C, presolve off first (H4b). Only tolerance-feasible: a tolerance effect (C step 6; H11; Method 6 step 9). Same value, different times: variability; seeds or permutations (H8) | 4, 1; H4, H8, H11 |
> | "Wrong answer, crash, numbers don't add up" (also on a closed solver) | C: debugging (closed solver: steps 1–3 through parameters) | H3–H5, H11 |
> | "Can we call this exact / verified / certified?" | D 🔴 checkpoint; Method 4 steps 6–7: name checker, version and covered stages (presolve?) | 4; H1, H12 |


### Before T3.6 (moved verbatim)

**Research Task Routing:**

| User says | Workflow | Main methods |
|---|---|---|
| "Is this worth doing?" "Pick a solver project" | A: choosing the problem | 3, 1 + Taste quick-check |
| "Can I trust this answer?" "Do we need exact solving?" (no failing instance yet) | A steps 1–2; then Method 5 for the design and Method 4 for the check | 5, 4, 1 |
| "Solvers, seeds or tolerances disagree" "Exact mode says infeasible, X found a solution" | Check each claimed solution against the original file in exact arithmetic (Method 4 step 4). Exactly feasible: the other answer is wrong; C, presolve off first (H4b). Only tolerance-feasible: a tolerance effect (C step 6; Method 6 step 9). Same value, different times: variability; seeds or permutations (H8) | 4, 1; H4, H8 |
| "Which baseline? How to design the experiment?" | B: experiment design | 2, 6; H6–H8 |
| "Build a test set / benchmark / competition" | B step 3 with Method 6 in full | 6 |
| "Wrong answer, crash, numbers don't add up" (also on a closed solver) | C: debugging (closed solver: steps 1–3 through parameters) | H3–H5 |
| "Should this be on by default?" "Is this ready to merge?" | C steps 4–5 | H3; 2 |
| "Is this result good? How to report it?" | D: judging and reporting | 2, 3; H2, H8 |
| A reviewer or user disputes a computational claim (variability, wrong answers) | C, then D in its checkpoint order | 4; H6, H4, H8, H5, H3, H2 |
| "Can we call this exact / verified / certified?" | D 🔴 checkpoint; Method 4 steps 6–7: name checker, version and covered stages (presolve?) | 4; H1 |
| "Released; someone found a bug in our checker" | E: after publication | H1; 3, 6 |
| "Stuck" "slower than the incumbent, no idea what next" "cannot get it published" | F: unsticking a project | 2, 3, 5, 1 |
| "Agenda for the next years" | A plus the gap ledger | 3 |
| Literature review, writing, supervising, rebuttal wording, proofs | No distillable Gleixner method: give generic advice marked "not Gleixner-style" | — |

**More than one row fits**: if a concrete instance or run misbehaves, start with its row (disagreement or C), then return to the question behind it; otherwise take the earliest open stage (A, B, D, E).

**Step 2: Gleixner-style fact-finding:**

**⚠️ Use tools (web search, arXiv, Crossref, GitHub, solver CHANGELOGs); never answer from memory.**

- **Baseline (Method 2)**: features the incumbent has and the new code lacks; exact versions of both arms and every third-party part; source access or parameters only?
- **Instances (Method 6)**: do independent solvers agree on each optimum or infeasibility? Was each solution checked against the original file in exact arithmetic? MIPLIB 2017 tags and changelog for unstable or exchanged instances.
- **Certificates (Method 4)**: which checker at which commit; open soundness fixes (VIPR PRs #24, #25, #28, issues #26, #27 open on 2026-11-14; re-check); a formally verified checker (CakeML, LeanVIPR); which steps lie outside?
- **Exact-mode state (Methods 3, 5)**: the current SCIP CHANGELOG and release report; recent wrong-answer issues and their stage.
- **Gap ledger (Method 3)**: the predecessors' limitation paragraphs; is the idea a printed gap, already closed?
- **Rival mechanisms**: does the SAT, pseudo-Boolean or CP community have it?
- **Metrics (H7, H8)**: shifts, time limit, seeds, exclusive machines.

Keep search results internal; the user sees the judgement and next step.

<a id="taste-marks"></a>

## Taste: marks of good research

### T3.6 long form

1. **An answer someone else can check without trusting your code.** Certificates "as simple to verify as possible if they are to be convincing" [VIPR §1; S019 p. 4]; "checking should not require a sophisticated code where that could contain bugs itself" [Sim21 01:53]; independent solution checks in arbitrary precision against the original file [M17 pp. 464–465; S002 pp. 22–23].
2. **An experiment that explains why, not a race.** To "analyze the reasons for their behavior by controlled scientific testing", citing Hooker [Th p. 10; Hooker95]; the epigraph; numbered questions (H6); attribution runs that print the null [S034 pp. 17–19; S074 pp. 11–12].
3. **A method that extends what can be solved at all**: to "solve problems which could not be solved before" [Th abstract]; a 5.7% mean speed-up not claimed as consistent (a one-sided Wilcoxon signed-rank test showed five instances, factors 90 to 357, carried it), yet OBBT's small slowdowns were "an acceptable price to pay" for newly solved instances (of 11 INT timeouts: plain 1, +OBBT 6, +OBBT+LVB 10) [Th pp. 145–147; S032 pp. 157–159]; OBBT as a "game changer" in the journal version [S011 p. 21]; headlines count instances solved [SU23; LCCP26].
4. **Exact where the answer is a proof or must be exactly feasible; floating point otherwise** (overturns the common picture): "for the majority of applications this is perfectly satisfactory" [STSM14 §1]; likewise in 2012, co-authored [S023 p. 22]; exactness for computer-assisted mathematics and verification [Chv22 §1]; against "a skeptical attitude that borders on paranoia" [VIPR §1].
5. **Printed with its limits and their size**: 17 of 107 certificate runs hit the 10 GB cap [VIPR; S019 p. 10]; "We also observed, however, that the performance gap to floating-point solvers is still large" [SU23], now with its factors [S022 pp. 17–18].
6. **An instrument that is unambiguous, heterogeneous, tilted to hard cases, corrected in public**: "Instances exhibiting such ambiguity are not suitable for benchmarking" [M17 p. 465; S002 p. 23]; benchmark v2 [MIPLIB-CL]; "users of solver software should not rely on simplistic comparisons" (group) [Dag18].
7. **Shipped in the default distribution** (already known): "an out-of-the-box technique" [Th p. 173]; [S10]; Undercover and the nonlinearity score became defaults [S018 p. 18; S010 p. 14].
8. **Application structure becomes a generic solver component** [Th p. 2; SAP19]; a supply-chain idea implemented through a generic proxy and switched on for all MIPs [S045 p. 14].

### Changes made in SKILL.md (T3.6)

- Mark 1: "as simple to verify as possible" located in the read file [S019 p. 4] (the VIPR card notes that the phrases SKILL.md quoted from [VIPR §1] sit on pp. 4 and 3 of the file); "independent exact solution checks" corrected to "independent solution checks in arbitrary precision against the original file" [S002 pp. 22–23] (08 §3.2, Method 6 step 3 and Taste 1 row).
- Mark 2: practice added: attribution runs that print the null [S034 pp. 17–19; S074 pp. 11–12] (08 §3.1, Method 1 variant; §4.2, first row: the practice behind Taste 2).
- Mark 3: thesis pages as card pages [S032 pp. 157–159] (printed pp. 145–147).
- Mark 4: the 2012 co-authored statement on floating-point sufficiency added [S023 p. 22].
- Mark 5: the certificate cap located in the file [S019 p. 10].
- Mark 6: the ambiguity quote located in the file [S002 p. 23].
- Mark 7: Undercover as a default heuristic [S018 p. 18] (the long form also has the nonlinearity score on by default [S010 p. 14]).
- Mark 8: an application idea implemented through a generic proxy and switched on for all MIPs [S045 p. 14].

### T3.6 review fixes (2026-11-28)

- Taste 2: the attribution runs labelled (group) [S034 pp. 17–19; S074 pp. 11–12]. Taste 4: the 2012 sentence labelled as a co-authored text [S023 p. 22].
- Taste 5 (review: the new quick-check question had no criterion and no card): + the floating-point solver's assumed accuracy and its failures counted per instance (his line with Steffy) [S029 pp. 8–9, 23; S013 TR pp. 9–10]. The quick-check question was folded into question 7, so the list keeps eight questions.
- Taste 1: its correction (arbitrary-precision tolerance checks [S002 pp. 22–23]) is now named in SKILL.md's Corrections list (MIPLIB 2017 line).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 2. **An experiment that explains why, not a race.** To "analyze the reasons for their behavior by controlled scientific testing", citing Hooker [Th p. 10; Hooker95]; the epigraph; numbered questions (H6); attribution runs that print the null [S034 pp. 17–19; S074 pp. 11–12].
> 4. **Exact where the answer is a proof or must be exactly feasible; floating point otherwise** (overturns the common picture): "for the majority of applications this is perfectly satisfactory" [STSM14 §1], likewise in 2012 [S023 p. 22]; exactness for computer-assisted mathematics and verification [Chv22 §1]; against "a skeptical attitude that borders on paranoia" [VIPR §1].
> 5. **Printed with its limits and their size**: 17 of 107 certificate runs hit the 10 GB cap [VIPR; S019 p. 10]; "We also observed, however, that the performance gap to floating-point solvers is still large" [SU23].


### Before T3.6 (moved verbatim)

1. **An answer someone else can check without trusting your code.** Certificates "as simple to verify as possible if they are to be convincing" [VIPR §1]; "checking should not require a sophisticated code where that could contain bugs itself" [Sim21 01:53]; independent exact solution checks [M17 pp. 464–465].
2. **An experiment that explains why, not a race.** To "analyze the reasons for their behavior by controlled scientific testing", citing Hooker [Th p. 10; Hooker95]; the epigraph; numbered questions (H6).
3. **A method that extends what can be solved at all**: to "solve problems which could not be solved before" [Th abstract]; a 5.7% mean speed-up not claimed as consistent (a one-sided Wilcoxon signed-rank test showed five instances, factors 90 to 357, carried it), yet OBBT's small slowdowns were "an acceptable price to pay" for newly solved instances (of 11 INT timeouts: plain 1, +OBBT 6, +OBBT+LVB 10) [Th pp. 145–147]; headlines count instances solved [SU23; LCCP26].
4. **Exact where the answer is a proof or must be exactly feasible; floating point otherwise** (overturns the common picture): "for the majority of applications this is perfectly satisfactory" [STSM14 §1]; exactness for computer-assisted mathematics and verification [Chv22 §1]; against "a skeptical attitude that borders on paranoia" [VIPR §1].
5. **Printed with its limits and their size**: 17 of 107 certificate runs hit the 10 GB cap [VIPR]; "We also observed, however, that the performance gap to floating-point solvers is still large" [SU23].
6. **An instrument that is unambiguous, heterogeneous, tilted to hard cases, corrected in public**: "Instances exhibiting such ambiguity are not suitable for benchmarking" [M17 p. 465]; benchmark v2 [MIPLIB-CL]; "users of solver software should not rely on simplistic comparisons" (group) [Dag18].
7. **Shipped in the default distribution** (already known): "an out-of-the-box technique" [Th p. 173]; [S10].
8. **Application structure becomes a generic solver component** [Th p. 2; SAP19].

<a id="taste-warnings"></a>

## Taste: warning signs and the quick-check

### T3.6 long form

1. "Verified" by the code that produced the answer, or an unchecked stage (presolve) left unnamed [VIPR §1; Method 4].
2. A mean carried by a handful of instances; timeouts left in an overhead comparison ("that just dilutes the results", automatic captions [MIP21 00:11]; in print [S006 pp. 19–20]).
3. One factor without its baseline; comparing unlike things ("not fully fair" [Sim21 02:10]).
4. Benchmark averages used to pick a solver: "Average performance on this set is not a suitable criterion to decide which MIP solver to use in a particular application scenario." [M17 p. 445]
5. Instances whose optimal value depends on tolerances, kept in a benchmark or in gap statistics.
6. An adjective where a count exists (H2).
7. A rational re-implementation of a part that only produces candidates (Method 5).
8. A bound or reduction called exact or valid without the sense in which it holds, or a bound from a changed problem reported as valid for the original (H11) [S017 TR pp. 4, 12; S001 TR pp. 9–10].

### Changes made in SKILL.md (T3.6)

- Warning sign 2: the printed source added beside the caption quote [S006 pp. 19–20] (co-authored 2018: comparisons that include time-limit runs are biased by the limit; a mean reduction may come from a drastic speed-up on few instances).
- Warning sign 8 (new): a bound or reduction called exact or valid without the sense in which it holds, pointing to Heuristic 11 [S017 TR pp. 4, 12; S001 TR pp. 9–10] (08 §5 HA, steps 3–4).
- Taste quick-check: one question added for mixed-precision methods (Method 7).

### T3.6 review fixes (2026-11-28)

- Warning sign 2 (review: the card page sat inside the quoted clause, which reads as a quote in print): the caption quote keeps [MIP21 00:11]; the printed point stands outside it (co-authored) [S006 pp. 19–20], where comparisons with timeouts are called strongly biased by the time limit.
- Warning sign 8 no longer points to Heuristic 11 (folded): it carries the S017 phrase itself, "since precisely speaking a different problem is solved" [S017 TR p. 4], with [S017 TR p. 12; S001 TR pp. 9–10], and points to Workflow C step 6.
- Quick-check: the ninth question (no card, list above the framework's five to eight) folded into question 7, backed by Taste 5.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 2. A mean carried by a handful of instances; timeouts left in an overhead comparison ("that just dilutes the results", automatic captions [MIP21 00:11]; in print [S006 pp. 19–20]).
> 8. A bound or reduction called exact or valid without the sense in which it holds (H11) [S017 TR pp. 4, 12; S001 TR pp. 9–10].
> - [ ] Is the remaining gap stated as a number, exclusions named?
> - [ ] For a mixed-precision method: is the floating-point solver's contract written down, and are its violations counted?


### Before T3.6 (moved verbatim)

**Warning signs:**

1. "Verified" by the code that produced the answer, or an unchecked stage (presolve) left unnamed [VIPR §1; Method 4].
2. A mean carried by a handful of instances; timeouts left in an overhead comparison ("that just dilutes the results", automatic captions [MIP21 00:11]).
3. One factor without its baseline; comparing unlike things ("not fully fair" [Sim21 02:10]).
4. Benchmark averages used to pick a solver: "Average performance on this set is not a suitable criterion to decide which MIP solver to use in a particular application scenario." [M17 p. 445]
5. Instances whose optimal value depends on tolerances, kept in a benchmark or in gap statistics.
6. An adjective where a count exists (H2).
7. A rational re-implementation of a part that only produces candidates (Method 5).

**Taste quick-check:**

- [ ] Can a third party check the result without trusting your solver?
- [ ] Does the experiment answer a stated why-question on a named subset?
- [ ] Does it solve new instances, or is the gain a mean carried by a few?
- [ ] Is the answer a proof or an exactly feasible plan? If not, is floating point plus a check enough?
- [ ] Like-for-like baseline, with both factors reported?
- [ ] Will it ship in the default distribution with tests?
- [ ] Is the remaining gap stated as a number, exclusions named?
- [ ] Is every benchmark instance unambiguous?

<a id="method-1"></a>

## Method 1: Turn the belief into a measurement

### Full-text evidence (08 §2, copied)

| Method | Evidence | Variant | Contradiction | Any link | Abstract-level | Say–do after reading |
|---|---|---|---|---|---|---|
| M1 Turn the belief into a measurement | 11 (10) | 22 (20) | 3 (3) | 33 (28) | S077 evidence, S081 variant | ✅ stated and practised; earliest per-instance count now 2012 |

**Method 1 · Turn the belief into a measurement**

- **Strongest cards.** The per-decision study itself [S072 pp. 2, 4–12, 14] (group: Hoen first). Earlier instances of counting a field belief per instance: the belief that floating-point bases are often optimal, counted on a set where it should hold and on one selected where it fails [S020 TR pp. 5, 9] (co-authored, 2012), and qualified for more than 14% of 1,202 LPs [S032 p. 65] (own). The practitioners' belief that scaling removes numerical error, turned into per-solution checks with counted outcomes [S037 pp. 2, 6, 9–10] (co-authored). A predecessor's unquantified caveat turned into a per-round measure and counted [D003 pp. 5, 11–12] (group). A reliability defect counted before and after a redesign [S015 pp. 7, 9] (group). Proposed in 2017 as future work: measure the numerical violation over all certificate derivations [S019 p. 10].
- **Step 3 (instrument, do not rewrite).** Shadow-mode runs that record without acting [S012 pp. 9, 18; S080 p. 19]; the unchanged solver observed through events [S072 pp. 2, 4–12].
- **Step 4 (a set where the belief should hold and one built to break it).** A set the floating-point solver finds easy and one compiled to be numerically difficult: the predecessor's FPEasy and NumDiff reused [S019 p. 9; S022 p. 9; S072 p. 8].
- **Say–do.** ✅. The move is older than the 2014 visit report the skill dates it to: it is practised in 2012 [S020 TR pp. 5, 9] and in the thesis [S032 p. 65].
- **Counter-cases.** A computational advantage argued without an implementation or count, in his sole-authored 2012 report [S066 pp. 3, 12]; a release report's reliability claim without counts of failed runs [S007 pp. 5, 26] (group); two modelling expectations left unmeasured in the 2008 Diplom thesis [S025 pp. 31, 44] (weak: student work, model fidelity rather than solver behaviour).
- **Main variant** (22 cards): the same move applied to one's own design beliefs and gains rather than to a belief of the field; see §3.1 and §4.2.

### Variants (08 §3.1, copied)

- **Method 1, own-design beliefs (22 cards).** The measuring move turned on the authors' own design rationale or headline gain: a design belief measured against a virtual best and by output-channel ablations, printing that the motivating mechanism was not the driver [S034 pp. 13, 17–19]; open transfers measured instead of folklore [S022 pp. 6, 12–14]; the authors' worry that conflicts eat the parallel gain answered from full transaction logs [S026 pp. 15, 20]; the price of parallelism counted before defending the design [S067 arXiv p. 5]; applicability counted before any performance claim [S043 pp. 20, 22–23; S073 pp. 10–12]; the claim that presolve buys robustness counted per failure type [S078 arXiv p. 18]; the safety risk checked by comparing rounded safe and unsafe bounds per instance [S085 pp. 13–14, 21]. Attribution runs that print the null are the sharpest form [S074 pp. 11–12; S070 p. 20; S072 p. 12; S064 p. 29]. This is the practice behind Taste 2 (§4.2). Proposed as Method 1 step 8: before claiming a gain or explaining a loss, name the suspected mechanism, run the control that removes or forces it (an output channel switched off [S034 pp. 17–19]; all inequalities forced [S070 p. 20]; a tighter tolerance [S072 p. 12]; the new component deactivated [S064 p. 29]; nodes set against time per node [S022 pp. 10–11; S083 p. 18]), print the result even when it is null [S074 pp. 11–12], and restate the claim without what did not hold [S022 p. 15].

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Method 1 step 5 | 25 and 27 of 50 `[NC25 Table 1]` | These counts are the text's [S072 p. 9] | Cite the page, not the table |

### T3.6 long form

**One line**: when the field holds a belief about solver behaviour without data, define a check a computer can run per decision, run the production solver as a grey box, and count.

**Evidence**:
- Stated: "Although for the majority of instances, we can confirm the conclusion that Dhiflaoui et al. (2003) and Koch (2004) have drawn based on the Netlib test set, namely that floating-point LP solvers often succeed in returning optimal bases, we have to relativize this finding for more than 14% of the instances." (thesis, own voice) [S032 p. 65]; the 2014 visit report defines a "reliability of integer assignments" to be analysed computationally [STSM14 §2, §4].
- Practice: every critical branch-and-bound decision of SCIP checked a posteriori in exact arithmetic, to "quantify the widely accepted belief" (group, Hoen first) [NC25; S072 pp. 2, 4–12, 14]; the 2012 refinement paper counts the belief on a set where it should hold and on one where it fails [S020 TR pp. 5, 9]; the belief that scaling removes numerical error, turned into per-solution checks [S037 pp. 2, 6, 9–10]; an algorithm-independent progress measure because tolerance-based stopping made propagation codes incomparable (group) [CP21; D003 pp. 5, 11–12].
- Say–do: ✅ stated + practised, 2012–2025; full texts: 11 cards evidence (10 studies), 22 variant, 3 contradiction.
- Variants/corrections:
  - ⚠ Older than the 2014 report: practised in 2012 [S020 TR pp. 5, 9] and in the thesis [S032 p. 65].
  - ⚠ Turned on one's own design beliefs and gains (22 cards), now step 8 [S034 pp. 13, 17–19; S074 pp. 11–12].
  - ⚠ Counter-cases: an advantage argued without a count in his sole-authored 2012 report [S066 pp. 3, 12]; a release report's reliability claim without failure counts (group) [S007 pp. 5, 26].

**Steps**:
1. Write the belief as one sentence (for example: floating-point MIP solvers are numerically robust).
2. Define a per-decision check. 2014: fix the rounded integers of a floating-point solution, solve the rest exactly, sort into three cases (same objective, different objective, infeasible). 2025: verify each critical branch-and-bound decision, the cheapest check first (DM3) [S072 pp. 4–8].
3. Instrument the solver, do not rewrite it; spend exact arithmetic only where a decision is close. Shadow-mode runs that record without acting are the same device [S012 pp. 9, 18; S080 p. 19].
4. Run a set where the belief should hold and one built to break it (FPEasy, 57; NumDiff, 50), each also permuted (EP8) [S019 p. 9; S072 p. 8].
5. Report per class: errors on 2 of 57 FPEasy instances (dual side only); NumDiff 25 (original) and 27 (permuted) of 50 fully correct [NC25; S072 p. 9].
6. Name the mechanism of the errors (exactly infeasible subproblems; slightly violated solutions trigger pruning) and test the obvious remedy: tighter tolerances help only partly [S072 pp. 12, 14].
7. Say which way it cuts for your agenda: here for robustness, against his earlier "compromised" framing.
8. Turn the move on your own claim (EP5): before claiming a gain or explaining a loss, name the suspected mechanism and run the control that removes or forces it (an output channel switched off [S034 pp. 17–19]; a tighter tolerance [S072 p. 12]; the new component deactivated [S064 p. 29]); print the result even when it is null [S074 pp. 11–12], and restate the claim without what did not hold [S022 p. 15].

**Applies to stage**: choosing the problem; experiment design; judging.

**Different from standard practice**: the field asserts or counter-asserts; he counts, and publishes a count that weakens his own motivating sentence.

**Limitations**: needs source access and decision logging; not possible on a closed solver. The 2014 plan of a joint paper by autumn 2015 did not happen; the question returned ten years later with another student [06 §6].

### Changes made in SKILL.md (T3.6)

- **Evidence condensed to the house format.** Stated → the thesis sentence, quoted in part [S032 p. 65] (the whole quotation is in the long form; the 2014 report and the 2025 abstract statements are in the moved-verbatim copy). Practice → [NC25; S072 pp. 2, 4–12, 14], the 2012 count [S020 TR pp. 5, 9], [S037 pp. 6, 9–10], [CP21; D003 pp. 5, 11–12]. Say–do from the 08 §2 table: 11 (10), 22 (20), 3 (3).
- **Variant bullets**: the move dates from 2012, not the 2014 report (08 §2, Say–do); turned on one's own design beliefs (08 §3.1, 22 cards), now step 8; counter-cases [S066 pp. 3, 12; S007 pp. 5, 26] (08 §2, Counter-cases). The weak counter-case [S025 pp. 31, 44] (student work, model fidelity) stays in the 08 text above.
- **Steps**: step 2 + cheapest check first (DM3) [S072 pp. 4–8]; step 3 + shadow mode [S012 pp. 9, 18] (08: also [S080 p. 19]); step 4 + EP8 [S072 p. 8] (08: predecessor's sets [S019 p. 9; S022 p. 9]); step 5 cites the page of the text's counts [S072 p. 9] instead of Table 1 (08 §3.2); step 6 + [S072 p. 12]; **step 8 new** (08 §3.1 and §4.2: Method 1 variant, attribution runs) [S034 pp. 17–19; S074 pp. 11–12; S022 p. 15].
- **Limitations**: the 2014 plan sentence moved here from the old Say–do line.

### T3.6 review fixes (2026-11-28)

- **Core Research Methods introduction**: Method 7 named as new against the prior picture; the prior-snapshot clause, the ✗/⚠ marking sentence and the count legend moved here (review: bookkeeping).
- **Stated** (review: own voice replaced by a thesis quote only): the 2014 visit report's "reliability of integer assignments" [STSM14 §2, §4] restored before the thesis quote [S032 p. 65], which again anchors step 2's 2014 design.
- **Say–do** shortened to one clause; the card tallies 11 (10), 22 (20), 3 (3) are in the 08 table above. **Variants removed**: the 2012 dating is in the Corrections list; the own-design variant is step 8; the counter-cases [S066 pp. 3, 12; S007 pp. 5, 26] moved into the Say–do clause.
- **Step 8** labelled group practice [S034 pp. 17–19; S074 pp. 11–12; S022 p. 15]. **Step 4**: EP8 no longer cites [S020 TR p. 9] or its T3.6 reading of what the two sets measure (review: close to a sealed item; the step itself stands on [S019 p. 9; S072 p. 8]).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> Seven methods pass the four Phase 2 checks (recurrence, say–do, executable, exclusive). Methods 1–3 are new against the prior picture; 4–6 deepen it (unconfirmed: the prior snapshot postdates notes 01–06 in git). On the 92 full texts Methods 1–6 held, corrected where marked ✗ or ⚠, and Method 7 was promoted [08 §2–§4]. Say–do counts: cards linking the method, studies in brackets.
> - Say–do: ✅ stated + practised, 2012–2025; full texts: 11 cards evidence (10 studies), 22 variant, 3 contradiction.
> - Variants/corrections:
>   - ⚠ Dates from 2012, not the 2014 report [S020 TR pp. 5, 9].
>   - ⚠ Turned on one's own design beliefs and gains: step 8 [S034 pp. 17–19].
>   - ⚠ Counter-cases without counts [S066 pp. 3, 12; S007 pp. 5, 26].
> - Stated: on the belief that floating-point LP solvers return optimal bases, "we have to relativize this finding for more than 14% of the instances" (thesis) [S032 p. 65].


### Before T3.6 (moved verbatim)

**One line**: when the field holds a belief about solver behaviour without data, define a check a computer can run per decision, run the production solver as a grey box, and count.

**Evidence**:
- Stated: the 2014 visit report defines a "reliability of integer assignments" that can be analysed computationally [STSM14 §2, §4]; the COW 2025 abstract asks whether each solver decision could be turned into a certificate valid in exact arithmetic (paraphrase) [COW25].
- Practice: every critical branch-and-bound decision of SCIP checked a posteriori in exact arithmetic, to "quantify the widely accepted belief" [NC25, first author Hoen]; group: an algorithm-independent progress measure because tolerance-based stopping made propagation codes incomparable [CP21].
- Say–do consistency: ✅ stated (2014, 2025) and practised (2025). The 2014 plan of a joint paper by autumn 2015 did not happen; the question returned ten years later with another student [06 §6].

**Steps**:
1. Write the belief as one sentence (for example: floating-point MIP solvers are numerically robust).
2. Define a per-decision check. 2014: fix the rounded integers of a floating-point solution, solve the rest exactly, sort into three cases (same objective, different objective, infeasible). 2025: verify each critical branch-and-bound decision.
3. Instrument the solver, do not rewrite it; spend exact arithmetic only where a decision is close.
4. Run a set where the belief should hold and one built to break it (FPEasy, 57; NumDiff, 50), each also permuted.
5. Report per class: errors on 2 of 57 FPEasy instances (dual side only); NumDiff 25 (original) and 27 (permuted) of 50 fully correct [NC25 Table 1].
6. Name the mechanism of the errors (exactly infeasible subproblems; slightly violated solutions trigger pruning) and test the obvious remedy: tighter tolerances help only partly.
7. Say which way it cuts for your agenda: here for robustness, against his earlier "compromised" framing.

**Applies to stage**: choosing the problem; experiment design; judging.

**Different from standard practice**: the field asserts or counter-asserts; he counts, and publishes a count that weakens his own motivating sentence.

**Limitations**: needs source access and decision logging; not possible on a closed solver.

**Core Research Methods introduction (before T3.6):**

Six methods passed the four Phase 2 checks (recurrence, say–do, executable, exclusive). Methods 1–3 are new against the prior picture; 4–6 deepen it (unconfirmed: the prior snapshot postdates notes 01–06 in git).

<a id="method-2"></a>

## Method 2: Like-for-like baseline, both factors reported

### Full-text evidence (08 §2, copied)

| Method | Evidence | Variant | Contradiction | Any link | Abstract-level | Say–do after reading |
|---|---|---|---|---|---|---|
| M2 Like-for-like baseline, both factors | 29 (21) | 49 (36) | 1 (1) | 64 (47) | — | ✅ from 3 studies to 21 |

**Method 2 · Like-for-like baseline, both factors reported**

- **Strongest cards.** The reduced and default floating-point baselines with both factors and the attribution sentence [S022 pp. 8–11, 17–18] (group, his line); the same pairing for safe Gomory cuts [S036 pp. 20–21, 24–27] and certified propagation [S074 pp. 8–9]; SCIP 10 prints fp-reduced and fp-default factors on one-solved and both-solved subsets and compares the release with the previous major and its last bugfix release [S021 pp. 4, 11–12] (group). Stripping the incumbent of the routines the new code lacks: SoPlex without the presolvers not yet implemented [S068 p. 6] (first-listed, group voice); crossover switched off in the commercial solvers because the new interior-point code lacks it [S064 pp. 26, 28–29; S027 pp. 9–11] (group, energy HPC line). Reduced baseline for a replacement component [S034 pp. 11, 19]; controlled shared inputs, called a fair comparison [S085 pp. 17–19]; both methods implemented in one LP solver to re-test the literature's expectation [S050 pp. 9–10]; engine swapped inside one framework [S061 pp. 5–6]. Earliest: a reduced setting that isolates a propagator plus a default control run [S039 pp. 7–8] (2013), a filter measured with interacting components switched off [S054 pp. 9, 11] (2013), and a presolve compared inside one solver per scenario [S017 TR pp. 15–17] (2012).
- **Say–do.** ✅. Stated: the attribution sentence [S022 p. 17]; practised in 21 studies, 2012–2026.
- **Quote** (SCIP 10, group): "Overall these results suggest a slowdown factor between 3 and 4 for solving MIPs exactly with the same features and a current slowdown of around 10 times compared to fp-default." [S021 p. 11]
- **Step 10** (previous major plus latest bugfix release) appears first in SCIP 10 [S021 p. 4]; the earlier releases compare with the previous major only [D004 pp. 13–15; S005 p. 7; S004 p. 4; S015 p. 4; S007 pp. 4–5].
- **Counter-cases.** Exact and floating-point SCIP on different LP-solver versions without comment and without a factor [S042 p. 10]; a solver comparison after relaxing tolerances whose confound is printed but not sized [S015 p. 16]; a learned method's headline against the default only, with a tuned baseline beside it [S012 pp. 11–13].

### Variants (08 §3.1, copied)

- **Method 2.** (a) Baseline strengthened or given rather than stripped: the fastest LP route searched over formulations [S025 pp. 55, 76, 81]; the oracle in its standard settings [S058 pp. 14–15]; a published predecessor rerun [S092 pp. 8–10]. (b) Release form, default against default with the suite's parts changing [S003 pp. 7–8, 16, 19; S005 pp. 7–8; S015 p. 4; S007 pp. 4–5]. (c) Only relative component effects across the exact and the floating-point arm, no default factor [S036 pp. 24–25; S074 pp. 9–10]. (d) Mismatch stated and argued but not removed [S024 pp. 16–17, 26; S037 p. 11; S045 pp. 19–20; S070 pp. 9, 17, 21]. (e) Like-for-like by shared inputs or a common scale instead of stripped features [D003 pp. 5, 10, 12; S080 pp. 19–21; S079 pp. 6–7]. (f) The rival's best case built by hand when no stripped rival exists [S078 arXiv pp. 13, 15, 17–20].

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Method 2 step 4 | quote cited `[SU23 p. 810]` | The sentence is on file p. 17 = printed p. 809 [S022 p. 17] | Cite printed p. 809 |

### Reading notes (08 §3.3, copied)

Two existing SKILL.md passages restate reading notes (Method 2, Limitations: one sentence; Method 6 step 3: one parenthesis). Under the operator's rule they should be rephrased neutrally or dropped. The update should not add further notes of this kind.

---

### T3.6 long form

**One line**: compare new code that lacks features of the incumbent with an incumbent stripped of exactly those features, and with the default incumbent; state the remaining mismatch.

**Evidence**:
- Stated: "in terms of solvability, the gap between the exact and inexact seems to be mostly due to the currently still missing solving methods" (co-authored) [SU23 p. 809; S022 p. 17]; the 2013 exact-MIP slowdown of two to four was measured against a plain branch and bound, and pseudo-Boolean against floating-point MIP solvers is "not fully fair" [Sim21 01:11, 02:10].
- Practice: floating-point SCIP "in a reduced setting with all features disabled that are not yet present in the current exact SCIP version" [SU23 p. 809; S022 pp. 8–11, 17–18]; the same pairing for safe Gomory cuts and certified propagation [S036 pp. 20–21, 24–27; S074 pp. 8–9]; SCIP 10 prints fp-reduced and fp-default factors and compares with the previous major and its last bugfix release (group) [S021 pp. 4, 11–12]; SoPlex with the presolvers switched off that the new code lacks [S068 p. 6]; earliest, a reduced setting isolating a propagator plus a default control run (2013) [S039 pp. 7–8].
- Say–do: ✅ stated + practised in 21 studies, 2012–2026; full texts: 29 cards evidence (21 studies), 49 variant, 1 contradiction.
- Variants/corrections:
  - ✗ Step 4's sentence is on printed p. 809 [S022 p. 17], not p. 810.
  - ⚠ Release form: default against default while the suite's parts change [S003 pp. 7–8; S005 pp. 7–8]; step 10 first appears in SCIP 10 [S021 p. 4].
  - ⚠ Baseline strengthened or given instead of stripped (the oracle in its standard settings [S058 pp. 14–15], a predecessor rerun [S092 pp. 8–10]); a mismatch argued but not removed [S024 pp. 16–17; S045 pp. 19–20].
  - ⚠ Not everywhere: exact and floating-point arms on different LP-solver versions, no factor given [S042 p. 10]; a learned method's headline against the default only, a tuned baseline beside it [S012 pp. 11–13].

**Steps**:
1. List what the incumbent has and the new code lacks (cuts, propagation, conflict analysis, symmetry; presolvers [S068 p. 6]; crossover [S064 p. 26]).
2. Build the reduced incumbent; keep default as a second baseline (EP1).
3. Report both factors with their subset: 3.9 (reduced) and 8.1 (default) on the 42 MIPLIB 2017 instances all three solve [SU23 pp. 809–810; S022 pp. 17–18]; SCIP 10: 3–4 and about 10 [S10 p. 11; S021 p. 11].
4. Attribute with the pair (the sentence under Stated) [SU23 p. 809], hedging each attribution separately (WM5) [S022 pp. 11, 17–18].
5. Keep third-party parts identical (same QSopt_ex version). If you cannot, say so and argue the effect (IPCO: CPLEX 12.3.0 against 12.8.0 [ZR21-04 p. 7; D002 p. 9]); then remove the mismatch in the next version (journal: CPLEX 12.3.0 "for all experiments" [SU23 p. 801; S022 p. 9]).
6. For a component question, compare inside the reduced baseline (no cuts against safe Gomory cuts) [GMI24 §4; S036 pp. 20–21].
7. Reuse the predecessor's sets (FPEasy, NumDiff) and add a harder public one (MIPLIB 2017); when your factor differs from the predecessor's, re-measure on the shared set and explain the difference there [S022 pp. 17–18].
8. Drop instances that differ mathematically between arms (tolerance-feasible, exactly infeasible) [S022 p. 17].
9. Print any gain that comes from a defect of the old baseline [SU23 p. 803 fn. 1].
10. For a release, compare with the previous major and its latest bugfix release (10.0 against 9.0 and 9.2.4; group) [S10; S021 p. 4].
11. Where no stripped rival exists, build the rival's best case by hand and say what it costs the rival (EP9) [S078 arXiv pp. 13, 17–20], or make the arms like-for-like through shared inputs, such as the same initial solution [S085 p. 19].

**Applies to stage**: experiment design; reporting.

**Different from standard practice**: the baseline is constructed, not given, and the unflattering default factor is printed too.

**Limitations**: needs source access; critics relay the default factor without qualifiers; his 2021 forecast of 2–4 held only like-for-like.

### Changes made in SKILL.md (T3.6)

- **Evidence condensed.** Stated → the attribution sentence, now cited to printed p. 809 [SU23 p. 809; S022 p. 17] (08 §3.2); the Simons talk statements are in the moved-verbatim copy. Practice → [S022 pp. 8–11, 17–18], [S036 pp. 20–21; S074 pp. 8–9], [S021 pp. 4, 11–12], earliest [S039 pp. 7–8]; further cards (S068, S064/S027, S034, S085, S050, S061, S054, S017) are in the 08 text above. Say–do: 29 (21), 49 (36), 1 (1).
- **Variant bullets**: ✗ the page of step 4; release form [S003 pp. 7–8], step 10 first in SCIP 10 [S021 p. 4]; baseline strengthened or given [S058 pp. 14–15; S092 pp. 8–10] (08 §3.1 (a)); not everywhere [S042 p. 10] (08 §2, Counter-cases). The mismatch-argued variant (08 §3.1 (d)) and the learned-method counter-case [S012 pp. 11–13] are in the long form.
- **Steps**: step 1 + presolvers switched off in SoPlex [S068 p. 6]; step 3 + card pages [S022 pp. 17–18; S021 p. 11]; step 4 cites p. 809 and refers to the sentence under Stated (the quotation itself is not repeated); step 5 + [D002 p. 9; S022 p. 9]; step 6 + [S036 pp. 20–21]; step 7 + re-measure a predecessor's factor on the shared set [S022 pp. 17–18]; step 8 + [S022 p. 17]; step 10 + [S021 p. 4]; **step 11 new**: the rival's best case built by hand (EP9) [S078 arXiv pp. 13, 17–20] (08 §3.1 (f)).
- **Limitations**: one clause restating a reading note was removed (operator rule, 08 §3.3).

### T3.6 review fixes (2026-11-28)

- **Stated** (review: his own voice had been replaced by co-authored text): the Simons talk statements [Sim21 01:11, 02:10] restored as Stated; the SU23 sentence kept and labelled Co-authored [SU23 p. 809; S022 p. 17].
- **Practice**: earliest in 2012 [S017 TR pp. 15–17] and 2013 [S039 pp. 7–8] (review: the Say–do clause already said 2012).
- **Say–do** one clause, with the counter-case [S042 p. 10]; tallies in the 08 table above.
- **Variants**: the ✗ page bullet is in the Corrections list; two ⚠ scope conditions remain: release reports compare default against default [S003 pp. 7–8; S021 p. 4]; where the rival is another code, standard settings or a predecessor rerun [S058 pp. 14–15; S092 pp. 8–10], or its best case built by hand (co-signed) [S078 arXiv pp. 13, 17–20].
- **Step 11 removed** (review: it rested on one co-signed study, S078, Gleixner fourth of six, and 08 §3.1 lists it as variant (f)); it is now the second ⚠ variant.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> - Stated: "in terms of solvability, the gap between the exact and inexact seems to be mostly due to the currently still missing solving methods" (co-authored) [SU23 p. 809; S022 p. 17].
> - Practice: floating-point SCIP "in a reduced setting with all features disabled that are not yet present in the current exact SCIP version" [SU23 p. 809; S022 pp. 8–11, 17–18]; the same pairing for safe cuts and certified propagation [S036 pp. 20–21; S074 pp. 8–9] and in SCIP 10 (group) [S021 pp. 4, 11–12]; earliest in 2013 [S039 pp. 7–8].
> - Say–do: ✅ stated + practised in 21 studies, 2012–2026; full texts: 29 cards evidence (21 studies), 49 variant, 1 contradiction.
> - Variants/corrections:
>   - ✗ Step 4's sentence is on printed p. 809 [S022 p. 17], not p. 810.
>   - ⚠ Release form: default against default [S003 pp. 7–8]; step 10 first in SCIP 10 [S021 p. 4].
>   - ⚠ Baseline strengthened or given, not stripped [S058 pp. 14–15; S092 pp. 8–10].
>   - ⚠ Not everywhere: arms on different LP-solver versions [S042 p. 10].
> 11. Where no stripped rival exists, build the rival's best case by hand (EP9) [S078 arXiv pp. 13, 17–20].


### Before T3.6 (moved verbatim)

**One line**: compare new code that lacks features of the incumbent with an incumbent stripped of exactly those features, and with the default incumbent; state the remaining mismatch.

**Evidence**:
- Stated: the 2013 exact-MIP slowdown of two to four was measured against a plain branch and bound [Sim21 01:11]; pseudo-Boolean against floating-point MIP solvers is "not fully fair" [Sim21 02:10].
- Practice: floating-point SCIP "in a reduced setting with all features disabled that are not yet present in the current exact SCIP version" [SU23 p. 809]; again for safe Gomory cuts [GMI24 §4] and in SCIP 10 [S10 p. 11].
- Say–do consistency: ✅ stated and practised in three studies (2021/2023, 2023/2024, 2025).

**Steps**:
1. List what the incumbent has and the new code lacks (cuts, propagation, conflict analysis, symmetry).
2. Build the reduced incumbent; keep default as a second baseline.
3. Report both factors with their subset: 3.9 (reduced) and 8.1 (default) on the 42 MIPLIB 2017 instances all three solve [SU23 pp. 809–810]; SCIP 10: 3–4 and about 10 [S10 p. 11].
4. Attribute with the pair: "in terms of solvability, the gap between the exact and inexact seems to be mostly due to the currently still missing solving methods" [SU23 p. 810].
5. Keep third-party parts identical (same QSopt_ex version). If you cannot, say so and argue the effect (IPCO: CPLEX 12.3.0 against 12.8.0 [ZR21-04 p. 7]); then remove the mismatch in the next version (journal: CPLEX 12.3.0 "for all experiments" [SU23 p. 801]).
6. For a component question, compare inside the reduced baseline (no cuts against safe Gomory cuts) [GMI24 §4].
7. Reuse the predecessor's sets (FPEasy, NumDiff) and add a harder public one (MIPLIB 2017).
8. Drop instances that differ mathematically between arms (tolerance-feasible, exactly infeasible).
9. Print any gain that comes from a defect of the old baseline [SU23 p. 803 fn. 1].
10. For a release, compare with the previous major and its latest bugfix release (10.0 against 9.0 and 9.2.4; group) [S10].

**Applies to stage**: experiment design; reporting.

**Different from standard practice**: the baseline is constructed, not given, and the unflattering default factor is printed too.

**Limitations**: needs source access; critics relay the default factor without qualifiers; his 2021 forecast of 2–4 held only like-for-like.

*(One clause of the Limitations line, restating a reading note, is left out here under the operator rule, 08 §3.3.)*

<a id="method-3"></a>

## Method 3: The conceded-gap ledger

### Full-text evidence (08 §2, copied)

| Method | Evidence | Variant | Contradiction | Any link | Abstract-level | Say–do after reading |
|---|---|---|---|---|---|---|
| M3 Conceded-gap ledger | 73 (54) | 16 (15) | 0 | 84 (62) | S022 abstract card | ✅, but step 1 alone is near-universal; the chains are the evidence |

**Method 3 · The conceded-gap ledger**

- **What the count means.** 73 of the 92 works read in full or in part carry a Method 3 evidence link, most of them for step 1 (limits printed where they arise) and across all voices, so step 1 alone is house style rather than a distinguishing move. The distinctive evidence is the chain from a printed gap to a later project and a release:
  - exact LP: precision boosting named as the agenda in 2012 [S020 TR p. 11], the no-recovery limit printed with its remedy [S013 TR p. 23], boosting proposed inside refinement [S029 p. 26], done in 2025 from the predecessors' printed gap [S050 pp. 2, 6, 9, 14];
  - exact MIP: the remaining gap printed with the next missing technique, safe cuts [D002 p. 14; S022 p. 18], then safe Gomory cuts entering through that gap [S036 pp. 2, 23–27], certified propagation as the next missing component [S074 pp. 2, 12], and the release with exact mode and its open gaps [S021 pp. 7, 9]; exact integer programming was printed as an open task in the 2012 suite overview [S023 p. 22; S071 p. 21];
  - certificates: the 2017 future-work list [S019 pp. 10–11] and the decision analysis with partial certificates as next step [S072 pp. 14–15];
  - applications and HPC: the branch-and-price paper extended by its missing cuts and safe bounds [S092 p. 10; S085 p. 3]; a printed gap taken up by a later paper [S098 p. 21; S027 p. 12]; a rewrite of the 2020 presolve paper that prints its own gaps [S078 arXiv pp. 4, 13, 17, 20, 26–27].
- **Step 4 (import from a rival community, with it).** Pseudo-Boolean conflict analysis with Nordström [S062 pp. 1, 3, 12; S080 pp. 2–4]; VeriPB proof logging for presolve with its authors [S038 pp. 1–2, 15]; a pseudo-Boolean proof system generalised [S060 p. 12]; delta debugging from SAT and SMT, with Biere acknowledged [S065 pp. 2, 13]; QSopt_ex's boosting brought into SoPlex [S050 pp. 2, 6]; safe bounds from exact branch and price in vehicle routing [S085 p. 12]; reverse direction, MIP's LP and Gomory cuts carried into a pseudo-Boolean solver [D006 pp. 1–2].
- **Step 6 (ship it).** Undercover became a default heuristic of SCIP [S018 p. 18]; the nonlinearity score shipped on by default and exact LP as an option of SoPlex [S010 pp. 14, 20], both credited to him [S010 p. 28]; a supply-chain idea implemented through a generic proxy and switched on for all MIPs [S045 pp. 14, 21]; exact MIP ships behind one parameter [S021 pp. 7, 9].
- **Say–do.** ✅. Stated in his own voice: gaps with counts and causes turned into design proposals [S029 pp. 23–26]; every thesis chapter prints its gap and next step [S032 pp. 67, 100–101, 111, 132, 151, 159, 186].
- **Counter-evidence.** The later numerically safe step was not printed as a gap in the 2024 branch-and-price paper [S092 p. 10]; a background parallel factorization proposed in 2020 [S029 p. 25] is not taken up in any later card; a relaxator stays on a development branch [S083 pp. 13, 19–20]; losses printed with no next project [S070 pp. 15–16, 19–20, 22]; no printed limits [S076 p. 11]; entry through a predecessor's unvaried design choice, not a printed limit [S082 report pp. 4, 7–8]; qualitative limits only [S008 pp. 9, 21–22, 24; S017 TR pp. 3–4, 15, 17].

### Variants (08 §3.1, copied)

- **Method 3.** Limits printed but uncounted, without a follow-up [S008 pp. 9, 21–22, 24; D005 draft pp. 4–5]; a community-level ledger kept by seminar editors [S084 pp. 2, 23]; capability adopted from a foreign open-source solver instead of importing a mechanism [S046 p. 4; D005 draft pp. 2–3].

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Method 3 Evidence | VIPR future work → decision analysis `[NC25]` and delta debugging `[MIPDD]` | VIPR's future work names approximate certificates for debugging solvers and for measuring numerical violation [S019 p. 10]; MIP-DD gives the limits of assertions and debug solutions as its origin and mentions VIPR only as a planned interface [S065 pp. 1–2, 13] | Keep VIPR → decision analysis; mark the MIP-DD edge as inferred, with MIP-DD's own origin |
| Method 4 step 6; Method 3 Limitations (overhead forecast) | +101% FPEasy, +51% NumDiff (2021) `[ZR21-04]`; the 2017 forecast of shrinking overhead failed by 2021 | IPCO: +101.2% and +51.4% [D002 pp. 13–14]. Journal: +56.3% (fpeasy), +22% (numdiff), +46% (miplib) on both-solved instances, which it reads as confirming the 2017 measurements [S022 p. 16]. The 2017 text expected times much closer to the non-certifying solver [S019 p. 10] | Give both versions with their numbers; restate the forecast counter-evidence as: not realised in print by 2023, the journal's overheads being of the size it calls confirmed from 2017 |
| Method 3 step 5 | SoPlex as exact LP solver lost as many hard instances as it won (automatic captions) | In print: 3 more solved on fpeasy, 6 fewer on numdiff, 18 more on miplib; every loss is a chip-verification instance where refinement breaks down [S022 p. 12], and precision boosting inside SoPlex is named as next step [S022 p. 18] | Replace the caption paraphrase by the printed counts |

### T3.6 long form

**One line**: each paper prints its own gaps with numbers; each gap becomes a later project, one component at a time, until the line ships by default; where a rival already has the missing mechanism, import it.

**Evidence**:
- Stated: "the performance gap to floating-point solvers is still large" [SU23 p. 810], printed with its factors [S022 pp. 17–18]; in his own voice every thesis chapter prints its gap with a count and the next step [S032 pp. 67, 100–101, 186]; in 2021 he saw no fundamental obstacle, the supplementary techniques had to be added one by one (paraphrase) [MIP21].
- Practice, as chains: exact LP, from boosting named as the agenda in 2012 [S020 TR p. 11] and the no-recovery limit printed with its remedy [S013 TR p. 23] to boosting proposed inside refinement [S029 p. 26] and built in 2025 [PB25; S050 pp. 2, 6]; exact MIP, from safe cuts as the next missing technique [D002 p. 14; S022 p. 18] to safe Gomory cuts [S036 pp. 2, 23–27], certified propagation [S074 pp. 2, 12] and SCIP 10 with exact mode and its open gaps [S021 pp. 7, 9]; certificates, from VIPR's future work [S019 pp. 10–11] to the decision analysis with partial certificates as next step [S072 pp. 14–15]; branch and price [LCCP24; S092 p. 10] to a numerically safe version [LCCP26; S085 p. 3].
- Say–do: ✅ stated + practised, 2012–2025; full texts: 73 cards evidence (54 studies), 16 variant, 0 contradiction. Step 1 alone is house style across voices; the chains are the evidence.
- Variants/corrections:
  - ✗ VIPR's future work led to the decision analysis [S019 p. 10]; the edge to delta debugging is inferred: MIP-DD gives the limits of assertions and debug solutions as its origin and plans VIPR only as an interface [S065 pp. 1–2, 13].
  - ✗ Step 5 now rests on the printed result, not on a talk paraphrase [S022 p. 12].
  - ✗ The 2017 forecast of shrinking certificate overhead was not realised in print by 2023: the journal's overheads are of the size it reads as confirming 2017 [S019 p. 10; S022 p. 16].
  - ⚠ Counter-evidence: the numerically safe step was not printed as a gap in 2024 [S092 p. 10]; a 2020 background-factorization proposal [S029 p. 25] is taken up in no later card.

**Steps**:
1. Print the gap where it arises, with a count and a suspected cause: refinement failed on 7 of 1,202 LPs [Th pp. 55, 89; S032 pp. 67, 100–101]; 17 of 107 certificate runs hit 10 GB [VIPR; S019 p. 10]; safe cuts missing [SU23; S022 p. 18].
2. Show with Method 2 that it is missing methods, not a roadblock.
3. One project per gap: PhD positions on "high-precision mixed-integer programming over the rational numbers" (2016); open agendas for postdocs [04 G2].
4. If the gap is a rival's strength, import the mechanism and work with that community: QSopt_ex-style precision boosting in SoPlex [PB25; S050 pp. 2, 6]; VeriPB proof logging for 0-1 presolve with Nordström [CPB24; S038 pp. 1–2, 15]; pseudo-Boolean conflict analysis [S062 pp. 1, 3, 12]; delta debugging from SAT/SMT, Biere acknowledged [MIPDD; S065 pp. 2, 13]. Publish where they read (ISSAC, CP, Constraints).
5. Read a lost experiment as the next idea: with SoPlex as exact LP solver, exact SCIP solved 3 more instances on fpeasy, 6 fewer on numdiff and 18 more on miplib, every loss a chip-verification instance where refinement breaks down; precision boosting inside SoPlex was named as the next step [S022 pp. 12, 18] and built [S050 pp. 2, 5–6].
6. Stop only when it ships: SCIP 10.0.0 (24 Nov 2025), exact MIP behind one parameter [S021 pp. 7, 9]; he wrote the integration commits (411 SCIP commits in 2025) and an exact-solving Homebrew test [06 §7]. Earlier: Undercover default [S018 p. 18]; the nonlinearity score on by default and exact LP as a SoPlex option, both credited to him [S010 pp. 14, 20, 28].
7. Keep printing what is open: presolve certified only for binary programs with integer data, strong branching not made safe, Gomory mixed-integer cuts the only exact separator [S021 pp. 7, 9, 11]; the 2023 reduced comparison also had no symmetry handling [S022 p. 17].

**Applies to stage**: choosing the problem; agenda; judging.

**Different from standard practice**: problems come from the solver's printed limits and missing tools, not a literature gap; the end state is a release.

**Limitations**: a ten-year horizon with a PhD pipeline; alone, keep one printed limit per paper and close one in the next. Counter-evidence: formal certificate checking (proposed 2016) was done by others; the parallel rational factorization (thesis; proposed again in 2020 [S029 p. 25]) and the MIPLIB hindsight study [S002 p. 43] were not found later; the 2017 forecast of shrinking certificate overhead was not realised in print by 2023 [S022 p. 16].

### Changes made in SKILL.md (T3.6)

- **Evidence condensed.** Stated → "the performance gap to floating-point solvers is still large" with its factors [SU23 p. 810; S022 pp. 17–18] and the thesis's per-chapter gaps [S032 pp. 67, 100–101, 186] (08 §2, Say–do); the MIP 2021 paraphrase is in the moved-verbatim copy. Practice → the four chains of 08 §2, as card arrows. Say–do: 73 (54), 16 (15), 0, with 08's caution that step 1 alone is house style.
- **Corrections (✗)**: the delta-debugging edge is inferred, MIP-DD's own origin is the limits of assertions and debug solutions [S065 pp. 1–2, 13] (08 §3.2); step 5 now rests on print [S022 p. 12] (08 §3.2); the overhead forecast restated as "not realised in print by 2023" [S019 p. 10; S022 p. 16] (08 §3.2).
- **Steps**: step 1 + [S032 pp. 100–101; S019 p. 10; S022 p. 18]; step 4 + [S050 pp. 2, 6; S038 pp. 1–2; S065 pp. 2, 13] (the pseudo-Boolean conflict analysis [S062 pp. 1, 3, 12] is in the long form); **step 5 rewritten** from the printed result [S022 pp. 12, 18]: 3 more observations solved on fpeasy, 6 fewer on numdiff, 18 more on miplib (instance-seed pairs, the S022 card's wording), every loss a chip-verification instance; step 6 + exact MIP behind one parameter [S021 pp. 7, 9] (shipped defaults [S018 p. 18; S010 pp. 14, 20, 28] in the long form); step 7 + [S021 pp. 9–11].
- **Limitations**: counter-evidence sourced [S029 p. 25; S002 p. 43]; the forecast sentence restated (variant bullet).

### T3.6 review fixes (2026-11-28)

- **Stated** (review: a co-authored sentence without its tag, and a practice labelled own voice): the MIP 2021 paraphrase restored as Stated [MIP21]; the SU23 sentence labelled Co-authored [SU23 p. 810], its factors placed one section earlier [S022 pp. 17–18] (they are in §4.7, not in the closing sentence); the thesis's per-chapter gaps moved to Practice as own text [S032 pp. 67, 100–101, 186].
- **Say–do** one clause; **variants removed**: the inferred MIP-DD edge, the printed step 5 and the overhead forecast are in the Corrections list; the forecast and the point that a next step can come without a printed gap [S092 p. 10] moved into Limitations.
- **Step 5**: "3 more instances solved", as printed [S022 p. 12] (review: the text says instances, not observations).
- **Step 6**: the parameter named, `exact/enabled` set to true before the instance is read, certificates with `certificate/filename` [S021 p. 7].
- **Step 7** (review: no page of S021 from 6 to 13 mentions symmetry in exact mode): what SCIP 10 prints as open, presolve certified only for binary programs with integer data, strong branching not made safe, Gomory mixed-integer cuts the only exact separator [S021 pp. 7, 9, 11]. The missing symmetry handling is a 2023 fact of the reduced comparison [S022 p. 17].

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> - Stated: "the performance gap to floating-point solvers is still large" [SU23 p. 810], printed with its factors [S022 pp. 17–18]; every thesis chapter prints its gap and next step (own voice) [S032 pp. 67, 100–101, 186].
> - Practice, as chains: exact LP [S020 TR p. 11 → S013 TR p. 23 → S029 p. 26 → S050 pp. 2, 6]; exact MIP [S022 p. 18 → S036 pp. 2, 23–27 → S074 pp. 2, 12 → S021 pp. 7, 9]; certificates [S019 pp. 10–11 → S072 pp. 14–15]; branch and price [S092 p. 10 → S085 p. 3].
> - Say–do: ✅ stated + practised, 2012–2025; full texts: 73 cards evidence (54 studies), 16 variant, 0 contradiction; step 1 alone is house style, the chains are the evidence.
> - Variants/corrections:
>   - ✗ VIPR → delta debugging is inferred; MIP-DD names its own origin [S065 pp. 1–2, 13].
>   - ✗ Step 5 rests on the printed result, not a talk [S022 p. 12].
>   - ✗ The 2017 overhead forecast was not realised in print by 2023 [S019 p. 10; S022 p. 16].
>   - ⚠ Not every next step was printed as a gap [S092 p. 10].
> 5. Read a lost experiment as the next idea: with SoPlex as exact LP solver, 3 more observations solved on fpeasy, 6 fewer on numdiff, 18 more on miplib, every loss a chip-verification instance where refinement breaks down; boosting became the next step [S022 pp. 12, 18].
> 6. Stop only when it ships: SCIP 10.0.0 (24 Nov 2025), exact MIP behind one parameter [S021 pp. 7, 9]; he wrote the integration commits (411 SCIP commits in 2025) and an exact-solving Homebrew test [06 §7].
> 7. Keep printing what is open (presolve certification for general MIP; symmetry in exact mode) [S021 pp. 9–11].
> **Limitations**: a ten-year horizon with a PhD pipeline; alone, keep one printed limit per paper and close one in the next. Counter-evidence: formal certificate checking (proposed 2016) was done by others; the parallel rational factorization and the MIPLIB hindsight study were not found [S029 p. 25; S002 p. 43].


### Before T3.6 (moved verbatim)

**One line**: each paper prints its own gaps with numbers; each gap becomes a later project, one component at a time, until the line ships by default; where a rival already has the missing mechanism, import it.

**Evidence**:
- Stated: in 2021 he saw no fundamental obstacle; the supplementary techniques had to be added one by one (paraphrase) [MIP21]; "the performance gap to floating-point solvers is still large" [SU23 p. 810].
- Practice: thesis limits → precision boosting [PB25]; VIPR future work → decision analysis [NC25] and delta debugging [MIPDD]; status update → safe cuts [GMI24] → certified propagation [CPDP24] → SCIP 10.0 [S10]; branch and price [LCCP24] → numerically safe version [LCCP26].
- Say–do consistency: ✅ stated and practised, 2015–2025.

**Steps**:
1. Print the gap where it arises, with a count and a suspected cause: refinement failed on 7 of 1,202 LPs [Th pp. 55, 89]; 17 of 107 certificate runs hit 10 GB [VIPR]; safe cuts missing [SU23].
2. Show with Method 2 that it is missing methods, not a roadblock.
3. One project per gap: PhD positions on "high-precision mixed-integer programming over the rational numbers" (2016); open agendas for postdocs [04 G2].
4. If the gap is a rival's strength, import the mechanism and work with that community: QSopt_ex-style precision boosting in SoPlex [PB25]; VeriPB proof logging for 0-1 presolve with Nordström [CPB24]; delta debugging from SAT/SMT [MIPDD]. Publish where they read (ISSAC, CP, Constraints).
5. Read a lost experiment as the next idea: SoPlex as exact LP solver lost as many hard instances as it won, so he expected a combination with QSopt_ex to pay off (paraphrase, automatic captions) [MIP21].
6. Stop only when it ships: SCIP 10.0.0 (24 Nov 2025); he wrote the integration commits (411 SCIP commits in 2025) and an exact-solving Homebrew test [06 §7].
7. Keep printing what is open (presolve certification for general MIP; symmetry in exact mode).

**Applies to stage**: choosing the problem; agenda; judging.

**Different from standard practice**: problems come from the solver's printed limits and missing tools, not a literature gap; the end state is a release.

**Limitations**: a ten-year horizon with a PhD pipeline; alone, keep one printed limit per paper and close one in the next. Counter-evidence: formal certificate checking (proposed 2016) was done by others; the thesis's parallel rational factorization and the MIPLIB hindsight study were not found; the 2017 forecast of shrinking certificate overhead failed by 2021.

<a id="method-4"></a>

## Method 4: Certificates someone else can check, read as an audit of the reasoning

### Full-text evidence (08 §2, copied)

| Method | Evidence | Variant | Contradiction | Any link | Abstract-level | Say–do after reading |
|---|---|---|---|---|---|---|
| M4 Certificates someone else can check | 17 (13) | 18 (14) | 0 | 30 (22) | S022 abstract card | ⚠ partial, unchanged |

**Method 4 · Certificates someone else can check**

- **Strongest cards.** The format with few inference rules, verification independent of how statements were made, and a checker that is only a reference [S019 pp. 3–5, 8–9]; a certificate plus a Coq check that the certificate encodes the intended model [S042 pp. 2–3, 10] (group); certificates extended to bound-shift, coverage printed (presolve must be off), and a certificate that exposed incorrect root reasoning behind a correct infeasibility verdict [D002 pp. 13–14; S022 pp. 15–16]; VeriPB now certifying presolve, the stage exact-MIP certificates left out [S038 pp. 2, 6–11] (group); the release names a formally verified checker and states coverage [S021 pp. 7, 10–11]; solver-independent checks in the delta debugger [S065 pp. 2, 5–6, 13]; the MIPLIB checkers reading the original file [S001 TR p. 10; S002 pp. 22–23]; a floating-point MILP solution checked by a second exact program [S037 p. 10]; Farkas rays double-checked before use [D004 p. 22].
- **Quote**: "Mathematically proven exactness of an algorithm is clearly not sufficient to ensure that the algorithm is implemented without errors." [S021 p. 10]
- **Say–do.** ⚠ partial, unchanged. In 2017 simplicity is offered in place of testing the checker [S019 pp. 4, 8]; in 2025 the release states that a certificate guarantees correct reasoning without a word on the reference checker's own soundness [S021 p. 10], while naming a formally verified checker [S021 p. 11].
- **New step (variant, 3 studies):** the solver writes what it knows cheaply during the solve, and a separate tool trims or completes the certificate afterwards, so the checker stays unchanged: dependency-graph trimming [S019 pp. 8–9]; completion of weakly dominating derivations [S036 pp. 18–20]; repair of conflict constraints after solving [S074 p. 8]. Quote: "This has the benefit of not complicating the logic used inside the proof checker itself." [S036 p. 18]
- **Step 5 (read the certificate for the reasoning).** The decision analysis records errors justified in hindsight: "We still record these errors, because we are interested not only in the correctness of the final result but in the correctness of the floating-point solver’s reasoning that led to the result." [S072 p. 5]

### Variants (08 §3.1, copied)

- **Method 4.** Correctness screened, not certified, in floating-point releases [S003 pp. 7, 16, 26; S014 pp. 72–73; S015 p. 9]; the input checked by redundant annotation of user structure [S046 p. 5]; a proof system without a checker yet, whose advanced verifier would trade the simple-checker ideal for smaller certificates [S060 pp. 8, 12, 24]; certification derived but not exercised [S074 p. 8]; numerical safety without certificate or independent check [S085 pp. 12–14].

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Method 4 step 6; Method 3 Limitations (overhead forecast) | +101% FPEasy, +51% NumDiff (2021) `[ZR21-04]`; the 2017 forecast of shrinking overhead failed by 2021 | IPCO: +101.2% and +51.4% [D002 pp. 13–14]. Journal: +56.3% (fpeasy), +22% (numdiff), +46% (miplib) on both-solved instances, which it reads as confirming the 2017 measurements [S022 p. 16]. The 2017 text expected times much closer to the non-certifying solver [S019 p. 10] | Give both versions with their numbers; restate the forecast counter-evidence as: not realised in print by 2023, the journal's overheads being of the size it calls confirmed from 2017 |

### T3.6 long form

**One line**: attach a certificate simple enough for an independent checker, use it to find wrong reasoning behind right answers, and test the checker itself.

**Evidence**:
- Stated: "We again emphasize that the format was designed with simplicity in mind; the certificate verification program we have provided is merely a reference and others should be able to write their own verifiers without much difficulty." (co-authored) [VIPR; S019 p. 8]; also [VIPR §1] and [Sim21 01:53] (Research Taste).
- Practice: VIPR's few inference rules, checked independently of how the statements were made [S019 pp. 3–5, 8–9]; a Coq check that the certificate encodes the intended model (group) [Chv22; S042 pp. 2–3, 10]; certificates extended to bound-shift with coverage printed (presolve off), and in 2021 a certificate showed the 2013 framework declared a NumDiff instance infeasible at the root for an incorrect reason, although it is infeasible [ZR21-04 §4; D002 pp. 13–14; S022 pp. 15–16]; VeriPB certifying presolve, the stage exact-MIP certificates left out (group) [S038 pp. 2, 6–11]; the release names a formally verified checker and its coverage [S021 pp. 7, 10–11].
- Say–do: ⚠ partial, unchanged: in 2017 simplicity stands in for testing the checker [S019 pp. 4, 8], and the reference checker had holes 2016–2026 (Limitations); full texts: 17 cards evidence (13 studies), 18 variant, 0 contradiction.
- Variants/corrections:
  - ✗ Step 6's overheads differ by version: IPCO +101.2% (FPEasy), +51.4% (NumDiff) [D002 pp. 13–14]; journal +56.3% (fpeasy), +22% (numdiff), +46% (miplib) on both-solved instances [S022 p. 16].
  - ⚠ New step 8: write cheaply online, trim or complete offline, checker unchanged [S019 pp. 8–9; S036 pp. 18–20; S074 p. 8].
  - ⚠ Correctness screened, not certified, in floating-point releases [S003 pp. 7, 16, 26; S015 p. 9]; a proof system whose advanced verifier would trade the simple-checker ideal for smaller certificates [S060 pp. 8, 12, 24].
  - ✗ MIPLIB's solution checks compute in arbitrary precision but accept by tolerances; objective values are recomputed exactly [S002 pp. 22, 42].

**Steps**:
1. Write the certificate as statements each checkable by a few inference rules, independent of how the solver found them (PD9) [S019 pp. 5–8].
2. Ship a reference checker that needs no MIP knowledge; publish certificates and per-instance tables [S019 pp. 4, 9].
3. Check the input too: does the certificate encode the intended model? (DM7) [S042 pp. 2–3]
4. Cross-check without the producing solver: each solution against the original file in exact or arbitrary-precision arithmetic (MIPLIB 2017: GMP arithmetic, acceptance by tolerance, objective values recomputed exactly [S002 pp. 22, 42]); a verified solution beating another solver's dual bound flags the instance [S002 p. 23].
5. Read the certificate for the reasoning, not only the verdict: "We still record these errors, because we are interested not only in the correctness of the final result but in the correctness of the floating-point solver’s reasoning that led to the result." [S072 p. 5]
6. Print coverage and cost, naming the version: presolve, dual reductions, symmetry outside; time overhead on both-solved instances, +101% on FPEasy and +51% on NumDiff in the IPCO version [ZR21-04; D002 pp. 13–14], +56.3%, +22% and +46% in the journal [S022 p. 16]; capped runs in their own rows (EP11) [S019 p. 9].
7. Test the checker as code (H1): differential tests against a second, ideally formally verified, checker before writing "verified".
8. Write what the solver knows cheaply during the solve and trim or complete the certificate offline, so that the checker stays unchanged (DM6): "This has the benefit of not complicating the logic used inside the proof checker itself." [S036 p. 18]

**Applies to stage**: experiment design; judging; after publication.

**Different from standard practice**: neither trusting the solver nor re-solving with another; a third, simpler program decides.

**Limitations**: only as strong as checker and specification. A simple format did not make the reference checker `viprchk` sound: bugs 2016–2026 (a solution tested against one constraint only, fixed Dec 2024; rounding over continuous variables accepted, reported Oct 2026); he fixed two, Hoen one, outsiders reported the rest [VIPR-gh]. Forged certificates were accepted in 2023 [Wood23], with no printed reply. SCIP 10 points to the CakeML-verified checker [S10; S021 p. 11]. Presolve is outside, and two exact-mode wrong answers in Oct 2026 came from PaPILO presolve bugs [SCIP-iss]. Whether any published certificate relied on a hole was never examined. The release's own words: "Mathematically proven exactness of an algorithm is clearly not sufficient to ensure that the algorithm is implemented without errors." (group) [S021 p. 10]

### Changes made in SKILL.md (T3.6)

- **Evidence condensed.** Stated → the VIPR sentence on the reference checker, quoted in part [S019 p. 8] (whole quotation in the long form). Practice → [S019 pp. 3–5, 8–9], [Chv22; S042 pp. 2–3], [ZR21-04 §4; S022 pp. 15–16], [S038 pp. 2, 6–11]. Say–do stays ⚠ partial: 17 (13), 18 (14), 0 (08 §2: simplicity offered in place of testing the checker [S019 pp. 4, 8]); the GitHub record of checker bugs moved from the old Say–do line to Limitations, in shorter form (the bug descriptions are in the moved-verbatim copy).
- **Corrections (✗)**: step 6 now names the version of each overhead: IPCO +101.2% / +51.4% [D002 pp. 13–14], journal +56.3% / +22% / +46% on both-solved instances [S022 p. 16] (08 §3.2); MIPLIB's solution checks are arbitrary-precision tolerance checks with exact objective values [S002 pp. 22, 42] (08 §3.2).
- **New step 8** (08 §2, Method 4, new step; 3 studies): write cheaply online, trim or complete offline, checker unchanged (DM6) [S019 pp. 8–9; S036 pp. 18–20; S074 p. 8]; the quotation [S036 p. 18] is in the long form.
- **Steps**: step 2 + [S019 p. 9]; step 5 + the decision-analysis reason [S072 p. 5] (quotation in the long form); step 6 rewritten with both versions.
- **Variant bullet**: screened, not certified, in floating-point releases [S003 pp. 7, 16] (08 §3.1); the proof-system variant [S060 pp. 8, 12, 24] is in the long form.

### T3.6 review fixes (2026-11-28)

- **Stated** (review): his own talk sentence [Sim21 01:53] restored as Stated; the VIPR sentence labelled Co-authored [S019 p. 8].
- **Say–do** one clause; **variants**: the ✗ overhead bullet is in the Corrections list and step 6; the step 8 bullet removed (step 8 itself stays, now labelled group, DM6 [S036 p. 18]); two ⚠ scope conditions remain: releases screen, not certify [S003 pp. 7, 16]; a library checker accepts within tolerances [S002 pp. 22–23].
- **Step 1** (review: the presolve certification recipe was only in the cards): PD6 named; for presolve on 0-1 programs (group, VeriPB): classify each reduction as primal, weak dual or strong dual; primal ones by implication (cutting planes, reverse unit propagation), dual ones by redundance-based strengthening with a witness substitution; aggregation scales split into integers s_E/s_D [S038 pp. 4, 6–10].
- **Step 4** (review: the ✗ bullet had removed its only support): integers fixed and the rest solved by a second, exact LP solver (co-authored) [S037 p. 10]; solver-independent checks against a reference solution (group) [S065 pp. 2, 5–6]; the dual-bound flag [S002 p. 23].
- **Step 6** (review: the journal figures lacked their sets): +56.3% fpeasy, +22% numdiff, +46% miplib solving time, 92.5%, 32.8%, 65.8% with checking (Table 9) [S022 p. 16]; presolve proof logging under 6%, checking 14.7 to 22.4 times the presolve time, at least 193 times on a quarter of the instances (group) [S038 pp. 12–13]; EP11 named.
- **Limitations**: the VeriPB objective-update rule comes without a formal proof in the paper (group) [S038 p. 5].

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> - Stated: the reference checker is "merely a reference and others should be able to write their own verifiers without much difficulty" (co-authored) [VIPR; S019 p. 8].
> - Say–do: ⚠ partial, unchanged: simplicity stands in for testing the checker [S019 pp. 4, 8], which had holes (Limitations); full texts: 17 cards evidence (13 studies), 18 variant, 0 contradiction.
> - Variants/corrections:
>   - ✗ Step 6's overheads differ by version [D002 pp. 13–14; S022 p. 16].
>   - ⚠ New step 8 [S019 pp. 8–9; S036 pp. 18–20; S074 p. 8].
>   - ⚠ Screened, not certified, in floating-point releases [S003 pp. 7, 16].
>   - ✗ MIPLIB's checks accept by tolerances [S002 p. 22].
> 1. Write the certificate as statements each checkable by a few inference rules, independent of how the solver found them (PD9).
> 4. Cross-check without the producing solver: each solution against the original file in exact arithmetic; a verified solution beating another solver's dual bound flags the instance.
> 6. Print coverage and cost with the version: presolve, dual reductions, symmetry outside; +101% time on FPEasy, +51% on NumDiff (IPCO 2021) [ZR21-04; D002 pp. 13–14], +56.3%, +22%, +46% in the journal [S022 p. 16].
> 8. Write what the solver knows cheaply during the solve; trim or complete the certificate offline, so that the checker stays unchanged (DM6) [S036 p. 18].


### Before T3.6 (moved verbatim)

**One line**: attach a certificate simple enough for an independent checker, use it to find wrong reasoning behind right answers, and test the checker itself.

**Evidence**:
- Stated: [VIPR §1] and [Sim21 01:53] (see Research Taste).
- Practice: VIPR [VIPR]; a Coq check that the certificate encodes the intended model [Chv22]; independent solution checking [M17 §4.7]; in 2021 a certificate showed the 2013 framework declared a NumDiff instance infeasible at the root for an incorrect reason, although it is infeasible [ZR21-04 §4].
- Say–do consistency: ⚠️ partial. A simple format did not make the reference checker `viprchk` sound: bugs 2016–2026 (a solution tested against one constraint only, fixed Dec 2024; rounding over continuous variables accepted, reported Oct 2026); he fixed two, Hoen one, outsiders reported the rest [VIPR-gh]. Forged certificates were accepted in 2023 [Wood23], with no printed reply. SCIP 10 points to the CakeML-verified checker [S10].

**Steps**:
1. Write the certificate as statements each checkable by a few inference rules, independent of how the solver found them.
2. Ship a reference checker that needs no MIP knowledge; publish certificates and per-instance tables.
3. Check the input too: does the certificate encode the intended model?
4. Cross-check without the producing solver: each solution against the original file in exact arithmetic; a verified solution beating another solver's dual bound flags the instance.
5. Read the certificate for the reasoning, not only the verdict.
6. Print coverage and cost: presolve, dual reductions, symmetry outside; +101% time on FPEasy, +51% on NumDiff (2021) [ZR21-04].
7. Test the checker as code (H1): differential tests against a second, ideally formally verified, checker before writing "verified".

**Applies to stage**: experiment design; judging; after publication.

**Different from standard practice**: neither trusting the solver nor re-solving with another; a third, simpler program decides.

**Limitations**: only as strong as checker and specification; presolve is outside, and two exact-mode wrong answers in Oct 2026 came from PaPILO presolve bugs [SCIP-iss]. Whether any published certificate relied on a hole was never examined.

<a id="method-5"></a>

## Method 5: Floating point produces, exact arithmetic decides

### Full-text evidence (08 §2, copied)

| Method | Evidence | Variant | Contradiction | Any link | Abstract-level | Say–do after reading |
|---|---|---|---|---|---|---|
| M5 Floating point produces, exact decides | 28 (21) | 21 (15) | 0 | 43 (31) | D001, S022 abstract card | ✅ |

**Method 5 · Floating point produces, exact arithmetic decides**

- **Strongest cards.** The design itself in LP refinement [S020 TR pp. 3, 5, 7–8, 11; S013 TR pp. 3, 6, 9–11, 15–16] and in the thesis [S032 pp. 15, 39–40, 45, 85, 89–92] (own); the limited-precision oracle paper [S029 pp. 7–8, 10, 12, 15, 24–26] (own); QP refinement with all work except the oracle solves in rationals [S058 pp. 6, 12]; exact MIP: heuristics on floating-point data with exact repair, a running-error pre-check, a padded objective limit, bound-shift switched off below 20% success, rational presolve [D002 pp. 4, 7–10; S022 pp. 2, 5–8, 10, 12–14]; safe cuts by directed rounding, exact LPs only when needed [S036 pp. 5–8, 18–19, 24]; safe propagation, with the stated reason that symbolic computation is too slow [S074 pp. 2, 6–7, 10–12]; the release [S021 pp. 7–10]; boosting only on named failures [S050 pp. 4–6, 10]; a cheapest-check-first ladder in the decision analysis [S072 pp. 6–8, 14]; integer-arithmetic duals and pricing in branch-price-and-cut [S085 pp. 12–14, 16, 21]; the same split outside MIP, in a pseudo-Boolean solver [S024 pp. 3, 6, 10, 14–15]. Earliest form of the repair device (fix the rounded integers, solve the rest exactly), in the 2011 group text [S001 TR pp. 9, 11, 17–18]; his own 2016 code ships exact LP as verification and reconstruction steps around floating-point refinement, floating point the default [S010 p. 20].
- **Say–do.** ✅. Stated in the thesis [S032 p. 15], in the oracle paper [S029 p. 7] and in a group paper [S074 p. 2]; practised in 21 studies.
- **Variants** (15 studies): see §3.1.

### Variants (08 §3.1, copied)

- **Method 5.** (a) Floating-point safety where no exact arithmetic runs: only the validity-deciding tolerance tightened [S011 p. 14]; a tighter internal tolerance than the reporting tolerance, and rounding-safe interval arithmetic for bounds [S006 pp. 7, 19]; double-double where round-off threatens validity [S003 pp. 11–13, 18, 25]; bounds, sides and coefficients relaxed before propagation, cut clean-up and an enforcement ladder with counters [S004 pp. 31, 33–38]; safeguards where a number becomes a bound [S014 pp. 35–36, 46; S045 pp. 17–18]. (b) The producer's accuracy matched to its role: loose oracle settings because rational residuals catch the errors [S058 p. 12]; a loose first-order LP tightened geometrically [S061 pp. 3–4]; low-accuracy LP iterates only guide heuristics [S076 pp. 8–9]. (c) Exactness at the cheapest stage, in model building [S023 p. 9; S071 p. 7]. (d) Precision chosen by measuring the correctness loss [S067 arXiv pp. 15–16]. (e) The boundary not drawn: OBBT bounds from floating-point LPs in the thesis's MINLP half [S032 pp. 146, 149]; a floating-point conic bound with no independent check [S083 pp. 12, 15, 17]; in a circle-packing paper, the bounds called exact and verified are computed with floating-point solvers and tolerances are not discussed [S041 pp. 3–5, 17, 21, 23]; no exact decider between two codes reaching different fixed points [D003 pp. 4, 10]. (f) Analogues on model resolution rather than arithmetic, inferred by the readers [S025 pp. 89, 94–95; S008 pp. 10–11, 16–17].

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Method 5 step 5 | boosting inside refinement | Proposed so in 2020 [S029 p. 26]; as built, an outer precision-boosting loop around an inner refinement loop, both on by default [S007 p. 16; S050 pp. 5–8] | Name both: the proposal and the built order |
| Method 5 Limitations | the 2025 paper replaces 2016's rational reconstruction by basis factorization on average | The thesis already finds the rational factorization about 46% faster on average [S032 p. 100]; the 2020 paper restates it [S029 p. 25]; the 2025 paper confirms it [S050 p. 10]; reconstruction and verification both shipped in 2016 [S010 p. 20] | Date the result to the thesis (2015) |
| Method 5 Limitations | refinement has no reliable recovery when the floating-point LP fails | Printed in 2016 with the remedy [S013 TR p. 23] and in 2023 [S022 p. 7]; a heuristic recovery existed in the QP code [S058 p. 12]; precision boosting provides it from 2025 [S050 pp. 2, 5–6] | Date it: true for LP refinement until 2025 |
| Method 5 step 6 | check the optimality of the basis early `[LPO20]` | Already in the thesis, own voice [S032 p. 85]; then [S029 p. 12] | Credit the thesis first |

### T3.6 long form

**One line**: do the expensive work in floating point; use exact arithmetic only for corrections, critical decisions and the final check.

**Evidence**:
- Stated: "Its computational efficiency rests on its mixed-precision nature" [Th p. 3; S032 p. 15]; "exact computation is used for critical decisions or to validate final solutions" [LPO20 §1.3, co-authored; S029 p. 7].
- Practice: LP refinement solves in floating point, computes residuals, corrections and checks in rationals [S020 TR pp. 3, 5, 7; S032 pp. 39–40, 85, 89–92]; "Primal heuristics are exclusively executed on the floating-point approximation of the rational input data", with exact repair, a running-error pre-check and bound-shift off below 20% success [SU23 p. 794; S022 pp. 2, 5–8, 12]; safe Gomory cuts by directed rounding, exact LPs only when needed [S036 pp. 5–8, 18–19]; safe propagation [S074 pp. 2, 6–7]; integer-arithmetic duals in branch-price-and-cut [S085 pp. 12–14].
- Say–do: ✅ stated about eight times (2014–2025) [S032 p. 15; S029 p. 7; S074 p. 2], practised in 21 studies; full texts: 28 cards evidence (21 studies), 21 variant, 0 contradiction.
- Variants/corrections:
  - ✗ Step 5 as built: an outer precision-boosting loop around inner refinement, both on by default [S007 p. 16; S050 pp. 5–8]; "inside refinement" was the 2020 proposal [S029 p. 26].
  - ✗ Limitations dated: the no-recovery limit was printed in 2016 with its remedy [S013 TR p. 23] and in 2023 [S022 p. 7] and lifted by boosting in 2025 [S050 pp. 2, 5–6]; basis verification beat reconstruction on average already in 2020 [S029 p. 25].
  - ⚠ Floating-point safety where no exact arithmetic runs: only the validity-deciding tolerance tightened [S011 p. 14]; double-double where round-off threatens validity [S003 pp. 11–13]; a tighter internal tolerance than the reported one [S006 pp. 7, 19].
  - ⚠ The boundary is not drawn everywhere: OBBT bounds from floating-point LPs in the thesis's MINLP half [S032 pp. 146, 149]; a floating-point conic bound with no independent check [S083 pp. 12, 15, 17].

**Steps**:
1. Split the algorithm into what produces information (basis, candidate, cut, reduction) and what decides correctness (bound, feasibility, final answer); what changes the model (presolve) runs in rationals [S022 pp. 5, 13].
2. Leave the producing part in floating point; no rational twin. An in-solver heuristic should spend small, bounded effort, so a rational sub-MIP is "not called for" [Sim21 01:38–01:41].
3. Repair exactly: fix rounded integers and solve the rest exactly (first in the 2011 group text [S001 TR pp. 9, 11]; with filters and a failure limit, DM1 [S022 pp. 5–6, 14]); in LP keep the basis and compute residuals and corrections in rationals.
4. Prefer safe directed rounding for bounds, exact LP as fallback; give each cheap safe method a switch-off rule (bound-shift off below 20% success [ZR21-04 p. 8; S022 p. 12]); decide most rows by running error analysis and recompute only the undecided band exactly (PD7) [S022 pp. 7–8].
5. Raise precision only on failure: proposed as boosting inside refinement [S029 p. 26], built as an outer boosting loop around refinement [S050 pp. 5–8]; the failure triggers are Method 7 step 5.
6. "check the optimality of the basis early" instead of relying on a priori bounds [LPO20; S029 p. 12], already in the thesis [S032 p. 85].
7. Write generic code so the exact variant is cheap (H10).

**Applies to stage**: algorithm design; deciding what must be exact.

**Different from standard practice**: neither all floating point nor all rational; the producing/deciding boundary is the design decision.

**Limitations**: LP refinement had no reliable recovery when the floating-point LP fails until boosting arrived in 2025 [S050 p. 2]; outside benchmarks found exact SoPlex buggy or slower than pure boosting on one LP family; basis factorization beats rational reconstruction on average since the thesis [S032 p. 100], restated in 2020 [S029 p. 25] and confirmed in 2025 [PB25; S050 p. 10]. Exact repair (step 3) is shown for LP and MILP only (fix a basis or the integers, correct the rest exactly); for cone constraints such as SDP, repair at the cone boundary is harder (inferred) and untested in his work: any transfer is an inference.

### Changes made in SKILL.md (T3.6)

- **Evidence condensed.** Stated → the thesis sentence [Th p. 3; S032 p. 15] and the oracle-paper sentence [LPO20 §1.3; S029 p. 7]; the Simons talk remark on rational heuristics is in the moved-verbatim copy. Practice → [S020 TR pp. 3, 5, 7; S032 pp. 39–40, 85], [SU23 p. 794; S022 pp. 2, 5–8], [S036 pp. 5–8, 18–19], [S074 pp. 2, 6–7]. Say–do: 28 (21), 21 (15), 0.
- **Corrections (✗)**: step 5 names the built order, an outer boosting loop around refinement [S050 pp. 5–8] (08 §3.2; also [S007 p. 16]); Limitations dated: no reliable recovery until boosting in 2025 [S050 p. 2], printed earlier with its remedy [S013 TR p. 23] (and [S022 p. 7]); basis factorization ahead of reconstruction, there dated to 2020 [S029 p. 25] (08 §3.2; corrected in the review fixes below: since the thesis [S032 p. 100]). Step 6 credits the thesis first [S032 p. 85] (08 §3.2).
- **Variant bullets**: floating-point safety without exact arithmetic [S011 p. 14; S003 pp. 11–13] (08 §3.1 (a)); the boundary not drawn everywhere [S032 pp. 146, 149; S083 p. 15] (08 §3.1 (e)).
- **Steps**: step 1 + model-changing work in rationals [S022 pp. 5, 13]; step 3 + filters and failure limit (DM1) [S022 pp. 5–6, 14] (the 2011 origin [S001 TR pp. 9, 11] is in the long form); step 4 + [S022 p. 12] and the running error analysis (PD7) [S022 pp. 7–8]; step 5 rewritten (proposal [S029 p. 26] and built order); step 6 + [S029 p. 12; S032 p. 85].

### T3.6 review fixes (2026-11-28)

- **Stated** (review: the own-voice reason behind step 2 and Warning sign 7 had gone): the Simons talk remark on rational heuristics restored [Sim21 01:38–01:41]. **Practice**: the SU23 sentence labelled co-authored; safe cuts and propagation labelled group.
- **Say–do** one clause; **variants**: the two ✗ bullets are in the Corrections list (one of them, *Limitations dated*, was unreadable without the ledger); two ⚠ scope conditions rewritten to act on: where no exact arithmetic runs, tighten only the validity tolerance [S011 p. 14], double-double where round-off threatens a bound [S003 pp. 11–13], count numerical fallbacks [S004 p. 38] (DM13); his MINLP-side work leaves OBBT and conic bounds in floating point [S032 pp. 146, 149; S083 p. 15].
- **Step 4**: PD6 and DM2 named. **Step 6** (review: Method 5 no longer said how to verify the final basis, and the factorization result was misdated to 2020): an exact factorization of the final basis, ahead of rational reconstruction on average since the thesis, "about 46% faster on average" there [S032 p. 100], restated in 2020 [S029 p. 25]; in 2020 fastest on 702 of 1,202 LPs against 569 under the 5% rule, 1,191 against 1,189 solved, one factorization on 1,123 [S029 pp. 23–24]; confirmed 2025 [S050 p. 10]; reconstruction still wins on some LPs [S029 p. 25]; the rational LU can become the bottleneck [S050 p. 14].

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> - Stated: "Its computational efficiency rests on its mixed-precision nature" [Th p. 3; S032 p. 15]; "exact computation is used for critical decisions or to validate final solutions" [LPO20 §1.3, co-authored; S029 p. 7].
> - Practice: LP refinement [S020 TR pp. 3, 5, 7; S032 pp. 39–40, 85]; "Primal heuristics are exclusively executed on the floating-point approximation of the rational input data" [SU23 p. 794; S022 pp. 2, 5–8]; safe Gomory cuts [S036 pp. 5–8, 18–19]; safe propagation [S074 pp. 2, 6–7].
> - Say–do: ✅ stated about eight times (2014–2025), practised in 21 studies; full texts: 28 cards evidence (21 studies), 21 variant, 0 contradiction.
> - Variants/corrections:
>   - ✗ Step 5 as built: an outer boosting loop around refinement [S050 pp. 5–8].
>   - ✗ Limitations dated [S013 TR p. 23; S029 p. 25].
>   - ⚠ Floating-point safety where no exact arithmetic runs [S011 p. 14; S003 pp. 11–13].
>   - ⚠ The boundary is not drawn everywhere [S032 pp. 146, 149; S083 p. 15].
> 4. Prefer safe directed rounding for bounds, exact LP as fallback; give each cheap safe method a switch-off rule (bound-shift off below 20% success [ZR21-04 p. 8; S022 p. 12]); decide most rows by running error analysis (PD7) [S022 pp. 7–8].
> 6. "check the optimality of the basis early" instead of relying on a priori bounds [LPO20; S029 p. 12], already in the thesis [S032 p. 85].


### Before T3.6 (moved verbatim)

**One line**: do the expensive work in floating point; use exact arithmetic only for corrections, critical decisions and the final check.

**Evidence**:
- Stated: "Its computational efficiency rests on its mixed-precision nature" [Th p. 3]; "exact computation is used for critical decisions or to validate final solutions" [LPO20 §1.3, co-authored]; rational heuristics were skipped not only because "we were lazy": an in-solver heuristic should spend small, bounded effort, so a rational sub-MIP is "not called for" [Sim21 01:38–01:41].
- Practice: iterative refinement for LP [ISSAC12; IR16]; "Primal heuristics are exclusively executed on the floating-point approximation of the rational input data" [SU23 p. 794]; safe Gomory cuts [GMI24]; precision boosting [PB25]; bound-shift switched off below a 20% success rate [ZR21-04 p. 8].
- Say–do consistency: ✅ stated about eight times (2014–2025), practised in six projects.

**Steps**:
1. Split the algorithm into what produces information (basis, candidate, cut, reduction) and what decides correctness (bound, feasibility, final answer).
2. Leave the producing part in floating point; no rational twin.
3. Repair exactly: fix rounded integers and solve the rest exactly; in LP keep the basis and compute residuals and corrections in rationals.
4. Prefer safe directed rounding for bounds, exact LP as fallback; give each cheap safe method a switch-off rule.
5. Raise precision only on failure (boosting inside refinement).
6. "check the optimality of the basis early" instead of relying on a priori bounds [LPO20].
7. Write generic code so the exact variant is cheap (H10).

**Applies to stage**: algorithm design; deciding what must be exact.

**Different from standard practice**: neither all floating point nor all rational; the producing/deciding boundary is the design decision.

**Limitations**: refinement has no reliable recovery when the floating-point LP fails [PB25]; outside benchmarks found exact SoPlex buggy or slower than pure boosting on one LP family; his group's 2025 paper replaces 2016's rational reconstruction by basis factorization on average [PB25]. Exact repair (step 3) is shown for LP and MILP only (fix a basis or the integers, correct the rest exactly); for cone constraints such as SDP, repair at the cone boundary is harder (inferred) and untested in his work: any transfer is an inference.

<a id="method-6"></a>

## Method 6: A benchmark is a designed instrument

### Full-text evidence (08 §2, copied)

| Method | Evidence | Variant | Contradiction | Any link | Abstract-level | Say–do after reading |
|---|---|---|---|---|---|---|
| M6 A benchmark is a designed instrument | 19 (13) | 27 (24) | 1 (1) | 41 (32) | — | ✅, with three factual corrections |

**Method 6 · A benchmark is a designed instrument**

- **Strongest cards.** MIPLIB 2017: purpose and non-purpose, licence, checker, selection models with free constants and a sensitivity table, feature validation, KS tests of the hardness claim, published manual decisions and a minimal exchange after flawed instances [S002 pp. 3, 6, 20, 22–23, 27–38, 40–44] (lead author of 16; committee voice). Its predecessor MIPLIB 2010 [S001 TR pp. 6–8, 10, 19, 21] (group). QPLIB as a hand-made relative [S009 pp. 2, 8, 13–16, 21]. The reoptimization competition with hidden series, written rules, loopholes closed and invalid answers penalised [S055 pp. 2–3, 6–7]; the ML4CO competition with hidden test sets and solver-computed bounds [S016 pp. 3–5, 8]. Development test sets built by counted funnels [S003 pp. 6–7] or by MIPLIB 2017's own selection model [S005 pp. 6–7] (group). A public library solved in exact arithmetic, wrong literature values named [S058 p. 14]. Step 9 in practice: tolerance-feasible but exactly infeasible instances kept out [S022 pp. 14, 17; S036 p. 21]; release reports drop numerically inconsistent runs from their version comparisons [S021 p. 5].
- **Say–do.** ✅, with three corrections (§3.2).
- **Counter-case.** Runs whose solutions violate the constraints scored as successes in a student-project paper [S069 p. 23].

---

### Variants (08 §3.1, copied)

- **Method 6.** Committee selection with hard and soft requirements, and unstable instances kept as their own test set [S001 TR pp. 6–8]; a manual similarity filter and no solution checks [S009 pp. 16, 21]; designed instance families instead of collected ones [S024 pp. 17–18, 25–26; S041 pp. 22–25; S092 p. 10; S087 pp. 26–28]; a partner's public artificial twin of a private set [S073 pp. 10–11, 14]; inconsistent runs dropped without a count [S004 p. 4; S007 pp. 4, 6; S080 pp. 20–21].

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Method 6 step 2 | licence CC BY 4.0 | Default instance licence CC BY-SA 4.0 [S002 p. 6]; CC BY 4.0 is the article's own licence [S002 p. 44] | Correct |
| Method 6 step 3; Taste 1 | every reported solution checked against the original file in exact arithmetic | The checker computes in GMP arbitrary precision but accepts by tolerances, because exact feasibility cannot be expected [S002 p. 22]; objective values of reported solutions are recomputed exactly by fixing the integers [S002 p. 42] | Say arbitrary-precision tolerance checks, plus exact objective values |
| Method 6 step 7 | v2 exchanged five instances | The paper names the two flawed instances and the minimal-exchange use of the selection model, not the count five [S002 pp. 43–44] | Source the five to the changelog only |
| Method 6 step 8 | verify bounds against exact values (MIPcc23) | The paper gives invalid answers twice the worst rank but does not say how validity was checked [S055 p. 7] | Source to the repository or drop the clause |

### Reading notes (08 §3.3, copied)

Two existing SKILL.md passages restate reading notes (Method 2, Limitations: one sentence; Method 6 step 3: one parenthesis). Under the operator's rule they should be rephrased neutrally or dropped. The update should not add further notes of this kind.

---

### T3.6 long form

**One line**: build test sets and competitions by explicit rules, write down the arbitrary choices, and correct them in public.

**Evidence**:
- Stated: his call of 11 Nov 2016, "New challenges are needed!" [Call16]; co-authored: "It seems quite natural to formulate the selection task as an optimization problem"; "The concrete choice of the square root was empirically motivated" [M17; S002 p. 36].
- Practice: MIPLIB 2017 (first of 16 authors; committee of 21): purpose and non-purpose, licence, checker, selection models, a sensitivity table, feature validation, KS tests of the hardness claim, manual decisions and a minimal exchange [M17; S002 pp. 3, 6, 22–23, 33, 36–44]; its predecessor MIPLIB 2010 (group) [S001 TR pp. 6–8, 10]; benchmark v2 and changelog [MIPLIB-CL]; MIPcc23 rules in his repository: hidden series, loopholes closed, invalid answers penalised [CC23; CC23-gh; S055 pp. 2–3, 6–7]; ML4CO with hidden test sets [S016 pp. 3–5].
- Say–do: ✅ stated + practised; full texts: 19 cards evidence (13 studies), 27 variant, 1 contradiction; three factual corrections.
- Variants/corrections:
  - ✗ Step 2's licence: instances default to CC BY-SA 4.0 [S002 p. 6]; CC BY 4.0 is the article's own [S002 p. 44].
  - ✗ Step 3: the checker computes in GMP arbitrary precision but accepts by tolerances; objective values are recomputed exactly [S002 pp. 22, 42].
  - ✗ Step 7's five exchanged instances are the changelog's count, not the paper's [S002 pp. 43–44; MIPLIB-CL]; step 8: the paper does not say how validity was checked [S055 p. 7].
  - ⚠ MIPLIB 2010 kept unstable instances as a test set of their own [S001 TR pp. 6–8]; one counter-case, numerical violations accepted as successes in a student-project paper [S069 p. 23].

**Steps**:
1. State purpose and non-purpose first (not for choosing a solver for an application) [S002 p. 3].
2. Collect broadly, with a redistribution licence (by default CC BY-SA 4.0 for MIPLIB 2017 instances [S002 p. 6]), in a public repository.
3. Check every reported solution against the original file in arbitrary-precision arithmetic with a mixed absolute/relative tolerance, and recompute objective values exactly by fixing the integers [S002 pp. 22, 42]; flag cross-solver inconsistencies; remove ambiguous instances [M17 p. 465; S002 p. 23].
4. Write admission as numbered criteria, counting exclusions per criterion: solved by at least one solver (no instance unsolved for 15 years, as in MIPLIB 2003), at least 10 s for half the solvers, coefficient-range limits, no indicator constraints, at most 10^6 nonzeros. Exclude what is ambiguous; keep what is hard.
5. Select by an optimization model over feature clusterings, tilted to hard instances; admit the empirical parts; validate the feature space against independent labels [S002 p. 37] and test the design claim per solver (one-sided KS tests, failures printed) [S002 pp. 40–41].
6. Print the manual decisions and the status of the result, with a sensitivity table for free constants [S002 pp. 3–4, 33, 43].
7. When a released instance proves wrong, admit it in the paper, naming the instances; compute a minimal exchange with the selection model and present it as a use of that model [M17 pp. 485–486; S002 pp. 43–44]; publish a new version (v2, June 2019: two flagged; five exchanged per the changelog [MIPLIB-CL]), tag it, keep a changelog.
8. For a competition: penalise invalid answers (twice the worst rank in MIPcc23 [S055 p. 7]), keep hidden series, close loopholes [CC23 §3; S055 pp. 2–3, 6].
9. In your own papers, keep instances where floating-point and exact results disagree out of gap statistics [S022 p. 17; S036 p. 21].

**Applies to stage**: experiment design; community infrastructure.

**Different from standard practice**: selection is a documented optimization with counted exclusions; the benchmark is versioned like software.

**Limitations**: about 40 CPU years, eight solvers; the campaign ran two 4-thread jobs per node, against his one-job rule [S002 p. 20]; selection depends on current solvers [M17 p. 478; S002 p. 36]; tuning on MIPLIB can overstate progress, and ML authors find it too heterogeneous.

### Changes made in SKILL.md (T3.6)

- **Evidence condensed.** Stated → the call and the square-root sentence, now located [S002 p. 36]; the selection-task quotation is in the moved-verbatim copy. Practice → [M17; S002 pp. 3, 6, 22–23, 33, 40–44], [S001 TR pp. 6–8], [MIPLIB-CL], [CC23; CC23-gh; S055 pp. 2–3, 6–7]. Say–do: 19 (13), 27 (24), 1 (1).
- **Corrections (✗)**, all from 08 §3.2: licence CC BY-SA 4.0 for instances [S002 p. 6] (CC BY 4.0 is the article's [S002 p. 44]); the checker accepts by tolerances in GMP arithmetic, objective values recomputed exactly [S002 pp. 22, 42]; the count of five exchanged instances rests on the changelog only [S002 pp. 43–44]; MIPcc23's validity check is not described in the paper [S055 p. 7], so step 8's clause "verify bounds against exact values" was dropped.
- **Steps**: step 1 + [S002 p. 3]; step 2 corrected; step 3 corrected, and one parenthesis restating a reading note removed (operator rule, 08 §3.3); step 5 + one-sided KS tests per solver [S002 pp. 40–41] (feature validation [S002 p. 37] in the long form); step 6 + sensitivity table [S002 pp. 33, 43]; step 7: "five exchanged per the changelog"; step 8 without the validity clause; step 9 + [S022 p. 17] (and, until the review fixes below, [S021 pp. 5–7]).
- **Limitations**: sourced [S002 p. 20] (two jobs per node).
- **Variant bullet**: one counter-case in a student-project paper [S069 p. 23] (08 §2, Counter-case); the 2010 committee variant [S001 TR pp. 6–8] is in the long form.

### T3.6 review fixes (2026-11-28)

- **Practice**: MIPLIB 2010 relabelled co-authored (committee): a Koch-led paper with a long byline, not student work (review).
- **Say–do** one clause with the counter-case [S069 p. 23]; **variants**: the three ✗ bullets are in the Corrections list (the self-quote *Five exchanged* gone with them, review); one ⚠ remains: release reports drop numerically inconsistent runs from their version comparisons [S021 p. 5].
- **Step 3** (review: the acceptance rule was only in the card): row i holds if a_i x* − u_i ≤ ε·max{(a_i x*)^+, (a_i x*)^−, |u_i|, 1} with ε = 10^-5, integrality within an absolute 10^-4 [S002 pp. 22–23]; objective values exact [S002 p. 42].
- **Step 9** (review: S021 p. 5 drops inconsistent runs from a release comparison, which is not the practice of step 9): [S022 p. 17; S036 p. 21]; S021 p. 5 is the variant above.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> - Practice: MIPLIB 2017 (first of 16 authors; committee of 21) [M17; S002 pp. 3, 6, 22–23, 33, 40–44]; MIPLIB 2010 (group) [S001 TR pp. 6–8]; benchmark v2 and changelog [MIPLIB-CL]; MIPcc23 rules in his repository [CC23; CC23-gh; S055 pp. 2–3, 6–7].
> - Say–do: ✅ stated + practised; full texts: 19 cards evidence (13 studies), 27 variant, 1 contradiction.
> - Variants/corrections:
>   - ✗ Licence: instances CC BY-SA 4.0 by default [S002 p. 6], not CC BY 4.0.
>   - ✗ Checks in GMP arbitrary precision with tolerances, objective values exact [S002 pp. 22, 42].
>   - ✗ "Five exchanged" is the changelog's count [S002 pp. 43–44]; MIPcc23's validity check is unstated [S055 p. 7].
>   - ⚠ One counter-case in a student-project paper [S069 p. 23].
> 3. Check every reported solution against the original file in arbitrary precision with a mixed absolute/relative tolerance; recompute objective values exactly by fixing the integers [S002 pp. 22, 42]; flag cross-solver inconsistencies; remove ambiguous instances [M17 p. 465].
> 9. In your own papers, keep instances where floating-point and exact results disagree out of gap statistics [S022 p. 17; S021 pp. 5–7].


### Before T3.6 (moved verbatim)

**One line**: build test sets and competitions by explicit rules, write down the arbitrary choices, and correct them in public.

**Evidence**:
- Stated: his call of 11 Nov 2016, "New challenges are needed!" [Call16]; co-authored: "It seems quite natural to formulate the selection task as an optimization problem"; "The concrete choice of the square root was empirically motivated" [M17].
- Practice: MIPLIB 2017 (first of 16 authors; committee of 21) [M17]; benchmark v2 and changelog [MIPLIB-CL]; MIPcc23 rules in his repository [CC23; CC23-gh].
- Say–do consistency: ✅ stated and practised.

**Steps**:
1. State purpose and non-purpose first (not for choosing a solver for an application).
2. Collect broadly, with a redistribution licence (CC BY 4.0), in a public repository.
3. Check every reported solution against the original file in exact arithmetic; flag cross-solver inconsistencies; remove ambiguous instances [M17 p. 465].
4. Write admission as numbered criteria, counting exclusions per criterion: solved by at least one solver (no instance unsolved for 15 years, as in MIPLIB 2003), at least 10 s for half the solvers, coefficient-range limits, no indicator constraints, at most 10^6 nonzeros. Exclude what is ambiguous; keep what is hard.
5. Select by an optimization model over feature clusterings, tilted to hard instances; admit the empirical parts.
6. Print the manual decisions and the status of the result.
7. When a released instance proves wrong, admit it in the paper, naming the instances; compute a minimal exchange with the selection model and present it as a use of that model [M17 pp. 485–486]; publish a new version (v2, June 2019: two flagged, five exchanged), tag it, keep a changelog.
8. For a competition: verify bounds against exact values, penalise invalid answers (twice the worst rank in MIPcc23), keep hidden series, close loopholes [CC23 §3].
9. In your own papers, keep instances where floating-point and exact results disagree out of gap statistics.

**Applies to stage**: experiment design; community infrastructure.

**Different from standard practice**: selection is a documented optimization with counted exclusions; the benchmark is versioned like software.

**Limitations**: about 40 CPU years, eight solvers; the campaign ran two 4-thread jobs per node, against his one-job rule; selection depends on current solvers [M17 p. 478]; tuning on MIPLIB can overstate progress, and ML authors find it too heterogeneous.

*(One parenthesis of step 3, restating a reading note, is left out here under the operator rule, 08 §3.3.)*

<a id="method-7"></a>

## Method 7: Write the floating-point solver's contract, prove against it, and audit it

### Full-text evidence (08 §4.1, copied)

The skill has six core methods, so a seventh is admissible.

**Cards (six full cards; four studies, five works counting the thesis).** S020 (2012) and S013 (2016) on LP refinement; the thesis S032 (2015); S058 (2019) on QP refinement; S029 (2020) on LP with limited-precision oracles (IPCO version D001 at abstract level); S050 (2025) on precision boosting with refinement.

**Four checks.**
1. *Cross-project recurrence* ✅: LP refinement [S020 TR p. 7; S013 TR pp. 9–10], the thesis [S032 pp. 41–45, 83–84], QP refinement [S058 pp. 7–8, 10–11], limited-precision oracles [S029 pp. 8–17], boosting plus refinement [S050 pp. 8–9]; four studies over thirteen years, own voice in S032 and S029.
2. *Say–do* ✅: the contract and its limit are stated, "Although there is no guarantee that a floating-point solver will produce correct solutions that are accurate to within a fixed tolerance level, this is often the case in practice." [S020 TR p. 7]; the assumption is conceded to be unreasonable as stated and protected by capped scaling [S013 TR pp. 9–10]; the oracle is defined with a failure outcome and residuals that make failure detectable [S029 pp. 8–9]; a double-precision solver cannot act as such an oracle for all inputs, which motivates the combination with boosting [S050 p. 8]. Practised: oracle failures counted and attributed [S029 p. 23; S050 p. 13], the theorem's prediction checked per instance [S029 p. 24], wrong oracle claims tested and rejected with a retry [S013 TR pp. 15–16], failure triggers with escalation [S050 pp. 5–6], recovery in the QP code [S058 p. 12].
3. *Executable and different from standard practice* ✅: the steps below lead to a stated contract, a proof against it and a counted audit. Standard practice either proves under an arithmetic model whose precision is far beyond double (the 3 × 6 example in [S029 pp. 6–7]) or uses the solver without stated assumptions; the practically fastest exact LP codes had no such theory [S029 p. 7].
4. *Exclusivity* ✅: the limited-precision-oracle device is specific to this line and is positioned against both classical exact methods and precision boosting [S029 pp. 6–8]; no card from other lines uses it.

**Why not a duplicate of Method 5.** Method 5 decides where exact arithmetic runs. Method 7 decides what may be assumed about the floating-point part, proves the exact layer against that assumption, and defines when the assumption has failed. Method 5 step 5 (raise precision only on failure) takes its failure definition from Method 7 step 5.

**Draft for SKILL.md.**
- **One line**: treat the production floating-point solver as a black-box oracle with a written accuracy contract and an explicit failure outcome; prove the exact layer against the contract; make contract violations detectable, escalate on them and count them.
- **Steps**:
  1. Write the contract as constants on a restricted input class: residuals at most η, complementarity at most σ, or a failure status [S029 pp. 8–9; S058 p. 7].
  2. Close the loopholes: inputs from a fixed number set, so that scaling cannot buy accuracy in one call [S029 p. 9]; scale factors tied to the violations and capped [S013 TR pp. 9–10].
  3. Prove against the contract: linear convergence by induction over rounds, oracle-polynomial running time, output-sensitive bounds [S013 TR pp. 10, 26–27; S032 pp. 41–45; S029 pp. 10–17].
  4. Say in the next paragraph where real solvers break the contract [S020 TR p. 7; S013 TR p. 10; S050 p. 8].
  5. Make violations detectable and decide what follows them: test the oracle's infeasibility and unboundedness claims exactly and retry with other settings [S013 TR pp. 15–16]; list failure triggers (non-optimal status, residuals near one, stalling, contradicted claims) and raise the precision [S050 pp. 5–6]; retry with reliable settings, then back off the scaling factor [S058 p. 12].
  6. In the experiments, count contract violations per instance and attribute each failure to a stage; check the theorem's quantitative prediction per instance [S029 pp. 23–24; S050 p. 13].
  7. Print what stays unproved or undetected: the combined algorithm's proof is sketched and conditioned on a backward-stable LU update [S050 pp. 8–9]; QP refinement does not detect infeasibility [S058 p. 12].
- **Applies to stage**: designing and analysing a mixed-precision algorithm; judging its failures.
- **Different from standard practice**: neither an IEEE arithmetic model nor a trusted solver; the solver is an oracle whose contract is stated, proved against and audited.
- **Limitations**: shown for LP and convex QP only; the read exact-MIP papers rely on safe bounding instead [S022 p. 4] (inference: no MIP analogue of the contract in the read texts); the contract is absolute on a restricted number set [S029 p. 9]; a double-precision solver does not meet it for all inputs [S050 p. 8], which is why reliable recovery arrived only with boosting [S050 pp. 2, 5–6]. Quote: "The LP iterative refinement procedure has no reliable way of recovering if the floating-point LP subroutine aborts with a failure due to numerical issues." [S050 p. 2]
- **Consequence for How to Use**: the entry `proof design` under *Not good for* should be narrowed to polyhedral and cutting-plane theory; proofs for mixed-precision LP algorithms are now in scope through Method 7.

### T3.6 long form

**One line**: treat the production floating-point solver as a black-box oracle with a written accuracy contract and an explicit failure outcome; prove the exact layer against the contract; make contract violations detectable, escalate on them and count them.

**Evidence**:
- Stated: "Although there is no guarantee that a floating-point solver will produce correct solutions that are accurate to within a fixed tolerance level, this is often the case in practice." (co-authored, 2012) [S020 TR p. 7].
- Practice: the oracle defined with constants and a failure outcome, residuals making failure detectable, inputs from a fixed number set (own voice, with Steffy) [LPO20; S029 pp. 8–9]; the assumption conceded as unreasonable in general and protected by capped scaling [S013 TR pp. 9–10]; convergence proved against it in the thesis [S032 pp. 41–45, 83–84]; QP refinement with every step except the oracle solves in rationals [S058 pp. 6–8, 12]; boosting on named failures, since a double-precision solver cannot meet the contract for all inputs [S050 pp. 5–6, 8].
- Say–do: ✅ stated + practised, 2012–2025: six full cards, four studies (five works with the thesis), own voice in the thesis and the oracle paper; promoted from the full texts [08 §4.1].
- Variants/corrections:
  - ⚠ Not a duplicate of Method 5: Method 5 decides where exact arithmetic runs, this method what may be assumed about the floating-point part and when that assumption has failed [08 §4.1].

**Steps**:
1. Write the contract as constants on a restricted input class: residuals at most η, complementarity at most σ, or a failure status [S029 pp. 8–9; S058 p. 7].
2. Close the loopholes: inputs from a fixed number set, so that scaling cannot buy accuracy in one call [S029 p. 9]; scale factors tied to the violations, capped, and rounded to powers of two (PD3) [S013 TR pp. 8, 10–11; S029 p. 10].
3. Prove against the contract: linear convergence by induction over rounds, oracle-polynomial running time, output-sensitive bounds (PD1, PD4) [S013 TR pp. 10, 26–27; S032 pp. 41–45; S029 pp. 10–17].
4. Say in the next paragraph where real solvers break the contract (WM4) [S020 TR p. 7; S013 TR p. 10; S050 p. 8].
5. Make violations detectable and decide what follows them (DM4): test the oracle's infeasibility and unboundedness claims exactly and retry with other settings [S013 TR pp. 15–16]; list failure triggers (non-optimal status, residuals near one, stalling, contradicted claims) and raise the precision [S050 pp. 5–6]; retry with reliable settings, then back off the scaling factor [S058 p. 12].
6. In the experiments, count contract violations per instance and attribute each failure to a stage; check the theorem's quantitative prediction per instance [S029 pp. 23–24; S050 p. 13].
7. Print what stays unproved or undetected: the combined algorithm's proof is sketched and conditioned on a backward-stable LU update [S050 pp. 8–9]; QP refinement does not detect infeasibility [S058 p. 12].

**Applies to stage**: designing and analysing a mixed-precision algorithm; judging its failures.

**Different from standard practice**: neither an arithmetic model with precision far beyond double (for a 3 × 6 LP the classical tolerance is about 10^-169,059 [S029 pp. 6–7]) nor a trusted solver without stated assumptions, which is how the practically fastest exact LP codes ran [S029 p. 7]; here the solver is an oracle whose contract is stated, proved against and audited.

**Limitations**: shown for LP and convex QP only; the read exact-MIP papers rely on safe bounding instead [S022 p. 4] (inference: no MIP analogue of the contract in the read texts); the contract is absolute on a restricted number set [S029 p. 9]; a double-precision solver does not meet it for all inputs [S050 p. 8], which is why reliable recovery arrived only with boosting: "The LP iterative refinement procedure has no reliable way of recovering if the floating-point LP subroutine aborts with a failure due to numerical issues." [S050 p. 2]

### Changes made in SKILL.md (T3.6)

- **New core method**, promoted by 08 §4.1 (six full cards: S020, S013, S032, S058, S029, S050; four studies, five works with the thesis; all four checks passed; distinct from Method 5). Written in the house format from 08's draft: One line, Evidence (Stated [S020 TR p. 7]; Practice [S029 pp. 8–9; S013 TR pp. 9–10; S032 pp. 41–45; S050 pp. 5–6, 8]; Say–do; one variant bullet on the boundary with Method 5), seven Steps, Applies to stage, Different from standard practice, Limitations.
- Condensed against 08's draft: step 2 keeps capping and power-of-two rounding (PD3) [S013 TR pp. 9–10] (the tie to the violations and [S029 p. 10] are in the long form); step 3 cites [S032 pp. 41–45; S029 pp. 10–17] (08 also [S013 TR pp. 10, 26–27]); step 4 cites [S050 p. 8] (08 also [S020 TR p. 7; S013 TR p. 10]); step 5 keeps the exact test of the oracle's claims [S013 TR pp. 15–16] and the triggers [S050 pp. 5–6] (the QP back-off [S058 p. 12] is in the long form); step 6 cites [S029 pp. 23–24] (08 also [S050 p. 13]); step 7 keeps the conditioned proof [S050 pp. 8–9] (QP refinement's missing infeasibility detection [S058 p. 12] in the long form).
- **Consequences elsewhere**: How to Use (proofs for mixed-precision LP algorithms in scope), a routing row, the Step 2 *Contract* bullet, Workflow A step 2, a Taste quick-check question, the Roundtable Card's lens, the iterative-refinement anatomy's methods, and the new anatomy of the oracle paper.

### T3.6 review fixes (2026-11-28)

- **Voice** (review: the catalog called S020 and S013 own voice while SKILL.md called the S020 quote co-authored, and *own voice, with Steffy* read an alphabetical two-author byline as a role): one label, *his line*, co-authored with Steffy (and Wolter) [S020 TR p. 7; S029 pp. 8–9]; own voice only for the thesis.
- **Steps** (review: the constants that carry the steps were only in the cards): step 1 defines the input class F(p) = {n/2^p : n ∈ Z, |n| ≤ 2^(2p)}, doubles in F(1074) [S029 p. 8]; step 2 cites the cap and the power-of-two rounding where they are printed [S013 TR pp. 8, 10–11; S029 p. 10] (review: [S013 TR pp. 9–10] missed p. 11); step 3 gives the rate, violations at most ε^k with ε = max{η, 1/α}, α > 2 [S029 p. 9]; step 5 lists the triggers, stalling defined as a violation reduction by less than 2^4 over two consecutive rounds (the card's reading of an extracted "24") [S050 pp. 5–6].
- **Applies to stage**: + a closed floating-point solver can be the oracle (inferred). Workflow B's checkpoint now carries the Method 7 condition, and the routing row points here first.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> - Stated: "Although there is no guarantee that a floating-point solver will produce correct solutions that are accurate to within a fixed tolerance level, this is often the case in practice." (co-authored, 2012) [S020 TR p. 7].
> - Practice: the oracle with constants and a failure outcome, failure detectable from residuals (own voice, with Steffy) [LPO20; S029 pp. 8–9]; the assumption conceded and protected by capped scaling [S013 TR pp. 9–10]; convergence proved in the thesis [S032 pp. 41–45]; boosting on named failures [S050 pp. 5–6, 8].
> - Say–do: ✅ stated + practised, 2012–2025: six full cards, four studies, own voice in the thesis and the oracle paper [08 §4.1].
> 1. Write the contract as constants on a restricted input class: residuals at most η, complementarity at most σ, or a failure status [S029 pp. 8–9; S058 p. 7].
> 2. Close the loopholes: inputs from a fixed number set, so scaling cannot buy accuracy in one call [S029 p. 9]; scale factors capped and rounded to powers of two (PD3) [S013 TR pp. 9–10].
> 3. Prove against the contract: linear convergence over rounds, oracle-polynomial running time, output-sensitive bounds (PD1, PD4) [S032 pp. 41–45; S029 pp. 10–17].
> 5. Make violations detectable and decide what follows (DM4): test the oracle's infeasibility and unboundedness claims exactly and retry [S013 TR pp. 15–16]; on named triggers (non-optimal status, residuals near one, stalling) raise the precision [S050 pp. 5–6].
> **Applies to stage**: designing and analysing a mixed-precision algorithm; judging its failures.


### Before T3.6

New in T3.6: no earlier SKILL.md text. The quotation in the long form's Limitations, "The LP iterative refinement procedure has no reliable way of recovering if the floating-point LP subroutine aborts with a failure due to numerical issues." [S050 p. 2], is a card quote; SKILL.md now cites the page without it.

<a id="workflows"></a>

## Stage Workflows

### Changes made in SKILL.md (T3.6)

- **A**: step 2 + the floating-point contract before the code (Method 7); step 4 + cards for the software nobody had [S019 pp. 4–5; S065 p. 2] and instance series [S055 p. 2] (PaPILO [S026 p. 1] in the long form); step 5 now points to Method 3 without a step number.
- **B**: step 1 + why the effect could go either way (WM2) [S022 p. 13]; step 2 + one factor per table (EP2) [S022 pp. 8–18]; step 3 + affected subset fixed before the runs (EP4) [H001 p. 5] (the two-set design EP8 and [S021 p. 5] are in the long form); step 5 + deterministic work limits (EP15) [S012 p. 6]. Step 4 and step 6 kept their old wording (the long form adds [S003 pp. 6–8] and [S002 p. 38]).
- **C**: step 3 + MIP-DD does all three [S065 pp. 4, 6, 8–9]; step 6 + the tolerance in the model's own units (H11) [S037 pp. 6–7].
- **D**: step 2 + the thesis test located [S032 pp. 23–24] (tests in later component papers [S011 pp. 16, 21; S006 p. 20], EP7, in the long form); step 3 + the negative control for variability (EP5) [S022 p. 15] (per-instance tables EP13 [S011 pp. 26–72] in the long form).
- **E**: step 1 + [S019 p. 9].
- **F**: unchanged; the ledger pointer follows the *Stages without evidence* line.

### T3.6 review fixes (2026-11-28)

- **A step 2** (review: an order the cards do not show): *state the floating-point contract the design relies on (Method 7)*.
- **B step 5** (review: no shift values or limit): an example protocol, 1 s and 100 nodes (MIP), 0.1 s and 10 iterations (LP), 7200 s, three seeds for MIP (group, 2025) [S050 p. 9]. **B checkpoint**: + the Method 7 condition (contract written, triggers tested, violations counted per instance and stage).
- **C step 6** now carries the folded Heuristic 11: check in the original model, the violation a tolerance allows in the model's own units (co-authored, group) [S002 pp. 22–23; S037 pp. 6–7], with a pointer to [#heuristic-11](#heuristic-11).
- **B step 3 long form**: the two-set clause no longer cites [S020 TR p. 9] (review, sealed-material caution).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 2. Attack the component that decides correctness or speed (presolve first in exact SCIP; LP accuracy first for MINLP stability) (Method 5); for a mixed-precision algorithm, write the floating-point contract before the code (Method 7).
> 5. A metric per component, with the shift of each shifted geometric mean (H7); deterministic work limits for paired runs in one solver (EP15) [S012 p. 6].
> **🔴 Checkpoint**: before any run: if the arms solve different mathematical problems on some instances, drop and name those instances (Method 2 step 8); if third-party parts differ, apply Method 2 step 5. Proceed only when both are in the protocol table.
> 6. Explain tolerance effects to users as tolerance effects, not bugs [ML], in the model's own units (H11) [S037 pp. 6–7].


<a id="workflow-a"></a>

### Workflow A

**T3.6 long form:**

**Input**: a candidate solver project and what its answer will be used for.

**Steps**:
1. Proof, exactly feasible plan, or good solution? For a good solution, do not ask for exactness (Taste 4).
2. Attack the component that decides correctness or speed (presolve first in exact SCIP; LP accuracy first for MINLP stability) (Method 5); for a mixed-precision algorithm, write the floating-point solver's contract before the code (Method 7).
3. Is it a printed gap, yours or a predecessor's? (Method 3)
4. Is the missing piece software nobody has (checker [S019 pp. 4–5], presolve library [S026 p. 1], delta debugger [S065 p. 2]) or a setting benchmarks omit (instance series [S055 p. 2], MIPcc23)?
5. Does a rival community have the mechanism? Plan the import (Method 3 step 4).
6. If it rests on a belief about solver behaviour, measure it first (Method 1).
7. Give a why-now: which tool just became available.

**🔴 Checkpoint**: if floating point with an a posteriori check already meets the need, stop and recommend exactly that (Taste 4; Method 4 step 4). If the result could never live in the default distribution, stop, say it falls outside his pattern (Taste 7), and mark further advice "not Gleixner-style".

**Output**: one paragraph (use, deciding component, ledger entry, why now) plus the Taste quick-check.

**Before T3.6 (moved verbatim):**

**Input**: a candidate solver project and what its answer will be used for.

**Steps**:
1. Proof, exactly feasible plan, or good solution? For a good solution, do not ask for exactness (Taste 4).
2. Attack the component that decides correctness or speed (presolve first in exact SCIP; LP accuracy first for MINLP stability) (Method 5).
3. Is it a printed gap, yours or a predecessor's? (Method 3)
4. Is the missing piece software nobody has (checker, presolve library, delta debugger) or a setting benchmarks omit (instance series, MIPcc23)?
5. Does a rival community have the mechanism? Plan the import (Method 3).
6. If it rests on a belief about solver behaviour, measure it first (Method 1).
7. Give a why-now: which tool just became available.

**🔴 Checkpoint**: if floating point with an a posteriori check already meets the need, stop and recommend exactly that (Taste 4; Method 4 step 4). If the result could never live in the default distribution, stop, say it falls outside his pattern (Taste 7), and mark further advice "not Gleixner-style".

**Output**: one paragraph (use, deciding component, ledger entry, why now) plus the Taste quick-check.

<a id="workflow-b"></a>

### Workflow B

**T3.6 long form:**

**Input**: an implemented method; candidate baselines; machines.

**Steps**:
1. Write the numbered questions (H6) and, for each, the expected effect with the reasons it could go either way (WM1, WM2) [S022 pp. 6, 8, 13].
2. Build the like-for-like baseline and keep default (Method 2); change one factor per table, each on top of the last (EP2) [S022 pp. 8–18].
3. Sets: the predecessor's plus a harder public one; a set the solver finds easy and one compiled to be numerically difficult (EP8) [S019 p. 9; S072 p. 8]; fix the affected subset by a mechanical criterion before the runs, with a control group (EP4) [H001 p. 5; S021 p. 5]; for a set you build, apply Method 6 steps 3–4; name each exclusion (H8).
4. Seeds or permutations where variability matters, each instance-seed pair one observation (H8; EP3) [S003 pp. 6–8].
5. A metric per component, with the shift of each shifted geometric mean (H7); in paired runs inside one solver, deterministic work limits instead of wall-clock time (EP15) [S012 pp. 4, 6].
6. Exclusive machines, or do not call it a benchmark [M17 p. 480; S002 p. 38].
7. Test the evaluation scripts against reference values (H5).

**🔴 Checkpoint**: before any run: if the arms solve different mathematical problems on some instances, drop and name those instances (Method 2 step 8); if third-party parts differ, apply Method 2 step 5. Proceed only when both are in the protocol table.

**Output**: a protocol table: questions, arms, sets, exclusions, seeds, metrics, hardware.

**Before T3.6 (moved verbatim):**

**Input**: an implemented method; candidate baselines; machines.

**Steps**:
1. Write the numbered questions (H6).
2. Build the like-for-like baseline and keep default (Method 2).
3. Sets: the predecessor's plus a harder public one; for a set you build, apply Method 6 steps 3–4; name each exclusion (H8).
4. Seeds or permutations where variability matters (H8).
5. A metric per component, with the shift of each shifted geometric mean (H7).
6. Exclusive machines, or do not call it a benchmark [M17 p. 480].
7. Test the evaluation scripts against reference values (H5).

**🔴 Checkpoint**: before any run: if the arms solve different mathematical problems on some instances, drop and name those instances (Method 2 step 8); if third-party parts differ, apply Method 2 step 5. Proceed only when both are in the protocol table.

**Output**: a protocol table: questions, arms, sets, exclusions, seeds, metrics, hardware.

<a id="workflow-c"></a>

### Workflow C

**T3.6 long form:**

**Input**: a failing or suspicious run, or a change proposed as a default.

**Steps**:
1. Known feasible solution as oracle (H4a).
2. Swap a component to localise (H4b).
3. Shrink the instance and add it to the regression set (H4c); MIP-DD does all three in one tool [S065 pp. 4, 6, 8–9].
4. For a default-on change: a performance run on the internal solvable set, tests per LP solver, an API version bump (H3).
5. If it does not hold up, revert and say so in the commit message (H3).
6. Explain tolerance effects to users as tolerance effects, not bugs [ML]: write the solver's feasibility test next to the row and compute the violation it allows in the model's own units (H11) [S037 pp. 6–7].

**🔴 Checkpoint**: no default-on merge without the performance run; no result from an evaluation script without a consistency check.

**Output**: a minimal reproducing instance, the cause, the regression entry.

**Before T3.6 (moved verbatim):**

**Input**: a failing or suspicious run, or a change proposed as a default.

**Steps**:
1. Known feasible solution as oracle (H4a).
2. Swap a component to localise (H4b).
3. Shrink the instance and add it to the regression set (H4c).
4. For a default-on change: a performance run on the internal solvable set, tests per LP solver, an API version bump (H3).
5. If it does not hold up, revert and say so in the commit message (H3).
6. Explain tolerance effects to users as tolerance effects, not bugs [ML].

**🔴 Checkpoint**: no default-on merge without the performance run; no result from an evaluation script without a consistency check.

**Output**: a minimal reproducing instance, the cause, the regression entry.

<a id="workflow-d"></a>

### Workflow D

**T3.6 long form:**

**Input**: result tables and logs.

**Steps**:
1. Check a surprising number, then explain it ("This is not an error in the table." [Sim21]).
2. Is the mean carried by a few instances? Count newly solved and lost; test consistency per bracket (thesis: one-sided Wilcoxon signed-rank test on log ratios of shifted values, 5% level [Th pp. 11–12; S032 pp. 23–24]; H8); his component papers ran such tests up to 2018 [S011 pp. 16, 21; S006 p. 20] (EP7).
3. Read losses as the next idea (Method 3) and certificates for wrong reasoning (Method 4); where a component cannot help, a gain is variability: rerun those instances with more seeds and restate the gain (EP5) [S022 p. 15].
4. Each headline with set, limit and denominator; the remaining gap as a number (H8); per-instance tables from which every aggregate can be recounted (EP13) [S011 pp. 26–72].
5. Before the final version, replace adjectives by counts (H2).

**🔴 Checkpoint**, in order (inferred from his practices): (1) wrong answers explained (Method 4 step 4; H4); (2) the gain survives seeds or permutations (H8); (3) not carried by a few instances (step 2); (4) only then default-on (H3) and the claim. Throughout: no "exact" or "verified" for a stage the certificate does not cover; no factor without its baseline.

**Output**: claims with subset and baseline; printed limits for the ledger. This rests on practice only; he gave no writing advice.

**Before T3.6 (moved verbatim):**

**Input**: result tables and logs.

**Steps**:
1. Check a surprising number, then explain it ("This is not an error in the table." [Sim21]).
2. Is the mean carried by a few instances? Count newly solved and lost; test consistency per bracket (thesis: one-sided Wilcoxon signed-rank test on log ratios of shifted values, 5% level [Th pp. 11–12]; H8).
3. Read losses as the next idea (Method 3) and certificates for wrong reasoning (Method 4).
4. Each headline with set, limit and denominator; the remaining gap as a number (H8).
5. Before the final version, replace adjectives by counts (H2).

**🔴 Checkpoint**, in order (inferred from his practices): (1) wrong answers explained (Method 4 step 4; H4); (2) the gain survives seeds or permutations (H8); (3) not carried by a few instances (step 2); (4) only then default-on (H3) and the claim. Throughout: no "exact" or "verified" for a stage the certificate does not cover; no factor without its baseline.

**Output**: claims with subset and baseline; printed limits for the ledger. This rests on practice only; he gave no writing advice.

<a id="workflow-e"></a>

### Workflow E

**T3.6 long form:**

**Input**: a released tool, certificate format or benchmark.

**Steps**:
1. Archive code version, logs and per-instance results with the paper [S019 p. 9].
2. Answer issues and pull requests fast; offer your revision for review (H1).
3. Correct released artefacts in public with the method that built them (Method 6, step 7).
4. Integrate into the default distribution yourself, with a packaging test (Method 3).

**🔴 Checkpoint**: if the public supplement cannot reproduce the final table, fix it (2017–2022 the VIPR repository could not reproduce the IPCO table [VIPR-gh]).

**Output**: changelog entries, release note, updated supplement.

**Before T3.6 (moved verbatim):**

**Input**: a released tool, certificate format or benchmark.

**Steps**:
1. Archive code version, logs and per-instance results with the paper.
2. Answer issues and pull requests fast; offer your revision for review (H1).
3. Correct released artefacts in public with the method that built them (Method 6, step 7).
4. Integrate into the default distribution yourself, with a packaging test (Method 3).

**🔴 Checkpoint**: if the public supplement cannot reproduce the final table, fix it (2017–2022 the VIPR repository could not reproduce the IPCO table [VIPR-gh]).

**Output**: changelog entries, release note, updated supplement.

<a id="workflow-f"></a>

### Workflow F

**T3.6 long form:**

**Input**: a stalled project (slower than the incumbent, unpublishable, no next step). Inferred from Methods 1–3 and 5; he stated no advice on stalls.

**Steps**:
1. State the stall as a number (factor, instances lost). No number yet: get one (Method 1) and stop.
2. Measure against the reduced baseline and default (Method 2 steps 1–4). Small like-for-like factor: missing components, step 3. Large: profile; is a candidate producer exact (Warning sign 7)?
3. One ledger entry with a count per missing component (Method 3 step 1); take the one behind most lost instances; import it where a rival has it (Method 3 step 4).
4. Read lost instances as the next idea; a counted negative result can be the paper (Method 1 step 7; Taste 5).

**🔴 Checkpoint**: if the like-for-like factor stays large and no component explains it, say so and stop: his record has no method for a real roadblock (several application lines ended after one to three papers [06 §6]). Mark further advice "not Gleixner-style".

**Output**: the stall as a number; missing components or roadblock; the next component or measurement; the limit to print.

**Stages without evidence** (last routing row): literature work has one remark, "I'm not aware of a handbook of computational MIP" [Sim21 00:52].

(full evidence per workflow: [ledger](#workflows))

**Before T3.6 (moved verbatim):**

**Input**: a stalled project (slower than the incumbent, unpublishable, no next step). Inferred from Methods 1–3 and 5; he stated no advice on stalls.

**Steps**:
1. State the stall as a number (factor, instances lost). No number yet: get one (Method 1) and stop.
2. Measure against the reduced baseline and default (Method 2 steps 1–4). Small like-for-like factor: missing components, step 3. Large: profile; is a candidate producer exact (Warning sign 7)?
3. One ledger entry with a count per missing component (Method 3 step 1); take the one behind most lost instances; import it where a rival has it (Method 3 step 4).
4. Read lost instances as the next idea; a counted negative result can be the paper (Method 1 step 7; Taste 5).

**🔴 Checkpoint**: if the like-for-like factor stays large and no component explains it, say so and stop: his record has no method for a real roadblock (several application lines ended after one to three papers [06 §6]). Mark further advice "not Gleixner-style".

**Output**: the stall as a number; missing components or roadblock; the next component or measurement; the limit to print.

**Stages without evidence** (last routing row): literature work has one remark, "I'm not aware of a handbook of computational MIP" [Sim21 00:52].

<a id="heuristic-1"></a>

## Heuristic 1: Your checker is code under test

### Full-text evidence (08 §5, copied)

- **H1** (checker as code under test): the 2017 paper offers simplicity instead of tests of the checker [S019 pp. 4, 8]: "the certificate verification program we have provided is merely a reference and others should be able to write their own verifiers without much difficulty." [S019 p. 8]; later a formally verified checker is named [S021 p. 11] and the delta debugger plans to treat an invalid certificate as a failure [S065 p. 13].

### T3.6 long form

1. **Your checker is code under test.** If an outsider finds a hole: thank them, post a revision within a day, ask them to review it, point users to a formally verified checker. Case: VIPR PR #24 (27 Oct 2026) answered in about 17 hours; his PR #25 asks the contributor to double-check; both open on 2026-11-14 [VIPR-gh]. In print the 2017 paper offers simplicity instead [S019 p. 8]; the 2025 release names a verified checker [S021 p. 11].

### Changes made in SKILL.md (T3.6)

- Added: the 2017 paper had offered simplicity in place of tests of the checker [S019 p. 8] (08 §5, H1). The formally verified checker named in the release [S021 p. 11] and the planned invalid-certificate failure type in MIP-DD [S065 p. 13] are in the long form and the 08 text above.

### Before T3.6 (moved verbatim)

1. **Your checker is code under test.** If an outsider finds a hole: thank them, post a revision within a day, ask them to review it, point users to a formally verified checker. Case: VIPR PR #24 (27 Oct 2026) answered in about 17 hours; his PR #25 asks the contributor to double-check; both open on 2026-11-14 [VIPR-gh].

<a id="heuristic-2"></a>

## Heuristic 2: Counts replace adjectives between versions

### Full-text evidence (08 §5, copied)

- **H2** (counts replace adjectives): between the IPCO and journal versions the closing sentence on the remaining gap keeps its adjective, and the journal adds the like-for-like factors behind it [D002 p. 14; S022 pp. 17–18]; the debugger's v5 count [S065 p. 8]; adjectives also remain beside counts [S022 p. 13].

### T3.6 long form

2. **Counts replace adjectives between versions.** MIP-DD: a majority claim (v1) became "24 among all the 51" (v5) [MIPDD-ax; S065 p. 8]; circle packing "exact dual bounds" → "strong dual bounds" [CP17]; Chvátal v1 a theorem title, v2 a safe framework plus a Coq check [Chv-ax]; the status update's closing sentence on the remaining gap gains its factors [D002 p. 14; S022 pp. 17–18]. No stated reason.

### Changes made in SKILL.md (T3.6)

- Added: the v5 count located [S065 p. 8]; the status update's closing sentence on the remaining gap gains its factors between the IPCO and journal versions [S022 pp. 17–18] (08 §5, H2; [D002 p. 14] in the long form). 08's remark that adjectives also remain beside counts [S022 p. 13] stays in the 08 text.

### T3.6 review fixes (2026-11-28)

- (Review: the closing sentence keeps "still large" in both versions [D002 p. 14; S022 p. 18]; the factors 8.1 and 3.9 stand in §4.7 [S022 p. 17].) The example now reads: the journal version keeps its closing adjective but adds like-for-like factors behind it [D002 p. 14; S022 pp. 17–18]. 08 §5 and its copy above were corrected the same way.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 2. **Counts replace adjectives between versions.** MIP-DD: a majority claim (v1) became "24 among all the 51" (v5) [MIPDD-ax; S065 p. 8]; circle packing "exact dual bounds" → "strong dual bounds" [CP17]; Chvátal v1 a theorem title, v2 a safe framework plus a Coq check [Chv-ax]; the status update's closing sentence gains its factors [S022 pp. 17–18]. No stated reason. ([ledger](#heuristic-2))


### Before T3.6 (moved verbatim)

2. **Counts replace adjectives between versions.** MIP-DD: a majority claim (v1) became "24 among all the 51" (v5) [MIPDD-ax]; circle packing "exact dual bounds" → "strong dual bounds" [CP17]; Chvátal v1 a theorem title, v2 a safe framework plus a Coq check [Chv-ax]. No stated reason.

<a id="heuristic-3"></a>

## Heuristic 3: A default has to earn its place

### Full-text evidence (08 §5, copied)

- **H3** (a default earns its place): defaults rest on measurements dated to the merge, components stay off where they do not pay [S003 pp. 9–11, 21–24; D004 pp. 15, 17–18, 20; S007 pp. 8, 10, 12–14; S021 pp. 5–7, 13, 19–21; S004 pp. 34–35, 61, 73]. *Variant*: a new signal enters as a tie-breaker or wrapper whose zero setting is the old default (weight 0.1 against 1 [S032 pp. 178, 180–181]; weight 10^-5 [S007 p. 16]; a filter around any branching rule [S054 p. 8]; the new presolver runs first and the old one continues [S079 pp. 5–7]; a learner starts from the default order [S040 p. 4]; a drop-in behind the existing linear-algebra interface [S066 pp. 4, 12]). *Tension*: presolvers neutral on MIPLIB kept for other classes and against overtuning [S031 p. 32].

### T3.6 long form

3. **A default has to earn its place.** Default-on needs a performance run on the internal solvable set and tests against several LP solvers; else ship it off; log reverts. Case: the merge-request template he created (commit 8201ee1d, 2018) and rewrote as tickable assertions with an "or" escape (2020) [MRT]; `prop_genvbounds` switched on then off by default (2012); own commits reverted (2014) [SCIP-gh; SoPlex-gh]. Release reports date defaults to merge-time measurements [S003 pp. 9–11; S021 pp. 5–7]; a new signal enters as a tie-breaker whose zero weight is the old default [S032 pp. 178, 180–181].

### Changes made in SKILL.md (T3.6)

- Added: defaults dated to merge-time runs in the release reports [S003 pp. 9–11; S021 pp. 5–7] (08 §5, H3). The tie-breaker variant (a new signal whose zero weight is the old default [S032 pp. 178, 180–181]) is in the long form and the 08 text; the tension with presolvers kept against overtuning [S031 p. 32] stays in the 08 text.

### T3.6 review fixes (2026-11-28)

- (Review: *defaults dated to merge-time runs* could not be parsed.) Now: release reports give the gain each new default showed when it was added ("At the time of addition" [S003 p. 10]; [S003 p. 18]) and leave off what did not pay [S021 pp. 13, 19–20].

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 3. **A default has to earn its place.** Default-on needs a performance run on the internal solvable set and tests against several LP solvers; else ship it off; log reverts. Case: the merge-request template he created (commit 8201ee1d, 2018) and rewrote as tickable assertions with an "or" escape (2020) [MRT]; `prop_genvbounds` switched on then off by default (2012); own commits reverted (2014) [SCIP-gh; SoPlex-gh]; defaults dated to merge-time runs [S003 pp. 9–11; S021 pp. 5–7]. ([ledger](#heuristic-3))


### Before T3.6 (moved verbatim)

3. **A default has to earn its place.** Default-on needs a performance run on the internal solvable set and tests against several LP solvers; else ship it off; log reverts. Case: the merge-request template he created (commit 8201ee1d, 2018) and rewrote as tickable assertions with an "or" escape (2020) [MRT]; `prop_genvbounds` switched on then off by default (2012); own commits reverted (2014) [SCIP-gh; SoPlex-gh].

<a id="heuristic-4"></a>

## Heuristic 4: Debug with three tools

### Full-text evidence (08 §5, copied)

- **H4** (debug with three tools): all three in one tool, reference solution as oracle, settings reduced toward a target to name the faulty component, shrink while the bug persists and add to the regression set [S065 pp. 4, 6, 8–9]; debug solutions in 2012 [S023 p. 18; S071 p. 17] and traced through presolve and postsolve [S004 p. 64]; a single-machine twin for a distributed solver [S007 p. 21]; reduced instances in the regression pipeline [S021 p. 38].

**08's merge proposal (copied):** (no content lost): H5 becomes tool (d) of H4 (the measuring scripts are debugged like the solver); H6 and H7 become one item (questions first, each with the metric that fits the component). With HA and HB added the count stays at ten.

### T3.6 long form

4. **Debug with three tools**: (a) a known feasible solution as oracle, (b) swap a component, (c) shrink the instance while it still fails and add it to the regression set; (d) debug the measuring scripts like the solver (H5). Case: mailing-list answers 2011, 2018 [ML]; commit "check debug solution in prop_genvbounds" (2013); MIP-DD (group) [MIPDD; S065 pp. 4, 6, 8–9].

### Changes made in SKILL.md (T3.6)

- Added: MIP-DD has all three tools in one [S065 pp. 4, 6, 8–9] (08 §5, H4), and "the measuring scripts are debugged too (H5)", which carries 08's proposed merge of H5 into H4 as a cross-reference instead of a renumbering (see [Rejected and held-back updates](#rejected)).

### Before T3.6 (moved verbatim)

4. **Debug with three tools**: (a) a known feasible solution as oracle, (b) swap a component, (c) shrink the instance while it still fails and add it to the regression set. Case: mailing-list answers 2011, 2018 [ML]; commit "check debug solution in prop_genvbounds" (2013); MIP-DD (group) [MIPDD].

<a id="heuristic-5"></a>

## Heuristic 5: Debug the measuring scripts

### Full-text evidence (08 §5, copied)

- **H5** (debug the measuring scripts): the test engine's mismatch status against reference values in 2011 [S001 TR p. 11]; result files and a comparison script ship with the solver [S023 p. 18]; a final feasibility check that lists every violation [S010 p. 19]; violation queries and statistics plugins [S003 pp. 24–27].

**08's merge proposal (copied):** (no content lost): H5 becomes tool (d) of H4 (the measuring scripts are debugged like the solver); H6 and H7 become one item (questions first, each with the metric that fits the component). With HA and HB added the count stays at ten.

### T3.6 long form

5. **Debug the measuring scripts**: make them flag results that contradict reference values. Case: SoPlex `check/evaluation.py` fix (2014; the consistency check could never fire) and `check/compare.py` shifted-mean fix; SCIP `check.awk` maximization parsing (2013) [SoPlex-gh; SCIP-gh]; the MIPLIB 2010 test engine's mismatch status [S001 TR p. 11]; a final check that lists every violation [S010 p. 19]. Practice only.

### Changes made in SKILL.md (T3.6)

- Added: MIPLIB 2010's test engine [S001 TR p. 11] (08 §5, H5). The other cases (result files and a comparison script shipped with the solver [S023 p. 18], a final check that lists every violation [S010 p. 19], violation queries and statistics plugins [S003 pp. 24–27]) stay in the 08 text above. Kept as its own item (08's merge proposal: see Heuristic 4 and the rejected section).

### Before T3.6 (moved verbatim)

5. **Debug the measuring scripts**: make them flag results that contradict reference values. Case: SoPlex `check/evaluation.py` fix (2014; the consistency check could never fire) and `check/compare.py` shifted-mean fix; SCIP `check.awk` maximization parsing (2013) [SoPlex-gh; SCIP-gh]. Practice only.

<a id="heuristic-6"></a>

## Heuristic 6: Questions first

### Full-text evidence (08 §5, copied)

- **H6** (questions first): numbered or bulleted questions in [S029 p. 22; S036 p. 20; D002 p. 8; S022 p. 8; S043 pp. 19–20; S092 p. 8; S050 p. 9; S085 p. 17; S079 p. 6; D003 p. 10]; unnumbered [S011 p. 14; S072 p. 7]. *Extension*: write down before measuring why the effect could go either way [S022 pp. 6, 13; S050 p. 9].

**08's merge proposal (copied):** (no content lost): H5 becomes tool (d) of H4 (the measuring scripts are debugged like the solver); H6 and H7 become one item (questions first, each with the metric that fits the component). With HA and HB added the count stays at ten.

### T3.6 long form

6. **Questions first**: computational sections open with numbered or bulleted questions: three in [LPO20] and [GMI24] and in the IPCO status update, four in the journal version [S029 p. 22; S036 p. 20; S022 p. 8]; say which numbers matter before the tables, why the effect could go either way [S022 pp. 6, 13], and which metric answers each question (H7).

### Changes made in SKILL.md (T3.6)

- **Corrected count** (08 §3.2): "three each in [LPO20], [SU23], [GMI24]" → three in [LPO20], [GMI24] and the IPCO status update, four in the journal version [S022 p. 8] (the IPCO version's three [D002 p. 8] are in the long form). The full list of cards with numbered or bulleted questions and the *expectation written before measuring* extension are in the 08 text above; Workflow B step 1 now carries the extension (WM2).

### T3.6 review fixes (2026-11-28)

- The IPCO status update now carries its keys [ZR21-04; D002 p. 8] (review).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 6. **Questions first**: computational sections open with numbered or bulleted questions (three in [LPO20], [GMI24] and the IPCO status update, four in the journal [S022 p. 8]); say which numbers matter before the tables. ([ledger](#heuristic-6))


### Before T3.6 (moved verbatim)

6. **Questions first**: computational sections open with numbered questions (three each in [LPO20], [SU23], [GMI24]); say which numbers matter before the tables.

<a id="heuristic-7"></a>

## Heuristic 7: The metric fits the component

### Full-text evidence (08 §5, copied)

- **H7** (the metric fits the component): a written source for fail fast in 2012/2013, measured by the stage at which failures are detected [S018 pp. 4, 15–17]; dive length measured for fail fast and success-gated execution [S034 pp. 12–15, 20–22; S079 pp. 5–7]; primal integral and time to first solution [S003 pp. 22–23; S022 pp. 2, 15; S045 pp. 18–19; S069 pp. 3, 7, 17; S073 pp. 11–13; S076 pp. 9–10]; limit-independent success-versus-effort profiles for a component that runs under working limits [S011 pp. 17–18].

**08's merge proposal (copied):** (no content lost): H5 becomes tool (d) of H4 (the measuring scripts are debugged like the solver); H6 and H7 become one item (questions first, each with the metric that fits the component). With HA and HB added the count stays at ten.

### T3.6 long form

7. **The metric fits the component.** Heuristics by time to first solution and primal integral; inside a solver they must "fail fast" [Sim21 00:45], a rule written down in 2012/2013 and measured by the stage at which failures are detected [S018 pp. 4, 15–17]; "finding good solutions earlier may be more relevant than proving optimality eventually" [SU23 p. 794]. Say when a component gave nothing ("the first disappointing thing" [Sim21]).

### Changes made in SKILL.md (T3.6)

- Added: fail fast in print, 2012/2013 [S018 p. 4] (08 §5, H7: measured by the stage at which failures are detected [S018 pp. 4, 15–17]). The further metric cases (dive length, success-gated execution, limit-independent profiles) stay in the 08 text above.

### T3.6 review fixes (2026-11-28)

- (Review: the card page sat inside a quotation it does not contain; S018 p. 4 says "fast fail".) Now: must "fail fast" [Sim21 00:45], in print a "fast fail" strategy [S018 p. 4].

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 7. **The metric fits the component.** Heuristics by time to first solution and primal integral; inside a solver they must "fail fast" [Sim21 00:45; S018 p. 4]; "finding good solutions earlier may be more relevant than proving optimality eventually" [SU23 p. 794]. Say when a component gave nothing ("the first disappointing thing" [Sim21]). ([ledger](#heuristic-7))


### Before T3.6 (moved verbatim)

7. **The metric fits the component.** Heuristics by time to first solution and primal integral; inside a solver they must "fail fast" [Sim21 00:45]; "finding good solutions earlier may be more relevant than proving optimality eventually" [SU23 p. 794]. Say when a component gave nothing ("the first disappointing thing" [Sim21]).

<a id="heuristic-8"></a>

## Heuristic 8: Subset discipline

### Full-text evidence (08 §5, copied)

- **H8** (subset discipline): five seeds with instance-seed pairs as observations already in 2017 [S003 pp. 6–8]; four [S034 pp. 11–12] and ten [S061 pp. 5–6] seeds; brackets after Achterberg and Wunderling with a sample-size caveat and ten permutations [S011 pp. 16, 19, 21]. *Extensions*: (i) fix the affected subset by a mechanical criterion before the runs and keep a control group [H001 p. 5; S028 p. 7; S006 pp. 19–20; S021 p. 5; S044 pp. 16–17]; (ii) count applicability and cost before the effect [S039 pp. 7–8; S018 pp. 13–16; S054 pp. 10–11; S043 pp. 19–25; S073 pp. 10–11]; (iii) negative control: where a component cannot help, a gain is variability, so rerun those instances with more seeds and restate the gain [S022 p. 15]: "We have to attribute a portion of the speedup on numdiff to performance variability since some of the instances where the variant with enabled heuristics is much faster are two infeasible instances." [S022 p. 15]; (iv) in paired runs inside one solver, deterministic work limits instead of wall-clock time [S012 pp. 4, 6, 18; S024 p. 11; S080 p. 20], while cross-solver tables keep time [S001 TR p. 14].

### T3.6 long form

8. **Subset discipline.** Headlines name subset and limit; overheads only on both-solved instances; a bias argument per exclusion, excluded instances named; "All experiments to evaluate the new code are run with three different random seeds, where we treat each instance-seed combination as a single observation" [ZR21-04], five seeds already in 2017 [S003 pp. 6–8]; "fastest" means within 5% [Th pp. 3, 13–14; GMI24 §4.4]. Brackets all solved, ≥1 s, ≥10 s, ≥100 s, after Achterberg and Wunderling (2013) [Th p. 145]; a failed test on a small bracket (20, 11 instances) is put down to sample size; single-instance claims rest on ten constraint permutations [Th p. 147]. Negative control: where a component cannot help, a gain is variability [S022 p. 15].

### Changes made in SKILL.md (T3.6)

- Added: five seeds with instance-seed pairs already in 2017 [S003 pp. 6–8] (08 §5, H8). The four extensions of 08 (affected subsets fixed before the runs, applicability before effect, the negative control, deterministic work limits) went into Workflow B steps 3 and 5 and Workflow D step 3 (EP4, EP15, EP5) instead of lengthening this item; the long form carries the negative control [S022 p. 15].

### Before T3.6 (moved verbatim)

8. **Subset discipline.** Headlines name subset and limit; overheads only on both-solved instances; a bias argument per exclusion, excluded instances named; "All experiments to evaluate the new code are run with three different random seeds, where we treat each instance-seed combination as a single observation" [ZR21-04]; "fastest" means within 5% [Th pp. 3, 13–14; GMI24 §4.4]. Brackets all solved, ≥1 s, ≥10 s, ≥100 s, after Achterberg and Wunderling (2013) [Th p. 145]; a failed test on a small bracket (20, 11 instances) is put down to sample size; single-instance claims rest on ten constraint permutations [Th p. 147].

<a id="heuristic-9"></a>

## Heuristic 9: Harvest what the solver already computed

### Full-text evidence (08 §5, copied)

- **H9** (harvest what the solver already computed): the two sources the skill marks as not read are now read, the OBBT paper in its report version [S011 pp. 7–12] and the conflict-driven heuristics [S034 pp. 7–10]; further cases [S039 pp. 4–7; S018 pp. 10–11, 13; S003 pp. 20–21; S043 pp. 15, 18; S006 p. 10]. *Variant (MINLP, group)*: the node's tighter bounds feed the relaxation [D007 p. 3; S083 pp. 2, 10–11; S044 pp. 12–13, 20; S063 pp. 12, 24].

### T3.6 long form

9. **Harvest what the solver already computed**: duals of bound-tightening LPs become cheap one-row bounds; infeasibility proofs feed heuristics and conflict analysis [LVB13; OBBT17; CDH20; S011 pp. 7–12; S034 pp. 7–10]; priority for the one-row observation is conceded to Tawarmalani and Sahinidis [S011 pp. 7, 9]. Mostly MINLP-side.

### Changes made in SKILL.md (T3.6)

- The two sources SKILL.md marked "not read" are read: the OBBT paper [S011 pp. 7–12] and the conflict-driven heuristics [S034 pp. 7–10]; "not read" removed (08 §5, H9; §3.2, Honest Boundary row). The priority concession to Tawarmalani and Sahinidis [S011 pp. 7, 9] is in the long form (08 §4.2: why H9 stays a heuristic).

### Before T3.6 (moved verbatim)

9. **Harvest what the solver already computed**: duals of bound-tightening LPs become cheap one-row bounds; infeasibility proofs feed heuristics and conflict analysis [LVB13; OBBT17; CDH20, not read]. Mostly MINLP-side.

<a id="heuristic-10"></a>

## Heuristic 10: Template the arithmetic type from the first commit

### Full-text evidence (08 §5, copied)

- **H10** (template the arithmetic type): [S026 pp. 3, 10; S022 p. 5; S021 p. 8]. *Extension*: fix the commit order from the start so that parallel output does not depend on thread count, and measure what determinism costs [S026 pp. 6–9; S005 p. 10; S004 pp. 62–63; S078 arXiv pp. 13, 15]: "Regardless of the number of threads used all runs return the same reductions and hence the same presolved problem." [S026 p. 11]

### T3.6 long form

10. **Template the arithmetic type from the first commit**, so the rational variant is a type argument: PaPILO [Sim21 01:33; PaPILO; S026 pp. 3, 10] (code by Gottwald and Hoen; one project); fix the commit order so that parallel output does not depend on the thread count, and measure what determinism costs (DM11) [S026 pp. 6–9, 11].

### Changes made in SKILL.md (T3.6)

- Added: PaPILO's templating located [S026 pp. 3, 10] and the determinism extension, a fixed commit order that keeps parallel output independent of the thread count [S026 pp. 6–9] (08 §5, H10; the quotation [S026 p. 11] is in the 08 text above; DM11 in the catalog).

### T3.6 review fixes (2026-11-28)

- + the folded Heuristic 12 (group): no reduction may break what the consumer needs, block structure for a parallel interior-point solver [S078 arXiv p. 7], duals and bases through postsolve for LP users [S004 pp. 62–63], certificate coverage (Method 4 step 1, [S038 pp. 4, 6–10]); pointer to [#heuristic-12](#heuristic-12).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 10. **Template the arithmetic type from the first commit**, so the rational variant is a type argument: PaPILO [Sim21 01:33; PaPILO; S026 pp. 3, 10] (code by Gottwald and Hoen; one project); a fixed commit order keeps parallel output independent of the thread count [S026 pp. 6–9]. ([ledger](#heuristic-10))


### Before T3.6 (moved verbatim)

10. **Template the arithmetic type from the first commit**, so the rational variant is a type argument: PaPILO [Sim21 01:33; PaPILO] (code by Gottwald and Hoen; one project).

**Already known**: build inside the open-source solver and release; shifted geometric means, seeds and one job per node are "pretty standard in MIP solving" [Sim21]. *(unchanged in SKILL.md)*

<a id="heuristic-11"></a>

## Former Heuristic 11 (HA, folded in the review fixes): Check and report in the original model, and translate tolerances into its units

### Full-text evidence (08 §5, copied)

**HA · Check and report in the original model, and translate tolerances back into its units**

- **Steps**:
  1. Keep the instance as the contributor wrote it, and run final checks on the original file, not the solver's transformed model [S001 TR pp. 6, 10; S002 pp. 22–23].
  2. Before trusting a model with tiny or wide-ranging coefficients, write the solver's feasibility test next to the row and compute what violation it allows in the model's own quantity; show how a priori scaling changes the tolerance [S037 pp. 6–7]; make a feasibility test invariant to row scaling [S045 p. 18].
  3. After a reformulation, check the original constraints and scale the reformulated constraint so that its tolerance implies the original one [S010 p. 15; S003 p. 12]; keep reformulations as annotations so that the original constraints decide [S015 pp. 7, 9]; solve with a tighter internal tolerance than the one reported in the original space [S006 p. 19].
  4. Name each step at which the solved problem departs from the intended one (decimal input, scaling, tolerances, presolve) [S001 TR pp. 9–10], and call a reduction exact only in a stated sense [S017 TR p. 12]; a method that solves a different problem gives no valid dual bound, "since precisely speaking a different problem is solved" [S017 TR p. 4].
  5. In solver comparisons, count tolerance violations next to time [S052 pp. 8, 10].
- **Checks**: recurrence ✅ (2011–2023, ten works); say–do ✅ (stated [S017 TR p. 4; S037 pp. 6–7], practised in two library checkers and three release reports); executable ✅; exclusivity not shown. **Voice**: co-authored and group.
- **Cross-references**: complements Method 4 step 4 (exact check) for the cases where only floating point runs; gives Workflow C step 6 a procedure.

### T3.6 long form

11. **Check and report in the original model, and translate tolerances into its units** (co-authored and group): run final checks on the original file, not the transformed model [S002 pp. 22–23]; for tiny or wide-ranging coefficients, compute what violation the solver's tolerance allows in the model's own quantity [S037 pp. 6–7]; a bound from a changed problem is no valid dual bound for the original, "since precisely speaking a different problem is solved" [S017 TR p. 4].

### Changes made in SKILL.md (T3.6)

- **New** (08 §5, HA: recurrence, say–do and executable checks passed; exclusivity not shown; co-authored and group voice). One line in SKILL.md with three card refs [S002 pp. 22–23; S037 pp. 6–7; S017 TR p. 4]; the five steps are in the 08 text above. Referenced from the routing table (disagreement and debugging rows), Workflow C step 6, Warning sign 8 and the anti-patterns.

### T3.6 review fixes (2026-11-28)

- **Folded** (review: twelve heuristics exceed the framework's five to ten; HA overlaps Method 4 step 4 and Method 6 step 3, 08 §4.2). Its content now stands in Workflow C step 6 [S002 pp. 22–23; S037 pp. 6–7] and Warning sign 8 [S017 TR pp. 4, 12; S001 TR pp. 9–10], and Method 6 step 3 carries the original-file check [S002 pp. 22–23]. The anchor stays; SKILL.md links it from Workflow C step 6.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 11. **Check and report in the original model, with tolerances in its units** (co-authored, group): final checks on the original file [S002 pp. 22–23]; the violation a tolerance allows, in the model's own quantity [S037 pp. 6–7]; no valid dual bound "since precisely speaking a different problem is solved" [S017 TR p. 4]. ([ledger](#heuristic-11))


### Before T3.6

New in T3.6 (08 §5: heuristic HA).

<a id="heuristic-12"></a>

## Former Heuristic 12 (HB, folded in the review fixes): Presolve serves its consumer

### Full-text evidence (08 §5, copied)

**HB · Presolve serves its consumer (group practice)**

- **Steps**:
  1. Write what the downstream consumer needs as an invariant no reduction may break: the block structure of a parallel interior-point solver [S078 arXiv p. 7; S033 p. 74; S068 pp. 3–4], dual and basis information for LP users [S004 pp. 62–63], the structure other components exploit [S031 p. 24], or certificate coverage in exact solving [S022 p. 15; S038 pp. 2, 6–11].
  2. Admit only reductions whose postsolve keeps it, and switch off presolvers that cannot postsolve what the consumer needs [S004 pp. 62–63].
  3. For exact solving, keep the acceptance thresholds of the floating-point presolver and set the tolerances to zero [S022 p. 13], and state what certificates do not cover [S021 p. 11].
  4. Measure downstream whether the reductions given up would have mattered [S078 arXiv pp. 17, 19].
  5. Check the postsolved solution against the original problem [S004 p. 63].
- **Checks**: recurrence ✅ (interior-point presolve 2020–2026; MIP presolve 2020–2021; exact presolve 2021–2025); say–do ✅ (the invariant is stated [S078 arXiv p. 7]); executable ✅; exclusivity not shown. **Voice**: group; his credited share is PaPILO's dual postsolving with Hoen [S004 p. 83] and first authorship of the 2020 presolve paper [S068 p. 3] (the card reads its voice as group).

### T3.6 long form

12. **Presolve serves its consumer** (group practice): write what the downstream consumer needs as an invariant no reduction may break (block structure for a parallel interior-point solver [S078 arXiv p. 7], dual and basis information for LP users [S004 pp. 62–63], certificate coverage in exact solving [S038 pp. 2, 6–11]); admit only reductions whose postsolve keeps it, and check the postsolved solution against the original problem.

### Changes made in SKILL.md (T3.6)

- **New** (08 §5, HB: recurrence, say–do and executable checks passed; exclusivity not shown; group voice; his credited share is PaPILO's dual postsolving with Hoen [S004 p. 83]). One line in SKILL.md with three card refs [S078 arXiv p. 7; S004 pp. 62–63; S038 pp. 2, 6–11]; the five steps are in the 08 text above. Referenced from the routing row on "exact / verified / certified".

### T3.6 review fixes (2026-11-28)

- **Folded** (review: twelve heuristics; HB failed exclusivity and is mostly group voice, 08 §4.2). Its content now stands in Heuristic 10 (consumer invariants [S078 arXiv p. 7; S004 pp. 62–63]) and Method 4 step 1 (certificate coverage of presolve [S038 pp. 4, 6–10]). The anchor stays; SKILL.md links it from Heuristic 10.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 12. **Presolve serves its consumer** (group): the consumer's need is an invariant no reduction may break (block structure [S078 arXiv p. 7], duals and bases for LP users [S004 pp. 62–63], certificate coverage [S038 pp. 2, 6–11]). ([ledger](#heuristic-12))


### Before T3.6

New in T3.6 (08 §5: heuristic HB).

<a id="misreadings"></a>

## Common Misreadings

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Common Misreading 4 | bylines alphabetical until 2017 | Alphabetical bylines appear before and after 2017 [S020 TR p. 3; S039 p. 3; S019 p. 3; S041 p. 3; S068 p. 3; S060 p. 1; S085 p. 1]; a non-alphabetical first-author byline in 2016/2017 [S011 pp. 1, 3]; release reports put the lead first and the rest alphabetically [S003 pp. 3, 41; S021 p. 1; S007 p. 1] | Replace by: byline order is not a reliable signal of his role |

### Changes made in SKILL.md (T3.6)

- Misreading 1: + [S072 p. 14].
- Misreading 4: "Bylines were alphabetical until 2017" replaced by "Byline order is no reliable signal of his role" with [S019 p. 3; S011 pp. 1, 3] (08 §3.2); the long form also cites [S085 p. 1] and the release-report convention [S003 p. 3].
- Misreading 5: + [S002 p. 43].

### T3.6 review fixes (2026-11-28)

- Misreading 1: *his 2025 study* → *his group's 2025 study (Hoen first)* (review: voice; the study is [S072 p. 14]).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> 1. **"He distrusts floating-point solvers and wants exactness everywhere."** See Taste 4: the solvers are "amazingly stable" [Sim21]; his 2025 study finds almost all decisions of floating-point SCIP exactly correct [NC25; S072 p. 14].


### Before T3.6 (moved verbatim)

1. **"He distrusts floating-point solvers and wants exactness everywhere."** See Taste 4: the solvers are "amazingly stable" [Sim21]; his 2025 study finds almost all decisions of floating-point SCIP exactly correct [NC25].
2. **"A VIPR-verified result is safe because the certificate is simple."** Method 4: checker holes 2016–2026, forged certificates accepted [Wood23], presolve outside [S10].
3. **"Exact MIP costs a factor of 2 to 4" (or "of 8").** Both are his group's numbers, for different baselines (3.9 like-for-like, 8.1 default; Method 2 step 3).
4. **"He runs SCIP at ZIB and fathered its PhD generation."** ZIB group headship ended 31 Mar 2023; HTW professor since 1 Oct 2020; Mexi is scipopt.org's primary contact [06 §1, §8]. One formal doctorate, as second supervisor; five mentees have Koch as sole advisor [04 V1–V2]. Bylines were alphabetical until 2017.
5. **"MIPLIB 2017 tells you which solver is best."** The paper says the opposite: the set is "only one of many possible and justified outcomes" [M17 pp. 445, 485].

<!-- anatomies -->

<a id="anatomy-iterative-refinement"></a>

## Anatomy: Iterative refinement for linear programming (ISSAC 2012, DOI 10.1145/2442829.2442858; INFORMS J. Comput. 28, 2016, DOI 10.1287/ijoc.2016.0692)

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Signature Work Anatomy, iterative refinement | content from the thesis; ISSAC 2012 and IJOC 2016 not read | Both now read in report versions. The +3% and +7% slowdowns and the 7 of 1,202 failures are in the journal report [S013 TR pp. 19–20] and the thesis; ISSAC 2012 has its own smaller study [S020 TR pp. 9–10]. The 1.85 to 3 speed-up is in the thesis [S032 pp. 15, 99–100] | Attribute the numbers to the journal and thesis, not to ISSAC |

### T3.6 long form

Read in their report versions [S020 TR; S013 TR] and in the thesis, which contains both [S032].

| Dimension | Finding |
|---|---|
| Origin | Stated: Steffy's initiative [Th p. iii; S032 p. 5]; MINLP instabilities sit in LP relaxations; metabolic models defeat double precision [Th pp. 1–2; S032 pp. 13–14] |
| Key insight | Refinement for LP: solves in floating point, corrections in rationals; scaling the residuals is what lets it work with absolute tolerances [S032 pp. 39–40; S013 TR p. 6] |
| Minimum evidence | ISSAC 2012: violations at most 4.6·10^-31 after five rounds on a troublesome set [S020 TR pp. 9–10]; precision 10^-50 at 3% / 7% average slowdown in the journal report and the thesis [S013 TR pp. 19–20; S032 pp. 66–67]; exact SoPlex 1.85–3 times faster than QSopt_ex (thesis) [Th pp. 3, 88; S032 pp. 15, 99–100] |
| Abandoned paths | Fails on 7 of 1,202 LPs, QSopt_ex solving 6 of them [S032 pp. 100–101]; background rational factorization proposed in the thesis and in 2020, no later record [S029 p. 25]; boosting done 2023/2025 [PB25; S050 pp. 2, 6] |
| Reception | COBRApy and NEOS (thesis claim, unchecked) [S032 pp. 17–18]; theory followed [LPO20] |
| Methods | 5, 7, 3 |

### Changes made in SKILL.md (T3.6)

- The note "Content from the thesis, which contains both (not read)" became "Read in their report versions [S020 TR; S013 TR] and in the thesis" (08 §3.2).
- Origin: + [S032 p. 5]. Key insight: + the scaling that makes refinement work with absolute tolerances [S032 pp. 39–40]. Minimum evidence: the 3% / 7% slowdowns sourced to the journal report [S013 TR pp. 19–20] (and the thesis), the 1.85–3 speed-up to the thesis [S032 p. 99] (08 §3.2: not ISSAC; ISSAC's own smaller study [S020 TR pp. 9–10] is in the long form). Abandoned paths: + [S032 pp. 100–101]. Methods: + 7.

### T3.6 review fixes (2026-11-28)

- **Five anatomies** (review: six exceed the framework's three to five): the oracle paper's rows joined this anatomy as its theory sequel (2020 parts of Origin, Key insight, Minimum evidence and Abandoned paths [S029 pp. 3, 7, 8–17, 23, 25–26]); its own section below keeps the full rows.
- **Minimum evidence**: the 3% / 7% slowdowns cite [S013 TR p. 20], where the sentence stands (review: [S013 TR pp. 19–20]).
- **Introduction** (review: *All six rest on the full texts* overstated): all five cite the full texts where they exist; Reception cells and cells keyed to web sources do not.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> "Inferred" marks what has no primary source. All six rest on the full texts.
> **Iterative refinement for linear programming (ISSAC 2012, DOI 10.1145/2442829.2442858; INFORMS J. Comput. 28, 2016, DOI 10.1287/ijoc.2016.0692)**
>
> Read in their report versions [S020 TR; S013 TR] and in the thesis, which contains both [S032].
>
> | Dimension | Finding |
> |---|---|
> | Origin | Stated: Steffy's initiative [Th p. iii; S032 p. 5]; MINLP instabilities sit in LP relaxations; metabolic models defeat double precision [Th pp. 1–2] |
> | Key insight | Refinement for LP: solves in floating point, corrections in rationals; scaled residuals make it work with absolute tolerances [S032 pp. 39–40] |
> | Minimum evidence | Precision 10^-50 at 3% / 7% average slowdown [S013 TR pp. 19–20]; exact SoPlex 1.85–3 times faster than QSopt_ex [Th pp. 3, 88; S032 p. 99] |
> | Abandoned paths | Fails on 7 of 1,202 LPs [S032 pp. 100–101]; background rational factorization (no record); boosting done 2023/2025 [PB25] |
> | Reception | COBRApy and NEOS (thesis claim, unchecked); theory followed [LPO20] |
> | Methods | 5, 7, 3 |
>
> ([full evidence](#anatomy-iterative-refinement))


### Before T3.6 (moved verbatim)

Content from the thesis, which contains both (not read).

| Dimension | Finding |
|---|---|
| Origin | Stated: Steffy's initiative [Th p. iii]; MINLP instabilities sit in LP relaxations; metabolic models defeat double precision [Th pp. 1–2] |
| Key insight | Refinement for LP: solves in floating point, corrections in rationals |
| Minimum evidence | Precision 10^-50 at 3% / 7% average slowdown; exact SoPlex 1.85–3 times faster than QSopt_ex [Th pp. 3, 88] |
| Abandoned paths | Fails on 7 of 1,202 LPs; background rational factorization (no record); boosting done 2023/2025 [PB25] |
| Reception | COBRApy and NEOS (thesis claim, unchecked); theory followed [LPO20] |
| Methods | 5, 3 |

<a id="anatomy-vipr"></a>

## Anatomy: Verifying Integer Programming Results (IPCO 2017, DOI 10.1007/978-3-319-59250-3_13; arXiv 1611.08832)

### T3.6 long form

| Dimension | Finding |
|---|---|
| Origin | Co-authored: solvers occasionally answer wrongly, exact solvers can have bugs; the motive is said not to be distrust [VIPR §1; S019 p. 3]. Alphabetical byline |
| Key insight | Statements checkable by few rules, independent of the solver [S019 pp. 3, 5–8] |
| Minimum evidence | 107 instances; checking far cheaper than solving; 10 GB shrunk to 8 kB [VIPR Table 1; S019 p. 10] |
| Abandoned paths | v1 excluded one instance (tool out of memory), v2 fixed it (the version read reports all 107 [S019 p. 10]); proof-assistant checking left to others |
| Reception | Formal checkers by others [CakeML; LeanVIPR]; holes found 2023–2026 [Wood23; VIPR-gh] |
| Methods | 4, 3 |

### Changes made in SKILL.md (T3.6)

- Origin: + [S019 p. 3] (the motive stated as not distrust). Key insight: + [S019 pp. 5–8]. Minimum evidence: + [S019 p. 10]. The v1/v2 instance exclusion cannot be checked from the file read, which reports all 107 instances (S019 card); kept as before, the check noted in the long form.

### T3.6 review fixes (2026-11-28)

- Abandoned paths: the v1/v2 statement is marked as web research on the arXiv versions; the version read reports all 107 instances [S019 p. 10] (review).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> | Abandoned paths | v1 excluded one instance (tool out of memory), v2 fixed it; proof-assistant checking left to others |


### Before T3.6 (moved verbatim)

| Dimension | Finding |
|---|---|
| Origin | Co-authored: solvers occasionally answer wrongly, exact solvers can have bugs [VIPR §1]. Alphabetical byline |
| Key insight | Statements checkable by few rules, independent of the solver |
| Minimum evidence | 107 instances; checking far cheaper than solving; 10 GB shrunk to 8 kB [VIPR Table 1] |
| Abandoned paths | v1 excluded one instance (tool out of memory), v2 fixed it; proof-assistant checking left to others |
| Reception | Formal checkers by others [CakeML; LeanVIPR]; holes found 2023–2026 [Wood23; VIPR-gh] |
| Methods | 4, 3 |

<a id="anatomy-miplib-2017"></a>

## Anatomy: MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library (Math. Program. Comput. 13, 2021, DOI 10.1007/s12532-020-00194-3)

### T3.6 long form

| Dimension | Finding |
|---|---|
| Origin | Stated: call of 11 Nov 2016 [Call16]; committee of 21, nine solver teams [S002 p. 2] |
| Why then | Co-authored: virtual-best and virtual-worst speed-ups of 2.70 and 3.62, 2011–2018 [M17 p. 444; S002 p. 2]. Inferred: 5,721 instances [S002 p. 7], too many to pick by hand |
| Key insight | Selection as optimization models over feature clusterings; the process is the contribution [S002 pp. 3, 42] |
| Minimum evidence | Feature clusters agree with submitters' model groups [M17 p. 485; S002 p. 37] |
| Abandoned paths | Old checker tolerance replaced by a mixed absolute/relative rule [S002 pp. 22–23]; two numerically unstable instances (neos-5075914-elvire, neos-3754224-navua) triggered benchmark v2 (June 2019) [M17 pp. 485–486, fn. 8; S002 pp. 43–44], which exchanged five in total to keep balancedness [MIPLIB-CL] |
| Reception | Received Jul 2019, accepted Sep 2020 [S002 p. 1]; tuning-on-MIPLIB critiques |
| Methods | 6, 4 |

### Changes made in SKILL.md (T3.6)

- Origin: + committee of 21 with nine solver teams [S002 p. 2]. Why then: + [S002 p. 2]. Key insight: + [S002 p. 42]. Minimum evidence: + [S002 p. 37]. Abandoned paths: + [S002 p. 22] for the tolerance rule; the five exchanged instances are sourced to the changelog (08 §3.2). Pages 25–26 of the file are cited nowhere (sealed material).

### Before T3.6 (moved verbatim)

| Dimension | Finding |
|---|---|
| Origin | Stated: call of 11 Nov 2016 [Call16]; committee of 21, nine solver teams |
| Why then | Co-authored: virtual-best and virtual-worst speed-ups of 2.70 and 3.62, 2011–2018 [M17 p. 444]. Inferred: 5,721 instances, too many to pick by hand |
| Key insight | Selection as optimization models over feature clusterings; the process is the contribution |
| Minimum evidence | Feature clusters agree with submitters' model groups [M17 p. 485] |
| Abandoned paths | Old checker tolerance replaced by a mixed absolute/relative rule; two numerically unstable instances (neos-5075914-elvire, neos-3754224-navua) triggered benchmark v2 (June 2019), which exchanged five in total to keep balancedness [M17 pp. 485–486, fn. 8; MIPLIB-CL] |
| Reception | Received Jul 2019, accepted Sep 2020; tuning-on-MIPLIB critiques |
| Methods | 6, 4 |

<a id="anatomy-status-update"></a>

## Anatomy: A computational status update for exact rational mixed integer programming (IPCO 2021, DOI 10.1007/978-3-030-73879-2_12; Math. Program. 197, 2023, DOI 10.1007/s10107-021-01749-5), through SCIP 10.0 (arXiv 2511.18580)

### T3.6 long form

| Dimension | Finding |
|---|---|
| Origin | Co-authored: roundoff undermines optimality where MIP proves mathematics or verifies hardware; the 2013 framework lacked presolve and heuristics [S022 p. 2]. First author Eifler |
| Key insight | Hybrid precision in every component: what only proposes stays in floating point behind an exact step, what changes the model runs in rationals [S022 pp. 2, 4–5] |
| Minimum evidence | Against the 2013 framework: 6.6 times faster, 2.8 times as many solved [ZR21-04]; 10.7 and 2.9 in the journal [SU23; S022 pp. 1, 17]; no reason given; hardware (Xeon E5-2660 → Gold 5122) and CPLEX setup differ between the versions [ZR21-04 p. 7; SU23 p. 801; S022 p. 9] (inferred possible cause) |
| Abandoned paths | Bound-shift off below 20% success [S022 p. 12] |
| Reception | Critics relay 8.1; a rival matches exact SCIP in one application [IHS26]; the mode ships in SCIP 10 [S021 pp. 7, 9] |
| Methods | 2, 5, 3 |

### Changes made in SKILL.md (T3.6)

- Origin: + [S022 p. 2]. Key insight: + proposers stay in floating point behind an exact step, model changes run in rationals [S022 pp. 4–5]. Minimum evidence: + [S022 p. 17] for the journal's 10.7 (the S022 card: on the 54 one-solved instances). Abandoned paths: + [S022 p. 12]. The long form also has the release [S021 pp. 7, 9].

### Before T3.6 (moved verbatim)

| Dimension | Finding |
|---|---|
| Origin | Co-authored: roundoff undermines optimality where MIP proves mathematics or verifies hardware; the 2013 framework lacked presolve and heuristics. First author Eifler |
| Key insight | Hybrid precision in every component |
| Minimum evidence | Against the 2013 framework: 6.6 times faster, 2.8 times as many solved [ZR21-04]; 10.7 and 2.9 in the journal [SU23]; no reason given; hardware (Xeon E5-2660 → Gold 5122) and CPLEX setup differ between the versions [ZR21-04 p. 7; SU23 p. 801] (inferred possible cause) |
| Abandoned paths | Bound-shift off below 20% success |
| Reception | Critics relay 8.1; a rival matches exact SCIP in one application [IHS26] |
| Methods | 2, 5, 3 |

<a id="anatomy-limited-precision-oracles"></a>

## Anatomy: Linear programming using limited-precision oracles (Gleixner, Steffy, Math. Program. 183, 2020, DOI 10.1007/s10107-019-01444-6; arXiv 1912.12820)

### T3.6 long form

| Dimension | Finding |
|---|---|
| Origin | Co-authored, two authors, he first: complexity analyses assume exact arithmetic or count bits, implementations use limited precision [S029 p. 3]; the fastest exact LP methods had no theory [S029 p. 7] |
| Why then | Inferred: the refinement code and its 1,202-LP test bed existed [S029 pp. 8, 22–23], so the theory followed working code |
| Key insight | The floating-point simplex as an oracle with constants and a failure outcome; oracle-polynomial bounds for the exact layers on top [S029 pp. 8–17] |
| Minimum evidence | A 3 × 6 LP whose classical tolerance is about 10^-169,059 while its vertex denominators are at most 8 [S029 pp. 6–7]; basis verification solved 1,191 of 1,202 LPs against QSopt_ex's 1,163 [S029 p. 23] |
| Abandoned paths | Background rational factorization and boosting inside refinement left as proposals [S029 pp. 25–26]; boosting built in 2025 as an outer loop [S050 pp. 5–8] |
| Reception | The boosting paper carries the oracle argument to the combined algorithm [S050 pp. 8–9] |
| Methods | 7, 5, 3 |

### Changes made in SKILL.md (T3.6)

- **New anatomy** (Gleixner and Steffy, Math. Program. 183, 2020; own voice, he first of two): the work behind Method 7. Rows from the S029 card [S029 pp. 3, 7, 8–17, 23, 25–26]; the long form also has the 3 × 6 example [S029 pp. 6–7] and the later boosting paper [S050 pp. 5–9].

### T3.6 review fixes (2026-11-28)

- Merged into the iterative-refinement anatomy in SKILL.md (review: six anatomies); SKILL.md links this section from there.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> **Linear programming using limited-precision oracles (Gleixner, Steffy, Math. Program. 183, 2020, DOI 10.1007/s10107-019-01444-6)**
>
> | Dimension | Finding |
> |---|---|
> | Origin | Co-authored, he first of two: analyses assume exact arithmetic, implementations use limited precision [S029 pp. 3, 7] |
> | Key insight | The floating-point simplex as an oracle with constants and a failure outcome [S029 pp. 8–17] |
> | Minimum evidence | Basis verification solved 1,191 of 1,202 LPs, QSopt_ex 1,163 [S029 p. 23] |
> | Abandoned paths | Background factorization and boosting inside refinement left as proposals [S029 pp. 25–26] |
> | Methods | 7, 5, 3 |
>
> ([full evidence](#anatomy-limited-precision-oracles))


### Before T3.6

New in T3.6: an important work read in full that had no anatomy (08 §4.1 and §2, Method 1; framework §五 asks for one anatomy per core method).

<a id="anatomy-decision-analysis"></a>

## Anatomy: Analyzing the numerical correctness of branch-and-bound decisions for mixed-integer programming (Hoen, Gleixner, CPAIOR 2025, DOI 10.1007/978-3-031-95976-9_3; arXiv 2412.14710)

### T3.6 long form

| Dimension | Finding |
|---|---|
| Origin | Group (Hoen first): a belief "widely accepted" that mature solvers handle numerics robustly, beside documented wrong answers [S072 p. 2]; a per-derivation measurement was VIPR future work in 2017 [S019 p. 10] |
| Key insight | Check every critical decision of the unchanged floating-point solver a posteriori, cheapest check first [S072 pp. 4–8] |
| Minimum evidence | FPEasy errors on 2 of 57 instances, dual side only; NumDiff 25 and 27 of 50 fully correct, original and permuted [S072 p. 9] |
| Abandoned paths | Tighter tolerances tested as the remedy; they help only partly [S072 p. 12] |
| Reception | Its conclusion reads the result two ways: robustness quantified, and a route to exact solving with the floating-point solver as a grey box [S072 pp. 14–15] |
| Methods | 1, 4, 5 |

### Changes made in SKILL.md (T3.6)

- **New anatomy** (Hoen and Gleixner, CPAIOR 2025; group voice): the main practice evidence of Method 1, now resting on its full text [S072 pp. 2, 4–9, 12, 14–15] and on VIPR's 2017 future-work proposal [S019 p. 10].

### T3.6 review fixes (2026-11-28)

- **Origin** (review: the VIPR edge is the skill's reading): VIPR's 2017 proposal [S019 p. 10] marked as an inferred link; the paper cites VIPR only in its outlook [S072 p. 15]. **Minimum evidence and abandoned paths** merged into one row pointing to Method 1 steps 5–6 [S072 pp. 9, 12] (review: duplicate rows; the full rows are in the long form above).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> | Origin | Group (Hoen first): the belief in solver robustness set against documented wrong answers [S072 p. 2]; VIPR future work [S019 p. 10] |
> | Minimum evidence | The counts of Method 1 step 5 [S072 p. 9] |
> | Abandoned paths | Tighter tolerances help only partly [S072 p. 12] |


### Before T3.6

New in T3.6: an important work read in full that had no anatomy (08 §4.1 and §2, Method 1; framework §五 asks for one anatomy per core method).

**Signature Work Anatomy introduction (before T3.6):** "Inferred" marks what has no primary source.

<a id="anti-patterns"></a>

## Research Anti-patterns

### T3.6 long form

Besides the warning signs and Taste marks 2 and 4: aggressive heuristics inside a solver (→ H7) [S018 p. 4]; assertions and debug solutions as the only bug finders [MIPDD §1; S065 p. 2] (→ H4c); an "exact" or "valid" label without the sense in which it holds (→ H11; Warning sign 8) [S017 TR pp. 4, 12].

### Changes made in SKILL.md (T3.6)

- Card pages added for the two existing anti-patterns [S018 p. 4; S065 p. 2] and a third one: "exact" without the sense in which it holds (→ H11) [S017 TR p. 12].

### T3.6 review fixes (2026-11-28)

- The third anti-pattern was dropped (review: one card only, from a co-authored applied paper; it duplicated Warning sign 8, which carries it with [S017 TR pp. 4, 12; S001 TR pp. 9–10]).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> Besides the warning signs and Taste marks 2 and 4: aggressive heuristics inside a solver (→ H7) [S018 p. 4]; assertions and debug solutions as the only bug finders [MIPDD §1; S065 p. 2] (→ H4c); "exact" without the sense in which it holds (→ H11) [S017 TR p. 12]. ([full evidence](#anti-patterns))


### Before T3.6 (moved verbatim)

Besides the warning signs and Taste marks 2 and 4: aggressive heuristics inside a solver (→ H7); assertions and debug solutions as the only bug finders [MIPDD §1] (→ H4c).

<a id="trajectory"></a>

## Research Trajectory and Latest

### Full-text evidence (08 §8, copied)

| Period | Works with a card | First-listed (alphabetical bylines included) or sole | Main topics (works) |
|---|---|---|---|
| 2008–2012 | 13 | 4: S025, S017, S020, S066 | MINLP components in SCIP (4); applications: mining, water networks (4); Suite overview (2, one work); MIPLIB 2010 (1); exact LP begins (1); LP linear algebra (1) |
| 2013–2017 | 13 | 5: S039, S032, S013, S011, S003 | MINLP components (4); exact LP and certificates (3); Suite reports (3; 5.0 as lead); applications (2); branching (1) |
| 2018–2022 | 41 | 7: D004, S002, S029, S041, S068, S101, D001 | applications and the energy HPC consortium (8); MINLP components with students (7); parallel, HPC and GPU (7); exact and certified (5); benchmark libraries and competitions (4); Suite reports (4; 6.0 as lead); presolve, propagation and conflict analysis (4); ML for MIP (2) |
| 2023–2026 | 33 | 1: S026 | exact and certified (8: S022 journal, S036, S074, S050, S072, S060, S038, S085); applications at HTW (7); presolve, conflict analysis, heuristics (5); MINLP cuts (4); Suite reports (3; 10.0 ships exact mode); GPU and distributed (3); ML for MIP (1); debugging (1); competitions (1) |

**Turns.**
1. From applied IP to solver numerics in 2012: first contact with ZIB through SCIP in the 2008 Diplom thesis [S025 p. 7]; mining in 2008–2009 [S025; S008]; the first exact-LP paper in 2012 [S020 TR p. 3].
2. From author to lead of group instruments, 2017–2021: the 5.0 release report with him first [S003 p. 3], the 6.0 report likewise [D004], and MIPLIB 2017 as first of 16 [S002 p. 1].
3. From author to supervisor and co-author after 2018: first-listed or sole in 4 of 13, 5 of 13, 7 of 41 and 1 of 33 works per period (table). Credited own code shrinks to single features [S004 p. 83; S007 p. 27; S021 p. 39].
4. Exactness into the mainline, one component at a time, 2021–2025 [D002 p. 14; S036 pp. 2, 26–27; S074 p. 12; S021 pp. 7, 9].
5. HTW-era applications 2024–2026 [S091; S092; S082 report p. 3; S087; H002 p. 13].

**Constant across the periods.** The producing/deciding split from 2012 to 2026 [S020 TR pp. 3, 5; S085 pp. 12–14]; limits printed with counts in most works (Method 3); like-for-like baselines from 2012–2013 [S017 TR pp. 15–17; S039 pp. 7–8] to 2026 [S085 pp. 17–19]; shifted geometric means and both-solved subsets [S028 p. 7; S003 pp. 6–8; S022 p. 9; S078 arXiv p. 18].

---

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Latest | CHAP won the Land-Doig MIP Competition `[CHAP26]` | The paper says CHAP was developed for the competition and evaluates it on the competition's 50 instances under its constraints; it reports no ranking [S076 pp. 1–2, 9] | Re-source the first place to the competition results page cited in 06-trajectory.md (not read in this step); keep the paper only for the benchmark results |
| Research Trajectory | proof logging from pseudo-Boolean solving `[L2R21; …]` | Learn to relax contains no proof log; soundness comes from exact reasoning plus a cross-solver check [S024 pp. 6, 15]; it starts the Nordström collaboration [D006 pp. 1–2]. Proof logging appears in [S038 pp. 2, 6–11; S060 pp. 1–2; S007 p. 17] | Move L2R21 to the collaboration, not the proof-logging line |
| Latest | numerically safe branch-price-and-cut closing 14 unsolved instances | The count is the paper's abstract [S085 p. 1] | Cite the page |

### T3.6 long form

- 2006–2015: applied IP (mining) [S025 p. 7; S008]; ZIB solver team from 2008 [06 T1]; MINLP components in SCIP [LVB13; OBBT17; S039; S011].
- 2012–2016: exact LP, trust in floating-point decisions, certificates, triggered by LP-relaxation instabilities [IR16; Th; STSM14; VIPR; S020 TR p. 3].
- 2015–2023: group head; SCIP 5.0/6.0 lead [S003 p. 3; D004]; MIPLIB 2017 [M17; S002 p. 1]; MIPcc23 [CC23].
- From 2018: author to supervisor. He is first-listed or sole in 4 of 13, 5 of 13, 7 of 41 and 1 of 33 carded works of 2008–12, 2013–17, 2018–22 and 2023–26 [08 §8]; credited own code shrinks to single features [S004 p. 83; S021 p. 39].
- 2020–2025: a collaboration with Nordström from pseudo-Boolean solving, starting with Learn to relax, which carries no proof log [L2R21; S024 pp. 6, 15]; proof logging follows [S038 pp. 2, 6–11; S060 pp. 1–2]; exactness into the mainline, one component at a time [SU23; GMI24; PB25; S10; S021 pp. 7, 9].
- 2021–2023: ML for MIP as a follower, then exit [06 T8]. 2020–2026: GPU methods; applied HTW projects [CP21; CHAP26; S092; S087; H002].

**Latest**

- SCIP 10.0.0 (24 Nov 2025) with exact mode [S10]; own commits to the exact linear constraint handler to Oct 2026 [06 §7–§8].
- 2026: MIP-DD in print [MIPDD]; numerically safe branch-price-and-cut closing 14 unsolved instances [LCCP26; S085 p. 1]; CHAP, developed for the 2026 Land-Doig MIP Competition [CHAP26; S076 pp. 1–2], whose first place rests on the competition page [06 §8], not on the paper; distributed presolving [DSAP26].
- Oct 2026: VIPR and presolve soundness reports (Method 4); applied HTW projects [06 §8]; no talk found in the last 12 months.

### Changes made in SKILL.md (T3.6)

- Turns added from 08 §8: author to supervisor from 2018 (first-listed or sole per period; credited own code shrinks to single features [S004 p. 83]).
- **Corrections** (08 §3.2): "proof logging from pseudo-Boolean solving [L2R21; …]" → the Nordström collaboration starts with Learn to relax, which holds no proof log [S024 pp. 6, 15]; proof logging follows [S038 pp. 2, 6–11; S060 pp. 1–2]. Latest: the 14 unsolved instances cited to the abstract page [S085 p. 1]; CHAP: the paper reports no ranking [S076 pp. 1–2, 9], so the first place is re-sourced to the competition page cited in 06 (§8, sources 38–39; not reread in this step).
- Card pages for the early phases [S025 p. 7; S003 p. 3].

### Before T3.6 (moved verbatim)

- 2006–2015: applied IP (mining); ZIB solver team from 2008 [06 T1]; MINLP components in SCIP [LVB13; OBBT17].
- 2012–2016: exact LP, trust in floating-point decisions, certificates, triggered by LP-relaxation instabilities [IR16; Th; STSM14; VIPR].
- 2015–2023: group head; SCIP 5.0/6.0 lead; MIPLIB 2017; MIPcc23 [M17; CC23].
- 2020–2025: proof logging from pseudo-Boolean solving; exactness into the mainline, one component at a time [L2R21; SU23; GMI24; PB25; S10].
- 2021–2023: ML for MIP as a follower, then exit [06 T8]. 2020–2026: GPU methods; applied HTW projects [CP21; CHAP26].

**Latest**

- SCIP 10.0.0 (24 Nov 2025) with exact mode [S10]; own commits to the exact linear constraint handler to Oct 2026 [06 §7–§8].
- 2026: MIP-DD in print [MIPDD]; numerically safe branch-price-and-cut closing 14 unsolved instances [LCCP26]; CHAP won the Land-Doig MIP Competition [CHAP26]; distributed presolving [DSAP26].
- Oct 2026: VIPR and presolve soundness reports (Method 4); applied HTW projects [06 §8]; no talk found in the last 12 months.

<a id="lineage"></a>

## Academic Lineage and collaboration pattern

### Full-text evidence (08 §9, copied)

**Most frequent co-authors per period** (distinct works; Suite reports and committee or consortium works excluded; conference and journal versions counted separately):

| Period | Works | Co-authors (works) |
|---|---|---|
| 2008–2012 | 12 | Berthold 6, Vigerske 5, Heinz 5, Koch 3 |
| 2013–2017 | 10 | Berthold 5, Weltge 3, Steffy 3, Müller 2, Wolter 2 |
| 2018–2022 | 25 | Pokutta 5, Müller 4, Serrano 4, Sofranac 4, Koch 4, Lodi 3, Rehfeldt 3 |
| 2023–2026 | 29 | Hoen 8, Eifler 6, Mexi 6, Bestuzheva 5, Ghannam 4, Nordström 3, Berthold 3 |

Sources: the coauthor lines of the cards, e.g. [S039 p. 3; S029 p. 3; S072 p. 1; S065 p. 1].

- **Peers early, students later.** Up to 2017 the co-authors are peers of the ZIB team (Berthold, Vigerske, Heinz, Steffy, Weltge); from 2018 the first authors are students and postdocs, with Gleixner second or last.
- **Own hand on record.** Contribution statements of the release reports credit him with the nonlinearity score and exact SoPlex [S010 p. 28]; OBBT-based bilinear inequalities, nonzero cancellation, the constraint classification with Hendel and an LP-solver integration [S003 p. 37]; conflict-driven diving with Witzig, LP-interface support and ring packing [D004 p. 39]; PaPILO's dual postsolving with Hoen [S004 p. 83]; the HiGHS LP interface with Mexi and Hoen [S007 p. 27]; contributions and revisions to the exact mode whose main author is Eifler [S021 p. 39]; in an interdisciplinary paper, the limitations, exceptions and thresholds [H002 p. 13]. No contribution statement exists for the 2- to 6-author papers, so their voice is read from byline position only.
- **Partners from rival communities.** Nordström from pseudo-Boolean solving, 2020–2025 [D006 pp. 1–2; S024; S062 p. 1; S080 p. 1; S038 p. 1]; Biere acknowledged for delta debugging [S065 p. 13]; Achterberg as co-author of a component replicated in Gurobi [S070 pp. 1, 21–22] besides MIPLIB 2017 [S002 p. 1]; Pokutta and Lodi on learning and GPU work [S012; S040 p. 1; S067 arXiv p. 1]; Sager on QP refinement [S058 p. 3]; Pedroso on two decomposition applications [S041 p. 3; S087 p. 1].
- **Consortia and committees.** The energy HPC project with DLR, GAMS, Jülich and HLRS, 2016–2020, gives no author his own section [S098 p. 2; S033; D005 draft p. 1]; MIPLIB selection by eight author teams in 2010 [S001 TR p. 7] and by a committee of 21 with nine solver teams in 2017 [S002 p. 2]; industry partners SAP [S045; S073 pp. 10, 14] and Siemens [S017 TR p. 3].

---

### Changes made in SKILL.md (T3.6)

- Partners: Nordström cited by card [S062 p. 1]; Biere added, acknowledged for delta debugging [S065 p. 13] (08 §9). The long form had Sager [S058 p. 3], Pedroso and the Gurobi replication [S070 pp. 1, 21–22]; they stay here and in 08 §9.

### Before T3.6 (moved verbatim)

- **Teachers**: Gary Froyland (UNSW, 2006); Rolf H. Möhring (Diplom, TU Berlin 2008). PhD TU Berlin 2015: advisor Martin Grötschel per DepositOnce, referees Thorsten Koch and Andrea Lodi; MGP lists Koch as second advisor [Th; MGP].
- **Peers**: Berthold, Steffy, Wolter, Vigerske, in a peer-run PhD team that inherited SCIP and SoPlex [04 L3–L5].
- **Students** (Common Misreading 4): formal, Eifler [Eif25]; mentored: Hendel, Müller, Rehfeldt, Serrano, Witzig; co-authored chapters: Chmiela, Mexi; at HTW: Hoen [04 V1–V5].
- **Partners**: Steffy (exact LP); Nordström (proof logging [L2R21]); Pokutta (ML); Achterberg (MIPLIB).

<a id="inner-tensions"></a>

## Inner Tensions

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Blind spots; Inner Tensions (significance testing) | no significance tests after 2015; eleven later co-authored texts use none | One-sided Wilcoxon tests in the 2016/2017 OBBT paper, with the sentence on the importance of significance testing [S011 pp. 16, 21]; Wilcoxon markers in all five result tables of the 2018 MINLP paper [S006 p. 20]; one-sided KS tests of MIPLIB 2017's hardness claim [S002 pp. 40–41]. 17 read component or release papers of 2017–2026 run no test (e.g. [S034 pp. 11–25; S080 pp. 18–22; S078 arXiv pp. 12–20; S085 pp. 17–22]) | Tests to 2018 in component studies, once in 2021 on the instrument, none in later component papers read |

### T3.6 long form

- **Tension: trust in floating point.** Roundoff "compromises the results of virtually all fast mixed integer programming solvers" (abstracts) [MIP21; Sim21], yet "amazingly stable" [Sim21]; decisions overwhelmingly correct [NC25; S072 p. 14].
- **Tension: simple certificates vs. the checker's record**, and **the price of exactness** (forecast 2–4 [Sim21]): Common Misreadings 2–3.
- **Tension: what benchmarking is for**: MIPLIB 2017 serves "a meaningful and fair comparison of the average performance of MIP solvers" [M17]; "The motivation is not benchmarking" [Sim21].
- **Tension: exact vs. good solutions early**: "personal interest is also to be even more strict" [Sim21] against [SU23 p. 794].
- **Say vs. do: significance testing**: a non-significant mean gain "shows the importance of significance testing" [Th p. 147]; one-sided Wilcoxon tests in the 2016/2017 OBBT paper [S011 pp. 16, 21] and the 2018 MINLP paper [S006 p. 20], KS tests of MIPLIB 2017's hardness claim [S002 pp. 40–41]; none in the 17 component or release papers of 2017–2026 read in full [S034 pp. 11–25; S080 pp. 18–22].
- **Tension: headline numbers**: one result appears as 6.6, "about an order of magnitude" and 10.7 [ZR21-04; MIP21; SU23].
- **Tension: supervisor in practice, not on record**: "my supervisors Thorsten Koch and Ambros Gleixner" [Mue20]; one formal doctorate [04 C1].
- **Tension: critique answered in code, not in print** [VIPR-gh; Wood23].

### Changes made in SKILL.md (T3.6)

- Significance testing corrected (08 §3.2): one-sided Wilcoxon tests in the OBBT paper [S011 pp. 16, 21] and the 2018 MINLP paper [S006 p. 20], KS tests of MIPLIB 2017's hardness claim [S002 pp. 40–41], none in the later component papers read (08: 17 papers of 2017–2026, e.g. [S034 pp. 11–25; S080 pp. 18–22; S078 arXiv pp. 12–20; S085 pp. 17–22]). The web-research clause "eleven later co-authored texts use none" is in the moved-verbatim copy.

### Before T3.6 (moved verbatim)

- **Tension: trust in floating point.** Roundoff "compromises the results of virtually all fast mixed integer programming solvers" (abstracts) [MIP21; Sim21], yet "amazingly stable" [Sim21]; decisions overwhelmingly correct [NC25].
- **Tension: simple certificates vs. the checker's record**, and **the price of exactness** (forecast 2–4 [Sim21]): Common Misreadings 2–3.
- **Tension: what benchmarking is for**: MIPLIB 2017 serves "a meaningful and fair comparison of the average performance of MIP solvers" [M17]; "The motivation is not benchmarking" [Sim21].
- **Tension: exact vs. good solutions early**: "personal interest is also to be even more strict" [Sim21] against [SU23 p. 794].
- **Say vs. do: significance testing**: a non-significant mean gain "shows the importance of significance testing" [Th p. 147]; eleven later co-authored texts use none.
- **Tension: headline numbers**: one result appears as 6.6, "about an order of magnitude" and 10.7 [ZR21-04; MIP21; SU23].
- **Tension: supervisor in practice, not on record**: "my supervisors Thorsten Koch and Ambros Gleixner" [Mue20]; one formal doctorate [04 C1].
- **Tension: critique answered in code, not in print** [VIPR-gh; Wood23].

<a id="roundtable-card"></a>

## Roundtable Card

### Full-text evidence (08 §3.1 and §3.2, copied)

- **Roundtable Card, Fischetti contrast.** The co-signed nonlinear branching rule picks at random among near-best candidates so that changing the seed exploits branching variability [S004 p. 42] (group). The card's inferred contrast (variability as noise) needs this counter-note.

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Blind spots; Inner Tensions (significance testing) | no significance tests after 2015; eleven later co-authored texts use none | One-sided Wilcoxon tests in the 2016/2017 OBBT paper, with the sentence on the importance of significance testing [S011 pp. 16, 21]; Wilcoxon markers in all five result tables of the 2018 MINLP paper [S006 p. 20]; one-sided KS tests of MIPLIB 2017's hardness claim [S002 pp. 40–41]. 17 read component or release papers of 2017–2026 run no test (e.g. [S034 pp. 11–25; S080 pp. 18–22; S078 arXiv pp. 12–20; S085 pp. 17–22]) | Tests to 2018 in component studies, once in 2021 on the instrument, none in later component papers read |
| Roundtable Card, Lübbecke contrast | default branch and cut on heterogeneous sets with safe dual bounds `[M17; LCCP26]` | LCCP26 is a problem-specific branch-price-and-cut on SCIP that beats a commercial default branch and cut [S085 pp. 17–19] | Drop `LCCP26` from that contrast |

### Changes made in SKILL.md (T3.6)

- Lens: + mixed-precision algorithms with a stated floating-point contract (Method 7).
- Fischetti contrast: + the counter-note that a co-signed rule exploits branching variability [S004 p. 42] (08 §3.1).
- Lübbecke contrast: `LCCP26` dropped (08 §3.2: a problem-specific branch-price-and-cut that beats a commercial default branch and cut [S085 pp. 17–19]).
- Blind spots: "no significance tests after 2015" → "no significance tests in the component papers read after 2018" (08 §3.2).

### T3.6 review fixes (2026-11-28)

- **Leads when** + a low-precision, GPU or third-party LP oracle under an exact layer; **First questions** + what the floating-point solver guarantees and how a violation is detected and counted (review: Method 7 had no signal on the card).
- **Lübbecke** (review: no counter-note where the contrast stands): + his group's 2026 branch and price on SCIP is over 7 times faster than a Gurobi-based branch and cut from the same start [S085 pp. 18–19]; *as proof of concept* dropped for length.
- **Bixby** (review: *every solution checked exactly* repeats the claim the full text contradicts): checked in arbitrary precision within a mixed tolerance, objective values exact [S002 pp. 22, 42]. The pre-synthesis wording is in the moved-verbatim copy above; the Corrections list's MIPLIB line now names the Roundtable Card.

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> - **Leads when**: solvers, seeds or versions disagree; feasibility flips with tolerances (big-M, wide coefficient ranges); an answer serves as a proof or must be exactly feasible; LP re-solves give unreliable bases or duals; a new component is compared with a fuller solver; a benchmark or competition is built; a speed-up is read from a mean; a bug needs reducing; a claim says "exact", "verified" or "certified".
> - **First questions asked**: What is the answer used for? Which decision decides correctness, and is it inside what is checked (presolve too)? What does the baseline have that your code lacks: like-for-like and default factors? Which subset holds the headline, and what does each exclusion bias? Do independent solvers agree? Which checker and version?
>   - *Lübbecke*: generic Dantzig–Wolfe as proof of concept on structured classes (DOI 10.1007/s10107-014-0761-5) against default branch and cut on heterogeneous sets with safe dual bounds [M17].
>   - *Forrest* (guest): referee solvers and borderline tolerance verdicts (https://github.com/coin-or/Cbc/issues/697) against exact checks by an independent checker (DOI 10.1007/978-3-319-59250-3_13). *Bixby* (guest): chained version pairs on private libraries (DOI 10.4171/dms/6/16) against a public library built by written rules, every solution checked exactly (DOI 10.1007/s12532-020-00194-3).


### Before T3.6 (moved verbatim)

- **Lens (one line)**: Can the answer be trusted, and was the comparison fair? Numerics, exact and certified solving, baseline and benchmark design, shipping inside the solver.
- **Leads when**: solvers, seeds or versions disagree; feasibility flips with tolerances (big-M, wide coefficient ranges); an answer serves as a proof or must be exactly feasible; LP re-solves give unreliable bases or duals; a new component is compared with a fuller solver; a benchmark or competition is built; a speed-up is read from a mean; a bug needs reducing; a claim says "exact", "verified" or "certified".
- **First questions asked**: What is the answer used for? Which decision decides correctness, and is it inside what is checked (presolve too)? What does the baseline have that your code lacks: like-for-like and default factors? Which subset holds the headline, and what does each exclusion bias? Do independent solvers agree? Which checker and version?
- **Default recommendation**: keep floating point; add exact repair or safe bounds at the deciding points; measure against a reduced baseline and default on named subsets with seeds; print the remaining gap as a number; ship in the open solver.
- **Will push back on**: rational re-implementations of candidate producers; exactness a tolerance-level answer would serve; factors without baselines; means carried by few instances; averages used to choose solvers; "verified" without checker and coverage; untested defaults.
- **Likely disagreements** (inferred from methods; no dispute documented):
  - *Achterberg*: speed on vendor sets, presolve as a big win (DOI 10.1287/ijoc.2018.0857; DOI 10.1007/978-3-642-38189-8_18) against exact, certifiable reductions [SU23; CPB24].
  - *Fischetti*: variability to exploit, heuristics as methods (DOI 10.1287/opre.2013.1231; DOI 10.1007/s10107-004-0570-3) against variability as noise, heuristics that fail fast [SU23].
  - *Lübbecke*: generic Dantzig–Wolfe as proof of concept on structured classes (DOI 10.1007/s10107-014-0761-5) against default branch and cut on heterogeneous sets with safe dual bounds [M17; LCCP26].
  - *Forrest* (guest): referee solvers and borderline tolerance verdicts (https://github.com/coin-or/Cbc/issues/697) against exact checks by an independent checker (DOI 10.1007/978-3-319-59250-3_13). *Bixby* (guest): chained version pairs on private libraries (DOI 10.4171/dms/6/16) against a public library built by written rules, every solution checked exactly (DOI 10.1007/s12532-020-00194-3).
- **Blind spots**: exact mode about 10 times slower than default, MILP only, no symmetry; his checker was unsound in places; small fixed exactness sets; open-source vantage only; no polyhedral theory; no significance tests after 2015; own voice thin after 2021.

<a id="honest-boundary"></a>

## Honest Boundary

### Full-text evidence (08 §1 and §11, copied)

**1. Coverage**

| Item | Count |
|---|---|
| Card entries | 103: full 90, partial 2, abstract 7, metadata 4 |
| Works with a card | 101; D005 and S022 each have an earlier abstract- or metadata-level card and a later full card |
| Works read in full or in part | 92 (90 full, 2 partial: S063, S064) |
| Abstract level only | D001, S051, S056, S057, S077, S081 (ID cites only, no pages) |
| Metadata only | S099, S101; S088 is a junk Scholar row (Role skip) |
| Batch files | 29: c01–c19 and c3-01 (core), s01–s05 and s3-01 (supplement), b01–b02 (thesis and a book-length guide), a2-01 (abstract and metadata) |
| Quotes | 197, all exact (`verify_card_quotes.py`, 2026-11-28) |
| INDEX Read column | refreshed by `mark_read_from_cards.py`: carded 90, skimmed 2, abstract 6, metadata 3 |
| 07 card index | regenerated by `build_card_index.py --date 2026-11-28` (103 rows) |

Coverage row from `team_status.py`: 107 Scholar rows; 103 distinct works indexed; 92 open full texts; 90 read in full, 2 in part, 6 abstract only, 2 metadata only, 3 skipped; 197 quotes verified.

**Counting rules for the three-paper threshold.** A practice repeated across releases counts once: the SCIP Optimization Suite reports S010, S014, S003, D004, S005, S004, S007, S021, together with the 8.0 journal paper S015 and the 8.0 abstract S096, form one series. These pairs count as one study each: H001/S028 (report and journal), S023/S071 (S071 is the Japanese version of the same 2012 report, card s01), D002/S022 (IPCO and journal), S020/S013 (ISSAC report and journal), D001/S029, S035/S018, S024/D006, S067/S057, D003/S077, S051/S063, S056/S070, D007/S083, S064/S027, S068/S078, S092/S085, S062/S080 (conference and journal extension), S039/S011 (the LVB paper and the OBBT paper that extends it), S025/S008 (thesis and journal). The PhD thesis S032 compiles several of these lines and is counted as its own work.

---

**11. Open gaps**

- **Abstract or metadata only.** The IPCO versions of the oracle paper [D001], of surrogate duality [S051] and of RLT separation [S056]; the journal versions of GPU propagation [S057] and of the progress measure [S077]; the round-up properties paper [S081]; the ICMS session report [S101]; the NIC symposium paper [S099]. For D001, S056, S057 and S077 the content is read in another version [S029; S070; S067 arXiv; D003]; differences between versions are not known.
- **Read in part.** The surrogate-duality journal paper and the 2019 interior-point report: the sections not read are named on their cards [S063; S064].
- **Report or preprint versions.** Many cards read a ZIB report or arXiv version (S001, S013, S017, S020, S011, S029, S058, S067, S078, S082, S085, S015, S026, S060, S007, D002, D003, D005): only the status update was compared across versions [D002; S022].
- **Evidence outside the cards.** Heuristics 1, 3, 4, 5 and 10 and parts of Methods 3 and 4 rest also on talks, commits, pull requests and mailing-list posts that no card covers; the cards neither confirm nor refute those parts.
- **Unresolved by the texts.** Whether the CHAP first place holds (competition page, not read here); the 2017 certificate overhead numbers themselves (not on the VIPR card; the comparison rests on the journal's sentence [S022 p. 16]); whether the background parallel factorization and the MIPLIB hindsight study were ever done [S029 p. 25; S002 p. 43]; his share in the energy HPC line, where no contribution statement exists [S068 p. 3; S098 p. 2].
- **Voice.** Contribution statements exist only for release reports and one interdisciplinary paper; in short bylines his role is inferred from position.
- **No critical outside reading.** No card reads a work that criticises his methods; peer critique stays with the research notes.

### Statements corrected by the full texts (08 §3.2, copied rows)

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Honest Boundary; Field boundary | not decomposition research | Co-authored decomposition papers: price-and-verify with Dantzig–Wolfe for circle packing, first-listed [S041 pp. 3, 14–16]; ring packing in the 6.0 release [D004 pp. 26–27, 39]; branch and price and branch-price-and-cut [S092 pp. 3–7; S085 pp. 1–3, 12–16; S087 pp. 14–25] (group) | Decomposition appears in co-authored application work; no methodological line of his own is shown |
| Field boundary | MINLP components to 2017 | MINLP-side co-authored work continues: [S043 pp. 19–25; S047 pp. 14–16; S063 pp. 12, 24; D007 p. 3; S083 pp. 2, 10–11; S044 pp. 9–13; S070 pp. 21–22] (group, to 2025) | MINLP components as his own line to 2017, as supervisor to 2025 |
| Honest Boundary, Not read | ISSAC 2012, IJOC 2016, JOGO 2017, conflict-driven heuristics, MIPLIB 2010, SCIP 5.0/6.0 reports | Now read: [S020 TR; S013 TR; S011; S034; S001 TR; S003; D004] (report versions where marked) | Update the list (§11 has what remains) |

### T3.6 long form

This skill is distilled from public information and has these limits:
- **Full-text coverage**: 107 Scholar rows, 103 distinct works indexed, 92 open full texts: 90 read in full, 2 in part [S063; S064]; 6 works known only from abstracts, 2 only from metadata, 3 rows skipped (among them the junk Scholar row S088); 197 card quotes verified (2026-11-28). Many cards read a ZIB-Report or arXiv version (cited with TR, arXiv, report or draft); only the status update was compared across versions [D002; S022] [08 §1, §11].
- **Tacit knowledge**: how he picks what is worth doing rests on two acknowledgements; internal reviews, meetings and test sets are not public.
- **Era and resources**: in-house SCIP and SoPlex, a long-lived BMBF campus, industry funding, exclusive cluster nodes, a group of 16 (2017); since 2020 a teaching university. Methods 3 and 6 assume such resources.
- **Field boundary**: numerics, exact and verified LP/MILP, mixed-precision LP and QP algorithms (Method 7), presolve (group), benchmarks, integration; MINLP components as his own line to 2017 and as supervisor to 2025 [S043 pp. 19–25; S070 pp. 21–22]. Decomposition appears only in co-authored application work (price-and-verify for circle packing [S041 pp. 3, 14–16]; branch and price at HTW [S092 pp. 3–7; S085 pp. 1–3]), with no methodological line of his own. Not polyhedral theory, commercial internals, ML for MIP.
- **Claimed but unverified**: significance testing as a rule (thesis, the OBBT paper and the 2018 MINLP paper; no later component paper read); a hierarchy of certificate formats; "dedicated rational heuristics"; a MIPLIB hindsight study [S002 p. 43]; reproducible supplements (VIPR's lagged five years); one job per node (relaxed in 2017 [S002 p. 20]).
- **Not read**: the IPCO versions of the oracle paper [D001], of surrogate duality [S051] and of RLT separation [S056]; the journal versions of GPU propagation [S057] and of the progress measure [S077] (their content is read in other versions); round-up properties [S081]; two short reports [S099; S101]. ISSAC 2012, IJOC 2016, JOGO 2017, the conflict-driven heuristics paper, MIPLIB 2010 and the SCIP 5.0/6.0 reports are now read [S020 TR; S013 TR; S011; S034; S001 TR; S003; D004]. Heuristics 1, 3–5 and 10 and parts of Methods 3 and 4 also rest on talks, commits, pull requests and mailing-list posts that no card covers.
- **Group work and captions**: most evidence after 2016 is group work; MIP 2021 and CO@Work 2024 quotes are unchecked automatic captions.
- **Unresolved by the texts**: whether the CHAP first place holds (competition page, not reread); the 2017 certificate overheads themselves; whether the background factorization and the MIPLIB hindsight study were ever done; his share in the energy HPC line, where no contribution statement exists [S068 p. 3; S098 p. 2]; no card reads a work that criticises his methods.
- **Research date**: 2026-11-28 (deep reading; web research 2026-11-08 to 2026-11-14). He is living and active and GitHub states change fast; update at least yearly or after each major SCIP release.
- **Validation 2026-11-14**: sealed-item test 9 with the skill / 10 without (5 items; 2 points or less is a tie); task test 10 supported and 0 fabricated grounds with the skill (on the version before the after-validation fixes of 2026-11-14; retention re-test after them: 5 of 6 pass); recorded in `FIDELITY.md`, which describes the sealed items: do not open it while using or testing this skill. The validation predates the deep reading.

### Changes made in SKILL.md (T3.6)

- **Coverage line new** (first bullet), from `team_status.py --coverage`: 107 Scholar rows, 103 distinct works indexed, 92 open full texts, 90 read in full, 2 in part, 6 abstract only, 2 metadata only, 3 skipped, 197 quotes verified; many cards read report or arXiv versions (08 §1, §11).
- Field boundary corrected (08 §3.2): mixed-precision LP algorithms added; MINLP components as his own line to 2017, then as co-author [S070 pp. 21–22]; decomposition only in co-authored application work [S041 pp. 3, 14–16] (the long form also cites [S092 pp. 3–7; S085 pp. 1–3]).
- *Claimed but unverified*: significance testing "(thesis only)" → "(to 2018 only)".
- *Not read* rewritten: the works read since (ISSAC 2012, IJOC 2016, JOGO 2017, conflict-driven heuristics, MIPLIB 2010, SCIP 5.0/6.0) left the list; what remains is the abstract- and metadata-level cards [D001; S051; S056; S057; S077; S081; S099; S101], the two partial reads [S063; S064], and the talks, commits and posts that no card covers (08 §11).
- *Unresolved* (new, from 08 §11): the CHAP first place, his share in the energy HPC line, no critical outside reading. The 2017 certificate overhead numbers and the background factorization / MIPLIB hindsight question are in 08 §11 and the long form.
- Research date 2026-11-28; the validation line notes that the validation predates the deep reading.
- *Corrections from the full texts*: a new subsection, one line each; the full list is in the [Corrections](#corrections) section below.

### T3.6 review fixes (2026-11-28)

- **Validation line** (review: SKILL.md linked `FIDELITY.md`, which describes the sealed items, so the link made it a file SKILL.md tells its user to open): the link replaced by plain text with a do-not-open note; `FIDELITY.md` added to the Sources appendix's do-not-open list. The links in this ledger's long form and moved-verbatim copy were removed too. The marco-e-lubbecke and matteo-fischetti skills carry the same link (reported to the operator, not changed here).
- **Not read**: the id lists moved here (review: bookkeeping): abstract or metadata level [D001; S051; S056; S057; S077; S081; S099; S101]; in part [S063; S064].

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> - **Not read**: abstract or metadata level only [D001; S051; S056; S057; S077; S081; S099; S101]; in part [S063; S064]; talks, commits and posts behind Heuristics 1, 3–5 and 10 have no card.
> - **Validation 2026-11-14**: sealed-item test 9 with the skill / 10 without (5 items; 2 points or less is a tie); task test 10 supported and 0 fabricated grounds with the skill (on the version before the after-validation fixes of 2026-11-14; retention re-test after them: 5 of 6 pass); see `FIDELITY.md` (link removed). It predates the deep reading.


### Before T3.6 (moved verbatim)

This skill is distilled from public information and has these limits:
- **Tacit knowledge**: how he picks what is worth doing rests on two acknowledgements; internal reviews, meetings and test sets are not public.
- **Era and resources**: in-house SCIP and SoPlex, a long-lived BMBF campus, industry funding, exclusive cluster nodes, a group of 16 (2017); since 2020 a teaching university. Methods 3 and 6 assume such resources.
- **Field boundary**: numerics, exact and verified LP/MILP, presolve (group), benchmarks, integration, MINLP components to 2017. Not polyhedral theory, commercial internals, decomposition research, ML for MIP.
- **Claimed but unverified**: significance testing as a rule (thesis only); a hierarchy of certificate formats; "dedicated rational heuristics"; a MIPLIB hindsight study; reproducible supplements (VIPR's lagged five years); one job per node (relaxed in 2017).
- **Not read**: ISSAC 2012, IJOC 2016, JOGO 2017, the conflict-driven heuristics paper, MIPLIB 2010, SCIP 5.0/6.0 reports.
- **Group work and captions**: most evidence after 2016 is group work; MIP 2021 and CO@Work 2024 quotes are unchecked automatic captions.
- **Research date**: 2026-11-14 (notes 2026-11-08). He is living and active and GitHub states change fast; update at least yearly or after each major SCIP release.
- **Validation 2026-11-14**: sealed-item test 9 with the skill / 10 without (5 items; 2 points or less is a tie); task test 10 supported and 0 fabricated grounds with the skill (on the version before the after-validation fixes of 2026-11-14; retention re-test after them: 5 of 6 pass); see `FIDELITY.md` (link removed in the T3.6 review: the file describes the sealed items).

<a id="corrections"></a>

## Corrections from the full texts

### The full list (08 §3.2, copied)

Full texts win over web snippets and talk captions. Each row says what changes.

| SKILL.md location | Current statement | What the full text shows | Change |
|---|---|---|---|
| Latest | CHAP won the Land-Doig MIP Competition `[CHAP26]` | The paper says CHAP was developed for the competition and evaluates it on the competition's 50 instances under its constraints; it reports no ranking [S076 pp. 1–2, 9] | Re-source the first place to the competition results page cited in 06-trajectory.md (not read in this step); keep the paper only for the benchmark results |
| Method 3 Evidence | VIPR future work → decision analysis `[NC25]` and delta debugging `[MIPDD]` | VIPR's future work names approximate certificates for debugging solvers and for measuring numerical violation [S019 p. 10]; MIP-DD gives the limits of assertions and debug solutions as its origin and mentions VIPR only as a planned interface [S065 pp. 1–2, 13] | Keep VIPR → decision analysis; mark the MIP-DD edge as inferred, with MIP-DD's own origin |
| Method 2 step 4 | quote cited `[SU23 p. 810]` | The sentence is on file p. 17 = printed p. 809 [S022 p. 17] | Cite printed p. 809 |
| Heuristic 6 | three numbered questions each in `[LPO20]`, `[SU23]`, `[GMI24]` | The journal opens with four main questions [S022 p. 8]; three is the IPCO version [D002 p. 8]; three in [S029 p. 22] and [S036 p. 20] | Three in LPO20, GMI24 and the IPCO version; four in the journal |
| Method 4 step 6; Method 3 Limitations (overhead forecast) | +101% FPEasy, +51% NumDiff (2021) `[ZR21-04]`; the 2017 forecast of shrinking overhead failed by 2021 | IPCO: +101.2% and +51.4% [D002 pp. 13–14]. Journal: +56.3% (fpeasy), +22% (numdiff), +46% (miplib) on both-solved instances, which it reads as confirming the 2017 measurements [S022 p. 16]. The 2017 text expected times much closer to the non-certifying solver [S019 p. 10] | Give both versions with their numbers; restate the forecast counter-evidence as: not realised in print by 2023, the journal's overheads being of the size it calls confirmed from 2017 |
| Method 3 step 5 | SoPlex as exact LP solver lost as many hard instances as it won (automatic captions) | In print: 3 more solved on fpeasy, 6 fewer on numdiff, 18 more on miplib; every loss is a chip-verification instance where refinement breaks down [S022 p. 12], and precision boosting inside SoPlex is named as next step [S022 p. 18] | Replace the caption paraphrase by the printed counts |
| Method 6 step 2 | licence CC BY 4.0 | Default instance licence CC BY-SA 4.0 [S002 p. 6]; CC BY 4.0 is the article's own licence [S002 p. 44] | Correct |
| Method 6 step 3; Taste 1 | every reported solution checked against the original file in exact arithmetic | The checker computes in GMP arbitrary precision but accepts by tolerances, because exact feasibility cannot be expected [S002 p. 22]; objective values of reported solutions are recomputed exactly by fixing the integers [S002 p. 42] | Say arbitrary-precision tolerance checks, plus exact objective values |
| Method 6 step 7 | v2 exchanged five instances | The paper names the two flawed instances and the minimal-exchange use of the selection model, not the count five [S002 pp. 43–44] | Source the five to the changelog only |
| Method 6 step 8 | verify bounds against exact values (MIPcc23) | The paper gives invalid answers twice the worst rank but does not say how validity was checked [S055 p. 7] | Source to the repository or drop the clause |
| Method 1 step 5 | 25 and 27 of 50 `[NC25 Table 1]` | These counts are the text's [S072 p. 9] | Cite the page, not the table |
| Method 5 step 5 | boosting inside refinement | Proposed so in 2020 [S029 p. 26]; as built, an outer precision-boosting loop around an inner refinement loop, both on by default [S007 p. 16; S050 pp. 5–8] | Name both: the proposal and the built order |
| Method 5 Limitations | the 2025 paper replaces 2016's rational reconstruction by basis factorization on average | The thesis already finds the rational factorization about 46% faster on average [S032 p. 100]; the 2020 paper restates it [S029 p. 25]; the 2025 paper confirms it [S050 p. 10]; reconstruction and verification both shipped in 2016 [S010 p. 20] | Date the result to the thesis (2015) |
| Method 5 Limitations | refinement has no reliable recovery when the floating-point LP fails | Printed in 2016 with the remedy [S013 TR p. 23] and in 2023 [S022 p. 7]; a heuristic recovery existed in the QP code [S058 p. 12]; precision boosting provides it from 2025 [S050 pp. 2, 5–6] | Date it: true for LP refinement until 2025 |
| Method 5 step 6 | check the optimality of the basis early `[LPO20]` | Already in the thesis, own voice [S032 p. 85]; then [S029 p. 12] | Credit the thesis first |
| Blind spots; Inner Tensions (significance testing) | no significance tests after 2015; eleven later co-authored texts use none | One-sided Wilcoxon tests in the 2016/2017 OBBT paper, with the sentence on the importance of significance testing [S011 pp. 16, 21]; Wilcoxon markers in all five result tables of the 2018 MINLP paper [S006 p. 20]; one-sided KS tests of MIPLIB 2017's hardness claim [S002 pp. 40–41]. 17 read component or release papers of 2017–2026 run no test (e.g. [S034 pp. 11–25; S080 pp. 18–22; S078 arXiv pp. 12–20; S085 pp. 17–22]) | Tests to 2018 in component studies, once in 2021 on the instrument, none in later component papers read |
| Common Misreading 4 | bylines alphabetical until 2017 | Alphabetical bylines appear before and after 2017 [S020 TR p. 3; S039 p. 3; S019 p. 3; S041 p. 3; S068 p. 3; S060 p. 1; S085 p. 1]; a non-alphabetical first-author byline in 2016/2017 [S011 pp. 1, 3]; release reports put the lead first and the rest alphabetically [S003 pp. 3, 41; S021 p. 1; S007 p. 1] | Replace by: byline order is not a reliable signal of his role |
| Research Integrity | no statement by him on AI use was found | A co-authored 2026 preprint discloses AI-tool use for scripts and language: "The authors checked all scripts, results, and text and take full responsibility for the content." [S078 arXiv p. 27] | Add as a co-authored statement |
| Honest Boundary; Field boundary | not decomposition research | Co-authored decomposition papers: price-and-verify with Dantzig–Wolfe for circle packing, first-listed [S041 pp. 3, 14–16]; ring packing in the 6.0 release [D004 pp. 26–27, 39]; branch and price and branch-price-and-cut [S092 pp. 3–7; S085 pp. 1–3, 12–16; S087 pp. 14–25] (group) | Decomposition appears in co-authored application work; no methodological line of his own is shown |
| Field boundary | MINLP components to 2017 | MINLP-side co-authored work continues: [S043 pp. 19–25; S047 pp. 14–16; S063 pp. 12, 24; D007 p. 3; S083 pp. 2, 10–11; S044 pp. 9–13; S070 pp. 21–22] (group, to 2025) | MINLP components as his own line to 2017, as supervisor to 2025 |
| Roundtable Card, Lübbecke contrast | default branch and cut on heterogeneous sets with safe dual bounds `[M17; LCCP26]` | LCCP26 is a problem-specific branch-price-and-cut on SCIP that beats a commercial default branch and cut [S085 pp. 17–19] | Drop `LCCP26` from that contrast |
| Research Trajectory | proof logging from pseudo-Boolean solving `[L2R21; …]` | Learn to relax contains no proof log; soundness comes from exact reasoning plus a cross-solver check [S024 pp. 6, 15]; it starts the Nordström collaboration [D006 pp. 1–2]. Proof logging appears in [S038 pp. 2, 6–11; S060 pp. 1–2; S007 p. 17] | Move L2R21 to the collaboration, not the proof-logging line |
| Latest | numerically safe branch-price-and-cut closing 14 unsolved instances | The count is the paper's abstract [S085 p. 1] | Cite the page |
| Signature Work Anatomy, iterative refinement | content from the thesis; ISSAC 2012 and IJOC 2016 not read | Both now read in report versions. The +3% and +7% slowdowns and the 7 of 1,202 failures are in the journal report [S013 TR pp. 19–20] and the thesis; ISSAC 2012 has its own smaller study [S020 TR pp. 9–10]. The 1.85 to 3 speed-up is in the thesis [S032 pp. 15, 99–100] | Attribute the numbers to the journal and thesis, not to ISSAC |
| Attribution | PaPILO shows his group and agenda, not his coding | The 8.0 report makes Hoen and Gleixner jointly responsible for PaPILO's dual postsolving: "AH and AG are responsible for the new dual postsolving functionality in PaPILO (Section 6)." [S004 p. 83]; he is first author of the PaPILO paper [S026 p. 1] | Qualify: one credited PaPILO feature, joint |
| Honest Boundary, Not read | ISSAC 2012, IJOC 2016, JOGO 2017, conflict-driven heuristics, MIPLIB 2010, SCIP 5.0/6.0 reports | Now read: [S020 TR; S013 TR; S011; S034; S001 TR; S003; D004] (report versions where marked) | Update the list (§11 has what remains) |

### Where each correction now stands in SKILL.md (T3.6)

| 08 §3.2 row | Where it stands in SKILL.md |
|---|---|
| Latest, CHAP first place | Latest: first place per the competition page [06 §8]; CHAP described as built for the competition, which the paper words as "developed for this competition" [S076 p. 2]; Corrections list (Lineage line) |
| Method 3 Evidence, VIPR → MIP-DD | Method 3 Practice keeps the certificate chain [S019 pp. 10–11 → S072 pp. 14–15]; ✗ bullet on the MIP-DD edge; Corrections |
| Method 2 step 4 page | Stated and step 4 cite [SU23 p. 809; S022 p. 17]; ✗ bullet |
| Heuristic 6 count | Heuristic 6 rewritten; Corrections |
| Method 4 step 6; Method 3 Limitations (overhead forecast) | Method 4 step 6 names both versions; Method 3 ✗ bullet; Corrections |
| Method 3 step 5 | Step 5 rewritten from print [S022 pp. 12, 18] |
| Method 6 step 2 licence | Step 2 and ✗ bullet |
| Method 6 step 3; Taste 1 | Step 3, Taste mark 1, Method 4 step 4 note and ✗ bullets |
| Method 6 step 7 (five exchanged) | Step 7 and the MIPLIB anatomy: "per the changelog" |
| Method 6 step 8 (exact values) | Clause dropped; ✗ bullet [S055 p. 7] |
| Method 1 step 5 | Cites [NC25; S072 p. 9] |
| Method 5 step 5 | Step 5 names the proposal and the built order; ✗ bullet |
| Method 5 Limitations (reconstruction → factorization) | Step 6 dates the result to the thesis [S032 p. 100], restated 2020 [S029 p. 25], confirmed 2025 [S050 p. 10]; the old Limitations clause and the ✗ bullet removed (review fixes) |
| Method 5 Limitations (no reliable recovery) | Limitations dated ("until boosting (2025)"); ✗ bullet |
| Method 5 step 6 | Step 6 credits the thesis [S032 p. 85] |
| Blind spots; Inner Tensions (significance testing) | Roundtable Card blind spots, Inner Tensions, Workflow D step 2 (long form), Honest Boundary *claimed but unverified* |
| Common Misreading 4 (bylines) | Misreading 4 rewritten; the Attribution paragraph no longer relies on bylines |
| Research Integrity (AI use) | Corrected by the operator's hand edit (2026-11-28), which no kit stage may make (the section is byte-identical by rule, `check_ledger.py`): the sentence now names the co-authored 2026 preprint that discloses AI-tool use with author verification [S078 arXiv p. 27] |
| Honest Boundary; Field boundary (decomposition) | Field boundary rewritten |
| Field boundary (MINLP to 2017) | Field boundary rewritten |
| Roundtable Card, Lübbecke contrast | `LCCP26` dropped |
| Research Trajectory (proof logging) | Trajectory 2020–2025 line rewritten |
| Latest (14 unsolved instances) | Cites [LCCP26; S085 p. 1] |
| Signature Work Anatomy, iterative refinement | Anatomy rewritten on the report versions and the thesis |
| Attribution (PaPILO) | Attribution qualified [S004 p. 83] |
| Honest Boundary, Not read | List rewritten (08 §11) |

Two further corrections came from the operator's notes and the cards rather than from 08 §3.2 alone: the Method 1 dating (practised in 2012 [S020 TR pp. 5, 9], 08 §2) and the CHAP wording in the Latest list.

### T3.6 long form of the SKILL.md list

One line each; detail in the [ledger](#corrections).

- Latest: CHAP's first place rests on the competition page; the paper reports no ranking [S076 pp. 1–2, 9].
- Method 3: the edge from VIPR's future work to delta debugging is inferred; MIP-DD names its own origin [S065 pp. 1–2, 13].
- Method 2 step 4: the quoted sentence is on printed p. 809 [S022 p. 17].
- Heuristic 6: four questions in the journal status update, three in its IPCO version [S022 p. 8; D002 p. 8].
- Methods 3 and 4: certificate overheads by version, IPCO +101.2%/+51.4%, journal +56.3%/+22%/+46% [D002 pp. 13–14; S022 p. 16].
- Method 3 step 5: the printed SoPlex result replaces the talk paraphrase [S022 p. 12].
- Method 6: instance licence CC BY-SA 4.0 [S002 p. 6]; tolerance checks in GMP arithmetic with exact objective values [S002 pp. 22, 42]; five exchanged per the changelog only [S002 pp. 43–44]; MIPcc23's validity check not described in print [S055 p. 7].
- Method 5: boosting built as an outer loop [S050 pp. 5–8]; basis factorization ahead of reconstruction since the thesis [S032 p. 100], restated in 2020 [S029 p. 25]; the no-recovery limit dated to before 2025 [S013 TR p. 23; S050 p. 2]; "check the basis early" first in the thesis [S032 p. 85].
- Method 1: the count of a field belief dates from 2012, not 2014 [S020 TR pp. 5, 9]; step 5 cites the page [S072 p. 9].
- Significance tests exist after 2015: to 2018 in component studies, in 2021 on MIPLIB's hardness claim [S011 pp. 16, 21; S006 p. 20; S002 pp. 40–41].
- Common Misreading 4: byline order is no reliable signal of his role [S011 pp. 1, 3; S019 p. 3].
- Research Integrity Rules (kept verbatim by rule): a co-authored 2026 preprint discloses AI-tool use with author verification [S078 arXiv p. 27].
- Field boundary: decomposition in co-authored application work [S041 pp. 3, 14–16; S085 pp. 1–3]; MINLP work as supervisor to 2025 [S070 pp. 21–22].
- Roundtable Card: LCCP26 dropped from the Lübbecke contrast [S085 pp. 17–19]; a Fischetti counter-note added [S004 p. 42].
- Trajectory: Learn to relax holds no proof log and starts the Nordström collaboration [S024 pp. 6, 15; D006 pp. 1–2].
- Attribution: one credited PaPILO feature, jointly with Hoen [S004 p. 83].
- Iterative-refinement anatomy: its numbers come from the journal report and the thesis, not from ISSAC [S013 TR pp. 19–20; S020 TR pp. 9–10].
- How to Use: proofs for mixed-precision LP algorithms are in scope (Method 7) [S029 pp. 8–17].

### T3.6 review fixes (2026-11-28)

- The SKILL.md list was compressed to six lines grouped by kind (review: bookkeeping), and the ✗ bullets inside Methods 1–7 were removed, so each contradiction is marked once.
- New or corrected entries: the factorization result dated to the thesis [S032 p. 100] (review: the T3.6 line said *since 2020*); Method 3 step 7's open items as SCIP 10 prints them [S021 pp. 7, 9, 11] (review: *symmetry in exact mode* is not on S021 pp. 9–11); Taste 1 and the Roundtable Card named beside Method 6 (review).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> - Latest: CHAP's first place rests on the competition page, not the paper [S076 pp. 1–2, 9].
> - Method 3: VIPR → delta debugging inferred [S065 pp. 1–2, 13]; step 5 and overheads from print [S022 pp. 12, 16].
> - Method 2 step 4 page [S022 p. 17]; Heuristic 6 count [S022 p. 8].
> - Method 6: licence, tolerance checks, "five", MIPcc23 validity [S002 pp. 6, 22, 43–44; S055 p. 7].
> - Method 5: boosting outer loop, factorization since 2020, early basis check in the thesis [S050 pp. 5–8; S029 p. 25; S032 p. 85].
> - Method 1 from 2012 [S020 TR pp. 5, 9]; significance tests to 2018 and in 2021 [S011 p. 16; S002 pp. 40–41].
> - Bylines [S011 pp. 1, 3]; PaPILO credit [S004 p. 83]; no proof log in Learn to relax [S024 pp. 6, 15].
> - Research Integrity Rules: the AI-use sentence now names the co-authored disclosure [S078 arXiv p. 27] (operator's hand edit, 2026-11-28).
> - Field boundary [S041 pp. 3, 14–16; S070 pp. 21–22]; Roundtable Card contrasts [S085 pp. 17–19; S004 p. 42].


<a id="rejected"></a>

## Rejected and held-back updates

### Considered and not promoted (08 §4.2, copied)

| Cluster | Cards (studies) | Checks passed | Failed check | Decision |
|---|---|---|---|---|
| Attribution runs: name the mechanism behind a gain or loss, run the control that removes or forces it, print the null, restate the claim | S034, S022, S074, S070, S072, S064, S085 (7) | recurrence, say–do (Taste 2 is stated in the thesis), executable | exclusivity: controlled testing is the field's stated ideal, cited from Hooker in the thesis | Method 1 variant (step 8) and Taste 2 practice; no new item |
| Check and report in the original model; translate tolerances back | S001, S017, S010, S015, S037, S045, S052, S002, S003, S006 (10 cards, 10 works) | recurrence, say–do, executable | exclusivity not shown; overlaps Method 4 step 4 and Method 6 step 3 | Heuristic HA (§5) |
| Harvest what the solver already computed (H9 as a method) | S039, S011, S018, S034, S003, S043 (6 cards, 5 studies) | recurrence, say–do, executable | exclusivity: priority for the dual one-row observation is conceded to Tawarmalani and Sahinidis [S011 pp. 7, 9]; mostly MINLP | stays Heuristic 9, now with read sources |
| Determinism by design, with its price measured | S026, S005, S004, S078, S007 (5 cards, 3 studies) | recurrence, say–do, executable | exclusivity not shown by the cards | extension of Heuristic 10 |
| Presolve serves its consumer | S033, S068, S078, S004, S031, S022, S038 (7 cards, 6 studies) | recurrence, say–do, executable | exclusivity not shown; mostly group voice | Heuristic HB (§5) |
| Re-derive a technique as an instance of a host-field family, then generalise | S047, S063, S044, S062, S080 (5 cards, 4 studies) | recurrence, executable | say–do (no own statement), exclusivity (general mathematical practice); outside the skill's scope | technique inventory (§7) |

---

### Candidate pool (08 §6, copied)

| Cluster | Cards | Why it stays in the pool |
|---|---|---|
| Negative variants and preliminary failures reported in the text | S020, S018, S032, S085 (4) | already Taste 5 and Method 3 step 1 |
| Build MINLP on mature MIP machinery | S035, S075, S030, S054 (4) | SCIP architecture stance of the group, 2010–2013; MINLP belongs to minlp-team; not exclusive |
| Solver-neutral virtual aggregates; bracket a method by extreme versions | S001, S002, S008, S034 (4) | covered by Method 6 step 1 and Warning sign 4 |
| Variability as a measured quantity (seed spread, a metric's own variability, de-tuning priced) | S001, S014, S084, S004, S022 (5; two from the Suite series) | covered by H8 and the Fischetti counter-note |
| Flag arbitrary and intuition-based constants in print | S001, S014 (2) | covered by Method 6 steps 5–6 |
| Behaviour-defined test sets | S001, S020 (2) | covered by Method 1 step 4 and Method 6 |
| Relaxation fed by the tree's data | D007/S083, S063, S044 (3 studies) | MINLP, group; H9 variant |
| Deterministic effort proxy instead of wall-clock time | S012, S024, S080 (3) | folded into H8 (iv) |
| Per-section code-contribution statements | Suite series (8 reports, one series), H002 (2 works) | a documentation convention; used for attribution only (§9) |
| The release ships the measurement instruments | S023, S010, S003 (2 works) | H5 evidence |
| Two-tier evidence in a release report; merge-time numbers | S003, S005 (one series) | H3 and Method 2 step 10 |
| Progress integral for censored runs | S069, S045 (2) | H7 evidence |
| Generic over tailored for a heterogeneous user base | D005, S098, S027 (one consortium) | Taste 8 evidence, consortium voice |
| Counterexample before reusing an algorithm from a neighbouring setting | S012, S080, S081 abstract (2 full) | technique inventory |
| Price-of-exactness attribution | S036, S074 (2) | Method 2 step 4 evidence |
| Shadow-mode instrumentation | S012, S080 (2) | Method 1 step 3 evidence |
| Success-gated execution | S034, S079 (2) | H7 evidence |
| Overhead of certification read against a rival community's certified task | S038, S036 (2) | Method 3 step 4 variant |
| Competition design | S016, S055, S049 (3) | Method 6 step 8 evidence |
| Confidential instances made shareable (artificial twin; reduction as anonymisation) | S073, S065 (2) | two cards |
| Designed instance families | S024, S092, S087, S041 (4) | Method 6 variant |
| Exact or heuristic, stated per reduction | S008, S017, S009 (3) | Method 4 labelling discipline and HA |
| Independent re-implementation in a second solver | S070 (S056 abstract; one study) | one study |
| LP-analogue proxy for an NP-hard structural quantity | S025, S008 (one study) | one study, 2008–2009 |
| Amdahl sequential fraction as the scaling summary | S078, S026 (2) | technique inventory |
| Revive a dormant idea with current machinery | S066 (S051 abstract) | one full card |

**Single-card candidates (41)**, recorded in the technique inventory where useful: pessimistic reporting of one's own tuning parameter [S025 pp. 78–81]; the simplest exact rule as a declared base case [S008 pp. 18–20]; standalone comparison read as complementarity, then the in-solver ablation [S018 pp. 14–17]; timeouts as lower-bound speed-ups [S032 p. 181]; limit-independent effort profiles, a random control arm and exclusions chosen per question [S011 pp. 13, 15, 17–18]; verifying what an unfinished run has proved [S019 p. 9]; redundant annotation of user structure [S046 p. 5]; objectives robust to tiny differences [S053 p. 11]; ablating the working limits [S031 p. 32]; resource-normalised speed-up [S033 pp. 104–105]; valid bounds under incomplete subproblem solves [S041 pp. 16, 18–21]; a theorem that licenses a cheap approximation [S043 pp. 12–14]; algorithm-independent reference points [D003 pp. 5, 7, 9, 12]; validating an instrument against independent labels minus the circular part, and testing the design claim per solver [S002 pp. 37, 40–41]; counters for numerical fallbacks [S004 p. 38]; usage counts as value of constraint types [S024 pp. 22–25]; known theorems as certificate-shrinking cuts [S042 pp. 7–10]; the staircase study, one factor per table [S022 pp. 8–18]; witness-and-order certification and abstract rules with techniques as instances [S060 pp. 2–11]; a theorem's safe parameter against the measured default [S083 pp. 11–12, 16–18]; encoding-length control as a numerical safeguard [S036 pp. 11–15, 23–24]; choosing a certificate encoding by measurement [S038 pp. 14–15]; an ordered-band score [S055 pp. 6–7]; a formulation judged with its separators, and cut classes by separability [S091 pp. 7, 10–11]; a safety whitelist for exact mode [S021 pp. 7–8]; an untrained method against learned baselines [S049 pp. 2, 6]; failures of one project as the next test set [S050 pp. 9, 12–13]; verifying only the decisions that decide correctness [S072 p. 4]; a formulation chosen for numerical safety over relaxation strength [S073 pp. 4–6]; proof-system strength as a design argument [S080 p. 2]; a fixed-choice sweep of a predecessor's heuristic [S082 report pp. 4–8]; relaxed integrality with post-solve repair [S087 pp. 10, 20–22]; a co-author credited with limitations and extensions [H002 p. 13]; the rival's best case built by hand [S078 arXiv pp. 13, 18–20]; rounded-bound agreement as the test of numerical safety, and a weakened setting to expose a component's effect [S085 pp. 13–14, 21].

---

### Rejected updates (08 §10, copied)

1. **Reading notes on single works** (26 cards: counts in the text that differ from a table, percentages computed against the new arm, means carried by few instances, a default chosen on the evaluation set, a headline resting on a near-limit instance). Not findings about the researcher; not used. At most the neutral lesson that counts in prose should be taken from the tables they summarise. Card ids are not listed here on purpose.
2. **Per-section code-contribution statements as a method**: one series of release reports; used only as an attribution source.
3. **Build MINLP on mature MIP machinery** (S035, S075, S030, S054): the group's architecture, outside the MILP field, not exclusive.
4. **The release ships the measurement instruments**, **two-tier evidence in a release report**, **merge-time numbers**: already covered by H3 and H5; one series.
5. **Seed spread as a variability metric**, **deterministic effort proxies**: covered by H8; added there as extensions, not as items.
6. **Progress integral for censored runs**, **success-gated execution**: covered by H7.
7. **Generic over tailored** (one consortium): Taste 8 evidence only.
8. **Solver-neutral virtual aggregates**, **keep instances in the contributor's form**, **flag arbitrary constants**, **behaviour-defined test sets**: covered by Methods 1 and 6.
9. **Shadow-mode instrumentation**: Method 1 step 3 evidence.
10. **Price-of-exactness attribution**: Method 2 step 4 evidence.
11. **Certificate completion outside the checker as a new method**: a step of Method 4.
12. **Negative variants reported in the text**: Taste 5 and Method 3 step 1.
13. **Test the suspected mechanism's remedy and print the null** as a heuristic: a variant of Method 1 (§4.2).
14. **Re-derive as an instance, then generalise**: generic and student-led; technique inventory only.
15. **AI-use disclosure** and **significance-tested ablation** as patterns: single statements that correct SKILL.md (§3.2), not methods.
16. **Material that restates sealed test items** (house rules at the top): not used, whatever its weight.

---

### Decisions of this pass (T3.6)

- **08's two heuristic merges not applied as renumbering.** 08 §5 proposes merging H5 into H4 and H6 with H7 so that HA and HB keep the count at ten. Renumbering would break the routing table, the workflows, the anti-patterns and the FIDELITY record, which cite H4a–c, H5, H6, H7 and H8 by number, and it adds no explanatory power (paper-reading-card.md §3, rule 4). The merges are carried as cross-references instead (Heuristic 4 names H5 as its fourth tool; Heuristic 6 keeps the question-to-metric link to H7 in the long form), and HA and HB became Heuristics 11 and 12. The skill then had twelve heuristics, two above the framework's range of five to ten. *Superseded by the review decision below.*
- **No new workflow.** 08 does not propose one; Method 7's design steps enter Workflow A step 2 and the routing table.
- **Held back (sealed material).** Every passage that restates a sealed validation item stays out of SKILL.md, this ledger and the technique catalog, as in 08 §10 item 16: S048 is cited nowhere, and the held-back passages of S013 and S020 are not used for Method 2 (08 §2, note to the table). No method or heuristic of this pass stands on such material.
- **07 and the cards are not offered to SKILL.md's user.** The generated card index carries one row whose contribution text overlaps a sealed item (a flag raised when 08 was written; the row is generated from a card digest, which this step does not edit); SKILL.md therefore lists `07-paper-cards.md` and `cards/` with the other sealed notes, and every card id it uses resolves in the [card key](#card-key) below instead.
- **Reading notes.** The two pre-synthesis clauses that restated reading notes (Method 2 Limitations; Method 6 step 3) were removed from SKILL.md and are not copied below (08 §3.3); no new ones were added (08 §10 item 1).

### Decisions of the T3.6 review fixes (2026-11-28)

- **Back to ten heuristics without renumbering H1–H10.** HA (Heuristic 11) and HB (Heuristic 12) were folded into steps: HA into Workflow C step 6 and Warning sign 8 (with Method 6 step 3), HB into Heuristic 10 and Method 4 step 1. Reasons: research-extraction-framework.md §3 sets five to ten heuristics; paper-reading-card.md §3 rule 4 rejects additions without explanatory power, and 08 §4.2 records that HA overlaps Method 4 step 4 and Method 6 step 3 and that HB fails exclusivity and is mostly group voice. Their sections stay here under their anchors as folded items.
- **Five anatomies.** The limited-precision-oracle anatomy joined the iterative-refinement anatomy as its theory sequel (framework §5: three to five anatomies; every core method keeps one).
- **Bookkeeping out of SKILL.md.** Card tallies, ✗ errata bullets, the not-read id lists and the prior-snapshot clause moved here; each contradiction is marked once, in SKILL.md's Corrections list.
- **Held back on sealed-material grounds.** The T3.6 reading of the 2012 two-set design [S020 TR p. 9] was removed from the files SKILL.md sends its user to (EP8, 08 §2 and §7.3, the long forms here), because in that form it comes close to a point of a sealed item; the two-set step itself stands on [S019 p. 9; S072 p. 8]. The point is not restated here.
- **Declined in T3.6, then made by the operator's hand edit (2026-11-28)**: the Research Integrity Rules sentence on AI use now names the co-authored disclosure [S078 arXiv p. 27], and the closed-solver line of Activation Rules adds Method 7 with the closed solver as its floating-point oracle (inferred). T3.6 may change neither section (`check_ledger.py`), so the deletion detector reports these two lines, by design. The pattern change in `scripts/check_ledger.py` for source keys is a kit change outside this step; the before/after check of source-key citations was repeated by hand.

<a id="sources"></a>

## Sources appendix

### Changes made in SKILL.md (T3.6)

- A *Deep reading* line points to `papers/INDEX.md`, 08, this ledger and the technique catalog, and names 07 and the cards as sealed (see [Rejected and held-back updates](#rejected)).
- The "(not read)" marks on [ISSAC12], [IR16], [OBBT17] and [CDH20] were removed: all four are read (cards S020 TR, S013 TR, S011, S034). The card behind each source key is listed in the [card key](#card-key).
- The sentence on sealed notes now also names 07 and the cards.

### T3.6 review fixes (2026-11-28)

- `FIDELITY.md` joins the do-not-open list, and the local full texts may be opened only at pages this skill cites (review: the papers' text files hold the sealed pages too).
- [ISSAC12] and [IR16] say which version was read: ZIB-Reports 12-19 and 15-15 [S020 TR; S013 TR] (review: the "(not read)" marks had simply been dropped).
- [LCCP26] author order corrected to Ghannam, Gleixner, Lam, Mexi, as on S085 p. 1 and in works.json (the moved-verbatim copy above keeps the old order).

Removed from or rewritten in SKILL.md by these fixes (the T3.6 text, moved verbatim):

> Linked research notes: [04 mentorship](04-mentorship.md) (`[04 V1]`) and [06 trajectory](06-trajectory.md) (`[06 T8]`). Notes 01, 02, 03, 05 and `holdout.md` contain passages sealed for the Phase 4 test: do not open them (nor 07 and the cards) while this skill is used or validated. Every DOI and arXiv id below was resolved on Crossref, DataCite or the arXiv API on 2026-11-14.
> - [ISSAC12] Gleixner, Steffy, Wolter, ISSAC 2012, DOI 10.1145/2442829.2442858
> - [IR16] Gleixner, Steffy, Wolter, "Iterative Refinement for Linear Programming", DOI 10.1287/ijoc.2016.0692
> - [LCCP24] Ghannam, Mexi, Lam, Gleixner, arXiv 2401.17937; [LCCP26] Ghannam, Gleixner, Mexi, Lam, arXiv 2607.15837


### Before T3.6 (moved verbatim)

Linked research notes: [04 mentorship](04-mentorship.md) (`[04 V1]`) and [06 trajectory](06-trajectory.md) (`[06 T8]`). Notes 01, 02, 03, 05 and `holdout.md` contain passages sealed for the Phase 4 test: do not open them while this skill is used or validated. Every DOI and arXiv id below was resolved on Crossref, DataCite or the arXiv API on 2026-11-14.

**Papers (primary)**

- [Th] Gleixner, *Exact and fast algorithms for mixed-integer nonlinear programming*, PhD thesis, TU Berlin 2015, DOI 10.14279/depositonce-4938
- [ISSAC12] Gleixner, Steffy, Wolter, ISSAC 2012, DOI 10.1145/2442829.2442858 (not read)
- [IR16] Gleixner, Steffy, Wolter, "Iterative Refinement for Linear Programming", DOI 10.1287/ijoc.2016.0692 (not read)
- [LPO20] Gleixner, Steffy, "Linear programming using limited-precision oracles", Math. Program. 183, DOI 10.1007/s10107-019-01444-6
- [VIPR] Cheung, Gleixner, Steffy, "Verifying Integer Programming Results", IPCO 2017, DOI 10.1007/978-3-319-59250-3_13, arXiv 1611.08832
- [M17] Gleixner, Hendel, Gamrath, Achterberg et al., "MIPLIB 2017", Math. Program. Comput. 13 (2021) 443–490, DOI 10.1007/s12532-020-00194-3
- [ZR21-04] Eifler, Gleixner, IPCO 2021, DOI 10.1007/978-3-030-73879-2_12, arXiv 2101.09141
- [SU23] Eifler, Gleixner, "A computational status update for exact rational mixed integer programming", Math. Program. 197 (2023) 793–812, DOI 10.1007/s10107-021-01749-5
- [GMI24] Eifler, Gleixner, "Safe and Verified Gomory Mixed-Integer Cuts …", SIAM J. Optim. 34, DOI 10.1137/23M156046X
- [CPDP24] Borst, Eifler, Gleixner, "Certified Constraint Propagation and Dual Proof Analysis …", arXiv 2403.13567
- [PB25] Eifler, Nicolas-Thouvenin, Gleixner, "Combining Precision Boosting with LP Iterative Refinement …", INFORMS J. Comput. 37, DOI 10.1287/ijoc.2023.0409
- [NC25] Hoen, Gleixner, CPAIOR 2025, DOI 10.1007/978-3-031-95976-9_3, arXiv 2412.14710
- [Chv22] Eifler, Gleixner, Pulaj, ACM TOMS 48, DOI 10.1145/3485630; [Chv-ax] arXiv 1809.01572
- [CP17] Gleixner, Maher, Müller, Pedroso, "Exact Methods for Recursive Circle Packing", arXiv 1702.07799
- [CP21] Sofranac, Gleixner, Pokutta, CP 2021, DOI 10.4230/LIPIcs.CP.2021.52
- [PaPILO] Gleixner, Gottwald, Hoen, INFORMS J. Comput. 35, DOI 10.1287/ijoc.2022.0171
- [MIPDD] Hoen, Kamp, Gleixner, INFORMS J. Comput. 38, DOI 10.1287/ijoc.2024.0844; [MIPDD-ax] arXiv 2405.19770
- [CPB24] Hoen, Oertel, Gleixner, Nordström, CPAIOR 2024, DOI 10.1007/978-3-031-60597-0_20
- [PS23] van Doornmalen, Eifler, Gleixner, Hojny, arXiv 2311.03877
- [L2R21] Devriendt, Gleixner, Nordström, "Learn to relax", Constraints 26, DOI 10.1007/s10601-020-09318-x
- [CC23] Bolusani, Besançon, Gleixner et al., "The MIP Workshop 2023 Computational Competition on reoptimization", Math. Program. Comput. 16, DOI 10.1007/s12532-024-00256-w, arXiv 2311.14834
- [S10] Hojny et al., "The SCIP Optimization Suite 10.0", arXiv 2511.18580
- [LCCP24] Ghannam, Mexi, Lam, Gleixner, arXiv 2401.17937; [LCCP26] Ghannam, Gleixner, Mexi, Lam, arXiv 2607.15837
- [LVB13] Gleixner, Weltge, CPAIOR 2013, DOI 10.1007/978-3-642-38171-3_26; [OBBT17] Gleixner, Berthold, Müller, Weltge, J. Global Optim. 67, DOI 10.1007/s10898-016-0450-4 (not read); [CDH20] Witzig, Gleixner, DOI 10.1287/ijoc.2020.0973 (not read)
- [SAP19] Gleixner et al., arXiv 1908.00796; [DSAP26] arXiv 2603.03498; [CHAP26] arXiv 2605.05086

**Stated methodology (primary)**

- [Sim21] Simons Institute talk, 30 Mar 2021, https://www.youtube.com/watch?v=JMZUJlWfMT8
- [MIP21] MIP Workshop 2021 talk (automatic captions), https://www.youtube.com/watch?v=rKyUcsjXFHs ; abstract https://researchseminars.org/talk/MIP2021/8/
- CO@Work 2024 opening, https://www.youtube.com/watch?v=o2BK_XEGcn4
- [STSM14] "Numerically Robust Integer-Feasibility", COST TD1207 report, 2014, https://cost-td1207.zib.de/sites/default/files/scientific_report_gleixner.pdf
- [COW25] COW 2025 abstract, https://cow25.sciencesconf.org/601453
- [Call16] MIPLIB 2017 call, https://listserv.zib.de/pipermail/opt-net/2016-November/001275.html
- [Dag18] Bonami, Gleixner, Linderoth, Misener (eds.), Dagstuhl Reports 8(2) 2018, §4.2 (group), DOI 10.4230/DagRep.8.2.64
- Homepage, https://www.zib.de/userpage/gleixner/

**Process evidence (primary)**

- [VIPR-gh] https://github.com/scipopt/vipr (PRs #24, #25, #28; issues #26, #27; states checked 2026-11-14)
- [VIPR-orig] https://github.com/ambros-gleixner/VIPR/pull/1 (original repository; PR #1 opened by Eifler, 22 Jul 2022, with Gleixner's review comments of 2–3 Aug 2022; checked 2026-11-19)
- [SCIP-gh] https://github.com/scipopt/scip ; [MRT] https://github.com/scipopt/scip/commit/8201ee1d ; [SCIP-iss] https://github.com/scipopt/scip/issues
- [SoPlex-gh] https://github.com/scipopt/soplex ; MIP-DD code https://github.com/scipopt/MIP-DD
- [CC23-gh] https://github.com/ambros-gleixner/MIPcc23
- [MIPLIB-CL] https://miplib.zib.de/ and https://miplib.zib.de/CHANGELOG.html
- [ML] SCIP mailing list, e.g. https://listserv.zib.de/pipermail/scip/2018-July/003465.html

**Students, collaborators and peers (secondary)**

- Theses (TU Berlin): [Eif25] Eifler 2025, DOI 10.14279/depositonce-23941; [Wit22] Witzig 2022, DOI 10.14279/depositonce-15389; [Hen22] Hendel 2022, DOI 10.14279/depositonce-15958; [Gam20] Gamrath 2020, DOI 10.14279/depositonce-10710; [Mil23] Miltenberger 2023, DOI 10.14279/depositonce-22309; [Mue20] Müller 2020, DOI 10.14279/depositonce-9889
- [Wood23] Wood, Zhou, Wu, Mendes, Pulaj, "Satisfiability Modulo Theories for Verifying MILP Certificates", arXiv 2312.10420
- [CakeML] https://github.com/CakeML/cakeml/tree/master/examples/vipr ; [LeanVIPR] https://github.com/cruisesong7/LeanVIPR
- [IHS26] Ihalainen et al., arXiv 2508.07015
- [Hooker95] Hooker, "Testing heuristics: We have it all wrong", J. Heuristics 1995, DOI 10.1007/BF02430364
- [MGP] https://mathgenealogy.org/id.php?id=206147
- Card papers of other members (DOIs in the card): Achterberg et al. 2020 (presolve); Achterberg, Wunderling 2013; Fischetti, Monaci 2014; Fischetti, Glover, Lodi 2005; Bergner et al. 2015

> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode

<a id="card-key"></a>

## Card key

Every card id cited in SKILL.md, this ledger or the technique catalog: year, short authors (from `works.json`), title (as on the card), the published form (from the card heading), **the file the card read**, deepest read level, batch file in `cards/` and, where SKILL.md has one, its source key. Card pages are pages of that file: for a ZIB-Report, arXiv version or manuscript they are not the published pagination, so cite the published work by its venue and the card page with the version (`ZIB-Report 19-08, p. 17`); where the file is the journal's own PDF, the offset gives the printed page. Abstract- and metadata-level cards are cited by id only. Version words in citations: S001, S013, S017 and S020 are cited as ZIB reports (`TR`), S067 and S078 as arXiv versions, S082 as a report and D005 as a draft (08 §1). S048 is held back and not listed (see [Rejected and held-back updates](#rejected)). Columns added in the T3.6 review fixes (2026-11-28).

| Card | Year | Authors | Title | Published as | File read (card pages are its pages) | Read level | Batch | SKILL.md key |
|---|---|---|---|---|---|---|---|---|
| D001 | 2019 | Gleixner, Steffy | Linear Programming Using Limited-Precision Oracles | IPCO 2019, LNCS 11480, pp. 399-412, DOI 10.1007/978-3-030-17953-3_30 | abstract only (Springer page) | abstract | a2-01 |  |
| D002 | 2021 | Eifler, Gleixner | A Computational Status Update for Exact Rational Mixed Integer Programming | IPCO 2021, DOI 10.1007/978-3-030-73879-2_12; arXiv 2101.09141 | ZIB-Report 21-04 = arXiv 2101.09141v1 | full | c10 | ZR21-04 |
| D003 | 2021 | Sofranac, Gleixner, Pokutta | An Algorithm-Independent Measure of Progress for Linear Constraint Propagation | CP 2021, DOI 10.4230/lipics.cp.2021.52; arXiv 2106.07573 | arXiv 2106.07573v3 | full | c10 | CP21 |
| D004 | 2018 | Gleixner et al. | The SCIP Optimization Suite 6.0 | ZIB-Report 18-26, 2018, no DOI | ZIB-Report 18-26, the report itself | full | s02 |  |
| D005 | 2019 | Breuer et al. | BEAM-ME: Ein interdisziplinärer Beitrag zur Erreichung der Klimaziele | OR News 66, pp. 6-8, 2019, no DOI | submitted draft (DLR elib 128739) | full | a2-01,s3-01 |  |
| D006 | 2020 | Devriendt, Gleixner, Nordström | Learn to Relax: Integrating 0-1 Integer Linear Programming with Pseudo-Boolean Conflict-Driven Search | CPAIOR 2020, LNCS 12296, pp. xxiv–xxvi; no DOI or arXiv id in the work list | the extended abstract in the CPAIOR 2020 front matter | full | s03 |  |
| D007 | 2022 | Bestuzheva, Gleixner, Völker | Strengthening SONC Relaxations with Constraints Derived from Variable Bounds | Proceedings of HUGO 2022, pp. 41–44, 2022, arXiv 2211.05518 | arXiv 2211.05518v1 | full | s04 |  |
| H001 | 2011 | Berthold et al. | On the computational impact of MIQCP solver components | ZIB-Report 11-01 2011, no DOI or arXiv id; urn:nbn:de:0297-zib-11998 | ZIB-Report 11-01, the report itself | full | s01 |  |
| H002 | 2026 | Weber et al. | Boolean Algebra–Driven Sepsis Diagnosis | arXiv preprint 2026, arXiv 2605.29686 | arXiv 2605.29686v1 | full | c18 |  |
| S001 | 2011 | Koch et al. | MIPLIB 2010: mixed integer programming library version 5 | Mathematical Programming Computation 2011, DOI 10.1007/s12532-011-0025-9 | ZIB-Report 10-31 (cited TR) | full | c02 |  |
| S002 | 2021 | Gleixner et al. | MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library | Mathematical Programming Computation 13(3), 443-490, 2021, DOI 10.1007/s12532-020-00194-3 | journal PDF; printed = file + 442 | full | c11 | M17 |
| S003 | 2017 | Gleixner et al. | The SCIP Optimization Suite 5.0 | ZIB-Report 17-61 2017, no DOI or arXiv id; urn:nbn:de:0297-zib-66297 | ZIB-Report 17-61, the report itself | full | c05 |  |
| S004 | 2021 | Bestuzheva et al. | The SCIP optimization suite 8.0 | arXiv preprint 2021, arXiv:2112.08872 | arXiv 2112.08872v1 (also ZIB-Report 21-41) | full | c12 |  |
| S005 | 2020 | Gamrath et al. | The SCIP optimization suite 7.0 | ZIB-Report 20-10 2020, urn:nbn:de:0297-zib-78023; no DOI or arXiv id | ZIB-Report 20-10, the report itself | full | c09 |  |
| S006 | 2018 | Vigerske, Gleixner | SCIP: global optimization of mixed-integer nonlinear programs in a branch-and-cut framework | Optimization Methods and Software 2018, DOI 10.1080/10556788.2017.1335312 | ZIB-Report 16-24, revised May 2017 | full | c08 |  |
| S007 | 2024 | Bolusani et al. | The SCIP optimization suite 9.0 | arXiv preprint 2024, arXiv 2402.17702 | arXiv 2402.17702v2 | full | c14 |  |
| S008 | 2009 | Boland et al. | LP-based disaggregation approaches to solving the open pit mining production scheduling problem with block processing selectivity | Computers & Operations Research 2009, DOI 10.1016/j.cor.2007.12.006 | journal PDF; printed = file + 1063 | full | c02 |  |
| S009 | 2019 | Furini et al. | QPLIB: a library of quadratic programming instances | Mathematical Programming Computation 2019, DOI 10.1007/s12532-018-0147-4 | authors' manuscript (no journal layout) | full | c08 |  |
| S010 | 2016 | Gamrath et al. | The SCIP Optimization Suite 3.2 | ZIB-Report 15-60 2016, no DOI or arXiv id | ZIB-Report 15-60, the report itself | full | c03 |  |
| S011 | 2017 | Gleixner et al. | Three Enhancements for Optimization-Based Bound Tightening | Journal of Global Optimization 2017, DOI 10.1007/s10898-016-0450-4 | ZIB-Report 15-16 | full | c06 | OBBT17 |
| S012 | 2021 | Chmiela et al. | Learning to schedule heuristics in branch and bound | Advances in Neural Information Processing Systems 34, 2021, arXiv 2103.10294 | arXiv 2103.10294v1 | full | c13 |  |
| S013 | 2016 | Gleixner, Steffy, Wolter | Iterative Refinement for Linear Programming | INFORMS Journal on Computing 2016, DOI 10.1287/ijoc.2016.0692 | ZIB-Report 15-15 (cited TR) | full | c04 | IR16 |
| S014 | 2017 | Maher et al. | The SCIP Optimization Suite 4.0 | ZIB-Report 17-12 2017, no DOI or arXiv id | ZIB-Report 17-12, the report itself | full | c07 |  |
| S015 | 2023 | Bestuzheva et al. | Enabling research through the SCIP optimization suite 8.0 | ACM Transactions on Mathematical Software 2023, DOI 10.1145/3585516 | arXiv 2303.07101v1 | full | c14 |  |
| S016 | 2022 | Gasse et al. | The machine learning for combinatorial optimization competition (ml4co): Results and insights | NeurIPS 2021 Competitions and Demonstrations Track, PMLR, 2022, arXiv 2203.02433 | arXiv 2203.02433v2 | full | c13 |  |
| S017 | 2012 | Gleixner et al. | Towards globally optimal operation of water supply networks | Numerical Algebra, Control and Optimization 2012, DOI 10.3934/naco.2012.2.695 | ZIB-Report 12-25 (cited TR) | full | c02 |  |
| S018 | 2014 | Berthold, Gleixner | Undercover: a primal MINLP heuristic exploring a largest sub-MIP | Mathematical Programming A 144(1–2) 2014, DOI 10.1007/s10107-013-0635-2 | ZIB-Report 12-07, revised January 2013 | full | c03 |  |
| S019 | 2017 | Cheung, Gleixner, Steffy | Verifying Integer Programming Results | IPCO 2017, DOI 10.1007/978-3-319-59250-3_13; arXiv 1611.08832 | ZIB-Report 16-58, revised March 2017 = arXiv 1611.08832v2 | full | c07 | VIPR |
| S020 | 2012 | Gleixner, Steffy, Wolter | Improving the accuracy of linear programming solvers with iterative refinement | ISSAC 2012, DOI 10.1145/2442829.2442858 | ZIB-Report 12-19 (cited TR) | full | c02 | ISSAC12 |
| S021 | 2025 | Hojny et al. | The SCIP optimization suite 10.0 | arXiv preprint 2025, arXiv 2511.18580 | arXiv 2511.18580v1 | full | c16 | S10 |
| S022 | 2023 | Eifler, Gleixner | A computational status update for exact rational mixed integer programming | Mathematical Programming 197(2), 793-812, 2023, DOI 10.1007/s10107-021-01749-5 | journal PDF (CC BY; card c3-01); printed = file + 792 | full | a2-01,c3-01 | SU23 |
| S023 | 2012 | Berthold et al. | Solving mixed integer linear and nonlinear problems using the SCIP Optimization Suite | ZIB-Report 12-27 2012, no DOI or arXiv id | ZIB-Report 12-27, the report itself | full | c03 |  |
| S024 | 2021 | Devriendt, Gleixner, Nordström | Learn to relax: Integrating 0-1 integer linear programming with pseudo-Boolean conflict-driven search | Constraints 26(1), 2021, DOI 10.1007/s10601-020-09318-x | 34-page manuscript, not the journal layout | full | c13 | L2R21 |
| S025 | 2008 | Gleixner | Solving large-scale open pit mining production scheduling problems by integer programming | Master's thesis (Diplomarbeit), Technische Universität Berlin 2008, no DOI or arXiv id | the Diplom thesis itself | full | c01 |  |
| S026 | 2023 | Gleixner, Gottwald, Hoen | PaPILO: A Parallel Presolving Library for Integer and Linear Optimization with Multiprecision Support | INFORMS Journal on Computing 2023, DOI 10.1287/ijoc.2022.0171 | arXiv 2206.10709v3 | full | c14 | PaPILO |
| S027 | 2022 | Rehfeldt et al. | A massively parallel interior-point solver for LPs with generalized arrowhead structure, and applications to energy system models | European Journal of Operational Research 2022, DOI 10.1016/j.ejor.2021.06.063 | accepted-version postprint | full | s04 |  |
| S028 | 2012 | Berthold et al. | Analyzing the computational impact of MIQCP solver components | Numerical Algebra, Control and Optimization 2(4) 2012, DOI 10.3934/naco.2012.2.739 | ZIB-Report 13-08 | full | s01 |  |
| S029 | 2020 | Gleixner, Steffy | Linear programming using limited-precision oracles | Mathematical Programming 183 (1) 2020, DOI 10.1007/s10107-019-01444-6; arXiv 1912.12820 | ZIB-Report 19-57 = arXiv 1912.12820v1 | full | c09 | LPO20 |
| S030 | 2012 | Bley et al. | Comparing MIQCP solvers to a specialised algorithm for mine production scheduling | Modeling, Simulation and Optimization of Complex Processes 2012, DOI 10.1007/978-3-642-25707-0_3 | ZIB-Report 09-32 | full | s01 |  |
| S031 | 2020 | Gemander et al. | Two-row and two-column mixed-integer presolve using hashing-based pairing methods | EURO Journal on Computational Optimization 8(3) 2020, DOI 10.1007/s13675-020-00129-6 | journal PDF; printed = file + 204 | full | s03 |  |
| S032 | 2015 | Gleixner | Exact and fast algorithms for mixed-integer nonlinear programming | PhD thesis, Technische Universität Berlin 2015, DOI 10.14279/depositonce-4938 | the thesis (DepositOnce PDF); main text printed = file − 12, front matter in roman numerals | full | b01 | Th |
| S033 | 2020 | Scholz et al. | Speeding up Energy System Models - a Best Practice Guide | BEAM-ME project guide 2020, DLR elib record 135507; no DOI or arXiv | the project guide itself | full | b02 |  |
| S034 | 2021 | Witzig, Gleixner | Conflict-driven heuristics for mixed integer programming | INFORMS Journal on Computing 33(2), 2021, DOI 10.1287/ijoc.2020.0973 | ZIB-Report 19-08 = arXiv 1902.02615v1 | full | c13 | CDH20 |
| S035 | 2010 | Berthold, Gleixner | Undercover – a primal heuristic for MINLP based on sub-MIPs generated by set covering | EWMINLP 2010, pp. 103–112, no DOI or arXiv id | the proceedings chapter | full | s01 |  |
| S036 | 2024 | Eifler, Gleixner | Safe and verified Gomory mixed-integer cuts in a rational mixed-integer program framework | SIAM Journal on Optimization 34(1) 2024, DOI 10.1137/23m156046x; arXiv 2303.12365 | arXiv 2303.12365v3 | full | c15 | GMI24 |
| S037 | 2016 | D'Andreagiovanni, Gleixner | Towards an accurate solution of wireless network design problems | ISCO 2016, DOI 10.1007/978-3-319-45587-7_12; arXiv 1604.00513 | arXiv 1604.00513v2 | full | s02 |  |
| S038 | 2024 | Hoen et al. | Certifying MIP-Based Presolve Reductions for 0-1 Integer Linear Programs | CPAIOR 2024, DOI 10.1007/978-3-031-60597-0_20; arXiv 2401.09277 | arXiv 2401.09277v2 | full | c15 | CPB24 |
| S039 | 2013 | Gleixner, Weltge | Learning and Propagating Lagrangian Variable Bounds for Mixed-Integer Nonlinear Programming | CPAIOR 2013, DOI 10.1007/978-3-642-38171-3_26 | ZIB-Report 13-04 | full | c03 | LVB13 |
| S040 | 2023 | Chmiela et al. | Online learning for scheduling MIP heuristics | CPAIOR 2023, DOI 10.1007/978-3-031-33271-5_8; arXiv 2304.03755 | arXiv 2304.03755v1 | full | s04 |  |
| S041 | 2020 | Gleixner et al. | Price-and-verify: a new algorithm for recursive circle packing using Dantzig–Wolfe decomposition | Annals of Operations Research 2020, DOI 10.1007/s10479-018-3115-5; arXiv 1702.07799 | ZIB-Report 17-07 = arXiv 1702.07799v2 | full | c10 | CP17 |
| S042 | 2022 | Eifler, Gleixner, Pulaj | A safe computational framework for integer programming applied to Chvátal's conjecture | ACM Transactions on Mathematical Software 48(2), 2022, DOI 10.1145/3485630 | arXiv 1809.01572v2 | full | c13 | Chv22 |
| S043 | 2020 | Müller, Serrano, Gleixner | Using two-dimensional projections for stronger separation and propagation of bilinear terms | SIAM Journal on Optimization 30(2) 2020, DOI 10.1137/19m1249825; arXiv 1903.05521 | ZIB-Report 19-15 = arXiv 1903.05521v2 | full | s03 |  |
| S044 | 2023 | Bestuzheva, Gleixner, Vigerske | A computational study of perspective cuts | Mathematical Programming Computation 2023, DOI 10.1007/s12532-023-00246-4; arXiv 2103.09573 | ZIB-Report 21-07 = arXiv 2103.09573v1 | full | s04 |  |
| S045 | 2019 | Gamrath et al. | Tackling industrial-scale supply chain problems by mixed-integer programming | Journal of Computational Mathematics 37 2019, DOI 10.4208/jcm.1905-m2019-0055 | ZIB-Report 16-45, revised March 2019 | full | s02 |  |
| S046 | 2018 | Breuer et al. | Optimizing large-scale linear energy system problems with block diagonal structure by using parallel interior-point methods | Operations Research Proceedings 2017, 2018, DOI 10.1007/978-3-319-89920-6_85 | ZIB-Report 17-75 | full | s02 |  |
| S047 | 2020 | Serrano, Schwarz, Gleixner | On the relation between the extended supporting hyperplane algorithm and Kelley's cutting plane algorithm | Journal of Global Optimization 78(1) 2020, DOI 10.1007/s10898-020-00906-y; arXiv 1905.08157 | ZIB-Report 19-18 = arXiv 1905.08157v1 | full | s03 |  |
| S049 | 2025 | Ghannam, Gleixner | Hybrid genetic search for dynamic vehicle routing with time windows | International Conference on Operations Research, Operations Research Proceedings 2023, LNOR 2025, DOI 10.1007/978-3-031-58405-3_35; arXiv 2307.11800 | arXiv 2307.11800v2 | full | c16 |  |
| S050 | 2025 | Eifler, Nicolas-Thouvenin, Gleixner | Combining precision boosting with LP iterative refinement for exact linear optimization | INFORMS Journal on Computing 37(4) 2025, DOI 10.1287/ijoc.2023.0409; arXiv 2311.08037 | arXiv 2311.08037v1 | full | c16 | PB25 |
| S051 | 2020 | Müller et al. | On generalized surrogate duality in mixed-integer nonlinear programming | IPCO 2020, LNCS 12125, pp. 322-337, DOI 10.1007/978-3-030-45771-6_25 | abstract only (Springer page) | abstract | a2-01 |  |
| S052 | 2016 | Cao, Gleixner, Miltenberger | Methoden zur Reduktion der Rechenzeit linearer Optimierungsmodelle in der Energiewirtschaft-Eine Performance-Analyse | EnInnov 2016: 14. Symposium Energieinnovation, Graz; no DOI | the conference paper itself | full | s02 |  |
| S053 | 2018 | Witzig et al. | Mixed-integer programming for cycle detection in nonreversible Markov processes | Multiscale Modeling & Simulation 16(1) 2018, DOI 10.1137/16m1091162; arXiv 1609.02063 | ZIB-Report 16-39 = arXiv 1609.02063v1 | full | s02 |  |
| S054 | 2013 | Berthold, Gleixner | Undercover Branching | Experimental Algorithms: 12th International Symposium SEA 2013, DOI 10.1007/978-3-642-38527-8_20 | ZIB-Report 13-14 | full | s01 |  |
| S055 | 2024 | Bolusani et al. | The MIP Workshop 2023 Computational Competition on reoptimization | Mathematical Programming Computation 16(2) 2024, DOI 10.1007/s12532-024-00256-w; arXiv 2311.14834 | arXiv 2311.14834v2 | full | c15 | CC23 |
| S056 | 2023 | Bestuzheva, Gleixner, Achterberg | Efficient separation of RLT cuts for implicit and explicit bilinear products | IPCO 2023, LNCS 13904, pp. 14-28, DOI 10.1007/978-3-031-32726-1_2 | abstract only (Springer page) | abstract | a2-01 |  |
| S057 | 2022 | Sofranac, Gleixner, Pokutta | Accelerating domain propagation: An efficient GPU-parallel algorithm over sparse matrices | Parallel Computing 109, article 102874, 2022, DOI 10.1016/j.parco.2021.102874 | abstract only (arXiv preprint) | abstract | a2-01 |  |
| S058 | 2019 | Weber, Sager, Gleixner | Solving quadratic programs to high precision using scaled iterative refinement | Mathematical Programming Computation 11(3) 2019, DOI 10.1007/s12532-019-00154-6; arXiv 1803.07178 | ZIB-Report 18-04 = arXiv 1803.07178v2 | full | s03 |  |
| S060 | 2023 | Doornmalen et al. | A proof system for certifying symmetry and optimality reasoning in integer programming | arXiv preprint 2023, arXiv 2311.03877 | arXiv 2311.03877v2 | full | c14 | PS23 |
| S061 | 2025 | Mexi et al. | Scylla: a matrix-free fix-propagate-and-project heuristic for mixed-integer optimization | International Conference on Operations Research, Operations Research Proceedings 2023, LNOR 2025, DOI 10.1007/978-3-031-58405-3_9; arXiv 2307.03466 | arXiv 2307.03466v2 | full | c16 |  |
| S062 | 2023 | Mexi et al. | Improving conflict analysis in MIP solvers by pseudo-Boolean reasoning | CP 2023, LIPIcs 280, 27:1–27:19, DOI 10.4230/lipics.cp.2023.27; arXiv 2307.14166 | arXiv 2307.14166v1 | full | s04 |  |
| S063 | 2022 | Müller et al. | On generalized surrogate duality in mixed-integer nonlinear programming | Mathematical Programming 2022, DOI 10.1007/s10107-021-01691-6; arXiv 1912.00356 | ZIB-Report 19-55 = arXiv 1912.00356v1 (read in part) | partial | s04 |  |
| S064 | 2019 | Rehfeldt et al. | A massively parallel interior-point solver for linear energy system models with block structure | ZIB-Report 19-41 2019, no DOI or arXiv id in the work list | ZIB-Report 19-41, revised October 2019, the report itself (read in part) | partial | s03 |  |
| S065 | 2026 | Hoen, Kamp, Gleixner | MIP-DD: Delta debugging for mixed-integer programming solvers | INFORMS Journal on Computing 38(2), 414–423, 2026, DOI 10.1287/ijoc.2024.0844; arXiv 2405.19770 | arXiv 2405.19770v5 | full | c18 | MIPDD |
| S066 | 2012 | Gleixner | Factorization and update of a reduced basis matrix for the revised simplex method | ZIB-Report 12-36 2012, no DOI or arXiv id | ZIB-Report 12-36, the report itself | full | s01 |  |
| S067 | 2020 | Sofranac, Gleixner, Pokutta | Accelerating domain propagation: An efficient gpu-parallel algorithm over sparse matrices | 2020 IEEE/ACM 10th Workshop on Irregular Applications: Architectures and Algorithms (IA3) 2020, DOI 10.1109/ia351965.2020.00007; arXiv 2009.07785 | arXiv 2009.07785v5 (extended version; cited arXiv) | full | s03 |  |
| S068 | 2020 | Gleixner et al. | First experiments with structure-aware presolving for a parallel interior-point method | Operations Research Proceedings 2019, 2020, DOI 10.1007/978-3-030-48439-2_13; arXiv 1908.00796 | ZIB-Report 19-39 = arXiv 1908.00796v1 | full | c10 | SAP19 |
| S069 | 2018 | Georges et al. | Feature-based algorithm selection for mixed integer programming | ZIB-Report 18-17, Zuse Institute Berlin 2018, no DOI | ZIB-Report 18-17, the report itself | full | s02 |  |
| S070 | 2025 | Bestuzheva, Gleixner, Achterberg | Efficient separation of RLT cuts for implicit and explicit bilinear terms | Mathematical Programming 210(1) 2025, DOI 10.1007/s10107-024-02104-0; arXiv 2211.13545 | arXiv 2211.13545v3 (extended version) | full | c17 |  |
| S071 | 2012 | Berthold et al. | SCIP Optimization Suite を利用した混合整数 (線形/非線形) 計画問題の解法 | 24th RAMP Symposium 2012, pp. 165–192, no DOI or arXiv id | ZIB-Report 12-24 (Japanese) | full | s01 |  |
| S072 | 2025 | Hoen, Gleixner | Analyzing the numerical correctness of branch-and-bound decisions for mixed-integer programming | CPAIOR 2025, DOI 10.1007/978-3-031-95976-9_3; arXiv 2412.14710 | arXiv 2412.14710v3 | full | c17 | NC25 |
| S073 | 2025 | Halbig et al. | A diving heuristic for mixed-integer problems with unbounded semi-continuous variables | EURO Journal on Computational Optimization 13, 100107, 2025, DOI 10.1016/j.ejco.2025.100107; arXiv 2403.19411 | arXiv 2403.19411v2 | full | c17 |  |
| S074 | 2024 | Borst, Eifler, Gleixner | Certified Constraint Propagation and Dual Proof Analysis in a Numerically Exact MIP Solver | arXiv preprint 2024, arXiv 2403.13567 | arXiv 2403.13567v1 | full | c15 | CPDP24 |
| S075 | 2010 | Berthold et al. | Extending SCIP for solving MIQCPs | EWMINLP 2010, pp. 181–196, no DOI or arXiv id | the proceedings chapter | full | s01 |  |
| S076 | 2026 | Tjusila et al. | CHAP: A Hybrid GPU-CPU Heuristic for MIP | arXiv preprint 2026, arXiv 2605.05086 | arXiv 2605.05086v1 | full | c18 | CHAP26 |
| S077 | 2022 | Sofranac, Gleixner, Pokutta | An algorithm-independent measure of progress for linear constraint propagation | Constraints 27(4), 432-455, 2022, DOI 10.1007/s10601-022-09338-9 | abstract only (arXiv preprint) | abstract | a2-01 |  |
| S078 | 2026 | Kempke et al. | Distributed Parallel Structure-Aware Presolving for Arrowhead Linear Programs | arXiv preprint 2026, arXiv 2603.03498 | arXiv 2603.03498v2 (cited arXiv) | full | c19 | DSAP26 |
| S079 | 2025 | Holly-Ponientzietz et al. | Clique Probing for Mixed-Integer Programs | arXiv preprint 2025, arXiv 2512.17551 | arXiv 2512.17551v2 | full | c17 |  |
| S080 | 2025 | Mexi et al. | Cut-based conflict analysis in mixed integer programming | INFORMS Journal on Computing 2025, DOI 10.1287/ijoc.2024.0999; arXiv 2410.15110 | arXiv 2410.15110v2 | full | c17 |  |
| S081 | 2025 | Runnwerth, Ghannam, Gleixner | Investigating Round-Up Properties for the Length-Constrained Cycle Partition Problem | Operations Research Proceedings 2024, LNOR, pp. 193-198, 2025, DOI 10.1007/978-3-031-92575-7_27 | abstract only (Springer page) | abstract | a2-01 |  |
| S082 | 2025 | Ebert et al. | Sorting criteria for line-based periodic timetabling heuristics | Operations Research Proceedings 2024, Lecture Notes in Operations Research, pp. 348–354, 2025, DOI 10.1007/978-3-031-92575-7_50 | ZIB-Report 24-07 (cited report) | full | c18 |  |
| S083 | 2023 | Bestuzheva, Völker, Gleixner | Strengthening SONC relaxations with constraints derived from variable bounds | arXiv preprint 2023, arXiv 2304.12145; ZIB-Report 23-03 | arXiv 2304.12145v1 | full | s05 |  |
| S084 | 2018 | Bonami et al. | Designing and implementing algorithms for mixed-integer nonlinear optimization (Dagstuhl Seminar 18081) | Dagstuhl Reports 2018, DOI 10.4230/DagRep.8.2.64 | the Dagstuhl Reports PDF; printed = file + 63 | full | c08 | Dag18 |
| S085 | 2026 | Ghannam et al. | A Numerically-safe Branch-Price-and-Cut Algorithm for the Length-Constrained Cycle Partition Problem | arXiv preprint 2026, arXiv 2607.15837 | arXiv 2607.15837v1 | full | c19 | LCCP26 |
| S087 | 2025 | Dionísio et al. | Branch and price for nonlinear production-maintenance scheduling in complex machinery | arXiv preprint 2025, arXiv 2511.07143 | arXiv 2511.07143v1 | full | c18 |  |
| S088 | 2025 | Anders et al. | Based on Joint Work With... | no venue, 2025, no DOI | metadata only | metadata | a2-01 |  |
| S091 | 2024 | Eifler, Witzig, Gleixner | Branch and Cut for Partitioning a Graph into a Cycle of Clusters | ISCO 2024, DOI 10.1007/978-3-031-60924-4_8; arXiv 2401.08412 | arXiv 2401.08412v1 | full | c15 |  |
| S092 | 2024 | Ghannam et al. | Branch and price for the length-constrained cycle partition problem | arXiv preprint 2024, arXiv 2401.17937 | arXiv 2401.17937v2 | full | c16 | LCCP24 |
| S096 | 2022 | Besançon et al. | SCIP8: rethinking nonlinear constraint representation and recent progress | ROADEF 2022, HAL hal-03595412 | HAL hal-03595412v1 | full | s04 |  |
| S098 | 2020 | Fuchs et al. | Realisierung von Beschleunigungsstrategien der anwendungsorientierten Mathematik und Informatik für optimierende Energiesystemmodelle | BEAM-ME-Abschlussbericht, DLR 2020, DOI 10.2314/kxp:1700331485 | the final project report itself | full | s04 |  |
| S099 | 2020 | Breuer et al. | BEAM-ME: Accelerating Linear Energy Systems Models by a Massively Parallel Interior Point Method | NIC Symposium 2020, NIC Series 50, pp. 345-352, 2020; no DOI, handle 2128/24557 | metadata only | metadata | a2-01 |  |
| S101 | 2018 | Gleixner et al. | Mathematical Optimization at the 5th International Conference on Mathematical Software, 11-14 July 2016, Berlin, Germany Preface | Optimization Methods & Software 33(3), p. 419, 2018, DOI 10.1080/10556788.2018.1459255 | metadata only | metadata | a2-01 |  |
