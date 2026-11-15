export const meta = {
  name: 'team-layer',
  description: 'T2: team layer for a nuwa research team: Roundtable Cards checked, roundtable SKILL.md and team README filled from the templates and the members\' cards (fault lines need evidence from both sides), per-member RESOURCES.md reconciled, then two read-only verifiers and a fixer',
  whenToUse: 'After team-base-skills.js (T1) has built every member skill (quality_check 12/12). Pass ALL members: the roundtable needs every card.',
  phases: [
    { title: 'Cards', detail: 'per member: check or write the Roundtable Card in SKILL.md; per guest (team.json "guests"): read-only digest; digest for the roundtable author' },
    { title: 'Resources', detail: 'per member: reconcile references/sources/RESOURCES.md with SKILL.md; private/README.md present' },
    { title: 'Roundtable', detail: 'roundtable SKILL.md from references/team-templates/roundtable-SKILL.md and the cards' },
    { title: 'README', detail: 'team README.md from references/team-templates/team-README.md' },
    { title: 'Verify', detail: 'two read-only verifiers: structure/consistency and evidence' },
    { title: 'Fix', detail: 'apply confirmed findings; links, placeholders and 12/12 gates again' },
  ],
}

// ---------------------------------------------------------------------------------------------
// Args (shared by all team workflows in scripts/workflows/):
//   args.repo     absolute path of the nuwa repo (has scripts/, references/)
//   args.team     team folder relative to repo, e.g. "product/bandit-team" (holds team.json)
//   args.scratch  absolute scratch dir for batch/chunk JSON files and backups (agents may write there)
//   args.date     "YYYY-MM-DD" (scripts cannot call Date.now())
//   args.members  array of member objects copied from team.json (slug, name, surname, living, hint, scholar,
//                 dblp, orcid, homepage, chase_hints, student_mode). Per-member steps run through pipeline();
//                 the roundtable waits for every member's card (a genuine barrier). Pass ALL members.
//   args.request  optional: the user's request in their own words; opens every agent prompt (set with make_args.mjs --request)
// Workflow-specific keys:
//   args.roundtable     optional roundtable slug (default: team.json "roundtable", read by the agents)
//   args.deep_tier      default true: deep reading (T3) is planned, so the TODO items the templates reserve for
//                       later steps (T3.1, T3.6, T3.8) stay in place; false (base tier, no deep reading planned):
//                       DEEP-READING.md becomes the template's short base-tier note, each RESOURCES.md drops its
//                       deep-tier placeholder row and marks row 1 "not harvested (base tier)", the README drops its
//                       deep-tier-only parts, the roundtable gets its base-tier wording, and no TODO may remain.
//                       Rerun on a team whose members already have paper cards (e.g. after adding a member): the
//                       card-backed fault lines and the deep-tier Honest Boundary that team-integrate.js wrote are kept.
//   args.example_team   optional team folder (relative to repo) of a finished team to imitate for shape only,
//                       e.g. "product/dfo-team"
//   args.guests         optional; make_args.mjs builds it from team.json "guests" (never write it by hand): members of
//                       other teams seated here, READ-ONLY. Each = the guest's entry in its home team's team.json
//                       verbatim plus "home" (its team folder) and "dir" (its folder, repo-relative: "<the folder that
//                       holds the teams>/<home>/<slug>", i.e. "product/<home>/<slug>" for teams under product/).
//                       A guest with a SKILL.md is a full seat: a read-only digest step (label guest:<slug>; its card
//                       is read, never written), a row in the roundtable Team table with a "Guest seat" note below it,
//                       seating rows, fault lines, and a README row. Its SKILL.md, card, notes and RESOURCES.md stay its
//                       home team's work (T1, T3, T4 and its own card step run there). Its side of a fault line cites
//                       its cards when its folder has them, else its notes, and is never marked "(card evidence
//                       pending)": that mark names this team's own members only. With a carded guest the author, the
//                       evidence verifier and the fixer also run scripts/check_citations.py <team> --roundtable
//                       (team_check.py runs it then at either tier); a guest that gets cards later is cited by card by a
//                       rerun of this step, or by team-integrate.js once a member here has finished the synthesis. On
//                       every run the guest strings (the README intro clause and install lines in both shells, the
//                       roundtable's Members line, description and disclaimer lists, Loading-the-Team and card-location
//                       sentences, the Team-table guest rows) are copied from python3 scripts/new_team.py <team.json>
//                       --guest-text, so a guest added later reaches all of them.
//                       The roundtable and README are written only when 2 seats AND at least one own member have a
//                       skill. A guest without a SKILL.md yet is not seated, as a member without a skill (its README row,
//                       intro-clause name and install lines stay as the scaffold rendered them), and "next" asks for a
//                       rerun once its home team's T1 is merged here and names the gates that stay red on it until then
//                       (team_check.py counts it as a seat: its guests, roundtable and templates rows, and check_links.py
//                       once its home folder has research notes). A guest whose digest agent returns nothing is left
//                       out of the run, with a rerun line in "next" (it is not called a guest without a skill). The
//                       README author, both verifiers and the fixer are told of both kinds, so their missing seats (and
//                       the TODO items the files keep for them, and the README link check_links.py counts as broken
//                       once the home folder of a guest without a SKILL.md has research notes) are not findings to
//                       fix here. For a team outside product/ the guests' install lines take the same path fix as
//                       the team's own copy line. Without guests every prompt is as before.
// Outputs: <team>/README.md, <team>/<roundtable>/SKILL.md, each member's Roundtable Card (only if missing or
//   incomplete) and references/sources/RESOURCES.md, private/README.md where missing; with deep_tier false also
//   <team>/DEEP-READING.md (the base-tier note). Never a file in a guest's folder.
// Gates run by the agents: scripts/check_links.py (0 broken), no "{{" left, TODOs only where a template reserves
//   them for a later step (none at all at the base tier), scripts/quality_check.py 12/12 per MEMBER, scripts/team_status.py.
//   The roundtable is not a research-craft skill and is never gated on quality_check.py; its gate is: links, every
//   seated member has a complete Roundtable Card, every fault line has evidence from both sides. Guests' cards are
//   checked read-only (a gap is home-team work); the verifiers check that no guest folder changed (git status).
// Next: commit; then the deep tier (team-harvest.js ...) or deliver the base tier.
// Launch: Workflow({scriptPath: "<repo>/scripts/workflows/team-layer.js", args: {...}}).
// Cost: 2 agents per member (card, resources) + 1 read-only agent per guest + 4-5 for the team (roundtable, README,
//   2 verifiers, and a fixer when there are findings).
// ---------------------------------------------------------------------------------------------

