# Networking: draw traffic intent and trust boundaries

**Learning purpose:** Select internet and hybrid connectivity, private access, performance controls and routing based on actual traffic.

## Start with the traffic matrix
For every flow, identify source, destination, protocol, direction, identity, expected volume and acceptable latency. Distinguish inbound user traffic from outbound dependency access and administrative access. This prevents a broad “open the network” change from hiding several unrelated needs.

Virtual networks provide isolation and connectivity foundations. Peering, gateways and routing choices must be evaluated as part of a topology rather than assuming that any connected network can automatically transit every other network. DNS resolution is part of private connectivity; a private address that clients cannot resolve or route to is not a functioning design. [S35: Virtual networks](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)

## Hybrid paths and performance
VPN and ExpressRoute offer different connectivity models. Select using resilience, bandwidth, latency, operational requirements and cost. A private connectivity service does not eliminate the need to consider encryption and application security. Redundant paths must also be diverse enough to address the intended failure scenario. [S36: ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

Performance is end to end. A fast circuit cannot compensate for a distant synchronous dependency or an application that repeatedly transfers unnecessary data. Place latency-sensitive components intentionally and measure the complete user journey. Avoid quoting a latency target as guaranteed merely because two services share a region.

## Load balancing and protection
Azure Front Door supports global HTTP application delivery; Application Gateway provides regional application-layer routing; Load Balancer addresses layer-4 traffic; Traffic Manager uses DNS-based routing. The decision depends on protocol, geographic scope, TLS handling, health detection and application requirements. DNS routing does not proxy each request. [S37: Load balancing options](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview)

Separate network filtering, web application protection and identity-based access. Network security groups, firewalls and web application firewalls operate at different layers and scopes. Private endpoints can provide private service access but require service-specific configuration and DNS planning. They do not by themselves prove that public access is disabled. [S38: Private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

## Worked example: private data, public application
Contoso wants public users to reach a booking frontend while keeping its database off the public access path. The architecture shows the public edge, application tier and private data path as different zones of trust. It includes the DNS and outbound service dependencies necessary for operation, rather than depicting a completely sealed application that cannot authenticate or report telemetry.

A traffic specification should identify allowed paths and intended denials. Meaningful geography and service symbols help explain the architecture, but explicit source, destination, protocol, port and identity requirements provide precision that an illustration alone cannot convey.

## Distinguish the security layers
Azure Firewall provides managed stateful network filtering and related capabilities whose availability depends on SKU. Network security groups scope traffic rules at their supported network attachment points. A route must actually send relevant traffic through an inspection point; placing a firewall in a diagram does not establish coverage. [S58: Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/overview)

A web application firewall targets web-layer attacks, such as selected malicious HTTP patterns. It does not replace secure application code, identity authorization or general network controls. Detection and prevention modes have different effects; tuning must account for legitimate application requests and false positives. [S59: Web Application Firewall](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview)

DDoS protection addresses availability threats from hostile traffic floods at its supported layers and resources. It is distinct from WAF protections for application requests. The selected protection plan must match the actual public exposure, supported service and response requirements. [S60: DDoS Protection](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview)

**Worked decision:** Contoso exposes an HTTPS booking application and also has administrative endpoints. A WAF on the public web path does not protect an unrelated management interface. The design first removes unnecessary public administration exposure, then assigns controls to the remaining flows. Controls are evaluated by path and threat rather than counted as security products.

## Hybrid routing and name resolution
A site-to-site VPN can provide encrypted tunnel connectivity over the internet. ExpressRoute provides private connectivity through a connectivity provider, with its own design and resilience considerations. Neither makes routing, DNS or identity configuration automatic. Consider how the service behaves when one path fails and whether the alternative path has enough capacity for the intended degraded mode.

Private endpoint design includes the private address, reachable network path and appropriate DNS resolution. A client resolving the public address can still take an unintended route if public access remains available. The architecture therefore names the resolution behavior expected from Azure, on-premises and remote clients separately.

## Worked routing decision
Contoso’s users are global, but its application has a regional private backend. Global application delivery and regional private connectivity are separate concerns. The architect may combine a global edge service with an appropriate origin path, but must verify the selected service and tier support that path. An attractive picture cannot substitute for the documented feature compatibility.

The diagram’s caption should state what the picture abstracts: certificates, identity exchanges, DNS and outbound telemetry may be omitted visually, but they remain part of the written traffic design.

## Outbound connectivity is explicit architecture
A NAT gateway provides an explicit outbound connectivity mechanism; it is not a web-application firewall or application authorization engine. If traffic must be inspected, routes and firewall design must establish that path. Microsoft’s current guidance changes defaults for new virtual networks under newer APIs, while existing networks can differ. Do not rely on remembered implicit outbound behavior. [S78: Explicit outbound access](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access)

**Worked decision:** Contoso’s private worker needs a third-party API and Azure dependencies. The design lists required destinations and a supported explicit outbound path, with the chosen inspection policy where required. Removing the worker’s public inbound exposure does not remove its outbound needs. DNS and egress behavior are validated as distinct concerns in a real deployment.

A route’s existence is not proof of adequate performance. For an illustrative transfer of 100 GB at a sustained 100 megabits per second, the ideal transfer time is roughly 8,000 seconds, or 2.22 hours, before overhead. This assumes decimal units and sustained throughput; real links and applications can be slower. The arithmetic exposes why nominal link speed alone cannot settle a migration window.
