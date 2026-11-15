export const meta = {
  name: 'team-integrate',
  description: "T3.8 integrate: refresh a research team's README, DEEP-READING.md and roundtable (fault lines backed by card evidence from both sides) from the members' finished deep reading, then review with two read-only lenses and fix until the gates pass",
  whenToUse: 'After team-synthesize (and team-tighten, if run) for the members, and after every team-increment (research-team playbook, stage T3.8).',
  phases: [
    { title: 'Status', detail: 'team_status.py: exact coverage table and each member stage' },
    { title: 'Integrate', detail: 'docs agent (README + DEEP-READING) and roundtable agent, on disjoint files' },
    { title: 'Verify', detail: 'two read-only skeptics: numbers/links/commands and evidence/attribution' },
    { title: 'Fix', detail: 'apply confirmed findings; rerun gates; one more fix round if a gate still fails' },
  ],
}

/*
 * team-integrate.js · research-team kit, stage T3.8 (team layer after the deep reading).
 * Launch:  Workflow({ scriptPath: '<repo>/scripts/workflows/team-integrate.js', args: { ... } })
 *
 * Args shared by all team workflows:
 *   args.repo     absolute path of the nuwa repo (has scripts/, references/)
 *   args.team     team folder relative to repo, e.g. "product/bandit-team" (holds team.json)
 *   args.scratch  absolute scratch dir for batch/chunk JSON files and backups (agents may write there)
 *   args.date     "YYYY-MM-DD" (scripts cannot call Date.now())
 *   args.members  array of member objects copied from team.json (slug, name, surname, living, hint, scholar,
 *                 dblp, orcid, homepage, chase_hints, student_mode). This step is team-level: it needs all
 *                 members together, so it runs once for the team (no per-member pipeline); pass every member.
 *   args.request  optional: the user's request in their own words; opens every agent prompt (set with make_args.mjs --request)
 *
 * Args specific to team-integrate:
 *   args.root_readme      default false: also refresh this team's one row/line in <repo>/README.md (nothing else there)
 *   args.new_fault_lines  maximum number of new documented disagreements the roundtable agent may add (default 2)
 *   args.guests           optional; make_args.mjs builds it from team.json "guests" (never by hand): members of other
 *                         teams seated here, READ-ONLY. Each = the guest's entry in its home team's team.json verbatim
 *                         plus "home" and "dir" (its folder, repo-relative: "<the folder that holds the teams>/<home>/
 *                         <slug>", i.e. "product/<home>/<slug>" for teams under product/). Fault lines follow a per-seat
 *                         card rule (a seat with paper cards in its own folder is cited by them; a guest without cards
 *                         by its notes, never marked "(card evidence pending)": that mark names this team's members not
 *                         ready only); the coverage tables stay members-only, with one dated pointer line per guest to
 *                         its home team's DEEP-READING.md (never its numbers), and the record's opening paragraph ends
 *                         with the guest pointer that python3 scripts/new_team.py <team.json> --guest-text prints
 *                         (GUEST_DEEP_READING). Rerun this step after the home team re-reads or re-synthesizes a guest
 *                         (team-read / team-synthesize / team-tighten / team-increment there). While no member of this
 *                         team has finished the synthesis this step integrates nothing, so a guest's paper cards are
 *                         brought in by a team-layer.js (T2) rerun instead (team_check.py wants a carded guest cited by
 *                         card at either tier); "next" says which step to rerun. A guest without a SKILL.md yet (its
 *                         home team's T1 has not reached this branch) was not seated by T2 and is not seated here
 *                         either: every agent is told so, and "next" asks to merge that T1 here, rerun team-layer.js
 *                         (T2) here, then this step, and names the team_check.py rows that stay red on it until then.
 *   (old names rootReadme / newFaultLines are still accepted, with a log line)
 *
 * Writes: <team>/README.md, <team>/DEEP-READING.md, <team>/<roundtable>/SKILL.md (+ one row of <repo>/README.md
 *   with root_readme); never a file in a guest's folder.
 *   Backups: <scratch>/<team-folder>-{README,DEEP-READING,roundtable-SKILL}.before-integrate-<date>.md.
 * Template TODO items this step resolves: every [TODO: …] in README.md, DEEP-READING.md and the roundtable SKILL.md that
 *   names team-integrate.js or T3.8.
 * Gates: DEEP-READING.md's table == python3 scripts/team_status.py <team> --coverage and the README's five-column summary
 *   == --coverage --short; scripts/check_links.py <team> → 0 broken; every fault line cites existing card ids on both
 *   sides; grep -rn --include='*.md' -e '{{' -e '\[TODO' <team> → no output (members still in progress excepted, in
 *   their own folders). The roundtable is not a research-craft skill: it is never gated on scripts/quality_check.py.
 * Next: commit the team docs.
 * Cost: 6-7 agents per run (status, docs, roundtable, 2 read-only reviewers, 1-2 fixers). The worked example
 *   product/dfo-team/ (5 members) measured 4 agents / ~1M tokens with an earlier version of this step.
 */

