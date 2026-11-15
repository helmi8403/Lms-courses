# Documents, objects and integration: design for access patterns

**Learning purpose:** Choose semi-structured and unstructured storage and explain how operational data becomes analytical data.

## Match the model to the work
Relational, document, key-value and object models solve different access problems. List the operations first: point lookup, join, aggregation, ordered scan, binary retrieval or search. Combining stores can be justified when access patterns genuinely differ, but every added store creates another consistency, recovery and operations boundary. [S17: Data models](https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/understand-data-store-models)

For document-oriented workloads, partition design is architectural. A partition key affects distribution, hot spots and the cost of cross-partition work. Test how growth changes distribution and how a single popular tenant behaves. Flexible schema is not the absence of a contract: consumers still rely on meaning and versioning. Azure Cosmos DB requires explicit attention to partitioning and supported consistency choices. [S18: Cosmos DB partitioning](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning)

## Object storage and durability
Binary assets, documents and large immutable objects often fit object storage. File shares serve a different access model and may be appropriate when applications require file protocols. Choose access tier and lifecycle policy from expected access frequency, retrieval requirements and retention rules rather than price per stored unit alone. Retrieval charges and delay can dominate a supposedly cheap tier. [S19: Blob access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

Azure Storage redundancy options address different failure boundaries: local, zone and geographic protection. Geographic replication can involve a lag, and read access to a secondary is a separate consideration. Redundancy is not a complete defense against logical deletion or corruption; recovery features and retention remain part of the design. [S20: Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

## Data integration and analysis
An integration design names the source, ingestion mode, transformations, destination, schema contract, quality checks and replay strategy. Batch is suitable where delay is acceptable; streaming may be justified where action depends on fresh events. Azure Data Factory provides orchestration and data-movement capabilities, while analytical platform selection depends on the processing and consumption model. Do not select an entire analytical platform merely because a connector exists. [S21: Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/introduction)

## Worked example: images and appointment trends
Contoso stores appointment records, uploaded scans and anonymized trend aggregates. Keeping all three as database blobs would simplify one interface but may fit their access patterns poorly. The design separates transactional facts from object assets and curated analytical output. A stable identifier links them, while permissions and retention are defined per category.

The analytical pipeline must handle late and duplicate events. It records lineage and an agreed freshness target. The worked design does not claim that removing a name alone anonymizes data: privacy review must consider the combination of fields and reidentification risk. Exact handling rules belong to the organization’s approved policy.

## Analytical storage is not the transactional database with a new label
An analytical serving layer is optimized for reading and aggregating prepared data. A warehouse can support structured reporting; a lake-oriented approach retains data for varied processing; a lakehouse combines relevant capabilities. The design evaluates concurrency, query style, data shape, freshness and the team’s tools. “Big data” alone is not a selection criterion. [S49: Analytical data stores](https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/analytical-data-stores)

Microsoft Fabric offers integrated ingestion, engineering, analytics and reporting experiences over a shared platform. Azure Databricks and Azure Synapse may also appear in an analytical shortlist, depending on processing and existing investments. Fabric is a current contextual option, not a claim that every Fabric component is explicitly examined in AZ-305. [S50: Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview)

Stream Analytics supports processing streaming data with a SQL-oriented approach. Choose a streaming path only when timely event processing has business value; batch processing is often simpler where delay is acceptable. A pipeline must decide how event time, late arrival and duplicate events affect the result. [S51: Stream Analytics](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction)

**Worked decision:** Contoso wants a weekly utilization dashboard and immediate detection of a queue surge. The weekly dashboard can use a scheduled curated dataset, whereas the surge signal needs fresher processing. Sending both through the most complex real-time system would add operating burden without improving the weekly decision. Conversely, a nightly refresh cannot support a response measured in minutes.

## Reason explicitly about a partition
Imagine one clinic contributes most of Contoso’s bookings. A partitioning strategy based only on clinic identity could concentrate demand. A strategy based only on a random identifier could distribute writes but make clinic-level queries more expensive. The architect compares distribution with dominant query patterns and transaction scope. There is no universally correct partition key.

Schema flexibility also requires versioning. A newly introduced document field may be absent from older records. Consumers need an agreed meaning for absence, null and default values. This protects the analytical pipeline from silently counting older records incorrectly.

## Make lifecycle cost visible
A rarely retrieved archive may fit a low-access tier, but an urgent recovery requirement could make retrieval delay unacceptable. A file share may fit an application expecting file semantics, while object storage better fits direct object retrieval. The worked recommendation identifies the access contract first and evaluates lifecycle cost second, rather than treating all stored bytes as equivalent.

## Consistency choices explained
Strong consistency offers the latest committed value; bounded staleness constrains how far reads may lag; session consistency provides guarantees within a client session; consistent prefix preserves update ordering without guaranteeing freshness; eventual consistency permits temporary divergence before convergence. The chosen API and account configuration constrain their use. Stronger consistency can trade latency and availability for a simpler freshness model. [S71: Cosmos DB consistency](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels)

**Worked decision:** a user editing a profile expects to see that edit on the next read, while a global popularity counter can tolerate delay. Session-oriented behavior may suit the former interaction, whereas weaker freshness may suit the counter. Neither conclusion automatically makes either model suitable for allocating the last available appointment. That transaction needs its own correctness design.

## Throughput is more than stored gigabytes
Cosmos DB expresses operation consumption in request units. Item size, indexing and query shape affect consumption. Provisioned throughput, autoscale and serverless differ in capacity and billing behavior; choose a supported mode using demand shape and required capabilities, not only average traffic. [S77: Cosmos request units](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units)

**Illustrative sizing, not a benchmark:** suppose a fictional measurement found an operation cost of 6 RU and the workload expected 200 such operations per second. That component alone implies 1,200 RU/s before other operations, growth and safety margin. These are invented teaching inputs, not a product guarantee. A hot partition can still constrain performance even when aggregate capacity appears adequate.

## Storage selection matrix in prose
LRS keeps redundancy within a primary location; ZRS spans zones in a region. GRS adds asynchronous secondary-region replication to local redundancy; GZRS combines zone resilience with geographic replication. Read-access variants allow secondary reads under their supported behavior; a replicated secondary is not automatically a writable active endpoint. [S20: Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

Hot, cool and cold blob tiers support online access with different storage/access cost tradeoffs; archive requires rehydration before ordinary reading. Exact minimum-retention, retrieval and account-support rules must be checked. File services are candidates when a protocol such as SMB or NFS is required; object APIs suit object-oriented access. [S19: Blob access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

**Concluded analytical decision:** for the fictional weekly utilization report, select a curated warehouse-style serving dataset rather than repeatedly querying the transactional database. For mixed exploration over retained files, evaluate a lake/lakehouse workflow separately. Select streaming analysis only for the queue-surge signal. This choice prioritizes different freshness requirements instead of forcing all data into one processing cadence.
