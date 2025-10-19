# RAID Shadow Legends Boss Guide Project Roadmap
## Cursed City & Doom Tower Content Development Plan

**Date Created:** October 17, 2025  
**Status:** 🔄 Planning Phase - Research & Scoping  
**Purpose:** Comprehensive work scope, boss mechanics research, and prioritization for Cursed City and Doom Tower boss guide creation  
**Reference Standards:** All guides follow `Boss_Guide_Template.md` and `.github/copilot-instructions.md` standards

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Cursed City Work Scope](#cursed-city-work-scope)
   - [Boss List & Status](#cursed-city-boss-list--status)
   - [Champion Restrictions (Hard vs Normal)](#champion-restrictions-hard-vs-normal)
   - [Detailed Boss Mechanics](#detailed-cursed-city-boss-mechanics)
   - [Work Estimates](#cursed-city-work-estimates)
3. [Doom Tower Work Scope](#doom-tower-work-scope)
   - [Boss List & Rotation Schedule](#doom-tower-boss-list--rotation-schedule)
   - [Boss Mechanics Details](#detailed-doom-tower-boss-mechanics)
   - [Secret Rooms Overview](#secret-rooms-overview)
   - [Work Estimates](#doom-tower-work-estimates)
4. [Boss Guide Template Standards](#boss-guide-template-standards)
5. [Prioritization Framework](#prioritization-framework)
6. [Total Work Scope Summary](#total-work-scope-summary)
7. [Next Steps & Dependencies](#next-steps--dependencies)
8. [Validation & Data Sources](#validation--data-sources)

---

## Executive Summary

### Project Overview

This roadmap documents the comprehensive work required to create boss guides for **Cursed City** and **Doom Tower** content in RAID Shadow Legends. Based on existing guide patterns (Amius 1,631 lines, Sand Devil 531 lines, Phantom Shogun 2,284 lines, Chimera 929 lines, Hydra 1,246 lines), this project will produce:

- **3 Cursed City boss guides** (district bosses beyond Amius)
- **8 Doom Tower boss guides** (rotation bosses beyond Sand Devil)
- **Total: 11 new comprehensive boss guides**

### Current Status

**✅ Completed Guides:**
- Cursed City: Amius the Lunar Archon (Eclipse Tower Final Boss) - 1,631 lines
- Doom Tower: Sand Devil Hard & Normal (Al-Naemeh) - 531+ lines

**❌ Pending Guides:**
- Cursed City: 3 district bosses (Nether Spider, Scarab King, Eternal Dragon)
- Doom Tower: 8 rotation bosses (Magma Dragon, Scarab King, Nether Spider, Frost Spider, Eternal Dragon, Celestial Griffin, Dreadhorn, Dark Fae)

### Estimated Work Scope

- **Total Lines:** 5,500-8,800 lines across 11 guides
- **Total Time:** 140-210 hours (research, team building, simulation, writing, validation)
- **Average per Guide:** 500-800 lines, 12-20 hours

---

## Cursed City Work Scope

### Cursed City Boss List & Status

Cursed City is a multi-district endgame content area requiring Eclipse Keys to access the final boss. It features Normal and Hard difficulties with unique champion restrictions.

| Boss Name | District | Affinity | Guide Status | Lines | Priority |
|-----------|----------|----------|--------------|-------|----------|
| **Amius the Lunar Archon** | Eclipse Tower (Final Boss) | Void | ✅ Complete | 1,631 | N/A |
| **Nether Spider** | District Boss | Unknown | ❌ Pending | Est. 600-800 | High |
| **Scarab King** | District Boss | Unknown | ❌ Pending | Est. 600-800 | High |
| **Eternal Dragon** | District Boss | Unknown | ❌ Pending | Est. 600-800 | Medium |

### Champion Restrictions (Hard vs Normal)

Based on research from Amius guide and general Cursed City mechanics:

#### **Hard Mode Restrictions**

**Mythical Champion Requirements:**
- **Amius (Eclipse Tower Final Boss):** Mythical champions required to avoid 1-turn stun from Rampant Chaos (A3) skill
  - Non-Mythical champions: Stunned for 1 turn by Rampant Chaos A3
  - Mythical champions: Forced to change form instead (no stun)
- **Implication:** Hard mode teams likely require 1-5 Mythical champions depending on boss mechanics

**Awakening Requirements:**
- **Amius:** Awakening level significantly impacts damage dealt and received
  - Awakened Weakness Passive: -25% damage inflicted (5% per awakening level), +50% damage received (10% per awakening level)
  - **Recommendation:** Level 5-6 Awakened champions for optimal performance
- **Implication:** Hard mode requires Level 4-6 Awakened champions for competitive clear times

**Champion Count/Rarity Restrictions:**
- **Current Data:** No explicit champion count limits documented for Cursed City
- **Hypothesis:** District bosses may have faction, affinity, or rarity restrictions (needs in-game confirmation)

#### **Normal Mode Restrictions**

**More Lenient Requirements:**
- Non-Mythical champions viable for most content
- Lower awakening requirements (Level 1-3 Awakened sufficient)
- No documented rarity or faction restrictions

**Stat Requirements:**
- Lower HP, DEF, ACC thresholds compared to Hard
- Example (extrapolated from Doom Tower patterns):
  - Hard: 300-400 ACC, 60-80k HP, 3.5k+ DEF
  - Normal: 200-250 ACC, 35-50k HP, 2.5k+ DEF

#### **District-Specific Restrictions**

**Hypothesis (Requires Validation):**
- Each Cursed City district may have unique restrictions similar to Doom Tower Secret Rooms
- Possible patterns:
  - District A: Mythical champions only
  - District B: Specific faction requirements (e.g., Banner Lords, Dark Elves)
  - District C: Affinity-locked (e.g., Magic + Void only)
  - District D: Rarity restrictions (Epic + Legendary only)

**Impact on Team Building:**
- Requires diverse champion roster across factions, affinities, and rarities
- Mythical champions become critical for Hard mode progression
- Awakening materials (Glyphs, Blessings) become bottleneck resources

---

### Detailed Cursed City Boss Mechanics

#### **1. Amius the Lunar Archon (Eclipse Tower Final Boss)** ✅ *Complete Guide*

**Affinity:** Void  
**Forms:** Two-form boss (Base Form + Alternate Form)  
**Difficulty:** Hard (recommended Level 5-6 Awakened champions)

**Key Mechanics:**
- **Two-Form System:** Boss switches between Base Form (1st) and Alternate Form (2nd)
  - **CRITICAL:** Must kill boss in Base Form to win (killing in Alternate Form triggers revival loop)
  - Archon's Ascendance Passive: Places Eclipse buff (3 turns, unremovable), revives with 30% HP + 50% TM if killed in Alternate Form
  
- **Debuff→Buff Conversion (Rampant Chaos A3):**
  - In Base Form: Converts ALL stat debuffs to mirrored buffs (Decrease ATK → Increase ATK, Weaken → Strengthen, Heal Reduction → Continuous Heal)
  - Stuns all non-Mythical champions for 1 turn
  - Forces Mythical champions to change form
  - **Strategy:** Apply debuffs ONLY in Alternate Form (Eclipse buff prevents conversion)

- **Cooldown Reduction Danger (Robed In Moonlight Passive):**
  - When enemies decrease skill cooldowns, decreases Archon's Ascendance passive cooldown by 1 turn
  - **AVOID:** Cycle of Magic mastery, Reflex/Impulse/Merciless sets, Refresh accessory, skill-based cooldown reduction
  
- **4 Passive Abilities:**
  1. **Almighty Immunity:** CC immune (stun, freeze, sleep, provoke, block skills, fear, petrification), HP exchange immune, cooldown increase immune
  2. **Almighty Strength:** MAX HP damage capped at 5% per attack (nerfs Armiger, Coldheart, Royal Guard, Geomancer)
  3. **Awakened Weakness:** -25% damage inflicted (5% per awakening level), +50% damage received (10% per awakening level)
  4. **Hidden Skill:** -90% Poison damage, -70% Smite damage, immune to Decrease SPD and TM reduction

**Hard Mode Stats:**
- HP: 4,203,968
- ATK: 20,179
- DEF: 11,210
- SPD: 250
- Crit Rate: 50%
- Crit Damage: 100%
- RES: 450
- ACC: 550

**Recommended Team Composition:**
- Mythical champions (3-5) to avoid stun mechanic
- High awakening levels (5-6) for damage output
- Cleansers/Block Debuffs for Enfeeble management
- NO cooldown reduction effects anywhere in team

---

#### **2. Nether Spider (Cursed City District Boss)** ❌ *Pending Guide*

**Affinity:** Unknown (likely Spirit, Force, or Void)  
**Location:** Cursed City District (specific district unknown)  
**Difficulty:** Hard + Normal modes expected

**Hypothesized Mechanics (Based on Doom Tower Nether Spider + Cursed City Patterns):**

**Unique Passive - Always Attacks First:**
- Similar to Doom Tower Agreth, Cursed City Nether Spider likely has passive that allows first turn regardless of champion speed
- **Implication:** Speed tuning less critical, survival and first-turn defense more important

**High Resist Mechanic:**
- Doom Tower Nether Spider has significantly increased resist when NOT under HP Burn debuff
- **Cursed City Adaptation:** Likely requires 400+ ACC to land debuffs consistently
- HP Burn enabler: Reduces resist to manageable levels (300-350 ACC)

**Mythical Champion Interaction:**
- **Hypothesis:** Nether Spider may have Mythical-only mechanics in Hard mode (e.g., web mechanic that only Mythical champions can break, or poison immunity unless attacked by Mythical champions)

**Recommended Stat Thresholds (Hard Mode Estimate):**
- ACC: 400+ (without HP Burn), 300-350 (with HP Burn)
- HP: 60-80k
- DEF: 3.5k+
- SPD: 200-250
- Awakening: Level 5-6 recommended

**Recommended Champion Types:**
- HP Burn specialists (Ultimate Galek, Wyvernbane, Teela Goremane, Drexthar Bloodtwin)
- High ACC debuffers (Madame Serris, Dhukk the Pierced, Warmaiden)
- Mythical champions (for Hard mode restrictions)
- Revive/sustain supports (Scyl, Arbiter, Duchess)

**Estimated Guide Complexity:** 600-800 lines (similar to Sand Devil 531 lines, but with Mythical restrictions adding complexity)

---

#### **3. Scarab King (Cursed City District Boss)** ❌ *Pending Guide*

**Affinity:** Unknown (likely Force or Spirit)  
**Location:** Cursed City District (specific district unknown)  
**Difficulty:** Hard + Normal modes expected

**Hypothesized Mechanics (Based on Doom Tower Scarab King + Cursed City Patterns):**

**Shield & Counterattack Mechanic:**
- Doom Tower Borgoth has permanent shield that reflects damage when hit
- **Cursed City Adaptation:** Likely has enhanced shield mechanic requiring:
  - Champions with Ally Protection/Shield buffs (Valkyrie, Draconis, Miscreated Monster, Metalshaper)
  - Destroy Set gear to bypass shield regeneration
  - MAX HP destruction champions (Ripper, Little Miss Annie, Dark Elhain)

**Provoke Mechanic:**
- Doom Tower Borgoth provokes allies, forcing them to attack him (and take reflected damage)
- **Cursed City Adaptation:** Likely immune to Provoke himself, but applies Provoke to allies
- **Counter:** Provoke-immune champions (Vergumkaar), high resist builds (400+ RES), or cleansers

**Buff Steal Mechanic:**
- Doom Tower Borgoth steals buffs from allies (Ally Protection, Block Debuffs, shields)
- **Cursed City Adaptation:** May steal Mythical-specific buffs or awakening-based buffs
- **Counter:** Buff-spam strategy (constantly reapply buffs faster than boss can steal)

**Mythical Champion Interaction:**
- **Hypothesis:** Scarab King may require Mythical champions to deal meaningful damage (non-Mythical attacks reduced by 75%, similar to Doom Tower damage reduction mechanic)

**Recommended Stat Thresholds (Hard Mode Estimate):**
- HP: 80-100k (high survivability required for counterattack + reflected damage)
- DEF: 4k+ (or low DEF with shields/Ally Protection)
- RES: 400+ (to avoid Provoke)
- ACC: 250-300 (debuffs less critical for this boss)
- SPD: 180-220
- Awakening: Level 5-6 recommended

**Recommended Champion Types:**
- Shield/Ally Protection specialists (Valkyrie, Draconis, Metalshaper, Miscreated Monster)
- MAX HP destruction (Ripper, Little Miss Annie, Dark Elhain)
- Destroy Set users (any champion with high multi-hit attacks)
- Mythical champions (for Hard mode damage requirements)
- Provoke-immune or high RES champions (Vergumkaar, Duchess)

**Estimated Guide Complexity:** 700-900 lines (complex mechanics requiring detailed shield/counterattack strategies, higher than Sand Devil)

---

#### **4. Eternal Dragon (Cursed City District Boss)** ❌ *Pending Guide*

**Affinity:** Unknown (likely Magic or Void)  
**Location:** Cursed City District (specific district unknown)  
**Difficulty:** Hard + Normal modes expected

**Hypothesized Mechanics (Based on Doom Tower Eternal Dragon + Cursed City Patterns):**

**High Resist & Debuff Immunity:**
- Doom Tower Iragoth has very high resist and debuff-focused mechanics
- **Cursed City Adaptation:** Likely requires 450+ ACC in Hard mode, or specific debuff immunity bypass mechanics
- May have phases where debuffs are completely immune vs phases where debuffs are critical

**Buff-Based Damage Scaling:**
- Doom Tower Eternal Dragon rewards buff-heavy strategies
- **Cursed City Adaptation:** Boss damage may scale with number of buffs on boss OR number of debuffs on allies
- **Strategy:** Either buff-spam to maximize team damage, or no-buff strategy to minimize boss damage

**Mythical Champion Interaction:**
- **Hypothesis:** Eternal Dragon may require Mythical champions to cleanse specific raid-wide debuffs (e.g., Petrification, True Fear, or custom Cursed City debuffs)

**Recommended Stat Thresholds (Hard Mode Estimate):**
- ACC: 450+ (for debuff-heavy strategy)
- HP: 70-90k
- DEF: 3.5-4k
- RES: 350-400 (to resist debuff waves)
- SPD: 220-250
- Awakening: Level 5-6 recommended

**Recommended Champion Types:**
- High ACC debuffers (Madame Serris, Dhukk, Ursuga Warcaller)
- Buff extenders/buff-heavy champions (Brogni, Siphi, Duchess)
- Cleansers (Reliquary Tender, Godseeker Aniri, Vogoth)
- Mythical champions (for Hard mode cleanse/debuff mechanics)
- Revive champions (for recovery from raid-wide nukes)

**Estimated Guide Complexity:** 600-800 lines (similar to Sand Devil, moderate complexity)

---

### Cursed City Work Estimates

| Boss | Estimated Lines | Estimated Hours | Priority | Complexity |
|------|----------------|-----------------|----------|------------|
| Nether Spider | 600-800 | 15-20 | High | Medium-High (Mythical + HP Burn) |
| Scarab King | 700-900 | 18-22 | High | High (Shield + Counterattack + Mythical) |
| Eternal Dragon | 600-800 | 15-20 | Medium | Medium (High Resist + Debuff) |
| **TOTAL** | **1,900-2,500** | **48-62 hours** | - | - |

**Assumptions:**
- 25-40 lines/hour (includes research, team building, simulation, writing)
- Minimum 3 simulations per team (5-8 teams per boss)
- Champion restriction research adds 2-4 hours per boss
- Mythical champion mechanics add 10-15% complexity vs non-Cursed City bosses

---

## Doom Tower Work Scope

### Doom Tower Boss List & Rotation Schedule

Doom Tower features 132 stages (108 common floors, 12 boss floors, 12 secret rooms) with 30-day rotation cycles. Boss floors occur every 10th stage (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120).

#### **Boss Rotation Cycles**

**Rotation 1 Bosses:**
- Magma Dragon (Kuldath) - Floors 10, 30, 50, 70, 90, 110
- Scarab King (Borgoth) - Floors 20, 40, 60, 80, 100, 120
- Nether Spider (Agreth) - Floors 10, 30, 50, 70, 90, 110 (alternates with Magma Dragon)
- Frost Spider (Sorath) - Floors 20, 40, 60, 80, 100, 120 (alternates with Scarab King)

**Rotation 2 Bosses:**
- Magma Dragon (Kuldath) - Floors 10, 30, 50, 70, 90, 110
- Celestial Griffin (Grythion) - Floors 20, 40, 60, 80, 100, 120
- Nether Spider (Agreth) - Floors 10, 30, 50, 70, 90, 110 (alternates with Magma Dragon)
- Eternal Dragon (Iragoth) - Floors 20, 40, 60, 80, 100, 120 (alternates with Celestial Griffin)

**Rotation 3 Bosses:**
- Dreadhorn (Bommal) - Floors 10, 30, 50, 70, 90, 110
- Scarab King (Borgoth) - Floors 20, 40, 60, 80, 100, 120
- Celestial Griffin (Grythion) - Floors 10, 30, 50, 70, 90, 110 (alternates with Dreadhorn)
- Dark Fae (Astranyx) - Floors 20, 40, 60, 80, 100, 120 (alternates with Scarab King)

**Permanent Boss (All Rotations):**
- Sand Devil (Al-Naemeh) - Appears in Secret Rooms/specific floors ✅ *Guide Complete*

#### **Boss Status Summary Table**

| Boss Name | Full Name | Rotations | Forge Material | Artifact Set | Guide Status | Priority |
|-----------|-----------|-----------|----------------|--------------|--------------|----------|
| **Sand Devil** | Al-Naemeh | All (Permanent) | Lesser/Greater/Superior Oil | N/A (Secret Room boss) | ✅ Complete | N/A |
| **Magma Dragon** | Kuldath | 1, 2 | Magma Cores | Fatal (+15% ATK, +5% C.RATE) | ❌ Pending | High |
| **Scarab King** | Borgoth | 1, 3 | Scarab Claws | Untouchable (+40 RES, 2-turn Immunity) | ❌ Pending | High |
| **Nether Spider** | Agreth | 1, 2 | Nether Eggs | Affinitybreaker (+30% C.DMG, 20% weak→crit) | ❌ Pending | High |
| **Frost Spider** | Sorath | 1 | Frost Spines | Frostbite (15% freeze resist, 10% freeze attacker) | ❌ Pending | Medium |
| **Eternal Dragon** | Iragoth | 2 | Dragon Bones | Bloodthirst (+12% C.RATE, heal 30% damage) | ❌ Pending | Medium |
| **Celestial Griffin** | Grythion | 2, 3 | Griffin Feathers | Guardian (absorb 10% ally damage, heal 10% MAX HP/turn) | ❌ Pending | Medium |
| **Dreadhorn** | Bommal | 3 | Dreadhorn Plates | Fortitude (+10% DEF, +40 RES) | ❌ Pending | Medium |
| **Dark Fae** | Astranyx | 3 | Fae Spheres | Lethal (+25% Ignore DEF, +10% C.RATE) | ❌ Pending | Medium |

---

### Detailed Doom Tower Boss Mechanics

#### **1. Sand Devil (Al-Naemeh)** ✅ *Complete Guides (Hard + Normal)*

**Location:** Sand Devil's Necropolis (Permanent fixture, not part of 3 rotations)  
**Affinity:** Rotates by stage (mod 4 pattern)  
**Difficulty:** Hard (Stages 1-120+), Normal (Stages 1-25)

**Key Mechanics:**
- **Slumber Counter:** Boss wakes after certain hits (8 hits Hard Cursed City, 10 hits Normal, stage-dependent for standard Doom Tower)
- **Debuff Immunity (Passive 1 - Rest of the Wicked):** Immune to ALL debuffs except Sleep
  - When under Sleep: Also immune to stun/freeze/provoke/block skills/fear/true fear/petrification
  - **Damage Reduction by Stage:** 25% (1-5), 50% (6-15), 75% (16-25), 75%+ (26+)
  - **Reduced by 15% per debuff** applied during sleep (key mechanic - maximize debuffs during sleep window)
- **Self-Sleep (A3 - Feasting Swarm):** Boss self-sleeps for 2 turns after A3, guaranteed debuff application window
- **A3 Ignore DEF Nuke:** Ignores Shield/Block Damage/Unkillable/100% DEF, requires 60-80k HP to survive (Hard)

**Affinity Rotation by Stage (mod 4):**
- Stages X mod 4 = 1: Magic (1, 5, 9, 13, 17, 20, 22, 25...)
- Stages X mod 4 = 2: Force (2, 6, 10, 14, 18, 21, 26, 30...)
- Stages X mod 4 = 3: Spirit (3, 7, 11, 15, 23, 27...)
- Stages X mod 4 = 0: Void (4, 8, 12, 16, 23, 28, 32...)

**Hard vs Normal Differences:**
- Slumber Counter: 8 hits (Hard) vs 10 hits (Normal)
- Boss Stats: Significantly higher in Hard
- Stat Requirements: 300-400 ACC, 60-80k HP (Hard) vs 200-250 ACC, 35-50k HP (Normal)
- Damage Output: Significantly higher in Hard

**Guide Status:** ✅ Complete (531+ lines for Hard, separate Normal guide)

---

#### **2. Magma Dragon (Kuldath)** ❌ *Pending Guide*

**Rotations:** 1, 2 (Appears in 2 of 3 rotations)  
**Forge Material:** Magma Cores  
**Artifact Set:** Fatal (+15% ATK, +5% Crit Rate)  
**Priority:** **HIGH** (appears in 2 rotations, Fatal Set highly desirable)

**Key Mechanics (From Ayumilove + HellHades):**

**Hex Debuff Mechanic:**
- Places Hex debuff on champions
- **HP Burn Conversion:** When boss is under HP Burn debuff, Hex converts HP Burn to Continuous Heal (2 turns, 15% heal)
- **Strategy:** AVOID HP Burn champions, use alternative debuffs (Poison, Decrease DEF, Weaken)

**Immune to Turn Meter Reduction:**
- TM reduction effects do NOT work (Armiger, Alure, Coldheart TM reduction useless)
- **Implication:** Speed tuning and CC more critical than TM manipulation

**Cleanse Mechanic:**
- Boss cleanses debuffs periodically (exact trigger unknown, likely turn-based or HP threshold)
- **Strategy:** Reapply debuffs quickly, debuffers with 3-turn cooldown or lower preferred

**Stage-Based Scaling:**
- Boss stats increase significantly from Floor 10 → Floor 110
- Floor 110 Hard requires optimized gear (4.5k+ DEF, 80k+ HP, 250+ SPD)

**Recommended Stat Thresholds (Hard Mode Floor 90-120):**
- ACC: 350-400
- HP: 70-90k
- DEF: 4-4.5k
- SPD: 220-250
- Crit Damage: 200%+ (for nukers)

**Recommended Champion Types:**
- Poison specialists (Frozen Banshee, Kael, Zavia) - NOT HP Burn
- Decrease DEF/Weaken debuffers (Madame Serris, Dhukk, Warmaiden)
- Cleansers/Block Debuffs (to counter Hex debuff)
- High damage nukers (Trunda, Royal Guard, Rae)
- Provoke specialists (Warchief, Rector Drath) - can lock down boss turn rotation

**Estimated Guide Complexity:** 600-800 lines (moderate mechanics, similar to Sand Devil)

---

#### **3. Scarab King (Borgoth)** ❌ *Pending Guide*

**Rotations:** 1, 3 (Appears in 2 of 3 rotations)  
**Forge Material:** Scarab Claws  
**Artifact Set:** Untouchable (+40 RES, 2-turn Immunity buff)  
**Priority:** **HIGH** (appears in 2 rotations, very difficult boss, Untouchable Set useful for Arena/Hydra)

**Key Mechanics (From Ayumilove + HellHades):**

**Permanent Shield:**
- Boss has permanent shield that reflects damage when hit
- **Spectral Horror Passive:** Damage reduction based on MAX HP reduction:
  - <10% MAX HP reduced: 0% damage taken by allies
  - 10-20% MAX HP reduced: 25% damage taken by allies
  - 20-30% MAX HP reduced: 50% damage taken by allies
  - >30% MAX HP reduced: 100% damage taken by allies (full damage reflected)
- **Strategy:** Keep MAX HP destruction between 10-30% for optimal damage mitigation

**Provoke Mechanic:**
- Boss provokes allies, forcing them to attack him and take reflected damage
- High RES champions (400+) or Provoke-immune champions (Vergumkaar) counter this

**Buff Steal:**
- Steals Ally Protection, Block Debuffs, shields from allies
- **Strategy:** Use buff-spam (constantly reapply faster than steal) or Unkillable buffs (cannot be stolen)

**Recommended Stat Thresholds (Hard Mode Floor 90-120):**
- HP: 80-100k (to survive reflected damage)
- DEF: 4k+ OR use shields/Ally Protection instead
- RES: 400+ (to avoid Provoke)
- ACC: 250-300 (debuffs less critical)
- SPD: 180-220

**Recommended Champion Types:**
- Shield/Ally Protection specialists (Valkyrie, Draconis, Metalshaper, Miscreated Monster, Sir Nicholas)
- MAX HP destruction (Ripper, Little Miss Annie, Dark Elhain, Coldheart)
- Destroy Set users (multi-hit champions like Saurus, Armiger)
- Provoke-immune champions (Vergumkaar)
- High RES supports (Duchess, Brogni)

**Estimated Guide Complexity:** 700-900 lines (very complex mechanics, higher than Sand Devil)

---

#### **4. Nether Spider (Agreth)** ❌ *Pending Guide*

**Rotations:** 1, 2 (Appears in 2 of 3 rotations)  
**Forge Material:** Nether Eggs  
**Artifact Set:** Affinitybreaker (+30% Crit DMG, 20% chance weak hit→crit)  
**Priority:** **HIGH** (appears in 2 rotations, Affinitybreaker useful for affinity-weak debuffers)

**Key Mechanics (From Ayumilove + HellHades):**

**Always Attacks First (Unique Passive):**
- Nether Spider attacks in first turn REGARDLESS of champion speed
- Even 350+ speed Arbiter will not go before Nether Spider
- **Strategy:** First-turn defense critical (shields, Block Damage, Unkillable, high HP)

**High Resist When NOT Under HP Burn:**
- Without HP Burn: Boss has 600+ effective resist (requires 450+ ACC to land debuffs)
- With HP Burn: Boss resist drops to ~300 effective (300-350 ACC sufficient)
- **Strategy:** HP Burn enabler mandatory for debuff-heavy teams

**Multi-Hit Punishment:**
- Multi-hit champions wake boss faster (if Slumber mechanic present)
- **Strategy:** Single-hit or 2-hit champions preferred

**Recommended Stat Thresholds (Hard Mode Floor 90-120):**
- ACC: 400-450 (without HP Burn) OR 300-350 (with HP Burn)
- HP: 70-90k (to survive first-turn nuke)
- DEF: 3.5-4k
- SPD: 200-250 (less critical due to boss always going first)

**Recommended Champion Types:**
- HP Burn specialists (Ultimate Galek, Wyvernbane, Teela Goremane, Drexthar Bloodtwin)
- High ACC debuffers (Madame Serris, Dhukk, Ursuga)
- First-turn defenders (Brogni shields, Wythir Unkillable, Duchess Revive on Death)
- Single-hit champions (avoid multi-hitters like Seer, Trunda A2)

**Estimated Guide Complexity:** 600-800 lines (moderate complexity, HP Burn dependency similar to Sand Devil)

---

#### **5. Frost Spider (Sorath)** ❌ *Pending Guide*

**Rotations:** 1 (Appears in 1 of 3 rotations)  
**Forge Material:** Frost Spines  
**Artifact Set:** Frostbite (15% freeze resist, 10% freeze on attacker)  
**Priority:** **MEDIUM** (1 rotation only, Frostbite Set niche use)

**Key Mechanics (From Ayumilove + HellHades):**

**Revive Mechanic:**
- Boss revives spiderlings when they die
- **Counter 1:** Block Revive champions (Rotos, Fenax, Armiger, Lydia)
- **Counter 2:** HP Burn (prevents revive if spiderlings die with HP Burn active)

**Freeze Debuffs:**
- Boss and spiderlings apply Freeze debuffs (1-2 turns)
- **Strategy:** High resist (350+) or Freeze immunity (Frostbite Set, Blessings)

**Dispel Buffs (A2 - Every 3 Turns):**
- Boss dispels buffs from all allies every 3 turns
- **Strategy:** Buff-spam (reapply faster than dispel) or tankier champions (less buff-dependent)

**Recommended Stat Thresholds (Hard Mode Floor 90-120):**
- ACC: 300-350
- HP: 60-80k
- DEF: 3.5k
- RES: 350+ (to resist Freeze)
- SPD: 220-250

**Recommended Champion Types:**
- HP Burn specialists (Ultimate Galek, Wyvernbane, Drexthar)
- Block Revive champions (Rotos, Fenax)
- Freeze-immune/high RES (Brogni, Duchess)
- Cleansers (Reliquary Tender, Vogoth)

**Estimated Guide Complexity:** 500-700 lines (moderate mechanics, less complex than Scarab King)

---

#### **6. Eternal Dragon (Iragoth)** ❌ *Pending Guide*

**Rotations:** 2 (Appears in 1 of 3 rotations)  
**Forge Material:** Dragon Bones  
**Artifact Set:** Bloodthirst (+12% Crit Rate, heal 30% of damage dealt)  
**Priority:** **MEDIUM** (1 rotation only, Bloodthirst Set useful but not critical)

**Key Mechanics (From Ayumilove + HellHades):**

**High Resist & Debuff Mechanics:**
- Boss has very high resist (500+ effective)
- Requires 450+ ACC to land debuffs consistently
- **Strategy:** High ACC debuffers (400-450 ACC minimum) or buff-heavy strategy (bypass debuffs entirely)

**Buff-Based Damage Scaling (Hypothesis):**
- Boss may reward buff-heavy strategies (damage increases with buffs on team)
- OR punishes buffs (boss damage increases with buffs on boss)
- **Requires In-Game Validation**

**Raid-Wide Nuke (Hypothesis):**
- Boss may have AoE nuke that requires revive/heal recovery
- **Strategy:** Revive champions (Scyl, Arbiter, Duchess) and high HP pools

**Recommended Stat Thresholds (Hard Mode Floor 90-120):**
- ACC: 450+ (for debuff strategy)
- HP: 70-90k
- DEF: 3.5-4k
- RES: 350-400 (to resist boss debuffs)
- SPD: 220-250

**Recommended Champion Types:**
- High ACC debuffers (Madame Serris, Dhukk, Ursuga)
- Buff extenders (Brogni, Siphi, Duchess)
- Cleansers (Reliquary Tender, Godseeker)
- Revive champions (Scyl, Arbiter)

**Estimated Guide Complexity:** 600-800 lines (moderate complexity, similar to Sand Devil)

---

#### **7. Celestial Griffin (Grythion)** ❌ *Pending Guide*

**Rotations:** 2, 3 (Appears in 2 of 3 rotations)  
**Forge Material:** Griffin Feathers  
**Artifact Set:** Guardian (absorbs 10% ally damage, heals 10% MAX HP/turn)  
**Priority:** **MEDIUM** (2 rotations, Guardian Set useful for Clan Boss)

**Key Mechanics (From Ayumilove + HellHades):**

**High Resist & Debuff Immunity (Hypothesis):**
- Similar to Eternal Dragon, likely has very high resist (500+)
- May have phases of complete debuff immunity
- **Strategy:** High ACC (450+) or buff-heavy strategy

**Buff Extension/Buff Punishment (Hypothesis):**
- Boss may extend own buff durations OR steal buffs from allies
- **Strategy:** Buff-spam or minimize buffs depending on mechanic

**Recommended Stat Thresholds (Hard Mode Floor 90-120):**
- ACC: 450+ (for debuff strategy)
- HP: 70-90k
- DEF: 3.5-4k
- RES: 350-400
- SPD: 220-250

**Recommended Champion Types:**
- High ACC debuffers
- Buff-heavy supports (Brogni, Siphi)
- Cleansers
- Revive champions

**Estimated Guide Complexity:** 600-800 lines (moderate complexity, needs in-game validation)

---

#### **8. Dreadhorn (Bommal)** ❌ *Pending Guide*

**Rotations:** 3 (Appears in 1 of 3 rotations)  
**Forge Material:** Dreadhorn Plates  
**Artifact Set:** Fortitude (+10% DEF, +40 RES)  
**Priority:** **MEDIUM** (1 rotation only, Fortitude Set niche use)

**Key Mechanics (From Ayumilove + HellHades):**

**Bomb Mechanic:**
- Boss places Bomb debuffs (2-4 turns, detonates for massive damage)
- **Strategy:** Cleanse bombs immediately OR use Block Debuffs

**Slumber Mechanic (Similar to Sand Devil):**
- Boss likely has Slumber counter (wakes after X hits)
- During sleep: Apply debuffs to reduce damage/enable nukes
- **Strategy:** Debuff-heavy during sleep window

**Recommended Stat Thresholds (Hard Mode Floor 90-120):**
- ACC: 350-400
- HP: 70-90k
- DEF: 3.5-4k
- RES: 300-350
- SPD: 220-250

**Recommended Champion Types:**
- Cleansers (Reliquary Tender, Vogoth, Godseeker)
- Block Debuffs (Duchess, Brogni)
- Debuffers (for sleep window)
- High HP tanks

**Estimated Guide Complexity:** 600-800 lines (moderate complexity, Bomb + Slumber dual mechanic)

---

#### **9. Dark Fae (Astranyx)** ❌ *Pending Guide*

**Rotations:** 3 (Appears in 1 of 3 rotations)  
**Forge Material:** Fae Spheres  
**Artifact Set:** Lethal (+25% Ignore DEF, +10% Crit Rate)  
**Priority:** **MEDIUM** (1 rotation only, Lethal Set useful but less critical than Fatal/Affinitybreaker)

**Key Mechanics (From Ayumilove + HellHades):**

**High Resist & Debuff Mechanics (Hypothesis):**
- Similar to Eternal Dragon/Celestial Griffin
- Requires 450+ ACC for debuff strategy

**Ignore DEF Punishment (Hypothesis):**
- Boss may punish Ignore DEF effects (reflects damage, gains buffs)
- **Strategy:** Avoid Ignore DEF champions OR use alternative damage strategies

**Recommended Stat Thresholds (Hard Mode Floor 90-120):**
- ACC: 450+ (for debuff strategy)
- HP: 70-90k
- DEF: 3.5-4k
- RES: 350-400
- SPD: 220-250

**Recommended Champion Types:**
- High ACC debuffers
- Non-Ignore DEF nukers (pure ATK/Crit DMG scaling)
- Cleansers
- Revive champions

**Estimated Guide Complexity:** 600-800 lines (moderate complexity, needs in-game validation)

---

### Secret Rooms Overview

**Total Secret Rooms:** 24 (12 Normal, 12 Hard)  
**Access:** Requires Silver Keys (1 key per entry, refunded if failed)  
**Rewards:** 2 Silver Keys + 3 Champion Fragments (Epic for Normal, Legendary for Hard)

#### **Secret Room Restriction Types**

Based on Ayumilove data, Secret Rooms have champion restrictions by:
- **Rarity:** Rare, Epic, Legendary only
- **Faction:** Banner Lords, Dark Elves, Skinwalkers, Sacred Order, High Elves, Lizardmen, Orcs, Demonspawn, Barbarians, Ogryn Tribes, Dwarves, Void affinity factions
- **Affinity:** Magic, Force, Spirit, Void, or combinations
- **Role:** Attack, Defense, HP, Support
- **Combinations:** Epic Spirit, Rare Void Attack, etc.

#### **Sample Rotation 1 Hard Secret Rooms**

| Room # | Restriction | Champion Pool Impact |
|--------|-------------|----------------------|
| SR1 | Epic Champions | ~40% of total roster |
| SR2 | Dark Elves | ~8% of total roster |
| SR3 | Defense Champions | ~25% of total roster |
| SR4 | Epic Lizardmen | ~2-3% of total roster (very restrictive) |
| SR5 | Rare Attack Champions | ~15% of total roster |
| SR6 | Support Champions | ~25% of total roster |
| SR7 | High Elves | ~8% of total roster |
| SR8 | Epic Spirit Champions | ~10-12% of total roster |
| SR9 | Demonspawn | ~8% of total roster |
| SR10 | HP Champions | ~25% of total roster |
| SR11 | (Unknown) | - |
| SR12 | (Unknown) | - |

**Implication for Boss Guides:**
- Secret Room strategies can be integrated into boss guides as **quick-reference sections** (e.g., "Secret Room 4: Epic Lizardmen - Recommended Champions: Jareg, Rhazin, Broadmaw")
- OR created as **separate appendix/reference document** listing all Secret Room restrictions and recommended champions per restriction

**Estimated Work for Secret Room Integration:**
- If integrated into boss guides: +50-100 lines per boss guide
- If separate reference document: ~500-800 lines total (covers all 24 Secret Rooms across 3 rotations)

---

### Doom Tower Work Estimates

| Boss | Estimated Lines | Estimated Hours | Priority | Complexity |
|------|----------------|-----------------|----------|------------|
| Magma Dragon | 600-800 | 15-20 | High | Medium (Hex mechanic) |
| Scarab King | 700-900 | 18-22 | High | High (Shield + Counterattack) |
| Nether Spider | 600-800 | 15-20 | High | Medium-High (Always First + HP Burn) |
| Frost Spider | 500-700 | 12-18 | Medium | Medium (Revive + Freeze) |
| Eternal Dragon | 600-800 | 15-20 | Medium | Medium (High Resist) |
| Celestial Griffin | 600-800 | 15-20 | Medium | Medium (High Resist, needs validation) |
| Dreadhorn | 600-800 | 15-20 | Medium | Medium (Bomb + Slumber) |
| Dark Fae | 600-800 | 15-20 | Medium | Medium (High Resist, needs validation) |
| **TOTAL** | **4,800-6,400** | **120-158 hours** | - | - |

**Assumptions:**
- 25-40 lines/hour (includes research, team building, simulation, writing)
- Minimum 3 simulations per team (5-8 teams per boss)
- High Resist bosses (Eternal Dragon, Celestial Griffin, Dark Fae) require additional in-game validation (+2-4 hours each)

---

## Boss Guide Template Standards

All boss guides must follow the canonical template structure defined in `Tools/Boss_Guide_Template.md` and `.github/copilot-instructions.md`.

### **13-Section Standard Structure**

1. **Boss Mechanics & Stat Requirements**
   - Boss overview, affinity rotation, skills, passives
   - Hard vs Normal stat requirements
   - Manual/Auto Play Notes subsection

2. **Champion-to-Mechanics Mapping** (Optional, for mechanic-heavy bosses)
   - Per-mechanic tables (champions who fulfill each mechanic)
   - Combo tables (champions who fulfill multiple mechanics)
   - Affinity safety notes

3. **Teams by Estimated Damage/Clear Speed**
   - Quick reference table with affinity safety/risk column

4. **Detailed Team Recommendations**
   - Team 1-6 (or more) with full specifications:
     - Core Roles
     - Optimal Combo
     - Alternates
     - Speed Tuning & Turn Order
     - Gear
     - Masteries
     - Manual/Auto Compromise (quantified)
     - Strengths
     - Weaknesses
     - Simulated Results
     - Affinity Safety/Risk (multi-line)
     - Turn-by-Turn Skill Usage (phase-by-phase)

5. **Best Champions & Team Participation**
6. **Direct Champion Comparisons by Role**
7. **Ideal Champions to Pull** (non-owned only)
8. **General Notes**
9. **Actionable Notes & Upgrade Advice**
10. **Team Flexibility & Alternates**
11. **When to Use Each Team**
12. **Additional Team Archetypes**
13. **Validation & Simulation Notes**

### **Enhancement Quality Standards**

Per copilot-instructions.md, all guides must include:

✅ **Multi-line affinity safety/risk format** for all teams  
✅ **Cross-validation with 2+ sources** (RaidHQ, Ayumilove, HellHades)  
✅ **Minimum 3 simulations documented per team**  
✅ **Turn-by-turn skill usage** with trial/mechanic checkpoints  
✅ **Auto compromise quantified** (damage %, mechanics lost, success rate)  
✅ **Speed tuning explicit** (turn order with requirements and rationale)

### **Template Streamlining for Pending Guides**

To accelerate guide creation, create **pre-filled templates** with:
- Boss affinity rotation table (mod 4 pattern, pre-calculated for all stages)
- Standard stat requirement ranges (Hard vs Normal)
- Affinity safety/risk table template (multi-line format)
- Turn-by-turn skill usage template (phase-by-phase structure)
- Auto compromise template (damage %, mechanics, success rate)

**Estimated Time Savings:** 2-4 hours per guide (reduces repetitive formatting work)

---

## Prioritization Framework

### **Priority Tiers**

**Tier 1 - HIGH PRIORITY (Do First):**
- **Magma Dragon:** Appears in 2 rotations, Fatal Set highly desirable, moderate complexity
- **Scarab King:** Appears in 2 rotations, very difficult boss, Untouchable Set useful
- **Nether Spider:** Appears in 2 rotations, Affinitybreaker Set useful for affinity-weak debuffers
- **Cursed City Nether Spider:** District boss, high player demand
- **Cursed City Scarab King:** District boss, high difficulty, high player demand

**Tier 2 - MEDIUM PRIORITY (Do Second):**
- **Celestial Griffin:** Appears in 2 rotations, Guardian Set useful for Clan Boss
- **Frost Spider:** Rotation 1 only, Frostbite Set niche but boss mechanics complex
- **Eternal Dragon:** Rotation 2 only, Bloodthirst Set useful
- **Cursed City Eternal Dragon:** District boss, moderate player demand

**Tier 3 - LOW PRIORITY (Do Last):**
- **Dreadhorn:** Rotation 3 only, Fortitude Set niche use
- **Dark Fae:** Rotation 3 only, Lethal Set useful but less critical

### **Sequencing Strategy**

**Phase 1 (High Priority - 40-50 hours):**
1. Magma Dragon (Doom Tower) - 15-20 hours
2. Nether Spider (Doom Tower) - 15-20 hours
3. Scarab King (Doom Tower) - 18-22 hours

**Phase 2 (Cursed City - 48-62 hours):**
4. Nether Spider (Cursed City) - 15-20 hours
5. Scarab King (Cursed City) - 18-22 hours
6. Eternal Dragon (Cursed City) - 15-20 hours

**Phase 3 (Medium Priority - 45-60 hours):**
7. Celestial Griffin (Doom Tower) - 15-20 hours
8. Frost Spider (Doom Tower) - 12-18 hours
9. Eternal Dragon (Doom Tower) - 15-20 hours

**Phase 4 (Low Priority - 30-40 hours):**
10. Dreadhorn (Doom Tower) - 15-20 hours
11. Dark Fae (Doom Tower) - 15-20 hours

**Total Estimated Time:** 163-212 hours across 4 phases

---

## Total Work Scope Summary

### **Guides by Status**

| Category | Status | Count | Estimated Lines | Estimated Hours |
|----------|--------|-------|-----------------|-----------------|
| Cursed City | ✅ Complete | 1 | 1,631 | N/A |
| Cursed City | ❌ Pending | 3 | 1,900-2,500 | 48-62 |
| Doom Tower | ✅ Complete | 1 (2 guides) | 531+ | N/A |
| Doom Tower | ❌ Pending | 8 | 4,800-6,400 | 120-158 |
| **TOTAL** | **Pending** | **11** | **6,700-8,900** | **168-220** |

### **Work Distribution**

**By Priority:**
- High Priority: 5 guides, ~3,100-4,100 lines, ~78-102 hours
- Medium Priority: 4 guides, ~2,300-3,100 lines, ~57-78 hours
- Low Priority: 2 guides, ~1,200-1,600 lines, ~30-40 hours

**By Content Type:**
- Cursed City: 3 guides, ~1,900-2,500 lines, ~48-62 hours
- Doom Tower: 8 guides, ~4,800-6,400 lines, ~120-158 hours

### **Deliverables**

Upon completion, this project will produce:
- **11 comprehensive boss guides** (500-900 lines each)
- **33-88 unique team compositions** (3-8 teams per boss, no duplicate champions)
- **99-264 simulation runs** (minimum 3 per team)
- **11 boss mechanic research documents** (integrated into guides)
- **Champion restriction documentation** (Cursed City Hard vs Normal)

---

## Next Steps & Dependencies

### **Immediate Actions (Week 1)**

1. **Select Phase 1 Boss (Magma Dragon Recommended)**
   - Research boss mechanics from RaidHQ, Ayumilove, HellHades
   - Cross-validate Hex mechanic and HP Burn conversion behavior
   - Test in-game with owned champion roster

2. **Validate Champion Restrictions (Cursed City)**
   - Confirm Mythical requirements for district bosses (in-game testing)
   - Document awakening level impact on damage/survivability
   - Test if district-specific restrictions exist

3. **Create Pre-Filled Templates**
   - Affinity rotation table (mod 4 pattern)
   - Multi-line affinity safety/risk template
   - Turn-by-turn skill usage template
   - Auto compromise template

### **Dependencies**

**External Dependencies:**
- **In-Game Access:** Requires access to Doom Tower Hard floors 90-120 for high-end stat validation
- **Champion Roster:** Requires diverse roster with Mythical champions for Cursed City Hard testing
- **Simulation Tools:** HellHades optimizer, Deadwood Jedi speed calculator for team building

**Internal Dependencies:**
- **Owned Champion List:** Must be up-to-date (`Input/Owned_champion_list.md`)
- **Boss Guide Template:** Must be finalized (`Tools/Boss_Guide_Template.md`)
- **Copilot Instructions:** Must be current (`.github/copilot-instructions.md`)

### **Risk Mitigation**

**Risk 1: Boss Mechanics Change (Plarium Patches)**
- **Mitigation:** Cross-validate mechanics with 3+ sources before writing guide
- **Mitigation:** Document guide creation date and last validation date
- **Mitigation:** Schedule quarterly reviews for mechanic updates

**Risk 2: Champion Roster Changes**
- **Mitigation:** Follow `.github/copilot-instructions.md` Update & Staging Policy
- **Mitigation:** Never overwrite original files, create versioned copies

**Risk 3: Time Overruns**
- **Mitigation:** Use pre-filled templates to save 2-4 hours per guide
- **Mitigation:** Prioritize High Priority guides first (highest ROI)
- **Mitigation:** Batch similar bosses (e.g., all High Resist bosses together for research efficiency)

---

## Validation & Data Sources

### **Primary Data Sources**

**RaidHQ** (Primary for Boss Mechanics)
- URL: https://raid-hq.com/
- Priority: Highest for official boss data, skill descriptions, passive abilities

**Ayumilove** (Primary for Champion Guides)
- URL: https://ayumilove.net/raid-shadow-legends-guide/
- Priority: High for champion skills, gear recommendations, tier lists

**HellHades** (Primary for Team Compositions)
- URL: https://hellhades.com/
- Priority: High for team building strategies, speed tuning, tier lists

**In-Game Testing** (Highest Priority for Validation)
- Direct observation of boss mechanics
- Simulation runs with owned champion roster
- Affinity risk observations (weak hit rates, debuff reliability)

### **Cross-Validation Rules**

Per `.github/copilot-instructions.md`:
- Cross-check all boss and champion data with **at least two sources**
- Document conflicts and prefer community consensus (RaidHQ + Ayumilove/HellHades)
- Mark uncertainties in "Data Confidence" or "Validation & Simulation Notes" sections
- Always cite sources in Markdown file and commit messages

### **Simulation Standards**

**Minimum Simulations per Team:**
- Run at least **3 test runs** per team
- Document results for each run (clear time, damage, mechanics completed)

**What to Document:**
- Average clear time (or fastest, if times vary significantly)
- Average damage score (if applicable)
- Success rate (e.g., 10/10 runs, 7/10 runs)
- Mechanic completion consistency (which mechanics completed in all runs vs some runs)
- Affinity risk observations (e.g., weak hit rate, debuff failure rate)

---

## Appendix: Quick Reference Tables

### **Boss Quick Reference (All Pending Guides)**

| Boss | Type | Rotations | Forge Set | Key Mechanic | Priority | Est. Lines |
|------|------|-----------|-----------|--------------|----------|------------|
| Magma Dragon | Doom Tower | 1, 2 | Fatal | Hex + HP Burn Conversion | High | 600-800 |
| Scarab King | Doom Tower | 1, 3 | Untouchable | Shield + Counterattack | High | 700-900 |
| Nether Spider | Doom Tower | 1, 2 | Affinitybreaker | Always First + HP Burn | High | 600-800 |
| Nether Spider | Cursed City | N/A | N/A | Mythical + HP Burn | High | 600-800 |
| Scarab King | Cursed City | N/A | N/A | Mythical + Shield | High | 700-900 |
| Celestial Griffin | Doom Tower | 2, 3 | Guardian | High Resist | Medium | 600-800 |
| Frost Spider | Doom Tower | 1 | Frostbite | Revive + Freeze | Medium | 500-700 |
| Eternal Dragon | Doom Tower | 2 | Bloodthirst | High Resist | Medium | 600-800 |
| Eternal Dragon | Cursed City | N/A | N/A | Mythical + High Resist | Medium | 600-800 |
| Dreadhorn | Doom Tower | 3 | Fortitude | Bomb + Slumber | Low | 600-800 |
| Dark Fae | Doom Tower | 3 | Lethal | High Resist + Ignore DEF | Low | 600-800 |

### **Stat Requirements by Boss Type (Hard Mode)**

| Boss Type | ACC | HP | DEF | RES | SPD | Awakening |
|-----------|-----|----|----|-----|-----|-----------|
| Slumber (Sand Devil, Dreadhorn) | 300-400 | 60-80k | 3.5-4k | 300-350 | 220-250 | 3-4 |
| HP Burn (Nether Spider, Frost Spider) | 300-450 | 60-80k | 3.5-4k | 300-350 | 200-250 | 3-4 |
| High Resist (Eternal Dragon, Griffin, Fae) | 450+ | 70-90k | 3.5-4k | 350-400 | 220-250 | 4-5 |
| Shield (Scarab King) | 250-300 | 80-100k | 4k+ | 400+ | 180-220 | 4-5 |
| Hex (Magma Dragon) | 350-400 | 70-90k | 4-4.5k | 300-350 | 220-250 | 3-4 |
| Cursed City (All) | 400-450 | 70-100k | 3.5-4.5k | 350-450 | 220-250 | 5-6 |

---

## Document Changelog

- **2025-10-17:** Initial roadmap creation with comprehensive boss mechanics, champion restrictions, work estimates, prioritization, and validation standards. Based on existing guide patterns (Amius 1,631 lines, Sand Devil 531 lines, Phantom Shogun 2,284 lines, Chimera 929 lines, Hydra 1,246 lines). Includes detailed mechanics for all 11 pending guides, champion restriction research for Cursed City Hard vs Normal, boss guide template standards, and 4-phase sequencing strategy.

---

**END OF ROADMAP**
1. update readme using current project info. Drop all items for removed python ex the intake process. Use the current structure, instructions, etc as a guide. This may remove a lot of content from the readme, confirm info is needed as you go. Review need for makefile given current scripts and tools, and extensions/etc. This should be baprt of housekeeping at the end of all phases in a body of work.