#!/usr/bin/env python3
"""
新建研究团队（多位研究者的研究Skill + 圆桌）：起草 team.json，按模板铺团队目录，或给已有团队加成员。

七种用法:
    1) 起草 team.json（schema 1）
       python3 new_team.py --init <团队slug> --field "..." --members "Name One;Name Two" [--title "..."]
                           [--language English] [--out PATH] [--force] [--guests "home/slug;home/slug"]
       成员 slug 由姓名生成（去重音、小写、非字母数字变 -；中文名保留原字），surname 取最后一个词（跳过 Jr./II 等），
       scholar / dblp / orcid / homepage / hint 留空，living=true，student_mode=false，created=今天，
       roundtable=<去掉 -team 的团队slug>-roundtable。默认写到 <--root>/<团队slug>/team.json，已存在不覆盖（--force 覆盖）。
       --guests：别队的成员作客座，写成紧跟 members 的 "guests"（逐位到 <--root>/<home>/ 解析，出错什么都不写）；
       不给 --guests 就不写这个键。填好 scholar id 和 hint 后做第 2 步。

    2) 按 team.json 铺团队目录
       python3 new_team.py <team.json> [--root DIR] [--templates DIR] [--force] [--dry-run] [--base-tier] [--set NAME=VALUE]...
       --root 默认 <仓库>/product，团队目录 = <--root>/<team.json 的 team>；--templates 默认 <仓库>/references/team-templates。
       生成（与 product/dfo-team/ 相同的布局）:
           <团队>/team.json                                       复制进来
           <团队>/README.md                                       ← team-README.md
           <团队>/DEEP-READING.md                                 ← DEEP-READING.md（标为未开始）
           <团队>/<roundtable>/SKILL.md                           ← roundtable-SKILL.md
           <团队>/<成员>/references/research/                     空目录（.gitkeep）；01–06 调研笔记由 T1 写
           <团队>/<成员>/references/sources/RESOURCES.md          ← member-RESOURCES.md
           <团队>/<成员>/references/sources/{publications,papers,talks,essays,software}/   空目录（.gitkeep）
           <团队>/<成员>/references/sources/private/README.md     ← private-README.md（private/ 其余内容被 git 忽略）
       成员的 SKILL.md 不生成（T1 写）。已存在的文件一律保留，--force 才覆盖；重跑只补缺的部分。
       --base-tier：确定只做轻量档（不深读）时用。DEEP-READING.md 换成模板开头注释里的两段轻量档说明；
       RESOURCES.md 删掉深读档占位行（第 3 行），第 1 行的 Notes 写 "not harvested (base tier)"、没有 Scholar id 时
       Link 写 "—"。其余 TODO 照旧由 team-layer.js（deep_tier: false）处理。

    3) 给已有团队加成员（先把他写进团队目录里的 team.json 的 members）
       python3 new_team.py <team.json> --add-member <slug> [--add-member <slug>]... [--root DIR] [--templates DIR] [--force] [--dry-run] [--base-tier]
       只铺这位成员的目录，并把他的一行插进 README.md 的成员表：有 <!-- members:start --> / <!-- members:end -->
       标记时把 {{MEMBER_TABLE}} 格式的一行插在 end 标记前；没有标记时照最后一个链接到成员文件夹的表格行造一行
       （同样的列数，slug / 姓名换成新成员，其余格 [TODO]）插在它后面；都找不到就在文末追加一条 [TODO]。
       圆桌 SKILL.md 和 DEEP-READING.md 不改，只在「下一步」里提醒。

    4) 改 team.json 里某位成员的字段（harvest 找到的 Scholar id、DBLP pid 等，不用手改 JSON）
       python3 new_team.py <team.json> --set-member <slug> KEY=VALUE [KEY=VALUE]... [--dry-run]
       KEY 是成员字段（scholar、dblp、orcid、homepage、hint、surname、family_name、living、student_mode、chase_hints）；
       living / student_mode 取 true/false，chase_hints 取 JSON 列表。只改这一位的这些字段，其余原样保留。

    5) 从 DBLP 补全成员的 dblp / orcid / homepage（只补空着的字段；要联网，走 sparql.dblp.org）
       python3 new_team.py <team.json> --lookup [--member slug,slug] [--dry-run]
       有 scholar id 时按 DBLP 人物页登记的 Scholar 链接找（唯一匹配才填，可靠）；找不到再按 orcid 找；
       都找不到时按姓名找，只有唯一一个完全同名的候选才填，并提示对照 hint 核对（同名的人很常见）。

    6) 给已有团队加客座（先把 {"slug": …, "home": …} 写进团队目录里的 team.json 的 guests）
       python3 new_team.py <team.json> --add-guest <slug> [--add-guest <slug>]... [--root DIR] [--dry-run]
       只把这位客座的一行（{{MEMBER_TABLE}} 的客座行格式）插进 README.md 成员表最后一个成员行或客座行后面
       （认 ](../<home>/<slug>/ 形式的链接；已有就保留、报「已有 <slug> 的行」；找不到表格行就在文末追加一条 [TODO]）。
       团队还没铺（没有 README.md）时报错退出 1：先不带 --add-guest 铺目录（guests 里有客座因主队的分支还没合进来而解析
       不了时铺目录也会停，这条报错就写明先把他们留在 guests 外面铺、等他们能解析了再加回来跑 --add-guest；就地能改的客座错误不给这句，
       见下面「客座」一节）。只有要加的这几位解析不了才停；guests 里别的客座解析不了只提示（⚠️；team_check.py 的 guests
       一项照样判 ✗，--guest-text 和 make_args.mjs 照样停）。
       不建任何文件夹；圆桌 SKILL.md 和 DEEP-READING.md 不改，「下一步」写 T2 何时跑，并列出按客座名单渲染、
       这一步没改的句子（README 的客座子句与两种 shell 的安装行；圆桌的 description、Members: 一行、免责声明、
       Loading the Team 的解析句、卡片位置句；DEEP-READING.md 的客座指引），逐字的新文本见第 7 种用法。

    7) 打印客座的渲染文本（只读，给 T2 / T3.8 的 agent 照抄）
       python3 new_team.py <team.json> --guest-text [--root DIR]
       stdout 是一个 JSON 对象（UTF-8，indent=1）：guests（每位 {slug, home, name, home_title, dir}；dir 在默认 --root 时
       是 product/<home>/<slug>，否则是显示路径）、SEATED_LIST、GUEST_CLAUSE、GUEST_INSTALL、GUEST_INSTALL_PS、
       GUEST_RESOLUTION、GUEST_CARDS、GUEST_SEATS_TODO、GUEST_DEEP_READING、README_GUEST_ROWS、ROUNDTABLE_GUEST_ROWS，
       与铺目录时渲染的逐字相同。解析提示打到 stderr；有客座解析不了时把错误（与铺目录时同样的句子）打到 stderr、
       退出码 1。没有客座时 GUEST_* 是空串、两个列表为空，退出码 0。不能和 --init、--guests、--add-member、--add-guest、
       --set-member、--lookup、--set、--force、--base-tier 同用（--dry-run 无害，照收）。

客座（team.json 可选键 guests: [{"slug": "<别队成员的 slug>", "home": "<那队的文件夹名>"}]）:
    别队（<--root>/<home>/）的单个成员坐进本队的圆桌和 README；他的 skill 只有一份，留在 home 队。每项只有 slug、home
    两个字符串键；姓名、surname、living、student_mode、hint 等都从 <home>/team.json 里他的成员条目原样读（那里缺的键
    就缺着，不补默认值）。load_config 只查形状（slug 在 guests 里唯一，不同于成员、roundtable、lead；home 不是本队、
    不在 guest_teams 里）；resolve_guests() 读 home 的 team.json（不解析它自己的 guests，不递归）：home 的 team.json
    找不到、team 字段不等于 home、slug 不是那队的成员（客座的客座不行；只差大小写时问 did you mean）、<home>/<slug>/
    不存在、本队目录里有同名的影子文件夹，都算错误（写明修法），铺目录（和 --init --guests）什么都不写；只因客座解析不了
    而停下、而且每条客座错误都是等合并的那三种（home 的 team.json 找不到；slug 不是那队的成员，也没有只差大小写的；
    <home>/<slug>/ 不存在）时，最后一句提示可以先把这几位留在 guests 外面铺本队成员，等他们能解析了（主队的分支在它的
    T1 写出 SKILL.md 之后合进来）再写回 guests、跑 --add-guest；有一条只差大小写、客座的客座、影子副本、home 的 team.json
    不合法或写的是别队的错误时不给这句（错误行自己写了修法）。不跑 load_config 的脚本（team_status.py、check_citations.py）
    读到的形状问题、home 是本队、slug 也是本队成员，resolve_guests 先按这些原因报。还没有 SKILL.md（home 队的 T1）只提示；
    他的文件夹里已有调研笔记（home 队的 T1 已经开始）或没有 references/research/（new_team.py 铺的成员文件夹都有）时，
    提示和「下一步」都说明 check_links.py 把 README 指向他 SKILL.md 的链接算坏链（不是 pending），要等 home 队的 T1
    写出 SKILL.md 再合并。本队不给客座建文件夹、RESOURCES.md 或 private/；客座的 T1、T3、T4
    在 home 队跑。surname 撞姓检查覆盖成员 + 客座（仍只警告）。team_check.py、team_status.py、check_citations.py
    到 teams_root(团队目录) 里解析（团队目录绝对路径的上级，不跟随链接：给的是 . 或相对路径时也对）。
    seated_guests() 给出圆桌的入座单位（guest_teams 的每一队 + guests 的每一位），team_check.py 用全部；check_citations.py
    只用 guests 的部分（teams=False），guest_teams 照加客座之前的写法自己读（那队的 team.json 不合法时停下）。
    guest_entries() 给没先跑 load_config 就读 guests 的地方（check_citations.py、team_status.py、team_check.py 的 hosts 一项
    读同级团队的 team.json）：slug 不是字符串的项跳过、guests 不是列表时为空，不抛异常。

模板占位符（简单字符串替换，{{NAME}}）:
    团队级   {{TEAM_SLUG}} {{TEAM_TITLE}} {{FIELD}} {{LANGUAGE}} {{DATE}}（今天） {{ROUNDTABLE_SLUG}}
             {{MEMBER_TABLE}}（每位成员一行 | [Name](slug/SKILL.md) | lens: [TODO] | 状态 |；
                 有客座时成员行之后每位客座一行 | [Name](../<home>/<slug>/SKILL.md) | lens: [TODO] | guest from [<home 队 title>](../<home>/README.md) · 状态 |）
             {{ROUNDTABLE_MEMBER_TABLE}}（圆桌 Team 表：每位成员一行 | `slug` | Name | [TODO: 一行 lens …] |；
                 成员行之后每位客座一行 | `slug` | Name (guest from <home 队 title>) | [TODO: …] |）
             {{MEMBER_LIST}}（逗号分隔的成员姓名，不含客座） {{MEMBER_COUNT}}（成员数）
             {{SEATED_LIST}}（{{MEMBER_LIST}} + 客座姓名，在 --set 之后接，--set MEMBER_LIST 也算进来；没有客座时 = {{MEMBER_LIST}}。
                 有客座时 T2 照 --guest-text 的 SEATED_LIST 重写圆桌的 description 与免责声明，而 --guest-text 按 team.json 的
                 姓名算、不收 --set，所以铺目录时用 --set 改的 MEMBER_LIST / SEATED_LIST 在这两处留不过 T2）
             客座子句（都接在模板已有行的末尾；没有客座时全是空串，不给输出添任何字符）:
             {{GUEST_CLAUSE}}（", with guests A and B from the <home 队 title> (…)"）
             {{GUEST_INSTALL}}（每支 home 队一行注释，其下每位客座一行 cp -r）
             {{GUEST_INSTALL_PS}}（同样分行，每位客座一行 PowerShell 的 Copy-Item；两段的注释行相同，单独成行、不含 ; ( )，
                 粘进默认设置的 zsh 也不坏："# guest(s) from the <home 队 title>: if this checkout holds git-ignored full
                 texts, copy only git-tracked files, see product/README.md"）
             {{GUEST_RESOLUTION}}（圆桌：客座 SKILL.md 的解析顺序） {{GUEST_CARDS}}（圆桌：客座的卡片在哪）
             {{GUEST_SEATS_TODO}}（圆桌：每位客座一条 Guest seat 说明的 [TODO]，T2 写）
             {{GUEST_DEEP_READING}}（DEEP-READING.md：客座在 home 队深读，链到那队的 DEEP-READING.md；--base-tier 时
                 接在轻量档说明那一段的末尾，模板开头注释里的那段本身不带它）
    成员级   以上全部，加 {{MEMBER_NAME}} {{MEMBER_SLUG}} {{MEMBER_SURNAME}}
             {{SCHOLAR_URL}}（https://scholar.google.com/citations?user=<id>&hl=en；没有 id 时为
             "— (no Scholar profile in team.json; list from DBLP/homepage)"，--base-tier 时为 "—"）
    --set NAME=VALUE 可补充或覆盖。模板里出现未知占位符或落单的 {{ 算错误：列出来，一个文件也不写。
    需要研究才能填的内容在模板里写成 [TODO: …]，`grep -rn "TODO" product/<团队>` 列出所有待办。

输出:
    逐行列出 + 新建 / = 已存在保留 / ! 覆盖 / ~ 更新（加成员时的 README），每个写入的文件后标 [TODO 数；
    两位成员、成员与客座或两位客座 surname 相同（圆桌的 [Surname lens]、@Surname 会撞）时警告；客座的解析提示照印；
    用 git check-ignore 检查成员 references/sources/ 下的 PDF/PS/DjVu/EPUB、papers/txt/ 和 private/ 是否被忽略，
    没覆盖时打印要加进仓库根 .gitignore 的几行（与本仓库 .gitignore 里的写法相同）；最后打印「下一步」。
    最后一行汇总 ✅/❌；team.json 不合法、模板缺失或占位符有误时退出码 1，什么都不写。

示例:
    python3 scripts/new_team.py --init bo-team --field "Bayesian optimization" --members "Peter Frazier;Roman Garnett"
    python3 scripts/new_team.py product/bo-team/team.json
    python3 scripts/new_team.py product/bo-team/team.json --add-member andreas-krause
    python3 scripts/new_team.py product/milp-team/team.json --add-guest robert-e-bixby     # guests 里写了 {"slug": "robert-e-bixby", "home": "lp-team"}
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DEFAULT_ROOT = REPO / "product"
DEFAULT_TEMPLATES = REPO / "references" / "team-templates"

TEAM_TEMPLATES = [("team-README.md", "README.md"), ("DEEP-READING.md", "DEEP-READING.md"),
                  ("roundtable-SKILL.md", "{roundtable}/SKILL.md")]
MEMBER_TEMPLATES = [("member-RESOURCES.md", "references/sources/RESOURCES.md"),
                    ("private-README.md", "references/sources/private/README.md")]
MEMBER_DIRS = ["references/research"] + [f"references/sources/{d}" for d in
                                         ("publications", "papers", "talks", "essays", "software")]
MARK_START, MARK_END = "<!-- members:start -->", "<!-- members:end -->"
IGNORED_PROBES = ["references/sources/papers/x.pdf", "references/sources/papers/X.PDF", "references/sources/papers/x.ps",
                  "references/sources/papers/x.ps.gz", "references/sources/papers/x.djvu", "references/sources/talks/x.pdf",
                  "references/sources/essays/x.epub", "references/sources/papers/txt/x.txt",
                  "references/sources/private/x.md"]
TRACKED_PROBES = ["references/sources/private/README.md", "references/sources/RESOURCES.md",
                  "references/sources/papers/INDEX.md"]
# 仓库根 .gitignore 里的同一组规则（前面加团队目录的上级，如 product/）；没覆盖时原样打印这几行
GITIGNORE_RULES = ["**/references/sources/**/*.[pP][dD][fF]", "**/references/sources/**/*.[pP][sS]",
                   "**/references/sources/**/*.[pP][sS].[gG][zZ]", "**/references/sources/**/*.[dD][jJ][vV][uU]",
                   "**/references/sources/**/*.[eE][pP][uU][bB]", "**/references/sources/papers/txt/",
                   "**/references/sources/private/*", "!**/references/sources/private/README.md"]
NO_SCHOLAR = "— (no Scholar profile in team.json; list from DBLP/homepage)"
CARD_DIMS = [f"D{i}" for i in range(1, 9)]
MEMBER_STR_KEYS = ("surname", "family_name", "hint", "scholar", "dblp", "orcid", "homepage")
BASE_TIER_NOTES = "not harvested (base tier)"

PLACEHOLDER_RE = re.compile(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}")
SAFE_SLUG_RE = re.compile(r"^\w[\w.-]*$")
NAME_SUFFIXES = {"jr", "jr.", "sr", "sr.", "ii", "iii", "iv"}
TRANSLIT = str.maketrans({"ł": "l", "Ł": "L", "ø": "o", "Ø": "O", "đ": "d", "Đ": "D", "ı": "i", "ß": "ss",
                          "æ": "ae", "Æ": "AE", "œ": "oe", "Œ": "OE", "þ": "th", "ð": "d"})


def display(p: Path) -> str:
    try:
        rel = os.path.relpath(p.resolve())
    except ValueError:  # Windows：路径与当前目录不在同一个盘符上（team_check 等经 resolve_guests 也会用到）
        return p.resolve().as_posix()
    return p.resolve().as_posix() if rel.startswith("..") else Path(rel).as_posix()


def same_path(a: Path, b: Path) -> bool:
    return a.resolve() == b.resolve()


def teams_root(team_dir: Path) -> Path:
    """放各团队目录的文件夹（如 product/）= 团队目录绝对路径的上级。os.path.abspath 只按字面折叠 . 和 ..、不跟随链接
    （与 make_args.mjs 的 path.resolve 相同），所以团队目录给的是 . 或 ./x 时也对（Path('.').parent 还是 .），团队目录本身
    是指向别处的链接（junction、symlink）时，别队仍在它所在的文件夹里找，与加客座之前的 team.parent 相同。"""
    return Path(os.path.abspath(team_dir)).parent


def today() -> str:
    return datetime.date.today().isoformat()


# ---------- --init ----------

def slugify(name: str) -> str:
    words = name.split()
    while len(words) > 1 and words[-1].strip(",").lower() in NAME_SUFFIXES:
        words.pop()
    s = unicodedata.normalize("NFKD", " ".join(words).translate(TRANSLIT))
    s = "".join(c for c in s if not unicodedata.combining(c)).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    if not slug:                                          # 中文等非拉丁姓名：保留原字
        slug = re.sub(r"[^\w]+", "-", unicodedata.normalize("NFKC", name).lower()).strip("-_")
    return slug


def surname_of(name: str) -> str:
    words = [w.strip(",") for w in name.split() if w.strip(",")]
    while len(words) > 1 and words[-1].lower() in NAME_SUFFIXES:
        words.pop()
    return words[-1] if words else name


def default_title(team: str) -> str:
    return " ".join(w.upper() if len(w) <= 3 else w.capitalize() for w in re.split(r"[-_]+", team) if w)


def surname_clashes(members: list) -> list[str]:
    """surname 相同（不分大小写）的成员：圆桌用 [Surname lens]、@Surname 称呼成员，同姓会分不清。
    也可以传成员 + 解析后的客座（resolve_guests 的条目，带 _home、_dir）：客座的 surname 在 home 队的 team.json 里，
    改它会连带改那队圆桌的称呼，所以建议先改本队成员的 surname。仍然只是警告。"""
    by: dict[str, list[tuple[dict, str]]] = {}
    for m in members:
        if isinstance(m, dict) and isinstance(m.get("name"), str) and m.get("name").strip():
            sur = (m.get("surname") or surname_of(m["name"])).strip()
            by.setdefault(sur.casefold(), []).append((m, sur))
    out = []
    for v in by.values():
        if len(v) < 2:
            continue
        labels = [f"{m.get('slug') or m['name']} ({sur})" for m, sur in v]
        if not any(m.get("_home") for m, _ in v):
            out.append(f"⚠️ surname 重复：{', '.join(labels)}。圆桌的 [Surname lens] 与 @Surname 会撞；在 team.json 里把 surname 改成"
                       f"能区分的写法（如 \"M. Smith\" / \"J. Smith\"），工作流和圆桌都用这个字段")
            continue
        labels = [f"{m.get('slug') or m['name']} ({sur}；客座，surname 在 {display(Path(m['_dir']).parent / 'team.json')})"
                  if m.get("_home") else lab for (m, sur), lab in zip(v, labels)]
        fix = ("先改本队成员在 team.json 里的 surname（如 \"M. Smith\" / \"J. Smith\"）" if any(not m.get("_home") for m, _ in v)
               else "只能在其中一位客座的 home 队 team.json 里改 surname")
        out.append(f"⚠️ surname 重复：{', '.join(labels)}。圆桌的 [Surname lens] 与 @Surname 会撞；{fix}："
                   f"客座的 surname 改了会连带改他 home 队圆桌的 [Surname lens] 与 @Surname")
    return out


def init_team(a) -> int:
    team = a.init
    if not SAFE_SLUG_RE.match(team) or ".." in team:
        print(f"❌ 团队 slug 只能用字母、数字、- _ .：{team!r}")
        return 1
    names = [n.strip() for n in re.split(r"[;\n]", a.members or "") if n.strip()]
    if not names:
        print('❌ --members 为空（用分号分隔："Name One;Name Two"）')
        return 1
    for n in sorted({n for n in names if names.count(n) > 1}):
        print(f"⚠️ {n!r} 出现了 {names.count(n)} 次（同名的不同研究者要靠 hint 区分，否则删掉重复）")
    base = team[:-5] if team.endswith("-team") and len(team) > 5 else team
    roundtable = f"{base}-roundtable"
    members, used = [], {roundtable}
    for n in names:
        slug = slugify(n) or "member"
        s, k = slug, 2
        while s in used:
            s, k = f"{slug}-{k}", k + 1
        used.add(s)
        members.append({"slug": s, "name": n, "surname": surname_of(n), "living": True, "hint": "",
                        "scholar": "", "dblp": "", "orcid": "", "homepage": "", "chase_hints": [],
                        "student_mode": False})
    cfg = {"schema": 1, "team": team, "title": a.title or default_title(team), "field": a.field,
           "language": a.language, "created": today(), "roundtable": roundtable, "chase_hints": [],
           "card_dimensions": {}, "members": members}
    guests = []
    if a.guests is not None:  # 客座：别队的成员，"home/slug;home/slug"，写成紧跟 members 的 guests
        cfg["guests"], errs = [], []
        for spec in [x.strip() for x in re.split(r"[;\n]", a.guests) if x.strip()]:
            home, sep, slug = (p.strip() for p in spec.partition("/"))
            if not sep or not home or not slug or "/" in slug:
                errs.append(f"--guests {spec!r} 应写成 home/slug（home 是那队的文件夹名，如 lp-team/qi-huangfu）")
            else:
                cfg["guests"].append({"slug": slug, "home": home})
        if not cfg["guests"] and not errs:
            errs.append('--guests 为空（用分号分隔："lp-team/slug-one;lp-team/slug-two"）')
        errs += guest_shape_errors(cfg)
        notes, stop = [], []
        if not errs:
            guests, rerrs, notes = resolve_guests_by_slug(cfg, Path(a.root))
            errs = [guest_msg(s, why) for s, why, _ in rerrs]
            stop = merge_pending_stop(rerrs)
        twice = [f"{m['name']} ({m['slug']} / {g['_home']}/{g['slug']})" for m in members for g in guests
                 if m["name"].casefold() == str(g.get("name") or "").casefold()]
        errs += [f"{t} 既在 --members 又是客座：同一个人只能是一队的成员、别队的客座" for t in twice]
        if errs:
            for e in errs:
                print(f"❌ {e}")
            if stop and not twice:  # 只因等合并的客座解析不了而停下（merge_pending_stop）
                print(guest_stop_hint(stop, init=True, every_guest={g["slug"] for g in cfg["guests"]} <= set(stop)))
            print(f"❌ --guests 有 {len(errs)} 处问题，什么都没写")
            return 1
        for n in notes:
            print(n)
    for w in surname_clashes(members + guests):
        print(w)
    out = Path(a.out) if a.out else Path(a.root) / team / "team.json"
    if out.exists() and not a.force:
        print(f"❌ {display(out)} 已存在，未覆盖（--force 覆盖）")
        return 1
    if a.dry_run:
        print(json.dumps(cfg, ensure_ascii=False, indent=1))
        print(f"✅ (dry run) 会写 {display(out)}（{len(members)} 位成员" + (f" + {len(guests)} 位客座" if guests else "") + "）")
        return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("| slug | name | surname |\n|---|---|---|")
    for m in members:
        print(f"| {m['slug']} | {m['name']} | {m['surname']} |")
    for g in guests:
        print(f"| {g['slug']} | {g['name']} (guest from {g['_home']}) | {g.get('surname') or surname_of(g['name'])} |")
    print(f"roundtable: {roundtable}")
    print()
    print("下一步:")
    print(f"  1. 编辑 {display(out)}：每位成员填 scholar（Google Scholar 主页网址 citations?user=<id> 里的 id）、")
    print("     hint（单位、年代、代表作；harvest 与检索靠它区分同名者）、能找到的 dblp / orcid / homepage；")
    print("     核对 slug（会成为文件夹名）、surname、living、student_mode；按需写团队级与个人级 chase_hints（开放仓库线索）。")
    print("     没有 Scholar 主页的人 scholar 留空（harvest 先按姓名搜一次，再以 DBLP/主页为主列表）；")
    print(f"     python3 {display(HERE / 'new_team.py')} {display(out)} --lookup 可从 DBLP 补 dblp / orcid / homepage。")
    print("     领域不是数学/计算类时，填 card_dimensions（D3–D5 在这个领域指什么，见 team-templates/team.example.json）。")
    if guests:
        print(f"     客座 {', '.join(g['slug'] for g in guests)} 只写 slug 和 home：他们的姓名、surname、scholar、hint 等在 home 队的"
              f" team.json 里，T1、T3、T4 也在 home 队跑。")
    if guests and not 3 <= len(members) + len(guests) <= 6:
        print(f"     注意：现在 {len(members) + len(guests)} 个席位（{len(members)} 位成员 + {len(guests)} 位客座）；"
              f"3–6 位视角互补、有公开分歧的研究者最合适。")
    elif not guests and not 3 <= len(members) <= 6:
        print(f"     注意：现在 {len(members)} 位；3–6 位视角互补、有公开分歧的研究者最合适。")
    root_opt = "" if same_path(Path(a.root), DEFAULT_ROOT) else f" --root {display(Path(a.root))}"
    print(f"  2. python3 {display(HERE / 'new_team.py')} {display(out)}{root_opt}      # 按模板铺团队目录"
          f"（确定只做轻量档、不深读时加 --base-tier）")
    print(f"  3. 然后按 {display(REPO / 'references/research-team-playbook.md')} 往下走"
          f"（T1: {display(HERE / 'workflows/team-base-skills.js')}，启动方式见 {display(HERE / 'workflows/README.md')}）。")
    print(f"✅ wrote {display(out)} ({len(members)} members" + (f" + {len(guests)} guests" if guests else "") + ")")
    return 0


# ---------- team.json ----------

def load_config(path: Path) -> tuple[dict | None, list[str]]:
    try:
        cfg = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        return None, [f"{display(path)}: 读不了 JSON：{e}"]
    errs = []
    if not isinstance(cfg, dict):
        return None, [f"{display(path)}: 顶层必须是对象"]
    if cfg.get("schema") != 1:
        errs.append(f"schema 必须是 1（现在是 {cfg.get('schema')!r}）")
    for key in ("team", "title", "field", "roundtable"):
        if not isinstance(cfg.get(key), str) or not cfg.get(key).strip():
            errs.append(f"缺 {key}（非空字符串）")
    for key in ("team", "roundtable"):
        v = cfg.get(key)
        if isinstance(v, str) and v and (not SAFE_SLUG_RE.match(v) or ".." in v):
            errs.append(f"{key} {v!r} 不能当文件夹名（只用字母、数字、- _ .）")
    lead = cfg.get("lead")  # 可选：团队总入口 skill 的文件夹名（如理事会的 optimization-lead），team_check 查它
    if lead is not None:
        if not isinstance(lead, str) or not SAFE_SLUG_RE.match(lead) or ".." in lead:
            errs.append(f"lead {lead!r} 不能当文件夹名（只用字母、数字、- _ .）")
        elif lead == cfg.get("roundtable") or lead in {m.get("slug") for m in cfg.get("members") or [] if isinstance(m, dict)}:
            errs.append(f"lead {lead!r} 与 roundtable 或某位成员的 slug 同名")
    members = cfg.get("members")
    if not isinstance(members, list) or not members:
        errs.append("members 必须是非空列表")
        members = []
    seen = set()
    for i, m in enumerate(members):
        if not isinstance(m, dict):
            errs.append(f"members[{i}] 不是对象")
            continue
        slug, name = m.get("slug"), m.get("name")
        where = f"members[{i}]" + (f" ({slug})" if isinstance(slug, str) else "")
        if not isinstance(slug, str) or not SAFE_SLUG_RE.match(slug) or ".." in slug:
            errs.append(f"{where}: slug {slug!r} 不能当文件夹名")
        elif slug in seen:
            errs.append(f"{where}: slug 重复")
        elif slug == cfg.get("roundtable"):
            errs.append(f"{where}: slug 与 roundtable 同名")
        seen.add(slug)
        if not isinstance(name, str) or not name.strip():
            errs.append(f"{where}: 缺 name")
        for key in MEMBER_STR_KEYS:
            if key in m and not isinstance(m[key], str):
                errs.append(f"{where}: {key} 必须是字符串")
        for key in ("living", "student_mode"):
            if key in m and not isinstance(m[key], bool):
                errs.append(f"{where}: {key} 必须是 true/false")
        if "chase_hints" in m and not (isinstance(m["chase_hints"], list) and all(isinstance(x, str) for x in m["chase_hints"])):
            errs.append(f"{where}: chase_hints 必须是字符串列表")
    errs += guest_shape_errors(cfg)
    if "chase_hints" in cfg and not (isinstance(cfg["chase_hints"], list) and all(isinstance(x, str) for x in cfg["chase_hints"])):
        errs.append("chase_hints 必须是字符串列表")
    cd = cfg.get("card_dimensions")
    if cd is not None and not (isinstance(cd, dict) and all(k in CARD_DIMS and isinstance(v, str) for k, v in cd.items())):
        errs.append(f"card_dimensions 必须是对象，键只能是 {'/'.join(CARD_DIMS)}，值是字符串（这个领域里该维度指什么）")
    sl = cfg.get("source_labels")
    if sl is not None and not (isinstance(sl, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in sl.items())):
        errs.append('source_labels 必须是 {"网址关键词": "来源标签"} 形式的对象')
    return cfg, [f"{display(path)}: {e}" for e in errs]


# ---------- 客座（team.json 的 guests：别队的单个成员坐进本队的圆桌与 README） ----------

def guest_shape_errors(cfg: dict) -> list[str]:
    """guests（可选）只查形状，不读别的文件：[{"slug": …, "home": …}]，每项只有这两个字符串键。"""
    gs = cfg.get("guests")
    if gs is None:
        return []
    if not isinstance(gs, list):
        return ['guests 必须是列表：[{"slug": "<home 队成员的 slug>", "home": "<home 队的文件夹名>"}]']
    errs = []
    member_slugs = {m.get("slug") for m in (cfg.get("members") if isinstance(cfg.get("members"), list) else [])
                    if isinstance(m, dict)}
    guest_teams = cfg.get("guest_teams") if isinstance(cfg.get("guest_teams"), list) else []
    seen = set()
    for i, g in enumerate(gs):
        if not isinstance(g, dict) or set(g) != {"slug", "home"} or not all(isinstance(v, str) for v in g.values()):
            errs.append(f"guests[{i}] 必须是只有 slug、home 两个字符串键的对象（姓名、surname 等从 home 队的 team.json 读）")
            continue
        slug, home = g["slug"], g["home"]
        where = f"guests[{i}] ({slug})"
        if not SAFE_SLUG_RE.match(slug) or ".." in slug:
            errs.append(f"{where}: slug {slug!r} 不能当文件夹名")
        elif slug in seen:
            errs.append(f"{where}: slug 重复")
        elif slug in member_slugs:
            errs.append(f"{where}: 也写在本队 members 里（一个人只能是一队的成员、别队的客座）")
        elif slug == cfg.get("roundtable"):
            errs.append(f"{where}: slug 与 roundtable 同名")
        elif slug == cfg.get("lead"):
            errs.append(f"{where}: slug 与 lead 同名")
        seen.add(slug)
        if not SAFE_SLUG_RE.match(home) or ".." in home:
            errs.append(f"{where}: home {home!r} 不能当文件夹名")
        elif home == cfg.get("team"):
            errs.append(f"{where}: home 是本队（本队的人写进 members）")
        elif home in guest_teams:
            errs.append(f"{where}: home {home!r} 已在 guest_teams 里（那队整队都已入座）")
    return errs


def guest_entries(cfg) -> list[dict]:
    """guests 里 slug 是字符串的项（对象），给没先跑 load_config 的读者用（check_citations.py、team_status.py，
    team_check.py 读同级团队的 team.json）：形状不对不抛异常，跳过那一项，guests 不是列表时为空；
    原因由 load_config（guest_shape_errors）报。"""
    gs = cfg.get("guests") if isinstance(cfg, dict) else None
    return [g for g in gs if isinstance(g, dict) and isinstance(g.get("slug"), str)] if isinstance(gs, list) else []


def _home_team(root: Path, home: str) -> tuple[dict | None, str, bool]:
    """root/<home>/team.json：(cfg, "", False) 或 (None, 原因与修法, 等合并)。等合并只在 team.json 找不到时为 True
    （多半是主队的分支还没合进来）；读不了、不合法、team 字段写的是别队时为 False（在 home 队里改）。
    只查形状（load_config），不解析它自己的 guests。"""
    hj = root / home / "team.json"
    if not hj.is_file():
        return None, f"{display(hj)} not found (is the home team's branch merged here?)", True
    hcfg, herrs = load_config(hj)
    if hcfg is None or herrs:
        return None, f"{herrs[0]} (fix it in the home team first)", False
    if hcfg["team"] != home:
        return None, (f"{display(hj)} says team {hcfg['team']!r}, not {home!r}: home must be the home team's folder name "
                      f"and that folder's team.json its own"), False
    return hcfg, "", False


def _guest_shape_reason(slug, home) -> str:
    """resolve_guests 自己也查的那部分形状（team_status.py、check_citations.py 不先跑 load_config）：空串 = 没问题。"""
    if not isinstance(slug, str) or not SAFE_SLUG_RE.match(slug) or ".." in slug:
        return f"slug {slug!r} cannot be a folder name"
    if home is None:
        return "no home (the home team's folder name under product/)"
    if not isinstance(home, str):
        return f"home {json.dumps(home, ensure_ascii=False)} is not a string"
    if not SAFE_SLUG_RE.match(home) or ".." in home:
        return f"home {home!r} cannot be a folder name"
    return ""


def guest_link_broken(g: dict) -> bool:
    """README 里指向这位（解析后的）客座 SKILL.md 的链接，check_links.py 算坏链而不是 pending：SKILL.md 还没有，而且
    home 队的 T1 已经开始（references/research/ 里有 .md 调研笔记）或没有 references/research/。pending 的规则与
    check_links.Checker.pending_member 相同（那里还要求 slug 列在 home 的 team.json 里，解析过的客座都满足）。"""
    d = Path(g["_dir"])
    if (d / "SKILL.md").is_file():
        return False
    research = d / "references" / "research"
    return not research.is_dir() or any(f.is_file() and f.suffix.lower() in (".md", ".markdown") for f in research.rglob("*"))


def resolve_guests_by_slug(cfg: dict, root: Path) -> tuple[list[dict], list[tuple[str | None, str, bool]], list[str]]:
    """resolve_guests 的实现：errors 是 (slug, 原因, 等合并) 三元组；slug 不是字符串的项为 (None, 整句, False)。
    等合并（True）只有三种，都是主队的分支还没合进本分支时会出的，合并之后自然能解析：home 的 team.json 找不到；
    slug 不是那队的成员，也没有只差大小写的成员；home 队里他的文件夹不存在。其余的错误（只差大小写、客座的客座、
    影子副本、home 的 team.json 不合法或写的是别队、形状不对）错误行自己写了就地的修法（merge_pending_stop）。"""
    gs = cfg.get("guests")
    out: list[dict] = []
    errs: list[tuple[str | None, str, bool]] = []
    notes: list[str] = []
    if not gs:
        return out, errs, notes
    if not isinstance(gs, list):
        return out, [(None, "guests: not a list of {slug, home} objects (see new_team.load_config)", False)], notes
    homes: dict[str, tuple[dict | None, str, bool]] = {}
    root_opt = "" if same_path(root, DEFAULT_ROOT) else f" --root {display(root)}"
    members = {m.get("slug") for m in cfg.get("members") or [] if isinstance(m, dict)} \
        if isinstance(cfg.get("members"), list) else set()
    for i, g in enumerate(gs):
        slug = g.get("slug") if isinstance(g, dict) else None
        home = g.get("home") if isinstance(g, dict) else None
        if not isinstance(slug, str):
            errs.append((None, f"guests[{i}]: not a {{slug, home}} pair of folder names (see new_team.load_config)", False))
            continue
        bad = _guest_shape_reason(slug, home)
        if bad:  # slug 是字符串：按 slug 报（team_status.py 列出这一项，原因写在它那一行）
            errs.append((slug, f"not a {{slug, home}} pair of folder names: {bad} (see new_team.load_config)", False))
            continue
        # 这两条 load_config 也报；team_status.py、check_citations.py 不跑 load_config，先在这里说对原因与修法
        if home == cfg.get("team"):
            errs.append((slug, "home is this team: list the person under members, not guests", False))
            continue
        if slug in members:
            errs.append((slug, "is also a member of this team: keep one of the two entries", False))
            continue
        if home not in homes:
            homes[home] = _home_team(root, home)
        hcfg, why, pending = homes[home]
        if hcfg is None:
            errs.append((slug, why, pending))
            continue
        hj = root / home / "team.json"
        entry = next((m for m in hcfg["members"] if isinstance(m, dict) and m.get("slug") == slug), None)
        if entry is None:
            via = next((x for x in hcfg.get("guests") or [] if isinstance(x, dict) and x.get("slug") == slug), None)
            if via is not None:
                errs.append((slug, f"{home} seats {slug} as its own guest; a guest of a guest is not allowed; "
                                   f"seat it from its home team {via.get('home')}", False))
            else:
                # 最常见的原因是主队加这位成员的分支还没合进本分支（playbook 第三节 T0 一行），所以先说合并，再说改 slug / home；
                # 只差大小写时（slug 区分大小写，手写的 guests 容易写错）先问是不是那一位，不说合并
                listed = [str(m.get("slug")) for m in hcfg["members"] if isinstance(m, dict)]
                near = next((s for s in listed if s.lower() == slug.lower()), None)
                errs.append((slug, f"not a member of {home} ({display(hj)} lists {', '.join(listed[:8])}"
                                   f"{' …' if len(listed) > 8 else ''}): " + (
                                       f"did you mean {near}? (slugs are case-sensitive)" if near else
                                       f"if the home team's branch that adds {slug} is not merged here yet, merge it first "
                                       f"(playbook §八, 加一位客座成员 step 2); otherwise check slug and home, or add {slug} "
                                       f"to the members of {home} first (step 1)"), near is None))
            continue
        d = root / home / slug
        if not d.is_dir():
            errs.append((slug, f"{display(d)}/ missing; scaffold it in the home team first: "
                               f"python3 {display(HERE / 'new_team.py')} {display(hj)} --add-member {slug}{root_opt}", True))
            continue
        shadow = root / str(cfg.get("team")) / slug
        if shadow.exists() or shadow.is_symlink():
            errs.append((slug, f"{display(shadow)} exists in this team: a shadow copy the roundtable would load "
                               f"instead of {display(d)}/; remove it (one skill per person, kept in its home team)", False))
            continue
        g_out = dict(entry, _home=home, _dir=d, _home_title=hcfg.get("title") or home)
        if not (d / "SKILL.md").is_file():
            note = f"guest {slug}: no SKILL.md yet (the home team's T1)"
            if guest_link_broken(g_out):  # home 队的 T1 跑到一半：链接不是 pending
                note += (f"; {display(d)}/ " + ("already has research notes" if (d / "references/research").is_dir()
                                                 else "has no references/research/")
                         + f", so check_links.py counts this team's README link to ../{home}/{slug}/SKILL.md as broken "
                           "(not pending) until the home team's T1 writes SKILL.md: merge the home team's branch after "
                           "its T1, or expect the T0 gate (check_links.py) to fail on that link until then")
            notes.append(note)
        out.append(g_out)
    return out, errs, notes


def guest_msg(slug: str | None, why: str) -> str:
    """resolve_guests_by_slug 的一条错误写成一行：slug 是字符串时以 "guest <slug>: " 开头。"""
    return why if slug is None else f"guest {slug}: {why}"


def merge_pending_stop(errs: list[tuple[str | None, str, bool]]) -> list[str]:
    """guest_stop_hint（和 --add-guest 找不到 README.md 时那句 "scaffold without it"）点名的客座：resolve_guests_by_slug
    的错误都是等合并的那三种时，这几位的 slug（按 guests 的顺序，不重复）。只要有一条就地能改的错误（只差大小写、
    影子副本、客座的客座、home 的 team.json 不合法或写的是别队、形状不对），或者没有错误，就是空列表：那条错误行
    自己写了修法，"先留在 guests 外面、以后再加回来" 帮不上忙。"""
    return list(dict.fromkeys(s for s, _, _ in errs)) if errs and all(p for _, _, p in errs) else []


def resolve_guests(cfg: dict, root: Path) -> tuple[list[dict], list[str], list[str]]:
    """team.json 的 guests 到 root/<home>/ 里解析（root = 放各团队目录的文件夹，如 product/；从团队目录出发的调用方传
    teams_root(团队目录)）。返回 (guests, errors, notes)。
    guests：每位能解析的客座一项 = home 队 team.json 里他的成员条目（所有键原样，那里缺的键就缺着）
    + _home（home 文件夹名）、_dir（root/<home>/<slug>）、_home_title（home 队的 title，没有时为 home）。
    errors（slug 是字符串的项每条以 "guest <slug>: " 开头，写明原因与修法）：形状不对（slug / home 不能当文件夹名、缺 home）、
    home 是本队、slug 也是本队成员（这两条与 load_config 相同，给不跑 load_config 的脚本报对修法）、home 的 team.json
    找不到或不合法、team 字段不等于 home、slug 不是那队的成员（多半是主队加他的分支还没合进来，报错先说合并；与那队某位
    成员的 slug 只差大小写时改问 did you mean <那个 slug>?；客座的客座不行）、root/<home>/<slug>/ 不存在、本队目录
    root/<team>/<slug> 存在（影子副本）。
    notes：还没有 SKILL.md（home 队的 T1）；他的文件夹里已有调研笔记或没有 references/research/ 时还说明 check_links.py
    把 README 的链接算坏链。
    只读 home 的 team.json 本身，不解析它的 guests（不递归）。"""
    guests, errs, notes = resolve_guests_by_slug(cfg, root)
    return guests, [guest_msg(slug, why) for slug, why, _ in errs], notes


def guest_reasons(cfg: dict, root: Path) -> dict[str, str]:
    """解析不了的客座 slug → 原因（resolve_guests 的错误去掉开头的 "guest <slug>: "；同一位有几条时取第一条）。"""
    out: dict[str, str] = {}
    for slug, why, _ in resolve_guests_by_slug(cfg, root)[1]:
        if slug is not None:
            out.setdefault(slug, why)
    return out


def seated_guests(cfg: dict, root: Path, teams: bool = True) -> dict[str, list[dict]]:
    """圆桌上坐着的别队的人，按入座单位：先是 guest_teams 的每一队（键 = 队名，值 = 那队全部成员，各带 _dir；
    那队的 team.json 读不了时为空列表），再是 guests 的每一位（键 = slug，值 = [resolve_guests 的条目]，解析不了时为空列表）。
    teams=False 只给 guests 的部分：check_citations.py 照加客座之前的写法自己读 guest_teams（那队的 team.json 在、却读不了
    或不是合法 JSON 时停下，不当作那队没有成员）；team_check.py 加客座之前就是这里这样读的。"""
    out: dict[str, list[dict]] = {}
    for g in (cfg.get("guest_teams") or []) if teams else []:
        gj = root / g / "team.json"
        try:
            gm = json.loads(gj.read_text(encoding="utf-8")).get("members", [])
        except (OSError, json.JSONDecodeError):
            gm = []
        out[g] = [dict(m, _dir=root / g / m["slug"]) for m in gm if m.get("slug")]
    if cfg.get("guests"):
        resolved = {r["slug"]: r for r in resolve_guests(cfg, root)[0]}
        for g in guest_entries(cfg):
            out[g["slug"]] = [resolved[g["slug"]]] if g["slug"] in resolved else []
    return out


def guest_stage(g: dict) -> str:
    """解析后的客座在 home 队走到哪：cards present（有卡片 digest）/ T1 base skill（有 SKILL.md）/ T0 scaffold。"""
    d = Path(g["_dir"])
    if any((d / "references/research/cards").glob("*.digest.json")):
        return "cards present"
    return "T1 base skill" if (d / "SKILL.md").is_file() else "T0 scaffold"


# ---------- 模板 ----------

def member_row(team_dir: Path, m: dict) -> str:
    stage = "T1 base skill" if (team_dir / m["slug"] / "SKILL.md").exists() else "T0 scaffold"
    if m.get("student_mode"):
        stage += " · student mode"
    return f"| [{m['name']}]({m['slug']}/SKILL.md) | lens: [TODO] | {stage} |"


def roundtable_row(m: dict) -> str:
    return (f"| `{m['slug']}` | {m['name']} | [TODO: the lens in one line, condensed from this member's Roundtable Card "
            f"\"Lens (one line)\"; team-layer.js (T2)] |")


def guest_row(g: dict) -> str:
    """README 成员表里客座的一行（g 是 resolve_guests 的条目）：链到 home 队的文件夹，状态格写明从哪队来。"""
    stage = "T1 base skill" if (Path(g["_dir"]) / "SKILL.md").exists() else "T0 scaffold"
    if g.get("student_mode"):
        stage += " · student mode"
    return (f"| [{g['name']}](../{g['_home']}/{g['slug']}/SKILL.md) | lens: [TODO] | "
            f"guest from [{g['_home_title']}](../{g['_home']}/README.md) · {stage} |")


def guest_roundtable_row(g: dict) -> str:
    """圆桌 Team 表里客座的一行：第一格仍是 `slug`（team_check 按它找座位）。"""
    return (f"| `{g['slug']}` | {g['name']} (guest from {g['_home_title']}) | [TODO: the lens in one line for THIS team's "
            f"field, from this guest's Roundtable Card in ../../{g['_home']}/{g['slug']}/SKILL.md (written for "
            f"{g['_home_title']}); team-layer.js (T2)] |")


def and_list(names: list[str]) -> str:
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]


def by_home(guests: list[dict]) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for g in guests:
        out.setdefault(g["_home"], []).append(g)
    return out


GUEST_KEYS = ("GUEST_CLAUSE", "GUEST_INSTALL", "GUEST_INSTALL_PS", "GUEST_RESOLUTION", "GUEST_CARDS", "GUEST_SEATS_TODO",
              "GUEST_DEEP_READING")


def guest_install_comment(gs: list[dict]) -> str:
    """一支 home 队的客座安装行上面那一行注释（"# " 之后的部分），bash、PowerShell 两段相同。注释单独成行，行里没有
    ; ( ) 这类 shell 字符：zsh 默认不开 INTERACTIVE_COMMENTS，交互粘贴时 # 不算注释，写在复制命令行尾的注释里有 ; 和
    (…) 时那一行解析失败、复制不执行；单独一行的注释在那里只报一句找不到命令，下一行照常执行（模板 bash 段第一行的
    # macOS / Linux 注释也是这样）。home 队 title 里 shell 会特殊对待的字符去掉。"""
    title = re.sub(r"[^\w .,:/+-]", "", gs[0]["_home_title"]).strip() or gs[0]["_home"]
    return (f"{'guest' if len(gs) == 1 else 'guests'} from the {title}: if this checkout holds git-ignored full texts, "
            "copy only git-tracked files, see product/README.md")


