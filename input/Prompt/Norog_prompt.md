# Champion Log Generation Prompt for Norog

You are to generate a complete champion log for Norog in JSON format, using the following module templates as structure and guidance. Each module (0–13) is included below. For each, fill in the relevant information for Norog. Output a single JSON object with each module as a key (e.g., "overview", "skills", "synergy", etc.).

---
## Example output structure:
```json
{
  "champion": "Norog",
  "owned": true,
  "overview": { ... },
  "skills": { ... },
  "team_inputs": { ... },
  "mastery_simulation": { ... },
  "clan_boss": { ... },
  "synergy": { ... },
  "investment": { ... },
  "intelligence": { ... },
  "turn_meter": { ... },
  "utility_comparison": { ... },
  "ratings": { ... },
  "final_summary": { ... },
  "synergy_engine": { ... }
}
```
---
Instructions:
- Fill in each section for Norog using the module templates below.
- Output only the final JSON object.

---
---
## Module 0
## Module 0: Champion Setup

**Inputs:**
- Champion name
- Ownership status: OWNED or NOTOWNED

**Goal:**
Initialize champion log and set ownership flag.

**Output:**
```json
{
  "champion": "<CHAMPION NAME>",
  "owned": <true/false>,
  "overview": {
    "role": "<PLACEHOLDER_ROLE>",
    "archetype": "<PLACEHOLDER_ARCHETYPE>",
    "primary_damage_stat": "<PLACEHOLDER_STAT>",
    "skill_scaling": {"A1": "<PLACEHOLDER_STAT>"},
    "best_mastery": {"pve_pvp": "<PLACEHOLDER_MASTERY>", "clan_boss": "<PLACEHOLDER_MASTERY>"},
    "booking_roi": "<PLACEHOLDER_VALUE>",
    "gear_sets": {
      "pvp_offense": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "pvp_defense": ["<PLACEHOLDER_SET>"],
      "clan_boss": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "hydra": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "iron_twins": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "dungeons": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "solo_farming": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"]
    },
    "gear_tradeoffs": [
      { "set": "<PLACEHOLDER_SET>", "pros": "<PLACEHOLDER_PROS>", "cons": "<PLACEHOLDER_CONS>" }
    ],
    "focus_stats": {
      "arena_dungeons": ["<PLACEHOLDER_STAT>", "<PLACEHOLDER_STAT>", "<PLACEHOLDER_STAT>"],
      "clan_boss": ["<PLACEHOLDER_STAT>", "<PLACEHOLDER_STAT>", "<PLACEHOLDER_STAT>"]
    },
    "accuracy_resistance": {
      "hard_10_dungeons": "<PLACEHOLDER_VALUE>",
      "hydra": "<PLACEHOLDER_VALUE>",
      "iron_twins": "<PLACEHOLDER_VALUE>"
    },
    "best_dungeon_use": "<PLACEHOLDER_DUNGEON>"
  }
}
```


---
## Module 1
---

### 📘 `module_1_overview.md`

```markdown
## Module 1: Overview & Initial Summary

**Inputs:**
- Champion role (e.g., "HP Nuker", "DEF Support", etc.)
- Archetype (e.g., "Burn DPS / Debuff Specialist")
- Gear sets (list best sets for each content type)
- Mastery (best mastery for each content type)
- Booking ROI (High/Medium/Low)

### Primary Damage Stat
- [ ] ATK
- [ ] HP
- [ ] DEF
- [ ] Hybrid (specify: __________)
- [ ] Other (specify: __________)

**Skill Scaling Details:**  
List each skill by name and the stat(s) it scales from (e.g., "A1: HP", "A2: DEF", etc.).

**Output:**
```json
"overview": {
  "role": "<REAL ROLE HERE>",
  "rarity": "<REAL RARITY>",
  "archetype": "<REAL ARCHETYPE HERE>",
  "primary_damage_stat": "<ATK/HP/DEF/Hybrid/Other>",
  "skill_scaling": {
    "A1": "<ATK/HP/DEF/Hybrid/Other>",
    "A2": "<ATK/HP/DEF/Hybrid/Other>",
    "A3": "<ATK/HP/DEF/Hybrid/Other>"
  },
  "best_mastery": {
    "pve_pvp": "<REAL MASTERY>",
    "clan_boss": "<REAL MASTERY>"
  },
  "booking_roi": "<REAL VALUE>",
  "gear_sets": {
    "pvp_offense": [ ... ],
    "pvp_defense": [ ... ],
    "clan_boss": [ ... ],
    "hydra": [ ... ],
    "iron_twins": [ ... ],
    "dungeons": [ ... ],
    "solo_farming": [ ... ]
  },
  "gear_tradeoffs": [
    { "set": "<SET>", "pros": "<PROS>", "cons": "<CONS>" }
  ],
  "focus_stats": {
    "arena_dungeons": [ ... ],
    "clan_boss": [ ... ]
  },
  "accuracy_resistance": {
    "hard_10_dungeons": "<REAL VALUE>",
    "hydra": "<REAL VALUE>",
    "iron_twins": "<REAL VALUE>"
  },
  "best_dungeon_use": "<REAL VALUE>"
}
```


---
## Module 2
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


---
## Module 3
---

### 📘 `module_3_team_inputs.md`

```markdown
## Module 3: Team Creator Inputs

