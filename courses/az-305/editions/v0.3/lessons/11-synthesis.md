# Synthesis: a defensible architecture decision

**Learning purpose:** Integrate the course into an original worked example without claiming a deployed or validated system.

## Architecture review: the fictional Contoso appointment service

This worked architecture is deliberately specific. All volumes, budgets and targets in this section are teaching assumptions, not measured facts, Azure guarantees or a recommendation to buy resources. Product compatibility must be checked in the service-selection chapters. The example shows how those comparisons become one coherent design rather than a shopping list.

### 1. Start with the decision brief

| Dimension | Fictional requirement | Consequence for the design |
|---|---|---|
| Users | Staff in one primary geography; public visitors can browse availability | Staff authorization and public delivery are different paths |
| Application | Supported managed web runtime; HTTP APIs; no OS driver or Kubernetes requirement | Begin with managed web hosting, not VMs or a cluster |
| Demand | 200 requests/second peak, 40 average during office hours; events concentrated after appointments | Size from representative requests and dependencies, not only average count |
| Transaction correctness | An appointment cannot be allocated twice | Authoritative write logic and concurrency control are mandatory |
| Documents | 2 TB initial uploaded content; 100 GB monthly growth | Object lifecycle and access controls need independent design |
| Reporting | Weekly utilization; at most 24-hour data delay | No justification for running every report on the transaction path |
| Recovery | 30-minute RTO; five-minute RPO, subject to business validation | Regional recovery and historical restoration require separate decisions |
| Team | Four application developers, shared operations support, no Kubernetes operations team | Operational complexity is a real constraint |
| Security | Separate staff/customer paths; minimal workload privileges; no secrets in source | Identity, deployment and application data access must be separated |
| Financial control | Budget approval required before purchasing; no amount supplied | Produce a cost model and choices, not a fabricated monthly quote |

A useful architectural discussion challenges the requirements before choosing products. For example, is the five-minute RPO acceptable for a newly booked appointment whose customer received confirmation? If not, the business requirement is internally inconsistent. A low RPO label cannot substitute for a policy governing lost confirmed transactions.

### 2. Make the primary service selections

| Concern | Selected candidate | Why this fits the fictional brief | Rejected alternative and reconsideration trigger |
|---|---|---|---|
| Web hosting | Azure App Service Standard as the initial plan | Supported web runtime, one staging slot and modest initial scale; no zone-redundancy or isolated-environment requirement is assumed | AKS adds cluster responsibility without a Kubernetes requirement; revisit for a demonstrated platform need |
| Booking records | Azure SQL Database General Purpose, provisioned compute, as the initial tier | Relational transactions fit allocation; steady traffic argues against pause/resume, and no specialized I/O requirement is assumed | Cosmos DB is not selected merely for global distribution; revisit only with a documented alternative correctness model |
| Uploaded documents | Blob Storage, hot access tier and ZRS for the active document set | Frequent online retrieval and zone resilience; historical versions and regional recovery remain separate decisions | Database blobs would couple document storage and backup growth to transaction infrastructure |
| Notification work | Service Bus Standard for the initial command path | Queues with required session-based ordering/duplicate controls; Premium is not selected without isolation or capacity need | Event Hubs is a stream abstraction, not the default command-processing choice |
| Credentials | Managed identity where supported; Key Vault Standard for unavoidable secrets | Reduces application-owned credential handling while retaining explicit permission design | A shared administrator credential is rejected regardless of convenience |
| Telemetry | Application Insights and Log Analytics Analytics tables for operational queries/alerts | Connects user requests with dependencies and infrastructure changes | CPU-only monitoring cannot establish booking success |
| Reporting | Scheduled Data Factory ingestion into a warehouse-style serving dataset | Separates tolerant reporting from latency-sensitive transactions | Immediate stream processing is not purchased for a weekly report without another requirement |

The initial tiers are explicit and conditional on the stated fictional brief. Standard web hosting is not being declared sufficient for every 200-request/second workload: representative capacity evidence must confirm it. If zone redundancy becomes mandatory, the web plan choice changes to a currently supported zone-capable configuration. Likewise, storage ZRS does not by itself satisfy regional recovery. This table records an architectural starting decision and its revision triggers, not a deployment approval or a benchmark claim.

### 3. Turn service choice into plan choice

For the web tier, identify whether the design needs deployment slots, autoscaling, zone resilience, private connectivity or dedicated isolation. Compare these requirements with the current plan capabilities. Reject a low-cost plan if it lacks a required capability; reject an expensive plan if the capability has no requirement behind it. Keep application instance count distinct from the maximum allowed by a plan.

For the database, distinguish engine compatibility, service tier, compute model and resource capacity. A variable workload may benefit from a supported serverless option, but a steady workload or strict responsiveness expectation may favor provisioned capacity. Business Critical or Hyperscale must solve a specific latency, resilience or scaling requirement rather than serve as a generic “production” label. A pooled design is justified by multiple databases with complementary demand, not by one database.

For messaging, map required sessions, duplicate detection, transaction behavior, isolation and capacity to the service’s actual tier. If the application design requires a feature unavailable in the cheaper tier, either change the tier or change the design explicitly. Do not leave a feature-to-tier incompatibility for implementation to discover.

Each selection becomes a short decision record: required feature, chosen plan, relevant official source, supported region, capacity assumption, rejected option and review trigger. The recorded source date matters because product plans evolve.

