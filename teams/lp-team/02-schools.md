# LP Team · 流派：共识与分歧

这里的「流派」是语料来源描述的设计传统。背景文献 [LP-S21–S59] 的正文未读：表中凡引背景 ID，都读作
「据同一格里的一手来源转述」（见 01-canon 说明）。例外是 2026-11-05 勘误时打开过原文的几处：标「原文核对」或「源码核对」的句子
据原文（LP-S22 技术报告版 TR01-20、LP-S50、LP-S52 预印本、LP-S55 源码与新增的 LP-S60），不是转述；经 LP-S60 转述的 LP-S61、LP-S62 仍是转述。

## 流派地图

### A. 默认变体：原始、对偶与内点

| 路线 | 核心做法 | 代表（出处） | 语料中的证据与评价 |
|------|---------|-------------|-------------------|
| 原始修正单纯形 | 保持原始可行（x_B ≥ 0），直到对偶可行 | 被称为 traditional variant [LP-S13 PDF p. 16]；早期并行单纯形工作多是原始的 [LP-S6 §2.2, PDF p. 4] | 原始 LP 收紧约束后，解一般不再原始可行 [LP-S13 PDF p. 16]；本语料里原始 phase II 只用于去扰动、去 shift 后的清理 [LP-S1 §3.2.3, PDF p. 59] |
| 对偶修正单纯形 | 保持对偶可行（ĉ_N ≥ 0）：CHUZR 选原始不可行的行离基，CHUZC 用比率检验选入基列 | Lemke 首创 [LP-S21，据 LP-S1 §3.1.2, PDF p. 50]；1990 年代有了 DSE [LP-S28] 与 BFRT [LP-S29] 之后成为首选 [LP-S1 §1, PDF p. 16; LP-S2 §1, PDF p. 2] | 理由：对偶可行的起点更易得、有原始没有的算法技巧、加约束后仍保持对偶可行（MIP）[LP-S10 PDF p. 11; LP-S13 PDF p. 16]；COPT 对 LP 的自动选择即对偶单纯形 [LP-S16 §11.3, PDF p. 151] |
| 内点法 / barrier（本队边界外） | — | 1980 年代起就有竞争力 [LP-S1 §1, PDF p. 16; LP-S2 §1, PDF p. 1] | 求解一族相关问题时对偶单纯形常被优先 [LP-S2 §1, PDF p. 1]；内部机制不在本队范围（00-charter） |

### B. 基逆的表示与更新

| 路线 | 核心做法 | 代表（出处） | 语料中的证据与评价 |
|------|---------|-------------|-------------------|
| product form（PF；幻灯片写作 PFI） | 每次基变化在 B^{-1} 上乘一个 eta 阵，B_0 = L_0 U_0 不动 | Dantzig–Orchard-Hays [LP-S34，据 LP-S5 §2.1, PDF p. 4] | 最简单、无动态数据结构，存的是完整 FTRAN 结果；通常比 FT 费存储、慢 [LP-S1 §2.4.2, PDF p. 35] |
| LU 更新族 | 直接更新三角因子 | Bartels–Golub [LP-S35]、Bartels [LP-S36]、FT [LP-S37]（Tomlin 1974 省去其额外的部分 BTRAN [LP-S38]）、Reid [LP-S39]、Suhl–Suhl [LP-S43]（均据 LP-S5 §1–§2.1, PDF pp. 2–6） | 被广泛认为最高效的一类；作者选 FT：Suhl 的更新需要一次 FT 不需要的 BTRAN，Reid 的不如 FT 适合超稀疏 LP [LP-S5 §2.1, PDF p. 6] |
| Schur complement 族 | B_k = B_0 H_k，经 Schur 补表示更新 | BLU [LP-S42]、Hall 的 alternative block LU [LP-S41]、partitioned LU（据称提出未实现）[LP-S40]（据 LP-S1 §2.5, PDF pp. 40–42; LP-S5 PDF pp. 8–9） | 作者称大量更新后，维持 Schur 补的可逆表示开销显著 [LP-S5 PDF p. 8] |
| 新乘积形式 APF、MPF | APF 用完整 BTRAN 结果 ê_p 与 A 的两列，作用在 B_0^{-1} 之前；MPF 把秩一因子插在 L 与 U 之间，用与 FT 相同的两个部分结果；二者都不要 Schur 补 | Huangfu–Hall [LP-S5 §3.1, PDF pp. 6–9; LP-S1 §2.5, PDF pp. 39–42] | MPF 简单且接近 FT（LP-R12, LP-R13）；APF 不推荐作一般用途，价值在 suboptimization 并行框架内 [LP-S5 §5, PDF p. 17] |
| collective FT（CFT；ERGO_301116 称 Multiple Forrest-Tomlin update） | 一次完成 t 个 FT 更新，由 B_k 的 FT 表示直接得到 B_{k+t} 的 | Huangfu–Hall [LP-S5 §3.2, PDF pp. 10–12] | 与逐个 FT 的效率相当（LP-R12, LP-R13）；为 PAMI 而设计 [LP-S1 §4.3.4, PDF p. 85] |

