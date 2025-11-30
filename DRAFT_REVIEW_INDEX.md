# Draft and Incomplete File Review Index
**Generated:** 2025-11-30  
**Purpose:** Track all incomplete, draft, or template-filled files requiring review and completion

---

## Summary Statistics

| Category | Count | Status |
|----------|-------|--------|
| **Champion Dictionary (Root - Draft)** | 18 | ⚠️ Needs review/completion |
| **Champion Dictionary (Complete - Draft flag)** | 2 | ⚠️ Needs draft flag removal |
| **Champion Dictionary (Complete)** | 72 | ✅ Complete |
| **Scrape Failed Champions** | 3 | ❌ Needs manual intervention |
| **Low Stat Confidence (<50)** | 8 | ⚠️ Needs stat validation |
| **Champion Intake Queue** | 0 | ✅ Empty |

---

## 1. Champions in Root Directory (Draft Status)

**Location:** `input/Champion_Dictionary/`  
**Issue:** These champions have `draft: true` and are not in Complete/ folder  
**Action Required:** Review, validate, set `draft: false`, move to Complete/

### A. High Priority - Low Stat Confidence (<50)

| Champion | Draft | Stat Confidence | Issue | Priority |
|----------|-------|-----------------|-------|----------|
| **He-Man** | scrape failed | 0 | Scrape failed, needs manual stats | 🔴 HIGH |
| **Leminisi_the_Gold-Wing** | scrape failed | 0 | Scrape failed, needs manual stats | 🔴 HIGH |
| **Ugir_the_Wyrm_Eater** | scrape failed | 0 | Scrape failed, needs manual stats | 🔴 HIGH |
| **Paragon** | true | 0 | No stat validation | 🔴 HIGH |
| **Rian_the_Conjurer** | true | 0 | No stat validation | 🔴 HIGH |
| **Runekeeper_Dazdurk** | true | 0 | No stat validation | 🔴 HIGH |
| **Taurus** | true | 0 | No stat validation | 🔴 HIGH |
| **Visix_the_Unbowed** | true | 0 | No stat validation | 🔴 HIGH |
| **Taya** | true | 25 | Very low stat confidence | 🟡 MEDIUM |

**Notes:**
- **Scrape failed** champions need stats from user screenshot or authoritative source
- **0 stat confidence** may have placeholder stats from template, needs validation
- All have gear/masteries/skills populated, only stats need verification

### B. Medium Priority - High Stat Confidence (87.5-100)

| Champion | Draft | Stat Confidence | Action Required | Priority |
|----------|-------|-----------------|-----------------|----------|
| **Queen_Eva** | true | 100 | Review, set draft: false, move to Complete/ | 🟢 READY |
| **Duedan_the_Runic** | true | 87.5 | Review, set draft: false, move to Complete/ | 🟢 READY |
| **Norog** | true | 87.5 | Review, set draft: false, move to Complete/ | 🟢 READY |
| **Quargan_the_Crowned** | true | 87.5 | Review, set draft: false, move to Complete/ | 🟢 READY |
| **Skeletor** | true | 87.5 | Review, set draft: false, move to Complete/ | 🟢 READY |
| **Ultimate_Galek** | true | 87.5 | Review, set draft: false, move to Complete/ | 🟢 READY |
| **Vergumkaar** | true | 87.5 | Review, set draft: false, move to Complete/ | 🟢 READY |
| **Vrask** | true | 87.5 | Review, set draft: false, move to Complete/ | 🟢 READY |
| **White_Dryad_Nia** | true | 87.5 | Review, set draft: false, move to Complete/ | 🟢 READY |

**Notes:**
- All have comprehensive sections populated (gear, masteries, skills with effects)
- Stats validated to 87.5% or higher confidence
- Ready for final review and promotion to Complete/

---

## 2. Champions in Complete/ Folder (Draft Flag Still Set)

