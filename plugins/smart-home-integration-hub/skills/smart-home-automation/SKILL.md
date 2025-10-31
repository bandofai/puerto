# Smart Home Automation Skill

**Expert patterns for creating intelligent, reliable, and user-friendly smart home automations**

This skill provides battle-tested patterns, templates, and best practices for building smart home automation routines that are robust, maintainable, and deliver excellent user experience.

---

## Core Principles

### 1. Reliability First
Automations must work consistently and predictably:
- Always include fallback actions
- Handle device offline scenarios
- Implement retry logic for critical actions
- Log all automation executions
- Provide clear error messages

### 2. User Intent Over Rigid Rules
Design automations that understand context:
- Consider time of day
- Account for occupancy
- Respect user overrides
- Learn from patterns
- Adapt to seasons

### 3. Graceful Degradation
When devices fail, automations should still function:
- Continue with available devices
- Notify user of failures
- Provide manual override options
- Skip non-critical actions
- Maintain safety as priority

### 4. Clear Communication
Users should know what's happening:
- Send notifications for important events
- Provide status updates
- Confirm manual triggers
- Explain automation decisions
- Allow easy disabling

---

## Automation Pattern Library

### Morning Routine Pattern

**Purpose**: Gradually wake user and prepare home for the day

**Best Practices**:
- Start subtle, increase gradually (lights, sounds)
- Check if anyone is home before executing
- Differentiate weekday vs. weekend
- Account for vacation/away mode
- Provide manual override

**Template**:
```json
{
  "routine_id": "morning-routine",
  "name": "Good Morning",
  "enabled": true,
  "triggers": [
    {
      "type": "time",
      "time": "06:30",
      "days": ["mon", "tue", "wed", "thu", "fri"]
    },
    {
      "type": "time",
      "time": "08:00",
      "days": ["sat", "sun"]
    }
  ],
  "conditions": [
    {
      "type": "state",
      "entity": "input_boolean.guest_mode",
      "state": "off"
    },
    {
      "type": "state",
      "entity": "binary_sensor.anyone_home",
      "state": "on"
    }
  ],
  "actions": [
    {
      "type": "scene",
      "scene": "scene.wake_up_lighting",
      "delay": 0,
      "description": "Gradual lighting"
    },
    {
      "type": "device",
      "device_id": "thermostat-main",
      "action": "set_temperature",
      "params": {"temperature": 72, "mode": "heat"},
      "delay": 0,
      "fallback": {
        "action": "notify",
        "message": "Thermostat unavailable"
      }
    },
    {
      "type": "device",
      "device_id": "blinds-bedroom",
      "action": "open",
      "delay": 300,
      "optional": true
    },
    {
      "type": "device",
      "device_id": "coffee-maker",
      "action": "turn_on",
      "delay": 600,
      "optional": true
    },
    {
      "type": "media",
      "device_id": "bedroom-speaker",
      "action": "play",
      "params": {
        "source": "news_briefing",
        "volume": 25
      },
      "delay": 900,
      "optional": true
    }
  ],
  "notifications": {
    "on_start": false,
    "on_complete": false,
    "on_failure": true
  }
}
```

### Evening Routine Pattern

**Purpose**: Prepare home for evening and night

**Best Practices**:
- Trigger based on sunset or time (whichever is earlier)
- Account for whether anyone is home
- Create comfortable ambiance
- Enhance security
- Save energy

**Template**:
```json
{
  "routine_id": "evening-routine",
  "name": "Good Evening",
  "enabled": true,
  "triggers": [
    {
      "type": "sun",
      "event": "sunset",
      "offset": 1800
    },
    {
      "type": "time",
      "time": "21:00"
    }
  ],
  "trigger_mode": "first",
  "conditions": [
    {
      "type": "state",
      "entity": "binary_sensor.anyone_home",
      "state": "on"
    }
  ],
  "actions": [
    {
      "type": "scene",
      "scene": "scene.evening_ambiance",
      "description": "Warm, dim lighting"
    },
    {
      "type": "device",
      "device_id": "outdoor-lights",
      "action": "turn_on",
      "params": {"brightness": 80}
    },
    {
      "type": "device",
      "device_id": "thermostat-main",
      "action": "set_temperature",
      "params": {"temperature": 68, "mode": "auto"}
    },
    {
      "type": "device",
      "device_id": "security-system",
      "action": "arm_home"
    }
  ]
}
```

### Away Mode Pattern

**Purpose**: Secure home and conserve energy when unoccupied

**Best Practices**:
- Wait for confirmation (delay before executing)
- Turn off non-essential devices
- Enable security features
- Set thermostats to eco mode
- Optional: simulate presence