### C. CHUZR 定价（选离基行）

| 路线 | 核心做法 | 代表（出处） | 语料中的证据与评价 |
|------|---------|-------------|-------------------|
| 最大不可行量（教科书式） | p = argmax Δx_i | [LP-S1 §3.2.2, PDF p. 54] | 未归一化的基线；HSOL README 的 edge-weight 选项含 Dan、Dvx、DSE、DSE0、DSE1，均未展开 [LP-S17 l. 85–86] |
| 对偶 steepest edge（DSE） | 用 e_i^T B^{-1} 的范数归一化；每次迭代多一次 FTRAN-DSE 来更新权重 | Forrest–Goldfarb [LP-S28，据 LP-S1 §3.2.2, PDF p. 54] | 论文称其为对偶修正单纯形最知名的归一化方案 [LP-S1 §3.2.2, PDF p. 54]；FTRAN-DSE 平均占 26.4% 时间（LP-R1）；从高级基热启动时初始化昂贵 [LP-S13 PDF p. 40] |
| Devex | 近似的边权 | Harris [LP-S26]；与 steepest edge [LP-S27] 一起取代了 suboptimization（据 LP-S1 §4.3.1, PDF p. 80） | dual Devex 初始化零成本但效果较差 [LP-S13 PDF p. 40]；COPT 的 DualPrice 只有 Devex 与 DSE 两档、默认自动 [LP-S16 §11.3, PDF pp. 151–152] |
| 问题类专用：LiDSE 与 over-weighting | 改变不可行量与权重的指数，从而改变对稠密行的惩罚 | Huangfu 论文 [LP-S1 §3.3.4–§3.3.5, PDF pp. 66–68]；Hall–Huangfu 幻灯片 [LP-S8 PDF p. 23] | 证据只在 pds（LP-R18）与网络 LP（LP-R20, LP-R21） |
| 超稀疏 CHUZR / partial CHUZR | 维护一张按截断值筛选的候选表 / 只看一部分行（APMOD12 称随机子集；源码核对：Clp 实为从不可行列表的随机位置起回绕连续扫描，数到 max(2000, number/8) 个超出容差的项即停，所以这类项不多于 2000 个时仍是全扫 [LP-S55 src/ClpDualRowSteepest.cpp l. 252–336 @874465237db8]） | 超稀疏版由 Hall–McKinnon 的原始超稀疏 CHUZC 改作对偶 [LP-S45，据 LP-S1 §3.2.2, PDF p. 55]；partial 版见于 Clp，作者不知有发表文献 [LP-S7 §4, PDF p. 5]，论文则说对偶的 partial CHUZR（原始中即 partial pricing）"is not a novel idea at all" [LP-S1 §3.3.3, PDF p. 64]。源码核对：自 2003-10-15 的提交起是 Clp 对偶 CHUZR 的默认（mode 3；此前默认 mode 0，全扫）[LP-S55 include/ClpDualRowSteepest.hpp l. 63–70, ClpDualRowSteepest.cpp l. 213–238 @29f4248e63e3; include/ClpDualRowSteepest.hpp l. 61–64, ClpDualRowSteepest.cpp l. 183–212 @9c09468576f2; src/ClpDualRowSteepest.hpp l. 81–87, src/ClpSimplex.cpp l. 162 @874465237db8]；原文核对：Koberstein 2005 §8.2.2.3 已发表随机起点的 partial pricing（默认比例 1/8）[LP-S60 PDF p. 117] | partial 在 NETGEN 上有益（LP-R20），在较大 pds 上不合适（LP-R18）；源码核对：Clp 头文件注释说只扫一部分在很简单的问题上可能更快 [LP-S55 src/ClpDualRowSteepest.hpp l. 84–85 @874465237db8] |

