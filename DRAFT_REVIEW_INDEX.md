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

### ALL 18 CHAMPIONS: SCRAPER DRAFTS - NEED FULL COMPLETION WORKFLOW

**CRITICAL DISCOVERY:** All 18 champions in root directory are **SCRAPER DRAFTS ONLY**. They have:
- ✅ Base stats populated (varying confidence levels)
- ✅ Skill names and descriptions scraped from sources
- ❌ **Template placeholders in skill effects arrays** (not populated with actual effects)
- ❌ **Meta ratings still "X/10"** (not evaluated)
- ❌ **Empty A4/A5 skill slots** (need removal)
- ❌ **No comprehensive sections** (gear, masteries, blessings, strategies likely template text)

**NONE are ready for promotion to Complete/.** All require **full Section 7 workflow completion**:
1. Fix/validate stats (per stat confidence level)
2. Remove empty skill slots (A4/A5)
3. Populate all skill effects arrays with comprehensive data
4. Add meta ratings for all content types
5. Add gear/masteries/blessings recommendations
6. Add strategies and mechanics tags
7. Validate JSON schema
8. Set draft: false
9. Move to Complete/

---

### Completion Priority by Stat Status

#### Group A: Stats Ready - Need Comprehensive Content (11 champions)

| Champion | Stat Confidence | Stats Status | Action Required | Est. Time |
|----------|-----------------|--------------|-----------------|-----------|
| **Queen_Eva** | 100 | ✅ Validated | Full Section 7 workflow | ~25-30 min |
| **Duedan_the_Runic** | 87.5 | ✅ Good | Full Section 7 workflow | ~25-30 min |
| **Norog** | 87.5 | ✅ Good | Full Section 7 workflow | ~25-30 min |
| **Quargan_the_Crowned** | 87.5 | ✅ Good | Full Section 7 workflow | ~25-30 min |
| **Skeletor** | 87.5 | ✅ Good | Full Section 7 workflow | ~25-30 min |
| **Ultimate_Galek** | 87.5 | ✅ Good | Full Section 7 workflow | ~25-30 min |
| **Vergumkaar** | 87.5 | ✅ Good | Full Section 7 workflow | ~25-30 min |
| **Vrask** | 87.5 | ✅ Good | Full Section 7 workflow | ~25-30 min |
| **White_Dryad_Nia** | 87.5 | ✅ Good | Full Section 7 workflow | ~25-30 min |
| **He-Man** | 0 → 100 | ✅ User screenshot provided | Update stats, then full workflow | ~30-35 min |
| **Leminisi_the_Gold-Wing** | 0 → 100 | ✅ User screenshot provided | Update stats, then full workflow | ~30-35 min |

**Total: ~5.5 hours for Group A**

#### Group B: Stats Need Validation - Then Comprehensive Content (6 champions)

| Champion | Stat Confidence | Stats Status | Action Required | Est. Time |
|----------|-----------------|--------------|-----------------|-----------|
| **Paragon** | 0 | ❌ Needs validation | Validate stats from sources, then full workflow | ~35-40 min |
| **Rian_the_Conjurer** | 0 | ❌ Needs validation | Validate stats from sources, then full workflow | ~35-40 min |
| **Runekeeper_Dazdurk** | 0 | ❌ Needs validation | Validate stats from sources, then full workflow | ~35-40 min |
| **Taurus** | 0 | ❌ Needs validation | Validate stats from sources, then full workflow | ~35-40 min |
| **Visix_the_Unbowed** | 0 | ❌ Needs validation | Validate stats from sources, then full workflow | ~35-40 min |
| **Taya** | 25 | ⚠️ Low confidence | Validate stats from sources, then full workflow | ~35-40 min |

**Total: ~3.5-4 hours for Group B**

#### Group C: Ignored Per User Request (1 champion)

| Champion | Stat Confidence | Stats Status | Action Required |
|----------|-----------------|--------------|-----------------|
| **Ugir_the_Wyrm_Eater** | 0 | ⏸️ Ignored | User requested skip |

**Notes:**
- **Group A** champions can start Section 7 workflow immediately
- **Group B** champions need stats from Ayumilove/HellHades before starting workflow
- **He-Man & Leminisi** have user screenshots - update stats first, then proceed as Group A
- All time estimates based on optimized Section 7 workflow (~25 operations, ~2-3 min per champion for data gathering + 20-25 min for comprehensive content)

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

### Immediate Next Steps

**User has provided screenshots for:**
1. **He-Man** - Update stats from screenshot, then start Section 7 workflow
2. **Leminisi_the_Gold-Wing** - Update stats from screenshot, then start Section 7 workflow

**Recommended approach:**
1. Update He-Man & Leminisi stats from screenshots (~5 min)
2. Pick ONE champion from Group A to complete first (test full workflow) (~25-30 min)
3. After successful completion, batch process remaining Group A champions
4. Move to Group B after Group A complete

### Full Completion Phases

**Phase 1: Update Screenshot Stats (2 champions, ~5 minutes)**
1. He-Man (update from user screenshot)
2. Leminisi_the_Gold-Wing (update from user screenshot)

**Phase 2: Test Full Workflow (1 champion, ~30 minutes)**
- Pick ONE Group A champion (recommend Queen_Eva - 100% stat confidence)
- Complete full Section 7 workflow start-to-finish
- Validate process works correctly
- Document any issues or refinements needed

**Phase 3: Batch Group A (10 champions, ~4-5 hours)**
- Process all Group A champions using validated workflow
- Can parallelize data gathering (Ayumilove + HellHades fetches)
- Batch commit every 3-5 champions

**Phase 4: Group B Stat Validation (6 champions, ~1 hour)**
- Research and validate stats from Ayumilove/HellHades
- Update stat_confidence to 90+
- Prepare for Section 7 workflow

**Phase 5: Batch Group B (6 champions, ~3-4 hours)**
- Process all Group B champions using validated workflow
- Batch commit every 3-5 champions

**Total Time Estimate: ~9-11 hours** (can be spread across multiple sessions)

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