### 4. Define the actual traffic and trust paths

| Source | Destination | Intent | Identity or control | Not permitted by this statement |
|---|---|---|---|---|
| Public visitor | Public application endpoint | Browse and begin an approved customer journey | Edge/application controls and application authorization | Direct database or administration access |
| Staff client | Staff application functions | Perform role-permitted appointment work | Workforce authentication and business authorization | Implicit permission to administer Azure |
| Web workload | Booking database | Required transaction operations | Narrow workload data permissions and approved network path | Subscription-wide management authority |
| Web workload | Document store | Scoped object operations | Appropriate identity/data role and object authorization | Public anonymous access to uploaded documents |
| Worker | Messaging service | Receive and settle its work | Queue/topic-scoped authorization where supported | Unrelated queue administration |
| Worker | Notification provider | Approved outbound delivery | Separate provider credential if unavoidable; controlled egress | Arbitrary external destinations |
| Application | Telemetry destination | Redacted operational evidence | Supported ingestion mechanism and access controls | Recording tokens or sensitive document bodies |
| Deployment identity | Deployment target | Release an approved artifact | Environment-scoped deployment authority | Routine use as the application’s runtime identity |

This is a conceptual allow-intent table, not a deployed firewall policy. Each row needs protocol, endpoint and supported control details in an implementation design. Some paths use Azure service integrations rather than a simple TCP allow rule. DNS, token acquisition and service dependencies must not disappear merely because the diagram omits them.

### 5. Follow one booking through the architecture

A visitor sees availability that may be briefly cached. The application treats it as a view, not a reservation. When the visitor submits a booking, authoritative transaction logic checks the current state and either commits the booking or returns a truthful conflict. The response distinguishes accepted, completed and failed work.

The notification is separate. A committed booking can enqueue work, but the design must handle the boundary between committing the booking and publishing the message. A robust implementation needs an explicit consistency strategy for that boundary rather than assuming two systems commit atomically. The worker handles repeated delivery using a durable business identifier and idempotent behavior. A provider timeout leaves an uncertain delivery result; the application does not assert that the recipient definitely received the message.

Uploaded documents use separate authorization and retention. A document identifier in the booking record is not itself a permission to download the document. Reports consume curated data without needing unrestricted operational access. These distinctions are why the design cannot be reduced to “frontend, API, database.”

### 6. Quantify capacity without pretending to have a benchmark

Suppose a representative fictional request consumes 20 milliseconds of CPU time. At 200 requests/second, the theoretical CPU work is four CPU-seconds per wall-clock second. That arithmetic is not a VM or App Service sizing recommendation: concurrency, garbage collection, network waits, per-instance limits and required spare capacity still matter. If the representative work is wrong, the estimate is wrong.

Likewise, 100 GB monthly document growth produces 1.2 TB annual new logical data before versions, backups, replication and retention expiry. Storing two versions on average is not necessarily exactly twice the invoice because operations and tier behavior also matter. The calculation identifies cost drivers to price, rather than inventing a total.

A recovery plan allocating three minutes to detection, two to decision, ten to restoration, five to validation and five to traffic return totals 25 minutes. Its five-minute contingency disappears if identity recovery takes longer than assumed. A technically fast failover is not sufficient if the human decision is not defined.

### 7. Compare three failure stories

| Failure | Useful mechanism | Mechanism that is insufficient alone | Business acceptance criterion |
|---|---|---|---|
| One application instance fails | Multiple healthy instances and suitable traffic handling | A backup of application code | Requests continue within the agreed degraded behavior |
| Primary region is unavailable | Coordinated application/data recovery and routing | Database backup completion notification | Required user journeys work and data-loss tolerance is met |
| Erroneous data update replicates | Historical recovery and reconciliation | A second region with the same bad update | Restored state is correct and legitimate subsequent work is handled |
| Key or identity access is lost | Protected key recovery plus permission/integration reconstruction | Healthy web servers | Application can access only its intended dependencies again |
| Notification provider times out | Observable uncertain state and controlled reconciliation | Blind unlimited retries | No false completion claim and no uncontrolled duplicate side effect |

The design uses different mechanisms because these failures differ. Saying “high availability enabled” cannot settle all five.

### 8. Show the financial tradeoff honestly

The cost model has at least eight lines: web compute, database compute/storage, object storage and operations, messaging, observability, networking/egress, resilience capacity and identity/security licensing. It distinguishes steady baseline from usage-sensitive cost. A secondary-region warm environment may shorten recovery while adding ongoing cost; a colder design may save steady cost while making recovery time less predictable.

The architect presents alternatives with the same workload assumptions and notes what each excludes. Prices must be checked for the actual region, currency, plan and commercial arrangement. A monthly estimate without assumptions about retention, traffic and replicas is not decision-grade evidence.

### 9. State the conclusion and what remains unresolved

For this fictional brief, choose a managed application and relational core with separate object storage and durable background work, not a Kubernetes platform or a globally writable document database by default. Keep the reporting path tolerant and separate. Adopt identity-scoped access and observability that follows business requests. Select exact plans from documented capability requirements rather than brand familiarity.

The design still requires current region/SKU confirmation, representative performance evidence, a priced capacity model and authorized operational validation before real deployment. Those are implementation needs, not claims that this course includes labs. The completed teaching outcome is a defensible, connected set of service and plan choices with visible tradeoffs, not an assertion that the service is already live.
