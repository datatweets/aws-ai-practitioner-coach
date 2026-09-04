<p align="center">
  <img src="assets/aws-certified-ai-practitioner-foundational.png" alt="AWS Certified AI Practitioner Foundational badge" width="250">
</p>

<h1 align="center">AWS AI Practitioner Exam Coach — AIF-C01</h1>

<p align="center">
  <strong>Practice AWS Certified AI Practitioner (AIF-C01) with Claude or ChatGPT.</strong><br>
  Beginner-friendly questions, three practice exams, weak-area drills, service comparisons, and plain-English explanations.
</p>

<p align="center">
  <a href="https://datatweets.com/">DataTweets.com</a> ·
  <a href="#start-here--3-simple-steps">Start Here</a> ·
  <a href="#use-with-claude-pro">Claude Pro</a> ·
  <a href="#use-with-chatgpt-plus">ChatGPT Plus</a> ·
  <a href="#download-the-3-practice-exams">Practice Exams</a>
</p>

<p align="center">
  <img alt="AWS AIF-C01" src="https://img.shields.io/badge/AWS-AIF--C01-FF9900?style=flat-square">
  <img alt="Beginner Friendly" src="https://img.shields.io/badge/Beginner-Friendly-22C55E?style=flat-square">
  <img alt="Claude Pro" src="https://img.shields.io/badge/Claude-Pro-7C3AED?style=flat-square">
  <img alt="ChatGPT Plus" src="https://img.shields.io/badge/ChatGPT-Plus-111827?style=flat-square">
</p>

> [!IMPORTANT]
> **Students do not need Python, coding, Git, or a terminal.** Download the files, add them to Claude or ChatGPT, and start practicing.

---

## What is this?

This repository turns Claude or ChatGPT into an adaptive study coach for the **AWS Certified AI Practitioner (AIF-C01)** exam.

Instead of memorizing `keyword → answer`, the coach teaches a reusable decision process:

**question clue → requirement → concept/service → best answer → why the other choices are wrong**

It can:

- ask AIF-C01 practice questions one at a time,
- use the three included 65-question practice exams,
- generate original practice questions,
- explain every answer in plain English,
- detect weak topics and repeat them intelligently,
- drill confusing AWS services and concepts,
- run mock exams,
- track misconception patterns such as **AWS Config vs Trusted Advisor** or **RAG vs fine-tuning**.

### Who is it for?

- Complete beginners to AWS AI
- Students preparing for the AIF-C01 exam
- Professionals who need a fast refresher
- Trainers who want an AI-assisted practice workflow
- Learners who prefer interactive questions over passive reading

---

## Start Here — 3 Simple Steps

<table>
<tr>
<td align="center" width="33%"><img src="assets/step-download.svg" width="72"><br><strong>1. Download</strong><br>Get the Claude Skill ZIP or the repository files.</td>
<td align="center" width="33%"><img src="assets/step-chat.svg" width="72"><br><strong>2. Add to AI</strong><br>Upload the Skill to Claude or create a ChatGPT Project.</td>
<td align="center" width="33%"><img src="assets/step-practice.svg" width="72"><br><strong>3. Practice</strong><br>Start a diagnostic, domain drill, or mock exam.</td>
</tr>
</table>

---

## Download the 3 Practice Exams

Each practice exam contains **65 questions** and an answer/explanation section.

| Practice exam | Questions | Download |
|---|---:|---|
| Practice Exam 1 | 65 | [Open / download Exam 1](practice-exams/AIF-C01-practice-exam-1.pdf) |
| Practice Exam 2 | 65 | [Open / download Exam 2](practice-exams/AIF-C01-practice-exam-2.pdf) |
| Practice Exam 3 | 65 | [Open / download Exam 3](practice-exams/AIF-C01-practice-exam-3.pdf) |

Together they provide **195 AWS AI Practitioner practice questions** across all five AIF-C01 domains.

