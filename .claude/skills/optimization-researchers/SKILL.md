---
name: optimization-researchers
description: |
  本仓库（Optimization-Researchers）的蒸馏路由：DFO Team / NLP Team 的两条自包含流水线。
  (1) 封闭语料 → 团队级 skill（DISTILL.md）；(2) team-kit → 逐人研究者 skill 与圆桌（TEAM-KIT.md）。
  触发：「蒸馏 X 加入 DFO team / NLP team」「加研究者」「加成员」「搭一个新团队」「重跑蒸馏」
  「更新语料」「重新蒸馏 skill」「研究者 skill」「圆桌」，以及在本仓库内任何提到 DISTILL、team-kit、
  product/、teams/ 的扩展请求。所需的一切都在本仓库内，不读、不依赖 nuwa-skill / nvwa-skill 仓库。
---

# Optimization-Researchers · 蒸馏路由

本仓库自带两条独立流水线。先按用户要的**产物**分流，再读对应入口文档，不要跳过入口文档直接动手。

| 用户要的 | 流水线 | 入口 | 产物 |
|---------|--------|------|------|
| 团队级 skill（「DFO Team / NLP Team 怎么看…」，每条事实带语料 ID） | **语料蒸馏** | `DISTILL.md` | `teams/<team>/SKILL.md` |
| 往语料里加一位研究者 / 一篇文献 / 一条结果 | **语料维护** | `README.md`「语料维护」+ `standards/researcher-extraction.md` + `standards/grounding.md` | `teams/<team>/01-canon.md`、`04-results.md`、`researchers/<name>.md`，然后重跑 DISTILL.md |
| 某位研究者本人的研究方法 skill（导师模式）、或把他加进圆桌团队 | **team-kit · 加成员** | `TEAM-KIT.md` → `references/research-team-playbook.md` 第八节 | `product/<team>/<member>/` |
| 新领域的研究顾问团（几位研究者 + 圆桌） | **team-kit · 新团队** | `TEAM-KIT.md` → playbook 第一至七节 | `product/<new-team>/` |

分不清时问一句：「要的是**团队口吻、事实可追溯到语料 ID** 的 skill，还是**某位研究者本人的研究方法**
skill？」前者走语料蒸馏，后者走 team-kit。

## 语料蒸馏 / 语料维护（DISTILL.md）

- 两条铁律（README）：**语料封闭**——蒸馏期间禁 WebSearch/WebFetch，skill 里每条事实带
  `[DFO-S*]` / `[NLP-R*]` 等 ID，语料没有的写进诚实边界；**锚点规则**——没有出处定位的声明不进语料库。
- 新增研究者档案走 `standards/researcher-extraction.md`（三重验证、矛盾处理、信息不足处理）并过
  `standards/grounding.md` 的验证层级；档案落 `teams/<team>/researchers/<name>.md`。
- 改完语料后重跑 DISTILL.md Phase 0–5，质量门 G1–G6 全过才交付；产物写 `teams/<team>/SKILL.md`，
  再复制到 `~/.claude/skills/<team>/`。
- 每次蒸馏在 `teams/DISTILLATION_LOG.md` 顶部记一条（语料版本、范围、质量门结果、试答）。

## team-kit（TEAM-KIT.md）

- kit 文档里的「[skill目录]」「女娲仓库根目录」= **本仓库根目录**；文档里写的「SKILL.md 特殊场景 >
  研究Skill / 研究团队Skill」指 `references/nuwa-SKILL.md`（冻结副本），不要去找别的仓库。
- 从仓库根运行脚本：`python3 -X utf8 scripts/<脚本> product/<team>[/<member>]`（Windows 控制台
  需要 utf8 模式，或设 `PYTHONUTF8=1`）。脚本只用标准库；工作流预览用 Node。
- 加成员：先写进 `product/<team>/team.json` → `python3 scripts/new_team.py product/<team>/team.json
  --add-member <slug>` → 只为他跑 T1（`scripts/workflows/team-base-skills.js`）→ 带全体成员重跑
  `team-layer.js` → 深读档再跑 T3 → `team-integrate.js`。闸门：`quality_check.py --mode research`
  12/12、`check_links.py` 0 断链、`team_check.py` 0 failed。
- 新团队：`python3 scripts/new_team.py --init <slug> --field "…" --members "A;B;C"` →
  `python3 scripts/new_team.py product/<slug>/team.json [--base-tier]` → 按 playbook T1–T4 走。
- 版权材料（PDF/全文 txt/private/）由根 `.gitignore` 忽略，不要 `git add -f`。
- 完成后在 `teams/DISTILLATION_LOG.md` 记一条，注明是 team-kit 产物（不带语料 ID、不受 G1–G6 约束）。

## 两条流水线的边界

- `teams/<team>/SKILL.md` 只以 `teams/` 语料为依据；`product/` 里的研究者 skill 各自带证据台账。
  两边互不引用、互不抄写。要把 team-kit 蒸馏出的研究者纳入语料，必须另按
  `standards/researcher-extraction.md` 写档案并过锚点规则。
- 本仓库不依赖外部 nuwa-skill / nvwa-skill 仓库：不要读 `~/.claude/skills/nuwa-skill`，不要 clone
  别的仓库来补文件。缺什么就在本仓库内补并记录。