### D. CHUZC 比率检验与退化处理

| 路线 | 核心做法 | 代表（出处） | 语料中的证据与评价 |
|------|---------|-------------|-------------------|
| 教科书对偶比率检验 | q = argmin c̄_j / ā_pj（ā_pj > 0） | [LP-S1 §3.2.3, PDF p. 57] | 平局与退化时步长可为零，可能停滞或循环 [LP-S8 PDF p. 4] |
| Harris 两遍检验 | 先按放宽的对偶容差求 θ_r，再在比率不超过 θ_r 的候选中取主元最大者 | Harris [LP-S26，据 LP-S1 §3.2.3, PDF p. 58] | 移植到对偶只需微小改动；不处理已在容差内不可行的候选 [LP-S1 §3.2.3, PDF p. 58] |
| BFRT | 把挡路的 BOXED 候选翻到另一界，沿分段线性的目标增益继续走 | Fourer [LP-S29，据 LP-S1 §3.2.3, PDF p. 57]；原文核对：Koberstein 据 Kostina 称 BFRT 的基本思想 1979 年已由 Gabasov、Kirillova、Kostyukova 在俄文文献中发表，西方文献多把 Fourer 当作首发 [LP-S61, LP-S62，据 LP-S60 PDF pp. 18, 41]（Kostina 原文未读） | 与 DSE 并列为 1990 年代对偶提速的两大原因 [LP-S2 §1, PDF p. 2]；比率在零处大量平局时无从翻界 [LP-S1 §3.2.3, PDF p. 58] |
| EXPAND 零步 | 把入基变量已有的微小不可行 reduced cost shift 成零 | Gill–Murray–Saunders–Wright [LP-S30，据 LP-S1 §3.2.3, PDF pp. 58–59] | HSOL 只取严格零步，不用完整的扩张容差框架 [LP-S1 §3.2.3, PDF p. 59] |
| 成本扰动 | 开始前（或迭代停滞时）随机扰动成本，结束后移除 | Koberstein 与 Clp [LP-S23; LP-S8 PDF p. 7]；源码核对：Clp 自 2003-10-15 的提交起按列非零数加权 [LP-S55 ClpSimplexDual.cpp l. 3131–3193 @29f4248e63e3]；原文核对：Koberstein 2005 称其扰动与 COIN LP 的相似 [LP-S60 PDF p. 98] | 作用之争见「分歧」1、2；源码核对：Clp 的库默认（perturbation 100）只在迭代超过 2(m+n) 后才扰动，clp 程序设 50、在开始前扰动，但不同成本值超过列数四分之一时不在开始前扰动，而把 perturbation 改回 100，此后同库默认一样等迭代超过 2(m+n) 才扰动 [LP-S55 src/ClpSimplexDual.cpp l. 335–338, 486–490, 6620–6662; src/ClpSimplex.hpp l. 732–737; src/ClpSolver.cpp l. 130 @874465237db8]；原文核对：Koberstein 2005 也只在不同成本值少于结构变量数四分之一时于开始前扰动 [LP-S60 PDF p. 98] |

### E. 并行化路线

