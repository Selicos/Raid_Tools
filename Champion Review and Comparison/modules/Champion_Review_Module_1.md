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