def guest_values(guests: list[dict]) -> dict:
    """客座的占位符：没有客座时全是空串（模板里它们都接在已有行的末尾，不给输出添任何字符）。"""
    if not guests:
        return {k: "" for k in GUEST_KEYS}
    homes = by_home(guests)
    clause = []
    for gs in homes.values():
        names = and_list([g["name"] for g in gs])
        clause.append(f"with guest {names} from the {gs[0]['_home_title']} (the skill lives in that team's folder)"
                      if len(gs) == 1 else
                      f"with guests {names} from the {gs[0]['_home_title']} (their skills live in that team's folder)")
    where = ", ".join(f"`{h}` for the {gs[0]['_home_title']}" if gs[0]["_home_title"] != h else f"`{h}`"
                      for h, gs in homes.items())
    return {
        "GUEST_CLAUSE": ", " + "; ".join(clause),
        # 接在 team-README.md 的 bash 复制行末尾：每支 home 队先另起一行注释，其下每位客座一行 cp -r（行尾不带注释）
        "GUEST_INSTALL": "".join(f"\n# {guest_install_comment(gs)}"
                                 + "".join(f"\ncp -r product/{g['_home']}/{g['slug']} ~/.claude/skills/" for g in gs)
                                 for gs in homes.values()),
        # 接在 PowerShell 那一行末尾，与 bash 的 GUEST_INSTALL 同样分行，注释相同
        "GUEST_INSTALL_PS": "".join(f"\n# {guest_install_comment(gs)}"
                                    + "".join(f"\nCopy-Item -Recurse product\\{g['_home']}\\{g['slug']} \"$HOME\\.claude\\skills\\\""
                                              for g in gs)
                                    for gs in homes.values()),
        "GUEST_RESOLUTION": (" A guest (marked \"guest from …\" in the Team table) resolves first at "
                             f"`../../<home>/<slug>/SKILL.md` in this repository (<home>: {where}), then at the installed "
                             "paths above; its research notes and cards are in that same folder."),
        "GUEST_CARDS": (" A guest's cards are in its home folder: `../../<home>/<slug>/references/research/cards/` "
                        "(card ids are per member)."),
        "GUEST_SEATS_TODO": (" [TODO: one \"Guest seat\" note per guest below the Team table: leads when (problem signals in "
                             "THIS team's field), likely disagreements with this team's members (evidence from both sides' "
                             "own files), and the delegate note for briefing the guest's agent (its SKILL.md names its home "
                             "roundtable); team-layer.js (T2)]"),
        "GUEST_DEEP_READING": (" Guests are read by their home teams: " + "; ".join(
            f"{and_list([g['name'] for g in gs])} in [../{h}/DEEP-READING.md](../{h}/DEEP-READING.md)"
            for h, gs in homes.items()) + "."),
    }


