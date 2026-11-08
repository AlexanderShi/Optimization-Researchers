# 蒸馏记录

## 2026-10-31 (15) · optimization-lead：Bertsimas 作为四支优化团队的总入口

- 用户请求：「我是希望Bertsimas领导所有的optimization team 要不单开一个optimization lead?」，随后「按方案建」。
  查明：此前 Bertsimas 只在明确召集的 Optimization Council 里领导四队；用户本机只装了 `dfo-team`、`nlp-team`
  （`teams/` 语料版），直接问它们时他不在场，product/ 的理事会与各队 skill 都没装
- 新 skill `product/optimization-council/optimization-lead/`（约 3,400 词，含审查后的修改）：问题先到 Bertsimas，他按 Domain Map
  标领域、按阶段门找第一个没过的阶段，再按他自己的召集人规则分派（LP 引擎 → LP；连续、锥、鲁棒非线性 → NLP；
  黑箱 → DFO；全局、混合整数 → MINLP；SD 无队，标为 open）。一队能定的交给该队（NLP、DFO 用语料队 skill
  或本队圆桌；LP、MINLP 没有队级 skill，交给最合适的成员，标「member view」）；两队以上有争议或落在断层线上
  → 召开理事会。各队作为独立 agent 按自己的 skill 回答、原文照录；最后他按签署规则审（现行做法、带求解时间
  测试的模型类、证书或界、决策指标），缺什么就点名。模式：`quick`、`lead only`、`discuss <team>`、`council`、
  `agenda`、`autopilot`；点名单队的问题（「DFO team …」）仍直接交给该队，不经过他
- 接线：理事会圆桌的泛称触发词（"Bertsimas, lead the teams"、"all optimization teams"、「让 Bertsimas 领导所有
  优化团队」）移给 lead，圆桌留 "Optimization Council" 等；Bertsimas 的 SKILL.md 里「被要求带队」的交接改指
  lead（12,881 → 12,904 词，仍在 13,000 预算内）；team.json 加 `"lead": "optimization-lead"`
- kit：`new_team.py` 校验可选的 `lead` 键（能当文件夹名、不与圆桌或成员同名）；`team_check.py` 新增 lead 一项
  （SKILL.md 存在、frontmatter name 一致、链接圆桌、本队成员和每个 guest 队），反例测试（缺文件夹、多一个 guest
  队、多一位成员、非法名字）都能报错
- 对抗审查（9 个 agent，只读）：四个视角（协议一致性、路由事实、作为 Claude Code skill 的可用性、诚信）加一次
  冒烟测试（真跑一题：领衔定性分派 → DFO 语料队回答 → 领衔审），共 93 条意见，去重后 58 条修改全部采纳（7 高、
  36 中、15 低），24 条驳回并写明理由。要点：
  - 语料队的缺口改由成员补：NLP 语料不含鲁棒（含 DRO）与锥（交 Curtis、Wächter、Ye 或 Ye、Toint、Nesterov）；
    DFO 语料不含离散、多目标、会崩的黑箱与软件细节（交 Audet、Vicente、Powell）；LP 的内点、PDLP、presolve、
    crossover 不在 Huangfu 的记录里（交 Ye、Wright）。以上均已在各队章程与 team.json 里核实
  - 圆桌不能当一个子 agent 跑（它的检查点要用户），只作会话内交接（`discuss <team>`）；领衔的 brief 带上理事会
    的 FL1–FL6 原文；审查按字段标「已给 / 不存在 / 等用户 / 缺」；新增检查点 B；各队答复开头先给 BOTTOM LINE，
    上限 700 词
  - 用 Claude Code 官方文档核实了两点：skill 名总在列表里，但列表超预算时最少用的 skill 先被删掉描述；`/skill-name`
    可直接调用
- 第二次冒烟测试（4 个 agent，用修改后的 skill）：21 项合规检查过 17 项。另 4 项里，2 项是测试 agent 违反了 brief
  已有的规定（领衔替该队先答了证书一项；答复 850 词超上限）；2 项由 skill 文本造成，已修：审查加「本队声明不在
  证据内」一档并点名能补的成员，长度改为每队 150 词加公共部分 150 词
- 文档：理事会 README（团队表、安装 28 个文件夹、用法「通过 lead 问各队」、诚实边界）、DEEP-READING 一行、
  product/README 第 11 行
- 安装（用户回复「装上」）：按 README 装进 `~/.claude/skills`，28 个文件夹（理事会三个、23 位客座成员、NLP 与 DFO
  两个圆桌；LP、MINLP 圆桌是模板，不装），只拷 git 跟踪的 1,372 个文件、48 MB：Bertsimas 文件夹里 git 忽略的
  501 个 PDF 和 516 个 txt（约 600 MB）不拷，README 安装一节补了这句。逐字节比对 1,372/1,372 一致，frontmatter
  名与文件夹名一致；已装的 `dfo-team`、`nlp-team` 与 `teams/` 下的相同；当前会话的 skill 列表已列出新装的 skill。
  未推送、未合并

## 2026-10-31 (14) · Dimitris Bertsimas 深读档 + 九个优化领域 + Optimization Council（主持四队跨队讨论）

- 用户请求：「蒸馏一下Dimitri bertsimas 做非常详尽的蒸馏并按照不同optimization领域来划分 并且让他领导所有optimization
  team 进行discussion」。**更名**：「Dimitri bertsimas」按 MIT 的 Dimitris Bertsimas（Boeing Professor of Operations
  Research）处理，不是 Dimitri P. Bertsekas；SKILL.md 的路由表把 Bertsekas 列为不代言。team-kit 线，分支
  `bertsimas-council`（独立 worktree `Optimization-Researchers-bertsimas`，基于 `minlp-team`，已含 lp-team 合并），
  2026-10-28 至 10-31 共 27 个提交，未推送、未合并
