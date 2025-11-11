# UNM Clan Boss - Champion Detail Reference

**Date**: 2025-11-07  
**Version**: 1.0  
**Status**: DRAFT - Ready for Current Stats Input  
**Purpose**: Comprehensive champion analysis for 2:1 speed tune UNM Clan Boss team building

---

## Table of Contents

**CORE TEAM:**
- [Ninja - HP Burn Activation Specialist](#-ninja---hp-burn-activation-specialist)
- [Rector Drath - Revive/Cleanse/Block Debuffs Specialist](#-rector-drath---revivecleanseblock-debuffs-specialist)
- [Underpriest Brogni - Shield/Reflect/Cleanser](#-underpriest-brogni---shieldreflectcleanser)
- [Mithrala Lifebane - DEF Support/Debuffer/Cleanser](#-mithrala-lifebane---def-supportdebuffercleanser)
- [Stag Knight - Decrease DEF/ATK Specialist](#-stag-knight---decrease-defatk-specialist)
- [Godseeker Aniri - Revive/Heal/Buffer](#-godseeker-aniri---revivehealbuffer)

**FUTURE TEAM:**
- [Leonardo - Unkillable/Counterattack Specialist](#-leonardo---unkillablecounteattack-specialist)
- [Michelangelo - Debuff Spread/Hybrid Control](#-michelangelo---debuff-spreadhybrid-control)

**ALTERNATES:**
- [Bad-el-Kazar - Sustain/Poison Specialist](#-bad-el-kazar---sustainpoison-specialist)
- [Geomancer - HP Burn Reflect/Passive Damage](#-geomancer---hp-burn-reflectpassive-damage)
- [Tayrel - Decrease DEF/ATK Alternative](#-tayrel---decrease-defatk-alternative)

---

## CORE TEAM CHAMPIONS

### **🎯 NINJA - HP Burn Activation Specialist** ⭐⭐⭐ **HIGH PRIORITY**

**Role:** Attack / HP Burn / Decrease DEF  
**Why Consider:** **10/10 Clan Boss rating** - HP Burn activation on A3 (75k × multiple turns = MASSIVE damage), Decrease DEF 60% backup, cooldown reset passive when boss under HP Burn + Freeze.

**Base Stats:** HP 16,845 | ATK 1,509 | DEF 947 | SPD 110 | C.RATE 15% | C.DMG 50% | RES 30 | ACC 0

**Key Mechanics:** (from `Ninja.json`)
- **A1 - Hailburn**: 3-hit attack, 30% chance Decrease DEF 60% (2 turns) per hit (Giant Slayer synergy)
- **A2 - Frozen Reflections**: AOE Freeze (1 turn, useless vs UNM immune) + self Increase ATK 50% + Increase C.RATE 30%
- **A3 - Arctic Rampage**: **HP Burn activation** (detonates existing HP Burn for instant 75k damage) + places new HP Burn (2 turns)
- **Passive - Hailburn Mastery**: **Cooldown reset** A3 when boss has HP Burn + Freeze (situational in CB, requires Freeze to land)

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - Giant Slayer T6 recommended]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ⚠️ MODERATE  
**Auto vs Manual Damage:** ~18-25% difference  
**Build Gaps:** [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐⭐ HIGH

**2:1 Viability:** ⭐⭐⭐ **EXCELLENT** - Base SPD 110, needs +153-170 SPD (achievable with SPD boots + Speed set)

**Meta Ratings:** **Clan Boss 10/10** (best-in-class HP Burn champion), Dungeons 10/10, Doom Tower 9/10

---

### **🎯 RECTOR DRATH - Revive/Cleanse/Block Debuffs Specialist** ⭐⭐⭐ **HIGH PRIORITY**

**Role:** Support / Team Revive / Cleanse / Block Debuffs  
**Why Consider:** **Survivability enabler** - Block Debuffs prevents boss Decrease SPD (maintains speed tune), Team Revive (safety net), Cleanse (removes existing debuffs). Extends team survival 10-15 turns.

**Base Stats:** HP 17,010 | ATK 1,035 | DEF 1,134 | SPD 109 | C.RATE 15% | C.DMG 50% | RES 30 | ACC 0

**Key Mechanics:** (from `Rector_Drath.json`)
- **A1 - Smite**: Single target heal (weakest ally, scales with caster HP) + 50% chance Decrease SPD 1 turn
- **A2 - Sacred Renewal**: **Cleanse all debuffs** + **Block Debuffs 2 turns** (prevents boss Decrease SPD) | Cooldown: 4 turns (booked)
- **A3 - Divine Intervention**: **Team Revive** 50% HP + Increase DEF 60% (2 turns) | Cooldown: 6 turns (booked)
- **Passive - Mercy**: Heals all allies 10% HP when ally drops below 25% HP (once per turn)

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - Warmaster T6 recommended]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ✅ GOOD  
**Auto vs Manual Damage:** ~8-10% difference  
**Build Gaps:** [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐⭐ HIGH

**2:1 Viability:** ⭐⭐⭐ **EXCELLENT** - Base SPD 109, needs +154-171 SPD (achievable with SPD boots + Speed set)

**Meta Ratings:** Clan Boss 7/10 (Block Debuffs utility), Dungeons 9/10, Faction Wars 9/10

---

### **🎯 UNDERPRIEST BROGNI - Shield/Reflect/Cleanser** ⭐⭐⭐ **HIGH PRIORITY**

**Role:** Support / Shield / Cleanser / Passive Damage  
**Why Consider:** **10/10 all content** - Unremovable shield, passive reflects 25% damage + heals allies, synergizes with Mithrala/Leonardo shields for massive team-wide benefits.

**Base Stats:** HP 22,965 | ATK 782 | DEF 1,266 | SPD 100 | C.RATE 15% | C.DMG 50% | RES 90 | ACC 0

**Key Mechanics:** (from `Underpriest_Brogni.json`)
- **A1 - Deepcrystal Scourge**: Single target, 45% chance HP Burn (2 turns, 60% booked)
- **A2 - Cavern's Grasp**: AOE, 75% chance remove 1 buff from enemies + 1 debuff from allies (100% booked), increases Shield value by 30% of damage dealt | Cooldown: 4 turns (3 booked)
- **A3 - Resilient Glow**: **Block Debuffs + Increase ATK 50% + Unremovable Shield 30% MAX HP** on all allies (2 turns) | Cooldown: 5 turns (3 booked)
- **Passive - Redoubt**: Allies under Shield reflect 25% damage to attacker + heal 25% of damage taken. Triggers Warmaster/Giant Slayer on reflect!

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - Warmaster T6 recommended for passive procs]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ✅ EXCELLENT  
**Auto vs Manual Damage:** ~5-8% difference  
**Build Gaps:** [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐⭐ HIGH

**2:1 Viability:** ⭐⭐⭐ **EXCELLENT** - Base SPD 100, needs +163-180 SPD (achievable with SPD boots + Speed set)

**Meta Ratings:** **Clan Boss 10/10**, Dungeons 10/10, Doom Tower 10/10, Arena 9/10, Faction Wars 10/10

---

### **🎯 MITHRALA LIFEBANE - DEF Support/Debuffer/Cleanser** ⭐⭐⭐ **HIGH PRIORITY**

**Role:** Support / Debuffer / Cleanser / Shield  
**Why Consider:** **10/10 all content** - DEF-scaling, Shield 30% MAX HP, unique Passive (RES = RES + ACC), Hex debuff, cleanse + buffs. Synergizes with Brogni shields.

**Base Stats:** HP 20,310 | ATK 870 | DEF 1,354 | SPD 105 | C.RATE 15% | C.DMG 50% | RES 30 | ACC 10

**Key Mechanics:** (from `Mithrala_Lifebane.json`)
- **A1 - Libation of Pain**: 2-hit random attack (DEF scaling 2.0 per hit), 80% chance Poison 5% (2 turns) per hit (100% booked)
- **A2 - Sigil of Toxic Glory**: AOE (DEF scaling 4.0), Hex (2 turns) + Increase DEF 60% + Increase ATK 50% on all allies (2 turns) | Cooldown: 5 turns (3 booked)
- **A3 - Brimming Cylix**: **Cleanse all debuffs** + Strengthen 25% + **Shield 30% MAX HP** on all allies (2 turns) | Cooldown: 5 turns (3 booked)
- **Passive - Gaze of Stone**: 50% chance Petrification (1 turn) when attacked by Hexed enemy (30% for allies). **RES = RES + ACC** (unique mechanic!)

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - Warmaster T6 recommended]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ✅ GOOD  
**Auto vs Manual Damage:** ~8-10% difference  
**Build Gaps:** [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐⭐ HIGH

**2:1 Viability:** ⭐⭐ **GOOD** - Base SPD 105, needs +158-175 SPD (achievable with SPD boots + Speed set + good substats)

**Meta Ratings:** **Clan Boss 10/10**, Dungeons 10/10, Doom Tower 10/10, Arena 10/10, Faction Wars 10/10

---

### **🎯 STAG KNIGHT - Decrease DEF/ATK Specialist** ⭐⭐⭐ **HIGH PRIORITY**

**Role:** Support / Decrease DEF + ATK / Debuffer  
**Why Consider:** **9/10 Clan Boss** - AOE Decrease DEF 60% + Decrease ATK 50% on A2 (core debuffs for team damage + survivability). High base stats for Epic, auto-friendly.

**Base Stats:** HP 20,970 | ATK 859 | DEF 1,046 | SPD 107 | C.RATE 15% | C.DMG 50% | RES 30 | ACC 0

**Key Mechanics:** (from `Stag_Knight.json`)
- **A1 - Spot Quarry**: 2-hit attack (ATK scaling 4.0 per hit), 30% chance Decrease SPD 30% (2 turns) per hit (50% booked) - **WASTED ON CB (immune)**
- **A2 - Huntmaster**: **AOE Decrease DEF 60% + Decrease ATK 50%** (2 turns, 70% base chance → 90% booked) | Cooldown: 4 turns (3 booked)
- **A3 - Debuff Spread**: Takes debuffs from target and spreads to all enemies | Cooldown: 5 turns (4 booked)
- **Passive - Marked Prey**: Extra turn on kill (useless in CB, great for waves)

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - Warmaster T6 recommended]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ✅ EXCELLENT  
**Auto vs Manual Damage:** ~5-7% difference  
**Build Gaps:** [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐⭐ HIGH

**2:1 Viability:** ⭐⭐⭐ **EXCELLENT** - Base SPD 107, needs +156-173 SPD (achievable with SPD boots + Speed set)

**Meta Ratings:** **Clan Boss 9/10**, Dungeons 10/10, Doom Tower 10/10, Arena 9/10, Faction Wars 10/10

---

### **🎯 GODSEEKER ANIRI - Revive/Heal/Buffer** ⭐⭐ **MEDIUM PRIORITY**

**Role:** Support / Reviver / Healer / Buffer  
**Why Consider:** **Survivability backup** - Team revive, buff extension, Regeneration set synergy, Miracle Heal blessing synergy. Low base SPD makes 2:1 challenging.

**Base Stats:** HP # | ATK # | DEF # | SPD 98 | C.RATE 15% | C.DMG 50% | RES # | ACC 0  
*(Note: Full stats needed from user or JSON)*

**Key Mechanics:** (estimated from role, JSON confirmation needed)
- **A1**: Likely single target heal or buff
- **A2**: **Buff Extension** (extends ally buffs, timing critical for Block Debuffs/Shields)
- **A3**: **Team Revive** + heal
- **Passive**: Likely healing or survivability mechanic

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - Warmaster T6 recommended]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ✅ GOOD  
**Auto vs Manual Damage:** ~8-12% difference  
**Build Gaps:** [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐ MEDIUM

**2:1 Viability:** ⭐ **DIFFICULT** - Base SPD 98, needs +165-182 SPD (requires god-tier substats + SPD boots + Speed set)

**Meta Ratings:** Clan Boss 8/10 (estimated), Dungeons 9/10, Faction Wars 9/10

---

## FUTURE TEAM CHAMPIONS

### **🎯 LEONARDO - Unkillable/Counterattack Specialist** ⭐⭐⭐ **HIGH PRIORITY (FUTURE)**

**Role:** Defense / Unkillable / Counterattack / Ally Protection  
**Why Consider:** **10/10 Clan Boss** - Self Unkillable + Counterattack (2 turns), Ally Protection on all allies, DEF-scaling damage with DEF ignore buff stacking. Cheese team viable.

**Base Stats:** HP 16,845 | ATK 782 | DEF 1,619 | SPD 101 | C.RATE 15% | C.DMG 63% | RES 15 | ACC 0

**Key Mechanics:** (from `Leonardo.json`)
- **A1 - New York Slice**: 2-hit attack (DEF scaling 1.7 per hit), ignores 3% DEF per buff on self (max 15% at 5 buffs). **On counterattack, repeats attack vs random enemy (4 total hits!)**
- **A2 - Shell Yeah!**: **Increase DEF 60% + Ally Protection 50%** on all allies (2 turns) + **Unkillable + Counterattack** on self (2 turns) | Cooldown: 5 turns (4 booked) - **CORE SKILL**
- **A3 - Ninjutsu Mastery**: AOE (DEF scaling 4.0), removes buffs, Decrease DEF 60% (2 turns, 75% chance → 100% booked) | Cooldown: 5 turns (4 booked)
- **Passive**: Likely TMNT synergy or DEF-based mechanic

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - Warmaster T6 recommended]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ⚠️ MODERATE  
**Auto vs Manual Damage:** ~12-18% difference (buff stacking requires manual optimization)  
**Build Gaps:** **NEEDS 7 Legendary books** | [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐⭐ HIGH (FUTURE)

**2:1 Viability:** ⭐⭐⭐ **EXCELLENT** - Base SPD 101, needs +162-179 SPD (achievable with SPD boots + Speed set + good substats)

**Meta Ratings:** **Clan Boss 10/10**, Dungeons 9/10, Doom Tower 9/10, Arena 9/10, Faction Wars 9/10

---

### **🎯 MICHELANGELO - Debuff Spread/Hybrid Control** ⭐⭐ **MEDIUM PRIORITY (FUTURE)**

**Role:** Attack / Debuffer / Hybrid Control / TMNT Synergy  
**Why Consider:** **7/10 Clan Boss** - Debuff Spread (A2), Decrease ATK + Leech (A3), TMNT join attack synergy with Leonardo. ATK-scaling, needs god-tier SPD substats.

**Base Stats:** HP 15,360 | ATK 1,520 | DEF 1,035 | SPD 99 | C.RATE 15% | C.DMG 63% | RES 30 | ACC 10

**Key Mechanics:** (from `Michelangelo.json`)
- **A1 - Boo-Yah!**: 2-hit attack (ATK scaling 2.0 per hit), places Increase ATK 50% on self (2 turns) if either hit crits
- **A2 - Express Delivery!**: Single target, 75% Decrease DEF 60% + 75% Stun (100% booked), **Debuff Spread** (takes all debuffs and spreads to all enemies), ignores 25% RES on crit | Cooldown: 4 turns (3 booked)
- **A3 - Shell Cyclone**: AOE, 75% Decrease ATK 50% + Leech (2 turns, 100% booked), Taunt on self (2 turns), ignores 25% RES on crit | Cooldown: 5 turns (4 booked)
- **Passive - Party Dude**: 15% Evade (30% under Taunt), **joins attack when Leonardo/Donatello/Michelangelo/Raphael attacks**, Shield 300% ATK on self (1 turn) when hit

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - Warmaster T6 recommended]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ⚠️ MODERATE  
**Auto vs Manual Damage:** ~15-20% difference (Debuff Spread timing, Taunt placement)  
**Build Gaps:** [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐ MEDIUM (FUTURE)

**2:1 Viability:** ⭐ **DIFFICULT** - Base SPD 99, needs +164-181 SPD (requires god-tier substats + SPD boots + Speed set)

**Meta Ratings:** **Clan Boss 7/10**, Dungeons 9/10, Doom Tower 9/10, Arena 9/10, Faction Wars 9/10

---

## ALTERNATE CHAMPIONS

### **🎯 BAD-EL-KAZAR - Sustain/Poison Specialist** ⭐⭐⭐ **HIGH PRIORITY (ALTERNATE)**

**Role:** Support / Poison / Heal / Cleanse  
**Why Consider:** **BEST-IN-SLOT sustain champion** - AoE Continuous Heal (2× 15% heal buffs for 2 turns), AoE cleanse, AoE poison (2× 5% per enemy), passive +20% damage vs poisoned targets. **Legendary tier survivability.**

**Base Stats:** HP 20,145 | ATK 1,079 | DEF 1,156 | SPD 103 | C.RATE 15% | C.DMG 50% | RES 40 | ACC 20

**Key Mechanics:**
- **A1 - Dark Sphere**: AoE attack, heals all allies for 20% of damage dealt (lifesteal-like mechanic)
- **A2 - Malice**: **AoE cleanse** (removes ALL debuffs from all allies) + **2× Continuous Heal 15%** (2 turns) + **2× Poison 5%** on all enemies (2 turns) | Cooldown: 4 turns (3 booked)
- **A3 - Infected**: Single target, Decrease ACC 50% + extends debuff duration (2 turns) | Cooldown: 5 turns (4 booked)
- **Passive - Prey Upon**: **All allies deal +20% damage vs poisoned targets** 🔥 **TEAM-WIDE DAMAGE AMP**

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - Warmaster T6 recommended]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ✅ GOOD  
**Auto vs Manual Damage:** ~8-10% difference  
**Build Gaps:** [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐⭐ HIGH (ALTERNATE)

**2:1 Viability:** ⭐⭐ **GOOD** - Base SPD 103, needs +160-177 SPD (achievable with SPD boots + Speed set + good substats)

**Meta Ratings:** **Clan Boss 10/10**, Dungeons 10/10, Doom Tower 9/10, Faction Wars 10/10

---

### **🎯 GEOMANCER - HP Burn Reflect/Passive Damage** ⭐⭐⭐ **HIGH PRIORITY (ALTERNATE)**

**Role:** Attack / HP Burn / Reflect Damage / Weaken  
**Why Consider:** **10/10 Clan Boss** - Stoneguard passive reflects damage (15% reduction + deflect to HP Burned enemies + 30% chance 3% MAX HP proc), HP Burn + Weaken (A3), set-and-forget auto champion.

**Base Stats:** HP 15,525 | ATK 1,343 | DEF 935 | SPD 108 | C.RATE 15% | C.DMG 60% | RES 30 | ACC 0

**Key Mechanics:** (from `Geomancer.json`)
- **A1 - Tremor Staff**: AOE attack (ATK scaling 2.4), 30% chance Decrease ACC 50% (2 turns, 40% booked)
- **A2 - Creeping Petrify**: Single target (ATK scaling 6.0), removes buffs (steals if target has HP Burn from this champion), reduces A3 cooldown by 2 if kill under HP Burn | Cooldown: 4 turns (3 booked)
- **A3 - Quicksand Grasp**: Single target, **HP Burn + Weaken 25%** (3 turns, 75% chance → 100% booked), depletes TM + fills self TM | Cooldown: 5 turns (3 booked)
- **Passive - Stoneguard**: **Decreases damage all allies take by 15%**, deflects to enemies under HP Burn (this champion). 30% chance 3% enemy MAX HP damage on deflect. **Triggers Warmaster on deflect!**

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries - **Warmaster T6 CRITICAL** for passive procs]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ✅ EXCELLENT  
**Auto vs Manual Damage:** ~3-5% difference (passive is AI-independent)  
**Build Gaps:** [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐⭐⭐ HIGH (ALTERNATE)

**2:1 Viability:** ⭐⭐⭐ **EXCELLENT** - Base SPD 108, needs +155-172 SPD (achievable with SPD boots + Speed set)

**Meta Ratings:** **Clan Boss 10/10**, Dungeons 10/10, Doom Tower 10/10, Arena 6/10, Faction Wars 10/10

---

### **🎯 TAYREL - Decrease DEF/ATK Alternative** ⚠️ **(NOT OWNED)**

**Role:** Defense / Decrease DEF + ATK / Debuffer  
**Why Consider:** **Stag Knight alternative** - Provides Decrease DEF 60% + Decrease ATK 50% on separate skills (A1 + A3), better survivability (DEF-scaling, High Elf Epic). **Easier to gear** than Stag Knight for same debuff coverage.

**Base Stats:** HP 16,185 | ATK 881 | DEF 1,343 | SPD 95 | C.RATE 15% | C.DMG 50% | RES 45 | ACC 0

**Key Mechanics:** (estimated from stats table, JSON pending)
- **A1**: Likely Decrease ATK 50% (standard High Elf Epic kit)
- **A3**: Likely Decrease DEF 60% + Decrease Turn Meter
- **Role**: Defense-based debuffer with high base DEF (1,343 vs Stag Knight's 1,046)
- **Affinity**: Magic = neutral vs UNM Force

**Current Stats:** HP # | ATK # | DEF # | SPD # | C.RATE #% | C.DMG #% | RES # | ACC # 

**Current Gear:**
- **Sets:** 
  - **SET 1 Bonus:** 
  - **SET 2 Bonus:** 
  - **SET 3 Bonus:** 
- **Artifacts:**
- **Relic:** 
- **Blessing:** [Blessing] [#-star] [Effect]
- **Masteries:**
  - **Offense (T#):** [List key masteries]
  - **Defense/Support (T#):** [List key masteries]

**Auto AI Rating:** ✅ EXCELLENT  
**Auto vs Manual Damage:** ~5-7% difference  
**Build Gaps:** **NOT OWNED** | [Missing masteries, ACC issues, C.RATE needs, etc.]  
**Priority for 2:1:** ⭐ LOW (NOT OWNED)

**2:1 Viability:** ⚠️ **VERY HARD** - Base SPD 95, needs +168-185 SPD (requires exceptional substats + SPD boots + Speed set)

**Meta Ratings:** (Estimated) **Clan Boss 9/10**, Dungeons 9/10

---

## File Metadata

**Filename**: `UNM_Champion_Details.md`  
**Location**: `c:\GIT\Raid_Tools\Output\`  
**Version**: 1.0  
**Created**: 2025-11-07  
**Author**: Selicos (with GitHub Copilot assistance)  
**Format**: Markdown (.md)  

**Related Project Files**:
- `.github/copilot-instructions.md` (project standards)
- `input/Champion_Dictionary/Complete/*.json` (source data)
- `Output/UNM_Clan_Boss_Team_Analysis.md` (main analysis document)

---

**🎯 NEXT STEPS:**
1. Populate "Current Stats" sections with actual champion builds
2. Fill in "Current Gear" sections (sets, artifacts, relics, blessings, masteries)
3. Complete "Build Gaps" analysis per champion
4. Set "Priority for 2:1" ratings based on regearing difficulty
5. Cross-reference with main UNM analysis document for team selection
