# Qi Huangfu · LP Team 研究者档案

> 档案依据：01-canon 的一手来源 [LP-S1–S20]（2026-10-27 下载并阅读；除 COPT 手册 [LP-S16] 只读 PDF pp. 15–18、151–158、167–171、231–240 外，
> 均全文已读；论文 [LP-S1] 依 ERA 条款只作短引），另加两条相关记录：FICO 博客 [LP-S58]（只核实其存在，正文未读）与 COAP 2015 奖公告
> [LP-S59]（只读首页）。版本：PAMI 论文以 ERGO-14-011 [LP-S2] 为阅读主本，arXiv v1 [LP-S3] 与 MPC 2018 [LP-S4] 作版本对照；更新技术读
> ERGO-13-001 报告 [LP-S5]（COAP 期刊版正文未读）；ParISS 读 ERGO-11-007 报告 [LP-S6]（LNCS 版正文未读）。
> **语料中没有个人主页、简历、访谈或第三方传记**——身份信息只来自文献的署名、致谢、作者句与讲者简介。
> 方法论立场按 `standards/researcher-extraction.md` 做三重验证；凡出自与 Hall 合著文本的立场，无法单独归于 Huangfu（见「信息不足」）。

## 身份速览（只列来源所写）

- 博士论文 "High performance simplex solver"，University of Edinburgh，2013 [LP-S1 title page, PDF p. 2]；导师 Julian Hall，第二导师 Jacek Gondzio；
  资助方 Format International Ltd. 与 NAIS [LP-S1 Acknowledgements, PDF p. 8]；声明论文为本人工作（另有注明者除外）[LP-S1 Declaration, PDF p. 6]。
- 隶属（按印出的样子）：2010–2013 年的报告与题页署 University of Edinburgh 数学学院 [LP-S10 PDF p. 1; LP-S12 PDF p. 1; LP-S6 PDF p. 1; LP-S7 PDF p. 1; LP-S5 PDF p. 1]；
  PAMI 论文署 FICO House, Birmingham, UK [LP-S2 PDF p. 1; LP-S4 PDF p. 3]；2016–2017 年幻灯片题页署 FICO [LP-S13 PDF p. 1; LP-S14 PDF p. 1; LP-S15 PDF p. 1]；
  2016 年 11 月的 COAP 奖公告称他 "of the FICO Xpress Team" [LP-S59 PDF p. 1]。何时加入 FICO、之后的去向：语料未说明；COPT 手册与 JuliaCon 页都不印他的隶属
  [LP-S16 §1.3–§1.4, PDF pp. 17–18; LP-S20 l. 14–15]。
- HSOL / hsol：README 称 "HSOL was originally written by Qi Huangfu"，presolve、crash、advanced basis start 由 Hall 与 Galabova 加入 [LP-S17 l. 21–23]；论文以被动句称 HSOL
  从零实现 [LP-S1 §1, PDF p. 17]；期刊版写两位作者从零实现 hsol [LP-S2 §1, PDF p. 2]；ERGO-13-001 既写 Huangfu 的 hsol，也写 Huangfu 和 Hall 的 hsol [LP-S5 §2.1, §4, PDF pp. 6, 13]。
- 最早的对偶原型：2010-12-02 的幻灯片署 "Written by Qi Huangfu (2010)"，并说 "First run last week!" [LP-S10 PDF p. 23; LP-S11 PDF p. 21]；对应的算法变体署 "H and Qi"
  （Hall 与 Huangfu）[LP-S11 PDF p. 15]。ParISS 由谁编写未说明 [LP-S6]。
- HiGHS："HiGHS has primal and dual revised simplex solvers, originally written by Qi Huangfu and further developed by Julian Hall." [LP-S18 l. 54]；highs.dev 称 HiGHS 基于他开发的
  对偶修正单纯形 [LP-S19 l. 106–114]；HiGHS 指定的引用文献是他与 Hall 的 MPC 2018 论文 [LP-S18 l. 285–292; LP-S19 l. 116–121]；当前团队名单不含他 [LP-S19 l. 123–137]。
- FICO Xpress："One of the authors has implemented the techniques underlying PAMI within the FICO Xpress simplex solver" [LP-S2 abstract, PDF p. 1]，§5.4 指明是 Huangfu
  [LP-S2 §5.4, PDF p. 23]；幻灯片印 "pami ideas incorporated in FICO Xpress (Huangfu 2014)" [LP-S14 PDF p. 12]；MPC 版以他的 FICO 博客为出处 [LP-S4 §5.4, PDF p. 24; LP-S58]。
