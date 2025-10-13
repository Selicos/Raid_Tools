---

### 📘 `module_13_synergy_engine.md`

```markdown
## Module 13: Synergy Engine

**Inputs:**
- `owned_champions` list
- All champion logs

**Goal:**
Build teams using only OWNED champions based on synergy and role matching.

**Output:**
```json
"synergy_engine": {
  "team_setups": [
    {
      "name": "<TEAM NAME>",
      "champions": ["<CHAMPION_1>", "<CHAMPION_2>", "..."],
      "strategy": "<TEAM STRATEGY OR NOTES>"
    }
    // Add more team setups as needed
  ],
  "similar_champions": [
    {
      "champion": "<CHAMPION NAME>",
      "similarity_reason": "<REASON FOR SIMILARITY>"
    }
    // Add more similar champions as needed
  ]
}
```
