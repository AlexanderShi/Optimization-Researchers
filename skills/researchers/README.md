# 研究者 Skill（逐人蒸馏产物）

本目录是 **DFO Team / NLP Team 的逐人研究者 skill**，与上一级 `skills/dfo-team/`、
`skills/nlp-team/` 的团队级 skill 并列。每个研究者一个可直接安装的 skill 目录，
外加一个圆桌（roundtable）skill 负责召集成员。

| 目录 | 团队 | 内容 |
|------|------|------|
| `dfo-team/` | DFO Team（无导数优化） | Powell、Conn、Scheinberg、Vicente、Audet 五位 + `dfo-roundtable` |
| `nonlinear-team/` | **NLP Team**（非线性规划；源目录名保留为 nonlinear-team） | Curtis、Nocedal、Wright、Ye、Wächter、Gill、Toint、Gould、Fletcher、Nesterov 十位 + `nonlinear-roundtable` |

每个团队目录下的 `README.md`、`DEEP-READING.md`、`team.json` 是团队说明与成员清单，
原样保留。

## 来源与出处层级

- **来源**：AlexanderShi/nvwa-skill 仓库 `product/dfo-team`、`product/nonlinear-team`，
  同步自提交 `eb012fa`（内容与 `ff2ef35`，2026-09-28 相同），2026-10-09 同步，
  文件逐字节一致（539 个文件）。
- **蒸馏方式**：nuwa team-kit（网络调研 + 逐篇论文卡片 + 证据台账），标注日期
  `researched: 2026-09-27`。每位研究者的证据链在其
  `references/research/09-evidence-ledger.md`，论文卡片在 `references/research/cards/`。
- **与本仓库语料的关系**：这批 skill **不是**按 `DISTILL.md` 的封闭语料协议蒸馏的，
  其事实性声明不带 `[DFO-S*]` / `[NLP-R*]` 语料 ID，出处以各自台账为准。
  团队级 skill（`skills/<team>/SKILL.md`）仍以 `teams/` 语料为唯一依据；两者互不引用。
  若要把某位研究者纳入语料，按 `standards/researcher-extraction.md` 另写
  `teams/<team>/researchers/<name>.md`（目前已有 Scheinberg、Duchi）。

## 安装

把某个研究者目录整体复制到 `~/.claude/skills/<name>/`（例如
`skills/researchers/dfo-team/michael-powell/` → `~/.claude/skills/michael-powell/`）。

圆桌 skill 按**同级目录**解析成员（`../<member>/SKILL.md`），其次才找
`~/.claude/skills/<name>/`。因此要么把整个团队目录一起安装，要么把圆桌与成员
分别装到 `~/.claude/skills/` 下。`nonlinear-roundtable` 对 `dfo-roundtable` 的
链接是 `../../dfo-team/dfo-roundtable/SKILL.md`，仅在本仓库目录结构内有效。
