# ITIL (Version 5) — Detailed Learning Course

## Start here

**An independently authored learning course, not an accredited PeopleCert course or a replacement for official courseware.** First track: ITIL (Version 5) Foundation. Lessons below teach concepts through an original fictional case. Other Version 5 qualifications are separate tracks and are not claimed to be covered here.

**Edition baseline:** PeopleCert-authored Foundation syllabus, version 5.0, February 2026, available through the provider-hosted [syllabus PDF](https://fasttracklearningsolutions.com/wp-content/uploads/2026/02/ITIL_Version5_Foundation_Syllabus_v5.0.pdf). Check the latest official syllabus before examination preparation. Seven syllabus areas guide this course: terminology, four dimensions, lifecycle, value system, value streams, AI, and complementary approaches. **Per-criterion verification of all 95 assessment criteria remains pending; this edition must not be represented as exhaustive exam coverage.**

Created 15 November 2026 (SGT). Dates follow Singapore Time (SGT). No certification, exam pass, completed study or implemented business improvement is implied.



## Learning route and evidence of learning

Read the lessons in sequence, use the worked explanations to connect each concept to a decision. Memorizing a definition is not the same as applying it. Keep a learner notebook with four columns: concept, example, decision, evidence that would show success.

| Module | Focus | Learner output |
| --- | --- | --- |
| 1 | Digital products, services and value | Outcome-and-stakeholder brief |
| 2 | The four dimensions | Balanced service assessment |
| 3 | Product and service lifecycle | Lifecycle decision portfolio |
| 4 | Value system and improvement | Governance and improvement proposal |
| 5 | Value streams | Delay and hand-off investigation |
| 6 | AI-enabled service management | Bounded AI use-case assessment |
| 7 | DevOps, PRINCE2 and integrated working | Delivery and operations operating agreement |

**Original case: Harbour Learning.** A fictional training company sells short professional courses. Its learners must discover classes, enrol, pay, access lessons, receive support and obtain evidence of completion. Staff use a digital learning product supported by internal teams and external suppliers. During busy periods, enrolment succeeds but access is delayed. This case is a teaching invention, not a report about Helmi’s systems.

## Module 1 — Understand value before managing activity

### 1.1 Product, service and the customer's work

A digital product combines resources and capabilities into something that can support a user need. A service helps someone achieve a useful outcome through an ongoing relationship. Product and service are closely connected, but they are not interchangeable: software can be delivered while the promised service remains unreliable.

At Harbour Learning, the enrolment application is part of the product. A learner being able to join the right class at the promised time is a service outcome. A deployment, account record or payment confirmation is an output. These outputs matter only when they contribute to the outcome.

**Distinction to practise:** “We created 500 accounts” measures output. “Eligible learners could begin their purchased classes on time” measures an outcome. The second statement still requires a definition of eligible, on time and usable access.

### 1.2 Value is contextual and co-created

Different stakeholders judge value differently. A learner values understandable lessons and convenient access. A sponsor values relevant capability. A support colleague values clear ownership and reliable information. A regulator may value appropriate records and safeguards. A provider cannot simply announce that value has been delivered because a feature exists.

Co-creation requires contributions from both sides. The provider makes access available, explains the service and supports difficulties. The learner supplies accurate information, chooses an appropriate course and engages in learning. This does not excuse poor service: it identifies the dependencies needed to make the relationship work.

Distinguish the person who uses the service, the person who defines or represents requirements, and the person who authorizes expenditure. They can be the same person, but need not be. Interviewing only the buyer can miss a user's accessibility or support needs.

### 1.3 Function, assurance, cost and risk

A useful learning service must perform the required function and do so under acceptable conditions. Correct course access is of little value if it is unavailable during the learner’s study window. Conversely, a highly available service that delivers the wrong course is not adequate.

Evaluate cost and risk from both provider and consumer perspectives. A service can remove the need for a customer to operate infrastructure while introducing dependencies on connectivity, identity and a supplier. “Managed” does not mean “risk-free.” Make transferred responsibilities, retained responsibilities and assumptions explicit.


## Module 2 — Assess the four dimensions together

### 2.1 Organizations and people

Services depend on responsibilities, skills, culture, communication and decision authority. An organizational chart does not show every operational dependency. Ask who may decide, who performs the work, who needs information and who owns the customer outcome when several teams contribute.

Harbour Learning’s support team can see that payment succeeded but cannot determine why access failed. Training support staff without granting appropriate information access may leave the bottleneck unchanged. Assign end-to-end ownership while retaining specialist responsibilities.

### 2.2 Information and technology

Examine the information needed to make decisions, its quality, its protection and its movement between systems. Technology includes more than the visible application: identity, integration, monitoring, data stores and operational tooling all influence service performance.

For delayed access, compare the meanings of “paid,” “enrolled” and “entitled” across systems. If teams use these words differently, automating the transfer may accelerate a misunderstanding. Define authoritative records, reconciliation rules and exception handling before treating integration speed as the whole problem.

### 2.3 Partners and suppliers

A supplier may provide payment processing, content, hosting or specialist support. Contracts do not eliminate the need to coordinate. Understand responsibilities, dependency concentration, escalation, continuity and how supplier performance affects customer outcomes.

A payment provider’s availability target does not prove that the full enrolment journey meets its target. Measure the service across organizational boundaries and identify which evidence each party can provide.

### 2.4 Value streams and processes

A process organizes activities toward a defined purpose. A value-stream view follows how demand becomes an outcome across activities, teams and systems. Local procedure compliance can coexist with long customer waits when hand-offs and queues are ignored.

Consider all four dimensions together. A proposed chatbot might require support skills and ownership, reliable knowledge content, supplier assurance, and a revised escalation flow. Evaluating only the software misses most of the operating design.


## Module 3 — Work across the digital product and service lifecycle

The lifecycle activities considered here are discover, design, acquire, build, transition, operate, deliver and support. Treat them as interconnected activities, not a mandatory waterfall or departments that never overlap. Feedback from operation and support should influence discovery and design.

### 3.1 Discover

Investigate needs, opportunities, constraints and the environment before deciding what to build. Distinguish a stakeholder's requested feature from the underlying problem.

For Harbour Learning, “add a resend button” is a solution suggestion. The underlying need may be reliable access after payment. Discovery examines who is affected, frequency, consequences, existing workarounds and evidence quality.

**Output for the learner:** a problem statement with affected stakeholders, desired outcome, boundaries and assumptions to test. Do not invent market demand or convert a single complaint into a prevalence claim.

### 3.2 Design

Translate the validated need into a service experience and operating design. Include user journeys, accessibility, support, security, information, supplier dependencies and success criteria, not just screens.

Design the normal path and the exception path. What happens when payment succeeds but access cannot be granted? Who communicates, which state is authoritative, and what stops duplicate or incorrect actions? Decide what is observable and how service recovery will work before release.

### 3.3 Acquire

Decide which capabilities to obtain and how. Compare building, buying, partnering or reusing against outcomes, total lifecycle cost, constraints and risks. A low purchase price can hide integration, support, exit and training costs.

For each option, record assumptions about information portability, operational ownership and supplier dependence. Acquisition is not merely procurement paperwork; it affects the service architecture and future choices.

### 3.4 Build

Create and integrate the product and service capabilities. Use small, testable increments with acceptance criteria connected to the intended outcome. Include supporting documentation, monitoring and operational knowledge.

A feature is not ready simply because its happy-path demonstration works. Test relevant failure modes, permissions, data quality, accessibility and integration boundaries. A test proves only what its conditions and assertions actually cover.

### 3.5 Transition

Prepare a changed product or service for use. Address readiness, communication, knowledge, support capability, data movement, deployment arrangements and recovery planning. Tailor the effort to risk and context rather than imposing identical ceremony on every change.

For Harbour Learning, rehearsal should establish that staff can recognize entitlement failures and know what action is permitted. A rollback document is not proof that rollback is viable; availability of a target and the consequences of reverting require evidence.

### 3.6 Operate

Sustain the capabilities needed for ongoing service. Monitor relevant conditions, maintain reliability, manage operational work and respond proportionately to exceptions. Avoid equating green infrastructure dashboards with successful customer outcomes.

A running server can coexist with learners unable to enter a course. Operational measures should connect technical signals to meaningful service indicators and provide enough context for action.

### 3.7 Deliver

Ensure stakeholders actually receive the agreed service. Consider the complete interaction, commitments, requests and experience. Delivery is not merely the moment code is deployed.

In the case, successful delivery includes the right learner receiving usable access to the right course within the agreed conditions. The evidence should reflect the complete journey rather than the status of one component.

### 3.8 Support

Help users, address disruptions and requests, and feed learning back into the lifecycle. Rapid restoration and deeper investigation serve different purposes. A workaround may restore service without removing the underlying cause.

Support knowledge should be understandable, maintained and linked to escalation. Repeated issues are useful signals for discovery and improvement, but not every disruption warrants a large investigation.


## Module 4 — Connect the value system, governance and improvement

### 4.1 A system, not a collection of isolated practices

A value-system perspective asks how direction, decisions, management capabilities and continual learning work together to turn needs into value. Optimizing one team can worsen the whole service if work is shifted elsewhere.

For example, reducing support handling time by immediately routing every ticket to engineering may improve one metric while increasing total resolution time. Inspect the full outcome and the incentives behind local measures.

### 4.2 Governance and management

Governance determines and oversees direction within stakeholder expectations and organizational constraints. Management plans and carries out work within that direction. Clear separation of accountability does not mean isolation: management evidence informs governance decisions.

A service owner may present options for reducing recurring access failures. Decision-makers must understand costs, risk, benefits and constraints before choosing. Record what was authorized, by whom and for what scope. General enthusiasm is not evidence that a particular action was approved.

### 4.3 Guiding thinking in practical decisions

Use value-focused questions, examine the current situation before replacing it, work incrementally with feedback, collaborate across boundaries, keep the whole system visible, simplify where justified, and automate only after understanding the work. These are explanatory teaching applications, not quotations from official guidance.

A simplification is useful when it removes unnecessary effort without removing needed control. Automation is useful when the decision and exception handling are sufficiently understood. Automating an ambiguous approval or unreliable data source can amplify errors.

### 4.4 Continual improvement as a disciplined loop

State the desired future, establish the current condition, choose a measurable improvement, act, evaluate and retain learning. The practical discipline is to distinguish baseline, target, intervention and result.

Harbour Learning might aim to reduce delayed access. First define delayed, collect a baseline and separate causes. Then choose a small intervention, such as clearer exception ownership, and examine outcomes alongside unintended effects. Improvement work must not be declared successful merely because the proposed change was implemented.

### 4.5 From firefighting to sustainable improvement

Necessary incident response protects current service. Planned improvement aims to strengthen future capability. The problem is repeated displacement of preventive work without an explicit decision or return plan.

Use transparent prioritization, response coverage, named improvement ownership and review of recurring demand. Protected capacity is not an absolute ban on interruptions. A major incident may justify reassignment; record the reason and what happens to displaced work.


## Module 5 — Investigate value streams

### 5.1 Follow demand to outcome

Start with a defined trigger and finish at a stakeholder outcome. Identify activities, decisions, queues, hand-offs, information and exceptions. Do not start by drawing departments and assume that is the customer journey.

For Harbour Learning: a learner seeks a class, chooses an offering, enrols, pays, receives entitlement, starts learning and obtains support when needed. Several paths and loops may exist.

### 5.2 Measure elapsed time and actual work separately

Elapsed time includes waiting. Work time measures effort or active handling. A five-minute task can sit in a queue for two days. Increasing task speed may have negligible effect if waiting dominates.

Define measurement boundaries. Include failed, repeated and abandoned paths when relevant; a report of successful journeys alone can hide the service's largest problems. Use medians and variation where appropriate rather than relying only on averages.

### 5.3 Find constraints and improve the whole

A bottleneck may be an approval, missing information, limited skill coverage or supplier dependency. Treat it as a hypothesis until evidence supports it. Ask why work waits and whether the control achieves a necessary purpose.

Do not simply remove every approval or hand-off. Redesign proportionately: improve information, clarify authority, route low-risk work appropriately or remove duplicated checks. Reassess downstream consequences.


## Module 6 — Use AI with explicit boundaries

### 6.1 Begin with a useful task

Possible applications include knowledge retrieval, summarization, classification, anomaly detection and assisted drafting. These are candidate uses, not guarantees of accuracy or automatic permission to deploy.

For Harbour Learning, an assistant might draft a support reply from approved knowledge. Its task should be bounded: explain access steps, identify missing information and escalate uncertainty. Changing account permissions or issuing refunds is a different capability with different risk and authorization needs.

### 6.2 Information quality and evaluation

AI output depends on available information and can be incomplete or wrong. Distinguish a generated answer from verified evidence. Validate against representative examples, including ambiguous and adversarial inputs, not only easy demonstrations.

Measure correctness, usefulness, escalation behavior and harmful failure modes. Examine whether performance differs across user groups or language needs. Retain a human route for cases the system cannot handle reliably.

### 6.3 Accountability, security and human control

Name who owns the AI service and who may authorize consequential actions. Minimize data access, protect sensitive information, establish logging and retention rules, and define what must not enter the system.

A human review step is meaningful only if the reviewer has time, context, authority and a clear decision to make. “Human in the loop” is not a complete control design.

### 6.4 Operate and improve the AI capability

Monitor changes in inputs, knowledge and performance. Define how incorrect advice is reported, corrected and prevented from recurring. Plan for supplier outages and the ability to disable a harmful capability without stopping essential support.


## Module 7 — Combine approaches without confusing their roles

### 7.1 DevOps and service management

DevOps emphasizes collaboration and feedback across development and operations, often supported by automation and iterative delivery. Service management keeps the focus on stakeholder value, service relationships and ongoing outcomes. They can reinforce each other rather than compete.

Fast deployment is not the sole objective. Consider change failure, recovery capability, user impact and operational learning. A pipeline can provide evidence, but automated success does not override unresolved service risks.

### 7.2 PRINCE2 and ongoing product/service work

Project management provides a structured way to govern temporary work toward agreed objectives. Ongoing product and service management continues beyond a project's closure. The handover must include operating capability and ownership, not just a delivery checklist.

A project may implement a new enrolment capability. Its business case and stage decisions do not eliminate the need for ongoing support, improvement and review of realized benefits.

### 7.3 An integrated operating agreement

Clarify how project decisions, product priorities, delivery workflows, service commitments and operational feedback connect. Use proportionate controls and avoid making teams produce duplicate evidence for identical decisions.


## Visual library and official-resource boundary

The requested style is **illustrated teaching, not boxes and sticks**. Planned original visual treatments: a detailed service scene showing stakeholder interactions; an editorial four-dimension panorama; a lifecycle landscape; an illustrated support incident; and a customer-journey storyboard. These should be labeled original explanatory illustrations, not official ITIL diagrams.

**Official stencil pack:** not verified. No official marks, licensed diagrams or accreditation badges are reproduced in this draft. Public availability does not by itself establish reuse rights. Link to official material where reuse permission has not been confirmed.

## Sources, coverage and next editorial checks

- [PeopleCert ITIL Version 5 Foundation](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/itil-1/itil-5-foundation-version-50-4154/)
- [PeopleCert ITIL FAQ](https://www.peoplecert.org/help-and-support/faq-itil)
- [PeopleCert-authored Foundation syllabus v5.0, February 2026, provider-hosted PDF](https://fasttracklearningsolutions.com/wp-content/uploads/2026/02/ITIL_Version5_Foundation_Syllabus_v5.0.pdf)

This is **Foundation learning draft v0.2**, with substantive original lessons across the seven syllabus areas. It is not yet a criterion-by-criterion validated complete course. Remaining editorial work: map all 95 assessment criteria to exact lessons, confirm any missing terminology and official model detail, verify current revision, add the illustrated visual library, and review lessons against the coverage map. Other Version 5 qualifications require their own verified syllabus and separate lessons.

Related research, kept separate: [Breaking the Firefighting Cycle — Research Paper Draft](https://app.notion.com/p/419b3e6738cc8152968ce1b3f864b54f).



## Expanded teaching notes — relationships, context and operational language

### General concepts and their digital forms

A product is an organized combination of resources and capabilities offered to meet needs. It can be physical, digital or a combination. A service concerns enabling a consumer’s desired outcomes through an ongoing arrangement rather than merely handing over a thing. These are original plain-language explanations, not the official glossary wording.

A digital product relies materially on digital technology and information for its capabilities. A digital service uses those capabilities to enable outcomes through service interactions. Harbour Learning’s physical course kit illustrates a non-digital product component; its learning application illustrates a digital product; facilitated learning is the broader service; providing online participation and support illustrates digital service delivery. One offering can combine all of them. Neither a website nor a subscription label alone explains the whole service relationship.

Digital product and service management is the coordinated work of directing, developing, delivering, operating and improving these capabilities and relationships so that they support stakeholder value. It includes decisions about people, information, suppliers and ways of working, not just software administration. The same organization may develop a product, consume another provider’s service and provide its own service. Exact Version 5 glossary wording remains unverified in this draft.


**Editorial status:** These are independently written explanations and fictional applications, not verbatim official definitions. The syllabus identifies required topics; it does not supply every definition, model or practice-guide detail. Exact official glossary recall must be checked against the licensed Version 5 book. This expansion improves teaching depth without declaring the course fully validated.

### Service offerings and the work behind a relationship

A service offering is the package a provider presents to a particular consumer need. Distinguish the promise from the underlying product. Harbour Learning may use the same learning platform for an individual self-study offering and an employer-sponsored cohort offering. The product can be shared, while support arrangements, reporting, conditions and experience differ.

An offering can include things supplied to the consumer, permission to use resources, and work performed for the consumer. At Harbour Learning, a physical course kit illustrates goods, access to an online course illustrates resource access, and an instructor-led feedback session illustrates an action performed as part of the service. Do not infer ownership transfer from access: a subscription can permit use while the provider retains ownership. Digital licensing can be more complicated than possession of a file.

A provider organizes capabilities to make a service available. A consumer contributes to using it and realizing outcomes. A product vendor supplies a product capability that another organization may incorporate into its service. Harbour Learning may buy an authoring product, consume a payment service and provide training services at the same time. These are relationship roles rather than permanent labels for an entire company. Outsourcing one component does not outsource accountability for every customer outcome.

An organization is a coordinated arrangement of people and responsibilities pursuing objectives. Relevant boundaries need not match a legal company boundary: a team can provide a service to another team. The person paying for the course, the person agreeing requirements and the learner using it may differ. Naming these roles prevents a common error: assuming that payment approval establishes what all users need.

### Choosing how closely to work together

Some relationships are primarily standardized exchanges. Others require continuing coordination, shared information and adaptation. A partnership involves deeper joint working toward outcomes. A closer relationship is not automatically better: it costs attention, needs trust and can create dependence.

Consider three original illustrations:

- **Basic relationship illustration:** An individual buys access to a clearly described self-study course. Most interaction is standardized.
- **Cooperative relationship illustration:** An employer and Harbour Learning coordinate enrolment lists, accessibility needs and reporting over several cohorts.
- **Collaborative (partnership) relationship illustration:** An employer and provider jointly develop a learning programme, share feedback and revise the service together.

These illustrate increasing joint working. They are not a substitute for the exact official distinctions between the syllabus’s relationship categories. The appropriate choice depends on uncertainty, interdependence, strategic importance and the effort both parties can sustain. Calling a supplier a partner without changing decisions, information sharing or responsibilities does not create partnership.

### Experience, assurance and sustainability

Utility concerns whether the capability helps do the needed work. Warranty concerns the conditions under which it can be relied upon. User experience concerns how people perceive and respond to using the service. Sustainability asks whether choices can remain responsible and viable over time rather than shifting unacceptable burdens elsewhere.

For Harbour Learning, an accurate course is insufficient if captions are unreadable, a support process is hostile or access repeatedly fails at the promised time. Conversely, an attractive interface cannot compensate for teaching the wrong material. These dimensions of quality should inform trade-offs together.

A sustainability discussion might consider unnecessary resource consumption, maintainability, inclusive access and supplier dependence. Do not call a service sustainable merely because it has no printed handouts. Boundaries and evidence matter: moving work to a supplier can move an impact without eliminating it.

Service quality is broader than one target. A service level makes an aspect of performance explicit. A service level agreement records commitments and the conditions needed to interpret them. A meaningful agreement states scope, measurement boundaries, responsibilities and exceptions. “Fast support” leaves much unresolved; a defined response commitment can be measured, but response speed alone does not establish useful resolution.

A service journey is the consumer’s experience across interactions and time, not just the provider’s internal fulfilment procedure. Awareness, selection, starting use, ongoing use, support and ending use may all influence the relationship. A technically correct entitlement process can still leave the learner confused by conflicting messages.

## Expanded teaching notes — external context and the four dimensions

The four dimensions do not operate in a vacuum. Use a PESTLE scan to identify external influences, then connect each influence to concrete decisions. The scan is not a prediction engine or a substitute for specialist advice.

| Context lens | Fictional Harbour Learning example | Decision implication |
| --- | --- | --- |
| Political | A public funding policy changes eligibility for a training programme | Revisit offering assumptions and information requirements |
| Economic | Employer training budgets contract | Reassess demand, affordability and delivery costs |
| Social | More learners study alongside care responsibilities | Revisit accessibility, scheduling and support channels |
| Technological | A key identity platform changes an interface | Plan compatibility work and supplier coordination |
| Legal | Applicable privacy or accessibility obligations change | Obtain qualified interpretation and adapt controls |
| Environmental | Resource constraints or disruption affect delivery locations | Review continuity and resource choices |

The examples are hypothetical, not statements that these events have occurred or legal guidance about obligations.

Internal influences also matter: available skills, culture, organizational strategy, technology debt, budget, existing commitments and decision rights. A tool suitable for one organization may be inappropriate in another with different staffing or responsibilities.

Trace one influence through several dimensions. If Harbour Learning supports a new learner population, it may need different communication skills, more accessible information and technology, supplier changes and a revised onboarding stream. A four-dimension analysis that produces four unrelated lists misses the relationships between them.

## Expanded teaching notes — lifecycle purposes and feedback

The lifecycle is a way to keep connected decisions visible over time. The activities are not necessarily sequential and do not need eight separate organizational owners. A discovery effort can continue during operation; a support issue can expose a design assumption; a supplier change can trigger acquisition and transition work.

The following are original decision-oriented explanations, not quoted official purpose statements:

| Activity | Main question in the Harbour Learning case | Useful evidence |
| --- | --- | --- |
| Discover | Which learner or business need is worth addressing, and what do we still not understand? | Observations, affected groups, impact and tested assumptions |
| Design | How should the experience and operating arrangements meet that need? | Service journey, requirements, exception handling and acceptance criteria |
| Acquire | Which required capabilities should we obtain, from whom and on what conditions? | Options, lifecycle costs, responsibilities and exit implications |
| Build | Can we produce and integrate the intended capability? | Working increments, review records and tests within defined conditions |
| Transition | Can the change enter use with appropriate readiness and coordination? | Readiness evidence, communications, support knowledge and recovery arrangements |
| Operate | Can the underlying capabilities remain dependable in ongoing use? | Health signals, operational records and maintenance evidence |
| Deliver | Are consumers receiving the agreed service? | End-to-end fulfilment and outcome-related service evidence |
| Support | Can people obtain help and disruptions or requests be handled appropriately? | Restored use, useful guidance, escalation and learning |

A lifecycle activity is not the same as a value stream. A value stream connects activities for a particular demand and outcome; it may revisit activities or run some concurrently. A value chain is an organizing view of activities that can contribute to value. An operating model makes the organization's approach tangible through responsibilities, decision rights, ways of working, information and supporting capabilities.

For example, the lifecycle reminds Harbour Learning that support readiness matters. Its enrolment-to-access value stream shows exactly where exceptions wait. Its operating model establishes who owns those exceptions and what authority they have. All three perspectives are useful because they answer different questions.

**Metrics boundary:** Suggested case measures in these lessons are original teaching examples. The official activity-specific success measures referenced in the Version 5 book have not been verified here. Do not describe this course’s examples as that official metric set.

## Expanded teaching notes — operational concepts without conflation

### Specifications, prototypes, tests and release

A product specification expresses what is intended, including requirements and constraints. A prototype is a representation used to explore or evaluate an idea. A polished prototype can still omit reliability, integrations and operational work needed in a functioning service.

Testing compares observed behavior with defined expectations under stated conditions. A test result is evidence with a scope, not a guarantee about every condition. A release makes a new or changed capability available for use; installation or deployment and release to users need not happen simultaneously. This distinction enables controlled introduction but also creates additional states to manage.

Continuous integration combines changes frequently with automated checks. Continuous delivery aims to keep changes ready for release with a reliable process. Continuous deployment automates promotion into production when conditions pass. These explanations describe common industry usage; tool settings alone do not establish effective practice. An organization can automate deployments while retaining manual decisions about feature exposure or business availability.

Supporting industry reading for CI/CD: [Microsoft continuous integration](https://learn.microsoft.com/en-us/devops/develop/what-is-continuous-integration) and [continuous delivery](https://learn.microsoft.com/en-us/devops/deliver/what-is-continuous-delivery). These support the general engineering explanation, not official ITIL glossary wording.

### Events, incidents and requests

An event is an observable occurrence or state change relevant to managing a service. Some events are normal; some warn of a possible problem; some indicate a disruption. An incident concerns disrupted or degraded service. An event is therefore not automatically an incident.

A service request concerns an agreed form of assistance, information or access rather than necessarily indicating failure. “Please enrol a new employee” and “an enrolled employee cannot access the purchased course” may require different handling even if both arrive at the same desk.

Do not force classification based solely on the communication channel. The purpose and circumstances of the work determine how it should be handled.

### Problems, errors and known errors

Separate the disrupted service from investigation into its causes. A problem concerns a cause or potential cause that warrants investigation. An error is an incorrect condition relevant to the failure. A known error reflects investigated understanding that remains relevant while the problem has not been fully resolved. Exact Version 5 glossary wording remains to be checked.

In the fictional case, inability to access a class is the learner’s disruption. Repeated failures associated with entitlement creation motivate investigation. A faulty translation of enrolment states may be the identified incorrect condition. Documented understanding and a safe workaround can support restoration before a permanent correction is completed.

Do not label an incident a known error merely because it has happened before. Recurrence is a signal; established understanding is a different claim. Likewise, a workaround can restore access without proving that the underlying cause has been removed.

A disaster involves disruption with consequences requiring an appropriately significant coordinated response. It is not simply a synonym for an inconvenient incident. An organization must define relevant thresholds and continuity arrangements rather than waiting for a tool label to determine severity.

### Reliability, observability and SRE

Reliability concerns dependable behavior over relevant conditions and time. Observability concerns the ability to understand internal behavior from available signals. Site Reliability Engineering applies engineering approaches to operating dependable systems. None of these is achieved by buying a monitoring product alone.

A health dashboard can show that a process is running while learners remain unable to obtain access. Combine signals into a service interpretation: what was attempted, what state resulted, who was affected and what evidence is missing? Avoid collecting unnecessary personal information merely because more logs are technically possible.

Supporting primary-source reading: [Google’s introduction to SRE](https://sre.google/sre-book/introduction/). The teaching case is original and does not claim to reproduce Google’s operating model or ITIL definitions.

### Metrics and critical success factors

A metric is a defined measurement. A critical success factor expresses something that must go well for the intended objective to be achieved. They are not interchangeable. “Learners can begin the correct course on time” can be a success requirement; the proportion of eligible learners gaining correct access within an agreed window is one possible measure.

A metric requires population, method, period and interpretation. A rising success percentage may result from excluding difficult cases. Include balancing evidence, such as abandoned enrolments, corrections and support burden, before declaring improvement.

## Expanded teaching notes — practices, governance and capability

A management practice combines capabilities needed to perform a type of work. It is not merely a written process, a team or a software module. People, knowledge, responsibilities, information and technology can all contribute. One practice can support several lifecycle activities and value streams; one activity can draw on several practices.

The Version 5 Foundation syllabus identifies **general** and **product and service management** practice groupings. These are the Foundation grouping labels relevant to this draft. Do not confuse them with certification bundles or import a grouping scheme from another edition.

For Harbour Learning, handling a disruption may draw on incident-related capability, knowledge, monitoring, communication and supplier coordination. Improving the recurring issue also needs decision authority and change capability. Creating a ticket category called “problem” does not prove that systematic investigation is taking place.

Practice guides can help an organization understand what capability it needs, coordinate responsibilities and avoid implementing a practice as an isolated checklist. However, **the exact Version 5 practice-guide structure has not been verified from a current official source**. This draft does not invent its section headings or claim full practice-guide coverage.

**Governance coverage remains partial:** The named official Version 5 governance activities and their precise explanation have not yet been verified against a current official source. The following is an original general explanation, not an asserted complete rendering of that criterion.

Governance enables work by establishing direction, decision authority and oversight. Effective governance is not equivalent to making every decision slower. Clear boundaries can allow routine work to proceed while reserving consequential decisions for accountable roles. Review evidence against objectives and revise the arrangements when they fail to produce the intended results.

A value system connects principles, governance, work activities, practices and learning. Treating each as a separate implementation project can lead to duplication and contradictory decisions. For example, governance may encourage faster customer access while a local approval procedure imposes unexamined delays. The conflict needs an explicit decision, not merely more reporting.

## Expanded teaching notes — mapping and managing streams

A core stream directly supports the organization's central value proposition. An enabling stream provides capabilities needed by other streams. In Harbour Learning, moving from enrolment to useful participation is central to the learning service; onboarding a support colleague or making a supplier available may enable it. The distinction depends on the organization and viewpoint, not on whether work is technically sophisticated.

Mapping creates a representation of how work actually flows. Management is the continuing activity of making that flow effective: assigning ownership, interpreting evidence, prioritizing improvements, coordinating changes and checking results. A map is therefore an input to management, not a substitute for it.

A practical map should make its boundaries explicit and show enough to answer the investigation question. Useful elements in an original teaching representation include demand, intended outcome, activities, participants, hand-offs, decisions, queues, elapsed time, active time, information, exceptions and evidence sources. This is not asserted to reproduce the official Version 5 map-element list.

Use observation to distinguish current practice from intended procedure. Staff may perform essential work outside the formal system, or the documented path may describe only successful cases. Validate the representation with those doing the work and those experiencing the outcome.

### Complexity and adaptation

In a simple, predictable task, a standard procedure can be highly effective. Where dependencies, people and changing conditions interact, outcomes may be less predictable. Complexity thinking draws attention to interactions and feedback, not just individual components.

At Harbour Learning, a policy change might alter learner behavior, support demand and supplier workload at the same time. Increasing one team's throughput could overload the next. Use bounded changes, observe effects and adapt rather than assuming that an earlier map will remain accurate indefinitely.

Optimization must fit the situation. Highly repeatable requests may benefit from standardization and automation. Uncertain cases may need better information, expert judgment and escalation. “Optimize” does not mean remove every variation or automate every decision.

## Expanded teaching notes — AI concepts and evidence boundaries

Artificial intelligence refers broadly to computational capabilities used for tasks associated with intelligent behavior. Generative AI produces content such as text or images from inputs. Agentic AI combines model-supported decisions with tool use or multi-step activity toward a goal. These categories overlap, and product marketing does not determine the actual authority or reliability of a system.

AI maturity is not simply how much AI an organization purchases. Relevant evidence includes consistent use, information readiness, skills, evaluation, governance, operational support and learning. A demonstration that works once does not establish sustained organizational capability.

AI governance establishes decision rights, responsibilities and oversight for AI-related choices and consequences. At Harbour Learning, this includes who approves a use case, what data may be used, who evaluates behavior and who can stop a harmful capability.

AI can support different lifecycle activities in different ways: organize discovery notes, propose design alternatives, summarize supplier information, assist development, draft transition guidance, identify operational patterns, assist fulfilment and retrieve support knowledge. These are original candidate applications, not claims of guaranteed benefits or an official prescribed deployment map. Each needs evidence, suitable data handling and proportionate authority.

For independently sourced risk-management context, see [NIST’s AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) and [its Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). NIST provides a separate voluntary approach; it is not the ITIL AI Capability Model and must not be relabeled as one.

**Unverified official model:** The exact ITIL AI Capability Model is not defined in the public syllabus. Its structure, labels, relationships and official explanation are **not verified in this draft from a current official Version 5 source**. Do not replace that model with an invented maturity ladder or relabel a third-party model as ITIL.

**Unverified official improvement model:** The exact Version 5 ITIL Continual Improvement Model steps and detailed official explanation are **not verified in this draft from a current official Version 5 source**. The general improvement discussion in Module 4 is original explanatory teaching, not a reproduced or verified official model. Do not silently substitute a previous-edition diagram.

## Version 0.2 editorial change note

This expansion strengthens terminology, relationships, external context, lifecycle distinctions, practices and streams with original explanations. Official glossary wording, the unverified official models, practice-guide structure, official activity metrics and criterion-level completeness remain verification gaps. All case measurements and examples are fictional. No practice examinations, video content or hands-on labs are added.



## Source-verification register — 15 November 2026 (SGT)

| Source | What it supports here | What it does not establish |
| --- | --- | --- |
| [PeopleCert Foundation overview](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/itil-1/itil-5-foundation-version-50-4154/) | Foundation course exists; public overview of its subject areas | Complete official glossary, official model diagrams or accredited status of this course |
| [PeopleCert FAQ](https://www.peoplecert.org/help-and-support/faq-itil) | Public context for the Version 5 qualification family | That Foundation covers every specialist qualification |
| [PeopleCert-authored syllabus v5.0, February 2026](https://fasttracklearningsolutions.com/wp-content/uploads/2026/02/ITIL_Version5_Foundation_Syllabus_v5.0.pdf) | Revision pin and assessment-topic inventory; checked as a provider-hosted PeopleCert-authored document | Full teaching definitions, book tables, model content or reproduction rights |
| [Microsoft CI](https://learn.microsoft.com/en-us/devops/develop/what-is-continuous-integration) and [CD](https://learn.microsoft.com/en-us/devops/deliver/what-is-continuous-delivery) | Supporting general engineering concepts | ITIL-specific official wording |
| [Google SRE introduction](https://sre.google/sre-book/introduction/) | Supporting reliability-engineering context | A universal organization design or official ITIL model |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | Supporting AI risk-management context | A substitute for the ITIL AI Capability Model |

Source status is evidence of this editorial check, not a promise that sources cannot change. Original Harbour Learning cases, suggested indicators and explanations are author-created instructional synthesis. No source confirms that these invented examples occurred.


### Editorial audit response

This version now labels basic, cooperative and collaborative (partnership) examples explicitly and distinguishes general concepts from digital forms. These changes improve explanatory coverage but do not establish exact official-definition fidelity. The remaining official model and governance gaps are verification gaps, not claims that the material is necessarily paywalled or unavailable publicly.
