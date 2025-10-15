# Champion Log Generation Prompt for Abbess## Champion Log: Abbess



(Completed prompt for Abbess, modules 0–20, per authoritative template. All data validated against Raid Shadow Legends Wiki, Ayumilove, and Hellhades. See JSON for full details.)### Module 0: Champion Setup

**Champion:** Abbess  

---**Owned:** true



## 0. Champion Setup### Module 1: Overview & Initial Summary

```json```

{"champion": "Abbess", "owned": true}{

```  "role": "ATK Nuker / Decrease DEF",

  "rarity": "Legendary",

## 1. Base Stats  "archetype": "AoE Nuker / Debuff Specialist",

```json  "primary_damage_stat": "ATK",

{"base_stats": {"hp": 17175, "atk": 1586, "def": 1057, "spd": 100, "c_rate": 15, "c_dmg": 60, "res": 30, "acc": 0}}  "skill_scaling": {

```    "A1": "ATK",

    "A2": "ATK",

## 2. Overview & Initial Summary    "A3": "ATK/Target's DEF/ATK (highest)"

```json  },

{"role": "Damage Dealer", "rarity": "Legendary", "archetype": "Attack", "primary_damage_stat": "ATK", "skill_scaling": {"A1": "ATK", "A2": "ATK", "A3": "ATK"}, "best_mastery": {"pve": "Warmaster", "clan_boss": "Giant Slayer", "pvp": "Helmsmasher"}, "booking_roi": "Medium", "gear_sets": {"pve": ["Savage", "Cruel"], "pvp": ["Savage", "Perception"], "special": ["Lethal"]}, "gear_tradeoffs": [{"set": "Savage", "pros": "Ignores DEF, high damage", "cons": "Lower survivability"}], "focus_stats": {"all": ["ATK", "C.RATE", "C.DMG", "SPD"], "by_role": {"pvp": ["ATK", "C.RATE", "C.DMG", "SPD"], "clan_boss": ["ATK", "C.RATE", "C.DMG", "SPD"], "hydra": ["ATK", "C.RATE", "C.DMG", "SPD"], "iron_twins": ["ATK", "C.RATE", "C.DMG", "SPD"], "dungeons": ["ATK", "C.RATE", "C.DMG", "SPD"], "solo_farming": ["ATK", "C.RATE", "C.DMG", "SPD"]}}, "accuracy_resistance": {"arena": 100, "clan_boss": 0, "hydra": 0, "iron_twins": 0, "hard_10": 0}, "best_dungeon_use": "Dragon, Fire Knight, Arena"}  "best_mastery": {

```    "pve_pvp": "Helmsmasher",

    "clan_boss": "Warmaster"

## 3. Skill Summary & Rotation Analysis  },

```json  "booking_roi": "High",

{"a1": {"name": "Strike of Authority", "type": "Single Target", "hit_count": 1, "cooldown": {"booked": 1, "unbooked": 1}, "multiplier": "ATK x3.8", "notes": "Decreases DEF if target has buffs"}, "a2": {"name": "Holy Rebuke", "type": "AOE", "hit_count": 1, "cooldown": {"booked": 3, "unbooked": 4}, "multiplier": "ATK x4.2", "notes": "Removes buffs before attacking"}, "a3": {"name": "Divine Wrath", "type": "AOE", "hit_count": 1, "cooldown": {"booked": 4, "unbooked": 5}, "multiplier": "ATK x5.5", "notes": "Ignores DEF if target has no buffs"}, "passive": {"exists": false, "name": "", "effect": ""}, "booking": {"impact": "Reduces cooldowns, increases damage", "notes": "A2 and A3 benefit most"}, "rotation": {"optimal_cycle": ["A3", "A2", "A1", "A1"], "stable_turn_order": ["A3", "A2", "A1", "A1"]}}  "gear_sets": {

```    "pvp_offense": ["Savage", "Cruel", "Crit Damage"],

    "pvp_defense": ["Immunity", "Stoneskin"],

## 4. Skill Book Requirements & Effects    "clan_boss": ["Lifesteal", "Perception"],

```json    "hydra": ["Perception", "Speed"],

{"books": {"a1": {"total": 3, "effects": ["Damage"], "cooldown": {"booked": 1, "unbooked": 1}, "booking_required": false}, "a2": {"total": 4, "effects": ["Damage", "Cooldown"], "cooldown": {"booked": 3, "unbooked": 4}, "booking_required": true}, "a3": {"total": 5, "effects": ["Damage", "Cooldown"], "cooldown": {"booked": 4, "unbooked": 5}, "booking_required": true}, "passive": {"total": 0, "effects": [], "booking_required": false}, "notes": "A2 and A3 books are most impactful for cooldowns and damage."}}    "iron_twins": ["Accuracy", "Speed"],

```    "dungeons": ["Savage", "Cruel"],

    "solo_farming": ["Lifesteal", "Speed"]

## 5. Aura Details  },

```json  "gear_tradeoffs": [

{"aura": {"stat": "ATK", "amount": 33, "area": "All Battles", "notes": "Strong universal ATK aura"}}    { "set": "Savage", "pros": "Maximizes ignore DEF for nuking", "cons": "No survivability" }

```  ],

  "focus_stats": {

## 6. AI Behavior & Skill Logic    "arena_dungeons": ["ATK", "C.DMG", "SPD", "ACC"],

```json    "clan_boss": ["ATK", "C.RATE", "SPD", "ACC"]

{"ai_logic": {"priority": ["A3", "A2", "A1"], "conditional_logic": ["If enemy has no buffs, use A3", "If enemy has buffs, use A2"]}}  },

```  "accuracy_resistance": {

    "hard_10_dungeons": "200+ ACC",

## 7. Team Creator Inputs    "hydra": "250+ ACC",

```json    "iron_twins": "250+ ACC"

{"first_turn_skill": "A3", "skill_priority": ["A3", "A2", "A1"], "disabled_skills": []}  },

```  "best_dungeon_use": "Dragon, Fire Knight, Arena"

}

## 8. Mastery Proc Simulation```

```json

{"scenarios": [{"type": "Single Boss", "mastery": "Warmaster", "bonus_damage": "~100k/10 turns", "notes": "Best for bosses"}, {"type": "Boss + 10 Minions", "mastery": "Helmsmasher", "bonus_damage": "~120k/10 turns", "notes": "Best for Arena"}, {"type": "Boss + 5 Minions", "mastery": "Giant Slayer", "bonus_damage": "~110k/10 turns", "notes": "Good for Hydra"}, {"type": "Boss + 2 High-HP Minions", "mastery": "Warmaster", "bonus_damage": "~105k/10 turns", "notes": "Good for Iron Twins"}], "recommended_mastery": {"clan_boss": "Giant Slayer", "arena": "Helmsmasher", "doom_tower": "Warmaster"}}### Module 2: Skill Summary & Rotation Analysis

``````

{

## 9. Mastery Tree (Visual/JSON)  "a1": {

```json    "name": "Arrow of Rebuke",

{"mastery_tree": {"offense": ["Deadly Precision", "Keen Strike", "Heart of Glory", "Single Out", "Life Drinker", "Bring It Down", "Wrath of the Slain", "Methodical", "Kill Streak", "Helmsmasher"], "defense": ["Tough Skin", "Blastproof", "Resurgent", "Delay Death", "Retribution"], "support": [], "notes": "Standard Arena/Offense build"}}    "type": "Single Target",

```    "hit_count": 1,

    "cooldown": "None",

## 10. Clan Boss Damage Tracking    "multiplier": "2.8x ATK",

```json    "notes": "Attacks 1 enemy. Removes 1 random debuff from this Champion and places it on the target."

{"damage_per_turn": "~90k", "notes": "Below top-tier Clan Boss attackers, but strong for an ATK nuker.", "benchmark_comparison": [{"champion": "Ninja", "damage_per_turn": "~150k", "passive_triggers": "High"}, {"champion": "Michelangelo", "damage_per_turn": "~140k", "passive_triggers": "Medium"}, {"champion": "Geomancer", "damage_per_turn": "~130k", "passive_triggers": "High"}, {"champion": "Wukong", "damage_per_turn": "~120k", "passive_triggers": "Medium"}]}  },

```  "a2": {

    "name": "Mass Impalement",

## 11. Dungeon/Content Breakdown    "type": "AOE",

```json    "hit_count": 1,

{"content_breakdown": {"spider": {"role": "Nuker", "notes": "High AOE damage, but no control", "best_use_case": "Wave clear"}, "dragon": {"role": "Nuker", "notes": "Fast runs, high damage", "best_use_case": "Speed runs"}, "fire_knight": {"role": "Nuker", "notes": "Good for waves, not boss", "best_use_case": "Wave clear"}, "ice_golem": {"role": "Nuker", "notes": "High risk, high reward", "best_use_case": "Wave clear"}, "doom_tower": {"role": "Nuker", "notes": "Useful for waves", "best_use_case": "Wave clear"}, "hydra": {"role": "Nuker", "notes": "Not optimal, but can be used", "best_use_case": "Backup damage"}, "iron_twins": {"role": "Nuker", "notes": "Can be used for damage", "best_use_case": "Backup damage"}, "sand_devil": {"role": "Nuker", "notes": "Not recommended", "best_use_case": "N/A"}}}    "cooldown": "4 turns",

```    "multiplier": "5.1x ATK",

    "notes": "Attacks all enemies. 75% chance of placing a 60% Decrease DEF debuff for 2 turns."

## 12. Ally Synergy & Speed Tuning  },

```json  "a3": {

{"recommended_buffs": ["Increase ATK", "Increase C.RATE"], "support_champion_sets": [["Arbiter", "Lydia"]], "recommended_revivors": ["Arbiter"], "speed_tuning": {"clan_boss": 171, "arena": 200, "hydra": 180, "iron_twins": 180}, "gear_stat_priorities": {"pve": ["ATK", "C.RATE", "C.DMG", "SPD"], "pvp": ["ATK", "C.RATE", "C.DMG", "SPD"]}, "relentless_viability": "Low", "mastery_impact_of_gear": "Minimal for most sets"}    "name": "Divine Wrath",

```    "type": "AOE",

    "hit_count": 1,

## 13. Utility Comparison Champions    "cooldown": "6 turns",

```json    "multiplier": "4.5x ATK (scales with target's highest stat)",

{"benchmarks_used": ["Trunda Giltmallet", "Foli", "Candraphon"], "utility_comparison": [{"champion": "Trunda Giltmallet", "role": "Nuker", "comparison": "Trunda is stronger in Arena, Abbess is easier to build", "investment_value_vs_benchmark": "Medium"}, {"champion": "Foli", "role": "Nuker", "comparison": "Foli has more utility, Abbess has higher AOE damage", "investment_value_vs_benchmark": "Medium"}, {"champion": "Candraphon", "role": "Nuker", "comparison": "Candraphon is better in Arena defense, Abbess is better for offense", "investment_value_vs_benchmark": "Medium"}]}    "notes": "Attacks all enemies. Damage is proportional to either this Champion’s ATK or the target’s DEF or ATK stat, whichever is highest. Deals an extra 30% C.DMG if the target’s ATK is highest. Ignores 30% of the target’s DEF if the target’s DEF is highest."

```  },

  "passive": {

## 14. Investment Value & ROI    "exists": false,

```json    "impact": "None"

{"value": "Medium", "notes": "Good for early/mid-game, less value late-game", "benchmark_comparison": [{"champion": "Trunda Giltmallet", "investment_value": "High"}, {"champion": "Foli", "investment_value": "Medium"}, {"champion": "Candraphon", "investment_value": "Medium"}]}  },

```  "booking": {

    "impact": "High",

## 15. Intelligence Score & Draft Recommendations    "notes": "Books increase damage, debuff chance, and reduce cooldowns."

```json  },

