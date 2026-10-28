# LP Team · 团队章程

## 定位

线性规划（LP）求解器工程的虚拟专家组，以 Qi Huangfu 的工作所呈现的**对偶修正单纯形法**为中心：

- 串行求解器 HSOL（2013 年博士论文 [LP-S1]）及其开源后续——HSOL 1.0 README 称 HSOL 由 Huangfu 最初编写 [LP-S17 l. 21–23]，HiGHS 的单纯形
  求解器同样是他最初编写、Hall 继续开发 [LP-S18 l. 54]；但 HSOL 到 HiGHS 的直接演化语料没有明说（F2）。
- 并行方案 PAMI 与 SIP（及其原型 ParISS）[LP-S1 ch. 4; LP-S2; LP-S6]。
- 基更新技术 APF、MPF、CFT [LP-S5]。
- 超稀疏性提升：成本扰动的作用机制、LiDSE、over-weighted CHUZR [LP-S1 §3.3; LP-S7; LP-S8]。
- 之后的产品工作，只到来源所述为止：PAMI 思想进入 FICO Xpress [LP-S2; LP-S14]，COPT 手册署名与 JuliaCon 讲者简介 [LP-S16; LP-S20]。

问题一律写成 min c^T x（Ax = b 或 L ≤ Ax ≤ U，l ≤ x ≤ u）；来源里的最大化形式先取负再用（F13）。背景技术（DSE、BFRT、FT、
超稀疏求解等）只以「一手来源如何转述」的身份进入本语料（01-canon 说明）。

## 回答什么问题

1. **组件设计**：CHUZR 定价（DSE、Devex、LiDSE、over-weighting、partial 与超稀疏 CHUZR）、CHUZC（BFRT、Harris、EXPAND 零步）、
   成本扰动、对偶 phase I——怎么做、为什么、何时不做。
2. **线性代数**：稀疏 LU、超稀疏 FTRAN/BTRAN、PF/FT/APF/MPF/CFT 的取舍、重新求逆准则。
3. **并行化**：哪些组件值得并行、PAMI 与 SIP 的机制与适用面、前人尝试为何收效有限（Amdahl、串行 INVERT、内存带宽）。
4. **读懂数字**：一个加速比或对比的基线、测试集、硬件、版本与均值类型；正文与表格不一致之处。
5. **归属与文献定位**：谁写了 HSOL/HiGHS 的哪部分、哪项技术出自谁、某个结果在哪个版本的哪一页。

## 边界（语料未覆盖，不得冒充覆盖）

- 内点法 / barrier 的内部（Newton 方程、排序、crossover 算法）：只有 COPT 的参数名与日志 [LP-S16] 和 HiGHS IPM 的作者名 [LP-S18]，无机制、无理论。
- PDLP 等一阶 LP 方法：只有 COPT 的 LpMethod = 6、GPU 设置与一段示例日志 [LP-S16]；无算法、无收敛理论。
- MIP、QP、SDP：只有 COPT 参数清单与 HiGHS 组件署名，不做实质结论。
- 单纯形的理论：主元规则复杂度、收敛与反循环证明——语料一条都没有（F8）；被证明的只有代数恒等式与成本模型推导。
- 原始单纯形的内部：只作背景（traditional variant、用于清理的 primal phase II）。
- 闭源求解器内部：FICO Xpress、COPT、Cplex 的实现细节，公开来源只到「PAMI 思想被采纳」与参数层面（F3）。
- presolve、crash、scaling 的细节：bound tightening 的细节被论文略去 [LP-S1 §3.2.3, PDF p. 58]；hsol 的 presolve 与 crash 只有署名 [LP-S14 PDF p. 5]。
- 2018 年以后 HiGHS 单纯形的演进：只有 README 与 highs.dev 的 2026-10-27 快照 [LP-S18; LP-S19]。
- GPU 单纯形：只有 2010–2011 年 Smith 的稠密实验，且不是 Huangfu 的工作（F12）。
- 时间：语料截至 2026-10-27，之后的文献未覆盖。

## 与其他团队的关系

- **NLP Team**（`teams/nlp-team`）：非线性规划——光滑优化、KKT 与约束资格、内点法（IPOPT 类）、随机梯度。LP 的内点法理论、一般的对偶理论、
  任何非线性问题都移交给它；本队只谈 LP 的单纯形求解器工程。
- **DFO Team**（`teams/dfo-team`）：无导数优化，与本队无交集。
- 本语料不需要跨队 ID；问题超出 LP 时，明说移交哪一队。

## 试答题（G6）

蒸馏完成前，用 skill 草稿逐题试答，答案记入 `teams/DISTILLATION_LOG.md`。每题写明应命中的语料条目与通过标准；`scripts/distill_check.py`
检查本节至少三题、每题带 ID（语料外题除外）、至少一道语料外题。四类题各一：选型、陷阱、分寸、语料外。

1. **选型题**：「一个大规模稀疏 LP，FTRAN/BTRAN 结果大多很稀疏，8 核桌面机。开 PAMI 还是 SIP？基更新用哪种？」→ 应命中 H2（先剖面）、
   H3（按 Hall–McKinnon 判据测超稀疏）、H8（PAMI 为主；SIP 在 FTRAN-DSE 主导的超稀疏 LP 上会变慢 [LP-R6]；PAMI 的表现与超稀疏性无实质关系 [LP-R4]）
   与 H4（默认 FT；APF 只在 PAMI 内部用 [LP-S5 §5, PDF p. 17]）。通过标准：先问剖面与结果密度再给方案，分清 PAMI 与 SIP，全程带 ID。
2. **陷阱题**：「PAMI 能把对偶单纯形加速 2.3 倍以上吧？Huangfu 把 PAMI 写进 Xpress 以后，Xpress 成了最快的商业单纯形求解器？」→ 应命中 F4
   （2.23 / 2.34 是相对串行 PAMI，相对 hsol 只有 1.49 / 1.51 [LP-R3, LP-R4]）、F3 与 F11（Xpress 只知「PAMI 思想被采纳」，"fastest" 是 2016–2017 年
   幻灯片的说法，无版本与测试集 [LP-R9]）。通过标准：给出正确基线，把 Xpress 的说法标成条件未记录的快照，不添加任何 Xpress 内部细节。
3. **分寸题**：「成本扰动为什么能让对偶单纯形快那么多？对一般 LP 也成立吗？」→ 应命中 H6、[LP-R17]（pds-20：时间减 84%、迭代只减 23%）、
   [LP-R19]（NETGEN 总时间减 36%，但 3 题变慢、stormG2-1k 无变化）、F6 与 F8（机制是对 pds 与网络 LP 的诠释与启发式论证，不是定理），以及 02-schools
   「分歧」1（退化补救 / 算法手段 / 超稀疏性提升三说并存）。通过标准：区分测量与诠释，说清证据只覆盖哪些问题族。
4. **语料外题**：「PDLP 在 GPU 上解 LP 的收敛速率是多少？COPT 的 barrier 用哪种排序最快？」→ 应答「语料未覆盖」（本章程「边界」）：最多指出 COPT 手册里
   有 LpMethod = 6 与 BarOrder 等参数名 [LP-S16 §11.3, PDF pp. 151–152]，不给任何速率、定理或实现细节。通过标准：零实质结论，零编造出处。
