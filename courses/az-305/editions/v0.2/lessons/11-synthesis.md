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

## Complete fictional decision record
The following numbers are invented design inputs, not observations or Azure guarantees: 200 peak requests per second; a 95th-percentile interactive target of 500 milliseconds; 30-minute recovery time; five-minute tolerated data-loss window; weekly reporting refreshed within 24 hours; and a small team without Kubernetes operating experience.

**Selected candidate architecture:** App Service for the supported stateless web runtime; Azure SQL Database for transactional booking; Blob Storage for documents; Service Bus for durable notification work; Key Vault for unavoidable secrets; workload identities where supported; Application Insights and platform logs for correlated operational evidence. A global edge is considered only if global delivery requirements justify it. Exact service tiers and regions remain subject to compatibility, cost and performance verification.

**Rejected alternatives:** AKS adds unjustified platform responsibility for this workload. Placing documents in the transactional database would couple binary-asset lifecycle to transaction performance without a demonstrated need. Treating Event Hubs as the notification work queue would choose a stream abstraction for a command-processing requirement. Querying live transactions for every weekly report would mix tolerant analytics with latency-sensitive work.

**Failure story:** if a regional outage occurs, application and data recovery must be coordinated. The RTO allocation is not sufficient evidence of success. If a faulty release overwrites data, a regional replica alone does not recover historical truth. If identity or key access fails, otherwise healthy compute may still be unusable. Each failure story therefore names a different mechanism and a different acceptance condition.

**Cost model:** estimate compute baseline and scale-out, database capacity, replicated storage, request volume, log ingestion/retention, networking and any secondary-region standby. No currency total is asserted without current region/SKU prices and workload quantities. A two-region design may cost more but still be justified; the decision needs the value of recovery, not a slogan about cost optimization.

**Outstanding evidence:** representative performance results, current price calculation, region/SKU compatibility, supported recovery configuration and organization-specific security review. These are implementation validation needs outside this instructional edition, not omitted course labs. The course demonstrates how to reach and document a design decision without pretending that a written architecture is already a validated service.
