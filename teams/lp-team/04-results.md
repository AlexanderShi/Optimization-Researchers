# LP Team · 关键结果速查

格式：结论（数字照印，不取整、不换算）| 假设（测试集、硬件、线程、基线、版本——观察或证明成立的条件）|
状态（proved-in-source / verified-web 计算结果 / cited）| 层级。蒸馏出的 skill 引用结果必须整条带出条件，
不得只摘一个加速比。语料**没有**任何收敛速率、迭代复杂度或反循环定理：被证明的只有代数恒等式与成本模型推导。
「均值」一律照来源写法；来源没说是哪种均值的，就写「均值类型未说明」。

## LP-R1 对偶修正单纯形的组件耗时剖面
- **结论**：30 题参考集上，各组件占总求解时间的平均百分比为 FTRAN-DSE 26.4、PRICE 18.4、INVERT 13.3、
  FTRAN 10.8、BTRAN 8.7、CHUZC1 7.3、UPDATE 4.8、FTRAN-BFRT 3.5、CHUZR 2.9、OTHER 2.3、CHUZC2 1.5
  [LP-S1 Table 4.3, PDF p. 78]；期刊版对 hsol 印同一组均值（其表 1 把 2.3 记作 update-factor）[LP-S2 Table 1, PDF p. 7; Table 4, PDF p. 18]。
  个别问题极度偏斜：FTRAN-DSE 在 sgpf5y6 占 80.7、stormG2-1000 占 70.6；PRICE 在 stat96v4 占 67.6、truss 占 53.8；
  INVERT 在 watson_2 占 34.5、self 占 33.9、maros-r7 占 27.4 [LP-S1 Table 4.3, PDF p. 78]。
- **假设**：30 题参考集（多数取自 Mittelmann 列表 [LP-S57]，据 [LP-S1 §1.3, PDF p. 18]）；论文只称剖面对象为
  "an advanced dual revised simplex method implementation"，期刊版称 hsol；迭代时间列（平均 867）的单位冲突：表题印 "(ms)"，正文写
  microseconds [LP-S1 §4.2.1, PDF pp. 76, 78; LP-S2 Table 4, PDF p. 18]；Average 行的均值类型未说明；硬件见 LP-R3、LP-R4。
- **状态**：verified-web: computational result reported in [LP-S1] (Table 4.3, §4.2.1, PDF pp. 76–78) and [LP-S2] (Table 1, PDF p. 7; Table 4, PDF p. 18)
- **层级**：verified-web；迭代时间单位需核对。

## LP-R2 Amdahl 上界与「8 核」目标
- **结论**：speedup = 1/(p_SEQ + (1 − p_SEQ)/N)。p_SEQ = 50% 时无论多少核加速至多为 2；Bixby–Martin 式只并行化常规可并行组件
  （CHUZC、CHUZR、PRICE、UPDATE，平均不足 35%）的方案，最好也只有约 1.5；假设串行部分 30%、其余完美并行，
  8、16、32、64 核的最佳加速为 2.6、2.9、3.1、3.2，因此论文假定 8 核 [LP-S1 §4.2.1–§4.2.2, PDF pp. 76–79]。
- **假设**：Amdahl 定律在论文中未注出处；30% 是明说的假设而非测量；组件份额来自 LP-R1；对 Bixby–Martin 的界是论文用自己的剖面
  推出的，不是 [LP-S52] 原文的结论。
- **状态**：proved-in-source [LP-S1]（Amdahl 定律的算术推论，§4.2.1–§4.2.2, PDF pp. 76–79）
- **层级**：verified-web。

## LP-R3 PAMI：论文版结果（8 核）
- **结论**：表 4.5 的 Geomean 行：SEQ 50.8、PAMI1 76.0、PAMI8 34.1；p1/seq 0.67、p8/p1 2.23、p8/seq 1.49；最好的 p8/seq 为 2.53
  （qap12）；maros-r7（0.47）与 Linf_520c（0.75）变慢，self 仅 1.07 [LP-S1 Table 4.5, PDF p. 88]。作者解读：串行 PAMI 约慢 30%；
  高于平均的加速多出现在相对稠密的 LP（部分因迭代更少，如 dfl001 迭代 26322 → 23668）；最差的也是稠密 LP，作者归因于其在
  表 4.3 中最大的 INVERT 份额；超稀疏 LP 加速温和而稳定 [LP-S1 §4.3.6, PDF pp. 87–89]。作者自评：
  "Though the speedup is not extremely impressive, the overall performance of PAMI is comparable to the dual simplex implementation of Cplex" [LP-S1 §4.5, PDF p. 93]。
