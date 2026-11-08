# LP Team · 正典文献表

验证层级定义见 `standards/grounding.md`。本语料是**封闭语料**：

- 一手来源 [LP-S1–S20] 于 2026-10-27 下载，转成文本（PDF 每页以 `=== <stem> | PDF page N ===` 起头），由八份读者
  笔记逐页抽取后汇总于此。下表「定位/核实」列给出 URL、下载日期、版本、txt stem 与读过的范围。
- 背景文献 [LP-S21–S59] 只核实了**元数据**（Crossref、出版社落地页、zbMATH、作者本人出版物页、图书馆目录等，
  2026-10-27），**正文未读**。它们在本语料中的全部内容都是「某一手来源如此转述」（cited-by-source）：引用时必须连同
  转述它的一手来源 ID 一起说，不得写成「X 证明了…」。「角色」列即一手来源怎么说它，附锚点。
- 锚点写法：`[LP-S1 §3.2.3, PDF p. 55]`；幻灯片只有 PDF 页；README / 网页用 txt 行号 `l. N`。论文印刷页 = PDF 页 − 1；
  COPT 手册印刷页 = PDF 页 − 14；MPC 期刊页 = PDF 页 + 116；其余报告印刷页 = PDF 页（ERGO-11-007 的 PDF pp. 2–8 除外，
  为 PDF 页 − 1）。
- 背景文献的元数据以记录为准；一手来源印法与记录不一致处在行内注明（不是对记录的怀疑，是引用方的笔误）。
  仍未定的字段标「需核对」。

## 一手来源（verified-web：2026-10-27 下载并阅读，版本与范围如注）

