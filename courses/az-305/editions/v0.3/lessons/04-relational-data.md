# Relational data: choose compatibility and operating responsibility

**Learning purpose:** Evaluate relational platforms, compute and service tiers, scaling, security and recovery as one design.

**Source verification:** 15 November 2026. These sections are independently written teaching material. Exact prices and region-specific SKU availability are deliberately not invented. Numerical examples are fictional inputs used to demonstrate decisions, not benchmark results. No practice examination, lab or video is included.

## 04.1 Separate the five decisions hidden in “choose a database”

A database recommendation is not complete when it names Azure SQL. It must answer five distinct questions: which engine and compatibility boundary; which deployment model; which performance and availability architecture; which compute consumption model; and which recovery design. A strong recommendation can be expressed as a sentence: “Use this engine on this managed deployment, in this tier with this compute allocation, because these measured needs require it; recover with these mechanisms.” This exposes assumptions that a product logo hides.

Begin with transaction correctness. Identify what must commit together, whether concurrent writes can conflict, and which reads can tolerate delay. Then record engine dependencies, typical and peak demand, working-set size, data growth, recovery targets and operator capability. Do not choose a database solely from data size. A small, latency-sensitive transaction workload can be harder to serve than a much larger archive. Conversely, a large database does not automatically need expensive transaction compute if it is seldom queried.

The distinction between a *hard constraint* and an *optimization preference* is important. A required unsupported extension can rule out a managed platform; a preference for an existing console should be weighed against the cost of running the underlying infrastructure. The design should name the exact constraint. “Legacy” is not a technical requirement, and “cloud native” is not evidence of fit.

## 04.2 Choose a deployment model before a tier

| Candidate | Select when | Reject or reassess when | Design obligation that remains |
|---|---|---|---|
| Azure SQL Database | The application fits a database-scoped managed SQL Server-engine service | Required instance/OS features are unsupported | Data access, query behavior, tier, recovery and application resiliency |
| Azure SQL Managed Instance | Instance-oriented SQL Server compatibility is valuable while keeping managed operation | OS-level access or a specific unsupported feature is mandatory | Compatibility validation, virtual-network design, capacity and instance lifecycle |
| SQL Server on an Azure VM | Engine/OS control or a required component makes managed placement unsuitable | The team cannot justify patching, backup and HA responsibilities | OS and SQL operations, disks, licensing, replicas and recovery |
| Azure Database for PostgreSQL | The application uses PostgreSQL and fits its supported managed capabilities | Required extension, privilege or version behavior is incompatible | Compute tier, connection behavior, maintenance, recovery and extensions |