- **假设**：30 题参考集；SEQ = HSOL，PAMI1 = 串行 PAMI，PAMI8 = 8 核；候选数 s = 8 且核数等于 s；ψ = 0.95；机器 compute64b，
  16 核 Intel Xeon E5620 2.4GHz，Intel C++ Compiler 13.0 + OpenMP 3.1 [LP-S1 §1.2, PDF p. 18]；时间单位未印；Geomean。
  章首写平均加速 1.5、表与第 5 章写 1.49 [LP-S1 ch. 4, PDF p. 70; ch. 5, PDF p. 95]。
- **状态**：verified-web: computational result reported in [LP-S1] (Table 4.5, §4.3.6, PDF pp. 86–89)
- **层级**：verified-web。

## LP-R4 PAMI：期刊版结果（8 核）
- **结论**：表 6 的 Mean 行（几何均值）：p1/hsol 0.64、p8/p1 2.34、p8/hsol 1.51；超过 65% 的问题在并行下比串行 PAMI 快一倍；最好的
  qap12（2.58）与 stp3d（2.33）得益于迭代更少，按相对迭代数缩放后仍为 1.74 与 1.75；在 maros-r7（0.49）与 Linf 520c（0.93）上
  pami8 慢于 hsol，此二者串行 pami 分别慢 3.48 与 2.75 倍，且 INVERT 份额大 [LP-S2 Table 6, PDF p. 20; §5.2, PDF p. 22]。
  "Interestingly, there is no real relation between the performance of pami and problem hyper-sparsity" [LP-S2 §5.2, PDF p. 22]。
  pami 相对 hsol 的迭代数均值 0.96，作者据此称有候选质量控制时 suboptimization 不损迭代数；pami 串行与并行走同一基序列
  [LP-S2 §5.2, PDF p. 21]。
- **假设**：同一 30 题参考集（表 3 与论文表 1.1 同）；hsol 为基线；无预处理、无 crash；硬件三版不同：ERGO 版硬件句断裂，
  arXiv 版为 16 个 Intel Xeon E5620 2.4GHz 处理器、用 8 个 [LP-S3 §5.1, PDF p. 17]，MPC 版为两颗 Intel Xeon E5-2670 2.6 GHz
  （16 核 16 线程）、用 8 线程 [LP-S4 §5.1, PDF p. 17]；三版表格数字相同，MPC 表号重排；时间单位未印。
  与论文版（LP-R3）不是同一次运行（例：cre-b 串行时间论文 6.2、期刊 4.62），语料未解释差异。
- **状态**：verified-web: computational result reported in [LP-S2] (Tables 5–6, §5.2, PDF pp. 19–22); same numbers in [LP-S3] and [LP-S4]
- **层级**：verified-web；硬件归属需核对（版本间不一致，来源未解释）。

## LP-R5 SIP：论文版结果（8 处理器）
- **结论**：表 4.7 Geomean：SEQ 50.8、SIP 44.8、PAMI 34.1；加速 SIP 1.13、PAMI 1.49。SIP 在 PAMI 失速处胜出：Linf_520c 1.31（PAMI
  0.75）、maros-r7 1.12（0.47）、self 1.36（1.07）。SIP 在多数超稀疏 LP 上变慢：sgpf5y6 0.67、stormG2-125 0.76、watson_2 0.78、
  ken-18 0.79、watson_1 0.80、stormG2-1000 0.84；稠密的 qap12 也慢（0.83）[LP-S1 Table 4.7, PDF p. 92]。作者结论：
  "SIP is frequently complementary to PAMI in achieving speedup when PAMI results in slowdown." [LP-S1 §4.4.2, PDF p. 92]。单次迭代 Gantt 图：dfl001
  第 10000 次迭代 SIP 图注 "754 ms"、HSOL 图注 "1144 ms"；SIP 下每个 FTRAN（尤其 FTRAN-DSE）都比 HSOL 慢，作者归因于内存访问竞争
  [LP-S1 §4.4.3, PDF pp. 92–93]。
- **假设**：同 LP-R3 的测试集与机器；SIP 用一个处理器做 FTRAN-DSE，结构部分矩阵分成 s − 2 份 [LP-S1 §4.4.1, PDF pp. 90–91]；
  Gantt 图注的 "ms" 与正文 microseconds 冲突（见 LP-R1）。
- **状态**：verified-web: computational result reported in [LP-S1] (Table 4.7, §4.4.2–§4.4.3, PDF pp. 91–93)
- **层级**：verified-web。

## LP-R6 SIP：期刊版结果
- **结论**：sip/hsol 均值 1.15，劣于 pami；最差的是超稀疏 LP，如 sgpf5y6（0.64，其 FTRAN-DSE 超过 80%）；稠密 LP 上温和稳定。
  正文称 sip 在 Linf 520c 与 maros-r7 上 "achieves speedups of 1.31 and 1.12"，而表 6 印 1.37 与 1.22（三版皆然；表 5 的时间与表
  一致，读者核对）[LP-S2 §5.3, PDF pp. 22–23; Table 6, PDF p. 20]。正文这两个数恰与论文表 4.7 相同（LP-R5），语料未解释。sip 迭代数相对 hsol
  在 [0.98, 1.06] 之间，仅 nug12（1.09）与 qap12（1.60）例外——二者高度退化、只差行列置换 [LP-S2 §5.3, PDF p. 22]。
