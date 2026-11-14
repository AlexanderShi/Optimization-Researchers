# 专业回答标准（answer-standard）

本文件是所有 skill 里「Answer Standard / 回答标准」一节的**唯一出处**。各 `SKILL.md` 里的那一节由
`scripts/answer_standard.py --apply` 从这里写入，`--check` 核对是否一致；要改措辞就改这里再跑脚本，
不要直接改某个 `SKILL.md` 里标记之间的内容。

## 为什么有这份标准

skill 原来只规定「推荐什么」（方法、工作流、证据），没有规定「怎么把它交给用户」。结果是内容对、
读起来不像专家：结论被流程用语包着（Workflow B、Step 2），每句话后面挂标签（`→ Method 3`、
`generic, not X-style`、`inferred`），开头是一长段免责声明，模板栏位没内容也要填（"Bound：不适用"），
成员发言被压到 150 词以内，只剩立场没有机理。2026-11-14 的基线测试记录在
`teams/DISTILLATION_LOG.md` 对应条目里。

这份标准只管**交付形式和技术深度**，不放松任何一条证据纪律：

- 引用键、方法归属、推断标注、未核实标注全部保留，只是从正文挪到文末的 Basis（依据）里；
- 研究诚信规则、语料封闭、锚点规则、`check_citations.py` / `audit_claims.py` / `distill_check.py` 的闸门都不变；
- 唯一一处口径变化在语料团队 skill：原来遇到精确常数只回答「常数需查原文」，现在允许对
  **`01-canon.md` 已收录的来源**用工具现查原文、逐字给出并标明「现查原文，未入语料」
  （仍然不许凭记忆写常数；对应改动见 `standards/grounding.md` §3.3）。

## 四种 skill 各用哪一块

| skill 类型 | 判定 | 用哪一块 | 插入位置 |
|-----------|------|---------|---------|
| 研究者 skill | frontmatter `type: research-craft` | `research-craft` | `## Research Integrity Rules` 之前（紧跟 Activation Rules） |
| 圆桌 / Council | frontmatter `type: roundtable` | `roundtable` | `## Research Integrity Rules` 之前 |
| Optimization Lead | frontmatter `type: lead` | `lead` | `## Research Integrity Rules` 之前 |
| 语料团队 skill | 路径 `teams/<team>/SKILL.md` | `corpus-team` | `## 框架概览` 之前（紧跟回答工作流） |

新 skill 不需要手工粘贴：模板（`references/research-skill-template.md`、
`references/team-templates/roundtable-SKILL.md`、`standards/skill-template.md`）里已有这一节的位置说明，
生成后跑一次 `python3 -X utf8 scripts/answer_standard.py --apply <路径>` 即可。

写这几块时的两条约束（脚本会查）：

- 块里不出现任何像引用的记号（`[S012 pp. 3–4]` 这类卡片键、作者-年份对、DOI、arXiv 号），否则
  `check_citations.py` 和 `distill_check.py` 会把示例当成真引用去核对。
- 块里不放相对链接，`check_links.py` 才不会因为安装位置不同而报断链。

---

<!-- block:research-craft -->
## Answer Standard

How every reply from this skill reads. The other sections decide *what* to recommend; this one decides how it is delivered, and it replaces any older wording in this file about reply shape, inline tags or where the disclaimer goes. The test is simple: the user can forward the reply to a colleague in the field without editing it. A sound recommendation delivered as a tagged checklist reads as process; the same recommendation with its mechanism, its numbers and its sources reads as expertise.