| ID | 文献 | 定位/核实 | 角色 |
|----|------|-----------|------|
| LP-S1 | Huangfu (2013), "High performance simplex solver", PhD thesis, University of Edinburgh | https://era.ed.ac.uk/handle/1842/7952（下载 2026-10-27；stem `thesis-2013`）；全文已读（PDF pp. 1–99，分三段读）；ERA 条款称论文 "cannot be reproduced or quoted extensively from"——本语料只作短引 | HSOL 的完整设计：LU、超稀疏求解与 PF/FT/APF/MPF/CFT 更新（Ch. 2），对偶算子、扰动与超稀疏性提升（Ch. 3），PAMI 与 SIP（Ch. 4），贡献与未来工作（Ch. 5） |
| LP-S2 | Huangfu, Hall (2014 报告号；题页印 2015-03-06), "Parallelizing the dual revised simplex method", ERGO Technical Report 14-011 | https://webhomes.maths.ed.ac.uk/hall/HuHa13/ERGO-14-011.pdf（下载 2026-10-27；stem `ERGO-14-011`）；全文已读（PDF pp. 1–26）；参考文献访问日期为 20/01/2016，故是题页日期之后修订过的文本（读者推断）；§5.1 的硬件句、§3 与 §5.4 各一句在 PDF 文字层本身断裂 | PAMI 与 SIP 的**阅读主本**：设计、剖面、全部结果表（数字以此版为准） |
| LP-S3 | Huangfu, Hall (2015), "Parallelizing the dual revised simplex method", arXiv:1503.01889 v1（6 Mar 2015） | https://arxiv.org/abs/1503.01889（下载 2026-10-27；stem `arXiv-1503.01889`）；全文已读（PDF pp. 1–27），只作版本对照；文件印日期 "October 16, 2018" 等于 PDF 生成日期（读者推断为重生成日期） | 版本差异：硬件句写 "16 (Intel Xeon E5620, 2.4GHz) processors"、用 8 个；摘要与 §5.4 含 FICO "advertising copy and blogs" 措辞（ERGO 与 MPC 版均无） |
| LP-S4 | Huangfu, Hall (2018), "Parallelizing the dual revised simplex method", Mathematical Programming Computation 10(1):119–142, DOI 10.1007/s12532-017-0130-5 | 作者本 https://webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf（下载 2026-10-27；stem `HuHa13-MPC2018`；CC BY 4.0）；全文已读（PDF pp. 1–26）；表格在文字层只剩标题，数值按页面图像核对，与 [LP-S2] 相同但表号重排（MPC 表 4/5/6 = ERGO 表 5/6/4）；Received 6 March 2015, Accepted 10 February 2016, online 14 December 2017；元数据另经 Crossref 核实 | 正式发表版；独有内容：Aboca 定位、对 ParISS 的串行比较、硬件 "two Intel Xeon E5-2670s"、Wunderling 的 suboptimization 试验；HiGHS 指定的引用文献即此篇 |
| LP-S5 | Huangfu, Hall (2013), "Novel update techniques for the revised simplex method", ERGO Technical Report 13-001（7 July 2013）；期刊版 Computational Optimization and Applications 60(3):587–608 (2015), DOI 10.1007/s10589-014-9689-1 | https://webhomes.maths.ed.ac.uk/hall/HuHa12/ERGO-13-001.pdf（下载 2026-10-27；stem `ERGO-13-001`）；报告全文已读（PDF pp. 1–19）；期刊版元数据经 Crossref/Springer 核实 2026-10-27，**期刊版正文未读**；多份幻灯片印作 60(4)，记录为 60(3) | APF、MPF、CFT 三种更新的原始报告、计算比较（表 1–3）与数值稳定性论证 |
| LP-S6 | Hall, Huangfu (2011), "A high performance dual revised simplex solver", ERGO Technical Report 11-007（12 May 2011）；会议版 PPAM 2011, LNCS 7203, pp. 143–151 (2012), DOI 10.1007/978-3-642-31464-3_15 | https://webhomes.maths.ed.ac.uk/hall/HaHu11/ERGO-11-007.pdf（下载 2026-10-27；stem `ERGO-11-007`）；报告全文已读（PDF pp. 1–8）；会议版元数据经 Crossref/Springer 核实，**LNCS 版正文未读**（不得假定数值与报告相同） | ParISS：带 suboptimization 的对偶修正单纯形原型及其 1/2/4/8 核结果（表 1） |
| LP-S7 | Hall, Huangfu (2012), "Promoting hyper-sparsity in the revised simplex method", APMOD 2012 extended abstract（"Preprint submitted to Elsevier", March 29, 2012） | https://webhomes.maths.ed.ac.uk/hall/APMOD12/（下载 2026-10-27；stem `APMOD12-abstract`）；全文已读（PDF pp. 1–5）；会议名未印于正文，取自 manifest | 成本扰动 → BFRT → 超稀疏性提升的网络 LP 分析；netgen108 剖面与 NETGEN 汇总 |
| LP-S8 | Hall, Huangfu (2012), "Promoting hyper-sparsity in the revised simplex method", APMOD 2012 slides（28 March 2012） | 同上目录（下载 2026-10-27；stem `APMOD12-slides`）；全文已读（27 页） | over-weighted CHUZR（幻灯片自称新技术）、partial CHUZR 与成本扰动在 NETGEN 101–150 和三个一般 LP 上的结果 |
| LP-S9 | Hall, Smith, Huangfu (2010), "Towards a practical parallelisation of the revised simplex method", IMA NLAO talk slides（14 September 2010；署名印作 "Julian Hall, Edmund Smith and Huangfu Qi"） | https://webhomes.maths.ed.ac.uk/hall/IMA-NLAO_10/IMA-NLAO_10.pdf（下载 2026-10-27；stem `IMA-NLAO_10`）；全文已读（57 页） | 并行动机与内存访问瓶颈；提出未实现的 CPU+GPU 对偶方案；Smith 的 GPU 标准单纯形结果；超稀疏 LP 上单纯形与 IPM 的对比（转述） |
| LP-S10 | Hall, Huangfu, Smith (2010), "A high performance dual revised simplex solver", Oxford CMA seminar at RAL slides（2 December 2010） | https://webhomes.maths.ed.ac.uk/hall/RAL10/RAL10.pdf（下载 2026-10-27；stem `RAL10`）；全文已读（36 页） | 首个对偶原型（署 "Written by Qi Huangfu (2010)"）及 pds-06/pds-10 结果；alternative product form 的幻灯片推导；对偶 vs 原始 vs barrier 的图表 |
| LP-S11 | Hall, Huangfu, Smith (2011), "High performance computing and the simplex method", Lancaster talk slides（12 April 2011） | https://webhomes.maths.ed.ac.uk/hall/Lancs11/Lancs11.pdf（下载 2026-10-27；stem `Lancs11`）；全文已读（27 页） | 同一原型结果的复述与评语；三条并行路线的署名（"H and Qi"、"H and Smith"） |
| LP-S12 | Hall, Huangfu (2011), "A high performance dual revised simplex solver", PPAM 2011 talk slides（13 September 2011） | https://webhomes.maths.ed.ac.uk/hall/PPAM11/PPAM11.pdf（下载 2026-10-27；stem `PPAM11`）；全文已读（41 页） | ParISS 2.0 的串行与并行结果（含页间不一致）；Clp 的作者与 Hall 的项目经理身份 |
| LP-S13 | Huangfu, Hall (2016), "Novel update techniques for the revised simplex method (and their application)", ERGO seminar slides（30 November 2016；署名 "Qi Huangfu1 Julian Hall2 Others"，1 = FICO） | https://webhomes.maths.ed.ac.uk/hall/ERGO_301116/ERGO_301116.pdf（下载 2026-10-27；stem `ERGO_301116`）；全文已读（42 页） | 三项 COAP 奖的署名划分；pami 与 FICO Xpress；hsol 的 159 题测试设置；DSE 与 dual Devex 的初始化取舍；hsol 2016 年的缺口 |
| LP-S14 | Hall, Huangfu, Galabova (2017), "An open-source high performance dual simplex solver", SIAM Conference on Optimization slides（22 May 2017；Huangfu 署 FICO） | https://webhomes.maths.ed.ac.uk/hall/SIOPT17/SIOPT17.pdf（下载 2026-10-27；stem `SIOPT17`）；全文已读（14 页） | hsol 功能清单与组件署名；"Xpress simplex solver now fastest commercial simplex solver"；商业关联（Cargill、Google glop） |
| LP-S15 | Huangfu, Hall (2017), "Novel update techniques for the revised simplex method", EUROPT 2017 slides（13 July 2017；Huangfu 署 FICO） | https://webhomes.maths.ed.ac.uk/hall/EUROPT17/EUROPT17.pdf（下载 2026-10-27；stem `EUROPT17`）；全文已读（22 页）；讲者未注明 | 更新方法的归一化几何均值表；MPF "Not used by h2gmp!"；h2gmp 署名 "H, Huangfu and Galabova (2013–date)" |
| LP-S16 | Ge, Huangfu, Wang, Wu, Ye (2022; v4 2026), "Cardinal Optimizer (COPT) User Guide", arXiv:2208.14314 | https://arxiv.org/abs/2208.14314（下载 2026-10-27；v4 = COPT 8.0.1，2026-01-30；v1 2022-08-30；stem `COPT-guide-arXiv-2208.14314`）；共 1452 页，**只读 PDF pp. 15–18、151–158、167–171、231–240**；How to Cite 印年份 2023 | 产品手册：COPT 的 LP 方法与参数（LpMethod、DualPrice、DualPerturb、Crossover、GPU 只用于 PDLP/barrier）与日志；**不**说明哪位作者实现了哪部分 |
| LP-S17 | "Welcome to HSOL 1.0"（HSOL 1.0 README；无作者行、无日期） | 副本 https://github.com/mattmilten/h2gmp（last commit d1472d1e92c6, 2018-03-23；上游 galabovaa/h2gmp 已无法访问；下载 2026-10-27；stem `h2gmp-README`，锚点为 txt 行号）；全文已读（127 行） | HSOL 的作者句、PAMI/SIP 的名称与运行开关、线程建议；问题写成最大化形式 |
| LP-S18 | "HiGHS - Linear optimization software"（github.com/ERGO-Code/HiGHS README，branch latest） | 下载 2026-10-27（stem `HiGHS-README`）；全文已读（292 行）；未印 HiGHS 版本号（只有 NuGet 包 1.15.1） | HiGHS 各组件的作者句；问题形式；学术用户被要求引用 [LP-S4] |
| LP-S19 | highs.dev 首页 "HiGHS - High-performance parallel linear optimization software" | https://highs.dev（下载 2026-10-27；stem `highs-dev`）；全文已读（178 行，并对照 HTML 核过注释段） | Authorship 段；"The Team" 名单（2026-10-27 快照） |
| LP-S20 | Huangfu (2022), "COPT and its Julia interface", JuliaCon 2022 lightning talk page（July 27, 2022） | https://pretalx.com/juliacon-2022/talk/XRDNVT/（下载 2026-10-27；stem `juliacon22-talk`）；全文已读（27 行） | 讲者简介：Huangfu 是 COPT 的开发者，并参与过 HiGHS 与 FICO-Xpress 等求解器 |