- **假设**：同 LP-R4；sip 至少需要 4 个处理器，多于 4 只增加 spmv 与 chuzc 的并行 [LP-S2 §4, PDF p. 15]。
- **状态**：verified-web: computational result reported in [LP-S2] (Table 6, §5.3, PDF pp. 20, 22–23)
- **层级**：verified-web；Linf 520c 与 maros-r7 的正文值与表值不一致，需核对。

## LP-R7 PAMI 候选质量截断 ψ 的实验
- **结论**：平均加速随 ψ：1.001 → 1.12；0.999 → 1.52；0.99 → 1.54；0.95 → 1.49；0.94 → 1.56（全表最高）；0.9 → 1.50；
  0.5 → 1.42；0.05 → 1.16；0.01 → 1.22。0.9 ≤ ψ ≤ 0.999 之间无实质差别，低于 0.9 均值明显下降；取该区间的中位数 ψ = 0.95，
  它**不是**表中最好的一行 [LP-S1 Table 4.4, §4.3.5, PDF pp. 86–87; LP-S2 Table 2, §3.3, PDF pp. 13–14]。用 0.999 而非 1.0 是给数值噪声
  留容差 [LP-S1 §4.3.5, PDF p. 86]。
- **假设**：30 题参考集；规则为 α_p < ψ α_p^i 时剔除候选（α 为 DSE 吸引力，α_p^i 为 major CHUZR 时的值）；期刊版称指标为
  "(geometric) mean speedup"，但两版都没说是哪个比值（ψ = 0.95 行的 1.49 与期刊表 6 的 p8/hsol 1.51 不同，来源未解释）。
- **状态**：verified-web: computational result reported in [LP-S1] (Table 4.4, PDF p. 87) and [LP-S2] (Table 2, PDF p. 14)
- **层级**：verified-web。

## LP-R8 与 Cplex 的比较
- **结论**：论文：PAMI 的整体表现与 Cplex 的对偶单纯形 "comparable"，依据是 PAMI、Clp、Cplex 的 elapsed-time performance profile
  （图 4.7，文字层无数据）[LP-S1 §4.3.6, PDF pp. 88–89]。期刊：在不开预处理与 crash 的 Cplex 12.4 面前，
  "the performance of the better of sip and pami is comparable with that of Cplex for the majority of the test problems"，
  作者同时承认拿商业求解器比研究代码 "perhaps, unreasonable" [LP-S2 §5.4, PDF p. 23; Fig. 4, PDF p. 24]。
- **假设**：论文图 4.7 的 Cplex/Clp 版本、设置与线程数在该页未说明（论文另处给出的对照版本为 Cplex 12.4 与 Clp 1.14 [LP-S1 §1.3, PDF p. 19]）；
  期刊图 4 为 Cplex 12.4 [LP-S56]、pami8、sip8 与 min(pami8, sip8) 的 performance profile；只有比较，没有「胜过」的说法。
- **状态**：verified-web: computational result reported in [LP-S1] (Fig. 4.7, PDF pp. 88–89) and [LP-S2] (Fig. 4, §5.4, PDF pp. 23–24)
- **层级**：verified-web（图形结果，无可读数值）。

## LP-R9 PAMI 思想进入 FICO Xpress
- **结论**：期刊图 5 为 Cplex、Xpress、Xpress8 的 performance profile（开预处理与 crash）；正文称在并行有帮助的问题上，并行 Xpress 让
  FICO 求解器达到 "Cplex (which has no parallel simplex facility)" 的串行水平 [LP-S2 §5.4, PDF p. 23; Fig. 5, PDF p. 24]；结论称
  "Huangfu has raised the performance of the Xpress parallel revised simplex solver to that of the worlds best commercial simplex solvers"
  [LP-S2 §6, PDF p. 25]；并称 Mittelmann 的独立基准亦反映此点（无数字）[LP-S2 §5.4, PDF p. 23]。2016–2017 幻灯片印
  "pami ideas incorporated in FICO Xpress (Huangfu 2014)" 与 "Xpress simplex solver now fastest commercial simplex solver"，配 cplex /
  xpress / xpress (8 cores) 的 profile（横轴 1–2）[LP-S14 PDF p. 12; LP-S15 PDF p. 21; LP-S13 PDF p. 34]。
- **假设**：Xpress 版本、图 5 的 Cplex 版本、测试集、硬件、谁跑的实验——全部未说明；幻灯片图中只有 cplex 一个对手。
- **状态**：verified-web: computational result reported in [LP-S2] (Fig. 5, §5.4, PDF pp. 23–24) and [LP-S14] (PDF p. 12)
- **层级**：需核对（实验条件未记录、不可复现）；"fastest" 是 2016–2017 年的快照说法。

