"""
Test OCR extraction on a specific champion image
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'components'))

from scrape_ayumilove import extract_stats_from_image

# Gretel Hagbane's image URL
image_url = "https://ayumilove.net/files/games/raid_shadow_legends/champion/Gretel_Hagbane.jpg"

print(f"Testing OCR on: {image_url}")
print("-" * 60)

stats = extract_stats_from_image(image_url)

if stats:
    print("\n✅ OCR Extraction Results:")
    print("-" * 60)
    for stat, value in stats.items():
        print(f"{stat:12} : {value}")
else:
    print("\n❌ No stats extracted")
    print("Make sure you have installed:")
    print("  1. pip install pillow pytesseract")
    print("  2. Tesseract OCR binary from:")
    print("     https://github.com/UB-Mannheim/tesseract/wiki")