## 背景文献 · verified-web（元数据于 2026-10-27 核实；正文未读，内容只经一手来源转述）

### verified-web · 对偶单纯形起源与综述

| ID | 文献 | 定位/核实 | 角色（cited-by-source） |
|----|------|-----------|------|
| LP-S21 | Lemke (1954). The dual method of solving the linear programming problem. Naval Research Logistics Quarterly 1(1):36–47 | DOI 10.1002/nav.3800010107（Crossref） | 对偶单纯形的首创者（1950 年代）[LP-S1 §3.1.2, PDF p. 50]；论文称直到 1990 年代中期才被认真视为更优的方法 [LP-S1 §3.2.1, PDF p. 53] |
| LP-S22 | Bixby (2002). Solving Real-World Linear Programs: A Decade and More of Progress. Operations Research 50(1):3–15 | DOI 10.1287/opre.50.1.3.17780（Crossref） | 论文转述：Cplex 5.0 至 7.1 的主要提速来自对偶中 "more aggressive perturbation in the dual"（尤其 pds 问题），并主张把扰动当算法手段而非退化补丁；论文说 Bixby 未给解释 [LP-S1 §3.3.2, PDF pp. 62, 64] |
| LP-S23 | Koberstein (2008). Progress in the dual simplex algorithm for solving large scale LP problems: techniques for a fast and stable implementation. Computational Optimization and Applications 41(2):185–204 | DOI 10.1007/s10589-008-9207-4（Crossref） | HSOL 的成本扰动是其方案的简化不加权版 [LP-S1 §3.2.3, PDF p. 59]；其加权扰动的稀疏性主张被论文判为无数值支持、未被证实 [LP-S1 §3.3.2, PDF p. 62]；Harris 与 BFRT 的实现细节出处 [LP-S2 §2.2.2, PDF p. 5]；对偶单纯形现代实现的全面讨论 [LP-S6 §2, PDF p. 2]；无数值主元的现代 FT 类描述 [LP-S5 §3.1.2, PDF p. 9]；成本扰动的出处之一 [LP-S7 §1, PDF p. 2] |
| LP-S24 | Koberstein, Suhl (2007). Progress in the dual simplex method for large scale LP problems: practical dual phase 1 algorithms. Computational Optimization and Applications 37(1):49–65 | DOI 10.1007/s10589-007-9022-3（Crossref + Springer） | HSOL 采用的对偶 phase I 子问题法；论文补写了它称原文 "not clearly expressed" 的 BOXED 变量处理 [LP-S1 §3.2.4, PDF p. 60]；达到对偶可行的最新技术 [LP-S6 §2, PDF p. 2] |
| LP-S25 | Maros (2002/2003). Computational Techniques of the Simplex Method. Springer, International Series in Operations Research & Management Science | DOI 10.1007/978-1-4615-0257-9（Crossref 记 2003；Springer 页记精装本 2002-12-31 出版、版权 2003；论文印 "Kluwer Academic Publishers, Boston, 2002"，"Boston" 未确认） | 论文引其语：扰动与 shifting "lack some theoretical beauty their practical usefulness is beyond any doubt" [LP-S1 §3.3.2, PDF p. 62] |