def team_values(cfg: dict, team_dir: Path, extra: dict, guests: list[dict] | None = None) -> dict:
    """团队级占位符。guests：resolve_guests 的条目（成员表、圆桌 Team 表在成员行之后加客座行）；不给或为空时与以前相同。
    SEATED_LIST 在 --set（extra）之后才接：生效的 MEMBER_LIST + 客座姓名，所以 --set MEMBER_LIST=X 也改圆桌的 description
    与免责声明（没有客座时 = MEMBER_LIST，与这两处用 {{MEMBER_LIST}} 时逐字相同）；--set SEATED_LIST=Y 时用 Y。
    这只管铺目录这一次：有客座时 T2（team-layer.js 的客座分支）照 --guest-text 打印的 SEATED_LIST 逐字重写这两处，
    而 guest_text 调用这里时 extra 为空（--guest-text 不收 --set），所以铺目录时用 --set 改的 MEMBER_LIST / SEATED_LIST
    在这两处留不过 T2。"""
    ms, gs = cfg["members"], guests or []
    v = {"TEAM_SLUG": cfg["team"], "TEAM_TITLE": cfg["title"], "FIELD": cfg["field"],
         "LANGUAGE": cfg.get("language") or "English", "DATE": today(), "ROUNDTABLE_SLUG": cfg["roundtable"],
         "MEMBER_TABLE": "\n".join([member_row(team_dir, m) for m in ms] + [guest_row(g) for g in gs]),
         "ROUNDTABLE_MEMBER_TABLE": "\n".join([roundtable_row(m) for m in ms] + [guest_roundtable_row(g) for g in gs]),
         "MEMBER_LIST": ", ".join(m["name"] for m in ms), "MEMBER_COUNT": str(len(ms)), "SEATED_LIST": ""}
    v.update(guest_values(gs))
    v.update(extra)
    if "SEATED_LIST" not in extra:
        v["SEATED_LIST"] = ", ".join([x for x in [v["MEMBER_LIST"]] if x] + [g["name"] for g in gs])
    return v