| 路线 | 核心做法 | 代表（出处） | 语料中的证据与评价 |
|------|---------|-------------|-------------------|
| 稠密 tableau / GPU 标准单纯形 | 对整张 tableau 做数据并行 | 论文表 4.1 列举的多项工作 [LP-S1 §4.1.1, PDF pp. 70–71]；Smith 的 i6（CPU）与 i8（GPU）[LP-S11 PDF p. 16; LP-S9 PDF pp. 53–56] | 加速「从几十到上千」，但无法实用地利用稀疏，整体不及好的串行稀疏修正单纯形 [LP-S1 §4.1.1, PDF pp. 70–71]；Smith 的 GPU 版被评为 "Not (really) of practical value but a good learning exercise" [LP-S10 PDF p. 26] |
| 单次迭代内数据并行（对偶） | 并行 PRICE（以及 UPDATE-DUAL、CHUZC）；原文核对：预印本的 PowerC 版另并行 Enter（约等于 CHUZR）与按行存储的 A_N 的更新 [LP-S52 SC-95-45 PDF pp. 6, 15–16] | Bixby–Martin [LP-S52，据 LP-S2 §2.2.4, PDF p. 6; LP-S1 §4.1.2, PDF p. 74] | π_p^T N 的成本占主导（n 远大于 m）时可显著加速 [LP-S13 PDF p. 17; LP-S12 PDF p. 26]；论文按自己的剖面推出 Amdahl 上界约 1.5（LP-R2），这不是 Bixby–Martin 的测量——其预印本 PowerC（共享内存）版 4 处理器的实测加速为 1.1–5.3（表 11，LP-R25） |
| 单次迭代内任务 + 数据并行：SIP | FTRAN-DSE 与 PRICE/CHUZC1 重叠；FTRAN、FTRAN-BFRT、UPDATE-DUAL 并发 | Huangfu–Hall [LP-S1 §4.4.1, PDF pp. 90–91; LP-S2 §4, PDF p. 15]；MPC 版另称 SIP 也扩展了 Forrest 的 Aboca [LP-S4 §2.2.4, §4, PDF pp. 8, 16] | LP-R5, LP-R6 |
| 跨迭代任务并行：multiple pricing / suboptimization | 一次选多个候选做 minor iterations，把多个 BTRAN/FTRAN 变成并行任务 | 原始：PARSMI [LP-S49]、ASYNPLEX [LP-S51]，一手来源也把 Wunderling [LP-S50] 列为原始 [LP-S1 Table 4.2, §4.1.2, PDF pp. 72–73; LP-S6 §2.2, PDF p. 4]——原文核对：其 block pivoting 推导了 einfügend 与 entfernend 两种形式（列基下即原始与对偶），制表的并行单纯形测量全是对偶 [LP-S50 PDF pp. 47, 121–122, 172, 176]；对偶：ParISS 原型 [LP-S6 §3, PDF p. 5]、PAMI [LP-S1 §4.3, PDF pp. 79–90; LP-S2 §3, PDF pp. 9–15] | 原始版（PARSMI、ASYNPLEX）加速有限且曾以数值不可靠为代价（LP-R25）；PAMI 均值 1.49 / 1.51（LP-R3, LP-R4） |
| 结构利用 / 分布式内存 | 利用块角结构做数据并行 | Lubin 等 [LP-S54，据 LP-S1 §4.1.3, PDF p. 76]；Smith 的 BALP（i7）[LP-S11 PDF p. 19] | 块角随机 LP 上极高效但限于该类（LP-R25）；BALP 被自评 "of little value" [LP-S11 PDF p. 25] |
| 重叠 INVERT | 新的分解在后台进行，就绪后用更新追上 | 论文转述的两项早期工作（加速 1.3–1.5，未入正典）[LP-S1 §4.1.2, ch. 5, PDF pp. 73, 95] | 复用 PF 追赶会数值不稳 [LP-S48，据 LP-S1 §4.1.2, PDF p. 73]；PAMI 不重叠 INVERT，FT 追赶式重叠只是提议 [LP-S1 ch. 5, PDF p. 95] |

## 共识（蒸馏进「框架概览」）

1. **对偶修正单纯形是大规模稀疏 LP 的首选单纯形变体**，转折点是 1990 年代的 DSE 与 BFRT
   [LP-S1 §1, PDF p. 16; LP-S2 §1, PDF p. 2; LP-S13 PDF p. 16; LP-S10 PDF p. 11]。
