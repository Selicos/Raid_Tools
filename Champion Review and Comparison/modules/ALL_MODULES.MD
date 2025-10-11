
## Module 0: Champion Setup

**Inputs:**
- Champion name
- Ownership status: OWNED or NOTOWNED

**Goal:**
Initialize champion log and set ownership flag.

**Output:**
```json
{
  "champion": "Artak",
  "owned": true
}

### 📘 `module_1_overview.md`

```markdown
## Module 1: Overview & Initial Summary

**Inputs:**
- Champion role, archetype, gear sets, mastery, booking ROI

**Goal:**
Summarize champion identity and performance across content types.

**Output:**
```json
"overview": {
  "role": "Attack",
  "archetype": "Burn DPS / Debuff Specialist",
  "best_mastery": {
    "pve_pvp": "Helmsmasher",
    "clan_boss": "Warmaster"
  },
  "booking_roi": "High",
  "gear_sets": {
    "pvp_offense": ["Savage", "Cruel", "Perception"],
    "pvp_defense": ["Stone Skin", "Swift Parry"],
    "clan_boss": ["Reflex", "Relentless", "Accuracy"],
    "hydra": ["Reflex", "Guardian", "Perception"],
    "iron_twins": ["Perception", "Speed"],
    "dungeons": ["Savage", "Cruel", "Accuracy"],
    "solo_farming": ["Immortal", "Regen"]
  },
  "gear_tradeoffs": [
    { "set": "Reflex", "pros": "More burns", "cons": "Unpredictable cooldowns" },
    { "set": "Savage", "pros": "Max damage", "cons": "Requires high Crit Rate" },
    { "set": "Guardian", "pros": "Team sustain", "cons": "Lower personal damage" }
  ],
  "focus_stats": {
    "arena_dungeons": ["ATK%", "Crit Rate", "Crit Damage", "Accuracy"],
    "clan_boss": ["Accuracy", "Speed", "ATK%", "HP%"]
  },
  "accuracy_resistance": {
    "hard_10_dungeons": "Accuracy required for burns",
    "hydra": "High accuracy needed",
    "iron_twins": "Accuracy required"
  },
  "best_dungeon_use": "Dragon HARD 10"
}

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
  "first_turn_skill": "Infernal Chains",
  "skill_priority": ["A3", "A2", "A1"],
  "disabled_skills": []
}

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
      "type": "Single Boss",
      "mastery": "Warmaster",
      "bonus_damage": "10K–14K per proc",
      "notes": "Burn ticks stack with Warmaster procs for sustained damage"
    },
    {
      "type": "Boss + 10 Minions",
      "mastery": "Helmsmasher",
      "bonus_damage": "22K–28K per AOE hit",
      "notes": "Helmsmasher boosts AOE burn application damage"
    },
    {
      "type": "Boss + 5 Minions",
      "mastery": "Helmsmasher",
      "bonus_damage": "18K–24K per AOE hit",
      "notes": "Ideal for Dragon and Ice Golem waves"
    },
    {
      "type": "Boss + 2 High-HP Minions",
      "mastery": "Helmsmasher",
      "bonus_damage": "15K–20K per AOE hit",
      "notes": "Burns help chip down tanky adds"
    }
  ],
  "recommended_mastery": {
    "clan_boss": "Warmaster",
    "spider_hard": "Helmsmasher",
    "hydra": "Warmaster",
    "iron_twins": "Helmsmasher"
  }
}

## Module 5: Clan Boss Damage Tracking

**Inputs:**
- OWNED champion list
- Damage modeling from Module 4

**Goal:**
Evaluate Clan Boss performance and benchmark against OWNED champions.

**Output:**
```json
"clan_boss": {
  "damage_per_turn": "55K–80K",
  "benchmarks": [
    {
      "champion": "Geomancer",
      "comparison": "Superior passive damage and reflect mechanics"
    },
    {
      "champion": "Deacon Armstrong",
      "comparison": "Support role; boosts Artak’s damage via DEF Down and turn meter control"
    }
  ],
  "passive_mastery_triggers": {
    "Artak": "Burn ticks trigger passive effects and stack with Warmaster",
    "Geomancer": "Passive reflects damage and scales with enemy attacks",
    "Deacon Armstrong": "No direct damage; supports rotation and debuff uptime"
  }
}

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
  "recommended_buffs": ["Increase ATK", "Decrease DEF", "Speed Boost", "Turn Meter Fill"],
  "support_champion_sets": [
    ["Deacon Armstrong", "Geomancer"],
    [],
    []
  ],
  "speed_tuning": {
    "arena": "230–250",
    "dungeons": "200–220",
    "clan_boss": "170–190"
  },
  "gear_stat_priorities": {
    "arena": ["Savage", "Cruel", "ATK%", "Crit Rate", "Crit Damage", "Accuracy"],
    "clan_boss": ["Accuracy", "Speed", "HP%", "ATK%", "Survivability"],
    "dungeons": ["Savage", "Cruel", "Accuracy", "ATK%", "Crit Rate"]
  },
  "relentless_viability": "Moderate — can help cycle burns faster but risks cooldown desync"
}


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
  "value": "High",
  "notes": "Artak offers strong burn-based damage, reliable debuff application, and PvE versatility.",
  "owned_comparison": [
    {
      "champion": "Geomancer",
      "comparison": "Geomancer has stronger passive damage and reflect mechanics, but Artak offers more active control and wave-clear."
    },
    {
      "champion": "Deacon Armstrong",
      "comparison": "Deacon is a setup specialist with excellent turn meter control and debuff support, but lacks direct damage."
    }
  ]
}

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
    "Geomancer": 7.5,
    "Deacon Armstrong": 9.0
  },
  "draft_logic": {
    "early_pick": true,
    "counter_pick": false,
    "avoid": false,
    "notes": "Artak is a strong early pick in PvE and PvP due to burn setup and AOE damage."
  }
}

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
  "extra_turn_effects": "None — passive only",
  "gear_set_stability": {
    "Reflex": "Unstable — risks cooldown desync",
    "Relentless": "Moderate — can improve burn uptime if tuned",
    "Savage": "Stable — no turn manipulation"
  },
  "rotation_desync_risks": {
    "Reflex": "High",
    "Relentless": "Medium",
    "Savage": "Low"
  }
}

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
    "champion": "Geomancer",
    "role": "Passive DPS",
    "comparison": "Strong passive damage and reflect mechanics; excels in Clan Boss and Hydra"
  },
  {
    "champion": "Deacon Armstrong",
    "role": "Support Controller",
    "comparison": "Turn meter boost, DEF Down, and speed tuning; ideal for Arena and setup roles"
  }
]

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
  "pvp": "A",
  "clan_boss": "A-",
  "hydra": "B+",
  "iron_twins": "B",
  "dungeons": "A",
  "solo_farming": "B",
  "relentless_viability": "Moderate"
}

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
  "mastery_preference": "Helmsmasher (PvE/PvP), Warmaster (Clan Boss), Giant Slayer (Clan Boss)",
  "booking_impact": "High — improves cooldowns and burn uptime",
  "damage_rotation": "A3 → A2 → A1 cycle with 80% burn uptime",
  "turn_meter_stability": "Stable with Savage; moderate risk with Reflex",
  "passive_impact": "Burn amplification and bonus effects",
  "gear_stat_notes": "Accuracy, ATK%, Crit Rate, Speed",
  "ally_synergy_impact": "Strong with Deacon Armstrong and Geomancer",
  "draft_value": "Early pick in PvE and Arena",
  "investment_value": "High — versatile and scalable",
  "relentless_viability": "Moderate — viable with tuning",
  "similar_owned_champions": ["Geomancer", "Deacon Armstrong"]
}

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
      "name": "Arena Nuking Team",
      "champions": ["Artak", "Deacon Armstrong"],
      "strategy": "Deacon opens with TM boost and DEF Down → Artak follows with AOE burn"
    },
    {
      "name": "Clan Boss Hybrid Team",
      "champions": ["Geomancer", "Artak", "Deacon Armstrong"],
      "strategy": "Geomancer handles passive damage, Artak adds burst, Deacon maintains rotation"
    },
    {
      "name": "Hydra Control Setup",
      "champions": ["Geomancer", "Deacon Armstrong", "Artak"],
      "strategy": "Use Artak for wave-clear; rely on Geomancer for boss damage"
    }
  ],
  "similar_champions": [
    {
      "champion": "Geomancer",
      "similarity_reason": "Passive damage, PvE boss utility"
    },
    {
      "champion": "Deacon Armstrong",
      "similarity_reason": "Setup specialist, strong synergy"
    }
  ]
}
