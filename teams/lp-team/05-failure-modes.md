# LP Team · 胡说陷阱清单

蒸馏出的 skill 必须把本清单整体移植进「绝不做」部分，一条不删。每条给出错误说法与反驳它的语料 ID。

## F1 把 PAMI、SIP、ParISS 与经典 multiple pricing 混为一谈
- **错误说法**：「SIP 也基于 suboptimization」「PAMI 是单次迭代内的并行」「ParISS 就是 PAMI」「Huangfu 发明了对偶多候选定价」。
- **语料怎么说**：PAMI 是跨多次迭代的并行，建立在对偶 suboptimization 之上、配候选质量控制 [LP-S2 abstract, §3, PDF pp. 1, 9–14; LP-S1 §4.3, PDF pp. 79–90]；
  SIP 是常规 DSE 对偶单纯形在单次迭代内的组件重叠 [LP-S2 §4, PDF p. 15; LP-S1 §4.4.1, PDF pp. 90–91]；ParISS 是 PPAM'11 的 PF 原型，期刊版称其
  "relatively unsophisticated, both algorithmically and computationally" [LP-S2 §3, PDF p. 9]，MPC 版称 pami 串行快它近一个数量级 [LP-S4 §3, PDF p. 10]；
  2010–2011 年的来源从不用 PAMI、SIP 两词 [LP-S6; LP-S12]。多候选思想：原始 multiple pricing 出自 Orchard-Hays [LP-S46]，对偶 suboptimization 出自 Rosander [LP-S47]
  （据 LP-S1 §4.3.1, PDF p. 80; LP-S6 §2.1, PDF p. 3）。PAMI 的展开也有两种：论文与期刊写 parallelism across multiple iterations，HSOL README 写 "parallel minor iterations"
  [LP-S17 l. 11–12]。

## F2 HSOL / hsol / HiGHS 的归属说错
- **错误说法**：「Huangfu 一人写了 hsol 的全部（含 presolve、crash）」「Huangfu 写了 HiGHS」「HiGHS 就是 HSOL 改名」「Huangfu 在现任 HiGHS 团队里」。
- **语料怎么说**：README："HSOL was originally written by Qi Huangfu"，presolve、crash 与 advanced basis start 由 Hall 与 Galabova 加入 [LP-S17 l. 21–23]；期刊版写
  "the authors have implemented a sequential dual simplex solver (hsol) from scratch"（两人署名）[LP-S2 §1, PDF p. 2]；ERGO-13-001 同时用「Huangfu 的」与「Huangfu 和 Hall 的」
  两种说法 [LP-S5 §2.1, §4, PDF pp. 6, 13]；幻灯片把 hsol 的 presolve 记给 Galabova、crash 记给 Hall 与 Galabova [LP-S14 PDF p. 5]。HiGHS 的原始与对偶修正单纯形
  "originally written by Qi Huangfu and further developed by Julian Hall"，IPM、QP、MIP 求解器分别由 Schork、Feldmeier、Gottwald 编写 [LP-S18 l. 54]；highs.dev 说 HiGHS
  基于 Huangfu 开发的对偶单纯形，项目由 Hall 管理 [LP-S19 l. 106–114]，其 "The Team" 名单里没有 Huangfu [LP-S19 l. 123–137]；highs.dev 的 "novel" 说的是 Schork 的
  IPM，不是单纯形 [LP-S19 l. 109–110]。HSOL 到 HiGHS 的直接演化语料没有明说，只有措辞与署名的重合 [LP-S17; LP-S18]。

## F3 COPT 与 FICO Xpress：归属说过头，或编造闭源内部机制
- **错误说法**：「Huangfu 一人开发了 COPT」「Huangfu 任职于 Cardinal Operations」（当作来源事实）「COPT 的单纯形用了 PAMI」「Xpress 里实现了 SIP / MPF」「COPT 有 GPU 单纯形」。
- **语料怎么说**：JuliaCon 简介称 "Qi Huangfu is the developer of COPT"，并参与过 HiGHS 与 FICO-Xpress [LP-S20 l. 15]；手册称 COPT 由 Cardinal Operations 开发、列 5 位手册作者，
  不分配组件，也不印个人隶属 [LP-S16 §1.3–§1.4, PDF pp. 17–18]。Xpress 方面语料只有："One of the authors has implemented the techniques underlying PAMI within the FICO Xpress simplex solver"
  [LP-S2 abstract, PDF p. 1]、§6 所说的 Huangfu 对 Xpress 的改进 [LP-S2 §6, PDF p. 25] 与幻灯片 "pami ideas incorporated in FICO Xpress (Huangfu 2014)" [LP-S14 PDF p. 12]；FICO 博客正文未读 [LP-S58]；
  Xpress 的版本、实现细节、是否含 SIP 均未说明（LP-R9）。COPT 手册只给参数层：DualPrice 0 = Devex、1 = 对偶 steepest edge、默认自动；DualPerturb 开关；日志 "up to 8 threads"
  但不说如何并行；GPU 只用于 PDLP 与 barrier [LP-S16 §11.3, §20.3.1, PDF pp. 151–152, 234]。

