# Marco E. Lübbecke · 02 Stated methodology (what he says research should be)

| Field | Value |
|---|---|
| Researcher | Marco E. Lübbecke (also Marco Lübbecke, M. E. Lübbecke). Professor and chair of operations research, RWTH Aachen University (since 2010); GERAD associate member (since December 2018). PhD TU Braunschweig 2001 (advisor Uwe Zimmermann), habilitation TU Berlin 2007, visiting professor TU Darmstadt 2009–10 (GERAD profile, S18). He has no middle name: he chose the initial "E." for the copyright form of his first paper (book, S28, p. vi, third-person author portrait). |
| Dimension | Research agent 02 of 06: stated methodology. These are his claims about how research should be done, sorted into the seven layers of `references/research-extraction-framework.md` §一. Whether he practises them is agent 03's job. |
| Research date | 2026-11-08 |
| Sources consulted | 46. Of these, 37 were opened and used: 29 primary (27 in his own single voice, 2 co-authored texts), 1 group text (GCG documentation), 6 secondary or observed accounts and 1 bundle of bibliographic metadata (Crossref, OpenAlex, Unpaywall, arXiv). 9 more could not be reached (see Gaps). WebSearch: 2 of the 5 allowed. Everything else came from curl, WebFetch, the WordPress.com, Bluesky and Mastodon public APIs, and the YouTube web player in a browser. |
| Local corpus | `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep`, so there was no user-supplied material. `private/` was not opened. |
| Saved this run | Four caption files under `references/sources/talks/` (each with a provenance header and a SHA-256 of its body): the *Subject to* podcast interview (2021, full, auto-captions), the TEDxRWTHAachen talk (2018, full, auto-captions), the RWTH teaching-award video (2023, full) and three excerpts of the CO@Work 2020 lecture. They are third-party material: keep them local and do not commit them. |

## Reading guide

**Tags.**

| Tag | Meaning |
|---|---|
| [stated] | His own single voice: blog posts and his blog comments, social-media posts, his talk words (captions), his talk abstracts and slides, his signed comment in TOP, first-person profile texts. |
| [stated-joint] | Co-authored text (the Branch-and-Price book with Desrosiers, Desaulniers and Gauthier; the 2020 OR Forum editorial with Pardalos). His individual voice cannot be separated. |
| [stated, self-report] | His own account of something he did. Agent 03 should check it against the record. |
| [stated-group] | Text of the RWTH group (GCG documentation); author not attributed. |
| [observed] | Somebody else's statement about him (podcast host, event organisers, students, colleagues in a thread). |
| [inferred] | This agent's reading. |
| P / S | Primary / secondary. |

**How quotes were checked.**
- Blog posts, pages and comments came from the WordPress.com public REST API (`public-api.wordpress.com/rest/v1.1/sites/mluebbecke.wordpress.com`), so the text is exactly what he published (with later edits; the API gives a modification date).
- Bluesky: all 343 of his own posts (2024-11-15 to 2026-11-07, reposts excluded) were read in full; thread context was fetched for the posts quoted as replies.
- Mastodon (mas.to/@mluebbecke): 282 statuses were retrieved (boosts excluded; the account reports 669 statuses in all). Those from 2022 were read in full; those from 2023–2026 were screened by keyword. Treat the Mastodon counts below as lower bounds.
- Talk captions: the *Subject to* and TEDx captions are YouTube auto-captions (ASR). The *Subject to* text is all lower case and has mis-hearings (a list is in the file header). Quotes from it keep the ASR wording, so they are verbatim for the captions, not certified for the audio.
- German quotes are given in the original with an English rendering marked [translation].
- Every quoted string was checked against the saved or downloaded text with a script (whitespace normalised; PDF line breaks and hyphenation joined) before this file was finished.

---

## A. Source corpus and its era and resource context

