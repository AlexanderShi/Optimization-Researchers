# Holdout: Marco E. Lübbecke

- **Researcher**: Marco E. Lübbecke (RWTH Aachen University, Chair of Operations Research; GERAD). ORCID 0000-0002-2635-0522; DBLP pid 24/5951.
- **Date**: 2026-11-14
- **Rule**: Sealed until the validation is done: this is test material, not evidence. It must not appear in the Phase 2 record, in SKILL.md or among the Phase 4 exam's questions. To unseal an item after a validation, move it under a heading '## Unsealed (<date>)' at the end of this file.
- **Status when picked**: no `SKILL.md` existed for this member, so the items were picked before the synthesis. Notes 01–06 and `00-prior.md` were read; none of the items below is stated in `00-prior.md`.
- **How the points were taken**: from the source itself, not from the notes' summary. Each source was opened on 2026-11-14 in the copy the research agents had downloaded on 2026-11-08 (scratch folder `milp-team-t1-scratch/base-skills/marco-e-lubbecke/`); the public URL or identifier is given with each item. Quotes are verbatim; PDF line breaks and hyphenation are joined. German quotes are followed by an English rendering marked [translation].
- **Spread**: 2001 (thesis, sole author), 2016 (blog comment thread, own voice), 2020 (code commit, own), 2020 (editorial, two authors), 2026 (preprint, four authors).

| Id | Year | Kind | Topic |
|---|---|---|---|
| H1 | 2001 | decision | integer solutions in the thesis code: how far to go beyond the root node |
| H2 | 2020 | decision | what the solver's landing page may claim, and which papers stay on its list |
| H3 (unsealed) | 2016 | decision (answering critics) | central or decentral planning, after readers push back on a blog post |
| H4 | 2026 | decision | NP-hard separation of a constraint family in a branch-and-price algorithm |
| H5 (unsealed) | 2020 | decision | publisher, access model and review model of a new journal |

---

## H1

**Source.** M. E. Lübbecke, *Engine Scheduling by Column Generation*, Dr. rer. nat. thesis, TU Braunschweig, 2001 (sole author). DOI 10.24355/dbbs.084-200511080100-720; DNB archive copy https://d-nb.info/962821152/34. Section 4.3 "Price-and-Branch" (printed p. 116); Section 5.3, "Discussion of Results" (about printed p. 127–128); Section 7.3 "Limitations and Perspectives" (printed p. 157). Opened as `01/papers/thesis_2001.txt` (text of the DNB PDF).

**Question.** In 2001 you are finishing a doctoral thesis on scheduling switching engines at industrial in-plant railroads. Your set-partitioning model is solved by column generation with an exact pricing algorithm. The planners need integer schedules, and nothing guarantees that the columns generated for the LP relaxation contain a good integer solution, or any at all. You could build a full branch-and-price code (columns generated at every node, with branching rules the pricing algorithm can respect), solve only the final restricted master as an integer program, or fall back on a heuristic. What do you do, how do you justify it, and what do you tell the reader about the risk?

**What they actually said or did.**
1. He generates columns at the root only and then runs branch-and-bound on the restricted master: "The column generation process is not invoked at any node other than the root node of the branch-and-bound tree. This policy may be termed price-and-branch by analogy with the folklore notion cut-and-branch" (p. 116). The implementation chapter calls it a "price-and-branch heuristic" (Algorithm 5.1).
2. The justification is what the runs showed, not a guarantee: the experiments indicate "that the restricted master program happen to be already integer feasible, and the solution quality is acceptable" (p. 116); "all final restricted master programs are integer feasible when default options are used", with quality "practically satisfactory, although occasionally significantly above ten percent from optimum" (Section 5.3).
3. He reads this as a general lesson and marks its weakness himself: "reality is not as bad as suggested by computational complexity"; "Although not being a mathematically satisfactory explanation this is an encouragement to attack practical problems even in the presence of negative complexity results." (p. 116)
4. He names the safeguard a production system would need: "in a failsafe industrial implementation one should safeguard against infeasibilities by including a branch-and-price code as emergency reserve", and that code could also run "by default if there is time left until the scheduling decision is due" to improve the solution (p. 116).
5. He lists the omission among the thesis's limits ("A fair discussion of our work must exhibit its limits as well.") and sketches the missing piece: "We did not further consider branch-and-price algorithms. From a practical point of view this is well justified by our obtaining always (even optimal) integer solutions. Theoretically, compatibility of branching rules poses a problem. One proposal is to branch by forcing/forbidding certain pattern structures, e.g., particular sequences of nodes." (p. 157)

