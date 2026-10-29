# Dimitris Bertsimas · 02 Stated methodology

> Research-craft note, nuwa Phase 1, research agent 02 of 06: what Bertsimas **says** research should be (how to choose problems, generate ideas, run and judge the work, write, and organise a group). Whether he practises it is note 03's job; this note only records what he said, tags it, counts repetitions and keeps contradictions.

| Field | Value |
|---|---|
| Researcher | Dimitris Bertsimas (b. 1962), Boeing Professor of Operations Research, MIT Sloan School of Management and Operations Research Center (ORC); MIT Vice Provost for Open Learning since 2024. Living. Not Dimitri P. Bertsekas (MIT LIDS), a different person. |
| Dimension | Stated methodology (framework §二, agent 2), sorted into the seven layers of framework §一 and, for this council, into the optimization domains of `team.json` |
| Research date | 2026-10-28 |
| Sources consulted | 47: 30 primary sources read, 12 secondary, 1 tertiary, 4 located and identified but not readable (metadata only). Full list under "Sources" |
| Search budget | 5 of 5 WebSearch calls used. Everything else came from curl or WebFetch on known URLs and from the arXiv, Crossref, OpenAlex and Open Library APIs |
| User-supplied material | None. At the start, `references/sources/papers`, `talks`, `essays` and `software` held only `.gitkeep`. During this pass, research agent 04 saved a public transcript under `talks/`: the 2014 MIT Sloan Oral History interview (S47, `talks/2014-10-24_sloan-oral-history-interview.md`). It is not user-supplied. I read it in full and checked every quote used here, with its page, against my own text extraction of the original PDF in MIT's repository. `private/` was not opened |
| Talk transcripts saved | None by this agent (see Gaps G1). S47 was saved by agent 04 |

**Labels.** [stated] = his own words, or a co-authored text he signs. [practice] = what papers or records show he did. [observed] = what others say about him. [inferred] = my reading, to be checked. *primary* = his own text, a Q&A or a speech in his own words. *secondary* = a journalist's or an institution's report. Direct quotes inside a secondary report are still his words, but the reporter chose and may have edited them. Domain codes follow `team.json` (LO IO RO CP SD ML DA HS AP); `ALL` means domain-independent.

**Quote discipline.** Every quotation below was checked word for word against a copy of its source saved on 2026-10-28. A script did the check, ignoring only differences in whitespace and quote marks: about 280 quotation strings, no misses (one hyphenation artefact was fixed by shortening the quote). Quotes from the 2014 oral history (S47) carry page numbers, checked against my own extraction of the original PDF. Typos in the sources are kept and marked [sic]. Paraphrases never go inside quotation marks and are labelled "paraphrase".

**Dating the key primary text (S01).** The essay "My Philosophy: Path, philosophy and aspirations" on his homepage is undated. Internal evidence [inferred]: "the first 25 years as a student and the last 27 years as a university professor" points to c. 2015 (he joined the faculty in 1988). "In the first half a century of life, I have formed a system of beliefs and values" points to c. 2012–2015. The "Life Stories" speech excerpt appended to it says a paper on personalized diabetes management "was published in Diabetes Care" "earlier this year". That paper (S33) came out online on 2016-12-05 and in print in February 2017, so the speech dates to c. 2017. Below, S01 is dated c. 2015–2017. A further clue: in the oral-history interview (S47, interview 2014-10-24, transcript PDF created 2016-06-06 and edited after the interview, since it mentions 2015–2016 events) he says "Recently I wrote a document, 3 pages. I am now 53. I wrote three pages reflecting on the years past, and where I should I focus on in the future." (p.18). If that three-page document is S01 [inferred], the essay dates to c. 2015–2016.

---

## 1. Claims repeated three or more times (real beliefs)

The counts are of separate statements. "Occasions" counts distinct documents or events, because the same essay can repeat itself.

| # | Claim (paraphrase; the verbatim quotes are in §2) | Statements / occasions | Span | Sources | Layers | Domains |
|---|---|---|---|---|---|---|
| R1 | Research is worth doing only if success would change something important: the human condition, what the next generation is taught, our understanding of how the world works, or industry practice, and soon | 11 / 5 | 2014 to 2026 | S47 ×3, S01 ×2, S17, S13 ×3, S16 ×2 | 1, 2, 5 | ALL |
| R2 | Doctoral students are his first priority and favourite activity | 8 / 4 (+1 secondary) | 2014 to 2026 | S47 ×3, S01 ×3, S13, S16; S17 (book dedication, secondary) | 7 | ALL |
| R3 | Aim high, beyond what you think you can achieve; positive energy decides success | 8 / 3 primary (+2 secondary) | 2012 to 2025 | S47 ×2 (p.7: "aggressive enough, or visionary enough, or ambitious enough"; "if you aspire often enough"), S01 essay and speech; S13 (paraphrase); S42 (2012, translated) | 2, 7 | ALL |
| R4 | Creating knowledge is not enough: transmit it through classes, books, open learning and education of practitioners; research enters courses, and courses become books | 9 / 6 | 2014 to 2026 | S47 ×3, S01, S13, S14 ×2, S15, S16 | 6, 7 | ALL, DA |
| R5 | Building companies is the way to affect the human condition at scale | 7 / 5 | 2012 to 2025 | S47 ×2, S01 ×2, S13, S14, S42 | 7 | ALL, AP |
| R6 | Real problems and data lead, models play a supporting role; problems come from his own experience (consulting, practice) | 7 / 5 | 2004 to 2025 | S07 ×2, S08 ×2, S05, S28, S12 | 1, 2, 6 | DA, AP |
| R7 | A theory or method is judged by whether it solves large, important, real problems ("Dantzig's test") | 4 / 4 | 1997 to 2022 | S09, S07, S06, S05 | 1, 5 | LO, RO, ALL |
| R8 | Tractability is a design requirement, and later specifically *practical* tractability | 5 / 5 | 2004 to 2022 | S29, S30, S05, S02 (2022 talk title); S17 (secondary) | 1, 3 | RO, IO, ML |
| R9 | "Why now": the measured speed-up of MIO solvers overturns the community's belief that MIO is intractable; NP-hardness is an opportunity | 7 / 7 | 2015 to 2019 | S21, S24, S27, S20, S26, S25, S05 | 2, 3 | IO, ML |
| R10 | Statistics and ML belong with optimization rather than probability ("a modern optimization lens") | 4 statements + 6 titles | 2015 to 2022 | S20, S05, S17 (secondary); titles in S21, S24, S04, S03, S22, S02 | 2, 3 | ML |
| R11 | A global, joint optimization beats greedy, sequential, trial-and-error or randomized practice | 8 / 8 | 2015 to 2021 | S25, S26, S27, S20, S03, S34, S05, S22 | 3, 4 | ML, IO |
| R12 | A result should come with a certificate: a suboptimality guarantee, provable optimality, or proof of infeasibility | 6 / 5 | 2015 to 2019 | S24, S26 ×2, S20, S03, S21 | 4, 5 | IO, ML |
| R13 | Interpretability matters materially in the real world | 6 / 4 | 2018 to 2025 | S05, S02 (3 talk titles), S36, S12 | 1 | ML, DA |
| R14 | The real objective is prescription, not prediction | 6 / 5 | 2014 to 2025 | S05, S28, S44 (2015 lecture title), S02 (2016 and 2020 talk titles), S12 | 1, 2 | DA |
| R15 | A book must give a "unified, insightful" treatment | 5 / 5 | 1997 to 2022 | S09, S10, S07, S08, S06 | 6 | ALL |
| R16 | Personal experience (losing his parents) seeded a research program in personalized medicine | 2 primary + 4 reports | 2014 to 2026 | S47, S01; S17, S16, S23 (chapter title), S41 (episode description) | 2 | AP, DA, ML |

Single statements that are informative but below the threshold of three: an ex-ante answerability rule (T1), a two-year impact horizon (T2), "aim to impress" as an early-career error (T3), the 1989 failed proof (F1), the evaluation caveat for the chemotherapy models (J3), the evaluation criteria for feature selection (E4), the structural choice in RAO that adaptive RO is a tool for solving RO (G3), PhD topics agreed by mutual convincing and kept separate from funding (P7, 2014), the rule that students join his companies only after graduating (O10, 2014).

---

## 2. Findings by layer (framework §一)

### Layer 1 · Research taste

**T1. The impact test, applied before the work starts** {ALL} [stated · primary · S01, c.2015–2017]
> "The only research worth doing has the following characteristic: Assume we succeed 100% in answering the research question we aim to address. Then, does something change in the world for the better among those things that are important in life? That is, does the human condition improve? Do the results of the research affect what we teach the future generations? Does the research increase the understanding of how the world works? If the answer to these questions is no, and in my experience it often is, then I do not think we should be doing this research on the first place [sic]. What is important is that these questions are answerable before we do the research."

- The test has three working parts: a thought experiment ("Assume we succeed 100%"), three questions that mirror his three life objectives, and the rule that the questions must be answerable *before* the research. The three objectives in S01: "To improve the human condition", "To positively affect the lives of people, especially young people.", "To increase the human understanding of how the world works."
- He expects most candidate questions to fail ("in my experience it often is").
- In the same essay he calls this the heart of what he teaches: "The most important thing I aspire to help them learn is why research is important and especially what research is important." and "In my opinion, research is serious business and is linked to what is important in life I outlined earlier."
- Repetition (R1): S17 (c.2016): "It is my objective to generate knowledge that affects what the next generations learn," and "Is it impactful? That's how I judge what is important." S13 (2025): "My strategy has been to address significant challenges that the world faces, and try to make progress," S16 (Killian Lecture, 2026-03-19, as reported): "I have tried to improve the human condition," and "I try to increase the human understanding of how the world works." The three-objective frame of c.2015 comes back almost word for word in 2026, so it has been stable for over a decade (the 2014 version is below).
- **The earliest dated version, with working definitions** (S47, oral history, 2014-10-24, pp.6–7). He applies the test to PhD topics:
  - "And if you are successful in addressing the topic we are discussing, so in other words, putting ability aside, and you are 100% successful, would it be something that changes the world for the better."
  - For theory, the test is whether the result can be taught: "The way I define it is, if it is a theoretical topic and you are fully successful in the research, can you teach this research in graduate-level courses? If you can teach it in undergraduate-level course, it is a big breakthrough. It happens maybe once or twice in a career. So that's on the theory side."
  - For applications, the test is adoption: "If it's an application, then the results of the research will then be used by companies in a reasonable amount of time. Not in 40 years, but 2 to 5 years."
  - The conclusion: "If it doesn't happen, then we shouldn't be working. That's my philosophy on that."
  - Why the test has to be operational (p.7): "In the earlier years, when I was younger, I did not realize fully that the key aspiration is to have impact. But impact is a bit ethereal. So now I've defined it, then I can measure it. Of course we are not always successful. But if you aspire often enough, sometimes you will be successful".
  - The rule: turn "impact" into two observable proxies, *teachability* (graduate course; undergraduate course = a once-or-twice-a-career breakthrough) and *adoption by companies within a few years*. Together with S01, S17, S13 and S16, the test is stable from 2014 to 2026.