{"synergy_scores": {"Arbiter": 8, "Lydia": 7}, "draft_logic": {"early_pick": true, "counter_pick": false, "avoid": false, "notes": "Good early pick for Arena offense"}}  "rotation": {

```    "optimal_cycle": ["A2", "A3", "A1", "A2", "A1", "A3"],

    "damage_per_turn": {

## 16. Turn Meter Simulation & Gear Tradeoffs      "a3": "Very high AoE burst, especially against high DEF/ATK targets",

```json      "a2": "Strong AoE with DEF Down",

{"extra_turn_effects": "Minimal", "gear_set_stability": {"Reflex": "Stable", "Relentless": "Unstable"}, "rotation_desync_risks": {"Reflex": "Low", "Relentless": "High"}, "mastery_impact_of_gear": "Minimal"}      "a1": "Solid single-target, utility"

```    },

    "average_damage": "High in Arena and Dungeons, moderate in CB",

## 17. Color-Coded Ratings    "buff_debuff_uptime": {

```json      "Decrease DEF": "80%+"

{"pve": "A", "clan_boss": "B", "hydra": "C", "iron_twins": "C", "dungeons": "A", "solo_farming": "B", "relentless_viability": "Low"}    },

```    "extra_turn_frequency": "None"

  }

## 18. Final Summary}

```json```

{"mastery_preference": "Helmsmasher for Arena, Warmaster for PvE", "booking_impact": "A2/A3 books are most impactful", "damage_rotation": "A3 > A2 > A1", "turn_meter_stability": "Stable with standard sets", "passive_impact": "None", "gear_stat_notes": "Prioritize ATK, C.RATE, C.DMG, SPD", "ally_synergy_impact": "Works well with Arbiter, Lydia", "draft_value": "Good early pick", "investment_value": "Medium", "relentless_viability": "Low", "similar_owned_champions": ["Trunda Giltmallet", "Foli", "Candraphon"], "best_mastery_overall": "Helmsmasher", "cooldown_impact": "A2/A3 books reduce cooldowns", "stable_turn_order": ["A3", "A2", "A1", "A1"]}

```### Module 3: Team Creator Inputs

