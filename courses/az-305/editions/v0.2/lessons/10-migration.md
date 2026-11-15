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
