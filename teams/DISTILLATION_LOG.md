# 蒸馏记录

## 2026-10-10 (8) · team-kit 研究 Skill 蒸馏：补两道证据闸门（引用闭包 + 声明抽审）

- 范围：team-kit（逐人研究者 skill 流水线）的质量门；`teams/` 语料与团队级 SKILL.md 未改动，G1–G6 不涉及
- 缺口：T3 深读的证据链里，摘录有 `verify_card_quotes.py` 逐字核对，但 SKILL.md、账本、技术目录、学生模式文件和
  圆桌里成百上千条 `[card S012 pp. 20–21]` 式引用没有任何机械闸门——卡片是否存在、页码是否落在读过全文的卡片上、
  是否超过文件页数，都没人查；四重验证也只是 agent 的口头断言，没有一条声明被回头对照过它所引的卡片
- 新增 `scripts/check_citations.py`（引用闭包，确定性）：扫 SKILL.md、`references/*.md`、`research/01–09`（07 除外，
  它是 digest 的投影）；✗ = unknown-id / no-card / page-on-unread / page-range / version / roundtable；⚠ = skip-mention /
  roundtable-bare；`--methods` 报每个核心方法在卡片 `method_links` 里的证据数与该节引用的不同作品数。新约定
  **版本引用**：读的是替代版本（报告版、预印本、后一版手册）就写 `[S025 TR pp. 3–12]`、`[S133 v2.0 p. 1]`，卡片正文写明
  （规则写进 `references/paper-reading-card.md` §四「引用规则」）
- 新增 `scripts/audit_claims.py` + `references/claim-audit.md`（声明→证据抽审）：`--sample` 抽 N 条带页码的声明，
  配上所引卡片全文（`cards/<批次>.md` 整张卡片 + 批次头 + digest 的 read_level / quotes + INDEX 页数）成审计包；
  一个零上下文 agent 只读包判定 supported / partial / unsupported / uncheckable；`--report` 追加到
  `<M>/references/research/10-claim-audit.md`，unsupported > 0 退出码 1
- 接入：`team_check.py` 每位成员新增 `citations`、团队级新增圆桌 `citations`（深读档）；`team-synthesize.js`
  （编辑闸门、fidelity 复核员第 4 项、修复闸门）、`team-tighten.js`、`team-increment.js`、`team-integrate.js`（圆桌闸门）
  的闸门清单加 `check_citations.py`；playbook §三/§四/§五/§九、workflows README、extraction-framework §十一、
  fidelity-scorecard、TEAM-KIT.md（本地修改表）、README、项目级 skill 同步
- 首跑 dfo-team（五人 + 圆桌，约 16,000 条卡片引用、10,000 条带页码）：解析器迭代两轮后剩 6 个真问题，全部是
  **替代版本**：Audet S025（37 处，`[S025 TR pp. …]`，卡片说明文件实为 1998 Rice 报告 CRPC-TR98779、OCR 全读，但按
  kit 语义登记为 unreadable）、Scheinberg S133（5 处，v1.2 手册行下读的是 v2.0 手册）。处理：承认版本引用为合法写法
  （卡片必须提到该版本），S133 的 5 处补上 `v2.0` 标记（其中 3 处本来就写着 "v2.0 manual" / "substitute"，2 处裸引用改为
  `[S133 v2.0 pp. 1–3]`）；**没有改 coverage 数字**——这两篇在覆盖表里仍算未读，是 kit 现有语义（文件 ≠ 命名作品 →
  unreadable）造成的已知不一致，更规范的做法是把替代版本登记成自己的 R/D 作品行再读，留作后续
- 声明抽审实测（Scheinberg，SKILL.md，20 条 / 池 269，seed 1，全部命中 full 级卡片；审计 agent = 同模型的独立子 agent，
  只读审计包）：**第一遍** 18 supported / 1 partial / 1 unsupported——两条「不支持」都因为审计包把卡片截在 9,000 字符、
  切掉了 D8 与方法关联行；去掉截断（上限 60,000 字符）重判这 15 条后 **20/20 supported**，审计 agent 在 reason 里保留了
  三处措辞比卡片强的提示（k=8 "rarely known" 比原文软、k=15 "而不是梯度容差" 是 skill 的措辞、k=16 ε_F 子句来自
  共引的 S012）。报告：`product/dfo-team/katya-scheinberg/references/research/10-claim-audit.md`。
  教训已写进脚本：审计包必须给整张卡片
