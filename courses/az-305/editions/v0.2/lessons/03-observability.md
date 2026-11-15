# Observability: design a useful evidence path

**Learning purpose:** Choose telemetry, routing, retention and alerts around service decisions rather than collecting everything.

## Select evidence for the question
Metrics answer numerical questions over time, logs provide discrete records, and distributed traces help connect work across component boundaries. Azure Monitor brings these telemetry types into an observability platform. The architecture should distinguish platform health, application behavior and user outcomes rather than treating a healthy virtual machine as proof of a working service. [S13: Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview)

A symptom such as slow checkout can have several causes: a database bottleneck, downstream timeout, exhausted connections or an application regression. Design correlation identifiers and consistent timestamps before an incident. Ensure they do not disclose personal information. A dashboard without reliable joins between components often describes the problem without locating it.

## Routing is a design decision
Resource diagnostic settings can route supported platform logs and metrics to destinations such as a Log Analytics workspace, storage or Event Hubs. Destination choice depends on analysis, retention, integration and cost requirements. Not every telemetry category or resource behaves identically; verify the supported categories and regional constraints for the chosen service. [S14: Diagnostic settings](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/diagnostic-settings)

Workspace boundaries should reflect access, residency and operations. One workspace may simplify cross-service investigation, while separated workspaces may support necessary isolation. Duplication has ingestion, retention and privacy costs. A routing plan should name the category, destination, retention, access owner and reason for collection.

## Alerts must lead to action
Separate a signal from a notification and from a response. CPU utilization can be a diagnostic signal without being the best page-the-on-call condition. Customer-visible error rate or availability may be closer to the service commitment. Thresholds require a baseline, a measurement window and a treatment of missing data. Missing telemetry is not necessarily evidence of health.

Avoid assuming that all anomalies warrant automatic remediation. The response may need approval, rate limits, suppression during maintenance or manual diagnosis. Excess notifications can hide the event that matters. Every alert needs an owner, a runbook and a review date.

## Worked example: an empty dashboard
Contoso deploys a service and sees no errors in its dashboard. The team initially assumes success. The architect notices the dashboard also shows no requests. There are at least two competing explanations: no traffic or failed collection. A meaningful acceptance check confirms a known synthetic event reaches the intended destination and that access controls expose it to the responder. This example illustrates validation, not an instruction to run a live test.

The resulting design includes collection health, application outcomes and infrastructure indicators as distinct signals. Retention for audit records is justified separately from the short window used for operational alerting.

## Choose collection mechanisms deliberately
Data collection rules define collection, processing and routing for supported Azure Monitor paths. With the relevant agents or ingestion paths, they can specify what is collected and where it is sent. They are not a universal replacement for resource diagnostic settings. Verify which path the telemetry uses before recommending a rule or transformation. [S47: Data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

Application Insights supports application performance monitoring, including supported OpenTelemetry instrumentation. Application dependencies and request traces can explain behavior that platform metrics cannot. Sampling can reduce volume but affects what is available for investigation; the design should explain which observations require unsampled or separately retained evidence. [S63: Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

**Worked decision:** Contoso needs to distinguish slow database calls from slow external messaging calls. Platform CPU charts are insufficient. The proposed evidence path correlates application requests with dependencies. It records whether instrumentation covers both dependencies and what happens when a client library does not propagate context. Missing spans remain a coverage gap rather than being treated as fast operations.

## Match alert type to signal
Metric alerts evaluate numerical time-series signals; log search alerts evaluate queries over logs; activity log alerts respond to management-plane events. Service Health and Resource Health signals answer different questions from an application’s business error rate. An action group identifies actions or notifications, but routing a notification does not prove a responder acted. [S64: Azure Monitor alert types](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-types)

**Worked decision:** A deployment change and a rise in failed bookings occur close together. The monitoring design needs an activity/change record plus application telemetry, not a single CPU threshold. The change might be causal or coincidental; the responder correlates time, scope and affected requests before deciding. The alert text should not declare “deployment caused outage” merely because the events are nearby.

## Retention, access and ingestion cost
Operational responders may need detailed recent logs while audit reviewers need selected longer-lived evidence. Design retention separately by purpose and check the supported table or storage options. Avoid collecting secrets and then relying on analysts never to query them. Filtering or transformation must preserve the evidence required for the stated purpose.

A fictional monthly cost estimate should account for ingestion volume, retention and duplicated destinations. A query spanning many workspaces can simplify a central view without erasing the access boundaries. The design records the intended reviewer’s ability to access each dataset; otherwise a dashboard may look complete only to an administrator.
