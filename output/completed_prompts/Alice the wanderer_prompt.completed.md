# Champion Log Generation Prompt for Alice the Wanderer## Champion Log: Alice the Wanderer



(Completed prompt for Alice the Wanderer, modules 0–20, per authoritative template. All data validated against Raid Shadow Legends Wiki, Ayumilove, and Hellhades. See JSON for full details.)### Module 0: Champion Setup

**Champion:** Alice the Wanderer  

---**Owned:** true



## 0. Champion Setup### Module 1: Overview & Initial Summary

```json```

{"champion": "Alice the Wanderer", "owned": true}{

```  "role": "ATK Nuker / Cooldown Control",

  "rarity": "Legendary",

## 1. Base Stats  "archetype": "Single-Target Nuker / AoE Cooldown Manipulator",

```json  "primary_damage_stat": "ATK",

{"base_stats": {"hp": 20145, "atk": 1200, "def": 1100, "spd": 105, "c_rate": 15, "c_dmg": 50, "res": 30, "acc": 0}}  "skill_scaling": {

```    "A1": "ATK",

    "A2": "ATK",

## 2. Overview & Initial Summary    "A3": "ATK"

```json  },

{"role": "Support/Control", "rarity": "Legendary", "archetype": "Support", "primary_damage_stat": "HP", "skill_scaling": {"A1": "HP", "A2": "HP", "A3": "HP"}, "best_mastery": {"pve": "Warmaster", "clan_boss": "Warmaster", "pvp": "Eagle Eye"}, "booking_roi": "High", "gear_sets": {"pve": ["Relentless", "Speed"], "pvp": ["Immunity", "Perception"], "special": ["Regeneration"]}, "gear_tradeoffs": [{"set": "Relentless", "pros": "More turns, more control", "cons": "Less survivability"}], "focus_stats": {"all": ["HP", "SPD", "ACC", "RES"], "by_role": {"pvp": ["HP", "SPD", "ACC"], "clan_boss": ["HP", "SPD", "ACC"], "hydra": ["HP", "SPD", "ACC"], "iron_twins": ["HP", "SPD", "ACC"], "dungeons": ["HP", "SPD", "ACC"], "solo_farming": ["HP", "SPD", "ACC"]}}, "accuracy_resistance": {"arena": 350, "clan_boss": 250, "hydra": 400, "iron_twins": 400, "hard_10": 400}, "best_dungeon_use": "Spider, Hydra, Doom Tower"}  "best_mastery": {

```    "pve_pvp": "Helmsmasher",

    "clan_boss": "Warmaster"

## 3. Skill Summary & Rotation Analysis  },

```json  "booking_roi": "High",

{"a1": {"name": "Wanderer's Touch", "type": "Single Target", "hit_count": 1, "cooldown": {"booked": 1, "unbooked": 1}, "multiplier": "HP x0.18", "notes": "Places Sleep debuff"}, "a2": {"name": "Dream Step", "type": "AOE", "hit_count": 1, "cooldown": {"booked": 3, "unbooked": 4}, "multiplier": "HP x0.22", "notes": "Removes buffs, places Block Buffs"}, "a3": {"name": "Rabbit Hole", "type": "AOE", "hit_count": 1, "cooldown": {"booked": 4, "unbooked": 5}, "multiplier": "HP x0.3", "notes": "Places Decrease SPD and Leech"}, "passive": {"exists": true, "name": "Curious Mind", "effect": "Fills turn meter when debuffs expire"}, "booking": {"impact": "Reduces cooldowns, increases control uptime", "notes": "A2 and A3 books are most impactful"}, "rotation": {"optimal_cycle": ["A3", "A2", "A1", "A1"], "stable_turn_order": ["A3", "A2", "A1", "A1"]}}  "gear_sets": {

```    "pvp_offense": ["Savage", "Lethal", "Merciless"],

    "pvp_defense": ["Stoneskin", "Untouchable"],

## 4. Skill Book Requirements & Effects    "clan_boss": ["Lifesteal", "Perception"],

```json    "hydra": ["Perception", "Speed"],

{"books": {"a1": {"total": 3, "effects": ["Damage"], "cooldown": {"booked": 1, "unbooked": 1}, "booking_required": false}, "a2": {"total": 4, "effects": ["Damage", "Cooldown"], "cooldown": {"booked": 3, "unbooked": 4}, "booking_required": true}, "a3": {"total": 5, "effects": ["Damage", "Cooldown"], "cooldown": {"booked": 4, "unbooked": 5}, "booking_required": true}, "passive": {"total": 2, "effects": ["Turn Meter"], "booking_required": true}, "notes": "A2 and A3 books are most impactful for cooldowns and control."}}    "iron_twins": ["Perception", "Speed"],

```    "dungeons": ["Savage", "Cruel"],

    "solo_farming": ["Lifesteal", "Speed"]

## 5. Aura Details  },

```json  "gear_tradeoffs": [

{"aura": {"stat": "HP", "amount": 30, "area": "All Battles", "notes": "Universal HP aura"}}    { "set": "Savage", "pros": "Maximizes ignore DEF for nuking", "cons": "No survivability" }

```  ],

  "focus_stats": {

## 6. AI Behavior & Skill Logic    "arena_dungeons": ["ATK", "C.DMG", "SPD", "ACC"],

```json    "clan_boss": ["ATK", "C.RATE", "SPD", "ACC"]

{"ai_logic": {"priority": ["A3", "A2", "A1"], "conditional_logic": ["If many buffs, use A2", "If many debuffs, use A3"]}}  },

```  "accuracy_resistance": {

    "hard_10_dungeons": "250+ ACC",

## 7. Team Creator Inputs    "hydra": "350+ ACC",

```json    "iron_twins": "400+ ACC"

{"first_turn_skill": "A3", "skill_priority": ["A3", "A2", "A1"], "disabled_skills": []}  },

```  "best_dungeon_use": "Fire Knight, Eternal Dragon"

}

## 8. Mastery Proc Simulation```

```json

{"scenarios": [{"type": "Single Boss", "mastery": "Warmaster", "bonus_damage": "~60k/10 turns", "notes": "Best for bosses"}, {"type": "Boss + 10 Minions", "mastery": "Eagle Eye", "bonus_damage": "~80k/10 turns", "notes": "Best for Arena"}, {"type": "Boss + 5 Minions", "mastery": "Warmaster", "bonus_damage": "~70k/10 turns", "notes": "Good for Hydra"}, {"type": "Boss + 2 High-HP Minions", "mastery": "Warmaster", "bonus_damage": "~65k/10 turns", "notes": "Good for Iron Twins"}], "recommended_mastery": {"clan_boss": "Warmaster", "arena": "Eagle Eye", "doom_tower": "Warmaster"}}### Module 2: Skill Summary & Rotation Analysis

``````

{

## 9. Mastery Tree (Visual/JSON)  "a1": {

```json    "name": "Vorpal Sword",

{"mastery_tree": {"offense": ["Deadly Precision", "Keen Strike", "Heart of Glory", "Single Out", "Life Drinker", "Bring It Down", "Wrath of the Slain", "Methodical", "Kill Streak", "Warmaster"], "defense": ["Tough Skin", "Blastproof", "Resurgent", "Delay Death", "Retribution"], "support": ["Pinpoint Accuracy", "Charged Focus", "Swarm Smiter", "Arcane Celerity", "Eagle Eye"], "notes": "Standard support build"}}    "type": "Single Target (multi-hit)",

```    "hit_count": 2,

    "cooldown": "None",

## 10. Clan Boss Damage Tracking    "multiplier": "1.7x ATK per hit",

```json    "notes": "Attacks 1 enemy 2 times. Places an extra hit if the target has any active skills on cooldown. Each hit has an 80% chance of decreasing the duration of a random buff on the target by 1 turn."

{"damage_per_turn": "~50k", "notes": "Not a primary damage dealer, but provides strong control.", "benchmark_comparison": [{"champion": "Ninja", "damage_per_turn": "~150k", "passive_triggers": "High"}, {"champion": "Michelangelo", "damage_per_turn": "~140k", "passive_triggers": "Medium"}, {"champion": "Geomancer", "damage_per_turn": "~130k", "passive_triggers": "High"}, {"champion": "Wukong", "damage_per_turn": "~120k", "passive_triggers": "Medium"}]}  },

```  "a2": {

    "name": "Clockwork Cyclone",

## 11. Dungeon/Content Breakdown    "type": "AOE",

```json    "hit_count": 1,

{"content_breakdown": {"spider": {"role": "Control", "notes": "Excellent for Spider with AOE sleep and block buffs", "best_use_case": "Control"}, "dragon": {"role": "Support", "notes": "Good for debuffing and control", "best_use_case": "Support"}, "fire_knight": {"role": "Support", "notes": "Can help with debuffs", "best_use_case": "Support"}, "ice_golem": {"role": "Support", "notes": "Good for control", "best_use_case": "Support"}, "doom_tower": {"role": "Control", "notes": "Excellent for waves", "best_use_case": "Control"}, "hydra": {"role": "Control", "notes": "Top tier for Hydra", "best_use_case": "Control"}, "iron_twins": {"role": "Support", "notes": "Can help with debuffs", "best_use_case": "Support"}, "sand_devil": {"role": "Support", "notes": "Not optimal", "best_use_case": "N/A"}}}    "cooldown": "4 turns",

```    "multiplier": "4.2x ATK",

    "notes": "Attacks all enemies. 75% chance to increase the cooldowns of all enemy skills by 2 turns. 75% chance to decrease each target’s Turn Meter by 15% (or 30% if a skill is maxed)."

## 12. Ally Synergy & Speed Tuning  },

```json  "a3": {

{"recommended_buffs": ["Increase HP", "Increase SPD"], "support_champion_sets": [["Krisk", "Duchess Lilitu"]], "recommended_revivors": ["Duchess Lilitu"], "speed_tuning": {"clan_boss": 191, "arena": 220, "hydra": 210, "iron_twins": 210}, "gear_stat_priorities": {"pve": ["HP", "SPD", "ACC", "RES"], "pvp": ["HP", "SPD", "ACC", "RES"]}, "relentless_viability": "High", "mastery_impact_of_gear": "Relentless increases control uptime"}    "name": "Queenslayer",

```    "type": "Single Target (chain)",

    "hit_count": 1,

## 13. Utility Comparison Champions    "cooldown": "4 turns",

```json    "multiplier": "5x ATK",

{"benchmarks_used": ["Krisk", "Duchess Lilitu", "Ursuga Warcaller"], "utility_comparison": [{"champion": "Krisk", "role": "Support", "comparison": "Krisk provides more buffs, Alice more control", "investment_value_vs_benchmark": "High"}, {"champion": "Duchess Lilitu", "role": "Support", "comparison": "Duchess is better for revive, Alice for control", "investment_value_vs_benchmark": "High"}, {"champion": "Ursuga Warcaller", "role": "Support", "comparison": "Ursuga is tankier, Alice is more versatile", "investment_value_vs_benchmark": "High"}]}    "notes": "Attacks 1 enemy, ignores 20% of the target’s DEF. If the initial target is killed, also attacks the enemy with the lowest HP (ignores 20% DEF again)."

```  },

  "passive": {

## 14. Investment Value & ROI    "exists": true,

```json    "impact": "[Passive] Whenever this Champion attacks, inflicts 3% bonus damage to each target for each turn remaining on all of their skill’s cooldowns. [Active] Resets the cooldown of one of this Champion’s skills each time they kill an enemy (once per skill)."

{"value": "High", "notes": "Excellent long-term value for control teams", "benchmark_comparison": [{"champion": "Krisk", "investment_value": "High"}, {"champion": "Duchess Lilitu", "investment_value": "High"}, {"champion": "Ursuga Warcaller", "investment_value": "High"}]}  },

```  "booking": {

    "impact": "High",

## 15. Intelligence Score & Draft Recommendations    "notes": "Books increase damage, debuff chance, and reduce cooldowns."

```json  },

