# 4. Delivery, operations, practices and continual improvement

## Learning goals

Distinguish recurring management capabilities from isolated activities. Explain how restoration, investigation, change, deployment and release interact. Design an improvement that can be evaluated.

## 4.1 Practices as capabilities

A practice combines resources needed to accomplish a kind of work. It includes people, knowledge, responsibilities, methods and tools; it is more than a process diagram. A detailed practice manual belongs in advanced learning, not an unsupported claim that Foundation teaches every specialist procedure.

An operating model explains how capabilities, accountabilities, teams, suppliers and decision rights work together. Product-oriented teams may own a service throughout its lifecycle; centralized capabilities may support many teams. Neither label guarantees effectiveness. Evaluate handoffs, expertise and outcomes.

## 4.2 A disruption from several perspectives

Learners cannot submit assignments. **Incident management** concentrates on restoring normal service and reducing disruption. A temporary alternate submission route may be appropriate before the underlying cause is understood.

**Problem management** investigates causes and reduces recurrence or impact. Restoration does not prove that the cause has been eliminated. Preserve evidence and distinguish an accepted workaround from a permanent correction.

**Monitoring and event management** helps detect meaningful changes in state and decide what needs attention. Alerting on every technical fluctuation can overwhelm responders; prioritize signals linked to meaningful service impact.

A routine access request is not automatically an incident. A security concern may require specialized handling beyond ordinary restoration. Classification should help route work, not become an argument that delays assistance.

## 4.3 Change, deployment and release

A **change** alters something that can affect a service. Change enablement supports appropriate assessment, authorization and coordination. **Deployment** moves components into an environment. **Release** makes new or changed functionality available for use. A feature may be deployed but not released to learners until training and support are ready.

For Harbour, turning on an assessment feature for everyone is different from installing its code behind a disabled feature flag. A successful installation does not demonstrate that the service is ready or that a rollback would restore the intended state.

Use proportionate controls. Consider impact, dependencies, uncertainty, observability and recovery arrangements. A tested routine change can follow a repeatable path; unusual high-impact changes need additional review. “Agile” is not permission to conceal uncertainty.

## 4.4 CI/CD, SRE and observability

Continuous integration promotes frequent integration and automated checks. Continuous delivery keeps changes in a releasable condition; continuous deployment automates production release under defined conditions. Terminology and implementation should be stated explicitly rather than assuming every pipeline deploys automatically.

Site reliability engineering applies engineering approaches to reliable operation. Service-level indicators describe performance; objectives set targets. Error-budget thinking helps balance reliability work and change, but a numerical target must reflect user needs and be supported by trustworthy measurement.

Observability helps infer internal behavior from emitted signals such as metrics, logs and traces. Collecting more logs is not the same as being able to answer an operational question. Avoid sensitive data in telemetry and define how evidence supports decisions.

## 4.5 Continual improvement

Improvement should connect the desired future to the current situation and a measurable action. A practical reasoning sequence is: articulate the ambition, understand the current state, define the target, plan and perform an improvement, evaluate the result, and sustain learning. Treat this as an original teaching scaffold rather than a quotation of a proprietary model.

Harbour's improvement record might say:

- Outcome: learners submit assessments without avoidable disruption.
- Current evidence: 6% of attempts fail during peak periods in a representative sample.
- Target: an agreed lower failure rate under comparable conditions.
- Hypothesis: reducing a bottleneck will improve successful completion.
- Action: a bounded experiment with monitoring and a recovery plan.
- Evaluation: compare failure rate, workload and learner experience, including unintended effects.
- Follow-through: keep, revise or stop the change; update knowledge and ownership.

These figures are fictional training data, not production evidence. Distinguish the target from a result already achieved.

## Exercise

The service desk closes tickets quickly but learners reopen them. Propose measures and an improvement without rewarding premature closure.

**Model reasoning:** Examine first-contact resolution quality, reopen rate, time until the learner can continue and feedback. Sample cases to understand causes. Improve knowledge or escalation and compare outcomes, not just closure speed. Protect privacy in case analysis.
