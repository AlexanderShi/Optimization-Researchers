# 声明→证据抽样审计（claim audit，研究Skill · 深读档）

> 研究Skill 的第三道证据闸门。前两道是确定性的：摘录逐字（`verify_card_quotes.py`）、引用闭包（`check_citations.py`：
> 每条 `[card S012 pp. 20–21]` 指向真实存在、确实读过、页码在范围内的卡片）。它们证明不了 SKILL.md 那句话是卡片
> **真正支持**的——「真论文 + 编造内容」正是此前团队 skill 胡说的机制（见 `standards/grounding.md` 第 5 节）。
> 本审计补这一层：把声明和它所引的卡片配成对，交给一个零上下文的 agent 判定蕴含关系。
>
> 铁律同 [fidelity-scorecard.md](fidelity-scorecard.md)：**写 skill 的 agent 和审计的 agent 必须是两个**。SkillLens
> （arXiv 2605.23899）实证 LLM 自评 skill 质量准确率仅 46.4%，接近随机。

## 一、什么时候跑

| 时机 | 规模 | 目的 |
|---|---|---|
| T3.6 汇总之后、T3.8 整合之前（每位成员） | 20 条（默认） | 交付闸门：unsupported = 0 |
| T4 增量之后（只抽本次增量改动的文件：`--files SKILL.md` 外加 09） | 10–20 条 | 增量没把卡片写走样 |
| 用户对某个方法起疑 | `--files` 指到相关文件、调大 `--n`，或手工挑 k | 定点复核 |

20 条是**抽查**：每位成员的 SKILL.md 约 300–500 条带页码引用，抽样只能证明「这份 skill 的声明大体是卡片撑得住的」，
不能证明每一条都对。想严就 `--n 40`，或换 `--seed` 再抽一轮。

## 二、步骤

```bash
S=${TMPDIR:-/tmp}/<team>-scratch; M=<slug>; T=product/<team>
# 1. 抽样 → 审计包（声明 + 所引卡片全文 + digest 的 read_level / quotes + INDEX 页数 + 审计简报）
python3 scripts/audit_claims.py $T/$M --sample --n 20 --seed 1 --out $S/audit-$M.json --list
# 2. 交给一个新 agent：只给它审计包的路径，让它按包里的 brief 判定，写 $S/verdicts-$M.json
#    （prompt 见第三节；它不读 SKILL.md、不读调研笔记、不上网、不用自己的领域知识补证据）
# 3. 写报告（追加到 <M>/references/research/10-claim-audit.md），按判定给退出码
python3 scripts/audit_claims.py $T/$M --report $S/verdicts-$M.json --packet $S/audit-$M.json
```

审计 agent 看到的每一项：`claim`（引用之前的那个分句）、`cite`（ID、页码、是否版本引用）、`card.text`（这位成员
读得最深的那张卡片的全文，`cards/<批次>.md` 里 `### <ID>` 到下一张卡片）、`card.batch_header`（批次意图与
文件页码 ↔ 印刷页码的对应）、`card.read_level`、`card.pages_in_index`、`card.quotes`（已逐字核对的摘录）。
证据层是**卡片**，不是论文原文：原文 `txt/` 不进 git，新容器里没有；卡片的摘录已过 `verify_card_quotes.py`，
页码引用已过 `check_citations.py`，所以「卡片 → SKILL.md」这一跳是剩下的未检环节。

## 三、审计 agent 的 prompt（可照抄）

```
You are the AUDITOR in a two-agent check of a research-craft skill. Your only input is this packet:
<绝对路径>/audit-<slug>.json
Read packet["brief"] and follow it. For each object in packet["items"], judge whether the cited paper card
(card.text, card.batch_header, card.read_level, card.pages_in_index, card.quotes) supports the claim at the cited
pages. Verdict: supported / partial / unsupported / uncheckable, as the brief defines them; one sentence of reason
each, naming where in the card the support is or what differs.
Hard rules: open no other file, no web search, no outside knowledge of the researcher or the field; when the card
does not cover the cited pages or topic, answer uncheckable rather than guessing.
Write exactly one JSON file <绝对路径>/verdicts-<slug>.json:
{"auditor": "<model>", "date": "<YYYY-MM-DD>", "verdicts": [{"k": 1, "verdict": "...", "reason": "..."}, ...]}
one entry per item in order; reasons without newlines. Reply with the counts per verdict and the k of anything
not "supported".
```

跨模型更好：有 Codex / 其他模型可用时，让它当审计 agent（同一个包、同一个 prompt）。

## 四、判定与处理

| 判定 | 含义 | 处理 |
|---|---|---|
| supported | 卡片在所引页码 / 维度上写了这件事，声明没有超出卡片 | — |
| partial | 有关联内容，但声明比卡片更强、更具体、更一般；或把卡片标为 variant / contradiction 的内容当成了 evidence | 人看一眼：收窄声明，或补上真正支持它的卡片引用 |
| unsupported | 卡片没有这个内容，或内容相反 | **必须处理**：改声明或改引用；改完重跑 `check_citations.py`，并用新 `--seed` 再抽一轮 |
| uncheckable | 卡片没覆盖所引页码或主题（如摘要级卡片、页码对不上） | 看是不是引错了卡片或版本（版本引用写 `[ID TR pp. …]`，见 paper-reading-card.md 第四节） |

`--report` 的退出码：unsupported > 0 → 1。报告按日期追加一节，不改旧节；「To act on」列表列出 unsupported 与 partial。
审计 agent 也会错：它的 reason 要指得出卡片里的位置，指不出的判定按 partial 对待，人再看。

## 五、实测（dfo-team，2026-10-10）

首次在 `product/dfo-team/katya-scheinberg` 上跑：20 条（seed 1，池 269 条带页码引用，全部命中 full 级卡片），
结果记在该成员的 `references/research/10-claim-audit.md` 和 `teams/DISTILLATION_LOG.md`。
