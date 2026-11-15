# Application architecture: decouple without losing correctness

**Learning purpose:** Explain messaging, events, APIs, caching, configuration and deployment as connected design decisions.

## Commands, events and streams
A command asks for work; an event describes something that happened. Service Bus, Event Grid and Event Hubs address different messaging patterns rather than being interchangeable queues. Choose from delivery requirements, ordering, throughput, replay, fan-out and consumer behavior. Assume duplicates can occur unless the complete end-to-end design establishes otherwise. Idempotent processing is often essential. [S30: Asynchronous messaging](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/messaging)

Decoupling does not remove dependencies; it changes their timing. A consumer that is unavailable creates a backlog. Design retention, dead-letter handling, observability and the response to poison messages. A retry without a limit can amplify an incident. A retry with no idempotency strategy can duplicate business effects.

## APIs and integration
API Management can provide a managed gateway and policies for publishing and controlling APIs. Authentication at the gateway is not automatically sufficient authorization inside every backend. Consider versioning, throttling, transformations, client identity and failure behavior. A gateway can become a critical dependency and needs its own continuity design. [S31: API Management](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts)

## Cache and configuration
A cache can lower latency and backend load but introduces staleness and invalidation decisions. Define the source of truth, expiration, cache-miss behavior and whether stale content can be served. Never treat cached permissions as harmless merely because they improve speed. Azure Managed Redis is a candidate for managed caching; service lifecycle and migration guidance matter when selecting a current offering. [S32: Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/overview)

Configuration has a lifecycle distinct from application binaries. Azure App Configuration can centralize configuration and feature flags, while secret values should use an appropriate secret store. Design rollback of a flag or setting, not only rollback of code. Configuration changes can cause incidents even when no binary is deployed. [S33: App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/overview)

## Automated deployment
A deployment design includes source version, artifact identity, configuration, environment promotion, checks, rollout strategy and rollback limits. Infrastructure as code can make intended configuration reproducible, but applying it can still be destructive. Approval should bind to a specific change rather than a vague project name. A rollback must consider data compatibility, not just redeploying old code. [S34: Safe deployments](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments)

## Worked example: duplicate appointment notifications
A worker sends a notification and crashes before acknowledging the message. Delivery resumes and the notification may be sent again. The architect records a business identifier and an idempotency strategy that survives worker replacement. A service’s duplicate-detection capability may help, but it is not a blanket guarantee about an external email provider. The lesson is to reason across the boundary where the actual side effect occurs.

## Select the message service from the interaction
Service Bus fits brokered enterprise messages where queues, topics and delivery controls matter. Event Grid fits event distribution and reactive integration. Event Hubs fits high-throughput event streams with independent consumers. The choice depends on the delivery model and processing semantics, not merely message size. [S55: Messaging service comparison](https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services)

**Worked decision:** Contoso sends a durable request to create an invoice, notifies interested systems that a document arrived, and ingests a continuous telemetry stream. These can reasonably use different patterns. The invoice path needs explicit handling of failed work; the document event may fan out; the telemetry stream may be replayed independently by consumers. One universal queue would obscure their different needs.

## API boundaries and failure behavior
An API design needs a contract, version policy and authorization model. The gateway can enforce selected controls, but the backend must still understand the caller’s permitted business action. Rate limiting protects capacity; it is not a substitute for authorization. Transformations can simplify consumer migration but may hide an incompatible backend if not governed.

For Contoso’s appointment API, the architect distinguishes public availability searches from authenticated booking writes. Caching a public search result may be acceptable for a short documented period, while a booking transaction requires authoritative validation. The API should not promise an available slot solely because a cached search showed it.

## Cache-aside as a concrete pattern
With cache-aside, the application checks the cache, loads missing data from the source and populates the cache. Updates require an invalidation strategy. Expiration limits staleness but does not guarantee immediate consistency; a cache miss surge can overload the backend. Access-sensitive data needs especially careful scoping and invalidation. [S65: Cache-aside pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside)

**Worked decision:** Contoso caches clinic descriptions, which change rarely, but does not use that cache as the authority for a staff member’s current permission to amend appointments. The latency benefit is preserved where stale data is tolerable. The authorization path remains tied to an approved access design.

## Deployment and configuration must be reversible in meaning
A blue-green or progressive rollout can limit exposure, but only if traffic and health evidence match the intended cohort. A schema change that removes a field used by the older release may prevent simple rollback. Feature flags can separate release of code from enabling behavior, but flag evaluation and configuration access introduce dependencies. The decision note records compatibility across versions and a stop condition; it never labels an unexecuted rollback as proven.

## A concrete automation design
A fictional Contoso pipeline starts from a reviewed source revision, builds one versioned application artifact, records its identity and promotes that same artifact between environments with separately versioned configuration. Bicep is a declarative Azure infrastructure option; it expresses intended resources but does not make every change harmless or eliminate drift. [S75: Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)

The pipeline separates identity used to build from identity used to deploy. A controlled environment supplies deployment authority, and secret values are not embedded in source. The design record identifies what changes automatically and what needs a deliberate release decision. This is a conceptual pipeline, not an executable workflow or a live authorization.

For a compatible application, a staged rollout can expose a limited population first; a blue-green approach maintains separate candidate and current environments. Both require defined health evidence and a safe treatment of database versions. If old and new versions cannot read the same schema, switching traffic back may not restore service. The selected approach therefore depends on compatibility, not only speed of deployment.

**Worked integration choice:** an external provider’s synchronous API is used when the user truly needs its immediate result. If the business permits completion later, a queued command isolates the user response from provider delay. The application must expose pending and failed outcomes honestly. Asynchronous design is not permission to report completion before work is done.