**Why this one.** A real fork in his own sole-authored text, with the reason given and the risk priced. A reader who knows the thesis gets it; a good researcher who does not will most likely recommend branch-and-price or answer in general terms, and will not name the "emergency reserve" or the empirical basis. It is a side decision of the thesis, not the survey chapter that made it known.

**Where it appears in the notes.**
- `01-publications.md` §3, item 3 ("Directions the thesis left out", S16 pp. 116, 157): the first four sentences (no branch-and-price; restricted master integer on the data; fail-safe reserve). Leave these out.
- `01-publications.md` §4, row CM5: the thesis half of its evidence ("S16 pp. 116, 153–158"). Leave the p. 116 part out; the other evidence of that row is not sealed.
- `05-peer-critique.md` §1, first bullet (the zbMATH review's description of the method as price-and-branch). Leave out.
- Overlap that is **not** sealed, because it comes from another source (the 2021 podcast): `02-methodology.md` §4.11 second bullet and §8 row "PhD, late 1990s", and `06-trajectory.md` T2 "Tooling of the time" (he did column generation only and never branched, for fear of writing tree management). If the synthesis keeps these, point 1 is partly known to the skill and the podcast gives a different reason; a grader should then weigh points 2–5.
- Not sealed: other sentences of thesis p. 157 that the notes use (customization and tailoring; `01` SW2 "Origin", C2).

---

## H2

**Source.** GCG repository, https://github.com/scipopt/gcg, commit `e21f41cc04caf7e8266da896d8db5225a04cbd18`, author Marco Lübbecke, 2020-10-09, file `doc/index.html.in` (38 insertions, 70 deletions). Context commits on the same file: `97f19a93` (2020-09-23) and `0cfab354` (2020-09-24) by a group member, `a49c11ea` (2020-09-25) by Lübbecke. Opened in the local clone `03/repo/gcg` with `git show` and `git log -S`.

**Question.** In autumn 2020 the landing page of your group's solver GCG has just been reworked, by a doctoral researcher of the group and by yourself. It is now headed "Decomposition for everyone!". Under two pictures of a coefficient matrix, labelled "before detection" and "after detection", a sentence says that whatever type of problem you give it, GCG will try to decompose it efficiently to solve it quicker. A list introduced as papers "known to have used GCG" has grown by about 25 entries in one day. Two weeks later you go over the page again. What do you change, what do you leave, and why?

**What they actually said or did.**
1. He edits the page himself in one commit. The claim under the pictures goes: the sentence "no matter what type of problem you give it, GCG will try to decompose it efficiently to solve it quicker" (added by the group member on 2020-09-23) is replaced by "An essential feature of GCG is its ability to detect decomposable model structure in MIPs. The figures above show an example MIP coefficient matrix, before and after structure detection."
2. He takes back his own headline: "Decomposition for everyone!", which he had put there himself on 2020-09-25 (`a49c11ea`), becomes "Welcome!" again. The captions become "Non-zero entries in original matrix" and "Non-zero entries after re-arrangement".
3. The list is pruned by one criterion, stated in the commit message: "not all papers that cite GCG or Gamrath (2010) actually *use* GCG; these are removed from the list now". Eight entries added the day the list grew are deleted, among them "Price-and-verify: a new algorithm for recursive circle packing using Dantzig-Wolfe decomposition" and "Could we use a million cores to solve an integer program?" (my count of linked entries in the file: 31 before, 23 after). The introduction changes from "GCG has already been used for many projects. Below, you can find some papers that are known to have used GCG." to "Here is a list of papers that use GCG or describe parts of its functionality."
4. He applies the pruning to his own group as well: the entries for Bergner et al., "Automatic Dantzig-Wolfe reformulation of mixed integer programs" (Mathematical Programming 2015, of which he is a co-author) and for a doctoral thesis from his chair are commented out, and so is the block "Projects at RWTH that use GCG", with the comment "for the moment, let us not refer to these projects".
5. What he keeps, and sharpens, is the claim about access rather than speed: "No user interaction is necessary, thus GCG provides decomposition-based MIP solving technology to everyone."

**Why this one.** A small editorial decision in a commit log, with the reason in his own words and a detail no summary predicts: he removes his own headline and his own group's entries, and keeps the "to everyone" claim. Someone who knows how he edits public text will cut the speed claim and separate using from citing; a good researcher without that knowledge will typically tone down wording and leave the list alone.

**Where it appears in the notes.**
- `03-process-evidence.md` §3, items 1 and 2 ("Overclaims are cut from public text"; "Citing is not the same as using"). Leave out.
- `03-process-evidence.md` §8, table rows 4 and 6: the phrases "Landing-page overclaim cut; paper list pruned" and "He rewrote a student's landing-page claims within 16 days". Leave these phrases out; the rest of the rows is not sealed.
- `03-process-evidence.md` Contradictions, item 3: its first sentence quotes the landing-page text of this commit. Leave that sentence out; the other two sources of the item are not sealed.
- `03-process-evidence.md` §4, item 2: the words "and the paper list".
- `06-trajectory.md`: "Sibling notes" bullet on commit e21f41cc; T13, bullet "a correction to the list of papers that use GCG"; §6, item 11; §9, Layer 5, second bullet. Leave out.

---

## H4

**Source.** F. Ciccarelli, F. Furini, C. Hojny, M. Lübbecke, "Branch-and-price strikes back for the k-vertex cut problem", arXiv:2602.04984v2 (2026-06-05), Section 3.1.4 (p. 20) and Appendix F (pp. 38–41, Proposition 6, Table F.1). Four authors with Lübbecke last; the code is the first author's (Zenodo DOI 10.5281/zenodo.17897865), so the decision is the team's. Unreviewed preprint. Opened as `01/papers/arxiv_2602.04984.txt` (text of the v2 PDF).

**Question.** In 2026 you and three co-authors are finishing a branch-and-price algorithm for the k-vertex cut problem. Your extended formulation contains clique-partitioning constraints. You add only those belonging to an initial family of cliques that covers every edge, which is enough for a valid model. The remaining ones, exponentially many, could be separated to tighten the LP bound, but you can prove that the separation problem is NP-hard. What do you do about these constraints, in the algorithm and in the paper, and why?

**What they actually said or did.**
1. They build the stronger variant first, only to measure the ceiling: "we also implemented a branch-and-price-and-cut algorithm in which the clique partitioning constraints (10d) are separated exactly at the root node", in order "to benchmark the best bound that can be obtained" from the formulation (p. 20). Separation is done by an integer program ("We therefore suggest to solve the separation problem by means of integer programming", App. F).
2. The measurement: violated cuts are found at the root on 47 of 304 instances (8.5 cuts on average, at most 44). On these the average root gap falls from 26.4% to 24.6%, while the average root LP time rises from 0.9 to 16.1 seconds (Table F.1 and text, pp. 40–41). The bound from the initial family is "in most cases almost indistinguishable from that obtained with exact separation at the root" (p. 20).
3. They also check the whole run, not only the root: the variant "does not lead to any noticeable advantage" in total time or nodes, and on the 28 of the 47 instances left unsolved the final gap is slightly worse (29.08% against 28.88%) (p. 41).
4. The decision: "our final algorithm therefore does not include the exact separation of clique partitioning constraints and relies exclusively on the inequalities" of the initial family, because the separation problem is NP-hard "and adds a computational overhead" (p. 20). Their verdict: "the exact separation of clique-partitioning inequalities at the root node is not an effective strategy" (p. 41).
5. The discarded variant stays in the paper: Appendix F gives the NP-hardness proof (Proposition 6), the separation model and the comparison table.

**Why this one.** A design choice with a fork, decided by a purpose-built experiment and reported although the component was dropped. A reader who knows the group's way of working predicts "build it to see the best possible bound, measure the cost on full runs, drop it, and print the negative result"; a good researcher without that knowledge tends to propose heuristic separation or to keep the cuts because they strengthen the bound.

**Where it appears in the notes.**
- `03-process-evidence.md` §6, table row "Exact separation of clique-partitioning constraints implemented as a branch-price-and-cut variant ...". Leave out.
- `03-process-evidence.md` §7, table row "2022–2026", last phrase "components measured and then dropped". Leave that phrase out.
- Not sealed: every other use of this preprint in the notes (baselines re-run, ablations, LP solver choice, symmetry handling, abstract v1 against v2, Appendix G).

## Unsealed (2026-11-14)

Moved here on 2026-11-14, before the skill was built, at the user's decision: H3 (a blog comment thread on central versus decentral planning) and H5 (a journal's publisher and review model) are not research decisions of the kind the test needs. The synthesis did not use them; they are no longer test material and may be used as evidence.

