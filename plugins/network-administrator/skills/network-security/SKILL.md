# Skill: Network Security

Firewall management, security policies, and compliance.

## Firewall Rule Design

### Principle of Least Privilege
- Default deny all traffic
- Explicitly allow only required services
- Log denied traffic for analysis
- Review rules quarterly

### Rule Structure Best Practices
1. **Order Matters**: Most specific first, most general last
2. **Documentation**: Comment every rule with business justification
3. **Grouping**: Group related rules together
4. **Cleanup**: Remove unused rules regularly
5. **Testing**: Test in lab before production

## Firewall Examples

### iptables (Linux)
\`\`\`bash
# Default policies
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow established connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH from management network
iptables -A INPUT -s 10.0.0.0/24 -p tcp --dport 22 -j ACCEPT

# Allow HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Log and drop everything else
iptables -A INPUT -j LOG --log-prefix "DROPPED INPUT: "
iptables -A INPUT -j DROP

# Save rules
iptables-save > /etc/iptables/rules.v4
\`\`\`

### pfSense/FreeBSD pf
\`\`\`
# Interfaces
wan_if = "em0"
lan_if = "em1"

# Networks
lan_net = "192.168.1.0/24"

# Default deny
block all

# Allow outbound from LAN
pass out on $wan_if from $lan_net to any

# Allow inbound to specific services
pass in on $wan_if proto tcp to port {80, 443} keep state

# Allow LAN to access firewall
pass in on $lan_if from $lan_net to any
\`\`\`

### Cisco ACL
\`\`\`
ip access-list extended DMZ_IN
 remark Allow HTTP/HTTPS from Internet
 permit tcp any host 203.0.113.10 eq 80
 permit tcp any host 203.0.113.10 eq 443
 remark Allow established connections
 permit tcp any any established
 remark Deny and log everything else
 deny ip any any log
 
interface GigabitEthernet0/0
 ip access-group DMZ_IN in
\`\`\`

## Network Segmentation

### Zero-Trust Architecture
- Segment network into zones based on trust level
- Enforce strict access controls between zones
- Monitor all inter-zone traffic
- Require authentication for all access

### Common Segmentation Patterns

**Three-Tier Architecture**:
1. **Internet (Untrusted)**: Public internet
2. **DMZ (Low Trust)**: Public-facing services
3. **Internal (Medium Trust)**: Internal applications
4. **Secure Zone (High Trust)**: Databases, sensitive data

**VLAN Segmentation**:
- VLAN 10: Management (10.0.10.0/24)
- VLAN 20: Servers (10.0.20.0/24)
- VLAN 30: Users (10.0.30.0/24)
- VLAN 40: Guest (10.0.40.0/24)
- VLAN 50: IoT Devices (10.0.50.0/24)

## Intrusion Detection/Prevention

### Snort Rules
\`\`\`
# Detect SSH brute force
alert tcp any any -> $HOME_NET 22 (flags: S; threshold: type both, track by_src, count 5, seconds 60; msg:"SSH brute force attempt"; sid:1000001;)

# Detect SQL injection attempts
alert tcp any any -> $HOME_NET 80 (content:"UNION"; nocase; content:"SELECT"; nocase; msg:"SQL injection attempt"; sid:1000002;)

# Detect port scans
alert tcp any any -> $HOME_NET any (flags: S; threshold: type both, track by_src, count 20, seconds 10; msg:"Port scan detected"; sid:1000003;)
\`\`\`

### Fail2Ban Configuration
\`\`\`ini
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600
\`\`\`

## Compliance Frameworks

### CIS Benchmarks
- Disable unused network services
- Enable logging and auditing
- Implement strong authentication
- Encrypt sensitive data in transit
- Regular security updates

### PCI-DSS Network Requirements
- **Requirement 1**: Install and maintain firewall
  - Deny all inbound traffic by default
  - Restrict connections between CDE and internet
  - No direct routes between internet and CDE

- **Requirement 4**: Encrypt transmission
  - Use strong cryptography (TLS 1.2+)
  - Never send unencrypted PANs
  - Verify encryption before transmission

### NIST Cybersecurity Framework
- **Identify**: Asset inventory, risk assessment
- **Protect**: Access control, security awareness
- **Detect**: Continuous monitoring, anomaly detection
- **Respond**: Incident response plan, communications
- **Recover**: Recovery planning, improvements

## Security Audit Procedures

### Firewall Rule Audit
1. List all rules
2. Identify unused rules (no hits in 90 days)
3. Check for overly permissive rules (any to any)
4. Verify logging on critical rules
5. Confirm rules match documentation
6. Remove or tighten unnecessary rules

### Configuration Hardening Checklist
- [ ] Change default passwords
- [ ] Disable unused services
- [ ] Enable logging
- [ ] Implement NTP for time synchronization
- [ ] Configure SNMP v3 (not v1/v2c)
- [ ] Enable encrypted management (SSH, HTTPS)
- [ ] Implement banner warnings
- [ ] Configure backup and restore procedures

### Penetration Testing
- External scan from internet
- Internal scan from user network
- Vulnerability assessment with Nessus/OpenVAS
- Manual testing of critical services
- Social engineering tests
- Remediate findings within SLA (Critical: 7 days, High: 30 days)

## Threat Detection

### Common Attack Patterns
- **Port Scanning**: Multiple connection attempts to different ports
- **Brute Force**: Multiple authentication failures from same source
- **DDoS**: High volume of requests from multiple sources
- **Data Exfiltration**: Large outbound data transfers
- **Lateral Movement**: Internal scanning and connection attempts

### Response Actions
1. **Detect**: Monitor logs and alerts
2. **Analyze**: Confirm attack vs false positive
3. **Contain**: Block malicious IPs/networks
4. **Eradicate**: Remove attack vectors
5. **Recover**: Restore normal operations
6. **Learn**: Update rules and procedures
