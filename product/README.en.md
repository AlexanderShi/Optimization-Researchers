# product/ · Per-researcher skills (team-kit products)

English | [中文](README.md)

This folder holds the **per-researcher skills** of the repository's optimization teams (six teams, listed below). They
are produced and maintained with the team-kit at the repository root (`scripts/` + `references/`; see
[TEAM-KIT.md](../TEAM-KIT.md)). They sit beside `teams/<team>/SKILL.md` (team-level skills distilled from the closed
corpus by DISTILL.md); the two pipelines do not reference each other.

| Folder | Team | Contents | Tier |
|------|------|------|------|
| `dfo-team/` | DFO Team (derivative-free optimization) | Powell, Conn, Scheinberg, Vicente and Audet + `dfo-roundtable` | Deep tier (356 works read in full, 59 in part, 1139 quotes checked verbatim; see `DEEP-READING.md`) |
| `nonlinear-team/` | **NLP Team** (nonlinear programming; the source folder name nonlinear-team is kept) | Curtis, Nocedal, Wright, Ye, Wächter, Gill, Toint, Gould, Fletcher, Nesterov and Robinson (eleven) + `nonlinear-roundtable` | Mixed tier: Curtis deep (2026-10-10), Nocedal deep (2026-10-17); the other nine at base tier (public-source research, no full-text deep reading) |
| [`lp-team/`](lp-team/README.md) | **LP Team** (linear programming engines) | Qi Huangfu, John J. H. Forrest and Robert E. Bixby + `lp-roundtable` | Base tier (public-source research, no full-text deep reading) |
| [`milp-team/`](milp-team/README.md) | **MILP Team** (mixed-integer linear programming: branch-and-cut inside solvers, decomposition, MIP benchmarking) | Ambros M. Gleixner, Marco E. Lübbecke, Tobias Achterberg and Matteo Fischetti, with Forrest and Bixby of the LP Team as guests + `milp-roundtable` | Base tier (public-source research; T1 validated on sealed questions) |
| [`minlp-team/`](minlp-team/README.md) | **MINLP Team** (mixed-integer nonlinear and global optimization) | Grossmann, Leyffer, Sahinidis, Misener, Burer and Dey + `minlp-roundtable` | Mixed tier: Leyffer, Sahinidis, Misener, Burer and Dey deep; Grossmann's deep reading stops at T3.2 (full texts fetched, no cards yet), so he is checked at base tier |
| [`optimization-council/`](optimization-council/README.md) | **Optimization Council** (Bertsimas convenes and leads cross-team discussion among the LP, NLP, DFO and MINLP teams; the front door optimization-lead also routes MILP questions to the MILP Team) | Dimitris Bertsimas (convener; his skill is split into nine domain files: LO, IO, RO, CP, SD, ML, DA, HS, AP) + [`optimization-lead`](optimization-council/optimization-lead/SKILL.md) (front door: he frames a question by domain and stage gate, routes it to the team that owns it, then reviews each team's answer) + `council-roundtable` (cross-team discussion); members of the four teams sit as guest delegations and must be installed together with their teams | Deep tier: Bertsimas (deep reading and nine domain files on 2026-10-29, domain map on 2026-10-31; 413 works read in full, 59 in part, 1125 quotes checked verbatim, plus the public parts of 21 books; see `DEEP-READING.md`); the guest teams keep their own tiers (DFO deep; NLP mixed; MINLP mixed, five deep; LP base). First session record: [`first-session-2026-10-31.md`](optimization-council/first-session-2026-10-31.md) (topic "the price of exactness", ten delegates from four teams; plan v2 awaits your approval at checkpoint 4) |

Each team folder's `README.md`, `DEEP-READING.md` and `team.json` describe the team and list its members;
`python3 scripts/team_status.py product/<team>` recomputes progress and the coverage tables at any time.

## Sources and provenance

- **Source**: the `product/dfo-team` and `product/nonlinear-team` folders of the AlexanderShi/nvwa-skill repository,
  synced from commit `eb012fa` (same content as `ff2ef35`, 2026-09-28) on 2026-10-09, byte for byte (539 files).
  The folder names match nvwa's, so the `product/...` paths inside the team docs work unchanged in this repository.
  Later changes made here with the team-kit are recorded in `teams/DISTILLATION_LOG.md`: Curtis's deep reading
  (entry (10)), Daniel P. Robinson joining nonlinear-team at base tier (entry (11), 2026-10-17, not from the nvwa sync),
  Nocedal's deep reading (entry (12), 2026-10-17).
- **Distillation method**: team-kit (web research + one paper card per work + an evidence ledger), dated
  `researched: 2026-09-27`. Each researcher's evidence chain is in their
  `references/research/09-evidence-ledger.md`, the paper cards in `references/research/cards/`.
- **Relation to this repository's corpus**: these skills were **not** distilled under the closed-corpus protocol of
  `DISTILL.md`; their factual claims carry no `[DFO-S*]` / `[NLP-R*]` corpus IDs, and their sources are in their own
  ledgers. The team-level skills (`teams/<team>/SKILL.md`) still rest only on the corpus in their folders.
  To bring a researcher into the corpus, write `teams/<team>/researchers/<name>.md` separately under
  `standards/researcher-extraction.md` (so far for Scheinberg and Duchi).

## Installation

Copy a researcher's folder as a whole to `~/.claude/skills/<name>/` (for example
`product/dfo-team/michael-powell/` → `~/.claude/skills/michael-powell/`).