### H3

**Source.** M. Lübbecke, blog *café opt*, post "#industrie40: zentral oder dezentral?", 2016-03-02, https://mluebbecke.wordpress.com/2016/03/02/industrie40-zentral-oder-dezentral/, and his four replies in its comment thread (WordPress.com public API, comment ids 117, 120, 122 and 124; 2016-03-03 11:15, 2016-03-04 08:57 and 09:25, 2016-03-08 14:24). Opened as `blog/posts.txt` and `blog/comments.txt` (API text). The other commenters are private persons and are not named here.

**Question.** In March 2016 you publish a blog post on "Industrie 4.0". With hospital appointment scheduling and car navigation as examples you argue for central planning, and you conclude that "decentralisation" is either something you have not understood or plain nonsense for tomorrow's production. Within two days readers from industry reply: a central planner cannot react in real time, the connection to it can fail, so subsystems must be able to act on their own; one of them proposes central planning plus local re-planning. How do you answer, and what do you propose yourself?

**What they actually said or did.**
1. He concedes at once and names his own exaggeration: "Vielen Dank, dass Du meine Überspitzung zu einer differenzierten Darstellung verknetest." [translation: Thank you for kneading my exaggeration into a differentiated account.] He finds the compromise "sehr sinnvoll" and "sogar für mathematisch/algorithmisch spannend" [translation: very sensible; even exciting mathematically and algorithmically] (comment 117).
2. He agrees on the mix and adds that the mix must itself be flexible: "Bei Deinem Fazit (Mix global/lokal) sind wir uns einig, der Mix selbst muss wohl auch flexibel sein, wenn die Möglichkeit gegeben ist, wird globale Information verwendet; und sonst lokal nachgesteuert." [translation: On your conclusion (a global/local mix) we agree; the mix itself must be flexible: where possible global information is used, otherwise one adjusts locally.] (comment 122)
3. He does not rest on robust central plans: plans can be laid out robustly, "da gibt es aber noch wenig praktisch Verwertbares" [translation: but there is little of practical use there yet] (comment 120).
4. His own proposal: give each vehicle an algorithm, not a route. "jedes Fahrzeug bekommt keine individuelle Route, sondern einen kleinen, schnellen, individuellen Algorithmus mit, der unter den "dezentral beobachteten Umständen" die Fortsetzung der Route berechnet" [translation: each vehicle gets no individual route but a small, fast, individual algorithm that computes the continuation of the route under the circumstances observed decentrally]. Local errors are unavoidable, but the set of algorithms is designed together: "Die individuellen Algorithmen wurden also koordiniert so erstellt, dass sie – wenn sie dann jeweils lokal entscheiden müssen – weniger Staus produzieren. Vielleicht hilft hier die Spieltheorie?" [translation: the individual algorithms are created in a coordinated way so that, when each must decide locally, they produce fewer jams. Perhaps game theory helps here?] (comments 120, 122)
5. His criterion for what is decided where, and the price of scale: "Je größer das zu planende/optimierende System, desto größer das Potenzial, aber natürlich auch: desto größer die Zerbrechlichkeit der Lösung." It will depend on "Durchführbarkeit/Robustheit/Echtzeitfähigkeit" which decisions are taken centrally and which decentrally. [translation: the larger the system planned or optimized, the larger the potential, but also the more fragile the solution; feasibility, robustness and real-time capability will decide.] (comment 124)

