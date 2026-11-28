# RUNBOOK · 两条流水线共用的运行纪律

来源：`teams/DISTILLATION_LOG.md` 第 (8)–(13) 条的「运行教训」与 2026-10 月的多次实跑（Curtis、Robinson、
Nocedal、MINLP、语料线闸门）。这些坑每个都至少花过一次重跑或半天手工；做任何蒸馏 / 扩展前先读一遍。
协议本身见 `DISTILL.md`（语料线）与 `TEAM-KIT.md`（team-kit 线）。

## 1. 分支与 worktree

- 每个任务一个分支 + **独立 worktree**：`git worktree add ../Optimization-Researchers-<task> -b <task> main`。
  主 checkout 可能停在别的长期分支上（例如暂停中的 `minlp-team`），不要在它上面切分支。
  做完 fast-forward 合入 `main`；是否推送 GitHub 由用户决定。
- 两个任务都改团队层文件（圆桌、README、DEEP-READING）时，后合入的要先 merge main 再重做 T3.8。
- worktree 里 `core.autocrlf=true` 把脚本检出成 CRLF，Workflow 工具拒绝 CRLF 的 `scripts/workflows/team-*.js`：
  本地转成 LF，**不要提交**这个改动。
- 删除 worktree 前，把 git 忽略的 `product/**/references/sources/papers/*.pdf` 与 `txt/` 复制回主 checkout 的同一路径
  （新容器里 `team_check.py` 的摘录核对要用）。Windows 删 worktree 可能剩一个空的锁定目录，手工删即可。
- 提交信息**不带任何 Claude 署名 / `Co-Authored-By` 行**（仓库规则；2026-10-23 已为此重写全部历史）。
- 历史重写会让 SKILL.md 里的「语料版本」hash 失效：`scripts/distill_check.py` 报 `stamp` 不在当前历史上并给出同树
  提交，改戳、记 LOG，不用重蒸馏。

## 2. 用量窗口与中断

- 一位深读档成员约 1,200–2,500 万子 agent token（读卡 600–900 万、抽审与收窄 250–450 万），跨 2–3 个用量窗口；
  六人深读团队跨多个窗口。先全员 T1，再两三人一批跑读卡，T3.6 运行中不要跑 T2（会互相改 SKILL.md）。
- 被用量上限打断时 agent 多半已经把文件写完：先 `git diff`、看每份笔记是否以 Sources 结尾，再用 `dims` / `only`
  只补缺的部分；半写的团队文件（DEEP-READING、圆桌）手工补完比盲目重跑便宜。
- `resumeFromRunId` 跨会话**不命中缓存**，全部 agent 重跑；续跑前先 `git checkout` 被修改了一半的文件，
  检索 agent 半途留下的文件挪进 scratch 而不是删。
- 每个任务用独立的 scratch 目录（`%TEMP%\<team>-<task>-scratch`），不与别的会话共用。

## 3. Windows

- Python 脚本一律 `python3 -X utf8 …` 或先 `export PYTHONUTF8=1`（cp1252 控制台打印 ✓、… 会直接崩）；
  `scripts/workflows/selftest.sh` 也要在 `PYTHONUTF8=1` 下跑。
- tesseract 装在 `C:\Program Files\Tesseract-OCR`（winget），不在 Git Bash 的 PATH 里：
  `export PATH="/c/Program Files/Tesseract-OCR:$PATH"` 之后再跑 `acquire_fulltexts.py`（含 `--reocr`）。
- Bash 工具里带反斜杠的 heredoc 不可靠：补丁、测试脚本先写成文件再执行。
- `Copy-Item` 装 skill 时目标目录可能不存在，先 `New-Item -ItemType Directory -Force`。

## 4. team-kit 常见坑

- Google Scholar 作者搜索已需登录：Scholar id 从 DBLP 人员记录（sparql.dblp.org 的 `dblp:webpage`）、ORCID
  `researcher-urls`、或研究者主页取；找不到就留空，不要猜。Scholar 个人页（`citations?user=ID`）仍可直接抓。
- `fetch_publications.py`（OpenAlex）**不需要 API key**；`publications/` 为空时手工跑一遍。
- 改了 `works.json` 的标题或年份（年份为空时 slug 里写 `nd`），PDF / txt 的文件名 slug 跟着变：按 `acquire_fulltexts.slug(row)` 给本地文件改名，
  否则报 "rows keep their committed txt/pdf status without a local file"。
- 1990–2000 年代的作者 PDF 常有「正文完好、数字和希腊字母全丢」的文字层：`acquire_fulltexts.py` 自动判定并 OCR
  （tesseract 在 PATH 时）；之前抓的用 `--reocr ID,…` + `plan_reading_batches.py --reread`。按 txt 的数字占比排序能找出来。
- 混合档团队加轻量档成员：`team-layer.js` 用 `deep_tier: true`（`false` 会把 DEEP-READING 整个换掉）；之后手工删
  "(card evidence pending for <slug>)"、按 `team_status.py --coverage`（及 `--short`）重贴两张表、改成员计数。
- 调研笔记里的 MATLAB 版本号（R2015b）会被 `check_citations.py` 当作作品 ID：写成行内代码。
- T3.2 的下载进程按顺序跑，不要并行：arXiv 按来源 IP 限流（每 3 秒一次），四个进程即使各隔 8 秒也会收到 429，被限流的作品
  记成 no-oa。用默认 `--delay 3` 一个一个跑，跑完 `grep 429` 日志，对那几篇再跑 `--only <ID,…> --recheck`（2026-11-26，MILP Team）。
