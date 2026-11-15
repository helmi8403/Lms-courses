# Compute: choose the responsibility you can operate

**Learning purpose:** Compare virtual machines, managed web hosting, containers, serverless and batch without treating modernization as an end in itself.

## The selection axes
Compute design combines runtime compatibility, deployment unit, scaling behavior, networking, persistence and operational control. A service is suitable only if its constraints fit the application and the team. Managed does not mean responsibility-free: application security, data protection, configuration and service-specific operation remain relevant. [S26: Compute selection](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree)

Virtual machines are candidates when operating-system control, specialized dependencies or legacy compatibility are essential. Their flexibility comes with responsibility for image management, patching and workload resilience. A scale set can manage a fleet, but application state and lifecycle handling still need design.

## Containers are packaging, not an operating model
A container packages dependencies; an orchestration platform manages execution and lifecycle. Azure Kubernetes Service is a candidate when Kubernetes capabilities and control are justified. Azure Container Apps may fit application-focused container hosting with a different operating burden. App Service is another candidate for supported web applications. Select the platform based on required control rather than adopting Kubernetes by default. [S27: Container hosting comparison](https://learn.microsoft.com/en-us/azure/container-apps/compare-options)

Ask whether the team can operate upgrades, networking, identity, observability and incident response for the chosen platform. Portability of an image does not make every platform feature portable. Describe which dependencies would still bind the application to a platform.

## Serverless and batch
Functions are a candidate for event-triggered code; execution and scaling behavior depend on the hosting option. Serverless does not make a long-running, stateful process automatically suitable. Batch workloads emphasize scheduling many tasks, data locality, parallelism and completion deadlines. Azure Batch provides managed scheduling and compute-management capabilities for parallel and high-performance workloads. [S28: Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview) [S29: Azure Batch](https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview)

## Worked example: three jobs, three placements
Contoso has a public web application, an image-processing worker and a legacy licensed desktop component. They need not share one compute platform. The web application values managed web hosting; the worker values event-driven scale; the legacy component may need a VM-compatible environment. The architecture document lists why each placement is appropriate and what would trigger reconsideration.

The most important comparison is not “which platform is newest?” but “which platform meets the requirement with acceptable operating cost and failure behavior?” The design also checks whether asynchronous work can tolerate retries and whether temporary files survive the chosen execution model.

## Compare control with operational burden
A VM is a useful candidate when an application needs a particular operating-system capability or unsupported runtime component. App Service is attractive for supported web applications whose team values managed hosting. Container Apps can suit containerized services without requiring the team to manage a Kubernetes cluster directly. AKS becomes compelling when the required Kubernetes control and ecosystem justify its additional responsibilities. These choices are not a maturity ladder.

**Worked decision:** Contoso has three small HTTP services and no Kubernetes-specific requirement. Packaging them as containers does not by itself justify AKS. The architect starts with the simpler compatible managed option, then records which future requirement would justify changing it. The rejected alternative remains visible so the decision can be revisited without pretending the initial choice was universal.

## Scaling requires a unit of work
A stateless web request, a queue message and a multi-hour simulation have different scaling signals. Scaling HTTP compute from CPU alone may miss connection or dependency saturation. Queue depth can indicate delayed work, but increasing workers may overload a database. The design should state the limiting dependency and the safe upper bound.

For batch processing, separate the scheduler, worker capacity, input data and output integrity. A task should have a defined success condition and a treatment for interruption. Spot capacity may suit interruptible work but requires tolerance for eviction and verification of current product availability. A guaranteed completion deadline cannot be inferred from inexpensive capacity.

## State and replacement
Treat local temporary state as expendable unless the chosen service explicitly provides the required persistence. A container restart is a normal lifecycle event, not an exceptional disaster. Store necessary durable state in a designed data service and account for its latency and throughput. A local cache may improve performance, but its loss should not corrupt business state.

The worked architectural conclusion is that compute selection cannot be separated from data placement, scaling boundaries and operating capability. A service name alone is not a design.

## A specific compute selection
For this fictional workload, Contoso needs a supported web runtime, small operations team, stateless requests and no Kubernetes-only features. App Service is the selected candidate; AKS is rejected because its additional platform control is not required. If the application instead needs a custom container with event-driven scaling and no cluster administration requirement, Container Apps becomes a candidate. An unsupported OS dependency would change the decision toward a VM-compatible path.

## Hosting options change serverless behavior
Functions hosting determines scaling, instance resources, network integration, container support and billing. Current Microsoft guidance recommends Flex Consumption for new serverless function applications, with Premium, Dedicated and Container Apps options addressing other needs. Existing legacy Consumption behavior should not be assumed for new deployments. Verify operating-system and runtime compatibility before selecting a plan. [S74: Functions hosting](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale)

**Worked decision:** a short event-triggered transformation with variable traffic can start its evaluation with Flex Consumption. A required custom Linux image or different steady-capacity requirement changes the shortlist. A long business process should not be represented as one unbounded invocation merely to keep the diagram simple; orchestration and durable state need explicit treatment.

## Batch arithmetic and limits
Suppose 1,000 independent image jobs each need two minutes of worker time. Their total is 2,000 worker-minutes. At perfect utilization, 50 concurrent workers would require 40 minutes; real duration is longer because of startup, transfer, retries and skew. This arithmetic is illustrative and says nothing about actual Azure SKU performance. The design can trade concurrency cost against deadline, while respecting downstream storage and database limits.