### verified-web · 定价与对偶比率检验

| ID | 文献 | 定位/核实 | 角色（cited-by-source） |
|----|------|-----------|------|
| LP-S26 | Harris (1973). Pivot selection methods of the Devex LP code. Mathematical Programming 5(1):1–28 | DOI 10.1007/BF01580108（Crossref；同名同作者另有 1975 年 Math. Programming Studies 章节，一手来源引的是 1973 年文） | Harris 两遍比率检验：被移植到对偶 CHUZC 并与 BFRT 结合 [LP-S1 §3.2.3, PDF pp. 58–59; LP-S2 §2.2.2, PDF p. 5]；Devex 定价：与 steepest edge 一起取代了 suboptimization [LP-S1 §4.3.1, PDF p. 80] |
| LP-S27 | Goldfarb, Reid (1977). A practicable steepest-edge simplex algorithm. Mathematical Programming 12(1):361–371 | DOI 10.1007/BF01593804（Crossref + Springer + zbMATH；论文把题名印作 "practical"） | steepest edge 与 Devex 成为公认定价规则之后，suboptimization 淡出 [LP-S1 §4.3.1, PDF p. 80] |
| LP-S28 | Forrest, Goldfarb (1992). Steepest-edge simplex algorithms for linear programming. Mathematical Programming 57(1–3):341–374 | DOI 10.1007/BF01581089（Crossref） | 对偶 steepest edge（DSE）及其权重更新公式与 10^-4 权重下限建议 [LP-S1 §3.2.2, PDF pp. 54–55; LP-S2 §2.2.1, PDF p. 5; LP-S6 §2, PDF p. 2; LP-S7 §1, PDF p. 1] |
| LP-S29 | Fourer (1994). Notes on the Dual Simplex Method. Draft report, Northwestern University（未发表；2000-08 上传 Optimization Online） | https://optimization-online.org/2000/08/214/（2026-10-27）；无 DOI | bound flipping ratio test（BFRT）的出处 [LP-S1 §3.2.3, PDF p. 57; LP-S2 §2.2.2, PDF p. 5; LP-S7 §1, PDF p. 1; LP-S8 PDF p. 5] |
| LP-S30 | Gill, Murray, Saunders, Wright (1989). A practical anti-cycling procedure for linearly constrained optimization. Mathematical Programming 45(1–3):437–474 | DOI 10.1007/BF01589114（Crossref） | EXPAND：HSOL 只取其严格零步（对偶形式），认为完整的扩张容差框架不必要 [LP-S1 §3.2.3, PDF pp. 58–59] |

