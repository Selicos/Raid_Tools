# UNM Clan Boss Champion Comparison & Team Optimization Prompt

## Project Overview

**Objective:** Identify the optimal 5th champion for a UNM Clan Boss team, optimize speed tuning, and evaluate potential team composition variations for maximum damage and survivability on full AUTO.

**Output File:** `Notes/UNM_Team_Optimization_DRAFT.md`

**Scope:** Analyze top 60 most viable champions from owned list, simulate 20-30 team compositions across 6 archetypes, and present top 10-15 teams with full specifications.

---

## Current Team (4 Champions, FIXED)

### Core 4 Champions

1. **Geomancer** (Magic, Epic, Barbarians)
   - **Current Stats:** SPD 217, RES 88, HP 57k, DEF 4,010, ACC ~250
   - **Role:** HP Burn passive specialist (reflects 75% boss damage, triggers Warmaster)
   - **Key Mechanics:** 
     - A1: Places HP Burn (3 turns, 100% if crit)
     - Passive: Reflects 75% of damage taken as HP Burn damage, triggers Warmaster on reflect
   - **Affinity Risk:** Magic (weak vs Force boss)

2. **Mithrala Lifebane** (Spirit, Legendary, Undead Hordes)
   - **Current Stats:** SPD 241, RES 145, HP 64k, DEF 4,171, ACC ~250
   - **Role:** Cleanse, sustain, debuffer
   - **Key Mechanics:**
     - A2: Cleanse all debuffs from ally, places Block Debuffs (2 turns)
     - A3: AoE damage + heal based on enemy MAX HP (scales with boss HP)
   - **Affinity Risk:** Spirit (weak vs Magic boss, safe vs current Force/GREEN boss)

