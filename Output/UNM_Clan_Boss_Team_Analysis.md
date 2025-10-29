# UNM Clan Boss Team Analysis

**Date**: 2025-10-27  
**Status**: In Progress - Champion Intake  
**Goal**: Optimize existing 5-champion UNM team from 44M → 50M+ damage with proper speed tune

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
| **1\. URGENT** | Gloves: C.RATE main stat | +40-50% DPS | 57% → 100%+ C.RATE |
| **2\. URGENT** | Remove Feral set → Lifesteal/Savage | Fix speed tune | 210 → 171 SPD target |
| **3\. HIGH** | SPD boots substats adjustment | Speed tune | Exactly 171 SPD (stun target) |
| **4\. MEDIUM** | C.DMG optimization | +15-20% DPS | 139% → 200%+ C.DMG |

* * * * *

**Questions Before Next Champion**
----------------------------------

1.  **Stun Target**: Should Geomancer be the designated stun target at **171 SPD exactly**? (He has good survivability with 57k HP + 4520 DEF)
    A. Unsure. Wait until all champions are input then review and recommend.

2.  **Gear Priority**: Can you regear Geomancer now, or document all 5 champions first for holistic analysis?
    A. let's document all 5. regearing can be time intensive and I'll mostly try to get close with what I have, without breaking my arena or other teams if possible. Speed might be managed for Mithrala and high speed champions by swapping Speed boots for Def% or HP%, same with accessories for flat stats.

3.  **Warmaster Procs**: With 57% C.RATE, you're only getting Warmaster on ~60% of multi-hits → **this alone is costing 5-8M damage per run**
    A. note this, if not already, and remove this question. 