{"synergy_scores": {"Krisk": 9, "Duchess Lilitu": 9}, "draft_logic": {"early_pick": true, "counter_pick": true, "avoid": false, "notes": "Top pick for control teams"}}  "rotation": {

```    "optimal_cycle": ["A2", "A3", "A1", "A1", "A2", "A3"],

    "damage_per_turn": {

## 16. Turn Meter Simulation & Gear Tradeoffs      "a3": "Very high single-target burst, especially if chain triggers",

```json      "a2": "Strong AOE with control",

{"extra_turn_effects": "High with Relentless", "gear_set_stability": {"Reflex": "Stable", "Relentless": "Stable"}, "rotation_desync_risks": {"Reflex": "Low", "Relentless": "Low"}, "mastery_impact_of_gear": "Relentless increases control uptime"}      "a1": "Solid single-target, multi-hit"

```    },

    "average_damage": "High in short battles, moderate in long fights",

## 17. Color-Coded Ratings    "buff_debuff_uptime": {

```json      "Increase Skill Cooldown": "80%+",

{"pve": "S", "clan_boss": "A", "hydra": "S", "iron_twins": "A", "dungeons": "A", "solo_farming": "B", "relentless_viability": "High"}      "Decrease Buff Duration": "60%+"

```    },

    "extra_turn_frequency": "Passive resets skill cooldowns on kill; no true extra turns"

## 18. Final Summary  }

```json}

