# AWS AI Practitioner Coach Skill

An adaptive study skill for **AWS Certified AI Practitioner (AIF-C01)**.

Version: **1.0.2**  
Blueprint: **AIF-C01 v1.1**  
Verified: **2026-09-03**

## What this package does

Instead of learning `keyword -> answer`, the coach learns and teaches:

`question signal -> requirement/constraint -> concept -> relationship -> best answer -> distractor elimination`

The package includes:

- a current AIF-C01 taxonomy,
- a relationship graph,
- explicit decision rules,
- original question-generation blueprints,
- an index derived from 195 questions across the three supplied practice exams,
- adaptive mastery guidance,
- setup instructions for Claude Pro and ChatGPT Plus.

The three source practice PDFs are **not redistributed in this ZIP**. Upload your own copies separately if you want the coach to use those exact questions.

---

# 1. Folder structure

```text
aws-ai-practitioner-coach/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── CHATGPT_PLUS_PROJECT_INSTRUCTIONS.md
├── CLAUDE_PRO_QUICK_SETUP.md
├── .gitignore
├── .github/
│   └── workflows/
│       └── validate.yml
├── docs/
│   └── TESTING.md
├── references/
│   ├── SOURCES.md
│   ├── official-blueprint-summary.md
│   ├── aif-c01-taxonomy.yaml
│   ├── relationship-graph.csv
│   ├── decision-rules.yaml
│   ├── question-blueprints.yaml
│   ├── practice-corpus-index.csv
│   └── practice-corpus-analysis.md
├── templates/
│   ├── student-state.yaml
│   └── session-report.md
└── scripts/
    ├── mastery.py
    ├── package_skill.py
    └── validate_skill.py
├── requirements-dev.txt
```

---

# 2. Publish this project on GitHub

Recommended repository name:

`aws-ai-practitioner-coach`

For a public educational repository, create an empty GitHub repository with that name and **do not initialize it with a README, .gitignore, or license**, because this package already contains the files that should form the first commit.

After the repository exists, upload/commit the complete contents of this folder to the repository root. The included GitHub Actions workflow runs `scripts/validate_skill.py` on every push and pull request.

The project intentionally does **not** include the three source practice-exam PDFs. Do not add them to a public repository unless you own redistribution rights. Learners should upload their own lawful copies privately to Claude or ChatGPT when they want exact source-question practice.

