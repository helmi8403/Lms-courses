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
