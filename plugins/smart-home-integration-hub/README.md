# Smart Home Integration Hub Plugin

**Comprehensive smart home device coordination, automation, energy monitoring, and multi-platform integration**

Version: 1.0.0
Category: Smart Home
Issue: #113

---

## Overview

The Smart Home Integration Hub plugin provides a complete solution for managing smart home devices, creating intelligent automation routines, monitoring energy consumption, and integrating with major smart home platforms (Google Home, Alexa, HomeKit, IFTTT).

This plugin combines device coordination, automation building, energy optimization, and seamless platform integration to create a unified smart home management experience.

---

## Features

### Device Management
- **Device Discovery**: Automatic network scanning and platform-specific discovery
- **Device Registration**: Centralized device registry with metadata
- **Status Monitoring**: Real-time connectivity and health monitoring
- **Dashboard Generation**: Comprehensive status dashboards
- **Anomaly Detection**: Offline device detection and connectivity alerts

### Automation & Routines
- **Pre-built Routines**: Morning, evening, and away mode automations
- **Conditional Logic**: Complex if-then-else automation rules
- **Scene Management**: Multi-device scene creation and activation
- **Voice Integration**: Natural language command parsing
- **Schedule-based**: Time, sun, and event-based triggers

### Energy Monitoring
- **Consumption Tracking**: Device-level and whole-home monitoring
- **Cost Calculation**: Support for flat, TOU, and tiered pricing
- **Pattern Analysis**: Peak hours, weekday/weekend, seasonal trends
- **Anomaly Detection**: Unusual consumption, vampire power, spikes
- **Optimization**: Actionable recommendations for energy savings

### Platform Integration
- **Google Home**: Device sync, routines, voice commands
- **Amazon Alexa**: Skills, routines, device discovery
- **Apple HomeKit**: Accessory configuration, scenes, Siri integration
- **IFTTT**: Applets, webhooks, cross-service automation
- **Cross-Platform Sync**: Unified state across all platforms

---

## Plugin Structure

```
smart-home-integration-hub/
├── .claude-plugin                   # Plugin configuration
├── README.md                        # This file
├── agents/                          # Specialized agents
│   ├── device-coordinator.md        # Device management (Sonnet)
│   ├── automation-builder.md        # Automation routines (Sonnet)
│   ├── energy-monitor.md            # Energy tracking (Haiku, Fast)
│   └── integration-helper.md        # Platform integration (Haiku, Fast)
├── skills/                          # Expert knowledge
│   ├── smart-home-automation/
│   │   └── SKILL.md                 # Automation patterns & best practices
│   └── energy-management/
│       └── SKILL.md                 # Energy monitoring strategies
└── templates/                       # Configuration templates
    ├── device-registry.json         # Device database template
    ├── automation-routine.json      # Automation routine template
    ├── energy-dashboard.json        # Energy dashboard template
    └── integration-config.json      # Platform integration template
```

---

## Agents

### 1. Device Coordinator (Sonnet)

**Role**: Device management and status monitoring specialist

**Responsibilities**:
- Device discovery (network scan, platform APIs)
- Device registration and registry management
- Status dashboard generation
- Connectivity monitoring
- Anomaly detection (offline devices)

**Tools**: Read, Write, Bash, Grep, Glob

**Use Cases**:
- "Discover all devices on my network"
- "Show me the device status dashboard"
- "Register my new smart light"
- "Which devices are offline?"
- "Monitor device connectivity"

**Key Features**:
- Multi-platform device discovery (Home Assistant, network scan)
- Real-time status monitoring
- Connectivity anomaly detection
- Comprehensive device registry
- Integration with other agents

---

### 2. Automation Builder (Sonnet)

**Role**: Automation routine and scene creation specialist

**Responsibilities**:
- Create morning/evening/away routines
- Build complex conditional logic (if-then-else)
- Design multi-device scenes
- Parse voice commands to automation actions
- Validate and test automations

**Tools**: Read, Write, Bash, Grep, Glob

**Use Cases**:
- "Create a morning routine that turns on lights and starts coffee"
- "Build an away mode automation"
- "Make a movie time scene"
- "Set up motion-activated lighting"
- "Create a bedtime routine"

**Key Features**:
- Pre-built routine templates (morning, evening, away)
- Complex conditional logic support
- Scene creation and management
- Voice command integration
- Automation validation and testing

**Skills Integration**:
- Reads `smart-home-automation` skill for best practices
- Follows proven automation patterns
- Implements reliability and failover strategies

---

### 3. Energy Monitor (Haiku, Fast)

**Role**: Energy consumption tracking and optimization specialist

**Responsibilities**:
- Track device-level and whole-home energy consumption
- Calculate costs (flat rate, TOU, tiered, demand)
- Analyze usage patterns
- Detect anomalies (unusual consumption, vampire power, spikes)
- Provide optimization recommendations