- 一篇全文只挂一个作品。T3.2 之后、每次 `merge_chase.py` 之后都看 `acquire_fulltexts.py` 结尾的 `identical texts`（文本逐字节
  相同的作品）和 `validate_works.py` 的 `same arxiv`：文件留给它本来是的那一篇（报告就留在报告那一行，预印本留在带 arXiv ID 的
  那一行），其余 `--drop`、备注写明，chase 加到别的行上的同一链接删掉；T3.2 之后删掉的放进 T3.3 的 `skip_ids`。标题检索已经不再
  配版本号不同的标题、不再挂别的作品已有的 arXiv ID，但 chase 手挂的链接和以前留下的文件只有这一行能查出来（2026-11-26，MILP
  Team：T3.2 时 8 份，T3.3 之后又查出 20 份）。
- 读卡工作流被用量上限截断时，读卡 agent 先写 `<bid>.md`、后写 digest，磁盘上常留下写完的卡片而没有 digest（2026-11-27，MILP
  Team 第一轮：四个工作流开跑约 10 分钟撞上周上限，86 批里 11 批齐全、29 批只缺 digest、46 批全空）。重跑前逐批分类：卡片和
  digest 都齐的留下；卡片完整（每篇都有 `### <ID> ·` 标题和 Quotes 段）、只缺 digest 的，只从卡片誊写 digest，不重读原文（约为
  重读的三成），写完核对 digest 的编号、标题和引文都出自它自己的卡片；全空的才重读。重跑用 `only` 只列要重读的批次：带
  `batches` 时工作流不做「已有卡片」检查，不带 `only` 会覆盖留下的卡片。几个读卡工作流并行之前先估一下这周还剩多少用量。
- 深读会读到 `holdout.md` 封存件的出处（博士论文、报告里的某几页）。卡片照常写；T3.6 起的综合、精简、增量和整合工作流的
  house rules 把封存件的要点挡在 Skill、08、09、技术目录和圆桌文件之外，别的作品说了同一件事也不写，等验证解封（2026-11-27）。
- 读的是替代版本（报告版、预印本、后一版手册）就写版本引用 `[S025 TR pp. 3–12]`，卡片正文写明。
- 审计包必须给整张卡片（曾因截到 9,000 字符误判 unsupported）；同样深的卡片取最晚一轮（OCR 重读后的）。
- 写 skill 的 agent 与审计 / 复核的 agent 必须是两个；每条声明两位审计员、有分歧第三位裁定更稳。
- 新成员的 SKILL.md、新圆桌写完后跑 `python3 -X utf8 scripts/answer_standard.py --apply product/<team>`（写入
  Answer Standard 一节，并在研究者 skill 的三处旧条款后补位置说明）；`team_check.py` 的 `answer-std` 一项核对。
  要改回答的写法只改 `references/answer-standard.md` 再 `--apply`，不要逐个改 SKILL.md；改完用同一批题对新旧版本
  各答一遍再盲评（`teams/DISTILLATION_LOG.md` 2026-11-14「回答标准」一条的做法），写法好不好只有读回答才看得出来。
- 字数预算（T3.6 的 11,500 / 13,000、T3.7、`team_status.py --max-words`）不算 Answer Standard 一节：量词数用
  `python3 -X utf8 scripts/answer_standard.py --words <SKILL.md 或目录>` 的第一列，不用 `wc -w`（2026-11-20 起）。

## 5. 语料流水线（DISTILL.md）

- 改语料前后都跑 `python3 -X utf8 scripts/distill_check.py teams/<team> --lint`；填完模板跑全量；装完跑 `--installed`。
- 「回答标准」一节不手写：填完模板跑 `python3 -X utf8 scripts/answer_standard.py --apply teams/<team>`，装完跑
  `--check --installed`。
- G7：`scripts/distill_audit.py --sample` → 新 agent 只读审计包 `.md` → `--report`；unsupported = 0，partial 逐条收窄。
- 语料版本戳 = 语料最后一次改动的提交（先提交语料，再写 skill）；头部契约与诚实边界两处一致。
- 跨队 ID（NLP skill 引 `[DFO-R7]`）合法，脚本到对方语料解析；两队语料必须同在 `teams/` 下。
- 试答题写在 `teams/<team>/00-charter.md`「试答题（G6）」小节，四类各一（选型、陷阱、分寸、语料外）。

## 6. 完成后

- `teams/DISTILLATION_LOG.md` 顶部记一条：用户原话、档位、分支、产物、闸门结果（含每条 ⚠ 的处理）、
  G6 试答摘要 / G7 计数、运行教训、成本、执行模型。
- 语料线安装只复制 `teams/<team>/SKILL.md` 到 `~/.claude/skills/<team>/`；team-kit 产物按 `product/README.md`。
- 新研究者装进 `~/.claude/skills` 后，在 `~/.claude/settings.json` 的 `skillOverrides` 里给他加一行 `"name-only"`，
  只有入口（总入口、各队圆桌、理事会圆桌、语料团队）保留描述（`product/README.md` 安装一节）。
- 合入 main 后告知用户是否推送；不要自行 `git push`。
- README 一定要有英文版：中文的 `README.md` 旁边放 `README.en.md`，两份顶部互相链接（`[English](README.en.md) | 中文`、
  `English | [中文](README.md)`）；改其中一份时同一次提交里改另一份，内容、数字、链接保持一致。各队的 README 本来就是英文。
