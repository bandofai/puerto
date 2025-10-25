# Skill: System Diagnostics

Comprehensive system health assessment, log analysis, and diagnostic techniques across Windows, macOS, and Linux platforms.

## Diagnostic Approach

### Systematic Diagnostic Process
1. **Gather initial information**: Symptoms, error messages, affected systems
2. **Check recent changes**: Updates, deployments, configuration changes
3. **Baseline comparison**: Compare current state vs known good state
4. **Resource check**: CPU, memory, disk, network utilization
5. **Log analysis**: System logs, application logs, error logs
6. **Hardware health**: Temperature, SMART status, hardware errors
7. **Root cause identification**: Correlate symptoms to specific cause
8. **Remediation**: Apply fix based on diagnosis
9. **Verification**: Confirm issue resolved and monitor

### Data Collection Best Practices
- Capture error messages exactly (screenshot or copy/paste)
- Note exact time of issue occurrence
- Identify what changed recently
- Document steps to reproduce
- Collect relevant log excerpts
- Note system configuration details

## Windows Diagnostics

### Event Viewer

#### Log Types
- **Application**: Application-specific events
- **System**: Windows system events (drivers, services)
- **Security**: Security auditing (login, access, policy changes)
- **Setup**: Windows installation and update events

#### Common Error Patterns
- **Event ID 7001**: Service dependency failure
- **Event ID 7031**: Service crashed unexpectedly
- **Event ID 1000**: Application crash
- **Event ID 10016**: DCOM permission issues
- **Event ID 41**: System powered off improperly

#### PowerShell Event Log Commands
```powershell
# Recent errors from System log
Get-EventLog -LogName System -EntryType Error -Newest 50

# Specific event ID
Get-EventLog -LogName System -InstanceId 7031 -Newest 20

# Events from last 24 hours
Get-EventLog -LogName Application -After (Get-Date).AddDays(-1) -EntryType Error

# Export errors to file
Get-EventLog -LogName System -EntryType Error -Newest 100 | Export-Csv errors.csv
```

### Performance Monitoring

#### Task Manager Analysis
- **Processes tab**: CPU and memory usage per process
- **Performance tab**: Overall system metrics
- **Users tab**: Resource usage per user session
- **Details tab**: PID, command line, priority

#### Resource Monitor
- **Overview**: Summary of CPU, memory, disk, network
- **CPU**: Which processes using CPU, thread count
- **Memory**: Physical memory usage, paging
- **Disk**: Read/write activity per process
- **Network**: Network activity per process

#### Performance Monitor (perfmon)
```powershell
# Counter examples
\Processor(_Total)\% Processor Time        # Overall CPU usage
\Memory\Available MBytes                   # Available RAM
\PhysicalDisk(_Total)\% Disk Time         # Disk busy percentage
\Network Interface(*)\Bytes Total/sec     # Network throughput

# Create data collector set for continuous monitoring
perfmon /rel                              # Reliability Monitor
```

### System Information Tools

```powershell
# Comprehensive system info
Get-ComputerInfo

# OS details
wmic os get Caption,Version,BuildNumber,OSArchitecture,LastBootUpTime

# Hardware details
wmic cpu get Name,NumberOfCores,NumberOfLogicalProcessors
wmic memorychip get Capacity,Speed,Manufacturer
wmic diskdrive get Model,Size,Status

# Services status
Get-Service | Where-Object {$_.Status -eq 'Stopped'} | Where-Object {$_.StartType -eq 'Automatic'}

# Installed software
Get-WmiObject -Class Win32_Product | Select-Object Name,Version
```

### Network Diagnostics

```powershell
# Network configuration
ipconfig /all
Get-NetAdapter
Get-NetIPAddress
Get-NetRoute

# DNS and connectivity
nslookup google.com
Resolve-DnsName google.com
Test-NetConnection -ComputerName google.com -Port 80

# Network statistics
netstat -ano                             # All connections with PID
netstat -b                               # Show executable
Get-NetTCPConnection                     # PowerShell equivalent

# Reset network
ipconfig /flushdns                       # Clear DNS cache
netsh winsock reset                      # Reset winsock
netsh int ip reset                       # Reset IP stack
```

### Disk Diagnostics

