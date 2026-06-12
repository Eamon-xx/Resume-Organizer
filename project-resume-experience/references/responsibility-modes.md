# Responsibility Modes

Use the mode that matches the candidate's confirmed contribution. If uncertain, ask before final resume writing.

## Solo Owner

The candidate mostly completed the project independently.

Allowed wording:
- "独立完成..."
- "负责从需求拆解、核心开发到部署..."
- "设计并实现..."

Avoid unless confirmed:
- Team leadership.
- Production scale.
- Business impact.

## Primary Owner

The candidate led the project, but others contributed.

Allowed wording:
- "主导..."
- "负责核心方案设计与主要模块实现..."
- "协调...并完成..."

Clarify:
- Which parts were delegated.
- Whether architecture decisions were owned by the candidate.

## Module Owner

The candidate owned one or more major modules inside a larger project.

Allowed wording:
- "负责...模块..."
- "围绕...设计并实现..."
- "与...模块联调..."

Avoid:
- "完成整个系统..."
- "主导项目..." unless confirmed.

## Contributor

The candidate contributed features, fixes, optimizations, tests, or docs.

Allowed wording:
- "参与..."
- "完成...功能开发..."
- "修复...问题..."
- "补充...测试..."

Prefer specificity over scope inflation. A precise contribution is stronger than an unsupported whole-project claim.

## Maintainer / Refactor

The candidate mainly improved existing code, deployment, tests, observability, or maintainability.

Allowed wording:
- "重构..."
- "优化..."
- "补充自动化测试..."
- "完善部署 / 配置 / 文档..."

Clarify:
- Whether changes improved performance, reliability, delivery speed, or readability.
- Whether numbers are measured or estimated.

## Confirmation Prompt

Use a compact prompt:

```text
我先确认职责边界：这个项目中你更接近哪种角色？
Solo Owner / Primary Owner / Module Owner / Contributor / Maintainer

如果是模块负责，请列出你负责的目录、模块或功能；如果有不能写成你贡献的部分，也一起说明。
```
