# Pilot: the exam and the architect’s job

**Learning purpose:** Understand the credential route, the scope of AZ-305 and how to reason about design before choosing a product.

## Course status and boundaries
This is an independently authored learning course, not Microsoft Official Curriculum and not an accredited training product. It explains architectural choices through original fictional examples. Public Microsoft documentation is the authority for product behavior. There are no exam dumps, practice-exam questions, videos or labs in this edition. Worked examples illustrate reasoning; they are not claims about actual examination content.

The verified study guide is the edition with skills measured from 17 April 2026. Its four weighted areas are identity, governance and monitoring (25–30%); data storage (20–25%); business continuity (15–20%); and infrastructure (30–35%). These weights guide study allocation, not a promise about a particular examination’s item distribution. [S01: AZ-305 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305)

## Exam essentials
AZ-305 is Designing Microsoft Azure Infrastructure Solutions. Passing it alone does not award Azure Solutions Architect Expert: Microsoft also requires the Azure Administrator Associate certification. The published passing score is 700 on a scaled score, not a statement that 70% of questions must be correct. Price depends on the country or region in which the exam is proctored; check the booking flow rather than budgeting from a foreign-currency quotation. [S02: AZ-305 exam](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-305/) [S03: Azure Solutions Architect Expert](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/) [S04: Exam scoring](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports)

Do not plan around an asserted fixed question count. Microsoft’s generic role-based examination policy distinguishes 100-minute non-lab exams from 120-minute exams that may contain labs; booking time also includes other activities. The AZ-305 page does not settle which applies to a future appointment. Confirm the actual appointment, permitted aids, accommodations and local identification rules before scheduling. Course videos, labs and practice exams are excluded at the owner’s request; the pilot still explains the exam. [S05: Exam duration and experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience)

## What an architect produces
An architect translates an ambiguous request into a defensible decision. “Make it fast and resilient” is not a measurable requirement. A useful design brief identifies the user journey, peak demand, acceptable latency, data sensitivity, recovery time, tolerated data loss, ownership and cost ceiling. A design decision then records the alternatives, the reason for the chosen option, its failure modes and the evidence that would invalidate it.

Azure Well-Architected Framework provides five lenses: reliability, security, cost optimization, operational excellence and performance efficiency. These lenses reveal tradeoffs. A second live region may improve continuity while increasing cost and reconciliation complexity. Cloud Adoption Framework complements workload design with organizational adoption and operating considerations. [S06: Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)

## Worked example: Contoso appointment booking
Contoso’s fictional booking application serves clinics across two regions. The initial request is “always available.” The architect instead documents: booking writes must not be duplicated; viewing appointment availability can tolerate stale data; staff need a clear degraded-mode procedure; and an outage must have an accountable incident owner. This separates the availability of a screen from the correctness of a transaction.

The design is deliberately incomplete until stakeholders specify targets. Choosing a multi-region database before resolving conflicting-write behavior would conceal a business decision inside technology. The teaching point is to identify the missing requirement explicitly, not fill it with an invented service-level promise.

## Reading sequence
Start with identity and governance, then observability, storage, continuity, compute, integration, networking and migration. Revisit earlier decisions after later chapters: network isolation changes monitoring access; database recovery changes application behavior; deployment design changes rollback safety. Each chapter ends in a worked design note rather than an assessment.

## Examination logistics are part of readiness
Exam duration is the answering time; seat duration includes surrounding instructions and administrative activities. During applicable role-based exams, Microsoft provides restricted access to Microsoft Learn from the examination interface. This is not unrestricted internet access, access to personal notes or extra time. The examination interface and current policy govern which content is available. [S05: Exam duration and experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience)

Prepare the correct booking account, required identification and testing environment, and request necessary accommodations through the official process before the appointment. A certification renewal assessment is distinct from taking AZ-305; Microsoft’s current role-based renewal route should be checked through the credential page. This course does not enroll the learner, purchase an exam or make an appointment. [S03: Azure Solutions Architect Expert](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/)

A score report indicates performance by area but does not disclose the exact items answered incorrectly. Use it as directional evidence rather than reverse-engineering a count of correct answers from a bar chart. The scaled score exists to account for differences in examination difficulty. [S04: Exam scoring](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports)
