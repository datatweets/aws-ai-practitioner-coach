# Claude Pro Setup — AWS AI Practitioner Coach

You do **not** need Python or coding.

## 1. Download the fixed Skill ZIP

Download [`downloads/aws-ai-practitioner-coach.zip`](downloads/aws-ai-practitioner-coach.zip) from this repository.

If an older ZIP failed to upload, delete it and use this new package. It follows Claude's documented structure:

```text
aws-ai-practitioner-coach.zip
└── aws-ai-practitioner-coach/
    ├── skill.md
    ├── references/
    ├── templates/
    └── scripts/
```

## 2. Enable Claude Skills

In Claude:

1. Open **Settings**.
2. Open **Capabilities**.
3. Turn on **Code execution and file creation**.
4. Go to **Customize → Skills**.

## 3. Upload the Skill

1. Click **+**.
2. Choose **Create skill**.
3. Choose **Upload a skill**.
4. Upload `aws-ai-practitioner-coach.zip`.
5. Make sure the Skill is enabled.

## 4. Add the Three Practice Exams

Create a Claude Project called `AWS AIF-C01 Study` and upload:

- `practice-exams/AIF-C01-practice-exam-1.pdf`
- `practice-exams/AIF-C01-practice-exam-2.pdf`
- `practice-exams/AIF-C01-practice-exam-3.pdf`

## 5. Start Practicing

```text
Use my AWS AI Practitioner Coach skill.
Start a 10-question beginner diagnostic.
Ask one question at a time.
```

Or:

```text
Use Practice Exam 1 and quiz me from it one question at a time.
```

See the main [README](README.md) for more practice prompts and explanations.
