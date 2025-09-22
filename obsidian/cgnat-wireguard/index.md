---
title: How to overcome CG-NAT for free with Oracle Cloud and NixOS
---
### Table of contents
- [[index|Introduction]]
- [[cloud-setup|Part 1. Cloud Setup]]

In today’s day and age, there aren’t many ISPs that still provide public IPs for its users. This can be a challenge to fellow homelab enthusiasts that seek to host services in their own hardware.

Luckily, this limitation can be surpassed free-of-charge by utilizing a combination of a WireGuard tunnel, Oracle Cloud’s Always-Free services, and the incredibly powerful NixOS.

```mermaid
---
config:
  layout: elk
---
flowchart TD
 subgraph s1["<span>OCI Instance</span><br><span>10.0.0.4/24 (Internal)</span><br><span>161.153.3.153 (Public IP)</span>"]
        n1["WireGuard peer (port 51820)"]
  end
 subgraph s2["<span style=color:>Router</span><span style=color:><br>100.64.0.1/24 (CG-NAT)</span>"]
        n2["WireGuard peer (any port)"]
  end
    s2 -- UDP 51820 --> s1
    n3["Summary"] -- "10.0.30.0/24" --> s2
    n4["Nextcloud"] -- "10.0.30.10/24" --> n3
    n5["Jellyfin"] -- "10.0.30.11/24" --> n3
    n6["Syncthing"] -- "10.0.30.12/24" --> n3
    n1@{ shape: proc}
    n2@{ shape: proc}
    s2@{ shape: rect}
    n3@{ shape: summary}
    n4@{ shape: cyl}
    n5@{ shape: cyl}
    n6@{ shape: cyl}

```

**Local**
In this setup, the local homelab network has all the services that should be exposed separated into the separate subnet 10.0.30.0/24. The WireGuard instance in the remote OCI instance will only have access to this subnet, limiting the scope of potential attacks on the former.

**Cloud**
The cloud instance has WireGuard listening on port 51820 with an open firewall firewall port both in *iptables* and in the OCI’s subnet security settings.

[[cloud-setup|Next >>]]