| ID | Source | Date | Voice | Era / resource context |
|---|---|---|---|---|
| S01–S11 | Blog *café opt — mathematical optimization in academia and industry* (mluebbecke.wordpress.com): About page, Me page and 9 posts (list in Sources) | 2014-09-29 to 2016-03-02 (About edited 2018-05-26) | [stated] P | RWTH chair, 4–6 years into the post; written for practitioners (German posts) and for the OR community (English). He stopped after March 2016; in 2021 he said "the blog is probably unread by people" (S20, 1:01:39). |
| S12 | His 21 comments on his own blog | 2014-11-01 to 2016-06-14 (one in 2024) | [stated] P | As S01–S11. |
| S13 | M. E. Lübbecke, "Comments on: An overview of curriculum-based course timetabling", TOP 23 (2015) 359–361, DOI 10.1007/s11750-015-0364-1 (read in full) | 2015-03-19 | [stated] P | Invited discussion of a survey; draws on his own timetabling work with G. Lach (RWTH course timetabling). |
| S14 | OR2017 Berlin semi-plenary abstract "Optimization meets Machine Learning" (wiwiss.fu-berlin.de) | 2017 | [stated] P (abstract on the organiser's page) | Early RWTH ML-for-MIP work. |
| S15 | ORBEL 31 keynote abstract "Branch-and-Price" (orbel.be/orbel31) | 2017 (year on the page) | [stated] P | GCG; he is listed as INFORMS Vice President for Information Technology. |
| S16 | TEDxRWTHAachen talk "Anything you can do I can do better" (YouTube Dc38La-Xvog; TED.com) | recorded 2018-06-09, published 2019-02-27 | [stated] P | Public lecture for a general audience. |
| S17 | RWTH Business School, "Meet your professors \| Prof. Dr. Marco Lübbecke" (Q&A, first person) | 2018-11-28 | [stated] P (published by the school) | Teaching in the M.Sc. Data Analytics & Decision Science (DDS). |
| S18 | GERAD profile, biography in the first person (gerad.ca/en/people/marco-lubbecke) | undated; written between Dec 2018 and 2024, probably 2020–21 ("exactly 20 years ago" after his 2001 PhD) [inferred] | [stated] P | GERAD associate member. |
| S19 | CO@Work 2020 decomposition-day lecture (YouTube vx2LNKx48vY, channel "Mixed Integer Programming"); three caption excerpts read and saved | uploaded 2020-09-23 | [stated] P | CO@Work summer school (ZIB), 2020. A recorded lecture: he says "stay safe" and will link literature "in the comments of the video", so an online edition [inferred]. Demos with SCIP and GCG. |
| S20 | *Subject to* podcast, "Subject to: Marco Lübbecke" (host Anand Subramanian; YouTube JzWAAvryTKA), full auto-transcript | 2021-09-23 | [stated] P (host's description: [observed] S) | Career interview recorded around his 50th birthday. He teaches "two thousand students every year" in "at least five courses" (0:56:43). |
| S21 | Slides, "Die Qual der Wahl — wieso wir in Entscheidungssituationen mehr Fantasie brauchen", RWTH WiWi Network Research Talk #6 (107-page PDF) | 2021-09-22 | [stated] P (some pages are students' project slides; noted where quoted) | Covers a 2008/09 coil-coating project, a 2020/21 student project (laser powder bed fusion) and the 2012– political districting project. |
| S22 | RWTH video "RWTH verleiht Lehrpreis 2022 an Marco Lübbecke" (YouTube LZLMijusUhg), German captions | 2023-03-08 | his part [stated] P; students [observed] S | RWTH teaching award 2022. |
| S23 | Slides, "Branch-and-Price Crash Course", CO@Work 2024 (ZIB), 180-page PDF | 2024-09-19 | [stated] P | Summer-school tutorial. |
| S24 | Keynote abstract "A Dantzig-Wolfe Hierarchy for the Stable Set Problem" (maastrichtuniversity.nl PDF, created 2025-01-08); that it belongs to his opening keynote at the joint Belgian–Dutch OR conference of 29 Jan 2025 is inferred from his posts of 2025-01-29/30 | 2025-01 | [stated] P | Joint work with Bastubbe, Gallus and Witt. |
| S25 | PRIME colloquium abstract "(Who wants) Political Re-Districting in Germany (?)", Paderborn University | 2025-07-01 | [stated] P | Districting decision-support tool. |
| S26 | Bluesky @mluebbecke.bsky.social: 343 own posts and replies | 2024-11-15 to 2026-11-07 | [stated] P | Account created 2024-02-06; profile: "I like mathematical optimization in theory and practice". On 2025-02-06 he wrote "ich hatte mehr als zwei Jahre Twitter Abstinenz" [translation: I had more than two years of Twitter abstinence]. |
| S27 | Mastodon @mluebbecke@mas.to: 282 statuses | 2022-11-06 to 2026-09-06 | [stated] P | Account created 2022-10-31. Includes live posts from the Column Generation 2023 workshop and Aussois 2024. |
| S28 | J. Desrosiers, M. Lübbecke, G. Desaulniers, J. B. Gauthier, *Branch-and-Price*, Les Cahiers du GERAD G-2024-36 (revised January 2026; PDF dated January 6, 2026), also Springer 2026, DOI 10.1007/978-3-031-96917-1. Read: Foreword (by F. Soumis), Preface, About the authors, §7.5 "Acceleration techniques", "Beginner's guide to an implementation", Chapter 8, solutions 1.2 | 2024–2026 | [stated-joint] P; Foreword [observed] S | Four authors, open access. The preface says no line of the book was generated by a large language model. |
| S29 | M. Lübbecke, P. M. Pardalos, "Welcome to SN Operations Research Forum!", SN Operations Research Forum 1 (2020) 1, DOI 10.1007/s43069-020-0001-1 (CC BY, read in full) | 2020-02-05 | [stated-joint] P | Founding editorial of the journal he co-founded. |
| S30 | GCG repository docs (github.com/scipopt/gcg, master): README.md, doc/resources/users/why-gcg.md, doc/resources/devs/howtouse/diverse-testset-generation.md | fetched 2026-11-08 | [stated-group] P | Group text; no author named. |
| S31–S36 | Observed accounts: *Subject to* video description and chapter list (S31); TEDx/TED.com descriptions and talk metadata (S32); WiWi Network event summary of S21 (S33); RWTH description of S22 and the students' statements in it (S34); GERAD news items (teaching award 2023, book 2026) (S35); other people's posts in the Bluesky threads quoted below, and the image attached to his post of 2024-12-04 (S36) | 2019–2026 | [observed] S | — |
| S37 | Bibliographic metadata used to verify identifiers: Crossref, OpenAlex (author A5082694588 via ORCID), Unpaywall, arXiv API, DataCite | fetched 2026-11-08 | metadata | — |

---

## 0. Claims repeated three or more times (the real beliefs)

Counts are of separate occasions (a post, a talk, an interview, a page). Repetitions inside one source count once unless noted. [stated-joint] occurrences are listed but not counted toward the threshold.

| # | Belief (faithful summary, not a quote) | Single-voice occurrences (date, source) | Count | Joint / observed support |
|---|---|---|---|---|
| R1 | Data, analyses and predictions do not decide anything; optimization (prescriptive analytics) turns them into decisions. In his words, "machine learning is predicting the past". | 2014-11-04 S05 ("Data is useless per se, even when big"); 2014-11-05 S12 ("collect less data, or collect "good" data only"); 2015-12-16 S10 ("Daten sind noch keine Erkenntnisse. Selbst Erkenntnisse sind noch keine Entscheidungen."); 2016-01-05 S12 (optimization needs data that normally is not collected); 2017 S14 (ML is "rather on the predictive than on the prescriptive side"); 2018 S16 ("machine learning is predicting the past"); 2018-11-28 S17 ("predictions do not automatically lead to good decisions"); 2021-09-22 S21 p. 55 ("reproduziert die Vergangenheit"); 2025-07-01 S25 ("More importantly, we offer prescriptive analytics") | 9 | — |
| R2 | His main research programme, by his own account, is detecting and exploiting model structure, and in the end the *semantics* of a model; a general MIP solver sees only a flat matrix. | 2014-11-04 S05 ("Most research topics in my head deal with finding and exploiting structures in mathematical programs."); 2015 S13 ("How can we exploit special problem structures?"); 2017 S15 ("detect exploitable model structure"); c. 2020 S18 ("get hold of model semantics directly from an LP/MPS file"); 2021 S20 0:53:05–0:54:39; 2023-01-02 S27 (structure easier to "detect" for "our decomposition codes"); 2023-05-17 S27 ("decomposable structures in matrices (I love it)"); 2026-10-20 S26 (MIP solvers "see only the "flat" model") | 8 | GCG docs S30 |
| R3 | OR has a communication problem: it is "too complicated", badly marketed and too little taught; the cure is examples, education and low-threshold access. | 2014-11-04 S12 ("marketing problem"); 2015-03-23 S09; 2015-03-24 and 2015-04-04 S12 ("better educate people"); 2015-03-25 S12; 2016-04-28 S12 ("tue Gutes und rede darüber"); 2021 S20 1:10:52; 2025-03-03 S26 ("we are bad at marketing") | 8 | Uchoa's point, which he relays on 2025-09-04 (S26), is [observed] |
| R4 | A claim of optimality must come with proof; provable quality guarantees are what sets mathematical optimization apart. | 2014-10-27 S04; 2014-12-19 S07 ("I am a well known supporter (a.k.a. "fan") of exact optimization"); 2018 S16 ("ask them whether they can prove it"); 2021-09-22 S21 p. 41 ("Gütegarantien (USP der Math. Opt.)") | 4 | — |
| R5 | Whoever writes the objective function holds power and must use it responsibly. Ask which plan is better and why, and separate the truly fixed constraints from habit. The value choices (rules, objective) are not the optimizer's to settle alone; once they are agreed, the optimum under them is transparent. | 2014-10-27 S04 (three modelling questions); 2015 S13 ("apples and oranges" in the objective); 2021-09-22 S21 p. 99; 2026-11-07 S26 ("those who design the objective function are the persons in power") | 4 | — |
| R6 | Writing is part of doing research: it produces ideas and exposes what one does not know; start writing early. | 2014-11-21 S06; 2024-11-20 S26 (the 2014 notes "would still be relevant for me today"); 2025-09-16 S26 (endorses a quoted line: "The role of writing is not to record the results of research, but is the process itself of research.") | 3 | Book preface S28 p. xiii; beginner's guide S28 p. 507 |
| R7 | A conclusion is not a summary. | 2024-10-26 S27; 2026-02-18 S26 ("periodic reminder"); 2026-08-24 S26 | 3 (he himself calls it "periodic") | — |
| R8 | Conferences are for people, more than for talks. | 2015-01-07 S08; 2021 S20 0:34:35; 2026-07-12 S26 ("this is why we go to conferences: people") | 3 | — |
| R9 | Theory and practice belong together; he works across disciplines. | 2014-10-15 S02; 2018-11-28 S17; 2021 S20 0:57:54 (teaching and research "should go hand in hand"); Mastodon and Bluesky profile texts, fetched 2026-11-08 ("in theory and practice"); 2024-12-11 S26 (a ladder from motivation to profit); 2026-05-29 S26 (praises Zimmermann, "who combined theory with practice") | 6 | Book author portrait S28 p. vi |
| R10 | Researchers should publish code and data, and software and data count as research contributions (in journals and in hiring). | 2021 S20 1:13:04–1:13:43; 2022-11-15 S27 (self-report: code archive with README for a 2005 paper); 2023-08-03 S27 (asks whether data are public "so that results can be independently reproduced"); 2024-11-20 S26 ("in particular #orms academics should publish code and data") | 4 | OR Forum editorial S29 p. 2 |
| R11 | Do not write a branch-and-price tree yourself; use a framework, and use a generic solver (GCG) to estimate whether an implementation will pay before investing in one. | 2020 S19 1:35:41–1:36:12; c. 2020 S18; 2021 S20 0:50:06 and 0:52:01; 2024-03-18 S27 (licence barriers block "ok, let us just try") | 4 | Book S28 pp. 494, 509 |
| R12 | Inside exact methods, be heuristic wherever exactness is not needed: do not solve the pricing problem exactly until the end. | 2014-12-19 S07; 2020 S19 1:33:12–1:34:13 (said four times in a row) | 2 sources (2020 talk repeats it as advice no. 1, 2, 3 and 10) | Book S28 §7.5 (multiple columns, etc.) |
| R13 | Research starts from an observed effect and asks *why*; computation suggests what theory must explain. | 2014-11-21 S06 (ask "why" after every sentence); 2021 S20 0:09:50, 0:38:06, 0:45:26; 2024-09-19 S23 p. 136; 2025-01 S24 | 4 | — |
| R14 | Teaching spreads the technology, and students and practitioners test the teacher's claims. | 2014-10-15 S03; 2021 S20 0:57:03–0:58:40; 2021-09-22 S21 p. 87; 2023-03-08 S22; 2025-03-03 S26; 2025-05-22 S26 ("when algorithms are taught, there needs to be coding") | 6 | Students' statements S34 [observed] |
| R15 | Limitations drive creativity. | 2021 S20 (0:06:24, 0:29:26 "the topic of the limitation", 0:36:56) | 1 source, 3 mentions | Book author portrait S28 p. vi ("he still thinks that limitations drive creativity") |

Below threshold but recurring in two sources: decentralised vs central planning (S11 and its comments, 2016); attend a selective workshop once early in a career (S08 2015); PhD advice (S20 2021; S26 2026).

---

## 1. Research taste (what is worth doing, what a good result is)

**1.1 He likes mathematics because errors are decidable.** [stated] P.
- "math everything is clear and when you're good at it you know when you're wrong" (S20, 0:08:29, ASR, 2021). Knowing he was wrong gave him "a sign where i could learn or had to learn more" (0:08:29).
- "sadly, this reminds me of why I love mathematics, where it is crystal clear what is true and what is false" (S26, 2025-01-09).
- Describing OR in 2022: "clean, beautiful, organized, and close to other interesting disciplines" (S27, 2022-11-22).
- Joint, third-person author portrait: he loves "the pure beauty, the perfect organization, the waterproofness" and "the tears of joy in the eyes of practitioners when mathematical optimization helps making their lives easier" (S28, p. vi) [stated-joint].

**1.2 Discrete and linear, by preference.** [stated] P.
- On his first optimization course: "maybe i'm not a continuous guy" (S20, 0:24:11, ASR).
- "tells me again that continuos is overrated, the world is discrete ;)" (S27, 2023-05-18, joking about a talk at Column Generation 2023).
- On whether integer *linear* programming is boring: "i think we are not done with linear yet" and "i will stick there until the end" (S20, 0:54:59–0:55:17, ASR). He also says the nonlinear "fancy stuff" is "too complicated for me" (same place).
- "I liked the times when MIP was MIP #orms" (S26, 2024-11-22), replying to the announcement that the MIP 2025 computational competition is on primal heuristics for MIQCQPs.

**1.3 Problems that need fundamental research, not off-the-shelf solving.** [stated] P.
- "I particularly appreciate problems that cannot be solved "out of the box" but require solid fundamental research." (S02, 2014.)
- "Theory is as appealing as practice, so what better field could I have chosen than operations research?" (S02.)

**1.4 Practical relevance comes in grades.** [stated] P. In a thread on what counts as evidence that "X is applicable to Y" (Sophie Huiberts's summary of an article; [observed] S36), he wrote: "over the years, I tried to distiguish between something like motivation -> applicability -> is it implemented -> they make money from it, as different degrees of how close theoretical considerations are to practice" (S26, 2024-12-11).

**1.5 What counts as a research contribution.** [stated] P.
- On the journal he co-founded: "we are writing software we are sharing repository we are hosting data um we're having technical contributions which are not a theorem" and, on hiring, "who's that guy he only wrote software well only come on that's so valuable so difficult to do" (S20, 1:13:04–1:13:43, ASR, 2021).
- Joint, 2020: the journal invites "failed experiments and wrong paths taken to learn from" and "articles that describe the hurdles of putting operations research in practice" (S29, p. 2) [stated-joint].

**1.6 What he rejects.** [stated] P.
- A machine-learning MIP method tested on randomly generated instances: "simply no. I will not accept this as a serious proposal for solving mixed-integer programs, regardless of whether you compared against gurobi or not" (S26, 2024-12-04). Context [observed] S36: his post shows the experimental-setup paragraph of a paper that generated MILP instances "by referencing the method for random instance generation described in (Qi, Wang, and Shen 2021)". In the thread Mike Trick identified that source as arXiv:2102.09663 (Qi, Wang, Shen, "Smart Feasibility Pump: Reinforcement Learning for (Mixed) Integer Programming", 2021; title checked on arXiv) and observed that its "large" instances have 9 variables and 18 constraints. Lübbecke replied "yes, this is it; and the citing paper is about the "RL-MILP Solver"" (2024-12-05). The citing paper was not identified or read.
- As a referee: "In referee reports, I complain when authors celebrate themselves for repairing something that they themselves previously broke; my request is to just do it right in the first place." (S26, 2025-09-15.)
- "I do not want to see AI generated images in presentations; they are usually not pretty, and - in my opinion - they do not add an epsilon to the content" (S26, 2025-09-04).
- Exaggeration, by his own account: in 2015 he called his first reaction to a 49-city TSP blog post "spontaneous (you may also call it: arrogant)" (S09). In 2021: "i'm also very known for just saying things i might regret later on" (S20, 1:03:50, ASR); he thinks he has a provocative streak, "maybe this is um some kind of in insecurity" (1:04:09). A 2021 slide flags its own provocation: "plakativ, ich weiß, aber wir wollen ja ins Gespräch kommen" [translation: blunt, I know, but we want to start a conversation] (S21, p. 61).

**1.7 Machine learning: interested in ML *for* optimization, sceptical of ML *instead of* optimization.** [stated] P (dated items; see Contradictions C3).
- 2015: ML is "an area where I see a lot of interesting stuff to dig into in the future!" (S12, 2015-08-17).
- 2017: "More importantly, we are interested in the reverse direction: where (and how) can machine learning help in improving methods for solving optimization problems and what is it that we can actually learn?" (S14.)
- c. 2020: "we make use of learning techniques to improve optimization algorithms. For example, we worked on learning when to apply branch-and-cut vs. branch-and-price." (S18.) The work referred to is presumably Kruber, Lübbecke, Parmentier, "Learning When to Use a Decomposition", CPAIOR 2017, LNCS, pp. 202–210, DOI 10.1007/978-3-319-59776-8_16 [inferred link; DOI checked on Crossref; paper not read].
- 2018: "machine learning is good for making decisions that are simple and repetitive" (S16, 0:02:10); "mathematical optimization is making best use of the future" (0:11:26).
- 2026: "is there also a stream for discrete optimization without machine learning? #orms" (S26, 2026-02-27, replying to the ISMP 2027 announcement of a "Discrete Optimization with Machine Learning" stream).

---

## 2. Problem choice (where problems come from, why now, when to stop)

**2.1 From partners in practice.** [stated] P.
- Blog About page: "If you think you face an optimization problem in your business or everyday life, get in touch!" (S01.)
- "I have worked on many optimization projects, often cooperations between academia and industry" (S02, 2014); "often in partnership with industry" (S18).
- His first research task (1996) was to turn a one-page, first-stage grant into the full proposal for scheduling locomotives on in-plant railways of chemical and steel plants (S20, 0:25:58–0:27:04, ASR) [stated, self-report].
- 2025 abstract: the districting talk covers "the entire analytics process, from the idea, data gathering, convincing officials, model and algorithm development to implementation and what decision makers have to say about this tool" (S25).
- [observed] S32: the TEDx description says his 20+ years of projects were "always in collaboration with companies or organizations".

**2.2 From teaching.** [stated] P. The districting project "started . . . in Class", with the slide notes "good data exercise" and "isn't this facility location?" (S21, p. 68). Once published, it came back into teaching: "in der Wissenschaft ist immer das erste Mal schwer | heute können (und müssen) unsere Studierenden den Ansatz "nachbauen"" [translation: in science the first time is always hard; today our students can (and must) rebuild the approach] (S21, p. 87).

**2.3 Recognise the classic problem inside the application.** [stated] P.
- Slide on a 2020 student project: "ah! ein Überdeckungsproblem! und Machine Scheduling! | klassische Standardprobleme des OR stecken hier drin" [translation: a covering problem! and machine scheduling! classic standard OR problems are inside] (S21, p. 57).
- "whenever you have to find a best ordering or sequence of actions, there is a TSP somewhere around the corner" (S09, 2015).

**2.4 Pick the question you want settled next, and have an answer about the field.** [stated] P (S05, 2014).
- Asked in job interviews for the greatest recent achievements of the field: "The precise answer is not so important, but you should have one."
- On "What will be the next big thing?": "Being a scientist, my interpretation is: Which major research question would you like to see settled next?" His own answer was structure in mathematical programs (R2).
- On grand challenges, he names opportunity and risk: "if we do not provide what we think are the right answers—operations research replies to the buzz words—someone else will." He then calls on OR to become "the science behind big data, internet of things, industry 4.0, etc."

**2.5 His declared agenda (dated).** [stated] P.
- 2014: structure in mathematical programs (S05).
- 2017: detecting exploitable model structure, and "identify blind spots where more research is needed" (S15).
- 2021: automatic Dantzig-Wolfe reformulation "is maybe the favorite" (S20, 0:52:16). The aim is a "commodity" like branch-and-cut, where "the cutting just happens right without you knowing it" (0:52:33–0:52:50), and to make the technology "more low threshold" (0:53:40). Next: "now i'm interested in the meaning in the semantics so to speak" (0:54:39). His example: "you are trying to model a supply chain application and i see that and i know that there are tricks for supply chain applications and i apply them without telling you" (0:54:26).
- c. 2020: GCG "aims to make the useful Dantzig-Wolfe reformulation available to everyone" (S18).
- 2025: "(in fact, I am more interested in "unstructured")", replying "what is his definition of "structured?"" to a summer-school lecture on structured MINLP (S26, 2025-06-02). See Contradictions C5.
- Joint, 2026: the book's §8.2 lists 25 subjects for "a second book", among them "Machine learning", "Implementation", "History of SCIP" and "Combination of Dantzig-Wolfe and Benders decompositions" (S28, p. 552) [stated-joint].

**2.6 A to-do list of borrowed ideas.** [stated, self-report] P. "ever since Bertsimas talked about optimal trees, this approach was on my todo list -- it seems that I can cross off this item now, good" (S27, 2023-05-18, on a column-generation talk about optimal classification trees).

**2.7 When to stop.** [stated] P. In S06 (2014) he gives "Know when to stop." as advice he got from Sándor Fekete, "but I am not very good at it", and adds: "realistically assess what can be achieved in a reasonable amount of time (unless you are really going for something big, then never give up!)". See C1.

---

## 3. Idea generation

**3.1 Effects first, then explanations.** [stated, self-report] P. On tailing-off in his PhD (late 1990s, CPLEX 3.0): "i was proud that i could see the tailing off" (S20, 0:37:49, ASR). He "plotted that" and confirmed the effect others had described (0:38:06), then "i was instead trying to find out why it occurred" (0:38:06). His "most cited article" came out of that search: "a collection of everything i could find about column generation because we wanted to have answers" (0:38:23). That article is presumably Lübbecke and Desrosiers, "Selected Topics in Column Generation", Operations Research 53(6) (2005) 1007–1023, DOI 10.1287/opre.1050.0234 [inferred identification; metadata checked on Crossref; not read].

**3.2 Ask "why".** [stated] P.
- "this is a question that drives me all the time maybe this why so what why is it so good why is it so bad so why should that be true so why drives me" (S20, 0:09:50, ASR).
- On his Berlin years: "we try to ask answer the the why questions what what what's happening here" (0:45:05–0:45:26, ASR).
- "A good question to ask after every single sentence is "why"?" (S06, 2014, as feedback practice).

**3.3 Computation suggests the theorem.** [stated] P.
- 2024 slides on how much of the integrality gap generic cuts close after a Dantzig-Wolfe reformulation: "attempt of an interpretation: DW reformulation is so strong that generic cutting planes (from original) are already "implied"" and "a formal proof of such results is an open research topic" (S23, PDF p. 136; the experiment is described on p. 133, "details in the Ph.D. thesis by Jonas Witt (2019)").
- 2025 keynote abstract: "We first motivate connecting the two topics by some computational observations about Dantzig-Wolfe reformulations of a classical ("edge") formulation for the stable set problem." Then a characterisation, and "Only recently, we fully understood also the reformulations in between the extremes." (S24.)

**3.4 Writing produces ideas.** [stated] P. "Writing spawns new ideas. One often thinks of results to be "easily transferable to another area" and recognizes the difficulties only when trying to exactly write them down." (S06, 2014.) Joint, 2026: "One of the most rewarding side effects of writing what one knows is that it mercilessly reveals what one does not know." (S28, p. xiii) [stated-joint].

**3.5 Read, and learn a method on a problem you know.** [stated] P.
- "Read, read, read. This is what Martin Skutella once said to me." (S06.)
- To summer-school students: "suggest to take a paper on your favorite problem, you know very well something about it, and then I'm quite sure that someone has tried a branch-and-price approach already. Then you can check that just to learn how it works." For a problem nobody has solved by branch-and-price: "I would look into some similar literature and see how people address that." (S19, 1:32:30–1:32:58.)

**3.6 Model in bigger pieces.** [stated] P.
- Branch-and-price is about "extending your modeling capabilities" and "algorithmically exploiting subproblems that you can solve well" (S23, PDF p. 2, 2024).
- 2020: "we dare to model, well, in different variables maybe we wouldn't have tried before"; "we model in paths not only in arcs, we model in entire matchings not in edges"; this is "only possible, because we have that column generation algorithm available" (S19, 1:37:02–1:37:39).

**3.7 Keep the compact model in view.** [stated] P. "you always have original variables!" and "these are the variables of the pricing problem!" (S23, PDF p. 168), answering "what if I have no original problem/variables?". Joint, 2026: skipping the reformulation and writing master and pricing problems directly "may conceal connections which are "there" anyway, and this knowledge is likely needed in branching and cutting later" (S28, p. 508) [stated-joint].

**3.8 Cross-talk transfer.** [stated, self-report] P. At Aussois 2024, during a talk on network bargaining games: "during the talk I could not help but thinking about branching rules (modify/fix parts of the problem to enforce integrality)" (S27, 2024-01-11). At MIP 2026 he was "totally amazed" that Eisenbrand's approximation of the first Chvátal closure for stable set "closely relates to our Dantzig-Wolfe hierarchy" (S26, 2026-10-20).

**3.9 Scarcity as a source of creativity.** [stated, self-report] P. On his Commodore C64 at 13: "it was so small so limited that you could learn everything about the machine" (S20, 0:06:04, ASR); "working with the limited resources i mean computationally that that also influenced me later on when coding" (0:06:42). Joint, third person: "he still thinks that limitations drive creativity" (S28, p. vi) [stated-joint].

---

## 4. Experiments and execution

**4.1 Modelling with a problem owner: three questions.** [stated] P (S04, 2014, German; [translation] mine).
- Decisions: "Welche Informationen enthält der konkrete Plan, der dem Ausführenden übergeben wird?" [translation: What information does the concrete plan handed to the person executing it contain?]
- Objective: "Wenn ich Ihnen zwei Pläne vorlege, können Sie mir sagen, welcher Plan besser ist und warum?" [translation: If I show you two plans, can you tell me which is better and why?]
- Constraints: "Welche Vorgaben sind also wirklich unverrückbar und welche nur in unseren Köpfen?" [translation: Which requirements are truly fixed, and which exist only in our heads?]
- He adds that some requirements are so self-evident that they are forgotten at first and only show up when the first plans are inspected (paraphrase).

**4.2 Joint beginner's protocol for branch-and-price (book, 2026).** [stated-joint] P (S28, pp. 507–509).
- "Step one is solely on paper. Don't skip this." Write the compact model as "a formal problem description"; "Rigor and a good organization here helps in every step downstream."
- Step two: implement the compact model in any MILP solver and language, and build the pipeline from data to an interpretable output. "Acquiring data can be the most time consuming, most boring or most exciting, maybe the most critical phase of the entire project." This step "also serves as a benchmark".
- Step three: Dantzig-Wolfe reformulate on paper, then write the column-generation loop: "through the implementation (and the debugging!), you understand the theory much better"; "maybe keep it simple first".
- Phase two (true branch-and-price): "use a framework that takes care of managing the branch-and-bound process for you".
- Risk: "We should not hide that even a large investment in an implementation may turn out to be fruitless in the end." Hence "you may wish to have some prediction about a success probability"; this is one motivation of GCG (p. 509).

**4.3 Start basic, then tune against measured weaknesses.** [stated-joint] P. "we rather recommend to start by implementing a basic branch-and-price algorithm (using a framework, see Beginner's guide to an implementation) and run computational experiments to identify the algorithm weaknesses on a representative set of relatively large test instances" (S28, p. 494). The three indicators named are the number of column-generation iterations, RMP time versus pricing time, and the number of branch-and-bound nodes (p. 495).

**4.4 His own advice list (2020).** [stated] P (S19).
- "So number one advice is, do not solve the pricing problem exactly." (1:33:12–1:33:17.) "Number two advice is: avoid solving the pricing problem exactly, and number three is the same, and number ten is the same." (1:33:46.) Exact pricing is needed for the optimality proof, "but when you're lucky only once" (1:34:07–1:34:13).
- With many pricing problems, "don't call all the pricing problems" (1:34:36).
- "monitor the Lagrangian dual bound, you get it for free. So when the duality gap is small just branch" (1:34:42).
- On stabilization, cuts and similar techniques: "So all that may be relevant, but need not be relevant." "in the end only rxperimentation [sic, caption] will tell you, whether it's actually worth trying to do this implementation." GCG gives "intuition" on "whether a fully fledged branch-and-price implementation will pay or not" (1:35:29–1:36:12).
- 2014, on heuristics inside branch-and-bound: "Remember: B&B stays exact, but heuristics help to speed up the search and satisfy the practitioner." (S07.)

**4.5 Data reduction is a modelling decision with a tradeoff.** [stated] P (S07, 2014). "Preprocess your data when it is too big, eliminate what is supportedly highly unlikely to play a role in a good solution, but don't be too strict, for otherwise you may miss good quality solutions." On data collection for Industry 4.0: "Sammeln Sie schlau und richtig, mit einem Ziel vor Augen." [translation: Collect cleverly and correctly, with a goal in view] (S10, 2015.)

**4.6 Deliverables for practitioners.** [stated] P.
- A rule he passes on from Torsten Koch: "never ever deliver to a practitioner a solution to any optimization problem that is not 2-opt" (S07, 2014) [stated, relaying Koch].
- A 2021 slide on the coil-coating project shows "Visualization/Verification of Solutions" with "+ a detailed Excel sheet" (S21, p. 42).

**4.7 Fair comparisons.** [stated] P (S13, TOP 2015, p. 360). "Fair computational comparisons of different approaches are hard to obtain"; settings, machines and time limits "vary significantly between the papers discussed", and "I was wondering how the comparison would be if all approaches were run under identical conditions. This part of the overview needs to be taken with a grain of salt."

**4.8 Test sets.** [stated] P.
- Call for MIPLIB 2024: "do you have very hard (but not "impossibly hard") mixed integer linear programs? please do consider submitting them to the next MIPLIB edition (called "2024"), ideally from a practical application context" (S27, 2024-09-09).
- On diverse test sets: "in the strIPlib, we follow a similar approach", with a link to GCG's guide on generating diverse test sets (S26, 2026-06-16). The guide itself is group text (S30): it builds diverse test sets from strIPlib following Donkiewicz (2021) [stated-group].
- Group text (S30, why-gcg.md): "your problem has to exhibit some kind of structure"; without one, a decomposition "can be detrimental to performance" [stated-group].

**4.9 Reproducibility.** [stated] P and [stated-joint].
- Self-report: asked for the code and instances of a 2005 paper, "I am a bit proud that I could send an answer containing an archive :)", and "I was surprised that it even contained a README :)" (S27, 2022-11-15). The paper is L. Heinrich-Litan, M. E. Lübbecke, "Rectangle Covers Revisited Computationally", LNCS (2005), pp. 55–66, DOI 10.1007/11427186_7 (checked on Crossref).
- Joint, 2020: "this implies making all data publicly available, ideally also the code, in order to help achieve reproducibility of results. If proprietary data cannot be made public, authors should provide additional, synthetic data that support the result in the same way as the original data." (S29, p. 2.) "We welcome suggestions for how pre-registration can be rewardingly interpreted and developed for computational work in operations research." (p. 2.)

**4.10 Show it running.** [stated, self-report] P. His 2020 lecture runs SCIP on the compact model of a cutting-stock instance and then GCG on the same instance, in answer to his own question: "Why is it important to know that there are different ways of formulating one and the same problem into integer programs?" (S19, 0:05:47–0:07:10; these lines come from the keyword search of the full captions and are not in the saved excerpts). A failed classroom demonstration is in §8.

**4.11 Era of his own early practice** [stated, self-report] P (S20, ASR).
- PhD (1996–2001): CPLEX 3.0 through the C interface, "using the column wise encoding of the of the matrix" (0:35:52). The documentation was "the printed manual in the next room" (0:36:06–0:36:22).
- He did column generation only and never branched, because CPLEX gave no tree control and he would have had to write his own tree management (0:36:35).
- "maybe it was buggy so i i would never know" (0:37:15).
- In Berlin (2000s) his group was "probably the first to make use of" the pricing in SCIP (0:51:15). Joint portrait: "part of the first team that ever used SCIP's column generation capabilities (with version 0.81)" (S28, p. vi).

---

## 5. Judging results (when to believe, when to stop, negative results)

**5.1 Distrust results that are too good.** [stated] P (S20, 0:09:03–0:09:50, ASR, 2021).
- "when we find a mistake i'm always kind of happy because then i know there's one less i never assume they're all gone".
- "sometimes there's this feeling something doesn't feel right the the results are too good um the the numbers doesn't feel right there must be something wrong".
- When a bug is found: "that's cool because now we know why".

**5.2 Interpretations stay labelled until proved.** [stated] P. See 3.3: "attempt of an interpretation"; "a formal proof of such results is an open research topic" (S23, 2024).

**5.3 Evidence standards in discussion.** [stated] P.
- "anecdotal evidence does not warrant the use of "often" ;)" (S26, 2024-11-20).
- See 1.4 for his ladder of practical relevance and 1.6 for the rejection of random instances as evidence for MIP solving.

**5.4 Compare with the strongest alternative, heuristics included.** [stated] P. His live summaries of others' talks at Column Generation 2023 (S27, 2023-05-17/18) weigh results against the best competitor:
- "results are good, but do not beat diving heuristics by a large margin at this point";
- "this solves much faster than the "full" duty model, but gives a considerably worse dual bound";
- "they can solve significantly larger instances (200+ objects), but still far away from what heuristics can handle (2000+ objects)".

**5.5 Practice tests the teacher.** [stated] P. Teaching seasoned people at the business school: "they challenged me right and that is good because i always have to find okay is it true what i'm telling them do i really have that experience" (S20, 0:58:26–0:58:40, ASR).

**5.6 Rejection and negative reception.** [stated] P.
- First journal paper: "we immediately got it back desk rejected" (S20, 0:31:10). He was told "it's normal so don't worry we just send it to the next journal" (0:31:28), and it was accepted by Computational Geometry: Theory and Applications. That is Bussieck and Lübbecke, "The vertex set of a 0/1-polytope is strongly P-enumerable", Computational Geometry 11(2) (1998) 103–109, DOI 10.1016/S0925-7721(98)00021-2 [Crossref-checked; identification by journal and his "first paper" remark (S27, 2023-04-23)].
- To juniors presenting at Aussois: "But by all means ignore if they don't like what you do as long as you like what you do. Just push on." (S08, 2015.)

**5.7 Naming his own bias.** [stated] P. "I believe that column generation and branch-and-price is still worthwhile further and deeper investigation, and this overview article supports this, but this perception may be personally biased." (S13, p. 360.)

**5.8 Experimental claims he states as findings** (for agent 03 to check) [stated] P.
- 2020: after a Dantzig-Wolfe reformulation, "empirically from our experiments", the additional cutting planes "from the literature, typically, don't help. Okay, they are typically already satisfied." (S19, 1:03:35–1:03:49.) See C2.
- 2018: over 25 years, hardware got faster "by a factor of 2,000" and solver implementations "by a factor of 2 million" (S16, 0:10:10–0:10:39). These are his figures; their source was not checked here.
- 2021 slide on the 2008/09 coil-coating project: "etwa 30% weniger Leerzeiten ggü. früheren "händischen" Plänen" [translation: about 30% less idle time than the earlier manual plans] (S21, p. 43).

---

## 6. Writing and talks

**6.1 "How to write a paper" (S06, 2014-11-21; blog categories "#phdchat" and "PhD advise").** [stated] P. Written for an early-career doctoral student. In 2024 he re-posted it: "several years back I wrote down some notes on writing a paper; this would still be relevant for me today, if I still wrote papers" (S26, 2024-11-20). The points, in his order:
- Content: "Above all, content matters." "There must be archival value." But start writing before the final results.
- "Writing spawns new ideas." (see 3.4)
- "Read, read, read." (from Skutella)
- "Know when to stop." (from Fekete; "I am not very good at it")
- "Will you regret it?": "Don't write the paper you will wish to have written again (this time "right") in a year from now." He notes that this "somewhat contradicts the previous item".
- "Marketing. Papers may remain unread when not properly sold." "Tell a story."
- "Be honest." "Give credit to others' work, be precise and complete, and stick to supported results, don't even leave room for interpretation."
- "Seek feedback." "Don't take critique personal."
- On how he gives feedback: "I often ask questions and try to "misunderstand as much as I can"", and he asks "why" after every sentence. He suggests sending (extended) abstracts to refereed conferences first to get feedback.
- "Think of your reader." (from Chvátal's book) "Imagine a specific reader".
- "Don't mix up." "When writing about models, don't write about algorithms. When presenting algorithms, don't write about the implementation. Also implementation is different from computations etc."
- "Writing is not linear." "only reading is linear, writing isn't."
- "Start now." "Proved a small result? Don't believe it until you have the nuts and bolts on paper." "Postponing the writing "to the end" is the worst idea you could have."
- Topics he promised for a follow-up post that never came: journal choice, least publishable units, co-authors, self-doubt, procrastination.

**6.2 Conclusions.** [stated] P.
- "short reminder for all academic writers: a summary is not a conclusion" (S27, 2024-10-26).
- "periodic reminder for academic writers: when your "conclusion" summarizes your work, it is a summary, not a conclusion." (S26, 2026-02-18.)
- "I love to see a conclusion (and if there is none, why do we have the paper?)" (S26, 2026-08-24).

**6.3 Talks.** [stated] P.
- "when I take pictures of speakers at a conference I realize how huge the percentage of time is when they talk to the blackboard" (S27, 2023-05-18).
- He praised Stefan Kober's MIP 2026 talk: "I also very much like the visual appearance and slide layout, with pictures on every slide (even a timeline)" (S26, 2026-10-21).
- On AI-generated images, see 1.6.
- At Aussois: "If your presentation contains a flaw someone will find it."; "even if a topic is not interesting to you, you may learn about different presentation styles and didactic approaches" (S08, 2015).
- Structure of his 2021 applied talk: each project story walks through "Project | Problem | Progress | Proofs | Profits" (S21, pp. 4–33).

**6.4 Public communication.** [stated] P (S09, 2015).
- He agrees, reluctantly, with Nathan Brixius that we "may need to simplify" for practitioners: "Jeez, I bit on my tongue, before I wrote that."
- "Bottomline is that we are lousy marketers of our profession if we always insist on this generality and power, even when a little less would do. We scare people away with too much technical detail."
- "Operations research and mathematical optimization needs more marketing, more simple examples, more accessible success stories".
- A blog comment of 2014-11-04: "So, let us all give examples, examples, examples of good OR work" (S12).

**6.5 Book writing (joint).** [stated-joint] P (S28).
- Every chapter has "Good to Know" and "More to Know" sections; "the examples demonstrate how column generation and branch-and-price is lived" (p. xiv).
- "What our book does not contain is a single line, or even only an inspiration generated by some large language model or similar." (p. xv.)
- Exercise 8.2: "Find all mistakes in this book." (p. 553.)
- [observed] S28 Foreword (F. Soumis, p. xii): a standardized notation "will make it easier to write papers that are clear and accessible to a broad community".

---

## 7. Research organisation (supervision, collaboration, agenda, time)

**7.1 Supervision.** [stated] P.
- Feedback style: many colours of ink, questions, "misunderstand as much as I can" (S06).
- His chair held a "Tag der Forschung" (research day) with "20+ three-minute elevator pitches about ongoing thesis projects (B Sc., M Sc., Ph.D.)" (S27, 2024-01-24) [stated, self-report].
- On having children during a PhD: "my experience is still yes of course when if not then" (S20, 0:42:29, ASR). He acknowledges that today's job insecurity "is a serious problem" (0:42:46).
- "if you do the PhD for the money, don't do it" (S26, 2026-07-24, replying to "Does a PhD Pay Off?").
- On a selective workshop: "If you have the opportunity, try to attend at least once during your (early) career" (S08, 2015).
- On where students should publish: "can you imagine that now I ask myself whether I can still recommend my students to send their best works to prestigous journals run by US based organizations?" (S26, 2025-03-03.) The reason he gives: it "may just be beyond their control what can be published or what remains public" (same thread).
- His 2021 slides end with "#IchBinHanna" (S21, p. 105), the German campaign against fixed-term academic contracts. That he backs it is [inferred] from the slide alone.
- The advice he passes on is credited to its sources: Skutella (read), Fekete (know when to stop), Chvátal (think of your reader), Koch (2-opt) (S06, S07).

**7.2 Collaboration.** [stated] P and [stated-joint].
- Desrosiers was the external examiner of his PhD and became his closest professional bond: "he's my perro heir" (ASR, read as *père OR* [inferred from the book dedication]) "so he's my oh our father" (S20, 0:40:13–0:40:33). The book dedication from Marco reads "Für père OR." (S28.)
- Joint: the four authors "had physically exhausting arguments about ways of presentations, assumptions, . . . and they were among the most productive and enlightening events in our research careers" (S28, p. xv).
- Book roles, joint: "Because the project was a bit stalling, Jean Bertrand joined the team"; then "a master coordinator (JD) and three text generators (MEL, GD, and JBG)" (S28, solution 1.2).
- Community: the GERAD bio says he co-organises, with Desrosiers and Desaulniers, "a biannual event (alternating between a school and a workshop) on column generation" (S18).

**7.3 Software as community infrastructure.** [stated] P.
- On SCIP's former academic licence: "it was a pain for everyone and a barrier for people to "ok, let us just try", so finally, these pains outweighed the benefits, I guess" (S27, 2024-03-18).
- "I have been using Gurobi for a decade in teaching now and I wonder whether we, as an academic community, should not rather use our own tools" (S26, 2025-09-09). His students find a callback easier than a SCIP constraint handler (same thread).
- "every other year a new "go-to" build system, package manager, ... a pain for maintainers, teachers, users, dinosaurs like me" (S26, 2025-02-16).

**7.4 Teaching load and its role.** [stated] P.
- "i was told i teach too much also early on several times maybe i teach too much but i love teaching" (S20, 0:56:25, ASR).
- Teaching is a way to "just inform people about about this technology we have" (0:57:03), so that later decision makers "remember there were these weird guys talking about what what was it integer pro" (0:57:23–0:57:34).
- To the 2014 students: he wants them able "die Welt ein bisschen besser zu machen" [translation: to make the world a little better] (S03).
- On the 2022 teaching award: he sees the prize "als Ermutigung an, dass wir das mit Ihnen zusammen experimentieren dürfen" [translation: as encouragement that we may experiment on this together with you] and names serving very different learners as "eine sehr große Herausforderung" (S22, 0:01:26–0:01:53).
- [observed] S34: students praise "die Forschungsnähe": he often discusses scientific publications in class, and the chair runs the tutOR platform for modelling exercises.

**7.5 Publishing system.** [stated] P and [stated-joint].
- "when public money is spent to finance the research+reviewing, then the results should be freely accessible to the public." (S26, 2024-11-20.)
- Joint, 2020: "We will not trade speed for quality." (S29, p. 3.) They believe the publishing "(r)evolution is possible, maybe even necessary, from within the current system" (p. 3).

**7.6 Social media as service.** [stated] P. Twitter "could be my way of paying back so i got information from twitter so why not giving information to twitter" (S20, 1:00:44–1:01:00, ASR). In 2022, on Mastodon: "on twitter I was looking for attention, here it feels like I can just be" (S27, 2022-11-18).

**7.7 His current role, self-described.** [stated, self-report] P. "...if I still wrote papers" (S26, 2024-11-20). Agent 03 should check this against his recent co-authorships.

**7.8 Luck and contingency.** [stated] P.
- On the Aachen chair, offered after five others declined: "i know and i appreciate that i was lucky" (S20, 0:49:28, ASR).
- Joint portrait: "Also because of persistence, support, privilege, coincidence, and luck, Marco can live his passion (and pass it on)." (S28, p. vi.)
- His career moves looked like walls avoided "by inches", with "no plan b" (S20, 0:46:59–0:47:10).

---

## 8. Failures, rejections, abandoned directions and retracted claims (as he states them)

| Date of event | What | Source |
|---|---|---|
| c. 1991–92 [inferred from his last Diplom exam "25 years ago" in 2021, S20 0:24:42] | Not admitted to the subject he applied for in Braunschweig (ASR "the chefs informatics", read as Wirtschaftsinformatik [inferred]); enrolled in mathematics from a brochure. Later admitted from the waiting list, he stayed with mathematics. "that was maybe the first thing that did go wrong in my life" | S20 0:15:39–0:16:39 (ASR); S27 2022-11-22; S28 p. vi |
| 1990s | First journal submission desk-rejected; then accepted by Computational Geometry (1998) | S20 0:31:10–0:32:05 |
| PhD, late 1990s | Did column generation only, never branch-and-price, for fear of writing his own tree management; could do nothing against tailing-off and instability; his code "maybe it was buggy" | S20 0:36:35–0:38:53 |
| 2001 | Applied for assistant professorships in the US and Canada and got only rejections: "i had no credentials as you would say so why would they hire me" | S20 0:43:22–0:44:13 (ASR); S28 p. vi |
| 2009 | Berlin contract ending with "no plan b"; a two-year Darmstadt position came via a chance meeting in an elevator at ISMP 2009 | S20 0:45:44–0:47:31 |
| 2010 | Aachen offered him the chair as candidate "number six" | S20 0:48:23–0:49:12 |
| 2001–2023 | Book first mentioned in a 2001 email, writing started 2015, published 2024/2026: "we were very optimistic about the duration of such a project" (joint); "these were, also emotionally, tough eight years" (his own) | S28 p. xiii; S27 2023-05-17 |
| 2014 | Admits he is "not very good at" knowing when to stop | S06 |
| 2014–2016 | Blog abandoned after 9 posts; promised follow-up posts on writing and on applied research were not written; 2021: "the blog is probably unread by people" | S06; S11; S20 1:01:39 |
| 2016 | Retracted in part: the post concluded that "Dezentralisierung" in Industry 4.0 is "schlicht und ergreifend Unsinn" [translation: plain nonsense] or misunderstood by him. In the comments he called the post "meine Überspitzung" [translation: my exaggeration], agreed on a global/local mix ("Bei Deinem Fazit (Mix global/lokal) sind wir uns einig") and sketched coordinated small local algorithms per vehicle | S11; S12 2016-03-03, 2016-03-04 |
| 2022 | A classroom experiment meant to show "that an obj function cut does not help" helped on that instance: "now we have TWO counterexamples!!" | S27 2022-11-18 |
| 2021 | "i'm also very known for just saying things i might regret later on" | S20 1:03:50 |

---

## Contradictions (kept, not reconciled)

**C1. Stop early, or never give up?** In one post (S06, 2014) he advises "Know when to stop" and to assess realistically what can be achieved, adds "(unless you are really going for something big, then never give up!)", and then gives "Will you regret it?" (do not write a paper you will want to rewrite), noting himself "I did not claim my thoughts would follow any logic". In S08 (2015) he tells juniors to ignore those who do not like their work and "Just push on."

**C2. Do cuts help after a Dantzig-Wolfe reformulation?**
- 2020 (S19, 1:03:35–1:03:49): the additional cutting planes "from the literature, typically, don't help", being "typically already satisfied".
- 2024 (S23, PDF p. 136): generic cuts from the original variables seem "implied", but "still, in practice, adding (problem specific) cuts appears to be indispensable for a good performance".
- Whether "from the literature" in 2020 included problem-specific cuts is not clear from the captions.

**C3. Machine learning.** He calls ML a field with "a lot of interesting stuff to dig into" (2015) and works on learning *for* MIP (S14 2017; S18 c. 2020). He also frames ML as "predicting the past" (S16 2018; S21 2021), rejects an RL-based MIP proposal tested on random instances (S26 2024-12-04), and asks for a discrete-optimization stream "without machine learning" (S26 2026-02-27). These may be two attitudes to two things (ML inside optimization versus ML replacing it) [inferred]. The sources do not say so explicitly.

**C4. LLMs and the teaching of modelling.**
- 2022-12-04 (S27): modelling exam questions "require quite some creativity and/or intelligence"; an LLM able to do them is a day "I do not believe that this day is anywhere near."
- 2025-06-10 (S26): "do LLMs make us optimization professors obsolete, and/or the material we teach? this is a question (and consequences for teaching and learning), many of us are contemplating these days".
- 2026 (S28, joint): the book contains no LLM-generated line, "And we are proud of that."

**C5. Structure versus "unstructured".** Exploiting model structure is his declared programme (R2). In 2025 he wrote "(in fact, I am more interested in "unstructured")" (S26, 2025-06-02). A reading consistent with GCG's aim (finding structure in MIPs that are not known to be structured) is possible but [inferred]; he did not explain.

**C6. Riding the buzzwords versus stepping back from them.** In 2014 he urged the community to "establish operations research as the science behind big data, internet of things, industry 4.0, etc." (S05). In 2025–26 he posts doubts about AI hype (for example "when AI fails then not because there isn't enough intelligence but because there is too much artificial", S26 2026-08-11) and the "without machine learning" quip. Whether this is a change of view or a change of target is [inferred], not stated.

**C7. Simplify for practitioners?** He accepts that "we sometimes may need to simplify" in public communication, with "Jeez, I bit on my tongue, before I wrote that" (S09, 2015). In 2016 he cannot see "wie man vor dem Hintergrund einer immer komplexeren Welt den Königsweg in immer einfacheren Lösungen suchen sollte" [translation: how, in an ever more complex world, one should seek the royal road in ever simpler solutions] (S11).

---

## Gaps

- **Twitter/X, 2009 to about 2022.** By his own account (S20) this was his main public channel, and he used it daily (S17, S18). It sits behind a login and was not used. This is the largest gap in his stated views from 2009–2022.
- **Mastodon 2023–2026** was screened by keyword only, and 282 of the 669 statuses reported by the account were retrieved (boosts excluded). Counts in §0 are lower bounds.
- **Not read, paywalled or unreachable (identified only):**
  - his single-authored "Automatic Decomposition and Branch-and-Price—A Status Report", SEA 2012, LNCS, pp. 1–8, DOI 10.1007/978-3-642-30850-5_1 (not open access; the SEA 2012 site did not connect);
  - "Column Generation", Wiley Encyclopedia of Operations Research and Management Science (2011), DOI 10.1002/9780470400531.eorms0158 (not open access);
  - "Selected Topics in Column Generation" (2005), DOI 10.1287/opre.1050.0234, and "A Primer in Column Generation" (with Desrosiers, in *Column Generation*, Springer), DOI 10.1007/0-387-25486-2_1: not checked for open copies, not read.
- **PhD thesis**, "Engine Scheduling by Column Generation" (TU Braunschweig 2001), DOI 10.24355/dbbs.084-200511080100-720. The repository answered with a proof-of-work bot check, which was not bypassed. Its preface and introduction would give his 2001 voice.
- **Talks found but not transcribed:**
  - buzzITtalk podcast episode 02, "Optimized Decision Making with Analytics" (2018): blubrry page gone (HTTP 410); only the YouTube preview description was read.
  - DFG Science TV portrait (2009, 67 s): no captions.
  - Cassyni talk "SN Operations Research Forum" (2021, DOI 10.52843/cassyni.42wn2q): client-rendered page, content not reached.
  - CO@Work 2020 lecture: only three excerpts read.
- **Sites down on 2026-11-08:** the RWTH OR chair site (or.rwth-aachen.de, with and without www) and gcg.or.rwth-aachen.de timed out; DBLP answered with a bot check (not bypassed); the ELLIIT profile URL served only an image. No chair-level lab guide, thesis guidelines or onboarding text was found.
- **Not found:** statements on how he allocates his own time; how he decides between competing projects or funding calls; how he runs group meetings. Also anything signed by him on errata or retracted results (agent 03 and 05 territory).
- **Caption quality:** the *Subject to* and TEDx texts are YouTube ASR and were not checked against the audio.
- **Attribution:**
  - That the RWTH teaching-award video's last speaker is Lübbecke is inferred from his first-person words.
  - That the book's third-person "About the authors" paragraph on Marco was written by himself is not documented.

---

## Sources

One line each: title; author; date; URL or DOI; primary/secondary.

- S01 café opt, "About"; M. Lübbecke; 2014-09-29 (edited 2018-05-26); https://mluebbecke.wordpress.com/about/; primary.
- S02 café opt, "Me"; M. Lübbecke; 2014-10-15; https://mluebbecke.wordpress.com/me/; primary.
- S03 "Optimierung überall!"; M. Lübbecke; 2014-10-15; https://mluebbecke.wordpress.com/2014/10/15/optimierung-uberall/; primary.
- S04 "Millionen Entscheidungen!"; M. Lübbecke; 2014-10-27; https://mluebbecke.wordpress.com/2014/10/27/millionen-entscheidungen/; primary.
- S05 "Where are we heading?"; M. Lübbecke; 2014-11-04; https://mluebbecke.wordpress.com/2014/11/04/where-are-we-heading/; primary.
- S06 "How to write a paper"; M. Lübbecke; 2014-11-21 (edited 2015-04-21); https://mluebbecke.wordpress.com/2014/11/21/how-to-write-a-paper/; primary.
- S07 "Know your Heuristics!"; M. Lübbecke; 2014-12-19; https://mluebbecke.wordpress.com/2014/12/19/know-your-heuristics/; primary.
- S08 "Aussois"; M. Lübbecke; 2015-01-07; https://mluebbecke.wordpress.com/2015/01/07/aussois/; primary.
- S09 "Are we too complicated?"; M. Lübbecke; 2015-03-23; https://mluebbecke.wordpress.com/2015/03/23/are-we-too-complicated/; primary.
- S10 "Industrie 5.0"; M. Lübbecke; 2015-12-16; https://mluebbecke.wordpress.com/2015/12/16/industrie-5-0/; primary.
- S11 "#industrie40: zentral oder dezentral?"; M. Lübbecke; 2016-03-02; https://mluebbecke.wordpress.com/2016/03/02/industrie40-zentral-oder-dezentral/; primary.
- S12 His 21 comments on café opt (WordPress.com public API, comments endpoint); M. Lübbecke; 2014-11-01 to 2024-10-17; https://public-api.wordpress.com/rest/v1.1/sites/mluebbecke.wordpress.com/comments/; primary.
- S13 "Comments on: An overview of curriculum-based course timetabling"; M. E. Lübbecke; TOP 23 (2015) 359–361; DOI 10.1007/s11750-015-0364-1; primary.
- S14 OR2017 semi-plenary abstract "Optimization meets Machine Learning"; M. Lübbecke; 2017; https://www.wiwiss.fu-berlin.de/en/or2017/scientific-program/plenary_speakers/semi-plenary/marco_luebbecke.html; primary.
- S15 ORBEL 31 keynote abstract "Branch-and-Price"; M. Lübbecke; 2017; https://www.orbel.be/orbel31/keyspeakers.php; primary.
- S16 TEDxRWTHAachen, "Anything you can do I can do better"; M. Lübbecke; recorded 2018-06-09, published 2019-02-27; https://www.youtube.com/watch?v=Dc38La-Xvog (transcript: references/sources/talks/2018-06-09_tedx-rwth-aachen_anything-you-can-do_auto-transcript.txt); primary.
- S17 "Meet your professors | Prof. Dr. Marco Lübbecke"; RWTH Business School (Q&A); 2018-11-28; https://business-school.rwth-aachen.de/en/blog/meet-your-professors-prof-dr-marco-luebbecke; primary.
- S18 GERAD profile biography; M. Lübbecke; undated (2018–2024, probably 2020–21); https://www.gerad.ca/en/people/marco-lubbecke; primary.
- S19 CO@Work 2020 decomposition lecture; M. Lübbecke; uploaded 2020-09-23; https://www.youtube.com/watch?v=vx2LNKx48vY (excerpts: references/sources/talks/2020-09-23_coatwork-2020-decomposition-lecture_caption-excerpts.txt); primary.
- S20 "Subject to: Marco Lübbecke" (podcast interview, host A. Subramanian); 2021-09-23; https://www.youtube.com/watch?v=JzWAAvryTKA (transcript: references/sources/talks/2021-09-23_subject-to-podcast_auto-transcript.txt); primary.
- S21 "Die Qual der Wahl" slides, WiWi Network Research Talk #6; M. Lübbecke; 2021-09-22; https://www.wiwi-network.rwth-aachen.de/wp-content/uploads/2021/09/WiWi-Network_Research-Talk_6_Luebbecke_Die-Qual-der-Wahl.pdf; primary.
- S22 "RWTH verleiht Lehrpreis 2022 an Marco Lübbecke"; RWTH Aachen University; 2023-03-08; https://www.youtube.com/watch?v=LZLMijusUhg (captions: references/sources/talks/2023-03-08_rwth-lehrpreis-2022-video_auto-transcript.txt); primary (his part) / secondary (students).
- S23 "Branch-and-Price Crash Course" slides, CO@Work 2024; M. Lübbecke; 2024-09-19; https://co-at-work.zib.de/slides/COatWork2024_Luebbecke_BranchAndPrice.pdf; primary.
- S24 Keynote abstract "A Dantzig-Wolfe Hierarchy for the Stable Set Problem"; M. Lübbecke; January 2025; https://www.maastrichtuniversity.nl/file/marco-l%C3%BCbbecke-full-professor-and-chair-operations-research-rwth-aachen-universitypdf-0; primary.
- S25 PRIME abstract "(Who wants) Political Re-Districting in Germany (?)"; M. Lübbecke; 2025-07-01; https://wiwi.uni-paderborn.de/en/news/prime-who-wants-political-re-districting-in-germany; primary.
- S26 Bluesky posts of @mluebbecke.bsky.social (343, via public.api.bsky.app); M. Lübbecke; 2024-11-15 to 2026-11-07; https://bsky.app/profile/mluebbecke.bsky.social; primary.
- S27 Mastodon statuses of @mluebbecke@mas.to (282, via the mas.to public API); M. Lübbecke; 2022-11-06 to 2026-09-06; https://mas.to/@mluebbecke; primary.
- S28 *Branch-and-Price*; J. Desrosiers, M. Lübbecke, G. Desaulniers, J. B. Gauthier; Les Cahiers du GERAD G-2024-36 (revised Jan 2026) and Springer 2026; DOI 10.1007/978-3-031-96917-1, https://www.gerad.ca/en/papers/G-2024-36; primary (joint).
- S29 "Welcome to SN Operations Research Forum!"; M. Lübbecke, P. M. Pardalos; 2020-02-05; DOI 10.1007/s43069-020-0001-1; primary (joint).
- S30 GCG README.md, why-gcg.md and diverse-testset-generation.md; RWTH GCG team; fetched 2026-11-08; https://github.com/scipopt/gcg (master); primary (group).
- S31 *Subject to* video description and chapter list; A. Subramanian; 2021-09-23; https://www.youtube.com/watch?v=JzWAAvryTKA; secondary.
- S32 TEDx video description and TED.com talk page data; TEDx Talks / TED; 2019-02-27; https://www.ted.com/talks/marco_lubbecke_anything_you_can_do_i_can_do_better; secondary.
- S33 "Research Talk #6 – Prof. Dr. Marco Lübbecke ..." event summary; WiWi Network RWTH; 2021; https://www.wiwi-network.rwth-aachen.de/?p=6183; secondary.
- S34 RWTH description and students' statements in S22; RWTH Aachen University; 2023-03-08; https://www.youtube.com/watch?v=LZLMijusUhg; secondary.
- S35 GERAD news "Marco Lübbecke received 2022 Teaching Award" (2023-05-17) and "Great news for the optimization community!" (2026-02-06); GERAD; https://www.gerad.ca/en/posts/1063, https://www.gerad.ca/en/posts/1305; secondary.
- S36 Others' posts in the quoted Bluesky threads (S. Huiberts 2024-12-11; C. Contardo and M. Trick 2024-12-04/05; T. Serra, M. F. L. and others 2025-09-09; R. Cory-Wright, A. Buchanan 2026-08-18) and the image in his post of 2024-12-04; various; 2024–2026; https://bsky.app; secondary.
- S37 Metadata: Crossref (DOIs above and 10.1016/S0925-7721(98)00021-2, 10.1007/11427186_7, 10.1007/978-3-642-13193-6_21, 10.1007/s10107-014-0761-5, 10.1007/978-3-319-59776-8_16, 10.1007/978-3-540-68552-4_18, 10.1007/s10479-010-0700-7), OpenAlex A5082694588, Unpaywall, arXiv:2102.09663 (Qi, Wang, Shen 2021, the paper cited by the work he rejected); fetched 2026-11-08; metadata.
- Not reached (counted in the 46): dissertation landing page (bot check); SEA 2012 site; buzzITtalk episode page; Cassyni event page; or.rwth-aachen.de; gcg.or.rwth-aachen.de; DBLP 24/5951 (bot check); ELLIIT profile (image only); DFG Science TV portrait (no captions).
- Identified, not read: Lübbecke & Desrosiers 2005 (DOI 10.1287/opre.1050.0234); Desrosiers & Lübbecke 2005 (DOI 10.1007/0-387-25486-2_1); Lübbecke 2011 (DOI 10.1002/9780470400531.eorms0158); Lübbecke 2012 (DOI 10.1007/978-3-642-30850-5_1); Lübbecke 2001 thesis (DOI 10.24355/dbbs.084-200511080100-720); Gamrath & Lübbecke, SEA 2010, "Experiments with a Generic Dantzig-Wolfe Decomposition for Integer Programs" (DOI 10.1007/978-3-642-13193-6_21); Bergner et al., "Automatic Dantzig–Wolfe reformulation of mixed integer programs", Math. Programming 149(1–2) 391–424 (online 2014; DOI 10.1007/s10107-014-0761-5); Kruber, Lübbecke, Parmentier 2017 (DOI 10.1007/978-3-319-59776-8_16); Lach & Lübbecke 2008 (DOI 10.1007/978-3-540-68552-4_18) and 2012 (DOI 10.1007/s10479-010-0700-7, cited in S13).