To validate and build a Claude-uploadable ZIP after cloning the repository, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py .
python scripts/package_skill.py
```

This creates:

```text
dist/aws-ai-practitioner-coach.zip
```

with the required root-folder structure for a custom Claude Skill. The generated archive intentionally contains only runtime Skill files (`SKILL.md`, references, templates, and the mastery helper), not GitHub CI or setup-only files.

---

# 3. Claude Pro - native Skill setup

Claude Pro currently supports custom Skills directly.

## Step 1 - Enable the required capability

In Claude:

1. Open **Settings**.
2. Open **Capabilities**.
3. Turn on **Code execution and file creation**.

Claude Skills require this capability.

## Step 2 - Upload the Skill

Use the ZIP provided with this package.

1. Go to **Customize -> Skills**.
2. Click **+**.
3. Choose **Create skill**.
4. Choose **Upload a skill**.
5. Upload `aws-ai-practitioner-coach.zip`.
6. Ensure **AWS AI Practitioner Coach** is enabled/toggled on.

The ZIP is structured according to the Agent Skills standard: the archive contains a root folder named `aws-ai-practitioner-coach`, and that folder contains `SKILL.md`.

## Step 3 - Recommended: create a Claude Project for your study

The Skill defines the tutoring workflow. A Project is useful for keeping your study material and conversations together.

Create a project named something like:

`AWS AIF-C01 Study`

Then add your legally obtained study material, especially the three source PDFs if you want exact source-question practice:

- `AIF-C01-practice-exam-1.pdf`
- `AIF-C01-practice-exam-2.pdf`
- `AIF-C01-practice-exam-3.pdf`

The Skill itself does not bundle those PDFs.

## Step 4 - Test the Skill

Try:

```text
Start AIF-C01 diagnostic mode. Give me 10 questions, one at a time.
```

Then:

```text
Give me a contrast drill on RAG vs fine-tuning vs continued pre-training.
```

Then test source mode:

```text
Use Practice Exam 1. Ask me question 23 but do not show the answer until I respond.
```

## Step 5 - Check triggering

If Claude does not use the Skill:

- confirm it is enabled under **Customize -> Skills**,
- confirm Code execution and file creation is enabled,
- explicitly say: `Use my AWS AI Practitioner Coach skill`,
- keep the source PDFs in the same Claude Project or attach them to the chat when using source-question mode.

---

# 4. ChatGPT Plus - Project compatibility setup

## Important current limitation

As of 2026-09-03, **native ChatGPT Skills are not available on personal ChatGPT Plus**. OpenAI currently documents native Skills for eligible Business, Enterprise, Healthcare, and Edu users.

Also, new custom GPT creation is not currently available on personal Plus accounts.

For Plus, the best no-code equivalent is a **ChatGPT Project** containing the Skill's instructions and reference files.

Projects are available to Plus users and can keep project files, instructions, and related chats together.

## Step 1 - Create the Project

1. In the ChatGPT sidebar, choose **New project**.
2. Name it:

   `AWS AIF-C01 Coach`

3. If ChatGPT offers a memory choice, **Project-only memory** is recommended for a clean study environment. This keeps the exam coach focused on study-project context.

## Step 2 - Add Project instructions

Open:

`CHATGPT_PLUS_PROJECT_INSTRUCTIONS.md`

Copy its entire contents into the project's **Project instructions**.

Do not paste the large taxonomy into the instruction box. Keep knowledge in files and behavior in Project instructions.

## Step 3 - Upload the knowledge files

Unzip the package locally and upload these files to the Project:

1. `references/official-blueprint-summary.md`
2. `references/aif-c01-taxonomy.yaml`
3. `references/relationship-graph.csv`
4. `references/decision-rules.yaml`
5. `references/question-blueprints.yaml`
6. `references/practice-corpus-index.csv`
7. `references/practice-corpus-analysis.md`

You may also upload `SKILL.md` as a reference, but the **Project instructions** are the primary behavior instructions in ChatGPT Plus.

## Step 4 - Add your practice PDFs

If you want the coach to ask the exact questions in your practice material, upload your own copies of the three PDFs to the Project.

Without the PDFs, the coach will still work: it can generate original questions from the taxonomy and decision rules.

## Step 5 - Start a first chat inside the Project

Use:

```text
Start diagnostic mode. Give me 10 original AIF-C01 questions one at a time. Track my weak concepts and explain every distractor after I answer.
```

A good second prompt is:

```text
Now give me a service-selection drill. Focus on AWS services that are easy to confuse.
```

And for source mode:

```text
Use Practice Exam 2. Ask me Q46. Do not reveal the answer before I respond.
```

## Step 6 - Continue studying in the same Project

For ChatGPT Plus, staying inside the same Project is important because project chats and files provide continuity. Ask periodically:

```text
Show my current weak concepts and choose the next 10 questions adaptively.
```

---

# 5. Recommended learning workflow

## Phase A - Diagnostic

Run 15-20 mixed questions.

Goal: identify weak domains and, more importantly, weak **contrast pairs**.

Examples:

- RAG vs fine-tuning
- Bedrock vs JumpStart
- Textract vs Rekognition
- CloudTrail vs Config
- Ground Truth vs A2I vs RLHF
- AgentCore Runtime vs Gateway vs Identity vs Policy

## Phase B - Contrast drills

Do 5-10 questions on one confusing relationship at a time.

The tutor should explain the **decisive clue**, not merely define both services.

## Phase C - Domain drills

Study D1-D5 separately until the coach stops seeing repeated misconceptions.

## Phase D - Mixed adaptive practice

Let the coach select questions based on weak concepts while approximately following official long-run weights:

- D1 20%
- D2 24%
- D3 28%
- D4 14%
- D5 14%

## Phase E - Mock exam

Ask for an exam-like set with explanations withheld until the end.

The current official AWS guide can include:

- multiple choice,
- multiple response,
- ordering,
- matching.

The uploaded practice PDFs mainly model multiple-choice and multiple-response questions, so this skill generates original ordering and matching items from the taxonomy.

---

# 6. Answer format

You can answer simply:

```text
B
```

or include confidence:

```text
B sure
```

```text
B unsure
```

```text
B guess
```

Confidence helps distinguish a knowledge gap from a lucky guess.

---

# 7. Useful commands/prompts

```text
Start diagnostic mode.
```

```text
Give me 10 D3 questions, one at a time.
```

```text
Drill RAG vs fine-tuning until I can distinguish them reliably.
```

```text
Give me difficult AgentCore, MCP, Strands, and Kiro questions.
```

```text
Give me only AWS service-selection scenarios.
```

```text
Review every concept I answered incorrectly today.
```

```text
Run a 20-question mock and do not explain anything until the end.
```

```text
Give me a matching question for CloudTrail, Config, Audit Manager, and Trusted Advisor.
```

```text
Use my uploaded Practice Exam 3, but ask questions in random order and hide the answers until I respond.
```

---

# 8. Updating the Skill when AWS changes the exam

Do not rewrite everything.

Update these files in order:

1. `references/official-blueprint-summary.md`
2. `references/aif-c01-taxonomy.yaml`
3. `references/relationship-graph.csv`
4. `references/decision-rules.yaml`
5. `SKILL.md` only if the tutoring workflow itself changes

Increment the package version and record the new AWS blueprint date/version.

---

# 9. Validation

From a terminal, optional:

```bash
python scripts/validate_skill.py ./aws-ai-practitioner-coach
```

You should see:

```text
OK: skill structure and core references validated
```

The package is intentionally usable without scripts. Markdown/YAML/CSV files contain the core logic so it remains portable.

---

# 10. Content and source policy

- The source PDFs supplied by the learner are used as a private study corpus.
- The package does not redistribute their full question text.
- `practice-corpus-index.csv` stores an index and short answer summaries for taxonomy mapping.
- Newly generated questions should be original, not close paraphrases of the practice corpus.
- If a source practice answer conflicts with current AWS documentation, the tutor should distinguish **source answer** from **current verification**, not silently overwrite the source.

---

# 11. Why the taxonomy matters

The core asset is not `SKILL.md` itself. It is the reasoning layer:

```text
Exam domain
  -> task statement
    -> concept
      -> question signal
        -> requirement / constraint
          -> relationship
            -> correct service or concept
              -> distractor contrast
                -> misconception
```

That structure lets the same knowledge base power Claude, ChatGPT, a web app, flashcards, course quizzes, or a future adaptive exam-prep platform.