```powershell
# Disk space
Get-PSDrive -PSProvider FileSystem

# Disk health
wmic diskdrive get status
Get-PhysicalDisk
Get-Disk

# SMART status (requires admin)
Get-PhysicalDisk | Get-StorageReliabilityCounter

# Check disk for errors
chkdsk C: /scan                          # Quick scan
chkdsk C: /f /r                          # Full repair (requires reboot)

# File system integrity
sfc /scannow                             # System File Checker
DISM /Online /Cleanup-Image /RestoreHealth  # Repair Windows image
```

## macOS Diagnostics

### Console and Log Analysis

#### Log Locations
- **/var/log/system.log**: General system log
- **/var/log/install.log**: Software installation log
- **~/Library/Logs**: User-specific application logs
- **/Library/Logs**: System-wide application logs
- **Console.app**: GUI log viewer

#### Unified Logging System
```bash
# Recent errors
log show --predicate 'eventMessage contains "error"' --last 1h

# Specific subsystem
log show --predicate 'subsystem == "com.apple.securityd"' --last 1d

# Application logs
log show --predicate 'processImagePath contains "Safari"' --last 1h

# Stream live logs
log stream --predicate 'eventType == logEvent and messageType == error'
```

### System Information

```bash
# Hardware overview
system_profiler SPHardwareDataType

# Software/OS info
system_profiler SPSoftwareDataType

# Disk info
system_profiler SPStorageDataType

# Network info
system_profiler SPNetworkDataType

# CPU info
sysctl -n machdep.cpu.brand_string
sysctl hw.ncpu                          # CPU core count

# Memory info
sysctl hw.memsize                       # Total RAM in bytes
vm_stat                                 # Virtual memory stats
```

### Performance Monitoring

```bash
# Activity Monitor (command line alternatives)
top -o cpu                              # Top CPU processes
top -o mem                              # Top memory processes
top -l 1 -s 0 | head -n 10             # One-time snapshot

# Detailed process info
ps aux                                  # All processes
ps aux | sort -k 3 -r | head -n 10     # Top CPU processes

# System load
uptime                                  # Load average
sysctl -n vm.loadavg                   # Load average values

# Disk I/O
iostat -w 1                            # Disk I/O stats every 1 second
```

### Network Diagnostics

```bash
# Network configuration
ifconfig                                # Network interfaces
networksetup -listallnetworkservices   # List network services
scutil --nwi                           # Network interface info

# Connectivity testing
ping -c 4 google.com
traceroute google.com
nc -zv hostname port                    # Test port connectivity

# DNS
scutil --dns                           # DNS configuration
dscacheutil -q host -a name google.com # DNS lookup

# Network quality
networkQuality                          # Network performance test (macOS 12+)

# Active connections
lsof -i                                # List open network connections
netstat -an                            # Network statistics
```

### Disk Diagnostics

```bash
# Disk space
df -h                                   # Disk free space
du -sh /path/to/dir                    # Directory size
ncdu /path/to/dir                      # Interactive disk usage (if installed)

# Disk info
diskutil list                          # List all disks
diskutil info disk0                    # Detailed disk info

# SMART status
diskutil info disk0 | grep SMART       # SMART status
smartctl -a disk0                      # Detailed SMART (requires smartmontools)

# Verify and repair
diskutil verifyVolume /                # Verify filesystem
diskutil repairVolume /                # Repair filesystem (from Recovery)

# Permissions (older macOS versions)
diskutil resetUserPermissions / $(id -u)
```

### Application and Crash Diagnostics

```bash
# Crash reports
open ~/Library/Logs/DiagnosticReports   # User crash reports
open /Library/Logs/DiagnosticReports    # System crash reports

# Recently modified crash reports
ls -lt ~/Library/Logs/DiagnosticReports | head

# Application hang samples
sample <process-name> -mayDie          # Create sample of hung process

# Core dumps location
launchctl limit core                    # Check core dump limits
```

## Linux Diagnostics

### Log Analysis with journalctl

```bash
# Recent logs (systemd)
journalctl -xe                          # Recent errors with explanation
journalctl -f                           # Follow logs (like tail -f)

# Priority filtering
journalctl -p err                       # Error priority and above
journalctl -p warning                   # Warning priority and above

# Time-based
journalctl --since "2025-10-20 14:00"
journalctl --since "1 hour ago"
journalctl --until "2025-10-20 16:00"

# Service-specific
journalctl -u nginx.service            # Logs for nginx service
journalctl -u ssh.service --since today

# Kernel messages
journalctl -k                          # Kernel messages
dmesg | tail -50                       # Last 50 kernel messages
dmesg -T | grep -i error               # Kernel errors with timestamps
```