def member_values(base: dict, m: dict, extra: dict, base_tier: bool = False) -> dict:
    v = dict(base)
    sch = (m.get("scholar") or "").strip()
    v.update({"MEMBER_NAME": m["name"], "MEMBER_SLUG": m["slug"], "MEMBER_SURNAME": m.get("surname") or surname_of(m["name"]),
              "SCHOLAR_URL": f"https://scholar.google.com/citations?user={sch}&hl=en" if sch
              else ("—" if base_tier else NO_SCHOLAR)})
    v.update(extra)
    return v


def split_row(line: str) -> list[str]:
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def base_tier_deep_reading(template: str) -> str | None:
    """DEEP-READING.md 模板开头注释里给轻量档的两段（标题 + 一段），缩进比注释正文深；找不到返回 None。"""
    lines = template.splitlines()
    k = next((i for i, ln in enumerate(lines) if "two paragraphs below" in ln), None)
    if k is None:
        return None
    body = []
    for ln in lines[k + 1:]:
        if not ln.startswith(" " * 12) or not ln.strip() or ln.strip().startswith(("Open work", "-->")):
            break
        body.append(ln.strip())
    if len(body) < 2 or not body[0].startswith("#"):
        return None
    return body[0] + "\n\n" + " ".join(body[1:]) + "\n"


