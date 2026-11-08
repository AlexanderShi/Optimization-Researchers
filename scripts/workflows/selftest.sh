#!/usr/bin/env bash
# selftest.sh — self-test of the research-team kit (run after changing any workflow or kit script; no tokens spent).
#
#   bash scripts/workflows/selftest.sh [product/<finished team>]      e.g. product/dfo-team, the worked example
#
# Without a team only parts 1 (no --forbid), 3 (without team_check.py) and 4 run; give a finished team for the full test.
# 1. The nine example previews (examples/*.args.json + *.answers.json) with dry_run.mjs --strict, plus the variants that
#    take other branches (base-tier team-layer; team-synthesize / team-increment resumed with from: "review" / "fix").
#    --forbid is built from the finished team's team.json (team and roundtable slugs, member surnames), so nothing of
#    that team may leak into the generic workflows.
# 2. make_args.mjs for every workflow on the finished team, and dry_run.mjs --team <team> (no args file) --strict for
#    every workflow: the args a real launch would get.
# 3. Every kit script compiles and answers --help; team_status.py --coverage runs; team_check.py <team> exits 0
#    (the delivery gate: links, templates, git, roundtable, coverage tables, 12/12, quotes, ledgers, works).
# 4. Guest seats fixture (no finished team needed, no tokens): a fictional host team seats a member of a fictional home
#    team as a guest (team.json "guests"), in a temporary repo root. new_team.py --dry-run and scaffold (guest rows, no
#    guest folder) and --guest-text (its keys; each string as the scaffold wrote it, the comment and Copy-Item lines under
#    the PowerShell copy line, the bash lines safe to paste into zsh; with three guests from two homes, one comment line
#    per home team, "guests" for two and the title without the characters a shell treats specially, over its guests'
#    copy lines, in --guest-text and under both shells' copy lines; dir with the default and another --root; empty
#    without guests); make_args.mjs (args.guests
#    with dir for team-layer / team-integrate, none for team-base-skills); dry_run.mjs --team --strict for both, with the
#    default fakes and with answers files that reach the guest branches, each also under --check-answers (no answer
#    sets a field its agent's schema lacks): team-integrate with a ready member, with a ready member and a guest without
#    SKILL.md (not seated: its T1 and a team-layer.js rerun first), and with none ready but a carded guest and a guest
#    without SKILL.md; team-layer at the base tier with a carded guest (the guest digest and both verifiers keep the
#    guest's folder read-only), with an own member or a guest without a skill, with a guest without a skill or whose
#    digest agent returned nothing beside a seated guest (the README author, both verifiers and the fixer are told, the
#    TODO items kept for them and the README link check_links.py counts as broken included; that link alone is no failing
#    gate of the fixer, another broken link is; "next" names the team_check.py rows that stay red on such a guest, its
#    roundtable row included, at either tier), and on a team under teams/ instead of product/ (team-layer and
#    team-integrate run --guest-text with --root <repo>/teams; the guests' install lines take the path fix of the team's
#    own copy line); the guests row of
#    team_check.py, also run as team_check.py . (and team_status.py .) inside the host folder; the hosts row on the home
#    team; team_status.py (Guests after the coverage table, --json guests); a negative copy (not a member at home: the
#    resolver's error and its "merge it first" advice from new_team.py, its --guest-text, make_args.mjs and
#    team_check.py); new_team.py's stop hint (how to scaffold without the guests that do not resolve) only when every
#    guest error is one a merge of the home team's branch cures: printed, naming the guest, for the negative copy (with
#    --add-guest's "scaffold without it" clause on a team not scaffolded yet) and for a copy whose only guest error is a
#    missing home team.json or a guest folder missing at home, and neither for a case-only slug typo (whose errors ask
#    "did you mean …?") nor for the ten cases below (other errors among them); the resolver's errors for ten cases (a
#    case-only slug typo asks "did you mean …?", also for a member past the eight names the message lists), the same text
#    from new_team.py, make_args.mjs and dry_run.mjs in a real repo layout, and the same note for a guest with research
#    notes but no SKILL.md; a home team.json read as new_team.py reads it (NaN and a member slug ending in a newline
#    resolve; bytes that are not UTF-8 stop both tools; a float, a long int and escaped characters print as repr() does);
#    --add-guest (row added; another unresolvable guest only a note; exit 1 on a team not scaffolded yet); a --base-tier
#    scaffold (the guest pointer ends the DEEP-READING note; the template's base-tier note has no guest placeholder and
#    equals the pre-feature text, commit f9291c1); check_links.py (a guest link to a scaffolded home folder without notes
#    is pending). Its previews take the finished team's --forbid too, unless the temporary folder's own path matches it
#    (a TMPDIR naming one of its words, which every fixture prompt would carry): then they run without it, and a note
#    line says so.
# Read-only against the repo: dry runs write nothing, scratch output (part 4's fixture too) goes to a temporary folder
# that is removed.
# Exit code: the number of failed checks (0 = all passed).
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
REPO=$(cd "$HERE/../.." && pwd)
cd "$REPO" || exit 99
TEAM=${1:-}
TMP=$(mktemp -d "${TMPDIR:-/tmp}/nuwa-selftest.XXXXXX")
trap 'rm -rf "$TMP"' EXIT
fail=0
ok() { printf '  ✓ %s\n' "$1"; }
bad() { printf '  ✗ %s\n' "$1"; fail=$((fail + 1)); }
WF="base-skills layer harvest chase read synthesize tighten increment integrate"

FORBID='$^'   # matches nothing
if [ -n "$TEAM" ]; then
  [ -f "$TEAM/team.json" ] || { echo "❌ $TEAM/team.json not found"; exit 99; }
  FORBID=$(python3 - "$TEAM/team.json" <<'PY'
import json, re, sys
t = json.load(open(sys.argv[1]))
words = {t["team"], t["roundtable"]} | {m.get("surname") or m["name"].split()[-1] for m in t["members"]}
print(r"\b(" + "|".join(sorted(re.escape(w) for w in words if len(w) > 2)) + r")\b")
PY
)
  echo "kit self-test · finished team $TEAM · forbid $FORBID"
else
  echo "kit self-test · no finished team given (parts 2 and team_check.py skipped; e.g. bash $0 product/dfo-team)"
fi

echo "1. example previews (strict)"
dry() {  # label, workflow, args (file or inline JSON), answers file
  local out rc
  out=$(node scripts/workflows/dry_run.mjs "scripts/workflows/team-$2.js" "$3" --answers "$4" --quiet --strict --forbid "$FORBID" 2>&1)
  rc=$?
  if [ $rc -eq 0 ]; then ok "$1 ($(grep -m1 '^agents' <<<"$out" | sed 's/  */ /g'))"; else bad "$1 (exit $rc)"; grep -E '^  - |✗' <<<"$out" | head -5; fi
}
for w in $WF; do
  dry "team-$w" "$w" "scripts/workflows/examples/team-$w.args.json" "scripts/workflows/examples/team-$w.answers.json"
done
dry "team-layer deep_tier false" layer "$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));d["deep_tier"]=False;print(json.dumps(d))' scripts/workflows/examples/team-layer.args.json)" scripts/workflows/examples/team-layer.answers.json
for w in synthesize increment; do
  for f in review fix; do
    a=$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));d["from"]=sys.argv[2];[d.pop(k,None) for k in ("find","since","what")];print(json.dumps(d))' "scripts/workflows/examples/team-$w.args.json" "$f")
    dry "team-$w from $f" "$w" "$a" "scripts/workflows/examples/team-$w.answers.json"
  done
done

[ -n "$TEAM" ] && echo "2. make_args.mjs and dry_run.mjs --team on $TEAM"
for w in $WF; do
  [ -n "$TEAM" ] || break
  if node scripts/workflows/make_args.mjs "team-$w" --team "$TEAM" --date 2026-01-01 --scratch "$TMP/scratch" > "$TMP/calls-$w.json" 2>/dev/null \
     && python3 -c 'import json,sys;c=json.load(open(sys.argv[1]));assert c and all(x["args"]["members"] for x in c)' "$TMP/calls-$w.json"; then
    out=$(node scripts/workflows/dry_run.mjs "scripts/workflows/team-$w.js" --team "$TEAM" --scratch "$TMP/scratch" --quiet --strict 2>&1)
    rc=$?
    if [ $rc -eq 0 ]; then ok "team-$w: $(python3 -c 'import json,sys;print(len(json.load(open(sys.argv[1]))))' "$TMP/calls-$w.json") call(s); preview $(grep -m1 '^agents' <<<"$out" | sed 's/  */ /g')"
    else bad "team-$w: dry_run --team exit $rc"; grep -E '^  - |✗' <<<"$out" | head -5; fi
  else bad "team-$w: make_args.mjs failed"; fi
done

