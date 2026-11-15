# Relational data: choose compatibility and operating responsibility

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
