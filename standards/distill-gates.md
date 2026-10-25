# 质量门的机械部分与声明抽审（distill-gates.md）

DISTILL.md Phase 4 的七道门里，能由脚本判定的部分全部交给脚本；人只处理脚本判不了的那一层。
两个脚本都只用 Python 标准库，从仓库根运行（Windows 用 `python3 -X utf8` 或 `PYTHONUTF8=1`）：

| 脚本 | 管什么 | 何时跑 |
|------|--------|--------|
| `scripts/distill_check.py teams/<team>` | 语料 lint + G1–G6 的机械部分 + 语料版本戳 + （`--installed`）安装漂移 | 改语料后（`--lint`）、Phase 3 填完模板后、Phase 5 安装后 |
| `scripts/distill_audit.py teams/<team>` | G7 声明→语料抽审：抽声明配语料证据成审计包，交零上下文 agent 判定，写 `teams/<team>/CLAIM-AUDIT.md` | Phase 4 末、交付前；增量重蒸馏后再抽一轮 |

为什么要有它们：2026-10-09 起的六次蒸馏，G1–G6 全靠蒸馏 agent 自己「扫描」「grep 核对」，没有一条
记录能被第三方复跑；team-kit 那条线 2026-10-10 补了 `check_citations.py` / `audit_claims.py` 之后，
语料线反而成了仓库里唯一没有机械闸门的产物线。首次全量运行（2026-10-24）就抓到两份 SKILL.md 的
语料版本戳 `6e2011c` 已随 2026-10-23 的历史重写失效——人工核对六次都没发现。

## 一、门 → 检查

| 门 | DISTILL.md 的要求 | `distill_check.py` 的检查（代号） | 人还要做什么 |
|----|------------------|--------------------------------|-------------|
| 前提 | 语料本身结构合格 | lint：`no-prefix`、`dup-def`、`tier`、`result-fields`、`schools`、`unknown-id`、`unknown-prefix`、`bare-id`、`researcher` | 补 04 缺的假设/层级行；给裸 ID 补前缀 |
| G1 语料封闭 | 每条事实带语料 ID | `unknown-id`（ID 不存在，含跨队）、`unknown-label`（H/F 标签不在 03/05）、`no-id`（承重条目没有 ID）、`description`（>300 字） | 看每条 `no-id`：是事实就补 ID 或删，是流程规范就留 |
| G2 引用闭包 | 每个（作者, 年份）在 01-canon | `author-year`：同一 canon 行须同时含年份与全部姓氏（折叠重音、忽略 ≤2 字母的缩写）；`--show-pairs` 列对账表 | 看 ⚠（部分命中 / 只在别队 canon） |
| G3 数学纪律 | 速率带假设 + ID + proved-vs-cited；无精确常数；维度因子；噪声模型 | `result-row`（结果表每行：R ID、假设列、状态列含 proved/cited/verified、有 S/L 来源）、`number`（承重部分出现语料里没有的 ≥2 位数字或小数） | 维度因子、噪声模型是否声明——读 G7 的 partial |
| G4 诚实边界 | 蒸馏日期、语料版本、语料缺口、验证层级 | `boundary`（四项齐全、头部契约与诚实边界 hash 一致）、`stamp`（hash 是本仓库提交；在当前 HEAD 历史上；语料自此未变；工作区干净） | 语料缺口清单是否对应 Phase 2 的记录 |
| G5 禁区完整性 | 05 整体移植；04、03 逐条 | `missing-F`、`missing-R`、`missing-H`、`unused-S`（01 的 ID 一次没被引）、`researcher`（档案没被提到） | 条目在但被改写——读 G7 |
| G6 试答 | 用草稿答测试题 | `probes`：00-charter 的「试答题」小节 ≥3 题、每题带应命中 ID（语料外题除外）、含语料外题 | **真的去答**，答案与命中情况记入 DISTILLATION_LOG |
| G7 声明抽审 | （新）SKILL.md 的话是语料真说的 | `distill_audit.py`（第三节） | 处理每条 unsupported / partial |

严重度：✗ 计入退出码（蒸馏不算完成）；⚠ 必须逐条看过，要么改掉，要么在 DISTILLATION_LOG 里说明
为什么留着（例如 H7「报告规范」没有 ID——它是用户的表达约定，不是事实）；`i` 是信息。
脚本能判「有没有」，判不了「对不对」：ID 存在 ≠ 语料这么说，所以 G7 不可省。

## 二、语料版本戳

- SKILL.md 两处（头部语料契约、诚实边界）写同一个 hash：**语料最后一次改动所在的提交**（`git log -1
  --format=%h -- teams/<team>` 在改 SKILL.md 之前的值），不是写 SKILL.md 的那次提交。先提交语料，再
  提交 skill，skill 才有 hash 可写。
- `distill_check.py` 核对：hash 是提交（否则 ✗）→ 在 HEAD 历史上（否则 ⚠，并找出 `teams/<team>` 同树的
  现历史提交供改戳）→ `git diff <hash> HEAD -- teams/<team>`（SKILL.md、CLAIM-AUDIT.md 之外有改动即 skill
  过期 ⚠，`--strict-stale` 时 ✗）→ 工作区无未提交语料改动。