**Template**:
```json
{
  "routine_id": "away-mode",
  "name": "Away from Home",
  "enabled": true,
  "triggers": [
    {
      "type": "zone",
      "zone": "home",
      "event": "leave",
      "entity": "group.family"
    }
  ],
  "conditions": [
    {
      "type": "state",
      "entity": "group.family",
      "state": "not_home",
      "for": 300
    }
  ],
  "actions": [
    {
      "type": "scene",
      "scene": "scene.all_off",
      "exceptions": ["security-lights", "fridge"]
    },
    {
      "type": "device",
      "device_id": "thermostat-main",
      "action": "set_preset",
      "params": {"preset": "eco"}
    },
    {
      "type": "device",
      "device_id": "security-system",
      "action": "arm_away"
    },
    {
      "type": "automation",
      "automation_id": "simulate-presence",
      "action": "enable"
    }
  ],
  "notifications": {
    "on_start": true,
    "message": "Away mode activated. All systems secured."
  }
}
```

### Arrival Home Pattern

**Purpose**: Welcome user and prepare home for occupation

**Best Practices**:
- Detect arrival before entering (geofencing)
- Adjust based on time of day
- Pre-heat/cool to comfortable temperature
- Enable appropriate lighting
- Disable security if armed

**Template**:
```json
{
  "routine_id": "arrival-home",
  "name": "Welcome Home",
  "enabled": true,
  "triggers": [
    {
      "type": "zone",
      "zone": "home",
      "event": "enter",
      "entity": "group.family"
    }
  ],
  "actions": [
    {
      "type": "choose",
      "choose": [
        {
          "conditions": [
            {
              "type": "sun",
              "after": "sunset"
            }
          ],
          "sequence": [
            {
              "type": "scene",
              "scene": "scene.evening_welcome"
            }
          ]
        },
        {
          "conditions": [
            {
              "type": "sun",
              "before": "sunset"
            }
          ],
          "sequence": [
            {
              "type": "scene",
              "scene": "scene.daytime_welcome"
            }
          ]
        }
      ]
    },
    {
      "type": "device",
      "device_id": "thermostat-main",
      "action": "set_preset",
      "params": {"preset": "home"}
    },
    {
      "type": "device",
      "device_id": "security-system",
      "action": "disarm"
    },
    {
      "type": "automation",
      "automation_id": "simulate-presence",
      "action": "disable"
    }
  ]
}
```

### Motion-Activated Lighting Pattern

**Purpose**: Automatic lighting based on motion, with smart dimming

**Best Practices**:
- Only activate when dark enough
- Adjust brightness based on time
- Turn off after no motion timeout
- Don't interfere with manual control
- Consider ambient light levels

**Template**:
```json
{
  "routine_id": "motion-lighting-hallway",
  "name": "Hallway Motion Lighting",
  "enabled": true,
  "triggers": [
    {
      "type": "state",
      "entity": "binary_sensor.hallway_motion",
      "to": "on"
    }
  ],
  "conditions": [
    {
      "condition": "or",
      "conditions": [
        {
          "type": "sun",
          "after": "sunset"
        },
        {
          "type": "numeric_state",
          "entity": "sensor.hallway_brightness",
          "below": 50
        }
      ]
    },
    {
      "type": "state",
      "entity": "input_boolean.motion_lighting_enabled",
      "state": "on"
    }
  ],
  "actions": [
    {
      "type": "choose",
      "choose": [
        {
          "conditions": [
            {
              "type": "time",
              "after": "22:00"
            },
            {
              "type": "time",
              "before": "06:00"
            }
          ],
          "sequence": [
            {
              "type": "device",
              "device_id": "hallway-lights",
              "action": "turn_on",
              "params": {"brightness": 20}
            }
          ]
        }
      ],
      "default": [
        {
          "type": "device",
          "device_id": "hallway-lights",
          "action": "turn_on",
          "params": {"brightness": 100}
        }
      ]
    },
    {
      "type": "wait_for_trigger",
      "trigger": {
        "type": "state",
        "entity": "binary_sensor.hallway_motion",
        "to": "off",
        "for": 300
      }
    },
    {
      "type": "device",
      "device_id": "hallway-lights",
      "action": "turn_off"
    }
  ],
  "mode": "restart"
}
```

### Climate Control Pattern

**Purpose**: Maintain comfort while optimizing energy usage

**Best Practices**:
- Adjust based on occupancy
- Consider external temperature
- Use schedules for predictable patterns
- Respect manual overrides
- Implement eco mode when away

