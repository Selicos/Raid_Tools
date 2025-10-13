# Champion Log Generation Prompt for Alice the Wanderer

---
## Module 0: Champion Setup

**Inputs:**
- Champion name: Alice the Wanderer
- Ownership status: OWNED

**Goal:**
Initialize champion log and set ownership flag.

**Output:**
```json
{
  "champion": "Alice the Wanderer",
  "owned": true
}
```

---
## Module 1: Overview & Initial Summary

**Inputs:**
- Champion role: Support/HP Control
- Archetype: Turn Meter Manipulator / Debuff Specialist
- Gear sets: Relentless, Speed, Perception, Accuracy
- Mastery: Eagle Eye (PvE/PvP), Warmaster (Clan Boss)
- Booking ROI: High

### Primary Damage Stat
- [ ] ATK
- [x] HP
- [ ] DEF
- [ ] Hybrid (specify: None)
- [ ] Other (specify: None)

**Skill Scaling Details:**
- A1: HP
- A2: HP
- A3: HP

**Output:**
```json
"overview": {
  "role": "Support/HP Control",
  "rarity": "Legendary",
  "archetype": "Turn Meter Manipulator / Debuff Specialist",
  "primary_damage_stat": "HP",
  "skill_scaling": {
    "A1": "HP",
    "A2": "HP",
    "A3": "HP"
  },
  "best_mastery": {
    "pve_pvp": "Eagle Eye",
    "clan_boss": "Warmaster"
  },
  "booking_roi": "High",
  "gear_sets": {
    "pvp_offense": ["Relentless", "Speed"],
    "pvp_defense": ["Perception"],
    "clan_boss": ["Relentless", "Immortal"],
    "hydra": ["Relentless", "Speed"],
    "iron_twins": ["Perception", "Speed"],
    "dungeons": ["Speed", "Accuracy"],
    "solo_farming": ["Relentless", "Immortal"]
  },
  "gear_tradeoffs": [
    { "set": "Relentless", "pros": "Extra turns, more debuffs", "cons": "Unreliable, can desync rotation" }
  ],
  "focus_stats": {
    "arena_dungeons": ["HP", "Speed", "Accuracy"],
    "clan_boss": ["HP", "Speed", "Accuracy"]
  },
  "accuracy_resistance": {
    "hard_10_dungeons": "350+",
    "hydra": "400+",
    "iron_twins": "500+"
  },
  "best_dungeon_use": "Spider, Fire Knight"
}
```

---
## Module 2: Skill Summary & Rotation Analysis

**Inputs:**
- Skill names, cooldowns, multipliers, effects

**Output:**
```json
"skills": {
  "a1": {
    "name": "Wanderer's Touch",
    "type": "Single Target",
    "hit_count": 1,
    "cooldown": "None",
    "multiplier": "0.18x HP",
    "notes": "Attacks 1 enemy. 50% chance to place Decrease Speed for 2 turns."
  },
  "a2": {
    "name": "Path of Mists",
    "type": "AOE",
    "hit_count": 1,
    "cooldown": "3 turns",
    "multiplier": "0.22x HP",
    "notes": "Attacks all enemies. 75% chance to place Decrease Turn Meter by 20%."
  },
  "a3": {
    "name": "Lost in the Wilds",
    "type": "AOE",
    "hit_count": 1,
    "cooldown": "5 turns",
    "multiplier": "0.25x HP",
    "notes": "Attacks all enemies. Places Block Buffs for 2 turns. Heals all allies by 10% of this Champion's HP."
  },
  "passive": {
    "exists": true,
    "impact": "Whenever an enemy's Turn Meter is reduced, fills this Champion's Turn Meter by 5%."
  },
  "booking": {
    "impact": "High",
    "notes": "Books reduce cooldowns and increase debuff chances."
  },
  "rotation": {
    "optimal_cycle": ["A3", "A2", "A1", "A2", "A1", "A2", "A1", "A2", "A1", "A2"],
    "damage_per_turn": {
      "a3": "~12,000",
      "a2": "~9,000",
      "a1": "~7,000"
    },
    "average_damage": "~9,000",
    "buff_debuff_uptime": {
      "HP Burn": "0%",
      "DEF Down": "0%",
      "Block Buffs": "80%"
    },
    "extra_turn_frequency": "Relentless set can grant extra turns ~10% of the time."
  }
}
```

---
## Module 3: Team Creator Inputs

**Output:**
```json
"team_inputs": {
  "first_turn_skill": "Lost in the Wilds",
  "skill_priority": ["A3", "A2", "A1"],
  "disabled_skills": []
}
```

---
## Module 4: Mastery Proc Simulation