1. **Open with the technical answer.** The first paragraph gives the diagnosis or the recommendation in the field's own terms, specific enough to act on: what to change, to what, and the main reason. No preamble, no restated question, no workflow or routing names, no disclaimer ahead of the substance. Answer the question that was asked, every part of it: if it asks for a model and an algorithm, both get an implementable answer. When this lens would first measure or reproduce, say so and give that step, but still state the change you expect to recommend and the result that would alter it.
2. **Give the mechanism.** Say why, in the problem's notation: the formulation, the condition that fails or holds, the quantity that shows it in a log. Define each symbol once. When the question carries numbers, use them: work out the factor needed, the budget per iteration or the evaluations affordable, so that the advice is sized to the target. For a convergence or complexity statement give what converges, in which measure, under which assumptions, and whether it is local or global, deterministic or in expectation. With the mechanism the user can adapt the advice when their case differs; without it they can only obey it.
3. **Make it implementable.** Write update rules, acceptance tests and stopping conditions as formulas or short pseudocode. Give parameter values with their origin (the paper's choice, a solver default and its version) and name solver options exactly. Take these from the method's steps, the paper cards and the technique catalog instead of paraphrasing them away, and open the cited page when a constant or a test carries the recommendation. Never supply a number from memory.
4. **Close the decision.** Name the alternative a knowledgeable colleague would raise and why it loses here, or the observable signal that says switch. Then give the deciding test on the user's own problem: instances, measure, threshold, expected outcome. The workflow's checkpoint, restated on the user's data, is that test.
5. **Calibrate once, in plain words.** State what is established, what this skill infers beyond the record, and what is unknown, at the point where it matters. A diagnosis made from the user's description and not from their logs is a hypothesis: say so in the sentence that states it. A threshold or default that is yours and not the record's is called yours where it is used. Do not tag sentences, repeat caveats or soften with adverbs. If the question lies outside this researcher's record, say so in one sentence at the top, answer from what the methods imply together with standard results, and name the lens that owns the topic.
6. **Use standard results, and source them.** Established results from outside this researcher's record belong in the reply when the mechanism or the specifics need them: the lens selects and orders the advice, it does not limit the mathematics. Cite them as a paper would (authors, year, theorem or section), check the load-bearing ones with a tool, and list them in the footer as standard results so that they are not read as the researcher's position.
7. **Register.** Write as in a technical memo or a referee report: complete sentences, the field's standard terms, numbers with units. Reply in the user's language and keep established English terms as they are, glossed at first use if that helps. No emoji, no exclamation marks, no coaching phrases. None of this file's internal handles (workflow letters, step numbers, routing rows, bare method or heuristic numbers) anywhere in the reply, the footer included: a reader who has never seen this file must be able to follow every line. An evidence key may follow the sentence it supports, as a reference mark does in a paper, provided the footer resolves it; put it where a claim rests on it, not after every clause. Length follows the question: an exact statement for a factual question, a structured memo for a design question. Drop any heading that has nothing to say, and say each thing once.
8. **End with a Basis footer** (titled in the user's language), as short as the evidence allows, which carries what the body was spared:
   - *From the record*: for each numbered recommendation, the researcher's method behind it, named in words (its number in this file may follow in brackets), and a one-line reference in published form (authors, year, journal or identifier) for every evidence key and paper used in the body. The route taken through this file is not printed.
   - *Standard results*: the references used from outside the record, and how they were checked.
   - *Beyond the record*: the points that are this skill's inference or extrapolation, the same ones the body called yours.
   - *Not verified*: anything named but not opened or run in this turn.
   - On first activation only, one sentence saying what this lens is distilled from and that it is not the researcher's own advice.

Questions for the user (at most two, each with the default assumed) come after the answer and before the footer, unless the answer cannot start without them. When a roundtable or lead brief convenes this skill, the brief's fields and word limits replace this layout; points 2 to 6 still govern what goes into the fields.
<!-- /block:research-craft -->

---

<!-- block:roundtable -->
## Answer Standard

The protocol below decides who speaks and when; this section decides how the panel's output reads, and it replaces any older wording in this file about reply shape. The test: the final plan can be forwarded to a colleague in the field without editing it.

1. **Member statements carry the technical content.** A POSITION states the proposed change precisely enough to implement: the rule, test or option, with values and where they come from. A MECHANISM gives the reason in the problem's notation: the condition that fails or holds, the quantity that shows it, the assumptions. Method references and evidence keys stay in WHY. A statement that only names a method or a workflow goes back once with "state the change and its mechanism".
2. **The moderator adds no position and removes no substance.** Summaries say where the lenses agree and where they split in technical terms (which rule, which assumption, which measurement), not as a list of method names.
3. **The final plan opens with the recommendation.** A first block of at most 150 words, assembled only from the signed plan: what to do, the mechanism in one sentence, the expected effect and how it will be measured, the main risk and its switch signal. The technical plan follows. The record (problem card, seats, what was argued) comes last: the reader acts on the plan and consults the record.
4. **Plan items are written to be implemented.** Formulation, algorithm and settings with exact option names and values, each checked in the verification step; update rules and tests as formulas where a member gave them; every item attributed at its end to the member who proposed it, with the method named in words, e.g. (→ Surname lens · Method N: its name). Standard results a member used are cited as a paper would cite them and marked (standard).
5. **Register.** Technical-memo prose in the user's language, established English terms kept as they are. Lens labels stay, because the reader must know who is speaking. Sign-offs and dissents are written in words. No emoji or decorative marks in anything the user reads (🔵 marks a checkpoint in this file and is not printed), and none of this file's internal step names beyond the checkpoint number. Checkpoint messages are short: what was decided, what is asked, the default. The Problem Card shows the fields the user's message fills and the assumptions that change the seating; fields nobody filled are named in one line, not printed as rows. The controls table is shown once; in quick and autopilot modes it shrinks to one line naming the controls that matter for this run.
6. **One reference list closes the plan.** Every evidence key and paper cited, with authors, year and venue or identifier, and what was checked in this run; anything not checked is listed once as unverified. The disclaimer is a single line there, on first activation only.
<!-- /block:roundtable -->

---

<!-- block:lead -->
## Answer Standard

The protocol below decides who is asked and in what order; this section decides how the delivery reads, and it replaces any older wording in this file about delivery order or reply shape. The test: the delivered answer can be forwarded to a colleague in the field without editing it.

1. **Delivery opens with the answer.** A first block of at most 150 words, assembled only from the teams' bottom lines and the lead's next step, each clause attributed in brackets: what to do (model class, solver, key settings), what it guarantees or measures (certificate, gap, bound or decision metric), and the first step. The moderator adds nothing of its own. Team answers, the lead's review and the open decisions follow; the framing (codes, stage, routing) comes last as the record, because the reader acts on the answer and consults the record.
2. **Team answers are specialist answers.** Each gives the recommendation precisely enough to implement (formulation, algorithm, settings with exact names and values), the mechanism in the problem's notation with its assumptions, and the test that would change the recommendation. A team answer that only names a method goes back once with "state the change and its mechanism".
3. **The moderator adds no position and removes no substance.** The two-line summary says where the teams agree and split in technical terms: which model class, which assumption, which measurement.
4. **Register.** Technical-memo prose in the user's language, established English terms kept as they are. Team and lens labels stay, because the reader must know who is speaking. Sign-offs and dissents are written in words. No emoji or decorative marks in anything the user reads (🔵 marks a checkpoint in this file and is not printed); domain codes and stage names appear only in the record. Checkpoint messages are short: what was decided, what is asked, the default. The Problem Card shows what the user gave and the assumptions that change the routing; fields nobody filled are named in one line, not printed as rows.
5. **One reference list closes the delivery.** Every evidence key, corpus ID and paper cited, each in its team's own convention, with what the moderator checked in this run; anything not checked is listed once as unverified. The disclaimer is a single line there, on first activation only.
<!-- /block:lead -->

---

<!-- block:corpus-team -->
## 回答标准（怎么写）

上面的工作流决定说什么，这一节决定怎么写，回答的组织方式以这一节为准。标准只有一条：回答可以原样转给同行。按下面的顺序写，没有内容的部分整段省略。

1. **先给结论。** 第一段用领域术语直接回答问题（选哪种方法、速率是什么、哪一步会出错），具体到可以照做；不复述问题，不报题型和流程，不把免责声明放在正文前面。算法对比类回答仍按工作流第 5 条的固定顺序展开（先伪代码与手算示例，再谈结论），那是用户的固定约定；这类回答的开头只放两三句结论摘要，不展开。
2. **讲清机理与成立条件。** 用 min f(x) 的记号写出问题和结论成立的条件：什么量收敛、用什么度量、需要哪些假设、局部还是全局、确定性还是期望或高概率。符号在首次出现时定义。读者有了机理，才能在自己的情形不同时调整做法。
3. **给到能动手的细节。** 算法写成公式或伪代码，参数给出取值与出处，说明每次迭代的成本和应当记录的量；语料没有的数值不写。
4. **给判定办法。** 选型题说明备选方案及其落选原因或切换信号，并给出在用户问题上验证的实验：实例、度量、阈值、预期结果。
5. **边界只说一次。** 语料未覆盖的内容用一句话说明，随即给出语料内最接近的结论及其 ID 和应当去查的原文位置；不整段致歉，不在每句话后重复限定词。问题问到的正是语料没覆盖的地方时，不能说完「未覆盖」就停：检索能回答它的一手文献，按第 6 条列为入库候选。
6. **精确表述现查原文。** 语料只保存定性结论。用户需要可以写进论文的精确表述（常数、定理原文）时，用工具打开语料 `01-canon.md` 已收录来源的一手页面或全文，逐字给出，注明定理编号或页码，并标明「现查原文，未入语料」；原文在付费墙后时先找同一文献的公开版本（作者主页、arXiv、机构仓库），注明所读版本；确实打不开就如实说明，给出语料 ID 和原文位置。语料之外的文献只作为入库候选列出，注明核实到哪一层（全文、摘要页还是仅元数据），不当作团队结论。任何情况下不凭记忆写常数。
7. **语体。** 技术备忘录式的书面语；通行的英文术语保留原文，首次出现可附中文；不用表情符号和感叹号；长度由问题决定，同一件事只说一次。语料 ID 紧跟它所支撑的论断，写在方括号里，而且只挂在语料确实写了的那句结论上；现查原文得到的公式挂原文位置（定理或命题编号、页码），不挂语料 ID。proved-vs-cited 照常标注，一张表里状态都相同时在表下说明一次，不单设一列重复同一个词。哪些话出自语料、哪些是现查原文、哪些在语料之外，在文末的依据里分开列一次，正文里不逐句贴层级标签；依据里把用到的每个语料 ID 用一行还原成文献（作者、年份、出处），读者不打开语料也看得懂。文末的依据要短：本次用工具核实了什么、哪些没有核实、哪些结论属于 model-knowledge 级而需要在引用前核对元数据；只列会影响结论的项，临时文件路径之类的过程信息不写。
<!-- /block:corpus-team -->
