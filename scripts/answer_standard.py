#!/usr/bin/env python3
"""Answer Standard：把 references/answer-standard.md 里的标准块写进各 SKILL.md，并核对是否一致。

标准的正文只有一份（references/answer-standard.md）。每个 SKILL.md 里的「Answer Standard / 回答标准」
一节夹在两行标记之间，由本脚本写入；要改措辞就改那份文件再跑 --apply，不要改标记之间的内容。

用法（从仓库根运行；Windows 用 python3 -X utf8）：
    python3 scripts/answer_standard.py --check [路径 …]      # 默认 product/ 与 teams/
    python3 scripts/answer_standard.py --apply [路径 …]      # 写入或刷新；已一致的文件不动
    python3 scripts/answer_standard.py --check --installed   # 另核对 ~/.claude/skills 里已安装的同名 skill
    python3 scripts/answer_standard.py --lint                # 只查标准块本身
    python3 scripts/answer_standard.py --words [路径 …]      # 字数预算的词数：不算这一节

路径可以是目录（递归找 SKILL.md）或某个 SKILL.md。退出码：有 ✗ 为 1，否则为 0。

字数预算不算这一节（2026-11-20 用户决定）：它由本脚本统一生成、各 skill 都一样，不是成员自己的内容。
T3.6（team-synthesize.js 的 word_budget / max_words）、T3.7（team-tighten.js）和 team_status.py 的 --max-words
都按 --words 的数比：每行先打印预算词数，再打印路径、总词数和这一节（连同两行标记）的词数。词数按空白切分，
与 wc -w 相同；标记缺一行或次序颠倒时这一节记 0，整篇都算。

skill 类型的判定与插入位置：
    type: research-craft          → research-craft 块，插在「## Research Integrity Rules」/「## 研究诚信规则」之前
    type: roundtable              → roundtable 块，插在「## Research Integrity Rules」之前
    type: lead                    → lead 块，插在「## Research Integrity Rules」之前
    teams/<team>/SKILL.md         → corpus-team 块，插在「## 框架概览」之前
其他 SKILL.md（没有 type、也不在 teams/ 下）跳过并注明。

研究者 skill 另有三处旧条款规定了回复的样子（逐条打方法标签、开场免责声明、Step 3 的固定格式）。
它们的内容仍然有效，只是位置变了，所以 --apply 在这三处各补一句「放在哪」，--check 核对这三句在不在：
    Step 3 标题下          → STEP3_FORM
    Activation Rules 里的标签条款（以 Label / Tag 开头的那一条）       → LABEL_PLACEMENT
    Activation Rules 里的免责声明条款（disclaimer / State once …）     → DISCLAIMER_PLACEMENT
没有对应条款的 skill（例如没有单独的标签条款）不算问题。

只用标准库。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STANDARD = REPO / "references" / "answer-standard.md"
DEFAULT_ROOTS = ["product", "teams"]

BEGIN = ("<!-- answer-standard:begin · written by scripts/answer_standard.py "
         "from references/answer-standard.md; edit that file, not this section -->")
END = "<!-- answer-standard:end -->"
BEGIN_RE = re.compile(r"^<!-- answer-standard:begin\b.*-->$", re.M)
END_RE = re.compile(r"^<!-- answer-standard:end -->$", re.M)
BLOCK_RE = re.compile(r"^<!-- block:(?P<kind>[a-z-]+) -->\n(?P<body>.*?)\n<!-- /block:(?P=kind) -->$", re.M | re.S)

ANCHORS = {
    "research-craft": re.compile(r"^## (?:Research Integrity Rules|研究诚信规则)\b.*$", re.M),
    "roundtable": re.compile(r"^## (?:Research Integrity Rules|研究诚信规则)\b.*$", re.M),
    "lead": re.compile(r"^## (?:Research Integrity Rules|研究诚信规则)\b.*$", re.M),
    "corpus-team": re.compile(r"^## 框架概览\b.*$", re.M),
}

# 研究者 skill 里三处旧条款的「放在哪」。
STEP3_FORM = ("Form and order: the Answer Standard above. The text below lists what the reply must contain; "
              "the methods behind the steps are credited in the Basis footer, in words, rather than tagged inline; "
              "the workflow's name is not printed; and 🔴 is this file's mark for a workflow checkpoint, "
              "never printed in the reply.")
LABEL_PLACEMENT = ("In the reply these attributions go in the Basis footer, in words and keyed to the numbered "
                   "recommendations, not inline in the prose (Answer Standard).")
DISCLAIMER_PLACEMENT = ("In the reply it is one sentence in the Basis footer, not an opening paragraph "
                        "(Answer Standard).")
# 旧版措辞：--apply 遇到就换成当前版本，--check 遇到算「缺」。改了上面三句时把旧句挪到这里。
SUPERSEDED = {
    "step3": [
        "Form and order: the Answer Standard above. The text below lists what the reply must contain; "
        "the methods behind the steps go in the Basis footer rather than inline, and 🔴 is this file's "
        "mark for a workflow checkpoint, never printed in the reply.",
    ],
    "label": [
        "In the reply these attributions go in the Basis footer, keyed to the numbered "
        "recommendations, not inline in the prose (Answer Standard).",
    ],
    "disclaimer": [],
}
STEP3_RE = re.compile(r"^### Step 3\b.*$", re.M)
ACTIVATION_RE = re.compile(r"^## (?:Activation Rules|激活规则)\b.*$", re.M)
NEXT_H2_RE = re.compile(r"^## ", re.M)
LABEL_BULLET_RE = re.compile(  # 以 Label / Tag 开头，或句中「tag key advice / each key recommendation with its method」
    r"^- (?:\*{0,2}(?:Label|Tag)\b|.*\b(?:[Ll]abel|[Tt]ag) (?:each |every )?(?:key )?"
    r"(?:recommendation|advice|suggestion)s?\b.*\bmethod)")
DISCLAIMER_BULLET_RE = re.compile(
    r"^- \*{0,2}(?:One-time disclaimer|Disclaimer once|State once|Say once|Once, on first activation|"
    r"On first activation|At first activation)\b")

# 标准块里不许出现的东西：会被 check_citations.py / distill_check.py / check_links.py 当真去核对。
LINT_RULES = [
    ("card-key", re.compile(r"\[[A-Z]{1,2}\d{2,4}\b"), "像卡片引用键（[S012 …]）"),
    ("corpus-id", re.compile(r"\[(?:DFO|NLP|LP|MINLP|MILP)-[SRL]\d+"), "像语料 ID（[NLP-R4]）"),
    ("doi", re.compile(r"\b10\.\d{4,9}/"), "像 DOI"),
    ("arxiv", re.compile(r"(?<![\d.])\d{4}\.\d{4,5}\b"), "像 arXiv 号"),
    ("year", re.compile(r"(?<![\d.])(?:19|20)\d{2}(?![\d.])"), "年份（会和作者名凑成作者-年份对）"),
    ("link", re.compile(r"\]\((?!https?://)[^)]+\)"), "相对链接"),
]


def out(line: str = "") -> None:
    print(line)


def load_blocks() -> dict[str, str]:
    if not STANDARD.exists():
        sys.exit(f"✗ 找不到 {STANDARD.relative_to(REPO)}")
    text = STANDARD.read_text(encoding="utf-8").replace("\r\n", "\n")
    blocks = {m.group("kind"): m.group("body").strip("\n") for m in BLOCK_RE.finditer(text)}
    missing = [k for k in ANCHORS if k not in blocks]
    if missing:
        sys.exit(f"✗ {STANDARD.relative_to(REPO)} 缺少标准块：{', '.join(missing)}")
    return blocks


def lint_blocks(blocks: dict[str, str]) -> int:
    problems = 0
    texts = dict(blocks)
    texts["placement"] = "\n".join([STEP3_FORM, LABEL_PLACEMENT, DISCLAIMER_PLACEMENT])
    for kind, body in texts.items():
        for n, line in enumerate(body.split("\n"), 1):
            for name, rx, why in LINT_RULES:
                m = rx.search(line)
                if m:
                    problems += 1
                    out(f"  ✗ lint {kind} 第 {n} 行 [{name}] {why}：{m.group(0)!r}")
        if kind != "placement" and not body.startswith("## "):
            problems += 1
            out(f"  ✗ lint {kind}：块必须以二级标题开头")
    if not problems:
        out(f"  ✓ lint  标准块 {len(blocks)} 个，无引用样记号、无相对链接")
    return problems


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def skill_kind(path: Path, text: str) -> str | None:
    m = re.search(r"^type:\s*(\S+)\s*$", frontmatter(text), re.M)
    if m:
        return m.group(1) if m.group(1) in ANCHORS else None
    parts = path.resolve().parts
    if len(parts) >= 3 and parts[-3] == "teams":
        return "corpus-team"
    return None


def find_targets(paths: list[str]) -> list[Path]:
    found: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if not p.is_absolute():
            p = REPO / p
        if p.is_file():
            found.append(p)
        elif p.is_dir():
            found.extend(sorted(q for q in p.rglob("SKILL.md") if ".claude" not in q.parts))
        else:
            out(f"  ✗ 路径不存在：{raw}")
    return found


def rendered(body: str) -> str:
    return f"{BEGIN}\n{body}\n{END}"


def current_block(text: str) -> str | None:
    b, e = BEGIN_RE.search(text), END_RE.search(text)
    if not b or not e or e.start() < b.end():
        return None
    return text[b.end():e.start()].strip("\n")


def word_counts(text: str) -> tuple[int, int]:
    """(总词数, 这一节连同两行标记的词数)。按空白切分，与 wc -w 相同；标记不成对时这一节记 0。"""
    text = text.replace("\r\n", "\n")
    total = len(text.split())
    b, e = BEGIN_RE.search(text), END_RE.search(text)
    if not b or not e or e.start() < b.end():
        return total, 0
    return total, len(text[b.start():e.end()].split())


def budget_words(text: str) -> int:
    """字数预算算的词数：这一节之外的部分（T3.6、T3.7 与 team_status.py 的 --max-words 都用它）。"""
    total, block = word_counts(text)
    return total - block


def apply_block(text: str, kind: str, body: str) -> tuple[str | None, str]:
    """返回 (新文本或 None, 状态)。文本已规范成 \\n。"""
    b, e = BEGIN_RE.search(text), END_RE.search(text)
    if bool(b) != bool(e) or (b and e and e.start() < b.end()):
        return None, "标记不成对"
    if b and e:
        if text[b.end():e.start()].strip("\n") == body:
            return text, "一致"
        return text[:b.start()] + rendered(body) + text[e.end():], "已刷新"
    a = ANCHORS[kind].search(text)
    if not a:
        return None, f"找不到插入位置（{ANCHORS[kind].pattern}）"
    return text[:a.start()] + rendered(body) + "\n\n" + text[a.start():], "已写入"


def activation_span(lines: list[str]) -> tuple[int, int]:
    """Activation Rules 一节的行号区间 [start, end)；没有这一节则 (0, 0)。"""
    start = next((i for i, l in enumerate(lines) if ACTIVATION_RE.match(l)), None)
    if start is None:
        return 0, 0
    end = next((i for i in range(start + 1, len(lines)) if NEXT_H2_RE.match(lines[i])), len(lines))
    return start, end


def placement_sites(lines: list[str]) -> dict[str, int | None]:
    """三处旧条款各自所在的行号（没有则 None）。标准块内部的行不算。"""
    inside = False
    skip: set[int] = set()
    for i, l in enumerate(lines):
        if BEGIN_RE.match(l):
            inside = True
        if inside:
            skip.add(i)
        if END_RE.match(l):
            inside = False
    a0, a1 = activation_span(lines)
    sites: dict[str, int | None] = {"step3": None, "label": None, "disclaimer": None}
    for i, l in enumerate(lines):
        if i in skip:
            continue
        if sites["step3"] is None and STEP3_RE.match(l):
            sites["step3"] = i
        if a0 <= i < a1:
            if sites["label"] is None and LABEL_BULLET_RE.match(l):
                sites["label"] = i
            if sites["disclaimer"] is None and DISCLAIMER_BULLET_RE.match(l):
                sites["disclaimer"] = i
    return sites


def placement_state(lines: list[str]) -> dict[str, bool | None]:
    """每处：True 已有「放在哪」/ False 缺 / None 该 skill 没有这条旧条款。"""
    sites = placement_sites(lines)
    state: dict[str, bool | None] = {}
    s3 = sites["step3"]
    if s3 is None:
        state["step3"] = None
    else:
        nxt = next((l for l in lines[s3 + 1:] if l.strip()), "")
        state["step3"] = nxt.strip() == STEP3_FORM
    for key, sentence in (("label", LABEL_PLACEMENT), ("disclaimer", DISCLAIMER_PLACEMENT)):
        i = sites[key]
        state[key] = None if i is None else lines[i].rstrip().endswith(sentence)
    return state


def apply_placements(text: str) -> tuple[str, list[str]]:
    lines = text.split("\n")
    done: list[str] = []
    state = placement_state(lines)
    sites = placement_sites(lines)
    for key, sentence in (("label", LABEL_PLACEMENT), ("disclaimer", DISCLAIMER_PLACEMENT)):
        if state[key] is False:
            i = sites[key]
            line = lines[i].rstrip()
            for old in SUPERSEDED[key]:          # 旧版措辞先去掉，再补当前版本
                if line.endswith(old):
                    line = line[:-len(old)].rstrip()
            lines[i] = line + " " + sentence
            done.append(key)
    if state["step3"] is False:
        i = sites["step3"]
        j = next((k for k in range(i + 1, len(lines)) if lines[k].strip()), None)
        if j is not None and lines[j].strip() in SUPERSEDED["step3"]:
            lines[j] = STEP3_FORM                   # 旧版那一行原地替换
        else:
            lines[i + 1:i + 1] = [STEP3_FORM, ""]   # 标题下紧跟一行，再空一行接原文
        done.append("step3")
    return "\n".join(lines), done


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO).as_posix()
    except ValueError:
        return str(path)


def process(path: Path, blocks: dict[str, str], write: bool, kind: str | None = None) -> tuple[str, str]:
    """返回 (标记, 说明)；标记 ∈ ✓ ✗ —。kind 给定时不再从路径判定（已安装的副本用仓库源文件的类型）。"""
    raw = path.read_bytes().decode("utf-8")
    crlf = "\r\n" in raw
    text = raw.replace("\r\n", "\n")
    kind = kind or skill_kind(path, text)
    if kind is None:
        return "—", "跳过（没有可识别的 type，也不在 teams/ 下）"
    body = blocks[kind]
    if not write:
        cur = current_block(text)
        if cur is None:
            return "✗", f"{kind}：缺少 Answer Standard 一节（跑 --apply）"
        if cur != body:
            return "✗", f"{kind}：与 references/answer-standard.md 不一致（跑 --apply）"
        if kind == "research-craft":
            missing = [k for k, v in placement_state(text.split("\n")).items() if v is False]
            if missing:
                return "✗", f"{kind}：旧条款缺「放在哪」一句（{', '.join(missing)}；跑 --apply）"
        return "✓", f"{kind}：一致"
    new, status = apply_block(text, kind, body)
    if new is None:
        return "✗", f"{kind}：{status}"
    notes = [status]
    if kind == "research-craft":
        new, done = apply_placements(new)
        if done:
            notes.append("补位置说明 " + "+".join(done))
    if new != text:
        path.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return "✓", f"{kind}：{'；'.join(notes)}"


def installed_copies(targets: list[Path]) -> list[tuple[Path, str]]:
    """(已安装的 SKILL.md, 仓库源文件的类型)。安装目录名 = 仓库里 skill 所在目录名。"""
    home = Path.home() / ".claude" / "skills"
    pairs = []
    for t in targets:
        inst = home / t.parent.name / "SKILL.md"
        kind = skill_kind(t, t.read_bytes().decode("utf-8").replace("\r\n", "\n"))
        if inst.exists() and kind:
            pairs.append((inst, kind))
    return pairs


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description="写入 / 核对各 SKILL.md 的 Answer Standard 一节")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="核对，不改文件")
    mode.add_argument("--apply", action="store_true", help="写入或刷新")
    mode.add_argument("--lint", action="store_true", help="只查标准块本身")
    mode.add_argument("--words", action="store_true",
                      help="只数词：每个 SKILL.md 打印字数预算算的词数（不算这一节）、总词数和这一节的词数")
    ap.add_argument("--installed", action="store_true",
                    help="--check 时另核对 ~/.claude/skills 里已安装的同名 skill 是否带同一份标准块")
    ap.add_argument("paths", nargs="*", help="目录或 SKILL.md；默认 product/ 与 teams/")
    args = ap.parse_args()

    if args.words:
        missing = [raw for raw in args.paths if not (Path(raw) if Path(raw).is_absolute() else REPO / raw).exists()]
        for path in find_targets(args.paths or DEFAULT_ROOTS):
            total, block = word_counts(path.read_text(encoding="utf-8"))
            out(f"{total - block}  {rel(path)}  （总 {total} 词，其中 Answer Standard 一节 {block} 词）")
        return 1 if missing else 0

    blocks = load_blocks()
    out(f"Answer Standard · {STANDARD.relative_to(REPO).as_posix()}")
    bad = lint_blocks(blocks)
    if args.lint:
        return 1 if bad else 0
    if bad and args.apply:
        out("  标准块没过 lint，未写入任何文件")
        return 1

    targets = find_targets(args.paths or DEFAULT_ROOTS)
    counts = {"✓": 0, "✗": 0, "—": 0}
    for path in targets:
        mark, note = process(path, blocks, write=args.apply)
        counts[mark] += 1
        out(f"  {mark} {rel(path)}  {note}")
    if args.check and args.installed:
        out("已安装（~/.claude/skills）")
        for inst, kind in installed_copies(targets):
            mark, note = process(inst, blocks, write=False, kind=kind)
            counts[mark] += 1
            out(f"  {mark} {inst.parent.name}  {note}")
    out(f"合计：✓ {counts['✓']} · ✗ {counts['✗'] + bad} · 跳过 {counts['—']}")
    return 1 if (counts["✗"] or bad) else 0


if __name__ == "__main__":
    sys.exit(main())
