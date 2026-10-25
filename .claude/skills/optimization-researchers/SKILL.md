---
name: optimization-researchers
description: |
  本仓库（Optimization-Researchers）的蒸馏路由：DFO Team / NLP Team（及 MINLP 等新团队）的两条自包含流水线。
  (1) 封闭语料 → 团队级 skill（DISTILL.md，质量门 G1–G7 由 scripts/distill_check.py + distill_audit.py 执行）；
  (2) team-kit → 逐人研究者 skill 与圆桌（TEAM-KIT.md）。
  触发：「蒸馏 X 加入 DFO team / NLP team」「加研究者」「加成员」「搭一个新团队」「重跑蒸馏」「更新语料」
  「重新蒸馏 skill」「强化 / 加强 X 的蒸馏」「强化蒸馏技能」「质量门」「抽审」「研究者 skill」「圆桌」，
  以及在本仓库内任何提到 DISTILL、team-kit、product/、teams/ 的扩展请求。
  所需的一切都在本仓库内，不读、不依赖 nuwa-skill / nvwa-skill 仓库。
---

# Optimization-Researchers · 蒸馏路由

本仓库自带两条独立流水线。先按用户要的**产物**分流，再读对应入口文档，不要跳过入口文档直接动手。
动手前读 `RUNBOOK.md`（分支/worktree、用量窗口、Windows 编码、常见坑——每条都是实跑踩过的）。

| 用户要的 | 流水线 | 入口 | 产物 |
|---------|--------|------|------|
| 团队级 skill（「DFO Team / NLP Team 怎么看…」，每条事实带语料 ID） | **语料蒸馏** | `DISTILL.md` → `standards/distill-gates.md` | `teams/<team>/SKILL.md` + `CLAIM-AUDIT.md` |
| 往语料里加一位研究者 / 一篇文献 / 一条结果 | **语料维护** | `README.md`「语料维护」+ `standards/researcher-extraction.md` + `standards/grounding.md` | `teams/<team>/01-canon.md`、`04-results.md`、`researchers/<name>.md`，`distill_check.py --lint` 0 ✗，然后重跑 DISTILL.md |
| 某位研究者本人的研究方法 skill（导师模式）、或把他加进圆桌团队 | **team-kit · 加成员** | `TEAM-KIT.md` → `references/research-team-playbook.md` 第八节 | `product/<team>/<member>/` |
| 「强化 / 加强 X 的蒸馏」（X 是已在 product/ 里的研究者） | **team-kit · 升档** | playbook 第五节（T3.1–T3.8 深读档）或 T4 增量 | 同上，深读档多出 cards/、07–10、technique-catalog |
| 新领域的研究顾问团（几位研究者 + 圆桌） | **team-kit · 新团队** | `TEAM-KIT.md` → playbook 第一至七节 | `product/<new-team>/`（常配一份 `teams/<new-team>/` 封闭语料 + 团队级 skill） |
| 「强化蒸馏技能本身」「质量门」「抽审」（改的是流程不是某个团队） | **协议维护** | `standards/distill-gates.md`、`scripts/distill_check.py`、`scripts/distill_audit.py`；kit 侧 `references/claim-audit.md`、`check_citations.py`、`audit_claims.py` | 改脚本/标准后在两队语料上跑一遍，记入 LOG |

分不清时问一句：「要的是**团队口吻、事实可追溯到语料 ID** 的 skill，还是**某位研究者本人的研究方法**
skill？」前者走语料蒸馏，后者走 team-kit。team-kit 加成员 / 强化成员时再问一句**档位**：轻量档（T1 + 带全体
重跑 T2，约 500–1,600 万子 agent token）还是深读档（T3.1–T3.8，约 1,200–2,500 万 token、跨 2–3 个用量窗口）——
用户历来自己选，不替他定。

## 语料蒸馏 / 语料维护（DISTILL.md）

- 两条铁律（README）：**语料封闭**——蒸馏期间禁 WebSearch/WebFetch，skill 里每条事实带
  `[DFO-S*]` / `[NLP-R*]` 等 ID，语料没有的写进诚实边界；**锚点规则**——没有出处定位的声明不进语料库。
- 新增研究者档案走 `standards/researcher-extraction.md`（三重验证、矛盾处理、信息不足处理）并过
  `standards/grounding.md` 的验证层级；档案落 `teams/<team>/researchers/<name>.md`。
