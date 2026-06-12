---
name: project-resume-experience
description: Use when converting a local software project, repository, README, codebase, Git history, or project notes into truthful resume project experience entries for a specific candidate role or job target.
---

# Project Resume Experience

## Core Rule

Project facts are not personal claims. Confirm the candidate's role and responsibility boundary before writing final resume text, especially for large or multi-author projects.

## Workflow

1. **Collect candidate context**
   - Target role, experience level, technical direction, preferred language, and claims to avoid.
   - If present, read `.resume-context.md` or similar local notes before asking.

2. **Confirm responsibility mode**
   - Use `references/responsibility-modes.md`.
   - Choose Solo Owner, Primary Owner, Module Owner, Contributor, or Maintainer / Refactor.
   - If responsibility is unclear, ask before deep scanning.

3. **Assess and scan the local project**
   - Start with `rg --files`, README/docs, dependency/build files, tests, and Git author summaries.
   - For large projects, scan broadly for project shape, then inspect only confirmed or likely responsibility areas.
   - Treat Git as evidence, not ground truth.

4. **Build evidence-backed cards**
   - Use `references/extraction-schema.md`.
   - Separate Project Fact Card from Personal Contribution Card.
   - Mark important claims as Confirmed, Evidence, Inferred, or Missing.

5. **Confirm uncertain claims**
   - Do not generate final resume text from unconfirmed ownership, fabricated metrics, vague impact, or whole-project claims.
   - Convert Inferred and Missing items into questions or conservative wording.

6. **Generate resume entries**
   - Use `references/resume-style.md`.
   - Default to conservative Chinese output unless the user requests otherwise.
   - If a JD is provided, create a JD-matched version without inventing fit.

## Reference Loading

- Read `references/extraction-schema.md` when producing cards, evidence tags, or final output structure.
- Read `references/responsibility-modes.md` when choosing or confirming contribution scope.
- Read `references/resume-style.md` before writing resume bullets or adapting to a target role.
- Read `references/examples.md` when examples would improve consistency or when adding new benchmark samples.

## Hard Stops

Stop and ask before final resume generation when:

- The project appears multi-author and the candidate's contribution is not confirmed.
- The user asks for "my project experience" but the project evidence only describes whole-project behavior.
- Git history conflicts with the claimed responsibility.
- Metrics, production usage, leadership scope, or business impact are not supported.

In these cases, output analysis and questions only, not final resume-ready text.