- 新团队 `product/optimization-council/`（深读档）：team.json 一位成员 + `guest_teams` 四队。Bertsimas 是召集人兼主持，
  `council-roundtable` 把 LP、NLP、DFO、MINLP 四队 23 位成员作为客座代表团入座
- kit 改动（两个提交）：`team_check.py` 与 `check_citations.py` 认理事会圆桌（team.json `guest_teams`），领域文件进引用
  扫描；`check_citations.py` 把成员文件里的 `[<他队成员> card …]` 解析到那位成员自己的卡片
- 流水线：T1 研究笔记 01–06 + 2014 Sloan 口述史转录（CC BY-NC 4.0，MIT Libraries）→ 出版物清单（965 行：932 Scholar、
  22 DBLP/Crossref、11 主页；186 行 dup_of）→ T3.2 开放全文索引 → T3.3 追源（186 个开放副本、42 个摘要）→ T3.5 四轮读卡
  → T3.6 汇总（新增 Method 7「先界后策」与 Heuristic 10，更正 C1–C21，证据账本 09 与技巧目录）→ T3.7 精简 → T4 书籍增量
  （21 张书籍公开部分卡：1997 序言、目录、勘误、出版社页、书评；C22）
- 覆盖：932 条 Scholar 行 → 751 部不同作品，473 部有开放全文；413 部全文精读、59 部读了部分、63 部摘要级、56 部元数据级、
  160 部跳过（学生论文、报告、非本人作品）；632 张卡（611 张研究卡 + 21 张书籍材料卡），1,125 条摘录逐字核对（1,122 条
  完全一致、3 条忽略空白与符号后一致、0 条找不到）。八本书只读公开部分，正文未读
- 按领域划分：用 team.json 的九个代码（LO 线性、IO 整数与混合整数、RO 鲁棒与自适应、CP 凸/锥/矩与多项式、SD 随机动态与
  排队、ML 机器学习与统计、DA 规范分析、HS 启发式与仿真、AP 应用）。800 项（779 部研究作品 + 21 项书籍材料）每项两位
  标注员，61 项裁决；`references/domains/` 九个领域文件共约 55,000 词，结构相同（§1 足迹到 §9 覆盖与缺口，§6 是与各队的
  交锋点和判定试验），两视角核验提出 271 条意见、采纳 270 条；SKILL.md 新增「Domain Map」九行八列（声音、时期与权重、
  代表作卡片、典型做法、涉及队伍、文件）和一条路由行
- 声明审计（零上下文双审计员，写手 ≠ 审计员）：SKILL.md 抽审 40 条 + 技巧目录 20 条，0 unsupported，15 条 partial 收窄；
  SKILL.md **全量普查** 318 条带页码声明（A 260 supported / 58 partial，B 253 / 65，0 unsupported），任一审计员标出的
  67 条中 63 条收窄或改引、4 条维持原文；九个领域文件抽审 2,459 条中的 108 条（0 unsupported，12 条收窄），其中引他队
  卡片的 11 条按对方卡片重审，11/11 supported。所有改前措辞原样存入 09 账本
- 抓到的真问题：H005 主页列为他的论文，Crossref（DOI 10.1007/s10994-022-06128-5）作者是 Amram、Dunn、Zhuo，works.json
  标为非本人，领域标签 NONE；SD 与 CP「无陈述方法论」被全文推翻（C1：SD 有 1988–1995 的单独署名文本，CP 只有合著）
- 工具缺陷（留作后续）：`audit_claims.py` 给 `[<slug> card S…]` 形式的引用配的是**领衔成员自己的同号卡片**，领域文件
  抽审因此有 11 条 uncheckable；本次用临时脚本按对方卡片重建审计包绕过，kit 本身没改
- 状态精简（2026-10-31）：Domain Map 使 SKILL.md 按 `team_status.py` 的算法到了 13,153 词（> 13,000）。更正清单 C1–C22
  （带卡片）与「声称未证」「web 阶段更正」两条原样移入 09 账本（`#corrections-list`、`#claimed-unverified`），SKILL.md
  每条更正留一句要点，现 12,881 词，`check_ledger.py --before` 通过；ML §6.1 第 1 点的「双向交锋」注明只见于两队笔记、
  不在任何卡片上
- 理事会圆桌（41 个 agent）：每队挖 4 条断层线，共 16 条，每条两位核验员对抗核验，留 14 条、弃 2 条（定制 LP 求解器之争；
  矩模型对 Wasserstein 集合）；写成 6 条编号断层线 FL1–FL6（`team_check` 只许 3–6 条），双方证据俱全；入座表 15 行，
  每行由 Bertsimas 主持，23 位客座有 22 位入座（Fletcher 不在任何一行）；agenda 模式（`agenda` / `next` / `plan`）；
  协议审与诚信审共 26 项意见，全部至少部分采纳，其中 3 项部分拒绝（与 `team_check` 规则冲突，或属于成员文件——后者已在
  状态精简中补上）
