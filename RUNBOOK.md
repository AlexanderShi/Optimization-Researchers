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
- 改了 `works.json` 的标题，PDF / txt 的文件名 slug 跟着变：按 `acquire_fulltexts.slug(row)` 给本地文件改名，
  否则报 "rows keep their committed txt/pdf status without a local file"。
- 1990–2000 年代的作者 PDF 常有「正文完好、数字和希腊字母全丢」的文字层：`acquire_fulltexts.py` 自动判定并 OCR
  （tesseract 在 PATH 时）；之前抓的用 `--reocr ID,…` + `plan_reading_batches.py --reread`。按 txt 的数字占比排序能找出来。
- 混合档团队加轻量档成员：`team-layer.js` 用 `deep_tier: true`（`false` 会把 DEEP-READING 整个换掉）；之后手工删
  "(card evidence pending for <slug>)"、按 `team_status.py --coverage`（及 `--short`）重贴两张表、改成员计数。
- 调研笔记里的 MATLAB 版本号（R2015b）会被 `check_citations.py` 当作作品 ID：写成行内代码。
- 读的是替代版本（报告版、预印本、后一版手册）就写版本引用 `[S025 TR pp. 3–12]`，卡片正文写明。
- 审计包必须给整张卡片（曾因截到 9,000 字符误判 unsupported）；同样深的卡片取最晚一轮（OCR 重读后的）。
- 写 skill 的 agent 与审计 / 复核的 agent 必须是两个；每条声明两位审计员、有分歧第三位裁定更稳。

## 5. 语料流水线（DISTILL.md）

- 改语料前后都跑 `python3 -X utf8 scripts/distill_check.py teams/<team> --lint`；填完模板跑全量；装完跑 `--installed`。
- G7：`scripts/distill_audit.py --sample` → 新 agent 只读审计包 `.md` → `--report`；unsupported = 0，partial 逐条收窄。
- 语料版本戳 = 语料最后一次改动的提交（先提交语料，再写 skill）；头部契约与诚实边界两处一致。
- 跨队 ID（NLP skill 引 `[DFO-R7]`）合法，脚本到对方语料解析；两队语料必须同在 `teams/` 下。
- 试答题写在 `teams/<team>/00-charter.md`「试答题（G6）」小节，四类各一（选型、陷阱、分寸、语料外）。

## 6. 完成后

- `teams/DISTILLATION_LOG.md` 顶部记一条：用户原话、档位、分支、产物、闸门结果（含每条 ⚠ 的处理）、
  G6 试答摘要 / G7 计数、运行教训、成本、执行模型。
- 语料线安装只复制 `teams/<team>/SKILL.md` 到 `~/.claude/skills/<team>/`；team-kit 产物按 `product/README.md`。
- 合入 main 后告知用户是否推送；不要自行 `git push`。
