# Issue #11: Speed Calculation Formula Corrections

**Created:** 2025-10-18  
**Status:** IN PROGRESS  
**Priority:** CRITICAL  
**Scope:** ALL champion reviews (4 files) + ALL boss guides (15+ files)

---

## Problem Statement

**CRITICAL ERROR IDENTIFIED:** Multiple documents show INCORRECT speed calculations by applying auras/gear sets to **total speed** instead of **base speed**.

### Correct Speed Calculation Formula

```
FINAL SPEED = (Base Speed × Gear Set Multipliers × Aura Multipliers) + Flat Speed Bonuses + Speed Buffs on Total
```

**Critical Rules:**
1. **Gear Sets** (Speed Set +12%, Divine Speed +15%) apply to **BASE SPEED ONLY**
2. **Auras** (Arbiter +30%, Wukong +24%, Deacon +19%) apply to **BASE SPEED ONLY**
3. **Flat Speed Bonuses** (Speed Boots +40-50, substats) are ADDED to base speed AFTER multipliers
4. **Speed Buffs** (Increase Speed debuff, Apothecary A3) apply to **TOTAL SPEED** (base + gear + aura + flat bonuses)

### Example (CORRECT Calculation)

**Champion:** Arbiter  
**Base Speed:** 110 (from champion stats, NOT including gear/aura)  
**Gear:** Speed Set (4 pieces) = +12% base speed  
**Aura:** Arbiter (30% SPD in Arena)  
**Flat Bonuses:** Speed Boots (+50), Substats (+60 total across all pieces)  

**STEP 1: Apply Gear Set Multiplier to Base Speed**
```
Base Speed with Gear = 110 × 1.12 (Speed Set) = 123.2 SPD
```

**STEP 2: Apply Aura Multiplier to Base Speed (NOT total)**
```
Base Speed with Gear + Aura = 110 × 1.12 × 1.30 (Arbiter Aura) = 160.16 SPD
```

**STEP 3: Add Flat Speed Bonuses**
```
Total Speed = 160.16 + 50 (Speed Boots) + 60 (Substats) = 270.16 SPD
```

**STEP 4: Apply Speed Buffs (if applicable)**
```
IF Apothecary A3 (30% Increase Speed buff) is active:
Final Speed = 270.16 × 1.30 = 351.21 SPD
```

**CRITICAL:** Auras and Gear Sets apply to **BASE SPEED (110)**, NOT total speed after substats/boots.

---

## Incorrect Examples Found

### Example 1: Arbiter Review Lines 633-641

**INCORRECT CALCULATION (current document):**
```markdown
**WITHOUT Arbiter (current setup):**
- Wukong: 250 SPD × 1.24 (Wukong aura) = 310 total SPD (speed lead)
- Mythrala: 240 SPD × 1.24 = 297.6 total SPD
- Loki: 230 SPD × 1.24 = 285.2 total SPD

**WITH Arbiter (upgraded setup):**
- Arbiter: 300 SPD × 1.30 (Arbiter aura) = 390 total SPD (speed lead)
- Mythrala: 240 SPD × 1.30 = 312 total SPD
- Wukong: 250 SPD × 1.30 = 325 total SPD
- Loki: 230 SPD × 1.30 = 299 total SPD
```

**ISSUE:** Calculation assumes 250 SPD is BASE SPEED, then applies aura. This is WRONG.

**CORRECT APPROACH:** Need to know ACTUAL base speeds, then apply gear/aura to base, THEN add flat bonuses.