This matrix is a selection aid, not a compatibility guarantee. The [Azure SQL deployment comparison](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview?view=azuresql) distinguishes the SQL family’s control/responsibility boundaries. [PostgreSQL’s managed-service overview](https://learn.microsoft.com/en-us/azure/postgresql/overview) establishes the separate engine option. A PostgreSQL application should not be forced into a SQL Server-engine service simply because both are relational.

**Worked decision: a packaged payroll application.** Fictional Contoso discovers that the vendor requires an operating-system agent beside SQL Server. The agent cannot be removed and the vendor does not support the managed alternatives. SQL Server on a VM is therefore the selected candidate, despite the greater operating burden. The rejection of SQL Database is tied to a vendor-supported dependency, not nostalgia. The architecture assigns patching, backup and recovery ownership explicitly. If the vendor later supports a managed deployment, that becomes a review trigger rather than an obligation to keep the VM forever.

**Worked decision: a new PostgreSQL service.** A different Contoso team uses PostgreSQL-specific data types and a supported extension. Azure Database for PostgreSQL is the starting candidate because engine conversion provides no business benefit. A VM is not selected merely to imitate the existing development machine. The team verifies extension and privilege compatibility, then chooses the managed compute and availability configuration appropriate to production.

## 04.3 DTU and vCore are purchasing models, not application architectures

| Model | What it expresses | Useful fit | Potential mismatch |
|---|---|---|---|
| DTU | A bundled resource measure across compute and I/O characteristics | A team wants a compact purchasing abstraction for a suitable workload | Independent CPU/memory/storage reasoning or particular vCore-only options are required |
| vCore | Explicit compute allocation with related hardware, storage and service-tier choices | Migration sizing, workload-specific capacity choices and eligible licensing benefits | The team assumes a vCore alone predicts query latency |

DTU uses Basic, Standard and Premium service tiers, while the vCore model uses General Purpose, Business Critical and Hyperscale for SQL Database. Do not mix “Premium” in the DTU model with every Azure product that also has a Premium label. The names are product-specific. [DTU purchasing model](https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-dtu?view=azuresql), [SQL Database vCore model](https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-sql-database-vcore?view=azuresql).

A purchasing model is not a substitute for profiling. If an application is blocked by a poorly selective query, purchasing more resources may hide the problem temporarily. The architect separates query design, indexing, concurrency, connection management and service capacity. The capacity recommendation explains what is actually saturated. “Database slow” is not enough to distinguish CPU, storage latency, transaction-log pressure or lock contention.

## 04.4 Service tier changes the performance and recovery architecture

| SQL Database vCore tier | Architectural reason to consider it | When not to choose it automatically | Evidence required |
|---|---|---|---|
| General Purpose | Balanced managed relational workloads without a demonstrated need for a specialized architecture | The workload has proven I/O-latency or scale requirements beyond its fit | Representative latency and throughput at the selected capacity |
| Business Critical | Demanding transactional I/O and resilience needs justify local-storage/replica architecture | “Production” is the only reason offered | Value of lower latency and required availability relative to cost |
| Hyperscale | Large-scale storage/growth or its separated compute/storage architecture suits the workload | A small ordinary workload is assumed to become faster merely from the name | Compatibility, growth, replicas and recovery behavior for this architecture |

Tier choice affects more than maximum size. It changes storage/replica behavior and which features are available. Treat tier-specific documentation as the authority; do not transplant the SQL Database table into Managed Instance. The [vCore comparison](https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-sql-database-vcore?view=azuresql) describes these architectures.

**Worked decision: predictable transaction traffic.** Contoso’s fictional booking service has a steady daily load. General Purpose is the initial candidate because there is no evidence that a more specialized tier is necessary. The design defines the latency and concurrency it must satisfy. Business Critical becomes justified if representative evidence shows that its I/O/resilience characteristics solve a material requirement. It is not rejected forever; it is rejected as an unsupported first assumption.

**Worked decision: fast growth.** Another workload has a rapidly growing relational dataset and independent read-serving needs. Hyperscale enters the shortlist because the architecture may fit those requirements. The team records the behavior of replicas, restore and cross-region movement rather than assuming that all operations are independent of data size. A favorable headline capacity does not settle the end-to-end design.

## 04.5 Provisioned, serverless and pooled capacity answer different questions

| Choice | Select when | Avoid or qualify when | Cost behavior to model |
|---|---|---|---|
| Provisioned single database | Regular activity, predictable baseline and prompt response after idle periods matter | Capacity is idle for long intervals without a business need | Continuously provisioned compute plus storage/backup |
| Serverless single database | Intermittent demand and autoscaling fit, and warm-up/resume behavior is acceptable | The application cannot tolerate pause/resume effects or maintains constant activity | Actual/minimum compute behavior, storage, pause eligibility |
| Elastic pool | Many databases have noncoincident peaks and can share bounded resources | All tenants peak simultaneously or one tenant dominates | Pool capacity and per-database bounds, not simply database count |

Current SQL Database documentation describes serverless for General Purpose and Hyperscale, with configurable scaling ranges. General Purpose auto-pause/resume is available; Hyperscale auto-pause/resume is currently preview. Serverless is not supported in Business Critical or DTU. “Serverless” does not mean zero charges whenever the application sends no business requests: minimum compute, memory activity, pause eligibility and storage still matter. [Serverless compute](https://learn.microsoft.com/en-us/azure/azure-sql/database/serverless-tier-overview?view=azuresql).

Elastic pools share resources among databases on the same logical server. They are especially useful when low average use is accompanied by peaks occurring at different times; a pool is not infinite per-tenant capacity. Set bounds and analyze aggregate demand. [Elastic pools](https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-pool-overview?view=azuresql).

**Pool arithmetic, with fictional measurements.** Ten tenant databases each average 0.2 units and occasionally reach 2 units. Buying 2 units for every tenant reserves 20 units. If observed peaks rarely overlap, a smaller shared pool might be sufficient. But if a scheduled month-end job makes all ten peak together, the aggregate still reaches 20. An average of 2 across the group hides that event. The lesson is to model correlation, not merely multiply averages. These arbitrary units illustrate reasoning; they are not DTU-to-vCore conversion factors.

**Serverless decision.** A monthly administrative tool is inactive for long periods and its first user can tolerate a short start-up delay. Serverless is a reasonable candidate if the supported configuration can pause as intended. A public booking API with tight first-request latency receives a different recommendation, even if both databases have identical storage size.

## 04.6 Managed Instance has its own tier boundary

| Managed Instance option | Reason to shortlist | Important distinction |
|---|---|---|
| General Purpose | Balanced instance-oriented workloads | Managed Instance is not SQL Database with a different label |
| Next-gen General Purpose | Greater capacity or improved throughput/flexibility is needed within this family | Check supported hardware, availability and migration behavior |
| Business Critical | High I/O performance and replica-based resilience justify the cost | Read/HA characteristics do not remove application recovery design |

The current dedicated [Managed Instance service-tier table](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/service-tiers-managed-instance-vcore?view=azuresql) lists General Purpose, its next-generation option and Business Critical. Do not infer that SQL Database Hyperscale is a Managed Instance tier from generic prose elsewhere on a page. Managed Instance compute is provisioned; applicable stop/start functionality is not equivalent to SQL Database serverless autoscaling.

A migration recommendation should preserve this product boundary. For example, if an application needs instance-level compatibility, first establish that Managed Instance supports it. Only then compare its tier choices. Selecting Hyperscale first and later discovering that the application needs a different deployment model reverses the decision order.

## 04.7 PostgreSQL compute choices require workload shape

| PostgreSQL tier | Best-fit starting point | Counterexample |
|---|---|---|
| Burstable | Intermittent, predominantly idle nonproduction work that fits its credit behavior | Sustained production load exhausting CPU credits |
| General Purpose | Balanced production CPU/memory requirements | A genuinely memory-dominated workload repeatedly missing its working set |
| Memory Optimized | A larger memory-per-vCore requirement is established | Paying for memory without evidence that memory pressure matters |

The current [PostgreSQL compute documentation](https://learn.microsoft.com/en-us/azure/postgresql/compute-storage/concepts-compute) describes a credit model for Burstable and explicitly discourages it for production. Do not recommend a burstable tier simply because the initial database is small. A small database can still receive sustained CPU-intensive work.

**Worked decision.** A fictional service performs continuous transaction processing throughout business hours. General Purpose is selected over Burstable because sustained demand, not stored size, determines the choice. If query evidence later shows a memory-constrained working set, Memory Optimized is evaluated. The team first checks query/index behavior to avoid turning an inefficient query into a permanent hardware expense.

## 04.8 Protection is a layered design, not a checkbox

A complete relational design records the workload principal, permitted operations, network path, encryption/key ownership, audit destination, backup policy and recovery operator. Those controls solve different threats. Network isolation does not prevent an authorized bad update; encryption does not prevent a compromised application from reading data it is allowed to read; backup completion does not prove an application can reconnect after restoration.

Consider a fictional customer-managed-key requirement. It introduces a key availability and recovery dependency. If the key is unavailable, restoring database bytes may not restore service. The design must therefore include key custody, rotation compatibility, authorization in the recovery environment and the consequences of revocation. If no custody requirement exists, adding customer-managed keys solely as a prestige feature may add operational risk without a demonstrated benefit.

The recommendation ends with an explicit boundary: the course explains the architecture; it has not created, priced, benchmarked or restored any database.
