# Azure stencil architecture plates

Six original teaching architectures assembled using unmodified Microsoft Azure service SVG icons from the official public icon package. The SVG embeds original icon SVGs; PNG is a rendered derivative of the composition. These are not official Microsoft architectures and do not claim deployment or validation.

Official icon source and usage terms: https://learn.microsoft.com/en-us/azure/architecture/icons/

The icon manifest records the package-relative file used for each symbol. Non-Azure buildings are original generic symbols for on-premises/external systems. Service diagrams use selected components; their captions state important omitted dependencies.

| File | Intended placement | Architectural meaning |
|---|---|---|
| 01-identity-hybrid | Identity chapter | Directory synchronization and workload permission are distinct lanes |
| 02-network-private-data | Network chapter | Public application path and privately addressed data path with DNS |
| 03-app-command-architecture | Application chapter | Synchronous authoritative transaction vs asynchronous durable command |
| 04-data-analytics | Data chapter | Operational inputs, orchestration, curated lake and analytical serving |
| 05-ha-dr | Continuity chapter | Asynchronous regional replication differs from historical recovery |
| 06-monitoring | Monitoring chapter | Application and guest telemetry collection paths converge for analysis |

## Technical caveats

- Identity plate: managed-identity association is conceptual, not a claim that identity is a network hop. Token acquisition and authorization still apply.
- Network plate: a private endpoint does not automatically disable a service's public access. NSGs, certificates, DNS, egress and roles remain explicit decisions.
- Application plate: database commit and message publish are not implied atomic. Use a deliberate consistency pattern.
- Data plate: Synapse is one worked candidate, not a universal recommendation over Fabric or Databricks.
- Continuity plate: historical backup location follows configured redundancy. The diagram does not specify a backup-storage SKU or guarantee RTO/RPO.
- Monitoring plate: diagnostic settings remain a separate path; DCRs are not a universal replacement. Alerts require configured action groups and human/process response.

Technical references: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn ; https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview ; https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview ; https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/messaging ; https://learn.microsoft.com/en-us/azure/data-factory/introduction ; https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db?view=azuresql ; https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview

Checked and composed 15 November 2026. Read at full-page landscape size. Preserve labels/captions and icon proportions when placing into PDF/PPT.