2. **大规模稀疏 LP 要用修正单纯形而非 tableau**；稠密 tableau 的并行加速再大，也不敌好的串行稀疏修正单纯形
   [LP-S10 PDF pp. 8, 17; LP-S1 §4.1.1, PDF pp. 70–71; LP-S2 §1, PDF pp. 1–2]。
3. **高效实现必须利用稀疏与超稀疏**；通用判据是 Hall–McKinnon 的：结果密度低于 10% 为超稀疏，超过 60% 的结果为超稀疏的 LP 是超稀疏模型
   [LP-S45，据 LP-S1 §1.3, PDF p. 19; LP-S2 §5.1, PDF p. 16; LP-S5 §4, PDF p. 13; LP-S7 §1, PDF p. 2]。
   （[LP-S7] 写作「每一类结果都超过 60%」；论文没说 60% 判据作用于 FTRAN、BTRAN 还是两者。）
4. **FT 类 LU 更新被广泛认为最高效，PF 最简单** [LP-S5 §1, §2.1, PDF pp. 2, 4; LP-S6 §2, PDF p. 3; LP-S1 §2.4.2, PDF p. 35]。
5. **并行只有建立在高效串行实现之上才有意义**；串行低效会人为放大并行余地
   [LP-S6 §3, PDF pp. 5–6; LP-S2 §2, PDF p. 3; LP-S53，据 LP-S6 §2.2, PDF pp. 3–4]。
6. **高效修正单纯形的并行加速远非线性**：串行的 INVERT 拖累了此前所有数据并行与任务并行实现，只并行部分组件受 Amdahl 定律限制
   [LP-S10 PDF p. 17; LP-S1 §4.2.1, PDF pp. 76–77; LP-S2 §6, PDF pp. 24–25]。
7. **作为定价规则，suboptimization 劣于常规 DSE**；DSE 与 BFRT 被视为最好的规则
   [LP-S2 §2.3, §6, PDF pp. 8, 24; LP-S1 ch. 5, PDF p. 95]。

## 分歧（保留原样，蒸馏进「流派对比」）

1. **扰动是什么**：A——论文转述的传统看法视扰动为解决退化的补救，并引 Maros 称其缺乏理论美感但实用价值无疑
   [LP-S25，据 LP-S1 §3.3.2, PDF p. 62]；B——论文转述 Bixby：Cplex 5.0 至 7.1 的主要提速来自更激进的对偶扰动（尤其在解 pds 问题时），并建议把扰动当作算法手段
   而不只是退化的补救，但没有给进一步的解释或细节 [LP-S22，据 LP-S1 §3.3.2, PDF p. 62]；C——Huangfu 论文与 Hall–Huangfu 给出机制：扰动让 BFRT 起作用、稠密行吸引力下降，
   从而提升超稀疏性 [LP-S1 §3.3.2, PDF pp. 62–64; LP-S7 §3, PDF pp. 4–5]，论文把扰动尺度的这一面当作 B 的可能原因 [LP-S1 §3.3.2, PDF p. 64]。
   C 是诠释与启发式论证，只在 pds 与网络 LP 上做过（LP-R17, LP-R19）。原文核对：Bixby 只就 Cplex 7.1 在 PDS 模型上的表现列了三点——充分利用稀疏、
   对偶中更激进的扰动、bound flipping——三点并列、未分主次；「算法手段」出自括号里对 7.1 做法的描述，扰动在文中本就列为处理退化的手段 [LP-S22 TR01-20 pp. 9–10, 12, 14]。
   所以 A 与 B 并不对立：论文转述的原话就是「而不只是」退化的补救 [LP-S1 §3.3.2, PDF p. 62]；「主要提速来自扰动」才是转述加上的，原文也没有单独测过对偶扰动
   （见 LP-S22 原文核对）。
