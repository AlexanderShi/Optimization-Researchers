# Optimization-Researchers

两个虚拟研究团队的**自包含蒸馏语料库**：

- **DFO Team** — 无导数优化（derivative-free / zeroth-order / blackbox optimization）
- **NLP Team** — 非线性规划（nonlinear programming：一阶/二阶方法、凸分析、随机梯度）

目的：仅凭本 repo（不联网、不依赖 nuwa-skill 仓库、不依赖模型参数记忆）就能蒸馏出
可用的团队 skill。这是对此前蒸馏失败的直接修正——之前的 team 靠网搜+记忆生成，
频繁胡说；本 repo 把「允许 team 说的话」全部落盘、全部带锚点，蒸馏时**语料库里
没有的就不许说**。

## 与 nuwa-skill 的关系

不依赖外部 nuwa-skill 仓库，两条流水线都在本 repo 内自带：

- **团队级 skill**：nuwa 的「纯本地语料模式 + 主题Skill 变体」思想被吸收进
  [DISTILL.md](./DISTILL.md)，蒸馏协议、模板、质量门全在本 repo。
- **逐人研究者 skill**：nuwa 的研究 Skill / 研究团队工具链（team-kit）已整体内置
  （`scripts/`、`references/`、`product/`，逐字节同步自 AlexanderShi/nvwa-skill `eb012fa`），
  入口见 [TEAM-KIT.md](./TEAM-KIT.md)。

删除 nuwa-skill 不影响本 repo 使用。

## 目录结构

```
README.md                 本文件
DISTILL.md                蒸馏协议（自包含，从这里开始）
RUNBOOK.md                两条流水线共用的运行纪律：分支/worktree、用量窗口、Windows、常见坑
standards/
  grounding.md            接地标准：锚点规则、验证层级、数学声明纪律
  researcher-extraction.md 研究者档案提炼标准（nuwa 三重验证适配版）
  skill-template.md       团队 skill 的输出模板
  distill-gates.md        质量门 G1–G7 的机械部分（distill_check.py）与 G7 声明抽审协议（distill_audit.py）
teams/
  dfo-team/               DFO Team 语料（00-charter … 05-failure-modes、researchers/）
    SKILL.md              由这份语料蒸馏出的团队级 skill（带语料 ID；复制到 ~/.claude/skills/dfo-team/）
    CLAIM-AUDIT.md        G7 声明→语料抽审记录（按日期追加；产物，不是语料）
  nlp-team/               NLP Team 语料（同构）+ SKILL.md + CLAIM-AUDIT.md
  DISTILLATION_LOG.md     每次蒸馏的记录（语料版本、质量门结果、试答）
TEAM-KIT.md               逐人研究者 skill 流水线（team-kit）入口
references/               team-kit 文档与模板：playbook、研究提炼框架、研究 skill 模板、
                          team-templates/；nuwa-SKILL.md 为冻结的 nuwa 根 skill 副本
scripts/                  team-kit 脚本：发表全表、全文、读卡、台账、团队状态；workflows/ 为 T1–T4；
                          本仓库新增 check_citations.py（引用闭包）、audit_claims.py（声明抽审，协议 references/claim-audit.md）；
                          语料线的 distill_check.py（lint + G1–G6 + 版本戳）、distill_audit.py（G7 抽审，协议 standards/distill-gates.md）
product/                  team-kit 产物：逐人研究者 skill + 圆桌（dfo-team、nonlinear-team = NLP Team）
.claude/skills/
  optimization-researchers/ 项目级 skill：在本仓库内把蒸馏请求分流到 DISTILL.md / TEAM-KIT.md
```

每个团队目录六个语料文件，编号即阅读顺序（`SKILL.md`、`CLAIM-AUDIT.md` 是蒸馏产物，不算语料）：

| 文件 | 内容 |
|------|------|
| `00-charter.md` | 团队定位：回答什么问题、边界在哪 |
| `01-canon.md` | 正典文献表（带 ID、验证层级、本地交叉验证出处） |
| `02-schools.md` | 流派：共识框架 + 各家分歧 |
| `03-heuristics.md` | 决策启发式（方法选型、基准测试纪律、报告规范） |
| `04-results.md` | 关键定理/速率（带假设、proved-vs-cited、结果 ID） |
| `05-failure-modes.md` | 已知胡说陷阱清单（蒸馏出的 skill 必须内置这些禁区） |
| `researchers/*.md` | 具名研究者档案（可选，每人一档）：身份、学派位置、核心贡献、方法论立场，全部 verified-web/local 锚定 |

## 快速开始

```
团队级 skill（封闭语料）                     逐人研究者 skill / 圆桌（team-kit）
1. 读 DISTILL.md；distill_check.py --lint    1. 读 TEAM-KIT.md → references/research-team-playbook.md
2. 按协议蒸馏 → teams/<team>/SKILL.md        2. 加成员：team.json + scripts/new_team.py --add-member；
3. distill_check.py 0 ✗ + distill_audit.py     新团队：scripts/new_team.py --init
   抽审 unsupported 0（G1–G7）              3. 按 T1–T4 跑 scripts/workflows/，产物在 product/<team>/
4. 只复制这个 SKILL.md 到                   4. team_check.py / check_citations.py / audit_claims.py
   ~/.claude/skills/<team>/；--installed 核对
```

做任何一条之前先读 [RUNBOOK.md](./RUNBOOK.md)（分支与 worktree、用量窗口、Windows 编码、常见坑）。

两条流水线所需的一切（协议、模板、脚本、语料、已蒸馏产物）都在本仓库内；在本仓库启动
Claude Code 时项目级 skill `optimization-researchers` 会自动把蒸馏/扩展请求分流到对应入口。

## 两条铁律

1. **语料封闭**：蒸馏期间禁止 WebSearch/WebFetch；skill 里每条事实性声明必须
   可追溯到语料 ID（如 `[DFO-S2]`、`[NLP-R4]`）。语料没有的，写进诚实边界，
   不准补。
2. **锚点规则**（源自 `optimization-paper-collection/_EXTRACT.md`，见
   [standards/grounding.md](./standards/grounding.md)）：没有出处定位的声明
   不进语料库；不确定的元数据宁可标 `需核对` 也不编造。

## 语料维护

- 新增文献：在 `01-canon.md` 加一行（分配新 ID、标验证层级），相关结论进
  `04-results.md`。
- 发现语料错误：直接改正并在该条目加 `勘误:` 注记——语料库是活的。
- 改完语料先跑 `python3 -X utf8 scripts/distill_check.py teams/<team> --lint`（ID 重复、04 缺状态行、
  引用了不存在的 ID 都在这一步抓），再重跑 DISTILL.md 得到更新版 skill（蒸馏是纯函数：语料 → skill）。
  语料改了而 skill 没重蒸馏时，`distill_check.py` 会在 `stamp` 一项报 skill 过期。

## 本地证据源（已用于交叉验证）

- `C:\Users\sr881\repos\autoresearch-optimization\research_runs\deep-momentum-vs-dfo-v2\sources.json`
  （13 条带 DOI/URL 的确定性一手来源）
- `C:\Users\sr881\repos\optimization-paper-collection\`（锚点规范 `_EXTRACT.md` +
  Nesterov 1983 完整机器区条目）
- `C:\Users\sr881\repos\autoresearch-optimization\docs\reviews\2026-07-25-professional-research-audit.md`
  （失败教训的权威记录：只验证论文存在≠验证论文内容）
