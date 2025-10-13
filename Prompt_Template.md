<!--
IMPORTANT: This file is the authoritative template for champion prompt processing and JSON generation.
All prompt-to-JSON and prompt-to-markdown workflows must follow the instructions and structure in this file.
Keep this file up to date and reference it in all related documentation and scripts.
-->

# Prompt-to-JSON and Prompt-to-Markdown Workflow

Given a champion prompt file (see `ChampionIntake/Prompt/[champion]_prompt.md`), generate:

1. **A fully completed JSON log** for the champion, using the structure and fields from `logTemplate.json`, filling in all required values with accurate, realistic, or best-guess data for this champion.
2. **A completed Markdown file** (`[champion]_prompt.completed.md`) that fills out every module in the prompt, replacing all placeholders with real values, so it serves as a human-readable, step-by-step worked example for this champion. **This file must be placed in the `output/completed` directory.**
3. Use the module-by-module breakdown in the prompt file for the `.md` structure.
4. Ensure all fields are filled, and the JSON is valid.
5. If any information is missing, use best-guess values based on Raid Shadow Legends sources (Wiki, Ayumilove, Hellhades).
6. Save the completed JSON in the corresponding `champion.json` file in `ChampionIntake/Champions/`.

---


## Example: Completed Markdown for <CHAMPION_NAME>

Below is a worked example of a completed prompt markdown for any champion. Replace `<CHAMPION_NAME>` and all champion-specific values as appropriate. **When generating this file, always save it to `output/completed/[champion]_prompt.completed.md`.** All modules are filled with real values, following the template and prompt structure:

---
# Champion Log Generation Prompt for <CHAMPION_NAME>

---
## Module 0: Champion Setup

**Inputs:**
- Champion name: <CHAMPION_NAME>
- Ownership status: OWNED

**Goal:**
Initialize champion log and set ownership flag.

**Output:**
```json
{
	"champion": "<CHAMPION_NAME>",
	"owned": true
}
```

---
## Module 1: Overview & Initial Summary

**Inputs:**
- Champion role: <ROLE>
- Archetype: <ARCHETYPE>
- Gear sets: <GEAR SETS>
- Mastery: <MASTERY>
- Booking ROI: <BOOKING ROI>

### Primary Damage Stat
- [x] <PRIMARY_STAT>
- [ ] (other options as appropriate)

**Skill Scaling Details:**
- A1: <STAT>
- A2: <STAT>
- A3: <STAT>

**Output:**
```json
"overview": {
	"role": "<ROLE>",
	"rarity": "<RARITY>",
	"archetype": "<ARCHETYPE>",
	"primary_damage_stat": "<PRIMARY_STAT>",
	"skill_scaling": {
		"A1": "<STAT>",
		"A2": "<STAT>",
		"A3": "<STAT>"
	},
	"best_mastery": {
		"pve_pvp": "<MASTERY>",
		"clan_boss": "<MASTERY>"
	},
	"booking_roi": "<BOOKING ROI>",
	"gear_sets": {
		"pvp_offense": [<SETS>],
		"pvp_defense": [<SETS>],
		"clan_boss": [<SETS>],
		"hydra": [<SETS>],
		"iron_twins": [<SETS>],
		"dungeons": [<SETS>],
		"solo_farming": [<SETS>]
	},
	"gear_tradeoffs": [
		{ "set": "<SET>", "pros": "<PROS>", "cons": "<CONS>" }
	],
	"focus_stats": {
		"arena_dungeons": [<STATS>],
		"clan_boss": [<STATS>]
	},
	"accuracy_resistance": {
		"hard_10_dungeons": "<VALUE>",
		"hydra": "<VALUE>",
		"iron_twins": "<VALUE>"
	},
	"best_dungeon_use": "<DUNGEON>"
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
		"name": "<A1 NAME>",
		"type": "<TYPE>",
		"hit_count": <NUMBER>,
		"cooldown": "<COOLDOWN>",
		"multiplier": "<MULTIPLIER>",
		"notes": "<NOTES>"
	},
	"a2": {
		"name": "<A2 NAME>",
		"type": "<TYPE>",
		"hit_count": <NUMBER>,
		"cooldown": "<COOLDOWN>",
		"multiplier": "<MULTIPLIER>",
		"notes": "<NOTES>"
	},
	"a3": {
		"name": "<A3 NAME>",
		"type": "<TYPE>",
		"hit_count": <NUMBER>,
		"cooldown": "<COOLDOWN>",
		"multiplier": "<MULTIPLIER>",
		"notes": "<NOTES>"
	},
	"passive": {
		"exists": <true/false>,
		"impact": "<IMPACT>"
	},
	"booking": {
		"impact": "<IMPACT>",
		"notes": "<NOTES>"
	},
	"rotation": {
		"optimal_cycle": [<SKILL ORDER>],
		"damage_per_turn": {
			"a3": "<VALUE>",
			"a2": "<VALUE>",
			"a1": "<VALUE>"
		},
		"average_damage": "<VALUE>",
		"buff_debuff_uptime": {
			"HP Burn": "<VALUE>",
			"Weaken": "<VALUE>"
		},
		"extra_turn_frequency": "<VALUE>"
	}
}
```

...existing code...
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

---