const a = (typeof args === 'string' ? JSON.parse(args) : args) || {}
function need(keys) {
  const miss = keys.filter(k => a[k] === undefined || a[k] === null || a[k] === '')
  if (miss.length) throw new Error(`team-integrate: missing args: ${miss.join(', ')} (see the header comment)`)
}
need(['repo', 'team', 'scratch', 'date', 'members'])
if (!Array.isArray(a.members) || !a.members.length) throw new Error('team-integrate: args.members must be a non-empty array of team.json member objects')
if (!/^\d{4}-\d{2}-\d{2}$/.test(String(a.date))) throw new Error('team-integrate: args.date must be "YYYY-MM-DD"')
a.members.forEach((m, i) => { if (!m || !/^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') || !m.name) throw new Error(`team-integrate: members[${i}] needs a kebab-case slug and a name`) })
if (!/^(?:[A-Za-z]:[\\/]|\/)/.test(String(a.repo)) || !/^(?:[A-Za-z]:[\\/]|\/)/.test(String(a.scratch))) throw new Error('team-integrate: args.repo and args.scratch must be absolute paths')
if (String(a.team).startsWith('/')) throw new Error('team-integrate: args.team must be relative to args.repo, e.g. "product/<team>"')
// args.guests (optional, built by make_args.mjs; null counts as absent): a guest's folder sits beside this team's,
// <parent of args.team>/<home>/<slug>
if (a.guests !== undefined && a.guests !== null && !Array.isArray(a.guests)) throw new Error('team-integrate: args.guests must be an array (make_args.mjs builds it from team.json "guests")')
// the team folder as a normalized POSIX path, as make_args.mjs normalizes it (path.posix.normalize) for the guests' "dir":
// "product//x", "product/x/.", "product\x" and "product/../product/x" are all "product/x"; a ".." leaving the repo stays
const TEAM_POSIX = String(a.team).replace(/\\/g, '/').split('/')
  .reduce((p, s) => (s === '..' && p.length && p[p.length - 1] !== '..' ? p.slice(0, -1) : s && s !== '.' ? [...p, s] : p), []).join('/')
const TEAMS_ROOT = TEAM_POSIX.includes('/') ? TEAM_POSIX.slice(0, TEAM_POSIX.lastIndexOf('/') + 1) : ''
// a guest's folder sits beside this team's folder, inside the repo
if ((a.guests || []).length && (!TEAM_POSIX || TEAM_POSIX === '..' || TEAM_POSIX.startsWith('../'))) throw new Error(`team-integrate: args.team "${a.team}" is the repo itself or outside it: a team with guests must be a folder inside args.repo, beside its guests' home teams (make_args.mjs builds the args)`)
for (const [i, g] of (a.guests || []).entries()) {
  if (!g || typeof g !== 'object' || !/^[a-z0-9][a-z0-9-]*$/.test(g.slug || '') || typeof g.name !== 'string' || !g.name.trim()) throw new Error(`team-integrate: guests[${i}] needs a kebab-case slug and a name (its entry in the home team's team.json)`)
  if (!/^[a-z0-9][a-z0-9-]*$/.test(g.home || '') || g.home === TEAM_POSIX.split('/').pop()) throw new Error(`team-integrate: guests[${i}] (${g.slug}) needs a kebab-case home: another team's folder`)
  if (typeof g.dir !== 'string' || g.dir.includes('..') || g.dir !== `${TEAMS_ROOT}${g.home}/${g.slug}`) throw new Error(`team-integrate: guests[${i}] (${g.slug}): dir must be "${TEAMS_ROOT}${g.home}/${g.slug}" (repo-relative, no ".."; make_args.mjs builds it)`)
  if (a.members.some(m => m.slug === g.slug)) throw new Error(`team-integrate: guests[${i}]: ${g.slug} is also in args.members (a person is a member of one team and a guest elsewhere)`)
  if (a.guests.findIndex(x => x && x.slug === g.slug) !== i) throw new Error(`team-integrate: guests[${i}]: ${g.slug} is listed twice`)
}
// args keys this workflow reads (all snake_case); anything else is logged. Old camelCase names still work as aliases.
const KNOWN_ARGS = ['repo', 'team', 'scratch', 'date', 'members', 'request', 'root_readme', 'new_fault_lines', 'guests']
const RENAMED = { rootReadme: 'root_readme', newFaultLines: 'new_fault_lines' } // old camelCase name -> current name
const ALIAS_OF = Object.fromEntries(Object.entries(RENAMED).map(([o, k]) => [k, o]))
function arg(key) { return a[key] !== undefined ? a[key] : ALIAS_OF[key] ? a[ALIAS_OF[key]] : undefined }
for (const [old, key] of Object.entries(RENAMED)) {
  if (a[old] === undefined) continue
  log(a[key] === undefined
    ? `team-integrate.js: args.${old} is the old name of args.${key}; using it (rename it to ${key})`
    : `team-integrate.js: args.${old} ignored because args.${key} is also given (${old} is only an alias)`)
}
const unknownArgs = Object.keys(a).filter(k => !KNOWN_ARGS.includes(k) && !(k in RENAMED))
if (unknownArgs.length) log(`team-integrate.js ignores args key(s) it does not know (misspelt?): ${unknownArgs.join(', ')}; it reads ${KNOWN_ARGS.join(', ')}`)
// args.request (optional): the user's request in their own words. Workflow agents see only their prompt and the
// user's latest message in the launching session; when that message is a side question they may decline the step,
// so A() opens every prompt with the request.
const REQUEST = typeof a.request === 'string' ? a.request.replace(/\s+/g, ' ').trim() : ''
if (a.request !== undefined && a.request !== null && typeof a.request !== 'string') log(`team-integrate.js: args.request must be a string (the user's request in their own words), got ${Array.isArray(a.request) ? 'array' : typeof a.request}; ignored`)
const WHY = REQUEST ? `Why this agent runs: in the session that launched this workflow the user asked: "${REQUEST}". This agent is one step of that work (research-team kit, team-integrate.js, stage T3.8). Do the step below.\n\n` : ''

const REPO = String(a.repo).replace(/\/+$/, '')
const TEAM_REL = String(a.team).replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const TEAM_NAME = TEAM_REL.split('/').pop()
const SCR = String(a.scratch).replace(/\/+$/, '')
const DATE = a.date
const ROOT_README = arg('root_readme') === true
const NEW_FAULTS = arg('new_fault_lines') === undefined ? 2 : Number(arg('new_fault_lines'))
const MEMBERS = a.members
// guests (args.guests): members of other teams seated here, READ-ONLY. Every guest sentence below is conditional on
// G, so that the prompts of a team without guests stay exactly as they were.
const GUESTS = a.guests || []
const G = GUESTS.length > 0
const GUEST_SLUGS = new Set(GUESTS.map(g => g.slug))
const GDIR = g => `${REPO}/${g.dir}`
const HOME_DIR = g => g.dir.slice(0, g.dir.lastIndexOf('/'))   // repo-relative home team folder, e.g. product/lp-team
const GUEST_DIRS = GUESTS.map(GDIR).join(', ')
const homeOf = slug => GUESTS.find(g => g.slug === slug)
// the guest text exactly as the scaffold renders it (read-only; one JSON object): T3.8 refreshes DEEP-READING.md's guest
// pointer from its GUEST_DEEP_READING string
const GUEST_TEXT = `python3 ${REPO}/scripts/new_team.py ${TEAM}/team.json --guest-text${TEAMS_ROOT === 'product/' ? '' : ` --root ${TEAMS_ROOT ? `${REPO}/${TEAMS_ROOT.slice(0, -1)}` : REPO}`}`
// after a home team re-reads or re-synthesizes a guest, this step runs again here
const GUEST_HOMES = [...new Set(GUESTS.map(HOME_DIR))].join(', ')
const GUEST_RERUN = `After the home team re-reads or re-synthesizes a guest (team-read, team-synthesize, team-tighten or team-increment in ${GUEST_HOMES}), rerun this step here.`
// ... but this step integrates nothing while no member of this team is ready: until then T2 cites a carded guest's cards
const T2_CALL = `node scripts/workflows/make_args.mjs team-layer --team ${TEAM_REL} builds the call`
const GUEST_RERUN_EARLY = `A guest that gets paper cards in its home team (team-read in ${GUEST_HOMES}) must be cited by card here (team_check.py fails the roundtable until it is): while no member of this team has finished the synthesis, rerun team-layer.js (T2) here, which cites it by card at either tier (${T2_CALL}); once one has, rerun this step.`
// a guest without a SKILL.md yet (its home team's T1 has not reached this branch) was not seated by T2, as a member without
// a skill: this step seats nothing for it (every agent is told), and T2 seats it once that T1 is merged here, then this step
const NO_SKILL_CTX = rows => `Guests without a SKILL.md yet (their home team's T1 has not reached this branch): ${rows.map(r => `${r.slug} (${r.stage}; ${r.home})`).join(', ')}. They are not seated, as a member without a skill: add nothing for them (no roundtable Team-table row, seating row, fault-line side or Guest seat note; team-layer.js seats them once that T1 is merged here). Their README row (its "lens: [TODO]" and stage included), intro-clause name and install lines stay as new_team.py rendered them, and that row's link to their SKILL.md is pending in check_links.py while their folder has no research notes and broken once it has some: both are expected until that merge, never a reason to fill or delete the row.`
const NO_SKILL_NEXT = rows => `Guests without a SKILL.md yet, not seated here: ${rows.map(r => `${r.slug} (T1 in ${HOME_DIR(homeOf(r.slug))})`).join(', ')}. Once their home team's T1 has written the SKILL.md, merge that branch here, rerun team-layer.js (T2) here to seat them (${T2_CALL}), then this step; until then the gates stay red on them: team_check.py's guests row (SKILL.md missing), its roundtable row (not in the Team table, seated in no row, in no fault line: team_check.py counts every guest of team.json as a seat, as it does every member, so it passes once the T2 rerun seats them) and its templates row (their README rows' "lens: [TODO]"), and check_links.py (team_check.py's links row) once their folders have research notes, which turns their README links from pending to broken.`

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A() needs opts.phase and opts.label')
  return agent(`${WHY}${prompt}`, opts)
}
function bk(name) { return `${SCR}/${TEAM_NAME}-${name}.before-integrate-${DATE}.md` }
const memberLine = MEMBERS.map(m => `${m.name} (${m.slug}${m.student_mode ? ', student_mode' : ''})`).join('; ')
const guestLine = GUESTS.map(g => `${g.name} (${g.slug}, guest from ${g.home}, folder ${GDIR(g)}${g.student_mode ? ', student_mode' : ''})`).join('; ')

const RULES = `House rules (non-negotiable):
- Evidence: every number comes from a script run (team_status.py), every claim about a member's research points to that member's card ids with pages (e.g. [<slug> card S072 p. 5]); quotes stay verbatim; never guess — write "not recorded" or "in progress" instead.${G ? ' A guest\'s card ids live in its own folder (its home team\'s); a guest without cards is cited through its own research notes or SKILL.md (e.g. [<slug> note 05 §3], [<slug> SKILL.md, "Method N · …"]).' : ''}
- Attribution: nothing written by a coauthor, a reviewer, an interviewer or a newsletter/column author is attributed to a member; reviews are the reviewer's voice.
- Privacy: never open, read or quote anything under a references/sources/private/ folder; only say that such folders are git-ignored and never read.
- Templates: README.md, DEEP-READING.md and the roundtable SKILL.md came from ${REPO}/references/team-templates/; their [TODO: …] items each name the step that resolves them. This step (team-integrate.js, T3.8) resolves every one that names team-integrate.js or T3.8, and after it no [TODO and no {{ may remain in the team's .md files (a member still in progress keeps the TODO items of its own folder).
- The roundtable is not a research-craft skill: never run scripts/quality_check.py on it (its persona-mode score, about 2/6, means nothing here). Its gates are: check_links.py 0 broken; every seated member has a complete Roundtable Card; every fault line cites card evidence from both sides (python3 scripts/check_citations.py <team> --roundtable → 0 problems: each [<slug> card S012 pp. …] names that member's existing card, read at those pages); no [TODO or {{ left.${G ? ' Per seat: a seat (member or guest) with paper cards in its own folder is cited by card ids from that folder; a guest without cards (its home team at the base tier, or its deep reading not done yet) is cited by its research notes or SKILL.md. check_citations.py resolves a guest\'s [<slug> card …] in the guest\'s own folder.' : ''}
- Scope: edit only the files this step names as its outputs; scratch files go under ${SCR}/. Do not git commit, push, stash, reset or checkout (the operator commits after the stage).${G ? ` Never edit, create, move or delete anything in a guest's folder (${GUEST_DIRS}) or elsewhere in another team's folder: a guest's files belong to its home team, where every per-member step for it runs.` : ''}`

function ctx(status) {
  return `Team: ${TEAM}/. Read ${TEAM}/team.json first ("field", "language", "roundtable" folder, "members"${G ? ', "guests"' : ''}). The team was built with the nuwa kit in ${REPO} (templates in ${REPO}/references/team-templates/, playbook ${REPO}/references/research-team-playbook.md, tools in ${REPO}/scripts/ and ${REPO}/scripts/workflows/). Today is ${DATE}.
Members in this run: ${memberLine}.${G ? `
Guests in this run (members of other teams seated here; READ-ONLY): ${guestLine}.` : ''}
Each member folder that finished the deep reading has: references/sources/publications/works.json + scholar.md; references/sources/papers/INDEX.md (full-text status, role, read level; PDFs and txt/ git-ignored); references/research/cards/*.md + *.digest.json (D1–D8 paper cards); 07-paper-cards.md (card index); 08-deep-reading-synthesis.md (patterns, promotions, corrections, open gaps); 09-evidence-ledger.md (evidence moved out of SKILL.md); references/technique-catalog.md; an updated SKILL.md. Student-mode members also have proof-playbook.md, open-problems.md, reading-path.md.${G ? ' A guest\'s folder has the same files once its home team has done its deep reading.' : ''}
${status ? `Status from python3 ${REPO}/scripts/team_status.py ${TEAM} (run ${DATE}):
Members ready (08 exists): ${status.ready.join(', ') || 'none'}. Not ready: ${status.not_ready.map(r => `${r.slug} (${r.stage})`).join(', ') || 'none'}.${G ? ` Guests ready (08 in their own folders; stage from team_status.py in their home teams): ${status.guests_ready.join(', ') || 'none'}. Guests not ready: ${status.guests_not_ready.map(r => `${r.slug} (${r.stage}; ${r.home})`).join(', ') || 'none'}.${status.guests_no_skill.length ? ` ${NO_SKILL_CTX(status.guests_no_skill)}` : ''} Guests are not in the coverage tables below: their coverage is in their home teams' DEEP-READING.md (${[...new Set(GUESTS.map(g => `../${g.home}/DEEP-READING.md`))].join(', ')}); never copy their numbers.` : ''}
Exact coverage table (python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage), for DEEP-READING.md:
${status.coverage_md}
Five-column summary summed from it (python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage --short), for the team README:
${status.coverage_short_md || '(not returned: run the command)'}` : ''}

${RULES}`
}

function statusPrompt() {
  return `${ctx(null)}

Your job (STATUS, read-only): run python3 ${REPO}/scripts/team_status.py ${TEAM} --json, python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage and python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage --short. Return coverage_md = the --coverage output verbatim; coverage_short_md = the --coverage --short output verbatim; for each member of team.json its slug, inferred stage and whether references/research/08-deep-reading-synthesis.md exists; and problems (e.g. a member in args but not in team.json or the reverse, a script error). Do not edit any file.${G ? ` Guests: for each guest in this run also run python3 ${REPO}/scripts/team_status.py ${REPO}/<its home team folder> --json and add the guest's row to members, with home = its home team (slug, its stage there, has_08 = its folder's references/research/08-deep-reading-synthesis.md exists, has_cards = its folder's references/research/cards/ holds paper cards, *.digest.json, has_skill = its folder's SKILL.md exists); report as problems a guest in args but not in team.json "guests" (or the reverse) and a guest no longer among its home team's members. coverage_md and coverage_short_md stay this team's (members only).` : ''}`
}

function docsPrompt(status) {
  return `${ctx(status)}

Your job (DOCS): update these files and no others: ${TEAM}/DEEP-READING.md and ${TEAM}/README.md${ROOT_README ? `, plus the single row/line for ${TEAM_REL} in ${REPO}/README.md` : ''}. First save copies: mkdir -p ${SCR}; cp ${TEAM}/DEEP-READING.md ${bk('DEEP-READING')}; cp ${TEAM}/README.md ${bk('README')} (skip a file that does not exist yet). Read each file fully before editing, and write in the language each file already uses (team.json "language" for new text).
1. ${TEAM}/DEEP-READING.md: the record of the deep reading. Keep the section structure of ${REPO}/references/team-templates/DEEP-READING.md if that template exists (otherwise keep the file's own sections): status and date (${DATE}); the pipeline actually used, from evidence only (works.json "source_note"/"sources", INDEX.md Source-column counts, the card files, the scripts and workflows in ${REPO}/scripts/ and ${REPO}/scripts/workflows/) — write "not recorded" rather than guess; the commands per member (python3 scripts/acquire_fulltexts.py ${TEAM_REL}/<slug>; python3 scripts/plan_reading_batches.py ${TEAM_REL}/<slug> [--round N --exclude …]; python3 scripts/verify_card_quotes.py ${TEAM_REL}/<slug>; python3 scripts/mark_read_from_cards.py ${TEAM_REL}/<slug>; python3 scripts/team_status.py ${TEAM_REL}; the workflows team-read / team-synthesize / team-tighten / team-increment / team-integrate); the coverage table exactly as above; the reading-batch brief as used (at most 15 lines, summarised from ${REPO}/scripts/workflows/team-read.js); what is still missing per member (works without an open text, books whose bodies were not read — the biggest gaps from each 08's "Open gaps"); how to extend (drop a PDF named like INDEX.md's ID into papers/, rerun acquire_fulltexts.py, plan a new round with --round N --exclude, or run team-increment.js); the privacy and integrity notes (private/ never read; PDFs and txt/ git-ignored).${G ? ` Guests: the commands and the coverage table cover this team's own members only; for each guest write one dated pointer line instead (${DATE}): "<Name> (guest from <home title>): deep reading recorded in [../<home>/DEEP-READING.md](../<home>/DEEP-READING.md)" — never copy a guest's numbers, which change with its home team's runs. Also run ${GUEST_TEXT} (read-only: it prints one JSON object with the guest text the scaffold renders) and make the record's opening paragraph ("This is the record of how the skills of … are deepened. …") end with its GUEST_DEEP_READING string, copied exactly, in place of any older guest pointer there (a guest added after the scaffold is missing from it until this step); if the command exits 1, report its error lines in problems and leave that paragraph as it is.` : ''}
2. ${TEAM}/README.md: Honest Boundary: replace any "without full-text reading" wording (and, for a team first delivered at the base tier, a Resources note that the deep-reading files are absent) with the true coverage: paste the five-column summary above (team_status.py --coverage --short) unchanged, pointing to DEEP-READING.md; never type or re-add a number yourself. Resources tree: show publications/works.json + scholar.md, papers/INDEX.md (+ git-ignored PDFs/txt), research/cards/, 07-paper-cards.md, 08-deep-reading-synthesis.md, 09-evidence-ledger.md, technique-catalog.md (only files that exist). Under Use, mention each member's technique catalog. In the team table, update a member's lens/status only where the member's methods or stage changed. Members not ready are shown "in progress" with their stage, never with invented numbers.${G ? ` A guest's row keeps its link ../<home>/<slug>/SKILL.md and takes its status from the Guests section of python3 ${REPO}/scripts/team_status.py ${TEAM} (its stage in its home team only, never coverage numbers); its technique catalog, if any, is ../<home>/<slug>/references/technique-catalog.md; the five-column summary stays members-only, and the Resources tree says that guests' files live in their home teams' folders.` : ''}${ROOT_README ? `
3. ${REPO}/README.md: only the row/line for ${TEAM_REL}: a short note that the skills were deepened by full-text reading, linking ${TEAM_REL}/DEEP-READING.md. Change nothing else.` : ''}
Resolve every [TODO: …] in DEEP-READING.md and README.md that names team-integrate.js or T3.8, from the script output, the members' 08s and INDEX.md; delete the TODO lines the templates say to delete; a member not ready is written "in progress" (with its stage), never left as a TODO. Afterwards grep -n -e '\\[TODO' -e '{{' ${TEAM}/DEEP-READING.md ${TEAM}/README.md must print nothing${G && status.guests_no_skill.length ? ' but the "lens: [TODO]" of the README row of a guest without a SKILL.md yet (named above), which stays until team-layer.js seats it' : ''}.
Then run python3 ${REPO}/scripts/check_links.py ${TEAM} (0 broken${G && status.guests_no_skill.length ? '; a broken README link to a guest without a SKILL.md yet, named above, is expected: report it and keep the row' : ''}) and return files changed and a summary.`
}

function roundtablePrompt(status) {
  return `${ctx(status)}

Your job (ROUNDTABLE): update ${TEAM}/<roundtable>/SKILL.md only (the folder named by team.json "roundtable"). First save a copy to ${bk('roundtable-SKILL')} (mkdir -p ${SCR} first).
1. Read it fully, then read each ready member's SKILL.md (Roundtable Card, core research method headings, Honest Boundary) and 08-deep-reading-synthesis.md (Promotions, Variants and contradictions, Technique inventory).${G ? ` Read each guest's the same way in its own folder (${GUEST_DIRS}): its 08 only if it is ready.` : ''}
2. Team table / member descriptions: update only where a member's methods changed (new or renamed core methods).${G ? ' Keep the guest rows, the Guest seat notes and the guest path in Loading the Team; update a guest\'s row only where its methods changed.' : ''}
3. Documented disagreements (fault lines) and shared references: check every disagreement against the members' cards. Keep a disagreement only if the cards support BOTH sides; add page-referenced card ids for each side (e.g. "[<slug> card S072 p. 5]"). Add at most ${NEW_FAULTS} new documented disagreement(s), and only ones the full texts clearly show, each with card evidence from both sides. A disagreement you cannot back with cards is reworded as an open question or removed (say which in the summary).${G ? ' Per seat: a guest\'s side cites card ids from its own folder (its references/research/07-paper-cards.md and cards/) when it has cards; a guest without cards keeps its notes or SKILL.md evidence, so never drop or reword a fault line only because a guest\'s side has no cards. That evidence stands until the guest\'s home team does the deep reading (a base-tier home team never does), so remove any "(card evidence pending…)" mark from a guest\'s side: the mark names only this team\'s own members whose side has no cards yet (members not ready), and a fault line with no such side carries none. A disagreement with a guest\'s home teammate who is not seated here never becomes a fault line here.' : ''}
4. Member agent brief: tell each member agent to consult its references/technique-catalog.md and references/research/08-deep-reading-synthesis.md when proposing designs, experiments or proofs, and to cite card ids; for student_mode members also proof-playbook.md, open-problems.md and reading-path.md.
5. Honest Boundary: replace any "no full-text reading" statement with one line pointing to ../DEEP-READING.md for coverage. A team first delivered at the base tier also carries finished base-tier sentences, not TODO items: "No deep reading was done (base tier); the fault lines rest on the members' research notes." under Papers behind the documented disagreements (replace it with the card-based list), and "…have not been checked against full texts" / "no full text has been read yet" in the Honest Boundary (replace them with how the fault lines now rest on paper cards).${G ? ' The guests\' coverage is in their home teams\' records: point to ../../<home>/DEEP-READING.md for them, never to this team\'s. The bullet on how the fault lines are grounded also names each guest whose folder has no paper cards (its sides rest on its research notes or SKILL.md).' : ''}
6. Resolve every [TODO: …] in the roundtable SKILL.md that names team-integrate.js or T3.8 (the fault lines, "Papers behind the documented disagreements", the Honest Boundary bullets on coverage and on how the fault lines are grounded, the research date). Afterwards grep -n -e '\\[TODO' -e '{{' ${TEAM}/<roundtable>/SKILL.md must print nothing.
Keep the roundtable protocol, checkpoints and controls unchanged, and keep it concise. Members not ready keep their current text.${G ? ' So do guests not ready, except that a "(card evidence pending…)" mark on a guest\'s side is removed (item 3).' : ''} Do not run quality_check.py on the roundtable (see the house rules). Then run python3 ${REPO}/scripts/check_links.py ${TEAM} and return files changed and a summary.`
}

function lensPrompts(status, reports) {
  const head = `${ctx(status)}