### verified-web · LU 分解（INVERT）

| ID | 文献 | 定位/核实 | 角色（cited-by-source） |
|----|------|-----------|------|
| LP-S31 | Markowitz (1957). The Elimination form of the Inverse and its Application to Linear Programming. Management Science 3(3):255–269 | DOI 10.1287/mnsc.3.3.255（Crossref + zbMATH；论文印页码 255–296，以记录为准） | Markowitz merit：以 b_ij 为主元时的填充上界 [LP-S1 §2.2.6, PDF p. 27] |
| LP-S32 | Tomlin (1972). Pivoting for Size and Sparsity in Linear Programming Inversion Routes. IMA Journal of Applied Mathematics 10(3):289–295 | DOI 10.1093/imamat/10.3.289（Crossref、OUP 与 zbMATH 的记录题名都以 Routes 结尾，各一手来源印作 routines——引题名须连同此注；期刊名的印法不一） | 按 merit count 的列排序 + 阈值行选择，u 取 0.01 或 0.1 [LP-S1 §2.2.6, PDF pp. 27–28]；标准 INVERT 技术 [LP-S5 §1, PDF p. 2; LP-S6 §2, PDF p. 3] |
| LP-S33 | Suhl, Suhl (1990). Computing Sparse LU Factorizations for Large-Scale Linear Programming Bases. ORSA Journal on Computing 2(4):325–335 | DOI 10.1287/ijoc.2.4.325（Crossref） | HSOL 实现的稀疏 LU（按计数升序的 Markowitz 搜索、阈值主元），论文称其为商业与公开代码广泛接受的默认选择 [LP-S1 §2.2.6, PDF p. 28]；标准 INVERT 技术 [LP-S5 §1, PDF p. 2; LP-S6 §2, PDF p. 3] |

### verified-web · 基更新家族（APF、MPF、CFT 的背景）

