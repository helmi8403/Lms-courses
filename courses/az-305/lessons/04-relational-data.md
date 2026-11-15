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