The team docs and the roundtable were just updated (reports: ${JSON.stringify(reports)}). Pre-edit copies: ${bk('README')}, ${bk('DEEP-READING')}, ${bk('roundtable-SKILL')}. You are a READ-ONLY reviewer: do not edit files (scratch work under ${SCR}/ only). Use git -C ${REPO} diff -- ${TEAM_REL}${ROOT_README ? ' README.md' : ''}.${G ? ` Guest folders are read-only: git -C ${REPO} status --porcelain -- ${GUESTS.map(g => g.dir).join(' ')} must print nothing; any output (a change in a guest's folder) is a blocker.` : ''}`
  return [
    { key: 'numbers-links', prompt: `${head}
LENS: numbers, links, commands.
1. Every coverage number in the changed files matches python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage (rerun it; compare cell by cell), and the README's five-column summary equals the --coverage --short output line for line.${G ? ' Guests are not in these tables (one dated pointer line each to ../<home>/DEEP-READING.md); a guest\'s number copied into this team\'s files is a finding.' : ''}
2. python3 ${REPO}/scripts/check_links.py ${TEAM}${ROOT_README ? ` ${REPO}/README.md` : ''} → 0 broken; every file path mentioned in the changed files exists.${G && status.guests_no_skill.length ? ' The README link to a guest without a SKILL.md yet (named above) is pending, or broken once its folder has research notes: that broken link is expected until its home team\'s T1 is merged here, so report it as a minor finding naming that cause, never as a blocker, and never ask to delete the row.' : ''}
3. Every command shown runs: run each script with --help (never modify product files).
4. Members not ready are not given numbers they do not have.
4b. grep -rn --include='*.md' -e '{{' -e '\\[TODO' ${TEAM}: every hit is a finding, except TODO items inside the own folder of a member that is not ready${G && status.guests_no_skill.length ? ' and the "lens: [TODO]" in the README row of a guest without a SKILL.md yet (named above)' : ''}.${ROOT_README ? `
5. ${REPO}/README.md changed only in the one row/line for ${TEAM_REL}.` : ''}` },
    { key: 'evidence', prompt: `${head}
