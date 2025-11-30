# Mastery Reference Guide for Documentation

## Purpose
This guide establishes the **single source of truth** for all mastery information in the Raid Tools repository. All champion reviews, boss guides, and build evaluations should reference these files rather than duplicating mastery details.

---

## Canonical Files

### 1. **Masteries.md** - Human-Readable Reference
- **Location:** `input/Mechanic_Dictionary/Masteries/Masteries.md`
- **Purpose:** Complete mastery system documentation with tables and descriptions
- **Use For:** 
  - Understanding mastery mechanics
  - Copying mastery build recommendations
  - Linking in documentation (e.g., "See Masteries.md for full mastery details")

### 2. **masteries.json** - Machine-Readable Data
- **Location:** `input/Mechanic_Dictionary/Masteries/masteries.json`
- **Purpose:** Structured data for automation and programmatic access
- **Use For:**
  - Automation scripts
  - Validation tools
  - Generating mastery recommendations programmatically

---

## Documentation Standards

### ✅ DO: Reference the Canonical Files

**In Champion Reviews:**
```markdown
## Masteries
**Build:** Warmaster + Master Hexer (Offense + Support trees)
- Full details: See [Masteries.md](../../../input/Mechanic_Dictionary/Masteries/Masteries.md)
- **Cost:** 800 gems OR farm Minotaur's Labyrinth
- **Key Masteries:**
  - **Warmaster (T6 Offense):** 60% chance for 4% MAX HP damage vs bosses
  - **Master Hexer (T6 Support):** +25% debuff duration (2 turns → 3 turns)
  - Bring It Down, Pinpoint Accuracy, Charged Focus
```

**In Boss Guides:**
```markdown
### Masteries
All champions require Defense + Support trees for survivability.
- Full mastery details: [Masteries.md](../../input/Mechanic_Dictionary/Masteries/Masteries.md)
- **Cost:** 800 gems OR farm Minotaur's Labyrinth per champion
- **Key Recommendations:**
  - **Sleep Debuffers:** Evil Eye (T6 Support) for 100% weak hit chance
  - **Healers:** Lasting Gifts (T5 Support) extends buff duration +25%
  - **Tanks:** Defense tree focus (Tough Skin, Blastproof, Delay Death)
```

### ❌ DON'T: Duplicate Full Mastery Tables

**Instead of this:**
```markdown
## Masteries
**Offense Tree (55 scrolls):**
- T1: Deadly Precision (3/3) - +5% Critical Rate
- T2: Keen Strike (3/3) - +10% critical damage
- T3: Heart of Glory (3/3) - +5% damage when attacking with full health
- T4: Single Out (3/3) - +8% damage to targets with less than 40% HP
- T5: Bring It Down (3/3) - +6% damage when attacking targets with higher max HP
- T5: Methodical (3/3) - +2% damage on default skill each use, max +10%
- T6: Warmaster (1/1) - 60% chance of bonus damage: 10% of target's MAX HP (4% for Bosses)

**Support Tree (75 scrolls):**
- T1: Pinpoint Accuracy (3/3) - +10 ACC
- T2: Exalt in Death (3/3) - +3 SPD when ally dies
- ... [15 more lines]
```

**Do this:**
```markdown
## Masteries
**Build:** Warmaster + Master Hexer (Offense + Support trees)
- See [Masteries.md](../../input/Mechanic_Dictionary/Masteries/Masteries.md) for full tier details
- **Cost:** 800 gems OR farm Minotaur's Labyrinth
- **Path:** Deadly Precision → Keen Strike → Heart of Glory → Single Out → Bring It Down + Methodical → Warmaster
- **Why:** Warmaster (4% MAX HP damage vs bosses) + Master Hexer (extend Poison 2→3 turns)
```

---

## Mastery Build Templates

### Template 1: Clan Boss Poisoner
```markdown
**Masteries:** Warmaster + Master Hexer (Offense + Support)
- Path: [Deadly Precision → Keen Strike → Single Out → Bring It Down + Methodical → **Warmaster**] + [Pinpoint Accuracy → Charged Focus → Lore of Steel → Evil Eye + Cycle of Magic → **Master Hexer**]
- Cost: 800 gems OR farm Minotaur's Labyrinth
- Details: [Masteries.md](../../input/Mechanic_Dictionary/Masteries/Masteries.md)
```

### Template 2: Tank/Support
```markdown
**Masteries:** Defense + Support trees
- Key: Tough Skin, Blastproof, Rejuvenation, Shadow Heal, Delay Death, Retribution (Defense) + Pinpoint Accuracy, Lore of Steel, Lasting Gifts (Support)
- Cost: 800 gems OR farm Minotaur's Labyrinth
- Details: [Masteries.md](../../input/Mechanic_Dictionary/Masteries/Masteries.md)
```

### Template 3: Arena Nuker
```markdown
**Masteries:** Helmsmasher (Offense tree)
- Path: Deadly Precision → Keen Strike → Ruthless Ambush → Opportunist → Kill Streak + Blood Shield → **Helmsmasher**
- Cost: 800 gems OR farm Minotaur's Labyrinth
- Details: [Masteries.md](../../input/Mechanic_Dictionary/Masteries/Masteries.md)
```

---

## Quick Reference: Common Mastery Paths

### Clan Boss
- **Poisoner/Debuffer:** Warmaster + Master Hexer
- **Damage Dealer (multi-hit):** Giant Slayer + Master Hexer
- **Tank:** Defense tree + Support (Lasting Gifts)
- **Speed Booster:** ⚠️ Avoid Rapid Response, Arcane Celerity (breaks speed tune)

### Dungeons
- **Wave Clear:** Warmaster/Giant Slayer + Defense tree
- **Boss Killer:** Warmaster + Bring It Down + Evil Eye
- **Support:** Defense + Support (Lasting Gifts, Lore of Steel)

### Arena
- **Nuker:** Helmsmasher + Kill Streak + Ruthless Ambush
- **Control:** Defense + Support (Evil Eye for debuff accuracy)
- **Speed Lead:** Offense + Support (avoid turn meter masteries)

### Doom Tower
- **Boss Specialist:** Warmaster + Defense (Delay Death, Retribution)
- **Debuffer:** Support tree (Evil Eye, Master Hexer)
- **Survivability:** Defense tree (Tough Skin, Blastproof, Rejuvenation, Shadow Heal)

---

## Questions & Feedback

If you encounter issues with this reference system:
1. Check if the mastery exists in `Masteries.md` and `masteries.json`
2. Verify the mastery name spelling matches the canonical files
3. Update the canonical files if game changes occur
4. Report inconsistencies between `.md` and `.json` files for correction

---

**Last Updated:** 2025-11-30  
**Version:** 1.1 (Migration Complete)  
**Maintained By:** Raid Tools Project