## LP-R10 hsol 相对 Clp 的串行质量（期刊版）
- **结论**：按表 6 的平均相对求解时间，8 核 pami 比 hsol 快 1.51 倍，hsol 比 Clp 快 2.29 倍；hsol 所需迭代数为 Clp 的 0.70
  （极端值 ns1688926 为 0.07、dbic1 为 0.11），折算后 hsol 的迭代速度是 Clp 的 1.60 倍；作者结论 hsol 是高质量的对偶修正单纯形
  求解器；图 3 的 profile 中 pami8 优于 hsol，hsol "generally superior" 于 Clp [LP-S2 §5.2, PDF pp. 21–22]。
- **假设**：Clp 1.15 [LP-S55]，无预处理、无 crash；30 题参考集；硬件同 LP-R4；正文说 2.29 依据表 6，但表 6 无 Clp 列（与表 5 的
  时间相符，读者核对），照原文记录。
- **状态**：verified-web: computational result reported in [LP-S2] (§5.2, Fig. 3, PDF pp. 21–22)
- **层级**：verified-web。

## LP-R11 hsol 与 clp、cplex：更新论文中的串行对照，及论文图 3.6
- **结论**：ERGO-13-001 表 2（求解时间 s / 迭代数 / 每迭代 µs）用来说明做更新实验的 hsol 有代表性：
  "hsol is competitive with cplex and clp, both overall and per iteration" [LP-S5 §4, PDF p. 13]。逐题差异很大，例如 CRE-B：hsol 6.4、clp 4.2、cplex 2.1；
  SGPF5Y6：180.2、242.1、7.9；NS1688926：25.0、4424.7、52.8；LINF 520C：3646.8、3349.1、8242.8 [LP-S5 Table 2, PDF p. 15]。
  论文第 3 章：HSOL 与 Clp 的对偶单纯形 "comparable"，依据为图 3.6 的 timing profile（文字层无数据）[LP-S1 §3.4, PDF pp. 68–69]。
- **假设**：ERGO-13-001 的 30 题取自 Netlib、Kennington 与其它公开集，"not particularly large"，与论文/期刊的参考集**不同**
  （含 GEN4、OSA-60、PDS-20、STAT96V1，不含 dbic1、fome13、nug12、pds-80）[LP-S5 Table 1, PDF p. 14]；clp 1.15、cplex 12.4 的对偶
  单纯形；硬件与线程未说明；表 2 列序为 hsol、clp、cplex，与表题所列顺序不同。论文图 3.6 的测试集、版本、硬件在该页未说明。
- **状态**：verified-web: computational result reported in [LP-S5] (Table 2, §4, PDF pp. 13, 15) and [LP-S1] (Fig. 3.6, §3.4, PDF pp. 68–69)
- **层级**：verified-web。

## LP-R12 基更新方法比较：论文版（表 2.4）
- **结论**：在 PF、APF、MPF 三种乘积形式中，MPF 在 30 题中的 26 题最好，APF 在 3 题最好（这 3 题稀疏 BTRAN 结果的比例都不低于
  FTRAN 的），APF 在 15 题最差（正文所印），其余题 PF 最差；以与 PF、APF 较好者之比的几何均值计，MPF 高效 42%；FT 在 27 题
  胜过最好的乘积形式，"in average" 比 PF/APF 较好者高效 63%、只比 MPF 高效 35%；CFT 与 FT 在多数题上很接近（差异双向，如
  watson 2：FT 4.9 vs CFT 6.5；stp3d：FT 124.5 vs CFT 101.9）[LP-S1 §2.5.4, Table 2.4, PDF pp. 45–46]。FT 的计算优势大于其存储
  优势，因为 "hyper-sparsity may be exploited fully when using the FT update"，APF、MPF 只在作用 B_0^{-1} 时能利用超稀疏
  [LP-S1 §2.5.4, PDF p. 46]。
- **假设**：论文 30 题参考集；所有方法走同一条从 B = I 到最优的基变化序列；都用为 FT 定出的重新求逆间隔（FT 不吃亏）；
  指标是每个基做 update + FTRAN + BTRAN 的总 CPU 时间，单位未印；串行效率测试，未给线程数；机器同 LP-R3。
- **状态**：verified-web: computational result reported in [LP-S1] (Table 2.4, §2.5.4, PDF pp. 45–46)
- **层级**：verified-web；「APF 最差 15 题」与读者按印刷表所作的计数不符，需核对；63% 未说明均值类型。