const ARGS = typeof args === 'string' ? JSON.parse(args) : args
function need(ok, msg) { if (!ok) throw new Error(`team-layer args: ${msg}`) }
need(ARGS && typeof ARGS === 'object', 'pass args as a JSON object')
need(typeof ARGS.repo === 'string' && /^(?:[A-Za-z]:[\\/]|\/)/.test(ARGS.repo), 'args.repo must be an absolute path')
need(typeof ARGS.team === 'string' && ARGS.team.length > 0 && !ARGS.team.startsWith('/'), 'args.team must be relative to args.repo, e.g. "product/<team>"')
need(typeof ARGS.scratch === 'string' && /^(?:[A-Za-z]:[\\/]|\/)/.test(ARGS.scratch), 'args.scratch must be an absolute path')
need(/^\d{4}-\d{2}-\d{2}$/.test(ARGS.date || ''), 'args.date must be "YYYY-MM-DD"')
need(Array.isArray(ARGS.members) && ARGS.members.length > 0, 'args.members must be a non-empty array copied from team.json')
ARGS.members.forEach((m, i) => need(m && /^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') && m.name, `args.members[${i}] needs a kebab-case slug and a name`))
need(ARGS.roundtable === undefined || /^[a-z0-9][a-z0-9-]*$/.test(ARGS.roundtable), 'args.roundtable must be a kebab-case slug')
// args.guests (optional, built by make_args.mjs; null counts as absent): a guest's folder sits beside this team's,
// <parent of args.team>/<home>/<slug>
need(ARGS.guests === undefined || ARGS.guests === null || Array.isArray(ARGS.guests), 'args.guests must be an array (make_args.mjs builds it from team.json "guests")')
// the team folder as a normalized POSIX path, as make_args.mjs normalizes it (path.posix.normalize) for the guests' "dir":
// "product//x", "product/x/.", "product\x" and "product/../product/x" are all "product/x"; a ".." leaving the repo stays
const TEAM_POSIX = ARGS.team.replace(/\\/g, '/').split('/')
  .reduce((p, s) => (s === '..' && p.length && p[p.length - 1] !== '..' ? p.slice(0, -1) : s && s !== '.' ? [...p, s] : p), []).join('/')
const TEAMS_ROOT = TEAM_POSIX.includes('/') ? TEAM_POSIX.slice(0, TEAM_POSIX.lastIndexOf('/') + 1) : ''
// a guest's folder sits beside this team's folder, inside the repo
need(!(ARGS.guests || []).length || (TEAM_POSIX && TEAM_POSIX !== '..' && !TEAM_POSIX.startsWith('../')), `args.team "${ARGS.team}" is the repo itself or outside it: a team with guests must be a folder inside args.repo, beside its guests' home teams (make_args.mjs builds the args)`)
for (const [i, g] of (ARGS.guests || []).entries()) {
  need(g && typeof g === 'object' && /^[a-z0-9][a-z0-9-]*$/.test(g.slug || '') && typeof g.name === 'string' && g.name.trim(), `args.guests[${i}] needs a kebab-case slug and a name (its entry in the home team's team.json)`)
  need(/^[a-z0-9][a-z0-9-]*$/.test(g.home || '') && g.home !== TEAM_POSIX.split('/').pop(), `args.guests[${i}] (${g.slug}) needs a kebab-case home: another team's folder`)
  need(typeof g.dir === 'string' && !g.dir.includes('..') && g.dir === `${TEAMS_ROOT}${g.home}/${g.slug}`, `args.guests[${i}] (${g.slug}): dir must be "${TEAMS_ROOT}${g.home}/${g.slug}" (repo-relative, no ".."; make_args.mjs builds it)`)
  need(!ARGS.members.some(m => m.slug === g.slug), `args.guests[${i}]: ${g.slug} is also in args.members (a person is a member of one team and a guest elsewhere)`)
  need(ARGS.guests.findIndex(x => x && x.slug === g.slug) === i, `args.guests[${i}]: ${g.slug} is listed twice`)
}
// args keys this workflow reads (all snake_case, like every team workflow); anything else is logged
const KNOWN_ARGS = ['repo', 'team', 'scratch', 'date', 'members', 'request', 'roundtable', 'deep_tier', 'example_team', 'guests']
const unknownArgs = Object.keys(ARGS).filter(k => !KNOWN_ARGS.includes(k))
if (unknownArgs.length) log(`team-layer.js ignores args key(s) it does not know (misspelt?): ${unknownArgs.join(', ')}; it reads ${KNOWN_ARGS.join(', ')}`)
// args.request (optional): the user's request in their own words. Workflow agents see only their prompt and the
// user's latest message in the launching session; when that message is a side question they may decline the step,
// so A() opens every prompt with the request.
const REQUEST = typeof ARGS.request === 'string' ? ARGS.request.replace(/\s+/g, ' ').trim() : ''
if (ARGS.request !== undefined && ARGS.request !== null && typeof ARGS.request !== 'string') log(`team-layer.js: args.request must be a string (the user's request in their own words), got ${Array.isArray(ARGS.request) ? 'array' : typeof ARGS.request}; ignored`)
const WHY = REQUEST ? `Why this agent runs: in the session that launched this workflow the user asked: "${REQUEST}". This agent is one step of that work (research-team kit, team-layer.js, stage T2). Do the step below.\n\n` : ''

const REPO = ARGS.repo.replace(/\/+$/, '')
const TEAM_REL = ARGS.team.replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const SCRATCH = ARGS.scratch.replace(/\/+$/, '')
const DATE = ARGS.date
const MEMBERS = ARGS.members
// guests (args.guests): members of other teams seated here, READ-ONLY. Every guest sentence below is conditional on
// G, so that the prompts of a team without guests stay exactly as they were.
const GUESTS = ARGS.guests || []
const G = GUESTS.length > 0
const SEATS = [...MEMBERS, ...GUESTS]   // the order of every index-aligned result list (the cards)
const IS_GUEST = new Set(GUESTS.map(g => g.slug))
// a card result is a guest's when its seat is (args.guests, SEATS order), never because an agent's answer says so
const isGuestCard = c => Boolean(c) && IS_GUEST.has(c.slug)
const GDIR = g => `${REPO}/${g.dir}`
const HOME_DIR = g => g.dir.slice(0, g.dir.lastIndexOf('/'))   // repo-relative home team folder, e.g. product/lp-team
const GUEST_DIRS = GUESTS.map(GDIR).join(', ')
const RUN_GUESTS = GUESTS.map(g => `${g.slug} (from ${g.home})`).join(', ')
const livingOf = g => ('living' in g ? `"living": ${g.living}` : '"living" not recorded (say nothing about it)')
const DEEP = ARGS.deep_tier !== false
const RT_DIR = ARGS.roundtable ? `${TEAM}/${ARGS.roundtable}` : `${TEAM}/<roundtable slug from team.json>`
const TPL = `${REPO}/references/team-templates`
const EXAMPLE = typeof ARGS.example_team === 'string' && ARGS.example_team.trim()
  ? `Worked example of a finished team (read for shape and level of detail only; never copy its field, researchers or content): ${REPO}/${ARGS.example_team.replace(/^\.\//, '').replace(/\/+$/, '')}/.`
  : ''
const LATER = 'team-harvest.js, team-read.js, team-synthesize.js, team-tighten.js, team-increment.js, team-integrate.js, T3, T3.1, T3.6, T3.8, T4'
const RUN_SLUGS = MEMBERS.map(m => m.slug).join(', ')
const TODO_RULE = DEEP
  ? `grep -n "TODO" shows only items a template reserves for a later step (${LATER})`
  : 'grep -n "TODO" shows nothing (base tier: every TODO item is resolved now, or deleted with its deep-tier-only part)'
const RT_GATE = `The roundtable is not a research-craft skill: never run scripts/quality_check.py on it (its persona-mode score, about 2/6, means nothing here). Its gate is: check_links.py 0 broken; every seated member${G ? ' and guest' : ''} has a complete Roundtable Card${G ? ' (a guest\'s card is checked read-only: a gap in it is home-team work, reported and never fixed here)' : ''}; every fault line has evidence from both sides; no "{{" and no TODO beyond what this step allows.`
const GUEST_LIST = GUESTS.map(g => `${g.name} (${g.slug}; home team ${g.home}, entry in ${REPO}/${HOME_DIR(g)}/team.json; folder ${GDIR(g)}/; ${livingOf(g)}${g.student_mode === true ? '; student mode' : ''})`).join('; ')
// the guest text exactly as the scaffold renders it (read-only; prints one JSON object): the guest-only prompts copy its
// strings instead of composing them, so a guest added later (new_team.py --add-guest) reaches every sentence at T2
const GUEST_TEXT = `python3 ${REPO}/scripts/new_team.py ${TEAM}/team.json --guest-text${TEAMS_ROOT === 'product/' ? '' : ` --root ${TEAMS_ROOT ? `${REPO}/${TEAMS_ROOT.slice(0, -1)}` : REPO}`}`
const GUEST_TEXT_KEYS = 'guests, SEATED_LIST, GUEST_CLAUSE, GUEST_INSTALL, GUEST_INSTALL_PS, GUEST_RESOLUTION, GUEST_CARDS, GUEST_SEATS_TODO, GUEST_DEEP_READING, README_GUEST_ROWS, ROUNDTABLE_GUEST_ROWS'
const GUEST_TEXT_RUN = `run ${GUEST_TEXT} (read-only: it prints one JSON object with the keys ${GUEST_TEXT_KEYS}, each the exact text the scaffold renders for this team's guests)`
const andList = xs => (xs.length < 2 ? xs.join('') : `${xs.slice(0, -1).join(', ')} and ${xs[xs.length - 1]}`)
// the team-level citations check: once a guest has paper cards in its own folder, its side is cited by card and
// team_check.py runs this check at either tier, so the roundtable author, the evidence verifier and the fixer run it too
const CITE_CMD = `python3 ${REPO}/scripts/check_citations.py ${TEAM} --roundtable`
const CITE_WHY = slugs => `team_check.py runs it at either tier because ${andList(slugs)} ${slugs.length > 1 ? 'have' : 'has'} paper cards; it checks that every [<slug> card …] citation names a card in that seat's own folder and cites a page only on a card that read the full text`
const CITE_GATE = slugs => `${CITE_CMD} → 0 problems (${CITE_WHY(slugs)})`
let GUEST_CARDED = []   // set by the card step: the seated guests whose own folders have paper cards
// set by the card step: the guests it could not seat. A guest without a SKILL.md yet (its home team's T1 has not reached
// this branch) is treated as a member without a skill: not seated, while the README row, intro-clause name and install
// lines new_team.py rendered stay. A guest whose digest agent returned nothing is not checked this run. The README
// author, both verifiers and the fixer are told, so their missing seats are not findings; each sentence appears only
// when such guests exist
let GUEST_NO_SKILL = []
let GUEST_FAILED = []
const NO_SKILL_HEAD = slugs => `Guests without a SKILL.md yet (their home team's T1 has not reached this branch): ${slugs.join(', ')}.`
const FAILED_HEAD = slugs => `Guests whose digest agent returned nothing in this run: ${slugs.join(', ')}.`
// a team outside product/: --guest-text writes the guests' install lines with product/<home>/<slug> (product\<home>\<slug>
// in PowerShell), as the template writes the team's own copy line, so they take the same path fix: the copied path becomes
// the guest's folder ("dir", <folder holding the teams>/<home>/<slug>); the rest of the line, and the comment lines, stay
const OUTSIDE_PRODUCT = G && TEAMS_ROOT !== 'product/'
const GUEST_PATHS = GUESTS.map(g => `${g.dir} and ${g.dir.replace(/\//g, '\\')}`).join('; ')
const INSTALL_FIX = `the copied path, product/<home>/<slug> in bash and product\\<home>\\<slug> in PowerShell, becomes the guest's folder (${GUEST_PATHS}), and the rest of the line stays as printed, as do the comment lines`

const HOUSE = `House rules for every agent in this workflow (nuwa research-team kit):
- Read ${TEAM}/team.json first: "team" (slug), "title", "field", "language" (of every member skill; the team layer follows it too), "roundtable" (the roundtable skill's folder slug${ARGS.roundtable ? `, here ${ARGS.roundtable}` : ''}) and the member entries (name, surname — used for lens labels such as [Surname lens] and @Surname —, living, hint, student_mode).${G ? ' Its "guests" ([{"slug", "home"}]) seat members of other teams here: each guest\'s entry (the same keys; read its hint, which may limit what may be said about the person) is in its home team\'s team.json, listed below.' : ''}
- Templates live in ${TPL}/ (team-README.md, roundtable-SKILL.md, member-RESOURCES.md, private-README.md, DEEP-READING.md). scripts/new_team.py fills their {{PLACEHOLDERS}} and leaves [TODO: …] items, each naming the step that resolves it. This workflow (team-layer.js, T2) resolves the items marked team-layer.js / T2 (and T1 items that are still open); ${DEEP ? `items reserved for later steps (${LATER}) stay as they are` : 'this team is BASE TIER (no deep reading planned), so nothing is left for later steps: items reserved for T3/T4 are resolved with the base-tier wording each template gives, or deleted with their deep-tier-only part, and no TODO item may remain'}.
- This run was given these members: ${RUN_SLUGS}. team-layer.js must be run with ALL members of team.json (the roundtable needs every card).${G ? `
- Guests seated here (members of other teams; READ-ONLY): ${GUEST_LIST}. They come with this run (make_args.mjs adds every guest of team.json); each guest with a SKILL.md is a full seat in the roundtable and the README (a guest without one is not seated, as a member without a skill).` : ''}
- ${RT_GATE}
- Evidence: every paper, tool or link you name carries a DOI, arXiv id or URL that you checked with a tool in this run; never cite from memory. What you say about a member must come from that member's own SKILL.md or research notes (references/research/), never from general knowledge of the researcher. Quotes verbatim with their source. If you did not check something, say so; never guess.${G ? ' The same holds for a guest: its own SKILL.md and research notes, in its folder above.' : ''}
- Sources: public and legitimate only; never shadow libraries or paywall circumvention.
- Privacy: never open, read, quote or copy anything under a references/sources/private/ folder except its README.md. Never send the user's email address or any other personal identifier to an external service.
- Scope: edit only the files this step names as its outputs (scratch files and backups go under ${SCRATCH}/team-layer/). Do not touch the repo's root SKILL.md, references/ or scripts/, and do not git commit or push: the session that launched this workflow commits after the stage.${G ? ` Never edit, create, move or delete anything in a guest's folder (${GUEST_DIRS}) or elsewhere in another team's folder: a guest's SKILL.md (card, Activation Rules, description), research notes, cards, RESOURCES.md and private/ belong to its home team, where every per-member step for it runs. Report a problem there as home-team work, naming the home team.` : ''}`

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A(): opts.phase and opts.label are required')
  return agent(`${WHY}${HOUSE}\n\n${prompt}`, opts)
}
const P = m => {
  const MD = `${TEAM}/${m.slug}`
  return { MD, SKILL: `${MD}/SKILL.md`, SRC: `${MD}/references/sources`, RES: `${MD}/references/research` }
}

// ---------- schemas ----------
const FINDINGS = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['blocker', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'problem', 'fix'] } },
  },
  required: ['lens', 'findings'],
}
const CARD = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    skill_exists: { type: 'boolean' },
    had_complete_card: { type: 'boolean' },
    edited: { type: 'boolean' },
    lens: { type: 'string' },
    known_for: { type: 'string' },
    leads_when: { type: 'string' },
    first_questions: { type: 'array', items: { type: 'string' } },
    default_recommendation: { type: 'string' },
    pushes_back_on: { type: 'string' },
    likely_disagreements: { type: 'array', items: { type: 'object', properties: { with: { type: 'string' }, point: { type: 'string' }, papers: { type: 'string' } }, required: ['with', 'point'] } },
    blind_spots: { type: 'string' },
    methods: { type: 'array', items: { type: 'string' } },
    workflows: { type: 'array', items: { type: 'string' } },
    taste: { type: 'array', items: { type: 'string' } },
    key_papers: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, id: { type: 'string' }, position: { type: 'string' }, where: { type: 'string' } }, required: ['title', 'id', 'position', 'where'] } },
    deep_tier_done: { type: 'boolean' },
    student_mode: { type: 'boolean' },
    quality_check: { type: 'string' },
  },
  required: ['slug', 'skill_exists', 'had_complete_card', 'edited', 'lens', 'leads_when', 'first_questions', 'likely_disagreements', 'blind_spots', 'methods', 'key_papers', 'deep_tier_done', 'student_mode', 'quality_check'],
}
// a guest's read-only digest: the member card's digest without "edited" (nothing is written in a guest's folder), plus
// the problems found in the guest's own files, which are home-team work
const GUEST_CARD = {
  type: 'object',
  properties: { ...Object.fromEntries(Object.entries(CARD.properties).filter(([k]) => k !== 'edited')), problems: { type: 'array', items: { type: 'string' } } },
  required: [...CARD.required.filter(k => k !== 'edited'), 'problems'],
}
const RES_OUT = {
  type: 'object',
  properties: {
    rows: { type: 'number' },
    added: { type: 'number' },
    verified: { type: 'number' },
    leads: { type: 'number' },
    rechecked: { type: 'number' },
    failed_recheck: { type: 'number' },
    unverifiable_cited: { type: 'array', items: { type: 'string' } },
    private_readme: { type: 'string', enum: ['existed', 'created', 'missing'] },
    summary: { type: 'string' },
  },
  required: ['rows', 'added', 'verified', 'leads', 'unverifiable_cited', 'private_readme', 'summary'],
}
const RT_OUT = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    words: { type: 'number' },
    description_chars: { type: 'number' },
    seated: { type: 'array', items: { type: 'string' } },
    fault_lines: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, sides: { type: 'string' }, kind: { type: 'string', enum: ['exchange in print', 'contrast of published methods'] }, evidence: { type: 'string' } }, required: ['title', 'sides', 'kind', 'evidence'] } },
    dropped_contrasts: { type: 'array', items: { type: 'string' } },
    seating_rows: { type: 'number' },
    shared_references: { type: 'number' },
    todos_left: { type: 'array', items: { type: 'string' } },
    links: { type: 'string' },
    card_problems: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['file', 'words', 'description_chars', 'seated', 'fault_lines', 'dropped_contrasts', 'seating_rows', 'todos_left', 'links', 'card_problems', 'summary'],
}
const README_OUT = {
  type: 'object',
  properties: { file: { type: 'string' }, words: { type: 'number' }, todos_left: { type: 'array', items: { type: 'string' } }, links: { type: 'string' }, team_status: { type: 'string' }, summary: { type: 'string' } },
  required: ['file', 'todos_left', 'links', 'team_status', 'summary'],
}
const FIX = {
  type: 'object',
  properties: {
    applied: { type: 'number' },
    declined: { type: 'array', items: { type: 'string' } },
    files_changed: { type: 'array', items: { type: 'string' } },
    check_links: { type: 'string' },
    placeholders_left: { type: 'number' },
    quality_checks: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['applied', 'declined', 'files_changed', 'check_links', 'placeholders_left', 'quality_checks', 'summary'],
}
// the fixer's report beside guests without a SKILL.md yet (G only): check_links.py counts their README links as broken
// once their home folders have research notes, which only a merge of their home team's T1 fixes, so the fixer also
// returns the number of the other broken links, which alone decide its links gate
const FIX_NO_SKILL = {
  ...FIX,
  properties: { ...FIX.properties, broken_other: { type: 'number' } },
  required: [...FIX.required, 'broken_other'],
}

// ---------- prompts ----------
const DIGEST_ASK = 'Also return, for the roundtable author: the core method names (the ### headings under the core-methods section), the stage-workflow names, the top 3 taste criteria, what the skill says the member is known for (signature works, software, books; one line, from the skill), the papers behind the member\'s most distinctive positions (title, DOI/arXiv id, the position it supports, and where in the skill or notes it is used), whether deep-reading files exist (references/technique-catalog.md or references/research/07-paper-cards.md), and whether the skill has a Student Mode.'

function cardPrompt(m) {
  const { MD, SKILL, RES } = P(m)
  return `Task (T2 team layer, step 1: Roundtable Card) for ${m.name} (${MD}/).
Read ${SKILL}. If it does not exist, edit nothing and return skill_exists = false (fill the other fields with empty values).
The card is the "## Roundtable Card" section with seven bullets: **Lens (one line)**, **Leads when**, **First questions asked**, **Default recommendation**, **Will push back on**, **Likely disagreements** (per other member), **Blind spots**. The roundtable moderator reads only this section, so it must be complete and short (under about 350 words).
- Complete card: edit nothing; return its content.
- Missing or incomplete card: write it from the skill's own sections (Research Taste, Core Research Methods, Stage Workflows, Research Anti-patterns, Honest Boundary, and the research notes in ${RES}/ they cite). Nothing new: every bullet must trace to the same skill. Likely disagreements: one per OTHER member listed in team.json, inferred from the methods on both sides, labelled "inferred", naming the paper(s) with identifiers each side rests on where this member's files give them, and "no dispute documented" unless one is. Put the card just before the Honest Boundary. If Activation Rules lack it, add one line: "When convened by <roundtable slug>, answer from the Roundtable Card first and keep it short." Then run python3 ${REPO}/scripts/quality_check.py ${SKILL}: it must still report 12/12 (report the result line either way).
${DIGEST_ASK}
Files you may edit: ${SKILL} — the Roundtable Card and that one Activation Rules line only.`
}

// a guest (args.guests): READ-ONLY. Its card was written by its home team (team-layer.js there); here it is only read.
function guestPrompt(g) {
  const MD = GDIR(g)
  const HOME = HOME_DIR(g)
  return `Task (T2 team layer, step 1 for a guest: read-only digest) for ${g.name} (${MD}/), a member of the team in ${REPO}/${HOME}/ who is seated in this team as a guest.
READ-ONLY: edit, create, move or delete nothing in that folder or anywhere else. Its SKILL.md, Roundtable Card, research notes and RESOURCES.md are its home team's work.
Read ${MD}/SKILL.md. If it does not exist, return skill_exists = false (fill the other fields with empty values) and problems = ["no SKILL.md yet: the home team's T1 (team-base-skills.js in ${HOME}) builds it; merge that branch here, then rerun team-layer.js"].
The card is the "## Roundtable Card" section with seven bullets: **Lens (one line)**, **Leads when**, **First questions asked**, **Default recommendation**, **Will push back on**, **Likely disagreements**, **Blind spots**. Read it, the Core Research Methods and the Research Taste, and the research notes in ${MD}/references/research/ that they cite; return the card's content as written (had_complete_card = all seven bullets are there and filled). Never write, complete or correct it here: it was written by and for the home team, so its Leads when speaks of that team's field and its Likely disagreements name that team's members (keep each "with" as written; the roundtable author decides what applies to this team).
Run python3 ${REPO}/scripts/quality_check.py ${MD}/SKILL.md (it only reads) and return its result line.
${DIGEST_ASK} For a guest, deep_tier_done is also true when ${MD}/references/research/cards/ holds paper cards (*.digest.json files): team_check.py then wants its side of a fault line cited by card.
problems: every gap you find in the guest's own files (an incomplete card, a quality_check result below 12/12, a note or paper the skill cites that is not there, …), each written as home-team work: "<what is wrong> — fix in ${HOME} (team-layer.js or team-base-skills.js there), then rerun team-layer.js here". Empty when there is none.
Files you may edit: none.`
}

function resourcesPrompt(m) {
  const { MD, SKILL, SRC, RES } = P(m)
  return `Task (T2 team layer: resource tracker) for ${m.name}. File: ${SRC}/RESOURCES.md.
team-base-skills.js (T1) filled it from the research notes; SKILL.md may cite sources the tracker lacks.
1. If the file is missing, create it from ${TPL}/member-RESOURCES.md (replace {{MEMBER_NAME}}, {{MEMBER_SLUG}}, {{SCHOLAR_URL}}). If T1 items are still TODO, fill them as the template says: one row per source in ${RES}/01-06, each verified.
2. Every paper, book, software, talk or page cited in ${SKILL} (and in references/proof-playbook.md, open-problems.md, reading-path.md, technique-catalog.md if they exist) has a row. Add the missing ones, verified with a tool in this run: DOI -> curl -s -o /dev/null -w "%{http_code}" https://doi.org/<doi> gives 30x and the Crossref title matches; arXiv -> the abs page title matches; other -> the page exists and says what the row says. Add "SKILL" (with the section) to "Used in" where SKILL.md cites the source.
3. Re-check 10 ✅ rows chosen across the table (all if fewer); a failing row becomes ⚠️ with the reason in Notes; if more than 2 fail, re-check every ✅ row.
4. A source SKILL.md cites that you cannot verify: mark it ⚠️ and list it in unverifiable_cited (the fixer decides whether the skill may keep citing it).
${DEEP
    ? '5. Deep tier planned: leave the TODO items reserved for later steps (row 1, the publication list, for team-harvest.js; the deep-tier placeholder row for team-synthesize.js) exactly as they are. No "{{" may remain.'
    : '5. Base tier (no deep reading planned): row 1 (the publication list) keeps Status ⚠️; its Link cell becomes "—" if it still holds a TODO item or the scaffold\'s "— (no Scholar profile in team.json; list from DBLP/homepage)" text (a real profile URL stays); its Notes become "not harvested (base tier)". Delete the deep-tier placeholder row (the one whose Title cell starts "[TODO: placeholder for the deep-tier rows") and keep the # column consecutive. Afterwards grep -n -e "TODO" -e "{{" on the file prints nothing except the TODO mentions inside the HTML comment at the top.'}
6. Make sure ${SRC}/private/README.md exists; if missing, create it from ${TPL}/private-README.md (replace {{MEMBER_NAME}} and {{MEMBER_SLUG}}). Never open anything else in private/.
Edit only ${SRC}/RESOURCES.md and (create only) ${SRC}/private/README.md. Return the counts.`
}

function roundtablePrompt(cards, missing, deepDone, guestMissing = [], guestCarded = [], guestFailed = []) {
  // guest text (G only): the guest strings, seated guests, guests without a skill or without a digest, carded guests
  const RT_NAME = ARGS.roundtable || '<the roundtable slug from team.json>'
  const gPlaceholders = G ? `${EXAMPLE ? ' ' : ''}This team seats guests. On every run, whether the file exists or not, ${GUEST_TEXT_RUN}; if it exits 1, add its error lines to card_problems and change no guest text. Make each guest string present and current in the file (a guest added after the scaffold, with new_team.py --add-guest, is missing from all of them until this step): the frontmatter description ("Runs the research-craft skills of … as separate agents") and the first-activation disclaimer ("distilled from the public work of … — not their actual opinions") name the researchers as SEATED_LIST; the line "Members: <member names>." ends with GUEST_CLAUSE before its final period; Loading the Team item 1 ends with GUEST_RESOLUTION; the card-location sentence of the fault lines (the one explaining [<member-slug> card S012 pp. 3–4]) ends with GUEST_CARDS; the Team table has, after the member rows, the ROUNDTABLE_GUEST_ROWS entry of each seated guest (the digests marked "guest": true), keeping its first two cells (its lens cell is item 2's). Copy the strings exactly; never compose guest text yourself. When you copy the template, they are the values of {{SEATED_LIST}}, {{GUEST_CLAUSE}}, {{GUEST_RESOLUTION}} and {{GUEST_CARDS}}, ROUNDTABLE_GUEST_ROWS are the guest rows of {{ROUNDTABLE_MEMBER_TABLE}}, and {{GUEST_SEATS_TODO}} becomes the Guest seat notes of item 2.` : ''
  const gSeated = G ? `Seated guests (members of other teams, READ-ONLY) are the digests marked "guest": true, with their home team and folder ("dir", under ${REPO}/); their cards were written by their home teams, for that team's field and members.
${guestMissing.length ? `Guests listed but without a skill yet (leave them out of every table; say so in the Honest Boundary; their home team's T1 builds the skill): ${guestMissing.join(', ')}.\n` : ''}${guestFailed.length ? `Guests whose digest agent returned nothing in this run: ${guestFailed.join(', ')}. Their skills were not read this time, which says nothing about whether they exist: never write that these guests have no skill. Leave them out of what this run adds (no new rows, seating or fault lines for them), keep what the file already has for them, and do not mention them in the Honest Boundary; team-layer.js runs again for them.\n` : ''}` : ''
  const gCarded = G && guestCarded.length ? `Guests whose own folders have paper cards (their home teams did the deep reading): ${guestCarded.join(', ')}. Their side of a fault line is cited by card (item 5).\n` : ''
  // a carded guest makes the members-only base-tier / pre-T3 sentences of items 9 and 10 false for its sides: qualify them
  const carded = guestCarded.map(s => GUESTS.find(g => g.slug === s)).filter(Boolean)
  const cardedHomes = [...new Set(carded.map(g => g.home))]
  const cardedWhere = carded.length ? `${cardedHomes.length > 1 ? 'their home teams' : `the home team ${cardedHomes[0]}`} (${cardedHomes.map(h => `../../${h}/DEEP-READING.md`).join(', ')})` : ''
  return `Task (T2 team layer: the roundtable skill). Output: ${RT_DIR}/SKILL.md.
Start from that file if scripts/new_team.py created it (${TPL}/roundtable-SKILL.md with the {{…}} placeholders filled and [TODO: …] items open). If it does not exist, copy the template and replace every placeholder yourself — {{ROUNDTABLE_SLUG}}, {{TEAM_TITLE}}, {{FIELD}}, {{MEMBER_LIST}} (comma-separated member names), {{ROUNDTABLE_MEMBER_TABLE}} (the Team table rows, item 2 below), {{DATE}} = ${DATE} — so that no "{{" remains. ${EXAMPLE}${gPlaceholders}
If the file is already filled (a rerun, e.g. after a member was added), update it in place: add the new member(s) to every table, seating row and fault line the evidence supports, and keep everything else.
Seated members (each has a SKILL.md with a Roundtable Card); digests from their cards: ${JSON.stringify(cards)}
${gSeated}${missing.length ? `Members listed but without a skill yet (leave them out of every table; say so in the Honest Boundary): ${missing.join(', ')}.\n` : ''}Members in this run: ${RUN_SLUGS}. Compare with the "members" of team.json: for a member of team.json that is NOT in this run, do not delete its existing rows, seating or fault lines, and add "NOT-IN-RUN <slug>" to card_problems (team-layer.js must be run with all members).${G ? ` Guests in this run: ${RUN_GUESTS}; compare them with the "guests" of team.json the same way ("NOT-IN-RUN <slug>" for a guest of team.json that is not in this run).` : ''}
Read each seated member's Roundtable Card, Core Research Methods and Research Taste yourself (${TEAM}/<slug>/SKILL.md) before writing; the digests are a map, not the evidence.${G ? ` A guest's are in its own folder (${REPO}/<dir>/SKILL.md), never under ${TEAM}/.` : ''}
${deepDone.length ? `Deep reading already done for: ${deepDone.join(', ')} (their paper cards and 07-09 exist), so this is a rerun on a deep-tier team. Do NOT downgrade what team-integrate.js (T3.8) wrote: keep the card-backed fault lines with their card evidence, "Papers behind the documented disagreements" and the deep-tier Honest Boundary bullets (coverage in ../DEEP-READING.md; fault lines resting on paper cards) and its research-date line. Only add what the new or changed members need; a fault line side that rests on a member without paper cards ends with "(card evidence pending for <slug>)".${G ? ' That mark names this team\'s own members only, never a guest (item 5).' : ''} Say in summary what you kept.\n` : ''}${gCarded}
Keep every part of the template: it is what makes the roundtable work.
 (a) "How the Roundtable Runs": each seated member runs as its own agent (Agent/Task tool, all seated members launched in one message, agents reused across rounds when the runtime can continue them); the model reading the skill is the moderator and never argues a member's position; the user chairs and the discussion pauses at every 🔵 checkpoint; the single-model fallback is announced; the cost line.
 (b) Activation Rules, Research Integrity Rules (with the private/ rule), Your Controls, Loading the Team (absolute paths; the moderator reads only the Roundtable Cards; a missing member is named, never improvised).${G ? ' Loading the Team resolves a guest\'s folder at ../../<home>/<slug>/ in this repository first (the template\'s guest sentence), then at the installed paths, and uses that folder for its SKILL.md, cards and notes; a missing guest is named with its home team.' : ''}
 (c) The Member Agent Brief block (its single-brace fields stay for the moderator to fill at run time).${G ? ' Add one line after the block: a guest\'s brief ends with the delegate note of its Guest seat note.' : ''}
 (d) Protocol Steps 0-5 with the four 🔵 checkpoints; Checkpoint 4 is never skipped, even in autopilot; Step 5 verifies every name, paper and link and offers to save the transcript only if the user says yes.
 (e) Output Template, Outside the Team, Shared References, Papers behind the documented disagreements, Honest Boundary, the attribution footer.

Resolve the TODO items marked team-layer.js (T2):
1. Frontmatter description: the kind of problem the team takes (from the members' "Leads when"), the parts a plan in this field must name (from their "Default recommendation"), one "Not for …" sentence; the whole description under 1024 characters (count them).
2. Team table: one row per seated member — the slug in backticks, full name, the lens in one line condensed from its card.${G ? ` Then one row per seated guest, after the member rows, in the scaffold's form: | \`<slug>\` | <Name> (guest from <home title>) | <its lens in one line for THIS team's field, from its card> | (<home title> = "title" in its home team.json). Under the table, replace the scaffold's Guest-seat TODO (at the end of the line below the table) with one note per seated guest, headed **Guest seat · <Name> (guest from <home title>)**: leads when (the problem signals in THIS team's field where its methods lead, from its own files; its card's "Leads when" speaks of its home team's field); likely disagreements with this team's seats, each with evidence from both sides' own files; and the delegate note for its brief: "You are seated as a guest in ${RT_NAME}, not your home roundtable: skip your disclaimer; answer from your Roundtable Card in the fields the brief asks for." Its card stays authoritative for its lens, default recommendation, push-backs and blind spots; for seating and disagreements here the note, the seating table and the fault lines take precedence. Write guest paths in this file as ../../<home>/<slug>/….` : ''}
3. Problem Card: keep the six generic fields; add 3-6 field-specific fields merged from the members' "First questions asked" (deduplicated), each with "why it matters" naming the lens or seating choice it feeds.${G ? ' A guest\'s first questions count only where they fit this team\'s field.' : ''}
4. Seating table: 8-14 rows "problem signal -> 2 leads -> 1 challenger" built from the members' "Leads when" and "Blind spots"; every seated member leads at least one row; a row where no other lens has evidence gets "— (outside the other lenses' evidence)".${G ? ' Seat every seated guest (as a lead or the challenger) in at least one row, from its Guest seat note.' : ''}
5. Documented fault lines (3-6) — the heart of this step:
   - Candidates: the members' "Likely disagreements", plus contrasts you see between their core methods and taste.
   - Keep a fault line only with evidence from BOTH sides: for each side, a passage in that member's SKILL.md or research notes (references/research/01-06; paper cards and 07-09 if they exist) that rests on a verifiable paper (DOI or arXiv id; page or section when a full text was read). Open those files and check the passage says it. Cite as [<member-slug> <file> §<section>; <DOI or arXiv id>] — or, once paper cards exist, [<member-slug> card <id> p. N].
   - Say whether it is an exchange in print between members (only when you found papers on both sides answering each other) or a contrast of published methods (the usual case). Never invent a debate or a quote.
   - Name what is still contested and the observation or experiment that would settle it.
${DEEP
    ? '   - While the members have no paper cards, end each fault line with "(card evidence pending)"; team-integrate.js (T3.8) rewrites them from the cards later.'
    : G
      ? '   - Base tier: this team\'s members get no paper cards, so cite their research notes and papers as above and do not add "(card evidence pending)".'
      : '   - Base tier: there will be no paper cards, so cite the research notes and papers as above and do not add "(card evidence pending)".'}
   - One-sided or unsupported contrasts are not fault lines: drop them and list them in dropped_contrasts with the missing side.${G ? `
   - Guests are full seats in fault lines. A guest's side is cited from its own folder: its research notes or SKILL.md as above, or [<guest-slug> card <id>] when that folder has paper cards, adding p. N only when that card's read_level (in the guest's references/research/cards/*.digest.json) is full or partial: check_citations.py rejects a page cited on an abstract-, metadata- or unreadable-level card. Card ids are per seat, from that seat's own references/research/cards/*.digest.json (indexed in its 07-paper-cards.md once its home team's T3.6 has run); such a side is cited by card ${DEEP ? 'now' : 'even at the base tier'}.${DEEP ? ' The pending mark of the bullet above is about this team\'s own members only: write it "(card evidence pending for <slug>)", naming the own members whose side has no paper cards, and leave it off a fault line with no such side. Never mark a guest\'s side pending: without cards it rests on its research notes or SKILL.md, which stand until its home team does the deep reading (a base-tier home team never does); once it has cards, its side is cited by card here: by team-integrate.js (T3.8) when a member of this team has finished the synthesis, before that by a rerun of this step.' : ''} A guest's card names its home teammates: a disagreement with a home teammate who is not seated here never becomes a fault line here. Put every seated guest in at least one fault line with evidence from both sides; when no such contrast exists for a guest, add "NO-FAULT-LINE <slug>: <why>" to card_problems instead of inventing one.` : ''}
6. Draft-plan items: the settings a plan in this field must always state, 2-3 switch signals, and the field's standard comparison protocol (verified, with its reference in Shared References).
7. Outside the Team: 2-4 bullets "problem signal -> the neighbouring tradition, method or tool that fits better", from team.json "field" and the members' blind spots; say whether any member partly covers it; every tool or paper named verified.
8. Shared References (verified <month year>): 3-8 field-wide references (the standard for comparing methods, a taxonomy of problem types, a survey, key open-source software), each a full reference with DOI or URL checked in this run, ending with one line on why it is here.
9. Papers behind the documented disagreements: ${!DEEP
    ? (carded.length
      ? 'base tier, worded for this team\'s members only because some guests\' sides rest on paper cards: write "No deep reading was done for this team\'s members (base tier); their sides of the fault lines rest on their research notes."'
      : 'base tier: write "No deep reading was done (base tier); the fault lines rest on the members\' research notes."')
    : deepDone.length ? 'keep the card-based list team-integrate.js wrote; add papers of new fault lines only where cards exist.'
      : carded.length ? 'while this team\'s members have no paper cards, write "Pending the deep reading (T3) for this team\'s members."' : 'while there are no paper cards, write "Pending the deep reading (T3)."'}${G && guestCarded.length ? ` For the card-cited sides of guests (${guestCarded.join(', ')}), also list the papers their cited cards read (full reference, DOI or arXiv link, the FL numbers, [<guest-slug> card <id>]); those cards were read in ${cardedWhere}.` : ''}
10. Honest Boundary: ${deepDone.length
    ? 'keep the deep-tier bullets on coverage and on how the fault lines are grounded (see above); add a note for members without paper cards yet;'
    : carded.length
      ? `the ${DEEP ? 'pre-T3' : 'base-tier (final)'} wording from the template, worded for this team's members only because some guests' sides rest on paper cards — "This team's members rest on web research only (research notes 01–06); no full text has been read for them yet." and "Fault lines are drawn from the Roundtable Cards and research notes; the members' sides have not been checked against full texts, and the card-cited sides of ${andList(carded.map(g => g.name))} rest on paper cards read in ${cardedWhere}.";`
      : `the ${DEEP ? 'pre-T3' : 'base-tier (final)'} wording from the template — "The members rest on web research only (research notes 01–06); no full text has been read yet." and "Fault lines are drawn from the members' Roundtable Cards and research notes and have not been checked against full texts.";`} historical-lens bullets for members with "living": false; the traditions outside the team (matching Outside the Team); research date ${DATE}.${G ? ` Guests: a historical-lens bullet only for a guest whose home entry has "living": false (no living wording when the key is absent); one bullet naming the guests, their home teams, and that their skills, cards and coverage are kept there (coverage: ../../<home>/DEEP-READING.md)${deepDone.length ? '; the bullet on how the fault lines are grounded also names each guest whose folder has no paper cards (its sides rest on its research notes or SKILL.md)' : ''}; the research date line also names the state of the guests' files you read (git -C ${REPO} log -1 --format='%h %ad' --date=short -- <guest folder>).` : ''}
Do not edit any other file (not the members' SKILL.md: report a wrong or thin card in card_problems instead).${G ? ' Never edit anything in a guest\'s folder: a gap in a guest\'s card or skill goes into card_problems as home-team work, written "HOME <home> <slug>: <what> — fix in <its home team folder>".' : ''}
Keep it concise (about 4,000 words at most).
Gates: python3 ${REPO}/scripts/check_links.py ${RT_DIR} (0 broken); grep -n "{{" (none); ${TODO_RULE}${G && guestCarded.length ? `; ${CITE_GATE(guestCarded)}` : ''}. Never run quality_check.py on the roundtable (see the house rules). Return the structured summary.`
}

function readmePrompt(cards, rt, deepDone, guestNoSkill = [], guestFailed = []) {
  // guest text (G only): the guest strings, the guest rows, install lines, coverage pointers
  const gPlaceholders = G ? `${EXAMPLE ? ' ' : ''}This team seats guests. On every run, whether the README exists or not, ${GUEST_TEXT_RUN}; if it exits 1, put its error lines in summary and change no guest text. Make each guest string present and current in the README (a guest added after the scaffold, with new_team.py --add-guest, has only its table row until this step): the intro sentence ("Research-craft skills distilled from the public work of <member names>…, plus a roundtable skill …") has GUEST_CLAUSE right after the member names; the team table has, after the member rows, one row per README_GUEST_ROWS entry (filled as below); the Install blocks carry the GUEST_INSTALL and GUEST_INSTALL_PS lines (as below). Copy the strings exactly${OUTSIDE_PRODUCT ? ' (the install lines with the path fix of the Install item below)' : ''}; never compose guest text yourself. When you copy the template, they are the values of {{GUEST_CLAUSE}}, {{GUEST_INSTALL}} and {{GUEST_INSTALL_PS}}, and README_GUEST_ROWS are the guest rows of {{MEMBER_TABLE}}.` : ''
  // guests the card step could not seat (G only): kept as the scaffold rendered them, never described as seated
  const gNotSeated = (G && guestNoSkill.length ? `${NO_SKILL_HEAD(guestNoSkill)} They are not seated in the roundtable this run, so the README never describes them as seated (not in the scope sentence, the Use examples or any line on who sits at the roundtable). It keeps what new_team.py rendered for them, as for a member without a skill: their README_GUEST_ROWS row exactly as --guest-text prints it, its "lens: [TODO]" and stage "T0 scaffold" included (there is no SKILL.md to take a lens from: report that TODO with the gates instead of filling it), their names in GUEST_CLAUSE, and their GUEST_INSTALL and GUEST_INSTALL_PS lines. Their row's link stays: check_links.py counts it pending while their home folder has no research notes, and broken once it has notes but no SKILL.md (report that; never delete the row). team-layer.js runs again here once their home team's T1 is merged.\n` : '')
    + (G && guestFailed.length ? `${FAILED_HEAD(guestFailed)} Their skills were not read this time, which says nothing about whether they exist: keep the row the README has for them (their README_GUEST_ROWS row only when it has none), and their intro-clause names and install lines as --guest-text prints them; fill nothing new for them (their lens cell waits for the rerun), and never write that they have no skill; team-layer.js runs again for them.\n` : '')
  // carded guests (their home teams did the deep reading): the README's base-tier "without full-text reading" covers members only
  const carded = cards.filter(c => isGuestCard(c) && c.deep_tier_done)
  const cardedHomes = [...new Set(carded.map(c => c.home))]
  return `Task (T2 team layer: the team README). Output: ${TEAM}/README.md.
Start from the README scripts/new_team.py created (${TPL}/team-README.md with placeholders filled and [TODO: …] items open) or, if there is none, from the template itself: replace every placeholder — {{TEAM_TITLE}}, {{TEAM_SLUG}} (team.json "team"), {{FIELD}}, {{MEMBER_LIST}}, {{ROUNDTABLE_SLUG}}, {{MEMBER_TABLE}} (one row per member: | [Name](<slug>/SKILL.md) | lens · known for | status |) — so that no "{{" remains. ${EXAMPLE}${gPlaceholders}
The roundtable skill was just written: ${rt ? `${rt.file} (seated: ${rt.seated.join(', ')})` : `${RT_DIR}/SKILL.md (its author returned no report; read the file)`}. Member digests: ${JSON.stringify(cards.map(c => ({ slug: c.slug, lens: c.lens, known_for: c.known_for, student_mode: c.student_mode, deep_tier_done: c.deep_tier_done, ...(isGuestCard(c) ? { guest: true, home: c.home, dir: c.dir } : {}) })))}
${gNotSeated}Resolve the TODO items marked team-layer.js (T2):
- The scope sentence (which tradition of the field this selection follows; which neighbouring traditions are not represented), consistent with the roundtable's "Outside the Team".
- The team table: each member's one-line lens and what it is known for, taken from that member's SKILL.md (not from memory); the status cell from python3 ${REPO}/scripts/team_status.py ${TEAM}; mark student-mode members; then delete the instruction line.${G ? ` Guests (the digests marked "guest": true): one row each after the member rows, its README_GUEST_ROWS entry (the scaffold's form | [<Name>](../<home>/<slug>/SKILL.md) | lens: [TODO] | guest from [<home title>](../<home>/README.md) · <stage> |) with the link cell and the "guest from [<home title>](../<home>/README.md)" part kept, "lens: [TODO]" replaced by its lens restated for this team's field · what it is known for (from its own SKILL.md), and the stage taken from the Guests section of the same team_status.py output (one line per guest: slug · home · its stage in its home team); student mode as for members.` : ''}
- Use: a realistic two-line problem from the field, with the budget, constraints and failure modes a member would ask about; the single-lens examples with real surnames and typical artefacts of the field. The checkpoint and control tables must match the roundtable skill's (read it).
- Install: the snippets must use the team's real path, ${TEAM_REL} (fix the template's product/<slug> path if the team lives elsewhere).${G ? ` The roundtable also needs each guest's folder (${GUESTS.map(g => g.dir).join(', ')}), installed from the same checkout: right after the team's own copy line, the bash block carries the GUEST_INSTALL lines and the PowerShell block the GUEST_INSTALL_PS lines, verbatim${OUTSIDE_PRODUCT ? ' apart from the path fix below' : ''} and once each (per home team one comment line of its own, "# guest(s) from the <home title>: if this checkout holds git-ignored full texts, copy only git-tracked files, see product/README.md", then one copy line per guest with no comment after it, so that the bash block also runs when pasted into zsh, where # starts no comment by default); say in the sentence above the snippets that the guests' folders are installed with the team.${OUTSIDE_PRODUCT ? ` This team is not under product/, and --guest-text writes those lines with product/, as the template writes the team's own copy line, so they take the same path fix: in each guest line ${INSTALL_FIX}.` : ''}` : ''}
- Honest Boundary for the base tier: "The research was done from web search results in <month year>, without full-text reading; each skill's Honest Boundary lists its gaps and RESOURCES.md marks unverified leads ⚠️." (unless team_status.py shows deep-reading output), plus a historical-lens bullet for each member with "living": false (with the year of death from its skill).${G ? ' For a guest: a historical-lens bullet only when its home entry has "living": false (no living wording when the key is absent), and one line saying that the guests\' skills, cards and deep reading are kept by their home teams.' : ''}${carded.length && !deepDone.length ? ` That sentence's "without full-text reading" covers this team's members only: say so, and that the card-cited sides of ${andList(carded.map(c => GUESTS.find(g => g.slug === c.slug).name))} rest on paper cards read in ${cardedHomes.length > 1 ? 'their home teams' : `the home team ${cardedHomes[0]}`} (${cardedHomes.map(h => `../${h}/DEEP-READING.md`).join(', ')}).` : ''}
${DEEP
    ? (deepDone.length
      ? '- Deep reading already done for some members: if team-integrate.js (T3.8) has filled the technique-catalogs paragraph and the coverage summary, keep them as they are (the next team-integrate.js run refreshes them); a new member without cards is shown "in progress".'
      : '- Deep tier planned: leave the TODO items reserved for team-integrate.js (T3.8) — the technique-catalogs paragraph and the coverage table — in place; they are the open-work list for the deep tier.')
    : `- No deep reading is planned (args.deep_tier is false): delete the technique-catalogs paragraph, the coverage table and their TODO lines, and say in the Resources section that the deep-reading files are absent. Also replace ${TEAM}/DEEP-READING.md, entirely, with the base-tier note given in the header comment of ${TPL}/DEEP-READING.md (a heading and one paragraph; fill {{TEAM_TITLE}} from team.json "title" and {{MEMBER_LIST}} with the member names, comma-separated), so the links to it keep working and no TODO item is left.`}${G ? ` The coverage of this team's files covers its own members only: guests are read by their home teams (../<home>/DEEP-READING.md)${DEEP ? '' : '; end the base-tier note\'s paragraph with the GUEST_DEEP_READING string from --guest-text (it starts with a space: " Guests are read by their home teams: …"), as the --base-tier scaffold does'}, and a guest's numbers are never copied here.` : ''}
Members in this run: ${RUN_SLUGS}; never delete the row of a team.json member that is not in this run.${G ? ` Guests in this run: ${RUN_GUESTS}; never delete the row of a team.json guest that is not in this run either.` : ''}
Keep the Resources tree and its explanation.
Gates: python3 ${REPO}/scripts/check_links.py ${TEAM} (0 broken); grep -n "{{" (none); ${TODO_RULE}.
Edit only ${TEAM}/README.md${DEEP ? '' : ` and ${TEAM}/DEEP-READING.md`}. Return the structured summary.${G ? ' Never edit anything in a guest\'s folder.' : ''}`
}

const LENSES = [
  {
    key: 'structure',
    prompt: () => `READ-ONLY verifier: structure and consistency of the team layer in ${TEAM}. Edit nothing.
1. python3 ${REPO}/scripts/check_links.py ${TEAM}: report every broken link.${G && GUEST_NO_SKILL.length ? ' The README link of a guest without a SKILL.md yet is reported as item 3b says.' : ''}
2. grep -rn "{{" ${TEAM} --include=*.md: every hit is a finding. grep -n "TODO" in README.md, DEEP-READING.md, the roundtable SKILL.md and each member's references/sources/RESOURCES.md (TODO mentions inside a template's top HTML comment do not count): ${DEEP
    ? `every TODO left must be one a template reserves for a later step (${LATER}; all of DEEP-READING.md's are reserved for team-integrate.js); any other TODO is a finding.`
    : 'this team is base tier, so every TODO item is a finding: DEEP-READING.md must be the short base-tier note from the template header, each RESOURCES.md has row 1 marked "not harvested (base tier)" and no deep-tier placeholder row, and the README has no deep-tier-only parts.'}${G && GUEST_NO_SKILL.length ? ' The "lens: [TODO]" in the README row of a guest without a SKILL.md yet is the exception (item 3b).' : ''}${G && GUEST_FAILED.length ? ' The TODO items the files already have for a guest whose digest agent returned nothing are not findings this run (item 3b): its README row\'s "lens: [TODO]", its roundtable Team-table row\'s lens TODO, and the Guest-seat TODO when no Guest seat note replaced it.' : ''}
3. Every member in team.json appears consistently: the README team table (linking to its folder), the roundtable Team table, the disclaimer's member list, the seating table (leads at least one row); lens labels and @-controls use real surnames. This run has: ${RUN_SLUGS}. Any member of team.json not in that list is a major finding (team-layer.js must be run with all members). Each member SKILL.md has a complete "## Roundtable Card" (7 bullets) and the Activation Rules line about the roundtable; python3 ${REPO}/scripts/quality_check.py <member>/SKILL.md still reports 12/12 (members only: never run it on the roundtable, which is not a research-craft skill).${G ? `
3b. Every guest in team.json "guests" appears too: a README row linking ../<home>/<slug>/SKILL.md and marked as a guest from its home team, a roundtable Team-table row (the slug in backticks), the disclaimer's list, at least one seating row (as a lead or the challenger), at least one fault line with evidence from both sides, and a "Guest seat" note below the Team table (leads when in this team's field, likely disagreements with this team's seats, the delegate note). This run's guests: ${RUN_GUESTS}; a guest of team.json not in that list is a major finding.${GUEST_NO_SKILL.length ? ` ${NO_SKILL_HEAD(GUEST_NO_SKILL)} They are not seated this run: their missing roundtable Team-table row, seating rows, fault lines and Guest seat note are not findings, nor are the "lens: [TODO]" and stage "T0 scaffold" of their README row; what new_team.py rendered for them stays (that README row, their names in GUEST_CLAUSE and SEATED_LIST, their install lines). That README row's link to ../<home>/<slug>/SKILL.md is pending in check_links.py (item 1) while their home folder has no research notes, and broken once it has notes but no SKILL.md: that broken link is expected until their home team's branch is merged here after its T1, so report it as a minor finding naming that cause, never as a blocker, and never ask to delete the row. Text that seats them (a Team-table row, seating row, fault line or Guest seat note for them, or a README line saying they sit at the roundtable) is a major finding; team-layer.js runs again here once their home team's T1 is merged.` : ''}${GUEST_FAILED.length ? ` ${FAILED_HEAD(GUEST_FAILED)} They were not checked this run: their missing rows, seating rows, fault lines and Guest seat notes are not findings, nor are the TODO items the files already have for them (item 2), and what the files already have for them stays; team-layer.js runs again for them.` : ''} Then ${GUEST_TEXT_RUN}; an exit 1 is a blocker finding (its error lines). Every guest string it prints is present and current, copied exactly: the README intro sentence has GUEST_CLAUSE right after the member names; the roundtable's "Members: …" line ends with GUEST_CLAUSE before its final period; the roundtable description and disclaimer name SEATED_LIST; Loading the Team item 1 ends with GUEST_RESOLUTION; the card-location sentence ends with GUEST_CARDS; the README Install blocks carry the GUEST_INSTALL (bash) and GUEST_INSTALL_PS (PowerShell) lines${OUTSIDE_PRODUCT ? `, compared after the path fix of a team outside product/ (in each line ${INSTALL_FIX}; a line that still copies from product/ is stale)` : ''}${DEEP ? '' : '; DEEP-READING.md\'s base-tier note ends with GUEST_DEEP_READING'}. A missing or stale string (e.g. one that lists only some of the guests) is a major finding; its fix is the exact string${OUTSIDE_PRODUCT ? ' (for an install line, with that path fix)' : ''}. A guest's card is checked read-only (7 bullets): its Activation Rules line and its Likely disagreements name its home roundtable and teammates, which is expected here, not a finding. A gap in a guest's own files (its card, SKILL.md, notes, quality_check result) is reported as home-team work (the file in the guest's folder; the fix "in <its home team folder>"), never as an edit to make here.` : ''}
4. The roundtable keeps: members run as separate agents with the user in the loop ("How the Roundtable Runs"); Activation Rules; Research Integrity Rules incl. the private/ rule; Your Controls; Loading the Team; the Member Agent Brief block; Protocol Steps 0-5 with four checkpoints (Checkpoint 4 never skipped, even in autopilot); Output Template; Outside the Team; Shared References; Honest Boundary; the footer. The README's checkpoint and control tables match the roundtable's.
5. Roundtable frontmatter: name equals team.json "roundtable"; type: roundtable; description under 1024 characters (count them), triggers present, no keyword stuffing.
6. Seating rows agree with the members' "Leads when"; the Problem Card's field-specific fields cover each member's "First questions asked".${G ? ' A guest\'s seating agrees with its Guest seat note (its card\'s Leads when was written for its home team\'s field).' : ''}
7. python3 ${REPO}/scripts/team_status.py ${TEAM} runs; the README status column and Honest Boundary agree with it. Install snippets use the team's real path (${TEAM_REL}).${G ? ' A guest\'s status cell agrees with the Guests section of that team_status.py output (its stage in its home team); the Install snippets also copy each guest\'s folder (the GUEST_INSTALL and GUEST_INSTALL_PS lines of item 3b).' : ''}
8. Nothing leaked from another team (for example a worked-example team's field, members or references).${G ? ' The guests of team.json, with their links into their home teams\' folders, are not leaks.' : ''}${G ? `
9. Guest folders are read-only: run git -C ${REPO} status --porcelain -- ${GUESTS.map(g => g.dir).join(' ')}; any output (a change in a guest's folder) is a blocker.` : ''}
Report findings with severity (blocker = broken protocol, wrong member, false claim; major = missing required part, broken link, inconsistency; minor = polish), file, location, problem and a concrete fix.`,
  },
  {
    key: 'evidence',
    prompt: () => `READ-ONLY verifier: evidence behind the team layer in ${TEAM}. Edit nothing. Assume a claim is unsupported until you have opened its source.