LENS: evidence and attribution.
1. Every roundtable disagreement cites card ids that exist in the members' 07-paper-cards.md, on BOTH sides; open those cards and check they support what the roundtable says.${G ? ` A guest's ids are in its own folder's references/research/cards/*.digest.json (${GUEST_DIRS}; its 07-paper-cards.md indexes them once its home team's T3.6 has run); a guest side without cards may cite its notes or SKILL.md, which is not a finding; a fault line built on a disagreement with a guest's home teammate who is not seated here is. So is a "(card evidence pending…)" mark that names a guest, or that ends a fault line with no side from a member not ready (the mark names this team's members not ready only).` : ''}
2. Nothing in the changed files is attributed to a member that is really a coauthor's, a reviewer's, an interviewer's or a column author's.
3. The member agent brief points each member to its technique-catalog.md and 08 (and student-mode files where relevant); the roundtable protocol, checkpoints and controls are unchanged against the pre-edit copy.
4. DEEP-READING.md's pipeline description claims nothing that the evidence (works.json sources, INDEX.md, cards, scripts) does not show.` },
  ]
}

function fixPrompt(status, findings, round) {
  return `${ctx(status)}

${round === 1 ? 'Two read-only reviewers checked the integration edits.' : 'After the first fix round some gates still fail.'} Findings: ${JSON.stringify(findings)}
Your job (FIX${round > 1 ? ', round ' + round : ''}): verify each finding yourself, apply those you confirm (blockers and majors always). Do not modify the pre-edit copies.
Then run every gate and report each in gates (name, command, passed, detail):
- coverage: the Coverage table in ${TEAM}/DEEP-READING.md equals python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage, and the README's five-column summary equals its --coverage --short output
- links: python3 ${REPO}/scripts/check_links.py ${TEAM}${ROOT_README ? ` ${REPO}/README.md` : ''} → 0 broken${G && status.guests_no_skill.length ? '. A broken README link to the SKILL.md of a guest without one yet (named above) is expected until its home team\'s T1 is merged here: list it in detail and count the gate as passed; any other broken link fails it' : ''}
- fault-lines: every documented disagreement in the roundtable cites existing card ids on both sides (python: extract the ids, look them up in the members' 07-paper-cards.md)${G ? '; a guest\'s ids in its own folder\'s references/research/cards/*.digest.json (its 07-paper-cards.md indexes them once its home team\'s T3.6 has run), and a guest side without cards may cite its notes or SKILL.md, with no "(card evidence pending…)" mark on it' : ''}
- templates: grep -rn --include='*.md' -e '{{' -e '\\[TODO' ${TEAM} → no output. A member not ready may still have TODO items inside its own folder (${TEAM}/<slug>/…): list them in detail and count the gate as passed; any other hit fails it.${G && status.guests_no_skill.length ? ' The "lens: [TODO]" in the README row of a guest without a SKILL.md yet (named above) passes too: list it.' : ''}
The roundtable is never gated on quality_check.py (not a research-craft skill).
Edit only ${TEAM}/README.md, ${TEAM}/DEEP-READING.md, the roundtable SKILL.md${ROOT_README ? ` and the one ${TEAM_REL} row of ${REPO}/README.md` : ''}. Report what you changed and declined.${G ? ` Never edit anything in a guest's folder (${GUEST_DIRS}): decline a finding about a guest's own files as home-team work (to be fixed in its home team folder).` : ''}${G && status.guests_no_skill.length ? ' Decline every finding that asks to seat a guest without a SKILL.md yet (named above), to fill its README lens or to repair its README link (only merging its home team\'s branch after T1 does that), and keep its README row.' : ''}`
}

