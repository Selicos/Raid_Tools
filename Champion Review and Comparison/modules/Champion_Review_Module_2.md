---

### 📘 `module_2_skills.md`

```markdown
## Module 2: Skill Summary & Rotation Analysis

**Inputs:**
- Skill names, cooldowns, multipliers, effects

**Goal:**
Analyze skill behavior and model 10-turn rotation.

**Output:**
```json
"skills": {
  "a1": {
    "name": "<A1 SKILL NAME>",
    "type": "<Single Target/AOE/Other>",
    "hit_count": <NUMBER>,
    "cooldown": "<COOLDOWN OR 'None'>",
    "multiplier": "<MULTIPLIER AND STAT, e.g., '0.2x HP'>",
    "notes": "<DESCRIPTION AND EFFECTS>"
  },
  "a2": {
    "name": "<A2 SKILL NAME>",
    "type": "<Single Target/AOE/Other>",
    "hit_count": <NUMBER>,
    "cooldown": "<COOLDOWN>",
    "multiplier": "<MULTIPLIER AND STAT>",
    "notes": "<DESCRIPTION AND EFFECTS>"
  },
  "a3": {
    "name": "<A3 SKILL NAME>",
    "type": "<Single Target/AOE/Other>",
    "hit_count": <NUMBER>,
    "cooldown": "<COOLDOWN>",
    "multiplier": "<MULTIPLIER AND STAT>",
    "notes": "<DESCRIPTION AND EFFECTS>"
  },
  "passive": {
    "exists": <true/false>,
    "impact": "<PASSIVE EFFECTS OR 'None'>"
  },
  "booking": {
    "impact": "<High/Medium/Low>",
    "notes": "<BOOKING EFFECTS>"
  },
  "rotation": {
    "optimal_cycle": [<LIST OF SKILLS IN ORDER>],
    "damage_per_turn": {
      "a3": "<VALUE OR DESCRIPTION>",
      "a2": "<VALUE OR DESCRIPTION>",
      "a1": "<VALUE OR DESCRIPTION>"
    },
    "average_damage": "<VALUE OR DESCRIPTION>",
    "buff_debuff_uptime": {
      "HP Burn": "<% OR DESCRIPTION>",
      "DEF Down": "<% OR DESCRIPTION>"
    },
    "extra_turn_frequency": "<DESCRIPTION OR 'None'>"
  }
}
```