3. **Godseeker Aniri** (Void, Epic, Sacred Order)
   - **Current Stats:** SPD 218, RES 291, HP 76k, DEF 3,403, ACC ~250
   - **Gear:** REGEN set
   - **Role:** Buff extender, healer, reviver
   - **Key Mechanics:**
     - A2: Extend all ally buffs by 1 turn (extends shields, Increase DEF, Block Debuffs, etc.)
     - A3: Revive all dead allies with 50% HP/TM
     - Passive: Heals ally when ally is hit (10% of Aniri's MAX HP)
   - **Affinity Risk:** Void (safe vs all affinities)
   - **REPLACEMENT CONSIDERATION:** May be replaced by Arbiter, Rector Drath, Scyl, or Tagoar if better for speed tune/damage

4. **Underpriest Brogni** (Magic, Legendary, Dwarves)
   - **Current Stats:** SPD 225, RES 229, HP 82k, DEF 4,499, ACC 137
   - **Gear:** BOLSTER set
   - **Role:** Shield specialist, Block Debuffs, passive damage dealer
   - **Key Mechanics:**
     - A2: Places 3-turn Block Debuffs on all allies
     - A3: Places shields on all allies (scales with Brogni DEF)
     - Passive: When ally loses shield, deals damage to boss (triggers Warmaster on shield damage)
   - **Affinity Risk:** Magic (weak vs Force boss)

### Current Speed Order
1. Mithrala: 241 SPD (fastest)
2. Brogni: 225 SPD
3. Aniri: 218 SPD
4. Geomancer: 217 SPD (slowest, current stun target for Spirit boss)

### Current Affinity Balance
- **Magic:** 2 champions (Geomancer, Brogni) - WEAK vs Force boss
- **Spirit:** 1 champion (Mithrala) - WEAK vs Magic boss, SAFE vs current Force boss
- **Void:** 1 champion (Aniri) - SAFE vs all affinities
- **Force:** 0 champions - GAP (Force champions safe vs current Force/GREEN boss)

### Current Team Buffs/Debuffs/Synergies Analysis

**Buffs Provided (Current 4 Champions):**
- **Block Debuffs:** Mithrala A2 (2 turns), Brogni A2 (3 turns) - HIGH UPTIME
- **Shields:** Brogni A3 (scales with DEF) - Extended by Aniri A2 (critical for Brogni passive damage)
- **Increase DEF:** None currently - **GAP**
- **Increase ATK:** None currently - **GAP**
- **Heal:** Aniri passive (10% of Aniri MAX HP when ally is hit), Mithrala A3 (scales with boss MAX HP)
- **Revive:** Aniri A3 (all allies, 50% HP/TM)
- **Buff Extension:** Aniri A2 (extends all ally buffs by 1 turn) - **CRITICAL SYNERGY**

**Debuffs Provided (Current 4 Champions):**
- **HP Burn:** Geomancer A1 (3 turns, 100% if crit) - **PRIMARY DAMAGE SOURCE**
- **Decrease DEF:** None currently - **CRITICAL GAP**
- **Decrease ATK:** None currently - **GAP** (reduces boss damage by 50%)
- **Decrease SPD:** None currently
- **Poison:** None currently - **GAP** (max 10 debuffs = 25% boss MAX HP per turn)
- **Weaken:** None currently - **GAP** (increases damage by 25%)
- **Leech:** None currently - **GAP** (sustain for late rounds)

**Key Synergies:**
1. **Brogni Shields + Aniri Buff Extension:** Shields last longer = more Brogni passive damage procs
2. **Geomancer HP Burn + Boss Reflect:** 75% of boss damage reflected back, triggers Warmaster
3. **Block Debuffs + Boss Mechanics:** Prevents Spirit Decrease Speed, Force Decrease DEF, Magic debuff block
4. **Mithrala Cleanse + Boss Debuffs:** Removes stun, Decrease Speed, Decrease DEF

**Critical Gaps for 5th Champion:**
1. **Decrease DEF** (60% damage amp) - HIGHEST PRIORITY
2. **Poison** (25% boss MAX HP per turn with 10 poisons) - HIGH PRIORITY
3. **Decrease ATK** (50% less damage taken) - HIGH PRIORITY for survivability
4. **Increase DEF** (scales with Aniri extension) - MEDIUM PRIORITY
5. **Weaken** (25% damage amp) - MEDIUM PRIORITY
6. **Leech** (late-round sustain) - MEDIUM PRIORITY
7. **Ally Attack / Counterattack** (more Geo/Brogni passive procs) - HIGH PRIORITY for damage

**Recommended 5th Champion Priorities (Based on Gaps):**
1. **Dual-role champions** (e.g., Fayne: Decrease DEF + Poison, Tayrel: Decrease DEF + Decrease ATK)
2. **High-value debuffers** (e.g., Deacon Armstrong: Decrease DEF + SPD aura, Rhazin: Decrease DEF + Weaken)
3. **Ally Attack champions** (e.g., Nogdar, Seeker, Tagoar: Extra turns for Geo/Brogni passives)
4. **Poison specialists** (e.g., Venomage, Frozen Banshee: 4-5 poisons per cycle)

---

## PHASE 0: Optimize Current 4-Champion Speed Tuning (PRIORITY)

**Objective:** Before analyzing 5th champion options, optimize speed tuning for the existing 4 champions to establish best baseline performance. **VALIDATE SKILLS/MECHANICS FROM CHAMPION REVIEWS ON FIRST ACCESS.**

### Champion Skill Quick Reference (To Be Validated)

**Geomancer (Magic, Epic, Barbarians):**
- **A1:** Places HP Burn (3 turns, 100% if crit)
- **Passive:** Reflects 75% of damage taken as HP Burn damage, triggers Warmaster on reflect
- **Recommended Gear:** Lifesteal + Speed OR Stalwart + Speed (for stun target)
- **Recommended Masteries:** Warmaster (T6 Offense) - triggers on passive reflect damage
- **Synergies:** Needs high Crit Rate (100%) to guarantee HP Burn, benefits from Aniri buff extension (HP Burn lasts longer)
- **VALIDATE:** Check Geomancer review (`Notes/Champion Reviews/Geomancer_Review_DRAFT.md`) if exists

**Mithrala Lifebane (Spirit, Legendary, Undead Hordes):**
- **A2:** Cleanse all debuffs from ally, places Block Debuffs (2 turns)
- **A3:** AoE damage + heal based on enemy MAX HP (scales with boss HP)
- **Recommended Gear:** Speed + Accuracy OR Speed + Immortal
- **Recommended Masteries:** Warmaster (T6 Offense) for A3 scaling damage
- **Synergies:** Cleanse pairs with Aniri revive (remove debuffs after revive), Block Debuffs extended by Aniri
- **VALIDATE:** Search online for Mithrala skill details (no review file exists yet)

**Godseeker Aniri (Void, Epic, Sacred Order):**
- **A2:** Extend all ally buffs by 1 turn (extends shields, Increase DEF, Block Debuffs, etc.)
- **A3:** Revive all dead allies with 50% HP/TM
- **Passive:** Heals ally when ally is hit (10% of Aniri's MAX HP)
- **Recommended Gear:** REGEN (current) + Speed OR Immortal + Speed
- **Recommended Masteries:** Support tree (Cycle of Magic, Lasting Gifts for buff extension)
- **Synergies:** CRITICAL for extending Brogni shields (more passive damage) and Block Debuffs (more survivability)
- **VALIDATE:** Check Godseeker Aniri review (`Notes/Champion Reviews/Godseeker_Aniri_Review_DRAFT.md`) if exists

**Underpriest Brogni (Magic, Legendary, Dwarves):**
- **A2:** Places 3-turn Block Debuffs on all allies
- **A3:** Places shields on all allies (scales with Brogni DEF)
- **Passive:** When ally loses shield, deals damage to boss (triggers Warmaster on shield damage)
- **Recommended Gear:** BOLSTER (current) + Speed OR Stalwart + Immortal
- **Recommended Masteries:** Warmaster (T6 Offense) - triggers on passive shield damage
- **Synergies:** CRITICAL synergy with Aniri buff extension (shields last longer = more passive procs), shields scale with DEF (high DEF = high damage)
- **VALIDATE:** Check Underpriest Brogni review (`Notes/Champion Reviews/Underpriest_Brogni_Review_DRAFT.md`) if exists

### Current Speed Order & Issues
1. **Mithrala:** 241 SPD (fastest) - Too fast for 1:1 (171-189), borderline for 2:1 (250-280)
2. **Brogni:** 225 SPD - Too fast for 1:1, too slow for 2:1
3. **Aniri:** 218 SPD - Too fast for 1:1, too slow for 2:1
4. **Geomancer:** 217 SPD (slowest) - Too fast for 1:1, too slow for 2:1

**Problem:** Not optimized for ANY standard speed tune (1:1 or 2:1)

### Speed Tuning Options to Evaluate

#### Option 1: 1:1 Speed Tune (171-189 SPD) - EASIEST
**Recommended Speeds:**
- **Mithrala:** 189 SPD (-52 SPD) - Goes first, applies cleanse/Block Debuffs
- **Brogni:** 185 SPD (-40 SPD) - Goes second, applies shields/Block Debuffs
- **Aniri:** 181 SPD (-37 SPD) - Goes third, extends buffs after they're applied
- **Geomancer:** 175 SPD (-42 SPD) - Goes last, STUN TARGET for Spirit boss, applies HP Burn

**Pros:**
- Easy to gear (lower SPD requirements)
- Consistent turn order (safe for AUTO)
- Optimized stun target (Geo is slowest, can tank stun)
- Frees up substats for DEF/HP/ACC/RES

**Cons:**
- Lower damage ceiling (1 turn per boss turn = fewer debuffs/procs)
- Geo HP Burn uptime slightly lower (reapplies every 3 turns, not 1.5 turns)

**Expected Damage:** 90M-110M (baseline for 1:1 tune)

---

#### Option 2: 2:1 Speed Tune (250-280 SPD) - HIGHEST DAMAGE
**Recommended Speeds (using DeadwoodJedi calculator):**
- **Mithrala:** 254 SPD (+13 SPD) - Goes first, applies cleanse/Block Debuffs
- **Brogni:** 252 SPD (+27 SPD) - Goes second, applies shields/Block Debuffs
- **Aniri:** 250 SPD (+32 SPD) - Goes third, extends buffs after they're applied
- **Geomancer:** 171 SPD (-46 SPD) - Goes last, STUN TARGET for Spirit boss, applies HP Burn (SLOW BAIT)

**Note:** Geo at 171 SPD is "slow bait" for 2:1 tune (team goes 2:1, Geo goes 1:1 as intentional stun target)

**Pros:**
- Highest damage ceiling (2 turns per boss turn = more debuffs/procs)
- Geo HP Burn uptime maximized (Mithrala/Brogni/Aniri reapply more often)
- Brogni shield uptime maximized (more shield procs = more passive damage)

**Cons:**
- Harder to gear (high SPD requirements, must be EXACT)
- Spirit boss Decrease Speed can break tune (need 250+ RES or cleanse)
- Sacrifices DEF/HP/ACC/RES substats for SPD

**Expected Damage:** 120M-140M+ (baseline for 2:1 tune)

---

#### Option 3: Hybrid/Flexible Tune (Current Range, Optimized) - BALANCED
**Recommended Speeds:**
- **Mithrala:** 235 SPD (-6 SPD) - Goes first, fast enough for consistent cleanse
- **Brogni:** 220 SPD (-5 SPD) - Goes second, applies shields before Aniri extends
- **Aniri:** 215 SPD (-3 SPD) - Goes third, extends buffs after Brogni shields
- **Geomancer:** 175 SPD (-42 SPD) - Goes last, STUN TARGET for Spirit boss

**Pros:**
- Minimal gear changes (only Geo needs significant SPD reduction)
- Optimized stun target (Geo is slowest)
- Balanced turn cycling (not quite 2:1, but faster than 1:1)
- Easier to maintain DEF/HP/ACC/RES stats

**Cons:**
- Not a "true" speed tune (inconsistent turn order vs boss)
- Damage ceiling between 1:1 and 2:1 (not optimal for either)

**Expected Damage:** 100M-120M (baseline for hybrid tune)

---

### PHASE 0 Deliverable

**Output:** Speed tuning recommendation table for current 4 champions

| Champion | Current SPD | Option 1 (1:1) | Option 2 (2:1) | Option 3 (Hybrid) | Recommended Gear Changes |
|----------|-------------|----------------|----------------|-------------------|--------------------------|
| Mithrala | 241 | 189 (-52) | 254 (+13) | 235 (-6) | [Evaluate: Can drop SPD boots for HP/DEF?] |
| Brogni | 225 | 185 (-40) | 252 (+27) | 220 (-5) | [Evaluate: BOLSTER set limits SPD flexibility] |
| Aniri | 218 | 181 (-37) | 250 (+32) | 215 (-3) | [Evaluate: REGEN set limits SPD flexibility] |
| Geomancer | 217 | 175 (-42) | 171 (-46) | 175 (-42) | [Evaluate: Drop SPD boots for Crit Rate/HP?] |

**Analysis:**
- Which option requires least gear changes?
- Which option maximizes damage while maintaining survivability?
- Which option best accommodates 5th champion flexibility?

**Recommendation:** Test all 3 options with current 4-champion team (no 5th) to establish baseline damage and survivability before adding 5th champion.

---

## Boss Mechanics & Restrictions

### UNM Clan Boss Key Mechanics

**Affinity Rotation:** Void → Spirit → Force → Magic (rotates daily)

**Current Boss:** Force affinity (GREEN) - Decrease DEF debuff, weak affinity for Magic champions

**Boss Immunities (DO NOT USE):**
- Turn Meter Reduction (e.g., Alure, Armiger)
- Freeze (e.g., Ninja A3)
- Stun (e.g., Scyl A2)
- Sleep, Provoke, Fear (all CC except debuffs)

**Debuff Limit:** Maximum 10 debuffs on boss at once
- **Priority debuffs:** Poison (2.5% MAX HP per turn), Decrease DEF (60% more damage), Decrease ATK (50% less damage taken), Weaken (25% more damage), HP Burn (rare, high value)

**Stun Mechanics:**
- **Spirit Boss:** Stuns slowest champion + applies Decrease Speed
- **Force Boss:** Applies Decrease DEF (current boss)
- **Magic Boss:** Blocks debuffs (resist-based)
- **Void Boss:** No special mechanics

**Damage Scaling:** Boss damage increases every 10 turns (survivability becomes critical after turn 30+)

### Speed Tuning Considerations

**1:1 Speed Tune (Simplest, AUTO-friendly):**
- All champions 171-189 SPD (go once per boss turn)
- Pros: Easy to gear, safe for AUTO, consistent
- Cons: Lower damage ceiling (fewer turns = fewer debuffs/procs)

**2:1 Speed Tune (High damage, requires precision):**
- All champions 250-280+ SPD (go twice per boss turn)
- Pros: Higher damage ceiling (more turns = more debuffs/procs)
- Cons: Difficult to gear, speed tuning must be EXACT, Spirit boss Decrease Speed can break tune

**Hybrid/Flexible Tune:**
- Mix of 1:1 and 2:1 (some champions fast, some slow)
- Pros: Easier to gear than full 2:1, can optimize stun target
- Cons: Less consistent, requires careful turn order planning

**AUTO Play Requirement:** Team must work on full AUTO (no manual skill selection)

---

## Analysis Requirements

### Phase 1: Champion Filtering (Top 60 Viable Champions)

**Selection Criteria:**
1. **Decrease DEF Champions:** Deacon Armstrong, Rhazin, Tayrel, Dhukk, Stag Knight, etc.
2. **Poison Champions:** Fayne, Venomage, Frozen Banshee, Narma, Juliana, etc.
3. **Ally Attack Champions:** Nogdar, Seeker, Tagoar, Longbeard, etc.
4. **Counterattack Champions:** Skullcrusher, etc.
5. **Shield Champions:** Maulie Tankard, Seeker, etc.
6. **Increase DEF Champions:** Tayrel, Rector Drath, Tagoar, etc.
7. **Leech Champions:** Bad-el-Kazar, etc.
8. **Buff Extension Champions:** (already have Godseeker Aniri)
9. **Revive Champions:** Arbiter, Rector Drath, Scyl, etc. (Godseeker Aniri alternatives)
10. **Self-Cleanse/Stun Immunity Champions:** Skullcrusher (passive counterattack cleanses), Maulie (Block Debuffs), etc.

**Exclusion Criteria:**
- Champions with TM reduction as primary mechanic (Alure, Armiger)
- Champions with Freeze/Stun/CC as primary mechanic (not usable on boss)
- Champions with very low base stats (won't survive UNM without godly gear)
- Champions requiring manual play (e.g., skill timing, conditional skills)

**Output:** List of top 60 champions ranked by UNM viability

### Phase 2-7: Team Simulations (6 Archetypes)

**For each archetype, simulate 3-5 team compositions:**

#### Archetype 1: Poison Focus
- **5th Champion Options:** Fayne, Venomage, Frozen Banshee, Narma
- **Strategy:** Maximize poison uptime (10 poisons = 25% boss MAX HP per turn), pair with Decrease DEF
- **Expected Damage:** 100M-130M (poison scaling + Geo/Brogni passives)

#### Archetype 2: Ally Attack / Counterattack
- **5th Champion Options:** Nogdar, Seeker, Tagoar, Skullcrusher
- **Strategy:** Extra turns = more Geo HP Burn procs + more Brogni shield damage procs
- **Expected Damage:** 110M-140M (high passive proc rate)

#### Archetype 3: Shield Extension
- **5th Champion Options:** Maulie Tankard, Seeker (shields), Tagoar (Increase DEF)
- **Strategy:** Continuous shields feed Brogni passive, extended Increase DEF reduces damage taken
- **Expected Damage:** 90M-120M (high survivability, moderate damage)

#### Archetype 4: Decrease DEF Focus
- **5th Champion Options:** Deacon Armstrong, Rhazin, Tayrel, Dhukk, Stag Knight
- **Strategy:** 60% damage amp on ALL damage (Geo passive, Brogni passive, poisons, etc.)
- **Expected Damage:** 110M-140M (damage amplification for all sources)

#### Archetype 5: Leech / Sustain
- **5th Champion Options:** Bad-el-Kazar (Leech + Decrease ATK + Poison + self-revive)
- **Strategy:** Late-round survivability (Leech heals from all damage), Decrease ATK reduces damage taken
- **Expected Damage:** 100M-130M (high survivability, consistent damage)

#### Archetype 6: Stun Target Specialist
- **5th Champion Options:** Skullcrusher (self-cleanse counterattack), Maulie (Block Debuffs + self-revive)
- **Strategy:** Intentional slowest champion (Spirit boss stun target), self-cleanse or immunity
- **Expected Damage:** 90M-120M (optimized stun target, no disruption to key roles)

### Phase 8: Godseeker Aniri Alternatives

**For top 5 teams from each archetype, test replacing Godseeker Aniri with:**

1. **Arbiter** (Void, Legendary, High Elves)
   - Pros: TM boost (30% to all allies), ATK buff (50% for 2 turns), revive (all allies 30% HP/TM), SPD aura (30%)
   - Cons: No buff extension (loses synergy with Brogni shields/Block Debuffs)

2. **Rector Drath** (Spirit, Epic, Knights Revenant)
   - Pros: Block Debuffs (3 turns, 3-turn CD), revive (single target, 100% HP), Decrease ATK (60% for 2 turns), DEF aura (33%)
   - Cons: Single-target revive only, weak affinity vs Magic boss

3. **Scyl of the Drakes** (Spirit, Legendary, Barbarians)
   - Pros: Revive (single target, 100% HP/TM), heal (30% to all allies), SPD aura (19%)
   - Cons: Stun doesn't work on boss, weak affinity vs Magic boss

4. **Tagoar** (Force, Epic, Ogryn Tribes)
   - Pros: Ally Attack (4-turn CD), Increase DEF (60% for 3 turns), DEF aura (33%), Force affinity (safe vs current boss)
   - Cons: No revive, no buff extension

**Evaluation Criteria:**
- Does replacement improve speed tuning? (Arbiter TM boost, Scyl/Arbiter SPD aura)
- Does replacement improve damage? (Arbiter ATK buff, Tagoar Ally Attack)
- Does replacement improve survivability? (Rector Drath Decrease ATK, Tagoar Increase DEF)
- Does buff extension loss hurt team? (Brogni shields/Block Debuffs no longer extended)

### Phase 9-10: Speed Tuning & Stun Target Optimization

**For each team composition:**

1. **Identify optimal speed tune:** 1:1, 2:1, or hybrid
2. **Calculate exact speed requirements** for all 5 champions
3. **Identify ideal stun target** (slowest champion, preferably self-cleanse or low priority)
4. **Note stat adjustments needed** for existing 4 champions (Geo, Mithrala, Aniri, Brogni)
5. **Document turn order** (who goes first, who applies debuffs before damage dealers, etc.)

**Stun Target Priority (Best to Worst):**
1. **Skullcrusher** (self-cleanse counterattack, stun removed immediately)
2. **Maulie Tankard** (Block Debuffs, can't be stunned if buff is up)
3. **Tank/Reviver** (Aniri, Rector Drath - can be revived if dies)
4. **Buffer** (Brogni, Tagoar - not critical for debuffs)
5. **Debuffer** (Deacon, Fayne - AVOID as stun target, critical for damage)
6. **Geomancer** (AVOID as stun target, HP Burn is primary damage source)

### Phase 11: Gear Recommendations

**For each team composition, recommend:**

1. **5th Champion Gear:**
   - **Lifesteal** (self-sustain, safe) vs **Relentless** (RNG extra turns, high damage) vs **Toxic** (extra poison) vs **Speed/Accuracy** (standard)
   - **Stalwart** (AoE reduction, helps stun target) vs **Immortal** (high HP sustain)

2. **Existing Champion Gear Changes (if needed):**
   - Geomancer: Currently no set noted (likely Lifesteal or Speed)
   - Mithrala: Currently no set noted
   - Aniri: Currently REGEN (keep or change?)
   - Brogni: Currently BOLSTER (keep or change?)

3. **Stat Priorities:**
   - **All champions:** DEF 4,200+, HP 70k+, ACC 250+ (debuffers), RES 250+ (if using resist strategy), SPD per speed tune
   - **Geomancer:** Crit Rate 100% (ensures HP Burn lands), Crit Damage optional (passive doesn't crit)
   - **Damage dealers:** Crit Rate 100%, Crit Damage 200%+

---

## Simulation Parameters

### Damage Calculation (Simplified)

**Total Damage Sources:**
1. **Geomancer HP Burn Passive:** ~30-40% of total damage (reflects boss damage, triggers Warmaster)
2. **Brogni Shield Passive:** ~15-25% of total damage (shield breaks trigger Warmaster)
3. **Poison Damage:** ~25-35% of total damage (10 poisons = 25% boss MAX HP per turn)
4. **Direct Damage (A1/A2/A3):** ~10-20% of total damage (less significant on UNM)
5. **Debuff Amplification:** Decrease DEF (+60%), Weaken (+25%)

**Estimated Damage Tiers:**
- **S Tier (140M+):** Optimal speed tune, Decrease DEF + Poison + Geo/Brogni passives, minimal deaths
- **A Tier (120M-140M):** Good speed tune, high poison uptime OR high passive procs, 1-2 deaths max
- **B Tier (100M-120M):** Decent speed tune, moderate poison OR passive procs, survivable to turn 50
- **C Tier (80M-100M):** Suboptimal tune, lower damage but still viable for 2-key

### Survivability Factors

1. **Healing/Sustain:** Aniri passive heal, Regen set, Leech, Lifesteal
2. **Damage Reduction:** Decrease ATK (50% less damage), Increase DEF (scales with DEF stat), shields (absorb damage)
3. **Debuff Management:** Block Debuffs (prevent Decrease DEF/Speed/ATK), cleanse (remove debuffs)
4. **Revive:** Aniri (all allies), Arbiter (all allies), Rector Drath (single target), Scyl (single target)
5. **Affinity Safety:** Avoid weak affinity champions in critical roles (debuffers, revivers)

### Speed Tune Validation

**1:1 Speed Tune (171-189 SPD):**
- Boss speed: 170
- Champion speed: 171-189 (goes once per boss turn)
- Turn order: Consistent, safe for AUTO

**2:1 Speed Tune (250-280 SPD, EXACT requirements):**
- Boss speed: 170
- Champion speed: 250-280 (goes twice per boss turn)
- **CRITICAL:** Speed must be EXACT to maintain tune (Spirit boss Decrease Speed can break tune)
- Use DeadwoodJedi calculator: https://www.deadwoodjedi.com/speed-tunes-4/

**Current Team Speeds (NOT optimized for either tune):**
- Mithrala: 241 (too fast for 1:1, too slow for reliable 2:1)
- Brogni: 225 (too fast for 1:1, borderline for 2:1)
- Aniri: 218 (too fast for 1:1, too slow for 2:1)
- Geomancer: 217 (too fast for 1:1, too slow for 2:1)

**Recommendation:** Focus on 1:1 speed tune (171-189 SPD) OR flexible hybrid tune with intentional stun target (slowest at ~175 SPD, others at 220-241 SPD)

---

## Output Format

### Section 1: Top 60 Viable Champions (Filtered List)

**Format:**
| Rank | Champion | Affinity | Role | Key Mechanics | UNM Viability (1-10) |
|------|----------|----------|------|---------------|----------------------|
| 1 | Deacon Armstrong | Force | Decrease DEF | 60% Dec DEF, SPD aura | 10/10 |
| 2 | Fayne | Magic | Poison + Dec DEF | 60% Dec DEF, 4 poisons | 9/10 |
| ... | ... | ... | ... | ... | ... |

### Section 2: Team Simulations (6 Archetypes, 3-5 teams each)

**Format per team:**

```markdown
#### Team X: [Archetype] - [5th Champion Name]

**5-Champion Roster:**
1. [Lead] Champion A (Affinity) - Aura: +33% DEF
2. Champion B (Affinity) - Role
3. Champion C (Affinity) - Role
4. Champion D (Affinity) - Role
5. Champion E (Affinity) - Role

**Speed Tuning:**
- Speed Tune Type: 1:1 (171-189 SPD)
- Turn Order:
  1. Champion A: 185 SPD (applies Decrease DEF first)
  2. Champion B: 180 SPD (applies poisons)
  3. Champion C: 178 SPD (extends buffs)
  4. Champion D: 176 SPD (shields)
  5. Champion E: 175 SPD (STUN TARGET, self-cleanses)

**Stun Target:** Champion E (slowest, passive self-cleanse)

**Stat Requirements:**
- Champion A: 185 SPD, 250 ACC, 4,500 DEF, 70k HP
- Champion B: 180 SPD, 250 ACC, 4,200 DEF, 65k HP
- Champion C: 178 SPD, 150 ACC, 4,000 DEF, 76k HP (REGEN set)
- Champion D: 176 SPD, 150 ACC, 4,500 DEF, 82k HP (BOLSTER set)
- Champion E: 175 SPD, 250 ACC, 4,800 DEF, 75k HP, 100% Crit Rate

**Gear Recommendations:**
- Champion A: Speed + Accuracy (standard debuffer)
- Champion B: Toxic + Speed (extra poison damage)
- Champion C: REGEN (keep existing)
- Champion D: BOLSTER (keep existing)
- Champion E: Lifesteal + Speed (stun target, self-sustain)

**Expected Damage:** 120M-130M (50 turns, AUTO)

**Damage Breakdown:**
- Geomancer HP Burn Passive: 40M (33%)
- Brogni Shield Passive: 25M (21%)
- Poison Damage: 40M (33%)
- Direct Damage: 15M (13%)
- **Total:** 120M

**Strengths:**
- High poison uptime (10 poisons maintained)
- Decrease DEF amplifies all damage (+60%)
- Safe stun target (Champion E self-cleanses)
- High survivability (Decrease ATK, shields, Increase DEF)

**Weaknesses:**
- Lower burst damage (relies on DOTs)
- Affinity risk: Champion B (Magic) weak vs Force boss
- Requires good ACC (250+) on 3 champions

**Affinity Safety:**
- **Spirit (Decrease Speed, stuns slowest):** Safe, Champion E is stun target with self-cleanse
- **Force (Decrease DEF):** Moderate risk, Champion B (Magic) may miss debuffs 15% more often
- **Magic (Block Debuffs):** Safe, high RES on all champions
- **Void (No mechanics):** Safe

**Team Rating:** A Tier (120M-130M expected)
```

### Section 3: Team Summary Table

**Format:**
| Rank | Team Name | Members | Archetype | Damage Range | Rating | Affinity Safety |
|------|-----------|---------|-----------|--------------|--------|-----------------|
| 1 | Poison Focus - Fayne | Geo, Mithrala, Brogni, Aniri, Fayne | Poison + Dec DEF | 130M-140M | S | Void/Spirit: Safe, Force: Moderate |
| 2 | Ally Attack - Nogdar | Geo, Mithrala, Brogni, Aniri, Nogdar | Ally Attack | 125M-135M | A | All: Safe |
| ... | ... | ... | ... | ... | ... | ... |

**Sort by:** Expected Damage (highest to lowest)

### Section 4: Champion Ranking Chart (Top 50)

**Format:**
| Rank | Champion | Affinity | Primary Role | Best Archetype | Teams Used In | Overall Rating (1-10) | Notes |
|------|----------|----------|--------------|----------------|---------------|----------------------|-------|
| 1 | Deacon Armstrong | Force | Decrease DEF | Dec DEF Focus | 12 teams | 10/10 | Best debuffer, SPD aura |
| 2 | Fayne | Magic | Poison + Dec DEF | Poison Focus | 10 teams | 9/10 | Dual-role, high value |
| ... | ... | ... | ... | ... | ... | ... | ... |

**Sort by:** Overall Rating (10/10 to 1/10)

### Section 4B: Eliminated Champions Tables (Footnotes)

**Format (Phase 1 → Phase 2 Elimination, 24 → 16):**
| Rank | Champion | Affinity | Primary Role | Viability Score | Drop Rationale |
|------|----------|----------|--------------|-----------------|----------------|
| 17 | Champion A | Force | Poison | 6.5/10 | Low poison uptime, outclassed by Fayne/Venomage |
| 18 | Champion B | Magic | Dec DEF | 6.2/10 | Lower ACC than Deacon, weaker aura |
| ... | ... | ... | ... | ... | ... |

**Format (Phase 2 → Phase 3 Elimination, 16 → 8):**
| Rank | Champion | Affinity | Primary Role | Viability Score | Drop Rationale |
|------|----------|----------|--------------|-----------------|----------------|
| 9 | Champion C | Spirit | Ally Attack | 7.8/10 | Good but lower damage than Nogdar, longer CD |
| 10 | Champion D | Void | Shield | 7.5/10 | Solid survivability but lower damage output |
| ... | ... | ... | ... | ... | ... |

### Section 5: Final Recommendations

**Top 3 Teams (Summary):**
1. **Team Name:** [Best team from simulations]
   - **Expected Damage:** XM-YM
   - **Why:** [Rationale for best overall]
   - **Gear/Stat Investments:** [What needs to change from current setup]

2. **Team Name:** [Second best]
   - [Same format]

3. **Team Name:** [Third best]
   - [Same format]

**Next Steps:**
1. [Action item 1 - e.g., "Regear Geomancer to 175 SPD for stun target"]
2. [Action item 2 - e.g., "Book Fayne A2/A3 for poison uptime"]
3. [Action item 3 - e.g., "Test Team 1 on Spirit boss first"]

---

## Fast Processing Template (Optimized for Speed)

### Simplified Simulation (Per Team)

**Step 1: Speed Tune Validation**
- Is team 1:1 (171-189 SPD)? YES/NO
- Is team 2:1 (250-280 SPD)? YES/NO
- Is stun target optimized? YES/NO

**Step 2: Damage Estimation**
- Geo HP Burn Passive: [% of total damage]
- Brogni Shield Passive: [% of total damage]
- Poison Damage: [% of total damage]
- Direct Damage: [% of total damage]
- **Total Estimated Damage:** [XM]

**Step 3: Survivability Check**
- Decrease ATK uptime: [%]
- Increase DEF uptime: [%]
- Shield uptime: [%]
- Revive available: YES/NO
- **Survivability Rating:** HIGH/MEDIUM/LOW

**Step 4: Affinity Safety**
- Spirit boss: SAFE/MODERATE/RISKY
- Force boss: SAFE/MODERATE/RISKY
- Magic boss: SAFE/MODERATE/RISKY
- Void boss: SAFE

**Step 5: Team Rating**
- Damage: S/A/B/C
- Survivability: S/A/B/C
- Affinity Safety: S/A/B/C
- **Overall Rating:** S/A/B/C

---

## Analysis Approach - CONFIRMED USER PREFERENCES

### **PHASE 0: Optimize Current 4-Champion Speed Tuning (BASELINE)**

**Before analyzing 5th champion options:**
- **VALIDATE (UNM-relevant only):** 
  - Extract UNM sections from champion reviews: Godseeker Aniri, Underpriest Brogni (Section 2 ratings, Section 3 skills, Section 4 gear, Section 5 masteries)
  - fetch_webpage from Ayumilove for Geomancer + Mithrala Lifebane
  - Cross-validate with HellHades/RaidHQ (second source)
  - Output: Condensed bullet points per champion
- Build quick reference table: Skills, Buffs/Debuffs, Synergies, Recommended Gear/Masteries
- Evaluate 3 speed tuning options: 1:1 (171-189 SPD), 2:1 (250-280 SPD), Hybrid (current range optimized)
- Analyze gear change requirements for each option
- Recommend baseline speed tune that maximizes damage + survivability + flexibility for 5th champion
- Output: Speed tuning recommendation table with gear change analysis + validated skill quick reference

### **Progressive Filtering: 24 → 16 → 8**

**Phase 1: Top 24 Champions (Initial Filter)**
- **Selection Method:** Curated UNM meta + grep_search for key mechanics (Option C)
- **Optimization:** Prioritize known UNM performers (Fayne, Deacon, Venomage, etc.), fill gaps with grep_search results
- **Archetype Balance:** Loose balance (~2-5 per archetype, prioritize high-value archetypes like Poison/Dec DEF)
- **Duplicates:** Count unique champions only (Rector Drath x2 = 1 entry, most duplicates not built for UNM)

**Phase 2: Basic Testing (24 → 16)**
- **Team Count:** 1-2 teams per champion (~30-35 teams total, optimize as able)
- **Reduction Criteria:** Damage + Survivability + Affinity Safety score (eliminate lowest 8)
- **Output:** Short table of eliminated 8 champions with drop rationale as footnote

**Phase 3: Final Selection (16 → 8)**
- **Format:** 8 champion/team/archetype combinations (e.g., "Fayne Poison Focus", "Deacon Dec DEF Focus")
- **Deep-dive analysis:** Full stats, gear, speed tuning, stun target optimization

### **Batch Processing (4 Updates)**

**UPDATE 0: Optimize Current 4-Champion Speed Tuning (BASELINE)**
- **STEP 1: VALIDATE SKILLS/MECHANICS (FIRST ACCESS ONLY)**
  - **Validation Depth:** UNM-relevant only (debuffs, buffs, passives, key synergies) - FOCUSED approach
  - **Champion Review Files (if exist):** Extract UNM sections only (Section 2 ratings, Section 3 skills, Section 4 gear, Section 5 masteries)
    - Read `Notes/Champion Reviews/Godseeker_Aniri_Review_DRAFT.md` (extract UNM sections)
    - Read `Notes/Champion Reviews/Underpriest_Brogni_Review_DRAFT.md` (extract UNM sections)
  - **Online Search (for missing champions):** fetch_webpage from Ayumilove + cross-validate with HellHades/RaidHQ
    - Geomancer: Ayumilove + HellHades validation
    - Mithrala Lifebane: Ayumilove + HellHades validation
  - **Output Format:** Condensed bullet points per champion (compact, easy to review)
  - Build validated quick reference table: Skills, Buffs/Debuffs, Synergies, Gear/Masteries
- **STEP 2: ANALYZE CURRENT TEAM GAPS**
  - Document buffs/debuffs provided by current 4 champions
  - Identify critical gaps (Decrease DEF, Poison, Decrease ATK, etc.)
  - Note synergies (Brogni shields + Aniri extension, Geo HP Burn + Aniri extension)
- **STEP 3: SPEED TUNING OPTIMIZATION**
  - Analyze 3 speed tuning options (1:1, 2:1, Hybrid)
  - Recommend baseline speed tune with gear change requirements
  - Test current 4-champion team (no 5th) to establish baseline damage/survivability

**UPDATE 1: Filter to Top 24 + Basic Testing → Eliminate to Top 16**
- grep_search owned list for UNM-viable mechanics
- Curate Top 24 (meta + grep results)
- Run basic simulations (~30-35 teams) using recommended baseline speed tune
- Eliminate to Top 16 with drop rationale table

**UPDATE 2: Detailed Simulations on Top 16 → Eliminate to Top 8**
- Run detailed simulations on Top 16 (~20-25 teams)
- Optimize speed tuning, stun target, gear
- Eliminate to Top 8 with drop rationale table

**UPDATE 3: Final Top 8 Deep-Dive + Summary Tables**
- Full analysis of Top 8 champion/team/archetype combinations
- Team summary table (all tested teams ranked)
- Champion ranking chart
- Final recommendations

### **Damage Estimation**

**Primary Method:** Simplified estimation (% breakdown of Geo/Brogni/Poison/Direct damage) - FAST
- Geo HP Burn Passive: ~30-40%
- Brogni Shield Passive: ~15-25%
- Poison Damage: ~25-35%
- Direct Damage: ~10-20%
- Debuff Amplification: Decrease DEF (+60%), Weaken (+25%)

**Secondary Method (Future Phase):** Turn-by-turn simulation for FAVORITES after Top 8 identified
- Favorites: Michelangelo, Embrys, Arbiter, Deacon (Relentless, 175 ACC), other top options
- Note: Ninja excluded (anti-synergy with Geomancer - both apply HP Burn, passive doesn't stack)
- Goal: Get past 80M once to unlock quick battle for AUTO farming

### **Speed Tuning Approach**

**Primary:** Optimize around current speed range (217-241 SPD) - hybrid/flexible tune
**Secondary:** Assess viability of 1:1 (171-189 SPD) and 2:1 (250-280 SPD) tunes
**Consider:** Pairing with speed buffers (Arbiter, High Khatun, Seeker) if beneficial

### **Affinity Mechanics (Validate Online)**

**Boss Affinity Rotation:** Void → Spirit → Force (GREEN, current) → Magic

**Affinity-Specific Mechanics:**
- **Weak Hits:** Weak affinity champions deal 30% less damage, 15% lower debuff accuracy
- **Strong Hits:** Strong affinity champions deal 30% more damage, 15% higher debuff accuracy
- **Crit Rate:** Weak affinity reduces crit rate by 15%
- **Accuracy:** Weak affinity debuffers need +15 ACC to compensate

**Current Boss (Force/GREEN):**
- Geomancer (Magic): WEAK - 30% less damage, 15% lower ACC/Crit
- Brogni (Magic): WEAK - 30% less damage, 15% lower ACC/Crit
- Mithrala (Spirit): SAFE - Neutral affinity vs Force
- Aniri (Void): SAFE - No affinity mechanics

**Optimization Goal:** Get past 80M on ANY affinity once (unlocks quick battle), then optimize per affinity

### **Gear Change Tolerance**

**Approach:** Consider current gear/stats → ideal gear transitions
- Evaluate: Can ideal sets maintain/improve current stats?
- Hypothesis: Estimate damage/survivability improvement with ideal gear
- Minimize changes: Only adjust 5th champion + minor tweaks to existing 4 unless major gain

**Current Gear:**
- Geomancer: Unknown (likely Lifesteal or Speed)
- Mithrala: Unknown
- Godseeker Aniri: REGEN (keep unless major benefit to change)
- Brogni: BOLSTER (keep unless major benefit to change)

### **Godseeker Aniri Replacement Testing**

**When:** Only for Top 8-10 teams (after Phase 2 complete)
**Alternatives:** Arbiter, Rector Drath, Scyl, Tagoar
**Note:** Tagoar "not that great but might work well with gear from another reviver" - test if Top 8 worthy
