---

### 📘 `module_1_overview.md`

```markdown
## Module 1: Overview & Initial Summary

**Inputs:**
- Champion role, archetype, gear sets, mastery, booking ROI

**Goal:**
Summarize champion identity and performance across content types.

### Primary Damage Stat
- [ ] ATK
- [ ] HP
- [ ] DEF
- [ ] Hybrid (specify: __________)
- [ ] Other (specify: __________)

**Skill Scaling Details:**  
List each skill and the stat(s) it scales from.

**Output:**
```json
"overview": {
  "role": "Attack",
  "archetype": "Burn DPS / Debuff Specialist",
  "primary_damage_stat": "ATK",                // <-- NEW FIELD
  "skill_scaling": {                           // <-- NEW FIELD
    "A1": "ATK",
    "A2": "ATK",
    "A3": "ATK"
  },
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
```
