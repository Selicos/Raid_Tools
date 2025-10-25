# OCR Test Images Directory

This directory contains test images for validating and improving OCR stat extraction.

## Directory Structure

```
test_images/
├── README.md (this file)
├── gretel_hagbane.jpg (working example)
├── husk.jpg (partial failure example)
└── ... (add more champion images here)
```

## How to Add Test Images

1. **Download champion image from Ayumilove:**
   - Go to the champion's Ayumilove page
   - Right-click the main champion image (the one with stats in lower right corner)
   - Save as: `champion_name.jpg` (use underscores for spaces)

2. **Place in this directory**

3. **Add to TEST_CHAMPIONS list in test_ocr_validation.py**

## Running Tests

```powershell
# Test a single champion's OCR
C:/GIT/Raid_Tools/.venv/Scripts/python.exe .\Tools\champion_scraper\test_ocr_validation.py --champion "Gretel Hagbane"

# Compare Ayumilove OCR vs RaidWiki stats
C:/GIT/Raid_Tools/.venv/Scripts/python.exe .\Tools\champion_scraper\test_ocr_validation.py --validate "Gretel Hagbane"

# Test all champions in TEST_CHAMPIONS list
C:/GIT/Raid_Tools/.venv/Scripts/python.exe .\Tools\champion_scraper\test_ocr_validation.py --all

# Generate detailed report
C:/GIT/Raid_Tools/.venv/Scripts/python.exe .\Tools\champion_scraper\test_ocr_validation.py --report
```

## Known Issues / Image Layout Variations

### Working (100% accuracy):
- **Gretel Hagbane**: Standard Ayumilove layout, stats in lower right corner, clear OCR

### Partial Failures:
- **Husk**: OCR only extracted HP: 33 (wrong), SPD: 98, RES: 45. Missing ATK, DEF, C.RATE, C.DMG, ACC
  - Issue: Different image layout/formatting

### To Be Tested:
- Add more champions here as you test them

## Improving OCR Extraction

When you find champions with OCR failures:

1. Save their image to this directory
2. Run the validation script to see exact failures
3. Examine the OCR debug output to see what text was extracted
4. Update the OCR extraction logic in `components/scrape_ayumilove.py` to handle the layout variation
5. Re-test until accuracy improves

## Next Steps

1. **Add 5-10 champion images** to build a good test set
2. **Run validation** to identify common OCR failure patterns
3. **Update OCR logic** to handle different image layouts
4. **Re-test** until overall accuracy is >90%
5. **Use RaidWiki as fallback** when OCR fails or accuracy is low
