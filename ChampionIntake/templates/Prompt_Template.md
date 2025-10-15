



# Champion Prompt Template (Markdown)

> **Note:** For each section, pull in the corresponding information from the champion's JSON prompt file as defined in `Prompt_Template.json`. Use the bullet points as guidance for the level of detail and content expected.

---

## 1. Base Stats
_(Populate with the `base_stats` section from the JSON template)_
- List all raw stats (HP, ATK, DEF, SPD, C.Rate, C.DMG, RES, ACC) for direct comparison and calculations.
- If mastery damage scales with HP, use updated HP values for simulation.

## 2. Overview & Initial Summary
_(Populate with the `overview` section from the JSON template)_
- Role classification
- Rarity and archetype
- Primary damage stat
- Skill scaling (A1, A2, A3)
- Recommended mastery (PvE, Clan Boss, PvP)
- Booking ROI
- Best gear sets by situation:
  - PvP (Arena Offense & Defense)
  - Clan Boss
  - Hydra
  - Iron Twins
  - Dungeons (Wave-Clearing)
  - Solo Farming
- Gear tradeoffs (pros/cons)
- Focus stats by role
- Accuracy and resistance requirements for HARD 10 dungeons, Hydra, and Iron Twins
- Best dungeon use case based on skills, buffs/debuffs, and passive

## 3. Skill Summary & Rotation Analysis
_(Populate with the `skills` section from the JSON template)_
- Skill-by-skill breakdown:
  - Hit count
  - Cooldowns (booked and unbooked)
  - Multipliers
  - Skill type classification
- Passive skill impact if relevant
- Compare booked vs unbooked cooldowns and note if booking is required
- Determine the most efficient damage rotation based on cooldowns and skill types
- Output the stable turn order over 6–10 turns

## 4. Skill Book Requirements & Effects
_(Populate with the `books` section from the JSON template)_
- For each skill, list book investment and its impact
- Compare booked vs unbooked cooldowns
- Note if booking is required for optimal use

## 5. Aura Details
_(Populate with the `aura` section from the JSON template)_
- List aura stat, amount, area, and any special notes

## 6. AI Behavior & Skill Logic
_(Populate with the `ai_logic` section from the JSON template)_
- Describe AI skill usage priority
- List any conditional logic for skill use

## 7. Team Creator Inputs
_(Populate with the `team_inputs` section from the JSON template)_
- First turn skill
- Skill priority
- Disabled skills

## 8. Mastery Proc Simulation
_(Populate with the `mastery_proc_simulation` section from the JSON template)_
- Simulate mastery damage across four scenarios:
  - Single Boss (use updated HP values if mastery damage scales)
  - Boss + 10 Minions (Spider’s Den HARD)
  - Boss + 5 Minions (2 cycles/10 turns)
  - Boss + 2 High-HP Minions (2 cycles/10 turns)
- Expected bonus damage per cycle for each mastery
- Recommend best mastery per boss type

## 9. Mastery Recommendation
_(Populate with the `recommended_mastery` section from the JSON template)_
- Note only the single best mastery for this champion

## 10. Clan Boss Damage Tracking
_(Populate with the `clan_boss_damage` section from the JSON template)_
- Damage per turn
- Compare against benchmark attackers: Ninja, Michelangelo, Geomancer, Wukong
- Estimate passive mastery triggers for benchmark champions

## 11. Dungeon/Content Breakdown
_(Populate with the `content_breakdown` section from the JSON template)_
- Rate champion roles and notes for all major content
- For each, specify best use case based on skills, buffs/debuffs, and passives

## 12. Ally Synergy & Speed Tuning
_(Populate with the `synergy_speed` section from the JSON template)_
- Recommended buffs
- Up to 3 sets of good team member champions, preferring the owned list (leave blank if unknown)
- Suggest speed tuning per boss (max 300)
- Gear/stat priorities by role
- Evaluate if Relentless/Extra Turn gear impacts mastery choice

## 13. Utility & Investment Value
_(Populate with the `utility_investment` section from the JSON template)_
- Ask for benchmark champion list once
- Allow updates
- Rate investment value vs benchmark champions

## 14. Turn Meter Simulation & Gear Tradeoffs
_(Populate with the `turn_meter_gear` section from the JSON template)_
- Simulate turn meter effects and gear set stability
- Evaluate if relentless/extra turn gear changes mastery choice

## 15. Final Summary
_(Populate with the `final_summary` section from the JSON template)_
- Mastery preference across content types
- Cooldown impact
- Best mastery overall
- Stable turn order
- Passive impact
- Gear and stat notes
- Ally synergy impact
- Relentless viability
- Investment value

## 16. Synergy Engine (Owned Champions Only)
_(Populate with the synergy engine section from the JSON template, if applicable)_

## 17. Community Ratings & Notes
_(Populate with the `community` section from the JSON template)_
- Community ratings and notes from Hellhades, Ayumilove, Reddit, etc.

---

For the canonical schema and field definitions, see: `ChampionIntake/templates/Prompt_Template.json`
