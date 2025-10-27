# HellHades OCR Scraper Design Document

## Purpose
Create a scraper for HellHades champion pages to extract base stats via OCR as an additional validation source alongside Ayumilove and RaidWiki.

## Champion Page Structure
**URL Pattern:** `https://hellhades.com/champions/[champion-slug]/`
Example: `https://hellhades.com/champions/djamarsa/`

## Data to Extract

### Priority 1: Base Stats (via OCR)
- HP, ATK, DEF, SPD
- C.RATE, C.DMG, RES, ACC
- **Image location:** Champion portrait with stat overlay (similar to Ayumilove)
- **OCR target:** Extract stats from champion stats card/overlay

### Priority 2: Champion Info (HTML parsing)
- Faction
- Affinity
- Rarity
- Role
- **HTML location:** Champion header/metadata section

### Priority 3: Skills (HTML parsing - if easy)
- Skill names and descriptions
- Cooldowns
- **HTML location:** Skills section (likely div/table structure)

## Implementation Plan

### Phase 1: Stat OCR
1. Fetch HellHades champion page
2. Locate champion stat image/card
3. Download/process image with Tesseract OCR
4. Parse stats from OCR text (similar to Ayumilove approach)
5. Return normalized stats dict

### Phase 2: Info Validation
1. Parse HTML for faction/affinity/rarity/role
2. Cross-validate with Ayumilove/RaidWiki info
3. Flag mismatches for review

### Phase 3: Integration
1. Add HellHades scraper to `try_all_scrapers()` workflow
2. Three-source validation:
   - **Primary:** Ayumilove (skills + OCR stats)
   - **Validation 1:** RaidWiki (stats text)
   - **Validation 2:** HellHades (OCR stats + info)
3. Confidence scoring based on source agreement:
   - 3/3 sources agree: 100% confidence
   - 2/3 sources agree: 85% confidence
   - 1/3 or all disagree: Flag for manual review

## File Structure
```
Tools/champion_scraper/components/
  scrape_hellhades.py       # New file
  scrape_ayumilove.py        # Existing
  scrape_raidwiki.py         # Existing
```

## Function Signature
```python
def scrape_hellhades_champion(champion_name, skip_stats=False):
    \"\"\"
    Scrape HellHades champion page for stats and info.
    
    Args:
        champion_name: Champion name (e.g., "Djamarsa")
        skip_stats: If True, skip OCR stat extraction (faster)
    
    Returns:
        dict: {
            'info': {'faction', 'affinity', 'rarity', 'role'},
            'stats': {'HP', 'ATK', 'DEF', 'SPD', 'C.RATE', 'C.DMG', 'RES', 'ACC'},
            'skills': [...],  # Optional, Phase 3
            'validation': {'confidence': float, 'sources': str}
        }
        Or None if scraping failed
    \"\"\"
```

## Expected Validation Workflow
```
1. Scrape Ayumilove (primary) → 8/8 stats, skills, info
2. Scrape RaidWiki (validation) → stats text (if available)
3. Scrape HellHades (validation) → OCR stats, info
4. Compare all three:
   - If all 3 match → 100% confidence
   - If 2/3 match → Use majority, 85% confidence
   - If all disagree → Flag for manual review, use Ayumilove (primary)
5. Store validation results in metadata
```

## Implementation Notes
- **Reuse OCR logic** from `scrape_ayumilove.py` (Tesseract + pytesseract)
- **Handle 404/500 errors gracefully** (like RaidWiki scraper)
- **No blocking** - if HellHades fails, continue with Ayumilove/RaidWiki
- **Rate limiting** - add 2-3 sec delay between requests to avoid throttling

## Testing Plan
1. Test HellHades scraper standalone on 5 champions (Legendary/Epic/Rare mix)
2. Compare OCR accuracy vs Ayumilove (expect 70-90% success rate)
3. Test three-source validation workflow on 10 champions
4. Verify faction/affinity/rarity/role accuracy vs known-good data

## Benefits
- ✅ **Third validation source** for stat accuracy
- ✅ **Cross-check faction/affinity** to catch scraper errors (like Djamarsa Barbarians→Demonspawn)
- ✅ **Confidence scoring** based on multi-source agreement
- ✅ **Reduced manual verification** for high-confidence (3/3 match) champions

## Risks/Challenges
- HellHades may have anti-scraping measures (CloudFlare, rate limiting)
- OCR accuracy depends on HellHades image quality/format
- HTML structure may change (requires maintenance)
- Additional scraping time (~2-3 sec per champion)

## Timeline
- **Phase 1 (Stat OCR):** ~30-45 min (scraper + OCR + testing)
- **Phase 2 (Info validation):** ~15-20 min (HTML parsing + testing)
- **Phase 3 (Integration):** ~15-20 min (three-source validation logic)
- **Total:** ~60-90 min for complete implementation

## Decision Point
**Should we implement HellHades scraper now or continue with current 14 champions using Ayumilove-first approach?**

**Recommendation:** 
- **Option A:** Continue with current workflow (Ayumilove-first + RaidWiki validation) for remaining 14 champions (~45-60 min total)
- **Option B:** Implement HellHades scraper first (60-90 min), then process all 14 champions with three-source validation

**User preference?**