2. **加权扰动**：Koberstein 称按列非零数加权的扰动能延缓稠密列的扩散 [LP-S23，据 LP-S1 §3.2.3, PDF p. 60]；
   论文称该说法既无数值支持、本研究也未证实，HSOL 改用不加权的简化版 [LP-S1 §3.2.3, §3.3.2, PDF pp. 59–60, 62]。
   原文核对：论文引的是 2008 年期刊文（正文未读）；作者 2005 年博士论文的权重与论文表 3.3 所转述的相同（与 2008 年文是否全同未核）[LP-S60 PDF p. 99; LP-S1 §3.2.3, PDF p. 60]，给的理由是在退化留下的选择余地里挑非零少的入基列，
   使 LU 更新的 spike 更稀疏、填充更少，并称其扰动与 COIN LP 的相似 [LP-S60 PDF pp. 98–99]——「延缓稠密列扩散」是论文的转述用语，LP-S60 没有这种说法；
   源码核对：Clp 自 2003-10-15 的提交起已按列非零数加权 [LP-S55 ClpSimplexDual.cpp l. 3131–3193 @29f4248e63e3]。读到的两份文本都没有印出单独检验加权的结果
   （2008 年期刊文未读）：Koberstein 2005 把扰动与 BFRT 放在同一步（Ver. 6）加入 [LP-S60 PDF pp. 138–140]；论文印出的只有扰动开与关的对比，
   加权与不加权只有一句「本研究的计算经验未能证实」，没有数字 [LP-S1 §3.2.3, §3.3, PDF pp. 60–62, 65, 67–68]。
3. **FT 类更新的数值优势从哪来**：传统理由是稳定性——Bartels–Golub 因 PF 的稳定性顾虑把 LU 引入单纯形，Bartels 在更新时做部分主元
   [LP-S35, LP-S36，据 LP-S5 §3.1.2, PDF p. 9]；ERGO-13-001 主张现代 FT 类代码 "include no numerical pivoting"，其数值优势只能来自删去
   病态基留下的 eta 与更少存储（更少 flop），而 PF 类更新在多数 LP 上并不出问题、出了问题也可由重新求逆修正 [LP-S5 §3.1.2, PDF pp. 9–10]。
4. **FTRAN 与 FTRAN-DSE 的任务并行**：Bixby–Martin 考虑过，认为计算上不利而放弃 [LP-S52，据 LP-S2 §2.2.4, PDF p. 6; LP-S1 §4.1.2, PDF p. 75]；
   Huangfu 论文主张利用超稀疏后两者的成本差距很大，BFRT 又带来第三个方程组，任务并行重新有了价值（SIP 的出发点）
   [LP-S1 §4.1.2, PDF p. 75; §4.4.1, PDF p. 90]。期刊版把 SIP 表述为对其工作的发展而非反驳，并警告朴素的重叠效率低 [LP-S2 §4, PDF p. 15]。
   原文核对：Bixby–Martin 不只是考虑过——串行 Cplex 已按 Forrest–Goldfarb 的建议把两次求解合在一次 LU 遍历里，计算量有所减少、缓存用得很好，
   他们把两者拆开并行的尝试全都更慢（未给数字）[LP-S52 SC-95-45 PDF pp. 4–5, 18]。Wunderling 1996 实现并测量了同一迭代中第二、第三个方程组的并发求解
   （只用于 steepest edge，只能用上 2 个处理器；列基的对偶里这两个即 FTRAN 与 FTRAN-DSE，这是本语料按其算法 6 的推断，测量时行数多于列数的 18 题用的是行基）：
   不用 block pivoting 时，加上这种并发求解后，2 个处理器与 1 个处理器的运行时间之比在 SMoPlex 由 88% 降到 84%（总求解时间之比），在 DoPlex 平均由 77% 降到 70%
   （均值类型未说明）；他的结论是这种并行不总是划算，原因之一正是高效的串行实现只需一次 LU 遍历 [LP-S50 PDF pp. 63–64, 100, 122, 172, 174, 176–177, 186, 189]。