**Why this one.** It shows how he answers critics on a claim he had put bluntly: he concedes the overstatement, then turns the objection into a research idea of his own (centrally designed, locally executed algorithms). A reader who knows him expects the concession and the turn to an algorithmic question; a good researcher who does not will either defend central optimization or agree to a hybrid without the "algorithm instead of route" idea.

**Where it appears in the notes.**
- `02-methodology.md` §8, table row "2016" ("Retracted in part ..."). Leave out.
- `02-methodology.md` §0, last line ("Below threshold but recurring ..."): the item "decentralised vs central planning (S11 and its comments, 2016)". Leave out.
- `02-methodology.md` Sources, S12: the comments of 2016-03-03 and 2016-03-04 cited for this exchange.
- Not sealed (the post itself, which the question states): `02-methodology.md` C7, second sentence; `06-trajectory.md` T9, "two German posts on Industry 4.0", and §6 item 8, third bullet.

### H5

**Source.** M. Lübbecke, P. M. Pardalos, "Welcome to SN Operations Research Forum!", SN Operations Research Forum 1 (2020) 1, DOI 10.1007/s43069-020-0001-1 (CC BY 4.0; published 2020-02-05), pp. 2–3: the paragraphs on open access, on publication speed and on the choice of publisher. Two authors; his voice cannot be separated. Opened as `dl_orf2020/orf.txt` (text of the publisher PDF).

