# Compute: choose the responsibility you can operate

**Learning purpose:** Compare virtual machines, managed web hosting, containers, serverless and batch without treating modernization as an end in itself.

**Edition:** AZ-305 independent teaching expansion v0.3. Product documentation checked 15 November 2026. This chapter teaches choices, not a deployment procedure. All Contoso figures and decisions are fictional worked examples. No examination questions, labs or videos are included.

## 7.1 Choose the execution model before the price tier

Compute selection has two layers. First decide the operating model: virtual machine, managed web application, container platform, event-triggered function or scheduled parallel work. Then select the plan that supports the required features and capacity. Starting with “the cheapest tier” often produces a design that cannot provide its required network path, deployment method or operating-system capability.

Write a workload card with these fields: supported runtime; process lifetime; HTTP or event trigger; persistent state; custom image or OS requirement; expected demand shape; minimum acceptable responsiveness after idle time; inbound and outbound network requirements; required platform control; deployment frequency; and the team that will operate it. A blank field is a requirement to resolve, not permission to assume an unlimited platform.

| Workload constraint | Initial candidate | Why it fits | Reason to reject it |
|---|---|---|---|
| Supported web runtime, standard HTTP application, small platform team | App Service | Managed application hosting without cluster administration | Required OS customization or unsupported hosting feature |
| Containerized service, event-driven scaling, no Kubernetes API requirement | Container Apps | Application-oriented container execution | Essential cluster-level control unavailable in the managed abstraction |
| Kubernetes controllers, ecosystem or cluster-control requirement | AKS | Kubernetes operating model | Team cannot own the required operational responsibilities |
| OS agents, unusual dependencies, specialized licensed software | Virtual Machines | Broad machine-level control | Managed hosting meets requirements with less responsibility |
| Short event-driven work with compatible programming model | Functions | Trigger-focused execution | Required image, runtime or execution behavior unsupported by chosen host |
| Large collections of scheduled independent tasks | Batch | Pool and task scheduling | Work is really an always-on interactive service |

This is an original decision framework, not a Microsoft ranking of products. The right answer changes when the workload card changes. For example, putting a web application into a container does not create a Kubernetes requirement. Similarly, a familiar VM deployment does not prove that operating-system control is necessary.

## 7.2 App Service: distinguish the application from its plan

An App Service plan defines the compute on which its applications run. Applications in the same dedicated plan share that plan’s instances. Free and Shared use shared infrastructure with quotas; Basic through Premium use dedicated plan compute; Isolated v2 adds the App Service Environment isolation model. Tier availability depends on operating system and region. [Microsoft: App Service plans](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans)

| Plan family | Appropriate design intent | Reject or upgrade when |
|---|---|---|
| Free / Shared | Learning, evaluation and low-stakes development | Production capabilities, capacity or isolation are required |
| Basic | Simple dedicated hosting with modest requirements | The release design needs deployment slots or more advanced scale capabilities |
| Standard | Production web hosting requiring staging slots and a broader operational feature set | Required capacity or premium-only capabilities exceed the tier |
| Premium generations | More demanding capacity and supported advanced features | The requirement is actually full environment isolation rather than larger shared-platform hosting |
| Isolated v2 / ASE v3 | Dedicated isolated environment justified by explicit requirements | Ordinary managed hosting already meets the requirement at lower complexity |

### Current feature constraints that can decide the tier

The documented comparison includes Premium v4; Premium v3 is not the latest generation name. Selected current limits are below, not a replacement for the table’s footnotes. [Microsoft: App Service limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-app-service-limits)

| Tier | Documented maximum scale-out | Staging slots per app |
|---|---:|---:|
| Basic | 3 instances | Not available |
| Standard | 10 instances | 5 |
| Premium v1 | 20 instances | 20 |
| Premium v2/v3/v4 | 30 instances | 20 |
| Isolated | 100 instances, more by request | 20 |

These are service limits, not evidence that a particular subscription can immediately allocate every size in every region. The selected SKU still needs capacity and compatibility verification. A requirement for six staging slots excludes Standard even if CPU demand is tiny; a requirement for two ordinary slots does not justify Premium by itself.

The distinction between Standard and Premium is not that one is “secure” and the other is not. Identify the feature, isolation, performance or scale requirement that drives the decision. Premium generations are not interchangeable in every region or operating system. A plan change also affects the other applications sharing that plan, so a small application can inherit the consequences of a large neighbor’s scaling decision.

Deployment slots are supported in Standard, Premium and Isolated tiers. They are live applications, not offline folders. Swaps move supported content and configuration between slots; some settings remain slot-specific. Slots consume resources from their plan. A slot swap does not reverse a database migration or external side effect. [Microsoft: deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)

