# Skill: Troubleshooting Procedures

Systematic diagnostic workflows and methodologies for IT support troubleshooting.

## Troubleshooting Methodology

### The Divide and Conquer Approach
1. **Gather Information**: Symptoms, error messages, affected systems, timeline
2. **Identify Changes**: Recent updates, deployments, configuration changes
3. **Develop Hypothesis**: Potential causes based on symptoms
4. **Test Hypothesis**: Systematic testing to confirm or eliminate causes
5. **Implement Solution**: Apply fix based on confirmed root cause
6. **Verify Resolution**: Confirm issue resolved, monitor for recurrence
7. **Document**: Record problem, solution, and prevention for future reference

### The OSI Model Troubleshooting (Network Issues)
Work from bottom to top or top to bottom:
1. **Physical (Layer 1)**: Cables connected? Link lights on?
2. **Data Link (Layer 2)**: Switch ports active? VLAN correct?
3. **Network (Layer 3)**: IP address assigned? Gateway reachable?
4. **Transport (Layer 4)**: Ports open? Firewall rules correct?
5. **Application (Layer 5-7)**: Service running? Application errors?

### The 5 Whys Root Cause Analysis
Keep asking "Why?" to drill down to root cause:
- **Why is the server down?** → Disk full
- **Why is disk full?** → Logs not rotating
- **Why are logs not rotating?** → Logrotate service not running
- **Why is logrotate not running?** → Service failed after last update
- **Why did update cause failure?** → Config file syntax error
- **Root Cause**: Config file error introduced in update

## Common Issue Patterns

### Performance Issues

#### Slow Computer
**Symptoms**: Applications slow to open, system unresponsive, high lag
**Common Causes**:
- Disk space < 10% free → Clean up files, empty trash
- High CPU usage → Identify resource-hogging process
- Low memory → Close applications, increase RAM
- Malware → Run antivirus scan
- Too many startup programs → Disable unnecessary startups
- Disk fragmentation (Windows) → Run defrag
- Failing disk → Check SMART status

**Diagnostic Commands**:
```bash
# Windows
taskmgr                      # Task Manager
wmic diskdrive get status    # Disk health
Get-ComputerInfo            # System info

# macOS
Activity Monitor            # GUI tool
top -o cpu                  # CPU usage
vm_stat                     # Memory stats

# Linux
top                         # Process monitor
df -h                       # Disk space
free -h                     # Memory usage
iostat 1                    # Disk I/O
```

#### Slow Network
**Symptoms**: Web pages slow to load, file transfers slow
**Common Causes**:
- Weak WiFi signal → Move closer to AP or switch to ethernet
- Bandwidth saturation → Identify bandwidth-hogging applications
- DNS issues → Test with different DNS server
- Network congestion → Check during different times
- ISP issues → Test with speed test, check ISP status

**Diagnostic Commands**:
```bash
# Test connectivity
ping google.com             # Basic connectivity
ping -t google.com          # Windows continuous ping
traceroute google.com       # Network path (Linux/macOS)
tracert google.com          # Network path (Windows)

# Test DNS
nslookup google.com         # DNS resolution
dig google.com              # Detailed DNS (Linux/macOS)

# Test speed
speedtest-cli               # Command-line speed test
curl -o /dev/null http://speedtest.wdc01.softlayer.com/downloads/test100.zip  # Download test
```

### Connectivity Issues

#### Cannot Access Network Share
**Symptoms**: Network drive not accessible, "path not found" errors
**Common Causes**:
- Credentials expired → Re-enter password
- Permissions changed → Verify access granted
- Server offline → Check server status
- Firewall blocking → Check firewall rules
- DNS not resolving → Check hostname resolution
- VPN not connected (for remote users) → Connect to VPN first

**Troubleshooting Steps**:
1. Test basic connectivity: `ping servername`
2. Test DNS resolution: `nslookup servername`
3. Test port connectivity: `telnet servername 445` (SMB port)
4. Verify credentials: Try mapping drive with explicit credentials
5. Check share exists: Contact server admin

#### VPN Won't Connect
**Symptoms**: VPN connection fails, timeout, or authentication errors
**Common Causes**:
- Incorrect credentials → Verify username/password
- VPN client outdated → Update to latest version
- Firewall blocking → Check firewall allows VPN ports (usually UDP 500, 4500)
- Certificate expired → Contact IT for renewed certificate
- Account locked → Reset password or unlock account
- Internet connectivity issue → Verify internet works without VPN
- VPN server offline → Check status page or contact IT