A roundtable skill resolves its members as **sibling folders** (`../<member>/SKILL.md`) first, and only then under
`~/.claude/skills/<name>/`. So either install the whole team folder together, or install the roundtable and its members
side by side under `~/.claude/skills/`. The link from `nonlinear-roundtable` to `dfo-roundtable` is
`../../dfo-team/dfo-roundtable/SKILL.md` and works only inside this repository's layout.

Teams with guests (`guests` in `team.json`: members of another team who sit at this team's roundtable; their skill exists
only once, in their home team, and this team's folder has no folder for them): in this repository the roundtable finds a
guest at `../../<home>/<slug>/SKILL.md`, where the guest's research notes and cards also live. When installing to
`~/.claude/skills/`, copy each guest's folder from the same checkout as well, besides this team's folders
(bash: `cp -r product/<home>/<slug> ~/.claude/skills/`;
PowerShell: `Copy-Item -Recurse product\<home>\<slug> "$HOME\.claude\skills\"`).
If the checkout holds git-ignored full-text PDFs and `txt/`, copy only the files `git ls-files -- <folder>` lists.
Both install blocks of a team README (bash and PowerShell) contain these lines: above each home team's copy line, a
separate comment line `# guest(s) from the <home team title>: …, see product/README.md` points back here; the copy lines
themselves carry no comment. If someone is missing, the roundtable says who and carries on without them.

After installing, let only the entry skills take up the skill listing: in `~/.claude/settings.json`, set every
researcher to `"name-only"` under `skillOverrides` (listed by name, without a description), and keep the descriptions of
the front door `optimization-lead`, the five team roundtables, `council-roundtable` and the corpus team skills
`dfo-team` and `nlp-team`. Claude Code puts the description of every installed skill into the context on every turn, and
the listing has a character budget (`skillListingBudgetFraction`, by default 1% of the context window); beyond it,
descriptions are dropped starting with the least-invoked skills. The descriptions of the 30 researchers add up to about
25,000 characters (2026-11-26) and would push out the entry skills' descriptions. Roundtables and the front door read
member files by path and are not affected; to use one researcher alone, go through the roundtable's `solo <member>` or
type `/<member slug>`. When you add a researcher, add a line to `skillOverrides`.

## Copyrighted material stays out of the repository

Following the kit's rules, the root `.gitignore` ignores PDF/PS/DjVu/EPUB files under `product/**/references/sources/`,
`papers/txt/` and `private/` (except its README). After running download scripts such as
`scripts/acquire_fulltexts.py`, do not `git add -f`.