- 首次理事会讨论（2026-10-31，`product/optimization-council/first-session-2026-10-31.md`，约 53,000 词）：agenda 模式，
  自动跑到检查点 4。Bertsimas 选题「精确性的代价」：可认证的精确答案何时值得其计算，"now tractable""certified""robust"
  各凭什么。四个议题各对一队、各落在一条断层线：「why now」加速比凭什么（LP，FL1）、证明时间给统计估计量买到什么（NLP，
  FL2）、模拟器上停下的鲁棒搜索能声称什么（DFO，FL4）、更重的锥松弛何时不再划算（MINLP，FL5）。四队十位代表入座
  （Huangfu；Gould、Nocedal、Wright；Vicente、Audet、Conn；Sahinidis、Burer、Dey）
  - 首轮 36 个 agent（框定、9 份开场、4 次领衔回应、9 份反驳、计划 v1、中立性检查、9 份签署、核查、组装）。**漏洞**：
    会话脚本只让 delegate 发言，漏了各议题的挑战者（Sahinidis 议题 1–2、Conn 议题 3、Dey 议题 4），违反圆桌 Step 1–2
    「挑战者与 delegate 同席」；计划 v1 的开放问题 16 和核查员都指出了这一点
  - 补跑挑战者回合（29 个 agent）：挑战者读议题全程记录和 v1 后开场 → Bertsimas 回应 → 挑战者回驳一轮。Bertsimas 据此
    起草 v2，v1 的 6 个附条件意见（Gould、Nocedal、Wright、Audet、Sahinidis、Burer）全部采纳并写进计划；经主持人中立性
    检查（如把「item 2 已在 (V1) 解决」改回未决）后 11 位全员重签：6 位签署（其中 Gould、Sahinidis 的附加条件 v2 尚未
    满足）、5 位异议（Nocedal、Wright、Audet、Conn、Dey），各附签署条件，留给用户在检查点 4 决定
  - 核查三轮：第一轮 40 条关键引用，12 个问题、7 项未证；第二轮三位核查员（卡片引用 287 条、具名事物与数字 193 项、
    对记录的忠实度 181 项），27 个问题、17 项未证；最后普查首轮全部 271 条卡片引用（17 个审计员，每块再配一个反驳者）：
    236 条成立，35 条被标、2 条被驳回，33 条存疑，其中 23 条为新标注，v2 照抄的 5 处同一引用也标上；并更正第一轮的
    3 处误读（S095 卡确有 stall-count 停止、S080 卡确有 p. 6、S014 卡确有 p. 17）。所有问题以斜体注记留在原处，未删
    任何内容；核查员原文里的本机临时路径改为「path omitted here」
  - 普查发现的规律：领衔在议题 4 把「按结构选乘积」说成自己论文的未来工作，而 S415 p. 30、S708 p. 42 写的是部分 /
    选择性乘积（2026 修订版按违约迭代加约束），「按结构」只是推断；Problem Card 把 (2,000, 10) 设计配了 SNR 6、1、
    0.05，S095 p. 11 实际只在 SNR 0.05 跑它
  - 源头修正：圆桌 FL2 判定试验把 10⁻²/10⁻⁴/10⁻⁶ 三档容差引到 Nocedal 的 S043 p. 7，而该卡只有对齐的 10⁻⁶ 一档；
    已改为「三档是本试验的设计」，并注明 QUIC 只有 CRAN 存档 1.1.1；会话记录里的 FL2 照抄件保留会话当时的措辞
  - 只设计、未运行任何试验；计划 v2 等用户在检查点 4 批准
- 已知边界：LP 与 MINLP 两队的团队圆桌仍是模板（T2 未跑），理事会把 LP 引擎问题转给 solo qi-huangfu，把 MINLP 求解器内核
  转给 Sahinidis、Dey 或 Leyffer；23 位客座中 12 位没有卡片（NLP 九位基础档、Huangfu、Grossmann、Sahinidis），只能引其
  SKILL.md 与研究笔记
- 闸门（全部 exit 0）：`team_check.py product/optimization-council` 14 项 0 失败（skill 12/12、works 0 错误、cards 632 张
  0 条未读行、quotes 0 NOT FOUND、ledger 52 个锚点、citations 0 problem）；`check_links` 29 个文件 0 断链（含会话记录）；无 `[TODO`、
  无 `{{`

## 2026-10-25 (13) · 语料流水线质量门机械化（G1–G7）+ 两队 skill 重新对账

- 用户请求：「强化一下Optimization researchers里知识蒸馏的技能」。理解为强化蒸馏**技能本身**（协议、质量门、
  路由 skill），不是某位研究者的档位。分支 `distill-gates`（独立 worktree，主 checkout 停在 `minlp-team`），
  fast-forward 合入 `main`
- 缺口：DISTILL.md 的 G1–G6 自 2026-10-09 起全靠蒸馏 agent 口头「扫描」「grep 核对」，六次蒸馏没有一条结果能被
  第三方复跑；team-kit 线 2026-10-10 补了 `check_citations.py` / `audit_claims.py` 之后，语料线成了仓库里唯一没有
  机械闸门的产物线。运行教训（分支、用量窗口、Windows、Scholar 登录、OCR）只存在于各条 LOG 和会话记忆里