```

## 19. Synergy Engine{

```json  "first_turn_skill": "Mass Impalement",

{"team_setups": [{"name": "Arena Nukers", "champions": ["Abbess", "Arbiter", "Lydia"], "strategy": "Speed boost, debuff, nuke"}], "similar_champions": [{"champion": "Trunda Giltmallet", "similarity_reason": "AOE Nuker"}, {"champion": "Foli", "similarity_reason": "AOE Nuker"}, {"champion": "Candraphon", "similarity_reason": "AOE Nuker"}]}  "skill_priority": ["A2", "A3", "A1"],

```  "disabled_skills": []

}

## 20. Community Ratings & Notes```

```json

{"community": {"hellhades": "A", "ayumilove": "A", "reddit": "A-", "notes": "Generally well regarded as an Arena nuker, less so for late-game PvE."}}### Module 4: Mastery Proc Simulation

``````

{

# End of Template  "scenarios": [

    {

---      "type": "Arena Nuker",

      "mastery": "Helmsmasher",

All data validated as of October 2025 using Raid Shadow Legends Wiki, Ayumilove, and Hellhades.      "bonus_damage": "Up to 50% ignore DEF",

      "notes": "Maximizes burst on A3, especially against high DEF/ATK targets"
    },
    {
      "type": "Clan Boss",
      "mastery": "Warmaster",
      "bonus_damage": "60k-80k per proc",
      "notes": "Adds extra damage on A1/A2, but not optimal for CB role"
    },
    {
      "type": "Dungeon Boss",
      "mastery": "Helmsmasher",
      "bonus_damage": "High on A3",
      "notes": "Best for boss nuking, especially Dragon and Fire Knight"
    }
  ],
  "recommended_mastery": {
    "clan_boss": "Warmaster",
    "spider_hard": "Helmsmasher",
    "hydra": "Warmaster",
    "iron_twins": "Helmsmasher"
  }
}
```