1. For every documented fault line in the roundtable SKILL.md: open the cited evidence on BOTH sides (the member SKILL.md passages, research notes, paper cards if any) and confirm each side's position is what the fault line says; both sides must be present; identifiers must resolve (curl -s -o /dev/null -w "%{http_code}" https://doi.org/<doi> gives 30x and the Crossref title matches; arXiv abs page title matches). A position attributed to a member that its own skill does not support is a blocker; a fault line with evidence on one side only is major; "exchange in print" needs papers on both sides that answer each other.${G ? ` A guest's side is checked in its own folder (${GUEST_DIRS}); when that folder has paper cards, the guest's side must cite them. A fault line built on a disagreement with a guest's home teammate who is not seated here is a major finding. So is a "(card evidence pending…)" mark that names a guest, or that ends a fault line where no own member's side lacks paper cards (the mark names this team's own members only).${GUEST_NO_SKILL.length ? ` ${NO_SKILL_HEAD(GUEST_NO_SKILL)} They are not seated this run: their missing fault lines are not findings, and a fault line that gives them a side is a major finding (team-layer.js runs again once their home team's T1 is merged here).` : ''}${GUEST_FAILED.length ? ` ${FAILED_HEAD(GUEST_FAILED)} They were not checked this run: their missing fault lines are not findings (team-layer.js runs again for them).` : ''}` : ''}
2. The Team-table lenses, the README "known for" lines and the seating rationale: each matches the member's own SKILL.md (no facts from memory).${G ? ' For a guest: its own SKILL.md in its folder (its lens may be restated for this team\'s field, never contradicted).' : ''}
3. Shared References and Outside the Team: every paper or tool resolves and says what the line claims.
4. RESOURCES.md: every paper cited in each member's SKILL.md has a row; spot-check 5 ✅ rows per member with tools.${G ? ' (Own members only: a guest\'s RESOURCES.md is its home team\'s work.)' : ''}
5. Nothing quotes or paraphrases material from any references/sources/private/ folder (do not open private files other than README.md).${G ? `
6. Guest folders are read-only: run git -C ${REPO} status --porcelain -- ${GUESTS.map(g => g.dir).join(' ')}; any output (a change in a guest's folder) is a blocker.${GUEST_CARDED.length ? `
7. Run ${CITE_CMD} (${CITE_WHY(GUEST_CARDED)}): every problem it lists is a finding; a card id that does not exist, or a page cited on a card that did not read the full text, is a blocker.` : ''}` : ''}
Report findings with severity (blocker/major/minor), file, location, problem and a concrete fix.`,
  },
]

function fixPrompt(findings) {
  return `Task (T2 team layer: fix). Two read-only verifiers checked ${TEAM}. Findings: ${JSON.stringify(findings)}
