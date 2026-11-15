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

## Select an effect that matches the governance intent
Audit records noncompliance; deny blocks matching requests under the rule’s applicable behavior. Modify and deployIfNotExists can support correction or deployment of related configuration, subject to their definitions and permissions. Existing resources may require remediation; assigning a policy is not proof that historical resources were fixed. Effects differ by resource lifecycle and must not be swapped casually. [S46: Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics)

**Worked decision:** Contoso wants required diagnostic settings on new and existing resources. The architect first inventories support and destinations, then evaluates an applicable policy and its remediation identity. A simple deny would only prevent a request that violates the rule; it would not populate the missing historical telemetry. The rollout record distinguishes the assignment, existing compliance state and authorized remediation.

## Design the hierarchy from conflicting requirements
Suppose marketing and clinical services share a platform team but need different permitted regions. Place the difference at a scope that makes inheritance understandable. Avoid a broad parent policy followed by dozens of undocumented exclusions. The shared team’s role can be granted independently from the policy scope; organizational responsibility need not force identical technical controls.

A resource group should normally make lifecycle management clearer. Resources with different retention or independent ownership may not belong in one deletion boundary. A tag called “production” is useful metadata but cannot enforce production isolation. An environment label should therefore be backed by the actual role and policy model.

## Explain the limits of a compliance result
A technical rule can test whether a property has an approved value; it may not establish that the chosen value satisfies a legal or business obligation. A region restriction does not automatically resolve every data-residency question, because backups, telemetry and integrated services also require analysis. The design identifies the evidence each control produces and the human review still required.

The governance record includes policy owner, assignment scope, exemption rationale, expiry and evidence date. This is a worked documentation pattern, not a claim that any tenant has passed compliance review.

## A concrete hierarchy and its consequences
In the fictional model, the organization has a platform management group and a workloads management group. The workload branch separates regulated and general workloads where policies differ. Clinical production and development use separate subscriptions because authorization and operational controls differ. Within clinical production, application and independently retained records use lifecycle-appropriate resource groups.

This is one possible model, not a Microsoft-mandated hierarchy. Its advantage is understandable inheritance. Its cost is additional subscription and policy administration. A small organization may rationally choose fewer boundaries if it can still express its actual controls clearly. The architectural justification is the requirement, not the number of boxes.

## Locks do not replace backup or permissions
A CanNotDelete lock prevents applicable control-plane deletion; a ReadOnly lock restricts applicable control-plane changes. Locks apply to management operations, not every data-plane operation. They can also interfere with operations that appear read-oriented but use management APIs in unexpected ways. Authorized users with appropriate rights can manage locks, so they are not an immutable security boundary. [S69: Resource locks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

**Worked decision:** protecting a storage account resource from accidental deletion does not prove that individual documents cannot be overwritten. Contoso combines an appropriate management safeguard with separately designed data recovery. The team documents the maintenance procedure and who may remove the safeguard rather than sharing a privileged credential to work around it.
