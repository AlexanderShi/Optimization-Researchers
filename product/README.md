# product/ · 逐人研究者 Skill（team-kit 产物）

[English](README.en.md) | 中文

本目录是各优化团队（六个队，见下表）的**逐人研究者 skill**，由仓库根的 team-kit
（`scripts/` + `references/`，见 [TEAM-KIT.md](../TEAM-KIT.md)）生产与维护。
与 `teams/<team>/SKILL.md`（按 DISTILL.md 从封闭语料蒸馏的团队级 skill）并列，两条流水线互不引用。

| 目录 | 团队 | 内容 | 档位 |
|------|------|------|------|
| `dfo-team/` | DFO Team（无导数优化） | Powell、Conn、Scheinberg、Vicente、Audet 五位 + `dfo-roundtable` | 深读档（356 篇全文精读、59 篇部分，1139 条摘录逐字核对；见 `DEEP-READING.md`） |
| `nonlinear-team/` | **NLP Team**（非线性规划；源目录名保留为 nonlinear-team） | Curtis、Nocedal、Wright、Ye、Wächter、Gill、Toint、Gould、Fletcher、Nesterov、Robinson 十一位 + `nonlinear-roundtable` | 混合档：Curtis 深读档（2026-10-10）、Nocedal 深读档（2026-10-17）；其余九位轻量档（公开来源调研，未做全文深读） |
| [`lp-team/`](lp-team/README.md) | **LP Team**（线性规划引擎） | Qi Huangfu、John J. H. Forrest、Robert E. Bixby 三位 + `lp-roundtable` | 轻量档（公开来源调研，未做全文深读） |
| [`milp-team/`](milp-team/README.md) | **MILP Team**（混合整数线性规划：求解器里的分支切割、分解、MIP 基准测试） | Ambros M. Gleixner、Marco E. Lübbecke、Tobias Achterberg、Matteo Fischetti 四位，LP Team 的 Forrest、Bixby 作客座 + `milp-roundtable` | 深读档（2026-11-28：343 篇全文精读、8 篇部分，827 条摘录逐字核对；见 `DEEP-READING.md`；T1 的封存题验证做在深读之前，之后没有重跑）；客座 Forrest、Bixby 按 LP Team 的轻量档 |
| [`minlp-team/`](minlp-team/README.md) | **MINLP Team**（混合整数非线性与全局优化） | Grossmann、Leyffer、Sahinidis、Misener、Burer、Dey 六位 + `minlp-roundtable` | 混合档：Leyffer、Sahinidis、Misener、Burer、Dey 深读档；Grossmann 的深读停在 T3.2（全文已取，还没有卡片），按轻量档检查 |
| [`optimization-council/`](optimization-council/README.md) | **Optimization Council**（优化理事会：Bertsimas 召集并主持 LP、NLP、DFO、MINLP 四队的跨队讨论；总入口 optimization-lead 另把 MILP 问题分派给 MILP Team） | Dimitris Bertsimas 一位（召集人；技能按九个优化领域分为九个领域文件：LO、IO、RO、CP、SD、ML、DA、HS、AP）+ [`optimization-lead`](optimization-council/optimization-lead/SKILL.md)（总入口：他按领域与阶段门定性，把问题分派给该管的队，再审各队答复）+ `council-roundtable`（跨队讨论）；四队成员作为客座代表团入座，须与四队一并安装 | 深读档：Bertsimas（2026-10-29 深读并写九个领域文件，2026-10-31 写领域图；413 篇全文精读、59 篇部分，1125 条摘录逐字核对，另读 21 项书籍公开部分；见 `DEEP-READING.md`）；客座四队按本队档位（DFO 深读档；NLP 混合档；MINLP 混合档，五位深读；LP 轻量档）。首次会话记录：[`first-session-2026-10-31.md`](optimization-council/first-session-2026-10-31.md)（议题「精确性的代价」，四队十位代表，计划 v2 待你在检查点 4 批准） |

每个团队目录下的 `README.md`、`DEEP-READING.md`、`team.json` 是团队说明与成员清单，
`python3 scripts/team_status.py product/<team>` 可随时重算进度与覆盖表。

## 来源与出处层级

