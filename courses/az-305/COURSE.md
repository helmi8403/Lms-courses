# AZ-305: Designing Azure Infrastructure Solutions

Independent original course · 15 November 2026 · Draft 1

No practice exams, videos or labs in this edition. Worked examples are fictional instructional explanations.

# 00. Pilot: the exam and the architect’s job

**Learning purpose:** Understand the credential route, the scope of AZ-305 and how to reason about design before choosing a product.

## Course status and boundaries
This is an independently authored learning course, not Microsoft Official Curriculum and not an accredited training product. It explains architectural choices through original fictional examples. Public Microsoft documentation is the authority for product behavior. There are no exam dumps, practice-exam questions, videos or labs in this edition. Worked examples illustrate reasoning; they are not claims about actual examination content.

The verified study guide is the edition with skills measured from 17 April 2026. Its four weighted areas are identity, governance and monitoring (25–30%); data storage (20–25%); business continuity (15–20%); and infrastructure (30–35%). These weights guide study allocation, not a promise about a particular examination’s item distribution. [S01: AZ-305 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305)

## Exam essentials
AZ-305 is Designing Microsoft Azure Infrastructure Solutions. Passing it alone does not award Azure Solutions Architect Expert: Microsoft also requires the Azure Administrator Associate certification. The published passing score is 700 on a scaled score, not a statement that 70% of questions must be correct. Price depends on the country or region in which the exam is proctored; check the booking flow rather than budgeting from a foreign-currency quotation. [S02: AZ-305 exam](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-305/) [S03: Azure Solutions Architect Expert](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/) [S04: Exam scoring](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports)

Do not plan around an asserted fixed question count. Microsoft’s generic role-based examination policy distinguishes 100-minute non-lab exams from 120-minute exams that may contain labs; booking time also includes other activities. The AZ-305 page does not settle which applies to a future appointment. Confirm the actual appointment, permitted aids, accommodations and local identification rules before scheduling. Course videos, labs and practice exams are excluded at the owner’s request; the pilot still explains the exam. [S05: Exam duration and experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience)

## What an architect produces
An architect translates an ambiguous request into a defensible decision. “Make it fast and resilient” is not a measurable requirement. A useful design brief identifies the user journey, peak demand, acceptable latency, data sensitivity, recovery time, tolerated data loss, ownership and cost ceiling. A design decision then records the alternatives, the reason for the chosen option, its failure modes and the evidence that would invalidate it.

Azure Well-Architected Framework provides five lenses: reliability, security, cost optimization, operational excellence and performance efficiency. These lenses reveal tradeoffs. A second live region may improve continuity while increasing cost and reconciliation complexity. Cloud Adoption Framework complements workload design with organizational adoption and operating considerations. [S06: Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)

## Worked example: Contoso appointment booking
Contoso’s fictional booking application serves clinics across two regions. The initial request is “always available.” The architect instead documents: booking writes must not be duplicated; viewing appointment availability can tolerate stale data; staff need a clear degraded-mode procedure; and an outage must have an accountable incident owner. This separates the availability of a screen from the correctness of a transaction.

The design is deliberately incomplete until stakeholders specify targets. Choosing a multi-region database before resolving conflicting-write behavior would conceal a business decision inside technology. The teaching point is to identify the missing requirement explicitly, not fill it with an invented service-level promise.

## Reading sequence
Start with identity and governance, then observability, storage, continuity, compute, integration, networking and migration. Revisit earlier decisions after later chapters: network isolation changes monitoring access; database recovery changes application behavior; deployment design changes rollback safety. Each chapter ends in a worked design note rather than an assessment.

---

# 01. Identity and authorization: separate the gates

**Learning purpose:** Distinguish identity proof, permission, privileged access and secret management across Azure and hybrid systems.

## Authentication is not authorization
Authentication establishes an identity; authorization determines what that identity may do. A successful sign-in is not proof that an application can read a database or change a resource. Human access, workload access and customer access have different lifecycle and risk requirements. Design each deliberately rather than using an administrator account as a universal credential.

