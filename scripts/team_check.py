#!/usr/bin/env python3
"""
研究团队的交付闸门：把手册第四节、第九节的检查一次跑完（研究团队 · 每一档结束时、交付之前）。

用法:
    python3 scripts/team_check.py product/<team> [--tier auto|base|deep] [--skip-quality] [--member a,b] [--json]

检查（任何一项 ✗ 退出码为 1；— 表示跳过并写明原因）:
  团队
    team.json       能读、字段合法（与 new_team.py 同一套校验，含 guests 的形状）
    guests          team.json 有 guests（别队的单个成员坐进本队，见 new_team.py「客座」）时：每位客座都能解析
                    （new_team.resolve_guests：home 的 team.json 在、slug 是那队的成员、home 下有他的文件夹、本队没有同名的
                    影子文件夹），SKILL.md 在 product/<home>/<slug>/ 里、## Roundtable Card 的 7 项齐全（缺了在 home 队修）；
                    通过时列出每位客座的 home 与进度；撞姓只在说明里提一句、不判 ✗，并写明在哪改（有本队成员撞姓：
                    先改本队成员的 surname；只是两位客座撞姓：在其中一位客座的 home 队 team.json 里改）。没有 guests 不报
    hosts           只提示（—）：别的团队的 team.json 把本队成员列为 guests 时，列出那些团队与成员（改这些成员后要重跑
                    那几队的 team-layer.js / team-integrate.js）。经 guest_teams 整队入座的不报
    links           check_links.py <team> 0 broken
    templates       团队里所有 .md 没有 {{ 和 [TODO
    git             git ls-files <team> 里没有 PDF / PostScript / DjVu / EPUB、txt/，private/ 下只有 README.md
    readme          团队 README 链接每位成员的文件夹（](<slug>/…)），有客座时也链接每位客座（](../<home>/<slug>/…)）
    roundtable      圆桌 SKILL.md 存在，frontmatter name = team.json 的 roundtable；Team 表有每位成员的 `slug`；
                    座位表里每位成员至少主讲一行；3–6 条 fault line，每条引用至少两位成员
                    （深读档：每条两边都有 [<slug> card <ID> p. N] 卡片引用，引用的 ID 在该成员的卡片里都存在，
                    不剩 "card evidence pending"）。只有 1 位成员时跳过（—）：team-layer.js 不足 2 人不写圆桌，
                    团队级的圆桌引用闭包同样跳过。
                    理事会（team.json 有 guest_teams：别队的成员也坐上圆桌，如 product/optimization-council）不跳过：
                    Team 表有本队与各 guest 队每位成员的 `slug`；本队成员每人至少主讲一行，每个 guest 队至少有一人入座；
                    3–6 条 fault line，每条至少两位成员（可跨队），有卡片的成员一方必须是卡片证据、ID 在他自己团队目录的
                    卡片里；本队成员与每个 guest 队都至少出现在一条 fault line 里
                    有客座（team.json 的 guests）时走同一条路（入座单位 = new_team.seated_guests：guest_teams 的每一队、
                    guests 的每一位）：Team 表有每位客座的 `slug`，每位客座至少入座一行（主讲或挑战都算），至少进一条
                    fault line；有卡片的客座一方必须是卡片证据、ID 在他 home 队文件夹的卡片里；解析不了的客座直接报出原因。
                    有客座时这些提示里客座的 slug 标 "(guest)"、人数按 seat(s) 计（只有 guest_teams 的理事会照旧）。
                    "card evidence pending" 与普通团队一样只在本队成员全部按深读档查时判 ✗（深读档团队的 T2 还没有卡片时就这样写；
                    有 guest_teams 的理事会照旧一律判 ✗）。跳过只在「成员 + 客座 < 2 且没有 guest_teams」时
    lead            team.json 有 lead（可选的团队总入口 skill，如理事会的 optimization-lead）时：<lead>/SKILL.md 存在，
                    frontmatter name = lead；正文链接圆桌、本队每位成员的 skill 和每个 guest 队的文件夹（有客座时还有每位
                    客座的 ../../<home>/<slug>/）。没有 lead 不报
    coverage        深读档：DEEP-READING.md 原样含 team_status.py --coverage 的表，README 原样含 --coverage --short 的表
    answer-std      answer_standard.py --check <team> 0 ✗：每位成员、圆桌和 lead 的 SKILL.md 里「Answer Standard」一节
                    与 references/answer-standard.md 一致，研究者 skill 的三处旧条款带有位置说明（缺了就跑 --apply）
  每位成员
    skill           SKILL.md 存在；quality_check.py 12/12（--skip-quality 跳过）；## Roundtable Card 的 7 项齐全
    works           深读档：validate_works.py 0 errors；INDEX.md 行数 = 去重后的研究作品数
    cards           深读档：没有未读行（INDEX 的 Read 列）；07 / 08 / 09 / technique-catalog 都在
    quotes          深读档：verify_card_quotes.py NOT FOUND = 0（本地没有 txt/ 时跳过：PDF 和 txt 不进 git，新容器里要先重跑
                    acquire_fulltexts.py）
    ledger          深读档：check_ledger.py 指向 09-evidence-ledger.md 的锚点都能解析
    citations       深读档：check_citations.py 0 problems（SKILL.md、账本、技术目录、学生模式文件、01–09 里的每条
                    [card S012 pp. …] 都指向真实存在、确实读过、页码在范围内的卡片；团队级一项查圆桌的 [<slug> card …]；
                    有客座在 home 队有卡片时，轻量档团队也跑团队级这一项：他那一方按卡片引用）

--tier auto（默认）：按成员判档——写了卡片（references/research/cards/*.digest.json）的成员按深读档查，其余按轻量档查；
有成员深读过就查团队级的深读项（覆盖表、圆桌引用闭包）。混合档团队（只给部分成员做了深读）里，圆桌每条 fault line
至少引两位成员，深读过的那一方必须是卡片证据。--tier deep / base 对全体成员强制一个档。
客座不进成员级检查、判档和覆盖表（那些在他的 home 队查）；圆桌那一项按每个座位自己文件夹里有没有卡片判，
有带卡片的客座时团队级的圆桌引用闭包（citations）不论档位都跑。
别的团队（guest_teams、guests 的 home 队、hosts 扫的同级团队）都在团队目录绝对路径的上级里找（new_team.teams_root：
os.path.abspath，不跟随链接），所以在团队目录里跑 team_check.py . 也对，团队目录本身是链接时也照旧在它所在的文件夹里找；
打印的路径相对当前目录。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import team_status as ts  # noqa: E402
import new_team  # noqa: E402  team.json 校验与客座解析（resolve_guests / seated_guests）

CARD_LABELS = ["Lens", "Leads when", "First questions asked", "Default recommendation", "Will push back on",
               "Likely disagreements", "Blind spots"]
BAD_FILES = re.compile(r"\.(pdf|ps|ps\.gz|djvu|epub)$|/txt/|/private/", re.I)
CITE = re.compile(r"\[([a-z0-9][a-z0-9-]*) ([^\]]+)\]")
CARD_ID = re.compile(r"\b[A-Z]\d{3,}\b")


class Report:
    def __init__(self):
        self.rows = []

    def add(self, scope: str, name: str, ok: bool | None, detail: str = ""):
        self.rows.append({"scope": scope, "check": name, "status": "pass" if ok else ("skip" if ok is None else "fail"),
                          "detail": detail})

    @property
    def failed(self) -> list[dict]:
        return [r for r in self.rows if r["status"] == "fail"]


def run(cmd: list[str], cwd: Path | None = None) -> tuple[int, str]:
    # 子进程强制 UTF-8（Windows 控制台默认 cp1252：✓、… 这类字符会让子脚本报错或让这里解码失败），解码错误替换而不是抛出
    env = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=cwd, timeout=600, env=env)
    except (OSError, subprocess.TimeoutExpired) as e:
        return 99, str(e)
    return p.returncode, ((p.stdout or "") + (p.stderr or "")).strip()


def last_line(out: str) -> str:
    lines = [l for l in out.splitlines() if l.strip()]
    return lines[-1][:200] if lines else ""


def section(text: str, start: str, stop: re.Pattern) -> str:
    i = text.find(start)
    if i < 0:
        return ""
    m = stop.search(text, i + len(start))
    return text[i:m.start() if m else len(text)]


def digest_ids(member_dir: Path) -> set[str]:
    ids = set()
    for dj in (member_dir / "references/research/cards").glob("*.digest.json"):
        try:
            ids |= {str(c.get("id")) for c in json.loads(dj.read_text(encoding="utf-8"))}
        except (ValueError, AttributeError):
            pass
    return ids


def teams_root(team: Path) -> Path:
    """放各团队目录的文件夹（如 product/）= new_team.teams_root：团队目录绝对路径的上级（不跟随链接，与 make_args.mjs
    相同），团队目录给的是 . 或 ./x 时也对（Path('.').parent 还是 .）。别队（guest_teams、guests、hosts）都到这里找；
    打印的路径一律经 new_team.display()（相对当前目录）。"""
    return new_team.teams_root(team)


def guest_members(team: Path, cfg: dict) -> dict[str, list[dict]]:
    """坐上圆桌的别队的人（new_team.seated_guests）：理事会的 guest_teams 每队一项 {队名: [成员 dict（带 _dir）]}
    （读不到的队给空列表），team.json 的 guests 每位一项 {slug: [解析后的条目]}（解析不了给空列表）。"""
    return new_team.seated_guests(cfg, teams_root(team))


def guest_reasons(team: Path, cfg: dict) -> dict[str, str]:
    """解析不了的客座 → 原因（new_team.guest_reasons：resolve_guests 的错误去掉开头的 "guest <slug>: "）。"""
    return new_team.guest_reasons(cfg, teams_root(team))


def check_roundtable(rep: Report, team: Path, cfg: dict, deep: bool, deep_members: set[str] | None = None):
    slugs = [m["slug"] for m in cfg["members"]]
    rt = team / cfg["roundtable"] / "SKILL.md"
    guests = guest_members(team, cfg)
    if guests:
        # 与下面普通团队的深读档一支相同：本队成员全部按深读档查时，fault line 才不许再写 "card evidence pending"
        all_deep = deep and (set(slugs) if deep_members is None else set(deep_members)) == set(slugs)
        check_council(rep, team, cfg, rt, guests, deep_members or set(), all_deep)
        return
    if len(slugs) < 2:
        # 只有一位创始成员的团队：team-layer.js 不足 2 人不写圆桌，没有可查的座位表与 fault line
        rep.add("team", "roundtable", None, f"{len(slugs)} member: no roundtable until a second member joins "
                "(team-layer.js seats ≥2, playbook §一 recommends 3–6; add members per playbook §八)")
        return
    if not rt.exists():
        rep.add("team", "roundtable", False, f"{rt} missing (team-layer.js, T2)")
        return
    text = rt.read_text(encoding="utf-8")
    probs = []
    m = re.search(r"^name:\s*(\S+)", text, re.M)
    if not m or m.group(1) != cfg["roundtable"]:
        probs.append(f"frontmatter name is {m.group(1) if m else 'missing'}, team.json says {cfg['roundtable']}")
    team_tab = section(text, "## Team", re.compile(r"^## ", re.M))
    missing = [s for s in slugs if f"`{s}`" not in team_tab]
    if missing:
        probs.append(f"not in the Team table: {', '.join(missing)}")
    seat = section(text, "Step 1 · Seating", re.compile(r"^###? ", re.M))
    leads = []
    for line in seat.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.lstrip().startswith("|") and len(cells) >= 2 and not set(cells[0]) <= set("-: ") \
                and cells[1].lower() not in ("leads", "lead"):
            leads.append(cells[1])
    if not leads:
        probs.append("no seating table found under 'Step 1 · Seating'")
    else:
        idle = [mm["slug"] for mm in cfg["members"]
                if not any((mm.get("surname") or mm["name"].split()[-1]) in l for l in leads)]
        if idle:
            probs.append(f"leads no seating row: {', '.join(idle)}")
    fl = section(text, "Documented fault lines", re.compile(r"^> 🔵|^###? ", re.M))
    items = re.findall(r"^\d+\. \*\*(.+?)\*\*(.*)$", fl, re.M)
    if not 3 <= len(items) <= 6:
        probs.append(f"{len(items)} documented fault lines (3–6 expected)")
    ids = {s: digest_ids(team / s) for s in slugs} if deep else {}
    dm = set(slugs) if deep_members is None else deep_members
    mixed = deep and dm != set(slugs)  # 混合档：只有部分成员深读过
    for title, body in items:
        cites = [(s, t) for s, t in CITE.findall(body) if s in slugs]
        sides = {s for s, _ in cites}
        if mixed:
            # 混合档：至少两位成员有据；深读过的成员那一方必须是卡片证据，卡片 ID 存在
            if len(sides) < 2:
                probs.append(f"fault line '{title[:50]}': cites {len(sides)} member(s) as [<slug> …], 2 needed")
            uncarded = sorted(s for s in sides & dm if not any(s2 == s and re.match(r"cards?\b", t) for s2, t in cites))
            if uncarded:
                probs.append(f"fault line '{title[:50]}': deep-read member(s) {', '.join(uncarded)} cited without card evidence")
            miss = sorted({f"{s} {i}" for s, t in cites if re.match(r"cards?\b", t) for i in CARD_ID.findall(t)
                           if i not in ids.get(s, set())})
            if miss:
                probs.append(f"fault line '{title[:50]}': card ids not in the digests: {', '.join(miss[:8])}")
        elif deep:
            card_sides = {s for s, t in cites if re.match(r"cards?\b", t)}
            if len(card_sides) < 2:
                probs.append(f"fault line '{title[:50]}': card evidence from {len(card_sides)} member(s), 2 needed")
            miss = sorted({f"{s} {i}" for s, t in cites if re.match(r"cards?\b", t) for i in CARD_ID.findall(t)
                           if i not in ids.get(s, set())})
            if miss:
                probs.append(f"fault line '{title[:50]}': card ids not in the digests: {', '.join(miss[:8])}")
            if "evidence pending" in body:
                probs.append(f"fault line '{title[:50]}': still says 'card evidence pending'")
        elif len(sides) < 2:
            probs.append(f"fault line '{title[:50]}': cites {len(sides)} member(s) as [<slug> …], 2 needed")
    rep.add("team", "roundtable", not probs, "; ".join(probs) or
            f"{len(slugs)} members seated, {len(items)} fault lines with evidence from both sides")


def check_council(rep: Report, team: Path, cfg: dict, rt: Path, guests: dict[str, list[dict]], deep_members: set[str],
                  all_deep: bool = True):
    """带别队座位的圆桌：本队成员每人至少主讲一行；入座单位（guest_teams 的每一队、guests 的每一位客座）至少有一人
    入座、至少进一条 fault line；fault line 的两边可以来自不同团队，卡片 ID 到那位成员自己的团队目录里核对。
    只有一位本队成员也查（不像普通团队那样跳过）。只有 guest_teams 的理事会，提示与通过说明和以前逐字相同。
    "card evidence pending"：有 guest_teams 时照旧一律判 ✗；只有 guests 时与普通团队相同，all_deep（本队成员全部按深读档查）
    时才判 ✗——深读档团队 T2 还没有卡片时 team-layer.js 就写 "(card evidence pending)"，T3.8 才改成卡片证据。"""
    gslugs = {g.get("slug") for g in cfg.get("guests") or [] if isinstance(g, dict)}
    teams_u = {g: ms for g, ms in guests.items() if g not in gslugs}   # guest_teams：整队入座
    seats_u = {g: ms for g, ms in guests.items() if g in gslugs}       # guests：单个客座
    probs = [f"guest team {g}: no readable team.json with members" for g, ms in teams_u.items() if not ms]
    if any(not ms for ms in seats_u.values()):
        why = guest_reasons(team, cfg)
        probs += [f"guest {g}: not resolvable ({why.get(g, 'see the guests row')})" for g, ms in seats_u.items() if not ms]
    if not rt.exists():
        rep.add("team", "roundtable", False, f"{rt} missing ({'council layer' if teams_u else 'team-layer.js, T2'})")
        return
    text = rt.read_text(encoding="utf-8")
    m = re.search(r"^name:\s*(\S+)", text, re.M)
    if not m or m.group(1) != cfg["roundtable"]:
        probs.append(f"frontmatter name is {m.group(1) if m else 'missing'}, team.json says {cfg['roundtable']}")
    own = cfg["members"]
    everyone = {mm["slug"]: dict(mm, _dir=team / mm["slug"]) for mm in own}
    for ms in guests.values():
        for gm in ms:
            everyone.setdefault(gm["slug"], gm)
    # 有客座时，共用的提示里客座的 slug 标 "(guest)"、人数说 seat(s)；只有 guest_teams 的理事会照旧（标记为空）
    seat_slugs = {gm["slug"] for ms in seats_u.values() for gm in ms} - {mm["slug"] for mm in own}
    lab = lambda s: f"{s} (guest)" if s in seat_slugs else s  # noqa: E731
    team_tab = section(text, "## Team", re.compile(r"^## ", re.M))
    missing = [s for s in everyone if f"`{s}`" not in team_tab]
    if missing:
        probs.append(f"not in the Team table: {', '.join(lab(s) for s in missing[:8])}" + (" …" if len(missing) > 8 else ""))
    seat = section(text, "Step 1 · Seating", re.compile(r"^###? ", re.M))
    leads, seated = [], []
    for line in seat.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.lstrip().startswith("|") and len(cells) >= 2 and not set(cells[0]) <= set("-: ") \
                and cells[1].lower() not in ("leads", "lead"):
            leads.append(cells[1])
            seated.append(" ".join(cells[1:]))
    sur = lambda mm: mm.get("surname") or mm["name"].split()[-1]  # noqa: E731
    if not leads:
        probs.append("no seating table found under 'Step 1 · Seating'")
    else:
        idle = [mm["slug"] for mm in own if not any(sur(mm) in l for l in leads)]
        if idle:
            probs.append(f"leads no seating row: {', '.join(idle)}")
        unseated = [g for g, ms in teams_u.items() if ms and not any(sur(gm) in s for s in seated for gm in ms)]
        if unseated:
            probs.append(f"guest team(s) seated in no row: {', '.join(unseated)}")
        unseated = [g for g, ms in seats_u.items() if ms and not any(sur(gm) in s for s in seated for gm in ms)]
        if unseated:
            probs.append(f"guest(s) seated in no row: {', '.join(unseated)}")
    fl = section(text, "Documented fault lines", re.compile(r"^> 🔵|^###? ", re.M))
    items = re.findall(r"^\d+\. \*\*(.+?)\*\*(.*)$", fl, re.M)
    if not 3 <= len(items) <= 6:
        probs.append(f"{len(items)} documented fault lines (3–6 expected)")
    carded = {s for s, mm in everyone.items() if any((mm["_dir"] / "references/research/cards").glob("*.digest.json"))}
    dm = carded | (set(deep_members) & set(everyone))
    ids = {s: digest_ids(everyone[s]["_dir"]) for s in dm}
    in_fl = set()
    for title, body in items:
        cites = [(s, t) for s, t in CITE.findall(body) if s in everyone]
        sides = {s for s, _ in cites}
        in_fl |= sides
        if len(sides) < 2 and not seats_u:
            probs.append(f"fault line '{title[:50]}': cites {len(sides)} member(s) as [<slug> …], 2 needed")
        elif len(sides) < 2:
            probs.append(f"fault line '{title[:50]}': cites {len(sides)} seat(s) as [<slug> …], 2 needed"
                         + (f": {', '.join(lab(s) for s in sorted(sides))}" if sides else ""))
        uncarded = sorted(s for s in sides & dm if not any(s2 == s and re.match(r"cards?\b", t) for s2, t in cites))
        if uncarded:
            probs.append(f"fault line '{title[:50]}': deep-read {'member(s)' if not seats_u else 'seat(s)'} "
                         f"{', '.join(lab(s) for s in uncarded)} cited without card evidence")
        miss = sorted({(s, i) for s, t in cites if re.match(r"cards?\b", t) for i in CARD_ID.findall(t)
                       if i not in ids.get(s, set())})
        if miss:
            probs.append(f"fault line '{title[:50]}': card ids not in the digests: "
                         f"{', '.join(f'{lab(s)} {i}' for s, i in miss[:8])}")
        if "evidence pending" in body and (teams_u or all_deep):
            probs.append(f"fault line '{title[:50]}': still says 'card evidence pending'")
    quiet = [mm["slug"] for mm in own if mm["slug"] not in in_fl]
    if quiet:
        probs.append(f"in no fault line: {', '.join(quiet)}")
    absent = [g for g, ms in teams_u.items() if ms and not any(gm["slug"] in in_fl for gm in ms)]
    if absent:
        probs.append(f"guest team(s) in no fault line: {', '.join(absent)}")
    absent = [g for g, ms in seats_u.items() if ms and not any(gm["slug"] in in_fl for gm in ms)]
    if absent:
        probs.append(f"guest(s) in no fault line: {', '.join(absent)}")
    n_guest = sum(len(ms) for ms in teams_u.values())
    homes = ", ".join(dict.fromkeys(str(g.get("home")) for g in cfg.get("guests") or [] if isinstance(g, dict)))
    if not seats_u:  # 理事会（只有 guest_teams）：与以前逐字相同
        detail = (f"council: {len(own)} lead member(s) and {n_guest} guest members from {len(teams_u)} teams in the Team "
                  f"table, {len(items)} fault lines with evidence from both sides, every guest team seated and in a fault line")
    elif not teams_u:
        detail = (f"{len(own)} member(s) and {len(seats_u)} guest(s) from {homes} seated, {len(items)} fault lines with "
                  f"evidence from both sides, every guest seated and in a fault line")
    else:
        detail = (f"council: {len(own)} lead member(s), {n_guest} guest members from {len(teams_u)} teams and "
                  f"{len(seats_u)} guest(s) from {homes} in the Team table, {len(items)} fault lines with evidence from "
                  f"both sides, every guest team and guest seated and in a fault line")
    rep.add("team", "roundtable", not probs, "; ".join(probs) or detail)


def check_lead(rep: Report, team: Path, cfg: dict):
    """可选的团队总入口 skill（team.json 的 lead，如理事会的 optimization-lead：召集人领导各队，按问题分派、审各队答复）：
    SKILL.md 存在，frontmatter name = lead；正文链接圆桌、本队每位成员的 skill 和每个 guest 队的文件夹。没有 lead 不报。"""
    lead = cfg.get("lead")
    if not lead:
        return
    f = team / lead / "SKILL.md"
    if not f.exists():
        rep.add("team", "lead", False, f"{lead}/SKILL.md missing")
        return
    text = f.read_text(encoding="utf-8")
    probs = []
    m = re.search(r"^name:\s*(\S+)", text, re.M)
    if not m or m.group(1) != lead:
        probs.append(f"frontmatter name is {m.group(1) if m else 'missing'}, team.json says {lead}")
    if f"](../{cfg['roundtable']}/" not in text:
        probs.append(f"no link to the roundtable ../{cfg['roundtable']}/")
    probs += [f"no link to member ../{mm['slug']}/" for mm in cfg["members"] if f"](../{mm['slug']}/" not in text]
    probs += [f"no link into guest team ../../{g}/" for g in cfg.get("guest_teams") or [] if f"](../../{g}/" not in text]
    gs = cfg.get("guests") or []  # 客座：链到他 home 队的文件夹
    probs += [f"no link to guest ../../{g['home']}/{g['slug']}/" for g in gs if f"](../../{g['home']}/{g['slug']}/" not in text]
    rep.add("team", "lead", not probs, "; ".join(probs) or (
            f"{lead}: links the roundtable, {len(cfg['members'])} member skill(s), {len(cfg.get('guest_teams') or [])} "
            f"guest team(s) and {len(gs)} guest(s)" if gs else
            f"{lead}: links the roundtable, {len(cfg['members'])} member skill(s) and {len(cfg.get('guest_teams') or [])} guest team(s)"))


def check_guests(rep: Report, team: Path, cfg: dict):
    """team.json 有 guests 时的一项：每位客座能解析（new_team.resolve_guests）、SKILL.md 在他 home 队的文件夹里、
    ## Roundtable Card 的 7 项齐全（圆桌只读这张卡入座；缺了在 home 队修）。通过时列出每位客座的 home 与进度；
    撞姓只在说明里提一句，不判 ✗：有本队成员在内时建议先改本队成员的 surname，只是客座之间撞姓时在其中一位客座的
    home 队 team.json 里改（与 new_team.surname_clashes 相同）。成员级检查（quality、works、cards…）是 home 队的事，这里不跑。"""
    if not cfg.get("guests"):
        return
    guests, errs, _ = new_team.resolve_guests(cfg, teams_root(team))
    probs, done = list(errs), []
    for g in guests:
        skill = Path(g["_dir"]) / "SKILL.md"
        if not skill.is_file():
            probs.append(f"{g['slug']}: SKILL.md missing in {new_team.display(Path(g['_dir']))} (the home team's T1)")
            continue
        card = section(skill.read_text(encoding="utf-8"), "## Roundtable Card", re.compile(r"^## ", re.M))
        lost = [l for l in CARD_LABELS if l.lower() not in card.lower()]
        if not card:
            probs.append(f"{g['slug']}: no ## Roundtable Card in {new_team.display(skill)} (fix it in the home team)")
        elif lost:
            probs.append(f"{g['slug']}: Roundtable Card lacks {', '.join(lost)} in {new_team.display(skill)} "
                         "(fix it in the home team)")
        else:
            done.append(f"{g['slug']} ({g['_home']}, {new_team.guest_stage(g)})")
    by: dict[str, list[dict]] = {}
    for mm in cfg["members"] + guests:  # 与 new_team.surname_clashes 同一个 surname 规则与同样的修法
        by.setdefault((mm.get("surname") or new_team.surname_of(mm["name"])).strip().casefold(), []).append(mm)
    clashes = [f"{(v[0].get('surname') or new_team.surname_of(v[0]['name'])).strip()}: {', '.join(x['slug'] for x in v)} ("
               + ("rename the local member's surname first" if any(not x.get("_home") for x in v)
                  else "rename it in one guest's home team.json") + ")"
               for v in by.values() if len(v) > 1 and any(x.get("_home") for x in v)]
    detail = "; ".join(probs) or ", ".join(done)
    if clashes:
        detail += "; surname clash (warning): " + "; ".join(clashes)
    rep.add("team", "guests", not probs, detail)


def check_hosts(rep: Report, team: Path, cfg: dict):
    """只提示（—）：同级的别的团队在 team.json 的 guests 里请了本队成员作客座。改这些成员（T3.6 改方法名、T4、改 surname、
    移走）后，那几队的圆桌与 README 要重跑 team-layer.js / team-integrate.js。经 guest_teams 整队入座的不报。
    没有客座这个功能时，team_check.py 根本不读同级的文件夹，所以这里每一个都在 try 里查（stat 本身也在里面：Python 3.13
    的 is_dir / is_file 遇到 EACCES 照样抛 PermissionError，如 POSIX 上别人的 700 文件夹）；查不了、不是团队、team.json
    读不了或解析不了（不是 UTF-8、不是合法 JSON、嵌套太深）的跳过这一个，不让旁边的文件夹把本队的闸门弄停。"""
    mine = {m["slug"] for m in cfg["members"]}
    try:
        here = team.resolve()
        entries = sorted(teams_root(team).iterdir())
    except OSError:
        return
    hosts = []
    for d in entries:
        tj = d / "team.json"
        try:
            if not d.is_dir() or d.resolve() == here or not tj.is_file():
                continue
            other = json.loads(tj.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, ValueError, RecursionError):
            continue
        # 同级团队的 team.json 没经过 load_config：形状不对的项跳过（那队自己的闸门报），不让本队的闸门崩
        seated = [g["slug"] for g in new_team.guest_entries(other) if g.get("home") == cfg["team"] and g["slug"] in mine]
        if seated:
            hosts.append(f"{d.name} ({', '.join(seated)})")
    if hosts:
        rep.add("team", "hosts", None, f"seated as guest elsewhere: {'; '.join(hosts)}: rerun those teams' team-layer.js / "
                                       "team-integrate.js after changing these members")


def check_member(rep: Report, team: Path, m: dict, deep: bool, skip_quality: bool, st: dict):
    sk = team / m["slug"]
    skill = sk / "SKILL.md"
    scope = m["slug"]
    if not skill.exists():
        rep.add(scope, "skill", False, "SKILL.md missing (team-base-skills.js, T1)")
        return
    probs = []
    if not skip_quality:
        q = ts.quality(skill)
        if q != "12/12":
            probs.append(f"quality_check.py {q}")
    card = section(skill.read_text(encoding="utf-8"), "## Roundtable Card", re.compile(r"^## ", re.M))
    if not card:
        probs.append("no ## Roundtable Card")
    else:
        lost = [l for l in CARD_LABELS if l.lower() not in card.lower()]
        if lost:
            probs.append(f"Roundtable Card lacks: {', '.join(lost)}")
    rep.add(scope, "skill", not probs, "; ".join(probs) or ("12/12, Roundtable Card complete" if not skip_quality
                                                            else "Roundtable Card complete (quality check skipped)"))
    if not deep:
        return
    wj = sk / "references/sources/publications/works.json"
    if not wj.exists():
        rep.add(scope, "works", False, "publications/works.json missing (team-harvest.js, T3.1)")
    else:
        rc, out = run([sys.executable, str(HERE / "validate_works.py"), str(wj)])
        ok = rc == 0 and st["index_complete"]
        detail = last_line(out)
        if not st["index_complete"]:
            detail += (f"; INDEX.md has {st['indexed']} research rows, works.json {st['works_distinct_research']} distinct "
                       "(rerun acquire_fulltexts.py)" if st["index_exists"] else "; papers/INDEX.md missing (acquire_fulltexts.py)")
        rep.add(scope, "works", ok, detail)
    miss = [n for n, ok in (("07", st["has_07"]), ("08", st["has_08"]), ("09", st["has_09"]),
                            ("technique-catalog", st["has_catalog"])) if not ok]
    rep.add(scope, "cards", not st["unread"] and not miss and st["cards"] > 0,
            f"{st['cards']} cards, {st['unread']} unread INDEX rows" + (f"; missing {', '.join(miss)}" if miss else ""))
    txt = sk / "references/sources/papers/txt"
    have = len(list(txt.glob("*.txt"))) if txt.is_dir() else 0
    if st["full_text"] and not have:
        rep.add(scope, "quotes", None, f"no local txt/ ({st['full_text']} rows have text): run acquire_fulltexts.py first "
                                       "(PDFs and txt/ are git-ignored), then rerun")
    else:
        rc, out = run([sys.executable, str(HERE / "verify_card_quotes.py"), str(sk)])
        head = next((l for l in out.splitlines() if l.startswith("quotes:")), last_line(out))
        extra = f"; only {have} of {st['full_text']} texts on disk" if have < st["full_text"] else ""
        rep.add(scope, "quotes", rc == 0, head + extra)
    rc, out = run([sys.executable, str(HERE / "check_ledger.py"), str(sk)])
    rep.add(scope, "ledger", rc == 0, last_line(out))
    rc, out = run([sys.executable, str(HERE / "check_citations.py"), str(team), "--member", m["slug"], "--no-roundtable",
                   "--show-warnings", "0"])
    rep.add(scope, "citations", rc == 0, next((l.strip() for l in out.splitlines() if l.startswith(("✅", "❌")) and m["slug"] in l),
                                              last_line(out)))


def main():
    ap = argparse.ArgumentParser(description="研究团队交付闸门（一次跑完手册第四节的检查）")
    ap.add_argument("team_dir")
    ap.add_argument("--tier", choices=["auto", "base", "deep"], default="auto")
    ap.add_argument("--skip-quality", action="store_true", help="不跑 quality_check.py（更快）")
    ap.add_argument("--member", default="", help="成员级检查只查这几位（逗号分隔 slug）；团队级检查照常")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    team = Path(a.team_dir)
    if not (team / "team.json").exists():
        sys.exit(f"❌ {team}/team.json not found")
    cfg, errs = new_team.load_config(team / "team.json")
    rep = Report()
    rep.add("team", "team.json", not errs, "; ".join(errs) or f"{len(cfg['members'])} members"
            + (f", {len(cfg['guests'])} guests" if cfg.get("guests") else ""))
    if errs:
        print("\n".join(f"❌ {e}" for e in errs))
        sys.exit(1)
    only = [x for x in a.member.split(",") if x]
    unknown = [x for x in only if x not in {m["slug"] for m in cfg["members"]}]
    gh = {g["slug"]: g["home"] for g in cfg.get("guests") or []}
    if any(x in gh for x in unknown):  # 客座：成员级检查在他的 home 队跑
        sys.exit("❌ --member: " + "; ".join(
            f"{x} is a guest from {gh[x]}: per-member checks run in {new_team.display(teams_root(team) / gh[x])}" if x in gh
            else f"not in team.json: {x}" for x in unknown))
    if unknown:
        sys.exit(f"❌ --member: not in team.json: {', '.join(unknown)}")
    carded = {m["slug"] for m in cfg["members"] if any((team / m["slug"] / "references/research/cards").glob("*.digest.json"))}
    # auto：按成员判档——写了卡片的成员按深读档查，其余按轻量档查（混合档团队：只给部分成员做了深读）
    deep_members = {m["slug"] for m in cfg["members"]} if a.tier == "deep" else (carded if a.tier == "auto" else set())
    deep = bool(deep_members)
    tier_label = "base" if not deep else ("deep" if deep_members == {m["slug"] for m in cfg["members"]} else
                                          f"mixed (deep: {', '.join(sorted(deep_members))})")
    sts = {m["slug"]: ts.member_status(team, m, False) for m in cfg["members"]}

    check_guests(rep, team, cfg)
    check_hosts(rep, team, cfg)
    rc, out = run([sys.executable, str(HERE / "check_links.py"), str(team)])
    rep.add("team", "links", rc == 0, last_line(out))
    hits = []
    for f in sorted(team.rglob("*.md")):
        if "/private/" in f.as_posix() and f.name != "README.md":
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if "{{" in line or "[TODO" in line:
                hits.append(f"{f.relative_to(team)}:{n}")
    rep.add("team", "templates", not hits, f"{len(hits)} line(s) with {{{{ or [TODO: {', '.join(hits[:8])}"
            + (" …" if len(hits) > 8 else "") if hits else "no {{ and no [TODO left")
    rc, out = run(["git", "ls-files", "--", "."], cwd=team)
    if rc != 0:
        rep.add("team", "git", None, "not a git checkout")
    else:
        bad = [p for p in out.splitlines() if BAD_FILES.search("/" + p) and not p.endswith("/private/README.md")
               and not p.startswith("private/README.md")]
        rep.add("team", "git", not bad, f"tracked copyrighted or private files: {', '.join(bad[:8])}" if bad
                else "no PDF/PS/DjVu/EPUB, txt/ or private/ files tracked (private/README.md only)")
    readme = team / "README.md"
    rtext = readme.read_text(encoding="utf-8") if readme.exists() else ""
    unlinked = [m["slug"] for m in cfg["members"] if f"]({m['slug']}/" not in rtext]
    if not cfg.get("guests"):
        rep.add("team", "readme", readme.exists() and not unlinked,
                "README.md missing" if not readme.exists() else
                (f"member rows missing: {', '.join(unlinked)}" if unlinked else "links every member"))
    else:  # 客座的行链到他 home 队的文件夹
        g_unlinked = [g["slug"] for g in cfg["guests"] if f"](../{g['home']}/{g['slug']}/" not in rtext]
        missing = ([f"member rows missing: {', '.join(unlinked)}"] if unlinked else []) + \
            ([f"guest rows missing: {', '.join(g_unlinked)} (](../<home>/<slug>/…); new_team.py --add-guest)"] if g_unlinked else [])
        rep.add("team", "readme", readme.exists() and not missing,
                "README.md missing" if not readme.exists() else ("; ".join(missing) or "links every member and guest"))
    check_roundtable(rep, team, cfg, deep, deep_members)
    check_lead(rep, team, cfg)
    rc, out = run([sys.executable, str(HERE / "answer_standard.py"), "--check", str(team.resolve())])
    rep.add("team", "answer-std", rc == 0, last_line(out))
    # 有卡片的客座（在他 home 队的文件夹里）：圆桌里他那一方按卡片引用，轻量档团队也是（team-layer.js），
    # 所以本队成员都还没有卡片时，团队级的圆桌引用闭包也要跑（页码、版本、读到哪一级只有 check_citations.py 查）
    carded_guests = [g["slug"] for g in new_team.resolve_guests(cfg, teams_root(team))[0]
                     if new_team.guest_stage(g) == "cards present"] if cfg.get("guests") else []
    if deep and len(cfg["members"]) + len(cfg.get("guests") or []) < 2 and not cfg.get("guest_teams"):
        rep.add("team", "citations", None, "1 member: no roundtable to check (member citations are checked per member)")
    elif deep or carded_guests:
        rc, out = run([sys.executable, str(HERE / "check_citations.py"), str(team), "--roundtable", "--show-warnings", "0"])
        rep.add("team", "citations", rc == 0, next((l.strip() for l in out.splitlines() if l.startswith(("✅", "❌")) and "roundtable" in l),
                                                   last_line(out)))
    if deep:
        ordered = [sts[m["slug"]] for m in cfg["members"]]
        dr = team / "DEEP-READING.md"
        full, short = ts.coverage_md(ordered), ts.coverage_short_md(ordered)
        probs = []
        if not dr.exists() or full not in dr.read_text(encoding="utf-8"):
            probs.append("DEEP-READING.md does not contain the table of team_status.py --coverage verbatim")
        flat = "\n".join(l.strip() for l in rtext.splitlines())  # the summary may sit indented inside a bullet
        if short not in flat:
            probs.append("README.md does not contain the table of team_status.py --coverage --short verbatim")
        rep.add("team", "coverage", not probs, "; ".join(probs) or "DEEP-READING.md and README.md match team_status.py")
    for m in cfg["members"]:
        if not only or m["slug"] in only:
            check_member(rep, team, m, m["slug"] in deep_members, a.skip_quality, sts[m["slug"]])

    if a.json:
        print(json.dumps({"team": cfg["team"], "tier": tier_label, "checks": rep.rows,
                          "failed": len(rep.failed)}, ensure_ascii=False, indent=1))
    else:
        mark = {"pass": "✓", "fail": "✗", "skip": "—"}
        print(f"team_check {team} · {tier_label} tier")
        for r in rep.rows:
            print(f"  {mark[r['status']]} {r['scope']:<22} {r['check']:<11} {r['detail']}")
        n = len(rep.failed)
        skipped = sum(1 for r in rep.rows if r["status"] == "skip")
        print(f"{'❌' if n else '✅'} {len(rep.rows)} checks: {n} failed, {skipped} skipped")
    sys.exit(1 if rep.failed else 0)


if __name__ == "__main__":
    main()