| ID | 文献 | 定位/核实 | 角色（cited-by-source） |
|----|------|-----------|------|
| LP-S34 | Dantzig, Orchard-Hays (1954). The product form for the inverse in the simplex method. Mathematics of Computation 8(46):64–67 | DOI 10.1090/S0025-5718-1954-0061469-8（Crossref） | 最早也最简单的 product form（PF）更新；APF、MPF 是其变体 [LP-S5 §1, §2.1, PDF pp. 2, 4; LP-S6 §2, PDF p. 3] |
| LP-S35 | Bartels, Golub (1969). The simplex method of linear programming using LU decomposition. Communications of the ACM 12(5):266–268 | DOI 10.1145/362946.362974（Crossref） | 出于对 PF 稳定性的顾虑把 LU 分解引入单纯形实现 [LP-S5 §3.1.2, PDF p. 9] |
| LP-S36 | Bartels (1971). A stabilization of the simplex method. Numerische Mathematik 16(5):414–434 | DOI 10.1007/BF02169151（Crossref；[LP-S5 §1, PDF p. 2] 正文写 "Bartels and Golub [1]"，但其文献表 [1] 仅 Bartels 一人） | 更新 LU 时用部分主元保稳定 [LP-S5 §3.1.2, PDF p. 9]；被称为最高效更新类（FT、Reid、Suhl）的源头 [LP-S5 §1, PDF p. 2] |
| LP-S37 | Forrest, Tomlin (1972). Updated triangular factors of the basis to maintain sparsity in the product form simplex method. Mathematical Programming 2(1):263–278 | DOI 10.1007/BF01584548（Crossref） | FT 更新（列尖峰、行消去、原文需额外部分 BTRAN）；论文以基于行式表示的置零取代原文的 search-and-move [LP-S1 §2.4.2–§2.4.3, PDF pp. 34–38]；更新实验的基准与 CFT 的基础 [LP-S5 §2.1, PDF pp. 2, 4]；[LP-S2 §2.4, PDF p. 8] |
| LP-S38 | Tomlin (1974). On pricing and backward transformation in linear programming. Mathematical Programming 6(1):42–47 | DOI 10.1007/BF01580221（Crossref） | 用常规求得的部分 BTRAN 结果构造 FT 的行 eta，省去额外的部分 BTRAN [LP-S1 §2.4.2, PDF p. 35; LP-S5 §2.1, PDF p. 5] |
| LP-S39 | Reid (1982). A sparsity-exploiting variant of the Bartels—Golub decomposition for linear programming bases. Mathematical Programming 24(1):55–69 | DOI 10.1007/BF01585094（Crossref） | 作者选 FT 而不选 Reid 更新，理由是 FT 更适合超稀疏 LP；列为不做数值主元的现代代码之一 [LP-S5 §2.1, §3.1.2, PDF pp. 6, 9] |
| LP-S40 | Gill, Murray, Saunders, Wright (1984). Sparse Matrix Methods in Optimization. SIAM Journal on Scientific and Statistical Computing 5(3):562–589 | DOI 10.1137/0905041（Crossref） | partitioned LU 更新（据称提出但未实现）：MPF 相对 PF 的类比对象 [LP-S1 §2.5.2, PDF p. 42; LP-S5 §1, PDF pp. 2, 9] |
| LP-S41 | Hall (1991). Sparse matrix algebra for active set methods in linear programming. PhD thesis, University of Dundee | Hall 出版物页 https://webhomes.maths.ed.ac.uk/hall/Publications.html（2026-10-27）；无 DOI | alternative block LU 更新（Hall 提出并实现）：APF 相对 PF 的类比对象 [LP-S1 §2.5.1, PDF p. 40; LP-S5 PDF p. 8] |
| LP-S42 | Eldersveld, Saunders (1992). A Block-LU Update for Large-Scale Linear Programming. SIAM Journal on Matrix Analysis and Applications 13(1):191–201 | DOI 10.1137/0613016（Crossref；EUROPT17 幻灯片给该工作标了另一个年份，来源未解释） | block LU（BLU）更新：定位 APF、MPF 的参照，二者都免去 Schur complement [LP-S1 §2.5.1–§2.5.2, PDF pp. 41–42; LP-S5 PDF pp. 8–9; LP-S15 PDF p. 11] |
| LP-S43 | Suhl, Suhl (1993). A fast LU update for linear programming. Annals of Operations Research 43(1):33–47 | DOI 10.1007/BF02025534（Crossref + Springer；记录作者顺序 Leena M. Suhl 在先，[LP-S5] 印 U. H. Suhl 在先） | Suhl 的 FT 类更新：作者称其效率受一次 FT 所不需要的 BTRAN 拖累；列为不做数值主元的代码之一 [LP-S5 §1, §2.1, PDF pp. 2, 4, 6, 9] |

### verified-web · 超稀疏性

| ID | 文献 | 定位/核实 | 角色（cited-by-source） |
|----|------|-----------|------|
| LP-S44 | Gilbert, Peierls (1988). Sparse Partial Pivoting in Time Proportional to Arithmetic Operations. SIAM Journal on Scientific and Statistical Computing 9(5):862–874 | DOI 10.1137/0909058（Crossref） | 两阶段 DFS 超稀疏三角求解；论文称原文只简略提及，并为置换因子补全了细节 [LP-S1 §2.3.3, PDF p. 32]；超稀疏求解技术 [LP-S5 §3.3, PDF p. 13]；hsol 超稀疏求解的署名之一 [LP-S14 PDF p. 7] |
| LP-S45 | Hall, McKinnon (2005). Hyper-Sparsity in the Revised Simplex Method and How to Exploit it. Computational Optimization and Applications 32(3):259–283 | DOI 10.1007/s10589-005-4802-0（Crossref + Hall 出版物页） | 超稀疏性的识别与 10%/60% 判据、超稀疏 FTRAN/BTRAN、原始超稀疏 CHUZC（被改作对偶 CHUZR）、利于 APF 的 LP 类 [LP-S1 §1.3, §2.3.3, §3.2.2, PDF pp. 19, 31–32, 55; LP-S2 §2.2, §5.1, PDF pp. 5, 16; LP-S5 PDF pp. 3, 8, 13; LP-S7 §1, PDF pp. 1–2]；幻灯片在其署名旁印 "COAP best paper prize (2005)" [LP-S14 PDF p. 7] |

### verified-web · suboptimization 与 multiple pricing