def base_tier_resources(text: str) -> tuple[str, list[str]]:
    """RESOURCES.md 的轻量档写法：删深读档占位行（第 3 行），第 1 行 Notes = not harvested (base tier)，
    Link 里还有 TODO 时换成 —。返回 (新文本, 没做成的事)。"""
    out, missed, row1, row3 = [], [], False, False
    for ln in text.split("\n"):
        cells = split_row(ln) if ln.lstrip().startswith("|") else []
        if cells and cells[0] == "3" and "deep-tier" in ln:
            row3 = True
            continue
        if cells and cells[0] == "1" and len(cells) >= 3:
            row1 = True
            cells[-1] = BASE_TIER_NOTES
            cells = ["—" if "[TODO" in c and i == len(cells) - 4 else c for i, c in enumerate(cells)]
            ln = "| " + " | ".join(cells) + " |"
        out.append(ln)
    if not row1:
        missed.append("找不到第 1 行（出版物列表）")
    if not row3:
        missed.append("找不到深读档占位行（第 3 行）")
    return "\n".join(out), missed


def template_problems(name: str, text: str, values: dict) -> list[str]:
    probs = []
    for i, line in enumerate(text.splitlines(), 1):
        unknown = [m.group(0) for m in PLACEHOLDER_RE.finditer(line) if m.group(1) not in values]
        stray = PLACEHOLDER_RE.sub("", line).count("{{")
        if unknown:
            probs.append(f"{name}:{i}: 未知占位符 {' '.join(unknown)}")
        if stray:
            probs.append(f"{name}:{i}: 落单的 {{{{（不是 {{{{NAME}}}} 形式）")
    return probs


def fill(text: str, values: dict) -> str:
    return PLACEHOLDER_RE.sub(lambda m: values.get(m.group(1), m.group(0)), text)


# ---------- 计划与执行 ----------

class Plan:
    def __init__(self, team_dir: Path, force: bool):
        self.team_dir, self.force = team_dir, force
        self.actions: list[tuple] = []       # (kind, path, content, label)
        self.errors: list[str] = []
        self.notes: list[str] = []
        self.guests: list[dict] = []         # resolve_guests 的条目（客座：不建文件夹，只写进成员表与圆桌）
        self.guest_errors: list[str] = []    # 让这次停下的客座解析错误（--add-guest 以外；也在 errors 里）
        self.guest_stop: list[str] = []      # 那几位客座的 slug，只在他们的错误都是等合并的那几种时（merge_pending_stop）

    def file(self, rel: str, content: str):
        self.actions.append(("file", self.team_dir / rel, content, rel))

    def dirs(self, member: str, rels: list[str]):
        self.actions.append(("dirs", self.team_dir / member, rels, member))

    def update(self, rel: str, content: str, why: str):
        self.actions.append(("update", self.team_dir / rel, content, f"{rel} ({why})"))

    def keep(self, rel: str, why: str):
        self.actions.append(("keep", self.team_dir / rel, None, f"{rel} ({why})"))


def row_like(line: str, nb: dict, m: dict, standard: str) -> str:
    """照着邻居成员的表格行造一行。邻居行是 {{MEMBER_TABLE}} 的格式（3 格、第一格链到 slug/SKILL.md）时直接用标准行；
    否则同样的列数：含邻居 slug 的格换成新 slug 与新姓名（没有全名时换姓），等于邻居姓名的格换成新姓名，其余格 [TODO]。"""
    cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
    if len(cells) == 3 and re.fullmatch(rf"\[[^\]]*\]\(\s*(?:\./)?{re.escape(nb['slug'])}/SKILL\.md\s*\)", cells[0]):
        return standard
    out = []
    for c in cells:
        if nb["slug"] in c:
            c = c.replace(nb["slug"], m["slug"])
            if nb.get("name") and nb["name"] in c:
                c = c.replace(nb["name"], m["name"])
            elif nb.get("surname") and m.get("surname"):
                c = c.replace(nb["surname"], m["surname"])
            out.append(c)
        elif c == nb.get("name"):
            out.append(m["name"])
        else:
            out.append("[TODO]")
    return "| " + " | ".join(out) + " |"


def member_link_re(slug: str) -> re.Pattern:
    """表格里链到成员文件夹的链接：](slug/…) 或 ](./slug/…)。"""
    return re.compile(rf"\]\(\s*(?:\./)?{re.escape(slug)}/")


def listed_in_table(text: str, slug: str) -> bool:
    rx = member_link_re(slug)
    return any(ln.lstrip().startswith("|") and rx.search(ln) for ln in text.split("\n"))


def insert_member_row(text: str, row: str, m: dict, others: list[dict]) -> tuple[str, str]:
    """有 members 标记时把标准行插在 end 标记前；否则照最后一个成员行的格式插在它后面；都没有就在文末追加 [TODO]。"""
    slug = m["slug"]
    lines = text.split("\n")
    if listed_in_table(text, slug) or f"({slug}/) to the member table" in text:
        return text, "already listed"
    if MARK_START in text and MARK_END in text and text.index(MARK_START) < text.index(MARK_END):
        end = next(i for i, ln in enumerate(lines) if MARK_END in ln)
        lines.insert(end, row)
        return "\n".join(lines), "row added before " + MARK_END
    last, nb = None, None
    for i, ln in enumerate(lines):
        if not ln.lstrip().startswith("|"):
            continue
        hit = next((o for o in others if member_link_re(o["slug"]).search(ln)), None)
        if hit:
            last, nb = i, hit
    if last is not None:
        lines.insert(last + 1, row_like(lines[last], nb, m, row))
        return "\n".join(lines), f"row added after {nb['slug']}'s row"
    tail = "" if text.endswith("\n") else "\n"
    return text + f"{tail}\n[TODO: add {m['name']} ({slug}/) to the member table: `{row}`]\n", \
        "no member table found, TODO appended"


def guest_link_re(home: str, slug: str) -> re.Pattern:
    """表格里链到客座（home 队文件夹）的链接：](../<home>/<slug>/…) 或 ](./../<home>/<slug>/…)。"""
    return re.compile(rf"\]\(\s*(?:\./)?\.\./{re.escape(home)}/{re.escape(slug)}/")


def guest_listed(text: str, home: str, slug: str) -> bool:
    rx = guest_link_re(home, slug)
    return any(ln.lstrip().startswith("|") and rx.search(ln) for ln in text.split("\n"))


def insert_guest_row(text: str, row: str, g: dict, members: list[dict], others: list[dict]) -> tuple[str, str]:
    """--add-guest：客座的一行（{{MEMBER_TABLE}} 的客座行格式）插在 members 标记的 end 前，否则插在成员表最后一个
    成员行或客座行后面；已有就不动；一个表格行都找不到就在文末追加 [TODO]。"""
    home, slug = g["_home"], g["slug"]
    lines = text.split("\n")
    if guest_listed(text, home, slug) or f"(../{home}/{slug}/) to the member table" in text:
        return text, "already listed"
    if MARK_START in text and MARK_END in text and text.index(MARK_START) < text.index(MARK_END):
        end = next(i for i, ln in enumerate(lines) if MARK_END in ln)
        lines.insert(end, row)
        return "\n".join(lines), "row added before " + MARK_END
    last, after = None, ""
    for i, ln in enumerate(lines):
        if not ln.lstrip().startswith("|"):
            continue
        hit = next((m["slug"] for m in members if member_link_re(m["slug"]).search(ln)), None) or \
            next((o["slug"] for o in others if guest_link_re(o["_home"], o["slug"]).search(ln)), None)
        if hit:
            last, after = i, hit
    if last is not None:
        lines.insert(last + 1, row)
        return "\n".join(lines), f"row added after {after}'s row"
    tail = "" if text.endswith("\n") else "\n"
    return text + f"{tail}\n[TODO: add {g['name']} (../{home}/{slug}/) to the member table: `{row}`]\n", \
        "no member table found, TODO appended"


def sync_team_json(plan: Plan, src: Path, cfg: dict, adding: list[str], adding_guests: list[str] | None = None):
    dest = plan.team_dir / "team.json"
    if not dest.exists():
        plan.file("team.json", src.read_text(encoding="utf-8"))
        return
    if dest.resolve() == src.resolve():
        plan.keep("team.json", "就是输入文件")
        return
    try:
        same = json.loads(dest.read_text(encoding="utf-8")) == cfg
    except (OSError, json.JSONDecodeError):
        same = False
    if same:
        plan.keep("team.json", "内容相同")
        return
    if plan.force:
        plan.file("team.json", src.read_text(encoding="utf-8"))
        return
    try:
        have = {m.get("slug") for m in json.loads(dest.read_text(encoding="utf-8")).get("members") or []}
    except (OSError, json.JSONDecodeError, AttributeError):
        have = set()
    missing = [s for s in adding if s not in have]
    have_g: set = set()
    if adding_guests:
        try:
            have_g = {g.get("slug") for g in json.loads(dest.read_text(encoding="utf-8")).get("guests") or []
                      if isinstance(g, dict)}
        except (OSError, json.JSONDecodeError, AttributeError):
            pass
    missing_g = [s for s in adding_guests or [] if s not in have_g]
    if missing:
        plan.errors.append(f"{display(dest)} 里没有成员 {', '.join(missing)}，而且与 {display(src)} 不同："
                           f"把成员写进团队目录里的 team.json 再跑，或 --force 用 {display(src)} 覆盖它")
    if missing_g:
        plan.errors.append(f"{display(dest)} 的 guests 里没有 {', '.join(missing_g)}，而且与 {display(src)} 不同："
                           f"把客座写进团队目录里的 team.json 再跑，或 --force 用 {display(src)} 覆盖它")
    if not missing and not missing_g:
        plan.notes.append(f"⚠️ {display(dest)} 与 {display(src)} 不同，保留团队目录里的版本（--force 覆盖）")


def load_templates(tdir: Path, names: list[str], plan: Plan) -> dict:
    out = {}
    for n in names:
        p = tdir / n
        if p.is_file():
            out[n] = p.read_text(encoding="utf-8")
        else:
            plan.errors.append(f"缺模板 {display(p)}")
    return out


def add_guest_rows(plan: Plan, cfg: dict, adding_guests: list[str]):
    """--add-guest：把这几位客座的行插进已有 README.md 的成员表（不建文件夹，不改圆桌和 DEEP-READING.md）。
    README.md 不存在时 build_plan 已经报错停下（先铺目录），走不到这里。邻居行按 team.json 的 guests 认（解析不了的
    客座已有的行也算邻居）。"""
    readme = plan.team_dir / "README.md"
    text = readme.read_text(encoding="utf-8")
    hows = []
    entries = [{"slug": g["slug"], "_home": g["home"]} for g in cfg.get("guests") or []]
    for g in plan.guests:
        if g["slug"] not in adding_guests:
            continue
        others = [o for o in entries if o["slug"] != g["slug"]]
        text, how = insert_guest_row(text, guest_row(g), g, cfg["members"], others)
        if how == "already listed":
            plan.keep("README.md", f"已有 {g['slug']} 的行")
        else:
            hows.append(f"{g['slug']}: {how}")
    if hows:
        plan.update("README.md", text, "; ".join(hows))