**Location:** `input/Champion_Dictionary/Complete/`  
**Issue:** Files in Complete/ folder but still have `draft: true` flag  
**Action Required:** Set `draft: false` or investigate why draft flag remains

| Champion | Draft | Location | Action Required | Priority |
|----------|-------|----------|-----------------|----------|
| **Uugo** | true | Complete/ | Set draft: false | 🟡 MEDIUM |
| **Apothecary** | true | Complete/ | Set draft: false | 🟡 MEDIUM |

**Notes:**
- These champions are in Complete/ folder, suggesting they were reviewed and approved
- Draft flag should be set to false to mark as finalized
- Quick fix: Set `draft: false` in both files

---

## 3. Scrape Failed Champions (Manual Intervention Required)

**Issue:** Champion scraper failed to retrieve stats from all sources  
**Action Required:** Manual stat collection from user screenshot or authoritative sources

| Champion | Error | Recommended Action |
|----------|-------|-------------------|
| **He-Man** | scrape failed | Request user screenshot of base stats OR verify from Ayumilove/HellHades |
| **Leminisi_the_Gold-Wing** | scrape failed | Request user screenshot of base stats OR verify from Ayumilove/HellHades |
| **Ugir_the_Wyrm_Eater** | scrape failed | Request user screenshot of base stats OR verify from Ayumilove/HellHades |

**Workflow:**
1. Request user provide screenshot of champion base stats screen
2. OR manually look up stats from Ayumilove + HellHades (cross-validate)
3. Update JSON with validated stats
4. Set `stat_confidence: 90` (manual verification) or `100` (user screenshot)
5. Update `validation_metadata.sources` with stat sources
6. Set `draft: false` and move to Complete/

---

## 4. Champion Intake Queue Status

**Location:** `input/Champion_Intake_list.md`  
**Status:** ✅ Empty (no champions queued for processing)

---

## 5. Recommended Completion Order

### Phase 1: Quick Wins (9 champions, ~15 minutes)
**Champions with 87.5-100% stat confidence, comprehensive sections complete**

1. Queen_Eva (100% confidence)
2. Duedan_the_Runic (87.5%)
3. Norog (87.5%)
4. Quargan_the_Crowned (87.5%)
5. Skeletor (87.5%)
6. Ultimate_Galek (87.5%)
7. Vergumkaar (87.5%)
8. Vrask (87.5%)
9. White_Dryad_Nia (87.5%)

**Action:** Review each file, validate JSON, set `draft: false`, move to Complete/

### Phase 2: Draft Flag Cleanup (2 champions, ~2 minutes)
**Champions in Complete/ folder with draft flag still set**

1. Uugo
2. Apothecary

**Action:** Set `draft: false` in both files

### Phase 3: Stat Validation Required (6 champions, ~30-60 minutes)
**Champions with 0% or low stat confidence, needs manual stat collection**

1. Paragon (0% confidence)
2. Rian_the_Conjurer (0%)
3. Runekeeper_Dazdurk (0%)
4. Taurus (0%)
5. Visix_the_Unbowed (0%)
6. Taya (25%)

**Action:** Validate stats from authoritative sources or user screenshots, update stat_confidence, review, set `draft: false`, move to Complete/

### Phase 4: Scrape Failed Recovery (3 champions, ~45-90 minutes)
**Champions where scraper failed, needs manual stats collection**

1. He-Man
2. Leminisi_the_Gold-Wing
3. Ugir_the_Wyrm_Eater

**Action:** Follow File Corruption Recovery Process (Section 7 of copilot-instructions.md):
- Delete corrupted/failed JSON
- Re-run scraper: `python Tools/champion_scraper/champion_scraper.py "Champion Name" --owned 1`
- If scraper fails again, manually populate stats from Ayumilove/HellHades
- Complete comprehensive sections, validate, set `draft: false`, move to Complete/

---

## 6. Validation Checklist (Per Champion)

Before marking any champion as complete (`draft: false`) and moving to Complete/:

