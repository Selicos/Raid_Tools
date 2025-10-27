"""
Batch OCR Test - Test all champions in Stat_Test folder

This script will:
1. Test OCR extraction for all champion images
2. Compare with RaidWiki where available
3. Generate a detailed accuracy report
4. Identify common OCR failure patterns
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'components'))

from scrape_ayumilove import extract_stats_from_image
from scrape_raidwiki import scrape_raidwiki_champion
from PIL import Image
import pytesseract

# Test champions with known correct stats (from your images)
KNOWN_STATS = {
    "Arbiter": {
        "HP": 21135, "ATK": 1068, "DEF": 1101, "SPD": 110,
        "C.RATE": 15, "C.DMG": 50, "RES": 30, "ACC": 10
    },
    "Artak": {
        "HP": 22140, "ATK": 936, "DEF": 1167, "SPD": 100,
        "C.RATE": 15, "C.DMG": 63, "RES": 30, "ACC": 10
    },
    "Broadmaw": {
        "HP": 18660, "ATK": 1101, "DEF": 958, "SPD": 104,
        "C.RATE": 15, "C.DMG": 50, "RES": 30, "ACC": 0
    },
    "Embrys the Anomaly": {
        "HP": 22140, "ATK": 1101, "DEF": 1277, "SPD": 111,
        "C.RATE": 15, "C.DMG": 50, "RES": 30, "ACC": 20
    },
    "Fenshi": {
        "HP": 16515, "ATK": 1465, "DEF": 738, "SPD": 97,
        "C.RATE": 15, "C.DMG": 60, "RES": 30, "ACC": 0
    },
    "Hotatsu": {
        "HP": 17505, "ATK": 760, "DEF": 1376, "SPD": 96,
        "C.RATE": 15, "C.DMG": 50, "RES": 30, "ACC": 15
    },
    "Husk": {
        "HP": 20970, "ATK": 969, "DEF": 936, "SPD": 98,
        "C.RATE": 15, "C.DMG": 50, "RES": 45, "ACC": 0
    },
    "Kalvalax": {
        "HP": 12720, "ATK": 1663, "DEF": 1068, "SPD": 99,
        "C.RATE": 15, "C.DMG": 63, "RES": 30, "ACC": 10
    },
    "Lady Annabelle": {
        "HP": 20310, "ATK": 881, "DEF": 1068, "SPD": 100,
        "C.RATE": 15, "C.DMG": 50, "RES": 30, "ACC": 15
    },
    "Scyl of the Drakes": {
        "HP": 19980, "ATK": 859, "DEF": 1387, "SPD": 95,
        "C.RATE": 15, "C.DMG": 63, "RES": 40, "ACC": 0
    }
}

# Image URLs from Ayumilove
IMAGE_URLS = {
    "Arbiter": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Arbiter.jpg",
    "Artak": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Artak.jpg",
    "Broadmaw": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Broadmaw.jpg",
    "Embrys the Anomaly": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Embrys_the_Anomaly.jpg",
    "Fenshi": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Fenshi.jpg",
    "Hotatsu": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Hotatsu.jpg",
    "Husk": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Husk.jpg",
    "Kalvalax": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Kalvalax.jpg",
    "Lady Annabelle": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Lady_Annabelle.jpg",
    "Scyl of the Drakes": "https://ayumilove.net/files/games/raid_shadow_legends/champion/Scyl_of_the_Drakes.jpg",
}


def test_ocr_against_known_stats(champion_name):
    """
    Test OCR extraction against known correct stats from images.
    """
    print("=" * 80)
    print(f"Testing: {champion_name}")
    print("=" * 80)
    
    known_stats = KNOWN_STATS.get(champion_name)
    if not known_stats:
        print(f"⚠️  No known stats for {champion_name}")
        return None
    
    image_url = IMAGE_URLS.get(champion_name)
    if not image_url:
        print(f"⚠️  No image URL for {champion_name}")
        return None
    
    # Extract stats via OCR
    print(f"\n🔍 Extracting stats from: {image_url}")
    ocr_stats_raw = extract_stats_from_image(image_url)
    
    # Map to standard format
    stat_mapping = {
        'HP': 'HP',
        'ATK': 'ATK',
        'DEF': 'DEF',
        'SPD': 'SPD',
        'C. RATE': 'C.RATE',
        'C. DMG': 'C.DMG',
        'RESIST': 'RES',
        'ACC': 'ACC'
    }
    
    ocr_stats = {}
    for ocr_key, standard_key in stat_mapping.items():
        if ocr_key in ocr_stats_raw:
            try:
                ocr_stats[standard_key] = int(ocr_stats_raw[ocr_key])
            except (ValueError, TypeError):
                ocr_stats[standard_key] = None
        else:
            ocr_stats[standard_key] = None
    
    # Compare
    print("\n📊 Stat Comparison:")
    print("-" * 80)
    print(f"{'Stat':<10} | {'Known (Image)':<15} | {'OCR Extracted':<15} | {'Match':<10}")
    print("-" * 80)
    
    matches = 0
    total = 0
    missing = 0
    incorrect = 0
    
    for stat in ['HP', 'ATK', 'DEF', 'SPD', 'C.RATE', 'C.DMG', 'RES', 'ACC']:
        known_val = known_stats.get(stat, 0)
        ocr_val = ocr_stats.get(stat)
        
        total += 1
        
        if ocr_val is None:
            status = "❌ MISSING"
            missing += 1
        elif ocr_val == known_val:
            status = "✅ MATCH"
            matches += 1
        else:
            status = f"❌ WRONG"
            incorrect += 1
        
        print(f"{stat:<10} | {str(known_val):<15} | {str(ocr_val if ocr_val is not None else ''):<15} | {status}")
    
    accuracy = (matches / total) * 100 if total > 0 else 0
    print("-" * 80)
    print(f"✅ Correct: {matches}/{total}")
    print(f"❌ Missing: {missing}/{total}")
    print(f"❌ Wrong: {incorrect}/{total}")
    print(f"📈 Accuracy: {accuracy:.1f}%")
    
    return {
        'champion': champion_name,
        'matches': matches,
        'missing': missing,
        'incorrect': incorrect,
        'total': total,
        'accuracy': accuracy,
        'ocr_stats': ocr_stats,
        'known_stats': known_stats
    }


def test_all_champions():
    """
    Test all champions and generate summary report.
    """
    results = []
    
    for champion_name in KNOWN_STATS.keys():
        result = test_ocr_against_known_stats(champion_name)
        if result:
            results.append(result)
        print("\n")
    
    # Summary
    print("=" * 80)
    print("OVERALL SUMMARY")
    print("=" * 80)
    
    total_accuracy = sum(r['accuracy'] for r in results) / len(results) if results else 0
    perfect_count = sum(1 for r in results if r['accuracy'] == 100)
    good_count = sum(1 for r in results if 75 <= r['accuracy'] < 100)
    poor_count = sum(1 for r in results if r['accuracy'] < 75)
    
    print(f"\nTested Champions: {len(results)}")
    print(f"✅ Perfect (100%): {perfect_count}")
    print(f"⚠️  Good (75-99%): {good_count}")
    print(f"❌ Poor (<75%): {poor_count}")
    print(f"\n📈 Average Accuracy: {total_accuracy:.1f}%")
    
    print("\n" + "=" * 80)
    print("CHAMPION BREAKDOWN")
    print("=" * 80)
    
    for result in sorted(results, key=lambda x: x['accuracy'], reverse=True):
        accuracy = result['accuracy']
        if accuracy == 100:
            status = "✅"
        elif accuracy >= 75:
            status = "⚠️ "
        else:
            status = "❌"
        
        print(f"{status} {result['champion']:<30} : {result['matches']}/{result['total']} ({accuracy:.1f}%) " +
              f"[Missing: {result['missing']}, Wrong: {result['incorrect']}]")
    
    # Pattern analysis
    print("\n" + "=" * 80)
    print("COMMON FAILURE PATTERNS")
    print("=" * 80)
    
    stat_failures = {}
    for result in results:
        for stat in ['HP', 'ATK', 'DEF', 'SPD', 'C.RATE', 'C.DMG', 'RES', 'ACC']:
            known_val = result['known_stats'].get(stat, 0)
            ocr_val = result['ocr_stats'].get(stat)
            
            if ocr_val is None or ocr_val != known_val:
                if stat not in stat_failures:
                    stat_failures[stat] = 0
                stat_failures[stat] += 1
    
    print("\nStats with Most Failures:")
    for stat, count in sorted(stat_failures.items(), key=lambda x: x[1], reverse=True):
        failure_rate = (count / len(results)) * 100
        print(f"  {stat}: {count}/{len(results)} failures ({failure_rate:.1f}%)")
    
    return results


if __name__ == "__main__":
    print("🧪 Batch OCR Testing - Champion Stats Validation")
    print("=" * 80)
    print("This will test OCR extraction against known correct stats from images")
    print("=" * 80)
    print()
    
    results = test_all_champions()
    
    print("\n✅ Testing complete! Check results above.")