- **来源**：AlexanderShi/nvwa-skill 仓库 `product/dfo-team`、`product/nonlinear-team`，
  同步自提交 `eb012fa`（内容与 `ff2ef35`，2026-09-28 相同），2026-10-09 同步，
  文件逐字节一致（539 个文件）。目录名与 nvwa 相同，因此团队文档内的
  `product/...` 路径在本仓库内原样有效。
  之后在本仓库内用 team-kit 做的改动记在 `teams/DISTILLATION_LOG.md`：Curtis 深读档（条目 (10)），
  Daniel P. Robinson 以轻量档加入 nonlinear-team（条目 (11)，2026-10-17，不来自 nvwa 同步），
  Nocedal 深读档（条目 (12)，2026-10-17）。
- **蒸馏方式**：team-kit（网络调研 + 逐篇论文卡片 + 证据台账），标注日期
  `researched: 2026-09-27`。每位研究者的证据链在其
  `references/research/09-evidence-ledger.md`，论文卡片在 `references/research/cards/`。
- **与本仓库语料的关系**：这批 skill **不是**按 `DISTILL.md` 的封闭语料协议蒸馏的，
  其事实性声明不带 `[DFO-S*]` / `[NLP-R*]` 语料 ID，出处以各自台账为准。
  团队级 skill（`teams/<team>/SKILL.md`）仍以同目录的语料为唯一依据。
  若要把某位研究者纳入语料，按 `standards/researcher-extraction.md` 另写
  `teams/<team>/researchers/<name>.md`（目前已有 Scheinberg、Duchi）。

## 安装

把某个研究者目录整体复制到 `~/.claude/skills/<name>/`（例如
`product/dfo-team/michael-powell/` → `~/.claude/skills/michael-powell/`）。

圆桌 skill 按**同级目录**解析成员（`../<member>/SKILL.md`），其次才找
`~/.claude/skills/<name>/`。因此要么把整个团队目录一起安装，要么把圆桌与成员
分别装到 `~/.claude/skills/` 下。`nonlinear-roundtable` 对 `dfo-roundtable` 的
链接是 `../../dfo-team/dfo-roundtable/SKILL.md`，仅在本仓库目录结构内有效。

有客座的团队（`team.json` 里有 `guests`：别队的成员坐进本队圆桌，他的 skill 只在他的主队
有一份，本队目录下没有他的文件夹）：在本仓库里，圆桌到 `../../<home>/<slug>/SKILL.md`
找客座，他的研究笔记和卡片也在那个文件夹里。装到 `~/.claude/skills/` 时，除了本队各目录，
还要从同一个 checkout 把每位客座的目录一起复制过去
（bash：`cp -r product/<home>/<slug> ~/.claude/skills/`；
PowerShell：`Copy-Item -Recurse product\<home>\<slug> "$HOME\.claude\skills\"`）。
本地有被 git 忽略的全文 PDF、`txt/` 时，只复制 `git ls-files -- <目录>` 列出的文件。
团队 README 的两段安装命令（bash 和 PowerShell）里都有这几行：每支主队的复制行上面单独一行注释
`# guest(s) from the <主队 title>: …, see product/README.md`，指回这里；复制行本身不带注释。
少装了谁，圆桌会说缺了谁，然后不带他继续。

装好之后，只让入口占 skill 列表：在 `~/.claude/settings.json` 的 `skillOverrides` 里把每位研究者设为
`"name-only"`（列出名字、不带描述），总入口 `optimization-lead`、五个队的圆桌、`council-roundtable` 和语料团队
`dfo-team`、`nlp-team` 保留描述。Claude Code 把每个已装 skill 的描述放进每一轮的上下文，列表有字符预算
（`skillListingBudgetFraction`，默认为上下文窗口的 1%），超出后从调用最少的 skill 开始去掉描述；30 位研究者的
描述合计约 25,000 字符（2026-11-26），会把入口的描述挤掉。圆桌和总入口按路径读成员文件，不受影响；要单独用某位
研究者，走圆桌的 `solo <成员>`，或直接输入 `/<成员 slug>`。新加一位研究者，就在 `skillOverrides` 里加一行。

## 版权材料不进仓库

仓库根 `.gitignore` 已按 kit 的规则忽略 `product/**/references/sources/` 下的
PDF/PS/DjVu/EPUB、`papers/txt/` 和 `private/`（README 除外）。跑
`scripts/acquire_fulltexts.py` 等下载脚本后不要 `git add -f`。
