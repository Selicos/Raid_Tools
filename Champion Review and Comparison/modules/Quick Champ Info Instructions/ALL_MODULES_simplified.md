# Champion Log Generation Modules
Do not use this file. Use the separate module items in the modules dir.

Use the following structure to generate a complete JSON-based champion log. Each module should be clearly labeled and contain the requested information.

---

## Module 0: Champion Identity
- Define the champion’s name, faction, rarity, affinity, and role.
- Summarize their core identity and battlefield purpose in 1–2 sentences.

---

## Module 1: Skill Breakdown
- List and describe all active and passive skills (A1, A2, A3, Passive, Aura if applicable).
- Include effects, debuff types, cooldowns, and any conditional mechanics.

---

## Module 2: Passive Utility
- Explain how the champion’s passive skills or mechanics contribute to survivability, damage mitigation, or team synergy.
- Include any reactive or conditional effects.

---

## Module 3: Gear Optimization
- Recommend gear sets and stat priorities for the champion’s primary role.
- Include notes for PvE vs PvP builds if applicable.

---

## Module 4: Mastery Simulation
- Suggest mastery trees (Offense, Defense, Support) and key nodes.
- Justify choices based on the champion’s mechanics and content focus.

---

## Module 5: Synergy and Pairing
- List ideal allies and team compositions.
- Mention champions or mechanics to avoid.
- Optionally include synergy scoring or tags.

---

## Module 6: PvE Encounter Performance
- Rate and explain performance in:
  - Clan Boss
  - Hydra
  - Doom Tower
  - Dungeons (Dragon, Ice Golem, Fire Knight, Spider)

---

## Module 7: PvP Viability
- Evaluate the champion’s effectiveness in Arena Offense and Defense.
- Mention strengths, weaknesses, and meta relevance.

---

## Module 8: Faction Wars Utility
- Describe the champion’s role and performance in Faction Wars.
- Include synergy with faction-specific champions or mechanics.

---

## Module 9: Clan Boss Strategy
- Detail speed tuning, debuff uptime, and damage contribution.
- Mention compatibility with UNM/NM teams or specific comps.

---

## Module 10: Hydra Strategy
- Explain how the champion interacts with Hydra mechanics.
- Include head targeting, survivability, and debuff utility.

---

## Module 11: Ratings Summary
- Provide a 1–5 rating scale across all major content types.
- Optionally include a table or color-coded summary.

---

## Module 12: Final Verdict
- Summarize the champion’s overall value, strengths, and ideal use cases.
- Include build notes and team placement tips.

---

## Module 13: JSON Output
- Only run this module if told to putput to json in the prompt.
- Output the full champion log in JSON format.
- Include all modules above in structured fields.
- Format for easy copy-paste into `champions/[ChampionName].json`
