# UNM Clan Boss Team Analysis

**Date**: 2025-10-29  
**Version**: 1.1 (Mechanics-Corrected + Goal Update)  
**Status**: READY FOR IMPLEMENTATION ✅  
**Goals**: 
- **Manual**: 80M+ damage per key (2-key UNM)
- **Auto**: 50M+ damage per key (easy 2-key completion)

  ## UNM Boss Stats Reference (CANONICAL)

  | Stat | Value | Impact on Team Building |
  |------|-------|------------------------|
  | **HP** | 1,180,000,000 | Total damage target (50-80 million) |
  | **SPD** | 170 | Determines tune range (171-189). 190 on first turn only. |
  | **ACC** | 250 | Boss debuffs on team (Decrease SPD resistable at 220+ RES) |
  | **RES** | 300 | Team needs 250+ ACC for 90-95% debuff landing |
  | **DEF** | ~3000 (estimated) | Defense calculation baseline |
  | **Stun** | Every 3 turns | CANNOT be resisted, slowest champ targeted |
  | **Poison Cap** | 50k per tick | Limits poison team damage ceiling |
  | **HP Burn Cap** | 75k per tick | Limits HP Burn team damage ceiling |
  | **Boss HP-based Damage Caps** | 10% max HP per proc (Warmaster/Giant Slayer) | Limits mastery proc damage |

  **Key Thresholds:**
  - 1-key team: 70.3M+ damage (max chest + unlocks auto)
  - 2-key team: ~40M+ per run (max chest in 2 keys)
  - Current performance: ~44-50M per run

  ---

  ## ⚡ Critical Mechanics Reference

  ## Clan Boiss First turn
  - On the first turn, the UNM clan boss has 190 speed. For all other turns speed is 170. 
  - Speed tune should target 170, though going ahead of 190 may be preferred.

  ### Clan Boss Stun Mechanic
  - **Frequency**: Every 3 turns
  - **Target**: Slowest champion (should be 191 SPD with high EHP)
  - **Resistable**: NO - 100% land rate regardless of RES stat
  - **Strategy**: Designated stun target (Geomancer at 191 SPD) absorbs all stuns

  ### Clan Boss Immunity List (passive)
  - Immune to (Debuffs and effects):
    - stun
    - freeze
    - sleep
    - decrease speed
    - provoke
    - block active skills
    - lock passive skills
    - fear/true fear
    - petrification 
    - berserk
    - enfeeble
    - nullify
    - max hp destruction
    - turn meter reduction
    - hp exchange

 ### Clan Boss 'Gathering Fury' Passive
 - Starting from the 10th turn, the damage inflicted by all skills increases each turn. 
 - Damage increases by the same percentage each turn, and accumulates over multiple turns. 
 - Starting from turn 20, damage is increased by a greater amount.
 - Starting from turn 50, all attacks ignore block damage and unkillable buffs. This ends unkillable runs.
  
  ### Poison & HP Burn Caps
  - **Poison**: 50k damage per tick maximum
    - Multiple poisons can activate at once. All activate when that champion or boss takes a turn.
    - Poison sensitivity can increase this damage.
    - Poison explosion is usually not as good as sustained poisons.
  - **HP Burn**: 75k damage per tick maximum

  ### Boss HP-based Damage Caps
  - **Warmaster/Giant Slayer**: 75k per 'hit' cap for bonus damage At UNM. This means that the mastery that triggers more often is ideal.

  ### Warmaster & Giant Slayer Masteries
  - **Warmaster**: 60% proc chance per skill activation (not per hit), regardless of crit. See mastery table for damage.
  - **Giant Slayer**: 30% proc chance per hit, regardless of crit See mastery table for damage
  - **Damage Cap**: Both types of bonus damage are capped at 75k per activation. Prefer the mastery that gets more possible activations per boss turn. 
  - **Other Masteries:** late game, other top tier masteries may be more effective for damage based on the champion, gear, role, build, and team.


  ---

## ⚡ **QUICK START: DO THESE 3 FIXES FIRST**

To be Completed After next champion/etc update

---

## Table of Contents