**Template**:
```json
{
  "routine_id": "smart-climate",
  "name": "Smart Climate Control",
  "enabled": true,
  "triggers": [
    {
      "type": "time_pattern",
      "minutes": "/30"
    },
    {
      "type": "state",
      "entity": "binary_sensor.anyone_home"
    },
    {
      "type": "numeric_state",
      "entity": "sensor.outdoor_temperature"
    }
  ],
  "actions": [
    {
      "type": "choose",
      "choose": [
        {
          "conditions": [
            {
              "type": "state",
              "entity": "binary_sensor.anyone_home",
              "state": "off"
            }
          ],
          "sequence": [
            {
              "type": "device",
              "device_id": "thermostat-main",
              "action": "set_preset",
              "params": {"preset": "eco"}
            }
          ]
        },
        {
          "conditions": [
            {
              "type": "time",
              "after": "06:00",
              "before": "22:00"
            },
            {
              "type": "state",
              "entity": "binary_sensor.anyone_home",
              "state": "on"
            }
          ],
          "sequence": [
            {
              "type": "device",
              "device_id": "thermostat-main",
              "action": "set_temperature",
              "params": {"temperature": 72}
            }
          ]
        },
        {
          "conditions": [
            {
              "type": "time",
              "after": "22:00"
            },
            {
              "type": "state",
              "entity": "binary_sensor.anyone_home",
              "state": "on"
            }
          ],
          "sequence": [
            {
              "type": "device",
              "device_id": "thermostat-main",
              "action": "set_temperature",
              "params": {"temperature": 68}
            }
          ]
        }
      ]
    }
  ]
}
```

---

## Conditional Logic Best Practices

### If-Then-Else Structure

**Use Cases**:
- Time-based variations
- Occupancy-based behavior
- Environmental conditions
- User preferences

**Example - Context-Aware Lighting**:
```json
{
  "action": {
    "type": "choose",
    "choose": [
      {
        "conditions": [
          {"type": "time", "after": "22:00", "before": "06:00"}
        ],
        "sequence": [
          {
            "type": "device",
            "device_id": "lights",
            "action": "turn_on",
            "params": {"brightness": 10, "color_temp": 2700}
          }
        ]
      },
      {
        "conditions": [
          {"type": "state", "entity": "input_select.mode", "state": "movie"}
        ],
        "sequence": [
          {
            "type": "scene",
            "scene": "scene.movie_time"
          }
        ]
      },
      {
        "conditions": [
          {"type": "state", "entity": "input_select.mode", "state": "focus"}
        ],
        "sequence": [
          {
            "type": "device",
            "device_id": "lights",
            "action": "turn_on",
            "params": {"brightness": 100, "color_temp": 5000}
          }
        ]
      }
    ],
    "default": [
      {
        "type": "device",
        "device_id": "lights",
        "action": "turn_on",
        "params": {"brightness": 80, "color_temp": 4000}
      }
    ]
  }
}
```

### Complex Conditions

**AND Logic** (all must be true):
```json
{
  "condition": "and",
  "conditions": [
    {"type": "state", "entity": "binary_sensor.anyone_home", "state": "on"},
    {"type": "time", "after": "18:00", "before": "23:00"},
    {"type": "sun", "after": "sunset"}
  ]
}
```

**OR Logic** (any can be true):
```json
{
  "condition": "or",
  "conditions": [
    {"type": "sun", "after": "sunset"},
    {"type": "numeric_state", "entity": "sensor.brightness", "below": 50}
  ]
}
```

**Nested Logic**:
```json
{
  "condition": "and",
  "conditions": [
    {"type": "state", "entity": "binary_sensor.anyone_home", "state": "on"},
    {
      "condition": "or",
      "conditions": [
        {"type": "time", "after": "22:00"},
        {"type": "state", "entity": "input_boolean.sleep_mode", "state": "on"}
      ]
    }
  ]
}
```

---

## Scene Design Patterns

### Lighting Scenes

**Relax Scene**:
```json
{
  "scene_id": "scene.relax",
  "name": "Relax",
  "entities": {
    "light.living_room_main": {
      "state": "on",
      "brightness": 40,
      "color_temp": 2700
    },
    "light.living_room_accent": {
      "state": "on",
      "brightness": 30,
      "rgb_color": [255, 147, 41]
    },
    "light.floor_lamp": {
      "state": "on",
      "brightness": 50,
      "color_temp": 2200
    }
  }
}
```

**Focus/Work Scene**:
```json
{
  "scene_id": "scene.focus",
  "name": "Focus",
  "entities": {
    "light.desk_lamp": {
      "state": "on",
      "brightness": 100,
      "color_temp": 5000
    },
    "light.overhead": {
      "state": "on",
      "brightness": 90,
      "color_temp": 4500
    },
    "media_player.speakers": {
      "state": "playing",
      "source": "focus_playlist",
      "volume": 0.3
    }
  }
}
```

