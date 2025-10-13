# Champion Log Generation Prompt for Geomancer

---
## Module 0: Champion Setup

**Inputs:**
- Champion name: Geomancer
- Ownership status: OWNED

**Goal:**
Initialize champion log and set ownership flag.

**Output:**
```json
{
  "champion": "Geomancer",
  "owned": true
}
```

---
## Module 1: Overview & Initial Summary

**Inputs:**
- Champion role: HP Burn Debuffer / Damage Dealer
- Archetype: Burn DPS / Turn Meter Control
- Gear sets: Perception, Lifesteal, Speed, Accuracy
- Mastery: Warmaster (PvE/PvP, Clan Boss)
- Booking ROI: High

### Primary Damage Stat
- [x] ATK
- [ ] HP
- [ ] DEF
- [ ] Hybrid (specify: None)
- [ ] Other (specify: None)

**Skill Scaling Details:**
- A1: ATK
- A2: ATK
- A3: ATK

**Output:**
```json
"overview": {
  "role": "HP Burn Debuffer / Damage Dealer",
  "rarity": "Epic",
  "archetype": "Burn DPS / Turn Meter Control",
  "primary_damage_stat": "ATK",
  "skill_scaling": {
    "A1": "ATK",
    "A2": "ATK",
    "A3": "ATK"
  },
  "best_mastery": {
    "pve_pvp": "Warmaster",
    "clan_boss": "Warmaster"
  },
  "booking_roi": "High",
  "gear_sets": {
    "pvp_offense": ["Perception", "Accuracy"],
    "pvp_defense": ["Resilience"],
    "clan_boss": ["Lifesteal", "Perception"],
    "hydra": ["Perception", "Relentless"],
    "iron_twins": ["Perception", "Accuracy"],
    "dungeons": ["Perception", "Speed"],
    "solo_farming": ["Lifesteal", "Speed"]
  },
  "gear_tradeoffs": [
    { "set": "Perception", "pros": "Boosts accuracy and speed for debuffs.", "cons": "Lower survivability than some sets." }
  ],
  "focus_stats": {
    "arena_dungeons": ["Accuracy", "Speed", "HP"],
    "clan_boss": ["Accuracy", "HP", "DEF"]
  },
  "accuracy_resistance": {
    "hard_10_dungeons": "250+",
    "hydra": "350+",
    "iron_twins": "350+"
  },
  "best_dungeon_use": "Spider 20+ (HP Burn)"
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
    "name": "Burning Fist",
    "type": "Single Target",
    "hit_count": 1,
    "cooldown": "None",
    "multiplier": "3.5x ATK",
    "notes": "Attacks 1 enemy. 30% chance of placing HP Burn debuff for 2 turns."
  },
  "a2": {
    "name": "Creeping Petrify",
    "type": "Single Target",
    "hit_count": 1,
    "cooldown": "3 turns",
    "multiplier": "4.0x ATK",
    "notes": "Attacks 1 enemy. Transfers all debuffs from Geomancer to the target, then attacks. Reduces target's Turn Meter by 100% if under HP Burn."
  },
  "a3": {
    "name": "Quicksand Grasp",
    "type": "AOE",
    "hit_count": 1,
    "cooldown": "4 turns",
    "multiplier": "3.8x ATK",
    "notes": "Places a 25% Weaken and HP Burn debuff on all enemies for 3 turns. Passive: Whenever an enemy under HP Burn attacks an ally, reflects a portion of the damage and reduces their Turn Meter."
  },
  "passive": {
    "exists": true,
    "impact": "Reflects damage and reduces Turn Meter of enemies under HP Burn when they attack allies."
  },
  "booking": {
    "impact": "High",
    "notes": "Books reduce cooldowns and increase debuff chance."
  },
  "rotation": {
    "optimal_cycle": ["A3", "A2", "A1", "A1", "A2", "A1", "A1", "A3", "A2", "A1"],
    "damage_per_turn": {
      "a3": "~12,000",
      "a2": "~10,000",
      "a1": "~8,000"
    },
    "average_damage": "~10,000",
    "buff_debuff_uptime": {
      "HP Burn": "95%+",
      "Weaken": "90%+"
    },
    "extra_turn_frequency": "None"
  }
}
```

---
## Module 3: Team Creator Inputs

