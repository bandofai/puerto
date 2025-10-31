# Skill: Network Monitoring

Performance monitoring, metrics analysis, and alerting.

## Monitoring Tools

### SNMP Monitoring
\`\`\`bash
# Query interface statistics
snmpwalk -v2c -c public 192.168.1.1 ifDescr
snmpwalk -v2c -c public 192.168.1.1 ifInOctets
snmpwalk -v2c -c public 192.168.1.1 ifOutOctets

# Monitor bandwidth
snmpget -v2c -c public 192.168.1.1 IF-MIB::ifHCInOctets.1
\`\`\`

### Network Performance Commands
\`\`\`bash
# Bandwidth testing
iperf3 -s                    # Server
iperf3 -c 192.168.1.1        # Client

# Latency monitoring
ping -c 100 192.168.1.1 | tail -1

# Packet loss detection
mtr -r -c 100 192.168.1.1

# Interface statistics
ip -s link show eth0
ifconfig eth0
netstat -i
\`\`\`

## Performance Metrics

### Key Metrics to Monitor
- **Bandwidth Utilization**: % of available capacity
- **Latency**: Round-trip time (RTT)
- **Packet Loss**: % of dropped packets
- **Jitter**: Variation in latency
- **Error Rate**: CRC errors, collisions
- **Interface Status**: Up/down, speed/duplex
- **CPU/Memory**: Device resource utilization

### Baseline Establishment
1. Collect metrics during normal operation (1-2 weeks)
2. Calculate average, median, 95th percentile
3. Set alert thresholds (e.g., 2x standard deviation)
4. Review and adjust quarterly

## Alerting Thresholds

| Metric | Warning | Critical |
|--------|---------|----------|
| Bandwidth | > 70% | > 90% |
| Latency | > 100ms | > 250ms |
| Packet Loss | > 0.5% | > 2% |
| CPU | > 70% | > 90% |
| Memory | > 80% | > 95% |
| Interface Errors | > 0.1% | > 1% |

## Log Analysis

### Syslog Patterns
\`\`\`bash
# Authentication failures
grep "authentication failure" /var/log/auth.log

# Link up/down events
grep "link.*down\|link.*up" /var/log/syslog

# High priority messages
grep -E "emerg|alert|crit|err" /var/log/syslog

# Firewall blocks
grep "BLOCK" /var/log/firewall.log | awk '{print $8}' | sort | uniq -c | sort -rn
\`\`\`

## Traffic Analysis

### tcpdump Examples
\`\`\`bash
# Capture traffic on specific port
tcpdump -i eth0 port 80 -w capture.pcap

# Analyze packet sizes
tcpdump -i eth0 -nn -q | awk '{print $NF}' | sort | uniq -c

# Monitor specific host
tcpdump -i eth0 host 192.168.1.100

# Capture syn packets (potential scan)
tcpdump -i eth0 'tcp[tcpflags] & tcp-syn != 0'
\`\`\`

## Capacity Planning

### Growth Analysis
1. Collect bandwidth data over 6-12 months
2. Calculate growth rate (month-over-month)
3. Project future capacity needs
4. Plan upgrades 6 months before capacity exhaustion

### Example Calculation
- Current peak: 700 Mbps (70% of 1 Gbps)
- Growth rate: 10% per month
- Months to 90%: ~3 months
- Action: Upgrade to 10 Gbps within 2 months

## Monitoring Tools Integration

### Prometheus + Grafana
\`\`\`yaml
scrape_configs:
  - job_name: 'network_devices'
    static_configs:
      - targets: ['192.168.1.1:9100']
\`\`\`

### Zabbix SNMP Monitoring
- Template: Network Generic Device by SNMP
- Macros: SNMP community, timeout
- Items: interface status, bandwidth, errors
- Triggers: bandwidth > 80%, interface down

### Nagios Plugins
\`\`\`bash
# Check interface status
check_snmp_interface -H 192.168.1.1 -C public -n eth0

# Check bandwidth
check_snmp_bandwidth -H 192.168.1.1 -C public -w 70 -c 90
\`\`\`
