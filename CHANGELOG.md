# Changelog

Newest first. Each version also gets a git tag (v1.0.0) once it is pushed from a checkout with push access.

## 1.0.2 (2026-10-05)

1: Logged SV's first observation (a casual line read as childish) and a keep note for SV's replacement line.

## 1.0.1 (2026-10-04)

Fixes from the first test run: five agents ran write, edit, detect, suggest and a full retro against v1.0.0.

1: Added "When rules conflict": hard rules, then facts, then SV's voice, then the platform, then the patterns. SV's strong opinions stay; portable filler goes.
2: Suggest now loads words.md and eval.md, which its output needs, and voice/profile.md loads in every mode.
3: A draft sent for editing no longer counts as a writing sample, and gendered verbs in a draft are no evidence of SV's gender.
4: Write never stalls on gaps: it drafts with [ADD: ...] and puts one question in Notes.
5: Detect reports each span once, counts hard rules, ends with a slop verdict, and quotes dashes as [dash].
6: Retro updates every copy of a rule it changes, splits mixed feedback, and dates profile lines.
7: The git steps act only on the skill's own checkout, never on a repository around it.
8: Hashtags are allowed where the platform guide allows them; markdown is still banned.

## 1.0.0 (2026-10-04)

First compilation.

1: Merged humanizer 3.1.0 (commit 225a6f3), stop-slop (commit 8da1f03) and no-ai-slop (commit 000650b) into one catalogue of 36 patterns in eight families, each with a tier, a fix and examples that add no facts.
2: Modes: write, edit, detect, suggest and retro. Strict mode applies stop-slop's absolute rules and raises the score gate to 40 out of 50.
3: SV's house rules became hard rules: no dashes, no not-X-but-Y, no chatbot residue, no recap endings, sentence case, paste-ready plain text, colons for lists, and never invent.
4: Added the LinkedIn module, the Hinglish reference (version 1, written by Claude), a draft voice profile, the retro ledger, the validator and the installer.
