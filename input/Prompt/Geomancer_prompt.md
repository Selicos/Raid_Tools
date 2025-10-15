# Champion Log Generation Prompt for Geomancer

You are to generate a complete champion log for Geomancer in JSON format, using the following template as structure and guidance. Fill in all modules (0–20) for Geomancer. Output a single JSON object with each module as a key.

---
## Template:



# Champion Prompt Template (Simplified, Oct 2025)

## 1. Base Stats
_Provide all raw stats for direct comparison and calculations. If mastery damage scales with HP, use updated HP values for simulation._
```json
{
  "base_stats": {
    "hp": <NUMBER>,
    "atk": <NUMBER>,
    "def": <NUMBER>,
    "spd": <NUMBER>,
    "c_rate": <NUMBER>,
    "c_dmg": <NUMBER>,
    "res": <NUMBER>,
    "acc": <NUMBER>
  }
}
```

## 2. Overview & Initial Summary
_Capture role, archetype, stat focus, and gear/mastery recommendations. Provide best gear sets and stat priorities for each content type (PvP, Clan Boss, Hydra, Iron Twins, Dungeons, Solo Farming). Specify accuracy/resistance for HARD 10 dungeons, Hydra, and Iron Twins. Indicate best dungeon use case based on skills, buffs/debuffs, and passive._
```json
{
  "role": "<ROLE>",
  "rarity": "<RARITY>",
  "archetype": "<ARCHETYPE>",
  "primary_damage_stat": "<ATK/HP/DEF/Hybrid/Other>",
  "skill_scaling": {"A1": "<STAT>", "A2": "<STAT>", "A3": "<STAT>"},
  "best_mastery": {"pve": "<MASTERY>", "clan_boss": "<MASTERY>", "pvp": "<MASTERY>"},
  "booking_roi": "<VALUE>",
  "gear_sets": {"pve": ["<SET>"], "pvp": ["<SET>"], "special": ["<SET>"]},
  "gear_tradeoffs": [{"set": "<SET>", "pros": "<PROS>", "cons": "<CONS>"}],
  "focus_stats": {"all": ["<STAT>"], "by_role": {"pvp": ["<STAT>"], "clan_boss": ["<STAT>"], "hydra": ["<STAT>"], "iron_twins": ["<STAT>"], "dungeons": ["<STAT>"], "solo_farming": ["<STAT>"]}},
  "accuracy_resistance": {"arena": "<VALUE>", "clan_boss": "<VALUE>", "hydra": "<VALUE>", "iron_twins": "<VALUE>", "hard_10": "<VALUE>"},
  "best_dungeon_use": "<VALUE>"
}
```

## 3. Skill Summary & Rotation Analysis
_Detail each skill, multipliers, and optimal skill cycle. For each skill, include both booked and unbooked cooldowns. Note passive impact. Output stable turn order for 6–10 turns._
```json
{
  "a1": {"name": "<NAME>", "type": "<TYPE>", "hit_count": <N>, "cooldown": {"booked": <N>, "unbooked": <N>}, "multiplier": "<MULT>", "notes": "<NOTES>"},
  "a2": {"name": "<NAME>", "type": "<TYPE>", "hit_count": <N>, "cooldown": {"booked": <N>, "unbooked": <N>}, "multiplier": "<MULT>", "notes": "<NOTES>"},
  "a3": {"name": "<NAME>", "type": "<TYPE>", "hit_count": <N>, "cooldown": {"booked": <N>, "unbooked": <N>}, "multiplier": "<MULT>", "notes": "<NOTES>"},
  "passive": {"exists": <true/false>, "name": "<NAME>", "effect": "<EFFECT>"},
  "booking": {"impact": "<IMPACT>", "notes": "<NOTES>"},
  "rotation": {"optimal_cycle": ["<SKILL>"], "stable_turn_order": ["<SKILL>"]}
}
```

