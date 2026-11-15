# 6. AI, DevOps and PRINCE2

## Learning goals

Explain useful AI applications and their limits; distinguish governance from technical evaluation; explain how complementary approaches can coexist with service management.

## 6.1 AI without magical thinking

Artificial intelligence covers systems that perform tasks associated with intelligent behavior. Machine learning learns patterns from data. Generative AI produces new outputs from learned patterns and a prompt or context. A plausible answer is not automatically a correct answer, and successful demonstrations do not prove dependable performance across all users.

Harbour could use AI to suggest support responses, classify requests or find relevant knowledge. Begin with a specific problem and evaluate it against a non-AI alternative. Consider whether the proposed benefit outweighs errors, oversight effort, privacy risk, cost and supplier dependence.

Different deployments require different controls. Suggesting an answer for a trained operator is not equivalent to changing a learner's grade autonomously. Define permitted actions, human review, escalation, monitoring and a way to stop use when performance is unacceptable.

## 6.2 Governance and capability

AI governance establishes accountability and boundaries for responsible use. Capability involves more than acquiring a model: people need competence, data needs stewardship, evaluation needs representative cases, and operations need monitoring and incident handling. Assess the current capability before claiming maturity. This course does not invent the names or scoring rules of an official AI capability model; consult the licensed Version 5 materials for those exact details.

Evaluation should test accuracy, usefulness, fairness and harmful failure modes. Include unusual inputs, missing context and changes over time. Protect personal data and intellectual property; do not place confidential learner records into an unapproved service. Keep records of decisions at an appropriate level without collecting unnecessary sensitive content.

## Worked example

Harbour proposes an AI support assistant. Start with approved knowledge retrieval and draft suggestions, with staff reviewing responses. Test against a representative anonymized question set, including questions for which the correct response is escalation. Measure unsupported claims, resolution quality, staff review effort and learner experience. A faster response that invents a refund policy is not an improvement.

## 6.3 DevOps as a complementary approach

DevOps emphasizes collaboration, shared responsibility, feedback and automation across development and operations. It can support shorter feedback cycles and dependable delivery. Service management adds context for value, relationships, practices and governance; the approaches need not be opposing camps.

An automated pipeline can provide repeatable evidence for change decisions. It does not remove accountability or guarantee security. Teams should agree what the pipeline verifies, what it cannot verify, and how failures or exceptions are handled.

## 6.4 PRINCE2 as a complementary approach

PRINCE2 addresses structured project management. A project can organize a time-bound initiative, while product and service management continue through ongoing use and improvement. Harbour's new assessment capability may be delivered through a project, but support, reliability, supplier management and outcome evaluation continue after the project ends.

Avoid conflating project completion with service success. A project can deliver agreed outputs while consumers fail to obtain intended benefits. Plan transition, responsibility and measurement before closing the initiative.

## Exercise

Write a proposal for an AI assistant that includes an outcome, permitted use, prohibited use, evidence needed, accountable owner and a stopping condition. Then explain where DevOps and project management could contribute.

**Model reasoning:** A good proposal bounds behavior and tests meaningful failure cases. DevOps can support versioned evaluation and repeatable deployment; project management can coordinate a time-bound introduction; service management sustains relationships, support and improvement. No framework by itself demonstrates that the AI is safe or useful.