- [ ] **Stats validated** (stat_confidence ≥ 90)
- [ ] **All 4 skills populated** with comprehensive effects arrays
- [ ] **Gear recommendations** present and content-specific
- [ ] **Masteries** present with canonical format (reference Masteries.md)
- [ ] **Blessings** recommendations present
- [ ] **Meta ratings** present (1-10 scale for primary content types)
- [ ] **Validation metadata** complete (sources, confidence, author)
- [ ] **JSON validation passes**: `python Tools/Validate/validate_json.py --schema input/Champion_Dictionary/Champion_Name.json`
- [ ] **No duplicate keys** or structural errors
- [ ] **Draft flag set to false**: `"draft": false`
- [ ] **File moved to Complete/**: `Move-Item "input/Champion_Dictionary/Champion_Name.json" "input/Champion_Dictionary/Complete/Champion_Name.json"`
- [ ] **Stats table synced** (if batch complete): `python Tools/champion_scraper/scripts/sync_table_from_json.py`

---

## 7. Next Steps

1. **Decide priority:** Which phase to tackle first (recommend Phase 1 for quick momentum)
2. **User input:** Request screenshots for scrape-failed champions (He-Man, Leminisi, Ugir) if available
3. **Batch processing:** Process Phase 1 champions in single session with batch table sync
4. **Commit strategy:** Commit after each phase completion with clear metrics
5. **Update this index:** After each phase, update statistics and remove completed champions

---

## 8. Files Requiring Template Updates or Review

### Templates Status

| Template | Location | Status | Notes |
|----------|----------|--------|-------|
| Champion_Dictionary_Template.json | input/Templates/ | ✅ Active | Canonical template in use |
| Champion_Dictionary_Schema.json | input/Templates/ | ✅ Active | Validation schema current |
| Champion_Review_Template.md | input/Templates/ | ✅ Updated | Mastery reference added 2025-11-30 |
| Boss_Guide_Template.md | input/Templates/ | ✅ Updated | Section 7 masteries added 2025-11-30 |
| Team_Entry_Template.md | input/Templates/ | ⚠️ Unknown | Needs review for current standards |
| Mechanic_Entry_Template.json | input/Templates/ | ⚠️ Missing | Referenced in copilot-instructions.md but doesn't exist |

**Action Required:**
- Verify Team_Entry_Template.md matches current team building workflow
- Create Mechanic_Entry_Template.json if mechanic dictionary expansion planned
- Review all templates for mastery documentation compliance

---

## 9. Notes and Assumptions

- **Comprehensive sections check:** All 18 draft champions have gear, masteries, and skill effects populated
- **Stat confidence calculation:** Based on validation_metadata.stat_confidence field
- **Scrape failed detection:** Champions with `draft: "scrape failed"` or stat_confidence = 0 AND no stats
- **Complete/ folder:** 72 champions counted, assumed all are finalized (except Uugo/Apothecary with draft flag)
- **Priority rankings:**
  - 🔴 HIGH: Scrape failed or 0% stat confidence (data missing or unvalidated)
  - 🟡 MEDIUM: Low confidence or minor issues (needs validation or flag update)
  - 🟢 READY: High confidence, comprehensive sections complete (ready for final review)

---

## 10. Questions for User

Before proceeding with completion workflow:

1. **Scrape-failed champions:** Do you have screenshots of base stats for He-Man, Leminisi_the_Gold-Wing, or Ugir_the_Wyrm_Eater?
2. **Priority preference:** Which phase should we tackle first? (Phase 1 Quick Wins recommended)
3. **Batch processing:** Should we process all Phase 1 champions in single session, or review one at a time?
4. **Stat validation approach:** For 0% confidence champions, should we validate from Ayumilove/HellHades or wait for user screenshots?
5. **Template review:** Should we audit Team_Entry_Template.md and create Mechanic_Entry_Template.json before champion completion?