- 历史被重写（例如 2026-10-23 删署名）后，戳会失效但语料内容没变：改成脚本给出的同树提交，在
  DISTILLATION_LOG 记一条「改戳，语料未变」，不用重蒸馏。

## 三、G7 声明→语料抽审

铁律同 `references/claim-audit.md`：**写 skill 的 agent 与审计 agent 必须是两个**，审计 agent 只读审计包，
不读 skill、不读语料全文、不上网、不用领域知识补证据。能用别的模型当审计员更好。

```bash
S=${TMPDIR:-/tmp}/distill-scratch; T=teams/<team>
# 1. 抽样 → 审计包（.json 给脚本，.md 给审计 agent 读）
python3 scripts/distill_audit.py $T --sample --n 20 --seed 1 --out $S/audit-<team>.json --list
# 2. 新开一个 agent，只给它 $S/audit-<team>.md 的路径和下面的 prompt，让它写 $S/verdicts-<team>.json
# 3. 写报告（追加到 teams/<team>/CLAIM-AUDIT.md），unsupported > 0 退出码 1
python3 scripts/distill_audit.py $T --report $S/verdicts-<team>.json --packet $S/audit-<team>.json
```

抽什么：承重部分（框架概览 / 流派对比 / 决策启发式 / 关键结果速查 / 绝不做）里带 ID 的声明。一条声明 =
同一条目里上一组方括号之后、这组方括号之前的分句（太短就带上条目开头）；结果表每行一条（结论 + 假设，
状态列的 ID 是引用）。证据 = 所引每个 ID 的定义（01 文献行 / 04 整节 / 03、05 整节）+ 00–05 与 researchers/
里提到它的每个条目；跨队 ID 到对方语料取。两份 skill 各约 50–70 条可抽声明，20 条是抽查；想严就 `--n 40`
或换 `--seed` 再抽一轮。

审计 agent 的 prompt（可照抄；把路径换掉）：

```
You are the AUDITOR in a two-agent check of a team-level skill distilled from a closed corpus. Your ONLY input
is this packet: <绝对路径>/audit-<team>.md — read all of it (in chunks if needed) and follow its "Brief".
For each "## Item k", judge whether the corpus evidence listed under it supports the item's Claim (Context is
the whole bullet / row, for reference only). Verdict: supported / partial / unsupported / uncheckable as the
brief defines them; one sentence of reason each, naming the evidence file:line that supports or contradicts.
Hard rules: open no other file, no web search, no outside knowledge of the field; when the evidence does not
cover the claim, answer uncheckable rather than guessing. Be strict about numbers, constants, rates,
assumptions, proved-vs-cited status, attributions, noise models and dimension factors; tolerant of wording.
Write exactly one JSON file <绝对路径>/verdicts-<team>.json:
{"auditor": "<model>", "date": "<YYYY-MM-DD>", "verdicts": [{"k": 1, "verdict": "...", "reason": "..."}, ...]}
one entry per item in order. Reply with the counts per verdict and the k of anything not "supported".
```

| 判定 | 含义 | 处理 |
|------|------|------|
| supported | 语料在所引 ID 处写了这件事，声明没有超出语料 | — |
| partial | 有关联内容，但声明更强/更具体/更一般，或加了语料没写的假设、常数、归属、噪声模型，或把分歧写成共识 | 人看一眼：收窄声明，或改引真正支持它的 ID；改完重跑 `distill_check.py` |
| unsupported | 语料没有这个内容，或内容相反 | **必须处理**：改声明或改引用；换 `--seed` 再抽一轮 |
| uncheckable | 证据只有一行文献表（题目 + 角色），声明讲的是题目推不出来的内容 | 多半是该说法只在 skill 里：补进语料（04/02/03）再重蒸馏，或改引有内容的 ID |

报告 `teams/<team>/CLAIM-AUDIT.md` 按日期追加，不改旧节，「To act on」列出 unsupported 与 partial。它是蒸馏
产物，不是语料（`distill_check.py` 的过期判断会把它和 SKILL.md 一起排除）。审计 agent 也会错：reason 指不出
语料位置的判定按 partial 对待，人再看。

## 四、已知边界

- `no-id`、`number`、`unused-S` 是启发式，故意只给 ⚠：表达约定本来就没有 ID，常数可能来自语料里没抄的
  公式，canon 里的教材可以只在来源索引出现。
- 跨队引用（NLP skill 引 [DFO-R7]）要两队语料同在 `teams/` 下才解析得到；只复制一个团队目录出去跑会报
  `unknown-prefix`。
- G2 的（作者, 年份）抽取只认拉丁姓氏 + 年份的写法（`Moré-Wild 2009`、`Sutskever 等 2013`、`Kuhn-Tucker (1951)`）；
  中文写的人名年份不在它的视野里，靠 G7。
- 脚本不读 `product/`（team-kit 产物另有 `check_citations.py` / `audit_claims.py`）。
