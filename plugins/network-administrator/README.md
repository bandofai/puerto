# Network Administrator Plugin

**Version**: 1.0.0

Network management and monitoring specialist for configuration, performance monitoring, security enforcement, and troubleshooting.

## Overview

Complete network administration solution with 4 specialized agents covering device configuration, performance monitoring, security policy enforcement, and troubleshooting across multi-vendor environments.

## Agents

### 1. network-config-manager (Haiku - Fast Configuration)
**Purpose**: Generate network device configurations quickly
**Model**: haiku-3.5 (~$0.001/1K tokens)
**Why Haiku**: Template-based config generation is deterministic, Haiku provides 3x faster execution

**Capabilities**:
- Network device configs (routers, switches, firewalls)
- VPN configurations (OpenVPN, WireGuard, IPSec)
- DHCP/DNS service configuration
- Template-based generation with validation

**Usage**: `@network-config-manager "Generate OpenVPN server config for remote access VPN, subnet 10.8.0.0/24"`

---

### 2. network-monitor (Sonnet - Performance Analysis)
**Purpose**: Network performance monitoring and analysis
**Model**: sonnet-3.5 (~$0.015/1K tokens)
**Why Sonnet**: Requires pattern recognition and anomaly detection

**Capabilities**:
- Performance metrics analysis (bandwidth, latency, packet loss)
- Log parsing and interpretation
- Anomaly detection with alerts
- Traffic pattern analysis
- Capacity planning recommendations

**Usage**: `@network-monitor "Analyze network performance for past 24 hours, identify bottlenecks"`

---

### 3. security-policy-enforcer (Sonnet - Security Judgment)
**Purpose**: Security policy enforcement and compliance
**Model**: sonnet-3.5 (~$0.015/1K tokens)
**Why Sonnet**: Security decisions require judgment and compliance validation

**Capabilities**:
- Firewall rule generation (iptables, pf, Cisco ACLs)
- Network segmentation enforcement
- IDS/IPS rule creation
- Compliance auditing (CIS, PCI-DSS, NIST)
- Security policy documentation

**Usage**: `@security-policy-enforcer "Generate firewall rules for PCI-DSS cardholder data environment"`

---

### 4. network-troubleshooter (Sonnet - Diagnostic Reasoning)
**Purpose**: Network diagnostics and troubleshooting
**Model**: sonnet-3.5 (~$0.015/1K tokens)
**Why Sonnet**: Troubleshooting requires diagnostic reasoning and root cause analysis

**Capabilities**:
- Connectivity diagnosis (Layer 2/3/4/7)
- Packet capture analysis
- Root cause identification
- Step-by-step remediation guides
- Incident post-mortems

**Usage**: `@network-troubleshooter "User cannot access internal server from VPN, diagnose issue"`

## Skills

### 1. network-configuration (8KB)
Device configuration syntax, VPN setup, network services

**Contents**:
- Cisco IOS, Juniper JunOS, Linux configurations
- VPN protocols (OpenVPN, WireGuard, IPSec)
- VLAN and routing protocols (OSPF, BGP)
- DHCP/DNS configuration
- Configuration management best practices

---

### 2. network-monitoring (7KB)
Performance monitoring, metrics analysis, alerting

**Contents**:
- SNMP monitoring techniques
- Performance metrics and baselines
- Alert threshold configuration
- Log analysis patterns
- Traffic analysis with tcpdump
- Capacity planning methodologies

---

### 3. network-security (9KB)
Firewall management, security policies, compliance

**Contents**:
- Firewall rule design (iptables, pf, Cisco ACL)
- Network segmentation and zero-trust
- IDS/IPS rule creation (Snort, Fail2Ban)
- Compliance frameworks (CIS, PCI-DSS, NIST)
- Security audit procedures
- Threat detection patterns

## Templates

### 1. firewall-rules-template.conf
Complete iptables firewall configuration with zone-based security

**Includes**:
- Default deny policies
- Zone definitions (WAN, LAN, DMZ)
- Management access rules
- Logging configuration

---

### 2. vpn-config-template.ovpn
OpenVPN client configuration template

**Includes**:
- Connection parameters
- Encryption settings (AES-256, SHA-256)
- TLS authentication
- DNS configuration

---

### 3. network-report-template.md
Comprehensive network performance report

**Includes**:
- Executive summary with health status
- Interface statistics
- Latency and packet loss metrics
- Top bandwidth consumers
- Security events
- Capacity planning analysis
- Recommendations

## Workflows

### Workflow 1: VPN Deployment
```
@network-config-manager "Create OpenVPN server config"
→ @security-policy-enforcer "Generate firewall rules for VPN"
→ @network-monitor "Monitor VPN connection stability"
```

### Workflow 2: Performance Issue Investigation
```
@network-monitor "High latency detected on WAN link"
→ @network-troubleshooter "Diagnose WAN latency issue"
→ Remediation steps provided
```

### Workflow 3: Security Compliance Audit
```
@security-policy-enforcer "Audit firewall against CIS benchmarks"
→ Generate compliance report
→ Provide remediation recommendations
```

