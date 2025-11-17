# UNM Clan Boss - Leonardo Unkillable Team

**Date**: 2025-11-16  
**Version**: 3.0 - Streamlined Structure  
**Status**: FUTURE BUILD (requires 7 Legendary books on Leonardo)  
**Performance Target**: 70-95M (manual), 50-70M (auto)  
**Speed Tune**: 3:2 (263-280 SPD)

**Related Documentation:**
- **Reference Guide:** `UNM_Clan_Boss_Team_Analysis.md` (mechanics, speed tuning, troubleshooting)
- **Current Team:** `UNM CB Guide update.md` (Tanky Killable 3:2)

---

## Table of Contents

- [UNM Clan Boss - Leonardo Unkillable Team](#unm-clan-boss---leonardo-unkillable-team)
  - [Table of Contents](#table-of-contents)
  - [1. Team Overview](#1-team-overview)
    - [1.1 Team Philosophy \& Comparison](#11-team-philosophy--comparison)
    - [1.2 Speed Tune \& Roster](#12-speed-tune--roster)
    - [1.3 Core Mechanics \& Rotation](#13-core-mechanics--rotation)
    - [1.4 Damage Projections](#14-damage-projections)
  - [2. Champion Builds (Verified Stats)](#2-champion-builds-verified-stats)
  - [3. Usage Guide](#3-usage-guide)
    - [3.1 Manual Rotation (4-Turn Cycle)](#31-manual-rotation-4-turn-cycle)
    - [3.2 Auto Mode Setup](#32-auto-mode-setup)
    - [3.3 Critical Timing Notes](#33-critical-timing-notes)
  - [4. Alternate Champions \& Variants](#4-alternate-champions--variants)
    - [4.1 Auto-Safe Variant (Mithrala)](#41-auto-safe-variant-mithrala)
    - [4.2 Affinity Replacements](#42-affinity-replacements)
  - [5. Build Timeline \& Resource Requirements](#5-build-timeline--resource-requirements)
  - [6. Quick Reference Tables](#6-quick-reference-tables)
    - [6.1 Team Snapshot](#61-team-snapshot)
    - [6.2 Speed Tune Quick Check](#62-speed-tune-quick-check)
    - [6.3 Build Checklist](#63-build-checklist)
    - [6.4 Troubleshooting Quick Reference](#64-troubleshooting-quick-reference)
    - [Godseeker Aniri (CRITICAL - Buff Extension)](#godseeker-aniri-critical---buff-extension)
    - [Michelangelo (HIGH - Join Attack DPS)](#michelangelo-high---join-attack-dps)
    - [Underpriest Brogni (CRITICAL - Gap Coverage)](#underpriest-brogni-critical---gap-coverage)
    - [Geomancer (HIGH - Damage Multiplier + Stun Target)](#geomancer-high---damage-multiplier--stun-target)
  - [7. Manual Rotation Guide](#7-manual-rotation-guide)
    - [Turn-by-Turn Execution (First 4 Boss Turns)](#turn-by-turn-execution-first-4-boss-turns)
    - [Critical Manual Timing](#critical-manual-timing)
  - [8. Auto Mode: Mithrala Variant](#8-auto-mode-mithrala-variant)
    - [Why Swap Godseeker for Mithrala?](#why-swap-godseeker-for-mithrala)
    - [Auto Team Composition](#auto-team-composition)
  - [9. Build Timeline \& Resource Requirements](#9-build-timeline--resource-requirements)
    - [Phase 1: Book Farming (Months 1-3)](#phase-1-book-farming-months-1-3)
    - [Phase 2: Regearing (Weeks 1-2)](#phase-2-regearing-weeks-1-2)
    - [Phase 3: Mastery Completion (Weeks 1-2)](#phase-3-mastery-completion-weeks-1-2)
    - [Total Timeline: 3-4 Months](#total-timeline-3-4-months)
  - [10. Troubleshooting](#10-troubleshooting)
    - [Problem 1: Leonardo Unkillable Only 2 Turns](#problem-1-leonardo-unkillable-only-2-turns)
    - [Problem 2: Speed Tune Breaking](#problem-2-speed-tune-breaking)
    - [Problem 3: Low Damage (30-40M instead of 70M+)](#problem-3-low-damage-30-40m-instead-of-70m)
    - [Problem 4: Team Dies During Gap Turn](#problem-4-team-dies-during-gap-turn)
    - [Problem 5: Run Ends at Turn 50](#problem-5-run-ends-at-turn-50)
  - [Quick Reference: Build Checklist](#quick-reference-build-checklist)

---

## 1. Team Overview

### 1.1 Team Philosophy & Comparison

**Core Mechanic:** Leonardo A2 (Unkillable 2 turns + Counterattack) extended by Godseeker A2 (+1 turn) = 3-turn Unkillable (75% uptime in 4-turn cycle).

**vs Tanky Killable Team:**

| Aspect | Tanky Killable | Leonardo Unkillable |
|--------|----------------|---------------------|
| **Damage** | 40-55M (68M peak) | 70-95M manual, 50-70M auto |
| **Books** | Brogni only | 3 Legendaries (Leo, Mickey, Geo) |
| **Turn Limit** | 60-80 turns | 50 turns (hard cap) |
| **Auto Viable** | ✅ 90% | ⚠️ 60% (needs Mithrala) |
| **Affinity** | Safe all bosses | ⚠️ Weak on Force |
| **Difficulty** | Medium | High |
| **Investment** | Low | Very High (20+ Legendary books) |

**When to Build:**
1. ✅ Tanky Killable hitting 72M+ (1-key secured)
2. ✅ Leonardo fully booked (7 books)
3. ✅ Godseeker fully booked (Epic)
4. ✅ Mickey & Geo regeared to 263-280 SPD

**Why Leonardo > Tanky:**
- Counterattack: 4-hit Leonardo A1 + Mickey joins (6-8 hits per boss turn)
- Glass cannon builds: Unkillable allows 100% C.RATE, 250%+ C.DMG focus
- Damage ceiling: 75% increase vs Tanky Killable

**Why NOT Leonardo (current):**
- ❌ 7 Legendary books on Leonardo (A2 5→3 CD MANDATORY)
- ❌ Mickey +25 SPD, Geo +39 SPD regear needed
- ❌ Manual-dependent (Godseeker AI terrible)
- ❌ Turn 50 hard limit (Tanky can survive 60-80 turns)

---

### 1.2 Speed Tune & Roster

**Speed Tune:** 3:2 (263-280 SPD, NO speed lead)  
**Boss SPD:** 170 (post-turn 1)  
**Reference:** See `UNM_Clan_Boss_Team_Analysis.md` Section 3 for 3:2 mechanics

**Manual Team (Max Damage):**

| Champion | SPD | Role | Current | Needs |
|----------|-----|------|---------|-------|
| **Godseeker Aniri** | 277 | Buff Extension | ✅ READY | - |
| **Underpriest Brogni** | 274 | Block Debuffs/Shield | ✅ READY | - |
| **Michelangelo** | 270 | Join Attack DPS | 245 SPD | +25 SPD |
| **Leonardo** | 267 | Unkillable/Tank | Not built | Full build |
| **Geomancer** | 263 | Weaken/HP Burn/Stun | 224 SPD | +39 SPD |

**Auto Team (Reliability):**
- Replace **Godseeker** → **Mithrala** (SPD 277)
- Keep all others same
- Trade-off: -20-25M damage, +30% success rate

---

### 1.3 Core Mechanics & Rotation

**4-Turn Cycle:**

| Boss Turns | Leonardo Status | Coverage | Hits per Turn |
|------------|----------------|----------|---------------|
| **1-3** | ✅ Unkillable (3 turns w/ Godseeker) | Counterattack active | 6-8 hits |
| **4** | ❌ Gap turn | Brogni Block Debuffs | Normal rotation |

**Key Skills:**
- **Leonardo A2:** Unkillable (2 turns) + Counterattack + Ally Protection + Inc DEF (5→3 CD w/ books)
- **Godseeker A2:** Extends ALL buffs +1 turn (4→3 CD w/ books)
- **Brogni A3:** Block Debuffs (2 turns) + Shield 30% MAX HP (5→3 CD w/ books)
- **Geomancer A3:** Weaken 25% + HP Burn (5→3 CD w/ books)
- **Mickey Passive:** Joins all Turtle attacks (Leonardo/Donatello/Mickey/Raphael)

**Rotation Pattern:**
1. **Round 1:** Leonardo A2 → Brogni A3 → Geo A3 → Others A1
2. **Round 2:** Godseeker A2 (extend!) → All A1
3. **Rounds 3-6:** All A1 (Leonardo Unkillable active)
4. **Round 7:** Leonardo A2 (refresh) → Brogni A3 (gap coverage) → All A1
5. **Round 8:** Godseeker A2 (extend!) → All A1
6. **Repeat** for 50 turns (12.5 cycles)

---

### 1.4 Damage Projections

**Manual Team (Godseeker):**
- Baseline: 70-80M (neutral affinity, optimal rotation)
- Peak: 85-95M (Void boss, perfect RNG)
- Low: 60-70M (weak affinity or rotation errors)

**Auto Team (Mithrala):**
- Baseline: 50-60M (Leonardo 50% Unkillable uptime)
- Peak: 65-70M (Void boss, good RNG)
- Success Rate: 90-95% (cleanse safety)

---

## 2. Champion Builds (Verified Stats)

| Champion | SPD | HP | DEF | ATK | C.RATE | C.DMG | ACC | Books | Mastery | Priority |
|----------|-----|----|----|-----|--------|-------|-----|-------|---------|----------|
| **Leonardo** | 267 | 50k | **3,500** | - | 100% | 200% | 100 | 7 Leg (A2 5→3) | Warmaster | 5/5 |
| **Godseeker** | 277 | 60k | **4,500** | - | 70% | - | 150 | Full Epic (A2 4→3) | Warmaster | 5/5 |
| **Michelangelo** | 270 | - | - | **4,000** | 100% | 200% | 200 | Full Leg | Giant Slayer | 5/5 |
| **Brogni** | 274 | **60k** | 3,500 | - | - | - | 250 | Full Leg (A3 5→3) | Warmaster | 5/5 |
| **Geomancer** | 263 | 40k | 2,500 | - | 100% | - | **250** | Full Leg (A3 5→3) | Giant Slayer | 5/5 |

**Critical Stats (Bold):**
- **Leonardo:** DEF 3,500+ (damage scaling + tank role)
- **Godseeker:** DEF 4,500+ (takes Ally Protection damage)
- **Michelangelo:** ATK 4,000+ (join attack damage)
- **Brogni:** HP 60k+ (shield scaling 30% MAX HP)
- **Geomancer:** ACC 250+ (Weaken MUST land)

**Key Skills:**
- **Leonardo A1:** 2-hit DEF scaling, repeats on counter (4 total hits)
- **Leonardo A2:** Unkillable 2 turns + Counterattack + Ally Prot + Inc DEF (5→3 CD)
- **Godseeker A2:** Extends ALL buffs +1 turn, heals 15% MAX HP (4→3 CD)
- **Mickey Passive:** Joins Turtle attacks + shield 300% ATK when hit
- **Brogni A3:** Block Debuffs 2 turns + Shield 30% MAX HP (5→3 CD)
- **Geo A3:** Weaken 25% + HP Burn 3 turns (5→3 CD)
- **Geo Passive:** Reflects 30% damage as HP Burn, -15% boss damage

**Gear Priority:**
- **All:** Speed boots (6★), Speed set (4pc)
- **Leonardo:** Speed + Immortal/DEF
- **Godseeker:** Speed + Immortal
- **Mickey:** Speed + Cruel/Savage (Ignore DEF)
- **Brogni:** Speed + Immortal
- **Geo:** Speed + Perception/Accuracy

**Current Status:**
- ✅ Godseeker: READY (SPD 277, fully booked)
- ✅ Brogni: READY (SPD 274, fully booked)
- ❌ Leonardo: NOT BUILT (needs 7 Legendary books, 267 SPD, 3,500 DEF)
- ❌ Mickey: NEEDS +25 SPD (currently 245 SPD)
- ❌ Geo: NEEDS +39 SPD (currently 224 SPD)

---

## 3. Usage Guide

### 3.1 Manual Rotation (4-Turn Cycle)

**Critical Manual Timing:**

| Round | Leonardo | Godseeker | Brogni | Geo | Others |
|-------|----------|-----------|--------|-----|--------|
| **1** | **A2** (Unkillable!) | A1/A3 | **A3** (Block Debuffs) | **A3** (Weaken) | A1 |
| **2** | A1 | **A2** (EXTEND!) | A1 | A1 | A1 |
| **3-6** | A1 | A1 | A1 | A1 | A1 |
| **7** | **A2** (Refresh) | A1 | **A3** (Gap cover) | A1/A3 | A1 |
| **8** | A1 | **A2** (EXTEND!) | A1 | A1 | A1 |

**DO:**
- ✅ Godseeker A2 on Rounds 2, 8, 14, 20... (immediately after Leonardo A2)
- ✅ Leonardo A2 on Rounds 1, 7, 13, 19... (every 4 rounds)
- ✅ Brogni A3 on Rounds 1, 7, 13, 19... (gap turn coverage)
- ✅ Geo A3 on Round 1, then every 3 turns (maintain Weaken uptime)

**DON'T:**
- ❌ Use Godseeker A2 before Leonardo A2 (wastes extension)
- ❌ Miss Brogni A3 on gap turn (Decrease Speed breaks tune)
- ❌ Let Geomancer Weaken drop (25% damage loss)

**Damage per Turn:** ~2.5-3M (counterattacks + HP Burn + Warmaster/GS procs)  
**Total 50 Turns:** ~125-150M potential → Realistic 70-95M (RNG, affinity, rotation errors)

---

### 3.2 Auto Mode Setup

**Problem:** Godseeker AI uses A2 at wrong times (50% Unkillable uptime instead of 75%)

**Solution:** Replace Godseeker → Mithrala (SPD 277)

**Auto Team Changes:**

| Swap | From | To | Impact |
|------|------|-----|--------|
| Buff Extension | Godseeker | Mithrala | -25% Unkillable uptime (75%→50%) |
| Survivability | Revive | Cleanse + Shield | +30% success rate (recovers from Dec SPD) |
| Damage | 70-95M | 50-70M | -20-25M damage |

**Auto Performance:**
- Expected: 50-70M damage
- Success Rate: 90-95%
- Turn Survival: 50 turns consistent

---

### 3.3 Critical Timing Notes

**Buff Extension Timing:**
- Godseeker A2 MUST be used Round 2, 8, 14, 20... (immediately after Leonardo A2)
- If used wrong: Leonardo Unkillable only 2 turns (gap turn wipe)

**Gap Turn Coverage:**
- Boss Turn 4, 8, 12... = Leonardo Unkillable OFF
- Brogni A3 Block Debuffs MUST cover these turns
- If missed: Decrease Speed lands → speed tune breaks → wipe

**Weaken Uptime:**
- Geomancer A3 every 3 turns (Rounds 1, 4, 7, 10...)
- If missed: 25% damage loss (Weaken 1.25× multiplier)

---

## 4. Alternate Champions & Variants

### 4.1 Auto-Safe Variant (Mithrala)

**Team:** Leonardo + **Mithrala** + Michelangelo + Brogni + Geomancer

**Why Mithrala:**
- ✅ A3 Cleanse (recovers from Decrease Speed)
- ✅ A3 Shield 30% MAX HP + Strengthen
- ✅ AI uses skills correctly (auto-friendly)
- ❌ NO Buff Extension (Leonardo 2-turn Unkillable = 50% uptime)

**Build:** SPD 277, DEF 4,000+, ACC 250+, HP 50k+

**Performance:**
- Damage: 50-70M (auto, 90% success)
- vs Manual: -20-25M damage, +30% reliability

---

### 4.2 Affinity Replacements

**Force Boss (Leonardo Void = Weak):**
- **Problem:** Leonardo -30% damage (Void weak to Force)
- **Solution:** Wait for Void/Spirit/Magic rotation OR
- **Replace:** Roshcard the Tower (Force, Block Damage 3 turns) if owned
  - SPD: 264-270 (replaces Leonardo as Unkillable provider)

**Magic Boss (Brogni Force = Weak):**
- **Problem:** Brogni shield reduced (Force weak to Magic)
- **Solution:** Increase Brogni HP to 70k+ (compensate) OR
- **Replace:** Warlord (Void, Block Damage 3 turns) if owned

**Affinity Performance:**

| Boss Affinity | Expected Damage | Notes |
|---------------|-----------------|-------|
| **Void** | 85-95M | Best (all neutral) |
| **Spirit** | 80-90M | Leonardo strong (+30%) |
| **Force** | 50-65M | Leonardo weak (-30%) ⚠️ |
| **Magic** | 70-85M | Brogni weak (shield -20%) |

---

## 5. Build Timeline & Resource Requirements

**Phase 1: Book Farming (Months 1-3)**

| Champion | Books Needed | Priority | Timeline |
|----------|--------------|----------|----------|
| **Leonardo** | 7 Legendary (A2 5→3) | 5/5 CRITICAL | 2-3 months |
| **Godseeker** | Full Epic | ✅ DONE | - |
| **Michelangelo** | Full Legendary | 4/5 Recommended | 1-2 months |
| **Geomancer** | Full Legendary (A3 5→3) | 4/5 Recommended | 1-2 months |

**Phase 2: Regearing (Weeks 1-2)**

| Champion | Current SPD | Target SPD | Change Needed |
|----------|-------------|------------|---------------|
| Michelangelo | 245 | 270 | +25 SPD (Speed boots + set) |
| Geomancer | 224 | 263 | +39 SPD (Speed boots + set + subs) |
| Leonardo | 0 | 267 | Full build (Speed + DEF) |

**Phase 3: Masteries (Weeks 1-2)**

- Leonardo: Warmaster (DEF scaling)
- Michelangelo: Giant Slayer (A1 2-hit)
- Geomancer: Giant Slayer (A1 2-hit)

**Total Timeline:** 3-4 months  
**Resource Cost:**
- Books: 20-22 Legendary total
- Energy: 5,000-10,000 (gear + masteries)
- Silver: 50-100M (gear upgrades)

**Milestones:**
- **Month 1-2:** Farm Leonardo books (highest priority)
- **Month 2-3:** Farm Mickey + Geo books
- **Month 3:** Regear all champions to 263-280 SPD
- **Month 4:** Mastery completion + testing

---

## 6. Quick Reference Tables

### 6.1 Team Snapshot

| Metric | Manual (Godseeker) | Auto (Mithrala) |
|--------|-------------------|-----------------|
| **Damage** | 70-95M | 50-70M |
| **Unkillable Uptime** | 75% (3/4 turns) | 50% (2/4 turns) |
| **Success Rate** | 60% (AI issues) | 90-95% |
| **Turn Limit** | 50 (hard cap) | 50 (hard cap) |
| **Affinity Safe** | Void/Spirit/Magic | All (cleanse safety) |

---

### 6.2 Speed Tune Quick Check

**All Champions: 263-280 SPD (NO speed lead)**

| Champion | Target | Status | Needs |
|----------|--------|--------|-------|
| Godseeker | 277 | ✅ READY | - |
| Brogni | 274 | ✅ READY | - |
| Mickey | 270 | ❌ 245 SPD | +25 SPD |
| Leonardo | 267 | ❌ Not built | Full build |
| Geo | 263 | ❌ 224 SPD | +39 SPD |

**Turn Order:** Godseeker (fastest) → Brogni → Mickey → Leonardo → Geo (slowest, stun target)

---

### 6.3 Build Checklist

**BEFORE STARTING:**
- [ ] Tanky Killable hitting 72M+ (1-key secured)
- [ ] Leonardo: 7 Legendary books acquired
- [ ] Leonardo: 267 SPD, 3,500 DEF, 100% C.RATE, Warmaster
- [ ] Godseeker: Fully booked ✅ (already complete)
- [ ] Michelangelo: 270 SPD (+25 from current), 100% C.RATE, Giant Slayer
- [ ] Geomancer: 263 SPD (+39 from current), 250 ACC, 100% C.RATE, Giant Slayer
- [ ] Brogni: Fully booked ✅ (already complete)
- [ ] 3-5 test runs completed (manual rotation verified)
- [ ] Mithrala variant tested (if auto needed)

---

### 6.4 Troubleshooting Quick Reference

| Problem | Symptoms | Fix |
|---------|----------|-----|
| **Unkillable Only 2 Turns** | Leonardo shows 2 turns vs 3 | Godseeker A2 Round 2/8/14 (after Leo A2) |
| **Speed Tune Breaking** | Boss laps team after ~10 turns | Verify 263-280 SPD, remove speed leads |
| **Low Damage (30-40M)** | Half expected damage | Geo ACC 250+, 100% C.RATE all DPS, check affinity |
| **Team Dies Gap Turn** | Wipe on Turn 4/8/12 | Brogni A3 on gap turns, Leo DEF 3,500+ |
| **Run Ends Turn 50** | Sudden wipe at turn 50 | EXPECTED (Gathering Fury), accept limit |

---

**Verdict:** Build Leonardo team AFTER Tanky Killable hits 72M+ (1-key secured). Requires 3-4 months book farming + regearing. Manual-dependent for max damage (70-95M), auto variant (Mithrala) provides 50-70M reliable damage.

**END OF GUIDE - Version 3.0**

**Base Stats:** HP 16,845 / DEF 1,619 / SPD 101  
**Skills:** A1 (2-hit DEF scaling, repeats on counter = 4 hits), A2 (Unkillable 2 turns + Counterattack + Ally Protection + Inc DEF, 5→3 turn CD with books)

| Stat | Target | Priority | Notes |
|------|--------|----------|-------|
| **SPD** | 267 | 5/5 | 264-270 acceptable |
| **DEF** | 3,500+ | 5/5 | Damage scaling + tank role |
| **C.RATE** | 100% | 5/5 | Warmaster procs |
| **C.DMG** | 200%+ | 4/5 | After C.RATE capped |
| **HP** | 50,000+ | 3/5 | Survivability baseline |

**Books:** 7 Legendary books (A2 5→3 turn CD is MANDATORY - tune breaks without full books)  
**Mastery:** Warmaster (DEF scaling damage)  
**Gear:** Speed (4pc) + Immortal/DEF (2pc)

---

### Godseeker Aniri (CRITICAL - Buff Extension)

**Base Stats:** HP 15,195 / DEF 1,244 / SPD 99  
**Skills:** A2 (Extends ALL buffs +1 turn, heals 15% MAX HP, 4→3 turn CD with books)

| Stat | Target | Priority | Notes |
|------|--------|----------|-------|
| **SPD** | 277 | 5/5 | 274-280 acceptable, FASTEST |
| **DEF** | 4,500+ | 5/5 | Takes Ally Protection damage |
| **HP** | 60,000+ | 4/5 | A2 heal scaling |
| **C.RATE** | 70%+ | 2/5 | Support role, low priority |

**Books:** Full Epic books (A2 4→3 turn CD is MANDATORY)  
**Mastery:** Warmaster OR Lasting Gifts (buff extension on ally death)  
**Gear:** Speed (4pc) + Immortal (2pc)

**Current Status:** ✅ READY (SPD 277, fully booked)

---

### Michelangelo (HIGH - Join Attack DPS)

**Base Stats:** HP 15,360 / ATK 1,520 / SPD 99  
**Skills:** A1 (2-hit ATK scaling), Passive (Joins Turtle attacks + shield)

| Stat | Target | Priority | Notes |
|------|--------|----------|-------|
| **SPD** | 270 | 5/5 | 267-274 acceptable |
| **ATK** | 4,000+ | 5/5 | Join attack damage + shield scaling |
| **C.RATE** | 100% | 5/5 | Giant Slayer procs |
| **C.DMG** | 200%+ | 4/5 | After C.RATE capped |
| **ACC** | 200+ | 3/5 | A2 Decrease DEF + Stun |

**Books:** Full Legendary books (A2 CD reduction + Passive shield CD)  
**Mastery:** Giant Slayer (A1 is 2-hit multi-hit)  
**Gear:** Speed (4pc) + Cruel/Savage (Ignore DEF)

**Current Status:** ❌ NEEDS +25 SPD (currently 245 SPD)

---

### Underpriest Brogni (CRITICAL - Gap Coverage)

**Base Stats:** HP 22,965 / DEF 1,266 / SPD 100  
**Skills:** A3 (Block Debuffs 2 turns + Shield 30% MAX HP, 5→3 turn CD with books)

| Stat | Target | Priority | Notes |
|------|--------|----------|-------|
| **SPD** | 274 | 5/5 | 270-277 acceptable |
| **HP** | 60,000+ | 5/5 | Shield scaling 30% MAX HP |
| **DEF** | 3,500+ | 4/5 | Survivability |
| **ACC** | 250+ | 3/5 | A1 HP Burn |

**Books:** Full Legendary books (A3 5→3 turn CD is MANDATORY)  
**Mastery:** Warmaster + Shield Bearer (increases HP for shield scaling)  
**Gear:** Speed (4pc) + Immortal (2pc)

**Current Status:** ✅ READY (SPD 274, fully booked)

---

### Geomancer (HIGH - Damage Multiplier + Stun Target)

**Base Stats:** HP 18,165 / DEF 1,134 / SPD 94  
**Skills:** A3 (Weaken 25% + HP Burn 3 turns, 5→3 turn CD with books), Passive (Reflects 30% damage as HP Burn)

| Stat | Target | Priority | Notes |
|------|--------|----------|-------|
| **SPD** | 263 | 5/5 | 263-266 acceptable, SLOWEST |
| **ACC** | 250+ | 5/5 | Weaken MUST land |
| **C.RATE** | 100% | 5/5 | Giant Slayer procs |
| **DEF** | 2,500+ | 3/5 | Stun target survivability |
| **HP** | 40,000+ | 3/5 | Survivability baseline |

**Books:** Full Legendary books (A3 5→3 turn CD)  
**Mastery:** Giant Slayer + Master Hexer (extends debuffs, A1 is 2-hit)  
**Gear:** Speed (4pc) + Perception/Accuracy (2pc)

**Current Status:** ❌ NEEDS +39 SPD (currently 224 SPD)

---

## 7. Manual Rotation Guide

### Turn-by-Turn Execution (First 4 Boss Turns)

**BOSS TURN 1:**

**Champion Round 1:**
1. Leonardo: A2 (Unkillable + Counterattack + Ally Protection + Inc DEF!)
2. Brogni: A3 (Block Debuffs + Shield)
3. Geomancer: A3 (Weaken + HP Burn)
4. Michelangelo: A1
5. Godseeker: A1 or A3 (if needed)

**Boss attacks:** Leonardo counterattacks (4 hits), Michelangelo joins (~2-4 hits) = 6-8 hits

**Champion Round 2:**
1. Godseeker: **A2 (EXTEND UNKILLABLE 2→3 TURNS!)**
2. All others: A1

**Damage:** ~2.5-3M (counterattacks + HP Burn + Warmaster/GS procs)

---

**BOSS TURNS 2-3:**

**All champions:** A1 spam (Leonardo Unkillable still active 3 turns total)  
**Boss attacks:** Leonardo counterattacks (4 hits per turn), Michelangelo joins (~2-4 hits per turn)

**Damage per turn:** ~2.5-3M

---

**BOSS TURN 4: GAP TURN**

**Champion Round 7:**
1. Leonardo: **A2 (REFRESH UNKILLABLE!)**
2. Brogni: **A3 (BLOCK DEBUFFS - CRITICAL FOR GAP COVERAGE)**
3. All others: A1

**Champion Round 8:**
1. Godseeker: **A2 (EXTEND!)**
2. All others: A1

**Damage:** ~2.5-3M

---

**CYCLE REPEATS** for 50 boss turns (12.5 cycles)

---

### Critical Manual Timing

**DO:**
- ✅ Godseeker A2 on Rounds 2, 8, 14, 20... (immediately after Leonardo A2)
- ✅ Leonardo A2 on Rounds 1, 7, 13, 19... (every 4 rounds = 3-turn CD + 1 turn active)
- ✅ Brogni A3 on Rounds 1, 7, 13, 19... (gap turn coverage)
- ✅ Geomancer A3 on Round 1, then every 3 turns

**DON'T:**
- ❌ Use Godseeker A2 before Leonardo A2 (wastes extension)
- ❌ Miss Brogni A3 on gap turn (Decrease Speed will break tune)
- ❌ Let Geomancer Weaken drop (damage loss)

---

## 8. Auto Mode: Mithrala Variant

### Why Swap Godseeker for Mithrala?

**Godseeker AI Issues:**
- ❌ Does NOT time A2 properly (extends at wrong turns)
- ❌ Unkillable only 50% uptime instead of 75%
- ❌ Run fails 20-30% of time (Decrease Speed lands during gap)

**Mithrala Auto Benefits:**
- ✅ A3 Cleanse recovers from Decrease Speed (speed tune safety)
- ✅ A3 Shield + Strengthen (additional survivability)
- ✅ AI uses skills correctly (auto-friendly)
- ❌ NO Buff Extension (Leonardo 2-turn Unkillable = 50% uptime)

---

### Auto Team Composition

| Champion | SPD | Role | Priority |
|----------|-----|------|----------|
| Leonardo | 267 | Unkillable/Tank | 5/5 |
| **Mithrala** | 277 | Cleanse/Shield | 4/5 |
| Michelangelo | 270 | Join Attack DPS | 5/5 |
| Brogni | 274 | Block Debuffs | 5/5 |
| Geomancer | 263 | Weaken/HP Burn/Stun | 4/5 |

**Expected Damage:** 50-70M (auto, 90-95% success rate)

**Trade-off:** -20-25M damage vs manual, but reliable auto farming

---

## 9. Build Timeline & Resource Requirements

### Phase 1: Book Farming (Months 1-3)

**Priority:**
1. ✅ **Leonardo:** 7 Legendary books (A2 5→3 CD is MANDATORY)
2. ✅ **Godseeker Aniri:** Full Epic books (already complete)
3. ⚠️ **Michelangelo:** Full Legendary books (recommended for A2 CD + Passive)
4. ⚠️ **Geomancer:** Full Legendary books (recommended for A3 CD)

**Estimated Time:** 2-3 months (monthly events, tournaments, CB chests)

---

### Phase 2: Regearing (Weeks 1-2)

**Priority:**
1. **Michelangelo:** +25 SPD (245→270) - Speed boots + Speed set + SPD substats
2. **Geomancer:** +39 SPD (224→263) - Speed boots + Speed set + SPD substats
3. **Leonardo:** Full build (267 SPD, 3,500 DEF, 100% C.RATE)

**Estimated Time:** 1-2 weeks (gear farming + Great Hall bonuses)

---

### Phase 3: Mastery Completion (Weeks 1-2)

**Priority:**
1. **Leonardo:** Warmaster (DEF scaling)
2. **Michelangelo:** Giant Slayer (A1 2-hit)
3. **Geomancer:** Giant Slayer (A1 2-hit)

**Estimated Time:** 1-2 weeks (Minotaur farming)

---

### Total Timeline: 3-4 Months

**Milestones:**
- **Month 1-2:** Farm Leonardo books (7 Legendary)
- **Month 2-3:** Farm Michelangelo + Geomancer books
- **Month 3:** Regear all champions to 263-280 SPD
- **Month 4:** Mastery completion + testing

**Resource Cost:**
- **Books:** 7 Legendary (Leonardo) + 12-15 Legendary (Mickey/Geo) = ~20-22 Legendary books total
- **Energy:** ~5,000-10,000 for gear farming + masteries
- **Silver:** ~50-100M for gear upgrades

---

## 10. Troubleshooting

### Problem 1: Leonardo Unkillable Only 2 Turns

**Symptoms:** Unkillable shows 2 turns instead of 3

**Fixes:**
1. ✅ Godseeker A2 in Round 2, 8, 14... (immediately after Leonardo A2)
2. ✅ Verify Godseeker books (A2 MUST be 3-turn CD)
3. ✅ If auto: Use Mithrala variant instead

---

### Problem 2: Speed Tune Breaking

**Symptoms:** Boss laps team after ~10 turns

**Fixes:**
1. ✅ Verify ALL champions 263-280 SPD (check in battle, not lobby)
2. ✅ Remove ANY speed lead champions (aura breaks tune calculation)
3. ✅ Check for Decrease Speed debuff (cleanse immediately with Mithrala A3 or reset)

---

### Problem 3: Low Damage (30-40M instead of 70M+)

**Fixes:**
1. ✅ Verify Geomancer ACC 250+ (Weaken MUST land)
2. ✅ Verify 100% C.RATE on Leonardo, Michelangelo, Geomancer
3. ✅ Check affinity (avoid Force boss - Leonardo Void = weak)
4. ✅ Verify Leonardo books (A2 MUST be 3-turn CD for proper rotation)

---

### Problem 4: Team Dies During Gap Turn

**Symptoms:** Champions die on Turn 4, 8, 12...

**Fixes:**
1. ✅ Brogni A3 MUST be cast on Rounds 1, 7, 13, 19... (gap turn coverage)
2. ✅ Verify Brogni books (A3 MUST be 3-turn CD)
3. ✅ Increase Leonardo DEF to 4,000+ (takes Ally Protection damage)
4. ✅ Increase Brogni HP to 70,000+ (shield scaling compensation)

---

### Problem 5: Run Ends at Turn 50

**Symptoms:** Team wipes suddenly at turn 50

**This is EXPECTED:** Boss Gathering Fury ignores Unkillable/Block Damage after turn 50.

**Solutions:**
- ✅ Accept 50-turn limit (this is the cheese trade-off)
- ✅ Maximize damage in first 50 turns (optimize builds, rotation)
- ✅ If need longer runs: Use Tanky Killable team (60-80 turn survivability)

---

## Quick Reference: Build Checklist

**BEFORE STARTING LEONARDO TEAM:**
- [ ] Tanky Killable team hitting 72M+ (1-key secured)
- [ ] Leonardo: 7 Legendary books acquired
- [ ] Leonardo: 267 SPD, 3,500 DEF, 100% C.RATE, Warmaster
- [ ] Godseeker: Fully booked (already complete)
- [ ] Michelangelo: 270 SPD (+25 from current), 100% C.RATE, Giant Slayer
- [ ] Geomancer: 263 SPD (+39 from current), 250 ACC, 100% C.RATE, Giant Slayer
- [ ] Brogni: Fully booked (already complete)
- [ ] 3-5 test runs completed (manual rotation verified)
- [ ] Mithrala variant tested (if auto needed)

**EXPECTED RESULTS:**
- ✅ 70-95M damage (manual, optimal rotation)
- ✅ 50-70M damage (auto with Mithrala)
- ✅ 50-turn consistent survival
- ⚠️ Affinity-dependent (avoid Force boss)

---

**END OF GUIDE - Version 3.0**

**Changes from v2.1:**
- ✅ Removed redundant UNM mechanics (now in `UNM_Clan_Boss_Team_Analysis.md`)
- ✅ Added comparison to current Tanky Killable team
- ✅ Streamlined to Leonardo-specific setup and rotation
- ✅ Added clear build timeline and resource requirements
- ✅ Added auto variant (Mithrala swap) with trade-offs
- ✅ Simplified troubleshooting to Leonardo-specific issues
- ✅ Added "when to transition" decision framework

**Next Steps:**
1. Focus on Tanky Killable optimization (72M+ goal)
2. Farm Leonardo books (7 Legendary - highest priority)
3. Regear Michelangelo + Geomancer when books complete
4. Test manual rotation once all requirements met