- 新增（协议见 `standards/distill-gates.md`）：
  - `scripts/distill_check.py teams/<team>`：语料 lint（前缀、重复 ID、01 的层级小节、04 的结论/状态/假设/层级行、
    02 的共识/分歧小节、语料内 ID 闭包、裸 ID、档案三重验证）+ G1 ID 闭包（跨队 ID 到对方语料解析）与承重条目
    无 ID 提示 + G2（作者, 年份）闭包（同一 canon 行须含年份与全部姓氏，折叠重音）+ G3 结果表结构与语料外数字 +
    G4 诚实边界四项、两处 hash 一致、**语料版本戳核对**（是本仓库提交、在当前历史上、语料自此未变、工作区干净）+
    G5 F/R/H 逐条覆盖与未引用的 S/L + G6 试答题小节 + `--installed` 安装漂移。✗ 退出码 1，⚠ 要人看
  - `scripts/distill_audit.py teams/<team> --sample / --report`：G7 声明→语料抽审。抽承重部分带 ID 的声明，配上所引
    ID 的定义（01 行 / 04 整节 / 03、05 整节）与 00–05、researchers/ 里提到它的每个条目，写成审计包 JSON + .md；
    零上下文 agent 判定 supported / partial / unsupported / uncheckable；报告追加到 `teams/<team>/CLAIM-AUDIT.md`，
    unsupported > 0 退出码 1。与 kit 的 `audit_claims.py` 同一套判定与铁律（写手 ≠ 审计员）
  - 试答题进语料：`teams/<team>/00-charter.md` 新增「试答题（G6）」小节，四类各一（选型、陷阱、分寸、**语料外**），
    每题标明应命中的 ID 与通过标准。此前 DISTILL.md 硬编码三题、两队共用、没有语料外题（G6 要求「如实说未覆盖」
    却从没测过）；MINLP 立队时已经要另拟题
  - `RUNBOOK.md`：两条流水线共用的运行纪律（分支/worktree、用量窗口与中断、Windows、team-kit 常见坑、语料线、
    完成后），全部来自第 (8)–(12) 条的实跑教训
  - DISTILL.md：Phase 0 加 `--lint` 前提与 distill-gates 必读；Phase 2 规则 4 写明升格启发式的编号与 ⚠；Phase 3 规定
    语料版本戳 = 语料最后一次改动的提交、两处一致；Phase 4 每道门标出脚本管的部分与人管的部分，G6 改读 00-charter
    的题，新增 G7；Phase 5 修正安装路径（`skills/` 目录 2026-10-09 已取消，命令却一直没改）并加 `--installed`
  - `standards/skill-template.md` 诚实边界加 G7 一行、页脚改 G1–G7；README、TEAM-KIT.md（对照表、本地修改表注明
    两个脚本不是 kit 文件）、项目级 skill（升档问档位、协议维护一行、闸门命令、RUNBOOK 指针）同步
- 首跑抓到的真问题：两份 SKILL.md 的语料版本 `6e2011c` **不在 main 的历史上**——2026-10-23 删署名重写历史后，
  该 hash 只靠 `refs/original/` 备份存活，同树提交为 `2c88951`；六次人工 G4 都没发现。处理：先提交试答题（语料提交
  `75ce176`），两队 SKILL.md 改戳 `75ce176`（事实条目未变，诚实边界写明来龙去脉），不重蒸馏
- 负向测试：复制 dfo-team 到 scratch、注入 11 处缺陷（不存在的 ID、跨队不存在的 ID、裸 ID、语料外作者-年份、语料外
  常数、删一条 F、删一行 R、头部与边界 hash 不一致、04 重复定义、状态行无 proved/cited、05 引不存在的 L），
  `distill_check.py` 11/11 抓到（10 ✗ + 1 ⚠）
- 两队全量结果：0 ✗ · 13 ⚠。⚠ 的处理：
  - `lint result-fields 缺 **假设**`（DFO R5/R7/R8/R9、NLP R5/R6）：语料 04 这几条本来就没写假设行（反例、差分区间、
    SMTP、profiles、momentum 实践面）。**留着**：补假设要读原文，不能从记忆补（grounding 第 1 节）；下次语料维护时
    按原文补或写 `(unanchored)`
  - `G3 result-row 假设列只有 —`（DFO R5/R8/R9、NLP R6）：同上，反例/工具/实证类结果，可接受
  - `G1 unknown-label H9`（NLP）：H9 是 Scheinberg 档案 ✅心智模型升格的启发式（第 (4) 条），03 无对应编号。
    SKILL.md 该条已加注出处；更稳的做法是把它写进 03-heuristics，留给下次语料维护
  - `install`：安装副本旧于仓库，Phase 5 重新复制后消失
