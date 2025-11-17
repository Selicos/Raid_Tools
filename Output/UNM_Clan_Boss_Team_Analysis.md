# UNM Clan Boss - Central Reference Guide

**Purpose:** Centralized reference for UNM Clan Boss mechanics, speed tuning concepts, team archetypes, and strategic frameworks.  
**Scope:** Boss mechanics, damage calculations, speed tune math, team composition theory, and archetype analysis.  
**Excluded:** Champion-specific builds (see individual champion dictionary entries or `UNM CB Guide update.md` for current team details).

**Date Updated:** 2025-11-16  
**Version:** 4.0 - Strategic Reference

---

# Table of Contents

- [UNM Boss Stats Reference](#unm-boss-stats-reference-canonical)
- [Critical Mechanics Reference](#critical-mechanics-reference)
- [Speed Tune Concepts](#speed-tune-concepts)
- [Stat Requirements Framework](#stat-requirements-framework)
- [Team Archetypes & Composition Theory](#team-archetypes--composition-theory)
- [Damage Calculation Framework](#damage-calculation-framework)
- [Gear & Mastery Optimization](#gear--mastery-optimization)
- [Validation & Sources](#validation--sources)

---

## UNM Boss Stats Reference (CANONICAL)

| Stat | Value | Impact on Team Building |
|------|-------|------------------------|
| **HP** | 1,180,000,000 | Total damage target (100-140M with 3:2) |
| **SPD** | 170 (190 turn 1 only) | Determines tune range |
| **ACC** | 250 | Boss debuffs on team (resistable at 220+ RES) |
| **RES** | 300 | Team needs 250+ ACC for 90-95% debuff landing |
| **DEF** | ~3000 (estimated) | Defense calculation baseline |
| **Stun** | Every 3 turns | CANNOT be resisted, slowest champ targeted |
| **Poison Cap** | 50k per tick | Limits poison team damage ceiling |
| **HP Burn Cap** | 75k per tick | Limits HP Burn team damage ceiling |
| **Warmaster/Giant Slayer Cap** | 75k per proc | Limits mastery proc damage at UNM |

**Key Thresholds:**
- 1-key team: 70.3M+ damage (max chest + unlocks auto)
- 2-key team: ~40M+ per run (max chest in 2 keys)
- **3:2 Target**: ~80M+ per run (50% more turn frequency vs 1:1 tune)

---

## Critical Mechanics Reference

### Clan Boss First Turn
- Turn 1: Boss has **190 speed**
- Turn 2+: Boss has **170 speed**
- **3:2 tune requires 263-280 SPD** (ratio 1.547-1.647×)
- Turn ratio: Champion_SPD / Boss_SPD ≥ 1.5 for 3:2

### Clan Boss Stun Mechanic
- **Frequency**: Every 3 turns
- **Target**: Slowest champion
- **Resistable**: NO - 100% land rate regardless of RES stat
- **3:2 Strategy**: Slowest champion (263 SPD minimum) absorbs all stuns. Use high EHP or Block Debuffs/Unkillable.

### Clan Boss Immunity List (Passive)
Immune to:
- Stun, Freeze, Sleep
- Decrease Speed, Provoke
- Block Active Skills, Lock Passive Skills
- Fear/True Fear, Petrification, Berserk
- Enfeeble, Nullify
- Max HP Destruction, Turn Meter Reduction, HP Exchange

### Clan Boss 'Gathering Fury' Passive
- **Turn 10+**: Damage increases each turn
- **Turn 20+**: Damage increase accelerates
- **Turn 50+**: All attacks ignore Block Damage and Unkillable buffs (ends unkillable runs)

### Poison & HP Burn Caps
- **Poison**: 50k damage per tick maximum
  - Multiple poisons can stack (10 debuff limit)
  - Poison Sensitivity can increase damage
- **HP Burn**: 75k damage per tick maximum
  - Only 1 HP Burn can be active at a time

### Warmaster & Giant Slayer Masteries
- **Warmaster**: 60% proc chance per skill activation, 75k cap
- **Giant Slayer**: 30% proc chance per hit, 75k cap per hit
- **Both work regardless of crit** (no C.RATE requirement)
- **Optimal Choice**: Giant Slayer for 3+ hit A1s, Warmaster for 1-2 hit A1s

---

## Speed Tune Concepts

### What is 3:2 Speed Tune?

**3:2 = Your champions take 3 turns for every 2 boss turns**

**Speed Ranges:**

| Speed Range | Ratio | Turns per 2 Boss Cycles | Viability |
|-------------|-------|------------------------|-----------|
| 171-190 | 1:1 | 2 turns each | Standard (baseline) |
| 255-262 | 3:2 Minimum | 3 turns each | Possible but tight |
| **263-280** | **3:2 Fast** | **3 turns each** | **OPTIMAL** |
| 281-299 | 3:2 Very Fast | 3 turns each | High-end gear required |
| 300-339 | ~4:3 | 4 turns each (approx) | Overkill for most teams |
| 340+ | 2:1 | 4 turns each | True 2:1 (extremely difficult) |

**3:2 Speed Ratio Math:**
- Boss SPD: 170 (post-turn 1)
- Champion SPD: 263-280
- Ratio: 263/170 = 1.547, 280/170 = 1.647
- **Result: 3 champion turns per 2 boss turns**

---

### 3:2 Requirements (CRITICAL)

**MUST HAVE:**
1. **ALL 5 champions in 263-280 SPD range** (tight band required)
2. **SPD boots on EVERY champion** (+45 base, or +40 with SPD ascension substat)
3. **Speed set 2pc on EVERY champion** (+12% base SPD)
4. **High SPD substats** (10-15 SPD per piece minimum, 15+ ideal)
5. **NO Turn Meter manipulation** (Arbiter, Deacon, Apothecary break tune)
6. **NO Relentless sets** (random turns break tune)

**CANNOT USE:**
- Champions with TM boost skills (breaks rotation)
- Decrease SPD debuffs on boss (changes boss speed)
- Random turn manipulation (Relentless set, etc.)

---

### Buff/Debuff Duration with 3:2 Tune (CRITICAL)

**Understanding Turn Timing:**
- **3:2 means:** 3 champion turns per 2 boss turns
- **Buff durations** are measured in champion turns (your turns)
- **Cooldowns** are also measured in champion turns

**Example: 3-Turn Cooldown, 2-Turn Duration Skill**
- **Turn Pattern:**
  - Champion Turn 1: Cast skill → Buff active (2 turns remaining)
  - Champion Turn 2: Buff active (1 turn remaining)
  - Champion Turn 3: Buff expires, skill ready again → cast
  - **Result: 2 turns on, 1 turn off = 66.7% uptime (NOT 100%)**

**Why NOT 100% Uptime:**
- 2-turn duration ≠ 3-turn cooldown (gap of 1 turn)
- In 3:2 tune: 3 champion turns = 2 boss turns
- Gap turn = vulnerable to boss attacks!

**Coverage Strategy:**
- Use multiple champions with staggered cooldowns
- Use buff extension mechanics (Godseeker Aniri, etc.)
- Use cleanse for gap turns when Block Debuffs drops

**Key Insight:** With 3:2 tune, **no skill can have 100% uptime** unless:
1. Duration ≥ Cooldown (rare: permanent buffs or very long durations)
2. Multiple champions rotate the same buff
3. Buff extension mechanics used strategically

---

### Other Speed Tune Options

**4:3 Speed Tune (Advanced)**
- **Speed Range:** 281-299 SPD
- **Ratio:** 1.65-1.76× boss speed
- **Result:** 4 champion turns per 3 boss turns
- **Difficulty:** High-end gear required, tight tuning window
- **Use Case:** Maximum turn efficiency teams (Myth-Heir, etc.)

**2:1 Speed Tune (Endgame)**
- **Speed Range:** 340+ SPD
- **Ratio:** 2.0× boss speed
- **Result:** 2 champion turns per 1 boss turn
- **Difficulty:** Extremely difficult, requires Swift Parry/Speed sets + perfect substats
- **Use Case:** Speed farming, specific unkillable comps

**Unkillable Speed Tunes**
- Varies by comp (Maneater, Seeker, Roshcard, etc.)
- See dedicated unkillable guides for specific tuning windows
- Common ranges: 171-179 (slow-kill), 190-210 (budget), 240+ (fast unkillable)

---

## Stat Requirements Framework

### Priority by Role

**All Champions (Universal):**
- **Speed:** Per tune requirements (263-280 for 3:2)
- **HP:** 50k+ minimum, 60-70k+ ideal for survivability
- **DEF:** 3.5k+ minimum, 4k-4.5k+ ideal (diminishing returns past 5k)

**Damage Dealers:**
1. **C.RATE:** 100% (or as close as possible without sacrificing core stats)
2. **C.DMG:** 200%+ (maximize after hitting C.RATE cap)
3. **ATK:** 3k+ for ATK-scaling nukers (lower priority if DEF/HP scaling)
4. **ACC:** 250+ for debuffers, 280-300 ideal

**Support/Sustain:**
1. **HP/DEF:** Maximize for shields, heals, and survivability
2. **ACC:** 250+ if applying debuffs (Dec DEF, Dec ATK, etc.)
3. **RES:** 250-300 for debuff immunity (optional, cleanse > RES)
4. **C.RATE/C.DMG:** Low priority (unless hybrid damage/support)

**Stun Target (Slowest Champion):**
- **DEF:** 4.5k+ ideal (stun damage scales with low DEF)
- **HP:** 55k+ to survive multiple stuns
- **Alternative:** Unkillable, Block Damage, or Ally Protection to bypass stun damage

### Stat Breakpoints

| Stat | Minimum | Good | Excellent | Notes |
|------|---------|------|-----------|-------|
| **Speed** | 263 (3:2) | 270 | 277+ | Per tune requirements |
| **HP** | 50k | 60k | 70k+ | Survivability baseline |
| **DEF** | 3.5k | 4k | 4.5k+ | Diminishing returns past 5k |
| **ACC** | 250 | 280 | 300+ | For 90-95% debuff landing |
| **C.RATE** | 70% | 85% | 100% | Damage dealers only |
| **C.DMG** | 150% | 200% | 250%+ | After C.RATE capped |
| **RES** | 200 | 250 | 300+ | Optional (cleanse > RES) |

---

## Team Archetypes & Composition Theory

### Core Team Roles

Every successful UNM Clan Boss team requires coverage across these five core roles:

**1. Decrease DEF (MANDATORY)**
- **Why:** Boss has ~3000 DEF. Dec DEF 60% multiplies damage by 2.5×
- **Requirements:** 250+ ACC, high uptime (66.7%+ minimum)
- **Archetype:** Debuffer, typically supports survivability or damage
- **Common Examples:** AOE Dec DEF (Stag Knight, Tayrel), single-target high-uptime

**2. Damage Source (PRIMARY)**
- **Types:**
  - HP Burn (75k/tick cap = ~7.5M over 50 turns)
  - Warmaster/Giant Slayer procs (75k/proc cap = ~6.75M per champion)
  - Poison (50k/tick cap = ~5M over 50 turns with multiple poisoners)
  - Reflect damage (passive, scales with team EHP)
  - Direct damage (A1/A2/A3 with high crit/crit dmg)
- **Optimal:** HP Burn + Warmaster = ~14M baseline before direct damage
- **Alternate:** Poison teams can reach 25-30M but require multiple poisoners

**3. Survivability (MANDATORY)**
- **Options (pick 2-3):**
  - Shields (30% MAX HP typical)
  - Block Debuffs (prevents boss debuffs)
  - Cleanse (removes debuffs after they land)
  - Heals (Continuous Heal, passive heals, Lifesteal sets)
  - Revive (emergency recovery)
  - Ally Protection/Block Damage (redirect or mitigate damage)
- **Key Stat:** 50k+ HP, 4k+ DEF on all champions
- **Combo:** Shields + Block Debuffs or Shields + Cleanse most common

**4. Debuff Mitigation (MANDATORY)**
- **Why:** Boss applies Dec SPD, Dec ATK, poisons, stuns
- **Strategies:**
  - Block Debuffs (proactive, 66.7% uptime typical)
  - Cleanse (reactive, 100% uptime possible with fast champions)
  - Perfect Veil (blocks debuffs, rare)
  - High RES (250-300, optional - cleanse > RES)
- **Ideal:** Block Debuffs with cleanse backup for gap turns

**5. Stun Target Management (MANDATORY)**
- **Boss Mechanic:** Stuns slowest champion every 3 turns (cannot be resisted)
- **Solutions:**
  - Tank it: 4.5k+ DEF, 55k+ HP on slowest champion
  - Block Damage: Prevents stun damage entirely
  - Unkillable: Immunity to stun damage
  - Ally Protection: Redirect stun to tankier champion
- **3:2 Tuning:** Slowest champion is typically 263-267 SPD

---

### Team Archetype Families

**1. Tanky Killable (3:2)**
- **Core Concept:** High survivability, consistent damage, no cheese mechanics
- **Requirements:**
  - All 5 champions 263-280 SPD
  - 2-3 survivability mechanics (shields, cleanse, heals)
  - Dec DEF 60% + Weaken/Dec ATK
  - HP Burn or Poison primary damage
  - Warmaster/Giant Slayer on 3-5 champions
- **Strengths:** Reliable, auto-friendly, affinity-safe
- **Weaknesses:** Lower damage ceiling (40-70M typical)
- **Example Composition:**
  - Dec DEF debuffer (Stag Knight, Tayrel)
  - HP Burn/Weaken specialist (Geomancer, Ninja)
  - Block Debuffs/Shield (Brogni, Wythir)
  - Cleanse/Sustain (Mithrala, Bad-el-Kazar)
  - Revive/Heal (Godseeker Aniri, Rector Drath)

**2. Unkillable (Various Speed Tunes)**
- **Core Concept:** Unkillable buff prevents all damage, allows glass cannon builds
- **Requirements:**
  - Unkillable champion (Maneater, Roshcard, Wythir, Leonardo, etc.)
  - Precise speed tuning (varies by comp: 171-179, 240+, etc.)
  - High ACC on debuffers (no survivability stats needed)
  - Max damage stats (100% C.RATE, 250%+ C.DMG)
- **Strengths:** Highest damage ceiling (60-120M+), consistent, immortal
- **Weaknesses:** Turn 50 limit (boss ignores unkillable), requires specific champions
- **Sub-Types:**
  - Budget unkillable (Maneater ×2, slow tune 171-179 SPD)
  - Fast unkillable (Seeker/Maneater, 240+ SPD)
  - Leonardo/Michelangelo (counterattack unkillable, 263+ SPD)
  - Myth-Heir (Demytha + Heiress, 4:3 tune)

**3. Ally Protection/Block Damage**
- **Core Concept:** Redirect or negate damage, allows squishy damage dealers
- **Requirements:**
  - Ally Protection champion (Leonardo, Jareg, Sandlashed)
  - Block Damage optional (Roshcard, Krisk)
  - High EHP on protection champion (70k+ HP, 5k+ DEF)
  - Speed tuning to ensure protection before boss turns
- **Strengths:** Flexible, can run glass cannon damage dealers
- **Weaknesses:** Requires specific champions, protection champion can die

**4. Counterattack**
- **Core Concept:** Boss attacks trigger counterattacks, doubling team turn frequency
- **Requirements:**
  - Counterattack champion (Skullcrusher, Leonardo, Valkyrie)
  - High damage dealers with strong A1s
  - Dec DEF + Weaken for damage amplification
  - Lifesteal sets or heals for sustain
- **Strengths:** Very high damage ceiling (70-100M+)
- **Weaknesses:** Requires specific champions, vulnerable without survivability

**5. Poison Teams**
- **Core Concept:** Stack 10 poisons for 50k/tick each = 500k/turn
- **Requirements:**
  - 2-3 poisoners (Frozen Banshee, Bad-el-Kazar, Elenaril, etc.)
  - Poison Sensitivity (Frozen Banshee) for +damage
  - Dec DEF for direct damage amplification
  - High ACC (250+) on all poisoners
- **Strengths:** Can reach 25-35M with mediocre gear
- **Weaknesses:** Lower ceiling than HP Burn/Warmaster, requires multiple champions

---

## Damage Calculation Framework

**Baseline 3:2 Tanky Killable (50 turns):**
- HP Burn: 75k × 2 ticks/turn × 50 turns = 7.5M
- Warmaster (5 champs): 5 × 60% proc × 75k × 3 skills/turn × 50 turns = 6.75M
- Dec DEF amp (2.5×): Direct damage increased
- Weaken amp (1.25×): All damage increased
- Reflect damage: ~10% boss damage reflected = 3-5M
- **Total: 40-70M** (varies by stats, affinity, RNG)

**Peak Unkillable (50 turns before Turn 50 limit):**
- HP Burn: 7.5M (same)
- Warmaster (5 champs, glass cannon builds): 6.75M × 1.5 (better stats) = 10M
- Dec DEF + Weaken: 3.75× total amp
- Counterattack bonus: +50% turns = +50% damage
- **Total: 70-120M** (varies by comp, affinity)

**Turn 50+ Considerations:**
- Boss ignores unkillable/block damage after turn 50
- Unkillable teams must finish by turn 50 or transition to killable setup
- Tanky killable teams can survive 60-80+ turns with proper sustain

---

### Speed Tune Compatibility Matrix

| Archetype | Speed Range | Tune Type | Difficulty | Damage Ceiling | Auto Viable? |
|-----------|-------------|-----------|------------|----------------|--------------|
| Tanky Killable | 263-280 | 3:2 | Medium | 40-70M | ✅ Yes |
| Fast Unkillable | 240-260 | Varies | High | 70-100M | ✅ Yes (with tune) |
| Budget Unkillable | 171-179 | 1:1 slow | Medium | 60-90M | ✅ Yes |
| Myth-Heir | 281-299 | 4:3 | Very High | 80-120M | ✅ Yes (precise) |
| Leonardo Counterattack | 263-280 | 3:2 | High | 70-95M | ⚠️ Partial (manual burst) |
| Poison Team | 263-280 | 3:2 | Low | 25-35M | ✅ Yes |
| Ally Protection | 263-280 | 3:2 | Medium | 50-80M | ✅ Yes |

---

### Affinity Strategy

**Boss Affinity Rotation:** Force → Magic → Spirit → Void (4-day cycle)

**Affinity Impact:**
- **Strong affinity:** +15% C.RATE, +30% damage, 30% chance for strong hit (bonus damage)
- **Weak affinity:** -15% C.RATE, -20% damage, 35% chance for weak hit (cannot apply debuffs)
- **Neutral affinity:** No bonuses or penalties

**Team Building for Affinity:**
- **Ideal:** All Void team (neutral all affinities)
- **Practical:** Avoid weak affinity on critical roles:
  - Dec DEF debuffer: Must land debuffs (no weak affinity)
  - HP Burn specialist: Must land HP Burn (no weak affinity)
  - Cleanse: Can be weak affinity (cleanse doesn't land debuffs)
  - Damage dealers: Avoid weak affinity (damage penalty)

**Affinity Priority by Boss:**
| Boss Affinity | Best Damage | Avoid | Notes |
|---------------|-------------|-------|-------|
| **Void** | All neutral | None | Best for max damage |
| **Force** | Spirit champs | Magic champs | Spirit champs get +30% damage |
| **Magic** | Force champs | Spirit champs | Force champs get +30% damage |
| **Spirit** | Magic champs | Force champs | Magic champs get +30% damage |

---

## Gear & Mastery Optimization

### Gear Set Priorities

**Universal (All Archetypes):**
1. **Speed set (2pc):** +12% SPD = essential for 3:2 tune
2. **Perception (2pc):** +40 ACC = critical for debuffers
3. **Immortal/Regeneration (2pc/4pc):** Passive healing, reduces reliance on active heals

**Tanky Killable:**
- Speed + Perception + Immortal (most common)
- Speed + Perception + Lifesteal (for damage dealers)
- Speed + Shield + Immortal (for ultra-tanky setups)

**Unkillable:**
- Speed + Perception + Savage (ignore DEF for damage)
- Speed + Lethal + Cruel (max crit damage)
- No survivability sets needed (unkillable = immortal)

**Counterattack:**
- Speed + Lifesteal + Perception (sustain from counters)
- Speed + Savage + Lifesteal (max damage + sustain)

---

### Mastery Optimization

**T6 Offense Masteries:**
- **Warmaster:** 60% proc rate, 75k cap. Best for 1-2 hit A1s
- **Giant Slayer:** 30% proc rate per hit, 75k cap per hit. Best for 3+ hit A1s
- **Both work regardless of crit** (no C.RATE requirement)

**Critical Offense Masteries:**
- **Methodical (T5):** +2% A1 damage per use (max +10%) = stacking damage over long fights
- **Bring It Down (T4):** +6% damage vs higher MAX HP targets = always active vs boss
- **Single Out (T3):** +8% damage vs targets <40% HP = active last 20-25 turns

**Critical Support Masteries:**
- **Master Hexer (T5):** 30% chance extend debuffs +1 turn = 2-turn debuffs become 3-turn often
- **Lasting Gifts (T4):** 30% chance extend buffs +1 turn = 2-turn buffs become 3-turn often
- **Lore of Steel (T4):** +15% set bonuses = boosts Speed, Immortal, Shield sets significantly

**Critical Defense Masteries:**
- **Unshakeable (T6):** +50 RES = helps resist boss debuffs (optional, cleanse > RES)
- **Delay Death (T3):** Stacking damage reduction = better survivability in long fights
- **Resurgent (T3):** 50% chance remove debuff when hit hard = emergency cleanse

---

## Validation & Sources

**Data Sources:**
- RaidHQ (boss mechanics, damage caps)
- Ayumilove (champion skills, masteries, gear)
- HellHades (team comps, tier lists, speed tunes)
- DeadwoodJedi (speed tune calculator, unkillable guides)
- In-game testing (3+ runs per concept validation)

**Confidence Level:**
- HIGH: Boss mechanics, speed tune math, damage caps (cross-validated 3+ sources)
- HIGH: Team archetypes, composition theory (validated with community consensus)
- MEDIUM: Specific damage projections (vary by gear, affinity, RNG)

**Last Updated:** 2025-11-16  
**Version:** 4.0 - Strategic Reference

---

## Related Documentation

- **Current Team Analysis:** `Output/UNM CB Guide update.md` (specific champion builds, current performance)
- **Champion Details:** `input/Champion_Dictionary/Complete/` (individual champion JSON entries)
- **Copilot Instructions:** `.github/copilot-instructions.md` (project workflows and standards)

---
