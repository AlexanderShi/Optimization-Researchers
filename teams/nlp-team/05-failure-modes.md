# NLP Team · 胡说陷阱清单

蒸馏出的 skill 必须整体移植进「绝不做」部分，一条不删。

## F1 把 O(1/k²) 用到非凸
Nesterov 加速的 O(1/k²) 是**凸**+L-光滑+目标间隙意义 [NLP-R2]。
对非凸问题宣称 O(1/k²) 目标收敛 = 胡说（非凸的标准度量是梯度范数平方的
期望/最小值，速率体系完全不同 [NLP-S16]）。

## F2 把 heavy ball 和 Nesterov 混为一谈
两者保证不同：heavy ball 有光滑强凸反例 [NLP-R4]，Nesterov 有全局凸保证
[NLP-R2]。统称「momentum 已被证明加速」= 胡说。

## F3 宣称 momentum 改进随机采样复杂度
语料的 verified-local 结论恰恰相反 [NLP-R5]。正确说法必须按 03-heuristics H4
的三句话分寸给全。

## F4 从记忆引用精确常数
Nesterov 1983 的领先常数在不同转述里就不一致，本地机器区条目明确要求
verify [NLP-S1]。任何 "≤ cLR²/(k+1)²" 式精确表达都必须现查原文。

## F5 忽略「L 已知」这类安静假设
加速方法无线搜索版本要求 L 已知；低估 L 破坏保证 [NLP-S1 机器区]。
引用速率不带假设清单 = 不合格。

## F6 无约束资格的 KKT 断言
不声明 CQ 就写「最优解满足 KKT」= 胡说 [NLP-S12, S18]。

## F7 局部/全局偷换
「Newton 二次收敛」是局部结果 [NLP-R7]；把它说成全局性质，或把信赖域的
全局一阶收敛 [NLP-R8] 说成快速收敛，都是偷换。

## F8 KKT 归属错误
KKT 条件 Karush (1939) 在先，Kuhn-Tucker (1951) 在后 [NLP-S12]；
只写 Kuhn-Tucker 不算错误引用，但宣称 1951 首创 = 史实错误。

## F9 把探索性实验当确证
本地 momentum 实验（sign reversal 等）在审计口径下是**探索性信号**，
不是确证的 claim [NLP-L2 + autoresearch 审计]。引用本地实验必须带
「exploratory」限定。

## F10 「大家都知道」句式
同 DFO Team F9：无 ID 的「众所周知/显然」删除或显式降级标注。

## F11 最大化形式混入
所有陈述一律 min 形式；引用以 max 形式写的原文结论时，先转成 min 再说，
并注明做了取负转化。
