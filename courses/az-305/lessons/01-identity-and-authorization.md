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
