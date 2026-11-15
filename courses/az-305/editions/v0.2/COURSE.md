# AZ-305: Designing Azure Infrastructure Solutions

Independent original course · 15 November 2026 · Expanded Draft 2

No practice exams, videos or labs. Fictional worked examples explain decisions.

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

## Examination logistics are part of readiness
Exam duration is the answering time; seat duration includes surrounding instructions and administrative activities. During applicable role-based exams, Microsoft provides restricted access to Microsoft Learn from the examination interface. This is not unrestricted internet access, access to personal notes or extra time. The examination interface and current policy govern which content is available. [S05: Exam duration and experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience)

Prepare the correct booking account, required identification and testing environment, and request necessary accommodations through the official process before the appointment. A certification renewal assessment is distinct from taking AZ-305; Microsoft’s current role-based renewal route should be checked through the credential page. This course does not enroll the learner, purchase an exam or make an appointment. [S03: Azure Solutions Architect Expert](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/)

A score report indicates performance by area but does not disclose the exact items answered incorrectly. Use it as directional evidence rather than reverse-engineering a count of correct answers from a bar chart. The scaled score exists to account for differences in examination difficulty. [S04: Exam scoring](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports)

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

## Mechanism comparison: cloud and hybrid sign-in
Password hash synchronization allows cloud authentication using synchronized password-derived information. Pass-through authentication validates through an on-premises agent, introducing an on-premises availability dependency. Federation delegates authentication to a separate identity provider and is appropriate only when its requirements justify the additional operating complexity. Synchronization and authentication are separate decisions: selecting a synchronization technology does not itself settle the sign-in method. [S42: Hybrid authentication selection](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn)

**Worked decision:** Contoso wants staff cloud access to continue during an on-premises outage. If its security requirements permit password hash synchronization, cloud authentication is a candidate that avoids depending on a live on-premises validation agent for each sign-in. If a policy requires on-premises validation, the architect documents that dependency, agent resilience and incident procedure. Federation is not selected simply because it sounds more enterprise-oriented.

## Conditional Access is a policy decision, not a password store
Conditional Access evaluates signals such as user, application, device and risk to require controls or deny access. A requirement for stronger authentication can be expressed as policy rather than embedded separately in every application. The design must consider licensing, affected identities and emergency access before enforcement. Report-only evaluation helps understand impact; it is not equivalent to blocking unsafe access. [S43: Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)

**Worked decision:** A staff member using an unmanaged device may be allowed to read low-sensitivity information but not perform a privileged operation, depending on application support and policy. The architecture records the intended access rule, not merely “enable MFA.” It also states how staff regain access during a device or authentication outage without turning a temporary exception into permanent broad access.