**Tools**: Read, Write

**Use Cases**:
- "Show me my energy consumption for today"
- "Which devices are using the most energy?"
- "Calculate my monthly energy costs"
- "Detect any unusual energy consumption"
- "How can I reduce my energy bill?"

**Key Features**:
- Multiple cost calculation methods
- Pattern analysis (hourly, daily, seasonal)
- Statistical anomaly detection
- Optimization recommendations
- Comprehensive energy dashboards

**Skills Integration**:
- Reads `energy-management` skill for monitoring strategies
- Implements proven optimization patterns
- Follows cost calculation best practices

---

### 4. Integration Helper (Haiku, Fast)

**Role**: Multi-platform integration specialist

**Responsibilities**:
- Google Home integration setup
- Alexa skills configuration
- HomeKit accessory setup
- IFTTT applet creation
- Cross-platform synchronization

**Tools**: Read, Write

**Use Cases**:
- "Set up Google Home integration"
- "Create an Alexa routine"
- "Configure HomeKit for my devices"
- "Build an IFTTT applet for weather-based automation"
- "Sync my devices across all platforms"

**Key Features**:
- Platform-specific configuration generation
- Device compatibility checking
- Step-by-step setup instructions
- Routine/scene translation across platforms
- Cross-platform sync management

---

## Skills

### Smart Home Automation Skill

**Location**: `skills/smart-home-automation/SKILL.md`

**Content**:
- Core automation principles (reliability, user intent, graceful degradation)
- Pattern library (morning, evening, away, arrival, motion-activated)
- Conditional logic best practices (if-then-else, complex conditions)
- Scene design patterns (lighting, multi-device)
- Error handling and resilience
- Testing and validation checklists
- Performance optimization
- Security considerations
- User experience guidelines

**Used By**: automation-builder agent

---

### Energy Management Skill

**Location**: `skills/energy-management/SKILL.md`

**Content**:
- Data collection patterns (device, circuit, whole-home monitoring)
- Sampling strategies (high-frequency, standard, low-frequency)
- Cost calculation methods (flat rate, TOU, tiered, demand)
- Usage pattern analysis (baseline, peak hours, weekday/weekend, seasonal)
- Anomaly detection strategies (statistical, unusual patterns, offline devices)
- Optimization strategies (load shifting, standby elimination, HVAC, upgrades)
- Reporting and visualization
- Best practices summary

**Used By**: energy-monitor agent

---

## Templates

### 1. Device Registry Template

**File**: `templates/device-registry.json`

**Purpose**: Centralized device database

**Contains**:
- Device information (ID, name, type, manufacturer, model)
- Network details (IP, MAC, port)
- Capabilities and features
- Status and connectivity
- Metadata (power consumption, tags, zones)
- Room and zone organization

**Example Device Entry**:
```json
{
  "device_id": "living-room-lights",
  "name": "Living Room Lights",
  "type": "light",
  "manufacturer": "Philips",
  "model": "Hue White and Color A19",
  "platform": "home-assistant",
  "location": "living_room",
  "ip_address": "192.168.1.100",
  "capabilities": ["on_off", "brightness", "color_temp", "rgb_color"],
  "status": "online",
  "metadata": {
    "power_consumption_w": 9,
    "energy_monitoring_enabled": true
  }
}
```

---

### 2. Automation Routine Template

**File**: `templates/automation-routine.json`

**Purpose**: Automation routine configuration

**Contains**:
- Routine metadata (ID, name, description)
- Triggers (time, sun, state, zone, numeric, pattern)
- Conditions (state, time, numeric, sun, zone, logical operators)
- Actions (scene, device, media, wait, choose, automation, notify)
- Mode and execution settings
- Notifications configuration

**Example Automation**:
```json
{
  "routine_id": "morning-routine",
  "name": "Good Morning",
  "triggers": [
    {"type": "time", "time": "07:00", "days": ["mon", "tue", "wed", "thu", "fri"]}
  ],
  "conditions": [
    {"type": "state", "entity": "binary_sensor.anyone_home", "state": "on"}
  ],
  "actions": [
    {"type": "scene", "scene": "scene.morning_lights"},
    {"type": "device", "device_id": "thermostat-main", "action": "set_temperature", "params": {"temperature": 72}}
  ]
}
```

---

### 3. Energy Dashboard Template

**File**: `templates/energy-dashboard.json`

**Purpose**: Energy monitoring dashboard data

**Contains**:
- Summary statistics (total kWh, cost, peak power)
- Top energy consumers
- Category breakdown (heating/cooling, appliances, lighting)
- Usage patterns (peak hours, hourly distribution)
- Cost breakdown (rate tiers)
- Comparisons (yesterday, last week, baseline)
- Anomalies detected
- Optimization recommendations
- Goals and achievements