**Inputs:**
- Skill priority logic from Module 2

**Goal:**
Define first-turn skill and priority order.

**Output:**
```json
"team_inputs": {
  "first_turn_skill": "<SKILL NAME>",
  "skill_priority": ["<SKILL_1>", "<SKILL_2>", "<SKILL_3>"],
  "disabled_skills": ["<SKILL_NAME_IF_ANY>"]
}
```


---
## Module 4
---

### 📘 `module_4_mastery_simulation.md`

```markdown
## Module 4: Mastery Proc Simulation

**Inputs:**
- Skill rotation and multipliers from Module 2

**Goal:**
Simulate Warmaster and Helmsmasher damage across 4 battle scenarios.

**Output:**
```json
"mastery_simulation": {
  "scenarios": [
    {
      "type": "<SCENARIO TYPE>",
      "mastery": "<MASTERY NAME>",
      "bonus_damage": "<BONUS DAMAGE VALUE OR RANGE>",
      "notes": "<NOTES ON DAMAGE OR EFFECTS>"
    },
    {
      "type": "<SCENARIO TYPE>",
      "mastery": "<MASTERY NAME>",
      "bonus_damage": "<BONUS DAMAGE VALUE OR RANGE>",
      "notes": "<NOTES ON DAMAGE OR EFFECTS>"
    }
    // Add more scenarios as needed
  ],
  "recommended_mastery": {
    "clan_boss": "<MASTERY NAME>",
    "spider_hard": "<MASTERY NAME>",
    "hydra": "<MASTERY NAME>",
    "iron_twins": "<MASTERY NAME>"
  }
}
```
````


---
## Module 5
## Module 5: Clan Boss Damage Tracking

**Inputs:**
- OWNED champion list
- Damage modeling from Module 4

**Goal:**
Evaluate Clan Boss performance using mastery simulation and rotation modeling.

**Output:**
```json
"clan_boss": {
  "damage_per_turn": "<DAMAGE VALUE OR RANGE>",
  "notes": "<NOTES ON DAMAGE, GEAR, OR ROTATION>"
}
```


---
## Module 6
---

### 📘 `module_6_synergy.md`

```markdown
## Module 6: Ally Synergy & Speed Tuning

**Inputs:**
- OWNED champion list
- Buff needs from Modules 1 and 2

**Goal:**
Recommend allies and stat tuning based on synergy and gear priorities.

**Output:**
```json
"synergy": {
  "recommended_buffs": ["<BUFF_1>", "<BUFF_2>", "..."],
  "support_champion_sets": [
    ["<CHAMPION_1>", "<CHAMPION_2>"],
    [],
    []
  ],
  "recommended_revivors": ["<REVIVER_1>", "<REVIVER_2>"],
  "speed_tuning": {
    "arena": "<VALUE OR RANGE>",
    "dungeons": "<VALUE OR RANGE>",
    "clan_boss": "<VALUE OR RANGE>"
  },
  "gear_stat_priorities": {
    "arena": ["<STAT_1>", "<STAT_2>", "..."],
    "clan_boss": ["<STAT_1>", "<STAT_2>", "..."],
    "dungeons": ["<STAT_1>", "<STAT_2>", "..."]
  },
  "relentless_viability": "<DESCRIPTION OR VALUE>"
}
```
````


---
## Module 7
---

### 📘 `module_7_investment.md`

```markdown
## Module 7: Investment Value & ROI

**Inputs:**
- OWNED champion list
- Damage and utility data from Modules 1–6

**Goal:**
Assess long-term value and compare to similar OWNED champions.

**Output:**
```json
"investment": {
  "value": "<High/Medium/Low>",
  "notes": "<NOTES ON VALUE, VERSATILITY, ETC.>",
  "owned_comparison": [
    {
      "champion": "<CHAMPION NAME>",
      "comparison": "<COMPARISON NOTES>"
    }
    // Add more comparisons as needed
  ]
}
```


---
## Module 8
---

### 📘 `module_8_intelligence.md`

```markdown
## Module 8: Intelligence Score & Draft Recommendations

