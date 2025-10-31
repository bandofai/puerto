# Skill: Network Configuration

Network device configuration, VPN setup, and service management.

## Device Configuration Syntax

### Cisco IOS
\`\`\`
hostname Router1
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
router ospf 1
 network 192.168.1.0 0.0.0.255 area 0
\`\`\`

### Juniper JunOS
\`\`\`
set system host-name Router1
set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.1/24
set protocols ospf area 0.0.0.0 interface ge-0/0/0.0
\`\`\`

### Linux iptables
\`\`\`bash
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -P INPUT DROP
\`\`\`

## VPN Configuration

### OpenVPN Server
\`\`\`
port 1194
proto udp
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh2048.pem
server 10.8.0.0 255.255.255.0
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 8.8.8.8"
\`\`\`

### WireGuard
\`\`\`ini
[Interface]
PrivateKey = <server_private_key>
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
PublicKey = <client_public_key>
AllowedIPs = 10.0.0.2/32
\`\`\`

## Network Services

### DHCP Configuration (ISC DHCP)
\`\`\`
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.200;
  option routers 192.168.1.1;
  option domain-name-servers 8.8.8.8, 8.8.4.4;
  default-lease-time 86400;
}
\`\`\`

### DNS Configuration (BIND)
\`\`\`
zone "example.com" {
  type master;
  file "/etc/bind/db.example.com";
};

// Zone file
@ IN SOA ns1.example.com. admin.example.com. (
  2025102001 ; Serial
  3600       ; Refresh
  1800       ; Retry
  604800     ; Expire
  86400 )    ; Minimum TTL
@ IN NS ns1.example.com.
www IN A 192.168.1.10
\`\`\`

## VLAN Configuration

### Cisco Switch
\`\`\`
vlan 10
 name Engineering
vlan 20
 name Sales

interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10
 
interface GigabitEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20
\`\`\`

## Routing Protocols

### OSPF
\`\`\`
router ospf 1
 router-id 1.1.1.1
 network 192.168.1.0 0.0.0.255 area 0
 network 10.0.0.0 0.255.255.255 area 0
\`\`\`

### BGP
\`\`\`
router bgp 65001
 neighbor 203.0.113.1 remote-as 65002
 network 192.168.1.0 mask 255.255.255.0
\`\`\`

## Configuration Management Best Practices

1. **Version Control**: Store all configs in git
2. **Backup Before Changes**: Always backup current config
3. **Test in Lab**: Validate configs in test environment
4. **Change Management**: Document all changes
5. **Rollback Plan**: Have rollback procedure ready
6. **Configuration Templates**: Use templates for consistency
7. **Validation**: Syntax check before applying
8. **Documentation**: Comment complex configurations
