# AWS AI Practitioner Coach

Adaptive exam-prep Skill for **AWS Certified AI Practitioner (AIF-C01)**.

**Version:** 1.0.3  
**Blueprint:** AIF-C01 v1.1  
**Verified:** 2026-09-03

The coach teaches a decision chain instead of `keyword -> answer` memorization:

`question signal -> requirement/constraint -> concept -> relationship -> best answer -> distractor elimination`

## What is included

- AIF-C01 taxonomy split by the five official domains
- concept/service relationship graph
- decision rules for high-confusion topics
- original question-generation blueprints
- adaptive mastery guidance and student-state template
- aggregate analysis of 195 questions from three user-supplied practice exams
- setup instructions for Claude Pro and ChatGPT Plus
- validation and packaging scripts

The public repository **does not contain the three practice PDFs or per-question answer mappings**. Learners can upload their own lawful copies privately when they want exact source-question practice.

## Repository structure

```text
aws-ai-practitioner-coach/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── CHATGPT_PLUS_PROJECT_INSTRUCTIONS.md
├── CLAUDE_PRO_QUICK_SETUP.md
├── requirements-dev.txt
├── .github/workflows/validate.yml
├── docs/TESTING.md
├── references/
│   ├── SOURCES.md
│   ├── official-blueprint-summary.md
│   ├── aif-c01-taxonomy.yaml
│   ├── taxonomy/d1.yaml ... d5.yaml
│   ├── relationship-graph.csv
│   ├── decision-rules.yaml
│   ├── question-blueprints.yaml
│   └── practice-corpus-analysis.md
├── scripts/
│   ├── mastery.py
│   ├── package_skill.py
│   └── validate_skill.py
└── templates/
    ├── student-state.yaml
    └── session-report.md
```

The taxonomy uses **progressive disclosure**: `aif-c01-taxonomy.yaml` is a small manifest, while detailed concepts live in `taxonomy/d1.yaml` through `d5.yaml`. A tutor only needs to load the relevant domain file.

## Claude Pro setup

Claude Pro supports uploading custom Skills.

1. In Claude, open **Settings -> Capabilities** and enable **Code execution and file creation**.
2. Clone/download this repository.
3. Build the upload ZIP:

```bash
python scripts/package_skill.py
```

4. In Claude, go to **Customize -> Skills -> Create skill -> Upload a skill**.
5. Upload `dist/aws-ai-practitioner-coach.zip` and enable the Skill.
6. Recommended: create a Claude Project named `AWS AIF-C01 Study` and upload your own practice PDFs there.
7. Test with:

```text
Use my AWS AI Practitioner Coach skill. Start a 10-question diagnostic, one question at a time.
```

See `CLAUDE_PRO_QUICK_SETUP.md` for the short setup guide.

## ChatGPT Plus setup

As of 2026-09-03, native ChatGPT Skills are documented for eligible Business, Enterprise, Healthcare, and Edu workspaces, not personal Plus accounts. New custom GPT creation is also not available on personal Plus accounts. For Plus, use a **ChatGPT Project** as the compatibility setup.

1. Create a Project named `AWS AIF-C01 Coach`.
2. Copy the contents of `CHATGPT_PLUS_PROJECT_INSTRUCTIONS.md` into **Project instructions**.
3. Upload these knowledge files:
   - `references/official-blueprint-summary.md`
   - `references/aif-c01-taxonomy.yaml`
   - `references/taxonomy/d1.yaml` through `d5.yaml`
   - `references/relationship-graph.csv`
   - `references/decision-rules.yaml`
   - `references/question-blueprints.yaml`
   - `references/practice-corpus-analysis.md`
4. Optionally upload `SKILL.md` as an additional reference.
5. Upload your own practice PDFs if you want exact source-question mode.
6. Start with:

```text
Start diagnostic mode. Give me 10 original AIF-C01 questions one at a time. Track my weak concepts and explain every distractor after I answer.
```

ChatGPT Plus Projects currently allow project instructions, persistent project context, and file uploads, making them the closest no-code equivalent for this package.

## Practice modes

The Skill supports:

- **Diagnostic** — identify weak concepts and contrast pairs
- **Practice** — one question at a time with immediate feedback
- **Weak areas** — target demonstrated weaknesses
- **Domain drill** — D1, D2, D3, D4, or D5
- **Contrast drill** — e.g. RAG vs fine-tuning
- **Service selection** — scenario-based AWS service decisions
- **Mock exam** — answers hidden until the end
- **Review** — revisit mistakes and misconceptions
- **Flash** — fast short questions

For generated mixed practice, the long-run domain weights are:

- D1: 20%
- D2: 24%
- D3: 28%
- D4: 14%
- D5: 14%

## High-value decision contrasts

The taxonomy explicitly models distinctions such as:

- RAG vs fine-tuning vs continued pre-training vs distillation
- Bedrock vs SageMaker JumpStart
- prompt engineering vs context engineering
- temperature vs Top-K vs Top-P vs response length
- ROUGE vs BERTScore vs LLM-as-a-judge
- Textract vs Rekognition vs Comprehend
- Ground Truth vs A2I vs RLHF
- CloudTrail vs AWS Config vs Audit Manager vs Trusted Advisor
- AgentCore Runtime vs Gateway vs Identity vs Memory vs Policy
- prompt injection vs jailbreaking vs hijacking vs exposure

The governance four-way distinction was strengthened after student testing exposed a real `AWS Config <-> Trusted Advisor` confusion.

## Validate the repository

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py .
```

Expected result for v1.0.3:

```text
OK: validated aws-ai-practitioner-coach v1.0.3 | 5 domains | 91 graph edges | 30 decision rules | 9 blueprints
```

GitHub Actions runs the same validation on pushes and pull requests.

## Build the Claude Skill ZIP

```bash
python scripts/package_skill.py
```

Output:

```text
dist/aws-ai-practitioner-coach.zip
```

The generated archive includes only runtime Skill files rather than repository/CI setup files.

## Source policy

- Official AWS documentation defines the current blueprint and scope.
- User-supplied practice materials may be used privately as written.
- Generated questions must be original and must not be presented as real AWS exam questions.
- If a practice source appears stale, the tutor preserves the **source answer** and offers **current AWS verification** separately.
- Raw practice accuracy must not be converted directly into the official AWS 100-1000 scaled score.

See `references/SOURCES.md` for the official documentation used to build the package.

## Updating when AWS changes AIF-C01

Update in this order:

1. `references/official-blueprint-summary.md`
2. `references/aif-c01-taxonomy.yaml` and the affected `references/taxonomy/d*.yaml`
3. `references/relationship-graph.csv`
4. `references/decision-rules.yaml`
5. `SKILL.md` only if tutoring behavior changes
6. increment the package version and update `CHANGELOG.md`

## License

No license has been added yet. Until a license is chosen, normal copyright applies to the repository contents.