**Worked choice:** Contoso has a small staff portal with a supported runtime, steady demand and a requirement to validate a candidate release before switching production traffic. Standard is the starting candidate because the slot requirement excludes Basic. The architect does not select Premium merely because the portal is important. Representative capacity evidence and any additional required feature decide whether Standard remains sufficient. Isolated is rejected because the organization has not specified a requirement for that environment model.

**Capacity reasoning:** suppose three applications share one plan. Their peaks occur simultaneously at the start of a working day. Adding their average CPU usage is misleading because their coincident peak matters. Moving one workload to a separate plan can be more useful than increasing every application’s shared resource pool. Conversely, unrelated low-demand applications can share capacity economically when isolation and simultaneous peaks are understood.

Scale-up changes plan capacity or features; scale-out changes instance count. A larger instance can help a memory-bound process, while more instances help only if requests and state can distribute correctly. Neither repairs a serialized application lock or a saturated downstream database automatically. [Microsoft: App Service scaling](https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up)

## 7.3 Functions: the host changes the architecture

Current Microsoft guidance identifies Flex Consumption as the default starting point for new serverless function apps. Premium, Dedicated and Container Apps hosting support other scenarios; legacy Consumption has different operating-system and lifecycle constraints. Host selection affects scaling, network integration, available resources, containers and billing. [Microsoft: Functions hosting comparison](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale)

| Hosting candidate | Use when | Important rejection test |
|---|---|---|
| Flex Consumption | Variable compatible event-driven code; managed scaling and VNet connectivity needed | A custom container or unsupported runtime/OS is essential |
| Premium | Prewarmed capacity, supported container use or steady workloads justify it | Idle baseline cost outweighs required benefits |
| Dedicated App Service plan | Existing dedicated capacity or controlled instance allocation is appropriate | The design depends on automatic serverless economics it does not provide |
| Container Apps | Function programming model must run as a supported container alongside other services | Container packaging and environment model add no value |
| Legacy Consumption | Existing compatible application with a justified transition plan | It is chosen for a new application using assumptions copied from old guidance |

**Worked choice:** a document-notification handler receives a burst of work after uploads, then may be idle. It uses a supported runtime and does not need a custom image. Flex Consumption is the initial candidate. If a proprietary native library requires a custom Linux container, the decision changes: Premium or Container Apps hosting becomes relevant. Calling both designs “Azure Functions” does not settle the hosting question.

A function timeout setting is not a business durability guarantee. Even where a host permits long execution, process replacement, platform activity and dependency failure still matter. An HTTP caller also has its own timeout. Holding an HTTP request open while a long job finishes can be the wrong interaction even if the worker can continue running.

Durable Functions supplies stateful orchestration using orchestrator, activity and entity functions, with runtime-managed state and recovery. It is suitable for workflows requiring durable progress rather than one enormous in-memory function. It does not make an external payment, email or other side effect magically exactly-once. [Microsoft: Durable Functions](https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview)

**Worked workflow:** Contoso receives a request, accepts it with a durable operation identifier, processes a document, waits for an external response and records the result. A restart must resume from durable progress, not lose the operation. The user sees pending, completed or failed status honestly. The design separates the orchestrator’s durable history from idempotency at the external side-effect boundary.

## 7.4 Container Apps: consumption and dedicated profiles