## F4 夸大加速比：拿错基线
- **错误说法**：「PAMI 让对偶单纯形快 2.3 倍」「ParISS 在 8 核上快 3 倍」「SIP 平均快 1.3 倍」「扰动让 pds-20 快 4.7 倍」。
- **语料怎么说**：2.23（论文）与 2.34（期刊）是 8 核 PAMI 相对**串行 PAMI**；相对 HSOL/hsol 只有 1.49 / 1.51，串行 PAMI 本身就慢（0.67 / 0.64）（LP-R3, LP-R4）；
  ParISS 的几何均值加速是 1.16 / 1.28 / 1.30（2/4/8 核），只覆盖 114 题里筛出的 13 题，3.39 是 stocfor3 一题且该题 8 核仍慢于 Clp（LP-R22）；SIP 均值 1.13 / 1.15（LP-R5, LP-R6）；
  pds-20 的 4.7 倍是迭代速度，总时间减 84%、迭代减 23%（LP-R17）；"solved 350% faster"（netgen114）无法换算成倍数，也不等于幻灯片的最大因子 6.16（LP-R19）。

## F5 把 comparable / competitive 升级成 beats
- **错误说法**：「PAMI 比 Cplex 快」「HSOL 串行胜过 Cplex」「论文证明 HSOL 比 Clp 快」。
- **语料怎么说**：论文只说 PAMI 与 Cplex 的对偶单纯形 comparable（performance profile），期刊只说 pami8 与 sip8 中较好者在多数测试题上与 Cplex 12.4 comparable（LP-R8）；
  论文第 5 章的总结把串行 HSOL 对标 Clp（comparable）、把并行 PAMI 对标 Cplex [LP-S1 ch. 5, PDF p. 94]；ERGO-13-001 表 2 有许多题 cplex 快得多（CRE-B 2.1 s vs hsol 6.4 s；
  SGPF5Y6 7.9 vs 180.2）（LP-R11）；LiDSE 系列只在 pds-30 到 pds-100 上与 Cplex 相当，只有指数 1.2 的变体逐题快于 Cplex（LP-R18）；「hsol 比 Clp 快 2.29 倍」是期刊版对
  Clp 1.15、无预处理与 crash 的结果（LP-R10），不是论文的结论。

## F6 把 pds / 网络专用技巧推广到一般 LP
- **错误说法**：「LiDSE 普遍优于 DSE」「over-weighting 就是 1-范数 steepest edge」「成本扰动在任何 LP 上都会提升超稀疏性」「partial CHUZR 总能加速」「三种技术合用总是最好」。
- **语料怎么说**：LiDSE 依赖 pds 的表元多为 ±1，对一般 LP 可能严重损害效率，"its scope for further application is fairly limited"（LP-R18）；over-weighting 等于 1-范数
  steepest edge 只对网络 LP 成立（LP-R21）；扰动机制只在 pds-20 与网络 LP 上分析过，一般 LP 的证据只有 pds-100、neos1、stormG2-1k 三题，stormG2-1k 的因子全为 1.0
  （LP-R17, LP-R19）；partial CHUZR 在较大 pds 上不合适（LP-R18）；组合技术在 pds-100 与 neos1 上的迭代与时间因子低于单用扰动（LP-R20）。