- G6 试答（用两份 SKILL.md 逐题作答，核对命中）：
  - DFO 1 选型：先问噪声类型（H1）；噪声主导先 ECNoise 估噪声再定差分区间 [DFO-S22, S3]（H4）；低维、评估贵、底层光滑 →
    模型型信赖域 [DFO-S2, S16]；带噪不用无噪设计的固定小 h [DFO-S3]；评估次数计费并声明 (d+1) 口径 [DFO-L1]（H2）；
    对比用双 profiles [DFO-S2, S8]（H3）——命中 ✓
  - DFO 2 陷阱：无一般收敛保证，McKinnon 反例 [DFO-S10]、[DFO-R5]；正面结果仅受限情形 [DFO-S11]；正式对比配 MADS 或
    模型型方法（H5，[DFO-S14]）；F2 ——命中 ✓，无编造定理
  - DFO 3 分寸：两点估计相对随机梯度至多 √d 因子、单点高斯平滑 O(n) 级、信息论下界证 sharp [DFO-R1; DFO-S21, S20]，
    常数查原文（F7）；SMTP 收敛性已证 [DFO-R8; DFO-S5]，「数量级改进」语料无定论（流派对比分歧 4，[DFO-L2] 在研）——
    两处「无定论」如实说 ✓
  - DFO 4 语料外：BO 核函数——「语料未覆盖」（F8、00-charter 边界、诚实边界缺口），只说 BO 是独立流派 ✓
  - NLP 1 选型：先 H2（尺度/条件数、有限差分核对解析梯度 [NLP-S5]，带噪区间见 [DFO-R7]）；中小规模 L-BFGS 默认基线
    [NLP-S10, S5]；非凸要稳健 → 信赖域 [NLP-S6]；病态先预条件 [NLP-S5]——命中 H1/H2 ✓
  - NLP 2 陷阱：不是全局；二次收敛是局部性质（Hessian Lipschitz、解处非奇异、初始点近）[NLP-R7; NLP-S5]；全局要线搜索
    [NLP-S17] 或信赖域 [NLP-S6]；信赖域的全局收敛是一阶 lim‖∇f‖=0 [NLP-R8]；F7 ——局部/全局分开 ✓
  - NLP 3 分寸：H4 三句——确定性凸 Nesterov O(1/k²) 可证加速 [NLP-R2; NLP-S1, S13]；heavy ball 二次局部加速、光滑强凸
    反例 [NLP-R4; NLP-S14, S7]；随机不必然改进采样复杂度 [NLP-R5; NLP-S3, S4]、收益与初始化/调度耦合 [NLP-R6; NLP-S2]；
    不混同 heavy ball 与 Nesterov（F2）✓
  - NLP 4 语料外：Adam 收敛证明——「语料未覆盖」，Adam 及之后仅 [NLP-S16] 综述级（00-charter 边界），不给定理/反例/出处 ✓
- G7 抽审（各 20 条，seed 1；审计员 = 只读审计包的独立子 agent，与写手分离）：
  - dfo-team：pool 53，**20 supported / 0 / 0 / 0**。审计员记了三处「忠于语料但语料本身可再斟酌」：流派表 Duchi 一格把
    [DFO-S23]（随机平滑）与 [DFO-S21] 并列在「两点+下界」后（02-schools 流派表原样如此）；F2 的 skill 版漏了「正面结果仅
    [DFO-S11] 受限情形」的括注——已补回；F4「三种噪声模型互不迁移」是 05 自己的综合、[DFO-S3, S22] 是噪声处理文献。
    另发现语料内不一致：fixed-budget/fixed-target 在 02 归 [DFO-S2 content]、在 03 H3 归 [DFO-S8]，skill 两处都引，留给语料维护
  - nlp-team：pool 67，**19 supported / 1 partial / 0 / 0**。partial：H1「凸+要最优速率 → 加速梯度」漏了 03 H1 的
    「可承受精确调参」——按 03 收窄为「凸、可承受精确调参、要最优速率」，同一审计员复判 supported（CLAIM-AUDIT.md 有 follow-up）
- 提交：`97a1f64` 闸门与文档 → `75ce176` 语料试答题 → skills 改戳 + 抽审报告 → 本条
- 成本：子 agent 约 37 万 token（两次抽审各 12–13 万，复判 1 万）；主会话内完成脚本、文档与试答
- 执行模型：claude-fable-5-1

## 2026-10-17 (12) · Jorge Nocedal 深读档（nonlinear-team 第二位深读成员）

- 用户请求：「加强nonlinear team nocedal的蒸馏」，选完整深读档（T3.1–T3.8）。分支 `nocedal-deep-read`（独立 worktree）。
  Robinson（第 11 条）先合入 main，本分支 merge main 后带全体 11 人重做 T3.8（旧的 10 人版留作标签 `nocedal-t38-10members`）
- 产物（`product/nonlinear-team/jorge-nocedal/`）：
  - 发表全表：223 条 Scholar 行，56 条 `dup_of`，剩 167 个不同作品，另有 12 项书籍材料；`validate_works.py` 0 错误。
    审计改正了 3 篇 LNM 章节的年份（Scholar 给的是 SpringerLink 上线年）、S150 的年份，以及 S111、S179、S188 被截断的作者和标题
  - 开放全文 97 篇（获取 73 → 补搜 91 → 读卡时又找到 6 篇）。卡片 209 张，分 36 个批次文件、5 轮读完：全读 80，部分 17，
    摘要 39，元数据 23，跳过 8，书籍材料 12；340 条摘录全部逐字匹配（宽松匹配 0）
  - 07–10、`technique-catalog.md`。SKILL.md 改写后 11,687 词：
    - 新增 Method 7「让曲率样本独立于梯度样本，并按梯度计价」，对照其他成员排他性成立，内层求解一步标为与 Curtis 共享
    - 新增 Heuristic 11、12，按全文更正 C1–C21
    - 约 60 个候选里，多数因在别的成员身上也成立（Curtis、Wächter、Toint、Ye、Gould）而被否
- 数字字体层坏掉的全文：97 篇中有 26 篇正文完好，但数字、希腊字母、数学符号和 fi/ff 连字全丢，第 1 轮读卡只能读正文。
  其中有 L-BFGS 1989、L-BFGS-B、紧凑表示 1994、Acta Numerica 1992、NITRO。本机装了 tesseract（winget），全部 OCR 后重读：
  10 篇在第 2 轮重读，16 篇在 T4 `inc-ocr` 重读。重读带出 C14–C19 六处更正，例如 KNITRO「与 LANCELOT 相当」只在 14 个大问题上成立
