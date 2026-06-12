# Project Resume Experience Skill Design

## Goal

Create a Codex skill that turns a local project into a truthful, role-targeted resume project experience entry.

The skill should prioritize rigor over one-shot automation. It must separate what the project does from what the candidate personally contributed, then adapt the final wording to the candidate profile and target role.

## Core Principle

Do not turn project facts into personal claims without confirmation.

Local project files, README content, dependency manifests, code structure, and Git history are evidence sources. They can support analysis, but they do not fully define the candidate's role. For larger or multi-author projects, the skill must confirm responsibility boundaries before generating final resume text.

## Inputs

The skill should gather these inputs progressively:

1. Candidate context
   - Target role
   - Experience level
   - Main technical direction
   - Preferred resume style
   - Claims or wording to avoid

2. Responsibility context
   - Solo Owner: project was mostly independently completed
   - Primary Owner: candidate led the project with some collaboration
   - Module Owner: candidate owned one or more major modules
   - Contributor: candidate contributed specific features, fixes, or optimizations
   - Maintainer / Refactor: candidate mainly maintained, refactored, tested, deployed, or optimized

3. Project evidence
   - README and documentation
   - Source structure
   - Dependency and build files
   - Tests
   - Git author distribution
   - Candidate-related commits, if identifiable
   - Relevant module paths confirmed by the user

4. Optional target context
   - Job description
   - Resume language
   - Output length
   - Desired version type, such as concise, technical, or JD-matched

## Recommended Workflow

1. Assess project scale
   - Small project: simple structure, likely single owner, few authors.
   - Medium project: multiple modules or uncertain ownership.
   - Large project: many modules, multiple authors, unclear role boundaries.

2. Ask only direction-setting questions first
   - Confirm target role and experience level.
   - Confirm responsibility mode.
   - Ask which modules or responsibilities should be treated as personal contribution.

3. Scan the project with scope
   - Build a high-level project map.
   - Identify technical stack and major modules.
   - Inspect user-confirmed or Git-suggested responsibility areas first.
   - Avoid treating the whole project as personal contribution unless confirmed.

4. Produce an evidence-backed fact card
   - Project overview
   - Technical stack
   - Major modules
   - Candidate contribution
   - Technical challenges
   - Solutions and implementation details
   - Results and impact
   - Missing or uncertain information

5. Require confirmation before final resume text
   - If responsibility is unclear, output a draft analysis only.
   - Mark uncertain claims as questions.
   - Do not fabricate metrics, ownership, leadership, scale, or business impact.

6. Generate resume-ready versions
   - Concise version
   - Technical-depth version
   - JD-matched version when a JD is provided

## Evidence Levels

Each important claim should be tagged internally or visibly when useful:

- Confirmed: explicitly confirmed by the user.
- Evidence: supported by project files, Git history, tests, or docs.
- Inferred: plausible from project structure but not confirmed.
- Missing: needed for a stronger resume entry but unavailable.

Final resume text should use only Confirmed claims and reliable Evidence claims. Inferred claims should be converted into questions or conservative wording.

## Output Shape

The first version of the skill should produce:

```text
Project Fact Card
- Project goal:
- Tech stack:
- Major modules:
- Evidence sources:

Personal Contribution Card
- Responsibility mode:
- Owned modules:
- Concrete work:
- Technical decisions:
- Problems solved:
- Confirmed impact:
- Claims to avoid:

Open Questions
- ...

Resume Entry
- Concise version:
- Technical version:
- JD-matched version, if applicable:
```

## Skill Structure

Recommended folder layout:

```text
project-resume-experience/
├── SKILL.md
├── references/
│   ├── extraction-schema.md
│   ├── responsibility-modes.md
│   ├── resume-style.md
│   └── examples.md
└── scripts/
    └── project_scan.py
```

`SKILL.md` should stay concise and describe the workflow, hard rules, and when to load references. Detailed examples and schemas should live in `references/`.

`project_scan.py` should be optional in the first version. The skill can work without it, but a script can later standardize collection of project structure, dependency files, Git author summaries, and recent commit summaries.

## Hard Rules

- Confirm responsibility boundaries before final resume generation.
- Separate project overview from personal contribution.
- Treat Git as evidence, not ground truth.
- Do not invent metrics, leadership scope, business impact, or production usage.
- Do not claim ownership of the whole project unless the user confirms it.
- For multi-author or large projects, perform staged confirmation before deep scanning.
- Prefer specific contribution wording over generic project description.

## First Version Scope

The first version should focus on:

- A rigorous staged workflow in `SKILL.md`.
- Clear responsibility modes.
- Evidence-level discipline.
- Conservative Chinese resume output by default.
- Optional JD-based rewrite when the user provides a job description.

Out of scope for the first version:

- Fully automated resume generation from a repository with no user confirmation.
- Complex scoring or ranking of candidate-project fit.
- Automatic quantitative impact generation.
- Parsing private external systems such as issue trackers unless the user provides exported text.

## Future Iteration

After collecting strong resume examples, add them to `references/examples.md` and use them to refine:

- Bullet structure.
- Verb choice.
- Technical depth by role.
- Seniority-specific framing.
- Chinese and English resume style differences.
- Patterns for AI, backend, frontend, full-stack, data, and infrastructure roles.