### Traditional Log Files

```bash
# Common log locations
tail -f /var/log/syslog                # System log (Debian/Ubuntu)
tail -f /var/log/messages              # System log (RHEL/CentOS)
tail -f /var/log/auth.log              # Authentication log
tail -f /var/log/kern.log              # Kernel log

# Application logs
tail -f /var/log/apache2/error.log     # Apache errors
tail -f /var/log/nginx/error.log       # Nginx errors
tail -f /var/log/mysql/error.log       # MySQL errors

# Search logs for errors
grep -i error /var/log/syslog | tail -50
zgrep -i error /var/log/syslog.*.gz    # Search compressed logs
```

### System Information

```bash
# OS information
uname -a                               # Kernel version
cat /etc/os-release                    # Distribution info
lsb_release -a                         # Detailed distribution info
hostnamectl                            # System info (systemd)

# Hardware information
lscpu                                  # CPU information
lsmem                                  # Memory information
lsblk                                  # Block devices
lspci                                  # PCI devices
lsusb                                  # USB devices
dmidecode                              # DMI/SMBIOS info (requires root)

# Detailed hardware
hwinfo --short                         # Hardware summary (if installed)
inxi -Fx                               # System info (if installed)
```

### Performance Monitoring

```bash
# Process monitoring
top                                    # Classic process monitor
htop                                   # Enhanced process monitor (if installed)
atop                                   # Advanced system monitor (if installed)

# System load
uptime                                 # Load average and uptime
w                                      # Who is logged in and load

# Memory
free -h                                # Memory usage (human-readable)
vmstat 1                               # Virtual memory stats every 1 second
cat /proc/meminfo                      # Detailed memory info

# CPU
mpstat 1                               # CPU stats every 1 second
sar -u 1 10                           # CPU usage, 10 samples

# Disk I/O
iostat -x 1                           # Extended I/O stats every 1 second
iotop                                 # I/O per process (requires root)

# Network I/O
iftop                                 # Network bandwidth per connection (requires root)
nethogs                               # Network bandwidth per process (requires root)
ss -s                                 # Socket statistics summary
```

### Network Diagnostics

```bash
# Network configuration
ip addr                                # IP addresses (modern)
ip route                               # Routing table
ifconfig                               # Network interfaces (legacy)

# Connectivity
ping -c 4 google.com
traceroute google.com
mtr google.com                         # My traceroute (combined ping/traceroute)

# DNS
dig google.com                         # Detailed DNS query
nslookup google.com                    # Simple DNS lookup
host google.com                        # Simple DNS lookup

# Port testing
telnet hostname port
nc -zv hostname port                   # Netcat port scan
nmap -p port hostname                  # Nmap port scan

# Active connections
ss -tuln                               # Listening TCP/UDP sockets (modern)
netstat -tuln                          # Listening sockets (legacy)
ss -tupn                               # Established connections with process

# Network statistics
ss -s                                  # Socket statistics
netstat -i                             # Interface statistics
```

### Disk Diagnostics

```bash
# Disk space
df -h                                  # Disk free space
df -i                                  # Inode usage
du -sh /path/to/dir                    # Directory size
du -sh /* | sort -h                    # Size of root directories

# Find large files
find /path -type f -size +100M         # Files larger than 100MB
du -ah /path | sort -rh | head -n 20  # 20 largest files/dirs

# Disk performance
iostat -x 1                            # Disk I/O stats
iotop                                  # Disk I/O per process

# SMART status
smartctl -a /dev/sda                   # SMART attributes
smartctl -H /dev/sda                   # Health status only

# Filesystem check (requires unmount or boot from rescue)
fsck /dev/sda1                         # Filesystem check
e2fsck -f /dev/sda1                    # ext2/ext3/ext4 check

# Disk info
lsblk                                  # List block devices
fdisk -l                               # Partition tables
blkid                                  # Block device attributes
```

### Service and Process Diagnostics

```bash
# Systemd services
systemctl status servicename           # Service status
systemctl is-active servicename        # Check if running
systemctl is-enabled servicename       # Check if enabled at boot
systemctl list-units --failed          # Failed services

# Process information
ps aux | grep processname              # Find process
pgrep -a processname                   # Find process by name
pidof processname                      # Get PID of process
top -p PID                             # Monitor specific process
htop -p PID                            # Monitor specific process (enhanced)

# Process tree
pstree                                 # Process tree
ps auxf                                # Process forest view

# Kill process
kill PID                               # Graceful termination
kill -9 PID                            # Force kill
pkill processname                      # Kill by name
killall processname                    # Kill all instances
```

