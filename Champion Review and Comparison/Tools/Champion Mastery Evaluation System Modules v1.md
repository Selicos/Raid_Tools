# Champion Mastery Evaluation System (Modular + Logging + Synergy-Aware)

This system evaluates Raid Shadow Legends champions using modular components. Each module outputs structured data to a champion log file. Logs are used for synergy analysis, team-building, and comparison. All champions must be initialized with an ownership status before evaluation.

---

## 🧭 Evaluation Flow Overview

1. **Initialize Champion (Module 0)**
2. **Run Modules 1–12** to populate champion log
3. **Run Module 13** to generate synergy-based team setups using only OWNED champions
4. **Use logs** for comparison, planning, and draft strategy

---

## 📁 Champion Log Format

Each module appends to a JSON log file:

```json
{
  "champion": "ChampionName",
  "owned": true,
  "overview": { ... },
  "skills": { ... },
  "team_inputs": { ... },
  "mastery_simulation": { ... },
  "clan_boss": { ... },
  "synergy": { ... },
  "investment": { ... },
  "intelligence": { ... },
  "turn_meter": { ... },
  "utility_comparison": { ... },
  "ratings": { ... },
  "final_summary": { ... }
}
