
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
  "recommended_buffs": ["Increase ATK", "Decrease DEF", "Speed Boost", "Turn Meter Fill"],
  "support_champion_sets": [
    ["Deacon Armstrong", "Geomancer"],
    [],
    []
  ],
  "speed_tuning": {
    "arena": "230–250",
    "dungeons": "200–220",
    "clan_boss": "170–190"
  },
  "gear_stat_priorities": {
    "arena": ["Savage", "Cruel", "ATK%", "Crit Rate", "Crit Damage", "Accuracy"],
    "clan_boss": ["Accuracy", "Speed", "HP%", "ATK%", "Survivability"],
    "dungeons": ["Savage", "Cruel", "Accuracy", "ATK%", "Crit Rate"]
  },
  "relentless_viability": "Moderate — can help cycle burns faster but risks cooldown desync"
}