## LP-R13 基更新方法比较：ERGO-13-001 版（表 1–3）
- **结论**：正文："it is the best for 26 of the 30 problems"（MPF 在乘积形式中），APF 在其余 4 题中的 3 题最好，APF 在 16 题最差；
  MPF 比 PF/APF 较好者高效 40%（几何均值）；FT 在 27 题胜过最好的乘积形式，比 PF/APF 较好者高效 61%、比 MPF 高效 34%；CFT 与 FT
  很接近，"the former being 4% faster" [LP-S5 §4, PDF pp. 16–17]。但表 1 的粗体（最好者）落在 APF 4 题（GEN4、maros-r7、NS1688926、
  STORMG2-1000）、PF 1 题（SELF）、MPF 25 题 [LP-S5 Table 1, PDF p. 14]。存储：MPF 比 PF/APF 较好者省 31%，FT 比 MPF 省 16%、比
  PF/APF 较好者省 42%，FT 与 CFT 平均填充无显著差别 [LP-S5 §4, PDF p. 17]。表 3：部分结果 ã_q、ẽ_p 远比 â_q、ê_p 稀疏（如 PDS-100：
  PF â_q 0.071、APF ê_p 0.387、MPF ã_q 0.036 与 ẽ_p 0.002、FT ã_q 0.016 与 ẽ_p 0.003，单位未印），作者据此说同时存两个部分结果远比存
  一个完整结果高效，直观解释是部分结果解的是三角而非方阵系统 [LP-S5 Table 3, §4, PDF pp. 17–18]。
- **假设**：30 题取自 Netlib、Kennington 与其它公开集（与论文参考集不同，见 LP-R11）；用 hsol 的模块；同一基变化序列、共用 FT
  最优重新求逆间隔（各自最优间隔也算过，结论不变，故略）；指标同 LP-R12；硬件未说明；「高效 X%」这类百分比如何对应时间比未说明，
  只有 40% 明说是几何均值。
- **状态**：verified-web: computational result reported in [LP-S5] (Tables 1 and 3, §4, PDF pp. 13–18)
- **层级**：verified-web；「26 of 30」与表 1 粗体（25）不一致，需核对。

## LP-R14 更新方法的归一化几何均值（EUROPT17）
- **结论**：幻灯片原文 "Update PFI FT APF MPF CFT Mean 1.00 0.30 0.95 0.45 0.29"——生成与使用更新数据的运算时间的几何均值，归一到
  PFI = 1.00；幻灯片结论：FT 远好于 PFI、"APF little better than PFI"、MPF 比 PFI 更接近 FT、CFT 与 FT 一样好 [LP-S15 PDF p. 16]。
- **假设**："30 representative LP problems from standard test sets"，所有更新走同一基变化序列 [LP-S15 PDF p. 16]；版本、硬件、是否
  与 ERGO-13-001 表 1 为同一次运行，均未说明；基线（PFI）与 LP-R12、LP-R13 的基线（PF/APF 较好者或 MPF）不同，**不可互换**。
- **状态**：verified-web: computational result reported in [LP-S15] (PDF p. 16)
- **层级**：verified-web。

## LP-R15 APF、MPF、CFT 的代数
- **结论**：秩一初等阵 T = I + u v^T，非奇异时 T^{-1} = I − (1/µ) u v^T，µ = 1 + v^T u（来源直接给出，未推导、未注出处）。
  APF：B̄ = (I + (a_q − a_{p'}) ê_p^T) B，B̄^{-1} = B^{-1}(I − (1/µ)(a_q − a_{p'}) ê_p^T)，µ = â_pq，用的是完整 BTRAN 结果 ê_p 与 A 的两列；
  MPF：B̄ = L (I + (ã_q − u_p) ẽ_p^T) U，µ = â_pq，用的是与 FT 相同的两个部分结果；CFT：suboptimization 之后只拿得到以 B_k 计算的
  部分结果，缺的部分 BTRAN 结果可逐步校正，每步一次内积加一次向量加法，部分 FTRAN 结果则补乘新的行 eta [LP-S5 §3.1–§3.2, PDF pp. 6–12;
  LP-S1 §2.5.1–§2.5.3, PDF pp. 39–45]。
- **假设**：B = LU（为方便忽略置换）；CFT 只分析 p_1 ≠ p_0 的情形（suboptimization 中 P 的每行只用一次），p_1 = p_0 时 µ = 0、只差一个
  缩放，被略去 [LP-S5 §3.2.2, PDF pp. 11–12]。
- **状态**：proved-in-source [LP-S5]（代数推导，§3.1–§3.2, PDF pp. 6–12）；同样的推导见 [LP-S1 §2.5, PDF pp. 39–45]
- **层级**：verified-web；来源没有任何误差界或稳定性证明。

## LP-R16 重新求逆（reinversion）准则
- **结论**：当自上次 INVERT 以来更新部分累计的时间 t_U^+ 等于上次 INVERT 的时间 t_I 时重新求逆；由「总的 INVERT + 更新时间最小」
  的成本模型推出；实现中两者都按操作数计 [LP-S1 §2.4.4, PDF p. 39]；hsol 用基于 flop 的伪时钟使性能可复现，
  "practical experience shows that performance is not sensitive to the parameters in the model" [LP-S5 §4, PDF p. 15]；PAMI 中并行求解压低了更新部分的
  时间，阈值放大为 t_U^+ = 1.5 × t_I [LP-S1 §4.3.4, PDF p. 85]。
