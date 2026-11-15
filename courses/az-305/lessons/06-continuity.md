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
