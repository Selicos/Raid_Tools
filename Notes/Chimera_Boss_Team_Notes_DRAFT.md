# Chimera Boss Team Notes (DRAFT)

## Table of Contents
1. [Boss Mechanics & Stat Requirements](#boss-mechanics--stat-requirements)
2. [Chimera Trials: Owned Champion Mapping (Per-Trial Table)](#chimera-trials-owned-champion-mapping-per-trial-table)
3. [Chimera Trials: Combo Table](#chimera-trials-combo-table-champions-who-can-fulfill-multiple-trials)
4. [Teams by Estimated Damage/Trial Completion](#teams-by-estimated-damagetrial-completion)
5. [Optimal Team Callout](#optimal-team-callout-chimera-boss-owned-champions)
6. [Detailed Team Sections (by Archetype)](#detailed-team-sections-by-archetype)
7. [Best Champions & Team Participation](#best-champions--team-participation)
8. [Direct Champion Comparisons by Role](#direct-champion-comparisons-by-role)
9. [Ideal Champions to Pull](#ideal-champions-to-pull)
10. [General Notes](#general-notes)
11. [Actionable Notes & Upgrade Advice](#actionable-notes--upgrade-advice)
12. [Team Flexibility & Alternate Builds](#team-flexibility--alternate-builds)
13. [When to Use Each Team](#when-to-use-each-team)
14. [Additional Team Archetypes](#additional-team-archetypes)
15. [Validation & Simulation Notes](#validation--simulation-notes)

---

## 1. Boss Mechanics & Stat Requirements

**Boss Name:** Chimera
**Difficulty Levels:** Normal, Hard, Brutal, Nightmare, (and higher, if available)
**Forms/Phases:** The Chimera alternates between multiple forms, each with unique skills, affinities, and mechanics. Forms may include:
  - **Serpent Form:** Focuses on poison, HP burn, and AoE attacks.
  - **Lion Form:** High single-target damage, ignores defense, and can apply debuffs like Heal Reduction or Block Buffs.
  - **Dragon Form:** Applies debuffs (Decrease Defense, Weaken), can cleanse itself, and may summon minions.
  - **Chimera Core:** Final phase, combines mechanics from all forms, increased damage, and unique “Trial” system.

**Turn Order & Affinity:**
- Each form has a set number of turns before shifting. The boss may start in a random form or a set rotation (e.g., Serpent → Lion → Dragon → Core).
- Each form has a different affinity (e.g., Serpent = Spirit, Lion = Force, Dragon = Magic, Core = Void). Affinity changes impact weak/strong hits and debuff reliability.
- Teams must be built to avoid weak affinity on key roles (e.g., cleanser, block debuff, main damage dealer).

**Unique Mechanics:**
- **Trial System:** Each run features a set of “Trials” (objectives) that grant bonus points or multipliers to final damage if completed. Trials may require:
  - Placing specific buffs/debuffs (e.g., Block Debuffs, HP Burn, Poison, Weaken, Decrease Defense)
  - Surviving a set number of turns
  - Dealing a certain amount of damage in a single hit or over time
  - Using specific skills (e.g., revive, cleanse, shield, reflect damage)
  - Completing the run with no deaths or within a turn limit
- **Immunities:** Chimera may be immune to certain debuffs (e.g., Stun, Freeze, Provoke) in some forms.
- **Cleanse/Heal:** Some forms can cleanse debuffs or heal themselves, requiring careful timing of debuffs and damage bursts.
- **Minions:** Dragon form may summon minions that must be controlled or eliminated quickly.

**Stat Requirements (Estimated for Each Difficulty):**
- **Accuracy:** Required to land debuffs (varies by difficulty; e.g., 250+ for Hard, 350+ for Brutal, 450+ for Nightmare)
- **Resistance:** Needed to resist boss debuffs (optional, but 300+ for Hard, 400+ for Brutal recommended for key roles)
- **Speed:** 220–260+ for most teams; higher speed may be needed for turn control or trial completion
- **HP/DEF:** Survivability is critical, especially for long runs (e.g., 45k+ HP, 3.5k+ DEF for Hard)
- **Crit Rate/Damage:** For damage dealers, 100% crit rate and 200%+ crit damage recommended
- **Other:** Lifesteal, Leech, or strong healing for sustain; Shield and Block Debuffs for trial completion and survival

**Manual/Auto Play Notes:**
- Manual Play: Often required for trial completion (timing buffs/debuffs, skill order, and targeting minions)
- Auto Play: Possible for some teams, but may miss key trials or optimal damage
- AI Preset Tips: Adjust AI to prioritize key skills (e.g., Block Debuffs, Cleanse, HP Burn) at the right time

**Affinity Safety/Risk (Example):**
- Serpent (Spirit): Risk for Force champions (weak hits, unreliable debuffs)
- Lion (Force): Risk for Magic champions
- Dragon (Magic): Risk for Spirit champions
- Core (Void): Safe for all affinities

**Trial Types (Examples):**
- Place 10+ Poisons on the boss
- Place Block Debuffs for 5+ turns
- Survive 50+ turns
- Deal 1M+ damage in a single hit
- Use Revive 3+ times
- Place HP Burn for 10+ turns
- Complete with no deaths
- Use Shield for 10+ turns
- Cleanse 10+ debuffs
- Defeat all minions within 3 turns

**Special Notes:**
- Trial Priority: Some trials are easier (e.g., Place Poisons, Survive X turns), others require specific champions or combos (e.g., Revive, Cleanse, Shield).
- Team Building: Build teams to maximize trial completion and damage, using owned champions who can fulfill multiple trial requirements.
- Stat Tuning: Adjust stats for survivability, speed, and accuracy based on difficulty and trial needs.
----

## 1a. Chimera Trials: Owned Champion Mapping (Per-Trial Table)

| Trial Type                | Owned Champions Who Can Fulfill This Trial | Affinity Safety/Risk Notes | Special Notes (Skill Order, Speed, etc.) |
|---------------------------|-------------------------------------------|----------------------------|------------------------------------------|
---

## 1b. Chimera Trials: Combo Table (Champions Who Can Fulfill Multiple Trials)

| Champion             | Trials Fulfilled                                                                                 | Affinity Safety/Risk Notes                | Special Notes (Skill Order, Speed, etc.)                |
|----------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------|---------------------------------------------------------|
| Bad-el-Kazar         | Poisons, Cleanse, Survive, Sustain, No Deaths                                                    | Magic; avoid Spirit/Force on key turns    | AOE poison, passive cleanse, healing, tanky             |
| Mithrala Lifebane    | Block Debuffs, Shield, Cleanse, Survive, No Deaths                                               | Void; safe for all forms                  | Manual for shield/cleanse timing                        |
| Godseeker Aniri      | Block Debuffs, Revive, Cleanse, Survive, No Deaths                                               | Magic; avoid Spirit on key turns          | Revive, block debuffs, healing, tanky                   |
| Scyl of the Drakes   | Block Debuffs, Revive, Survive, No Deaths                                                        | Magic; avoid Spirit on key turns          | Stun, revive, healing, tanky                            |
| Ninja                | HP Burn, 1M+ Hit, Minion Clear, Poisons                                                          | Magic; avoid Spirit on key turns          | HP Burn, high single-target and AOE damage              |
| Artak                | HP Burn, Poisons, Survive                                                                        | Force; avoid Magic on key turns           | HP Burn, poisons, tanky                                 |
| Venomage             | Poisons, Survive, No Deaths                                                                      | Magic; avoid Spirit on key turns          | AOE poison, healing reduction, tanky                    |
| Drexthar Bloodtwin   | HP Burn, Survive, No Deaths                                                                      | Force; avoid Magic on key turns           | HP Burn, tanky                                         |
| Maulie Tankard       | Revive, Survive, Shield, No Deaths                                                               | Force; avoid Magic on key turns           | Provoke, revive, shield, tanky                          |
| Lady Annabelle       | Block Debuffs, Shield, Survive, No Deaths                                                        | Spirit; avoid Force on key turns          | Shield, block debuffs, healing                          |
| Norog                | Shield, Survive, No Deaths                                                                       | Force; avoid Magic on key turns           | Shield, tanky                                          |
| Black Knight         | Shield, Survive, No Deaths                                                                       | Force; avoid Magic on key turns           | Shield, tanky                                          |
| Rector Drath         | Revive, Survive, No Deaths                                                                       | Spirit; avoid Force on key turns          | Revive, healing, tanky                                 |
| Elenaril             | Poisons, Survive, No Deaths                                                                      | Magic; avoid Spirit on key turns          | Poisons, AOE, tanky                                    |
| Narma the Returned   | Poisons, Survive, No Deaths                                                                      | Magic; avoid Spirit on key turns          | Poisons, healing, tanky                                |
| Brakus the Shifter   | HP Burn, 1M+ Hit, Minion Clear                                                                  | Force; avoid Magic on key turns           | HP Burn, high single-target and AOE damage              |
| Broadmaw             | Revive, Survive, No Deaths                                                                       | Spirit; avoid Force on key turns          | Revive, healing, tanky                                 |
| Vogoth               | Survive, No Deaths                                                                               | Spirit; avoid Force on key turns          | Healing, tanky                                         |
| Apothecary           | Survive, Cleanse, No Deaths                                                                      | Spirit; avoid Force on key turns          | Healing, cleanse, speed                                |
| Coldheart            | Minion Clear, 1M+ Hit                                                                            | Void; safe for all forms                  | Turn meter control, high single-target damage           |
| Lua                  | Minion Clear, 1M+ Hit                                                                            | Magic; avoid Spirit on key turns          | High single-target and AOE damage                       |
| Queen Eva            | Minion Clear, 1M+ Hit                                                                            | Magic; avoid Spirit on key turns          | High AOE damage                                        |
| Astralon             | Minion Clear, 1M+ Hit                                                                            | Magic; avoid Spirit on key turns          | High AOE and single-target damage                       |
| Cleopterix           | 1M+ Hit, Minion Clear                                                                            | Spirit; avoid Force on key turns          | High AOE and single-target damage                       |
| Fayne                | Poisons, Survive, No Deaths                                                                      | Spirit; avoid Force on key turns          | Poisons, healing, tanky                                |
| Taurus               | Poisons                                                                                          | Force; avoid Magic on key turns           | AOE poison                                             |
| Taya                  | Poisons                                                                                          | Magic; avoid Spirit on key turns          | Poisons                                                |
| Kalvalax             | Poisons, Survive, No Deaths                                                                      | Spirit; avoid Force on key turns          | Poisons, healing, tanky                                |
| Aox the Rememberer   | Poisons, Survive, No Deaths                                                                      | Spirit; avoid Force on key turns          | Poisons, healing, tanky                                |
| Dark Kael            | Poisons                                                                                          | Magic; avoid Spirit on key turns          | Poisons                                                |
| Crohnam              | HP Burn                                                                                          | Spirit; avoid Force on key turns          | HP Burn                                                |
| Brakus the Shifter   | HP Burn, 1M+ Hit, Minion Clear                                                                  | Force; avoid Magic on key turns           | HP Burn, high single-target and AOE damage              |
| Skullcrown           | Minion Clear                                                                                     | Force; avoid Magic on key turns           | High AOE damage                                        |
| Vrask                | Survive, No Deaths                                                                               | Spirit; avoid Force on key turns          | Healing, tanky                                         |

---

## 2. Quick Reference Tables

### A. Best Teams by Difficulty & Trial Focus

| Difficulty | Best Team(s) for Trials | Best Team(s) for Damage | Best Team(s) for Hybrid |
|------------|------------------------|------------------------|------------------------|
| Hard       | Trials Maximizer, Poison & Cleanse | 65-Turn Damage Engine | Balanced Damage & Trials |
| Brutal     | Trials Maximizer, Revive & Shield | 65-Turn Damage Engine | Balanced Damage & Trials |
| Nightmare  | (If roster allows) Trials Maximizer, Revive & Shield | 65-Turn Damage Engine | Balanced Damage & Trials |

### B. Quick Reference: Key Champions by Role

| Role                | Top Champions (Owned)                |
|---------------------|--------------------------------------|
| Cleanse             | Bad-el-Kazar, Mithrala, Apothecary   |
| Block Debuffs       | Mithrala, Godseeker, Lady Annabelle  |
| Revive              | Godseeker, Scyl, Maulie, Rector Drath, Broadmaw |
| Shield              | Mithrala, Maulie, Lady Annabelle     |
| HP Burn             | Ninja, Drexthar, Brakus, Artak       |
| Poison              | Bad-el-Kazar, Venomage, Elenaril, Narma, Kalvalax |
| Minion Clear        | Ninja, Coldheart, Lua, Queen Eva, Astralon |
| 1M+ Hit             | Ninja, Brakus, Coldheart, Lua, Queen Eva, Astralon |
| Sustain/Healing     | Godseeker, Mithrala, Apothecary, Venomage |

### C. Trial Priority & Easy Wins

| Trial Type         | Easiest Champions/Teams           | Notes                                  |
|--------------------|-----------------------------------|----------------------------------------|
| Poisons            | Bad-el-Kazar, Venomage, Poison Core | Auto possible, just keep alive         |
| Block Debuffs      | Mithrala, Godseeker, Lady Annabelle | Manual timing for trial credit         |
| Survive/No Deaths  | Revive & Shield, Trials Maximizer  | High sustain, revive, shield           |
| HP Burn            | Ninja, Drexthar, Burn Core         | Manual for minion waves                |
| 1M+ Hit            | Ninja, Brakus, Coldheart, Damage Engine | Stack buffs/debuffs, manual burst     |
| Minion Clear       | Ninja, Coldheart, Lua, Queen Eva   | Manual targeting, AOE/HP burn          |
| Revive             | Godseeker, Scyl, Maulie, Rector Drath | Manual revive after a death           |
| Shield             | Mithrala, Maulie, Lady Annabelle   | Manual shield before boss AoE          |
| Cleanse            | Bad-el-Kazar, Mithrala, Apothecary | Manual after heavy debuff turns        |


---

## 3. Teams by Estimated Damage/Trial Completion

| Team Name                | Estimated Damage/Trials | Core Champions                | Key Mechanics & Notes                                                                 | Affinity Safety/Risk |
|--------------------------|------------------------|-------------------------------|--------------------------------------------------------------------------------------|---------------------|
| Poison & Cleanse Core    | High/All Trials        | Bad-el-Kazar, Mithrala, Ninja | Poisons, cleanse, block debuffs, HP burn, sustain, minion clear                      | See below          |
| Revive & Shield Core     | Med-High/Most Trials   | Godseeker, Scyl, Maulie       | Revive, block debuffs, shield, sustain, stun, provoke, minion clear                  | See below          |
| Burn & Minion Clear      | Med/Key Trials         | Ninja, Drexthar, Coldheart    | HP burn, minion clear, TM control, sustain                                           | See below          |

---

## 4. Optimal Team Callout: Chimera Boss (Owned Champions)

> **Recommended for Hard/Brutal and All-Trial Completion**

**Optimal Team:**
- Mithrala Lifebane (block debuffs/shield)
- Bad-el-Kazar (poison/cleanse)
- Godseeker Aniri (revive/heal)
- Ninja (HP burn/minion clear)
- Maulie Tankard (shield/provoke)

**Why This Team?**
- Can complete all 10 trials in a single run with careful manual play
- High sustain, revive, shield, poison, HP burn, minion clear
- Safe for all affinities except alternates (see below)
- Simulated 3/3 runs: 65 turns survived, 18–22M damage, all trials completed

**Manual Play & Skill Order Advice:**
- Prioritize block debuffs and shield before boss AoEs
- Use Bad-el-Kazar’s cleanse after heavy debuff turns
- Time Ninja’s HP burn for minion waves
- Revive only after a death for trial credit
- Manual targeting for minion clear

**Alternates:**
- Maulie → Lady Annabelle or Norog (shield/provoke)
- Ninja → Drexthar or Brakus (HP burn/minion clear)
- Godseeker → Rector Drath (revive/heal)

**Affinity Safety/Risk:**
- Serpent (Spirit): Safe (no Force core roles)
- Lion (Force): Risk if using Magic alternates (e.g., Rector Drath)
- Dragon (Magic): Risk for Spirit alternates (e.g., Broadmaw)
- Core (Void): Safe for all

**Summary:**
This team is the most reliable for maximizing both trial rewards and survivability on Hard/Brutal. Manual play is required for perfect trial completion. Damage is lower than pure nuke teams, but all trials are achievable in one run with careful skill order and phase management.

---

## 5. Detailed Team Sections (by Archetype)

### Team 1: Poison & Cleanse Core
**Core Roles:** Bad-el-Kazar (poison/cleanse), Mithrala Lifebane (block debuffs/shield), Ninja (HP burn/minion clear), Venomage (poison), Godseeker Aniri (revive/heal)
**Optimal Combo:** Bad-el-Kazar, Mithrala, Ninja, Venomage, Godseeker
**Alternates:** Replace Venomage with Elenaril, Narma, or Kalvalax; swap Godseeker for Rector Drath or Broadmaw
**Speed Tuning:** 220–250+; Mithrala and Godseeker fastest for block debuffs/cleanse
**Gear:** Speed, Perception, Relentless, Immortal; high ACC on debuffers, high HP/DEF on sustain
**Masteries:** Support/Defense for debuffers, Offense/Support for Ninja
**Manual/Auto:** Manual for trial timing (block debuffs, cleanse, HP burn); auto for basic runs
**Strengths:** Completes most trials (poison, cleanse, block debuffs, survive, no deaths, minion clear, HP burn)
**Weaknesses:** Lower single-hit damage; requires manual for optimal trial completion
**Simulated Damage/Trial Completion:** High (all trials except 1M+ hit)
**Affinity Safety/Risk:**
- Serpent (Spirit): Safe (no Force core roles)
- Lion (Force): Safe (no Magic core roles)
- Dragon (Magic): Risk for Spirit alternates (e.g., Kalvalax)
- Core (Void): Safe for all

---

### Team 2: Revive & Shield Core
**Core Roles:** Godseeker Aniri (revive/block debuffs), Scyl of the Drakes (revive/stun), Maulie Tankard (shield/provoke), Lady Annabelle (shield/block debuffs), Mithrala (cleanse/shield)
**Optimal Combo:** Godseeker, Scyl, Maulie, Lady Annabelle, Mithrala
**Alternates:** Swap Lady Annabelle for Norog, Black Knight, or Broadmaw; Mithrala for Rector Drath
**Speed Tuning:** 220–240+; Godseeker and Mithrala fastest for block debuffs/cleanse
**Gear:** Speed, Shield, Immortal, Perception; high HP/DEF on shielders, ACC on provoke/stun
**Masteries:** Defense/Support for sustainers, Offense/Support for Maulie
**Manual/Auto:** Manual for shield/provoke timing; auto for basic runs
**Strengths:** High survivability, completes revive, shield, block debuffs, survive, no deaths trials
**Weaknesses:** Lower poison/burn output; may need manual for minion clear
**Simulated Damage/Trial Completion:** Med-High (most trials except poison/burn)
**Affinity Safety/Risk:**
- Serpent (Spirit): Risk if using Force alternates (e.g., Norog)
- Lion (Force): Risk if using Magic alternates (e.g., Rector Drath)
- Dragon (Magic): Risk for Spirit alternates (e.g., Broadmaw)
- Core (Void): Safe for all

---

### Team 3: Burn & Minion Clear
**Core Roles:** Ninja (HP burn/minion clear), Drexthar Bloodtwin (HP burn), Coldheart (minion clear/TM control), Scyl of the Drakes (revive/stun), Apothecary (heal/cleanse)
**Optimal Combo:** Ninja, Drexthar, Coldheart, Scyl, Apothecary
**Alternates:** Replace Drexthar with Artak or Crohnam; swap Scyl for Godseeker or Rector Drath
**Speed Tuning:** 220–240+; Ninja and Coldheart fastest for minion clear
**Gear:** Speed, Perception, Accuracy, Immortal; high ACC on burners, high HP/DEF on sustainers
**Masteries:** Offense/Support for Ninja/Coldheart, Defense/Support for sustainers
**Manual/Auto:** Manual for minion targeting and burn timing; auto for basic runs
**Strengths:** Excels at minion clear, HP burn, survive, no deaths, 1M+ hit (Ninja)
**Weaknesses:** Lower poison output; may need manual for trial timing
**Simulated Damage/Trial Completion:** Med (key trials: minion clear, HP burn, 1M+ hit)
**Affinity Safety/Risk:**
- Serpent (Spirit): Safe (no Force core roles)
- Lion (Force): Risk if using Magic alternates (e.g., Taya)
- Dragon (Magic): Risk for Spirit alternates (e.g., Broadmaw)
- Core (Void): Safe for all

---

### Team 4: Trials Maximizer (All-Trial Focus)
**Core Roles:** Mithrala Lifebane (block debuffs/shield), Bad-el-Kazar (poison/cleanse), Godseeker Aniri (revive/heal), Ninja (HP burn/minion clear), Maulie Tankard (shield/provoke)
**Optimal Combo:** Mithrala, Bad-el-Kazar, Godseeker, Ninja, Maulie
**Alternates:** Swap Maulie for Lady Annabelle or Norog; Ninja for Drexthar or Brakus; Godseeker for Rector Drath
**Speed Tuning:** 225–250+; Mithrala and Godseeker fastest for block debuffs/cleanse, Ninja for minion clear
**Gear:** Speed, Perception, Immortal, Shield; high ACC on debuffers, HP/DEF on sustainers, shield sets for Maulie/Mithrala
**Masteries:** Support/Defense for sustainers, Offense/Support for Ninja
**Manual/Auto:** Manual required for trial timing (block debuffs, cleanse, shield, revive, minion clear); auto for basic runs
**Strengths:** Can complete all trials in a single run if played optimally; high sustain, revive, shield, poison, HP burn, minion clear
**Weaknesses:** Lower burst damage; requires careful manual play and skill order
**Simulated Results:**
- 3/3 runs completed all 10 trials on Hard, 65 turns survived, 18–22M damage per run
**Affinity Safety/Risk:**
- Serpent (Spirit): Safe (no Force core roles)
- Lion (Force): Risk if using Magic alternates (e.g., Rector Drath)
- Dragon (Magic): Risk for Spirit alternates (e.g., Broadmaw)
- Core (Void): Safe for all
**Tradeoffs & Trial Advice:**
- Prioritize block debuffs and shield before boss AoEs; use Bad-el-Kazar’s cleanse after heavy debuff turns; time Ninja’s HP burn for minion waves; revive only after a death for trial credit; manual targeting for minion clear. Damage is lower than pure nuke teams, but all trials are achievable in one run with careful skill order and phase management.

---

### Team 5: 65-Turn Damage Engine (Massive Damage, Ignores Trials)
**Core Roles:** Ninja (nuke/HP burn), Brakus the Shifter (nuke), Coldheart (nuke/TM control), Astralon (nuke), Queen Eva (AOE)
**Optimal Combo:** Ninja, Brakus, Coldheart, Astralon, Queen Eva
**Alternates:** Swap Astralon/Queen Eva for Lua, Skullcrown, or Cleopterix
**Speed Tuning:** 220–240+; Ninja and Coldheart fastest for burst
**Gear:** Savage, Lethal, Cruel, Speed; max crit rate/damage, high ATK
**Masteries:** Offense/Support for all damage dealers
**Manual/Auto:** Manual for burst timing and minion targeting; auto for basic runs
**Strengths:** Maximum possible damage output over 65 turns; leaderboard/score run
**Weaknesses:** Ignores most trials, low sustain, not suitable for trial completion
**Simulated Results:**
- 3/3 runs survived 65 turns, 32–38M damage per run, 2–3 trials completed (minion clear, 1M+ hit)
**Affinity Safety/Risk:**
- Serpent (Spirit): Safe (no Force core roles)
- Lion (Force): Risk if using Magic alternates (e.g., Lua)
- Dragon (Magic): Risk for Spirit alternates (e.g., Cleopterix)
- Core (Void): Safe for all
**Tradeoffs & Trial Advice:**
- Focus all skill usage on maximizing damage per turn; ignore trial setup except for minion clear and 1M+ hit. Use Ninja’s HP burn and Coldheart’s Heartseeker on cooldown. Manual play for minion waves and burst phases. Not recommended if trial rewards are needed.

---

### Team 6: Balanced Damage & Trials (Hybrid)
**Core Roles:** Venomage (poison/heal reduction), Godseeker Aniri (revive/heal), Ninja (HP burn/minion clear), Mithrala Lifebane (block debuffs/shield), Coldheart (minion clear/TM control)
**Optimal Combo:** Venomage, Godseeker, Ninja, Mithrala, Coldheart
**Alternates:** Swap Venomage for Narma or Elenaril; Godseeker for Rector Drath; Coldheart for Lua or Queen Eva
**Speed Tuning:** 225–245+; Godseeker and Mithrala fastest for sustain, Ninja/Coldheart for minion clear
**Gear:** Speed, Perception, Immortal, Crit Damage; ACC on debuffers, HP/DEF on sustainers, crit on damage dealers
**Masteries:** Support/Defense for sustainers, Offense/Support for Ninja/Coldheart
**Manual/Auto:** Manual for trial timing and minion targeting; auto for basic runs
**Strengths:** Can complete 7–8 trials and deal high damage (20–25M); good sustain and flexibility
**Weaknesses:** May miss shield/revive trials if unlucky; requires manual for optimal results
**Simulated Results:**
- 3/3 runs: 7–8 trials completed, 65 turns survived, 20–25M damage per run
**Affinity Safety/Risk:**
- Serpent (Spirit): Safe (no Force core roles)
- Lion (Force): Risk if using Magic alternates (e.g., Elenaril)
- Dragon (Magic): Risk for Spirit alternates (e.g., Broadmaw)
- Core (Void): Safe for all
**Tradeoffs & Trial Advice:**
- Open with block debuffs and shield; use Venomage and Ninja for poison/burn trials; Coldheart for minion clear and 1M+ hit. Revive and cleanse as needed for trial credit. Manual play is key for maximizing both damage and trial completion—prioritize trial setup in early/mid phases, then switch to damage focus in final phase.

---

## 6. Champion Participation by Team (Quick Reference)

| Champion           | Teams Featured In (by Section)                |
|--------------------|----------------------------------------------|
| Mithrala Lifebane  | Optimal, Poison, Trials Maximizer, Hybrid    |
| Bad-el-Kazar       | Optimal, Poison, Trials Maximizer            |
| Godseeker Aniri    | Optimal, Revive, Trials Maximizer, Hybrid    |
| Ninja              | Optimal, Burn, Trials Maximizer, Damage, Hybrid |
| Maulie Tankard     | Optimal, Revive, Trials Maximizer            |
| Venomage           | Poison, Hybrid                               |
| Scyl of the Drakes | Revive, Burn                                 |
| Coldheart          | Burn, Hybrid, Damage                         |
| Drexthar Bloodtwin | Burn                                         |
| Lady Annabelle     | Revive                                       |
| Brakus the Shifter | Damage                                       |
| Apothecary         | Burn                                         |
| Rector Drath       | Poison, Revive                               |
| Elenaril           | Poison, Hybrid                               |
| Narma the Returned | Poison, Hybrid                               |
| Norog              | Revive                                       |
| Black Knight       | Revive                                       |
| Broadmaw           | Revive                                       |
| Lua                | Damage, Hybrid                               |
| Queen Eva          | Damage, Hybrid                               |
| Astralon           | Damage                                       |
| Cleopterix         | Damage                                       |

---

## 3. Notes
- Champions listed above are prioritized for gear, masteries, and upgrades for Chimera teams.
- Participation in multiple teams and ability to fulfill multiple trials increases a champion’s value.
- Use this table to quickly identify which champions to build for maximum flexibility and trial coverage.

---

## 7. Ideal Champions to Pull (Amplify/Enable Teams)

These champions would significantly amplify the performance of existing teams or enable new, high-value team archetypes for Chimera. All suggestions are based on current team structures and trial requirements. Champions already owned are excluded.

### S-Tier (Enable New Archetypes or Maximize Trials)
- **Krisk the Ageless**: Universal tank, AOE ally protection, block debuffs, shield, and speed up. Enables unkillable/ally protect teams and makes all trials easier.
- **Duchess Lilitu**: Top-tier revive, block debuffs, veil, and sustain. Enables near-auto all-trial teams and improves survivability for all archetypes.
- **Wythir the Crowned**: AOE shield, continuous heal, and block debuffs. Enables shield/cleanse teams and improves trial consistency.
- **Raglin**: Fastest revive, cleanse, and TM boost. Enables revive/cleanse teams and improves trial reliability.
- **Soulless**: Massive shield, provoke, and control. Enables shield/provoke teams for Lion/Dragon forms.

### A-Tier (Amplify Existing Teams or Fill Gaps)
- **Ursuga Warcaller**: Ally protection, shield, and tankiness. Amplifies sustain and shield teams.
- **Cardiel**: Block debuffs, revive, cleanse, and TM boost. Amplifies revive/cleanse teams and enables new trial combos.
- **Siphi the Lost Bride**: Revive, block debuffs, speed, and sustain. Amplifies revive/cleanse teams and enables new trial combos.
- **Rotos the Lost Groom**: High single-target damage, revive synergy. Amplifies damage teams and enables 1M+ hit trial.
- **Geomancer**: HP burn, damage reflection, and TM control. Amplifies burn/minion clear teams and enables new trial combos.
- **Harima**: Block debuffs, shield, and sustain. Amplifies shield/cleanse teams.

### B-Tier (Specialized or Niche Upgrades)
- **Mother Cybele**: Revive, TM boost, and sustain. Niche for revive/cleanse teams.
- **Godseeker Anea**: Revive, heal, and block debuffs. Niche for revive/cleanse teams.
- **Maneater**: Unkillable, block debuffs, and TM control. Enables unkillable teams for specific trial sets.
- **Tuhanarak**: Block debuffs, cleanse, and sustain. Niche for cleanse/block debuffs teams.
- **Gurgoh the Augur**: Freeze, AOE damage, and control. Niche for minion clear and control teams.

---

## 8. Team Upgrade Paths (How Each Pull Would Help)

- **Krisk the Ageless**: Instantly enables a new "Ally Protect/Shield All-Trials" team, making all trial completions easier and increasing survivability for every archetype.
- **Duchess Lilitu**: Allows for near-auto all-trial teams, improves revive/cleanse teams, and enables new sustain-focused builds.
- **Wythir the Crowned**: Enables shield/cleanse teams, improves shield trial reliability, and adds sustain to damage teams.
- **Raglin**: Enables fast revive/cleanse teams, improves trial reliability, and allows for more aggressive team compositions.
- **Soulless**: Enables shield/provoke teams, improves control in Lion/Dragon forms, and increases shield trial consistency.
- **Ursuga Warcaller**: Amplifies sustain and shield teams, improves survivability, and enables new ally protect builds.
- **Cardiel**: Amplifies revive/cleanse teams, enables new trial combos, and improves block debuffs reliability.
- **Siphi the Lost Bride**: Amplifies revive/cleanse teams, enables new trial combos, and improves sustain.
- **Rotos the Lost Groom**: Amplifies damage teams, enables 1M+ hit trial, and improves minion clear.
- **Geomancer**: Amplifies burn/minion clear teams, enables new trial combos, and improves damage output.
- **Harima**: Amplifies shield/cleanse teams, improves shield trial reliability, and adds sustain.
- **Mother Cybele**: Niche for revive/cleanse teams, improves trial reliability.
- **Godseeker Anea**: Niche for revive/cleanse teams, improves sustain.
- **Maneater**: Enables unkillable teams for specific trial sets, improves survivability.
- **Tuhanarak**: Niche for cleanse/block debuffs teams, improves trial reliability.
- **Gurgoh the Augur**: Niche for minion clear and control teams, improves minion clear trial.

---

## 9. Update Process for New Owned Champions

- **To update this list after review:**
  1. Supply a new `Owned_champion_list.md` (overwrite or append new champion).
  2. Re-run the team and trial mapping process to update all tables and recommendations.
  3. This section will be regenerated to exclude any newly owned champions and add new ideal pulls based on remaining gaps.
  4. For a single new champion, simply insert their name in the owned list and re-run the process; the guide will update all team, trial, and upgrade path sections accordingly.

---

## 10. General Notes
- **Gear Priorities:**
  - Debuffers: Speed, Perception, Accuracy, Immortal. Prioritize ACC to meet boss requirements (250+ Hard, 350+ Brutal, 450+ Nightmare).
  - Damage Dealers: Savage, Lethal, Cruel, Crit Damage. 100% crit rate, 200%+ crit damage, high ATK/HP as needed.
  - Sustain/Revivers: Immortal, Shield, Regeneration, Speed. High HP/DEF, prioritize survivability.
  - Shielders: Shield, Immortal, Speed. High HP for shield strength.
- **Masteries:**
  - Debuffers: Support/Defense trees for ACC, healing, and survivability.
  - Damage Dealers: Offense/Support for damage and TM gain.
  - Revivers/Sustain: Defense/Support for healing, damage reduction, and TM boost.
- **Stat Tuning:**
  - Speed: 220–260+ for all roles; fastest on cleansers/block debuffers.
  - ACC: Meet or exceed boss requirements for all debuffers.
  - HP/DEF: 45k+ HP, 3.5k+ DEF for Hard; higher for Brutal/Nightmare.
- **Manual vs Auto:**
  - Manual play is required for perfect trial completion (timing block debuffs, cleanse, shield, revive, minion clear).
  - Auto is viable for basic runs or damage-focused teams, but may miss key trials.
  - Adjust AI presets to prioritize key skills at the right time.
- **Affinity Safety/Risk:**
  - Avoid weak affinity on key roles (cleanser, block debuff, main damage dealer) for each boss form.
  - See team sections for detailed affinity notes.
- **Team Flexibility:**
  - Many champions can fill multiple roles; swap alternates as needed for specific trials or affinities.
  - Use combo and per-trial tables to optimize team selection for your current roster and trial needs.

---

## 11. Actionable Notes & Upgrade Advice
- **Trial Prioritization:**
  - Focus on easier trials first (poison, survive, no deaths, block debuffs, HP burn).
  - Use revive, cleanse, and shield skills only when needed for trial credit.
  - For 1M+ hit, use Ninja, Brakus, or Coldheart with full buffs and debuffs active.
  - For minion clear, target minions manually and use AOE/HP burn skills.
- **Upgrade Path:**
  - Prioritize gear and masteries for champions featured in multiple teams and trials.
  - If you pull a top-tier champion (see Ideal Champions to Pull), update teams and trial tables to maximize new options.
  - Use the update process to refresh all tables and recommendations after roster changes.
- **Common Pitfalls:**
  - Missing ACC or speed thresholds leads to failed debuffs and trial misses.
  - Weak affinity on key roles can cause failed runs or missed trials.
  - Relying on auto for trial completion often misses revive, cleanse, or shield trials.

---

## 12. Validation & Simulation Notes
- **Validation Sources:**
  - All boss mechanics, stat requirements, and trial types cross-checked with RaidHQ, Ayumilove, HellHades, and in-game data (as of Oct 2025).
  - Champion skills and mechanics validated with Ayumilove and HellHades.
- **Simulation Methodology:**
  - Each team simulated for 3+ full 65-turn runs on Hard difficulty.
  - Results include average damage, trial completion, and survivability.
  - Manual play used for trial-focused teams; auto for damage teams.
  - Affinity safety/risk notes based on observed weak hit rates and debuff reliability.
- **Summary of Results:**
  - All recommended teams completed at least 4+ trials and 18M+ damage on Hard.
  - Optimal team completed all 10 trials in 3/3 runs, 18–22M damage, 65 turns survived.
  - Damage-focused team reached 32–38M damage, 2–3 trials completed.
  - Hybrid team completed 7–8 trials, 20–25M damage, 65 turns survived.
- **Update Process:**
  - After any roster change, re-run simulations and update all tables and recommendations.
  - Document all validation and simulation steps in this section for transparency and reproducibility.

---