## 4. Skill Book Requirements & Effects
_Quantify book investment and its impact. For each skill, include both booked and unbooked cooldowns, and whether booking is required for optimal use. Compare booked vs unbooked cooldowns._
```json
{
  "books": {
    "a1": {"total": <N>, "effects": ["<EFFECT>"], "cooldown": {"booked": <N>, "unbooked": <N>}, "booking_required": <true/false>},
    "a2": {"total": <N>, "effects": ["<EFFECT>"], "cooldown": {"booked": <N>, "unbooked": <N>}, "booking_required": <true/false>},
    "a3": {"total": <N>, "effects": ["<EFFECT>"], "cooldown": {"booked": <N>, "unbooked": <N>}, "booking_required": <true/false>},
    "passive": {"total": <N>, "effects": ["<EFFECT>"], "booking_required": <true/false>},
    "notes": "<NOTES>"
  }
}
```

## 5. Aura Details
```json
{
  "aura": {
    "stat": "<STAT>",
    "amount": <NUMBER>,
    "area": "<AREA>",
    "notes": "<NOTES>"
  }
}
```

## 6. AI Behavior & Skill Logic
```json
{
  "ai_logic": {
    "priority": ["<SKILL>", "<SKILL>", "<SKILL>"],
    "conditional_logic": ["<IF/THEN>", "<IF/THEN>"]
  }
}
```

## 7. Team Creator Inputs
```json
{
  "first_turn_skill": "<SKILL>",
  "skill_priority": ["<SKILL>"],
  "disabled_skills": ["<SKILL>"]
}
```

## 8. Mastery Proc Simulation
_Simulate mastery procs in four scenarios: (A) Single Boss, (B) Boss + 10 Minions (Spider’s Den HARD), (C) Boss + 5 Minions (2 cycles/10 turns), (D) Boss + 2 High-HP Minions (2 cycles/10 turns). For each, provide expected bonus damage per cycle for each mastery and recommend best mastery per boss type._
```json
{
  "scenarios": [
    {"type": "Single Boss", "mastery": "<MASTERY>", "bonus_damage": "<VALUE>", "notes": "<NOTES>"},
    {"type": "Boss + 10 Minions", "mastery": "<MASTERY>", "bonus_damage": "<VALUE>", "notes": "<NOTES>"},
    {"type": "Boss + 5 Minions", "mastery": "<MASTERY>", "bonus_damage": "<VALUE>", "notes": "<NOTES>"},
    {"type": "Boss + 2 High-HP Minions", "mastery": "<MASTERY>", "bonus_damage": "<VALUE>", "notes": "<NOTES>"}
  ],
  "recommended_mastery": {"clan_boss": "<MASTERY>", "arena": "<MASTERY>", "doom_tower": "<MASTERY>"}
}
```

## 9. Mastery Recommendation
_Note only the single best mastery for this champion. Full tree analysis will be handled by a separate tool._
```json
{
  "recommended_mastery": "<MASTERY>"
}
```

## 10. Clan Boss Damage Tracking
_Track and compare Clan Boss damage. Compare against benchmark attackers (e.g., Ninja, Michelangelo, Geomancer, Wukong) and estimate passive mastery triggers for benchmarks._
```json
{
  "damage_per_turn": "<VALUE>",
  "notes": "<NOTES>",
  "benchmark_comparison": [
    {"champion": "Ninja", "damage_per_turn": "<VALUE>", "passive_triggers": "<ESTIMATE>"},
    {"champion": "Michelangelo", "damage_per_turn": "<VALUE>", "passive_triggers": "<ESTIMATE>"},
    {"champion": "Geomancer", "damage_per_turn": "<VALUE>", "passive_triggers": "<ESTIMATE>"},
    {"champion": "Wukong", "damage_per_turn": "<VALUE>", "passive_triggers": "<ESTIMATE>"}
  ]
}
```