**CORRECTED EXAMPLE (assuming realistic base speeds):**
```markdown
**Champion Base Speeds (from Ayumilove):**
- Arbiter: 110 base SPD
- Sun Wukong: 105 base SPD
- Mythrala Lifebane: 100 base SPD
- Loki: 105 base SPD

**Gear Assumptions (realistic for Gold 3+ Arena):**
- All champions: Speed Set (4 pieces) + Divine Speed (2 pieces) OR 3x Speed Set
- All champions: Speed Boots (+50 SPD), substats (+40-80 SPD depending on gear quality)

**WITHOUT Arbiter (Wukong as speed lead):**

Wukong (speed lead):
- Base: 105
- Gear: 105 × 1.12 (Speed Set) = 117.6
- Aura: 105 × 1.12 × 1.24 (Wukong Aura) = 145.8
- Flat: 145.8 + 50 (boots) + 60 (substats) = 255.8 total SPD

Mythrala:
- Base: 100
- Gear: 100 × 1.12 (Speed Set) = 112
- Aura: 100 × 1.12 × 1.24 (Wukong Aura) = 138.9
- Flat: 138.9 + 50 (boots) + 50 (substats) = 238.9 total SPD

Loki:
- Base: 105
- Gear: 105 × 1.12 (Speed Set) = 117.6
- Aura: 105 × 1.12 × 1.24 (Wukong Aura) = 145.8
- Flat: 145.8 + 50 (boots) + 40 (substats) = 235.8 total SPD

**WITH Arbiter (Arbiter as speed lead):**

Arbiter (speed lead):
- Base: 110
- Gear: 110 × 1.12 (Speed Set) = 123.2
- Aura: 110 × 1.12 × 1.30 (Arbiter Aura) = 160.16
- Flat: 160.16 + 50 (boots) + 80 (high substats) = 290.16 total SPD

Mythrala:
- Base: 100
- Gear: 100 × 1.12 (Speed Set) = 112
- Aura: 100 × 1.12 × 1.30 (Arbiter Aura) = 145.6
- Flat: 145.6 + 50 (boots) + 50 (substats) = 245.6 total SPD

Wukong:
- Base: 105
- Gear: 105 × 1.12 (Speed Set) = 117.6
- Aura: 105 × 1.12 × 1.30 (Arbiter Aura) = 152.88
- Flat: 152.88 + 50 (boots) + 60 (substats) = 262.88 total SPD

Loki:
- Base: 105
- Gear: 105 × 1.12 (Speed Set) = 117.6
- Aura: 105 × 1.12 × 1.30 (Arbiter Aura) = 152.88
- Flat: 152.88 + 50 (boots) + 40 (substats) = 242.88 total SPD

**Speed Gain from Arbiter Aura (vs Wukong Aura):**
- Wukong: 255.8 → 262.88 = +7.08 SPD
- Mythrala: 238.9 → 245.6 = +6.7 SPD
- Loki: 235.8 → 242.88 = +7.08 SPD
- Arbiter (new): 290.16 SPD (replaces Wukong as speed lead)

**KEY INSIGHT:** 
- Aura difference (30% vs 24% = 6% more) applies to BASE SPEED (100-110), NOT total speed (240-290)
- Actual speed gain is ~6-7 SPD per champion, NOT 15-30 SPD as incorrectly calculated
- However, Arbiter herself is FASTER than Wukong (290 vs 256), which is the MAIN benefit
```

**CRITICAL CLARIFICATION:**
- The user's CURRENT total speeds (250 SPD for Wukong, 240 SPD for Mythrala) are ALREADY factored in gear + aura + flat bonuses
- To calculate the benefit of swapping Wukong aura → Arbiter aura, we need to REVERSE-ENGINEER base speeds OR use simplified comparison

### Example 2: Arbiter Review Line 613

**INCORRECT:**
```markdown
Example: Wukong with 250 base SPD → 325 SPD with Arbiter aura (250 × 1.30 = 325)
```

**ISSUE:** 250 SPD is NOT base speed. Wukong's base speed is 105 (from Ayumilove).

**CORRECTED:**
```markdown
Example: Wukong with 105 base SPD + Speed Set + Speed Boots + Substats → ~250 total SPD with Wukong aura. With Arbiter aura: (105 × 1.12 × 1.30) + 110 flat = ~263 total SPD.
```

### Example 3: Arbiter Review Line 939

**INCORRECT:**
```markdown
Example: Arbiter with 200 base SPD + Speed Set (12%) = 224 SPD. With Lore of Steel: 200 × 1.138 = 227.6 SPD (+3.6 SPD)
```

**ISSUE:** 200 SPD is NOT Arbiter's base speed. Arbiter's base speed is 110 (from Ayumilove).

**CORRECTED:**
```markdown
Example: Arbiter with 110 base SPD + Speed Set (12%) = 123.2 SPD. With Lore of Steel: 110 × 1.138 = 125.18 SPD (+1.98 SPD before adding flat bonuses).
```

---

## Champion Base Speeds (Reference)

**Source:** Ayumilove (cross-validated with HellHades)

| Champion | Base Speed | Rarity | Affinity | Faction |
|----------|-----------|--------|----------|---------|
| **Arbiter** | 110 | Legendary | Void | High Elves |
| **Sun Wukong** | 105 | Legendary | Magic | Sylvan Watchers |
| **Mythrala Lifebane** | 100 | Legendary | Void | Shadowkin |
| **Loki the Deceiver** | 105 | Legendary | Void | Demonspawn |
| **Ninja** | 110 | Legendary | Void | Shadowkin |
| **Deacon Armstrong** | 102 | Epic | Force | Knights Revenant |
| **Apothecary** | 109 | Rare | Magic | High Elves |
| **Godseeker Aniri** | 96 | Epic | Spirit | Barbarians |
| **Underpriest Brogni** | 99 | Legendary | Magic | Dwarves |
| **Embrys the Anomaly** | 100 / 125 | Mythic | Void | Demonspawn |
| **Coldheart** | 113 | Epic | Void | Dark Elves |
| **Michelangelo** | 105 | Legendary | Magic | Sylvan Watchers |