Container Apps offers Consumption and Dedicated models. Consumption suits demand-driven use, including scale-to-zero. Dedicated workload profiles provide dedicated capacity choices, including specialized hardware, and are billed at the profile-instance level rather than as an independent fixed machine per application. A workload-profiles environment can accommodate different needs. [Microsoft: Container Apps plans](https://learn.microsoft.com/en-us/azure/container-apps/plans)

| Candidate | Strong fit | Cost or design consequence |
|---|---|---|
| Consumption profile | Intermittent or variable services within supported resource requirements | Minimum replicas and active work determine how much scale-to-zero helps |
| Dedicated profile | Steady load, larger or specialized capacity, explicit compute isolation | Provisioned profile capacity can remain a cost even when an individual app is quiet |
| Container Apps job | Finite containerized work triggered manually, on schedule or by events | Completion, retry and timeout policy must be designed |
| AKS instead | Kubernetes-specific controllers or platform capabilities are essential | Cluster responsibilities become part of the workload’s operating cost |

A continuously running application and a finite job have different lifecycles. Container Apps jobs run work that ends, while applications typically serve continuing traffic or events. Jobs and apps share environment capabilities, but choosing a job does not establish its success criterion or make partial output safe. [Microsoft: Container Apps jobs](https://learn.microsoft.com/en-us/azure/container-apps/jobs)

**Worked choice:** a container receives HTTP traffic throughout the day while a nightly import runs for a finite period. Contoso uses an application for the HTTP service and evaluates a job for the import. It does not keep a permanently running container solely to sleep until midnight. For the import, completion means all intended records were reconciled, not merely that the container exited with a status code.

**Sizing consequence:** imagine two services each needing a large peak allocation but at different times. Shared dedicated profile capacity might be efficient if the peaks genuinely do not overlap. If both peak together, the aggregate requirement must fit. The illustration is about demand correlation, not a claim that every possible profile or scaling behavior is available in every region.

## 7.5 AKS: cluster tier is separate from worker capacity

AKS offers Free, Standard and Premium cluster-management tiers. Free has no financially backed uptime SLA; Standard targets production requiring uptime SLA coverage; Premium adds long-term support capabilities under its applicable support plan. Nodes, disks, networking and other resources still have costs. Current documentation also distinguishes Base and Automatic SKUs; Automatic is preconfigured with Standard cluster management. [Microsoft: AKS pricing tiers](https://learn.microsoft.com/en-us/azure/aks/free-standard-pricing-tiers)

| Tier | Choose for | Do not infer |
|---|---|---|
| Free | Development, evaluation or appropriate non-production use | Free worker machines or production uptime commitment |
| Standard | Production cluster management with required SLA coverage | The application itself has achieved its availability target |
| Premium | A justified long-term support requirement | Freedom to ignore application, node or security maintenance |

The cluster-management tier is only one dimension. Worker node family, pool layout, availability placement, pod resources, network design, upgrade policy and workload architecture remain independent decisions. A more expensive control plane cannot compensate for one replica of a stateful application with no recovery plan.

**Worked choice:** Contoso operates a platform that requires custom Kubernetes controllers and already has a capable platform team. Standard is the initial production tier; Premium is considered only if a documented supported-version lifecycle requirement calls for long-term support. The team separately sizes worker pools and allocates workloads. If that Kubernetes requirement disappeared, a managed application platform would return to the shortlist.

A cluster is also an organizational boundary. Several teams sharing a cluster may save infrastructure cost but create common upgrade schedules, operational dependencies and failure impact. Separate clusters can improve boundaries while increasing management effort. The architecture must explain which resources are shared, who owns their changes and how a failed rollout affects other tenants.

## 7.6 VM families and Batch: choose the bottleneck

Azure VM families emphasize different ratios and capabilities: general purpose, compute optimized, memory optimized, storage optimized, GPU and high-performance computing. Exact series determine processor architecture, temporary storage, disk and network behavior. Size names alone are insufficient: regional availability, quota and compatibility also matter. [Microsoft: VM sizes](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)

| Evidence from workload | Family direction | Why a different family may lose |
|---|---|---|
| Balanced modest CPU and memory | General purpose | Specialized resources remain unused |
| High sustained CPU, modest memory | Compute optimized | Paying mainly for additional memory does not help |
| Large working set or memory pressure | Memory optimized | More CPU does not prevent paging |
| High local storage throughput requirement | Storage optimized | Network/disk limits dominate a compute-only choice |
| Supported accelerator computation | GPU | Unsupported application cannot exploit the accelerator |
| Tightly coupled scientific computation | HPC-capable candidate | Network and parallel-runtime constraints may dominate |

**Worked sizing:** a licensed legacy component is memory-bound at 24 GB while using little CPU. Contoso starts with a memory-oriented candidate rather than a large general-purpose size selected only by vCPU count. It checks the license’s core implications and storage/network limits before concluding that candidate is cheaper. The choice remains conditional on measurements, not an invented benchmark.

Batch manages pools of compute nodes and schedules jobs and tasks. It is appropriate for large parallel workloads where scheduling, pool lifecycle and task execution are central requirements. Application packages, input/output handling and task logic still need design. [Microsoft: Azure Batch](https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview)

For a fictional 2,400 independent tasks at five worker-minutes each, the work is 12,000 worker-minutes. With 100 fully utilized workers the ideal lower bound is 120 minutes, before startup, transfer, skew and failures. Doubling workers can help only if input delivery and output storage can keep up. If the deadline is two hours, the ideal calculation alone already leaves no margin.

Spot or interruptible capacity can reduce cost when the work tolerates interruption, but lost progress changes the economics. A checkpointable simulation differs from a task whose entire six-hour result disappears on eviction. The design should compare total expected completion cost, not only the quoted rate of a single machine.