### Multi-Device Scenes

**Movie Time**:
```json
{
  "scene_id": "scene.movie_time",
  "name": "Movie Time",
  "entities": {
    "light.living_room_main": {
      "state": "on",
      "brightness": 15
    },
    "light.living_room_accent": {
      "state": "off"
    },
    "cover.living_room_blinds": {
      "position": 0
    },
    "media_player.tv": {
      "state": "on",
      "source": "Netflix"
    },
    "media_player.soundbar": {
      "state": "on",
      "volume": 0.5
    },
    "climate.thermostat": {
      "temperature": 70
    }
  }
}
```

---

## Error Handling & Resilience

### Retry Logic
```json
{
  "action": {
    "type": "device",
    "device_id": "smart-lock",
    "action": "lock",
    "retry": {
      "max_attempts": 3,
      "delay_seconds": 5,
      "on_failure": {
        "type": "notify",
        "message": "Failed to lock door after 3 attempts"
      }
    }
  }
}
```

### Fallback Actions
```json
{
  "action": {
    "type": "device",
    "device_id": "primary-thermostat",
    "action": "set_temperature",
    "params": {"temperature": 72},
    "fallback": {
      "type": "device",
      "device_id": "backup-thermostat",
      "action": "set_temperature",
      "params": {"temperature": 72}
    }
  }
}
```

### Timeout Handling
```json
{
  "action": {
    "type": "wait_for_trigger",
    "trigger": {
      "type": "state",
      "entity": "binary_sensor.door",
      "to": "closed"
    },
    "timeout": 300,
    "on_timeout": {
      "type": "notify",
      "message": "Door still open after 5 minutes",
      "priority": "high"
    }
  }
}
```

---

## Testing & Validation

### Pre-Deployment Checklist
- [ ] All devices in automation exist in registry
- [ ] Trigger conditions are achievable
- [ ] Time ranges are valid
- [ ] Fallback actions defined for critical operations
- [ ] Notifications configured appropriately
- [ ] Conflicting automations identified
- [ ] Manual override method exists
- [ ] Documentation complete

### Test Scenarios
1. **Happy Path**: Automation executes perfectly
2. **Device Offline**: Primary device unavailable
3. **Multiple Triggers**: Multiple conditions met simultaneously
4. **Manual Override**: User manually changes state
5. **Edge Times**: Automation at midnight, DST changes
6. **Conflict Resolution**: Multiple automations affecting same device

---

## Performance Optimization

### Reduce Trigger Frequency
Instead of:
```json
{"type": "time_pattern", "seconds": "/10"}
```

Use:
```json
{"type": "time_pattern", "minutes": "/5"}
```

### Batch Actions
Instead of multiple small automations, combine related actions:
```json
{
  "actions": [
    {"type": "scene", "scene": "scene.morning_lights"},
    {"type": "device", "device_id": "thermostat", "action": "set_temperature"},
    {"type": "device", "device_id": "coffee", "action": "turn_on"}
  ]
}
```

### Use Scenes for Multi-Device Control
Scenes are more efficient than individual device actions.

---

## Security Considerations

### Door Lock Automations
- Never auto-unlock based on location alone
- Require additional confirmation
- Log all lock/unlock events
- Notify on unexpected state changes

### Security System Integration
- Never disarm automatically without strong confirmation
- Use multi-factor triggers (location + time + confirmation)
- Always notify on arm/disarm events
- Fail secure (armed) on errors

### Camera/Privacy
- Disable cameras when occupants home
- Clear indicators when recording
- Secure video storage
- Respect privacy zones

---

## User Experience Guidelines

### Notifications
- Use sparingly (avoid notification fatigue)
- Prioritize by importance (critical, high, normal, low)
- Make actionable when possible
- Provide context in message
- Allow user to disable per automation

### Manual Override Respect
- Don't fight user manual changes
- Pause automation for period after manual override
- Provide easy enable/disable toggles
- Document override behavior

### Gradual Changes
- Fade lights instead of instant on/off
- Gradual temperature adjustments
- Progressive volume changes
- Smooth transitions between scenes

---

## Summary

**Great automations are**:
1. **Reliable**: Work consistently, handle failures gracefully
2. **Contextual**: Adapt to time, occupancy, and conditions
3. **Non-intrusive**: Enhance life without being annoying
4. **Transparent**: Users understand what's happening
5. **Controllable**: Easy to override or disable
6. **Efficient**: Optimize energy and resources
7. **Secure**: Protect home and privacy
8. **Maintainable**: Easy to update and troubleshoot

Follow these patterns and your smart home automations will delight users and run reliably for years.
