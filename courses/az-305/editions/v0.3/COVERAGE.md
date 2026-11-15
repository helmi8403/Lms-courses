# v0.3 coverage and limits

Alignment reference: [AZ-305 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305), skills measured from 17 April 2026. Product facts checked 15 November 2026.

The table maps broad objective groups to actual teaching, not a guarantee of examination readiness. Every listed section teaches service alternatives and worked reasoning; implementation validation is not claimed.

| Area | Chapter | Concrete teaching in this edition |
|---|---|---|
| Identity/access | 01 | Human/customer/workload patterns, hybrid protocols, licensing, privilege, key custody |
| Governance | 02 | Hierarchy, inheritance, policy effects, remediation, exemptions and locks |
| Monitoring | 03 | Collection mechanisms, table plans, retention/query/alert implications and response |
| Relational data | 04 | SQL DB/MI/VM/PostgreSQL; purchasing, tiers, compute, pools and protection |
| Document/object/file data | 05 | Cosmos modes/consistency; file/object interfaces; access tiers and redundancy |
| Integration/analytics | 05 | Movement runtime, warehouse/lake/stream alternatives and selected use cases |
| Recovery/availability | 06 | Failure domains, platform-specific recovery and RTO/RPO tradeoffs |
| Compute | 07 | App Service, Functions, containers, AKS, VM families and batch plan decisions |
| Application architecture | 08 | Messaging tiers, API Management, Redis, configuration and release choices |
| Networks | 09 | Routing, security products/plans, load balancing, hybrid paths, DNS and egress |
| Migration | 10 | Compatibility, source/target tooling, downtime, transfer and cutover choices |
| Synthesis | 11 | Explicit fictional requirements, selected plans, traffic contract and cost model |

## What changed from v0.2

The service chapters have been rebuilt, not merely padded with more general warnings. They contain named plan alternatives, decisive capability constraints, selected and rejected choices, current documented caveats and capacity/cost reasoning. Six Azure stencil diagrams have been added and embedded in the chapter source. The word and table counts are recorded in `build-manifest.json` rather than estimated in this document.

## Boundaries that remain real

- No promise to enumerate every SKU, hardware size, region, quota, protocol variant or future exam item. The official guide allows related topics beyond its illustrative bullets.
- Licensing tables explain capability selection; they do not establish a particular customer's contractual entitlement.
- Numerical workload examples are fictional. Prices and measured latency/failover claims are not fabricated.
- Some preview/product-generation distinctions can change. Their dated source matters.
- Detailed operator procedures and live validation are outside this explanatory course. The owner excluded labs, practice exams and videos.
- Export layout, table pagination, diagram legibility and official screenshot attribution require artifact-production QA separate from source review.

Treat this as detailed independent instruction with transparent limits, not an official or exhaustive Microsoft certification product.