5. **修正单纯形值不值得并行**：常见看法（Hall 综述所载）是加速难以扩展、修正单纯形不适合并行 [LP-S53，据 LP-S2 §1, PDF p. 2; LP-S1 §4.2.1, PDF p. 77]；
   Huangfu–Hall 主张背景已变：对偶成为首选、多核桌面普及，任何加速都值得 [LP-S1 §1, PDF pp. 16–17; LP-S2 §1, PDF p. 2]。
   原文核对：Bixby 2002 年写道，barrier 能在很宽的问题规模上被很有效地并行，单纯形法 "in this sense" 没有被成功并行化 [LP-S22 TR01-20 p. 9]；
   他与 Martin 的预印本说，用分布式内存在一般测试集上看来难有好的并行性能，但分布式代码对单机内存放不下的大模型仍有用；对共享内存的 PowerC 版则说在很多模型上
   结果相当好 [LP-S52 SC-95-45 PDF pp. 10, 21]；Wunderling 的结论是 2 个处理器的并行看来可用于一般 LP，多于 2 个只对行数与列数相差很大的 LP 有意义，
   block pivoting 只宜用于迭代数增加不多的问题类 [LP-S50 PDF p. 186]。
6. **partial CHUZR 有没有用**：APMOD12（网络 LP）称它有望在稠密行主导之前避开它们，NETGEN 平均时间因子 1.73 [LP-S8 PDF pp. 21–22]；
   论文（pds）称它在 pds-20 上只略有帮助、对较大 pds 不合适且拖慢 LiDSE，并说对偶中的 partial CHUZR 远不如原始中的 partial pricing 可取
   [LP-S1 §3.3.3, §3.3.5, PDF pp. 64–67]。源码核对：Clp 把它作为对偶 CHUZR 的默认（超出容差的不可行项不多于 2000 个时仍是全扫，见上文 C 表），头文件注释说它在很简单的问题上可能更快 [LP-S55 src/ClpDualRowSteepest.hpp l. 81–87, src/ClpSimplex.cpp l. 162 @874465237db8]；
   原文核对：Koberstein 2005 在 13 个大的 Netlib 题上加入随机化 partial pricing（即对偶的 partial CHUZR，Ver. 12）后总时间 −15.0%、迭代 −0.4%，其中 KEN-18 一题由 87.16 降到 59.44 s
   （总和 201.33 → 171.13 s；13 题中 4 题变慢）[LP-S60 PDF pp. 117, 139, 171]。结论随问题族而变；pds 与 NETGEN 之外，语料里单独检验它的只有这 13 题
   （neos1、stormG2-1k 只有与其它技术合用的结果，LP-R20），且 13 题的时间收益几乎全来自 KEN-18 一题，不得合并成一句「有用」或「没用」。
7. **APF 的评价口径**：ERGO-13-001 按逐题排名称 APF 在 16 题最差、不推荐作一般技术 [LP-S5 §4–§5, PDF pp. 16–17]；EUROPT17 按归一化
   几何均值给 APF 0.95（PFI = 1.00），称 "APF little better than PFI" [LP-S15 PDF p. 16]。两种统计口径并存（LP-R13, LP-R14）。
8. **对偶单纯形 vs barrier**：同一份幻灯片里两张 CPLEX 图分别写 "Dual simplex better than primal but barrier clearly better" 与
   "Little to choose between dual simplex and barrier with crossover"（图无标注，数据来源与版本未印）[LP-S10 PDF pp. 12–13; LP-S11 PDF p. 10]；
   另一份幻灯片转述 Hall–McKinnon：超稀疏 LP 上单纯形通常好于 IPM，其它 LP 常常不然 [LP-S9 PDF p. 20]。语料没有统一结论。
9. **PAMI 与 suboptimization 的关系**：论文第 5 章与期刊摘要称 PAMI 基于、扩展 suboptimization [LP-S1 ch. 5, PDF p. 94; LP-S2 abstract, PDF p. 1]；
   论文 §4.3.1 却强调两者目的不同（PAMI 只借它取得任务并行的余地），并说 PAMI 更接近 Wunderling 与 PARSMI [LP-S1 §4.3.1, PDF p. 80]。
   同一作者不同章节的侧重不同（推断）；语料没有自行调和。