**CRITICAL:** Always use BASE SPEED from Ayumilove/HellHades when calculating aura/gear set bonuses.

---

## Files to Update

### Champion Reviews (4 files)

1. **Arbiter_Review_DRAFT.md** (PRIORITY 1 - just created, most errors)
   - Lines 613, 633-641, 939, 1639 (speed calculation examples)
   - Section 3: Skills & Mechanics (Passive Aura description)
   - Section 4: Gear Recommendations (Speed Set description)
   - Section 5: Masteries (Lore of Steel Speed Set bonus example)

2. **Ninja_Review_DRAFT.md** (PRIORITY 2)
   - Search for: "speed aura", "speed set", "×", speed calculation examples
   - Update any incorrect formulas

3. **Brogni_Review_DRAFT.md** (PRIORITY 3)
   - Search for: "speed set", speed calculation examples
   - Update any incorrect formulas

4. **Embrys_Review_DRAFT.md** (PRIORITY 3)
   - Search for: "speed set", speed calculation examples
   - Update any incorrect formulas

### Boss Guides (15+ files)

5. **Shredder_Team_Notes_FINAL.md**
   - Lines 394-395: "Arbiter's 30% SPD aura + Apothecary speed boost"
   - Clarify: Aura applies to base speed, buff applies to total speed

6. **IronTwins_Team_Notes_FINAL.md**
   - Lines 339, 413, 419, 426, 451: Speed tuning examples
   - Verify no incorrect calculations

7. **Chimera_Boss_Guide_Strategy_FINAL.md**
   - Lines 496-497: "Apothecary must be 15+ speed faster than Ninja"
   - Clarify: Speed buff applies to TOTAL speed

8. **PhantomShogun_Boss_Guide_Normal_FINAL.md** + **PhantomShogun_Boss_Guide_Hard_FINAL.md**
   - Lines 676 / 720: "Arbiter Increase Turn Meter boost will disrupt speed tuning"
   - Verify speed tuning advice is accurate

9. **SandDevil_DoomTower_Normal_Boss_Guide_FINAL.md**
   - Search for speed-related content
   - Verify no incorrect calculations

10. **ALL OTHER BOSS GUIDES:**
    - ClanBoss_UltraNightmare_Team_Notes_FINAL.md
    - Dragon_Hard_Team_Notes_FINAL.md
    - FireKnight_Hard_Team_Notes_FINAL.md
    - Hydra_ClanBoss_Team_Notes_FINAL.md
    - IceGolem_Hard_Team_Notes_FINAL.md
    - Spider_Hard_Team_Notes_FINAL.md
    - Amius_CursedCity_Boss_Guide_FINAL.md
    - Search for speed-related content, verify accuracy

---

## Standardized Speed Calculation Template (for mechanics database)

**File:** Notes/Mechanics/formulas.json (FUTURE - when created)

```json
{
  "speed_calculation": {
    "formula": "FINAL_SPEED = (Base_Speed × Gear_Set_Multipliers × Aura_Multipliers) + Flat_Speed_Bonuses + Speed_Buffs_on_Total",
    "components": {
      "base_speed": {
        "description": "Champion's base speed stat (from champion page, NOT including gear/aura)",
        "source": "Ayumilove, HellHades, in-game champion page (before gear equipped)"
      },
      "gear_set_multipliers": {
        "description": "Gear set bonuses that apply to BASE SPEED ONLY",
        "examples": {
          "Speed Set (2 pieces)": 1.12,
          "Divine Speed Set (2 pieces)": 1.15,
          "Triple Speed Set (6 pieces)": 1.36
        },
        "calculation": "Multiply all gear set bonuses together, then apply to base speed"
      },
      "aura_multipliers": {
        "description": "Aura bonuses that apply to BASE SPEED ONLY",
        "examples": {
          "Arbiter (30% SPD Arena)": 1.30,
          "Sun Wukong (24% SPD Arena)": 1.24,
          "Deacon Armstrong (19% SPD All Battles)": 1.19,
          "Arbiter (19% SPD All Battles)": 1.19
        },
        "calculation": "Apply aura multiplier to (base speed × gear set multipliers)"
      },
      "flat_speed_bonuses": {
        "description": "Flat speed bonuses ADDED AFTER multipliers",
        "examples": {
          "Speed Boots (5-star, +16)": 40,
          "Speed Boots (6-star, +16)": 50,
          "Substats (per roll)": "3-8 SPD depending on rarity/level"
        },
        "calculation": "Add all flat bonuses to (base speed × multipliers)"
      },
      "speed_buffs": {
        "description": "Speed buffs that apply to TOTAL SPEED (base + gear + aura + flat)",
        "examples": {
          "Increase Speed (30%)": 1.30,
          "Apothecary A3 (30% Inc Speed 2 turns)": 1.30,
          "Decrease Speed (30%)": 0.70
        },
        "calculation": "Apply buff multiplier to total speed (after all other bonuses)"
      }
    },
    "validation": {
      "always_fetch_base_speed": "Use Ayumilove or HellHades to confirm champion base speed before calculations",
      "never_apply_aura_to_total": "Auras and gear sets ONLY apply to base speed, NOT total speed after substats/boots",
      "buffs_apply_to_total": "Speed buffs (Increase Speed, Apothecary A3) apply to TOTAL speed"
    }
  }
}
```