- T4 增量两次：`inc-ocr`（上条）和 `inc-book`。后者读《Numerical Optimization》两版的前后附录、勘误、zbMATH 书评和 Springer 页面。
  书与 S. J. Wright 合著，Wright 也是本队成员，书籍材料只用来定时间和定位，不当作 Nocedal 一个人的声音，也不据此升格方法。
  两次增量各自在 +400 词上限内，合起来却让 SKILL.md 到了 13,121 词，于是跑 T3.7 精简到 11,666 词（`--before` 无损）
- 声明抽审（每条两位零上下文审计员，有分歧时第三位裁定）：
  - 第一轮 SKILL.md 60 条：50/10/0/0，两位审计员 59/60 一致；10 条 partial 收窄后复判全部 supported
  - 增量后第二轮 SKILL.md 20 条：18/2/0/0；09 与技术目录 20 条：17/3/0/0。收窄后复判全部 supported；
    另有 1 条无需改，原因是脚本不会按声明里写明的批次选卡
- kit 改动（TEAM-KIT.md 本地修改表都有记录）：
  - `verify_card_quotes.py` 去掉 U+FFFE：pdfium 写在行末的断词连字符，59 篇全文受影响
  - `acquire_fulltexts.py` 识别数字全丢的文字层并自动 OCR：阈值 0.5%，26 篇坏文本抓到 24 篇，1112 篇正常全文 0 误报
  - `quality_check.py` 把输出重配置为 UTF-8
  - `audit_claims.py` 在同样深的卡片里取最晚一轮：原来会把 OCR 重读前的旧卡片交给审计员，第二轮抽审有 10 条因此换卡重审
- 团队层（T3.8，11 人）：
  - 圆桌 fault line 1–3 的 Nocedal 一方改为卡片证据（S052、S053、S042、S019、S041 等），Curtis 与 Robinson 一方保留
  - DEEP-READING、README 的覆盖表原样取自 `team_status.py`
  - merge 时 Nocedal 的 Roundtable Card 两边都保留：main 的 Robinson 分歧与措辞精简，本分支的 Method 7 与盲点。
    RESOURCES.md 里 main 的第 200 行改编为第 218 行
- 验证（Windows 11，Python 3.13）：
  - `team_check.py product/nonlinear-team` 29 项 0 失败 0 跳过；`check_citations.py` 全队 0 问题；`check_links.py` 129 文件 0 断链
  - Nocedal `quality_check.py` 12/12；`check_ledger.py --before`（精简前副本）通过；无 `{{`、`[TODO`
- 运行教训：
  - 第 1 轮读卡跑到周用量上限，21 批停在 16 批，用 `only` 补跑剩下 5 批
  - `inc-book` 跨会话中断，用 `resumeFromRunId` 续跑；检索 agent 把半途留下的文件挪进 scratch，没有删
  - 改了 works.json 的标题，文件名 slug 也会跟着变，本地 PDF/txt 要随之改名（S188）
- 成本：子 agent 约 2,490 万 token（读卡约 900 万，两次增量约 510 万，抽审与收窄约 430 万，T3.6 约 240 万，
  T3.8 两次约 270 万，其中 10 人版作废）；`inc-book` 首跑中断那部分未计量
- 执行模型：claude-opus-5-5

## 2026-10-17 (11) · Daniel P. Robinson 加入 nonlinear-team（轻量档，第 11 位成员）

- 用户请求：「蒸馏一下Daniel P Robinson 放到nonlinear team」，选轻量档（T1 + 带全体重跑 T2，不做 T3）。分支 `robinson-member`
  （独立 worktree，与 Nocedal 深读、MINLP 两个会话隔离），fast-forward 合入 `main`。scratch 用独立的
  `nonlinear-team-robinson-scratch`，不与共用的 `nonlinear-team-scratch` 混
- 标识（2026-10-16 核实）：DBLP 20/8222（SPARQL；合作者 Vidal 32、Curtis 31）、ORCID 0000-0003-0251-4227
  （Lehigh 2019–、JHU 2011–2019）、主页 coral.ise.lehigh.edu/danielprobinson/；没找到 Google Scholar 主页，`scholar` 留空
- T1（`team-base-skills.js`）：
  - 首跑在周用量上限处整体中断（8 个 agent 全报错），但 02、06 两份笔记已写完（均以 Sources 结尾），先提交；
    用 `dims: ["01","03","04","05"]` 只补跑缺的四路，其余阶段照常（复核步从磁盘读全部 6 份笔记）
  - 结果：复核 ready（288 条来源，约 77% 一手）；4 个核心方法（只假设求解器能检验的东西 / 可扩张子空间加速 /
    嵌入现任方法 / 先做确定性类比，最后一个标为与 Curtis 的联合手艺）；SKILL.md 12/12、8001 词；RESOURCES.md 210 行，
    207 ✅、3 ⚠️
- 额外的保真审计（kit 闸门之外，工作流 6 位分节核查员 → 每节 2 位反驳者 → 修复 → 复核）：对照 Crossref、arXiv、DBLP、
  研究笔记，以及 Curtis 深读档里 35 篇与 Robinson 合写论文的全文与卡片。419 条声明，381 条成立；38 条问题全部修正，
  其中 6 条重大：截断的 Izmailov–Solodov 引文、随机内点法 v3 的事实错误、把 steering 规则归给 Curtis
  （CGJR16 自己写明来自 Byrd–Nocedal–Waltz）、三处夸大（含 Roundtable Card 里编出的一条「与 Toint 有文献分歧」，
  实际 Cartis–Gould–Toint 说两者界「of the same order」）。复核员再报 9 处残留（与 Gould 合署的引文写成他本人的话、
  A100 一句无笔记出处等），手工逐条核对原文后修好，相应笔记加注日期的更正行
