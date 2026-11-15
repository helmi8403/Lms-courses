# Expanded edition: objective-depth audit response

15 November 2026. This records manuscript work, not live implementation evidence.

**Status meanings:** mentioned = named only; explained = mechanism and tradeoff taught; demonstrated = original worked design reaches a choice or illustrates a concrete consequence. Demonstrated does not mean deployed or tested.

| Teaching area | Status | Concrete addition |
|---|---|---|
| Human and hybrid identity | Demonstrated | Hash synchronization, pass-through and federation selection; Conditional Access; proxy and directory protocols |
| External access | Demonstrated | Workforce partner versus customer identity journey |
| Effective authorization | Demonstrated | Inheritance, management/data access, privilege activation and review lifecycle |
| Secret/key custody | Demonstrated | Vault/HSM selection, rotation and deletion recovery dependencies |
| Resource governance | Demonstrated | Explicit hierarchy, policy effects, remediation, exceptions and locks |
| Monitoring | Demonstrated | DCRs, instrumentation, alert selection, workspace and retention reasoning |
| Relational platforms | Demonstrated | Azure SQL options and PostgreSQL alternative; tier and compute distinction |
| Relational protection | Demonstrated | Identity, private access, keys, auditing and restoration design |
| Document storage | Demonstrated | Consistency options, partition tradeoff and illustrative RU calculation |
| Object/file storage | Demonstrated | Access contracts, redundancy, retrieval and lifecycle selection |
| Analytics/integration | Demonstrated | Weekly reporting versus immediate stream signal; warehouse/lake alternatives |
| Continuity | Demonstrated | SQL failover/PITR/LTR, Cosmos multi-region, VM placement and recovery arithmetic |
| Compute | Demonstrated | Constrained App Service choice; rejected AKS; Functions hosting and batch arithmetic |
| Integration | Demonstrated | Command/event/stream selection, API boundary and cache-aside consequence |
| Configuration/deployment | Demonstrated | Artifact promotion, Bicep, staged alternatives and schema rollback limits |
| Network | Demonstrated | DNS/private access, explicit egress, hybrid routes and security-layer choices |
| Migration | Demonstrated | DMS, Storage Mover/AzCopy/Data Box; downtime and reconciliation decisions |
| Integrated architecture | Demonstrated | Measurable fictional brief, selected services, rejected options and evidence still needed |

## Remaining limits, stated rather than hidden

- No universal guarantee that all possible related exam topics or every SKU configuration are covered.
- Exact regional compatibility, quotas, licensing, current prices and implementation procedures require the referenced product documentation.
- No practice exams, videos or labs, as directed by the owner.
- Visual assets, screenshots and PDF/PPT layout require separate production QA; this manuscript audit cannot certify them.
- Numerical examples are explicitly invented teaching inputs, not measurements or Azure service promises.
- The authoring draft has roughly 11,500 words and 78 source references. Do not advertise it as Microsoft Official Curriculum or an accredited product.
