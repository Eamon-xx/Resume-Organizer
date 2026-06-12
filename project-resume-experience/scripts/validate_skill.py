from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REFERENCES = [
    ROOT / "references" / "extraction-schema.md",
    ROOT / "references" / "responsibility-modes.md",
    ROOT / "references" / "resume-style.md",
    ROOT / "references" / "examples.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read_skill() -> str:
    if not SKILL.exists():
        fail("SKILL.md is missing")
    return SKILL.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md is missing YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def main() -> None:
    text = read_skill()
    fields = parse_frontmatter(text)

    if fields.get("name") != "project-resume-experience":
        fail("frontmatter name must be project-resume-experience")

    description = fields.get("description", "")
    if not description.startswith("Use when"):
        fail("frontmatter description must start with 'Use when'")

    if len(description) > 500:
        fail("frontmatter description should stay under 500 characters")

    for path in REFERENCES:
        if not path.exists():
            fail(f"required reference is missing: {path.relative_to(ROOT)}")
        rel = path.relative_to(ROOT).as_posix()
        if rel not in text:
            fail(f"SKILL.md does not link reference: {rel}")

    print("PASS: project-resume-experience skill structure is valid")


if __name__ == "__main__":
    main()