## F7 把背景技术的发明权记到 Huangfu（或 Hall–Huangfu）名下
- **错误说法**：DSE、BFRT、Harris 检验、超稀疏求解、FT 及其 BTRAN 捷径、suboptimization、成本扰动、partial CHUZR、对偶 phase I、稀疏 LU，或对偶单纯形本身，是他们的发明。
- **语料怎么说**（均据一手来源的署名）：DSE—Forrest–Goldfarb [LP-S28]；BFRT—Fourer [LP-S29]；两遍比率检验与 Devex—Harris [LP-S26]；超稀疏性—Hall–McKinnon [LP-S45]，
  DFS 三角求解—Gilbert–Peierls [LP-S44]；FT—Forrest–Tomlin [LP-S37]，省去额外部分 BTRAN—Tomlin (1974) [LP-S38]；suboptimization—Rosander [LP-S47]；成本扰动—Koberstein 与 Clp
  [LP-S23; LP-S8 PDF p. 7]；partial CHUZR—Clp（作者不知有发表文献）[LP-S7 §4, PDF p. 5]；对偶 phase I—Koberstein–Suhl [LP-S24]；稀疏 LU—Suhl–Suhl [LP-S33]；对偶单纯形—Lemke [LP-S21]。
  来源自称新的只有：APF、MPF、CFT [LP-S5 §3.1, PDF p. 6]；超稀疏性提升的诠释与 LiDSE [LP-S1 §3.3]；over-weighted CHUZR（Hall 与 Huangfu 的幻灯片）[LP-S8 PDF pp. 23, 27]；
  PAMI 与 SIP 的设计 [LP-S1 ch. 4; LP-S2]；置换因子上的 DFS 伪代码，以及维护行式与超稀疏结构的 FT 实现文档 [LP-S1 §2.3.3, §2.4.3, PDF pp. 32–38]。

## F8 把诠释或启发式论证说成定理；编造收敛与复杂度结果
- **错误说法**：「论文证明了扰动会提升超稀疏性」「dense columns have larger perturbed dual values 是定理」「语料给了 PAMI 的收敛或反循环保证」「suboptimization 的迭代数有界」。
- **语料怎么说**：论文的「扰动 → BFRT → 稠密行吸引力下降」是基于 pds-20 的诠释，原话 "computational experiences suggests" [LP-S1 §3.3.2, PDF p. 64]；APMOD12 的网络分析用 Claim 与
  it can be argued，是启发式论证 [LP-S7 §3, PDF pp. 4–5; LP-S8 PDF p. 16]。语料里被证明的只有代数恒等式与成本模型推导（LP-R2, LP-R15, LP-R16, LP-R21）；「原始与对偶可行即最优」
  在期刊里只写「可以证明」、未给证明 [LP-S2 §2.1, PDF p. 4]。任何收敛速率、迭代复杂度、反循环保证、误差界，语料都没有——答「语料未覆盖」。

## F9 混用版本与表号
- **错误说法**：把论文（2013）、ERGO-14-011、arXiv、MPC 的数字或表号混着引；把 ParISS（2011-05）、ParISS 2.0（2011-09）与 2010-12 原型当成一个；把论文与 ERGO-13-001 的更新实验
  当成同一测试集。
- **语料怎么说**：PAMI 均值论文 1.49、期刊 1.51，SIP 1.13 与 1.15——同一 30 题集、不同运行（LP-R3–R6）；ERGO、arXiv、MPC 三版数字相同但 MPC 表号重排、三版硬件句不同（LP-R4）；
  FICO 的广告措辞只在 arXiv v1 [LP-S3 §5.4, PDF p. 24]；更新实验论文版的 42% / 63% / 35% 与 ERGO-13-001 版的 40% / 61% / 34% 来自不同的 30 题集（LP-R12, LP-R13）；正文与表格不一致处
  照原样并列：SIP 在 Linf 520c 与 maros-r7 正文 1.31 / 1.12、表 1.37 / 1.22（LP-R6），MPF 正文 26 题、表中粗体 25 题（LP-R13）；ParISS 系列各看各的（LP-R22, LP-R23, LP-R24）；
  会议版 PPAM（LNCS）与期刊版 COAP 正文都未读，不得假定数值同报告版 [LP-S6; LP-S5]。

## F10 误读表列、实验口径与单位
- **错误说法**：把更新实验当整机求解时间；把 ftran / btran 列读成密度；把 "(ms)" 当毫秒照抄；把 Average 当算术均值；把「高效 X%」换算成倍数。
- **语料怎么说**：论文表 2.4 与 ERGO-13-001 表 1 计的是固定基序列上 update + FTRAN + BTRAN 的 CPU 时间、单位未印（LP-R12, LP-R13）；ftran / btran 列是密度低于 10% 的结果所占
  比例 [LP-S1 §1.3, PDF p. 19]；论文表 4.3、期刊表 4 与 Gantt 图注印 "ms"，正文却写 microseconds，冲突未解（LP-R1, LP-R5）；APMOD12 的 Average、Improvement factors、Speed 均未定义
  （LP-R19）；「高效 X%」这类百分比如何对应时间比来源没说，只有 40% 与 42% 明说是几何均值（LP-R12, LP-R13）；hsol 的 159 题测试排除了 7 道 hard 题、忽略了 82 道最快解时间低于 0.1 s 的题，
  且不开 presolve 与 crash，幻灯片只有图、没有可读数值 [LP-S13 PDF pp. 37–39; LP-S14 PDF pp. 9–11]。