You can study the PDFs normally or upload them to Claude/ChatGPT and ask the coach to quiz you from them.

---

## Use with Claude Pro

Claude supports custom Skills. This is the easiest setup.

### Step 1 — Download the fixed Claude Skill ZIP

**[Download `aws-ai-practitioner-coach.zip`](downloads/aws-ai-practitioner-coach.zip)**

> [!NOTE]
> If an older ZIP gave you an upload error, use the current ZIP above. It follows Anthropic's documented structure:
>
> ```text
> aws-ai-practitioner-coach.zip
> └── aws-ai-practitioner-coach/
>     ├── skill.md
>     ├── references/
>     ├── templates/
>     └── scripts/
> ```
>
> The folder name matches the Skill name, and the Skill metadata uses only the required `name` and `description` fields.

### Step 2 — Enable Skills in Claude

1. Open **Settings**.
2. Open **Capabilities**.
3. Turn on **Code execution and file creation**.
4. Go to **Customize → Skills**.

You do not need to write code. Claude uses this capability internally for Skills.

### Step 3 — Upload the Skill

1. Click **+**.
2. Choose **Create skill**.
3. Choose **Upload a skill**.
4. Upload `aws-ai-practitioner-coach.zip`.
5. Make sure the Skill is enabled.

### Step 4 — Add the practice exams

Create a Claude Project called:

`AWS AIF-C01 Study`

Upload the three PDFs from `practice-exams/`.

### Step 5 — Start practicing

```text
Use my AWS AI Practitioner Coach skill.
Start a 10-question beginner diagnostic.
Ask one question at a time and track my weak topics.
```

Or:

```text
Use Practice Exam 1.
Ask me question 1, but do not reveal the answer until I respond.
```

For a shorter setup guide, see [`CLAUDE_PRO_QUICK_SETUP.md`](CLAUDE_PRO_QUICK_SETUP.md).

---

## Use with ChatGPT Plus

For a personal ChatGPT Plus account, use a **Project** to keep instructions, files, and study chats together.

### Step 1 — Create a Project

Create a project named:

`AWS AIF-C01 Coach`

### Step 2 — Add the coach instructions

Open [`CHATGPT_PLUS_PROJECT_INSTRUCTIONS.md`](CHATGPT_PLUS_PROJECT_INSTRUCTIONS.md) and copy its contents into your Project instructions.

### Step 3 — Upload the knowledge files

Upload these from `references/`:

- `official-blueprint-summary.md`
- `aif-c01-taxonomy.yaml`
- `taxonomy/d1.yaml` through `taxonomy/d5.yaml`
- `relationship-graph.csv`
- `decision-rules.yaml`
- `question-blueprints.yaml`

### Step 4 — Upload the three practice exams

Upload the PDFs from `practice-exams/`.

### Step 5 — Start practicing

```text
Start AWS AI Practitioner diagnostic mode.
Give me 10 questions one at a time.
After each answer, explain the decisive clue, the correct answer, and why every distractor is wrong.
Track my weak topics.
```

---

## How the coach helps you reason

The Skill uses a taxonomy, relationship graph, and decision rules to recognize what a question is really testing.

| If the question says... | Think about... |
|---|---|
| Current/private information without retraining | RAG / Knowledge Bases for Amazon Bedrock |
| Labeled examples to teach behavior or output style | Fine-tuning |
| Large unlabeled domain corpus | Continued pre-training |
| Smaller/faster/cheaper model that keeps teacher behavior | Model distillation |
| API activity and who did what | AWS CloudTrail |
| Resource configuration and compliance state | AWS Config |
| Collect audit evidence | AWS Audit Manager |
| Best-practice recommendations | AWS Trusted Advisor |

The goal is to learn **decision rules**, not just remember answer letters.

---

## Practice ideas

### Beginner diagnostic

```text
I am a beginner. Give me 15 mixed AIF-C01 questions one at a time and explain each answer simply.
```

