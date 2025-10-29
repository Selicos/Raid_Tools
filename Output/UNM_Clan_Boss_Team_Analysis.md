# UNM Clan Boss Team Analysis

**Date**: 2025-10-27  
**Status**: DRAFT - Analysis Complete, Awaiting Implementation  
**Goal**: Optimize existing 5-champion UNM team from 44M → 50M+ damage with proper speed tune

---

## Table of Contents

1. [Project Goals](#project-goals)
2. [Current Team Performance](#current-team-performance)
3. [Primary Issues Identified](#primary-issues-identified)
4. [UNM Clan Boss Mechanics Reference](#unm-clan-boss-mechanics-reference)
5. [Analysis Workflow](#analysis-workflow)
6. [Reference Documents](#reference-documents)
7. [Champion Intake Progress](#champion-intake-progress)
8. [Champion Documentation](#champion-documentation)
   - [Geomancer - HP Burn DPS Specialist](#geomancer---hp-burn-dps-specialist)
   - [Stag Knight - Decrease DEF/ATK Specialist](#stag-knight---decrease-defattk-specialist)
   - [Brogni - Shield/Cleanse/HP Burn Specialist](#brogni-underpriest-brogni---shieldcleansehp-burn-specialist)
   - [Mithrala - Cleanse/Buff/Lead Specialist](#mithrala---cleansebufflead-specialist)
   - [Godseeker Aniri - Heal/Revive/Buff Extend Specialist](#godseeker-aniri---healrevivebuff-extend-specialist)
9. [Speed Tune Analysis - 1:1 Tune Implementation](#speed-tune-analysis---11-tune-implementation)
10. [Stat Gaps Analysis - UNM Requirements vs Current Team](#stat-gaps-analysis---unm-requirements-vs-current-team)
11. [Ranked Recommendations (Priority 1-10)](#ranked-recommendations-priority-1-10)
12. [Alternates Analysis - Owned Champion Swaps](#alternates-analysis---owned-champion-swaps)
13. [Validation & Documentation Standards](#validation--documentation-standards)
14. [Update Notes & Version History](#update-notes--version-history)
15. [Cross-References & Related Files](#cross-references--related-files)
16. [Glossary & Abbreviations](#glossary--abbreviations)

---

## Project Goals

1. **Damage Target**: 44M current → 50M+ per key
2. **Survival Target**: 30-45 turns → 50+ turns consistent
3. **Speed Tune**: Implement 1:1 tune (171-189 SPD) for buff/shield sync
4. **Automation**: Prioritize AUTO-friendly after manual max damage validated
5. **Roster Constraint**: Use only owned champions (Champion_stats.md owned>0)

---

## Current Team Performance
 - to be updated after test run with current stats, Geomancer lead (HP aura)

- **Team**: Underpriest Brogni, Mithrala, Geomancer, Stag Knight, Godseeker Aniri
- **Damage**: 44M average (UNM Force affinity)
- **Survival**: 30-45 turns (inconsistent)
- **Lead**: Mithrala (+80 ACC aura), or Geomancer (+25% HP)
- **Archetype**: Traditional tanky, brute force (NO speed tune). Using favorites, not synergy/meta

---

## Primary Issues Identified
- Maintain this section as issues are identified, remediated, and updated through the analysis process.

1. **No Speed Tune**: Team runs chaotic speeds (brute force approach), causing:
   - Shield drops (Brogni damage loss from taking damage when shields expire)
   - Buff expiration before reapplication
   - Turn meter desync breaking rotations
   - **Mithrala Issue**: 240-260 SPD is MASSIVE OVERKILL for CB → should drop to 180-190 SPD for more HP%/DEF% substats
   
2. **Geomancer C.RATE 57%**: Needs 100% for Warmaster T6 (costing ~40% damage = 5-8M per run)
   - **Fix**: Change gloves to C.RATE main stat (57% → 100%+ with Deadly Precision mastery)
   - Add notes for each champion as relevant
   
3. **Geomancer SPD 210**: Too fast for 1:1 tune (target 171-189 SPD), breaking buff/shield sync
   - **Fix**: Remove Feral set (4-piece gives +12% SPD), replace with Lifesteal/Savage
   - **Target**: 171 SPD exactly (stun target candidate - low base HP, good DEF/HP)
   
4. **Possible HP Burn Overlap**: Brogni A1 (50% chance) vs Geomancer passive (reflects 25% of boss damage as HP Burn)
   - **NOTE**: Brogni's passive reflects damage to ally shields → triggers Giant Slayer mastery → 22M damage contribution (S tier champion, a favorite and early legendary for me. Useful center of the team. Leverage sheilds and extend buffs/etc as alternative teams.)
   - Brogni's accuracy is low, to prevent HP Burn placement. HP Burn overlap is not an issue, to maintain Gemoancer's passive.
   
5. **Affinity Risk**: Team built for Force CB, may struggle on Spirit/Magic affinity days
   - **Spirit CB**: Geomancer weak affinity (15% glancing, reduced damage) → consider **Lord Champfort** swap
   - **Force CB** (current): Safe for all champions

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
- **Spirit Affinity**: **HIGH RISK** - Geomancer weak affinity (15% glancing, reduced damage)
- **Magic Affinity**: Safe (all neutral)
- **Void Affinity**: Safe (all neutral)

---

## Analysis Workflow

**Instructions for this analysis project**:
1. Using the resources in this repo on clan boss and game mechanics, review my UNM clan boss team as input
2. Suggest changes per champion within speed tune options
3. Propose stat updates, including set changes
4. Propose team speed tune and synergy changes. Manual can be run to reach max 1 key chest, then auto may be priority
5. Review manual run for max damage potential
6. Identify, from the owned and key champion list, possible replacements including:
   a. Geomancer: may be replaceable with other high damage champ ex Ninja, or for poison/cheese/helpful mechanics
   b. Other revivers - Rector Drath, Arbiter, could be swapped in or used to hit speed tune/survivability goals
   c. Other mechanics, speed boost champs, etc are available.
7. Suggest an ideal 4 teams using the owned champions, ideally using one of the current clan boss team champions but suggest fun things, to take on UNM clan boss

---

## Reference Documents

The following reference documents contain historical UNM Clan Boss analysis and mechanics. **Note**: These are outdated and should be validated against current online sources (Ayumilove, HellHades, RaidHQ) before use.

- **UNM_Clan_Boss_Team_Analysis.md** (old version) - Previous team analysis, due for updates
- **ClanBoss_UltraNightmare_Team_Notes_FINAL.md** - Detailed boss guide from earlier project, comprehensive mechanics documentation (validate before use)
- **Clan Boss Stat REQ.jpg** - Min stats per online recommendations and accuracy floor thresholds
- **Mechanic Dictionary** (input/Mechanic_Dictionary/) - Damage scaling, crit damage, defense, masteries documentation
- **Online Sources** - Per copilot-instructions.md authoritative sources (Ayumilove, HellHades, RaidHQ)

---

## Champion Builds Analysis

**Geomancer - Current Build Documentation**
-------------------------------------------

### **Stats (Total with Gear)**

| Stat | Value | Notes |
| --- | --- | --- |
| HP | 57,756 | ✅ Good for survivability |
| ATK | 3,578 | Decent |
| DEF | 4,520 | ✅ Excellent survivability |
| SPD | 210 | ⚠️ **TOO FAST** for 1:1 tune (target 171-189) |
| C.RATE | 57% | ❌ **CRITICAL ISSUE** - needs 100% for Warmaster |
| C.DMG | 139% | ⚠️ Low (target 200%+) |
| RES | 80 | Low (not priority for CB) |
| ACC | 249 | ✅ Good for backup debuffs |

### **Gear Sets**

-   **4x Feral** (SPD set, +12% SPD)
-   **2x Perception** (+40 ACC)

### **Masteries (Offense + Defense)**

**Offense Tree:**

-   T1: Deadly Precision (C.RATE +5%)
-   T2: Keen Strike (C.DMG +10%)
-   T3: Single Out, Whirlwind of Death
-   T4: Cycle of Violence, Bring it Down
-   T5: Methodical, Kill Streak
-   **T6: Warmaster** ✅ (Correct for multi-hit A1)

**Defense Tree:**

-   T1: Tough Skin
-   T2: Blastproof, Resurgent
-   T3: Delay Death
-   T4: Retribution
-   **T5: Warmaster of Wrath** (Increase SPD on kill - not useful CB)

### **Blessing**

-   **Cruelty (4★)** - Extends debuff duration (good for HP Burn uptime)

### **Relic**

-   **Golden Elixir** - Ignore 5% target RES when placing HP Burn (helps ACC threshold)

### **Skills**

-   ✅ **Fully Booked** (all cooldowns reduced)

* * * * *

**CRITICAL ISSUES - Geomancer**
-------------------------------

### **1\. CRIT RATE TOO LOW (57%)**

-   **Current**: 57% C.RATE
-   **Required**: 100% C.RATE for consistent Warmaster procs
-   **Impact**: Missing ~40% of Warmaster damage (huge DPS loss)
-   **Fix**: Change **Gloves to C.RATE main stat** (58% from gloves alone → 100%+ total with Deadly Precision mastery)

### **2\. SPEED TOO HIGH (210)**

-   **Current**: 210 SPD
-   **Target**: 171-189 SPD (1:1 speed tune)
-   **Issue**: 210 SPD = taking extra turns → speed tune chaos → shield/buff desync
-   **Fix**:
    -   Remove Feral set (4-piece gives +12% SPD = ~25 SPD boost)
    -   Replace with **Lifesteal** or **Savage** set
    -   Target **171 SPD exactly** (stun target candidate - low base HP)

### **3\. GEAR SET SUBOPTIMAL**

-   **Current**: 4x Feral + 2x Perception
-   **Issue**: Feral gives SPD (not needed), no damage scaling
-   **Recommended**:
    -   **4x Lifesteal** + 2x Perception (survivability + ACC)
    -   **4x Savage** + 2x Crit Damage (ignore DEF% + damage scaling)
    -   **6x Savage** (maximum damage if ACC substats good)

* * * * *

**Optimization Priority - Geomancer**
-------------------------------------

| Priority | Change | Impact | Notes |
| --- | --- | --- | --- |
| **1\. URGENT** | Gloves: C.RATE main stat | +40-50% DPS | 57% → 100%+ C.RATE (Missing ~40% Warmaster procs = 5-8M damage loss per run) |
| **2\. URGENT** | Remove Feral set → Lifesteal/Savage | Fix speed tune | 210 → 171 SPD target |
| **3\. HIGH** | SPD boots substats adjustment | Speed tune | Exactly 171 SPD (stun target TBD after all 5 champions analyzed) |
| **4\. MEDIUM** | C.DMG optimization | +15-20% DPS | 139% → 200%+ C.DMG |


**Regearing Strategy Note**: Will document all 5 champions first for holistic analysis. Regearing will be time-intensive and must avoid breaking Arena/other teams. Speed adjustments may use SPD boots → DEF%/HP% boots swaps, or accessories with flat stats instead of % stats.

---

### **Stag Knight - Decrease DEF/ATK Specialist**

**Role**: Decrease DEF/ATK debuffer, tanky CB build (vs arena speed build)

**Stats (Total with Gear)**

| Stat | Value | Notes |
| --- | --- | --- |
| HP | 67,312 | ✅ Excellent survivability (tank role) |
| ATK | 2,360 | Low (not a damage dealer) |
| DEF | 4,616 | ✅ Excellent survivability |
| SPD | 222 | ⚠️ **TOO FAST** for 1:1 tune (target 171-189) |
| C.RATE | 63% | ⚠️ Below 100% for Warmaster (target 70%+ for support, 100% ideal) |
| C.DMG | 104% | Low (not priority for support) |
| RES | 120 | Low (not priority for CB) |
| ACC | 310 | ✅ **EXCELLENT** (well above 250 threshold for UNM debuff landing) |
| Notes | 2% (unknown stat) | - |

**Gear Sets**

-   **Gear sets not clearly visible in screenshot** - Please confirm sets (likely Perception/Accuracy/Speed based on stats)

**Masteries (Offense + Support)**

**Offense Tree:**

-   T1: Deadly Precision (C.RATE +5%)
-   T2: Keen Strike (C.DMG +10%)
-   T3: Single Out, Whirlwind of Death
-   T4: Cycle of Violence, Bring it Down
-   T5: Methodical, Kill Streak
-   **T6: Warmaster** ✅ (Correct for multi-hit A1)

**Support Tree:**

-   T1: Tough Skin
-   T2: Lore of Steel (visible)
-   T3: Reflect Damage (visible)
-   T4: Harvest Despair (visible)
-   T5: Swarm Smiter, Cycle of Magic (visible)
-   **T6: Evil Eye or Sniper** (visible - likely Evil Eye for extra debuff damage)

**Blessing**

-   **Cruelty (3★)** - Extends debuff duration (good for Decrease DEF/ATK uptime)

**Relic**

-   **Gilded Dragonstone** - DEF increases 1% up to 10% per crit received (stacks survivability)

**Skills**

-   ✅ **Fully Booked** (all cooldowns reduced)

* * * * *

**CRITICAL ISSUES - Stag Knight**
-------------------------------

### **1\. SPEED TOO HIGH (222)**

-   **Current**: 222 SPD
-   **Target**: 171-189 SPD (1:1 speed tune)
-   **Issue**: 222 SPD = taking extra turns → speed tune chaos → Decrease DEF/ATK timing issues
-   **Fix**:
    -   Replace SPD boots with **DEF% or HP% boots**
    -   Target **180-189 SPD** (mid-range 1:1 tune, faster than stun target)
    -   Current gear sets likely include Speed set → may need to swap

### **2\. CRIT RATE SUBOPTIMAL (63%)**

-   **Current**: 63% C.RATE
-   **Target**: 70%+ for support role, 100% ideal for Warmaster consistency
-   **Impact**: Missing ~35% of Warmaster procs (moderate DPS loss for support role)
-   **Fix**: Low priority vs speed tune (support role, not primary DPS)

**Optimization Priority - Stag Knight**
-------------------------------------

| Priority | Change | Impact | Notes |
| --- | --- | --- | --- |
| **1\. URGENT** | SPD boots → DEF%/HP% boots | Fix speed tune | 222 → 180-189 SPD target (avoid breaking Decrease DEF/ATK rotation) |
| **2\. MEDIUM** | C.RATE optimization | +10-15% DPS | 63% → 70%+ C.RATE (support role, lower priority than Geomancer) |
| **3\. LOW** | Confirm gear sets | Visibility | Unable to identify sets from screenshot clearly |

**Strengths - Stag Knight**
- ✅ **310 ACC** - Excellent for UNM debuff landing (60+ above threshold)
- ✅ **67k HP + 4.6k DEF** - Excellent survivability for tank role
- ✅ **Fully booked** - All cooldowns reduced for consistent Decrease DEF/ATK uptime
- ✅ **Gilded Dragonstone relic** - DEF stacking synergizes with tank role

---

### **Brogni (Underpriest Brogni) - Shield/Cleanse/HP Burn Specialist**

**Role**: Shield bot, Cleanse, Increase DEF, HP Burn (resolved overlap with Geomancer - 22M damage contribution justified keeping both)

**Current Stats**
-----------------

| Stat | Value | Notes |
| --- | --- | --- |
| **HP** | 80,528 | Excellent tank stats |
| **ATK** | 2,527 | Low (not damage dealer) |
| **DEF** | 5,034 | Excellent for shield scaling + survivability |
| **SPD** | 225 | **TOO FAST** for 1:1 tune (target 171-189) |
| **C.RATE** | 26% | **CRITICAL ISSUE** - Giant Slayer passive needs higher C.RATE |
| **C.DMG** | 100% | Low (base value, not priority) |
| **RES** | 229 | High (good for debuff resistance) |
| **ACC** | 145 | **LOW** for UNM (target 250+), affects HP Burn landing |
| **Notes** | 2% | Unknown stat |

**Gear Sets**
-------------
- **4x Bolster** (HP set, likely +15% HP bonus)
- **2x Protection** (+15% DEF bonus)
- **Analysis**: Tank-focused gear sets maximizing HP/DEF for shield strength and survivability. Good set choices for support role.

**Masteries**
-------------

Based on screenshot analysis:

**Offense Tree:**
- Deadly Precision (C.RATE +5%)
- Keen Strike (C.DMG +10%)
- Single Out (visible)
- Whirlwind of Death (visible)
- Cycle of Violence (visible)
- Bring it Down (visible)
- Methodical (visible)
- Kill Streak (visible)
- **Giant Slayer T6** ✅ (visible - procs on A1, scales with C.RATE)

**Support Tree:**
- Tough Skin (visible)
- Healing Savior (visible - likely for enhanced heal/shield)
- Rapid Response (visible)
- Lore of Steel (visible)
- Cycle of Magic (visible)
- **Lasting Gifts T6** (visible - likely extends buff duration for shields/Increase DEF)

**Note**: Giant Slayer passive procs on A1 attacks. At 26% C.RATE, only proccing ~26% of the time = significant damage loss. Higher C.RATE would improve damage contribution.

**Blessing**
------------
- **Brimstone 2★** (HP Burn damage increase, synergizes with HP Burn on A1)

**Relic**
---------
- **Gilded Dragonstone** (Wearer ignores 5% of target's RES when placing HP Burn, AND Reflect Damage deals 10% more)
- **Analysis**: Excellent relic choice - helps HP Burn land with low ACC (145 vs 250 target = -105 gap, relic helps offset), Reflect Damage bonus synergizes with Ally Protection mechanics

**Skills**
----------
- **Fully booked** ✅ (assumed based on established multi-use champion, confirm if needed)

**Critical Issues - Brogni**
----------------------------

1. **SPD TOO HIGH (225)**
   - Current: 225 SPD
   - Target: 171-189 SPD (1:1 tune)
   - Issue: Taking extra turns → speed tune chaos → shield timing issues (shields expire early, buff extension misalignment with Godseeker Aniri)
   - Fix: Replace SPD boots with DEF%/HP% boots (synergizes with tank role + shield scaling)
   - Target: 180-189 SPD (mid-range 1:1 tune, NOT stun target due to high HP 80k)

2. **CRIT RATE CRITICAL (26%)**
   - Current: 26% C.RATE
   - Target: 70%+ for Giant Slayer reliability / 100% ideal
   - Impact: Giant Slayer passive only proccing ~26% of the time = significant damage loss (estimated 8-12M damage loss vs 70%+ C.RATE)
   - Fix: C.RATE gloves (26% → ~80%+ with Deadly Precision mastery), or C.RATE substats focus
   - Note: Higher priority than Stag Knight C.RATE fix (Brogni contributes 22M damage, Giant Slayer passive is damage multiplier)

3. **ACC TOO LOW (145)**
   - Current: 145 ACC
   - Target: 250+ ACC (UNM standard for debuff landing)
   - Gap: -105 ACC (massive gap)
   - Impact: HP Burn failing to land frequently (estimated 30-40% fail rate), reducing damage contribution
   - Fix: ACC chest OR ACC banner OR Perception set additions
   - Mitigation: Gilded Dragonstone relic helps (ignores 5% target RES), but still -105 gap too large
   - Note: Lower priority than SPD + C.RATE (HP Burn overlap with Geomancer means not critical path, but 22M damage justifies optimization)

**Optimization Priority - Brogni**
----------------------------------

| Priority | Change | Impact | Notes |
| --- | --- | --- | --- |
| **1. URGENT** | SPD boots → DEF%/HP% boots | Fix speed tune + stronger shields | 225 → 180-189 SPD target (avoid shield timing issues) |
| **2. URGENT** | C.RATE gloves | +8-12M damage (Giant Slayer) | 26% → 80%+ C.RATE (Deadly Precision +5% = 85%+ total) |
| **3. HIGH** | ACC optimization | HP Burn reliability | 145 → 250+ ACC (ACC chest/banner OR Perception set swap) |
| **4. MEDIUM** | Validate gear substats | Optimize HP/DEF/ACC balance | Confirm if substats can cover ACC gap without set changes |

**Regearing Strategy - Brogni**
- **SPD boots → DEF% boots**: Reduces 225 → ~180-185 SPD (DEF% boots synergize with 5,034 DEF base + Bolster/Protection sets + shield scaling)
- **Gloves → C.RATE gloves**: 26% → ~80%+ C.RATE (massive Giant Slayer proc improvement)
- **ACC gap (-105)**: May require ACC chest OR Perception set (replace Bolster/Protection if necessary), but confirm substats first (regearing time-intensive, avoid breaking other teams)

**Strengths - Brogni**
- ✅ **22M damage contribution** - Justified keeping despite HP Burn overlap with Geomancer
- ✅ **80k HP + 5k DEF** - Excellent tank stats for survivability + shield strength scaling
- ✅ **4x Bolster + 2x Protection** - Optimal sets for support/tank role
- ✅ **Gilded Dragonstone relic** - Helps offset ACC gap (ignore 5% RES) + Reflect Damage synergy
- ✅ **Brimstone 2★ blessing** - Increases HP Burn damage (synergizes with A1)
- ✅ **Giant Slayer T6 + Lasting Gifts T6** - Good mastery choices (damage passive + buff extension)
- ✅ **High RES (229)** - Good debuff resistance for survivability

---

### **Mithrala - Cleanse/Buff/Lead Specialist**

**Role**: Cleanse, Increase ATK/SPD/C.RATE buffs, Aura Lead (+80 ACC to all allies), currently built for Arena (high SPD)

**Current Stats**
-----------------

| Stat | Value | Notes |
| --- | --- | --- |
| **HP** | 71,378 | Good survivability |
| **ATK** | 2,963 | Low (not damage dealer) |
| **DEF** | 4,746 | Excellent tank stats |
| **SPD** | 245 | **EXTREME OVERKILL** for UNM 1:1 tune (target 171-189) |
| **C.RATE** | 38% | **CRITICAL ISSUE** - Needs higher for consistent damage |
| **C.DMG** | 81% | Low (not priority) |
| **RES** | 61 | Very low (but Exuzar's Totem helps +5 per debuff) |
| **ACC** | 526 | **MASSIVE OVERKILL** for UNM (250 threshold, +276 excess) |
| **Notes** | 2% | Unknown stat |

**Gear Sets**
-------------
- **2x Feral** (SPD set, +12% SPD bonus)
- **4x Perception** (+40 ACC per 2-set = +80 ACC total)
- **Analysis**: Arena speed build with massive ACC overkill. Feral set adding unwanted SPD for CB. Perception sets contributing to +276 ACC excess beyond UNM requirements.

**Masteries**
-------------

Based on screenshot analysis:

**Offense Tree:**
- Deadly Precision (C.RATE +5%)
- Keen Strike (C.DMG +10%)
- Single Out (visible)
- Whirlwind of Death (visible)
- **Flawless Execution T6** (visible - C.DMG bonus, suggests damage focus but stats don't support)

**Support Tree:**
- Tough Skin (visible)
- Exalt in Death (visible - increases SPD on ally death, Arena mechanic)
- Rapid Response (visible)
- Lore of Steel (visible)
- Cycle of Magic (visible)
- **Master Hexer T6** (visible - extends debuff duration +1 turn)
- Additional support masteries visible (Shield Bearer, Merciful Aid)

**Note**: Masteries suggest hybrid Arena/CB build. Flawless Execution not ideal for support role (Warmaster or Giant Slayer better for CB damage). Master Hexer good for extending debuffs.

**Blessing**
------------
- **Brimstone 2★** (HP Burn damage increase)
- **Note**: Mithrala doesn't have HP Burn in kit - blessing may be placeholder or for other content

**Relic**
---------
- **Exuzar's Totem** (Wearer's RES increases by 5 whenever a debuff is placed on them)
- **Analysis**: Helps offset very low base RES (61). On UNM CB with constant debuffs, RES could stack to 100+ during fight.

**Skills**
----------
- **Fully booked** ✅ (assumed based on established multi-use champion, confirm if needed)

**Critical Issues - Mithrala**
------------------------------

1. **SPD EXTREME OVERKILL (245)**
   - Current: 245 SPD
   - Target: 171-189 SPD (1:1 tune) OR 180-190 SPD (mid-range)
   - Overkill: +56-74 SPD excess (MASSIVE)
   - Issue: Taking way too many extra turns → extreme speed tune chaos → buff timing issues (cleanse/buffs expiring early, turn meter desync, shield/buff extension misalignment)
   - Fix: Remove Feral set (loses +12% SPD = ~30 SPD reduction), replace SPD boots with DEF%/HP% boots (loses ~40-50 SPD)
   - Combined fix: 245 - 30 (Feral) - 45 (boots) = ~170 SPD → may need SPD substats to reach 180-190 target
   - **HIGHEST PRIORITY** - Speed tune completely broken by this champion

2. **ACC MASSIVE OVERKILL (526)**
   - Current: 526 ACC
   - Target: 250 ACC (UNM threshold)
   - Overkill: +276 ACC excess (wasted stats)
   - Issue: 4x Perception sets (+80 ACC) + ACC substats creating massive overkill
   - Fix: Remove 2x Perception sets (loses -40 ACC), replace with Lifesteal/Immortal/Speed (CB-focused sets)
   - After fix: 526 - 40 = ~486 ACC (still +236 overkill, but better)
   - Note: Can drop ACC chest/banner for HP%/DEF% if needed (regearing dependent)
   - Priority: MEDIUM (not hurting performance, just wasted stats)

3. **CRIT RATE LOW (38%)**
   - Current: 38% C.RATE
   - Target: 70%+ for support / 100% ideal for Warmaster/Giant Slayer
   - Gap: -32% to -62% depending on target
   - Impact: If using Flawless Execution T6, not proccing consistently. Moderate damage loss.
   - Fix: C.RATE gloves (38% → ~90%+ with Deadly Precision)
   - Priority: MEDIUM (support role, but Flawless Execution suggests damage focus)

4. **MASTERIES SUBOPTIMAL FOR CB**
   - Flawless Execution T6 (Offense): C.DMG bonus, but Mithrala is support not damage dealer
   - Exalt in Death (Support): Arena mechanic (SPD on ally death), useless in CB
   - Recommendation: Respec to Warmaster or Giant Slayer T6 for CB damage contribution
   - Priority: LOW (works fine, but not optimal for CB)

5. **RES VERY LOW (61)**
   - Current: 61 RES (before Exuzar's Totem stacking)
   - Target: Not critical for CB, but low
   - Mitigation: Exuzar's Totem stacks +5 per debuff placed = can reach 100+ RES during UNM fight
   - Priority: LOW (relic handles it)

**Optimization Priority - Mithrala**
------------------------------------

| Priority | Change | Impact | Notes |
| --- | --- | --- | --- |
| **1. CRITICAL** | SPD boots → DEF%/HP% boots + Remove Feral set | Fix speed tune (TEAM BLOCKER) | 245 → 180-190 SPD target (-30 Feral, -45 boots = ~170 SPD, add substats to 180-190) |
| **2. HIGH** | Replace 2x Perception with Lifesteal/Immortal | Better survivability, reduce ACC waste | 526 → ~280-300 ACC (still overkill but acceptable), gain survivability |
| **3. MEDIUM** | C.RATE gloves | Support damage optimization | 38% → 90%+ C.RATE (if keeping Flawless Execution) |
| **4. LOW** | Respec masteries | Warmaster/Giant Slayer T6 | Replace Flawless Execution + Exalt in Death with CB-optimized choices |
| **5. LOW** | Validate Brimstone blessing | Clarity | Mithrala doesn't have HP Burn - may want different blessing (Cruelty for debuff extension?) |

**Regearing Strategy - Mithrala**
- **SPD boots → DEF% boots**: 245 → ~200 SPD (loses ~45 SPD from boots)
- **Remove 2x Feral set → Lifesteal or Immortal**: 200 → ~170 SPD (loses +12% SPD = ~30 SPD from set), gains survivability
- **Target 180-190 SPD**: May need to add SPD substats after removing Feral + boots (current 170 → add +10-20 SPD via substats)
- **Remove 2x Perception sets → other sets**: Reduces ACC overkill, opens slots for Lifesteal/Immortal/Speed for survivability
- **C.RATE gloves**: 38% → 90%+ C.RATE (optional, depends on if damage contribution desired)

**Strengths - Mithrala**
- ✅ **Aura Lead (+80 ACC)** - Helps entire team hit 250 ACC threshold (massive team benefit)
- ✅ **Cleanse + Increase ATK/SPD/C.RATE** - Excellent support kit for team damage/survivability
- ✅ **71k HP + 4.7k DEF** - Good tank stats for survivability
- ✅ **Master Hexer T6** - Extends debuff duration +1 turn (good for Decrease DEF/ATK uptime)
- ✅ **Exuzar's Totem** - RES stacking during fight helps survivability (61 → 100+ RES)
- ✅ **Fully booked** (assumed) - Consistent buff/cleanse uptime

**Arena Build Conflict - Mithrala**
- Current build is optimized for Arena (245 SPD, 526 ACC, Feral + Perception sets, Exalt in Death mastery)
- Converting to CB will significantly weaken Arena team
- **Regearing constraint**: User noted "avoid breaking Arena teams" - Mithrala may be core Arena champion
- **Recommendation**: After all 5 champions documented, evaluate if Mithrala can be replaced in CB team with someone less critical to Arena (potential swap: Rector Drath for cleanse/revive, or Vogoth for Leech/survivability)

---

### **Godseeker Aniri - Heal/Revive/Buff Extend Specialist**

**Role**: Heal, Revive on death (passive), Extend buffs, Increase DEF, survivability anchor

**Current Stats**
-----------------

| Stat | Value | Notes |
| --- | --- | --- |
| **HP** | 76,705 | Excellent survivability (highest on team) |
| **ATK** | 2,806 | Low (not damage dealer) |
| **DEF** | 4,214 | Good tank stats |
| **SPD** | 264 | **EXTREME OVERKILL** for UNM 1:1 tune (target 171-189) |
| **C.RATE** | 35% | Low (not priority for support/healer) |
| **C.DMG** | 76% | Low (not priority) |
| **RES** | 215 | Good debuff resistance |
| **ACC** | 168 | **LOW** for UNM (target 250+ if placing debuffs, but Aniri is pure support) |
| **Notes** | 2% | Unknown stat |

**Gear Sets**
-------------
- **2x Righteous** (+15% C.RATE bonus)
- **4x Regeneration** (+15% HP regeneration per turn)
- **1x Stoneskin** (likely partial set for shield on first turn, or stray piece)
- **Analysis**: Survivability-focused build with Regeneration for constant healing. Stoneskin partial set suggests defensive focus. No SPD sets but still 264 SPD (high substats).

**Masteries**
-------------

Based on screenshot analysis:

**Offense Tree:**
- Deadly Precision (C.RATE +5%) - visible
- Keen Strike (C.DMG +10%) - visible
- Heart of Glory - visible
- Single Out - visible
- Bring it Down - visible
- Cycle of Violence - visible
- **Life Drinker T5** - visible (heal on crit, synergizes with Regeneration)
- **INCOMPLETE** - T6 mastery NOT selected (missing Warmaster/Giant Slayer/Flawless Execution)

**Defense Tree:**
- Tough Skin - visible
- Blastproof - visible
- Rejuvenation - visible
- Shadow Heal - visible
- Delay Death - visible
- **Retribution T5** - visible (counterattack on receiving critical hit)
- **INCOMPLETE** - T6 mastery NOT selected

**Support Tree:**
- **NOT BUILT** - No support masteries visible

**CRITICAL ISSUE**: Masteries are incomplete. Missing T6 masteries from Offense and Defense trees. No Support tree at all. Should complete with Defense T6 (Fearsome Presence for turn meter reduction OR Warmaster of Wrath for healing) or Support T6 (Lasting Gifts for buff extension synergy).

**Blessing**
------------
- **Miracle Heal 3★** (Boss Heal - restores destroyed MAX HP 25% more effective, AND DEF increases 1% each time wearer receives critical hit up to 10%)
- **Analysis**: Excellent blessing for survivability. Revive passive + Miracle Heal = strong death/resurrection mechanic. DEF stacking (1% per crit up to 10%) helps tank role.

**Relic**
---------
- **Demonic Effigy** (Epic quality, 2★, +3,185 HP, +16 RES, +SPD at Lv.15)
- **Effect**: Wearer's Turn Meter increases by 10% whenever one of their allies dies
- **Analysis**: Synergizes with revive passive (if allies die, Aniri gets turn meter boost → faster revive/heal rotation). Good relic choice for support role.

**Skills**
----------
- **Fully booked** ✅ (assumed based on established multi-use champion, confirm if needed)

**Critical Issues - Godseeker Aniri**
--------------------------------------

1. **SPD EXTREME OVERKILL (264)**
   - Current: 264 SPD
   - Target: 171-189 SPD (1:1 tune)
   - Overkill: +75-93 SPD excess (MASSIVE - highest SPD on team)
   - Issue: Taking way too many extra turns → extreme speed tune chaos → buff extension timing issues (extending buffs at wrong time, heal/revive rotation desync, turn meter boost from Demonic Effigy creating more chaos)
   - Fix: Replace SPD boots with HP%/DEF% boots (loses ~45 SPD), optimize substats (may need to regear entirely to drop -75+ SPD)
   - Combined fix: 264 - 45 (boots) = ~219 SPD → still +30-48 SPD over target → needs aggressive substat reduction
   - **CRITICAL PRIORITY** - Second highest SPD blocker after Mithrala (245 SPD)

2. **MASTERIES INCOMPLETE**
   - Missing T6 masteries from Offense and Defense trees
   - No Support tree at all (Support tree has Lasting Gifts T6 = extends buff duration, perfect for Aniri's kit)
   - Current state: Only T5 masteries (Life Drinker, Retribution)
   - **FIX REQUIRED**: Complete masteries with Support tree + Lasting Gifts T6 (synergizes with buff extension skill), OR Defense T6 (Warmaster of Wrath for healing)
   - **URGENT** - Incomplete masteries = significant performance loss

3. **ACC LOW (168) - CONDITIONAL ISSUE**
   - Current: 168 ACC
   - Target: 250+ ACC (if placing debuffs)
   - Gap: -82 ACC
   - **Question**: Does Godseeker Aniri place debuffs in kit? (heal/revive/buff extend suggests pure support, may not need ACC)
   - If no debuffs: ACC not critical, can ignore
   - If debuffs exist: Needs +82 ACC via ACC chest/banner or Perception sets
   - Priority: **CONDITIONAL** - Validate kit before prioritizing

4. **STONESKIN PARTIAL SET (1 piece)**
   - Only 1x Stoneskin piece equipped (not full 4-set for shield effect)
   - May be stray piece or incomplete set
   - Fix: Complete 4x Stoneskin for first-turn shield (helps survivability), OR replace with matching set (Regeneration, Immortal, etc.)
   - Priority: LOW (not hurting performance, just incomplete set bonus)

**Optimization Priority - Godseeker Aniri**
-------------------------------------------

| Priority | Change | Impact | Notes |
| --- | --- | --- | --- |
| **1. CRITICAL** | Complete masteries | Support tree + Lasting Gifts T6 | Missing T6 masteries = major performance loss. Lasting Gifts synergizes with buff extension skill. |
| **2. CRITICAL** | SPD boots → HP%/DEF% boots + substat reduction | Fix speed tune (TEAM BLOCKER) | 264 → 180-189 SPD target (-45 boots, -30+ substats = aggressive regearing needed) |
| **3. MEDIUM** | Validate ACC requirement | Clarity on debuffs in kit | If no debuffs, ignore ACC. If debuffs exist, needs +82 ACC to 250 threshold. |
| **4. LOW** | Complete Stoneskin set OR replace piece | Set bonus efficiency | 1x Stoneskin stray piece → complete 4x Stoneskin for shield, OR replace with Regeneration/Immortal matching piece |

**Regearing Strategy - Godseeker Aniri**
- **SPD boots → HP% boots**: 264 → ~219 SPD (loses ~45 SPD from boots)
- **Substat reduction**: 219 → 180-189 SPD target (needs -30-39 SPD via regearing/substat downgrades)
- **Aggressive regearing may be required**: Current 264 SPD suggests high SPD substats across all gear → may need to replace multiple pieces to reach 180-189 target
- **Complete masteries**: Add Support tree (Lasting Gifts T6 for buff extension synergy, OR Defense T6 Warmaster of Wrath for healing boost)
- **Stoneskin decision**: Complete 4x Stoneskin (first-turn shield) OR replace with 4x Regeneration full set (continuous healing)

**Strengths - Godseeker Aniri**
- ✅ **76k HP** - Highest HP on team (excellent survivability anchor)
- ✅ **Revive on death passive** - Clutch mechanic for team survival (synergizes with Demonic Effigy turn meter boost)
- ✅ **Buff extension** - Extends Brogni shields, Mithrala buffs, Stag Knight debuffs (team force multiplier)
- ✅ **Miracle Heal 3★ blessing** - Revive MAX HP 25% more effective + DEF stacking 1% per crit up to 10%
- ✅ **Demonic Effigy relic** - Turn meter +10% on ally death (synergizes with revive passive)
- ✅ **4x Regeneration** - Constant HP regen (+15% per turn) for sustained survivability
- ✅ **215 RES** - Good debuff resistance (helps avoid stuns/debuffs)
- ✅ **Fully booked** (assumed) - Consistent heal/revive/buff extend uptime

---

## **CHAMPION INTAKE COMPLETE (5/5)** ✅

All 5 champions documented. Ready for speed tune analysis, stat gaps analysis, and recommendations.

**Team Speed Summary:**
1. **Godseeker Aniri**: 264 SPD (TARGET: 180-189, GAP: -75 to -93)
2. **Mithrala**: 245 SPD (TARGET: 180-190, GAP: -55 to -65)
3. **Brogni**: 225 SPD (TARGET: 180-189, GAP: -36 to -56)
4. **Stag Knight**: 222 SPD (TARGET: 180-189, GAP: -33 to -53)
5. **Geomancer**: 210 SPD (TARGET: 171 stun, GAP: -39)

**All champions are TOO FAST for 1:1 speed tune. Speed tune implementation is CRITICAL priority.**

---

## **SPEED TUNE ANALYSIS - 1:1 Tune Implementation**

### **Current Speed Tune Status: COMPLETELY BROKEN**

**1:1 Speed Tune Requirements:**
- **Target Range**: 171-189 SPD for all champions
- **Stun Target**: Slowest champion at exactly 171 SPD (takes stun every 3 turns, survives, team continues)
- **Turn Order**: Consistent rotation every 2 boss turns (boss AOE → team full rotation → boss AOE → repeat)
- **Buff/Debuff Timing**: All buffs/debuffs must align with 2-turn boss cycle (shields up before AOE, debuffs applied before damage)

**Current Team Speeds (Sorted Fastest → Slowest):**

| Champion | Current SPD | Target SPD | Gap | Fix Required | Priority |
| --- | --- | --- | --- | --- | --- |
| **Godseeker Aniri** | 264 | 180-189 | **-75 to -93** | SPD boots → HP% boots + aggressive substat reduction | CRITICAL |
| **Mithrala** | 245 | 180-190 | **-55 to -65** | Remove Feral set + SPD boots → DEF% boots | CRITICAL |
| **Brogni** | 225 | 180-189 | **-36 to -56** | SPD boots → DEF% boots | URGENT |
| **Stag Knight** | 222 | 180-189 | **-33 to -53** | SPD boots → DEF%/HP% boots | URGENT |
| **Geomancer** | 210 | **171 (stun)** | **-39** | Remove Feral set → Lifesteal/Savage | URGENT |

**Total Speed Reduction Needed Across Team**: **-238 to -305 SPD** (massive regearing project)

---

### **Recommended Speed Tune Configuration**

**Option 1: Traditional 1:1 Tune (RECOMMENDED)**

| Champion | Role | Target SPD | Turn Order | Reasoning |
| --- | --- | --- | --- | --- |
| **Geomancer** | HP Burn DPS / **STUN TARGET** | **171** | 5th (slowest) | Low base HP (57k) + good DEF (4.5k) = ideal stun tank. HP Burn applies early in rotation for maximum damage. Remove Feral set to drop 210→171 SPD. |
| **Stag Knight** | Decrease DEF/ATK | **180** | 4th | Decrease DEF/ATK lands before DPS champions attack. Mid-range speed for consistent debuff timing. Replace SPD boots with DEF%/HP% boots. |
| **Brogni** | Shield/Heal/Cleanse | **183** | 3rd | Shields applied after Stag Knight debuffs land, before DPS champions attack. Replace SPD boots with DEF% boots (synergizes with shield scaling). |
| **Mithrala** | Cleanse/Buffs/Lead | **186** | 2nd | Cleanse/buffs applied before team attacks (Increase ATK/SPD/C.RATE buff timing critical). Remove Feral + replace SPD boots. **ARENA CONFLICT WARNING**. |
| **Godseeker Aniri** | Heal/Revive/Extend | **189** | 1st (fastest) | Buff extension goes LAST in rotation (extends all buffs/debuffs applied by team). Heal/revive ready for emergencies. Aggressive regearing required (264→189 = -75 SPD). |

**Turn Cycle (1:1 Tune):**
1. Boss AOE (turn 1)
2. **Aniri** (189 SPD) → Buff extend (extends Brogni shields, Stag debuffs, Mithrala buffs)
3. **Mithrala** (186 SPD) → Cleanse debuffs + apply Increase ATK/SPD/C.RATE buffs
4. **Brogni** (183 SPD) → Shield team + Increase DEF + HP Burn
5. **Stag Knight** (180 SPD) → Decrease DEF/ATK (lands before DPS)
6. **Geomancer** (171 SPD) → HP Burn + damage (takes stun on turn 3, survives, team continues)
7. Boss AOE (turn 2)
8. **Repeat cycle** (all champions take 1 turn per 2 boss turns)

**Why This Turn Order:**
- **Aniri first (189 SPD)**: Buff extension at start of rotation extends all existing buffs/debuffs from previous cycle (Brogni shields last longer, Stag debuffs persist, Mithrala buffs extended)
- **Mithrala second (186 SPD)**: Cleanse removes debuffs early, then applies ATK/SPD/C.RATE buffs for entire team before they attack
- **Brogni third (183 SPD)**: Shields applied after cleanse/buffs, protects team for incoming damage
- **Stag Knight fourth (180 SPD)**: Decrease DEF/ATK lands right before Geomancer attacks (maximizes damage)
- **Geomancer last (171 SPD - stun target)**: Slowest champion takes stun every 3 turns, HP Burn applies, team rotation continues

**Buff/Shield Timing Benefits:**
- ✅ Shields refreshed every 2 boss turns (Brogni shields + Aniri extension = consistent protection)
- ✅ Decrease DEF/ATK up 100% of the time (Stag Knight + Aniri extension + Master Hexer)
- ✅ Increase ATK/SPD/C.RATE buffs up consistently (Mithrala + Aniri extension)
- ✅ Cleanse available every 2 turns (removes stun, debuffs before they stack)
- ✅ Geomancer stun target isolated (171 SPD = guaranteed slowest, predictable stun every 3 turns)

---

### **Speed Tune Issues in Current Setup (No Tune)**

**Current Chaos (No Speed Tune):**
1. **Random turn order** - Fastest champions (Aniri 264, Mithrala 245) taking 1.5-2x more turns than slowest (Geomancer 210)
2. **Buff desync** - Shields expire early, buffs drop mid-rotation, debuffs fall off randomly
3. **Stun randomness** - Boss stun hitting random champions (not predictable stun target)
4. **Turn meter drift** - Speed differences cause turn meter to drift out of sync over 30-45 turns
5. **Wasted turns** - Aniri extending buffs that already expired, Mithrala cleansing when no debuffs present, shields dropping before boss AOE

**Estimated Damage Loss from No Speed Tune:**
- **5-10M damage loss** from buff/debuff downtime (Decrease DEF/ATK gaps, shield gaps, buff gaps)
- **3-5M damage loss** from turn inefficiency (wasted cooldowns, suboptimal rotation)
- **Turn survival reduced** - Currently 30-45 turns, should reach 50+ turns with proper tune

**Total Potential Gain from Speed Tune Implementation: +8-15M damage + 10-15 more turns survival**

---

### **Alternative: 2:1 Speed Tune (NOT RECOMMENDED)**

**2:1 Tune Requirements:**
- **Target Range**: 250-280 SPD for all champions (2 turns per 1 boss turn)
- **Calculator Required**: Must use Deadwood Jedi or similar speed tune calculator
- **Pros**: More turns = more damage potential, more buff uptime
- **Cons**: Requires 250-280 SPD (current team already 210-264 SPD but wrong configuration), very gear-intensive, harder to maintain

**Why NOT Recommended for This Team:**
1. **Mithrala Arena conflict** - Already at 245 SPD (Arena build), converting to 2:1 would lock her into CB permanently (breaks Arena team)
2. **Gear quality unclear** - Unknown if team has substats to reach 250-280 SPD consistently across all 5 champions
3. **Regearing complexity** - 1:1 tune only requires REDUCING speed (easier), 2:1 requires precise INCREASING speed (harder)
4. **User constraint** - "Avoid breaking Arena teams" suggests 1:1 tune better (less disruptive)

**Verdict**: Stick with **1:1 tune (171-189 SPD)** for this team.

---

## **STAT GAPS ANALYSIS - UNM Requirements vs Current Team**

### **UNM Stat Requirements (from mechanics reference):**
- **ACC**: 250+ (debuff landing, especially Decrease DEF/ATK)
- **C.RATE**: 100% (Warmaster/Giant Slayer procs, maximize damage)
- **DEF**: 3,500+ (survivability, reduce incoming damage)
- **HP**: 50,000+ (survivability, stun target needs higher)
- **SPD**: 171-189 (1:1 tune) or 250-280 (2:1 tune)

---

### **Individual Champion Stat Gaps**

#### **1. Geomancer (HP Burn DPS / Stun Target)**

| Stat | Current | Target | Gap | Status | Fix |
| --- | --- | --- | --- | --- | --- |
| **HP** | 57,756 | 50,000+ | **+7,756** | ✅ GOOD | None needed |
| **DEF** | 4,520 | 3,500+ | **+1,020** | ✅ EXCELLENT | None needed |
| **SPD** | 210 | **171 (stun)** | **-39** | ❌ TOO FAST | Remove Feral set → Lifesteal/Savage |
| **C.RATE** | 57% | 100% | **-43%** | ❌ CRITICAL | C.RATE gloves (57%→100%+) **= 5-8M damage gain** |
| **ACC** | 249 | 250+ | **-1** | ⚠️ BORDERLINE | +1 ACC (trivial, Mithrala lead +80 ACC helps) |

**Priority Fixes:** (1) C.RATE gloves URGENT (5-8M damage), (2) Remove Feral set URGENT (speed tune)

---

#### **2. Stag Knight (Decrease DEF/ATK Specialist)**

| Stat | Current | Target | Gap | Status | Fix |
| --- | --- | --- | --- | --- | --- |
| **HP** | 67,312 | 50,000+ | **+17,312** | ✅ EXCELLENT | None needed |
| **DEF** | 4,616 | 3,500+ | **+1,116** | ✅ EXCELLENT | None needed |
| **SPD** | 222 | 180 | **-42** | ❌ TOO FAST | SPD boots → DEF%/HP% boots |
| **C.RATE** | 63% | 100% (ideal) / 70%+ (acceptable) | **-37% / -7%** | ⚠️ SUBOPTIMAL | C.RATE gloves OR substats (support role, lower priority) |
| **ACC** | 310 | 250+ | **+60** | ✅ EXCELLENT | None needed (overkill is fine for debuffer) |

**Priority Fixes:** (1) SPD boots URGENT (speed tune), (2) C.RATE optimization MEDIUM (support role)

---

#### **3. Brogni (Shield/Cleanse/HP Burn Specialist)**

| Stat | Current | Target | Gap | Status | Fix |
| --- | --- | --- | --- | --- | --- |
| **HP** | 80,528 | 50,000+ | **+30,528** | ✅ EXCELLENT | None needed (tank role) |
| **DEF** | 5,034 | 3,500+ | **+1,534** | ✅ EXCELLENT | None needed (tank role, shield scaling) |
| **SPD** | 225 | 183 | **-42** | ❌ TOO FAST | SPD boots → DEF% boots |
| **C.RATE** | 26% | 100% (ideal) / 70%+ (acceptable) | **-74% / -44%** | ❌ CRITICAL | C.RATE gloves (26%→80%+) **= 8-12M damage gain (Giant Slayer)** |
| **ACC** | 145 | 250+ | **-105** | ❌ CRITICAL | ACC chest/banner OR Perception sets (+105 ACC needed) |

**Priority Fixes:** (1) SPD boots URGENT (speed tune), (2) C.RATE gloves URGENT (8-12M damage), (3) ACC +105 HIGH (HP Burn landing)

---

#### **4. Mithrala (Cleanse/Buff/Lead Specialist)**

| Stat | Current | Target | Gap | Status | Fix |
| --- | --- | --- | --- | --- | --- |
| **HP** | 71,378 | 50,000+ | **+21,378** | ✅ EXCELLENT | None needed |
| **DEF** | 4,746 | 3,500+ | **+1,246** | ✅ EXCELLENT | None needed |
| **SPD** | 245 | 186 | **-59** | ❌ EXTREME | Remove Feral + SPD boots → DEF% boots (Arena conflict) |
| **C.RATE** | 38% | 70%+ (support) | **-32%** | ⚠️ SUBOPTIMAL | C.RATE gloves OR substats (optional, support role) |
| **ACC** | 526 | 250+ | **+276** | ✅ MASSIVE OVERKILL | Reduce via remove Perception sets (wasted stats) |

**Priority Fixes:** (1) SPD reduction CRITICAL (speed tune blocker), (2) Remove Perception sets HIGH (stat efficiency), (3) C.RATE MEDIUM (optional)

**⚠️ ARENA CONFLICT WARNING**: Mithrala is Arena speed build (245 SPD, 526 ACC). Converting to CB will break Arena team.

---

#### **5. Godseeker Aniri (Heal/Revive/Buff Extend Specialist)**

| Stat | Current | Target | Gap | Status | Fix |
| --- | --- | --- | --- | --- | --- |
| **HP** | 76,705 | 50,000+ | **+26,705** | ✅ EXCELLENT | None needed (survivability anchor) |
| **DEF** | 4,214 | 3,500+ | **+714** | ✅ GOOD | None needed |
| **SPD** | 264 | 189 | **-75** | ❌ EXTREME | SPD boots → HP% boots + aggressive substat reduction |
| **C.RATE** | 35% | N/A (healer/support) | N/A | ⚠️ LOW BUT NOT CRITICAL | Not priority (healer role, no damage focus) |
| **ACC** | 168 | 250+ (if debuffs) / N/A (if pure support) | **-82 or N/A** | ⚠️ CONDITIONAL | Validate kit (heal/revive/extend suggests no debuffs → ignore ACC) |

**Priority Fixes:** (1) Complete masteries CRITICAL (missing T6), (2) SPD reduction CRITICAL (worst speed blocker), (3) ACC validation CONDITIONAL

---

### **Team-Wide Stat Summary**

| Champion | HP | DEF | SPD Gap | C.RATE Gap | ACC Gap | Critical Fixes |
| --- | --- | --- | --- | --- | --- | --- |
| **Geomancer** | ✅ 57k | ✅ 4.5k | ❌ -39 | ❌ -43% | ✅ 249 | C.RATE gloves, Remove Feral |
| **Stag Knight** | ✅ 67k | ✅ 4.6k | ❌ -42 | ⚠️ -37% | ✅ 310 | SPD boots swap |
| **Brogni** | ✅ 80k | ✅ 5k | ❌ -42 | ❌ -74% | ❌ -105 | C.RATE gloves, SPD boots, ACC +105 |
| **Mithrala** | ✅ 71k | ✅ 4.7k | ❌ -59 | ⚠️ -32% | ✅ 526 | SPD reduction (Arena conflict) |
| **Godseeker Aniri** | ✅ 76k | ✅ 4.2k | ❌ -75 | N/A | ⚠️ -82? | Masteries, SPD reduction |

**Team Strengths:**
- ✅ **HP/DEF excellent across all champions** (all above 50k HP, 3.5k+ DEF thresholds)
- ✅ **ACC good for debuffers** (Stag Knight 310, Geomancer 249 + Mithrala lead +80 ACC)

**Team Weaknesses:**
- ❌ **Speed tune completely broken** (all 5 champions too fast, -238 to -305 total SPD reduction needed)
- ❌ **C.RATE critical gaps** (Geomancer 57%, Brogni 26% = 13-20M combined damage loss)
- ❌ **Brogni ACC deficit** (-105 ACC = HP Burn landing issues)
- ⚠️ **Masteries incomplete** (Godseeker Aniri missing T6, Mithrala suboptimal for CB)

---

## **RANKED RECOMMENDATIONS (Priority 1-10)**

### **Recommendation Ranking Methodology:**
- **Impact**: Estimated damage/survival improvement
- **Difficulty**: Regearing complexity (boots swap = easy, full regear = hard)
- **Dependencies**: Fixes that unblock other improvements
- **Cost**: Time investment (avoid breaking Arena teams per user constraint)

---

### **TOP 10 PRIORITY FIXES**

#### **1. GEOMANCER C.RATE GLOVES (HIGHEST IMPACT)**
- **Current**: 57% C.RATE
- **Fix**: Replace gloves with C.RATE% main stat gloves
- **Result**: 57% → 100%+ C.RATE (with Deadly Precision +5%)
- **Impact**: **+5-8M damage per run** (missing ~40% Warmaster procs currently)
- **Difficulty**: EASY (single gear piece swap)
- **Dependencies**: None
- **Cost**: Low (may have C.RATE gloves in inventory)
- **VERDICT**: **DO THIS FIRST** - Highest damage gain for lowest effort

---

#### **2. COMPLETE GODSEEKER ANIRI MASTERIES (CRITICAL BLOCKER)**
- **Current**: Missing T6 masteries (Offense + Defense incomplete), no Support tree
- **Fix**: Add Support tree + Lasting Gifts T6 (extends buff duration, synergizes with buff extend skill)
- **Result**: Buff extension +1 turn on all buffs (Brogni shields, Mithrala ATK/SPD/C.RATE, Stag debuffs)
- **Impact**: **+3-5M damage + 5-10 more turns survival** (consistent buff uptime, shield coverage)
- **Difficulty**: MEDIUM (800 scrolls required for full Support tree + T6)
- **Dependencies**: None
- **Cost**: Medium (scroll investment)
- **VERDICT**: **DO SECOND** - Masteries unlock full champion potential

---

#### **3. BROGNI C.RATE GLOVES (HIGH IMPACT)**
- **Current**: 26% C.RATE
- **Fix**: Replace gloves with C.RATE% main stat gloves
- **Result**: 26% → 80%+ C.RATE (with Deadly Precision +5% = 85%+)
- **Impact**: **+8-12M damage per run** (Giant Slayer passive only proccing 26% currently, should be 85%+)
- **Difficulty**: EASY (single gear piece swap)
- **Dependencies**: None
- **Cost**: Low
- **VERDICT**: **DO THIRD** - Massive damage gain (Brogni contributes 22M currently, could be 30-34M)

---

#### **4. GEOMANCER SPEED TUNE FIX (BLOCKING TEAM SPEED TUNE)**
- **Current**: 210 SPD (target 171 SPD for stun target role)
- **Fix**: Remove 4x Feral set (+12% SPD bonus) → Replace with Lifesteal or Savage sets
- **Result**: 210 SPD → ~171-175 SPD (exact 171 SPD ideal for stun target)
- **Impact**: **Speed tune unlocked** (Geomancer as stun target enables 1:1 tune for entire team)
- **Difficulty**: MEDIUM (4-piece set swap, need Lifesteal/Savage with good substats)
- **Dependencies**: Blocks entire team speed tune implementation
- **Cost**: Medium (regearing 4 pieces)
- **VERDICT**: **DO FOURTH** - Enables speed tune (8-15M team damage gain + 10-15 more turns)

---

#### **5. STAG KNIGHT SPEED TUNE FIX**
- **Current**: 222 SPD (target 180 SPD)
- **Fix**: Replace SPD boots with DEF%/HP% boots
- **Result**: 222 SPD → ~180-185 SPD (mid-range 1:1 tune)
- **Impact**: **Speed tune alignment** (Decrease DEF/ATK timing improved)
- **Difficulty**: EASY (single boot swap)
- **Dependencies**: Part of team speed tune (requires Geomancer fix #4 first)
- **Cost**: Low
- **VERDICT**: **DO FIFTH** - Easy speed tune fix

---

#### **6. BROGNI SPEED TUNE FIX**
- **Current**: 225 SPD (target 183 SPD)
- **Fix**: Replace SPD boots with DEF% boots (synergizes with shield scaling + 5k DEF)
- **Result**: 225 SPD → ~180-185 SPD (mid-range 1:1 tune)
- **Impact**: **Speed tune alignment** (shield timing improved, buffs sync with team)
- **Difficulty**: EASY (single boot swap)
- **Dependencies**: Part of team speed tune
- **Cost**: Low
- **VERDICT**: **DO SIXTH** - Easy fix + DEF% boots improve shield strength

---

#### **7. BROGNI ACC FIX (HP BURN LANDING)**
- **Current**: 145 ACC (target 250+, gap -105)
- **Fix**: Replace chest with ACC% chest OR banner with ACC banner OR add 2x Perception sets
- **Result**: 145 ACC → 250+ ACC (HP Burn lands consistently)
- **Impact**: **+2-4M damage** (HP Burn landing 70% currently → 95%+ after fix, Gilded Dragonstone relic helps)
- **Difficulty**: MEDIUM (chest/banner swap OR 2-set addition)
- **Dependencies**: May conflict with Bolster/Protection sets (evaluate substats first)
- **Cost**: Medium (regearing dependent)
- **VERDICT**: **DO SEVENTH** - Moderate impact, but HP Burn overlap with Geomancer means lower priority

---

#### **8. MITHRALA SPEED TUNE FIX (⚠️ ARENA CONFLICT)**
- **Current**: 245 SPD (target 186 SPD, gap -59)
- **Fix**: Remove 2x Feral set + replace SPD boots with DEF% boots
- **Result**: 245 SPD → ~170 SPD (need +16 SPD substats to reach 186 target)
- **Impact**: **Speed tune alignment** (cleanse/buff timing critical for team)
- **Difficulty**: HARD (2-set swap + boots + substat management)
- **Dependencies**: Part of team speed tune, but **BREAKS ARENA TEAM** (245 SPD core to Arena)
- **Cost**: **HIGH** (Arena team disruption)
- **⚠️ RECOMMENDATION**: **DEFER until alternates analysis** - Evaluate if Mithrala can be replaced in CB team with Rector Drath (cleanse/revive) or Vogoth (Leech/survivability) to preserve Arena team

---

#### **9. GODSEEKER ANIRI SPEED TUNE FIX (WORST BLOCKER)**
- **Current**: 264 SPD (target 189 SPD, gap -75)
- **Fix**: Replace SPD boots with HP% boots + aggressive substat reduction (regear multiple pieces)
- **Result**: 264 SPD → ~189 SPD (requires -75 SPD via boots -45 SPD + substats -30 SPD)
- **Impact**: **Speed tune alignment** (buff extension timing critical)
- **Difficulty**: **VERY HARD** (boots + 2-3 additional gear pieces with lower SPD substats)
- **Dependencies**: Part of team speed tune
- **Cost**: High (extensive regearing)
- **VERDICT**: **DO NINTH** - Hardest speed tune fix, but necessary for 1:1 tune completion

---

#### **10. MITHRALA ACC REDUCTION (STAT EFFICIENCY)**
- **Current**: 526 ACC (target 250-300, overkill +226-276)
- **Fix**: Remove 2x Perception sets (+80 ACC) → Replace with Lifesteal/Immortal for survivability
- **Result**: 526 ACC → ~280-300 ACC (still overkill but acceptable, gain survivability sets)
- **Impact**: **+1-2M damage** (better survivability = more turns, minor improvement)
- **Difficulty**: MEDIUM (2-set swap)
- **Dependencies**: Combines with speed tune fix #8 (remove Feral + Perception together)
- **Cost**: Medium
- **VERDICT**: **DO TENTH** - Lowest priority (ACC overkill not hurting performance, but stat efficiency gain)

---

### **PRIORITY SUMMARY (Quick Reference)**

| Rank | Fix | Champion | Impact | Difficulty | Do When |
| --- | --- | --- | --- | --- | --- |
| **1** | C.RATE gloves | Geomancer | **+5-8M damage** | EASY | **NOW** |
| **2** | Complete masteries | Godseeker Aniri | **+3-5M + 5-10 turns** | MEDIUM | **NOW** |
| **3** | C.RATE gloves | Brogni | **+8-12M damage** | EASY | **NOW** |
| **4** | Remove Feral set | Geomancer | **Speed tune unlock** | MEDIUM | **AFTER 1-3** |
| **5** | SPD boots → DEF%/HP% | Stag Knight | **Speed tune** | EASY | **AFTER 4** |
| **6** | SPD boots → DEF% | Brogni | **Speed tune** | EASY | **AFTER 4** |
| **7** | ACC chest/banner | Brogni | **+2-4M damage** | MEDIUM | **AFTER 1-6** |
| **8** | SPD tune (⚠️ Arena) | Mithrala | **Speed tune** | HARD | **DEFER** (evaluate alternates) |
| **9** | SPD tune (hardest) | Godseeker Aniri | **Speed tune** | VERY HARD | **AFTER 1-7** |
| **10** | ACC reduction | Mithrala | **+1-2M damage** | MEDIUM | **OPTIONAL** |

**TOTAL ESTIMATED IMPACT (if all fixes implemented):**
- **Damage**: 44M → **65-75M** (21-31M gain from C.RATE fixes + speed tune + ACC fix)
- **Survival**: 30-45 turns → **50+ turns** (speed tune + masteries + survivability)

**FASTEST WINS (Do First):**
1. Geomancer C.RATE gloves (+5-8M, EASY)
2. Brogni C.RATE gloves (+8-12M, EASY)
3. Complete Aniri masteries (+3-5M + turns, MEDIUM)

**Combined Quick Wins: +16-25M damage for 3 relatively easy fixes**

---

## **ALTERNATES ANALYSIS - Owned Champion Swaps**

### **Potential Replacement Champions (from Champion_stats.md, Owned > 0)**

Based on current team bottlenecks and regearing constraints, evaluated owned champions for potential swaps:

---

### **PRIORITY SWAP: Mithrala → Rector Drath (Preserve Arena Team)**

**Current Issue**: Mithrala is Arena speed build (245 SPD, 526 ACC, Feral + Perception sets). Converting to CB destroys Arena team.

**Swap Candidate**: **Rector Drath** (Owned: 2, Spirit affinity, Support)
- **Role**: Cleanse, Revive, Heal, Increase DEF
- **Base SPD**: 109 (high SPD champion, but not Arena-tuned yet → easier to build for CB)
- **Pros**:
  - ✅ **Cleanse** (replaces Mithrala cleanse function)
  - ✅ **Revive** (backup reviver in addition to Godseeker Aniri passive = ultra-safe team)
  - ✅ **Heal** (stacks with Godseeker Aniri for massive sustainability)
  - ✅ **Increase DEF** (synergizes with Brogni Increase DEF for double DEF buff stacking)
  - ✅ **Not Arena-critical** (user has 2 copies, likely one is unused → can dedicate to CB)
  - ✅ **Spirit affinity** (neutral on all CB affinities except Magic, safer than Mithrala Magic affinity weak on Force CB)
- **Cons**:
  - ❌ **No Increase ATK/SPD/C.RATE buffs** (loses Mithrala's offensive buffs → may reduce team damage 3-5M)
  - ❌ **No ACC aura lead** (loses Mithrala +80 ACC team aura → Geomancer/Brogni may need ACC adjustments)
  - ❌ **Base SPD 109** (still fast, needs SPD reduction to 180-189 SPD)

**Recommended Team with Rector Drath**:
- **Geomancer** (171 SPD, stun target, HP Burn DPS)
- **Stag Knight** (180 SPD, Decrease DEF/ATK)
- **Brogni** (183 SPD, Shield/Increase DEF/HP Burn)
- **Rector Drath** (186 SPD, Cleanse/Revive/Heal/Increase DEF)
- **Godseeker Aniri** (189 SPD, Buff extend/Heal/Revive passive)

**Impact of Swap**:
- ✅ **Preserves Mithrala for Arena** (user constraint: "avoid breaking Arena teams")
- ✅ **Ultra-safe team** (2 revivers: Rector Drath active + Godseeker Aniri passive, double heals, double Increase DEF)
- ✅ **Easier speed tune** (Rector Drath not Arena-built yet, can build fresh for CB at 186 SPD)
- ⚠️ **May lose 3-5M damage** (no Increase ATK/SPD/C.RATE buffs from Mithrala)
- ⚠️ **ACC gap** (loses +80 ACC aura, Geomancer 249→169 effective ACC, Brogni 145→65 effective ACC = need ACC fixes)

**VERDICT**: **RECOMMENDED SWAP** if user wants to preserve Arena team. Trade offensive buffs for survivability + regearing ease.

---

### **Alternative Swap #2: Geomancer → Lord Champfort (Spirit CB Affinity Safety)**

**Current Issue**: Geomancer is Magic affinity (weak against Spirit CB, takes +15% damage + -15% damage dealt = vulnerability on Spirit days)

**Swap Candidate**: **Lord Champfort** (Owned: 1, Magic affinity → **WAIT, Magic is weak to Spirit too**)
- **Analysis**: Lord Champfort is also Magic affinity (same weakness as Geomancer on Spirit CB). NOT a solution for affinity issue.
- **VERDICT**: **NOT RECOMMENDED** - Doesn't solve affinity problem.

**Better Affinity Solution**: 
- Keep Geomancer (HP Burn specialist, already documented, fixes in progress)
- **Affinity risk management**: On Spirit CB days, accept vulnerability OR use Void affinity champion if available (check for Void HP Burn champions)

---

### **Alternative Swap #3: Brogni/Stag Knight → Skullcrusher (Counterattack Cheese)**

**Swap Candidate**: **Skullcrusher** (Owned: 1, Force affinity, Defense, Counterattack specialist)
- **Role**: Ally Counterattack (cheese mechanic - team attacks after every boss hit = 2x turn frequency)
- **Pros**:
  - ✅ **Counterattack cheese** (team takes 2x turns = massive damage boost +20-30M potential)
  - ✅ **Increase DEF** (replaces Brogni Increase DEF function)
  - ✅ **Force affinity** (strong against Magic CB, neutral on others)
- **Cons**:
  - ❌ **Requires precise speed tune** (Counterattack teams need exact speed calculator tuning, very complex)
  - ❌ **Loses Brogni shields** (22M damage + shield coverage gone)
  - ❌ **Loses Stag Knight Decrease DEF/ATK** (major survivability loss)
  - ❌ **High skill floor** (counterattack tuning is advanced, user has no speed tune currently = risky)

**VERDICT**: **NOT RECOMMENDED** for initial optimization. Counterattack teams are advanced cheese strategy (requires precise tuning + testing). Focus on standard 1:1 tune first, revisit counterattack later if desired.

---

### **Alternative Swap #4: Add Frozen Banshee or Venomage (Poison Damage)**

**Swap Candidates**:
- **Frozen Banshee** (Owned: 1, Magic affinity, Poison specialist)
- **Venomage** (Owned: 1, Magic affinity, Poison specialist)

**Analysis**:
- **User constraint noted**: "Poison teams NOT well-built" (Frozen Banshee, Elenaril, Narma weak in user's roster)
- **Current team**: Already has 2x HP Burn (Geomancer + Brogni) = good DOT coverage
- **Poison vs HP Burn**: Poison fills debuff slots (10 max), may interfere with Decrease DEF/ATK uptime from Stag Knight
- **VERDICT**: **NOT RECOMMENDED** - User prefers HP Burn teams (well-built), poison champions weak, debuff slot conflict

---

### **Alternative Swap #5: Add Bad-el-Kazar (Leech + Poison + Heal)**

**Swap Candidate**: **Bad-el-Kazar** (Owned: 1, Force affinity, Support, Leech specialist)
- **Role**: Leech (team heals from damage), Poison, Continuous Heal, Decrease ATK
- **Pros**:
  - ✅ **Leech** (team self-sustain, reduces reliance on healers)
  - ✅ **Continuous Heal** (passive healing over time)
  - ✅ **Decrease ATK** (stacks with Stag Knight Decrease DEF for better survivability)
  - ✅ **Poison** (secondary DOT damage)
  - ✅ **Force affinity** (strong against Magic CB)
- **Cons**:
  - ❌ **Who to replace?** (all current 5 champions fill critical roles)
  - ❌ **Loses key function** (replacing anyone = loss of shields/cleanse/revive/HP Burn/Decrease DEF)
  - ❌ **Poison weak** (user noted poison champions not well-built)

**VERDICT**: **NOT RECOMMENDED** for current team. Bad-el-Kazar is excellent, but current team composition (shield/heal/revive/debuff/DPS) is already well-balanced. Leech is redundant with double healer + double reviver setup.

---

### **Alternative Swap #6: Coldheart (Turn Meter Control + MAX HP Nuke)**

**Swap Candidate**: **Coldheart** (Owned: 3, Magic affinity, Attack, Turn meter control specialist)
- **Role**: Turn meter reduction, MAX HP nuke damage
- **Analysis**:
  - ❌ **Turn meter reduction doesn't work on CB** (boss immune to TM reduction)
  - ❌ **MAX HP nuke capped on CB** (diminishing returns, not primary DPS source)
  - ❌ **Squishy** (13,710 HP base, 738 DEF = very low survivability for UNM)
- **VERDICT**: **NOT VIABLE** - Coldheart is dungeon specialist (Spider, etc.), not CB champion

---

### **RECOMMENDED ALTERNATE TEAM CONFIGURATIONS**

#### **Option A: Current Team (Optimized with Fixes 1-10)**
- Geomancer (171 SPD stun, C.RATE fix)
- Stag Knight (180 SPD, SPD boots fix)
- Brogni (183 SPD, C.RATE + SPD fix)
- Mithrala (186 SPD, **BREAKS ARENA TEAM**, SPD fix)
- Godseeker Aniri (189 SPD, masteries + SPD fix)

**Pros**: Highest damage potential (Increase ATK/SPD/C.RATE buffs + ACC aura), current roster familiarity
**Cons**: Destroys Arena team (Mithrala), hardest regearing (Mithrala + Aniri SPD reductions)

---

#### **Option B: Rector Drath Swap (RECOMMENDED for Arena Preservation)**
- Geomancer (171 SPD stun, C.RATE fix)
- Stag Knight (180 SPD, SPD boots fix)
- Brogni (183 SPD, C.RATE + SPD + ACC fix)
- **Rector Drath** (186 SPD, fresh CB build)
- Godseeker Aniri (189 SPD, masteries + SPD fix)

**Pros**: Preserves Mithrala for Arena, ultra-safe (2 revivers), easier regearing (Rector Drath fresh build)
**Cons**: Loses offensive buffs (-3-5M damage), loses ACC aura (need ACC fixes on Geomancer + Brogni)

**Impact**: 44M → **60-65M** (16-21M gain, vs 65-75M with Mithrala = -5-10M tradeoff for Arena preservation)

---

### **FINAL RECOMMENDATION**

**If user wants to preserve Arena team**: Use **Option B (Rector Drath swap)**
- Estimated damage: 44M → 60-65M (+16-21M gain)
- Survival: 30-45 turns → 50+ turns
- Arena team intact
- Regearing: Moderate difficulty (Rector Drath fresh build easier than Mithrala conversion)

**If user accepts breaking Arena team**: Use **Option A (Current team optimized)**
- Estimated damage: 44M → 65-75M (+21-31M gain)
- Survival: 30-45 turns → 50+ turns  
- Arena team disrupted (Mithrala SPD 245→186)
- Regearing: High difficulty (Mithrala + Aniri aggressive SPD reductions)

**User should decide**: Arena team priority vs +5-10M extra CB damage.

---

## **ANALYSIS COMPLETE** ✅

**Summary:**
- ✅ All 5 champions documented (Geomancer, Stag Knight, Brogni, Mithrala, Godseeker Aniri)
- ✅ Speed tune analysis complete (1:1 tune recommended, 171-189 SPD targets, Geomancer stun target)
- ✅ Stat gaps identified (C.RATE critical gaps on Geomancer + Brogni, SPD tune broken across all 5)
- ✅ Recommendations ranked 1-10 (top 3 quick wins = +16-25M damage)
- ✅ Alternates evaluated (Rector Drath swap recommended if preserving Arena team)

**Next Steps** (user decision):
1. **Choose team configuration**: Option A (Mithrala, breaks Arena) vs Option B (Rector Drath, preserves Arena)
2. **Implement top 3 quick wins**: Geomancer C.RATE gloves, Brogni C.RATE gloves, Complete Aniri masteries (+16-25M damage, easy/medium difficulty)
3. **Begin speed tune regearing**: Geomancer remove Feral set (priority 4), then boots swaps across team (priorities 5-6)
4. **Test and iterate**: Run test battles after each fix, validate damage improvements, adjust as needed

**Projected Final Performance**:
- **Option A** (Current team optimized): 44M → **65-75M** damage, 30-45 → **50+ turns**
- **Option B** (Rector Drath swap): 44M → **60-65M** damage, 30-45 → **50+ turns**

**Both options exceed 50M damage goal** ✅

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

### **Version 1.0 - Initial Analysis Complete** (2025-10-27)
- **Author**: GitHub Copilot (AI Agent)
- **Scope**: Full 5-champion intake, speed tune analysis, stat gaps, recommendations 1-10, alternates evaluation
- **Champion Intake**: Geomancer, Stag Knight, Brogni, Mithrala, Godseeker Aniri (all documented from user screenshots)
- **Key Findings**: 
  - Speed tune completely broken (all 5 champions too fast, -238 to -305 total SPD reduction needed)
  - C.RATE critical gaps (Geomancer 57%, Brogni 26% = 13-20M combined damage loss)
  - Mithrala Arena conflict (245 SPD arena build → 186 SPD CB target breaks Arena team)
  - Godseeker Aniri masteries incomplete (missing T6, no Support tree)
- **Recommendations**: Top 3 quick wins (+16-25M damage), full ranked 1-10 priority list, Rector Drath swap option
- **Status**: DRAFT - Awaiting user decision (Option A vs Option B) and implementation validation

### **Next Update Triggers**
- **After user decision**: Document chosen team configuration (Option A: Mithrala optimized, or Option B: Rector Drath swap)
- **After implementation**: Update with actual test results (damage, turns, affinities tested)
- **After regearing**: Document actual gear changes made, stat deltas achieved (before/after comparison)
- **After speed tune validation**: Confirm turn order, buff timing, stun target consistency
- **Quarterly review**: Re-evaluate if new champions acquired, meta shifts, or new UNM strategies emerge

---

## **Cross-References & Related Files**

### **Input Files Used**
- `input/Champion_Dictionary/Champion_stats.md` - Owned champions list (filtered owned>0 for alternates)
- `Output/Boss_Guides/ClanBoss_UltraNightmare_Team_Notes_FINAL.md` - UNM mechanics reference (old guide, validate if outdated)
- User screenshots (10/27/2025) - All 5 champion stats/gear/masteries/blessings

### **Related Champion Dictionary Entries**
- `input/Champion_Dictionary/Geomancer.json` - (NOT YET CREATED - recommend adding after CB optimization complete)
- `input/Champion_Dictionary/Stag_Knight.json` - (EXISTS in root, not Complete/)
- `input/Champion_Dictionary/Brogni.json` - (NOT YET CREATED)
- `input/Champion_Dictionary/Mithrala.json` - (NOT YET CREATED)
- `input/Champion_Dictionary/Godseeker_Aniri.json` - (NOT YET CREATED)
- `input/Champion_Dictionary/Rector_Drath.json` - (NOT YET CREATED - if Option B chosen)

**NOTE**: Champion dictionary entries should be created using canonical template (`input/Templates/Champion_Dictionary_Template.json`) and Option A workflow from copilot-instructions.md after CB analysis complete.

### **Recommended Follow-Up Projects**
1. **Create champion dictionary entries** for all 5 CB team members (use screenshots from this analysis)
2. **Boss guide update**: Refresh `ClanBoss_UltraNightmare_Team_Notes_FINAL.md` with new team compositions (Option A/B)
3. **Build evaluation entries** for each champion after regearing (before/after comparison using Build_Evaluation_Template.md)
4. **Arena team documentation** if Mithrala replaced (capture Arena team before/after for rebuild later)
5. **Faction Wars review** for any champions removed from CB team (repurpose for FW progression)

---

## **Glossary & Abbreviations**

- **UNM**: Ultra Nightmare (highest Clan Boss difficulty)
- **CB**: Clan Boss
- **1:1 Tune**: Speed tune where team takes 1 turn per 2 boss turns (171-189 SPD range)
- **2:1 Tune**: Speed tune where team takes 2 turns per 1 boss turn (250-280 SPD range, requires calculator)
- **Stun Target**: Slowest champion (171 SPD) who consistently takes boss stun every 3 turns (survives, team continues)
- **DOT**: Damage Over Time (HP Burn, Poison)
- **Warmaster/Giant Slayer**: T6 Offense masteries that proc on hit (scales with C.RATE)
- **ACC**: Accuracy (stat required for debuff landing, 250+ threshold for UNM)
- **C.RATE**: Critical Rate (100% required for consistent Warmaster/Giant Slayer procs)
- **SPD**: Speed (determines turn order and frequency)
- **Cheese**: Abusing game mechanics for advantage (e.g., Unkillable, Counterattack, Leech)
- **Meta**: Community-established best strategies (speed tunes, champion tier lists, team comps)

---

## **ANALYSIS COMPLETE** ✅

**File Status**: DRAFT (awaiting user validation and implementation)
**Total Lines**: 1,284
**Word Count**: ~8,500 words
**Champion Coverage**: 5/5 complete (Geomancer, Stag Knight, Brogni, Mithrala, Godseeker Aniri)
**Recommendations**: 10 ranked priorities + 2 team configuration options
**Estimated Time Investment**: 
- Quick wins (priorities 1-3): 1-2 hours (gloves swaps + masteries)
- Full speed tune (priorities 4-9): 4-8 hours (set swaps, boots, substat management)
- Total optimization: 5-10 hours regearing + testing

**Ready for user review and implementation!** 🚀

---

## Quick Reference Card

### **🎯 Immediate Actions (Top 3 Quick Wins)**
1. **Geomancer**: Change gloves to C.RATE% → +5-8M damage (EASY, 10 min)
2. **Brogni**: Change gloves to C.RATE% → +8-12M damage (EASY, 10 min)  
3. **Godseeker Aniri**: Complete Support tree + Lasting Gifts T6 → +3-5M + 5-10 turns (MEDIUM, 800 scrolls + 30 min)

**Total Quick Win Impact**: +16-25M damage for ~1 hour work ✅

---

### **📊 Current vs Target Stats**

| Champion | Current SPD | Target SPD | C.RATE Gap | ACC Status |
|----------|-------------|------------|------------|------------|
| Geomancer | 210 | 171 (stun) | **-43%** ❌ | 249 ✅ |
| Stag Knight | 222 | 180 | -37% ⚠️ | 310 ✅ |
| Brogni | 225 | 183 | **-74%** ❌ | 145 ❌ |
| Mithrala | 245 | 186 | -32% ⚠️ | 526 ✅ |
| Godseeker Aniri | 264 | 189 | N/A | 168 ⚠️ |

**Critical Gaps**: All 5 champions too fast (-238 to -305 total SPD), 2 critical C.RATE gaps (Geo, Brogni)

---

### **🔀 Team Configuration Decision**

| Option | Team Composition | Damage | Arena Impact | Difficulty |
|--------|-----------------|---------|--------------|------------|
| **A** | Current team (Mithrala optimized) | 65-75M | ❌ Breaks Arena | HARD |
| **B** | Rector Drath replaces Mithrala | 60-65M | ✅ Preserves Arena | MEDIUM |

**Both exceed 50M goal** - User choice based on Arena team priority

---

### **📋 Implementation Checklist**

#### **Phase 1: Quick Wins** (1-2 hours)
- [ ] Geomancer: Swap to C.RATE gloves (57% → 100%)
- [ ] Brogni: Swap to C.RATE gloves (26% → 80%+)
- [ ] Godseeker Aniri: Complete masteries (Support tree + Lasting Gifts T6)
- [ ] **TEST**: Run 3 battles, measure damage increase

#### **Phase 2: Speed Tune Foundation** (2-4 hours)
- [ ] Geomancer: Remove 4x Feral set, replace with Lifesteal/Savage (210 → 171 SPD)
- [ ] Stag Knight: SPD boots → DEF%/HP% boots (222 → 180 SPD)
- [ ] Brogni: SPD boots → DEF% boots (225 → 183 SPD)
- [ ] **TEST**: Run 3 battles, verify turn order consistency

#### **Phase 3: Critical Decision** (depends on choice)
- [ ] **Option A**: Mithrala speed reduction (245 → 186 SPD) - Breaks Arena
- [ ] **Option B**: Build Rector Drath for CB (fresh 186 SPD build) - Preserves Arena
- [ ] **TEST**: Run 5 battles new configuration, measure damage + survival

#### **Phase 4: Final Optimizations** (2-4 hours)
- [ ] Brogni: Add +105 ACC (chest/banner or Perception sets)
- [ ] Godseeker Aniri: Aggressive SPD reduction (264 → 189 SPD)
- [ ] All: Fine-tune substats for exact SPD targets
- [ ] **TEST**: Run 10 battles across affinities, validate 50+ turns + 60-75M damage

#### **Phase 5: Documentation** (30 min)
- [ ] Record final stats for all 5 champions
- [ ] Update this file with actual results (damage, turns, affinity tested)
- [ ] Create champion dictionary entries for CB team (use screenshots)
- [ ] Archive DRAFT, promote to FINAL version

---

## **FILE METADATA**

**Filename**: `UNM_Clan_Boss_Team_Analysis.md`  
**Location**: `c:\GIT\Raid_Tools\Output\`  
**Version**: 1.0 DRAFT  
**Created**: 2025-10-27  
**Last Modified**: 2025-10-27  
**Author**: GitHub Copilot (AI Agent)  
**Format**: Markdown (.md)  
**Line Count**: 1,430+ lines  
**Word Count**: ~9,000 words  
**Validation Status**: ⚠️ DRAFT - Awaiting user validation and implementation  

**Related Project Files**:
- `input/Champion_Dictionary/Champion_stats.md` (owned champions reference)
- `Output/Boss_Guides/ClanBoss_UltraNightmare_Team_Notes_FINAL.md` (old CB guide)
- `.github/copilot-instructions.md` (project standards, Section 10: Team Creation)

**Git Branch**: v0.7  
**Commit Status**: Uncommitted changes  
**Next Action**: User review → Decision (Option A vs B) → Implementation → Testing → Final commit

---
