# Changelog

## 1.1.1 - 2026-09-04

- Replaced the large README hero graphic with the AWS Certified AI Practitioner badge supplied for this project.
- Fixed Claude Skill packaging to match Anthropic's documented ZIP structure: `aws-ai-practitioner-coach/skill.md`.
- Simplified Skill YAML frontmatter to only the required `name` and `description` fields.
- Updated the packaging script and validator so future builds keep the Claude-compatible structure.
- Updated beginner setup instructions for students who previously saw a Claude Skill upload error.

## 1.1.0 - 2026-09-03

### Student experience redesign
- Rewrote README as a beginner-first AWS AI Practitioner landing page.
- Added custom certificate-style and step-by-step SVG graphics.
- Added SEO-focused AIF-C01 headings, descriptions, FAQ, and search terms.
- Added DataTweets.com branding and links.
- Moved Python commands to a clearly marked maintainer-only section.
- Simplified Claude Pro and ChatGPT Plus setup for non-technical learners.
- Added a ready-to-upload Claude Skill ZIP under `downloads/`.
- Added all three 65-question practice exam PDFs under `practice-exams/` for direct student access.

## 1.0.3 - 2026-09-03

- Split the taxonomy into five domain files with a small top-level manifest for progressive loading.
- Kept source-practice PDFs private in this version: the public package contained aggregate corpus analysis but no per-question answer mappings.
- Updated Skill, ChatGPT Project instructions, README, packaging, and validation for the progressive-disclosure layout.

## 1.0.2 - 2026-09-03

- Fixed CI/local validation when the repository root is passed as `.`.
- Normalized governance concept IDs in the relationship graph to match taxonomy IDs.
- Removed duplicate governance `best-for` edges while retaining explicit confusion-pair edges.
- Changed the Claude packaging script to include only runtime Skill files.
- Added `requirements-dev.txt` for reproducible local validation.
- Re-verified ChatGPT Plus Project fallback and Claude Pro custom Skill availability against current official product documentation.

## 1.0.1 - 2026-09-03

- Added GitHub repository publishing guidance and CI validation.
- Added a portable ZIP packaging script for Claude custom-skill upload.
- Strengthened the four-way governance distinction: CloudTrail vs AWS Config vs Audit Manager vs Trusted Advisor.
- Added explicit confusion-pair handling after confident wrong answers.
- Expanded validation to parse YAML/CSV references and enforce key governance graph edges.
- Added manual QA scenarios for adaptive tutoring behavior.

## 1.0.0 - 2026-09-03

- Initial AIF-C01 taxonomy, relationship graph, decision rules, question blueprints, adaptive tutoring workflow, and ChatGPT Plus / Claude Pro setup guides.