const STATUS = {
  type: 'object',
  properties: {
    coverage_md: { type: 'string' },
    coverage_short_md: { type: 'string' },
    members: { type: 'array', items: { type: 'object', properties: { slug: { type: 'string' }, stage: { type: 'string' }, has_08: { type: 'boolean' }, ...(G ? { home: { type: 'string' }, has_cards: { type: 'boolean' }, has_skill: { type: 'boolean' } } : {}) }, required: ['slug', 'stage', 'has_08'] } },
    problems: { type: 'array', items: { type: 'string' } },
  },
  required: ['coverage_md', 'coverage_short_md', 'members', 'problems'],
}
const OUT = {
  type: 'object',
  properties: { files_changed: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } },
  required: ['files_changed', 'summary', 'problems'],
}
const FINDINGS = {
  type: 'object',
  properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['blocker', 'major', 'minor'] }, file: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'problem', 'fix'] } } },
  required: ['findings'],
}
const FIX = {
  type: 'object',
  properties: {
    applied: { type: 'number' },
    declined: { type: 'array', items: { type: 'string' } },
    gates: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, command: { type: 'string' }, passed: { type: 'boolean' }, detail: { type: 'string' } }, required: ['name', 'command', 'passed', 'detail'] } },
    summary: { type: 'string' },
  },
  required: ['applied', 'declined', 'gates', 'summary'],
}