- Windows 修复：`team_check.py` / `team_status.py` 的子进程改为强制 UTF-8（`PYTHONUTF8=1` + 解码 errors=replace）。
  此前只用 `python3 -X utf8` 不设环境变量时，quality_check 一列全是 `?`、新脚本输出的 `…` 还会让 team_check 崩溃
- 验证（Windows 11，Python 3.13，Node 24）：`check_citations.py product/dfo-team` 0 problems（6 位成员级报告 + 圆桌）、
  `product/nonlinear-team` 0（轻量档不适用，只报 DOI 计数）；`team_check.py product/dfo-team` 38 项 0 失败 5 跳过
  （比此前多 6 项 citations）、`product/nonlinear-team` 16 项 0 失败；`workflows/selftest.sh product/dfo-team` 全部通过；
  `check_links.py references/` 只剩 nuwa 原有的 2 条指向 CONTRIBUTING/COMMUNITY 的断链（本仓库没有这两个文件，与本次无关）
- 提交：本条随上述改动一起提交（分支 `team-kit-evidence-gates`，fast-forward 合入 `main`）
- 执行模型：claude-fable-5-1

## 2026-10-09 (7) · 取消 skills/ 目录，产物并入语料目录

- `skills/dfo-team/SKILL.md` → `teams/dfo-team/SKILL.md`，`skills/nlp-team/SKILL.md` →
  `teams/nlp-team/SKILL.md`，本记录 → `teams/DISTILLATION_LOG.md`（均 `git mv`，内容未改）
- DISTILL.md Phase 3 的产物路径、README、TEAM-KIT.md、product/README.md、项目级 skill 同步改为
  `teams/<team>/SKILL.md`；安装仍是只复制该文件到 `~/.claude/skills/<team>/`
- 以下历史条目中的 `skills/...` 路径为当时位置，不再逐条改写

## 2026-10-09 (6) · 内置 team-kit（逐人研究者 skill 流水线）

- 范围：从 AlexanderShi/nvwa-skill `eb012fa` 逐字节同步 `scripts/`（52 文件）、
  `references/`（13 文件）到仓库根，nuwa 根 `SKILL.md` 冻结为 `references/nuwa-SKILL.md`；
  上一条的两个团队由 `skills/researchers/` 移到 `product/`，与 kit 默认布局一致
- 验证：`team_status.py` 两队正常；`check_links.py` dfo-team 79 文件、nonlinear-team 105 文件
  均 0 断链；`team_check.py product/dfo-team` 32 项 0 失败 5 跳过；`workflows/selftest.sh`
  在 Windows 下初次失败 24 项（工作流只认 POSIX 绝对路径），与 nvwa-skill 原仓库对照结果相同
- 自包含加固（同日）：9 个 `scripts/workflows/team-*.js` 的 `args.repo`/`args.scratch` 路径检查改为
  兼容 Windows，之后 `selftest.sh` 全部通过；`new_team.py --init` + 铺目录演练在本仓库内跑通；
  全仓库路径引用扫描无指向外部仓库的悬空引用；`standards/researcher-extraction.md` 的出处改指
  本仓库 `references/extraction-framework.md`；新增项目级 skill
  `.claude/skills/optimization-researchers/`（蒸馏请求路由，不依赖 nuwa-skill）
- 新增根 `.gitignore`（kit 的版权材料规则）与入口文档 `TEAM-KIT.md`；README 目录树与
  「与 nuwa-skill 的关系」同步更新。团队级 skill 与 `teams/` 语料未改动

## 2026-10-09 (5) · 同步逐人研究者 skill（非语料蒸馏，仅归档）

