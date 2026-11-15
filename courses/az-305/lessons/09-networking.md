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

The accompanying traffic table identifies allowed paths and intended denials. The illustration should use meaningful geography, application silhouettes and service symbols, but the table provides precision that an attractive picture alone cannot convey.
