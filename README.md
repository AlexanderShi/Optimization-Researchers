# Optimization-Researchers

两个虚拟研究团队的**自包含蒸馏语料库**：

- **DFO Team** — 无导数优化（derivative-free / zeroth-order / blackbox optimization）
- **NLP Team** — 非线性规划（nonlinear programming：一阶/二阶方法、凸分析、随机梯度）

目的：仅凭本 repo（不联网、不依赖 nuwa-skill 仓库、不依赖模型参数记忆）就能蒸馏出
可用的团队 skill。这是对此前蒸馏失败的直接修正——之前的 team 靠网搜+记忆生成，
频繁胡说；本 repo 把「允许 team 说的话」全部落盘、全部带锚点，蒸馏时**语料库里
没有的就不许说**。

## 与 nuwa-skill 的关系

无依赖。nuwa 的「纯本地语料模式 + 主题Skill 变体」思想被吸收进 [DISTILL.md](./DISTILL.md)，
但蒸馏协议、模板、质量门都在本 repo 内自带。删除 nuwa-skill 不影响本 repo 使用。

## 目录结构

```
README.md                 本文件
DISTILL.md                蒸馏协议（自包含，从这里开始）
standards/
  grounding.md            接地标准：锚点规则、验证层级、数学声明纪律
  skill-template.md       团队 skill 的输出模板
teams/
  dfo-team/               DFO Team 语料（00-charter … 05-failure-modes）
  nlp-team/               NLP Team 语料（同构）
skills/                   蒸馏产物落盘处（再复制到 ~/.claude/skills/）
```

每个团队目录六个文件，编号即阅读顺序：

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
1. 读 DISTILL.md
2. 按协议蒸馏 → skills/<team>/SKILL.md
3. 复制到 ~/.claude/skills/<team>/
```

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
- 改完语料后重跑 DISTILL.md 即可得到更新版 skill（蒸馏是纯函数：语料 → skill）。

## 本地证据源（已用于交叉验证）

- `C:\Users\sr881\repos\autoresearch-optimization\research_runs\deep-momentum-vs-dfo-v2\sources.json`
  （13 条带 DOI/URL 的确定性一手来源）
- `C:\Users\sr881\repos\optimization-paper-collection\`（锚点规范 `_EXTRACT.md` +
  Nesterov 1983 完整机器区条目）
- `C:\Users\sr881\repos\autoresearch-optimization\docs\reviews\2026-07-25-professional-research-audit.md`
  （失败教训的权威记录：只验证论文存在≠验证论文内容）
