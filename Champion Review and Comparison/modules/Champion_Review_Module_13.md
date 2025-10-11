
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
      "name": "Arena Nuking Team",
      "champions": ["Artak", "Deacon Armstrong"],
      "strategy": "Deacon opens with TM boost and DEF Down → Artak follows with AOE burn"
    },
    {
      "name": "Clan Boss Hybrid Team",
      "champions": ["Geomancer", "Artak", "Deacon Armstrong"],
      "strategy": "Geomancer handles passive damage, Artak adds burst, Deacon maintains rotation"
    },
    {
      "name": "Hydra Control Setup",
      "champions": ["Geomancer", "Deacon Armstrong", "Artak"],
      "strategy": "Use Artak for wave-clear; rely on Geomancer for boss damage"
    }
  ],
  "similar_champions": [
    {
      "champion": "Geomancer",
      "similarity_reason": "Passive damage, PvE boss utility"
    },
    {
      "champion": "Deacon Armstrong",
      "similarity_reason": "Setup specialist, strong synergy"
    }
  ]
}