**Output:**
```json
"team_inputs": {
  "first_turn_skill": "A3",
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
      "bonus_damage": "~20,000 per proc",
      "notes": "Warmaster procs on HP Burn reflect and direct hits."
    },
    {
      "type": "Hydra",
      "mastery": "Warmaster",
      "bonus_damage": "~18,000 per proc",
      "notes": "High value due to frequent HP Burn triggers."
    }
  ],
  "recommended_mastery": {
    "clan_boss": "Warmaster",
    "spider_hard": "Warmaster",
    "hydra": "Warmaster",
    "iron_twins": "Warmaster"
  }
}
```

---
## Module 5: Clan Boss Damage Tracking

**Output:**
```json
"clan_boss": {
  "damage_per_turn": "~25,000",
  "notes": "HP Burn reflect and debuffs provide high damage and utility."
}
```

---
## Module 6: Ally Synergy & Speed Tuning

**Output:**
```json
"synergy": {
  "recommended_buffs": ["Increase DEF", "Block Debuffs"],
  "support_champion_sets": [["Duchess Lilitu", "Bad-el-Kazar"]],
  "recommended_revivors": ["Duchess Lilitu"],
  "speed_tuning": {
    "arena": "220-240",
    "dungeons": "200-220",
    "clan_boss": "171-175"
  },
  "gear_stat_priorities": {
    "arena": ["Accuracy", "Speed", "HP"],
    "clan_boss": ["Accuracy", "HP", "DEF"],
    "dungeons": ["Accuracy", "Speed", "HP"]
  },
  "relentless_viability": "Not recommended; Perception or Lifesteal preferred."
}
```

---
## Module 7: Investment Value & ROI

**Output:**
```json
"investment": {
  "value": "High",
  "notes": "Geomancer is one of the best Epic HP Burners for Clan Boss and Hydra.",
  "owned_comparison": [
    {"champion": "Aothar", "comparison": "Geomancer provides more utility and higher damage."}
  ]
}
```

---
## Module 8: Intelligence Score & Draft Recommendations

**Output:**
```json
"intelligence": {
  "synergy_scores": {
    "Duchess Lilitu": 9,
    "Bad-el-Kazar": 8
  },
  "draft_logic": {
    "early_pick": true,
    "counter_pick": false,
    "avoid": false,
    "notes": "Excellent pick for HP Burn and Turn Meter control."
  }
}
```

---
## Module 9: Turn Meter Simulation & Gear Tradeoffs

**Output:**
```json
"turn_meter": {
  "extra_turn_effects": "None",
  "gear_set_stability": {
    "Reflex": "Can help cycle A3 faster.",
    "Relentless": "Not recommended.",
    "Savage": "Not relevant for HP Burn role."
  },
  "rotation_desync_risks": {
    "Reflex": "Low risk if speed tuned.",
    "Relentless": "May cause desync; avoid.",
    "Savage": "No impact."
  }
}
```

---
## Module 10: Utility Comparison Champions

**Output:**
```json
"utility_comparison": [
  {"champion": "Aothar", "role": "HP Burn", "comparison": "Geomancer is superior for Clan Boss and Hydra."}
]
```

---
## Module 11: Color-Coded Ratings

**Output:**
```json
"ratings": {
  "pvp": "B",
  "clan_boss": "S",
  "hydra": "S",
  "iron_twins": "A",
  "dungeons": "A",
  "solo_farming": "B",
  "relentless_viability": "Not recommended"
}
```

---
## Module 12: Final Summary

**Output:**
```json
"final_summary": {
  "mastery_preference": "Warmaster for all PvE content.",
  "booking_impact": "High; books increase damage and debuff uptime.",
  "damage_rotation": "A3 > A2 > A1, maintain HP Burn and Weaken debuffs.",
  "turn_meter_stability": "Stable with proper speed tuning.",
  "passive_impact": "Reflects damage and reduces enemy Turn Meter.",
  "gear_stat_notes": "Prioritize Accuracy, Speed, HP.",
  "ally_synergy_impact": "Works best with revivers and Increase DEF buffers.",
  "draft_value": "Excellent for Clan Boss and Hydra.",
  "investment_value": "High",
  "relentless_viability": "Not recommended",
  "similar_owned_champions": ["Aothar"]
}
```

---
## Module 13: Synergy Engine

**Output:**
```json
"synergy_engine": {
  "team_setups": [
    {
      "name": "Clan Boss HP Burn",
      "champions": ["Geomancer", "Duchess Lilitu", "Bad-el-Kazar"],
      "strategy": "Maintain HP Burn and Weaken, use Increase DEF and Block Debuffs."
    }
  ],
  "similar_champions": [
    {"champion": "Aothar", "similarity_reason": "HP Burn specialist, but less utility."}
  ]
}
```