**Example Summary**:
```json
{
  "summary": {
    "total_kwh": 42.3,
    "total_cost_usd": 5.08,
    "avg_power_w": 1763,
    "peak_power_w": 4250
  },
  "top_consumers": [
    {"device_name": "HVAC", "kwh": 18.2, "percent": 43}
  ],
  "recommendations": [
    {"title": "Shift dishwasher to off-peak", "savings": "$4.50/month"}
  ]
}
```

---

### 4. Integration Configuration Template

**File**: `templates/integration-config.json`

**Purpose**: Multi-platform integration settings

**Contains**:
- Google Home configuration (OAuth, device mapping, routines)
- Alexa configuration (skill ID, endpoint, capabilities)
- HomeKit configuration (bridge, accessories, scenes)
- IFTTT configuration (webhooks, applets)
- Cross-platform sync settings
- Compatibility matrix
- Voice commands reference

**Example Platform Config**:
```json
{
  "google_home": {
    "enabled": true,
    "device_mapping": {
      "living-room-lights": {
        "type": "action.devices.types.LIGHT",
        "traits": ["OnOff", "Brightness", "ColorSetting"]
      }
    },
    "routines": [
      {"name": "Good Morning", "trigger_phrase": "Good morning"}
    ]
  }
}
```

---

## Installation

### Prerequisites

- Python 3.8+
- Claude Code CLI
- Smart home platform access (Home Assistant, Google Home, etc.)
- Network access to smart home devices

### Setup

1. **Install Plugin**:
   ```bash
   # Plugin is already in the correct location
   cd /Users/tomas.kavka/www/bandofai/puerto-issue-113/plugins/smart-home-integration-hub
   ```

2. **Verify Structure**:
   ```bash
   ls -la
   # Should show: agents/, skills/, templates/, .claude-plugin, README.md
   ```

3. **Initialize Configuration**:
   ```bash
   # Create working directory
   mkdir -p ~/.claude/smart-home/
   mkdir -p ~/.claude/smart-home/automations/
   mkdir -p ~/.claude/smart-home/energy-reports/
   mkdir -p ~/.claude/smart-home/integrations/

   # Copy templates
   cp templates/device-registry.json ~/.claude/smart-home/
   cp templates/integration-config.json ~/.claude/smart-home/integrations/
   ```

4. **Install Python Dependencies** (optional, for advanced features):
   ```bash
   pip install requests python-ifttt --break-system-packages
   ```

---

## Usage

### Quick Start

1. **Discover Devices**:
   ```
   Use the device-coordinator agent to discover devices on my network
   ```

2. **Create Morning Routine**:
   ```
   Use the automation-builder agent to create a morning routine
   ```

3. **Monitor Energy**:
   ```
   Use the energy-monitor agent to show my energy consumption
   ```

4. **Set Up Google Home**:
   ```
   Use the integration-helper agent to set up Google Home integration
   ```

### Common Workflows

#### Device Management Workflow
1. Discover devices → device-coordinator
2. Register new devices → device-coordinator
3. Generate status dashboard → device-coordinator
4. Monitor connectivity → device-coordinator

#### Automation Workflow
1. Create automation routine → automation-builder
2. Add conditional logic → automation-builder
3. Create scenes → automation-builder
4. Test automation → automation-builder
5. Deploy automation → automation-builder

#### Energy Optimization Workflow
1. Track consumption → energy-monitor
2. Analyze patterns → energy-monitor
3. Detect anomalies → energy-monitor
4. Get recommendations → energy-monitor
5. Implement optimizations → automation-builder

#### Platform Integration Workflow
1. Generate integration config → integration-helper
2. Follow setup instructions → integration-helper
3. Map devices → integration-helper
4. Create platform routines → integration-helper
5. Enable sync → integration-helper

---

## Configuration

### Device Registry Configuration

Edit `~/.claude/smart-home/device-registry.json`:

```json
{
  "home_info": {
    "name": "My Smart Home",
    "location": "Home",
    "timezone": "America/New_York"
  },
  "devices": [
    // Add your devices here
  ]
}
```

### Energy Monitoring Configuration

Create `~/.claude/smart-home/energy-config.json`:

```json
{
  "rate_per_kwh": 0.12,
  "currency": "USD",
  "time_of_use": {
    "peak": {"rate": 0.18, "hours": ["16:00-21:00"]},
    "off_peak": {"rate": 0.08, "hours": ["00:00-06:00"]},
    "standard": {"rate": 0.12, "hours": ["06:00-16:00", "21:00-24:00"]}
  }
}
```

### Integration Configuration

Edit `~/.claude/smart-home/integrations/integration-config.json`:

- Add your platform credentials
- Map devices to platform IDs
- Configure routines and scenes
- Enable cross-platform sync

---

## Examples

### Example 1: Create Morning Routine

