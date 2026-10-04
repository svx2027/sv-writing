# sv-writing

`writing-skill` is SV's master writing skill for Claude Code and any other agent that reads skills. It writes, edits, detects and suggests so text reads like SV, a specific person, and never like a chatbot. It works in English and Hinglish and starts with LinkedIn. It also learns: when SV gives feedback, the skill writes the lesson into its own files and publishes a new version here.

It compiles three open-source skills into one:

1. [humanizer](https://github.com/blader/humanizer) by Siqi Chen (blader), based on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
2. [stop-slop](https://github.com/hardikpandya/stop-slop) by Hardik Pandya
3. [no-ai-slop](https://github.com/petergyang/no-ai-slop) by Peter Yang

## What each source gave

humanizer: the theory (every AI tell is the model's default choice), the strength ranking, most of the patterns with their before and after examples, the never-invent rule, the self-audit and voice matching.

stop-slop: the core file plus reference files layout, the absolute bans that power strict mode, false agency, narrator from a distance, lazy extremes, vague declaratives and the 50-point score.

no-ai-slop: voice preservation and the minimum effective edit, detect mode, the portability test, faux-insight setups, colon reveals, recap endings, synonym cycling and the pass or fail eval loop.

Added here: SV's house rules, Hinglish, the LinkedIn module, suggest mode, write mode and the retro loop.

Where the sources disagree, this skill picks a side and says so. stop-slop bans every adverb and every three-item list; here those bans apply only in strict mode, because applied everywhere they flatten a writer's voice. humanizer dropped synonym cycling as a human habit and no-ai-slop kept it; here it is a weak-alone clarity fix. no-ai-slop allows a dash or two in long drafts; SV allows none.

## Install

### Claude Code on your computer

```
git clone https://github.com/svx2027/sv-writing.git ~/.claude/skills/writing-skill
```

Type `/writing-skill`, or ask for writing help and Claude picks the skill up on its own. Claude Code notices new and changed skills without a restart.

The install is a git checkout, which keeps it current: the skill runs `git pull` once per session, and the retro loop commits and pushes from the same folder. To update by hand, run `bash ~/.claude/skills/writing-skill/install.sh`.

### Claude Code on the web (cloud sessions)

Cloud sessions can't see the skills folder on your computer. Add this line to your cloud environment's setup script (the environment menu in the session's title bar, then Edit, then Setup script):

```
git clone --depth 1 https://github.com/svx2027/sv-writing.git ~/.claude/skills/writing-skill
```

Every new session in that environment then starts with the latest version. For the retro loop to push from a cloud session, the Claude GitHub App needs access to this repository.

### Claude.ai and other agents

Claude.ai and Claude Desktop: download this repository as a ZIP and upload it as a skill in Settings. That copy can't update itself, so upload again after big changes.

Codex, Gemini CLI, Cursor and other agents: copy this folder into the agent's skills folder, or point the agent at `SKILL.md`.

## Use

1. Edit (the default): `/writing-skill` and paste a draft. You get the clean text, what changed, a before and after score, and up to three suggestions only you can act on.
2. Detect: "is this slop?" or "detect". Every tell, quoted, with a short fix and no rewrite.
3. Suggest: "suggest" or "feedback". Ranked improvements with a top pick, and no rewrite.
4. Write: "write a LinkedIn post about...". A draft built only from facts you gave, with `[ADD: ...]` wherever a fact is missing, plus two other first lines to choose from.
5. Strict: add "strict" to any request for stop-slop's hard rules.
6. Retro: give feedback any time ("never use 'folks'", "this hook works", or paste the version you actually posted). The skill files the lesson, bumps the version, logs it in `retro/LEARNINGS.md` and pushes.

## How it learns

1. Feedback stated as a rule ("never", "always", "from now on") becomes a rule at once, in the one file it belongs to.
2. Feedback about a single line is logged as an observation. A second matching observation promotes both into a rule.
3. Samples of SV's writing go into `platforms/<platform>/samples/` unchanged, and `voice/profile.md` records what they show.
4. When SV posts a different version from the draft, every change SV made counts as feedback.
5. Every change bumps the version in `SKILL.md`, gets a `CHANGELOG.md` entry and a git tag, passes `scripts/validate.py`, and is pushed here. GitHub keeps every version; the install always runs the latest.

## Layout

```
SKILL.md                     core: hard rules, modes, workflow, strict mode, retro loop
references/patterns.md       36 tells in 8 families, tiered, with fixes and examples
references/words.md          cut-on-sight words, jargon, empty adverbs and phrases
references/hinglish.md       Hinglish forms of the tells, plus Hinglish-only tells
references/eval.md           pass or fail checks and the 50-point score
platforms/linkedin/          LinkedIn guide and SV's post samples
platforms/_template/         copy this to add Instagram, YouTube or any platform
voice/profile.md             SV's voice, built from samples and feedback
retro/LEARNINGS.md           the feedback ledger
scripts/validate.py          checks run before every commit
install.sh                   install or update
```

## Make it yours

Fork it, then replace `voice/profile.md`, the hard rules in `SKILL.md`, the samples in `platforms/*/samples/` and `retro/LEARNINGS.md`. Change the repository URL in `SKILL.md` and `install.sh`. The patterns, word lists and eval work for anyone.

## License

MIT, like all three sources. Their notices are in `THIRD_PARTY_NOTICES.md`.