- **假设**：成本模型假设每个更新 eta 平均时间恒定、每次 INVERT 时间恒定、其它运算不受间隔影响（正文说「两个假设」却列了三条）；
  该页公式在文字层损坏；最优间隔本身无法确定，总时间对间隔不敏感是经验陈述（无数据）[LP-S1 §2.4.4, PDF p. 39]。
- **状态**：proved-in-source [LP-S1]（成本模型推导，§2.4.4, PDF p. 39）
- **层级**：verified-web；公式文本需对照 PDF 核对。

## LP-R17 成本扰动在 pds-20 上的效果（HSOL）
- **结论**：不扰动 49913 次迭代、46.2 s；扰动后 38517 次、7.6 s——迭代减 23%、时间减 84%、迭代速度快 4.7 倍 [LP-S1 §3.3.1, PDF p. 61]。
  超稀疏结果比例（关 → 开）：btran 76.1% → 98.4%、price 77.5% → 99.3%、ftran-dse 72.1% → 95.1%、ftran（t = 2%）78.6% → 98.1%
  [LP-S1 Table 3.5, PDF p. 61]；有实际翻界的迭代数：扰动 10672、不扰动 2286 [LP-S1 §3.3.2, PDF p. 62]。作者的解释链：扰动让 BFRT
  有效 → 成功的 BFRT 降低稠密行的不可行量与 DSE 吸引力 → 稠密行在 CHUZR 中更少、更晚被选 [LP-S1 §3.3.2, PDF pp. 62–64]。
- **假设**：单一问题 pds-20（不在 30 题参考集内）；第 3 章未重述硬件；表 3.5 只有 FTRAN 列标明 t = 2%，其余三列阈值有歧义；解释链
  是基于 pds-20 观测的诠释（"computational experiences suggests"），不是定理 [LP-S1 §3.3.2, PDF p. 64]。
- **状态**：verified-web: computational result reported in [LP-S1] (§3.3.1–§3.3.2, Table 3.5, PDF pp. 61–64)
- **层级**：verified-web。

## LP-R18 LiDSE 与广义 LiDSE（pds 族）
- **结论**：LiDSE 用 |Δx_i|/w_i 代替 DSE 的 Δx_i²/w_i [LP-S1 §3.3.4, PDF p. 66]。pds-20（表 3.8）：不扰动时 LiDSE 把时间从 46.2 降到
  17.6，扰动下从 7.6 降到 4.0（作者称减 47%）[LP-S1 Table 3.8, PDF p. 67]。pds-30…pds-100（表 3.9，Geomean）：Cplex 28.7、Perturb 47.9、
  LiDSE（含扰动）30.9、Perturbation and Partial 59.7、LiDSE+Partial 35.2，作者称 "HSOL is 6% slower in average"；迭代数上 LiDSE 需要
  "about 60% more iterations" 于 Cplex（表 3.10 Geomean 147707 vs 92222），竞争力来自迭代速度 [LP-S1 §3.3.5, Tables 3.9–3.10, PDF pp. 67–68]。
  广义形式 |Δx_i|^t/w_i（表 3.11 Geomean）：t = 1 为 30.9、1.2 为 24.6、1.5 为 34.8、2 为 47.9；t = 1.2 的版本
  "solves each problem faster than Cplex" [LP-S1 Table 3.11, PDF p. 68]。partial CHUZR 对较大 pds 不合适、还拖慢 LiDSE [LP-S1 §3.3.5, PDF p. 67]。
- **假设**：只在 pds 族上测；LiDSE 的依据是 pds 的表元多为 ±1、DSE 权重近似 e_i 的 1-范数；对表元大小差异大的一般 LP 可能严重损害效率，
  作者自评 "its scope for further application is fairly limited" [LP-S1 §3.3.4–§3.3.5, PDF pp. 67–68]；Cplex 版本在这几页未说明（论文的
  对照版本见 LP-R8）；时间单位未印；"Plain" 行未定义；"6%" 的算法未说明，与表中 Geomean 不直接对应。
- **状态**：verified-web: computational result reported in [LP-S1] (Tables 3.8–3.11, §3.3.4–§3.3.5, PDF pp. 66–68)
- **层级**：verified-web；「6% slower」需核对。