## Hardware Health Monitoring

### Temperature Monitoring

#### Windows
```powershell
# Requires third-party tools
# Core Temp, HWMonitor, Open Hardware Monitor
wmic /namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature
```

#### macOS
```bash
# Requires istats or smcFanControl
sudo powermetrics --samplers smc | grep -i "CPU die temperature"
```

#### Linux
```bash
sensors                                # lm-sensors package
cat /sys/class/thermal/thermal_zone*/temp  # Temperature in millidegrees
watch sensors                          # Real-time monitoring
```

### Disk SMART Status

#### All Platforms
```bash
# Install smartmontools first
smartctl -a /dev/sda                   # All SMART info
smartctl -H /dev/sda                   # Health status only
smartctl -t short /dev/sda             # Run short self-test
smartctl -l selftest /dev/sda          # View test results
```

**Key SMART Attributes**:
- **Reallocated_Sector_Ct**: Increasing = disk failing
- **Current_Pending_Sector**: Non-zero = potential bad sectors
- **Offline_Uncorrectable**: Non-zero = disk errors
- **Temperature**: High temps reduce disk lifespan
- **Power_On_Hours**: Disk age

### Memory Diagnostics

#### Windows
```powershell
# Memory diagnostics tool
mdsched.exe                            # Windows Memory Diagnostic

# Check for memory errors in Event Viewer
Get-EventLog -LogName System -Source "Microsoft-Windows-MemoryDiagnostics-Results"
```

#### Linux
```bash
# memtest86+ (boot from USB/CD)
# Check dmesg for memory errors
dmesg | grep -i "memory\|ecc"
grep -i "hardware error" /var/log/messages
```

## Common Diagnostic Scenarios

### High CPU Usage

**Investigation Steps**:
1. Identify process consuming CPU
2. Determine if legitimate workload or issue
3. Check for malware (unusual process names)
4. Review process start time (did it hang?)
5. Check for resource leaks

**Resolution Options**:
- Restart problematic application
- Kill runaway process
- Update software with bug fix
- Increase CPU resources
- Optimize application configuration

### High Memory Usage

**Investigation Steps**:
1. Check available memory
2. Identify memory-consuming processes
3. Check for memory leaks (growing over time)
4. Review page file/swap usage
5. Check for memory-intensive recent changes

**Resolution Options**:
- Close unnecessary applications
- Restart leaking applications
- Clear cache files
- Add more RAM
- Tune application memory settings

### Disk Space Exhaustion

**Investigation Steps**:
1. Check disk space: `df -h`
2. Find large directories: `du -sh /*`
3. Find large files: `find / -type f -size +1G`
4. Check log file sizes
5. Check for filled partitions (/tmp, /var)

**Resolution Options**:
- Delete old log files
- Clean up temporary files
- Archive or compress old data
- Move data to different partition/disk
- Increase disk space

### Network Connectivity Issues

**Investigation Steps**:
1. Test local interface (localhost)
2. Test gateway (default route)
3. Test external host (google.com)
4. Test DNS resolution
5. Check firewall rules
6. Review network logs

**Resolution Options**:
- Restart network interface
- Reset network stack
- Flush DNS cache
- Update network drivers
- Modify firewall rules
- Check physical connections

## Diagnostic Reports

### Information to Include
- **System details**: OS, hardware, configuration
- **Problem description**: Symptoms, error messages
- **Resource utilization**: CPU, memory, disk, network metrics
- **Log excerpts**: Relevant error messages
- **Recent changes**: Updates, deployments, config changes
- **Root cause**: Technical explanation of issue
- **Remediation steps**: How to fix
- **Verification**: How to confirm fixed
- **Prevention**: How to avoid in future

### Report Format
Use the diagnostic-report.md template for consistency and completeness.

## Diagnostic Tools Summary

| Platform | CPU | Memory | Disk | Network | Logs |
|----------|-----|--------|------|---------|------|
| **Windows** | Task Manager, perfmon | Resource Monitor | chkdsk, SMART | ipconfig, Test-NetConnection | Event Viewer |
| **macOS** | Activity Monitor, top | vm_stat | diskutil, SMART | ifconfig, networkQuality | Console, log show |
| **Linux** | top, htop, mpstat | free, vmstat | df, iostat, SMART | ip, ss, iftop | journalctl, dmesg |