- 范围：新增 `product/dfo-team/`（5 人 + dfo-roundtable）与
  `product/nonlinear-team/`（10 人 + nonlinear-roundtable），共 539 个文件，
  逐字节同步自 AlexanderShi/nvwa-skill `eb012fa` 的 `product/dfo-team`、`product/nonlinear-team`
  （首次落在 `skills/researchers/`，同日随第 6 条移到 `product/`）
- 性质：nuwa team-kit 网络调研蒸馏（researched 2026-09-27），**不经 DISTILL.md 协议、
  不带语料 ID**，出处以各 skill 自带的 `09-evidence-ledger.md` 为准；团队级 skill 与
  `teams/` 语料未改动，质量门 G1–G6 不适用于本条
- 说明文件：`product/README.md`（来源、出处层级、安装方式）

## 2026-10-09 (4) · Katya Scheinberg 双队强化 + nuwa 提炼纪律入标

- 语料版本：6e2011c
- 范围：双队 SKILL.md 增量更新 + 新标准 `standards/researcher-extraction.md`
- 新标准：移植 nuwa-skill extraction-framework 的心智模型三重验证
  （跨域复现/生成力/排他性）、矛盾处理、信息不足处理，适配主题型语料；
  DISTILL.md Phase 0 增加必读、Phase 2 增加硬规则 4（仅三重通过的心智
  模型可进 skill）
- 入库核实（3 个一手页面，2026-10-09）：Georgia Tech 主页（Coca-Cola
  Foundation Chair、MathOR 主编、MOS 主席、Lagrange/Farkas Prize）、
  arXiv:1304.2808（随机模型信赖域）、arXiv:1807.07994（随机 Armijo
  线搜索）；两篇期刊版均未在 arXiv 页列出 → 标需核对；生平据 Wikipedia
  （次级来源，已标注）
- 三重验证结果：Scheinberg 5 条候选立场 → 2 条通过（概率质量标准而非
  期望标准；经典骨架的概率化改造），3 条降级为工作信条。Duchi 两侧档案
  追溯补注（通过：上界必配下界、资源-统计权衡）
- skill 变更：双队数学纪律新增 Scheinberg 准则（概率 vs 期望假设必须
  说清）；DFO 流派表模型型支线 + R11；NLP 随机梯度支线 + H9（随机情形
  的全局化）+ R13；来源索引 S24/S23 + 研究者名册；语料契约与诚实边界
  → 6e2011c
- 质量门：G1–G5 PASS（G2 新人名 Bandeira/Vicente/Paquette 均在 canon 内
  ——Vicente 经 S14/S16 已在）。G6 增补试答：「模型不准还能用信赖域吗？」
  → 能，模型以概率≥1/2 足够准即几乎必然收敛，但该结果限函数值无噪声
  [DFO-R11, S24]，带噪函数值不迁移——通过
- 执行模型：claude-fable-5

## 2026-10-09 (3) · 增量重蒸馏：John Duchi 全面加入 NLP Team

- 语料版本：add5d2e（NLP 侧 Duchi 入库提交）
- 范围：仅 `skills/nlp-team/SKILL.md` 增量更新
- 入库核实（4 个一手页面，2026-10-09）：Stanford 主页（自述研究目标、
  奖项）、JMLR v12 官方页（AdaGrad 12:2121–2159）、arXiv:1005.2012
  （分布式 dual averaging，abs 页列出期刊版 IEEE TAC 57(3):592–606）、
  arXiv:1703.08570（复合/弱凸随机方法，期刊版未列→标需核对）；
  另 [NLP-S22] l1 球投影仅 Scholar 快照级
- 变更：语料契约 → add5d2e；数学纪律加入 Duchi 准则（最优必配下界）；
  随机梯度学派加入 Duchi 支线；新增 H8（几何与结构优先）；结果速查新增
  R10（AdaGrad）、R11（分布式 dual averaging）、R12（复合/弱凸
  prox-linear）；来源索引新增 verified-web 段与研究者档案；诚实边界更新
  （AdaGrad 已入库、弱凸/分布式为入口级单点覆盖、S21 期刊版未核实）