### Weak-area practice

```text
Review my mistakes and give me new questions only on my weakest concepts.
```

### Bedrock and Generative AI

```text
Drill me on Amazon Bedrock, Knowledge Bases, Guardrails, Agents, RAG, and model customization.
```

### Difficult contrasts

```text
Give me difficult comparison questions on RAG vs fine-tuning vs continued pre-training vs distillation.
```

### Governance services

```text
Drill CloudTrail vs AWS Config vs Audit Manager vs Trusted Advisor until I stop confusing them.
```

### Full mock

```text
Run a 65-question AIF-C01-style mock exam. Do not give explanations until the end.
```

---

## AIF-C01 topics covered

The coach covers the five AWS Certified AI Practitioner domains:

1. **Fundamentals of AI and ML**
2. **Fundamentals of Generative AI**
3. **Applications of Foundation Models**
4. **Guidelines for Responsible AI**
5. **Security, Compliance, and Governance for AI Solutions**

Topics include AI/ML basics, supervised and unsupervised learning, foundation models, transformers, embeddings, Amazon Bedrock, SageMaker, RAG, fine-tuning, continued pre-training, distillation, prompting, responsible AI, Guardrails, IAM, CloudTrail, Config, Audit Manager, AgentCore, MCP, Kiro, Strands, and more.

---

## Beginner FAQ

### Do I need Python?

**No.** Students do not need Python or any local coding setup.

### Do I need AWS experience?

No. The coach can begin at a beginner level and increase difficulty as you improve.

### Are the practice exams included?

Yes. See the [`practice-exams/`](practice-exams/) folder.

### Can the coach explain why I am wrong?

Yes. It explains the decisive clue, why the correct option fits, why the distractors fail, and a rule you can reuse on future questions.

### Is this an official AWS product?

No. This is an independent educational project for AWS AI Practitioner exam preparation.

---

## Learn more with DataTweets

This project is part of the learning resources from **[DataTweets.com](https://datatweets.com/)**.

DataTweets publishes practical learning material in:

- Artificial Intelligence and Generative AI
- Data Science and Machine Learning
- Data Engineering
- AWS and cloud technologies
- Analytics
- SQL, Python, dbt, Terraform, and modern data tools

**[Visit DataTweets.com](https://datatweets.com/)**

---

## AWS AI Practitioner exam prep

This repository is designed for learners searching for **AWS AI Practitioner practice exams**, **AIF-C01 practice questions**, **AWS Certified AI Practitioner study guides**, **AWS AI Practitioner mock exams**, **Amazon Bedrock exam practice**, **Claude AWS certification Skills**, **ChatGPT AWS AI Practitioner study projects**, and **AIF-C01 exam preparation for beginners**.

---

## For maintainers and contributors only

> Students can stop reading here.

The repository contains small Python utilities for validating and rebuilding the Skill package. They are not required for studying.

```bash
python -m pip install -r requirements-dev.txt
python scripts/package_skill.py
python scripts/validate_skill.py .
```

The packager creates the ready-to-upload Claude ZIP in both `dist/` and `downloads/` using the required `aws-ai-practitioner-coach/skill.md` layout.

---

## Repository structure

```text
aws-ai-practitioner-coach/
├── README.md
├── SKILL.md
├── CLAUDE_PRO_QUICK_SETUP.md
├── CHATGPT_PLUS_PROJECT_INSTRUCTIONS.md
├── assets/
├── downloads/
├── practice-exams/
├── references/
├── templates/
├── scripts/
└── .github/
```

---

## Disclaimer

This is an independent educational resource and is **not affiliated with or endorsed by Amazon Web Services (AWS)**. AWS, Amazon Bedrock, Amazon SageMaker, AWS Certified, and related names and marks are trademarks or certification marks of Amazon.com, Inc. or its affiliates.

The AWS Certified AI Practitioner badge shown in this repository is used only to identify the certification targeted by this independent study project.