**Output:**
```json
"mastery_simulation": {
  "scenarios": [
    {
      "type": "Clan Boss",
      "mastery": "Warmaster",
      "bonus_damage": "~15,000 per proc",
      "notes": "Procs on A2/A3 for high value."
    },
    {
      "type": "Hydra",
      "mastery": "Eagle Eye",
      "bonus_damage": "~10,000 per proc",
      "notes": "Focus on accuracy for debuffs."
    }
  ],
  "recommended_mastery": {
    "clan_boss": "Warmaster",
    "spider_hard": "Eagle Eye",
    "hydra": "Eagle Eye",
    "iron_twins": "Eagle Eye"
  }
}
```

---
## Module 5: Clan Boss Damage Tracking

**Output:**
```json
"clan_boss": {
  "damage_per_turn": "~18,000",
  "notes": "Best in support role, not primary damage dealer."
}
```

---
## Module 6: Ally Synergy & Speed Tuning

**Output:**
```json
"synergy": {
  "recommended_buffs": ["Increase Speed", "Block Debuffs"],
  "support_champion_sets": [
    ["Arbiter", "Duchess Lilitu"],
    ["Krisk", "Uugo"]
  ],
  "recommended_revivors": ["Arbiter", "Duchess Lilitu"],
  "speed_tuning": {
    "arena": "250-300",
    "dungeons": "220-250",
    "clan_boss": "175-190"
  },
  "gear_stat_priorities": {
    "arena": ["Speed", "HP", "Accuracy"],
    "clan_boss": ["HP", "Speed", "Accuracy"],
    "dungeons": ["HP", "Speed", "Accuracy"]
  },
  "relentless_viability": "High for PvE, situational for PvP."
}
```

---
## Module 7: Investment Value & ROI

**Output:**
```json
"investment": {
  "value": "High",
  "notes": "Versatile support, strong in all content, especially dungeons and Hydra.",
  "owned_comparison": [
    { "champion": "Arbiter", "comparison": "Arbiter is faster, Alice offers more debuffs." },
    { "champion": "Uugo", "comparison": "Uugo is better for Hydra, Alice is more versatile." }
  ]
}
```

---
## Module 8: Intelligence Score & Draft Recommendations

**Output:**
```json
"intelligence": {
  "synergy_scores": {
    "Arbiter": 9,
    "Krisk": 8,
    "Uugo": 7
  },
  "draft_logic": {
    "early_pick": true,
    "counter_pick": false,
    "avoid": false,
    "notes": "Excellent first pick for control teams."
  }
}
```

---
## Module 9: Turn Meter Simulation & Gear Tradeoffs

**Output:**
```json
"turn_meter": {
  "extra_turn_effects": "Relentless set grants extra turns, passive grants TM boost on enemy TM reduction.",
  "gear_set_stability": {
    "Reflex": "Can desync skill rotation.",
    "Relentless": "High TM gain, but can desync.",
    "Savage": "Not recommended."
  },
  "rotation_desync_risks": {
    "Reflex": "Medium",
    "Relentless": "High",
    "Savage": "Low"
  }
}
```

---
## Module 10: Utility Comparison Champions

**Output:**
```json
"utility_comparison": [
  { "champion": "Arbiter", "role": "Speed Lead/Revive", "comparison": "Arbiter is faster, Alice has more debuffs." },
  { "champion": "Uugo", "role": "Hydra Support", "comparison": "Uugo is better for Hydra, Alice is more versatile." }
]
```

---
## Module 11: Color-Coded Ratings

**Output:**
```json
"ratings": {
  "pvp": "A",
  "clan_boss": "B+",
  "hydra": "A-",
  "iron_twins": "B",
  "dungeons": "A",
  "solo_farming": "B",
  "relentless_viability": "A"
}
```

---
## Module 12: Final Summary

**Output:**
```json
"final_summary": {
  "mastery_preference": "Eagle Eye for PvE/PvP, Warmaster for Clan Boss",
  "booking_impact": "High",
  "damage_rotation": "A3 > A2 > A1, with Relentless for extra turns",
  "turn_meter_stability": "Passive and Relentless can cause desync, but high TM gain",
  "passive_impact": "Significant TM gain on enemy TM reduction",
  "gear_stat_notes": "Prioritize HP, Speed, Accuracy",
  "ally_synergy_impact": "Works best with TM boosters and revivers",
  "draft_value": "First pick for control teams",
  "investment_value": "High",
  "relentless_viability": "High for PvE",
  "similar_owned_champions": ["Arbiter", "Uugo"]
}
```

---
## Module 13: Synergy Engine

**Output:**
```json
"synergy_engine": {
  "team_setups": [
    {
      "name": "Control Team",
      "champions": ["Alice the Wanderer", "Arbiter", "Krisk"],
      "strategy": "Maximize TM control and debuffs."
    }
  ],
  "similar_champions": [
    { "champion": "Arbiter", "similarity_reason": "Speed lead, revive, TM boost." },
    { "champion": "Uugo", "similarity_reason": "Hydra support, debuffs." }
  ]
}
```
