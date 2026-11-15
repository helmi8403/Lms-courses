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
