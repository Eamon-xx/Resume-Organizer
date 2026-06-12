# Extraction Schema

Use this schema when turning local project evidence into resume material.

## Evidence Levels

| Level | Meaning | Resume Use |
| --- | --- | --- |
| Confirmed | User explicitly confirmed it. | Safe to use. |
| Evidence | Supported by files, docs, tests, Git, or visible code. | Safe when wording stays within evidence. |
| Inferred | Plausible from structure or commit patterns but not confirmed. | Ask or phrase conservatively. |
| Missing | Needed for a stronger claim but unavailable. | Ask; do not invent. |

## Project Scale

- Small: single-purpose project, simple structure, one likely owner.
- Medium: multiple modules, unclear responsibility, or mixed evidence.
- Large: many modules, multiple authors, broad platform scope, or unclear role boundaries.

For medium or large projects, confirm responsibility before detailed scanning.

## Project Fact Card

```text
Project Fact Card
- Project goal:
- Domain / user scenario:
- Tech stack:
- Major modules:
- Data flow / architecture:
- Tests / quality signals:
- Deployment / runtime signals:
- Evidence sources:
- Uncertain project facts:
```

Only describe what the project is or does. Do not use "I", "my", "responsible for", or personal ownership language here.

## Personal Contribution Card

```text
Personal Contribution Card
- Responsibility mode:
- Confirmed owned modules:
- Concrete work:
- Technical decisions:
- Problems solved:
- Collaboration boundary:
- Confirmed impact:
- Claims to avoid:
- Inferred items needing confirmation:
```

This card is the only source for final personal resume claims.

## Open Questions

Ask short, decision-changing questions. Prioritize:

1. Target role and experience level.
2. Responsibility mode.
3. Owned modules or excluded modules.
4. Metrics or impact evidence.
5. JD-specific emphasis.

## Final Output Template

```text
项目事实卡
- ...

个人贡献卡
- ...

待确认问题
- ...

简历项目经历
- 精简版：
- 技术版：
- JD 匹配版：
```

If final wording is blocked by missing responsibility confirmation, omit the resume section and explain what must be confirmed.
