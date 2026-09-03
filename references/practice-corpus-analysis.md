# Practice Corpus Analysis

This file summarizes the three user-provided AIF-C01 practice exams without redistributing their full question text.

## Corpus size

- Practice Exam 1: 65 questions
- Practice Exam 2: 65 questions
- Practice Exam 3: 65 questions
- Total indexed questions: **195**

## Domain distribution in the uploaded practice corpus

| Domain | Exam 1 | Exam 2 | Exam 3 | Combined |
|---|---:|---:|---:|---:|
| D1 | 12 | 12 | 12 | 36 |
| D2 | 16 | 16 | 17 | 49 |
| D3 | 19 | 19 | 19 | 57 |
| D4 | 9 | 9 | 8 | 26 |
| D5 | 9 | 9 | 9 | 27 |

The uploaded exams intentionally emphasize D2 and D3. Their title pages also call out revised-objective coverage: Exam 1 says 11 questions, Exam 2 says 9, and Exam 3 says 10 covering newer topics such as MCP, AgentCore, context engineering, distillation, Kiro, Strands, and LLM-as-a-judge.

## Current official weighting to use for generated mixed practice

Use the current AWS blueprint rather than copying the practice-set percentages:

- D1: 20%
- D2: 24%
- D3: 28%
- D4: 14%
- D5: 14%

## Frequently detected concept tags in this corpus

| Concept tag | Indexed questions |
|---|---:|
| `bedrock` | 37 |
| `foundation-model` | 17 |
| `llm` | 13 |
| `agentcore` | 11 |
| `prompt-engineering` | 9 |
| `amazon-q-family` | 8 |
| `fine-tuning` | 8 |
| `rag` | 8 |
| `d1-general` | 7 |
| `supervised-learning` | 6 |
| `model-cards` | 6 |
| `computer-vision` | 6 |
| `embedding-vector` | 6 |
| `reinforcement-learning` | 5 |
| `labeled-vs-unlabeled-data` | 5 |
| `agentcore-gateway` | 5 |
| `d3-general` | 5 |
| `diffusion-model` | 4 |
| `model-dashboard` | 4 |
| `model-distillation` | 4 |
| `unsupervised-learning` | 4 |
| `temperature` | 4 |
| `overfitting-underfitting` | 4 |
| `kiro` | 4 |
| `document-extraction` | 4 |


## Design implications

1. **Do not learn letter patterns.** Correct-option letters are kept only so a tutor can score an explicitly referenced source question.
2. **Use the relationship graph for explanations.** A good explanation identifies the decisive requirement and why plausible distractors fail.
3. **Use official AWS weights for newly generated practice.** The three PDFs are a style/coverage corpus, not the authority for the current blueprint.
4. **Keep current-objective concepts versioned.** AgentCore, MCP, Kiro, Strands, context engineering, distillation, and LLM-as-a-judge are explicitly represented in the taxonomy.
5. **Support official question formats beyond this corpus.** The supplied PDFs use multiple-choice and multiple-response formats; the current AWS guide also lists ordering and matching, so the skill includes original blueprints for those formats.
