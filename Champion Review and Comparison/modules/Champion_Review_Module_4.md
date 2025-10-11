
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
      "type": "Single Boss",
      "mastery": "Warmaster",
      "bonus_damage": "10K–14K per proc",
      "notes": "Burn ticks stack with Warmaster procs for sustained damage"
    },
    {
      "type": "Boss + 10 Minions",
      "mastery": "Helmsmasher",
      "bonus_damage": "22K–28K per AOE hit",
      "notes": "Helmsmasher boosts AOE burn application damage"
    },
    {
      "type": "Boss + 5 Minions",
      "mastery": "Helmsmasher",
      "bonus_damage": "18K–24K per AOE hit",
      "notes": "Ideal for Dragon and Ice Golem waves"
    },
    {
      "type": "Boss + 2 High-HP Minions",
      "mastery": "Helmsmasher",
      "bonus_damage": "15K–20K per AOE hit",
      "notes": "Burns help chip down tanky adds"
    }
  ],
  "recommended_mastery": {
    "clan_boss": "Warmaster",
    "spider_hard": "Helmsmasher",
    "hydra": "Warmaster",
    "iron_twins": "Helmsmasher"
  }
}
