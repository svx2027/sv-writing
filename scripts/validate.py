#!/usr/bin/env python3
"""Check the writing-skill package before every commit.

Run from anywhere: python3 scripts/validate.py
Exits 1 and lists every problem when a check fails.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = "writing-skill"
MAX_SKILL_WORDS = 3500
MAX_DESCRIPTION_CHARS = 1024
DASHES = ("—", "–")  # em dash, en dash
SKIP_DIRS = {".git", "samples"}  # samples are SV's own posts, kept unchanged

errors = []


def rel(path):
    return path.relative_to(ROOT).as_posix()


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
            continue
        yield path


# 1. SKILL.md frontmatter
skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
match = re.match(r"^---\n(.*?)\n---\n", skill_text, re.S)
version = None
if not match:
    errors.append("SKILL.md: missing YAML frontmatter between --- lines")
    body = skill_text
else:
    front = match.group(1)
    body = skill_text[match.end():]
    name = re.search(r"^name:\s*(\S+)\s*$", front, re.M)
    if not name or name.group(1) != SKILL_NAME:
        errors.append(f"SKILL.md: name must be {SKILL_NAME}")
    block = re.search(r"^description:\s*\|\s*\n((?:[ \t]+\S.*\n?)+)", front + "\n", re.M)
    if block:
        description = " ".join(line.strip() for line in block.group(1).splitlines())
    else:
        inline = re.search(r"^description:\s*(.+)$", front, re.M)
        description = inline.group(1).strip() if inline else ""
    if not description:
        errors.append("SKILL.md: description is missing")
    elif len(description) > MAX_DESCRIPTION_CHARS:
        errors.append(f"SKILL.md: description has {len(description)} characters; the limit is {MAX_DESCRIPTION_CHARS}")
    found = re.search(r'^\s+version:\s*"?(\d+\.\d+\.\d+)"?\s*$', front, re.M)
    if found:
        version = found.group(1)
    else:
        errors.append('SKILL.md: metadata.version must look like "1.2.3"')

# 2. SKILL.md length (every word is read on each use)
words = len(body.split())
if words > MAX_SKILL_WORDS:
    errors.append(f"SKILL.md: body has {words} words; the limit is {MAX_SKILL_WORDS}")

# 3. CHANGELOG.md matches the version
changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
heading = re.search(r"^## (\d+\.\d+\.\d+)", changelog, re.M)
if not heading:
    errors.append("CHANGELOG.md: no '## x.y.z' heading found")
elif version and heading.group(1) != version:
    errors.append(f"CHANGELOG.md: newest entry is {heading.group(1)} but SKILL.md says {version}")

# 4. No em or en dashes outside quoted examples, inline code and code blocks
for path in markdown_files():
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or line.lstrip().startswith(">"):
            continue
        visible = re.sub(r"`[^`]*`", "", line)
        if any(dash in visible for dash in DASHES):
            errors.append(f"{rel(path)}:{number}: em or en dash outside a quoted example or code")

# 5. Every file path a markdown file mentions exists
path_pattern = re.compile(r"\b((?:references|platforms|voice|retro|scripts)/[\w./-]*\w)")
for path in markdown_files():
    for mention in set(path_pattern.findall(path.read_text(encoding="utf-8"))):
        if not (ROOT / mention).exists():
            errors.append(f"{rel(path)}: mentions {mention}, which does not exist")

# 6. Patterns are numbered 1..N and every #N reference points at one
patterns = (ROOT / "references" / "patterns.md").read_text(encoding="utf-8")
numbers = [int(n) for n in re.findall(r"^### (\d+)\. ", patterns, re.M)]
if numbers != list(range(1, len(numbers) + 1)):
    errors.append("references/patterns.md: patterns must be numbered 1, 2, 3 ... without gaps")
for heading_match in re.finditer(r"^### (\d+)\. .*\n+(.*)", patterns, re.M):
    if not heading_match.group(2).startswith("Tier:"):
        errors.append(f"references/patterns.md: pattern {heading_match.group(1)} must start with a Tier: line")
table_rows = re.findall(r"^\| (\d+) \|", patterns, re.M)
if [int(n) for n in table_rows] != numbers:
    errors.append("references/patterns.md: the index table must list every pattern in order")
for path in markdown_files():
    for ref in re.findall(r"(?<![\w&])#(\d{1,3})\b", path.read_text(encoding="utf-8")):
        if not 1 <= int(ref) <= len(numbers):
            errors.append(f"{rel(path)}: refers to pattern #{ref}, which does not exist")

# 7. Every platform has a guide and a samples folder
for platform in sorted((ROOT / "platforms").iterdir()):
    if not platform.is_dir():
        continue
    if not (platform / "guide.md").exists():
        errors.append(f"{rel(platform)}: missing guide.md")
    if not (platform / "samples" / "README.md").exists():
        errors.append(f"{rel(platform)}: missing samples/README.md")

# 8. Files the retro loop writes to exist
for required in ("voice/profile.md", "retro/LEARNINGS.md", "references/words.md",
                 "references/hinglish.md", "references/eval.md"):
    if not (ROOT / required).exists():
        errors.append(f"missing {required}")

if errors:
    print(f"validate: {len(errors)} problem(s)")
    for problem in errors:
        print(f"  {problem}")
    sys.exit(1)
print(f"validate: ok (version {version}, {len(numbers)} patterns, SKILL.md {words} words)")
