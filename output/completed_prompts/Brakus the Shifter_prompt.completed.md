{
  "champion": "Brakus the Shifter",
  "owned": true,
  "overview": {
    "role": "Single Target Nuker / Debuffer / Self-Revive",
    "rarity": "Legendary",
    "archetype": "Multi-hit Nuker / Fear / Weaken / Self-Revive",
    "primary_damage_stat": "ATK",
    "skill_scaling": {
      "A1": "ATK",
      "A2": "ATK",
      "A3": "ATK"
    },
    "best_mastery": {
      "pve_pvp": "Helmsmasher (PvP)",
      "clan_boss": "Warmaster or Giant Slayer"
    },
    "booking_roi": "High (A2/A3)",
    "gear_sets": {
      "pvp_offense": ["Savage", "Cruel", "Swift Parry", "Crit Damage"],
      "pvp_defense": ["Swift Parry", "Stoneskin"],
      "clan_boss": ["Savage", "Cruel", "Lifesteal"],
      "hydra": ["Savage", "Perception"],
      "iron_twins": ["Perception", "Speed"],
      "dungeons": ["Savage", "Cruel", "Speed"],
      "solo_farming": ["Lifesteal", "Speed"]
    },
    "gear_tradeoffs": [
      { "set": "Savage", "pros": "Ignores DEF for max nuke potential", "cons": "Lower survivability" },
      { "set": "Swift Parry", "pros": "Chance to survive and nuke after revive", "cons": "Lower damage ceiling" }
    ],
    "focus_stats": {
      "arena_dungeons": ["ATK%", "C.RATE", "C.DMG", "SPD", "ACC"],
      "clan_boss": ["ATK%", "C.RATE", "C.DMG", "SPD"]
    },
    "accuracy_resistance": {
      "hard_10_dungeons": "~220+ ACC",
      "hydra": "350+ ACC",
      "iron_twins": "350+ ACC"
    },
    "best_dungeon_use": "Fire Knight, Arena, Faction Wars"
  },
  "skills": {
    "a1": {
      "name": "Innocent Blood",
      "type": "Single Target",
      "hit_count": 1,
      "cooldown": "None",
      "multiplier": "3.75x ATK",
      "notes": "Attacks 1 enemy. Heals this Champion by 15% of the damage inflicted."
    },
    "a2": {
      "name": "Full Moon Rampage",
      "type": "Single Target (6 hits)",
      "hit_count": 6,
      "cooldown": "3 turns (booked)",
      "multiplier": "0.97x ATK per hit",
      "notes": "Attacks 1 enemy 6 times. Heals this Champion by 25% of the damage inflicted (50% if target is under [Fear] or [True Fear]). After the first hit, 75% chance of placing 25% [Weaken] for 2 turns."
    },
    "a3": {
      "name": "Hunter’s Howl",
      "type": "Buff + Single Target (3 hits)",
      "hit_count": 3,
      "cooldown": "4 turns (booked)",
      "multiplier": "2.3x ATK per hit",
      "notes": "Places 50% [Increase ATK] on all allies for 3 turns, then attacks 1 enemy 3 times. Each hit has 50% chance of placing [True Fear] for 1 turn. If [True Fear] is placed, 50% chance of placing [Fear] on 2 random enemies for 1 turn."
    },
    "passive": {
      "exists": true,
      "impact": "Passive: Damage increases by 40% when HP drops below 40%. Active: Revives this Champion with 20% HP when killed, grants an Extra Turn. (5 turn cooldown when booked)"
    },
    "booking": {
      "impact": "High (A2/A3)",
      "notes": "A2 and A3 gain significant cooldown reduction and effect chance. Passive revive cooldown also reduced."
    },
    "rotation": {
      "optimal_cycle": ["A3", "A2", "A1", "A1", "A2", "A1", "A3"],
      "damage_per_turn": {
        "a3": "High (buffs team, applies True Fear/Fear, 3-hit nuke)",
        "a2": "Very high (6-hit nuke, Weaken, self-heal)",
        "a1": "Moderate (self-heal, single target)"
      },
      "average_damage": "Very high for single target, especially under 40% HP",
      "buff_debuff_uptime": {
        "Increase ATK": "~100% with proper cycle",
        "Weaken": "~75% uptime on boss/single target"
      },
      "extra_turn_frequency": "Rare (on revive only)"
    }
  },
  "team_inputs": {
    "first_turn_skill": "Hunter’s Howl",
    "skill_priority": ["Hunter’s Howl", "Full Moon Rampage", "Innocent Blood"],
    "disabled_skills": []
  },
  "mastery_simulation": {
    "scenarios": [
      {
        "type": "Arena Nuker",
        "mastery": "Helmsmasher",
        "bonus_damage": "~20-30% more damage on nukes",
        "notes": "Procs on A2/A3 for maximum nuke potential."
      },
      {
        "type": "Clan Boss",
        "mastery": "Warmaster or Giant Slayer",
        "bonus_damage": "~8-12k per proc",
        "notes": "Procs on multi-hit A2/A3, boosting boss damage."
      }
    ],
    "recommended_mastery": {
      "clan_boss": "Warmaster or Giant Slayer",
      "dungeons": "Helmsmasher",
      "hydra": "Helmsmasher",
      "iron_twins": "Helmsmasher"
    }
  },
  "clan_boss": {
    "damage_per_turn": "High (multi-hit, Weaken, Increase ATK)",
    "notes": "Provides Weaken and Increase ATK, self-revive for extra survivability."
  },
  "synergy": {
    "recommended_buffs": ["Increase ATK", "Weaken", "True Fear", "Fear", "Revive"],
    "support_champion_sets": [
      ["Martyr", "Cardiel"],
      ["Scyl of the Drakes", "Duchess Lilitu"],
      ["Godseeker Aniri", "Arbiter"]
    ],
    "recommended_revivors": ["Scyl of the Drakes", "Godseeker Aniri", "Arbiter"],
    "speed_tuning": {
      "arena": "200-270+",
      "dungeons": "180-220+",
      "clan_boss": "170-200"
    },
    "gear_stat_priorities": {
      "arena": ["ATK%", "C.RATE", "C.DMG", "SPD", "ACC"],
      "clan_boss": ["ATK%", "C.RATE", "C.DMG", "SPD"],
      "dungeons": ["ATK%", "C.RATE", "C.DMG", "ACC"]
    },
    "relentless_viability": "Low, better in Savage/Cruel for nuking."
  },
  "investment": {
    "value": "High",
    "notes": "Top-tier single target nuker for Arena and Fire Knight. Books are a great investment for A2/A3.",
    "owned_comparison": [
      {"champion": "Martyr", "comparison": "Martyr offers DEF Down, Brakus offers Weaken and self-revive."},
      {"champion": "Cardiel", "comparison": "Cardiel offers more team support, Brakus more single target damage."}
    ]
  },
  "intelligence": {
    "synergy_scores": {
      "Martyr": 9,
      "Cardiel": 8,
      "Scyl of the Drakes": 7
    },
    "draft_logic": {
      "early_pick": true,
      "counter_pick": true,
      "avoid": false,
      "notes": "Early pick for Arena, counter-pick vs revive teams."
    }
  },
  "turn_meter": {
    "extra_turn_effects": "Rare (on revive only)",
    "gear_set_stability": {
      "Swift Parry": "Can save from death and enable revive nuke.",
      "Savage": "Best for Arena nuking.",
      "Lifesteal": "Viable for PvE sustain."
    },
    "rotation_desync_risks": {
      "Swift Parry": "Low risk, generally beneficial.",
      "Savage": "None, best for nuking.",
      "Lifesteal": "None, best for PvE."
    }
  },
  "utility_comparison": [
    {"champion": "Martyr", "role": "Debuffer/Support", "comparison": "Martyr offers DEF Down, Brakus offers Weaken and self-revive."},
    {"champion": "Cardiel", "role": "Revive/Support", "comparison": "Cardiel offers more team support, Brakus more single target damage."},
    {"champion": "Scyl of the Drakes", "role": "Revive/Control", "comparison": "Scyl offers more control, Brakus more damage."}
  ],
  "ratings": {
    "pvp": "A",
    "clan_boss": "A",
    "hydra": "B",
    "iron_twins": "B",
    "dungeons": "A",
    "solo_farming": "B",
    "relentless_viability": "C (better in Savage/Cruel)"
  },
  "final_summary": {
    "mastery_preference": "Helmsmasher for Arena, Warmaster/Giant Slayer for PvE",
    "booking_impact": "High (A2/A3)",
    "damage_rotation": "A3 for buff/debuff, A2 for 6-hit nuke, A1 for sustain",
    "turn_meter_stability": "Stable, extra turn only on revive.",
    "passive_impact": "Massive damage boost under 40% HP, self-revive for clutch plays.",
    "gear_stat_notes": "Prioritize ATK%, C.RATE, C.DMG, ACC. Savage/Cruel for Arena.",
    "ally_synergy_impact": "Excellent with Martyr, Cardiel, Scyl.",
    "draft_value": "First-pick for Arena/Fire Knight teams.",
    "investment_value": "High, books are well spent.",
    "relentless_viability": "Low, best in Savage/Cruel.",
    "similar_owned_champions": ["Martyr", "Cardiel", "Scyl of the Drakes"]
  },
  "synergy_engine": {
    "team_setups": [
      {
        "name": "Arena Nuker",
        "champions": ["Brakus the Shifter", "Martyr", "Cardiel", "Scyl of the Drakes"],
        "strategy": "Open with A3 for buffs/debuffs, A2 for single target nuke."
      },
      {
        "name": "Fire Knight Multi-Hit",
        "champions": ["Brakus the Shifter", "Martyr", "Godseeker Aniri"],
        "strategy": "Multi-hit A2/A3 for shield break, Weaken for boss damage."
      }
    ],
    "similar_champions": [
      {"champion": "Martyr", "similarity_reason": "Debuff synergy and revive."},
      {"champion": "Cardiel", "similarity_reason": "Revive and support."},
      {"champion": "Scyl of the Drakes", "similarity_reason": "Revive and control."}
    ]
  }
}
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


