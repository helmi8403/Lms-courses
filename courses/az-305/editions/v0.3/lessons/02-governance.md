# Governance: organize ownership before enforcement

**Learning purpose:** Design resource boundaries, compliance controls, tagging and identity governance without confusing their purposes.

## Build a governance model whose inheritance can be explained

A useful resource hierarchy is an argument about ownership and controls. Management groups apply governance above subscriptions, with inheritance into descendants. Subscriptions grouped together must trust the same Entra tenant. This is why a management group is not simply a folder for unrelated customers. [Management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview).

### Concrete hierarchy decision

| Scope in fictional Contoso | Purpose | Example control | Reason not to place it higher |
|---|---|---|---|
| Platform management group | Shared connectivity and operations subscriptions | Platform ownership and common audit requirements | Workload teams should not inherit platform administration |
| Regulated-workloads management group | Workloads with a shared jurisdiction policy | Approved-region restrictions | Marketing may legitimately use different regions |
| Clinical-production subscription | Production billing/access boundary | Restricted deployment roles | Development engineers do not need equivalent production rights |
| Clinical-development subscription | Safe development lifecycle | Budget and allowed-resource controls | Its disposable-resource assumptions must not govern production |
| Records resource group | Independently retained resources | Explicit retention ownership | Application replacement should not imply records deletion |

These are original design examples, not a prescribed Azure hierarchy. Their merit is that a reviewer can explain where a rule originates and which descendants it affects. A hierarchy that mirrors every reorganization may create churn without improving control. A single flat subscription may be simpler initially but can fail to express genuinely different ownership or isolation requirements.

A common anti-pattern is placing a restrictive policy at the root and creating a large collection of exceptions below it. Exceptions are sometimes necessary, but if nearly every workload needs one, the assignment boundary may be wrong. Another anti-pattern is putting an owner tag on a resource and treating it as permission. Metadata does not enforce access. Tags support cost allocation and discovery; authorization and policy remain separate mechanisms.

### Select the control from the intended effect

| Intent | Candidate control | What it does not prove |
|---|---|---|
| Decide who can perform an operation | RBAC | Resource properties satisfy organizational standards |
| Report a disallowed resource configuration | Audit policy | The configuration was corrected |
| Block a matching create/update request | Deny policy | Existing resources were repaired |
| Adjust supported properties | Modify effect with appropriate remediation design | Every property is modifiable or historical resources are already corrected |
| Add required related configuration | DeployIfNotExists with permissions and remediation | Assignment alone completed all historical deployment |
| Reduce accidental management deletion | CanNotDelete lock | Individual data objects are protected from deletion |
| Prevent applicable management changes | ReadOnly lock | Every data-plane operation is prohibited |

Effects differ by resource type and lifecycle; remediation requires its own identity and permissions. [Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics). Locks constrain supported control-plane operations and can also interfere with normal management activities. [Resource locks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources).

**Worked decision:** Contoso wants supported resources to send diagnostic logs to an approved destination. The architect starts by discovering existing resource types and available categories. Audit establishes the initial compliance picture. A suitable deploy-if-not-exists policy can support configuration, but the remediation identity’s rights are deliberately scoped and the existing-resource remediation is separately tracked. Calling the policy assignment “monitoring complete” would be incorrect because data flow still needs evidence.

The architecture also evaluates an exception: a resource does not support the same diagnostic category. The response is not to force an imaginary setting. Record the unsupported requirement, alternative evidence and an owner for the residual gap. A technical limitation becomes a visible decision rather than a silent exclusion from the compliance denominator.

### Tag policy as an operating contract

A tag dictionary should state allowed values, accountable owner and handling of missing values. Consider `workload`, `environment`, `businessOwner` and `costCentre`, but use the organization’s actual reporting needs. A tag containing a personal name may become stale or expose information unnecessarily; a team identifier can be more stable. Sensitive information, secrets and access codes do not belong in tags.

Suppose a cost report excludes untagged resources. It may show excellent cost allocation precisely because it omitted the poorly governed resources. The report should show unallocated cost explicitly. If tags are inherited or appended through policy, clarify when that behavior occurs and what happens to pre-existing resources. Otherwise managers may believe changing a parent tag immediately changes every historical child resource.

### Identity governance as an evidence chain

Governance has three separate questions: should a person receive access, should they still retain it, and when should they activate privilege? Entitlement and approval processes address the first; access reviews address the second; privileged activation addresses the third. These processes depend on accurate sponsorship and resource ownership. A review sent to someone who cannot understand the resource is formally complete but operationally weak.

**Worked decision:** a supplier supports Contoso for three months. The design records the sponsor, permitted applications, expiry and reviewer. Privileged operations require an eligible assignment and a controlled activation path where supported. The supplier’s contract extension triggers a new access decision; it does not rely on someone remembering to remove a standing administrator role. The audit record shows the business justification without disclosing credentials.

### Governance rollout and reversibility

Governance changes should be treated as changes to a functioning operating system, not administrative housekeeping. A broad deny policy can prevent a recovery deployment. A ReadOnly lock can block an expected management operation. A tag remediation can affect billing reports. Before enforcement, identify affected scopes, exceptions, recovery procedures and evidence of impact.

The original teaching sequence is: describe intent, discover current state, choose a control, evaluate impact, obtain appropriate change authority, apply to a bounded scope, review results, then expand if justified. It is not an executable lab and it is not permission to change a tenant. Its purpose is to show why control rollout is part of architecture.

### What governance cannot settle by itself

A policy evaluating a region property does not prove every integrated service, backup and telemetry destination meets a residency obligation. A lock does not prove a document is recoverable. An access review does not prove that no alternate credential exists. A cost-center tag does not prove the invoice is correct. Strong design identifies the precise evidence each control produces and the separate review still required.

The final governance decision record contains the intent, scope, inheritance, control mechanism, remediation authority, exemption process, evidence date and owner. If any of those fields is absent, the organization may know which product was enabled without knowing what operational promise it makes.
