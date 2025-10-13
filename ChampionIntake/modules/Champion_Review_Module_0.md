## Module 0: Champion Setup

**Inputs:**
- Champion name
- Ownership status: OWNED or NOTOWNED

**Goal:**
Initialize champion log and set ownership flag.

**Output:**
```json
{
  "champion": "<CHAMPION NAME>",
  "owned": <true/false>,
  "overview": {
    "role": "<PLACEHOLDER_ROLE>",
    "archetype": "<PLACEHOLDER_ARCHETYPE>",
    "primary_damage_stat": "<PLACEHOLDER_STAT>",
    "skill_scaling": {"A1": "<PLACEHOLDER_STAT>"},
    "best_mastery": {"pve_pvp": "<PLACEHOLDER_MASTERY>", "clan_boss": "<PLACEHOLDER_MASTERY>"},
    "booking_roi": "<PLACEHOLDER_VALUE>",
    "gear_sets": {
      "pvp_offense": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "pvp_defense": ["<PLACEHOLDER_SET>"],
      "clan_boss": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "hydra": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "iron_twins": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "dungeons": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"],
      "solo_farming": ["<PLACEHOLDER_SET>", "<PLACEHOLDER_SET>"]
    },
    "gear_tradeoffs": [
      { "set": "<PLACEHOLDER_SET>", "pros": "<PLACEHOLDER_PROS>", "cons": "<PLACEHOLDER_CONS>" }
    ],
    "focus_stats": {
      "arena_dungeons": ["<PLACEHOLDER_STAT>", "<PLACEHOLDER_STAT>", "<PLACEHOLDER_STAT>"],
      "clan_boss": ["<PLACEHOLDER_STAT>", "<PLACEHOLDER_STAT>", "<PLACEHOLDER_STAT>"]
    },
    "accuracy_resistance": {
      "hard_10_dungeons": "<PLACEHOLDER_VALUE>",
      "hydra": "<PLACEHOLDER_VALUE>",
      "iron_twins": "<PLACEHOLDER_VALUE>"
    },
    "best_dungeon_use": "<PLACEHOLDER_DUNGEON>"
  }
}
```
