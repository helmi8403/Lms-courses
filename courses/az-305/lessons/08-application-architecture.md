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