| ID | 文献 | 定位/核实 | 角色（cited-by-source） |
|----|------|-----------|------|
| LP-S46 | Orchard-Hays (1968). Advanced linear-programming computing techniques. McGraw-Hill, New York | 美国国会图书馆目录记录（2026-10-27）；无 DOI | 原始单纯形的 multiple pricing（后被 Rosander 移入对偶）[LP-S1 §4.3.1, PDF p. 80; LP-S6 §2.1, PDF p. 3]；[LP-S2 §2.4, PDF p. 8] 把 PF 更新也引到此书 |
| LP-S47 | Rosander (1975). Multiple pricing and suboptimization in dual linear programming algorithms. In Balinski, Hellerman (eds), Computational Practice in Mathematical Programming, Mathematical Programming Studies 4:108–117 | DOI 10.1007/BFb0120714（Crossref + Springer） | 对偶 suboptimization 的最早提出者 [LP-S1 §4.3.1, PDF p. 80; LP-S5 §3, PDF p. 6]；[LP-S2 §2.3, PDF p. 7] 称未见实用实现的报告，PAMI 是对其方案的扩展 [LP-S2 §3, PDF p. 9] |

### verified-web · 更早的并行单纯形工作

| ID | 文献 | 定位/核实 | 角色（cited-by-source） |
|----|------|-----------|------|
| LP-S48 | Hall, McKinnon (1992). Update procedures for the parallel revised simplex method. Technical report MSR 92-13 | Hall 出版物页（2026-10-27）；无 DOI；论文印发行单位 University of Edinburgh，核实页面未显示 | 重叠 INVERT 时复用 PF 更新导致数值不稳——PAMI 不重叠 INVERT 的理由 [LP-S1 §4.1.2, §4.3.4, ch. 5, PDF pp. 73, 85, 95] |
| LP-S49 | Hall, McKinnon (1996). PARSMI, a parallel revised simplex algorithm incorporating minor iterations and Devex pricing. In Applied Parallel Computing (PARA '96), LNCS 1184, pp. 359–368 | DOI 10.1007/3-540-62095-8_38（Crossref + Springer + Hall 出版物页；各一手来源印 pp. 67–76，以记录为准） | 带 minor iterations 与 Devex 的并行原始修正单纯形；与 Wunderling 并列为 PAMI 的最近亲 [LP-S1 §4.1.2, §4.3.1, PDF pp. 72, 74, 80]；建立在 suboptimization 上 [LP-S2 §2.3, PDF p. 8] |
| LP-S50 | Wunderling (1996). Paralleler und Objektorientierter Simplex-Algorithmus. Doctoral thesis, ZIB-Report TR-96-09（德文） | ZIB OPUS docId 538（2026-10-27） | major/minor 结构的并行原始单纯形 [LP-S1 §4.1.2, PDF pp. 72–74]；也试验过原始 suboptimization（仅 MPC 版有此句）[LP-S4 §2.3, PDF p. 9] |
| LP-S51 | Hall, McKinnon (1998). ASYNPLEX, an asynchronous parallel revised simplex algorithm. Annals of Operations Research 81:27–49 或 27–50 | DOI 10.1023/A:1018957107705（Crossref/Springer 作 27–50，zbMATH 与 Hall 出版物页作 27–49——**末页需核对**；一手来源题名多印一个 "method"，记录无） | 异步并行修正单纯形；论文称其为 PARSMI 的 "preliminary version" [LP-S1 §4.1.2, PDF pp. 72, 74]；建立在 suboptimization 上 [LP-S2 §2.3, PDF p. 8] |
| LP-S52 | Bixby, Martin (2000). Parallelizing the Dual Simplex Method. INFORMS Journal on Computing 12(1):45–56 | DOI 10.1287/ijoc.12.1.45.11902（Crossref） | 此前唯一发表的对偶单纯形并行化：无 BFRT、无超稀疏求解；只数据并行 PRICE（与 UPDATE-DUAL）；考虑过 FTRAN 与 FTRAN-DSE 的任务并行但因计算上不利而放弃 [LP-S1 §4.1.2, PDF pp. 74–75; LP-S2 §1, §2.2.4, §4, PDF pp. 2, 6, 15; LP-S6 §2.2, PDF p. 4] |
| LP-S53 | Hall (2010). Towards a practical parallelisation of the simplex method. Computational Management Science 7(2):139–170 | DOI 10.1007/s10287-008-0080-5（Crossref + Hall 出版物页；网络首发 2008） | 并行单纯形综述：论文据其挑选并评价前人工作 [LP-S1 ch. 4, §4.1.2, PDF pp. 70, 73–74]；据其称尚无并行代码在一般稀疏 LP 上明显胜过好的串行求解器 [LP-S6 §2.2, PDF pp. 3–4] |
| LP-S54 | Lubin, Hall, Petra, Anitescu (2013). Parallel distributed-memory simplex for large-scale stochastic LP problems. Computational Optimization and Applications 55(3):571–596 | DOI 10.1007/s10589-013-9542-y（Crossref + Hall 出版物页） | 块角随机 LP 的并行对偶修正单纯形 [LP-S1 §4.1.3, PDF p. 76]；HPC 单纯形进展之一 [LP-S5 §1, PDF p. 1]；幻灯片署 "Lubin, H et al."，非 Huangfu [LP-S13 PDF pp. 23–25] |

### verified-web · 对照求解器与测试集来源

| ID | 文献 | 定位/核实 | 角色（cited-by-source） |
|----|------|-----------|------|
| LP-S55 | COIN-OR Clp（The COIN-OR Linear Programming Solver） | https://github.com/coin-or/Clp（2026-10-27：release 1.14.x/1.15.x/1.16.x 标签存在；一手来源所引 coin-or.org 页面已 404；2013–2016 年的网页状态未核） | 公开源码对照：版本随来源变——1.06 [LP-S6 §4, PDF p. 7]、1.14 [LP-S1 §1.3, PDF p. 19]、1.15 [LP-S2 §5.2, PDF p. 21; LP-S5 §4, PDF p. 13]、v1.16 [LP-S13 PDF p. 37; LP-S14 PDF p. 9]；幻灯片称由 John Forrest (IBM) 编写、Hall 现为项目经理 [LP-S12 PDF p. 34] |
| LP-S56 | IBM ILOG CPLEX Optimizer | 一手来源所引 URL 现重定向到 IBM CPLEX 产品页（2026-10-27）；所用版本无法在现页核实 | 商业对照：Cplex 12.4 [LP-S1 §1.3, PDF p. 19; LP-S2 §5.4, PDF p. 23; LP-S5 §4, PDF p. 13]、v12.5 [LP-S13 PDF p. 37; LP-S14 PDF p. 9] |
| LP-S57 | Mittelmann. Benchmarks for Optimization Software | https://plato.asu.edu/bench.html（一手来源所引 plato.la.asu.edu 现重定向；现页称自 2018 年起移除了若干商业求解器的结果；2013–2016 年访问时的页面未核） | 30 题参考集的多数题目来源 [LP-S1 §1.3, PDF p. 18; LP-S2 §5.1, PDF p. 15]；[LP-S2 §5.4, PDF p. 23] 称并行 Xpress 的竞争力亦见于其独立基准（未给数字，无法对现页核对） |

### verified-web · 与一手来源相关的记录

| ID | 文献 | 定位/核实 | 角色（cited-by-source） |
|----|------|-----------|------|
| LP-S58 | Huangfu (2014). The Algorithm that Runs the World. FICO Blog, Analytics & Optimization（13 May 2014） | 官方 URL 现对 curl/WebFetch 返回 bot 检查；经 Internet Archive 快照 20150127063109 核实其存在（2026-10-27）；**正文未读** | Huangfu 在 FICO Xpress 中实现这些技术的引用出处 [LP-S4 §5.4, PDF p. 24; LP-S3 §5.4, PDF p. 24]；幻灯片记作 "(Huangfu 2014)" [LP-S14 PDF p. 12]；[LP-S2] 未引 |
| LP-S59 | COAP 2015 Best Paper Prize (2016). Computational Optimization and Applications 65(3):541–544（无作者） | DOI 10.1007/s10589-016-9882-5（Crossref + Springer；2026-10-27）；txt stem `COAP-2015-best-paper`（不在 manifest 内），**只读首页** | 宣布 2015 年 COAP 最佳论文奖授予 Huangfu（印作 "of the FICO Xpress Team"）与 Hall 的 "Novel update techniques for the revised simplex method"（即 [LP-S5] 的期刊版）[LP-S59 PDF p. 1]；这就是 manifest 所说 HuHa12 页面链接的第二个 DOI；一手来源均未提及此 DOI |

## 具名研究者档案

| 研究者 | 档案 | 核实基础 |
|--------|------|---------|
| Qi Huangfu | `researchers/qi-huangfu.md` | [LP-S1–S20] 的署名、致谢、作者句与讲者简介（2026-10-27）；无个人主页或简历入库 |
