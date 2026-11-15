# Governance: organize ownership before enforcement

**Learning purpose:** Design resource boundaries, compliance controls, tagging and identity governance without confusing their purposes.

## Resource organization is an operating model
A useful hierarchy reflects stable control boundaries, not every temporary organization chart. Management groups can group subscriptions for inherited governance. Subscriptions can separate operational or billing boundaries. Resource groups collect related resources for lifecycle management. Tags provide descriptive metadata; they do not create an authorization boundary. [S11: Resource organization](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org)

Start by identifying owners, environments, legal constraints and isolation needs. Then select the hierarchy. Avoid placing unrelated production workloads in a shared lifecycle container simply because a diagram looks shorter. Conversely, needless fragmentation creates policy exceptions, duplicated administration and poor visibility.

## Policy, permissions and locks do different jobs
Azure Policy evaluates resource properties against organizational rules and supports compliance reporting and enforcement effects. Azure RBAC governs who can perform actions. A policy can constrain an allowed operation; it does not replace identity authorization. An audit result is evidence about an evaluated condition, not certification that the complete organization is compliant. [S12: Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

Control design should include rollout sequencing. Begin with an understood scope and measurable effect. Investigate existing exceptions before enforcing a denial that could disrupt deployment. Name the exception owner, rationale and expiry. “Permanent exception” without periodic review gradually becomes an undocumented second policy.

## Tags and compliance evidence
Choose a small mandatory vocabulary, such as business owner, workload, environment and cost center. Define allowed values and who maintains them. Tag consistency matters more than tag count. Do not store personal information or secrets in metadata that may be broadly visible. Reporting must account for untagged resources rather than silently excluding them.

Governance evidence has freshness and scope. A compliance report taken before the latest deployment cannot prove the new deployment meets policy. A successful check in a development subscription cannot prove an inherited production policy is identical. Preserve the evaluated scope and time with the finding.

## Worked example: two departments and one platform team
Contoso has a regulated clinical workload and an internal marketing site. Both use a shared platform team, but their data controls differ. The architect separates the workload boundaries while reusing common policy definitions. Department-specific exceptions are recorded independently. A central group can view compliance without needing every developer to administer every subscription.

The design note explicitly avoids using the word “secure” as an absolute conclusion. It states what each control prevents, what it detects, who responds and what remains outside its coverage. This makes governance review practical rather than a checklist of product names.