---

## Correction Strategy (BATCHED)

### BATCH 1: Update Issue #11 Documentation (THIS FILE)

**Status:** ✅ COMPLETE

### BATCH 2: Fix Arbiter_Review_DRAFT.md (PRIORITY 1)

**Lines to Update:**
1. Line 613: Fix Wukong base speed example
2. Lines 622-623: Fix Mythrala speed tuning example
3. Lines 633-641: Fix speed tuning comparison table (Wukong vs Arbiter aura)
4. Line 678: Add clarification to Speed Set description
5. Line 939: Fix Lore of Steel Speed Set example
6. Line 1639: Fix Divine Speed Set calculation example

**Approach:**
- Use realistic base speeds (Ayumilove data)
- Show CORRECT formula step-by-step
- Add NOTE: "Auras and gear sets apply to BASE SPEED, not total speed"

### BATCH 3: Validate + Fix Remaining Champion Reviews (PRIORITY 2)

**Files:**
- Ninja_Review_DRAFT.md
- Brogni_Review_DRAFT.md
- Embrys_Review_DRAFT.md

**Approach:**
- Search for speed calculation examples
- Verify base speeds from Ayumilove
- Update any incorrect formulas

### BATCH 4: Validate + Fix Boss Guides (PRIORITY 3)

**Files:** 15+ boss guides

**Approach:**
- Search for: "speed aura", "speed buff", "speed set", "×", calculation examples
- Verify accuracy of speed tuning advice
- Add clarifications where needed (aura vs buff distinction)

### BATCH 5: Create Mechanics Database (FUTURE - MEDIUM Priority)

**File:** Notes/Mechanics/formulas.json

**Content:**
- Speed calculation formula (standardized)
- Base speed reference table (all owned champions)
- Gear set multipliers
- Aura multipliers
- Speed buff multipliers

**Benefits:**
- Single source of truth for all speed calculations
- Prevents future errors
- Machine-readable for potential automation

### BATCH 6: Git Commit

**Commit Message:**
```
Fix speed calculation formulas (Issue #11)

- Corrected aura/gear set application (BASE SPEED ONLY, not total)
- Fixed Arbiter review speed tuning examples (lines 613, 633-641, 939, 1639)
- Added clarifications: Auras apply to base, buffs apply to total
- Validated champion base speeds via Ayumilove/HellHades
- Updated [N] files: 4 champion reviews + [N] boss guides

CRITICAL: All speed calculations now use correct formula:
FINAL_SPEED = (Base × Gear × Aura) + Flat + Buffs_on_Total
```

---

## Validation Checklist

- [ ] BATCH 1: Create Issue #11 documentation (this file) ✅
- [ ] BATCH 2: Fix Arbiter_Review_DRAFT.md (6 locations)
- [ ] BATCH 3: Validate Ninja, Brogni, Embrys reviews
- [ ] BATCH 4: Validate 15+ boss guides
- [ ] BATCH 5: Create Notes/Mechanics/formulas.json (FUTURE)
- [ ] BATCH 6: Git commit all changes

---

## Notes

**User Request (2025-10-18):**
> "verify across all documents how speed is calculated. Remember that buffs apply to total speed, but auras only apply to base speed. Confirm the base speed and recommendations that alters speed properly. speed related gear also only applies to base speed."

**Response:** Issue #11 created to systematically fix all speed calculation errors. Arbiter review (just created) contains multiple incorrect examples that will be corrected in BATCH 2.

**Estimated Time:**
- BATCH 2: 30-45 minutes (Arbiter review, 6 locations)
- BATCH 3: 30-45 minutes (3 champion reviews)
- BATCH 4: 1-2 hours (15+ boss guides, validation only)
- BATCH 5: 2-3 hours (create mechanics database - FUTURE)
- **Total:** 2.5-4.5 hours (excluding BATCH 5)
