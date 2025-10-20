# Boss Guide Update & Validation Prompt

**Date:** October 19, 2025  
**Purpose:** Systematically update all boss guides using UNM Clan Boss validation methodology  
**Methodology:** Comprehensive champion mechanics validation, aura verification, passive skill classification, affinity safety analysis

---

## 📋 TABLE OF CONTENTS

1. [Overview & Objectives](#overview--objectives)
2. [UNM Validation Methodology Summary](#unm-validation-methodology-summary)
3. [Boss Guide Update Workflow](#boss-guide-update-workflow)
4. [Priority Boss Queue](#priority-boss-queue)
5. [Validation Checklist (Per Boss)](#validation-checklist-per-boss)
6. [Critical Validation Requirements](#critical-validation-requirements)
7. [Output Standards](#output-standards)
8. [Questions for User](#questions-for-user)

---

## 1. OVERVIEW & OBJECTIVES

### **Project Goal**
Apply the comprehensive validation methodology developed for UNM Clan Boss to ALL existing boss guides, ensuring:
- All champion auras validated for content applicability (Arena-only, Dungeon-only, All Battles)
- All passive skills validated for damage classification (Patch 4.40, 4.70 changes documented)
- All champion mechanics cross-validated with 2+ authoritative sources (Ayumilove, HellHades, RaidHQ)
- Affinity safety/risk documented for every team and champion
- Executive summaries added with Top 3-5 recommendations per boss
- Implementation guides added with gear/masteries/books for top champions

### **Scope**
- **Total Boss Guides to Update:** ~8-12 guides (estimate based on existing files in `Notes/` directory)
- **Priority Order:** Sand Devil (Normal → Hard), Fire Knight (Hard), Dragon (Hard), Spider (Hard), Ice Golem (Hard), Iron Twins (DRAFT → FINAL), Hydra, Chimera, Shredder (DRAFT), Amius Cursed City (DRAFT)
- **Difficulty Focus:** Hard mode by default, but update Normal first if it already exists
- **Batch Approach:** Process 2 bosses per batch, complete all validations before moving to next batch

---

## 2. UNM VALIDATION METHODOLOGY SUMMARY

### **What We Did for UNM Clan Boss (Complete Process)**

**UPDATE 0: Champion Validation & Gap Analysis**
- ✅ Validated all 4 base team champions (skills, mechanics, cooldowns, multipliers)
- ✅ Identified critical gaps (Decrease DEF, Poison, Decrease ATK, Ally Attack)
- ✅ Documented 3 speed tuning options (1:1, 2:1, Hybrid)
- ✅ Cross-validated with Ayumilove + HellHades + in-game stats

**UPDATE 1: Top 24 Champions & Basic Simulations**
- ✅ grep_search for owned champions with critical mechanics
- ✅ Curated Top 24 by role with rationale tables
- ✅ Basic damage/survivability estimates
- ✅ Filtered to Top 16 based on simulated results

**UPDATE 2: Top 16 → Top 8 Detailed Analysis**
- ✅ Detailed simulations with speed/gear/stun optimization
- ✅ Affinity risk documented for each champion
- ✅ Refined damage estimates with ACC/turn count validation
- ✅ Filtered to Top 8 finalists

**UPDATE 3: Final Deep-Dive Analysis**
- ✅ Team summary table (Top 8 champions)
- ✅ Champion ranking charts (3 categories: Most Users, Damage-Focused, New Players)
- ✅ Final recommendations with priority pick order
- ✅ Simulation results (minimum 3 test runs per team documented)

**Section 13: CRITICAL AURA VALIDATION**
- ✅ Validated all champion auras for Clan Boss applicability
- ✅ **CRITICAL ERROR DISCOVERED:** Arbiter aura is Arena-only (30% SPD does NOT apply to Clan Boss)
- ✅ **Stag Knight aura is Dungeons-only** (24% SPD does NOT apply to Clan Boss)
- ✅ **Tagoar aura is All Battles** (+33% DEF DOES apply to Clan Boss)
- ✅ Pattern recognition: "in the Arena" vs "in Dungeons" vs "in all Battles"

**Section 14: PASSIVE MECHANICS VALIDATION**
- ✅ **Geomancer (Patch 4.70):** Reflect damage NO LONGER procs Warmaster/Giant Slayer or Lifesteal sets
  * Optimal Mastery: Warmaster (higher activation on A1/A3 direct hits)
  * Expected: 15-20M per UNM run
- ✅ **Brogni (Patch 4.40):** Shield damage STILL procs Giant Slayer (MULTIPLE procs, one per ally with shield)
  * Optimal Mastery: Giant Slayer (NOT Warmaster)
  * Expected: 15-25M per UNM run
  * **Plarium Confirmed:** "Giant Slayer proc/trigger multiple times from Underpriest Brogni's passive skill when the shield reflects damage is working as intended"
- ✅ Validated all artifact sets, masteries, buff interactions, speed tune breakpoints

**Section 15: Executive Summary & Implementation Guide**
- ✅ Top 3 recommendations with quick reference table
- ✅ Critical validation findings summary
- ✅ User goal priority pick
- ✅ Step-by-step implementation guide (Tagoar build, speed tuning, Brogni ACC fix, testing checklist)
- ✅ Backup champions listed
- ✅ Long-term optimization roadmap

### **Key Validation Discoveries**

**1. Aura Content Restrictions:**
- **Arena-only auras:** Arbiter (30% SPD), High Khatun, Gorgorab
- **Dungeon-only auras:** Stag Knight (24% SPD), Rhazin (30% DEF)
- **All Battles auras:** Tagoar (33% DEF), Bad-el-Kazar (33% HP), Tayrel (25% ATK), Deacon Armstrong (19% SPD)

**2. Passive Skill Classifications (Post-Patch):**
- **Geomancer:** "Damage Reflect" classification → NO Warmaster/GS/Lifesteal procs
- **Brogni:** "Shield Damage Reflect" classification → YES Giant Slayer procs (multiple), NO Warmaster procs
- **Why different:** Brogni released before nerf (April 2021), Plarium confirmed GS interaction is intentional

**3. Affinity Safety Documentation:**
- Every team requires explicit affinity safety/risk analysis
- Multi-line format for each team (per champion affinity vs boss affinity)
- Example: "Champion A (Magic): WEAK vs Force boss, may miss debuffs (60% weak hit rate observed)"

**4. Damage Estimate Validation:**
- Conservative estimates based on in-game testing
- Minimum 3 simulations per team documented
- Clear methodology: average vs peak, manual vs auto

---

## 3. BOSS GUIDE UPDATE WORKFLOW

### **Standard Workflow for Each Boss (8 Steps)**

**STEP 1: Pre-Update Assessment**
- [ ] Read existing boss guide (Normal or Hard, whichever exists)
- [ ] Identify all recommended champions in guide
- [ ] Check if champions are in owned champion list (`input/Owned_champion_list.md`)
- [ ] Flag any auras mentioned in guide for validation
- [ ] Flag any passive skills mentioned in guide for validation

**STEP 2: Aura Validation**
- [ ] Fetch Ayumilove pages for all champions with auras mentioned in guide
- [ ] Document aura wording (exact text: "in the Arena", "in Dungeons", "in all Battles")
- [ ] Create aura validation table:
  * Champion | Aura | Content Applicability | Applies to [Boss Name]?
- [ ] Update all recommendations if aura errors found

**STEP 3: Passive Skill Validation**
- [ ] Identify all champions with passive damage/reflect/proc mechanics
- [ ] Fetch Ayumilove pages for passive skill wording
- [ ] Check for Patch 4.40, 4.70, or other patch notes affecting passive
- [ ] Document mastery recommendations (Warmaster vs Giant Slayer)
- [ ] Create passive validation table:
  * Champion | Passive Type | Patch Changes | Warmaster/GS? | Expected Damage

**STEP 4: Affinity Safety Analysis**
- [ ] Document boss affinity (Magic, Force, Spirit, Void)
- [ ] For each recommended champion, document affinity safety:
  * SAFE: Strong or neutral affinity vs boss
  * RISKY: Weak affinity vs boss (may miss debuffs/attacks)
- [ ] Add multi-line affinity safety notes to ALL team recommendations
- [ ] Example format:
  ```
  Affinity Safety/Risk:
  - Champion A (Magic): Safe vs Spirit boss
  - Champion B (Force): Risky vs Magic boss, may miss debuffs
  - Champion C (Void): Safe (neutral vs all affinities)
  ```

**STEP 5: Champion Ranking & Top Recommendations**
- [ ] Re-rank champions based on validated mechanics
- [ ] Adjust damage estimates if aura/passive errors found
- [ ] Create Top 3-5 recommendations table:
  * Rank | Champion | Affinity | Damage/Clear Time | Aura | Why Choose | Investment
- [ ] Document backup champions (Top 6-8)

**STEP 6: Executive Summary Creation**
- [ ] Add Executive Summary section at top of guide
- [ ] Include:
  * Top 3-5 champion recommendations (quick reference table)
  * Critical validation findings (aura errors, passive changes)
  * User goal priority pick (fastest clear, safest, easiest to gear)
  * Expected clear times/damage for each difficulty (Normal, Hard, if applicable)

**STEP 7: Implementation Guide Addition**
- [ ] For Top 3 champions, add detailed build guides:
  * Gear requirements (sets, stats, priorities)
  * Masteries (Tier 6 choice, key masteries)
  * Skill books (priority order)
  * Speed tuning (if applicable)
  * Expected contribution (damage, survivability, utility)
- [ ] Add testing checklist:
  * Run 3-5 test battles
  * Document clear times, success rate, deaths
  * Optimize gear/speed based on results

**STEP 8: Final Validation & Documentation**
- [ ] Update Table of Contents (add Executive Summary, Implementation Guide sections)
- [ ] Run document checklist:
  * ✅ Aura validation complete
  * ✅ Passive mechanics validated
  * ✅ Affinity safety documented for all teams
  * ✅ Executive summary added
  * ✅ Implementation guide added for Top 3
  * ✅ Validation sources cited (Ayumilove, HellHades, RaidHQ)
- [ ] Mark guide as "VALIDATED" with date
- [ ] Commit changes with detailed message

---

## 4. PRIORITY BOSS QUEUE

### **Batch 0: UNM Clan Boss (CURRENT PRIORITY - IN PROGRESS)**

**Boss 0: UNM Clan Boss (Ultra Nightmare)**
- **Files to Update:**
  * `Notes/UNM_Team_Optimization_DRAFT.md` (CURRENT - Continue optimization)
- **Priority:** CRITICAL (user content priority #1: Clan Boss UNM)
- **Current Status:** Base 4-champion analysis complete (Geo/Mithrala/Aniri/Brogni)
- **NEW FOCUS:** Team composition optimization for MAXIMUM DAMAGE
  * **Phase A:** Integrate Stag Knight as CORE 5th champion (replaces gap analysis)
    - Stag Knight brings: Decrease DEF 60% + Decrease ATK 50% + 24% SPD aura (Dungeons only)
    - **CRITICAL:** Validate if Stag Knight aura applies to Clan Boss or Dungeons only
    - Speed tune: Stag Knight positioning in turn order (before DPS, after buffers)
    - Expected damage: 120M-140M with Stag Knight core
  
  * **Phase B:** Explore Aniri Replacement Options (free up slot for higher damage)
    - **Candidates:** Arbiter (revive + TM boost), Rector Drath (revive + Block Debuffs), Scyl (revive + heal)
    - **Goal:** Replace Aniri's buff extension with higher raw damage or better synergy
    - **Trade-off:** Lose buff extension (Brogni shields/Block Debuffs shorter) vs gain raw damage/utility
  
  * **Phase C:** Explore Geomancer Replacement Options (if HP Burn redundant)
    - **Candidates:** Champions with higher raw damage than Geomancer passive reflect
    - **Consideration:** Geomancer is current HP Burn source - only replace if better HP Burn champion exists OR HP Burn not optimal
    - **Candidates:** Ninja (HP Burn + nuke), Artak (HP Burn A2 + raw damage), other high-damage dealers
  
  * **Phase D:** Explore Brogni Replacement Options (if shields not critical for damage)
    - **Candidates:** Champions with higher raw damage or better debuff synergy
    - **Consideration:** Brogni provides: Block Debuffs, Shields (passive damage procs), survivability
    - **Trade-off:** Lose survivability/passive damage vs gain raw damage/better debuffs
    - **Candidates:** High-damage dealers, Decrease DEF champions (if Stag Knight not core)

  * **Phase E:** High-Damage Champion Analysis (Owned List)
    - **Focus:** Champions with mechanics that enable high Clan Boss damage:
      * Poison specialists: Fayne, Venomage, Frozen Banshee, Narma (2.5% MAX HP per poison per turn)
      * Ally Attack: Nogdar x2, Seeker x2, Tagoar (extra turns = more procs/damage)
      * Counterattack: Skullcrusher (doubles all champion attacks)
      * Enemy MAX HP damage: Coldheart x3 (but limited on Clan Boss), Fayne (Decrease DEF + Poison)
      * Raw nukers: Ninja, Artak, Sun Wukong, Ithos (if viable for Clan Boss)
      * Buff/Debuff amplifiers: Rhazin (Weaken + Decrease DEF), Tayrel (Decrease DEF + Decrease ATK)
    - **Validation:** Check each champion's Clan Boss rating (10/10, 9/10, 8/10 from reviews)
    - **Expected outcome:** Identify Top 5-8 highest damage champions to test in team compositions

  * **Phase F:** Team Composition Simulations (5-8 unique teams)
    - **Team 1:** Mithrala + Stag Knight + [3 highest damage champions] (Core with Stag Knight)
    - **Team 2:** Mithrala + Brogni + Stag Knight + [2 highest damage] (Keep Brogni survivability)
    - **Team 3:** Mithrala + Aniri + Stag Knight + [2 highest damage] (Keep Aniri buff extension)
    - **Team 4:** Mithrala + Stag Knight + Nogdar + [2 DPS] (Ally Attack spam)
    - **Team 5:** Mithrala + Stag Knight + Skullcrusher + [2 DPS] (Counterattack doubling)
    - **Team 6:** Full poison team (Mithrala + Stag Knight + Fayne + Venomage + Frozen Banshee)
    - **Team 7-8:** Alternative compositions based on Phase E findings
  
  * **Expected Damage Target:** 150M-180M+ (stretch goal with optimized high-damage team)

- **Validation Requirements:**
  * Validate Stag Knight aura: "24% SPD in Dungeons" vs "24% SPD in all Battles"
  * Validate all high-damage champion mechanics (passives, multipliers, proc rates)
  * Cross-check with UNM_Champion_Comparison_Prompt.md for detailed analysis
  * Document affinity safety for all new compositions

- **Output:** Updated UNM_Team_Optimization_DRAFT.md with:
  * Phase A-F analysis and findings
  * Top 5-8 team compositions with damage estimates
  * Final recommendation: Best team for 150M+ damage goal
  * Implementation guide for recommended team

---

### **Batch 1: Sand Devil & Fire Knight (HIGH PRIORITY)**

**Boss 1: Sand Devil (Doom Tower)**
- **Files to Update:**
  * `Notes/SandDevil_DoomTower_Normal_Boss_Guide_DRAFT.md` (if exists, update FIRST)
  * `Notes/SandDevil_DoomTower_Hard_Boss_Guide_DRAFT.md` (update SECOND)
- **Priority:** HIGH (user content priority #2: Doom Tower Hard)
- **Focus:**
  * Validate auras for all recommended champions
  * Validate passive mechanics (HP Burn, Reflect Damage, Shields)
  * Document affinity safety (Sand Devil affinity: Spirit)
  * Add Executive Summary + Implementation Guide

**Boss 2: Fire Knight (Hard)**
- **Files to Update:**
  * `Notes/FireKnight_Hard_Team_Notes_FINAL.md`
- **Priority:** HIGH (user content priority #2: Dungeons All Stages 25)
- **Focus:**
  * Validate auras for all recommended champions
  * Validate passive mechanics (Counterattack, Ally Attack, Turn Meter manipulation)
  * Document affinity safety (Fire Knight affinity: Magic)
  * Add Executive Summary + Implementation Guide
  * **User preference:** HP Burn teams (well-built), Poison teams (NOT well-built)

---

### **Batch 2: Dragon & Spider (HIGH PRIORITY)**

**Boss 3: Dragon (Hard)**
- **Files to Update:**
  * `Notes/Dragon_Hard_Team_Notes_FINAL.md`
- **Priority:** HIGH (user content priority #2: Dungeons All Stages 25)
- **Focus:**
  * Validate auras for all recommended champions
  * Validate passive mechanics (HP Burn, Poison, Decrease DEF)
  * Document affinity safety (Dragon affinity: Magic)
  * Add Executive Summary + Implementation Guide
  * **User preference:** HP Burn teams (well-built)

**Boss 4: Spider (Hard)**
- **Files to Update:**
  * `Notes/Spider_Hard_Team_Notes_FINAL.md`
- **Priority:** HIGH (user content priority #2: Dungeons All Stages 25, user confirmed strong Spider team)
- **Focus:**
  * Validate auras for all recommended champions
  * Validate passive mechanics (HP Burn, Enemy MAX HP damage, Turn Meter manipulation)
  * Document affinity safety (Spider affinity: Spirit)
  * Add Executive Summary + Implementation Guide
  * **User preference:** HP Burn teams (well-built)

---

### **Batch 3: Ice Golem & Iron Twins (MEDIUM PRIORITY)**

**Boss 5: Ice Golem (Hard)**
- **Files to Update:**
  * `Notes/IceGolem_Hard_Team_Notes_FINAL.md`
- **Priority:** MEDIUM (user content priority #2: Dungeons All Stages 25)
- **Focus:**
  * Validate auras for all recommended champions
  * Validate passive mechanics (Block Buffs, Decrease ACC, HP Burn)
  * Document affinity safety (Ice Golem affinity: Force)
  * Add Executive Summary + Implementation Guide

**Boss 6: Iron Twins (DRAFT → FINAL)**
- **Files to Update:**
  * `Notes/IronTwins_Team_Notes_DRAFT.md` → `Notes/IronTwins_Team_Notes_FINAL.md`
- **Priority:** MEDIUM (user content priority #3: Advanced PVE Content)
- **Focus:**
  * Complete DRAFT guide (if incomplete)
  * Validate auras for all recommended champions
  * Validate passive mechanics (Decrease DEF, Ally Attack, Shields)
  * Document affinity safety (Iron Twins affinities: varies by boss)
  * Add Executive Summary + Implementation Guide
  * Promote DRAFT → FINAL after validation

---

### **Batch 4: Hydra, Chimera, Shredder (LOWER PRIORITY)**

**Boss 7: Hydra (Clan Boss)**
- **Files to Update:**
  * `Notes/Hydra_ClanBoss_Team_Notes_FINAL.md`
- **Priority:** LOWER (user content priority #3: Advanced PVE Content)
- **Focus:**
  * Validate auras for all recommended champions
  * Validate passive mechanics (complex multi-head mechanics)
  * Document affinity safety (Hydra heads: multiple affinities)
  * Add Executive Summary + Implementation Guide

**Boss 8: Chimera (Clan Boss)**
- **Files to Update:**
  * `Notes/Chimera_Boss_Team_Notes_FINAL.md`
- **Priority:** LOWER (user content priority #3: Advanced PVE Content)
- **Focus:**
  * Validate auras for all recommended champions
  * Validate passive mechanics (form changes, damage mitigation)
  * Document affinity safety (Chimera affinity: varies by form)
  * Add Executive Summary + Implementation Guide

**Boss 9: Shredder (DRAFT)**
- **Files to Update:**
  * `Notes/Shredder_Team_Notes_DRAFT.md`
- **Priority:** LOWER (user content priority #3: Advanced PVE Content)
- **Focus:**
  * Complete DRAFT guide (if incomplete)
  * Validate auras for all recommended champions
  * Validate passive mechanics
  * Document affinity safety
  * Add Executive Summary + Implementation Guide
  * Promote DRAFT → FINAL after validation

---

### **Batch 5: Cursed City Amius (LOWEST PRIORITY)**

**Boss 10: Amius (Cursed City)**
- **Files to Update:**
  * `Notes/Amius_CursedCity_Boss_Guide_DRAFT.md`
- **Priority:** LOWEST (user content priority #3: Advanced PVE Content)
- **Focus:**
  * Complete DRAFT guide (if incomplete)
  * Validate auras for all recommended champions
  * Validate passive mechanics
  * Document affinity safety
  * Add Executive Summary + Implementation Guide
  * Promote DRAFT → FINAL after validation

---

## 5. VALIDATION CHECKLIST (PER BOSS)

### **For Each Boss, Complete the Following:**

**Pre-Update Assessment:**
- [ ] Read existing guide (Normal or Hard, whichever exists first)
- [ ] List all recommended champions in guide
- [ ] Verify all champions in owned champion list
- [ ] Identify auras mentioned in guide
- [ ] Identify passive skills mentioned in guide

**Aura Validation:**
- [ ] Fetch Ayumilove pages for all champions with auras
- [ ] Document exact aura wording ("in the Arena", "in Dungeons", "in all Battles")
- [ ] Create aura validation table
- [ ] Flag any Arena-only or Dungeon-only auras as errors (if applied to wrong content)
- [ ] Update recommendations if aura errors found

**Passive Skill Validation:**
- [ ] Fetch Ayumilove pages for champions with passive damage/reflect/proc mechanics
- [ ] Check for Patch 4.40, 4.70, or other patch notes
- [ ] Document mastery recommendations (Warmaster vs Giant Slayer)
- [ ] Create passive validation table
- [ ] Update damage estimates if passive errors found

**Affinity Safety Analysis:**
- [ ] Document boss affinity
- [ ] Create affinity safety table for all recommended champions
- [ ] Add multi-line affinity notes to ALL team recommendations
- [ ] Flag high-risk teams (2+ champions with weak affinity)

**Champion Ranking Update:**
- [ ] Re-rank champions based on validated mechanics
- [ ] Adjust damage/clear time estimates
- [ ] Create Top 3-5 recommendations table
- [ ] Document backup champions (Top 6-8)

**Executive Summary Creation:**
- [ ] Add Executive Summary section at top of guide
- [ ] Include Top 3-5 recommendations (quick reference table)
- [ ] Include critical validation findings
- [ ] Include user goal priority pick
- [ ] Include expected clear times/damage

**Implementation Guide Addition:**
- [ ] For Top 3 champions, add detailed build guides
- [ ] Include gear requirements (sets, stats, priorities)
- [ ] Include masteries (Tier 6 choice, key masteries)
- [ ] Include skill books (priority order)
- [ ] Include speed tuning (if applicable)
- [ ] Include testing checklist

**Final Validation:**
- [ ] Update Table of Contents
- [ ] Run document checklist (auras, passives, affinity, summary, implementation)
- [ ] Cite validation sources (Ayumilove, HellHades, RaidHQ)
- [ ] Mark guide as "VALIDATED" with date
- [ ] Commit changes with detailed message

---

## 6. CRITICAL VALIDATION REQUIREMENTS

### **Aura Validation (MANDATORY)**

**For EVERY champion with an aura mentioned in guide:**

1. **Fetch Ayumilove page** for champion
2. **Document exact aura wording:**
   - "Increases Ally [STAT] in **the Arena** by X%" = **Arena-only** ❌ Does NOT apply to Dungeons/Clan Boss/Doom Tower
   - "Increases Ally [STAT] in **Dungeons** by X%" = **Dungeon-only** ❌ Does NOT apply to Arena/Clan Boss/Doom Tower
   - "Increases Ally [STAT] in **all Battles** by X%" = **All Battles** ✅ Applies to ALL content
3. **Create aura validation table:**
   ```markdown
   | Champion | Aura | Content Applicability | Applies to [Boss Name]? |
   |----------|------|----------------------|-------------------------|
   | Arbiter | +30% SPD in the Arena | Arena-only | ❌ NO |
   | Tagoar | +33% DEF in all Battles | All Battles | ✅ YES |
   ```
4. **Update recommendations if errors found:**
   - Remove champions with non-applicable auras from top recommendations
   - Re-rank champions based on corrected aura benefits
   - Document aura error in Executive Summary

---

### **Passive Skill Validation (MANDATORY)**

**For EVERY champion with passive damage/reflect/proc mechanics:**

1. **Fetch Ayumilove page** for champion
2. **Check for patch notes:** Patch 4.40 (Brogni), Patch 4.70 (Geomancer), or other relevant patches
3. **Document passive classification:**
   - "Damage Reflect" = NO Warmaster/Giant Slayer procs (e.g., Geomancer post-Patch 4.70)
   - "Shield Damage Reflect" = YES Giant Slayer procs, NO Warmaster procs (e.g., Brogni post-Patch 4.40)
   - "Passive Damage" = Depends on wording (check if procs masteries/sets)
4. **Document optimal mastery:**
   - Warmaster vs Giant Slayer choice
   - Rationale based on skill mechanics
5. **Create passive validation table:**
   ```markdown
   | Champion | Passive Type | Patch Changes | Warmaster/GS? | Expected Damage |
   |----------|--------------|---------------|---------------|-----------------|
   | Geomancer | Damage Reflect | Patch 4.70: NO mastery procs | Warmaster (A1/A3) | 15-20M |
   | Brogni | Shield Damage Reflect | Patch 4.40: YES GS procs | Giant Slayer | 15-25M |
   ```
6. **Update damage estimates if errors found:**
   - Adjust champion damage estimates based on validated passive mechanics
   - Re-rank champions if damage estimates change significantly

---

### **Affinity Safety Documentation (MANDATORY)**

**For EVERY team recommendation:**

1. **Document boss affinity** (Magic, Force, Spirit, Void)
2. **For each champion in team, document affinity:**
   - Magic → Strong vs Spirit, Weak vs Force
   - Force → Strong vs Magic, Weak vs Spirit
   - Spirit → Strong vs Force, Weak vs Magic
   - Void → Neutral vs all affinities
3. **Add multi-line affinity safety notes:**
   ```markdown
   **Affinity Safety/Risk:**
   - Champion A (Magic): Safe vs Spirit boss, strong affinity
   - Champion B (Force): Risky vs Magic boss, may miss debuffs (60% weak hit rate)
   - Champion C (Void): Safe, neutral affinity
   - Overall: Medium risk, 1 champion has weak affinity in debuffer role
   ```
4. **Flag high-risk teams:**
   - 2+ champions with weak affinity = HIGH RISK
   - Weak affinity in critical debuffer role = HIGH RISK
   - Document backup options with better affinity

---

### **Source Citation (MANDATORY)**

**For ALL validations, cite sources:**

1. **Ayumilove:** Champion pages for skills, auras, masteries, patch notes
2. **HellHades:** Team compositions, tier lists, gear recommendations
3. **RaidHQ:** Boss mechanics, trial requirements, stat thresholds
4. **In-game testing:** User-provided simulation results, clear times, success rates

**Citation Format:**
```markdown
**Validation Sources:**
- Ayumilove Geomancer page: "Patch 4.70: Stoneguard passive adjusted, reflected damage no longer triggers Giant Slayer/Warmaster"
- HellHades tier list: Geomancer ranked S-tier for Clan Boss
- User testing: 3 runs, 15M-20M damage average
```

---

## 7. OUTPUT STANDARDS

### **Required Sections for All Updated Guides:**

**1. Executive Summary (NEW - Add at top)**
- Top 3-5 champion recommendations (quick reference table)
- Critical validation findings (aura errors, passive changes)
- User goal priority pick (fastest clear, safest, easiest to gear)
- Expected clear times/damage for each difficulty

**2. Table of Contents (UPDATE)**
- Add Executive Summary section
- Add Implementation Guide section
- Update section numbers/anchors

**3. Boss Mechanics & Stat Requirements (EXISTING - Validate)**
- Cross-validate with RaidHQ, Ayumilove, HellHades
- Document boss affinity
- Document trial requirements (if applicable)

**4. Champion Ranking & Recommendations (EXISTING - Update)**
- Re-rank based on validated mechanics
- Adjust damage/clear time estimates
- Add affinity safety column to all tables

**5. Detailed Team Sections (EXISTING - Update)**
- Add multi-line affinity safety notes to ALL teams
- Update damage estimates based on validated passives
- Add expected clear times/success rates

**6. Aura Validation Section (NEW - Add)**
- Aura validation table for all recommended champions
- Document any aura errors found
- Update recommendations if errors impact rankings

**7. Passive Mechanics Validation Section (NEW - Add)**
- Passive validation table for all champions with passive damage/reflect/proc mechanics
- Document patch changes (4.40, 4.70, etc.)
- Update damage estimates if errors found

**8. Implementation Guide (NEW - Add)**
- For Top 3 champions, add detailed build guides:
  * Gear requirements (sets, stats, priorities)
  * Masteries (Tier 6 choice, key masteries)
  * Skill books (priority order)
  * Speed tuning (if applicable)
  * Testing checklist

**9. Validation & Simulation Notes (EXISTING - Update)**
- Number of simulations/test runs performed
- Clear time methodology (average, fastest, manual/auto)
- Affinity safety/risk observations
- Data sources (Ayumilove, HellHades, RaidHQ, in-game testing)

---

### **File Naming Standards:**

**DRAFT Files:**
- `[Boss_Name]_[Difficulty]_Boss_Guide_DRAFT.md`
- Example: `SandDevil_DoomTower_Hard_Boss_Guide_DRAFT.md`

**FINAL Files (After Validation):**
- `[Boss_Name]_[Difficulty]_Team_Notes_FINAL.md`
- Example: `SandDevil_DoomTower_Hard_Team_Notes_FINAL.md`

**Promotion Workflow:**
- Complete all validations in DRAFT file
- Run validation checklist
- User review & approval
- Rename DRAFT → FINAL
- Archive old FINAL (if exists) with date suffix: `_OLD_2025-10-19.md`

---

### **Commit Message Standards:**

```
Update [Boss] guide with comprehensive validation

- Added Executive Summary with Top 3-5 recommendations
- Section X: Aura validation - [Champion] aura is [Arena/Dungeon]-only (ERROR CORRECTED)
- Section Y: Passive mechanics validation - [Champion] passive [does/does not] proc Warmaster/Giant Slayer
- Updated all team recommendations with affinity safety/risk analysis
- Re-ranked champions based on validated mechanics
- Added Implementation Guide for Top 3 champions (gear/masteries/books)
- Expected clear times: [Normal: X, Hard: Y]
- Validation sources: Ayumilove, HellHades, RaidHQ, in-game testing
```

---

## 8. QUESTIONS FOR USER

### **Priority & Scope Questions:**

**Q1: Batch Approach Confirmation**
- **Question:** Should we process bosses in batches of 2 (as outlined), or would you prefer a different batch size (1 boss at a time, 3+ bosses per batch)?
- Batch one at a time, and break out by section of the guide as it exists, returning to prior sections with updates a required ex best damage teams. Output to the DRAFT file and review as possible to optimize processing on later sections. 

**Q2: Difficulty Order Preference**
- **Question:** For bosses with both Normal and Hard guides (e.g., Sand Devil), should we ALWAYS update Normal first, or only if Normal already exists?
- Yes. And Queue the HARD after every other boss is run.

**Q3: DRAFT-to-FINAL Promotion**
- **Question:** Should we auto-promote DRAFT → FINAL after validation is complete, or always wait for your explicit approval before renaming?
- Wait for confirmation, but do this as a cleanup after all files are set, and when exiting. 

---

### **Validation Requirements Questions:**

**Q4: Aura Validation Depth**
- **Question:** Should we validate auras for ALL champions mentioned in guides (including backup/alternative options), or only Top 8-10 primary recommendations?
- All heroes. Validate champion data at least one time vs online sources, even if there is a champion review for that champion.

**Q5: Passive Mechanics Validation Scope**
- **Question:** Should we validate passive mechanics for ALL champions with passives (including generic passives like "heal when attacked"), or only champions with damage/reflect/proc passives (Geomancer, Brogni, etc.)?
- All, especially for synergy with the team or archetype.

**Q6: Simulation Requirements**
- **Question:** Do you want us to run NEW simulations/test runs for each boss (minimum 3 runs per team), or can we use existing simulation results from guides and only re-validate the damage estimates?
- Yes. A Lot of the existing data is out of date.

---

### **User Preference Questions:**

**Q7: Content Priority Confirmation**
- **Question:** Confirm content priority order:
  1. Clan Boss UNM (COMPLETE ✅)
  2. Doom Tower Hard ( other DT bosses)
  3. Advanced PVE (Iron Twins, Hydra, Chimera, Shredder, Amius)
  4. Dungeons All Stages 25 ( Fire Knight, Dragon, Spider, Ice Golem)
  5. Sand Devil and Pahntom Shogun Hard

**Q8: HP Burn vs Poison Team Preference**
- **Question:** You mentioned "HP Burn teams (well-built), Poison teams (NOT well-built)". Should we prioritize HP Burn champions in ALL dungeon guides, or only for specific bosses (Dragon, Spider, Fire Knight)?
- Use poison when maximally effective, but prefer hp burn and surviving or activating if it makes sense for the boss.

**Q9: Team Composition Preference**
- **Question:** For bosses with multiple team archetypes (e.g., Fire Knight: TM control vs Ally Attack vs Counterattack), should we recommend based on:
  - 1. Highest success rate (consistency priority)
  - 2. Fastest clear time (speed farming priority)
  - 3. Easiest to book/etc and gear (accessibility priority)

---

### **Output Format Questions:**

**Q10: Executive Summary Placement**
- **Question:** Should Executive Summary always be at the TOP of the guide (before Table of Contents), or after TOC?
- After TOC, and update before completing the guide.

**Q11: Implementation Guide Depth**
- **Question:** For Implementation Guides, provide:
  - Basic guidance (gear sets, mastery tier 6, book priority) - CONCISE

**Q12: Affinity Safety Documentation**
- **Question:** Affinity safety notes should appear in:
  - Executive Summary + team tables + detailed sections (maximum visibility)
- **Reason:** Placement affects how often users see affinity warnings

---

### **Workflow Questions:**

**Q13: Git Workflow**
- Commit after each boss update (12 commits). 

**Q14: Chat Review Process**
  - Update guide files directly and present summary of changes in chat AFTER update (faster, less iterative)

**Q15: Error Handling**
- **Question:** If we discover CRITICAL errors in a guide (e.g., champion not in owned list, major damage estimate error), should we:
  - Rebuild that section using template or the existing section. Use current validated data and analysis/testing/simulation and guidance.
---

## 📋 READY TO START

**Once questions are answered:**
1. Prioritize boss queue based on user responses
2. Begin Batch 1: Sand Devil (Normal → Hard) + Fire Knight (Hard)
3. Apply UNM validation methodology to each boss
4. Present validation findings in chat for approval
5. Update guide files with comprehensive validations
6. Commit changes with detailed message
7. Move to Batch 2

**Estimated Time per Boss:** 30-60 minutes (depending on validation depth and guide complexity)

**Estimated Total Project Time:** 8-12 bosses × 45 minutes average = **6-9 hours** (spread across multiple sessions)

---

## 9. CLARIFYING QUESTIONS (ANSWERED REQUIRED)

### **Workflow & Processing Questions:**

**Q16: Section-by-Section Processing Clarification**
  - Do A: Process sections 1-9 sequentially, updating DRAFT file after each section, and circle back to update earlier sections (e.g., Executive Summary, Team Rankings) once validation is complete?

**Q17: "Review as Possible to Optimize Processing" Clarification**
 Complete the entire guide update, then present summary at the end for optimization feedback?

---

### **Content Priority Questions:**

**Q18: Updated Priority Queue Confirmation**
- **Order of Bosses:**
  0. **UNM Clan Boss (CURRENT - IN PROGRESS):** Continue optimization with Stag Knight core + Geo/Brogni/Aniri replacement exploration for maximum damage
  1. Sand Devil Normal, Phantom Shogun Normal (if exists)
  2. Fire Knight, Dragon, Spider, Ice Golem (Dungeons Hard)
  3. Iron Twins, Hydra, Chimera, Shredder, Amius (Advanced PVE)
  4. Sand Devil Hard, Phantom Shogun Hard (Queue after all other bosses)
  5. Other Doom Tower Hard bosses


---

### **Simulation & Testing Questions:**

**Q19: "NEW Simulations" Clarification**
- For NEW simulations:
  - **Step 1:** Use community calculators/simulators (HellHades optimizer, Deadwood Jedi speed calculator) and document methodology AND THEN to double check:
  - **Step 2:** Estimate based on validated mechanics (aura, passive, affinity) and document conservative estimates with rationale

**Q20: Testing Workflow**
- For each boss, Update guide with validated mechanics and estimated damage/clear times, THEN you test in-game and provide actual results to refine estimates?

---

### **DRAFT File & Existing Guides Questions:**

**Q21: Existing FINAL Files**
- Create new `_DRAFT.md` file for updates, leaving FINAL unchanged until promotion?
**Q22: Section Rebuild vs. Update**
  - If there are validation/etc errors, rebuild section from scratch using reference templates/guides in this project

---

### **Team Composition Ranking Questions:**

**Q23: Team Archetype Priority Order**
- You ranked:
  1. Highest success rate (consistency)
  2. Fastest clear time (speed farming)
  3. Easiest to book/gear (accessibility)

**Question:** When presenting Top 3-5 teams, should the ranking order be:
- Provide separate rankings for each category (like UNM: "Most Users", "Damage-Focused", "New Players")

---

### **HP Burn vs. Poison Strategy Questions:**

**Q24: "Maximally Effective" Poison Clarification**
- You said "Use poison when maximally effective, but prefer hp burn"
- **Question:** "Maximally effective" poison means:
  - **Option A:** Boss has high HP pool and takes full poison damage (e.g., Clan Boss, high HP dungeon bosses)
  - **Option B:** User has well-built poison champions for that specific boss
  - **Option C:** Poison outperforms HP Burn in clear time/damage for that boss
  - All of the above, in that priority order

**Q25: "Surviving or Activating" HP Burn Clarification**
- You said "prefer hp burn and surviving or activating if it makes sense for the boss"
- **Question:** Does this mean:
  - HP Burn is preferred IF team can survive long enough for HP Burn to deal meaningful damage (multi-turn bosses)?
  - OR HP Burn is preferred IF HP Burn can be activated/maintained consistently (not cleansed/resisted)?
  - BOTH

---

### **Git Commit & File Cleanup Questions:**

**Q26: Commit Message for Section-by-Section Updates**
- You said "Commit after each boss update"
- **Question:** If I update a boss guide in multiple passes (e.g., Aura Validation → Passive Validation → Executive Summary), should I:
  - Commit only when entire boss guide is complete (1 commit per boss)

**Q27: DRAFT-to-FINAL Cleanup Timing**
- Leave all files as draft until all bosses are complete, or if moving to another task. This prompt file will can be re-used.

---

## 📋 SUMMARY OF CLARIFICATIONS NEEDED

**Critical for Workflow:**
- Q16: Section-by-section (Option A) or full-pass (Option B)?
- Q17: Pause after each section or present summary at end?
- Q18: **MOST IMPORTANT** - Final boss priority queue (Option A, B, or C)?
- Q19: Simulation method (in-game, calculators, or estimates)?
- Q21: DRAFT file creation approach

**Important for Quality:**
- Q20: Testing workflow (estimate first, or test first?)
- Q22: Section rebuild vs. update for errors
- Q23: Team ranking format (priority order or separate categories?)
- Q24-Q25: HP Burn vs. Poison strategy definitions

**Process Details:**
- Q26: Commit frequency per boss
- Q27: DRAFT-to-FINAL promotion timing

---

**END OF PROMPT** ✅

**Next Action:** User answers Q16-Q27 → Agent begins first boss guide update with finalized workflow