### Workflow 4: Network Configuration Change
```
@network-config-manager "Add new VLAN 50 for IoT devices"
→ @security-policy-enforcer "Create segmentation rules for IoT VLAN"
→ @network-monitor "Monitor new VLAN performance"
```

## Key Features

✅ **Multi-Vendor Support**: Cisco, Juniper, pfSense, Linux
✅ **VPN Technologies**: OpenVPN, WireGuard, IPSec
✅ **Performance Monitoring**: Real-time metrics, anomaly detection
✅ **Security Enforcement**: Firewall rules, network segmentation
✅ **Compliance**: CIS Benchmarks, PCI-DSS, NIST
✅ **Troubleshooting**: Systematic diagnostics with OSI model approach
✅ **Cost-Optimized**: Haiku for configs, Sonnet for analysis

## Architecture

```
┌────────────────────┐
│ network-config-    │ (Fast config generation)
│ manager (Haiku)    │
└────────────────────┘
         │
    ┌────┴──────────────────┬─────────────────────┐
    │                       │                     │
┌───▼──────────┐  ┌────────▼─────┐  ┌───────────▼──────┐
│ network-     │  │ security-    │  │ network-         │
│ monitor      │  │ policy-      │  │ troubleshooter   │
│ (Sonnet)     │  │ enforcer     │  │ (Sonnet)         │
│              │  │ (Sonnet)     │  │                  │
│ Analysis &   │  │ Security &   │  │ Diagnostics &    │
│ Reporting    │  │ Compliance   │  │ Remediation      │
└──────────────┘  └──────────────┘  └──────────────────┘
```

## Usage Examples

### Example 1: Create Firewall Rules for DMZ
```bash
@security-policy-enforcer "Generate firewall rules for DMZ hosting web server (HTTP/HTTPS) at 192.168.100.10, allow from internet, deny all else"
```

**Output**: Complete iptables configuration with logging

---

### Example 2: Monitor Network Performance
```bash
@network-monitor "Generate weekly performance report for network 10.0.1.0/24, highlight any anomalies or capacity issues"
```

**Output**: Comprehensive report with bandwidth utilization, latency metrics, capacity recommendations

---

### Example 3: Troubleshoot VPN Issue
```bash
@network-troubleshooter "Users report VPN connects but cannot access internal resources. VPN subnet: 10.8.0.0/24, Internal network: 192.168.1.0/24"
```

**Output**: Step-by-step diagnosis (routing, firewall, NAT) with specific commands and remediation

---

### Example 4: Setup Site-to-Site VPN
```bash
@network-config-manager "Create IPSec site-to-site VPN between Site A (203.0.113.1, LAN: 10.0.1.0/24) and Site B (198.51.100.1, LAN: 10.0.2.0/24)"
```

**Output**: IPSec configuration for both sites with PSK and routing

---

### Example 5: Security Compliance Audit
```bash
@security-policy-enforcer "Audit current firewall configuration against PCI-DSS requirements for cardholder data environment. Identify gaps and provide remediation steps."
```

**Output**: Compliance checklist, identified gaps, prioritized remediation recommendations

## Performance Metrics

- **Config Generation**: < 10 seconds
- **Performance Analysis**: 2-5 minutes
- **Security Audit**: 5-10 minutes
- **Troubleshooting**: 5-15 minutes
- **Cost per Task**: $0.01-0.20

## Installation

Plugin located at: `plugins/network-administrator/`

Agents automatically available:
```
@network-config-manager
@network-monitor
@security-policy-enforcer
@network-troubleshooter
```

## Design Decisions

### Why Haiku for Config Manager?
- Configuration generation is template-based (deterministic)
- No complex decision-making required
- 3x faster than Sonnet
- 15x cheaper than Sonnet
- Sufficient for validation and template processing

### Why Sonnet for Monitoring, Security, Troubleshooting?
- Monitoring requires anomaly detection and pattern analysis
- Security needs judgment for rule design and compliance
- Troubleshooting requires diagnostic reasoning
- All benefit from Sonnet's intelligence at reasonable cost

### Multi-Vendor Support
- Abstract common patterns in skills
- Device-specific syntax in templates
- Agents adapt output format based on target platform

## Compliance Coverage

- **CIS Benchmarks**: Network device hardening
- **PCI-DSS**: Network segmentation, firewall management
- **NIST Cybersecurity Framework**: Identify, Protect, Detect, Respond, Recover
- **ISO 27001**: Information security controls

## Troubleshooting

**Issue**: Generated config doesn't work on device
**Solution**: Verify device type and OS version, check syntax in network-configuration skill

**Issue**: Monitoring not detecting issues
**Solution**: Verify SNMP community strings, check firewall allows monitoring traffic

**Issue**: Security audit failing
**Solution**: Review compliance requirements in network-security skill, ensure all requirements understood

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-10-20 | Initial release: 4 agents, 3 skills, 3 templates |

---

**Built with ❤️ by the Puerto Plugin System**
**Designed with @ultimate-subagent-creator**