## LP-R19 成本扰动在 NETGEN 与三个一般 LP 上（ParISS，APMOD12）
- **结论**：摘要：50 个 NETGEN 问题总迭代减 5%、总时间减 36%，3 题变慢，35 题时间减 10%、25 题减 30%，最好情形 netgen114
  "solved 350% faster"；netgen108 迭代减 10%、时间提高 2.2 倍（各组件中 PRICE 0.31 → 0.08 s、FTRAN-DSE 0.17 → 0.05 s，INVERT 几乎不变
  0.14 → 0.13 s）；pds-10 迭代约减 10%、时间减逾 60% [LP-S7 §1–§2, Table 1, PDF pp. 2–3]。幻灯片（改进因子：迭代、速度、时间）：
  pds-100 退化迭代 88% → 0%、2.4、5.2、12.5；neos1 61% → 0%、18.1、1.4、25.8；stormG2-1k 78% → 0%、1.0、1.0、1.0；NETGEN 101–150
  的时间因子 Min 0.93、Average 1.80、Max 6.16，平均退化迭代 32% → 0% [LP-S8 PDF pp. 10, 18]。
- **假设**：求解器为 ParISS（Hall–Huangfu 的对偶修正单纯形，带 DSE 与 BFRT）[LP-S7 §1, PDF p. 1]；硬件、线程、版本均未说明；
  "Improvement factors"、"Speed" 与 "Average" 的类型未定义；阈值：BTRAN/PRICE 10%，NETGEN 上 FTRAN 2%；"350% faster" 与 6.16 无法互相换算。
  机制分析（扰动分开退化的 BFRT 断点、使翻界发生在可能更稀疏的列上）只针对网络 LP，属启发式论证 [LP-S7 §3, PDF pp. 4–5]。
- **状态**：verified-web: computational result reported in [LP-S7] (§1–§2, Table 1, PDF pp. 2–3) and [LP-S8] (PDF pp. 10–11, 18–19)
- **层级**：verified-web。

## LP-R20 partial CHUZR、over-weighted CHUZR 与三者组合（APMOD12）
- **结论**：NETGEN 101–150 的平均改进因子（迭代 / 速度 / 时间）：只用 partial CHUZR 1.06 / 1.63 / 1.73（时间 Min 1.06）；只用
  over-weighted CHUZR 1.03 / 1.77 / 1.83；三者组合 1.05 / 1.87 / 1.97（时间 Min 0.96）；平均退化迭代 32% 分别降到 23%、17%、0%
  [LP-S8 PDF pp. 22, 24, 25]。三个一般 LP 用全部技术：pds-100 1.1 / 7.9 / 8.5、neos1 7.7 / 1.4 / 10.8、stormG2-1k 0.9 / 1.2 / 1.1——
  pds-100 与 neos1 的迭代与时间因子都**低于**只用成本扰动（LP-R19），幻灯片未作评论 [LP-S8 PDF pp. 10, 26]。
- **假设**：同 LP-R19；partial CHUZR 在随机子集上做 CHUZR，作者称其见于 Clp、不知有发表文献 [LP-S7 §4, PDF p. 5]；over-weighting 的
  确切选择规则幻灯片未印。
- **状态**：verified-web: computational result reported in [LP-S8] (PDF pp. 22–26)
- **层级**：verified-web。

## LP-R21 网络 LP 上 over-weighting 等价于 1-范数 steepest edge
- **结论**：若 B^{-1} 的每个非零元满足 [B^{-1}]_ij² = 1（网络问题），则 ‖e_i^T B^{-1}‖_1 = ‖e_i^T B^{-1}‖_2² = ŵ_i² = |J_i|（B^{-1} 第 i 行的
  非零个数）；因此用 ŵ_i² 加权（over-weighting）即 1-范数 steepest edge，也即按行密度加权。一般 LP 上
  "Computing 1-norm weight or row density is intractable"，故幻灯片提议一般情形用 ŵ_i² 作替代 [LP-S8 PDF p. 23]。
- **假设**：网络 LP 的单位幅值性质；ŵ_i 是 B^{-1} 第 i 行的（不平方）2-范数——由幻灯片自己印出的等式链确定。
- **状态**：proved-in-source [LP-S8]（一行恒等式，PDF p. 23）
- **层级**：verified-web。

## LP-R22 ParISS：最早的报告结果（ERGO-11-007 表 1）
- **结论**：几何均值加速（相对 1 核）2、4、8 核为 1.16、1.28、1.30，作者称 "(geometric) mean speed-up was about 30% on 4 and 8 cores"；
  相对 Clp：1 核均值 0.37（只有 cre-b 比 Clp 快，"slower by a factor of 2.7 on average"），8 核均值 0.48（4 题至少与 Clp 一样快，平均仍慢
  2.1 倍）；最好的 8 核加速 stocfor3 为 3.39，但该题 1 核只有 Clp 的 0.13、8 核仍为 0.46 [LP-S6 §4, Table 1, PDF p. 7]。