**T2. Impact should show up soon, in teaching or in industry** {ALL, DA, AP} [stated · secondary report with a direct quote · S13, 2025]
> "Second, in my research, I've tried to address problems that I think are important. If you solve them, something changes, in what we teach or in industry, and in short order. Not in 50 years, but in two years."

- There is one earlier statement of the horizon. In 2014, for applied work: "Not in 40 years, but 2 to 5 years." (S47 p.6). The numbers differ; see contradiction C8.

**T3. Change the world, do not impress** {ALL} [stated · primary · S01]
> "It took me more than a decade to fully crystalize [sic] these principles. I see a lot of people, including myself in my early years, who aim to impress rather than change the world. More than the specific areas of research, my central aspiration is to help my graduate students learn these principles."

- This is a self-correction with a date attached: his principles took "more than a decade" to form, so roughly from the late 1990s if counted from 1988 [inferred].
- A related statement, S13 (2025): "We don't do things at MIT to get awards; we do things here because we believe they are important."
- **The 2014 account dates the change** (S47 p.14) [stated · primary]:
  - "In the beginning of my career, when I was not mature enough I would say, my objective was, I didn't realize this, it was not a conscious decision, to try to impress my seniors. I was trying to impress the world that I am a very good researcher. I've succeeded, to a degree."
  - "I did not pick topics naturally. Some of them were important, but I didn't pick them because of that. It was a different objective."
  - The turn came "when I was in my mid-thirties, 10 years into being a professor, I realized that the world doesn't really care to be impressed!", i.e. c. 1997–1998. Then: "So I said, "Let me try to do things that I think are important. Maybe the world doesn't think they are important, but I think they are important." As a result, I think I became a better advisor."
  - So his own criterion of importance outranks outside recognition.
- **Significance, not the theory/application label** (S47 p.14): "So as a result, Bob, I don't put a lot of emphasis on theoretical or applied. Is it significant?"

**T4. The six "Philosophical principles" of *Machine Learning under a Modern Optimization Lens* (2019)** {ML, IO, DA} [stated · primary · S05, publisher page of his own press; co-author J. Dunn; the preface itself not read]
> "Interpretability is materially important in the realworld [sic]."
> "Practical tractability not polynomial solvability leads to real world impact."
> "NP -hardness is an opportunity not anobstacle [sic]."
> "ML is inherently linked to optimization not probability theory. Data represent an objective reality; models only exist in our imagination."
> "Optimization has a significant edge over randomization."
> "The ultimate objective in the real world is prescription,not [sic] prediction."

- Each principle recurs elsewhere: interpretability in R13, tractability in R8, NP-hardness in R9, optimization rather than probability in R10, optimization over randomization in R11, prescription in R14. Together they are the clearest compact statement of his post-2014 taste.

