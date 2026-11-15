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