**Question.** In 2020 you and a co-editor launch a new operations research journal. Its stated purpose is to respond to the way research is now shared: software, data, blogs, preprints, fast feedback. Three design choices are open. Do you run it with a traditional publisher or as a fully open outlet run by the community? Is it open access? Do you keep classical anonymous peer review, or go for something faster such as post-publication review? What do you choose on each, and why?

**What they actually said or did.**
1. A traditional publisher, chosen after weighing the alternative: "we were discussing alternatives that are fully open and that are run entirely by the community. We believe in both." (p. 3)
2. The reason is archival, and the limit is stated as their own: "future generations need to be able to access the knowledge and experience we produce today. At the moment, we lack the imagination that this can totally be accomplished decentrally, given the increasing diversity of formats." Hence "the publishing (r)evolution is possible, maybe even necessary, from within the current system, not entirely replacing it" (p. 3).
3. Not open access, and said plainly: "The OR Forum is not an open access journal. Maybe it will become one, but currently, we have a hybrid format". The mitigations offered are free access to the content of the first two years and a sharing feature for in-browser reading; they concede that "all this does not make the research results entirely free" (pp. 2–3).
4. Review stays classical: "We start the journal with (only) a classical, anonymous peer-review process." "We will not trade speed for quality." Speed is sought after acceptance instead: "We assign every accepted contribution directly to an issue" (p. 3).
5. Post-publication review is deferred, with its cost named: it "could increase publication speed even more, but will face us with discussions about how to define and ensure quality" (p. 3).

**Why this one.** A set of forks where his later public statements (publicly funded research should be freely accessible; code and data should be published) suggest the opposite choice on two of the three. Someone who knows the editorial answers "inside the system, hybrid, classical review, and here is why"; a good researcher guessing from his values will say community-run and open access. The answer therefore tests whether a respondent tracks what he did, not what his slogans imply.

**Where it appears in the notes.**
- `02-methodology.md` §7.5, second bullet ("We will not trade speed for quality."; the "(r)evolution ... from within the current system" quote). Leave out.
- Not sealed, because they use other parts of the same editorial (p. 2: formats invited, data and code policy, pre-registration): `02-methodology.md` §0 row R10 (joint support), §1.5 second bullet, §4.9 second bullet; `06-trajectory.md` T12 "Operations Research Forum" bullets and §4, last table row. If the synthesis describes the journal, it should not state its publisher, access or review model.
