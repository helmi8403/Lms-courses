# Continuity: recovery objectives before redundancy

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
