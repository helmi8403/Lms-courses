# Migration: move a dependency system, not a server list

**Learning purpose:** Evaluate readiness and migration strategy for applications, databases and unstructured data with clear cutover criteria.

## 10.1 Discovery produces a dependency model

Azure Migrate provides discovery, assessment and migration capabilities across supported workloads. Its assessments help establish readiness, sizing and cost inputs, but the application owner must still validate compatibility and business behavior. A migration plan needs application dependencies, not just a machine inventory. [Microsoft: Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview?view=migrate)

| Workload finding | Migration direction | Additional decision |
|---|---|---|
| Required OS dependency cannot be removed within deadline | Rehost to suitable IaaS candidate | Patch, backup and operational ownership |
| Supported web runtime with manageable changes | Replatform to managed hosting | Deployment, filesystem and network differences |
| Business value justifies substantial change | Refactor selected boundaries | Transition coexistence and scope control |
| Application no longer provides value | Retire with authorization | Retention, dependencies and evidence preservation |
| Constraint prevents move | Retain for now | Supported hybrid path and review trigger |

**Worked dependency:** the booking service has a nightly file import, a database used by reporting and an on-premises identity dependency. Moving only the web server creates a hybrid system whether or not the project intended one. The design must decide which dependencies move in the same wave and which remain temporarily reachable. The temporary state has cost, latency, security and support consequences, so it deserves an architecture of its own.

Do not call rehosting a failure merely because it is less modern. A deadline or compatibility requirement may make it the correct first move. Equally, do not promise later modernization without an owner, trigger and measurable benefit. A migration is complete when the agreed service, data and operating outcomes are met, not when a VM first boots.

## 10.2 Database migration: supported pair first

Database Migration Service supports documented source-target migration combinations, including scenarios intended to reduce downtime. The correct path depends on engine, source version, destination, available mode and current tools. “Online” does not mean that no cutover or validation is needed. [Microsoft: Database Migration Service](https://learn.microsoft.com/en-us/azure/dms/dms-overview)

| Requirement | Approach to evaluate | Principal tradeoff |
|---|---|---|
| Downtime window permits complete transfer | Offline migration | Simpler transition but longer interruption |
| Short write interruption | Supported synchronization/online path | More setup, catch-up and reconciliation complexity |
| Engine-specific features must remain | Compatible managed service or VM candidate | More control may mean more operating responsibility |
| Cross-engine change | Explicit conversion project | Schema, query and semantic compatibility effort |

**Worked decision:** Contoso’s database is too large to copy within a 20-minute write pause. The architect evaluates a supported online synchronization path, followed by a controlled freeze and final catch-up. If the exact source-target combination does not support that path, the proposal is rejected or changed; the label “DMS” cannot solve an unsupported pairing. The evidence list includes compatibility findings, lag at cutover, row or business-total reconciliation and the application’s connection switch.

**What rollback means:** before the target accepts writes, the source may remain authoritative. After target writes begin, reverting the application to the source risks losing or duplicating those writes unless a reconciliation strategy exists. This boundary belongs in the approval and runbook. A backup taken before cutover preserves a state but does not automatically preserve all later transactions.

## 10.3 Files and objects: transfer tool versus migration service

Storage Mover is a managed service for supported migration scenarios, including on-premises file/folder and supported object sources. Evaluate its source/target and protocol support rather than assuming all metadata or ACL semantics map unchanged. [Microsoft: Storage Mover](https://learn.microsoft.com/en-us/azure/storage-mover/service-overview)

| Candidate | Best-fit reasoning | Reject or qualify when |
|---|---|---|
| Managed storage migration | Repeated large migration with orchestration and monitoring | Source/target combination or metadata behavior unsupported |
| Supported command-line transfer tool | Controlled copying with appropriate automation | Team needs migration management the tool does not provide |
| Data Box offline transfer | Network window cannot move bulk data efficiently | Shipping/custody/import delay conflicts with deadline |
| Application-level export/import | Semantics matter more than raw files | Export loses required history, permissions or relationships |

Data Box transfers data using a shipped physical device. It can make bulk movement feasible where network constraints are severe, but device availability, region, logistics and import time matter. A final-delta plan is still needed if the source changes while the device is in transit. [Microsoft: Data Box](https://learn.microsoft.com/en-us/azure/databox/data-box-overview)

**Worked arithmetic:** assume a fictional 20 TB archive and sustained 200 megabits per second available for transfer. Using decimal units, the ideal payload time is approximately 800,000 seconds, or 9.26 days, before overhead and interruptions. If the permitted network window is eight hours per day, elapsed time increases substantially. This calculation does not recommend an exact device; it shows why an offline option enters the shortlist.

A migration acceptance check must distinguish bytes, names, metadata, permissions and application behavior. Matching file counts can conceal missing content or incorrect access. Hash validation may support content integrity but does not prove that the target application interprets the data correctly. The plan names the evidence appropriate to each property rather than using one vague “verified” flag.

## 10.4 A complete fictional wave decision

Contoso must relocate a supported web application, its relational database and a document archive. The application depends on a scheduled import and a directory service. The deadline is fixed, but the business permits a limited write pause and a longer period of read-only access if announced. These are invented requirements for teaching, not a live project plan.

The architect selects managed web hosting if runtime compatibility is confirmed, a compatible database target with a supported low-downtime migration approach, and a managed archive-transfer path. The scheduled import moves in the same wave or is explicitly paused. The directory dependency remains temporarily hybrid under a documented supported connection. A wholesale refactor is rejected because it adds scope without being necessary to meet the relocation objective.

The wave has five distinct evidence states: readiness established; initial transfer completed; final synchronization within agreed bounds; target business behavior accepted; and old dependencies safely retired. None is inferred from another. For example, initial copy completion does not authorize source deletion. Old resources may remain temporarily for retention or recovery, with cost and access explicitly tracked.

The cost comparison includes duplicate operation during transition, transfer and storage charges, temporary network capacity and staff effort. A cheaper steady-state platform can still have a more expensive migration. Conversely, retaining an unsuitable platform to avoid short-term work may produce greater long-term cost. The architect makes the time horizon explicit so the comparison is not manipulated by choosing only one month of expense.

## Scope and verification limits for this expansion

This source adds concrete plan and service selection, not every SKU’s full limit table. It deliberately does not invent currency prices, benchmark results, quotas for an unspecified subscription or guarantees for an unspecified region. The linked pages were checked on 15 November 2026. Recheck fast-changing plans and features before a real design is approved, especially Functions hosting, AKS SKUs/support, APIM classic-versus-v2 networking, Redis preview sizes and regional availability.

All examples are original instructional scenarios. None was executed against Azure. There are no practice exams, laboratory procedures or video activities. Detailed database and data-storage design belongs to the companion data chapter; this expansion explains the compute, application and migration decisions that depend on it.
