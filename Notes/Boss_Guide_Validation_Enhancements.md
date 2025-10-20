# Boss Guide Validation Enhancements

**Date:** October 19, 2025  
**Purpose:** Document required validation enhancements for all boss guides based on UNM methodology  
**Champion Validation Status:** 20/20 (100%) ✅

---

## 📋 VALIDATION FINDINGS

### Sand Devil Normal Guide Status

**✅ STRONG AREAS:**
- Comprehensive boss mechanics documentation
- Detailed champion-to-mechanics mapping
- Affinity safety documented in multiple locations
- Multi-line affinity format used in team sections

**❌ MISSING/INCOMPLETE:**
1. **Aura Validation:** No systematic validation of champion auras vs. "in All Battles" requirement
2. **Passive Skill Classification:** Not explicitly documented which champions have passive skills
3. **Source Cross-Validation:** Champion mechanics not cross-validated with 2+ sources
4. **Error Rate Documentation:** No mention of restricted aura error patterns

---

## 🎯 REQUIRED ENHANCEMENTS (All Guides)

### 1. Champion Aura Validation Section

Add new section after "Champion-to-Mechanics Mapping" (Section 2):

```markdown
### 2.X. Champion Aura Validation

**PURPOSE:** Validate all champion auras work in this content (not restricted to Arena/Dungeons only)

| Champion | Aura Stat | Aura Wording | Dungeon Applicable? | Notes |
|----------|-----------|--------------|---------------------|-------|
| Vogoth | +30% DEF | "All Battles" ✅ | YES | Confirmed safe for this dungeon |
| Nogdar | +18% HP (Leech) | "All Battles" ✅ | YES | Confirmed safe for this dungeon |
| Tayrel | +24% DEF | "All Battles" ✅ | YES | Confirmed safe for this dungeon |
| Arbiter | +30% SPD | "Arena" ❌ | NO | Arena-only, DOES NOT WORK here |
| Stag Knight | +24% SPD | "Dungeons" ❌ | NO | Dungeons-only, may not work in Doom Tower |
| Rhazin | +90 RESIST | "Arena" ❌ | NO | Arena-only, DOES NOT WORK here |
```

**VALIDATION SOURCES:**
- Champion aura list: `input/Boss_Guide_Update_Validation_Prompt.md`
- Cross-validated with Ayumilove + HellHades
- Error rate: 40% of champions have restricted auras

**ACTION:** Before recommending any champion as "aura lead", verify aura works in this content.

---

### 2. Passive Skill Documentation

Add subsection to each champion role mapping (Sleep, Healing, Revive, etc.):

**Example for Healing Champions:**

```markdown
| Champion | Affinity | Heal Type | Skill | **Has Passive?** | Passive Effect | Notes |
|----------|----------|-----------|-------|------------------|----------------|-------|
| Vogoth | Magic | Passive Heal | Passive | ✅ YES | Heals ally to 30% HP when hit + 50% Sleep on attacker | Passive-based sustain |
| Bad-el-Kazar | Spirit | AoE HoT | A2 | ✅ YES | Extends debuffs/buffs, Continuous Heal | Passive extends Poison |
| Rector Drath | Spirit | AoE Heal | A2 | ❌ NO | N/A | Active skills only |
```

**PURPOSE:** Identify which champions have passive damage/healing for Patch 4.40/4.70 compatibility.

---

### 3. Source Cross-Validation Notes

Add to end of each champion role table:

```markdown
**VALIDATION SOURCES:**
- Vogoth: Ayumilove + HellHades (confirmed passive Sleep + heal)
- Frozen Banshee: Ayumilove + RaidHQ (confirmed A1 extends debuffs)
- Geomancer: Ayumilove + HellHades (confirmed passive reflects as HP Burn)
```

**REQUIREMENT:** All champion mechanics must be cross-validated with 2+ sources.

---

### 4. Team Aura Leader Documentation

Add to each team's "Detailed Team Recommendations" section:

**Example:**

```markdown
**Aura Leader:**
- **Recommended:** Vogoth (+30% DEF "All Battles" ✅ SAFE)
- **NOT RECOMMENDED:** Arbiter (+30% SPD "Arena" ❌ DOES NOT WORK)
- **Alternative:** Tayrel (+24% DEF "All Battles" ✅ SAFE)
```

**PURPOSE:** Prevent users from setting restricted-aura champions as lead.

---

### 5. Champion Comparison Table Enhancement

Update "Direct Champion Comparisons by Role" (Section 6) to include:

**Example:**