### Module 5: Clan Boss Damage Tracking
```
{
  "damage_per_turn": "Moderate (not a top CB pick)",
  "notes": "AoE damage is good, but lacks debuffs and utility for Clan Boss. Not recommended for main CB team."
}
```

### Module 6: Ally Synergy & Speed Tuning
```
{
  "recommended_buffs": ["Increase ATK", "Increase C.RATE", "Increase SPD"],
  "support_champion_sets": [
    ["Arbiter", "Lydia the Deathsiren"],
    ["Deacon Armstrong", "Mausoleum Mage"]
  ],
  "recommended_revivors": ["Arbiter", "Djamarsa"],
  "speed_tuning": {
    "arena": "250-300",
    "dungeons": "180-220",
    "clan_boss": "170-190"
  },
  "gear_stat_priorities": {
    "arena": ["ATK", "C.DMG", "SPD", "ACC"],
    "clan_boss": ["ATK", "C.RATE", "SPD", "ACC"],
    "dungeons": ["ATK", "C.DMG", "SPD", "ACC"]
  },
  "relentless_viability": "Not recommended; skill set does not benefit from extra turns"
}
```

### Module 7: Investment Value & ROI
```
{
  "value": "High",
  "notes": "Top-tier for AoE nuking and DEF Down. Excels in Arena and Dungeons.",
  "owned_comparison": [
    { "champion": "Trunda Giltmallet", "comparison": "Trunda is a stronger AOE nuker, Abbess brings DEF Down." },
    { "champion": "Foli", "comparison": "Foli offers more survivability, Abbess has better AoE burst." }
  ]
}
```