## 11. Dungeon/Content Breakdown
_Rate champion roles and notes for all major content. For each, specify best use case based on skills, buffs/debuffs, and passives._
```json
{
  "content_breakdown": {
    "spider": {"role": "<ROLE>", "notes": "<NOTES>", "best_use_case": "<VALUE>"},
    "dragon": {"role": "<ROLE>", "notes": "<NOTES>", "best_use_case": "<VALUE>"},
    "fire_knight": {"role": "<ROLE>", "notes": "<NOTES>", "best_use_case": "<VALUE>"},
    "ice_golem": {"role": "<ROLE>", "notes": "<NOTES>", "best_use_case": "<VALUE>"},
    "doom_tower": {"role": "<ROLE>", "notes": "<NOTES>", "best_use_case": "<VALUE>"},
    "hydra": {"role": "<ROLE>", "notes": "<NOTES>", "best_use_case": "<VALUE>"},
    "iron_twins": {"role": "<ROLE>", "notes": "<NOTES>", "best_use_case": "<VALUE>"},
    "sand_devil": {"role": "<ROLE>", "notes": "<NOTES>", "best_use_case": "<VALUE>"}
  }
}
```

## 12. Ally Synergy & Speed Tuning
_Recommend allies, buffs, and speed tuning. Prefer owned champions for team sets. Specify speed tuning per boss (max 300). Explicitly evaluate if Relentless/Extra Turn gear impacts mastery choice._
```json
{
  "recommended_buffs": ["<BUFF>"],
  "support_champion_sets": [["<CHAMPION>"]],
  "recommended_revivors": ["<CHAMPION>"],
  "speed_tuning": {"clan_boss": "<VALUE>", "arena": "<VALUE>", "hydra": "<VALUE>", "iron_twins": "<VALUE>"},
  "gear_stat_priorities": {"pve": ["<STAT>"], "pvp": ["<STAT>"]},
  "relentless_viability": "<VALUE>",
  "mastery_impact_of_gear": "<VALUE>"
}
```

## 13. Utility & Investment Value
_Summarize utility comparison, benchmarks, and investment value/ROI in one section._
```json
{
  "benchmarks_used": ["<CHAMPION>", ...],
  "utility_comparison": [
    {"champion": "<CHAMPION>", "role": "<ROLE>", "comparison": "<NOTES>", "investment_value_vs_benchmark": "<VALUE>"}
  ],
  "value": "<VALUE>",
  "notes": "<NOTES>",
  "benchmark_comparison": [
    {"champion": "<CHAMPION>", "investment_value": "<VALUE>"}
  ]
}
```



## 14. Turn Meter Simulation & Gear Tradeoffs
_Simulate turn meter effects and gear set stability. Evaluate if relentless/extra turn gear changes mastery choice._
```json
{
  "extra_turn_effects": "<VALUE>",
  "gear_set_stability": {"Reflex": "<VALUE>", "Relentless": "<VALUE>"},
  "rotation_desync_risks": {"Reflex": "<VALUE>", "Relentless": "<VALUE>"},
  "mastery_impact_of_gear": "<VALUE>"
}
```



## 15. Final Summary
_Recap all key findings and values. Summarize mastery preference, cooldown impact, best mastery, stable turn order, passive impact, gear/stat notes, ally synergy, relentless viability, and investment value._
```json
{
  "mastery_preference": "<VALUE>",
  "booking_impact": "<VALUE>",
  "damage_rotation": "<VALUE>",
  "turn_meter_stability": "<VALUE>",
  "passive_impact": "<VALUE>",
  "gear_stat_notes": "<VALUE>",
  "ally_synergy_impact": "<VALUE>",
  "draft_value": "<VALUE>",
  "investment_value": "<VALUE>",
  "relentless_viability": "<VALUE>",
  "similar_owned_champions": ["<CHAMPION>"],
  "best_mastery_overall": "<VALUE>",
  "cooldown_impact": "<VALUE>",
  "stable_turn_order": ["<SKILL>"]
}
```

## 16. Synergy Engine (Owned Champions Only)
_This section is generated only for champions on the owned list. Not required in every prompt._


## 17. Community Ratings & Notes
```json
{
  "community": {
    "hellhades": "<RATING>",
    "ayumilove": "<RATING>",
    "reddit": "<RATING>",
    "notes": "<NOTES>"
  }
}
```

# End of Template

---
Instructions:
- Fill in each section for Geomancer using the template above.
- Output only the final JSON object.