**User**: "Create a morning routine for weekdays at 6:30 AM"

**Agent**: automation-builder

**Actions**:
1. Reads smart-home-automation skill
2. Uses morning routine pattern
3. Generates automation with:
   - Time trigger (6:30 AM, weekdays)
   - Gradual lighting scene
   - Thermostat adjustment
   - Coffee maker activation
4. Saves to `~/.claude/smart-home/automations/morning-routine.json`

---

### Example 2: Energy Consumption Analysis

**User**: "Show me my energy consumption and find ways to save money"

**Agent**: energy-monitor

**Actions**:
1. Reads energy-management skill
2. Loads energy data
3. Analyzes consumption patterns
4. Detects anomalies (vampire power, high usage)
5. Generates recommendations:
   - Shift dishwasher to off-peak ($4.50/month savings)
   - Eliminate TV standby power ($1.56/month savings)
   - Optimize HVAC schedule ($12/month savings)
6. Saves dashboard to `~/.claude/smart-home/energy-reports/`

---

### Example 3: Google Home Integration

**User**: "Set up Google Home integration for my devices"

**Agent**: integration-helper

**Actions**:
1. Loads device registry
2. Checks device compatibility
3. Generates Google Home configuration
4. Creates device mappings
5. Provides step-by-step setup instructions
6. Saves config to `~/.claude/smart-home/integrations/google-home-config.json`

---

## Best Practices

### Device Management
- Keep device registry up to date
- Use meaningful device names and tags
- Organize devices by rooms and zones
- Monitor connectivity regularly
- Document network changes

### Automation Design
- Follow the automation skill patterns
- Test automations before deploying
- Include fallback actions for critical operations
- Use conditions to prevent unwanted triggers
- Document automation logic

### Energy Monitoring
- Establish baseline before optimizing
- Monitor for at least a week before analyzing
- Consider external factors (weather, occupancy)
- Prioritize high-impact optimizations
- Track impact of changes

### Platform Integration
- Start with one platform, expand gradually
- Keep platform credentials secure
- Test cross-platform sync carefully
- Document platform-specific limitations
- Monitor sync logs for conflicts

---

## Troubleshooting

### Common Issues

**Device Not Found**:
- Check device is powered on
- Verify network connectivity
- Check IP address is correct
- Try device discovery again

**Automation Not Triggering**:
- Verify trigger conditions are met
- Check automation is enabled
- Review condition logic
- Check device availability

**Energy Data Missing**:
- Verify energy monitoring enabled on devices
- Check data collection interval
- Review device connectivity
- Validate data file exists

**Integration Sync Failed**:
- Check platform credentials
- Verify network connectivity
- Review sync logs
- Check device compatibility

---

## API Reference

### Device Registry Schema

```json
{
  "device_id": "string (required, unique)",
  "name": "string (required)",
  "type": "string (required): light|thermostat|lock|cover|sensor|camera|media_player",
  "manufacturer": "string",
  "model": "string",
  "platform": "string: home-assistant|google-home|alexa|homekit",
  "location": "string",
  "ip_address": "string (IP format)",
  "mac_address": "string (MAC format)",
  "capabilities": ["array of strings"],
  "status": "string: online|offline|unknown",
  "metadata": {
    "power_consumption_w": "number",
    "energy_monitoring_enabled": "boolean"
  }
}
```

### Automation Routine Schema

```json
{
  "routine_id": "string (required, unique)",
  "name": "string (required)",
  "enabled": "boolean",
  "triggers": [
    {
      "type": "time|sun|state|zone|numeric_state|time_pattern",
      // Type-specific parameters
    }
  ],
  "conditions": [
    {
      "type": "state|time|numeric_state|sun|zone",
      "condition": "and|or (for logical operators)",
      // Type-specific parameters
    }
  ],
  "actions": [
    {
      "type": "scene|device|media|wait_for_trigger|choose|automation|notify",
      // Type-specific parameters
    }
  ]
}
```

---

## Contributing

This plugin was created for issue #113. To extend or modify:

1. Follow the expert patterns from `subagent-creation` skill
2. Maintain single responsibility per agent
3. Use appropriate models (Haiku for templates, Sonnet for complex logic)
4. Update skills with new patterns and learnings
5. Keep templates comprehensive and well-documented

---

## License

Part of the Puerto plugin ecosystem.

---

## Support

For issues, questions, or contributions related to this plugin, please refer to issue #113 in the main Puerto repository.

---

## Changelog

### Version 1.0.0 (2025-10-21)
- Initial release
- 4 specialized agents (device-coordinator, automation-builder, energy-monitor, integration-helper)
- 2 expert skills (smart-home-automation, energy-management)
- 4 comprehensive templates
- Full documentation

---

**Built with expertise from the subagent-creation skill - Production-ready patterns for reliable smart home automation.**