echo "3. scripts and the delivery gate"
for f in scripts/*.py; do
  python3 -m py_compile "$f" 2>/dev/null || { bad "py_compile $f"; continue; }
  case $(basename "$f") in
    merge_research.py|mark_read_from_cards.py|srt_to_transcript.py|quality_check.py) continue ;;  # no argparse --help
  esac
  python3 "$f" --help > /dev/null 2>&1 || bad "$f --help"
done
ok "py_compile + --help"
bash -n scripts/team_commit.sh && ok "team_commit.sh parses" || bad "team_commit.sh does not parse"
if [ -n "$TEAM" ]; then
  python3 scripts/team_status.py "$TEAM" --coverage > /dev/null && ok "team_status.py --coverage" || bad "team_status.py --coverage"
  out=$(python3 scripts/team_check.py "$TEAM" 2>&1); rc=$?
  if [ $rc -eq 0 ]; then ok "team_check.py: $(tail -1 <<<"$out")"; else bad "team_check.py exit $rc"; grep '✗' <<<"$out" | head -8; fi
fi

echo "4. guest seats fixture (fictional home and host teams in a temporary repo root)"
# product/host-example-team seats cy-sample, a member of product/home-example-team, as a guest. The fixture repo root
# is under $TMP (removed on exit with the other scratch output); the kit runs from this repo with --root / --repo.
# The variants are copies of it under $TMP: a real repo layout (scripts/new_team.py beside product/, run from its root
# with the default --root), three guests from two homes, ten guests that do not resolve, --add-guest, --base-tier, a
# guest that is not a member at home, a guest whose home team.json or folder is missing, a home folder without notes.
FX="$TMP/guest-fixture"
HOME_TEAM="$FX/product/home-example-team"
HOST_TEAM="$FX/product/host-example-team"
GROW='| [Cy Sample](../home-example-team/cy-sample/SKILL.md) | lens: [TODO] | guest from [Home Example Team](../home-example-team/README.md) · T1 base skill |'
GMSG='guest ed-nobody: not a member of home-example-team'   # the resolver's error in the negative copy
MERGE='merge it first (playbook §八, 加一位客座成员 step 2)'   # and its first advice (the home team's branch is not merged)
# the previews below take the finished team's --forbid too (the guest branches must not leak that team either), unless
# the temporary folder's own path matches it (a TMPDIR naming the team, its roundtable or a surname): every fixture
# prompt carries that path, so each preview would fail although nothing leaked. They then run without it, with a note
GFORBID=$FORBID
if [ -n "$TEAM" ] && fw=$(node -e 'const [re, p] = process.argv.slice(1), r = new RegExp(re), m = r.exec(p) || r.exec(require("path").resolve(p)); if (!m) process.exit(1); console.log(m[0])' "$FORBID" "$TMP" 2> /dev/null); then
  GFORBID='$^'
  echo "  · the temporary folder's path matches --forbid (\"$fw\"): part 4's previews run without it (every fixture prompt carries that path)"
fi
skill_md() {  # slug, name: a minimal SKILL.md with a complete Roundtable Card
  printf -- '---\nname: %s\ndescription: FICTIONAL research-craft skill of %s for the kit self-test.\n---\n\n# %s\n\n' "$1" "$2" "$2"
  printf -- '## Roundtable Card\n\n- **Lens (one line)**: a fictional lens.\n- **Leads when**: a fictional signal.\n'
  printf -- '- **First questions asked**: a fictional question.\n- **Default recommendation**: a fictional plan.\n'
  printf -- '- **Will push back on**: a fictional claim.\n- **Likely disagreements**: none documented (fixture).\n'
  printf -- '- **Blind spots**: everything outside the fixture.\n\n## Honest Boundary\n\n- Fixture only.\n'
}
note_md() { printf '# 01 Publications (fictional)\n\n- One research note.\n'; }
team_json() {  # team, title, member entry (JSON), guest slug from home-example-team or "" (no "guests" key)
  local guests=""
  [ -n "$4" ] && guests=$(printf ',\n "guests": [{"slug": "%s", "home": "home-example-team"}]' "$4")
  printf '{\n "schema": 1,\n "team": "%s",\n "title": "%s",\n "field": "fictional field of the kit self-test",\n' "$1" "$2"
  printf ' "language": "English",\n "created": "2026-01-01",\n "roundtable": "%s-roundtable",\n "chase_hints": [],\n' "${1%-team}"
  printf ' "card_dimensions": {},\n "members": [\n  %s\n ]%s\n}\n' "$3" "$guests"
}
# Cy Sample's entry has no "living": a guest's entry is copied verbatim, never completed
CY='{"slug": "cy-sample", "name": "Cy Sample", "surname": "Sample", "hint": "FICTIONAL placeholder of the kit self-test", "scholar": "", "dblp": "", "orcid": "", "homepage": "", "chase_hints": [], "student_mode": false}'
DI='{"slug": "di-example", "name": "Di Example", "surname": "Example", "living": true, "hint": "FICTIONAL placeholder of the kit self-test", "scholar": "", "dblp": "", "orcid": "", "homepage": "", "chase_hints": [], "student_mode": false}'
guest_args() {  # make_args.mjs output, workflow: the team-level call carries args.guests (home entry + home + dir), per-member calls none
  python3 - "$1" "$HOME_TEAM/team.json" "$2" 2>&1 <<'PY'
import json, sys
calls = json.load(open(sys.argv[1], encoding="utf-8"))
home = json.load(open(sys.argv[2], encoding="utf-8"))["members"][0]
if sys.argv[3] == "base-skills":
    if not calls or any("guests" in c["args"] for c in calls):
        sys.exit("a per-member call carries args.guests")
    print(f"{len(calls)} call(s), no args.guests")
else:
    want = dict(home, home="home-example-team", dir="product/home-example-team/cy-sample")
    got = calls[0]["args"].get("guests") if len(calls) == 1 else None
    g = got[0] if isinstance(got, list) and len(got) == 1 and isinstance(got[0], dict) else None
    if g != want:
        show = lambda d, k: json.dumps(d[k]) if k in d else "(missing)"
        sys.exit(f"{len(calls)} call(s); " + ("args.guests[0]: " + ", ".join(f"{k} {show(g, k)} (expected {show(want, k)})"
                 for k in sorted(set(g) | set(want)) if show(g, k) != show(want, k))
                 if g is not None else f"args.guests = {json.dumps(got)[:160]}"))
    print(f"args.guests = cy-sample with dir {g['dir']}, its home entry verbatim")
PY
}
check_row() {  # team_check.py --json output, check name -> "<status> <detail>" ("none" without that row)
  python3 -c 'import json,sys;r=[c for c in json.load(open(sys.argv[1],encoding="utf-8"))["checks"] if c["check"]==sys.argv[2]];print(*((r[0]["status"],r[0]["detail"]) if r else ("none",)))' "$1" "$2" 2>/dev/null || echo "none (no JSON)"
}
jedit() {  # file, Python statements on d: edits a fixture's JSON file in place
  python3 -c 'import json,sys;p=sys.argv[1];d=json.load(open(p,encoding="utf-8"));exec(sys.argv[2]);open(p,"w",encoding="utf-8").write(json.dumps(d,ensure_ascii=False,indent=1)+"\n")' "$1" "$2"
}
report() {  # label, exit code of a check script, its output (a summary, or one problem per line): ✓, or ✗ with the problems
  if [ "$2" -eq 0 ]; then ok "$1: $3"; else bad "$1: $(head -1 <<<"$3")"; tail -n +2 <<<"$3" | head -6 | sed 's/^/    /'; fi
}
lacks() {  # a tool's output in the negative copy -> the texts it lacks (", no …" each; "" = both are there)
  grep -qF "$GMSG" <<<"$1" || printf ', no "%s …"' "$GMSG"
  grep -qF "$MERGE" <<<"$1" || printf ', no "%s"' "$MERGE"
}
mkdir -p "$HOME_TEAM" "$HOST_TEAM/di-example/references/research"
team_json home-example-team "Home Example Team" "$CY" "" > "$HOME_TEAM/team.json"
team_json host-example-team "Host Example Team" "$DI" cy-sample > "$HOST_TEAM/team.json"
skill_md di-example "Di Example" > "$HOST_TEAM/di-example/SKILL.md"
note_md > "$HOST_TEAM/di-example/references/research/01-publications.md"
out=$(python3 scripts/new_team.py "$HOME_TEAM/team.json" --root "$FX/product" 2>&1); rc=$?
if [ $rc -ne 0 ] || [ ! -d "$HOME_TEAM/cy-sample/references/research" ]; then
  bad "fixture: new_team.py did not scaffold the home team (exit $rc); the guest checks are skipped"; grep '❌' <<<"$out" | head -5
else
  skill_md cy-sample "Cy Sample" > "$HOME_TEAM/cy-sample/SKILL.md"
  note_md > "$HOME_TEAM/cy-sample/references/research/01-publications.md"
  # T0 of the host: the dry run resolves the guest and plans no folder for it; the scaffold writes the guest rows
  # (--dry-run lists the files it would write, not their text, so the rows are checked in the written files)
  out=$(python3 scripts/new_team.py "$HOST_TEAM/team.json" --root "$FX/product" --dry-run 2>&1); rc=$?
  if [ $rc -eq 0 ] && grep -qF '(1 members + 1 guests)' <<<"$out" && grep -q '^  + di-example/' <<<"$out" && ! grep -q '^  [+=!~] cy-sample' <<<"$out"; then
    ok "new_team.py --dry-run on the host: guest resolved, member folder planned, no guest folder"
  else bad "new_team.py --dry-run on the host (exit $rc)"; grep -E '❌|cy-sample' <<<"$out" | head -5; fi
  out=$(python3 scripts/new_team.py "$HOST_TEAM/team.json" --root "$FX/product" 2>&1); rc=$?
  probs=""
  [ $rc -eq 0 ] || probs="$probs; exit $rc"
  grep -qF "$GROW" "$HOST_TEAM/README.md" 2>/dev/null || probs="$probs; README.md lacks the guest row $GROW"
  grep -qF '| `cy-sample` | Cy Sample (guest from Home Example Team) |' "$HOST_TEAM/host-example-roundtable/SKILL.md" 2>/dev/null \
    || probs="$probs; the roundtable Team table lacks | \`cy-sample\` | Cy Sample (guest from Home Example Team) |"
  [ ! -e "$HOST_TEAM/cy-sample" ] || probs="$probs; host-example-team/cy-sample exists"
  if [ -z "$probs" ]; then ok "new_team.py scaffold of the host: guest rows in README.md and the roundtable Team table, no guest folder"
  else bad "new_team.py scaffold of the host:${probs#;}"; grep '❌' <<<"$out" | head -5; fi
  # --guest-text (read-only): the guest strings T2 and T3.8 copy, one JSON object on stdout; each one is what the scaffold
  # wrote (README intro and install lines of both shells, roundtable, DEEP-READING.md). dir is product/<home>/<slug> with
  # the default --root: FXR, a copy with scripts/new_team.py beside product/, is run from its root for that
  FXR="$TMP/guest-fixture-repo"
  mkdir -p "$FXR/scripts" && cp scripts/new_team.py "$FXR/scripts/" && cp -r "$FX/product" "$FXR/product"
  python3 scripts/new_team.py "$HOST_TEAM/team.json" --root "$FX/product" --guest-text > "$TMP/guest-text.json" 2> /dev/null; r1=$?
  (cd "$FXR" && python3 scripts/new_team.py product/host-example-team/team.json --guest-text > "$TMP/guest-text-repo.json" 2> /dev/null); r2=$?
  python3 scripts/new_team.py "$HOME_TEAM/team.json" --root "$FX/product" --guest-text > "$TMP/guest-text-home.json" 2> /dev/null; r3=$?
  # three guests from two homes (GM, a copy of FX): a new host seats cy-sample and fe-extra from home-example-team and,
  # written between them in its team.json, xo-second from second-example-team, whose title has characters a shell treats
  # specially; it is scaffolded, then --guest-text runs on it
  GM="$TMP/guest-fixture-two-homes"
  MULTI="$GM/product/multi-example-team"
  cp -r "$FX" "$GM" && mkdir -p "$GM/product/second-example-team" "$MULTI"
  jedit "$GM/product/home-example-team/team.json" 'd["members"].append({"slug": "fe-extra", "name": "Fe Extra", "hint": "FICTIONAL placeholder of the kit self-test"})'
  team_json second-example-team "Second Example Team (B&C)" '{"slug": "xo-second", "name": "Xo Second", "hint": "FICTIONAL placeholder of the kit self-test"}' "" \
    > "$GM/product/second-example-team/team.json"
  for g in home-example-team/fe-extra second-example-team/xo-second; do
    mkdir -p "$GM/product/$g/references/research" && note_md > "$GM/product/$g/references/research/01-publications.md"
  done
  skill_md fe-extra "Fe Extra" > "$GM/product/home-example-team/fe-extra/SKILL.md"
  skill_md xo-second "Xo Second" > "$GM/product/second-example-team/xo-second/SKILL.md"
  team_json multi-example-team "Multi Example Team" "$DI" "" > "$MULTI/team.json"
  jedit "$MULTI/team.json" 'd["guests"] = [{"slug": s, "home": h + "-example-team"} for s, h in (("cy-sample", "home"), ("xo-second", "second"), ("fe-extra", "home"))]'
  python3 scripts/new_team.py "$MULTI/team.json" --root "$GM/product" > /dev/null 2>&1; r4=$?
  python3 scripts/new_team.py "$MULTI/team.json" --root "$GM/product" --guest-text > "$TMP/guest-text-multi.json" 2> /dev/null; r5=$?
  msg=$(python3 - "$TMP" "$HOST_TEAM" "$HOME_TEAM/cy-sample" "$GROW" "$r1 $r2 $r3 $r4 $r5" "$MULTI" 2>&1 <<'PY'
import json, re, sys
from pathlib import Path
tmp, host, cy, grow, codes, multi = (Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4], sys.argv[5].split(),
                                     Path(sys.argv[6]))
KEYS = ["guests", "SEATED_LIST", "GUEST_CLAUSE", "GUEST_INSTALL", "GUEST_INSTALL_PS", "GUEST_RESOLUTION", "GUEST_CARDS",
        "GUEST_SEATS_TODO", "GUEST_DEEP_READING", "README_GUEST_ROWS", "ROUNDTABLE_GUEST_ROWS"]
TAIL = ": if this checkout holds git-ignored full texts, copy only git-tracked files, see product/README.md"
COMMENT = "guest from the Home Example Team" + TAIL
RT = "host-example-roundtable/SKILL.md"
show = lambda v, n=120: json.dumps(v, ensure_ascii=False)[:n]
probs = []
def load(name, what, code):
    try:
        d = json.loads((tmp / name).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        d = None
    if code != "0" or not isinstance(d, dict):
        probs.append(f"{what}: exit {code}, " + ("a JSON object" if isinstance(d, dict) else "no JSON object") + " on stdout")
        return {}
    miss, extra = [k for k in KEYS if k not in d], [k for k in d if k not in KEYS]
    if miss or extra:
        probs.append(f"{what}: keys" + (" missing " + ", ".join(miss) if miss else "") + (" unexpected " + ", ".join(extra) if extra else ""))
    return d
d = load("guest-text.json", "--root <fixture>/product", codes[0])
r = load("guest-text-repo.json", "default --root", codes[1])
h = load("guest-text-home.json", "home team (no guests)", codes[2])
m = load("guest-text-multi.json", "three guests from two homes", codes[4])
def scaffolded(f):
    try:
        return (host / f).read_text(encoding="utf-8")
    except OSError:
        probs.append(f"no scaffolded {f} to compare with")
        return ""
text = {f: scaffolded(f) for f in ("README.md", RT, "DEEP-READING.md")}
want = {"GUEST_INSTALL": "\n# " + COMMENT + "\ncp -r product/home-example-team/cy-sample ~/.claude/skills/",
        "GUEST_INSTALL_PS": "\n# " + COMMENT + '\nCopy-Item -Recurse product\\home-example-team\\cy-sample "$HOME\\.claude\\skills\\"',
        "SEATED_LIST": "Di Example, Cy Sample", "README_GUEST_ROWS": [grow]}
def differ(got, exp):  # both values from 30 characters before their first difference
    a, b = show(got, None), show(exp, None)
    i = next((n for n, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
    return f"…{a[max(0, i - 30):i + 60]}…, expected …{b[max(0, i - 30):i + 60]}…"
for k, v in want.items():
    if k in d and d[k] != v:
        probs.append(f"{k} = {differ(d[k], v)}")
# every string is in the file the scaffold wrote it to (GUEST_CLAUSE right after the member list, in both files)
for k, f, before in (("GUEST_CLAUSE", "README.md", "Di Example"), ("GUEST_CLAUSE", RT, "Di Example"), ("SEATED_LIST", RT, ""),
                     ("GUEST_RESOLUTION", RT, ""), ("GUEST_CARDS", RT, ""), ("GUEST_SEATS_TODO", RT, ""),
                     ("GUEST_DEEP_READING", "DEEP-READING.md", "")):
    v = d.get(k)
    if k in d and (not isinstance(v, str) or not v.strip() or before + v not in text[f]):
        probs.append(f"{k} {show(v, 60)} is not in the scaffolded {f}" + (f" after {before!r}" if before else ""))
# the install lines: the guests' lines (a comment line per home team, then one copy line per guest) directly under the
# copy line of the team in that shell (appended at its end)
def under(readme, team, k, own, what=""):
    start = {"GUEST_INSTALL": f"for d in product/{team}/", "GUEST_INSTALL_PS": f"Get-ChildItem product\\{team} "}[k]
    lines = readme.splitlines()
    i = next((n for n, l in enumerate(lines) if l.startswith(start)), None)
    below = lines[i + 1:i + 1 + len(own)] if i is not None else None
    if below != own:
        probs.append(f"{what}README.md: the lines under {start!r}… are {show(below, 120)}, not the {k} lines")
for k in ("GUEST_INSTALL", "GUEST_INSTALL_PS"):
    if isinstance(d.get(k), str):
        under(text["README.md"], "host-example-team", k, d[k][1:].split("\n"))
# three guests from two homes: one comment line per home team, in the order of first appearance in team.json ("guests"
# for two; the title without the characters a shell treats specially), each over the copy lines of that home's guests;
# --guest-text gives exactly these lines, and the scaffold wrote them under the team's copy line in each shell
MULTI = {"GUEST_INSTALL": ["# guests from the Home Example Team" + TAIL,
                           "cp -r product/home-example-team/cy-sample ~/.claude/skills/",
                           "cp -r product/home-example-team/fe-extra ~/.claude/skills/",
                           "# guest from the Second Example Team BC" + TAIL,
                           "cp -r product/second-example-team/xo-second ~/.claude/skills/"],
         "GUEST_INSTALL_PS": ["# guests from the Home Example Team" + TAIL,
                              'Copy-Item -Recurse product\\home-example-team\\cy-sample "$HOME\\.claude\\skills\\"',
                              'Copy-Item -Recurse product\\home-example-team\\fe-extra "$HOME\\.claude\\skills\\"',
                              "# guest from the Second Example Team BC" + TAIL,
                              'Copy-Item -Recurse product\\second-example-team\\xo-second "$HOME\\.claude\\skills\\"']}
TWO = "three guests from two homes: "
try:
    multi_readme = (multi / "README.md").read_text(encoding="utf-8") if codes[3] == "0" else None
except OSError:
    multi_readme = None
if multi_readme is None:
    probs.append(f"{TWO}the scaffold exit {codes[3]}, no README.md to compare with")
for k, own in MULTI.items():
    exp = "".join("\n" + l for l in own)
    if k in m and m[k] != exp:
        probs.append(f"{TWO}{k} = {differ(m[k], exp)}")
    if multi_readme is not None:
        under(multi_readme, "multi-example-team", k, own, TWO)
# safe to paste into zsh with its default options (no INTERACTIVE_COMMENTS: # is no comment there): every comment is a
# line of its own without shell characters, and no copy line carries a comment
for what, x in (("", d), (TWO, m)):
    v = x.get("GUEST_INSTALL")
    for l in v[1:].split("\n") if isinstance(v, str) else []:
        if (re.fullmatch(r"# [\w .,:/+-]+", l) is None) if l.startswith("#") else ("#" in l):
            probs.append(f"{what}GUEST_INSTALL line {l!r} is not safe to paste into zsh (a comment with shell characters, or a comment after a command)")
for k, f, start in (("README_GUEST_ROWS", "README.md", grow),
                    ("ROUNDTABLE_GUEST_ROWS", RT, "| `cy-sample` | Cy Sample (guest from Home Example Team) | ")):
    rows = d.get(k)
    if k in d and not (isinstance(rows, list) and len(rows) == 1 and isinstance(rows[0], str) and rows[0].startswith(start)
                       and rows[0] in text[f].splitlines()):
        probs.append(f"{k} = {show(rows)}: expected one row starting {start[:50]!r}…, a line of the scaffolded {f}")
fields = {"slug": "cy-sample", "home": "home-example-team", "name": "Cy Sample", "home_title": "Home Example Team"}
for what, x, dir_ok, dir_want in (
        ("--root <fixture>/product", d, lambda p: "\\" not in p and Path(p).resolve() == cy.resolve(), f"the displayed path of {cy.as_posix()}"),
        ("default --root", r, lambda p: p == "product/home-example-team/cy-sample", "product/home-example-team/cy-sample")):
    gs = x.get("guests")
    g = gs[0] if isinstance(gs, list) and len(gs) == 1 and isinstance(gs[0], dict) else None
    if x and (g is None or sorted(g) != sorted([*fields, "dir"]) or any(g[k] != v for k, v in fields.items())):
        probs.append(f"{what}: guests = {show(gs, 200)}")
    elif x and not (isinstance(g["dir"], str) and dir_ok(g["dir"])):
        probs.append(f"{what}: guests[0].dir = {show(g['dir'])}, expected {dir_want}")
if d and r and {k: v for k, v in d.items() if k != "guests"} != {k: v for k, v in r.items() if k != "guests"}:
    probs.append("the strings differ between --root <fixture>/product and the default --root")
empty = {k: [] if k in ("guests", "README_GUEST_ROWS", "ROUNDTABLE_GUEST_ROWS") else "" for k in KEYS if k != "SEATED_LIST"}
off = [k for k, v in empty.items() if k in h and h[k] != v] + (["SEATED_LIST"] if h.get("SEATED_LIST", "Cy Sample") != "Cy Sample" else [])
if off:
    probs.append("home team (no guests): not empty: " + ", ".join(off))
print("\n".join(probs) or "the host's 11 keys, each string as the scaffold wrote it (the comment and Copy-Item lines under "
      "the PowerShell copy line; the bash lines safe to paste into zsh), dir product/home-example-team/cy-sample with the "
      "default --root and the displayed path with another; three guests from two homes: per home team one comment line "
      "(\"guests\" for two, the title without shell characters) over its guests' copy lines, in --guest-text and under "
      "both shells' copy lines; the home team (no guests): empty strings and lists, exit 0")
sys.exit(1 if probs else 0)
PY
); rc=$?
  report "new_team.py --guest-text" $rc "$msg"
  # the args of a real launch (a workflow NAME resolves against --repo, which has no scripts/ here: pass the path)
  for w in layer integrate base-skills; do
    if msg=$(node scripts/workflows/make_args.mjs "scripts/workflows/team-$w.js" --team product/host-example-team --repo "$FX" \
             --date 2026-01-01 --scratch "$TMP/scratch" 2>&1 > "$TMP/guest-calls-$w.json"); then
      msg=$(guest_args "$TMP/guest-calls-$w.json" "$w"); rc=$?
    else rc=1; fi
    if [ $rc -eq 0 ]; then ok "make_args.mjs team-$w on the host: $msg"; else bad "make_args.mjs team-$w on the host: $(tail -1 <<<"$msg")"; fi
  done
  for w in layer integrate; do
    out=$(node scripts/workflows/dry_run.mjs "scripts/workflows/team-$w.js" --team product/host-example-team --repo "$FX" --scratch "$TMP/scratch" \
          --quiet --strict --forbid "$GFORBID" --out "$TMP/guest-prompts-$w" 2>&1)
    rc=$?
    n=$(grep -l 'home-example-team/cy-sample' "$TMP/guest-prompts-$w"/*.md 2>/dev/null | grep -c .)
    if [ $rc -eq 0 ] && [ "$n" -gt 0 ]; then ok "dry_run.mjs --team --strict team-$w on the host: $(grep -m1 '^agents' <<<"$out" | sed 's/  */ /g'); guest folder in $n prompt(s)"
    else bad "dry_run.mjs --team --strict team-$w on the host (exit $rc; guest folder in $n prompt(s))"; grep -E '^  - |✗|dry_run:' <<<"$out" | head -5; fi
  done
  # the guest branches the default fakes do not reach (team-integrate stops at its status agent, team-layer runs only the
  # deep-tier rerun), driven by answers files, each under --strict and --check-answers (an answer that sets a field its
  # agent's schema does not declare fails it: a real agent never returns that field): every "<where>|<text>" pair must be
  # found, <where> being a prompt label (the file NNN-<label>.md of --out), "log" (a log line) or "return" (the return
  # value); a pair "!<label>|<text>" requires that prompt to exist WITHOUT the text (a guest sentence that must stay
  # conditional), and "!log|<text>" / "!return|<text>" that no log line / not the return value has it.
  # The host is GTEAM (product/host-example-team; teams/host-example-team for the copy outside product/)
  GN=0
  GTEAM=product/host-example-team
  gdry() {  # label, repo, workflow, extra dry_run options, answers JSON, "<where>|<text>" ...
    local label=$1 repo=$2 w=$3 opts=$4 ans=$5 d out rc probs="" want where text
    shift 5
    GN=$((GN + 1)); d="$TMP/guest-branch-$GN"
    printf '%s\n' "$ans" > "$d.answers.json"
    # shellcheck disable=SC2086  # $opts holds several options
    out=$(node scripts/workflows/dry_run.mjs "scripts/workflows/team-$w.js" --team "$GTEAM" --repo "$repo" --scratch "$TMP/scratch" \
          $opts --answers "$d.answers.json" --check-answers --quiet --strict --forbid "$GFORBID" --out "$d" 2>&1); rc=$?
    [ $rc -eq 0 ] || probs="; exit $rc"
    for want in "$@"; do
      where=${want%%|*}; text=${want#*|}
      case $where in
        log) grep -qF -- "log: $text" <<<"$out" || probs="$probs; no log line \"$text…\"" ;;
        return) grep -qF -- "$text" "$d/return.json" 2> /dev/null || probs="$probs; the return value lacks \"$text\"" ;;
        \!log) ! grep -qF -- "log: $text" <<<"$out" || probs="$probs; a log line has \"$text\" (it must not here)" ;;
        \!return) [ -f "$d/return.json" ] && ! grep -qF -- "$text" "$d/return.json" || probs="$probs; the return value has \"$text\" (or is missing; it must not have it here)" ;;
        \!*) if ! ls "$d"/[0-9][0-9][0-9]-"${where#!}".md > /dev/null 2>&1; then probs="$probs; no ${where#!} prompt"
            elif cat "$d"/[0-9][0-9][0-9]-"${where#!}".md | grep -qF -- "$text"; then probs="$probs; the ${where#!} prompt has \"$text\" (it must not here)"; fi ;;
        *) cat "$d"/[0-9][0-9][0-9]-"$where".md 2> /dev/null | grep -qF -- "$text" || probs="$probs; the $where prompt lacks \"$text\"" ;;
      esac
    done
    if [ -z "$probs" ]; then ok "$label: $(grep -m1 '^agents' <<<"$out" | sed 's/  */ /g')"
    else bad "$label:${probs#;}"; grep -E '^  - |✗|threw|dry_run:' <<<"$out" | head -3; fi
  }
  ST='"coverage_md": "| c |", "coverage_short_md": "| s |", "problems": []'
  CYROW='"slug": "cy-sample", "stage": "T1 base skill", "has_08": false, "home": "home-example-team"'
  gdry "team-integrate with a ready member and a guest without cards: docs, roundtable, both reviewers and the fixer" "$FX" integrate "" \
    "{\"^status:team\$\": {$ST, \"members\": [{\"slug\": \"di-example\", \"stage\": \"T3.6 synthesized\", \"has_08\": true}, {$CYROW, \"has_cards\": false}]}}" \
    'integrate_docs|--guest-text' 'integrate_docs|GUEST_DEEP_READING string' \
    "integrate_roundtable|never drop or reword a fault line only because a guest's side has no cards" \
    'verify_numbers-links|status --porcelain -- product/home-example-team/cy-sample' 'verify_evidence|status --porcelain -- product/home-example-team/cy-sample' \
    "fix_integration|decline a finding about a guest's own files as home-team work" 'return|Guests not ready: cy-sample' \
    '!return|apart from the rows that stay red on the guests without a SKILL.md yet'
  gdry "team-integrate, no member ready, a guest with paper cards: rerun team-layer.js (T2), not this step" "$FX" integrate "" \
    "{\"^status:team\$\": {$ST, \"members\": [{\"slug\": \"di-example\", \"stage\": \"T1 base skill\", \"has_08\": false}, {$CYROW, \"has_cards\": true}]}}" \
    'log|guests with paper cards in their home teams (cy-sample)' "return|rerun team-layer.js (T2) here, which cites a carded guest's side by card at either tier" \
    "status_team|has_cards = its folder's references/research/cards/ holds paper cards" "status_team|has_skill = its folder's SKILL.md exists"
  gdry "team-layer base tier with a carded guest: members-only base-tier wording, check_citations.py, the DEEP-READING guest pointer; the guest's folder read-only for its digest, both verifiers and the fixer" "$FX" layer \
    "--set deep_tier=false" '{"^card:": {"deep_tier_done": false}, "^guest:": {"deep_tier_done": true}, "^verify:evidence$": {"findings": [{"severity": "minor", "file": "f", "problem": "p", "fix": "x"}]}}' \
    "roundtable|Base tier: this team's members get no paper cards" "roundtable|No deep reading was done for this team's members (base tier)" \
    'roundtable|--roundtable → 0 problems' "readme|end the base-tier note's paragraph with the GUEST_DEEP_READING string" \
    "readme|covers this team's members only" 'verify_evidence|--roundtable (team_check.py runs it at either tier' 'fix_team-layer|--roundtable → 0 problems' \
    "return|a carded guest's side is cited by card at the base tier too" \
    "roundtable|from that seat's own references/research/cards/*.digest.json (indexed in its 07-paper-cards.md once its home team's T3.6 has run)" \
    'readme|each guest with a SKILL.md is a full seat in the roundtable and the README (a guest without one is not seated' \
    'guest_cy-sample|READ-ONLY: edit, create, move or delete nothing in that folder or anywhere else' 'guest_cy-sample|Files you may edit: none.' \
    'verify_structure|status --porcelain -- product/home-example-team/cy-sample' 'verify_evidence|status --porcelain -- product/home-example-team/cy-sample' \
    "fix_team-layer|Never edit anything in a guest's folder" \
    'return|Base tier: the team is complete after the commit' '!return|apart from what stays red on the guests without a SKILL.md yet'
  gdry "team-layer, own member without a skill: roundtable and README not written (the guest alone is not enough)" "$FX" layer "" \
    '{"^card:": {"skill_exists": false}}' 'log|no member of this team has a skill yet: roundtable and README not written' 'return|Nothing was written'
  gdry "team-layer, a guest without SKILL.md: left out, a rerun line in next" "$FX" layer "" '{"^guest:": {"skill_exists": false}}' \
    'log|no SKILL.md yet for guest(s): cy-sample' 'return|Guests without a SKILL.md yet, not seated by this run: cy-sample (T1 in product/home-example-team)'
  # a second guest, fe-extra, without a SKILL.md or whose digest agent returns nothing, beside a seated guest: the roundtable
  # and README are written, and the README author, both verifiers and the fixer (brought in by a verifier finding) are told
  # that its missing seats are not findings; a guest whose digest agent died is never called one without a skill
  GF="$TMP/guest-fixture-two-guests"
  cp -r "$FX" "$GF" && mkdir -p "$GF/product/home-example-team/fe-extra/references/research"
  jedit "$GF/product/home-example-team/team.json" 'd["members"].append({"slug": "fe-extra", "name": "Fe Extra", "hint": "FICTIONAL placeholder of the kit self-test"})'
  jedit "$GF/product/host-example-team/team.json" 'd["guests"].append({"slug": "fe-extra", "home": "home-example-team"})'
  skill_md fe-extra "Fe Extra" > "$GF/product/home-example-team/fe-extra/SKILL.md"
  note_md > "$GF/product/home-example-team/fe-extra/references/research/01-publications.md"
  VF='"^verify:structure$": {"findings": [{"severity": "major", "file": "README.md", "problem": "fixture finding", "fix": "x"}]}'
  # the fixer's links gate beside such a guest: check_links.py counts its README link as broken once its home folder has
  # notes, so only the other broken links the fixer reports (broken_other) make "next" say it reported a failing gate
  FXL='"^fix:team-layer$": {"check_links": "❌ 7 files checked, 1 broken links · 0 pending"'
  gdry "team-layer, a guest without SKILL.md beside a seated guest: not seated, kept as scaffolded, not a finding for the verifiers and the fixer, its README link no failing gate of the fixer" "$GF" layer "" \
    "{\"^guest:fe-extra\$\": {\"skill_exists\": false}, $VF, $FXL, \"broken_other\": 0}}" \
    "readme|Guests without a SKILL.md yet (their home team's T1 has not reached this branch): fe-extra. They are not seated in the roundtable this run" \
    'verify_structure|They are not seated this run: their missing roundtable Team-table row, seating rows, fault lines and Guest seat note are not findings' \
    'verify_evidence|They are not seated this run: their missing fault lines are not findings' \
    'fix_team-layer|They are not seated this run: decline every finding that asks to seat them' \
    'return|Guests without a SKILL.md yet, not seated by this run: fe-extra (T1 in product/home-example-team)' '!readme|This team is not under product/' \
    'verify_structure|The README link of a guest without a SKILL.md yet is reported as item 3b says' \
    "verify_structure|that broken link is expected until their home team's branch is merged here after its T1, so report it as a minor finding" \
    "fix_team-layer|and one about their README row's broken link" \
    'fix_team-layer|(0 broken, apart from the README links of the guests without a SKILL.md yet above: report its result line in check_links as printed and, in broken_other,' \
    "return|the gates stay red on them: team_check.py's guests row (SKILL.md missing), its roundtable row (not in the Team table, seated in no row, in no fault line" \
    'return|Gates (apart from what stays red on the guests without a SKILL.md yet: below): ' '!return|The fixer reported a failing gate'
  gdry "team-layer at the base tier, a guest without SKILL.md and a fixer reporting another broken link: a failing gate, the team complete only once the guest is seated" "$GF" layer "--set deep_tier=false" \
    "{\"^card:\": {\"deep_tier_done\": false}, \"^guest:fe-extra\$\": {\"skill_exists\": false}, $VF, $FXL, \"broken_other\": 1}}" \
    'return|The fixer reported a failing gate (see fix)' \
    'return|Base tier: the team is complete once the rerun below has seated the guests without a SKILL.md yet and is committed' \
    'return|or all T2 gates at once: python3 scripts/team_check.py product/host-example-team --tier base.' \
    '!return|Base tier: the team is complete after the commit'
  gdry "team-layer, a guest whose digest agent returned nothing: left out of this run, not a finding for the verifiers and the fixer, a rerun line" "$GF" layer "" \
    "{\"^guest:fe-extra\$\": null, $VF}" \
    'log|guest digest agent returned nothing for: fe-extra' 'roundtable|Guests whose digest agent returned nothing in this run: fe-extra' \
    'readme|Guests whose digest agent returned nothing in this run: fe-extra. Their skills were not read this time' \
    'verify_structure|Guests whose digest agent returned nothing in this run: fe-extra. They were not checked this run' \
    'verify_evidence|They were not checked this run: their missing fault lines are not findings' \
    'fix_team-layer|They were not checked this run: decline findings about their missing rows' \
    'return|Rerun team-layer.js: the digest agent returned nothing for guest(s) fe-extra' \
    'verify_structure|The TODO items the files already have for a guest whose digest agent returned nothing are not findings this run (item 3b)' \
    'verify_structure|nor are the TODO items the files already have for them (item 2)' \
    'readme|keep the row the README has for them (their README_GUEST_ROWS row only when it has none)'
  # T3.8 with a guest without SKILL.md (fe-extra; has_skill false) beside a seated guest: T2 did not seat it, so neither
  # does this step: every agent is told, it is not listed as a guest not ready, and "next" asks for its home team's T1,
  # then a team-layer.js (T2) rerun here, then this step; also when no member is ready (the early return), where it is
  # not among the carded guests T2 is to cite
  NSROW='"slug": "fe-extra", "stage": "T0 scaffold", "has_08": false, "home": "home-example-team", "has_skill": false'
  gdry "team-integrate with a ready member and a guest without SKILL.md beside a seated guest: not seated here, its T1 and a team-layer.js (T2) rerun first" "$GF" integrate "" \
    "{\"^status:team\$\": {$ST, \"members\": [{\"slug\": \"di-example\", \"stage\": \"T3.6 synthesized\", \"has_08\": true}, {$CYROW, \"has_cards\": false}, {$NSROW, \"has_cards\": false}]}}" \
    'log|guests without a SKILL.md yet, not seated here' 'return|Guests not ready: cy-sample' '!return|fe-extra (T0 scaffold; home team' \
    'return|Guests without a SKILL.md yet, not seated here: fe-extra (T1 in product/home-example-team). Once their home team' \
    'return|rerun team-layer.js (T2) here to seat them' \
    "return|team_check.py's guests row (SKILL.md missing), its roundtable row (not in the Team table, seated in no row, in no fault line" \
    'return|→ exit 0, apart from the rows that stay red on the guests without a SKILL.md yet (below).' \
    "integrate_roundtable|Guests without a SKILL.md yet (their home team's T1 has not reached this branch): fe-extra (T0 scaffold; home-example-team). They are not seated" \
    'integrate_docs|but the "lens: [TODO]" of the README row of a guest without a SKILL.md yet' \
    'verify_numbers-links|The README link to a guest without a SKILL.md yet (named above) is pending, or broken once its folder has research notes' \
    'fix_integration|Decline every finding that asks to seat a guest without a SKILL.md yet' 'fix_integration|passes too: list it'
  gdry "team-integrate, no member ready, a carded guest and a guest without SKILL.md: T2 cites the carded one, the other needs its T1 first" "$GF" integrate "" \
    "{\"^status:team\$\": {$ST, \"members\": [{\"slug\": \"di-example\", \"stage\": \"T1 base skill\", \"has_08\": false}, {$CYROW, \"has_cards\": true}, {$NSROW, \"has_cards\": true}]}}" \
    'return|cannot bring in the paper cards of cy-sample yet' 'return|Guests without a SKILL.md yet, not seated here: fe-extra (T1 in product/home-example-team)'
  # a copy whose teams sit under teams/, not product/: the guest-text command takes --root <repo>/teams (without it the
  # guests resolve under product/ and it exits 1), and it still writes product/ in the guests' install lines, so the README
  # author, verify:structure and the fixer give them the path fix of the team's own copy line; team-integrate runs the
  # same command for the DEEP-READING guest pointer
  FXT="$TMP/guest-fixture-teams"
  mkdir -p "$FXT" && cp -r "$FX/product" "$FXT/teams"
  GTEAM=teams/host-example-team
  gdry "team-layer on a team outside product/ (teams/): --guest-text with --root <repo>/teams, the guests' install lines with the path fix of the team's own copy line" "$FXT" layer "" "{$VF}" \
    'readme|This team is not under product/, and --guest-text writes those lines with product/' \
    'readme|becomes the guest'"'"'s folder (teams/home-example-team/cy-sample and teams\home-example-team\cy-sample)' \
    'verify_structure|compared after the path fix of a team outside product/' 'fix_team-layer|an install line with the path fix of a team outside product/' \
    'readme|guest-fixture-teams/teams/host-example-team/team.json --guest-text --root ' 'readme|guest-fixture-teams/teams (read-only: it prints one JSON object' \
    'verify_structure|guest-fixture-teams/teams (read-only: it prints one JSON object' 'fix_team-layer|guest-fixture-teams/teams (an install line with the path fix'
  gdry "team-integrate on a team outside product/ (teams/): --guest-text with --root <repo>/teams, the guest's folder under teams/" "$FXT" integrate "" \
    "{\"^status:team\$\": {$ST, \"members\": [{\"slug\": \"di-example\", \"stage\": \"T3.6 synthesized\", \"has_08\": true}, {$CYROW, \"has_cards\": false}]}}" \
    'integrate_docs|guest-fixture-teams/teams/host-example-team/team.json --guest-text --root ' \
    'integrate_docs|guest-fixture-teams/teams (read-only: it prints one JSON object' \
    'verify_numbers-links|status --porcelain -- teams/home-example-team/cy-sample'
  GTEAM=product/host-example-team
  # the gate: the guests row passes (the fresh scaffold fails other rows, as every team does before T1 and T2)
  python3 scripts/team_check.py "$HOST_TEAM" --json --skip-quality > "$TMP/guest-check.json" 2> "$TMP/guest-check.err"
  r=$(check_row "$TMP/guest-check.json" guests)
  if [ "${r%% *}" = pass ]; then ok "team_check.py --json --skip-quality on the host: guests pass (${r#pass })"
  else bad "team_check.py --json --skip-quality on the host: guests row: $r"; tail -3 "$TMP/guest-check.err"; fi
  # run inside the host folder as "." (the guests resolve against the team folder's resolved parent): the same guests row
  (cd "$HOST_TEAM" && python3 "$REPO/scripts/team_check.py" . --json --skip-quality > "$TMP/guest-check-dot.json" 2> /dev/null)
  r=$(check_row "$TMP/guest-check-dot.json" guests)
  s=$(cd "$HOST_TEAM" && python3 "$REPO/scripts/team_status.py" . --json --no-quality 2> /dev/null \
      | python3 -c 'import json,sys;print("; ".join(g["slug"]+" "+g["stage"] for g in json.load(sys.stdin).get("guests",[])))' 2> /dev/null)
  if [ "${r%% *}" = pass ] && [ "$r" = "$(check_row "$TMP/guest-check.json" guests)" ] && [ "$s" = "cy-sample T1 base skill" ]; then
    ok "inside the host folder: team_check.py . (guests ${r#pass }) and team_status.py . --json ($s) resolve the guest"
  else bad "inside the host folder: team_check.py . guests row: ${r:0:100}; team_status.py . --json guests: ${s:-none}"; fi
  # the home team's gate notes (—, no verdict) the teams that seat its members as guests, read from its sibling folders
  python3 scripts/team_check.py "$HOME_TEAM" --json --skip-quality > "$TMP/guest-check-home.json" 2> /dev/null
  r=$(check_row "$TMP/guest-check-home.json" hosts); r0=$(check_row "$TMP/guest-check.json" hosts)
  hosts='seated as guest elsewhere: host-example-team (cy-sample)'
  if [ "${r#"skip $hosts: "}" != "$r" ] && [ "$r0" = none ]; then ok "team_check.py on the home team: hosts row — $hosts: …; none on the host"
  else bad "hosts row: home team: ${r:0:120}; host: ${r0:0:80} (expected \"skip $hosts: …\" and none)"; fi
  # team_status.py on the host: ## Guests is the last section, after the coverage table (which counts the members only)
  python3 scripts/team_status.py "$HOST_TEAM" --no-quality > "$TMP/guest-status.md" 2> /dev/null; r1=$?
  python3 scripts/team_status.py "$HOST_TEAM" --json --no-quality > "$TMP/guest-status.json" 2> /dev/null; r2=$?
  python3 scripts/team_status.py "$HOST_TEAM" --coverage > "$TMP/guest-coverage.md" 2> /dev/null; r3=$?
  msg=$(python3 - "$TMP" "$r1 $r2 $r3" 2>&1 <<'PY'
import json, sys
from pathlib import Path
tmp, codes = Path(sys.argv[1]), sys.argv[2].split()
probs = [f"{w}: exit {c}" for w, c in zip(("team_status.py", "--json", "--coverage"), codes) if c != "0"]
read = lambda name: (tmp / name).read_text(encoding="utf-8")
lines = read("guest-status.md").splitlines()
heads = [i for i, l in enumerate(lines) if l.startswith("## ")]
cov = next((i for i, l in enumerate(lines) if l.startswith("| Researcher |")), None)
g = next((i for i, l in enumerate(lines) if l == "## Guests"), None)
row = next((l for l in lines[g:] if l.startswith("- cy-sample ")), "") if g is not None else ""
if g is None or cov is None or cov > g or heads[-1] != g:
    probs.append(f"## Guests at line {g + 1 if g is not None else '—'}, the coverage table at line "
                 f"{cov + 1 if cov is not None else '—'}: expected Guests as the last section, after the coverage table")
elif not (row.startswith("- cy-sample · home home-example-team · T1 base skill · read in ")
          and row.endswith("/home-example-team/DEEP-READING.md")):
    probs.append(f"the Guests row is {row[:150]!r}")
try:
    js = json.loads(read("guest-status.json")).get("guests")
except (OSError, ValueError, AttributeError):
    js = "(no JSON)"
if js != [{"slug": "cy-sample", "home": "home-example-team", "stage": "T1 base skill"}]:
    probs.append(f"--json guests = {json.dumps(js, ensure_ascii=False)[:160]}")
cov_text = read("guest-coverage.md")
if "Sample" in cov_text or "Di Example" not in cov_text:
    probs.append("--coverage does not list the members only (Di Example, not the guest)")
print("\n".join(probs) or "## Guests last, after the coverage table (cy-sample · home home-example-team · T1 base skill · "
      "read in …/home-example-team/DEEP-READING.md); --json guests; --coverage lists the members only")
sys.exit(1 if probs else 0)
PY
); rc=$?
  report "team_status.py on the host" $rc "$msg"
  # a negative copy: the guest's slug is not a member of its home team
  NEG="$TMP/guest-fixture-negative"
  cp -r "$FX" "$NEG" && team_json host-example-team "Host Example Team" "$DI" ed-nobody > "$NEG/product/host-example-team/team.json"
  o1=$(python3 scripts/new_team.py "$NEG/product/host-example-team/team.json" --root "$NEG/product" --dry-run 2>&1); r1=$?
  o3=$(python3 scripts/new_team.py "$NEG/product/host-example-team/team.json" --root "$NEG/product" --guest-text 2>&1 > "$TMP/guest-text-negative.json"); r3=$?
  o2=$(node scripts/workflows/make_args.mjs scripts/workflows/team-layer.js --team product/host-example-team --repo "$NEG" \
       --date 2026-01-01 --scratch "$TMP/scratch" 2>&1 > /dev/null); r2=$?
  python3 scripts/team_check.py "$NEG/product/host-example-team" --json --skip-quality > "$TMP/guest-check-negative.json" 2> /dev/null
  r=$(check_row "$TMP/guest-check-negative.json" guests)
  probs=""
  m=$(lacks "$o1"); { [ $r1 -ne 0 ] && [ -z "$m" ]; } || probs="$probs; new_team.py exit $r1$m"
  m=$(lacks "$o3")$([ -s "$TMP/guest-text-negative.json" ] && echo ', JSON on stdout')
  { [ $r3 -ne 0 ] && [ -z "$m" ]; } || probs="$probs; new_team.py --guest-text exit $r3$m"
  m=$(lacks "$o2"); { [ $r2 -ne 0 ] && [ -z "$m" ]; } || probs="$probs; make_args.mjs exit $r2$m"
  m=$(lacks "$r"); { [ "${r%% *}" = fail ] && [ -z "$m" ]; } || probs="$probs; team_check.py guests row ${r%% *}$m"
  if [ -z "$probs" ]; then ok "negative copy (not a member at home): new_team.py, its --guest-text (no JSON), make_args.mjs and team_check.py fail with \"$GMSG … $MERGE …\""
  else bad "negative copy (not a member at home):${probs#;}"; fi
  # the stop hint: only when every guest error is one a merge of the home team's branch cures (home team.json missing, not
  # a member there and no member equal up to case, the member's folder missing) does new_team.py add how to scaffold the
  # team's own members without those guests; on a team not scaffolded yet, --add-guest's error adds "scaffold without it"
  # the same way. The negative copy prints both, and the hint names the guest there and in a copy whose only guest error
  # is each of the other two kinds (HJ: the home team.json missing; HF: the member's folder missing at home); a case-only
  # slug typo (Cy-Sample: did you mean …?) neither, its error line giving the local fix (the ten cases below, other errors
  # among them, print no hint either)
  HINT='· only guests that do not resolve stopped this run:'
  WITHOUT='; while a guest in team.json does not resolve, scaffold without it'
  TYPO="$TMP/guest-fixture-case-typo"
  cp -r "$FX" "$TYPO" && team_json host-example-team "Host Example Team" "$DI" Cy-Sample > "$TYPO/product/host-example-team/team.json"
  o4=$(python3 scripts/new_team.py "$TYPO/product/host-example-team/team.json" --root "$TYPO/product" --dry-run 2>&1); r4=$?
  HJ="$TMP/guest-fixture-no-home-json"   # hal-away from gone-example-team, which has no team.json here
  cp -r "$FX" "$HJ" && jedit "$HJ/product/host-example-team/team.json" 'd["guests"] = [{"slug": "hal-away", "home": "gone-example-team"}]'
  o5=$(python3 scripts/new_team.py "$HJ/product/host-example-team/team.json" --root "$HJ/product" --dry-run 2>&1); r5=$?
  HF="$TMP/guest-fixture-no-member-folder"   # bo-fresh, in home-example-team's members without a folder there
  cp -r "$FX" "$HF" && jedit "$HF/product/home-example-team/team.json" 'd["members"].append({"slug": "bo-fresh", "name": "Bo Fresh", "hint": "FICTIONAL placeholder of the kit self-test"})'
  team_json host-example-team "Host Example Team" "$DI" bo-fresh > "$HF/product/host-example-team/team.json"
  o6=$(python3 scripts/new_team.py "$HF/product/host-example-team/team.json" --root "$HF/product" --dry-run 2>&1); r6=$?
  hint_for() {  # scaffold --dry-run output, its exit code, guest slug, its error (a fragment) -> the texts it lacks ("" = none)
    local errs
    errs=$(grep '^❌ guest ' <<<"$1")
    if [ "$2" -eq 0 ] || [ "$(grep -c . <<<"$errs")" != 1 ] || ! grep -qF -- "❌ guest $3: " <<<"$errs" || ! grep -qF -- "$4" <<<"$errs"; then
      printf ': exit %s, not the one guest error "guest %s: …%s…"' "$2" "$3" "$4"
    elif ! grep -F -- "$HINT" <<<"$1" | grep -qF -- "$3"; then
      printf ' prints no "%s …" naming %s' "$HINT" "$3"
    fi
  }
  for c in NEG:ed-nobody TYPO:Cy-Sample; do
    f=$([ "${c%%:*}" = NEG ] && echo "$NEG" || echo "$TYPO")
    mkdir -p "$f/product/fresh-example-team" && team_json fresh-example-team "Fresh Example Team" "$DI" "${c#*:}" > "$f/product/fresh-example-team/team.json"
    python3 scripts/new_team.py "$f/product/fresh-example-team/team.json" --root "$f/product" --add-guest "${c#*:}" > "$TMP/stop-hint-add.${c%%:*}" 2>&1
    echo $? >> "$TMP/stop-hint-add.${c%%:*}"
  done
  probs=""
  m=$(hint_for "$o1" $r1 ed-nobody 'not a member of home-example-team'); [ -z "$m" ] || probs="$probs; the negative copy's scaffold (not a member at home)$m"
  m=$(hint_for "$o5" $r5 hal-away "gone-example-team/team.json not found (is the home team's branch merged here?)")
  [ -z "$m" ] || probs="$probs; the scaffold of a copy whose only guest error is a missing home team.json$m"
  m=$(hint_for "$o6" $r6 bo-fresh 'home-example-team/bo-fresh/ missing; scaffold it in the home team first')
  [ -z "$m" ] || probs="$probs; the scaffold of a copy whose only guest error is a guest folder missing at home$m"
  grep -qF -- "$WITHOUT" "$TMP/stop-hint-add.NEG" || probs="$probs; --add-guest ed-nobody on a team not scaffolded yet prints no \"$WITHOUT\""
  [ "$(tail -1 "$TMP/stop-hint-add.NEG")" != 0 ] || probs="$probs; --add-guest ed-nobody on a team not scaffolded yet exit 0"
  { [ $r4 -ne 0 ] && grep -qF 'did you mean cy-sample? (slugs are case-sensitive)' <<<"$o4"; } || probs="$probs; a case-only typo: exit $r4, no \"did you mean cy-sample?\""
  ! grep -qF -- "$HINT" <<<"$o4" || probs="$probs; a case-only typo prints the stop hint"
  { [ "$(tail -1 "$TMP/stop-hint-add.TYPO")" != 0 ] && ! grep -qF -- "$WITHOUT" "$TMP/stop-hint-add.TYPO" \
    && grep -qF 'README.md not found: scaffold the team first' "$TMP/stop-hint-add.TYPO" \
    && grep -qF 'did you mean cy-sample? (slugs are case-sensitive)' "$TMP/stop-hint-add.TYPO"; } \
    || probs="$probs; --add-guest Cy-Sample on a team not scaffolded yet: exit $(tail -1 "$TMP/stop-hint-add.TYPO"), \"$WITHOUT\", or not both \"README.md not found: scaffold the team first\" and \"did you mean cy-sample?\""
  if [ -z "$probs" ]; then ok "the stop hint only when every guest error is one a merge cures: \"$HINT …\", naming the guest, when its only error is that it is not a member at home (the negative copy; and, for --add-guest on a team not scaffolded yet, \"${WITHOUT#; } …\"), that its home team.json is missing, or that its folder is missing at home; a case-only slug typo neither (its scaffold and that --add-guest, after \"README.md not found: scaffold the team first\", ask \"did you mean cy-sample?\")"
  else bad "the stop hint:${probs#;}"; fi
  # the resolver's errors, one line per guest, are the same text from new_team.py (scaffold and --guest-text),
  # make_args.mjs and dry_run.mjs in a real repo layout (a copy of FXR): the host seats ten guests that do not
  # resolve, each for another reason (two are case-only slug typos, one of a member past the 8 names the message lists)
  C5="$TMP/guest-fixture-errors"
  cp -r "$FXR" "$C5" && mkdir -p "$C5/product/many-example-team" "$C5/product/other-example-team" "$C5/product/bad-example-team" "$C5/product/host-example-team/cy-sample"
  jedit "$C5/product/home-example-team/team.json" 'd["members"] += [{"slug": "bo-fresh", "name": "Bo Fresh"}] + [{"slug": f"h{i}-filler", "name": f"H{i} Filler"} for i in range(3, 9)]; d["guests"] = [{"slug": "zed-other", "home": "third-example-team"}]'
  team_json many-example-team "Many Example Team" '{"slug": "m1-filler", "name": "M1 Filler"}' "" > "$C5/product/many-example-team/team.json"
  jedit "$C5/product/many-example-team/team.json" 'd["members"] += [{"slug": f"m{i}-filler", "name": f"M{i} Filler"} for i in range(2, 10)]'
  team_json else-example-team "Else Example Team" '{"slug": "gus-member", "name": "Gus Member"}' "" > "$C5/product/other-example-team/team.json"
  team_json bad-example-team "Bad Example Team" '{"slug": "pat-member"}' "" > "$C5/product/bad-example-team/team.json"   # no "name"
  jedit "$C5/product/host-example-team/team.json" 'd["guests"] = [{"slug": s, "home": h + "-example-team"} for s, h in (("hal-away", "gone"), ("ed-nobody", "home"), ("fay-nobody", "many"), ("zed-other", "home"), ("bo-fresh", "home"), ("cy-sample", "home"), ("gus-member", "other"), ("pat-member", "bad"), ("H5-Filler", "home"), ("M9-Filler", "many"))]'
  (cd "$C5" && python3 scripts/new_team.py product/host-example-team/team.json --dry-run --templates "$REPO/references/team-templates" > "$TMP/errors.new_team" 2>&1); e1=$?
  (cd "$C5" && python3 scripts/new_team.py product/host-example-team/team.json --guest-text > "$TMP/errors.guest-text.json" 2> "$TMP/errors.guest-text"); e2=$?
  node scripts/workflows/make_args.mjs scripts/workflows/team-layer.js --team product/host-example-team --repo "$C5" --date 2026-01-01 \
    --scratch "$TMP/scratch" > /dev/null 2> "$TMP/errors.make_args"; e3=$?
  node scripts/workflows/dry_run.mjs scripts/workflows/team-layer.js --team product/host-example-team --repo "$C5" --scratch "$TMP/scratch" \
    --quiet > /dev/null 2> "$TMP/errors.dry_run"; e4=$?
  msg=$(python3 - "$TMP" "$e1 $e2 $e3 $e4" 2>&1 <<'PY'
import itertools, sys
from pathlib import Path
tmp, codes = Path(sys.argv[1]), sys.argv[2].split()
CASES = [  # slug, case, fragments of the new_team.py line, the end of that line
    ("hal-away", "home team.json missing", ["product/gone-example-team/team.json not found"], ""),
    ("ed-nobody", "not a member, 8 names listed", ["not a member of home-example-team", "lists cy-sample, bo-fresh, h3-filler, "
     "h4-filler, h5-filler, h6-filler, h7-filler, h8-filler)"], ""),
    ("fay-nobody", "not a member, 9 names listed", ["not a member of many-example-team", "lists m1-filler, m2-filler, m3-filler, "
     "m4-filler, m5-filler, m6-filler, m7-filler, m8-filler …)"], ""),
    ("zed-other", "guest of a guest", ["a guest of a guest is not allowed"], ""),
    ("bo-fresh", "guest folder missing", ["product/home-example-team/bo-fresh/ missing",
     "python3 scripts/new_team.py product/home-example-team/team.json --add-member bo-fresh"], "--add-member bo-fresh"),
    ("cy-sample", "shadow copy", ["product/host-example-team/cy-sample exists in this team", "shadow copy"], ""),
    ("gus-member", "home team.json says another team", ["says team 'else-example-team', not 'other-example-team'"], ""),
    ("pat-member", "home team.json fails new_team.py's checks", ["product/bad-example-team/team.json: members[0] (pat-member): 缺 name "
     "(fix it in the home team first)"], ""),
    # a slug that differs from a home member's only in letter case asks for that member instead of the merge advice;
    # every member is searched, also past the 8 names the message lists (m9-filler is the 9th of many-example-team)
    ("H5-Filler", "a case-only slug typo", ["not a member of home-example-team", "h8-filler): did you mean h5-filler? "
     "(slugs are case-sensitive)"], "did you mean h5-filler? (slugs are case-sensitive)"),
    ("M9-Filler", "a case-only slug typo past the 8 names listed", ["not a member of many-example-team", "m8-filler …): did you "
     "mean m9-filler? (slugs are case-sensitive)"], "did you mean m9-filler? (slugs are case-sensitive)")]
TOOLS = [("new_team.py", "errors.new_team", "❌ "), ("new_team.py --guest-text", "errors.guest-text", "❌ "),
         ("make_args.mjs", "errors.make_args", "make_args: "), ("dry_run.mjs", "errors.dry_run", "dry_run: ")]
def lines(name, prefix):
    try:
        text = (tmp / name).read_text(encoding="utf-8")
    except OSError:
        return []
    return [l[len(prefix):] for l in text.splitlines() if l.startswith(prefix + "guest ")]
got = {t: lines(name, prefix) for t, name, prefix in TOOLS}
probs = [f"{t}: exit 0" for (t, _, _), c in zip(TOOLS, codes) if c == "0"]
if (tmp / "errors.guest-text.json").is_file() and (tmp / "errors.guest-text.json").read_text(encoding="utf-8").strip():
    probs.append("new_team.py --guest-text: JSON on stdout although guests do not resolve")
# errors a merge cures (home team.json missing, not a member, folder missing) among ones fixed in place: no stop hint
if any("only guests that do not resolve" in l for l in (tmp / "errors.new_team").read_text(encoding="utf-8").splitlines()):
    probs.append("new_team.py: the stop hint (\"only guests that do not resolve stopped this run\"), although some of these "
                 "errors are fixed in place (a case-only typo, a shadow copy, a guest of a guest, a home team.json to fix)")
ref = got["new_team.py"]
for i, (slug, case, frags, end) in enumerate(CASES):
    line = ref[i] if i < len(ref) else ""
    if not line.startswith(f"guest {slug}: ") or any(f not in line for f in frags) or not line.endswith(end):
        probs.append(f"new_team.py, {case}: line {i + 1} is {line[:100]!r}…, expected 'guest {slug}: …{frags[-1][:50]}…'")
if len(ref) != len(CASES):
    probs.append(f"new_team.py: {len(ref)} guest error line(s), expected {len(CASES)} (one per guest)")
for t, ls in got.items():
    for a, b in itertools.zip_longest(ref, ls, fillvalue=""):
        if a != b:  # show the two lines up to 40 characters past the first difference
            k = next((n for n, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
            probs.append(f"{t}: …{b[:k + 40][-90:]!r} where new_team.py has …{a[:k + 40][-90:]!r}")
print("\n".join(probs) or f"{len(CASES)} cases, one line each (home team.json missing; not a member, 8 and 9 names listed; "
      "guest of a guest; guest folder missing; shadow copy; home team.json says another team; home team.json failing "
      "new_team.py's checks; a case-only slug typo, did you mean …?, also of a member past the 8 names listed); no stop hint")
sys.exit(1 if probs else 0)
PY
); rc=$?
  report "resolver errors in a real repo layout, the same text from new_team.py (scaffold, --guest-text), make_args.mjs and dry_run.mjs" $rc "$msg"
  # a guest folder with research notes but no SKILL.md yet (the home team's T1 half done): the note that check_links.py
  # counts the README link as broken is the same text from new_team.py --guest-text, make_args.mjs and dry_run.mjs
  P8="$TMP/guest-fixture-half-t1"
  cp -r "$FXR" "$P8" && rm -f "$P8/product/home-example-team/cy-sample/SKILL.md"
  n1=$(cd "$P8" && python3 scripts/new_team.py product/host-example-team/team.json --guest-text 2>&1 > /dev/null | tr -d '\r' | grep '^guest cy-sample: ')
  n2=$(node scripts/workflows/make_args.mjs scripts/workflows/team-layer.js --team product/host-example-team --repo "$P8" --date 2026-01-01 \
       --scratch "$TMP/scratch" 2>&1 > /dev/null | sed -n 's/^make_args: note: \(guest cy-sample: \)/\1/p')
  n3=$(node scripts/workflows/dry_run.mjs scripts/workflows/team-layer.js --team product/host-example-team --repo "$P8" --scratch "$TMP/scratch" \
       --quiet 2>&1 | sed -n 's/^note     \(guest cy-sample: \)/\1/p')
  if grep -qF 'so check_links.py counts this team' <<<"$n1" && [ "$n1" = "$n2" ] && [ "$n1" = "$n3" ]; then
    ok "a guest with research notes but no SKILL.md: new_team.py --guest-text, make_args.mjs and dry_run.mjs print the same note (check_links.py counts its README link as broken)"
  else bad "a guest with research notes but no SKILL.md: notes differ: new_team.py ${n1:0:90} | make_args.mjs ${n2:0:90} | dry_run.mjs ${n3:0:90}"; fi
  # the home team.json is read as new_team.py reads it: the constant NaN (Python's json takes it, JSON.parse does not) and
  # a member slug ending in a newline (the $ of new_team.py's SAFE_SLUG_RE matches before it) resolve in both tools; bytes
  # that are not UTF-8 stop both, with one 读不了 JSON line per guest; a value that new_team.py prints with repr() (a float,
  # an int longer than a JS number holds, characters repr() escapes) gives the same line from both
  for v in nan latin1 repr; do
    ENC="$TMP/guest-fixture-json-$v"
    cp -r "$FXR" "$ENC"
    case $v in
      nan) jedit "$ENC/product/home-example-team/team.json" 'd["created"] = float("nan"); d["members"].append({"slug": "zz-newline" + chr(10), "name": "Zz Newline"})' ;;
      latin1) python3 -c 'import sys;p=sys.argv[1];b=open(p,"rb").read();open(p,"wb").write(b.replace(b"placeholder of the kit self-test", "placeholder Müller".encode("cp1252"), 1))' \
        "$ENC/product/home-example-team/team.json" ;;
      repr) jedit "$ENC/product/home-example-team/team.json" 'd["schema"] = [2.0, 10 ** 22 + 1, chr(7) + chr(0x200b) + chr(0xe9)]' ;;
    esac
    (cd "$ENC" && python3 scripts/new_team.py product/host-example-team/team.json --guest-text > /dev/null 2> "$TMP/json-$v.new_team"); echo $? > "$TMP/json-$v.new_team.rc"
    node scripts/workflows/make_args.mjs scripts/workflows/team-layer.js --team product/host-example-team --repo "$ENC" --date 2026-01-01 \
      --scratch "$TMP/scratch" > /dev/null 2> "$TMP/json-$v.make_args"; echo $? > "$TMP/json-$v.make_args.rc"
  done
  msg=$(python3 - "$TMP" 2>&1 <<'PY'
import sys
from pathlib import Path
tmp = Path(sys.argv[1])
read = lambda name: (tmp / name).read_text(encoding="utf-8", errors="replace")
rc = {f"{v}.{t}": read(f"json-{v}.{t}.rc").strip() for v in ("nan", "latin1", "repr") for t in ("new_team", "make_args")}
probs = []
if rc["nan.new_team"] != "0" or rc["nan.make_args"] != "0":
    probs.append(f"NaN and a member slug ending in a newline in the home team.json: new_team.py --guest-text exit "
                 f"{rc['nan.new_team']}, make_args.mjs exit {rc['nan.make_args']} (Python's json takes NaN and "
                 "new_team.py's SAFE_SLUG_RE that slug: both must resolve the guest)")
# Python's repr() of the schema value, as new_team.py's load_config prints it
REPR = ("guest cy-sample: product/home-example-team/team.json: schema 必须是 1（现在是 [2.0, 10000000000000000000001, "
        + repr(chr(7) + chr(0x200b) + chr(0xe9)) + "]） (fix it in the home team first)")
for t, prefix in (("new_team", "❌ "), ("make_args", "make_args: ")):
    ls = [l[len(prefix):] for l in read(f"json-repr.{t}").splitlines() if l.startswith(prefix + "guest ")]
    if rc[f"repr.{t}"] == "0" or ls != [REPR]:
        probs.append(f"a schema of [2.0, 10 ** 22 + 1, chr(7) + chr(0x200b) + chr(0xe9)] in the home team.json: {t} exit "
                     f"{rc['repr.' + t]}, guest line(s) {[l[:150] for l in ls]}, expected [{REPR!r}]")
HEAD, TAIL = "guest cy-sample: product/home-example-team/team.json: 读不了 JSON：", " (fix it in the home team first)"
for t, prefix in (("new_team", "❌ "), ("make_args", "make_args: ")):
    ls = [l[len(prefix):] for l in read(f"json-latin1.{t}").splitlines() if l.startswith(prefix + "guest ")]
    if rc[f"latin1.{t}"] == "0" or len(ls) != 1 or not (ls[0].startswith(HEAD) and ls[0].endswith(TAIL)):
        probs.append(f"bytes that are not UTF-8 in the home team.json: {t} exit {rc['latin1.' + t]}, guest line(s) "
                     f"{[l[:110] for l in ls]}, expected one line '{HEAD}… {TAIL.strip()}' and exit 1")
print("\n".join(probs) or "the constant NaN and a member slug ending in a newline resolve in new_team.py --guest-text and "
      "make_args.mjs alike (exit 0); bytes that are not UTF-8 stop both with one line, '…/team.json: 读不了 JSON：… (fix it in "
      "the home team first)'; a schema of [2.0, 10 ** 22 + 1, chr(7) + chr(0x200b) + 'é'] gives both the line with Python's "
      f"repr(), …（现在是 [2.0, 10000000000000000000001, {repr(chr(7) + chr(0x200b) + chr(0xe9))}]）…")
sys.exit(1 if probs else 0)
PY
); rc=$?
  report "a home team.json read as new_team.py reads it (make_args.mjs)" $rc "$msg"
  # --add-guest: the guest's README row only (no folder; roundtable and DEEP-READING.md unchanged, the next steps point to
  # --guest-text); another guest that does not resolve is only a ⚠️ note, adding that one still fails; a team without
  # README.md (not scaffolded yet) exits 1
  ADD="$TMP/guest-fixture-add-guest"
  cp -r "$FX" "$ADD"
  jedit "$ADD/product/home-example-team/team.json" 'd["members"].append({"slug": "bo-fresh", "name": "Bo Fresh", "hint": "FICTIONAL placeholder of the kit self-test"})'
  python3 scripts/new_team.py "$ADD/product/home-example-team/team.json" --root "$ADD/product" --add-member bo-fresh > /dev/null 2>&1; r0=$?
  jedit "$ADD/product/host-example-team/team.json" 'd["guests"] += [{"slug": "zed-ghost", "home": "home-example-team"}, {"slug": "bo-fresh", "home": "home-example-team"}]'
  o1=$(python3 scripts/new_team.py "$ADD/product/host-example-team/team.json" --root "$ADD/product" --add-guest bo-fresh 2>&1); r1=$?
  o2=$(python3 scripts/new_team.py "$ADD/product/host-example-team/team.json" --root "$ADD/product" --add-guest zed-ghost 2>&1); r2=$?
  mkdir -p "$ADD/product/fresh-example-team" && team_json fresh-example-team "Fresh Example Team" "$DI" cy-sample > "$ADD/product/fresh-example-team/team.json"
  o3=$(python3 scripts/new_team.py "$ADD/product/fresh-example-team/team.json" --root "$ADD/product" --add-guest cy-sample 2>&1); r3=$?
  BROW='| [Bo Fresh](../home-example-team/bo-fresh/SKILL.md) | lens: [TODO] | guest from [Home Example Team](../home-example-team/README.md) · T0 scaffold |'
  below=$(python3 -c 'import sys;l=open(sys.argv[1],encoding="utf-8").read().splitlines();i=l.index(sys.argv[2]) if sys.argv[2] in l else -9;print(l[i+1] if 0<=i+1<len(l) else "(no such row)")' "$ADD/product/host-example-team/README.md" "$GROW" 2>&1)
  probs=""
  [ $r0 -eq 0 ] || probs="$probs; fixture: --add-member bo-fresh in the home team exit $r0"
  { [ $r1 -eq 0 ] && ! grep -q '❌' <<<"$o1"; } || probs="$probs; --add-guest bo-fresh exit $r1: $(grep -m1 '❌' <<<"$o1")"
  [ "$below" = "$BROW" ] || probs="$probs; README.md: under cy-sample's row: ${below:0:90}"
  grep -F '⚠️ guest zed-ghost: not a member of home-example-team' <<<"$o1" | grep -qF 'so it does not stop --add-guest' \
    || probs="$probs; no ⚠️ note on zed-ghost (not a member at home)"
  grep -qF -- '--guest-text' <<<"$o1" || probs="$probs; the next steps do not name --guest-text"
  [ ! -e "$ADD/product/host-example-team/bo-fresh" ] || probs="$probs; host-example-team/bo-fresh exists"
  for f in host-example-roundtable/SKILL.md DEEP-READING.md; do
    cmp -s "$ADD/product/host-example-team/$f" "$HOST_TEAM/$f" || probs="$probs; $f changed"
  done
  { [ $r2 -ne 0 ] && grep -qF '❌ guest zed-ghost: not a member of home-example-team' <<<"$o2"; } || probs="$probs; --add-guest zed-ghost exit $r2"
  { [ $r3 -ne 0 ] && grep -qF 'README.md not found: scaffold the team first: python3 ' <<<"$o3" && grep -qF '(without --add-guest)' <<<"$o3" \
    && [ "$(ls -A "$ADD/product/fresh-example-team")" = team.json ]; } || probs="$probs; a team without README.md: exit $r3: $(tail -1 <<<"$o3")"
  if [ -z "$probs" ]; then ok "new_team.py --add-guest bo-fresh: its row under cy-sample's, no folder, roundtable and DEEP-READING.md unchanged, next steps name --guest-text; zed-ghost (no member at home) only a ⚠️ note, --add-guest zed-ghost exits 1; a team without README.md exits 1 (scaffold it first)"
  else bad "new_team.py --add-guest:${probs#;}"; fi
  # --base-tier with a guest: DEEP-READING.md is the base-tier note of a team without guests with the guest pointer
  # (--guest-text's GUEST_DEEP_READING) ending its paragraph; the template's note itself (in its header comment) has no
  # guest placeholder and is the pre-feature text, so a team without guests renders it unchanged. The pre-feature text is
  # pinned to f9291c1, the template's last change before the guest seats (HEAD drifts once this is committed); without that
  # commit (no git checkout, a shallow clone) the comparison is skipped and the ✓ line says so
  BT="$TMP/guest-fixture-base-tier"
  BTT="$BT/product/base-example-team"
  mkdir -p "$BT/product" && cp -r "$HOME_TEAM" "$BT/product/"
  for g in "" cy-sample; do
    w=$([ -n "$g" ] && echo guest || echo none)
    rm -rf "$BTT" && mkdir -p "$BTT" && team_json base-example-team "Base Example Team" "$DI" "$g" > "$BTT/team.json"
    python3 scripts/new_team.py "$BTT/team.json" --root "$BT/product" --base-tier > /dev/null 2>&1; echo $? > "$TMP/base-tier-$w.rc"
    cp "$BTT/DEEP-READING.md" "$TMP/base-tier-$w.md" 2> /dev/null
  done
  python3 scripts/new_team.py "$BTT/team.json" --root "$BT/product" --guest-text > "$TMP/base-tier-guest-text.json" 2> /dev/null
  PRE=f9291c1
  git -C "$REPO" show "$PRE:references/team-templates/DEEP-READING.md" > "$TMP/DEEP-READING.pre.md" 2> /dev/null \
    || rm -f "$TMP/DEEP-READING.pre.md"
  msg=$(python3 - "$TMP" references/team-templates/DEEP-READING.md "$PRE" 2>&1 <<'PY'
import json, sys
from pathlib import Path
tmp, tpl, pre = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
probs = []
def read(p):
    try:
        return p.read_text(encoding="utf-8")
    except OSError:
        return None
for w in ("none", "guest"):
    rc = (read(tmp / f"base-tier-{w}.rc") or "?").strip()
    if rc != "0":
        probs.append("--base-tier scaffold " + ("with the guest" if w == "guest" else "without guests") + f": exit {rc}")
plain, guest = read(tmp / "base-tier-none.md"), read(tmp / "base-tier-guest.md")
try:
    pointer = json.loads(read(tmp / "base-tier-guest-text.json") or "")["GUEST_DEEP_READING"]
except (ValueError, KeyError, TypeError):
    pointer = ""
if plain is None or guest is None or not pointer:
    probs.append("no DEEP-READING.md from a --base-tier scaffold, or no GUEST_DEEP_READING from --guest-text")
else:
    if "{{" in plain or "Cy Sample" in plain:
        probs.append("without guests: DEEP-READING.md names the guest or keeps a {{placeholder}}")
    if not plain.endswith("\n") or guest != plain[:-1] + pointer + "\n":
        probs.append(f"with the guest: DEEP-READING.md ends {guest[-100:]!r}; expected the note of a team without guests, "
                     f"its paragraph ending with {pointer[:60]!r}…")
def note(text):  # the base-tier entry of the header comment: the line naming "two paragraphs below" (the anchor of
    ls = (text or "").splitlines()  # new_team.py), from the first line of its entry (5-space indent) to the next entry
    k = next((i for i, l in enumerate(ls) if "two paragraphs below" in l), None)
    if k is None:
        return None
    entry = lambda l: len(l) - len(l.lstrip(" ")) <= 5
    a = next((i for i in range(k, -1, -1) if entry(ls[i])), 0)
    b = next((i for i in range(k + 1, len(ls)) if entry(ls[i])), len(ls))
    return "\n".join(ls[a:b])
pre_text = read(tmp / "DEEP-READING.pre.md")  # None: the pinned commit is not in this checkout
mine, head = note(read(tpl)), note(pre_text)
if mine is None:
    probs.append(f"{tpl.as_posix()}: no base-tier note (\"two paragraphs below\") in the header comment")
elif "{{GUEST" in mine:
    probs.append(f"{tpl.as_posix()}: the header comment's base-tier note carries a guest placeholder")
if pre_text is not None and head is None:
    probs.append(f"{pre}:{tpl.as_posix()}: no base-tier note (\"two paragraphs below\") in the header comment")
elif head is not None and mine is not None and mine != head:
    probs.append(f"{tpl.as_posix()}: the header comment's base-tier note differs from the pre-feature text ({pre})")
print("\n".join(probs) or "DEEP-READING.md is the base-tier note of a team without guests with the guest pointer ending "
      "its paragraph; the template's base-tier note has no guest placeholder "
      + (f"and equals the pre-feature text ({pre})" if head is not None
         else f"(commit {pre} is not in this checkout: the pre-feature comparison is skipped)"))
sys.exit(1 if probs else 0)
PY
); rc=$?
  report "new_team.py --base-tier with a guest" $rc "$msg"
  # a copy whose home folder is a fresh scaffold (no SKILL.md, no notes yet): the host README's guest link is pending
  PEND="$TMP/guest-fixture-pending"
  cp -r "$FX" "$PEND" && rm -f "$PEND/product/home-example-team/cy-sample/SKILL.md" "$PEND/product/home-example-team/cy-sample/references/research/"*.md
  out=$(python3 scripts/check_links.py "$PEND/product/host-example-team/README.md" 2>&1); rc=$?
  if [ $rc -eq 0 ] && grep -qF '../home-example-team/cy-sample/SKILL.md (pending:' <<<"$out"; then
    ok "check_links.py: a guest link to a scaffolded home folder without notes is pending ($(tail -1 <<<"$out" | sed 's/ (member.*//'))"
  else bad "check_links.py on the host README, home folder without notes (exit $rc)"; tail -3 <<<"$out"; fi
fi

echo "self-test: $([ $fail -eq 0 ] && echo "✅ all passed" || echo "❌ $fail failed")"
exit $fail