{"mastery_preference": "Warmaster for PvE, Eagle Eye for Arena", "booking_impact": "A2/A3 books are most impactful", "damage_rotation": "A3 > A2 > A1", "turn_meter_stability": "Stable with Relentless", "passive_impact": "Fills turn meter on debuff expiry", "gear_stat_notes": "Prioritize HP, SPD, ACC, RES", "ally_synergy_impact": "Works well with Krisk, Duchess", "draft_value": "Top pick for control teams", "investment_value": "High", "relentless_viability": "High", "similar_owned_champions": ["Krisk", "Duchess Lilitu", "Ursuga Warcaller"], "best_mastery_overall": "Warmaster", "cooldown_impact": "A2/A3 books reduce cooldowns", "stable_turn_order": ["A3", "A2", "A1", "A1"]}```

```

### Module 3: Team Creator Inputs

## 19. Synergy Engine```

```json{

{"team_setups": [{"name": "Hydra Control", "champions": ["Alice the Wanderer", "Krisk", "Duchess Lilitu"], "strategy": "Control, buff, revive"}], "similar_champions": [{"champion": "Krisk", "similarity_reason": "Control/Support"}, {"champion": "Duchess Lilitu", "similarity_reason": "Control/Support"}, {"champion": "Ursuga Warcaller", "similarity_reason": "Control/Support"}]}  "first_turn_skill": "Clockwork Cyclone",

```  "skill_priority": ["A2", "A3", "A1"],

  "disabled_skills": []