## Legacy application access and directory protocols
Application proxy is a candidate for remote access to supported on-premises web applications through Entra preauthentication and connector-based access. It is not a universal replacement for every network protocol. Validate the application’s authentication and single-sign-on requirements, and make connector availability part of the dependency design. [S44: Application proxy](https://learn.microsoft.com/en-us/entra/identity/app-proxy/overview-what-is-app-proxy)

Entra Domain Services provides managed domain features such as domain join, LDAP and Kerberos/NTLM. It is distinct from Entra ID’s modern identity service and is not a drop-in answer to every legacy Active Directory requirement. Check schema, administration and trust requirements before selecting it. [S66: Microsoft Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview)

**Worked decision:** An old web application needs remote employee access, while a separate legacy service needs domain-style authentication. The first may fit application proxy; the second requires a directory-protocol assessment. Combining them under “hybrid identity” without separating protocols would produce an incomplete design.

## Privilege activation and effective access
PIM can make privileged assignments eligible and time-bound, with activation conditions such as approval or stronger authentication. An access review asks whether access should continue; PIM asks how privilege is activated and controlled. Neither substitutes for a correctly scoped role. [S45: Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)

The application owner also distinguishes Entra directory roles from Azure resource roles. An identity administrator’s directory responsibilities do not imply the application’s data-access design. When documenting authorization, name the principal, operation and resource scope, then inspect inherited access. A custom role is justified by a real gap in built-in roles, not by a preference to duplicate them.

## Customer access is not employee guest access
External ID supports both business collaboration and customer identity scenarios. B2B collaboration brings partners into a workforce context with controlled access. Customer identity uses an external-tenant configuration for consumer or business-customer applications. A supplier who needs internal collaboration and a public customer registering for a service do not automatically belong in the same identity design. [S76: External ID](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview)

**Worked decision:** Contoso invites a contracted administrator to a limited internal resource scope with sponsorship and expiry. Patients using its public-facing application follow a separately designed customer identity journey. Neither identity type receives broad Azure administration rights merely by signing in. The application maps authenticated identity to authorized business actions.

## Vault or Managed HSM: select custody, not prestige
Key Vault handles secrets, certificates and cryptographic keys. Managed HSM is a dedicated key-management offering with single-tenant HSM protection and a distinct access-control and recovery model; it is not a general secret or certificate store. Select it when explicit key-custody or isolation requirements justify its operational and cost implications. Do not choose it simply because the name sounds stronger. [S67: Managed HSM](https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/overview)

Soft delete and purge protection address different deletion stages. Recovering a vault does not automatically restore every integrated role assignment or event subscription. The recovery plan therefore includes authorization and integration reconstruction, not just key material. Rotation also requires consumer compatibility: keeping an old version temporarily may be necessary while dependent services transition. [S68: Vault recovery](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview)

**Complete authorization example:** a production support group is eligible for a narrowly scoped operational role; developers have ordinary access only in development; a workload identity reads only its own required data and secrets. A central platform assignment is inherited where intended, but a clinical exception is not granted at a parent scope that would expose unrelated workloads. An access review removes a departed contractor, while PIM controls temporary privilege for a remaining operator. Each mechanism addresses a different lifecycle stage.

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

## Select an effect that matches the governance intent
Audit records noncompliance; deny blocks matching requests under the rule’s applicable behavior. Modify and deployIfNotExists can support correction or deployment of related configuration, subject to their definitions and permissions. Existing resources may require remediation; assigning a policy is not proof that historical resources were fixed. Effects differ by resource lifecycle and must not be swapped casually. [S46: Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics)

**Worked decision:** Contoso wants required diagnostic settings on new and existing resources. The architect first inventories support and destinations, then evaluates an applicable policy and its remediation identity. A simple deny would only prevent a request that violates the rule; it would not populate the missing historical telemetry. The rollout record distinguishes the assignment, existing compliance state and authorized remediation.

## Design the hierarchy from conflicting requirements
Suppose marketing and clinical services share a platform team but need different permitted regions. Place the difference at a scope that makes inheritance understandable. Avoid a broad parent policy followed by dozens of undocumented exclusions. The shared team’s role can be granted independently from the policy scope; organizational responsibility need not force identical technical controls.

A resource group should normally make lifecycle management clearer. Resources with different retention or independent ownership may not belong in one deletion boundary. A tag called “production” is useful metadata but cannot enforce production isolation. An environment label should therefore be backed by the actual role and policy model.

## Explain the limits of a compliance result
A technical rule can test whether a property has an approved value; it may not establish that the chosen value satisfies a legal or business obligation. A region restriction does not automatically resolve every data-residency question, because backups, telemetry and integrated services also require analysis. The design identifies the evidence each control produces and the human review still required.

The governance record includes policy owner, assignment scope, exemption rationale, expiry and evidence date. This is a worked documentation pattern, not a claim that any tenant has passed compliance review.

## A concrete hierarchy and its consequences
In the fictional model, the organization has a platform management group and a workloads management group. The workload branch separates regulated and general workloads where policies differ. Clinical production and development use separate subscriptions because authorization and operational controls differ. Within clinical production, application and independently retained records use lifecycle-appropriate resource groups.

This is one possible model, not a Microsoft-mandated hierarchy. Its advantage is understandable inheritance. Its cost is additional subscription and policy administration. A small organization may rationally choose fewer boundaries if it can still express its actual controls clearly. The architectural justification is the requirement, not the number of boxes.

## Locks do not replace backup or permissions
A CanNotDelete lock prevents applicable control-plane deletion; a ReadOnly lock restricts applicable control-plane changes. Locks apply to management operations, not every data-plane operation. They can also interfere with operations that appear read-oriented but use management APIs in unexpected ways. Authorized users with appropriate rights can manage locks, so they are not an immutable security boundary. [S69: Resource locks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Worked decision:** protecting a storage account resource from accidental deletion does not prove that individual documents cannot be overwritten. Contoso combines an appropriate management safeguard with separately designed data recovery. The team documents the maintenance procedure and who may remove the safeguard rather than sharing a privileged credential to work around it.

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

## Choose collection mechanisms deliberately
Data collection rules define collection, processing and routing for supported Azure Monitor paths. With the relevant agents or ingestion paths, they can specify what is collected and where it is sent. They are not a universal replacement for resource diagnostic settings. Verify which path the telemetry uses before recommending a rule or transformation. [S47: Data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

Application Insights supports application performance monitoring, including supported OpenTelemetry instrumentation. Application dependencies and request traces can explain behavior that platform metrics cannot. Sampling can reduce volume but affects what is available for investigation; the design should explain which observations require unsampled or separately retained evidence. [S63: Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

**Worked decision:** Contoso needs to distinguish slow database calls from slow external messaging calls. Platform CPU charts are insufficient. The proposed evidence path correlates application requests with dependencies. It records whether instrumentation covers both dependencies and what happens when a client library does not propagate context. Missing spans remain a coverage gap rather than being treated as fast operations.

## Match alert type to signal
Metric alerts evaluate numerical time-series signals; log search alerts evaluate queries over logs; activity log alerts respond to management-plane events. Service Health and Resource Health signals answer different questions from an application’s business error rate. An action group identifies actions or notifications, but routing a notification does not prove a responder acted. [S64: Azure Monitor alert types](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Worked decision:** A deployment change and a rise in failed bookings occur close together. The monitoring design needs an activity/change record plus application telemetry, not a single CPU threshold. The change might be causal or coincidental; the responder correlates time, scope and affected requests before deciding. The alert text should not declare “deployment caused outage” merely because the events are nearby.

## Retention, access and ingestion cost
Operational responders may need detailed recent logs while audit reviewers need selected longer-lived evidence. Design retention separately by purpose and check the supported table or storage options. Avoid collecting secrets and then relying on analysts never to query them. Filtering or transformation must preserve the evidence required for the stated purpose.

A fictional monthly cost estimate should account for ingestion volume, retention and duplicated destinations. A query spanning many workspaces can simplify a central view without erasing the access boundaries. The design records the intended reviewer’s ability to access each dataset; otherwise a dashboard may look complete only to an administrator.

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

## Explain the tier decision in workload terms
In Azure SQL Database’s vCore model, General Purpose targets many common workloads, Business Critical emphasizes demanding latency and resilience characteristics, and Hyperscale uses a distinct architecture for larger-scale needs. Exact features and supported combinations vary. DTU and vCore are purchasing models; provisioned and serverless concern compute behavior; they are not interchangeable labels for the same dimension. [S48: SQL Database vCore tiers](https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-sql-database-vcore?view=azuresql)

**Worked decision:** Contoso’s small but steady booking workload needs predictable performance. A pause-capable compute choice should not be selected solely because the database is small: inactivity patterns and resume latency matter. A group of databases with uneven peaks might justify shared elastic capacity, but simultaneous peaks could remove that benefit. The architect compares the actual demand distribution rather than total database count.

## Compatibility narrows the shortlist
A modern application with database-scoped dependencies can start its evaluation with SQL Database. An application relying on instance-level behavior may warrant Managed Instance compatibility assessment. A dependency on operating-system agents or unavailable engine capabilities may point toward SQL Server on a VM. These are candidate paths, not automatic decisions. Record the specific feature that prevents a managed alternative rather than saying “legacy” as a blanket reason.

For a VM-based database, the team owns the relevant operating-system and database management work. For a managed database, the application still owns query correctness, data-access permissions and recovery requirements. An operations team’s familiarity can be a constraint, but it should be priced and compared with the cost of maintaining control.

## Protection and performance interact
A read-only reporting path can offload some work but may have freshness differences. A cross-region design can change latency and consistency behavior. Encryption and network restrictions can affect integration choices. Therefore a platform recommendation should include a short compatibility matrix: essential feature, supported candidate, remaining validation and operational owner.

In the fictional overnight-report example, the architect does not purchase a larger tier immediately. The first decision is whether reporting needs transactional recency. That answer determines whether isolation into an analytical system is acceptable. The chosen approach is explained with a rejected alternative and the condition that would make the alternative preferable.

## A relational choice outside the SQL Server family
Azure Database for PostgreSQL flexible server is a managed PostgreSQL option with compute, storage, availability and maintenance choices. An application already built on PostgreSQL should be assessed against this engine-compatible option before assuming that migration to the SQL Server family is necessary. Extension support, version compatibility and required privileges remain important. [S70: Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/overview)

**Worked decision:** Contoso’s analytics-support application uses PostgreSQL-specific features. The architect selects PostgreSQL flexible server as the first candidate because avoiding unnecessary engine conversion reduces application change. SQL Database is rejected for this scenario unless a separate business benefit justifies conversion. A PostgreSQL VM remains an alternative if an essential capability cannot be supported in the managed offering, but the operating burden must be explicit.

## Worked protection design
For the fictional booking database, the design combines a workload identity, minimal data permissions, a restricted network path and database audit evidence. Platform-managed encryption is the starting assumption; customer-managed keys require a specific custody need and introduce a key-availability dependency. Backup retention and the ability to restore are separate from network isolation. A restore may create a new database requiring connection and access validation before use.

An approval to increase compute does not imply approval to weaken network rules. Similarly, a backup policy is not proof that the application can recover within its target. These decisions are documented together so a performance change cannot quietly invalidate the protection model.

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

## Analytical storage is not the transactional database with a new label
An analytical serving layer is optimized for reading and aggregating prepared data. A warehouse can support structured reporting; a lake-oriented approach retains data for varied processing; a lakehouse combines relevant capabilities. The design evaluates concurrency, query style, data shape, freshness and the team’s tools. “Big data” alone is not a selection criterion. [S49: Analytical data stores](https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/analytical-data-stores)

Microsoft Fabric offers integrated ingestion, engineering, analytics and reporting experiences over a shared platform. Azure Databricks and Azure Synapse may also appear in an analytical shortlist, depending on processing and existing investments. Fabric is a current contextual option, not a claim that every Fabric component is explicitly examined in AZ-305. [S50: Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview)

Stream Analytics supports processing streaming data with a SQL-oriented approach. Choose a streaming path only when timely event processing has business value; batch processing is often simpler where delay is acceptable. A pipeline must decide how event time, late arrival and duplicate events affect the result. [S51: Stream Analytics](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction)

**Worked decision:** Contoso wants a weekly utilization dashboard and immediate detection of a queue surge. The weekly dashboard can use a scheduled curated dataset, whereas the surge signal needs fresher processing. Sending both through the most complex real-time system would add operating burden without improving the weekly decision. Conversely, a nightly refresh cannot support a response measured in minutes.

## Reason explicitly about a partition
Imagine one clinic contributes most of Contoso’s bookings. A partitioning strategy based only on clinic identity could concentrate demand. A strategy based only on a random identifier could distribute writes but make clinic-level queries more expensive. The architect compares distribution with dominant query patterns and transaction scope. There is no universally correct partition key.

Schema flexibility also requires versioning. A newly introduced document field may be absent from older records. Consumers need an agreed meaning for absence, null and default values. This protects the analytical pipeline from silently counting older records incorrectly.

## Make lifecycle cost visible
A rarely retrieved archive may fit a low-access tier, but an urgent recovery requirement could make retrieval delay unacceptable. A file share may fit an application expecting file semantics, while object storage better fits direct object retrieval. The worked recommendation identifies the access contract first and evaluates lifecycle cost second, rather than treating all stored bytes as equivalent.

## Consistency choices explained
Strong consistency offers the latest committed value; bounded staleness constrains how far reads may lag; session consistency provides guarantees within a client session; consistent prefix preserves update ordering without guaranteeing freshness; eventual consistency permits temporary divergence before convergence. The chosen API and account configuration constrain their use. Stronger consistency can trade latency and availability for a simpler freshness model. [S71: Cosmos DB consistency](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels)

**Worked decision:** a user editing a profile expects to see that edit on the next read, while a global popularity counter can tolerate delay. Session-oriented behavior may suit the former interaction, whereas weaker freshness may suit the counter. Neither conclusion automatically makes either model suitable for allocating the last available appointment. That transaction needs its own correctness design.

## Throughput is more than stored gigabytes
Cosmos DB expresses operation consumption in request units. Item size, indexing and query shape affect consumption. Provisioned throughput, autoscale and serverless differ in capacity and billing behavior; choose a supported mode using demand shape and required capabilities, not only average traffic. [S77: Cosmos request units](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units)

**Illustrative sizing, not a benchmark:** suppose a fictional measurement found an operation cost of 6 RU and the workload expected 200 such operations per second. That component alone implies 1,200 RU/s before other operations, growth and safety margin. These are invented teaching inputs, not a product guarantee. A hot partition can still constrain performance even when aggregate capacity appears adequate.

## Storage selection matrix in prose
LRS keeps redundancy within a primary location; ZRS spans zones in a region. GRS adds asynchronous secondary-region replication to local redundancy; GZRS combines zone resilience with geographic replication. Read-access variants allow secondary reads under their supported behavior; a replicated secondary is not automatically a writable active endpoint. [S20: Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

Hot, cool and cold blob tiers support online access with different storage/access cost tradeoffs; archive requires rehydration before ordinary reading. Exact minimum-retention, retrieval and account-support rules must be checked. File services are candidates when a protocol such as SMB or NFS is required; object APIs suit object-oriented access. [S19: Blob access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

**Concluded analytical decision:** for the fictional weekly utilization report, select a curated warehouse-style serving dataset rather than repeatedly querying the transactional database. For mixed exploration over retained files, evaluate a lake/lakehouse workflow separately. Select streaming analysis only for the queue-surge signal. This choice prioritizes different freshness requirements instead of forcing all data into one processing cadence.

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

## Mechanisms for relational continuity
SQL Database failover groups coordinate geo-replication and failover for a group of databases and provide listener endpoints. Geographic replication is asynchronous, so an unplanned failover can involve data loss. Application connection resilience and dependent configuration still matter. A failover mechanism does not establish zero data loss under every failure. [S52: SQL Database failover groups](https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db?view=azuresql)

**Worked decision:** Contoso accepts a documented small recovery-point window for appointments but not silent duplicate processing. Its design pairs a database continuity mechanism with application reconciliation behavior. The team records which operation is authoritative after failover and how clients recover connections. It does not assume that promoting a secondary also moves every secret, identity permission and downstream dependency correctly.

## Choose protection for the mistake
Blob soft delete, versioning and immutability address different risks and have compatibility and retention implications. Soft delete helps recover eligible deletion events; versioning retains prior object versions; immutability can prevent modification for a defined retention or hold condition. Storage redundancy protects against certain infrastructure failures but can replicate a legitimate deletion. [S53: Blob data protection](https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview)

**Worked decision:** A clerk overwrites a scanned document. Geographic redundancy alone is not the answer because the new value can replicate. A recoverable historical version addresses the specific mistake. For a separate legal-retention requirement, an immutable policy might be considered with authorized governance, because it can intentionally restrict later deletion. The two requirements must not be conflated.

## Compute availability choices
Multiple VMs can be placed across availability zones where supported. Availability sets distribute instances across fault and update domains within their applicable scope; they are not equivalent to separate regions. Scale sets manage groups of VMs but still need suitable placement, health handling and application state design. A single-instance application remains vulnerable even if its infrastructure is easy to recreate. [S54: VM availability options](https://learn.microsoft.com/en-us/azure/virtual-machines/availability)

**Worked decision:** Contoso runs two stateless frontend instances but one unmanaged session store. The frontend diagram looks redundant while the user journey is still dependent on a single state component. The design review follows a request through every dependency, then chooses protection for each failure boundary.

## Recovery sequence as a worked explanation
A reasoned recovery narrative first establishes the incident and authorization, then selects the recovery point, restores data and required infrastructure, verifies identity and connectivity, validates business behavior, and changes traffic only when the checks justify it. Return-to-normal includes reconciliation of writes and an explicit decision about the former primary. These are conceptual stages, not executable instructions or an assertion that this course performed a recovery.

## Historical recovery versus regional failover
SQL Database automated backups support point-in-time restoration within configured retention; long-term retention addresses selected older recovery points. Geo-restore depends on appropriate geo-redundant backup configuration and can require a new database and application reconnection. A failover replica and a historical backup solve different problems. [S73: SQL backups](https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview?view=azuresql)

For Contoso, regional service loss motivates a failover design, while an unnoticed erroneous update motivates historical recovery. Restoring an old state may discard later legitimate writes, so business reconciliation is part of the decision. The restoration mechanism alone cannot choose the correct business cutoff.

## Semi-structured availability and recovery
Cosmos DB for NoSQL supports zone-redundant and multi-region designs with failover and backup options. Single-write and multi-write-region arrangements have different operating and conflict implications. Client configuration, consistency and the application’s failure response are part of the design. Backups protect historical state; replication supports availability and does not eliminate logical-corruption risk. [S72: Cosmos DB reliability](https://learn.microsoft.com/en-us/azure/reliability/reliability-cosmos-db)

**Worked decision:** Contoso’s non-transactional catalog can serve reads from multiple regions with tolerated lag. It keeps a deliberately governed write path rather than enabling multi-region writes without conflict rules. That choice simplifies conflict ownership, but writes may be unavailable during a failover transition. The tradeoff is documented instead of hidden behind “globally distributed.”

## Quantified recovery reasoning
Assume a fictional 30-minute RTO and five-minute RPO. The planning allocation is three minutes for detection, two for decision, ten for recovery, five for validation and five for traffic restoration: 25 minutes, leaving five minutes of contingency. These figures are planning assumptions, not measured service timings. A ten-minute replication lag would fail the assumed RPO even if traffic returned in 25 minutes.

For a hybrid VM, the conceptual sequence includes supported replication/recovery configuration, identity and network dependencies, isolated validation of the recovery instance and a controlled traffic decision. Database consistency must match the application’s recovery point. The plan remains unproven until separately authorized operational verification supplies evidence; this course does not perform it.

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

## Compare control with operational burden
A VM is a useful candidate when an application needs a particular operating-system capability or unsupported runtime component. App Service is attractive for supported web applications whose team values managed hosting. Container Apps can suit containerized services without requiring the team to manage a Kubernetes cluster directly. AKS becomes compelling when the required Kubernetes control and ecosystem justify its additional responsibilities. These choices are not a maturity ladder.

**Worked decision:** Contoso has three small HTTP services and no Kubernetes-specific requirement. Packaging them as containers does not by itself justify AKS. The architect starts with the simpler compatible managed option, then records which future requirement would justify changing it. The rejected alternative remains visible so the decision can be revisited without pretending the initial choice was universal.

## Scaling requires a unit of work
A stateless web request, a queue message and a multi-hour simulation have different scaling signals. Scaling HTTP compute from CPU alone may miss connection or dependency saturation. Queue depth can indicate delayed work, but increasing workers may overload a database. The design should state the limiting dependency and the safe upper bound.

For batch processing, separate the scheduler, worker capacity, input data and output integrity. A task should have a defined success condition and a treatment for interruption. Spot capacity may suit interruptible work but requires tolerance for eviction and verification of current product availability. A guaranteed completion deadline cannot be inferred from inexpensive capacity.

## State and replacement
Treat local temporary state as expendable unless the chosen service explicitly provides the required persistence. A container restart is a normal lifecycle event, not an exceptional disaster. Store necessary durable state in a designed data service and account for its latency and throughput. A local cache may improve performance, but its loss should not corrupt business state.

The worked architectural conclusion is that compute selection cannot be separated from data placement, scaling boundaries and operating capability. A service name alone is not a design.

## A specific compute selection
For this fictional workload, Contoso needs a supported web runtime, small operations team, stateless requests and no Kubernetes-only features. App Service is the selected candidate; AKS is rejected because its additional platform control is not required. If the application instead needs a custom container with event-driven scaling and no cluster administration requirement, Container Apps becomes a candidate. An unsupported OS dependency would change the decision toward a VM-compatible path.

## Hosting options change serverless behavior
Functions hosting determines scaling, instance resources, network integration, container support and billing. Current Microsoft guidance recommends Flex Consumption for new serverless function applications, with Premium, Dedicated and Container Apps options addressing other needs. Existing legacy Consumption behavior should not be assumed for new deployments. Verify operating-system and runtime compatibility before selecting a plan. [S74: Functions hosting](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale)

**Worked decision:** a short event-triggered transformation with variable traffic can start its evaluation with Flex Consumption. A required custom Linux image or different steady-capacity requirement changes the shortlist. A long business process should not be represented as one unbounded invocation merely to keep the diagram simple; orchestration and durable state need explicit treatment.

## Batch arithmetic and limits
Suppose 1,000 independent image jobs each need two minutes of worker time. Their total is 2,000 worker-minutes. At perfect utilization, 50 concurrent workers would require 40 minutes; real duration is longer because of startup, transfer, retries and skew. This arithmetic is illustrative and says nothing about actual Azure SKU performance. The design can trade concurrency cost against deadline, while respecting downstream storage and database limits.

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

## Select the message service from the interaction
Service Bus fits brokered enterprise messages where queues, topics and delivery controls matter. Event Grid fits event distribution and reactive integration. Event Hubs fits high-throughput event streams with independent consumers. The choice depends on the delivery model and processing semantics, not merely message size. [S55: Messaging service comparison](https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services)

**Worked decision:** Contoso sends a durable request to create an invoice, notifies interested systems that a document arrived, and ingests a continuous telemetry stream. These can reasonably use different patterns. The invoice path needs explicit handling of failed work; the document event may fan out; the telemetry stream may be replayed independently by consumers. One universal queue would obscure their different needs.

## API boundaries and failure behavior
An API design needs a contract, version policy and authorization model. The gateway can enforce selected controls, but the backend must still understand the caller’s permitted business action. Rate limiting protects capacity; it is not a substitute for authorization. Transformations can simplify consumer migration but may hide an incompatible backend if not governed.

For Contoso’s appointment API, the architect distinguishes public availability searches from authenticated booking writes. Caching a public search result may be acceptable for a short documented period, while a booking transaction requires authoritative validation. The API should not promise an available slot solely because a cached search showed it.

## Cache-aside as a concrete pattern
With cache-aside, the application checks the cache, loads missing data from the source and populates the cache. Updates require an invalidation strategy. Expiration limits staleness but does not guarantee immediate consistency; a cache miss surge can overload the backend. Access-sensitive data needs especially careful scoping and invalidation. [S65: Cache-aside pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside)

**Worked decision:** Contoso caches clinic descriptions, which change rarely, but does not use that cache as the authority for a staff member’s current permission to amend appointments. The latency benefit is preserved where stale data is tolerable. The authorization path remains tied to an approved access design.

## Deployment and configuration must be reversible in meaning
A blue-green or progressive rollout can limit exposure, but only if traffic and health evidence match the intended cohort. A schema change that removes a field used by the older release may prevent simple rollback. Feature flags can separate release of code from enabling behavior, but flag evaluation and configuration access introduce dependencies. The decision note records compatibility across versions and a stop condition; it never labels an unexecuted rollback as proven.

## A concrete automation design
A fictional Contoso pipeline starts from a reviewed source revision, builds one versioned application artifact, records its identity and promotes that same artifact between environments with separately versioned configuration. Bicep is a declarative Azure infrastructure option; it expresses intended resources but does not make every change harmless or eliminate drift. [S75: Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

The pipeline separates identity used to build from identity used to deploy. A controlled environment supplies deployment authority, and secret values are not embedded in source. The design record identifies what changes automatically and what needs a deliberate release decision. This is a conceptual pipeline, not an executable workflow or a live authorization.

For a compatible application, a staged rollout can expose a limited population first; a blue-green approach maintains separate candidate and current environments. Both require defined health evidence and a safe treatment of database versions. If old and new versions cannot read the same schema, switching traffic back may not restore service. The selected approach therefore depends on compatibility, not only speed of deployment.

**Worked integration choice:** an external provider’s synchronous API is used when the user truly needs its immediate result. If the business permits completion later, a queued command isolates the user response from provider delay. The application must expose pending and failed outcomes honestly. Asynchronous design is not permission to report completion before work is done.

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

A traffic specification should identify allowed paths and intended denials. Meaningful geography and service symbols help explain the architecture, but explicit source, destination, protocol, port and identity requirements provide precision that an illustration alone cannot convey.

## Distinguish the security layers
Azure Firewall provides managed stateful network filtering and related capabilities whose availability depends on SKU. Network security groups scope traffic rules at their supported network attachment points. A route must actually send relevant traffic through an inspection point; placing a firewall in a diagram does not establish coverage. [S58: Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/overview)

A web application firewall targets web-layer attacks, such as selected malicious HTTP patterns. It does not replace secure application code, identity authorization or general network controls. Detection and prevention modes have different effects; tuning must account for legitimate application requests and false positives. [S59: Web Application Firewall](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview)

DDoS protection addresses availability threats from hostile traffic floods at its supported layers and resources. It is distinct from WAF protections for application requests. The selected protection plan must match the actual public exposure, supported service and response requirements. [S60: DDoS Protection](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview)

**Worked decision:** Contoso exposes an HTTPS booking application and also has administrative endpoints. A WAF on the public web path does not protect an unrelated management interface. The design first removes unnecessary public administration exposure, then assigns controls to the remaining flows. Controls are evaluated by path and threat rather than counted as security products.

## Hybrid routing and name resolution
A site-to-site VPN can provide encrypted tunnel connectivity over the internet. ExpressRoute provides private connectivity through a connectivity provider, with its own design and resilience considerations. Neither makes routing, DNS or identity configuration automatic. Consider how the service behaves when one path fails and whether the alternative path has enough capacity for the intended degraded mode.

Private endpoint design includes the private address, reachable network path and appropriate DNS resolution. A client resolving the public address can still take an unintended route if public access remains available. The architecture therefore names the resolution behavior expected from Azure, on-premises and remote clients separately.

## Worked routing decision
Contoso’s users are global, but its application has a regional private backend. Global application delivery and regional private connectivity are separate concerns. The architect may combine a global edge service with an appropriate origin path, but must verify the selected service and tier support that path. An attractive picture cannot substitute for the documented feature compatibility.

The diagram’s caption should state what the picture abstracts: certificates, identity exchanges, DNS and outbound telemetry may be omitted visually, but they remain part of the written traffic design.

## Outbound connectivity is explicit architecture
A NAT gateway provides an explicit outbound connectivity mechanism; it is not a web-application firewall or application authorization engine. If traffic must be inspected, routes and firewall design must establish that path. Microsoft’s current guidance changes defaults for new virtual networks under newer APIs, while existing networks can differ. Do not rely on remembered implicit outbound behavior. [S78: Explicit outbound access](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access)

**Worked decision:** Contoso’s private worker needs a third-party API and Azure dependencies. The design lists required destinations and a supported explicit outbound path, with the chosen inspection policy where required. Removing the worker’s public inbound exposure does not remove its outbound needs. DNS and egress behavior are validated as distinct concerns in a real deployment.

A route’s existence is not proof of adequate performance. For an illustrative transfer of 100 GB at a sustained 100 megabits per second, the ideal transfer time is roughly 8,000 seconds, or 2.22 hours, before overhead. This assumes decimal units and sustained throughput; real links and applications can be slower. The arithmetic exposes why nominal link speed alone cannot settle a migration window.

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

## Select a migration tool by the source and transition
Database Migration Service supports migration scenarios across documented source and target combinations. Online and offline possibilities depend on that combination and current tooling. An “online” migration can still need a controlled cutover and validation; it does not mean every database operation continues without interruption. [S57: Database Migration Service](https://learn.microsoft.com/en-us/azure/dms/dms-overview)

For storage, Azure Storage Mover is a managed migration service for supported file and object scenarios. AzCopy is a command-line transfer tool for supported storage operations; current guidance directs large migration scenarios toward Storage Mover where appropriate. Tool selection should include orchestration, monitoring and repeatability, not only transfer speed. [S56: AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) [S61: Storage Mover](https://learn.microsoft.com/en-us/azure/storage-mover/service-overview)

Data Box provides an offline-transfer option using shipped devices. It can address constrained network transfer windows but introduces shipping, custody, import timing and final-delta considerations. It is not instantaneous and does not eliminate the need to reconcile changes made after the initial copy. [S62: Data Box](https://learn.microsoft.com/en-us/azure/databox/data-box-overview)

## Worked decision: moving an archive
Contoso has a large archive and limited connectivity. The architect compares network-based migration with a supported offline transfer option. The archive is mostly stable, so the initial bulk movement can be separated from a smaller final synchronization. The design identifies who owns file integrity, metadata and access-control validation. It does not assume that successful byte transfer proves the destination permissions are correct.

## Worked decision: database downtime
A database owner permits a short write outage but not an entire weekend. The design evaluates a supported synchronization-based migration followed by a deliberate write freeze and cutover. If the required source-target combination lacks that path, the architect reports the incompatibility rather than describing an unsupported tool sequence as a solution.

The cutover record separates source backup, synchronization status, application connection change, business reconciliation and acceptance. If the destination receives new writes, reverting to the source requires a plan for those writes. “We can point back” is not sufficient rollback reasoning.

## Dependency-aware migration waves
Group tightly coupled services into a wave or explicitly fund the temporary hybrid arrangement. Resolve hard-coded endpoints, scheduled transfers and identity dependencies before the move. The exit criterion includes operational handover and retirement of obsolete access, not only successful target startup. These are explained design stages; no migration is performed by this material.

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

## Complete fictional decision record
The following numbers are invented design inputs, not observations or Azure guarantees: 200 peak requests per second; a 95th-percentile interactive target of 500 milliseconds; 30-minute recovery time; five-minute tolerated data-loss window; weekly reporting refreshed within 24 hours; and a small team without Kubernetes operating experience.

**Selected candidate architecture:** App Service for the supported stateless web runtime; Azure SQL Database for transactional booking; Blob Storage for documents; Service Bus for durable notification work; Key Vault for unavoidable secrets; workload identities where supported; Application Insights and platform logs for correlated operational evidence. A global edge is considered only if global delivery requirements justify it. Exact service tiers and regions remain subject to compatibility, cost and performance verification.

**Rejected alternatives:** AKS adds unjustified platform responsibility for this workload. Placing documents in the transactional database would couple binary-asset lifecycle to transaction performance without a demonstrated need. Treating Event Hubs as the notification work queue would choose a stream abstraction for a command-processing requirement. Querying live transactions for every weekly report would mix tolerant analytics with latency-sensitive work.

**Failure story:** if a regional outage occurs, application and data recovery must be coordinated. The RTO allocation is not sufficient evidence of success. If a faulty release overwrites data, a regional replica alone does not recover historical truth. If identity or key access fails, otherwise healthy compute may still be unusable. Each failure story therefore names a different mechanism and a different acceptance condition.

**Cost model:** estimate compute baseline and scale-out, database capacity, replicated storage, request volume, log ingestion/retention, networking and any secondary-region standby. No currency total is asserted without current region/SKU prices and workload quantities. A two-region design may cost more but still be justified; the decision needs the value of recovery, not a slogan about cost optimization.

**Outstanding evidence:** representative performance results, current price calculation, region/SKU compatibility, supported recovery configuration and organization-specific security review. These are implementation validation needs outside this instructional edition, not omitted course labs. The course demonstrates how to reach and document a design decision without pretending that a written architecture is already a validated service.