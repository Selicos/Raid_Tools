
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
    "name": "Flame Eruption",
    "type": "Single Target",
    "hit_count": 1,
    "cooldown": "None",
    "multiplier": "3.8x ATK",
    "notes": "Chance to place HP Burn"
  },
  "a2": {
    "name": "Molten Rage",
    "type": "AOE",
    "hit_count": 1,
    "cooldown": "4 / 3",
    "multiplier": "4.5x ATK",
    "notes": "Places HP Burn on all enemies"
  },
  "a3": {
    "name": "Infernal Chains",
    "type": "AOE",
    "hit_count": 1,
    "cooldown": "5 / 4",
    "multiplier": "5.0x ATK",
    "notes": "Decreases DEF and applies HP Burn"
  },
  "passive": {
    "exists": true,
    "impact": "Boosts burn damage and triggers bonus effects"
  },
  "booking": {
    "impact": "High",
    "notes": "Reduces cooldowns and improves burn uptime"
  },
  "rotation": {
    "optimal_cycle": ["A3", "A2", "A1", "A1", "A2", "A1", "A3", "A1", "A2", "A1"],
    "damage_per_turn": {
      "a3": "25K–35K + burn",
      "a2": "20K–30K + burn",
      "a1": "10K–15K + burn"
    },
    "average_damage": "20K–30K per turn with burn procs",
    "buff_debuff_uptime": {
      "HP Burn": "80% uptime",
      "DEF Down": "50% uptime"
    },
    "extra_turn_frequency": "None — passive triggers only"
  }
}
