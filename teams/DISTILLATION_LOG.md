# 蒸馏记录

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