Verify each finding yourself (verifiers can be wrong), then apply those you confirm: blockers and majors always, minors when cheap.
- A fault line that fails the both-sides test: find the missing evidence in the members' files if it is there; otherwise drop the fault line (or move it to a "contrasts to check" note) and renumber references to it.
- A wrong or incomplete member card: fix only that member's "## Roundtable Card" in its SKILL.md, then rerun python3 ${REPO}/scripts/quality_check.py on it (12/12).${G ? `
- A finding about a guest's own files (its card, SKILL.md, notes, RESOURCES.md): never edit them; decline it as home-team work, naming the file and the fix for its home team (team-layer.js or team-base-skills.js in that team's folder, then team-layer.js here again). A finding about a guest's row, Guest seat note, seating rows or fault lines in this team's files is fixed here; a missing or stale guest string (the intro clause, the Members line, the description and disclaimer lists, the Loading-the-Team or card-location sentence, an install line) is fixed with the exact string from ${GUEST_TEXT}${OUTSIDE_PRODUCT ? ` (an install line with the path fix of a team outside product/: ${INSTALL_FIX})` : ''}.` : ''}${G && GUEST_NO_SKILL.length ? `
- ${NO_SKILL_HEAD(GUEST_NO_SKILL)} They are not seated this run: decline every finding that asks to seat them (a Team-table row, seating row, fault line or Guest seat note) or to fill their README lens (there is no SKILL.md to take it from), and one about their README row's broken link (check_links.py counts it broken once their home folder has research notes but no SKILL.md; only merging their home team's branch after its T1 fixes it); their README row, intro-clause names and install lines stay as new_team.py rendered them; team-layer.js runs again here once their home team's T1 is merged.` : ''}${G && GUEST_FAILED.length ? `
- ${FAILED_HEAD(GUEST_FAILED)} They were not checked this run: decline findings about their missing rows, seating, fault lines or Guest seat notes, and keep what the files have for them; team-layer.js runs again for them.` : ''}
- An unverifiable citation: replace it with a verified one or remove it.
Files you may edit: ${TEAM}/README.md, the roundtable SKILL.md, members' references/sources/RESOURCES.md, members' Roundtable Card sections${DEEP ? '' : `, ${TEAM}/DEEP-READING.md (base-tier note only)`}. Back up each file to ${SCRATCH}/team-layer/ before its first edit.${G ? ` Never edit anything in a guest's folder (${GUEST_DIRS}) or in another team's folder.` : ''}
Then rerun the gates and report them: python3 ${REPO}/scripts/check_links.py ${TEAM} (0 broken${G && GUEST_NO_SKILL.length ? ', apart from the README links of the guests without a SKILL.md yet above: report its result line in check_links as printed and, in broken_other, how many broken links it lists besides those README links (0 when they are the only ones)' : ''}); grep -rn "{{" ${TEAM} --include=*.md (count); ${TODO_RULE}; ${G && GUEST_CARDED.length ? `${CITE_GATE(GUEST_CARDED)}, its result in summary; ` : ''}quality_check.py on every member SKILL.md (never on the roundtable: ${RT_GATE})
Return applied and declined findings (with reasons) and the gate results.`
}

