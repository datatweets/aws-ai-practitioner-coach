# Manual QA for AWS AI Practitioner Coach

Run these scenarios after a material taxonomy or Skill update.

## 1. Customization strategy contrast

Expected distinctions:

- changing private/current knowledge without weight updates -> RAG / Knowledge Bases for Amazon Bedrock
- labeled input-output examples for task behavior -> fine-tuning
- large unlabeled domain corpus -> continued pre-training
- smaller/faster/cheaper model that approximates a stronger teacher -> distillation

The tutor should not reduce these to one-keyword rules; stems should contain a goal plus at least one decisive constraint.

## 2. Governance four-way contrast

Expected distinctions:

- API calls and user actions -> AWS CloudTrail
- resource configuration state and compliance rules -> AWS Config
- automated evidence collection for audits -> AWS Audit Manager
- cost/performance/security/resilience recommendations -> AWS Trusted Advisor

If a learner confuses AWS Config with Trusted Advisor, the next question should test the same pair from a different scenario before moving to a distant topic.

## 3. Source-question behavior

When a learner supplies a practice PDF and requests an exact question, the tutor should preserve that source's wording/answer intent and should not silently replace it with current AWS knowledge. If asked to verify currency, separate `Source answer` from `Current AWS verification`.

## 4. Mock behavior

A mock should withhold explanations until the end and should never convert raw accuracy directly into the official AWS 100-1000 scaled score.

## 5. Static validation

Run:

```bash
python scripts/validate_skill.py .
```

Then build the Claude upload package:

```bash
python scripts/package_skill.py
```