- COPT：COPT 用户手册五位作者之一（Ge, Huangfu, Wang, Wu, Ye）[LP-S16 §1.3, PDF p. 17]；JuliaCon 2022 讲者简介：
  "Qi Huangfu is the developer of COPT and has worked on many different optimization solvers, including HiGHS and FICO-Xpress." [LP-S20 l. 15]
- 奖项（来源所印）：2015 年 COAP 最佳论文奖，授予他与 Hall 的 "Novel update techniques for the revised simplex method" [LP-S59 PDF p. 1; LP-S13 PDF p. 29]。

## 在 LP 版图中的位置

在 02-schools 的五张图里，来源标为新提出的、署有他名字的工作落在三格：B（基更新——与 Hall 的 APF、MPF、CFT）、C（定价——LiDSE 与超稀疏性提升的诠释；over-weighting 与 Hall 合作）、
E（并行——PAMI 与 SIP）。在 A（对偶 vs 原始）与 D（比率检验）两格他是集成者而非发明者：DSE、BFRT、Harris、EXPAND、扰动、对偶 phase I 都取自前人（F7），
他的增量在实现层——离基行 DSE 权重核查、Harris 组与 BFRT 的结合、BOXED 变量在 phase I 中的处理 [LP-S1 §3.2.2–§3.2.4, PDF pp. 54–60]。

## 核心贡献（逐条带锚点）

### 1. HSOL：高效的串行对偶修正单纯形 [LP-S1 ch. 2–3]
- 线性代数：实现 Suhl–Suhl 稀疏 LU [LP-S1 §2.2.6, PDF p. 28]；为置换因子写出两阶段 DFS 超稀疏求解的伪代码（论文称 Gilbert–Peierls 只简略提过）
  [LP-S1 §2.3.3, PDF pp. 32–33]；写出维护行式表示与超稀疏结构的 FT 更新实现，论文称此前 "never been documented" [LP-S1 §2.4.3, PDF p. 36]。
- 对偶算子：离基行 DSE 权重核查（r = 0.5）与对偶超稀疏 CHUZR [LP-S1 §3.2.2, PDF p. 55]；BFRT 与 Harris 组的结合、对偶 EXPAND 零步、Koberstein 扰动的
  简化不加权版 [LP-S1 §3.2.3, PDF pp. 58–59]。
- 质量：论文称与 Clp 的对偶单纯形 comparable（LP-R11）；期刊版测得 hsol 比 Clp 1.15 快 2.29 倍（LP-R10）。

### 2. 三种基更新：APF、MPF、CFT [LP-S5; LP-S1 §2.5]
- 作者称不知道此前有人描述过这两种乘积形式变体 [LP-S5 §3.1, PDF p. 6]；MPF 简单且接近 FT，APF 只在 suboptimization 框架内有价值，CFT 让 FT 能用在
  minor iterations 之后（LP-R12, LP-R13, LP-R14, LP-R15）。该文获 2015 年 COAP 最佳论文奖 [LP-S59]。

### 3. 超稀疏性提升 [LP-S1 §3.3; LP-S7; LP-S8]
- 诠释成本扰动为何让 pds 问题的迭代大幅变快（LP-R17）；LiDSE 与广义 LiDSE（LP-R18）；与 Hall 合作提出 over-weighted CHUZR（LP-R20, LP-R21）。

### 4. 并行对偶单纯形：PAMI 与 SIP [LP-S1 ch. 4; LP-S2]
- PAMI：suboptimization + 任务并行的 BTRAN/FTRAN + 数据并行的 PRICE/CHUZC1 + 用 APF 合并 FTRAN-BFRT + CFT + 候选质量控制（H9, H10）；8 核相对 hsol 的均值
  1.49（论文）/ 1.51（期刊）（LP-R3, LP-R4）。
- SIP：常规 DSE 对偶单纯形的单次迭代内并行，在 PAMI 变慢处互补（LP-R5, LP-R6）。
- 演进：2010-12 原型 → ParISS（2011-05）→ ParISS 2.0（2011-09）→ PAMI（LP-R22, LP-R23, LP-R24）；arXiv 版称 PAMI 的 fundamental design、MPC 版称其
  concept 由 Hall 与 Huangfu 在 PPAM'11 提出（ERGO 版此句缺一个词）[LP-S3 §3, PDF p. 9; LP-S4 §3, PDF p. 10; LP-S2 §3, PDF p. 9]。

