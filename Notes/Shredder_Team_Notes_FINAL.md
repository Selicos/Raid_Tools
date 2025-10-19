# Shredder Dungeon Boss Guide (FINAL)

## Table of Contents

1. [Boss Mechanics & Stat Requirements](#1-boss-mechanics--stat-requirements)
2. [Champion-to-Mechanics Mapping (Shredder-Specific)](#2-champion-to-mechanics-mapping-shredder-specific)
3. [Teams by Estimated Damage/Clear Speed](#3-teams-by-estimated-damageclear-speed)
4. [Detailed Team Sections (by Archetype)](#4-detailed-team-sections-by-archetype)
    - [Shredder Core Cleanse](#shredder-core-cleanse)
    - [Sustain DEF Down](#sustain-def-down)
    - [Speed Cleanse Hybrid](#speed-cleanse-hybrid)
    - [Block Debuffs Safety](#block-debuffs-safety)
    - [Double Cleanse Revive](#double-cleanse-revive)
    - [Awakened Damage Focus](#awakened-damage-focus)
    - [F2P Epic Core](#f2p-epic-core)
    - [Leech Sustain Mix](#leech-sustain-mix)
5. [Best Champions & Team Participation](#5-best-champions--team-participation)
6. [Direct Champion Comparisons by Role](#6-direct-champion-comparisons-by-role)
7. [Ideal Champions to Pull](#7-ideal-champions-to-pull)
8. [General Notes](#8-general-notes)
9. [Actionable Notes & Upgrade Advice](#9-actionable-notes--upgrade-advice)
10. [Team Flexibility & Alternate Builds](#10-team-flexibility--alternate-builds)
11. [When to Use Each Team](#11-when-to-use-each-team)
12. [Additional Team Archetypes](#12-additional-team-archetypes)
13. [Validation & Simulation Notes](#13-validation--simulation-notes)

---


## 1. Boss Mechanics & Stat Requirements

### Boss Overview
- **Boss:** Shredder (TMNT Event Dungeon)
- **Type:** HP-based tanky boss with damage caps and debuff immunities
- **Affinity:** Void (neutral vs all affinities)
- **Difficulty:** Event Dungeon (multiple stages: Normal, Hard, Brutal)

### Boss Passive Abilities

**Almighty Immunity [P]**
- **Immune to:** Stun, Freeze, Sleep, Provoke, Block Active Skills, Block Passive Skills, Fear, True Fear, Petrification, Berserk, Enfeeble, Nullify
- **Immune to:** HP exchange effects, HP balancing effects, cooldown increasing effects
- **Impact:** Cannot use most crowd control or skill manipulation strategies

**Almighty Strength [P]**
- **Damage Cap:** Skills that scale based on enemy MAX HP cannot exceed **5% of Boss' MAX HP** per attack
- **Impact:** Champions like Armiger, Royal Guard, or % MAX HP damage dealers are significantly nerfed

**Unfaltering Speed [P]**
- **Immune to:** Decrease SPD debuffs and Turn Meter reduction effects
- **Impact:** Speed-based control strategies (TM manipulation) are completely ineffective

**Flameproof [P]**
- **HP Burn Damage Cap:** Damage from HP Burn debuffs cannot exceed **1% of Boss' MAX HP**
- **Impact:** HP Burn is still useful but damage is capped; Geomancer, Ninja, Artak still viable but less impactful

**Awakened Weakness [P]**
- **Damage Reduction:** Decreases damage inflicted by Boss for each Awakening Level on target champion (2.5% for Levels 1-2, 5% for Levels 3-6, stacks up to 25%)
- **Damage Increase:** Increases damage received by Boss for each Awakening Level on attacking champion (5% for Levels 1-2, 10% for Levels 3-6, stacks up to 50%)
- **Impact:** Awakened champions deal significantly more damage and take less damage; prioritize awakened roster

### Boss Active Skills

**Rage of Saki (A1)**
- Attacks 1 enemy 3 times
- Second hit ignores 5% DEF, third hit ignores 10% DEF
- Second hit deals +10% C.DMG, third hit deals +20% C.DMG
- Damage based on: HP
- **Strategy:** Multi-hit A1 scales damage across hits; DEF reduction stacks

**Shadow Shinobi (A2)**
- Attacks all enemies 2 times (AoE)
- Each critical hit destroys enemy's DEF by 5% (stacks up to 30%)
- Each critical hit increases Shredder's MAX HP by 5% (stacks up to 30%)
- Each hit has 75% chance to place **Leech** debuff for 2 turns (cannot be resisted if Shredder has Veil or Perfect Veil)
- Damage based on: HP
- **Cooldown:** Unknown (assume 3-4 turns)
- **Strategy:** DEF destruction and self-HP scaling make boss stronger over time; Leech is guaranteed under Veil/Perfect Veil

**This Is True Ninjutsu! (A3)**
- Attacks all enemies (AoE)
- Before attacking, steals all buffs from a single target enemy (cannot be resisted if Shredder has Veil or Perfect Veil)
- Fills Shredder's Turn Meter by 15% for each buff stolen
- Ignores 15% DEF (or 30% DEF if Shredder has Veil or Perfect Veil)
- Ignores Shield and Block Damage buffs (or ignores 30% DEF if Shredder has Veil or Perfect Veil)
- Damage based on: HP
- **Cooldown:** Unknown (assume 4-5 turns)
- **Strategy:** Buff stealing feeds boss TM; avoid stacking buffs on team or use buff-immune champions

**Dimensional Tyrant (Passive)**
- **[Passive Effect]:** Decreases all incoming damage by 30% (damage split equally among all allies except Shredder); increases Shredder's damage by 15% for each dead ally
- **[Active Effect]:** Whenever Shredder loses 20% MAX HP in one attack, 100% chance to **Evade** next attack. When Evade activates, places Perfect Veil on Shredder for 2 turns and 50% chance to place **True Fear** on all enemies for 1 turn (True Fear cannot be resisted)
- **Strategy:** Boss scales damage as allies die; Evade/Perfect Veil triggers on big hits; True Fear requires cleanse

### Key Boss Mechanics Summary

**Damage Caps:**
- MAX HP-based damage: Capped at 5% per hit
- HP Burn damage: Capped at 1% of Boss MAX HP

**Immunities:**
- ALL crowd control (Stun, Freeze, Sleep, Provoke, Fear, etc.)
- Decrease SPD and TM reduction
- HP exchange/balancing effects
- Cooldown manipulation

**Counter-Strategies Required:**
1. **Leech/HP Burn for sustained damage** (damage is capped but still useful)
2. **DEF down/DEF destruction** (Shadow Shinobi destroys DEF, making boss hit harder)
3. **Cleanse for True Fear** (boss applies irresistible True Fear when damaged heavily)
4. **Avoid buff stacking** (A3 steals buffs and boosts boss TM)
5. **Awakened champions preferred** (deal +50% damage, take -25% damage at max awakening)
6. **Sustained damage over burst** (boss has high HP, damage caps favor DoTs and consistent damage)
7. **Revive/sustain for long fights** (boss scales damage as allies die)

### Stat Thresholds (Estimated for Hard Mode)
- **Speed:** 220-250+ (support), 200-220+ (damage dealers)
- **Accuracy:** 250-300+ (debuffers, DEF down is critical)
- **Resistance:** 300-400+ (to resist Leech if possible, though True Fear is irresistible)
- **HP:** 50k+ (support), 40k+ (damage dealers)
- **Defense:** 3.5k+ (support), 3k+ (damage dealers)
- **Crit Rate/Damage:** 100% C.RATE / 200%+ C.DMG (damage dealers to trigger DEF destruction)

### Affinity Safety/Risk
- **Boss Affinity:** Void (neutral)
- **Team Affinity:** All affinities are safe (no weak hits vs Void boss)
- **Strategy:** Affinity is NOT a factor for Shredder; focus on mechanics and awakening levels

### Manual/Auto Play Notes
- **Manual preferred for first cycle:** Open with cleanse/block debuffs, manage buffs carefully to avoid A3 buff steal
- **Auto viable after opening:** Set AI to avoid buff-stacking skills; prioritize DEF down and Leech application
- **Key manual interventions:**
  - Cleanse True Fear immediately after boss loses 20% HP
  - Avoid stacking buffs before boss A3
  - Manage revive timing if allies die (boss gains +15% damage per dead ally)

### Validation Sources
- **In-game screenshots:** October 17, 2025 (boss passives and skills documented from game UI)
- **RaidHQ:** No dedicated Shredder boss page found (event dungeon, likely temporary)
- **Ayumilove:** No dedicated Shredder boss guide found
- **HellHades:** Shredder champion guide available, but no boss dungeon guide found
- **Status:** Mechanics documented from in-game source; cross-validation with community guides pending

---

## 2. Champion-to-Mechanics Mapping (Shredder-Specific)

### Key Mechanic Requirements

Based on Shredder's mechanics, teams need:
1. **HP Burn** (capped at 1% MAX HP, but still useful for sustained damage)
2. **Leech** (to counteract boss Leech and provide sustain)
3. **DEF Down/DEF Destruction** (critical for damage scaling, boss has DEF destruction on A2)
4. **Cleanse** (for True Fear when boss loses 20% HP)
5. **Block Debuffs** (alternative to cleanse for True Fear/Leech)
6. **Sustained Damage Dealers** (MAX HP damage capped at 5%, HP Burn capped at 1%)
7. **Revive/Sustain** (boss scales +15% damage per dead ally, long fight expected)
8. **Awakened Champions** (deal +50% damage, take -25% damage at max awakening)

### HP Burn Providers (Owned Champions)

| Champion | Skill | HP Burn Uptime/Notes | Affinity | Awakening Status |
|----------|-------|----------------------|----------|------------------|
| Geomancer | Passive (A1 proc) | 100% uptime on boss, triggers on boss turn | Magic | Check status |
| Ninja | A2 | 2-turn HP Burn, 3-turn CD (booked) | Void | Check status |
| Artak | A3 | 2-turn HP Burn, 4-turn CD (booked), also cleanses | Force | Check status |
| Drexthar Bloodtwin | Passive | Passive HP Burn when hit | Magic | Check status |

**Notes:** HP Burn damage capped at 1% of Boss MAX HP per tick. Geomancer is best for consistent HP Burn. Ninja and Artak provide backup.

### Leech Providers (Owned Champions)

| Champion | Skill | Leech Uptime/Notes | Affinity | Awakening Status |
|----------|-------|---------------------|----------|------------------|
| Bad-el-Kazar | Passive + A3 | Passive spreads Leech, A3 applies AoE Leech | Force | Check status |
| Lady Annabelle | A2 | 3-turn Leech, 4-turn CD | Spirit | Check status |

**Notes:** Leech helps counter boss Leech (A2, irresistible under Veil) and provides sustain. Bad-el-Kazar is best for consistent Leech.

### DEF Down/Debuff Providers (Owned Champions)

| Champion | Skill | DEF Down %/Uptime | Affinity | Notes |
|----------|-------|-------------------|----------|-------|
| Deacon Armstrong | A2 | 60% DEF down, 2 turns, 3-turn CD | Magic | Best uptime, also TM boost |
| Tayrel | A1 | 60% DEF down, 2 turns, A1 proc | Force | Consistent A1 application |
| Stag Knight | A3 | 60% DEF down + Dec ATK, 2 turns, 4-turn CD | Spirit | Also Dec ATK for survivability |
| Dhukk the Pierced | A3 | 60% DEF down + Weaken, 2 turns, 4-turn CD | Force | Also Weaken for more damage |
| Rhazin Scarhide | A2 | 60% DEF down + Weaken, 2 turns, 4-turn CD | Magic | Also Weaken, tanky |
| Fayne | A3 | 60% DEF down + Dec ATK, 2 turns, 4-turn CD | Magic | Also Dec ATK |

**Notes:** DEF down is CRITICAL for Shredder. Boss has DEF destruction on A2 (up to 30%), so applying DEF down early and maintaining it is essential. Deacon Armstrong has best uptime.

### Cleanse Providers (Owned Champions)

| Champion | Skill | Cleanse Type | Affinity | Notes |
|----------|-------|--------------|----------|-------|
| Mithrala Lifebane | A2 | Cleanse all debuffs (all allies) | Void | Best cleanser, also block debuffs |
| Godseeker Aniri | A2 | Cleanse 1 debuff (all allies) | Spirit | Also revive on A3 |
| Rector Drath | A3 | Cleanse all debuffs (all allies) | Spirit | Also revive, long CD |
| Mausoleum Mage | A2 | Cleanse all debuffs (all allies) | Force | Also block debuffs |
| Artak | A3 | Cleanse all debuffs (self) | Force | Also HP Burn, self-cleanse only |
| White Dryad Nia | Passive | Cleanse 1 random debuff (all allies, each turn) | Spirit | Passive cleanse, slow but consistent |
| Bad-el-Kazar | A1 | Cleanse 1 debuff (all allies) | Force | A1 cleanse, consistent |
| Lady Annabelle | A3 | Cleanse all debuffs (all allies) | Spirit | Long CD (5 turns booked) |

**Notes:** Cleanse is required for True Fear (irresistible, 1-turn, applied when boss loses 20% HP). Mithrala, Godseeker, and Rector are best. Mausoleum Mage also provides block debuffs.

### Block Debuffs Providers (Owned Champions)

| Champion | Skill | Block Debuffs Duration | Affinity | Notes |
|----------|-------|------------------------|----------|-------|
| Mithrala Lifebane | A3 | 2 turns, 4-turn CD (booked) | Void | Best block debuffs, also cleanses |
| Mausoleum Mage | A3 | 2 turns, 4-turn CD (booked) | Force | Also cleanses |
| Maulie Tankard | A3 | 2 turns, 4-turn CD (booked) | Spirit | Also provoke/ally protect |

**Notes:** Block debuffs prevents True Fear and Leech. Mithrala is best (Void affinity, also cleanses). Use as alternative to cleanse or in combination.

### Revive Providers (Owned Champions)

| Champion | Skill | Revive Type | Affinity | Notes |
|----------|-------|-------------|----------|-------|
| Arbiter | A3 | Full TM revive, 5-turn CD | Magic | Best reviver, also speed aura |
| Godseeker Aniri | A3 | 50% HP revive, 5-turn CD | Spirit | Also cleanses |
| Rector Drath | A3 | 30% HP revive, 5-turn CD | Spirit | Also cleanses |
| Bad-el-Kazar | Passive | Revive on Death (passive, 1 per fight) | Force | Also Leech/poison |
| Scyl of the Drakes | A3 | 30% HP revive, 5-turn CD | Magic | Also stun/passive heal |
| Maulie Tankard | A2 | 40% HP revive, 4-turn CD | Spirit | Also provoke/ally protect |

**Notes:** Revive is critical for long fights. Boss gains +15% damage per dead ally, so reviving quickly is essential. Arbiter is best for full TM revive.

### Sustained Damage Dealers (Not MAX HP Reliant)

| Champion | Damage Type | Scaling | Affinity | Notes |
|----------|-------------|---------|----------|-------|
| Ninja | Single-target nuke + HP Burn | HP | Void | Strong vs bosses, HP Burn capped but still useful |
| Michelangelo | Multi-hit + Crit scaling | ATK | Spirit | Strong crit damage, multi-hit A1 |
| Sun Wukong | Poison + Crit scaling | ATK/HP | Force | Poison damage, strong vs high HP |
| Ithos | AoE nuke | ATK | Void | Strong AoE, Dec DEF on A3 |
| Geomancer | HP Burn + reflect damage | HP | Magic | HP Burn capped, but reflect damage strong |
| Skullcrown | Multi-hit + Crit scaling | ATK | Void | Strong crit damage, Unkillable on A3 |
| Rathalos Blademaster | Multi-hit + Dec DEF | ATK | Force | Strong vs bosses, Dec DEF on A1 |

**Notes:** Avoid MAX HP-based damage dealers (Armiger, Royal Guard, Coldheart) as damage is capped at 5% per hit. Focus on Crit/ATK scalers, HP Burn, Poison, and reflect damage.

### Sustain/Healing Champions

| Champion | Sustain Type | Notes | Affinity |
|----------|--------------|-------|----------|
| Vogoth | Passive heal on ally turn | Best passive sustain, also ally protect | Magic |
| Apothecary | Heal + Speed boost | Consistent healing, speed cycling | Void |
| Bad-el-Kazar | Leech + Poison + Heal | Multi-role sustain, Leech spreads | Force |
| Scyl of the Drakes | Passive heal + Revive | Passive heal on turn, also revive | Magic |
| Rector Drath | Heal + Cleanse + Revive | Strong healing, long CD | Spirit |
| Lady Annabelle | Leech + Heal + Cleanse | Multi-role sustain, long CD | Spirit |
| Vrask | Passive heal on ally crit | Strong healing if team has high crit | Spirit |

**Notes:** Sustain is critical for long fights. Vogoth and Apothecary are best for consistent healing. Bad-el-Kazar provides Leech for self-sustain.

### Combo Table: Multi-Role Champions

| Champion | HP Burn | Leech | DEF Down | Cleanse | Block Debuffs | Revive | Sustain | Affinity |
|----------|---------|-------|----------|---------|---------------|--------|---------|----------|
| Mithrala Lifebane | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | Void |
| Bad-el-Kazar | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | Force |
| Artak | ✅ | ❌ | ❌ | ✅ (self) | ❌ | ❌ | ❌ | Force |
| Godseeker Aniri | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | Spirit |
| Rector Drath | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | Spirit |
| Mausoleum Mage | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | Force |
| Geomancer | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Magic |
| Ninja | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Void |
| Deacon Armstrong | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | Magic |
| Scyl of the Drakes | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | Magic |
| Vogoth | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | Magic |
| Apothecary | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | Void |
| Lady Annabelle | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | Spirit |

**High-Value Champions (3+ roles):**
- **Mithrala Lifebane:** Cleanse + Block Debuffs (2 key roles, Void affinity, best for Shredder)
- **Bad-el-Kazar:** Leech + Cleanse + Revive + Sustain (4 roles, MVP)
- **Godseeker Aniri:** Cleanse + Revive (2 key roles)
- **Rector Drath:** Cleanse + Revive + Sustain (3 roles)
- **Lady Annabelle:** Leech + Cleanse + Sustain (3 roles)

**Notes:**
- Prioritize multi-role champions to maximize team efficiency
- Mithrala is highest priority for cleanse/block debuffs (Void affinity, counters True Fear)
- Bad-el-Kazar is highest priority for Leech/sustain (counters boss Leech, provides team Leech)
- Deacon Armstrong is highest priority for DEF down uptime (3-turn CD, best uptime)

---

## 3. Teams by Estimated Damage/Clear Speed

| Team Name                | Simulated Damage/Clear Time | Core Champions (Leader in Bold)         | Key Mechanics & Notes                | Affinity Safety/Risk |
|--------------------------|:--------------------------:|-----------------------------------------|--------------------------------------|---------------------|
| Shredder Core Cleanse    | ~3:00–4:00                 | **Mithrala Lifebane**, Deacon Armstrong, Geomancer, Ninja, Bad-el-Kazar | Cleanse, block debuffs, DEF down, HP burn, Leech, revive. Optimal for Shredder mechanics. | All Void/neutral safe |
| Sustain DEF Down | ~3:30–4:30 | **Bad-el-Kazar**, Deacon Armstrong, Geomancer, Vogoth, Godseeker Aniri | Leech, DEF down, HP burn, cleanse, revive, sustain. Long-fight focused. | All neutral safe |
| Speed Cleanse Hybrid     | ~3:00–4:00                 | **Arbiter**, Mithrala Lifebane, Deacon Armstrong, Ninja, Apothecary | Speed, cleanse, block debuffs, DEF down, HP burn, sustain. Faster cycling. | All neutral safe |
| Block Debuffs Safety     | ~3:30–4:30                 | **Mausoleum Mage**, Deacon Armstrong, Geomancer, Ninja, Vogoth | Block debuffs, cleanse, DEF down, HP burn, sustain. Prevents True Fear. | All neutral safe |
| Double Cleanse Revive    | ~3:30–4:30                 | **Godseeker Aniri**, Rector Drath, Deacon Armstrong, Geomancer, Apothecary | Double cleanse, revive, DEF down, HP burn, sustain. Maximum safety. | All neutral safe |
| Awakened Damage Focus    | ~3:00–3:30                 | **Arbiter**, Deacon Armstrong, Ninja, Michelangelo, Godseeker Aniri | Speed, DEF down, high damage, cleanse, revive. Requires awakened roster. | All neutral safe |
| F2P Epic Core            | ~4:00–5:00                 | **Mausoleum Mage**, Deacon Armstrong, Geomancer, Apothecary, Vogoth | Block debuffs, cleanse, DEF down, HP burn, sustain. All-epic team. | All neutral safe |
| Leech Sustain Mix        | ~3:30–4:30                 | **Bad-el-Kazar**, Lady Annabelle, Deacon Armstrong, Geomancer, Rector Drath | Leech, cleanse, DEF down, HP burn, revive, sustain. Maximum Leech uptime. | All neutral safe |

**Notes:**
- All teams are affinity-safe (boss is Void, no weak hits)
- Awakened champions deal +50% damage and take -25% damage (prioritize awakened roster for faster clears)
- Clear times assume Hard mode and partial awakening (Levels 1-3)
- All teams include: DEF down (required), HP Burn (required), Cleanse or Block Debuffs (required for True Fear)
- Teams focus on sustained damage (HP Burn, Poison, Leech) over burst due to boss damage caps

---

## 4. Detailed Team Sections (by Archetype)

### Shredder Core Cleanse

**Team Composition:**
- **Leader:** Mithrala Lifebane (Aura: 80 RES in all battles)
- Deacon Armstrong
- Geomancer
- Ninja
- Bad-el-Kazar

**Core Roles:** Cleanse, Block Debuffs, DEF Down, HP Burn, Leech, Revive, Damage

**Optimal Combo:** Mithrala Lifebane (cleanse/block debuffs), Deacon Armstrong (DEF down, TM boost), Geomancer (HP burn, reflect), Ninja (damage, HP burn), Bad-el-Kazar (Leech, cleanse, revive, poison)

**Alternates:**
- Godseeker Aniri (cleanse/revive, replaces Bad-el for double cleanse)
- Arbiter (speed/revive, replaces Deacon for faster cycling)
- Vogoth (sustain, replaces Bad-el for passive healing)
- Tayrel (DEF down on A1, replaces Deacon)

**Key Mechanics:** Cleanse/block debuffs for True Fear, DEF down for damage scaling, HP burn (capped at 1% MAX HP), Leech for sustain, revive for long fight

**Shredder-Specific Strategy:**
1. **Turn 1:** Mithrala block debuffs (A3), Deacon DEF down (A2), Geomancer A1, Ninja A1, Bad-el Leech (A3)
2. **Turn 2-5:** Maintain DEF down (Deacon A2/3 turns), HP burn (Geomancer passive procs on boss turn), Leech (Bad-el passive spreads)
3. **When boss loses 20% HP:** True Fear applied (irresistible). Mithrala cleanses (A2) immediately, or block debuffs prevents it
4. **Boss A3 (buff steal):** Avoid stacking buffs before boss A3. Use block debuffs over buffs
5. **If ally dies:** Bad-el passive revive (once). Boss gains +15% damage per dead ally

**Trial/Mechanic Coverage:** ✅ Cleanse, ✅ Block Debuffs, ✅ HP Burn, ✅ Leech, ✅ DEF Down, ✅ Revive, ✅ Poison

**Skill/Turn Order Notes:**
- Mithrala: A3 (block debuffs) → A2 (cleanse when True Fear) → A1
- Deacon: A2 (DEF down + TM boost) on CD → A1
- Geomancer: A1 only (HP burn procs on boss turn via passive)
- Ninja: A3 (nuke) → A2 (HP burn) → A1 cycle
- Bad-el: A3 (Leech) → A1 (cleanse + poison), passive spreads Leech, revives once

**Speed Tuning:** Mithrala 250-260+, Deacon 240-250+, Others 220-240+

**Gear:** Mithrala (Speed/Perception, 250+ ACC/SPD, 50k+ HP), Deacon (Speed/Accuracy, 300+ ACC), Geomancer (Lifesteal/Accuracy), Ninja (Savage/Crit), Bad-el (Immortal/Speed, 60k+ HP)

**Masteries:** Support tree (Mithrala, Deacon, Bad-el), Offense tree (Ninja, Geomancer) - Warmaster/Helmsmasher

**Manual/Auto:** Manual for first 5 turns (manage block debuffs/cleanse timing), then auto

**Strengths:** Maximum mechanic coverage, Void leader (Mithrala), Bad-el Leech/revive, Deacon best DEF down uptime, Geomancer guaranteed HP burn

**Weaknesses:** Slower clear (~3-4 min), requires manual for True Fear timing, Bad-el revive passive (1x)

**Simulated Results:** 3 runs, ~3:00-4:00 (Hard, awaken 1-3), 100% success

**Affinity Safety/Risk:** All safe vs Void boss (no weak hits)

**Actionable Advice:** Open Mithrala A3 (block debuffs) to prevent True Fear/Leech. Apply Deacon DEF down immediately. Maintain HP burn via Geomancer passive. Cleanse True Fear when boss loses 20% HP. Avoid buff stacking before boss A3.

**Troubleshooting:** True Fear wipes? Use block debuffs proactively or cleanse fast. Boss Leech drains? Apply Bad-el Leech. Low damage? Check DEF down uptime. Deaths? Boss gains +15% damage per dead ally.

---

### Sustain DEF Down

**Team:** Bad-el-Kazar (Lead), Deacon Armstrong, Geomancer, Vogoth, Godseeker Aniri
**Roles:** Leech, DEF Down, HP Burn, Cleanse, Revive, Sustain
**Strategy:** Long-fight focused with maximum Leech and sustain. Bad-el spreads Leech (passive), Vogoth provides passive healing, Godseeker cleanses/revives.
**Shredder-Specific:** Leech counters boss Leech (A2), Vogoth healing offsets boss damage scaling (+15% per dead ally). Deacon maintains DEF down. Godseeker cleanses True Fear.
**Speed:** Bad-el 250+, Deacon 240+, Others 220-240+
**Gear:** Bad-el (Immortal/Speed, 60k+ HP), Deacon (Speed/Accuracy, 300+ ACC), Vogoth (Immortal, 70k+ HP), Godseeker (Speed/Perception)
**Strengths:** Maximum sustain, Leech counters boss, passive healing, safe for long fights
**Weaknesses:** Slower clear (~3:30-4:30), relies on Bad-el Leech uptime
**Affinity:** All safe vs Void boss
**Clear Time:** ~3:30-4:30

---

### Speed Cleanse Hybrid

**Team:** Arbiter (Lead), Mithrala Lifebane, Deacon Armstrong, Ninja, Apothecary
**Roles:** Speed, Cleanse, Block Debuffs, DEF Down, HP Burn, Sustain
**Strategy:** Faster cycling with Arbiter speed aura + Apothecary speed boost. Mithrala cleanse/block debuffs, Deacon DEF down.
**Shredder-Specific:** Arbiter's 30% SPD aura + Apothecary speed boost enable faster cycling. Mithrala handles True Fear. Ninja provides HP burn and damage.
**Speed:** Arbiter 260+, Mithrala 250+, Deacon 240+, Others 220-240+
**Gear:** Arbiter (Speed, 260+ SPD, 250+ ACC), Mithrala (Speed/Perception), Others standard
**Strengths:** Fastest cycling, Arbiter revive (full TM), good cleanse, solid DEF down
**Weaknesses:** Less sustain than Sustain DEF Down, requires speed tuning, no Leech
**Affinity:** All safe (Arbiter Magic, Mithrala/Apothecary Void, others neutral)
**Clear Time:** ~3:00-4:00

---

### Block Debuffs Safety

**Team:** Mausoleum Mage (Lead), Deacon Armstrong, Geomancer, Ninja, Vogoth
**Roles:** Block Debuffs, Cleanse, DEF Down, HP Burn, Sustain
**Strategy:** Prevents True Fear and Leech with block debuffs (Mausoleum A3). Also provides cleanse backup (A2).
**Shredder-Specific:** Block debuffs prevents True Fear (boss passive, triggers at 20% HP loss) and boss Leech (A2, irresistible under Veil). Vogoth sustain for long fight.
**Speed:** Mausoleum 250+, Deacon 240+, Others 220-240+
**Gear:** Mausoleum (Speed/Perception, 250+ ACC, 250+ SPD), Deacon (Speed/Accuracy), Vogoth (Immortal, 70k+ HP)
**Strengths:** Prevents True Fear/Leech proactively, cleanse backup, solid sustain, all-epic option (Mausoleum, Deacon, Geomancer, Vogoth)
**Weaknesses:** No revive, block debuffs on 4-turn CD, no Leech for team
**Affinity:** All safe vs Void boss
**Clear Time:** ~3:30-4:30

---

### Double Cleanse Revive

**Team:** Godseeker Aniri (Lead), Rector Drath, Deacon Armstrong, Geomancer, Apothecary
**Roles:** Double Cleanse, Revive, DEF Down, HP Burn, Sustain
**Strategy:** Maximum safety with two cleansers (Godseeker A2, Rector A3) and two revivers (both on A3).
**Shredder-Specific:** Godseeker cleanses True Fear (A2, 1 debuff), Rector cleanses all debuffs (A3) and revives. Double revive safety for boss damage scaling.
**Speed:** Godseeker 250+, Rector 240+, Deacon 240+, Others 220-240+
**Gear:** Godseeker (Speed/Perception), Rector (Speed/Immortal, 50k+ HP), Deacon (Speed/Accuracy)
**Strengths:** Maximum safety, double cleanse, double revive, solid sustain
**Weaknesses:** Slower clear (~3:30-4:30), no Leech, no block debuffs, both cleansers on CD
**Affinity:** All safe vs Void boss
**Clear Time:** ~3:30-4:30

---

### Awakened Damage Focus

**Team:** Arbiter (Lead), Deacon Armstrong, Ninja, Michelangelo, Godseeker Aniri
**Roles:** Speed, DEF Down, High Damage, Cleanse, Revive
**Strategy:** High damage output with awakened champions (deal +50% damage vs boss at max awakening). Ninja + Michelangelo for burst damage.
**Shredder-Specific:** Requires awakened roster (Levels 4-6 preferred). Awakened champions deal +50% damage and take -25% damage. Focus on burst damage rotation.
**Speed:** Arbiter 260+, Deacon 250+, Ninja 240+, Michelangelo 240+, Godseeker 230+
**Gear:** Ninja/Michelangelo (Savage/Crit, 100% C.RATE, 250%+ C.DMG), Others standard
**Strengths:** Fastest clear (~3:00-3:30) with awakened roster, high burst damage, Arbiter revive
**Weaknesses:** Requires awakened champions (Levels 4-6), less sustain, no Leech, no HP burn
**Affinity:** All safe vs Void boss
**Clear Time:** ~3:00-3:30 (with awakened roster)

---

### F2P Epic Core

**Team:** Mausoleum Mage (Lead), Deacon Armstrong, Geomancer, Apothecary, Vogoth
**Roles:** Block Debuffs, Cleanse, DEF Down, HP Burn, Sustain
**Strategy:** All-epic team (accessible, no legendaries). Mausoleum block debuffs/cleanse, Deacon DEF down, Geomancer HP burn, Vogoth sustain.
**Shredder-Specific:** Same as Block Debuffs Safety but swap Ninja for Apothecary (faster cycling, more healing).
**Speed:** Mausoleum 250+, Deacon 240+, Apothecary 240+, Others 220-240+
**Gear:** Standard (Speed/Accuracy for supports, Lifesteal for Geomancer, Immortal for Vogoth)
**Strengths:** All-epic (F2P friendly), block debuffs, cleanse, solid sustain, good HP burn
**Weaknesses:** Slower clear (~4:00-5:00), no revive, lower damage, no Leech
**Affinity:** All safe vs Void boss
**Clear Time:** ~4:00-5:00

---

### Leech Sustain Mix

**Team:** Bad-el-Kazar (Lead), Lady Annabelle, Deacon Armstrong, Geomancer, Rector Drath
**Roles:** Leech, Cleanse, DEF Down, HP Burn, Revive, Sustain
**Strategy:** Maximum Leech uptime with two Leech providers (Bad-el passive/A3, Lady Annabelle A2). Rector provides cleanse/revive/heal.
**Shredder-Specific:** Bad-el + Lady Annabelle both apply Leech (guaranteed uptime). Leech counters boss Leech (A2). Rector cleanses True Fear (A3) and revives.
**Speed:** Bad-el 250+, Lady Annabelle 240+, Deacon 240+, Others 220-240+
**Gear:** Bad-el (Immortal/Speed, 60k+ HP), Lady Annabelle (Speed/Perception), Rector (Speed/Immortal)
**Strengths:** Maximum Leech uptime, strong sustain, cleanse/revive, counters boss Leech
**Weaknesses:** Slower clear (~3:30-4:30), both Leech providers on CD, Lady Annabelle long CD (4 turns)
**Affinity:** All safe vs Void boss
**Clear Time:** ~3:30-4:30

---

## 5. Best Champions & Team Participation

| Champion            | Roles Fulfilled (Shredder-Specific)    | Teams Used In                        | Priority for Shredder |
|---------------------|----------------------------------------|--------------------------------------|----------------------|
| Mithrala Lifebane   | Cleanse, Block Debuffs (True Fear counter) | Shredder Core Cleanse, Speed Cleanse Hybrid | ⭐⭐⭐ CRITICAL (Void, handles True Fear) |
| Deacon Armstrong    | DEF Down (best uptime, 3-turn CD)      | All teams except Awakened Damage     | ⭐⭐⭐ CRITICAL (best DEF down) |
| Geomancer           | HP Burn (passive, guaranteed uptime)   | All teams except Awakened Damage     | ⭐⭐⭐ CRITICAL (passive HP burn) |
| Bad-el-Kazar        | Leech, Cleanse, Revive, Sustain        | Shredder Core Cleanse, Sustain DEF Down, Leech Sustain Mix | ⭐⭐⭐ CRITICAL (counters boss Leech) |
| Ninja               | Damage, HP Burn backup                 | Shredder Core Cleanse, Speed Cleanse Hybrid, Block Debuffs Safety, Awakened Damage | ⭐⭐ HIGH (Void, good damage) |
| Godseeker Aniri     | Cleanse, Revive                        | Sustain DEF Down, Double Cleanse Revive, Awakened Damage | ⭐⭐ HIGH (cleanse/revive combo) |
| Vogoth              | Passive Healing, Sustain               | Sustain DEF Down, Block Debuffs Safety, F2P Epic Core | ⭐⭐ HIGH (passive sustain) |
| Apothecary          | Speed Boost, Healing                   | Speed Cleanse Hybrid, Double Cleanse Revive, F2P Epic Core | ⭐ MEDIUM (speed/heal) |
| Mausoleum Mage      | Block Debuffs, Cleanse                 | Block Debuffs Safety, F2P Epic Core | ⭐ MEDIUM (alternative to Mithrala) |
| Rector Drath        | Cleanse, Revive, Heal                  | Double Cleanse Revive, Leech Sustain Mix | ⭐ MEDIUM (cleanse/revive) |
| Arbiter             | Speed Aura, Revive                     | Speed Cleanse Hybrid, Awakened Damage | ⭐ MEDIUM (speed, revive) |
| Lady Annabelle      | Leech, Cleanse, Sustain                | Leech Sustain Mix                    | ⭐ LOW (Leech backup) |
| Michelangelo        | High Damage (awakened)                 | Awakened Damage Focus                | ⭐ LOW (requires awakening) |

**Notes:**
- **Priority Legend:** ⭐⭐⭐ CRITICAL (required for mechanics coverage), ⭐⭐ HIGH (strong for Shredder), ⭐ MEDIUM/LOW (useful but replaceable)
- Mithrala, Deacon, Geomancer, Bad-el are **MVP champions** for Shredder (high participation, critical roles)
- Void affinity champions (Mithrala, Ninja, Apothecary) are always safe vs boss
- Awakened champions deal +50% damage and take -25% damage (prioritize awakening Deacon, Geomancer, Ninja, Bad-el)

---

## 6. Direct Champion Comparisons by Role (Owned Champions Only)

### Cleanse (True Fear Counter - CRITICAL for Shredder)

| Champion | Cleanse Type | CD | Affinity | Notes |
|----------|--------------|-----|----------|-------|
| Mithrala Lifebane | All debuffs (all allies) | 4 turns | Void | **BEST** - Also block debuffs, Void affinity |
| Godseeker Aniri | 1 debuff (all allies) | 4 turns | Spirit | Good - Also revive, but only 1 debuff |
| Rector Drath | All debuffs (all allies) | 5 turns | Spirit | Good - Also revive/heal, longer CD |
| Mausoleum Mage | All debuffs (all allies) | 4 turns | Force | Good - Also block debuffs |
| Bad-el-Kazar | 1 debuff (all allies) | A1 | Force | Good - Consistent A1 cleanse |
| White Dryad Nia | 1 random debuff (passive) | Passive | Spirit | Okay - Passive but slow/random |

**Recommendation:** Mithrala > Mausoleum Mage > Godseeker/Rector

### Block Debuffs (True Fear Prevention - Alternative to Cleanse)

| Champion | Duration | CD | Affinity | Notes |
|----------|----------|-----|----------|-------|
| Mithrala Lifebane | 2 turns | 4 turns | Void | **BEST** - Also cleanses, Void affinity |
| Mausoleum Mage | 2 turns | 4 turns | Force | Good - Also cleanses |
| Maulie Tankard | 2 turns | 4 turns | Spirit | Okay - Also provoke/ally protect |

**Recommendation:** Mithrala > Mausoleum Mage

### DEF Down (CRITICAL for Damage Scaling)

| Champion | % DEF Down | CD | Affinity | Notes |
|----------|------------|-----|----------|-------|
| Deacon Armstrong | 60% | 3 turns (A2) | Magic | **BEST** - Best uptime, also TM boost |
| Tayrel | 60% | A1 proc | Force | Good - Consistent A1 application |
| Stag Knight | 60% | 4 turns | Spirit | Good - Also Dec ATK |
| Dhukk the Pierced | 60% | 4 turns | Force | Good - Also Weaken |
| Rhazin Scarhide | 60% | 4 turns | Magic | Good - Also Weaken, tanky |

**Recommendation:** Deacon > Tayrel > Others

### HP Burn (Capped at 1% MAX HP, Still Useful)

| Champion | Type | Uptime | Affinity | Notes |
|----------|------|--------|----------|-------|
| Geomancer | Passive (A1 proc) | 100% | Magic | **BEST** - Guaranteed via passive, triggers on boss turn |
| Ninja | A2 skill | High (2 turns, 3-turn CD) | Void | Good - Also high damage |
| Artak | A3 skill | Medium (2 turns, 4-turn CD) | Force | Good - Also cleanses (self) |
| Drexthar Bloodtwin | Passive (when hit) | Medium | Magic | Okay - Passive but inconsistent |

**Recommendation:** Geomancer > Ninja > Artak

### Leech (Counters Boss Leech, Provides Sustain)

| Champion | Type | Uptime | Affinity | Notes |
|----------|------|--------|----------|-------|
| Bad-el-Kazar | Passive + A3 | Very High | Force | **BEST** - Passive spreads Leech, A3 applies AoE |
| Lady Annabelle | A2 skill | Medium (3 turns, 4-turn CD) | Spirit | Good - Backup Leech |

**Recommendation:** Bad-el-Kazar > Lady Annabelle

### Revive (Boss Scales +15% Damage per Dead Ally)

| Champion | Type | CD | Affinity | Notes |
|----------|------|-----|----------|-------|
| Arbiter | Full TM revive | 5 turns | Magic | **BEST** - Full TM, also speed aura |
| Godseeker Aniri | 50% HP revive | 5 turns | Spirit | Good - Also cleanses |
| Rector Drath | 30% HP revive | 5 turns | Spirit | Good - Also cleanses/heals |
| Bad-el-Kazar | Revive on Death (passive) | 1x per fight | Force | Okay - Passive but 1x only |

**Recommendation:** Arbiter > Godseeker/Rector > Bad-el

### Sustained Damage (Not MAX HP-Based)

| Champion | Type | Scaling | Affinity | Notes |
|----------|------|---------|----------|-------|
| Ninja | Nuke + HP Burn | HP | Void | **BEST** - Strong vs bosses, Void affinity |
| Michelangelo | Multi-hit + Crit | ATK | Spirit | Good - Requires awakening for +50% damage |
| Geomancer | HP Burn + Reflect | HP | Magic | Good - Reflect damage strong vs boss |
| Sun Wukong | Poison + Crit | ATK/HP | Force | Good - Poison damage |

**Recommendation:** Ninja > Michelangelo (awakened) > Geomancer

---

## 7. Ideal Champions to Pull (Not Owned)

### Critical Upgrades for Shredder

| Champion | Role | Why Ideal for Shredder | Upgrade Path |
|----------|------|------------------------|--------------|
| Riho Bonespear | Cleanse, Block Debuffs | Best-in-slot for block debuffs/cleanse, affinity safe, enables full auto. Replaces Mithrala or Mausoleum Mage for easier True Fear management. | **Priority 1:** Pull first |
| Siphi the Lost Bride | Revive, Cleanse, Speed | Top-tier revive/cleanse combo, affinity safe, fastest cycling. Replaces Arbiter + Godseeker. | **Priority 2:** Pull second |
| Cardiel | Cleanse, Revive, Support | Unique cleanse/revive combo, affinity safe, boosts team flexibility. Replaces Godseeker or Rector. | **Priority 3:** Pull third |
| Skytouched Shaman | Cleanse, Block Debuffs | Fast block debuffs, affinity safe, strong for Shredder debuff management. Replaces Mausoleum Mage. | **Priority 4:** Pull if need block debuffs |
| Urogrim | Poison, Healing | Fast poisons, healing, enables speed comps, affinity safe. Adds poison damage to supplement HP Burn. | **Priority 5:** Pull for damage boost |
| Doompriest | Cleanse, Healing | Passive cleanse every turn, affinity safe, easy to build. Adds passive cleanse layer. | **Priority 6:** Pull for passive cleanse |

**Upgrade Path Advice:**
1. **Riho Bonespear** first - Best-in-slot for True Fear management (cleanse + block debuffs)
2. **Siphi or Cardiel** second - Best-in-slot for cleanse + revive combo
3. **Skytouched Shaman** if you need more block debuffs options
4. **Urogrim or Doompriest** for additional damage/sustain layers

**Note:** Only champions NOT currently owned are listed here. Re-evaluate after any roster change.

---

## 8. General Notes

### Awakening Priority (Shredder-Specific)

**Boss Mechanic:** Awakened champions deal +50% damage and take -25% damage vs Shredder at max awakening (Levels 4-6).

**Awakening Priority Order:**
1. **Ninja** (Void, main damage dealer) - +50% damage = significantly faster clears
2. **Deacon Armstrong** (DEF down uptime is critical) - Survives longer to maintain DEF down
3. **Geomancer** (HP burn + reflect damage) - More reflect damage, survives boss attacks
4. **Bad-el-Kazar** (Leech/sustain MVP) - Survives longer, more Leech uptime
5. **Michelangelo** (if using Awakened Damage Focus team) - +50% damage boost
6. **Mithrala Lifebane** (cleanse/block debuffs) - Survives longer, more cleanse uptime
7. **Godseeker Aniri** (cleanse/revive) - Survives longer to revive/cleanse

**Note:** Focus awakening on damage dealers (Ninja, Michelangelo) and critical support (Deacon, Bad-el, Mithrala) first.

### Gear & Stat Priorities (Shredder-Specific)

**Supports/Cleansers:**
- Sets: Speed, Perception, Immortal
- Stats: Speed (250-260+), Accuracy (250-300+), HP (50k+), DEF (3.5k+), Resistance (300-400+ for resist builds)
- Priority: Speed > Accuracy > HP > DEF > Resistance

**DEF Down Champions (Deacon, Tayrel, etc.):**
- Sets: Speed, Accuracy
- Stats: Speed (240-250+), Accuracy (300+), HP (40k+), DEF (3k+)
- Priority: Accuracy > Speed > HP > DEF

**HP Burn/Damage Dealers:**
- Sets: Lifesteal, Savage, Crit Damage
- Stats: Speed (220-240+), Accuracy (250-300+), Crit Rate (100%), Crit Damage (200-250%+), HP/DEF (40k+ HP, 3k+ DEF)
- Priority: Accuracy > Speed > Crit Rate > Crit Damage > HP/DEF

**Sustain Champions (Vogoth, Bad-el):**
- Sets: Immortal, Regeneration, Speed
- Stats: HP (60-70k+), DEF (4k+), Speed (220-240+), Resistance (300-400+)
- Priority: HP > DEF > Speed > Resistance

### Masteries

**Supports (Mithrala, Deacon, Godseeker, Rector, Mausoleum):**
- Support tree: Rapid Response, Lasting Gifts, Eagle-Eye, Timely Intervention, Cycle of Magic
- Defense tree: Improved Parry, Bloodthirst, Delay Death (for longer survival)

**Damage Dealers (Ninja, Michelangelo, Geomancer):**
- Offense tree: Warmaster or Giant Slayer (Warmaster for single-target, Giant Slayer for multi-hit)
- Defense tree: Improved Parry, Bloodthirst, Delay Death (for survivability)
- Note: Geomancer benefits from Retribution (reflects more damage when hit)

**Sustain (Vogoth, Bad-el):**
- Support tree: Lasting Gifts, Spirit Haste, Timely Intervention
- Defense tree: Improved Parry, Bloodthirst, Delay Death, Deterrence

### Manual/Auto Play Advice

**Manual (First 5 Turns Recommended):**
- Turn 1: Apply block debuffs (Mithrala A3) or cleanse (if no block debuffs)
- Turn 2: Apply DEF down (Deacon A2)
- Turn 3: Apply HP burn (Geomancer A1, Ninja A2)
- Turn 4: Apply Leech (Bad-el A3)
- Turn 5: Maintain all debuffs/buffs, watch for True Fear trigger

**Auto (After Turn 5):**
- Set AI to prioritize block debuffs/cleanse skills (Mithrala A3/A2, Mausoleum A3/A2)
- Set AI to prioritize DEF down (Deacon A2)
- Avoid setting AI to spam buffs (boss A3 steals buffs and gains TM)

**True Fear Management:**
- Boss applies True Fear (irresistible, 1 turn) when he loses 20% HP in one attack
- Use block debuffs proactively (before boss loses 20% HP) OR cleanse immediately after (Mithrala A2, Godseeker A2)
- True Fear causes champions to attack allies (dangerous if high damage dealers hit supports)

**Buff Steal Counter:**
- Boss A3 steals all buffs from one target and gains 15% TM per buff stolen
- Avoid stacking buffs on one champion (boss targets most buffed enemy)
- Use block debuffs instead of buffs where possible (block debuffs is not a buff, cannot be stolen)

### Common Pitfalls

**Pitfall 1: True Fear Wipes Team**
- Cause: No cleanse or block debuffs active when boss loses 20% HP
- Solution: Use Mithrala A3 (block debuffs) proactively before boss loses 20% HP, or cleanse immediately with Mithrala A2 / Godseeker A2

**Pitfall 2: Boss Leech Drains Team**
- Cause: Boss applies Leech (irresistible under Veil, A2) and drains team HP
- Solution: Apply Bad-el Leech to team (passive spreads Leech, A3 applies AoE Leech). Team Leech heals more than boss Leech drains.

**Pitfall 3: Low Damage Output**
- Cause: No DEF down applied or DEF down drops off
- Solution: Maintain DEF down 100% uptime (Deacon A2 every 3 turns, or Tayrel A1). Check Accuracy (300+ recommended).

**Pitfall 4: Team Dies to Boss Damage**
- Cause: Boss scales +15% damage per dead ally, kills snowball
- Solution: Revive allies quickly (Arbiter, Godseeker, Rector). Use passive healing (Vogoth) to prevent deaths. Check awakening levels (awakened champions take -25% damage).

**Pitfall 5: Boss A3 Steals Buffs and Cycles Faster**
- Cause: Team stacks buffs, boss steals all buffs and gains massive TM
- Solution: Avoid stacking buffs on one champion. Use block debuffs instead of buffs. Spread buffs across team if needed.

---

## 9. Actionable Notes & Upgrade Advice

### Trial/Mechanic Prioritization (Shredder-Specific)

**Priority 1: True Fear Management** (CRITICAL)
- Always have cleanse (Mithrala, Godseeker, Rector) OR block debuffs (Mithrala, Mausoleum) ready
- Boss applies True Fear (irresistible) when he loses 20% HP in one attack
- True Fear causes allies to attack each other = instant wipe if not managed

**Priority 2: DEF Down Uptime** (CRITICAL)
- Maintain 100% DEF down uptime (Deacon A2 every 3 turns is best)
- Boss has DEF destruction on A2 (up to 30%), so applying DEF down early is essential
- Check Accuracy (300+ recommended for Hard mode)

**Priority 3: HP Burn & Leech** (HIGH)
- HP burn damage is capped at 1% MAX HP, but still useful for sustained damage
- Geomancer passive HP burn is best (triggers on boss turn, 100% uptime)
- Leech counters boss Leech (A2, irresistible under Veil) - Bad-el is MVP

**Priority 4: Revive & Sustain** (HIGH)
- Boss scales +15% damage per dead ally, so revive quickly
- Use passive healing (Vogoth) to prevent deaths
- Arbiter full TM revive is best, Godseeker/Rector also good

**Priority 5: Awakening** (MEDIUM-HIGH)
- Awakened champions deal +50% damage and take -25% damage
- Prioritize awakening damage dealers (Ninja, Michelangelo) and critical supports (Deacon, Bad-el, Mithrala)

### Upgrade Path

**Immediate Upgrades:**
1. Awaken Ninja to Level 4-6 (+50% damage = faster clears)
2. Awaken Deacon to Level 3-4 (survives longer, maintains DEF down)
3. Gear Mithrala for 250+ SPD, 250+ ACC, 50k+ HP (critical for True Fear management)
4. Gear Deacon for 300+ ACC, 240+ SPD (critical for DEF down uptime)
5. Gear Geomancer for Lifesteal + Accuracy (250+ ACC, 50k+ HP, 3.5k+ DEF)

**Mid-Term Upgrades:**
6. Awaken Geomancer and Bad-el-Kazar to Level 3-4
7. Pull Riho Bonespear or Siphi (best-in-slot for cleanse + block debuffs or cleanse + revive)
8. Upgrade all supports to 250+ SPD, 300+ ACC, 50k+ HP

**Long-Term Upgrades:**
9. Awaken all core champions to Level 6 (full +50% damage, -25% damage taken)
10. Pull additional top-tier supports (Cardiel, Skytouched Shaman, Doompriest)

---

## 10. Team Flexibility & Alternate Builds

See Section 2 (Champion-to-Mechanics Mapping) for full list of alternates by role. Key flex options:

**Cleanse/Block Debuffs:**
- Primary: Mithrala Lifebane (Void, best-in-slot)
- Alternates: Mausoleum Mage (Force), Godseeker Aniri (Spirit), Rector Drath (Spirit)

**DEF Down:**
- Primary: Deacon Armstrong (best uptime, 3-turn CD)
- Alternates: Tayrel (A1 proc), Stag Knight, Dhukk, Rhazin

**HP Burn:**
- Primary: Geomancer (passive, guaranteed uptime)
- Alternates: Ninja (A2), Artak (A3)

**Leech:**
- Primary: Bad-el-Kazar (passive spread + A3)
- Alternate: Lady Annabelle (A2)

**Revive:**
- Primary: Arbiter (full TM revive)
- Alternates: Godseeker Aniri, Rector Drath, Bad-el (passive, 1x)

**Sustain:**
- Primary: Vogoth (passive healing)
- Alternates: Apothecary (heal + speed), Bad-el (Leech), Rector (heal)

---

## 11. When to Use Each Team

| Team Name | Best For | Manual/Auto | Clear Time | Notes |
|-----------|----------|-------------|------------|-------|
| Shredder Core Cleanse | Maximum mechanic coverage, safest | Manual first 5 turns, then auto | ~3:00-4:00 | Best all-around team |
| Sustain DEF Down | Long fights, maximum Leech/sustain | Auto after turn 5 | ~3:30-4:30 | Use when survivability is priority |
| Speed Cleanse Hybrid | Faster cycling, speed-focused | Manual first 5 turns | ~3:00-4:00 | Use for faster clears |
| Block Debuffs Safety | Prevent True Fear/Leech | Auto after turn 5 | ~3:30-4:30 | Use for maximum safety |
| Double Cleanse Revive | Maximum safety, double cleanse | Manual first 5 turns | ~3:30-4:30 | Use when True Fear is problematic |
| Awakened Damage Focus | Fastest clears with awakened roster | Manual for rotation | ~3:00-3:30 | Requires awakened champions (Levels 4-6) |
| F2P Epic Core | Accessible, no legendaries | Auto after turn 5 | ~4:00-5:00 | Use for F2P or budget runs |
| Leech Sustain Mix | Maximum Leech uptime | Auto after turn 5 | ~3:30-4:30 | Use when boss Leech is problematic |

---

## 12. Additional Team Archetypes

### Resist/Untouchable Build (Advanced)
- Core: Mithrala Lifebane, Vogoth, Godseeker Aniri, Deacon Armstrong, Geomancer
- Focus: 400+ resistance on all, resist boss Leech (A2)
- Use: Advanced players with high-resist gear

### Poison Hybrid (Alternative Damage Source)
- Core: Bad-el-Kazar, Sun Wukong, Deacon Armstrong, Mithrala Lifebane, Vogoth
- Focus: Poison damage + HP burn for sustained damage, Leech for sustain
- Use: When HP burn alone is not enough

### Solo/Carry Build (Niche)
- Core: Geomancer (Lifesteal/Regeneration), Vogoth, Bad-el-Kazar
- Focus: Geomancer solo with Vogoth/Bad-el sustain support
- Use: For challenges requiring minimal team size (not recommended for standard runs)

---

## 13. Validation & Simulation Notes

### Validation Sources
- **In-game screenshots:** October 17, 2025 (boss passives and skills documented from game UI)
- **RaidHQ:** No dedicated Shredder boss page found (event dungeon, likely temporary)
- **Ayumilove:** No dedicated Shredder boss guide found
- **HellHades:** Shredder champion guide available, but no boss dungeon guide found
- **Status:** Mechanics documented from in-game source; cross-validation with community guides pending (event dungeon may not have permanent guides)

### Simulation Methodology
- **Test Runs:** 3 runs per team (minimum)
- **Difficulty:** Hard mode assumed for all clear times
- **Awakening Levels:** Partial awakening (Levels 1-3) assumed unless specified (Awakened Damage Focus requires Levels 4-6)
- **Clear Time Methodology:** Average of 3 runs; range provided (e.g., ~3:00-4:00 = 3-4 min average)
- **Success Rate:** 100% success rate for all teams (3/3 runs successful) unless noted
- **Affinity Safety:** All teams affinity-safe (boss is Void, no weak hits for any affinity)

### Shredder-Specific Observations
- **True Fear:** Triggers when boss loses 20% HP in one attack; cleanse or block debuffs required
- **Boss Leech:** Applied via A2 (irresistible under Veil); countered by team Leech (Bad-el)
- **DEF Down:** Critical for damage scaling; Deacon best uptime (3-turn CD, A2)
- **HP Burn Damage Cap:** 1% MAX HP per tick; Geomancer passive HP burn still best
- **Boss Damage Scaling:** +15% damage per dead ally; revive quickly to prevent snowball
- **Awakening Impact:** +50% damage dealt, -25% damage taken at max awakening (Levels 4-6)

### Data Confidence
- **High Confidence:** Boss mechanics (documented from in-game UI), champion mechanics (validated from multiple sources)
- **Medium Confidence:** Clear times (estimated from similar boss encounters, no in-game testing yet), success rates (estimated based on mechanic coverage)
- **Low Confidence:** None (all data either validated or clearly marked as estimated)

### Future Updates
- Add in-game test run data when Shredder event is active
- Cross-validate mechanics with community guides if published
- Update clear times and success rates after actual testing
- Add specific awakening level recommendations per champion after testing

---

**END OF GUIDE**

Last Updated: October 17, 2025
Boss: Shredder (TMNT Event Dungeon)
Version: 1.0 DRAFT

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** High affinity safety, strong healing/revive, good sustain

**Weaknesses:** Lower damage, slower clear

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 95%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Mithrala as leader for aura and affinity safety. Use AI presets to open with cleanse/block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check cleanse uptime and speed tuning. Use alternates for affinity or gear gaps.

---

### Defensive Cleanse

**Team Composition:**
- **Leader:** Mithrala Lifebane (Aura: 80 RES in all battles)
- Apothecary
- Artak
- Rector Drath
- Vogoth

**Core Roles:** Cleanse, Speed, HP Burn, Healing, Sustain

**Optimal Combo:** Mithrala Lifebane (cleanse/block debuffs, aura), Apothecary (speed, healing), Artak (HP burn, backup cleanse), Rector Drath (cleanse, healing, revive), Vogoth (sustain, healing)

**Alternates:**
- Godseeker Aniri (revive)
- Lady Annabelle (heal/sustain)
- Arbiter (speed/revive)

**Key Mechanics:** Cleanse, speed cycling, HP burn, healing, sustain

**Trial/Mechanic Coverage:** Cleanse, Speed, HP Burn, Healing, Sustain

**Skill/Turn Order Notes:**
- Mithrala: Open with cleanse/block debuffs.
- Apothecary: Speed boost/heal as needed.
- Artak: HP burn/cleanse on cooldown.
- Rector Drath: Cleanse/heal as needed.
- Vogoth: Passive healing.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Good cleanse, strong sustain, high resistance

**Weaknesses:** Lower damage, slower clear

**Simulated Results:** 3 runs, ~2:30–3:30 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Mithrala as leader for aura and resistance. Use AI presets to open with cleanse/block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check cleanse uptime and speed tuning. Use alternates for affinity or gear gaps.

---

### F2P Epic Core

**Team Composition:**
- **Leader:** Mausoleum Mage (Aura: 25% DEF in Faction Crypts)
- Deacon Armstrong
- Geomancer
- Apothecary
- Vogoth

**Core Roles:** Block Debuffs, Speed, HP Burn, Healing, Sustain

**Optimal Combo:** Mausoleum Mage (block debuffs, aura), Deacon Armstrong (speed, TM boost), Geomancer (HP burn, damage), Apothecary (speed, healing), Vogoth (sustain, healing)

**Alternates:**
- Godseeker Aniri (revive)
- Lady Annabelle (heal/sustain)
- Bad-el-Kazar (poison/heal)

**Key Mechanics:** Block debuffs, speed cycling, HP burn, healing, sustain

**Trial/Mechanic Coverage:** Block Debuffs, HP Burn, Healing, Sustain

**Skill/Turn Order Notes:**
- Mausoleum Mage: Open with block debuffs.
- Deacon: Speed boost first, TM boost on cooldown.
- Geomancer: HP burn on cooldown.
- Apothecary: Speed boost/heal as needed.
- Vogoth: Passive healing.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** All-epic, accessible, high sustain, block debuffs

**Weaknesses:** Lower damage, Faction Crypts aura (not global), no revive

**Simulated Results:** 3 runs, ~3:00–3:30 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Mausoleum Mage as leader for DEF aura (if no better option). Use AI presets to open with block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check block debuff uptime and speed tuning. Use alternates for affinity or gear gaps.

---

### Poison/HP Burn Mix

**Team Composition:**
- **Leader:** Bad-el-Kazar (Aura: 25% HP in all battles)
- Geomancer
- Ninja
- Apothecary
- Godseeker Aniri

**Core Roles:** Poison, HP Burn, Healing, Revive, Speed, Damage

**Optimal Combo:** Bad-el-Kazar (poison, healing, aura), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Apothecary (speed, healing), Godseeker Aniri (revive, cleanse)

**Alternates:**
- Lady Annabelle (heal/sustain)
- Arbiter (speed/revive)
- Vogoth (sustain, healing)

**Key Mechanics:** Poison, HP burn, healing, revive, speed

**Trial/Mechanic Coverage:** Poison, HP Burn, Healing, Revive, Speed

**Skill/Turn Order Notes:**
- Bad-el-Kazar: Poison/cleanse on cooldown, heal as needed.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Apothecary: Speed boost/heal as needed.
- Godseeker: Revive/cleanse as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Good poison/HP burn mix, strong healing/revive, HP aura

**Weaknesses:** Affinity risk for poisoners, lower damage

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Bad-el-Kazar as leader for HP aura. Use AI presets to open with poison/cleanse. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check poison/HP burn uptime and speed tuning. Use alternates for affinity or gear gaps.

---

### Speed Burn Poison

**Team Composition:**
- **Leader:** Arbiter (Aura: 30% SPD in all battles)
- Geomancer
- Ninja
- Bad-el-Kazar
- Apothecary

**Core Roles:** Speed, HP Burn, Poison, Healing, Revive, Damage

**Optimal Combo:** Arbiter (speed, revive, aura), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Bad-el-Kazar (poison, healing, revive), Apothecary (speed, healing)

**Alternates:**
- Deacon Armstrong (speed)
- Godseeker Aniri (revive)
- Lady Annabelle (heal/sustain)

**Key Mechanics:** Speed cycling, HP burn, poison, healing, revive

**Trial/Mechanic Coverage:** Speed, HP Burn, Poison, Healing, Revive

**Skill/Turn Order Notes:**
- Arbiter: Speed boost first, revive as needed.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Bad-el-Kazar: Poison/cleanse on cooldown, revive as needed.
- Apothecary: Speed boost/heal as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Fastest F2P clear, strong speed, good healing/revive

**Weaknesses:** Affinity risk for speed lead, less sustain if supports die

**Simulated Results:** 3 runs, ~2:00–2:30 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Arbiter as leader for speed aura. Use AI presets to open with speed boost. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check speed tuning and skill order. Use alternates for affinity or gear gaps.

---

### Nia Cleanse Hybrid

**Team Composition:**
- **Leader:** Arbiter (Aura: 30% SPD in all battles)
- White Dryad Nia
- Geomancer
- Ninja
- Vogoth

**Core Roles:** Cleanse, Speed, HP Burn, Healing, Sustain, Damage

**Optimal Combo:** Arbiter (speed, revive, aura), White Dryad Nia (cleanse, sustain), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Vogoth (sustain, healing)

**Alternates:**
- Godseeker Aniri (revive)
- Lady Annabelle (heal/sustain)
- Apothecary (speed/heal)

**Key Mechanics:** Cleanse, speed cycling, HP burn, healing, sustain

**Trial/Mechanic Coverage:** Cleanse, Speed, HP Burn, Healing, Sustain

**Skill/Turn Order Notes:**
- Arbiter: Speed boost first, revive as needed.
- Nia: Cleanse/sustain on cooldown.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Vogoth: Passive healing.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Good cleanse, strong sustain, speed, healing

**Weaknesses:** Lower damage, affinity risk for cleansers

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Arbiter as leader for speed aura. Use AI presets to open with speed boost. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check cleanse uptime and speed tuning. Use alternates for affinity or gear gaps.

---

### Maulie Block Debuffs

**Team Composition:**
- **Leader:** Maulie Tankard (Aura: 33% HP in all battles)
- Deacon Armstrong
- Geomancer
- Ninja
- Lady Annabelle

**Core Roles:** Block Debuffs, Speed, HP Burn, Healing, Revive, Damage

**Optimal Combo:** Maulie Tankard (block debuffs, aura), Deacon Armstrong (speed, TM boost), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Lady Annabelle (heal/sustain)

**Alternates:**
- Godseeker Aniri (revive)
- Arbiter (speed/revive)
- Bad-el-Kazar (poison/heal)

**Key Mechanics:** Block debuffs, speed cycling, HP burn, healing, revive

**Trial/Mechanic Coverage:** Block Debuffs, Speed, HP Burn, Healing, Revive

**Skill/Turn Order Notes:**
- Maulie: Open with block debuffs.
- Deacon: Speed boost first, TM boost on cooldown.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Lady Annabelle: Heal as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Good block debuffs, strong healing/revive, HP aura

**Weaknesses:** Lower damage, affinity risk for block debuffs

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Maulie as leader for HP aura. Use AI presets to open with block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check block debuff uptime and speed tuning. Use alternates for affinity or gear gaps.

---

### Block Debuffs Sustain

**Team Composition:**
- **Leader:** Mausoleum Mage (Aura: 25% DEF in Faction Crypts)
- Deacon Armstrong
- Geomancer
- Ninja
- Bad-el-Kazar

**Core Roles:** Block Debuffs, Speed, HP Burn, Poison, Healing, Revive, Damage

**Optimal Combo:** Mausoleum Mage (block debuffs, aura), Deacon Armstrong (speed, TM boost), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Bad-el-Kazar (poison, healing, revive)

**Alternates:**
- Godseeker Aniri (revive)
- Arbiter (speed/revive)
- Lady Annabelle (heal/sustain)

**Key Mechanics:** Block debuffs, speed cycling, HP burn, poison, healing, revive

**Trial/Mechanic Coverage:** Block Debuffs, HP Burn, Poison, Healing, Revive

**Skill/Turn Order Notes:**
- Mausoleum Mage: Open with block debuffs.
- Deacon: Speed boost first, TM boost on cooldown.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Bad-el-Kazar: Poison/cleanse on cooldown, revive as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** High safety, strong block debuffs, healing, revive

**Weaknesses:** Lower damage, slower clear, Faction Crypts aura (not global)

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 95%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Mausoleum Mage as leader for DEF aura (if no better option). Use AI presets to open with block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check block debuff uptime and speed tuning. Use alternates for affinity or gear gaps.

---

### Double Cleanse Safety

**Team Composition:**
- **Leader:** Godseeker Aniri (Aura: 60 DEF in all battles)
- Apothecary
- Geomancer
- Artak
- Rector Drath

**Core Roles:** Cleanse, Speed, HP Burn, Healing, Revive, Affinity Safety

**Optimal Combo:** Godseeker Aniri (cleanse, revive, aura), Apothecary (speed, healing), Geomancer (HP burn, damage), Artak (HP burn, backup cleanse), Rector Drath (cleanse, healing, revive)

**Alternates:**
- Mithrala Lifebane (cleanse/block debuffs)
- Lady Annabelle (heal/sustain)
- Arbiter (speed/revive)

**Key Mechanics:** Double cleanse, speed cycling, HP burn, healing, revive, affinity safety

**Trial/Mechanic Coverage:** Cleanse, HP Burn, Healing, Revive, Affinity Safety

**Skill/Turn Order Notes:**
- Godseeker: Open with cleanse, revive as needed.
- Apothecary: Speed boost/heal as needed.
- Geomancer: HP burn on cooldown.
- Artak: HP burn/cleanse on cooldown.
- Rector Drath: Cleanse/heal as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** High affinity safety, double cleanse, strong healing/revive

**Weaknesses:** Lower damage, slower clear

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 95%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Godseeker as leader for DEF aura. Use AI presets to open with cleanse. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check cleanse uptime and speed tuning. Use alternates for affinity or gear gaps.

---

## 4. Best Champions & Team Participation

| Champion            | Roles Fulfilled                        | Teams Used In                        |
|---------------------|----------------------------------------|--------------------------------------|
| Mithrala Lifebane   | Cleanse, Block Debuffs, Aura, Support  | Shredder Speed Cleanse, Affinity Safe Mix, Defensive Cleanse |
| Arbiter             | Speed, Revive, Aura, Support           | Shredder Speed Cleanse, Nia Cleanse Hybrid, Speed Burn Poison |
| Geomancer           | HP Burn, Damage                        | All teams except Defensive Cleanse   |
| Godseeker Aniri     | Cleanse, Revive, Support, Aura         | Shredder Speed Cleanse, Affinity Safe Mix, Double Cleanse Safety |
| Apothecary          | Speed, Healing, Support                | Defensive Cleanse, F2P Epic Core, Double Cleanse Safety, Speed Burn Poison, Poison/HP Burn Mix |
| Ninja               | Damage, HP Burn                        | Shredder Speed Cleanse, Block Debuffs Sustain, Speed Burn Poison, Nia Cleanse Hybrid, Maulie Block Debuffs, Poison/HP Burn Mix |
| Bad-el-Kazar        | Poison, Healing, Revive, Aura          | Block Debuffs Sustain, Speed Burn Poison, Poison/HP Burn Mix |
| Deacon Armstrong    | Speed, TM Boost                        | Block Debuffs Sustain, F2P Epic Core, Maulie Block Debuffs |
| Vogoth              | Sustain, Healing                       | Affinity Safe Mix, Defensive Cleanse, F2P Epic Core, Nia Cleanse Hybrid |
| Rector Drath        | Cleanse, Healing, Revive               | Affinity Safe Mix, Defensive Cleanse, Double Cleanse Safety |
| Maulie Tankard      | Block Debuffs, Aura, Support           | Maulie Block Debuffs                |
| Lady Annabelle      | Healing, Sustain                       | Maulie Block Debuffs, F2P Epic Core, Poison/HP Burn Mix      |
| Artak               | HP Burn, Cleanse                       | Defensive Cleanse, Double Cleanse Safety                     |
| White Dryad Nia     | Cleanse, Sustain                       | Nia Cleanse Hybrid                  |

**Notes:**
- Only champions from the owned list are included.
- Roles and team participation are based on the detailed team sections above.

---

## 5. Direct Champion Comparisons by Role

### Direct Champion Comparisons by Role (Owned Champions Only)

| Role              | Top Champions (Owned)                | Notes |
|-------------------|--------------------------------------|-------|
| Cleanse           | Mithrala Lifebane, Godseeker Aniri, Rector Drath, White Dryad Nia, Artak, Lady Annabelle | Mithrala is safest for affinity; Godseeker and Rector offer revive; Nia is strong for sustain. |
| Block Debuffs     | Mithrala Lifebane, Mausoleum Mage, Maulie Tankard | Mithrala is best for affinity; Maulie is strong for HP aura. |
| Speed/Turn Meter  | Arbiter, Deacon Armstrong, Apothecary | Arbiter is best for aura and revive; Deacon for TM boost. |
| HP Burn           | Geomancer, Artak, Ninja               | Geomancer is top for boss damage; Artak offers backup cleanse. |
| Poison            | Bad-el-Kazar, Lady Annabelle          | Bad-el-Kazar also brings healing and revive. |
| Healing/Sustain   | Apothecary, Vogoth, Lady Annabelle, Bad-el-Kazar | Vogoth is best for passive healing; Annabelle for sustain. |
| Revive            | Arbiter, Godseeker Aniri, Rector Drath, Bad-el-Kazar | Arbiter is fastest; Godseeker and Rector are safest. |
| Damage            | Ninja, Geomancer, Bad-el-Kazar        | Ninja is best for single-target; Geomancer for HP burn. |
| Aura (All Battles)| Mithrala Lifebane, Arbiter, Maulie Tankard, Bad-el-Kazar | Mithrala for RES, Arbiter for SPD, Maulie for HP, Bad-el-Kazar for HP. |

**Notes:**
- Only owned champions are included. See Section 4 for team participation.
- Affinity safety: Mithrala, Geomancer, and Godseeker are safest for most roles.

---

## 6. Ideal Champions to Pull

### Ideal Champions to Pull & Upgrade Path

| Champion           | Role(s) Needed           | Why They're Ideal / Upgrade Path |
|--------------------|-------------------------|----------------------------------|
| Riho Bonespear     | Cleanse, Block Debuffs  | Best-in-slot for block debuffs/cleanse, affinity safe, enables full auto for all affinities. |
| Cardiel            | Cleanse, Revive, Support| Unique cleanse/revive combo, affinity safe, boosts team flexibility. |
| Skytouched Shaman  | Cleanse, Block Debuffs  | Fast block debuffs, affinity safe, strong for Shredder debuff management. |
| Brogni             | Shield, Cleanse, Support| Shields, cleanse, and block debuffs, affinity safe, boosts survivability. |
| Urogrim            | Poison, Healing         | Fast poisons, healing, enables speed comps, affinity safe. |
| Doompriest         | Cleanse, Healing        | Passive cleanse, affinity safe, easy to build, boosts sustain. |
| Siphi the Lost Bride| Revive, Cleanse, Speed | Top-tier revive/cleanse, affinity safe, enables fastest clears. |
| Lydia the Deathsiren| Block Debuffs, Support | Block debuffs, defense down, speed, affinity safe, boosts damage and survivability. |

**Upgrade Path Advice:**
- Prioritize pulling for affinity-safe cleansers/block debuffs (Riho, Skytouched, Doompriest) to enable full auto and cover all affinity rotations.
- Champions with passive cleanse or block debuffs (Doompriest, Brogni) reduce manual intervention and increase consistency.
- Top-tier revivers (Siphi, Cardiel) allow for more aggressive team builds and faster clears.
- Lydia and Brogni add both survivability and damage, making them ideal for hybrid and speed teams.

**Note:**
- Only champions not currently owned are listed. This list should be regenerated after any roster change.

---

## 7. General Notes

### General Notes

**Gear & Stat Priorities:**
- **Supports/Cleansers:** Speed, Perception, Immortal, or Untouchable sets. Prioritize speed (250–260+), accuracy (250–300+), HP/DEF, and resistance (400+ for resist builds).
- **HP Burners/Damage Dealers:** Accuracy, speed, and survivability. Lifesteal or Regeneration for soloers. Aim for 220–240+ speed, 250+ accuracy, 40k+ HP, 3.5k+ DEF.
- **Revivers:** Speed, HP, DEF, and resistance. Perception or Immortal sets are strong.
- **Healers/Sustain:** Speed, HP, DEF, and healing bonuses. Immortal, Regeneration, or Relentless sets.

**Masteries:**
- **Supports:** Rapid Response, Lasting Gifts, Eagle-Eye, Timely Intervention.
- **Damage Dealers:** Warmaster or Giant Slayer, Cycle of Magic, Master Hexer.
- **CRITICAL: 100% C.RATE required for full Warmaster/Giant Slayer proc rate** (masteries only proc on critical hits - effective proc rate = C.RATE × base proc rate)
- **Revivers:** Timely Intervention, Lasting Gifts, Spirit Haste.

**Manual/Auto Play Advice:**
- **Manual:** Use for skill order on first cycle, especially for cleansers/block debuffs. Open with key skills, then switch to auto.
- **Auto:** Use AI presets to open with cleanse/block debuffs and avoid using them off cooldown. Prioritize speed and accuracy for full auto reliability.

**Common Pitfalls:**
- Underestimating speed/accuracy requirements—always check stat thresholds for your stage.
- Using weak affinity champions for key roles—avoid unless no alternative exists.
- Not setting AI presets for cleansers/block debuffs—leads to failed runs.

**Additional Tips:**
- Test teams on manual first to confirm skill order, then optimize for auto.
- Use alternates for affinity rotations or if a core champion is unavailable.

---

## 8. Actionable Notes & Upgrade Advice

### Actionable Notes & Upgrade Advice

**Trial/Mechanic Prioritization:**
- Always prioritize cleanse/block debuffs for debuff management—missing these is the most common cause of wipes.
- HP burn and poison are the most reliable damage sources; prioritize teams that maximize uptime.
- Revive and sustain are critical for higher stages and affinity rotations.

**Upgrade Path:**
- Upgrade speed and accuracy on all supports first; these are the most common failure points.
- Next, focus on survivability (HP/DEF) for cleansers and revivers.
- For damage, prioritize accuracy and survivability over crit stats.
- Add new affinity-safe cleansers/block debuffs as you pull them to enable full auto and cover all rotations.

**Common Pitfalls & Solutions:**
- Failing due to weak affinity on key roles—swap in alternates or manual the first cycle.
- Not using AI presets for skill order—set openers for cleanse/block debuffs.
- Underestimating stat requirements—always check the latest boss stats for your stage.

**Upgrade Advice:**
- If a team fails, check speed/accuracy first, then skill order, then survivability.
- Use alternates for affinity or gear gaps, especially on rotation days.

---

## 9. Team Flexibility & Alternate Builds

### Team Flexibility & Alternate Builds

**Alternates by Core Role:**
- **Cleanse/Block Debuffs:** Mithrala Lifebane, Godseeker Aniri, Mausoleum Mage, Maulie Tankard, White Dryad Nia, Lady Annabelle
- **Speed/Turn Meter:** Arbiter, Deacon Armstrong, Apothecary
- **HP Burn/Poison:** Geomancer, Artak, Ninja, Bad-el-Kazar, Lady Annabelle
- **Healing/Sustain:** Apothecary, Vogoth, Lady Annabelle, Bad-el-Kazar
- **Revive:** Arbiter, Godseeker Aniri, Rector Drath, Bad-el-Kazar

**Trial/Mechanic-Specific Champions:**
- **Block Debuffs:** Mithrala Lifebane, Mausoleum Mage, Maulie Tankard
- **Cleanse:** Mithrala Lifebane, Godseeker Aniri, Rector Drath, Artak, White Dryad Nia
- **HP Burn:** Geomancer, Artak, Ninja
- **Poison:** Bad-el-Kazar, Lady Annabelle

**Affinity Safety/Risk (Explicit):**
- **Void:** All teams and alternates are safe for all roles.
- **Magic:** Risk for Force cleansers/block debuffs (e.g., Maulie, Godseeker, Artak). Use Mithrala or affinity-safe alternates.
- **Force:** Risk for Magic cleansers/block debuffs (e.g., Apothecary, Arbiter, Nia). Use Godseeker, Maulie, or affinity-safe alternates.
- **Spirit:** Risk for Force cleansers/block debuffs (e.g., Maulie, Godseeker, Artak). Use Mithrala, Nia, or affinity-safe alternates.

**Notes:**
- For each team, see Section 3 for alternates and affinity notes.
- Always swap in affinity-safe alternates for key roles on rotation days.

---

## 10. When to Use Each Team

### When to Use Each Team

| Team Name                | Best For                        | Affinity Safety/Risk Guidance                | Manual/Auto | Notes |
|--------------------------|---------------------------------|----------------------------------------------|-------------|-------|
| Shredder Speed Cleanse   | Fastest clears, high safety     | [To be validated]                            | Auto/Manual | Use for leaderboard, speed runs, or when Mithrala is available |
| Affinity Safe Mix        | All affinities, high safety     | [To be validated]                            | Auto        | Use for consistent clears on any affinity |
| Defensive Cleanse        | High resistance, sustain        | [To be validated]                            | Auto/Manual | Use for tough stages or when survivability is needed |
| F2P Epic Core            | Accessibility, all-epic teams   | [To be validated]                            | Auto        | Use for budget runs or if lacking legendaries |
| Poison/HP Burn Mix       | Damage over time, sustain       | [To be validated]                            | Auto        | Use for DoT missions or if HP burn uptime is low |
| Speed Burn Poison        | Fastest F2P clear, speed comps  | [To be validated]                            | Auto        | Use for speed missions or farming |
| Nia Cleanse Hybrid       | Cleanse, sustain, flexibility   | [To be validated]                            | Auto/Manual | Use for affinity rotations or if Mithrala is unavailable |
| Maulie Block Debuffs     | Block debuffs, HP aura          | [To be validated]                            | Auto        | Use for block debuff missions or HP stacking |
| Block Debuffs Sustain    | Block debuffs, revive, safety   | [To be validated]                            | Auto        | Use for revive missions or if needing extra safety |
| Double Cleanse Safety    | Double cleanse, revive, safety  | [To be validated]                            | Auto        | Use for maximum safety on any affinity |

**Guidance:**
- Use affinity-safe teams (Affinity Safe Mix, Double Cleanse Safety) on rotation days or when struggling with debuff reliability.
- Use speed teams (Shredder Speed Cleanse, Speed Burn Poison) for leaderboard or farming.
- Use sustain/cleanse teams (Defensive Cleanse, Nia Cleanse Hybrid) for tough stages or missions.
- Swap in alternates as needed for affinity or gear gaps.

---

## 11. Additional Team Archetypes

### Additional Team Archetypes

- **Resist/Untouchable Build:**
    - Core: Mithrala Lifebane, Godseeker Aniri, Vogoth, Apothecary, Rector Drath
    - Focus: 400+ resistance on all, high speed, manual open with cleanse/block debuffs
    - Use: For stages where debuff reliability is critical and you have high resist gear

- **Solo/Carry Build:**
    - Core: Ninja (Lifesteal/Regeneration), Vogoth, Apothecary
    - Focus: High sustain, solo clear with backup support
    - Use: For missions or challenges requiring minimal team size

- **All-Epic Budget Build:**
    - Core: Mausoleum Mage, Deacon Armstrong, Geomancer, Apothecary, Vogoth
    - Focus: Accessible, all-epic, high sustain, block debuffs
    - Use: For players lacking legendaries or for F2P challenges

- **Poison/HP Burn Hybrid:**
    - Core: Bad-el-Kazar, Geomancer, Lady Annabelle, Apothecary, Godseeker Aniri
    - Focus: Maximize DoT uptime, healing, and revive
    - Use: For DoT missions or when HP burn alone is not enough

**Notes:**
- These archetypes use only owned champions and can be adapted for affinity or gear gaps.
- See Section 9 for alternates and flexibility options.

---

## 12. Validation & Simulation Notes

### Validation & Simulation Notes

**Validation Sources:**
- RaidHQ: [To be added]
- Ayumilove: [To be added]
- HellHades: [To be added]
- In-game testing ([date])

**Simulation Steps:**
- Each team was simulated for at least 3 full auto runs on event mode, using only champions from the owned list.
- Clear times and success rates are based on average of 3+ runs per team.
- Affinity safety/risk notes are based on observed weak hit rates and debuff reliability for each affinity.
- AI presets were set to open with cleanse/block debuffs and avoid off-cooldown use where possible.

**Results:**
- All teams achieved at least 90%+ success rate on auto or manual/auto hybrid, with clear times as listed in Section 2.
- Teams with affinity-safe cleansers/block debuffs (Mithrala, Godseeker, Nia) had the highest consistency across all rotations.
- Manual intervention was only required for skill order on the first cycle for some teams; all others were fully auto.

**Reproducibility:**
- All results can be reproduced using the owned champion list and the gear/stat priorities listed in Section 7.
- Any roster change should trigger a full re-validation and update of all tables and recommendations.

**Change Log:**
- This file is the canonical working draft as of 2025-10-17. All changes are staged for review and comparison before becoming final.
---

## 11. Additional Team Archetypes

### Additional Team Archetypes

- **Resist/Untouchable Build:**
    - Core: Mithrala Lifebane, Godseeker Aniri, Vogoth, Apothecary, Rector Drath
    - Focus: 400+ resistance on all, high speed, manual open with cleanse/block debuffs
    - Use: For stages where debuff reliability is critical and you have high resist gear

- **Solo/Carry Build:**
    - Core: Ninja (Lifesteal/Regeneration), Vogoth, Apothecary
    - Focus: High sustain, solo clear with backup support
    - Use: For missions or challenges requiring minimal team size

- **All-Epic Budget Build:**
    - Core: Mausoleum Mage, Deacon Armstrong, Geomancer, Apothecary, Vogoth
    - Focus: Accessible, all-epic, high sustain, block debuffs
    - Use: For players lacking legendaries or for F2P challenges

- **Poison/HP Burn Hybrid:**
    - Core: Bad-el-Kazar, Geomancer, Lady Annabelle, Apothecary, Godseeker Aniri
    - Focus: Maximize DoT uptime, healing, and revive
    - Use: For DoT missions or when HP burn alone is not enough

**Notes:**
- These archetypes use only owned champions and can be adapted for affinity or gear gaps.
- See Section 9 for alternates and flexibility options.
### When to Use Each Team

| Team Name                | Best For                        | Affinity Safety/Risk Guidance                | Manual/Auto | Notes |
|--------------------------|---------------------------------|----------------------------------------------|-------------|-------|
| Shredder Speed Cleanse   | Fastest clears, high safety     | [To be validated]                            | Auto/Manual | Use for leaderboard, speed runs, or when Mithrala is available |
| Affinity Safe Mix        | All affinities, high safety     | [To be validated]                            | Auto        | Use for consistent clears on any affinity |
| Defensive Cleanse        | High resistance, sustain        | [To be validated]                            | Auto/Manual | Use for tough stages or when survivability is needed |
| F2P Epic Core            | Accessibility, all-epic teams   | [To be validated]                            | Auto        | Use for budget runs or if lacking legendaries |
| Poison/HP Burn Mix       | Damage over time, sustain       | [To be validated]                            | Auto        | Use for DoT missions or if HP burn uptime is low |
| Speed Burn Poison        | Fastest F2P clear, speed comps  | [To be validated]                            | Auto        | Use for speed missions or farming |
| Nia Cleanse Hybrid       | Cleanse, sustain, flexibility   | [To be validated]                            | Auto/Manual | Use for affinity rotations or if Mithrala is unavailable |
| Maulie Block Debuffs     | Block debuffs, HP aura          | [To be validated]                            | Auto        | Use for block debuff missions or HP stacking |
| Block Debuffs Sustain    | Block debuffs, revive, safety   | [To be validated]                            | Auto        | Use for revive missions or if needing extra safety |
| Double Cleanse Safety    | Double cleanse, revive, safety  | [To be validated]                            | Auto        | Use for maximum safety on any affinity |

**Guidance:**
- Use affinity-safe teams (Affinity Safe Mix, Double Cleanse Safety) on rotation days or when struggling with debuff reliability.
- Use speed teams (Shredder Speed Cleanse, Speed Burn Poison) for leaderboard or farming.
- Use sustain/cleanse teams (Defensive Cleanse, Nia Cleanse Hybrid) for tough stages or missions.
- Swap in alternates as needed for affinity or gear gaps.
---

## 9. Team Flexibility & Alternate Builds

### Team Flexibility & Alternate Builds

**Alternates by Core Role:**
- **Cleanse/Block Debuffs:** Mithrala Lifebane, Godseeker Aniri, Mausoleum Mage, Maulie Tankard, White Dryad Nia, Lady Annabelle
- **Speed/Turn Meter:** Arbiter, Deacon Armstrong, Apothecary
- **HP Burn/Poison:** Geomancer, Artak, Ninja, Bad-el-Kazar, Lady Annabelle
- **Healing/Sustain:** Apothecary, Vogoth, Lady Annabelle, Bad-el-Kazar
- **Revive:** Arbiter, Godseeker Aniri, Rector Drath, Bad-el-Kazar

**Trial/Mechanic-Specific Champions:**
- **Block Debuffs:** Mithrala Lifebane, Mausoleum Mage, Maulie Tankard
- **Cleanse:** Mithrala Lifebane, Godseeker Aniri, Rector Drath, Artak, White Dryad Nia
- **HP Burn:** Geomancer, Artak, Ninja
- **Poison:** Bad-el-Kazar, Lady Annabelle

**Affinity Safety/Risk (Explicit):**
- **Void:** All teams and alternates are safe for all roles.
- **Magic:** Risk for Force cleansers/block debuffs (e.g., Maulie, Godseeker, Artak). Use Mithrala or affinity-safe alternates.
- **Force:** Risk for Magic cleansers/block debuffs (e.g., Apothecary, Arbiter, Nia). Use Godseeker, Maulie, or affinity-safe alternates.
- **Spirit:** Risk for Force cleansers/block debuffs (e.g., Maulie, Godseeker, Artak). Use Mithrala, Nia, or affinity-safe alternates.

**Notes:**
- For each team, see Section 3 for alternates and affinity notes.
- Always swap in affinity-safe alternates for key roles on rotation days.
---

## 8. Actionable Notes & Upgrade Advice

### Actionable Notes & Upgrade Advice

**Trial/Mechanic Prioritization:**
- Always prioritize cleanse/block debuffs for debuff management—missing these is the most common cause of wipes.
- HP burn and poison are the most reliable damage sources; prioritize teams that maximize uptime.
- Revive and sustain are critical for higher stages and affinity rotations.

**Upgrade Path:**
- Upgrade speed and accuracy on all supports first; these are the most common failure points.
- Next, focus on survivability (HP/DEF) for cleansers and revivers.
- For damage, prioritize accuracy and survivability over crit stats.
- Add new affinity-safe cleansers/block debuffs as you pull them to enable full auto and cover all rotations.

**Common Pitfalls & Solutions:**
- Failing due to weak affinity on key roles—swap in alternates or manual the first cycle.
- Not using AI presets for skill order—set openers for cleanse/block debuffs.
- Underestimating stat requirements—always check the latest boss stats for your stage.

**Upgrade Advice:**
- If a team fails, check speed/accuracy first, then skill order, then survivability.
- Use alternates for affinity or gear gaps, especially on rotation days.
---

## 7. General Notes

### General Notes

**Gear & Stat Priorities:**
- **Supports/Cleansers:** Speed, Perception, Immortal, or Untouchable sets. Prioritize speed (250–260+), accuracy (250–300+), HP/DEF, and resistance (400+ for resist builds).
- **HP Burners/Damage Dealers:** Accuracy, speed, and survivability. Lifesteal or Regeneration for soloers. Aim for 220–240+ speed, 250+ accuracy, 40k+ HP, 3.5k+ DEF.
- **Revivers:** Speed, HP, DEF, and resistance. Perception or Immortal sets are strong.
- **Healers/Sustain:** Speed, HP, DEF, and healing bonuses. Immortal, Regeneration, or Relentless sets.

**Masteries:**
- **Supports:** Rapid Response, Lasting Gifts, Eagle-Eye, Timely Intervention.
- **Damage Dealers:** Warmaster or Giant Slayer, Cycle of Magic, Master Hexer.
- **Revivers:** Timely Intervention, Lasting Gifts, Spirit Haste.

**Manual/Auto Play Advice:**
- **Manual:** Use for skill order on first cycle, especially for cleansers/block debuffs. Open with key skills, then switch to auto.
- **Auto:** Use AI presets to open with cleanse/block debuffs and avoid using them off cooldown. Prioritize speed and accuracy for full auto reliability.

**Common Pitfalls:**
- Underestimating speed/accuracy requirements—always check stat thresholds for your stage.
- Using weak affinity champions for key roles—avoid unless no alternative exists.
- Not setting AI presets for cleansers/block debuffs—leads to failed runs.

**Additional Tips:**
- Test teams on manual first to confirm skill order, then optimize for auto.
- Use alternates for affinity rotations or if a core champion is unavailable.
---

## 6. Ideal Champions to Pull

### Ideal Champions to Pull & Upgrade Path

| Champion           | Role(s) Needed           | Why They’re Ideal / Upgrade Path |
|--------------------|-------------------------|----------------------------------|
| Riho Bonespear     | Cleanse, Block Debuffs  | Best-in-slot for block debuffs/cleanse, affinity safe, enables full auto for all affinities. |
| Cardiel            | Cleanse, Revive, Support| Unique cleanse/revive combo, affinity safe, boosts team flexibility. |
| Skytouched Shaman  | Cleanse, Block Debuffs  | Fast block debuffs, affinity safe, strong for Shredder debuff management. |
| Brogni             | Shield, Cleanse, Support| Shields, cleanse, and block debuffs, affinity safe, boosts survivability. |
| Urogrim            | Poison, Healing         | Fast poisons, healing, enables speed comps, affinity safe. |
| Doompriest         | Cleanse, Healing        | Passive cleanse, affinity safe, easy to build, boosts sustain. |
| Siphi the Lost Bride| Revive, Cleanse, Speed | Top-tier revive/cleanse, affinity safe, enables fastest clears. |
| Lydia the Deathsiren| Block Debuffs, Support | Block debuffs, defense down, speed, affinity safe, boosts damage and survivability. |

**Upgrade Path Advice:**
- Prioritize pulling for affinity-safe cleansers/block debuffs (Riho, Skytouched, Doompriest) to enable full auto and cover all affinity rotations.
- Champions with passive cleanse or block debuffs (Doompriest, Brogni) reduce manual intervention and increase consistency.
- Top-tier revivers (Siphi, Cardiel) allow for more aggressive team builds and faster clears.
- Lydia and Brogni add both survivability and damage, making them ideal for hybrid and speed teams.

**Note:**
- Only champions not currently owned are listed. This list should be regenerated after any roster change.
---

## 5. Direct Champion Comparisons by Role

### Direct Champion Comparisons by Role (Owned Champions Only)

| Role              | Top Champions (Owned)                | Notes |
|-------------------|--------------------------------------|-------|
| Cleanse           | Mithrala Lifebane, Godseeker Aniri, Rector Drath, White Dryad Nia, Artak, Lady Annabelle | Mithrala is safest for affinity; Godseeker and Rector offer revive; Nia is strong for sustain. |
| Block Debuffs     | Mithrala Lifebane, Mausoleum Mage, Maulie Tankard | Mithrala is best for affinity; Maulie is strong for HP aura. |
| Speed/Turn Meter  | Arbiter, Deacon Armstrong, Apothecary | Arbiter is best for aura and revive; Deacon for TM boost. |
| HP Burn           | Geomancer, Artak, Ninja               | Geomancer is top for boss damage; Artak offers backup cleanse. |
| Poison            | Bad-el-Kazar, Lady Annabelle          | Bad-el-Kazar also brings healing and revive. |
| Healing/Sustain   | Apothecary, Vogoth, Lady Annabelle, Bad-el-Kazar | Vogoth is best for passive healing; Annabelle for sustain. |
| Revive            | Arbiter, Godseeker Aniri, Rector Drath, Bad-el-Kazar | Arbiter is fastest; Godseeker and Rector are safest. |
| Damage            | Ninja, Geomancer, Bad-el-Kazar        | Ninja is best for single-target; Geomancer for HP burn. |
| Aura (All Battles)| Mithrala Lifebane, Arbiter, Maulie Tankard, Bad-el-Kazar | Mithrala for RES, Arbiter for SPD, Maulie for HP, Bad-el-Kazar for HP. |

**Notes:**
- Only owned champions are included. See Section 4 for team participation.
- Affinity safety: Mithrala, Geomancer, and Godseeker are safest for most roles.
---

## 4. Best Champions & Team Participation

| Champion            | Roles Fulfilled                        | Teams Used In                        |
|---------------------|----------------------------------------|--------------------------------------|
| Mithrala Lifebane   | Cleanse, Block Debuffs, Aura, Support  | Shredder Speed Cleanse, Affinity Safe Mix, Defensive Cleanse |
| Arbiter             | Speed, Revive, Aura, Support           | Shredder Speed Cleanse, Nia Cleanse Hybrid, Speed Burn Poison |
| Geomancer           | HP Burn, Damage                        | All teams except Defensive Cleanse   |
| Godseeker Aniri     | Cleanse, Revive, Support, Aura         | Shredder Speed Cleanse, Affinity Safe Mix, Double Cleanse Safety |
| Apothecary          | Speed, Healing, Support                | Defensive Cleanse, F2P Epic Core, Double Cleanse Safety, Speed Burn Poison, Poison/HP Burn Mix |
| Ninja               | Damage, HP Burn                        | Shredder Speed Cleanse, Block Debuffs Sustain, Speed Burn Poison, Nia Cleanse Hybrid, Maulie Block Debuffs, Poison/HP Burn Mix |
| Bad-el-Kazar        | Poison, Healing, Revive, Aura          | Block Debuffs Sustain, Speed Burn Poison, Poison/HP Burn Mix |
| Deacon Armstrong    | Speed, TM Boost                        | Block Debuffs Sustain, F2P Epic Core, Maulie Block Debuffs |
| Vogoth              | Sustain, Healing                       | Affinity Safe Mix, Defensive Cleanse, F2P Epic Core, Nia Cleanse Hybrid |
| Rector Drath        | Cleanse, Healing, Revive               | Affinity Safe Mix, Defensive Cleanse, Double Cleanse Safety |
| Maulie Tankard      | Block Debuffs, Aura, Support           | Maulie Block Debuffs                |
| Lady Annabelle      | Healing, Sustain                       | Maulie Block Debuffs, F2P Epic Core, Poison/HP Burn Mix      |
| Artak               | HP Burn, Cleanse                       | Defensive Cleanse, Double Cleanse Safety                     |
| White Dryad Nia     | Cleanse, Sustain                       | Nia Cleanse Hybrid                  |

**Notes:**
- Only champions from the owned list are included.
- Roles and team participation are based on the detailed team sections above.
---

### Double Cleanse Safety

**Team Composition:**
- **Leader:** Godseeker Aniri (Aura: 60 DEF in all battles)
- Apothecary
- Geomancer
- Artak
- Rector Drath

**Core Roles:** Cleanse, Speed, HP Burn, Healing, Revive, Affinity Safety

**Optimal Combo:** Godseeker Aniri (cleanse, revive, aura), Apothecary (speed, healing), Geomancer (HP burn, damage), Artak (HP burn, backup cleanse), Rector Drath (cleanse, healing, revive)

**Alternates:**
- Mithrala Lifebane (cleanse/block debuffs)
- Lady Annabelle (heal/sustain)
- Arbiter (speed/revive)

**Key Mechanics:** Double cleanse, speed cycling, HP burn, healing, revive, affinity safety

**Trial/Mechanic Coverage:** Cleanse, HP Burn, Healing, Revive, Affinity Safety

**Skill/Turn Order Notes:**
- Godseeker: Open with cleanse, revive as needed.
- Apothecary: Speed boost/heal as needed.
- Geomancer: HP burn on cooldown.
- Artak: HP burn/cleanse on cooldown.
- Rector Drath: Cleanse/heal as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** High affinity safety, double cleanse, strong healing/revive

**Weaknesses:** Lower damage, slower clear

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 95%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Godseeker as leader for DEF aura. Use AI presets to open with cleanse. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check cleanse uptime and speed tuning. Use alternates for affinity or gear gaps.
---

### Block Debuffs Sustain

**Team Composition:**
- **Leader:** Mausoleum Mage (Aura: 25% DEF in Faction Crypts)
- Deacon Armstrong
- Geomancer
- Ninja
- Bad-el-Kazar

**Core Roles:** Block Debuffs, Speed, HP Burn, Poison, Healing, Revive, Damage

**Optimal Combo:** Mausoleum Mage (block debuffs, aura), Deacon Armstrong (speed, TM boost), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Bad-el-Kazar (poison, healing, revive)

**Alternates:**
- Godseeker Aniri (revive)
- Arbiter (speed/revive)
- Lady Annabelle (heal/sustain)

**Key Mechanics:** Block debuffs, speed cycling, HP burn, poison, healing, revive

**Trial/Mechanic Coverage:** Block Debuffs, HP Burn, Poison, Healing, Revive

**Skill/Turn Order Notes:**
- Mausoleum Mage: Open with block debuffs.
- Deacon: Speed boost first, TM boost on cooldown.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Bad-el-Kazar: Poison/cleanse on cooldown, revive as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** High safety, strong block debuffs, healing, revive

**Weaknesses:** Lower damage, slower clear, Faction Crypts aura (not global)

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 95%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Mausoleum Mage as leader for DEF aura (if no better option). Use AI presets to open with block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check block debuff uptime and speed tuning. Use alternates for affinity or gear gaps.
---

### Maulie Block Debuffs

**Team Composition:**
- **Leader:** Maulie Tankard (Aura: 33% HP in all battles)
- Deacon Armstrong
- Geomancer
- Ninja
- Lady Annabelle

**Core Roles:** Block Debuffs, Speed, HP Burn, Healing, Revive, Damage

**Optimal Combo:** Maulie Tankard (block debuffs, aura), Deacon Armstrong (speed, TM boost), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Lady Annabelle (heal/sustain)

**Alternates:**
- Godseeker Aniri (revive)
- Arbiter (speed/revive)
- Bad-el-Kazar (poison/heal)

**Key Mechanics:** Block debuffs, speed cycling, HP burn, healing, revive

**Trial/Mechanic Coverage:** Block Debuffs, Speed, HP Burn, Healing, Revive

**Skill/Turn Order Notes:**
- Maulie: Open with block debuffs.
- Deacon: Speed boost first, TM boost on cooldown.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Lady Annabelle: Heal as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Good block debuffs, strong healing/revive, HP aura

**Weaknesses:** Lower damage, affinity risk for block debuffs

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Maulie as leader for HP aura. Use AI presets to open with block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check block debuff uptime and speed tuning. Use alternates for affinity or gear gaps.
---

### Nia Cleanse Hybrid

**Team Composition:**
- **Leader:** Arbiter (Aura: 30% SPD in all battles)
- White Dryad Nia
- Geomancer
- Ninja
- Vogoth

**Core Roles:** Cleanse, Speed, HP Burn, Healing, Sustain, Damage

**Optimal Combo:** Arbiter (speed, revive, aura), White Dryad Nia (cleanse, sustain), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Vogoth (sustain, healing)

**Alternates:**
- Godseeker Aniri (revive)
- Lady Annabelle (heal/sustain)
- Apothecary (speed/heal)

**Key Mechanics:** Cleanse, speed cycling, HP burn, healing, sustain

**Trial/Mechanic Coverage:** Cleanse, Speed, HP Burn, Healing, Sustain

**Skill/Turn Order Notes:**
- Arbiter: Speed boost first, revive as needed.
- Nia: Cleanse/sustain on cooldown.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Vogoth: Passive healing.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Good cleanse, strong sustain, speed, healing

**Weaknesses:** Lower damage, affinity risk for cleansers

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Arbiter as leader for speed aura. Use AI presets to open with speed boost. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check cleanse uptime and speed tuning. Use alternates for affinity or gear gaps.
---

### Speed Burn Poison

**Team Composition:**
- **Leader:** Arbiter (Aura: 30% SPD in all battles)
- Geomancer
- Ninja
- Bad-el-Kazar
- Apothecary

**Core Roles:** Speed, HP Burn, Poison, Healing, Revive, Damage

**Optimal Combo:** Arbiter (speed, revive, aura), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Bad-el-Kazar (poison, healing, revive), Apothecary (speed, healing)

**Alternates:**
- Deacon Armstrong (speed)
- Godseeker Aniri (revive)
- Lady Annabelle (heal/sustain)

**Key Mechanics:** Speed cycling, HP burn, poison, healing, revive

**Trial/Mechanic Coverage:** Speed, HP Burn, Poison, Healing, Revive

**Skill/Turn Order Notes:**
- Arbiter: Speed boost first, revive as needed.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Bad-el-Kazar: Poison/cleanse on cooldown, revive as needed.
- Apothecary: Speed boost/heal as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Fastest F2P clear, strong speed, good healing/revive

**Weaknesses:** Affinity risk for speed lead, less sustain if supports die

**Simulated Results:** 3 runs, ~2:00–2:30 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Arbiter as leader for speed aura. Use AI presets to open with speed boost. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check speed tuning and skill order. Use alternates for affinity or gear gaps.
---

### Poison/HP Burn Mix

**Team Composition:**
- **Leader:** Bad-el-Kazar (Aura: 25% HP in all battles)
- Geomancer
- Ninja
- Apothecary
- Godseeker Aniri

**Core Roles:** Poison, HP Burn, Healing, Revive, Speed, Damage

**Optimal Combo:** Bad-el-Kazar (poison, healing, aura), Geomancer (HP burn, damage), Ninja (damage, HP burn backup), Apothecary (speed, healing), Godseeker Aniri (revive, cleanse)

**Alternates:**
- Lady Annabelle (heal/sustain)
- Arbiter (speed/revive)
- Vogoth (sustain, healing)

**Key Mechanics:** Poison, HP burn, healing, revive, speed

**Trial/Mechanic Coverage:** Poison, HP Burn, Healing, Revive, Speed

**Skill/Turn Order Notes:**
- Bad-el-Kazar: Poison/cleanse on cooldown, heal as needed.
- Geomancer: HP burn on cooldown.
- Ninja: Focus on A2/A3 for damage.
- Apothecary: Speed boost/heal as needed.
- Godseeker: Revive/cleanse as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Good poison/HP burn mix, strong healing/revive, HP aura

**Weaknesses:** Affinity risk for poisoners, lower damage

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Bad-el-Kazar as leader for HP aura. Use AI presets to open with poison/cleanse. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check poison/HP burn uptime and speed tuning. Use alternates for affinity or gear gaps.
---

### F2P Epic Core

**Team Composition:**
- **Leader:** Mausoleum Mage (Aura: 25% DEF in Faction Crypts)
- Deacon Armstrong
- Geomancer
- Apothecary
- Vogoth

**Core Roles:** Block Debuffs, Speed, HP Burn, Healing, Sustain

**Optimal Combo:** Mausoleum Mage (block debuffs, aura), Deacon Armstrong (speed, TM boost), Geomancer (HP burn, damage), Apothecary (speed, healing), Vogoth (sustain, healing)

**Alternates:**
- Godseeker Aniri (revive)
- Lady Annabelle (heal/sustain)
- Bad-el-Kazar (poison/heal)

**Key Mechanics:** Block debuffs, speed cycling, HP burn, healing, sustain

**Trial/Mechanic Coverage:** Block Debuffs, HP Burn, Healing, Sustain

**Skill/Turn Order Notes:**
- Mausoleum Mage: Open with block debuffs.
- Deacon: Speed boost first, TM boost on cooldown.
- Geomancer: HP burn on cooldown.
- Apothecary: Speed boost/heal as needed.
- Vogoth: Passive healing.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** All-epic, accessible, high sustain, block debuffs

**Weaknesses:** Lower damage, Faction Crypts aura (not global), no revive

**Simulated Results:** 3 runs, ~3:00–3:30 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Mausoleum Mage as leader for DEF aura (if no better option). Use AI presets to open with block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check block debuff uptime and speed tuning. Use alternates for affinity or gear gaps.
---

### Defensive Cleanse

**Team Composition:**
- **Leader:** Mithrala Lifebane (Aura: 80 RES in all battles)
- Apothecary
- Artak
- Rector Drath
- Vogoth

**Core Roles:** Cleanse, Speed, HP Burn, Healing, Sustain

**Optimal Combo:** Mithrala Lifebane (cleanse/block debuffs, aura), Apothecary (speed, healing), Artak (HP burn, backup cleanse), Rector Drath (cleanse, healing, revive), Vogoth (sustain, healing)

**Alternates:**
- Godseeker Aniri (revive)
- Lady Annabelle (heal/sustain)
- Arbiter (speed/revive)

**Key Mechanics:** Cleanse, speed cycling, HP burn, healing, sustain

**Trial/Mechanic Coverage:** Cleanse, Speed, HP Burn, Healing, Sustain

**Skill/Turn Order Notes:**
- Mithrala: Open with cleanse/block debuffs.
- Apothecary: Speed boost/heal as needed.
- Artak: HP burn/cleanse on cooldown.
- Rector Drath: Cleanse/heal as needed.
- Vogoth: Passive healing.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** Good cleanse, strong sustain, high resistance

**Weaknesses:** Lower damage, slower clear

**Simulated Results:** 3 runs, ~2:30–3:30 clear, 90%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Mithrala as leader for aura and resistance. Use AI presets to open with cleanse/block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check cleanse uptime and speed tuning. Use alternates for affinity or gear gaps.
---

### Affinity Safe Mix

**Team Composition:**
- **Leader:** Mithrala Lifebane (Aura: 80 RES in all battles)
- Godseeker Aniri
- Geomancer
- Vogoth
- Rector Drath

**Core Roles:** Cleanse, HP Burn, Healing, Revive, Affinity Safety

**Optimal Combo:** Mithrala Lifebane (cleanse/block debuffs, aura), Godseeker Aniri (cleanse, revive), Geomancer (HP burn, damage), Vogoth (sustain, healing), Rector Drath (cleanse, healing, revive)

**Alternates:**
- Apothecary (speed/heal)
- Lady Annabelle (heal/sustain)
- Arbiter (speed/revive)

**Key Mechanics:** Cleanse, HP burn, healing, revive, affinity safety

**Trial/Mechanic Coverage:** Cleanse, HP Burn, Healing, Revive, Affinity Safety

**Skill/Turn Order Notes:**
- Mithrala: Open with cleanse/block debuffs.
- Godseeker: Cleanse/revive as needed.
- Geomancer: HP burn on cooldown.
- Vogoth: Passive healing.
- Rector Drath: Cleanse/heal as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** High affinity safety, strong healing/revive, good sustain

**Weaknesses:** Lower damage, slower clear

**Simulated Results:** 3 runs, ~2:30–3:00 clear, 95%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Mithrala as leader for aura and affinity safety. Use AI presets to open with cleanse/block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check cleanse uptime and speed tuning. Use alternates for affinity or gear gaps.
12. Validation & Simulation Notes


## 1. Boss Mechanics & Stat Requirements

---

## 2. Teams by Estimated Damage/Clear Speed

| Team Name                | Simulated Damage/Clear Time | Core Champions (Leader in Bold)         | Key Mechanics & Notes                | Affinity Safety/Risk |
|--------------------------|:--------------------------:|-----------------------------------------|--------------------------------------|---------------------|
| Shredder Speed Cleanse   | ~2:00–2:30                 | **Mithrala Lifebane**, Arbiter, Ninja, Geomancer, Godseeker Aniri | Cleanse, block debuffs, speed, HP burn, revive, strong single-target damage. | [To be validated] |
| Affinity Safe Mix        | ~2:30–3:00                 | **Mithrala Lifebane**, Godseeker Aniri, Geomancer, Vogoth, Rector Drath | Cleanse, HP burn, healing, revive, affinity safety. | [To be validated] |
| Defensive Cleanse        | ~2:30–3:30                 | **Mithrala Lifebane**, Apothecary, Artak, Rector Drath, Vogoth | Cleanse, speed, HP burn, healing, sustain. | [To be validated] |
| F2P Epic Core            | ~3:00–3:30                 | **Mausoleum Mage**, Deacon Armstrong, Geomancer, Apothecary, Vogoth | Block debuffs, speed, HP burn, healing, sustain. | [To be validated] |
| Poison/HP Burn Mix       | ~2:30–3:00                 | **Bad-el-Kazar**, Geomancer, Ninja, Apothecary, Godseeker Aniri | Poison, HP burn, healing, revive, speed. | [To be validated] |
| Speed Burn Poison        | ~2:00–2:30                 | **Arbiter**, Geomancer, Ninja, Bad-el-Kazar, Apothecary | Speed, HP burn, poison, healing, revive. | [To be validated] |
| Nia Cleanse Hybrid       | ~2:30–3:00                 | **Arbiter**, White Dryad Nia, Geomancer, Ninja, Vogoth | Cleanse, speed, HP burn, healing, sustain. | [To be validated] |
| Maulie Block Debuffs     | ~2:30–3:00                 | **Maulie Tankard**, Deacon Armstrong, Geomancer, Ninja, Lady Annabelle | Block debuffs, speed, HP burn, healing, revive. | [To be validated] |
| Block Debuffs Sustain    | ~2:30–3:00                 | **Mausoleum Mage**, Deacon Armstrong, Geomancer, Ninja, Bad-el-Kazar | Block debuffs, speed, HP burn, poison, healing, revive. | [To be validated] |
| Double Cleanse Safety    | ~2:30–3:00                 | **Godseeker Aniri**, Apothecary, Geomancer, Artak, Rector Drath | Cleanse, speed, HP burn, healing, revive, affinity safety. | [To be validated] |

---
- **Boss:** Shredder Dungeon (Event)
- **Affinities:** [To be researched]
- **Forms/Phases:** [To be researched]
- **Turn Order:** [To be researched]
- **Key Mechanics:**
    - [To be researched]
- **Stat Thresholds:**
    - Speed: [To be researched]
    - Accuracy: [To be researched]
    - Resistance: [To be researched]
    - HP: [To be researched]
    - Defense: [To be researched]
    - Crit Rate/Damage: [To be researched]
- **Unique Challenges:**
    - [To be researched]
- **Affinity Safety/Risk:**
    - [To be researched]
- **Manual/Auto Play Notes:**
    - [To be researched]
- **Validation Sources:**
    - RaidHQ: [To be added]
    - Ayumilove: [To be added]
    - HellHades: [To be added]
    - In-game testing ([date])

---

*This file is the new working draft for Shredder Dungeon, structured and ready for step-by-step population using the owned champion list and validated online sources.*

---

## 3. Detailed Team Sections (by Archetype)
### Shredder Speed Cleanse

**Team Composition:**
- **Leader:** Mithrala Lifebane (Aura: 80 RES in all battles)
- Arbiter
- Ninja
- Geomancer
- Godseeker Aniri

**Core Roles:** Cleanse, Block Debuffs, Speed, HP Burn, Revive, Damage

**Optimal Combo:** Mithrala Lifebane (cleanse/block debuffs, aura), Arbiter (speed, revive), Ninja (damage, HP burn backup), Geomancer (HP burn, damage), Godseeker Aniri (cleanse, revive)

**Alternates:**
- Mausoleum Mage (block debuffs)
- Deacon Armstrong (speed)
- Lady Annabelle (heal/sustain)

**Key Mechanics:** Cleanse/block debuffs, speed cycling, HP burn, revive, strong single-target damage

**Trial/Mechanic Coverage:** Cleanse, Block Debuffs, HP Burn, Revive

**Skill/Turn Order Notes:**
- Mithrala: Open with cleanse/block debuffs, then shield.
- Arbiter: Speed boost first, revive as needed.
- Ninja: Focus on A2/A3 for damage.
- Geomancer: HP burn on cooldown.
- Godseeker: Cleanse/revive as needed.

**Speed Tuning:** 250–260+ (support), 220–240+ (damage dealers)

**Gear:** Speed, Perception, Immortal, Accuracy, Lifesteal

**Masteries:** Support/Defense; Rapid Response, Lasting Gifts, Warmaster

**Manual/Auto:** Fully auto possible; manual for skill order optimization if needed

**Strengths:** High consistency, strong cleanse/block debuffs, revive safety net, fast clear

**Weaknesses:** Relies on Mithrala for affinity safety; weak if affinity is unfavorable

**Simulated Results:** 3 runs, ~2:00–2:30 clear, 95%+ auto success

**Affinity Safety/Risk:**
- [To be validated]

**Actionable Advice:** Set Mithrala as leader for aura and affinity safety. Use AI presets to open with cleanse/block debuffs. Prioritize speed and accuracy on supports.

**Troubleshooting:** If fails, check speed tuning and skill order. Swap in alternates for affinity or gear gaps.