def build_plan(a, src: Path, cfg: dict, adding: list[str], extra: dict, adding_guests: list[str] | None = None) -> Plan:
    team_dir = Path(a.root) / cfg["team"]
    plan = Plan(team_dir, a.force)
    slugs = [m["slug"] for m in cfg["members"]]
    homes = {g["slug"]: g["home"] for g in cfg.get("guests") or []}
    adding_guests = adding_guests or []
    guests, gerrs, gnotes = resolve_guests_by_slug(cfg, Path(a.root))  # 客座：解析错误和其他校验错误一样，什么都不写
    stop = merge_pending_stop(gerrs)  # 客座的错误都是等合并的那几种时：可以先不带这几位铺（guest_stop_hint）
    if adding:
        if not team_dir.is_dir():
            plan.errors.append(f"团队目录 {display(team_dir)} 不存在：先不带 --add-member 跑一次")
        unknown = [s for s in adding if s not in slugs and s not in homes]
        if unknown:
            plan.errors.append(f"{display(src)} 的 members 里没有 {', '.join(unknown)}（先把他写进 team.json）")
        plan.errors += [f"{s} 是客座（home 队 {homes[s]}）：用 --add-guest {s}" for s in adding if s in homes]
    if adding_guests:
        readme = team_dir / "README.md"
        if not readme.is_file():  # 团队目录不存在或还没铺：--add-guest 只往已有 README 的成员表里加行
            root_opt = "" if same_path(Path(a.root), DEFAULT_ROOT) else f" --root {display(Path(a.root))}"
            cmd = f"python3 {display(HERE / 'new_team.py')} {display(src)}{root_opt} (without --add-guest)"
            # 铺目录时等合并的客座也会让它停下：先不带这几位铺，等他们能解析了再加回来、跑 --add-guest。这时先说把他们
            # 留在 guests 外面、再给铺目录的命令（照写的顺序做就跑得通）。有就地能改的客座错误时不给这一句、只给命令（与
            # 铺目录时的 guest_stop_hint 相同：那条 ❌ / ⚠️ 自己写了修法）
            plan.errors.append(f"{display(readme)} not found: scaffold the team first" + (
                f"; while a guest in team.json does not resolve, scaffold without it: leave {and_list(stop)} out of "
                f"guests, then run {cmd}; once {'it resolves, add it' if len(stop) == 1 else 'they resolve, add them'} "
                "back and run --add-guest" if stop else f": {cmd}"))
        plan.errors += [f"{s} 是本队成员，不是客座：用 --add-member {s}" for s in adding_guests if s in slugs]
        unknown = [s for s in adding_guests if s not in homes and s not in slugs]
        if unknown:
            plan.errors.append(f"{display(src)} 的 guests 里没有 {', '.join(unknown)}"
                               f"（先把 {{\"slug\": …, \"home\": …}} 写进 team.json 的 guests）")
    if src.parent.name != cfg["team"] and src.name == "team.json" and src.parent.parent.resolve() == Path(a.root).resolve():
        plan.notes.append(f"⚠️ {display(src)} 所在文件夹名与 team 字段 {cfg['team']!r} 不同，团队目录按 team 字段建")
    if src.parent.name == cfg["team"] and not same_path(src.parent, team_dir):
        plan.notes.append(f"⚠️ {display(src)} 在团队文件夹 {display(src.parent)} 里，但团队目录会建在 {display(team_dir)}；"
                          f"要铺在原处就加 --root {display(src.parent.parent)}")
    plan.guests = guests
    msg = guest_msg  # 与 resolve_guests 的写法相同
    if adding_guests:
        # --add-guest 只加这几位：只有他们解析不了才停；别的客座解析不了只提示（team_check.py 的 guests 一项照样判 ✗，
        # --guest-text 和 make_args.mjs 照样停）
        plan.errors += [msg(s, why) for s, why, _ in gerrs if s in adding_guests]
        plan.notes += [f"⚠️ {msg(s, why)} (not being added in this run, so it does not stop --add-guest; team_check.py's "
                       "guests row fails, and --guest-text and make_args.mjs (T2, T3.8) stop on it, until it is fixed)"
                       for s, why, _ in gerrs if s not in adding_guests]
    else:
        plan.guest_errors = [msg(s, why) for s, why, _ in gerrs]
        plan.guest_stop = stop
        plan.errors += plan.guest_errors
    plan.notes += gnotes
    plan.notes += surname_clashes(cfg["members"] + guests)
    if not adding and not adding_guests and not a.force and (team_dir / "README.md").is_file():
        text = (team_dir / "README.md").read_text(encoding="utf-8")
        unlisted = [m["slug"] for m in cfg["members"] if not listed_in_table(text, m["slug"])]
        if unlisted:
            plan.notes.append(f"⚠️ 已有的 README.md 成员表里没有 {', '.join(unlisted)}（重跑不改已存在的文件）："
                              f"用 --add-member {' --add-member '.join(unlisted)} 加行，圆桌 SKILL.md 也要补上")
        unlisted_g = [g["slug"] for g in guests if not guest_listed(text, g["_home"], g["slug"])]
        if unlisted_g:
            plan.notes.append(f"⚠️ 已有的 README.md 成员表里没有客座 {', '.join(unlisted_g)}（重跑不改已存在的文件）："
                              f"用 --add-guest {' --add-guest '.join(unlisted_g)} 加行，圆桌 SKILL.md 由 T2 补上")
    sync_team_json(plan, src, cfg, adding, adding_guests)
    if adding_guests:  # 客座不建文件夹、不用模板：只改 README 的成员表
        if not plan.errors:
            add_guest_rows(plan, cfg, adding_guests)
        return plan
    tnames = ([] if adding else [t for t, _ in TEAM_TEMPLATES]) + [t for t, _ in MEMBER_TEMPLATES]
    templates = load_templates(Path(a.templates), tnames, plan)
    if plan.errors:
        return plan

    base = team_values(cfg, team_dir, extra, guests)
    for t, _ in TEAM_TEMPLATES:
        if t in templates:
            plan.errors += template_problems(t, templates[t], base)
    probe = member_values(base, cfg["members"][0], extra, a.base_tier)
    for t, _ in MEMBER_TEMPLATES:
        plan.errors += template_problems(t, templates[t], probe)
    deep_note = None
    if a.base_tier and not adding:
        deep_note = base_tier_deep_reading(templates.get("DEEP-READING.md", ""))
        if deep_note is None:
            plan.errors.append("--base-tier: DEEP-READING.md 模板开头注释里找不到轻量档的两段说明（\"two paragraphs below\" 之后）")
        elif guests and not any(m.group(1) == "GUEST_DEEP_READING" for m in PLACEHOLDER_RE.finditer(deep_note)):
            # 有客座：轻量档说明那一段的末尾接上客座指引（模板开头注释里的这段不带占位符，与没有客座的团队相同）
            deep_note = deep_note.rstrip("\n") + "{{GUEST_DEEP_READING}}\n"
    if plan.errors:
        return plan

    if not adding:
        for t, dest in TEAM_TEMPLATES:
            text = deep_note if (t == "DEEP-READING.md" and deep_note) else templates[t]
            plan.file(dest.format(roundtable=cfg["roundtable"]), fill(text, base))
    for m in cfg["members"]:
        if adding and m["slug"] not in adding:
            continue
        mv = member_values(base, m, extra, a.base_tier)
        plan.dirs(m["slug"], MEMBER_DIRS)
        for t, dest in MEMBER_TEMPLATES:
            text = fill(templates[t], mv)
            if a.base_tier and t == "member-RESOURCES.md":
                text, missed = base_tier_resources(text)
                plan.notes += [f"⚠️ --base-tier: {m['slug']} 的 RESOURCES.md {x}，那部分照模板原样" for x in missed]
            plan.file(f"{m['slug']}/{dest}", text)
    if adding:
        readme = team_dir / "README.md"
        if not readme.is_file():
            plan.notes.append(f"⚠️ {display(readme)} 不存在，成员表没有更新")
        else:
            text = readme.read_text(encoding="utf-8")
            hows = []
            for m in cfg["members"]:
                if m["slug"] not in adding:
                    continue
                others = [o for o in cfg["members"] if o["slug"] != m["slug"]]
                text, how = insert_member_row(text, member_row(team_dir, m), m, others)
                if how == "already listed":
                    plan.keep("README.md", f"已有 {m['slug']} 的行")
                else:
                    hows.append(f"{m['slug']}: {how}")
            if hows:
                plan.update("README.md", text, "; ".join(hows))
    return plan


def execute(plan: Plan, dry: bool) -> tuple[dict, int]:
    counts = {"created": 0, "kept": 0, "overwritten": 0, "updated": 0, "dirs": 0}
    todos = 0
    for kind, path, content, label in plan.actions:
        if kind == "dirs":
            new = []
            for rel in content:
                d = path / rel
                if not d.is_dir():
                    new.append(rel)
                if not dry:
                    d.mkdir(parents=True, exist_ok=True)
                    keep = d / ".gitkeep"
                    if not any(d.iterdir()):
                        keep.touch()
            counts["dirs"] += len(new)
            if new:
                groups = ["references/research/"] if "references/research" in new else []
                srcs = [r.rsplit("/", 1)[1] for r in new if r.startswith("references/sources/")]
                if srcs:
                    groups.append("references/sources/{" + ",".join(srcs) + "}/" if len(srcs) > 1
                                  else f"references/sources/{srcs[0]}/")
                print(f"  + {label}/: {', '.join(groups)} (.gitkeep)")
            continue
        if kind == "keep":
            counts["kept"] += 1
            print(f"  = {label}")
            continue
        n_todo = content.count("[TODO")
        tag = f" · {n_todo} TODO" if n_todo else ""
        if kind == "update":
            counts["updated"] += 1
            print(f"  ~ {label}{tag}")
        elif path.exists() and not plan.force:
            counts["kept"] += 1
            print(f"  = {label} (已存在，保留；--force 覆盖)")
            continue
        elif path.exists():
            counts["overwritten"] += 1
            print(f"  ! {label} (覆盖){tag}")
        else:
            counts["created"] += 1
            print(f"  + {label}{tag}")
        todos += n_todo
        if not dry:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    return counts, todos