- T2（`team-layer.js`，全体 11 人）：混合档团队必须用 `deep_tier: true`（false 会把 DEEP-READING.md 整个换成轻量档说明，
  抹掉 Curtis 的深读记录）。Curtis 一方的 11 条卡片引用全部保留。kit 的缺口：这个模式会给「刻意保持轻量档」的成员
  写「(card evidence pending for <slug>)」、把覆盖表留给 T3.8。手工处理：删掉 5 处 pending 标记，DEEP-READING / README
  的「nine members」改成 ten，两张覆盖表按 `team_status.py --coverage`（及 `--short`）原样重贴。
  另外补跑了 Robinson 的 OpenAlex 拉取（`fetch_publications.py` 不需要 API key，T1 的 agent 误以为需要）
- T2 差异审计 + 圆桌试跑（kit 第九节最后一项）：首跑因会话结束中断在修复步（已改了 5 个文件的一半）。这 5 个文件从 git 还原后续跑，
  缓存没有命中，9 个 agent 全部重跑。结果：262 条声明，16 条问题（4 条重大，都在圆桌 fault line 的 Robinson 一方，如 TOP 2015
  的引文改写、把事后观察写成预先划分的子集）；试跑题目为「QP 全局解假设 + 秩亏 Jacobian 的 SQP 重设计与 SNOPT/IPOPT 基准」，
  Robinson 入座主讲，4 个检查点齐全、协议通过；评审另报 14 处文件缺陷（座次多行匹配无规则、单模型回退缺少视角隔离、
  计划条目缺少归属、SNOPT 拟牛顿默认与「等量导数信息」冲突等），共修 28 处。首跑核查员报出、次跑没报的 4 处再手工修
  （Ye 卡片补回作者的保留句、Wright 的 Team links 补 Robinson、Gould 卡片里 steering 是联合工作、Fletcher 的 NA223 p.15
  实指无二阶导时的可行性恢复），均先核对原文
- 验证（Windows 11，Python 3.13）：`team_check.py product/nonlinear-team` 24 项 0 失败 0 跳过（Curtis 的摘录核对用从主
  checkout 复制来的 git 忽略的 `txt/`，180 条逐字通过）；`check_links.py` 122 文件 0 断链；`check_citations.py --roundtable`
  0 问题；11 位成员 `quality_check.py` 均 12/12；无 `{{`、`[TODO`、pending 标记
- 留作后续（未改 kit）：`team-layer.js` 在混合档团队里没有「成员刻意保持轻量档」的概念，可在 `team.json` 成员项加 tier
  字段，让 pending 标记和覆盖表的推迟只针对计划深读的人
- 成本：子 agent 约 1,600 万 token 以上（T1 约 540 万，含中断的 150 万；保真审计约 390 万；T2 约 510 万；
  T2 差异审计次跑约 150 万，首跑中断未计量）
- 执行模型：claude-opus-5-5

## 2026-10-10 (10) · Frank E. Curtis 深读档（nonlinear-team 成为混合档团队）

- 用户请求：「强化一下Frank E Curtis skill」，选完整深读档（T3.1–T3.8）。只深读 Curtis；其余九人保持轻量档，
  不计划深读。分支 `curtis-deep-read`（独立 worktree，与 MINLP 会话隔离），fast-forward 合入 `main`
- 产物（`product/nonlinear-team/frank-e-curtis/`）：
  - 发表全表：96 个不同作品（S 96 · D 3 · H 1，4 条 `dup_of`），`validate_works.py` 0 错误。
  - 87 篇开放全文，分 30 个核心批次 + 1 个摘要批次写成 96 张卡片（全读 86，摘要 8，元数据 1，不可读 1，S086 文本层乱码）；
    180 条摘录逐字通过 `verify_card_quotes.py`。
  - 07–09、`technique-catalog.md`，SKILL.md 改写：
    - 核心方法仍是 5 个；提议的 M6「守住现任、让保证休眠」在团队层排他性不成立（Wright、Fletcher、Toint、Wächter 共享这一做法），
      降为 Heuristic 5 的扩展。
    - 新增 Heuristic 11；纠正 C1–C12。
  - 声明抽审 `10-claim-audit.md`：60 条，41 条支持、19 条部分支持、0 条不支持。19 条全部按卡片收窄或改引用后，
    由零上下文核查员复判：16 条支持、3 条部分支持，这 3 条按核查员的卡片读法再收紧（最后一步未再复判）。
- 团队层（T3.8）：DEEP-READING.md 写成混合档记录，覆盖表原样取自 `team_status.py --coverage`；
  README 加入 `--coverage --short` 五列摘要，Curtis 状态改为深读档；圆桌第 1、3、5 条 fault line 中 Curtis 一方改为卡片证据，
  其余九人一方仍引研究笔记。
- kit 改动：
  - `team_check.py` 按成员判档（`deep_members`，混合档圆桌规则）。
  - 修复同一脚本两处正则里的 `\b` 被写成退格字节（0x08），它让混合档圆桌规则看不见卡片引用。
  - `audit_claims.py` 报告里去掉声明中的 markdown 链接（锚点在报告里断链）。
  - 5 个脚本加 UTF-8 输出重配置；`plan_reading_batches.py` 显式 `encoding="utf-8"`。
- 运行教训：
  - 深读档跨了三个用量窗口，子 agent 约 1,200 万 token，其中读卡约 660 万、抽审约 260 万、汇总约 150 万。
  - 被用量上限打断的 workflow 会留下半写的文件（这次的 DEEP-READING、圆桌），续跑前先 `git diff` 审阅再决定重跑或补完。
  - worktree 里 `core.autocrlf=true` 检出的 CRLF 脚本会被 Workflow 工具拒绝，需转 LF（不入库）。
