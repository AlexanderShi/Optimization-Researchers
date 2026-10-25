#!/usr/bin/env python3
"""
语料流水线（DISTILL.md）的确定性质量门：把 Phase 4 的 G1–G6 里能机械判定的部分、语料自身的结构检查（lint）、
语料版本戳与安装漂移一次跑完。此前「语料 → 团队级 skill」这条线只有人工核对，没有任何脚本闸门
（team-kit 那条线有 check_citations.py / audit_claims.py）；本脚本是它们在语料侧的对应物。

用法:
    python3 scripts/distill_check.py teams/<team>              # 语料 lint + SKILL.md 的 G1–G6 机械部分 + 版本戳
    python3 scripts/distill_check.py teams                     # 所有带 01-canon.md 的团队
    python3 scripts/distill_check.py teams/<team> --lint       # 只查语料（蒸馏前 / 改语料后）
    python3 scripts/distill_check.py teams/<team> --installed  # 另比对 ~/.claude/skills/<name>/SKILL.md 是否与仓库一致
    python3 scripts/distill_check.py teams/<team> --no-git     # 不做 git 版本戳检查
    python3 scripts/distill_check.py teams/<team> --strict-stale   # 语料在版本戳之后有改动时判 ✗ 而不是 ⚠
    python3 scripts/distill_check.py teams/<team> --json

检查（✗ 计入退出码 1；⚠ 要人看一眼；i 只是信息）:
  lint（语料本身；G1 的前提是这张 ID 表）
    no-prefix       01-canon 里没有 `| PREFIX-S1 |` 这样的行，定不了团队前缀
    dup-def         01 的 S/L、04 的 R、03 的 H、05 的 F 重复定义
    tier            01-canon 的文献行不在任何验证层级小节下（verified-local / model-knowledge / verified-web / 本地工件 / 档案）
    result-fields   04 每个 `## PREFIX-R*` 小节：缺 **结论** / **状态** ✗；缺 **假设** / **层级** ⚠；
                    状态行不含 proved / cited / verified ✗（proved-vs-cited 在语料侧就得有）
    schools         02-schools 缺「共识」或「分歧」小节 ⚠（Phase 1 的共识/分歧表靠它）
    unknown-id      00–05 与 researchers/ 里引用了不存在的 ID（跨队 ID 到对方语料里解析）
    unknown-prefix  引用的前缀不是任何团队的
    bare-id         方括号里只有 S23 这样的裸 ID、同组没有带前缀的 ID，按本队前缀解析 ⚠
    researcher      researchers/*.md 没提「三重验证」⚠（standards/researcher-extraction.md 第 5 节）
  G1 语料封闭（SKILL.md）
    unknown-id / unknown-prefix / bare-id   同上
    unknown-label   [H7]、**F3** 这类标签在 03 / 05 里不存在 ⚠
    no-id           承重部分（框架概览 / 流派对比 / 决策启发式 / 绝不做）里没有任何 ID 或 H/F 标签的条目 ⚠
    description     frontmatter description 超过 300 字（不计空白）⚠
  G2 引用闭包
    author-year     SKILL.md 里的（作者, 年份）在本队 01-canon 里找不到同时含该年份与全部姓氏的行：
                    部分姓氏命中 ⚠；只在别队 canon 命中 ⚠；都没有 ✗
  G3 数学纪律
    result-row      关键结果速查每行：ID 列不是 R ID ✗；假设列空 ✗、只有 — ⚠；状态列不含 proved / cited / verified ✗；
                    整行没有任何 S/L 来源 ID ⚠
    number          承重部分里出现了语料中不存在的数字（≥2 位或带小数点；年份不算）⚠——精确常数只能来自语料
  G4 诚实边界
    boundary        缺 YYYY-MM-DD 日期 / 语料版本 hash / 「语料缺口」/ 「验证层级」✗；头部语料契约与诚实边界的 hash 不一致 ✗
    stamp           语料版本 hash 不是本仓库的提交 ✗；不在当前 HEAD 的历史上（历史被重写？）⚠ 并给出同树的等价提交；
                    自该提交以来 teams/<team>/ 的语料文件有改动（SKILL.md、CLAIM-AUDIT.md 除外）⚠ = skill 过期
                    （--strict-stale 时 ✗）；工作区有未提交的语料改动 ⚠
  G5 禁区完整性 / 逐条移植
    missing-F       05 的 F* 没出现在「绝不做」✗          missing-R   04 的 R* 没出现在「关键结果速查」✗
    missing-H       03 的 H* 没出现在「决策启发式」✗       unused-S    01 的 S/L ID 在 SKILL.md 里一次没出现 ⚠
    researcher      researchers/<name>.md 在 SKILL.md 里没被提到 ⚠
  G6 试答
    probes          00-charter.md 的「试答题」小节：没有 ⚠（退回 DISTILL.md 的默认题）；少于 3 题 ✗；
                    某题没写应命中的 ID / 标签（语料外题除外）✗；没有「语料外」题 ⚠
  install（--installed）
    installed       ~/.claude/skills/<frontmatter name>/SKILL.md 不存在或与仓库不一致 ⚠

ID 写法（与 standards/grounding.md 一致）：[DFO-S4]、[NLP-R2]、[DFO-L1]；同一方括号里可省前缀 [DFO-S21, S23]、
[NLP-R4 vs R2]；区间 [NLP-S19–S23]；ID 后可跟说明 [DFO-S4 content]、[NLP-S1 机器区]。方括号外只认完整 ID
（表格首列、04 的标题、正文里的 DFO-R11）。启发式与禁区用 H1… / F1… 标签。
不扫描：front matter（description 除外）、围栏代码块、行内代码。

退出码：有 ✗ → 1；路径不是团队目录 → 2。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

CORPUS_FILES = ["00-charter.md", "01-canon.md", "02-schools.md", "03-heuristics.md", "04-results.md",
                "05-failure-modes.md"]
PRODUCT_FILES = {"SKILL.md", "CLAIM-AUDIT.md"}
SECTION_KEYS = {"workflow": "回答工作流", "overview": "框架概览", "schools": "流派对比", "heuristics": "决策启发式",
                "results": "关键结果速查", "never": "绝不做", "boundary": "诚实边界", "sources": "来源索引"}
LOAD_BEARING = ["overview", "schools", "heuristics", "never"]  # results 由 G3 按表格结构查
TIER_WORDS = ("verified-local", "model-knowledge", "verified-web", "本地", "工件", "研究者", "档案")
DEFAULT_PROBES = 3

FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
ATX_RE = re.compile(r"^ {0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
CODE_SPAN_RE = re.compile(r"(`+)(?!`).*?(?<!`)\1(?!`)")
BRACKET_RE = re.compile(r"\[([^\[\]]*)\]")
FULL_ID_RE = re.compile(r"(?<![A-Za-z0-9_-])(?P<prefix>[A-Z]{2,6})-(?P<kind>[SRL])(?P<num>\d{1,3})(?![0-9A-Za-z])")
# 方括号里的一个记号：区间 | 完整 ID | 裸 ID | H/F 标签（顺序即优先级）
TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9_-])(?:"
    r"(?:(?P<rp>[A-Z]{2,6})-)?(?P<rk>[SRL])(?P<ra>\d{1,3})\s*[–—-]\s*(?:[SRL])?(?P<rb>\d{1,3})"
    r"|(?P<fp>[A-Z]{2,6})-(?P<fk>[SRL])(?P<fn>\d{1,3})"
    r"|(?P<bk>[SRL])(?P<bn>\d{1,3})"
    r"|(?P<lk>[HF])(?P<ln>\d{1,2})"
    r")(?![0-9A-Za-z])")
BOLD_LABEL_RE = re.compile(r"\*\*(?P<kind>[HF])(?P<num>\d{1,2})(?![0-9A-Za-z])[^*\n]*\*\*")
LABEL_WORD_RE = r"(?<![A-Za-z0-9_-]){kind}{num}(?![0-9A-Za-z])"
ITEM_START_RE = re.compile(r"^\s{0,3}(?:[-*+]|\d{1,3}[.)])\s+")
TABLE_ROW_RE = re.compile(r"^\s*\|")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}")
CANON_ROW_RE = re.compile(r"^\s*\|\s*(?P<prefix>[A-Z]{2,6})-(?P<kind>[SL])(?P<num>\d{1,3})\s*\|")
RESULT_HEAD_RE = re.compile(r"^##\s+(?P<prefix>[A-Z]{2,6})-R(?P<num>\d{1,3})(?![0-9A-Za-z])")
LABEL_HEAD_RE = re.compile(r"^##\s+(?P<kind>[HF])(?P<num>\d{1,2})(?![0-9A-Za-z])")
HASH_RE = re.compile(r"(?<![0-9a-zA-Z])[0-9a-f]{7,40}(?![0-9a-zA-Z])")
DATE_RE = re.compile(r"(?<!\d)\d{4}-\d{2}-\d{2}(?!\d)")
AUTHOR_YEAR_RE = re.compile(
    r"(?<![A-Za-zÀ-ɏ])(?P<names>[A-Z][A-Za-zÀ-ɏ'’]+(?:[-–][A-Z][A-Za-zÀ-ɏ'’]+)*)"
    r"(?:\s*(?:等|et al\.?))?\s*\(?(?P<year>(?:18|19|20)\d{2})[a-z]?\)?(?![0-9])")
NUM_RE = re.compile(r"(?<![A-Za-z0-9_./:-])(?:\d+\.\d+|\d{2,})(?![0-9A-Za-z/.])")
YEAR_RE = re.compile(r"^(?:18|19|20)\d{2}$")
URLISH_RE = re.compile(r"\S*(?:https?://|doi\.org|arxiv|arXiv|\.html?|\.md|\.json|\.py)\S*")
PROVED_RE = re.compile(r"proved|cited|verified", re.I)


# ---------------------------------------------------------------- 文本工具


def fold(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()


def prose_lines(text: str) -> list[str]:
    """按行返回正文：front matter 与围栏代码块换成空行、行内代码换成空格（行号不变）。"""
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    if lines and lines[0].strip() == "---":
        j = 1
        while j < len(lines) and lines[j].strip() not in ("---", "..."):
            j += 1
        out = [""] * (j + 1)
        i = j + 1
    fence = None
    for line in lines[i:]:
        if fence:
            s = line.strip()
            if s and set(s) == {fence[0]} and len(s) >= len(fence):
                fence = None
            out.append("")
            continue
        m = FENCE_RE.match(line)
        if m:
            fence = m.group(1)
            out.append("")
        else:
            out.append(CODE_SPAN_RE.sub(lambda mm: " " * len(mm.group()), line))
    return out


def front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fm: dict[str, str] = {}
    key = None
    for line in lines[1:]:
        if line.strip() in ("---", "..."):
            break
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            fm[key] = "" if val in ("|", ">", "|-", ">-") else val
        elif key and line.startswith((" ", "\t")):
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm


@dataclass
class Section:
    title: str
    level: int
    start: int  # 标题行（0 基）
    end: int    # 不含


def sections(prose: list[str]) -> list[Section]:
    heads = [(i, len(m.group(1)), m.group(2)) for i, line in enumerate(prose) if (m := ATX_RE.match(line))]
    out = []
    for k, (i, lvl, title) in enumerate(heads):
        end = len(prose)
        for j, lvl2, _ in heads[k + 1:]:
            if lvl2 <= lvl:
                end = j
                break
        out.append(Section(title, lvl, i, end))
    return out


def find_section(secs: list[Section], key: str) -> Section | None:
    word = SECTION_KEYS.get(key, key)
    for s in secs:
        if s.level == 2 and word in s.title:
            return s
    return None


@dataclass
class Item:
    line: int   # 1 基
    text: str
    kind: str   # bullet | row | para


def items_in(prose: list[str], start: int, end: int) -> list[Item]:
    """把一段正文切成条目：列表项（含缩进续行）、表格行（去掉表头与分隔行）、段落（连续的非缩进行）。"""
    items: list[Item] = []
    cur: Item | None = None
    pending_row: Item | None = None

    def flush():
        nonlocal cur
        if cur:
            items.append(cur)
        cur = None

    for i in range(start, end):
        line = prose[i]
        if not line.strip() or ATX_RE.match(line):
            flush()
            if pending_row:
                items.append(pending_row)
                pending_row = None
            continue
        if TABLE_ROW_RE.match(line):
            flush()
            if TABLE_SEP_RE.match(line):
                pending_row = None  # 分隔行之前那一行是表头
                continue
            if pending_row:
                items.append(pending_row)
            pending_row = Item(i + 1, line.strip(), "row")
            continue
        if pending_row:
            items.append(pending_row)
            pending_row = None
        if ITEM_START_RE.match(line):
            flush()
            cur = Item(i + 1, line.strip(), "bullet")
        elif cur and (line.startswith((" ", "\t")) or cur.kind == "para"):
            cur.text += " " + line.strip()
        else:
            flush()
            cur = Item(i + 1, line.strip(), "para")
    flush()
    if pending_row:
        items.append(pending_row)
    return items


def table_rows(prose: list[str], start: int, end: int) -> tuple[list[str], list[tuple[int, list[str]]]]:
    """第一张表：表头单元格 + [(行号, 单元格列表)]。"""
    header: list[str] = []
    rows: list[tuple[int, list[str]]] = []
    seen_sep = False
    for i in range(start, end):
        line = prose[i]
        if not TABLE_ROW_RE.match(line):
            if rows:
                break
            continue
        if TABLE_SEP_RE.match(line):
            seen_sep = True
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not seen_sep and not header:
            header = cells
        elif seen_sep:
            rows.append((i + 1, cells))
    return header, rows


# ---------------------------------------------------------------- ID


@dataclass(frozen=True)
class Ref:
    prefix: str
    kind: str      # S R L
    num: int
    line: int
    bare: bool = False

    @property
    def id(self) -> str:
        return f"{self.prefix}-{self.kind}{self.num}"


@dataclass(frozen=True)
class Label:
    kind: str      # H F
    num: int
    line: int

    @property
    def id(self) -> str:
        return f"{self.kind}{self.num}"


def refs_in_line(line: str, lineno: int, default_prefix: str) -> tuple[list[Ref], list[Label]]:
    refs: list[Ref] = []
    labels: list[Label] = []
    spans: list[tuple[int, int]] = []
    for g in BRACKET_RE.finditer(line):
        spans.append((g.start(), g.end()))
        last_prefix: str | None = None
        for m in TOKEN_RE.finditer(g.group(1)):
            if m.group("rk"):
                pfx = m.group("rp") or last_prefix
                bare = pfx is None
                pfx = pfx or default_prefix
                last_prefix = pfx
                a, b = int(m.group("ra")), int(m.group("rb"))
                for n in range(min(a, b), max(a, b) + 1):
                    refs.append(Ref(pfx, m.group("rk"), n, lineno, bare))
            elif m.group("fk"):
                last_prefix = m.group("fp")
                refs.append(Ref(last_prefix, m.group("fk"), int(m.group("fn")), lineno))
            elif m.group("bk"):
                bare = last_prefix is None
                refs.append(Ref(last_prefix or default_prefix, m.group("bk"), int(m.group("bn")), lineno, bare))
            elif m.group("lk"):
                labels.append(Label(m.group("lk"), int(m.group("ln")), lineno))
    for m in FULL_ID_RE.finditer(line):
        if any(a <= m.start() < b for a, b in spans):
            continue
        refs.append(Ref(m.group("prefix"), m.group("kind"), int(m.group("num")), lineno))
    for m in BOLD_LABEL_RE.finditer(line):
        labels.append(Label(m.group("kind"), int(m.group("num")), lineno))
    return refs, labels


def refs_in_text(text: str, default_prefix: str, first_line: int = 1) -> tuple[list[Ref], list[Label]]:
    refs, labels = [], []
    for k, line in enumerate(text.splitlines() or [text]):
        r, l = refs_in_line(line, first_line + k, default_prefix)
        refs += r
        labels += l
    return refs, labels


@dataclass
class Def:
    kind: str
    num: int
    file: str
    line: int
    text: str
    tier: str = ""

    @property
    def id(self) -> str:
        return f"{self.kind}{self.num}"


@dataclass
class Corpus:
    dir: Path
    slug: str
    files: dict[str, str] = field(default_factory=dict)       # 相对名 → 原文
    prose: dict[str, list[str]] = field(default_factory=dict)  # 相对名 → 正文行
    prefix: str = ""
    defs: dict[str, dict[int, Def]] = field(default_factory=lambda: {"S": {}, "L": {}, "R": {}, "H": {}, "F": {}})
    dups: list[tuple[str, str, int]] = field(default_factory=list)   # (id, file, line)
    numbers: set[str] = field(default_factory=set)
    canon_lines: list[str] = field(default_factory=list)   # 折叠后的 01-canon 行

    @property
    def researchers(self) -> list[str]:
        return [f for f in self.files if f.startswith("researchers/")]

    @property
    def skill(self) -> str | None:
        return self.files.get("SKILL.md")

    def define(self, kind: str, num: int, d: Def):
        if num in self.defs[kind]:
            self.dups.append((f"{self.prefix}-{kind}{num}" if kind in "SRL" else f"{kind}{num}", d.file, d.line))
        else:
            self.defs[kind][num] = d

    def lookup(self, kind: str, num: int) -> Def | None:
        return self.defs.get(kind, {}).get(num)


def load_corpus(team_dir: Path) -> Corpus:
    c = Corpus(team_dir, team_dir.name)
    names = [f for f in CORPUS_FILES if (team_dir / f).exists()]
    rdir = team_dir / "researchers"
    if rdir.is_dir():
        names += [f"researchers/{p.name}" for p in sorted(rdir.glob("*.md"))]
    for f in names + [p for p in ("SKILL.md",) if (team_dir / p).exists()]:
        text = (team_dir / f).read_text(encoding="utf-8", errors="replace")
        c.files[f] = text
        c.prose[f] = prose_lines(text)
    # 前缀：01-canon 文献行里最常见的
    canon = c.prose.get("01-canon.md", [])
    prefixes = Counter(m.group("prefix") for line in canon if (m := CANON_ROW_RE.match(line)))
    c.prefix = prefixes.most_common(1)[0][0] if prefixes else ""
    c.canon_lines = [fold(line) for line in canon]
    # 定义
    tier = ""
    for i, line in enumerate(canon):
        if (h := ATX_RE.match(line)):
            tier = h.group(2)
        m = CANON_ROW_RE.match(line)
        if m and m.group("prefix") == c.prefix:
            c.define(m.group("kind"), int(m.group("num")), Def(m.group("kind"), int(m.group("num")), "01-canon.md",
                                                               i + 1, line.strip(), tier))
    res = c.prose.get("04-results.md", [])
    for s in sections(res):
        m = RESULT_HEAD_RE.match(res[s.start])
        if m and m.group("prefix") == c.prefix:
            body = "\n".join(res[s.start:s.end]).strip()
            c.define("R", int(m.group("num")), Def("R", int(m.group("num")), "04-results.md", s.start + 1, body))
    for fname, kind in (("03-heuristics.md", "H"), ("05-failure-modes.md", "F")):
        pl = c.prose.get(fname, [])
        for s in sections(pl):
            m = LABEL_HEAD_RE.match(pl[s.start])
            if m and m.group("kind") == kind:
                body = "\n".join(pl[s.start:s.end]).strip()
                c.define(kind, int(m.group("num")), Def(kind, int(m.group("num")), fname, s.start + 1, body))
    # 语料里出现过的数字（G3 用）
    for f, pl in c.prose.items():
        if f in PRODUCT_FILES:
            continue
        for line in pl:
            c.numbers.update(NUM_RE.findall(URLISH_RE.sub(" ", line)))
    return c


class Registry:
    def __init__(self, teams_root: Path):
        self.root = teams_root
        self.by_slug: dict[str, Corpus] = {}
        self.by_prefix: dict[str, Corpus] = {}
        for d in sorted(p for p in teams_root.iterdir() if p.is_dir() and (p / "01-canon.md").exists()):
            c = load_corpus(d)
            self.by_slug[c.slug] = c
            if c.prefix:
                self.by_prefix.setdefault(c.prefix, c)

    def resolve(self, ref: Ref) -> tuple[Corpus | None, Def | None]:
        c = self.by_prefix.get(ref.prefix)
        if not c:
            return None, None
        return c, c.lookup(ref.kind, ref.num)


# ---------------------------------------------------------------- 报告


class Report:
    GATES = ["lint", "G1", "G2", "G3", "G4", "G5", "G6", "install"]

    def __init__(self):
        self.rows: list[dict] = []

    def add(self, team: str, gate: str, code: str, status: str, where: str, detail: str):
        self.rows.append({"team": team, "gate": gate, "code": code, "status": status, "where": where, "detail": detail})

    def fail(self, *a):
        self.add(*a[:3], "fail", *a[3:])

    def warn(self, *a):
        self.add(*a[:3], "warn", *a[3:])

    def info(self, *a):
        self.add(*a[:3], "info", *a[3:])

    def count(self, team: str, gate: str, status: str) -> int:
        return sum(1 for r in self.rows if r["team"] == team and r["gate"] == gate and r["status"] == status)

    @property
    def failed(self) -> list[dict]:
        return [r for r in self.rows if r["status"] == "fail"]


# ---------------------------------------------------------------- 检查


def git(root: Path, *args: str) -> tuple[int, str]:
    env = {**os.environ, "PYTHONUTF8": "1"}
    try:
        p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, env=env)
    except OSError as e:
        return 127, str(e)
    return p.returncode, (p.stdout or b"").decode("utf-8", "replace").strip()


def check_lint(c: Corpus, reg: Registry, rep: Report):
    t = c.slug
    missing = [f for f in CORPUS_FILES if f not in c.files]
    if missing:
        rep.fail(t, "lint", "missing-file", c.slug, "语料缺文件: " + ", ".join(missing))
    if not c.prefix:
        rep.fail(t, "lint", "no-prefix", "01-canon.md", "找不到 `| PREFIX-S1 |` 形式的文献行，无法确定团队前缀")
        return
    for cid, f, line in c.dups:
        rep.fail(t, "lint", "dup-def", f"{f}:{line}", f"{cid} 重复定义")
    for d in c.defs["S"].values():
        if not any(w in d.tier for w in TIER_WORDS):
            rep.warn(t, "lint", "tier", f"01-canon.md:{d.line}", f"{c.prefix}-{d.id} 所在小节「{d.tier}」没有写验证层级")
    for d in c.defs["R"].values():
        where = f"04-results.md:{d.line}"
        rid = f"{c.prefix}-{d.id}"
        for fld, sev in (("结论", "fail"), ("状态", "fail"), ("假设", "warn"), ("层级", "warn")):
            if f"**{fld}**" not in d.text:
                getattr(rep, sev)(t, "lint", "result-fields", where, f"{rid} 缺 **{fld}**")
        status_lines = [l for l in d.text.splitlines() if "**状态**" in l]
        if status_lines and not any(PROVED_RE.search(l) for l in status_lines):
            rep.fail(t, "lint", "result-fields", where, f"{rid} 的状态行没有 proved / cited / verified")
    sch = c.prose.get("02-schools.md", [])
    titles = " ".join(s.title for s in sections(sch))
    for word in ("共识", "分歧"):
        if word not in titles:
            rep.warn(t, "lint", "schools", "02-schools.md", f"没有「{word}」小节")
    # 语料内引用闭包（定义处不算引用）
    for f, pl in c.prose.items():
        if f in PRODUCT_FILES:
            continue
        for i, line in enumerate(pl):
            if f == "01-canon.md" and CANON_ROW_RE.match(line):
                line = re.sub(CANON_ROW_RE, "| ", line, count=1)
            if f == "04-results.md" and RESULT_HEAD_RE.match(line):
                continue
            refs, labels = refs_in_line(line, i + 1, c.prefix)
            _closure(c, reg, rep, "lint", f, refs, labels)
    for f in c.researchers:
        if "三重验证" not in c.files[f]:
            rep.warn(t, "lint", "researcher", f, "档案没提「三重验证」（standards/researcher-extraction.md 第 5 节）")
    rep.info(t, "lint", "ids", c.slug,
             f"前缀 {c.prefix} · S {len(c.defs['S'])} · L {len(c.defs['L'])} · R {len(c.defs['R'])} · "
             f"H {len(c.defs['H'])} · F {len(c.defs['F'])} · 档案 {len(c.researchers)}")


def _closure(c: Corpus, reg: Registry, rep: Report, gate: str, f: str, refs: list[Ref], labels: list[Label]) -> int:
    """引用 → 定义。返回跨队引用数。"""
    cross = 0
    for r in refs:
        other, d = reg.resolve(r)
        where = f"{f}:{r.line}"
        if other is None:
            rep.fail(c.slug, gate, "unknown-prefix", where, f"{r.id}：没有前缀为 {r.prefix} 的团队")
            continue
        if d is None:
            rep.fail(c.slug, gate, "unknown-id", where, f"{r.id} 不存在" + ("" if other is c else f"（{other.slug} 语料里也没有）"))
            continue
        if other is not c:
            cross += 1
        if r.bare:
            rep.warn(c.slug, gate, "bare-id", where, f"裸 ID {r.kind}{r.num}，同组没有带前缀的 ID，按 {r.prefix} 解析")
    for l in labels:
        if c.lookup(l.kind, l.num) is None:
            hint = ("（skill 自有的启发式：只有 ✅三重验证通过的研究者心智模型可以这样升格，见 DISTILL.md Phase 2 规则 4；"
                    "否则补进 03-heuristics 再重蒸馏）" if l.kind == "H" else "")
            rep.warn(c.slug, gate, "unknown-label", f"{f}:{l.line}",
                     f"标签 {l.id} 在 {'03-heuristics' if l.kind == 'H' else '05-failure-modes'} 里不存在{hint}")
    return cross


def check_skill(c: Corpus, reg: Registry, rep: Report, repo: Path, use_git: bool, strict_stale: bool,
                show_pairs: bool = False) -> dict:
    t = c.slug
    text = c.skill or ""
    pl = c.prose["SKILL.md"]
    secs = sections(pl)
    fm = front_matter(text)
    meta = {"name": fm.get("name", ""), "stamp": "", "date": ""}

    # ---- G1
    desc_len = len(re.sub(r"\s+", "", fm.get("description", "")))
    if desc_len > 300:
        rep.warn(t, "G1", "description", "SKILL.md", f"frontmatter description {desc_len} 字（上限 300，不计空白）")
    all_refs: list[Ref] = []
    all_labels: list[Label] = []
    for i, line in enumerate(pl):
        r, l = refs_in_line(line, i + 1, c.prefix)
        all_refs += r
        all_labels += l
    cross = _closure(c, reg, rep, "G1", "SKILL.md", all_refs, all_labels)
    for key in LOAD_BEARING:
        s = find_section(secs, key)
        if not s:
            rep.fail(t, "G1", "section", "SKILL.md", f"缺「{SECTION_KEYS[key]}」小节")
            continue
        for it in items_in(pl, s.start + 1, s.end):
            refs, labels = refs_in_text(it.text, c.prefix, it.line)
            if refs or labels:
                continue
            if len(it.text) < 40 and it.text.rstrip().endswith(("：", ":")):
                continue  # 引导句
            rep.warn(t, "G1", "no-id", f"SKILL.md:{it.line}", f"[{SECTION_KEYS[key]}] 条目没有语料 ID / 标签：{it.text[:90]}")
    rep.info(t, "G1", "refs", "SKILL.md", f"{len(all_refs)} 条 ID 引用（跨队 {cross}）· {len(all_labels)} 条 H/F 标签 · "
             f"{len({r.id for r in all_refs})} 个不同 ID")

    # ---- G2
    seen: set[tuple[str, str]] = set()
    for i, line in enumerate(pl):
        for m in AUTHOR_YEAR_RE.finditer(URLISH_RE.sub(" ", line)):
            names, year = m.group("names"), m.group("year")
            if (names, year) in seen:
                continue
            seen.add((names, year))
            surnames = [fold(n) for n in re.split(r"[-–]", names) if len(n) >= 3]
            best = _author_hit(c, surnames, year)
            if show_pairs:
                rep.info(t, "G2", "pair", f"SKILL.md:{i + 1}", f"{names} {year} → {best}")
            if best == "all":
                continue
            where = f"SKILL.md:{i + 1}"
            if best == "some":
                rep.warn(t, "G2", "author-year", where, f"「{names} {year}」只有部分姓氏与年份同行出现在 01-canon")
                continue
            elsewhere = [o.slug for o in reg.by_slug.values() if o is not c and _author_hit(o, surnames, year) == "all"]
            if elsewhere:
                rep.warn(t, "G2", "author-year", where, f"「{names} {year}」不在本队 01-canon，只在 {', '.join(elsewhere)} 的 canon 里")
            else:
                rep.fail(t, "G2", "author-year", where, f"「{names} {year}」不在 01-canon.md（语料外引用）")
    rep.info(t, "G2", "pairs", "SKILL.md", f"{len(seen)} 个（作者, 年份）对")

    # ---- G3
    s = find_section(secs, "results")
    if s:
        header, rows = table_rows(pl, s.start + 1, s.end)
        col = {"id": 0, "assume": None, "status": None}
        for k, h in enumerate(header):
            if "假设" in h:
                col["assume"] = k
            elif "状态" in h or "层级" in h or "proved" in h:
                col["status"] = k
        if col["assume"] is None or col["status"] is None:
            rep.fail(t, "G3", "result-row", f"SKILL.md:{s.start + 1}", f"结果表表头缺「假设」或「状态」列：{header}")
        for line, cells in rows:
            where = f"SKILL.md:{line}"
            idm = FULL_ID_RE.fullmatch(cells[0].strip("* ")) if cells else None
            if not idm or idm.group("kind") != "R":
                rep.fail(t, "G3", "result-row", where, f"ID 列不是结果 ID：{cells[0] if cells else ''}")
            if col["assume"] is not None and col["assume"] < len(cells):
                a = cells[col["assume"]].strip()
                if not a:
                    rep.fail(t, "G3", "result-row", where, "假设列为空")
                elif a in ("—", "-", "–", "无"):
                    rep.warn(t, "G3", "result-row", where, f"假设列只有「{a}」（反例/工具类结果可接受，速率/定理不行）")
            if col["status"] is not None and col["status"] < len(cells) and not PROVED_RE.search(cells[col["status"]]):
                rep.fail(t, "G3", "result-row", where, f"状态列没有 proved / cited / verified：{cells[col['status']][:60]}")
            refs, _ = refs_in_text("|".join(cells), c.prefix, line)
            if not any(r.kind in "SL" for r in refs):
                rep.warn(t, "G3", "result-row", where, "整行没有任何 S/L 来源 ID")
        rep.info(t, "G3", "rows", "SKILL.md", f"结果表 {len(rows)} 行")
    else:
        rep.fail(t, "G3", "section", "SKILL.md", "缺「关键结果速查」小节")
    all_numbers = set(c.numbers)
    for o in reg.by_slug.values():
        all_numbers |= o.numbers
    for key in LOAD_BEARING + ["results"]:
        sec = find_section(secs, key)
        if not sec:
            continue
        for i in range(sec.start + 1, sec.end):
            clean = URLISH_RE.sub(" ", pl[i])
            clean = re.sub(r"[A-Z]{2,6}-[SRL]\d{1,3}", " ", clean)
            for n in NUM_RE.findall(clean):
                if YEAR_RE.match(n) or n in all_numbers:
                    continue
                rep.warn(t, "G3", "number", f"SKILL.md:{i + 1}", f"数字 {n} 在语料里没出现过（精确常数只能来自语料）")

    # ---- G4
    s = find_section(secs, "boundary")
    stamp = ""
    if not s:
        rep.fail(t, "G4", "boundary", "SKILL.md", "缺「诚实边界」小节")
    else:
        body = "\n".join(pl[s.start + 1:s.end])
        dates = DATE_RE.findall(body)
        if not dates:
            rep.fail(t, "G4", "boundary", f"SKILL.md:{s.start + 1}", "诚实边界没有 YYYY-MM-DD 日期")
        else:
            meta["date"] = dates[0]
        m = re.search(r"语料版本\s*[:：]?\s*([0-9a-f]{7,40})", body)
        if not m:
            rep.fail(t, "G4", "boundary", f"SKILL.md:{s.start + 1}", "诚实边界没有「语料版本 <hash>」")
        else:
            stamp = m.group(1)
        for word in ("语料缺口", "验证层级"):
            if word not in body:
                rep.fail(t, "G4", "boundary", f"SKILL.md:{s.start + 1}", f"诚实边界没有「{word}」")
    head = "\n".join(pl[:40])
    m = re.search(r"语料版本\s*[:：]?\s*([0-9a-f]{7,40})", head)
    if m and stamp and m.group(1) != stamp:
        rep.fail(t, "G4", "boundary", "SKILL.md", f"头部语料契约的版本 {m.group(1)} 与诚实边界的 {stamp} 不一致")
    elif not m and stamp:
        rep.warn(t, "G4", "boundary", "SKILL.md", "头部语料契约没有写语料版本")
    meta["stamp"] = stamp
    if stamp and use_git:
        _check_stamp(c, rep, repo, stamp, strict_stale)
    elif stamp:
        rep.info(t, "G4", "stamp", "SKILL.md", f"语料版本 {stamp}（--no-git，未核对）")

    # ---- G5
    def covered(key: str, pattern: str) -> bool | None:
        sec = find_section(secs, key)
        if not sec:
            return None
        return re.search(pattern, "\n".join(pl[sec.start + 1:sec.end])) is not None

    for kind, key, code in (("F", "never", "missing-F"), ("H", "heuristics", "missing-H")):
        for num in sorted(c.defs[kind]):
            hit = covered(key, LABEL_WORD_RE.format(kind=kind, num=num))
            if hit is False:
                rep.fail(t, "G5", code, f"{c.defs[kind][num].file}:{c.defs[kind][num].line}",
                         f"{kind}{num} 没出现在 SKILL.md「{SECTION_KEYS[key]}」")
    for num in sorted(c.defs["R"]):
        hit = covered("results", rf"(?<![A-Za-z0-9_-]){c.prefix}-R{num}(?![0-9A-Za-z])")
        if hit is False:
            rep.fail(t, "G5", "missing-R", f"04-results.md:{c.defs['R'][num].line}", f"{c.prefix}-R{num} 没出现在 SKILL.md「关键结果速查」")
    used = {r.id for r in all_refs}
    for kind in ("S", "L"):
        for num in sorted(c.defs[kind]):
            if f"{c.prefix}-{kind}{num}" not in used:
                rep.warn(t, "G5", "unused-S", f"01-canon.md:{c.defs[kind][num].line}", f"{c.prefix}-{kind}{num} 在 SKILL.md 里一次没出现")
    for f in c.researchers:
        stem = Path(f).stem
        if stem not in text and stem.replace("-", " ") not in fold(text):
            rep.warn(t, "G5", "researcher", f, f"SKILL.md 没提到档案 {stem}")
    rep.info(t, "G5", "coverage", "SKILL.md", f"05 的 F {len(c.defs['F'])} 条、04 的 R {len(c.defs['R'])} 条、"
             f"03 的 H {len(c.defs['H'])} 条逐条核对；01 的 S/L {len(c.defs['S']) + len(c.defs['L'])} 条中 "
             f"{sum(1 for k in ('S', 'L') for n in c.defs[k] if f'{c.prefix}-{k}{n}' in used)} 条被引用")

    # ---- G6
    ch = c.prose.get("00-charter.md", [])
    probe = next((s for s in sections(ch) if "试答" in s.title), None)
    if not probe:
        rep.warn(t, "G6", "probes", "00-charter.md", "没有「试答题」小节：G6 只能用 DISTILL.md 的默认题")
    else:
        qs = [it for it in items_in(ch, probe.start + 1, probe.end) if it.kind == "bullet"]
        if len(qs) < DEFAULT_PROBES:
            rep.fail(t, "G6", "probes", f"00-charter.md:{probe.start + 1}", f"试答题只有 {len(qs)} 题（至少 {DEFAULT_PROBES}）")
        outside = 0
        for q in qs:
            refs, labels = refs_in_text(q.text, c.prefix, q.line)
            is_outside = "语料外" in q.text or "未覆盖" in q.text
            outside += is_outside
            if not refs and not labels and not is_outside:
                rep.fail(t, "G6", "probes", f"00-charter.md:{q.line}", f"试答题没写应命中的 ID / 标签：{q.text[:80]}")
        if not outside:
            rep.warn(t, "G6", "probes", f"00-charter.md:{probe.start + 1}", "没有「语料外」题（检验 skill 会不会如实说未覆盖）")
        rep.info(t, "G6", "probes", "00-charter.md", f"{len(qs)} 道试答题（语料外 {outside}）")
    return meta


def _author_hit(c: Corpus, surnames: list[str], year: str) -> str:
    """01-canon 里有没有同时含年份与全部姓氏的行：all / some / none。"""
    best = "none"
    for line in c.canon_lines:
        if year not in line:
            continue
        hits = [s for s in surnames if re.search(rf"(?<![a-z]){re.escape(s)}(?![a-z])", line)]
        if surnames and len(hits) == len(surnames):
            return "all"
        if hits:
            best = "some"
        elif not surnames:
            return "all"
    return best


def _check_stamp(c: Corpus, rep: Report, repo: Path, stamp: str, strict: bool):
    t = c.slug
    rel = f"teams/{c.slug}"
    rc, _ = git(repo, "rev-parse", "--verify", "--quiet", f"{stamp}^{{commit}}")
    if rc == 127:
        rep.warn(t, "G4", "stamp", "SKILL.md", "找不到 git，无法核对语料版本")
        return
    if rc != 0:
        rep.fail(t, "G4", "stamp", "SKILL.md", f"语料版本 {stamp} 不是本仓库的提交")
        return
    rc, _ = git(repo, "merge-base", "--is-ancestor", stamp, "HEAD")
    if rc != 0:
        _, want = git(repo, "rev-parse", f"{stamp}:{rel}")
        equiv = ""
        _, lst = git(repo, "rev-list", "HEAD", "--", rel)
        for h in lst.split():
            _, tree = git(repo, "rev-parse", f"{h}:{rel}")
            if tree == want:
                equiv = h[:7]
        hint = f"；{rel} 同树的现历史提交：{equiv}（可改戳）" if equiv else ""
        rep.warn(t, "G4", "stamp", "SKILL.md", f"语料版本 {stamp} 不在当前 HEAD 的历史上（历史被重写？）{hint}")
    _, changed = git(repo, "diff", "--name-only", stamp, "HEAD", "--", rel)
    files = [f for f in changed.split("\n") if f and Path(f).name not in PRODUCT_FILES]
    if files:
        (rep.fail if strict else rep.warn)(t, "G4", "stamp", "SKILL.md",
                                           f"语料在版本 {stamp} 之后改过（skill 过期，需重跑蒸馏）：{', '.join(Path(f).name for f in files)}")
    _, dirty = git(repo, "status", "--porcelain", "--", rel)
    dirty_files = [l[3:] for l in dirty.split("\n") if l.strip() and Path(l[3:].strip()).name not in PRODUCT_FILES]
    if dirty_files:
        rep.warn(t, "G4", "stamp", rel, f"工作区有未提交的语料改动：{', '.join(Path(f).name for f in dirty_files)}")
    _, log = git(repo, "log", "-1", "--format=%h %ad %s", "--date=short", stamp)
    rep.info(t, "G4", "stamp", "SKILL.md", f"语料版本 {log}" + ("" if files else " · 语料自此未变"))


def check_installed(c: Corpus, rep: Report, name: str):
    if not name:
        rep.warn(c.slug, "install", "installed", "SKILL.md", "frontmatter 没有 name，不知道装到哪")
        return
    p = Path.home() / ".claude" / "skills" / name / "SKILL.md"
    if not p.exists():
        rep.warn(c.slug, "install", "installed", str(p), "未安装")
        return
    a = (c.skill or "").replace("\r\n", "\n").rstrip()
    b = p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").rstrip()
    if a != b:
        rep.warn(c.slug, "install", "installed", str(p), "已安装副本与仓库 SKILL.md 不一致（Phase 5 要重新复制）")
    else:
        rep.info(c.slug, "install", "installed", str(p), "与仓库一致")


# ---------------------------------------------------------------- 主程序


MARK = {"fail": "✗", "warn": "⚠", "info": "i", "pass": "✓"}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="DISTILL.md 语料流水线的确定性质量门（lint + G1–G6 机械部分 + 版本戳 + 安装漂移）",
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="teams/<team> 或 teams")
    ap.add_argument("--lint", action="store_true", help="只查语料，不查 SKILL.md")
    ap.add_argument("--installed", action="store_true", help="比对 ~/.claude/skills/<name>/SKILL.md")
    ap.add_argument("--no-git", action="store_true", help="不做 git 版本戳检查")
    ap.add_argument("--strict-stale", action="store_true", help="语料在版本戳之后有改动时判 ✗")
    ap.add_argument("--show-pairs", action="store_true", help="列出 G2 核对的每个（作者, 年份）对及其命中情况（对账表）")
    ap.add_argument("--quiet", action="store_true", help="不打印 i 行")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    path = Path(a.path)
    if (path / "01-canon.md").exists():
        teams_root, only = path.parent, [path.name]
    elif path.is_dir() and any((p / "01-canon.md").exists() for p in path.iterdir() if p.is_dir()):
        teams_root, only = path, None
    else:
        print(f"❌ {path}: 不是团队目录（没有 01-canon.md），也不是 teams/ 根", file=sys.stderr)
        sys.exit(2)
    repo = teams_root.resolve().parent
    reg = Registry(teams_root)
    rep = Report()
    metas: dict[str, dict] = {}
    for slug, c in reg.by_slug.items():
        if only and slug not in only:
            continue
        check_lint(c, reg, rep)
        if a.lint:
            continue
        if c.skill is None:
            rep.info(slug, "G1", "skill", slug, "还没有 SKILL.md（未蒸馏）")
            continue
        metas[slug] = check_skill(c, reg, rep, repo, not a.no_git, a.strict_stale, a.show_pairs)
        if a.installed:
            check_installed(c, rep, metas[slug]["name"])

    if a.json:
        print(json.dumps({"rows": rep.rows, "failed": len(rep.failed)}, ensure_ascii=False, indent=1))
        sys.exit(1 if rep.failed else 0)

    for slug in (only or list(reg.by_slug)):
        c = reg.by_slug.get(slug)
        if not c:
            continue
        m = metas.get(slug, {})
        head = f"teams/{slug}"
        if m.get("date") or m.get("stamp"):
            head += f" · SKILL.md 蒸馏 {m.get('date') or '?'} @ {m.get('stamp') or '?'}"
        print(head)
        for r in rep.rows:
            if r["team"] != slug or r["status"] == "info" and a.quiet:
                continue
            if r["status"] == "info":
                continue
            print(f"  {MARK[r['status']]} {r['gate']} {r['code']}: {r['where']}: {r['detail']}")
        if not a.quiet:
            for r in rep.rows:
                if r["team"] == slug and r["status"] == "info":
                    print(f"  i {r['gate']} {r['code']}: {r['detail']}")
        gates = [g for g in Report.GATES if any(r["team"] == slug and r["gate"] == g for r in rep.rows)]
        summary = []
        for g in gates:
            nf, nw = rep.count(slug, g, "fail"), rep.count(slug, g, "warn")
            summary.append(f"{g} {'✗' if nf else '✓'}" + (f"({nf} ✗, {nw} ⚠)" if nf or nw else ""))
        print("  " + " · ".join(summary))
    bad = len(rep.failed)
    warns = sum(1 for r in rep.rows if r["status"] == "warn")
    print(f"{'❌' if bad else '✅'} {bad} ✗ · {warns} ⚠ · {len(metas)} skill(s) · {len(only or reg.by_slug)} team(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
