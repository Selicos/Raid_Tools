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

## Migration Plan for Existing Documentation

### Phase 1: Update All Templates
- [ ] `input/Templates/Champion_Build_detailed.md` - Add mastery reference link
- [ ] `input/Templates/Champion_Review_Template.md` - Simplify mastery section
- [ ] `input/Templates/Boss_Guide_Template.md` - Add canonical mastery reference
- [ ] `input/Templates/Team_Entry_Template.md` - Simplify mastery notes

### Phase 2: Update Active Reviews (Gradual)
- Champion reviews should use simplified format with reference link
- Boss guides should reference mastery file for detailed builds
- Build evaluations should link to mastery file for optimization

### Phase 3: Automation
- Scripts can parse `masteries.json` for recommendations
- Validation scripts can check mastery paths against canonical data
- Auto-generate mastery summaries from JSON for champion entries

---

## Benefits of This Approach

### 1. **Reduce Redundancy**
- Champion reviews: ~50-100 lines reduced per file (mastery tables)
- Boss guides: ~200-300 lines reduced per file (team mastery sections)
- Total: ~2,000-5,000 lines of duplicate content eliminated

### 2. **Single Source of Truth**
- Update mastery description once in `Masteries.md` → all references updated
- Fix mastery mechanics once in `masteries.json` → all automation updated
- No conflicting mastery recommendations across files

### 3. **Easier Maintenance**
- Mastery changes (game patches) only require updating 2 files
- Consistent terminology across all documentation
- Validation scripts can ensure references point to valid masteries

### 4. **Better Readability**
- Reviews focus on champion-specific strategy, not generic mastery tables
- Guides provide actionable mastery paths, not exhaustive tier lists
- Users see "why" and "what" rather than drowning in tier descriptions

---

## Implementation Checklist

### Immediate Actions
- [x] Create this reference guide
- [ ] Update `Masteries.md` with canonical system rules (already done)
- [ ] Validate `masteries.json` structure matches `Masteries.md` content
- [ ] Add mastery reference links to all template files

### Gradual Migration
- [ ] As champion reviews are updated, replace full mastery tables with reference format
- [ ] As boss guides are updated, consolidate repeated mastery sections
- [ ] Update copilot-instructions.md with mastery reference policy

### Future Automation
- [ ] Create script to validate mastery references in documentation
- [ ] Create script to auto-generate mastery summaries from JSON
- [ ] Add mastery validation to champion JSON schema

---

## Example: Before vs After

### ❌ Before (Verbose)
```markdown
## Masteries

### PVE General (Arena, Dungeons, Doom Tower, Faction Wars)

**Offense Tree:**
- T1: Deadly Precision (3/3) - +5% Critical Rate
- T2: Keen Strike (3/3) - +10% critical damage
- T3: Heart of Glory (3/3) - +5% damage when attacking with full health
- T4: Single Out (3/3) - +8% damage to targets with less than 40% HP
- T5: Bring It Down (3/3) - +6% damage when attacking targets with higher max HP
- T5: Methodical (3/3) - +2% damage on default skill each use, stacks across rounds, max +10%
- T6: Warmaster (1/1) - 60% chance of bonus damage: 10% of target's MAX HP (4% for Bosses), once per skill

**Support Tree:**
- T1: Pinpoint Accuracy (3/3) - +10 ACC
- T2: Exalt in Death (3/3) - +3 SPD when ally dies
- T3: Rapid Response (3/3) - +3 SPD when HP is above 50%
- T4: Arcane Celerity (3/3) - +6 SPD when placing a buff
- T4: Lore of Steel (3/3) - +15% set bonuses
- T5: Cycle of Magic (3/3) - 5% chance to reduce skill cooldowns by 1 turn
- T5: Lasting Gifts (3/3) - +25% buff duration
- T6: Master Hexer (3/3) - +25% debuff duration

**Cost:** 800 gems for instant unlock OR farm Minotaur's Labyrinth

**Why this build:**
- **Warmaster:** Required for Clan Boss damage (procs on A1 every turn)
- **Master Hexer:** Extends Poison duration +1 turn (2 turns → 3 turns, critical for Clan Boss)
- **Lasting Gifts:** Extends Continuous Heal +1 turn (2 turns → 3 turns, more healing uptime)
```

### ✅ After (Concise + Reference)
```markdown
## Masteries

**Build:** Warmaster + Master Hexer (Offense + Support)
- **Path:** Deadly Precision → Keen Strike → Single Out → Bring It Down + Methodical → **Warmaster**
- **Support:** Pinpoint Accuracy → Lore of Steel → Cycle of Magic + Lasting Gifts → **Master Hexer**
- **Cost:** 800 gems OR farm Minotaur's Labyrinth
- **Why:** Warmaster (4% MAX HP damage vs bosses) + Master Hexer (extend Poison/Continuous Heal 2→3 turns)
- **Full Details:** [Masteries.md](../../input/Mechanic_Dictionary/Masteries/Masteries.md)

**⚠️ Speed Tune Warning:** Avoid Rapid Response/Arcane Celerity if using Counterattack team
```

**Lines Saved:** 28 lines → 8 lines = **71% reduction**

---

## Questions & Feedback

If you encounter issues with this reference system:
1. Check if the mastery exists in `Masteries.md` and `masteries.json`
2. Verify the mastery name spelling matches the canonical files
3. Update the canonical files if game changes occur
4. Report inconsistencies between `.md` and `.json` files for correction

---

**Last Updated:** 2025-11-30  
**Version:** 1.0  
**Maintained By:** Raid Tools Project