- 验证（Windows 11，Python 3.13）：
  - `team_check.py product/nonlinear-team` 23 项 0 失败。
  - `quality_check.py` 12/12。
  - `check_citations.py`：2655 条卡片引用，0 问题。
  - `check_links.py` 112 文件 0 断链。
  - `workflows/selftest.sh product/nonlinear-team` 全部通过。
- 全文 PDF 与 `txt/`（git 忽略）已从 worktree 复制到主 checkout 同一路径，worktree 随后删除。

## 2026-10-10 (9) · MINLP Team 立队与深读（进行中，因用量上限暂停）

- 用户请求：「我需要一个MINLP team 在这些研究者中选六个 进行彻底蒸馏」。按本仓库惯例做两件产物：
  team-kit 深读档 `product/minlp-team/`（六人研究 skill + `minlp-roundtable`），以及封闭语料
  `teams/minlp-team/` + 团队级 `minlp-team` skill（DISTILL.md）。分支 `minlp-team`，未推送、未合入 main
- 成员（理由：两两之间有可对证的分歧，覆盖凸 MINLP、非凸全局求解、MIQCQP 松弛三条主线）：
  Grossmann ↔ Leyffer（多树分解 vs NLP 分支定界）、Sahinidis ↔ Misener（factorable/BARON vs αBB/ANTIGONE）、
  Burer ↔ Dey（锥松弛 vs 割平面）。team.json 的 Scholar id 取自 DBLP 人员记录、ORCID 与主页（Scholar 作者搜索现需登录）
- 暂停时的进度（`python3 -X utf8 scripts/team_status.py product/minlp-team` 可随时重算）：

| 成员 | T1 skill | T3.1 | T3.2 全文/作品 | T3.3 | T3.5 读卡 | T3.6 |
|---|---|---|---|---|---|---|
| Dey | 12/12 | ✓ | 123/156 | ✓ | 完成（154 张，0 未读） | 挖卡完成，SKILL.md 未改 |
| Burer | 12/12 | ✓ | 67/71 | ✓ | 完成（73 张，0 未读） | 挖卡完成，SKILL.md 未改 |
| Leyffer | 12/12 | ✓ | 162/211 | ✓ | 第 1 轮完成；第 2 轮（摘要）部分 | — |
| Misener | 12/12 | ✓ | 101/147 | ✓ | 第 1 轮完成；第 2 轮（摘要）部分 | — |
| Sahinidis | 12/12 | ✓ | 28/381 | 进行中被停 | — | — |
| Grossmann | 12/12 | ✓ | 获取中（180/1312 时） | — | — | — |

- 续跑（同一会话可用 `resumeFromRunId`；新会话用 make_args.mjs 重新生成参数，读卡用 `overwrite: false` 跳过已有卡片）：
  1. Dey、Burer：`team-synthesize.js`（runId wf_01f11165-82a、wf_705e7fc1-1af）
  2. Leyffer、Misener：`team-read.js` round 2（runId wf_3b31ef0e-d73、wf_5e72e2e4-7e9），之后 T3.6
  3. Sahinidis：`team-chase.js`（runId wf_588a3df1-b1c）→ 切批 → 读卡 → T3.6
  4. Grossmann：重跑 `acquire_fulltexts.py product/minlp-team/ignacio-e-grossmann --delay 10`（会跳过已下载的）→ 补搜 → 读卡 → T3.6
  5. 全体 T3.6 之后：T2 `team-layer.js`（全体，T3.6 运行中不要跑，会互相改 SKILL.md）→ 各人 T3.7 / 声明抽审 → T3.8 `team-integrate.js` → `team_check.py`
  6. 封闭语料：续跑工作流 minlp-corpus-build（runId wf_7f245ead-5af；91 条文献核实完成、五份研究者档案已提交，
     缺 canon/results、Leyffer 档案、00/02/03/05 与三视角复核），之后按 DISTILL.md 蒸馏 `teams/minlp-team/SKILL.md`，
     G6 试答改用 MINLP 题（选型、OA 用于非凸的陷阱、SDP 与 RLT 强弱的分寸）
- 已知限制：本机没有 tesseract，文字层乱码的扫描件无法 OCR（Leyffer 6 篇、Misener 1 篇），退到摘要级；
  Windows 下脚本须设 `PYTHONUTF8=1`（或 `PYTHONIOENCODING=utf-8`），否则 cp1252 控制台会让 acquire / team_status 崩溃
- 更新（同日，低用量收尾）：Leyffer、Misener 读卡全部完成（204 / 146 张，0 未读）；Dey、Burer 的 T3.6 汇总、闸门与声明抽审完成（Dey 17/3/0/0、Burer 15/5/0/0，partial 已按卡片收窄），两人深读档完整，T3.7 不需要（均低于 13000 词）。调研笔记里的 MATLAB 版本号（R2015b 等）会被 check_citations 误认作作品 ID，已改写成行内代码；一次 acquire 崩溃曾把 Leyffer 的 INDEX.md 截到 30 行并进入 7949d35，已从 eb7b6e5 恢复。续跑清单更新为：Leyffer、Misener 的 T3.6；Sahinidis、Grossmann 的补搜→读卡→T3.6；T2；T3.8；封闭语料与团队级 skill。
- 执行模型：claude-opus-5-5

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