phase('Status')
const st = await A(statusPrompt(), { label: 'status:team', phase: 'Status', schema: STATUS, effort: 'low' })
if (!st) throw new Error('team-integrate: the status agent returned nothing; run python3 scripts/team_status.py <team> --coverage by hand and retry')
const argSlugs = new Set(MEMBERS.map(m => m.slug))
const statusRows = st.members.filter(r => argSlugs.has(r.slug))
// guests: their rows come from team_status.py in their home teams (one per guest, args order); kept apart from the
// members' lists, so readiness (and the coverage tables) stay this team's own
const guestRows = G ? GUESTS.map(g => st.members.find(r => r.slug === g.slug)).filter(Boolean) : []
// a guest without a SKILL.md yet (has_skill false, or team_status.py's stage says so: "T0 scaffold", "… no SKILL.md") is not
// seated: its own list, apart from the seated guests' readiness
const noSkill = r => r.has_skill === false || /T0 scaffold|no SKILL\.md/.test(String(r.stage || ''))
const seatedGuestRows = guestRows.filter(r => !noSkill(r))
const status = {
  coverage_md: st.coverage_md,
  coverage_short_md: st.coverage_short_md || '',
  ready: statusRows.filter(r => r.has_08).map(r => r.slug),
  not_ready: statusRows.filter(r => !r.has_08).map(r => ({ slug: r.slug, stage: r.stage })),
  ...(G ? {
    guests_ready: seatedGuestRows.filter(r => r.has_08).map(r => r.slug),
    guests_not_ready: seatedGuestRows.filter(r => !r.has_08).map(r => ({ slug: r.slug, stage: r.stage, home: homeOf(r.slug).home })),
    guests_no_skill: guestRows.filter(noSkill).map(r => ({ slug: r.slug, stage: r.stage, home: homeOf(r.slug).home })),
  } : {}),
}
const unseen = MEMBERS.filter(m => !st.members.some(r => r.slug === m.slug)).map(m => m.slug)
if (unseen.length) log(`members in args but not reported by team_status.py: ${unseen.join(', ')}`)
const unseenGuests = GUESTS.filter(g => !guestRows.some(r => r.slug === g.slug)).map(g => `${g.slug} (${HOME_DIR(g)})`)
if (unseenGuests.length) log(`guests in args but not reported by the status agent (team_status.py in their home teams): ${unseenGuests.join(', ')}`)
if (st.problems.length) log(`status problems: ${st.problems.join('; ')}`)
if (status.not_ready.length) log(`not ready (no 08 yet), shown as in progress: ${status.not_ready.map(r => `${r.slug} (${r.stage})`).join(', ')}`)
if (G && status.guests_not_ready.length) log(`guests not ready (no 08 in their own folders), their sides keep their current evidence: ${status.guests_not_ready.map(r => `${r.slug} (${r.stage}; ${r.home})`).join(', ')}`)
if (G && status.guests_no_skill.length) log(`guests without a SKILL.md yet, not seated here (their home team's T1 has not reached this branch; team-layer.js seats them once it is merged here): ${status.guests_no_skill.map(r => `${r.slug} (${r.stage}; ${r.home})`).join(', ')}`)
// with a guest without a SKILL.md yet, "next" asks for its home team's T1 and a T2 rerun here before this step
const noSkillNext = G && status.guests_no_skill.length ? [NO_SKILL_NEXT(status.guests_no_skill)] : []
if (!status.ready.length) {
  // a guest with paper cards (or ready) while no member here is: team_check.py already wants its side cited by card, and
  // only team-layer.js (T2) can do that now (this step integrates together with a ready member of this team)
  const guestsCarded = G ? seatedGuestRows.filter(r => r.has_08 || r.has_cards).map(r => r.slug) : []
  if (guestsCarded.length) log(`guests with paper cards in their home teams (${guestsCarded.join(', ')}): this step brings them in only together with a ready member of this team; until one is ready, team-layer.js (T2) here cites them by card`)
  log('no member has finished the synthesis; nothing to integrate')
  return {
    stage: 'T3.8 integrate',
    date: DATE,
    status,
    skipped: 'no member ready',
    next: [...(guestsCarded.length
      ? [`No member of this team has finished the synthesis (T3.6), so this step cannot bring in the paper cards of ${guestsCarded.join(', ')} yet, and team_check.py fails the roundtable until their sides cite them: rerun team-layer.js (T2) here, which cites a carded guest's side by card at either tier (${T2_CALL}).`,
        'At the deep tier, run team-synthesize.js for this team\'s members as well, then this step again: it integrates them together with the guests (a base-tier team does not run this step).']
      : ['Run team-synthesize.js first.', ...(G ? [GUEST_RERUN_EARLY] : [])]), ...noSkillNext],
  }
}

