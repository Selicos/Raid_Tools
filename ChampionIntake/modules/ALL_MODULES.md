

# Champion Prompt Modules (Canonical Structure)

This file defines the canonical modules for champion prompt generation. Each module corresponds to a section in the markdown prompt template and a key in the JSON template. Use these as the authoritative reference for module file creation and intake script logic.

---


## Module 1: Base Stats

**Inputs:**
- All raw stats (HP, ATK, DEF, SPD, C.Rate, C.DMG, RES, ACC)
- If mastery damage scales with HP, use updated HP values for simulation

**Output:**
```json
"base_stats": {
  "hp": null,
  "atk": null,
  "def": null,
  "spd": null,
  "c_rate": null,
  "c_dmg": null,
  "res": null,
  "acc": null
}
```


## Module 2: Overview & Initial Summary

**Inputs:**
- Role classification
- Rarity and archetype
- Primary damage stat
- Skill scaling (A1, A2, A3)
- Recommended mastery (PvE, Clan Boss, PvP)
- Booking ROI
- Best gear sets by situation (PvE, PvP, Special)
- Gear tradeoffs (pros/cons)
- Focus stats by role
- Accuracy and resistance requirements for HARD 10 dungeons, Hydra, and Iron Twins
- Best dungeon use case based on skills, buffs/debuffs, and passive

**Output:**
```json
"overview": {
  "role": null,
  "rarity": null,
  "archetype": null,
  "primary_damage_stat": null,
  "skill_scaling": {"A1": null, "A2": null, "A3": null},
  "best_mastery": {"pve": null, "clan_boss": null, "pvp": null},
  "booking_roi": null,
  "gear_sets": {"pve": [], "pvp": [], "special": []},
  "gear_tradeoffs": [],
  "focus_stats": {"all": [], "by_role": {"pvp": [], "clan_boss": [], "hydra": [], "iron_twins": [], "dungeons": [], "solo_farming": []}},
  "accuracy_resistance": {"arena": null, "clan_boss": null, "hydra": null, "iron_twins": null, "hard_10": null},
  "best_dungeon_use": null
}
```


## Module 3: Skill Summary & Rotation Analysis

**Inputs:**
- Skill-by-skill breakdown (A1, A2, A3, Passive)
- Hit count, cooldowns (booked/unbooked), multipliers, skill type
- Passive skill impact if relevant
- Compare booked vs unbooked cooldowns and note if booking is required
- Most efficient damage rotation based on cooldowns and skill types
- Stable turn order over 6–10 turns

**Output:**
```json
"skills": {
  "a1": {"name": null, "type": null, "hit_count": null, "cooldown": {"booked": null, "unbooked": null}, "multiplier": null, "notes": null},
  "a2": {"name": null, "type": null, "hit_count": null, "cooldown": {"booked": null, "unbooked": null}, "multiplier": null, "notes": null},
  "a3": {"name": null, "type": null, "hit_count": null, "cooldown": {"booked": null, "unbooked": null}, "multiplier": null, "notes": null},
  "passive": {"exists": null, "name": null, "effect": null},
  "booking": {"impact": null, "notes": null},
  "rotation": {"optimal_cycle": [], "stable_turn_order": []}
}
```


## Module 4: Skill Book Requirements & Effects

**Inputs:**
- For each skill, list book investment and its impact
- Compare booked vs unbooked cooldowns
- Note if booking is required for optimal use

**Output:**
```json
"books": {
  "a1": {"total": null, "effects": [], "cooldown": {"booked": null, "unbooked": null}, "booking_required": null},
  "a2": {"total": null, "effects": [], "cooldown": {"booked": null, "unbooked": null}, "booking_required": null},
  "a3": {"total": null, "effects": [], "cooldown": {"booked": null, "unbooked": null}, "booking_required": null},
  "passive": {"total": null, "effects": [], "booking_required": null},
  "notes": null
}
```


## Module 5: Aura Details

**Inputs:**
- List aura stat, amount, area, and any special notes

**Output:**
```json
"aura": {
  "stat": null,
  "amount": null,
  "area": null,
  "notes": null
}
```


## Module 6: AI Behavior & Skill Logic

**Inputs:**
- Describe AI skill usage priority
- List any conditional logic for skill use

**Output:**
```json
"ai_logic": {
  "priority": [],
  "conditional_logic": []
}
```


## Module 7: Team Creator Inputs

**Inputs:**
- First turn skill
- Skill priority
- Disabled skills

**Output:**
```json
"team_inputs": {
  "first_turn_skill": null,
  "skill_priority": [],
  "disabled_skills": []
}
```


## Module 8: Mastery Proc Simulation

**Inputs:**
- Simulate mastery damage across four scenarios:
  - Single Boss
  - Boss + 10 Minions (Spider’s Den HARD)
  - Boss + 5 Minions (2 cycles/10 turns)
  - Boss + 2 High-HP Minions (2 cycles/10 turns)
- Expected bonus damage per cycle for each mastery
- Recommend best mastery per boss type