**Troubleshooting Steps**:
1. Verify internet connectivity (ping google.com)
2. Check VPN client logs for specific error
3. Try different network (mobile hotspot) to rule out firewall
4. Verify credentials work on web portal
5. Reinstall VPN client if corrupted

### Application Issues

#### Application Won't Start
**Symptoms**: App crashes on launch, "failed to initialize" errors
**Common Causes**:
- Missing dependencies → Install required libraries
- Corrupted installation → Reinstall application
- Conflicting software → Identify and remove conflicts
- Insufficient permissions → Run as administrator or check file permissions
- Config file corruption → Delete/reset config file
- OS incompatibility → Verify app version supports OS

**Diagnostic Approach**:
1. Check application logs (Event Viewer on Windows, Console on macOS, syslog on Linux)
2. Look for error messages in logs
3. Verify dependencies installed
4. Test with fresh user profile (rule out user-specific issues)
5. Reinstall application if needed

#### Application Crashes
**Symptoms**: App suddenly closes, "application has stopped working"
**Common Causes**:
- Software bug → Update to latest version
- Memory leak → Restart application periodically
- Resource exhaustion → Close other applications
- Corrupted data file → Repair or restore backup
- Plugin/extension conflict → Disable plugins one by one

**Data Collection**:
- Note exact steps to reproduce
- Check crash logs/dump files
- Note frequency (always, intermittent, specific action)
- Note recent changes (updates, new plugins, etc.)

### Access Issues

#### Account Locked
**Symptoms**: Cannot login, "account locked" message
**Common Causes**:
- Too many failed login attempts → Unlock account via help desk
- Password expired → Reset password
- Account disabled → Contact manager or HR

**Resolution**: Help desk unlocks account, user may need password reset

#### Forgotten Password
**Symptoms**: User cannot remember password
**Resolution Process**:
1. Verify user identity (employee ID, manager name, etc.)
2. Reset password in directory (AD, LDAP, etc.)
3. Provide temporary password securely (not via email)
4. Require password change on next login
5. Document password reset in ticket

### Email Issues

#### Cannot Send Email
**Symptoms**: Emails stuck in outbox, send errors
**Common Causes**:
- Mailbox quota exceeded → Delete old emails
- SMTP settings incorrect → Verify settings
- Attachment too large → Reduce attachment size (< 25MB typically)
- Recipient email invalid → Check recipient address
- Internet connectivity → Verify network working

**Troubleshooting**:
1. Check mailbox quota (usually in account settings)
2. Try sending without attachment (rule out size issue)
3. Try sending to different recipient (rule out recipient issue)
4. Check sent items (might have sent despite error)
5. Verify SMTP settings match IT standards

#### Cannot Receive Email
**Symptoms**: Not receiving expected emails
**Common Causes**:
- Mailbox quota full → Delete old emails
- Email in junk/spam folder → Check spam folder
- Email rules moving messages → Check inbox rules
- Sender issue → Have sender check their sent items
- Mail forwarding → Check if forwarding is configured

**Troubleshooting**:
1. Check mailbox quota: File > Info > Cleanup Tools
2. Check junk/spam folder
3. Check inbox rules: File > Manage Rules & Alerts
4. Have sender confirm email was sent
5. Check mail forwarding settings

## Diagnostic Command Reference

### Windows

#### System Information
```powershell
Get-ComputerInfo                    # Comprehensive system info
systeminfo                          # System details
wmic os get Caption,Version,BuildNumber,OSArchitecture  # OS info
wmic cpu get Name,NumberOfCores,NumberOfLogicalProcessors  # CPU info
wmic memorychip get Capacity,Speed  # RAM info
```