## F11 把基准快照当成常量
- **错误说法**：「Xpress 是最快的商业单纯形求解器」「Cplex 没有并行单纯形」（当作现状）；不带版本地说「比 Clp/Cplex 快」；不带日期地列 HiGHS 团队。
- **语料怎么说**："Xpress simplex solver now fastest commercial simplex solver" 是 2016–2017 年幻灯片的话，无版本、测试集、硬件，图中只有 cplex（LP-R9）；
  "Cplex (which has no parallel simplex facility)" 是 ERGO-14-011 在 Cplex 12.4 时代的陈述（LP-R9）；Mittelmann 页面自 2018 年起移除了若干商业求解器的结果，2013–2016 年的状态未核 [LP-S57]；对照版本随来源变：
  Clp 1.06 / 1.14 / 1.15 / v1.16、Cplex 12.4 / v12.5 [LP-S55; LP-S56]；highs.dev 团队名单是 2026-10-27 的快照 [LP-S19]；同一论文三版的硬件不同 [LP-S3; LP-S4]。

## F12 把联合工作或他人工作记到 Huangfu 一人名下；误用 MPF 与 glop
- **错误说法**：Smith 的 GPU 标准单纯形与 BALP 结果、Lubin 等人的块角随机 LP 求解器（5 亿变量、8192 个 Blue Gene 核）、2005 与 2013 年的 COAP 奖是 Huangfu 的；MPF 用在 hsol 或 pami 里；
  Huangfu 或 Hall 写了 Google glop；ParISS 是 Huangfu 写的。
- **语料怎么说**：幻灯片是联合署名：GPU 的 i6/i8 与 BALP 的 i7 记给 Smith [LP-S11 PDF pp. 16, 19; LP-S9 PDF p. 53]；随机 LP 记给 "Lubin, H et al." [LP-S13 PDF p. 25; LP-S54]；三项 COAP 奖中只有 2015 年
  （更新技术）涉及 Huangfu [LP-S13 PDF pp. 2, 21, 25, 29; LP-S59]——SIOPT17 把该奖印在 pami 幻灯片旁，却没说是哪篇获奖 [LP-S14 PDF p. 8]。MPF："Not used by h2gmp! Used by Google in glop"
  [LP-S15 PDF p. 19]，"Not used by pami!" [LP-S13 PDF p. 32]；谁在 glop 里实现 MPF 未说明；SIOPT17 只列 Google (techniques in glop) [LP-S14 PDF p. 13]。明确署名给 Huangfu 的只有 2010 年的原型
  （"Written by Qi Huangfu (2010)" [LP-S10 PDF p. 23; LP-S11 PDF p. 21]）与 HSOL 的原始编写 [LP-S17 l. 21]；ParISS 由谁编写两份来源都没说 [LP-S6; LP-S12]；EUROPT17 结论页的第一人称句不知是谁讲的 [LP-S15 PDF p. 22]。

## F13 直接搬用最大化形式
- **错误说法**：照抄 HSOL README 或幻灯片里的 max 形式、照抄「BFRT 最大化对偶目标」，而不换成用户约定的 min 形式。
- **语料怎么说**：HSOL README 把问题写作 "Maximize c^Tx subject to L <= Ax <= U; l <= x <= u" [LP-S17 l. 8]，等价的最小化是 min (−c)^T x，约束不变，最优值取负；幻灯片的对偶 (D) 写作
  maximize b^T y s.t. A^T y + s = c, s ≥ 0 [LP-S10 PDF p. 4; LP-S8 PDF p. 3; LP-S13 PDF pp. 8–9]，即 min −b^T y s.t. A^T y + s = c, s ≥ 0；「BFRT 最大化对偶目标」[LP-S13 PDF p. 15] 即最小化负的对偶目标；
  COPT 手册的 LP 例 (12.3) 是最大化 [LP-S16 §12.1, PDF p. 170]。论文、ERGO 系列、HiGHS 与 COPT 的向量形式本来就是 min 形式 [LP-S1 §3.1.1, PDF p. 48; LP-S2 §2.1, PDF p. 3; LP-S18 l. 47–52; LP-S16 §12.1.1, PDF p. 169]。
