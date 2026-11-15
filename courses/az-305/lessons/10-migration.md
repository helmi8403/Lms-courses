# Migration: move a dependency system, not a server list

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