### 5. 工业转化与后续产品
- 在 FICO Xpress 中实现 PAMI 背后的技术（LP-R9）；HiGHS 单纯形的最初编写者 [LP-S18 l. 54]；COPT 手册作者与 JuliaCon 简介所称的 COPT 开发者
  [LP-S16 §1.3, PDF p. 17; LP-S20 l. 15]——这三处的具体贡献语料都没有展开。

## 方法论立场（按三重验证分级）

### 心智模型 1 串行效率先行：并行只在一流的串行实现之上才算数 ✅三重通过
- **跨域复现**：并行原型 [LP-S6 §3, PDF pp. 5–6]（ParISS 先要求串行组件高效）；并行论文 [LP-S2 §2, PDF p. 3]（只在低效实现里有效的发展 "not worthy of attention"）；
  更新技术 [LP-S5 §4, PDF p. 13]（先证明做实验的 hsol 与 clp、cplex 有竞争力，结论才适用于最高效的求解器）；串行求解器本身 [LP-S1 §1, PDF p. 17]（从零写 HSOL 作为
  并行基础）——四份不同工作、三个算法族。
- **生成力**：遇到任何「单纯形加速 X 倍」的主张，他会先问：基线是不是一流的串行实现，加速相对谁？可检验：他自己的期刊版同时报 p1/hsol、p8/p1、p8/hsol，
  并按迭代比缩放最好的个例（LP-R4）。
- **排他性**：与语料转述的另一种并行单纯形文化相对——稠密 tableau 与 GPU 实现报「几十到上千倍」加速，却不敌好的串行稀疏修正单纯形 [LP-S1 §4.1.1, PDF pp. 70–71]；
  Shu 的高加速来自老式 PRICE [LP-S1 §4.1.2, PDF p. 73]。

### 心智模型 2 为暴露并行而换用（稍劣的）算法变体，再用控制机制补回损失 ✅三重通过
- **跨域复现**：定价层——复活被遗忘的 suboptimization，只为取得任务并行，并用 ψ 截断控制候选质量 [LP-S2 §2.3, §3.3, PDF pp. 8, 13–14]；线性代数层——设计 APF
  让多个 FTRAN 合成一次、设计 CFT 让 minor iterations 之后仍能用 FT [LP-S5 §3.1.1, §3.2, PDF pp. 7–12]；对照方案 SIP 不换变体，只能取单次迭代内的有限并行
  [LP-S1 §4.4.1, PDF p. 90]。
- **生成力**：面对一条串行依赖链，他会问：有没有代数上等价或略劣的变体能暴露并行，再用什么控制补回？可检验：论文为串行的 INVERT 提出「后台分解 + FT 追赶」
  的重叠方案 [LP-S1 ch. 5, PDF p. 95]。
- **排他性**：与 Bixby–Martin 只并行常规方法组件的路线相对 [LP-S52，据 LP-S2 §2.2.4, PDF p. 6]，也与「suboptimization 已被淘汰」的通行看法相对
  [LP-S2 §2.3, PDF p. 8]。

### 心智模型 3 从意外的计算现象出发，用剖面找机制，再把机制做成新技巧 ✅三重通过
- **跨域复现**：定价层——扰动带来不成比例的提速 → 统计超稀疏率与翻界次数 → BFRT 诠释 → LiDSE、partial CHUZR [LP-S1 §3.3, PDF pp. 61–68]；同一路线在 APMOD12
  走到 over-weighting [LP-S7 §1–§3, PDF pp. 1–5; LP-S8 PDF pp. 9–27]；并行层——组件剖面（LP-R1）→ CHUZC2 不并行、SIP 的结构、解释 PAMI 最好与最差的个例
  [LP-S1 §4.2–§4.4, PDF pp. 76–93; LP-S2 §5.2, PDF p. 22]。
- **生成力**：遇到「迭代只少 10%、时间却少 60%」这类现象，他会把时间拆到组件与稀疏率上，问路径是否经过了更超稀疏的顶点——这正是 [LP-S7 §1, PDF p. 2] 的提问方式。
- **排他性**：与文献很少讨论扰动为何有效、Bixby 不给解释、Koberstein 的加权扰动没有数值证据的状况相对 [LP-S1 §3.3.2, PDF p. 62]。

### 工作信条（未全过三重验证，按标准降级）
- **实现简单是一等设计目标**：MPF 被推荐给 "an industrial context where an independent code-base is necessary" [LP-S5 §5, PDF p. 18]；HSOL 故意保持简单以便设计并行方案
  [LP-S1 ch. 5, PDF p. 95]；现有公开代码因太复杂难扩展而不被采用 [LP-S1 §1, PDF p. 17]。跨域与生成力都过，**排他性弱**（重视简单是普遍的工程价值），降级。