def git_ignore_check(team_dir: Path, slugs: list[str]) -> tuple[bool, str]:
    """用 git check-ignore 确认 PDF、txt/、private/ 被忽略而 private/README.md 不被忽略。返回 (是否有泄漏, 说明)。"""
    anchor = next((p for p in [team_dir, *team_dir.parents] if p.is_dir()), None)
    if anchor is None:
        return False, "· git: 没检查（目录不存在）"
    try:
        top = subprocess.run(["git", "-C", str(anchor), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired):
        return False, "· git: 没检查（没有 git）"
    if top.returncode != 0 or not top.stdout.strip():
        return False, f"· git: 没检查（{display(anchor)} 不在 git 仓库里）；自己确认 PDF、papers/txt/ 和 private/ 不会被提交"
    rel = lambda s, p: os.path.relpath(team_dir / s / p, anchor)
    want_ignored = [rel(s, p) for s in slugs for p in IGNORED_PROBES]
    want_tracked = [rel(s, p) for s in slugs for p in TRACKED_PROBES]
    try:
        out = subprocess.run(["git", "-C", str(anchor), "check-ignore", "--no-index", "--stdin", "-z"],
                             input="\0".join(want_ignored + want_tracked) + "\0",
                             capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired):
        return False, "· git: check-ignore 失败，没检查"
    if out.returncode not in (0, 1):
        return False, f"· git: check-ignore 出错（{out.stderr.strip()[:120]}），没检查"
    ignored = set(out.stdout.split("\0"))
    leaks = [p for p in want_ignored if p not in ignored]
    hidden = [p for p in want_tracked if p in ignored]
    if not leaks and not hidden:
        return False, ("✅ git: 每位成员 references/sources/ 下的 PDF/PS/DjVu/EPUB、papers/txt/ 和 private/"
                       "（README.md 除外）都被 .gitignore 忽略")
    msg = ["❌ git: .gitignore 没覆盖这个团队目录，版权全文或私人材料可能被提交。在仓库根 .gitignore 加上:"]
    msg += [f"     {r}" for r in gitignore_lines(team_dir, Path(top.stdout.strip()))]
    msg += [f"     没被忽略: {p}" for p in leaks[:6]] + [f"     不该被忽略: {p}" for p in hidden[:3]]
    return True, "\n".join(msg)


def gitignore_lines(team_dir: Path, top: Path) -> list[str]:
    """要加进仓库根 .gitignore 的规则：GITIGNORE_RULES 前面加上团队目录的上级（相对仓库根，如 product/）。"""
    base = Path(os.path.relpath(team_dir.parent.resolve(), top.resolve())).as_posix()
    base = "" if base == "." else base + "/"
    return [f"!{base}{r[1:]}" if r.startswith("!") else f"{base}{r}" for r in GITIGNORE_RULES]


def guest_stop_hint(slugs: list[str], adding: list[str] | None = None, init: bool = False,
                    every_guest: bool = False) -> str:
    """只因等合并的客座解析不了而停下时（主队的 T1 还在别的分支上跑、分支还没合进来时常见）的一句：本队自己的成员
    可以先铺，客座等能解析了再加（playbook §八 加一位客座成员第 2–3 步）。slugs 是 merge_pending_stop 给的：这次的客座
    错误都是 home 的 team.json 找不到、slug 不是那队的成员（也没有只差大小写的）、home 队里他的文件夹不存在；有一条
    就地能改的错误时调用方不打印这一句。错误本身的句子不变（与 make_args.mjs 逐字相同）。
    --add-guest 只给已经写在 team.json 的 guests 里的客座加 README 行，所以两种写法都先说写回 guests、再跑 --add-guest。
    every_guest（只用于 --init）：--guests 里的每一位都在 slugs 里。这时照字面把他们「从 --guests 里拿掉」会剩一个空的
    --guests，而空的 --guests 报「--guests 为空」，所以改说不带 --guests 再跑。"""
    them, they = ("it", "it resolves") if len(slugs) == 1 else ("them", "they resolve")
    if init and every_guest:  # 一位客座都不剩：不带 --guests 再跑；他们能解析了再写进 guests
        now = (f"to draft team.json now, run this again without --guests; once the team is scaffolded and "
               f"{and_list(slugs)} {'resolves' if len(slugs) == 1 else 'resolve'}, write {them} into team.json's guests "
               "and run --add-guest")
    elif init:  # 等他们能解析了才写回 guests（铺完就写回的话，--add-member 和重铺又会停在他们身上）
        now = (f"to draft team.json now, leave {and_list(slugs)} out of --guests; once the team is scaffolded and {they}, "
               f"write {them} into team.json's guests and run --add-guest")
    else:
        what = f"add {and_list(adding)}" if adding else "scaffold this team's own members"
        now = (f"to {what} now, leave {and_list(slugs)} out of team.json's guests, run this again, and once {they}, "
               f"write {them} back into team.json's guests and run --add-guest")
    return (f"· only guests that do not resolve stopped this run: {now} (a home team's branch that is not "
            "merged here yet: merge it after its T1 has written SKILL.md; playbook §八, 加一位客座成员 steps 2–3)")


def broken_link_steps(gs: list[dict]) -> list[str]:
    """「下一步」里的一条：README 指向这些客座 SKILL.md 的链接 check_links.py 算坏链（guest_link_broken）。两种情形分开说：
    home 队的 T1 已经开始（他的文件夹里已有调研笔记、还没有 SKILL.md）；他的文件夹里没有 references/research/——
    new_team.py 铺成员文件夹时总会建这个目录，所以这不说明 T1 开始了，只说明这个文件夹不是 new_team.py 铺的（或那个目录被删了）。"""
    bad = [g for g in gs if guest_link_broken(g)]
    if not bad:
        return []
    started = [g for g in bad if (Path(g["_dir"]) / "references/research").is_dir()]
    bare = [g for g in bad if g not in started]
    links = "、".join("../" + g["_home"] + "/" + g["slug"] + "/SKILL.md" for g in started + bare)
    why = "；".join(x for x in [
        f"客座 {', '.join(g['slug'] for g in started)} 还没有 SKILL.md，但 home 队的 T1 已经开始（home 队的文件夹里已有调研笔记）"
        if started else "",
        f"客座 {', '.join(g['slug'] for g in bare)} 还没有 SKILL.md，home 队的文件夹里也没有 references/research/"
        f"（new_team.py 铺的成员文件夹都有这个目录，所以{'这个文件夹' if len(bare) == 1 else '这些文件夹'}不是它铺的，"
        "或那个目录被删了）" if bare else ""] if x)
    return [f"  · {why}：check_links.py 把 "
            f"README 里指向 {links} 的链接算坏链，不是 pending，直到 home 队的 T1 写出 SKILL.md。所以等 home 队的 T1 跑完再合并"
            f"它的分支；现在就合并的话，T0 闸门 check_links.py（和 team_check.py 的 links 一项）在这些链接上不过"]


def guest_next_steps(cfg: dict, team_dir: Path, gs: list[dict]) -> list[str]:
    """--add-guest 之后：客座的流水线在 home 队；T2 等客座的 SKILL.md 到了本分支再跑；按客座名单渲染的句子
    （README、圆桌、DEEP-READING.md）这一步不改，列出来，并指向 --guest-text 给的逐字文本。"""
    t = display(team_dir)
    py = lambda s: f"python3 {display(HERE / s)}"
    tl = display(HERE / "workflows/team-layer.js")
    out = ["下一步:"]
    for hg in by_home(gs).values():
        out.append(f"  · 客座 {', '.join(g['slug'] for g in hg)} 的 T1、T3、T4 在 home 队 {display(Path(hg[0]['_dir']).parent)} 跑，"
                   f"不在这里；本队不给客座建文件夹、RESOURCES.md 或 private/")
    out += broken_link_steps(gs)
    waiting = [display(Path(g["_dir"]) / "SKILL.md") for g in gs if not (Path(g["_dir"]) / "SKILL.md").is_file()]
    out.append(f"  · T2 团队层：{'等 ' + '、'.join(waiting) + ' 出现在本分支（先合并 home 队的分支）后，' if waiting else ''}"
               f"跑 {tl}（args 带全体成员；make_args.mjs 会从 team.json 自己加上 guests）：它写圆桌 "
               f"{t}/{cfg['roundtable']}/SKILL.md 里客座的 Team 表行、座次、fault line 与 Guest seat 说明，"
               f"以及 README 里客座的 lens 与安装行；这一步没改圆桌 SKILL.md 和 DEEP-READING.md")
    root_opt = "" if same_path(team_dir.parent, DEFAULT_ROOT) else f" --root {display(team_dir.parent)}"
    out.append(f"  · 这一步只在 README 的成员表里加了行。按客座名单渲染的这些句子还只列着先前的客座（加的是第一位客座时还没有）："
               f"README 开头那句的客座子句、安装一节两种 shell 的客座行（每支主队一行注释，其下是 bash 的 cp -r、PowerShell 的 Copy-Item）；"
               f"圆桌 SKILL.md 的 description、`Members:` 一行、首次激活的免责声明、Loading the Team 里客座的解析句、"
               f"卡片位置那句；DEEP-READING.md 的客座指引。逐字的新文本：python3 {display(HERE / 'new_team.py')} "
               f"{display(team_dir / 'team.json')}{root_opt} --guest-text（只读，打印 JSON）。T2 照它刷新 README 和圆桌"
               f"（轻量档连 DEEP-READING.md 一起），深读档的 DEEP-READING.md 由 T3.8 刷新")
    out.append(f"  · 已做过深读的团队：T2 之后再跑 {display(HERE / 'workflows/team-integrate.js')}（T3.8）；"
               f"客座的覆盖数字留在 home 队的 DEEP-READING.md，不抄过来")
    out.append(f"  · 闸门：{py('team_check.py')} {t}（guests 一项查客座能否解析、SKILL.md 与 Roundtable Card 是否齐全）")
    out.append(f"  · 全流程见 {display(REPO / 'references/research-team-playbook.md')} §八；每个阶段结束就 commit（容器随时可能被回收）。")
    return out


def next_steps(cfg: dict, team_dir: Path, adding: list[str], leak: bool, base_tier: bool = False,
               guests: list[dict] | None = None, adding_guests: list[str] | None = None) -> list[str]:
    t = display(team_dir)
    py = lambda s: f"python3 {display(HERE / s)}"
    wf = display(HERE / "workflows/README.md")
    guests = guests or []
    if adding_guests:
        return guest_next_steps(cfg, team_dir, [g for g in guests if g["slug"] in adding_guests])
    out = ["下一步:"]
    ms = [m for m in cfg["members"] if not adding or m["slug"] in adding]
    no_sch = [m["slug"] for m in ms if not (m.get("scholar") or "").strip()]
    no_hint = [m["slug"] for m in ms if not (m.get("hint") or "").strip()]
    if no_sch or no_hint:
        out.append("  · 先补 team.json：" + "；".join(x for x in [
            f"没有 scholar id 的 {', '.join(no_sch)}（有主页就填；确实没有就留空：harvest 先按姓名搜一次，再以 DBLP/主页为主列表；"
            f"--lookup 可从 DBLP 补 dblp/orcid/homepage）" if no_sch else "",
            f"没有 hint 的 {', '.join(no_hint)}（消歧需要）" if no_hint else ""] if x))
    out.append(f'  · grep -rn "TODO" {t}      # 列出所有待补项')
    who = f"成员 {', '.join(adding)} " if adding else "每位成员"
    out.append(f"  · T1 {who}的基础 Skill：{display(HERE / 'workflows/team-base-skills.js')}（启动方式见 {wf}；"
               f"每位成员一个 workflow 并行）；闸门 {py('quality_check.py')} {t}/<成员>/SKILL.md --mode research → 12/12")
    if guests and not adding:
        for hg in by_home(guests).values():
            out.append(f"  · 客座 {', '.join(g['slug'] for g in hg)} 的 T1、T3、T4 在 home 队 {display(Path(hg[0]['_dir']).parent)} "
                       f"跑，不在这里；本队不给客座建文件夹、RESOURCES.md 或 private/")
    if adding:
        out.append(f"  · 圆桌 {t}/{cfg['roundtable']}/SKILL.md：把新成员加进名单、座次和 Roundtable Card"
                   f"（手改或重跑 {display(HERE / 'workflows/team-layer.js')}）；README 里他那一行的 lens 也要填")
        out.append(f"  · 已做过深读的团队：新成员走 T3（见 playbook），再用 {py('team_status.py')} {t} --coverage 刷新 DEEP-READING.md 的覆盖表")
    else:
        tier = "（轻量档：args.deep_tier = false）" if base_tier else "（只做轻量档时 args.deep_tier = false）"
        out.append(f"  · T2 团队层：{display(HERE / 'workflows/team-layer.js')}{tier}；闸门 {py('check_links.py')} {t}")
        if guests:
            waiting = [g["slug"] for g in guests if not (Path(g["_dir"]) / "SKILL.md").is_file()]
            out.append("  · 有客座：T2 要等每位客座的 SKILL.md 已在本分支的 home 队目录里（先合并 home 队的分支）"
                       + (f"，还缺 {', '.join(waiting)}" if waiting else "，现在都有了")
                       + "；make_args.mjs 会从 team.json 把 guests 加进 T2 / T3.8 的 args")
            out += broken_link_steps(guests)
    out.append(f"  · 进度：{py('team_status.py')} {t}")
    out.append(f"  · 全流程见 {display(REPO / 'references/research-team-playbook.md')}；每个阶段结束就 commit（容器随时可能被回收）。")
    if leak:
        out.append("  · 先按上面补好 .gitignore 再提交：PDF/PS/DjVu/EPUB、papers/txt/ 和 private/（README.md 除外）不能进仓库。")
    else:
        out.append("  · PDF/PS/DjVu/EPUB、papers/txt/ 和 private/（README.md 除外）被 .gitignore 忽略：不要 git add -f，"
                   "版权全文与私人材料不进仓库；commit 前看一眼 git status。")
    return out


def scaffold(a) -> int:
    src = Path(a.team_json)
    if not src.is_file():
        print(f"❌ 找不到 {a.team_json}")
        return 1
    cfg, errs = load_config(src)
    extra = {}
    for kv in a.set or []:
        k, sep, v = kv.partition("=")
        if not sep or not re.fullmatch(r"[A-Za-z0-9_]+", k):
            errs.append(f"--set {kv!r} 应为 NAME=VALUE")
        else:
            extra[k] = v
    if errs:
        for e in errs:
            print(f"❌ {e}")
        print(f"❌ team.json 有 {len(errs)} 处问题，什么都没写")
        return 1
    adding = list(dict.fromkeys(a.add_member or []))
    adding_guests = list(dict.fromkeys(a.add_guest or []))
    plan = build_plan(a, src, cfg, adding, extra, adding_guests)
    for n in plan.notes:
        print(n)
    if plan.errors:
        for e in plan.errors:
            print(f"❌ {e}")
        if plan.guest_stop and all(e in plan.guest_errors for e in plan.errors):  # 只因等合并的客座解析不了而停下
            print(guest_stop_hint(plan.guest_stop, adding))
        print(f"❌ {len(plan.errors)} 个问题，什么都没写")
        return 1
    print(f"{'(dry run) ' if a.dry_run else ''}{display(plan.team_dir)}/")
    counts, todos = execute(plan, a.dry_run)
    if adding_guests:  # 客座不建文件夹：没有要查 .gitignore 的东西（他的文件夹由 home 队查）
        leak, git_msg = False, "· git: --add-guest 不建文件夹，没检查（客座的文件夹在 home 队，那里的 new_team.py 查过）"
    else:
        leak, git_msg = git_ignore_check(plan.team_dir, [m["slug"] for m in cfg["members"] if not adding or m["slug"] in adding])
    print(git_msg)
    print()
    for line in next_steps(cfg, plan.team_dir, adding, leak, a.base_tier, plan.guests, adding_guests):
        print(line)
    if adding_guests:
        what = f"guest {', '.join(adding_guests)}"
    elif adding:
        what = f"member {', '.join(adding)}"
    else:
        what = f"team {cfg['team']} ({len(cfg['members'])} members" + (f" + {len(plan.guests)} guests" if plan.guests else "") + ")"
    verb = "would scaffold" if a.dry_run else "scaffolded"
    print(f"{'❌' if leak else '✅'} {verb} {what}: created {counts['created']} files + {counts['dirs']} folders, "
          f"updated {counts['updated']}, kept {counts['kept']}, overwritten {counts['overwritten']} · "
          f"{todos} [TODO markers in written files" + (" · .gitignore does not cover it" if leak else ""))
    return 1 if leak else 0


GUEST_TEXT_KEYS = ("SEATED_LIST",) + GUEST_KEYS


def guest_text(a) -> int:
    """--guest-text（只读）：本队客座在模板里渲染出的文本，一个 JSON 对象打到 stdout（UTF-8）：guests（每位
    {slug, home, name, home_title, dir}）、SEATED_LIST、各 GUEST_* 占位符的值、README_GUEST_ROWS（README 成员表的客座行）、
    ROUNDTABLE_GUEST_ROWS（圆桌 Team 表的客座行），都与铺目录时渲染的逐字相同（T2 / T3.8 照抄，--add-guest 之后刷新句子用）。
    解析提示打到 stderr；有客座解析不了时，错误（与铺目录时同样的句子）打到 stderr，退出码 1，不打 JSON。
    没有客座时 GUEST_* 都是空串、两个列表为空（SEATED_LIST 与铺目录时一样 = 成员名单），退出码 0。什么都不写。"""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    src = Path(a.team_json)
    if not src.is_file():
        print(f"❌ 找不到 {a.team_json}", file=sys.stderr)
        return 1
    cfg, errs = load_config(src)
    if errs:
        for e in errs:
            print(f"❌ {e}", file=sys.stderr)
        return 1
    root = Path(a.root)
    guests, gerrs, notes = resolve_guests(cfg, root)
    for n in notes:
        print(n, file=sys.stderr)
    if gerrs:
        for e in gerrs:
            print(f"❌ {e}", file=sys.stderr)
        print(f"❌ --guest-text: {len(gerrs)} guest problem(s), no text printed", file=sys.stderr)
        return 1
    v = team_values(cfg, root / cfg["team"], {}, guests)
    default = same_path(root, DEFAULT_ROOT)
    out: dict = {"guests": [{"slug": g["slug"], "home": g["_home"], "name": g["name"], "home_title": g["_home_title"],
                             "dir": f"product/{g['_home']}/{g['slug']}" if default else display(Path(g["_dir"]))}
                            for g in guests]}
    out.update({k: v[k] for k in GUEST_TEXT_KEYS})
    out["README_GUEST_ROWS"] = [guest_row(g) for g in guests]
    out["ROUNDTABLE_GUEST_ROWS"] = [guest_roundtable_row(g) for g in guests]
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


# ---------- 改成员字段 / 从 DBLP 补全 ----------

def write_config(path: Path, cfg: dict, dry: bool, changes: list[str]) -> int:
    for c in changes:
        print(c)
    if not changes:
        print(f"= {display(path)}: nothing to change")
        return 0
    if dry:
        print(f"✅ (dry run) would update {display(path)} ({len(changes)} change(s))")
        return 0
    path.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"✅ updated {display(path)} ({len(changes)} change(s)); commit it with the team")
    return 0