- 质量门：G1–G5 PASS（G2 核对新增人名 Hazan/Singer/Agarwal/Ruan 均在
  canon S19–S22 内）。G6 增补试答：「稀疏特征的大规模在线学习步长怎么
  选？」→ 按坐标自适应（AdaGrad），regret 与事后最优 proximal 可比，
  精确界查原文 [NLP-R10, S19]——通过
- 执行模型：claude-fable-5

## 2026-10-09 (2) · 增量重蒸馏：John Duchi 加入 DFO Team

- 语料版本：8a99343（Duchi 入库提交）
- 范围：仅 `skills/dfo-team/SKILL.md` 增量更新；nlp-team 不变
- 入库核实（语料构建阶段，联网允许）：Scholar 个人页 + arXiv:1312.2139 +
  arXiv:1103.4296 的 abs 页，均核实于 2026-10-09（新层级 verified-web）
- 变更：语料契约版本号 → 8a99343；数学纪律新增「最优必配下界」Duchi 准则
  [DFO-S21]；流派表随机 ZO 支线加入 Duchi；R1 强化为 √d 因子+sharp 下界；
  新增 R10（randomized smoothing）；来源索引新增 verified-web 段与研究者档案；
  诚实边界补研究者档案「仅基于摘要」限定
- 质量门：G1–G5 PASS。G2 再次抓到初版 skill 流派表 KW/SPSA 编号错位
  （误标 S17/S18，应为 S18/S19），已修正。G6 增补试答：
  「两点零阶估计比单点好在哪？」→ √d vs O(n) 级因子、有下界证 sharp、
  常数查原文 [DFO-R1, S21]——通过
- 执行模型：claude-fable-5

## 2026-10-09 · 首次蒸馏

- 语料版本：b007570（首次语料提交）
- 协议：DISTILL.md Phase 0–5，纯本地语料，零 WebSearch
- 产物：`skills/dfo-team/SKILL.md`、`skills/nlp-team/SKILL.md`
- 执行模型：claude-fable-5

### 质量门结果

| 门 | 结果 | 说明 |
|----|------|------|
| G1 语料封闭 | PASS | 两份 skill 中全部事实性声明带语料 ID；无 ID 的仅为流程性指令 |
| G2 引用闭包 | PASS | 全部（作者,年份）对均存在于对应 01-canon.md。自查中发现并修正一次 DFO 来源索引 S17–S19 编号错位 |
| G3 数学纪律 | PASS | 全部速率为定性+假设+proved-vs-cited；无精确常数；ZO 维度因子保留（DFO-R1/R2）；噪声模型显式（DFO-R7、F4） |
| G4 诚实边界 | PASS | 两份均含：蒸馏日期、语料版本 b007570、文献覆盖截止 ~2026-07、语料缺口清单、验证层级声明 |
| G5 禁区完整性 | PASS | DFO 9/9 条、NLP 11/11 条全量移植 |
| G6 试答 | PASS | 见下 |

### G6 试答摘要

1. **「10维、带噪声、评估贵的黑盒问题选什么？」** → 先问噪声类型；先估噪声
   [DFO-S22] 再定差分区间 [DFO-S3]；低维+评估贵首选模型型信赖域 [DFO-S2, S16]；
   报告声明 (d+1) 口径 [DFO-L1]。全程带 ID ✓
2. **「Nelder–Mead 有收敛保证吗？」** → 无一般保证，McKinnon 反例 [DFO-S10]，
   正面结果仅受限情形 [DFO-S11]，正式对比须配有保证的方法 [H5]。命中陷阱清单 F2 ✓
3. **「momentum 能加速 SGD 吗？」** → H4 三句话：确定性凸有可证加速 [NLP-R2]；
   heavy ball 有光滑强凸反例 [NLP-R4]；随机情形不必然改进采样复杂度
   [NLP-R5]、实践收益与初始化/调度耦合 [NLP-R6]。分寸完整 ✓

### 安装

复制到 `C:\Users\sr881\.claude\skills\dfo-team\`、`C:\Users\sr881\.claude\skills\nlp-team\`。