```markdown
| Champion | Affinity | Sleep Skill | Aura | Aura Safe? | Passive? | Owned? |
|----------|----------|-------------|------|------------|----------|--------|
| Gretel | Void | A3 (4 CD) | None | N/A | ❌ NO | ✅ YES |
| Vogoth | Magic | Passive | +30% DEF | ✅ YES | ✅ YES | ✅ YES |
| Criodan | Magic | A3 (4 CD) | Unknown | ⚠️ VERIFY | ❌ NO | ✅ YES |
| Arbiter | Void | None | +30% SPD | ❌ NO (Arena) | ❌ NO | ✅ YES |
```

**PURPOSE:** Quick reference for aura safety, passive skills, and owned status.

---

## 🔧 IMPLEMENTATION WORKFLOW

### Priority Order (Per Guide):

1. **HIGH:** Add Champion Aura Validation section (Section 2.X)
2. **HIGH:** Update team sections with "Aura Leader" subsection
3. **MEDIUM:** Add "Has Passive?" column to all champion tables
4. **MEDIUM:** Add source cross-validation notes
5. **LOW:** Enhance champion comparison tables with aura/passive columns

### Batching Strategy:

- **Batch 1:** Sand Devil (Normal + Hard)
- **Batch 2:** Fire Knight Hard + Dragon Hard
- **Batch 3:** Spider Hard + Ice Golem Hard
- **Batch 4:** Remaining guides (Hydra, Chimera, Shredder, etc.)

---

## 📊 CHAMPION AURA QUICK REFERENCE

**✅ SAFE AURAS (Work in All Content):**
- Tagoar: +24% HP
- Bad-el-Kazar: +30% HP
- Tayrel: +24% DEF
- Vogoth: +30% DEF
- Geomancer: +15% SPD
- Venomage: +15% C.RATE
- Nogdar: +18% HP (Leech)
- Frozen Banshee: +10% HP
- Mithrala: +80 ACC ⭐ **HIGHEST IN GAME**

**❌ RESTRICTED AURAS (Arena/Dungeons Only):**
- Arbiter: +30% SPD (Arena)
- Stag Knight: +24% SPD (Dungeons)
- Rhazin: +90 RESIST (Arena)
- Rector Drath: +33% HP (Arena)
- Brogni: +30% DEF (Arena)
- Narma: +80 ACC (Dungeons)
- Seeker: +20% SPD (Arena)
- Wukong: +30% SPD (Arena)

**⚠️ NO AURAS:**
- Scyl, Godseeker Aniri, Skullcrusher, Ninja, Artak, Fayne

---

## 📝 EXAMPLE ENHANCEMENT (Sand Devil Normal)

### Before (Current):

```markdown
### 4.1. Team 1: Gretel + Godseeker + Geomancer + Bad-el + Deacon

**Core Champions:**
1. **Gretel Hagbane** - Sleep champion (A3 AoE Sleep 75%→100%)
2. **Godseeker Aniri** - Healer + reviver (A2 heal + Continuous Heal, A3 revive all)
...
```

### After (Enhanced):

```markdown
### 4.1. Team 1: Gretel + Godseeker + Geomancer + Bad-el + Deacon

**Aura Leader:**
- **Recommended:** Geomancer (+15% SPD "All Battles" ✅ SAFE)
- **Alternative:** Bad-el-Kazar (+30% HP "All Battles" ✅ SAFE)
- **NOT RECOMMENDED:** Arbiter (+30% SPD "Arena" ❌ DOES NOT WORK)

**Core Champions:**
1. **Gretel Hagbane** - Sleep champion (A3 AoE Sleep 75%→100%) | ❌ NO AURA | ❌ NO PASSIVE
2. **Godseeker Aniri** - Healer + reviver (A2 heal + Continuous Heal, A3 revive all) | ⚠️ NO AURA | ❌ NO PASSIVE
3. **Geomancer** - Passive MAX HP damager (reflects damage as HP Burn) | ✅ AURA SAFE | ✅ HAS PASSIVE
...
```

---

## ✅ VALIDATION CHECKLIST (Per Guide)

- [ ] Section 2.X: Champion Aura Validation added
- [ ] All team sections: "Aura Leader" subsection added
- [ ] All champion tables: "Has Passive?" column added
- [ ] Source cross-validation notes added (2+ sources per champion)
- [ ] Champion comparison tables: Aura/Passive columns added
- [ ] Validation & Simulation Notes: Cross-validation documented
- [ ] Error patterns documented (35-40% restricted aura rate)

---

## 🎯 NEXT STEPS

1. Apply enhancements to Sand Devil Normal (DRAFT)
2. Apply enhancements to Sand Devil Hard (DRAFT)
3. Review DRAFTs with user
4. Promote to FINAL after approval
5. Repeat for Fire Knight, Dragon, Spider, Ice Golem

**Total Estimated Time:** 2-3 hours per guide (comprehensive validation)

---

**END OF VALIDATION ENHANCEMENTS DOCUMENT**