phase('Integrate')
const [docs, table] = await parallel([
  () => A(docsPrompt(status), { label: 'integrate:docs', phase: 'Integrate', schema: OUT }),
  () => A(roundtablePrompt(status), { label: 'integrate:roundtable', phase: 'Integrate', schema: OUT }),
])
if (!docs) log('docs agent returned nothing; README/DEEP-READING may be unchanged (the reviewers will see)')
if (!table) log('roundtable agent returned nothing; the roundtable may be unchanged (the reviewers will see)')

phase('Verify')
const ls = lensPrompts(status, { docs, roundtable: table })
const reviews = await parallel(ls.map(l => () => A(`${l.prompt}
Report findings with severity (blocker = wrong number, broken link, unsupported or misattributed claim; major = misleading or materially incomplete; minor = polish), the file, and a concrete fix each.`, { label: `verify:${l.key}`, phase: 'Verify', schema: FINDINGS })))
const missing = ls.filter((l, i) => !reviews[i]).map(l => l.key)
if (missing.length) log(`reviewer(s) returned nothing: ${missing.join(', ')}; those lenses were not checked`)
const findings = reviews.flatMap((r, i) => (r ? r.findings.map(f => ({ ...f, lens: ls[i].key })) : []))
log(`${findings.length} findings (${findings.filter(f => f.severity === 'blocker').length} blockers, ${findings.filter(f => f.severity === 'major').length} majors)`)