#### Process and Performance
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10  # Top CPU processes
Get-Process | Sort-Object WS -Descending | Select-Object -First 10   # Top memory processes
Get-EventLog -LogName System -Newest 50 -EntryType Error  # Recent system errors
Get-EventLog -LogName Application -Newest 50 -EntryType Error  # Recent app errors
```

#### Network Diagnostics
```powershell
ipconfig /all                      # Network configuration
Test-NetConnection -ComputerName google.com -Port 80  # Test connectivity
Get-NetAdapter                     # Network adapters
Get-NetRoute                       # Routing table
```

#### Disk
```powershell
Get-PSDrive                        # Disk space
wmic diskdrive get status          # Disk health
chkdsk C:                          # Check disk errors
```

### macOS

#### System Information
```bash
system_profiler SPHardwareDataType   # Hardware info
system_profiler SPSoftwareDataType   # Software/OS info
sysctl -n machdep.cpu.brand_string   # CPU info
sysctl hw.memsize                    # Total RAM
```

#### Process and Performance
```bash
top -o cpu                           # Top CPU processes
top -o mem                           # Top memory processes
ps aux | sort -k 3 -r | head -n 10   # Top CPU processes (alternate)
vm_stat                              # Virtual memory stats
```

#### Logs
```bash
log show --predicate 'eventMessage contains "error"' --last 1h  # Recent errors
Console.app                          # GUI log viewer
```

#### Network
```bash
ifconfig                            # Network interfaces
networksetup -listallnetworkservices  # Network services
networkQuality                      # Network quality test
scutil --nwi                        # Network interface info
```

#### Disk
```bash
df -h                               # Disk space
diskutil list                       # List disks
diskutil info disk0                 # Disk information
smartctl -a disk0                   # SMART status (requires smartmontools)
```

### Linux

#### System Information
```bash
uname -a                            # Kernel version
lsb_release -a                      # Distribution info
cat /etc/os-release                 # OS details
lscpu                               # CPU information
free -h                             # Memory info
lsblk                               # Block devices
```

#### Process and Performance
```bash
top                                 # Process monitor
htop                                # Enhanced process monitor
ps aux --sort=-%cpu | head -n 10    # Top CPU processes
ps aux --sort=-%mem | head -n 10    # Top memory processes
uptime                              # Load average
vmstat 1                            # Virtual memory stats
```

#### Logs
```bash
journalctl -xe                      # Recent systemd logs
journalctl -u servicename           # Logs for specific service
journalctl -p err                   # Error priority logs
dmesg | tail -50                    # Recent kernel messages
tail -f /var/log/syslog             # Follow syslog
```

#### Network
```bash
ip addr                             # IP addresses
ip route                            # Routing table
ss -tuln                            # Listening ports
netstat -tuln                       # Listening ports (older)
dig google.com                      # DNS query
```

#### Disk
```bash
df -h                               # Disk space
du -sh /path/to/dir                 # Directory size
iostat -x 1                         # I/O stats
smartctl -a /dev/sda                # SMART disk health
```

## Escalation Criteria

### When to Escalate to Tier 2
- Complex issues beyond documented procedures
- Requires advanced technical knowledge
- Multiple failed troubleshooting attempts
- Specialized system or application
- Time-sensitive with approaching SLA breach

### When to Escalate to Vendor
- Hardware failure under warranty
- Software bug requiring vendor patch
- Product-specific issue not documented
- Requires vendor-level access or tools

### When to Declare Major Incident
- Complete service outage affecting all users
- Critical business function unavailable
- Data loss or corruption
- Security breach
- Prolonged outage exceeding SLA thresholds

## Prevention Strategies

### Proactive Monitoring
- Set up disk space alerts (< 20% free)
- Monitor memory usage trends
- Track application crash frequency
- Watch for repeated authentication failures
- Monitor system update status

### Regular Maintenance
- Apply security patches monthly
- Clear temporary files quarterly
- Review and clean up startup programs
- Update applications to latest versions
- Archive old data regularly

### User Education
- Password best practices
- How to clear browser cache
- When to restart vs troubleshoot
- How to check disk space
- How to submit good tickets (include error messages, steps to reproduce)

## Documentation Best Practices

### Ticket Documentation Should Include
1. **Problem Description**: User's reported symptoms
2. **Steps Taken**: Diagnostic commands and tests performed
3. **Root Cause**: What caused the issue
4. **Resolution**: What fixed it
5. **Verification**: How confirmed it's fixed
6. **Prevention**: How to avoid in future (if applicable)

### Creating Runbooks
- One runbook per common task
- Step-by-step with exact commands
- Include expected outputs
- Note failure modes and troubleshooting
- Test runbook before publishing
- Keep updated with OS/software changes
