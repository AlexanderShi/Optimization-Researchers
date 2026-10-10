#!/usr/bin/env python3
"""
研究Skill的引用闭包检查（研究Skill · 深读档的引用闸门：T3.6 / T3.7 / T3.8 / T4 之后、交付之前）。

摘录（quotes）有 verify_card_quotes.py 逐字核对；但 SKILL.md、证据账本、技术目录、学生模式文件和圆桌里成百上千条
「[card S012, pp. 20–21]」式引用此前没有闸门：卡片是否存在、页码是否落在真正读过的全文范围内、按摘要/元数据级读的
作品有没有被当成全文引页，都没人查（check_ledger.py --before 只查精简时有没有丢引用，team_check.py 只查圆桌
fault line 的卡片 ID）。本脚本把这些变成确定性检查：引用必须指向真实存在、确实读过、页码在范围内的卡片。

检查（任何一项 ✗ 退出码为 1）:
    unknown-id       引用的作品 ID 不在这位成员的卡片、INDEX.md 或 works.json 里（笔误，或凭空造出的卡片）
    no-card          作品在 INDEX / works.json 里但没有卡片，却被当证据引用（引了页码，或该行不是 skip）
    page-on-unread   引了页码，但该作品最深的卡片只到 abstract / metadata / unreadable 级（没有全文就没有页码）
    page-range       引用的页码超过 INDEX.md 的 Pages（读的就是那个文件）
    version          版本引用（见下）所引的卡片不存在，或卡片正文里没有提到那个版本
    roundtable       圆桌里 [<slug> card …] 的 slug 不是队员；或该引用在那位成员处过不了上面的检查
警告（⚠，不计入退出码）:
    skip-mention     只提到（不带页码）INDEX 里 Role=skip 的行，例如诚实边界里说明哪些行被排除
    roundtable-bare  圆桌里不带 [<slug> card …] 的裸卡片 ID，无法判定属于谁
信息（不计入退出码）:
    每个文件的引用数、带页码的引用数、不同作品数、版本引用数；DOI / arXiv 标识数（在 works.json 里的 / 外部的）
    --methods：每个核心方法的证据：卡片 method_links 里指向它的不同作品数（evidence / variant / contradiction）、
               SKILL.md 该方法一节里引用的不同作品数、Say–do 标记。深读后晋升的方法在卡片里没有 method_links
               （读卡时它还不存在），所以两个数都看；--strict-methods 时两个数都少于 --min-evidence（默认 3）算 ✗

版本引用：读的不是索引里那个文件、而是同一作品的另一个版本（技术报告版、预印本、后一版手册）时，在 ID 和页码之间
写明版本，如 [S025 TR pp. 3–12]、[S133 v2.0 pp. 1–3]、[S012 arXiv pp. 4–5]（版本词也可以跟在页码后面的同一段里，
如 [S133 p. 1 (v2.0 manual)]）；卡片正文必须写明读的是哪个版本（含同一个词）。这种引用只查卡片存在与版本说明，
不查 read_level 和页数（索引的 Pages 是另一个文件的）。
认得的版本词：TR、v<数字>、arXiv、preprint、report、manual、draft、precursor、substitute。

扫描的文件（成员）：SKILL.md；references/*.md（technique-catalog、proof-playbook、open-problems、reading-path）；
references/research/0[1-9]-*.md（不含 cards/：卡片本身是证据，不是引用）。团队目录时还查圆桌 SKILL.md 的
[<slug> card …] 引用。轻量档成员（没有 cards/）不查卡片 ID，只报 DOI / arXiv 计数。
不扫描：围栏代码块、front matter、行内代码 `…`（写法示例）、表格单元格之外的页码（| 不能跨）。

引用写法（ID 规则与 check_ledger.py 相同：一个大写字母 + 3–4 位数字；字母限于 S D H R X B 和这位成员 works.json
实际用到的，别的字母如 [O102]、[P643 abstract] 这类轻量档自定标签不认；works.json 里 dup_of 指向别行的 ID 按被指向的行算）:
    [S012 p. 9]  [S012 pp. 3, 8–9]  [card S012, pp. 20–21]  [cards S023, pp. 17–19; S104, pp. 26–30]  [S012]
    [S088, Thm 4.6, pp. 11–12]  [S012 第3页]  [S053 p. 14, 1993]（末尾的年份不算页码）；圆桌：[michael-powell card S093 pp. 3–4]
    DOI 里的 S0025-5718 之类不算 ID（紧跟在 10.xxxx/ 后面的不认）。

用法:
    python3 check_citations.py <成员目录|团队目录> [--member a,b] [--roundtable | --no-roundtable]
                               [--methods] [--strict-methods] [--min-evidence 3] [--show N] [--json]
示例:
    python3 scripts/check_citations.py product/dfo-team                        # 全体成员 + 圆桌
    python3 scripts/check_citations.py product/dfo-team/katya-scheinberg       # 一位成员
    python3 scripts/check_citations.py product/dfo-team --roundtable           # 只查圆桌
    python3 scripts/check_citations.py product/dfo-team --methods              # 另加每个方法的证据计数

输出:
    每个问题一行（✗ 类别: 文件:行: 内容），警告一行一个 ⚠，每位成员一行汇总；最后一行 ✅/❌ 总计。
    有 ✗ 退出码 1，路径不存在为 2。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from check_links import prose_lines  # noqa: E402  front matter / 围栏代码块换成空行，行号不变
import team_status as ts  # noqa: E402  INDEX.md 解析

LEVEL_RANK = {"full": 4, "partial": 3, "abstract": 2, "metadata": 1, "unreadable": 0}
UNREAD = {"abstract", "metadata", "unreadable"}
DEFAULT_LETTERS = set("SDHRXB")
# 页码单元：起页最多 3 位（PDF 页），区间终页最多 4 位；4 位数字（年份）不算页
PAGES = r"\d{1,3}(?:\s*[-–—]\s*\d{1,4})?(?:\s*,\s*\d{1,3}(?:\s*[-–—]\s*\d{1,4})?)*"
VERSION_RE = re.compile(r"\b(TR|v\d+(?:\.\d+)*|arXiv|preprint|report|manual|draft|precursor|substitute)\b", re.I)
# 一条引用：ID，然后（同一段 […] 或同一表格单元格里、不越过 ; 和另一个 ID）可选的页码
CITE_RE = re.compile(
    r"(?<![A-Za-z0-9_])(?P<id>[A-Z]\d{3,4})(?![0-9])"
    r"(?:(?P<gap>(?:(?![A-Z]\d{3})[^\]\[;|\n]){0,30}?)"
    r"(?:(?<![A-Za-z])pp?\.?\s*(?P<pages>" + PAGES + r")(?![\d])|第\s*(?P<zh>" + PAGES + r")\s*页))?")
DOI_PREFIX_RE = re.compile(r"10\.\d{4,9}/[^\s]*$")
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s\"'<>)\]|,;]+)")
ARXIV_RE = re.compile(r"(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?\b")
SLUG_RE = re.compile(r"^\s*(?P<slug>[a-z0-9][a-z0-9-]*) cards?\s+")
RT_RE = re.compile(r"\[(?P<slug>[a-z0-9][a-z0-9-]*) cards?\s+(?P<body>[^\]]+)\]")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
METHOD_HEAD_RE = re.compile(r"^###\s+(?:Method|方法)\s*(\d+)\b.*$", re.I | re.M)
SAYDO_RE = re.compile(r"say[–\-]?do|言行一致", re.I)
MEMBER_FILES = ["SKILL.md", "references/technique-catalog.md", "references/proof-playbook.md",
                "references/open-problems.md", "references/reading-path.md"]


def page_numbers(spec: str) -> list[int]:
    nums = []
    for unit in re.split(r"\s*,\s*", spec.strip()):
        parts = [int(x) for x in re.findall(r"\d+", unit)]
        if parts:
            nums.append(max(parts))
    return nums


def heading_at(prose: list[str]) -> list[str]:
    """每一行所在的最近标题（给报告用）。"""
    out, cur = [], ""
    for line in prose:
        m = re.match(r"^ {0,3}#{1,6}[ \t]+(.*?)[ \t#]*$", line)
        if m:
            cur = m.group(1).strip()
        out.append(cur)
    return out


def blank_code(line: str) -> str:
    """行内代码换成等长空格（写法示例不算引用），行号与列位置不变。"""
    return INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), line)


class Member:
    def __init__(self, team: Path, m: dict):
        self.slug = m["slug"]
        self.name = m.get("name") or m["slug"]
        self.dir = team / self.slug
        research = self.dir / "references/research"
        self.cards_dir = research / "cards"
        self.cards: dict[str, dict] = {}
        for dj in sorted(self.cards_dir.glob("*.digest.json")) if self.cards_dir.is_dir() else []:
            try:
                data = json.loads(dj.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            for c in data:
                cid, lv = str(c.get("id") or ""), str(c.get("read_level") or "")
                if not cid:
                    continue
                rec = self.cards.setdefault(cid, {"best": "", "batches": [], "levels": set()})
                rec["batches"].append(dj.name.replace(".digest.json", ""))
                rec["levels"].add(lv)
                if LEVEL_RANK.get(lv, -1) > LEVEL_RANK.get(rec["best"], -1):
                    rec["best"] = lv
        self.deep = bool(self.cards)
        self.index = {r["ID"]: r for r in ts.index_rows(self.dir / "references/sources/papers/INDEX.md") if r.get("ID")}
        wj = self.dir / "references/sources/publications/works.json"
        self.works: dict[str, dict] = {}
        if wj.exists():
            try:
                for w in json.loads(wj.read_text(encoding="utf-8")).get("works", []):
                    if w.get("id"):
                        self.works[str(w["id"])] = w
            except json.JSONDecodeError:
                pass
        self.letters = DEFAULT_LETTERS | {i[0] for i in list(self.works) + list(self.index) + list(self.cards)}
        self.dois = {str(w.get("doi")).lower() for w in self.works.values() if w.get("doi")}
        self.arxivs = {re.sub(r"v\d+$", "", str(w.get("arxiv"))) for w in self.works.values() if w.get("arxiv")}
        self._card_md: dict[str, str] = {}

    def canonical(self, cid: str) -> str:
        """works.json 里 dup_of 指向别行的 ID → 被指向的行（最多跟 5 跳）。"""
        seen = 0
        while cid in self.works and self.works[cid].get("dup_of") and seen < 5:
            cid = str(self.works[cid]["dup_of"])
            seen += 1
        return cid

    def pages_of(self, cid: str) -> int | None:
        p = (self.index.get(cid) or {}).get("Pages", "")
        return int(p) if p and p.isdigit() else None

    def card_markdown(self, cid: str) -> str:
        """这位成员所有批次里该作品的卡片正文（合并）。"""
        if cid in self._card_md:
            return self._card_md[cid]
        texts = []
        for b in (self.cards.get(cid) or {}).get("batches", []):
            md = self.cards_dir / f"{b}.md"
            if not md.exists():
                continue
            t = md.read_text(encoding="utf-8", errors="replace")
            heads = list(re.finditer(r"^###\s+([A-Z]\d{3,4})\b", t, re.M))
            for k, h in enumerate(heads):
                if h.group(1) == cid:
                    texts.append(t[h.start():heads[k + 1].start() if k + 1 < len(heads) else len(t)])
        self._card_md[cid] = "\n".join(texts)
        return self._card_md[cid]

    def check_cite(self, cid: str, pages: list[int], version: str) -> tuple[str | None, str]:
        """(问题类别或 None, 说明)；类别以 '~' 开头表示警告。"""
        orig = cid
        cid = self.canonical(cid)
        via = f" (= {orig}, dup_of)" if cid != orig else ""
        card = self.cards.get(cid)
        row = self.index.get(cid)
        if card is None:
            if row is None and cid not in self.works:
                return "unknown-id", f"{orig}: not in this member's cards, INDEX.md or works.json"
            role = (row or {}).get("Role", "")
            if not pages and role == "skip":
                return "~skip-mention", f"{orig}: INDEX row is Role=skip (mentioned, no page cited)"
            why = f"Role={role or '?'}, Read={(row or {}).get('Read') or '—'}" if row else "in works.json only, not in INDEX.md"
            return "no-card", f"{orig}{via}: no paper card ({why})" + (f"; pages cited: {pages}" if pages else "")
        if version:
            if version.lower() not in self.card_markdown(cid).lower():
                return "version", (f"{orig}{via}: cited as the '{version}' version, but the card (batch "
                                   f"{', '.join(card['batches'])}) never mentions '{version}': say which version was read")
            return None, ""
        if pages and card["best"] in UNREAD:
            return "page-on-unread", (f"{orig}{via}: p. {max(pages)} cited, but its deepest card is {card['best']}-level "
                                      f"(batch {', '.join(card['batches'])}): no full text, so no page to cite"
                                      " (a substitute version read instead? then cite it as a version: [ID TR pp. …])")
        n = self.pages_of(cid)
        if pages and n and max(pages) > n:
            return "page-range", f"{orig}{via}: p. {max(pages)} cited, but INDEX.md says the file read has {n} pages"
        return None, ""


def cites_in(line: str, letters: set[str]):
    """一行里的引用：(match, id, pages, version)。"""
    for m in CITE_RE.finditer(line):
        cid = m.group("id")
        if cid[0] not in letters or DOI_PREFIX_RE.search(line[max(0, m.start() - 24):m.start()]):
            continue
        spec = m.group("pages") or m.group("zh") or ""
        pages = page_numbers(spec) if spec else []
        version = ""
        if spec:  # 版本词可以在页码前（S025 TR pp. 3–12）或页码后同一段里（S133 p. 1 (v2.0 manual)）
            tail = re.split(r"[\]\[;|\n]|(?=[A-Z]\d{3})", line[m.end():m.end() + 40], maxsplit=1)[0]
            vm = VERSION_RE.search(m.group("gap") or "") or VERSION_RE.search(tail)
            version = vm.group(1) if vm else ""
        yield m, cid, pages, version


def scan_text(text: str, mem: Member, rel: str, report: dict):
    """扫描一个文件的全部引用，问题写进 report。"""
    prose = [blank_code(l) for l in prose_lines(text)]
    heads = heading_at(prose)
    cites = paged = versioned = 0
    ids: set[str] = set()
    for no, line in enumerate(prose, 1):
        for m, cid, pages, version in cites_in(line, mem.letters):
            cites += 1
            ids.add(cid)
            paged += bool(pages)
            versioned += bool(version)
            kind, detail = mem.check_cite(cid, pages, version)
            if kind:
                entry = {"file": rel, "line": no, "section": heads[no - 1], "detail": detail, "text": line.strip()[:160]}
                (report["warnings"] if kind.startswith("~") else report["problems"]).setdefault(kind.lstrip("~"), []).append(entry)
    joined = "\n".join(prose)
    dois = {d.rstrip(".").lower() for d in DOI_RE.findall(joined)}
    arx = set(ARXIV_RE.findall(joined))
    report["files"][rel] = {"cites": cites, "paged": paged, "versioned": versioned, "ids": len(ids),
                            "dois": len(dois), "dois_own": len(dois & mem.dois),
                            "arxiv": len(arx), "arxiv_own": len(arx & mem.arxivs)}


def method_audit(mem: Member, min_ev: int) -> list[dict]:
    skill = mem.dir / "SKILL.md"
    if not skill.exists():
        return []
    text = skill.read_text(encoding="utf-8")
    heads = list(METHOD_HEAD_RE.finditer(text))
    links: dict[int, dict[str, set]] = {}
    for dj in sorted(mem.cards_dir.glob("*.digest.json")) if mem.deep else []:
        try:
            data = json.loads(dj.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for c in data:
            for ml in c.get("method_links") or []:
                mm = re.match(r"^(?:Method|M|方法)\s*(\d+)\b", str(ml.get("method") or ""), re.I)
                if mm:
                    links.setdefault(int(mm.group(1)), {}).setdefault(str(ml.get("relation") or "evidence"), set()).add(
                        mem.canonical(str(c.get("id"))))
    out = []
    for k, h in enumerate(heads):
        n = int(h.group(1))
        end = heads[k + 1].start() if k + 1 < len(heads) else len(text)
        block = text[h.end():end]
        nxt = re.search(r"^##\s", block, re.M)  # 下一个二级标题处截断
        if nxt:
            block = block[:nxt.start()]
        say = next((ln for ln in block.splitlines() if SAYDO_RE.search(ln)), "")
        mark = "✅" if "✅" in say else ("⚠" if "⚠" in say else "?")
        cited = {mem.canonical(cid) for ln in blank_code(block).splitlines() for _, cid, _, _ in cites_in(ln, mem.letters)}
        ev = links.get(n, {})
        n_ev, n_cited = len(ev.get("evidence", ())), len(cited)
        out.append({"method": n, "title": h.group(0).split(":", 1)[-1].strip()[:60], "say_do": mark,
                    "evidence": n_ev, "variant": len(ev.get("variant", ())),
                    "contradiction": len(ev.get("contradiction", ())), "cited_in_block": n_cited,
                    "thin": n_ev < min_ev and n_cited < min_ev})
    return out


def check_member(team: Path, m: dict, args) -> dict:
    mem = Member(team, m)
    report = {"slug": mem.slug, "deep": mem.deep, "files": {}, "problems": {}, "warnings": {}, "methods": []}
    if not mem.deep:
        skill = mem.dir / "SKILL.md"
        if skill.exists():
            joined = "\n".join(prose_lines(skill.read_text(encoding="utf-8")))
            report["files"]["SKILL.md"] = {"dois": len(set(DOI_RE.findall(joined))), "arxiv": len(set(ARXIV_RE.findall(joined)))}
        return report
    # 07-paper-cards.md 不扫：它是 digest 的投影（build_card_index.py），单元格里的页码是书目页，不是读到的页
    files = [mem.dir / f for f in MEMBER_FILES] + sorted(
        p for p in (mem.dir / "references/research").glob("0[1-9]-*.md") if not p.name.startswith("07-"))
    for f in files:
        if f.exists():
            scan_text(f.read_text(encoding="utf-8"), mem, f.relative_to(mem.dir).as_posix(), report)
    if args.methods:
        report["methods"] = method_audit(mem, args.min_evidence)
        if args.strict_methods:
            for r in report["methods"]:
                if r["thin"]:
                    report["problems"].setdefault("method-evidence", []).append(
                        {"file": "SKILL.md", "line": 0, "section": f"Method {r['method']}",
                         "detail": (f"Method {r['method']}: {r['evidence']} work(s) link to it in the card digests and "
                                    f"{r['cited_in_block']} distinct work(s) are cited in its section (both < {args.min_evidence})"),
                         "text": ""})
    return report


def check_roundtable(team: Path, cfg: dict, members: dict[str, Member]) -> dict:
    rt = team / str(cfg.get("roundtable") or "") / "SKILL.md"
    report = {"file": rt.relative_to(team).as_posix() if rt.exists() else "", "cites": 0, "paged": 0,
              "problems": {}, "warnings": {}}
    if not cfg.get("roundtable") or not rt.exists():
        return report
    prose = [blank_code(l) for l in prose_lines(rt.read_text(encoding="utf-8"))]

    def add(kind: str, no: int, detail: str, line: str):
        entry = {"file": report["file"], "line": no, "detail": detail, "text": line.strip()[:160]}
        (report["warnings"] if kind.startswith("~") else report["problems"]).setdefault(kind.lstrip("~"), []).append(entry)

    for no, line in enumerate(prose, 1):
        covered = []
        for m in RT_RE.finditer(line):
            covered.append((m.start(), m.end()))
            slug = m.group("slug")
            # 一对方括号里可以有几位成员：[a card S1 p. 2; b card S3 p. 4]，按 ; 切段，段首的 "<slug> card" 换人
            for seg in m.group("body").split(";"):
                sm = SLUG_RE.match(seg)
                if sm:
                    slug, seg = sm.group("slug"), seg[sm.end():]
                mem = members.get(slug)
                if mem is None:
                    add("roundtable", no, f"[{slug} card …]: '{slug}' is not a member slug in team.json", line)
                    continue
                if not mem.deep:
                    add("~roundtable-bare", no, f"[{slug} card …] but {slug} has no cards (base tier)", line)
                    continue
                for _, cid, pages, version in cites_in(seg, mem.letters):
                    report["cites"] += 1
                    report["paged"] += bool(pages)
                    kind, detail = mem.check_cite(cid, pages, version)
                    if kind:
                        add("roundtable" if not kind.startswith("~") else kind, no, f"[{slug} card …] {detail}", line)
        for c in CITE_RE.finditer(line):  # 裸 ID：不在任何 [<slug> card …] 里
            if any(s <= c.start() < e for s, e in covered):
                continue
            if c.group("id")[0] not in DEFAULT_LETTERS or DOI_PREFIX_RE.search(line[max(0, c.start() - 24):c.start()]):
                continue
            add("~roundtable-bare", no, f"{c.group('id')}: card id without [<slug> card …], cannot tell whose", line)
    return report


def n_problems(rep: dict) -> int:
    return sum(len(v) for v in rep.get("problems", {}).values())


def print_entries(kind: str, entries: list[dict], mark: str, show: int):
    for e in entries[:show]:
        where = f"{e['file']}:{e['line']}" if e.get("line") else e["file"]
        print(f"  {mark} {kind}: {where}: {e['detail']}")
    if len(entries) > show:
        print(f"  … {len(entries) - show} more {kind}" + (" (--show-warnings N to list more)" if mark == "⚠" else ""))


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description="研究Skill引用闭包检查：每条卡片引用都指向真实存在、确实读过、页码在范围内的卡片",
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="成员目录（含 SKILL.md）或团队目录（含 team.json）")
    ap.add_argument("--member", default="", help="团队目录时只查这几位（逗号分隔 slug）")
    ap.add_argument("--roundtable", action="store_true", help="团队目录时只查圆桌")
    ap.add_argument("--no-roundtable", action="store_true", help="团队目录时不查圆桌")
    ap.add_argument("--methods", action="store_true", help="另报每个核心方法的证据计数")
    ap.add_argument("--strict-methods", action="store_true", help="证据不足 --min-evidence 的方法算 ✗（隐含 --methods）")
    ap.add_argument("--min-evidence", type=int, default=3, help="--strict-methods 的门槛（默认 3，与新方法的晋升门槛相同）")
    ap.add_argument("--show", type=int, default=40, help="每类问题最多列几条（默认 40）")
    ap.add_argument("--show-warnings", type=int, default=5, help="每类警告最多列几条（默认 5；0 只给数目）")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.strict_methods:
        a.methods = True
    p = Path(a.path)
    if (p / "team.json").exists():
        team = p
        cfg = json.loads((team / "team.json").read_text(encoding="utf-8"))
        members_cfg = cfg.get("members") or []
    elif (p / "SKILL.md").exists():
        team = p.parent
        cfg = json.loads((team / "team.json").read_text(encoding="utf-8")) if (team / "team.json").exists() else {}
        members_cfg = [m for m in cfg.get("members", []) if m.get("slug") == p.name] or [{"slug": p.name, "name": p.name}]
        a.no_roundtable = True
    else:
        print(f"❌ {p}: neither a team folder (team.json) nor a member folder (SKILL.md)", file=sys.stderr)
        sys.exit(2)
    only = [x for x in a.member.split(",") if x]
    unknown = [x for x in only if x not in {m["slug"] for m in members_cfg}]
    if unknown:
        print(f"❌ --member: not in team.json: {', '.join(unknown)}", file=sys.stderr)
        sys.exit(2)

    members = {m["slug"]: Member(team, m) for m in cfg.get("members", members_cfg)}
    reports = []
    if not a.roundtable:
        for m in members_cfg:
            if not only or m["slug"] in only:
                reports.append(check_member(team, m, a))
    rt = None
    if not a.no_roundtable and cfg.get("roundtable"):
        rt = check_roundtable(team, cfg, members)

    total = sum(n_problems(r) for r in reports) + (n_problems(rt) if rt else 0)
    if a.json:
        print(json.dumps({"team": cfg.get("team", team.name), "members": reports, "roundtable": rt, "problems": total},
                         ensure_ascii=False, indent=1, default=sorted))
        sys.exit(1 if total else 0)

    for r in reports:
        if not r["deep"]:
            f = r["files"].get("SKILL.md", {})
            print(f"— {r['slug']}: no paper cards (base tier): card citations not applicable; "
                  f"SKILL.md has {f.get('dois', 0)} DOI(s), {f.get('arxiv', 0)} arXiv id(s)")
            continue
        for kind, entries in r["problems"].items():
            print_entries(kind, entries, "✗", a.show)
        for kind, entries in r["warnings"].items():
            print_entries(kind, entries, "⚠", a.show_warnings)
        if r["methods"]:
            print(f"  methods ({r['slug']}): " + "; ".join(
                f"M{x['method']} {x['say_do']} links {x['evidence']}/{x['variant']}/{x['contradiction']} cited {x['cited_in_block']}"
                + (" ⚠thin" if x["thin"] else "") for x in r["methods"]) + "  (links = evidence/variant/contradiction works in the digests; cited = distinct works cited in the section)")
        cites = sum(f["cites"] for f in r["files"].values())
        paged = sum(f["paged"] for f in r["files"].values())
        ver = sum(f["versioned"] for f in r["files"].values())
        dois = sum(f["dois"] for f in r["files"].values())
        own = sum(f["dois_own"] for f in r["files"].values())
        n = n_problems(r)
        w = sum(len(v) for v in r["warnings"].values())
        print(f"{'❌' if n else '✅'} {r['slug']}: {cites} card citations ({paged} with pages, {ver} to another version) in "
              f"{len(r['files'])} files; {dois} DOI(s) ({own} in works.json); {n} problem(s), {w} warning(s)")
    if rt:
        for kind, entries in rt["problems"].items():
            print_entries(kind, entries, "✗", a.show)
        for kind, entries in rt["warnings"].items():
            print_entries(kind, entries, "⚠", a.show_warnings)
        n = n_problems(rt)
        print(f"{'❌' if n else '✅'} roundtable: {rt['cites']} member-card citations ({rt['paged']} with pages); "
              f"{n} problem(s), {sum(len(v) for v in rt['warnings'].values())} warning(s)")
    print(f"{'❌' if total else '✅'} check_citations {p}: {total} problem(s)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