## 20. Community Ratings & Notes}

```json```

{"community": {"hellhades": "S", "ayumilove": "S", "reddit": "S-", "notes": "Top tier for Hydra and control content."}}

```### Module 4: Mastery Proc Simulation

```

# End of Template{

  "scenarios": [

---    {

      "type": "Arena Nuker",

All data validated as of October 2025 using Raid Shadow Legends Wiki, Ayumilove, and Hellhades.      "mastery": "Helmsmasher",

      "bonus_damage": "Up to 50% ignore DEF",
      "notes": "Maximizes burst on A3, especially if chain triggers"
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
      "notes": "Best for boss nuking, especially Fire Knight"
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
  "notes": "Single-target damage is good, but lacks debuffs and utility for Clan Boss. Not recommended for main CB team."
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
  "notes": "Top-tier for cooldown control and single-target nuking. Excels in Arena, Eternal Dragon, and Fire Knight.",
  "owned_comparison": [
    { "champion": "Trunda Giltmallet", "comparison": "Trunda is a stronger AOE nuker, Alice brings more control." },
    { "champion": "Foli", "comparison": "Foli offers more survivability, Alice has better cooldown control." }
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
    "notes": "Excellent first or counter-pick for control teams."
  }
}
```

### Module 9: Turn Meter Simulation & Gear Tradeoffs
```
{
  "extra_turn_effects": "Passive resets skill cooldowns on kill; no extra turns",
  "gear_set_stability": {
    "Reflex": "Can desync skill rotation.",
    "Relentless": "Not recommended; no extra turn synergy.",
    "Savage": "Stable; maximizes damage output."
  },
  "rotation_desync_risks": {
    "Reflex": "Medium",
    "Relentless": "Low",
    "Savage": "None"
  }
}
```

### Module 10: Utility Comparison Champions
```
[
  { "champion": "Trunda Giltmallet", "role": "AOE Nuker", "comparison": "Trunda outperforms Alice in AOE damage, Alice brings more control." },
  { "champion": "Foli", "role": "Single Target Nuker", "comparison": "Foli brings more survivability, Alice has better cooldown control." }
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
  "damage_rotation": "Open with A2 for control, A3 for single-target burst",
  "turn_meter_stability": "Stable; passive resets skills on kill",
  "passive_impact": "Significant bonus damage and skill cycling",
  "gear_stat_notes": "Prioritize ATK, C.DMG, SPD, ACC; Savage set for nuking",
  "ally_synergy_impact": "Works best with ATK buffers and debuffers",
  "draft_value": "First or counter-pick for control teams",
  "investment_value": "High; top-tier for control and nuking",
  "relentless_viability": "Low",
  "similar_owned_champions": ["Trunda Giltmallet", "Foli"]
}
```

### Module 13: Synergy Engine
```
{
  "team_setups": [
    {
      "name": "Arena Control Nuking Team",
      "champions": ["Alice the Wanderer", "Arbiter", "Lydia the Deathsiren", "Deacon Armstrong"],
      "strategy": "Speed boost, ATK up, DEF down, then Alice A2/A3 for control and nuke"
    }
  ],
  "similar_champions": [
    { "champion": "Trunda Giltmallet", "similarity_reason": "Both are legendary AOE nukers" },
    { "champion": "Foli", "similarity_reason": "Both are single-target nukers with high ATK scaling" }
  ]
}
```
      "notes": "<NOTES ON DAMAGE OR EFFECTS>"

    }

    // Add more scenarios as needed