**Inputs:**
- Synergy data from Module 6
- OWNED champion list

**Goal:**
Score synergy and guide PvP drafting strategy.

**Output:**
```json
"intelligence": {
  "synergy_scores": {
    "<CHAMPION_1>": <SCORE>,
    "<CHAMPION_2>": <SCORE>
    // Add more champions as needed
  },
  "draft_logic": {
    "early_pick": <true/false>,
    "counter_pick": <true/false>,
    "avoid": <true/false>,
    "notes": "<NOTES ON DRAFT LOGIC>"
  }
}
```


---
## Module 9
---

### 📘 `module_9_turn_meter.md`

```markdown
## Module 9: Turn Meter Simulation & Gear Tradeoffs

**Inputs:**
- Skill rotation and gear sets from Modules 1–2

**Goal:**
Evaluate turn meter stability and gear impact.

**Output:**
```json
"turn_meter": {
  "extra_turn_effects": "<DESCRIPTION OR 'None'>",
  "gear_set_stability": {
    "Reflex": "<DESCRIPTION>",
    "Relentless": "<DESCRIPTION>",
    "Savage": "<DESCRIPTION>"
  },
  "rotation_desync_risks": {
    "Reflex": "<RISK LEVEL OR DESCRIPTION>",
    "Relentless": "<RISK LEVEL OR DESCRIPTION>",
    "Savage": "<RISK LEVEL OR DESCRIPTION>"
  }
}
```


---
## Module 10
## Module 10: Utility Comparison Champions

**Inputs:**
- OWNED champion list
- Role and utility tags from Modules 1 and 7

**Goal:**
Compare utility roles using OWNED champions and identify similar options.

**Output:**
```json
"utility_comparison": [
  {
    "champion": "<CHAMPION NAME>",
    "role": "<ROLE>",
    "comparison": "<COMPARISON NOTES>"
  }
  // Add more champion comparisons as needed
]
```


---
## Module 11
---

### 📘 `module_11_ratings.md`

```markdown
## Module 11: Color-Coded Ratings

**Inputs:**
- Data from Modules 1–9

**Goal:**
Rate performance across content types using color-coded tiers.

**Output:**
```json
"ratings": {
  "pvp": "<RATING>",
  "clan_boss": "<RATING>",
  "hydra": "<RATING>",
  "iron_twins": "<RATING>",
  "dungeons": "<RATING>",
  "solo_farming": "<RATING>",
  "relentless_viability": "<DESCRIPTION OR RATING>"
}
```


---
## Module 12
---

### 📘 `module_12_final_summary.md`

```markdown
## Module 12: Final Summary

**Inputs:**
- All previous log blocks

**Goal:**
Recap all findings in prioritized format.

**Output:**
```json
"final_summary": {
  "mastery_preference": "<MASTERY PREFERENCE>",
  "booking_impact": "<BOOKING IMPACT>",
  "damage_rotation": "<DAMAGE ROTATION SUMMARY>",
  "turn_meter_stability": "<TURN METER STABILITY>",
  "passive_impact": "<PASSIVE IMPACT>",
  "gear_stat_notes": "<GEAR/STAT NOTES>",
  "ally_synergy_impact": "<ALLY SYNERGY IMPACT>",
  "draft_value": "<DRAFT VALUE>",
  "investment_value": "<INVESTMENT VALUE>",
  "relentless_viability": "<RELENTLESS VIABILITY>",
  "similar_owned_champions": ["<CHAMPION_1>", "<CHAMPION_2>"]
}
```


---
## Module 13
---

### 📘 `module_13_synergy_engine.md`

```markdown
## Module 13: Synergy Engine

**Inputs:**
- `owned_champions` list
- All champion logs

**Goal:**
Build teams using only OWNED champions based on synergy and role matching.

**Output:**
```json
"synergy_engine": {
  "team_setups": [
    {
      "name": "<TEAM NAME>",
      "champions": ["<CHAMPION_1>", "<CHAMPION_2>", "..."],
      "strategy": "<TEAM STRATEGY OR NOTES>"
    }
    // Add more team setups as needed
  ],
  "similar_champions": [
    {
      "champion": "<CHAMPION NAME>",
      "similarity_reason": "<REASON FOR SIMILARITY>"
    }
    // Add more similar champions as needed
  ]
}
```