// ---------- run ----------
phase('Cards')
if (!DEEP) log('args.deep_tier is false (base tier): DEEP-READING.md becomes the short base-tier note, RESOURCES.md rows 1 and 3 get their base-tier form, the README drops its deep-tier-only parts, and no TODO may remain')

const [resources, team] = await parallel([
  // per-member resource trackers: independent of the cards and the roundtable (disjoint files)
  () => pipeline(MEMBERS, m => A(resourcesPrompt(m), { label: `resources:${m.slug}`, phase: 'Resources', schema: RES_OUT })),
  async () => {
    // barrier by necessity: the roundtable needs every member's card (and a read-only digest of every guest's)
    const cards = await pipeline(SEATS, s => IS_GUEST.has(s.slug)
      ? A(guestPrompt(s), { label: `guest:${s.slug}`, phase: 'Cards', schema: GUEST_CARD })
      : A(cardPrompt(s), { label: `card:${s.slug}`, phase: 'Cards', schema: CARD }))
    // results follow SEATS (members, then guests); a guest's home and folder come from args, never from its agent
    const got = cards.map((c, i) => c ? { ...c, slug: SEATS[i].slug, ...(IS_GUEST.has(SEATS[i].slug) ? { guest: true, home: SEATS[i].home, dir: SEATS[i].dir } : {}) } : null)
    const failedSeats = SEATS.filter((s, i) => !got[i])
    const failed = failedSeats.filter(s => !IS_GUEST.has(s.slug)).map(s => s.slug)
    const noSkill = got.filter(c => c && !isGuestCard(c) && !c.skill_exists).map(c => c.slug)
    if (failed.length) log(`card agent returned nothing for: ${failed.join(', ')} — they are left out of the roundtable`)
    if (noSkill.length) log(`no SKILL.md yet for: ${noSkill.join(', ')} — run team-base-skills.js first; they are left out of the roundtable`)
    // a guest whose digest agent died is not a guest without a skill: its own list, sentence and rerun line
    const guestFailed = failedSeats.filter(s => IS_GUEST.has(s.slug)).map(s => s.slug)
    const guestNoSkill = got.filter(c => isGuestCard(c) && !c.skill_exists)
    GUEST_FAILED = guestFailed
    GUEST_NO_SKILL = guestNoSkill.map(c => c.slug)
    if (guestFailed.length) log(`guest digest agent returned nothing for: ${guestFailed.join(', ')} — left out of this run (this says nothing about their skills); rerun team-layer.js`)
    if (guestNoSkill.length) log(`no SKILL.md yet for guest(s): ${guestNoSkill.map(c => `${c.slug} (its home team's T1, team-base-skills.js in ${HOME_DIR(c)}; merge that branch here)`).join(', ')} — they are left out of the roundtable`)
    const guestWork = got.filter(c => isGuestCard(c) && c.skill_exists && Array.isArray(c.problems) && c.problems.length)
    if (guestWork.length) log(`home-team work found in guests' files (never fixed here): ${guestWork.map(c => `${c.slug} (${HOME_DIR(c)}): ${c.problems.join('; ')}`).join(' | ')}`)
    const seated = got.filter(c => c && c.skill_exists)
    const edited = seated.filter(c => !isGuestCard(c) && c.edited).map(c => c.slug)
    if (edited.length) log(`Roundtable Card written or completed for: ${edited.join(', ')}`)
    // with guests, two seats are not enough: the roundtable is this team's, so at least one own member needs a skill
    if (G && !seated.some(c => !isGuestCard(c))) { log('no member of this team has a skill yet: roundtable and README not written'); return { cards: got, roundtable: null, readme: null } }
    if (seated.length < 2) { log('fewer than 2 members have a skill: roundtable and README not written'); return { cards: got, roundtable: null, readme: null } }
    // deepDone: this team's own members (a rerun after T3.8); a guest with cards is cited by card, but never makes a rerun
    const deepDone = seated.filter(c => !isGuestCard(c) && c.deep_tier_done).map(c => c.slug)
    const guestCarded = seated.filter(c => isGuestCard(c) && c.deep_tier_done).map(c => c.slug)
    GUEST_CARDED = guestCarded
    if (deepDone.length) log(`deep reading already done for ${deepDone.join(', ')}: rerun on a deep-tier team, the card-backed roundtable parts and README coverage are kept`)
    if (guestCarded.length) log(`guest(s) with paper cards in their own folders: ${guestCarded.join(', ')}: their fault-line sides are cited by card`)
    const rt = await A(roundtablePrompt(seated, [...failed, ...noSkill], deepDone, guestNoSkill.map(c => c.slug), guestCarded, guestFailed), { label: 'roundtable', phase: 'Roundtable', schema: RT_OUT })
    if (!rt) log('roundtable agent returned nothing')
    else {
      if (rt.dropped_contrasts.length) log(`roundtable: ${rt.dropped_contrasts.length} one-sided contrast(s) dropped: ${rt.dropped_contrasts.join('; ')}`)
      const notInRun = rt.card_problems.filter(x => /^NOT-IN-RUN\s/.test(x)).map(x => x.split(/\s+/)[1])
      if (notInRun.length) log(`team.json members${G ? ' or guests' : ''} missing from this run: ${notInRun.join(', ')}; rerun team-layer.js with ALL members${G ? ' and guests' : ''} (their existing rows were kept)`)
      if (G) {
        const noFault = rt.card_problems.filter(x => /^NO-FAULT-LINE\s/.test(x))
        if (noFault.length) log(`guest(s) in no fault line (team_check.py requires one each): ${noFault.join('; ')}`)
        const home = rt.card_problems.filter(x => /^HOME\s/.test(x))
        if (home.length) log(`home-team work reported by the roundtable author (never fixed here): ${home.join('; ')}`)
      }
    }
    const rd = await A(readmePrompt(seated, rt, deepDone, GUEST_NO_SKILL, guestFailed), { label: 'readme', phase: 'README', schema: README_OUT })
    if (!rd) log('README agent returned nothing')
    return { cards: got, roundtable: rt, readme: rd }
  },
])

const resList = (resources || []).map((r, i) => r ? { member: MEMBERS[i].slug, ...r } : { member: MEMBERS[i].slug, error: 'no result' })
resList.filter(r => r.error).forEach(r => log(`resources agent returned nothing for ${r.member}`))

phase('Verify')
const wroteTeamFiles = Boolean(team && (team.roundtable || team.readme))
if (!wroteTeamFiles) log('no roundtable or README was written in this run: verification and fix skipped (fix the causes logged above and rerun)')
const reviews = wroteTeamFiles
  ? (await parallel(LENSES.map(l => () => A(l.prompt(), { label: `verify:${l.key}`, phase: 'Verify', schema: FINDINGS })))).filter(Boolean)
  : []
if (wroteTeamFiles && reviews.length < LENSES.length) log(`${LENSES.length - reviews.length} verifier(s) returned nothing`)
const findings = reviews.flatMap(r => r.findings.map(f => ({ ...f, lens: r.lens })))
const serious = findings.filter(f => f.severity !== 'minor').length
if (wroteTeamFiles) log(`verification: ${findings.length} findings (${findings.filter(f => f.severity === 'blocker').length} blockers, ${serious} blocker+major)`)

phase('Fix')
let fix = null
if (findings.length) fix = await A(fixPrompt(findings), { label: 'fix:team-layer', phase: 'Fix', schema: G && GUEST_NO_SKILL.length ? FIX_NO_SKILL : FIX })
else if (wroteTeamFiles) log('no findings: fix step skipped')

// the fixer's links gate; beside guests without a SKILL.md yet (G only) its check_links line also counts their README links,
// broken until their home team's T1 is merged here, so the other broken links it reports (broken_other) decide
const linksFailed = f => (G && GUEST_NO_SKILL.length && typeof f.broken_other === 'number'
  ? f.broken_other > 0
  : f.check_links && !/(^|\D)0 broken|✅/.test(f.check_links))
const fixFailed = fix && (linksFailed(fix) || fix.placeholders_left > 0)
// guests: work for their home teams (no skill yet, gaps in their own files) and where their deep tier runs
const guestCards = team && team.cards ? team.cards.filter(isGuestCard) : []
// guests whose digest agent returned nothing (null in team.cards, SEATS order): this run left them out, so rerun
const guestNoDigest = team && team.cards ? SEATS.filter((s, i) => IS_GUEST.has(s.slug) && !team.cards[i]).map(s => s.slug) : []
// guests without a SKILL.md yet: not seated by this run, as a member without a skill; T2 runs again once their home team's
// T1 is merged here (make_args.mjs prints the note on their README link, which check_links.py may count as broken)
const guestNoSkillCards = guestCards.filter(c => !c.skill_exists)
const homeWork = guestCards.filter(c => c.skill_exists && Array.isArray(c.problems) && c.problems.length).map(c => `${c.slug} (${HOME_DIR(c)}): ${c.problems.join('; ')}`)
const guestNext = [
  ...(guestNoDigest.length ? [`Rerun team-layer.js: the digest agent returned nothing for guest(s) ${guestNoDigest.join(', ')}, so this run left them out (their skills were not read; nothing says they are missing).`] : []),
  ...(guestNoSkillCards.length ? [`Guests without a SKILL.md yet, not seated by this run: ${guestNoSkillCards.map(c => `${c.slug} (T1 in ${HOME_DIR(c)})`).join(', ')}. Once their home team's T1 has written the SKILL.md, merge that branch here and rerun team-layer.js here (make_args.mjs adds every guest of team.json); until then their README rows (stage T0 scaffold), intro-clause names and install lines stay as new_team.py rendered them, and the gates stay red on them: team_check.py's guests row (SKILL.md missing), its roundtable row (not in the Team table, seated in no row, in no fault line: team_check.py counts every guest of team.json as a seat, as it does every member, so it passes once the rerun seats them) and its templates row (their README rows' "lens: [TODO]"), and check_links.py (team_check.py's links row) once their home folders have research notes, which turns their README links from pending to broken.`] : []),
  ...(homeWork.length ? [`Home-team work for guests (done in their home teams, never here; then rerun team-layer.js here): ${homeWork.join(' | ')}.`] : []),
  // a guest that gets paper cards later (its home team's deep reading, merged here) must then be cited by card here, and
  // team_check.py fails the roundtable until it is: T3.8 does that once a member of this team is ready, T2 before that
  ...(G ? [DEEP
    ? `Guests' deep tier runs in their home teams (${[...new Set(GUESTS.map(HOME_DIR))].join(', ')}), not here. Once a guest has paper cards there (merged here), its side must cite them (team_check.py fails the roundtable until it does): team-integrate.js here (T3.8) brings them into the fault lines once a member of this team has finished the synthesis; before that, rerun team-layer.js here.`
    : `A guest whose home team does the deep reading gets paper cards there (${[...new Set(GUESTS.map(HOME_DIR))].join(', ')}); once they are merged here, rerun team-layer.js here: a carded guest's side is cited by card at the base tier too, and team_check.py fails the roundtable until it is.`] : []),
]
return {
  stage: 'T2 team layer',
  date: DATE,
  team: TEAM_REL,
  next: !wroteTeamFiles ? ['Nothing was written: fix the causes in the log (e.g. members without SKILL.md: run team-base-skills.js) and rerun team-layer.js with all members.', ...guestNext] : [
    `Gates${guestNoSkillCards.length ? ' (apart from what stays red on the guests without a SKILL.md yet: below)' : ''}: python3 scripts/check_links.py ${TEAM_REL} → 0 broken; grep -rn --include='*.md' -e '{{' -e '\\[TODO' ${TEAM_REL} → ${DEEP ? 'only the items reserved for T3 steps' : 'no output; or all T2 gates at once: python3 scripts/team_check.py ' + TEAM_REL + ' --tier base'}.`,
    ...(fixFailed ? ['The fixer reported a failing gate (see fix): look at it before committing.'] : []),
    `Commit: bash scripts/team_commit.sh ${TEAM_REL} "feat(${TEAM_REL.split('/').pop()}): team layer (README + roundtable)".`,
    DEEP ? `Deep tier next: team-harvest.js per member (node scripts/workflows/make_args.mjs team-harvest --team ${TEAM_REL} builds the calls).`
      : guestNoSkillCards.length ? 'Base tier: the team is complete once the rerun below has seated the guests without a SKILL.md yet and is committed; until then the roundtable runs with the seats it has (try it on a real question, playbook §九).'
        : 'Base tier: the team is complete after the commit; try the roundtable on a real question (playbook §九).',
    ...guestNext,
  ],
  // members' cards, then guests' digests (SEATS order); a guest's entry is keyed "guest" and carries its home-team work
  cards: team && team.cards ? team.cards.map((c, i) => c
    ? (isGuestCard(c)
      ? { guest: c.slug, home: c.home, skill_exists: c.skill_exists, had_complete_card: c.had_complete_card, quality_check: c.quality_check, problems: Array.isArray(c.problems) ? c.problems : [] }
      : { member: c.slug, edited: c.edited, skill_exists: c.skill_exists, quality_check: c.quality_check })
    : IS_GUEST.has(SEATS[i].slug) ? { guest: SEATS[i].slug, home: SEATS[i].home, error: 'no result' } : { member: SEATS[i].slug, error: 'no result' }) : null,
  resources: resList,
  roundtable: team ? team.roundtable : null,
  readme: team ? team.readme : null,
  findings: findings.length,
  serious_findings: serious,
  fix,
}