**T5. A theory is tested by the problems it solves (Dantzig's test)** {LO, RO, ALL} [stated · primary · S09 1997, S07 2004, S06 2022]
- S07 (DMD, with R. Freund) quotes Dantzig, "The final test of any theory is its capacity to solve the problems which originated it.", and sets its own mission to "demonstrate that the tools and models of management science pass Dantzig's test."
- S09 (ILO, with J. N. Tsitsiklis, 1997): "The success of any optimization methodology hinges on its ability to deal with large and important problems."
- S06 (RAO, with D. den Hertog, 2022): "Our extensive treatment of a variety of applications of RO and ARO in several fields in Part VI is guided by the quote of George Dantzig at the beginning of the preface." Which Dantzig quote is used was not read; that it is the same one as in S07 is [inferred].
- R7.

**T6. Interpretability is a requirement in its own right** {ML, DA, AP} [stated · primary]
- S05: "Interpretability is materially important in the realworld [sic]."
- S36 (2019, with Delarue, Jaillet, Martin). Paraphrase: understanding a model's reasoning can raise trust, expose hidden biases and reduce vulnerability to adversarial attacks. Verbatim: "However, the concept of interpretability remains loosely defined and application-specific." Their answer is a definition: "In this paper, we introduce a mathematical framework in which machine learning models are constructed in a sequence of interpretable steps."
- Talk titles in S02: "Princeton Day of Optimization 2018: Interpretable AI by Dimitris Bertsimas" (video posted 2019-10-29); "2019 MIT Citi - 4 - Interpretable AI and Its Applications in Financial Services" (2019-06-22); "Interpretable AI by Dimitris Bertsimas, MIT plus Opening of OR62 Conference" (2020-09-18).
- S14 (2025), on the role of generative AI: "we use machine learning to make better predictions, but generative AI can explain them."
- S12 (2025) lists "from interpretable risk scores to fair allocation policies" among recent advances.
- R13.

**T7. Tractability makes a theory usable** {RO, IO, ML} [stated · primary]
- S29 (2004, with M. Sim): "An attractive aspect of our method is that the new robust formulation is also a linear optimization problem." and "Thus we naturally extend our methods to discrete optimization problems in a tractable way."
- S30 (2011, with D. B. Brown and C. Caramanis): "Our focus is on the computational attractiveness of RO approaches, as well as the modeling power and broad applicability of the methodology."
- S02, talk title (2022-10-18): "Robust and Adaptive Optimization: A Tractable Approach to Optimization Under Uncertainty".
- S05 (2019): "Practical tractability not polynomial solvability leads to real world impact."
- S17 (secondary, the ORC writer, possibly paraphrasing him): "The key contribution is a tractable theory of optimization under uncertainty."
- The meaning shifts over time [inferred]. In 2004 "tractable" means the robust counterpart stays in the same complexity class (an LP stays an LP). In 2019 it means empirical solve times on real instances, explicitly *not* polynomial solvability. See C2.

**T8. Insight through geometry first, then algebra and algorithms** {LO, IO} [stated · primary · S09 1997, S10 2005]
> S09: "Our general philosophy is that insight matters most. For the subject matter of this book, this necessarily requires a geometric view. On the other hand, problems are solved by algorithms, and these can only be described algebraically. Hence, our focus is on the beautiful interplay between algebra and geometry."
> S10 (OoI, with R. Weismantel): "We depart from earlier treatments of integer optimization by placing significant emphasis on strong formulations, duality, algebra and most importantly geometry."

- Two occasions, both co-authored textbooks of his theory-first period. This is below the threshold of three; treat it as the taste of the textbook era.

**T9. What he calls bad practice** {ALL, DA, ML} [stated · primary]
- Teaching that puts methods first. S08: "This is in contrast with the vast majority of books and classes available today, in which methods play the leading role." S07: "Simply teaching students to plug numbers into black-box models is not relevant to a student's education."
- A literature that does not help practitioners. S35 (2020): "Indeed, sparsity is a valuable property and the profusion of research on the topic might have provided little guidance to practitioners."
- Research aimed at impressing others (T3), and research that would change nothing even if it succeeded (T1).

### Layer 2 · Problem choice

**P1. Start from a real problem and its data, because problems "do not come with labels"** {DA, AP, ALL} [stated · primary · S08 2016]
> "The philosophical underpinnings of the book are that real world problems are usually complex and often will defined [sic]; they do not come with labels, meaning that they are not necessarily regression problems or optimization problems. The only objective reality is data, which itself may be incomplete and of questionable quality, and the role of models is to facilitate the solution of real world problems. Problems and data play a leading role in this book, while models play an essential but supporting role. This is in contrast with the vast majority of books and classes available today, in which methods play the leading role."

- S08: "Most chapters in the book start with a real world problem (typically from our experience) and a data set, and then use a variety of methods to address the problem."
- S07: "Rather than covering methodology, the book introduces decision support systems through real world applications". Its cases come from practice: "the book features over thirty business cases that are drawn from our own consulting experience or the experience of our students".
- S28 (2014/2020, with N. Kallus) shapes the problem class itself around data seen in practice: "In a departure from other work on data-driven optimization and reflecting our practical experience with the data available in applications of OR/MS".
- S14 (2025): "As an academic, I've always aspired to educate, write publications, and utilize what we do in practice."
- R6. Era note: S07 and S08 are teaching texts for MBA and analytics audiences and S28 is an applied paper. The PhD texts of 1997 and 2005 (S09, S10) lead with theory instead; see C2.

**P2. "Why now": go back to a problem once the tool believed impractical has changed** {IO, ML} [stated · primary]
- S27 (2016, with A. King): "Linear regression models are traditionally built through trial and error to balance many competing goals such as predictive power, interpretability, significance, robustness to error in data, and sparsity, among others. This problem lends itself naturally to a mixed integer quadratic optimization (MIQO) approach but has not been modeled this way because of the belief in the statistics community that MIQO is intractable for large scale problems."
- S21 (Georgia Tech lecture, 2015; abstract partly edited by the host): "While such beliefs were accurate two decades ago, the field of discrete optimization has made very substantial progress." and "Most importantly, he suggests that the belief widely held in statistics that mixed integer optimization is not practically relevant for statistics applications needs to be revisited."
- The speed-up sentence that opens his abstracts:
  - S24 (arXiv 2015, AoS 2016): "In the last twenty-five years (1990-2014), algorithmic advances in integer optimization combined with hardware improvements have resulted in an astonishing 200 billion factor speedup in solving Mixed Integer Optimization (MIO) problems."
  - S25 (2017): "In the last 25 years, algorithmic advances in integer optimization coupled with hardware improvements have resulted in an astonishing 800 billion factor speedup in mixed-integer optimization (MIO). Motivated by this speedup, we present optimal classification trees".
  - S26 (2017) and S20 (2016) use 450 billion for 1991–2015.
- S05 (2019): "NP -hardness is an opportunity not anobstacle [sic]."
- R9: seven occurrences, 2015–2019. The size of the speed-up differs between papers (C5). Era: the argument depends on 2010s commercial MIO solvers and hardware. In his own framing it was not available "two decades ago".

**P3. Bring another field's central problems under your own lens** {ML} [stated · primary]
- S20 (IFORS Distinguished Lecture, EURO 2016): "The field of Statistics has historically been linked with Probability Theory. However, some of the central problems of classification, regression and estimation can naturally be written as optimization problems. While continuous optimization approaches has [sic] had a significant impact in Statistics, mixed integer optimization (MIO) has played a very limited role, primarily based on the belief that MIO models are computationally intractable."
- S17 (secondary, c.2016): "The key plan is to revisit some of the central problems of statistics and machine learning under a modern optimization lens that includes discrete, robust and convex optimization."
- S05: "ML is inherently linked to optimization not probability theory."
- The same branding recurs across a decade, as "under a modern optimization lens" or "via a modern optimization lens", in S21 (2015), S20 (2016), S24 (2016), course 15.095 (S04), the 2019 book (S03), S22 (2021); S02 (2022) has "ML from the Perspective of Modern Optimization". R10.

**P4. Aim high, beyond what you think you can do** {ALL} [stated · primary · S01]
- Key principle of research: "There is nothing that we cannot achieve if we put our minds into it."
- Value 3, "High aspirations matter.": "We should aim to change the world, if we have a chance to do it. I do not know of many examples of people who changed the world without aiming to do so."
- Speech: "As a professor, I have tried to teach my students to aim high, even higher that [sic] they think they can achieve and dedicate themselves to achieve it."
- His own examples: finishing a five-year degree in four years ("With the objective to find my boundaries, I set a goal of doing exactly that despite the advice of my father not to do it"), and the failed 1989 proof (F1).
- R3. The positive-energy half is under O3.

**P5. Personal experience can seed a research program** {AP, DA, ML} [stated · primary · S01]
- After his father (gastric cancer, diagnosed 2007), his aunt and his mother (complications of diabetes) died in 2009: "this experience led me to initiate a research program in personalized medicine".
- "Overcoming the sadness of losing 3 of the closest people in my life and transforming a very difficult experience to a positive outcome, has made the journey and my life more meaningful and worthwhile."
- On how the group has shifted: "Today, more than half my research group are working on their PhD in personalized medicine" "with the aspiration to affect the practice of medicine and using analytics, especially Machine learning, to make it more effective."
- He ties two papers to this. One is a gastric-cancer paper with three students that won "the first prize in healthcare from INFORMS"; matching it to S32 (gastric cancer trials; students O'Hair, Relyea, Silberholz) is [inferred]. The other is the Diabetes Care paper (S33).
- In reports: S17 (c.2016, "grew out of personal tragedy"; his quote "I believe this [research] will change how disease is treated today,"); S16 (2026, as reported, the parents' deaths "helped propel him to start looking at extensively at ways operations research could help health care"); S23 (chapter title "Overcoming the loss of close family members and turning into motivation for doing research"); S41 (episode description). R16.
- **Earlier and fuller, 2014** (S47 pp.14–17) [stated · primary]:
  - "Nobody can convince me that it's not an important topic." and "Half my family chain was lost to that disease. It's a serious matter." (p.15, on diabetes).
  - The program had two roots. One was industry: his health-data company D2 Hawkeye, "So this is almost a decade of experience, and it exposed me to the healthcare system. That was one influence." (p.16). The other was personal: "So I decided that would become a significant portion of my effort, trying to fight these diseases using the things I know, specifically, quantitative methods." (p.16).
  - He sets a boundary on his competence: "I'm not a biologist, I'm not a physician, although I learned some things because I look at these things." (p.16).
  - On motivating students: "And it's easy for young people to be motivated. Many of them are idealistic, they would like to impact the world positively." (p.15).

**P6. Keep the topics that will shape the future of the field** {IO, ALL} [stated · primary · S10, 2005]
> "We have selected those topics that we feel have influenced the current state of the art and most importantly we feel will affect the future of the field."

- Once. It is a selection rule for a book, but it has the same forward-looking structure as T1.

**P7. Agree PhD topics by mutual convincing, and keep them separate from funding** {ALL} [stated · primary · S47, 2014, pp.6–7 and 13–14]
> "The way I do it is somewhat different. I separate funding and PhD topic. In other words, my philosophy on this is as follows: I need to convince the students that the topic I propose matters. The students can also propose a topic they are interested in. But both of us need to convince the other person."

- How it plays out: "They can convince me to work on whatever they decide to work on, but they have to convince me on the topic's impact in either theory or practice, as I have to convince them as well. And some do. In fact, some of them, I would say one-fourth of them, we work on topics as they have defined." (p.14).
- Funded projects are kept beside the thesis topic, not in its place: "Very often, 50% of my students work on the topic of their research, and that's the price you pay for having complete freedom." (p.7; transcript wording kept). Such projects can still lead somewhere: "Sometimes it can lead to a PhD topic as well, because it gives us exposure to the world." (p.7).
- Why: "But I view funding as an enabler of doing excellent work, not a constraint that these are the only topics you should be working on if you want to have funding. Otherwise, you might not be aggressive enough, or visionary enough, or ambitious enough." (p.7).
- Once (2014) as a stated procedure. The impact criterion inside it is R1.

**P8. Find the missing data asset that a field's practice lacks** {AP, DA, ML} [stated · primary · S47, 2014, pp.16–17]
- His diagnosis of cancer research: "But doctors make the decisions on what combinations to use with intuition." "But nobody designs experiments using the totality of human knowledge - because nobody has it."
- His response was to build the asset: "With 20 MIT undergraduates and several of my doctoral students, we actually developed such a database. This was in 2008." The problem then splits into prediction and selection: "Given that the majority of clinical trials use drugs in different combinations that have been seen earlier, we use machine learning methods to predict outcomes of different chemotherapy regimens." and "Then we use optimization to say, let's say we have 50 possibilities of combinations. Which are the best 10 to try, as opposed to all 50?"
- A modest goal: "We aren't going to cure cancer that way, but we are going to be far more effective in the treatments. And we will learn faster."
- Once (the published version is S32).

### Layer 3 · Idea generation

**G1. Recast a greedy or sequential practice as one problem solved jointly to optimality** {ML, IO} [stated · primary]
- S25 (with J. Dunn, 2017): "State-of-the-art decision tree methods apply heuristics recursively to create each split in isolation, which may not capture well the underlying characteristics of the dataset. The optimal decision tree problem attempts to resolve this by creating the entire decision tree at once to achieve global optimality."
- S26 (with A. King, 2017), whose title is *Logistic Regression: From Art to Science*: the MINLO approach is chosen "in order to explicitly incorporate these properties in a joint, rather than sequential, fashion."
- S27 (2016): models "are traditionally built through trial and error to balance many competing goals". His answer is one MIQO-based approach "that explicitly addresses various competing objectives" (the abstract's last sentence).
- R11. The move: name the craft step done by hand or greedily, write the whole design problem as a single (mixed-integer) optimization, and solve it to certified optimality.

**G2. Find the widely held belief and test it** {ML, RO, DA} [stated · primary]
- S20 (2016): "We show that robustness and not sparsity is the major reason of the success of Lasso in contrast to widely held beliefs in ML/S." The related paper S39 was found as metadata only.
- S25 (2017): optimal trees, "refuting the notion that optimal methods overfit the training data".
- S34 (2015, with M. Johnson and N. Kallus) questions randomization: "However, with a small sample, which is a practical reality in many disciplines, randomized groups are often too dissimilar to be useful." It is generalised in S05 ("Optimization has a significant edge over randomization.") and S22 (2021): "...compared to the usual randomization approach."
- The intractability belief, under P2.
- Four or more occasions. As a stated habit [inferred from the stated pattern]: name the consensus, then attack it with an optimization formulation and a computation.

**G3. Use one theory to solve another's problem: adaptive RO as a tool for RO** {RO} [stated · primary · S06, 2022]
> "We present RO and ARO for LO in Parts I and II, and we return to RO for nonlinear optimization in Parts III and IV, as opposed to presenting RO first and then ARO. The reason is that ARO offers new and very effective ways to solve RO problems, a fact not fully recognized earlier."

- Once. It is an organising idea ("Our unifying treatment of RO and ARO.") stated as a claim about the field.

**G4. Tune the conservatism and put feasibility first** {RO} [stated · primary · S29 2004; as reported in S16 2026]
- S29: "Under this approach, we are willing to accept a suboptimal solution for the nominal values of the data in order to ensure that the solution remains feasible and near optimal when the data changes. A concern with such an approach is that it might be too conservative." and "In particular, we flexibly adjust the level of conservatism of the robust solutions in terms of probabilistic bounds of constraint violations."
- S16 (Killian Lecture 2026, reported): on the Panama Canal, "Other approaches to optimization aimed at getting more vessels through the canal every day — up to 48 — but would encounter significant problems at times." "Bertsimas' approach identified that 45 vessels a day was better", a number that "was always feasible" (his words inside the report).
- Two occasions, 22 years apart. The same stated value: a solution that stays feasible under realistic uncertainty, at a price the decision-maker can tune.

**G5. A research line can start from life events.** This is a cross-reference to P5. He presents transforming a loss into a program as a deliberate choice ("transforming a very difficult experience to a positive outcome").

**G6. Combine the stochastic and the optimization view** {SD, IO} [stated · primary · S47, 2014, pp.1–2]
- Describing his own PhD on vehicle routing "when there is uncertainty" (p.1): "So I combined stochastic ideas and optimization ideas."
- Once. It is the only statement found in which he describes an idea in the SD domain. His later stance that ML belongs with optimization rather than probability (R10) points the other way; see C4.

### Layer 4 · Experiments and execution

**E1. A three-part evaluation: fast, certified, better out of sample** {ML, IO} [stated · primary]
- S20 (2016): "In all cases we demonstrate that optimal solutions to large scale instances (a) can be found in seconds, (b) can be certified to be optimal in minutes and (c) outperform classical approaches."
- S03 (homepage description of the 2019 book): "...leads to solutions to central ML problems at large scale that can be found in seconds/minutes, can be certified to be optimal in minutes/hours, and outperform classical heuristic approaches in out-of-sample experiments."
- S24: "(a) provides a solution with a guarantee on its suboptimality even if we terminate the algorithm early".
- S25: "We comprehensively benchmark these methods on a sample of 53 datasets from the UCI machine learning repository."
- Three or more occasions. As a stated protocol: (i) solve time at realistic scale, (ii) an optimality certificate or gap, (iii) out-of-sample comparison against the standard heuristic (Lasso, CART).

**E2. Warm-start with fast first-order heuristics, then certify with MIO** {IO, ML} [stated · primary]
- S24: "We develop a discrete extension of modern first order continuous optimization methods to find high quality feasible solutions that we use as warm starts to a MIO solver that finds provably optimal solutions."
- S21 (2015, host-edited): "Dr. Bertsimas will discuss how to apply modern first order optimization methods to find feasible solutions for classical problems in statistics, and mixed integer optimization to improve the solutions and to prove optimality by finding matching lower bounds."
- Two occasions.

**E3. Test on synthetic data (known truth) and on real data** {ML, DA} [stated · primary]
- S24: "Using a wide variety of synthetic and real datasets".
- S26: "Using both real and synthetic data".
- S27: "on both real and synthetic data sets".
- S36: "on real and synthetic datasets".
- S25: "Synthetic tests demonstrate that these methods recover the true decision tree more closely than heuristics".
- Five occasions. These are what the abstracts say was done; checking the actual experimental designs is note 03's job.

**E4. Criteria for judging a variable-selection method** {ML} [stated · primary · S35, 2020, with J. Pauphilet and B. Van Parys]
> "A cogent feature selection method is expected to exhibit a two-fold convergence, namely the accuracy and false detection rate should converge to $1$ and $0$ respectively, as the sample size increases."
> "Jointly considered, accuracy, false detection and computational time provide a comprehensive assessment of each feature selection method"
> "We released code for methods that were not publicly implemented."

- Once. Context: this paper appeared in *Statistical Science* in 2020, amid published comparisons of best-subset selection and the Lasso. That exchange was not read here (it belongs to note 05).

**E5. Deployment is the decisive experiment, and it includes educating the users** {AP, DA} [stated · primary · S14, 2025]
> "To have an impact, you need to have appropriate methods, implement them, and apply them, but you also need to educate people on how to use them."

- "We have developed a variety of tools at MIT and implemented them at hospitals around the world."
- The impact claim: "Using analytics, we have reduced patients' length of stay at Hartford Hospital from 5.67 days to five days." The 2026 report gives other numbers (C6).
- He also founded a company to carry the work into practice: "Therefore, I founded Holistic Hospital Optimization (H20) with the goal of optimizing hospital operations with machine learning to improve patient care."

**E6. Build a metric for prescriptive value** {DA} [stated · primary · S28]
> "As an analogue to R^2, we develop a metric P termed the coefficient of prescriptiveness to measure the prescriptive content of data and the efficacy of a policy from an operations perspective".

- Once; linked to R14.

**E7. Propose, then test in the field** {AP, DA} [stated · primary · S47, 2014, pp.17–18]
> "At the end of the day, we propose things. We need to examine whether our proposals work in practice."

- In 2014 that meant hospital trials. Paraphrase of p.17: a trial in Nashville, and planned ones in the Cleveland area and in Massachusetts.
- Adoption takes time: "It's a long, long process to convince people who don't think this way. Doctors, they mean very well, but they don't think data, machine learning, optimization." and "But I have found enough people who are convincible. When they see the evidence… We shall see. It's a long struggle. But I'm very devoted to that."
- With E5 (2025) this makes two occasions, eleven years apart. The diabetes system is reported the same way: "We have already seen that it changes the life of certain people." (p.16).

### Layer 5 · Judging results

**J1. Judge importance before the work, with the impact test.** See T1. In S17 (c.2016): "Is it impactful? That's how I judge what is important."

**J2. A result is stronger when it carries a certificate** {IO, ML} [stated · primary]
- S24: "(a) provides a solution with a guarantee on its suboptimality even if we terminate the algorithm early".
- S26: "provides high quality solutions in realistic timelines as well as a guarantee of suboptimality". Also: "When the MINLO is infeasible, we obtain a guarantee that imposing distinct statistical properties is simply not feasible." Infeasibility is presented as a usable negative result.
- S20 and S03: "certified to be optimal".
- R12.

**J3. Say what the evaluation cannot show** {AP, DA} [stated · primary · S32, 2016]
> "Though it is inherently challenging to evaluate the performance of such models without actually running clinical trials, we use two techniques to obtain estimates for the quality of regimens selected by our models compared with those actually tested in current clinical practice." … "This evaluation of the proposed models suggests that they merit further testing in a clinical trial setting."

- Once. It is the only explicitly hedged conclusion found in this pass.

**J4. Report where a method wins, not only that it wins** {ML} [stated · primary · S25]
> "we identify that optimal classification trees are likely to outperform CART by 1.2–1.3% in situations where the CART accuracy is high and we have sufficient training data"

- Once in this pass.

**J5. Reliability over nominal optimality.** See G4: the robust 45-vessel plan "was always feasible", and the trade of nominal optimality for feasibility in S29.

**J6. Value a failed attempt for what it taught.** See F1: "In the end I did not succeed in this goal, but my understanding of optimization deepened considerably."

**J7. Trust what the data showed, and say when there is no theory** {DA, AP, ALL} [stated · primary · S47, 2014]
- p.18: "But I absolutely believe - it's not a theoretical belief, I've seen it in the data - that looking at personalized traits of people, you can actually design appropriate meds for them, personalized."
- p.19, on organisations: "As the size of the company increases, because you need structures, the creativity and the inventiveness goes down. I have found this empirically. I don't have a theory about it, but I have loads of empirical data about it."
- Two statements in one interview. The stance [inferred]: an empirical regularity he has seen is enough to act on, and he labels it as empirical rather than dressing it up as theory.

**J8. Success is not guaranteed; aspire often** {ALL} [stated · primary · S47 p.7]
> "Of course we are not always successful. But if you aspire often enough, sometimes you will be successful"

- He treats the impact test as a filter applied to many attempts, not a promise for each one. Compare F3.

### Layer 6 · Writing and talks

**W1. A "unified, insightful" treatment as the standard for a book** {ALL} [stated · primary] (R15)
- S10 (2005): "The purpose of this book is to provide a unified, insightful, and modern treatment of the theory of integer optimization with an eye towards the future."
- S06 (2022): "The purpose of this book is to provide a unified, insightful, and original treatment of robust and adaptive optimization."
- S08 (2016): "The Analytics Edge provides a unified, insightful, modern and entertaining treatment of analytics."
- S09 describes "a modern and unified introduction to linear optimization". S07 has a section "Unified Treatment of Quantitative Methods".

**W2. Comprehensive but economical; principles before details** {LO} [stated · primary · S09]
> "Another of our objectives is to be comprehensive, but economical." … "Our premise is that once mature understanding of the basic principles is in place, further details can be acquired by the reader with little additional effort."

**W3. Say it once or twice, then reinforce it in exercises and cases** {ALL} [stated · primary · S07]
> "That is, the relevant points are made in the book once or twice, with appropriate examples, and then reinforced in the exercises and in the case modules."

**W4. Readable and engaging** {ALL} [stated · primary · S07]
> "We have deliberately written the book in a style that is engaging, informative, informal, conversational in tone, and imbued with a touch of humor from time to time."

- S08 adds "entertaining".

**W5. Lead with the real case; methods serve it** {DA, AP} [stated · primary] (R6)
- S08: chapters "start with a real world problem (typically from our experience) and a data set".
- S12 (2025): "Each chapter introduces a class of algorithms through the lens of a real clinical example."
- S07: spreadsheets "are a vehicle for working with models, but are not a substitute for thinking through the construction of models and analyzing modeling-related issues."

**W6. Separate structure from the details of an algorithm** {LO} [stated · primary · S09]
> "In the same spirit, we separate the structural understanding of linear programming from the particulars of the simplex method."

- In the same text: "we include a derivation of duality theory that does not rely on the simplex method". Exercises should deepen understanding: "Most of them are intended to deepen the understanding of the subject, or to explore extensions of the theory in the text, as opposed to routine drills." The book ends with "the art of linear optimization" because "progress on challenging problems requires both problem specific insight, as well as a deeper understanding of the underlying theory."

**W7. Explain the organising choices** {RO} [stated · primary · S06]
- See G3: ARO comes before nonlinear RO, and the reason is given.

**W8. Open the abstract with the field's belief and the enabling change** {IO, ML} [stated text pattern · primary · S24, S25, S26, S27]
- The pattern: state the community belief or the old practice, quote the speed-up, then write "Motivated by this speedup, we present …" (S25, S26).
- How consistently he writes this way is for note 03 (practice).

**W9. Keep the talk titles consistent across a decade** [practice-adjacent · primary · S02, S20, S21, S22, S44]
- "modern optimization lens" (2015 to 2022), "Interpretable AI" (2018 to 2020), "From predictive to prescriptive analytics" (2015, 2016, 2020).
- This is listed because the titles are his own framing (R10, R13, R14). No talk content was read (G1).

**W10. Turn research into courses and books** {ALL} [stated · primary] (R4)
- S01: "It is my aspiration to generate new knowledge that I consider important in life and teach the next generations by introducing new classes and writing books." Also: "I also believe that this responsibility is increasing with age".
- The S04 course list includes 15.094 Robust Optimization, 15.095 Machine Learning Under a Modern Optimization Lens and 15.076 Analytics for a better world [practice].
- **2014 account of the cycle** (S47 pp.11–13) [stated · primary]:
  - He teaches new things on purpose: "I actually do not like teaching the same thing year in/year out. So over time, I have developed many, many courses and have written books on these courses, actually." and "Generally speaking, my style is that I like teaching new things. On the way, I also learn."
  - ILO came from a decade of teaching notes: "I started teaching in 1988 the doctoral optimization class. To be honest, I did not think it was taught exceptionally well - I inherited the class, so I covered it the way we had been doing it, the first time. But I taught it over a decade, and during this time, I developed a set of notes." With Tsitsiklis, "Then we wrote a book in 1997, about 10 years later, that was tested."
  - Why books: "I believe a good book contributes greatly to a good class."
  - Research and teaching are integrated: "Yes, it's integrated. For example, these days I am also working on healthcare analytics, and quite a bit of material from the research has entered these courses."
  - The sequence: teach, write notes, test them in class over years, then publish a book. Research is cycled into courses.

**W11. Compression forces you to decide what matters** {ALL} [stated · primary · S47, 2014, p.10]
- On rebuilding his course for the first Sloan MOOC (8 four-minute modules, paraphrase): "It forces you to think: What is important? What is less important? How to sequence the material. As a result, all of this material is higher quality, in my opinion, from what I used to do."
- He frames the MOOC itself as an experiment: "We are experimenting. Nobody knows, really." and "Slow steps." (pp.10–11).

**W12. Rehearse students' talks** {ALL} [stated · primary · S47, 2014, p.19]
- "he's giving a talk and I would like to rehearse with him, so I will be able to help him on that given my experience."
- Once. It is the only statement found about talks.

### Layer 7 · Research organisation

**O1. Students first** {ALL} [stated · primary] (R2)
- S01: "I consider being the advisor of my graduate students far and away the most important aspect of my life as an academic. My graduate students have been and continue to be my first priority."
- S01, speech: "In a typical day of my life, I meet with my doctoral students discussing ideas about making new discoveries, constantly learning new things."
- S01, bio: "Mentoring my students has been one of my greatest passions and proudest accomplishments."
- S13 (2025): "Working with my doctoral students is my principal and most favorite activity,"
- S16 (2026): "It is far and away my favorite activity, to supervise my doctoral students," and "It is a privilege, in my opinion, to work with exceptional young people like the ones we have at MIT, in ability and character and aspiration. They actually make me a better scientist, and a better person."
- S17 (secondary): *The Analytics Edge* is dedicated to his "past, present and future doctoral students."
- S47 (2014): "That's an important component of my academic life, that I enjoy having very talented doctoral students." and "I enjoy it. I find it to be the major reason I enjoy academic life." (p.5). Also: "In fact, the only thing I am particularly proud of is my doctoral students." (p.18). The interview ends: "The students, really. Not me." (p.23).

**O2. What a PhD student should learn: which research matters, not only OR** {ALL} [stated · primary · S01]
> "The superficial objective is to teach them the principles of Operations Research, my area of expertise. I feel this is the minimal and not a particularly important objective. The most important thing I aspire to help them learn is why research is important and especially what research is important."

- How he sees incoming students: "When I meet them they are typically in their early twenties, they have been among the very best in their undergraduate institutions, with high aspirations, exceptional ability, various degrees of maturity, a bit inexperienced, without often a clear vision of their future and direction."

**O3. Positive reinforcement and positive energy** {ALL} [stated · primary · S01] (R3)
- Value 8, "Positive reinforcement.": "Especially with young people, it is critical to give them positive reinforcement: an encouraging word, a positive comment goes a long way to empower very talented but a bit uncertain young people to achieve their potential."
- Speech: "it has been my experience that the most important quality for determining success in life, more than IQ or EQ is positive energy, the belief that you will succeed in whatever you set out to achieve."
- Speech: "I have observed both from my personal experience as well as from the experience of my students that those that have a positive orientation towards the goals they set typically achieve them."
- S13 (2025, journalist's paraphrase): "Bertsimas emphasizes that he operates on a philosophy centered around positive thinking, high aspirations, and a can-do attitude applied to making a difference in the world for other people."

**O4. Work with exceptional people, because nobody changes the world alone** {ALL} [stated · primary · S01; S13; S16]
- Value 5, "Surround yourself with exceptional people.": "In my experience, first rate people surround themselves with other first rate people, but second rate people surround themselves with third rate people. In my experience, one cannot succeed to change the world alone. A superb team is necessary."
- S13 (2025): "It gives me the opportunity to work on things that are important with exceptional students predominantly from the Operations Research Center, and encourages my entrepreneurial spirit."

**O5. Meritocracy and open ideas: the best idea wins, whoever had it** {ALL} [stated · primary · S01, value 1 "Merit should guide decisions."]
> "MIT is by and large a meritocracy" … "In my experience, merit in the end carries the day and the best way to achieve a merit based environment is to encourage an open ideas environment. In my experience, the best idea should be followed, not whose idea it was."

**O6. Integrity and loyalty, especially towards students** {ALL} [stated · primary · S01, values 2 and 7]
> "I feel it is important to do what you say and, independent of contracts and agreements, your word should matter."
> "I have tried to be loyal to the people who are close to me, especially my students. They have entrusted their future in my hands and I take this responsibility very seriously." … "I have also experienced that loyalty is reciprocated."

**O7. Independence and judgment at the few decisions that matter** {ALL} [stated · primary · S01, values 4 and 6]
> "All my life I have tried to be in a position that I can affect my future. I have always put more weight on my own beliefs. I have also tried to form beliefs independently, judge people and ideas on their merits."
> "In my experience, there are few important decisions in life that have a first order effect in our trajectory and impact. Exhibiting good judgment during these decisions can affect our lives to the first order."

**O8. Three channels: research, education, companies; companies are the channel for scale** {ALL, AP} [stated · primary · S01] (R5)
- "The key methods I have been using are:" "Scientific research", "Education", "Building companies".
- "I believe that research and education can affect the human condition and influence a limited number of human lives." … "My observation, however, is that the limited number of scientists who have produced research that is capable of affecting the lives of millions of people created the companies themselves. It is my belief that the major way to affect the human condition in large scale is to build a successful company. From my experience, the only way to build a successful company is to inspire a team of people, create a common vision and execute the vision successfully."
- "Money is not my primary motivation. I see money as an enabler for changing the world, as a consequence of being successful in changing the world, but not as the primary objective."
- "I have been a serial entrepreneur in the last 20 years, and I intend to continue to do it with increasing intensity until I cannot do it anymore."
- Repeated in S13 ("encourages my entrepreneurial spirit"), S14 (H2O), and S42 (To Vima, 2012-12-16, English translation, secondary): "It is a professor's obligation to show a different path to young minds, by establishing a healthy economic environment with employment for them".
- The 2014 version (S47 p.15) is more explicit and hedges itself:
  - "When I realized that impacting the world is important to me, I thought the best way to impact the world on applied topics is to actually start a company. You can do consulting.... But a company, especially with a good idea, can impact the world more."
  - "The major point is that I have found that if you start a company, and you develop it, you can affect the world far more so than one individual person can. Because the only way you can affect the world with a research topic or a paper is very indirect. You influence some of the researchers, who influence other researchers."
  - He then adds at once: "This is a bit pessimistic, I don't really believe it to the same degree...." See C9.

**O9. Choose an environment that mixes disciplines, strong students and openness to founding firms** {ALL} [stated · secondary · S13, 2025]
- Journalist's paraphrase: "Bertsimas praised MIT Sloan and the Operations Research Center as ideal places for him to pursue his work, due to its interdisciplinary nature, the quality of the students, and its openness to founding firms based on breakthrough work."
- His words: "Being at MIT Sloan and at the Operations Research Center has made a material difference in my career and my life."

**O10. Running a very large group: what he stated in 2014, and what is still missing** {ALL}
- **Admissions policy** (S47 p.6): "But I have a policy: if somebody wants to work with me, I say yes, and I find the funding. The way I see it is the following: I don't try to optimize graduate students. I feel it's our obligation." The reason: "We get very talented people in our environment, and in a way we are responsible for educating them well." The limit: "On the other hand, there is an upper boundary of physical capacity, which maybe I have exceeded!"
- **Meeting format** (S47 p.13): "But that's not my style. I meet with every one of my students, one on one, once a week for about an hour. Maybe twice a week."
  - Shared company projects get a separate sub-group meeting: "In addition, I have a separate topic with each one of them." and "So this is yet another meeting with a sub-group."
  - No whole-group meeting: "But I don't meet with all my students as a group. That's not me, because one works here, another there...."
  - Time budget (p.6): "Thirty hours a week I meet with my students."
- **Students become co-authors** (S47 p.6): "And they become close colleagues. I write books with them, I write papers with them. I view it as my paramount obligation as an academic."
- **Topic ownership grows with maturity** (S47 p.13): "In the beginning, I have a higher role in choosing topics, but by the time they graduate they work in multiple topics, not only one. So later, as they become more mature, they have much more say. In a way, I try to educate them on what type of research is important."
  - What he sees as his main contribution (p.14): "In a way, the biggest contribution is not the specific topic they work, but the values of what research is important." Also: "But if you guide the young guys with this emphasis, independent of the success they have on a specific topic, the value system is affected."
- **Companies and students** (S47 p.16): "I don't involve my students before. But once a student has graduated, then I feel it is OK if the student is inclined to start a company."
- **Careers** (S47 p.19): "60% of my students become professors." "I view it as my obligation to help them on that, regardless of where they end up, whether in academia, or in industry.." He also passes on his view of large organisations (J7): "I'm not a huge fan of large organizations."
- **Resources** (S47 pp.7–8):
  - "As a result, my constraint at the moment is not money. It's time."
  - "Today 70% of my funding comes from companies and 30% from government agencies, I typically have two or three larger grants, and maybe three or four smaller grants."
  - Credibility: "Given a longer history of success, people trust that you do reasonable things." and "I would say people know that I do what I say. If I say we're going to deliver something, we deliver it."
- **Load, 2014** (S47 p.5): "So far I have graduated 59 doctoral students, and currently I am working with another 16." Later, about five new doctoral students a year (S13, journalist: "Lately he has been advising about five doctoral students per year, a remarkable number.").
- **Still missing**: how he handles 20 to 26 students at once *after* 2014, his selection criteria for students and postdocs, and his time management. These are chapters of the 2021 "Subject to" interview (S23: "Supervising many PhD students at the same time", "Criteria for selecting PhD students and postdocs", "Time management"), which was **not read** (G1). Whether the 2014 "say yes" policy still holds is unknown. A 2021 chapter on selection criteria suggests it may have changed [inferred].

---

## 3. Stated methodology by optimization domain (team.json codes)

This is for the council: these are the positions the record shows him **stating** in each domain. Domains marked as gaps should not be voiced as his stated method.

| Code | Domain | Stated positions (items) | Evidence strength | Delegations in team.json |
|---|---|---|---|---|
| LO | Linear optimization | T5 ("success … hinges on its ability to deal with large and important problems"); T8 (insight, geometry, algebra–geometry interplay); W2, W6 (economical, structure before algorithm, duality without simplex, "the art of linear optimization") | One 1997 textbook (co-authored with Tsitsiklis), plus the Dantzig test in S07 | lp-team, nonlinear-team |
| IO | Integer and mixed-integer | T8 (strong formulations, duality, algebra, "most importantly geometry"); P6 (topics that will shape the future); P2 / R9 (speed-up as "why now"; NP-hardness as "an opportunity"); E2 (heuristic warm start, MIO certificate); J2 / R12 (certificates, infeasibility as a result) | Strong: 7+ statements, 2005–2019 | minlp-team, lp-team |
| RO | Robust, adaptive, distributionally robust | T7 / R8 (tractability; computational attractiveness, modelling power, broad applicability); G4 (tunable conservatism; feasibility first); G3 (ARO as a way to solve RO; unified treatment); T5 (applications guided by Dantzig); G2 (robustness, not sparsity, explains Lasso) | Moderate: 2004 and 2011 abstracts, 2022 book page and talk title, 2026 lecture report | nonlinear-team, minlp-team, dfo-team |
| CP | Convex, conic, polynomial; moment problems | **Gap**: no stated methodology found | n/a | nonlinear-team, minlp-team |
| SD | Stochastic and dynamic; queueing | **Nearly a gap**: G6 (his PhD "combined stochastic ideas and optimization ideas", S47 p.2); the S11 blurb ("Part IV outlines the use of optimization in queueing networks."); the S23 chapter title "MSc + PhD + Reflections on Queuing Theory" (not read) | Very weak | none |
| ML | ML and statistics under an optimization lens | T4, T6 / R13, P2, P3 / R10, G1 / R11, G2, E1, E3, E4, J2, J4 | Strongest: 2015–2022, many repetitions | minlp-team, nonlinear-team, dfo-team |
| DA | Data-driven decisions, prescriptive analytics | T4 / R14 (prescription, not prediction); P1 / R6 (problems and data first); E6 (coefficient of prescriptiveness); E5 (deploy and educate); E7 (propose, then field-test); J3 (state evaluation limits); J7 (trust what the data showed); T2 (two-year horizon; 2–5 years in 2014) | Strong | all four |
| HS | Heuristic, simulation-based, derivative-free | **Mostly a gap.** S31 (1993) states only its scope: "Our goal in this review is to describe the method, its convergence and its behavior in applications." S10 places "local search over exponential neighborhoods and simulated annealing" inside integer optimization. In his later stated program heuristics are the baseline to beat (G1, E1) [inferred]. | Weak | dfo-team |
| AP | Applications as testbeds | P5 / R16 (personal experience and the D2 Hawkeye years → healthcare); P8 (build the missing data asset: the 2008 trial database); E5, E7 (deployment and hospital trials; H2O); J3; O8 / R5 (companies); G4 (Panama Canal); S07 (cases from "our own consulting experience") | Moderate | all four |

---

## 4. Failures, abandoned directions and self-corrections (as he states them)

- **F1. The 1989 proof that did not come** {LO or IO; which algorithm is not named} [stated · primary · S01]
  - "In the summer of 1989, as an assistant professor I set a goal to prove that a central algorithm in optimization was faster than previously thought possible. This would have been a major research development."
  - "We were moving houses that summer and my wife complains that I did not help in the move as the proof was coming any minute." "In the end I did not succeed in this goal, but my understanding of optimization deepened considerably."
  - Context: his first year on the faculty, at age 26 (he became assistant professor at 26 per S19). He tells it as the lesson "aim high", not as a reason to avoid risk.
- **F2. Aiming to impress** [stated · primary · S01; S47 p.14]: an early-career error ("including myself in my early years"). He corrected it over "more than a decade". In 2014 he dated the turn to "when I was in my mid-thirties, 10 years into being a professor" and admitted that in the earlier period "I did not pick topics naturally." (T3).
- **F6. First semester of teaching, 1988** [stated · primary · S47 p.5]: he defended his thesis on a Tuesday and taught the next day (paraphrase). "I taught it very fast, and the students were not happy.... I taught the way I would liked to take courses, but the students did not like it. After that, I improved."
- **F7. Not always successful** [stated · primary · S47 p.7]: "Of course we are not always successful. But if you aspire often enough, sometimes you will be successful" (J8).
- **F3. Most questions fail his test** [stated · primary · S01]: "If the answer to these questions is no, and in my experience it often is".
- **F4. A goal set against advice** [stated · primary · S01]: the four-year undergraduate degree, against his father's advice. It succeeded, and he tells it as a lesson about finding one's boundaries.
- **F5. A limited evaluation stated openly** [stated · primary · S32]: the chemotherapy-regimen models "merit further testing in a clinical trial setting".
- **Not found in this pass**: rejected papers, retracted claims, or abandoned research lines in his own words. The 2021 interview chapter "Reflections on Queuing Theory" may cover his move away from queueing; it was not read (G1).

---

## 5. Era and resource context of the statements

| Period | His position and resources (from the sources) | Statements from this period |
|---|---|---|
| 1985–1989 | NTUA diploma in 4 years (normal duration 5); MIT doctoral student in 1985; joint PhD in applied mathematics and operations research 1988, in about 3 years; thesis on vehicle routing with uncertainty; assistant professor at 26, and "the only untenured faculty at that time in the OR group" (S01, S19, S47 pp.1–5) | F1, F4, F6, G6 (told later, in S01 and S47) |
| 1997–1998 | "mid-thirties, 10 years into being a professor": the stated turn from impressing seniors to doing what he thinks is important (S47 p.14) | T3, F2 |
| 1997–2005 | Professor, then Boeing Professor (1997); theory textbooks with Tsitsiklis (1997, Athena Scientific; edition verified in Open Library) and Weismantel (2005); MBA text with Freund (2nd ed. 2004); robust optimization (S29, 2004) | T5, T7 (complexity-class sense), T8, W2, W3, W4, W6, P6 |
| 2006–2019 | ORC co-director (2006–2019); founds the MBAn program in 2013; personal losses in 2009 lead to the healthcare program; the "modern optimization lens" program (2014 onward) relies on the MIO solver and hardware speed-up he cites; Editor-in-Chief of *INFORMS Journal on Optimization* (2017–2024 per S40; he signed the first issue's "From the Editor", S37). In 2014 (S47): about 70 PhD students in the ORC (p.3); 16 current and 59 graduated doctoral students of his own (p.5); 4 courses a year (p.12); funding 70% companies and 30% government, from "two or three larger grants, and maybe three or four smaller grants" (p.8); his binding constraint is time, not money (p.7) | T1 to T4, P1 to P8, G1, G2, G6, E1 to E4, E7, J2 to J4, J7, J8, O10, R9 to R14 |
| 2019–2026 | Associate dean (2019–2025); Vice Provost for Open Learning (2024 onward); von Neumann Theory Prize and INFORMS President's Award (2019); Killian Award (2025) and Killian Lecture (2026-03-19); AI tools for online education | T2, E5, O1, O4, O9, R4; "the art of the feasible in AI" (S15) |

- **Group size**, as reported over time (current and completed PhD students):
  - 16 current, 59 completed (oral history; interview 2014-10, transcript edited by 2016; S47 p.5). The counts below come from other sources and are not on one consistent scale.
  - 18 current, 55 completed (KEPE, June 2015, S44).
  - 19 current, 53 completed (Georgia Tech 2015, S21).
  - 16 current, 57 completed (EURO 2016, S20).
  - 25 current, 76 completed (NISS, Feb 2021, S22).
  - 26 current, 81 completed (S23, Oct 2021).
  - 25 current, 103 completed (NTUA invitation, July 2025, S45).
  - 106 completed (S16, March 2026; S19, Dec 2025, which also reports more than 126 doctoral students in total).
  - 20 current, 109 completed (S01, "As of 2026, I have supervised 109 completed doctoral theses and am currently advising 20 more.").
- **Industry access**: "Consultant for over one hundred leading companies, 1991-present" (S40). He co-founded 10 analytics companies by his count in 2021–2025 (S23, S15) and 13 by 2026 (S01: "I have co-founded 13 analytics companies"). Hospital partnership: Hartford HealthCare (S14, S16).
- **Transferability caution** [inferred]: almost all statements of method date from 2014–2026. He was then a chaired professor directing a center, a degree program and later MIT Open Learning, with 16 to 26 concurrent PhD students and direct industry and hospital access. The two-year impact horizon (T2) and the company-building channel (O8) assume that kind of access. The 1997–2005 textbook statements (T8, W2, W6) come from a theory-first period with no such dependence.

---

## 6. Observed by others (context only; not used as evidence of method)

- Killian Award citation (S13, [observed · secondary]): Bertsimas, "through his remarkable intellectual breadth and accomplishments, incredible productivity, outstanding contributions to theory and practice, and educational leadership, has made enormous contributions to his profession, the Institute, and the world."
- Roger Levy, chair of the MIT faculty, introducing the 2026 lecture (S16, [observed · secondary]): "He's one of the rare individuals who has made significant contributions to both intellectual threads in the field of operations research", namely optimization and stochastic processes.
- NTUA's report of his December 2025 honorary-doctorate lecture (S19, Greek, [observed · secondary]). The Greek title is «Ένα ταξίδι από την Επιχειρησιακή Έρευνα στην Τεχνητή Νοημοσύνη και στο μέλλον»; S18 gives the English title "A Journey from Operations Research to AI and to the Future". It says he spoke of "στη διαρκή ανάγκη σύνδεσης της θεωρητικής έρευνας με την πράξη" (my translation: "the continuing need to connect theoretical research with practice"). It also reports "Κατέληξε ευχαριστώντας τους φοιτητές του που έκαναν μαζί του το όραμά του πραγματικότητα." (my translation: "He concluded by thanking his students, who made his vision a reality together with him."). These are the university's summary, not his words.

---

## Contradictions (kept, not reconciled)

- **C1. Decide before you start vs. aim beyond what you can do** (S01, both c.2015–2017).
  - The impact test must be "answerable before we do the research" (T1).
  - In the same essay he tells students to "aim high, even higher that [sic] they think they can achieve". He values the failed 1989 attempt because "my understanding of optimization deepened considerably", which is a benefit that could not be known in advance.
- **C2. Theory and complexity first (1997–2005) vs. practical tractability first (2019)**.
  - 1997: "Our general philosophy is that insight matters most" (S09). That book covers the complexity of linear optimization and the ellipsoid method, and in 1989 his own goal was a complexity-type result (F1).
  - 2004: "tractable" means the robust counterpart stays a linear optimization problem (S29).
  - 2019: "Practical tractability not polynomial solvability leads to real world impact." and "NP -hardness is an opportunity not anobstacle [sic]." (S05).
  - His own account of the change is that his principles took "more than a decade to fully crystalize" (S01).
- **C3. Data as "objective reality" vs. data as uncertain**.
  - 2019: "Data represent an objective reality; models only exist in our imagination." (S05).
  - 2016: "The only objective reality is data, which itself may be incomplete and of questionable quality" (S08).
  - His robust-optimization program starts from data that "changes" and uncertain parameters (S29).
  - [inferred tension]
- **C4. "ML is inherently linked to optimization not probability theory" (S05, 2019) vs. his own probability work**. His homepage still lists Applied Probability (queueing theory, stochastic processes) among his principal research interests (S01), and he co-wrote a 2022 queueing-theory book (S11). In 2014 he described his own thesis as a combination: "So I combined stochastic ideas and optimization ideas." (S47 p.2, G6). [inferred tension between a stated principle and his practice and earlier statement; note 03 should check it]
- **C5. Size of the MIO speed-up**, papers of 2015–2017:
  - "200 billion" for 1990–2014 (S24).
  - "450 billion" for 1991–2015 (S27, S26, S20).
  - "800 billion" for "the last 25 years" (S25).
  - The figures are not reconciled across papers.
- **C6. Hartford length of stay**:
  - "from 5.67 days to five days" (S14, his words, May 2025).
  - "from 5.38 days to 4.93 days" (S16, the reporter's account of his March 2026 lecture).
  - Different baselines and endpoints; whether these are different periods or hospitals is not stated.
- **C7. Open ideas vs. weighting his own beliefs** (S01, same essay):
  - "the best idea should be followed, not whose idea it was"
  - "I have always put more weight on my own beliefs."
- **C8. Time horizon**:
  - "Not in 40 years, but 2 to 5 years." (S47 p.6, 2014, for applied work).
  - "Not in 50 years, but in two years." (S13, 2025).
  - Both the number and the counter-example differ.
  - Separately, there is a tension between these short horizons and "Research can change the world." and "aim to change the world" (S01). [inferred tension: near-term measurable impact vs. world-changing ambition]
- **C9. Companies vs. papers, hedged in the same breath** (S47 p.15, 2014):
  - "the only way you can affect the world with a research topic or a paper is very indirect"
  - followed at once by "This is a bit pessimistic, I don't really believe it to the same degree...."
  - The firmer later form is in S01: "the major way to affect the human condition in large scale is to build a successful company".
- **C10. Taking every student vs. surrounding yourself with first-rate people**:
  - 2014: "if somebody wants to work with me, I say yes, and I find the funding" and "I don't try to optimize graduate students." (S47 p.6).
  - S01, value 5: "first rate people surround themselves with other first rate people, but second rate people surround themselves with third rate people."
  - The 2014 statement assumes MIT's admissions have already selected ("We get very talented people in our environment"). The 2021 interview has a chapter on "Criteria for selecting PhD students and postdocs" (S23, not read). [inferred tension]

---

## Gaps (what this pass could not find or read)

- **G1. No talk transcripts.** yt-dlp is not installed in this environment, so `scripts/download_subtitles.sh` cannot run. A direct request for YouTube captions was refused by the session's permission policy and was not retried. Nothing was saved under `references/sources/talks/`. Talks most likely to hold stated methodology, all listed on S02 unless noted:
  - "Subject to: Dimitris Bertsimas" (2021-10-28, 74:37; https://www.youtube.com/watch?v=cifspW4gLwA). Chapters include "MSc + PhD + Reflections on Queuing Theory", "On writing the first book", "Main research contributions", "On OR being a well-kept secret", "Supervising many PhD students at the same time", "Criteria for selecting PhD students and postdocs", "Time management", "Future work". Highest priority for a later pass.
  - "Dimitris Bertsimas receives John Von Neumann Prize" (2019; https://www.youtube.com/watch?v=83RpSXhmgyw).
  - "Transdisciplinary Fundamental Research Problems" (MIT NSF workshop, 2016; https://www.youtube.com/watch?v=neEbn_M2JD0).
  - Keynote at the Analytics for a Better World Practitioner's Fellowship launch (2022; https://www.youtube.com/watch?v=zingj2KQVY8).
  - "Math4DS Live NO.32" (2022; https://www.youtube.com/watch?v=gkAtEEhGhKA).
  - "Robust and Adaptive Optimization: A Tractable Approach…" (2022; https://www.youtube.com/watch?v=RBbgKMpgrDg).
  - The NTUA honorary-doctorate lecture (Dec 2025, Greek; embedded video id 0iK0HfggQEU on S19).
  - "Universal AI and the Future of Universities" (NTUA, 2025-07-09; https://www.youtube.com/live/uw6v8KKC16s, from S45).
  - The 2026 Killian Lecture: no video located.
- **G2. Book prefaces not read.** Only the publisher's blurbs and "Educational Philosophy" sections (S05 to S12) were read, not the prefaces of the ML-lens book, RAO (so the Dantzig quote is unconfirmed), AE, AEH or the queueing book. The PDF of *The Analytics Edge in Healthcare* is free for academic use, but only through a request form, which was not submitted.
- **G3. Editorials not read.** "From the Editor" (IJOO 1(1), 2019, S37) and "Machine Learning and Optimization: Introduction to the Special Issue" (IJOO 1(2), 2019, S38) are likely to state his editorial criteria for an optimization paper [inferred]. Both were identified through Crossref; the publisher returned HTTP 403, and no open copy was found on MIT DSpace.
- **G4. Podcasts.** The two "Data Made to Matter" episodes (MIT Sloan, 2017) were available only as episode descriptions (S41).
- **G5.** The Analytics for a Better World site (analyticsbw.org) did not resolve, so the movement's statement of purpose was not read.
- **G6. Writing, refereeing, talks.** No essay, blog post or lecture of his on how to write a paper, respond to referees or give a talk was found. Layer 6 rests on book blurbs and abstract framing.
- **G7. Group practice.** Partly filled by the 2014 oral history (S47): one-to-one weekly meetings, topic negotiation, funding kept separate, companies only after graduation (O10, P7). Still missing: anything after 2014 on selection criteria and time management (the S23 chapters), and anything in his words on handling negative results, rejected papers or referee critiques (see the "Not found" line in §4).
- **G8. Domains with no stated method**: CP (moment problems, semidefinite optimization), SD (queueing, stochastic networks), HS (simulated annealing beyond the 1993 review's scope sentence), and within AP finance and air transportation.
- **G9. Dating.** The Internet Archive was offline on 2026-10-28, so the homepage essay (S01) could not be dated from archived copies and older versions of his homepage could not be checked.
- **G10. Search budget.** The WebSearch allowance (5 calls) was used up. Further Greek-press interviews (Kathimerini, To Vima) were seen only through the secondary site S42.

---

## Sources

One line each: id, title, author, date, URL or DOI, primary/secondary, and what was read. Accessed 2026-10-28.

- **S01** "About Me" and "My Philosophy: Path, philosophy and aspirations", including "Life Stories" (excerpt of a speech to a graduating class). Dimitris Bertsimas, personal homepage, undated (c. 2015–2017 by internal evidence). https://dbertsim.mit.edu/ (moved from https://www.mit.edu/~dbertsim/). **Primary**; read in full.
- **S02** "Media" page (lectures, interviews, panels, award videos, podcasts). Bertsimas homepage. https://dbertsim.mit.edu/media. **Primary** (list of titles and dates).
- **S03** "Published Books" page. Bertsimas homepage. https://dbertsim.mit.edu/published-books. **Primary**.
- **S04** "Teaching" page (courses taught). Bertsimas homepage. https://dbertsim.mit.edu/teaching. **Primary**.
- **S05** *Machine Learning Under a Modern Optimization Lens*, D. Bertsimas and J. Dunn, Dynamic Ideas 2019; publisher page incl. "Philosophical principles of the book". https://www.dynamic-ideas.com/books/machine-learning-under-a-modern-optimization-lens. **Primary**; preface not read.
- **S06** *Robust and Adaptive Optimization*, D. Bertsimas and D. den Hertog, Dynamic Ideas 2022; publisher page. https://www.dynamic-ideas.com/books/robust-and-adaptive-optimization. **Primary**.
- **S07** *Data, Models, and Decisions: The Fundamentals of Management Science*, 2nd ed., D. Bertsimas and R. Freund, Dynamic Ideas 2004; publisher page ("Educational Philosophy", "Distinguishing Characteristics"). https://www.dynamic-ideas.com/books/ecbcnthsfb6hnzfdezpw0aldtvl9yr. **Primary**.
- **S08** *The Analytics Edge*, D. Bertsimas, A. K. O'Hair and W. R. Pulleyblank, Dynamic Ideas 2016; publisher page ("Educational Philosophy"). https://www.dynamic-ideas.com/books/kgsni67q285zmpdit17ix1cwbnuqac. **Primary**.
- **S09** *Introduction to Linear Optimization*, D. Bertsimas and J. N. Tsitsiklis, Athena Scientific 1997 (ISBN 1886529191, checked in Open Library) and Dynamic Ideas 2008; publisher page ("Educational Philosophy", "Distinguishing Characteristics"). https://www.dynamic-ideas.com/books/q3ggobj67w504tsa95ae456yvndd2d. **Primary**.
- **S10** *Optimization over Integers*, D. Bertsimas and R. Weismantel, Dynamic Ideas 2005; publisher page. https://www.dynamic-ideas.com/books/x0g7bsm2nvnl6j7ebqodcrhsvlgbm7. **Primary**.
- **S11** *Queueing Theory: Classical and Modern Methods*, D. Bertsimas and D. Gamarnik, Dynamic Ideas 2022; publisher page. https://www.dynamic-ideas.com/books/queueing-theory. **Primary**.
- **S12** *The Analytics Edge in Healthcare*, D. Bertsimas, A. Orfanoudaki and H. Wiberg, Dynamic Ideas 2025; book site. https://analyticsedge-healthcare.github.io (publisher page https://www.dynamic-ideas.com/books/the-analytics-edge-in-healthcare). **Primary**; book body not read.
- **S13** "Dimitris Bertsimas receives the 2025-2026 Killian Award", Peter Dizikes, MIT News, 2025-05-14. https://news.mit.edu/2025/dimitris-bertsimas-receives-killian-award-0514. **Secondary** (with direct quotes).
- **S14** "Q&A: A roadmap for revolutionizing health care through data-driven innovation", Sara Feijo, MIT News, 2025-05-05. https://news.mit.edu/2025/qa-roadmap-revolutionizing-health-care-through-data-driven-innovation-0505. **Primary** (his answers in a Q&A).
- **S15** "Dimitris Bertsimas named vice provost for open learning", Sara Feijo, MIT News, 2024-08-08. https://news.mit.edu/2024/dimitris-bertsimas-named-vice-provost-open-learning-0808. **Secondary** (with direct quotes).
- **S16** "On algorithms, life, and learning" (report on the 54th Killian Lecture, 2026-03-19), Peter Dizikes, MIT News, 2026-03-23. https://news.mit.edu/2026/algorithms-life-learning-killian-lecture-dimitris-bertsimas-0323. **Secondary** (with direct quotes from the lecture).
- **S17** "Faculty Impact" (Bertsimas profile), MIT Operations Research Center, undated: internal evidence c. 2016, but it calls him "former co-director", which implies an edit after 2019. https://orc.mit.edu/faculty-impact. **Secondary** (with direct quotes).
- **S18** Faculty directory page (bio, honours news), MIT Sloan. https://mitsloan.mit.edu/faculty/directory/dimitris-bertsimas. **Secondary**.
- **S19** "Αναγόρευση του Καθηγητή Δημητρίου Μπερτσιμά σε Επίτιμο Διδάκτορα…", NTUA news, December 2025 (ceremony 2025-12-22). https://ntua.gr/el/news/item/5100-anagorefsi-tou-kathigiti-dimitriou-bertsima-se-epitimo-didaktora-tis-sxolis-ilektrologon-mixanikon-kai-mixanikon-ypologiston-tou-ethnikoy-metsoviou-polytexneiou. **Secondary** (Greek).
- **S20** "Machine Learning and Statistics via a modern optimization lens", IFORS Distinguished Lecture abstract, EURO 2016 Poznań (lecture 2016-07-04; date from S18). https://euro2016.euro-online.org/index.html%3Fp=763.html. **Primary** (speaker abstract).
- **S21** "Multivariate statistics and machine learning under a modern optimization lens", 2015 Distinguished Scholarship Lecture, Georgia Tech, event page created 2015-01-21. https://hg.gatech.edu/node/366361. **Primary/secondary** (abstract partly in the third person, edited by the host).
- **S22** "Machine Learning under a Modern Optimization Lens", NISS webinar series "Mathematical Foundations of Data Science", 2021-02-05, abstract. https://www.niss.org/node/5391. **Primary** (speaker abstract).
- **S23** "Subject to: Dimitris Bertsimas", s.t. (Subject to) interview series, YouTube, 2021-10-28 (date as listed on S02). https://www.youtube.com/watch?v=cifspW4gLwA. **Secondary**: only the uploader's description and chapter list were read; the interview itself was not.
- **S24** Bertsimas, King and Mazumder, "Best subset selection via a modern optimization lens", *Annals of Statistics* 44(2):813–852, 2016. DOI 10.1214/15-AOS1388; arXiv 1507.03133. **Primary**; abstract read.
- **S25** Bertsimas and Dunn, "Optimal classification trees", *Machine Learning* 106(7):1039–1082, 2017. DOI 10.1007/s10994-017-5633-9. **Primary**; abstract read (Springer page).
- **S26** Bertsimas and King, "Logistic regression: from art to science", *Statistical Science* 32(3):367–384, 2017. DOI 10.1214/16-STS602. **Primary**; abstract read (Crossref).
- **S27** Bertsimas and King, "OR Forum—An algorithmic approach to linear regression", *Operations Research* 64(1):2–16, 2016. DOI 10.1287/opre.2015.1436. **Primary**; abstract read (OpenAlex).
- **S28** Bertsimas and Kallus, "From predictive to prescriptive analytics", *Management Science* 66(3):1025–1044, 2020. DOI 10.1287/mnsc.2018.3253; arXiv 1402.5481. **Primary**; abstract read.
- **S29** Bertsimas and Sim, "The price of robustness", *Operations Research* 52(1):35–53, 2004. DOI 10.1287/opre.1030.0065. **Primary**; abstract read (OpenAlex).
- **S30** Bertsimas, Brown and Caramanis, "Theory and applications of robust optimization", *SIAM Review* 53(3):464–501, 2011. DOI 10.1137/080734510. **Primary**; abstract read.
- **S31** Bertsimas and Tsitsiklis, "Simulated annealing", *Statistical Science* 8(1):10–15, 1993. DOI 10.1214/ss/1177011077. **Primary**; abstract read (OpenAlex).
- **S32** Bertsimas, O'Hair, Relyea and Silberholz, "An analytics approach to designing combination chemotherapy regimens for cancer", *Management Science* 62(5):1511–1531, 2016. DOI 10.1287/mnsc.2015.2363. **Primary**; abstract read.
- **S33** Bertsimas, Kallus, Weinstein and Zhuo, "Personalized diabetes management using electronic medical records", *Diabetes Care* 40(2):210–217, 2017 (online 2016-12-05). DOI 10.2337/dc16-0826. Metadata only.
- **S34** Bertsimas, Johnson and Kallus, "The power of optimization over randomization in designing experiments involving small samples", *Operations Research* 63(4):868–876, 2015. DOI 10.1287/opre.2015.1361. **Primary**; abstract read.
- **S35** Bertsimas, Pauphilet and Van Parys, "Sparse regression: scalable algorithms and empirical performance", *Statistical Science* 35(4):555–578, 2020. DOI 10.1214/19-STS701; arXiv 1902.06547. **Primary**; abstract read.
- **S36** Bertsimas, Delarue, Jaillet and Martin, "The price of interpretability", arXiv 1907.03419, 2019. **Primary**; abstract read.
- **S37** Bertsimas, "From the Editor", *INFORMS Journal on Optimization* 1(1):1, 2019. DOI 10.1287/ijoo.2019.0011. **Not read** (HTTP 403); identified via Crossref.
- **S38** Bertsimas, "Machine Learning and Optimization: Introduction to the Special Issue", *INFORMS Journal on Optimization* 1(2):91, 2019. DOI 10.1287/ijoo.2019.0017. **Not read**; identified via Crossref.
- **S39** Bertsimas and Copenhaver, "Characterization of the equivalence of robustification and regularization in linear and matrix regression", *European Journal of Operational Research* 270(3):931–942, 2018. DOI 10.1016/j.ejor.2017.03.051. Metadata only (no abstract available).
- **S40** Curriculum Vitae, Dimitris Bertsimas, PDF dated 2025-12-31 (the homepage "Download CV" Dropbox link; the dbertsim.mit.edu/pdfs/cv.pdf link returned 404). **Primary** (appointments, awards, industrial experience, journal service).
- **S41** "Data Made to Matter" podcast (MIT Sloan): "On a Mission in Medicine: Using Data for Personalized Treatment" (2017-05-25) and "Education in the Age of Analytics" (2017-06-26). Apple Podcasts episode pages. **Secondary**; descriptions only.
- **S42** "Teaching in MIT since 26 years old", ellines.com, 2024-05-30, quoting *Kathimerini* (2012-12-30) and *To Vima* (2012-12-16) in English translation. https://www.ellines.com/en/teaching-in-mit-since-26-years-old/. **Secondary** (translated quotes).
- **S43** University of Athens, booklet for the honorary doctorate (Rector's address), 2022-07-05. https://hub.uoa.gr/wp-content/uploads/2022/07/mdimop_Bertsimas_anag_teyxos.pdf. **Secondary**; consulted, no statements by Bertsimas.
- **S44** KEPE press release, 2015-06-16, announcing the Distinguished Lecture "From Predictive to Prescriptive Analytics" (2015-06-24). https://www.kepe.gr/wp-content/uploads/2015/06/08_KE%CE%A0%CE%95_d_bertzima2.pdf. **Secondary**.
- **S45** NTUA invitation to the lecture "Universal AI and the Future of Universities", 2025-07-09. https://www.mech.ntua.gr/files/announcements/2025/07/omilia-bertsimas.pdf. **Secondary**.
- **S46** Wikipedia, "Dimitris Bertsimas" (page source), read 2026-10-28. https://en.wikipedia.org/wiki/Dimitris_Bertsimas. **Tertiary** (used only as a lead to S42).
- **S47** "Interview with Dimitris Bertsimas", Sloan Oral History Project (interviewers George Roth and Robert B. McKersie), interview 2014-10-24. Transcript PDF of 23 pages, created 2016-06-06, © MIT 2016, CC BY-NC 4.0. MIT Libraries Distinctive Collections, https://hdl.handle.net/1721.3/199289 (PDF: https://dome.mit.edu/server/api/core/bitstreams/4d4f0948-bc17-458f-89d9-361debb7fce4/content). Local copy saved by research agent 04 in this run: `../sources/talks/2014-10-24_sloan-oral-history-interview.md`. **Primary** (his spoken words; transcript edited after the interview). Read in full; every quote and page number above was checked against my own pdftotext extraction of the original PDF.