**Output:**
```json
"mastery_proc_simulation": {
  "scenarios": [
    {"type": null, "mastery": null, "bonus_damage": null, "notes": null},
    {"type": null, "mastery": null, "bonus_damage": null, "notes": null},
    {"type": null, "mastery": null, "bonus_damage": null, "notes": null},
    {"type": null, "mastery": null, "bonus_damage": null, "notes": null}
  ],
  "recommended_mastery": {"clan_boss": null, "arena": null, "doom_tower": null}
}
```


## Module 9: Mastery Recommendation

**Inputs:**
- Note only the single best mastery for this champion

**Output:**
```json
"recommended_mastery": null
```


## Module 10: Clan Boss Damage Tracking

**Inputs:**
- Damage per turn
- Compare against benchmark attackers: Ninja, Michelangelo, Geomancer, Wukong
- Estimate passive mastery triggers for benchmark champions

**Output:**
```json
"clan_boss_damage": {
  "damage_per_turn": null,
  "notes": null,
  "benchmark_comparison": [
    {"champion": "Ninja", "damage_per_turn": null, "passive_triggers": null},
    {"champion": "Michelangelo", "damage_per_turn": null, "passive_triggers": null},
    {"champion": "Geomancer", "damage_per_turn": null, "passive_triggers": null},
    {"champion": "Wukong", "damage_per_turn": null, "passive_triggers": null}
  ]
}
```


## Module 11: Dungeon/Content Breakdown

**Inputs:**
- Rate champion roles and notes for all major content
- For each, specify best use case based on skills, buffs/debuffs, and passives

**Output:**
```json
"content_breakdown": {
  "spider": {"role": null, "notes": null, "best_use_case": null},
  "dragon": {"role": null, "notes": null, "best_use_case": null},
  "fire_knight": {"role": null, "notes": null, "best_use_case": null},
  "ice_golem": {"role": null, "notes": null, "best_use_case": null},
  "doom_tower": {"role": null, "notes": null, "best_use_case": null},
  "hydra": {"role": null, "notes": null, "best_use_case": null},
  "iron_twins": {"role": null, "notes": null, "best_use_case": null},
  "sand_devil": {"role": null, "notes": null, "best_use_case": null}
}
```


## Module 12: Ally Synergy & Speed Tuning

**Inputs:**
- Recommended buffs
- Up to 3 sets of good team member champions, preferring the owned list (leave blank if unknown)
- Suggest speed tuning per boss (max 300)
- Gear/stat priorities by role
- Evaluate if Relentless/Extra Turn gear impacts mastery choice

**Output:**
```json
"synergy_speed": {
  "recommended_buffs": [],
  "support_champion_sets": [],
  "recommended_revivors": [],
  "speed_tuning": {"clan_boss": null, "arena": null, "hydra": null, "iron_twins": null},
  "gear_stat_priorities": {"pve": [], "pvp": []},
  "relentless_viability": null,
  "mastery_impact_of_gear": null
}
```


## Module 13: Utility & Investment Value

**Inputs:**
- Ask for benchmark champion list once
- Allow updates
- Rate investment value vs benchmark champions

**Output:**
```json
"utility_investment": {
  "benchmarks_used": [],
  "utility_comparison": [],
  "value": null,
  "notes": null,
  "benchmark_comparison": []
}
```


## Module 14: Turn Meter Simulation & Gear Tradeoffs

**Inputs:**
- Simulate turn meter effects and gear set stability
- Evaluate if relentless/extra turn gear changes mastery choice

**Output:**
```json
"turn_meter_gear": {
  "extra_turn_effects": null,
  "gear_set_stability": {"Reflex": null, "Relentless": null},
  "rotation_desync_risks": {"Reflex": null, "Relentless": null},
  "mastery_impact_of_gear": null
}
```


## Module 15: Final Summary

**Inputs:**
- Mastery preference across content types
- Cooldown impact
- Best mastery overall
- Stable turn order
- Passive impact
- Gear and stat notes
- Ally synergy impact
- Relentless viability
- Investment value

**Output:**
```json
"final_summary": {
  "mastery_preference": null,
  "booking_impact": null,
  "damage_rotation": null,
  "turn_meter_stability": null,
  "passive_impact": null,
  "gear_stat_notes": null,
  "ally_synergy_impact": null,
  "draft_value": null,
  "investment_value": null,
  "relentless_viability": null,
  "similar_owned_champions": [],
  "best_mastery_overall": null,
  "cooldown_impact": null,
  "stable_turn_order": []
}
```


## Module 16: Synergy Engine (Owned Champions Only)

**Inputs:**
- Provide team setups and similar champion synergy for owned champions only

**Output:**
```json
"synergy_engine": {
  "team_setups": [],
  "similar_champions": []
}
```


## Module 17: Community Ratings & Notes

**Inputs:**
- Community ratings and notes from Hellhades, Ayumilove, Reddit, etc.

**Output:**
```json
"community": {
  "hellhades": null,
  "ayumilove": null,
  "reddit": null,
  "notes": null
}
```

---

For the canonical schema and field definitions, see: `ChampionIntake/templates/Prompt_Template.json`