phase('Fix')
let fix = await A(fixPrompt(status, findings, 1), { label: 'fix:integration', phase: 'Fix', schema: FIX })
let failing = fix ? fix.gates.filter(g => !g.passed) : [{ name: 'fix agent', command: '-', passed: false, detail: 'fix agent returned nothing' }]
let rounds = 1
if (failing.length) {
  log(`gate(s) still failing: ${failing.map(g => g.name).join(', ')}; one more fix round`)
  const fix2 = await A(fixPrompt(status, failing.map(g => ({ severity: 'blocker', file: 'gate', problem: `${g.name} failed: ${g.detail}`, fix: `make "${g.command}" pass` })), 2), { label: 'fix2:integration', phase: 'Fix', schema: FIX })
  rounds = 2
  if (fix2) { fix = fix2; failing = fix2.gates.filter(g => !g.passed) }
  if (failing.length) log(`STILL failing after two fix rounds: ${failing.map(g => `${g.name} (${g.detail})`).join('; ')}; needs a human look`)
}

return {
  stage: 'T3.8 integrate',
  date: DATE,
  status,
  docs,
  roundtable: table,
  findings: findings.length,
  blockers: findings.filter(f => f.severity === 'blocker').length,
  lenses_missing: missing,
  fix,
  fix_rounds: rounds,
  gates_failing: failing.map(g => g.name),
  next: [
    `Delivery gate (every check of playbook §四 at once): python3 scripts/team_check.py ${TEAM_REL} → exit 0${noSkillNext.length ? ', apart from the rows that stay red on the guests without a SKILL.md yet (below)' : ''}.`,
    `Commit the team docs: bash scripts/team_commit.sh ${TEAM_REL} "docs(${TEAM_NAME}): integrate the deep reading"${ROOT_README ? ' (and README.md)' : ''}.`,
    status.not_ready.length ? `Rerun team-integrate.js after ${status.not_ready.map(r => r.slug).join(', ')} finish(es) the synthesis.` : 'All members are integrated.',
    ...(G ? [
      ...(status.guests_not_ready.length ? [`Guests not ready: ${status.guests_not_ready.map(r => `${r.slug} (${r.stage}; home team ${HOME_DIR(homeOf(r.slug))})`).join(', ')}: rerun team-integrate.js here once their home teams finish the deep reading (a base-tier home team never does: its guest's side stays on its research notes or SKILL.md, without a pending mark, and is final).`] : []),
      ...noSkillNext,
      GUEST_RERUN,
    ] : []),
  ],
}
