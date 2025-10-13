---

### 📘 `module_8_intelligence.md`

```markdown
## Module 8: Intelligence Score & Draft Recommendations

**Inputs:**
- Synergy data from Module 6
- OWNED champion list

**Goal:**
Score synergy and guide PvP drafting strategy.

**Output:**
```json
"intelligence": {
  "synergy_scores": {
    "<CHAMPION_1>": <SCORE>,
    "<CHAMPION_2>": <SCORE>
    // Add more champions as needed
  },
  "draft_logic": {
    "early_pick": <true/false>,
    "counter_pick": <true/false>,
    "avoid": <true/false>,
    "notes": "<NOTES ON DRAFT LOGIC>"
  }
}
```