1. [Quick Start: Do These 3 Fixes First](#-quick-start-do-these-3-fixes-first)
2. [Quick Optimization Guide - 3 Steps Per Champion](#quick-optimization-guide---3-steps-per-champion)
3. [Implementation Priority Order](#implementation-priority-order)
4. [Project Goals](#project-goals)
5. [Current Team Performance](#current-team-performance)
6. [Primary Issues Identified](#primary-issues-identified)
7. [UNM Clan Boss Mechanics Reference](#unm-clan-boss-mechanics-reference)
8. [UNM Boss Mechanics - Detailed Analysis](#unm-boss-mechanics---detailed-analysis)
   - [Boss Base Stats](#boss-base-stats)
   - [Damage Scaling Formula](#damage-scaling-formula)
   - [Attack Pattern Sequence](#attack-pattern-sequence)
   - [Stun Mechanics (CRITICAL - Non-Resistable)](#stun-mechanics-critical---non-resistable)
   - [Affinity Rotation & Effects](#affinity-rotation--effects)
   - [Debuff Limit & Priority](#debuff-limit--priority)
   - [Turn Prediction & Survivability Thresholds](#turn-prediction--survivability-thresholds)
   - [Boss Damage Mitigation Stack](#boss-damage-mitigation-stack)
9. [Survivability & Stat Safety Analysis](#survivability--stat-safety-analysis)
   - [Effective HP Calculation](#effective-hp-calculation)
   - [Current Team Effective HP Table](#current-team-effective-hp-table)
   - [HP vs DEF% Boots Trade-Off Analysis](#hp-vs-def-boots-trade-off-analysis)
   - [ACC Safety Thresholds & Debuff Land Rates](#acc-safety-thresholds--debuff-land-rates)
   - [Stun Target Survivability Requirements](#stun-target-survivability-requirements)
   - [Speed Tune Impact on Survivability](#speed-tune-impact-on-survivability)
   - [Champion-Specific Survivability Notes](#champion-specific-survivability-notes)
   - [Survivability Optimization Priority (Phase 2)](#survivability-optimization-priority-phase-2)
10. [Team Archetype Comparison & Realistic Expectations](#team-archetype-comparison--realistic-expectations)
   - [Current Team Archetype: Tanky Buff/Debuff Stack](#current-team-archetype-tanky-buffdebuff-stack)
   - [Alternative Team Archetypes](#alternative-team-archetypes)
   - [Realistic Expectations: Where Does Current Team Rank?](#realistic-expectations-where-does-current-team-rank)
   - [Why Current Team is GOOD (Don't Chase Unrealistic Upgrades)](#why-current-team-is-good-dont-chase-unrealistic-upgrades)
11. [Analysis Workflow](#analysis-workflow)
12. [Reference Documents](#reference-documents)
13. [Champion Intake Progress](#champion-intake-progress)
14. [Champion Documentation](#champion-documentation)
   - [Geomancer - HP Burn DPS Specialist](#geomancer---hp-burn-dps-specialist)
   - [Stag Knight - Decrease DEF/ATK Specialist](#stag-knight---decrease-defattk-specialist)
   - [Brogni - Shield/Cleanse/HP Burn Specialist](#brogni-underpriest-brogni---shieldcleansehp-burn-specialist)
   - [Mithrala - Cleanse/Buff/Lead Specialist](#mithrala---cleansebufflead-specialist)
   - [Godseeker Aniri - Heal/Revive/Buff Extend Specialist](#godseeker-aniri---healrevivebuff-extend-specialist)
15. [Speed Tune Analysis - 1:1 Tune Implementation](#speed-tune-analysis---11-tune-implementation)
16. [Stat Gaps Analysis - UNM Requirements vs Current Team](#stat-gaps-analysis---unm-requirements-vs-current-team)
17. [Ranked Recommendations (Priority 1-10)](#ranked-recommendations-priority-1-10)
18. [Alternates Analysis - Owned Champion Swaps](#alternates-analysis---owned-champion-swaps)
19. [Gear Audit Workflow - Speed Boot Optimization](#gear-audit-workflow---speed-boot-optimization)
20. [Validation & Documentation Standards](#validation--documentation-standards)
21. [Update Notes & Version History](#update-notes--version-history)
22. [Cross-References & Related Files](#cross-references--related-files)
23. [Glossary & Abbreviations](#glossary--abbreviations)

---

## Project Goals

### **Primary Goals (Updated 2025-10-29 for Version 1.1)**

1. **Manual Damage Target**: 44M current → **80M+ per key** (2-key UNM = 160M total)
   - **Rationale**: 2-key UNM gives max rewards (sacred shards, books, etc.)
   - **Achievability**: Current team has all components (HP Burn, Decrease DEF/ATK, shields, cleanse, buff extend)
   - **Path**: Phase 1 (+16-25M) + Phase 2 (+8-12M) + Phase 3 optimizations = 68-81M baseline, manual micro +10-15M = **78-96M potential**

2. **Auto Damage Target**: **50M+ per key** (easy 2-key completion with safety margin)
   - **Rationale**: Auto runs for daily farming without manual babysitting
   - **Achievability**: With proper speed tune (171-189 SPD), AI should maintain buff/debuff rotation
   - **Path**: Phase 1-2 optimizations = 68-81M manual → Auto efficiency ~65-75% = **44-61M auto** ✅

3. **Survival Target**: 30-45 turns current → **50+ turns consistent** (both manual and auto)
   - **Rationale**: More turns = more damage, better reward chance
   - **Path**: Speed tune + EHP improvements (+705k team EHP from regearing) = 50-55 turns realistic

4. **Speed Tune**: Implement 1:1 tune (171-189 SPD) for buff/shield sync
   - **Status**: 1/5 complete (Geomancer 171 SPD ✅), 2/5 almost (Brogni 192, Aniri 199), 2/5 need work (Stag 219, Mithrala 251)

5. **Automation**: Prioritize AUTO-friendly after manual max damage validated
   - **AI Quirks**: Document any manual-only strategies (skill priority, turn targeting)
   - **Testing**: Run 5 auto battles to validate AI behavior after Phase 2 speed tune

6. **Roster Constraint**: Use only owned champions (Champion_stats.md owned>0)
   - **Current Team**: Geomancer, Stag Knight, Brogni, Mithrala, Godseeker Aniri (all owned)
   - **Alternate Option**: Rector Drath (owned) for Path 2B if Mithrala Arena conflict unacceptable

---

## Gear & Resource Availability

### **Available Relics (Key for UNM CB)**

| Relic | Effect | UNM CB Application | Current User |
|-------|--------|-------------------|--------------|
| **Demonic Effigy** | Turn meter +10% when ally dies | Revival synergy (Godseeker Aniri passive, safety net) | **Godseeker Aniri** ✅ |
| **Wand of Submission** | 25% chance to reflect stun debuff | **CRITICAL FOR CB!** Stun protection for key champions | **AVAILABLE** 🎯 |

**Priority Relic Assignment:**
- **Wand of Submission** → **Stag Knight** (Decrease DEF/ATK = most critical debuffer, 25% stun reflect = safety net)
  - OR → **Brogni** (Shield/HP Burn specialist, high value target)
  - Current: Brogni has Gilded Dragonstone (-5% RES for HP Burn, less critical than stun protection)
- **Demonic Effigy** → Keep on Godseeker Aniri ✅ (revive synergy perfect)

### **Available Gear Sets (Quantity & Quality)**

**HIGH AVAILABILITY** (lots of optimized pieces, easy to build):
- **Perception** (4-set: +40 ACC) - ABUNDANT ✅
- **Resilience** (2-set: +10% RES) - ABUNDANT ✅
- **Bolster** (4-set: +1.5k HP per buff on ally) - ABUNDANT ✅
- **Feral** (2-set: +15% SPD) - ABUNDANT ✅

**MEDIUM AVAILABILITY** (decent number, can build 1-2 champions):
- **Relentless** (4-set: 18% chance extra turn) - NOT RECOMMENDED for CB (breaks speed tune)
- **Cruel** (2-set: +15% C.DMG, ignore 5% DEF) - Good for damage dealers
- **Immortal** (2-set: +7.5% HP) - Good for tanks
- **Regeneration** (4-set: +15% HP per turn) - Good for healers/supports
- **Speed** (2-set: +12% SPD) - Useful for speed tune adjustments
- **Lifesteal** (4-set: +30% damage as heal) - **CRITICAL for most CB teams** ✅
- **Swift Parry** (4-set: +15% C.RATE, 4% damage reflect) - Good for crit champions
- **Protection** (2-set: +15% DEF) - Good for tanks
- **Stone Skin** (4-set: Shield 20% HP first turn) - Good for early survivability
- **Defiant** (2-set: +10% RES, +5% C.RATE per debuff max 25%) - Situational
- **Righteous** (2-set: +15% C.RATE) - Good for crit champions
- **Supersonic** (2-set: +10 SPD flat) - Minor speed tune adjustment
- **Merciless** (2-set: +15% C.DMG, +3% C.RATE) - Good for damage dealers

**LOW AVAILABILITY** (maybe 1 full set, not optimized):
- Most other sets available but not well-rolled or incomplete

### **Dungeon/Resource Constraints**

**Spider (Accessories):**
- **Easy:** Farmable ✅
- **Hard:** Up to Stage 6 (Mythic accessories) ✅
- **Limitation:** Can't farm Spider Hard 10+ for high-tier mythics yet.

**Dungeon Bosses (Artifacts):**
- **Easy:** Farmable ✅
- **Hard:** Up to Stage 6 (Mythic accessories) ✅
- **Limitation:** Can't farm Spider Hard 10+ for high-tier mythics yet.

**Sand Devil, Phantom Shogun (ACC Accessories):**
- **Easy:** Farmable to lvl 16 of 25.
- **Limitation:** Can't reliably farm past 15.

**Gear Ascension:**
- **Max Level:** 2-4 stars (Forge/Glyphs)
- **Limitation:** Can't push to 5-6 star ascension yet (high-level dungeons/resources not accessible)
- **Impact:** Can improve gear but not maximize (missing 10-20% potential stats from max ascension)

**Mastery Resets:**
- **Cost:** 300 gems per champion
- **Availability:** ~1 week of gathering per reset
- **Impact:** Can change masteries as needed, but resource-limited (prioritize high-impact resets)

### **Gear Optimization Strategy (Based on Availability)**
- Maintain this section as issues are identified, remediated, and updated through the analysis process.

**IMMEDIATE FIXES (High Availability, Easy Swaps):**
To be completed after analysis

**MEDIUM-TERM BUILDS (1-2 weeks, use Medium Availability sets):**
To be completed after analysis

**LONG-TERM OPTIMIZATIONS (Resource-Limited):**
To be completed after analysis

### **Gear Set Recommendations by Champion (Based on Availability)**
- Maintain this section as issues are identified, remediated, and updated through the analysis process.

| Champion | Current Sets | Recommended Sets | Priority Changes |
|----------|-------------|------------------|------------------|
| **Geomancer** | | | |
| **Stag Knight** | | | |
| **Brogni** | | | |
| **Mithrala** | | | |
| **Godseeker Aniri** | | | |

**Key Takeaway:** 

---

## Current Team Performance
 - **VALIDATED 2025-10-30**: 53M damage confirmed in test run with current stats

- **Team**:  Geomancer (lead), Underpriest Brogni, Mithrala, Stag Knight, Godseeker Aniri
- **Damage**: 50M average (UNM Force affinity) 
- **Survival**: 35-45 turns (inconsistent)
- **Lead Options**: Mithrala (+80 ACC aura), or Geomancer (+25% HP). Mithrala can be replaced with aura in mind ex speed.
- **Archetype**: Traditional tanky, brute force (NO speed tune). Using meta champs but not ideal. Surprising damage for lack of tune and synergy

---

## Primary Issues Identified
- Maintain this section as issues are identified, remediated, and updated through the analysis process.


---

## **QUICK OPTIMIZATION GUIDE - 3 Steps Per Champion**

**Baseline Confirmed**: 44M damage (2025-10-28 test)  
**Target**: 60-75M damage (+16-31M gain)  
**Implementation**: Follow 3-step fixes below in priority order

---

### **🎯 GEOMANCER - HP Burn DPS** 
**Status**:

**Step 1 - SPEED TUNE ** 🎯 **Enables team speed tune**
- **Status**: 
- **Result**: 
- **Gear**: 

**Step 2 - ** **+ damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Step 3 - ** **+ base damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Note**: 

---

### **🎯 BROGNI - Shield/HP Burn Specialist** 
**Status**:

**Step 1 - SPEED TUNE ** 🎯 **Enables team speed tune**
- **Status**: 
- **Result**: 
- **Gear**: 

**Step 2 - ** **+ damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Step 3 - ** **+ base damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Note**: 

---

### **🎯 STAG KNIGHT - Dec Def/Attack, may be replacable as boss is immune to decr
**Status**:

**Step 1 - SPEED TUNE ** 🎯 **Enables team speed tune**
- **Status**: 
- **Result**: 
- **Gear**: 

**Step 2 - ** **+ damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Step 3 - ** **+ base damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Note**: 

---

### **🎯 MITHRALA - Cleanse/Buff/Lead** 
**Status**:

**Step 1 - SPEED TUNE ** 🎯 **Enables team speed tune**
- **Status**: 
- **Result**: 
- **Gear**: 

**Step 2 - ** **+ damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Step 3 - ** **+ base damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Note**: 

---

### **🎯 GODSEEKER ANIRI - Heal/Revive/Buff Extend**
**Status**:

**Step 1 - SPEED TUNE ** 🎯 **Enables team speed tune**
- **Status**: 
- **Result**: 
- **Gear**: 

**Step 2 - ** **+ damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Step 3 - ** **+ base damage**
- **Action**: 
- **Result**: 
- **Why**: 
- **Difficulty**: 

**Note**: 

---

## **IMPLEMENTATION PRIORITY ORDER**

### **Phase 1: IMMEDIATE WINS** 

**Expected Result After Phase 1**: 

**Test After Phase 1**: Run 3 battles, measure damage increase, validate improvement before continuing

---

### **Phase 2: 


**Expected Result After Phase 2**: 

**Test After Phase 2**: Run 5 battles, verify turn order consistency, validate buff/shield timing

---

### **Phase 3: FINAL OPTIMIZATIONS** 

**Option A** 

**Option B** 

---

## **PROJECTED FINAL PERFORMANCE**

| Phase | Actions | Manual Damage | Auto Damage | Turns | Time Investment |
|-------|---------|---------------|-------------|-------|-----------------|
| **Baseline** | Current setup (tested 2025-10-28) | 44M ✅ | ~30M | 30-45 | N/A |
| **After Phase 1** | 
| **After Phase 2** | 
| **After Phase 3 (A)** | TBD | | | | |
| **After Phase 3 (B)** | TBD | | | | |

**V1.1 Goals**: 80M+ manual, 50M+ auto  
**Achievement**: 
**Auto Efficiency Assumption**: 

---

## Primary Issues Identified
- Maintain this section as issues are identified, remediated, and updated through the analysis process.

1. **No Speed Tune**: 

---

## Team Stat Reference
See [Current Team Stats](#current-team-stats) above for all champion stat details. For mechanics, see [Critical Mechanics Reference](#-critical-mechanics-reference).

---

---

## UNM Clan Boss Mechanics Reference
- Include likely damage output and final turn range, as possible.
- Update this section with validated boss mechanics, notes, synergy, meta, etc for better analysis and reference.

### Speed Tune Options

| Tune Type | Speed Range | Requirements | Difficulty | Notes |
|-----------|-------------|--------------|------------|-------|
| **1:1 Tune** | 171-189 SPD | Stun target 171 SPD (slowest) | Medium | Standard safe tune, all champions take 1 turn per CB turn |
| **2:1 Tune** | 250-280 SPD | Calculator required, precise tuning | Hard | High damage but fragile, needs exact speeds |
| **Unkillable** | Varies | Specific champions (Maneater, Roshcard) | Medium | Cheese strategy, requires unkillable buffers |
| **Speed Boost** | 191+ SPD | Speed aura + TM boost | Medium | Dynamic tune, harder to AUTO |



**1:1 Speed Tune Formula**: 171 SPD (stun target, slowest) to 189 SPD (max safe). All champions act once per CB turn, predictable buff/shield rotation.

### Champion Stat Goals (UNM)
These are generic guidelines, not specific

| Stat | Debuffer | DPS | Tank/Support | Notes |
|------|----------|-----|--------------|-------|
| **ACC** | 250+ | 200+ | 150+ | 250 ACC = ~90% land rate UNM, 300+ ideal |
| **DEF** | 4000+ | 3500+ | 4200+ | Survivability threshold, scales with HP |
| **HP** | 60k+ | 50k+ | 80k+ | Higher for tanks, balance with DEF |
| **SPD** | 200+ | 195+ | 191+ | 1:1 tune range (adjust for 2:1 if 250-280) |
| **C.RATE** | 50%+ | **100%** | 50%+ |  |
| **C.DMG** | 60%+ | 300%+ | 60%+ | Multiplies attack damage when critical,  |
| **RES** | 200+ | 150+ | 200+ | Optional, reduces debuff duration on team |

### Boss Mechanics

### Stat Requirements (UNM)

| Stat | Debuffer | DPS | Tank/Support | Notes |
|------|----------|-----|--------------|-------|
| **ACC** | 250+ | 200+ | 150+ | 250 ACC = ~90% land rate UNM, 300+ ideal |
| **DEF** | 3500+ | 3500+ | 4000+ | Survivability threshold, scales with HP |
| **HP** | 50k+ | 50k+ | 60k+ | Higher for tanks, balance with DEF |
| **SPD** | 171-189 | 171-189 | 171-189 | 1:1 tune range (adjust for 2:1 if 250-280) |
| **C.RATE** | 70%+ | **100%** | 70%+ | **CRITICAL** for Warmaster/Giant Slayer T6 |
| **C.DMG** | 150%+ | 200%+ | 150%+ | Multiplies crit damage, secondary to C.RATE |
| **RES** | 200+ | 150+ | 200+ | Optional, reduces debuff duration on team |

### Boss Mechanics

- **Affinity Rotation**: Void → Spirit → Force → Magic (4-day cycle)
- **Stun Mechanic**: Random champion every 3 turns (targets lowest HP after AOE hit)
- **Debuff Limit**: 10 max debuffs on boss (prioritize Weaken, Decrease DEF, HP Burn, Poison)
- **Turn 50 Scaling**: Boss damage/stats increase significantly at turn 50+ (survival threshold)
- **AOE Attacks**: Every turn, requires high DEF+HP or shields/block damage
- **Single Target Nukes**: Random target, requires healing/lifesteal/shields

### Affinity Risks

- **Force Affinity (Current)**: Safe for all current champions (all neutral or strong affinity)
- **Spirit Affinity**: **HIGH RISK** - Geomancer weak
  - Estimated damage loss: -10 to -15M total team damage (Geomancer contributes ~35M, loses ~30% = -10.5M, team total drops to ~34-39M)
- **Magic Affinity**: Safe (all neutral)
- **Void Affinity**: Safe (all neutral)

---

## Survivability & Stat Safety Analysis

### Effective HP Calculation

**Effective HP (EHP)** measures champion's total survivability accounting for DEF mitigation.

**Formula:** `EHP = HP × (1 + DEF / 1000)`

**Example:** 60,000 HP × (1 + 4,000 DEF / 1000) = 60,000 × 5.0 = **300,000 EHP**

**Interpretation:** A champion with 300k EHP can survive 300k raw damage before dying (accounting for DEF reduction).

### Current Team Effective HP Table ✅ **UPDATED 2025-10-29**

| Champion | HP | DEF | EHP Calculation | Total EHP | Survivability Rank |
|----------|-----|-----|-----------------|-----------|-------------------|
| | | | | | |
| | | | | | |

**Key Changes from last calculations (2025-10-29):**

**� BROGNI:** 
  - **RANK:** 
  - HP: 
  - DEF:
  - SPD: 
  - ACC: 
  - C.RATE: 
  - **Shield scaling:** 

**�🎉 STAG KNIGHT:** 
  - **RANK:** 
  - HP: 
  - DEF:
  - SPD: 
  - ACC: 
  - C.RATE: 

**MITHRALA:** 
  - **RANK:** 
  - HP: 
  - DEF:
  - SPD: 
  - ACC: 
  - C.RATE: 

**GEOMANCER:** 
  - **RANK:** 
  - HP: 
  - DEF:
  - SPD: 
  - ACC: 
  - C.RATE: 

**GODSEEKER ANIRI:** 
  - **RANK:** 
  - HP: 
  - DEF:
  - SPD: 
  - ACC: 
  - C.RATE: 

**Team Total:** 🏆

**Speed Tune Status:** 

### HP vs DEF% Boots Trade-Off Analysis

**Question:** Should champions use **HP% boots** or **DEF% boots**?

**Answer:** Depends on champion's **base HP** and **base DEF** ratio. Generally:
- **HP% boots preferred** if: Base HP > Base DEF × 15
- **DEF% boots preferred** if: Base DEF > Base HP / 15
- **Rule of thumb:** DEF% boots provide better **EHP per stat point** for most champions (70-80% of roster)

**Current Team Boot Analysis:**

| Champion | Current Boots | Current HP | Current DEF | EHP (Current) | **DEF% Boots (Projected)** | Projected HP | Projected DEF | EHP (Projected) | EHP Gain | Recommendation |
|----------|---------------|------------|-------------|---------------|---------------------------|--------------|---------------|-----------------|----------|----------------|

**Boot Swap Recommendations (Phase 2 Optimization):**

**Total Team EHP Gain:** 

**Brogni Special Case:**
- Brogni shields scale with MAX HP (24k shields at 80k HP)
- DEF% boots reduce HP (79,988 → 67,990), reducing shields (24k → 20.4k)
- **Trade-off:** 
- **RECOMMENDATION:** 

---


---

## Primary Issues Identified
- Maintain this section as issues are identified, remediated, and updated through the analysis process.

---


## **REMEDIATION PRIORITY ORDER**

### **Phase 1: IMMEDIATE WINS**
Do these 3 fixes FIRST - easiest and highest impact:

1. 
2. 
3. 

**Expected Result After Phase 1**: 

**Test After Phase 1**: 

---

### **Phase 2: 

**Expected Result After Phase 2**: 

**Test After Phase 2**: 

---

### **Phase 3: FINAL OPTIMIZATIONS** 

**Expected Result After Phase 3**: 

**Test After Phase 3**: 

---

## **PROJECTED FINAL PERFORMANCE**

| Phase | Actions | Manual Damage | Auto Damage | Turns | Time Investment |
|-------|---------|---------------|-------------|-------|-----------------|
| **Baseline** | Current setup (tested 2025-10-28) | 44M ✅ | ~30M | 30-45 | N/A |
| **After Phase 1** |
| **After Phase 2** | 
| **After Phase 3** |  

---

## **WORKING**
- This section holds quick start for data collection on champion changes, expected analysis using that data, and information on how to update this analysis document with results. 
- Many sections of this analysis require information from later sections. Update these once all required information is available.

### **Data Collection Flow**

**User Action Required:**

**Quick Start** (Recommended):
1. Provide gear and stat changes for current core team
2. List additional champions to consider, their role, and their gear/stats/etc like existing champions.

**Data Needed per Champion:**
- Screenshot: Gear details page (all 6 pieces visible)
  - List sets and main stats for better gear alternative analysis. This may include all substats, ascended stat, etc.
- Screenshot: Total stats list, numbers only but in order (HP, Atk, DEF, SPD, C.Rate, C.Dmg, RES, ACC, Ignore Def)
- Screenshot: Relic setup
- Blessing info, as text
- Assume fully booked, lowest cooldowns, etc.
- Reference information in the champion dictionary and stat table for skills, effects, etc. The entries are detailed json.

**Alternative:** (if screenshots difficult):
- Output a sample table of stats and other requested information not submitted. 
- Intake the table to update this analysis document

**Processing, Copilot:**
- Scrape the screenshots for information or use other data as input.
- Find that champion in the champion stat list. If it does not exist, we'll create a new entry using the same format as existing champions.
- Update the champion information using input data. 
- Move to the next champion, as needed.

---

### **Expected Analysis Output** (After data received)

Once gear stat details are provided, I (copilot) will create:

1. **Exact SPD Breakdown Table** - Base + sets + boots + substats for each champion
2. **Boot Swap Calculator** - Before/after SPD with exact values
3. **Stat Trade-off Analysis** - DEF/HP gains vs SPD loss for each swap
4. **Replacement Boots Recommendations** - DEF% vs HP% per champion role
5. **Substat Requirements** - Minimum SPD substats needed on replacement gear
6. **Gear Availability Check** - Confirm you have replacement boots/sets in inventory
7. **Regearing Plan** - Exact order of operations (which champion first, which piece first, what stat to focus on and their ideal level)

- This process may be completed against new champion stat/gear/etc changes, new champions to use on this team, staging other teams like entirely, attempting other speed tunes, or just to refresh current recommendations using existing champion information.
- This process should use the structure of the current analysis report, replacing existing data as new analysis is generated.
- This may be completed by creating a new file and inserting the new report as a draft, using the current date and goal ex add new champion to analysis.

---

## **Validation & Documentation Standards**

### **Sources Cited**
All analysis validated against authoritative sources:
- **UNM Mechanics**: User Q&A (10/27/2025), Clan Boss Stat REQ.jpg, ClanBoss_UltraNightmare_Team_Notes_FINAL.md
- **Champion Stats**: User-provided screenshots (10/27/2025) - Geomancer, Stag Knight, Brogni, Mithrala, Godseeker Aniri
- **Speed Tune Requirements**: Community consensus (1:1 tune 171-189 SPD, 2:1 tune 250-280 SPD with calculator)
- **Stat Requirements**: UNM standard thresholds (250+ ACC, 100% C.RATE Warmaster, 3500+ DEF, 50k+ HP)
- **Owned Champions**: Champion_stats.md (10/27/2025) - filtered owned>0 for alternates analysis
- **Damage Estimates**: Based on Warmaster/Giant Slayer proc rates (C.RATE correlation), community testing results

### **Confidence Level**
- **High Confidence** (90%+): Champion stat documentation (user screenshots), speed tune gaps (measured deltas), C.RATE damage loss calculations (Warmaster proc math)
- **Medium Confidence** (70-90%)**: Damage improvement estimates (+16-25M quick wins, +21-31M total), turn survival improvements (50+ turns projection)
- **Lower Confidence** (50-70%): Rector Drath swap impact (-3-5M damage tradeoff), ACC aura loss mitigation strategy

### **Assumptions & Uncertainties**
1. **Godseeker Aniri ACC requirement**: Assumed NOT needed (healer/support role suggests no debuffs in kit) - **VALIDATE** kit before prioritizing ACC fix
2. **Mithrala Brimstone blessing**: Doesn't have HP Burn in kit (unusual choice) - May be placeholder or for other content
3. **Regearing availability**: Assumed user has C.RATE gloves, DEF%/HP% boots, Lifesteal/Savage sets in inventory - **CONFIRM** gear availability before implementation
4. **Masteries completion cost**: Estimated 800 scrolls for Godseeker Aniri Support tree - **VALIDATE** current scroll inventory
5. **Arena team dependency**: Assumed Mithrala is core Arena champion (245 SPD suggests speed lead role) - **CONFIRM** Arena team composition before Rector Drath swap decision

### **Testing & Validation Requirements**
Before implementing recommended fixes:
1. **Baseline test run**: Capture current damage (44M), turn count (30-45), team survival with current stats/gear
2. **Per-fix validation**: Test after EACH major change (C.RATE gloves, masteries, speed tune steps) to validate impact
3. **Minimum 3 test runs per configuration**: Drop 1 outlier, use remaining 2-3 for damage average (RNG variance in CB)
4. **Affinity testing**: Validate on Force CB (current known), test Spirit/Magic/Void affinities after optimization
5. **Auto vs Manual**: Document manual damage first, then test AUTO mode for consistency (user priority: "AUTO-friendly after manual validated")

### **Simulation Notes**
- **No in-game simulation conducted yet**: All damage estimates based on mathematical calculations (Warmaster proc rates, C.RATE gaps, speed tune efficiency)
- **Recommend deadwoodjedicalculator.com**: Use for precise 1:1 speed tune validation (turn order simulator)
- **Test environment**: User should test on Force CB UNM (current safe affinity) before attempting other affinities

---

## **Update Notes & Version History**

### **Version 1.1 - Goal Update & Boss Stats Correction** 

---

### **Version 1.0 - Initial Setup

---

## **FILE METADATA**

**Filename**: `UNM_Clan_Boss_Team_Analysis.md`  
**Location**: `c:\GIT\Raid_Tools\Output\`  
**Version**: 1.1 DRAFT  
**Created**: 2025-10-27  
**Last Modified**: 2025-10-30  
**Author**: Selicos
**Format**: Markdown (.md)  
**Line Count**: 800 lines  
**Word Count**: ~6,100 words  

**Related Project Files**:
- `.github/copilot-instructions.md` (project standards, Section 10: Team Creation)
- `input/Champion_Dictionary/Champion_stats.md` (owned champions reference and base state information)
- `input/Mechanic_Dictionary/` (dir holding game mechanics information, equations, and more. Review in depth if information is not found in this analysis.)

---
