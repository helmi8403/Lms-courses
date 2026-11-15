# Identity and authorization: separate the gates

**Learning purpose:** Distinguish identity proof, permission, privileged access and secret management across Azure and hybrid systems.

## Authentication is not authorization
Authentication establishes an identity; authorization determines what that identity may do. A successful sign-in is not proof that an application can read a database or change a resource. Human access, workload access and customer access have different lifecycle and risk requirements. Design each deliberately rather than using an administrator account as a universal credential.

Azure RBAC binds a principal to a role at a scope. Prefer the narrowest scope and capabilities that satisfy a real task. A management-plane role and a data-plane role are not interchangeable: operating a storage resource is a different concern from reading its stored content. Also account for inherited assignments when explaining effective access. [S07: Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

## Workloads and managed identities
A managed identity lets supported Azure workloads acquire Microsoft Entra tokens without application teams managing a password or secret. A system-assigned identity shares the resource lifecycle; a user-assigned identity can have an independent lifecycle and be associated with resources. Neither grants access by itself: the target must support the authentication mechanism and the identity still needs appropriate authorization. [S08: Managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)

An architect checks how identity behaves during replacement, scaling and recovery. A tightly coupled identity can simplify ownership but complicate resource replacement. A shared identity can simplify deployment but enlarge the impact of a mistaken permission. Avoid one identity per entire organization merely to reduce administrative effort.

## Hybrid access and governance
An on-premises dependency may require a protocol or directory integration that differs from a cloud-native service. Inventory the protocol, directory authority, trust relationship and network route before proposing a hybrid authentication design. “Use Entra ID” is not a sufficient explanation of how a legacy application accepting only a particular authentication protocol will behave.

For people, distinguish standing permissions from eligible, time-bound privileged access. Access reviews and lifecycle processes address a different failure mode from authentication: someone can authenticate correctly yet no longer have a business need for access. Guest access requires sponsorship, expiry and review just as employee access does. Specific identity-governance capabilities and licensing must be checked for the selected tenant. [S09: Identity governance](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview)

## Secrets, certificates and cryptographic keys
Key Vault separates sensitive material from application configuration and provides controlled access to secrets, keys and certificates. The three are not synonyms: a secret is retrieved sensitive data; a cryptographic key supports cryptographic operations; a certificate binds identity to a public key and has its own lifecycle. A design must name who creates, rotates, revokes and recovers each artifact. [S10: Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)

## Worked example: a service that reads invoices
Contoso’s invoice API should read invoice data but not alter deployment policy. Its workload identity receives a narrowly scoped data-access role. The deployment operator receives a separately defined management role. The operator’s ability to deploy code remains a security consideration, because code deployed under a powerful workload identity may exercise that identity’s permissions. This is why separating accounts alone is insufficient: review the complete path by which authority can be exercised.

The decision note states the identity owner, target permissions, token audience, credential-free path where supported, rotation responsibility for unavoidable secrets, and recovery behavior. It does not record passwords, private keys or tokens.

## Mechanism comparison: cloud and hybrid sign-in
Password hash synchronization allows cloud authentication using synchronized password-derived information. Pass-through authentication validates through an on-premises agent, introducing an on-premises availability dependency. Federation delegates authentication to a separate identity provider and is appropriate only when its requirements justify the additional operating complexity. Synchronization and authentication are separate decisions: selecting a synchronization technology does not itself settle the sign-in method. [S42: Hybrid authentication selection](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn)

**Worked decision:** Contoso wants staff cloud access to continue during an on-premises outage. If its security requirements permit password hash synchronization, cloud authentication is a candidate that avoids depending on a live on-premises validation agent for each sign-in. If a policy requires on-premises validation, the architect documents that dependency, agent resilience and incident procedure. Federation is not selected simply because it sounds more enterprise-oriented.

## Conditional Access is a policy decision, not a password store
Conditional Access evaluates signals such as user, application, device and risk to require controls or deny access. A requirement for stronger authentication can be expressed as policy rather than embedded separately in every application. The design must consider licensing, affected identities and emergency access before enforcement. Report-only evaluation helps understand impact; it is not equivalent to blocking unsafe access. [S43: Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)

**Worked decision:** A staff member using an unmanaged device may be allowed to read low-sensitivity information but not perform a privileged operation, depending on application support and policy. The architecture records the intended access rule, not merely “enable MFA.” It also states how staff regain access during a device or authentication outage without turning a temporary exception into permanent broad access.

## Legacy application access and directory protocols
Application proxy is a candidate for remote access to supported on-premises web applications through Entra preauthentication and connector-based access. It is not a universal replacement for every network protocol. Validate the application’s authentication and single-sign-on requirements, and make connector availability part of the dependency design. [S44: Application proxy](https://learn.microsoft.com/en-us/entra/identity/app-proxy/overview-what-is-app-proxy)

Entra Domain Services provides managed domain features such as domain join, LDAP and Kerberos/NTLM. It is distinct from Entra ID’s modern identity service and is not a drop-in answer to every legacy Active Directory requirement. Check schema, administration and trust requirements before selecting it. [S66: Microsoft Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview)

**Worked decision:** An old web application needs remote employee access, while a separate legacy service needs domain-style authentication. The first may fit application proxy; the second requires a directory-protocol assessment. Combining them under “hybrid identity” without separating protocols would produce an incomplete design.

## Privilege activation and effective access
PIM can make privileged assignments eligible and time-bound, with activation conditions such as approval or stronger authentication. An access review asks whether access should continue; PIM asks how privilege is activated and controlled. Neither substitutes for a correctly scoped role. [S45: Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)

The application owner also distinguishes Entra directory roles from Azure resource roles. An identity administrator’s directory responsibilities do not imply the application’s data-access design. When documenting authorization, name the principal, operation and resource scope, then inspect inherited access. A custom role is justified by a real gap in built-in roles, not by a preference to duplicate them.

## Customer access is not employee guest access
External ID supports both business collaboration and customer identity scenarios. B2B collaboration brings partners into a workforce context with controlled access. Customer identity uses an external-tenant configuration for consumer or business-customer applications. A supplier who needs internal collaboration and a public customer registering for a service do not automatically belong in the same identity design. [S76: External ID](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview)

**Worked decision:** Contoso invites a contracted administrator to a limited internal resource scope with sponsorship and expiry. Patients using its public-facing application follow a separately designed customer identity journey. Neither identity type receives broad Azure administration rights merely by signing in. The application maps authenticated identity to authorized business actions.

## Vault or Managed HSM: select custody, not prestige
Key Vault handles secrets, certificates and cryptographic keys. Managed HSM is a dedicated key-management offering with single-tenant HSM protection and a distinct access-control and recovery model; it is not a general secret or certificate store. Select it when explicit key-custody or isolation requirements justify its operational and cost implications. Do not choose it simply because the name sounds stronger. [S67: Managed HSM](https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/overview)

Soft delete and purge protection address different deletion stages. Recovering a vault does not automatically restore every integrated role assignment or event subscription. The recovery plan therefore includes authorization and integration reconstruction, not just key material. Rotation also requires consumer compatibility: keeping an old version temporarily may be necessary while dependent services transition. [S68: Vault recovery](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview)

**Complete authorization example:** a production support group is eligible for a narrowly scoped operational role; developers have ordinary access only in development; a workload identity reads only its own required data and secrets. A central platform assignment is inherited where intended, but a clinical exception is not granted at a parent scope that would expose unrelated workloads. An access review removes a departed contractor, while PIM controls temporary privilege for a remaining operator. Each mechanism addresses a different lifecycle stage.