- **公平的比较口径**：同一基序列、共用 FT 区间、几何均值、performance profile [LP-S5 §4, PDF pp. 13–16; LP-S1 §2.5.4, PDF p. 46; LP-S2 §5.1, PDF p. 16]。跨域与生成力都过，
  但排他性与心智模型 1 重叠、不能独立成立，降级。

## 矛盾与张力

1. **对偶 suboptimization 算不算新**（时间性）：2010-12 的幻灯片写 "Dual: New, even in serial?"，2011-04 的去掉了问号 [LP-S10 PDF p. 19; LP-S11 PDF p. 20]，而同期来源都把
   它记给 Rosander [LP-S6 §2.1, PDF p. 3]；2017 年的说法改为 "Suggested by Rosander (1975)"、此前未在串行中被高效实现 [LP-S14 PDF p. 8; LP-S15 PDF p. 18]。宜读作「在现代
   实现中是新的」，不是概念新。
2. **PAMI 是否「基于」suboptimization**：见 02-schools「分歧」9 [LP-S1 ch. 5, §4.3.1, PDF pp. 80, 94]。
3. **串行竞争力表述的演化**（时间性）：2011-04 的 "Underlying serial solver is now competitive with clp"，同页 1 核时间却慢于 clp；一个月后 ParISS 单核平均慢 2.7 倍
   [LP-S11 PDF p. 23; LP-S6 §4, PDF p. 7]；论文摘要说与最好的公开对偶单纯形 comparable，第 1 章改说「最好的之一」[LP-S1 Abstract, §1, PDF pp. 4, 17]；2013 年称 hsol 与 cplex
   competitive [LP-S5 §4, PDF p. 13]，2016–2017 年幻灯片只说 8 核 pami 正在接近 cplex [LP-S15 PDF p. 20; LP-S13 PDF p. 33]。
4. **partial CHUZR**（领域性）：网络 LP 上正面（与 Hall 合作）、pds 上负面（论文）——见 02-schools「分歧」6。
5. **推荐 MPF 却不用 MPF**：报告推荐 MPF [LP-S5 §5, PDF p. 18]，但 hsol/h2gmp 与 pami 都不用它 [LP-S15 PDF p. 19; LP-S13 PDF p. 32]。
6. **「第一个」通用并行修正单纯形**：期刊称其工作是第一个 "parallel revised simplex solver of general utility"，同文却引了更早的并行修正单纯形（Bixby–Martin、PARSMI、ASYNPLEX）；
   关键在未定义的 general utility [LP-S2 abstract, §1, §2.3, PDF pp. 1–2, 8]。
7. **FICO 相关措辞随版本变**：arXiv v1 有 FICO "advertising copy and blogs" 的句子，ERGO 与 MPC 版删去 [LP-S3 §5.4, PDF p. 24; LP-S2 §5.4, PDF p. 23; LP-S4 §5.4, PDF p. 24]。

## 信息不足

- **生平与职业**：语料无个人主页、简历、访谈；职业时间线只能由署名拼出（Edinburgh → FICO → JuliaCon 简介所称的 COPT 开发者），何时离开 FICO、是否就职 Cardinal Operations，
  语料未说明——此维度为推测，不入 skill。
- **Xpress 工作的范围**：只有「实现了 PAMI 背后的技术」与「对 Xpress 的改进」两类说法；版本、范围、是否含 SIP 或更新技术均未说明，FICO 博客正文未读 [LP-S2 §5.4, §6, PDF pp. 23, 25; LP-S58]。
- **COPT**：手册不分配组件；他在 COPT 中具体做了什么，语料未说明 [LP-S16 §1.3–§1.4, PDF pp. 17–18; LP-S20 l. 15]。
- **HiGHS**：他是单纯形的最初编写者，此后的开发归 Hall，当前团队名单里没有他——2018 年以后他与 HiGHS 的关系语料未说明 [LP-S18 l. 54; LP-S19 l. 123–137]。
- **个人立场与合著立场**：三条心智模型的跨域证据大半出自与 Hall 合著的文本，只有论文是独著（且在 Hall 指导下）；无法把立场单独归于 Huangfu。
- **理论立场**：所有来源都是算法工程与计算实验，没有收敛或复杂度工作；本档案对其理论立场不作推断（F8）。
- **阅读限制**：论文按 ERA 条款只短引；COPT 手册只读四段页码；会议版（LNCS）与 COAP 期刊版正文未读。
