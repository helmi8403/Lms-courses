# Synthesis: a defensible architecture decision

**Learning purpose:** Integrate the course into an original worked example without claiming a deployed or validated system.

## Fictional architecture brief
Contoso’s appointment service requires authenticated staff access, public appointment browsing, durable booking records, uploaded documents and asynchronous notifications. Its architecture must explain operational ownership, data protection, continuity and cost. The following is an illustrative design narrative, not a deployment prescription or a tested reference implementation.

## Identity and governance decision
Separate staff identity from workload identity. Give the application only the permissions needed for its data path. Organize resources by lifecycle and policy boundary, and record owners. Evaluate governance controls against specific outcomes: who can deploy, which configurations are allowed, how exceptions expire and how access is reviewed.

## Data and compute decision
Use a relational model for booking consistency, object storage for uploaded assets and a separate analytical path when reporting would distort transaction performance. Select a managed compute option if it fits runtime requirements and the team’s ability to operate it. Keep a VM exception only for an actual compatibility need. Record where application state lives so scaling does not silently lose it.

## Integration and networking decision
Asynchronous notifications remove a slow downstream provider from the booking response path, but require duplicate-safe processing and backlog handling. The edge and private data path have separate controls. A diagram shows region, trust boundary and traffic direction, while a companion table states protocol, identity and expected access.

## Continuity decision
Choose resilience and recovery patterns from agreed recovery objectives. Document what happens when a zone, region, identity dependency or data path fails. Separate restored infrastructure from validated service recovery. A prior deployment artifact is a rollback candidate, not proof that rollback is safe after a schema change.

## Operations and decision record
The design contains an architecture decision record for each significant choice: context, requirements, alternatives, selected option, consequences, validation evidence still needed and review trigger. It also names the information that remains unknown. An explicit unknown is more useful than an invented assurance.

In a real project, deployment, cost commitment and access changes require their own authorization. Nothing in this course creates resources or validates a live tenant. The deliverable is architectural understanding and a traceable explanation of choices.