def set_member(a) -> int:
    path = Path(a.team_json)
    cfg, errs = load_config(path)
    if errs:
        for e in errs:
            print(f"❌ {e}")
        return 1
    m = next((x for x in cfg["members"] if x.get("slug") == a.set_member), None)
    home = next((g["home"] for g in cfg.get("guests") or [] if g["slug"] == a.set_member), None)
    if m is None and home:  # 客座的字段在 home 队的 team.json 里
        print(f"❌ {a.set_member!r} is a guest from {home}: its fields live in the home team: python3 "
              f"{display(HERE / 'new_team.py')} {display(teams_root(path.parent) / home / 'team.json')} "
              f"--set-member {a.set_member} KEY=VALUE ...")
        return 1
    if m is None:
        print(f"❌ {a.set_member!r} is not a member slug in {display(path)}: {', '.join(x['slug'] for x in cfg['members'])}")
        return 1
    allowed = set(MEMBER_STR_KEYS) | {"living", "student_mode", "chase_hints"}
    changes = []
    for kv in a.pairs:
        k, sep, v = kv.partition("=")
        if not sep or k not in allowed:
            print(f"❌ {kv!r}: use KEY=VALUE with KEY one of {', '.join(sorted(allowed))}")
            return 1
        if k in ("living", "student_mode"):
            if v.lower() not in ("true", "false"):
                print(f"❌ {k} takes true or false, not {v!r}")
                return 1
            val = v.lower() == "true"
        elif k == "chase_hints":
            try:
                val = json.loads(v)
            except json.JSONDecodeError as e:
                print(f"❌ chase_hints takes a JSON list of strings: {e}")
                return 1
            if not (isinstance(val, list) and all(isinstance(x, str) for x in val)):
                print("❌ chase_hints takes a JSON list of strings")
                return 1
        else:
            val = v.strip()
            if k == "dblp":
                val = re.sub(r"^https?://dblp\.org/pid/|\.html$", "", val)
            if k == "scholar":
                mm = re.search(r"user=([\w-]+)", val)
                val = mm.group(1) if mm else val
        if m.get(k) != val:
            changes.append(f"~ {a.set_member}.{k}: {json.dumps(m.get(k), ensure_ascii=False)} → {json.dumps(val, ensure_ascii=False)}")
            m[k] = val
    if any(".surname:" in c for c in changes):
        for w in surname_clashes(cfg["members"] + resolve_guests(cfg, teams_root(path.parent))[0]):
            print(w)
    return write_config(path, cfg, a.dry_run, changes)


def lookup(a) -> int:
    path = Path(a.team_json)
    cfg, errs = load_config(path)
    if errs:
        for e in errs:
            print(f"❌ {e}")
        return 1
    sys.path.insert(0, str(HERE))
    import dblp_works as dw
    only = [x for x in (a.member or "").split(",") if x]
    gh = {g["slug"]: g["home"] for g in cfg.get("guests") or []}
    for s in only:
        if s in gh:  # 客座的 dblp / orcid / homepage 归 home 队
            print(f"· {s} is a guest from {gh[s]}: its ids live in the home team: python3 {display(HERE / 'new_team.py')} "
                  f"{display(teams_root(path.parent) / gh[s] / 'team.json')} --lookup --member {s}")
    changes, rc = [], 0
    for m in cfg["members"]:
        if only and m["slug"] not in only:
            continue
        pid, how = (m.get("dblp") or "").strip(), ""
        try:
            if not pid:
                pids = []
                if (m.get("scholar") or "").strip():
                    pids, how = dw.find_by_scholar(m["scholar"]), "its Scholar link on the DBLP person page"
                if not pids and (m.get("orcid") or "").strip():
                    pids, how = dw.find_by_orcid(m["orcid"]), "its ORCID"
                if not pids:
                    cand, exact = dw.find_by_name(m["name"])
                    pids, how = sorted(exact), "name only"
                    if len(exact) != 1:
                        print(f"· {m['slug']}: {len(exact)} exact-name DBLP candidates (of {len(cand)}); pick one by hand: "
                              f"python3 scripts/dblp_works.py --name \"{m['name']}\"")
                        continue
                if len(pids) != 1:
                    print(f"· {m['slug']}: {len(pids)} DBLP persons match {how}; not filled "
                          f"(python3 scripts/dblp_works.py --name \"{m['name']}\" lists candidates)")
                    continue
                pid = pids[0]
                changes.append(f"~ {m['slug']}.dblp: \"\" → \"{pid}\" (matched by {how}: https://dblp.org/pid/{pid}.html)")
                if how == "name only":
                    changes.append(f"  ⚠️ {m['slug']}: matched by name only; check https://dblp.org/pid/{pid}.html against the hint "
                                   f"({m.get('hint') or 'no hint'}) and clear dblp if it is someone else")
                m["dblp"] = pid
            info = dw.person_info([pid]).get(pid, {})
        except Exception as e:  # network or endpoint errors: report and go on
            print(f"❌ {m['slug']}: DBLP lookup failed ({e})")
            rc = 1
            continue
        orcids = [dw.short(o, "https://orcid.org/") for o in info.get("orcid", [])]
        homes = list(dict.fromkeys(info.get("primaryHomepage", []) + info.get("homepage", [])))
        if not (m.get("orcid") or "").strip() and len(orcids) == 1:
            changes.append(f"~ {m['slug']}.orcid: \"\" → \"{orcids[0]}\" (from DBLP {pid})")
            m["orcid"] = orcids[0]
        if not (m.get("homepage") or "").strip() and homes:
            changes.append(f"~ {m['slug']}.homepage: \"\" → \"{homes[0]}\" (from DBLP {pid})")
            m["homepage"] = homes[0]
    return write_config(path, cfg, a.dry_run, changes) or rc


# 加 --add-guest 之前，argparse 把 --a、--ad、--add、--add-（也含 =VALUE 写法）补全成唯一以它们开头的 --add-member；
# 有了 --add-guest，这几个缩写会报 ambiguous option。照旧当 --add-member 用，以前能跑的命令行照样能跑（--add-guest 的
# 缩写从 --add-g 起；allow_abbrev 不关，--dry 这类缩写照旧）。--help 不变。
ADD_MEMBER_ABBREVS = ("--a", "--ad", "--add", "--add-")


def old_add_abbrevs(argv: list[str]) -> list[str]:
    out = []
    for i, x in enumerate(argv):
        if x == "--":  # 之后都是位置参数，不动
            return out + argv[i:]
        opt, sep, val = x.partition("=")
        out.append("--add-member" + sep + val if opt in ADD_MEMBER_ABBREVS else x)
    return out


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description="起草 team.json / 按模板铺研究团队目录 / 给团队加成员或客座")
    ap.add_argument("team_json", nargs="?", help="team.json（铺目录、--add-member、--add-guest、--guest-text 时）")
    ap.add_argument("--init", metavar="TEAM_SLUG", help="起草 team.json")
    ap.add_argument("--field", help="--init: 领域（写进 team.json 的 field）")
    ap.add_argument("--members", help='--init: 成员姓名，分号分隔 "Name One;Name Two"')
    ap.add_argument("--title", help="--init: 团队标题（默认由 slug 生成）")
    ap.add_argument("--language", default="English", help="--init: 成员 Skill 与卡片的语言（默认 English）")
    ap.add_argument("--out", help="--init: team.json 写到哪（默认 <--root>/<slug>/team.json）")
    ap.add_argument("--root", default=str(DEFAULT_ROOT), help=f"团队目录的上级（默认 {display(DEFAULT_ROOT)}）")
    ap.add_argument("--templates", default=str(DEFAULT_TEMPLATES), help=f"模板目录（默认 {display(DEFAULT_TEMPLATES)}）")
    ap.add_argument("--add-member", action="append", metavar="SLUG", help="只铺这位（已写进 team.json 的）成员，可重复")
    ap.add_argument("--add-guest", action="append", metavar="SLUG",
                    help="把这位（已写进 team.json 的 guests 的）客座加进 README 成员表，不建文件夹，可重复")
    ap.add_argument("--guests", metavar='"HOME/SLUG;HOME/SLUG"',
                    help="--init: 客座（别队的成员，home 是那队的文件夹名），写成 team.json 的 guests")
    ap.add_argument("--set", action="append", metavar="NAME=VALUE", help="补充或覆盖模板占位符，可重复")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的文件")
    ap.add_argument("--dry-run", action="store_true", help="只显示会做什么")
    ap.add_argument("--base-tier", action="store_true",
                    help="只做轻量档：DEEP-READING.md 写成轻量档说明，RESOURCES.md 去掉深读档占位行")
    ap.add_argument("--set-member", metavar="SLUG", help="改 team.json 里这位成员的字段：后面跟 KEY=VALUE ...")
    ap.add_argument("pairs", nargs="*", metavar="KEY=VALUE", help="--set-member 的字段")
    ap.add_argument("--lookup", action="store_true", help="从 DBLP 补全空着的 dblp / orcid / homepage（联网）")
    ap.add_argument("--member", help="--lookup：只查这几位（逗号分隔 slug）")
    ap.add_argument("--guest-text", action="store_true",
                    help="只读：打印本队客座渲染出的文本（JSON：guests、SEATED_LIST、GUEST_* 的值、README 与圆桌 Team 表的客座行）")
    a = ap.parse_intermixed_args(old_add_abbrevs(sys.argv[1:]))
    if a.guest_text:
        if not a.team_json or a.init or a.add_member or a.add_guest or a.guests is not None or a.set_member or a.lookup \
                or a.pairs or a.set or a.force or a.base_tier:
            ap.error("--guest-text takes a team.json (and --root) and nothing else (no --init, --add-member, --add-guest, "
                     "--guests, --set-member, --lookup, --set, --force, --base-tier)")
        sys.exit(guest_text(a))
    if a.pairs and not a.set_member:
        ap.error(f"unexpected arguments: {' '.join(a.pairs)} (KEY=VALUE pairs go with --set-member)")
    if a.set_member or a.lookup:
        if not a.team_json or a.init or a.add_member or a.base_tier or (a.set_member and a.lookup):
            ap.error("--set-member / --lookup take a team.json and nothing else (no --init, --add-member, --base-tier)")
        if a.add_guest or a.guests is not None:
            ap.error("--set-member / --lookup take a team.json and nothing else (no --add-guest, --guests)")
        if a.set_member and not a.pairs:
            ap.error("--set-member needs KEY=VALUE pairs, e.g. --set-member ada-example dblp=12/3456")
        sys.exit(set_member(a) if a.set_member else lookup(a))
    if a.init:
        if a.team_json or a.add_member or a.base_tier:
            ap.error("--init 不能和 team.json / --add-member / --base-tier 同时用（--base-tier 用在第 2 步）")
        if a.add_guest:
            ap.error("--init 不能和 --add-guest 同时用（起草时用 --guests \"home/slug;home/slug\"）")
        if not a.field or not a.members:
            ap.error("--init 需要 --field 和 --members")
        sys.exit(init_team(a))
    if a.guests is not None:
        ap.error('--guests 只跟 --init 用；已有团队先把 {"slug": …, "home": …} 写进 team.json 的 guests，再 --add-guest <slug>')
    if a.add_guest and (a.add_member or a.base_tier):
        ap.error("--add-guest 不能和 --add-member / --base-tier 同时用（分开跑；客座不建文件夹，没有档位）")
    if not a.team_json:
        ap.error("需要 team.json，或用 --init 起草一个")
    sys.exit(scaffold(a))


if __name__ == "__main__":
    main()
