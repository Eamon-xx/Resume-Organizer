# Project Resume Experience Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first rigorous version of a Codex skill that converts local project evidence into truthful, role-targeted resume project experience entries.

**Architecture:** Keep `SKILL.md` focused on trigger conditions, staged workflow, and hard rules. Move detailed schemas, responsibility modes, resume wording guidance, and examples into one-level `references/` files.

**Tech Stack:** Markdown-based Codex skill files with a small optional Python validation script.

---

## File Structure

- Create: `project-resume-experience/references/extraction-schema.md`
  - Fact card, contribution card, evidence levels, output templates.
- Create: `project-resume-experience/references/responsibility-modes.md`
  - Responsibility modes and wording constraints.
- Create: `project-resume-experience/references/resume-style.md`
  - Chinese-first resume writing guidance by role and seniority.
- Create: `project-resume-experience/references/examples.md`
  - Minimal initial examples and future example slots.
- Create: `project-resume-experience/scripts/validate_skill.py`
  - Lightweight structural validator for required files and frontmatter.
- Create: `project-resume-experience/SKILL.md`
  - Main skill entrypoint, concise workflow, reference loading guidance, hard rules.

## Task 1: Add Lightweight Validation First

**Files:**
- Create: `project-resume-experience/scripts/validate_skill.py`

- [ ] **Step 1: Write validator**

Validate:
- Required files exist.
- `SKILL.md` has frontmatter.
- `name` equals `project-resume-experience`.
- `description` starts with `Use when`.
- `SKILL.md` links all reference files.

- [ ] **Step 2: Run validator and verify RED**

Run: `py project-resume-experience/scripts/validate_skill.py`

Expected: FAIL because the required skill files do not exist yet.

## Task 2: Create Skill Entrypoint

**Files:**
- Create: `project-resume-experience/SKILL.md`

- [ ] **Step 1: Write `SKILL.md`**

Include:
- YAML frontmatter with `name: project-resume-experience`.
- Trigger-focused description under 500 characters.
- Overview with the core principle: project facts are not personal claims.
- Staged workflow: collect context, confirm responsibility, scoped scan, fact card, confirmation, final resume entry.
- Reference loading guidance.
- Hard rules for evidence and ownership.

- [ ] **Step 2: Review for skill authoring constraints**

Check:
- Description starts with `Use when`.
- Description does not summarize detailed workflow.
- Body is concise and delegates detail to references.

## Task 3: Add Reference Files

**Files:**
- Create: `project-resume-experience/references/extraction-schema.md`
- Create: `project-resume-experience/references/responsibility-modes.md`
- Create: `project-resume-experience/references/resume-style.md`
- Create: `project-resume-experience/references/examples.md`

- [ ] **Step 1: Write extraction schema**

Define project fact card, personal contribution card, open questions, resume output, and evidence levels.

- [ ] **Step 2: Write responsibility mode guidance**

Define Solo Owner, Primary Owner, Module Owner, Contributor, and Maintainer / Refactor. Include allowed phrasing and risky phrasing.

- [ ] **Step 3: Write resume style guidance**

Cover Chinese default output, role emphasis, seniority framing, conservative metric handling, and JD-matched rewrites.

- [ ] **Step 4: Write initial examples**

Add compact examples showing how the same project changes under Solo Owner, Module Owner, and Contributor modes.

## Task 4: Run Validation

**Files:**
- All skill files.

- [ ] **Step 1: Run validator and verify GREEN**

Run: `py project-resume-experience/scripts/validate_skill.py`

Expected: PASS with a concise success message.

## Task 5: Verify Repository State

**Files:**
- All files above.

- [ ] **Step 1: List skill files**

Run: `rg --files project-resume-experience`

Expected: all six created skill files are listed.

- [ ] **Step 2: Review git diff**

Run: `git diff -- project-resume-experience docs/superpowers`

Expected: diff contains only the planned skill files and planning/spec documents.

- [ ] **Step 3: Check git status**

Run: `git status --short`

Expected: new files are visible and no unrelated changes are present.