- **假设**：Netlib 与 Kennington 共 114 题：去掉 1 秒内解完的 84 题、ParISS 在某次运行失败的 14 题、比 Clp 慢十倍以上的 3 题，剩 13 题；
  Clp 1.06 [LP-S55]（串行对偶）；双路四核 AMD Opteron 2378，C++ + OpenMP + Intel 编译器；每核一个 tableau 行，INVERT 串行且不重叠
  [LP-S6 §3–§4, PDF pp. 5–7]；对 Clp 两列的均值类型未说明；ParISS 用哪种基更新在本报告中未说明（[LP-S2 §3, PDF p. 9] 称其基于 PF）。
- **状态**：verified-web: computational result reported in [LP-S6] (Table 1, §4, PDF pp. 6–7)
- **层级**：verified-web；会议版（LNCS）数值未读，不得假定相同。

## LP-R23 ParISS 2.0（PPAM 2011 幻灯片）
- **结论**：串行效率（1 核，相对 Clp）25 题均值 0.92，最高 dcp2 1.93、最低 pilot87 0.39 [LP-S12 PDF p. 34]；并行效率表（2/4/8 核与 best）
  只印一个未标列名的 Mean 1.21，maros-r7 的 best 只有 0.28 [LP-S12 PDF p. 35]；"ParISS 2.0 (8 cores) relative to Clp (1 core)" 表 Mean 1.11，
  但该表逐题数值与上一页的 8 核列完全相同——两页标题不可能同时成立 [LP-S12 PDF p. 36]；总结页
  "Average (best) of 18% (50%) relative to 1 core" 与相对 Clp 的 10%（50%）无法从表中追溯 [LP-S12 PDF p. 41]。
- **假设**：25 题（Netlib + Kennington + 作者的两个问题，选法未说明）；双路四核 AMD Opteron 2378 [LP-S12 PDF p. 33]；Clp 版本未印。
- **状态**：verified-web: computational result reported in [LP-S12] (PDF pp. 33–36, 41)
- **层级**：需核对（幻灯片内部不一致）。

## LP-R24 2010 年 12 月的首个对偶原型（pds-06、pds-10）
- **结论**：pds-06：1、2、4、8 核求解时间 3.76、2.51、2.00、1.52 s，总迭代 10266、9625、8820、7616；clp dual 1.92 s、9808 次。
  pds-10：12.58、10.01、6.86、5.72 s，总迭代 17983、17051、16263、15404；clp dual 6.61 s [LP-S10 PDF pp. 24–25; LP-S11 PDF pp. 22–23]。
  时间下降同时来自迭代减少与每秒迭代增加。Lancs11 称 "Speed-up of 2.5 leads to it opt-performing clp"（sic）与
  "Underlying serial solver is now competitive with clp"——但同页 1 核时间都慢于 clp [LP-S11 PDF pp. 22–23]。
- **假设**：原型"Written by Qi Huangfu (2010)"，已用 DSE 与超稀疏 PRICE，但 "Does not (yet) use" 超稀疏 B^{-1} 运算与 BFRT；每核一个主元行；
  双路四核 AMD Opteron 2378 [LP-S10 PDF p. 23]；clp 版本未印；只有两题。
- **状态**：verified-web: computational result reported in [LP-S10] (PDF pp. 23–25) and [LP-S11] (PDF pp. 21–23)
- **层级**：verified-web。

## LP-R25 前人并行单纯形的结果（转述）
- **结论**：一手来源转述的他人结果：稠密 tableau 类实现加速「从几十到上千」，但整体不如好的串行稀疏修正单纯形 [LP-S1 §1, §4.1.1, PDF pp. 16, 70–71]；
  Bixby–Martin（基于 Cplex 的对偶修正单纯形）加速在 1 与 3 之间 [LP-S1 Table 4.2, PDF p. 72]；PARSMI 1.7–1.9（每迭代至多快 2.4 倍），
  ASYNPLEX 2.4–4.8 [LP-S1 Table 4.2, PDF p. 72]；Wunderling 无已知加速数据 [LP-S1 Table 4.2, PDF p. 72]；Lubin 等人在块角问题上用 256
  处理器相对串行 Clp 超过 100 倍，但限于该类 LP [LP-S1 §4.1.3, PDF p. 76]；
  "In two of the more successful implementations [8, 9], the limited speed-up came at the cost of unreliability due to numerical instability."
  （[8, 9] 即 PARSMI 与 ASYNPLEX）[LP-S6 §2.2, PDF p. 4]；幻灯片称
  Lubin、Hall 等人在 8192 个 Blue Gene 核上解了 5 亿变量/约束的 LP [LP-S13 PDF p. 25]。
- **假设**：全部是引用方的转述，被引原文未读；测试集与硬件各不相同、不可横比。
- **状态**：cited — [LP-S1] citing [LP-S52, LP-S49, LP-S51, LP-S50, LP-S54, LP-S53]; [LP-S6] citing [LP-S49, LP-S51]; [LP-S13] citing [LP-S54]
- **层级**：verified-web（仅「一手来源如此转述」这一层）。