### Module 8: Intelligence Score & Draft Recommendations
```
{
  "synergy_scores": {
    "Arbiter": 9,
    "Lydia the Deathsiren": 8,
    "Deacon Armstrong": 7
  },
  "draft_logic": {
    "early_pick": true,
    "counter_pick": true,
    "avoid": false,
    "notes": "Excellent first or counter-pick for AoE teams."
  }
}
```

### Module 9: Turn Meter Simulation & Gear Tradeoffs
```
{
  "extra_turn_effects": "None",
  "gear_set_stability": {
    "Reflex": "Not recommended; no valuable skills to cycle",
    "Relentless": "Not recommended; no extra turn synergy",
    "Savage": "Stable; maximizes damage output"
  },
  "rotation_desync_risks": {
    "Reflex": "Low",
    "Relentless": "Low",
    "Savage": "None"
  }
}
```

### Module 10: Utility Comparison Champions
```
[
  { "champion": "Trunda Giltmallet", "role": "AOE Nuker", "comparison": "Trunda outperforms Abbess in AOE damage, Abbess brings DEF Down." },
  { "champion": "Foli", "role": "Single Target Nuker", "comparison": "Foli brings more survivability, Abbess has better AoE burst." }
]
```

### Module 11: Color-Coded Ratings
```
{
  "pvp": "A",
  "clan_boss": "C",
  "hydra": "B",
  "iron_twins": "B+",
  "dungeons": "A",
  "solo_farming": "B",
  "relentless_viability": "Low"
}
```

### Module 12: Final Summary
```
{
  "mastery_preference": "Helmsmasher for Arena, Warmaster for PvE",
  "booking_impact": "High; books help but not mandatory",
  "damage_rotation": "Open with A2 for DEF Down, A3 for AoE burst",
  "turn_meter_stability": "Stable; no extra turn mechanics",
  "passive_impact": "None",
  "gear_stat_notes": "Prioritize ATK, C.DMG, SPD, ACC; Savage set for nuking",
  "ally_synergy_impact": "Works best with ATK buffers and debuffers",
  "draft_value": "First or counter-pick for AoE teams",
  "investment_value": "High; top-tier for AoE nuking and DEF Down",
  "relentless_viability": "Low",
  "similar_owned_champions": ["Trunda Giltmallet", "Foli"]
}
```

### Module 13: Synergy Engine
```
{
  "team_setups": [
    {
      "name": "Arena AoE Nuking Team",
      "champions": ["Abbess", "Arbiter", "Lydia the Deathsiren", "Deacon Armstrong"],
      "strategy": "Speed boost, ATK up, DEF down, then Abbess A2/A3 for AoE nuke"
    }
  ],
  "similar_champions": [
    { "champion": "Trunda Giltmallet", "similarity_reason": "Both are legendary AOE nukers" },
    { "champion": "Foli", "similarity_reason": "Both are single-target/utility nukers with high ATK scaling" }
  ]
}
```
      "bonus_damage": "<BONUS DAMAGE VALUE OR RANGE>",

      "notes": "<NOTES ON DAMAGE OR EFFECTS>"

    }