- 质量门 G1–G7 全过才交付（`standards/distill-gates.md`）：
  - `python3 -X utf8 scripts/distill_check.py teams/<team>`：语料 lint + G1（ID 闭包、含跨队）+ G2（作者-年份在
    canon）+ G3（结果表结构、语料外数字）+ G4（诚实边界四项、语料版本戳是本仓库提交且在当前历史上、语料自此未变）
    + G5（05 的 F、04 的 R、03 的 H 逐条在）+ G6（00-charter 试答题小节）。0 ✗；每条 ⚠ 改掉或在 LOG 说明。
  - G6 真的去答 `00-charter.md`「试答题」的四类题，答案记 LOG。
  - `scripts/distill_audit.py teams/<team> --sample --n 20` → **另一个**零上下文 agent 只读审计包 `.md` 判定 →
    `--report` 写 `teams/<team>/CLAIM-AUDIT.md`；unsupported = 0，partial 收窄后换 seed 再抽。
- 语料版本戳 = 语料最后一次改动的提交（先提交语料再写 skill），头部契约与诚实边界两处一致。
- 产物 `teams/<team>/SKILL.md` 只复制这一个文件到 `~/.claude/skills/<team>/`，`distill_check.py --installed` 核对。
- 每次蒸馏在 `teams/DISTILLATION_LOG.md` 顶部记一条（语料版本、范围、✗/⚠ 处理、G6 试答、G7 计数、模型）。

## team-kit（TEAM-KIT.md）

- kit 文档里的「[skill目录]」「女娲仓库根目录」= **本仓库根目录**；文档里写的「SKILL.md 特殊场景 >
  研究Skill / 研究团队Skill」指 `references/nuwa-SKILL.md`（冻结副本），不要去找别的仓库。
- 从仓库根运行脚本：`python3 -X utf8 scripts/<脚本> product/<team>[/<member>]`（Windows 控制台
  需要 utf8 模式，或设 `PYTHONUTF8=1`）。脚本只用标准库；工作流预览用 Node。
- 加成员：先写进 `product/<team>/team.json`（Scholar id 从 DBLP / ORCID / 主页取，Scholar 搜索需登录；找不到留空）
  → `python3 scripts/new_team.py product/<team>/team.json --add-member <slug>` → 只为他跑 T1
  （`scripts/workflows/team-base-skills.js`）→ 带全体成员重跑 `team-layer.js`（混合档团队用 `deep_tier: true`）
  → 深读档再跑 T3 → `team-integrate.js`。闸门：`quality_check.py --mode research` 12/12、`check_links.py` 0 断链、
  `team_check.py` 0 failed。深读档另加两道证据闸门：`check_citations.py` 0 problems（引用闭包：每条
  `[card S012 pp. …]` 指向存在、读过、页码在范围内的卡片；替代版本写成 `[ID TR pp. …]`）和 `audit_claims.py`
  声明抽审 unsupported = 0（零上下文 agent 判定，协议 `references/claim-audit.md`）。
- 新团队：`python3 scripts/new_team.py --init <slug> --field "…" --members "A;B;C"` →
  `python3 scripts/new_team.py product/<slug>/team.json [--base-tier]` → 按 playbook T1–T4 走。
- 版权材料（PDF/全文 txt/private/）由根 `.gitignore` 忽略，不要 `git add -f`。
- 完成后在 `teams/DISTILLATION_LOG.md` 记一条，注明是 team-kit 产物（不带语料 ID、不受 G1–G7 约束）。

## 运行纪律（细节在 RUNBOOK.md）

- 每个任务独立分支 + worktree，从 `main` 开；主 checkout 可能停在别的长期分支上。做完 ff 合入 main，推送与否问用户。
- 提交信息不带任何 Claude 署名 / `Co-Authored-By` 行。
- 深读档跨多个用量窗口：分批跑读卡；被打断先 `git diff` 再用 `dims` / `only` 补缺；`resumeFromRunId` 跨会话不命中缓存。
- Windows：`python3 -X utf8`；tesseract 要手动加进 PATH；带反斜杠的 heredoc 写成文件再跑。

## 两条流水线的边界

- `teams/<team>/SKILL.md` 只以 `teams/` 语料为依据；`product/` 里的研究者 skill 各自带证据台账。
  两边互不引用、互不抄写。要把 team-kit 蒸馏出的研究者纳入语料，必须另按
  `standards/researcher-extraction.md` 写档案并过锚点规则。
- 本仓库不依赖外部 nuwa-skill / nvwa-skill 仓库：不要读 `~/.claude/skills/nuwa-skill`，不要 clone
  别的仓库来补文件。缺什么就在本仓库内补并记录。