Azure RBAC binds a principal to a role at a scope. Prefer the narrowest scope and capabilities that satisfy a real task. A management-plane role and a data-plane role are not interchangeable: operating a storage resource is a different concern from reading its stored content. Also account for inherited assignments when explaining effective access. [S07: Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

## Workloads and managed identities
A managed identity lets supported Azure workloads acquire Microsoft Entra tokens without application teams managing a password or secret. A system-assigned identity shares the resource lifecycle; a user-assigned identity can have an independent lifecycle and be associated with resources. Neither grants access by itself: the target must support the authentication mechanism and the identity still needs appropriate authorization. [S08: Managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)

An architect checks how identity behaves during replacement, scaling and recovery. A tightly coupled identity can simplify ownership but complicate resource replacement. A shared identity can simplify deployment but enlarge the impact of a mistaken permission. Avoid one identity per entire organization merely to reduce administrative effort.

## Hybrid access and governance
An on-premises dependency may require a protocol or directory integration that differs from a cloud-native service. Inventory the protocol, directory authority, trust relationship and network route before proposing a hybrid authentication design. “Use Entra ID” is not a sufficient explanation of how a legacy application accepting only a particular authentication protocol will behave.

For people, distinguish standing permissions from eligible, time-bound privileged access. Access reviews and lifecycle processes address a different failure mode from authentication: someone can authenticate correctly yet no longer have a business need for access. Guest access requires sponsorship, expiry and review just as employee access does. Specific identity-governance capabilities and licensing must be checked for the selected tenant. [S09: Identity governance](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview)

## Secrets, certificates and cryptographic keys
Key Vault separates sensitive material from application configuration and provides controlled access to secrets, keys and certificates. The three are not synonyms: a secret is retrieved sensitive data; a cryptographic key supports cryptographic operations; a certificate binds identity to a public key and has its own lifecycle. A design must name who creates, rotates, revokes and recovers each artifact. [S10: Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)

## Worked example: a service that reads invoices
Contoso’s invoice API should read invoice data but not alter deployment policy. Its workload identity receives a narrowly scoped data-access role. The deployment operator receives a separately defined management role. The operator’s ability to deploy code remains a security consideration, because code deployed under a powerful workload identity may exercise that identity’s permissions. This is why separating accounts alone is insufficient: review the complete path by which authority can be exercised.

The decision note states the identity owner, target permissions, token audience, credential-free path where supported, rotation responsibility for unavoidable secrets, and recovery behavior. It does not record passwords, private keys or tokens.

---

# 02. Governance: organize ownership before enforcement

**Learning purpose:** Design resource boundaries, compliance controls, tagging and identity governance without confusing their purposes.

## Resource organization is an operating model
A useful hierarchy reflects stable control boundaries, not every temporary organization chart. Management groups can group subscriptions for inherited governance. Subscriptions can separate operational or billing boundaries. Resource groups collect related resources for lifecycle management. Tags provide descriptive metadata; they do not create an authorization boundary. [S11: Resource organization](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org)

Start by identifying owners, environments, legal constraints and isolation needs. Then select the hierarchy. Avoid placing unrelated production workloads in a shared lifecycle container simply because a diagram looks shorter. Conversely, needless fragmentation creates policy exceptions, duplicated administration and poor visibility.

## Policy, permissions and locks do different jobs
Azure Policy evaluates resource properties against organizational rules and supports compliance reporting and enforcement effects. Azure RBAC governs who can perform actions. A policy can constrain an allowed operation; it does not replace identity authorization. An audit result is evidence about an evaluated condition, not certification that the complete organization is compliant. [S12: Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

Control design should include rollout sequencing. Begin with an understood scope and measurable effect. Investigate existing exceptions before enforcing a denial that could disrupt deployment. Name the exception owner, rationale and expiry. “Permanent exception” without periodic review gradually becomes an undocumented second policy.

## Tags and compliance evidence
Choose a small mandatory vocabulary, such as business owner, workload, environment and cost center. Define allowed values and who maintains them. Tag consistency matters more than tag count. Do not store personal information or secrets in metadata that may be broadly visible. Reporting must account for untagged resources rather than silently excluding them.

Governance evidence has freshness and scope. A compliance report taken before the latest deployment cannot prove the new deployment meets policy. A successful check in a development subscription cannot prove an inherited production policy is identical. Preserve the evaluated scope and time with the finding.

## Worked example: two departments and one platform team
Contoso has a regulated clinical workload and an internal marketing site. Both use a shared platform team, but their data controls differ. The architect separates the workload boundaries while reusing common policy definitions. Department-specific exceptions are recorded independently. A central group can view compliance without needing every developer to administer every subscription.

The design note explicitly avoids using the word “secure” as an absolute conclusion. It states what each control prevents, what it detects, who responds and what remains outside its coverage. This makes governance review practical rather than a checklist of product names.

---

# 03. Observability: design a useful evidence path

**Learning purpose:** Choose telemetry, routing, retention and alerts around service decisions rather than collecting everything.

## Select evidence for the question
Metrics answer numerical questions over time, logs provide discrete records, and distributed traces help connect work across component boundaries. Azure Monitor brings these telemetry types into an observability platform. The architecture should distinguish platform health, application behavior and user outcomes rather than treating a healthy virtual machine as proof of a working service. [S13: Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview)

A symptom such as slow checkout can have several causes: a database bottleneck, downstream timeout, exhausted connections or an application regression. Design correlation identifiers and consistent timestamps before an incident. Ensure they do not disclose personal information. A dashboard without reliable joins between components often describes the problem without locating it.

## Routing is a design decision
Resource diagnostic settings can route supported platform logs and metrics to destinations such as a Log Analytics workspace, storage or Event Hubs. Destination choice depends on analysis, retention, integration and cost requirements. Not every telemetry category or resource behaves identically; verify the supported categories and regional constraints for the chosen service. [S14: Diagnostic settings](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/diagnostic-settings)

Workspace boundaries should reflect access, residency and operations. One workspace may simplify cross-service investigation, while separated workspaces may support necessary isolation. Duplication has ingestion, retention and privacy costs. A routing plan should name the category, destination, retention, access owner and reason for collection.

## Alerts must lead to action
Separate a signal from a notification and from a response. CPU utilization can be a diagnostic signal without being the best page-the-on-call condition. Customer-visible error rate or availability may be closer to the service commitment. Thresholds require a baseline, a measurement window and a treatment of missing data. Missing telemetry is not necessarily evidence of health.

Avoid assuming that all anomalies warrant automatic remediation. The response may need approval, rate limits, suppression during maintenance or manual diagnosis. Excess notifications can hide the event that matters. Every alert needs an owner, a runbook and a review date.

## Worked example: an empty dashboard
Contoso deploys a service and sees no errors in its dashboard. The team initially assumes success. The architect notices the dashboard also shows no requests. There are at least two competing explanations: no traffic or failed collection. A meaningful acceptance check confirms a known synthetic event reaches the intended destination and that access controls expose it to the responder. This example illustrates validation, not an instruction to run a live test.

The resulting design includes collection health, application outcomes and infrastructure indicators as distinct signals. Retention for audit records is justified separately from the short window used for operational alerting.

---

# 04. Relational data: choose compatibility and operating responsibility

**Learning purpose:** Evaluate relational platforms, compute and service tiers, scaling, security and recovery as one design.

## Begin with the workload, not the database brand
Record transaction boundaries, query patterns, consistency requirements, write rate, data size, growth and operational skill. Separate hard compatibility constraints from familiar habits. A stored procedure dependency or instance-level feature may constrain placement; a preference for a familiar console may not justify a larger operating burden.

Azure SQL Database, Azure SQL Managed Instance and SQL Server on Azure Virtual Machines offer different balances between managed operation and control. SQL Database suits database-oriented managed deployments; Managed Instance addresses a broader instance-compatibility space; SQL Server on a VM offers operating-system and instance control with more customer responsibility. Selection still requires a feature and migration assessment. [S15: Azure SQL platform comparison](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview?view=azuresql)

## Service tier and compute are separate choices
A service tier addresses capability and performance characteristics; compute choices determine how capacity is allocated and billed. Provisioned versus serverless behavior and elastic sharing must be evaluated against the actual workload and supported combination. Check availability, minimum capacity, pause behavior, storage characteristics and latency before recommending a particular SKU. Do not generalize one product’s tier behavior to another. [S16: SQL purchasing models](https://learn.microsoft.com/en-us/azure/azure-sql/database/purchasing-models?view=azuresql)

## Scaling and data protection
Scaling up changes resource capacity; scaling out divides or distributes work. Read replicas can reduce read pressure but do not automatically solve write contention. Sharding changes application and operational complexity. A schema or query problem may be cheaper to correct than perpetual capacity growth. Benchmark with representative skew, not only average transaction volume.

Data protection includes identity, network access, encryption, auditing, retention and recoverability. Encryption alone does not prevent an authorized but mistaken deletion. Replication can propagate bad changes, so it does not remove the need for recoverable historical versions or backups. Define who can restore, where restored data can land and how sensitive data remains protected after restoration.

## Worked example: an overnight reporting surge
Contoso’s booking database performs acceptably during the day but slows during overnight reports. The first question is whether reports compete with transactional work, not whether the database needs a larger machine. Candidate designs include query optimization, separating analytical processing, or an appropriate read-scaling approach. Each has data-freshness implications.

The decision records the maximum acceptable reporting delay and whether reports require an identical transactional snapshot. A proposal that delivers yesterday’s data faster is not a success if the business requires current balances. Conversely, paying for transactional capacity to satisfy a tolerant nightly report may be unnecessary. The architect explains both the chosen option and the rejected alternative.

---

# 05. Documents, objects and integration: design for access patterns

**Learning purpose:** Choose semi-structured and unstructured storage and explain how operational data becomes analytical data.

## Match the model to the work
Relational, document, key-value and object models solve different access problems. List the operations first: point lookup, join, aggregation, ordered scan, binary retrieval or search. Combining stores can be justified when access patterns genuinely differ, but every added store creates another consistency, recovery and operations boundary. [S17: Data models](https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/understand-data-store-models)

For document-oriented workloads, partition design is architectural. A partition key affects distribution, hot spots and the cost of cross-partition work. Test how growth changes distribution and how a single popular tenant behaves. Flexible schema is not the absence of a contract: consumers still rely on meaning and versioning. Azure Cosmos DB requires explicit attention to partitioning and supported consistency choices. [S18: Cosmos DB partitioning](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning)

## Object storage and durability
Binary assets, documents and large immutable objects often fit object storage. File shares serve a different access model and may be appropriate when applications require file protocols. Choose access tier and lifecycle policy from expected access frequency, retrieval requirements and retention rules rather than price per stored unit alone. Retrieval charges and delay can dominate a supposedly cheap tier. [S19: Blob access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

Azure Storage redundancy options address different failure boundaries: local, zone and geographic protection. Geographic replication can involve a lag, and read access to a secondary is a separate consideration. Redundancy is not a complete defense against logical deletion or corruption; recovery features and retention remain part of the design. [S20: Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

## Data integration and analysis
An integration design names the source, ingestion mode, transformations, destination, schema contract, quality checks and replay strategy. Batch is suitable where delay is acceptable; streaming may be justified where action depends on fresh events. Azure Data Factory provides orchestration and data-movement capabilities, while analytical platform selection depends on the processing and consumption model. Do not select an entire analytical platform merely because a connector exists. [S21: Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/introduction)

## Worked example: images and appointment trends
Contoso stores appointment records, uploaded scans and anonymized trend aggregates. Keeping all three as database blobs would simplify one interface but may fit their access patterns poorly. The design separates transactional facts from object assets and curated analytical output. A stable identifier links them, while permissions and retention are defined per category.

The analytical pipeline must handle late and duplicate events. It records lineage and an agreed freshness target. The worked design does not claim that removing a name alone anonymizes data: privacy review must consider the combination of fields and reidentification risk. Exact handling rules belong to the organization’s approved policy.

---

# 06. Continuity: recovery objectives before redundancy

**Learning purpose:** Separate high availability, backup and disaster recovery, and explain end-to-end recovery across compute and data.

## Three different promises
High availability reduces disruption from expected component failures. Backup preserves recoverable data states. Disaster recovery restores service after a larger failure. The mechanisms can overlap but are not substitutes. A replicated deletion can leave an available system with the wrong data. A valid backup can still take too long to restore for the business.

Recovery point objective describes tolerated data loss measured in time; recovery time objective describes tolerated restoration time. The achieved result depends on the complete recovery procedure, not only a product’s replication interval. Include detection, decision, authorization, provisioning, restore, validation and traffic movement in the timeline. [S22: Disaster recovery design](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery)

## Compute and data recovery
Azure Backup supports backup scenarios; Azure Site Recovery supports replication and recovery orchestration for supported workloads. Their supported sources, workload consistency, network prerequisites and restore behaviors must be checked separately. Database-native recovery may be more appropriate for a particular database than treating the entire server as one opaque unit. [S23: Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-overview) [S24: Site Recovery](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview)

For objects, protection may include versioning, soft delete, immutability or backup depending on the service and threat. These controls address different mistakes. Restore authorization should not be assumed to match ordinary read permissions. Recovery also needs usable keys, configuration, identity and dependency endpoints.

## Zones and regions
Availability zones isolate certain failures within a region. Multiple regions address different failure scopes and introduce latency, cost and coordination decisions. Do not assume every region offers the same services or capacity, or that an application’s state is automatically replicated with its compute. Service-specific zone support must be verified. [S25: Availability zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)

An active-active design is not automatically superior. Concurrent writes can introduce conflicts; a passive region can lack the capacity or current configuration needed at failover. Select the pattern from recovery objectives and operational ability, then document degraded behavior.

## Worked example: a 30-minute recovery target
In this fictional design, Contoso requires recovery within 30 minutes. The team’s draft lists a 10-minute database restore and calls the target met. The architect adds the remaining stages: recognizing the incident, choosing a recovery point, validating restored data, restoring dependent configuration and directing clients. Those stages may consume the rest of the budget.

The design therefore includes a recovery sequence with owners, evidence of success, stop conditions and a return-to-normal procedure. These are planning artifacts, not measured recovery claims. No test has been run in this course. A backup completion record proves completion of a backup operation, not successful end-to-end recovery.

---

# 07. Compute: choose the responsibility you can operate

**Learning purpose:** Compare virtual machines, managed web hosting, containers, serverless and batch without treating modernization as an end in itself.

## The selection axes
Compute design combines runtime compatibility, deployment unit, scaling behavior, networking, persistence and operational control. A service is suitable only if its constraints fit the application and the team. Managed does not mean responsibility-free: application security, data protection, configuration and service-specific operation remain relevant. [S26: Compute selection](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree)

Virtual machines are candidates when operating-system control, specialized dependencies or legacy compatibility are essential. Their flexibility comes with responsibility for image management, patching and workload resilience. A scale set can manage a fleet, but application state and lifecycle handling still need design.

## Containers are packaging, not an operating model
A container packages dependencies; an orchestration platform manages execution and lifecycle. Azure Kubernetes Service is a candidate when Kubernetes capabilities and control are justified. Azure Container Apps may fit application-focused container hosting with a different operating burden. App Service is another candidate for supported web applications. Select the platform based on required control rather than adopting Kubernetes by default. [S27: Container hosting comparison](https://learn.microsoft.com/en-us/azure/container-apps/compare-options)

Ask whether the team can operate upgrades, networking, identity, observability and incident response for the chosen platform. Portability of an image does not make every platform feature portable. Describe which dependencies would still bind the application to a platform.

## Serverless and batch
Functions are a candidate for event-triggered code; execution and scaling behavior depend on the hosting option. Serverless does not make a long-running, stateful process automatically suitable. Batch workloads emphasize scheduling many tasks, data locality, parallelism and completion deadlines. Azure Batch provides managed scheduling and compute-management capabilities for parallel and high-performance workloads. [S28: Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview) [S29: Azure Batch](https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview)

## Worked example: three jobs, three placements
Contoso has a public web application, an image-processing worker and a legacy licensed desktop component. They need not share one compute platform. The web application values managed web hosting; the worker values event-driven scale; the legacy component may need a VM-compatible environment. The architecture document lists why each placement is appropriate and what would trigger reconsideration.

The most important comparison is not “which platform is newest?” but “which platform meets the requirement with acceptable operating cost and failure behavior?” The design also checks whether asynchronous work can tolerate retries and whether temporary files survive the chosen execution model.

---

# 08. Application architecture: decouple without losing correctness

**Learning purpose:** Explain messaging, events, APIs, caching, configuration and deployment as connected design decisions.

## Commands, events and streams
A command asks for work; an event describes something that happened. Service Bus, Event Grid and Event Hubs address different messaging patterns rather than being interchangeable queues. Choose from delivery requirements, ordering, throughput, replay, fan-out and consumer behavior. Assume duplicates can occur unless the complete end-to-end design establishes otherwise. Idempotent processing is often essential. [S30: Asynchronous messaging](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/messaging)

Decoupling does not remove dependencies; it changes their timing. A consumer that is unavailable creates a backlog. Design retention, dead-letter handling, observability and the response to poison messages. A retry without a limit can amplify an incident. A retry with no idempotency strategy can duplicate business effects.

## APIs and integration
API Management can provide a managed gateway and policies for publishing and controlling APIs. Authentication at the gateway is not automatically sufficient authorization inside every backend. Consider versioning, throttling, transformations, client identity and failure behavior. A gateway can become a critical dependency and needs its own continuity design. [S31: API Management](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts)

## Cache and configuration
A cache can lower latency and backend load but introduces staleness and invalidation decisions. Define the source of truth, expiration, cache-miss behavior and whether stale content can be served. Never treat cached permissions as harmless merely because they improve speed. Azure Managed Redis is a candidate for managed caching; service lifecycle and migration guidance matter when selecting a current offering. [S32: Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/overview)

Configuration has a lifecycle distinct from application binaries. Azure App Configuration can centralize configuration and feature flags, while secret values should use an appropriate secret store. Design rollback of a flag or setting, not only rollback of code. Configuration changes can cause incidents even when no binary is deployed. [S33: App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/overview)

## Automated deployment
A deployment design includes source version, artifact identity, configuration, environment promotion, checks, rollout strategy and rollback limits. Infrastructure as code can make intended configuration reproducible, but applying it can still be destructive. Approval should bind to a specific change rather than a vague project name. A rollback must consider data compatibility, not just redeploying old code. [S34: Safe deployments](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments)

## Worked example: duplicate appointment notifications
A worker sends a notification and crashes before acknowledging the message. Delivery resumes and the notification may be sent again. The architect records a business identifier and an idempotency strategy that survives worker replacement. A service’s duplicate-detection capability may help, but it is not a blanket guarantee about an external email provider. The lesson is to reason across the boundary where the actual side effect occurs.

---

# 09. Networking: draw traffic intent and trust boundaries

**Learning purpose:** Select internet and hybrid connectivity, private access, performance controls and routing based on actual traffic.

## Start with the traffic matrix
For every flow, identify source, destination, protocol, direction, identity, expected volume and acceptable latency. Distinguish inbound user traffic from outbound dependency access and administrative access. This prevents a broad “open the network” change from hiding several unrelated needs.

Virtual networks provide isolation and connectivity foundations. Peering, gateways and routing choices must be evaluated as part of a topology rather than assuming that any connected network can automatically transit every other network. DNS resolution is part of private connectivity; a private address that clients cannot resolve or route to is not a functioning design. [S35: Virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)

## Hybrid paths and performance
VPN and ExpressRoute offer different connectivity models. Select using resilience, bandwidth, latency, operational requirements and cost. A private connectivity service does not eliminate the need to consider encryption and application security. Redundant paths must also be diverse enough to address the intended failure scenario. [S36: ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

Performance is end to end. A fast circuit cannot compensate for a distant synchronous dependency or an application that repeatedly transfers unnecessary data. Place latency-sensitive components intentionally and measure the complete user journey. Avoid quoting a latency target as guaranteed merely because two services share a region.

## Load balancing and protection
Azure Front Door supports global HTTP application delivery; Application Gateway provides regional application-layer routing; Load Balancer addresses layer-4 traffic; Traffic Manager uses DNS-based routing. The decision depends on protocol, geographic scope, TLS handling, health detection and application requirements. DNS routing does not proxy each request. [S37: Load balancing options](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview)

Separate network filtering, web application protection and identity-based access. Network security groups, firewalls and web application firewalls operate at different layers and scopes. Private endpoints can provide private service access but require service-specific configuration and DNS planning. They do not by themselves prove that public access is disabled. [S38: Private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

## Worked example: private data, public application
Contoso wants public users to reach a booking frontend while keeping its database off the public access path. The architecture shows the public edge, application tier and private data path as different zones of trust. It includes the DNS and outbound service dependencies necessary for operation, rather than depicting a completely sealed application that cannot authenticate or report telemetry.

The accompanying traffic table identifies allowed paths and intended denials. The illustration should use meaningful geography, application silhouettes and service symbols, but the table provides precision that an attractive picture alone cannot convey.

---

# 10. Migration: move a dependency system, not a server list

**Learning purpose:** Evaluate readiness and migration strategy for applications, databases and unstructured data with clear cutover criteria.

## Discovery precedes placement
A migration inventory should include application owners, dependencies, authentication, data classification, performance, licensing and operational commitments. Server names alone cannot reveal a shared database, a hard-coded endpoint or a scheduled file exchange. Assess readiness and the target operating model before selecting a migration wave. [S39: Migration planning](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/plan-migration)

Different workloads may be retained, retired, rehosted, replatformed or refactored. The right choice depends on business value and constraints. A deadline may favor an initial rehost, followed by a separately justified modernization. A low-value system may not deserve migration at all.

## IaaS and PaaS migration
Azure Migrate helps assess and migrate supported workloads. Assessment results are inputs, not an automatic guarantee of application compatibility. For a PaaS destination, validate runtime behavior, integrations and operational differences. For IaaS, include images, disks, network design, identity and management, not merely machine size. [S40: Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview?view=migrate)

Database migration requires compatibility assessment, transfer or replication, cutover and reconciliation. Decide how long writes can pause and how the team will detect missing or duplicated data. Unstructured data transfer similarly needs integrity checks, access-control mapping and a treatment for files changed during copying. Available bandwidth and transfer windows affect the approach. [S41: Storage migration](https://learn.microsoft.com/en-us/azure/storage/common/storage-migration-overview)

## Cutover is a decision with evidence
A cutover plan names the operator, prerequisites, start condition, validation, stop condition and fallback. The fallback may cease to be simple after new writes occur in the target. Explain how those writes would be preserved or reconciled rather than assuming a DNS reversal restores correctness.

Cloud Adoption Framework emphasizes planning migration sequencing and readiness. Sequence related dependencies together or explicitly support a temporary hybrid period. Include the people who will operate the result, not only those moving the data. [S39: Migration planning](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/plan-migration)

## Worked example: a shared database surprises the team
Contoso schedules a booking application for migration but discovers an on-premises reporting job writes directly to its database. Moving the application alone would not remove that dependency. Options include moving the writer in the same wave, preserving a temporary supported path or redesigning the interaction. The choice requires the reporting owner’s agreement.

The design note records the dependency, the transition duration and the condition for retiring the old path. “Migration complete” means the agreed service and operational outcomes are met, not simply that a virtual machine is running in Azure.

---

# 11. Synthesis: a defensible architecture decision

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